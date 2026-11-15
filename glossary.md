# 용어집

공부하면서 나온 용어를 누적한다. **내 말로** 한 줄, 필요하면 예시. 처음 나온 유닛을 적어 둔다.

| 용어 | 한 줄 정의 (내 말로) | 처음 나온 곳 |
|---|---|---|
| Agent | | Unit 1 |
| Tool | LLM에게 주는 함수. LLM은 "이 도구를 이렇게 불러 줘"라는 글만 쓰고, 실제 실행은 에이전트 프로그램이 함. system prompt의 설명 글로 존재를 알려 줌 | Unit 1 |
| Agency (행위 주체성) | 스스로 판단해 행동하는 능력. 에이전트가 환경에 작용할 수 있는 정도. LLM 출력이 프로그램 흐름을 얼마나 결정하느냐로 단계를 나눔 (☆☆☆ 단순 처리기 ~ ★★★ 멀티스텝·멀티 에이전트) | Unit 1 |
| Reasoning vs Planning | Reasoning(추론) = 주어진 정보로 "무엇이 필요하고 지금 상황이 어떤가"를 따져 결론을 끌어내기. Planning(계획) = 그 결론을 바탕으로 단계 순서 짜기. 추론이 먼저, 계획은 추론의 결과물 | Unit 1 |
| Action vs Tool | Action = 목표를 위해 하는 행동, Tool = 그때 쓰는 개별 기능(함수). 행동 하나에 도구 여러 개가 들어갈 수 있음 | Unit 1 |
| VLM | Vision Language Model. 텍스트에 더해 이미지도 입력으로 받는 LLM | Unit 1 |
| Thought / Action / Observation | 에이전트가 반복하는 3단계. Thought = LLM이 다음 할 일을 정함, Action = 도구를 인자와 함께 호출(보통 JSON 글), Observation = 도구 결과를 대본에 붙여 다시 LLM에게. `Final Answer`가 나오면 끝 | Unit 1 |
| ReAct | | Unit 1 |
| while 루프 | "조건이 맞는 동안 계속 반복"하는 코드 구조. 에이전트는 목표를 이룰 때까지(최종 답이 나올 때까지) 사이클을 반복. 무한 반복을 막으려 보통 최대 횟수를 둠 | Unit 1 |
| Token | LLM이 다루는 글의 최소 단위. 단어보다 작은 조각일 때가 많음 (`interest` + `ing`) | Unit 1 |
| Subword 토큰화 (BPE) | 자주 나오는 글자 묶음을 토큰으로 삼고, 모르는 단어는 더 작은 조각(최악엔 바이트)으로 쪼개는 방식. 그래서 사전에 없는 단어도 항상 표현 가능 | Unit 1 |
| Transformer (인코더·디코더) | Attention 기반 신경망 구조. 인코더 = 글 → 의미 벡터(BERT), 디코더 = 토큰을 하나씩 생성(Llama, 대부분의 LLM) | Unit 1 |
| Embedding (임베딩) | 글을 의미가 담긴 숫자 벡터로 바꾼 것. 뜻이 비슷한 문장은 벡터 공간에서 가까이 위치 → 의미 검색에 씀 | Unit 1 |
| Autoregressive (자기회귀) | 방금 만든 출력을 다음 입력에 붙여 다시 예측하는 방식. EOS 토큰이 나올 때까지 반복 | Unit 1 |
| EOS token | End of Sequence. "생성 끝"을 뜻하는 특수 토큰. 모델마다 모양이 다름 | Unit 1 |
| Attention | 다음 토큰을 예측할 때 입력 중 중요한 토큰에 더 큰 가중치를 주는 방식 | Unit 1 |
| Context length | LLM이 한 번에 처리할 수 있는 최대 토큰 수 | Unit 1 |
| Greedy / Beam search | 다음 토큰 고르는 전략. greedy = 매번 점수 1등, beam search = 후보 문장 여러 개를 같이 키워 총점이 가장 높은 것 선택 | Unit 1 |
| Pre-training vs Fine-tuning | 사전학습 = 대량 텍스트로 다음 토큰 맞히며 언어 자체를 배움, 파인튜닝 = 그 뒤 대화·도구 사용 같은 특정 작업을 추가로 가르침 | Unit 1 |
| Chat template | 메시지 리스트(system/user/assistant)를 그 모델이 학습한 형식의 문자열 하나로 바꾸는 규칙. `transformers`에선 Jinja2 코드로 토크나이저 안에 있고 `apply_chat_template()`로 적용 | Unit 1 |
| Special token | 글자가 아니라 "구분 신호"로 쓰는 토큰. 차례 시작·끝(`<|im_start|>`, `<|im_end|>`), 생성 끝(EOS) 등. 통째로 토큰 1개이고 모델마다 모양이 다름 | Unit 1 |
| System / User / Assistant message | 채팅 메시지의 역할. system = 모델의 행동 규칙(에이전트에선 도구 목록·형식도), user = 사람, assistant = 모델의 답 | Unit 1 |
| Base vs Instruct model | Base = 다음 토큰 예측만 배운 모델, Instruct = 그 위에 지시 따르기·대화를 파인튜닝한 모델(이름 끝 `-Instruct`). 채팅엔 보통 Instruct | Unit 1 |
| ChatML | `<|im_start|>역할 ... <|im_end|>` 모양의 대표적인 채팅 템플릿 형식. SmolLM2·Qwen 등이 씀 | Unit 1 |
| Jinja2 | 빈칸·반복문이 있는 "문서 틀"을 채워 글을 만드는 파이썬 템플릿 언어. 채팅 템플릿이 이걸로 쓰여 있음 | Unit 1 |
| Hallucination (환각) | LLM이 모르는 걸 그럴듯하게 지어내는 것. 예: 검색 도구 없이 오늘 날씨를 물으면 아무 날씨나 말함 | Unit 1 |
| Callable | 괄호 `()`를 붙여 부를 수 있는 것(함수 등). 도구에서 "실제로 일하는 부분" | Unit 1 |
| Type hint (타입 힌트) | `a: int`, `-> int`처럼 변수·반환값의 종류를 적어 두는 표시. 도구 설명에서 "어떤 입력을 넣어야 하나"를 알려 줌 | Unit 1 |
| Docstring | 함수 맨 위 `"""..."""` 설명 글. 도구 설명(Description)으로 그대로 쓰임 | Unit 1 |
| Decorator (데코레이터) | 함수 위에 `@이름`을 붙여, 그 함수를 다른 걸로 감싸거나 바꿔 주는 파이썬 문법. `@tool`은 함수를 `Tool` 객체로 바꿈 | Unit 1 |
| MCP (Model Context Protocol) | 도구를 LLM 앱에 연결하는 공통 규격(오픈 프로토콜). 한 번 만든 도구를 여러 프레임워크·모델에서 재사용. USB-C 같은 것 | Unit 1 |
| Chain-of-Thought (CoT) | "Let's think step by step"처럼 답 전에 단계별로 생각을 쓰게 하는 프롬프팅 기법. 도구 없이 머릿속으로만 → 논리·수학에 강함 | Unit 1 |
| ReAct | Reasoning + Acting. 생각(Thought) 사이사이에 도구 사용(Action)과 결과 보기(Observation)를 끼워 넣는 프롬프팅 기법. TAO 사이클의 정식 이름 | Unit 1 |
| Reasoning model (추론 모델) | `<think>…</think>` 안에서 먼저 생각하고 답하도록 **학습 단계에서** 훈련된 모델(DeepSeek R1, OpenAI o1). CoT·ReAct는 프롬프트로 시키는 것이라는 점이 다름 | Unit 1 |
| JSON agent | Action(도구 이름 + 인자)을 JSON 글로 쓰는 에이전트. 파서가 JSON을 읽어 도구를 실행 | Unit 1 |
| Function-calling agent | JSON agent의 하위 종류. 도구 호출마다 **별도 메시지**를 만들도록 파인튜닝된 모델을 씀. 요즘 GPT·Claude·Qwen의 tool calling | Unit 1 |
| Code agent | Action을 JSON 대신 **파이썬 코드 블록**으로 쓰는 에이전트. 반복문·조건문으로 여러 도구 호출을 한 번에. 실행은 바깥 실행기가 함(보안 주의). smolagents의 `CodeAgent` | Unit 1 |
| Stop and parse | LLM이 Action을 다 쓰면 **생성을 멈추고**(stop), 바깥 **파서**가 그 글을 읽어 도구 이름·인자를 꺼내는(parse) 방식 | Unit 1 |
| Stop sequence | "이 글자가 나오면 생성을 멈춰라"라고 API에 정해 주는 문자열. 예: `Observation:` → LLM이 관찰을 지어내지 못하게 함 | Unit 1 |
| Parser (파서) | 정해진 형식의 글(JSON·코드)을 읽어 프로그램이 쓸 수 있는 값으로 바꾸는 코드. 예: `json.loads()` | Unit 1 |
| Prompt injection | 웹페이지·문서 등 입력 속에 숨겨진 지시문이 LLM을 속여 원래 목적과 다른 행동(예: 해로운 코드 실행)을 하게 만드는 공격 | Unit 1 |
| smolagents | | Unit 1 |
| HF Space | | Unit 1 |
| Ollama | 내 PC에서 LLM을 받아(`pull`) 로컬 서버(`localhost:11434`)로 돌려 주는 프로그램 | Unit 0 |
| LiteLLM | 여러 회사·로컬 모델의 API를 하나의 호출 형식으로 맞춰 주는 라이브러리. smolagents의 `LiteLLMModel`이 이걸 씀 | Unit 0 |
| VRAM (전용 GPU 메모리) | GPU에 붙은 전용 메모리. 모델이 여기 다 들어가면 빠름. "공유 GPU 메모리"는 일반 RAM을 빌려 쓰는 것이라 느려서 사양 판단에서 뺌 | Unit 0 |
| PowerShell vs cmd | 둘 다 Windows 터미널. cmd는 옛날 것, PowerShell은 새것이고 `irm`·`iex` 같은 명령은 PowerShell에서만 됨 | Unit 0 |
| 모델 vs 에이전트 프로그램(하네스) | 모델 = 글을 생성하는 두뇌(파일 하나), 하네스 = 그 두뇌를 불러 도구를 쓰고 반복시키는 프로그램(Claude Code, smolagents). 서로 바꿔 끼울 수 있음 | Unit 0 |
| HF Access Token | 내 코드가 HF에 "나"로 로그인하는 비밀 키. Read 권한이면 충분, `.env`/환경 비밀에만 저장 | Unit 0 |
