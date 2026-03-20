---
mode: agent
description: "Shareable status document with progress table and readiness statement."
---
Write a shareable status document for a topic. Same information as topic-status but as a file. --format teams produces a compact ASCII card suitable for paste into Teams or a standup doc. Progress table, open signals with owners, readiness statement, recommended next step.

Write artifact to: signals/{topic}/status-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
