Now I have everything needed. Let me score all five variations.

---

## quest:score — topic-retro, Round 2

**Rubric:** v2 (C-01–C-12; 5 essential / 3 recommended / 4 aspirational)
**Scoring:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/4 * 10)`
**Golden threshold:** all 5 essential pass AND composite ≥ 80

---

## V-01 — Phrasing Register: Imperative/Technical

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory complete and enumerated | PASS | Phase B produces explicit table; "Failure condition: 'No signals found' ends the retro" eliminates ghost artifacts |
| C-02 | Predicted vs actual explicitly stated | PASS | Phase C mandates both Predicted and Actual with explicit rule: "A match verdict without both sides fails" |
| C-03 | Gap signals identified | PASS | Phase D covers all WRONG/PARTIAL namespaces and empty namespaces where absence is material |
| C-04 | Echo section, exactly one finding | PASS | Phase A = dedicated Echo phase; selection procedure steps 1-5 produce exactly one; "No Echo" fallback explicit |
| C-05 | Accuracy verdict rendered | PASS | Phase E produces STRONG/ADEQUATE/WEAK verdict + "Signal accuracy for [topic]: [score]/100" statement |
| C-06 | Gaps actionable | PASS | Phase D requires exact skill name "e.g., /listen-adoption, /flow-resilience — not generic advice" and Commit impact YES/NO |
| C-07 | Per-namespace accuracy differentiated | PASS | Phase E required table has per-namespace rows with Score column |
| C-08 | AMEND scope respected | PASS | "SCOPE APPLIED: [constraint] All phases honor this constraint" before Phase A |
| C-09 | Calibration trend surfaced | PASS | Phase E "Calibration trend" block handles both prior-retro and first-retro cases |
| C-10 | Echo feeds back into signal design | PASS | Phase A Echo record mandates DESIGN CHANGE with typed options: new skill / rubric amendment / threshold / new signal type |
| C-11 | Explicit numeric formula per namespace | PASS | Phase E: "Apply this formula to every namespace: Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)"; table column labeled "[formula]" |
| C-12 | Echo before accuracy | PASS | Phase A is first phase; "LOCK PHASE A. The Echo record must not be revised after Phase B runs." Accuracy is Phase E (last) |

**essential_pass = 5, recommended_pass = 3, aspirational_pass = 4**
**Composite = (5/5 × 60) + (3/3 × 30) + (4/4 × 10) = 60 + 30 + 10 = 100**
**Band: Golden**

---

## V-02 — Output Format: Pure Table-Driven

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory complete and enumerated | PASS | Table 2 "One row per artifact found"; Coverage Summary table lists empty namespaces and total |
| C-02 | Predicted vs actual explicitly stated | PASS | Table 3 column headers require non-empty "Predicted" and "Actual" cells; "must be non-empty for every row" stated explicitly |
| C-03 | Gap signals identified | PASS | Table 5 covers missing signals and material empty namespaces |
| C-04 | Echo section, exactly one finding | PASS | Table 1 dedicated to "one post-ship finding"; locked immediately |
| C-05 | Accuracy verdict rendered | PASS | Verdict table inside Table 4: STRONG/ADEQUATE/WEAK with column |
| C-06 | Gaps actionable | PASS | Table 5 column "Skill (exact name e.g. /listen-adoption)" and "Would Have Caught"; "Changed Commit Decision? YES/NO" |
| C-07 | Per-namespace accuracy differentiated | PASS | Table 4 has per-namespace rows; score is a required column |
| C-08 | AMEND scope respected | PASS | Applied Scope table outputs before Table 1 when AMEND present |
| C-09 | Calibration trend surfaced | PASS | Table 4 Verdict sub-table has "Prior Retro Score" and "Calibration Trend" columns |
| C-10 | Echo feeds back into signal design | PASS | Table 1 "Design Change" column requires exact skill / rubric amendment + detail / threshold + value |
| C-11 | Explicit numeric formula per namespace | PASS | Table 4 column header is literally `Score: (C*100+P*50)/(C+P+W)` — formula is part of the column label; cannot produce the column without the formula being visible |
| C-12 | Echo before accuracy | PASS | Table 1 (Echo) precedes Table 4 (Accuracy) by document order; "Output only these five tables in order" and "This table is locked. Do not revise it based on findings in Table 3 or Table 4." |

**essential_pass = 5, recommended_pass = 3, aspirational_pass = 4**
**Composite = 100**
**Band: Golden**

**Excellence note — C-11 mechanism:** Embedding the formula directly in the column header (`Score: (C*100+P*50)/(C+P+W)`) is the strongest C-11 mechanism across all five variations. The model cannot populate the column without seeing the formula at the point of output production. No prose instruction can be skipped because the header IS the instruction.

---

## V-03 — Lifecycle Emphasis: Strict Phase Gates

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory complete and enumerated | PASS | Phase 1 artifact list + coverage summary; "COMMIT PHASE 1. The inventory is now fixed." |
| C-02 | Predicted vs actual explicitly stated | PASS | Phase 3: "Both Predicted and Actual must be explicitly stated for every namespace. A match verdict without both sides is a failure of this phase." |
| C-03 | Gap signals identified | PASS | Phase 4 reviews WRONG/PARTIAL + material empty namespaces |
| C-04 | Echo section, exactly one finding | PASS | Phase 2 selects "exactly one" from candidates; fallback if none |
| C-05 | Accuracy verdict rendered | PASS | Phase 5 STRONG/ADEQUATE/WEAK verdict + explicit score statement |
| C-06 | Gaps actionable | PASS | Phase 4: "exact skill name, e.g., /scout-compliance, /trace-state — not generic advice such as 'run more tests'" |
| C-07 | Per-namespace accuracy differentiated | PASS | Phase 5 required table has per-namespace rows with `Score: (C*100+P*50)/(C+P+W)` column |
| C-08 | AMEND scope respected | PASS | ">> SCOPE APPLIED: [constraint] All phases operate within this scope" stated before Phase 1 |
| C-09 | Calibration trend surfaced | PASS | Phase 5 calibration block; first-retro case produces explicit baseline statement |
| C-10 | Echo feeds back into signal design | PASS | Phase 2 Echo record mandates typed DESIGN CHANGE |
| C-11 | Explicit numeric formula per namespace | PASS | Phase 5 states formula inline; table column labeled `Score: (C*100+P*50)/(C+P+W)` |
| C-12 | Echo before accuracy | PASS | COMMIT gate after Phase 2 before Phase 3; explicit: "If Phase 3 analysis would change the Echo, note the tension but preserve the Phase 2 record." Accuracy is Phase 5. |

**essential_pass = 5, recommended_pass = 3, aspirational_pass = 4**
**Composite = 100**
**Band: Golden**

**Excellence note — C-12 mechanism:** V-03 has the strongest C-12 enforcement: the COMMIT gate at Phase 2 explicitly handles the edge case where later analysis would tempt Echo revision. "Note the tension but preserve the Phase 2 record" turns a potential failure mode into a named artifact. No other variation handles this conflict explicitly.

---

## V-04 — Role Sequence: Three-Voice Protocol

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory complete and enumerated | PASS | Role 1 (Archivist) produces Signal Registry table; "records. does not interpret, assess, or predict" ensures clean enumeration |
| C-02 | Predicted vs actual explicitly stated | PASS | Role 3 Step A: "Both Predicted and Actual must be explicitly stated. A match verdict without both sides is not acceptable." |
| C-03 | Gap signals identified | PASS | Role 3 Step B covers WRONG/PARTIAL and empty namespaces |
| C-04 | Echo section, exactly one finding | PASS | Role 2 selects "exactly one with highest decision impact" |
| C-05 | Accuracy verdict rendered | PASS | Role 3 Step D produces STRONG/ADEQUATE/WEAK verdict |
| C-06 | Gaps actionable | PASS | Step B: "Skill: [exact skill name, e.g., /listen-adoption, /flow-resilience — not generic advice]" + Would have caught |
| C-07 | Per-namespace accuracy differentiated | PASS | Step C has per-namespace accuracy table with labeled formula column |
| C-08 | AMEND scope respected | PASS | "SCOPE: [constraint] All three roles operate within this scope." |
| C-09 | Calibration trend surfaced | PASS | Step D "Calibration" block |
| C-10 | Echo feeds back into signal design | PASS | Role 2 Echo Record requires typed DESIGN CHANGE |
| C-11 | Explicit numeric formula per namespace | PASS | Step C states "Apply formula: Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)"; column labeled `Score: (C*100+P*50)/(C+P+W)` |
| C-12 | Echo before accuracy | PASS | Role 2 (Echo Finder) completes and locks Echo Record before Role 3 (Scorer) runs. Final output order: "Echo Record (Role 2) then Signal Registry (Role 1) then Step A through Step D (Role 3)." Echo Finder explicitly cannot compute accuracy; Scorer explicitly cannot revise Echo. |

**essential_pass = 5, recommended_pass = 3, aspirational_pass = 4**
**Composite = 100**
**Band: Golden**

**Excellence note — C-12 mechanism:** Role separation makes cross-contamination architecturally impossible rather than merely prohibited. The Echo Finder role is defined as unable to compute accuracy ("does not compute accuracy. does not assess gaps"). The Scorer role is defined as unable to revise the Echo. The constraint is a role contract, not a prose instruction.

---

## V-05 — Inertia Framing: Commit-Decision Anchor

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory complete and enumerated | PASS | Section 1 lists all artifacts grouped by namespace with empty namespace list and coverage tier |
| C-02 | Predicted vs actual explicitly stated | PASS | Section 2: "The signals predicted: [required, must be explicit]" and "What actually happened: [required, must be explicit]" per namespace |
| C-03 | Gap signals identified | PASS | Section 3 covers empty namespaces and WRONG/PARTIAL namespaces; tiered by commit impact |
| C-04 | Echo section, exactly one finding | PASS | Section 0 "THE THING WE DIDN'T SEE COMING" selects exactly one; three-test elimination procedure |
| C-05 | Accuracy verdict rendered | PASS | Section 2 includes STRONG/ADEQUATE/WEAK verdict statement |
| C-06 | Gaps actionable | PASS | Section 3: "Skill to run: [exact skill name — e.g., /listen-adoption, /scout-compliance — not 'gather more data']"; "Inertia check" adds a second actionability dimension |
| C-07 | Per-namespace accuracy differentiated | PASS | Section 2 accuracy table has per-namespace rows |
| C-08 | AMEND scope respected | PASS | "APPLIED SCOPE: [constraint] All sections stay within that scope." |
| C-09 | Calibration trend surfaced | PASS | Section 2 calibration block; first-retro case explicit |
| C-10 | Echo feeds back into signal design | PASS | Section 0 DESIGN CHANGE with typed options; commit-relevance framing adds urgency |
| C-11 | Explicit numeric formula per namespace | PASS | Section 2: "compute per-namespace accuracy using this formula: Score = (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)"; table column `Score: (C*100+P*50)/(C+P+W)` |
| C-12 | Echo before accuracy | PASS | Section 0 (Echo) is first; output order: Section 0 → Section 1 → Section 2 → Section 3; "This Echo entry is final. Do not revise it after Section 2 runs." |

**essential_pass = 5, recommended_pass = 3, aspirational_pass = 4**
**Composite = 100**
**Band: Golden**

**Note — C-12 mechanism:** V-05 has the weakest C-12 lock: "do not revise after Section 2 runs" permits revision between Section 0 and Section 2 (i.e., after Section 1 completes). V-01/V-03/V-04 lock immediately after Echo is produced. This is not a criterion failure but a robustness gap in adversarial execution.

**Excellence note — C-06 mechanism:** V-05 uniquely adds an "Inertia check" column to gap analysis: "Given actual team capacity at commit time, was skipping this signal reasonable?" This adds a practical actionability dimension absent in all other variations — gaps are tiered by both commit impact AND feasibility.

---

## Ranking

| Rank | Variation | Score | Band | Differentiator |
|------|-----------|-------|------|----------------|
| 1 (tied) | V-01 | 100 | Golden | Imperative pass/fail conditions; LOCK gate fires immediately after Echo |
| 1 (tied) | V-02 | 100 | Golden | Formula-in-column-header is structurally unavoidable; table position enforces C-12 |
| 1 (tied) | V-03 | 100 | Golden | Hardest C-12: explicit tension-handling at COMMIT gate; phase gate at every boundary |
| 1 (tied) | V-04 | 100 | Golden | Role-as-barrier makes contamination architecturally impossible, not merely prohibited |
| 1 (tied) | V-05 | 100 | Golden | Commit-decision framing forces quantification; inertia check adds feasibility dimension to gaps |

All five variations achieve perfect scores under rubric v2. The R2 design goal — ensuring C-11 and C-12 are structurally embedded across all axis combinations — succeeded completely.

---

## Excellence Signals from R2

**Three new patterns not present in R1:**

**ES-01 — Formula-as-column-header (V-02):** Placing the formula `(C*100+P*50)/(C+P+W)` in the accuracy table's column header makes it impossible to produce the column without applying the formula. The instruction is embedded in the output structure itself, not in a preceding paragraph that can be read and then forgotten. R1's top scorers stated the formula in prose; R2-V-02 makes formula-skipping structurally equivalent to missing the column.

**ES-02 — Tension-preserving Echo lock (V-03):** The clause "If Phase 3 analysis would change the Echo, note the tension but preserve the Phase 2 record" converts a likely failure mode (retroactive Echo drift when accuracy analysis reveals new information) into a named, visible output. Without this clause, a model finding tension between Echo and accuracy verdicts has no instruction other than to silently revise. With it, the tension becomes evidence of a real discovery.

**ES-03 — Role-as-architectural-barrier (V-04):** Defining the Echo Finder role as constitutionally unable to compute accuracy ("does not compute accuracy. does not assess gaps") and the Scorer role as constitutionally unable to revise the Echo enforces C-12 at a different level than phase gates or output position. Role contracts survive across multi-turn execution contexts where phase gate language may be treated as advisory.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Formula-as-column-header: embedding the formula in the accuracy table column header makes C-11 structurally unavoidable — the model cannot populate the column without seeing the formula at the point of output production", "Tension-preserving Echo lock: explicit clause handling the case where later-phase analysis would change the Echo converts retroactive drift from a silent failure into a named, visible artifact", "Role-as-architectural-barrier: defining roles as constitutionally unable to perform each other's work enforces Echo-before-accuracy at the contract level, surviving contexts where phase-gate prose is treated as advisory"]}
```
