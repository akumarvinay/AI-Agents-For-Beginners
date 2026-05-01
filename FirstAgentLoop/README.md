## First Agent Loop — Overview

A minimal agent loop demonstrating a multi-turn conversation with an LLM. This example shows how to:

- Configure an OpenAI client from environment variables.
- Drive a multi-turn conversation through a shared history.
- Exit cleanly when the model signals completion by inspecting `finish_reason`.

## What you built

- An OpenAI client configured from environment variables.
- A continuous loop that calls the LLM and inspects `finish_reason`.
- A multi-turn conversation driven by a shared history.
- A simple agent loop that exits when `finish_reason == "stop"`.

## How it works

1. The program loads OpenAI credentials (and any other configuration) from environment variables.
2. It maintains a conversation history and repeatedly calls the LLM to get the next response.
3. After each response, the loop checks the LLM's `finish_reason`:
	- If `finish_reason == "stop"`, the agent exits.
	- Otherwise, the conversation continues. This is where tool calls would be handled in more advanced agents.

The core loop—checking `finish_reason == "stop"` to decide whether to exit—is the foundation for adding tools and other agent features later.

## Files

- `agent_loop.py` — Example agent loop implementation (located in this folder).
- `README.md` — This document.

## Next steps

The next lesson extends this loop with:

- Tools (functions the agent can call).
- Tool execution and result wiring.
- Memory management for richer conversations.
- A system prompt to steer agent behavior.

## Quick start

1. Set your OpenAI API key in the environment (example for PowerShell):

```powershell
$env:OPENAI_API_KEY = "your_api_key_here"
```

2. Run the loop script:

```powershell
python .\agent_loop.py
```

3. (Optional but recommended) Create and activate a Python virtual environment, then install dependencies:

```powershell
# Create a venv named .venv
python -m venv .venv

# Activate the venv (PowerShell)
. .\venv\Scripts\Activate.ps1

# Upgrade pip and install the OpenAI package
python -m pip install --upgrade pip
python -m pip install openai
```

Alternatively, if you have a `requirements.txt` file in this folder, install with:

```powershell
python -m pip install -r requirements.txt
```

## Notes

- The loop's structure stays the same when you add tools; only the branch that handles tool calls changes.
- Keep conversation history small to control API usage and costs.

## Completion summary

- Preserved original points: OpenAI client from env, multi-turn loop, and `finish_reason` check — Done.
- Produced a tidy README with sections and quick start instructions — Done.
