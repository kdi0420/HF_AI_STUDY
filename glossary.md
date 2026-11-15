# 용어집

공부하면서 나온 용어를 누적한다. **내 말로** 한 줄, 필요하면 예시. 처음 나온 유닛을 적어 둔다.

| 용어 | 한 줄 정의 (내 말로) | 처음 나온 곳 |
|---|---|---|
| Agent | | Unit 1 |
| Tool | | Unit 1 |
| Agency (행위 주체성) | 스스로 판단해 행동하는 능력. 에이전트가 환경에 작용할 수 있는 정도. LLM 출력이 프로그램 흐름을 얼마나 결정하느냐로 단계를 나눔 (☆☆☆ 단순 처리기 ~ ★★★ 멀티스텝·멀티 에이전트) | Unit 1 |
| Reasoning vs Planning | Reasoning(추론) = 주어진 정보로 "무엇이 필요하고 지금 상황이 어떤가"를 따져 결론을 끌어내기. Planning(계획) = 그 결론을 바탕으로 단계 순서 짜기. 추론이 먼저, 계획은 추론의 결과물 | Unit 1 |
| Action vs Tool | Action = 목표를 위해 하는 행동, Tool = 그때 쓰는 개별 기능(함수). 행동 하나에 도구 여러 개가 들어갈 수 있음 | Unit 1 |
| VLM | Vision Language Model. 텍스트에 더해 이미지도 입력으로 받는 LLM | Unit 1 |
| Thought / Action / Observation | | Unit 1 |
| ReAct | | Unit 1 |
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
| Chat template | | Unit 1 |
| Special token | | Unit 1 |
| Code agent | | Unit 1 |
| smolagents | | Unit 1 |
| HF Space | | Unit 1 |
| Ollama | 내 PC에서 LLM을 받아(`pull`) 로컬 서버(`localhost:11434`)로 돌려 주는 프로그램 | Unit 0 |
| LiteLLM | 여러 회사·로컬 모델의 API를 하나의 호출 형식으로 맞춰 주는 라이브러리. smolagents의 `LiteLLMModel`이 이걸 씀 | Unit 0 |
| VRAM (전용 GPU 메모리) | GPU에 붙은 전용 메모리. 모델이 여기 다 들어가면 빠름. "공유 GPU 메모리"는 일반 RAM을 빌려 쓰는 것이라 느려서 사양 판단에서 뺌 | Unit 0 |
| PowerShell vs cmd | 둘 다 Windows 터미널. cmd는 옛날 것, PowerShell은 새것이고 `irm`·`iex` 같은 명령은 PowerShell에서만 됨 | Unit 0 |
| 모델 vs 에이전트 프로그램(하네스) | 모델 = 글을 생성하는 두뇌(파일 하나), 하네스 = 그 두뇌를 불러 도구를 쓰고 반복시키는 프로그램(Claude Code, smolagents). 서로 바꿔 끼울 수 있음 | Unit 0 |
| HF Access Token | 내 코드가 HF에 "나"로 로그인하는 비밀 키. Read 권한이면 충분, `.env`/환경 비밀에만 저장 | Unit 0 |
