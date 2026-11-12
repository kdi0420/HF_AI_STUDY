"""Onboarding Step 5 확인용: 로컬 Ollama 모델을 smolagents로 불러 본다.

실행 전: Ollama 설치 + `ollama pull qwen2:7b` + Ollama 서버가 떠 있어야 한다.
실행: python ollama_check.py
"""
import sys
import urllib.request

from smolagents import CodeAgent, LiteLLMModel

API_BASE = "http://127.0.0.1:11434"
MODEL_ID = "ollama_chat/qwen2:7b"  # 다른 모델이면 여기만 바꾼다

# 1) 서버가 떠 있는지
try:
    with urllib.request.urlopen(API_BASE, timeout=3) as r:
        print("[1/3] 서버:", r.read().decode().strip())  # "Ollama is running"
except OSError as e:
    sys.exit(f"[1/3] 서버에 연결 못 함 ({e}). Ollama 앱을 켜거나 `ollama serve`를 실행하세요.")

model = LiteLLMModel(model_id=MODEL_ID, api_base=API_BASE, num_ctx=8192)

# 2) 모델에 직접 한 번 묻기
messages = [{"role": "user", "content": [{"type": "text", "text": "한 문장으로 자기소개 해줘."}]}]
print("[2/3] 모델 답:", model.generate(messages).content)

# 3) 에이전트로 한 번 돌려 보기 (작은 모델이라 형식을 틀려 몇 번 재시도할 수 있음)
agent = CodeAgent(tools=[], model=model, max_steps=3)
print("[3/3] 에이전트 답:", agent.run("2의 10제곱은 얼마야? 파이썬으로 계산해서 답해."))
