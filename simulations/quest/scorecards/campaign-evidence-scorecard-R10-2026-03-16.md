> **Note**: The prompt includes V-01 only. V-02 through V-05 were not included in this run. Scoring is performed on V-01 as the sole variation present.

---

# Quest Score — campaign-evidence (Round 10)

## V-01 — Axis: Role Sequence (Intel-first)

### Essential Criteria (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Multi-stage campaign (5 stages) | **PASS** | Five named stages executed in declared order: Intelligence Analyst → Web Evidence Collector → Hypothesis Architect → Pattern Analyst → Synthesis Director. |
| C-02 | Evidence before hypothesis | **PASS** | Stage 1 (intelligence) and Stage 2 (websearch) both complete before Stage 3 (hypothesis formation). SEQUENCING RULE governs this explicitly. |
| C-03 | Hypotheses with falsification conditions | **PASS** | Stage 3 requires each hypothesis to carry "(b) an explicit falsification condition." FALSIFICATION RULE invoked at Stage 3 with binary check. |
| C-04 | Output is self-contained | **PASS** | Stage 5 (Synthesis Director) produces a final brief with title-bearing required sections; reader-coherent without re-reading stages. |

**Essential subtotal: 4/4 → 60 pts**

---

### Recommended Criteria (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Source attribution per claim | **PASS** | ATTRIBUTION RULE declares "At least 70% of material claims in any stage must carry attribution." Binary invocation at Stages 1, 2, 4, 5. |
| C-06 | Synthesis distinguishes consensus from conflict | **PASS** | Stage 5 section 1 explicitly requires: "Do not list findings side by side; name the agreement or tension directly." |
| C-07 | Confidence levels calibrated, not uniform | **PASS** | CALIBRATION RULE includes: "Anti-uniformity guard: at least two distinct levels…A uniform distribution triggers mandatory recalibration." Invoked at Stage 4 with recalibration trigger. |

**Recommended subtotal: 3/3 → 30 pts**

---

### Aspirational Criteria (10 pts / 24 denominators)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Gaps and open questions surfaced | **PASS** | Stage 5 section 4: "What remains unknown after this campaign? Frame for follow-up pickup." |
| C-09 | Decision readiness signal included | **PASS** | Stage 5 section 5 present and required. |
| C-10 | Hypotheses declared post-evidence | **PASS** | Hypotheses finalized at Stage 3 after Stages 1+2. Rationale is encoded in Stage 3 body. |
| C-11 | Explicit calibration anti-pattern guard | **PASS** | CALIBRATION RULE body contains explicit anti-uniformity guard with recalibration trigger. |
| C-12 | Decision readiness compressed to one sentence | **PASS** | "One sentence only: state whether evidence is sufficient to proceed and, if not, name the specific gap." |
| C-13 | Named rules declared at preamble, invoked at point of use | **PASS** | GOVERNANCE PREAMBLE declares all four rules by identifier. Each stage invokes rules by name. |
| C-14 | Hypothesis reordering rationale stated | **PASS** | Stage 3 body: "a hypothesis anchored before evidence gathering is a bias, not a hypothesis." Rationale is encoded at the stage where it governs. |
| C-15 | Evidence-first sequencing formalized as named rule | **PASS** | SEQUENCING RULE is a peer-tier named rule in the preamble with `[invoked at: Stage 1–5]` inline scope. Not a structural convention — it is a citable identifier. |
| C-16 | Zero-gap rule invocation — no applicable stage untagged | **PASS** | Coverage map confirms: ATTRIBUTION (S1,2,4,5), FALSIFICATION (S3,5), CALIBRATION (S4,5), SEQUENCING (S1–5). All applicable cells have positive invocations; all non-applicable cells have N/A invocations. |
| C-17 | Coverage mapping declared prospectively | **PASS** | "Finalized before Stage 1. Cannot be modified after execution begins." Map appears before Stage 1 header. |
| C-18 | All governance rules at peer tier | **PASS** | Preamble opens: "All rules declared here are peers. No rule is primary." All four rules appear at identical structural tier. |
| C-19 | Coverage map immutability declared | **PASS** | "Cannot be modified after execution begins." Immutability is explicit, not implied. |
| C-20 | Rule scope embedded inline in rule declaration | **PASS** | Every rule carries `[invoked at: Stage N, Stage M…]` as inline annotation within the rule body — not only in the separate coverage map. |
| C-21 | Interrogative invocation at critical rules | **PASS** | Stage 1 ATTRIBUTION: "Are ≥70% of domain claims attributed…? [ Yes / No ]". Stage 3 FALSIFICATION: "Does every hypothesis carry an explicit falsification condition? [ Yes / No ]". Stage 4 CALIBRATION: "Do confidence ratings include ≥2 distinct levels? [ Yes / No ]". All three critical rules receive interrogative form. |
| C-22 | Universal binary invocation format | **PASS** | Every applicable-stage invocation uses `[ Yes / No ]` form. Non-applicable cells are governed by C-31 (separate criterion); C-22's pass condition reads "at any applicable stage" — all applicable invocations are binary. |
| C-23 | Stage-indexed invocation trail | **PASS** | Every invocation carries `[Stage N of 5]` suffix. Count is derivable by rule: ATTRIBUTION 4, FALSIFICATION 2, CALIBRATION 2, SEQUENCING 5 = 13 positive + 7 negative = 20 total. |
| C-24 | Per-stage entry and exit conditions declared | **PASS** | All five stages carry explicit entry and exit conditions. Entry/exit pairs are distinct from gate record and appear in stage body. |
| C-25 | Gate record surfaced as required output artifact | **PASS** | GATE RECORD TEMPLATE appears as a named section in the preamble. Stage 5 exit condition requires "audit table complete." Gate record is readable as a standalone artifact. |
| C-26 | Consolidated invocation audit table in final output | **FAIL** | Stage 5's five required output sections (Consensus/Conflict, Hypothesis verdicts, Calibration note, Gaps, Decision readiness) do not include a consolidated invocation audit table. The "audit table complete" in Stage 5 exit condition refers to the gate record fill, not a rule×stage audit table. No section lists rule name, stage index, invocation form, and pass/fail per invocation row. |
| C-27 | Gate record pre-templated in preamble with blank cells | **PASS** | GATE RECORD TEMPLATE section present in preamble with `[ ]` blank cells for all 5 stages × entry/exit. "*Pre-instantiated. Fill each cell as its stage completes. An unfilled cell signals a gap.*" |
| C-28 | Sequencing compliance as machine-verifiable column value | **FAIL** | Stage 3 requires `[S1]` or `[S2]` inline citation on hypotheses, but this is prose annotation, not a structured evidence table with a stage-index column as a discrete field. No evidence table exists where rows can be sorted by stage value to mechanically detect ordering violations. |
| C-29 | Governance framework extensible without static updates | **PASS** | "Adding a new peer rule propagates automatically; no static count is updated." The count (20) is shown as derivation from map cells, not stored as an independent integer. Peer-equality declaration is structural. |
| C-30 | Stage roles declared as named handoff actors | **PASS** | Each stage carries a named role identifier (Intelligence Analyst, Web Evidence Collector, Hypothesis Architect, Pattern Analyst, Synthesis Director) plus explicit `Role handoff from:` and `Role passes to: Stage N — Role Name` declarations at every stage boundary. Stage 1 handles the opening case with "(opening stage — no predecessor)". |
| C-31 | Negative invocation at non-applicable stages | **PASS** | All 7 non-applicable cells carry explicit negative invocations with "N/A — [reason]" format: FALSIFICATION at S1, S2, S4; CALIBRATION at S1, S2, S3; ATTRIBUTION at S3. Every cell in the coverage map has a corresponding invocation artifact — positive or negative. |

**Aspirational subtotal: 21/24 → 8.75 pts**

---

## Score Summary

```
composite = (4/4 × 60) + (3/3 × 30) + (21/24 × 10)
          = 60 + 30 + 8.75
          = 98.75
```

| Band | Threshold | Result |
|------|-----------|--------|
| Gold | 100 | — |
| **Silver** | **90–99** | **98.75** ✓ |
| Bronze | 80–89 | — |

All essential: **PASS**. Golden threshold met. Two aspirational fails prevent Gold.

---

## Gap Analysis

| ID | Gap | Path to Gold |
|----|-----|-------------|
| C-26 | No consolidated invocation audit table in final output | Add a sixth required section to Stage 5: "Invocation Audit Table" with columns: Rule, Stage, Invocation Form, Pass/Fail. Row count must equal coverage map cells (positive + negative). |
| C-28 | Sequencing compliance not machine-verifiable via column | Add a structured evidence table with columns: [Stage Source \| Finding \| Attribution]. Hypothesis rows include a "Grounded-in" column constrained to S1/S2 values. Sort by Stage Source to mechanically verify no H row appears before S2. |

---

## Excellence Signals (V-01)

**Signal 1 — Named role handoff converts sequencing into social obligation (C-30)**
`Role passes to: Stage 3 — Hypothesis Architect` is not a structural marker — it is an actor-to-actor transfer. An executor must read the named Evidence Collector role before the Hypothesis Architect may open, making pre-commitment visible at the handoff boundary rather than detectable only after the campaign completes. This pattern makes sequencing violations require active impersonation, not just mis-ordering.

**Signal 2 — Negative invocations complete coverage mechanically (C-31)**
Every non-applicable rule/stage cell carries an explicit "N/A — [reason]" invocation. Combined with the coverage map, the full matrix is now 100% claimed: positive invocations at applicable cells, negative invocations at non-applicable ones. A reader scanning for a rule name will find it at every stage — there is no absence to interpret. The map is checkable by counting artifacts, not by trusting structural convention.

**Signal 3 — Intel-first axis as an evidence quality property, not just a sequencing choice**
V-01's rationale for leading with intelligence (domain model built before search results) is distinct from prior orderings. It frames the axis as: websearch findings are read *through* a pre-built domain lens (Stage 1), so the lens cannot be contaminated by the data it will interpret. This is a quality claim, not just a structural one — and it's testable: does Stage 2 output reference Stage 1 concepts or introduce them independently?

---

```json
{"top_score": 98.75, "all_essential_pass": true, "new_patterns": ["Named role handoff actors at every stage boundary convert sequencing from structural ordering into explicit actor-to-actor transfer obligation — violations are visible at the handoff itself, not only at rule declaration", "Negative invocations at all non-applicable rule/stage cells complete the coverage map mechanically — distinguishing rule-forgotten absences from rule-checked-inapplicable absences without interpretation"]}
```
