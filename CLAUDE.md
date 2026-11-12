@AGENTS.md
@context/USER.md
@context/STATUS.md

# Claude Code 전용 메모

공통 규칙은 위의 `AGENTS.md`가 단일 원천이다. 여기에는 Claude Code에만 해당하는 내용만 둔다.
교훈은 이 파일이 아니라 `AGENTS.md`의 "교훈" 섹션에 추가한다.

## 자동으로 일어나는 일 (`.claude/settings.json`의 훅)

- **세션 시작**: `.claude/hooks/session-start.sh`가 origin과 동기화하고, main에 안 합쳐진 이전 세션 작업을 알려준다.
- **턴 종료**: `.claude/hooks/autosave.sh`가 변경사항을 `wip(autosave)`로 커밋하고 현재 브랜치에 푸시한다 (클라우드 세션만).

## 레포 전용 스킬 (`.claude/skills/`)

| 명령 | 언제 |
|---|---|
| `/new-unit <번호·주제>` | 새 유닛 시작 ("유닛2 시작하자") |
| `/wrap-up` | 공부 마무리: 노트·진도표·STATUS·로그 갱신, main 반영 |
