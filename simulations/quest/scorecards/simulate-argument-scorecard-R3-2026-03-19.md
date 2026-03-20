## simulate-argument R3 — Score Report (v3 Rubric)

### Scoring Basis

These are prompt templates, not executed outputs. Each variation is scored on whether its structural mechanisms **mandate** the behavior required by each criterion — whether the design guarantees compliance when run on any topic, not whether a specific execution found a DRIFT or a P1 fault.

---

### V-01 — Output Format (Table-Dominant Phase 3)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 claim map present | PASS | Phase 2 table with 6+ row minimum, C-ID, claim text, type column |
| C-02 dependency graph complete | PASS | Depends on column; every inference row must list at least one C-ID |
| C-03 section coverage | PASS | "At least one claim per major section" stated explicitly |
| C-04 every inference traced | PASS | One table row per inference = one traced step; all 3 check columns present |
| C-05 fault register matches verdicts | PASS | "Every row with Verdict = WEAK or BROKEN from Phase 3 must appear here" |
| C-06 logical forms named | PASS | Logical Form column; named structure required; empty cell = structural gap |
| C-07 AMEND ordered + actionable | PASS | Phase 5: 3 fixes P1→P2→P3, each referencing F-ID, C-ID, Class, exact repair |
| C-08 frontmatter complete | PASS | 6 required fields listed explicitly with consistency requirement |
| C-09 term drift detected | PASS | Consistency column has `DRIFT: [term, def C-ID, shift]`; P3 AMEND: "if DEF-DRIFT, name originating definition claim (C-ID) and propose stable replacement wording" |
| C-10 structural weakness exposed | PASS | Gap field: "[DEPTH-TIER] [structural explanation of why the inference fails — not just that it does]"; Domain Comparison column required for WEAK/BROKEN |
| C-11 falsification target | PASS | Phase 0 best-case statement; "This is the falsification target. Every fault you find should either support or undermine this statement." Phase 4 Closing returns to it. |
| C-12 inline reviewer hook | PASS | Reviewer Flag? column required for WEAK/BROKEN; "N/A for SOUND" |
| C-13 fault pattern synthesized | PASS | Phase 4 Closing: "State the dominant fault class by code (most rows). Assess whether the fault pattern confirms or refutes the Phase 0 best-case statement." Codes (DEF-DRIFT etc.) = structural vocabulary |
| C-14 fault class taxonomy | PASS | Class column with four codes; Phase 4 Closing "count rows in the Class column" |
| C-15 reviewer depth tier | PASS | Depth column + Domain Comparison column; Gap field format starts with `[DEPTH-TIER]` tag |

```
C-01 PASS  C-02 PASS  C-03 PASS  C-04 PASS  C-05 PASS
C-06 PASS  C-07 PASS  C-08 PASS
C-09 PASS  C-10 PASS  C-11 PASS  C-12 PASS  C-13 PASS  C-14 PASS  C-15 PASS

essential_pass    = 5/5
recommended_pass  = 3/3
aspirational_pass = 7/7

composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10) = 60 + 30 + 10 = 100
golden = YES
```

---

### V-02 — Phrasing Register (Adversarial Skeptic Voice)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-05 | PASS | Claim Map, Depends on, section coverage, 3A/3B/3C trace, Fault Register all present |
| C-06 | PASS | 3A dedicated form identification pass; named form required before validity checks |
| C-07 | PASS | Phase 5: 3 fixes P1→P2→P3, F-ID, C-ID, Class, exact repair |
| C-08 | PASS | Frontmatter with 6 fields |
| C-09 | PASS | 3B DRIFT check with term+C-ID+shift; P3 AMEND: "if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording" |
| C-10 | PASS | Adversarial prior + "the inference that looks valid on first read but doesn't survive scrutiny from someone who knows the field"; Reviewer flag in 3C natural to role |
| C-11 | PASS | Phase 0 challenge statement; "This is what you are about to challenge" |
| C-12 | PASS | 3C: "Reviewer flag: Would a domain reviewer flag this as non-obvious? YES/NO — one-sentence justification"; adversarial role makes this natural |
| C-13 | PASS | Phase 4 Closing: "Count rows per class code. Name the dominant class (most rows). Does fault pattern confirm or refute Phase 0? Is inertia defensible?" Dominant class named by code = structural vocabulary |
| C-14 | PASS | Class column; Phase 4 Closing counts per code |
| C-15 | PASS | 3C: Depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) + Domain comparison; Gap field: depth tier tag in brackets |

```
essential_pass = 5/5  recommended_pass = 3/3  aspirational_pass = 7/7
composite = 100  golden = YES
```

---

### V-03 — Inertia Framing (Null-Hypothesis Frame)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-05 | PASS | All structural elements present |
| C-06 | PASS | 3A form identification pass |
| C-07 | PASS | Phase 5 AMEND |
| C-08 | PASS | Frontmatter |
| C-09 | PASS | 3B DRIFT with C-ID; P3 AMEND DEF-DRIFT instruction |
| C-10 | PASS | "bearing on whether a knowledgeable reviewer would catch it before submission"; Gap field structural explanation |
| C-11 | PASS | Phase 0: best-case paragraph + explicit H0 "This argument is structurally sound and requires no revision"; null hypothesis IS the falsification target |
| C-12 | PASS | 3C Reviewer flag present |
| C-13 | PASS | Phase 4 Closing 3-step test: (1) dominant class by code, (2) P1 count → null reject/fail-to-reject, (3) "H0 is [rejected/not rejected]. Inertia is [not defensible/defensible]." Names structural class code, not just depth tier. |
| C-14 | PASS | Class column; step 1 counts per code |
| C-15 | PASS | 3C depth tier + domain comparison; Gap field tier tag |

**Note on C-13**: The three-step rejection test is the tightest C-13 mechanism in any round. Step 1 names the dominant fault class by code (structural vocabulary). Step 3 delivers a binary verdict on Phase 0. The v3 disqualifier ("naming only a depth tier") cannot apply — the code names are fault taxonomy codes, not depth tiers.

```
essential_pass = 5/5  recommended_pass = 3/3  aspirational_pass = 7/7
composite = 100  golden = YES
```

---

### V-04 — Table Phase 3 + Expanded Phase 4 Synthesis

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-05 | PASS | All present |
| C-06 | PASS | Logical Form column |
| C-07 | PASS | Phase 5 AMEND |
| C-08 | PASS | Frontmatter |
| C-09 | PASS | Consistency DRIFT column; P3 DEF-DRIFT instruction |
| C-10 | PASS | Domain Comparison column; Gap field structural explanation |
| C-11 | PASS | Phase 0 best-case + "The Phase 4 synthesis will return to this statement explicitly" — forward reference strengthens C-11 |
| C-12 | PASS | Reviewer Flag? column |
| C-13 | PASS | Phase 4 Synthesis item 3: "Does the fault pattern confirm or refute the Phase 0 best-case statement? Reference the best-case statement by paraphrase. **Name the dominant fault class in your answer.**" Satisfies both the "confirm/refute" and the structural class name requirements. |
| C-14 | PASS | Class column; Synthesis item 1: "Dominant fault class: [CODE] ([n] of [total] faults)" |
| C-15 | PASS | Depth + Domain Comparison columns; Gap field tier tag; Synthesis item 2 counts depth tier distribution |

**Distinguishing feature**: The 3-part Phase 4 Synthesis is the most explicit C-13 enforcement of any single-voice variation. Item 1 = C-14 integration, Item 2 = C-15 synthesis, Item 3 = C-13 with mandatory class name. The Phase 4 Synthesis section also adds a new behavior: asking "at this depth tier, would standard peer review surface these faults before publication?" — a depth-to-reviewability link not present in other variations.

```
essential_pass = 5/5  recommended_pass = 3/3  aspirational_pass = 7/7
composite = 100  golden = YES
```

---

### V-05 — All Three Axes (Table + Adversarial + Inertia)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-05 | PASS | All present |
| C-06 | PASS | Logical Form column |
| C-07 | PASS | Phase 5 AMEND |
| C-08 | PASS | Frontmatter |
| C-09 | PASS | Consistency DRIFT column; P3 DEF-DRIFT instruction |
| C-10 | PASS | Adversarial role ("as the skeptical reviewer, your column entries should reflect what you would write in a review form") + Domain Comparison column |
| C-11 | PASS | Phase 0: best-case + H0 null hypothesis; "You will attempt to reject H0. If you cannot, you must say so explicitly." |
| C-12 | PASS | Reviewer Flag? column: "As the skeptical reviewer, would you flag this in a written review?" — adversarial voice makes this structurally authentic |
| C-13 | PASS | Phase 4 Synthesis item 3: null rejection verdict with "name the dominant fault class in the rejection statement." |
| C-14 | PASS | Class column; Synthesis item 1 names dominant code |
| C-15 | PASS | Depth + Domain Comparison columns; Gap field tier tag; Synthesis item 2 |

**Interaction check**: Three axes interact as predicted — adversarial voice makes Reviewer Flag? column natural ("what you would write in a review form"), inertia frame makes Phase 4 Synthesis item 3 a decision not an assessment, table format makes the adversarial role operational rather than rhetorical. No competing expectations detected.

```
essential_pass = 5/5  recommended_pass = 3/3  aspirational_pass = 7/7
composite = 100  golden = YES
```

---

### Ranking

All five variations score 100. Ranked by enforcement strength on the historically difficult criteria (C-13, C-15):

| Rank | Variation | Distinguishing Strength |
|------|-----------|------------------------|
| 1 | **V-05** | Maximum enforcement: table compliance + adversarial depth + binary decision; all three axes mutually reinforce |
| 2 | **V-04** | Clearest structural separation: Phase 3 compress → Phase 4 expand; 3-part synthesis makes C-13/C-14/C-15 explicit subsections |
| 3 | **V-03** | Tightest C-13 mechanism: formal three-step null-rejection test with P1 count threshold + binary "inertia defensible" verdict |
| 4 | **V-01** | Most minimal/elegant: table format alone closes C-15 without role framing; empty cell = visible structural gap |
| 5 | **V-02** | Deepest C-10 signal: adversarial prior inverts default hedging; but relies more on framing than structural enforcement |

---

### Excellence Signals (New in R3)

Three patterns emerged in R3 that had no equivalent in prior rounds:

**1. table-column-enforcement** (V-01, V-04, V-05): Replacing free-form STEP blocks with a wide Inference Trace Table makes every required field a named column. An empty cell is a visible structural gap, not an invisible omission. This is a fundamentally different compliance mechanism than sub-pass gating — it transfers the enforcement burden from the model's attention to the table's structure.

**2. null-rejection-test** (V-03, V-05): Phase 4 closing as a formal three-step H0/reject test (count dominant class code → count P1 faults → binary verdict on inertia) forces C-13 to be a decision with a severity threshold, not an open-ended assessment. The "inertia is [not defensible / defensible with minor fixes / defensible]" sentence is more actionable than "the fault pattern refutes Phase 0."

**3. adversarial-prior-inversion** (V-02, V-05): Framing Phase 0 as a prior-to-retract rather than a target-to-test inverts the default hedging behavior. The model must either name the dominant structural fault class or explicitly state "my prior was wrong" — both outcomes are structurally committed. Reviewer hooks become natural to the role rather than mandated additions.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table-column-enforcement", "null-rejection-test", "adversarial-prior-inversion"]}
```
