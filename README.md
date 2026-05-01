# AI-Agents-For-Beginners

A small learning repository for building simple AI agents and understanding agent workflows. This is my first repo for exploring agent loops, tools, memory, and system prompts.

## Purpose

Capture a sequence of tiny, focused examples that show how to drive an LLM in a loop, wire tools into the loop, and manage short-term conversation memory. The goal is learning and experimentation — not production readiness.

## Repo structure

- `FirstAgentLoop/` — A minimal example demonstrating a multi-turn agent loop (`agent_loop.py`) and related notes.

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
. .\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r FirstAgentLoop\requirements.txt
```

3. Set your OpenAI API key (example):

```powershell
$env:OPENAI_API_KEY = "your_api_key_here"
```

4. Run the example loop:

```powershell
python FirstAgentLoop\agent_loop.py
```

## Notes and next steps

- This repo is for hands-on learning. Expect frequent changes as you iterate.
- Next lessons will add tools, tool execution, memory management, and system prompts.
- If you'd like, I can add a CONTRIBUTING guide, simple tests, or CI next.

---
If you want a shorter or more formal README (with badges, license, or contributor guidelines), tell me which parts to include and I will update it.
# AI-Agents-For-Beginners
