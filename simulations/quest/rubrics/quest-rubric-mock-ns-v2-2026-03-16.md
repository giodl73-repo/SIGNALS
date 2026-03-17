---
skill: quest-rubric
skill_target: mock-ns
date: 2026-03-16
version: 2
---

# Rubric: mock-ns (v2)

Evaluates output from the `mock-ns` skill, which generates a mock artifact for a single
namespace. The artifact must carry the correct MOCK ARTIFACT header, assign the right
category for the selected skill, follow the golden structure of that skill, apply automatic
flagging, and land at the correct path -- single-pass, no prompts. No coverage summary
table (that belongs to mock-all).

Composite score = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)

Golden threshold: all essential pass + composite >= 80.

---

## Criteria

### Essential (must all pass)

**C-01** -- MOCK ARTIFACT header block is present, syntactically complete, and immediately
follows any frontmatter.
- **Weight**: essential
- **Category**: format
- **Pass condition**: The output contains all five required fields in order:
  `[MOCK ARTIFACT -- NOT VERIFIED]`, `Skill: {skill-id}`, `Topic: {topic}`,
  `Category: {value}`, `Date: {date}`, `Status: MOCK (awaiting review)`.
  All fields are present and non-empty. The block appears before any namespace body content.
  Missing any field or placing the block after body content is a hard fail.

**C-02** -- Category assignment is correct for the skill selected.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: The Category field value matches the canonical category for the skill:
  HIGH-STRUCTURE for structural-archetype skills (scout-feasibility, trace-request,
  flow-resilience, draft-spec, draft-proposal, draft-pitch, review-design, review-code,
  trace-component, trace-contract, trace-state, trace-skill, trace-migration,
  trace-deployment, flow-conversation, flow-lifecycle, flow-trigger, flow-dataflow,
  flow-integration, flow-throttle, program-plan, scout-stakeholders, scout-requirements,
  scout-naming, scout-compliance, scout-market);
  EVIDENCE-HEAVY for prove-websearch, prove-interview, prove-prototype, listen-feedback,
  listen-support, listen-adoption;
  MIXED for scout-competitors, prove-hypothesis, review-customers, review-users.
  Any unlisted or mismapped category value fails this criterion.

**C-03** -- Mock body follows the golden rubric structure of the selected skill.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: The namespace body contains the key structural elements of the selected
  (or representative) skill: correct section headings, required tables or lists, gate or
  verdict line where the skill produces one, and enforcement mechanisms in the expected
  positions. A reader familiar with the real skill can identify which skill was mocked.
  Generic prose without skill-specific structure fails this criterion.

**C-04** -- Automatic category flag is present and matches the category.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: A `Flag:` line appears in or immediately after the MOCK ARTIFACT header
  block. Its value must match the category:
  `none (structural coverage reliable)` for HIGH-STRUCTURE;
  `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` for EVIDENCE-HEAVY;
  `REVIEW-FOR-PLAUSIBILITY` for MIXED.
  Any category-flag mismatch fails this criterion.

**C-05** -- Artifact path and filename follow the convention
`simulations/mock/{topic}-{namespace}-mock-{date}.md`.
- **Weight**: essential
- **Category**: format
- **Pass condition**: The artifact write line shows the exact path pattern. The namespace
  segment matches the namespace argument (scout, draft, review, flow, trace, prove, listen,
  program, or topic). Date is in YYYY-MM-DD format. The skill-id is NOT embedded in the
  path (it belongs in the header, not the filename). Path segment mismatch or skill-id
  leaking into the filename fails this criterion.

---

### Recommended (output is better with these)

**C-06** -- Representative skill selection is correct when `--skill` is not specified.
- **Weight**: recommended
- **Category**: correctness
- **Pass condition**: When no `--skill` flag is given, the Skill field in the header matches
  the correct namespace default: scout=scout-feasibility, draft=draft-spec,
  review=review-design, flow=flow-resilience, trace=trace-request, prove=prove-hypothesis,
  listen=listen-support, program=program-plan, topic=topic-plan.
  topic-status is excluded as meta-structural and must NOT appear as the topic default.

**C-07** -- Fidelity warning block for the assigned category is present in the artifact body.
- **Weight**: recommended
- **Category**: depth
- **Pass condition**: The artifact body includes the category-appropriate fidelity warning.
  EVIDENCE-HEAVY: WARNING block stating content is structurally correct but evidentially
  fabricated. MIXED: CAUTION block distinguishing reliable structural elements from
  partially-fabricated specific claims. HIGH-STRUCTURE: NOTE block stating structure and
  enforcement mechanisms are reliable, adequate for Tier 1, REAL-REQUIRED at Tier 2+ for
  critical namespaces (trace, scout-feasibility, listen). Absence of the warning when the
  category is EVIDENCE-HEAVY is a hard fail for this criterion.

**C-08** -- Final line is the next-step invocation prompt.
- **Weight**: recommended
- **Category**: format
- **Pass condition**: The last line of the artifact reads:
  `Next: /mock:review {topic} {this-file}` where `{this-file}` is the artifact path
  produced in this run. The prompt is present unless the skill is being called from within
  a mock-review session to regenerate a thin namespace.

---

### Aspirational (raise the bar once essential/recommended are stable)

**C-09** -- Tier-conditional flag refinement for critical namespaces.
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: For HIGH-STRUCTURE namespaces designated critical at Tier 2+ (trace-*,
  scout-feasibility, listen-*), the flag reads
  `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` rather than the base
  `none (structural coverage reliable)`. This surfaces the tier escalation directly in the
  artifact header without requiring the user to consult the critical namespace list.

**C-10** -- Setup phase shows evidence of TOPICS.md consultation.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The skill's setup output (progress lines before artifact content)
  includes a dedicated emit line confirming TOPICS.md was read: topic found/not found,
  tier classification read or defaulted, compliance tags checked. The emit must appear as
  its own output line (e.g., `> TOPICS.md: {result}`) -- embedding the tier in a general
  progress line without a dedicated TOPICS.md emit fails this criterion.

**C-11** -- TOPICS.md emit is the first observable output line, preceding all computation.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The `> TOPICS.md: ...` emit line appears before any namespace-default
  lookup, category assignment, flag computation, or body generation. If any computation
  step (skill selection, category resolution, flag derivation) appears in the output before
  the TOPICS.md emit, this criterion fails. The emit is step zero -- not interspersed with
  setup steps and not deferred until after the skill is identified. A prompt that specifies
  TOPICS.md as a dedicated first step with an explicit "before doing anything else" / "before
  any other computation" instruction consistently produces this ordering.

**C-12** -- TOPICS.md emit uses the structured three-field format.
- **Weight**: aspirational
- **Category**: format
- **Pass condition**: The emit line takes the exact form:
  `> TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}`
  All three fields must be present: topic existence, tier value (or default), and compliance
  tags (or `none`). A bare `> TOPICS.md: found` or similar single-field emit fails this
  criterion. The tier field from this emit is the value that feeds the C-09 tier-conditional
  flag check -- a prompt that specifies the verbatim format makes this linkage explicit and
  auditable.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Version History

**v2** -- added C-11 (TOPICS.md emit precedes all computation) and C-12 (emit uses
structured three-field format), both extracted from Round 1 excellence signals in
V-03 and V-04 which achieved 100/100 by satisfying C-09 and C-10. Updated aspirational
denominator from 2 to 4 in scoring formula.

**v1** -- established 5 essential criteria (C-01 to C-05), 3 recommended (C-06 to C-08),
and 2 aspirational (C-09 to C-10) as the baseline scoring structure for mock-ns.
