Written to `simulations/quest/rubrics/org-review-rubric-v9-2026-03-16.md`.

---

**v9 summary:**

**Scale changes v8 → v9:**
- Aspirational: 18 → **21 criteria** | 90 → **105 pts**
- Total: 180 → **195 pts** | Gold: 145 → **160**

**Three new criteria:**

| ID | Name | Source | PASS | FAIL |
|----|------|--------|------|------|
| C-27 | CH-ID Cross-Section Saturation Pre-committed | V-01, V-04, V-05 R9 | 3 variants | V-02, V-03 |
| C-28 | Null Hypothesis Progression Formula Pre-committed as 3-Stage Mechanical Contract | V-02, V-04, V-05 R9 | 3 variants | V-01, V-03 |
| C-29 | Scope-to-Finding Coverage Gate Post-Bracket-Closing | V-03, V-05 R9 | 2 variants | V-01, V-02, V-04 |

**Round 9 scores under v9:**

| Rank | Variant | v8 | v9 | Delta |
|------|---------|----|----|-------|
| 1 | **V-05** | 180 | **195/195** | +15 |
| 2 | **V-04** | 180 | **190/195** | +10 |
| 3 | V-01 | 180 | **185/195** | +5 |
| 3 | V-02 | 180 | **185/195** | +5 |
| 3 | V-03 | 180 | **185/195** | +5 |

The three new criteria mirror the C-24/C-25/C-26 independence pattern exactly: each appears in at least one variant without the others, each has a distinct structural layer (cross-section saturation / temporal progression formula / post-execution coverage gate), and all three require V-05 to achieve Perfect. No retroactive score changes on R1–R8.
**Category**: correctness

Severity labels (HIGH / MEDIUM / LOW, or equivalent) carry explicit commit-gate meaning -- not
aesthetic importance. HIGH means the finding blocks commitment to proceed. MEDIUM means
commitment may proceed only after remediation. LOW is advisory; commitment may proceed. These
semantics are stated somewhere in the output (preamble, legend, or first use). A severity label
that is present but never defined scores partial.

**Pass condition**: the output defines or cites severity semantics that map directly to
proceed/condition/block commitments. Every finding severity label is interpretable against these
semantics.

**Fails if**: severity labels are absent, or labels appear with no stated meaning.

---

### C-03 -- Null Hypothesis Gate Before Domain Testimony
**Weight**: essential | **Points**: 12 | **Category**: correctness

The review surfaces and addresses the null hypothesis -- what the team does today instead of
building this, and why that is acceptable -- before domain-specific findings. The null hypothesis
gate produces its own verdict. Domain findings do not substitute for it. The challenger role
(C-01) provides the null hypothesis testimony; if no named challenger exists, the review includes
an explicit null hypothesis section regardless.

**Pass condition**: a null hypothesis statement and verdict appear before domain-specific
reviewer sections. The verdict is a distinct signal (PASS / CONDITIONAL / FAIL or equivalent),
not prose absorbed into domain findings.

**Fails if**: no null hypothesis is addressed, or domain findings are the primary vehicle for
null hypothesis evaluation.

---

### C-04 -- Commitment Disposition Emitted
**Weight**: essential | **Points**: 12 | **Category**: behavior

The review closes with an explicit disposition from a fixed vocabulary: READY (proceed),
CONDITIONAL (proceed after remediation), or BLOCKED (do not proceed). The disposition is a
labeled field, not a prose conclusion. The disposition is grounded in the findings -- it does not
contradict any HIGH-severity finding without explanation.

**Pass condition**: output contains a clearly labeled disposition field with a value from
READY / CONDITIONAL / BLOCKED (or exact equivalents). The disposition is consistent with
finding severities.

**Fails if**: no disposition is emitted, or disposition is embedded in prose without a labeled
field, or disposition contradicts HIGH findings without explanation.

---

### C-05 -- Action Items Traceable to Findings
**Weight**: essential | **Points**: 12 | **Category**: behavior

The review produces a traceable action list. Each action item traces to the finding that
generated it (by role + finding reference, or numbered citation). Items are distinguished by
disposition class: BLOCKED items must be resolved before any commitment, CONDITIONAL items must
be resolved before proceeding, advisory items may be deferred. The action list is a synthesis
artifact -- not re-stating reviewer recommendations verbatim.

**Pass condition**: output contains >= 1 action item per HIGH or MEDIUM finding. Each item
carries a disposition class and finding reference. The list is consolidated (not scattered across
reviewer sections).

**Fails if**: no consolidated action list exists, or items cannot be traced to specific findings.

---

## Recommended Criteria -- 30 pts (output is better with these)

### C-06 -- Artifact Scope Declared Before Review Begins
**Weight**: recommended | **Points**: 10 | **Category**: coverage

The review explicitly enumerates what is under review: artifact name, version, surfaces in scope
(spec, design, prior decisions, constraints), and surfaces explicitly out of scope. Scope is
declared before reviewer sections begin -- not inferred from reviewer comments. Any artifact
discovered mid-review is flagged as a scope gap, not silently incorporated.

**Pass condition**: a scope section or preamble block names in-scope and out-of-scope surfaces
before the first reviewer section. Mid-review artifact discoveries are flagged.

**Fails if**: scope is defined only in passing within reviewer sections, or is never declared.

---

### C-07 -- Summary with Integrating Narrative
**Weight**: recommended | **Points**: 10 | **Category**: depth

The review closes with a synthesis section that integrates findings across roles -- naming
conflicts (where two roles' recommendations are incompatible), convergence (where all roles
agree), and uncovered areas. The summary explains why the disposition is what it is, not just
what it is. The null hypothesis verdict is explicitly referenced.

**Pass condition**: a synthesis/summary section exists. It names at least one cross-role
conflict or convergence. It references the null hypothesis verdict. It explains the disposition
rather than restating it.

**Fails if**: the summary is absent, or emits a disposition without integrating narrative.

---

### C-08 -- Depth Parameter Honored
**Weight**: recommended | **Points**: 10 | **Category**: behavior

If --depth deep is specified, the review runs all available roles (not filtered). If
--depth standard (default), the review selects roles relevant to the artifact type and states
the selection rationale. If --depth quick, the review covers top-priority roles with an
explicit note that coverage is abbreviated. The depth mode is acknowledged in the output.

**Pass condition**: output reflects the requested depth mode. standard/deep depth modes produce
>= 5 roles. quick depth produces >= 3 roles with abbreviation note. Role selection rationale is
stated for standard mode.

**Fails if**: output ignores the depth parameter, or role count is inconsistent with depth
without explanation.

---

## Aspirational Criteria -- 105 pts (structural integrity, auditability, automation)

### C-09 -- Adversarial Bracket Architecture
**Weight**: aspirational | **Points**: 5 | **Category**: depth

The challenger role runs both before domain testimony (Bracket Opening: null hypothesis
challenge) and after all domain sections (Bracket Closing: does domain evidence actually answer
the challenge?). Domain reviewers write without seeing the Bracket Closing. The Bracket Closing
reassesses whether domain evidence defeated the null hypothesis, not just whether the artifact is
technically sound. The closing challenger carries override authority -- a FAIL at closing
overrides domain PASses.

**Pass condition**: challenger appears in two distinct sections (pre-domain and post-domain).
Post-domain section explicitly references domain findings and reassesses the null hypothesis
challenge. Override authority is stated.

**Fails if**: challenger appears only once (standard gate sequencing, not bracket architecture).
Partial if bracket exists but override authority is absent.

---

### C-10 -- Disposition Algebra Committed Before Execution
**Weight**: aspirational | **Points**: 5 | **Category**: correctness

The mapping from gate verdicts to overall disposition is stated as an explicit formula before any
reviewer sections execute. The formula names the rule for each combination (e.g., "BLOCKED if
any gate = FAIL; CONDITIONAL if no FAIL and >= 1 CONDITIONAL; READY if all PASS"). The
evaluator applies the formula -- they do not reason editorially from findings at summary time.
The formula is placed in the preamble, not generated at summary time.

**Pass condition**: a disposition formula appears in the preamble or pre-execution template.
The formula covers all gate-verdict combinations. The summary section applies the formula rather
than producing one.

**Fails if**: no disposition formula is stated. Partial if formula appears only at summary time
(after all verdicts are visible).

---

### C-11 -- Override Decision Emitted as Labeled Field
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 1 -- Override invoked: YES | NO as labeled field in Bracket Closing

When adversarial bracket override authority exists (C-09), the override decision is emitted as a
labeled boolean field (Override invoked: YES | NO or equivalent) within the Bracket Closing
section -- not implied by the overall BLOCKED disposition. The field is machine-readable and
referenced by the disposition formula. An auditor can verify whether the Bracket Closing override
was exercised without reading the disposition reasoning.

**Pass condition**: a labeled override field appears in the Bracket Closing section when C-09 is
active. The field value (YES or NO) is unambiguous. The disposition formula references the field.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). A C-09
failure automatically makes C-11 vacuous.

**Fails if** (C-09 active): override decision must be inferred from prose or from the final
disposition; no labeled field present.

---

### C-12 -- Action Item Class Derived Mechanically from Gate Verdicts
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-05 Round 1 -- "Class derives mechanically from gate verdict (FAIL -> BLOCKED,
CONDITIONAL -> CONDITIONAL)" stated in preamble as derivation rule

The disposition class assigned to each action item (BLOCKED / CONDITIONAL / ADVISORY) derives
from the gate verdict that generated it, not from editorial re-assessment of finding text at
synthesis time. The derivation rule is stated in the preamble. The evaluator applies the rule;
they do not independently assign classes at synthesis time.

**Pass condition**: a gate-to-class derivation rule is stated before action item synthesis.
Action item classes are consistent with the rule. No item's class contradicts the gate verdict
that sourced it.

**Fails if**: no derivation rule is stated. Partial if a rule is stated but some items are
assigned classes inconsistently with it, or if the rule appears only after all reviewers have
executed (post-commitment).

---

### C-13 -- Prompt Inputs as Template Variables
**Weight**: aspirational | **Points**: 5 | **Category**: automation
**Source**: V-04 Round 1 -- explicit {{depth}} template variable was the decisive difference
between PASS and PARTIAL on C-08

Review inputs (at minimum: depth mode, artifact under review) are declared as explicit template
variables in the prompt structure (e.g., {{depth}}, {{artifact_id}}, {{reviewer_set}}), not
described only in natural language. The output acknowledges the injected variable values.

**Pass condition**: >= 2 template variables are declared in the prompt template. The output
contains an explicit acknowledgment block showing injected values. Variables cover at minimum
depth mode and artifact identity.

**Fails if**: no template variables are declared. Partial if one variable is declared but
artifact identity or depth mode is missing.

---

### C-14 -- Gate Verdict Preserved in Action Register
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-02 Round 2 -- Finding Reference: [role] / [gate verdict] / [finding] as positional
slot; V-04 Round 2 -- dedicated Gate Verdict column in action register table

The action register preserves the intermediate gate verdict (FAIL / CONDITIONAL / PASS) for each
action item -- either as a dedicated table column or as a defined positional slot in the finding
reference string. Without it, verifying that the class derivation rule (C-12) was applied
correctly requires re-reading reviewer narrative.

**Pass condition**: every row in the action register carries an explicit gate verdict value in a
dedicated column or defined positional slot. The gate verdict for each row is consistent with the
verdict recorded in the corresponding reviewer section.

**Fails if**: no gate verdict in the action register (class only, no intermediate verdict).
Partial if gate verdicts appear for some rows but not all, or verdict is embedded in prose rather
than a defined structural position.

---

### C-15 -- Reviewer Set as Injectable Template Parameter
**Weight**: aspirational | **Points**: 5 | **Category**: automation
**Source**: V-04 Round 2 -- {{reviewer_set}} declared as third template variable beyond
{{artifact_id}} and {{depth}}

The set of domain reviewers invoked by the prompt is declared as an injectable template variable
({{reviewer_set}} or equivalent), not hardcoded in the prompt structure or selected editorially
at review time. C-13 parameterizes what to review and how deep; C-15 parameterizes who reviews.

**Pass condition**: the prompt declares a template variable for reviewer selection. The output
acknowledgment block emits the injected reviewer set value. The review invokes reviewers
consistent with the declared variable value.

**Fails if**: reviewer selection is hardcoded or selected editorially (not injectable). Partial
if a reviewer variable is declared but not acknowledged in output or not used consistently.

---

### C-16 -- Alternatives Table as Adversarial Bracket Anchor
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 4 -- bracket opening populates 4-dimension comparison table; domain
reviewers re-score same dimensions from their frames; bracket closing aggregates into revised
table and re-applies disposition derivation rule; override auditable from table data

The adversarial bracket uses a quantified multi-dimension comparison table as its structural
anchor. The Bracket Opening (challenger/inertia-advocate) populates the table with initial
dimension scores (>= 3 dimensions, scored on a defined scale). Domain reviewers re-score the
same dimensions from their respective frames. The Bracket Closing aggregates the domain scores
into a revised table and re-applies the disposition derivation rule to the aggregated values.
The override decision is auditable from the table data without reading reviewer narrative.

**Pass condition**: a dimension-score table is introduced at Bracket Opening; domain reviewer
sections each re-score the same dimensions; Bracket Closing shows the aggregated revised table
and applies the disposition formula to it. Override decision can be derived from table values
alone.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). A C-09
failure automatically makes C-16 vacuous.

**Fails if** (C-09 active): bracket exists but no quantified dimension table; or domain
reviewers do not re-score the same dimensions; or bracket closing does not aggregate and
re-apply the derivation rule to table values.

---

### C-17 -- Pre-commitment Cascade: All Three Contracts in Preamble
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-05 Round 4 -- first variant to state DISPOSITION CONTRACT + CLASS DERIVATION
CONTRACT + NULL HYPOTHESIS DERIVATION RULE together in preamble before any reviewer runs

All three pre-commitment contracts are stated together in the preamble before any reviewer
section executes:
1. DISPOSITION CONTRACT: gate verdicts -> overall disposition (covers all combinations)
2. CLASS DERIVATION CONTRACT: gate verdict -> action item class (BLOCKED / CONDITIONAL / ADVISORY)
3. NULL HYPOTHESIS DERIVATION RULE: evidence (scores, facts, or alternatives comparison) ->
   null hypothesis verdict (g_null)

Co-locating all three prevents cascade failures where one contract is pre-committed but another
is decided editorially at execution time. C-10 requires (1); C-12 requires (2); C-17 requires
all three. The null hypothesis derivation rule goes beyond C-03 (which requires the gate to
exist) by requiring the mapping to be explicitly pre-committed rather than narrated.

**Pass condition**: all three contracts appear in the preamble, before any reviewer section
begins. The null hypothesis derivation rule is a formula that maps evidence to a g_null verdict
(not an instruction like "evaluate the alternatives"). All three stated before execution.

**Fails if**: any of the three contracts is absent from the preamble, or appears post-hoc.
Partial if exactly two of three contracts are pre-committed.

---

### C-18 -- Inline Gate Ledger at Origin
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-03 Round 4 -- each reviewer section ends with a local ledger row capturing Gate
Verdict + Class at moment of verdict emission; master action register assembled by copying local
rows verbatim

Each reviewer section ends with a local ledger row that captures Gate Verdict + Class at the
moment of verdict emission -- before consolidation. The master action register is assembled by
copying local rows verbatim, not independently synthesized at consolidation time. Structural
defects are visible at origin: a misclassified action item traces to the exact reviewer section
where the classification was introduced.

C-14 requires gate verdict in the master register. C-18 requires it to be emitted locally first.
The two are sequential in the derivation chain: local emission (C-18) -> copy to register
(C-14). C-14 can pass while C-18 fails. C-18 passing without C-14 is contradictory: local
emission not copied into the register does not satisfy C-18's assembly requirement.

**Pass condition**: each reviewer section includes a local ledger row (or equivalent inline
capture block) with at minimum Gate Verdict + Class. The prompt defines the local ledger syntax.
The master register assembly instruction states rows are copied from local ledgers.

**Fails if**: gate verdicts appear only in the master register with no per-section local capture.
Partial if some reviewer sections include local ledger rows but others do not.

---

### C-19 -- Gate Ledger Protocol as Pre-committed Fourth Contract
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-04 and V-05 Round 5 -- LOCAL GATE LEDGER PROTOCOL stated in preamble as fourth
pre-committed contract alongside the three C-17 algebraic contracts

The LOCAL GATE LEDGER PROTOCOL (defining local ledger row syntax, mandatory emission timing, and
assembly rule) is committed in the preamble as a fourth pre-commitment contract, alongside the
three contracts required by C-17. C-17 pre-commits the algebraic contracts (what formulas to
apply); C-19 pre-commits the procedural contract (how local gate ledger rows are structured and
assembled). A prompt with C-17 PASS and C-19 FAIL pre-commits the formulas but leaves the
chain-of-custody mechanism editorial -- the AI decides local ledger format at execution time,
making cross-section comparison unreliable.

**Pass condition**: LOCAL GATE LEDGER PROTOCOL (or equivalent) appears in the preamble,
defining: (a) the syntax of a local ledger row (Gate Verdict + Class at minimum), (b) when to
emit it (end of each reviewer section, after verdict), and (c) the assembly rule (copy to master
register verbatim). Protocol is stated before any reviewer section executes.

**Vacuous case**: C-18 not active (no inline gate ledger emitted) -- this criterion scores 0
(not partial, not fail). C-18 FAIL automatically makes C-19 vacuous.

**Fails if** (C-18 active): local ledger rows are emitted (C-18 PASS) but the protocol governing
their syntax and assembly was not pre-committed in the preamble.

---

### C-20 -- Verbatim Assembly Prohibition on Re-derivation
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-04 Round 5 -- "Copy all Local Gate Ledger rows...verbatim. Do not re-derive Gate
Verdict or Class." explicit prohibition; V-05 Round 5 -- "Copy...verbatim" implies same
constraint

The master register assembly instruction explicitly prohibits re-derivation of Gate Verdict or
Class during assembly. The instruction is a copy directive, not a synthesis directive. Without
this prohibition, the AI may silently correct or reclassify local verdicts during consolidation,
breaking the chain of custody that C-18 establishes. The local ledger emits the authoritative
verdict (C-18); C-20 ensures that authority is not overridden during assembly.

C-18 establishes local emission as the point of authority. C-20 protects that authority during
assembly. Together they form a complete chain: local emission (C-18) -> protected verbatim copy
(C-20) -> register (C-14).

**Pass condition**: the master register assembly instruction contains an explicit verbatim-copy
directive and a prohibition on re-deriving Gate Verdict or Class. The instruction is stated
before (or in) the master register section, not post-hoc.

**Vacuous case**: C-18 not active -- this criterion scores 0 (not partial, not fail). C-18 FAIL
automatically makes C-20 vacuous. No local rows exist to copy; the assembly instruction type is
not evaluable.

**Fails if** (C-18 active): master register assembly instruction is a synthesis directive rather
than a verbatim-copy directive; or no explicit prohibition on re-derivation is stated.

---

### C-21 -- Universal Gate Ledger Coverage
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 5 -- chain extends to lifecycle reviewer archetype; §5 Lifecycle Reviewer
emits local row; coverage is universal across bracket, domain, and lifecycle archetypes

The inline gate ledger (C-18) is emitted by ALL verdict-emitting reviewer archetypes, not only
bracket and domain roles. At minimum, coverage must extend to: (a) Bracket Opening (challenger /
inertia-advocate), (b) all domain reviewers, (c) Bracket Closing (post-domain challenger), and
(d) the Lifecycle reviewer (if present). The master register assembly instruction covers all
archetype sections. Without universal coverage, lifecycle verdicts enter the master register
without chain-of-custody tracing, and any classification error introduced by the lifecycle
reviewer is untraceable to source.

C-18 requires some reviewer sections to emit local rows. C-21 requires all verdict-emitting
reviewer archetypes to emit them. C-18 can pass while C-21 fails when bracket and domain roles
emit local rows but the lifecycle reviewer does not (V-04 R5 case).

**Pass condition**: every verdict-emitting reviewer archetype present in the review emits a
local gate ledger row. The master register assembly instruction names ALL sections from which
rows are copied (bracket opening, domain reviewers, bracket closing, lifecycle reviewer). No
verdict-emitting reviewer section is exempt.

**Vacuous case**: C-18 not active -- this criterion scores 0 (not partial, not fail). C-18 FAIL
automatically makes C-21 vacuous.

**Fails if** (C-18 active): any reviewer archetype is absent from the local ledger emission
requirement or from the master register assembly instruction. Partial if lifecycle reviewer
coverage is declared but not executed, or if only some domain reviewer sections emit local rows.

---

### C-22 -- Lifecycle Verdict Integration at Bracket Closing
**Weight**: aspirational | **Points**: 5 | **Category**: depth
**Source**: V-04 Round 6 -- lifecycle reviewer (§4) positioned before bracket closing (§5);
bracket closing names g_lifecycle as a labeled received input to null hypothesis reassessment;
first architecture where Bracket Closing integrates both domain and lifecycle evidence

When bracket architecture is used (C-09 active), the lifecycle reviewer section executes BEFORE
the Bracket Closing section, so the challenger can explicitly receive and reference the lifecycle
gate verdict (g_lifecycle) during null hypothesis reassessment. A Bracket Closing that cannot
see the lifecycle verdict reassesses domain evidence only -- it cannot integrate the lifecycle
signal into the override decision.

V-03 and V-05 use Bracket-Closing-then-Lifecycle ordering; their bracket closings operate before
lifecycle testimony is available. V-04 R6 is the first architecture to sequence lifecycle (§4)
before bracket closing (§5), enabling bracket closing to name "Lifecycle verdict received:
g_lifecycle = [value]" as a labeled field and factor it into the null hypothesis reassessment
alongside domain evidence.

C-21 requires lifecycle to emit a local gate ledger row. C-22 additionally requires the bracket
closing to receive and reference that verdict explicitly -- local emission without bracket
acknowledgment does not satisfy C-22.

**Pass condition**: (C-09 active) the lifecycle reviewer section appears before the Bracket
Closing section in the prompt execution order. The Bracket Closing names the lifecycle gate
verdict explicitly as a received input (labeled field or named reference) in its null hypothesis
reassessment. The lifecycle verdict value is factored into the override decision.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). C-09 FAIL
automatically makes C-22 vacuous.

**Fails if** (C-09 active): bracket closing appears before lifecycle section; or lifecycle
verdict is not named or referenced in the bracket closing reassessment. Partial if lifecycle
section precedes bracket closing but bracket closing does not name the lifecycle verdict
explicitly.

---

### C-23 -- Multi-alternative Null Hypothesis Coverage
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-03 and V-05 Round 6 -- three-alternative table (Status Quo / Build / Hybrid)
with NULL HYPOTHESIS DERIVATION RULE mapping both differentials (B-A and B-C) to one verdict;
prevents verdict from being trivially defeated by choosing a weak comparator

When the alternatives table includes three or more options, the NULL HYPOTHESIS DERIVATION RULE
maps ALL relevant differentials involving the proposed artifact to the verdict -- not just one.
A two-differential rule (e.g., Build beats Status Quo AND Build beats Hybrid) prevents the null
hypothesis from being defeated by cherry-picking the weakest alternative. Without this, a prompt
with a three-alternative table may apply a single-differential derivation rule, allowing the
verdict to PASS even if the artifact beats Status Quo but loses to an incremental improvement.

C-17 requires the derivation rule to be a pre-committed formula. C-23 requires that formula to
cover all relevant pairwise comparisons when three or more alternatives are present. A
multi-input rule remains C-17 compatible as long as it maps evidence to a verdict mechanically
(not narratively) -- ES-R6-1 confirms this.

**Pass condition**: the alternatives table contains three or more options. The NULL HYPOTHESIS
DERIVATION RULE names all relevant pairwise differentials involving the proposed artifact (at
minimum: build vs status quo AND build vs best non-build alternative). The derivation rule is a
formula mapping all named differentials to a single verdict. The formula is pre-committed in the
preamble before any reviewer section executes.

**Vacuous case**: C-09 not active OR the alternatives table contains only two options -- this
criterion scores 0 (not partial, not fail). With exactly two alternatives, a single-differential
rule is sufficient and C-23 does not apply.

**Fails if** (C-09 active, three+ alternatives): the alternatives table has three or more options
but the NULL HYPOTHESIS DERIVATION RULE maps only one differential to the verdict, leaving other
alternatives unaddressed. Partial if more than one differential is evaluated but the rule is
stated narratively rather than as a formula.

---

### C-24 -- Domain-Aggregate Formula Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-04 Round 7 -- DOMAIN-AGGREGATE FORMULA (median rule) pre-committed in preamble as
part of fourth contract; bracket closing §5 applies formula mechanically rather than aggregating
editorially; first architecture with a pre-committed aggregation method for domain verdicts

When domain reviewer verdicts must be aggregated before the bracket closing applies its
disposition derivation rule, the aggregation formula (median rule, majority rule, or equivalent)
is pre-committed in the preamble as part of the fourth (or broader) contract block. The bracket
closing is explicitly instructed to apply the formula rather than select an aggregation method
editorially at execution time. Without this, the AI chooses how to combine domain verdicts at
the moment of bracket closing -- an editorial step invisible to the pre-commitment contracts.

C-17 pre-commits the three algebraic contracts (disposition, class, null hypothesis derivation).
C-19 pre-commits the procedural gate ledger protocol. C-24 extends pre-commitment discipline to
the domain aggregation method -- a distinct formula that determines the input to the disposition
contract when multiple domain reviewers contribute verdicts.

**Pass condition**: a domain-aggregate formula is stated in the preamble before any section
executes. The bracket closing section references and applies the formula mechanically. The
formula covers all cases needed to produce a single aggregated signal from multiple domain
verdicts.

**Vacuous case**: C-09 not active OR no multi-domain aggregation step exists (domain verdicts
enter the disposition formula directly without a separate aggregation layer) -- this criterion
scores 0 (not partial, not fail).

**Fails if** (C-09 active, aggregation step present): domain verdicts are aggregated editorially
at bracket closing without a pre-committed formula; or a formula is referenced but not
pre-committed in the preamble. Partial if a formula is pre-committed but the bracket closing
section does not cite it explicitly.

---

### C-25 -- Non-verdict Section Explicitly Excluded from Gate Ledger
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 7 -- §3.5 Domain-Aggregate Checkpoint explicitly marked "EXCLUDED: §3.5
emits NO ledger row" because §3.5 produces no verdict; first architecture where a non-verdict
intermediate section is unambiguously excluded from the gate ledger emission requirement

When the review includes an intermediate section that synthesizes or checkpoints findings but
produces no gate verdict of its own (e.g., a domain-aggregate checkpoint, a mid-review scope
reconciliation section), the gate ledger protocol explicitly names that section as excluded from
ledger emission. Without this exclusion declaration, the scope of C-21 (universal coverage) is
ambiguous: a reviewer implementing "all sections emit a ledger row" may incorrectly include
non-verdict sections, producing artificial verdicts; a reviewer implementing "verdict-emitting
sections only" may silently exclude sections that should emit.

C-21 requires all verdict-emitting sections to emit ledger rows. C-25 requires the protocol to
explicitly state which sections are NOT verdict-emitting (and therefore exempt from C-21
coverage). Together they form a complete protocol: inclusion by default (C-21) with explicit
exception handling (C-25).

**Pass condition**: the gate ledger protocol (C-19) explicitly names at least one intermediate
non-verdict section and marks it excluded from ledger emission, with a stated reason (e.g.,
"produces no verdict" or equivalent). The exclusion is declared in the preamble or protocol
block, not discovered mid-review.

**Vacuous case**: C-18 not active OR no intermediate non-verdict section exists in the review
architecture -- this criterion scores 0 (not partial, not fail). Vacuous does not mean incorrect;
a review with no non-verdict sections is architecturally simpler, not worse.

**Fails if** (C-18 active, non-verdict section present): the non-verdict section is not
mentioned in the protocol, or is listed under C-21's universal coverage requirement without an
exclusion exception.

---

### C-26 -- Canonical Section Order Pre-committed as Immutable Contract
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-03 and V-05 Round 8 -- §7 SECTION ORDER CONTRACT names the canonical execution
sequence (ROLE MANIFEST -> BRACKET OPENING -> DOMAIN(s) -> LIFECYCLE -> BRACKET CLOSING) as an
immutable constraint in the preamble; distinct from C-22 which checks behavioral ordering in
output; C-26 requires the ordering to be contractually declared before execution so reordering
is a contract violation, not merely an observable defect

The canonical section execution order is declared in the preamble as an explicit immutable
contract term -- not merely implied by the sequence of sections in the template. The declaration
names each section in order and states that reordering is prohibited. Without this, an AI
executing the prompt may reorder sections (e.g., run lifecycle after bracket closing) without
violating any stated contract. C-22 detects when lifecycle appears after bracket closing in the
output (behavioral check on a single ordering constraint); C-26 requires the full canonical
sequence to be pre-committed as a named contract, making any reordering a contract violation
detectable before execution.

V-03 and V-05 Round 8 introduce §7 SECTION ORDER CONTRACT with the explicit sequence
declaration and immutability statement. V-04 Round 8 achieves C-24 + C-25 (Perfect under v7)
without §7 -- its section ordering is implied by the printed template but is not contractually
declared. V-04 is "minimal perfect" under v7; V-05 is the extended perfect that adds C-26.

C-22 is synergistic with C-26: C-22 requires behavioral conformance (lifecycle precedes bracket
closing in the actual output); C-26 requires the ordering to be pre-committed as an immutable
contract. Together they form complete ordering enforcement: declaration (C-26) + behavioral
conformance (C-22). C-26 can satisfy in principle even when the contract names only the ordering
rule without the lifecycle section (if lifecycle is absent from the review), as long as the
declared sequence is immutable.

**Pass condition**: the preamble contains an explicitly labeled section-order contract or
equivalent clause (e.g., "SECTION ORDER CONTRACT", "EXECUTION SEQUENCE: immutable") naming the
canonical section sequence. The contract explicitly states that reordering is prohibited (or that
the sequence is immutable). The named sequence includes at minimum bracket opening, domain
sections, and bracket closing in that order (with lifecycle positioned before bracket closing
when lifecycle is present). The contract is stated before any reviewer section executes.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). Without
the adversarial bracket architecture, there is no multi-section sequence to contractually
constrain. C-09 FAIL automatically makes C-26 vacuous.

**Fails if** (C-09 active): no section order contract is stated in the preamble; or the
execution sequence is only implied by the printed template order without a named immutability
constraint. Partial if a sequence is named but the immutability statement is absent.

---

### C-27 -- CH-ID Cross-Section Saturation Pre-committed as Requirement
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-01, V-04, V-05 Round 9 -- §8 CH-ID SATURATION REQUIREMENT pre-commits a two-tier
coverage formula: SATURATED = response from >= 1 DOMAIN section before LIFECYCLE executes;
FULLY SATURATED = domain + lifecycle both responded before BRACKET CLOSING; dedicated §3.8
CH-ID SATURATION CHECK section verifies pre-LIFECYCLE saturation; BRACKET CLOSING enforces full
saturation and prohibits PASS when any CH-ID is UNSATURATED without waiver; absent in V-02 and
V-03

A dedicated CH-ID SATURATION REQUIREMENT is pre-committed in the preamble defining two
cross-section coverage tiers: (1) SATURATED -- every CH-ID has received a response from at
least one DOMAIN reviewer section before LIFECYCLE executes; (2) FULLY SATURATED -- every CH-ID
has received both a domain and a lifecycle response before BRACKET CLOSING. A dedicated §3.8
CH-ID SATURATION CHECK section runs between the domain sections and LIFECYCLE to verify
pre-LIFECYCLE saturation. BRACKET CLOSING prohibits a PASS verdict when any CH-ID is
UNSATURATED without a stated waiver.

**Distinction from C-05**: C-05 requires every reviewer section to carry a CH-ID response table
(per-section structural rule). C-27 adds the cross-section completion contract: the combination
of responses across all sections must satisfy the two-tier formula, verified at a dedicated gate,
with a blocking enforcement at BRACKET CLOSING. C-05 is a per-section input requirement; C-27
is the cross-section output coverage requirement. C-05 captures the behavioral outcome (table
present in every section); C-27 captures the pre-commitment layer (cross-section coverage
required and mechanically verified, PASS prohibited without saturation).

**Pass condition**: a CH-ID SATURATION REQUIREMENT block appears in the preamble defining the
SATURATED and FULLY SATURATED tiers. A dedicated CH-ID SATURATION CHECK section (or equivalent)
runs after domain sections and before LIFECYCLE. BRACKET CLOSING includes a saturation table and
an explicit prohibition on PASS when any CH-ID is UNSATURATED without waiver. The requirement is
pre-committed, not generated at execution time.

**Vacuous case**: C-09 not active OR C-05 not active (no CH-ID tracing architecture) -- this
criterion scores 0 (not partial, not fail). Without bracket architecture the cross-section
saturation check has no bracket closing to enforce it. Without CH-ID tracing there are no
identifiers to saturate.

**Fails if** (C-09 active, C-05 active): domain and lifecycle sections emit CH-ID response
tables but no cross-section saturation requirement is pre-committed; or BRACKET CLOSING does not
enforce saturation. Partial if a saturation check section exists but the requirement is not
pre-committed in the preamble, or BRACKET CLOSING references saturation without a blocking
prohibition.

---

### C-28 -- Null Hypothesis Progression Formula Pre-committed as 3-Stage Mechanical Contract
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-02, V-04, V-05 Round 9 -- §8/§9 NULL HYPOTHESIS PROGRESSION CONTRACT pre-commits
a 3-stage mechanical derivation: g_null(initial) at BRACKET OPENING (= GOpen), g_null(post-domain)
at §3.5 (= formula over G_domain_agg and g_null(initial)), g_null(final) at BRACKET CLOSING (=
formula over G_lifecycle and g_null(post-domain)); GClose verdict must equal g_null(final) unless
explicit override declared with justification; progression summary reported in CROSS-ROLE SIGNALS
and DISPOSITION; absent in V-01 and V-03

A NULL HYPOTHESIS PROGRESSION CONTRACT is pre-committed in the preamble specifying a three-stage
mechanical derivation chain for the null hypothesis verdict (g_null):
  Stage 1: g_null(initial) = GOpen (Bracket Opening gate verdict)
  Stage 2: g_null(post-domain) = formula(G_domain_agg, g_null(initial))
  Stage 3: g_null(final) = formula(G_lifecycle, g_null(post-domain))
The GClose (Bracket Closing) verdict must equal g_null(final). Deviation requires an explicit
override with named justification. The three g_null values are emitted as labeled fields at
their respective checkpoints. The progression summary appears in CROSS-ROLE SIGNALS and
DISPOSITION.

**Distinction from C-03**: C-03 requires a null hypothesis verdict before domain testimony (a
gate presence requirement). C-28 pre-commits the trajectory formula governing how that verdict
evolves across all three checkpoints. C-03 is a gate; C-28 is a contractually-bound derivation
chain: the verdict cannot evolve arbitrarily -- each stage derives mechanically from the prior
stage plus the incoming gate verdict. Override requires named justification and is auditable as
a deviation from the formula.

**Pass condition**: a NULL HYPOTHESIS PROGRESSION CONTRACT (or equivalent) appears in the
preamble naming all three stages and their derivation formulas. The contract specifies that GClose
must equal g_null(final) or declare an explicit override. The three g_null values are emitted as
labeled fields at their respective checkpoints during execution. The progression is summarized in
CROSS-ROLE SIGNALS or equivalent synthesis section.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). Without
bracket architecture there is no GOpen/GClose pair to anchor the progression chain. C-09 FAIL
automatically makes C-28 vacuous.

**Fails if** (C-09 active): the null hypothesis verdict is produced at each checkpoint (C-03
PASS) but the derivation formula linking checkpoints is not pre-committed -- each stage is
determined editorially at execution time. Partial if two of three stages are pre-committed with
derivation formulas but the third stage is editorial, or if the GClose override requirement is
absent.

---

### C-29 -- Scope-to-Finding Coverage Gate Post-Bracket-Closing
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-03, V-05 Round 9 -- §8/§10 SCOPE COVERAGE GATE PROTOCOL pre-commits a dedicated
§5.5 SCOPE COVERAGE RECONCILIATION section after BRACKET CLOSING mapping each §1 IN-SCOPE
surface to reviewer findings; GAP surfaces forced to LOW advisory and appended to ACTION ITEM
REGISTER as ADVISORY-GAP items; gate emits COVERED/PARTIAL signal (informational only, excluded
from gate ledger); §1 IN-SCOPE rows annotated at enumeration time; absent in V-01, V-02, V-04

A SCOPE COVERAGE GATE PROTOCOL is pre-committed in the preamble specifying that after BRACKET
CLOSING, a dedicated §5.5 SCOPE COVERAGE RECONCILIATION section executes. The section
mechanically maps each surface enumerated in §1 IN-SCOPE to reviewer findings across all
sections. Each surface is classified: COVERED (appears in >= 1 finding) or GAP (no finding).
GAP surfaces are automatically assigned LOW advisory severity and appended to the ACTION ITEM
REGISTER as ADVISORY-GAP items. The gate emits a COVERED/PARTIAL signal that is informational
only -- it does not feed the §3 gate ledger formula and produces no ledger row. The §1 IN-SCOPE
surface list carries an annotation at enumeration time: "These rows are cited in SCOPE COVERAGE
RECONCILIATION."

**Distinction from CROSS-ROLE SIGNALS scope coverage field**: The CROSS-ROLE SIGNALS section
may include a prose "Scope coverage" observation. C-29 captures the contractual pre-commitment:
a dedicated post-bracket-closing section with a mechanical coverage formula, forced advisory
assignment for GAP surfaces, explicit exclusion from the gate ledger, and §1 annotation at scope
enumeration time. The prose field is an observation; §5.5 is a contract enforcement.

**Pass condition**: a SCOPE COVERAGE GATE PROTOCOL (or equivalent) appears in the preamble
defining the §5.5 section, its placement after BRACKET CLOSING, the COVERED/GAP classification
rule, the ADVISORY-GAP forced assignment for gaps, and the informational-only (non-ledger) status
of its output. The §1 scope enumeration carries the annotation that rows will be cited in §5.5.
The §5.5 section executes after BRACKET CLOSING and produces a coverage table mapping every §1
IN-SCOPE surface. GAP items appear in the ACTION ITEM REGISTER as ADVISORY-GAP.

**Vacuous case**: C-09 not active OR no explicit §1 scope surface enumeration exists -- this
criterion scores 0 (not partial, not fail). Without a pre-declared scope surface list the
reconciliation section has no source set to map against.

**Fails if** (C-09 active, §1 scope enumeration present): scope coverage is assessed only
through prose observation in CROSS-ROLE SIGNALS without a dedicated post-bracket-closing section;
or GAP surfaces are not forced to ADVISORY-GAP status; or the section emits a gate ledger row
(violating its informational-only contract). Partial if a dedicated §5.5 section exists but the
pre-commitment is absent from the preamble, or the §1 annotation is missing.

---

## Scoring Reference

### Composite Formula

```
essential_pts    = (essential_pass  / 5) * 60
recommended_pts  = (recommended_pass / 3) * 30
aspirational_pts =  aspirational_pass    *  5   # 5 pts each, max 105
composite = essential_pts + recommended_pts + aspirational_pts
```

**Maximum**: 60 + 30 + 105 = **195 pts**

### Score Bands

| Band | Condition | Composite |
|------|-----------|-----------|
| Gold | all 5 essential pass | >= 160 |
| Strong | all 5 essential pass | 90-159 |
| Partial | <= 4 essential pass | any |
| Minimal | <= 3 essential pass | any |

### Paths to Gold (160 pts)

| Path | Essential | Rec | Asp passed | Composite |
|------|-----------|-----|------------|-----------|
| Full rec + 14 asp | 5/5 | 3/3 | 14/21 | 60+30+70 = 160 |
| 2 rec + 16 asp | 5/5 | 2/3 | 16/21 | 60+20+80 = 160 |
| 1 rec + 18 asp | 5/5 | 1/3 | 18/21 | 60+10+90 = 160 |

### Round 1 Calibration (retroactive, v1 -> v9)

| Variant | C-09 | C-11 | C-16 | C-22 | C-23 | C-24 | C-25 | C-26 | C-27 | C-28 | C-29 | v8 | v9 |
|---------|------|------|------|------|------|------|------|------|------|------|------|----|----|
| V-01 | FAIL | vac | vac | vac | vac | vac | vac | vac | vac | vac | vac | 75 | 75 |
| V-02 | FAIL | vac | vac | vac | vac | vac | vac | vac | vac | vac | vac | 69 | 69 |
| V-03 | PASS | PASS | vac | TBD | TBD | vac | vac | TBD | vac | vac | vac | TBD | TBD |
| V-04 | vac | vac | vac | vac | vac | vac | vac | vac | vac | vac | vac | 95 | 95 |
| V-05 | PASS | PASS | PASS | TBD | TBD | vac | vac | TBD | vac | vac | vac | TBD | TBD |

C-27, C-28, C-29 vacuous for all Round 1 variants.

### Round 2 Calibration (retroactive, v8 -> v9)

| Variant | C-27 | C-28 | C-29 | v8 | v9 |
|---------|------|------|------|----|----|
| V-01 | vac | vac | vac | 85 | 85 |
| V-02 | vac | vac | vac | 85 | 85 |
| V-03 | vac | vac | vac | 97 | 97 |
| V-04 | vac | vac | vac | 110 | 110 |

C-27, C-28, C-29 vacuous for all Round 2 variants.

### Round 4 Calibration (retroactive, v8 -> v9)

| Variant | C-27 | C-28 | C-29 | v8 | v9 |
|---------|------|------|------|----|----|
| V-01 | vac | vac | vac | 110 | 110 |
| V-02 | vac | vac | vac | 75 | 75 |
| V-03 | vac | vac | vac | 100 | 100 |
| V-04 | vac | vac | vac | 110 | 110 |
| V-05 | vac | vac | vac | 135 | 135 |

C-27, C-28, C-29 vacuous for all Round 4 variants.

### Round 5 Calibration (retroactive, v8 -> v9)

| Variant | C-27 | C-28 | C-29 | v8 | v9 |
|---------|------|------|------|----|----|
| V-01 | vac | vac | vac | 120 | 120 |
| V-02 | vac | vac | vac | 115 | 115 |
| V-03 | vac | vac | vac | 115 | 115 |
| V-04 | vac | vac | vac | 150 | 150 |
| V-05 | vac | vac | vac | 160 | 160 |

C-27, C-28, C-29 vacuous for all Round 5 variants.

### Round 6 Calibration (retroactive, v8 -> v9)

| Variant | C-27 | C-28 | C-29 | v8 | v9 |
|---------|------|------|------|----|----|
| V-01 | vac | vac | vac | 140 | 140 |
| V-02 | vac | vac | vac | 140 | 140 |
| V-03 | vac | vac | vac | 160 | 160 |
| V-04 | vac | vac | vac | 160 | 160 |
| V-05 | vac | vac | vac | 160 | 160 |

C-27, C-28, C-29 vacuous for all Round 6 variants.

### Round 7 Calibration (retroactive, v8 -> v9)

| Variant | C-27 | C-28 | C-29 | v8 | v9 |
|---------|------|------|------|----|----|
| V-01 | vac | vac | vac | 165 | **165** |
| V-02 | vac | vac | vac | 165 | **165** |
| V-03 | vac | vac | vac | 165 | **165** |
| V-04 | vac | vac | vac | 170 | **170** |
| V-05 | vac | vac | vac | 170 | **170** |

C-27, C-28, C-29 vacuous for all Round 7 variants. No CH-ID saturation contracts, null
hypothesis progression formulas, or scope coverage gate protocols appear before Round 9.

### Round 8 Calibration (retroactive, v8 -> v9)

| Variant | C-27 | C-28 | C-29 | v8 | v9 |
|---------|------|------|------|----|----|
| V-01 | vac | vac | vac | 170 | **170** |
| V-02 | vac | vac | vac | 170 | **170** |
| V-03 | vac | vac | vac | 170 | **170** |
| V-04 | vac | vac | vac | 175 | **175** |
| V-05 | vac | vac | vac | 180 | **180** |

C-27, C-28, C-29 vacuous for all Round 8 variants. V-05 R8 scores 180/180 under both v8
and v9 -- the three new criteria are strictly additive and do not retroactively alter R8 scores.

### Round 9 Calibration (v8 -> v9)

All 5 R9 variations carry the V-05 R8 template (§3a + exclusion registry + §7) as base.
All 5 score 180/180 under v8 before the new criteria are applied.

| Rank | Variant | C-27 | C-28 | C-29 | v8 | v9 |
|------|---------|------|------|------|----|----|
| 1 | **V-05** | PASS | PASS | PASS | 180 | **195** |
| 2 | **V-04** | PASS | PASS | FAIL | 180 | **190** |
| 3 | V-01 | PASS | FAIL | FAIL | 180 | **185** |
| 3 | V-02 | FAIL | PASS | FAIL | 180 | **185** |
| 3 | V-03 | FAIL | FAIL | PASS | 180 | **185** |

V-01: §8 CH-ID SATURATION REQUIREMENT present (C-27 PASS). No null hypothesis progression
contract (C-28 FAIL). No scope coverage gate (C-29 FAIL). Score: 180 + 5 = 185.
V-02: NULL HYPOTHESIS PROGRESSION CONTRACT present (C-28 PASS). No CH-ID saturation
contract (C-27 FAIL). No scope coverage gate (C-29 FAIL). Score: 180 + 5 = 185.
V-03: SCOPE COVERAGE GATE PROTOCOL present (C-29 PASS). No CH-ID saturation contract
(C-27 FAIL). No null hypothesis progression contract (C-28 FAIL). Score: 180 + 5 = 185.
V-04: CH-ID saturation + null hypothesis progression (C-27 + C-28 PASS). No scope coverage
gate (C-29 FAIL). Score: 180 + 5 + 5 = 190.
V-05: All three contracts present (C-27 + C-28 + C-29 PASS). Score: 180 + 5 + 5 + 5 = 195.

Round 9 top score: 195/195 (V-05 alone). Perfect under v9 requires C-27 + C-28 + C-29
simultaneously. V-04 holds two of three (190); V-01/V-02/V-03 hold one each (185); only V-05
holds all three. V-05 R9 is the canonical T3 target for v9.

**Key shift**: The three new criteria are independent in the same way C-24/C-25/C-26 were
independent -- each appears in at least one variant without the others, preventing any two from
being treated as a compound. Perfect requires all three simultaneously; none implies the others.

### Scoring Key

PASS = full points | PARTIAL = half points (round down) | FAIL = 0
C-11 vacuous (C-09 inactive) = 0, not partial.
C-16 vacuous (C-09 inactive) = 0, not partial.
C-19 vacuous (C-18 inactive) = 0, not partial.
C-20 vacuous (C-18 inactive) = 0, not partial.
C-21 vacuous (C-18 inactive) = 0, not partial.
C-22 vacuous (C-09 inactive) = 0, not partial.
C-23 vacuous (C-09 inactive OR two-option table) = 0, not partial.
C-24 vacuous (C-09 inactive OR no aggregation step) = 0, not partial.
C-25 vacuous (C-18 inactive OR no non-verdict section) = 0, not partial.
C-26 vacuous (C-09 inactive) = 0, not partial.
C-27 vacuous (C-09 inactive OR C-05 inactive) = 0, not partial.
C-28 vacuous (C-09 inactive) = 0, not partial.
C-29 vacuous (C-09 inactive OR no §1 scope enumeration) = 0, not partial.
