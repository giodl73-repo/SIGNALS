# scout-inertia R10 — Quest Score Evaluation

## Score Summary

| Variation | Essential | Recommended | Aspirational (x/23) | **Total** |
|-----------|-----------|-------------|---------------------|-----------|
| V-01 | 60 | 30 | 21/23 = 9.13 | **89.13** |
| V-02 | 60 | 30 | 23/23 = 10.0 | **100.0** |
| V-03 | 60 | 30 | 23/23 = 10.0 | **100.0** |
| V-04 | 60 | 30 | 23/23 = 10.0 | **100.0** |
| V-05 | 60 | 30 | 23/23 = 10.0 | **100.0** |

**Ranking**: V-02 = V-03 = V-04 = V-05 > V-01

---

## Key C-30/C-31 Decisions

**C-30 (PASS for all five)**: Every variation adds explicit scope declarations — table "Governed sections" column (V-01/V-02/V-04/V-05) or prose "CONSTRAINT-N governs Section N:" prefix (V-03). C-30 is a low-resistance, format-invariant addition.

**C-31 (FAIL for V-01; PASS for V-02–V-05)**: V-01 deliberately keeps verbatim directives in section bodies → C-29 fails → C-31 fails. V-02–V-05 all place verbatim strings inside the manifest block (table column or prose body), satisfying all three co-residence requirements. V-03 resolves R10's primary discriminator question: **C-31 is format-agnostic** — prose manifest satisfies it.

**V-01 as controlled ablation**: Confirms C-29 is C-31's binding constraint. Preserving C-27/C-28/C-30 while removing C-29 breaks C-31 entirely.

---

## Excellence Signals (New Patterns)

1. **C-30 is format-invariant and low-resistance** — any manifest block achieves C-30 by appending a governed-site declaration per entry, regardless of prose or tabular format.
2. **C-31 is format-agnostic** — V-03 prose manifest establishes that co-residence (not table structure) is the requirement; labeled criterion prefixes + co-located verbatim strings in prose satisfy all three properties.
3. **C-29 is C-31's binding constraint** — verbatim co-location is the hardest property; moving reference strings into the manifest (rather than leaving them in governed sections) is the final step to triple convergence.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-30 scope annotation is format-invariant and low-resistance — achievable via explicit 'Governed sections' table column or 'CONSTRAINT-N governs Section N' prose prefix; any manifest block can add C-30 by appending one governed-site declaration per entry without restructuring the scaffold", "C-31 triple-constraint convergence is format-agnostic — V-03 prose manifest confirms that labeled criterion prefixes plus co-located verbatim strings in prose satisfy all three co-residence requirements; table structure is not required, only co-residence of the three properties in one identifiable block", "C-29 is C-31's binding constraint — V-01's controlled ablation (removes verbatim from manifest, preserves C-27/C-28/C-30) fails C-31 entirely, establishing verbatim co-location as the hardest and last property to achieve in triple convergence; moving reference strings into the manifest rather than leaving them in governed sections is the implementation burden"]}
```
 10 = **9.13**

**V-01 Total: 60 + 30 + 9.13 = 89.13**

---

### V-02 — SCAFFOLD MANIFEST table: criterion IDs + governed sections + verbatim directives in one pre-document block (targets C-30 + C-31)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | M-05 verbatim directive in manifest; section stub quotes M-05 and adds criterion question |
| C-02 Switching costs quantified | PASS | M-06 verbatim directive "'Significant' without a number fails C-02. Minimum 2 cost categories." |
| C-03 Threat score HIGH | PASS | M-07 verbatim directive "Default is HIGH. Deviation requires a specific quantified condition." |
| C-04 Why inertia loses | PASS | M-08 verbatim directive "'When they see value' fails. Each row cites FM-[N]..." |
| C-05 Failure modes identified | PASS | M-01 verbatim directive "MINIMUM 2 rows required. 'Manual is slow' fails..." |
| C-06 Dimensions separate | PASS | Section 3 four-row table with labeled categories |
| C-07 Forward-looking risk | PASS | Bridge Q3 references M-03 as "(closes C-05 → R-02)"; criterion-chain closure creates structural compounding-risk obligation |
| C-08 Adoption trigger conditions | PASS | Bridge Q4 references M-04 as "(closes C-05 → C-04)"; trigger-condition closure structural slot |
| **C-27 Constraint-before-site** | **PASS** | SCAFFOLD MANIFEST block appears before Section 1; lifecycle order declared immediately after manifest; all governed sections follow |
| **C-28 Criterion-ID-labeled scan** | **PASS** | Manifest "Criterion" column: C-05, A-16, Q3, A-16/A-19, C-01, C-02, C-03, C-04, A-19; completeness checklist uses C-01–C-05 IDs; section stubs quote manifest IDs as [M-01], [M-02] |
| **C-29 Manifest-bound verbatim directive** | **PASS** | "Verbatim directive — applies exactly at governed site" column contains quoted rejection strings for every entry: "MINIMUM 2 rows required...", "PRIMARY KEY CONSTRAINT...", "'Teams export data manually' fails...", etc. |
| **C-30 Manifest scope annotation** | **PASS** | "Governed sections" column present: "Section 1 — FM Inventory", "Sections 1 (source) and 5 (citation)", "Section 1 (Actor column), Section 3 (role attribution), Section 5 (team scoping)", etc. |
| **C-31 Triple-constraint convergence** | **PASS** | Single SCAFFOLD MANIFEST block: (1) precedes all governed sections (C-27), (2) "Criterion" column provides ID labels on every entry (C-28), (3) "Verbatim directive" column contains quoted canonical strings co-located with enforcement rules (C-29). All three properties co-resident in one block |

**Aspirational count**: 21/21 R9 baseline (inherited from R9 V-05 structure) + C-30 PASS + C-31 PASS = **23/23**

**Aspirational pts**: 23/23 × 10 = **10.0**

**V-02 Total: 60 + 30 + 10.0 = 100.0**

---

### V-03 — Prose STRUCTURAL MANIFEST with CONSTRAINT-[N] [criterion] labeled prefixes + verbatim conditions in prose body (tests C-30 prose form; tests C-31 format-agnosticism)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | CONSTRAINT-05 [C-01] governs Section 2; verbatim rejection string present in manifest prose |
| C-02 Switching costs quantified | PASS | CONSTRAINT-06 [C-02] governs Section 3; verbatim string: "Every estimate carries a number and a unit. 'Significant' without a number fails C-02." |
| C-03 Threat score HIGH | PASS | CONSTRAINT-07 [C-03] governs Section 4; verbatim string: "Deviation requires a specific quantified condition — not a qualitative judgment." |
| C-04 Why inertia loses | PASS | CONSTRAINT-08 [C-04] governs Section 5; verbatim string: "'When they see value' fails." |
| C-05 Failure modes identified | PASS | CONSTRAINT-01 [C-05] governs Section 1; verbatim rejection string present in manifest prose |
| C-06 Dimensions separate | PASS | Section 3 four-row table |
| C-07 Forward-looking risk | PASS | Bridge artifact Q3 labeled "closes C-05 → R-02"; CONSTRAINT-03 references Q3 closure |
| C-08 Adoption trigger conditions | PASS | Bridge artifact Q4 labeled "closes C-05 → C-04"; CONSTRAINT-04 references Q4 closure |
| **C-27 Constraint-before-site** | **PASS** | STRUCTURAL MANIFEST prose block appears before Section 1; all 8 CONSTRAINT entries are declared before any governed section |
| **C-28 Criterion-ID-labeled scan** | **PASS** | Each CONSTRAINT entry carries a labeled criterion bracket: [C-05], [A-16/A-19], [Q3 — closes C-05 → R-02], [Q4 — closes C-05 → C-04], [C-01], [C-02], [C-03], [C-04]; trailing completeness checklist uses C-01–C-05 IDs |
| **C-29 Manifest-bound verbatim directive** | **PASS** | Each CONSTRAINT entry in the STRUCTURAL MANIFEST includes a named verbatim string: "The verbatim rejection string is: '...'" or "The verbatim acceptance condition for deviation is: '...'" — canonical strings reside in the manifest prose body, not in governed sections |
| **C-30 Manifest scope annotation** | **PASS** | Every CONSTRAINT entry uses the pattern "CONSTRAINT-NN [criterion] governs Section N (section-name):" — scope is declared in the labeled prefix, not inferred from document order. Satisfies C-30 in prose form |
| **C-31 Triple-constraint convergence** | **PASS** | The STRUCTURAL MANIFEST is a single identifiable block: (1) pre-document (C-27), (2) criterion-ID labels on every entry via bracket notation [C-05], [A-16/A-19], etc. (C-28), (3) verbatim strings co-located inside each entry's prose body (C-29). **C-31 is format-agnostic**: the three properties can be co-resident in a prose block as well as a table |

**Aspirational count**: 21/21 R9 baseline + C-30 PASS + C-31 PASS = **23/23**

**Aspirational pts**: 23/23 × 10 = **10.0**

**V-03 Total: 60 + 30 + 10.0 = 100.0**

---

### V-04 — SCAFFOLD MANIFEST (C-30 + C-31) + [COMMAND] register + remediation-column bridge gate (dual-axis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | M-05 verbatim directive in manifest; [C-01 COMMAND — M-05] in section body back-references manifest |
| C-02 Switching costs quantified | PASS | M-06 verbatim directive; [C-02 COMMAND — M-06] + [UNIT RULE — M-06] |
| C-03 Threat score HIGH | PASS | M-07 verbatim directive; [C-03 COMMAND — M-07] |
| C-04 Why inertia loses | PASS | M-08 verbatim directive; [C-04 COMMAND — M-08] |
| C-05 Failure modes identified | PASS | M-01 verbatim directive; [C-05 COMMAND — M-01] |
| C-06 Dimensions separate | PASS | Section 3 four-row table |
| C-07 Forward-looking risk | PASS | [BRIDGE Q3 COMMAND — closes C-05 → R-02 — M-03] |
| C-08 Adoption trigger conditions | PASS | [BRIDGE Q4 COMMAND — closes C-05 → C-04 — M-04] |
| **C-27 Constraint-before-site** | **PASS** | SCAFFOLD MANIFEST precedes Section 1; lifecycle order declared immediately after manifest |
| **C-28 Criterion-ID-labeled scan** | **PASS** | Manifest "Criterion" column; section [COMMAND] headers carry M-XX back-references; completeness checklist uses C-01–C-05 IDs |
| **C-29 Manifest-bound verbatim directive** | **PASS** | "Verbatim directive — applies verbatim at governed site" column with quoted strings for all 9 entries |
| **C-30 Manifest scope annotation** | **PASS** | "Governed sections" column: "Section 1 — FM Inventory", "Sections 1 (source) and 5 (citation)", "Section 1 (Actor column), Section 3 (role attribution), Section 5 (team scoping)", etc. |
| **C-31 Triple-constraint convergence** | **PASS** | Single SCAFFOLD MANIFEST table: pre-document (C-27) + criterion-ID labels (C-28) + verbatim directives (C-29) all co-resident |

**V-04 additional strength**: Bridge gate carries remediation column with inline examples "(e.g., 'users' → 'data-ops team')" and "(e.g., 'sometimes' → 'file > 10MB')" — makes required remediation action explicit and checkable. "If N: action required" column in BRIDGE COMPLETION STATUS table adds prescriptive action path.

**Aspirational count**: 21/21 R9 baseline + C-30 PASS + C-31 PASS = **23/23**

**Aspirational pts**: 23/23 × 10 = **10.0**

**V-04 Total: 60 + 30 + 10.0 = 100.0**

---

### V-05 — All axes: SCAFFOLD MANIFEST (C-30 + C-31) + full [COMMAND] register + all-column inline examples extended + lifecycle declaration + extended bridge gate (maximum convergence)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | M-05 verbatim directive; [C-01 COMMAND — M-05] with full rejection string in section |
| C-02 Switching costs quantified | PASS | M-06 verbatim directive; [C-02 COMMAND — M-06] + [UNIT RULE — M-06] |
| C-03 Threat score HIGH | PASS | M-07 verbatim directive; [C-03 COMMAND — M-07]; Section 4 adds inline deviation example: "(e.g., 'switching cost < 2 days for teams < 5 engineers')" |
| C-04 Why inertia loses | PASS | M-08 verbatim directive; [C-04 COMMAND — M-08] |
| C-05 Failure modes identified | PASS | M-01 verbatim directive; [C-05 COMMAND — M-01] |
| C-06 Dimensions separate | PASS | Section 3 four-row table with Confidence level column and inline examples |
| C-07 Forward-looking risk | PASS | [BRIDGE Q3 COMMAND — closes C-05 → R-02 — M-03] |
| C-08 Adoption trigger conditions | PASS | [BRIDGE Q4 COMMAND — closes C-05 → C-04 — M-04] |
| **C-27 Constraint-before-site** | **PASS** | SCAFFOLD MANIFEST precedes Section 1 with full lifecycle order declaration |
| **C-28 Criterion-ID-labeled scan** | **PASS** | Manifest "Criterion" column; [COMMAND] headers carry M-XX back-references; criterion-code labeled rules [A-16 PRIMARY KEY RULE — M-02], [A-19 CITATION INTEGRITY RULE — M-09]; completeness checklist uses C-01–C-05 |
| **C-29 Manifest-bound verbatim directive** | **PASS** | "Verbatim directive — applies verbatim at governed site" column with quoted strings; M-04 verbatim includes extended clause: "Triggers without thresholds cannot generate falsifiable defeat conditions." |
| **C-30 Manifest scope annotation** | **PASS** | "Governed sections" column with complete site specifications; M-03/M-04 explicitly lists three governed sites each |
| **C-31 Triple-constraint convergence** | **PASS** | Single SCAFFOLD MANIFEST table satisfies all three co-residence requirements |

**V-05 additional strength over V-04**: Section 5 DC table extends all-column inline examples to defeat condition text "(e.g., 'FM-01 causes silent data loss for data-ops teams on files > 10MB')" and team type "(e.g., data-ops teams > 20 pipelines)" — two columns that V-04 leaves as headers only. Section 4 deviation justification column adds inline example. Bridge gate revision columns carry inline examples. Trigger column header in FM table uses more specific example "pipeline ingests file > 10MB".

**Aspirational count**: 21/21 R9 baseline + C-30 PASS + C-31 PASS = **23/23**

**Aspirational pts**: 23/23 × 10 = **10.0**

**V-05 Total: 60 + 30 + 10.0 = 100.0**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational (x/23) | **Total** |
|-----------|-----------|-------------|---------------------|-----------|
| V-01 | 60 | 30 | 21/23 = 9.13 | **89.13** |
| V-02 | 60 | 30 | 23/23 = 10.0 | **100.0** |
| V-03 | 60 | 30 | 23/23 = 10.0 | **100.0** |
| V-04 | 60 | 30 | 23/23 = 10.0 | **100.0** |
| **V-05** | **60** | **30** | **23/23 = 10.0** | **100.0** |

**Ranking**: V-02 = V-03 = V-04 = V-05 (100.0) > V-01 (89.13)

**Tiebreaker (V-02/V-03/V-04/V-05)**: All four achieve C-30 and C-31. Structural differentiation:
- V-05 and V-04 extend all-column inline examples to non-unit fields (defeat condition text, team type, deviation justification) — most comprehensive model guidance
- V-04 adds "If N: action required" column to bridge completion status — most prescriptive remediation path
- V-02 achieves the minimum tabular SCAFFOLD MANIFEST sufficient for C-30+C-31
- V-03 establishes that C-31 is format-agnostic (prose manifest sufficient)

---

## C-30/C-31 Resolution

**C-30 across all variations:**
All five variations satisfy C-30. V-01 through V-05 all include explicit "Governed sections" or "governs Section NN" declarations in their manifests. This confirms that C-30 scope annotation is a **low-resistance pattern** — it can be added to any manifest format (table column or prose prefix) without restructuring the scaffold.

**C-31 resolution — format-agnostic:**
V-03 is the key finding. Its prose STRUCTURAL MANIFEST satisfies C-31 without a table: labeled prefixes provide criterion IDs (C-28), verbatim strings reside in the manifest prose body (C-29), and the block precedes all governed sections (C-27). The rubric for C-31 requires co-residence, not table structure. **C-31 is format-agnostic.**

**V-01 as controlled ablation:**
V-01's deliberate exclusion of verbatim directives from the manifest block — while preserving C-27, C-28, and C-30 — breaks C-31. This confirms that **C-29 is C-31's binding constraint**: the hardest-to-achieve property in triple convergence is verbatim co-location of canonical strings with their enforcement directive inside the manifest itself.

---

## Excellence Signals from R10 Top Variations

**1. C-30 scope annotation is format-invariant and low-resistance**
Every variation adds C-30 at minimal structural cost. Whether via an explicit "Governed sections" table column (V-01/V-02/V-04/V-05) or an explicit "CONSTRAINT-NN governs Section NN:" prose prefix (V-03), the scope declaration satisfies C-30. The common property is declaration (the governed site is named in the manifest entry), not format. Any scaffold with a manifest block can add C-30 by appending one field per entry.

**2. C-31 is format-agnostic — co-residence, not table structure, is the requirement**
V-03 demonstrates that a prose manifest with labeled criterion prefixes and co-located verbatim strings satisfies all three triple-convergence properties simultaneously. The rubric's "one identifiable manifest block" does not require a table. This means C-31 is achievable without restructuring a prose-format scaffold — only adding criterion-ID labels and verbatim strings to each manifest entry is required.

**3. C-29 is C-31's binding constraint — verbatim co-location is the hardest property**
V-01's controlled design (removes verbatim directives from manifest, preserves C-27/C-28/C-30) fails C-31 entirely. This isolates C-29 as the property that breaks C-31 when absent. In practice: a scaffold can have pre-document placement (C-27) and criterion-ID labels (C-28) without satisfying C-31; adding verbatim directives to the manifest is the final step to triple convergence. The implementation burden of C-29 is higher because it requires moving reference strings INTO the manifest rather than leaving them in governed sections.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-30 scope annotation is format-invariant and low-resistance — achievable via explicit 'Governed sections' table column or 'CONSTRAINT-N governs Section N' prose prefix; any manifest block can add C-30 by appending one governed-site declaration per entry without restructuring the scaffold", "C-31 triple-constraint convergence is format-agnostic — V-03 prose manifest confirms that labeled criterion prefixes plus co-located verbatim strings in prose satisfy all three co-residence requirements; table structure is not required, only co-residence of the three properties in one identifiable block", "C-29 is C-31's binding constraint — V-01's controlled ablation (removes verbatim from manifest, preserves C-27/C-28/C-30) fails C-31 entirely, establishing verbatim co-location as the hardest and last property to achieve in triple convergence; moving reference strings into the manifest rather than leaving them in governed sections is the implementation burden"]}
```
