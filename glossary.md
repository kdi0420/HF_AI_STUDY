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
