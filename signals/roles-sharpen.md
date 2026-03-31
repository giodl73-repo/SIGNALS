source: {path}
# Path to a postmortem, completion log, or topic-echo artifact.
# If not provided, glob for the most recent topic-echo or postmortem in signals/.

---

## PHASE 1 — EXTRACT FAILURE CLASSES

Read the source document. Extract each distinct failure class — a category of thing that
went wrong or was missed during execution.

| # | Failure class | Description | Source section |
|---|---------------|-------------|----------------|
| FC-1 | | [what went wrong, one sentence] | [section or line reference] |

Failure classes are structural, not individual bugs.

---

## PHASE 2 — MAP TO ROLES

Glob `.craft/roles/**/*.md` to load all installed roles.

For each failure class, identify which role SHOULD have caught it by matching against:
- `expertise.depth` — does the role claim knowledge in this area?
- `expertise.relevance` — does the role fire on artifacts where this failure appeared?
- `lens.verify` — do existing checks come close but miss the specific failure?

| FC # | Mapped role | Match basis | Current closest verify check | Gap |
|------|-------------|-------------|------------------------------|-----|
| FC-1 | | depth / relevance / verify | [existing check or "none"] | [what's missing] |

---

## PHASE 3 — PROPOSE VERIFY CHECKS

For each mapped failure class, write the new verify check.

| FC # | Role | Proposed verify check | Rationale |
|------|------|-----------------------|-----------|
| FC-1 | | [the check, in lens.verify style] | [why this catches the failure class] |

Each check must be: specific, scoped to the role's tension, actionable, non-redundant.

---

## PHASE 4 — APPLY

Read each role file, append new checks to lens.verify, write updated file.

---

Write artifact to: signals/roles/sharpen/{topic}-roles-sharpen-{date}.md

Frontmatter:
```
skill: roles-sharpen
topic: {topic}
date: {date}
source: {path}
failure_classes: {N}
roles_sharpened: {N}
checks_added: {N}
```

AMEND: re-run with a different source document.
