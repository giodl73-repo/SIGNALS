Written to `simulations/quest/golden/file-issue-golden-2026-03-17.md`.

**What made it golden** (vs. V-01 at 98.33):

1. **C-17/C-18/C-19 triad is jointly required** — V-01 had C-19 alone, which failed C-17 symmetrically with R6 V-02 (C-18 alone). Both sites are structural: provenance headings trace the chain; the completion condition gate verifies it at runtime. Neither alone closes C-17.

2. **C-18 couples the gate to dispatch verification** — the Phase A completion condition must say "both collection schema and output template were dispatched by severity confirmation," not just "fields are non-empty." This makes C-16 and C-18 inseparable in the strongest implementations.

3. **C-15 blocking semantics, not surface form** — "PHASE B IS LOCKED" passes as well as "DO NOT BEGIN PHASE B UNTIL." The criterion is about blocking architecture, not keyword matching.

4. **Table notation is architecturally equivalent** — V-03's manifest table and V-04's verification table both satisfy C-17/C-18/C-19. The criteria are about position and linkage, not prose form.

**Simplification note**: The deployed body is QU5-simplified (29.7% reduction), which drops the aspirational C-15 through C-19 patterns. Pre-simplification score was 100.00 across three independently confirmed variations (V-02, V-03, V-04).
rror -- {description}
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

---

## What Made It Golden

Four patterns distinguish the 100.00 variations from V-01 (98.33, C-17 FAIL, C-18 FAIL):

### 1. C-17 + C-18 + C-19 are jointly required -- C-19 alone does not close C-17

V-01 had C-19 (provenance in sub-operation headings) but no C-18 (dispatch verification in the completion condition). This produced a C-17 FAIL symmetric with R6 V-02, where C-18 alone without C-19 also failed C-17. The rubric encodes an accumulation path: C-17 passes only when both sites are present. Provenance headings trace the dispatch chain through structure; the completion condition gate verifies the dispatch linkage at runtime. Neither site alone is sufficient.

### 2. Completion condition embeds dispatch verification (C-18)

The Phase A gate must explicitly require that *both* collection schema and output template were dispatched by severity confirmation -- not merely that the four required fields are non-empty. V-01's completion condition read "all fields confirmed and non-empty," which verifies presence but not dispatch linkage. Adding "both the collection schema (A2) and output template (A3) have been dispatched by that confirmation" makes the gate also verify C-17 compliance. C-16 and C-18 are now coupled: satisfying C-18 automatically satisfies C-16.

### 3. The blocking imperative does not require a specific surface form (C-15)

V-02 tested whether "PHASE B IS LOCKED. Begin only after..." satisfied C-15 in place of "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." Result: PASS. The criterion requires an explicit, blocking phase-boundary directive -- the declarative form ("IS LOCKED") is structurally equivalent to the imperative. This confirms C-15 is about blocking semantics, not keyword matching.

### 4. Structural notation satisfies dispatch criteria (C-17, C-18, C-19)

V-03 and V-04 demonstrated that table-based dispatch (manifest table in A1, verification table in the completion condition) satisfies C-17/C-18/C-19 as fully as prose-based dispatch. The criteria are about architectural position and linkage, not text form. A manifest table row makes both-column dispatch structurally visible; a verification table row makes dispatch-linkage a named checkable state. Form is not load-bearing.

### 5. Severity-first sequencing is necessary but not sufficient for C-17 (C-14 vs. C-17)

A skill can pass C-14 (severity sequenced first) while failing C-17 (unified pipeline dispatch). C-14 requires that severity is validated before any other field is collected. C-17 additionally requires that the *same* severity confirmation event dispatches *both* the collection schema and the output template -- not two separate decisions triggered independently. The distinction: C-14 is about ordering; C-17 is about unified dispatch key.

---

## Rubric v6 -- Final Criteria Summary

**Essential (60%)**: C-01 required fields | C-02 severity enum enforced | C-03 GitHub issue format | C-04 artifact path under simulations/feedback/

**Recommended (30%)**: C-05 actionable specific title | C-06 reproducibility context | C-07 repo open offer presented

**Aspirational (10%, /12)**: C-08 severity-appropriate framing | C-09 context enrichment | C-10 pre-write validation gate | C-11 corrective actions per check | C-12 per-severity body templates | C-13 severity-labeled issue creation | C-14 severity-first field sequencing | C-15 macro-phase hard boundary | C-16 phase boundary completion condition | C-17 severity-driven unified pipeline dispatch | C-18 completion condition embeds dispatch verification | C-19 dispatch provenance encoded in sub-operation headings

**Scoring**: `(essential/4 * 60) + (recommended/3 * 30) + (aspirational/12 * 10)`

**Simplification note**: QU5 simplified version (this prompt body) drops C-15, C-16, C-17, C-18, C-19 to achieve 29.7% token reduction. All essential and recommended criteria preserved. Pre-simplification score: 100.00.
