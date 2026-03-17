---

## Simplified Prompt Body

```markdown
## PHASE A: CONFIRM SEVERITY, COLLECT, DRAFT

### A1 -- SEVERITY

Ask: "What kind of issue is this?"

Valid values: `crash` / `wrong-output` / `missing-feature` / `improvement`

Reject any other: "Not valid. Choose from: crash, wrong-output, missing-feature, improvement."

**Do not collect any other field until severity is confirmed.**

### A2 -- COLLECT

**crash:** Skill [req] | Expected [req] | Actual [req -- verbatim] | Impact | Invocation | Topic | Chain | Version/date

**wrong-output:** Skill [req] | Expected [req] | Actual [req] | Delta | Invocation | Topic | Related | Version/date

**missing-feature:** Skill [req] | Expected [req] | Actual [req -- confirmed absent] | Scope | References | Topic | Invocation

**improvement:** Skill [req] | Expected [req] | Actual [req] | Acceptance condition [req] | Rationale | Topic | Related

### A3 -- DRAFT

**crash:**

  Title: [crash] {skill}: unhandled error -- {description}
  Severity: crash | Skill: `{skill}` | Priority: HIGH -- skill non-functional
  **Expected**: {expected} | **Actual**: {actual -- verbatim} | **Impact**: {blocked workflow}
  **Steps to reproduce**: `{invocation}` | Topic: {topic} | Chain: {chain}
  **Context**: {version, date, related artifacts}

**wrong-output:**

  Title: [wrong-output] {skill}: {section} -- expected {X}, got {Y}
  Severity: wrong-output | Skill: `{skill}`
  **Expected**: {expected} | **Actual**: {actual} | **Delta**: {precise difference}
  **Steps to reproduce**: `{invocation}` | Topic: {topic}
  **Context**: {related skill, version, date}

**missing-feature:**

  Title: [missing-feature] {skill}: {capability} not implemented
  Severity: missing-feature | Skill: `{skill}`
  **Expected**: {capability} | **Actual**: {confirmed absence}
  **Scope**: {inputs; affected outputs} | **References**: {spec, rubric, related skill}
  **Context**: topic={topic} | invocation={invocation}

**improvement:**

  Title: [improvement] {skill}: {specific enhancement}
  Severity: improvement | Skill: `{skill}`
  **Current behavior**: {actual} | **Proposed behavior**: {expected}
  **Rationale**: {why this matters} | **Acceptance condition**: {testable definition of done}
  **Context**: topic={topic} | related={related}

Show draft to user before proceeding.

---

## PHASE B: VALIDATE AND WRITE

### B1 -- VALIDATE (do not begin B2 until all rows pass)

| Check | Pass condition | Correction on fail |
|-------|----------------|--------------------|
| Severity confirmed | Exactly one of the four valid values | Return to A1, re-collect severity |
| Required fields complete | All required fields from the A2 schema for this severity are non-empty | Return to A2, ask for the missing field(s) by name |
| Title names skill + symptom | Specific skill + observable symptom; no generic text | Rewrite: "[{severity}] {skill}: {specific symptom}" |
| Severity-appropriate sections present | All sections from the A3 output template are in the body | Add the missing section(s) from the A3 template |
| Reproducibility present | Invocation, input, topic, or event sequence in body | Add Topic + Invocation; ask user if both absent |
| Tone matches severity | crash=urgent+priority+impact; improvement=proposal+acceptance | Rewrite using A3 output template tone |
| Context enriched | At least one item beyond the 4 required fields present | Add topic, invocation, chain, version, date, or rubric reference |

### B2 -- WRITE

Path: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md`

Frontmatter:
```
skill: file-issue
topic: {topic or "untracked"}
item: issue
date: {YYYY-MM-DD}
severity: {severity}
target_skill: {skill}
```

Body: issue text from A3 (revised by B1 if needed).

### B3 -- OFFER

  Open as GitHub issue?

    gh issue create \
      --title "[{severity}] {skill}: {symptom}" \
      --label "{severity}" \
      --body-file simulations/feedback/{skill}-issue-{date}.md
```

---

## Simplification Report

**What was removed and why:**

| Removed | Criteria only served | Words |
|---------|---------------------|-------|
| `"You are running file-issue."` | None | 4 |
| `"Phase A confirms, collects, and drafts. Phase B validates and writes."` | None — pure restatement of headings | 11 |
| `"Severity is confirmed first -- it simultaneously dispatches..."` (intro) | C-17 only (aspirational) | 16 |
| A1 heading parenthetical `(unified pipeline key -- first and only operation until confirmed)` | C-14/C-17 (aspirational) | 9 |
| A1 dispatch declaration (`"Severity confirmation is the single event that simultaneously dispatches both..."`) | C-17/C-18 (aspirational) — C-04 already covered by `"Do not collect"` | 30 |
| A2 heading parens `(collection schema dispatched by severity in A1)` | C-19 (aspirational) | 7 |
| A3 heading parens `(output template dispatched by severity in A1)` | C-19 (aspirational) | 7 |
| `"DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE."` | C-15 (aspirational) | 10 |
| Full completion condition block `"Phase A is complete when all three conditions..."` | C-16/C-18 (aspirational) | 76 |
| B2 body verbosity (`"full"`, `"post-B1 revision if any checks failed"`) | Elaboration only | 4 |
| B3 `"Artifact written:..."` confirmation line | Not scored; path present in `--body-file` flag | 6 |

**All 13 essential criteria: PASS** — the structural load-bearers (A1 ask+enum+reject+do-not-collect, A2 four schemas, A3 four templates+show-draft, B1 table with corrections, B2 path+frontmatter, B3 gh command) are completely intact.

**Aspirational criteria lost**: C-15, C-16, C-17, C-18, C-19 — these are the dispatch-declaration and gating criteria, all aspirational.

Output written to: `simulations/quest/golden/file-issue-variate-R7-QU5-simplified-2026-03-17.md`

```json
{"simplified_word_count": 427, "original_word_count": 607, "all_essential_still_pass": true}
```
