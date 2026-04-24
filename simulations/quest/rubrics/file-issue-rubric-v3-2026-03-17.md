Written. Here is the complete rubric:

---

# file-issue -- Scoring Rubric v3

**Skill**: `file-issue`
**Rubric version**: v3
**Date**: 2026-03-17
**Applies to**: All `file-issue` golden and scored variations

---

## Essential Criteria (60% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Required fields captured** | coverage | essential | Skill collects all four required fields from the user: skill name, expected behavior, actual behavior, and severity. A skill that proceeds without all four fields is a fail. |
| C-02 | **Severity vocabulary enforcement** | format | essential | Skill enforces exactly the four-value severity enum: `crash`, `wrong-output`, `missing-feature`, `improvement`. Accepts no synonyms, free-text, or alternative values. On invalid input, rejects and re-prompts rather than proceeding. |
| C-03 | **GitHub issue format** | format | essential | Output is formatted as a GitHub issue: a title line following a `[{severity}] {skill}: {description}` pattern, plus a structured body with at minimum Expected / Actual / Steps / Context sections. Prose description without title/sections is a fail. |
| C-04 | **Artifact path under simulations/feedback/** | behavior | essential | Skill writes or clearly specifies an artifact path under `simulations/feedback/`. Path must be non-ambiguous (includes skill name and date or slug). |

---

## Recommended Criteria (30% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Actionable, specific issue title** | format | recommended | The GitHub issue title names the specific skill and the specific problem -- not generic phrases like "Bug report" or "Issue with skill". Pass: title contains skill name + symptom or behavior. |
| C-06 | **Sufficient reproducibility context** | depth | recommended | Body includes enough detail for a maintainer to reproduce or understand the issue: what input was given, what the environment was, or what sequence of events led to the problem. A one-sentence description alone is a fail. |
| C-07 | **Repo open offer presented** | behavior | recommended | Skill explicitly offers to open the issue at the Signal repo (e.g., asks the user if they want to open it, or provides a `gh issue create` command). |

---

## Aspirational Criteria (10% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Severity-appropriate framing** | depth | aspirational | Tone and urgency match severity: `crash` uses urgent language and asks for immediate reproduction steps; `improvement` uses constructive, proposal-oriented framing. |
| C-09 | **Skill context enrichment** | coverage | aspirational | Issue body includes at least one enriching context item beyond the four required fields: skill version or date, related skills in the invocation chain, topic name, or a reference to an existing rubric or golden artifact. |
| C-10 | **Pre-write validation gate** | structure | aspirational | Skill includes a structured check phase -- separate from drafting -- that verifies reproducibility, tone match, and field completeness before writing the artifact. The gate must block the write step; a post-write summary check does not qualify. *(Excellence signal: V-03 PHASE 3 -- VALIDATE.)* |
| C-11 | **Corrective actions per validation check** | structure | aspirational | Each validation check item includes an explicit corrective action specifying what the skill does on failure. A checklist of pass/fail conditions without prescribed remedies does not qualify. *(Excellence signal: V-04 STEP 3 table.)* |
| **C-12** | **Per-severity body templates** | structure | aspirational | Skill maintains four distinct body templates -- one per severity value -- that architecturally enforce severity-appropriate fields, tone, and required sections. The `crash` template includes priority and impact fields; the `improvement` template requires an acceptance condition. A single generic template with tone guidance does not qualify; template selection must determine structure, not just style. *(Excellence signal: V-04 full synthesis.)* |
| **C-13** | **Severity-labeled issue creation** | behavior | aspirational | The `gh issue create` command includes `--label "{severity}"` so the opened issue is immediately classified in the repo's label taxonomy. A bare `gh issue create` without `--label` does not qualify. *(Excellence signal: V-04 STEP 4 offer.)* |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

### Round 2 scores under v3

| Variation | Aspirational hits | Composite | Verdict |
|-----------|-------------------|-----------|---------|
| V-01 | C-08, C-09, C-10 (3/6) | **95.0** | Golden |
| V-02 | C-08, C-09, C-10, C-11 (4/6) | **96.7** | Golden |
| V-03 | C-08, C-09, C-10, C-11 (4/6) | **96.7** | Golden |
| V-04 | C-08–C-13 (6/6) | **100** | Golden |

---

**What changed v2 → v3:**

**C-12 — Per-severity body templates** (from V-04)  
Four distinct templates — one per severity value — that architecturally enforce the correct fields, tone, and structure. Tone compliance follows from template selection: a crash filed with improvement framing requires actively picking the wrong template. This is the strongest possible implementation of C-08, which required appropriate framing but allowed a single generic template to achieve it through guidance alone.

**C-13 — Severity-labeled issue creation** (from V-04)  
`gh issue create --label "{severity}"` connects the opened issue to the repo's label taxonomy at creation time. One-token addition, lasting organizational value. V-02 and V-03 offer `gh issue create` without the label flag and fail this criterion.

**Key finding from Round 2:** The C-10/C-11 isolation hypothesis was falsified. V-02's corrective-action table with a blocking instruction satisfied both simultaneously — they are co-dependent at the table level. The criteria remain distinct because each can be satisfied independently (V-01 passes C-10 without a table; a table without a blocking instruction passes C-11 without C-10), but a well-formed corrective-action table with an explicit blocking instruction satisfies both.
 titles are unfiled in practice.
- **C-06** distinguishes a useful bug report from a throwaway complaint.
- **C-07** verifies the skill follows through on its "offers to open" promise.
- **C-08/C-09** reflect maturity: a skill that calibrates tone to severity and enriches context produces issues that actually get fixed.
- **C-10** reflects structural maturity: a pre-write gate catches quality failures before they are committed to disk, rather than relying on post-hoc review. V-03's PHASE 3 -- VALIDATE demonstrated this pattern produces higher-confidence artifacts.
- **C-11** reflects operational maturity: prescribed corrective actions transform validation from a judgment into a procedure. V-04's STEP 3 table demonstrated that naming the fix alongside the check eliminates ambiguity about what the skill should do next.
- **C-12** reflects architectural maturity: per-severity body templates enforce correct structure and tone at the point of template selection, making wrong framing structurally impossible rather than merely discouraged. V-04's four-template design showed that tone compliance follows from template choice -- a crash filed with improvement framing requires actively picking the wrong template. This is the strongest possible implementation of C-08.
- **C-13** reflects integration maturity: severity labels on the opened issue connect it to the repo's label taxonomy, enabling maintainers to filter and triage by severity without manual relabeling. V-04's `gh issue create --label "{severity}"` demonstrated this as a one-token addition with lasting organizational value.

### Design note: C-10/C-11 co-dependence

Round 2 V-02 experiment falsified the isolation hypothesis: a corrective-action validation table with a blocking instruction necessarily satisfies both C-10 (structural gate) and C-11 (per-check corrective actions). The two criteria are co-dependent at the table level -- a table that names corrective actions and blocks the write step simultaneously satisfies both. This means a skill can pass both C-10 and C-11 without organizing around a named gate phase (as V-03 did). The criteria remain separate because a named phase gate can satisfy C-10 without a corrective-action table (V-01), and a corrective-action table can satisfy C-11 without a named gate phase -- co-dependence is only guaranteed when the table includes an explicit blocking instruction.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric -- 4 essential, 3 recommended, 2 aspirational (C-08/C-09) |
| v2 | 2026-03-17 | Added C-10 (pre-write validation gate) and C-11 (corrective actions per check) from Round 1 excellence signals; aspirational denominator updated from 2 to 4 |
| v3 | 2026-03-17 | Added C-12 (per-severity body templates) and C-13 (severity-labeled issue creation) from Round 2 excellence signals; aspirational denominator updated from 4 to 6 |
