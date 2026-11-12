#!/bin/bash
# SessionStart 훅: 이전 세션에서 이어받을 정보를 에이전트 컨텍스트에 출력한다.
#   - origin과 동기화 (main이 깨끗하고 뒤처져 있으면 fast-forward)
#   - main에 아직 합쳐지지 않은 브랜치 = 이전 세션의 미완료 작업 목록
#   - 그 중 가장 최근 브랜치의 context/STATUS.md가 다르면 그 내용도 출력
# 읽기·동기화만 하고, 실패해도 세션 시작을 막지 않는다.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

with_timeout() {
  if command -v timeout >/dev/null 2>&1; then timeout "$@"; else shift; "$@"; fi
}

fetch_ok=1
with_timeout 20 git fetch --quiet --prune origin 2>/dev/null || fetch_ok=0

base="origin/main"
git rev-parse --verify --quiet "$base" >/dev/null || base="main"

branch="$(git branch --show-current)"
dirty="$(git status --porcelain | wc -l | tr -d ' ')"

echo "## 세션 인계 정보 (session-start 훅)"
echo "- 현재 브랜치: ${branch:-(detached)} / 커밋 안 된 변경: ${dirty}개"
[ "$fetch_ok" = 1 ] || echo "- ⚠️ origin fetch 실패: 원격 상태가 최신이 아닐 수 있음"

# main 위에 있고, 깨끗하고, 뒤처져 있으면 자동으로 따라잡는다
if [ "$branch" = "main" ] && [ "$dirty" = 0 ] && [ "$base" = "origin/main" ]; then
  behind="$(git rev-list --count main..origin/main 2>/dev/null || echo 0)"
  if [ "$behind" -gt 0 ] && git merge --ff-only --quiet origin/main 2>/dev/null; then
    echo "- main을 origin/main으로 동기화함 (+${behind}커밋)"
  fi
fi

# main에 합쳐지지 않은 원격 브랜치 = 이전 세션의 미완료 작업
unmerged=()
while IFS='|' read -r ref date subject; do
  case "$ref" in origin|origin/HEAD|origin/main) continue ;; esac
  ahead="$(git rev-list --count "$base..$ref" 2>/dev/null || echo 0)"
  [ "$ahead" -gt 0 ] || continue
  mark=""; [ "$ref" = "origin/$branch" ] && mark=" ← 현재 브랜치"
  unmerged+=("- \`${ref#origin/}\` (+${ahead}커밋, ${date}) \"${subject}\"${mark}")
done < <(git for-each-ref --sort=-committerdate \
           --format='%(refname:short)|%(committerdate:relative)|%(subject)' refs/remotes/origin)

if [ "${#unmerged[@]}" -gt 0 ]; then
  echo ""
  echo "### main에 아직 합쳐지지 않은 작업 (최근 순, 최대 5개)"
  printf '%s\n' "${unmerged[@]:0:5}"
  echo ""
  echo "→ AGENTS.md '세션 프로토콜'에 따라: 사용자 첫 요청에 답하기 전에 이 사실을 한 줄로 알리고,"
  echo "  이어서 할지 / main에 합칠지 물어본다."

  # 가장 최근 미병합 브랜치의 STATUS.md가 지금 것과 다르면 보여준다
  latest="$(printf '%s\n' "${unmerged[0]}" | sed -E 's/^- `([^`]+)`.*/\1/')"
  if [ "origin/$latest" != "origin/$branch" ] &&
     remote_status="$(git show "origin/$latest:context/STATUS.md" 2>/dev/null)" &&
     [ "$remote_status" != "$(cat context/STATUS.md 2>/dev/null)" ]; then
    echo ""
    echo "### \`$latest\` 브랜치의 최신 context/STATUS.md (지금 로드된 것보다 새것일 수 있음)"
    echo '```markdown'
    printf '%s\n' "$remote_status"
    echo '```'
  fi
fi

exit 0
