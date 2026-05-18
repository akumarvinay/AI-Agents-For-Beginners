Here is what you built and why each part matters:

Thought: before every tool call - the model must articulate its reasoning before acting. This is not decoration. It shapes the action that follows and makes the agent easier to debug.
Observation: after every tool result - the model explicitly processes what it learned before deciding the next step. This prevents the model from ignoring tool output.
Multi-step reasoning - with a harder task and two tools, you saw the full ReAct loop: Thought, Act, Observe, repeat until done.
Side-by-side comparison - running both versions in one script made the difference concrete. Same task, same tools, different quality of reasoning.
In production, visible reasoning also helps you debug agents that go wrong. When an agent fails, the Thought lines tell you where its logic broke down.