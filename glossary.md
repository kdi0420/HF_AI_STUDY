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
| Observation (관찰) | Action 결과를 환경이 돌려준 신호(API 응답·에러·로그 등). 에이전트가 대본(프롬프트) 끝에 덧붙여 다음 Thought의 재료로 씀 | Unit 1 |
| Context (컨텍스트) | 지금 LLM에게 보내는 입력 전체(system prompt + 대화 + 지난 Action·Observation). 에이전트의 "기억"은 결국 이것 | Unit 1 |
| Log (로그) | 프로그램이 실행하면서 남기는 기록 글. 도구의 Observation은 "Action이 어떻게 실행됐나"를 알려 주는 로그 같은 것 | Unit 1 |
| Status code (상태 코드) | 웹 요청 결과를 숫자로 알려 주는 신호. 200 = 성공, 404 = 없음, 401·403 = 권한 없음, 500 = 서버 오류 | Unit 1 |
| smolagents | HF가 만든 가벼운 에이전트 라이브러리. Dummy Agent에서 손으로 한 일(system prompt·멈추기·파싱·도구 실행·관찰 붙이기·루프)을 대신 해 줌. 우리는 모델·도구·`CodeAgent`만 고르면 됨 | Unit 1 |
| HF Space | HF가 공짜로 빌려주는 작은 웹 서버. `app.py`를 올리면 웹페이지(예: Gradio 채팅 화면)로 실행돼 링크로 공유할 수 있음. "Duplicate" = 남의 Space를 내 계정에 복사 | Unit 1 |
| Ollama | 내 PC에서 LLM을 받아(`pull`) 로컬 서버(`localhost:11434`)로 돌려 주는 프로그램 | Unit 0 |
| LiteLLM | 여러 회사·로컬 모델의 API를 하나의 호출 형식으로 맞춰 주는 라이브러리. smolagents의 `LiteLLMModel`이 이걸 씀 | Unit 0 |
| VRAM (전용 GPU 메모리) | GPU에 붙은 전용 메모리. 모델이 여기 다 들어가면 빠름. "공유 GPU 메모리"는 일반 RAM을 빌려 쓰는 것이라 느려서 사양 판단에서 뺌 | Unit 0 |
| PowerShell vs cmd | 둘 다 Windows 터미널. cmd는 옛날 것, PowerShell은 새것이고 `irm`·`iex` 같은 명령은 PowerShell에서만 됨 | Unit 0 |
| 모델 vs 에이전트 프로그램(하네스) | 모델 = 글을 생성하는 두뇌(파일 하나), 하네스 = 그 두뇌를 불러 도구를 쓰고 반복시키는 프로그램(Claude Code, smolagents). 서로 바꿔 끼울 수 있음 | Unit 0 |
| HF Access Token | 내 코드가 HF에 "나"로 로그인하는 비밀 키. Read 권한이면 충분, `.env`/환경 비밀에만 저장 | Unit 0 |
| Serverless API (HF Inference) | 모델을 내 PC에 설치·배포하지 않고 HF 서버에 메시지를 보내 답만 받는 방식. `huggingface_hub`의 `InferenceClient`로 부름. 무료 계정은 크레딧이 필요 | Unit 1 |
| max_tokens | "최대 이만큼의 토큰까지만 써라"라는 생성 길이 제한. 넘으면 문장 중간이라도 끊김 (Ollama에선 `num_predict`) | Unit 1 |
| 이어 쓰기 (assistant prefill) | messages 마지막에 assistant 메시지를 미리 넣어 두면 모델이 그 뒤를 이어 쓰게 하는 방법. Dummy Agent에서 "모델이 쓴 Action + 진짜 Observation"을 넣고 Final Answer를 받아 냄. 모델·서버 템플릿마다 지원 여부가 다름 | Unit 1 |
| `@tool` (데코레이터) | 함수 위에 붙이는 한 줄. 함수 이름·타입 힌트·docstring을 읽어 "도구 설명서"를 만들어 system prompt에 넣어 줌. 데코레이터 = 함수에 기능을 덧씌우는 파이썬 문법 | Unit 1 |
| docstring | 함수 바로 밑의 `"""설명"""` 글. smolagents는 첫 줄을 도구 설명, `Args:` 아래를 인자 설명으로 읽음 | Unit 1 |
| Gradio | 파이썬 몇 줄로 웹 화면(채팅창 등)을 만들어 주는 라이브러리. `launch(share=True)`는 인터넷 공개 링크를 만드니 내 PC 실습에선 `share=False` | Unit 1 |
| num_ctx (컨텍스트 창) | Ollama 모델이 한 번에 읽을 수 있는 입력 길이(토큰). system prompt가 길면 늘려야 앞부분이 잘리지 않음 | Unit 1 |
| Jupyter 노트북 (`.ipynb`) | 코드를 칸(셀)으로 나눠 한 칸씩 실행하고, 결과가 칸 바로 아래 남는 파일. `.py`는 위에서 아래까지 한 번에 실행. 브라우저에서 `jupyter notebook 파일이름`으로 열고 `Shift+Enter`로 실행 | Unit 1 |
| Agentic Framework (에이전트 프레임워크) | 에이전트를 만들 때 매번 손으로 짜야 하는 부품(LLM 호출·도구 목록·파서·system prompt·기억·에러 재시도)을 미리 만들어 둔 조립 세트. 예: smolagents, LlamaIndex, LangGraph | Unit 2 |
| Abstraction (추상화) | 복잡한 속을 감추고 간단한 사용법만 보여 주는 포장. 편하지만 속에서 무슨 일이 일어나는지는 덜 보임 (예: `CodeAgent.run()` 한 줄 안에 TAO 루프 전체) | Unit 2 |
| Predefined workflow (정해진 워크플로) | 단계 순서를 개발자가 미리 정해 둔 흐름. LLM은 각 단계를 수행만 하고 순서는 안 정함 (예: 요약 → 번역). 이 정도면 프레임워크 없이 평범한 코드로 충분 | Unit 2 |
| Parser (파서) | LLM이 쓴 글에서 필요한 부분(도구 이름·인자, 코드 블록)을 꺼내 프로그램이 쓸 수 있는 꼴로 바꾸는 것. system prompt가 요구한 형식과 맞아야 동작 | Unit 2 |
| RAG (검색 증강 생성) | Retrieval-Augmented Generation. 질문과 관련된 자료를 먼저 찾아서 프롬프트에 붙이고, 그걸 보고 답하게 하는 방식. "오픈북 시험". 모델이 모르는 내 문서·최신 정보로도 답할 수 있음 | Unit 2 |
| Vector store (벡터 저장소) | 문서 조각을 임베딩(의미 벡터)으로 바꿔 저장해 둔 창고. 질문도 벡터로 바꿔 뜻이 가까운 조각을 찾아 줌 → RAG의 "검색" 담당 | Unit 2 |
| Knowledge base (지식 창고) | 에이전트가 검색해 쓸 수 있도록 모아 둔 자료 묶음 (문서, FAQ, 데이터 등) | Unit 2 |
| Orchestration (오케스트레이션) | 여러 에이전트·단계를 지휘자처럼 조율하는 것. 누가 언제 무엇을 할지 정하고 결과를 모음 | Unit 2 |
| Multi-agent system (멀티 에이전트) | 역할이 다른 에이전트 여러 개가 함께 일하는 구조. 보통 매니저 에이전트가 하위 에이전트(웹 검색 담당, 코드 담당 등)에게 일을 나눠 줌 | Unit 2 |
| Fallback (대비책) | 첫 방법이 실패했을 때 쓰는 플랜 B. 예: 지식 창고에 답이 없으면 웹 검색 | Unit 2 |
| ToolCallingAgent | smolagents의 두 번째 에이전트 종류. 행동을 JSON(도구 이름 + 인자)으로 냄. 모델 API의 **tool calling 기능**을 써서, 도구 호출이 글 속이 아니라 `tool_calls`라는 별도 칸으로 옴 → 글을 오려 낼 필요가 적음. 변수·계산은 못 함. 기본 종류인 CodeAgent는 행동을 파이썬 코드로 씀 | Unit 2 |
| MultiStepAgent | smolagents 에이전트의 부모 설계도(클래스). 한 단계 = 생각 1번 + 행동 1번, 이걸 끝날 때까지 반복(TAO 루프). CodeAgent·ToolCallingAgent가 이걸 물려받음 | Unit 2 |
| Class / 상속 | Class = 객체를 만드는 설계도. 상속 = 부모 설계도의 기능을 물려받고 일부만 바꾼 자식 설계도 (MultiStepAgent → CodeAgent) | Unit 2 |
| LiteLLM | 여러 회사(OpenAI, Anthropic, Ollama …)의 서로 다른 API를 같은 모양으로 맞춰 주는 통역 라이브러리. smolagents의 `LiteLLMModel`이 이걸 씀 (`ollama_chat/qwen3.5:9b`) | Unit 2 |
| OpenAI 호환 API | OpenAI가 정한 요청·응답 모양을 다른 서버도 똑같이 따르는 것. 덕분에 한 코드로 여러 서버에 붙음 (Ollama도 `/v1` 주소로 제공) | Unit 2 |
| Sandbox (샌드박스) | 코드를 바깥(내 파일·인터넷 등)에 함부로 손대지 못하게 가둬서 돌리는 실행 공간. smolagents 기본 실행기는 허용된 `import`만 받는 정도의 안전장치이고, 진짜 격리는 Docker·E2B 같은 원격 샌드박스 | Unit 2 |
| `additional_authorized_imports` | CodeAgent가 쓰는 코드에 기본 허용 목록 밖의 모듈 `import`를 추가로 허락하는 옵션. 예: `['pandas']` | Unit 2 |
| Tracing / OpenTelemetry | Tracing = 에이전트가 단계마다 무엇을 했는지 기록을 남기는 것(블랙박스). OpenTelemetry = 그 기록 형식의 공통 표준. Langfuse 같은 서비스가 받아서 화면으로 보여 줌 | Unit 2 |
| `step_callbacks` (콜백) | 콜백 = "일이 끝나면 불러 줘" 하고 맡겨 두는 내 함수. smolagents는 한 바퀴(ActionStep)가 끝날 때마다 이 목록의 함수에 그 바퀴 기록(`step`)을 넘겨 불러 줌. 예: 바퀴마다 시간·토큰 출력 | Unit 2 |
| 모듈 / `import` | 모듈 = 남이 미리 만들어 둔 기능 묶음(도구 상자), `import` = 그 상자를 꺼내 오기. 예: `datetime`(날짜·시간), `os`(내 컴퓨터 파일·폴더), `json`(데이터 ↔ 글자) | Unit 2 |
| Tool making (도구 만들기) | 에이전트가 필요한 도구를 스스로 코드로 작성·등록해 다음에 다시 쓰는 것. 보통 `create_tool` 같은 메타 도구(도구를 만드는 도구)를 주어 구현. 예: LATM, Voyager의 스킬 창고 | Unit 2 |
| Tool calling (도구 호출 기능) | OpenAI·Anthropic·Ollama 같은 모델 API가 제공하는 기능. 요청에 도구 목록(`tools`)을 따로 넣으면, 모델이 답을 글 대신 "도구 이름 + 인자" JSON으로 정해진 칸(`tool_calls`)에 돌려줌. function calling이라고도 함 | Unit 2 |
| 클래스 (class) / 인스턴스 | 클래스 = 설계도, 인스턴스 = 그 설계도로 찍어 낸 실물. `SuperheroPartyThemeTool`은 클래스, `party_theme_tool = SuperheroPartyThemeTool()`이 인스턴스(실제 도구). "상속(subclass)" = 남의 설계도(`Tool`)를 물려받아 내 것만 채워 넣기 | Unit 2 |
| `Tool` 클래스 / `forward` | smolagents 도구의 부모 설계도. 상속해서 `name` · `description` · `inputs` · `output_type`을 적고, 실제 일은 `forward()`에 씀. `forward`의 인자 이름 = `inputs`의 키. `@tool`도 속으로는 이걸 자동으로 만듦 | Unit 2 |
| `add_base_tools` | 에이전트에 기본 도구(웹 검색·웹페이지 읽기, ToolCallingAgent는 파이썬 실행까지)를 자동으로 넣는 옵션. `final_answer`는 옵션과 무관하게 항상 들어감 | Unit 2 |
| `UserInputTool` | 에이전트가 사람에게 질문하고(`input()`), 사람이 친 답을 관찰로 받는 기본 도구. 이름은 `user_input` | Unit 2 |
