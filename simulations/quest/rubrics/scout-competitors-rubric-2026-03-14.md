---
skill: quest-rubric
skill_target: scout-competitors
topic: plugin
date: 2026-03-14
version: 1
status: initial
---

# Rubric: scout-competitors v1

Scoring criteria for evaluating scout-competitors output quality.
Built from: wave-1 trace findings + wave-2 trace findings + spec amendments.

---

## Criteria

### Essential (must pass -- output is not useful without these)

**C-01**: Matrix includes "none / status quo" as an explicit competitor row
- Pass: A row labeled "None (inertia)", "Status quo", or equivalent appears in the matrix
- Fail: All rows are named tools/companies; no inertia row

**C-02**: Whitespace identified -- at least one space where no competitor has solved the problem
- Pass: A whitespace finding is explicitly stated (e.g., "No tool owns pre-build investigation in Claude Code")
- Fail: Matrix without whitespace analysis, or only "crowded zones" identified

**C-03**: Table stakes listed -- features the product must have to be taken seriously
- Pass: A "table stakes" or "must have" list appears with 2+ items
- Fail: No table stakes listed

**C-04**: Threat level assessed per competitor (HIGH/MEDIUM/LOW or equivalent)
- Pass: Each competitor row includes a threat assessment
- Fail: Matrix has no threat column or equivalent; reader cannot prioritize

**C-05**: Setup auto-detects from repo context without requiring user prompting
- Pass: Setup describes what was auto-detected (domain, product category, competitors identified)
- Fail: Setup asks the user for domain information that was available in repo context

---

### Recommended (output is better with these -- rubric grows here via quest-golden)

**C-06**: Inertia framed as the primary competition risk, not just a matrix row
- Pass: A finding, section, or finding narrative explicitly addresses "why teams do nothing" as the primary threat
- Fail: Inertia row exists but is not discussed in findings; matrix without narrative

**C-07**: WebSearch or external verification cited for at least one competitor claim
- Pass: At least one competitor feature claim includes a source reference or search evidence
- Fail: All competitor claims are from training data with no external verification noted

**C-08**: --mode risk flag or equivalent reframing offered for exec audiences
- Pass: The output either used --mode risk, OR the findings section includes a "cost of not acting" framing
- Fail: Output is purely a competitive matrix with no ROI/risk framing for non-developer audiences

---

### Aspirational (raise the bar once essential and recommended are stable)

**C-09**: GTM difficulty quantified per competitor (distribution, sales cycle, competitive intensity)
- Pass: Each competitor has a GTM difficulty assessment beyond just "market position"
- Fail: No GTM-specific assessment per competitor

**C-10**: Amend options are specific and actionable
- Pass: 3+ amend options listed, each with a concrete adjustment AND what would change in the output
- Fail: Amend options are generic ("add more competitors") without specifying impact

---

## Scoring

| Weight | Criteria |
|--------|----------|
| Essential | C-01 through C-05 (all must pass) |
| Recommended | C-06 through C-08 (2/3 should pass) |
| Aspirational | C-09 through C-10 (nice to have) |

Composite score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
Maximum: 100. Golden threshold: essential all pass + composite >= 80.

---

## Rubric change log

| Version | Change | Source |
|---------|--------|--------|
| v1 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational | Wave-1 + wave-2 trace findings |
