# listen-support Round 14 -- Skill Body Prompt Variations

**Written to**: `simulations/quest/rubrics/listen-support-rubric-v13-variate-R14-2026-03-15.md`

---

## Coverage matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-36 exception paraphrase-clause field | YES | YES | YES | YES | YES |
| C-37 verbatim anchor at Step 4 | YES | YES | YES | YES | YES |
| C-38 dual-field "both lines" gate | YES | YES | YES | YES | YES |
| C-39 every-assignment scope confirmation | YES | YES | -- | YES | YES |
| C-40 verbatim instruction in exception block | YES | YES | YES | YES | YES |
| C-41 imperative dual-field gate language | YES | YES | -- | YES | YES |

---

## Variation axes selected

| # | Variation | Axis | Drops | Expected score |
|---|-----------|------|-------|----------------|
| V-01 | C-40 Direct Fix | Exception block verbatim instruction tightening | nothing | 255/255 |
| V-02 | Numbered Checklist Format | Output format -- numbered items replace fenced code block at Step 4 | nothing | 255/255 |
| V-03 | Phase-Separated Exception Blocks | Lifecycle emphasis -- Phase 1/3 blocks have Fallback status field | C-39, C-41 | ~245/255 |
| V-04 | V-01 + V-02 + competitor gate | Combined tightest verbatim + numbered format + Step 4 name gate | nothing | 255/255 |
| V-05 | Full synthesis | All six + conversational register + inertia gates at Steps 4 and 5 | nothing | 255/255 |

---

## Key C-40 fix applied across all variations

Every exception block `Paraphrase clause:` field now carries:

> `-- do not paraphrase, do not summarize, copy it verbatim word-for-word from your Step 2C block`

This converts the field from a faithful-restatement requirement (prior R13 V-04 form) to a string-retrieval requirement, satisfying C-40.

## Key C-41 form in V-01/V-04/V-05

```
Do not fill the table until both lines are written:
```

V-03 intentionally uses declarative form (`Both of the following lines must be written before any row in the table is populated`) to isolate the lifecycle emphasis axis from gate-form compliance.
