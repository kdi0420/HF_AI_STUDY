# Unit 0 — 온보딩

- 링크: [Unit 0 소개](https://huggingface.co/learn/agents-course/unit0/introduction) · [Onboarding](https://huggingface.co/learn/agents-course/unit0/onboarding) · [Discord 101](https://huggingface.co/learn/agents-course/unit0/discord101)
- 라이브: [Live 1: How the Course Works and First Q&A](https://huggingface.co/learn/agents-course/communication/live1) ([YouTube](https://www.youtube.com/watch?v=iLVyYDbdSmM))
- 목표일: 11/15

## 체크리스트

- [x] Hugging Face 계정 만들기 (https://hf.co/join)
- [x] Hub에서 [Agents Course Organization](https://huggingface.co/agents-course) 팔로우 (Onboarding Step 3)
- [ ] HF Access Token 발급 (Settings → Access Tokens) → 레포 루트 `.env`의 `HF_TOKEN=`에 저장 (Unit 1 실습에서 씀)
- [x] Discord 가입 → `#introduce-yourself`에 자기소개, Hugging Face Hub 아래 courses 채널 확인 (권장)
- [ ] 라이브 1 영상 보기
- [ ] 현준과 공부 요일·시간 정하기

## 코스 구조 메모

<!-- 소개 페이지에서 확인한 것: 유닛 구성, 인증서 조건, 권장 진도, 필요한 도구 -->

- 인증서 조건:
- 권장 진도:
- 필요한 도구:

## Step 5 메모 — Ollama로 로컬 실행 (선택)

- 언제 쓰나: HF Inference **무료 크레딧 한도에 걸렸을 때**의 대안. 필수 단계 아님.
- 내 이해(2026-11-12): Ollama를 깔아서 모델을 **내 컴퓨터에서** 돌리고, 에이전트는 그 모델을 쓰게 한다.
- 구조: `ollama pull`(모델 받기) → `ollama serve`(내 PC에 `localhost:11434` 서버 띄우기) → smolagents에서 `InferenceClientModel` 대신 `LiteLLMModel`로 그 서버를 가리킴. 에이전트 코드는 그대로.
- 장점: 무료·횟수 제한 없음, 오프라인, 데이터가 밖으로 안 나감.
- 단점: 내 PC 사양(RAM/GPU)에 묶임 — 7B 모델 ≈ 4~5GB, RAM 8GB 이상 권장. 작은 모델이라 도구 호출·추론이 큰 호스팅 모델보다 약함 → 에이전트가 형식을 틀리기 쉬움.
- 보충: `num_ctx=8192`는 컨텍스트 길이. Ollama 기본값이 작아서 에이전트의 긴 시스템 프롬프트(도구 설명)가 잘리지 않게 늘리는 것.
- 보충: 원문은 "OpenAI 호환 API라서 된다"고 하지만, `ollama_chat/` 접두사를 쓰면 LiteLLM은 Ollama 자체 API(`/api/chat`)로 보낸다. 핵심은 "LiteLLM이 여러 API 형식을 통일해 준다"는 것. (OpenAI 호환 주소는 `/v1`에 따로 있음)
- 클라우드 세션(이 Claude 앱)에서는 못 돌림 → 내 PC에서 할 실습.

## 라이브 1 메모

<!-- 영상 보면서 기억할 것만. 질문은 ../../questions.md 로 -->

-

## 한 줄 소감

-
