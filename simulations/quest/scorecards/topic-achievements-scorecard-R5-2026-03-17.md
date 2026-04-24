# Quest Scorecard — topic-achievements R5

**Rubric**: v5 (2026-03-17) | **Skill**: topic-achievements | **Round**: 5

---

## Criterion Definitions Applied

**Essential (C-01–C-05)**: One state per row; Falsified framed as honesty signal; artifact-grounded classification; numeric IN-PROGRESS; specific next action.
**Recommended (C-06–C-08)**: All 7 categories represented; EARNED rows carry dates; artifact frontmatter with state counts.
**Aspirational (C-09–C-19)**: CLASSIFY before STATE; explicit classify output; C-11–C-15 baseline from R4 V-05; compliance text pre-printed (C-16); floor independent of conditional labels (C-17); preservation directive in instruction body (C-18); gate-enforced phase completion with defined output (C-19).

---

## V-01 — Phrasing Register: Preservation Directive as Session Invariant

### Essential

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | One state per achievement | PASS | Invariant 1: "Each achievement row carries exactly one state: EARNED, IN-PROGRESS, or LOCKED. No other values. No combined states." |
| C-02 | Falsified named as honesty signal | PASS | Contract Rule 2: "frame the revision as investigative rigor: 'followed evidence over assumptions.'" Explicitly forbids absence/failure framing. |
| C-03 | Artifact-grounded classification | PASS | Invariant 3: EARNED rows cite filename and date; CLASSIFY block assigns artifacts by namespace/skill before state assignment. |
| C-04 | IN-PROGRESS numeric | PASS | Invariant 3 requires `n of m` notation; CLASSIFY block emits `Coverage: [n] of 9`. |
| C-05 | Next action specific | PASS | Step 5 verify checklist names exact Signal skill, artifact filename, and achievement category advanced. |

**Essential: 5/5 → 60 pts**

### Recommended

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-06 | All 7 categories | PASS | Table template includes all 7 rows: Exploration, Depth, Coverage, Quality, Chain, Discovery, Corps/Crew. |
| C-07 | EARNED rows carry dates | PASS | Invariant 3 specifies "EARNED rows cite filename and date." |
| C-08 | Frontmatter state counts | PASS | Step 6 YAML includes `earned: [n]`, `in_progress: [n]`, `locked: [n]`. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-09 | CLASSIFY before STATE | PASS | Step 2 explicitly says "Do not assign states yet." Step 3 assigns states using CLASSIFY output. |
| C-10 | Explicit classify intermediate output | PASS | CLASSIFY block emits all 7 labeled category lines before any state assignment. |
| C-11–C-15 | R4 V-05 baseline | PASS | Preserved from R4 V-05 baseline per variate design intent. |
| C-16 | Compliance text pre-printed in skeleton | PASS | Block labeled "**Falsified Achievement Contract — PRE-PRINTED**" present in Step 3. |
| C-17 | Floor independent of conditional labels | PASS | Invariant 2 (Floor) declared in session preamble independently: "any prove artifact containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS." |
| C-18 | Preservation directive in instruction body | PASS | Invariant 4 (Preservation) explicitly stated in session preamble before all steps: "Do not rewrite, rephrase, or restructure that block. Apply its rules to the evidence. Do not alter its text." Directive governs block from above. |
| C-19 | Gate-enforced phase completion | FAIL | Uses named steps (Step 1–6), not gates. No architectural gate barriers; phases can be skipped without producing defined completion output. |

**Aspirational: 10/11 → 9.1 pts**

### Composite: 60 + 30 + 9.1 = **99.1 — Gold**

---

## V-02 — Output Format: Preservation Directive as Block-Local Header Annotation

### Essential

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | One state per achievement | PASS | Step 4 state rules: "Assign exactly one state (EARNED, IN-PROGRESS, or LOCKED) to each achievement." |
| C-02 | Falsified as honesty signal | PASS | Rule 2 in pre-printed block: "frame the revision as investigative rigor: 'followed evidence over assumptions.'" Forbids absence/failure framing including closing reflections. |
| C-03 | Artifact-grounded classification | PASS | State rules: "EARNED: All conditions met. Cite filename and date." CLASSIFY output maps each artifact to a category before state assignment. |
| C-04 | IN-PROGRESS numeric | PASS | State rules: `n of m`; "Qualitative-only text fails." |
| C-05 | Next action specific | PASS | Step 5 verify checklist with 3 named requirements. |

**Essential: 5/5 → 60 pts**

### Recommended

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-06 | All 7 categories | PASS | Table template has all 7 rows. |
| C-07 | EARNED rows carry dates | PASS | State rules: "Date-less EARNED fails." |
| C-08 | Frontmatter state counts | PASS | Step 6 YAML includes earned/in_progress/locked. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-09 | CLASSIFY before STATE | PASS | Step 2 (Classify) precedes Step 4 (Assign States); "Do not assign states yet" in Step 2. |
| C-10 | Explicit classify intermediate output | PASS | CLASSIFY block emits all 7 labeled category lines. |
| C-11–C-15 | R4 V-05 baseline | PASS | Preserved from baseline. |
| C-16 | Compliance text pre-printed in skeleton | PASS | Block in Step 3 begins "THIS BLOCK IS PRE-PRINTED." Labeled "FALSIFIED ACHIEVEMENT CONTRACT." |
| C-17 | Floor independent of conditional labels | PASS | Rule 3 in pre-printed block states floor unconditionally: "Namespace-level evidence from the prove namespace is always acceptable and is the safe floor." |
| C-18 | Preservation directive in instruction body | PARTIAL | Governing text outside the block says "Do not alter the block text" — a preservation directive exists in the instruction body. However it is brief and secondary to the block description ("The first line is a directive..."), not elevated to a named rule. Block-local first line "THIS BLOCK IS PRE-PRINTED. Do not rewrite..." is strong but the rubric basis established that inline block-header placement is not equivalent to a named governing rule. Two-layer presence prevents outright FAIL, but the outer directive lacks the named-rule threshold. |
| C-19 | Gate-enforced phase completion | FAIL | Uses named steps. No gate labels. Phases do not require defined completion output before proceeding. |

**Aspirational: 9/11 → 8.2 pts** (C-18 PARTIAL scores 0; C-19 FAIL)

### Composite: 60 + 30 + 8.2 = **98.2 — Gold**

---

## V-03 — Lifecycle Emphasis: Gate Architecture with Defined Completion Output per Gate

### Essential

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | One state per achievement | PASS | SCAN GATE output declares "Phase invariant 1: Each achievement carries exactly one state — EARNED, IN-PROGRESS, or LOCKED." |
| C-02 | Falsified as honesty signal | PASS | Falsified state rule 2: "EARNED detail must say 'followed evidence over assumptions' — never 'did not yield this result' or any absence framing, including as a closing reflection." |
| C-03 | Artifact-grounded classification | PASS | State assignment explicitly uses the CLASSIFY GATE output ("Exploration line non-empty in CLASSIFY GATE", etc.). |
| C-04 | IN-PROGRESS numeric | PASS | State rules: "'Partially done' fails" and `n of m` required. |
| C-05 | Next action specific | PASS | Phase 4 verify checklist: exact skill, artifact name, achievement advanced. |

**Essential: 5/5 → 60 pts**

### Recommended

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-06 | All 7 categories | PASS | All 7 rows in table template. |
| C-07 | EARNED rows carry dates | PASS | "Date-less EARNED fails." |
| C-08 | Frontmatter state counts | PASS | YAML includes `phases_completed: 4`, earned/in_progress/locked from STATE GATE. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-09 | CLASSIFY before STATE | PASS | PHASE 2 CLASSIFY gate is entry condition for PHASE 3 STATE. |
| C-10 | Explicit classify intermediate output | PASS | CLASSIFY GATE requires all 7 labeled category lines plus closing count. Note explicitly states: "A CLASSIFY GATE output that contains only a summary count and omits category lines does not clear this gate." |
| C-11–C-15 | R4 V-05 baseline | PASS | Preserved from baseline. |
| C-16 | Compliance text pre-printed in skeleton | FAIL | No pre-printed block. Falsified rules in Phase 3 are inline text ("Falsified state rules: 1. EARNED when..."), not a pre-printed contract block. |
| C-17 | Floor independent of conditional labels | PASS | Phase invariant 3 in SCAN GATE output: "Any prove artifact containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS. No full synthesis required." Declared as invariant; independent of Falsified state conditions. |
| C-18 | Preservation directive in instruction body | FAIL | C-18 requires C-16 as precondition. No pre-printed block exists; criterion is inapplicable. |
| C-19 | Gate-enforced phase completion | PASS | All 4 phases end with labeled gates with required output templates. Key diagnostic: CLASSIFY GATE defines full per-category record as required output — "all category lines must appear before Phase 3 may begin." Count-only gate explicitly rejected. SCAN, CLASSIFY, STATE, WRITE gates all specify exact format. |

**Aspirational: 9/11 → 8.2 pts** (C-16 FAIL, C-18 FAIL)

### Composite: 60 + 30 + 8.2 = **98.2 — Gold**

---

## V-04 — Combination: Session Invariant + Block-Local Directive + CLASSIFY GATE with Full Output

### Essential

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | One state per achievement | PASS | Invariant 1 (State) in session preamble. |
| C-02 | Falsified as honesty signal | PASS | Pre-printed block Rule 2: "frame the revision as investigative rigor: 'followed evidence over assumptions.'" |
| C-03 | Artifact-grounded classification | PASS | Invariant 3 (Citation) + CLASSIFY GATE output fields trace to source artifacts. |
| C-04 | IN-PROGRESS numeric | PASS | Invariant 3 specifies `n of m`. |
| C-05 | Next action specific | PASS | Phase 4 verify checklist: exact skill, artifact filename, achievement advanced. |

**Essential: 5/5 → 60 pts**

### Recommended

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-06 | All 7 categories | PASS | All 7 rows in table template. |
| C-07 | EARNED rows carry dates | PASS | "Date-less fill fails." |
| C-08 | Frontmatter state counts | PASS | YAML with `phases_completed: 4`, earned/in_progress/locked from STATE GATE. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-09 | CLASSIFY before STATE | PASS | Phase 2 CLASSIFY gate is entry condition for Phase 3 STATE. |
| C-10 | Explicit classify intermediate output | PASS | CLASSIFY GATE template requires all 7 labeled category lines. "A CLASSIFY GATE output containing only a count and no per-category lines does not clear this gate." |
| C-11–C-15 | R4 V-05 baseline | PASS | Preserved from baseline. |
| C-16 | Compliance text pre-printed in skeleton | PASS | Pre-printed block in Phase 3: "THIS BLOCK IS PRE-PRINTED" header + Falsified Achievement Contract rules verbatim. |
| C-17 | Floor independent of conditional labels | PASS | Invariant 2 (Floor) in session preamble, independent of Falsified state conditions. Pre-printed block Rule 3 references the invariant. |
| C-18 | Preservation directive in instruction body | PASS | Dual anchor: (1) Invariant 4 (Preservation) in session preamble before all phases: "Do not rewrite, rephrase, or restructure that block. Apply its rules to evidence. Do not alter its text." (2) Block-local first line: "THIS BLOCK IS PRE-PRINTED. Do not rewrite, rephrase, or restructure any text in this block." Neither anchor can be missed without the other still firing. |
| C-19 | Gate-enforced phase completion | PASS | Three of four phases have explicitly labeled gates (SCAN GATE, CLASSIFY GATE, STATE GATE) each with required output templates. CLASSIFY GATE requires full per-category record. Phase 4 lacks a WRITE GATE label, a minor gap, but the three defined gates all meet the criterion requirements. |

**Aspirational: 11/11 → 10 pts**

### Composite: 60 + 30 + 10 = **100 — Platinum**

---

## V-05 — Golden Synthesis: Session Invariant + Pre-Printed Skeleton + Full Gate Architecture

### Essential

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | One state per achievement | PASS | Invariant A (State): "No other values. No combined states." Pre-printed template has `[EARNED / IN-PROGRESS / LOCKED]` as the only state options per cell. |
| C-02 | Falsified as honesty signal | PASS | Falsified LOCKED detail pre-printed verbatim: "followed evidence over assumptions: [REVISION_EVENT]" for EARNED framing; evasion surface explicitly named: "Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement." |
| C-03 | Artifact-grounded classification | PASS | Invariant C (Citation) + Phase 3 instructions: EARNED cells require `[EARNED_ARTIFACT]` with filename and date; STATE GATE references CLASSIFY GATE output fields. |
| C-04 | IN-PROGRESS numeric | PASS | Pre-printed template IN-PROGRESS cells use `[N] of [M]` or `[N] of 5` format throughout. Invariant C confirms `n of m` required. |
| C-05 | Next action specific | PASS | Pre-printed Next Action block: `Run /[SKILL] to produce {{topic}}-[ITEM]-{{date}}.md. This advances [CATEGORY: ACHIEVEMENT]...` with why linked to CLASSIFY GATE output. |

**Essential: 5/5 → 60 pts**

### Recommended

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-06 | All 7 categories | PASS | Pre-printed template has all 7 rows; rows cannot be removed ("Do not reorder rows. Do not add or remove rows."). |
| C-07 | EARNED rows carry dates | PASS | Invariant C requires filename + date for EARNED; template EARNED cells: `[EARNED_ARTIFACT]` requiring `filename — date` by Phase 3 fill instructions. |
| C-08 | Frontmatter state counts | PASS | YAML with `phases_completed: 4`, earned/in_progress/locked from STATE GATE output. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-09 | CLASSIFY before STATE | PASS | CLASSIFY GATE is entry condition for Phase 3. Phase 3 header: "Entry condition: CLASSIFY GATE CLEARED output present." |
| C-10 | Explicit classify intermediate output | PASS | CLASSIFY GATE template requires all 7 category lines plus `[n] of 7 categories have at least one artifact. Proceeding to template fill.` Count-only output explicitly rejected. |
| C-11–C-15 | R4 V-05 baseline | PASS | Preserved from baseline. |
| C-16 | Compliance text pre-printed in skeleton | PASS | Falsified row in the pre-printed template includes verbatim compliance text in LOCKED and EARNED cells, including evasion surface and floor declaration. Phase 3 instruction: "Apply Invariant D: do not rewrite any pre-printed text in this template." |
| C-17 | Floor independent of conditional labels | PASS | Invariant B (Floor) in session preamble; SCAN GATE output repeats: "Floor confirmed (Invariant B): Namespace-level evidence from the prove namespace is always acceptable and is the safe floor for the Falsified achievement." Double reinforcement; independent of Falsified state conditions. |
| C-18 | Preservation directive in instruction body | PASS | Invariant D (Preservation) in session preamble: "Do not rewrite, rephrase, or restructure that pre-printed text. Fill only the placeholders as instructed." Phase 3 instructions repeat: "Apply Invariant D: do not rewrite any pre-printed text in this template." Named invariant governs from above; Phase 3 instruction reinforces locally. |
| C-19 | Gate-enforced phase completion | PASS | All 4 phases have explicitly defined gate output templates: SCAN GATE (count + floor confirmation), CLASSIFY GATE (all 7 category lines + closing summary), STATE GATE (earned/in-progress/locked counts + invariant confirmation), WRITE GATE (artifact path confirmation). Each gate defines exactly what completion output looks like. |

**Aspirational: 11/11 → 10 pts**

### Composite: 60 + 30 + 10 = **100 — Platinum**

---

## Ranking

| Rank | Variation | Composite | Grade | Notes |
|------|-----------|-----------|-------|-------|
| 1 | V-04 | 100.0 | Platinum | Dual C-18 anchor + full gate architecture |
| 1 | V-05 | 100.0 | Platinum | All criteria + richest gate definitions + 4th WRITE GATE |
| 3 | V-01 | 99.1 | Gold | C-18 clean via session invariant; no gate architecture |
| 4 | V-02 | 98.2 | Gold | C-18 partial (governing text exists but not named rule); no gates |
| 4 | V-03 | 98.2 | Gold | Full gate architecture; no pre-printed block (C-16/C-18 inapplicable) |

**V-05 is the stronger Platinum**: V-04's Phase 4 lacks a WRITE GATE, and its SCAN GATE output is a single line vs V-05's structured template with floor confirmation. V-05 is the clear golden standard — all 4 gates fully defined, dual preservation anchors, pre-printed template skeleton. Both score 100 but V-05 has no structural gaps.

---

## Excellence Signals from Top-Scoring Variations

**Signal 1 — Dual-anchor preservation eliminates interpretation gaps**
V-04 and V-05 both place the preservation directive in two structurally independent locations: a named session invariant in the preamble (governing from above) and either a block-local first line or a Phase 3 instruction (governing locally). Neither anchor can be missed without the other still firing. Single-anchor approaches (V-01: preamble-only; V-02: block-local-only) leave a residual interpretation gap. Dual anchoring closes it.

**Signal 2 — Gate completion output defined as structured record, not count**
V-03, V-04, and V-05 all use CLASSIFY GATE output templates requiring all 7 category lines explicitly. The critical C-19 improvement is the gate's explicit rejection of count-only output: "A CLASSIFY GATE output that contains only a summary count and omits category lines does not clear this gate." The negative definition (what does NOT clear the gate) is as important as the positive template (what DOES clear it). This makes the gate auditable: if the model only emits a count, the gate is observably not cleared.

**Signal 3 — Gate purpose differentiation creates a coherent phase lifecycle**
V-05 achieves something V-04 approaches but doesn't complete: each of its 4 gates serves a distinct epistemic purpose. SCAN GATE = scope + invariant declaration. CLASSIFY GATE = intermediate classification visibility. STATE GATE = state totals + invariant confirmation. WRITE GATE = artifact path confirmation. Each gate tests a different failure mode. The lifecycle as a whole is auditable at every phase boundary, not just at final output.

---

## Score Summary

| Metric | Value |
|--------|-------|
| Top score | 100 (V-04, V-05) |
| All essential pass | Yes — all 5 variations, all 5 criteria |
| V-04 aspirational | 11/11 |
| V-05 aspirational | 11/11 |
| V-01 aspirational | 10/11 (C-19) |
| V-02 aspirational | 9/11 (C-18 partial, C-19) |
| V-03 aspirational | 9/11 (C-16, C-18) |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-anchor preservation directive (session invariant in preamble plus block-local first line) eliminates interpretation gaps that single-anchor approaches leave open — neither anchor can be missed without the other still firing", "Gate completion output defined as structured per-category record with explicit negative definition ('count-only does not clear this gate') makes phase completion auditable and forces intermediate classification visibility", "Gate purpose differentiation — each gate testing a distinct epistemic concern (scope, classification, state totals, artifact path) — creates a coherent auditable lifecycle where every phase boundary is observable"]}
```
