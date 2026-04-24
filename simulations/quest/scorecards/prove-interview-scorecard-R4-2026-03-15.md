## prove-interview — Round 4 Scoring (v4 Rubric)

---

### V-01 — Axis: Role Sequence (SKEPTIC → NEUTRAL → CHAMPION)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Persona identity declared | PASS | Subject Cards require SUBJECT + SEQUENCE POSITION with role/title explicit |
| C-02 | Prior knowledge scoped | PASS | PRIOR KNOWLEDGE and BLIND SPOTS are mandatory fields in Subject Cards |
| C-03 | Answers in persona voice | PASS | VOCABULARY SIGNATURE is mandatory; answers must use it; explicit rewrite instruction if interchangeable |
| C-04 | Evidence explicitly extracted | PASS | Step 4 is a dedicated extraction phase with structured per-item format |
| C-05 | Surprising/confirming labeled | PASS | `SURPRISING (expected: [from register], got: [what actually emerged])` template embedded; register pre-populates expectations |
| C-06 | Questions probe declared concerns | PASS | "Probe the subject's declared core concern directly"; follow-ups require trigger citation |
| C-07 | Multiple distinct personas | PASS | SKEPTIC → NEUTRAL → CHAMPION mandated; three meaningfully distinct dispositions enforced |
| C-08 | Evidence signal-typed | PASS | Step 4 format: `[Signal type]` with enumerated type list |
| C-09 | Cross-interview synthesis | PASS | Step 5 requires named convergence, contradiction, cascade observation, and composite signal |
| C-10 | Simulation fidelity annotated | PASS | Step 6 explicit: name one grounded claim (with basis) + one constructed element |
| C-11 | Voice divergence acknowledged | PASS | Step 7 explicit: cite specific word/phrase contrast; generic statements ("different roles") rejected by name |
| C-12 | Follow-up origin visible | PASS | `triggered by: "[exact phrase from the subject's preceding answer]"` template embedded in body |
| C-13 | Expectation register pre-populated | PASS | Step 1 gate: "Do not begin any interview transcript until all subject rows are complete. The register is the proof." |
| C-14 | INCONCLUSIVE label used | PASS | `INCONCLUSIVE (ambiguous because: [name the ambiguity])` explicitly listed alongside SURPRISING/CONFIRMING |
| C-15 | Phase-criterion ownership explicit | PASS | Steps 1–7 labeled with single-purpose headings; each maps to one rubric concern |
| C-16 | Format templates embedded | PASS | triggered-by, SURPRISING/CONFIRMING/INCONCLUSIVE, Subject Card, Evidence Item — all in body |
| C-17 | Evidence strength-rated | PASS | `Strength: strong \| moderate \| weak` + `Rationale: [one sentence]` in Step 4 format |
| C-18 | Evidence basis declared | PASS | `Basis: verbatim \| inferred \| corroborated` in Step 4 format |
| C-19 | Subject sequence justified | PASS | Sequence Strategy section at top: SKEPTIC→NEUTRAL→CHAMPION with named rationale (surfaces objections before advocates anchor narrative) |
| C-20 | Phase completion gated | PARTIAL | Step 1 has explicit gate; Steps 2–7 lack "phase complete when:" checkpoints — transitions flow structurally but without validation conditions |

**Essential:** 5/5 → 60 pts  
**Recommended:** 3/3 → 30 pts  
**Aspirational:** 11.5/12 → 9.6 pts  
**Composite: 99.6**

All essential pass: **YES** — Golden.

---

### V-02 — Axis: Output Format (Table-Driven)

> **Note:** Prompt is truncated at "If an answer is interchangeable across" — sections covering moment labeling, evidence table structure, synthesis, fidelity note, and voice divergence are not visible. Criteria for cut-off sections are scored PARTIAL (conservative inference) unless the design hypothesis makes intent unambiguous.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Persona identity declared | PASS | Table 2 Subject Registry: Name/Role is first field |
| C-02 | Prior knowledge scoped | PASS | Table 2 includes Prior Knowledge and Blind Spots fields |
| C-03 | Answers in persona voice | PARTIAL | Vocabulary Signature in Table 2, instruction to use it in transcript — answer-writing section truncated before enforcement rule |
| C-04 | Evidence explicitly extracted | PASS | Hypothesis explicitly designs for a structured evidence table; dedicated extraction artifact is the design goal |
| C-05 | Surprising/confirming labeled | PARTIAL | Table 1 pre-populates expectations structurally (C-13 satisfied); SURPRISING/CONFIRMING label templates not visible in truncated portion |
| C-06 | Questions probe declared concerns | PASS | "Q1: Probe the subject's Core Concern" explicit; triggered-by format shown |
| C-07 | Multiple distinct personas | PASS | SKEPTIC/NEUTRAL/CHAMPION dispositions in Table 2 |
| C-08 | Evidence signal-typed | PASS | Central design hypothesis: evidence table with signal type column |
| C-09 | Cross-interview synthesis | PARTIAL | Cut off — likely present; not verifiable |
| C-10 | Simulation fidelity annotated | PARTIAL | Cut off — not verifiable |
| C-11 | Voice divergence acknowledged | PARTIAL | Cut off — not verifiable |
| C-12 | Follow-up origin visible | PASS | `triggered by: "[exact phrase]"` format shown in transcript section |
| C-13 | Expectation register pre-populated | PASS | Table 1 gate: "do not proceed to interviews until this table has one complete row per subject. 'Complete' means all six columns filled with non-placeholder content." |
| C-14 | INCONCLUSIVE label | PARTIAL | Cut off — not verifiable |
| C-15 | Phase-criterion ownership explicit | PASS | Numbered tables with labeled purposes; each table maps to a single distinct rubric concern |
| C-16 | Format templates embedded | PARTIAL | triggered-by template visible; evidence table template implied by hypothesis but not shown |
| C-17 | Evidence strength-rated | PASS | Hypothesis explicitly targets via strength column; "strong / moderate / weak" named in rubric text |
| C-18 | Evidence basis declared | PASS | Hypothesis explicitly targets via basis column; "verbatim / inferred / corroborated" named in rubric text |
| C-19 | Subject sequence justified | PASS | Table 2 "Interview Order: [N of M — justify the position]" requires justification, not just position |
| C-20 | Phase completion gated | PASS | Table 1 explicit gate with definition of "complete"; Table 2 order justification enforces entry completion |

**Essential:** 4/5 (C-03: 0.5, C-05: 0.5) → 48 pts  
**Recommended:** 3/3 → 30 pts  
**Aspirational:** 9/12 (4 PARTIALs × 0.5) → 7.5 pts  
**Composite: 85.5** *(conservative — truncation penalty; full prompt likely scores higher)*

All essential pass: **YES** (PARTIALs on C-03/C-05, no FAILs) — Golden (composite ≥ 80).

---

### Rankings

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | V-01 | 99.6 | Complete, all criteria addressed, architectural gate at Step 1, cascade observation in synthesis |
| 2 | V-02 | 85.5 | Table-first design strong on C-17/C-18/C-19/C-20; penalized for truncation on C-03/C-05 and four UNKNOWN aspirationals |

---

### Excellence Signals from V-01

**What made V-01 better:**

1. **Cascade observation as synthesis subtype** — Step 5 requires naming specifically whether the skeptic's objection persisted, transformed, or was resolved by the time the champion interview closed. This is architecturally stronger than C-09's convergence/contradiction requirement — it enforces temporal tracking of objection lifecycle across the interview sequence.

2. **Vocabulary Signature as an auditable voice contract** — Naming 2–3 specific terms per subject in a mandatory field converts C-03 ("answers in persona voice") from a judgment call into a testable constraint. Any answer can be spot-checked against the declared vocabulary. V-02 has this field but V-01 enforces it more aggressively ("if an answer could belong to any of your three subjects without edits, rewrite it").

3. **Three-option moment label set** — SURPRISING / CONFIRMING / INCONCLUSIVE as an explicit triad prevents forced binary classification. V-01 is the first variation to embed all three label templates with their formats, making C-14 structurally inevitable.

---

```json
{"top_score": 99.6, "all_essential_pass": true, "new_patterns": ["cascade-observation: synthesis requires naming whether the skeptic's initial objection persisted, transformed, or was resolved by the champion interview — tracks objection lifecycle across sequence, beyond C-09 convergence/contradiction", "vocabulary-signature-contract: per-subject vocabulary signature (2-3 role-specific terms) declared before interviews converts C-03 voice fidelity from authorial judgment into an auditable per-answer constraint"]}
```
