import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

system_message = "You are a helpful personal assistant."
messages = []

tools = [
    {
        "type": "function",
        "function": {
            "name": "check_calendar",
            "description": "Check the user's calendar for events on a given date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date to check in YYYY-MM-DD format."
                    }
                },
                "required": ["date"]
            }
        }
    }
]

def check_calendar(date):
    return "10am: Team standup, 2pm: Dentist appointment"

def execute_tool(name, args):
    if name == "check_calendar":
        return check_calendar(**args)
    return f"Unknown tool: {name}"


messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": "What's on my calendar today?"}
]

response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=messages,
    tools=tools,
)

finish_reason = response.choices[0].finish_reason
print(f"Finish reason: {finish_reason}")

# Add initial messages and API call here
messages = [
    {
        "role": "system",
        "content": system_message
    },
    {
        "role":"user",
        "content": "What's on my calendar today?"
    }
]

response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    tools = tools,
    messages=messages
)

if finish_reason == "tool_calls":
    assistant_message = response.choices[0].message
    messages.append(assistant_message)

    for tool_call in assistant_message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        result = execute_tool(name, args)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        })

    final_response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=messages,
        tools=tools,
    )
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)

		
		
		
		
```
Congratulations
You have built a working tool-calling application. Here is what you accomplished:

Defined tool schemas that the LLM can read and act on
Wrote a tool-call loop that detects finish_reason == "tool_calls" and dispatches execution
Returned tool results to the model so it could compose a complete answer
Let the model decide when to call the tool based on the user's request
```
		

