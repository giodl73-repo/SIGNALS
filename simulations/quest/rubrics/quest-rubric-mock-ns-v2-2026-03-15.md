---
skill: quest-rubric
skill_target: mock-ns
date: 2026-03-15
version: 2
---

# Rubric: mock-ns (v2)

Evaluates output from the `mock-ns` skill, which generates a mock artifact for a single
namespace. The artifact must carry the correct MOCK ARTIFACT header, assign the right skill
category, follow the golden structure of the selected skill, apply automatic flagging, and
land at the correct path -- single-pass, no prompts, no coverage summary table (that
belongs to mock-all).

v2 adds three aspirational criteria (C-11 to C-13) extracted from Round 1 excellence
signals: flag sequencing before header assembly, explicit topic-status exclusion note, and
fidelity-warning lead-section positioning.

---

## Criteria

### Essential (must all pass)

**C-01** -- MOCK ARTIFACT header block is present, syntactically complete, and immediately
follows any frontmatter.
- **Weight**: essential
- **Category**: format
- **Pass condition**: The output contains the exact five-line block in this order:
  `[MOCK ARTIFACT -- NOT VERIFIED]`, `Skill: {skill-id}`, `Topic: {topic}`,
  `Category: HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED`, `Date: {date}`,
  `Status: MOCK (awaiting review)`. All five fields are present and non-empty. The header
  appears before any namespace body content.

**C-02** -- Category assignment is correct for the skill selected.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: The Category value in the header matches the canonical category table
  from the spec: HIGH-STRUCTURE for structural-archetype skills (scout-feasibility,
  trace-request, flow-resilience, draft-spec, draft-proposal, draft-pitch, review-design,
  review-code, trace-component, trace-contract, trace-state, trace-skill, trace-migration,
  trace-deployment, flow-conversation, flow-lifecycle, flow-trigger, flow-dataflow,
  flow-integration, flow-throttle, program-plan, scout-stakeholders, scout-requirements,
  scout-naming, scout-compliance, scout-market); EVIDENCE-HEAVY for prove-websearch,
  prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption;
  MIXED for scout-competitors, prove-hypothesis, review-customers, review-users. No
  unlisted category value is accepted.

**C-03** -- Mock body follows the golden rubric structure of the selected skill, not a
generic template.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: The namespace body contains the key structural elements of the
  selected (or representative) skill: correct section headings, required tables or lists,
  gate or verdict line where the skill produces one, and enforcement mechanisms in the
  expected positions. A reader familiar with the real skill could identify which skill was
  mocked. Generic prose without skill-specific structure fails this criterion.

**C-04** -- Automatic category flag is present and matches the category.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: A `Flag:` line appears in or immediately after the MOCK ARTIFACT
  header block. Its value must match the category: `none (structural coverage reliable)`
  for HIGH-STRUCTURE; `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)` for
  EVIDENCE-HEAVY; `REVIEW-FOR-PLAUSIBILITY` for MIXED. No category-flag mismatch is
  accepted.

**C-05** -- Artifact path and filename follow the convention
`simulations/mock/{topic}-{namespace}-mock-{date}.md`.
- **Weight**: essential
- **Category**: format
- **Pass condition**: The output line reporting the artifact write (e.g.,
  `> Artifact written: ...`) shows the exact path pattern. The namespace segment matches
  the namespace argument (scout, draft, review, flow, trace, prove, listen, program, or
  topic). Date is in YYYY-MM-DD format. Skill-id is NOT embedded in the path (it goes in
  the header, not the filename).

---

### Recommended (output is better with these)

**C-06** -- Representative skill selection is correct when `--skill` is not specified.
- **Weight**: recommended
- **Category**: correctness
- **Pass condition**: When no `--skill` flag is given, the Skill field in the header
  matches the correct namespace default: scout=scout-feasibility, draft=draft-spec,
  review=review-design, flow=flow-resilience, trace=trace-request, prove=prove-hypothesis,
  listen=listen-support, program=program-plan, topic=topic-plan (not topic-status, which
  is excluded as meta-structural per the spec).

**C-07** -- Fidelity warning block for the assigned category is present in the artifact
body.
- **Weight**: recommended
- **Category**: depth
- **Pass condition**: The artifact body includes the category-appropriate fidelity warning
  before or immediately after the mock content begins. EVIDENCE-HEAVY: the WARNING block
  stating content is structurally correct but evidentially fabricated. MIXED: the CAUTION
  block distinguishing reliable structural elements from partially-fabricated specific
  claims. HIGH-STRUCTURE: the NOTE block stating structure and enforcement mechanisms are
  reliable, adequate for Tier 1, REAL-REQUIRED at Tier 2+ for critical namespaces. Absence
  of the warning when the category is EVIDENCE-HEAVY is a hard fail for this criterion.
  All three category variants must be fully specified -- truncated HIGH-STRUCTURE warnings
  (missing the REAL-REQUIRED at Tier 2+ qualifier) are scored PARTIAL.

**C-08** -- Final line is the next-step invocation prompt.
- **Weight**: recommended
- **Category**: format
- **Pass condition**: The last line of the artifact (after all content) reads:
  `Next: /mock:review {topic} {this-file}` where `{this-file}` is the artifact path
  produced in this run. The prompt is present unless the spec notes it may be omitted
  when called from within a mock-review session to regenerate a thin namespace.

---

### Aspirational (raise the bar once essential/recommended are stable)

**C-09** -- Tier-conditional flag refinement for critical namespaces.
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: For HIGH-STRUCTURE namespaces that are designated critical at Tier
  2+ (trace, scout-feasibility, listen), the flag reads
  `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` rather than the base
  `none (structural coverage reliable)`. This surfaces the tier escalation requirement
  directly in the artifact without requiring the user to recall the critical namespace
  list.

**C-10** -- Setup phase shows evidence of TOPICS.md consultation.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The skill's setup output (progress lines before the artifact content)
  includes a dedicated emit line indicating TOPICS.md was read: topic found/not found, tier
  classification read or defaulted, compliance tags checked. The emit line must appear as
  its own output line (e.g., `> TOPICS.md: {result}`) -- embedding the tier in a general
  `> Generating mock for...` line without a dedicated TOPICS.md emit does not satisfy this
  criterion. If compliance tags are present for the topic, compliance-adjacent namespaces
  (scout-compliance, trace-permissions) are pre-flagged `REAL-REQUIRED (compliance-sensitive)`
  regardless of category.

**C-11** -- Flag value is computed as a named procedural step before header assembly.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The skill procedure includes a discrete step dedicated to computing
  the flag value, sequenced before the header-assembly step. The header block's Flag field
  references the pre-computed value by name rather than computing it inline during header
  construction. This sequencing enforces flag correctness at the point of least cognitive
  load and directly prevents the most common C-04 failure (flag deferred or left as a
  placeholder). Evidence: an explicit "Compute flag" or equivalent step in the procedure,
  with the header assembly step referencing it by name.

**C-12** -- topic-status exclusion is documented inline with the default skill table.
- **Weight**: aspirational
- **Category**: correctness
- **Pass condition**: The default skill documentation includes an explicit exclusion note
  for topic-status alongside the namespace default mapping table, stating that topic-status
  is excluded as meta-structural (or equivalent). The exclusion note appears in the same
  section as the default table -- a passing C-06 (correct default chosen) without this
  explicit note scores FAIL for C-12. The note must use language strong enough to prevent
  substitution: "excluded," "not used as default," or "Do NOT use" are acceptable;
  absence of any exclusion language fails this criterion.

**C-13** -- Fidelity warning block is positioned as a lead section before mock body content.
- **Weight**: aspirational
- **Category**: depth
- **Pass condition**: The fidelity warning block appears as the first section of the
  artifact body, before any skill-specific content, separated from the header and from the
  body by `---` delimiters. Positioning the warning before the reader encounters mock
  content establishes the epistemological framing (what can be trusted, what cannot) before
  the content is consumed. A warning block appended after the mock content, or embedded
  inline within it, scores FAIL for this criterion. This is independent of C-07 -- an
  artifact can pass C-07 (warning present) and fail C-13 (warning not in lead position).

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

PARTIAL counts as 0.5 for any criterion.

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Essential (5x) | Recommended (3x) | Aspirational (5x) |
|------|---------------|-----------------|------------------|
| Points | 60 | 30 | 10 |
| Formula | pass/5 x 60 | pass/3 x 30 | pass/5 x 10 |

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Output is usable as a mock artifact |
| Silver | >= 60, all essential pass | Usable but fidelity warnings or next-step missing |
| Bronze | >= 60, some essential fail | Structurally present but unreliable for downstream use |
| Fail | < 60 or any essential fail | Not safe to use; regenerate |

---

## Common Failure Modes

- **C-01 fail**: Header block present but missing a field (most often `Flag:` or `Status:`).
- **C-02 fail**: Category set to HIGH-STRUCTURE for a prove-* or listen-* skill. These are
  EVIDENCE-HEAVY and must be flagged REAL-REQUIRED.
- **C-03 fail**: Mock body is generic prose ("this namespace covers feasibility concerns")
  rather than a structured table/gate matching the actual skill output.
- **C-04 fail**: Flag field absent, or flag says `none` for an EVIDENCE-HEAVY skill.
- **C-05 fail**: Filename embeds the skill-id (e.g., `frogs-trace-request-mock-...`) instead
  of the namespace (e.g., `frogs-trace-mock-...`).
- **C-07 partial**: HIGH-STRUCTURE warning present but truncated -- missing the
  "REAL-REQUIRED at Tier 2+ for critical namespaces" qualifier.
- **C-10 fail**: TOPICS.md consulted but result embedded in a general progress line rather
  than a dedicated `> TOPICS.md: {result}` emit.
- **C-11 fail**: Flag value computed inline during header assembly rather than in a prior
  named step -- the most common path to a deferred or incorrect flag.
- **C-12 fail**: Default skill table correct (C-06 passes) but no exclusion note for
  topic-status -- leaves the door open for topic-status substitution in edge cases.
- **C-13 fail**: Fidelity warning present (C-07 passes) but positioned after mock content
  rather than as a lead section before the body begins.
