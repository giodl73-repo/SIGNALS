---
skill: quest-rubric
skill_target: scout-competitors
topic: plugin
date: 2026-03-14
version: 2
status: active
prior_version: scout-competitors-rubric-2026-03-14.md
changes: Added C-11 (inertia naming), C-12 (WebSearch instruction). C-07 clarified.
---

# Rubric: scout-competitors v2

---

## Criteria

### Essential (all must pass)

**C-01**: Matrix includes "none / status quo" as explicit competitor row -- UNCHANGED
**C-02**: Whitespace identified -- UNCHANGED
**C-03**: Table stakes listed -- UNCHANGED
**C-04**: Threat level per competitor -- UNCHANGED
**C-05**: Setup auto-detects without prompting -- UNCHANGED

### Recommended (2/3 should pass)

**C-06**: Inertia framed as the primary competition risk -- UNCHANGED

**C-07 (revised)**: Skill body explicitly instructs WebSearch use for claim verification
- Pass: Prompt body contains an explicit instruction to use WebSearch and cite a source
- Fail: WebSearch declared in tools but not explicitly instructed in the prompt body
- Note: This is a skill authoring criterion, not an output criterion. Evaluating the
  skill body, not the output.

**C-08**: --mode risk framing offered for exec audiences -- UNCHANGED

### Aspirational

**C-09**: GTM difficulty quantified per competitor -- UNCHANGED
**C-10**: Amend options specific and actionable -- UNCHANGED

**C-11 (new from ES-01)**: Inertia named as "The Primary Competitor" (or equivalent strong naming)
- Pass: The inertia row or section is explicitly titled "The Primary Competitor" or uses
  language that frames it as the dominant threat, not just one row among equals
- Fail: Inertia is a row but has the same visual weight as named competitors
- Source: ES-01 from Round 1 excellence signal extraction

**C-12 (new from ES-02)**: --mode risk is a named section in the findings structure
- Pass: The skill body includes "--mode risk" or "cost of not acting" as an explicitly
  named findings section or flag description
- Fail: Risk framing is implied but not instructed as a named output section
- Source: ES-02 from Round 1 excellence signal extraction

---

## Scoring (updated)

Essential: C-01 through C-05 (all must pass) = 60 points
Recommended: C-06 through C-08 (2/3 should pass) = 30 points
Aspirational: C-09 through C-12 (nice to have) = 10 points

Golden threshold: essential all pass + composite >= 85

---

## Rubric change log

| Version | Change | Source |
|---------|--------|--------|
| v1 | Initial -- 5E, 3R, 2A | Wave-1 + wave-2 trace findings |
| v2 | Added C-11 (inertia naming), C-12 (risk section naming). C-07 revised to skill-body criterion | Round 1 quest-score ES-01, ES-02 |
