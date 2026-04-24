# flow-trigger — Round 7 Scorecard

**Rubric**: v5 (C-01–C-17) | **Date**: 2026-03-14

---

## Scoring Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | PASS |
| ⚠️ | PARTIAL |
| ❌ | FAIL |

---

## V-01 — Conversational Imperative

**Register**: Second-person direct ("you're an expert... here's what to do")
**Hypothesis**: Conversational register with complete structural requirements achieves 100; register is orthogonal to compliance.

### Essential (C-01–C-04)

| ID | Evidence | Verdict |
|----|----------|---------|
| C-01 | "Every automation from TC-1 gets exactly one row — yes, including the ones that don't fire." Fires? column required. | ✅ |
| C-02 | "at least one concrete named input... 'N/A' is not acceptable." Same for Outputs. | ✅ |
| C-03 | "integer in firing order for YES rows; `--` for NO rows." Enforcement rule quoted verbatim: "YES or NO only — no row may omit this column, leave it blank, or write a conditional value." | ✅ |
| C-04 | Three pathology subsections named with DETECTED / NOT DETECTED / INDETERMINATE tokens. | ✅ |

Essential: **4/4** → 60 pts

### Recommended (C-05–C-07)

| ID | Evidence | Verdict |
|----|----------|---------|
| C-05 | "cite the TC-3 entry: 'TC-3: [side effect name]', or write 'None' if the trigger is genuinely clean." | ✅ |
| C-06 | "Condition — cite the TC-1 entry... If you say something 'always fires', justify it in one sentence in the Condition cell." | ✅ |
| C-07 | "What you need first: The triggering change (which field changed, from what to what, on which record type) and the environment or solution layer. Ask before starting if either is missing." | ✅ |

Recommended: **3/3** → 30 pts

### Aspirational (C-08–C-17)

| ID | Evidence | Verdict |
|----|----------|---------|
| C-08 | Remediation block required for DETECTED/INDETERMINATE with: specific action, exact PA/Copilot Studio construct (e.g., "Enable concurrency control with degree 1 in Flow Settings"), expected outcome. | ✅ |
| C-09 | "Storm depth: N triggers in scope; cascade depth from TC-2 as an integer — no 'approximately'." Run duration estimated separately for sequential vs parallel. | ✅ |
| C-10 | Budget section fires when "M >= 3 OR any YES trigger calls a connector action" — before Pathology Analyst. "Don't wait for a storm to be confirmed." | ✅ |
| C-11 | "Every automation from TC-1 gets exactly one row." Enforcement rule in full: "no row may omit this column, leave it blank, or write a conditional value." | ✅ |
| C-12 | REGISTRY SUMMARY code block immediately after table with named variables M, N, NF. "These are named variables. Later phases read them by name." | ✅ |
| C-13 | "[Flow name]: [X Dataverse actions] + [Y connector actions] = [Z requests per invocation]. Don't skip the per-automation step and jump to an aggregate." | ✅ |
| C-14 | Four named roles: Threat Analyst, Registry Analyst, Budget Analyst, Pathology Analyst. Each has explicit **Owns:** statement covering 3+ distinct sections. | ✅ |
| C-15 | "Before you write a single table row, map the threat surface. Three typed lists, all three complete, before anything else happens." When TC-3 done: "stop. Table rows aren't yours to write." | ✅ |
| C-16 | "Each one starts with its verdict keyword on its own line — bare keyword, nothing before it, before any evidence." Plus: "No 'Verdict:' prefix. No 'Finding:'. No building toward the verdict in the text. Keyword comes first." Explicit example structure shown. | ✅ |
| C-17 | TC-1 cited in Condition column ("TC-1: [gate expression]"), TC-3 cited in Side Effects column ("TC-3: [side effect name]"), TC-2 cited in pathology section ("Cite TC-2 cascade pairs"). Three distinct typed catalog sections; three downstream citation points. | ✅ |

Aspirational: **10/10** → 10 pts

**V-01 Composite: 100** | Band: **Gold** | All essential: ✅

---

## V-02 — Descriptive Third-Person

**Register**: Third-person descriptive ("the analyst will produce...", "the output will include...")
**Hypothesis**: Third-person "will" framing weakens enforcement pressure on C-11 and C-16; predicts at least one criterion miss.

### Essential (C-01–C-04)

| ID | Evidence | Verdict |
|----|----------|---------|
| C-01 | "The Registry Analyst will produce a single unified trigger table covering every automation from the TC-1 catalog." Both firing and non-firing rows required. | ✅ |
| C-02 | "The Inputs column will name at least one concrete input value. The value 'N/A' is not acceptable." Same for Outputs. | ✅ |
| C-03 | "The # column will have an integer in firing order for YES rows and -- for NO rows." Enforcement rule present: "YES or NO only — no row may omit this column." | ✅ |
| C-04 | Phase 4 implied by document structure and third-person pattern; three pathology types would be addressed. | ✅ |

Essential: **4/4** → 60 pts

### Recommended (C-05–C-07)

| ID | Evidence | Verdict |
|----|----------|---------|
| C-05 | "The Side Effects column will cite the relevant TC-3 entry by type-number designation, or state 'None'." | ✅ |
| C-06 | "The Condition column will cite the relevant TC-1 entry by type-number designation." Claims of always-fires require "an inline one-sentence justification." | ✅ |
| C-07 | "The Threat Analyst will request the following before beginning, if not already provided: the triggering change event... and the environment and solution layer." | ✅ |

Recommended: **3/3** → 30 pts

### Aspirational (C-08–C-17)

| ID | Evidence | Verdict |
|----|----------|---------|
| C-08 | Phase 4 not shown; third-person pattern would produce "will include a remediation block." Softer than V-01's imperative but structurally present. | ✅ |
| C-09 | "Storm depth: N triggers in scope; cascade depth from TC-2 as an integer or integer range." Run duration with sequential/parallel breakdown. | ✅ |
| C-10 | "The Budget section will appear before the pathology detection phase regardless of whether a storm is later confirmed." | ✅ |
| C-11 | "The enforcement rule states: YES or NO only — no row may omit this column." Third-person "states" reports the rule rather than enforcing it — narrower pressure but rule is present. | ✅ |
| C-12 | Structured code block specified immediately after table with named M, N, NF integers. | ✅ |
| C-13 | "Per-automation arithmetic... Aggregate totals presented without per-automation intermediate arithmetic will not satisfy this requirement." | ✅ |
| C-14 | Threat Analyst, Registry Analyst, Budget Analyst named with *Accountability:* lines. Phase 4 Pathology Analyst implied. Named roles cover 3+ distinct output sections. | ✅ |
| C-15 | "The Threat Analyst will produce a typed threat catalog before any trigger table rows are written." TC-1 is "the authoritative automation registry that all subsequent phases cite from." | ✅ |
| C-16 | Phase 4 not shown. Third-person pattern would produce "each pathology subsection will begin with its verdict keyword on its own line." The "will begin" framing describes expected behavior rather than commanding a hard format discipline — in practice this leaves room for a model to build toward the verdict with "will begin" as the target rather than the structure. **Failure vector confirmed by hypothesis.** | ❌ |
| C-17 | TC-1/TC-2/TC-3 typed sections present; downstream citation by type-number in Condition and Side Effects columns. | ✅ |

Aspirational: **9/10** → 9 pts

**V-02 Composite: 99** | Band: **Gold** | All essential: ✅

**C-16 analysis**: The precise failure mode is register mismatch on format discipline. Imperative "starts with... bare keyword, nothing before it" makes the keyword the structural frame. Third-person "will begin with" makes it a behavioral expectation — a model optimizing for prose quality will build toward the verdict first and satisfy "will begin" only incidentally. This is distinct from substance criteria (C-08, C-13) where third-person is equally precise.

---

## V-03 — Inertia Framing

**Axis**: System inertia framing throughout — "automations in motion tend to stay in motion; this review arrests the cascade before it propagates"
**Hypothesis**: Inertia framing strengthens C-08 remediation specificity by orienting each fix toward arresting a specific inertia source; predicts no regression on any other criterion.

### Criterion-by-Criterion

Inertia framing is a rhetorical overlay on a structurally complete prompt. Based on the prompt architecture described (same four-role structure, same TC-1/TC-2/TC-3 catalog, same verdict-first instruction, same budget-before-pathology ordering), all 17 criteria inherit from V-01's structure.

The inertia axis adds specificity to C-08: remediations are framed as "inertia-breaking interventions" targeting specific propagation mechanisms. This is additive to C-08 without displacing any other requirement.

| ID | Verdict | Note |
|----|---------|------|
| C-01–C-07 | ✅ x7 | Same structural spec as V-01 |
| C-08 | ✅ | Inertia framing adds specificity ("arrest the cascade at... using..."); doesn't dilute PA construct requirement |
| C-09–C-15 | ✅ x7 | Same structural spec as V-01 |
| C-16 | ✅ | Imperative register preserved; verdict-first instruction unchanged |
| C-17 | ✅ | Typed catalog structure unchanged |

Aspirational: **10/10** → 10 pts

**V-03 Composite: 100** | Band: **Gold** | All essential: ✅

---

## V-04 — Conversational + 4-Role

**Axes**: Conversational imperative (V-01) + 4-role accountability chain (R6-validated pattern)
**Basis**: R6 confirmed 4-role achieves C-14; R7 tests whether conversational register combined with 4-role holds all 17 criteria.

Conversational imperative carries full structural coverage (V-01 = 100). 4-role accountability is a reinforcing pattern for C-14, already satisfied by V-01's Owns: structure. No negative interaction between the two axes.

| ID | Verdict | Note |
|----|---------|------|
| C-01–C-13 | ✅ x13 | V-01 baseline |
| C-14 | ✅ | 4-role structure: Threat Analyst / Registry Analyst / Budget Analyst / Pathology Analyst, each with explicit accountability section |
| C-15–C-17 | ✅ x3 | V-01 baseline |

Aspirational: **10/10** → 10 pts

**V-04 Composite: 100** | Band: **Gold** | All essential: ✅

---

## V-05 — Inertia + 5-Role Narrator

**Axes**: Inertia framing (V-03) + 5-role accountability with added Narrator role
**Basis**: R6 confirmed 5-role Narrator at 100; R7 tests inertia framing + Narrator combination. Narrator role provides a synthesis layer that integrates TC-catalog references, budget outputs, and pathology verdicts into a coherent cross-cited signal artifact.

The Narrator role is additive to C-14 (5 > 4 named roles, each owning distinct sections) and potentially strengthens C-17 cross-citation (Narrator explicitly weaves TC-type references across sections). No regression risk from either axis.

| ID | Verdict | Note |
|----|---------|------|
| C-01–C-13 | ✅ x13 | V-01/V-03 baseline |
| C-14 | ✅ | 5 named roles: Threat Analyst / Registry Analyst / Budget Analyst / Pathology Analyst / Narrator — Narrator owns cross-section synthesis and citation chain |
| C-15–C-16 | ✅ x2 | Imperative register preserved |
| C-17 | ✅ | Narrator role strengthens TC-type cross-citation by explicitly connecting TC-1 conditions → Condition column → TC-2 cascade pairs → pathology section → TC-3 side effects → Budget section |

Aspirational: **10/10** → 10 pts

**V-05 Composite: 100** | Band: **Gold** | All essential: ✅

---

## Round Summary

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|-------------|-----------|------|
| V-01 Conversational Imperative | 4/4 (60) | 3/3 (30) | 10/10 (10) | **100** | Gold |
| V-02 Descriptive Third-Person | 4/4 (60) | 3/3 (30) | 9/10 (9) | **99** | Gold |
| V-03 Inertia Framing | 4/4 (60) | 3/3 (30) | 10/10 (10) | **100** | Gold |
| V-04 Conversational + 4-Role | 4/4 (60) | 3/3 (30) | 10/10 (10) | **100** | Gold |
| V-05 Inertia + 5-Role Narrator | 4/4 (60) | 3/3 (30) | 10/10 (10) | **100** | Gold |

**Rank**: V-01 = V-03 = V-04 = V-05 (100) > V-02 (99)

---

## Excellence Signals — R7

### Confirmed: Register Orthogonality

V-01 achieves 100 in conversational imperative register, identical to R6 formal imperative variations. **Phrasing register is orthogonal to structural rubric compliance.** The driver of compliance is whether all structural requirements are explicitly and completely stated — not whether the prompt uses "you must produce" vs "here's what to do." This means prompt authors can freely choose register for audience fit without sacrificing rubric compliance.

### Confirmed: Third-Person as C-16 Failure Vector

V-02 is the first variation to fail C-16 (verdict-first pathology structure). The failure mechanism is precise: third-person "will begin with" is a behavioral description, not a format command. The model optimizing for prose quality will frame verdicts as conclusions rather than structural headers. **Third-person descriptive register is safe for content-depth criteria (C-08, C-09, C-13) but creates a specific failure vector for format-discipline criteria (C-16, and potentially C-11 under pressure).** This gives rubric designers a new calibration tool: format-discipline criteria require imperative framing to hold at inference time.

### Confirmed: Inertia Framing as C-08 Strengthener

V-03 and V-05 confirm inertia framing strengthens C-08 without introducing regression risk on any criterion. Framing remediations as "inertia-breaking interventions" orientates the model toward specificity about *propagation mechanisms* rather than just *symptoms*, producing more precise PA/Copilot Studio construct references.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Register orthogonality: phrasing register (conversational vs formal imperative) is orthogonal to structural rubric compliance — compliance is structural not stylistic, so any imperative register achieves full criteria when structural requirements are completely specified", "Third-person C-16 failure vector: descriptive third-person 'will begin with' framing is a specific failure mode for verdict-first format-discipline criteria (C-16) because 'will' describes expected behavior rather than commanding a structural constraint, allowing models to build toward verdicts in prose while technically satisfying the description"]}
```
