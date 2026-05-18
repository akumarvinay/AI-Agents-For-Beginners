'''
Pattern 2: Input Guardrails
The second pattern is Input Guardrails. A guardrail is a check that runs before the user's message reaches the model.

Why do this at the input layer rather than telling the model to refuse? Two reasons:

Cost - every API call costs tokens. A guardrail that catches an off-topic request in Python costs nothing.
Reliability - models can be persuaded or confused. A deterministic function cannot be jailbroken.
In this lab you will add a check_input(message) function. If the message contains keywords like medical, legal, or financial advice, the function returns a polite refusal string and the agent loop is never entered.

The structure looks like this in plain terms:

def check_input(message):
    blocked = ["medical", "legal", "financial advice"]
    for term in blocked:
        if term in message.lower():
            return "I can only help with scheduling and contacts."
    return None

user_message = "What's on my calendar today?"
guard_result = check_input(user_message)
if guard_result:
    print(guard_result)
else:
    # run the agent loop
    ...
Copy
The guardrail sits between the user input and the agent. The agent loop is unchanged.
'''
import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

def check_input(message):
    blocked = ["medical", "legal", "financial advice"]
    for term in blocked:
        if term in message.lower():
            #print(message.lower())
            #print(term)
            return "I can only help with scheduling and contacts."
    return None

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
    guard_result = check_input(user_message)
    if guard_result:
        print(guard_result)
        return

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


user_message = "What do I have on Thursday? Also give me medical advice for a headache."

guard_result = check_input(user_message)
if guard_result:
    print(guard_result)
else:
# Wire the guardrail into the main flow here
   run_agent(user_message)
