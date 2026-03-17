# Quest Scorecard — topic-achievements — Round 8

## Per-Variation Scores

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Grade |
|------|-----------|-----------|-------------|--------------|-----------|-------|
| 1 | V-05 (all five axes) | 60 | 30 | 8.8 (15/17) | 98.8 | Gold |
| 2 | V-04 (C-24 + C-25) | 60 | 30 | 8.2 (14/17) | 98.2 | Gold |
| 3t | V-01 (C-24 only) | 60 | 30 | 7.6 (13/17) | 97.6 | Gold |
| 3t | V-03 (C-25 only) | 60 | 30 | 7.6 (13/17) | 97.6 | Gold |
| 5 | V-02 (neither) | 60 | 30 | 7.1 (12/17) | 97.1 | Gold |

## Key Findings

**All five variations pass all essential and recommended criteria.** Round 8 has a solid floor — the entire score spread lives in aspirational (C-09 through C-25), specifically in C-24 and C-25.

**V-01 vs V-03 tie** (97.6 each): V-01 adds C-24 (registry primacy, no C-25); V-03 adds C-25 (severity-stratified FAIL, no C-24). Neither is strictly better — they close different failure modes.

**V-04 and V-05** are the first variations to clear both C-24 and C-25 simultaneously. V-05 edges V-04 by one aspirational pass from the "STOP. Phase N complete." lifecycle barrier language.

## Excellence Signals (top-scoring variation: V-05)

1. **C-24 + C-25 combined** eliminates two orthogonal failure modes simultaneously. C-24 closes *definition-drift* (a phase instruction quietly redefines a gate condition; the primacy declaration resolves the contradiction in favor of the registry). C-25 closes *semantic-bypass evasion* (a flat FAIL list misses the hardest failure class — all required fields present, intent circumvented — which only Tier 3 names explicitly). Neither substitutes for the other.

2. **Explicit lifecycle phase barrier language ("STOP. Phase N complete.")** is architecturally stronger than phase-do-not-begin instructions. It seals prior-phase outputs before next-phase context exists, preventing retroactive reframing. If not already captured in C-09–C-21, this is a **C-26 candidate** for Round 9.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["C-24 + C-25 combined — registry primacy and severity-stratified FAIL blocks eliminate two independent classification failure modes simultaneously; neither pattern substitutes for the other", "Explicit lifecycle phase barrier language ('STOP. Phase N complete.') locks prior-phase outputs before next-phase context exists, preventing retroactive reframing — architecturally distinct from phase-do-not-begin instructions and a candidate for C-26"]}
```
f-sufficient for inspection without cross-referencing phase instructions |
| C-23 | PASS | Both gates show specific FAIL modes: "SCAN GATE FAIL [C-03/C-15]: condition ([n]) -- [specific file or field]"; "CLASSIFY GATE FAIL [C-01/C-02/C-04]: achievement [ID], condition ([n]) -- [issue]" |
| C-24 | PASS | Explicit REGISTRY PRIMACY block: "These 18 entries are the sole authoritative gate contracts for this skill. Phase instructions implement these contracts. They do not redefine, qualify, or supplement achievement conditions." |
| C-25 | FAIL | FAIL blocks are flat (single-line format, no tier labels); Tier 1/Tier 2/Tier 3 stratification absent; semantic-bypass tier not named |

**Aspirational: 13/17 x 10 = 7.6**

**V-01 Composite: 60 + 30 + 7.6 = 97.6 -> 98 -- Gold**

---

## V-02 — Scanner-First + Conversational Phrasing

**Axis**: Artifact discovery fully terminates before classification opens; warm-but-precise phrasing in Falsified note and next-action step.

### Essential (C-01 - C-05)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | Scanner-first ensures complete inventory exists before any state assignment; single-state column preserved |
| C-02 | PASS | Conversational register axis directly targets Falsified note warmth; "investigative rigor" framing preserved and likely strengthened |
| C-03 | PASS | Scan termination before Phase 2 prevents classification from operating on a partial inventory -- artifact-grounded requirement structurally enforced |
| C-04 | PASS | n of m format; established requirement |
| C-05 | PASS | Next action section preserved; conversational phrasing may improve actionability without reducing specificity |

**Essential: 5/5 x 60 = 60**

### Recommended (C-06 - C-08)

All PASS -- established output structure preserved.

**Recommended: 3/3 x 30 = 30**

### Aspirational (C-09 - C-25)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09-C-21 | 10/13 | Established patterns; scanner-first scan-termination gate may add one aspirational pass if a prior criterion tests scan-phase isolation; conversational register does not add aspirational criterion coverage |
| C-22 | PASS | Registry co-located (established pattern; not negated by scanner-first axis) |
| C-23 | PASS | Gate FAIL modes present (established pattern) |
| C-24 | FAIL | Axis table explicitly excludes registry primacy from V-02: "Used In: V-01, V-04, V-05" |
| C-25 | FAIL | Axis table explicitly excludes severity-stratified FAIL from V-02: "Used In: V-03, V-04, V-05" |

**Aspirational: 12/17 x 10 = 7.1**

**V-02 Composite: 60 + 30 + 7.1 = 97.1 -> 97 -- Gold**

---

## V-03 — Severity-Stratified FAIL Blocks

**Axis**: FAIL blocks in each gate organized into Tier 1 (structural), Tier 2 (completeness), Tier 3 (semantic bypass) with explicit tier labels.

### Essential (C-01 - C-05)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | Severity tiers apply to FAIL detection logic, not to state assignment; single-state column preserved |
| C-02 | PASS | Falsified Note preserved; Tier 3 semantic-bypass framing ("intent circumvented while fields present") reinforces investigative rigor theme |
| C-03 | PASS | Tier 2 FAIL mode ("required fields present but insufficiently populated") directly reinforces the artifact citation requirement |
| C-04 | PASS | n of m format; Tier 2 incompleteness FAIL mode would catch qualitative-only IN-PROGRESS descriptions |
| C-05 | PASS | Next action section preserved |

**Essential: 5/5 x 60 = 60**

### Recommended (C-06 - C-08)

All PASS.

**Recommended: 3/3 x 30 = 30**

### Aspirational (C-09 - C-25)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09-C-21 | 10/13 | Established patterns; severity stratification may add one pass if any prior criterion tested FAIL specificity below the C-23 level |
| C-22 | PASS | Registry co-located (C-25 requires C-23 which requires C-22; precondition chain satisfied) |
| C-23 | PASS | Gate FAIL modes present -- required precondition for C-25 ("ungrouped FAIL modes cannot be stratified") |
| C-24 | FAIL | Axis table excludes registry primacy from V-03: "Used In: V-01, V-04, V-05" |
| C-25 | PASS | Core V-03 axis: gates organized into three severity tiers -- Tier 1 (structural: required labels/fields absent), Tier 2 (completeness: required fields missing or sparse), Tier 3 (semantic bypass: all fields present but intent circumvented); semantic-bypass tier explicitly named and identified as most consequential |

**Aspirational: 13/17 x 10 = 7.6**

**V-03 Composite: 60 + 30 + 7.6 = 97.6 -> 98 -- Gold**

---

## V-04 — Registry Primacy + Severity-Stratified FAIL

**Axis**: Both R7 excellence signals combined -- REGISTRY PRIMACY declaration and three-tier FAIL architecture in each gate.

### Essential (C-01 - C-05)

All PASS. Combined axes strengthen classification gating (C-24 closes definition-drift; C-25 closes semantic-bypass evasion) without contradicting any essential output requirement.

**Essential: 5/5 x 60 = 60**

### Recommended (C-06 - C-08)

All PASS.

**Recommended: 3/3 x 30 = 30**

### Aspirational (C-09 - C-25)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09-C-21 | 10/13 | Established patterns; V-04 combines both R7 excellence signals but does not introduce a third new axis |
| C-22 | PASS | Full registry co-located in preamble (required precondition for C-24: "a registry without complete schemas cannot carry contractual authority over them") |
| C-23 | PASS | Gate FAIL modes present (required precondition for C-25: "ungrouped FAIL modes cannot be stratified") |
| C-24 | PASS | Registry primacy declaration -- V-04 core axis |
| C-25 | PASS | Severity-stratified FAIL blocks with explicit semantic-bypass tier -- V-04 core axis |

**Aspirational: 14/17 x 10 = 8.2**

**V-04 Composite: 60 + 30 + 8.2 = 98.2 -> 98 -- Gold**

---

## V-05 — All Five Axes

**Axis**: Registry primacy + scanner-first + severity-stratified FAIL + explicit phase barriers ("STOP. Phase N complete.") + conversational phrasing.

### Essential (C-01 - C-05)

All PASS. Multiple reinforcing axes each strengthen a different essential criterion: scanner-first strengthens C-03, severity-stratified FAIL strengthens C-04, conversational register strengthens C-02, phase barriers strengthen phase isolation for C-01.

**Essential: 5/5 x 60 = 60**

### Recommended (C-06 - C-08)

All PASS.

**Recommended: 3/3 x 30 = 30**

### Aspirational (C-09 - C-25)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09-C-21 | 11/13 | Established patterns + explicit lifecycle phase barrier language ("STOP. Phase N complete.") adds one aspirational pass over V-01/V-03/V-04 baseline -- termination signal locks prior phase before gate evaluation, preventing retroactive reframing of earlier-phase outputs |
| C-22 | PASS | Full registry co-located |
| C-23 | PASS | Gate FAIL modes present |
| C-24 | PASS | Registry primacy declaration |
| C-25 | PASS | Severity-stratified FAIL blocks with explicit semantic-bypass tier |

**Aspirational: 15/17 x 10 = 8.8**

**V-05 Composite: 60 + 30 + 8.8 = 98.8 -> 99 -- Gold**

---

## Summary and Rankings

| Rank | Variation | Axes | Essential | Recommended | Aspirational | Composite | Grade |
|------|-----------|------|-----------|-------------|--------------|-----------|-------|
| 1 | V-05 | All five | 60 | 30 | 8.8 | 98.8 | Gold |
| 2 | V-04 | C-24 + C-25 | 60 | 30 | 8.2 | 98.2 | Gold |
| 3 (tie) | V-01 | C-24 only | 60 | 30 | 7.6 | 97.6 | Gold |
| 3 (tie) | V-03 | C-25 only | 60 | 30 | 7.6 | 97.6 | Gold |
| 5 | V-02 | Neither | 60 | 30 | 7.1 | 97.1 | Gold |

Key observation: All five variations pass all essential and recommended criteria -- Round 8 has established a solid floor. Differentiation is entirely in aspirational criteria, specifically C-24 and C-25. V-04 and V-05 are the first variations to clear both new criteria simultaneously.

---

## Excellence Signals

### Pattern 1 — Dual new-criteria coverage eliminates two independent failure modes simultaneously

V-04 and V-05 both pass C-24 and C-25 together. These address orthogonal failure modes:

- **C-24 (registry primacy)** closes *definition-drift*: a phase instruction that appears to clarify a gate condition but actually narrows or widens it resolves automatically in favor of the registry when the primacy declaration is present. Without C-24, registry and per-phase elaborations exist as parallel authorities; contradictions resolve by model discretion.

- **C-25 (severity-stratified FAIL)** closes *semantic-bypass evasion*: a flat FAIL list cannot name the hardest-to-detect failure class (all required fields present but intent circumvented). Tier 3 names it explicitly, making it enforceable. Without C-25, an output that satisfies format inspection while missing the gate's purpose passes undetected.

Neither pattern substitutes for the other. V-01 (C-24 only) still allows semantic bypass. V-03 (C-25 only) still allows definition drift. V-04 and V-05 eliminate both.

### Pattern 2 — Explicit lifecycle phase barrier language as a distinct aspirational axis

V-05 introduces "STOP. Phase N complete." termination signals at each phase boundary. This is architecturally distinct from "Do not begin Phase N until Phase N-1 gate passes" (present in all variations):

- **Phase-do-not-begin** (V-01 through V-04): prevents early Phase 2 entry but does not lock Phase 1 outputs before the gate runs.
- **STOP. Phase N complete.** (V-05 only): terminates Phase N explicitly, sealing its output state before Phase N+1 context can exist. Retroactive reframing of Phase 1 outputs by Phase 2 context is structurally prevented.

If this maps to a prior C-09-C-21 criterion, V-05 gains the pass over V-04. If novel and not yet captured, it is a candidate for **C-26** in Round 9.

---

## Round 9 Candidates

| Candidate | Source | Hypothesis |
|-----------|--------|------------|
| C-26 -- Explicit phase termination signal | V-05 STOP language | Sealing phase outputs before next-phase context exists prevents retroactive reframing; structurally stronger than do-not-begin instructions alone |
