Now I have everything I need to score. The V-01 content starts mid-prompt (the file captures the Phase 2 registry table through Phase 5, with the PASS 1/PASS 2 Auditor/Skeptic structure visible). Scoring now.

---

## validate-consistency — Scorecard R1

**Date**: 2026-03-20
**Rubric version**: v1 (10 criteria: 60 essential / 30 recommended / 10 aspirational)

---

### Per-Criterion Evaluation

**C-01 — Registry populated, multi-location quantities flagged** (12 pts essential)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | Registry table has "Appears in N locations" column; example shows "2+ — flag for cross-check"; "Record ALL quantities, including those that appear only once" |
| V-02 | PASS | 2A sweep has YES/NO Cross-check? column with explicit examples; Phase 2E completeness gate reinforces it |
| V-03 | PASS | Step 2 requires marking each quantity MULTI or SINGLE |
| V-04 | PASS | Phase 2 instructs "Flag any quantity that appears in more than one location for cross-checking" |
| V-05 | PASS | Phase 2 table with "Cross-check?" column and multi-location flagging |

All PASS — 12/12 each.

---

**C-02 — Value consistency check (3A) is executed** (12 pts essential)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | 3A table in PASS 2 SKEPTIC: Location A / Value A / Location B / Value B / Consistent? |
| V-02 | PASS | Phase 3A with identical column structure |
| V-03 | PASS | Step 3 output: Location A / Value A / Location B / Value B / Pass/Fail |
| V-04 | PASS | Phase 3A table present |
| V-05 | PASS | Phase 3A table present |

All PASS — 12/12 each.

---

**C-03 — Inconsistency register present with severity labels** (12 pts essential)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | Phase 4 table: I-ID, Type, What conflicts, Severity, Fix required; "none found" row if empty |
| V-02 | PASS | Phase 4 table with P1/P2/P3 labels and "none found" row |
| V-03 | PASS | Step 7 table: I-ID, Type, What conflicts, Severity, Fix required; "none found" row |
| V-04 | PARTIAL | Replaces Phase 4 table with prose Finding blocks per inconsistency. All data fields are present (I-ID, severity, description, action) but the format is prose, not a table. Rubric requires a table — format deviation. |
| V-05 | PASS | Phase 4 table with I-ID, Type, Severity, Fix; "none found" row |

V-04: 6/12. Others: 12/12.

---

**C-04 — P1 issues correctly identified and not downgraded** (12 pts essential)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | "Severity rules — these are hard. The Skeptic does not negotiate them down." Plus "P1 — REJECT condition. No exceptions." Hard structural enforcement via Skeptic role mandate |
| V-02 | PARTIAL | P1 defined as "Different values for the same quantity, or two equations that provably disagree" but no explicit anti-downgrade mandate or structural enforcement. A model could still quietly relabel. |
| V-03 | PASS | "Do not relabel it P2 to soften it." Explicit instruction in the severity rule itself |
| V-04 | PARTIAL | Severity labeled "P1 — reject condition" in the Finding template but no hard prohibition on downgrading. Prose format forces writing both values, which helps, but no structural guard. |
| V-05 | PASS | Phase 4B Devil's Advocate review: every P1 downgrade must be documented with rebuttal or acceptance. "Do not silently remove it." Inertia warning triggers if all defenses are accepted. |

V-02, V-04: 6/12. Others: 12/12.

---

**C-05 — Frontmatter fields correct and counts match register** (12 pts essential)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | "p1_count and p2_count must match the actual count of rows in the register. Count them after Phase 4 is complete — do not carry forward from earlier." |
| V-02 | PASS | "quantities_checked = the total from Phase 2E (all registered quantities, not just the ones that were cross-checkable)" — explicit binding from a specific phase output |
| V-03 | PASS | Step 9: "Count: total quantities registered in step 2. Count: P1 entries in step 7. Count: P2 entries in step 7." — dedicated count step before frontmatter |
| V-04 | PASS | Phase 4B: "After writing all findings, count: P1 findings [n], P2 findings [n], Total quantities checked [n]. These numbers go directly into the frontmatter. Do not estimate them." |
| V-05 | PASS | "p1_count: [final count after Phase 4B], p2_count: [final count after Phase 4B]" — post-DA counts, prevents staleness from downgrade changes |

All PASS — 12/12 each.

---

**C-06 — All four check types (3A–3D) executed** (10 pts recommended)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | PASS 2 SKEPTIC has 3A, 3B, 3C, 3D — each with a table; 3D has explicit "none applicable" fallback |
| V-02 | PASS | Phase 3A, 3B, 3C, 3D all present; "If Phase 2D is empty, write: Phase 2D: no directional claims found — 3D not applicable." |
| V-03 | PASS | Steps 3–6 map exactly to 3A–3D; Step 6: "If the paper has no directional claims: write the table with 'none found.'" |
| V-04 | PASS | Phase 3A, 3B, 3C, 3D all present; "If any section has no applicable checks, write: [section] — none applicable." |
| V-05 | PASS | Phase 3A, 3B, 3C, 3D all present; "If no directional claims: '3D — none applicable.'" |

All PASS — 10/10 each.

---

**C-07 — Phase 5 amendments ordered and actionable** (10 pts recommended)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | "Ordered P1→P2→P3. Each fix: names exact section/table/equation, states correct value or form, does not say 'verify which is right'" |
| V-02 | PASS | "Ordered P1→P2→P3. One entry per severity level. Each entry: exact location to change + correct value or form." |
| V-03 | PASS | "Three or more targeted fixes, ordered P1→P2→P3. Each fix must: name the exact section/table/equation to change, and state the correct value or form. 'Verify which value is correct' is not a fix." |
| V-04 | PASS | "Names the exact location (section, table, equation number). States the correct value or form. Does not defer to the author to 'decide which is right'" |
| V-05 | PASS | "Each fix: exact location + correct value or form. Not 'verify which is right.'" |

All PASS — 10/10 each.

---

**C-08 — Equation consistency (3B) shows algebraic reasoning for FAIL** (10 pts recommended)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | "SKEPTIC RULE for 3B: a FAIL verdict must include the symbolic step. 'They differ' is not a verdict — it is a placeholder. Show the algebra." |
| V-02 | PASS | "For any FAIL row: show the algebraic step. Do not write 'they differ'." |
| V-03 | PASS | Step 4: "For any Fail row: do not write 'they differ.' Write the actual symbolic step that shows the discrepancy." |
| V-04 | PASS | Phase 3B column "If FAIL: algebraic step"; prose Finding template includes algebraic step slot as required format element |
| V-05 | PASS | "For any FAIL: show the algebraic step." |

All PASS — 10/10 each.

---

**C-09 — Boundary/limit checks (3C) include explicit evaluation steps** (5 pts aspirational)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | "SKEPTIC RULE for 3C: show the substitution. 'Setting dR/dt=0 in Eq. 7 gives...' — work it out. A reader must be able to verify your verdict without re-deriving." |
| V-02 | PASS | 3C column "Substitution: what you computed"; "Show the substitution for every row, pass or fail." |
| V-03 | PASS | Step 5: "write the substitution... For every row: write the substitution." |
| V-04 | PASS | 3C column "Substitution made"; prose Finding template includes substitution slot with worked example |
| V-05 | PASS | "For every row: show the substitution." |

All PASS — 5/5 each.

---

**C-10 — Single-location quantities registered as unverifiable** (5 pts aspirational)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | Registry example: "1 — single-location (unverifiable)"; "Mark single-location quantities explicitly — do not omit them." |
| V-02 | PASS | Rule: "If a quantity appears in only 1 location: mark Cross-check? = NO and annotate 'single-location — cannot cross-check'"; Phase 2E gate triggers re-sweep if 0 single-location found |
| V-03 | PASS | Step 2: each quantity gets "SINGLE" label; single-location quantities included by mandate |
| V-04 | PASS | "Mark quantities that appear only once as 'single-location — cannot cross-check.'" |
| V-05 | PASS | "Include single-location quantities with note 'single-location — cannot cross-check.'" |

All PASS — 5/5 each.

---

### Composite Scores

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | **Total** |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:---------:|
| V-01 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **100** |
| V-02 | 12 | 12 | 12 | 6 | 12 | 10 | 10 | 10 | 5 | 5 | **94** |
| V-03 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **100** |
| V-04 | 12 | 12 | 6 | 6 | 12 | 10 | 10 | 10 | 5 | 5 | **88** |
| V-05 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **100** |

---

### Ranking

| Rank | Variation | Score | All Essential Pass? | Notes |
|------|-----------|-------|---------------------|-------|
| 1 (tie) | V-01 | 100 | Yes | Strongest C-04 via Skeptic role mandate ("No exceptions"); hard role separation creates internal accountability |
| 1 (tie) | V-03 | 100 | Yes | Most structurally minimal; numbered imperatives with mandatory "none found" output per step eliminate skip paths |
| 1 (tie) | V-05 | 100 | Yes | Only variation with a post-register validation pass; DA mechanism is the strongest novel C-04 guard |
| 4 | V-02 | 94 | No (C-04 partial) | Phase 2E completeness gate is the best C-10/C-01 fix; loses 6 pts for no anti-downgrade enforcement |
| 5 | V-04 | 88 | No (C-03, C-04 partial) | Prose memo format is the most natural output for C-08/C-09 but fails the table format requirement in C-03 |

---

### Excellence Signals (from tied 100-score variations)

**V-03 contribution — Mandatory output per step regardless of result**
> "Do not skip steps. If a step yields no findings, write the output anyway and state 'none found.'"
The numbered imperative format makes the instruction structurally binding. Every section that could be skipped becomes a step with a required output line. This is the most transferable pattern: works without complex role framing.

**V-05 contribution — Named-defenses Devil's Advocate block**
> Lists the 4 standard author defenses, then requires rebuttal or documented acceptance for every P1 finding.
This is a novel mechanism for any skill where the primary failure mode is "charitable drift." The pattern generalizes: wherever a skill must hold a hard verdict against social pressure, a named-defenses block with required rebuttal is more robust than a stern instruction.

**V-01 contribution — Hard role instruction inside severity rules**
> "Severity rules — these are hard. The Skeptic does not negotiate them down."
Embedding the anti-downgrade mandate directly inside the severity definition (not in a preamble) means it fires at the moment of classification. Placement matters.

---

### Failure Mode Tally

| Failure mode | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 miss (incomplete flagging) | Fixed | Fixed | Fixed | Fixed | Fixed |
| C-04 miss (P1 downgraded) | Fixed | Unaddressed | Fixed | Unaddressed | Fixed |
| C-05 miss (stale frontmatter) | Fixed | Fixed | Fixed | Fixed (strongest) | Fixed |
| C-06 miss (missing 3D) | Fixed | Fixed | Fixed | Fixed | Fixed |
| C-08 miss (missing algebra) | Fixed | Fixed | Fixed | Fixed | Fixed |

V-02 and V-04 both leave C-04 structurally unaddressed. This is the only essential failure mode not caught by all variations.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["mandatory-output-per-step: each phase/step requires an output table or explicit none-found statement, removing the option to silently skip", "named-defenses-da-block: list standard author defenses and require rebuttal or documented acceptance before a P1 finding can be downgraded", "post-phase-explicit-count: a dedicated count step after the register phase, with direct frontmatter binding, prevents stale metadata"]}
```
