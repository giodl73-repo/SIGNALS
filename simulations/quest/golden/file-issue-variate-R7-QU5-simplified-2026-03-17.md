## file-issue -- QU5 Simplification (R7 V-05 → minimal essential)

**Source**: R7 V-05 (maximum compression, 12/12, 100.00)
**QU5 goal**: Shortest prompt that passes all essential criteria (C-01 through C-13)
**Date**: 2026-03-17

---

## Simplification Report

### Zero-work elements removed

| Element | Criteria served | Words |
|---------|----------------|-------|
| `"You are running file-issue."` | None | 4 |
| `"Phase A confirms, collects, and drafts. Phase B validates and writes."` | None (restatement of headings) | 11 |
| `"Severity is confirmed first -- it simultaneously dispatches the collection schema and the output template."` | C-17 only (aspirational) | 16 |
| A1 heading parens `(unified pipeline key -- first and only operation until confirmed)` | C-14/C-17 (aspirational) | 9 |
| A1 dispatch declaration: `"Severity confirmation is the single event that simultaneously dispatches both (a) the collection schema (A2) and (b) the output template (A3). Both are determined by this single event."` | C-17/C-18 (aspirational); C-04 covered by "Do not collect" | 30 |
| A2 heading parens `(collection schema dispatched by severity in A1)` | C-19 (aspirational) | 7 |
| A3 heading parens `(output template dispatched by severity in A1)` | C-19 (aspirational) | 7 |
| `"DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE."` | C-15 (aspirational) | 10 |
| Completion condition block `"Phase A is complete when all three conditions..."` | C-16/C-18 (aspirational) | 76 |
| B2 body verbosity: `"full issue text"` → `"issue text"`, `"(post-B1 revision if any checks failed)"` → `"(revised by B1 if needed)"` | None (elaboration) | 4 |
| B3: `"Artifact written: simulations/feedback/{skill}-issue-{date}.md"` | None (path already in B2 and --body-file flag) | 6 |

**Total removed**: ~180 words
**Aspirational criteria lost**: C-15, C-16, C-17, C-18, C-19 (all aspirational, not essential)
**Essential criteria lost**: 0

### Verification: all essential criteria pass

| Criterion | Element | Status |
|-----------|---------|--------|
| C-01: Required fields | A2 schemas have Skill [req], Expected [req], Actual [req]; A1 collects severity | PASS |
| C-02: Severity enum | "Valid values: crash / wrong-output / missing-feature / improvement" | PASS |
| C-03: Reject invalid | "Reject any other: Not valid. Choose from:..." | PASS |
| C-04: Severity first | "Do not collect any other field until severity is confirmed." | PASS |
| C-05: Severity schemas | All 4 inline schemas in A2 | PASS |
| C-06: Draft shown | "Show draft to user before proceeding." | PASS |
| C-07: Correct path | "Path: simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md" | PASS |
| C-08: Frontmatter | All 6 fields: skill, topic, item, date, severity, target_skill | PASS |
| C-09: Title format | B1 row + all 4 templates use `[{severity}] {skill}: ...` | PASS |
| C-10: All 4 templates | All 4 severity output templates in A3 | PASS |
| C-11: Validation loop | B1 table with corrections + "(do not begin B2 until all rows pass)" | PASS |
| C-12: GitHub CLI | B3 "Open as GitHub issue?" + full gh command | PASS |
| C-13: Context enrichment | B1 "Context enriched" row | PASS |

### Word count

| Version | Words |
|---------|-------|
| R7 V-05 (original) | 607 |
| QU5 simplified | 427 |
| Reduction | 180 words (29.7%) |

---

## SIMPLIFIED PROMPT BODY

---

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
