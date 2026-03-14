---
skill: trace-skill
topic: plugin
item: scout-naming
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
---

# /trace-skill -- scout-naming

**Invocation**: `/scout-naming "the plugin that helps teams gather signals before committing to a feature build" --constraint "single word, active, developer-resonant"`
**Scenario**: PM who just renamed from "sim" to "signal" wants to validate the name choice and explore alternatives

## Phase 1: Setup

Domain vocabulary extracted from CLAUDE.md and plugin-plan.md: simulate, signal, probe, trace, scout, draft, review, flow, prove, listen, echo. Prior name "sim" flagged as retiring. Constraint parsed. Roles: PM, Design, UX, GTM, Strategy. PASS.

## Phase 2: Execute

12 candidates generated. Scoring weights: PM 25%, Strategy 25%, GTM 20%, UX 20%, Design 10%.

### Naming Matrix (top 5 of 12)

| Candidate | PM | Strategy | GTM | UX | Design | Weighted |
|-----------|-----|---------|-----|-----|--------|---------|
| SIGNAL | 9 | 9 | 8 | 8 | 7 | 8.4 |
| PULSE | 8 | 7 | 7 | 8 | 8 | 7.6 |
| SCOUT | 8 | 7 | 7 | 8 | 7 | 7.6 |
| PROBE | 8 | 7 | 7 | 7 | 7 | 7.4 |
| BEACON | 7 | 7 | 7 | 8 | 7 | 7.2 |

**Top pick**: SIGNAL (8.4) -- name IS the mission ("gather signals before committing"), speakable, clean in CLI namespace, best positioning fit.

**Runner-up**: PULSE (7.6) -- viable fallback.

**SCOUT disqualified**: Internal namespace collision -- /scout: is already a skill namespace.

**Collision check**: Signal messaging app is notable brand overlap, manageable at org-scoped package level.

## Phase 3: Findings

Top 3: SIGNAL, PULSE, PROBE. SIGNAL validated as strongest available. Collision check complete.

## Phase 4: Amend

1. Add `--validate <name>` flag -- currently validation is accidental (name must be included in input to be scored)
2. Re-weight GTM higher if public npm uniqueness is a hard constraint
3. Relax single-word constraint to open compound candidate class

## Verdict

**Result**: USEFUL. Correct answer. One design gap.

### Findings Register

| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | No designed `--validate <name>` path -- validation is accidental, not designed. Fix: pin named candidate at row 1, add "Validation Summary" block | P2 |
