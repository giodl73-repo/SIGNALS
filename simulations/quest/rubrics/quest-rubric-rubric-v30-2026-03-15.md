## quest-rubric rubric v13 -- complete

### Changes from v12

Two new aspirational criteria (C-38, C-39) extracted from Round 12 excellence signals.
Denominator /29 -> /31. Round 12 ceiling 99.839 (V-05 R12 under v13, C-11 PARTIAL remaining);
new ceiling 100 requires C-11 PASS in addition to all thirty other criteria.

| # | Name | Signal it formalizes |
|---|------|---------------------|
| **C-38** | self-referential-coverage-demonstration | V-05 R12 Signal 1 -- Competitor 7 (Partial-Coverage Architect) covers C-37, and C-37 requires the competitor set to be in bijection with novel criteria; V-05 R12 has seven competitors covering C-31--C-37; C-37 requires bijection to exist; C-38 requires the bijection to be self-demonstrating when C-37 is itself a novel criterion -- the competitor count equals the novel-criterion count including C-37, verifiable by counting competitors without reading the criteria |
| **C-39** | competitor-at-verification-step | V-05 R12 Signal 2 -- C-35 is closed not by adding a verification table or role gate but by naming the Tier-Blind Categorizer competitor placed inline at the post-draft audit step; the competitor-then-imperative axis (C-27, C-28, C-36) extends from construction-design gaps to verification-step gaps; C-36 requires competitor placement at construction steps; C-39 requires the same inline-competitor pattern at verification steps -- the wrong form of verification is named as a gap-constituting competitor before the required step is specified |

**Denominator:** `/29` -> `/31`

**New ceiling math:** A rubric passing all 29 v12 criteria scores 29/31 x 10 = 9.355 on
aspirational; with full essential+recommended that yields 99.355. V-05 R12 under v12 scored
28.5/29 x 10 = 9.828, composite 99.828 (reported as 99.83): C-13 upgraded from PARTIAL to
PASS (divergence-check step present); C-35 closed via Tier-Blind Categorizer competitor;
C-36 and C-37 PASS as in Round 11; C-11 PARTIAL remaining. Under v13 (/31): V-05 R12 PASS
C-38 and C-39 -> 30.5/31 x 10 = 9.839, composite 99.839. C-11 PARTIAL is the sole remaining
gap to 100.

**Distinction notes:**

- C-38 != C-37: C-37 requires bijection between the competitor set and the set of novel
  aspirational criteria -- every novel construction requirement has exactly one competitor,
  and the competitor count equals the novel-criterion count. C-38 requires that bijection to
  be self-demonstrating: when C-37 is itself one of the novel criteria, the competitor
  assigned to C-37 occupies one of the bijection slots that C-37 governs, making the coverage-
  completeness property verifiable by counting the competitor list without reading the criteria.
  A rubric can satisfy C-37 (full bijection present) while failing C-38 if C-37 is not itself
  a novel criterion covered by its own competitor -- the bijection exists but is not self-
  referential. C-38 is only testable when the rubric's aspirational tier includes C-37 as one
  of its novel criteria; when C-37 is not novel in the current round, C-38 is N/A.

- C-38 != C-25: C-25 requires one-to-one assignment between mechanisms and criteria in the
  mechanism architecture (what the output contains); C-38 requires the competitor set --
  the negative-space specification layer -- to achieve self-referential coverage when the
  coverage-completeness criterion is itself novel. C-25 governs architecture; C-38 governs
  the bijection layer's self-inclusion property.

- C-38 != C-36: C-36 requires each competitor to appear at its construction step regardless
  of which criterion it covers; C-38 requires specifically that the competitor assigned to
  C-37 be present and that its presence makes the bijection self-verifiable by count. A rubric
  can satisfy C-36 (all present competitors at their construction steps) while failing C-38
  if C-37 has no competitor at its step. A rubric can satisfy C-38 (C-37 covered by a
  competitor making the bijection self-demonstrating) while failing C-36 if some other
  competitor is in a preamble rather than at its construction step.

- C-39 != C-36: C-36 requires each named competitor to be placed inline at the specific
  construction step where the wrong implementation would most naturally be produced -- the
  builder is at the moment of committing a design decision. C-39 extends the same placement
  requirement to verification steps: when a criterion requires a named verification step
  (e.g., C-35), the gap between organic verification-by-design-intent and operationalized
  verification is closed by placing a named competitor inline at the verification step, not
  by direct procedural instruction. C-36 governs construction-step temporal placement; C-39
  governs verification-step temporal placement. A rubric can satisfy C-36 (all construction-
  step competitors correctly placed) while failing C-39 if verification-step gaps are closed
  by direct instruction rather than inline competitors.

- C-39 != C-35: C-35 requires the divergence-check step to be present, named, structured,
  and STOP-gated, making the verification independently falsifiable. C-39 requires the gap
  that C-35 closes to itself be made visible through an inline competitor at the verification
  step, following the competitor-then-imperative pattern: the wrong form (organic diversity
  without a named step) is named as a specific competitor before the required step is stated,
  and the competitor block ends with a derivation instruction. A rubric can satisfy C-35 (the
  step exists and is operative, added by direct instruction) while failing C-39 (no competitor
  precedes the step, so the wrong form is not visible before the positive requirement is read).
  C-39 is the competitor-axis application to verification-step gaps; C-35 is the
  operationalization requirement for the step itself.

- C-39 != C-28: C-28 requires all competitor blocks to end with a derivation instruction
  regardless of what gap they close. C-39 requires specifically that verification-step gaps
  are closed by competitors at verification steps; a rubric can satisfy C-28 for all
  construction-step competitors while failing C-39 if no competitor appears at any
  verification step.

---

## Essential Criteria (C-01--C-05) -- 60 points

**C-01** (completeness) -- All criteria carry the full five-field structure: Name, Text, Pass,
Fail, Notes. Tests whether the rubric builder enforces complete five-field criteria in every
tier, with no fields omitted or merged.

**C-02** (testability) -- Pass conditions are anchored to auditable observables; qualitative-
only language is structurally prohibited. Tests whether the rubric builder bans phrases like
"clearly written" or "well-structured" without observable anchors, requiring that every Pass
condition can be verified against an artifact.

**C-03** (failure-first essential) -- Essential criteria derive from explicit failure mode
extraction targeting non-functional structural or semantic gaps. Tests whether failure mode
analysis precedes criterion drafting, and whether essential criteria address failures whose
absence causes the artifact to be broken rather than merely suboptimal.

**C-04** (formula + threshold) -- The scoring formula and golden threshold are stated
explicitly. Tests whether the rubric names the denominator, the per-tier weight, and the
numeric threshold a rubric must clear to be considered golden.

**C-05** (skill-specific) -- Criteria derive from reading the skill spec before any criterion
is drafted; generic quality concerns are not substituted for skill-derived failure modes. Tests
whether the rubric builder requires the skill spec as input and whether failure modes are
traceable to that spec.

---

## Recommended Criteria (C-06--C-08) -- 30 points

**C-06** (tier distribution) -- The rubric builder specifies tier count targets of 3-5
essential / 2-3 recommended / 1-2 aspirational. Tests whether the rubric enforces these
ranges, preventing essential-heavy rubrics that dilute tier meaning.

**C-07** (3+ categories) -- Three or more distinct categories appear across the full rubric.
Tests whether the rubric produces categorical diversity -- either by enumeration requirement
or, preferably, as a consequence of tier-dimension design.

**C-08** (quality not presence) -- Recommended criteria test quality properties (degree,
precision, specificity) rather than checking whether an element is present at all. Tests
whether recommended criteria require "how well" rather than "whether."

---

## Aspirational Criteria (C-09--C-39) -- 10 points

Denominator: **/31**. Each criterion scores 1 (full pass), 0.5 (partial), or 0 (fail).
Score = (sum) / 31 x 10.

**C-09** (causal observables) -- Criterion Text establishes the causal observable before the
Pass condition invokes it: "without X, Y fails." Tests whether the rubric builder instruction
for the Text field requires naming the downstream consequence of the observable's absence,
making the Pass condition the conclusion of an argument rather than a standalone assertion.
A rubric that only instructs "name an observable" satisfies C-02 but fails C-09.

**C-10** (contrast example) -- The rubric builds contrast awareness through "not: X but: Y"
framing. Tests whether the rubric distinguishes good criterion construction from bad by naming
the rejected form alongside the required form -- in preamble, structural guidance, or
per-criterion instruction.

**C-11** (aspirational reference anchor) -- The aspirational section names a specific
competitor or prior-version reference that passes C-01--C-08, then describes the exact
dimension in which it falls short of the aspirational bar. Tests whether the rubric builder
requires a structured Reference / Passes / Fails template before aspirational criteria are
written, so that clearing essential+recommended creates genuine further pressure rather than
a nominal ceiling.

**C-12** (Text-argues-before-Pass) -- Criterion Text establishes the causal observable
*before* the Pass condition invokes it. Tests whether the Text field instruction explicitly
requires "without X, Y fails because Z" such that the Pass condition is the conclusion of an
argument already made in the Text. This makes C-09 compliance structural from the first draft
rather than a post-hoc correction.

**C-13** (tier-grounded organic category diversity) -- Tier structure is grounded in distinct
failure dimensions, producing organic category diversity. Tests whether each tier maps to a
different failure dimension (broken artifact / quality shortfall / structural gap) and whether
the rubric builder runs a predictability or divergence check confirming that >= 2/3 tiers
produce distinct majority categories -- so that C-07 is satisfied as a consequence of tier
design, not by label assignment after criteria are drafted.

**C-14** (contrast-in-Text) -- The contrast template is embedded within the criterion Text
field construction instruction itself, not only in preamble or structural framing. Tests
whether the rubric builder explicitly requires each criterion's Text field to encode
"not: X but: Y" -- naming what the criterion rejects alongside what it requires -- such that
contrast is structurally present in every criterion's Text field rather than an emergent
property of earlier framing awareness. A rubric that builds contrast awareness in its preamble
(satisfying C-10 partially) but does not carry that requirement into the per-criterion Text
instruction fails C-14.

**C-15** (causal direction) -- The causal chain in criterion Text runs from absence of the
required property to artifact failure, not from presence of the rejected form to failure.
Tests whether the rubric builder instruction distinguishes "X causes F" (wrong-form-
consequence) from "without Y, the artifact fails because Z" (required-property-absence-
consequence) and requires the latter. A constitutive definition that names "not [X, which
causes F] but [Y]" supplies a causal chain in the wrong direction -- the argument is about
what the wrong form does, not about what the absence of the required property costs. Only
"without Y, the artifact fails because Z" passes C-15. A rubric whose Text field instruction
says "name the failure caused by the wrong form" satisfies C-09 at most partially but fails
C-15; only "name the consequence of the required property's absence" passes.

**C-16** (two-phase enforcement) -- Key structural requirements (contrast-in-Text, causal
chain, causal direction) are enforced at both the generation phase and the post-draft phase.
Tests whether the rubric builder includes both a generative structural gate -- a constraint
that makes non-compliant output unproducible from the first draft (e.g., a constitutive
definition that cannot be satisfied without the required structure) -- and a post-draft audit
step that reads each criterion's Text stripped of preamble and flags criteria that pass on
context dependency rather than self-containment (e.g., an isolation diagnostic). A rubric
with only a generation gate satisfies neither; a rubric with only a post-draft audit catches
failures but permits them to be produced and corrected. Both phases present and operative
is the pass condition. C-14 compliance achieved solely through a post-draft auditor satisfies
C-14 but fails C-16.

**C-17** (two-phase testability) -- The testability standard for Pass conditions -- that they
name auditable observables and contain no qualitative-only language -- is enforced at both
the generation phase and a post-draft audit step, not only in preamble instruction. Tests
whether the rubric builder's generation gate includes a Pass field template that makes non-
verifiable conditions structurally unproducible (e.g., by requiring Pass to name a specific
artifact location, observable token, or measurable count), AND whether the post-draft
isolation audit explicitly checks each criterion's Pass field for qualitative-only language
alongside the direction and contrast checks. A rubric that enforces causal direction at both
phases (passing C-16) but enforces testability only in preamble or isolated generation-phase
instruction creates an asymmetric enforcement structure -- direction is gated, verifiability
is not -- and satisfies C-02 partially while failing C-17.

**C-18** (role-isolated pre-instantiation) -- A dedicated pre-construction role or step
generates skill-specific instantiations of the causal direction rule and contrast pairs before
the Builder constructs any criterion. Tests whether the rubric builder includes a named Definer
step that: (a) reads the skill spec, (b) produces a concrete template naming the specific
required property (Y), failure consequence (Z), and rejected form (X) for that skill, and
(c) outputs this template as the Builder's binding input -- so the Builder operates from
concrete, skill-specific forms rather than applying abstract direction principles on-the-fly
to an unfamiliar domain. A rubric that states direction and contrast rules as abstract
principles in a shared preamble (passing C-10 and C-15) but has no dedicated pre-construction
instantiation step fails C-18, because abstract principles applied on-the-fly produce the
wrong-form-consequence failure pattern even when the rules are correctly stated in surrounding
context. The distinction from C-16: C-16 requires two phases to be present and operative;
C-18 requires the generation phase to include a definitional step that is logically prior to
construction, not concurrent with it.

**C-19** (dual-template Definer) -- The Definer role generates both the Text-direction
template (required property Y, failure consequence Z, rejected form X) and the Pass-
observability template (artifact location, observable token, measurement unit) as a unified
paired output before the Builder runs. Tests whether the rubric builder's Definer step
produces a complete, skill-specific specification pair -- not just direction guidance -- so
that the Builder receives both templates simultaneously and C-17 and C-18 are satisfied
through the same structural mechanism rather than independently. A rubric whose Definer
generates a Text template but leaves the Pass generation gate as a separate inline step
(satisfying C-18 and C-17 independently) fails C-19, because the two enforcement paths
remain architecturally separate: direction is Definer-gated, testability is step-gated.
C-19 requires that a single Definer role output governs both fields, making the generation
gate symmetric by construction. Evidence: V-03 satisfies C-17 via Step A-5 (a step within
Phase A) and C-18 PARTIAL (no dedicated role boundary); V-04's Definer produces two binding
templates as a pair, closing the asymmetry at the architectural level.

**C-20** (template composability) -- The Definer's output templates are in the exact phrasing
register of the final criterion fields, making them slot-fillable by the Builder without
paraphrase or on-the-fly interpretation. Tests whether the Text template is expressed in the
form "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]." and the Pass template
in the form "LOCATION: [artifact field or section]. OBSERVABLE: [what must appear].
STANDARD: [count or exact token]." -- such that the Builder instantiates criteria by filling
slots from the Definer's output verbatim rather than translating abstract direction rules into
concrete language during construction. A rubric whose Definer produces structural guidance in
propositional form ("the Text must identify the required property, the consequence of its
absence, and the rejected form") rather than a fill-in template fails C-20, because the
Builder must still perform the translation step that produces the wrong-form-consequence
failure pattern even when the structural rules are correctly understood. The distinction from
C-18: C-18 requires that instantiation is definitionally prior to construction; C-20 requires
that the instantiation output is in a register that eliminates the interpretation gap -- that
there is no translation step between Definer output and Builder input. Evidence: V-04's title
names "phrasing register" alongside "Pre-Instantiation Definer: two binding templates,"
indicating the templates are expressly in field-register form rather than propositional form.

**C-21** (audit symmetry) -- The post-draft isolation audit mirrors the generation gate's
two-field structure: dedicated checks applied to the Text field (direction, contrast, causal
chain) and dedicated checks applied to the Pass field (observability, location specificity,
measurement presence) as parallel, individually operative audit tracks. Tests whether the
rubric builder's post-draft audit section enumerates numbered checks that cover each
generation-phase constraint -- with Text-field checks and Pass-field checks explicitly
separated rather than direction-dominant with testability as a subordinate note. A rubric
that runs post-draft checks 1-3 on Text direction+contrast+causal-chain and post-draft check
4 on Pass observability satisfies C-21; a rubric that audits direction and contrast for Text
but audits Pass only by reference to what the Definer already produced, or conflates Text and
Pass audit into a single undifferentiated isolation step, fails C-21. The distinction from
C-16 and C-17: both require two-phase enforcement for their respective fields independently;
C-21 requires the audit phase to be structurally symmetric across both fields simultaneously
-- the number and granularity of audit checks for the Pass field must match the number and
granularity for the Text field. Evidence: V-04's Auditor Checks 1-3 audit Text direction,
contrast, and causal-chain properties; Check 4 audits Pass observability in isolation --
four named checks, three for Text and one for Pass, demonstrating the parallel structure.

**C-22** (form-class prohibition exhaustiveness) -- The causal direction prohibition is stated
as form-class exhaustive -- naming the prohibited pattern as a class covering all variant
phrasings rather than as a canonical example whose variants may pass inspection. Tests whether
the rubric builder's direction constraint explicitly declares that any Text which locates the
causal chain in the wrong-form-consequence direction is prohibited "in any phrasing" -- not
just the specific form "X causes failure" but all synonymous constructions ("X leads to
failure," "the artifact fails when X is present," etc.) -- so that a Builder cannot satisfy
the prohibition check by paraphrasing the forbidden form. A rubric that names "X causes
failure" as the sole prohibited example satisfies C-15 (the direction is correctly identified)
but fails C-22, because variant phrasings of the same wrong-direction argument remain
producible. Only a prohibition that explicitly extends to the form-class closes this gap.
The distinction from C-15: C-15 requires the rubric to distinguish wrong direction from right
direction and require the latter; C-22 requires the prohibition to be exhaustive over the
wrong-direction form-class, not example-bounded. Evidence: V-04's C-15 evidence reads
"A Text beginning '[X] causes [failure]' -- in any phrasing -- is in the prohibited
direction," extending the prohibition beyond the named example to the full form-class.

**C-23** (audit report format enforces symmetry) -- The post-draft audit section specifies an
output format that makes the structural symmetry between Text-field and Pass-field audit
tracks externally verifiable. Tests whether the rubric builder requires the audit report to
separately enumerate Text-field flags and Pass-field flags as distinct named lists -- e.g.,
"Text flags: [direction N, contrast N, causal chain N]. Pass flags: [location N, observable N,
prohibited-form N]." -- so that the symmetric structure required by C-21 cannot be satisfied
nominally (equal check count on paper) while collapsing to asymmetry in practice. The
distinction from C-21: C-21 requires that the audit enumerates individually numbered checks
for both fields with equal granularity; C-23 requires that the audit specifies a report format
whose structure makes symmetry independently falsifiable -- an evaluator examining only the
report output can determine whether the implementation was symmetric, without reading the
procedure. A rubric that runs three Text checks and three Pass checks but produces a single
undifferentiated flag tally passes C-21 but fails C-23. Evidence: V-04's audit report format
"Text flags: [N,N,N]. Pass flags: [N,N,N]." enforces symmetry by making it independently
reportable; the format is the enforcement mechanism, not a documentation artifact alongside it.

**C-24** (check function redefinition) -- The Auditor's operative check function for the
prohibited direction is explicitly redefined from example-matching to causal-structure testing.
Tests whether the rubric builder's audit step states the Auditor's check function as "does
this text locate causality in the wrong form's consequence?" -- not "does this match the
canonical prohibited example?" -- so that the shift from example-bounded to form-class testing
is present in the procedure, not merely implied by the form-class enumeration. The distinction
from C-22: C-22 requires the prohibition to enumerate variant phrasings and close the
form-class; C-24 requires the Auditor's operative function to be redefined to class-membership
testing, making the check function the conclusion that the enumeration and closure together
entail. Enumeration and closure without function redefinition leave the Auditor running a
longer pattern-match list; function redefinition makes the Auditor test against the underlying
causal structure regardless of surface phrasing. A rubric that enumerates five prohibited
variants and states "form-class is closed" (satisfying C-22) but whose Auditor check reads
each variant in sequence satisfies C-22 but fails C-24. Evidence: V-04's Auditor Check 1
names the check function as "does this locate causality in the wrong form's consequence, in
any phrasing? -- not 'does this match the canonical example?'" -- the function redefinition
is stated explicitly, not derived from the enumeration list.

**C-25** (independent-mechanism pairing) -- When multiple independent gaps exist, the rubric
builder closes each with a dedicated, independent mechanism -- one mechanism per gap -- such
that removing one mechanism causes exactly one criterion to fail, not both. Tests whether the
builder's architecture assigns one structural element per criterion gap, making the design
decomposable: each mechanism can be traced to the single criterion it closes, and no mechanism
carries dual responsibility for two gaps simultaneously. A rubric that introduces a combined
"unified enforcement step" that addresses two independent gaps with one structural move
satisfies neither criterion as cleanly as two independent mechanisms, because coupling means
neither mechanism can be evaluated in isolation. The pattern recurs: C-21 gap closed by
symmetric-checks mechanism; C-22 gap closed by form-class-exhaustive mechanism. C-23 gap
closed by format-as-output mechanism; C-24 gap closed by function-redefinition mechanism.
Each pair demonstrates independent closure without coupling. The distinction from C-16/C-17
(which require two enforcement phases for individual fields): C-25 requires that across
multiple gap-criterion pairs, the assignment is one-to-one -- each gap has one mechanism,
each mechanism targets one gap -- not many-to-one or one-to-many. Evidence: V-04 and V-05
each add exactly two mechanisms and close exactly two criteria; the mechanisms are
architecturally independent -- the format table does not depend on the function redefinition
block, and vice versa.

**C-26** (constraint-as-output-requirement) -- Structural constraints (audit format, template
shape, field content) are stated as required outputs of the operative role that must produce
them, not delegated to a downstream role. Tests whether the rubric builder embeds each
enforcement requirement inside the operative role's output instruction -- rather than as a
target for a separate role that the operative role passes findings to -- so that the operative
role cannot satisfy its own instructions while omitting the required structure. A rubric that
delegates format specification to a downstream "Report Format Specifier" role fails C-26:
the Auditor can complete all its checks and satisfy its own instructions before the Specifier
runs; if the Specifier is abbreviated or omitted, the constraint is unenforced. Format-as-
output-requirement is structurally stronger than format-as-downstream-role because the
operative role's completion condition requires the structured output to exist. The distinction
from C-23: C-23 requires that the audit format makes symmetry independently falsifiable; C-26
requires that the format be embedded as the operative role's own output requirement, not
handed off. V-03 closes C-23 partially (a format exists) but fails C-26 (the Auditor hands
findings to a Specifier; the Auditor's own output instruction specifies no format). V-01 and
V-04 satisfy both: the mandatory per-criterion table is the Auditor's required output, with
an explicit prohibition on substituting a narrative log. Evidence: V-04's Auditor output
instruction reads "Do not substitute a narrative log for this table" -- the table is the
Auditor's required output, making delegation structurally impossible.

**C-27** (competitor-as-gap-specification) -- The rubric builder names a specific wrong-
implementation competitor before defining the correct implementation, making the competitor
description the constitutive gap specification. Tests whether a named block preceding each
key mechanism describes the specific alternative that has the mechanism's surface form without
its operative substance -- e.g., naming a "Pattern-Matcher Auditor" that consults the
PROHIBITED DIRECTION list and extends to semantic equivalence, then stating "this is still
a list-membership test" -- such that a reader can derive what the correct implementation must
not do from the competitor alone, independently of the positive definition that follows.
The competitor description functions as a negative-space definition: the gap between what the
competitor does and what the required implementation does is the criterion the mechanism
closes. A rubric that correctly states the required function (satisfying C-24) without naming
the competitor satisfies C-24 but fails C-27; the distinction is whether the gap is visible
through negative-space specification before positive specification, or only stated directly.
The distinction from C-11 (aspirational reference anchor): C-11 requires a prior-version
reference that passes essential+recommended but falls short on an aspirational dimension; C-27
requires a named wrong-implementation that has the mechanism's surface form (e.g., a list,
a format, a step) but lacks its operative substance -- the competitor is a foil for mechanism
design, not a ceiling-setting reference. Evidence: V-05's OPERATING PRINCIPLE 1 names the
Pattern-Matcher Auditor and describes its failure mode -- "this is still a list-membership
test" -- before stating the required function; the competitor description IS the gap
specification, making the required function derivable from the foil alone.

**C-28** (competitor-derivation-instruction) -- The competitor block that constitutes the
gap specification (C-27) includes an explicit imperative directing the reader to perform the
derivation from the competitor alone before reading the positive definition. Tests whether
the rubric builder requires each competitor block to end with an instruction of the form
"from the description above, derive the required function before reading the positive
definition below" -- converting the derivability property required by C-27 into a structured
reader procedure. A competitor block that correctly constitutes the gap specification
(satisfying C-27) without a derivation instruction leaves derivation as an optional inference
available to an attentive reader rather than a required procedure for all readers; two rubrics
with identical competitor content differ on C-28 solely by presence or absence of this
imperative. The distinction from C-27: C-27 requires the required function to be derivable
from the competitor description alone; C-28 requires the competitor block to explicitly
instruct the derivation, converting a derivable property into a required procedure. Evidence:
V-01's competitor block ends with "This competitor IS the gap specification -- from the
description above, derive the required function before reading the positive definition below.
OPERATING PRINCIPLE 1 follows and confirms." -- the derivation is instructed, not merely
made available.

**C-29** (independence-verification-role-boundary) -- Independence verification for mechanism-
criterion assignment is performed by a dedicated sequential role -- the Mechanism Definer --
that is structurally prior to the aspirational criterion Builder, not as a gate within the
Builder's instructions or a post-draft audit step. Tests whether the construction workflow
names a specific role whose sole output is the independence map, and whose completion is the
Builder's input precondition -- so that the Builder receives a completed independence map as
input rather than verifying independence concurrently with construction. A rubric whose
Builder instructions include a pre-criterion independence check (satisfying C-25 partially)
but with no dedicated prior role boundary fails C-29: the independence check is concurrent
with, not prior to, construction, and can be abbreviated or skipped without violating the
Builder's role contract. The distinction from C-25: C-25 requires one-to-one assignment as
a design principle and requires the assignment to be stated explicitly; C-29 requires that
verification occur in a named, sequentially prior role phase, making it structurally impossible
to begin writing aspirational criteria without a completed independence map. The distinction
from C-18: C-18 requires a definitional step prior to criterion-field construction; C-29
requires that independence verification specifically -- not direction instantiation -- be a
prior named role step with the independence map as its exit condition. Evidence: V-04's
four-role sequence (Dual Definer -> Builder E+R -> Mechanism Definer -> Builder aspirational
-> Dual Auditor) places the MECHANISM DEFINER between construction phases; the Definer's exit
condition is the independence map; the Builder aspirational cannot run until the map is
complete and shows "Yes -- affects C-NN only" in every row.

**C-30** (independence-demonstrable-by-removal) -- The mechanism set is assembled so that
independence is demonstrable by the removal test: removing any single mechanism from the
architecture leaves exactly one criterion failing, confirming that no mechanism carries dual
responsibility for two gaps and that no two mechanisms jointly close a single criterion.
Tests whether the rubric builder's mechanism assignment satisfies the removal test as a
structural property -- independently verifiable by an evaluator who inspects what criterion
would fail if each mechanism were absent, without reading the mechanism-design rationale.
A rubric whose mechanism map correctly names one mechanism per criterion (satisfying C-25 by
declaration) but whose mechanisms share structural dependencies -- such that removing
mechanism A degrades both criterion X and criterion Y because they both rely on a shared
structural property A produces -- satisfies C-25 by statement but fails C-30 by construction.
The distinction from C-25: C-25 requires one-to-one assignment as a stated principle,
evidenced by named mechanism-criterion pairs; C-30 requires the architecture to satisfy the
removal test as a constructive property, making independence verifiable by inspection rather
than by reading the builder's design argument. The distinction from C-29: C-29 requires a
dedicated prior role step to produce the independence map; C-30 requires that the mechanism
set itself passes the removal test -- the role boundary can exist (C-29 pass) while the
mechanisms share dependencies (C-30 fail). Evidence: V-05's three-mechanism design --
MECHANISM MAP, OUTPUT OWNERSHIP PRINCIPLE, Pattern-Matcher competitor block -- demonstrates
independence by construction: removing any one mechanism leaves exactly one criterion failing
(C-25, C-26, or C-27 respectively), no mechanism degrades two criteria, and no two mechanisms
jointly close one criterion; independence is architectural, not asserted.

**C-31** (aspirational-tier-count-bounded) -- The tier distribution specification names an
explicit upper bound for the aspirational tier count ("1-2 aspirational"), completing the
three-tier count triplet; the aspirational tier is bounded by the same range-setting
instruction that bounds the essential and recommended tiers. Without an aspirational ceiling,
a rubric builder can produce a criteria-dense aspirational tier that absorbs failures from
the recommended tier, inflates the aspirational score, and makes the tier structure
progressively meaningless as criteria accumulate. Not "targets stated for essential and
recommended only" but "targets stated for all three tiers, with the aspirational upper bound
making over-population of the aspirational tier a STOP condition parallel to the essential
and recommended ranges." Tests whether the role spec states an explicit aspirational count
range alongside the essential and recommended ranges, and whether the aspirational upper
bound is operative (a STOP or rewrite condition for a builder who drafts more than two
aspirational criteria, not merely a preference). The distinction from C-06: C-06 requires
tier count targets to be present; C-31 requires the aspirational tier's explicit upper bound
to complete the three-tier triplet. A role spec can satisfy C-06 partially by stating
essential and recommended ranges while failing C-31 because the aspirational tier is
unbounded. Evidence: all five Round 10 variations specify "3-5 essential / 2-3 recommended"
but none state "1-2 aspirational"; the aspirational tier remains unbounded across the full
round, confirming the gap is systematic rather than incidental.

**C-32** (category-diversity-stop-enforced) -- Category diversity (>= 3 distinct categories
across the full rubric) is enforced by an explicit STOP condition or named verification check
in the operative role's construction instructions, not merely by listing category options as
a menu. Without enforcement, a builder can select three adjacent quality properties from the
same category domain, producing a rubric that appears diverse by label while measuring the
same underlying property from multiple angles. Not "categories offered as choices from a
named list" but "distribution verified by an operative check with a STOP on under-diversity
-- a named condition requiring the builder to confirm >= 3 distinct categories appear before
proceeding to Emit." Tests whether the role spec includes a named STOP condition or
verification step requiring the builder to confirm >= 3 distinct categories across the output;
the check must be operative (blocking Emit if the distribution requirement is not met) rather
than aspirational (noting that diversity is preferred). The distinction from C-07: C-07
requires that 3+ distinct categories appear across the full rubric; C-32 requires that their
presence is enforced by an explicit operative check, not merely encouraged by the category
menu. A rubric can satisfy C-07 incidentally (the output happens to have 3+ categories
because the builder selected well from the menu) while failing C-32 (no operative STOP made
the distribution required). Evidence: all five Round 10 variations list five category options
(correctness | depth | format | coverage | behavior) but none include a verification step or
STOP condition requiring >= 3 distinct categories in the output; C-07 is universally PARTIAL
across Round 10, confirming that listing options does not produce enforced diversity.

**C-33** (partial-handling-named-in-scoring) -- The scoring specification names PARTIAL
handling as an explicitly required sub-element, defining the fractional score assigned to a
PARTIAL result and the conditions under which a criterion earns PARTIAL rather than PASS or
FAIL; all three scoring states are named with their values and earn conditions. Without named
PARTIAL handling, a rubric whose criteria have partial-satisfaction states produces
inconsistent scoring -- evaluators assign partial credit by judgment rather than by defined
procedure, making the same criterion earn different point values across evaluators. Not
"PARTIAL implied by the composite formula structure" but "PARTIAL named as a third scoring
state alongside PASS and FAIL, with fractional score value (e.g., 0.5) and earn conditions
stated explicitly in the Scoring section." Tests whether the Scoring section contains an
explicitly named PARTIAL sub-element that states: (a) the fractional score value and (b) the
conditions under which a criterion earns PARTIAL rather than PASS or FAIL; both elements must
be present, not just the score value or the earn conditions alone. The distinction from C-04:
C-04 requires the composite formula and golden threshold to be stated; C-33 requires PARTIAL
handling to be a named scoring sub-element with score value and earn conditions, making the
three-state scoring system complete and unambiguous. A rubric passes C-04 (formula and
threshold present) while failing C-33 (PARTIAL is implied by the formula structure but not
named with earn conditions). Evidence: V-01 and V-02 require Phase 4 Emit to produce
"Scoring -- composite formula, golden threshold, PARTIAL handling" as three named sub-
elements; V-03, V-04, and V-05 require only "Scoring" with no sub-element specification,
leaving PARTIAL handling undefined in the rubric output.

**C-34** (independence-map-criterion-annotated) -- The independence map produced by the
Mechanism Definer cites the single affected criterion by number for each mechanism entry,
enabling a third-party auditor to verify the one-to-one assignment without running the
removal test. Without criterion-specific annotation, the independence map is a declarative
table (mechanisms listed, independence claimed) rather than a verifiable artifact -- an
auditor must construct the argument that each mechanism targets exactly one criterion by
reading the mechanism descriptions and matching them to criteria. Not "independence declared
per mechanism" but "criterion number cited per mechanism entry in the form 'affects C-NN
only,' with a STOP condition if any entry is blank or cites multiple criteria." Tests whether
the independence map's output format includes, for each mechanism entry, an explicit citation
of the single criterion it affects (e.g., "Yes -- affects C-NN only"); whether the map
format makes it structurally impossible to complete an entry without naming a specific
criterion; and whether there is a STOP condition for entries that are absent, blank, or cite
multiple criteria. The distinction from C-29: C-29 requires the Mechanism Definer role to
produce a completed independence map as its exit condition; C-34 requires the map's per-entry
format to cite the affected criterion by number, making the map independently auditable.
A rubric satisfies C-29 (dedicated prior role, map exists) while failing C-34 (the map
entries declare independence without naming the affected criterion). The distinction from
C-30: C-30 requires the mechanism set to satisfy the removal test as a constructive property;
C-34 requires the map to encode criterion-specific annotations enabling third-party audit
without the removal test -- a mechanism set satisfying C-30 by construction can still fail
C-34 if the per-entry criterion citations are absent from the map format. Evidence: V-02's
independence map uses "Yes -- affects C-NN only" per entry with an explicit STOP condition
for any "No" row; the format makes the one-to-one assignment auditable from the map alone,
without access to the criteria or the removal test. V-01's PARTIAL on C-25 traces precisely
to this gap: one-to-one assignment is implicit in V-01's competitor-block structure, but no
independence map format with criterion citations exists, so the assignment cannot be verified
by a third party without reading the mechanism descriptions and performing the matching step.

**C-35** (divergence-check-operationalized) -- After criteria are assigned to tiers, a named
verification step counts the category assignments per tier, identifies the majority category
for each tier, and outputs the per-tier distribution as a structured artifact; the step
includes a STOP condition if fewer than 2 of 3 tiers have distinct majority categories.
Without this step, tier-to-severity grounding produces organic diversity by design intent
but leaves the distribution unverified -- an evaluator cannot confirm the diversity claim
without re-reading all criteria and performing the count manually. Not "tiers grounded in
distinct failure dimensions so that diversity is expected to emerge" but "majority category
computed per tier after assignment, distribution recorded as a named output, STOP fires before
Emit if the >= 2/3-distinct-majority requirement is not met." Tests whether the construction
workflow includes a named step that: (a) counts category assignments within each tier,
(b) identifies the majority category per tier, (c) outputs the count as a verification table
(e.g., "Essential: correctness x3, depth x1, format x1 -- majority: correctness. Recommended:
depth x2, format x1 -- majority: depth. Aspirational: behavior x1, coverage x1 -- no
majority"), and (d) fires a STOP if < 2 tiers have distinct majority categories, requiring
revision before Emit. The distinction from C-13: C-13 requires the tier structure to be
grounded in distinct failure dimensions and requires the divergence check to be run; it is
universally PARTIAL in Round 11 because all five variations satisfy the grounding requirement
but none produce the explicit check as a named step with structured output. C-35 requires the
check to be operationalized -- a named step, a structured output format, and a STOP condition
-- making the verification independently falsifiable by an evaluator who examines the
construction record rather than re-deriving the distribution from the criteria themselves.
A rubric whose tier design organically produces category diversity (satisfying C-13 partially)
fails C-35 if no named step captures and records the distribution; design intent and
verification artifact are distinct requirements. Evidence: all five Round 11 variations assign
criteria by failure severity, which produces organic diversity (C-13 PARTIAL across the board)
but none output a per-tier category count or name a step that would fire if the distribution
requirement were not met; the universal PARTIAL on C-13 confirms the operationalization gap
is systematic.

**C-36** (competitor-at-construction-step) -- Each named competitor that constitutes a gap
specification (C-27) appears inline at the specific construction step where the wrong
implementation would most naturally be produced -- not in a preamble, operating-principles
section, or shared block preceding all mechanism definitions. When a competitor is placed at
a construction step, the builder encounters the gap specification at the exact moment of
commitment: before writing the aspirational count, before writing the category assignment,
before writing the scoring section. This creates a just-in-time prevention gate whose
authority derives from temporal proximity, not from prior reading or ambient context.
Not "competitor named before the positive definition" but "competitor placed inline at the
construction step for its specific mechanism -- the wrong implementation is the first content
the builder reads before making the structural decision the competitor's failure traces to."
Tests whether each competitor block appears as the opening of the construction step whose
output it governs -- so that the gap specification is encountered before the design decision
is committed, not during a general preamble that precedes all steps simultaneously. The
distinction from C-27: C-27 requires the competitor to constitute the gap specification
regardless of placement; C-36 requires the competitor to be placed at the construction step
whose wrong output it specifies. A rubric can satisfy C-27 (competitor correctly constitutes
the gap spec, placed in an operating-principles block at the start of the role) while failing
C-36 (the competitor is read once at role startup, not at the specific construction step).
The distinction from C-11: C-11 requires a structured Reference / Passes / Fails anchor
before the aspirational section opens, using a prior-version reference whose overall design
passes essential+recommended; C-36 requires per-mechanism competitors to be placed at the
step for each mechanism specifically, with temporal anchor at the mechanism's construction
moment. V-05's PARTIAL on C-11 traces precisely to this gap: V-05 places the Unbounded-
Aspirational competitor at Builder A (satisfying C-36), but the three-field prior-version
Reference / Passes / Fails format required by C-11 is absent. Evidence: V-05's Unbounded-
Aspirational competitor appears at Builder A (the step where aspirational count is committed);
the Category-Menu competitor at the category-verification step; the Formula-Only Scorer
competitor at the scoring-section step; the Declared-Independent Map competitor at the
Mechanism Definer step -- each competitor is the first content read before the structural
decision it governs. V-01--V-04 fail C-27 entirely (no competitors) and therefore fail C-36
by absence; V-05 PASS on C-36 by placing each competitor inline at its construction step.

**C-37** (competitor-criterion-coverage-complete) -- For every aspirational criterion that
introduces a novel construction requirement -- a requirement that does not appear in the
essential or recommended tiers and that creates a new decision point the builder must navigate
during aspirational criterion construction -- there is exactly one named competitor that IS
its gap specification (C-27), and the total competitor count equals the novel-requirement
criterion count. The gap structure is enumerable by inspection: a reader who counts the
competitors knows how many novel construction requirements the rubric's aspirational tier
introduces, without reading the criteria themselves. Without complete coverage, a rubric can
have well-formed competitors for some gaps while leaving others navigated only by positive
specification -- the builder can produce a wrong implementation of an uncovered gap because
no competitor makes the wrong form visible before the construction decision is committed.
Not "competitors exist for some novel criteria" but "every novel construction requirement in
the aspirational tier has exactly one competitor, the set of competitors and the set of
novel-requirement criteria are in bijection, and the total competitor count equals the total
novel-criterion count." Tests whether the rubric's competitor set covers all aspirational
criteria that introduce structural design decisions not constrained by essential or recommended
criteria; whether each novel criterion has exactly one competitor (no criterion covered by two
competitors, no competitor covering two criteria); and whether the coverage is verifiable by
inspection. The distinction from C-27: C-27 requires competitors to exist and to constitute
gap specifications for the mechanisms they accompany; it is satisfied by naming any number of
well-formed competitors, regardless of whether all novel criteria are covered. C-37 requires
the coverage to be complete -- a rubric with two well-formed competitors for two criteria
(C-27 PASS) but two additional novel criteria with no competitors fails C-37 even though its
competitors satisfy C-27. The distinction from C-25: C-25 requires one-to-one assignment
between mechanisms and criteria at the architecture level (what the output contains); C-37
requires one-to-one correspondence between competitors and novel criteria in the gap-
specification layer (what the builder reads before constructing). The distinction from C-36:
C-36 requires each competitor to be placed at the correct construction step; C-37 requires
the competitor set to be complete -- a rubric can satisfy C-36 (all present competitors are
at their correct steps) while failing C-37 (some novel criteria have no competitor). Evidence:
V-05 passes both -- four named competitors, each at its construction step (C-36), covering
the four novel aspirational criteria introduced in Round 10 (C-31 -> Unbounded-Aspirational,
C-32 -> Category-Menu, C-33 -> Formula-Only Scorer, C-34 -> Declared-Independent Map)
exactly (C-37). V-01--V-04 fail both by competitor absence.

**C-38** (self-referential-coverage-demonstration) -- When the aspirational tier's set of
novel criteria includes C-37 (the coverage-completeness criterion) itself, the competitor
assigned to C-37 occupies one of the bijection slots that C-37 governs, making coverage
completeness verifiable by counting the competitor list without reading the criteria. The
bijection is self-demonstrating rather than asserted: a reader who enumerates the competitors
and confirms that one (e.g., Partial-Coverage Architect) is assigned to C-37 has verified
that the coverage is complete, because C-37's presence in the competitor set means the set
covers every novel criterion including the coverage criterion itself. Not "coverage
completeness claimed by assertion, by a separate count step, or by consulting the criterion
list" but "the competitor assigned to C-37 is inside the bijection it governs -- counting
the competitors yields the novel-criterion count, and one of those competitors closes C-37,
making the self-inclusion structurally present." Tests whether: (a) C-37 is listed as a novel
criterion in the current round; (b) a named competitor appears at C-37's construction step
(satisfying C-36 for C-37's own competitor); (c) the total competitor count equals the total
novel-criterion count including C-37; and (d) this equality is verifiable by listing and
counting competitors without access to the criterion list. The distinction from C-37: C-37
requires bijection between the competitor set and the novel-criterion set; C-38 requires that
bijection to be self-demonstrating when C-37 is itself a novel criterion -- the competitor
covering C-37 is inside the set whose size C-37 constrains, making completeness a structural
self-inclusion rather than an externally verified claim. A rubric satisfies C-37 (bijection
present) while failing C-38 if C-37 is not a novel criterion in the current round and
therefore has no assigned competitor. C-38 is N/A for rounds where C-37 was introduced in a
prior round and is not itself novel. The distinction from C-36: C-36 requires each competitor
to appear at its construction step regardless of which criterion it covers; C-38 requires
specifically that the competitor at C-37's construction step be present and that its presence
makes the bijection self-verifiable by count. Evidence: V-05 R12 assigns Competitor 7
(Partial-Coverage Architect) to C-37 -- one of the seven novel criteria introduced in Round 12
(C-31--C-37); counting the seven competitors confirms bijection, and one competitor covers
C-37 itself, making the SEVEN-COMPETITOR COVERAGE CONFIRMATION block verifiable by count
without reading the criteria. V-05 R11 satisfies C-37 (four competitors, four novel criteria
in bijection) but fails C-38 because C-37 was not itself a novel criterion in Round 11 (it
was introduced that round but the competitor set covers C-31--C-34, not C-37 itself).

**C-39** (competitor-at-verification-step) -- The competitor-then-imperative pattern (C-27,
C-28, C-36) applies to verification-step gaps as well as construction-design gaps: when a
criterion requires a named verification step (e.g., C-35 requires a divergence-check step),
the gap between organic verification-by-design-intent and operationalized verification is
closed by placing a named competitor inline at the verification step where the wrong form
would be accepted as sufficient -- not by direct procedural instruction, additional table
entry, or role gate. The competitor names the specific wrong form of verification (e.g.,
Tier-Blind Categorizer: a rubric whose tier-grounded design produces organic category
diversity, relying on design intent without counting or outputting a distribution), and ends
with a derivation instruction ("from the description above, derive what the required
verification step must do -- before reading the operative requirement"), converting the
verification gap into a required reader procedure before the positive step is specified.
Not "verification-step gap closed by adding a check to the procedure" but "verification-step
gap closed by a named competitor placed inline at the post-draft audit or verification step,
constituting the gap specification for the operationalization requirement, following the
competitor-then-imperative axis." Tests whether: (a) each verification-step gap (a criterion
requiring a named verification step that is universally absent in the prior round) has a named
competitor placed inline at the verification step rather than in a preamble or as a separate
instruction; (b) the competitor constitutes the gap specification for the verification
requirement -- naming the wrong form of verification and making the required step derivable
from the competitor alone; (c) the competitor block ends with a derivation instruction;
and (d) the placement is at the verification step itself, so the builder encounters the wrong-
form competitor at the moment of committing to how to verify, not during general orientation.
The distinction from C-36: C-36 requires each competitor to appear at the construction step
for its mechanism (where a design decision is committed); C-39 extends the same placement
requirement to verification steps -- steps that check whether a design requirement is met
rather than steps that produce the design itself. The distinction from C-35: C-35 requires
the divergence-check step to be present, named, structured, and STOP-gated; C-39 requires
the gap that C-35 closes to be made visible through an inline competitor at the verification
step, following the competitor-then-imperative pattern, rather than being stated directly as
a procedural instruction. A rubric can satisfy C-35 (step added by direct instruction, present
and operative) while failing C-39 (no competitor precedes the step, wrong form not visible
before positive requirement). The distinction from C-28: C-28 requires all competitor blocks
to end with a derivation instruction regardless of what gap they close; C-39 requires
specifically that verification-step gaps are closed by competitors at verification steps -- a
rubric can satisfy C-28 for all construction-step competitors while failing C-39 if no
competitor appears at any verification step. Evidence: V-05 R12 closes C-35 via the Tier-
Blind Categorizer placed inline at the post-draft audit step -- the competitor names the wrong
form (organic diversity without a named step), ends with a derivation instruction, and appears
before the divergence-check step specification; the gap between design-intent verification and
operationalized verification is made visible through a wrong-form competitor before the
required step is stated, extending the competitor-then-imperative axis from construction-
design gaps to verification-step gaps. The Tier-Blind Categorizer simultaneously closes C-35
(the step exists, derived from the competitor) and upgrades C-13 from PARTIAL to PASS (both
the tier-grounding and the operationalized check are now present), demonstrating that a
correctly placed verification-step competitor can satisfy multiple interdependent criteria
through the derivation instruction.

---

## Scoring

```
Essential:    (C-01 + C-02 + C-03 + C-04 + C-05) x 12            max 60
Recommended:  (C-06 + C-07 + C-08) / 3 x 30                       max 30  (partials = 0.5)
Aspirational: (C-09 through C-39) / 31 x 10                        max 10  (partials = 0.5)

Composite = Essential + Recommended + Aspirational                  max 100
Golden threshold: >= 90
```

**Scoring note:** The aspirational denominator shifts from `/29` to `/31` to reflect the
addition of C-38 and C-39.

*Round 12 ceiling recalibration.* V-05 R12 under v12 scored 28.5/29 x 10 = 9.828 aspirational
(reported as 99.83 composite): C-13 upgraded from PARTIAL to PASS (Tier-Blind Categorizer
provides the operationalized divergence check); C-35 closed (Tier-Blind Categorizer placed at
audit step); C-36 and C-37 PASS as in Round 11; C-11 PARTIAL remaining. Under v13 (/31):
V-05 R12 PASS C-38 (Competitor 7 at C-37's construction step, seven-competitor self-
referential bijection confirmed by count) and PASS C-39 (Tier-Blind Categorizer inline at
verification step, competitor-then-imperative axis extended). New aspirational: 30.5/31 x 10
= 9.839, composite 99.839. C-11 PARTIAL is the sole remaining gap; clearing it yields 100.

*C-38 closes the self-referential coverage gap.* C-37 requires bijection between competitors
and novel criteria; any well-formed competitor set of the right size satisfies it. C-38
requires that when C-37 itself is a novel criterion, the bijection be self-demonstrating --
the coverage criterion is covered, making completeness verifiable by counting without
accessing the criterion list. The SEVEN-COMPETITOR COVERAGE CONFIRMATION block in V-05 R12
confirms this: seven competitors, one per novel criterion (C-31--C-37), Competitor 7 covering
C-37 itself. Counting confirms bijection; no criterion list is needed. The pattern is
recursive: in any future round where C-38 is itself a novel criterion, a rubric satisfying
C-38 would require an eighth competitor (Partial-Self-Coverage Architect) covering C-38,
extending the self-referential chain.

*C-39 extends the competitor axis to verification steps.* C-36 places construction-step
competitors at design-commitment moments; the competitor-then-imperative axis previously
applied only to decisions about what to produce. C-39 extends the same temporal-proximity
mechanism to verification decisions -- how to verify. The Tier-Blind Categorizer named inline
at the post-draft audit step makes the wrong form of verification the first thing the builder
reads before specifying the required step, satisfying both C-35 (step now exists, derived
from competitor) and C-13 (divergence check is operationalized, not merely grounded). A
single well-placed verification-step competitor closes multiple interdependent criteria through
the derivation instruction -- the pattern of multi-criterion closure is the diagnostic
signature of a well-placed verification-step competitor.

*C-38 and C-39 form two structural extensions of the coverage triad.* C-27 -> C-36 -> C-37
established existence -> placement -> completeness for construction-step competitors. C-38
extends completeness into self-reference (the coverage criterion covers itself when novel),
and C-39 extends placement into a new step class (verification steps). A rubric satisfying
C-27, C-36, C-37, C-38, and C-39 has a complete, correctly-placed, self-demonstrating
competitor set for construction gaps and at least one correctly-placed competitor for each
verification-step gap, making the negative-space specification exhaustive across both decision
classes.
