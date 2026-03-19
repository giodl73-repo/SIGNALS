---
name: discover-hypothesis
description: "State what you believe and what would change your mind. Entry point to a prove investigation. A hypothesis has: a claim"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


State what you believe and what would change your mind. Entry point to a prove investigation. A hypothesis has: a claim (what you believe), a falsification condition (what evidence would prove it wrong), a confidence level (0-100), and a list of experiments that will test it. The hypothesis is a commitment -- you cannot move the goalposts after seeing results.