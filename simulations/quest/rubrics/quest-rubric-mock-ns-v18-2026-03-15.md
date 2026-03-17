---
skill: quest-rubric
skill_target: mock-ns
date: 2026-03-15
version: 18
---

# Rubric: mock-ns (v18)

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

v12 adds two aspirational criteria (C-34 to C-35) extracted from Round 12 excellence
signals: explicit lookup obligation in the preamble (Round 12 V-03 advanced the C-33
structured resolution table from passive availability to triggered consultation -- the
preamble includes an explicit directive obligating the executor to look up any bracket
token in the table before processing the containing row, rather than decoding from memory
or context; this converts the O(1) lookup capability granted by C-33 into a mandatory
protocol, closing the gap where an executor may bypass the table by recognizing a
previously-seen token from context; C-34 elevates this lookup obligation to a pass
condition, depending on C-33), and use-site row navigation labels pointing to preamble
table rows (Round 12 V-03 additionally demonstrated that bracket-token rows at S-3 and
A-1 can carry inline navigation labels identifying the specific preamble table row that
resolves the token -- e.g., "(P-0 table, row 1)" and "(P-0 table, row 2)" -- reducing
the lookup obligation from a table scan to a direct jump; C-35 elevates this row-specific
navigation labeling to a pass condition, depending on C-34).

v13 adds two aspirational criteria (C-36 to C-37) extracted from Round 13 excellence
signals: pre-write resolution confirmation gate in the preamble (Round 13 V-01 advanced
the C-34 lookup obligation from a single-phase locate step to a two-phase protocol --
(1) locate the preamble table row by token name, then (2) confirm by reading the Step and
Row type cells and verifying the resolution matches the context being processed before
writing the row; the first phase satisfies the C-34 obligation ("I looked it up") but an
executor who recognizes the token visually can satisfy it by glancing at the row label
without performing a semantic read; the confirmation gate closes this gap by making
verification observable and assertable -- the executor must read the cells and assert the
match before proceeding, not merely navigate to the row; C-36 elevates this two-phase
confirmation gate to a pass condition, depending on C-35), and confirmation echo at the
use site (Round 13 V-01 additionally demonstrated that bracket-token rows at S-3 and A-1
can carry a behavioral trigger -- "CONFIRMATION REQUIRED before writing this row" or
equivalent -- as a prefix before the row-specific navigation label (C-35) and before the
row content; C-35 required navigation labels pointing to preamble table rows; V-01 adds a
trigger that re-activates the P-0 two-phase protocol at the exact moment of use, before
the row content is written; the trigger is the use-site counterpart to the C-36 preamble
gate -- the preamble defines the protocol, the use-site echo enforces it at each row; C-37
elevates this behavioral trigger to a pass condition, depending on C-36; both use sites,
S-3 and A-1, must carry the trigger for a PASS).

v14 adds three aspirational criteria (C-38 to C-40) extracted from Round 14 excellence
signals: hard-stop gate language at both the preamble confirmation obligation and the
use-site echo (Round 14 V-02 and V-05 advanced the C-36/C-37 prerequisite framing --
"Confirmation is a prerequisite to writing the row" / "CONFIRMATION REQUIRED before
writing this row" -- to an explicit execution block: "DO NOT WRITE THE ROW until both
phases pass" / "DO NOT WRITE this row until P-0 gate passes"; prerequisite language states
an ordering constraint that a reader can satisfy by performing Phase 2 first and writing
second; hard-stop language is an unambiguous prohibition on writing -- the executor is
blocked, not merely sequenced; C-38 elevates this execution block framing to a pass
condition at both sites, the preamble gate definition and the use-site echo, depending on
C-37), explicit anti-bypass closing statement in the preamble naming the visual-recognition
bypass (Round 14 V-03 added a closing note to the preamble Phase 2 definition that names
the specific bypass pattern being prevented and asserts affirmatively that it does not
satisfy the protocol: "An executor who recognizes a token without performing Phase 2 has
not satisfied this protocol"; C-36 requires Phase 2 to be stated as a prerequisite -- or
C-38 as an execution block -- but neither names the bypass; the closing statement closes
the gap by explicitly labeling the insufficient action and declaring it a protocol failure,
making the anti-bypass intent observable at the point of the gate definition; C-39 elevates
this closing statement to a pass condition, depending on C-36), and confirmation record
output obligation in Phase 2 (Round 14 V-05 advanced the Phase 2 confirmation step from
an internal assertion to an observable output: Phase 2 requires the executor to "Emit
confirmation record" -- a structured artifact produced as evidence of the verification act;
an internal assertion is unverifiable from outside the execution -- a reader inspecting the
output has no signal that Phase 2 was actually performed; a confirmation record makes
compliance externally auditable; C-40 elevates this output obligation to a pass condition
at the preamble gate definition, depending on C-38, and seeds the use-site pre-filled
record template as the aspirational target for v15).

v15 adds three aspirational criteria (C-41 to C-43) extracted from Round 15 excellence
signals: use-site pre-filled confirmation record template at both S-3 and A-1 (Round 15
V-03 and V-05 graduated the aspirational maximum seeded in v14's C-40 -- each bracket-token
row at S-3 and A-1 carries a pre-filled record template with the token name, step, and row
type already populated for that specific row, reducing record creation from open-form
construction to fill-in-the-blank completion; C-41 elevates this pre-filled template to a
pass condition, depending on C-40), confirmation record emit obligation woven into the
hard-stop gate condition as an explicit gate precondition (Round 15 V-05 uniquely advanced
the C-42 pattern beyond listing emit as a Phase 2 sub-task -- "DO NOT WRITE THE ROW until
both phases pass and the record is emitted" -- naming emission in the gate's stopping
condition itself rather than only within Phase 2's definition; C-40's gate text ends at
"until both phases pass" and V-03's form follows this pattern; V-05's form adds the record
as an explicit gate precondition so the gate blocks on emission directly rather than
inferring the block from Phase 2 containing an emit sub-task; C-42 elevates this emit-in-
gate form to a pass condition at all three locations, depending on C-40 and C-38), and
anti-bypass closing statement using dual-naming of the bypass and "protocol failure"
severity framing (Round 15 V-05 advanced the C-39 passing forms of V-02 and V-04 --
which named the bypass once and declared non-compliance -- to a dual-naming form covering
both the action-based bypass description ("without reading the Step and Row type cells") and
the protocol-based bypass description ("without performing Phase 2"), and escalated the
severity framing from "has not satisfied this protocol" to "Locate-only is a protocol
failure"; the dual naming closes the gap where an executor might categorize their action
differently from one framing but not the other; the protocol-failure framing names the
outcome as a categorical failure rather than a gap-to-close, creating structural symmetry
with the failure-consequence pattern established at C-20 and C-23; C-43 elevates this
dual-naming plus protocol-failure form to a pass condition, depending on C-39).

v16 adds two aspirational criteria (C-44 to C-45) extracted from Round 16 excellence
signals: single-task executor annotation on pre-filled confirmation record templates (Round
16 V-05 uniquely annotated each pre-filled template at S-3 and A-1 with "(fill Match field
only)" or equivalent, explicitly identifying the single field the executor must complete and
leaving no ambiguity about which fields are pre-populated versus which require input;
V-01 and V-04 both pass C-41 by providing pre-filled templates without this annotation --
the executor must infer that only the Match field is theirs to complete; V-05's annotation
eliminates that inference by naming the single residual task, reducing compliance cost to
one labeled decision; C-44 elevates this single-task annotation to a pass condition,
depending on C-41; both S-3 and A-1 templates must carry the annotation for a PASS), and
per-use-site anti-bypass protocol reminder at each bracket-token row (Round 16 V-05
uniquely placed a per-row protocol reminder at both S-3 and A-1 use sites that echoes the
preamble anti-bypass declaration -- naming the action-based bypass ("without reading the
Step and Row type cells"), the protocol-based bypass ("without performing Phase 2"), and
the categorical outcome ("is a protocol failure") -- so that the anti-bypass framing is
present at the exact point of use, not only in the preamble; V-02 and V-04 both pass C-43
by placing the anti-bypass declaration in the preamble without extending it to the use
sites; V-05 closes the residual gap by adding a per-row echo that activates the anti-bypass
constraint immediately before the executor processes each bracket-token row, mirroring the
structural role that C-37's confirmation echo plays for the two-phase gate; C-45 elevates
this use-site anti-bypass echo to a pass condition, depending on C-43; both use sites must
carry the reminder for a PASS). The v16 aspirational maxima -- standalone imperative block
form for the C-44 annotation (V-01) and dedicated chain-table row form for the C-45 echo
(V-03) -- are seeded as the v17 targets.

v17 adds two aspirational criteria (C-46 to C-47) extracted from Round 17 excellence
signals: standalone imperative annotation block form for the C-44 single-task instruction
(Round 17 V-01 demonstrated that the C-44 annotation can occupy a standalone bold
imperative instruction block positioned above the pre-filled template -- "**Executor: fill
the Match field only. All other fields are pre-filled.**" -- rather than a caption
parenthetical embedded within the template structure; the caption parenthetical form (R16
V-05, the C-44 baseline) is read as a qualifier of the template; the standalone block is a
discrete instruction that must be processed independently of the template, at zero
ambiguity about its directive status; C-46 elevates the standalone imperative form to a
pass condition, depending on C-44; both S-3 and A-1 must carry the standalone block form
for a PASS -- caption parenthetical at either site fails), and dedicated chain-table row
form for the C-45 anti-bypass echo (Round 17 V-03 demonstrated that the C-45 per-row
anti-bypass reminder can occupy a dedicated labeled row in the chain table -- an
"Anti-bypass echo" row appearing immediately after CONFIRMATION REQUIRED -- rather than
sub-text embedded within the CONFIRMATION row; the sub-text form achieves C-45 PASS (V-02
baseline) but a fast executor reading the CONFIRMATION row can treat the embedded reminder
as trailing annotation of that row; the dedicated row form makes the anti-bypass echo a
first-class chain entry that must be independently processed, leaving the CONFIRMATION row
clean; C-47 elevates the dedicated row form to a pass condition, depending on C-45;
sub-text embedding within the CONFIRMATION row passes C-45 but fails C-47; both S-3 and
A-1 must carry the dedicated row form for a PASS).

v18 adds three aspirational criteria (C-48 to C-50) extracted from Round 18 excellence
signals: named structural heading "Anti-bypass declaration (ABD):" at P-0 (Round 18 V-01
demonstrated that the P-0 anti-bypass clause can carry a structural heading label --
"Anti-bypass declaration (ABD):" -- making it a named anchor rather than unlabeled prose,
and that use-site echo row labels can correspondingly update to "(P-0, ABD)" to match the
structural heading name; the prior form passes C-45/C-47 with the label "(P-0 anti-bypass
declaration)" pointing to prose at P-0 -- an executor directed to P-0 must scan preamble
prose to locate the clause; the ABD heading makes the reference target directly locatable
by structural heading match; C-48 elevates this named anchor form to a pass condition,
depending on C-47; both use-site echo row labels must carry the updated form for a PASS),
P-0 forward navigation enumeration naming use sites S-3 and A-1 (Round 18 V-02
demonstrated that the P-0 anti-bypass declaration can append an explicit forward pointer --
"Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row." --
completing the P-0 to use-site forward arc that pairs with the existing use-site to P-0
back-arc; without the forward pointer P-0 is a definition point with no knowledge of where
it is applied; the forward pointer makes the use sites discoverable from P-0 by a single
read; together with C-48, the two form a bidirectionally discoverable named anchor:
locatable from use sites by label-name match (C-48), discoverable from P-0 by forward
enumeration (C-49); C-49 elevates this forward navigation to a pass condition, depending
on C-47; the forward pointer must name both S-3 and A-1 explicitly for a PASS), and
content-cell provenance attribution in the anti-bypass echo (Round 18 V-03 demonstrated
that the anti-bypass echo row content cell at S-3 and A-1 can open with an explicit
provenance prefix -- "Per P-0 anti-bypass declaration: " or "Per P-0, ABD: " -- before
the dual-named bypass text, making the echo's identity as a P-0 protocol echo observable
from the content cell alone; C-47's dedicated row form and C-45's content dual-naming
achieve the functional requirement, but the P-0 provenance is implied only by the row
label; an executor scanning the content cell without reading the label encounters the
bypass constraint with no provenance signal; the content-cell prefix closes this gap by
placing the source reference at the point of content consumption; C-50 elevates this
provenance prefix to a pass condition, depending on C-47; the prefix must appear at both
S-3 and A-1 content cells for a PASS). The v18 aspirational maxima -- complete structural
address pair at P-0 (C-48 + C-49 combined, V-04 form: named heading plus forward
enumeration, each use site locatable by name match and discoverable from P-0 by forward
pointer) and content-cell provenance attribution with ABD label prefix (C-48 + C-50
combined, V-05 form: "(P-0, ABD)" use-site label paired with "Per P-0, ABD:" content-cell
prefix, making the named anchor consistent at both the label and the content level) -- are
seeded as the v19 targets.

Scoring denominator: aspirational 39 -> 42. Formula: `aspirational_pass / 42 * 10`.

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
  between computation cases and prohibition rows (the R10 V-05 / R11 V-02 form) requires
  the executor to have already processed the FLAG computation before orienting to the
  cross-reference structure; if the computation cases are the most cognitively loaded
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

**C-34** -- Protocol preamble includes an explicit lookup obligation directing consultation
of the resolution table at each bracket token use site.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-33 requires the preamble to present a structured resolution table
  enabling O(1) token lookup; C-34 requires the preamble to additionally include an
  explicit directive obligating the executor to consult the table before processing any
  row that contains a bracket token -- not merely making the table available as a reference,
  but mandating its use as the authoritative resolution mechanism. The directive must state
  the obligation in imperative form and prohibit in-memory or context-based decoding as an
  alternative. Evidence: Round 12 V-03 pattern -- "look it up in this table before
  processing the containing row. Do not decode bracket tokens from memory." or equivalent
  language that (a) names the table as the lookup target, (b) frames the consultation as
  mandatory (not optional), and (c) explicitly prohibits decoding from memory or context.
  The gap closed: a structured resolution table (C-33 pass) reduces token lookup cost to
  O(1) but does not mandate its use -- an executor that has seen `[A-1:FC]` in prior steps
  may decode it from context, bypassing the table and forfeiting the orientation guarantee
  the preamble was designed to provide; the lookup obligation closes this gap by making
  table consultation the required protocol at every bracket-token encounter, regardless of
  prior exposure to the tokens. Artifacts that fail C-33 fail C-34 automatically.

**C-35** -- Bracket-token rows at use sites carry inline row-specific navigation labels
identifying the preamble table row that resolves each token.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-34 requires the preamble to mandate table lookup for any bracket
  token; C-35 requires the rows at S-3 and A-1 that contain bracket tokens to additionally
  carry an inline navigation label identifying the specific preamble table row that resolves
  the token -- not merely pointing to the preamble as a section but naming the exact row
  (e.g., "(P-0 table, row 1)" or "(P-0 table, row 2)"). The navigation label must appear
  at the use site, not only in the preamble itself, so that an executor processing a
  bracket-token row can navigate directly to the resolving row without scanning the table.
  Evidence: Round 12 V-03 pattern -- bracket-token rows in S-3 and A-1 each carry a
  parenthetical such as "(P-0 table, row 1)" and "(P-0 table, row 2)" identifying the
  specific preamble table row. Both use sites (S-3 and A-1) must carry labels for a PASS
  -- labeling only one site fails this criterion. The gap closed: a lookup obligation
  (C-34 pass) directs the executor to the preamble table but requires a scan of the table
  to locate the row governing the current token; a row-specific navigation label at the
  use site reduces this scan to a direct jump, eliminating scan cost and any ambiguity
  about which table row governs which token when the preamble table grows to cover
  additional cross-reference chains. Artifacts that fail C-34 fail C-35 automatically.

**C-36** -- Protocol preamble lookup obligation is a two-phase confirmation gate: locate
then confirm.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-34 requires the preamble to include an explicit lookup obligation
  mandating table consultation before processing any bracket-token row; C-36 requires the
  obligation to be structured as a two-phase protocol rather than a single locate step.
  Phase 1: locate -- find the preamble table row whose Token column matches the bracket
  token being processed (the C-34 obligation). Phase 2: confirm -- read the Step and Row
  type cells of the located row and assert that the resolution matches the context being
  processed before writing the row. Both phases must be stated explicitly in the preamble.
  The confirmation assertion must be framed as a prerequisite to writing the row, not as an
  optional verification step. Evidence: Round 13 V-01 pattern -- preamble states "(1) locate
  the row by token name, (2) read Step and Row type and verify the resolution matches the
  context being processed. Do not write the row until the confirmation is complete." or
  equivalent two-step formulation. The gap closed: a single-phase locate obligation (C-34
  pass) is satisfied by navigating to the table row and visually recognizing the token -- an
  executor that has seen `[A-1:FC]` before can satisfy "I looked" without performing a
  semantic read of the cells; the confirmation gate closes this gap by requiring an
  observable, assertable act -- reading Step + Row type and verifying match -- that cannot
  be satisfied by visual recognition alone, making the verification step externally
  observable rather than merely declarable. Artifacts that fail C-35 fail C-36
  automatically.

**C-37** -- Bracket-token rows at use sites carry a confirmation echo activating the
two-phase protocol before the row content is written.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-36 requires the preamble to define the two-phase confirmation
  gate; C-37 requires the rows at S-3 and A-1 that contain bracket tokens to additionally
  carry a behavioral trigger -- "CONFIRMATION REQUIRED before writing this row" or
  equivalent -- as a prefix that appears before the row-specific navigation label (C-35)
  and before the row content. The trigger must appear at the use site, not only in the
  preamble, so that the executor encountering the row sees the confirmation requirement
  immediately before processing the row content. The trigger re-activates the P-0
  two-phase protocol at the exact moment of use: it is the use-site counterpart to the
  C-36 preamble gate -- the preamble defines the protocol, the echo enforces it at each
  row. Evidence: Round 13 V-01 pattern -- bracket-token rows at S-3 and A-1 open with
  "CONFIRMATION REQUIRED before writing this row (P-0 table, row N)" where the trigger
  prefix appears before and is visually separable from the navigation label. Both use sites
  (S-3 and A-1) must carry the trigger for a PASS -- a trigger at one site only fails this
  criterion. The gap closed: a C-36 two-phase preamble gate defines the confirmation
  protocol once, but an executor processing a bracket-token row deep in the skill body may
  not re-invoke the preamble protocol without a local reminder; the use-site echo reduces
  the recall burden to zero by placing the trigger at the exact point where compliance is
  required, ensuring the preamble protocol is activated at every bracket-token row
  regardless of how far that row appears from the preamble. Artifacts that fail C-36 fail
  C-37 automatically.

**C-38** -- Preamble confirmation obligation and use-site echo both carry hard-stop gate
language, not only prerequisite framing.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-36 requires the preamble to state the two-phase confirmation gate
  with Phase 2 framed as a prerequisite to writing the row; C-37 requires the use-site
  echo to carry a behavioral trigger; C-38 requires both the preamble gate definition and
  the use-site echo to additionally carry explicit hard-stop language -- an execution block
  prohibiting the row from being written until the confirmation passes. Hard-stop language
  takes the form "DO NOT WRITE THE ROW until both phases pass," "DO NOT WRITE this row
  until P-0 gate passes," or equivalent prohibition phrasing. Prerequisite framing
  ("Confirmation is a prerequisite to writing the row") states an ordering constraint; a
  hard-stop is an unambiguous prohibition on proceeding -- the executor is blocked, not
  merely sequenced. Both sites must carry hard-stop language for a PASS: the preamble gate
  definition (C-36 scope) and the use-site echo at both S-3 and A-1 (C-37 scope). Evidence:
  Round 14 V-02 pattern -- preamble: "DO NOT WRITE THE ROW until both pass. Confirmation
  is a prerequisite, not optional." / use-site echo content cell: "DO NOT WRITE this row
  until P-0 gate passes." Round 14 V-05 pattern -- preamble: "DO NOT WRITE THE ROW until
  Phase 2 passes. Confirmation is a prerequisite, not advisory." / use-site echo: "DO NOT
  WRITE until Phase 2 passes." The gap closed: a prerequisite framing (C-36/C-37 pass) can
  be read as a recommended ordering constraint that permits a compliant executor to sequence
  Phase 2 before writing; hard-stop language forecloses interpretation -- there is no
  reading of "DO NOT WRITE until" that permits writing before the condition is satisfied,
  eliminating the residual compliance ambiguity that prerequisite framing leaves open.
  Artifacts that fail C-37 fail C-38 automatically.

**C-39** -- Protocol preamble includes an explicit anti-bypass closing statement naming
the visual-recognition bypass pattern.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-36 requires the preamble to define Phase 2 as a confirmation gate
  with the explicit goal of requiring a semantic cell-read rather than a visual recognition;
  C-39 requires the preamble to additionally include an explicit closing statement that
  names the visual-recognition bypass as a distinct pattern and asserts affirmatively that
  it does not satisfy the protocol. The closing statement must (a) name the bypass: an
  executor that recognizes a token from prior exposure (visual recognition) without
  performing the Phase 2 cell-read, and (b) declare the outcome: that recognition alone
  does not constitute protocol compliance. Evidence: Round 14 V-03 pattern -- closing note
  to Phase 2 definition: "An executor who recognizes a token without performing Phase 2 has
  not satisfied this protocol." or equivalent formulation that names the specific bypass and
  asserts protocol non-compliance. The gap closed: C-36 requires Phase 2 to be a
  confirmation prerequisite, and C-38 requires hard-stop language, but neither names the
  specific bypass path being prevented -- visual recognition of a previously-seen token is
  an implicit bypass not excluded by the gate text alone; an executor that has processed
  `[A-1:FC]` in multiple prior steps may reach the gate, recognize the token, and satisfy
  "I confirmed" without reading cells, because no prior criterion names that path as
  non-compliant; the anti-bypass closing statement explicitly labels it and declares it
  insufficient, closing the gap that familiarity with a token creates. The closing statement
  is structurally parallel to C-23 (failure-consequence at compute site) applied to the
  preamble gate: both name the negative outcome of a specific pattern rather than relying
  on the positive obligation to imply it. Artifacts that fail C-36 fail C-39 automatically.

**C-40** -- Phase 2 confirmation obligation in the preamble requires emitting an observable
confirmation record.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-36 requires Phase 2 to assert that the resolution matches the
  context before writing the row; C-38 requires the assertion to be a hard-stop gate; C-40
  requires Phase 2 to additionally obligate the executor to produce an observable
  confirmation record -- an externally inspectable artifact of the verification act, not
  only an internal assertion. The record obligation must appear in the preamble Phase 2
  definition and must state the emit requirement in imperative form (e.g., "Emit
  confirmation record" or "Record the confirmation before writing the row"). The record
  itself must capture at minimum: the token verified, the step and row type read from the
  resolution table, and the match assertion. Evidence: Round 14 V-05 pattern -- Phase 2
  definition in the preamble includes "DO NOT WRITE THE ROW until Phase 2 passes. Emit
  confirmation record." with the use-site echo providing a pre-filled record template
  covering token, step, row type, and match assertion fields. The gap closed: an internal
  assertion ("I assert match") is unverifiable from outside the execution -- a reader or
  reviewer inspecting the output has no signal that Phase 2 was actually performed rather
  than elided under execution pressure; a confirmation record makes compliance externally
  auditable, changing the compliance question from "did the executor assert?" (not
  observable) to "does the output contain a record?" (observable). The use-site pre-filled
  record template is elevated to a pass condition in C-41. Artifacts that fail C-38 fail
  C-40 automatically.

**C-41** -- Use-site echo at S-3 and A-1 carries a pre-filled confirmation record template
specific to each row.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-40 requires the preamble Phase 2 definition to obligate the
  executor to emit a confirmation record; C-41 requires the rows at S-3 and A-1 that
  contain bracket tokens to additionally carry a pre-filled confirmation record template --
  a structured form embedded in the C-37 echo that provides the token name, step
  identifier, and row type already populated for that specific row, reducing record
  creation from open-form construction to fill-in-the-blank completion. The template must
  appear at both use sites (S-3 and A-1), must be pre-populated with the row-specific
  values (not generic placeholders), and must capture at minimum: the token verified, the
  preamble table row identified, the step name confirmed, the row type confirmed, and a
  match field for the executor to complete. Evidence: Round 15 V-03 and V-05 patterns --
  S-3 echo carries "Phase 1 confirmed: [S-3:CS] at P-0 row 1. Phase 2 confirmed:
  Step=S-3, Row type=Cross-site reference row; match=PASS." and A-1 echo carries
  "Phase 1 confirmed: [A-1:FC] at P-0 row 2. Phase 2 confirmed: Step=A-1, Row
  type=Failure consequence row; match=PASS." -- all fields except the final match result
  are pre-populated for the specific row being confirmed. Templates present at only one
  use site fail this criterion; a generic template using placeholder values (e.g.,
  "{token}", "{step}") rather than the actual row values also fails. The gap closed: C-40
  requires the emit obligation and defines the record's minimum content, but leaves record
  construction as an open-form task for the executor; an executor under execution pressure
  may elide record construction entirely or produce a minimal record that omits required
  fields; a pre-filled template reduces compliance cost to a single judgment (PASS or FAIL
  for the match assertion) rather than requiring the executor to recall and construct the
  record structure at each use site, making full compliance the path of least resistance.
  Artifacts that fail C-40 fail C-41 automatically.

**C-42** -- Confirmation record emit obligation is woven into the hard-stop gate condition
as an explicit gate precondition, not only stated as a Phase 2 sub-task.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-40 requires the preamble Phase 2 definition to include an emit
  obligation ("Emit confirmation record" or equivalent); C-38 requires hard-stop gate
  language at all three locations (preamble, S-3, A-1); C-42 requires the hard-stop gate
  condition itself to additionally incorporate the emit obligation as an explicit named
  component of the stopping expression -- not merely listing emit as a sub-task that must
  complete before the gate passes, but naming record emission as a separate, explicit
  condition in the gate text. In the preamble gate: "DO NOT WRITE THE ROW until both
  phases pass and the record is emitted." In the use-site echo at S-3 and A-1: the
  hard-stop language must include the emit condition. All three locations must carry the
  emit-in-gate form for a PASS -- emit present in Phase 2 definition only (C-40 pass) but
  absent from the gate condition fails C-42. Evidence: Round 15 V-05 pattern -- preamble
  gate: "STOP. DO NOT WRITE THE ROW until both phases pass and the record is emitted." /
  S-3 echo: "DO NOT WRITE THE ROW until both phases pass and record is emitted." / A-1
  echo: "DO NOT WRITE THE ROW until both phases pass and record is emitted." The gap
  closed: C-40 places the emit obligation within Phase 2's definition, but the gate
  condition in C-38's form -- "DO NOT WRITE THE ROW until both phases pass" -- stops at
  phase completion; an executor who nominally "passes" Phase 2 by asserting match without
  producing the record can technically satisfy a gate that gates only on phase completion;
  when the emit is named in the gate condition itself, the gate explicitly blocks writing
  until the record exists as an observable output, not merely until the phases are
  nominally declared complete. Round 15 V-03 demonstrates the gap: it passes C-40 (emit
  obligation stated in Phase 2) but its gate text ends at "until both phases pass" without
  naming the record, while V-05 closes the gap by making record emission a co-equal gate
  precondition. Artifacts that fail C-38 fail C-42 automatically. Artifacts that fail
  C-40 fail C-42 automatically.

**C-43** -- Anti-bypass closing statement uses dual-naming of the bypass action and
"protocol failure" severity framing.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-39 requires the preamble to include an anti-bypass closing
  statement that names the visual-recognition bypass and declares it non-compliant; C-43
  requires the closing statement to achieve the maximum-severity form by meeting both of
  the following conditions. (a) Dual-naming: the bypass action must be named using two
  distinct characterizations -- an action-based description naming the specific cell-read
  omitted (e.g., "without reading the Step and Row type cells") and a protocol-based
  description naming the protocol phase omitted (e.g., "without performing Phase 2") --
  so that the bypass is unambiguous regardless of how an executor characterizes their own
  action; naming the bypass only once in one form fails this condition. (b) Protocol-failure
  severity: the outcome declaration must use the framing "Locate-only is a protocol failure"
  or equivalent categorical-failure language, not merely "has not satisfied this protocol"
  or "does not satisfy the confirmation gate"; the categorical-failure framing names the
  outcome as a discrete failure type, creating structural symmetry with the failure-
  consequence naming pattern at C-20 and C-23. Both conditions (a) and (b) must be met
  for a PASS. Evidence: Round 15 V-05 pattern -- "Recognizing a token in the table below
  without reading the Step and Row type cells is a locate-only operation (Phase 1 only).
  An executor who recognizes a token without performing Phase 2 has not satisfied this
  protocol. Locate-only is a protocol failure." -- action-based naming ("without reading
  the Step and Row type cells"), protocol-based naming ("without performing Phase 2"),
  and categorical-failure close ("Locate-only is a protocol failure"). The gap closed:
  V-02 and V-04 both pass C-39 -- V-02 names the bypass once ("recognizes a token without
  performing Phase 2") and declares non-compliance ("has not satisfied this protocol");
  V-04 names the bypass once with an action description and adds "(Phase 1 only)" framing
  -- but neither form uses dual naming, and neither escalates to categorical-failure
  language; an executor that characterizes their own action in the action-based framing
  (not reading cells) but is confronted only with the protocol-based naming (not performing
  Phase 2) may not recognize the non-compliance; dual naming closes this recognition gap
  by covering both characterizations; the protocol-failure close then elevates the
  outcome from an ordering violation to a named failure category that parallels the
  failure-consequence naming already required at C-20 and C-23. Artifacts that fail C-39
  fail C-43 automatically.

**C-44** -- Pre-filled confirmation record template at each use site carries an explicit
single-task executor annotation.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-41 requires the pre-filled template at S-3 and A-1 to have the
  token name, step identifier, and row type pre-populated, leaving the match field for the
  executor to complete; C-44 requires the template to additionally carry an explicit
  annotation identifying the single field the executor must provide -- e.g., "(fill Match
  field only)" or "(complete Match field only; all other fields are pre-populated)" --
  eliminating any ambiguity about which fields require executor input. The annotation must
  appear at both use sites (S-3 and A-1); annotation at one site only fails this criterion.
  Evidence: Round 16 V-05 pattern -- each pre-filled template block at S-3 and A-1 carries
  the parenthetical "(fill Match field only)" immediately adjacent to the template,
  explicitly naming the single residual executor task; V-01 and V-04 both pass C-41 without
  this annotation -- the executor must infer that only the Match field is theirs to complete,
  which introduces a one-token inference gap that the annotation eliminates. The gap closed:
  a pre-filled template (C-41 pass) presents the executor with a form where most fields are
  populated and one is blank, but does not state explicitly how many fields are theirs to
  complete or which fields those are; an executor inspecting the form for the first time
  may scan all fields to determine which ones are blank before committing to a value;
  the single-task annotation names the residual work as a single labeled action, making
  the compliance act unambiguous and instantaneous. Artifacts that fail C-41 fail C-44
  automatically.

**C-45** -- Bracket-token rows at use sites carry a per-row anti-bypass protocol reminder
echoing the preamble anti-bypass declaration.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-43 requires the preamble to include a dual-naming anti-bypass
  closing statement with categorical-failure framing; C-45 requires the rows at S-3 and
  A-1 that contain bracket tokens to additionally carry a per-row protocol reminder that
  echoes the anti-bypass declaration at the exact point of use -- naming the action-based
  bypass description, the protocol-based bypass description, and the categorical-failure
  outcome, so that the anti-bypass constraint is activated immediately before the executor
  processes each bracket-token row. The reminder must appear at both use sites (S-3 and
  A-1) and must name both bypass forms (action-based and protocol-based) for a PASS --
  a reminder that names only one form, or that appears at only one use site, scores
  PARTIAL. Evidence: Round 16 V-05 pattern -- bracket-token rows at S-3 and A-1 each carry
  "Protocol reminder: processing this row without reading the Step and Row type cells, or
  without performing Phase 2, is a protocol failure." immediately before the row content,
  echoing the preamble's dual-naming form and categorical-failure close at the use site;
  V-02 and V-04 both pass C-43 without this use-site echo -- their anti-bypass declaration
  exists only in the preamble, leaving the residual gap that an executor processing a
  bracket-token row far from the preamble may not re-activate the anti-bypass constraint
  without a local reminder. The gap closed: C-43's preamble anti-bypass declaration (like
  C-36's preamble gate) is established once at the protocol definition point; C-45 closes
  the same recall gap that C-37 closes for the confirmation trigger -- placing the
  constraint at the exact point of use so the anti-bypass framing is activated at every
  bracket-token row regardless of distance from the preamble, completing the structural
  symmetry between the confirmation protocol (C-36 preamble / C-37 echo) and the anti-
  bypass protocol (C-43 preamble / C-45 echo). Artifacts that fail C-43 fail C-45
  automatically.

**C-46** -- C-44 single-task executor annotation uses the standalone imperative block form,
positioned above the pre-filled template rather than embedded within it as a caption
qualifier.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-44 requires an explicit annotation at both S-3 and A-1 identifying
  the single field the executor must complete; C-46 requires that annotation to take the
  standalone imperative block form -- a dedicated instruction unit positioned above (prior
  to) the pre-filled template that names both the required action and the pre-filled scope
  in imperative register. Two conditions are required: (a) structural position -- the
  annotation must appear as a discrete block or line before the template, not as a caption
  qualifier trailing the template header or embedded within the template row structure,
  so that the instruction is processed as a standalone directive before the template is
  encountered; and (b) imperative register -- the annotation must use direct imperative
  phrasing (e.g., "**Executor: fill the Match field only. All other fields are
  pre-filled.**") that states the action as a command, not a parenthetical observation.
  Evidence: Round 17 V-01 pattern -- standalone bold instruction block above the pre-filled
  table at both S-3 and A-1: "**Executor: fill the Match field only. All other fields are
  pre-filled.**" -- imperative phrasing, positionally prior to the table, structurally
  separate from the template. The gap closed: the caption parenthetical form (C-44 pass,
  R16 V-05 baseline) places the annotation as a qualifier of the template header -- an
  executor reading the template structure encounters the annotation as part of the template
  rather than as a prior directive; the annotation can be processed as a description of the
  template ("this template has one fill-in field") rather than as a command to the executor
  ("you must fill in this one field"); the standalone imperative form removes this
  ambiguity by making the instruction a first-class directive that must be processed before
  the template is engaged, with register and position both marking it as an executable
  command. Both S-3 and A-1 must carry the standalone block form for a PASS -- caption
  parenthetical at either site, or a standalone block at one site and caption at the other,
  fails this criterion. Artifacts that fail C-44 fail C-46 automatically.

**C-47** -- C-45 anti-bypass echo at each use site occupies a dedicated labeled chain-table
row rather than sub-text embedded within the CONFIRMATION row.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-45 requires the anti-bypass reminder to appear at both S-3 and A-1
  naming both bypass forms and the categorical-failure outcome; C-47 requires that reminder
  to additionally occupy a dedicated, independently labeled row in the chain table rather
  than appearing as sub-text, annotation, or continuation text within the CONFIRMATION row.
  The dedicated row must have its own label (e.g., "Anti-bypass echo" or equivalent) and
  must appear as a sequentially separate chain entry -- immediately following the
  CONFIRMATION REQUIRED row -- so that an executor processing the chain table encounters
  it as a discrete step and cannot treat it as trailing annotation of the CONFIRMATION row.
  The CONFIRMATION row itself must carry only the hard-stop gate language (C-38/C-42
  scope); the anti-bypass obligation is extracted into its own row with equal structural
  standing. Evidence: Round 17 V-03 pattern -- dedicated "Anti-bypass echo" row at both
  S-3 and A-1 immediately after CONFIRMATION REQUIRED, carrying: "Processing this row
  without reading the Step and Row type cells, or without performing Phase 2, is a protocol
  failure." -- full cell naming (C-45 requirement), dedicated row, CONFIRMATION row clean.
  The gap closed: the sub-text form (C-45 pass, V-02 baseline) places the anti-bypass
  reminder as additional content within the CONFIRMATION row; a fast executor reading
  "DO NOT WRITE THE ROW until both phases pass and record is emitted" in the CONFIRMATION
  row processes the hard-stop gate and may treat the anti-bypass reminder as a qualifying
  note of that gate rather than as an independently binding constraint; the dedicated row
  form prevents this by making the anti-bypass echo a first-class chain entry that must be
  independently read and processed -- the executor cannot claim to have processed the chain
  without independently encountering the anti-bypass row. The dedicated row form completes
  the structural parallel: C-40/C-42 established that record emission should be a co-equal
  gate precondition, not merely a Phase 2 sub-task; C-47 applies the same principle to
  the anti-bypass declaration, elevating it from a gate qualifier to a first-class chain
  entry. Both S-3 and A-1 must carry the dedicated row form for a PASS -- sub-text
  embedding at either site fails this criterion. Artifacts that fail C-45 fail C-47
  automatically.

**C-48** -- P-0 anti-bypass clause carries a named structural heading "Anti-bypass
declaration (ABD):", making it a label-matchable anchor; use-site echo row labels update
to "(P-0, ABD)" to match the heading name.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-47 requires a dedicated "Anti-bypass echo" row at both use sites
  with a row label referencing P-0 (e.g., "(P-0 anti-bypass declaration)"); C-48 requires
  the P-0 anti-bypass clause itself to carry a structural heading -- "Anti-bypass
  declaration (ABD):" or equivalent -- making it a named structural anchor rather than
  unlabeled prose, and requires the use-site echo row labels to correspondingly update to
  match the structural heading name (e.g., "(P-0, ABD)"). Two conditions are required:
  (a) structural heading at P-0 -- the anti-bypass clause must be introduced by a labeled
  heading that names the declaration and provides a scannable abbreviation (ABD or
  equivalent), so that a reader can locate the clause by heading match without scanning
  preamble prose; and (b) label-matched use-site references -- the echo row labels at S-3
  and A-1 must update from the prior "(P-0 anti-bypass declaration)" form to a form that
  matches the structural heading name at P-0 (e.g., "(P-0, ABD)"), closing the gap where
  the use-site label named a prose description rather than a structural heading.
  Evidence: Round 18 V-01 pattern -- P-0 clause opens with "Anti-bypass declaration
  (ABD):" as a structural heading; S-3 and A-1 echo row labels carry "(P-0, ABD)"
  matching the heading abbreviation. The gap closed: without a named heading, the
  use-site label "(P-0 anti-bypass declaration)" directs the reader to P-0 as a location
  but not to a named structural element -- an executor at P-0 must scan the preamble to
  find which clause the label refers to; the ABD heading creates an exact match point,
  reducing the navigation cost from a prose scan to a single heading lookup. Both use-site
  echo row labels must carry the updated form for a PASS -- a label using the prior
  "(P-0 anti-bypass declaration)" form at either site passes C-47 but fails C-48.
  Artifacts that fail C-47 fail C-48 automatically.

**C-49** -- P-0 anti-bypass declaration appends a forward navigation enumeration naming
both use sites S-3 and A-1 explicitly.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-47 established that dedicated anti-bypass echo rows exist at S-3
  and A-1, carrying use-site to P-0 back-references (via row labels); C-49 requires P-0
  to close the forward arc by appending an explicit forward pointer that names both use-site
  locations. The pointer must identify both S-3 and A-1 by step name and state that those
  rows echo the P-0 declaration -- e.g., "Anti-bypass echo rows at S-3 and A-1 echo this
  declaration at each bracket-token row." or equivalent. Two conditions are required:
  (a) explicit naming -- both S-3 and A-1 must be named; a pointer that names only one
  site, or that uses a generic description ("at each use site") without naming the steps,
  fails this criterion; and (b) forward arc framing -- the pointer must be positioned at
  P-0 as a statement about where the declaration is applied, not as a note about the
  protocol generally. Evidence: Round 18 V-02 pattern -- P-0 anti-bypass clause appends
  "Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row."
  completing the P-0 to use-site forward arc. The gap closed: without the forward pointer,
  P-0 is a definition point with no structural knowledge of where it is applied -- an
  executor reading P-0 cannot locate the use sites without scanning the full skill body;
  the forward pointer makes both use sites discoverable from P-0 in a single read.
  Together with C-48 (when both pass), C-48 and C-49 form a bidirectionally discoverable
  named anchor: locatable from use sites by label-name match (C-48), discoverable from P-0
  by forward enumeration (C-49). Each is independently achievable -- C-49 does not require
  C-48 to pass, and C-48 does not require C-49 to pass -- but the complete structural
  address pair (both forward and backward navigation at the named anchor) requires both.
  Artifacts that fail C-47 fail C-49 automatically.

**C-50** -- Anti-bypass echo row content cell at S-3 and A-1 opens with an explicit
provenance attribution prefix naming P-0 as the source.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: C-47 requires the dedicated anti-bypass echo row to carry the
  dual-named bypass text (C-45 requirement) and occupy its own labeled row; C-45 requires
  the content to name both the action-based bypass and the protocol-based bypass with
  categorical-failure framing; C-50 requires the content cell to additionally open with an
  explicit provenance prefix -- "Per P-0 anti-bypass declaration:" or "Per P-0, ABD:"
  (when C-48 passes) or equivalent -- before the dual-named bypass text. The provenance
  prefix makes the echo's identity as a P-0 protocol echo observable from the content cell
  alone, independently of the row label. Two conditions are required: (a) the prefix must
  appear at the start of the content cell, before any bypass constraint text, so that an
  executor scanning the content cell encounters the provenance reference before the
  constraint; and (b) the prefix must name P-0 as the source -- a generic attribution
  ("Per preamble:") that does not name P-0 does not satisfy this criterion; both S-3 and
  A-1 content cells must carry the prefix for a PASS. Evidence: Round 18 V-03 pattern --
  echo row content cell at S-3 and A-1 opens with "Per P-0 anti-bypass declaration: "
  before the dual-named bypass text; Round 18 V-05 pattern -- content cell opens with
  "Per P-0, ABD: " (matching the C-48 ABD label). The gap closed: C-47 places the
  anti-bypass obligation in a dedicated row with its own label, and C-45 ensures the bypass
  constraint is fully named in the content; the P-0 provenance is implied by the row label
  but is absent from the content cell -- an executor who scans only the content cell
  (skipping the row label, a common pattern in dense chain tables) encounters the bypass
  constraint without any signal that it derives from P-0 rather than being a locally-scoped
  rule; the content-cell prefix closes this gap by placing the source reference at the
  exact point where the constraint is consumed, making provenance observable at both the
  label level (C-47) and the content level (C-50) independently. Artifacts that fail C-47
  fail C-50 automatically.

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 42 * 10)
```

PARTIAL counts as 0.5 for any criterion.

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Essential (5x) | Recommended (3x) | Aspirational (42x) |
|------|---------------|-----------------|-------------------|
| Points | 60 | 30 | 10 |
| Formula | pass/5 x 60 | pass/3 x 30 | pass/42 x 10 |

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
| C-32 pre-computation positioning | |
| C-33 structured resolution table | |
| C-34 explicit lookup obligation | |
| C-35 use-site row navigation labels | C-35 use-site row navigation labels |
| C-36 two-phase confirmation gate | |
| C-37 confirmation echo at use site | C-37 confirmation echo at use site |
| C-38 hard-stop gate language | C-38 hard-stop gate language |
| C-39 anti-bypass closing statement | |
| C-40 confirmation record obligation | |
| C-41 pre-filled record template | C-41 pre-filled record template |
| C-42 emit woven into gate condition | C-42 emit woven into gate condition |
| C-43 dual-naming + protocol failure | |
| C-44 single-task executor annotation | C-44 single-task executor annotation |
| C-45 per-use-site anti-bypass echo | C-45 per-use-site anti-bypass echo |
| C-46 standalone imperative block form | C-46 standalone imperative block form |
| C-47 dedicated anti-bypass echo row | C-47 dedicated anti-bypass echo row |
| C-48 named ABD heading at P-0 | C-48 named ABD heading at P-0 (use-site labels) |
| C-49 P-0 forward navigation enumeration | |
| | C-50 content-cell provenance attribution |

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
- **C-34 fail**: Structured resolution table is present (C-33 passes) but the preamble
  carries no explicit lookup obligation -- the table is presented as a reference resource
  rather than a mandatory consultation protocol. An executor may decode bracket tokens
  from context memory for tokens seen in prior steps, bypassing the table and forfeiting
  the orientation guarantee. Missing either the affirmative mandate ("look it up in this
  table before processing the containing row") or the memory-decoding prohibition ("Do not
  decode bracket tokens from memory") fails this criterion; a note that the table "may be
  used for reference" does not satisfy the mandatory framing. Fails automatically when
  C-33 fails.
- **C-35 fail**: Explicit lookup obligation is present (C-34 passes) but bracket-token
  rows at the use sites (S-3 and A-1) carry no row-specific navigation labels identifying
  which preamble table row resolves each token -- an executor following the C-34 obligation
  must scan the resolution table to find the governing row rather than jumping directly to
  it. Labels present at only one use site (S-3 or A-1 but not both) also fail this
  criterion; both sites must carry labels for a PASS. A label that points to the preamble
  section but not to a specific row does not satisfy the row-specificity requirement. Fails
  automatically when C-34 fails.
- **C-36 fail**: Row-specific navigation labels are present at both use sites (C-35 passes)
  but the preamble lookup obligation is stated as a single locate step ("find the row and
  look it up") rather than a two-phase confirmation gate -- the executor satisfies the
  obligation by navigating to the table row without being required to read the Step and Row
  type cells and assert that the resolution matches the processing context. A locate-only
  obligation can be satisfied by visual token recognition, which does not constitute
  semantic verification; the confirm phase closes this gap by requiring a cell-level read
  and an explicit match assertion before the row is written. Missing either phase in the
  preamble fails this criterion; a single-sentence obligation that mentions "confirm" as
  part of a longer clause rather than as a discrete numbered step also fails. Fails
  automatically when C-35 fails.
- **C-37 fail**: Two-phase confirmation gate is defined in the preamble (C-36 passes) but
  bracket-token rows at the use sites (S-3 and A-1) carry no behavioral trigger echoing
  the confirmation requirement -- an executor processing a bracket-token row deep in the
  skill body must independently recall the preamble protocol to activate confirmation;
  without a use-site trigger, the confirmation gate is enforced only at the preamble's
  reading time, not at the point of use. A trigger present at only one use site (S-3 or
  A-1 but not both) fails this criterion; both sites must carry the trigger for a PASS.
  A trigger that names confirmation but does not precede the navigation label and row
  content (appearing after rather than before) fails the positioning requirement. Fails
  automatically when C-36 fails.
- **C-38 fail**: Confirmation triggers are present at both the preamble and use sites
  (C-36 and C-37 pass) but use only prerequisite framing -- "Confirmation is a prerequisite
  to writing the row" / "CONFIRMATION REQUIRED before writing this row" -- without an
  explicit execution block prohibiting the write until the gate passes. Prerequisite
  framing is an ordering constraint; a reader under execution pressure may satisfy it by
  performing Phase 2 perfunctorily without treating it as an unambiguous block. Missing
  hard-stop language ("DO NOT WRITE THE ROW until...") at either the preamble gate
  definition or the use-site echo (S-3 or A-1) fails this criterion; hard-stop language
  must appear at all three locations for a PASS. Fails automatically when C-37 fails.
- **C-39 fail**: Two-phase confirmation gate is defined in the preamble with Phase 2 as a
  prerequisite or hard-stop (C-36/C-38 pass) but the preamble carries no closing statement
  naming the visual-recognition bypass and declaring it non-compliant -- an executor
  familiar with the tokens may satisfy the gate by recognizing them rather than by
  performing the Phase 2 cell-read, and no criterion prior to C-39 names this path
  explicitly as protocol failure. A passing C-36 that states the confirm phase implicitly
  closes the gap through positive obligation, but does not label the bypass or assert its
  insufficiency; C-39 requires that label and assertion to appear as a dedicated closing
  statement. Fails automatically when C-36 fails.
- **C-40 fail**: Phase 2 in the preamble is a hard-stop gate (C-38 passes) but carries no
  obligation to produce an observable confirmation record -- the Phase 2 assertion remains
  internal and unverifiable from the output. Preamble Phase 2 that states "assert match"
  or "verify the resolution" without an explicit "Emit confirmation record" directive fails
  this criterion; a directive present in a comment or side note rather than in the Phase 2
  protocol definition also fails. Use-site echo language that mentions recording without
  a preamble-level obligation is insufficient -- the obligation must be established in the
  preamble where the protocol is defined. Fails automatically when C-38 fails.
- **C-41 fail**: Preamble emit obligation is present (C-40 passes) but the bracket-token
  rows at the use sites (S-3 and A-1) carry no pre-filled confirmation record template --
  record construction remains open-form, requiring the executor to recall and build the
  record structure from scratch at each use site. A template present at only one use site
  (S-3 or A-1 but not both) fails this criterion; both sites must carry templates for a
  PASS. A template that uses generic placeholders (e.g., "{token}", "{step}") rather than
  the actual values for that specific row also fails -- the template must be pre-populated
  with the row-specific token name, step identifier, and row type so the executor fills in
  only the match result. Fails automatically when C-40 fails.
- **C-42 fail**: Pre-filled templates are present at both use sites (C-41 passes) and
  hard-stop gate language is present (C-38 passes) but the gate condition at the preamble
  and/or use sites ends at phase completion ("until both phases pass") without naming the
  record emission as an explicit gate precondition -- the gate blocks on phase completion
  but not explicitly on record existence. A preamble that lists "Emit confirmation record"
  within Phase 2's definition (C-40 pass) but whose gate text reads "DO NOT WRITE THE ROW
  until both phases pass" (not "...and the record is emitted") fails this criterion. All
  three locations (preamble gate, S-3 echo, A-1 echo) must carry the emit-in-gate form.
  Fails automatically when C-38 fails. Fails automatically when C-40 fails.
- **C-43 fail**: Anti-bypass closing statement is present (C-39 passes) but uses only a
  single naming form for the bypass (either action-based OR protocol-based, not both) or
  uses non-categorical severity language ("has not satisfied this protocol" / "does not
  satisfy the confirmation gate") rather than protocol-failure framing. Missing either the
  dual-naming form (both "without reading the Step and Row type cells" and "without
  performing Phase 2" in the same closing statement) or the categorical-failure close
  ("Locate-only is a protocol failure" or equivalent) fails this criterion; both conditions
  must be met for a PASS. A closing statement that uses the categorical-failure framing
  without dual-naming, or dual-naming without categorical-failure framing, scores PARTIAL.
  Fails automatically when C-39 fails.
- **C-44 fail**: Pre-filled templates are present at both use sites (C-41 passes) but carry
  no explicit single-task executor annotation identifying which field requires completion --
  the executor must infer that only the Match field is theirs to complete by inspecting the
  template and determining which fields are blank; this inference gap remains even though
  the inference is trivial in a well-formed template. An annotation present at only one
  use site (S-3 or A-1 but not both) scores PARTIAL; annotations using vague language
  (e.g., "complete as needed") rather than naming the specific field also fail. Fails
  automatically when C-41 fails.
- **C-45 fail**: Dual-naming anti-bypass declaration is present in the preamble (C-43
  passes) but bracket-token rows at the use sites (S-3 and A-1) carry no per-row protocol
  reminder echoing the anti-bypass framing -- an executor processing a bracket-token row
  deep in the skill body must independently recall the preamble's anti-bypass protocol to
  activate the constraint; without a use-site reminder, the anti-bypass declaration is
  enforced only at the preamble's reading time, not at the point of use. A reminder that
  names only one bypass form (action-based OR protocol-based, not both) scores PARTIAL; a
  reminder present at only one use site scores PARTIAL. A full PASS requires both bypass
  forms named and the categorical-failure framing present at both S-3 and A-1. Fails
  automatically when C-43 fails.
- **C-46 fail**: Single-task executor annotation is present at both use sites (C-44 passes)
  but uses the caption parenthetical form embedded within the template structure rather than
  a standalone imperative block positioned above the template -- the annotation is read as
  a qualifier of the template (describing it) rather than as a prior directive to the
  executor (commanding them). An annotation that is positionally prior but uses
  non-imperative register (e.g., "Match field is the only field to complete"), or that uses
  imperative register but is embedded within the template row, fails this criterion; both
  structural position (above the template) and imperative register are required for a PASS.
  An annotation satisfying both conditions at one site but not the other scores PARTIAL.
  Fails automatically when C-44 fails.
- **C-47 fail**: Per-row anti-bypass reminder is present at both use sites with full cell
  naming and categorical-failure framing (C-45 passes) but appears as sub-text or
  continuation text within the CONFIRMATION row rather than as a dedicated, independently
  labeled chain-table row -- a fast executor processing the CONFIRMATION row can read the
  hard-stop gate language, treat the anti-bypass text as a qualifying annotation of that
  gate, and proceed without independently processing the anti-bypass constraint as a
  first-class obligation. A dedicated row present at one site but sub-text at the other
  scores PARTIAL; both S-3 and A-1 must carry the dedicated labeled row form for a PASS.
  Fails automatically when C-45 fails.
- **C-48 fail**: Dedicated anti-bypass echo rows are present at both use sites (C-47 passes)
  but the P-0 anti-bypass clause carries no structural heading label -- it is unlabeled
  prose that a reader must scan to locate; and/or the use-site echo row labels retain the
  prior "(P-0 anti-bypass declaration)" form rather than updating to match a structural
  heading at P-0 (e.g., "(P-0, ABD)"). Both conditions are required for a PASS: a named
  heading at P-0 AND label-matched use-site references. A heading present at P-0 without
  updated use-site labels scores PARTIAL; updated use-site labels without a matching
  structural heading at P-0 also scores PARTIAL (labels reference a name that does not
  exist as a structural element). Fails automatically when C-47 fails.
- **C-49 fail**: Dedicated anti-bypass echo rows are present at both use sites (C-47 passes)
  but the P-0 anti-bypass declaration carries no forward pointer naming the use sites --
  P-0 is a definition point with no structural knowledge of where it is applied; an executor
  reading P-0 cannot navigate to the echo rows without scanning the full skill body. A
  forward pointer that names only one of the two use sites (S-3 but not A-1, or vice versa)
  scores PARTIAL; a generic reference ("at each bracket-token row") that does not name the
  steps by name also scores PARTIAL. Both S-3 and A-1 must be named explicitly for a PASS.
  Fails automatically when C-47 fails.
- **C-50 fail**: Dedicated anti-bypass echo rows are present at both use sites (C-47 passes)
  and the dual-named bypass constraint is in the content cell (C-45 passes) but the content
  cell opens with no provenance attribution prefix naming P-0 -- an executor scanning only
  the content cell encounters the bypass constraint without knowing it is a P-0 echo rather
  than a locally-scoped rule. A prefix present at one use site but absent at the other
  scores PARTIAL; a generic attribution ("Per preamble:" or "Per protocol:") that does not
  name P-0 specifically also scores PARTIAL -- the prefix must name P-0 to create the
  label-level provenance signal that distinguishes a P-0 echo from a local annotation.
  Fails automatically when C-47 fails.
