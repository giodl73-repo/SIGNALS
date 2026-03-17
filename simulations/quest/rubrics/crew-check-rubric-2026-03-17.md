# crew-check Rubric v2

Evaluates crew-check skill outputs and prompt designs against correctness, behavioral compliance, depth, and coverage criteria.

---

## Essential Criteria (weight: 60 points total)

These must all pass for the output to be considered correct. Failure in any essential criterion means the output is structurally broken regardless of quality elsewhere.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Role source traceability | correctness | Every reviewer named in the output corresponds to a file present in `.craft/roles/`. The role name used in output must match the filename stem exactly. No invented or inferred role names are permitted. |
| C-02 | Review matrix structure | correctness | Output contains a structured list (table or labeled list) with all four required columns per row: **role**, **findings**, **severity**, **recommendation**. No column may be blank or missing for any reviewer row. |
| C-03 | Perspective fidelity | correctness | Each reviewer's findings are written from that role's orientation and lens -- not generic feedback that any role could have written. A PM finding differs in framing from an engineering finding from a security finding. |
| C-04 | Depth mode compliance | behavior | Standard mode: reviewer count is a subset selected for relevance to the artifact type. Deep mode (`--depth deep`): all roles in `.craft/roles/` are included. If depth is not specified, standard mode applies. Pass condition: the role count in the output is consistent with the mode used. |
| C-05 | Severity presence | correctness | Every finding row includes an explicit severity label. Acceptable label sets: critical/major/minor/info, high/medium/low, or equivalent. Mixed or absent severity is a fail. |

---

## Recommended Criteria (weight: 30 points total)

Output is materially better with these. Failure here does not block utility but reduces signal value.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Finding specificity | depth | Findings reference concrete details from the input artifact -- specific sections, fields, decisions, or behaviors. Generic observations ("this needs more testing") without artifact-specific grounding are a fail for that row. Pass if >= 80% of rows contain at least one artifact-specific reference. |
| C-07 | Recommendation actionability | depth | Each recommendation is specific enough to act on: it names what to change, add, remove, or verify. "Improve this" without direction is a fail for that row. Pass if >= 80% of rows contain an actionable recommendation. |
| C-08 | Severity calibration consistency | correctness | Severity labels are applied proportionally across rows. Critical is not assigned to stylistic issues; info is not assigned to blocking gaps. Pass if no obvious miscalibration exists (e.g., critical for a typo, info for a security hole). |

---

## Aspirational Criteria (weight: 10 points total)

Raise the bar once essential and recommended are stable. Five criteria at 2 points each.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-role synthesis | coverage | Output includes a synthesis section (or summary row) identifying convergent findings: themes where 2+ roles raised the same concern. At minimum: one convergent theme named with the roles that share it. |
| C-10 | AMEND responsiveness | behavior | When an AMEND instruction is present (add specific reviewer, change scope), the output correctly incorporates the amendment: new reviewer appears with a full row; scope change is reflected in which roles are included or excluded. Pass requires the amended output to differ from the un-amended output in the expected direction. |
| C-11 | Lens-anchoring step | depth | Before writing each reviewer's findings, the output or prompt explicitly anchors the lens: quotes or paraphrases one line from that role's `orientation.frame` or `lens.verify`. The anchor must be role-specific (not generic). Correlates directly with C-03 pass/fail -- variations lacking this step fail perspective fidelity for non-challenger roles. |
| C-12 | Severity calibration contract | correctness | The prompt or output defines the operational meaning of each severity level -- e.g., HIGH = blocks commit, MEDIUM = fix before ship, LOW = advisory. A label vocabulary alone (without definitions) does not satisfy this criterion. Pass requires at least one sentence per level specifying when that level applies. |
| C-13 | Challenger-first sequencing | behavior | The challenger archetype (null-hypothesis, skeptic) runs first in the reviewer sequence before other roles. This is the structural mechanism that semantically anchors the severity scale and prevents severity inflation across subsequent rows. Pass if the challenger role appears first in the output, or if the prompt mandates it. |

---

## Criterion Weights by Tier

| Tier | Criteria | Points Each | Total |
|------|----------|-------------|-------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 12 | 60 |
| Recommended | C-06, C-07, C-08 | 10 | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13 | 2 | 10 |
| **Total** | | | **100** |

---

## Scoring Worksheet

```
essential_pass   = count of C-01..C-05 that pass  (0-5)
recommended_pass = count of C-06..C-08 that pass  (0-3)
aspirational_pass = count of C-09..C-13 that pass (0-5)

composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

---

## Failure Pattern Reference

| Pattern | Likely failing criteria |
|---------|------------------------|
| Reviewer roles not from `.craft/roles/` | C-01 |
| Matrix missing severity or recommendation columns | C-02, C-05 |
| All reviewers sound identical | C-03, C-11 |
| Standard mode runs all roles / deep mode runs subset | C-04 |
| Findings are generic ("needs review") | C-06 |
| Recommendations are vague ("improve this") | C-07 |
| Critical assigned to minor issues | C-08, C-12 |
| No theme emerges from multi-role agreement | C-09 |
| AMEND instruction ignored | C-10 |
| Non-challenger roles lack differentiated voice | C-11 |
| Severity labels defined but not operationally grounded | C-12 |
| Severity inflation across rows | C-13 |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11 lens-anchoring step, C-12 severity calibration contract, C-13 challenger-first sequencing from R1 excellence signals; aspirational tier expanded to 5 criteria at 2 pts each |
