# 입문자 필수 질문 리스트 (CS · AI 기초)

수학 기반이고 CS는 처음인 입장에서 "이건 꼭 스스로 답할 수 있어야 한다"는 질문 모음 (2026-11-12, AI가 뽑음).
답은 여기 쓰지 않는다. 하나씩 AI에게 물어보고, 답은 `questions.md` "해결됨"이나 `glossary.md`에 남긴다.

- ✅ = 이미 한 번 답을 들음(어디 적혔는지 표시) · 📘 = 코스(Unit 1~)에서 직접 다룸 · 표시 없음 = 따로 물어봐야 함
- 순서대로 보면 아래 단계가 위 단계를 딛고 선다.

## 1. 컴퓨터·터미널
1. 터미널(명령줄)이란 무엇이고, 왜 마우스 대신 글자로 명령하나?
2. PowerShell·cmd·bash는 뭐가 다른가? ✅ glossary "PowerShell vs cmd"
3. 경로(path)란? 절대 경로·상대 경로, "현재 폴더"(`cd`)는 무슨 뜻인가?
4. 환경 변수와 `PATH`란? 왜 설치 후 터미널을 새로 열어야 하나?
5. 패키지 매니저(winget · pip · npm)란? 왜 웹사이트에서 받지 않고 명령으로 설치하나?
6. `localhost`와 포트(`11434`)란? 서버·클라이언트란?
7. 프로세스와 "백그라운드에서 돈다"는 건 무슨 뜻인가?

## 2. Git · GitHub
8. Git은 무엇이고 GitHub와 뭐가 다른가? ✅ TIL git-basics
9. 레포·commit·push·pull·clone은 각각 무엇인가? ✅ TIL git-basics
10. branch·main·merge는 무엇이고 왜 갈래를 나누나? ✅ TIL git-basics
11. 충돌(conflict)은 왜 생기고 어떻게 푸나?
12. `.gitignore`는 왜 필요한가? (비밀 키·대용량 파일)
13. Pull Request(PR)란? fork와 clone은 뭐가 다른가?
14. 공개 레포에 한 번 올린 건 왜 지워도 남나? (커밋 기록)

## 3. Python 개발 환경
15. Python 인터프리터란? `python 파일.py`를 치면 무슨 일이 일어나나?
16. 패키지·라이브러리·`import`란?
17. 가상환경(venv)은 왜 프로젝트마다 따로 만드나? ✅ 이번 세션 설치 안내
18. `requirements.txt`는 무엇이고 버전 충돌은 왜 생기나?
19. Jupyter 노트북(`.ipynb`)과 `.py` 파일은 뭐가 다른가? (코스 실습이 노트북)

## 4. 인터넷 · API
20. API란? "API를 호출한다"는 건 정확히 무엇을 하는 건가?
21. HTTP 요청·응답과 JSON이란?
22. API 키·토큰은 무엇이고 왜 코드에 쓰면 안 되나? (`.env`)
23. 클라우드에서 돈다 / 로컬에서 돈다는 무슨 차이인가? ✅ questions "Claude Code vs 로컬"

## 5. AI · LLM 구조
24. "모델"은 실체가 무엇인가? (가중치 = 숫자 덩어리 파일)
25. 7B·9B 같은 파라미터 수는 무엇을 뜻하나?
26. 학습(training)과 추론(inference)은 뭐가 다른가? 내 PC에서 하는 건 어느 쪽인가?
27. 토큰이란? 컨텍스트 길이(`num_ctx`)란? 📘 Unit 1
28. LLM은 어떻게 다음 단어를 고르나? (다음 토큰 예측, 확률, temperature) 📘 Unit 1
29. 왜 AI에 GPU·VRAM이 필요한가? ✅ glossary "VRAM"
30. 양자화(Q4 등)란? 왜 9B 모델이 6.6GB로 줄어드나?
31. 오픈 웨이트 모델과 닫힌 모델(Claude, GPT)은 뭐가 다른가?
32. 프롬프트·시스템 프롬프트·채팅 템플릿이란? 📘 Unit 1
33. 파인튜닝이란? 프롬프트로 시키는 것과 뭐가 다른가? 📘 Bonus 1
34. 임베딩이란? (`embeddinggemma` 같은 모델은 뭘 하나)
35. thinking(추론) 모델, 멀티모달(vision·audio) 모델이란?
36. 환각(hallucination)은 왜 생기나?

## 6. 에이전트
37. 에이전트란 무엇이고 그냥 챗봇과 뭐가 다른가? 📘 Unit 1
38. 하네스(에이전트 프로그램)란? 모델과 어떻게 나뉘나? ✅ glossary "모델 vs 에이전트 프로그램"
39. 도구(tool)·function calling이란? 모델이 어떻게 "실행"을 하나? 📘 Unit 1
40. Thought → Action → Observation 루프, ReAct란? 📘 Unit 1
41. 코드 에이전트와 JSON 에이전트는 뭐가 다른가? 📘 Unit 1
42. 에이전트 프레임워크(smolagents·LlamaIndex·LangGraph)는 왜 쓰나? 📘 Unit 2
43. RAG란? 📘 Unit 3
44. MCP란? 
45. 에이전트 성능은 어떻게 평가하나? (SWE-bench, GAIA 같은 벤치마크) 📘 Unit 4

## 7. Hugging Face 생태계
46. HF Hub에는 무엇이 있나? (모델·데이터셋·Spaces)
47. Space란? 왜 결과물을 거기에 올리나? 📘 Unit 1
48. Inference Providers·크레딧이란? 왜 무료 한도가 있나?
49. `transformers` 라이브러리는 무엇을 해 주나?
