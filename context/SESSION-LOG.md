# 세션 로그

세션마다 한 항목. **최신이 위.** `/wrap-up`이 추가한다. 이 파일은 자동 로드되지 않는다 (필요할 때만 읽는다).

<!--
## YYYY-MM-DD — 한 줄 제목
- 브랜치:
- 한 일:
- 남은 일 / 메모:
-->

## 2026-11-22 — Unit 2: CodeAgents 복습 + 데스크탑 실습 완료
- 브랜치: `claude/brave-planck-yfy5cu` → main 반영 (곁가지 질문 세션 `claude/admiring-cori-e44nys`의 questions·glossary·USER 변경도 함께 합침)
- 한 일: 사용자가 원문을 다시 붙여 줌 → CodeAgents 전체를 장별 입문자 설명(Code vs JSON 장점 4, `run()` 루프와 Dummy Agent 대응, 예제 ①②③, Hub 공유·`trust_remote_code`, 완성판 Alfred 도구 3종, Langfuse). 데스크탑 실행 안내를 PowerShell 열기부터 한 줄씩 → 새 venv 만들고 노트북 2단계 실행. 결과 "1~5바퀴 검색만, 6바퀴에 답" 분석: smolagents 1.26 소스로 확인 — 강제 종료 아님(모델은 남은 바퀴 수를 모름, planning 때만 알려 줌), Input tokens는 누적값(바퀴별 2,204→7,732, `num_ctx=8192`에 근접), 생각(Thought)은 DEBUG 로그라 숨겨짐(`model_output`으로 확인). 가상 장소 + 곡 목록 없는 검색 요약 + `visit_webpage` 없음 → 같은 검색을 맴돎, 답은 쌓인 결과 요약 + 모델 상식. 5단계(실행기·허용 import·`step_callbacks`)와 Langfuse(선택 사항, 키 2개, 데이터 외부 전송, 로컬 대안 Phoenix) 추가 설명. 사용자 "내 말로" 정리를 노트 3번에 기록. glossary에 콜백·모듈/import
- 남은 일 / 메모: 사용자가 이후 노트북 3~6단계도 끝까지 실행했다고 알려 줌(결과는 안 붙임 → 노트에 기록 없음). 다음은 ToolCallingAgents. 사용자가 "유난히 어려웠다"고 함 → 다음 섹션도 입문자용 상세 유지

## 2026-11-19 — Unit 2 시작: 프레임워크 소개 · Introduction to smolagents · Why Use smolagents
- 브랜치: `claude/nice-archimedes-2u2tyf` → main 반영
- 한 일: `/new-unit 2 frameworks`로 `units/unit2-frameworks/`(notes·quiz·`code/requirements.txt` = smolagents 1.26 + litellm부터) 생성, README 진도표 "진행중". 2.1 목차는 원문 Contents와 대조, 2.2·2.3 세부는 기억 기반(원문 대조 필요). 원문 붙여 주기 → 입문자용 설명: ① 소개 — 프레임워크 = 조립 키트, predefined workflow면 불필요, 6가지(엔진·도구·파서·프롬프트·메모리·에러 재시도)를 Unit 1 Dummy Agent 경험과 표로 연결. 사용자가 이해를 말로 정리 → 에이전트 ≠ 프레임워크, 파서는 꺼내기만, 프롬프트–파서 한 쌍 등 보충, 정의(원문에 한 문장 정의 없음 → 일반적 뜻)와 라이브러리 vs 프레임워크 ② Introduction to smolagents — 목차 7개, RAG·벡터 저장소·fallback, Anthropic "Building Effective Agents"(workflow vs agent) ③ Why Use — 장점 4(Code-first의 "파싱 불필요"는 JSON→호출 번역이 없어진다는 뜻), Code vs JSON 예시, MultiStepAgent 상속, 모델 클래스 5개(우리는 `LiteLLMModel`). glossary에 15개 추가
- 남은 일 / 메모: 다음은 CodeAgents(실습 나올 가능성 높음 → 데스크탑용 **새** 노트북, 새 venv `units\unit2-frameworks\code\.venv`, 만들자마자 main 반영, PowerShell부터 한 줄씩). 노트 0~2번 "내 말로" 중 0번만 채움. 세션 시작 훅이 알리는 `claude/awesome-meitner-oda4pe`는 레포 독립 전 옛 브랜치(이력 연결 없음, 내용 main에 있음) → 무시해도 됨

## 2026-11-16 (2) — Unit 1: First Agent with smolagents · Final Quiz → 기초 인증서
- 브랜치: `claude/focused-hamilton-uke261` → main 반영 (노트북은 만들자마자 main 반영)
- 한 일: 원문 붙여 주기 → 입문자 설명(smolagents·CodeAgent, Space 복제, `app.py` = 도구+모델+에이전트+화면, `@tool` 타입 힌트·docstring). 템플릿 Space 파일을 받아 보니 smolagents 1.13·옛 `prompts.yaml`(`<end_code>`) → 1.26 기본 프롬프트로. HF 크레딧 0이라 데스크탑 Ollama판 노트북 `units/unit1-intro-agents/code/smolagents_first_agent.ipynb`(0~8단계, `LiteLLMModel("ollama_chat/qwen3.5:9b", num_ctx=8192, reasoning_effort="none")`) 작성, 클라우드 가짜 Ollama 서버로 전 칸 검증(smolagents도 `stop=["Observation:", …]`·관찰을 user 메시지로 보냄 = Dummy 6-B와 같음). `GradioUI.launch()` 기본 `share=True`(공개 링크) 발견 → `share=False`. `requirements.txt`를 `smolagents[litellm,gradio]==1.26.0`·ddgs·pytz로. `reasoning_effort`는 Ollama에서 켜기/끄기뿐(low·medium·high 동일) 확인. 데스크탑 실행: 6단계 한 코드로 `get_weather` 2번 + `if` 비교 3바퀴, 7단계 웹 검색 `No results found` 2번 → 검색어 줄여 4바퀴 성공. 질문: JSON vs Code 에이전트, parsed code는 누가 쓰나 → 노트 10번. Final Quiz 통과 → Unit 1 기초 인증서(이미지는 실명이 있어 레포에 안 올림). 한 페이지 요약 초안
- 남은 일 / 메모: Conclusion 원문 + 요약 다듬기 → Unit 2 시작. 데스크탑에서 실행한 노트북은 클라우드에서 고치지 말 것

## 2026-11-16 — Unit 1: Dummy Agent Library (데스크탑 노트북 실습)
- 브랜치: `claude/jolly-bohr-emcu5y` (이전 세션 `claude/magical-lamport-v3gnee`의 "Ollama로 실습" 결정 포함) → main 반영
- 한 일: (이전 세션) 무료 크레딧 0 → Unit 1 실습은 데스크탑 Ollama로 결정. 원문 붙여 주기 → 장별 입문자 설명(Serverless API, system prompt 3요소, 환각, stop, 가짜 도구, 이어 쓰기, "손으로 하면 번거롭다" 표). 사용자가 한 칸씩 실행하길 원해서 Jupyter 노트북 `units/unit1-intro-agents/code/dummy_agent_ollama.ipynb` + 환경 안내 `practice-guide.md`(Colab은 데스크탑 Ollama에 못 붙어 제외) 작성. 데스크탑에서 venv + `pip install notebook` → 0~6단계 성공: 3단계 환각 확인, 6-A(assistant 이어 쓰기) 막힘 → 6-B(관찰을 user 메시지로) 성공. 7단계 루프(6-A 방식)는 빈 출력 → `substring not found` 반복 → 10바퀴에 상식으로 답함, 원인 분석 기록. 사용자 요청으로 7단계를 6-B + 고치는 법을 알려 주는 에러 관찰(`FORMAT_HINT`)로 고쳐 레포 노트북에 반영하고 채팅으로도 전달→ 데스크탑에서 3바퀴 만에 성공(London 8°C → Paris 14°C → Paris가 더 따뜻). 독립판 `dummy_agent_loop.ipynb`도 같은 코드. 사용자 복습을 노트에 사용자 말로 기록
- 남은 일 / 메모: First Agent with smolagents부터. 교훈: 데스크탑 실행 파일은 바로 main에 반영(브랜치에만 둬서 파일 없음 에러 났음, AGENTS.md). 사용자 선호: 데스크탑 안내는 PowerShell 열기부터 한 줄씩(USER.md). 다음 `git pull` 전에 데스크탑 `dummy_agent_ollama.ipynb` 로컬 변경 되돌리기(STATUS 데스크탑 메모)

## 2026-11-15 (3) — Unit 1: Thought (ReAct) · Actions · Observe
- 브랜치: `claude/nice-rubin-74ox66` → main 반영
- 한 일: 원문 붙여 주기 → 입문자용 상세 설명 방식 유지. Thought(생각 종류 표, CoT vs ReAct vs 추론 모델 `<think>`, ReAct 논문 그림 (d)는 붙여넣기에 빠져 미확인으로 설명). Actions(JSON / Code / Function-calling agent, stop and parse, Code agent 장점·보안 위험) — `units/unit1-intro-agents/code/stop_and_parse_demo.py`(멈추지 않으면 Observation을 지어냄 → stop sequence로 자르기 → 파싱·실행, 코드 액션 for 문). Observe(관찰 3단계, 대본 = 기억, 관찰 종류 표, Parse→Execute→Append) — `observe_adapt_demo.py`(에러 관찰 보고 "NYC" → "New York" 재시도). glossary에 용어 14개 추가(Code agent 빈칸 포함)
- 남은 일 / 메모: Dummy Agent Library부터 재개(14개 중 10개 완료, 사용자는 다음 날 코딩 실습 예정). HF 토큰(Read) 필요 → 클라우드 세션은 `request_credential`. ReAct·Actions·Observe 노트의 "내 말로:" 칸 비어 있음. Unit 1 목표일 새로 정하기 대기

## 2026-11-15 (2) — Unit 1: Messages · Tools · Quiz 2 · TAO 사이클
- 브랜치: `claude/inspiring-euler-aua9sk` → main 반영
- 한 일: 원문 붙여 주기 → AI가 **입문자용으로 처음부터 자세히** 설명하는 방식으로 진행(사용자 요청으로 기본값이 됨, USER.md 반영). Messages and Special Tokens(대본 비유, 특수 토큰, Base vs Instruct, 채팅 템플릿·Jinja2) — SmolLM2 토크나이저로 `apply_chat_template` 실행 확인(기본 system 자동 추가, `add_generation_prompt`, `<|im_end|>` = EOS). What are Tools?(LLM은 호출 글만 쓰고 에이전트가 실행, system prompt에 도구 설명, `@tool`·`Tool` 클래스, MCP) — 원문 코드 실행, 타입 힌트·docstring 없으면 설명이 `_empty`로 나오는 것 확인. Quick Quiz 2 5/5. Thought–Action–Observation 사이클(while 루프, Alfred 날씨 예시) — 가짜 LLM 루프 데모 `units/unit1-intro-agents/code/tao_loop_demo.py` 작성·실행. glossary에 용어 14개 추가
- 남은 일 / 메모: Thought (ReAct)부터 재개(14개 중 7개 완료). Messages·Tools·TAO·What is an Agent? 노트의 "내 말로:" 칸 비어 있음. Unit 1 목표일 새로 정하기 대기. 원문 붙여넣기엔 그림(시스템 프롬프트 예시 등)이 빠지므로, 그림 내용은 AI가 만든 예시라고 밝히고 설명함

## 2026-11-15 — Unit 1 시작: Agent 개념 · Quick Quiz 1 · LLM 기초
- 브랜치: `claude/trusting-cannon-d51xhg` → main 반영
- 한 일: 사용자가 원문을 붙여 주면 AI가 핵심 요약 → 질문 받기 방식으로 진행. 소개(로드맵), What is an Agent?(정의·뇌/몸·agency 스펙트럼·Action≠Tool), Quick Quiz 1 6/6(Q4는 영어 보기 때문에 헷갈림 → quiz.md), What are LLMs?(Transformer 3종·토큰·EOS·autoregressive·디코딩·attention·학습 2단계) 전체 복습. 질문 4개 해결(reasoning vs planning, 디코더 vs Seq2Seq, 다음 토큰 예측의 힘 + 미등록 단어 토큰화, HF Access Token vs LLM 토큰). SmolLM2 토크나이저로 직접 실험(한국어는 바이트 단위로 쪼개짐). 다음 섹션들의 토큰·모델 요구사항을 원문에서 확인(Read 토큰 하나, Llama는 당장 불필요). glossary에 용어 14개 추가
- 남은 일 / 메모: Messages and Special Tokens부터 재개. What is an Agent? "내 말로" 칸 비어 있음. Unit 1 목표일(11/15) 지나서 새 날짜 필요. 사용자는 "AI가 쉽게 풀어서 자세히" 설명받는 걸 좋아함(입문자 레벨 요청 반복)

## 2026-11-12 — Ollama 로컬 실행 성공, Unit 0 완료
- 브랜치: `claude/sleepy-johnson-2xk2ep` → main 반영
- 한 일: 집 데스크탑(Windows, RAM 64GB, VRAM 10GB)에 Ollama 설치를 단계별 안내(PowerShell vs cmd 설명). ollama.com "Local" 목록 PDF + 웹 검색으로 모델 비교 → `qwen3.5:9b` 선택(2순위 `gemma4:12b`). 확인 스크립트 `units/unit0-onboarding/code/ollama_check.py` 작성 → 사용자가 데스크탑에서 clone·venv·실행까지 성공(100% GPU). "Claude Code vs 로컬 모델" 질문 → 모델(두뇌) vs 에이전트 프로그램(몸)으로 설명, questions 해결됨. Git 기초 TIL. Unit 0 완료 처리(README·노트 요약)
- 남은 일 / 메모: HF 토큰은 Unit 1 실습 직전으로 미룸. 친구와 요일은 사용자가 알아서(추적 안 함). 사용자 선호 추가: 답변 끝에 확인 질문·퀴즈 던지지 않기(USER.md). ollama.com은 이 세션 네트워크에서 막혀 있어 모델 정보는 사용자 PDF + 웹 검색으로 확인

## 2026-11-12 — Unit 0 온보딩 진행, Ollama(Step 5) 정리
- 브랜치: `claude/awesome-meitner-oda4pe` → main 반영
- 한 일: 세션이 이 레포에서 제대로 열렸는지 확인. Unit 0 계정·Org 팔로우·Discord 완료 체크. HF 토큰 발급 방법 안내. Onboarding Step 5(Ollama 로컬 실행) 설명 → 노트·용어집(Ollama, LiteLLM, HF Access Token)·questions 해결됨에 기록
- 남은 일 / 메모: 토큰 발급·라이브 1·친구와 요일 정하기·코스 구조 메모. Ollama는 집 데스크탑에서 해 볼 예정. 확인 질문(왜 기본은 HF 서버 모델?)은 AI가 답해 해결됨으로 이동. Ollama는 Unit 0 완료 조건 아님(선택). 라이브 1은 앞 15~20분만 훑기로 함(YouTube는 세션에서 접속 불가라 챕터 미확인)

## 2026-11-12 — 저장소 시작: AI_playground에서 독립
- 브랜치: `main` (빈 저장소 첫 커밋)
- 한 일 (이 세션의 대화 흐름):
  1. 사용자: Todoist 읽고 HF Unit 0·1 공부용 폴더를 설계해 달라고 요청 → Todoist "🤗 개인 › AI 공부"에서 "Hugging Face 에이전트 코스 같이 공부하기 - 친구"(1주 1유닛, 주 3~4시간)과 하위 할 일 Unit 0·Unit 1(~11/15) 확인
  2. AI_playground에 `experiments/2026-11-12-hf-agents-course/` 생성: 진도표, Unit 0 체크리스트, Unit 1 섹션별 노트·퀴즈 오답 노트, 용어집, 질문 목록, 실습 requirements
  3. 사용자: "AI_playground 밑에 새 git을 만들어 거기서 할 수 없나?" → 안쪽 `.git`은 클라우드 세션에 복제되지 않아서 비추천, 별도 GitHub 저장소를 권함
  4. 사용자가 `kdi0420/hf_ai_study`를 만들고 "이 채팅과 내용 전부 옮겨 달라"고 요청 → 이 저장소로 이전. 구조를 HF 공부 전용으로 정리(`units/`), AI 규칙·훅·스킬(`/new-unit`, `/wrap-up`) 이식
- 남은 일 / 메모: 처음엔 huggingface.co 차단이었으나 환경 "기본값"에 허용 추가 → 목차를 원문과 대조해 Quiz 1·2, 섹션 링크, 한국어판 링크 반영. 다음 세션은 **이 저장소를 선택해서** 시작해야 이 규칙들이 로드된다
