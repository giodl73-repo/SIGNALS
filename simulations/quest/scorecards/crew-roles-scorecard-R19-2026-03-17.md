## crew-roles — Quest Score R19 (rubric v13)

### Setup

**Baseline**: R18 V-05 — all 33 criteria, v13 formula `/33 * 10` (0.303 pts each)
**Axes tested**: I (Phrasing Register), J (Lifecycle Compression), K (Inertia Front-Loading)
**Key questions**: Does C-39 require "Phase 4" literally? Does C-40 back-ref chain survive step renumbering? Do prose gates score PASS or PARTIAL on C-39/C-40?

---

### Scoring Key

| Rating | Weight |
|--------|--------|
| PASS | 1.0 |
| PARTIAL | 0.5 |
| FAIL | 0.0 |

Formula: `sum(criterion_weight) / 33 * 10`

---

### C-38, C-39, C-40, C-41 — Criterion Definitions

| Criterion | Requirement | What earns PASS vs PARTIAL vs FAIL |
|-----------|-------------|-------------------------------------|
| C-38 | EARLY INERTIA ANCHOR CHECK in Phase 6.1 — explicit PASS/FAIL label, blocks Step 6.2 | PASS: label + block. PARTIAL: mechanism present, no label. FAIL: absent |
| C-39 | FRAME FILL PRE-ANCHOR CHECK in Phase 4, explicit PASS/FAIL label | PASS: Phase 4 + label. PARTIAL: mechanism present but Phase wrong OR label missing (one dimension). FAIL: mechanism present but both Phase wrong AND label missing, OR phase far off |
| C-40 | NON-GENERIC REQUIREMENT block in Phase 2 with operational def + negative list + NON-GENERIC CHECK: PASS emission + Phase 7 back-ref | PASS: all four elements, correct phase. PARTIAL: content present (def + examples + back-ref) but missing block label or emission label, or wrong phase. FAIL: absent |
| C-41 | 6th LENS AUDIT item per non-inertia role + CROSS-ROLE SPREAD CHECK in Phase 7 | PASS: both items present. PARTIAL: one present. FAIL: neither |

---

### V-01 — Axis-I: Phrasing Register (7 phases, prose gates)

**Hypothesis**: Gate authority weakens when uppercase labels convert to prose; content survives.

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01–C-05 (Essential) | PASS | All 5 fields, inertia-advocate present, `.craft/roles/{domain}/`, domain specificity, 5+ roles |
| C-06–C-08 (Recommended) | PASS | Lens actionability, collaborates_with named, perspective diversity |
| C-09 | PASS | INPUT INVENTORY table with Row-ID / Source / Excerpt, 5-row minimum, explicit exit gate |
| C-10 | PASS | "This table is the sole citation source… no field may cite the convergence summary" |
| C-11 | PASS | Phase 1 exit gate: "Do not proceed to Phase 2 until at least 5 rows are present" |
| C-12 | PASS | `S1: "{exact phrase}", S2: …, S3: …` labeled format present |
| C-13 | PASS | `G1: "{exact phrase}", G2: …, G3: …` labeled format present |
| C-14 | PASS | Candidate roster table with S/G label column; inertia-advocate assigned "defends S1 (and S2, S3)" |
| C-15 | PASS | Frame fill: all five fields with `Phase 1 source: {row-id} = "{verbatim phrase}"` per field |
| C-16 | PASS | Planning table: Role / Scope / Perspective / Planned-Vocab-Term / Gap/Strength |
| C-17 | PASS | Scope audit: "Fewer than 2 — expand or reassign, then re-count. Two or more — proceed" |
| C-18 | PASS | Perspective audit: "Fewer than 3 — add roles or reassign. Three or more — proceed" |
| C-19 | PASS | "Step 6.1 — Write the inertia-advocate first" |
| C-20 | PASS | "Emit: INERTIA-ADVOCATE WRITTEN: {path}" present in Step 6.1 |
| C-21 | PASS | LENS AUDIT block present for each remaining role with 6 check items |
| C-22 | PASS | "Is verify[1] domain-specific? Yes / No + evidence" in LENS AUDIT |
| C-23 | PASS | "Is verify[2] domain-specific? Yes / No + evidence" in LENS AUDIT |
| C-24 | PASS | "Is simplify[1] a concrete cut rule? Yes / No + evidence" in LENS AUDIT |
| C-25 | PASS | "Does Planned-Vocab-Term appear verbatim? Yes / No + location" in LENS AUDIT |
| C-26 | PASS | Phase 7 Check 1: "Emit per file: PASS or FAIL [missing field]" |
| C-27 | PASS | Check 2: orientation = "status-quo advocate" |
| C-28 | PASS | Check 3A: scope spread >= 2, emit PASS/FAIL |
| C-29 | PASS | Check 3B + ROLE-REPLACE sub-procedure fires at mismatch |
| C-30 | PASS | Check 4A: all planning table roles written |
| C-31 | PASS | Check 4B: Planned-Vocab-Terms verbatim, ROLE-REPLACE fires |
| C-32 | PASS | Check 5A: written fields match frame fill per role |
| C-33 | PASS | Check 5B: citations verifiable, emit per violation |
| C-34 | PASS | Check 6: no generic placeholders |
| C-35 | PASS | Check 7: all files at `.craft/roles/{domain}/` |
| C-36 | PASS | Check 8: perspective spread >= 3 |
| C-37 | PASS | Phase 7 INERTIA ANCHOR CHECK: "re-read… Emit: PASS or FAIL" — labeled, blocking |
| **C-38** | **PARTIAL** | Phase 6.1 re-read mechanism present and blocking ("Do not start Step 6.2 until this confirmation is complete") but no explicit "EARLY INERTIA ANCHOR CHECK: PASS/FAIL" label emitted |
| **C-39** | **PARTIAL** | Phase 4 location ✓ (correct phase); fires after inertia-advocate frame fill, before other roles ✓; blocking consequence stated ✓; but prose format — no "FRAME FILL PRE-ANCHOR CHECK: PASS/FAIL" label emitted |
| **C-40** | **PARTIAL** | Operational definition ✓; negative-example list ✓; Phase 2 location ✓; explicit back-reference "this confirmation is the non-generic check that Phase 7 will reference back to" ✓; but no "NON-GENERIC REQUIREMENT:" block label, no "NON-GENERIC CHECK: PASS" emission |
| **C-41** | **PASS** | 6th LENS AUDIT item present: "references INERTIA BASELINE term (S or G label + phrase from Phase 2)? Yes / No + which term"; Phase 7 CROSS-ROLE SPREAD CHECK present with "Emit: PASS or FAIL [N…]" |

**Criterion scores**: C-09–C-37 = 29×1.0; C-38 = 0.5; C-39 = 0.5; C-40 = 0.5; C-41 = 1.0
**Total**: 31.5 / 33 × 10 = **9.55**

---

### V-02 — Axis-J: Lifecycle Compression (4 steps, labeled gates)

**Hypothesis**: Cross-phase C-40 back-reference may break under step renumbering; FRAME FILL PRE-ANCHOR CHECK may lose blocking identity in compressed STEP 2.

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS | All fields, inertia-advocate, correct path, domain specificity, 5+ roles |
| C-06–C-08 | PASS | As baseline |
| C-09–C-11 | PASS | INPUT INVENTORY ≥5 rows, sole citation source, EXIT GATE enforced |
| C-12–C-13 | PASS | S1-S3 and G1-G3 labeled format present |
| C-14 | PASS | Candidate roster in STEP 2 with S/G label column |
| C-15 | PASS | Frame fill with `Phase 1 source: {row-id} = "{verbatim phrase}"` per field |
| C-16–C-18 | PASS | Planning table; SCOPE AUDIT `< 2: fail / >= 2: pass` labeled; PERSPECTIVE AUDIT labeled |
| C-19–C-20 | PASS | Inertia-advocate written first; "INERTIA-ADVOCATE WRITTEN: {path}" emitted |
| C-21–C-25 | PASS | 6-item LENS AUDIT per non-inertia role (inherited from baseline) |
| C-26–C-36 | PASS | All STEP 4 verification checks present with PASS/FAIL labels |
| C-37 | PASS | STEP 4 INERTIA ANCHOR CHECK: "Emit: INERTIA ANCHOR CHECK: PASS/FAIL" with explicit "as validated at STEP 1 NON-GENERIC CHECK" back-ref |
| **C-38** | **PASS** | STEP 3 EARLY INERTIA ANCHOR CHECK: "EARLY INERTIA ANCHOR CHECK: PASS — proceed to remaining roles / FAIL — revise file and re-check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS." — explicit label, explicit block statement, references prior STEP 2 PASS |
| **C-39** | **PARTIAL** | FRAME FILL PRE-ANCHOR CHECK present in STEP 2 with explicit "FRAME FILL PRE-ANCHOR CHECK: PASS / FAIL" labels ✓; fires after inertia-advocate frame fill, before other roles ✓; but STEP 2 ≠ Phase 4 — step numbering does not map to Phase 4 |
| **C-40** | **PARTIAL** | NON-GENERIC REQUIREMENT block in STEP 1 (not Phase 2) — all structural elements present: operational def ✓, negative-example list ✓, explicit "NON-GENERIC CHECK: PASS" emission ✓, EXIT GATE includes it ✓; STEP 4 back-ref "as validated at STEP 1 NON-GENERIC CHECK" ✓; phase placement wrong (STEP 1 ≠ Phase 2) |
| **C-41** | **PASS** | STEP 3 LENS AUDIT item 6 present; STEP 4 CROSS-ROLE SPREAD CHECK: "Emit: CROSS-ROLE SPREAD CHECK: PASS/FAIL [N non-inertia roles with baseline reference, list them]" |

**Criterion scores**: C-09–C-37 = 29×1.0; C-38 = 1.0; C-39 = 0.5; C-40 = 0.5; C-41 = 1.0
**Total**: 32.0 / 33 × 10 = **9.70**

---

### V-03 — Axis-K: Inertia Front-Loading (7 phases, inertia-advocate in Phase 2)

**Hypothesis**: Phase 2 ANCHOR VALIDATION satisfies C-39's functional intent (fires before Phase 5/6); rubric "Phase 4" may be literal or functional.

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS | All fields, inertia-advocate, correct path, domain specificity; total roles = 4 Phase-3 candidates + inertia-advocate ≥ 5 ✓ |
| C-06–C-08 | PASS | As baseline |
| C-09–C-11 | PASS | INPUT INVENTORY ≥5 rows in Phase 1, sole citation source, EXIT GATE present |
| C-12–C-13 | PASS | S1-S3 and G1-G3 labeled format |
| C-14 | PASS | Phase 3 candidate roster table (non-inertia roles) with G-label column; inertia-advocate defined in Phase 2 with own frame fill; Planning Table Phase 5 unifies both ✓ |
| C-15 | PASS | Frame fill in Phase 2 (inertia-advocate) and Phase 4 (others) with citations per field |
| C-16–C-18 | PASS | Planning table in Phase 5; SCOPE AUDIT / PERSPECTIVE AUDIT labeled with PASS/FAIL |
| C-19–C-20 | PASS | STEP 6.1: inertia-advocate written first; "INERTIA-ADVOCATE WRITTEN: {path}" emitted |
| C-21–C-25 | PASS | STEP 6.2 LENS AUDIT: 6 items per non-inertia role |
| C-26–C-36 | PASS | Phase 7 verification checks 1–8 present with labeled emissions |
| C-37 | PASS | Phase 7 INERTIA ANCHOR CHECK: explicit label + "as validated at Phase 2 NON-GENERIC CHECK" back-ref — strongest chain-of-custody of any variation |
| **C-38** | **PASS** | Phase 6.1 EARLY INERTIA ANCHOR CHECK: "EARLY INERTIA ANCHOR CHECK: PASS — proceed to STEP 6.2 / FAIL — revise and re-check. Since Phase 2 ANCHOR VALIDATION already confirmed this pattern in the FRAME FILL, this check should confirm file fidelity, not discover a new omission." — explicit label, explicit block, explicit purpose statement |
| **C-39** | **FAIL** | PHASE 2 ANCHOR VALIDATION fires in Phase 2 (before Phase 3 candidate roster) — mechanism present and blocking ✓; but Phase 2 ≠ Phase 4; C-39 specifies Phase 4 as the required location; this is the farthest phase deviation (Δ = 2 phases earlier than Phase 4) |
| **C-40** | **PASS** | "NON-GENERIC REQUIREMENT:" block label present in Phase 2 ✓; operational definition: "a phrase is non-generic if and only if it contains at least one noun or verb specific to this domain…" ✓; negative-example list ✓; "Emit: NON-GENERIC CHECK: PASS (with each validated S-label: phrase and G-label: phrase)" ✓; Phase 2 EXIT GATE includes "NON-GENERIC CHECK PASS" ✓; Phase 7 back-ref: "as validated at Phase 2 NON-GENERIC CHECK" ✓ — all four structural elements present in Phase 2 as specified |
| **C-41** | **PASS** | Phase 6.2 LENS AUDIT item 6 present; Phase 7 CROSS-ROLE SPREAD CHECK with labeled emission |

**Criterion scores**: C-09–C-37 = 29×1.0; C-38 = 1.0; C-39 = 0.0; C-40 = 1.0; C-41 = 1.0
**Total**: 32.0 / 33 × 10 = **9.70**

---

### V-04 — Axis-I + Axis-J: Prose + 4 Steps

**Hypothesis**: Compound degradation — prose removes gate labels; step compression removes phase identity; C-39 three-checkpoint chain may collapse.

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS | All fields, inertia-advocate, correct path, domain specificity, 5+ roles |
| C-06–C-08 | PASS | As baseline |
| C-09–C-11 | PASS | INPUT INVENTORY ≥5 rows, sole citation source, "Do not proceed to Step 2 until 5+ rows are present" |
| C-12–C-15 | PASS | Labeled S/G terms; candidate roster with labels; frame fill with Step 1 citations |
| C-16–C-18 | PASS | Planning table; "Count distinct Scope values — if fewer than 2… Count distinct Perspective values — if fewer than 3…" — mechanism present, prose format |
| C-19–C-20 | PASS | "Write the inertia-advocate first"; emit present in Step 3 |
| C-21–C-25 | PASS | Step 3 per-role checklist: 6 items including INERTIA BASELINE reference |
| C-26–C-36 | PASS | Step 4 verification checks emit "PASS or FAIL" — labeled at verification level |
| C-37 | PASS | Step 4 inertia anchor check: "Emit: PASS or FAIL" with "as confirmed non-generic in Step 1" back-ref |
| **C-38** | **PARTIAL** | Step 3 inertia-advocate confirmation: "re-read its lens.verify and confirm the S-label entry is present. If yes, proceed to remaining roles. If no, revise and re-read before continuing. Do not write other roles until this confirmation is complete." — blocking ✓; no "EARLY INERTIA ANCHOR CHECK: PASS/FAIL" label emitted |
| **C-39** | **FAIL** | Step 2 back-read check in prose: "read it back and check: does lens.verify contain… If yes, continue… If no, revise." — fires at right logical moment ✓; but (a) Step 2 ≠ Phase 4, (b) prose format with no label, (c) no PASS/FAIL emission — both dimensions missing |
| **C-40** | **PARTIAL** | Step 1 operational definition ✓; negative-example list ✓; forward-reference "Step 4 inertia anchor check will reference these specific validated phrases" ✓; Step 4 back-ref "as confirmed non-generic in Step 1" ✓; but no "NON-GENERIC REQUIREMENT:" block label, no "NON-GENERIC CHECK: PASS" emission, Step 1 ≠ Phase 2 |
| **C-41** | **PASS** | Step 3 checklist item 6: "Does lens.verify reference at least one INERTIA BASELINE term (S or G label + phrase from Step 1)? Yes / No + which term"; Step 4 cross-role spread check: "Emit: PASS or FAIL [N non-inertia roles with reference, list them]" |

**Criterion scores**: C-09–C-37 = 29×1.0; C-38 = 0.5; C-39 = 0.0; C-40 = 0.5; C-41 = 1.0
**Total**: 31.0 / 33 × 10 = **9.39**

---

### V-05 — Axis-I + Axis-J + Axis-K: Full Integration

**Hypothesis**: Earliest anchor (Step 1 before candidates), most compressed (4 steps), prose gates — does full integration produce a clean audit chain or collapse checkpoints?

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS | All fields, inertia-advocate, correct path, domain specificity; 4 Step-2 candidates + inertia-advocate = 5 ✓ |
| C-06–C-08 | PASS | As baseline |
| C-09–C-11 | PASS | INPUT INVENTORY ≥5 rows in Step 1, sole citation source, "Do not proceed past this point until 5+ rows exist" |
| C-12–C-15 | PASS | S1-S3/G1-G3 labeled; G-label references in Step 2 candidates; frame fill with citations |
| C-16–C-18 | PASS | Planning table in Step 3; scope/perspective count checks in prose — mechanism present |
| C-19–C-20 | PASS | "Write the inertia-advocate first using its Step 1 frame fill values"; emit present |
| C-21–C-25 | PASS | Step 3 per-role checklist: 6 items |
| C-26–C-36 | PASS | Step 4 checks emit "PASS or FAIL" |
| C-37 | PASS | Step 4 inertia anchor check: "as confirmed non-generic in Step 1" back-ref ✓; "Emit: PASS or FAIL" |
| **C-38** | **PARTIAL** | Step 3 confirmation: "re-read the lens.verify and confirm the S-label entry is present — since the Step 1 back-read already confirmed the frame fill, this is a file-fidelity confirmation. If the entry is absent (file fidelity failure), revise and re-read before continuing." — blocking ✓, explicit purpose articulation (strongest functional clarity of any variation) ✓; but no "EARLY INERTIA ANCHOR CHECK: PASS/FAIL" label |
| **C-39** | **FAIL** | Step 1 back-read: "read back the lens.verify text and confirm it contains at least one 'S{N}: {phrase}' entry… If yes, the anchor is set — proceed to Step 2. If no, revise the inertia-advocate lens.verify now, before Step 2." — prose, Step 1 location (furthest from Phase 4: Δ = 3 steps earlier), no label emission |
| **C-40** | **PARTIAL** | Step 1 non-generic test with operational def ✓, negative examples ✓, "record the validated label-phrase pairs; Step 4 inertia anchor check will reference these exact phrases" ✓; Step 4 back-ref "as confirmed non-generic in Step 1" ✓; no "NON-GENERIC REQUIREMENT:" block label, no "NON-GENERIC CHECK: PASS" emission |
| **C-41** | **PASS** | Step 3 checklist item 6 ✓; Step 4 cross-role spread check ✓ |

**Criterion scores**: C-09–C-37 = 29×1.0; C-38 = 0.5; C-39 = 0.0; C-40 = 0.5; C-41 = 1.0
**Total**: 31.0 / 33 × 10 = **9.39**

---

### Composite Score Summary

| Variation | C-38 | C-39 | C-40 | C-41 | Sum | Score |
|-----------|------|------|------|------|-----|-------|
| V-01 (Prose, 7-phase) | 0.5 | 0.5 | 0.5 | 1.0 | 31.5 | **9.55** |
| V-02 (Labeled, 4-step) | 1.0 | 0.5 | 0.5 | 1.0 | 32.0 | **9.70** |
| V-03 (Front-load, 7-phase) | 1.0 | 0.0 | 1.0 | 1.0 | 32.0 | **9.70** |
| V-04 (Prose + 4-step) | 0.5 | 0.0 | 0.5 | 1.0 | 31.0 | **9.39** |
| V-05 (All-three) | 0.5 | 0.0 | 0.5 | 1.0 | 31.0 | **9.39** |

Prior 29 criteria (C-09–C-37) = 29.0 for all variations.

**Rank**: V-02 = V-03 (9.70) > V-01 (9.55) > V-04 = V-05 (9.39)

---

### Scoring Question Answers

**Q1: Does C-39 require "Phase 4" literally?**
Yes. Phase 4 is literal. V-03's Phase 2 ANCHOR VALIDATION and V-05's Step 1 back-read both FAIL C-39. Earlier is not equivalent. The three-checkpoint chain requires the first check to fire at Phase 4 specifically (after frame fill in a phase that exists after candidate roster Phase 3, before write Phase 6). Moving it before Phase 3 changes the chain semantics.

**Q2: Does C-40 back-reference chain survive step renumbering?**
Partially. V-02 shows the chain survives (STEP 1 NON-GENERIC CHECK → STEP 4 back-ref) with explicit step-numbered labels, scoring PARTIAL not FAIL. The chain content is preserved; only the "Phase 2" placement criterion is missed. Step renumbering does not break the reference chain when labels are explicit.

**Q3: Do prose-register gates score PASS on C-38/C-39/C-40?**
No — PARTIAL across the board. V-01 confirms that content equivalence does not earn PASS when a criterion requires explicit PASS/FAIL emission labels. Uppercase label format is load-bearing: it signals to LLMs that the gate is non-optional and requires an explicit state transition.

---

### Excellence Signals (from V-02 and V-03)

**V-02 — Cross-step reference chain preservation under compression**
The FRAME FILL PRE-ANCHOR CHECK explicitly names the prior state: "If STEP 2 FRAME FILL PRE-ANCHOR CHECK PASS was correctly emitted, this is confirmation." This creates a forward-traceable audit chain even across 4-step compression. The pattern: each checkpoint should name the preceding checkpoint's emission token, converting a sequential dependency into an explicit reference chain.

**V-03 — Phase-exact C-40 placement earns PASS; clarifies EARLY ANCHOR CHECK purpose**
By placing the inertia-advocate's entire frame fill in Phase 2, V-03 achieves the only full PASS on C-40 across all R19 variations. The EARLY INERTIA ANCHOR CHECK in Phase 6.1 explicitly states its role: "Since Phase 2 ANCHOR VALIDATION already confirmed this pattern in the FRAME FILL, this check should confirm file fidelity, not discover a new omission." This purpose declaration reduces redundancy ambiguity and makes the three-checkpoint chain semantics explicit.

**Common to both top variations**
- Blocking consequences stated explicitly at each gate: "STEP 6.2 is blocked until EARLY INERTIA ANCHOR CHECK PASS" / "Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS"
- Every gate emits a named token (PASS/FAIL with the gate label) that downstream gates can reference by name

---

### Baseline Comparison

R18 V-05 (all 33 criteria baseline) = 10.0 theoretical maximum.
R19 stress-testing reveals no variation achieves full PASS on C-39 + C-40 simultaneously in a single design. The two criteria are structurally in tension: Phase-exact C-40 placement (Phase 2) rewards front-loading (Axis-K) which disqualifies C-39 Phase-4 placement. The ideal R20 target: a variation that keeps C-40 in Phase 2 AND adds C-39 back in Phase 4 by splitting Phase 2 into 2.1 (INERTIA BASELINE + NON-GENERIC CHECK) and 2.2 (CONVERGENCE SUMMARY), then placing inertia-advocate frame fill in Phase 4 as in the baseline — with full uppercase labels throughout.

---

```json
{"top_score": 9.7, "all_essential_pass": true, "new_patterns": ["Uppercase PASS/FAIL label format is load-bearing not cosmetic — prose equivalents of C-38, C-39, C-40 gates consistently score PARTIAL; content equivalence alone does not earn PASS", "C-40 back-reference chain survives step renumbering when explicit step-numbered labels are maintained — V-02 scores PARTIAL not FAIL, confirming chain content is preserved even when phase placement deviates", "C-39 Phase-4 placement and C-40 Phase-2 placement are architecturally incompatible in a front-loading design — achieving PASS on both simultaneously requires keeping inertia-advocate frame fill in Phase 4 while placing NON-GENERIC REQUIREMENT block in Phase 2 as separate sub-steps"]}
```
