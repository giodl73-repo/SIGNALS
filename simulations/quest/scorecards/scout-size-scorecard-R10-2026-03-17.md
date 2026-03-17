## scout-size R10 — Quest Score

### Scoring approach

All five variations share an identical body (PRE-FLIGHT GATE through SIGNAL BOUNDARY CHECK) taken from R9 V-05. That body passes C-01 through C-27 in all variations. The SELF-CHECK section is the only differentiator across variations. I score C-28 through C-31 per-variation; C-01 through C-27 are identical and marked PASS throughout.

---

### Criteria common to all variations (body is R9 V-05 base)

| # | Criterion | All 5 | Evidence |
|---|-----------|-------|----------|
| C-01 | Complexity tier vocabulary | PASS | STEP 3: "exactly LOW / MEDIUM / HIGH / XL" enforced |
| C-02 | Sprint range | PASS | STEP 4: sprint range with explicit failing forms for point estimates |
| C-03 | Surface area Total row | PASS | STEP 2: "Total row required. 'Several integration points' is not an enumeration." |
| C-04 | Inertia check | PASS | STEP 1: Workaround, Maintenance cost, Cost direction all labeled fields |
| C-05 | Confidence with basis | PASS | STEP 5: "what IS known -- specific evidence, prior work, or verified reasoning" |
| C-06 | Team specializations | PASS | STEP 4: "specialist disciplines + FTE fractions + implementation ownership per role" |
| C-07 | Complexity driver | PASS | STEP 3: "Primary driver: [one or two factors most responsible]" |
| C-08 | AMEND modifies output | PASS | STRUCTURAL AMEND RE-EVALUATION DIRECTIVE in STEP 7; default pass if absent |
| C-09 | Out-of-scope boundary | PASS | PRE-FLIGHT GATE: "Name at least one sub-system... explicitly NOT covered" |
| C-10 | Break-even signal | PASS | PRE-FLIGHT GATE: break-even field required before any analysis |
| C-11 | Specialization ownership | PASS | STEP 4: "implementation ownership per role" with passing/failing example |
| C-12 | Named unknowns | PASS | STEP 6: Unknown / Impact / Movement fields required |
| C-13 | Cross-signal synthesis | PASS | STEP 7: "cross-signal observation combining at least two dimensions" |
| C-14 | Unknowns in dedicated section | PASS | STEP 5 explicitly closed against unknowns; STEP 6 is canonical home |
| C-15 | Hypothesis revision lifecycle | PASS | PRE-FLIGHT GATE elicits tier + sprint range; STEP 7 confirms or revises |
| C-16 | AMEND cascades to synthesis | PASS | STRUCTURAL AMEND RE-EVALUATION DIRECTIVE handles this structurally |
| C-17 | Sections name failure mode | PASS | STEP 6 FAILURE MODE block: "generic hedge fails exactly as silently"; STEP 7: "juxtaposition, not synthesis" |
| C-18 | Pre-analysis self-check gate | PASS | PRE-FLIGHT GATE before STEP 1; STOP instruction present |
| C-19 | Prohibition guards | PASS | STEP 5 closed against unknowns; STEP 2/3 closed against scope |
| C-20 | Complete closure mesh | PASS | STEP 1, 2, 3, 7 all carry scope prohibitions; STEP 3, 5, 7 carry unknown prohibitions |
| C-21 | Gate elicits hypothesis | PASS | Preliminary hypothesis is a field inside PRE-FLIGHT GATE, not standalone |
| C-22 | Synthesis names gate at both ends | PASS | "look back at PRE-FLIGHT GATE" + "committed in PRE-FLIGHT GATE" in verdict |
| C-23 | Guards name canonical home | PASS | "scope was resolved in PRE-FLIGHT GATE, not in analysis steps" |
| C-24 | Commitment-chain trace | PASS | Gate commitment: / Analysis: / Verdict: on separate labeled lines |
| C-25 | Gate forward-references enforcement sections | PASS | Enforcement contract names STEP 1, 2, 3, 7 (scope) and STEP 7 (hypothesis) |
| C-26 | Structural AMEND directive in synthesis | PASS | "applies on every invocation, independent of whether an AMEND directive is present"; "structural failure of this section's integrity" |
| C-27 | Dedicated FAILURE MODE blocks | PASS | Both STEP 6 and STEP 7 carry `> **FAILURE MODE FOR THIS SECTION**:` blocks |

---

### V-01 — Axis: Depth/behavior disqualifying forms (C-30 only)

Self-check header: "ASPIRATIONAL CRITERIA (C-09 through C-31)" — explicitly excludes C-01-C-08.

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-28 | Per-criterion self-check covering all aspirational | PASS | Self-check covers C-09 through C-31 with pass/fail per criterion |
| C-29 | Structural criteria have exact disqualifying forms | PASS | C-18-C-27 all carry exact disqualifying forms (inherited from R9 V-05) |
| C-30 | Depth/behavior criteria have exact disqualifying forms | PASS | C-09-C-17 each carry a named disqualifying form (e.g., C-09: "Standard integrations excluded" fails — names a category, not a specific sub-system) |
| C-31 | Self-check extends to essential/recommended | FAIL | "Essential and recommended criteria are absent from this self-check. C-31 FAILS in this variation — intended single-axis design." |

**Aspirational: 22/23** (fails C-31)
**Composite: 60 + 30 + (22/23 × 10) = 99.57**

---

### V-02 — Axis: Essential/recommended scope extension (C-31 only)

Self-check header: "ALL 31 CRITERIA (C-01 through C-31)" — includes C-01-C-08 as flat checklist with pass conditions and verification guidance. C-09-C-17 retain pass-condition-only descriptions.

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-28 | Per-criterion self-check covering all aspirational | PASS | Self-check covers C-09 through C-31 plus C-01-C-08 |
| C-29 | Structural criteria have exact disqualifying forms | PASS | C-18-C-27 all carry exact disqualifying forms |
| C-30 | Depth/behavior criteria have exact disqualifying forms | FAIL | "Depth/behavior items above contain pass conditions only — exact disqualifying forms are absent. C-30 FAILS in this variation — intended single-axis design." C-09: "At least one explicit exclusion or out-of-scope boundary named" carries no disqualifying form. |
| C-31 | Self-check extends to essential/recommended | PASS | C-01-C-05 present as essential checklist; C-06-C-08 present as recommended checklist with verification guidance |

**Aspirational: 22/23** (fails C-30)
**Composite: 60 + 30 + (22/23 × 10) = 99.57**

---

### V-03 — Minimal combination (C-30 + C-31)

Self-check header: "ALL 31 CRITERIA (C-01 through C-31)." Adds disqualifying forms to C-09-C-17 AND adds C-01-C-08 as flat checklist (no disqualifying forms for essential/recommended, but pass/fail entries present).

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-28 | Per-criterion self-check covering all aspirational | PASS | Covers C-01 through C-31 |
| C-29 | Structural criteria have exact disqualifying forms | PASS | C-18-C-27 all carry exact disqualifying forms |
| C-30 | Depth/behavior criteria have exact disqualifying forms | PASS | C-09-C-17 each carry disqualifying form (e.g., C-09: "Standard integrations excluded" fails — category, not specific sub-system) |
| C-31 | Self-check extends to essential/recommended | PASS | C-01-C-05 in flat checklist; C-06-C-08 in flat checklist; "Essential and recommended are present above — PASS" |

**Aspirational: 23/23**
**Composite: 60 + 30 + (23/23 × 10) = 100.00**

---

### V-04 — Fuller integration (table format for C-01-C-08)

Self-check header: "ALL 31 CRITERIA." Adds V-03 mechanisms plus presents C-01-C-08 in a three-column table (ID / What to verify / Failing form), making essential/recommended structurally scannable. C-09-C-17 have disqualifying forms as flat checklist items.

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-28 | Per-criterion self-check covering all aspirational | PASS | Covers C-01 through C-31; table format for C-01-C-08 |
| C-29 | Structural criteria have exact disqualifying forms | PASS | C-18-C-27 all carry exact disqualifying forms |
| C-30 | Depth/behavior criteria have exact disqualifying forms | PASS | C-09-C-17 each carry disqualifying form (same as V-03) |
| C-31 | Self-check extends to essential/recommended | PASS | Essential/recommended table present; "Essential/recommended table is present above — PASS" with explicit disqualifying form for C-31 itself |

**Aspirational: 23/23**
**Composite: 60 + 30 + (23/23 × 10) = 100.00**

Note: V-04 exceeds V-03 in structural scannability by presenting C-01-C-08 in a table with failing forms. The rubric doesn't require this surplus structure, but the table format makes C-31 compliance auditable at a glance.

---

### V-05 — Full integration (all 31 criteria with complete disqualifying forms)

Self-check header: "ALL 31 CRITERIA." V-04 mechanisms plus disqualifying-form treatment extended to essential (C-01-C-05) and recommended (C-06-C-08) tables — two separate tables using ID / Pass condition / Disqualifying form format. Every criterion across all 31 carries both a pass condition and an exact failing form.

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-28 | Per-criterion self-check covering all aspirational | PASS | Covers C-01 through C-31; separate tables for essential and recommended |
| C-29 | Structural criteria have exact disqualifying forms | PASS | C-18-C-27 all carry exact disqualifying forms (table items in structural section) |
| C-30 | Depth/behavior criteria have exact disqualifying forms | PASS | C-09-C-17 each carry disqualifying form with notably richer annotations (e.g., C-13: "HIGH complexity and a 4-6 sprint timeline means this requires careful planning — 'careful planning' is derivable from complexity alone; a failing conclusion survives removing one of the cited dimensions") |
| C-31 | Self-check extends to essential/recommended | PASS | Essential table (C-01-C-05) and recommended table (C-06-C-08) each with ID / Pass condition / Disqualifying form; C-31 self-check item includes its own disqualifying form: "a self-check that covers all 23 aspirational criteria with complete precision but omits C-01-C-08 entries entirely fails C-31" |

**Aspirational: 23/23**
**Composite: 60 + 30 + (23/23 × 10) = 100.00**

V-05 goes beyond rubric minimum: C-31 only requires pass/fail for essential/recommended; V-05 adds disqualifying forms to those entries, eliminating the last detection-gap class.

---

### Ranking

| Rank | Variation | Aspirational | Score | Delta |
|------|-----------|-------------|-------|-------|
| 1 (tied) | V-03 | 23/23 | 100.00 | — |
| 1 (tied) | V-04 | 23/23 | 100.00 | — |
| 1 (tied) | V-05 | 23/23 | 100.00 | — |
| 4 (tied) | V-01 | 22/23 | 99.57 | −0.43 |
| 4 (tied) | V-02 | 22/23 | 99.57 | −0.43 |

All essential criteria pass in all five variations.

---

### Excellence Signals (from V-05, the most thorough top-scorer)

**Signal 1 — Depth/behavior self-check parity.** V-05 applies the disqualifying-form treatment uniformly across all aspirational criterion categories. R9 V-05 established this precision for structural criteria (C-18-C-27) under C-29 but left depth/behavior criteria (C-09-C-17) as pass-condition descriptions. V-05 closes the asymmetry: every depth/behavior criterion names the exact output pattern that satisfies the surface signal but fails the criterion. The richer annotations go further than the minimal form in V-03 — e.g., C-13's disqualifying form tests whether a conclusion "survives removing one of the cited dimensions," a precision that guides a model beyond the simple definition.

**Signal 2 — Weight-class-complete verification trace.** V-05 extends the self-check to all 31 criteria across all weight classes. The essential/recommended entries use the same three-column table format (ID / Pass condition / Disqualifying form) as the aspirational entries, creating a uniform audit artifact. This closes the structural gap where the most consequential criteria (essential failures disqualify the output entirely) were implicitly assumed to pass rather than explicitly verified.

**Signal 3 — Table-over-checklist for essential/recommended.** V-04 and V-05 both use a table to present C-01-C-08, making the coverage structurally distinguishable from the aspirational section at a glance. The table boundary is self-evident: absence would leave a visible structural gap, the same reliability argument that motivated dedicated FAILURE MODE blocks (C-27) at the section level.

**Signal 4 — Uniform disqualifying-form treatment beyond rubric minimum.** V-05 extends disqualifying forms to essential and recommended criteria even though C-31 only requires pass/fail + evidence. The same argument that justified C-29 (structural category) and C-30 (depth/behavior category) applies: a self-check item that states only the pass condition requires inference to identify a failing form. V-05 eliminates this inference requirement uniformly across all 31, making the artifact a complete detection instrument rather than a 23-criterion precise audit with an 8-criterion assumption layer.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Depth/behavior self-check parity: exact disqualifying forms for C-09-C-17 closing the asymmetry where structural criteria (C-18-C-27) had disqualifying-form precision but depth/behavior criteria carried only pass conditions", "Weight-class-complete verification trace: essential (C-01-C-05) and recommended (C-06-C-08) included in self-check with pass/fail and evidence, making the audit cover all 31 criteria rather than aspirational-only", "Table-format structural separation for essential/recommended entries (ID / Pass condition / Disqualifying form) making C-01-C-08 coverage visually distinct and absence structurally self-evident", "Uniform disqualifying-form treatment extended to all 31 criteria including essential/recommended beyond rubric minimum, eliminating the last class of criteria that required inference to identify a failing form"]}
```
