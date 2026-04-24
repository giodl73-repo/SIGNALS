Written to `simulations/quest/rubrics/org-review-rubric-v19-2026-03-17.md`.

---

**v19 summary:**

**New criteria: C-51, C-52, C-53** (5 pts each, aspirational)

| ID | Name | Source | PASS variants |
|----|------|--------|---------------|
| C-51 | REVIEWER PRIORITY MANIFEST as Named Non-verdict Sequencing Block | V-01/V-04/V-05 R20 | 3/5 |
| C-52 | Lifecycle Phase Sub-Step Sequencing in Section Order Contract | V-02/V-04/V-05 R20 | 3/5 |
| C-53 | PIPELINE COMPLIANCE LEDGER as Pre-committed Named Post-Domain Section | V-03/V-05 R20 | 2/5 |

**Chain logic:**

R20 introduced three independent structural axes against the R19 V-05 300/300 baseline. Each axis
asked: does adding this structural block independently preserve 300/300? All five variants scored
300/300 under v18, confirming all three are additive extensions, not corrections. The new criteria
capture the structural patterns that differentiate the variants:

- C-51: The REVIEWER PRIORITY MANIFEST is a pre-committed non-verdict block that locks reviewer
  execution order. It extends C-25 by naming a second explicit non-verdict section in the exclusion
  list. Its existence converts the reviewer sequence from an implied template order into a
  contractually locked constraint.

- C-52: The §8 SECTION ORDER CONTRACT (C-26) extends from section-level immutability to sub-step
  immutability within the lifecycle reviewer section. The LIFECYCLE PHASE GATE SUB-TABLE schema
  extends the TABLE FORMAT CONTRACT (C-44) to cover lifecycle phase-level output structures.
  Together, lifecycle phase sequencing becomes as contractually locked as section sequencing.

- C-53: The PIPELINE COMPLIANCE LEDGER is a new named post-domain section (step 10a in §8 section
  order). It carries its own TABLE FORMAT CONTRACT schema declaration, is explicitly named in the
  gate ledger non-verdict exclusion list, and appears after all domain sections and before BRACKET
  CLOSING. It extends three prior criteria simultaneously: C-25 (non-verdict exclusion), C-26
  (section order coverage), and C-44 (unified schema). With C-53, the pipeline compliance audit is
  a contractually pre-committed section, not an editorial post-bracket synthesis step.

**V-04 + C-53 next round target**: V-04 passes C-51 and C-52 but not C-53. Add a PIPELINE
COMPLIANCE LEDGER section to V-04 = 315/315.

**Score changes:**
- Aspirational: 42 -> 45 (criteria count C-09 through C-53)
- Max aspirational pts: 45 x 5 = 225
- Max: 300 -> 315
- Gold threshold: 265 -> 275

**R20 ranking under v19:**

| Rank | Variant | Score | New criteria PASS |
|------|---------|-------|-------------------|
| 1 | V-05 | **315/315** | C-51+C-52+C-53 |
| 2 | V-04 | **310/315** | C-51+C-52 |
| 3 (tie) | V-01 | **305/315** | C-51 |
| 3 (tie) | V-02 | **305/315** | C-52 |
| 3 (tie) | V-03 | **305/315** | C-53 |

**R20 score computation (all R20 variants at 300/300 under v18; new criteria differentiators):**

| Variant | C-51 | C-52 | C-53 | v19 Score |
|---------|------|------|------|-----------|
| **V-05** | PASS (+5) | PASS (+5) | PASS (+5) | **315/315** |
| **V-04** | PASS (+5) | PASS (+5) | FAIL (0) | **310/315** |
| **V-01** | PASS (+5) | FAIL (0) | FAIL (0) | **305/315** |
| **V-02** | FAIL (0) | PASS (+5) | FAIL (0) | **305/315** |
| **V-03** | FAIL (0) | FAIL (0) | PASS (+5) | **305/315** |

**C-51 discrimination (R20):** V-01/V-04/V-05 pre-commit a REVIEWER PRIORITY MANIFEST block that
sequences reviewer roles by execution priority and names the manifest explicitly in the §6 gate
ledger non-verdict exclusion list. V-02/V-03 omit this block -- reviewer execution order is
implied by template structure, not contractually locked.

**C-52 discrimination (R20):** V-02/V-04/V-05 extend the §8 SECTION ORDER CONTRACT with sub-step
numbering for lifecycle reviewer phases (e.g., Step 7a, 7b, 7c for lifecycle phase gates) and add
LIFECYCLE PHASE GATE SUB-TABLE schema to TABLE FORMAT CONTRACT. V-01/V-03 have lifecycle section
placement (C-22 PASS) but without sub-step enumeration in the immutable contract.

**C-53 discrimination (R20):** V-03/V-05 add a PIPELINE COMPLIANCE LEDGER as step 10a in the §8
section order (after BRACKET CLOSING per C-26, as a post-bracket audit step), declare its schema
in TABLE FORMAT CONTRACT, and name it explicitly in the §6 gate ledger non-verdict exclusion list
per C-25. V-01/V-02/V-04 have no pipeline compliance ledger section.

**R20 floor:** All five variants exceed Gold (275). Floor advances from R19's 285 to R20's 305.

No retroactive score changes on R1-R19. All R19 v18 scores carry forward unchanged.

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

## Aspirational Criteria -- 225 pts (structural integrity, auditability, automation)

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
chain-of-custody mechanism editorial.

**Pass condition**: LOCAL GATE LEDGER PROTOCOL (or equivalent) appears in the preamble,
defining: (a) the syntax of a local ledger row (Gate Verdict + Class at minimum), (b) when to
emit it (end of each reviewer section, after verdict), and (c) the assembly rule (copy to master
register verbatim). Protocol is stated before any reviewer section executes.

**Vacuous case**: C-18 not active -- this criterion scores 0 (not partial, not fail). C-18 FAIL
automatically makes C-19 vacuous.

**Fails if** (C-18 active): local ledger rows are emitted (C-18 PASS) but the protocol governing
their syntax and assembly was not pre-committed in the preamble.

---

### C-20 -- Verbatim Assembly Prohibition on Re-derivation
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-04 Round 5 -- "Copy all Local Gate Ledger rows...verbatim. Do not re-derive Gate
Verdict or Class." explicit prohibition; V-05 Round 5 -- "Copy...verbatim" implies same
constraint

The master register assembly instruction explicitly prohibits re-derivation of Gate Verdict or
Class during assembly. The instruction is a copy directive, not a synthesis directive. The local
ledger emits the authoritative verdict (C-18); C-20 ensures that authority is not overridden
during assembly.

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
**Source**: V-05 Round 5 -- chain extends to lifecycle reviewer archetype; lifecycle reviewer
emits local row; coverage is universal across bracket, domain, and lifecycle archetypes

The inline gate ledger (C-18) is emitted by ALL verdict-emitting reviewer archetypes, not only
bracket and domain roles. At minimum, coverage must extend to: (a) Bracket Opening (challenger /
inertia-advocate), (b) all domain reviewers, (c) Bracket Closing (post-domain challenger), and
(d) the Lifecycle reviewer (if present). The master register assembly instruction covers all
archetype sections.

C-18 requires some reviewer sections to emit local rows. C-21 requires all verdict-emitting
reviewer archetypes to emit them.

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
**Source**: V-04 Round 6 -- lifecycle reviewer positioned before bracket closing; bracket closing
names g_lifecycle as a labeled received input to null hypothesis reassessment; first architecture
where Bracket Closing integrates both domain and lifecycle evidence

When bracket architecture is used (C-09 active), the lifecycle reviewer section executes BEFORE
the Bracket Closing section, so the challenger can explicitly receive and reference the lifecycle
gate verdict (g_lifecycle) during null hypothesis reassessment.

C-21 requires lifecycle to emit a local gate ledger row. C-22 additionally requires the bracket
closing to receive and reference that verdict explicitly.

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
**Source**: V-03 and V-05 Round 6 -- three-alternative table with NULL HYPOTHESIS DERIVATION
RULE mapping both differentials (B-A and B-C) to one verdict; prevents verdict from being
trivially defeated by choosing a weak comparator

When the alternatives table includes three or more options, the NULL HYPOTHESIS DERIVATION RULE
maps ALL relevant differentials involving the proposed artifact to the verdict -- not just one.
A two-differential rule (e.g., Build beats Status Quo AND Build beats Hybrid) prevents the null
hypothesis from being defeated by cherry-picking the weakest alternative.

**Pass condition**: the alternatives table contains three or more options. The NULL HYPOTHESIS
DERIVATION RULE names all relevant pairwise differentials involving the proposed artifact (at
minimum: build vs status quo AND build vs best non-build alternative). The derivation rule is a
formula mapping all named differentials to a single verdict. The formula is pre-committed in the
preamble before any reviewer section executes.

**Vacuous case**: C-09 not active OR the alternatives table contains only two options -- this
criterion scores 0 (not partial, not fail).

**Fails if** (C-09 active, three+ alternatives): the NULL HYPOTHESIS DERIVATION RULE maps only
one differential to the verdict. Partial if more than one differential is evaluated but the rule
is stated narratively rather than as a formula.

---

### C-24 -- Domain-Aggregate Formula Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-04 Round 7 -- DOMAIN-AGGREGATE FORMULA (median rule) pre-committed in preamble;
bracket closing applies formula mechanically; first architecture with a pre-committed aggregation
method for domain verdicts

When domain reviewer verdicts must be aggregated before the bracket closing applies its
disposition derivation rule, the aggregation formula (median rule, majority rule, or equivalent)
is pre-committed in the preamble. The bracket closing is explicitly instructed to apply the
formula rather than select an aggregation method editorially at execution time.

**Pass condition**: a domain-aggregate formula is stated in the preamble before any section
executes. The bracket closing section references and applies the formula mechanically. The
formula covers all cases needed to produce a single aggregated signal from multiple domain
verdicts.

**Vacuous case**: C-09 not active OR no multi-domain aggregation step exists -- this criterion
scores 0 (not partial, not fail).

**Fails if** (C-09 active, aggregation step present): domain verdicts are aggregated editorially
at bracket closing without a pre-committed formula; or a formula is referenced but not
pre-committed. Partial if a formula is pre-committed but the bracket closing section does not
cite it explicitly.

---

### C-25 -- Non-verdict Section Explicitly Excluded from Gate Ledger
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 7 -- domain-aggregate checkpoint explicitly marked "EXCLUDED: emits NO
ledger row" because it produces no verdict; first architecture where a non-verdict intermediate
section is unambiguously excluded from the gate ledger emission requirement

When the review includes an intermediate section that synthesizes or checkpoints findings but
produces no gate verdict of its own, the gate ledger protocol explicitly names that section as
excluded from ledger emission. C-21 requires all verdict-emitting sections to emit ledger rows.
C-25 requires the protocol to explicitly state which sections are NOT verdict-emitting.

In R20, the exclusion list is extended by variants: V-01/V-04/V-05 name REVIEWER PRIORITY
MANIFEST as excluded; V-03/V-05 name PIPELINE COMPLIANCE LEDGER as excluded. C-25 passes when
at least one non-verdict section is explicitly named and excluded. C-51 and C-53 capture the
specific named additions.

**Pass condition**: the gate ledger protocol (C-19) explicitly names at least one intermediate
non-verdict section and marks it excluded from ledger emission, with a stated reason. The
exclusion is declared in the preamble or protocol block, not discovered mid-review.

**Vacuous case**: C-18 not active OR no intermediate non-verdict section exists -- this criterion
scores 0 (not partial, not fail).

**Fails if** (C-18 active, non-verdict section present): the non-verdict section is not
mentioned in the protocol, or is listed under C-21's universal coverage requirement without an
exclusion exception.

---

### C-26 -- Canonical Section Order Pre-committed as Immutable Contract
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-03 and V-05 Round 8 -- SECTION ORDER CONTRACT names the canonical execution
sequence as an immutable constraint in the preamble; distinct from C-22 which checks behavioral
ordering in output; C-26 requires the ordering to be contractually declared before execution so
reordering is a contract violation, not merely an observable defect

The canonical section execution order is declared in the preamble as an explicit immutable
contract term -- not merely implied by the sequence of sections in the template. The declaration
names each section in order and states that reordering is prohibited.

C-22 is synergistic with C-26: C-22 requires behavioral conformance; C-26 requires the ordering
to be pre-committed as an immutable contract.

In R20, V-02/V-04/V-05 extend this contract to include lifecycle sub-step numbering (C-52);
V-03/V-05 extend it to include step 10a for PIPELINE COMPLIANCE LEDGER (C-53).

**Pass condition**: the preamble contains an explicitly labeled section-order contract naming the
canonical section sequence. The contract explicitly states that reordering is prohibited. The
named sequence includes at minimum bracket opening, domain sections, and bracket closing in that
order (with lifecycle positioned before bracket closing when lifecycle is present). The contract
is stated before any reviewer section executes.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). C-09 FAIL
automatically makes C-26 vacuous.

**Fails if** (C-09 active): no section order contract is stated in the preamble; or the
execution sequence is only implied by the printed template order without a named immutability
constraint. Partial if a sequence is named but the immutability statement is absent.

---

### C-27 -- CH-ID Cross-Section Saturation Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-01, V-04, V-05 Round 9 -- CH-ID SATURATION REQUIREMENT pre-commits a two-tier
coverage formula: SATURATED = response from >= 1 DOMAIN section before LIFECYCLE executes;
FULLY SATURATED = domain + lifecycle both responded before BRACKET CLOSING; dedicated CH-ID
SATURATION CHECK section verifies pre-LIFECYCLE saturation; BRACKET CLOSING enforces full
saturation and prohibits PASS when any CH-ID is UNSATURATED without waiver; absent in V-02/V-03

A dedicated CH-ID SATURATION REQUIREMENT is pre-committed in the preamble defining two
cross-section coverage tiers: (1) SATURATED -- every CH-ID has received a response from at
least one DOMAIN reviewer section before LIFECYCLE executes; (2) FULLY SATURATED -- every CH-ID
has received both a domain and a lifecycle response before BRACKET CLOSING. BRACKET CLOSING
prohibits a PASS verdict when any CH-ID is UNSATURATED without a stated waiver.

**Distinction from C-05**: C-05 requires every reviewer section to carry a CH-ID response table
(per-section structural rule). C-27 adds the cross-section completion contract.

**Pass condition**: a CH-ID SATURATION REQUIREMENT block appears in the preamble defining the
SATURATED and FULLY SATURATED tiers. A dedicated CH-ID SATURATION CHECK section runs after
domain sections and before LIFECYCLE. BRACKET CLOSING includes a saturation table and an
explicit prohibition on PASS when any CH-ID is UNSATURATED without waiver.

**Vacuous case**: C-09 not active OR C-05 not active -- this criterion scores 0 (not partial,
not fail).

**Fails if** (C-09 active, C-05 active): no cross-section saturation requirement is pre-committed;
or BRACKET CLOSING does not enforce saturation. Partial if a saturation check section exists but
the requirement is not pre-committed, or BRACKET CLOSING references saturation without a blocking
prohibition.

---

### C-28 -- Null Hypothesis Progression Formula Pre-committed as 3-Stage Mechanical Contract
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-02, V-04, V-05 Round 9 -- NULL HYPOTHESIS PROGRESSION CONTRACT pre-commits a
3-stage mechanical derivation chain; GClose verdict must equal g_null(final) unless explicit
override declared; absent in V-01 and V-03

A NULL HYPOTHESIS PROGRESSION CONTRACT is pre-committed in the preamble specifying a three-stage
mechanical derivation chain for the null hypothesis verdict (g_null):
  Stage 1: g_null(initial) = GOpen (Bracket Opening gate verdict)
  Stage 2: g_null(post-domain) = formula(G_domain_agg, g_null(initial))
  Stage 3: g_null(final) = formula(G_lifecycle, g_null(post-domain))
The GClose (Bracket Closing) verdict must equal g_null(final). Deviation requires an explicit
override with named justification. The three g_null values are emitted as labeled fields at
their respective checkpoints.

**Distinction from C-03**: C-03 requires a null hypothesis gate to exist. C-28 pre-commits the
trajectory formula governing how that verdict evolves across all three checkpoints.

**Pass condition**: a NULL HYPOTHESIS PROGRESSION CONTRACT appears in the preamble naming all
three stages and their derivation formulas. The contract specifies that GClose must equal
g_null(final) or declare an explicit override. The three g_null values are emitted as labeled
fields at their respective checkpoints. The progression is summarized in CROSS-ROLE SIGNALS or
equivalent synthesis section.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). C-09 FAIL
automatically makes C-28 vacuous.

**Fails if** (C-09 active): the null hypothesis verdict is produced at each checkpoint but the
derivation formula linking checkpoints is not pre-committed. Partial if two of three stages are
pre-committed but the third stage is editorial, or if the GClose override requirement is absent.

---

### C-29 -- Scope-to-Finding Coverage Gate Post-Bracket-Closing
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-03, V-05 Round 9 -- SCOPE COVERAGE GATE PROTOCOL pre-commits a dedicated SCOPE
COVERAGE RECONCILIATION section after BRACKET CLOSING; GAP surfaces forced to ADVISORY-GAP and
appended to ACTION ITEM REGISTER; gate emits informational-only signal; absent in V-01, V-02,
V-04

A SCOPE COVERAGE GATE PROTOCOL is pre-committed in the preamble specifying that after BRACKET
CLOSING, a dedicated SCOPE COVERAGE RECONCILIATION section executes. Each scope surface is
classified: COVERED (appears in >= 1 finding) or GAP (no finding). GAP surfaces are
automatically assigned LOW advisory severity and appended to the ACTION ITEM REGISTER as
ADVISORY-GAP items. The gate emits a COVERED/PARTIAL signal that is informational only -- it
does not feed the gate ledger formula and produces no ledger row.

**Pass condition**: a SCOPE COVERAGE GATE PROTOCOL appears in the preamble defining the
reconciliation section, its placement after BRACKET CLOSING, the COVERED/GAP classification
rule, the ADVISORY-GAP forced assignment for gaps, and the informational-only (non-ledger) status
of its output. The scope enumeration carries the annotation that rows will be cited in
reconciliation. The reconciliation section executes after BRACKET CLOSING and maps every
IN-SCOPE surface. GAP items appear in the ACTION ITEM REGISTER as ADVISORY-GAP.

**Vacuous case**: C-09 not active OR no explicit scope surface enumeration exists -- this
criterion scores 0 (not partial, not fail).

**Fails if** (C-09 active, scope enumeration present): scope coverage is assessed only through
prose in CROSS-ROLE SIGNALS without a dedicated post-bracket-closing section; or GAP surfaces
are not forced to ADVISORY-GAP status; or the section emits a gate ledger row. Partial if a
dedicated reconciliation section exists but the pre-commitment is absent from the preamble, or
the scope annotation is missing.

---

### C-30 -- Per-Finding Severity Chain Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-01, V-04, V-05 Round 11 -- per-finding Severity column on every finding row;
Section Severity derives mechanically as worst(F-1, F-2, ...) over all finding severities in
that section; eliminates editorial section-level severity assignment; absent in V-02 and V-03

Each finding row in every reviewer section carries an individual Severity field. The Section
Severity is pre-committed to derive mechanically as the worst-case over all individual finding
severities in that section. The derivation formula is stated as an immutable contract in the
preamble before any reviewer section executes. No editorial assignment of section-level severity
is permitted.

**Distinction from C-02**: C-02 defines what severity labels mean. C-30 defines how they
propagate from individual finding to section signal.

**Distinction from C-12**: C-12 pre-commits gate-verdict-to-action-item-class derivation.
C-30 pre-commits finding-severity-to-section-severity aggregation. Different layers.

**Pass condition**: a per-finding severity aggregation formula appears in the preamble as an
immutable contract. Every finding row in every reviewer section carries an individual Severity
field. The Section Severity in each gate ledger row is consistent with
worst(individual finding severities in that section).

**Vacuous case**: C-02 not active -- this criterion scores 0 (not partial, not fail).

**Fails if** (C-02 active): section-level severity is assigned editorially without an
individual-finding-severity aggregation contract; or finding rows do not carry individual
Severity fields; or the aggregation formula is not pre-committed. Partial if individual finding
severities are present but the worst-case aggregation formula is not pre-committed.

---

### C-31 -- Role Lens Exhaustion Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-02, V-04, V-05 Round 11 -- LENS COVERAGE TABLE pre-committed requiring ALL
lens.verify entries to appear with ADDRESSED or OPEN status; OPEN entries automatically surface
as ADVISORY-OPEN-LENS items; absent in V-01 and V-03

A LENS COVERAGE TABLE is pre-committed in the preamble: for each active reviewer role, ALL
lens.verify entries listed in that role's definition must appear in the table with status
ADDRESSED (a finding references this lens dimension) or OPEN (no finding referenced this lens
dimension). The pre-commitment contract specifies that OPEN entries are automatically promoted to
ADVISORY-OPEN-LENS items in the ACTION ITEM REGISTER.

**Distinction from C-27**: C-27 tracks cross-section saturation of CH-IDs. C-31 tracks
exhaustion of role-specific lens.verify dimensions. Independent source sets.

**Distinction from C-29**: C-29 operates on the artifact scope inventory. C-31 operates on the
reviewer competency inventory.

**Pass condition**: a LENS COVERAGE TABLE protocol appears in the preamble naming the requirement
that all lens.verify entries from each active role appear with ADDRESSED or OPEN status. The
table is populated after all reviewer sections complete and before DISPOSITION. OPEN entries
appear as ADVISORY-OPEN-LENS action items.

**Vacuous case**: C-09 not active OR role definitions contain no lens.verify entries -- this
criterion scores 0 (not partial, not fail).

**Fails if** (C-09 active, lens.verify entries present): no LENS COVERAGE TABLE exists; or lens
entries appear without ADDRESSED/OPEN classification; or OPEN entries are not promoted to
ADVISORY-OPEN-LENS action items; or the protocol is not pre-committed. Partial if a LENS
COVERAGE TABLE is produced but only for some roles, or OPEN entries are noted but not formally
registered as action items.

---

### C-32 -- Primary Driver Derivation Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-03, V-05 Round 11 -- pre-committed 9-rule precedence formula over the gate verdict
vector mechanically selects a single gate as the Primary Driver of the DISPOSITION; eliminates
the last remaining editorial step after all gate verdicts are known; absent in V-01, V-02, V-04

A PRIMARY DRIVER DERIVATION CONTRACT is pre-committed in the preamble specifying a rule-ordered
precedence formula over the full gate verdict vector. After all gate verdicts are known, the
formula applies the rules in order to select exactly one gate as the Primary Driver of the
DISPOSITION mechanically. The Primary Driver attribution is emitted as a labeled field at
DISPOSITION time and is auditable from gate verdict values alone without reading reviewer
narrative.

**Distinction from C-10 / C-17**: C-10/C-17 answer "what is the outcome?". C-32 answers "which
gate caused it?".

**Pass condition**: a PRIMARY DRIVER DERIVATION CONTRACT appears in the preamble. The contract
names an ordered rule set (>= 3 rules in a defined precedence order) covering all gate verdict
combinations and selecting exactly one gate as Primary Driver per combination. A labeled Primary
Driver field is emitted at DISPOSITION time with a value derivable from the gate verdict vector
without reading reviewer narrative.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). C-09 FAIL
automatically makes C-32 vacuous.

**Fails if** (C-09 active): no Primary Driver attribution is emitted; or attribution is assigned
editorially without a pre-committed rule formula; or the formula is stated post-hoc. Partial if
a Primary Driver field is emitted but the derivation formula is not pre-committed, or the rule
set does not cover all gate verdict combinations.

---

### C-33 -- Lens Applicability Rating Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-02 Round 12 -- role lens inventory table declares per-entry applicability rating
(HIGH / MEDIUM / LOW) for each role's lens dimensions relative to the specific artifact under
review; applicability tier is the structural basis for ADDRESSED/OPEN determination; absent in
V-01 and V-03

Each entry in the LENS COVERAGE TABLE (C-31) carries an explicit applicability rating (HIGH /
MEDIUM / LOW) for the role's lens dimension relative to the specific artifact under review -- not
a generic capability rating attached to the role definition. The applicability rating is
pre-committed as the basis for the ADDRESSED/OPEN determination. The rating is artifact-specific.

**Distinction from C-31**: C-31 requires the LENS COVERAGE TABLE with ADDRESSED/OPEN
classification. C-33 requires the underlying applicability rating that grounds that decision.
With C-33, the ADDRESSED/OPEN determination is a derived function of the applicability rating.

**Pass condition**: each row in the LENS COVERAGE TABLE includes an explicit applicability rating
(HIGH / MEDIUM / LOW or equivalent tiered scale) specific to the artifact under review. The
preamble or table header states that applicability ratings determine coverage expectations. The
rating is not inferred from generic role definitions.

**Vacuous case**: C-31 not active -- this criterion scores 0 (not partial, not fail).

**Fails if** (C-31 active): the LENS COVERAGE TABLE has ADDRESSED/OPEN classifications but no
per-lens applicability ratings; or applicability is described generically without a per-artifact
rating. Partial if some lens entries carry applicability ratings but others do not, or if a
single applicability level is applied to all lenses without differentiation.

---

### C-34 -- ADVISORY-GAP Domain Coverage Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-02 Round 12 -- gap-check "Which artifact domains have no HIGH-applicability role?"
identifies uncovered artifact domains and classifies each as ADVISORY-GAP in the action register;
first variant where artifact-domain coverage is a pre-committed check with forced ADVISORY-GAP
promotion; absent in V-01 and V-03

A DOMAIN COVERAGE GAP-CHECK protocol is pre-committed in the preamble: after the LENS COVERAGE
TABLE is populated (C-31), a dedicated gap-check step identifies every artifact domain that has
no reviewer with HIGH applicability to it. Each uncovered domain is classified as ADVISORY-GAP
and promoted to the ACTION ITEM REGISTER with the domain name and reason for the gap.

**Distinction from C-31**: C-31 is role-outward (did the reviewer exhaust their lenses?). C-34
is domain-inward (does the domain have an expert reviewer?). The two checks are orthogonal.

**Distinction from C-29**: C-29 maps scope surfaces to reviewer findings post-bracket-closing.
C-34 maps artifact domains to reviewer applicability tiers during the LENS COVERAGE TABLE phase.

**Pass condition**: a domain coverage gap-check is pre-committed in the preamble as a step
following the LENS COVERAGE TABLE. The gap-check identifies artifact domains with no
HIGH-applicability reviewer and classifies each as ADVISORY-GAP. ADVISORY-GAP items appear in
the ACTION ITEM REGISTER naming the uncovered domain and the reason for the gap.

**Vacuous case**: C-31 not active -- this criterion scores 0 (not partial, not fail). C-31 FAIL
automatically makes C-34 vacuous.

**Fails if** (C-31 active): uncovered domains are noted in prose without ADVISORY-GAP
classification or action register promotion; or the gap-check is not pre-committed. Partial if
a gap-check section runs but uncovered domains are not classified as ADVISORY-GAP or not
promoted to the action register.

---

### C-35 -- Null Hypothesis Challenger Dimension Comparison Table
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-02 Round 12 -- challenger uses a structured dimension comparison table contrasting
current-state vs. proposed-state per dimension with explicit per-dimension ratings or scores;
makes null hypothesis evaluation machine-readable and auditable from table values; absent in
V-01 and V-03

The challenger's null hypothesis evaluation uses a structured dimension comparison table with a
defined column set (>= 2 dimensions, current-state score or rating and proposed-state score or
rating per dimension, and a per-dimension differential or verdict). The table is populated before
domain reviewer sections run. The null hypothesis verdict (g_null) is derivable from the table
differentials without reading the challenger's prose argument.

**Distinction from C-03**: C-03 requires a null hypothesis gate to exist (gate presence). C-35
requires the structured table format (structural format requirement).

**Distinction from C-16**: C-16 requires a shared scoring scaffold across all bracket sections.
C-35 requires the challenger's NH comparison specifically to be a structured table.

**Distinction from C-23**: C-23 requires the derivation rule to cover all pairwise differentials.
C-35 requires the structured table format regardless of how many alternatives are compared.

**Pass condition**: the challenger's null hypothesis evaluation contains a structured dimension
comparison table with at least 2 dimensions. Each dimension carries an explicit current-state
score or rating and a proposed-state score or rating. Per-dimension differentials or verdicts are
present. The null hypothesis gate verdict (g_null) is derivable from the table values without
reading challenger prose. The table appears before any domain reviewer section executes.

**Vacuous case**: C-09 not active -- this criterion scores 0 (not partial, not fail). C-09 FAIL
automatically makes C-35 vacuous.

**Fails if** (C-09 active): the challenger provides prose null hypothesis testimony without a
structured dimension comparison table; or a table is present but dimensions are not rated for
both current-state and proposed-state; or the null hypothesis verdict cannot be derived from
table values alone. Partial if a comparison table is present but has only one dimension, or
per-dimension differentials are absent.

---

### C-36 -- Scope Surface Domain Annotation Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: coverage
**Source**: V-03, V-05 Round 13 -- each IN-SCOPE surface carries a [DOMAIN: label] annotation
at enumeration time, creating a mechanical domain registry consumed by the C-34 gap-check; V-01
and V-02 omit domain tags, requiring editorial domain inference; first architecture where scope
enumeration doubles as a pre-committed domain registry

Each surface enumerated in the IN-SCOPE list carries an explicit [DOMAIN: label] annotation at
the time of enumeration -- before any reviewer section executes. The annotations form a domain
registry consumed directly by the C-34 domain coverage gap-check; no editorial domain inference
is needed at gap-check time.

**Distinction from C-06**: C-06 requires scope surfaces to be enumerated. C-36 requires each
enumerated surface to carry a domain annotation.

**Distinction from C-29**: C-29 maps surfaces to reviewer findings post-bracket-closing. C-36
maps surfaces to artifact domains at enumeration time.

**Distinction from C-34**: C-34 requires the domain gap-check to produce ADVISORY-GAP items.
C-36 requires the annotations that make the gap-check mechanical. Analogous to C-18 vs. C-14:
C-36 is domain assignment at source; C-34 is consumption.

**Pass condition**: every row in the IN-SCOPE surface list carries an explicit domain annotation
(e.g., [DOMAIN: API], [DOMAIN: Security], [DOMAIN: DataModel]) at enumeration time. The preamble
or scope section header declares that domain annotations are required on all in-scope surfaces.
The C-34 domain gap-check explicitly references the domain registry as its source.

**Vacuous case**: C-34 not active -- this criterion scores 0 (not partial, not fail). C-34 FAIL
automatically makes C-36 vacuous.

**Fails if** (C-34 active): surfaces are enumerated without domain annotations; or domain
annotations are present on some but not all rows; or domain assignments are inferred editorially
at gap-check time; or the gap-check does not cite the domain tags as its registry source. Partial
if domain tags are present on most rows but one or more are unannotated, or if the gap-check only
partially consumes the registry.

---

### C-37 -- NH Dimension Table Bracket Closing Re-population Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-01, V-04, V-05 Round 13 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT pre-commits
BRACKET CLOSING to re-populate the NH dimension comparison table with revised per-dimension
values after receiving domain and lifecycle evidence; g_null(final) derivable from revised table
values alone; V-02 and V-03 absent (no NH dimension table -> C-37 vacuous)

After domain reviewers and the lifecycle reviewer have emitted their findings, the BRACKET
CLOSING re-populates the NH dimension comparison table introduced at BRACKET OPENING (C-35) with
revised per-dimension ratings incorporating received evidence. The g_null(final) verdict (stage 3
of C-28) is derivable from the revised table's per-dimension differentials alone, without reading
the bracket closing's prose argument. The re-population requirement is pre-committed in the
preamble.

**Distinction from C-35**: C-35 requires the NH dimension table at bracket opening. C-37 requires
the bracket closing to re-populate it with post-evidence revised values. C-35 establishes the
table format; C-37 closes the trajectory.

**Distinction from C-16**: C-16 is about the shared ALTERNATIVES TABLE as bracket anchor. C-37
is about the NH DIMENSION TABLE trajectory specifically.

**Distinction from C-28**: C-28 pre-commits the g_null progression formula chain. C-37 requires
the NH dimension table as the structural substrate. C-28 can pass with a prose-derived
g_null(final); C-37 additionally requires the table to be the derivation source at closing.

**Pass condition**: the preamble pre-commits a requirement that BRACKET CLOSING re-populate the
NH dimension comparison table with revised per-dimension values based on received domain and
lifecycle evidence. The bracket closing section contains an updated version of the NH dimension
table with revised ratings for each dimension. The g_null(final) verdict is derivable from the
revised table's per-dimension differentials or verdicts without reading bracket closing narrative.

**Vacuous case**: C-35 not active -- this criterion scores 0 (not partial, not fail). C-09 FAIL
automatically makes C-37 vacuous.

**Fails if** (C-35 active): bracket closing reassesses in prose but does not re-populate the NH
dimension table; or the NH dimension table appears at opening but is absent from bracket closing;
or the re-population is not pre-committed. Partial if the bracket closing contains a partial
dimension table (some dimensions revised, others carried forward without explanation).

---

### C-38 -- Multi-Alternative Column Structure in NH Dimension Table
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: R13 synthesis -- all R13 variants are mutually exclusive on C-23 (pairwise NH
derivation rule) and C-35 (NH dimension table): C-23 PASS variants have no NH dimension table;
C-35 PASS variants have two-column tables, failing C-23 because the Best-Non-Build-Alt column is
absent; C-38 names the structural resolution: extend the NH dimension table to three comparison
columns, making both pairwise differentials mechanically derivable from table values

When the NH dimension comparison table (C-35) is present and the alternatives table includes
three or more options (the condition that activates C-23), the NH dimension table includes
explicit separate columns for the Status-Quo state, the Proposed-Build state, AND the
Best-Non-Build-Alt state. Per-dimension differential or verdict columns cover BOTH pairwise
comparisons, making both derivations mechanical from table data. The NULL HYPOTHESIS DERIVATION
RULE references both table differentials as its formula inputs.

**Distinction from C-23**: C-23 requires the derivation rule to name both pairwise differentials
as formula inputs. C-38 additionally requires the NH dimension table to contain the structural
columns supplying those differential values mechanically.

**Distinction from C-35**: C-35 requires at minimum two comparison columns. C-38 requires three
comparison columns when three+ alternatives exist.

**Distinction from C-37**: C-37 requires bracket closing re-population. C-38 requires the
three-column structure at both opening and closing.

**Pass condition**: the NH dimension comparison table (C-35 table, and its bracket closing
re-population per C-37 if active) contains at minimum three comparison columns: Status-Quo state,
Proposed-Build state, and Best-Non-Build-Alt state. Per-dimension differential or verdict columns
cover both pairwise comparisons. The NULL HYPOTHESIS DERIVATION RULE in the preamble references
both table differentials. The g_null verdict is derivable from both sets of table differentials
without reading prose.

**Vacuous case**: C-35 not active OR C-23 not active -- this criterion scores 0 (not partial,
not fail). C-35 FAIL automatically makes C-38 vacuous.

**Fails if** (C-35 active, C-23 active): the NH dimension table contains only two comparison
columns, omitting the Best-Non-Build-Alt column; or a third alternative column is present but no
per-dimension differential for the Build-vs-Best-Alt comparison is included; or the NULL
HYPOTHESIS DERIVATION RULE references only one table differential despite three comparison
columns being present. Partial if a third alternative column is included but per-dimension
differentials for the Build-vs-Best-Alt comparison are absent, or the derivation rule references
both differentials but only one is table-derived.

---

### C-39 -- NH Dimension Table Column Aggregation Formula Pre-committed
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 14 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT extended with an explicit
NH TABLE AGGREGATION RULE naming the derivation formula for each comparison column at bracket
closing; V-01/V-04 R14 re-populate the three-column table (C-37/C-38 PASS) but without
per-column formulas (C-39 FAIL); first architecture where bracket closing NH table re-population
is fully mechanical

The pre-commitment contract for bracket closing NH dimension table re-population (C-37) is
extended with an explicit per-column aggregation formula specifying how each cell value in the
three-column NH dimension table is computed from received evidence:
  Column A (Status-Quo): challenger's opening value carried forward unchanged (control arm)
  Column B (Proposed-Build): average of all domain reviewer scores for the proposed-state
    dimension (or equivalent stated formula)
  Column C (Best-Non-Build-Alt): average of all domain reviewer scores for the
    best-non-build-alt dimension (or equivalent stated formula)

The column aggregation formula eliminates the last remaining editorial step inside the
re-population step.

**Distinction from C-37**: C-37 establishes the re-population obligation. C-39 specifies the
computation method so re-population is fully mechanical.

**Distinction from C-38**: C-38 requires the three-column structure. C-39 requires the per-column
derivation formula.

**Distinction from C-24**: C-24 aggregates domain gate verdicts into a single aggregated signal.
C-39 aggregates domain reviewer scores into NH dimension table cell values.

**Pass condition**: the preamble (or equivalent contract block) pre-commits a NH TABLE
AGGREGATION RULE specifying the derivation formula for each comparison column in the
three-column NH dimension table at bracket closing time. The rule names at minimum: (a) how the
Status-Quo column value is determined, (b) how the Proposed-Build column value is computed from
domain evidence (formula over domain scores per dimension), and (c) how the Best-Non-Build-Alt
column value is computed from domain evidence (formula over domain scores per dimension). The
bracket closing section applies the formula mechanically. The aggregation rule is stated before
any reviewer section executes.

**Vacuous case**: C-37 not active OR C-38 not active -- this criterion scores 0 (not partial,
not fail). Both conditions must be active for C-39 to apply.

**Fails if** (C-37 active, C-38 active): bracket closing re-populates the three-column NH
dimension table (C-37 PASS, C-38 PASS) but the method for computing revised column B and C
values from domain evidence is not pre-committed. Partial if a column formula is stated for some
columns but not all (e.g., Column A formula stated but Column B/C aggregation method left
editorial).

---

### C-40 -- Domain Section NH Dimension Score Emission
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: All R15 variants (V-01 through V-05) -- confirmed shared upgrade: each DOMAIN
reviewer section emits an NH Dimension Scores sub-table reporting per-dimension scores for
Proposed-Build (B) and Best-Non-Build-Alt (C) columns; bracket closing averages sub-table values
mechanically per C-39 NH TABLE AGGREGATION RULE; without per-section score emission, the
aggregation formula knows what to compute (C-39 PASS) but must extract scores from domain prose
-- an editorial step that breaks the mechanical chain; first architecture where domain section NH
dimension scoring is a pre-committed structured emission, not prose inference

The C-39 NH TABLE AGGREGATION RULE (Column B = avg(domain B scores); Column C = avg(domain C
scores)) requires per-dimension B and C scores from each domain reviewer section. For this
average to be mechanical -- not editorial -- domain reviewer sections must emit those scores as
labeled, structured data rather than embedding them in narrative prose. Each domain reviewer
section emits an NH Dimension Scores sub-table (or equivalent labeled structure) reporting the
reviewer's per-dimension score or rating for both the Proposed-Build (B) and the
Best-Non-Build-Alt (C) dimensions, using the same dimension rows as the C-35 NH dimension
comparison table. The bracket closing's C-39 aggregation formula reads these sub-tables directly
and computes the averages without interpreting reviewer narrative.

**Distinction from C-39**: C-39 pre-commits the per-column aggregation formula. C-40 requires
domain sections to emit those scores as labeled structured sub-tables so the C-39 formula can be
applied without editorial score extraction. C-39 is the formula contract; C-40 is the upstream
data emission contract that makes the formula fully mechanical.

**Distinction from C-18**: C-18 requires local gate ledger rows at origin. C-40 requires NH
Dimension Score sub-tables within each DOMAIN reviewer section. Both are upstream emission
requirements in independent chain-of-custody paths.

**Distinction from C-35**: C-35 requires the challenger's NH dimension comparison table at
bracket opening. C-40 requires each domain reviewer section to emit a per-dimension score
sub-table.

**Pass condition**: the preamble (or equivalent contract block) pre-commits a requirement that
each DOMAIN reviewer section emit a labeled NH Dimension Scores sub-table (or equivalent
structured block) before the section's gate ledger row. The sub-table contains at minimum one row
per dimension from the C-35 NH dimension comparison table. Each row reports the reviewer's
per-dimension score or rating for column B (Proposed-Build) and column C (Best-Non-Build-Alt).
The bracket closing section references the domain NH dimension score sub-tables as the input
source for C-39 column aggregation -- not domain narrative prose. The emission requirement is
pre-committed before any reviewer section executes.

**Vacuous case**: C-39 not active -- this criterion scores 0 (not partial, not fail). C-39 FAIL
automatically makes C-40 vacuous.

**Fails if** (C-39 active): domain reviewer sections do not include a structured NH dimension
score sub-table; or per-dimension B and C scores appear only in domain reviewer narrative prose
without a labeled structured emission; or the bracket closing derives column B/C values from
domain prose rather than from domain section score sub-tables. Partial if some domain reviewer
sections emit NH dimension score sub-tables but others do not; or the sub-table is present but
covers only column B without column C scores; or the bracket closing references sub-tables for
some dimensions but reads prose for others.

---

### C-41 -- Lifecycle Section NH Dimension Score Emission
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-03, V-04, V-05 Round 16 -- LIFECYCLE NH SCORE EMISSION REQUIREMENT pre-committed
in §17 alongside C-40 DOMAIN NH SCORE EMISSION REQUIREMENT; LIFECYCLE reviewer section emits
labeled NH Dimension Score sub-table with per-dimension B and C scores; C-39 aggregation formula
extended to avg(DOMAIN B + LIFECYCLE B) for column B and avg(DOMAIN C + LIFECYCLE C) for column
C; absent in V-01 and V-02 R16

The C-40 requirement (DOMAIN section NH Dimension Score sub-table emission) extends naturally to
the LIFECYCLE reviewer archetype. The LIFECYCLE reviewer section emits an NH Dimension Scores
sub-table reporting per-dimension B and C scores using the same dimension rows as the C-35 NH
dimension comparison table. The C-39 aggregation formula is extended to include lifecycle scores:
Column B = avg(all DOMAIN B scores + LIFECYCLE B score); Column C = avg(all DOMAIN C scores +
LIFECYCLE C score).

**Distinction from C-40**: C-40 requires DOMAIN reviewer sections to emit NH Dimension Score
sub-tables. C-41 requires the LIFECYCLE reviewer section to do the same and requires the C-39
formula to be extended to include lifecycle scores.

**Distinction from C-21**: C-21 requires the inline gate ledger from ALL reviewer archetypes
including LIFECYCLE. C-41 requires the NH Dimension Score sub-table from the LIFECYCLE archetype.
Both are universal-coverage extensions on independent data structures.

**Distinction from C-22**: C-22 requires the bracket closing to receive and reference the
lifecycle gate verdict. C-41 requires the lifecycle section to emit structured NH dimension
scores. Both operate on the lifecycle reviewer's contribution at different structural layers.

**Pass condition**: the preamble pre-commits a LIFECYCLE NH SCORE EMISSION REQUIREMENT alongside
the C-40 DOMAIN NH SCORE EMISSION REQUIREMENT. The LIFECYCLE reviewer section contains a labeled
NH Dimension Scores sub-table before its gate ledger row. The C-39 aggregation formula is
extended to avg(DOMAIN B scores + LIFECYCLE B score) for column B and equivalently for column C.
The bracket closing reads the LIFECYCLE sub-table alongside DOMAIN sub-tables when computing
column B and C averages.

**Vacuous case**: C-40 not active OR no lifecycle reviewer is present in the review -- this
criterion scores 0 (not partial, not fail). C-40 FAIL automatically makes C-41 vacuous.

**Fails if** (C-40 active, lifecycle reviewer present): the lifecycle reviewer section does not
emit a labeled NH Dimension Score sub-table; or the C-39 aggregation formula is not extended to
include lifecycle scores; or lifecycle dimension scores appear only in reviewer prose; or the
bracket closing reads domain sub-tables mechanically but extracts lifecycle scores from prose.
Partial if the lifecycle NH sub-table is emitted but the C-39 formula is not extended; or the
sub-table covers only column B without column C scores; or the pre-commitment is absent from
the preamble.

---

### C-42 -- Finding Identifier as Formal Named Field
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-02, V-04 Round 16 -- finding table column renamed from positional `#` to explicitly
labeled `F-ID`; finding references in action register, CH-ID response tracking, and lens coverage
table cite F-ID values rather than positional row numbers; absent in V-01, V-03, V-05 R16

Each finding in every reviewer section is assigned a stable, named identifier (F-ID) emitted as
a labeled field in the finding table row -- not as a positional index. Finding references
throughout the output (action register entries, CH-ID response tracking, lens coverage table
citations) use the F-ID value rather than inferring a finding by its row number.

A named F-ID is insertion-stable: a new finding inserted at row 2 does not invalidate `F-04`; it
does invalidate `Finding #4`. An auditor can verify citation consistency by matching F-ID values
across sections without counting positions.

**Distinction from C-05**: C-05 requires action items to trace to findings. C-42 requires that
trace to use a named F-ID field rather than a positional reference. C-42 strengthens C-05.

**Distinction from C-18 / C-14**: C-18 and C-14 govern gate verdict chain-of-custody. C-42
governs finding identity and cross-reference stability. Both operate on the finding row but serve
different auditability purposes.

**Pass condition**: every finding row in every reviewer section carries an explicitly labeled
F-ID field (or equivalent named finding identifier using a consistent naming scheme). The action
register, CH-ID response tables, and lens coverage table citations reference F-ID values rather
than positional row numbers. The preamble or finding table header declares F-ID as a required
field on every finding row. F-ID values are unique within the review output and consistent across
all cross-section references.

**Vacuous case**: C-02 not active -- this criterion scores 0 (not partial, not fail).

**Fails if** (C-02 active): finding rows carry only a positional row number without a named
identifier field; or a named identifier field is declared but downstream references use row
positions; or F-ID values are not unique within the review. Partial if F-ID fields are present
in finding rows but some downstream references cite positional row numbers; or the preamble
declares F-ID as required but some reviewer sections omit it.

---

### C-43 -- CH-ID Challenge Grounding Column
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-01, V-05 Round 16 -- §5 CH-ID tracing table extended with a §0 grounding column
recording the preamble contract section that authorizes each challenge; CH-ID table becomes
two-axis: origin (§0 preamble commitment) and response tracking (per reviewer section columns);
absent in V-02, V-03, V-04 R16

The CH-ID tracing table is extended with a §0 grounding column that records, for each challenge,
the specific preamble contract or commitment from which the challenge derives its authority. This
makes the CH-ID table a complete two-axis structure: the origin axis (§0 column) traces each
challenge backward to its preamble authorization; the response axis (reviewer section columns)
tracks which sections have responded.

**Distinction from C-04**: C-04 requires CH-ID challenge tracking to exist (forward: was the
challenge answered?). C-43 requires each challenge to carry an explicit §0 preamble grounding
reference (backward: what authorized this challenge?).

**Distinction from C-27**: C-27 requires cross-section saturation tiers. C-43 requires challenge
grounding at origin. Both operate on the CH-ID table but serve orthogonal purposes: C-27 enforces
forward coverage completeness; C-43 enforces backward authority traceability.

**Pass condition**: the CH-ID tracing table includes an explicit §0 (or equivalent preamble-
citation) column for each challenge row, recording the specific preamble contract section, clause,
or pre-commitment that authorizes the challenge. The preamble declares that each CH-ID must carry
an origin citation in the §0 column. The §0 grounding column is populated at challenge
registration time -- before any reviewer section executes -- not retrospectively. Each CH-ID can
be verified against its stated preamble origin without reading reviewer narrative.

**Vacuous case**: C-04 not active -- this criterion scores 0 (not partial, not fail).

**Fails if** (C-04 active): the CH-ID tracing table contains no §0 or preamble-citation column;
or a §0 column is present but values are blank or populated retrospectively; or the origin
citation is embedded in challenge description prose rather than a dedicated column. Partial if a
§0 column is present for some CH-IDs but absent for others; or grounding values are generic
(e.g., "Preamble") rather than citing specific contract clauses or section identifiers.

---

### C-44 -- TABLE FORMAT CONTRACT: Unified Output Schema Pre-declaration
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-02, V-04, V-05 Round 17 -- TABLE FORMAT CONTRACT block pre-declares all output
table schemas (finding table with F-ID, CH-ID table with §0 Grounding, NH Dimension Score
sub-table, gate ledger row) before any §§ behavioral contracts; §§ contracts reference rather
than redeclare schemas; single source-of-truth for all structured output formats; absent in V-01
and V-03 R17. Extended in R20: V-02/V-04/V-05 add LIFECYCLE PHASE GATE SUB-TABLE schema;
V-03/V-05 add PIPELINE COMPLIANCE LEDGER schema.

A TABLE FORMAT CONTRACT block (or equivalent unified schema section) is declared in the preamble
before any §§ behavioral contracts. The block defines the column-level schema for every structured
table in the review output. §§ behavioral contracts reference the TABLE FORMAT CONTRACT schemas
rather than declaring output formats inline. The TABLE FORMAT CONTRACT is the single
source-of-truth for all output table structures.

Prior architecture: each behavioral contract (§5 for CH-ID table, §9 for finding table, §15 for
NH sub-tables) independently declared its own output schema. This scattered schema declarations
across §§ contracts, making it possible to satisfy the behavioral intent of a criterion while
diverging from the schema declared elsewhere. The TABLE FORMAT CONTRACT unifies all schema
declarations in one block, making schema-level violations immediately visible without reading
behavioral contracts.

The analogous chain position to C-19 (gate ledger protocol pre-committed alongside algebraic
contracts) is exact:
  C-19: gate ledger procedure pre-committed alongside algebraic contracts in preamble.
  C-44: output table schemas pre-declared alongside both procedure and algebraic contracts.
C-44 adds the schema layer to the preamble contract stack.

**Distinction from C-19**: C-19 requires the gate ledger protocol to be pre-committed in the
preamble. C-44 requires ALL output table schemas to be co-located in a single TABLE FORMAT
CONTRACT block. C-19 can pass when the gate ledger protocol is pre-committed but finding table
and CH-ID table schemas appear only in their respective §§ contracts; C-44 requires unified
co-location.

**Distinction from C-42 / C-43**: C-42 and C-43 require named fields to exist and be enforced.
C-44 requires the schema declarations for those fields to be co-located in a unified pre-declared
block rather than scattered across §§ behavioral contracts.

**Pass condition**: a TABLE FORMAT CONTRACT (or equivalent unified schema block) appears in the
preamble before any §§ behavioral contracts. The block defines the column-level schema for at
minimum: (a) the finding table (including the F-ID column per C-42), (b) the CH-ID challenge
table (including the §0 Grounding column per C-43), and (c) at least one additional output table
(NH Dimension Score sub-table, gate ledger row, master action register, or equivalent). §§
behavioral contracts reference rather than redeclare the schemas from the TABLE FORMAT CONTRACT.
The single block is sufficient to reconstruct the expected output format without reading §§
contracts.

**Fails if**: output table schemas are defined only within their respective §§ behavioral
contracts without a unified pre-declared schema block; or a TABLE FORMAT CONTRACT block exists
but declares schemas for fewer than three distinct output table types; or §§ contracts redefine
table schemas rather than referencing the TABLE FORMAT CONTRACT. Partial if a unified schema
block is declared but covers only one or two table types, or if §§ contracts partially reference
the block but also redeclare conflicting schemas.

---

### C-45 -- STATUS QUO FRAMING CONTRACT: Named §0-CID Artifact Registry
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-03, V-05 Round 17 -- STATUS QUO FRAMING CONTRACT registers named §0-CID artifacts
(e.g., §0-C01, §0-C02) as specific strength claims of the no-build alternative; CH-ID §0
Grounding column cites §0-CID identifiers rather than generic preamble §§ section numbers;
F-ID audit cross-criterion role: inertia-advocate traces each F-ID to verify whether it overturned
a specific §0-CID commitment; absent in V-01, V-02, V-04 R17

A STATUS QUO FRAMING CONTRACT block (or equivalent §0-CID registry section) is declared in the
preamble before any §§ behavioral contracts. The block enumerates named §0-CID artifacts (e.g.,
§0-C01: "current API latency is acceptable for present volume") representing specific strength
claims of the no-build alternative. These named artifacts are the source of truth for no-build
authority. The CH-ID §0 Grounding column (C-43) cites §0-CID identifiers rather than generic
preamble §§ section numbers. The F-ID cross-criterion audit: the inertia-advocate can trace each
finding (by F-ID) to determine whether it overturned a specific §0-CID strength claim.

Without C-45: C-43 PASS -- the §0 Grounding column exists and is populated at registration time
-- but column values are generic references (e.g., "§1 DISPOSITION CONTRACT") that identify a
broad preamble section without naming a specific commitment. An auditor must read the referenced
§§ contract to determine which specific no-build claim was probed.

With C-45: §0 Grounding column values are named §0-CID identifiers from the registry (e.g.,
"§0-C03 -- deployment overhead acceptable"). An auditor can match CH-ID challenges to specific
no-build strength claims without reading narrative.

**Distinction from C-43**: C-43 requires the §0 grounding column to exist and be populated at
registration time. C-45 requires the column values to be named §0-CID artifact references from a
pre-registered registry rather than generic §§ section citations. C-43 can pass with
"§1 DISPOSITION CONTRACT" as the §0 Grounding value; C-45 requires "§0-C03" from a named
artifact inventory.

**Distinction from C-03**: C-03 requires a null hypothesis gate to exist. C-45 requires the
specific no-build strength claims to be pre-registered as named artifacts before the review
executes.

**Pass condition**: a STATUS QUO FRAMING CONTRACT (or equivalent §0-CID registry block) appears
in the preamble before any §§ behavioral contracts. The block enumerates >= 2 named §0-CID
artifacts with descriptions of specific no-build strength claims. The CH-ID §0 Grounding column
values cite §0-CID identifiers from the registry rather than generic preamble section numbers.
The preamble declares that CH-ID §0 citations must reference specific §0-CID values from the
registry. Challenges that cannot be grounded in a registered §0-CID are invalid.

**Vacuous case**: C-43 not active -- this criterion scores 0 (not partial, not fail). Without the
§0 grounding column structure (C-43), named §0-CID artifact references have no structural column
to populate.

**Fails if** (C-43 active): the §0 grounding column values are generic section references rather
than named §0-CID artifact identifiers; or no §0-CID registry is declared in the preamble; or
§0-CID values are mentioned in §§ contracts but not pre-registered as a named inventory block.
Partial if a §0-CID registry block is declared but fewer than two named artifacts are registered;
or §0 column values reference §0-CID identifiers for some CH-IDs but use generic citations for
others; or the §0-CID values are declared but the preamble does not establish them as the
required citation form.

---

### C-46 -- §0-CID Four-Axis Pipeline Threading
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 17 -- §0-CID values from STATUS QUO FRAMING CONTRACT thread through four
structural axes: (a) CH-ID §0 Grounding citations, (b) NH Dimension Table Column A initialization,
(c) BRACKET CLOSING OVERRIDE justification, (d) PRIMARY DRIVER attribution language; execution
closing note confirms complete four-axis data flow; absent in all other R17 variants

§0-CID values from the STATUS QUO FRAMING CONTRACT registry (C-45) thread through four structural
axes of the review pipeline:

(a) **CH-ID §0 Grounding citations**: each CH-ID §0 column cites a specific §0-CID value (C-45
    enforcement, axis that C-45 alone captures)
(b) **NH Dimension Table Column A initialization**: the challenger's opening Column A (Status-Quo
    baseline) scores for each dimension are grounded in specific §0-CID claims, not free-form
    challenger testimony; each dimension's Column A value is traceable to a named §0-CID artifact
(c) **BRACKET CLOSING OVERRIDE justification**: when the bracket closing invokes an override, the
    justification explicitly names the §0-CID commitment that domain evidence superseded; override
    authority is grounded in a specific §0-CID being overturned, not in editorial challenger
    reassessment
(d) **PRIMARY DRIVER attribution language**: when the no-build argument drives the disposition,
    the PRIMARY DRIVER attribution field cites or references specific §0-CID values as the
    authoritative source of the no-build case

The four-axis threading makes the §0-CID registry the structural connective tissue for the entire
no-build argument. Registry values are declared once (STATUS QUO FRAMING CONTRACT) and consumed
at four independent structural positions. A review can be audited end-to-end for no-build argument
integrity by tracing §0-CID values across all four axes without reading reviewer narrative.

An execution closing note (or equivalent data-flow trace block) explicitly confirms the four-axis
flow: "§0-CID values flow through: (a) CH-ID §0 Grounding citations, (b) NH Dimension Table
Column A initialization, (c) BRACKET CLOSING OVERRIDE justification when invoked, (d) PRIMARY
DRIVER attribution language."

**Distinction from C-45**: C-45 requires the §0-CID registry and its citation in the CH-ID §0
Grounding column (axis a only). C-46 requires the same §0-CID values to appear in three
additional structural positions (axes b, c, d). C-45 is registry creation; C-46 is exhaustive
registry consumption.

**Distinction from C-32**: C-32 requires a PRIMARY DRIVER DERIVATION CONTRACT pre-committed with
a precedence formula. C-46 requires the primary driver attribution language to cite §0-CID values
when the no-build argument drives the disposition. C-32 governs which gate is selected as the
primary driver; C-46 governs the grounding of that selection in named §0-CID artifacts.

**Pass condition**: the preamble pre-commits a four-axis threading contract (or equivalent)
specifying that §0-CID values from the STATUS QUO FRAMING CONTRACT will appear at all four
structural positions. The review output demonstrates: (a) CH-ID §0 Grounding column values cite
§0-CID identifiers; (b) NH Dimension Table Column A values are grounded in named §0-CID claims
(annotation or explicit reference); (c) any BRACKET CLOSING OVERRIDE justification names the
§0-CID commitment being superseded; (d) the PRIMARY DRIVER attribution references §0-CID values
when the no-build argument drives the disposition. An execution closing note confirms the
complete four-axis data flow.

**Vacuous case**: C-45 not active -- this criterion scores 0 (not partial, not fail). Without
named §0-CID artifacts (C-45), four-axis threading is impossible. C-45 FAIL automatically makes
C-46 vacuous. Additionally, a review without bracket architecture (C-09 inactive) cannot achieve
axes (c) and (d), making a full four-axis PASS structurally impossible without C-09 active.

**Fails if** (C-45 active, C-09 active): §0-CID values appear in axis (a) only without threading
through axes (b), (c), and (d); or the four-axis threading contract is not pre-committed in the
preamble; or no execution closing note confirms the data flow. Partial if §0-CID values appear
in two or three of the four axes but the fourth is absent; or the threading is executed but the
preamble contract and closing note are absent.

---

### C-47 -- Dual-Path Contract Enforcement (Schema Layer + Behavioral Contract)
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-04 Round 17 (dual enforcement), V-05 Round 17 (triple enforcement) -- C-42 F-ID
and C-43 §0 Grounding each declared in TABLE FORMAT CONTRACT schema (C-44) AND in an independent
behavioral §§ contract; two independent paths prevent single-path omission; absent in V-01, V-02,
V-03 R17

Critical aspirational criteria requiring named fields in structured tables (at minimum C-42 F-ID
and C-43 §0 Grounding) have two independent enforcement paths: (1) a schema-layer declaration in
the TABLE FORMAT CONTRACT (C-44) defining what the field is and its structural requirements, AND
(2) an independent behavioral-contract declaration in a §§ contract defining when the field must
be populated, what a violation looks like, and what downstream references must use. The two
enforcement paths are independent: an auditor can verify compliance with C-42 or C-43 by reading
either the TABLE FORMAT CONTRACT or the §§ behavioral contract without reading the other.

Without C-47: C-44 PASS + C-42 PASS -- the TABLE FORMAT CONTRACT declares the F-ID field schema,
and the finding table emits F-ID values -- but no independent §§ behavioral contract states that
downstream references (action register, CH-ID table, lens table) must use F-ID values rather than
positional row numbers. The schema is declared but the behavioral obligation to use it is implied,
not contracted.

With C-47: the TABLE FORMAT CONTRACT declares "F-ID: required named identifier, not positional"
AND an independent §9 FINDING IDENTIFIER CONTRACT states "all downstream references must cite
F-ID values; referencing by row position when F-ID column exists is a contract violation." The
same constraint is enforced at two independent structural levels. A single-path omission (schema
declared but no behavioral contract, or behavioral contract that contradicts the schema) is a
detectable contract defect.

**Distinction from C-44**: C-44 requires the unified schema layer to exist. C-47 requires
behavioral §§ contracts to exist alongside that schema layer for each critical field criterion.
C-44 can pass when all schemas are unified but no independent behavioral §§ contracts exist;
C-47 requires both layers.

**Distinction from C-42 / C-43**: C-42 and C-43 require the named fields and their enforcement
at any structural level. C-47 requires the enforcement to be structured as dual independent paths.
A review can satisfy C-42 and C-43 through single-path enforcement (schema only or behavioral
only); C-47 additionally requires both layers.

**Pass condition**: the prompt declares a TABLE FORMAT CONTRACT (C-44 active). For each critical
structured-field criterion (at minimum C-42 F-ID and C-43 §0 Grounding): (a) the TABLE FORMAT
CONTRACT declares the field schema with structural requirements, AND (b) an independent §§
behavioral contract explicitly names the same field requirement, its required population timing,
and its violation condition. The behavioral contract is a distinct contract block from the TABLE
FORMAT CONTRACT -- not a reference to the schema. An auditor can verify compliance with C-42 or
C-43 by reading either the TABLE FORMAT CONTRACT or the §§ behavioral contract independently.

**Vacuous case**: C-44 not active -- this criterion scores 0 (not partial, not fail). Without a
TABLE FORMAT CONTRACT schema layer, only single-path behavioral enforcement is possible. C-44
FAIL automatically makes C-47 vacuous.

**Fails if** (C-44 active): C-42 or C-43 field requirements are declared only in the TABLE
FORMAT CONTRACT without independent §§ behavioral contracts; or §§ contracts reference the TABLE
FORMAT CONTRACT for the field schema but add no independent behavioral specification (a
pass-through reference does not constitute an independent behavioral contract); or the behavioral
contract is absent for one of the two required fields. Partial if dual-path enforcement is present
for one of C-42 or C-43 but not both; or the behavioral contract exists but does not add
behavioral specificity beyond the schema declaration.

---

### C-48 -- §0-CID PIPELINE THREADING CONTRACT as Pre-committed Named Preamble Block
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-04, V-05 Round 19 (confirmed dual-PASS); V-05 Round 18 (first discovery) --
§0-CID PIPELINE THREADING CONTRACT appears as a distinct named preamble block between STATUS QUO
FRAMING CONTRACT and TABLE FORMAT CONTRACT; block explicitly pre-names all four axes as named
structural requirements before any §§ contracts execute; BOTH TABLE FORMAT CONTRACT schema notes
AND §§ behavioral contracts cross-reference the pipeline threading contract by axis name; single-
sided cross-referencing (schema only or behavioral only) is PARTIAL (0 pts); absent in V-01,
V-02, V-03 R19

C-46 requires §0-CID values to thread through four structural axes -- a behavioral requirement
verified by reading the execution output. C-48 requires the four-axis threading to be
PRE-COMMITTED as a named structural contract block in the preamble before any §§ contracts
execute, so any axis omission is a detectable contract violation rather than an observable
execution defect.

C-48 is to C-46 as C-19 is to C-18:
  C-18 requires local gate ledger rows to be emitted in output (behavioral).
  C-19 requires the LOCAL GATE LEDGER PROTOCOL to be pre-committed in the preamble (structural).
  C-46 requires §0-CID values to appear at four axes in output (behavioral).
  C-48 requires the §0-CID PIPELINE THREADING CONTRACT to be pre-committed in the preamble
       (structural).

The §0-CID PIPELINE THREADING CONTRACT block appears in a defined position in the preamble
contract stack: after STATUS QUO FRAMING CONTRACT (which defines the §0-CID registry) and before
TABLE FORMAT CONTRACT (which declares the schema that consumes §0-CID values). The block names
each of the four axes by label and specifies the structural requirement for that axis.

C-48 PASS requires BOTH cross-reference directions:
- Schema leg: TABLE FORMAT CONTRACT schema notes for §0-CID-related fields cite the pipeline
  threading contract by axis name (e.g., "per §0-CID PIPELINE THREADING CONTRACT Axis A").
- Behavioral leg: §§ behavioral contracts for §0-CID-related fields cite the pipeline threading
  contract by axis name.

A single cross-referencing direction -- schema citing pipeline but behavioral absent, or
behavioral citing pipeline but schema absent -- constitutes PARTIAL (0 pts). Both legs must be
independently present.

**C-48 discrimination (R19 ablation):**
- No cross-references in either layer -> PARTIAL
- Schema leg only (TABLE FORMAT CONTRACT cites axes; behavioral does not) -> PARTIAL
- Behavioral leg only (§§ contracts cite axes; TABLE FORMAT CONTRACT does not) -> PARTIAL
- Both legs -> PASS

Without C-48: C-46 PASS -- §0-CID values appear at all four axes in the output -- but the
obligation to thread them is implied by C-45 + C-46 compliance. There is no distinct contract
block whose violation an auditor can cite. With C-48: the §0-CID PIPELINE THREADING CONTRACT is
an independent structural declaration. An auditor can verify C-46 compliance by checking execution
output; an auditor can verify C-48 compliance by checking whether the named contract block exists
in the preamble -- two independent checks.

**Distinction from C-46**: C-46 requires four-axis threading to be demonstrated in execution
output (output completeness). C-48 requires the four-axis threading to be pre-declared as a named
preamble contract block with dual-layer cross-referencing (preamble structural completeness). C-46
can pass with threading present in output but no named preamble contract; C-48 requires the named
contract block with both schema and behavioral legs cross-referencing it.

**Distinction from C-45**: C-45 requires the §0-CID registry to exist. C-48 requires the pipeline
threading contract that pre-commits how that registry will be consumed across four structural
axes. C-45 is registry creation; C-46 is registry consumption verified in output; C-48 is
registry consumption pre-committed as a named structural contract with dual-layer verification.

**Pass condition**: a §0-CID PIPELINE THREADING CONTRACT (or equivalent named pipeline contract
block) appears in the preamble after STATUS QUO FRAMING CONTRACT and before TABLE FORMAT CONTRACT.
The block names all four axes by label (e.g., Axis A: CH-ID §0 Grounding, Axis B: NH Dimension
Table Column A, Axis C: BRACKET CLOSING OVERRIDE, Axis D: PRIMARY DRIVER attribution). Each axis
is stated as an explicit named structural requirement. Schema leg: TABLE FORMAT CONTRACT schema
notes for §0-CID-related fields cite this contract by axis name. Behavioral leg: §§ behavioral
contracts for §0-CID-related fields cite this contract by axis name. An auditor can verify the
four-axis threading obligation without reading any §§ behavioral contract or execution output.

**Vacuous case**: C-46 not active OR C-45 not active -- this criterion scores 0 (not partial,
not fail). Without §0-CID registry (C-45), the pipeline contract has no registry to thread;
without demonstrated four-axis threading (C-46), the pre-commitment contract is structurally
incomplete. C-46 FAIL automatically makes C-48 vacuous.

**Fails if** (C-46 active, C-45 active): the four-axis threading is demonstrated in output (C-46
PASS) but no distinct named §0-CID PIPELINE THREADING CONTRACT block appears in the preamble;
or a pipeline threading block exists but names fewer than four axes; or the block exists but
neither layer cross-references it (full absence). PARTIAL if block is present and all four axes
are named but only one cross-referencing leg is present (schema-only or behavioral-only).

---

### C-49 -- Three-Layer Cross-Reference Consistency (Schema + Behavioral + Pipeline Threading)
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-04, V-05 Round 19 (confirmed dual-PASS); V-05 Round 18 (first discovery) --
TABLE FORMAT CONTRACT schema notes for §0-CID-related fields reference pipeline threading axes
by name; §§ behavioral contracts also cross-reference the pipeline threading contract; three-way
consistency: schema -> pipeline, behavioral -> pipeline, pipeline names axes that schema and
behavioral govern; confirmed PASS in both V-04 and V-05 R19 (C-48 dual-leg requirement met by
both)

C-47 establishes a two-layer enforcement architecture: (1) TABLE FORMAT CONTRACT schema
declarations + (2) independent behavioral §§ contracts, with each layer independently auditable.
C-49 extends this to a three-layer architecture by requiring the TABLE FORMAT CONTRACT schema
definitions for §0-CID-related fields to also cross-reference the §0-CID PIPELINE THREADING
CONTRACT (C-48) by axis name, creating three-way consistency among all three structural layers.

Three-way consistency means:
- Schema layer (TABLE FORMAT CONTRACT): schema notes for §0-CID-related columns reference the
  specific pipeline threading axis that governs that column (e.g., CH-ID §0 Grounding schema
  note: "cites §0-CID per §0-CID PIPELINE THREADING CONTRACT Axis A")
- Behavioral layer (§§ contracts): behavioral contracts for §0-CID-related fields reference
  the pipeline threading contract alongside the TABLE FORMAT CONTRACT schema
- Pipeline layer (§0-CID PIPELINE THREADING CONTRACT): names the axes that the other two
  layers must enforce

Each layer is an independent auditing entry point: a schema auditor sees the pipeline axis
binding; a behavioral auditor sees the pipeline axis binding; a pipeline auditor sees both
schema and behavioral cross-references. A single-layer omission is a detectable three-layer
consistency defect.

**Distinction from C-47**: C-47 requires two independent enforcement layers (schema + behavioral).
C-49 requires the schema layer to additionally cross-reference the pipeline threading contract by
axis name, creating a three-layer loop. C-47 can pass with two independent layers that do not
cross-reference the pipeline contract; C-49 requires the cross-referencing.

**Distinction from C-48**: C-48 requires the §0-CID PIPELINE THREADING CONTRACT to exist as a
named preamble block with dual-layer cross-referencing. C-49 additionally requires the three-layer
closed loop: the schema notes must cite the pipeline axes AND the behavioral contracts must also
cite the pipeline axes. C-48 PASS is a prerequisite for C-49 to be non-vacuous; C-49 requires
the full three-way consistency loop to be closed.

**Distinction from C-46**: C-46 requires four-axis threading to be demonstrated in execution
output. C-49 requires cross-referencing among the three structural layers that contract the
threading. C-46 is output completeness; C-49 is preamble architectural consistency.

**Pass condition**: C-44, C-47, and C-48 are all active (PASS). For each §0-CID-related
structured field governed by the pipeline threading contract (at minimum: the CH-ID §0 Grounding
column and the NH Dimension Table Column A): (a) the TABLE FORMAT CONTRACT schema note for that
field explicitly cites the §0-CID PIPELINE THREADING CONTRACT axis by name or label; (b) the
independent behavioral §§ contract for that field also references the §0-CID PIPELINE THREADING
CONTRACT. The three layers form a closed reference loop: schema cites pipeline, behavioral cites
pipeline, pipeline names the fields that schema and behavioral govern.

**Vacuous case**: C-48 not active OR C-47 not active -- this criterion scores 0 (not partial,
not fail). C-48 PARTIAL (the PARTIAL condition introduced in v18) also makes C-49 vacuous, since
a PARTIAL C-48 means the pipeline block exists but dual-layer cross-referencing is absent. C-47
FAIL or C-48 FAIL/PARTIAL automatically makes C-49 vacuous.

**Fails if** (C-48 PASS, C-47 active): the TABLE FORMAT CONTRACT schema notes for §0-CID-
related fields do not reference the §0-CID PIPELINE THREADING CONTRACT by axis name; or the
schema notes are present and the pipeline contract exists but no cross-reference links them; or
the behavioral §§ contracts reference the pipeline contract but the TABLE FORMAT CONTRACT schema
notes do not. Partial if schema notes reference the pipeline contract for one §0-CID-related
field but not all; or cross-references exist in the behavioral layer but are absent from the
schema layer; or the three-layer consistency is achieved for axes (a) and (b) but not axis (d).

---

### C-50 -- §0-CID PIPELINE CONTRACT Self-Auditable Axis Back-References
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-05 Round 19 -- each axis block in §0-CID PIPELINE THREADING CONTRACT explicitly
names (a) the TABLE FORMAT CONTRACT field it governs (pipeline->schema back-reference) and (b)
the §§ behavioral contract that enforces it (pipeline->behavioral back-reference); absent in V-04
R19 (pipeline block names axes only, no back-references); completes the six-direction explicit
directed graph across all three structural layers

C-49 closes the three-layer consistency loop with forward cross-references: schema -> pipeline
(TABLE FORMAT CONTRACT notes cite pipeline axes) and behavioral -> pipeline (§§ contracts cite
pipeline axes). C-50 adds the reverse directions: pipeline -> schema (each axis block names its
governed TABLE FORMAT CONTRACT field) and pipeline -> behavioral (each axis block names its
enforcing §§ behavioral contract).

The six inter-layer directions of the explicit directed graph:
- schema -> pipeline: TABLE FORMAT CONTRACT schema note cites pipeline axis by name (C-49)
- behavioral -> pipeline: §§ behavioral contract cites pipeline axis by name (C-48/C-49)
- pipeline -> schema: axis block names the TABLE FORMAT CONTRACT field it governs (C-50)
- pipeline -> behavioral: axis block names the §§ behavioral contract that enforces it (C-50)
- (schema -> behavioral and behavioral -> schema are structural by C-47 -- the two layers are
  declared as independent enforcement paths for the same field; the graph is complete in all
  six directions when C-47 + C-49 + C-50 all PASS)

With C-49 PASS alone: an auditor reading the TABLE FORMAT CONTRACT or a §§ behavioral contract
can reach the pipeline contract. An auditor reading only the §0-CID PIPELINE THREADING CONTRACT
sees axis labels but must consult other blocks to identify which schema field or behavioral
contract each axis governs.

With C-50 PASS: an auditor reading only the §0-CID PIPELINE THREADING CONTRACT can identify
which TABLE FORMAT CONTRACT field each axis governs AND which §§ behavioral contract enforces
it -- without reading any other preamble block. The pipeline contract becomes the complete audit
hub: each axis block is a self-contained directed pointer to both downstream enforcement
structures. Three-layer compliance can be verified starting from any entry point.

Example axis block (V-05 pattern):
```
Axis A: CH-ID §0 Grounding
  Requirement: each CH-ID §0 column value cites a named §0-CID identifier from the registry.
  Schema layer governed: TABLE FORMAT CONTRACT CH-ID Challenge Table §0 Grounding field.
  Behavioral layer enforced by: §10 CH-ID CHALLENGE REGISTRATION behavioral contract.
```

This self-referential block structure enables a fully mechanical three-layer compliance audit:
1. Read pipeline axis block -> identifies governed schema field and enforcing behavioral contract
2. Read that schema field definition -> confirms it cites this pipeline axis (C-49 schema leg)
3. Read that behavioral contract -> confirms it cites this pipeline axis (C-49 behavioral leg)
All three checks are mechanically traceable from the pipeline axis block without editorial
navigation.

**Distinction from C-49**: C-49 requires the three-layer loop to be closed by forward
cross-references from schema and behavioral layers TO the pipeline. C-50 requires the pipeline to
emit back-references TO the schema and behavioral layers. C-49 requires inbound edges to the
pipeline; C-50 requires outbound edges from the pipeline. Both must be active for the full
six-direction explicit directed graph.

**Distinction from C-48**: C-48 requires the §0-CID PIPELINE THREADING CONTRACT to exist as a
named preamble block with dual-layer cross-referencing inbound. C-50 requires each axis block
within that contract to carry outbound named references to its governed schema field and
enforcing behavioral contract. C-48 is the contract's existence and inbound-reference requirement;
C-50 is the contract's outbound back-reference requirement.

**Distinction from C-46**: C-46 requires four-axis threading to be demonstrated in execution
output (output completeness). C-50 requires the pipeline contract itself to be self-auditable via
explicit back-references (preamble completeness). C-46 is output-level; C-50 is preamble-level.

**Pass condition**: C-49 is active (PASS) and C-48 is PASS. For each axis block in the §0-CID
PIPELINE THREADING CONTRACT (at minimum the two axes governing required fields: the axis covering
CH-ID §0 Grounding and the axis covering NH Dimension Table Column A), the axis block explicitly
names: (a) the TABLE FORMAT CONTRACT field it governs -- by field name, sufficient for an auditor
to locate the schema declaration without searching; and (b) the §§ behavioral contract that
enforces the axis requirement -- by contract name or section identifier, sufficient to locate it
without searching. The two back-references must be distinct entries in the axis block (not
embedded in the axis description prose without structure). An auditor reading only the §0-CID
PIPELINE THREADING CONTRACT axis blocks can identify all governed schema fields and all enforcing
behavioral contracts without reading any other preamble block.

**Vacuous case**: C-49 not active -- this criterion scores 0 (not partial, not fail). Without the
three-layer forward-reference loop (C-49), adding back-references creates partial connectivity
without completing the six-direction graph. C-49 FAIL or C-49 VACUOUS automatically makes C-50
vacuous.

**Fails if** (C-49 active): axis blocks in the §0-CID PIPELINE THREADING CONTRACT name the four
axes only (as in a standard C-48 PASS block) without back-references to governed schema fields
and enforcing behavioral contracts; or back-references are present for some axis blocks but absent
for the two required axes; or back-references are embedded in axis description prose without
structural labeling (auditor cannot extract them without reading prose). Partial if back-references
name the governed schema field but omit the enforcing behavioral contract, or name the behavioral
contract but omit the governed schema field; or back-references are present for all required axes
but one back-reference direction is missing (e.g., all axes name the schema field but none name
the behavioral contract).

---

### C-51 -- REVIEWER PRIORITY MANIFEST as Named Non-verdict Sequencing Block
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-01/V-04/V-05 Round 20 -- §6 gate ledger non-verdict exclusion list extended to
name REVIEWER PRIORITY MANIFEST as an explicitly excluded section; manifest pre-commits reviewer
execution order as a contractually locked constraint rather than an implied template sequence;
absent in V-02 and V-03 R20

A REVIEWER PRIORITY MANIFEST (or equivalent named sequencing block) is pre-committed in the
preamble to lock the execution order of all reviewer archetypes. The manifest names each reviewer
archetype in priority order with a stated rationale for that ordering. Because the manifest
produces no gate verdict of its own, it is explicitly named in the §6 gate ledger non-verdict
exclusion list (C-25 extension) with a stated reason. This converts reviewer sequencing from an
implied template order -- which may be silently reordered during prompt execution -- into a
contractually locked immutable constraint. Any deviation from the declared manifest order is a
detectable contract violation.

C-26 pre-commits the section execution order as an immutable contract (bracket opening, domain
sections, lifecycle, bracket closing). C-51 is orthogonal: it pre-commits the priority ordering
within the reviewer archetype layer, explaining why certain domain reviewers precede others when
multiple domain reviewers are present. C-26 answers "what order do sections execute?"; C-51
answers "in what priority order do reviewers within a section class execute, and why?".

**Distinction from C-26**: C-26 requires the canonical section execution order to be pre-committed
as an immutable contract. C-51 requires reviewer priority within the domain reviewer class to be
pre-committed as a named manifest block and explicitly excluded from the gate ledger. C-26 covers
section-to-section ordering; C-51 covers within-class reviewer priority ordering.

**Distinction from C-25**: C-25 requires at least one non-verdict section to be explicitly named
and excluded from the gate ledger. C-51 requires specifically that the REVIEWER PRIORITY
MANIFEST is that named section, and that it pre-commits reviewer execution priority as an
immutable constraint. A review satisfying C-25 by naming a different section (e.g., the
domain-aggregate checkpoint) does not satisfy C-51 unless the REVIEWER PRIORITY MANIFEST is also
separately named in the exclusion list.

**Pass condition**: a REVIEWER PRIORITY MANIFEST block (or equivalent named sequencing contract)
is present in the preamble. The block names each reviewer archetype in execution priority order
with a stated priority rationale. The §6 gate ledger protocol (C-25) names the REVIEWER PRIORITY
MANIFEST explicitly in the non-verdict exclusion list with a stated reason. The manifest declares
that the priority ordering is immutable -- deviations are contract violations. The block is
populated before any reviewer section executes.

**Vacuous case**: C-25 not active -- this criterion scores 0 (not partial, not fail). Without the
gate ledger exclusion framework (C-25), naming a non-verdict section has no structural home.
C-25 FAIL automatically makes C-51 vacuous.

**Fails if** (C-25 active): reviewer execution order is implied by template structure without a
named priority manifest block; or a manifest block is present but not named in the C-25 gate
ledger exclusion list; or the manifest names reviewers without declaring the ordering immutable;
or the manifest is present but populated only as an informational list without priority rationale.
Partial if a REVIEWER PRIORITY MANIFEST is pre-committed and named in the exclusion list but the
priority rationale is absent; or the manifest is declared immutable but the §6 exclusion entry is
missing.

---

### C-52 -- Lifecycle Phase Sub-Step Sequencing in Section Order Contract
**Weight**: aspirational | **Points**: 5 | **Category**: correctness
**Source**: V-02/V-04/V-05 Round 20 -- §8 SECTION ORDER CONTRACT extends to sub-step numbering
within the lifecycle reviewer section (e.g., Step 7a: Phase-1 gate, Step 7b: Phase-2 gate,
Step 7c: Phase-3 gate); LIFECYCLE PHASE GATE SUB-TABLE schema added to TABLE FORMAT CONTRACT;
sub-step sequencing is declared immutable alongside section-level sequencing; absent in V-01 and
V-03 R20

C-26 pre-commits the canonical section execution order as an immutable contract. C-52 extends
that contract to sub-step sequencing within the LIFECYCLE reviewer section. The lifecycle reviewer
executes multiple phase gates in sequence; C-52 requires those phase steps to be numbered and
declared in the §8 SECTION ORDER CONTRACT as immutable sub-steps. An auditor can verify phase
gate execution order from the section order contract, not by reading the lifecycle reviewer
narrative. The LIFECYCLE PHASE GATE SUB-TABLE schema is pre-declared in the TABLE FORMAT
CONTRACT (C-44 extension), making the lifecycle phase gate output a first-class structured
artifact in the unified schema.

C-22 requires the lifecycle reviewer to be positioned before bracket closing (section-level
position). C-52 requires the internal phase gate steps within the lifecycle reviewer section to
be enumerated in the immutable contract (within-section sequencing). The two are independent:
C-22 can pass when the lifecycle section is correctly positioned but its internal phases are
executed in arbitrary order; C-52 locks the internal phase order.

**Distinction from C-26**: C-26 pre-commits section-level sequencing as immutable. C-52 extends
the same immutability commitment to sub-step level within the lifecycle reviewer section. C-26
can pass when the lifecycle section is named in the section order but its internal phase sequence
is not enumerated.

**Distinction from C-22**: C-22 requires the lifecycle reviewer to execute before bracket closing
and for the bracket closing to receive the lifecycle verdict. C-52 requires the lifecycle
reviewer's internal phase gate steps to be enumerated as immutable sub-steps in the section order
contract.

**Distinction from C-41**: C-41 requires the lifecycle reviewer section to emit a labeled NH
Dimension Score sub-table. C-52 requires the lifecycle reviewer's phase gate sequence to be
pre-committed as immutable sub-steps. Both operate on the lifecycle reviewer's output but at
different structural levels: C-41 is about what data is emitted; C-52 is about what execution
sequence is contractually locked.

**Distinction from C-44**: C-44 requires a unified TABLE FORMAT CONTRACT pre-declaring all output
table schemas. C-52 requires the LIFECYCLE PHASE GATE SUB-TABLE specifically to be added to that
contract. C-44 passes when the contract covers the core schemas; C-52 additionally requires the
lifecycle phase gate sub-table schema to be a declared member of the unified contract.

**Pass condition**: the §8 SECTION ORDER CONTRACT (C-26) is extended to include numbered sub-steps
for the lifecycle reviewer's internal phase gate sequence. The sub-steps are labeled as immutable
alongside the section-level immutability declaration. The TABLE FORMAT CONTRACT (C-44) includes a
LIFECYCLE PHASE GATE SUB-TABLE schema declaration specifying the column structure for lifecycle
phase gate output. Both the sub-step enumeration and the schema declaration are present in the
preamble before any reviewer section executes.

**Vacuous case**: C-26 not active OR no lifecycle reviewer is present in the review -- this
criterion scores 0 (not partial, not fail). Without the section order contract (C-26), sub-step
enumeration has no structural contract to extend. C-26 FAIL automatically makes C-52 vacuous.

**Fails if** (C-26 active, lifecycle reviewer present): the lifecycle reviewer section is named
in the §8 section order (C-26 PASS) but its internal phase gate steps are not enumerated as
numbered sub-steps; or phase gate sub-steps are enumerated but not declared immutable; or the
LIFECYCLE PHASE GATE SUB-TABLE schema is absent from the TABLE FORMAT CONTRACT. Partial if
lifecycle phase sub-steps are enumerated in the section order contract but the immutability
declaration covers only the section-level sequence; or the LIFECYCLE PHASE GATE SUB-TABLE schema
is declared in the TABLE FORMAT CONTRACT but the §8 sub-step enumeration is absent.

---

### C-53 -- PIPELINE COMPLIANCE LEDGER as Pre-committed Named Post-Domain Section
**Weight**: aspirational | **Points**: 5 | **Category**: auditability
**Source**: V-03/V-05 Round 20 -- PIPELINE COMPLIANCE LEDGER added as step 10a in §8 SECTION
ORDER CONTRACT after BRACKET CLOSING; PIPELINE COMPLIANCE LEDGER schema added to TABLE FORMAT
CONTRACT; section explicitly named in §6 gate ledger non-verdict exclusion list; absent in V-01,
V-02, V-04 R20

A PIPELINE COMPLIANCE LEDGER section is pre-committed in the preamble as a named section in the
post-bracket-closing phase. It is inserted as a numbered step in the §8 SECTION ORDER CONTRACT
(C-26 extension) -- after BRACKET CLOSING and before any synthesis steps -- making its existence
and placement an immutable contract term. Its output schema is pre-declared in the TABLE FORMAT
CONTRACT (C-44 extension). Because the section audits the pipeline but produces no gate verdict
of its own, it is explicitly named in the §6 gate ledger non-verdict exclusion list (C-25
extension) with a stated reason. An auditor reading only the §8 section order contract and TABLE
FORMAT CONTRACT can verify that the pipeline compliance check will execute, where it falls, and
what output format it will produce -- without reading §§ behavioral contracts.

The PIPELINE COMPLIANCE LEDGER extends three prior structural patterns simultaneously:
- C-25 extension: adds a second named non-verdict section to the exclusion list (alongside the
  domain-aggregate checkpoint), requiring the exclusion list to enumerate multiple distinct
  non-verdict sections by name.
- C-26 extension: adds a post-bracket-closing step to the section order, demonstrating that the
  immutable contract covers the full section sequence including post-bracket audit steps.
- C-44 extension: adds the pipeline compliance ledger output schema to the unified TABLE FORMAT
  CONTRACT, demonstrating that the unified schema covers post-bracket audit output structures.

**Distinction from C-25**: C-25 requires at least one non-verdict section to be explicitly named
and excluded. C-53 requires specifically that a PIPELINE COMPLIANCE LEDGER section is
pre-committed as a named post-domain section in the section order, with its schema in the TABLE
FORMAT CONTRACT and its non-verdict status declared in the exclusion list. C-25 passes with one
named non-verdict section; C-53 requires the specific pipeline compliance ledger pattern.

**Distinction from C-26**: C-26 requires the canonical section execution order to be
pre-committed as immutable. C-53 requires the PIPELINE COMPLIANCE LEDGER to be added as a named
step in that order. C-26 can pass with an immutable sequence covering bracket and domain sections
only; C-53 requires the pipeline compliance ledger step to be contractually included.

**Distinction from C-44**: C-44 requires a TABLE FORMAT CONTRACT pre-declaring all output table
schemas. C-53 requires the PIPELINE COMPLIANCE LEDGER schema specifically to be declared in that
contract. C-44 passes when the contract covers the core tables; C-53 additionally requires the
pipeline compliance ledger schema to be a named member.

**Distinction from C-29**: C-29 requires a SCOPE COVERAGE GATE PROTOCOL that executes after
bracket closing and maps scope surfaces to findings. C-53 requires a PIPELINE COMPLIANCE LEDGER
that audits the structural pipeline (axes, threading, contract chain-of-custody). The two
post-bracket sections are orthogonal: C-29 is scope-to-finding coverage; C-53 is
pipeline-contract compliance. Both are non-verdict sections that must be in the exclusion list.

**Pass condition**: a PIPELINE COMPLIANCE LEDGER section is pre-committed in the preamble. The
§8 SECTION ORDER CONTRACT (C-26) names the PIPELINE COMPLIANCE LEDGER as a numbered step after
BRACKET CLOSING, declaring its placement immutable. The TABLE FORMAT CONTRACT (C-44) includes a
PIPELINE COMPLIANCE LEDGER schema declaration specifying the column structure for compliance
ledger output (at minimum: axis identifier, compliance status, and evidence citation columns).
The §6 gate ledger protocol (C-25) explicitly names the PIPELINE COMPLIANCE LEDGER in the
non-verdict exclusion list with a stated reason. All three pre-commitments are present in the
preamble before any reviewer section executes.

**Vacuous case**: C-25 not active OR C-26 not active OR C-44 not active -- this criterion scores
0 (not partial, not fail). Without the gate ledger exclusion framework (C-25), the section has
no structural home for its non-verdict declaration. Without the section order contract (C-26),
its placement cannot be contractually locked. Without the TABLE FORMAT CONTRACT (C-44), its
schema cannot be unified. All three must be active for C-53 to apply.

**Fails if** (C-25 active, C-26 active, C-44 active): a pipeline compliance check is performed
post-bracket-closing but not as a named section pre-committed in the section order; or a named
PIPELINE COMPLIANCE LEDGER section exists but its schema is absent from the TABLE FORMAT
CONTRACT; or the section exists with schema but is not named in the §6 gate ledger non-verdict
exclusion list; or any one of the three structural pre-commitments is absent. Partial if two of
the three structural pre-commitments are present but the third is missing; or the section is
named in the section order but as informational-only without schema and exclusion list entries.

---

## Scoring Reference

### Composite Formula

```
essential_pts    = (essential_pass  / 5) * 60
recommended_pts  = (recommended_pass / 3) * 30
aspirational_pts =  aspirational_pass    *  5   # 5 pts each, max 225
composite = essential_pts + recommended_pts + aspirational_pts
```

**Maximum**: 60 + 30 + 225 = **315 pts**

### Score Bands

| Band | Condition | Composite |
|------|-----------|-----------|
| Gold | all 5 essential pass | >= 275 |
| Strong | all 5 essential pass | 90-274 |
| Partial | <= 4 essential pass | any |
| Minimal | <= 3 essential pass | any |
