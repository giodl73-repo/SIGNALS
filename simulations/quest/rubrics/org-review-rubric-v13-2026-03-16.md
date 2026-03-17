All the numbers are correct. Written to `simulations/quest/rubrics/org-review-rubric-v13-2026-03-16.md`.

---

**v13 changes summary:**

**New criterion — C-39: NH Dimension Table Column Aggregation Formula Pre-committed**

Extracted from V-05 R14. V-01 and V-04 both achieved C-38 PASS (three-column NH table) and C-23 PASS, but left the column value computation editorial at bracket closing time. V-05 added an explicit NH TABLE AGGREGATION RULE specifying:
- Column A = challenger's opening value carried forward (control arm, unchanged)
- Column B = average of domain reviewer scores for the proposed-state dimension
- Column C = average of domain reviewer scores for the best-non-build-alt dimension

This eliminates the last editorial step inside C-37's re-population contract.

**Vacuous condition:** C-37 inactive OR C-38 inactive (both must be active).

**Score changes:**
- Aspirational: 30 → 31
- Max: 240 → 245
- Gold threshold: 205 → 210

**R14 ranking under v13:**

| Rank | Variant | Score |
|------|---------|-------|
| 1 | V-05 R14 | **245/245** (first perfect score) |
| 2 | V-01/V-04 R14 | 240/245 |
| 4 | V-02 R14 | 235/245 |
| 5 | V-03 R14 | 230/245 |
erentiating criteria satisfied simultaneously for the first time.

**R14 score computation (baseline = V-05 R13 under v12 = 230):**

| Variant | C-23 | C-38 | C-39 | Delta | v13 Score |
|---------|------|------|------|-------|-----------|
| **V-05** | PASS (+5) | PASS (+5) | PASS (+5) | +15 | **245/245** |
| **V-01** | PASS (+5) | PASS (+5) | FAIL (0) | +10 | **240/245** |
| **V-04** | PASS (+5) | PASS (+5) | FAIL (0) | +10 | **240/245** |
| **V-02** | PASS (+5) | FAIL (0) | vac (0) | +5 | **235/245** |
| **V-03** | FAIL (0) | FAIL (0) | vac (0) | 0 | **230/245** |

Gold delta matches the 5 pt pattern for a single-criterion increment. 205->210.

**C-39 vacuous condition:** C-37 not active OR C-38 not active. Without bracket closing re-population (C-37) or without a three-column NH table structure (C-38), there is no per-column derivation to specify.

**C-23 notes (R14):**
- V-01/V-04/V-05: Three-column NH table yields D1=(B-A) and D2=(B-C) as table columns; NULL HYPOTHESIS DERIVATION RULE names BOTH differentials; "BOTH D1 AND D2 required for DEFEATED." PASS.
- V-02: §17 derivation rule maps D1_net (from NH table) and D2_net (from alternatives table scalar) to HOLDS/CONDITIONAL/DEFEATED as a formula. Both differentials named. PASS. (C-38 FAIL: D2 not NH-table-derivable.)
- V-03: §17 names only D1 from the two-column NH table; D2 absent. FAIL.

**C-38 notes (R14):**
- V-01/V-04/V-05: NH dimension table has Status-Quo (A), Proposed-Build (B), Best-Non-Build-Alt (C) columns; per-dimension D1=(B-A) and D2=(B-C) present; derivation rule references both. PASS.
- V-02: NH table two-column only; D2 sourced from alternatives table scalar, not NH table. FAIL.
- V-03: Two-column NH table; Best-Non-Build-Alt column absent. FAIL.

**C-39 notes (R14):**
- V-05: §17 NH TABLE AGGREGATION RULE: Column A = challenger's original opening value (carried forward); Column B = average of domain reviewer scores for Proposed-Build dimension; Column C = average of domain reviewer scores for Best-Non-Build-Alt dimension. Per-column formula pre-committed. PASS.
- V-01/V-04: §17 pre-commits re-population of three-column table (C-37/C-38 PASS) but no per-column derivation formula. AI selects aggregation method at bracket closing time. FAIL.
- V-02/V-03: C-38 FAIL -> C-39 vacuous.

No retroactive score changes on R1--R13. R13 v12 scores carry forward unchanged.

---

## Essential Criteria -- 60 pts (review is wrong without these)

### C-01 -- Multi-voice Role Architecture
**Weight**: essential | **Points**: 12 | **Category**: depth

Review is structured as a matrix of named roles, each applying a distinct evaluation frame
to the artifact. At minimum, one adversarial/challenger role (the inertia-advocate: argues for
not proceeding, surfaces why the status quo is acceptable) and at least one domain role must be
present. Domain reviewers apply their own frame independently -- findings are not aggregated or
merged across roles at collection time. Each reviewer section evaluates the artifact from that
reviewer's frame and carries its own severity labels. The review is multi-voice; without an
adversarial role, it cannot evaluate whether proceeding is correct, only whether the artifact
implements its premise. No reviewer section is empty or identical to another.

**Pass condition**: output contains a named challenger role and >= 1 domain role. Each role
section applies its own frame to the artifact; findings are not aggregated across roles.

**Fails if**: findings are aggregated across roles, severity labels are absent from any role
section, or no adversarial/challenger role is present.

---

### C-02 -- Severity Carries Commit-Gate Semantics
**Weight**: essential | **Points**: 12 | **Category**: correctness

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

## Aspirational Criteria -- 155 pts (structural integrity, auditability, automation)

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
automatically makes C-20 vacuous.

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
(not narratively).

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
conformance (C-22).

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
is the cross-section output coverage requirement.

**Pass condition**: a CH-ID SATURATION REQUIREMENT block appears in the preamble defining the
SATURATED and FULLY SATURATED tiers. A dedicated CH-ID SATURATION CHECK section (or equivalent)
runs after domain sections and before LIFECYCLE. BRACKET CLOSING includes a saturation table and
an explicit prohibition on PASS when any CH-ID is UNSATURATED without waiver. The requirement is
pre-committed, not generated at execution time.

**Vacuous case**: C-09 not active OR C-05 not active (no CH-ID tracing architecture) -- this
criterion scores 0 (not partial, not fail).

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
chain.

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

**Distinction from CROSS-ROLE SIGNALS scope coverage field**: C-29 captures the contractual
pre-commitment: a dedicated post-bracket-closing section with a mechanical coverage formula,
forced advisory assignment for GAP surfaces, explicit exclusion from the gate ledger, and §1
annotation at scope enumeration time.

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
or GAP surfaces are not forced to ADVISORY-GAP status; or the section emits a gate ledger row.
Partial if a dedicated §5.5 section exists but the pre-commitment is absent from the preamble,
or the §1 annotation is missing.

---

### C-30 -- Per-Finding Severity Chain Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-01, V-04, V-05 Round 11 -- §14 [IMMUTABLE] pre-commits individual Severity column
on every finding row; Section Severity derives mechanically as worst(F-1, F-2, ...) over all
finding severities in that section; eliminates editorial section-level severity assignment;
creates full auditability chain: individual finding -> individual severity -> aggregation formula
-> Section Severity signal; absent in V-02 and V-03

Each finding row in every reviewer section carries an individual Severity field. The Section
Severity -- reported in the gate ledger row and referenced in the action register -- is
pre-committed to derive mechanically as the worst-case over all individual finding severities in
that section (e.g., `Section Severity = worst(F-1, F-2, ...)` for all finding rows F-n). The
derivation formula is stated as an immutable contract (e.g., §14 [IMMUTABLE]) in the preamble
before any reviewer section executes. No editorial assignment of section-level severity is
permitted after findings are stated: the section severity is derived, not chosen.

**Distinction from C-02**: C-02 requires severity labels to carry explicit commit-gate semantics
(HIGH/MEDIUM/LOW mapped to block/condition/proceed). C-30 adds the structural pre-commitment:
individual finding severities are declared per-row, and the Section Severity is their mechanical
aggregate. C-02 defines what the labels mean; C-30 defines how they propagate from individual
finding to section signal.

**Distinction from C-12**: C-12 pre-commits the gate-verdict-to-action-item-class derivation
rule. C-30 pre-commits the finding-severity-to-section-severity aggregation formula. Both are
mechanical derivations; they operate at different layers of the output structure.

**Pass condition**: a per-finding severity aggregation formula appears in the preamble as an
immutable contract before any reviewer section executes. Every finding row in every reviewer
section carries an individual Severity field. The Section Severity in each gate ledger row is
consistent with worst(individual finding severities in that section). No section-level severity
is assigned editorially outside this formula.

**Vacuous case**: C-02 not active (no severity labels in use) -- this criterion scores 0 (not
partial, not fail). Without severity labels there are no individual severities to aggregate.

**Fails if** (C-02 active): section-level severity is assigned editorially without an
individual-finding-severity aggregation contract; or finding rows do not carry individual
Severity fields; or the aggregation formula is not pre-committed in the preamble. Partial if
individual finding severities are present but the worst-case aggregation formula is not
pre-committed (section severity assigned as a named value rather than derived).

---

### C-31 -- Role Lens Exhaustion Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-02, V-04, V-05 Round 11 -- §15 [IMMUTABLE] pre-commits LENS COVERAGE TABLE
requiring ALL lens.verify entries from each role definition to appear with ADDRESSED or OPEN
status; OPEN entries automatically surface as ADVISORY-OPEN-LENS items in ACTION ITEM REGISTER;
role-capability completeness enforced at expertise-coverage time; absent in V-01 and V-03

A LENS COVERAGE TABLE is pre-committed in the preamble: for each active reviewer role, ALL
`lens.verify` entries listed in that role's definition must appear in the table with status
ADDRESSED (a finding references this lens dimension) or OPEN (no finding referenced this lens
dimension). The pre-commitment contract (e.g., §15 [IMMUTABLE]) specifies that OPEN entries are
automatically promoted to ADVISORY-OPEN-LENS items in the ACTION ITEM REGISTER. The table is
produced at expertise-coverage time -- after all reviewer sections have executed but before
DISPOSITION -- enabling the Bracket Closing to factor unexplored lens dimensions into the
override decision.

**Distinction from C-27**: C-27 tracks cross-section saturation of CH-IDs (challenge
identifiers) that must receive responses from domain and lifecycle sections. C-31 tracks
exhaustion of role-specific `lens.verify` dimensions that every reviewer is expected to consult.
C-27 is a response-coverage contract over challenge identifiers; C-31 is a capability-coverage
contract over reviewer lens dimensions. The two source sets are independent.

**Distinction from C-29**: C-29 requires post-bracket-closing reconciliation of declared §1
scope surfaces to reviewer findings (scope-to-finding coverage). C-31 requires at-review-time
reconciliation of declared role lens dimensions to findings (role-capability-to-finding
coverage). C-29 operates on the artifact scope inventory; C-31 operates on the reviewer
competency inventory.

**Pass condition**: a LENS COVERAGE TABLE protocol appears in the preamble (or equivalent
pre-commitment block) naming the requirement that all `lens.verify` entries from each active
role appear in the table with ADDRESSED or OPEN status. The table is populated after all
reviewer sections complete and before DISPOSITION. OPEN entries appear as ADVISORY-OPEN-LENS
action items in the ACTION ITEM REGISTER. The protocol is pre-committed before any reviewer
section executes.

**Vacuous case**: C-09 not active OR role definitions contain no `lens.verify` entries -- this
criterion scores 0 (not partial, not fail). Without role-defined lens dimensions there is no
lens exhaustion requirement to enforce.

**Fails if** (C-09 active, lens.verify entries present): no LENS COVERAGE TABLE exists; or lens
entries appear but without ADDRESSED/OPEN classification; or OPEN entries are not promoted to
ADVISORY-OPEN-LENS action items; or the protocol is not pre-committed in the preamble. Partial
if a LENS COVERAGE TABLE is produced but only for some roles, or OPEN entries are noted but not
formally registered as action items.

---

### C-32 -- Primary Driver Derivation Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-03, V-05 Round 11 -- §16 [IMMUTABLE] pre-commits a 9-rule precedence formula over
the gate verdict vector that mechanically selects a single gate as the Primary Driver of the
DISPOSITION at synthesis time; eliminates the last remaining editorial step after all gate
verdicts are known; disposition attribution auditable from gate verdict values alone without
reading reviewer narrative; absent in V-01, V-02, V-04

A PRIMARY DRIVER DERIVATION CONTRACT is pre-committed in the preamble specifying a rule-ordered
precedence formula over the full gate verdict vector. After all gate verdicts are known, the
formula applies the rules in order to select exactly one gate as the Primary Driver of the
DISPOSITION. The formula eliminates the last remaining editorial step at synthesis time: the
evaluator does not choose which gate "most influenced" the disposition -- the formula derives it
mechanically. The Primary Driver attribution is emitted as a labeled field at DISPOSITION time
and is auditable from gate verdict values alone without reading reviewer narrative.

**Distinction from C-10 / C-17 (DISPOSITION ALGEBRA / CASCADE)**: C-10 and C-17 pre-commit the
formula that maps gate verdicts to the DISPOSITION categorical outcome (READY / CONDITIONAL /
BLOCKED). C-32 pre-commits the formula that maps gate verdicts to a single-gate attribution (the
Primary Driver). The DISPOSITION ALGEBRA answers "what is the outcome?"; C-32 answers "which
gate caused it?". Both are mechanical derivations from the same gate verdict vector; C-32 adds
an attribution layer absent from C-10 and C-17.

**Distinction from C-12**: C-12 pre-commits gate-verdict-to-action-item-class derivation (what
class does each action item receive?). C-32 pre-commits gate-verdict-to-primary-driver
attribution (which gate most caused the disposition?). Different target, same layer of
mechanical pre-commitment.

**Pass condition**: a PRIMARY DRIVER DERIVATION CONTRACT (or equivalent) appears in the preamble
before any reviewer section executes. The contract names an ordered rule set (>= 3 rules in a
defined precedence order) covering all gate verdict combinations and selecting exactly one gate
as Primary Driver per combination. A labeled Primary Driver field is emitted at DISPOSITION time
with a value derivable from the gate verdict vector without reading reviewer narrative. The
Primary Driver is consistent with the pre-committed rule set applied to the actual gate verdicts.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). Without
bracket architecture there is no multi-gate verdict vector to derive a primary driver from.
C-09 FAIL automatically makes C-32 vacuous.

**Fails if** (C-09 active): no Primary Driver attribution is emitted at DISPOSITION; or
attribution is assigned editorially without a pre-committed rule formula; or the formula is
stated post-hoc after reviewers execute. Partial if a Primary Driver field is emitted but the
derivation formula is not pre-committed in the preamble, or the rule set does not cover all gate
verdict combinations.

---

### C-33 -- Lens Applicability Rating Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-02 Round 12 -- role lens inventory table declares a per-entry applicability rating
(HIGH / MEDIUM / LOW) for each role's lens dimensions relative to the specific artifact under
review; the applicability tier is the structural basis for the ADDRESSED/OPEN determination in
the LENS COVERAGE TABLE; first variant where C-31's coverage table includes a mechanically
interpretable artifact-specific applicability rating rather than implicit generic capability
assumptions; absent in V-01 and V-03

Each entry in the LENS COVERAGE TABLE (C-31) carries an explicit applicability rating (HIGH /
MEDIUM / LOW) for the role's lens dimension relative to the specific artifact under review -- not
a generic capability rating attached to the role definition. The applicability rating is
pre-committed as the basis for the ADDRESSED/OPEN determination: a HIGH-applicability lens
dimension is held to full ADDRESSED/OPEN coverage; lower-applicability lens dimensions may carry
a pre-stated reduced coverage expectation. The rating is artifact-specific: the same role in a
different review may carry a different applicability rating if the artifact type differs.

**Distinction from C-31**: C-31 requires the LENS COVERAGE TABLE to be present with
ADDRESSED/OPEN classification for each lens.verify entry. C-33 requires the underlying
applicability rating that grounds the ADDRESSED/OPEN decision -- the per-lens evidence of why
coverage is expected at all. C-31 can pass while C-33 fails when the table classifies lenses as
ADDRESSED/OPEN without stating the applicability basis for those classifications. With C-33, the
ADDRESSED/OPEN determination is a derived function of the applicability rating; without it, the
classification is an editorial judgment at table-population time.

**Pass condition**: each row in the LENS COVERAGE TABLE includes an explicit applicability rating
(HIGH / MEDIUM / LOW or equivalent tiered scale) specific to the artifact under review. The
preamble or table header states that applicability ratings determine coverage expectations (e.g.,
HIGH-applicability lenses must be ADDRESSED; LOW-applicability lenses may remain OPEN without
penalty). The rating is not inferred from generic role definitions.

**Vacuous case**: C-31 not active -- this criterion scores 0 (not partial, not fail). Without a
LENS COVERAGE TABLE there are no rows to carry applicability ratings.

**Fails if** (C-31 active): the LENS COVERAGE TABLE has ADDRESSED/OPEN classifications but no
per-lens applicability ratings; or applicability is described generically in role definitions
without a per-artifact rating in the table. Partial if some lens entries carry applicability
ratings but others do not, or if a single applicability level is applied to all lenses without
differentiation.

---

### C-34 -- ADVISORY-GAP Domain Coverage Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-02 Round 12 -- gap-check section "Which artifact domains have no HIGH-applicability
role?" identifies uncovered artifact domains and classifies each as ADVISORY-GAP in the action
register; produces a domain-level coverage map orthogonal to per-role lens exhaustion (C-31) and
per-surface scope reconciliation (C-29); first variant where artifact-domain coverage by reviewer
applicability tier is a pre-committed check with forced ADVISORY-GAP promotion for uncovered
domains; absent in V-01 and V-03

A DOMAIN COVERAGE GAP-CHECK protocol is pre-committed in the preamble: after the LENS COVERAGE
TABLE is populated (C-31), a dedicated gap-check step identifies every artifact domain that has
no reviewer with HIGH applicability to it. Each uncovered domain is classified as ADVISORY-GAP
and promoted to the ACTION ITEM REGISTER. The ADVISORY-GAP item records the uncovered domain
name and the reason no HIGH-applicability reviewer covers it (absent role, OPEN lens, or
LOW/MEDIUM applicability only). The classification is an action class, not merely an observation
note. The gap-check is pre-committed in the preamble; it does not run editorially at review time.

**Distinction from C-31**: C-31 tracks whether each role's lens.verify dimensions were ADDRESSED
or OPEN in the review (per-role capability exhaustion -- did the reviewer use every lens they
have?). C-34 tracks whether each artifact domain has at least one HIGH-applicability reviewer
covering it (per-domain reviewer coverage -- does the domain have an expert?). A domain may have
all roles marking the relevant lens as ADDRESSED while no role has HIGH applicability to that
domain -- C-31 passes while C-34 fails. The two checks are orthogonal: C-31 is role-outward
(did the reviewer exhaust their lenses?); C-34 is domain-inward (does the domain have an expert
reviewer?).

**Distinction from C-29**: C-29 maps §1 IN-SCOPE surfaces to reviewer findings post-bracket-
closing (scope-to-finding coverage). C-34 maps artifact domains to reviewer applicability tiers
during the LENS COVERAGE TABLE phase (domain-to-reviewer coverage). C-29 checks whether findings
exist for declared surfaces; C-34 checks whether HIGH-applicability reviewers exist for each
domain. Different phase, different source mapping, different classification output.

**Pass condition**: a domain coverage gap-check is pre-committed in the preamble as a step
following the LENS COVERAGE TABLE. The gap-check identifies artifact domains with no
HIGH-applicability reviewer and classifies each as ADVISORY-GAP. ADVISORY-GAP items appear in
the ACTION ITEM REGISTER naming the uncovered domain and the reason for the gap. The protocol
is declared before any reviewer section executes.

**Vacuous case**: C-31 not active (no lens applicability rating framework) -- this criterion
scores 0 (not partial, not fail). Without applicability ratings there is no HIGH-applicability
tier to check against. C-31 FAIL automatically makes C-34 vacuous.

**Fails if** (C-31 active): the coverage table identifies OPEN lenses but never checks whether
any artifact domain is uncovered at the HIGH-applicability tier; or uncovered domains are noted
in prose without ADVISORY-GAP classification or action register promotion; or the gap-check is
not pre-committed (run editorially at review time). Partial if a gap-check section runs but
uncovered domains are not classified as ADVISORY-GAP or not promoted to the action register.

---

### C-35 -- Null Hypothesis Challenger Dimension Comparison Table
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-02 Round 12 -- challenger uses a structured dimension comparison table contrasting
current-state vs. proposed-state per dimension with explicit per-dimension ratings or scores;
makes null hypothesis evaluation machine-readable and auditable from table values without reading
prose; first variant where the challenger's null hypothesis comparison is a structured table
rather than prose testimony; absent in V-01 and V-03

The challenger's null hypothesis evaluation uses a structured dimension comparison table with a
defined column set (>= 2 dimensions, current-state score or rating and proposed-state score or
rating per dimension, and a per-dimension differential or verdict). The table is populated before
domain reviewer sections run. The null hypothesis verdict (g_null, from C-17/C-28) is derivable
from the table differentials -- a scorer can verify the g_null value from table data alone
without reading the challenger's prose argument.

**Distinction from C-03**: C-03 requires a null hypothesis statement and verdict before domain
testimony (a gate presence requirement). C-35 requires the challenger's evaluation to use a
structured comparison table. A review can pass C-03 with prose null hypothesis testimony; C-35
additionally requires the table format. C-03 is a gate presence requirement; C-35 is a
structural format requirement for how that gate is evaluated.

**Distinction from C-16**: C-16 requires the adversarial bracket to use a quantified
multi-dimension table as a shared structural anchor -- populated by the Bracket Opening,
re-scored by domain reviewers in their sections, and aggregated at Bracket Closing. C-35 requires
the challenger's null hypothesis comparison specifically to be a structured table; domain
reviewers need not re-score the same dimensions. C-16 is about a shared scoring scaffold across
all bracket sections; C-35 is about the challenger's evaluation format at null hypothesis gate
time only.

**Distinction from C-23**: C-23 requires the NULL HYPOTHESIS DERIVATION RULE to cover all
pairwise differentials when three or more alternatives are present. C-35 requires the challenger
to use a structured dimension comparison table regardless of how many alternatives are compared.
C-23 is about the completeness of the derivation rule over alternatives; C-35 is about the
structural format of the comparison itself.

**Pass condition**: the challenger's null hypothesis evaluation contains a structured dimension
comparison table with at least 2 dimensions. Each dimension carries an explicit current-state
score or rating and a proposed-state score or rating. Per-dimension differentials or verdicts are
present. The null hypothesis gate verdict (g_null) is derivable from the table values without
reading challenger prose. The table appears before any domain reviewer section executes.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). Without
bracket architecture the challenger has no formal structural position as a pre-domain gate; its
evaluation format is not architecturally constrained. C-09 FAIL automatically makes C-35 vacuous.

**Fails if** (C-09 active): the challenger provides prose null hypothesis testimony without a
structured dimension comparison table; or a table is present but dimensions are not rated for
both current-state and proposed-state; or the null hypothesis verdict cannot be derived from
table values alone. Partial if a comparison table is present but has only one dimension, or
per-dimension differentials are absent.

---

### C-36 -- §1 Scope Surface Domain Annotation Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-03, V-05 Round 13 -- each §1 IN-SCOPE surface carries a `[DOMAIN: label]`
annotation at enumeration time, creating a mechanical domain registry consumed by the C-34
gap-check (§5.8); V-01 and V-02 omit domain tags, requiring editorial domain inference at
gap-check time; first architecture where the §1 scope enumeration doubles as a pre-committed
domain registry with no editorial step between scope declaration and domain gap-check execution

Each surface enumerated in the §1 IN-SCOPE list carries an explicit `[DOMAIN: label]` annotation
at the time of enumeration -- before any reviewer section executes. The annotations form a domain
registry: a complete mechanical list of all artifact domains present in scope. The C-34 domain
coverage gap-check consumes this registry directly; no editorial domain inference is needed at
gap-check time. Without §1 domain tags, the gap-check must infer domain membership from artifact
surface names at execution time -- an editorial step that can produce different coverage maps for
the same scope declaration depending on how the AI parses surface names.

**Distinction from C-06**: C-06 requires scope surfaces to be enumerated before review begins.
C-36 requires each enumerated surface to carry a domain annotation. C-06 can pass with
plain-text §1 rows; C-36 additionally requires the `[DOMAIN: label]` tag on each row. C-06 is
a presence requirement on scope enumeration; C-36 is a structural annotation requirement on each
enumerated surface.

**Distinction from C-29**: C-29 maps §1 surfaces to reviewer findings post-bracket-closing
(scope-to-finding coverage: was this surface reviewed?). C-36 maps §1 surfaces to artifact
domains at enumeration time (scope-to-domain assignment: what domain is this surface?). C-29
checks coverage after the fact; C-36 pre-classifies domain membership before review begins.

**Distinction from C-34**: C-34 requires the domain coverage gap-check to be pre-committed and
produce ADVISORY-GAP items for uncovered domains. C-36 requires the §1 annotations that make
the gap-check mechanical rather than editorial. C-34 can pass when the gap-check infers domains
from surface names at execution time; C-36 eliminates that editorial step by pre-assigning
domain labels at scope enumeration. The relationship is analogous to C-18 (local gate ledger at
origin) vs. C-14 (gate verdict in register): C-36 is domain assignment at source; C-34 is
consumption of the domain registry.

**Pass condition**: every row in the §1 IN-SCOPE surface list carries an explicit domain
annotation (e.g., `[DOMAIN: API]`, `[DOMAIN: Security]`, `[DOMAIN: DataModel]`) at enumeration
time. The preamble or §1 section header declares that domain annotations are required on all
in-scope surfaces. The C-34 domain gap-check section explicitly references the §1 domain
registry as its source, consuming domain labels rather than inferring them.

**Vacuous case**: C-34 not active -- this criterion scores 0 (not partial, not fail). Without a
domain coverage gap-check, domain annotations on §1 surfaces have no mechanical consumer and the
annotation requirement is vacuous. C-34 FAIL automatically makes C-36 vacuous.

**Fails if** (C-34 active): §1 surfaces are enumerated without domain annotations; or domain
annotations are present on some but not all §1 rows; or domain assignments are inferred
editorially at gap-check time rather than declared at enumeration time; or the C-34 gap-check
does not cite §1 domain tags as its registry source. Partial if domain tags are present on most
§1 rows but one or more rows are unannotated, or if the gap-check only partially consumes the
registry.

---

### C-37 -- NH Dimension Table Bracket Closing Re-population Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-01, V-04, V-05 Round 13 -- §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT
pre-commits BRACKET CLOSING to re-populate the NH dimension comparison table with revised
per-dimension values after receiving domain and lifecycle evidence; table structure
`Dimension | Current-State | Proposed-State | Differential | NH Verdict` re-evaluated at
closing; g_null(final) derivable from revised table values alone; V-02 and V-03 absent (no NH
dimension table -> C-37 vacuous)

After domain reviewers and the lifecycle reviewer have emitted their findings, the BRACKET
CLOSING re-populates the NH dimension comparison table introduced at BRACKET OPENING (C-35) with
revised per-dimension ratings incorporating received evidence. The g_null(final) verdict (stage 3
of C-28) is derivable from the revised table's per-dimension differentials alone, without reading
the bracket closing's prose argument. The re-population requirement is pre-committed in the
preamble: the bracket closing section is explicitly instructed to update each dimension's ratings
based on received evidence before deriving g_null(final).

**Distinction from C-35**: C-35 requires the challenger to use an NH dimension comparison table
at bracket opening (pre-domain). C-37 requires the bracket closing to re-populate that same
table with post-evidence revised values. C-35 establishes the table as the opening evaluation
format; C-37 closes the trajectory by requiring the table to be re-evaluated after all evidence
is in. C-35 can pass while C-37 fails (table exists at opening but bracket closing reassesses
in prose only).

**Distinction from C-16**: C-16 requires the adversarial bracket to use a quantified
multi-dimension ALTERNATIVES TABLE as a structural anchor, re-scored by domain reviewers and
aggregated at bracket closing. C-37 requires the bracket closing to re-populate the NH DIMENSION
TABLE -- the challenger's own null hypothesis evaluation table. The two tables may co-exist;
C-16 is about a shared scoring scaffold across all bracket sections; C-37 is about the NH
dimension trajectory specifically. A variant can pass C-16 (alternatives table aggregated at
closing) while failing C-37 (NH dimension table not re-populated at closing).

**Distinction from C-28**: C-28 pre-commits the g_null progression formula across three stages
(g_null(initial), g_null(post-domain), g_null(final)). C-37 requires the bracket closing to
re-populate the NH dimension table as the structural substrate from which g_null(final) is
derived. C-28 is about the formula chain; C-37 is about the table providing the evidence base
for that formula's final stage. C-28 can pass with a prose-derived g_null(final); C-37
additionally requires the table to be the derivation source at closing.

**Pass condition**: the preamble pre-commits a requirement that BRACKET CLOSING re-populate the
NH dimension comparison table with revised per-dimension values based on received domain and
lifecycle evidence. The bracket closing section contains an updated version of the C-35 NH
dimension table with revised ratings for each dimension. The g_null(final) verdict is derivable
from the revised table's per-dimension differentials or verdicts without reading the bracket
closing narrative. The re-population requirement is stated before any reviewer section executes.

**Vacuous case**: C-35 not active -- this criterion scores 0 (not partial, not fail). Without an
NH dimension table at bracket opening there is no table for the bracket closing to re-populate.
C-09 FAIL automatically makes C-37 vacuous.

**Fails if** (C-35 active): bracket closing reassesses the null hypothesis in prose but does not
re-populate the NH dimension table; or the NH dimension table appears at opening but is absent
from the bracket closing section; or the bracket closing re-population is not pre-committed in
the preamble (table updated editorially). Partial if the bracket closing contains a partial
dimension table (some dimensions revised, others carried forward unchanged without explanation).

---

### C-38 -- Multi-Alternative Column Structure in NH Dimension Table
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: R13 synthesis -- all R13 variants are mutually exclusive on C-23 (pairwise NH
derivation rule) and C-35 (NH dimension table): C-23 PASS variants (V-02/V-03) have no NH
dimension table; C-35 PASS variants (V-01/V-04/V-05) have two-column tables covering only Build
vs. Status-Quo, failing C-23 because the Best-Non-Build-Alt column is absent; no R13 variant
achieves both; C-38 names the structural resolution: extend the NH dimension table to three
comparison columns, making both pairwise differentials (C-23 condition) mechanically derivable
from table values and restoring C-23 PASS alongside C-35 PASS

When the NH dimension comparison table (C-35) is present and the alternatives table includes
three or more options (the condition that activates C-23), the NH dimension table includes
explicit separate columns for the Status-Quo state, the Proposed-Build state, AND the
Best-Non-Build-Alt state. Per-dimension differential or verdict columns cover BOTH pairwise
comparisons (Build vs. Status-Quo AND Build vs. Best-Non-Build-Alt), making both derivations
mechanical from table data. The NULL HYPOTHESIS DERIVATION RULE (C-17/C-23) references both
table differentials as its formula inputs. The g_null verdict is derivable from both sets of
per-dimension differentials without reading prose.

**Distinction from C-23**: C-23 requires the NULL HYPOTHESIS DERIVATION RULE to name both
pairwise differentials as formula inputs when three+ alternatives are present. C-38 additionally
requires the NH dimension table to contain the structural columns supplying those differential
values mechanically -- the table becomes the evidence base for both differentials. C-23 can pass
with a pairwise formula referencing a non-table evidence source; C-38 requires table columns as
the structural derivation basis.

**Distinction from C-35**: C-35 requires the NH dimension table to contain at minimum a
current-state column and a proposed-state column (minimum two comparison columns). C-38 requires
the table to extend to three comparison columns when three+ alternatives exist -- adding the
Best-Non-Build-Alt column to resolve the C-23/C-35 incompatibility observed in R13. A C-35 PASS
with two columns satisfies C-35 but fails C-38 when the alternatives table has three+ options.

**Distinction from C-37**: C-37 requires the bracket closing to re-populate the NH dimension
table with revised values. C-38 requires the table (at opening and at closing) to have the
multi-alternative column structure. A C-37 PASS with a two-column table satisfies C-37 but
fails C-38 when C-23 is active.

**Pass condition**: the NH dimension comparison table (C-35 table, and its bracket closing
re-population per C-37 if active) contains at minimum three comparison columns: Status-Quo state,
Proposed-Build state, and Best-Non-Build-Alt state. Per-dimension differential or verdict columns
cover both pairwise comparisons. The NULL HYPOTHESIS DERIVATION RULE in the preamble references
both table differentials. The g_null verdict is derivable from both sets of table differentials
without reading prose.

**Vacuous case**: C-35 not active OR C-23 not active (alternatives table contains only two
options -- a single-differential table is sufficient) -- this criterion scores 0 (not partial,
not fail). C-35 FAIL automatically makes C-38 vacuous.

**Fails if** (C-35 active, C-23 active): the NH dimension table contains only two comparison
columns (Status-Quo and Proposed-Build), omitting the Best-Non-Build-Alt column; or a third
alternative column is present but no per-dimension differential for the Build-vs-Best-Alt
comparison is included; or the NULL HYPOTHESIS DERIVATION RULE references only one table
differential despite three comparison columns being present. Partial if a third alternative
column is included but per-dimension differentials for the Build-vs-Best-Alt comparison are
absent, or the derivation rule references both differentials but only one is table-derived.

---

### C-39 -- NH Dimension Table Column Aggregation Formula Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 14 -- §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT extended with an
explicit NH TABLE AGGREGATION RULE naming the derivation formula for each comparison column at
bracket closing: Column A = challenger's original opening value carried forward per dimension;
Column B = average of domain reviewer scores for the proposed-state dimension; Column C = average
of domain reviewer scores for the best-non-build-alt dimension; V-01/V-04 R14 re-populate the
three-column table (C-37/C-38 PASS) but without per-column formulas (C-39 FAIL); first
architecture where the bracket closing NH table re-population is fully mechanical with no
editorial discretion remaining in how column values are computed

The pre-commitment contract for bracket closing NH dimension table re-population (C-37) is
extended with an explicit per-column aggregation formula specifying how each cell value in the
three-column NH dimension table is computed from received evidence. The formula names the
derivation rule for each comparison column independently:
  Column A (Status-Quo): challenger's opening value carried forward unchanged (no domain
    testimony revises the status-quo baseline; it is the control arm)
  Column B (Proposed-Build): average (or equivalent stated formula) of all domain reviewer
    scores for the proposed-state dimension
  Column C (Best-Non-Build-Alt): average (or equivalent stated formula) of all domain reviewer
    scores for the best-non-build-alt dimension

The column aggregation formula eliminates the last remaining editorial step inside the
re-population step: without it, the bracket closing knows it must re-populate the table (C-37)
and that the table has three columns (C-38), but must decide editorially how to compute revised
B and C column values from domain evidence. With C-39, that decision is mechanically
pre-committed.

**Distinction from C-37**: C-37 requires the bracket closing to re-populate the NH dimension
table with revised per-dimension values. C-39 requires the pre-committed formula specifying how
each column value is computed during re-population. C-37 establishes the re-population
obligation; C-39 specifies the computation method so re-population is fully mechanical. C-37 can
pass when the bracket closing re-populates values by editorial judgment; C-39 additionally
requires the derivation rule for each column to be pre-committed before any reviewer section
executes.

**Distinction from C-38**: C-38 requires the NH dimension table to have three comparison columns
(structural requirement on column count). C-39 requires the per-column derivation formula for
how each of those three column values is computed at bracket closing (computation requirement on
column content derivation). C-38 can pass with three columns whose values are editorially
assigned at closing; C-39 additionally requires the assignment to be formula-driven.

**Distinction from C-24**: C-24 pre-commits the domain-aggregate formula for combining domain
gate verdicts into a single aggregated signal consumed by the disposition contract. C-39
pre-commits the per-column aggregation formula for computing revised NH dimension table cells
from domain reviewer scores. Both are pre-committed aggregation formulas operating on different
inputs. C-24 aggregates gate verdicts; C-39 aggregates dimension-level scores into NH table
cell values.

**Pass condition**: the preamble (or §17 equivalent contract block) pre-commits a NH TABLE
AGGREGATION RULE (or equivalent) specifying the derivation formula for each comparison column in
the three-column NH dimension table at bracket closing time. The rule names at minimum: (a) how
the Status-Quo column value is determined (typically: carried forward from opening), (b) how the
Proposed-Build column value is computed from domain evidence (formula over domain scores per
dimension), and (c) how the Best-Non-Build-Alt column value is computed from domain evidence
(formula over domain scores per dimension). The bracket closing section applies the formula
mechanically -- no editorial column-value selection permitted. The aggregation rule is stated
before any reviewer section executes.

**Vacuous case**: C-37 not active OR C-38 not active -- this criterion scores 0 (not partial,
not fail). Without bracket closing re-population (C-37) there is no re-population step to
specify a formula for. Without a three-column table structure (C-38) the per-column distinction
is moot. Both conditions must be active for C-39 to apply.

**Fails if** (C-37 active, C-38 active): bracket closing re-populates the three-column NH
dimension table with revised values (C-37 PASS, C-38 PASS) but the method for computing revised
column B and C values from domain evidence is not pre-committed -- the bracket closing selects
an aggregation method editorially. Partial if a column formula is stated for some columns but
not all (e.g., Column A formula stated but Column B/C aggregation method left editorial).

---

## Scoring Reference

### Composite Formula

```
essential_pts    = (essential_pass  / 5) * 60
recommended_pts  = (recommended_pass / 3) * 30
aspirational_pts =  aspirational_pass    *  5   # 5 pts each, max 155
composite = essential_pts + recommended_pts + aspirational_pts
```

**Maximum**: 60 + 30 + 155 = **245 pts**

### Score Bands

| Band | Condition | Composite |
|------|-----------|-----------|
| Gold | all 5 essential pass | >= 210 |
| Strong | all 5 essential pass | 90-209 |
| Partial | <= 4 essential pass | any |
| Minimal | <= 3 essential pass | any |

### Paths to Gold (210 pts)

| Path | Essential | Rec | Asp passed | Composite |
|------|-----------|-----|------------|-----------|
| Full rec + 24 asp | 5/5 | 3/3 | 24/31 | 60+30+120 = 210 |
| 2 rec + 26 asp | 5/5 | 2/3 | 26/31 | 60+20+130 = 210 |
| 1 rec + 28 asp | 5/5 | 1/3 | 28/31 | 60+10+140 = 210 |
| 0 rec + 30 asp | 5/5 | 0/3 | 30/31 | 60+0+150 = 210 |

### Round 11 Calibration (retroactive, v10 -> v13)

All R11 variants: C-33/C-34/C-35 absent from all -> C-36/C-37/C-38/C-39 all vacuous or FAIL.
No retroactive score change; all R11 v11 scores carry forward unchanged.

### Round 12 Calibration (retroactive, v11 -> v13)

C-36: domain gap-check (C-34 PASS) in V-02 R12 but §1 domain annotation not confirmed from
partial text -- FAIL assumed pending full text confirmation. C-37: V-02 R12 bracket closing
re-population of NH table not confirmed -- FAIL assumed. C-38: V-02 R12 two-column NH table
(no Best-Alt column confirmed) -- FAIL. C-39: C-38 FAIL -> C-39 vacuous. No retroactive score
change until R12 full text review.

### Round 13 Calibration (v11 -> v13)

| Variant | v11 | C-36 | C-37 | C-38 | C-39 | v13 |
|---------|-----|------|------|------|------|-----|
| **V-05** | 220 | PASS (+5) | PASS (+5) | FAIL | vac (0) | **230/245** |
| **V-03** | 220 | PASS (+5) | vac (0) | vac (0) | vac (0) | **225/245** |
| V-04 | 215 | FAIL | PASS (+5) | FAIL | vac (0) | **220/245** |
| V-02 | 215 | FAIL | vac (0) | vac (0) | vac (0) | **215/245** |
| V-01 | 210 | FAIL | PASS (+5) | FAIL | vac (0) | **215/245** |

C-39 vacuous for all R13 variants: C-38 FAIL or C-38 vacuous in every variant (no three-column
NH table with per-column aggregation formula in any R13 prompt).

**C-36 notes:**
- V-03, V-05: §1 IN-SCOPE surfaces carry `[DOMAIN: label]` annotations; C-34 gap-check (§5.8)
  consumes registry mechanically, no editorial domain inference. PASS.
- V-01, V-02, V-04: §1 rows are plain text; domain inference at gap-check time is editorial. FAIL.

**C-37 notes:**
- V-01, V-04, V-05: §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT pre-commits BRACKET CLOSING
  to re-populate the NH dimension table with revised values. PASS.
- V-02: C-35 FAIL (§17 is LENS APPLICABILITY CONTRACT, not NH dimension table) -> C-37 vacuous.
- V-03: C-35 FAIL (no NH dimension table) -> C-37 vacuous.

**C-38 notes:**
- V-01, V-04, V-05: NH dimension table has two comparison columns (`Current-State |
  Proposed-State`) only; Best-Non-Build-Alt column absent; C-23 FAIL confirms single-differential
  structure in all three. FAIL.
- V-02, V-03: C-35 FAIL -> C-38 vacuous.

### Round 14 Calibration (v12 -> v13)

Baseline = V-05 R13 under v12 = 230. C-23 and C-38 are the only open criteria from v12.
C-39 is the new R14 criterion. All other criteria inherited PASS from V-05 R13 base.

| Variant | v12 base | C-23 | C-38 | C-39 | v13 |
|---------|----------|------|------|------|-----|
| **V-05** | 230 | PASS (+5) | PASS (+5) | PASS (+5) | **245/245** |
| **V-01** | 230 | PASS (+5) | PASS (+5) | FAIL (0) | **240/245** |
| **V-04** | 230 | PASS (+5) | PASS (+5) | FAIL (0) | **240/245** |
| **V-02** | 230 | PASS (+5) | FAIL (0) | vac (0) | **235/245** |
| **V-03** | 230 | FAIL (0) | FAIL (0) | vac (0) | **230/245** |

**C-39 PASS (V-05):** §17 NH TABLE AGGREGATION RULE names per-column derivation: Column A =
challenger's original opening value (carried forward); Column B = average of domain reviewer
scores for the Proposed-Build dimension; Column C = average of domain reviewer scores for the
Best-Non-Build-Alt dimension. Fully mechanical re-population; no editorial discretion.

**C-39 FAIL (V-01, V-04):** Three-column table re-populated at closing (C-37/C-38 PASS) but no
per-column derivation formula in §17. AI selects aggregation method at bracket closing time.

**C-39 vacuous (V-02, V-03):** C-38 FAIL -> C-39 vacuous.

**New ranking (v13):**

| Rank | Variation | v13 Score | Band | v12 Score |
|------|-----------|-----------|------|-----------|
| **1** | **V-05 R14** | **245/245** | Gold | 230 |
| **2** | **V-01 R14** | **240/245** | Gold | 230 |
| **2** | **V-04 R14** | **240/245** | Gold | 230 |
| **4** | V-02 R14 | **235/245** | Gold | 230 |
| **5** | V-03 R14 | **230/245** | Gold | 230 |

V-05 R14 is the first variant to achieve the maximum score. Path to 245: three-column NH
dimension table (C-38) + pairwise derivation rule naming both table differentials (C-23) +
per-column aggregation formula at bracket closing (C-39). All three satisfied simultaneously
for the first time in R14 V-05.

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
C-30 vacuous (C-02 inactive) = 0, not partial.
C-31 vacuous (C-09 inactive OR no lens.verify entries) = 0, not partial.
C-32 vacuous (C-09 inactive) = 0, not partial.
C-33 vacuous (C-31 inactive) = 0, not partial.
C-34 vacuous (C-31 inactive OR no multi-domain artifact) = 0, not partial.
C-35 vacuous (C-09 inactive) = 0, not partial.
C-36 vacuous (C-34 inactive) = 0, not partial.
C-37 vacuous (C-35 inactive) = 0, not partial.
C-38 vacuous (C-35 inactive OR C-23 inactive) = 0, not partial.
C-39 vacuous (C-37 inactive OR C-38 inactive) = 0, not partial.
