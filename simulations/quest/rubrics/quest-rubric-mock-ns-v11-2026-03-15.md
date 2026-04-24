---
skill: quest-rubric
skill_target: mock-ns
date: 2026-03-15
version: 11
---

# Rubric: mock-ns (v11)

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

v6 added two aspirational criteria (C-21 to C-22) extracted from Round 5 excellence
signals: no-exemption affirmative closure at the compute site (after enumerating named path
classes, the prohibition adds a positive-obligation statement asserting that every execution
path carries the computed FLAG and that no path is exempt, closing the gap where an
enumeration -- even with a catch-all -- can still be read as illustrative rather than
exhaustive), and catch-all instruction clause in the anti-displacement closure at the
consumption site (after naming the three canonical instruction types that cannot precede the
FLAG prohibition, the closure adds a catch-all covering any other instruction in the step,
mirroring the C-18 catch-all pattern applied to the consumption side).

v7 added two aspirational criteria (C-23 to C-24) extracted from Round 6 excellence
signals: failure-consequence statement at the compute site (V-02's C-21 pass demonstrated
the affirmative closure pattern -- "Every execution path that reaches A-1 carries the FLAG
value emitted here. No path is exempt." -- but carried no explanation of what goes wrong if
a path violates this closure; C-23 closes this gap by requiring the compute-site prohibition
to name the upstream contamination mechanism and its consequence at the consumption site,
mirroring C-20 applied to the compute side), and no-instruction-exempt affirmative closure
at the consumption site (V-01's C-22 pass demonstrated the catch-all instruction clause --
"or any other instruction in this step" -- but added no positive-obligation statement
asserting that every instruction in the step is governed by the prohibition; C-24 closes
this gap by requiring a positive-coverage affirmative after the catch-all, mirroring C-21's
pattern applied to the instruction enumeration at the consumption side).

v8 added two aspirational criteria (C-25 to C-26) extracted from Round 7 excellence
signals: guarantee-break framing in the compute-site failure-consequence statement (V-04's
C-23 pass named the contamination mechanism and downstream effect in minimal form -- "If any
path modifies FLAG after this point, A-1 will inherit a corrupted value that cannot be
distinguished from a correctly-computed one" -- but did not frame the violation as breaking
the affirmative closure guarantee that was just stated; V-05's extended form added "the
guarantee stated above is broken" as an explicit causal bridge between the C-21 closure and
the consequence, making the violation's impact visible at the point of the guarantee rather
than as an independent warning; C-25 elevates this framing to a pass condition, depending
on C-23), and cross-site consequence reference in the compute-site failure-consequence
statement (V-05's extended form additionally named "the same silent category mismatch
described at the consumption site," explicitly linking the compute-site consequence to
C-20's consumption-site consequence and making the structural symmetry between the two
prohibition sites navigable; C-26 elevates this cross-reference to a pass condition,
depending on C-23 and requiring C-20 to be present at the consumption site as the reference
target).

v9 added two aspirational criteria (C-27 to C-28) extracted from Round 9 excellence
signals: structural isolation of the guarantee-break and cross-site claims (V-02's Round 9
pass demonstrated that C-25's guarantee-break framing and C-26's cross-site reference can
appear as individually scannable, labeled units -- dedicated rows in the tabular form --
rather than as subordinate clauses appended to a longer failure-consequence statement; when
embedded as end-of-paragraph clauses both claims are present and machine-readable but
cognitively skippable; C-27 elevates structural isolation to a pass condition, requiring
each claim to occupy an independently scannable unit so neither can be treated as a trailing
qualification of the consequence statement it follows, depending on C-25 and C-26), and
navigation-anchored cross-site reference (V-02's Round 9 pass additionally demonstrated
that the cross-site reference can name the specific structural location of the target --
"see A-1 Failure consequence row below" -- rather than a generic site description -- "at
the consumption site"; naming the location turns a semantic reference into a navigable
pointer; C-28 elevates location-specific navigation anchoring to a pass condition, depending
on C-26 and C-27; the bidirectional form -- A-1 also names S-3 as the source -- was seeded
as the v10 aspirational target).

v10 adds three aspirational criteria (C-29 to C-31) extracted from Round 10 excellence
signals: bidirectional navigation anchor (Round 10 demonstrated 4/5 variants achieving the
aspirational maximum seeded in v9 -- V-01, V-02, V-04, and V-05 all carry an explicit
self-identification marker at A-1 naming S-3 as the source of the cross-reference, so that
the structural link is discoverable from either end; C-29 graduates this property from
aspirational maximum to pass condition, depending on C-28), bracket token notation for
cross-reference links (V-02 and V-05 additionally replaced natural-language location
descriptions with structured bracket identifiers -- [A-1:FC] in the forward direction and
[S-3:CS] in the backward direction -- creating machine-parseable tokens that a reader can
match without parsing surrounding prose; C-30 elevates bracket token notation to a pass
condition, depending on C-29), and pre-chain protocol preamble (V-05 uniquely placed a
dedicated orientation block before all prohibition rows that names every cross-reference
token pair, states what each identifier resolves to, and establishes the complete
bidirectional link before any individual row is read; C-31 elevates this orientation
structure to a pass condition, depending on C-30).

v11 adds two aspirational criteria (C-32 to C-33) extracted from Round 11 excellence
signals: pre-computation preamble positioning (Round 11 V-01 advanced the C-31 preamble
from "before all prohibition rows" to "before all computation cases AND all prohibition
rows" -- the preamble appears at the very top of S-3, before FLAG is evaluated, so the
executor has the full cross-reference map before encountering any FLAG-related logic; C-32
graduates this earlier positioning to a pass condition, noting that C-31 variants still
embedded mid-S-3 between computation and prohibition are a recognized positioning gap;
depends on C-31), and structured token resolution table (Round 11 V-02 demonstrated that
the prose preamble required by C-31 can be replaced by a structured table consisting of an
abbreviation key naming row-type codes and a resolution table mapping each token to its
step, row type, paired token, and direction -- enabling O(1) token lookup by name rather
than prose parsing; C-33 elevates this structured table form to a pass condition, depending
on C-32).

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

**C-23** -- FLAG prohibition at the compute site includes a failure-consequence statement.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-21 requires the compute-site prohibition to conclude with an
  affirmative closure asserting positive coverage and no exemptions; C-23 requires the
  prohibition to also include an explicit failure-consequence statement naming what goes
  wrong if any execution path reaches the consumption site carrying a FLAG value that
  differs from the one emitted at the compute step. The consequence statement must
  identify at minimum: (a) the upstream contamination mechanism (e.g., a path that
  modifies or bypasses FLAG after the compute step breaks the guarantee of the affirmative
  closure), and (b) the downstream effect (e.g., A-1 will silently inherit a corrupted
  value that is indistinguishable from a correctly-computed one). Evidence: language such
  as "If any path modifies FLAG after this point, the guarantee stated above is broken:
  A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed
  one, producing the same silent category mismatch described at the consumption site." or
  equivalent. The gap closed: C-21's affirmative closure asserts that every path carries
  the value and no path is exempt, but does not explain WHY the executor should treat
  violation as serious -- an executor under pressure may deprioritize an unexplained
  positive-obligation statement. Naming the upstream consequence at the compute site makes
  the cost of violation visible at the point of the guarantee, mirroring the role C-20
  plays at the consumption site. Artifacts that fail C-21 fail C-23 automatically.

**C-24** -- Anti-displacement closure at the consumption site includes a no-instruction-
exempt affirmative closure.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-22 requires the anti-displacement closure to include a catch-all
  clause covering instruction types not explicitly listed; C-24 requires the closure to
  additionally conclude with a positive-obligation statement asserting that every instruction
  in the step -- whether named in the enumeration or reached by the catch-all -- is governed
  by the FLAG prohibition, and that no instruction in the step is exempt. Two components
  are required: (a) a positive-coverage statement asserting that every instruction in the
  step is subject to the rule (e.g., "Every instruction in this step -- named or unnamed --
  is governed by this rule"), and (b) an explicit no-exemption statement (e.g., "No
  instruction in this step is exempt"). The gap closed: C-22's catch-all covers unlisted
  instruction types by inclusion -- "or any other instruction in this step" is a negative
  bound that adds to the named list; C-24's affirmative closure states coverage as a
  positive fact and eliminates the residual interpretive ambiguity that even a catch-all
  can leave, where an executor might read "or any other" as limited to the same semantic
  category as the three named types. The pattern mirrors C-21 (positive-obligation +
  no-exemption applied to path enumeration at the compute site) applied to instruction
  enumeration at the consumption site, completing the structural symmetry between the two
  prohibition sites. Artifacts that fail C-22 fail C-24 automatically.

**C-25** -- Compute-site failure-consequence statement frames the violation explicitly as
breaking the affirmative closure guarantee.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-23 requires the compute-site prohibition to include a
  failure-consequence statement naming the contamination mechanism and downstream effect;
  C-25 requires the consequence statement to additionally frame the violation as explicitly
  breaking the positive guarantee asserted by the C-21 affirmative closure. The framing
  must name the guarantee as the thing that is broken -- not merely state the downstream
  effect -- creating an explicit causal bridge between the guarantee ("Every execution path
  that reaches A-1 carries the FLAG value emitted here. No path is exempt.") and the
  consequence ("the guarantee stated above is broken"). Evidence: language such as "If any
  path modifies FLAG after this point, the guarantee stated above is broken: A-1 will
  inherit a corrupted value..." or "this violates the closure guarantee asserted above --
  A-1 inherits a corrupted value..." or equivalent. The gap closed: a minimal C-23 pass
  names the mechanism (modification after compute step) and the effect (corrupted value
  indistinguishable from correct), but an executor who skims the consequence statement
  without reading the C-21 closure may not connect the two; the guarantee-break framing
  makes the causal chain explicit at the point of the consequence, so the consequence is
  understood as a violation of a stated commitment rather than an independent risk.
  Artifacts that fail C-23 fail C-25 automatically.

**C-26** -- Compute-site failure-consequence statement cross-references the consumption-site
failure-consequence statement.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-23 requires the compute-site prohibition to include a
  failure-consequence statement; C-26 requires the consequence statement to additionally
  include an explicit cross-reference to the consumption-site failure-consequence (C-20),
  naming the shared failure mechanism by its description at the other site. The cross-
  reference establishes that the failure observed at the consumption site (a category
  mismatch invisible to downstream tooling) is the same failure produced by a violation at
  the compute site, making the structural symmetry between the two prohibition sites
  explicit and navigable. Evidence: language such as "producing the same silent category
  mismatch described at the consumption site," "the same inertia risk named at A-1 applies
  here," or equivalent that names the consumption-site consequence by reference. The gap
  closed: without a cross-reference, the compute-site consequence (C-23) and the
  consumption-site consequence (C-20) are two isolated statements that a reader at either
  site must independently discover describe the same failure; an explicit cross-reference
  closes the navigation gap and reinforces the mirrored structure of the two escalation
  chains. Artifacts that fail C-23 fail C-26 automatically. Artifacts where C-20 is not
  present at the consumption site cannot satisfy C-26 (no target to reference).

**C-27** -- Guarantee-break framing and cross-site reference each appear as structurally
isolated, individually scannable units.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-25 requires the guarantee-break framing and C-26 requires the
  cross-site reference; C-27 requires each to appear as a structurally isolated,
  independently scannable unit rather than as a subordinate clause or end-of-paragraph
  appendage embedded within a longer failure-consequence statement. In tabular form: each
  claim occupies its own dedicated, labeled row in the prohibition table so that a reader
  scanning the table encounters it as a discrete entry and cannot skim past it as a
  trailing qualification. In prose form: each claim occupies its own clearly delimited
  statement -- a separate sentence ending at a full stop, not a participial phrase or
  relative clause appended to the consequence sentence. The gap closed: both claims can
  pass C-25 and C-26 as clauses embedded in a single consequence sentence
  ("the guarantee stated above is broken: A-1 will inherit a corrupted value...producing
  the same silent category mismatch described at the consumption site") -- the claims are
  present and machine-readable but a fast reader processing the sentence as a unit may
  register only the core consequence and treat the causal bridge and cross-reference as
  qualifying detail rather than as independently binding constraints; isolation removes
  this skimmability risk by making each claim a first-class structural entry that must be
  processed on its own terms. Artifacts that fail C-25 or C-26 fail C-27 automatically.

**C-28** -- Cross-site reference includes a navigation anchor naming the specific structural
location of the consumption-site target.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-26 requires the compute-site consequence to cross-reference the
  consumption-site failure-consequence by naming the shared failure description; C-28
  requires the cross-reference to additionally include a structural navigation anchor that
  names the specific location of the reference target -- not merely a generic site
  description ("at the consumption site") but a pointer to the specific step, row, or
  section where C-20's consequence statement appears (e.g., "see A-1 Failure consequence
  row below," "as described in the A-1 consequence statement," "Step A-1, Failure
  consequence section"). The navigation anchor turns a semantic reference (same failure
  described somewhere at the other site) into a navigable pointer (same failure described
  at this specific, findable location). A one-directional anchor (S-3 names A-1's location)
  satisfies C-28; the full bidirectional form where A-1 correspondingly marks itself as the
  reference destination is captured as C-29. The gap closed: a generic "at the consumption
  site" cross-reference (C-26 pass) tells the reader that a companion statement exists but
  requires a full document scan to locate it; a location-specific anchor reduces the
  navigation cost to a single jump and reinforces the structural symmetry of the two
  escalation chains by making both ends of the link explicitly findable. Artifacts that
  fail C-26 fail C-28 automatically. Artifacts that fail C-27 fail C-28 automatically
  (a non-isolated cross-reference cannot carry a navigation anchor as a first-class
  structural element).

**C-29** -- Consumption-site target carries a bidirectional anchor identifying itself as
the reference destination for the compute-site cross-reference.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-28 requires the compute-site cross-reference to name A-1's specific
  structural location (forward anchor); C-29 requires A-1's Failure consequence row or
  block to correspondingly carry an explicit self-identification marker naming S-3 as the
  source of the cross-reference (backward anchor), so that the structural link is
  discoverable from either direction. Evidence: A-1 includes a marker such as
  `[Target of S-3 Cross-site reference row above]` (V-01 pattern), `[This row is the
  target named in S-3 Cross-site reference row above]` (V-04 pattern), or equivalent
  language that names S-3 as the source and identifies A-1 as the designated destination.
  The gap closed: a one-directional anchor (C-28 pass) requires the reader to navigate
  from S-3 to find A-1; a reader arriving at A-1 from a scan or from a different entry
  point has no signal that this row is the structural link target for S-3's cross-reference;
  a bidirectional anchor ensures both ends are explicitly labeled so the link is
  discoverable and verifiable from either site without requiring a prior traversal.
  Artifacts that fail C-28 fail C-29 automatically.

**C-30** -- Cross-reference links use structured bracket token notation at both sites.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-29 requires bidirectional markers at both sites using natural-
  language or structural descriptions; C-30 requires those markers to use structured bracket
  token identifiers that encode the step and row-type as a scannable token pair. In the
  forward direction (S-3 naming A-1): a token such as `[A-1:FC]` (step colon row-type
  abbreviation) appears in the row label or cell, replacing or augmenting prose descriptions.
  In the backward direction (A-1 naming S-3): a companion token such as `[S-3:CS]` appears
  alongside the self-identification marker, explicitly forming a parseable token pair. Both
  directions must carry bracket tokens for a PASS -- bracket notation at S-3 without a
  corresponding token at A-1 (or vice versa) fails this criterion. Evidence: V-02 pattern
  -- S-3 row label carries `[A-1:FC]`, A-1 carries `[A-1:FC] sourced from [S-3:CS]`; V-05
  pattern -- bracket tokens appear in both row labels and cell content with the token pair
  `[S-3:CS]` / `[A-1:FC]` forming the complete link identifier. The gap closed:
  natural-language location descriptions (C-29 pass) are human-readable but require prose
  parsing to extract the step and row references; bracket token notation creates a
  structured, scannable identifier that a reader or tool can match without parsing
  surrounding context, reducing navigation cost and misidentification risk in dense
  prohibition tables. Artifacts that fail C-29 fail C-30 automatically.

**C-31** -- A pre-chain protocol preamble orients all cross-reference tokens before any
prohibition row is read.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-30 requires bracket token notation at both sites forming a parseable
  token pair; C-31 requires a dedicated orientation block positioned before all prohibition
  rows that names every cross-reference token pair used in the chain, states what each
  identifier resolves to (step name and row type), and establishes the complete bidirectional
  link structure before the reader encounters any individual row. The preamble must appear
  as a structurally distinct unit -- a labeled section, header block, or protocol note --
  not as a comment embedded in a row. Evidence: V-05 pattern -- a preamble section names
  `[S-3:CS]` (S-3 Cross-site reference row) and `[A-1:FC]` (A-1 Failure consequence row),
  states the relationship between them (S-3 references A-1; A-1 identifies itself as mutual
  target), and appears before the first prohibition row so a reader can understand the
  complete cross-reference structure without traversing the chain sequentially. The gap
  closed: bracket tokens at the use site (C-30 pass) are machine-parseable but require the
  reader to visit both rows to assemble the full link picture; a preamble places the
  complete chain map at a single orientation point, enabling a reader to verify
  bidirectionality, confirm token pairing, and locate any specific node in the chain
  without prior traversal -- reducing cognitive load from O(rows visited) to O(1) for the
  chain orientation task. Artifacts that fail C-30 fail C-31 automatically.

**C-32** -- Protocol preamble is positioned before all FLAG computation cases, not only
before prohibition rows.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-31 requires a dedicated preamble positioned "before all prohibition
  rows"; C-32 requires that preamble to additionally appear before all FLAG computation
  cases -- i.e., at the very top of the compute step, before the first case evaluation,
  not between the computation rows and the prohibition chain. An executor who reads the
  preamble before encountering any FLAG-related logic has the cross-reference map available
  when processing both the computation and the prohibition rows. Evidence: Round 11 V-01
  pattern -- "Cross-reference protocol:" block appears at the very top of S-3, before
  computation cases AND before the FLAG immutability chain, so the executor has protocol
  context before encountering FLAG cases. The gap closed: a C-31 preamble positioned
  between computation cases and prohibition rows (the R10 V-05 form and the R11 V-02 form)
  requires the executor to have already processed the FLAG computation before orienting to
  the cross-reference structure; if the computation cases are the most cognitively loaded
  part of the step, the preamble arrives too late to scaffold that processing. Pre-
  computation positioning ensures the map is established before any FLAG-related logic is
  encountered in the step, at zero additional cognitive cost. Artifacts that fail C-31 fail
  C-32 automatically.

**C-33** -- Protocol preamble uses a structured token resolution table with abbreviation
key.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-32 requires the preamble to appear before all computation cases as
  a structurally distinct block; C-33 requires that block to present its token mapping in a
  structured resolution table rather than prose, consisting of two components: (a) an
  abbreviation key that names the row-type suffix codes used in the token notation (e.g.,
  `:CS = Cross-site reference row`, `:FC = Failure consequence row`), making the encoding
  scheme self-documenting at the preamble rather than implicit, and (b) a resolution table
  with at minimum four columns -- Token, Step, Row type, and Paired token -- mapping each
  token to its structural location, the type of row it identifies, the token it is paired
  with, and the direction of the link. Evidence: Round 11 V-02 pattern -- abbreviation key
  defines `:CS` and `:FC`, then a five-column table (Token / Step / Row type / Paired token
  / Direction) maps `[S-3:CS]` and `[A-1:FC]` with explicit direction indicators
  (`forward --> names A-1`, `<-- backward, names S-3`). The gap closed: a prose preamble
  (C-31/C-32 pass) presents the cross-reference map as a text block the reader must parse
  in natural language -- understanding requires reading the prose, identifying the token
  names, and mentally constructing the bidirectional link structure; a structured resolution
  table enables O(1) lookup by token name: a reader or tool arriving at any bracket token
  can locate the preamble table row for that token and read off its step, row type, paired
  counterpart, and direction without parsing surrounding prose, reducing lookup cost and
  misidentification risk in preambles that may grow as cross-reference chains expand.
  Artifacts that fail C-32 fail C-33 automatically.

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)
```

PARTIAL counts as 0.5 for any criterion.

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Essential (5x) | Recommended (3x) | Aspirational (25x) |
|------|---------------|-----------------|-------------------|
| Points | 60 | 30 | 10 |
| Formula | pass/5 x 60 | pass/3 x 30 | pass/25 x 10 |

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Output is usable as a mock artifact |
| Silver | >= 60, all essential pass | Usable but fidelity warnings or next-step missing |
| Bronze | >= 60, some essential fail | Structurally present but unreliable for downstream use |
| Fail | < 60 or any essential fail | Not safe to use; regenerate |

---

## Escalation chains

| Compute site | Consumption site |
|---|---|
| C-14 prohibit | C-14 prohibit |
| C-16 run-scoped | C-17 first rule |
| C-18 named classes | C-19 named types + closure |
| C-21 affirmative closure | C-22 catch-all type |
| C-23 failure consequence | C-20 failure consequence |
| C-25 guarantee-break framing | C-24 no-instruction-exempt affirmative |
| C-26 cross-site reference | |
| C-27 isolated units | |
| C-28 navigation anchor (forward) | |
| C-29 bidirectional anchor | C-29 bidirectional anchor |
| C-30 bracket tokens | C-30 bracket tokens |
| C-31 pre-chain preamble | |
| **C-32 pre-computation positioning** | |
| **C-33 structured resolution table** | |

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
- **C-23 fail**: Affirmative closure at the compute site is present (C-21 passes) but
  carries no failure-consequence statement -- the executor is told every path carries the
  value and no path is exempt, but is not told what goes wrong if a path violates this
  guarantee. The upstream contamination mechanism (modified FLAG producing a silently
  corrupted value at A-1) is left implicit. Fails automatically when C-21 fails.
- **C-24 fail**: Catch-all instruction clause is present (C-22 passes) but the anti-
  displacement closure ends there without a positive-coverage affirmative -- the enumeration
  plus catch-all is a negative bound; without "Every instruction in this step is governed
  by this rule. No instruction is exempt." the coverage is asserted by exclusion rather
  than as a positive fact, leaving residual interpretive ambiguity for instruction types
  a reader might consider outside the semantic category of the named three. Fails
  automatically when C-22 fails.
- **C-25 fail**: Failure-consequence statement at the compute site is present (C-23 passes)
  but states the mechanism and effect without framing the violation as breaking the
  affirmative closure guarantee -- the consequence reads as an independent warning rather
  than as the cost of violating the specific positive commitment stated in C-21. The
  guarantee-break framing is the causal bridge that makes the consequence logically
  dependent on the closure, not merely adjacent to it. Fails automatically when C-23 fails.
- **C-26 fail**: Failure-consequence statement at the compute site is present (C-23 passes)
  but names no cross-reference to the consumption-site consequence (C-20) -- the two
  consequence statements remain isolated, and a reader at either site must independently
  discover that the other carries a companion description of the same failure. Fails
  automatically when C-23 fails. Also fails if C-20 is absent at the consumption site
  (no reference target exists).
- **C-27 fail**: Both C-25 and C-26 are present (both pass) but one or both appear as
  subordinate clauses embedded within a longer consequence sentence rather than as
  structurally isolated units -- the guarantee-break framing or the cross-site reference
  (or both) can be skimmed past as qualifying detail of the surrounding statement rather
  than processed as first-class constraints. In tabular form: the claims appear in a
  single consequence cell rather than as dedicated labeled rows. In prose form: the claims
  appear as participial phrases or relative clauses rather than as full, delimited
  statements. Fails automatically when C-25 or C-26 fails.
- **C-28 fail**: Cross-site reference is present and structurally isolated (C-26 and C-27
  pass) but names the target only by generic site description ("at the consumption site")
  without a location anchor -- a reader must scan the entire consumption-site section to
  find C-20's statement rather than being able to navigate directly to it. Fails
  automatically when C-26 or C-27 fails.
- **C-29 fail**: Forward navigation anchor is present at S-3 (C-28 passes) but A-1's
  Failure consequence row carries no backward self-identification marker -- a reader
  arriving at A-1 from a scan has no signal that this row is the designated target of S-3's
  cross-reference; the link is navigable in one direction only. The partial form (S-3 names
  A-1's location without a reciprocal marker at A-1) passes C-28 but fails C-29. Fails
  automatically when C-28 fails.
- **C-30 fail**: Bidirectional markers are present at both sites (C-29 passes) but use
  natural-language location descriptions rather than structured bracket token identifiers --
  the link is navigable but requires prose parsing to resolve step and row references;
  bracket tokens are absent or present at only one site (a forward token without a backward
  companion, or vice versa, fails this criterion because the token pair is incomplete). Fails
  automatically when C-29 fails.
- **C-31 fail**: Bracket token notation is present at both sites (C-30 passes) but no
  dedicated orientation block appears before the prohibition rows naming the token pairs
  and their resolutions -- a reader must visit both rows to assemble the full link picture
  rather than finding it at a single orientation point. An inline comment in a row that
  mentions the token pair is not sufficient; the preamble must appear as a structurally
  distinct block preceding all prohibition rows. Fails automatically when C-30 fails.
- **C-32 fail**: A C-31 preamble is present (C-31 passes) but is positioned between the
  FLAG computation cases and the prohibition rows rather than before the computation cases
  -- the executor encounters FLAG case evaluation before reading the cross-reference
  protocol, losing the orientation benefit during the most cognitively loaded part of the
  step. A preamble at the R10 V-05 / R11 V-02 position (after computation, before
  prohibition chain) passes C-31 but fails C-32. Fails automatically when C-31 fails.
- **C-33 fail**: Preamble is pre-computation (C-32 passes) but presents its token mapping
  in prose rather than a structured resolution table -- the cross-reference map requires
  natural-language parsing to extract token-to-location bindings rather than enabling O(1)
  lookup by token name. Missing either the abbreviation key (defining the `:CS` and `:FC`
  suffix codes) or the resolution table (columns: Token / Step / Row type / Paired token /
  Direction) fails this criterion; a prose preamble with bracket tokens mentioned inline
  does not satisfy the structural requirement. Fails automatically when C-32 fails.
