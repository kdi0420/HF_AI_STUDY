# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-22 (**Unit 2 진행중**, Tools 원문 설명·실습 노트북 `tools_ollama.ipynb` main 반영 → 데스크탑 실행 대기)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영. **데스크탑에서 실행할 파일은 만들자마자 main에 반영**(사용자 승인 하에)해야 `git pull`로 받아짐

## 지금 초점

- **Unit 2 (프레임워크) 진행중** (2026-11-19 시작): `units/unit2-frameworks/`. 0. 소개(프레임워크 정의·6가지, 노트 0번) → 1. Introduction to smolagents(2.1 목차 7개·RAG, 노트 1번) → 2. Why Use smolagents(장점 4·모델 클래스 5, 노트 2번) → 3. CodeAgents(동작 과정·예제 3개·Hub 공유·Langfuse, 노트 3번) 읽고 11-22 전체 복습, "내 말로" 채움. **데스크탑 실습 노트북 전부 완료**. Langfuse는 선택(안 함)
- Unit 1 완료 (2026-11-16, 기초 인증서). Conclusion 원문·한 페이지 요약 다듬기는 아직
- 환경: 집 데스크탑 Ollama + `qwen3.5:9b`(100% GPU). Unit 2는 **새 venv** `units\unit2-frameworks\code\.venv` (requirements.txt는 smolagents부터, LlamaIndex·LangGraph는 그 섹션에서 추가). 2026-11-22 데스크탑에서 만들고 설치 완료

## 다음 할 일

- [ ] **Tools 실습**: `units/unit2-frameworks/code/tools_ollama.ipynb` (2026-11-22 만듦, 가짜 모델로 검증, main 반영) → 데스크탑에서 `git pull` 후 같은 venv로 0~7단계(8단계는 읽기만), 결과 붙여 주면 분석(5-B 없는 테마에 모델 반응, 7-B 입력창). 그다음 노트 5번 "내 말로"
- [ ] **Unit 2.1 다음 섹션**: [Retrieval Agents](https://huggingface.co/learn/agents-course/unit2/smolagents/retrieval_agents) → 원문 붙여 주면 입문자용 설명 + 쉬운 실습 노트북
- [ ] (선택) ToolCallingAgents 실습 `units/unit2-frameworks/code/tool_calling_agents_ollama.ipynb` (main에 있음, 사용자가 건너뛰기로 함)
- [ ] Unit 2 노트 0번 "내 말로:" 채우기 (프레임워크가 필요한 때·6가지)
- [ ] 2.2 · 2.3 세부 섹션 목록을 원문과 대조해 진도표 채우기 (그 섹션 시작할 때)
- [ ] Unit 1 마무리: [Conclusion](https://huggingface.co/learn/agents-course/unit1/conclusion) 원문 읽기 + 노트 끝 "한 페이지 요약"(AI 초안 있음)을 사용자와 같이 다듬기
- [ ] Todoist "Unit 1" 할 일 완료 처리 (사용자가 하거나 요청 시 AI가)
- [ ] 노트의 "내 말로:" 칸 채우기 (What is an Agent? · Messages · Tools · TAO · ReAct · Actions · Observe, 사용자 말로). Dummy Agent·smolagents는 기록함
- [ ] (선택) smolagents 노트북 8단계 Gradio 채팅 화면(`share=False`) · `reasoning_effort` 켜고 끈 속도 비교 · 6단계에 "Answer with both temperatures" 넣어 보기
- [ ] (선택) HF Space에 첫 에이전트 올리기: Space 안 모델은 크레딧 필요 → 크레딧 구매 or 생략 결정. 인증서와는 무관
- [ ] (필요할 때만) HF 토큰 발급(Settings → Access Tokens → **Read**). 데스크탑은 `.env`, 클라우드 세션은 `request_credential`
- [ ] (낮은 우선순위) Meta Llama 접근 신청 · 라이브 1 앞 15~20분 훑기 · `gemma4:12b`와 비교 · `ollama launch`로 로컬 코딩 에이전트 체험

## 사용자 결정 대기

- Unit 2~4 목표일(11/22 · 11/29 · 12/6)은 "1주 1유닛" 계산값 → 친구와 편하게 연락해서 확정 (AI가 챙길 일 아님)
- 이 레포를 친구와 공유할지 (공유하면 GitHub collaborator 초대)

## 데스크탑 메모

- 레포 위치: `문서\HF_AI_STUDY` = `$HOME\Documents\HF_AI_STUDY` (clone 완료). 쓸 때마다 `git pull`. 데스크탑에서는 실행만, 파일 수정은 AI에게. 평소 `main` 브랜치 (한 번 `claude/...` 브랜치로 checkout했을 수 있음 → 그렇다면 `git checkout main`)
- Unit 1 실습 venv: `units\unit1-intro-agents\code\.venv` (2026-11-16 만듦, `requirements.txt` 설치 완료: smolagents 1.26 + litellm + gradio + ddgs)
- Unit 0 실습 venv: `units\unit0-onboarding\code\.venv`
- **데스크탑에서 실행한 노트북**(`dummy_agent_ollama.ipynb`, `smolagents_first_agent.ipynb`)은 내 PC에 실행 결과가 저장돼 있음 → **클라우드에서 고치지 말고 새 파일로** 만들기. 그래도 `git pull`이 이 파일들 때문에 막히면 `git checkout -- <파일 경로>`(실행 결과만 버림) 후 `git pull`
- `dummy_agent_loop.ipynb`: 고친 7단계만 따로 떼어 낸 독립 실행판(내용은 노트북 7단계와 같음)
- Jupyter 끄기: `Esc` → `Ctrl + C` 두 번, 안 되면 PowerShell 창을 X로 닫아도 됨

## 최근 세션 (최신 3개, 전체는 SESSION-LOG.md)

- 2026-11-22 (2): **ToolCallingAgents → Tools** — 2.1 지금까지 요약 → 원문 입문자 설명(레시피 vs 주문서, 송장 칸 비유, 1.26 소스 확인) → 사용자가 2.1 0~4번을 자기 말로 정리("도구는 주어졌다 가정, 부르는 법만 봄"). 실습 노트북은 만들었지만 사용자가 건너뜀. 옛 브랜치 2개는 합치지 않기로. 이어서 Tools 원문 설명 + 쉬운 실습 노트북 `tools_ollama.ipynb`(0~8단계) 만들어 main 반영
- 2026-11-22: **CodeAgents 복습·실습 완료** — 원문 전체 입문자 설명 다시 → 데스크탑 새 venv + 노트북 0~6단계 전부 실행(2단계 결과만 받아 분석), "5바퀴 검색 후 답" 분석(모델이 스스로 끝냄·가상 장소라 맴돎·검색 결과 요약 + 상식) → 5단계·Langfuse 추가 설명 → 사용자가 섹션을 자기 말로 정리
- 2026-11-19: **Unit 2 시작** (`/new-unit`) → 소개(프레임워크 정의·필요한 때·6가지를 Dummy Agent 경험과 연결, 사용자 이해 확인·보충) → Introduction to smolagents(2.1 목차 7개, RAG·벡터 저장소) → Why Use smolagents(장점 4, Code vs JSON, MultiStepAgent, 모델 클래스 5). 이론만, 실습 없음
