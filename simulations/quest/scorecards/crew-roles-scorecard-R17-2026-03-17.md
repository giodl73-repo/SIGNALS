# crew-roles Scorecard — Round 17 (Rubric v11)

## Differential from R16

R16 introduced C-36 (INERTIA BASELINE artifact + INERTIA ANCHOR CHECK). R17 stress-tests that mechanism under three structural risks: accidental verbatim matching (Risk-1), late detection requiring cascade revision (Risk-2), and single-file anchoring (Risk-3). All 5 variations use the R16 V-04 baseline (all 28 v11 criteria satisfied) and layer new axes on top.

---

## Scoring Framework

- **Essential** (C-01–C-05): Hard blockers. Any FAIL = disqualification.
- **Recommended** (C-06–C-08): Quality indicators.
- **Aspirational** (C-09–C-36): Formula = `aspirational_pass / 28 * 10`
  - Each full PASS = 0.357 pts. PARTIAL = 0.

---

## V-01 — Axis-D: Labeled strength terms

**S1/S2/S3 + G1/G2/G3 labels; label+phrase required verbatim at every forward-reference.**

### Essential

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | All fields present in FRAME FILL template |
| C-02 | Inertia-advocate present | PASS | "inertia-advocate is always included and written first" |
| C-03 | Correct output path | PASS | CHECK 7 verifies `.craft/roles/{domain}/` |
| C-04 | Domain specificity | PASS | LENS AUDIT checks domain-specific verify questions |
| C-05 | Minimum 3 roles | PASS | Phase 3 requires minimum 5 candidates |

**All essential PASS.**

### Recommended

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Lens actionability | PASS | LENS AUDIT item: simplify[1] concrete cut |
| C-07 | Collaborates_with resolves | PASS | LENS AUDIT item: collaborates_with inertia-advocate |
| C-08 | Perspective diversity | PASS | PERSPECTIVE AUDIT >= 3, CHECK 8 |

### Aspirational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Scope gradient | PASS | SCOPE AUDIT >= 2, CHECK 3A |
| C-10 | Inertia domain-grounded | PASS | INERTIA BASELINE requires named tool; S-labels enforce non-generic phrases ("Generic phrases do not constitute valid anchor terms") |
| C-11 | Vocabulary-forced-field | PASS | Planned-Vocab-Term column + CHECK 4B |
| C-12 | INPUT INVENTORY phase | PASS | Phase 1, min 5 rows, EXIT GATE |
| C-13 | Slot-level source citation | PASS | Per-field `Phase 1 source: {row-id} = "{verbatim phrase}"` in FRAME FILL |
| C-14 | Planning table before authoring | PASS | Phase 5 planning table with DUAL GATE precedes Phase 6 |
| C-15 | CHECK 1 input completeness | PASS | CHECK 1 present in Phase 7 |
| C-16 | CHECK 2 inertia-advocate present | PASS | CHECK 2 present |
| C-17 | CHECK 3A scope re-validation | PASS | CHECK 3A present |
| C-18 | CHECK 3B vocab binding re-validation | PASS | CHECK 3B present |
| C-19 | CHECK 4A scope post-write | PASS | CHECK 4A present |
| C-20 | CHECK 4B vocab binding post-write | PASS | CHECK 4B present |
| C-21 | CHECK 5 frame-slot match | PASS | CHECK 5A present |
| C-22 | CHECK 6 output-path verification | PASS | CHECK 6 present |
| C-23 | CHECK 7 file-count match | PASS | CHECK 7 present |
| C-24 | Re-evaluation after role replacement | PASS | ROLE-REPLACE sub-procedure with re-evaluation block |
| C-25 | Source citation in FRAME FILL output | PASS | Per-slot citations in FRAME FILL output |
| C-26 | FRAME FILL gate blocks Phase 6 | PASS | EXIT GATE: FRAME FILL COMPLETE (all fields, all citations, S-label terms in inertia-advocate lens.verify) |
| C-27 | Forensic source-phrase tracing | PASS | CHECK 5B citation verification |
| C-28 | SCOPE AUDIT gate | PASS | EXIT GATE: SCOPE AUDIT PASS + PERSPECTIVE AUDIT PASS blocks Phase 6 |
| C-29 | Gap-Addressed column in planning table | PASS | Gap/Strength column uses S/G label notation |
| C-30 | Inertia-first gate | PASS | STEP 6.1 writes inertia-advocate first |
| C-31 | Vocab binding column | PASS | Planned-Vocab-Term in planning table |
| C-32 | Inline LENS AUDIT | PASS | Per-role LENS AUDIT in STEP 6.2 (5 items) |
| C-33 | PERSPECTIVE AUDIT + CHECK 8 re-validation | PASS | Phase 5 PERSPECTIVE AUDIT + Phase 7 CHECK 8 |
| C-34 | Per-slot Phase 1 source + CHECK 5A/5B split | PASS | Per-field citations in FRAME FILL; CHECK 5A + CHECK 5B split in Phase 7 |
| C-35 | ROLE-REPLACE sub-procedure (4 fields + CONFIRMED gate) | PASS | planned/written/resolution/re-evaluation + ROLE-REPLACE CONFIRMED gate |
| C-36 | INERTIA BASELINE artifact + INERTIA ANCHOR CHECK | PASS | Phase 2 INERTIA BASELINE with name + S1-S3 + G1-G3 labels; Phase 7 INERTIA ANCHOR CHECK verifies label-prefixed verbatim match |

**V-01 Aspirational: 28/28 = 10.0**

---

## V-02 — Axis-E: Early INERTIA ANCHOR CHECK

**EARLY INERTIA ANCHOR CHECK fires in Phase 6.1 (blocking gate); Phase 7 check retained as confirmation.**

### Essential

All PASS (same base prompt structure; 5 fields, inertia-advocate first, correct path, domain specificity, min 5 candidates).

### Recommended

All PASS (LENS AUDIT items intact, PERSPECTIVE AUDIT present).

### Aspirational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Scope gradient | PASS | SCOPE AUDIT + CHECK 3A |
| C-10 | Inertia domain-grounded | PASS | INERTIA BASELINE: named tool, strengths (with "make it hard to displace"), gaps; EXIT GATE enforces COMPLETE |
| C-11 | Vocabulary-forced-field | PASS | Planned-Vocab-Term + CHECK 4B |
| C-12 | INPUT INVENTORY phase | PASS | Phase 1, min 5 rows, EXIT GATE |
| C-13 | Slot-level source citation | PASS | Per-field citations in FRAME FILL |
| C-14 | Planning table before authoring | PASS | Phase 5 precedes Phase 6 |
| C-15 | CHECK 1 | PASS | Present |
| C-16 | CHECK 2 | PASS | Present |
| C-17 | CHECK 3A | PASS | Present |
| C-18 | CHECK 3B | PASS | Present |
| C-19 | CHECK 4A | PASS | Present |
| C-20 | CHECK 4B | PASS | Present |
| C-21 | CHECK 5 | PASS | CHECK 5A present |
| C-22 | CHECK 6 | PASS | Present |
| C-23 | CHECK 7 | PASS | Present |
| C-24 | Re-evaluation after ROLE-REPLACE | PASS | Sub-procedure present |
| C-25 | Source citation in FRAME FILL output | PASS | Per-slot citations |
| C-26 | FRAME FILL gate blocks Phase 6 | PASS | EXIT GATE: FRAME FILL COMPLETE |
| C-27 | Forensic source-phrase tracing | PASS | CHECK 5B present |
| C-28 | SCOPE AUDIT gate | PASS | EXIT GATE blocks Phase 6 |
| C-29 | Gap-Addressed column | PASS | Gap/Strength column in planning table; inertia-advocate entry "must name which strength(s) it defends" |
| C-30 | Inertia-first gate | PASS | STEP 6.1 |
| C-31 | Vocab binding column | PASS | Planned-Vocab-Term column |
| C-32 | Inline LENS AUDIT | PASS | Per-role LENS AUDIT in STEP 6.2 |
| C-33 | PERSPECTIVE AUDIT + CHECK 8 | PASS | Phase 5 + Phase 7 |
| C-34 | Per-slot source + CHECK 5A/5B split | PASS | Present |
| C-35 | ROLE-REPLACE sub-procedure | PASS | 4 fields + CONFIRMED gate |
| C-36 | INERTIA BASELINE + INERTIA ANCHOR CHECK | PASS | Phase 2 artifact present (name + strengths + gaps); Phase 6.1 EARLY INERTIA ANCHOR CHECK (blocking gate); Phase 7 INERTIA ANCHOR CHECK (confirmation pass) — both check prose verbatim terms |

**V-02 Aspirational: 28/28 = 10.0**

**Note**: V-02 retains Risk-1 exposure (prose strengths without labels, so matching is heuristic). The early check (Axis-E) addresses Risk-2 structurally but not Risk-1. This is not a criterion failure under v11 — C-36 requires INERTIA BASELINE + INERTIA ANCHOR CHECK, both satisfied — but it is a gap that could surface as C-37.

---

## V-03 — Axis-F: Cross-role baseline spread

**LENS AUDIT gains 6th item; CROSS-ROLE SPREAD CHECK in Phase 7; Phase 4 requires all lens.verify to contain at least one INERTIA BASELINE term.**

### Essential

All PASS.

### Recommended

All PASS.

### Aspirational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09–C-11 | Scope gradient, Inertia domain-grounded, Vocab-forced-field | PASS | Same base mechanisms; Phase 2 strengthened with "Use specific phrases that can be quoted verbatim" |
| C-12–C-14 | INPUT INVENTORY, Slot-level citation, Planning table gate | PASS | All present with unchanged structure |
| C-15–C-23 | CHECK 1–7 | PASS | All 9 checks present |
| C-24–C-27 | ROLE-REPLACE, Source citation, FRAME FILL gate, Forensic tracing | PASS | FRAME FILL EXIT GATE now requires "all lens.verify fields contain at least one INERTIA BASELINE term" — stricter than baseline, but gate still present (C-26 PASS) |
| C-28–C-32 | SCOPE AUDIT gate, Gap-Addressed column, Inertia-first gate, Vocab binding column, Inline LENS AUDIT | PASS | LENS AUDIT has 6th item (INERTIA BASELINE term check); C-32 requires inline LENS AUDIT to exist — 6-item version still qualifies |
| C-33–C-35 | PERSPECTIVE AUDIT, Per-slot source, ROLE-REPLACE sub-procedure | PASS | All present; ROLE-REPLACE re-evaluation lists "INERTIA ANCHOR CHECK" but not CROSS-ROLE SPREAD CHECK — ROLE-REPLACE re-evaluation still has all 4 required fields + CONFIRMED gate (C-35 PASS) |
| C-36 | INERTIA BASELINE + INERTIA ANCHOR CHECK | PASS | Phase 2 artifact present; Phase 7 INERTIA ANCHOR CHECK passes; additional CROSS-ROLE SPREAD CHECK extends beyond C-36 requirements |

**V-03 Aspirational: 28/28 = 10.0**

**Note**: V-03 uniquely validates baseline influence across the registry (Axis-F), addressing Risk-3. Its ROLE-REPLACE re-evaluation does not include CROSS-ROLE SPREAD CHECK — a minor incompleteness, but not a criterion failure since C-35 checks for 4-field format + CONFIRMED gate, not CROSS-ROLE SPREAD re-evaluation coverage. Potential C-37 candidate here.

---

## V-04 — Axis-D + Axis-E: Labels + Early Check

**S-labels + EARLY INERTIA ANCHOR CHECK in Phase 6.1 (blocking, label+phrase required); Phase 7 as confirmation pass.**

### Essential

All PASS.

### Recommended

All PASS.

### Aspirational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Scope gradient | PASS | SCOPE AUDIT + CHECK 3A |
| C-10 | Inertia domain-grounded | PASS | Phase 2 INERTIA BASELINE with S-labels; "Generic phrases ('flexible', 'easy') do not constitute valid anchor terms" enforces domain specificity at authoring time |
| C-11 | Vocabulary-forced-field | PASS | Planned-Vocab-Term in planning table + CHECK 4B |
| C-12–C-14 | INPUT INVENTORY, Slot citation, Planning table gate | PASS | All present |
| C-15–C-23 | CHECK 1–7 | PASS | All 9 checks present |
| C-24–C-29 | ROLE-REPLACE, Source citation, FRAME FILL gate, Forensic tracing, SCOPE AUDIT gate, Gap-Addressed | PASS | FRAME FILL EXIT GATE: "inertia-advocate lens.verify contains at least two S-label terms verbatim"; Gap/Strength uses S/G label notation |
| C-30 | Inertia-first gate | PASS | STEP 6.1 |
| C-31 | Vocab binding column | PASS | Planned-Vocab-Term column |
| C-32 | Inline LENS AUDIT | PASS | 5-item LENS AUDIT in STEP 6.2 |
| C-33–C-35 | PERSPECTIVE AUDIT, Per-slot source, ROLE-REPLACE | PASS | All present |
| C-36 | INERTIA BASELINE + INERTIA ANCHOR CHECK | PASS | Phase 2 S/G labeled artifact (name + S1-S3 + G1-G3); Phase 6.1 EARLY INERTIA ANCHOR CHECK ("Label alone without exact phrase does not pass. Exact phrase without label does not pass."); Phase 7 INERTIA ANCHOR CHECK as confirmation pass |

**V-04 Aspirational: 28/28 = 10.0**

**Distinction**: V-04 has the most precisely specified C-36 implementation among the single/dual-axis variations: the "label alone without phrase does not pass; phrase alone without label does not pass" rule makes the check binary and auditable, eliminating both accidental-pass (Risk-1) and late-detection (Risk-2) in a single formulation. The Phase 7 check becomes a true confirmation pass, not a re-verification.

---

## V-05 — Axis-D + Axis-E + Axis-F: Full integration

**S-labels + Early check + Cross-role spread. Extends Phase 3 table with Baseline-term-in-lens column; Phase 5 table tracks baseline terms; ROLE-REPLACE re-evaluation includes CROSS-ROLE SPREAD CHECK.**

### Essential

All PASS.

### Recommended

All PASS.

### Aspirational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Scope gradient | PASS | SCOPE AUDIT + CHECK 3A |
| C-10 | Inertia domain-grounded | PASS | S-labels with "specific, quotable language. Generic phrases ('easy', 'fast') invalidate the label" — strongest domain-grounding formulation |
| C-11 | Vocabulary-forced-field | PASS | Planned-Vocab-Term + CHECK 4B |
| C-12–C-14 | INPUT INVENTORY, Slot citation, Planning table gate | PASS | All present |
| C-15–C-23 | CHECK 1–7 | PASS | All present |
| C-24 | Re-evaluation after ROLE-REPLACE | PASS | Sub-procedure present |
| C-25 | Source citation in FRAME FILL | PASS | Per-slot citations |
| C-26 | FRAME FILL gate | PASS | EXIT GATE: "inertia-advocate lens.verify has >=2 S-labels verbatim; at least one other role's lens.verify has at least one INERTIA BASELINE term verbatim" |
| C-27 | Forensic source-phrase tracing | PASS | CHECK 5B |
| C-28 | SCOPE AUDIT gate | PASS | EXIT GATE blocks Phase 6 |
| C-29 | Gap-Addressed column | PASS | Gap/Strength column with S/G label notation |
| C-30 | Inertia-first gate | PASS | STEP 6.1 |
| C-31 | Vocab binding column | PASS | Planning table includes Baseline-term-in-lens column (additive to Planned-Vocab-Term) |
| C-32 | Inline LENS AUDIT | PASS | 6-item LENS AUDIT per role in STEP 6.2 |
| C-33 | PERSPECTIVE AUDIT + CHECK 8 | PASS | Phase 5 + Phase 7 |
| C-34 | Per-slot source + CHECK 5A/5B | PASS | Present |
| C-35 | ROLE-REPLACE sub-procedure | PASS | 4 fields + CONFIRMED gate; re-evaluation now includes "INERTIA ANCHOR CHECK, and CROSS-ROLE SPREAD CHECK for this role" — most complete re-evaluation spec of all variations |
| C-36 | INERTIA BASELINE + INERTIA ANCHOR CHECK | PASS | Phase 2 S/G labeled artifact; Phase 6.1 EARLY INERTIA ANCHOR CHECK (label+phrase required); Phase 7 INERTIA ANCHOR CHECK (confirmation) + CROSS-ROLE SPREAD CHECK (Phase 7 blocking gate); EXIT GATE: ALL CHECKS PASS + INERTIA ANCHOR CHECK PASS + CROSS-ROLE SPREAD CHECK PASS |

**V-05 Aspirational: 28/28 = 10.0**

**Distinction**: V-05 is the only variation where the ROLE-REPLACE re-evaluation explicitly includes CROSS-ROLE SPREAD CHECK. It also uniquely tracks baseline-term-in-lens at Phase 3 (planning intent), Phase 4 (FRAME FILL output), Phase 5 (planning table column), Phase 6.2 (LENS AUDIT item), and Phase 7 (CROSS-ROLE SPREAD CHECK) — a 5-checkpoint chain for the Axis-F requirement, compared to V-03's 3-checkpoint chain.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 5/5 PASS | 3/3 PASS | 28/28 | **10.0** |
| V-02 | 5/5 PASS | 3/3 PASS | 28/28 | **10.0** |
| V-03 | 5/5 PASS | 3/3 PASS | 28/28 | **10.0** |
| V-04 | 5/5 PASS | 3/3 PASS | 28/28 | **10.0** |
| V-05 | 5/5 PASS | 3/3 PASS | 28/28 | **10.0** |

All 5 variations score **10.0**. This is consistent with the predicted scorer: all preserve C-36, all add hardening on top of it, none break existing criteria.

---

## Ranking (qualitative tiebreak)

All 5 tie at 10.0 on the v11 formula. Qualitative ranking by structural rigor:

1. **V-05** — Full integration: labels prevent accidental match, early check prevents cascade, cross-role spread verifies registry-wide influence; ROLE-REPLACE re-evaluation is the only one that re-runs CROSS-ROLE SPREAD CHECK.
2. **V-04** — Strongest C-36 for the inertia-advocate path: "label alone without phrase does not pass; phrase alone without label does not pass" is the most binary and auditable formulation.
3. **V-03** — Addresses Risk-3 (registry-level influence) but retains Risk-1 (prose labels, accidental matching possible); ROLE-REPLACE does not re-run CROSS-ROLE SPREAD CHECK.
4. **V-01** — Eliminates Risk-1 without early detection; Phase 7 is the only check firing point.
5. **V-02** — Eliminates Risk-2 (late detection) without label precision; prose matching retains Risk-1.

---

## Excellence Signals (from V-04 and V-05)

**Signal 1 — Label+phrase dual-requirement (Axis-D)**: The "label alone without exact phrase does not pass; exact phrase without label does not pass" rule converts the INERTIA ANCHOR CHECK from a text search into a structured audit. This closes the gap between a passing check and an anchored check. The label (S1/S2/S3) serves as a registry identifier; the phrase is the actual domain evidence. Requiring both makes the check falsifiable.

**Signal 2 — Two-pass verification with different timing (Axis-E)**: EARLY INERTIA ANCHOR CHECK in Phase 6.1 (blocking gate, immediately after writing) + Phase 7 INERTIA ANCHOR CHECK (confirmation pass after all other checks). This converts a single-point check into a temporal guarantee: compliance is verified at minimum-cost moment (one role written) and then re-confirmed at registry-complete moment. The Phase 7 check adds no new information but confirms no subsequent edit broke Phase 6.1's passing state.

**Signal 3 — 5-checkpoint baseline tracking chain (V-05)**: Axis-F in V-05 tracks the Baseline-term-in-lens requirement at Phase 3 (planning intent), Phase 4 (FRAME FILL), Phase 5 (planning table column), Phase 6.2 (LENS AUDIT item 6), and Phase 7 (CROSS-ROLE SPREAD CHECK). Each checkpoint converts an intent (stated in Phase 3) into a deliverable (verified in Phase 7). Contrast with V-03's 3-checkpoint version (Phase 4 FRAME FILL gate, Phase 6.2 LENS AUDIT item, Phase 7 CROSS-ROLE SPREAD CHECK) which skips the Phase 3 planning intent column.

---

## C-37 Candidate Patterns

These patterns appear across R17 variations but are not yet in the v11 rubric:

| Candidate | Pattern | First appears |
|-----------|---------|---------------|
| C-37a | INERTIA BASELINE uses S/G label prefixes; INERTIA ANCHOR CHECK verifies label+exact-phrase verbatim (neither alone passes) | V-01 / V-04 / V-05 |
| C-37b | EARLY INERTIA ANCHOR CHECK fires in Phase 6.1 as a blocking gate before STEP 6.2, independent from Phase 7 confirmation pass | V-02 / V-04 / V-05 |
| C-37c | CROSS-ROLE SPREAD CHECK in Phase 7 verifies at least one non-inertia-advocate role's lens.verify contains an INERTIA BASELINE term; LENS AUDIT gains baseline-term item per non-inertia-advocate role | V-03 / V-05 |

V-05 satisfies all three simultaneously. If any of these is extracted as C-37 for R18, the formula becomes `/29 * 10`.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["S-labeled anchor terms (S1/S2/S3 + exact phrase, neither alone passes) make INERTIA BASELINE verbatim propagation auditable and non-accidental across all phases", "EARLY INERTIA ANCHOR CHECK fires as blocking gate in Phase 6.1 immediately after inertia-advocate is written, with Phase 7 INERTIA ANCHOR CHECK retained as confirmation pass -- two-pass verification at minimum-cost and registry-complete moments", "CROSS-ROLE SPREAD CHECK in Phase 7 requires at least one non-inertia-advocate lens.verify to reference an INERTIA BASELINE term, with matching LENS AUDIT item per role in Phase 6.2 -- validates baseline shaped the full registry rather than only the defender role"]}
```
