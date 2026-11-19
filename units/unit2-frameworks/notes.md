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
| 1 | [Introduction to smolagents](https://huggingface.co/learn/agents-course/unit2/smolagents/introduction) | 2.1에서 뭘 배우나 (Alfred 파티 준비 예시) | [ ] |
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

- 내 말로:

## 유닛 2 한 페이지 요약

<!-- 유닛 끝나고 "프레임워크 3개를 언제 무엇을 쓰나"를 친구에게 3분 안에 설명한다고 생각하고 쓴다 -->

