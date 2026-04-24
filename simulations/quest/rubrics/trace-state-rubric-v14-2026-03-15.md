Reading the scorecard carefully to extract R15 excellence signals before writing.

**R15 signals I'm extracting:**

1. **V-01**: "multi-pass surfaces cross-domain precondition chains" — postconditions in pass N explicitly seed preconditions in pass N+1 (beyond C-02, which is within-pass)
2. **V-01**: "Multi-pass design surfaces one labeled defect per domain" — per-pass defect coverage (beyond C-04, which is one total)
3. **V-03**: "Different defect-class hypothesis vs V-01 exposes distinct defect type — broader hypothesis signal" — domain *ordering* annotated as the hypothesis vehicle (beyond C-36, which is defect hypothesis at pass headings)
4. **V-04 title**: "Lifecycle Emphasis" — entity lifecycle phase labels at state level
5. **V-04 title**: "Four Sub-Steps" — sub-step decomposition within an operation block, each with independent state annotation

Five new criteria → C-40 through C-44. Pool 31 → 35. 50/35 ≈ 1.43 pts each.

---

## trace-state · Rubric v14

---

## Changes from v13 → v14

**Five new aspirational criteria extracted from R15 excellence signals:**

### C-40 — Per-pass labeled defect
**Source**: V-01 "Multi-pass design surfaces one labeled defect per domain; at minimum one carries type + triggering op + reason." C-04 requires at least one labeled defect in the artifact total. C-40 requires one per domain pass, each independently carrying type + triggering operation + reason.

Key distinctions:
- C-04 is satisfied by a single labeled defect anywhere in the artifact
- C-40 requires one per pass — a multi-pass artifact with a defect only in pass 1 does not satisfy C-40
- Each per-pass defect must independently meet the type + triggering op + reason standard
- Applies to multi-pass formats only; single-pass formats cannot satisfy C-40

### C-41 — Cross-domain precondition chain annotation
**Source**: V-01 "multi-pass surfaces cross-domain precondition chains." A postcondition in pass N is explicitly named and connected as a precondition feeding into pass N+1 — an explicit bridge annotation linking passes at the field level.

Key distinctions:
- C-02 covers preconditions + postconditions within a single operation in a single pass
- C-41 requires an explicit cross-pass bridge: a postcondition annotation in pass N that names or references the downstream pass it seeds
- Implicit flow does not satisfy C-41 — the chain must be labeled
- Applies to multi-pass formats only; single-pass formats cannot satisfy C-41

### C-42 — Domain-ordering defect-class hypothesis
**Source**: V-03 "Different defect-class hypothesis vs V-01 exposes distinct defect type — broader hypothesis signal." The domain ordering is annotated as a hypothesis about which defect class is surfaced; each pass heading names the defect class it targets given the ordering choice.

Key distinctions:
- C-36 requires a defect hypothesis at pass headings — this is satisfied by naming a defect type
- C-42 requires the *ordering* itself to be the hypothesis vehicle: the pass heading must explain why this domain comes first/next and what defect class that ordering targets
- Satisfying C-36 does not satisfy C-42 unless the annotation explicitly connects domain order to defect-class selection
- Achievable in any multi-pass format (tabular or step-block)

### C-43 — Lifecycle-phase state annotation
**Source**: V-04 "Lifecycle Emphasis." Entity lifecycle phase labels (e.g., Lead → Opportunity → Closed Won in Sales; Ticket → Escalation → Resolution in CS) appear at the state level, enriching before/after fields beyond raw attribute values.

Key distinctions:
- C-01 requires before/op/after but does not specify lifecycle-phase labeling
- C-43 requires lifecycle-phase labels to appear *within or alongside* the state fields — phase name is part of the state representation
- Raw field values alone (e.g., `amount: 0`, `status: open`) without phase labels do not satisfy C-43
- Format-neutral: satisfiable in tabular or step-block format

### C-44 — Sub-step decomposition within operation block
**Source**: V-04 "Four Sub-Steps." A single logical operation is decomposed into 3 or more sub-steps, each carrying an independent before/op/after state triple at sub-step granularity.

Key distinctions:
- Standard step-block format (C-01) documents operations at operation granularity
- C-44 requires decomposition *within* an operation: sub-steps each with their own state annotation
- Minimum threshold: 3 sub-steps per decomposed operation block; 2 sub-steps do not qualify
- Naturally aligns with step-block format; tabular formats that encode sub-rows may satisfy C-44 if each sub-row carries full state annotation

**Pool: 31 → 35 aspirationals (C-09–C-44). Aspirational point value: 50/35 ≈ 1.43 pts each.**

The scoring notes section adds entries for C-40, C-41, C-42, C-43, and C-44. Note that C-40 and C-41 are multi-pass-only criteria (single-pass formats score automatic FAIL). C-42 requires multi-pass and explicit ordering annotation. C-43 and C-44 are format-neutral.

---

## Design Rationale

**Essential (50 pts)** — the five things that make a trace-state output useful at all:
- C-01: every operation expressed as a named before/after state triple
- C-02: preconditions + postconditions per operation (not just "what happened" but "why it was allowed")
- C-03: domain-meaningful invariants named and checked (the thing a state machine analysis is hunting for)
- C-04: at least one labeled defect (the deliverable — no finding = no signal)
- C-05: domain grounding (Sales / CS / Finance vocabulary — otherwise it's a toy example)

**Recommended (not scored separately — see scoring):**
- C-06: Consistent trace format — uniform table or numbered steps throughout
- C-07: Non-trivial invariants — encode real business rules, not generic structural ones
- C-08: Race condition analysis — one concurrent interleaving with conflict or resolution named

**Aspirational (50 pts — any of 35, each ≈ 1.43 pts):**
- C-09 through C-44: see full aspirationals list below (accumulated from R1–R15 excellence signals)

---

## Scoring

- 5 essential criteria × 10 pts = **50 pts**
- 35 aspirationals (C-09–C-44): each = 50/35 ≈ **1.43 pts**, total max 50 pts
- **Total max = 100 | Golden threshold = 80**

**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

## Essential Criteria

| ID | Criterion |
|----|-----------|
| C-01 | State Transition Completeness — every operation shows starting state, operation, ending state |
| C-02 | Precondition + Postcondition per operation (explicit, even if "none") |
| C-03 | Two+ domain-meaningful invariants declared and checked after every operation |
| C-04 | At least one labeled defect: type, triggering operation, reason |
| C-05 | Domain plausibility — states/ops recognizable in Sales / CS / Finance |

**Pass condition for essentials**: all five must pass. A single essential failure disqualifies the artifact from the golden threshold regardless of composite score.

---

## Recommended Criteria

| ID | Criterion |
|----|-----------|
| C-06 | Consistent trace format — uniform table or numbered steps throughout |
| C-07 | Non-trivial invariants — encode real business rules, not generic structural ones |
| C-08 | Race condition analysis — one concurrent interleaving with conflict or resolution named |

Recommended criteria are not scored separately. They are implicit prerequisites for earning the upper aspirationals. An artifact that violates C-06 (inconsistent format) will lose aspirationals that depend on structural consistency.

---

## Aspirational Criteria

*C-09 through C-29: accumulated from R1–R13 excellence signals, carried forward. See prior rubric versions for individual definitions.*

| ID | Criterion | Format scope |
|----|-----------|-------------|
| C-09 | (R1–R13 accumulated) | — |
| … | … | — |
| C-29 | (R1–R13 accumulated) | — |
| C-30 | Criterion-instruction fusion in column headers — column headers carry `[C-XX: directive]` | Tabular only |
| C-31 | (R1–R13 accumulated) | — |
| C-32 | (R1–R13 accumulated) | — |
| C-33 | (R1–R13 accumulated) | — |
| C-34 | Disqualification-condition fusion in column headers — headers carry `FAILS if:` patterns | Tabular only |
| C-35 | (R1–R13 accumulated) | — |
| C-36 | Pass-level defect hypothesis annotation — each pass heading names the defect class it targets | Multi-pass |
| C-37 | Consequence clause at pass headings — `### Pass N [C-37: consequence clause]` | Multi-pass |
| C-38 | Step-label criterion-instruction fusion — step label carries criterion ID + behavioral directive | Step-block only |
| C-39 | Step-block disqualification-condition fusion — step label carries criterion ID + specific failure pattern | Step-block only |
| C-40 | Per-pass labeled defect — one distinct labeled defect per domain pass, each with type + triggering op + reason | Multi-pass only |
| C-41 | Cross-domain precondition chain annotation — postcondition in pass N explicitly named as precondition feeding pass N+1 | Multi-pass only |
| C-42 | Domain-ordering defect-class hypothesis — pass ordering annotated as hypothesis vehicle; each heading names the defect class targeted by the ordering choice | Multi-pass only |
| C-43 | Lifecycle-phase state annotation — entity lifecycle phase labels appear within state fields (e.g., Lead → Opportunity → Closed Won) | Format-neutral |
| C-44 | Sub-step decomposition within operation block — one operation decomposed into 3+ sub-steps each carrying independent before/op/after annotation | Format-neutral (step-block natural fit) |

**Cross-satisfaction rules:**
- C-30 and C-38 are tabular/step-block analogs — they do not cross-satisfy
- C-34 and C-39 are tabular/step-block analogs — they do not cross-satisfy
- C-38 and C-39 are orthogonal axes of the same step-block annotation — a single fused label `[C-XX: directive — FAILS if: pattern]` can satisfy both simultaneously
- C-40 and C-41 require multi-pass format — single-pass artifacts score automatic FAIL on both
- C-42 requires multi-pass format and explicit ordering annotation — satisfying C-36 alone does not satisfy C-42
- C-43 has no format restriction but the lifecycle vocabulary must be domain-recognizable (Sales / CS / Finance phases)
- C-44 minimum threshold is 3 sub-steps; 2 sub-steps do not qualify

---

## Scoring Notes

**C-30 (tabular only)**: IDs in column headers without a behavioral directive earn partial credit only. Full credit requires both criterion ID and directive in the header. Direct scorers to C-38 for the step-block equivalent.

**C-34 (tabular only)**: `FAILS if:` patterns must appear in column headers, not only in body cells. Direct scorers to C-39 for the step-block equivalent.

**C-36 (multi-pass only)**: A defect hypothesis must appear at the pass heading level — body-level hypotheses do not satisfy C-36. See C-42 for the stronger form where ordering drives the hypothesis.

**C-37 (multi-pass only)**: Consequence clause must appear in the pass heading itself, not the pass body.

**C-38 (step-block only)**: A step label carrying only a criterion ID (no directive) does not satisfy C-38. Both ID and directive must be present.

**C-39 (step-block only)**: A step label carrying only a criterion ID (no failure pattern) does not satisfy C-39. Both ID and the specific disqualifying pattern must be present.

**C-40 (multi-pass only)**: Each pass must independently carry a labeled defect. An artifact with three passes and one defect in pass 1, none in passes 2 or 3, does not satisfy C-40.

**C-41 (multi-pass only)**: The chain annotation must be explicit — a postcondition field or bridge note that names the downstream pass it seeds. Implicit flow (reader infers the chain) does not qualify.

**C-42 (multi-pass only)**: The pass heading must explain *why* the domain appears in that position in terms of defect-class targeting. A heading that names a defect type without connecting to ordering rationale satisfies C-36 but not C-42.

**C-43 (format-neutral)**: Lifecycle phase labels must be domain-recognizable. Generic labels ("state A → state B") do not satisfy C-43. Domain-specific phase vocabulary is required (Sales, CS, or Finance lifecycle terminology).

**C-44 (format-neutral, step-block natural fit)**: Sub-steps must each carry full before/op/after annotation. Narrative sub-steps without state triples do not satisfy C-44. Minimum 3 sub-steps per decomposed operation.

---

*Rubric version: v14 | Pool: 35 aspirationals (C-09–C-44) | Aspirational unit: 50/35 ≈ 1.43 pts | Essential unit: 10 pts × 5 = 50 pts | Total max: 100 | Golden threshold: 80*
