## prove-websearch R4 Scorecard

**Top score: 122/122** | **All essential pass: true**

---

### Results

| V | Score | Delta | Key |
|---|-------|-------|-----|
| V-01 | **122** | +2 | Rule 7 verdict copy-forward — closes C-18 |
| V-02 | 120 | 0 | Advisory "consistent with" — C-18 still FAIL |
| V-03 | 120 | 0 | PHASE 3.5 admissibility registry — C-18 still FAIL |
| V-04 | **122** | +2 | Rule 7 + Rule 8 — closes C-18, minimal composite |
| V-05 | **122** | +2 | Rule 7 + Rule 8 + PHASE 3.5 + inertia framing — maximum coverage |

---

### The Differentiating Criterion: C-18

Under v4's stricter re-evaluation, C-18 ("Null-Attack Verdict **Propagation**") requires a structural carry-through chain — not just field presence. The advisory "Must be consistent with PHASE 3" language in R3 V-05 / V-02 / V-03 admits silent re-adjudication. Rule 7 (verdict copy-forward mandate + standalone `Verdict token:` in PHASE 3 + GATE 3 enforcement) converts C-18 from FAIL to PASS.

Math confirms: R3 V-05 = 116 (v3 base) − 2 (C-18 FAIL under v4) + 2+2+2 (C-19/20/21 PASS) = **120** ✓

---

### New Patterns (v5 Rubric Candidates)

1. **`verdict-copy-forward-binding`** (C-22) — PHASE 3 emits a standalone `Verdict token`; Rule 7 mandates verbatim copy-forward to PHASE 4; GATE 3 enforces token existence; violation consequence named at RULES level. Direct analog of C-21's PRE-COMMIT→GATE 1 mechanism applied to verdict propagation.

2. **`evidence-floor-enforcement`** (C-23) — Rule 8 minimum 2 sources per SEARCH BLOCK with mandatory supplemental search trigger. Closes thin-evidence escape that allows 1-source queries to nominally satisfy structure.

3. **`synthesis-citation-isolation`** (C-24) — PHASE 3.5 admissibility registry locks the citation set before synthesis begins. Closes new-claim injection escape that "do not introduce new claims" cannot structurally prevent.

4. **`baseline-anchored-falsification`** (C-25, V-05 only) — Status-quo inertia framing in PRE-COMMIT grounds the falsification event against a concrete baseline, sharpening Q2 from abstract contrary result to evidence of failure to outperform.

---

**Golden: V-05** (comprehensive) | **Minimal composite: V-04** | **Minimal proof: V-01**

```json
{"top_score": 122, "all_essential_pass": true, "new_patterns": ["verdict-copy-forward-binding", "evidence-floor-enforcement", "synthesis-citation-isolation"]}
```
| **30** |

C-06: GATE 1 requires Q1 present and Q2 NULL HYPOTHESIS ATTACK with distinct target. C-07: GATE 3 Balance result (BALANCED or ONE-SIDED with documented follow-up). C-08: Credibility column in every evidence table row.

---

### Aspirational Criteria (32 pts max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-09 Cross-source synthesis (5) | PASS | PASS | PASS | PASS | PASS | 4 synthesis sub-fields; Convergence requires >=2 URLs; Conflict requires >=2 URLs or documented absence |
| C-10 Query refinement trail (5) | PASS | PASS | PASS | PASS | PASS | Planned/Gap/Adjusted fields in every SEARCH BLOCK; Rule 6 mandates completion |
| C-11 Phase-gate enforcement (2) | PASS | PASS | PASS | PASS | PASS | GATE 0/1/2/3 chain with "Do not proceed" in each; V-03/V-05 add GATE 3.5; V-05 adds GATE 0.5 |
| C-12 Live-phase trail placement (2) | PASS | PASS | PASS | PASS | PASS | Refinement trail is inside PHASE 2 SEARCH BLOCK, not in synthesis |
| C-13 Named-target gate framing (2) | PASS | PASS | PASS | PASS | PASS | GATE 1: "Q2 target declaration matches the PRE-COMMIT falsification event" -- names the specific adversarial target |
| C-14 Structured synthesis sub-fields (2) | PASS | PASS | PASS | PASS | PASS | Null-Attack Verdict / Convergence / Conflict / Conclusion -- 4 labeled pre-printed fields |
| C-15 Rule-first constraint ordering (2) | PASS | PASS | PASS | PASS | PASS | RULES block (Rules 1-7 or 1-8) appears before Topic/Hypothesis fields |
| C-16 Null-attack target declaration (2) | PASS | PASS | PASS | PASS | PASS | FALSIFICATION PRE-COMMIT block names specific contrary result; GATE 1 binds Q2 target to it |
| C-17 Unconditional refinement mandate (2) | PASS | PASS | PASS | PASS | PASS | Rule 6 in RULES block: "MUST be completed for every SEARCH BLOCK -- no exceptions. Omitting or skipping this field is a Rule 3 violation." |
| **C-18** Null-attack verdict propagation (2) | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** | See detail below |
| C-19 Rules-block violation consequence (2) | PASS | PASS | PASS | PASS | PASS | Rule 6 at RULES level: "no exceptions" + "Rule 3 violation" consequence; identical in all five |
| C-20 Verdict field precedes synthesis (2) | PASS | PASS | PASS | PASS | PASS | Null-Attack Verdict is the first labeled field in PHASE 4, before Convergence |
| C-21 Pre-commit gate binding (2) | PASS | PASS | PASS | PASS | PASS | GATE 0 PRE-COMMIT block before query template; GATE 1 requires copy-forward from PRE-COMMIT |
| **Aspirational subtotal** | **32** | **28** | **28** | **32** | **32** |

---

### C-18 Detail: The Differentiating Criterion

**C-18 pass condition:** "The synthesis or conclusion section contains a required field or instruction that forces an explicit null hypothesis verdict (YES falsified / NO not falsified / INCONCLUSIVE). Verdict *propagation* ensures the adversarial result is visible at the decision point."

**Why v4 reads C-18 more strictly than v3:** Under v3, having a standalone Null-Attack Verdict field in PHASE 4 with advisory "Must be consistent with PHASE 3" scored as PASS. Under v4, with C-20 (verdict field structure) and C-21 (copy-forward binding) codified as separate criteria, C-18's "propagation" is interpreted as requiring a structural carry-through chain -- not just field presence. Advisory consistency checks can be silently violated; a copy-forward mandate cannot. Under v4, C-18 requires structural enforcement, not merely structural shape.

**V-01 / V-04 / V-05 -- C-18 PASS (2 pts):**
Rule 7 (RULES block): "The Null-Attack Verdict in PHASE 4 MUST be the verbatim copy of the 'Verdict token:' field set in PHASE 3. You may NOT independently re-assess the verdict in PHASE 4. The token travels forward unchanged. Omitting or changing the token is a Rule 3 violation."

PHASE 3 adds a standalone `Verdict token: [YES / NO / INCONCLUSIVE]` field: "Write only the single matching token. This token is the authoritative verdict. It will be copied verbatim to PHASE 4 per Rule 7. Do not change it there."

GATE 3 explicitly checks: "Verdict token is set to exactly one of YES / NO / INCONCLUSIVE."

PHASE 4 instruction: "Copy the Verdict token from PHASE 3 here verbatim -- per Rule 7. Do not re-assess."

True propagation: PHASE 3 emits a named structural artifact (token); GATE 3 enforces its existence; Rule 7 mandates verbatim copy-forward at RULES level with named violation consequence; PHASE 4 references the token by rule number. Chain is structurally unbroken. C-18 PASS.

**V-02 / V-03 -- C-18 FAIL (0 pts):**
PHASE 4 text (identical to R3 V-05): "Must be consistent with PHASE 3 null hypothesis verdict."

No `Verdict token:` field in PHASE 3. No Rule 7 copy-forward mandate. GATE 3 checks only "Null hypothesis verdict is completed (YES / NO / INCONCLUSIVE)" -- the field exists but nothing prevents a model from reaching YES in PHASE 3 and rendering INCONCLUSIVE in PHASE 4 while technically satisfying "consistent with." The advisory consistency check is not structural propagation. C-18 FAIL.

This is the same escape the R4 thesis identified: "a model can independently re-assess in PHASE 4 and produce a different verdict, technically violating 'must be consistent' without a structural stop."

---

### Score Totals

| V | Essential | Recommended | Aspirational | **Total** |
|---|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 32 | **122/122** |
| V-02 | 60 | 30 | 28 | **120/122** |
| V-03 | 60 | 30 | 28 | **120/122** |
| V-04 | 60 | 30 | 32 | **122/122** |
| V-05 | 60 | 30 | 32 | **122/122** |

---

## Variation Summaries

### V-01 (122/122) -- Minimal R4 Golden

Single addition to R3 V-05: Rule 7 + standalone Verdict token in PHASE 3 + copy-forward instruction in PHASE 4 + GATE 3 enforcement. Closes the 2-pt gap with the smallest structural change. Confirms the R4 thesis: verdict copy-forward is the one mechanism that converts C-18 from FAIL to PASS under v4's stricter reading.

**Architecture:** 7-rule RULES block. GATE 0/1/2/3 chain. One new mechanism. Zero unnecessary overhead.

**If V-01 is golden:** the prompt is at 122/122 with a single targeted fix. This is the tightest proof that the escape was specifically the PHASE 3->4 verdict chain-of-custody, not a broader structural problem.

---

### V-02 (120/122) -- Evidence Floor, C-18 Gap Remains

Rule 8 raises the source floor to minimum 2 URLs per SEARCH BLOCK with a supplemental search trigger for under-threshold queries. GATE 2 enforces the floor. This closes a thin-evidence escape not captured by any v4 criterion -- Convergence requires "at least two sources" but nothing in R3 V-05 guaranteed 2 per SEARCH BLOCK.

**C-18 FAIL:** Advisory "Must be consistent with PHASE 3" retained. The evidence floor improvement does not address the verdict chain-of-custody gap.

**Score ceiling under v4:** 120/122. The evidence floor is a genuine structural advance for C-23 territory (not yet in rubric).

---

### V-03 (120/122) -- Citation Pre-Audit, C-18 Gap Remains

PHASE 3.5 CITATION PRE-AUDIT inserts an admissibility registry between PHASE 3 and PHASE 4. Every URL cited in Convergence/Conflict must appear in the registry. Registry is built from PHASE 2 evidence tables -- no new URLs allowed. GATE 3.5 locks the registry before synthesis begins.

This closes the new-claim-injection escape: a model writing Convergence can cite a URL it read during search but did not log in PHASE 2 tables. "Do not introduce new claims" is advisory; the admissibility registry is structural.

**C-18 FAIL:** Advisory "Must be consistent with PHASE 3" retained. The citation audit does not address the verdict chain-of-custody gap.

**Score ceiling under v4:** 120/122. The admissibility registry is a genuine structural advance for C-24 territory (not yet in rubric).

---

### V-04 (122/122) -- Minimal Composite Golden

Combines V-01 (Rule 7 verdict copy-forward) + V-02 (Rule 8 evidence floor). 8-rule RULES block. GATE 0/1/2/3 chain. Two targeted additions to R3 V-05.

Closes both the 2-pt C-18 gap (verdict chain-of-custody) and the thin-evidence escape (evidence floor). V-04 achieves 122/122 while closing two structural escapes without the citation audit overhead of V-03/V-05.

**If V-04 is golden:** the prompt is at 122/122 with two independent structural fixes. Recommended production golden if citation admissibility is deferred to a separate rubric cycle.

---

### V-05 (122/122) -- Maximum Structural Coverage

Combines V-04 (Rule 7 + Rule 8) + V-03 (PHASE 3.5 admissibility registry + GATE 3.5) + inertia framing in PRE-COMMIT (Status quo field + GATE 0.5). Full 6-gate lifecycle chain (GATE 0 / 0.5 / 1 / 2 / 3 / 3.5).

The inertia framing addition grounds the falsification event in a status-quo baseline: the model states "The status quo is [X], which currently achieves [Y]" before committing to the falsification event. This sharpens Q2 from "search for a contrary result" to "search for evidence that the alternative does NOT outperform the baseline." The baseline anchors adversarial commitment in a concrete performance gap rather than an abstract contrary result.

**Score under v4:** 122/122. Three additional structural mechanisms beyond 122/122 minimum -- excellence signals for v5 rubric criteria.

---

## Excellence Signals (R4 New Patterns)

### Pattern 1: `verdict-copy-forward-binding` (C-22 candidate)

**What it closes:** The PHASE 3 -> PHASE 4 verdict chain-of-custody escape. A model can reach YES in PHASE 3 and render INCONCLUSIVE in PHASE 4, technically satisfying "must be consistent with" without any structural stop.

**Mechanism:** PHASE 3 emits a standalone `Verdict token: [YES / NO / INCONCLUSIVE]` field (one word only). GATE 3 requires the token to be set. Rule 7 (RULES-level) mandates PHASE 4 copy the token verbatim. Named violation consequence: "Omitting or changing the token is a Rule 3 violation." PHASE 4 instruction: "Copy the Verdict token from PHASE 3 here verbatim -- per Rule 7. Do not re-assess."

**Analog:** This is the exact PHASE 3->4 parallel of C-21's PRE-COMMIT->GATE 1 mechanism for the falsification event. Commit a named token at phase N; gate phase N+1 on its existence; require verbatim copy-forward at phase N+2; name the violation consequence at RULES level.

**Present in:** V-01, V-04, V-05.

---

### Pattern 2: `evidence-floor-enforcement` (C-23 candidate)

**What it closes:** The thin-evidence escape. A 1-source SEARCH BLOCK satisfies the table structure but cannot support Convergence (which requires "at least two sources"). One source per query is formally compliant but epistemically weak.

**Mechanism:** Rule 8 (RULES-level) sets a minimum of 2 distinct source URLs per SEARCH BLOCK. A 1-source block triggers a mandatory supplemental search, documented inline with exact query and source. GATE 2 checks the floor before PHASE 3 proceeds. The supplemental is required, not optional.

**Present in:** V-02, V-04, V-05.

---

### Pattern 3: `synthesis-citation-isolation` (C-24 candidate)

**What it closes:** The new-claim-injection escape in synthesis. A model writing Convergence can introduce a URL it read during search but did not log in PHASE 2 tables, or fabricate a plausible-sounding URL. "Do not introduce new claims" is advisory.

**Mechanism:** PHASE 3.5 CITATION PRE-AUDIT constructs an admissibility registry from PHASE 2 evidence tables before any synthesis field is written. Every URL in Convergence/Conflict must appear in the registry. Registry is populated from PHASE 2 tables only (no new URLs allowed). GATE 3.5 locks the registry before PHASE 4. PHASE 4 instruction: "Cite only URLs in the admissibility registry."

**Present in:** V-03, V-05.

---

### Pattern 4: `baseline-anchored-falsification` (C-25 candidate, V-05 only)

**What it closes:** The abstract falsification escape. A falsification event in isolation ("evidence that X does NOT achieve Y") allows the model to identify a weak contrary result. An event anchored to a concrete baseline ("evidence that X does NOT outperform status quo Z which achieves W") requires a sharper adversarial result that cannot be satisfied by hedged qualifications.

**Mechanism:** PRE-COMMIT gains "Status quo (inertia framing):" field naming the current approach and its baseline performance. Falsification event must reference the baseline. GATE 0 checks status quo is named. GATE 0.5 checks inertia framing is complete before query design. Propagates to frontmatter as `status_quo_baseline`.

**Present in:** V-05 only.

---

## R4 Findings

**The verdict chain-of-custody escape is confirmed.** V-01 proves that Rule 7 (single addition) closes the 2-pt C-18 gap. The advisory "Must be consistent with PHASE 3" language in R3 V-05 was structurally insufficient under v4's stricter C-18 interpretation -- it admitted silent re-adjudication without a stop condition.

**Three new escapes identified beyond the closed gap:**
1. PHASE 3->4 verdict chain-of-custody -- closed by Rule 7 (C-22 candidate)
2. Thin-evidence escape (1 source per SEARCH BLOCK) -- closed by Rule 8 (C-23 candidate)
3. New-claim injection in synthesis -- closed by PHASE 3.5 admissibility registry (C-24 candidate)

**V-05 is the comprehensive golden.** It addresses all three R4 escapes plus inertia framing. At 122/122 under v4 with four additional structural mechanisms pointing toward v5 criteria, V-05 represents maximum structural coverage.

**V-04 is the minimal composite golden.** Rule 7 + Rule 8 closes the score gap and a second meaningful escape. Zero citation audit overhead. Achieves 122/122 with the smallest structural change from R3 V-05 that also closes a forward escape.

**V-01 is the minimal proof.** If a production team wants the absolute minimum change from R3 V-05, V-01 (Rule 7 only) reaches 122/122. It does not close the evidence floor or citation injection escapes, but those are not yet v4 criteria.

---

## Version History

| Round | Date | Top Score | Golden Candidate |
|-------|------|-----------|-----------------|
| R1 | 2026-03-14 | ~108-110 | V-05 (phase gates + target framing + tables) |
| R2 | 2026-03-14 | ~112-114 | V-03 (null attack + phase gates) |
| R3 | 2026-03-14 | 116/116 (v3) = 120/122 (v4) | V-04 or V-05 |
| R4 | 2026-03-14 | **122/122** | V-05 (comprehensive) or V-04 (minimal composite) |

---

```json
{"top_score": 122, "all_essential_pass": true, "new_patterns": ["verdict-copy-forward-binding", "evidence-floor-enforcement", "synthesis-citation-isolation"]}
```
