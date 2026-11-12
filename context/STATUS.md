# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-12 (Unit 0 완료)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영

## 지금 초점

- **Unit 1** 시작, 목표 **11/15** → 끝나면 기초 인증서.
- Unit 0 완료(2026-11-12). 덤으로 집 데스크탑에 Ollama + `qwen3.5:9b` 로컬 실행 환경 구축(100% GPU, smolagents 연결 확인).

## 다음 할 일

- [ ] Unit 1 섹션 순서대로 `units/unit1-intro-agents/notes.md` 채우기 (목차·링크는 원문과 대조 완료). 1번 "What is an Agent?"부터
- [ ] Unit 1 실습 직전: HF 토큰 발급(Settings → Access Tokens → Read). 클라우드 세션에선 `request_credential`로 환경 비밀(huggingface.co용)에 저장 — 컨테이너가 매번 새로 만들어져서 `.env`는 세션마다 사라짐. 개인 환경 "기본값"에 `huggingface.co`·`router.huggingface.co`는 허용돼 있음(2026-11-12 확인)
- [ ] Unit 1 실습: dummy agent → smolagents로 Alfred 만들기 → HF Space 배포 → 최종 퀴즈. HF 크레딧이 떨어지면 데스크탑 Ollama(`ollama_chat/qwen3.5:9b`)로 교체
- [ ] (선택) 라이브 1 앞 15~20분 훑기 · `gemma4:12b`와 비교 · `ollama launch`로 로컬 코딩 에이전트 체험

## 사용자 결정 대기

- Unit 2~4 목표일(11/22 · 11/29 · 12/6)은 "1주 1유닛" 계산값 → 친구와 편하게 연락해서 확정 (AI가 챙길 일 아님)
- 이 레포를 친구와 공유할지 (공유하면 GitHub collaborator 초대)

## 데스크탑 메모

- 레포 위치: `문서\HF_AI_STUDY` (clone 완료). 쓸 때마다 `git pull`. 데스크탑에서는 실행만, 파일 수정은 AI에게
- Unit 0 실습 venv: `units\unit0-onboarding\code\.venv` (활성화 `.venv\Scripts\Activate.ps1`)

## 최근 세션 (최신 3개, 전체는 SESSION-LOG.md)

- 2026-11-12: Ollama 데스크탑 설치(`qwen3.5:9b`, 100% GPU) + smolagents 연결 확인, Unit 0 완료
- 2026-11-12: Unit 0 온보딩 진행 (계정·팔로우·Discord), Ollama(Step 5) 정리
- 2026-11-12: AI_playground에서 HF 공부 폴더 설계 → 이 저장소로 독립
