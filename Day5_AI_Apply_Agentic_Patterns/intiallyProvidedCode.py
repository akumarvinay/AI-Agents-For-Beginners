import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

def check_calendar(day):
    events = {
        "monday": "Team standup at 9am",
        "tuesday": "Dentist at 2pm",
        "wednesday": "No events",
        "thursday": "1pm lunch with Alex, 3pm product review",
        "friday": "Weekly retro at 4pm"
    }
    return events.get(day.lower(), "No events found for that day.")

tools = [
    {
        "type": "function",
        "function": {
            "name": "check_calendar",
            "description": "Check the calendar for a given day.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "string", "description": "Day of the week"}
                },
                "required": ["day"]
            }
        }
    }
]

system_prompt = "You are a helpful personal assistant. Before every tool call, write 'Thought: [your reasoning]'. After every tool result, write 'Observation: [what you learned]'. Then decide your next step."

def run_agent(user_message):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    while True:
        response = client.chat.completions.create(
            model="openai/gpt-4.1-mini",
            messages=messages,
            tools=tools
        )
        msg = response.choices[0].message
        messages.append(msg)
        if msg.tool_calls:
            for tc in msg.tool_calls:
                args = json.loads(tc.function.arguments)
                if tc.function.name == "check_calendar":
                    result = check_calendar(**args)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result
                })
        else:
            print(msg.content)
            break

# Run the agent with a new task here
