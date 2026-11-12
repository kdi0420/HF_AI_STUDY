# 세션 로그

세션마다 한 항목. **최신이 위.** `/wrap-up`이 추가한다. 이 파일은 자동 로드되지 않는다 (필요할 때만 읽는다).

<!--
## YYYY-MM-DD — 한 줄 제목
- 브랜치:
- 한 일:
- 남은 일 / 메모:
-->

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
