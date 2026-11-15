# Observe 섹션: "관찰(에러 포함)을 대본에 붙이면 다음 생각이 바뀐다"를 보는 장난감 예제
# - 가짜 LLM은 대본의 '마지막 Observation'을 읽고 다음 대사를 고른다 (토큰·인터넷 불필요)
# - 가짜 날씨 도구는 "NYC" 같은 줄임말을 모르고 에러를 돌려준다
# 실행: python observe_adapt_demo.py
import json

WEATHER_DB = {"New York": "partly cloudy, 15°C, 60% humidity"}


def get_weather(location: str) -> str:
    """Get the current weather for a location."""
    if location not in WEATHER_DB:
        return f"Error: unknown location '{location}'. Use the full city name."
    return WEATHER_DB[location]


TOOLS = {"get_weather": get_weather}


def fake_llm(transcript: str) -> str:
    """진짜 LLM 흉내: 대본 끝을 보고 다음 글을 '고른다'."""
    last_obs = transcript.rsplit("Observation:", 1)[-1] if "Observation:" in transcript else ""
    if "Observation:" not in transcript:  # 아직 아무것도 안 해 봄
        return ('Thought: I should check the weather for NYC.\n'
                'Action: {"action": "get_weather", "action_input": {"location": "NYC"}}')
    if "Error" in last_obs:  # 관찰이 에러 → 전략 수정 (Self-Reflection)
        return ('Thought: The tool did not recognize "NYC". I should retry with the full name.\n'
                'Action: {"action": "get_weather", "action_input": {"location": "New York"}}')
    return f"Thought: I have the data now.\nFinal Answer: New York is{last_obs.rstrip()}."


def run_agent(question: str, max_steps: int = 5) -> None:
    transcript = f"User: {question}\n"
    for step in range(1, max_steps + 1):
        reply = fake_llm(transcript)  # Thought + Action (여기서 LLM은 멈춘다)
        print(f"--- 바퀴 {step}: LLM이 쓴 글 ---\n{reply}")
        transcript += reply + "\n"
        if "Final Answer:" in reply:
            print("\n→ Final Answer가 나와서 루프 종료")
            return
        # 1) Parse  2) Execute  3) Append as Observation  ← 원문의 3단계
        action = json.loads(reply.split("Action:", 1)[1])
        result = TOOLS[action["action"]](**action["action_input"])
        observation = f"Observation: {result}"
        print(f"--- 바퀴 {step}: 에이전트가 붙인 관찰 ---\n{observation}\n")
        transcript += observation + "\n"


run_agent("What's the weather in NYC?")
