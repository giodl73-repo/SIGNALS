---
name: signal-scout-naming
description: Name generation and evaluation with multi-persona scoring.
allowed-tools: [Read, Write, WebSearch]
param_set: standard
---
Generate and evaluate candidate names using multi-persona scoring. Supports --validate <name> to pin an existing name at row 1 and produce a validation summary alongside alternatives. Generate 10-15 candidates. Score across PM (memorability), Design (visual weight), UX (speakability), GTM (searchability), Strategy (positioning fit). Collision check against package registries and domains. Stock roles: PM, Design, UX, GTM, Strategy.

Write artifact to: simulations/scout/naming/{topic}-naming-{date}.md
