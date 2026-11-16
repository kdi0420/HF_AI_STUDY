# Dummy Agent Library 섹션을 집 데스크탑 Ollama로 따라 하는 스크립트
# - 원문은 HF 서버(Serverless API, 모델 moonshotai/Kimi-K2.5)를 부르지만,
#   무료 크레딧이 0이라 같은 흐름을 내 PC의 Ollama(qwen3.5:9b)로 한다 (2026-11-16 결정)
# - 파이썬 기본 패키지만 씀 (pip 설치 불필요, HF 토큰 불필요)
# - 준비: Ollama 앱이 켜져 있고 `ollama list`에 qwen3.5:9b가 있어야 함
# 실행: python dummy_agent_ollama.py
import json
import os
import urllib.request

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
MODEL = os.environ.get("OLLAMA_MODEL", "qwen3.5:9b")


def chat(messages, max_tokens=200, stop=None):
    """원문의 client.chat.completions.create(...)와 같은 역할.

    - messages: [{"role": ..., "content": ...}] 목록 → Ollama가 채팅 템플릿을 씌워 모델에 넣음
    - max_tokens: 최대 몇 토큰까지 쓸지 (Ollama에선 num_predict)
    - stop: 이 글자가 나오기 직전에 생성을 멈춤 (stop sequence)
    - think=False: 원문의 extra_body={'thinking': {'type': 'disabled'}}와 같은 뜻 (속생각 끄기)
    """
    options = {"num_predict": max_tokens}
    if stop:
        options["stop"] = stop
    body = {"model": MODEL, "messages": messages, "stream": False, "think": False, "options": options}
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/chat",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read())["message"]["content"]


def show(title, text):
    print("=" * 60)
    print(title)
    print("-" * 60)
    print(text)
    print()


# ── 1) Serverless API 자리: 그냥 질문 하나 ─────────────────────────────
show(
    "1) 기본 호출: 'The capital of France is'",
    chat([{"role": "user", "content": "The capital of France is"}], max_tokens=50),
)

# ── 2) 도구 설명 + 사이클 규칙이 들어간 system prompt (원문 그대로) ──────
SYSTEM_PROMPT = """Answer the following questions as best you can. You have access to the following tools:

get_weather: Get the current weather in a given location

The way you use the tools is by specifying a json blob.
Specifically, this json should have an `action` key (with the name of the tool to use) and an `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are:
get_weather: Get the current weather in a given location, args: {"location": {"type": "string"}}
example use :

{{
  "action": "get_weather",
  "action_input": {"location": "New York"}
}}

ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:

$JSON_BLOB (inside markdown cell)

Observation: the result of the action. This Observation is unique, complete, and the source of truth.
... (this Thought/Action/Observation can repeat N times, you should take several steps when needed. The $JSON_BLOB must be formatted as markdown and only use a SINGLE action at a time.)

You must always end your output with the following format:

Thought: I now know the final answer
Final Answer: the final answer to the original input question

Now begin! Reminder to ALWAYS use the exact characters `Final Answer:` when you provide a definitive answer. """

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "What's the weather in London?"},
]

# ── 3) 멈추지 않고 부르기 → Observation을 지어내는지 보기 ────────────────
show(
    "2) stop 없이 호출 (Observation을 스스로 지어내면 = 환각)",
    chat(messages, max_tokens=200),
)

# ── 4) "Observation:" 직전에서 멈추기 ────────────────────────────────
partial = chat(messages, max_tokens=150, stop=["Observation:"])
show("3) stop=['Observation:']으로 호출 (Action까지만 써야 정상)", partial)


# ── 5) 가짜 도구 (진짜라면 날씨 API를 부를 자리) ─────────────────────
def get_weather(location):
    return f"the weather in {location} is sunny with low temperatures. \n"


# 원문은 get_weather('London')을 손으로 불렀다.
# 여기선 Actions 섹션의 "parse"까지 해 본다: 모델이 쓴 JSON에서 location을 꺼낸다.
location = "London"  # JSON 읽기에 실패하면 원문처럼 London으로
try:
    blob = partial[partial.index("{"): partial.rindex("}") + 1]
    location = json.loads(blob)["action_input"]["location"]
except (ValueError, KeyError, TypeError):
    print("(JSON 읽기 실패 → 원문처럼 'London'으로 직접 부름)\n")
observation = get_weather(location)
show(f"4) 진짜(가짜) 도구 실행: get_weather({location!r})", observation)

# ── 6) 진짜 Observation을 붙여 다시 부르기 ─────────────────────────────
# 원문(6-A)은 관찰을 assistant 칸에 이어 붙이지만, Ollama + qwen3.5에서는 잘 안 돼서(2026-11-16 실습)
# 관찰을 새 user 메시지로 보내는 6-B 방식을 쓴다
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "What's the weather in London?"},
    {"role": "assistant", "content": partial},
    {"role": "user", "content": "Observation:\n" + observation},
]
show(
    "5) Observation을 user 메시지로 보내고 다시 호출 → Final Answer를 써야 함",
    chat(messages, max_tokens=200),
)
