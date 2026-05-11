Every Agent has five components:

System Prompt - gives the agent its identity and instructions
Tool - a callable function the agent can invoke
Memory - the messages list that carries full conversation history
Orchestration Loop - detects tool calls, executes them, feeds results back
Model - the LLM that reads context and decides what to do next



The system prompt is where you give the agent its identity and behavioral instructions. It is always the first message in the messages list.

Tools are what allow the agent to act in the world beyond generating text. Each tool has two parts: a definition (which describes it to the model in JSON Schema format) and a handler (a Python function that does the actual work).