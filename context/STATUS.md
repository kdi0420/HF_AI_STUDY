# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-22 (**Unit 2 진행중**, 2.1의 7번 Multi-Agent Systems 설명·노트·실습 노트북 완료 → 사용자 질문·"내 말로" 대기, 다음은 **8 Vision and Browser agents**)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영. **데스크탑에서 실행할 파일은 만들자마자 main에 반영**(사용자 승인 하에)해야 `git pull`로 받아짐

## 지금 초점

- **Unit 2 (프레임워크) 진행중** (2026-11-19 시작): `units/unit2-frameworks/`. 2.1 smolagents 0~6번 끝: 소개 → Why smolagents → CodeAgents(데스크탑 실습 완료) → ToolCallingAgents(실습 건너뜀) → Tools("내 말로" 정리, 실습 `tools_ollama.ipynb` 데스크탑 대기) → Retrieval Agents(실습 `retrieval_agents_ollama.ipynb` 데스크탑 대기) → **Multi-Agent Systems**(입문자 설명 + 노트 7번 + 실습 `multi_agent_systems_ollama.ipynb` main에 있음, **새 패키지 2개 plotly·pandas → 데스크탑에서 `pip install -r requirements.txt` 먼저**). 노트에 "2.1 중간 정리 — 내 말로"(0~4번) 있음. 남은 2.1: 8 Vision/Browser
- Unit 1 완료 (2026-11-16, 기초 인증서). Conclusion 원문·한 페이지 요약 다듬기는 아직
- 환경: 집 데스크탑 Ollama + `qwen3.5:9b`(100% GPU). Unit 2는 **새 venv** `units\unit2-frameworks\code\.venv` (requirements.txt는 smolagents부터, LlamaIndex·LangGraph는 그 섹션에서 추가). 2026-11-22 데스크탑에서 만들고 설치 완료

## 다음 할 일

- [ ] Multi-Agent Systems 사용자 질문 받기 + 노트 7번 "내 말로:" 채우기 (사용자가 원하면). Retrieval 노트 6번 "내 말로:"도 비어 있음
- [ ] **Unit 2.1 다음 섹션**: [Vision and Browser agents](https://huggingface.co/learn/agents-course/unit2/smolagents/vision_agents) → 원문 붙여 주면 입문자용 상세 설명 + 쉬운 실습 노트북(칸마다 설명) → 바로 main 반영. 2.1 마지막 섹션이라 끝나면 2.1 전체 정리
- [ ] (사용자가 원할 때) Multi-Agent 실습 `units/unit2-frameworks/code/multi_agent_systems_ollama.ipynb` 데스크탑 실행: `git pull` → venv 켜고 `pip install -r requirements.txt`(plotly·pandas) → Jupyter. 4~6단계는 인터넷 없이 됨, 7단계(웹 검색 팀원)는 선택·오래 걸림. 결과 붙여 주면 분석(4단계 팀장이 팀원을 몇 번·무슨 말로 불렀나, 5단계 토큰, 6단계 계획·검사 통과/실패)
- [ ] (사용자가 원할 때) Retrieval 실습 `units/unit2-frameworks/code/retrieval_agents_ollama.ipynb` 데스크탑 실행: `git pull` → venv 켜고 `pip install -r requirements.txt`(새 패키지 3개) → Jupyter. 결과 붙여 주면 분석(2·5·6단계 🔎 검색어·`web_search` 횟수, 7단계는 `ollama pull nomic-embed-text` 약 270MB 받았을 때만)
- [ ] (사용자가 원할 때) Tools 실습 `units/unit2-frameworks/code/tools_ollama.ipynb` 데스크탑 실행 → 결과 붙여 주면 분석(5-B 없는 테마에 모델 반응, 7-B 입력창)
- [ ] (선택, 하고 싶을 때) Tools의 공유·가져오기 실습: Hub 도구 올리기·가져오기 / Space를 도구로 / MCP 서버 연결 — 노트 5번 "Sharing and Importing 실전 정리"에 준비물 있음. 말하면 노트북 만들기
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

- 2026-11-22 (4): **Multi-Agent Systems** — 원문 입문자 설명(팀장·팀원, 기억 나뉨) + 클라우드에서 1.26 소스·가짜 모델로 원문 함정 확인(`"plotly"`만으론 `plotly.express` import 막힘 · 검사 함수에 `agent` 칸 없으면 무조건 실패 · `VisitWebpageTool` 40000자 > `num_ctx`) → 노트 7번·용어 5개 + 실습 노트북 `multi_agent_systems_ollama.ipynb`(0~8단계, 인터넷 없는 팀 실습 + 선택 웹 팀원) main 반영
- 2026-11-22 (3): **Retrieval Agents** — 원문 입문자 설명(보통 RAG vs Agentic RAG, 문서→조각→BM25→도구) + 클라우드에서 코스 코드 직접 실행해 함정 확인(BM25는 키워드 검색인데 "semantic"이라 적힘 · 조각 5개에 `k=5`라 전부 반환 · `catering,` 쉼표 때문에 점수 0) → 노트 6번·용어 6개 + 실습 노트북 `retrieval_agents_ollama.ipynb`(0~8단계) main 반영
- 2026-11-22 (2): **ToolCallingAgents → Tools** — 2.1 지금까지 요약 → 원문 입문자 설명(레시피 vs 주문서, 송장 칸 비유, 1.26 소스 확인) → 사용자가 2.1 0~4번을 자기 말로 정리("도구는 주어졌다 가정, 부르는 법만 봄"). 실습 노트북은 만들었지만 사용자가 건너뜀. 옛 브랜치 2개는 합치지 않기로. 이어서 Tools 원문 설명 + 쉬운 실습 노트북 `tools_ollama.ipynb`(0~8단계) 만들어 main 반영
