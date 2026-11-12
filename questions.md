# 질문 · 막힌 점

공부하다 생긴 질문을 바로 적는다. 해결되면 답과 출처(코스 섹션, AI, 친구, Discord)를 남긴다.
친구와 만날 때 "미해결"만 훑으면 된다.

## 미해결

<!-- - [Unit 1 §4] 질문 내용 (YYYY-MM-DD) -->

## 해결됨

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
