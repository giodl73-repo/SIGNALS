# Scorecard — `/discover-causal` R2 Variations

**Rubric:** v2 | **Max score:** 120 | **Date:** 2026-03-17

---

## Scoring Matrix

### V-01: Compliance-audit format

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Mechanism pathway traced | **PASS** 15/15 | `X -> [step 1] -> [step 2] -> Y` required with min 2 intermediate steps; SECTION STATUS tracks step count |
| C-02 | Falsification condition present | **PASS** 15/15 | FALSIFICATION section required; SECTION STATUS confirms "at least one condition named" |
| C-03 | Inertia check performed | **PASS** 15/15 | "Do not acknowledge and defer — resolve this now"; SECTION STATUS tracks resolution |
| C-04 | AMEND section produced | **PASS** 15/15 | AMEND with 4 requirements; SECTION STATUS tracks each element |
| C-05 | Evidence cited | **PASS** 10/10 | Explicit "If no evidence exists, say so explicitly"; SECTION STATUS flags absence |
| C-06 | Confounders identified | **PASS** 10/10 | CONFOUNDERS section required and tracked in STATUS |
| C-07 | Narrowed claim more testable | **PASS** 10/10 | AMEND STATUS: `[ ] Amended version more testable than original: yes / no / unclear` |
| C-08 | Multi-step chain | **PASS** 5/5 | STATUS explicitly checks `Multi-step chain (X -> M1 -> M2 -> Y): yes / no` |
| C-09 | Effect size estimated | **FAIL** 0/5 | No quantification requirement |
| C-10 | Inertia resolved before mechanism | **PARTIAL** 3/5 | Inertia precedes mechanism in ordering; scope restriction required in CAUSAL PATHWAY; but no hard gate — model can build full-Y mechanism then note scope restriction after |
| C-11 | AMEND marginal contribution | **PASS** 5/5 | AMEND item 4 explicit; STATUS `[ ] Marginal contribution over inertia stated: yes / not applicable / missing (flag)` |
| C-12 | Falsification How-to-Observe | **PARTIAL** 3/5 | STATUS tracks "How-to-Observe specified: yes / no / partial" — but instruction only says "state what you would measure" — no WHEN TO OBSERVE required field |
| C-13 | Section compliance surfaced | **PASS** 5/5 | Every section has SECTION STATUS block; this is the primary C-13 mechanism |

**V-01 Total: 111/120** — All essential pass. All recommended pass. Aspirational: 18/30.

---

### V-02: Marginality framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Mechanism pathway traced | **PASS** 15/15 | `X -> [step 1] -> [step 2] -> {marginal scope}`, min 2 steps |
| C-02 | Falsification condition present | **PASS** 15/15 | "Vague hedges do not count"; must state what would indicate mechanism broken |
| C-03 | Inertia check performed | **PASS** 15/15 | 3-answer format (YES/PARTIAL/NO); "Do not skip or defer" |
| C-04 | AMEND section produced | **PASS** 15/15 | AMEND with marginal contribution table + side-by-side comparison |
| C-05 | Evidence cited | **PASS** 10/10 | "If none exists, say so explicitly" |
| C-06 | Confounders identified | **PASS** 10/10 | Explicit requirement in EVIDENCE AND CONFOUNDERS |
| C-07 | Narrowed claim more testable | **PASS** 10/10 | Marginal framing inherently narrows; side-by-side comparison enforces check |
| C-08 | Multi-step chain | **PASS** 5/5 | "Minimum 2 named intermediate steps" |
| C-09 | Effect size estimated | **FAIL** 0/5 | No quantification requirement |
| C-10 | Inertia resolved before mechanism | **PARTIAL** 4/5 | MARGINAL SCOPE is a required written intermediate step; "Record: 'The mechanism trace concerns: {marginal scope statement}'" — strong commitment but no explicit "may not proceed" gate |
| C-11 | AMEND marginal contribution | **PASS** 5/5 | This is V-02's primary axis; marginal contribution table is the AMEND output; all four dimensions required |
| C-12 | Falsification How-to-Observe | **PARTIAL** 3/5 | "State what you would measure/observe" (HOW) + "what result indicates broken" (WHAT) — no explicit WHEN TO OBSERVE required |
| C-13 | Section compliance surfaced | **FAIL** 0/5 | No SECTION STATUS blocks; clean prose format |

**V-02 Total: 107/120** — All essential pass. All recommended pass. Aspirational: 17/30.

---

### V-03: Falsification operationalization

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Mechanism pathway traced | **PASS** 15/15 | `X -> [step 1] -> [step 2] -> Y`, min 2 steps, "name the actual causal process" |
| C-02 | Falsification condition present | **PASS** 15/15 | Three-part structure requires specific observable outcome |
| C-03 | Inertia check performed | **PASS** 15/15 | "Do not defer. Resolve before tracing the mechanism." |
| C-04 | AMEND section produced | **PASS** 15/15 | 4 requirements; "amended version must be more specific and more falsifiable" |
| C-05 | Evidence cited | **PASS** 10/10 | "If none exists, say so explicitly" |
| C-06 | Confounders identified | **PASS** 10/10 | Explicit in CONFOUNDERS |
| C-07 | Narrowed claim more testable | **PASS** 10/10 | "The amended version must be more specific and more falsifiable than the original" — explicit requirement |
| C-08 | Multi-step chain | **PASS** 5/5 | "Minimum 2 named intermediate steps" |
| C-09 | Effect size estimated | **FAIL** 0/5 | No quantification requirement |
| C-10 | Inertia resolved before mechanism | **PARTIAL** 3/5 | "Resolve before tracing the mechanism" — strong instruction; no scope declaration step or written commitment required |
| C-11 | AMEND marginal contribution | **PASS** 5/5 | AMEND point 4: "If inertia was Partial or Yes: states what X contributes beyond what inertia produces" |
| C-12 | Falsification How-to-Observe | **PASS** 5/5 | WHAT BREAKS IT + HOW TO OBSERVE + WHEN TO OBSERVE as required named fields; enforcement rules explicitly disqualify each hedge type |
| C-13 | Section compliance surfaced | **FAIL** 0/5 | No SECTION STATUS blocks |

**V-03 Total: 110/120** — All essential pass. All recommended pass. Aspirational: 18/30.

---

### V-04: Scope-lock ordering

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Mechanism pathway traced | **PASS** 15/15 | STEP 4 traces to declared scope, min 2 intermediate steps |
| C-02 | Falsification condition present | **PASS** 15/15 | STEP 5; "specific, observable outcome (not a hedge)" |
| C-03 | Inertia check performed | **PASS** 15/15 | STEP 2: INERTIA RESOLUTION; philosophy explicitly names this as the primary failure mode |
| C-04 | AMEND section produced | **PASS** 15/15 | STEP 7 with 4 requirements; scope-anchored |
| C-05 | Evidence cited | **PASS** 10/10 | "If none, say so explicitly" |
| C-06 | Confounders identified | **PASS** 10/10 | Explicit in STEP 6 |
| C-07 | Narrowed claim more testable | **PASS** 10/10 | Scope-anchored claim inherently narrower; AMEND requirement #4 |
| C-08 | Multi-step chain | **PASS** 5/5 | "Minimum 2 named intermediate steps" |
| C-09 | Effect size estimated | **FAIL** 0/5 | No quantification requirement |
| C-10 | Inertia resolved before mechanism | **PASS** 5/5 | SCOPE DECLARATION verbatim block (Step 3) with explicit gate: "You may not proceed to Step 4 until this declaration is written"; mechanism forbidden to claim beyond declared scope |
| C-11 | AMEND marginal contribution | **PASS** 5/5 | Steps 2–3 require marginal dimension selection and restatement; AMEND requirement #4 binds it |
| C-12 | Falsification How-to-Observe | **PARTIAL** 3/5 | WHAT BREAKS IT and HOW TO OBSERVE present; WHEN TO OBSERVE in example only ("within time T") — not a required named field |
| C-13 | Section compliance surfaced | **FAIL** 0/5 | No SECTION STATUS blocks |

**V-04 Total: 108/120** — All essential pass. All recommended pass. Aspirational: 18/30.

---

### V-05: Combined aspirational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Mechanism pathway traced | **PASS** 15/15 | PHASE 4 table; "Minimum 2 rows. Single-hop tables are incomplete"; mechanism column must name actual process |
| C-02 | Falsification condition present | **PASS** 15/15 | PHASE 5 with three required parts; enforcement rules |
| C-03 | Inertia check performed | **PASS** 15/15 | PHASE 2; PHASE STATUS tracks resolution; fraction of Y required |
| C-04 | AMEND section produced | **PASS** 15/15 | PHASE 7 with AMEND GATE: explicit stop if hypothesis not narrowed |
| C-05 | Evidence cited | **PASS** 10/10 | PHASE 6 evidence table; "None found — mechanism is currently unvalidated" |
| C-06 | Confounders identified | **PASS** 10/10 | Explicit in PHASE 6; tracked in PHASE STATUS |
| C-07 | Narrowed claim more testable | **PASS** 10/10 | AMEND GATE blocks progression; STATUS `[ ] Amended version more testable than original` |
| C-08 | Multi-step chain | **PASS** 5/5 | Phase 4 table min 2 rows; STATUS tracks `Multi-step chain: yes / no` |
| C-09 | Effect size estimated | **FAIL** 0/5 | No quantification requirement |
| C-10 | Inertia resolved before mechanism | **PASS** 5/5 | PHASE 3 SCOPE DECLARATION verbatim block; PHASE STATUS `[ ] Scope declaration written`; PHASE 4 STATUS `[ ] Trace respects declared scope: yes / no` |
| C-11 | AMEND marginal contribution | **PASS** 5/5 | Marginal contribution table required in PHASE 7; PHASE STATUS `[ ] Marginal contribution table complete: yes / not applicable / missing (flag)`; PHASE 2 requires dimension identification |
| C-12 | Falsification How-to-Observe | **PASS** 5/5 | PHASE 5: WHAT + HOW + WHEN as required fields; enforcement rules explicitly disqualify each hedge type; PHASE STATUS `[ ] All conditions operationalized: yes / partial / no` |
| C-13 | Section compliance surfaced | **PASS** 5/5 | Every phase has PHASE STATUS block; artifact frontmatter `section_compliance: all_complete / gaps_flagged / {list gaps}` |

**V-05 Total: 115/120** — All essential pass. All recommended pass. Aspirational: 25/30.

---

## Rankings

| Rank | Variation | Score | Aspirational |
|------|-----------|-------|-------------|
| 1 | V-05 Combined aspirational | **115/120** | 25/30 |
| 2 | V-01 Compliance-audit | **111/120** | 18/30 |
| 3 | V-03 Falsification operationalization | **110/120** | 18/30 |
| 4 | V-04 Scope-lock ordering | **108/120** | 18/30 |
| 5 | V-02 Marginality framing | **107/120** | 17/30 |

---

## Excellence Signals from V-05

**1. AMEND GATE — explicit stop/revise instruction**
V-05 places a blocking gate at the end of PHASE 7: if the amended hypothesis is not more specific and more falsifiable than the original, the model must output "AMEND GATE: Hypothesis is not narrower. Revise before writing artifact." This is structurally stronger than tracking the property in STATUS — it forces revision rather than allowing a weak AMEND through.

**2. Phase status blocks as completion certificates**
Every phase ends with a PHASE STATUS block. The instruction "A passing PHASE STATUS may not be written for a phase that was not completed" turns each status block into a truth-bearing commitment. Silent underspecification becomes structurally impossible — the model must either fill the status correctly or lie in a visible, auditable way.

**3. Three-part falsification with per-rule enforcement**
The WHAT BREAKS IT / HOW TO OBSERVE / WHEN TO OBSERVE required fields, each with an explicit rule naming the exact disqualifying pattern ("Check the data" fails, "Eventually" fails), make it structurally impossible to pass C-12 with a hedge. Prior variations either omitted WHEN or left enforcement implicit.

**4. Written SCOPE DECLARATION as a progression gate**
The verbatim scope block in PHASE 3 — combined with PHASE 4 STATUS `[ ] Trace respects declared scope: yes / no` — creates a two-point enforcement: write the scope before tracing, then verify the trace did not exceed it. V-04 introduced the gate; V-05 adds the backward check on the completed trace.

**5. Marginal contribution table as AMEND forcing function**
The four-dimension table (Speed / Reliability / Cost / Completeness) forces the model to reason about inertia contribution even when the answer is N/A. The PHASE STATUS flags "missing" as a specific state distinct from "not applicable", making it visible when the model skips C-11 rather than genuinely concluding it does not apply.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["AMEND GATE blocks artifact write until hypothesis is demonstrably narrower — forces revision rather than tracking compliance", "Phase status as completion certificate: 'a passing status may not be written for a phase that was not completed' makes the status truth-bearing", "Backward scope check on completed mechanism trace (in addition to forward gate before tracing) catches C-10 violations that slip past the declaration step"]}
```
