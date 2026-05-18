
import json
import os
from openai import OpenAI

'''
Pattern 1: Structured Output
The first pattern is Structured Output. Instead of letting the model return free-form text, you instruct it to always end its final response with a predictable JSON block.

This matters in production because downstream systems - dashboards, logs, orchestrators - need to parse agent responses programmatically. Free-form text is unpredictable. A JSON block at the end is not.

The approach is simple: add one sentence to the system prompt. You are not changing the model or the loop - you are changing what the model is told to produce.

Add this instruction to your system_prompt string:

Always end your final response with a JSON summary block:
{"summary": "...", "actions_taken": ["..."]}

The model will include this block in every response where it reaches a conclusion. The rest of the response stays in natural language - the JSON is appended at the end.
'''

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

system_prompt = "You are a helpful personal assistant. Before every tool call, write 'Thought: [your reasoning]'. After every tool result, write 'Observation: [what you learned]'. Then decide your next step. Always end your final response with a JSON summary block:{'summary': '...', 'actions_taken': ['...']}"

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
run_agent("What is on my calendar today, as today is monday")