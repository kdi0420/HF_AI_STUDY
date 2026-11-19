# Unit 2 — Introduction to Agentic Frameworks

- 링크: [Unit 2 소개](https://huggingface.co/learn/agents-course/unit2/introduction)
- 목표일: 11/22 ("1주 1유닛" 계산값, 친구와 확정 전)
- 이 유닛의 결과물: 같은 종류의 에이전트를 **프레임워크 3개(smolagents · LlamaIndex · LangGraph)로** 만들어 보고, 언제 무엇을 쓸지 말할 수 있기
- 실습 환경: 집 데스크탑 Ollama(`qwen3.5:9b`) + 이 유닛의 `code/.venv` (새 venv)

## 진도

2.1 smolagents 목차는 원문 "Contents"와 대조함 (2026-11-19). **2.2 · 2.3의 세부 섹션은 기억 기반 → 원문 대조 필요**(그 섹션 시작할 때 확인). 퀴즈 위치도 미확인.

| # | 섹션 | 끝나면 설명할 수 있어야 하는 것 | 완료 |
|---|---|---|---|
| 0 | [Introduction to Agentic Frameworks](https://huggingface.co/learn/agents-course/unit2/introduction) | 프레임워크가 필요한 때 / 필요 없는 때, 프레임워크가 챙겨 주는 6가지 | [x] (2026-11-19 읽음) |
| **2.1** | **smolagents** | | |
| 1 | [Introduction to smolagents](https://huggingface.co/learn/agents-course/unit2/smolagents/introduction) | 2.1에서 뭘 배우나 (Alfred 파티 준비 예시) | [x] (2026-11-19) |
| 2 | [Why Use smolagents](https://huggingface.co/learn/agents-course/unit2/smolagents/why_use_smolagents) | smolagents의 장점·한계, 다른 프레임워크와의 차이 | [ ] |
| 3 | [CodeAgents](https://huggingface.co/learn/agents-course/unit2/smolagents/code_agents) | 코드로 행동하는 에이전트의 동작 과정 (Unit 1 실습과 연결) | [ ] |
| 4 | [ToolCallingAgents](https://huggingface.co/learn/agents-course/unit2/smolagents/tool_calling_agents) | JSON 도구 호출 에이전트 vs CodeAgent | [ ] |
| 5 | [Tools](https://huggingface.co/learn/agents-course/unit2/smolagents/tools) | `@tool` vs `Tool` 클래스, Hub에서 도구 가져오기·공유 | [ ] |
| 6 | [Retrieval Agents](https://huggingface.co/learn/agents-course/unit2/smolagents/retrieval_agents) | 검색(RAG)을 도구로 쓰는 에이전트 | [ ] |
| 7 | [Multi-Agent Systems](https://huggingface.co/learn/agents-course/unit2/smolagents/multi_agent_systems) | 에이전트가 다른 에이전트를 부리는 구조 | [ ] |
| 8 | [Vision and Browser agents](https://huggingface.co/learn/agents-course/unit2/smolagents/vision_agents) | 이미지를 보는 에이전트, 브라우저 조작 | [ ] |
| **2.2** | **LlamaIndex** (원문 대조 필요) | | |
| 9 | [Introduction to LlamaIndex](https://huggingface.co/learn/agents-course/unit2/llama-index/introduction) | LlamaIndex의 구성 요소(components · tools · agents · workflows) | [ ] |
| 10 | LlamaHub · Components · Tools · Agents · Workflows (세부 링크는 시작할 때 채움) | 내 문서·데이터를 붙인 에이전트(RAG)를 만드는 흐름 | [ ] |
| **2.3** | **LangGraph** (원문 대조 필요) | | |
| 11 | [Introduction to LangGraph](https://huggingface.co/learn/agents-course/unit2/langgraph/introduction) | 언제 LangGraph를 쓰나 | [ ] |
| 12 | Building Blocks · First Graph · Document Analysis Agent (세부 링크는 시작할 때 채움) | 노드·엣지·상태(state)로 흐름을 그리기 | [ ] |
| 13 | 퀴즈 · Conclusion | 틀린 문제 → `quiz.md`, 유닛 2 한 페이지 요약 | [ ] |

## 섹션별 노트

<!-- 각 섹션: "내 말로 정리" 3~5줄 + 예시. 모르는 건 ../../questions.md, 용어는 ../../glossary.md -->

### 0. Introduction to Agentic Frameworks — 2026-11-19 읽음

- 로드맵: 2.1 **smolagents**(HF가 만든 가벼운 프레임워크) → 2.2 **LlamaIndex**(내 데이터를 붙인 에이전트를 실제 서비스까지) → 2.3 **LangGraph**(상태를 가진 흐름 설계)
- **프레임워크(agentic framework)** = 에이전트를 만들 때 매번 손으로 짜야 하는 부품(멈추기·파싱·루프·에러 처리 …)을 미리 만들어 둔 **조립 세트**. Unit 1에서 Dummy Agent(손으로 짬) → smolagents `CodeAgent`(몇 줄)로 이미 체험함
- **항상 필요하진 않다**: 정해진 순서대로만 가면 되는 일(**predefined workflow**, 예: "요약해 → 그걸 번역해" 같은 프롬프트 사슬)은 그냥 파이썬 코드로 충분 → 장점: **추상화(abstraction, 속을 감춰 주는 포장) 없이** 시스템 전체를 내가 이해·통제
- **필요해지는 때**: 흐름이 복잡해질 때 — LLM이 **함수(도구)를 부르거나**, **에이전트 여러 개**를 쓸 때 (Unit 1 Agency 스펙트럼의 ★★☆ 이상)
- 프레임워크가 챙겨 줘야 할 6가지 = **Unit 1 Dummy Agent에서 손으로 한 일 목록과 같음**

| 원문 기능 | 뜻 | Unit 1에서 직접 한 것 |
|---|---|---|
| LLM engine | 시스템을 돌리는 두뇌 모델 | Ollama `qwen3.5:9b`를 부르는 `chat()` 함수 |
| List of tools | 에이전트가 쓸 수 있는 도구 목록 | `get_weather`, `TOOLS` 사전 |
| Parser | LLM 글에서 도구 호출 부분을 꺼내는 것 | `stop=["Observation:"]`으로 멈추고 JSON 꺼내 `json.loads` |
| System prompt synced with parser | 프롬프트가 요구하는 형식 = 파서가 읽는 형식 | "```json 블록으로 Action" 규칙. 모델이 형식을 어기자 `substring not found` (7단계 실패) |
| Memory system | 지난 대화·행동·관찰 기억 | messages 리스트에 Thought/Action/Observation을 쌓아 매번 다시 보냄 (Input tokens 누적) |
| Error logging & retry | LLM 실수를 기록하고 다시 시도 | 손으로 만든 `FORMAT_HINT` 에러 관찰 / smolagents는 검색 에러를 관찰로 돌려줘 모델이 검색어 바꿔 재시도 |

- 내 말로 (2026-11-19): LLM은 결국 **다음 단어 맞추기를 엄청 잘하는 애**인데, 그것만으로는 실제로 쓰기 어려움 → 그걸 끼워 넣은 게 AI 에이전트. 이 단원은 LLM이 있다는 가정 하에, LLM을 **어떻게 일하게 만들지**(에이전트를 어떻게 만들지) 얘기하는 것. 6가지 = LLM 실행을 함수처럼 만들기 / 어떤 도구가 있는지 알려 주기 / LLM 글에서 도구 호출만 꺼내 실제로 부르기 / 특정 형식으로 말하라고 지시 / 이전 내용을 하나로 붙이기 / 에러 기록하고 다시 시도
  - 보충 ① **에이전트 ≠ 프레임워크**: 에이전트 = 완성된 시스템(집), 프레임워크 = 그걸 짓는 **조립 키트**(공구 + 규격 부품 + 조립 순서). "에이전트가 어떻게 움직이나"는 Unit 1, Unit 2는 "그걸 **매번 손으로 안 짜려고** 남이 만들어 둔 키트 3종 비교"
  - 보충 ② 파서는 **꺼내기만** 하고, 실제로 도구를 부르는 건 실행기(executor)·루프 쪽. 프레임워크는 둘 다 들어 있음
  - 보충 ③ "형식 지시(system prompt)"와 "꺼내기(parser)"는 **한 쌍** — 프롬프트가 시킨 모양을 파서가 읽음
  - 보충 ④ LLM은 우리가 만들진 않지만 **고르는 부품**(엔진 자리에 `qwen3.5` 대신 다른 모델을 끼워도 나머지는 그대로)
  - 보충 ⑤ 원문의 단서: 프레임워크가 **항상 필요하진 않음**. 순서가 정해진 단순한 일은 그냥 코드로
- 정의 (원문에는 한 문장 정의가 없음 → 일반적인 뜻, AI 정리): **LLM으로 에이전트를 만들고 돌릴 때 매번 필요한 공통 부품(모델 연결·도구 등록·파서·system prompt·메모리·에러 처리·TAO 루프)을 미리 구현해 둔 소프트웨어 틀(라이브러리)**
  - "framework" = 뼈대. 라이브러리는 내가 필요할 때 불러 쓰는 것, 프레임워크는 **틀이 내 코드를 불러 씀** — 나는 `@tool` 함수만 쓰고, smolagents 루프가 알맞은 때 그 함수를 부름

### 1. Introduction to smolagents — 2026-11-19 읽음

- smolagents = HF가 만든 **가벼운(lightweight)** 에이전트 프레임워크. "smol" = small을 귀엽게 쓴 인터넷 말투. 원문이 GitHub 저장소에 **star**(즐겨찾기·추천 표시)를 눌러 달라고 함 → 선택 사항
- 목표: smolagents로 에이전트 만드는 법 + **언제 smolagents가 맞고 언제 다른 걸 써야 하는지** 판단하기
- 이야기: Unit 1의 **Alfred**가 돌아옴. 웨인 가족이 집을 비운 사이 Wayne Manor에서 **파티를 준비** → 할 일마다 smolagents의 기능 하나씩
- 2.1 목차 7개 (Unit 1과 연결)

| # | 섹션 | 한 줄 | Unit 1과 연결 |
|---|---|---|---|
| 1 | Why Use smolagents | 장점·단점, 다른 프레임워크와 비교해 고르는 법 | 0번 "항상 필요한 건 아님"의 연장 |
| 2 | CodeAgents | smolagents의 **기본** 에이전트. 행동을 **파이썬 코드**로 씀 | 이미 써 봄 (`smolagents_first_agent.ipynb`, 도구 둘 한 번에 + `if` 비교) |
| 3 | ToolCallingAgents | 두 번째 종류. 행동을 **JSON 덩어리(blob)**로 쓰고, 시스템이 파싱해서 실행 | Dummy Agent의 JSON 방식을 프레임워크가 자동으로 |
| 4 | Tools | 도구 만드는 두 방법(`@tool` 데코레이터 / `Tool` 클래스), 기본 도구 상자, Hub에 공유·남의 도구 가져오기 | `@tool get_weather` 만들어 봄 |
| 5 | Retrieval Agents | **지식 창고(knowledge base)**를 검색해 답하는 에이전트. **벡터 저장소** + **RAG** + 실패 시 대비책(fallback) | 임베딩(용어집), 웹 검색 도구 |
| 6 | Multi-Agent Systems | 능력이 다른 에이전트 여러 개를 **지휘(orchestration)** (예: 웹 검색 담당 + 코드 실행 담당) | Agency 스펙트럼의 멀티 에이전트 ★★★ |
| 7 | Vision and Browser agents | **VLM**으로 이미지를 보는 에이전트 → 화면을 보며 웹을 돌아다니는 **브라우저 에이전트** | VLM(용어집) |

- 원문 Overview에 "code agents designed for software development tasks"라고 돼 있지만, CodeAgent는 **개발 일 전용이 아니라 행동을 코드로 쓰는 방식**(Unit 1에서 날씨 비교에도 씀). 코딩 일을 잘한다는 정도로 읽으면 됨
- RAG (Retrieval-Augmented Generation, 검색 증강 생성) = ① 질문과 관련된 자료를 **찾아서(retrieval)** ② 프롬프트에 **붙이고(augmented)** ③ 그걸 보고 **답을 씀(generation)**. 시험으로 치면 "오픈북". 모델이 원래 모르는 내 자료·최신 정보로도 답할 수 있음
  - 벡터 저장소(vector store) = 문서 조각들을 임베딩(의미 숫자 벡터)으로 바꿔 넣어 둔 창고 → 질문도 벡터로 바꿔 **뜻이 가까운 조각**을 꺼냄 (단어가 달라도 뜻이 비슷하면 찾음)
  - fallback = 플랜 B. 예: 지식 창고에 없으면 웹 검색으로
- 참고 자료 중 눈여겨볼 것: Anthropic의 [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — 원문은 "research paper"라고 했지만 논문이라기보다 **연구 블로그 글**. **workflow(순서를 코드가 정함) vs agent(순서를 LLM이 정함)** 구분과 "단순한 것부터 시작하라"는 조언 → 0번 섹션 "프레임워크가 항상 필요하진 않다"와 같은 얘기 · [smolagents 공식 문서](https://huggingface.co/docs/smolagents) · [좋은 에이전트 만들기 가이드](https://huggingface.co/docs/smolagents/tutorials/building_good_agents)
- 실습 메모: 코스 예제는 HF 서버 모델(`InferenceClientModel`)을 씀 → 크레딧이 없으니 Unit 1처럼 **데스크탑 Ollama**(`LiteLLMModel`)로 바꿔서 할 예정. 7번 Vision은 이미지를 받는 모델(VLM)이 필요 → `qwen3.5:9b`로 되는지 그때 확인(미확인)
- 내 말로:

## 유닛 2 한 페이지 요약

<!-- 유닛 끝나고 "프레임워크 3개를 언제 무엇을 쓰나"를 친구에게 3분 안에 설명한다고 생각하고 쓴다 -->

