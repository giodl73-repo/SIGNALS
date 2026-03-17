---
name: track
description: "Manage the topic narrative and program plan. Combines topic + program into a single
dashboard command for topic health and signal coverage.

Covers:
- topic-new    -> register the topic with strategy planning and signal coverage plan
- topic-plan   -> revise signal strategy as new information arrives
- topic-status -> terminal coverage display computed from signal glob against strategy
- topic-story  -> editorial synthesis of all signals into a coherent narrative
- topic-echo   -> unexpected findings: what did we learn that we did not expect?

Output: a topic dashboard showing signal coverage, narrative synthesis, and the echo
(what we learned that we did not plan to learn). Includes a readiness statement:
ready to commit, needs these signals, or blocked on this decision.

Use at the start of a topic (topic-new), after each signal run (topic-status), and
at decision time (topic-story + topic-echo). The dashboard is the PM's artifact.
"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
Show the current state of a topic in the terminal. Signal coverage, open gaps, readiness for target outcome. Does NOT write a file -- display only. For a written artifact use topic-report. Globs simulations/**/{topic}-* to discover all signals. Cross-references against strategy.md planned signals. Computes coverage percentage.

Write artifact to: none (terminal display only)
