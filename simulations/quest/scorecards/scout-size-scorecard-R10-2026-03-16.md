# Quest:Score — scout-size — Round 10

**Scoring note**: Only V-01 is complete. V-02 provides the two-phase framing and Phase 1 header only — charter body, Phase 2, and output compilation structure are absent. V-03–V-05 not provided. V-01 scored in full; V-02 scored on visible structure with inferences noted.

---

## V-01 — Single-Phase with Embedded Self-Test Query

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | **PASS** | Step 2 table requires individually named integration points + "Total integration points [numeric count required]" row; WRONG: "several API endpoints and some database tables" fails for no named points and no count |
| C-02 | Complexity tier on-scale | **PASS** | Column header "[choose exactly one: LOW / MEDIUM / HIGH / XL]"; prose explicitly names failing vocabulary: MODERATE, 3/5, medium-high |
| C-03 | Inertia check present | **PASS** | Step 1 dedicated table: Workaround Name, Ongoing Cost Description, Cost Direction [cheaper / comparable / more expensive], Key Driver; WRONG example fails for naming workaround without cost direction |
| C-04 | Confidence level with basis | **PASS** | Step 6 two-column table; basis column: "[name what is specifically known or verified — a bare level with no basis fails]"; WRONG: bare "Confidence: HIGH" |
| C-05 | Signal boundary respected | **PASS** | Preamble prohibits sprint assignments / owner names / task breakdowns / milestone dates; Signal Boundary Check checklist repeats constraint as final gate |

**Essential: 5/5 → 60/60**

---

### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Team-size names specialist types | **PASS** | Step 4: "Name specialist disciplines, not just headcount. '3 engineers' fails; '1 backend, 1 frontend, 0.5 PM' passes." Specialist Discipline / Fraction table enforces this |
| C-07 | Timeline as sprint range | **PASS** | Column "[N–M sprints — e.g. '3–5 sprints']"; prose: "Not a calendar date. Not a single number." |
| C-08 | Primary complexity driver | **PASS** | Step 3 column "[name 1–2 specific factors — 'it's complex' fails]" |

**Recommended: 3/3 → 30/30**

---

### Aspirational (21 criteria, 10 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Tier sensitivity up/down | PASS | Step 9 table has Direction / Single Named Falsifiable Condition / Destination Tier rows for both tier-up and tier-down |
| C-10 | Confidence calibration | PASS | Step 8 raise/lower confidence table |
| C-11 | Confidence gap named | PASS | Step 7: "Name the specific thing that is not yet known — the primary source of residual uncertainty"; column header reinforces "specific unknown" requirement |
| C-12 | Sensitivity as single named conditions | PASS | Step 9 bullets + WRONG: "Several factors could push the tier up." (list, not a single named condition) |
| C-13 | Sensitivity names explicit tier destination | PASS | Column header "[must differ from current tier — fill with LOW / MEDIUM / HIGH / XL]"; CORRECT example: "Tier rises to XL if offline sync is required" |
| C-14 | Falsifiable conditions | PASS | Step 9 requires "Falsifiable — a reader must be able to name an action that settles it"; CORRECT example: "confirm by reviewing the mobile spec with the product owner before next sprint planning" |
| C-15 | Basis/gap non-overlapping | PASS | Three-layer enforcement: (1) gap column header "[must address a dimension not covered by the Confidence Basis above]"; (2) C-28 self-test query in "Before finalizing" block; (3) WRONG: basis-negated gap / CORRECT: different-dimension gap |
| C-16 | Destination tier differs from current | PASS | Column header encodes constraint; WRONG: "Tier rises to HIGH when current tier is already HIGH" is a named instance of this exact failure |
| C-17 | Inline failure examples for C-11/C-15/C-16 | PASS | C-11/C-15 scoped: WRONG and CORRECT in Step 7 within the gap section; C-16 scoped: WRONG in Step 9 within the sensitivity section — none in a separate appendix |
| C-18 | Structural encoding for C-13/C-16 | PASS | Both C-13 (tier destination) and C-16 (destination ≠ current) encoded in same column header; C-02 tier vocabulary also in column header |
| C-19 | Examples precede output field | **FAIL** | Steps 1, 2, 6, 7: WRONG/CORRECT appear **after** table rows — model completes the field slot before encountering examples. Step 9 is C-19-compliant (examples precede the table), but C-11/C-15-scoped examples are in Step 7 post-slot, failing the minimum scope requirement |
| C-20 | Role-separated production | **FAIL** | Single-phase by design; no role separation |
| C-21 | Both WRONG and CORRECT instances | PASS | All C-17-scoped fields: Step 7 has concrete named WRONG (negation-of-basis gap) + CORRECT (different-dimension gap); Step 9 has WRONG (list / destination-equals-current) + CORRECT (XL destination for specific named condition) |
| C-22 | Relational constraints co-encoded in field label | PASS | Gap column: "[must address a dimension not covered by the Confidence Basis above]"; Destination Tier column: "[must differ from current tier — fill with LOW / MEDIUM / HIGH / XL]" — both relational constraints encoded at label level |
| C-23 | Role charters own all fields | **FAIL** | No role charters (single-phase design) |
| C-24 | Phase 2 non-access names prohibited category | **FAIL** | No Phase 2 |
| C-25 | Phase 2 self-test query | **FAIL** | No Phase 2; C-28 (single-phase analog) is satisfied instead |
| C-26 | Role ownership in column headers | **FAIL** | No role tags (single-phase) |
| C-27 | Cross-phase constraints in compilation table | **FAIL** | No compilation table (single-phase) |
| C-28 | Single-phase self-test in gap field body | **PASS** | Step 7 "Before finalizing" block: *"Could a reader derive this gap by negating something I confirmed in the basis — reversing 'X is confirmed' to 'X is not confirmed'? If yes, your gap is a negation of the basis, not a genuine gap."* Concrete, executable, distinct from the rule restatement and the WRONG/CORRECT block |
| C-29 | Phase 1 exclusion list | **FAIL** | No Phase 1 charter (single-phase) |

**Aspirational PASSes: 13/21 → 6.19/10**

---

### V-01 Composite

| Tier | Points | Earned |
|------|--------|--------|
| Essential (5/5) | 60 | 60.00 |
| Recommended (3/3) | 30 | 30.00 |
| Aspirational (13/21) | 10 | 6.19 |
| **Total** | **100** | **96.19** |

---

## V-02 — Two-Phase with Bidirectional Field Ownership (Incomplete)

Visible structure: two-phase framing ("The signal is produced in two phases by two analyst roles. Do not blend the phases. Each role produces exactly the fields in its charter.") and Phase 1 role header ("You are the Sizing Analyst."). Phase 1 charter body, Phase 2, and output compilation structure not provided.

**Visible signals:**
- Two-phase framing present → structural precondition for C-20, C-23 established in preamble
- Phase 1 role identity established → charter-separation model confirmed

**Inferred from hypothesis + rubric's C-29 citation of V-02:**
- C-20: PASS expected — two-phase framing is unambiguous
- C-29: PASS expected — rubric's C-29 definition cites V-02 as the evidence case: "V-02's Phase 1 charter names fields it does NOT produce (Confidence Gap, Confidence Calibration explicitly excluded and handed to Phase 2)"
- C-23, C-24, C-25, C-26, C-27, C-28: Cannot score without Phase 2 charter and output structure

**Composite: cannot produce.** V-02 is the C-29-demonstrating variation; scoring blocked by truncation.

---

## V-03–V-05

Not provided. Cannot score.

---

## Excellence Signals (from V-01)

**Signal 1 — C-28 pattern confirmed effective**: V-01 is the first variation to satisfy C-28. The "Before finalizing" self-test query achieves C-15 compliance through active generation-time checking — C-15 PASSes on the strength of the query alone. Single-phase designs do not need role separation to prevent basis/gap conflation; they need the self-test query embedded at the field-body level.

**Signal 2 — Pre-slot asymmetry within a single prompt**: V-01 is internally inconsistent on C-19. Step 9 places WRONG/CORRECT **before** the output table (C-19 compliant). Steps 1, 2, 6, 7 place WRONG/CORRECT **after** the output table (C-19 non-compliant). The C-19-compliant pattern already exists in V-01 — it is not applied uniformly. Mirroring Step 9's structure in all steps would bring V-01 from 96.19 to ~96.67 (adding C-19 PASS at 0.476 pts), a small numerical gain but a meaningful design improvement.

**Signal 3 — C-28 and C-19 independence**: V-01 demonstrates that C-28 and C-19 are orthogonal. A post-slot self-test query satisfies C-28 (it is within the section governing the field's production) but fails C-19 (the model fills the slot before reading the query). Moving the "Before finalizing" block and WRONG/CORRECT examples to appear **before** the table row would satisfy both simultaneously. Step 9 demonstrates this is achievable within the same prompt.

---

## Ranking (scorable variations)

| Rank | Variation | Score | All Essential |
|------|-----------|-------|---------------|
| 1 | V-01 | 96.19 | Yes |
| — | V-02 | Incomplete | — |
| — | V-03–V-05 | Not provided | — |

---

```json
{"top_score": 96, "all_essential_pass": true, "new_patterns": ["pre-slot placement satisfies both C-28 and C-19 simultaneously: moving the self-test query and WRONG/CORRECT block to appear before the output table row (Step 9 pattern) eliminates the C-19 failure while preserving C-28 compliance — V-01 demonstrates both patterns within the same prompt, Step 9 being the C-19-compliant template the other steps do not follow"]}
```
