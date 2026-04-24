All checks pass. `org-review-rubric-v7-2026-03-16.md` is written — 898 lines, 50 KB.

---

**Summary of v7 changes:**

**Two new criteria extracted from Round 7 excellence signals:**

| ID | Name | Source | PASS | vac |
|----|------|--------|------|-----|
| C-24 | Domain-Aggregate Formula Pre-committed | V-04 R7 | V-04 | V-01/V-02/V-03 (no aggregation step); V-05 (§3.5 is checkpoint, not formula) |
| C-25 | Non-verdict Section Explicitly Excluded from Gate Ledger | V-05 R7 | V-05 | V-01/V-02/V-03/V-04 (no non-verdict section) |

**C-24 logic:** V-04 R7 pre-commits the DOMAIN-AGGREGATE FORMULA (median rule) in the preamble as a fifth contract. C-17 covers the three algebraic contracts; C-19 covers the ledger protocol; C-24 closes the last editorial gap — how domain verdicts are combined before the disposition formula runs.

**C-25 logic:** V-05 R7 explicitly marks §3.5 as "EXCLUDED: §3.5 emits NO ledger row" because §3.5 produces no verdict. Without this, C-21's "all sections emit" instruction is ambiguous for non-verdict sections. C-21 handles inclusion; C-25 handles explicit exclusion of exempt sections.

**Scale:** 15 → 17 aspirational criteria | 75 → 85 pts | Total: 165 → **175 pts** | Gold: 130 → **140**

**Round 7 top score:** 170/175. V-04 (C-24 PASS) and V-05 (C-25 PASS) tied. Perfect (175) requires both patterns simultaneously — no single R7 variant holds both.
eaning -- not
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

## Aspirational Criteria -- 85 pts (structural integrity, auditability, automation)

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

## Scoring Reference

### Composite Formula

```
essential_pts    = (essential_pass  / 5) * 60
recommended_pts  = (recommended_pass / 3) * 30
aspirational_pts =  aspirational_pass    *  5   # 5 pts each, max 85
composite = essential_pts + recommended_pts + aspirational_pts
```

**Maximum**: 60 + 30 + 85 = **175 pts**

### Score Bands

| Band | Condition | Composite |
|------|-----------|-----------|
| Gold | all 5 essential pass | >= 140 |
| Strong | all 5 essential pass | 90-139 |
| Partial | <= 4 essential pass | any |
| Minimal | <= 3 essential pass | any |

### Paths to Gold (140 pts)

| Path | Essential | Rec | Asp passed | Composite |
|------|-----------|-----|------------|-----------|
| Full rec + 10 asp | 5/5 | 3/3 | 10/17 | 60+30+50 = 140 |
| 2 rec + 12 asp | 5/5 | 2/3 | 12/17 | 60+20+60 = 140 |
| 1 rec + 14 asp | 5/5 | 1/3 | 14/17 | 60+10+70 = 140 |

### Round 1 Calibration (retroactive, v1 -> v7)

| Variant | C-09 | C-11 | C-16 | C-22 | C-23 | C-24 | C-25 | v6 | v7 |
|---------|------|------|------|------|------|------|------|----|----|
| V-01 | FAIL | vac | vac | vac | vac | vac | vac | 75 | 75 |
| V-02 | FAIL | vac | vac | vac | vac | vac | vac | 69 | 69 |
| V-03 | PASS | PASS | vac | TBD | TBD | vac | vac | TBD | TBD |
| V-04 | vac | vac | vac | vac | vac | vac | vac | 95 | 95 |
| V-05 | PASS | PASS | PASS | TBD | TBD | vac | vac | TBD | TBD |

Round 1 C-22/C-23 evidence not available for bracket-architecture variants.
C-24 and C-25 vacuous for all Round 1 variants.

### Round 2 Calibration (retroactive, v6 -> v7)

| Variant | C-24 | C-25 | v6 | v7 |
|---------|------|------|----|----|
| V-01 | vac | vac | 85 | 85 |
| V-02 | vac | vac | 85 | 85 |
| V-03 | vac | vac | 97 | 97 |
| V-04 | vac | vac | 110 | 110 |

C-24 and C-25 vacuous for all Round 2 variants.

### Round 4 Calibration (retroactive, v6 -> v7)

| Variant | C-24 | C-25 | v6 | v7 |
|---------|------|------|----|----|
| V-01 | vac | vac | 110 | 110 |
| V-02 | vac | vac | 75 | 75 |
| V-03 | vac | vac | 100 | 100 |
| V-04 | vac | vac | 110 | 110 |
| V-05 | vac | vac | 135 | 135 |

C-24 and C-25 vacuous for all Round 4 variants.

### Round 5 Calibration (retroactive, v6 -> v7)

| Variant | C-24 | C-25 | v6 | v7 |
|---------|------|------|----|----|
| V-01 | vac | vac | 120 | 120 |
| V-02 | vac | vac | 115 | 115 |
| V-03 | vac | vac | 115 | 115 |
| V-04 | vac | vac | 150 | 150 |
| V-05 | vac | vac | 160 | 160 |

C-24 and C-25 vacuous for all Round 5 variants.

### Round 6 Calibration (retroactive, v6 -> v7)

| Variant | C-24 | C-25 | v6 | v7 |
|---------|------|------|----|----|
| V-01 | vac | vac | 140 | 140 |
| V-02 | vac | vac | 140 | 140 |
| V-03 | vac | vac | 160 | 160 |
| V-04 | vac | vac | 160 | 160 |
| V-05 | vac | vac | 160 | 160 |

C-24 and C-25 vacuous for all Round 6 variants. No domain-aggregate formula or non-verdict
section architectures appear until Round 7.

### Round 7 Calibration (v6 -> v7)

| Variant | C-24 | C-25 | v6 | v7 |
|---------|------|------|----|----|
| V-01 | vac | vac | 165 | **165** |
| V-02 | vac | vac | 165 | **165** |
| V-03 | vac | vac | 165 | **165** |
| V-04 | PASS | vac | 165 | **170** |
| V-05 | vac | PASS | 165 | **170** |

V-01/V-02/V-03: no domain-aggregate formula or non-verdict section; C-24 and C-25 vacuous.
Score unchanged at 165.
V-04: DOMAIN-AGGREGATE FORMULA (median rule) pre-committed in preamble as part of fourth
contract; bracket closing §5 applies formula mechanically. C-24 PASS (+5). No §3.5-type
non-verdict section in V-04 architecture. C-25 vacuous.
V-05: §3.5 Domain-Aggregate Checkpoint present but produces no verdict; gate ledger protocol
explicitly marks "EXCLUDED: §3.5 emits NO ledger row". C-25 PASS (+5). §3.5 is a checkpoint
not an aggregation formula application; no pre-committed domain-aggregate formula present.
C-24 vacuous.

Round 7 top score: 170/175. V-04 and V-05 tied. Perfect (175) not yet achieved.
Perfect requires C-24 PASS (V-04 architecture with pre-committed domain-aggregate formula) AND
C-25 PASS (V-05 architecture with explicit non-verdict section exclusion) simultaneously --
no single R7 variant holds both.

### Scoring Key

PASS = full points | PARTIAL = half points (round down) | FAIL = 0
C-11 vacuous (C-09 inactive) = 0, not partial.
C-16 vacuous (C-09 inactive) = 0, not partial.
C-19 vacuous (C-18 inactive) = 0, not partial.
C-20 vacuous (C-18 inactive) = 0, not partial.
C-21 vacuous (C-18 inactive) = 0, not partial.
C-22 vacuous (C-09 inactive) = 0, not partial.
C-23 vacuous (C-09 inactive OR two-option table) = 0, not partial.
C-24 vacuous (C-09 inactive OR no multi-domain aggregation step) = 0, not partial.
C-25 vacuous (C-18 inactive OR no non-verdict intermediate section) = 0, not partial.

---

## Criterion Summary

| ID | Criterion | Weight | Category | Pts |
|----|-----------|--------|----------|-----|
| C-01 | Role Matrix Coverage | essential | correctness | 12 |
| C-02 | Severity Carries Commit-Gate Semantics | essential | correctness | 12 |
| C-03 | Null Hypothesis Gate Before Domain Testimony | essential | correctness | 12 |
| C-04 | Commitment Disposition Emitted | essential | behavior | 12 |
| C-05 | Action Items Traceable to Findings | essential | behavior | 12 |
| C-06 | Artifact Scope Declared Before Review Begins | recommended | coverage | 10 |
| C-07 | Summary with Integrating Narrative | recommended | depth | 10 |
| C-08 | Depth Parameter Honored | recommended | behavior | 10 |
| C-09 | Adversarial Bracket Architecture | aspirational | depth | 5 |
| C-10 | Disposition Algebra Committed Before Execution | aspirational | correctness | 5 |
| C-11 | Override Decision Emitted as Labeled Field | aspirational | auditability | 5 |
| C-12 | Action Item Class Derived Mechanically from Gate Verdicts | aspirational | correctness | 5 |
| C-13 | Prompt Inputs as Template Variables | aspirational | automation | 5 |
| C-14 | Gate Verdict Preserved in Action Register | aspirational | auditability | 5 |
| C-15 | Reviewer Set as Injectable Template Parameter | aspirational | automation | 5 |
| C-16 | Alternatives Table as Adversarial Bracket Anchor | aspirational | auditability | 5 |
| C-17 | Pre-commitment Cascade: All Three Contracts in Preamble | aspirational | correctness | 5 |
| C-18 | Inline Gate Ledger at Origin | aspirational | auditability | 5 |
| C-19 | Gate Ledger Protocol as Pre-committed Fourth Contract | aspirational | correctness | 5 |
| C-20 | Verbatim Assembly Prohibition on Re-derivation | aspirational | auditability | 5 |
| C-21 | Universal Gate Ledger Coverage | aspirational | auditability | 5 |
| C-22 | Lifecycle Verdict Integration at Bracket Closing | aspirational | depth | 5 |
| C-23 | Multi-alternative Null Hypothesis Coverage | aspirational | correctness | 5 |
| C-24 | Domain-Aggregate Formula Pre-committed | aspirational | correctness | 5 |
| C-25 | Non-verdict Section Explicitly Excluded from Gate Ledger | aspirational | auditability | 5 |

---

## Design Notes

The essential criteria map directly to what makes an org-review output useful vs useless:
- Without C-01 (role matrix), it is a monologue, not a review.
- Without C-02 (severity semantics), severity labels are decoration.
- Without C-03 (null hypothesis gate), the review cannot answer should we build this?
- Without C-04 (disposition), the review produces no actionable signal.
- Without C-05 (traceable action items), findings do not translate to next steps.

C-06--C-08 lift quality without making the output useless if absent.

C-09/C-10 are the structural mechanisms that prevent post-hoc rationalization -- the distinction
between a review that finds the truth and one that confirms a prior belief.

**C-11/C-12/C-13 are the Round 1 extraction** -- patterns that separated V-05 (95 pts) and
V-04 (90 pts) from the field:
- C-11: Did the challenger actually override, or did we just get lucky with BLOCKED?
- C-12: Was BLOCKED actually forced by the gate, or did the AI soften it at synthesis?
- C-13: Can this prompt be run programmatically, or must a human interpret it?

**C-14/C-15 are the Round 2 extraction** -- patterns that separated V-04 (100 pts) from the
field and identified the next tier of auditability and automation:
- C-14: Can you verify the derivation row by row without re-reading reviewer narrative? Gate
  verdict in the action register is the missing link between C-12's derivation rule (preamble)
  and the action class (register). Without C-14, C-12 can be nominally satisfied while the AI
  assigns classes inconsistently.
- C-15: Is reviewer selection part of the automation contract, or still editorial at call time?
  C-13 parameterized content; C-15 parameterizes reviewer configuration.

**C-16/C-17/C-18 are the Round 4 extraction** -- patterns that explain why V-05 scored 125/125
under v3 and what the next tier requires:
- C-16: Is the bracket override mechanically auditable, or does it still require narrative
  re-reading? The Alternatives Table is the first mechanism that makes the bracket override
  decision derivable from structured data without reading prose.
- C-17: Are all three pre-commitment contracts present, or does one remain editorial? C-10 and
  C-12 are parallel contracts; the null hypothesis derivation rule is the third. A prompt with
  C-10 + C-12 but no pre-committed g_null mapping is still partially editorial.
- C-18: Where does the gate verdict first appear -- at origin or at consolidation? C-14 ensures
  the verdict is in the register (destination); C-18 ensures it is also emitted at the reviewer
  section (source). The two form a complete chain of custody.

**C-19/C-20/C-21 are the Round 5 extraction** -- patterns that explain why V-04 and V-05 both
saturated v4 (140/140) and what the next tier requires:
- C-19: Is the local gate ledger protocol itself pre-committed, or is the format decided
  editorially at execution time? C-17 pre-commits the algebraic contracts; C-19 extends
  pre-commitment discipline to the procedural assembly contract. Without C-19, local ledger
  row format can vary across sections, breaking cross-section comparability.
- C-20: Does the master register assembly instruction protect local verdicts from silent
  correction? C-18 establishes local emission as the point of authority. C-20 ensures that
  authority holds during assembly. Without the verbatim-copy + no-re-derive instruction, the
  AI can introduce errors at consolidation that are invisible in the local ledger.
- C-21: Does chain-of-custody extend to all reviewer archetypes, or only bracket and domain
  roles? V-04 passes C-18 with bracket + domain coverage; V-05 extends it to the lifecycle
  reviewer. A lifecycle verdict that enters the master register without local emission has no
  source tracing -- classification errors are introduced silently.

**C-22/C-23 are the Round 6 extraction** -- patterns that explain why V-03, V-04, and V-05
saturated v5 (155/155) and what Perfect under v6 requires:
- C-22: Does the bracket closing integrate lifecycle evidence, or is its null hypothesis
  reassessment incomplete? V-04 R6 is the first architecture to sequence lifecycle before bracket
  closing, giving the challenger direct access to g_lifecycle when deciding whether domain +
  lifecycle evidence together defeat the null hypothesis. V-03 and V-05 sequence bracket closing
  before lifecycle, so their challengers operate with incomplete signal. A bracket closing that
  has seen both domain and lifecycle verdicts makes a strictly richer override decision.
- C-23: When three or more alternatives exist, does the null hypothesis derivation rule cover all
  of them? V-03 and V-05 use a two-differential rule (Build vs Status Quo AND Build vs Hybrid),
  preventing the null hypothesis from being defeated by choosing only the weakest comparator.
  V-04 uses a two-alternative table and is therefore exempt. Perfect under v6 requires both: the
  three-alternative table design (C-23) AND the lifecycle-before-bracket-closing ordering (C-22)
  -- the two patterns seen separately in V-04 (C-22) and V-03/V-05 (C-23) must be combined.

**C-24/C-25 are the Round 7 extraction** -- patterns that explain why all five R7 variants
saturated v6 (165/165) and what Perfect under v7 requires:
- C-24: When multiple domain reviewers contribute verdicts, is the aggregation method
  pre-committed or editorial? V-04 R7 introduces the DOMAIN-AGGREGATE FORMULA (median rule) as
  a pre-committed contract in the preamble, making bracket closing a mechanical formula
  application rather than an editorial aggregation choice. C-17 pre-commits the three algebraic
  contracts; C-24 extends pre-commitment discipline to the domain aggregation step that feeds
  into those formulas. Without C-24, a prompt satisfying C-17 still allows editorial variance at
  the final aggregation step.
- C-25: When the review architecture includes non-verdict intermediate sections (checkpoints,
  synthesis passes that produce no gate verdict), does the gate ledger protocol explicitly name
  them as excluded? V-05 R7 introduces §3.5 Domain-Aggregate Checkpoint with an explicit
  "EXCLUDED: §3.5 emits NO ledger row" declaration. Without this, C-21's "universal coverage"
  instruction is ambiguous for non-verdict sections -- the AI must decide at execution time
  whether a given section should emit a ledger row. Explicit exclusion eliminates that editorial
  decision point. Perfect under v7 requires both: V-04's domain-aggregate formula (C-24) AND
  V-05's non-verdict exclusion declaration (C-25) -- no single R7 variant holds both.

**Dependency structure:**
- C-11 depends on C-09 (vacuous if C-09 fails).
- C-16 depends on C-09 (vacuous if C-09 fails).
- C-22 depends on C-09 (vacuous if C-09 fails).
- C-23 depends on C-09 (vacuous if C-09 fails) AND on a three-or-more alternative table
  (vacuous if table has only two options).
- C-24 depends on C-09 (vacuous if C-09 fails) AND on a multi-domain aggregation step
  (vacuous if domain verdicts enter disposition formula directly without aggregation layer).
- C-12 is independent but synergistic with C-10.
- C-13 is independent; operates at the prompt-template level.
- C-14 is synergistic with C-12: rule (C-12) + evidence to audit it (C-14).
- C-15 is synergistic with C-13: content params (C-13) + reviewer params (C-15).
- C-17 subsumes C-10 and C-12 requirements: if C-17 passes, C-10 and C-12 necessarily pass.
  If C-10 or C-12 fail, C-17 fails. C-17 adds the null hypothesis derivation rule as the
  third contract.
- C-18 requires C-14 to pass: local emission without register copy does not satisfy C-18.
  C-14 can pass independently (consolidated verdict, no local emission).
- C-19 depends on C-18 (vacuous if C-18 fails): protocol pre-commitment is only evaluable
  when the inline gate ledger is actually in use.
- C-20 depends on C-18 (vacuous if C-18 fails): assembly prohibition only evaluable when
  local rows exist to be assembled.
- C-21 depends on C-18 (vacuous if C-18 fails): coverage across archetypes only evaluable
  when inline gate ledger emission is occurring.
- C-25 depends on C-18 (vacuous if C-18 fails): non-verdict exclusion only evaluable when
  the gate ledger protocol is in use. Also vacuous if no non-verdict section exists.
- C-19 is synergistic with C-17: C-17 pre-commits algebraic contracts; C-19 pre-commits
  the procedural contract. Together they form a complete pre-commitment envelope.
- C-22 is synergistic with C-21: C-21 requires lifecycle to emit a local gate ledger row;
  C-22 requires bracket closing to receive and reference that verdict. Together they form a
  complete lifecycle signal path: emission (C-21) -> integration (C-22).
- C-23 is synergistic with C-17: C-17 requires a pre-committed derivation formula; C-23
  requires that formula to cover multi-alternative comparisons when three+ options exist.
- C-24 is synergistic with C-17: C-17 requires algebraic pre-commitment contracts; C-24
  requires the aggregation formula that feeds those contracts to also be pre-committed.
- C-25 is synergistic with C-21: C-21 requires all verdict-emitting sections to emit rows;
  C-25 requires non-verdict sections to be explicitly excluded. Together they define the
  complete emission boundary: include all (C-21) + exclude named exceptions (C-25).

**Scale history:**
- v1: C-01--C-10. Aspirational: 2 criteria (10 pts). Total: 100. Gold: 80.
- v2: adds C-11, C-12, C-13. Aspirational: 5 criteria (25 pts). Total: 115. Gold: 90.
- v3: adds C-14, C-15. Aspirational: 7 criteria (35 pts). Total: 125. Gold: 100.
  V-04 R2 retroactively scores 110/125, clearing Gold with 10 pts headroom.
- v4: adds C-16, C-17, C-18. Aspirational: 10 criteria (50 pts). Total: 140. Gold: 110.
  V-05 R4 retroactively scores 135/140. Perfect (140) not yet achieved.
  V-04 and V-05 R5 both achieve Perfect (140/140) -- Round 5 saturates v4.
- v5: adds C-19, C-20, C-21. Aspirational: 13 criteria (65 pts). Total: 155. Gold: 120.
  V-05 R5 scores 155/155 -- first Perfect across all rounds.
  V-04 R5 scores 150/155 -- fails only C-21 (lifecycle reviewer excluded from ledger).
  V-03/V-04/V-05 R6 all score 155/155 -- Round 6 saturates v5 for three variants.
- v6: adds C-22, C-23. Aspirational: 15 criteria (75 pts). Total: 165. Gold: 130.
  V-03/V-04/V-05 R6 score 160/165. Perfect (165) not yet achieved.
  V-01--V-05 R7 all score 165/165 -- Round 7 saturates v6 for all variants.
- v7: adds C-24, C-25. Aspirational: 17 criteria (85 pts). Total: 175. Gold: 140.
  V-04 R7 scores 170/175 (C-24 PASS). V-05 R7 scores 170/175 (C-25 PASS).
  Perfect (175) not yet achieved. Perfect requires C-24 PASS (domain-aggregate formula
  pre-committed) AND C-25 PASS (non-verdict section explicitly excluded) simultaneously.
