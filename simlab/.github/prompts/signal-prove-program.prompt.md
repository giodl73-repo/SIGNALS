---
mode: agent
description: "General-purpose research orchestrator for open-ended research questions."
---
General-purpose research orchestrator. Takes a research question, plans experiments (which prove skills + web searches + data analysis), runs them in sequence, feeds outputs forward, synthesizes findings. More flexible than prove-topic: not limited to a Signal topic, can run any combination of prove skills, web searches, and custom experiments. Use for open-ended research questions that may span multiple namespaces or require custom experiment sequences. Output: Qx.md style research document with hypothesis, experiments, findings, and principles.

Write artifact to: signals/prove/research/{topic}-research-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
