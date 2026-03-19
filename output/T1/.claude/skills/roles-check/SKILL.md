---
name: roles-check
description: Run any artifact through the full org. Reads .craft/roles/ and selects relevant reviewers based on artifact type. Each r
allowed-tools: [Read, Write, Glob]
param_set: full
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


| Axis | Execution Position            | Schema Field Governed                   | Behavioral Contract               | Compliant   |
|------|-------------------------------|-----------------------------------------|-----------------------------------|-------------|
| A    | CH-ID REGISTRATION TABLE      | CH-ID Challenge Table §0 Grounding      | §10 CH-ID CHALLENGE REGISTRATION  | [YES/NO]    |
| B    | BRACKET OPENING               | NH Dimension Comparison Table Col A     | §16 NH DIMENSION TABLE CONTRACT   | [YES/NO]    |
| C    | BRACKET CLOSING (if OVERRIDE) | LOCAL GATE LEDGER ROW BRACKET CLOSING   | §1 ALGEBRA + §4 PROGRESSION       | [YES/NO/NA] |
| D    | DISPOSITION                   | DISPOSITION Primary Driver field        | §19 PRIMARY DRIVER DERIVATION     | [YES/NO/NA] |