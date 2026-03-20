---
mode: agent
description: "Run the full design validation campaign. Orchestrates: review-design, review-users, review-customers, listen-feedback, l"
---
confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


You are running /rhythm-qa for: {{topic}}

Run the full design validation campaign. Orchestrates validate-design, validate-users, validate-customers, validate-feedback, and validate-adoption in sequence. Produces a validation brief ranking findings by adoption impact.

DISPLAY ONLY for the campaign coordination — sub-skills write their own artifacts.

---

## STEP 1 -- SIGNAL CHECK

Glob: signals/**/{topic}-spec* or signals/**/{topic}-design*
If no spec or design artifact exists: "No spec or design artifact found for {{topic}}. Run /specify-spec {{topic}} first."
Stop.

---

## STEP 2 -- CAMPAIGN (run each sub-skill in sequence)

**validate-design {{topic}}**
Question: Does this design hold under expert review?
Key output: reviewer count, P1 blockers, verdict

**validate-users {{topic}}**
Question: Does this design match user mental models?
Key output: blocking usability issues, worst persona experience

**validate-customers {{topic}}**
Question: Will paying customers adopt this?
Key output: top adoption blocker, willingness-to-pay signal

**validate-feedback {{topic}}**
Question: What will users say in the first 30 days?
Key output: aggregate NPS prediction, top blocking theme

**validate-adoption {{topic}}**
Question: How does adoption curve across all team archetypes?
Key output: laggard blocking condition, time-to-full-adoption estimate

---

## STEP 3 -- VALIDATION BRIEF

```
VALIDATION BRIEF: {{topic}}
================================
P1 Blockers (ship-stopping):
  [from validate-design / validate-users]
  ...

Top Adoption Risk: [single biggest barrier]
Predicted NPS at 30 days: [aggregate]
Fastest win: [fix that unblocks the most users]

Verdict: VALIDATED / VALIDATE-WITH-CONDITIONS / NOT VALIDATED
```

---

## STEP 4 -- NEXT RECOMMENDED

2 skills that would most improve confidence:
  -> /[skill] {{topic}}   [gap it closes]
  -> /[skill] {{topic}}   [gap it closes]