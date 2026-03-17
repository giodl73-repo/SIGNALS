---
skill: quest-rubric
skill_target: mock-ns
date: 2026-03-16
version: 4
---

# Rubric: mock-ns (v4)

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
  any other computation" instruction in the step body (not merely in a step label or
  parenthetical) consistently produces this ordering.

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

**C-13** -- Three-field emit requirement names the fields by semantic purpose, not just
shows the template.
- **Weight**: aspirational
- **Category**: format
- **Pass condition**: The skill specification, in addition to showing the emit template
  (required for C-12), also identifies the three fields by their semantic purpose --
  existence (found/not found), tier classification, and compliance tags -- either inline
  with the template or as an explicit enumeration (e.g., "All three fields (existence, tier,
  compliance tags) must appear" or "Keep all three fields -- existence, tier, and compliance
  tags"). Naming the fields by purpose makes the requirement auditable: a caller can verify
  each field independently rather than pattern-matching the template surface. A specification
  that shows only the template without naming field purposes satisfies C-12 but fails C-13.

**C-14** -- Emit-first ordering constraint enumerates specific computation steps that are
blocked until after the emit.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The TOPICS.md step instruction explicitly names at least two of the
  following specific operations as blocked until after the emit line: skill selection,
  category lookup or assignment, flag computation or derivation, body generation,
  namespace-default resolution. A generic superlative ("before doing anything else,"
  "before any other step") without naming specific blocked operations satisfies C-11 but
  fails C-14. Enumerating specific operations creates explicit prohibitions on named
  computation steps, which is more robust under instruction-following shortcuts and prompt
  compression than a generic superlative. Both formal prohibition framing (e.g., "CONSTRAINT:
  Do not perform skill selection, category lookup, flag computation, or any other step
  until after...") and conversational before-X-before-Y enumeration (e.g., "before selecting
  a skill, before assigning a category, before computing anything") satisfy this criterion.

**C-15** -- Per-field resolution guidance accompanies the three-field emit requirement.
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: The skill specification provides individual resolution guidance for
  each of the three emit fields -- not just names them (C-13) but also tells the executor
  what to do with each field's value. Acceptable forms include: resolution bullets after
  the enumeration sentence (one bullet per field stating the consequence or action), inline
  annotation of each field with its conditional behavior, or a table mapping field values
  to downstream steps. A specification that enumerates the fields by name but provides no
  per-field resolution guidance satisfies C-13 but fails C-15. Per-field resolution makes
  the three-field format actionable at the point of emission, not just auditable after the
  fact -- the executor knows immediately what to do with a "not found" existence result,
  a Tier 2 classification, or a non-empty compliance tag set.

**C-16** -- Ordering constraint names all three primary computation operations exhaustively.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The TOPICS.md step instruction names all three primary computation
  operations -- skill selection (or namespace-default resolution), category lookup (or
  assignment), and flag computation (or derivation) -- as blocked until after the emit.
  C-14 requires at least two named operations; C-16 requires the full primary trio. Naming
  only skill selection and category lookup (omitting flag computation) satisfies C-14 but
  fails C-16. Exhaustive enumeration of all three operations closes the gap in which a
  model might infer that flag computation is exempt from the ordering constraint because it
  was not named alongside selection and lookup. The three operations may appear in any
  order, may use register-equivalent phrasing (e.g., "flag derivation," "computing the
  flag," "flag assignment"), and may be accompanied by additional named operations -- the
  criterion requires that all three are present, not that only three are present.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential pass + composite >= 80.

**Reference scores under v4**:
- V-02 (2-op enumeration + per-field resolution bullets, no flag-computation mention): 7/8 aspirational (C-16 FAIL) = 98.75
- V-03 (3-op exhaustive enumeration, no per-field resolution bullets): 7/8 aspirational (C-15 FAIL) = 98.75
- V-01 (template-only, generic superlative): 4.5/8 aspirational (C-13 PARTIAL, C-14/C-15/C-16 FAIL) = 95.6
- A variate combining V-02 resolution bullets + V-03 three-op enumeration: 8/8 aspirational = 100

---

## Version History

**v4** -- added C-15 (per-field resolution guidance for emit fields, not just enumeration)
and C-16 (ordering constraint names all three primary computation operations exhaustively:
skill selection, category lookup, AND flag computation), both extracted from Round 3
excellence signals. V-02 satisfies C-15 (resolution bullets per field) but fails C-16
(names only 2 ops, omitting flag computation). V-03 satisfies C-16 (all 3 ops named in
passive blocked-until construction) but fails C-15 (no per-field resolution guidance).
Both score 98.75 under v4; a composite variate combining both patterns scores 100.
Updated aspirational denominator from 6 to 8.

**v3** -- added C-13 (three-field emit requirement names fields by semantic purpose, not
just shows template) and C-14 (ordering constraint enumerates specific blocked computation
steps, not a generic superlative), both extracted from Round 2 excellence signals. V-03
and V-04 satisfy both; V-02 satisfies C-13 but not C-14 (generic superlative); V-01 satisfies
neither. Updated aspirational denominator from 4 to 6 in scoring formula. Perfect score
remains 100.

**v2** -- added C-11 (TOPICS.md emit precedes all computation) and C-12 (emit uses
structured three-field format), both extracted from Round 1 excellence signals in
V-03 and V-04 which achieved 100/100 by satisfying C-09 and C-10. Updated aspirational
denominator from 2 to 4 in scoring formula.

**v1** -- established 5 essential criteria (C-01 to C-05), 3 recommended (C-06 to C-08),
and 2 aspirational (C-09 to C-10) as the baseline scoring structure for mock-ns.
