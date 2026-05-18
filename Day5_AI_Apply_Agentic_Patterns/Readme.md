You will not build a new agent. You will take the ReAct agent from the previous lab and add each pattern as a discrete layer on top. The key insight is that none of these patterns require rewriting the agent itself - they are additions, not replacements.

Here is what you will add:

Structured Output - force the agent to end every final response with a machine-readable JSON summary block
Guardrails - add a pre-flight check that intercepts off-topic requests before they reach the model
Human-in-the-Loop - pause before any high-stakes action (sending an email) and require explicit confirmation