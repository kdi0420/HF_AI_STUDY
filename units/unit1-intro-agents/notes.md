# Unit 1 — Introduction to Agents

- 링크: [Unit 1 소개](https://huggingface.co/learn/agents-course/unit1/introduction)
- 목표일: 11/15 · 끝나면 **기초 인증서**
- 이 유닛의 결과물: smolagents로 만든 에이전트 **Alfred**를 HF Space에 올리기 + 최종 퀴즈 통과
- 실습 전 준비: **HF Access Token 발급**(Settings → Access Tokens → Read). 클라우드 세션에선 `request_credential`로 환경 비밀에 저장, 데스크탑에선 `.env`. HF 크레딧이 떨어지면 데스크탑 Ollama(`qwen3.5:9b`)로 교체 — Unit 0 노트 Step 5

## 진도

목차는 코스 원문과 대조함 (2026-11-12). 한국어판: https://huggingface.co/learn/agents-course/ko/unit1/introduction

| # | 섹션 | 끝나면 설명할 수 있어야 하는 것 | 완료 |
|---|---|---|---|
| 1 | [What is an Agent?](https://huggingface.co/learn/agents-course/unit1/what-are-agents) | 에이전트 = 무엇이 무엇을 하는 시스템인가? 챗봇과 뭐가 다른가? | [ ] |
| 2 | [Quick Quiz 1](https://huggingface.co/learn/agents-course/unit1/quiz1) | 틀린 문제 → `quiz.md` | [ ] |
| 3 | [What are LLMs?](https://huggingface.co/learn/agents-course/unit1/what-are-llms) | LLM이 "다음 토큰 예측기"라는 게 에이전트에 어떤 의미인가? | [ ] |
| 4 | [Messages and Special Tokens](https://huggingface.co/learn/agents-course/unit1/messages-and-special-tokens) | 채팅 메시지(system/user/assistant)가 실제로 모델에 어떻게 들어가나? 채팅 템플릿은 왜 필요한가? | [ ] |
| 5 | [What are Tools?](https://huggingface.co/learn/agents-course/unit1/tools) | 도구는 어떻게 정의하고, LLM은 도구를 어떻게 "아는가"? (system prompt에 도구 설명) | [ ] |
| 6 | [Quick Quiz 2](https://huggingface.co/learn/agents-course/unit1/quiz2) | 틀린 문제 → `quiz.md` | [ ] |
| 7 | [Thought–Action–Observation 사이클](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure) | 루프가 한 바퀴 도는 과정을 예시로 말할 수 있나? | [ ] |
| 8 | [Thought (ReAct)](https://huggingface.co/learn/agents-course/unit1/thoughts) | ReAct가 뭐고, 왜 "생각하고 행동하기"가 성능을 올리나? | [ ] |
| 9 | [Actions](https://huggingface.co/learn/agents-course/unit1/actions) | JSON 액션 vs 코드 액션(code agent)의 차이와 장단점은? 멈추고 파싱하는 방식은? | [ ] |
| 10 | [Observe](https://huggingface.co/learn/agents-course/unit1/observations) | 도구 실행 결과가 어떻게 다시 모델 입력으로 들어가나? | [ ] |
| 11 | [Dummy Agent Library](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library) | 프레임워크 없이 에이전트 루프를 손으로 짜면 어떤 모양인가? | [ ] |
| 12 | [First Agent with smolagents](https://huggingface.co/learn/agents-course/unit1/tutorial) | `CodeAgent` + 도구 + 모델로 Alfred 만들고 Space에 올리기 | [ ] |
| 13 | [Final Quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz) | 통과 → 기초 인증서 | [ ] |
| 14 | [Conclusion](https://huggingface.co/learn/agents-course/unit1/conclusion) | 유닛 1 한 페이지 요약 쓰기 | [ ] |

## 섹션별 노트

<!-- 각 섹션: "내 말로 정리" 3~5줄 + 예시. 모르는 건 ../../questions.md, 용어는 ../../glossary.md -->

### 1. What is an Agent?

-

### 2. What are LLMs?

-

### 3. Messages and Special Tokens

-

### 4. What are Tools?

-

### 5. Thought–Action–Observation 사이클

-

### 6. Thought (ReAct)

-

### 7. Actions

-

### 8. Observe

-

### 9. Dummy Agent Library

- 코드: `code/` 에 따라 친 것 저장

### 10. First Agent with smolagents

- 만든 Space 링크:
- 추가한 도구:
- 막혔던 점:

## 유닛 1 한 페이지 요약

<!-- 유닛 끝나고 "에이전트란?"을 친구에게 3분 안에 설명한다고 생각하고 쓴다 -->

-
