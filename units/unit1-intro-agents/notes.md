# Unit 1 — Introduction to Agents

- 링크: [Unit 1 소개](https://huggingface.co/learn/agents-course/unit1/introduction)
- 목표일: 11/15 · 끝나면 **기초 인증서**
- 이 유닛의 결과물: smolagents로 만든 에이전트 **Alfred**를 HF Space에 올리기 + 최종 퀴즈 통과
- 실습 전 준비: **HF Access Token 발급**(Settings → Access Tokens → Read). 클라우드 세션에선 `request_credential`로 환경 비밀에 저장, 데스크탑에선 `.env`. HF 크레딧이 떨어지면 데스크탑 Ollama(`qwen3.5:9b`)로 교체 — Unit 0 노트 Step 5

## 진도

목차는 코스 원문과 대조함 (2026-11-12). 한국어판: https://huggingface.co/learn/agents-course/ko/unit1/introduction

| # | 섹션 | 끝나면 설명할 수 있어야 하는 것 | 완료 |
|---|---|---|---|
| 1 | [What is an Agent?](https://huggingface.co/learn/agents-course/unit1/what-are-agents) | 에이전트 = 무엇이 무엇을 하는 시스템인가? 챗봇과 뭐가 다른가? | [x] |
| 2 | [Quick Quiz 1](https://huggingface.co/learn/agents-course/unit1/quiz1) | 틀린 문제 → `quiz.md` | [x] |
| 3 | [What are LLMs?](https://huggingface.co/learn/agents-course/unit1/what-are-llms) | LLM이 "다음 토큰 예측기"라는 게 에이전트에 어떤 의미인가? | [x] |
| 4 | [Messages and Special Tokens](https://huggingface.co/learn/agents-course/unit1/messages-and-special-tokens) | 채팅 메시지(system/user/assistant)가 실제로 모델에 어떻게 들어가나? 채팅 템플릿은 왜 필요한가? | [x] |
| 5 | [What are Tools?](https://huggingface.co/learn/agents-course/unit1/tools) | 도구는 어떻게 정의하고, LLM은 도구를 어떻게 "아는가"? (system prompt에 도구 설명) | [x] |
| 6 | [Quick Quiz 2](https://huggingface.co/learn/agents-course/unit1/quiz2) | 틀린 문제 → `quiz.md` | [x] |
| 7 | [Thought–Action–Observation 사이클](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure) | 루프가 한 바퀴 도는 과정을 예시로 말할 수 있나? | [x] |
| 8 | [Thought (ReAct)](https://huggingface.co/learn/agents-course/unit1/thoughts) | ReAct가 뭐고, 왜 "생각하고 행동하기"가 성능을 올리나? | [x] |
| 9 | [Actions](https://huggingface.co/learn/agents-course/unit1/actions) | JSON 액션 vs 코드 액션(code agent)의 차이와 장단점은? 멈추고 파싱하는 방식은? | [x] |
| 10 | [Observe](https://huggingface.co/learn/agents-course/unit1/observations) | 도구 실행 결과가 어떻게 다시 모델 입력으로 들어가나? | [x] |
| 11 | [Dummy Agent Library](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library) | 프레임워크 없이 에이전트 루프를 손으로 짜면 어떤 모양인가? | [~] 읽음, 데스크탑 실행 남음 |
| 12 | [First Agent with smolagents](https://huggingface.co/learn/agents-course/unit1/tutorial) | `CodeAgent` + 도구 + 모델로 Alfred 만들고 Space에 올리기 | [ ] |
| 13 | [Final Quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz) | 통과 → 기초 인증서 | [ ] |
| 14 | [Conclusion](https://huggingface.co/learn/agents-course/unit1/conclusion) | 유닛 1 한 페이지 요약 쓰기 | [ ] |

## 섹션별 노트

<!-- 각 섹션: "내 말로 정리" 3~5줄 + 예시. 모르는 건 ../../questions.md, 용어는 ../../glossary.md -->

### 0. 소개 (로드맵) — 2026-11-15 읽음

- 유닛 1에서 배우는 것 4덩어리: ① 에이전트란 무엇이고 어떻게 판단하나(추론·계획) ② LLM = 에이전트의 "뇌", 대화는 Messages로 구조화 ③ 도구(Tools)로 바깥 세계에 작용 ④ Think → Act → Observe 루프
- 실습: `smolagents`로 **Alfred** 만들기 → HF Spaces에 공개 → 최종 퀴즈 통과 시 기초 인증서
- 큰 유닛이니 천천히, 여러 번 다시 와서 볼 것 (원문 권고)

### 1. What is an Agent? — 2026-11-15 읽음

- 원문 정의: AI 모델로 **환경과 상호작용**해 **사용자가 정한 목표**를 이루는 시스템. 추론 + 계획 + 행동(주로 도구로) 실행
- 구조: **뇌**(AI 모델, 무엇을 할지 결정) + **몸**(도구·능력, 할 수 있는 행동의 범위를 정함. 날개 없으면 "날기" 불가)
- Agency(행위 능력) 스펙트럼: LLM 출력이 프로그램 흐름을 얼마나 좌우하나 → 단순 처리기 ☆☆☆ → 라우터(분기) ★☆☆ → 도구 호출자 ★★☆ → 멀티스텝(반복 여부까지 결정) ★★★ → 멀티 에이전트(다른 에이전트를 실행) ★★★
- LLM은 **텍스트만** 생성 → ChatGPT가 이미지를 만드는 건 개발자가 붙인 **이미지 생성 도구**를 LLM이 호출하기 때문
- **Action ≠ Tool**: 행동 하나에 도구 여러 개를 쓸 수 있음 (커피 내오기 = 주방 이동 + 커피머신 + 가져오기). 도구 설계가 에이전트 품질을 크게 좌우
- 예시: 개인 비서(Siri 등), 고객센터 챗봇, 게임 NPC
- Q. reasoning과 planning은 뭐가 다른가? → reasoning = 상황을 따져 결론 내기("원두가 없네 → 먼저 사야 함"), planning = 그 결론으로 단계 순서 짜기. 관찰 결과가 예상과 다르면 다시 추론해서 계획을 고침 (2026-11-15)
- 내 말로:

### 2. What are LLMs? — 2026-11-15 읽음

- LLM = 대량의 텍스트로 학습해 사람 말을 이해·생성하는 모델. 대부분 **Transformer**(Attention 기반) 구조
- Transformer 3종: 인코더(BERT, 텍스트 → 의미 벡터, 분류·검색) / **디코더**(Llama, 토큰을 하나씩 생성, 챗봇·코드) / Seq2Seq(T5·BART, 번역·요약). **LLM은 보통 수십억 파라미터의 디코더**
- 핵심 원리: **앞 토큰들이 주어졌을 때 다음 토큰 예측**. 토큰 = 단어보다 작은 조각(`interest` + `ing`). Llama 2 어휘는 약 3.2만 토큰
- **Autoregressive**: 이번 출력이 다음 입력에 붙음 → **EOS 토큰**이 나오면 멈춤. 특수 토큰 모양은 모델마다 다름(`<|im_end|>`, `<|eot_id|>` …)
- 다음 토큰 고르기(디코딩): 점수 최댓값만 고르기(greedy) / beam search(후보 문장 여러 개의 총점 비교)
- Attention: 다음 토큰에 중요한 단어에 집중("The capital of **France** is …"). context length = 한 번에 볼 수 있는 최대 토큰 수
- 프롬프트가 중요: LLM이 하는 일은 입력을 보고 다음 토큰을 고르는 것뿐이라 입력 문구가 출력을 좌우
- 학습: 사전학습(pre-training, 다음 토큰 맞히기로 언어 패턴 습득) → 파인튜닝(대화·도구 사용 등 특정 작업)
- 쓰는 법: 로컬 실행 vs 클라우드/API. 코스는 주로 HF API 사용 (나는 데스크탑 Ollama도 있음)
- 에이전트에서: LLM = **뇌**. 지시 해석, 대화 맥락 유지, 계획, 도구 선택
- 노트북 실습엔 HF 토큰 + **Meta Llama 모델 접근 신청** 필요
- Q. Transformer·인코더·디코더·Seq2Seq가 뭔가? → Transformer = 모든 토큰이 서로를 보고 "누가 중요한지" 가중치를 매기는(Attention) 신경망 설계도. 인코더 = 문장 전체를 앞뒤로 다 보고 의미 벡터로 요약(독해 담당), 디코더 = 앞 토큰만 보고 다음 토큰 생성(이어쓰기 담당), Seq2Seq = 인코더가 입력을 다 읽고 디코더가 그걸 참고해 새 문장 생성(통역사). 큰 디코더는 프롬프트만으로 번역·요약도 해서 LLM은 대부분 디코더 (2026-11-15)
- Q. 우리가 쓰는 LLM도 질문을 이해하고 답을 만드니까 사실 Seq2Seq 아닌가? → **하는 일(입력→출력)**로 보면 맞지만, 인코더/디코더/Seq2Seq는 **내부 구조** 이름. 디코더 전용 LLM은 질문과 답을 **이어진 글 한 줄**로 보고, 질문 읽기(이해)도 같은 디코더 안에서 함. 별도 인코더 부품이 없을 뿐 이해를 안 하는 건 아님. 구조가 단순하고, 인터넷 글 아무거나로 "다음 토큰 맞히기" 학습이 돼서 크게 키우기 쉬워 대세가 됨 (2026-11-15)
- 헷갈렸던 것: "토큰을 하나 만들면 다음 토큰을 학습한다"가 아님. **학습은 미리 끝나 있고**, 답할 때는 학습 없이 "예측 → 붙이기 → 다시 예측"만 반복 (2026-11-15)
- Q. 다음 토큰 맞히기만으로 어떻게 이렇게 복잡한 능력이 나오나? → ① 단순한 건 **목표**지 **함수**가 아님(수십억 파라미터). ② 방대한 글에서 다음 토큰을 잘 맞히려면 문법·지식·논리를 안에 익혀야 함(추리소설 마지막 "범인은 ___" 맞히려면 줄거리를 이해해야 함). ③ 한 토큰씩이라도 매번 앞 글 전체를 보고 이어 가므로, 긴 글 = 작은 결정 수천 번의 연쇄(단순 규칙 반복 → 복잡한 모양: 만델브로 집합 z²+c). ④ 파인튜닝으로 "도움 되는 답" 쪽으로 다듬음. 다만 **왜 이렇게까지 잘 되는지는 아직 완전히 밝혀지지 않음**(해석 가능성 연구 중) (2026-11-15)
- Q. 사전에 없는 단어는 어떻게 토큰화하나? → 서브워드 토큰화(BPE 등). 사전에 글자·**바이트** 단위 조각까지 다 들어 있어서 아는 큰 조각으로 최대한 자르고, 모르면 더 잘게 자름 → "모르는 단어"가 생기지 않음. 직접 확인(SmolLM2 토크나이저, 어휘 49,152개): `flurbonixation` → `fl` `ur` `bon` `ix` `ation` 5개 / `안녕하세요` → 바이트 단위 14개 (영어 위주 모델이라 한국어는 잘게 쪼개짐 = 토큰 더 많이 듦) (2026-11-15)
- 내 말로: 디코더는 결국 다음 단어(정확히는 토큰) 맞히기만 하는 것. 질문이랑 답을 하나로 합쳐서 다음에 뭐가 올지 예측하고, 우리가 쓰는 대부분의 LLM이 디코더 (보충: 목표는 단순해도, 아주 많은 글에서 다음 토큰을 잘 맞히려면 문법·사실·추론 패턴까지 익혀야 해서 결과적으로 똑똑해짐)
- 인코더는 사람이 한 말을 AI가 다룰 수 있는 숫자 벡터로 바꿔 주는 것 (보충: 디코더도 안에서 글을 숫자로 바꾸긴 함. 인코더의 특징은 **출력이 의미 벡터**라서 분류·검색에 쓰고, 새 글은 못 쓴다는 것)

### 3. Messages and Special Tokens — 2026-11-15 읽음

- 채팅 화면의 "메시지 여러 개"는 **UI용 겉모습**. 모델에 들어가기 전에 **전부 이어 붙여 긴 글 하나(프롬프트)**가 됨. 모델은 대화를 기억하지 않고 **매번 처음부터 전체를 다시 읽음**
- 메시지 = `{"role": ..., "content": ...}`. role 3종: **system**(행동 규칙, 계속 유지되는 지시) / **user**(사람) / **assistant**(모델)
- 에이전트에서 system 메시지 = 쓸 수 있는 **도구 목록**, 액션 형식, 생각을 나누는 방식까지 담는 곳 (다음 섹션 Tools와 연결)
- **채팅 템플릿** = 메시지 리스트 → 그 모델 전용 형식의 문자열로 바꾸는 변환 규칙. 모델마다 구분용 **특수 토큰**이 다름: SmolLM2는 `<|im_start|>`·`<|im_end|>`(ChatML), Llama 3.2는 `<|start_header_id|>`·`<|eot_id|>`
- **Base 모델**(다음 토큰 예측만 학습, `SmolLM2-135M`) vs **Instruct 모델**(지시·대화에 맞게 파인튜닝, `SmolLM2-135M-Instruct`). Instruct 모델은 **학습 때 쓴 템플릿 그대로** 넣어야 제대로 답함
- `transformers`에선 템플릿이 **Jinja2 코드**로 토크나이저에 들어 있음 → `tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)` 한 줄이면 끝. API 서버도 뒤에서 이걸 씀
- 직접 확인 (SmolLM2-1.7B-Instruct 토크나이저, 2026-11-15):
  - system 메시지를 안 넣어도 템플릿이 **기본 system("You are a helpful AI assistant named SmolLM...")을 자동으로 붙임**
  - `add_generation_prompt=True` → 맨 끝에 `<|im_start|>assistant`가 붙음 = "이제 네 차례" 신호. `False`면 마지막 user 메시지에서 끝남 (원문 Jinja 예시 출력이 이 경우)
  - `<|im_start|>`는 글자 조각이 아니라 **토큰 1개**(id 1), `<|im_end|>`도 1개(id 2)이고 이게 곧 **EOS 토큰** → 모델이 `<|im_end|>`를 내면 답 끝
  - 예시 대화 3개 + 기본 system → 토큰 69개
- 입문자용 비유 (2026-11-15 다시 설명 요청): 채팅 = **연극 대본**. 메시지마다 배역 이름표(특수 토큰)를 붙여 대본 한 권으로 묶고, 끝에 `assistant:` 이름표만 적어 두면 "이어쓰기 기계"인 모델이 알아서 assistant 대사를 씀 → 다 쓰면 `<|im_end|>`로 멈춤. 모델은 기억력이 없어서 앱이 **매번 대본 전체를 다시 보냄**(대화가 길수록 토큰·비용 증가, context length 한계). 모델마다 대본 양식이 달라 템플릿(메일머지 같은 빈칸 틀)으로 맞춰 줌
- 내 말로:

### 4. What are Tools? — 2026-11-15 읽음

- 도구(Tool) = **LLM에게 주는 함수**. 목적이 분명해야 함. 예: 웹 검색, 이미지 생성, 검색(Retrieval), 외부 API(GitHub·YouTube·Spotify)
- 좋은 도구 = **LLM의 약점을 메워 주는 것**: ① 계산(계산기가 모델 자체 계산보다 정확) ② 최신 정보(모델 지식은 학습 시점에서 멈춤 → 도구 없이 오늘 날씨를 물으면 지어냄 = hallucination)
- 도구의 구성: **설명 글** + **호출 가능한 것(callable, 실제로 일하는 함수)** + **타입 붙은 인자** + (선택) 타입 붙은 출력
- 동작 원리: LLM은 글만 쓸 수 있어서 도구를 **직접 못 부름**. LLM은 `call weather_tool('Paris')` 같은 **"호출해 달라는 글"**을 쓰고 → **에이전트(프로그램)**가 그 글을 읽고 진짜로 실행 → 결과를 새 메시지로 대화에 붙여 LLM에게 다시 보냄 → LLM이 자연스러운 답을 씀. 사용자에겐 이 중간 과정이 안 보임
- 도구를 알려 주는 방법: **system prompt에 도구 설명 글을 넣음**. 무엇을 하는지 + 정확히 어떤 입력을 받는지를 **정확하고 일관된 형식**(코드·JSON 등)으로
- 예: `Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int`
- 손으로 쓰면 실수하기 쉬움 → 파이썬 함수에 이미 정보가 다 있음(함수 이름, **docstring**, **타입 힌트**) → `inspect`로 뽑아내는 `@tool` **데코레이터**를 붙이면 `to_string()`이 설명 글을 자동 생성
- `Tool` 클래스: name·description·func·arguments·outputs를 담고, `to_string()`(설명 글 만들기)과 `__call__()`(도구를 함수처럼 부르면 실제 함수 실행) 제공. 원문 말로는 가상의 구현이지만 실제 라이브러리와 거의 같음
- **MCP**(Model Context Protocol) = 도구를 LLM에 연결하는 **공통 규격(오픈 프로토콜)**. 한 번 만든 도구를 MCP 지원하는 어떤 프레임워크·모델에서든 재사용. 비유: USB-C 포트 (예: 지금 Claude 세션에 붙은 Todoist·Google Calendar 커넥터가 MCP 서버)
- 직접 확인 (원문 `Tool` + `@tool` 코드 실행, 2026-11-15):
  - `calculator.to_string()` → 원문과 똑같은 설명 글이 나옴
  - `calculator(6, 7)` → `42` (`__call__` 덕분에 도구 객체를 함수처럼 부를 수 있음)
  - 타입 힌트·docstring을 **뺀** 함수에 `@tool`을 붙이면 → `Description: No description provided., Arguments: x: _empty, y: _empty, Outputs: No return annotation` → LLM이 뭘 넣어야 할지 알 수 없음. 그래서 원문이 "타입 힌트·docstring·이름을 잘 지어라"고 함
- 입문자용 비유: LLM = **전화로 지시만 하는 상황실 직원**(손이 없음), 에이전트 = **현장 요원**(지시서대로 실제 실행 후 결과 보고), system prompt의 도구 설명 = 상황실 벽에 붙은 **"쓸 수 있는 장비 목록"**
- 내 말로:

### 5. Thought–Action–Observation 사이클 — 2026-11-15 읽음

- 에이전트의 일 = **Thought(생각) → Action(행동) → Observation(관찰)**을 목표를 이룰 때까지 반복하는 **while 루프**
  - Thought: LLM이 다음 단계를 정함 / Action: 도구를 인자와 함께 호출 / Observation: 도구 결과를 보고 되돌아봄
- 많은 프레임워크는 이 규칙을 **system prompt에 직접 적어 둠**: ① 에이전트의 행동 방식 ② 쓸 수 있는 도구(Tools 섹션) ③ 사이클 형식(`Thought:` → `Action:` JSON → … → `Final Answer:`)
- 예시 (날씨 에이전트 Alfred, "뉴욕 날씨?"): Thought "날씨 도구로 최신 정보부터" → Action `{"action": "get_weather", "action_input": {"location": "New York"}}` → Observation "partly cloudy, 15°C, 60% humidity" (프롬프트에 추가) → Thought "이제 답할 수 있다" → `Final Answer: ...` → 루프 끝
- 배울 점 3가지(원문): ① 목표를 이룰 때까지 **반복**(관찰이 에러·부족이면 다시 루프) ② 도구로 학습 시점 너머의 **실시간 정보** ③ 매 바퀴 새 관찰을 생각에 반영(**동적 적응**)
- 이 구조가 다음 섹션의 **ReAct**(Reasoning + Acting)
- 직접 확인: `code/tao_loop_demo.py` (가짜 LLM + 가짜 날씨 도구, 토큰 불필요). 바퀴 1 = Thought+Action → 에이전트가 JSON을 읽고 도구 실행 → Observation을 대본에 붙임, 바퀴 2 = Thought+Final Answer → 루프 탈출. LLM은 **글만 쓰고**, 루프·JSON 읽기·도구 실행·대본 붙이기는 전부 **에이전트 코드**가 함
- 입문자용 비유: **요리 레시피 없이 요리하기** — 생각("간을 봐야겠다") → 행동(맛보기) → 관찰("싱겁다") → 생각("소금 조금") → … → "완성!"에서 멈춤
- 내 말로:

### 6. Thought (ReAct) — 2026-11-15 읽음

- Thought = 에이전트의 **내부 추론·계획**("속마음 독백"). 프롬프트에 들어온 정보(질문, 지난 관찰)를 분석해 **다음 Action을 정함**. 큰 문제를 작은 단계로 쪼개고, 지난 시도를 돌아보고, 새 정보로 계획을 고침
- Thought 종류(원문 표): 계획 · 분석 · 결정 · 문제 해결 · 기억 활용 · 자기 반성 · 목표 설정 · 우선순위
- 함수 호출(function-calling)용으로 파인튜닝된 모델은 Thought가 **선택 사항** (Actions 섹션에서 자세히)
- **CoT**(Chain-of-Thought): "Let's think step by step"으로 **답 전에 단계별로 생각**하게 하는 **프롬프팅 기법**. 도구 없이 머릿속으로만 → 논리·수학에 강함. 예: 15% of 200 = 10%(20) + 5%(10) = 30
- **ReAct**(Reasoning + Acting): 생각 사이사이에 **행동(도구 사용)을 끼워 넣는** 프롬프팅 기법. Thought → Action → Observation 반복 = 앞 섹션 TAO 사이클의 정식 이름
- CoT vs ReAct: 둘 다 단계별 논리 ✅ / 외부 도구는 ReAct만 / CoT = 논리·수학·내부 작업, ReAct = 정보 찾기·여러 단계의 동적 작업
- 원문 그림 (d) = ReAct 논문(Yao et al., 2022)의 비교 그림 (a 그냥 답 · b CoT · c 행동만 · d ReAct). CoT만 쓰면 사실을 지어내고, 행동만 하면 검색 결과를 엮지 못하는데, ReAct는 둘을 합쳐 맞힘 (그림 자체는 붙여넣기에 빠져 있어서 미확인)
- **추론 모델**(DeepSeek R1, OpenAI o1): `<think>…</think>` 토큰으로 생각과 최종 답을 구분하도록 **학습 단계에서** 배운 모델. CoT·ReAct는 **프롬프트로 시키는 것**, 이건 **훈련으로 몸에 밴 것**
- 입문자용 비유: CoT = **연습장에 풀이 쓰고 답 쓰기**(시험장, 책 없음), ReAct = **오픈북 과제**(풀이 쓰다가 "이건 찾아봐야겠다" → 책 펴기 → 찾은 내용 보고 이어서 풀이), 추론 모델 = 시키지 않아도 **풀이부터 쓰는 습관이 든 학생**
- 내 말로:

### 7. Actions — 2026-11-15 읽음

- Action = 에이전트가 **환경(바깥세상)과 상호작용하는 구체적인 단계**. 웹 검색, 기기 조작 등 하나하나가 **의도된 작업**. 예: 고객 상담 에이전트 → 고객 정보 조회, 도움말 문서 안내, 사람 상담원에게 넘기기
- 에이전트 종류(Action을 어떻게 쓰나):
  - **JSON Agent**: Action을 JSON으로 씀
  - **Code Agent**: 코드 블록을 쓰고, 바깥(실행기)이 실행
  - **Function-calling Agent**: JSON Agent의 하위 종류. Action마다 **새 메시지를 따로 만들도록 파인튜닝**됨
- Action의 목적 4가지: 정보 수집(검색·DB·문서) · 도구 사용(API·계산·코드 실행) · 환경 조작(화면 UI·물리 기기) · 소통(사용자와 채팅, 다른 에이전트와 협업)
- 핵심: LLM은 **글만** 다룸 → Action(도구 이름 + 인자)을 글로 **설명**할 뿐. 완전한 Action을 다 쓰면 **반드시 생성을 멈춰야(STOP)** 함 → 제어권이 LLM에서 에이전트로 넘어가고, 결과를 **파싱 가능**하게 유지
- **Stop and Parse** 3단계: ① 정해진 형식(JSON·코드)으로 쓰기 ② Action을 다 쓰면 **멈추기**(추가·잘못된 출력 방지) ③ **바깥 파서**가 읽어서 어떤 도구를, 어떤 인자로 부를지 꺼냄
- **Code Agent** 장점: 표현력(반복문·조건문·함수) · 모듈성·재사용 · 디버깅 쉬움(문법이 명확해 에러 찾기 쉬움) · 외부 라이브러리·API 직접 사용
- 주의: LLM이 쓴 코드를 실행하면 **보안 위험**(prompt injection, 해로운 코드). → 기본 안전장치가 있는 `smolagents` 같은 프레임워크 권장 ([보안 실행 문서](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution))
- Code Agent도 Stop and Parse를 따름: 코드 블록 경계를 명확히 하고, 끝을 신호로 알림(예: `final_answer` 출력)
- 직접 확인: `code/stop_and_parse_demo.py` (토큰 불필요). ① 멈추지 않은 가짜 LLM이 `Observation: sunny, 30°C`를 **지어냄** ② `Observation:`에서 자르기(stop) ③ JSON 파싱 → 진짜 도구 실행 → `partly cloudy, 15°C` ④ 코드 액션은 `for` 문 하나로 도시 3곳을 **한 번의 Action에** 처리
- 입문자용 비유: Action = **식당 주문서**. JSON Agent = 정해진 칸에 체크하는 **주문 용지**, Code Agent = 주방에 주는 **조리 지시서**("A 끓이고, 다 되면 B 넣고, 짜면 물 추가"), Stop = 주문서를 다 쓰면 **펜을 내려놓고 주방에 넘기기**(음식 나오기 전에 "맛있었다"까지 쓰면 안 됨), Parse = 주방에서 주문서를 **읽는 사람**
- 내 말로:

### 8. Observe — 2026-11-15 읽음

- Observation = 에이전트가 **자기 Action의 결과를 알아차리는 방법**. 환경이 보내는 **신호**(API 데이터, 에러 메시지, 시스템 로그) → 다음 Thought의 재료
- 관찰 단계에서 하는 일 3가지: ① **피드백 수집**(성공했나 실패했나) ② **결과 덧붙이기**(기존 컨텍스트에 추가 = 기억 갱신) ③ **전략 조정**(갱신된 컨텍스트로 다음 생각·행동을 다듬음)
- 예: 날씨 API가 "partly cloudy, 15°C, 60% humidity" → **프롬프트 끝에** 붙음 → 정보가 더 필요한지, 최종 답을 낼지 판단
- 피드백을 반복해서 반영 → 목표에 **동적으로 맞춰짐**. 관찰은 웹페이지 글부터 로봇 팔 위치까지 다양 = 도구의 **"로그"**(Action 실행 결과를 글로 알려 줌)
- 관찰 종류: 시스템 피드백(에러·성공 알림·상태 코드) · 데이터 변화(DB 갱신·파일 수정·상태 변화) · 환경 데이터(센서·시스템 지표·자원 사용량) · 응답 분석(API 응답·쿼리 결과·계산 결과) · 시간 이벤트(마감 도달·예약 작업 완료)
- 결과를 붙이는 순서(프레임워크가 함): ① Action **파싱**(어떤 함수, 어떤 인자) ② **실행** ③ 결과를 **Observation으로 덧붙이기**
- 여기까지가 TAO 사이클 전체. 흐릿해도 다음 유닛들에서 다시 다룸 → 이제 첫 에이전트 코딩
- 직접 확인: `code/observe_adapt_demo.py` (토큰 불필요). "NYC"로 불렀더니 `Observation: Error: unknown location` → 다음 Thought가 "전체 이름으로 다시" → `New York`으로 재시도 → 성공 → Final Answer. **에러도 관찰**이고, 그게 대본에 붙어야 전략을 바꿀 수 있음
- 입문자용 비유: **내비게이션** — 출발(Action) → GPS가 "경로 이탈"(Observation, 에러) → 경로 재탐색(새 Thought) → … → "목적지 도착"(Final Answer). GPS 신호가 없으면 내비는 계속 옛 경로만 안내함
- 내 말로:

### 9. Dummy Agent Library — 2026-11-16 읽음

- 왜 "더미(가짜)" 라이브러리? 코스는 특정 프레임워크에 묶이지 않으려 함 → **파이썬 함수 하나 = 도구**, 손으로 짠 코드 = 에이전트. 실제 서비스용은 아니고 **원리를 보는 출발점**. 다음은 smolagents, 이후 유닛에서 LangGraph·LlamaIndex
- **Serverless API**: 모델을 내 PC에 설치·배포하지 않고 HF 서버에 메시지를 보내 답만 받음. `InferenceClient(model="moonshotai/Kimi-K2.5", token=HF_TOKEN)` → `client.chat.completions.create(messages=..., max_tokens=..., stream=False)` → 답은 `output.choices[0].message.content`
  - `extra_body={'thinking': {'type': 'disabled'}}` = Kimi K2.5(추론 모델)의 **속생각 끄기**. 켜 두면 `<think>` 같은 생각이 먼저 나와 토큰을 씀
  - **chat 메서드를 권장**하는 이유: 채팅 템플릿(특수 토큰)을 서버가 알아서 씌워 줌 → **모델을 바꿔도 코드가 그대로**
- Dummy Agent의 system prompt = ① **도구 정보**(`get_weather`, 인자 `location`) ② **사이클 규칙**(Question → Thought → Action(JSON) → Observation … → `Final Answer:`)
  - 원문의 "The prompt now is"에 보이는 `<|begin_of_text|>`, `<|start_header_id|>`는 **Llama 3의 특수 토큰**. 모델은 Kimi인데 예시는 Llama 3 것 → 예전 판의 흔적으로 보임(미확인). 요점은 "system → user → **비어 있는 assistant 자리**로 끝남 = 모델이 거기부터 씀"
  - 프롬프트의 `{{ }}`는 그냥 문자열이라 모델에게 **중괄호 두 개 그대로** 보임 (원문 템플릿의 흔적, 동작엔 큰 문제 없음)
- **문제**: 멈추지 않으면 모델이 `Observation: ... 12°C`를 **지어냄(환각)**. 다음 토큰 예측기라서 형식상 Observation 자리가 오면 그럴듯한 글을 채워 넣을 뿐, 도구를 부를 손이 없음
- **해결**: `stop=["Observation:"]` → `Observation:` 직전에서 생성이 멈춤(그 글자는 안 나옴) → 제어권이 우리 코드로
- 가짜 도구 `get_weather(location)` → 고정 문장 반환 (진짜라면 날씨 API)
- **이어 쓰기**: messages에 assistant 메시지로 `모델이 쓴 Thought+Action` + `"Observation:\n"` + `진짜 도구 결과`를 넣고 다시 부르면 → 모델이 그 뒤를 이어 `Final Answer:`를 씀
  - 원문의 마지막 "new prompt" 예시는 `action_input`이 `{"type": ..., "value": "London"}`로 앞과 달라짐 → 예시 정리가 덜 된 것. 흐름만 보면 됨
- 원문 결론: 프레임워크 없이 하면 **손이 많이 감(tedious)** → smolagents 같은 라이브러리가 이 일을 대신함

| 손으로 한 일 | TAO에서 | 프레임워크가 대신 |
|---|---|---|
| system prompt에 도구 설명·규칙 쓰기 | (준비) | `@tool`의 이름·docstring·타입 힌트로 자동 생성 |
| `stop=["Observation:"]`으로 멈추기 | Thought + Action | 자동 |
| JSON에서 도구 이름·인자 꺼내기 (원문은 생략하고 `get_weather('London')` 직접 호출) | Action 파싱 | 자동 |
| 도구 실행 | Action 실행 | 자동 |
| 결과를 `Observation:`으로 붙여 다시 호출 | Observation | 자동 |
| `Final Answer:`가 나올 때까지 반복 | 루프 | `while` + 최대 횟수 |

- 우리 실습: 무료 크레딧 0 → **데스크탑 Ollama(`qwen3.5:9b`)로**. `code/dummy_agent_ollama.py` (기본 패키지만, 토큰 불필요). 원문의 `client.chat.completions.create`를 `localhost:11434/api/chat` 호출로 바꾼 것뿐이고, `think=False`가 원문의 thinking disabled, `num_predict`가 `max_tokens`. 원문과 달리 모델이 쓴 JSON에서 `location`을 **파싱**해서 도구를 부름. 클라우드에선 가짜 서버로 흐름만 검증, 실제 qwen3.5 결과는 데스크탑에서 확인 필요
- 입문자용 비유: **대본 리딩에서 상대역 대사 끊기** — 모델(배우)은 혼자 두면 상대역(도구) 대사까지 지어내 읽음 → 감독(에이전트 코드)이 "Observation:"에서 "컷!" → 진짜 상대역 대사를 대본에 써 넣고 → "거기서부터 다시" → 배우가 마지막 대사(Final Answer)를 읽음
- 실습 방식(2026-11-16): 사용자가 한 칸씩 실행·확인하고 싶어 함 → **데스크탑 Jupyter 노트북** `code/dummy_agent_ollama.ipynb` (0단계 Ollama 확인 ~ 6단계 원문 재현, 6-B 관찰을 user 메시지로, 7단계 도전 `while` 루프로 자동화). 환경 준비·실행법: `practice-guide.md`. Colab은 데스크탑 Ollama에 접속할 수 없어서 제외
- 실행 결과 (데스크탑):
  - 0~1단계 통과 (2026-11-16): `qwen3.5:9b` 확인, "The capital of France is" → Paris 답
  - `chat()` 함수 (내 말로 + 보충): "AI한테 말을 걸어 주는 애". messages를 받아 **모델 이름·옵션과 함께 요청(편지 봉투)으로 포장 → Ollama 서버에 보내기 → 답장에서 본문만 꺼내 돌려주기**. 따로 만든 이유 = 이 15줄을 3·4·6·7단계에서 계속 써야 해서 (원문의 `client.chat.completions.create`도 남이 만들어 둔 같은 역할의 함수)
  - `max_tokens` = 답 길이의 **상한선**(목표 길이 아님). 모델이 먼저 끝내면 짧게 끝나고(Paris), 넘으면 중간에 잘림
  - 2단계: system prompt = 모델용 **근무 매뉴얼**. ① 일·도구 목록 ② 도구 호출 양식(JSON) ③ 답하는 순서(Thought→Action→Observation→…→`Final Answer:`). 사람용 설명이 아니라 **우리 코드가 모델 글을 읽기 위한 형식 약속**
  - 3단계 (2026-11-16): 실행할 때마다 `get_weather` Action을 씀. 그런데 이때 `get_weather` **함수는 아직 없음**(5단계에서 만듦) → 모델은 system prompt의 **설명 글**만 보고 "이런 도구가 있다"고 믿고 호출 **글**을 쓴 것. 뒤에 붙는 날씨 결과가 실행마다 달라짐 = 도구를 안 부르고 **지어낸 것**(환각)이라는 증거. 모델은 다음 토큰을 확률로 골라서 매번 조금씩 다르게 씀
- 내 말로:

### 10. First Agent with smolagents

- 만든 Space 링크:
- 추가한 도구:
- 막혔던 점:

## 유닛 1 한 페이지 요약

<!-- 유닛 끝나고 "에이전트란?"을 친구에게 3분 안에 설명한다고 생각하고 쓴다 -->

-
