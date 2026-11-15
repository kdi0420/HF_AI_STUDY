# Thought-Action-Observation 루프를 눈으로 보기 위한 장난감 예제
# - 진짜 LLM 대신 "정해진 대사를 읽는 가짜 LLM"을 쓴다 (토큰·인터넷 불필요)
# - 진짜 날씨 API 대신 고정된 문장을 돌려주는 가짜 도구를 쓴다
# 실행: python tao_loop_demo.py
import json


def get_weather(location: str) -> str:
    """Get the current weather for a location."""
    return f"Current weather in {location}: partly cloudy, 15°C, 60% humidity."


TOOLS = {"get_weather": get_weather}

# 가짜 LLM: 호출될 때마다 미리 적어 둔 답을 차례로 돌려준다.
# 진짜 LLM이라면 매번 '지금까지의 대본 전체'를 읽고 이 글을 스스로 만들어 낸다.
SCRIPTED_REPLIES = [
    'Thought: I need to check the current weather for New York.\n'
    'Action: {"action": "get_weather", "action_input": {"location": "New York"}}',
    "Thought: I have the weather data now.\n"
    "Final Answer: The current weather in New York is partly cloudy, 15°C, 60% humidity.",
]


def fake_llm(transcript: str, turn: int) -> str:
    return SCRIPTED_REPLIES[turn]


def run_agent(question: str, max_steps: int = 5) -> str:
    transcript = f"User: {question}\n"
    for turn in range(max_steps):  # while 루프 + 안전장치(최대 횟수)
        reply = fake_llm(transcript, turn)  # 1) Thought (+ Action 또는 Final Answer)
        print(f"--- 바퀴 {turn + 1}: LLM이 쓴 글 ---\n{reply}\n")
        transcript += reply + "\n"

        if "Final Answer:" in reply:  # 목표 달성 → 루프 탈출
            return reply.split("Final Answer:")[1].strip()

        # 2) Action: LLM이 쓴 JSON 글을 읽어서 에이전트가 진짜로 도구를 실행
        action = json.loads(reply.split("Action:")[1])
        result = TOOLS[action["action"]](**action["action_input"])

        # 3) Observation: 결과를 대본에 붙이고 다시 LLM에게 (다음 바퀴)
        print(f"--- 바퀴 {turn + 1}: 에이전트가 도구 실행 → Observation ---\n{result}\n")
        transcript += f"Observation: {result}\n"
    return "최대 횟수 초과: 답을 못 찾음"


if __name__ == "__main__":
    answer = run_agent("What's the current weather in New York?")
    print("=== 사용자에게 보이는 최종 답 ===\n" + answer)
