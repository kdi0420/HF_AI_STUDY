# 질문 · 막힌 점

공부하다 생긴 질문을 바로 적는다. 해결되면 답과 출처(코스 섹션, AI, 친구, Discord)를 남긴다.
친구와 만날 때 "미해결"만 훑으면 된다.

## 미해결

<!-- - [Unit 1 §4] 질문 내용 (YYYY-MM-DD) -->

- [Unit 1 Dummy Agent] Ollama + `qwen3.5:9b`에서는 왜 마지막 assistant 메시지 "이어 쓰기"(원문 6-A 방식)가 안 되나? 채팅 템플릿이 지원 안 하는 것으로 추정(미확인). 관찰을 user 메시지로 보내는 6-B는 됨 (2026-11-16)

## 해결됨

- [Unit 1 Tools · 곁가지] LLM이 도구를 쓰려면 도구가 있다는 걸 미리 알아야 하는데, 도구가 수백~수만 개면 어떻게 다 아나? (2026-11-22)
  - 답: 기본은 **매 호출마다 도구 이름·설명·인자를 system prompt(또는 API의 `tools` 칸)에 넣는 것**. 수십 개까진 괜찮지만 많아지면 토큰 비용이 늘고 컨텍스트 창을 차지하고 고르는 정확도도 떨어진다. 그래서 다 넣지 않는다: (1) **도구 검색**: 도구 설명을 벡터 저장소에 넣고 질문과 비슷한 것만 골라 넣기(도구판 RAG), 또는 "도구 찾는 도구"를 하나 주기. (2) **점진적 공개**: 처음엔 이름·한 줄 설명만, 필요할 때 전체 설명을 불러오기(Claude Code의 deferred tools + `ToolSearch`, 스킬 목록이 실제 예). (3) **묶음·계층**: MCP 서버별로 묶거나 멀티 에이전트로 나눠 하위 에이전트만 자기 도구를 앎. (4) **범용 도구 몇 개로 대체**: 코드 실행·터미널·웹 검색이 있으면 파이썬 라이브러리·명령어 수백만 개를 쓸 수 있고, 그건 모델이 학습으로 이미 안다. 실제로 똑똑한 에이전트는 도구 수십만 개가 아니라 범용 도구 수십 개 + 검색 구조. "만들까?"는 찾아도 없을 때만
  - 출처: AI (이 세션 Claude Code의 도구 목록 구조를 직접 관찰). [Tools](https://huggingface.co/learn/agents-course/unit1/tools)와 연결

- [Unit 1 TAO · 곁가지] TAO 루프에서 정확히 언제 멈추고 도구를 실행하나? (2026-11-22)
  - 답: LLM이 스스로 판단해서 멈추는 게 아니라, **프로그램이 정해 둔 멈춤 표시(stop sequence)**가 나오면 글쓰기를 끊는다. Dummy Agent에서는 `Observation:`이 멈춤 표시였다 → 끊긴 글에서 Action을 꺼내(파싱) 도구 실행 → 결과를 `Observation:` 뒤에 붙여 LLM을 **다시 호출**. 한 바퀴 = LLM 호출 1번. `final_answer`가 나오면 루프가 끝난다. 멈추지 않으면 LLM이 관찰 결과를 지어낸다(환각). CodeAgent는 코드 블록 끝 표시, 요즘 API는 `tool_calls` 응답이 같은 역할
  - 출처: AI + [Dummy Agent Library](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library)

- [Unit 2 CodeAgents · 곁가지] 필요한 도구가 미리 정의돼 있지 않으면 에이전트가 직접 도구를 만들 수 있나? 계산처럼 LLM이 해도 되지만 도구가 더 정확한 경우는 언제·어떻게 만들게 하나? (2026-11-22)
  - 답: 세 경우로 나뉜다. (1) **CodeAgent**는 행동 자체가 파이썬 코드라 계산·문자열 처리 같은 건 도구 없이 그 자리에서 코드로 한다 → 사실상 "즉석 도구". (2) **ToolCallingAgent(JSON)**는 목록에 있는 도구만 부를 수 있다. 없는 이름을 쓰면 "그런 도구 없음" 에러가 관찰로 돌아오고, 모델이 다른 방법을 찾거나 그냥 머리로 답한다. (3) 도구를 **오래 두고 다시 쓰려면** `create_tool(name, code)` 같은 "도구 만드는 도구"(메타 도구)를 하나 주면 된다. 만드는 것도 그냥 행동 하나라서 멈추는 시점은 평소와 같다(`Observation:` 앞에서 멈춤 → 프로그램이 코드를 실행해 함수 등록 → "등록됨" 관찰). 도구를 쓸지 말지는 LLM이 Thought에서 정하고, system prompt의 도구 설명·"계산은 도구로" 같은 지시로 유도한다(보장은 안 됨). LLM이 쓴 코드를 실행하므로 샌드박스가 필수. 연구 사례: LATM(LLM이 도구를 만들고 작은 모델이 씀), Voyager(만든 코드를 "스킬 창고"에 저장해 재사용)
  - 출처: AI. 코스 [CodeAgents](https://huggingface.co/learn/agents-course/unit2/smolagents/code_agents)와 연결. 메타 도구 코드 예시는 개념 스케치(실행 검증 안 함)

- [Unit 1 실습 준비] 남은 실습 2개(Dummy Agent, smolagents 첫 에이전트)는 집 데스크탑(Ollama)에서 해야 하나, 노트북에서 HF 토큰으로 할 수 있나? 유료인가? (2026-11-16)
  - 답: 둘 다 가능. **토큰 발급은 무료**지만 **2026-10 무렵부터 무료 계정의 월 크레딧이 0**(전엔 $0.10)이라, HF 서버 모델을 부르려면 크레딧 구매 또는 PRO(약 $9/월, 월 $2 크레딧 포함 — 가격은 제3자 자료, 공식 미확인)가 필요. 실습 비용 자체는 몇 센트 수준 추정(미확인). 무료로 하려면 데스크탑 Ollama로 모델만 교체: Dummy Agent는 Ollama의 OpenAI 호환 주소(`localhost:11434/v1`), smolagents는 `LiteLLMModel("ollama_chat/qwen3.5:9b")`로 Space 대신 로컬에서 `app.py` 실행. 단 HF Space는 집 PC의 Ollama에 접근 못 하므로 Space에 올린 버전은 크레딧 필요
  - 출처: [Inference Providers Pricing](https://huggingface.co/docs/inference-providers/pricing) (Free Users: Monthly Credits "None"), [Dummy Agent Library](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library), [Tutorial](https://huggingface.co/learn/agents-course/unit1/tutorial)
- [Unit 1 What is an Agent?] reasoning(추론)과 planning(계획)은 뭐가 다른가? agency는 한국어로? (2026-11-15)
  - 답: reasoning = 상황을 따져 결론 내기("원두가 없네 → 먼저 사야 함"), planning = 그 결론으로 단계 순서 짜기. 관찰 결과가 다르면 다시 추론해 계획을 고친다(Think 단계). agency = 행위 주체성(스스로 판단해 행동하는 능력)
  - 출처: AI + [What is an Agent?](https://huggingface.co/learn/agents-course/unit1/what-are-agents)
- [Unit 1 What are LLMs?] 우리가 쓰는 LLM도 질문 → 답이니 Seq2Seq 아닌가? 왜 대부분 디코더라고 하나? (2026-11-15)
  - 답: 인코더/디코더/Seq2Seq는 하는 일이 아니라 내부 구조 이름. 디코더 전용 LLM은 질문과 답을 한 줄로 이어 붙여 "이어쓰기"를 하고, 질문 이해도 같은 디코더 안에서 한다. 구조가 단순하고 아무 글로나 다음 토큰 맞히기 학습이 돼서 키우기 쉬워 대세
  - 출처: AI + [What are LLMs?](https://huggingface.co/learn/agents-course/unit1/what-are-llms)
- [Unit 1 What are LLMs?] 다음 토큰 맞히기만으로 어떻게 복잡한 능력이 나오나? 사전에 없는 단어는 어떻게 토큰화하나? (2026-11-15)
  - 답: 목표는 단순해도 함수는 수십억 파라미터이고, 방대한 글에서 잘 맞히려면 지식·논리를 익혀야 한다(추리소설 "범인은 ___"). 왜 이렇게까지 잘 되는지는 아직 연구 중. 미등록 단어는 서브워드(BPE)로 아는 조각 → 글자 → 바이트까지 쪼개서 항상 표현된다(SmolLM2로 직접 확인: `flurbonixation` 5토큰, `안녕하세요` 14토큰)
  - 출처: AI (실험은 SmolLM2 tokenizer.json)
- [Unit 1 실습 준비] HF Access Token의 "토큰"은 LLM 토큰과 같은 말인가? 어떤 토큰을 받아야 하나? (2026-11-15)
  - 답: 다르다. LLM 토큰 = 글 조각, Access Token = 내 계정 출입증(비밀 문자열 `hf_...`). Read 토큰 하나면 됨: Dummy Agent(환경변수 `HF_TOKEN`), smolagents 튜토리얼(Space Secret `HF_TOKEN`). Messages 섹션은 불필요. 호출 권한 오류가 나면 Fine-grained + "Make calls to Inference Providers"로 재발급(미확인)
  - 출처: [Dummy Agent Library](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library), [Tutorial](https://huggingface.co/learn/agents-course/unit1/tutorial)

- [Unit 0 Onboarding Step 5] Claude Code로 돌리는 것과 로컬(Ollama)에서 돌리는 것은 뭐가 다르지? 로컬에 까는 의미는? (2026-11-12)
  - 답: AI 도구 = **모델(두뇌)** + **에이전트 프로그램(몸: 파일 읽기·명령 실행·반복 루프)**. Claude Code는 몸은 내 컴퓨터(또는 클라우드 컨테이너)에서, 두뇌(Claude 모델)는 Anthropic 서버에서 돌아간다. Ollama는 두뇌를 내 GPU에서 돌린다. 둘은 바꿔 끼울 수 있다(`ollama launch claude` = Claude Code 몸 + 로컬 두뇌). 로컬의 의미: 무료·무제한 반복, 데이터가 밖으로 안 나감, 오프라인, 모델을 직접 고르고 비교할 수 있음. 대신 9B 로컬 모델은 Claude 같은 최상위 모델보다 훨씬 덜 똑똑하다 → 공부·실험·개인정보용, 진짜 일은 큰 모델.
  - 출처: AI. 이 구분이 Unit 1의 "에이전트 = LLM + 도구 + 루프"와 같은 이야기
- [Unit 0 Onboarding] Ollama는 무료·무제한인데 코스는 왜 기본으로 HF 서버 모델을 쓰라고 할까? (2026-11-12)
  - 답: (1) 설치 없이 누구 컴퓨터에서든 같은 코드가 돌아가야 해서, (2) 서버 쪽 모델이 훨씬 커서 에이전트 형식을 덜 틀려서, (3) 결과물을 HF Space에 올리면 그 안에서 돌아가야 하는데 무료 Space엔 GPU가 없어 로컬 모델을 못 돌리고 API를 불러야 해서. 그래서 Ollama는 "크레딧 떨어졌을 때 연습용 대안"
  - 출처: AI (코스 원문엔 이유가 따로 안 적혀 있음 — 추론)

- [Unit 0 Onboarding Step 5] Ollama가 뭐고 장점·성질은? (2026-11-12)
  - 답: 오픈소스 LLM을 내 PC에 받아 `localhost:11434` 서버로 돌리는 프로그램. 무료·오프라인·프라이버시가 장점, PC 사양 의존·작은 모델이라 에이전트 성능이 약한 게 단점. smolagents에선 `LiteLLMModel`로 모델 한 줄만 바꾸면 됨. 자세한 건 `units/unit0-onboarding/notes.md` "Step 5 메모"
  - 출처: [Onboarding Step 5](https://huggingface.co/learn/agents-course/unit0/onboarding#step-5-running-models-locally-with-ollama-in-case-you-run-into-credit-limits) + AI

<!--
- [Unit 1 §4] 질문 내용
  - 답:
  - 출처:
-->
