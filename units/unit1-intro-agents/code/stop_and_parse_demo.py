# Actions 섹션의 "Stop and Parse"와 "Code Agent"를 눈으로 보기 위한 장난감 예제
# - 진짜 LLM 대신 "멈추지 않고 계속 써 버리는 가짜 LLM 출력"을 쓴다 (토큰·인터넷 불필요)
# - 진짜 날씨 API 대신 고정된 문장을 돌려주는 가짜 도구를 쓴다
# 실행: python stop_and_parse_demo.py
import json


def get_weather(location: str) -> str:
    """Get the current weather for a location."""
    return f"partly cloudy, 15°C (in {location})"


TOOLS = {"get_weather": get_weather}

# 가짜 LLM이 "멈추지 않았을 때" 써 버리는 글.
# Action 뒤에 Observation까지 스스로 지어내고 있다 (= 환각).
RAW_LLM_OUTPUT = (
    "Thought: I need to check the current weather for New York.\n"
    'Action: {"action": "get_weather", "action_input": {"location": "New York"}}\n'
    "Observation: It is sunny and 30°C.\n"  # ← 도구를 부르지도 않았는데 지어낸 결과
    "Final Answer: It is sunny and 30°C in New York."
)

STOP_SEQUENCE = "Observation:"  # 이 글자가 나오면 생성을 멈추라고 정해 둔 신호


def apply_stop(text: str, stop: str) -> str:
    """진짜 API에선 서버가 해 주는 일: stop 글자가 나오기 직전에서 자른다."""
    return text.split(stop)[0]


def parse_json_action(text: str) -> tuple[str, dict]:
    """파서(parser): 'Action:' 뒤 JSON을 읽어 도구 이름과 인자를 꺼낸다."""
    json_part = text.split("Action:", 1)[1].strip()
    action = json.loads(json_part)
    return action["action"], action["action_input"]


print("=" * 60)
print("1) 멈추지 않았을 때 LLM이 쓴 글 (그대로 믿으면 안 됨)")
print("=" * 60)
print(RAW_LLM_OUTPUT)

print("\n" + "=" * 60)
print(f"2) Stop: '{STOP_SEQUENCE}' 직전에서 자름")
print("=" * 60)
stopped = apply_stop(RAW_LLM_OUTPUT, STOP_SEQUENCE)
print(stopped)

print("=" * 60)
print("3) Parse: 파서가 도구 이름·인자를 꺼내서 진짜로 실행")
print("=" * 60)
name, args = parse_json_action(stopped)
print(f"도구 이름: {name!r} / 인자: {args!r}")
observation = TOOLS[name](**args)
print(f"진짜 Observation: {observation}")

print("\n" + "=" * 60)
print("4) Code Agent: JSON 대신 파이썬 코드를 쓰면 반복문도 한 번에")
print("=" * 60)
# 가짜 LLM이 쓴 코드 블록. JSON 하나로는 도시 하나만 부를 수 있지만,
# 코드면 for 문으로 세 도시를 한 번의 Action에 처리할 수 있다.
LLM_CODE = """
results = []
for city in ["New York", "Paris", "Seoul"]:
    results.append(f"{city}: {get_weather(city)}")
final_answer = " / ".join(results)
print(final_answer)
"""
print(LLM_CODE)
print("--- 실행 결과 ---")
# 주의: exec는 LLM이 쓴 코드를 그대로 실행한다 → 진짜로는 위험!
# 여기선 우리가 직접 쓴 안전한 코드라서 괜찮다. 실제로는 smolagents처럼
# 쓸 수 있는 함수·모듈을 제한한 실행기(샌드박스)를 써야 한다.
exec(LLM_CODE, {"get_weather": get_weather})
