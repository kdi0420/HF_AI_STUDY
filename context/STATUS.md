# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-15 (Unit 1 ~ Observe 완료, TAO 이론 끝)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영

## 지금 초점

- **Unit 1** 진행 중 (14개 중 10개 완료). Observe까지 끝 = TAO 이론 끝(에러 관찰 → 재시도 데모 `code/observe_adapt_demo.py`). 다음: **Dummy Agent Library**(첫 코딩 실습) — 원문 붙여 주면 **처음부터 자세히** 설명. 여기서부터 HF 토큰 필요
- Unit 0 완료(2026-11-12). 집 데스크탑에 Ollama + `qwen3.5:9b` 로컬 실행 환경 있음(100% GPU, smolagents 연결 확인)

## 다음 할 일

- [ ] **Dummy Agent Library**부터 재개 → First Agent with smolagents. (Messages·Tools·TAO·ReAct·Actions·Observe 노트의 "내 말로:" 칸도 사용자 말로 채우기)
- [ ] What is an Agent? 노트의 "내 말로:" 칸 채우기 (사용자 말로)
- [ ] Unit 1 실습 직전: HF 토큰 발급(Settings → Access Tokens → **Read**, 원문 지시). 쓰는 곳: Dummy Agent(`HF_TOKEN` 환경변수, 모델 `moonshotai/Kimi-K2.5`) · smolagents 튜토리얼(복제한 Space의 Secret `HF_TOKEN`, 모델 `Qwen/Qwen2.5-Coder-32B-Instruct`). 데스크탑은 `.env`, 클라우드 세션은 `request_credential`(환경 비밀, huggingface.co용). 개인 환경 "기본값"에 `huggingface.co`·`router.huggingface.co` 허용됨
- [ ] Unit 1 실습: dummy agent → smolagents로 Alfred(템플릿 Space 복제) → 최종 퀴즈. 튜토리얼의 `load_tool(..., trust_remote_code=True)`는 실행 전 승인표 필요. HF 크레딧이 떨어지면 데스크탑 Ollama(`ollama_chat/qwen3.5:9b`)로 교체
- [ ] (낮은 우선순위) Meta Llama 접근 신청: What are LLMs? 끝 노트북에만 필요. 다음 섹션들은 Llama를 안 씀
- [ ] (선택) 라이브 1 앞 15~20분 훑기 · `gemma4:12b`와 비교 · `ollama launch`로 로컬 코딩 에이전트 체험

## 사용자 결정 대기

- Unit 1 목표일 11/15가 지남 → 새 목표일 (Todoist "Unit 1" 할 일 날짜도 같이)

- Unit 2~4 목표일(11/22 · 11/29 · 12/6)은 "1주 1유닛" 계산값 → 친구와 편하게 연락해서 확정 (AI가 챙길 일 아님)
- 이 레포를 친구와 공유할지 (공유하면 GitHub collaborator 초대)

## 데스크탑 메모

- 레포 위치: `문서\HF_AI_STUDY` (clone 완료). 쓸 때마다 `git pull`. 데스크탑에서는 실행만, 파일 수정은 AI에게
- Unit 0 실습 venv: `units\unit0-onboarding\code\.venv` (활성화 `.venv\Scripts\Activate.ps1`)

## 최근 세션 (최신 3개, 전체는 SESSION-LOG.md)

- 2026-11-15 (2): Messages and Special Tokens · What are Tools? · Quick Quiz 2(5/5) · Thought–Action–Observation 사이클. 입문자용 상세 설명 + 코드 직접 실행(채팅 템플릿, `@tool`, 루프 데모)
- 2026-11-15: Unit 1 소개 · What is an Agent? · Quick Quiz 1(6/6) · What are LLMs? 공부, 토크나이저 직접 실험
- 2026-11-12: Ollama 데스크탑 설치(`qwen3.5:9b`, 100% GPU) + smolagents 연결 확인, Unit 0 완료
