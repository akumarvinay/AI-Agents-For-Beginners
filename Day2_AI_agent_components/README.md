# Agent Components Overview

Every agent has five core components:

1. **System Prompt** - gives the agent its identity and instructions
2. **Tool** - a callable function the agent can invoke
3. **Memory** - the messages list that carries full conversation history
4. **Orchestration Loop** - detects tool calls, executes them, feeds results back
5. **Model** - the LLM that reads context and decides what to do next

---

## 1. System Prompt

The system prompt defines the agent's identity and behavior. It is always the first message in the messages list, and it guides the model on how to respond and when to use tools.

## 2. Tools

Tools let the agent act in the world beyond text generation.

Each tool consists of:

- a **definition** (described to the model in JSON Schema format)
- a **handler** (a Python function that performs the actual work)

## 3. Memory

You do not need to add any new code for memory. The message list itself is the agent's memory.

Every time you append a message — whether it is a user message, an assistant message, or a tool result — you extend the agent's context window.

Because the model reads the entire list on every API call, it always has the full conversation history.

This is the simplest form of memory: a growing list. Later labs examine what happens when that list becomes too large and how to manage it.

## 4. Orchestration Loop

The orchestration loop connects all of the components.

It does more than just detect when the conversation should stop. It also:

- detects when the model requests a tool
- executes that tool
- feeds the result back into memory
- continues the loop until the task is complete

## 5. Final Integration

All five components are now wired into a single working script:

- **System Prompt** - gives the agent identity and instructs it to use tools
- **Tool** - the `check_calendar` function the agent can call
- **Memory** - the messages list that carries the full conversation
- **Orchestration Loop** - detects tool calls, runs them, and feeds results back
- **Model** - the brain that reads context and decides what to do next