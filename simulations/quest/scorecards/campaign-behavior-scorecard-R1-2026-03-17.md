Now I have the full rubric (C-01–C-10) and all five complete variation prompts. Scoring each against the rubric.

---

# quest-score — campaign-behavior R1

**Rubric version:** v1 (2026-03-17)
**N_essential=5, N_recommended=3, N_aspirational=2**
**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
**Golden threshold:** all essential pass AND composite >= 80

---

## Per-Criterion Evaluation

### V-01 — Trace-first sequence

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 All five sub-skills | essential | PASS | trace-contract, trace-permissions, trace-state, flow-lifecycle, flow-conversation all listed with individual instructions |
| C-02 Ranked by blast radius | essential | PASS | "Ranked findings list (blast radius order, highest first)" — blast radius defined at end |
| C-03 Spec gaps | essential | PASS | Explicit "Spec gaps:" field in report structure with "or 'none found'" |
| C-04 Contract violations | essential | PASS | Explicit "Contract violations:" field with "or 'none found'" |
| C-05 Consolidated report | essential | PASS | "Synthesize into a single consolidated report. Do not concatenate five separate outputs." |
| C-06 Source attribution | recommended | PASS | Per-finding template is "[sub-skill source] \| finding \| blast radius rationale \| remediation direction" — source is first field |
| C-07 Remediation hint | recommended | PASS | "remediation direction" is explicit fourth field in per-finding template |
| C-08 Severity annotation | recommended | **FAIL** | Per-finding template: source \| finding \| blast radius rationale \| remediation — no severity tier. Blast radius rationale ≠ severity at epicenter |
| C-09 Cross-skill pattern | aspirational | PASS | "Cross-reference findings that appear in multiple sub-skills — these are systemic issues with higher blast radius" |
| C-10 Readiness verdict | aspirational | PASS | "Implementation readiness verdict: go / conditional-go / no-go with one-sentence rationale citing the highest-blast-radius finding or its absence" |

**Essential:** 5/5 → 60 pts
**Recommended:** 2/3 → 20 pts
**Aspirational:** 2/2 → 10 pts
**Composite: 90** | All essential: YES

---

### V-02 — Table-dominant format

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 All five sub-skills | essential | PASS | All five named with individual table sections; "Do not skip any sub-skill. Mark 'none' explicitly." |
| C-02 Ranked by blast radius | essential | PASS | "Ranked Findings (by blast radius, highest first)" table + definition block |
| C-03 Spec gaps | essential | PASS | "Spec Gaps" section with "or write: No spec gaps detected" |
| C-04 Contract violations | essential | PASS | "Contract Violations" section with "or write: No contract violations detected" |
| C-05 Consolidated report | essential | PASS | Campaign Summary + Ranked Findings + Spec Gaps + Verdict = single unified document |
| C-06 Source attribution | recommended | PASS | "Sub-skill" column in Ranked Findings table; also attributed structurally by per-sub-skill section headers |
| C-07 Remediation hint | recommended | PASS | "Remediation" column in Ranked Findings table |
| C-08 Severity annotation | recommended | PASS | "Severity \| high/med/low" column in both per-sub-skill table AND Ranked Findings consolidated table |
| C-09 Cross-skill pattern | aspirational | PASS | Dedicated "Cross-skill Findings" section: "label them explicitly" |
| C-10 Readiness verdict | aspirational | PASS | "Implementation Readiness Verdict" section with Verdict + Rationale format |

**Essential:** 5/5 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 2/2 → 10 pts
**Composite: 100** | All essential: YES

---

### V-03 — Imperative phrasing

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 All five sub-skills | essential | PASS | STEP 1–5 for all five; each step has a mandatory flag list |
| C-02 Ranked by blast radius | essential | PASS | "Rank every finding by blast radius. Blast radius = how many components or users break... Wide blast radius first." |
| C-03 Spec gaps | essential | PASS | "Spec gaps section: what the simulation exposed that the spec does not cover. Write 'none' if clean." |
| C-04 Contract violations | essential | PASS | "Contract violations section: mismatches between component promises. Write 'none' if clean." |
| C-05 Consolidated report | essential | PASS | "One report. Not five." — crisp and unambiguous |
| C-06 Source attribution | recommended | PASS | "Source sub-skill" is first item in per-finding template |
| C-07 Remediation hint | recommended | PASS | "What to fix" is fourth item in per-finding template |
| C-08 Severity annotation | recommended | **FAIL** | Per-finding template: Source \| What breaks \| Why blast radius is wide/narrow \| What to fix — no severity tier. "Why blast radius is wide/narrow" is scope rationale, not epicenter severity |
| C-09 Cross-skill pattern | aspirational | **FAIL** | SYNTHESIZE section does not instruct the model to look for cross-skill patterns. No cross-skill/systemic detection step |
| C-10 Readiness verdict | aspirational | PASS | "Verdict: go / conditional-go / no-go. One sentence. Name the finding that drove it or name its absence." |

**Essential:** 5/5 → 60 pts
**Recommended:** 2/3 → 20 pts
**Aspirational:** 1/2 → 5 pts
**Composite: 85** | All essential: YES

---

### V-04 — Combo: Trace-first + Table-dominant

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 All five sub-skills | essential | PASS | All five sections with typed tables (trace-contract, trace-permissions, trace-state, flow-lifecycle, flow-conversation) |
| C-02 Ranked by blast radius | essential | PASS | "Ranked Findings (blast radius order)" + definition: "Blast radius = how broadly a failure propagates... Wide blast radius = corrupts shared state..." |
| C-03 Spec gaps | essential | PASS | "Spec Gaps — Write 'none detected' if clean." |
| C-04 Contract violations | essential | PASS | "Contract Violations — Write 'none detected' if clean." |
| C-05 Consolidated report | essential | PASS | Campaign Summary + Ranked Findings + Spec Gaps + Cross-skill Findings + Verdict = single unified document |
| C-06 Source attribution | recommended | PASS | "Sub-skill" column in Ranked Findings table; each sub-skill has its own table section |
| C-07 Remediation hint | recommended | PASS | "Remediation" column in Ranked Findings table |
| C-08 Severity annotation | recommended | PASS | Ranked Findings table has "Severity" column; trace-contract sub-skill table also has "Severity" column. Consolidated view carries severity for all findings |
| C-09 Cross-skill pattern | aspirational | PASS | "Cross-skill Findings — Findings that appeared in two or more sub-skills. Label as SYSTEMIC." |
| C-10 Readiness verdict | aspirational | PASS | "Implementation Readiness Verdict — Verdict: go/conditional-go/no-go — Rationale: [one sentence — cite the highest-blast-radius finding or state none found]" |

**Essential:** 5/5 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 2/2 → 10 pts
**Composite: 100** | All essential: YES

---

### V-05 — Phase gates + Imperative + Blast radius upfront

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 All five sub-skills | essential | PASS | Five phases with ENTER/EXIT gates; EXIT CRITERIA requires "record findings or write 'no findings — phase N clean'" — gates structurally prevent skipping |
| C-02 Ranked by blast radius | essential | PASS | "Rank every finding by blast radius (wide first). Use the definition above." — with the definition placed BEFORE any sub-skill runs AND anti-confusion clause: "Do not substitute severity, priority, or frequency." |
| C-03 Spec gaps | essential | PASS | "SPEC GAPS: List every condition the simulation exposed that the spec does not address. Write 'none detected' if the spec covered every case." |
| C-04 Contract violations | essential | PASS | "CONTRACT VIOLATIONS: List every producer/consumer mismatch. Write 'none detected' if clean." |
| C-05 Consolidated report | essential | PASS | "Write ONE report. Not five. Synthesize across all phases. — CONSOLIDATE — do not skip this step" |
| C-06 Source attribution | recommended | PASS | "[phase/sub-skill source]" is the first field in the per-finding template |
| C-07 Remediation hint | recommended | PASS | "What must change to resolve it (one clear direction)" is the fifth field in the per-finding template |
| C-08 Severity annotation | recommended | PASS | "Severity at the epicenter: high / med / low" is the fourth field — and crucially, the prompt *names* the blast radius / severity distinction explicitly ("at the epicenter") |
| C-09 Cross-skill pattern | aspirational | PASS | "Identify any finding that appeared in two or more phases. Call it SYSTEMIC. Systemic findings rank higher than isolated findings of equivalent blast radius." — the ranking elevation rule goes beyond just labeling |
| C-10 Readiness verdict | aspirational | PASS | "VERDICT: go / conditional-go / no-go. One sentence rationale. Name the finding that drove it, or state that no blocking findings were detected." |

**Essential:** 5/5 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 2/2 → 10 pts
**Composite: 100** | All essential: YES

---

## Scorecard

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Essential | Recommended | Aspirational | **Composite** |
|-----------|------|------|------|------|------|------|------|------|------|------|-----------|-------------|--------------|---------------|
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 5/5 | 3/3 | 2/2 | **100** |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 5/5 | 3/3 | 2/2 | **100** |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 5/5 | 3/3 | 2/2 | **100** |
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | 5/5 | 2/3 | 2/2 | **90** |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | PASS | 5/5 | 2/3 | 1/2 | **85** |

All five reach golden threshold (all essential pass, composite >= 80). Three-way tie at 100.

---

## Three-Way Tie Differentiation (V-02 vs V-04 vs V-05)

All three satisfy every rubric criterion. Breaking the tie on above-rubric signal quality:

**V-02** — Table format forces attribution and blast radius to be machine-checkable. Per-sub-skill table includes Spec gap? and Contract violation? columns, enabling findings to be pre-tagged before consolidation. Weakness: blast radius definition is placed *after* sub-skill sections (before the ranked list), not before generation begins. Standard execution order (flow-first) means lifecycle gaps are found without a contract baseline.

**V-04** — Adds trace-first sequencing to V-02's table structure. Contracts and permissions are verified before lifecycle and conversation are simulated, giving flow-lifecycle a baseline to check against. The per-sub-skill tables have typed schemas (each table is purpose-built for its sub-skill's specific finding types). Weakness: blast radius definition still embedded mid-prompt rather than upfront.

**V-05** — Blast radius definition appears as a preamble *before any sub-skill runs*, making it the active ranking criterion during generation, not just during synthesis. EXIT CRITERIA gates guarantee no phase is partially executed. The C-09 implementation goes further than V-02/V-04: not just "label as SYSTEMIC" but "Systemic findings rank higher than isolated findings of equivalent blast radius" — a ranking refinement that could resolve ties in blast radius scoring. The per-finding template explicitly names both blast radius ("wide/medium/narrow — and why") AND severity ("at the epicenter") as distinct fields, matching the C-08 distinction at the template level rather than relying on the model to infer it.

**Recommended champion: V-05** — wins on generation-time anchoring (definition upfront), completeness guarantee (EXIT CRITERIA gates), and systemic ranking precision.

---

## Failure Patterns

**C-08 (Severity annotation) — failed by V-01 and V-03**

Pattern: Both use prose-based per-finding templates that list blast radius rationale but omit an explicit severity tier. Both prompts capture "why the blast radius is wide/narrow" but that answers the propagation scope question, not the epicenter damage question. The fix is structural: add `severity: high/med/low` as a named field in the per-finding template.

Root cause: **skill gap**, not rubric gap. The rubric correctly distinguishes blast radius from severity. The prompt designs that failed did not enforce that distinction in the output template.

**C-09 (Cross-skill pattern detection) — failed by V-03 only**

Pattern: V-03's SYNTHESIZE section does not instruct the model to look for cross-skill overlaps. Its imperative style strips all structural scaffolding, including the synthesis step that catches systemic issues.

Root cause: **skill gap**. Imperative style is effective for per-sub-skill rigor but loses the cross-skill synthesis instruction when structural scaffolding is eliminated. V-03 needs one imperative line in SYNTHESIZE: "Flag any finding that appeared in two or more steps as SYSTEMIC."

---

## Excellence Signals

Patterns from the top-scoring variations (V-02, V-04, V-05) that explain the 10–15pt gap over V-01 and V-03:

1. **Template fields enforce scoreable dimensions** — V-02/V-04/V-05 include an explicit `Severity` column in the findings table. V-01's prose template has four named fields; severity is not one of them. When the template names a field, the model fills it. When the field is absent, the model conflates blast radius with severity. Rule: every dimension in the rubric must appear as a named field in the output template.

2. **Structural section > prose instruction for optional content** — V-02/V-04 have a dedicated "Cross-skill Findings" section. V-01 has a prose instruction ("cross-reference findings that appear in multiple sub-skills"). Both address C-09, but a required section with an explicit header is harder to omit than a mid-paragraph instruction. V-03 has neither and fails C-09.

3. **Blast radius definition placement matters** — V-05 places the definition before any sub-skill runs. V-02/V-04 place it before the ranked list (post-generation). V-01 places it at the very end. Pre-generation placement means the ranking criterion is in context while findings are being generated, not just while they're being sorted.

4. **EXIT CRITERIA as completeness contract** — V-05's per-phase gates force explicit clean/findings declaration at each phase boundary. This eliminates implicit skipping and makes C-01 compliance structurally enforced rather than instructionally requested.

5. **Systemic elevation rule (V-05 only)** — "Systemic findings rank higher than isolated findings of equivalent blast radius" is a tie-breaking rule for the ranking function that the rubric implies but doesn't state. When two findings have the same blast radius width, the one corroborated by multiple sub-skills is more credible and should rank higher.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["template fields enforce scoreable dimensions — every rubric criterion needs a named field in the output template or models collapse adjacent dimensions (blast radius and severity were conflated in V-01/V-03 because severity had no template slot)", "structural section beats prose instruction for optional content — a required section header is harder to omit than a mid-paragraph cross-reference instruction", "blast radius definition placement: pre-generation anchoring (V-05) outperforms post-generation sorting (V-02/V-04) — definition should precede first sub-skill, not first ranking step", "EXIT CRITERIA gates make sub-skill completeness structurally enforced rather than instructionally requested", "systemic elevation rule — systemic findings should rank higher than isolated findings of equivalent blast radius, not just be labeled differently"]}
```
