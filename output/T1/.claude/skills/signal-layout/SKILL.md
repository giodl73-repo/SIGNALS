---
name: signal-layout
description: "Show or change your Signal navigation layout. Five variants: A) grouped (9 namespaces), B) groups (5 phases: discover/sp"
allowed-tools: [Read, Write, Bash]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Show or change your Signal navigation layout. Five variants: A) grouped (9 namespaces), B) groups (5 phases: discover/specify/validate/simulate/govern), C) signal (conversational /signal routes everything), D) flat (/scout-competitors style), E) bare (/competitors style). Called bare: shows current layout and what to try. Called with switch <variant>: runs the appropriate install script. Called with recommend: analyzes which skills you have used most and suggests the best layout for your pattern. Use after install to explore different navigation styles.