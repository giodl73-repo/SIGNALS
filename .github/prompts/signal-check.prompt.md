---
mode: agent
description: "Self-check your signals before committing. Analyzes all signal artifacts for a topic across 4 dimensions: SEQUENCE, COHERENCE, STALENESS, CAUSAL GAP."
---
You are running /signal-check for: {{topic}}

Self-check your signals before committing. Not punitive — coaching. Surfaces what looks
inconsistent so you can decide whether to address it before committing. Run before
/specify-commitment or any major decision.

---

## PHASE 1 — ARTIFACT INVENTORY

Glob `signals/**/*{{topic}}*` to find all signal artifacts for this topic.

| # | Artifact | Skill | Date | Namespace |
|---|----------|-------|------|-----------|
| 1 | | | | |

If fewer than 3 artifacts found: note sparse coverage but continue. Signal-check works
with whatever exists.

---

## PHASE 2 — SEQUENCE

Did you discover before specifying? Did you specify before validating?

Expected order (not enforced, but deviations get flagged):
discover → specify → validate/simulate → prove

| Check | Result | Artifacts |
|-------|--------|-----------|
| Discovery before specification? | [YES / OUT-OF-ORDER / N/A] | [artifact names] |
| Specification before validation? | [YES / OUT-OF-ORDER / N/A] | [artifact names] |
| Any validation run before discovery? | [YES (flag) / NO] | |

Out-of-order is not always wrong — flag it, don't block it. The user ran /simulate-lifecycle
on a design question during QA? That's fine. Record it as intentional cross-namespace flow
if the context supports it.

---

## PHASE 3 — COHERENCE

Do your signals agree with each other?

For each pair of artifacts that address overlapping concerns:

| Artifact A | Artifact B | Agreement | Tension | Resolution needed? |
|------------|------------|-----------|---------|-------------------|
| | | AGREE / DISAGREE / ORTHOGONAL | [describe if DISAGREE] | [YES / NO] |

Coherence failures worth flagging:
- Risk identified in discover but absent from spec
- Spec claims a capability that validation found missing
- Two reviews give opposite severity to the same concern
- Echo surprise contradicts a spec assumption still in force

---

## PHASE 4 — STALENESS

Are signals recent enough to trust?

For each artifact:

| # | Artifact | Date | Age (days) | References code? | Code changed since? | Status |
|---|----------|------|------------|-----------------|---------------------|--------|
| 1 | | | | [YES / NO] | [YES / NO / N/A] | CURRENT / STALE / UNVERIFIABLE |

### Staleness detection

For artifacts that reference code files or specific findings:
- Check `git log --since={artifact-date} -- {referenced-files}` for changes
- If referenced code has changed since the artifact date: mark STALE
- If the artifact carries findings (P1/P2/P3) that reference specific code: check whether
  each finding's referenced file/line has been modified

### PRE-IMPLEMENTATION detection

| Artifact | Contains findings about code that didn't exist at artifact date? | Marker |
|----------|----------------------------------------------------------------|--------|
| | [YES / NO] | [PRE-IMPLEMENTATION / POST-IMPLEMENTATION / N/A] |

Artifacts created before implementation that carry design-phase findings should be marked
PRE-IMPLEMENTATION. These are valid as historical record but should not be treated as
current state by downstream consumers.

### Staleness summary

```
Total artifacts: N
CURRENT: N  |  STALE: N  |  UNVERIFIABLE: N  |  PRE-IMPLEMENTATION: N
```

If STALE > 0: list which skills should be re-run to refresh.

---

## PHASE 5 — CAUSAL GAP

Do you have evidence for the mechanism linking feature to outcome?

For each claim in spec or proposal artifacts:

| Claim | Evidence artifact | Mechanism described? | Gap? |
|-------|-------------------|---------------------|------|
| [feature X leads to outcome Y] | [artifact or "none"] | [YES / NO] | [COVERED / GAP] |

A causal gap means: you asserted a link between feature and outcome but no signal artifact
contains evidence for the mechanism. Not every claim needs causal backing — flag gaps,
don't block on them.

---

## PHASE 6 — SYNTHESIS

```
Topic: {{topic}}
Artifacts checked: N
Sequence: [OK / N flags]
Coherence: [OK / N tensions]
Staleness: [N CURRENT / N STALE / N PRE-IMPLEMENTATION]
Causal gaps: [N gaps]

Overall: READY / REVIEW-RECOMMENDED / STALE-SIGNALS
```

### Recommended actions

| Priority | Action | Why |
|----------|--------|-----|
| 1 | | |
| 2 | | |
| 3 | | |

---

Write artifact to: signals/signal-check/{{topic}}-signal-check-{{date}}.md

Frontmatter:
```
skill: signal-check
topic: {{topic}}
date: {{date}}
artifacts_checked: {N}
stale_count: {N}
coherence_tensions: {N}
causal_gaps: {N}
verdict: {READY / REVIEW-RECOMMENDED / STALE-SIGNALS}
```

AMEND: re-run after refreshing stale artifacts to verify staleness resolved.
