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
| 2 | [Why Use smolagents](https://huggingface.co/learn/agents-course/unit2/smolagents/why_use_smolagents) | smolagents의 장점·한계, 다른 프레임워크와의 차이 | [x] (2026-11-19) |
| 3 | [CodeAgents](https://huggingface.co/learn/agents-course/unit2/smolagents/code_agents) | 코드로 행동하는 에이전트의 동작 과정 (Unit 1 실습과 연결) | [x] (2026-11-19 읽음, 11-22 복습·실습 완료) |
| 4 | [ToolCallingAgents](https://huggingface.co/learn/agents-course/unit2/smolagents/tool_calling_agents) | JSON 도구 호출 에이전트 vs CodeAgent | [x] (2026-11-22 읽음·내 말로 정리, 실습 노트북은 데스크탑 대기) |
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

### 2. Why Use smolagents — 2026-11-19 읽음

- smolagents = 단순하지만 강력한 에이전트 프레임워크. LLM에게 **agency**(검색·이미지 생성처럼 바깥 세계에 작용하는 능력)를 줌. 안에서 도는 건 Unit 1의 Thought → Action → Observation 그대로
- 장점 4가지

| 장점 | 뜻 | 내 경험·주의 |
|---|---|---|
| Simplicity | 코드·추상화를 최소로 → 이해·도입·확장이 쉬움 | 속이 얇아서 `agent.memory`, 로그로 안을 들여다보기 쉬움 |
| Flexible LLM Support | 어떤 LLM이든 연결 | HF 서버 대신 Ollama `qwen3.5:9b`로 바꿔 끼움 (`LiteLLMModel`) |
| Code-First | CodeAgent가 기본. 행동을 코드로 써서 **JSON 파싱이 필요 없음** → 도구 호출이 단순 | 주의: 글에서 코드 부분(`<code>`~`</code>`)은 여전히 **꺼냄**. 없어지는 건 "JSON → 함수 호출로 바꾸는" 번역 단계 |
| HF Hub Integration | Hub와 바로 연결, **Gradio Space를 도구로** 씀 | 남이 Space에 올린 앱(예: 이미지 생성)을 도구처럼 부를 수 있음 |

- 언제 쓰나: ① 가볍고 최소한의 해법이 필요할 때 ② 복잡한 설정 없이 **빨리 실험**할 때 ③ 앱 로직이 **단순(straightforward)**할 때. 반대로 흐름에 분기·상태가 많으면 LangGraph, 내 문서·데이터 연결이 중심이면 LlamaIndex 쪽이 맞을 수 있음(뒤에서 비교, 지금은 예고)
- Code vs JSON (원문 그림): 같은 일도 JSON은 도구 1번 = 행동 1번 → 바퀴가 많아지고 중간 값을 LLM이 기억해 옮겨야 함. 코드는 변수·반복문·`if`로 **한 행동에 여러 호출을 묶음**. Unit 1 실습에서 `get_weather` 둘을 한 코드에 부른 것이 그 예
- 에이전트 종류: smolagents 에이전트는 모두 **MultiStepAgent**(여러 단계 에이전트) = 부모 설계도(클래스). 한 단계(step) = 생각 1번 + 행동 1번(실행 포함), 이걸 끝날 때까지 반복 = TAO 루프
  - 자식 두 종류: **CodeAgent**(기본, 코드로 행동) · **ToolCallingAgent**(JSON으로 도구 호출)
  - 원문은 "One tool call"이라 썼지만 CodeAgent는 한 단계의 코드 안에서 도구를 **여러 번** 부를 수 있음(Unit 1: 1바퀴에 London·Paris). "행동 1번"으로 읽는 게 정확
  - 도구는 `@tool` 데코레이터(함수 위 한 줄) 또는 `Tool` 클래스로 정의
- 모델 연결: 조건(메시지 목록을 받아 답 메시지를 돌려주는 등, [기준](https://huggingface.co/docs/smolagents/main/en/reference/models))만 맞으면 어떤 모델이든. 미리 만든 연결 클래스 5개

| 클래스 | 모델이 도는 곳 | 메모 |
|---|---|---|
| `TransformersModel` | **내 PC**, `transformers` 라이브러리로 모델을 직접 불러옴 | 가중치 다운로드·GPU 메모리 필요 |
| `InferenceClientModel` | **HF 서버**(serverless) 또는 제휴 업체(inference providers) | 코스 기본값. 크레딧 필요 → Unit 1 Dummy Agent의 `InferenceClient`와 같은 길 |
| `LiteLLMModel` | LiteLLM(여러 회사 API를 같은 모양으로 맞춰 주는 **통역기**)이 가리키는 곳 | **우리가 쓰는 것**: `ollama_chat/qwen3.5:9b` → 데스크탑 Ollama |
| `OpenAIServerModel` | OpenAI 방식(API 모양)을 따르는 **아무 서버** | Ollama도 OpenAI 방식 주소(`localhost:11434/v1`)를 제공해서 이걸로도 연결 가능 |
| `AzureOpenAIServerModel` | Microsoft Azure 클라우드에 띄운 OpenAI 모델 | 회사용, 우리는 안 씀 |

  - 요점: **엔진만 바꿔 끼우고 나머지(도구·에이전트 코드)는 그대로** = 0번 섹션 보충 ④
- 참고: [smolagents 소개 블로그](https://huggingface.co/blog/smolagents) (코드 행동이 왜 좋은지)
- 내 말로:

### 3. Building Agents That Use Code (CodeAgents) — 2026-11-19 읽음, 2026-11-22 다시 훑음

- CodeAgent = smolagents의 **기본** 에이전트. 행동을 **파이썬 코드**로 씀. 라이브러리 핵심이 약 1,000줄 → 속을 들여다보기 쉬움
- 왜 코드인가 (근거 논문: [Executable Code Actions Elicit Better LLM Agents](https://huggingface.co/papers/2402.01030)): JSON은 시스템이 글을 **파싱해서** 어떤 도구를 부를지 알아내야 함. 코드는 그대로 실행

| 장점 | 뜻 | 예 |
|---|---|---|
| Composability (조합) | 행동을 이어 붙이고 재사용 | 도구 결과를 변수에 담아 다음 도구에 바로 넘김, `for`로 여러 번 |
| Object Management (객체 다루기) | 이미지·표 같은 복잡한 것도 변수로 들고 다님 | JSON은 글자만 → 이미지를 "전달"하기 어려움 |
| Generality (범용성) | 계산 가능한 일이면 뭐든 표현 | 도구가 없어도 `datetime`으로 시간 계산 |
| Natural for LLMs | 학습 데이터에 좋은 코드가 많음 | 모델이 JSON 규칙보다 파이썬을 더 잘 씀 |

- `CodeAgent.run()` 안에서 일어나는 일 (= Unit 1 Dummy Agent에서 손으로 짠 것)

| 원문 단계 | 뜻 | Unit 1 Dummy Agent에서는 |
|---|---|---|
| `SystemPromptStep` | system prompt를 기억(memory)에 저장 | messages 맨 앞 system 메시지 |
| `TaskStep` | 사용자 질문 저장 | user 메시지 |
| 2.1 `write_memory_to_messages()` | 기억(로그)을 LLM이 읽는 **chat messages 목록**으로 변환 | messages 리스트를 직접 만들어 보냄 |
| 2.2 `Model`에 보냄 → 답(completion) | LLM 호출 | `chat()` 함수 |
| 2.3 파싱 → 코드 조각 꺼냄 | 글에서 코드 블록만 | `stop=["Observation:"]` + JSON 꺼내기 |
| 2.4 실행 | 코드를 돌림 | `TOOLS[name](**args)` |
| 2.5 `ActionStep`에 기록 | 생각·코드·결과(관찰)를 기억에 추가 | Observation을 messages에 붙임 |
| `step_callbacks` | 단계마다 끝에 부르는 내 함수(선택) | 없었음. 예: 단계마다 로그 저장 |

  - 2.1~2.5를 `final_answer`가 나오거나 `max_steps`(기본 20)에 닿을 때까지 반복 = TAO 루프
- 예시 ① **플레이리스트**: `CodeAgent(tools=[DuckDuckGoSearchTool()], model=InferenceClientModel())`. 도구 이름은 `web_search` → 실행 로그에 `web_search(query=...)` 코드가 보임
- 예시 ② **메뉴**: `@tool suggest_menu(occasion)`. docstring에 **허용 값(casual/formal/superhero/custom)을 적어 두면** 모델이 없는 값을 지어내는(hallucination) 걸 줄임 → 도구 설명서 = 모델이 읽는 유일한 사용법
- 예시 ③ **준비 시간 계산**: 에이전트 코드는 smolagents의 **자체 파이썬 실행기**(`LocalPythonExecutor`)에서 돔. 허용 목록 밖 `import`는 막힘(sandbox 비슷한 안전장치) → `additional_authorized_imports=['datetime']`로 추가 허용
  - 확인(smolagents 1.26, 2026-11-19): 기본 허용 = `collections datetime itertools math queue random re stat statistics time unicodedata` → **`datetime`은 이미 기본 허용**이라 이 예제에선 사실 안 써도 됨. `import os`는 "Import of os is not allowed"로 막힘
  - 원문 코드 위쪽 `import numpy`, `import time`, `import datetime`은 **내 노트북**의 import일 뿐, 에이전트 코드의 허용 여부와 무관
  - 주의: 공식 문서도 로컬 실행기는 완전한 보안 장치가 아니라고 함 → 진짜 격리는 Docker·E2B 같은 원격 sandbox ([secure code execution](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution))
- **Hub 공유**: `agent.push_to_hub('아이디/이름')` 올리기, `from_hub(..., trust_remote_code=True)` 내려받기. 올리면 Space로도 바로 써 볼 수 있음
  - 우리 규칙: Hub 쓰기·`trust_remote_code`(남의 코드를 내 PC에서 실행)는 **승인 받고** (`docs/ai-workflow.md`)
- **완성판 Alfred**: 도구를 만드는 세 가지 길이 한 에이전트에 다 들어 있음

| 종류 | 예 | 모양 |
|---|---|---|
| 기본 제공 도구 | `DuckDuckGoSearchTool` `VisitWebpageTool` `FinalAnswerTool` | 가져다 넣기만 |
| `@tool` 함수 | `suggest_menu`, `catering_service_tool` | 함수 + 타입 힌트 + docstring |
| `Tool` 클래스 | `SuperheroPartyThemeTool` | `name` · `description` · `inputs` · `output_type` + 실제 일은 `forward()` |

  - `max_steps=10`(최대 바퀴 수), `verbosity_level=2`(로그 자세히)
  - `final_answer` 도구는 CodeAgent가 **항상 자동으로** 넣음(1.26 확인) → 목록의 `FinalAnswerTool()`은 없어도 됨
  - `catering_service_tool`은 `query`를 안 씀 → 검색하는 척하는 **연습용 가짜 도구**
- **추적(tracing)**: 에이전트는 예측이 어렵고 속을 보기 어려움 → 실행 기록을 바깥에 남겨 나중에 분석. 비행기 **블랙박스**
  - **OpenTelemetry** = 실행 기록 형식의 공통 표준, `SmolagentsInstrumentor().instrument()` = smolagents에 기록 장치 달기, **Langfuse** = 그 기록을 받아 화면으로 보여 주는 서비스(클라우드)
  - 원문은 키를 `os.environ[...] = "sk-lf-..."`로 코드에 직접 씀 → 우리는 **`.env`에만** (비밀 규칙). 클라우드 대신 내 PC에서 보는 방법도 있음 ([inspect runs](https://huggingface.co/docs/smolagents/tutorials/inspect_runs))
  - 자세한 건 Bonus Unit 2 (에이전트 관찰·평가)
  - (2026-11-22 다시 정리) **필수 아님**: 코스 진도·인증서와 무관한 선택 실습. 하면 `agent.run()` 한 번 = trace 하나가 웹 화면에 남고, 바퀴·LLM 호출·도구 호출을 나무 모양으로 클릭해 볼 수 있음(노트북 3단계에서 손으로 본 memory를 화면으로 보는 것). 주의: Langfuse Cloud를 쓰면 프롬프트·검색 결과·답이 **외부 서버로 전송**됨 → Ollama로 다 내 PC에서 돌리는 의미가 줄어듦. 키 없이 내 PC에서만 보려면 Phoenix(로컬 서버) 같은 대안
- 실습 메모: 예제는 `InferenceClientModel`(HF 서버, 크레딧) → 데스크탑에선 `LiteLLMModel("ollama_chat/qwen3.5:9b")`로 바꿈. Langfuse·Hub 공유는 계정·키가 필요해 선택
- 실습 노트북: `code/code_agents_ollama.ipynb` (2026-11-19 만듦, 클라우드에서 가짜 모델로 전 칸 실행 확인 — 진짜 Ollama 결과는 데스크탑에서). 원문 예제 ①②③ + 완성판 Alfred, 덤으로 기억(memory) 들여다보기 · docstring 허용 값 지우기 실험 · `import` 막힘 확인 · `step_callbacks`
  - 확인(1.26): 기억 속 관찰은 `tool-response` 역할로 저장되고, 모델에게 보내기 직전에 `user`로 바뀜(`tool_role_conversions`). 행동 기록 `tool-call`은 `assistant`로
- 실습 결과 (2026-11-22, 데스크탑 `qwen3.5:9b`, `max_steps=6`)
  - **예제 ① 플레이리스트**: 1~5바퀴 전부 `web_search`(검색어만 조금씩 바꿈) → 6바퀴에 `final_answer`. 사용자가 "이상하다"고 느낀 점을 같이 확인함
    - 6바퀴 답은 **모델이 스스로** 낸 것(강제 종료였다면 `Reached max steps` 에러가 남). 모델은 남은 바퀴 수를 모름(1.26 확인: 남은 바퀴는 planning을 켰을 때만 알려 줌) → 딱 6에서 끝난 건 우연에 가까움
    - 검색 결과가 5번 다 거의 같음(`late nights in the wayne manor` 유튜브가 매번 1등). 원인: 웨인 저택은 **가상의 장소**라 "파티 음악 추천"이 딱 맞게 나오는 페이지가 없음 + Spotify 결과는 곡 목록 없이 "Sign up..."뿐 + 이 예제엔 `visit_webpage`가 없어 **페이지를 열어 볼 수 없음** → 더 찾을 게 없어서 같은 검색을 맴돔
    - "겹치는 걸 고른 건가?" → **반쯤 맞음**. 코드로 교집합을 계산한 게 아니라, 6바퀴 때 messages에 쌓인 검색 결과 5개를 **모델이 한꺼번에 읽고 요약**. 답 1번(5번 다 나온 것)·2번(1·5번)·3번(4번)은 검색 결과에서 왔고, 4번 "재즈·80년대 뉴웨이브" 등은 **검색 결과에 없는 모델의 일반 지식**
    - 화면의 Input tokens는 **누적값**(1.26 `monitoring.py` 확인). 바퀴별로 빼 보면 2,204 → 3,377 → 4,731 → 5,739 → 6,810 → 7,732로 매번 검색 결과만큼 커짐. `num_ctx=8192`에 거의 닿음 → 한 바퀴 더 갔으면 넘쳤을 것
    - 모델의 생각(Thought)은 기본 로그(`verbosity_level=1`)에선 안 보임(DEBUG 단계). `agent.memory.steps[i].model_output`으로 확인 가능
    - `Provider List: https://docs.litellm.ai/...` 줄은 LiteLLM이 찍는 안내문, 결과와 무관
  - 5단계 다시 설명 들음(2026-11-22): 5-A 에이전트 코드는 별도 실행기에서 돌고 허용 목록 밖 `import`는 막힘(출입 카드 비유) / 5-B 필요한 모듈만 골라 허락 / 5-C 도구 없이 코드로 계산 + `step_callbacks`로 바퀴마다 보고받기. 콜백 속 토큰은 그 바퀴 값, 회색 줄은 누적값
  - 3~6단계도 데스크탑에서 끝까지 실행함(2026-11-22, 사용자 보고). 3단계 이후 결과는 따로 붙여 주지 않아 기록 없음 → 노트북 0~6단계 실습 완료
- 내 말로 (2026-11-22): 결국 **직접 코드를 쓸 수 있는 에이전트**를 만든 것. 처음엔 에이전트가 어떻게 굴러가는지(기억을 messages로 바꿔 모델에게 보내고 → 코드 실행 → 기록) 봤고, 플레이리스트에서 **이미 만들어져 있는 도구**를 가져다 쓰는 법, 메뉴에서 **도구를 직접 만들어** 쓰는 법, 준비 시간 계산에서 `import`와 **보안**(허용 목록) 문제를 다룸. 그리고 에이전트를 **Hub에 올려 공유**하는 법, 외부 프로그램(Langfuse)으로 **실행 기록(trace)을 보는 법**까지. Langfuse는 이번엔 안 해 봄. 유난히 어려웠던 섹션
  - AI 보충: 완성판 Alfred에서 도구 만드는 세 가지 길(기본 제공 · `@tool` 함수 · `Tool` 클래스)이 한 에이전트에 다 들어 있다는 것, 준비 시간 예제의 핵심은 "도구가 0개인데도 코드로 계산"(Generality)이라는 것

### 4. Tool Calling Agents — 2026-11-22 읽음

- ToolCallingAgent = smolagents의 두 번째 에이전트. 행동을 **JSON 구조**(도구 이름 + 인자)로 냄. 모델 회사(OpenAI·Anthropic 등) API에 들어 있는 **tool calling 기능**을 그대로 씀 → 업계 표준 방식
- 같은 일, 다른 모양 (Alfred: 출장 요리 + 파티 테마 검색)
  - CodeAgent: `for query in [...]: print(web_search(...))` — 반복문 하나로 두 번
  - ToolCallingAgent: `[{"name": "web_search", "arguments": ...}, {"name": "web_search", ...}]` — 호출 2개를 목록으로. 시스템이 이 JSON을 읽어 실행
  - (1.26 확인) 실제 인자는 `{"query": "..."}` 사전 모양. 원문 예시는 글자만 쓴 간단 버전
- 동작 과정은 CodeAgent와 **똑같은 TAO 루프**(3번 섹션 표). 다른 건 **행동의 모양**뿐: 코드 대신 JSON → 시스템이 파싱해 도구 실행
- smolagents가 CodeAgent를 기본으로 미는 이유: [전반적으로 성능이 더 좋음](https://huggingface.co/papers/2402.01030) (3번 섹션 근거 논문). ToolCallingAgent는 **변수 처리·복잡한 도구 호출이 필요 없는 단순한 시스템**에 효과적
- 예제: `ToolCallingAgent(tools=[WebSearchTool()], model=InferenceClientModel())` — `CodeAgent`에서 **클래스 이름만** 바뀜
  - 로그: `Executing parsed code:` 대신 `Calling tool: 'web_search' with arguments: {'query': ...}`
- 확인(smolagents 1.26 소스, 2026-11-22)
  - 모델에게 도구 목록을 글이 아니라 API의 `tools` 칸으로 따로 보내고, 모델은 답을 `tool_calls` 칸에 돌려줌. 그 칸이 비어 오면 그때만 글에서 JSON을 찾아 꺼냄(`parse_tool_calls`) → Unit 1 Dummy Agent처럼 손으로 오려 내는 일이 대부분 없어짐
  - `tool_choice="required"`: 매 바퀴 **반드시 도구를 불러야** 함. 최종 답도 `final_answer` 도구 호출(`{'answer': ...}`)로 냄. `final_answer`는 다른 도구와 같은 바퀴에 섞으면 에러
  - 한 바퀴에 도구 호출이 여러 개 오면 **동시에(병렬)** 실행 (`max_tool_threads`)
  - `WebSearchTool` = 기본 제공 웹 검색(기본 엔진 DuckDuckGo, `bing`도 가능). 이름 `web_search`는 `DuckDuckGoSearchTool`과 같음
- 실습 노트북: `code/tool_calling_agents_ollama.ipynb` (2026-11-22 만듦, 클라우드에서 가짜 모델로 2~4단계 실행 확인 — 진짜 Ollama 결과는 데스크탑에서). 원문 예제 + `tool_calls` 들여다보기 + **같은 계산 문제를 CodeAgent vs ToolCallingAgent로 비교**
- 내 말로 (2026-11-22): 툴 콜링 에이전트는 해야 되는 툴(도구 호출)을 파이썬 코드가 아니라 **JSON 블록 형태**로 만들어 줌. 내용이 간단함 (CodeAgent와 행동 모양만 다르고 나머지는 같아서)

#### 2.1 중간 정리 — 내 말로 (2026-11-22, 0~4번)

- 결국 **조립 키트**, 그러니까 AI 에이전트의 **프레임워크**에 대해 다루는 내용. 첫 번째로 HF가 만든 프레임워크 **smolagents**를 함
- 처음엔 smolagents의 **장점**에 대해 얘기함
- **CodeAgent**는 기본 에이전트. 행동을 **파이썬 코드로 직접** 써 주는 에이전트 → 이걸 바탕으로 CodeAgent를 알아봄
- **ToolCallingAgent**는 해야 되는 도구 호출을 파이썬 코드가 아니라 **JSON 블록** 형태로 만들어 줌
- AI 보충: CodeAgent가 코드로 "만드는" 건 **도구 자체가 아니라 도구를 부르는 행동**. 도구는 우리가 만들거나(`@tool`, `Tool` 클래스) 기본 제공 도구를 가져다 넣음 → 모델은 그 도구를 코드 안에서 `web_search(...)`처럼 **부름**. 두 에이전트 모두 도구는 같고, **부르는 방식**만 코드 vs JSON

## 유닛 2 한 페이지 요약

<!-- 유닛 끝나고 "프레임워크 3개를 언제 무엇을 쓰나"를 친구에게 3분 안에 설명한다고 생각하고 쓴다 -->

