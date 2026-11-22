# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-22 (**Unit 2 진행중**, **2.1 smolagents 끝**(0~8번, 노트에 "2.1 전체 정리" 표) → 다음은 **2.2 LlamaIndex**)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영. **데스크탑에서 실행할 파일은 만들자마자 main에 반영**(사용자 승인 하에)해야 `git pull`로 받아짐

## 지금 초점

- **Unit 2 (프레임워크) 진행중** (2026-11-19 시작): `units/unit2-frameworks/`. 2.1 smolagents 0~8번 끝: 소개 → Why smolagents → CodeAgents(데스크탑 실습 완료) → ToolCallingAgents(실습 건너뜀) → Tools("내 말로" 정리, 실습 `tools_ollama.ipynb` 데스크탑 대기) → Retrieval Agents(실습 `retrieval_agents_ollama.ipynb` 데스크탑 대기) → **Multi-Agent Systems**(입문자 설명 + 노트 7번 + 실습 `multi_agent_systems_ollama.ipynb` main에 있음, 새 패키지 plotly·pandas) → **Vision Agents**(입문자 설명 + 노트 8번 + 실습 `vision_agents_ollama.ipynb` main에 있음, 3단계용 새 패키지 helium·selenium). 노트에 "2.1 중간 정리 — 내 말로"(0~4번) 있음
- Unit 1 완료 (2026-11-16, 기초 인증서). Conclusion 원문·한 페이지 요약 다듬기는 아직
- 환경: 집 데스크탑 Ollama + `qwen3.5:9b`(100% GPU). Unit 2는 **새 venv** `units\unit2-frameworks\code\.venv` (requirements.txt는 smolagents부터, LlamaIndex·LangGraph는 그 섹션에서 추가). 2026-11-22 데스크탑에서 만들고 설치 완료

## 다음 할 일

- [ ] **2.2 LlamaIndex 시작**: [Introduction to LlamaIndex](https://huggingface.co/learn/agents-course/unit2/llama-index/introduction) — 원문 목차 대조해 진도표 9·10번 채우기 → 원문 붙여 주면 입문자용 설명 + 실습 노트북 (LlamaIndex 패키지는 그때 requirements에 추가). 2.1 사이에 퀴즈가 있는지도 원문에서 확인
- [ ] (사용자가 원할 때) Vision 실습 `units/unit2-frameworks/code/vision_agents_ollama.ipynb` 데스크탑 실행: `git pull` → venv 켜고 `pip install -r requirements.txt`(helium·selenium) → Jupyter. **코스만 따라가려면 0→1→2**, 0단계에서 `qwen3.5:9b`가 `vision`인지 확인(아니면 `qwen2.5vl:7b` 약 6GB 받을지 결정). 3단계(브라우저)는 선택·크롬 필요
- [ ] (사용자가 원할 때) Multi-Agent 실습 `units/unit2-frameworks/code/multi_agent_systems_ollama.ipynb` 데스크탑 실행: `git pull` → venv 켜고 `pip install -r requirements.txt`(plotly·pandas) → Jupyter. **코스만 따라가려면 0→1→2→3→4**(4단계는 웹 검색이라 10~20분, DuckDuckGo에 막히면 5단계 = 인터넷 없는 팀원), 5·6은 원문 밖·선택. 결과 붙여 주면 분석(팀장이 팀원을 몇 번·무슨 말로 불렀나, `Initial plan`, 검사 통과/실패, 6-B 토큰)
- [ ] (사용자가 원할 때) Retrieval 실습 `units/unit2-frameworks/code/retrieval_agents_ollama.ipynb` 데스크탑 실행: `git pull` → venv 켜고 `pip install -r requirements.txt`(새 패키지 3개) → Jupyter. **코스만 따라가려면 0→1→2→3(첫 칸)→5(첫 두 칸)만**, 나머지는 원문 밖·선택. 결과 붙여 주면 분석(2·5·6단계 🔎 검색어·`web_search` 횟수, 7단계는 `ollama pull nomic-embed-text` 약 270MB 받았을 때만)
- [ ] (사용자가 원할 때) Tools 실습 `units/unit2-frameworks/code/tools_ollama.ipynb` 데스크탑 실행 → 결과 붙여 주면 분석(5-B 없는 테마에 모델 반응, 7-B 입력창)
- [ ] (선택, 하고 싶을 때) Tools의 공유·가져오기 실습: Hub 도구 올리기·가져오기 / Space를 도구로 / MCP 서버 연결 — 노트 5번 "Sharing and Importing 실전 정리"에 준비물 있음. 말하면 노트북 만들기
- [ ] (선택) ToolCallingAgents 실습 `units/unit2-frameworks/code/tool_calling_agents_ollama.ipynb` (main에 있음, 사용자가 건너뛰기로 함)
- [ ] (사용자가 원하면) 노트 6번 Retrieval "내 말로:" 채우기
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

- 2026-11-22 (5): **Vision Agents → 2.1 끝** — 원문 입문자 설명(그림 주는 법 2가지: 처음에 `images=` / 매 Step 스크린샷 콜백) + 클라우드에서 가짜 Ollama 서버·가짜 브라우저로 확인(Ollama 모델은 `flatten_messages_as_text=False` 없으면 그림 에러 · 원문 `save_screenshot`은 1.26에서 `agent.logs` 에러 · 본문에 빠진 준비 단계) → 노트 8번·용어 5개 + 실습 `vision_agents_ollama.ipynb` main 반영. 같은 세션에서 옛 브랜치 2개 삭제 요청 → 세션 권한으로 거절돼 훅에서 알림만 빼기로, 팀원 병렬 실행 질문 답함. 스크린샷 콜백 질문 → 사용자가 "그림도 입력으로 받는 에이전트"로 내 말로 정리 → 노트에 2.1 전체 정리 표
- 2026-11-22 (4): **Multi-Agent Systems** — 원문 입문자 설명(팀장·팀원, 기억 나뉨) + 클라우드에서 1.26 소스·가짜 모델로 원문 함정 확인(`"plotly"`만으론 `plotly.express` import 막힘 · 검사 함수에 `agent` 칸 없으면 무조건 실패 · `VisitWebpageTool` 40000자 > `num_ctx`) → 노트 7번·용어 5개 + 실습 노트북 `multi_agent_systems_ollama.ipynb`(원문 경로 0~4 + 원문 밖·선택 5~6) main 반영. 합치는 중 새 USER.md 선호(원문 기본)를 보고 노트북을 원문 순서로 다시 짬 → 팀장이 일 시키는 흐름 재설명, 사용자가 "툴 자리에 에이전트를 넣은 것 = 역할 분배"로 내 말로 정리
- 2026-11-22 (3): **Retrieval Agents + Quiz 2** — 원문 입문자 설명 + 실습 노트북 `retrieval_agents_ollama.ipynb`(0~8단계, 클라우드에서 코스 코드 직접 실행해 BM25 함정 확인) main 반영 → 사용자 지적: "원문보다 너무 많다, 코스를 따라가고 싶다" → 원문/추가 구분·중요도 설명, USER.md에 원문 기본 선호 기록 → "검색기를 도구로 감싸 준 것"·"RAG = 찾기 + 답 쓰기, 방식(패턴)" 정리 → **Quiz 2 전부 맞음**
