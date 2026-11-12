#!/bin/bash
# Stop 훅: AI 턴이 끝날 때마다 변경사항을 자동 커밋·푸시한다.
# 클라우드 세션은 컨테이너가 사라지면 작업도 사라지므로, 앱을 그냥 닫아도 작업이 남게 하는 안전망.
#
#   - 클라우드 세션에서만 동작. 로컬에서 켜려면: export HF_STUDY_AUTOSAVE=1
#   - main에는 직접 푸시하지 않는다. main 위에서 변경이 생기면 autosave/<시각> 브랜치로 옮겨 저장.
#   - 병합·리베이스 중이면 아무것도 안 한다.
#   - 비밀처럼 보이는 파일, 5MB 넘는 파일은 커밋에서 뺀다.
# 실패해도 세션을 막지 않는다 (항상 exit 0).
set -uo pipefail

cat >/dev/null 2>&1 || true   # 훅 입력(JSON)은 쓰지 않음

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ] && [ "${HF_STUDY_AUTOSAVE:-}" != "1" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

gitdir="$(git rev-parse --git-dir)"
if [ -e "$gitdir/MERGE_HEAD" ] || [ -d "$gitdir/rebase-merge" ] || [ -d "$gitdir/rebase-apply" ]; then
  exit 0
fi

with_timeout() {
  if command -v timeout >/dev/null 2>&1; then timeout "$@"; else shift; "$@"; fi
}

branch="$(git branch --show-current)"
[ -n "$branch" ] || exit 0   # detached HEAD면 건드리지 않음

if [ -n "$(git status --porcelain)" ]; then
  if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
    branch="autosave/$(date +%Y%m%d-%H%M%S)"
    git switch --quiet -c "$branch" || exit 0
  fi

  git add -A

  # 안전장치: 비밀처럼 보이는 파일 / 큰 파일은 스테이징에서 뺀다
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    base="$(basename "$f")"
    size="$(wc -c <"$f" 2>/dev/null || echo 0)"
    case "$base" in
      .env|.env.*) [ "$base" = ".env.example" ] || { git reset --quiet -- "$f"; echo "autosave: 비밀 의심 파일 제외 — $f"; continue; } ;;
      *.pem|*.key|id_rsa*|*credentials*.json) git reset --quiet -- "$f"; echo "autosave: 비밀 의심 파일 제외 — $f"; continue ;;
    esac
    if [ "$size" -gt 5242880 ]; then
      git reset --quiet -- "$f"; echo "autosave: 5MB 초과 파일 제외 — $f"
    fi
  done < <(git diff --cached --name-only --diff-filter=AM)

  if ! git diff --cached --quiet; then
    files="$(git diff --cached --name-only | head -3 | tr '\n' ' ')"
    count="$(git diff --cached --name-only | wc -l | tr -d ' ')"
    git commit --quiet -m "wip(autosave): ${count}개 파일 — ${files% }" || exit 0
  fi
fi

# 브랜치에 푸시 안 된 커밋이 있으면 푸시 (main은 제외: main 반영은 /wrap-up에서)
if [ "$branch" != "main" ] && [ "$branch" != "master" ]; then
  upstream_ahead=1
  if git rev-parse --verify --quiet "origin/$branch" >/dev/null; then
    upstream_ahead="$(git rev-list --count "origin/$branch..HEAD" 2>/dev/null || echo 1)"
  fi
  if [ "$upstream_ahead" != 0 ]; then
    if with_timeout 30 git push --quiet -u origin "$branch" 2>/dev/null; then
      echo "autosave: $branch 에 저장·푸시함"
    else
      echo "autosave: 푸시 실패 (로컬 커밋은 남아 있음, 다음 턴에 재시도)"
    fi
  fi
fi

exit 0
