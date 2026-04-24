---
skill: quest-rubric
skill_target: mock-ns
date: 2026-03-15
version: 6
---

# Rubric: mock-ns (v6)

Evaluates output from the `mock-ns` skill, which generates a mock artifact for a single
namespace. The artifact must carry the correct MOCK ARTIFACT header, assign the right skill
category, follow the golden structure of the selected skill, apply automatic flagging, and
land at the correct path -- single-pass, no prompts, no coverage summary table (that
belongs to mock-all).

v2 added three aspirational criteria (C-11 to C-13) extracted from Round 1 excellence
signals: flag sequencing before header assembly, explicit topic-status exclusion note, and
fidelity-warning lead-section positioning.

v3 added two aspirational criteria (C-14 to C-15) extracted from Round 2 excellence
signals: dual-point flag immutability (prohibition language at both the compute site and the
consumption site), and structural exclusion column in the default skill table (exclusion
constraint elevated from inline annotation to dedicated table column).

v4 added two aspirational criteria (C-16 to C-17) extracted from Round 3 excellence
signals: run-scoped immutability declaration (prohibition language explicitly covers the
entire run, not only sequential subsequent steps), and first-rule prioritization of the
FLAG prohibition at the consumption site (the prohibition is the first stated instruction
at header assembly, before any other header-construction logic).

v5 added three aspirational criteria (C-18 to C-20) extracted from Round 4 excellence
signals: named path class enumeration at the compute site (prohibition explicitly lists
every execution path class rather than relying on a general "anywhere" statement),
anti-displacement closure at the consumption site (first-rule prohibition names the
specific instruction types that cannot precede it and concludes with a declarative closure),
and failure-consequence framing at the consumption site (the prohibition includes an explicit
inertia-consequence statement naming the specific failure mechanism and downstream impact of
rederiving FLAG at header assembly).

v6 adds two aspirational criteria (C-21 to C-22) extracted from Round 5 excellence
signals: no-exemption affirmative closure at the compute site (after enumerating named path
classes, the prohibition adds a positive-obligation statement asserting that every execution
path carries the computed FLAG and that no path is exempt, closing the gap where an
enumeration -- even with a catch-all -- can still be read as illustrative rather than
exhaustive), and catch-all instruction clause in the anti-displacement closure at the
consumption site (after naming the three canonical instruction types that cannot precede the
FLAG prohibition, the closure adds a catch-all covering any other instruction in the step,
mirroring the C-18 catch-all pattern applied to the consumption side).

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

**C-14** -- FLAG immutability is declared explicitly at both the compute site and the
consumption site.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-11 requires the compute step to precede header assembly; C-14
  requires that explicit prohibition language appears at *both* sites. At the compute step:
  language declaring the FLAG value final after emission -- "do not modify FLAG after this
  point," "FLAG is now resolved. Do not re-evaluate or modify it after this emit," or
  equivalent. At the header assembly step: language prohibiting re-derivation -- "Do not
  re-derive," "copy it exactly, do not rederive," "Copy FLAG verbatim. Do not rederive.,"
  or equivalent. Prohibition at only one site fails this criterion. Artifacts that fail
  C-11 (no named FLAG variable) fail C-14 automatically. The dual-point enforcement
  eliminates the residual risk that a model under pressure recomputes the flag at header
  time despite a compute step being present.

**C-15** -- Default skill table uses a dedicated structural column for exclusion
constraints, not inline annotation.
- **Weight**: aspirational
- **Category**: correctness
- **Pass condition**: C-12 requires exclusion language to appear alongside the default
  table; C-15 requires that the exclusion constraint be elevated to a dedicated column of
  the table itself -- e.g., a three-column table with columns for namespace, default skill,
  and exclusion note. The exclusion column must be labeled, must carry the topic-status
  exclusion entry in the topic row, and must be positioned as a structural element the
  reader cannot skip. An exclusion note appended as prose after the table, or embedded as
  a bracket annotation on the same row (e.g., `[NOT topic-status]`), passes C-12 but fails
  C-15. Evidence: a table with a named Exclusion column or equivalent structural column
  carrying hard-constraint language.

**C-16** -- FLAG immutability prohibition is declared as run-scoped, not only
step-sequential.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-14 requires prohibition language at both the compute site and the
  consumption site; C-16 requires that the prohibition at the compute site explicitly
  covers the entire run -- "anywhere in this run," "in any step of this run," "MUST NOT be
  recomputed at any point during this run," or equivalent. Step-sequential language
  ("do not modify FLAG in any subsequent step") satisfies C-14 but fails C-16, because
  conditional branches or regeneration paths that bypass normal step order could still
  reach header assembly without encountering a prior-step prohibition. Run-scoped language
  closes this gap by making the prohibition independent of execution path. Artifacts that
  fail C-14 fail C-16 automatically.

**C-17** -- FLAG prohibition at the consumption site is the first stated rule of the
header assembly step.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-14 requires that prohibition language appear somewhere at the
  consumption site; C-17 requires that it be the *first* stated instruction at the header
  assembly step -- before any other header-construction logic, field-listing, or formatting
  rules. Evidence: language such as "The first rule of this step is: copy FLAG from S-N
  verbatim. Do not rederive it." or "RULE 1 -- Do not compute a new FLAG value here. Copy
  it from the compute step." appearing as the opening statement of the step, not as a
  trailing note or mid-step aside. Positioning the prohibition first ensures it is
  processed before any competing instruction that might create pressure to rederive.
  Prohibition present but not prioritized (appearing after other instructions in the step)
  passes C-14 but fails C-17. Artifacts that fail C-14 fail C-17 automatically.

**C-18** -- FLAG prohibition at the compute site enumerates named execution path classes.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-16 requires the prohibition at the compute site to be run-scoped
  ("anywhere in this run" or equivalent); C-18 requires it to explicitly enumerate named
  execution path classes rather than relying on a general scope statement alone. At minimum,
  three path classes must be named: conditional branches, fallback paths, and regeneration
  sequences. Evidence: language such as "MUST NOT be recomputed anywhere in this run -- not
  in any step, any conditional branch, any fallback path, or any regeneration sequence"
  (V-02 pattern) or an equivalent enumeration. The enumeration eliminates interpretive
  ambiguity: a reader or executor cannot narrow "anywhere in this run" to exclude non-linear
  paths. A catch-all clause ("or any other execution context") and a bypass-order clarifier
  ("including paths that do not pass through prior steps in normal order") further
  strengthen the criterion but are not required for a PASS. Artifacts that fail C-16 fail
  C-18 automatically.

**C-19** -- FLAG prohibition at the consumption site includes anti-displacement closure.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-17 requires the FLAG prohibition to be the first stated rule of
  the header assembly step; C-19 requires the prohibition statement to include explicit
  anti-displacement language that names the specific instruction types that cannot precede
  it -- field-listing, category lookup, and formatting instructions are the canonical three
  -- and concludes with a declarative closure asserting no other instruction in the step
  precedes the rule. Evidence: language such as "This rule is first -- it applies before
  any field is listed, before any category lookup, before any formatting instruction in
  this step. No instruction in A-1 precedes this rule." (V-01 A-1 pattern) or equivalent.
  The gap closed: a first-positioned prohibition (C-17 pass) that names no competing types
  and offers no declarative closure can still be displaced under execution pressure when
  adjacent instructions are processed before the prohibition is anchored. Anti-displacement
  closure prevents this by explicitly naming what cannot come first and asserting the rule's
  primacy in unambiguous terms. Artifacts that fail C-17 fail C-19 automatically.

**C-20** -- FLAG prohibition at the consumption site includes an explicit failure-consequence
statement.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-17 requires the FLAG prohibition to be first; C-19 requires
  anti-displacement closure; C-20 requires the prohibition to also include an explicit
  inertia-consequence statement -- a named description of what specifically goes wrong if
  FLAG is rederived at header assembly. The consequence statement must identify at minimum:
  (a) the failure mechanism (e.g., category mismatch produced by rederivation), and
  (b) why the failure is dangerous (e.g., invisible to downstream tooling, silently
  corrupts trust tier, cannot be caught by automated review). Evidence: language such as
  "Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to
  downstream tooling and silently corrupts the artifact's trust tier." (V-05 A-1 pattern)
  or equivalent. The gap closed: prohibition language that says "do not rederive" without
  naming the consequence requires the executor to infer why -- an executor under pressure
  may deprioritize an unexplained prohibition. Naming the consequence makes the cost of
  violation visible at the moment the instruction is processed. Artifacts that fail C-17
  fail C-20 automatically.

**C-21** -- FLAG prohibition at the compute site includes a no-exemption affirmative closure.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-18 requires the prohibition at the compute site to enumerate named
  execution path classes; C-21 requires it to conclude with an affirmative closure that
  asserts the positive obligation and states explicitly that no path is exempt. Two
  components are required: (a) a positive-obligation statement asserting that every
  execution path that reaches the consumption site carries the FLAG value emitted at the
  compute step (e.g., "Every execution path that reaches A-1 carries the FLAG value emitted
  here"), and (b) an explicit no-exemption statement (e.g., "No path is exempt"). The
  gap closed: an enumeration of path classes -- even one that includes a catch-all clause
  ("or any other execution context") -- can still be read as illustrative rather than
  exhaustive; the affirmative closure states exhaustiveness as a positive fact and forecloses
  the possibility of an unmentioned path class treating itself as outside the prohibition.
  The V-05 compute-site pattern is the reference: "MUST NOT be recomputed anywhere in this
  run -- not in any step, any conditional branch, any fallback path, any regeneration
  sequence, or any other execution context, including paths that do not pass through prior
  steps in normal order. Every execution path that reaches A-1 carries the FLAG value
  emitted here. No path is exempt." Artifacts that fail C-18 fail C-21 automatically.

**C-22** -- Anti-displacement closure at the consumption site includes a catch-all
instruction clause.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-19 requires the anti-displacement closure to name the three
  canonical instruction types that cannot precede the FLAG prohibition (field-listing,
  category lookup, and formatting instructions) and to conclude with a declarative closure
  asserting primacy; C-22 requires the closure to additionally include a catch-all clause
  covering any other instruction in the step not explicitly listed. Evidence: language
  such as "This rule is first -- it applies before any field is listed, before any category
  lookup, before any formatting instruction, or any other instruction in this step. No
  instruction in A-1 precedes this rule." The catch-all clause mirrors the C-18 pattern
  (catch-all in path enumeration) applied to instruction enumeration at the consumption
  site. The gap closed: naming only the three canonical instruction types leaves the
  anti-displacement closure vulnerable to novel instruction types introduced in future
  revisions -- an executor encountering an instruction not in the named list may not
  recognize it as subject to the displacement prohibition. The catch-all eliminates this
  gap by making the coverage exhaustive by construction. Artifacts that fail C-19 fail
  C-22 automatically.

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)
```

PARTIAL counts as 0.5 for any criterion.

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Essential (5x) | Recommended (3x) | Aspirational (14x) |
|------|---------------|-----------------|-------------------|
| Points | 60 | 30 | 10 |
| Formula | pass/5 x 60 | pass/3 x 30 | pass/14 x 10 |

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
- **C-14 fail**: Prohibition language present at the compute step but absent at the header
  assembly step (or vice versa) -- one-sided enforcement leaves the residual re-derivation
  risk intact. Fails automatically when C-11 fails.
- **C-15 fail**: Exclusion note for topic-status present as inline text or bracket
  annotation (C-12 passes) but not elevated to a structural table column -- the constraint
  is visible only to a careful reader, not enforced by table structure.
- **C-16 fail**: Prohibition language present at the compute site (C-14 passes) but scoped
  to sequential steps only ("in any subsequent step") rather than the full run -- leaves
  conditional branches and regeneration paths unprotected. Fails automatically when C-14
  fails.
- **C-17 fail**: Prohibition language present at the header assembly step (C-14 passes) but
  positioned mid-step or as a trailing note rather than as the first stated rule --
  competing instructions before the prohibition create residual re-derivation pressure.
  Fails automatically when C-14 fails.
- **C-18 fail**: Prohibition at the compute site is run-scoped (C-16 passes) but uses only
  a general scope statement ("anywhere in this run") without naming execution path classes
  -- a reader can still interpret the prohibition as applying only to the normal step
  sequence. Fails automatically when C-16 fails.
- **C-19 fail**: Prohibition at the consumption site is first-positioned (C-17 passes) but
  does not name specific competing instruction types and carries no declarative closure --
  the prohibition is asserted but not defended against the instructions that most commonly
  displace it. Fails automatically when C-17 fails.
- **C-20 fail**: Prohibition at the consumption site is first-positioned (C-17 passes) but
  names no failure consequence -- the executor is left to infer why rederivation is
  dangerous rather than having the cost of violation made explicit at the point of the
  instruction. Fails automatically when C-17 fails.
- **C-21 fail**: Prohibition at the compute site enumerates named path classes (C-18 passes)
  but lacks an affirmative closure -- the enumeration, even with a catch-all clause, can
  still be read as illustrative rather than exhaustive. Missing either the positive-path
  assertion ("Every execution path that reaches A-1 carries the FLAG value emitted here")
  or the no-exemption statement ("No path is exempt") fails this criterion. Fails
  automatically when C-18 fails.
- **C-22 fail**: Anti-displacement closure names the three canonical instruction types
  (C-19 passes) but omits a catch-all clause covering other instruction types -- leaves the
  closure vulnerable to instruction types not in the named list. Fails automatically when
  C-19 fails.
