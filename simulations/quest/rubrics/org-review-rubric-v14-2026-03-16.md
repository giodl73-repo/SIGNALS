Written to `simulations/quest/rubrics/org-review-rubric-v14-2026-03-16.md` (74 KB).

---

**v14 summary:**

**New criterion: C-40 -- Domain Section NH Dimension Score Emission** (5 pts, aspirational, auditability)

Extracted from the R15 "DOMAIN section NH Dimension Scores sub-table (C-39 chain)" confirmed shared upgrade. The analogy is exact:

| Chain | Origin emission | Formula consumer | Protected by |
|-------|----------------|-----------------|--------------|
| Gate ledger | C-18 (local ledger row) | C-14 (master register) | C-20 (verbatim copy prohibition) |
| NH table | **C-40** (domain score sub-table) | C-39 (column aggregation) | -- |

Without C-40: C-39 knows the averaging formula but must extract per-dimension B and C scores from domain prose — an editorial step. With C-40: domain sections emit labeled sub-tables; bracket closing reads them directly and averages mechanically.

**Score changes:** Aspirational 31→32 | Max 245→250 | Gold threshold 210→215

**R14 under v14:** V-05/V-01/V-04 drop to 245/240/240 (C-40 FAIL — C-39 pre-committed but no sub-table emission). V-02/V-03 unchanged (C-40 vacuous via C-39).

**R15 under v14:** All five variants 250/250. The NH evaluation trajectory is now fully mechanical end-to-end: C-35 → C-37 → C-38 → C-23 → C-39 → C-40.
 aggregation) to be
        a mechanical average with no editorial extraction step

**Vacuous condition:** C-39 not active. Without a pre-committed per-column aggregation formula
(C-39), domain section score emission has no mechanical consumer; C-40 is vacuous.

**Score changes:**
- Aspirational: 31 -> 32
- Max: 245 -> 250
- Gold threshold: 210 -> 215

**R15 ranking under v14:**

| Rank | Variant | Score |
|------|---------|-------|
| 1 (tie) | V-01 R15 | **250/250** |
| 1 (tie) | V-02 R15 | **250/250** |
| 1 (tie) | V-03 R15 | **250/250** |
| 1 (tie) | V-04 R15 | **250/250** |
| 1 (tie) | V-05 R15 | **250/250** |

All five R15 variations achieve 250/250 -- first perfect score under v14.

**R15 score computation (baseline = V-05 R14 under v13 = 245):**

| Variant | C-40 | Delta | v14 Score |
|---------|------|-------|-----------|
| **V-01** | PASS (+5) | +5 | **250/250** |
| **V-02** | PASS (+5) | +5 | **250/250** |
| **V-03** | PASS (+5) | +5 | **250/250** |
| **V-04** | PASS (+5) | +5 | **250/250** |
| **V-05** | PASS (+5) | +5 | **250/250** |

Gold delta matches the 5 pt pattern for a single-criterion increment. 210 -> 215.

**C-40 PASS (all R15 variants):** Each DOMAIN reviewer section emits a labeled NH Dimension
Scores sub-table reporting per-dimension B (Proposed-Build) and C (Best-Non-Build-Alt) scores.
Bracket closing reads sub-tables directly, applies C-39 averaging formula mechanically, and
re-populates columns B and C without prose extraction. No editorial step in the chain.

**C-40 FAIL (V-05, V-01, V-04 R14):** Three-column NH table re-populated at bracket closing
with C-39 per-column aggregation formula (C-39 PASS), but domain reviewer sections do not emit
labeled NH Dimension Score sub-tables. Bracket closing must extract per-dimension B and C scores
from domain prose. Editorial extraction step present; C-40 FAIL.

**C-40 vacuous (V-02, V-03 R14):** C-39 vacuous (C-38 FAIL) -> C-40 vacuous.

No retroactive score changes on R1--R14. R14 v13 scores carry forward unchanged.

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

## Aspirational Criteria -- 160 pts (structural integrity, auditability, automation)

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

### C-27 -- CH-ID Cross-Section Saturation Pre-committed as Requirement
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

The analogy to C-18 (inline gate ledger at origin) is precise:
  C-18 requires local gate ledger rows at origin so C-14 (master register) is a verbatim copy,
    not a re-derivation. C-20 protects that chain against re-derivation at assembly.
  C-40 requires domain NH dimension score sub-tables at origin so C-39 (column aggregation) is a
    verbatim average, not a prose-extraction step. The C-39 formula becomes a copy-and-average,
    not an editorial inference.

Without C-40: C-39 PASS + C-37 PASS + C-38 PASS -- the bracket closing knows the formula and
the three-column table structure, but must scan domain reviewer narrative to extract per-dimension
B and C scores. Score selection from narrative is an editorial step: different AI runs may extract
different scores for the same prose, producing different averages.

With C-40: each domain reviewer section contains a labeled sub-table of per-dimension B and C
scores. The bracket closing reads the sub-tables, computes averages by formula, and re-populates
columns B and C mechanically. No prose interpretation required at any step in the NH chain.

**Distinction from C-39**: C-39 pre-commits the per-column aggregation formula (how columns B
and C are computed from domain scores). C-40 requires domain sections to emit those scores as
labeled structured sub-tables so the C-39 formula can be applied without editorial score
extraction. C-39 can pass when the bracket closing applies a pre-committed averaging formula but
extracts input scores from domain prose; C-40 additionally requires the input scores to be
structured emissions. C-39 is the formula contract; C-40 is the upstream data emission contract
that makes the formula fully mechanical.

**Distinction from C-18**: C-18 requires local gate ledger rows (Gate Verdict + Class) at the
end of each reviewer section. C-40 requires NH Dimension Score sub-tables (per-dimension B and C
scores) within each DOMAIN reviewer section. Both are upstream emission requirements in
independent chain-of-custody paths: C-18 feeds the gate ledger chain; C-40 feeds the NH table
aggregation chain.

**Distinction from C-35**: C-35 requires the challenger's NH dimension comparison table at
bracket opening (pre-domain gate format). C-40 requires each domain reviewer section to emit a
per-dimension score sub-table (mid-review data supply for bracket closing). C-35 is a format
requirement on the challenger's opening evaluation; C-40 is a data emission requirement on domain
reviewers' section outputs.

**Pass condition**: the preamble (or equivalent contract block) pre-commits a requirement that
each DOMAIN reviewer section emit a labeled NH Dimension Scores sub-table (or equivalent
structured block) before the section's gate ledger row. The sub-table contains at minimum one row
per dimension from the C-35 NH dimension comparison table. Each row reports the reviewer's
per-dimension score or rating for column B (Proposed-Build) and column C (Best-Non-Build-Alt).
The bracket closing section references the domain NH dimension score sub-tables as the input
source for C-39 column aggregation -- not domain narrative prose. The emission requirement is
pre-committed before any reviewer section executes.

**Vacuous case**: C-39 not active -- this criterion scores 0 (not partial, not fail). Without a
pre-committed per-column aggregation formula (C-39), domain section NH dimension score emission
has no mechanical consumer. C-39 FAIL automatically makes C-40 vacuous.

**Fails if** (C-39 active): domain reviewer sections do not include a structured NH dimension
score sub-table; or per-dimension B and C scores appear only in domain reviewer narrative prose
without a labeled structured emission; or the bracket closing derives column B/C values from
domain prose rather than from domain section score sub-tables. Partial if some domain reviewer
sections emit NH dimension score sub-tables but others do not; or the sub-table is present but
covers only column B without column C scores; or the bracket closing references sub-tables for
some dimensions but reads prose for others.

---

## Scoring Reference

### Composite Formula

```
essential_pts    = (essential_pass  / 5) * 60
recommended_pts  = (recommended_pass / 3) * 30
aspirational_pts =  aspirational_pass    *  5   # 5 pts each, max 160
composite = essential_pts + recommended_pts + aspirational_pts
```

**Maximum**: 60 + 30 + 160 = **250 pts**

### Score Bands

| Band | Condition | Composite |
|------|-----------|-----------|
| Gold | all 5 essential pass | >= 215 |
| Strong | all 5 essential pass | 90-214 |
| Partial | <= 4 essential pass | any |
| Minimal | <= 3 essential pass | any |

### Paths to Gold (215 pts)

| Path | Essential | Rec | Asp passed | Composite |
|------|-----------|-----|------------|-----------|
| Full rec + 25 asp | 5/5 | 3/3 | 25/32 | 60+30+125 = 215 |
| 2 rec + 27 asp | 5/5 | 2/3 | 27/32 | 60+20+135 = 215 |
| 1 rec + 29 asp | 5/5 | 1/3 | 29/32 | 60+10+145 = 215 |
| 0 rec + 31 asp | 5/5 | 0/3 | 31/32 | 60+0+155 = 215 |

### Round 11 Calibration (retroactive, v10 -> v14)

All R11 variants: C-33/C-34/C-35 absent -> C-36 through C-40 all vacuous or FAIL.
No retroactive score change; all R11 v11 scores carry forward unchanged.

### Round 12 Calibration (retroactive, v11 -> v14)

C-36/C-37/C-38/C-39 status same as v13 assessment. C-40: C-39 vacuous or FAIL in all R12
variants -> C-40 vacuous. No retroactive score change until R12 full text review.

### Round 13 Calibration (v11 -> v14)

| Variant | v11 | C-36 | C-37 | C-38 | C-39 | C-40 | v14 |
|---------|-----|------|------|------|------|------|-----|
| **V-05** | 220 | PASS (+5) | PASS (+5) | FAIL | vac | vac | **230/250** |
| **V-03** | 220 | PASS (+5) | vac | vac | vac | vac | **225/250** |
| V-04 | 215 | FAIL | PASS (+5) | FAIL | vac | vac | **220/250** |
| V-02 | 215 | FAIL | vac | vac | vac | vac | **215/250** |
| V-01 | 210 | FAIL | PASS (+5) | FAIL | vac | vac | **215/250** |

C-39/C-40 vacuous for all R13 variants: C-38 FAIL in every variant.

### Round 14 Calibration (v13 -> v14)

Baseline = V-05 R13 under v13 = 245. C-40 is the only open criterion for R14 variants.

| Variant | v13 | C-40 | v14 |
|---------|-----|------|-----|
| **V-05** | 245 | FAIL (0) | **245/250** |
| **V-01** | 240 | FAIL (0) | **240/250** |
| **V-04** | 240 | FAIL (0) | **240/250** |
| **V-02** | 235 | vac (0) | **235/250** |
| **V-03** | 230 | vac (0) | **230/250** |

**C-40 FAIL (V-05, V-01, V-04 R14):** C-39 PASS (per-column aggregation formula pre-committed),
but domain reviewer sections do not emit labeled NH Dimension Score sub-tables. Bracket closing
must extract per-dimension B and C scores from domain prose. Editorial extraction step present.

**C-40 vacuous (V-02, V-03 R14):** C-39 vacuous (C-38 FAIL) -> C-40 vacuous.

### Round 15 Calibration (v13 -> v14)

Baseline = V-05 R14 under v13 = 245. C-40 is the only open criterion in v14 for R15 variants.

| Variant | v13 | C-40 | v14 |
|---------|-----|------|-----|
| **V-01** | 245 | PASS (+5) | **250/250** |
| **V-02** | 245 | PASS (+5) | **250/250** |
| **V-03** | 245 | PASS (+5) | **250/250** |
| **V-04** | 245 | PASS (+5) | **250/250** |
| **V-05** | 245 | PASS (+5) | **250/250** |

**C-40 PASS (all R15 variants):** Each DOMAIN reviewer section emits a labeled NH Dimension
Scores sub-table reporting per-dimension B (Proposed-Build) and C (Best-Non-Build-Alt) scores.
Bracket closing reads sub-tables directly, applies C-39 averaging formula mechanically, and
re-populates columns B and C without prose extraction. No editorial step in the chain.

All five R15 variants achieve the maximum score. The NH dimension table chain is now fully
mechanical from domain section emission (C-40) through column formula (C-39) through
three-column structure (C-38) through pairwise derivation rule (C-23) through bracket closing
re-population (C-37) through opening table format (C-35). Every editorial step in the NH
evaluation trajectory has been eliminated.

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
C-29 vacuous (C-09 inactive OR no scope enumeration) = 0, not partial.
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
C-40 vacuous (C-39 inactive) = 0, not partial.
