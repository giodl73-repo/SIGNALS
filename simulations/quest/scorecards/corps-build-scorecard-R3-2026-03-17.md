## Quest Score — corps-build Round 3

### Scoring Approach

Each criterion scored PASS / PARTIAL / FAIL based on prompt design strength:
- **PASS** = requirement stated with enforcement mechanism (verification loop, invariant check, or demonstration)
- **PARTIAL** = requirement stated without enforcement (relies on model compliance without verification)
- **FAIL** = requirement absent or only implied

PARTIAL counts as 0.5 in composite formula.

---

## V-01 — Example-Driven

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PARTIAL | "Total must equal count of files written in Step 2" stated but no count verification loop or explicit check statement. Variate's own hypothesis flags this as its weakest axis. |
| C-02 | PASS | Concrete ASCII example using `+--`/`|` provided before instructions; format ambiguity eliminated at source. |
| C-03 | PASS | "Mandatory, one per team, no exceptions" + full IA example file. Clear imperative with demonstration. |
| C-04 | PASS | Path pattern `.roles/{area-slug}/{role-slug}.md` + example files make directory fidelity concrete. |
| C-05 | PASS | Example role files show all five fields with substantive bodies; "use the example above as the quality bar" is an explicit calibration anchor. |
| C-06 | PASS | Headcount table example with exact column structure including Levels column. |
| C-07 | PASS | `role-type: standard` in example frontmatter; step sequence explicitly names standard/specialized/IA order. |
| C-08 | PASS | AMEND block present with three named options (specific area, level term, group node). |
| C-09 | PASS | Explicit instruction: "lens and expertise must reference this specific team's declared domain" + IA example demonstrates domain-specificity over generic resistance. |
| C-10 | PARTIAL | Table total = file count stated but no explicit check statement ("MATCH/MISMATCH" pattern absent). |

**essential_pass**: 4.5 / 5 → 54 pts  
**recommended_pass**: 3 / 3 → 30 pts  
**aspirational_pass**: 1.5 / 2 → 7.5 pts  
**Composite: 91.5** → **92**

---

## V-02 — Constraint-First

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | INVARIANT-1 declared at top; "confirm INVARIANT-1: count files written. If count does not match parse manifest total, identify the gap before proceeding." Explicit verification with resolution requirement. |
| C-02 | PASS | INVARIANT-2 declared at top; "after drawing, state: INVARIANT-2 CHECK: [n] areas in hierarchy, [n] areas in manifest — [MATCH | MISMATCH]." Mandatory post-write check. |
| C-03 | PASS | INVARIANT-3 declared at top; "INVARIANT-3 enforcement: do not close a team's file set without the IA file." Team-level closure gate. |
| C-04 | PASS | INVARIANT-4 declared; "INVARIANT-4 enforcement: before writing the first file for any team, confirm `.roles/{area-slug}/` is correct path derived from `org.yaml`." Pre-write path validation. |
| C-05 | PASS | INVARIANT-5 declared at top + field descriptions in Step 2 body. Declared at model's entry point. |
| C-06 | PASS | Headcount table with explicit column structure including Levels column + coverage notes section. |
| C-07 | PASS | Frontmatter sequence (standard → specialized → IA) explicit in Step 2; `role-type` in frontmatter required. |
| C-08 | PASS | AMEND block with three options; options reference named invariants (INV-1, INV-3, INV-4, INV-5) for area regeneration. |
| C-09 | PASS | "Lens and expertise must be drawn from this specific team's declared domain vocabulary. An IA whose lens reads 'resistance to change in general' violates INVARIANT-5." Named failure mode. |
| C-10 | PASS | "INVARIANT-1 FINAL CHECK: table Total = [n], files written = [n] — [MATCH | MISMATCH]" explicit cross-reference check statement. |

**essential_pass**: 5 / 5 → 60 pts  
**recommended_pass**: 3 / 3 → 30 pts  
**aspirational_pass**: 2 / 2 → 10 pts  
**Composite: 100**

---

## V-03 — Minimal Imperative

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PARTIAL | Parse summary provides per-team role count but no total count check and no gap-resolution step. Hypothesis correctly predicts this as a likely failure axis. |
| C-02 | PASS | "`+--` and `|`" specified; "all names verbatim"; two nesting levels required. Clear format requirement even without example. |
| C-03 | PASS | "Every team must have an Inertia Advocate (`role-type: inertia-advocate`)" — direct imperative. |
| C-04 | PASS | Path `.roles/{area-slug}/{role-slug}.md` explicit; after-teams paths for shared/exec-office stated. |
| C-05 | PASS | Five fields listed with content descriptions ("concrete systems or decisions," "named system or practice"). |
| C-06 | PASS | Headcount table structure provided with Total row and Levels column. |
| C-07 | PASS | `role-type` and `area` in frontmatter; standard/specialized/IA sequence stated. |
| C-08 | PASS | "Close with an AMEND section offering three specific options" — all three present with named targets. |
| C-09 | PARTIAL | "The IA's lens and expertise must name this team's specific domain, not generic resistance" — stated but no example, no verification, no named failure mode. |
| C-10 | PARTIAL | Total row present in table template but no explicit "table total = file count" statement and no check notation. |

**essential_pass**: 4.5 / 5 → 54 pts  
**recommended_pass**: 3 / 3 → 30 pts  
**aspirational_pass**: 1 / 2 → 5 pts  
**Composite: 89**

---

## V-04 — Constraint-First + Example-Driven

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | INVARIANT-1 declared + "Confirm INVARIANT-1: count files after all writes. If count does not equal parse manifest total, identify and resolve the gap before Step 3." |
| C-02 | PASS | INVARIANT-2 declared + example hierarchy showing exact `+--`/`|` format for a 2-team org. Dual enforcement. |
| C-03 | PASS | INVARIANT-3 declared + "Apply INVARIANT-3 before closing each team: if the IA file is not yet written, write it before moving to the next team." |
| C-04 | PASS | INVARIANT-4 declared + "Apply INVARIANT-4 by writing only to subdirectories declared in the parse manifest." |
| C-05 | PASS | INVARIANT-5 declared + example files show all five fields at target quality. "Use the example files above as the quality bar for field depth." Best enforcement on this criterion. |
| C-06 | PASS | Example headcount table with exact columns + instructions replicate the structure. |
| C-07 | PASS | `role-type: standard` in example frontmatter; sequence explicit; specialized F-2 requirement called out separately ("should not be possible to copy this F-2 into a standard role file without changing it"). |
| C-08 | PASS | AMEND block with three options; area regeneration references invariant re-checks INV-1, INV-3, INV-5. |
| C-09 | PASS | Example IA file shows domain-specific lens/expertise + explicit instruction using the example's domain vocabulary as the bar. Strongest enforcement on C-09 of any single-axis variation. |
| C-10 | PASS | "Final INVARIANT-1 check: `Table Total = [n], files written = [n] — [MATCH | MISMATCH]`" explicit cross-reference. |

**essential_pass**: 5 / 5 → 60 pts  
**recommended_pass**: 3 / 3 → 30 pts  
**aspirational_pass**: 2 / 2 → 10 pts  
**Composite: 100**

---

## V-05 — Constraint-First + Schema-as-Contract + Coverage Audit

| ID | Result | Evidence note |
|----|--------|---------------|
| C-01 | PASS | INVARIANT-1 + audit [A] checks file count explicitly with required/written comparison + INVARIANT-1 FINAL CHECK in Step 4. Three-layer enforcement. |
| C-02 | PASS | INVARIANT-2 + "INVARIANT-2 CHECK: [n] areas drawn, [n] areas in manifest — [MATCH | MISMATCH]" in Step 4. |
| C-03 | PASS | INVARIANT-3 + audit [B] checks IA presence per team by name before org-chart.md is written. |
| C-04 | PASS | INVARIANT-4 + audit [C] checks directory fidelity with extra-directory detection. Most thorough structural check of any variation. |
| C-05 | PASS | INVARIANT-5 + schema table F-1..F-5 with per-field content requirements + audit [D] spot-check. Schema names failure modes explicitly ("'Technical perspective' fails. 'Schema migration cost at >10M rows' passes."). |
| C-06 | PASS | Headcount table with level distribution note; "if levels declared in org.yaml, show breakdown by level label." |
| C-07 | PASS | Category A/B/C framing makes standard/specialized distinction structural rather than instructional. Specialized F-2 must be unduplicated from standard roles — strongest enforcement on type distinction. |
| C-08 | PASS | STEP 5 AMEND with three options; area regeneration re-runs audit checks [A]-[E] scoped to that area. |
| C-09 | PASS | Audit [E] checks IA domain-vocabulary uniqueness: "no two IA files may share identical F-2 or F-3 body text." PASS enforced by resolution gate ("differentiate before continuing to the next team"). Strongest enforcement on C-09 across all variations. |
| C-10 | PASS | Audit [A] count check + "INVARIANT-1 FINAL CHECK: Table Total = [n], audit [A] written = [n]." Dual-layer cross-reference. |

**essential_pass**: 5 / 5 → 60 pts  
**recommended_pass**: 3 / 3 → 30 pts  
**aspirational_pass**: 2 / 2 → 10 pts  
**Composite: 100**

---

## Composite Summary and Ranking

| Rank | Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Composite | All Essential |
|------|-----------|------|------|------|------|------|------|------|------|------|------|-----------|---------------|
| 1 (tie) | V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** | YES |
| 1 (tie) | V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** | YES |
| 1 (tie) | V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** | YES |
| 4 | V-01 | PARTIAL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | **92** | NO (partial) |
| 5 | V-03 | PARTIAL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PARTIAL | **89** | NO (partial) |

**Tie-break within the 100s**: V-05 > V-04 > V-02 by enforcement depth on C-09 (audit [E] uniqueness gate) and C-10 (dual-layer cross-reference). V-04 > V-02 because the worked example anchors C-05 and C-09 quality more concretely than field descriptions alone.

**Control result (V-03)**: The minimal prompt reaches 89 and passes all essentials at PASS or PARTIAL. It does not fail C-03 as the hypothesis anticipated — the imperative "every team must have an Inertia Advocate" was sufficient for that criterion. The actual failures are on the enforcement criteria (C-01 counting, C-09 IA specificity, C-10 cross-reference) — the criteria where R1/R2 structure adds measurable value. **Conclusion: R1/R2 structure is partially load-bearing, but only for completeness verification and aspirational depth — not for the essential format and structural criteria.**

---

## Excellence Signals

Top variation: **V-05**, differentiated by:

1. **Coverage audit as verification gate** — running the audit *before* writing org-chart.md creates a hard blocking step where any completeness gap is surfaced and resolved while role files are still the active context. This is structurally different from a post-hoc check: the model cannot proceed to the output artifact without an explicit AUDIT RESULT: PASS. V-02 and V-04 have check statements, but they don't gate the next step.

2. **Constraint-first as activation framing** — declaring invariants at the very top of the prompt means the model reads "INVARIANT-3: every team node must have an inertia-advocate.md" before reading how to write role files. The invariant is active during write decisions, not discovered at review. This distinguishes V-02/V-04/V-05 from V-01 (example only) and explains V-01's gap on C-01/C-10.

3. **IA uniqueness as a differentiability gate** — audit [E] makes it a verifiable, blocking condition that no two IA files share identical F-2 or F-3 text, with a resolution gate ("differentiate before continuing to the next team"). This is the only variation that converts the aspirational C-09 criterion into a verification step with an explicit fail condition. Generic IA content cannot survive this check.

**R3's distinguishing finding**: constraint-first framing is the dominant new addition — it is the common thread in all three 100-scoring variations (V-02, V-04, V-05) and absent from the two variations that fell short (V-01: no invariants on C-01/C-10; V-03: no invariants anywhere). The example axis (V-01) provided strong quality anchoring but did not add completeness enforcement; its contribution is best understood as a *quality* lever (C-05, C-09) rather than a *completeness* lever (C-01, C-10).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["constraint-first invariant declaration activates model compliance during writes rather than as post-hoc review — invariants read before steps are active during every write decision", "worked example as quality anchor eliminates format and field-depth ambiguity through demonstration — stronger than prose descriptions for C-02 and C-05", "IA uniqueness audit gate converts aspirational domain-contextualization into a verifiable blocking condition — no two IA files may share identical lens or expertise text before the output artifact is written"]}
```
