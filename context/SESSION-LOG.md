# 세션 로그

세션마다 한 항목. **최신이 위.** `/wrap-up`이 추가한다. 이 파일은 자동 로드되지 않는다 (필요할 때만 읽는다).

<!--
## YYYY-MM-DD — 한 줄 제목
- 브랜치:
- 한 일:
- 남은 일 / 메모:
-->

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
