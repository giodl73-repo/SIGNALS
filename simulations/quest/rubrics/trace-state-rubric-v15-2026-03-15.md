Written to `simulations/quest/rubrics/trace-state-rubric-v15-2026-03-15.md`.

---

## trace-state · Rubric v15 — Summary

**Three R16 excellence signals → C-45, C-46, C-47. Pool 35 → 38. Unit: 50/38 ≈ 1.32 pts.**

---

### C-45 — Defect-entry state-triple decomposition *(format-neutral)*
**Source**: V-05 Signal 1. Each defect log entry decomposes into three sub-steps (Pre-Defect State / Triggering Operation / Post-Defect State+Reason), each with an independent state triple. C-44 governs operation-block sub-steps; C-45 is the orthogonal criterion governing the defect documentation site.

---

### C-46 — Phase vocabulary declaration before trace *(format-neutral)*
**Source**: V-05 Signal 2. A per-domain lifecycle phase declaration (all phases in sequence) appears *before* the trace table/block begins. C-43 requires labels in cells; C-46 requires the upfront declaration that makes completeness verifiable. The two are independent and additive — neither subsumes the other.

---

### C-47 — Defect-hypothesis confirmation annotation *(multi-pass only; requires C-40 + C-41 + C-42)*
**Source**: V-05 Signal 3. Each per-pass defect entry carries a confirmation note that names the specific defect class from the C-42 pass-heading prediction and cites the specific bridge row from the C-41 bridge table. Without this annotation, C-40 + C-41 + C-42 are satisfied independently but the self-validating circuit is not closed. Generic "as predicted" language does not qualify.

---

**V-05 rescored under v15:** 50 + (25 + 2) × 1.32 + 4 × 0.66 = 50 + 35.64 + 2.64 = **88.3** (assumes C-45 and C-46 PASS, C-47 PASS; PARTIAL weight 0.66). Ceiling gap now shifts to C-38/C-39 (step-block structurally excluded by tabular format) and the persistent C-10–C-16 block — confirming R17 axis as hybrid step-block multi-pass.
ranularity.

Key distinctions:
- C-44 covers sub-step decomposition within an operation block (the operation trace itself)
- C-45 covers sub-step decomposition within a defect log entry (the finding documentation)
- C-44 and C-45 are orthogonal: a variation can satisfy one without the other
- Each of the three sub-steps must carry an independent state triple — narrative sub-steps without state annotation do not qualify
- Format-neutral: satisfiable in tabular sub-rows or step-block sub-step blocks within the defect section

### C-46 — Phase vocabulary declaration before trace
**Source**: V-05 Signal 2 "Phase-annotated tabular state cells as C-43 native structure." A dedicated phase vocabulary declaration per domain appears before the trace table (or trace block), naming each lifecycle phase in sequence for each domain (e.g., `Finance: Draft → Pending → Approved → Posted`). This makes the `[phase: X]` labels in state cells traceable to a declared source and enables completeness verification.

Key distinctions:
- C-43 requires lifecycle-phase labels to appear within or alongside state fields but does not require an upfront declaration
- C-46 requires the declaration to appear before the trace begins, specifying all phases per domain
- Without C-46, lifecycle labels in cells are present (satisfying C-43) but their completeness and phase-arc coverage cannot be verified against a declared sequence
- Both C-43 and C-46 can be satisfied independently: C-43 without C-46 (labels in cells, no declaration), or C-46 without C-43 (declaration present but labels absent from cells); full credit requires both
- Format-neutral: tabular format uses a declaration table; step-block uses a phase legend block

### C-47 — Defect-hypothesis confirmation annotation
**Source**: V-05 Signal 3 "Ordering hypothesis + bridge table + per-pass defect form a self-validating circuit." In a multi-pass artifact satisfying C-40, C-41, and C-42, each per-pass defect entry carries an explicit confirmation note that references: (1) the defect class predicted in the pass heading (from C-42), and (2) the bridge row from C-41 that exposed the dependency chain leading to the defect. This closes the hypothesis loop within the artifact.

Key distinctions:
- C-40 requires a labeled defect per pass (type + triggering op + reason) — does not require a reference to the hypothesis
- C-42 requires a defect-class hypothesis at pass headings — does not require a per-defect confirmation
- C-41 requires a bridge annotation between passes — does not require the bridge to be referenced from the defect entry
- C-47 requires all three to be connected: the defect entry explicitly names the predicted class from C-42 and the bridge row from C-41 that surfaced the dependency
- Requires C-40, C-41, and C-42 all to be satisfied; C-47 is the synthesis confirmation layer
- Multi-pass only; single-pass formats cannot satisfy C-47
- A generic reference ("as predicted") does not satisfy C-47 — the note must name the specific class from C-42 and cite the specific bridge row or field from C-41

**Pool: 35 → 38 aspirationals (C-09–C-47). Aspirational point value: 50/38 ≈ 1.32 pts each.**

The scoring notes section adds entries for C-45, C-46, and C-47. C-45 is format-neutral. C-46 is format-neutral (declaration before trace). C-47 is multi-pass only and requires C-40 + C-41 + C-42 all satisfied.

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

**Aspirational (50 pts — any of 38, each ≈ 1.32 pts):**
- C-09 through C-47: see full aspirationals list below (accumulated from R1–R16 excellence signals)

---

## Scoring

- 5 essential criteria × 10 pts = **50 pts**
- 38 aspirationals (C-09–C-47): each = 50/38 ≈ **1.32 pts**, total max 50 pts
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
| C-45 | Defect-entry state-triple decomposition — each defect log entry decomposed into Pre-Defect State / Triggering Operation / Post-Defect State+Reason, each with independent state triple | Format-neutral |
| C-46 | Phase vocabulary declaration before trace — dedicated per-domain phase declaration (all phases in sequence) appears before the trace table/block begins | Format-neutral |
| C-47 | Defect-hypothesis confirmation annotation — each per-pass defect entry carries a confirmation note naming the predicted class from C-42 and citing the specific bridge row from C-41 | Multi-pass only |

**Cross-satisfaction rules:**
- C-30 and C-38 are tabular/step-block analogs — they do not cross-satisfy
- C-34 and C-39 are tabular/step-block analogs — they do not cross-satisfy
- C-38 and C-39 are orthogonal axes of the same step-block annotation — a single fused label `[C-XX: directive — FAILS if: pattern]` can satisfy both simultaneously
- C-40 and C-41 require multi-pass format — single-pass artifacts score automatic FAIL on both
- C-42 requires multi-pass format and explicit ordering annotation — satisfying C-36 alone does not satisfy C-42
- C-43 has no format restriction but the lifecycle vocabulary must be domain-recognizable (Sales / CS / Finance phases)
- C-44 minimum threshold is 3 sub-steps; 2 sub-steps do not qualify
- C-45 covers the defect documentation site; C-44 covers the operation trace site — they are orthogonal and can be satisfied independently or together
- C-46 does not require C-43 to be satisfied but the two work together: C-46 without C-43 means a declared vocabulary with no cell-level labels; C-43 without C-46 means labels present but completeness unverifiable
- C-47 requires C-40, C-41, and C-42 all to be satisfied as prerequisites; C-47 is the synthesis confirmation layer that closes their circuit

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

**C-45 (format-neutral)**: The three sub-steps — Pre-Defect State, Triggering Operation, Post-Defect State+Reason — must each carry an independent state triple. A defect entry that lists the three elements as flat fields without state-triple structure does not satisfy C-45. Applies to the defect log section only; operation-block sub-steps are governed by C-44.

**C-46 (format-neutral)**: The phase declaration must name every phase in the lifecycle arc for each domain, not just the phases that appear in the trace. A partial vocabulary (e.g., naming only the phases that happen to appear in the trace rows) does not satisfy C-46. Format: a table or legend block positioned before the first trace row/step.

**C-47 (multi-pass only; requires C-40 + C-41 + C-42)**: The confirmation note must be specific. "Confirmed as predicted" does not satisfy C-47. The note must name: (1) the defect class named in the C-42 pass heading annotation, and (2) the bridge row or field from the C-41 bridge table that surfaced the dependency. A C-47-satisfying note reads something like: "Confirms revenue-leak defect class (C-42 prediction: pass 2) — triggered by bridge row Finance.Approved → Sales.Commit from C-41 bridge table."

---

*Rubric version: v15 | Pool: 38 aspirationals (C-09–C-47) | Aspirational unit: 50/38 ≈ 1.32 pts | Essential unit: 10 pts × 5 = 50 pts | Total max: 100 | Golden threshold: 80*
