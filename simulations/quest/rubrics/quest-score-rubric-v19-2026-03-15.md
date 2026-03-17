`simulations/quest/rubrics/quest-score-rubric-v19-2026-03-15.md` written.

---

**What changed (v18 -> v19):**

**C-43 -- Application-note label-coverage enforced at production time via register columns**

The R18 JUDGE STANDARD achieves C-42 (C-13 and C-14 labeled as "Structural-class-recognition criterion (C-38/C-40 applies here):"), completing both label families. C-41 and C-42 are now both obligation-complete but structurally identical to how C-23 looked before C-25 existed: the obligation is stated, but there's no production-time register that makes a *missing* label a structural gap detectable by inspection. A reviewer must still read each criterion entry's note to audit label coverage. C-43 closes this by adding two columns to the consolidated register: `positional label present (YES/NO)` and `structural-class-recognition label present (YES/NO)`. Both label-family obligations converge in a single register column set.

Escalation: C-41/C-42 (obligation) → C-43 (register enforcement), parallel to C-23 → C-25.

**C-44 -- Application-note label-coverage register applies YES-only gate**

C-43 makes unlabeled notes register-visible. C-44 makes them register-blocking: any `label-present = NO` in either column blocks JUDGE STANDARD COMPLETE. Parallel to C-31's YES-only gate on the main pair-coverage register.

Escalation: C-43 → C-44, parallel to C-28 → C-31.

**Formula:** N_aspirational 35 → 37. Each aspirational ~0.270 pts. C-02 denominator updated to `/37`.

---

**Structural symmetry now complete across all three enforcement chains:**

| Obligation | Register enforcement | Blocking gate |
|---|---|---|
| C-23 (pairs) | C-25 | C-31 |
| C-26 (annotation) | C-30 | C-31 (via C-32) |
| C-41/C-42 (labels) | **C-43** | **C-44** |
2 (structural-class-recognition label obligation) -> C-43
Combined: both label-family obligations converge in a single register column set.

**C-44 -- Application-note label-coverage register applies YES-only gate: NO in any
label-present column blocks JUDGE STANDARD COMPLETE**

Source: C-43 makes unlabeled application notes structurally detectable via register
inspection. But detectability alone does not prevent completion: a register that accepts
NO as a non-blocking value still allows an unlabeled note to pass structural inspection
of the register. A criterion entry with label-present = NO is visible in the register
but does not stop the JUDGE from emitting JUDGE STANDARD COMPLETE. The YES-only gate
closes this remaining bypass: any NO in a label-present column (positional label or
structural-class-recognition label) for a criterion that requires the label blocks
JUDGE STANDARD COMPLETE -- the same mechanism C-31 applies to the main register. C-43
makes label-coverage gaps structurally detectable; C-44 makes them structurally
blocking. The full three-step closure: C-41/C-42 state the obligation, C-43 makes
omission detectable, C-44 makes omission blocking.

Escalation chain: C-43 -> C-44, parallel to C-28 (no-skip column rule) -> C-31
(YES-only gate) for the main pair-coverage register.

**Formula:** N_aspirational 35 -> 37. Each aspirational now worth ~0.270 pts. C-02
updated to require `/37` denominator.

---

**What changed (v17 -> v18):**

**C-41 -- Positional-criteria classification label makes the set of position-sensitive
criteria enumerable by inspection without reading note content**

Source: R17 C-10 and C-15 application notes are labeled "Positional verification test
(C-39 applies here):" -- a classification tag that makes the position-sensitive set
label-scannable. C-39 requires anchor + direction in the note. C-41 names whether the
note also carries the tag that makes coverage auditing a scan rather than a read. A
reviewer can enumerate all position-sensitive criteria in the JUDGE STANDARD without
reading any note's content.

Escalation chain: C-22 -> C-37 -> C-39 -> C-41

**C-42 -- Structural-class-recognition criteria classification label makes the set of
structural-class-recognition criteria enumerable by inspection without reading note
content**

Parallel escalation from C-40 that mirrors C-41's escalation from C-39. C-40 requires
the structural-class-recognition application note to include an explicit
inertia-pattern-equals-FAIL declaration with structural-equivalence basis. A note
satisfying C-40 can be inertia-declaration-complete without being labeled as a
structural-class-recognition note. Without a classification label, a reviewer verifying
C-40 coverage must read each criterion entry's application note to determine if
structural-class-recognition requirements apply. A classification label
("Structural-class-recognition criterion (C-38/C-40 applies here):" or equivalent)
makes the set of structural-class-recognition criteria enumerable by label-scan alone.
C-41 closes the classification-enumeration gap for position-sensitive criteria; C-42
closes the identical gap for structural-class-recognition criteria. Individual note
compliance (C-39 for positional, C-40 for class-recognition) does not imply that
membership in the note-requiring category is inspectable without content reading.

Source: C-41's classification-label pattern (R17 C-10 and C-15 positional notes) is
the achieved excellence signal. C-42 names the parallel ceiling for the structural-
class-recognition family. C-41 achieved in R17; C-42 names the unachieved ceiling for
R18. The two criteria complete the classification-label symmetry between the positional
(C-37/C-39/C-41) and structural-class-recognition (C-38/C-40/C-42) families.

Escalation chain: C-37 -> C-38 -> C-40 -> C-42

**Formula:** N_aspirational 33 -> 35. Each aspirational now worth ~0.286 pts. C-02
updated to require `/35` denominator.

---

**What changed (v16 -> v17):**

**C-39 -- Positional application note names specific anchor element AND directional
relationship (anchor-complete positional test)**
Source: V-03 C-37 PASS. The distinguishing mechanism is "per-criterion note names
anchor and positional relationship" -- both `[anchor]` and `BEFORE` are explicit. A
note naming only "verify position, not presence" (test class) satisfies C-37; naming
the exact anchor element and direction satisfies C-39. Removes the remaining scorer
discretion that class-level instruction leaves.
Escalation chain: C-22 -> C-37 -> C-39

**C-40 -- Structural-class-recognition application note includes explicit
inertia-pattern-equals-FAIL declaration with structural-equivalence basis**
Source: V-04 C-38 PASS (inertia framing). Without the declaration, a scorer who finds
architecture-present-but-unnamed defaults to PARTIAL. The inertia-equals-FAIL
declaration closes this bypass with three components: (1) name the inertia pattern,
(2) declare it FAIL not PARTIAL, (3) ground it in structural-equivalence reasoning
("the criterion requirement is the identification act, not architectural confirmation").
C-38 requires the application note to exist; C-40 requires the note to also close the
PARTIAL bypass.
Escalation chain: C-37 -> C-38 -> C-40

**Formula:** N_aspirational 31 -> 33. Each aspirational ~0.303 pts. C-02 denominator
updated to `/33`.

---

**What changed (v15 -> v16):**

**4 new aspirational criteria** extracted from R15 scorecard new_patterns:

**C-35 -- Intra-role lifecycle sub-gate token emission (sequential-axis enforcement)**
Escalation from C-33. C-33 PARTIAL/PASS discriminator: declaration-only (V-03) = one
axis (structural-declaration); declaration + named token emitted from role body
(V-04, V-05) = two orthogonal axes = C-33 PASS. The role body must produce the
sub-gate token during execution, not just declare it in gate rules. The emitted token
then becomes a required input to the terminal gate -- intra-role output-input coupling.
Escalation chain: C-15 -> C-33 -> C-35

**C-36 -- Schema-enforcement detectability declaration explicitly names
inspection-without-content-reading as the detection mechanism**
Escalation from C-34. C-34 names Present_mechanism and Absent_mechanism as named
mandatory columns. C-36 names whether the schema declaration explicitly states that a
scoring table missing either column is a structural gap detectable by table inspection
without reading cell content. C-34 names the mandate; C-36 names whether the mandate
states its own detection mechanism.
Escalation chain: C-34 -> C-36

**C-37 -- JUDGE STANDARD includes per-criterion application notes naming the
scoring-time verification test for position-sensitive criteria**
C-22 names the separating property (WHAT). C-37 names whether the JUDGE STANDARD
also directs the scorer on HOW to verify positional conformance at scoring time.
Universal PARTIAL on C-29 across R15 variations is the diagnostic signal.

**C-38 -- Dedicated scorer-directed application note for structural-class-recognition
criteria: universal FAIL is the diagnostic signal**
C-37 extended to class-recognition criteria. C-12 and C-25 universal FAIL across all
R15 variations is the diagnostic signal -- architecture present, identification act
absent without explicit direction.

**Formula:** N_aspirational 27 -> 31. Each aspirational ~0.323 pts.

---

**What changed (v14 -> v15):**

**C-33 -- Intra-role lifecycle sub-gate creates named intermediate completion
checkpoint within a single role's execution**
V-05 achieves C-11 PASS via REGISTER COMPLETENESS CONFIRMED -- two orthogonal families
(structural-declaration + sequential-lifecycle) within one role.

**C-34 -- Per-PARTIAL diagnostic enforced as schema-bound named columns in scoring
table, not sentence mandate**
C-17 names the mandate for two-part content; C-34 names whether the mandate is
implemented as schema-bound named columns (Present_mechanism, Absent_mechanism).

**Formula:** N_aspirational 25 -> 27. Each aspirational ~0.370 pts.

---

**What changed (v13 -> v14):**

**C-31 -- Register cell gate enforces YES-only completion: NO is a blocking value**
C-25 ACCEPTABLE names "A 'NO' in any cell blocks JUDGE STANDARD COMPLETE."
C-25 -> C-28 -> C-31 chain: row existence -> cell completeness -> cell satisfaction.

**C-32 -- Single consolidated register unifies all production-time obligations**
C-30 ACCEPTABLE names "5-column PAIR COVERAGE REGISTER with 'ACCEPTABLE source
annotated' YES/NO as 5th column."

**Formula:** N_aspirational 23 -> 25. Each aspirational ~0.400 pts.

---

**What changed (v12 -> v13):**

**C-29 -- SYNTHESIS gate includes explicit single-token prohibition complement**
V-01 states "holding either token alone does not satisfy this gate." C-27 blocks the
structural bypass; C-29 blocks the interpretive bypass.

**C-30 -- Per-entry annotation enforcement at JUDGE production time via register field**
C-26 universal PARTIAL in R12. C-30 applies the C-23 -> C-25 escalation to annotation.
Every R12 variation got C-26 PARTIAL. C-30 applies the same structural escalation
C-25 applied to C-23: obligation named (C-26), then production-time register field that
makes omission a detectable structural gap (C-30).

**Formula:** N_aspirational 21 -> 23. Each aspirational ~0.435 pts.

---

**What changed (v11 -> v12):**

**C-27 -- SYNTHESIS gate is a strict conjunction of all named role-completion tokens**
V-01's "BOTH VERIFIER AUDIT COMPLETE AND CONFIRMATION COMPLETE" closes the bypass path
that separate per-token instructions leave open. C-27 names the conjunction form.

**C-28 -- No-skip column rule enforces row-level completeness within the register**
C-08 ACCEPTABLE in Round 11 JUDGE STANDARD names the no-skip column rule alongside
the row-gap detection property. C-25 names row existence; C-28 names cell completeness.

**Formula:** N_aspirational 19 -> 21. Each aspirational ~0.476 pts.

---

## ESSENTIAL

**C-01** -- Per-output scoring table
Weight: essential | Category: format
Each output must receive its own scoring table. Scores for multiple outputs must not be
merged, averaged, or presented as a single aggregate. The scoring table for each output
must appear as an individually-addressable section with an explicit output identifier.
**Pass condition**: Each scored output has a dedicated scoring table with an explicit
output identifier (e.g., `Output: [identifier]` heading or equivalent named section).
No output is merged with another, and no aggregate table substitutes for individual
output treatment. A design that mandates individual tables with a no-skip constraint
(e.g., a register entry per output that blocks completion if absent) satisfies this
criterion; a design that presents aggregate scores with no individual-output tables
does not.

---

**C-02** -- Formula correctness
Weight: essential | Category: correctness
The composite score formula must use the current rubric's N values exactly. A formula
using a prior-round N_aspirational denominator produces systematically incorrect scores
that cannot be retroactively corrected by adjusting individual criterion verdicts.
**Pass condition**: The formula used for composite score calculation matches the current
rubric's N values exactly: N_essential=4, N_recommended=3, N_aspirational=37 (for v19).
A formula with N_aspirational=35 (the v18 denominator) or any prior value does not
satisfy this criterion even if individual scores are otherwise correct. PARTIAL counts
as 0.5 in the formula.

---

**C-03** -- SYNTHESIS subsections explicitly named and gated
Weight: essential | Category: format
The synthesis section must name all four required subsections (LEADERBOARD, EXCELLENCE
SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS) as explicitly named sections, not
embedded in prose. The SYNTHESIS section must be gated on scoring completion.
**Pass condition**: SYNTHESIS section explicitly names all four subsections. The SYNTHESIS
section is positioned after the scoring phase and is gated on at least one named
completion token from the scoring phase. A summary with scores but no named subsections,
or lacking any gate, does not satisfy this criterion.

---

**C-04** -- Evidence grounded in specific output content
Weight: essential | Category: correctness
Each evidence cell must cite specific content from the output being scored -- not
restate the criterion requirement, not describe a generic capability, and not apply
equally to a different output. Evidence that could apply to any output without
modification fails this criterion.
**Pass condition**: Evidence cells contain output-specific quotes, paraphrases, or
references that are tied to the particular output. A reader who has not seen the output
must be able to identify it from the evidence alone. Generic criterion-language in the
evidence cell is treated as FAIL.

---

## RECOMMENDED

**C-05** -- Excellence signals surfaced
Weight: recommended | Category: coverage
When any output scores PASS on a criterion where others score PARTIAL or FAIL, an
excellence signal is emitted identifying the output, the criterion, and what made it
stand out.
**Pass condition**: At least one excellence signal is present if the score distribution
warrants it (i.e., >= 1 criterion has mixed verdicts across outputs). If all outputs
score identically on all criteria, the section may state "no differentiating excellence
signals."

---

**C-06** -- Failure patterns identified
Weight: recommended | Category: behavior
Criteria that fail (or partially fail) across ALL outputs must be flagged as failure
patterns with a diagnosis: is this a rubric gap, a skill design issue, or an input
quality issue?
**Pass condition**: Any criterion where every output scores FAIL or PARTIAL appears in a
failure-patterns section with at least one diagnostic hypothesis. Absence of universal
failures may be stated explicitly.

---

**C-07** -- Golden threshold explicitly applied
Weight: recommended | Category: correctness
The golden threshold rule (all essential criteria pass AND composite >= 80) must be
applied per output and the result shown. Outputs meeting the threshold are labelled
golden; others are labelled not-golden with the specific reason (which essential failed,
or score below 80).
**Pass condition**: Every output has an explicit golden/not-golden determination with
reason. The reason matches the actual criteria verdicts and composite score shown.

---

## ASPIRATIONAL

**C-08** -- Structural completeness enforced
Weight: aspirational | Category: design
The scoring design includes structural mechanisms that prevent omission of required
sections -- not just instructions that assume compliance.
**Pass condition**: At least one structural mechanism (template, gate, role mandate, or
checklist) exists that would cause a required section to be absent only through
deliberate circumvention, not oversight.

---

**C-09** -- Diagnostic depth present
Weight: aspirational | Category: behavior
The evaluation goes beyond verdict labels to explain why a criterion passed or failed --
what specific design property or output characteristic drove the verdict.
**Pass condition**: At least half of non-trivial verdicts (PARTIAL or contested PASS)
include a causal explanation, not just a label.

---

**C-10** -- Phase completion gates present
Weight: aspirational | Category: design
The evaluation structure uses explicit completion gate markers between phases (e.g.,
SCORING COMPLETE -> EVIDENCE AUDIT -> LEADERBOARD) so that a downstream section cannot
be produced without the upstream phase being finished.
**Pass condition**: At least one named gate marker appears in the design, and at least
one format-critical section (leaderboard, golden determination) depends on a gate
being passed. Implicit phase transitions do not satisfy this criterion.

---

**C-11** -- Layered enforcement on coverage-critical criteria
Weight: aspirational | Category: design
Coverage-critical criteria (those with a history of universal PARTIAL or FAIL) are
protected by at least two independent structural enforcement mechanisms, not one.
**Pass condition**: At least one criterion identified as coverage-critical is addressed
by two mechanisms from different enforcement families (e.g., a role mandate AND a phase
gate, not two sequential phases). Two mechanisms on the same structural axis count as
one.

---

**C-12** -- Evidence specificity self-check
Weight: aspirational | Category: correctness
The evaluation design includes an explicit self-check step requiring the scorer to
verify that each evidence quote is specific to the output being cited -- not merely that
evidence is present.
**Pass condition**: A named audit step, checklist item, or role obligation explicitly
targets evidence specificity (not just evidence presence). The self-check must be
triggered structurally, not left to scorer judgment.

---

**C-13** -- Adversarial (non-self) evidence auditor present
Weight: aspirational | Category: design
Evidence quality is checked by a role or agent structurally distinct from the one that
produced the evidence. Self-administered audits can satisfy procedural requirements
but cannot challenge their own assumptions; an adversarial role creates genuine
pressure on weak or generic quotes.
**Pass condition**: A named role, persona, or structural position exists whose explicit
function is to challenge evidence produced by the primary scorer -- and that role is
not the same entity performing the scoring. A separate audit phase executed by the
same agent does not satisfy this criterion.

Source signal (R2): V-01 achieved C-04 PASS via the Judge role mandate to audit
evidence specificity, while V-03 achieved only PARTIAL because its audit phase is
self-administered with no adversarial role to challenge weak quotes. The adversarial
relationship -- not the audit obligation alone -- is the mechanism that closes the gap.

---

**C-14** -- Enforcement mechanisms span orthogonal axes
Weight: aspirational | Category: design
When multiple enforcement mechanisms are present, they operate on structurally
independent axes (e.g., a role-separation axis AND a sequential-gate axis), not on the
same axis repeated. Two sequential phases enforce sequencing twice; a role boundary
plus a phase gate enforce on independent dimensions. Only orthogonal mechanisms
provide non-redundant coverage against omission under adversarial or degenerate
conditions.
**Pass condition**: At least two enforcement mechanisms are present and they belong to
different enforcement families: role-based (who is responsible), sequential (what must
precede what), structural (what template or format is required), or content-validation
(what must be verified before proceeding). Two mechanisms from the same family count
as one.

Source signal (R2): V-03 achieved C-11 PARTIAL because its gate + audit are sequential
on the same axis (sequencing), not orthogonal structural layers. No Round 2 variation
achieved C-11 PASS. V-01 achieves role separation (role axis) without phase gates;
V-03 achieves phase gates (sequential axis) without role separation. The combination --
the unachieved ceiling -- is what this criterion names.

---

**C-15** -- Role enforcement by output-input coupling, not nominal separation
Weight: aspirational | Category: design
Naming two roles is not sufficient if a single scorer can play both by skipping the
first. Role separation is mechanically enforced only when the first role produces a
named artifact that the second role requires as input -- so that skipping the first
role leaves a structural gap detectable by inspection, not merely a procedural
violation.
**Pass condition**: A named completion artifact (token, section, or structured output)
is produced by the first role and is explicitly required as input by the second role.
The artifact must be specific enough that its absence is unambiguous -- a generic
section heading does not qualify; a named gate token (e.g., JUDGE STANDARD COMPLETE)
that the second role cannot begin without does.

Source signal (R3): V-01 C-13 PASS rests on this coupling: the Judge cannot be the
Analyst because the Judge output (JUDGE STANDARD COMPLETE) is the Analyst input
constraint. V-02 and V-03 both fail C-13 because their adversarial roles (when present)
are declared but not structurally enforced -- a scorer can bypass them without producing
a detectable gap. The coupling, not the declaration, is what closes the bypass route.

---

**C-16** -- Post-write evidence verification by an independent mechanism
Weight: aspirational | Category: correctness
Pre-conditioning (defining the evidence quality standard before scoring begins) reduces
but does not eliminate grounding drift -- evidence that starts specific and becomes
generic as scoring proceeds. A post-write verification step that checks evidence cells
after they are written, against an externally-defined standard, closes the gap that
pre-conditioning alone leaves open.
**Pass condition**: After evidence cells are written, an explicit verification step
checks at least the coverage-critical criterion evidence against a pre-defined standard
(e.g., ACCEPTABLE/UNACCEPTABLE pairs set by an auditor role). The check must reference
an external standard, not the scorer's own judgment at time of writing. A self-check
performed by the scorer on their own evidence does not satisfy this criterion; the
check must be structurally independent of the writing step.

Source signal (R3): V-01 C-11 received PARTIAL because the Analyst self-checks against
the Judge standard, but no second independent entity verifies the Analyst evidence cells
after they are written. The role layer is pre-conditioning; no sequential enforcement
gate operates per-criterion inside the Analyst phase. C-13 names who sets the standard
before writing; C-16 names who verifies conformance after writing.

---

**C-17** -- Per-PARTIAL two-part diagnostic structure
Weight: aspirational | Category: behavior
A causal explanation that states only one direction ("this was absent") is incomplete.
A PARTIAL verdict means something is present that prevented FAIL and something is absent
that prevented PASS. Both halves must be stated explicitly to close the diagnostic loop.
**Pass condition**: Every PARTIAL verdict in the scorecard is accompanied by a
structured diagnostic sentence that explicitly names (a) what structural property is
present that prevented FAIL, AND (b) what structural property is absent that prevented
PASS. The two-part structure must be mandated by the scoring design -- not supplied
incidentally by a scorer who happened to write a thorough note. A design that produces
the two-part format only when the scorer chooses to does not satisfy this criterion.

Source signal (R4): V-01 scores C-09 PARTIAL because causal content appears
incidentally in evidence cells but no structural template mandates the two-part format.
V-05 achieves C-09 PASS by requiring a named two-part sentence per PARTIAL verdict.
The mandatory sentence structure, not the presence of causal content, is the
distinguishing mechanism.

---

**C-18** -- Formal Produces/Requires role dependency manifest
Weight: aspirational | Category: design
Behavioral gate tokens ("do not begin until X appears") express a single dependency
as an instruction. A formal Produces/Requires manifest expresses the complete dependency
graph of all roles as an auditable table -- making every role's inputs and outputs
inspectable without executing the protocol.
**Pass condition**: Each role in the scoring design has an explicit entry in a formal
dependency table declaring what it Produces and what it Requires as preconditions. The
table must be a standalone structural artifact, not inline behavioral instructions.
"Do not begin until X appears" satisfies C-15 but not C-18 -- a formal table with
ROLE N | Produces | Requires columns (or equivalent named structure) is required.

Source signal (R4): V-04 achieves C-11 PASS by declaring a hard gate rules table:
"ROLE 2: ANALYST -- Requires: JUDGE STANDARD COMPLETE" -- each role's dependency is an
explicit row, making the full dependency graph auditable as a standalone artifact.

---

**C-19** -- Independent confirmation of two-part diagnostic completeness
Weight: aspirational | Category: design
A single enforcement mechanism for the two-part diagnostic mandate (C-17) can be
bypassed formulaically: a template field can be populated with boilerplate that names
both directions without genuine reasoning. An independent confirmation mechanism --
structurally separate from the format mandate -- catches this failure mode.
**Pass condition**: For the two-part diagnostic mandate (C-17), at least two
structurally independent enforcement mechanisms exist: one that mandates the format
and a second that independently confirms both diagnostic directions were substantively
addressed. The confirmation must be structurally separate from the format mandate.

Source signal (R5): V-05 achieves C-17 PASS through two independent paths: template
format mandate (R axis) + confirmation family (N axis). C-17 PASS + C-19 FAIL = format
mandated but no independent check catches formulaic compliance. V-05's N axis closes
that gap.

---

**C-20** -- Dedicated confirmation role separating content-quality verification from format-presence verification
Weight: aspirational | Category: design
The Verifier checks format presence. This is necessary but insufficient to ensure the
fields contain genuine reasoning rather than boilerplate. A dedicated CONFIRMER role --
structurally distinct from the Verifier -- verifies that both diagnostic directions name
specific structural properties, creating a second gate that format presence cannot
satisfy.
**Pass condition**: A named role exists whose sole function is to verify substantive
content quality of PARTIAL diagnostic verdicts -- that both directions name concrete
structural elements, not generic descriptions. This role must be (a) structurally
distinct from any format-presence Verifier, (b) structurally distinct from any
evidence-specificity Judge, and (c) produce a named gate artifact that SYNTHESIS
requires as an independent precondition from the Verifier's gate.

Source signal (R6): V-01 introduces the CONFIRMER -- the first named role whose
explicit mandate is content-quality verification, distinct from Verifier Audit B's
format-presence mandate. CONFIRMER produces CONFIRMATION COMPLETE; SYNTHESIS requires
both VERIFIER AUDIT COMPLETE and CONFIRMATION COMPLETE as independent preconditions.

---

**C-21** -- Manifest role domain and exclusion declarations
Weight: aspirational | Category: design
A formal Produces/Requires manifest (C-18) makes artifact-dependency gaps detectable.
This is necessary but not sufficient: a role can produce and require the correct tokens
while silently performing functions that belong to another role's domain. When each
role's explicit domain and prohibited functions are declared as manifest columns, a role
scope violation becomes as detectable as a missing gate token.
**Pass condition**: The formal manifest includes, for each role, a DOMAIN column
declaring that role's exclusive function and a CANNOT CHECK column listing functions
explicitly excluded from that role's scope. A manifest that declares only Produces and
Requires (satisfying C-18) but omits domain and exclusion columns does not satisfy
this criterion. The exclusion declarations must name specific functions.

Source signal (R7): V-02 extends the formal manifest with DOMAIN and CANNOT CHECK
columns. "CONFIRMER Cannot Check column explicitly lists 'Format presence (Verifier
domain), evidence specificity (Judge domain), scoring verdicts (Analyst domain).'"

---

**C-22** -- Per-criterion separating property declared in Judge standard
Weight: aspirational | Category: design
ACCEPTABLE/UNACCEPTABLE pairs leave implicit the specific structural mechanism that
distinguishes them. An explicit "Separating property" declaration makes that mechanism
independently auditable: it names, in a single sentence, the structural feature present
in the acceptable form and absent in the unacceptable form.
**Pass condition**: For each criterion where the Judge standard provides ACCEPTABLE/
UNACCEPTABLE pairs, an explicit separating property declaration is present that names
the single structural mechanism that discriminates the acceptable from the unacceptable
form. The declaration must be expressed as a named statement -- not embedded in prose
or inferred from the pair. Absence of a separating property declaration on any
criterion that carries a pair is treated as FAIL for this criterion.

Source signal (R8): R8 JUDGE STANDARD introduces "Separating property" lines for each
covered criterion -- e.g., C-01: "individual-output table with explicit no-skip
constraint vs aggregate treatment." C-22 names whether the standard makes its own
discriminating mechanism explicit.

---

**C-23** -- Complete ACCEPTABLE/UNACCEPTABLE pair coverage across all scoring criteria
Weight: aspirational | Category: design
C-22 requires a separating property for every criterion that has a pair. C-23 requires
the prior condition: every scoring criterion must have at least one pair. A JUDGE
STANDARD that covers only criteria with known structural complexity leaves the remaining
criteria unanchored by examples.
**Pass condition**: The JUDGE STANDARD contains at least one ACCEPTABLE/UNACCEPTABLE
pair for every criterion in the current rubric. Coverage is all-or-nothing: every
criterion must be anchored by at least one concrete pair. C-23 is satisfied by coverage
completeness alone, regardless of separating property status.

Source signal (R9): R8 introduced separating properties but provided pairs for only 4
criteria. R9 extends full pair coverage to all 19 scoring criteria. C-22 names whether
the discriminating mechanism is explicit for existing pairs; C-23 names whether pairs
exist for all criteria.

---

**C-24** -- JUDGE STANDARD ACCEPTABLE examples grounded in current-round inputs
Weight: aspirational | Category: correctness
A JUDGE STANDARD with invented ACCEPTABLE examples can look specific while being
round-generic. An invented example is reusable across rounds; an input-grounded example
is verifiable against the current materials and cannot be recycled without modification.
**Pass condition**: ACCEPTABLE examples in the JUDGE STANDARD for coverage-critical
criteria are explicitly drawn from or verifiably traceable to the actual inputs being
scored in the current round. The JUDGE STANDARD must indicate that its examples are
grounded in provided scoring inputs. A JUDGE STANDARD that provides plausible examples
with no annotation linking them to actual round inputs does not satisfy this criterion.

Source signal (R9): R9 C-04 ACCEPTABLE states "drawn from provided inputs, not
invented" -- introducing a meta-grounding requirement at the JUDGE STANDARD level.
C-24 applies the C-04 grounding requirement to the JUDGE STANDARD's own examples.

---

**C-25** -- Pair-coverage completeness enforced at JUDGE production time via pre-structured register
Weight: aspirational | Category: design
C-23 requires that every criterion has a pair. C-25 requires the enforcement mechanism
to operate at production time, not reactively after the JUDGE STANDARD is written. A
pre-structured row-per-criterion register makes every missing pair a structural gap
detectable by inspection. A behavioral mandate relies on the writer's own completeness
check; a post-write audit detects missing pairs after the fact.
**Pass condition**: The JUDGE STANDARD sub-section includes a pre-structured register
with one explicit row per scoring criterion, established before pairs are written. A
missing row is a structural gap detectable by inspection. A behavioral instruction
without a pre-structured row inventory does not satisfy this criterion. A post-write
audit without a production-time register also does not satisfy this criterion --
detection and prevention are distinct mechanisms, and C-25 requires prevention.

Source signal (R10): V-01 achieves C-23 PASS via a 24-row coverage register where
"missing row = structural gap, detectable on inspection." V-02 and V-03 achieve PARTIAL
via behavioral or reactive-only mechanisms. C-23 names the coverage obligation; C-25
names the structural mechanism that makes it preventively enforceable.

---

**C-26** -- Per-entry source annotation makes ACCEPTABLE example grounding self-contained
Weight: aspirational | Category: correctness
C-24 requires that ACCEPTABLE examples are grounded in current-round inputs. C-26
requires the grounding to be expressed at the entry level -- attached to each individual
example -- not declared once in a preamble. A per-entry annotation makes grounding
inspectable per-example.
**Pass condition**: Every ACCEPTABLE example in the JUDGE STANDARD carries an explicit
per-entry source annotation (e.g., `from [Output-N]:`) attached to the example itself --
not in a preamble, not in a section header. A general statement of grounding intent
anywhere other than the individual example entry does not satisfy this criterion.

Source signal (R10): V-02 achieves C-24 PASS via "`from [Output-N]:` prefix on every
ACCEPTABLE entry; grounding is inspectable without reading the full output." C-24 names
the grounding obligation; C-26 names the entry-level annotation that makes traceability
inspectable per-entry.

---

**C-27** -- SYNTHESIS gate is a strict conjunction of all named role-completion tokens
Weight: aspirational | Category: design
C-10 requires at least one named gate token before SYNTHESIS. C-20 requires SYNTHESIS
to have CONFIRMATION COMPLETE as an independent precondition. C-27 requires the
conjunction mechanism: SYNTHESIS must be blocked unless ALL role-completion tokens are
simultaneously present. A design that lists two gate tokens without an explicit
conjunction connector leaves a bypass path.
**Pass condition**: The SYNTHESIS gate instruction explicitly names all required
role-completion tokens in a conjunction form using an explicit logical connector
(AND, BOTH...AND, or equivalent) so that SYNTHESIS cannot begin unless every listed
token is present. Multiple tokens listed in separate instructions without an explicit
conjunction do not satisfy this criterion. The conjunction must be expressed in the
gate instruction itself.

Source signal (R11): V-01 SYNTHESIS gate states "BOTH VERIFIER AUDIT COMPLETE AND
CONFIRMATION COMPLETE" -- the explicit BOTH...AND conjunction means SYNTHESIS is
structurally blocked if either token is absent. C-10 names gate existence; C-20 names
CONFIRMER independence; C-27 names the conjunction form that makes both obligations
simultaneously unbypassable.

---

**C-28** -- No-skip column rule enforces row-level completeness within the register
Weight: aspirational | Category: design
C-25 requires a pre-structured row-per-criterion register. C-28 requires a
complementary column-level constraint: every cell in every row must be populated --
no column within a row may be left blank. Without a no-skip column rule, a register row
may exist (satisfying C-25) while having empty structural column cells. The no-skip
rule elevates the register from row-existence enforcement to row-completeness
enforcement.
**Pass condition**: The register design includes an explicit no-skip column rule --
stated in the register header, gate constraint, or equivalent structural declaration --
that treats any blank cell in any required row as a structural violation preventing
JUDGE STANDARD COMPLETE. The rule must apply to all required columns. A register with
row-existence enforcement but no cell-level completeness constraint does not satisfy
this criterion.

Source signal (R11): C-08 ACCEPTABLE in the Round 11 JUDGE STANDARD names the no-skip
column rule as a distinct enforcement element alongside the row-gap detection property.
C-25 names whether a production-time row inventory exists; C-28 names whether each row
must be fully populated.

---

**C-29** -- SYNTHESIS gate includes explicit single-token prohibition complement
Weight: aspirational | Category: design
C-27 requires the BOTH...AND conjunction form, closing the structural bypass path. A
second bypass path remains: an interpretive bypass. A scorer who holds one token can
claim that satisfying a required condition individually constitutes compliance. An
explicit prohibition ("holding either token alone does not satisfy this gate") closes
it. C-27 names the positive conjunction requirement; C-29 names the negative exclusion
requirement that completes the double-closure of the SYNTHESIS gate.
**Pass condition**: The SYNTHESIS gate instruction contains, in addition to the required
conjunction form (C-27), an explicit negative prohibition statement that names subset
satisfaction as insufficient. The prohibition must be attached to the gate instruction
itself. A gate with BOTH...AND conjunction but no prohibition statement satisfies C-27
and fails C-29. Both must appear together in the same gate instruction to satisfy C-29.

Source signal (R12): V-01 SYNTHESIS gate states "holding either token alone does not
satisfy this gate" -- the prohibition clause attached to the same gate instruction as
the BOTH...AND conjunction. C-27 blocks the structural bypass; C-29 blocks the
interpretive bypass.

---

**C-30** -- Per-entry annotation enforcement at JUDGE production time via register field
Weight: aspirational | Category: correctness
C-26 requires each ACCEPTABLE example to carry an explicit per-entry source annotation
attached to the example itself. The Round 12 scorecard shows C-26 universally PARTIAL:
all variations declare grounding intent in the JUDGE role preamble but none enforce
annotation at production time. Only a production-time register field makes annotation
omission a structural gap detectable by inspection at any workflow stage.
**Pass condition**: The JUDGE STANDARD register includes an annotation-field column (or
equivalent named per-row structural slot) for the source annotation required by C-26.
The column must be established before ACCEPTABLE examples are written, so that an
unpopulated annotation field is a structural gap detectable by register inspection.
A preamble instruction to annotate all entries does not satisfy this criterion.

Source signal (R12): C-26 scores PARTIAL across all five Round 12 variations -- the
only criterion with a universal ceiling in R12. The C-24 -> C-26 -> C-30 chain closes
the same progression C-22 -> C-23 -> C-25 closed for pair coverage.

---

**C-31** -- Register cell gate enforces YES-only completion: NO is a blocking value
Weight: aspirational | Category: design
C-28 requires no blank cells. But a register that accepts NO as a valid non-blank value
still allows an unmet obligation to pass structural inspection. The YES-only gate closes
this remaining bypass: NO values block JUDGE STANDARD COMPLETE the same way blank
cells do. Blank blocks, NO blocks, only YES passes.
**Pass condition**: The register design includes an explicit gate consequence for NO
values -- stated in the register header, gate constraint, or equivalent structural
declaration -- that treats any cell containing NO as a blocking state preventing JUDGE
STANDARD COMPLETE. A register that accepts NO as a structurally valid non-blocking
value does not satisfy this criterion, even if it satisfies C-28's blank-cell
constraint.

Source signal (R13): C-25 ACCEPTABLE in the Round 13 JUDGE STANDARD states "A 'NO' in
any cell blocks JUDGE STANDARD COMPLETE." The C-25 -> C-28 -> C-31 chain closes the
register's enforcement from row existence to cell completeness to cell satisfaction.

---

**C-32** -- Single consolidated register unifies all production-time obligations as columns in one artifact
Weight: aspirational | Category: design
C-25 and C-30 can each be satisfied by separate register artifacts. When obligations
are tracked across separate artifacts, each artifact can be complete while the others
lag. A single consolidated register with all production-time obligations as named
columns (pair present, separating property declared, annotation attached) creates one
inspectable artifact whose state reflects all obligations simultaneously.
**Pass condition**: The JUDGE STANDARD uses a single register artifact that includes
columns for all production-time obligations -- at minimum: pair present (YES/NO),
separating property declared (YES/NO), and ACCEPTABLE source annotated (YES/NO). An
obligation tracked in a separate register, sub-gate, post-write audit, or checklist
rather than as a column in the consolidated register does not satisfy this criterion.

Source signal (R13): C-30 ACCEPTABLE in the Round 13 JUDGE STANDARD names "5-column
PAIR COVERAGE REGISTER with 'ACCEPTABLE source annotated' YES/NO as 5th column" as the
distinguishing mechanism.

---

**C-33** -- Intra-role lifecycle sub-gate creates named intermediate completion checkpoint within a single role's execution
Weight: aspirational | Category: design
C-10 requires phase gates between phases; C-15 requires output-input coupling between
roles. Both operate on inter-role boundaries. When a role's execution includes multiple
distinct obligations, a single terminal completion token cannot enforce intermediate
state. An intra-role lifecycle sub-gate -- a named intermediate completion state that
must be achieved before the role can produce its terminal token -- creates a two-stage
completion structure for a single role. The sub-gate is on the sequential enforcement
axis; the gate rules section is on the structural-declaration axis. These are orthogonal
families within one role's scope. C-10 and C-15 name inter-role gates; C-33 names
intra-role lifecycle sub-gates as a distinct mechanism family.
**Pass condition**: At least one role in the scoring design includes an explicitly named
intermediate completion sub-gate -- a named checkpoint state that must be reached and
named in the output before the role can produce its terminal completion token. The
sub-gate must be declared in a gate rules section or equivalent structural declaration
(not embedded in behavioral instruction prose). A role with only a terminal completion
token and no named intermediate checkpoint does not satisfy this criterion. The sub-gate
and the terminal gate must be named separately.

Source signal (R14): C-11 ACCEPTABLE in the Round 14 JUDGE STANDARD names "C-31
enforced via gate rules section (structural declaration) AND REGISTER COMPLETENESS
CONFIRMED lifecycle sub-gate (sequential enforcement) -- two orthogonal families" as
the mechanism. V-05 achieves C-11 by declaring REGISTER COMPLETENESS CONFIRMED as a
named intermediate state within the JUDGE lifecycle.

---

**C-34** -- Per-PARTIAL diagnostic enforced as schema-bound named columns in scoring table, not sentence mandate
Weight: aspirational | Category: behavior
C-17 requires the two-part diagnostic to be mandated by the scoring design. C-17 is
satisfied by a sentence-format mandate: a required diagnostic sentence per PARTIAL
verdict. But a sentence mandate is an instructional constraint: a scorer can populate
it without isolating the specific structural mechanisms. The sentence structure is
evaluated by reading the sentence; it cannot be evaluated by table inspection alone.
Present_mechanism and Absent_mechanism as named columns in the scoring table schema
escalates to structural enforcement: the two-part mandate becomes a column-schema
requirement identical in kind to any other required table column. C-17 names the
mandate for two-part content; C-34 names whether the mandate is implemented as
schema-bound named columns.
**Pass condition**: The scoring table format includes Present_mechanism and
Absent_mechanism as explicitly named, mandatory columns that appear in every PARTIAL
verdict row. The columns must be declared in the table schema definition. A table design
that uses a combined evidence cell with a sentence-format mandate satisfies C-17 but not
C-34. The column schema must be pre-defined; the columns must be mandatory per PARTIAL
row; and the column names must be explicitly stated.

Source signal (R14): C-17 ACCEPTABLE in the Round 14 JUDGE STANDARD names "from V-04:
Present_mechanism: for PARTIAL verdicts, name the specific structural element that is
present and prevented FAIL; Absent_mechanism: name the specific structural element that
is absent and prevented PASS -- both columns mandatory per PARTIAL row."
Escalation from C-17 to C-34 mirrors the escalation from C-23 (coverage obligation
named) to C-25 (structural register enforces coverage at production time).

---

**C-35** -- Intra-role lifecycle sub-gate emits named token from role body (sequential-axis enforcement)
Weight: aspirational | Category: design
C-33 requires a named intermediate sub-gate declared in a gate rules section. The gate
rules section creates the structural-declaration axis. But C-33's pass condition does
not require the sub-gate to produce a named token emitted during role body execution.
Declaration of the blocking condition is the structural axis; emission of a confirming
token during execution is the sequential axis. The sequential axis requires more than
declaration: the role body must emit the named intermediate token during its own
execution, making sub-gate achievement inspectable in the output record. The emitted
token is then required as a precondition by the role's terminal completion gate,
creating intra-role output-input coupling equivalent to C-15's inter-role coupling.
C-33 names the sub-gate obligation (declared in gate rules); C-35 names whether the
sub-gate additionally emits a named token from the role body during execution.
**Pass condition**: The named intermediate sub-gate (required by C-33) must produce a
named token that appears in the role's execution output, not merely in the gate rules
declaration. The emitted token must be explicitly required as a precondition by the
same role's terminal completion gate. A gate rules section that declares the sub-gate's
blocking condition without requiring a token to be emitted from the role body satisfies
C-33 but not C-35. The token must be emitted from the role body -- not a pre-declared
gate condition that the scorer copies in.

Source signal (R15): V-03 achieves C-33 PARTIAL via gate-rules structural declaration
alone (one axis); V-04 and V-05 achieve C-33 PASS by emitting REGISTER COMPLETENESS
CONFIRMED as a named token from the JUDGE role body during execution, required as a
precondition by JUDGE STANDARD COMPLETE (two axes). "Declaration alone = PARTIAL;
declaration plus token = PASS."

---

**C-36** -- Schema-enforcement detectability declaration explicitly names inspection-without-content-reading as the detection mechanism
Weight: aspirational | Category: design
C-34 requires Present_mechanism and Absent_mechanism as named mandatory columns whose
absence is detectable by table inspection. But the detectability claim is implicit in
C-34: a reader must know that named columns are inspectable without reading cells. A
schema declaration that explicitly states "a scoring table missing either column is a
structural gap detectable by table inspection without reading cell content" makes
detectability self-attesting: the declaration names its own detection mechanism.
C-34 names whether the mandate is expressed as named schema columns; C-36 names
whether the schema declaration makes its own detectability mechanism explicit --
inspection-without-content-reading stated, not inferred.
**Pass condition**: The schema declaration for the Present_mechanism and Absent_mechanism
columns must include an explicit statement that a scoring table missing either column
is a structural gap detectable by table inspection without reading cell content (or
equivalent language). The statement must appear in the schema definition. A schema that
defines the two mandatory columns without stating how their absence is detected satisfies
C-34 but not C-36. The absence-detection claim must explicitly name "inspection" or
"without reading cell content" or equivalent.

Source signal (R15): V-02 achieves C-34 PARTIAL via "columns present in table header
with prose mandate alone -- the mandate is evaluated by reading it, not by column
inspection." V-04 and V-05 achieve C-34 PASS by including explicit language: "a scoring
table missing either column is a structural gap detectable by table inspection without
reading cell content."

---

**C-37** -- JUDGE STANDARD includes per-criterion application notes naming the scoring-time verification test for position-sensitive criteria
Weight: aspirational | Category: design
C-22 requires a separating property declaration naming the discriminating mechanism for
each criterion. A separating property states WHAT the correct structural form is; it
does not direct the scorer on HOW to verify conformance at scoring time. For criteria
where scoring requires positional verification -- checking that a structural element
appears in a specific position relative to another element, not merely that it exists --
a separating property alone is insufficient: a scorer who confirms existence will not
perform the positional check without being explicitly directed. An application note per
position-sensitive criterion names the specific verification test to apply at scoring
time: "verify that [structural element] is positioned before [structural anchor]," not
just "verify that [structural element] exists." C-22 names the discriminating mechanism
explicitly (separating property); C-37 names whether the JUDGE STANDARD also includes
an explicit scoring-time test directing positional verification rather than existence
verification.
**Pass condition**: For each criterion whose pass condition requires positional or
sequencing verification, the JUDGE STANDARD includes a dedicated per-criterion
application note naming the specific verification test the scorer must apply at scoring
time. The application note must name the structural position to verify -- not just the
structural form to recognize. Architectural correctness without a scorer-directed
verification instruction scores the criterion PARTIAL or FAIL, because the scorer
performs existence verification rather than positional verification without explicit
direction. The application note must be attached to the criterion entry -- not stated
as a general scoring instruction in a preamble.

Source signal (R15): C-29 achieves PARTIAL across four of five R15 variations despite
architecturally correct designs -- "V-04 is the only variation producing C-29 PASS
because it instructs the scorer to verify position of the masking check in denominator
declarations before the pre-scan, not just confirm existence."

---

**C-38** -- Dedicated scorer-directed application note for structural-class-recognition criteria: universal FAIL is the diagnostic signal
Weight: aspirational | Category: design
C-37 names the application note mechanism for position-verification criteria. C-38
extends it to a second class: criteria where scoring requires the scorer to identify a
named structural class rather than verify a positional relationship. For these criteria,
architectural presence of the pattern is necessary but not sufficient to produce
criterion recognition: a scorer who confirms structural correctness will not name the
pattern as a distinct structural class without explicit direction. The diagnostic signal
that a criterion belongs to this class is universal FAIL: when no variation scores above
FAIL across all scored outputs despite architecturally satisfying the criterion, the
JUDGE STANDARD is missing a scorer-directed identification instruction. C-06 names
universal FAIL as a pattern requiring diagnosis; C-38 names the specific structural gap
the diagnosis reveals and the required remedy.
**Pass condition**: For each criterion whose pass condition requires the scorer to
identify and name a specific structural class rather than verify existence or position,
the JUDGE STANDARD includes a dedicated per-criterion application note that explicitly
directs the scorer to recognize and name the structural class as a distinct category.
The application note must name the class and direct the scorer to identify its presence
as a named structural class -- not just as structural correctness. A criterion that
scores universal FAIL triggers review for this type of application note; the absence
of a dedicated identification instruction is the presumptive diagnosis. A JUDGE
STANDARD with separating properties (satisfying C-22) but no dedicated application note
directing class identification does not satisfy C-38 for pattern-recognition criteria.

Source signal (R15): C-12 and C-25 universal FAIL across all five R15 variations --
"both require dedicated scorer-directed application notes to fire; having the two-layer
enforcement or co-location pattern present does not produce recognition without an
explicit instruction telling the scorer to identify and name it as a distinct structural
class."

---

**C-39** -- Positional application note names specific anchor element AND directional relationship (anchor-complete positional test)
Weight: aspirational | Category: design
C-37 requires a per-criterion application note naming the scoring-time positional
verification test for position-sensitive criteria. An application note can satisfy C-37
by naming the positional test at the class level: "verify position relative to anchor,
not just confirm presence." Class-level naming tells the scorer to perform a positional
check rather than an existence check but leaves scorer discretion about which positional
check to apply: which element is the anchor, and in which direction must the verified
element appear. A scorer who knows to check position but not the specific anchor or
direction may check position relative to the wrong element, or may check AFTER when
BEFORE is required. Anchor-complete naming closes this gap: the application note names
the specific anchor element the positional check must reference AND the directional
relationship (BEFORE, AFTER, or co-located with). This removes scorer discretion
entirely -- the verification test is fully specified, not just directed. C-37 names
whether a scoring-time positional test is directed at all; C-39 names whether that test
is specified to the exact anchor element and directionality, making the positional
verification instruction anchor-complete and direction-complete.
**Pass condition**: For each position-sensitive criterion, the per-criterion application
note (required by C-37) must name (a) the specific structural anchor element relative
to which the position is verified, AND (b) the directional relationship (BEFORE, AFTER,
or co-located with). A note that names the positional test class ("verify position, not
presence") without naming the specific anchor element and direction satisfies C-37 but
not C-39. A note stating "verify that [element] appears BEFORE [anchor]" where both
[element] and [anchor] are named and the direction (BEFORE) is explicit satisfies C-39.
The anchor and direction must be named in the application note itself -- not in the
separating property or in a preamble. A preamble instruction to "check positional
relationships" without per-criterion anchor naming does not satisfy this criterion.

Source signal (R16): V-03 achieves C-37 PASS via "APPLICATION NOTE for position-
sensitive criteria... Positional verification test: verify that [element] appears BEFORE
[anchor] in the scored output -- not that [element] exists... Confirm position, not
presence." The distinguishing mechanism: "per-criterion note names anchor and positional
relationship." Both the anchor element ("[anchor]") and the directional relationship
("BEFORE") are named explicitly in the application note, not just the class of
positional test. A note naming only the test type satisfies C-37 but not C-39.

Escalation chain: C-22 (separating property names discriminating mechanism) ->
C-37 (application note names scoring-time positional verification test) -> C-39
(application note names specific anchor element and directional relationship, making
the positional test anchor-complete and direction-complete).

---

**C-40** -- Structural-class-recognition application note includes explicit inertia-pattern-equals-FAIL declaration with structural-equivalence basis
Weight: aspirational | Category: design
C-38 requires a dedicated application note directing the scorer to recognize and name
the structural class. The application note can satisfy C-38 by instructing "identify
and name this pattern as [class] -- recognizing it as a distinct structural class is
the criterion requirement, not just confirming its architectural presence." This
instruction is sufficient to direct the identification act. But it does not specify
what verdict to assign when the architectural pattern is present but the identification
act is absent -- when a scored variation contains all required architectural components
but does not name the class. The "inertia pattern" is this case: architecture intact,
identification act not performed. A scorer who encounters the inertia pattern may
default to PARTIAL -- reasoning that "something is present, something is absent" -- or
even PASS if the scorer equates architectural presence with criterion satisfaction.
Without an explicit declaration that inertia = FAIL, the application note leaves open
the PARTIAL (and PASS) interpretation. An explicit inertia-equals-FAIL declaration
closes this scoring ambiguity: "the criterion requirement is the identification act,
not architectural confirmation; a variation with all components but no class-naming is
structurally equivalent to a variation that lacks the components entirely." The
structural-equivalence basis grounds the FAIL verdict in an equivalence argument rather
than a verdict directive alone, making the ruling independently verifiable rather than
merely asserted. C-38 names whether a dedicated application note exists directing class
identification; C-40 names whether the note also explicitly rules out PARTIAL and PASS
for the inertia case by declaring inertia-equals-FAIL with the structural-equivalence
basis that justifies the verdict.
**Pass condition**: The structural-class-recognition application note (required by C-38)
must include an explicit declaration that a scored variation containing all required
architectural components but not naming the structural class as a distinct category is
FAIL -- not PARTIAL. The declaration must state the structural-equivalence basis:
"architecturally present without the identification act = structurally equivalent to
lacking the components" or equivalent reasoning that explains why PARTIAL is not a
valid intermediate verdict for this case. The declaration must: (a) name the inertia
pattern explicitly (architectural presence without naming), (b) declare its verdict as
FAIL (not PARTIAL), and (c) provide the structural-equivalence reasoning (the
identification act IS the criterion requirement -- architecture is not). An application
note that directs class identification (satisfying C-38) but leaves open the PARTIAL
or PASS interpretation for architectural-presence-without-naming does not satisfy C-40.
The inertia-equals-FAIL declaration must be in the application note itself -- not in the
criterion's pass condition or in a general scoring instruction.

Source signal (R16): V-04 achieves C-38 PASS via "APPLICATION NOTE for structural-
class-recognition criteria: A criterion is a structural-class-recognition criterion if
its pass condition requires the scorer to identify and name a structural pattern as a
distinct class... The inertia pattern is FAIL -- it is structurally equivalent to a
variation that lacks the components entirely, because the criterion requirement is the
identification act, not architectural confirmation... A scored variation that contains
all architectural components but does not name the class is FAIL on a structural-class-
recognition criterion." The distinguishing mechanism: "dedicated application note with
inertia framing." Three components: (1) naming the inertia pattern explicitly,
(2) declaring it FAIL (not PARTIAL), (3) grounding the FAIL verdict in structural-
equivalence reasoning. C-38 is satisfied by having a dedicated application note
directing class identification; C-40 is satisfied only when the note additionally closes
the PARTIAL bypass path via the inertia-equals-FAIL declaration with
structural-equivalence basis.

Escalation chain: C-37 (per-criterion positional application note) -> C-38 (per-
criterion class-recognition application note) -> C-40 (class-recognition note
explicitly declares inertia = FAIL with structural-equivalence basis, closing the
PARTIAL and PASS bypass paths for the architectural-presence-without-identification
case).

---

**C-41** -- Positional-criteria classification label makes the set of position-sensitive criteria enumerable by inspection without reading note content
Weight: aspirational | Category: design
C-39 requires the positional application note to name the specific anchor element and
directional relationship. An anchor-complete note satisfies C-39 whether or not the
note entry carries a classification label. Without a classification label, a reviewer
verifying C-39 coverage must read each criterion entry's application note to determine
if positional requirements apply and whether the anchor and direction are named. A
classification label ("Positional verification test (C-39 applies here):" or equivalent)
at the note entry makes the set of position-sensitive criteria enumerable by scanning
for the label tag alone -- without reading note content for the classification step. The
label functions identically to the named column header in C-36: it makes structural
class membership self-attesting. C-39 names whether the anchor and direction are present
in the note; C-41 names whether the note entry also carries a classification label that
makes its position-sensitive category inspectable without content reading. The
classification label closes the audit gap: coverage verification of C-39 (do all
position-sensitive criteria have anchor-complete notes?) becomes a label-scan rather
than a note-content-read.
**Pass condition**: Each positional application note (required by C-39 to be
anchor-complete) includes an explicit classification label at the note entry that
identifies the note as a positional-verification note and names the criterion class that
triggered its inclusion (e.g., "Positional verification test (C-39 applies here):").
The label must be part of the note entry itself -- not in a preamble or section header.
An application note that is anchor-complete (satisfying C-39) but unlabeled as a
positional-verification test does not satisfy C-41. The classification label makes the
set of position-sensitive criteria in the JUDGE STANDARD enumerable by scanning for
the label tag alone, without reading each criterion's note content to determine class
membership.

Source signal (R17): C-10 and C-15 in the R17 JUDGE STANDARD are labeled "Positional
verification test (C-39 applies here):" -- the classification and the specific criterion
class are explicit in the note entry. A reviewer scanning the R17 JUDGE STANDARD can
identify the position-sensitive criteria by label alone, without reading each note's
anchor and direction content to determine whether the criterion requires positional
verification.

Escalation chain: C-22 (separating property names discriminating mechanism) -> C-37
(application note names scoring-time positional verification test) -> C-39 (note names
specific anchor element and directional relationship) -> C-41 (note also carries
classification label making position-sensitive criterion membership enumerable by
inspection without reading note content).

---

**C-42** -- Structural-class-recognition criteria classification label makes the set of structural-class-recognition criteria enumerable by inspection without reading note content
Weight: aspirational | Category: design
Parallel escalation from C-40 that mirrors C-41's escalation from C-39. C-40 requires
the structural-class-recognition application note to include an explicit
inertia-pattern-equals-FAIL declaration with structural-equivalence basis. A note
satisfying C-40 can be inertia-declaration-complete without being labeled as a
structural-class-recognition note. Without a classification label, a reviewer verifying
C-40 coverage must read each criterion entry's application note to determine if
structural-class-recognition requirements apply and whether the inertia declaration is
present. A classification label ("Structural-class-recognition criterion (C-38/C-40
applies here):" or equivalent) makes the set of structural-class-recognition criteria
enumerable by scanning for the label tag alone -- without reading note content for the
classification step. C-41 closes the classification-enumeration gap for
position-sensitive criteria; C-42 closes the identical gap for structural-class-
recognition criteria. Individual note compliance (C-39 for positional, C-40 for
class-recognition) does not imply that membership in the note-requiring category is
inspectable without content reading. The classification label is the mechanism that
makes set membership self-attesting and label-scannable in both families.
**Pass condition**: Each structural-class-recognition application note (required by
C-40 to include the inertia-pattern-equals-FAIL declaration with structural-equivalence
basis) includes an explicit classification label at the note entry that identifies the
note as a structural-class-recognition note and names the criterion class that triggered
its inclusion (e.g., "Structural-class-recognition criterion (C-38/C-40 applies here):").
The label must be part of the note entry itself -- not in a preamble or section header.
An application note that is inertia-declaration-complete (satisfying C-40) but unlabeled
as a structural-class-recognition note does not satisfy C-42. The classification label
makes the set of structural-class-recognition criteria in the JUDGE STANDARD enumerable
by scanning for the label tag alone, without reading each criterion's note content.

Source signal (R18): C-13 and C-14 in the R18 JUDGE STANDARD are labeled "Structural-
class-recognition criterion (C-38/C-40 applies here):" -- completing the classification-
label symmetry with the positional family. A reviewer scanning the R18 JUDGE STANDARD
can identify structural-class-recognition criteria by label alone, without reading each
application note to determine whether the criterion requires class identification.

Escalation chain: C-37 (per-criterion positional application note) -> C-38 (per-
criterion class-recognition application note) -> C-40 (class-recognition note declares
inertia = FAIL with structural-equivalence basis) -> C-42 (note also carries
classification label making structural-class-recognition criterion membership enumerable
by inspection without reading note content). Parallel to C-39 -> C-41.

---

**C-43** -- Application-note label-coverage enforced at production time via register columns in the consolidated register
Weight: aspirational | Category: design
C-41 and C-42 establish label obligations: each positional application note must carry
a positional classification label; each structural-class-recognition application note
must carry a structural-class-recognition classification label. Both are outcome
requirements -- they specify what the notes must look like when complete. Neither
criterion establishes a production-time enforcement mechanism. A reviewer verifying
label-coverage compliance must read each criterion entry and inspect its note for the
label text, identical to how C-23 required full pair coverage but left missing pairs
detectable only by reading the JUDGE STANDARD and comparing against the criterion list.
C-25 closed that gap by adding a pre-structured row-per-criterion register where a
missing row is a structural gap detectable by inspection. C-43 applies the same
escalation to the joint label obligations: the consolidated production-time register
(C-32) includes dedicated columns tracking label-presence for each criterion requiring
an application note -- one column for positional-label present (YES/NO, governing C-41
compliance) and one column for structural-class-recognition-label present (YES/NO,
governing C-42 compliance). A criterion entry showing NO in either label-present column
is a structural gap detectable by register inspection without reading the criterion's
note content. C-41 and C-42 name the per-note label obligations; C-43 names the
production-time register mechanism that makes label omission preventively detectable in
a single consolidated artifact rather than reactively discoverable by reading note
entries. Both label-family obligations converge in C-43's register column set, closing
the production-time enforcement gap for the entire application-note label
infrastructure.
**Pass condition**: The consolidated production-time register (satisfying C-32) includes
at minimum two additional columns: (a) "positional label present (YES/NO)" for all
criteria that require positional application notes, and (b) "structural-class-
recognition label present (YES/NO)" for all criteria that require structural-class-
recognition application notes. The columns must be established before the JUDGE
STANDARD is written, so that an unpopulated or NO-valued label-present entry is a
structural gap detectable by register inspection. A behavioral instruction to add labels
to all applicable notes does not satisfy this criterion. A post-write audit of label
presence also does not satisfy this criterion -- detection and prevention are distinct
mechanisms, and C-43 requires prevention. The label-coverage obligation tracked in a
separate sub-register or checklist rather than as columns in the consolidated register
does not satisfy this criterion.

Source signal (R18): R18 achieves C-42, completing both classification-label families
(C-41 positional, C-42 structural-class-recognition). Both families are now obligation-
complete but lack production-time enforcement. The gap mirrors C-23 before C-25: pair
coverage was obligated (C-23) but not register-enforced (C-25). C-43 applies the
C-23 -> C-25 escalation to the label-coverage obligations (C-41/C-42 -> C-43).

Escalation chains: C-41 (positional label obligation) -> C-43 |
                   C-42 (structural-class-recognition label obligation) -> C-43 |
parallel to: C-23 (pair-coverage obligation) -> C-25 (register enforcement).

---

**C-44** -- Application-note label-coverage register applies YES-only gate: NO in any label-present column blocks JUDGE STANDARD COMPLETE
Weight: aspirational | Category: design
C-43 adds register columns tracking label presence for all application-note-bearing
criteria, making unlabeled notes a structural gap detectable by register inspection.
But detection alone does not prevent completion: a register that accepts NO as a valid
non-blocking value still allows an unlabeled note to be present without blocking JUDGE
STANDARD COMPLETE. A criterion entry with label-present = NO is visible in the register
but does not stop the JUDGE from producing its terminal token. The YES-only gate closes
this remaining bypass: any criterion entry showing label-present = NO for a required
classification label (positional or structural-class-recognition) blocks JUDGE STANDARD
COMPLETE -- the same mechanism C-31 applies to the main pair-coverage register. C-43
makes label-coverage gaps structurally detectable; C-44 makes them structurally
blocking. The three-step closure for label obligations is complete: C-41/C-42 state the
obligation, C-43 makes omission detectable, C-44 makes omission blocking. This mirrors
the three-step closure for pair obligations: C-23 (obligation) -> C-25 (detectable) ->
C-31 (blocking).
**Pass condition**: The consolidated register design includes an explicit gate consequence
for NO values in either label-present column (positional or structural-class-
recognition) -- stated in the register header, gate constraint, or equivalent structural
declaration -- that treats any label-present = NO entry as a blocking state preventing
JUDGE STANDARD COMPLETE. A register that accepts NO as a structurally valid non-blocking
value in label-present columns does not satisfy this criterion, even if it satisfies
C-43's detection requirement. The gate consequence must be stated in the register design
itself. A behavioral instruction to resolve all NO entries before continuing does not
satisfy this criterion; the gate consequence must be structural, not instructional.

Source signal (R18): C-43 names the detection gap (unlabeled notes not register-
visible); C-44 names the blocking gap (unlabeled notes register-visible but not
register-blocking). Escalation chain: C-43 -> C-44, parallel to C-28 (no-skip column
rule, detection) -> C-31 (YES-only gate, blocking) for the main pair-coverage register.

---

## Formula

composite = (essential_pass / N_essential x 60)
          + (recommended_pass / N_recommended x 30)
          + (aspirational_pass / N_aspirational x 10)

PARTIAL counts as 0.5. FAIL counts as 0.

Current weights: N_essential = 4, N_recommended = 3, N_aspirational = 37

Each aspirational criterion is worth ~0.270 pts (10 / 37).
Max score: 100.

---

## Golden Threshold

An output is golden if:
- All essential criteria score PASS (not PARTIAL), AND
- Composite score >= 80

An output is not-golden if either condition fails. The determination must state
which condition failed and why.

---

## Design Notes

### v1 rationale
Established the essential/recommended/aspirational tier structure. C-01 through C-09
cover completeness, formula correctness, format, evidence grounding, synthesis, and
structural completeness as baseline and stretch goals.

### v2 additions (C-10, C-11, C-12)
Derived from Round 1 findings:
- C-10 (phase completion gates): V-02 and V-04 were the only Round 1 designs that
  prevented truncation -- the gate marker, not the named phase, was the mechanism.
- C-11 (layered enforcement): V-04 (90pts, highest) was structurally unreachable
  by any single-mechanism design; combining table templates + phase gates eliminated
  omission risk.
- C-12 (evidence specificity self-check): C-04 was universally PARTIAL in Round 1 --
  the only criterion with a universal ceiling; the gap is between evidence presence
  (already essential) and evidence specificity (uncaptured).

N_aspirational increased from 2 -> 5. Each aspirational worth ~2 pts.

### v3 additions (C-13, C-14)
Derived from Round 2 excellence signals:
- C-13 (adversarial auditor): V-01 achieved C-04 PASS via Judge role; V-03 achieved
  only PARTIAL despite having an explicit audit phase. The distinguishing mechanism
  is adversarial separation.
- C-14 (orthogonal enforcement axes): C-11 was universally unachieved in Round 2.
  V-03 got PARTIAL because gate + audit operate on the same sequencing axis.

N_aspirational increases from 5 -> 7. Each aspirational now worth ~1.4 pts.

### v4 additions (C-15, C-16)
Derived from Round 3 excellence signals:
- C-15 (output-input role coupling): V-01 was the only variation to achieve C-13
  PASS in Round 3. The distinguishing mechanism: the Judge produces JUDGE STANDARD
  COMPLETE, the Analyst required input.
- C-16 (post-write evidence verification): C-11 was universally PARTIAL in Round 3.
  The unachieved ceiling: a verification step that fires after evidence cells are
  written, by an entity independent of the writer.

N_aspirational increases from 7 -> 9. Each aspirational now worth ~1.1 pts.

### v5 additions (C-17, C-18)
Derived from Round 4 excellence signals:
- C-17 (per-PARTIAL two-part diagnostic): V-05 achieves C-09 PASS by requiring a
  named two-part sentence per PARTIAL verdict.
- C-18 (formal Produces/Requires manifest): V-04 achieves C-11 PASS by declaring a
  complete hard gate rules table.

N_aspirational increases from 9 -> 11. Each aspirational now worth ~0.91 pts.

### v6 additions (C-19)
Derived from Round 5 excellence signal:
- C-19 (independent confirmation): V-05 achieves C-17 PASS through two independent
  paths: template format mandate + confirmation family.

N_aspirational increases from 11 -> 12. Each aspirational now worth ~0.833 pts.

### v7 additions (C-20)
Derived from Round 6 excellence signals:
- C-20 (dedicated CONFIRMER role): V-01 introduces the CONFIRMER -- first named role
  whose explicit mandate is content-quality verification. Produces CONFIRMATION
  COMPLETE; SYNTHESIS requires both gates independently.

N_aspirational increases from 12 -> 13. Each aspirational now worth ~0.769 pts.

### v8 additions (C-21)
Derived from Round 7 excellence signals:
- C-21 (manifest role domain and exclusion declarations): V-02 extends the formal
  manifest with DOMAIN and CANNOT CHECK columns.

N_aspirational increases from 13 -> 14. Each aspirational now worth ~0.714 pts.

### v9 additions (C-22)
Derived from Round 8 excellence signals:
- C-22 (per-criterion separating property): R8 JUDGE STANDARD introduces explicit
  "Separating property" lines for each covered criterion.

N_aspirational increases from 14 -> 15. Each aspirational now worth ~0.667 pts.

### v10 additions (C-23, C-24)
Derived from Round 9 excellence signals:
- C-23 (complete pair coverage): R9 extends full pair coverage to all 19 scoring
  criteria.
- C-24 (ACCEPTABLE examples grounded in current-round inputs): R9 introduces
  "drawn from provided inputs, not invented" at the JUDGE STANDARD level.

N_aspirational increases from 15 -> 17. Each aspirational now worth ~0.588 pts.

### v11 additions (C-25, C-26)
Derived from Round 10 excellence signals:
- C-25 (pair-coverage register at JUDGE production time): V-01 achieves C-23 PASS
  via a 24-row register.
- C-26 (per-entry source annotation): V-02 achieves C-24 PASS via `from [Output-N]:`
  prefix on every ACCEPTABLE entry.

N_aspirational increases from 17 -> 19. Each aspirational now worth ~0.526 pts.

### v12 additions (C-27, C-28)
Derived from Round 11 excellence signals:
- C-27 (SYNTHESIS conjunction gate): V-01's "BOTH...AND" closes the bypass path that
  separate per-token instructions leave open.
- C-28 (no-skip column rule): C-25 names row existence; C-28 names cell completeness.
  Together they close the register from row existence to row completeness.

N_aspirational increases from 19 -> 21. Each aspirational now worth ~0.476 pts.

### v13 additions (C-29, C-30)
Derived from Round 12 excellence signals:
- C-29 (SYNTHESIS prohibition complement): C-27 closes the structural bypass; C-29
  closes the interpretive bypass. Double-closure-complete.
- C-30 (per-entry annotation register field): C-26 universal PARTIAL in R12. C-30
  applies the C-23 -> C-25 escalation to annotation.

N_aspirational increases from 21 -> 23. Each aspirational now worth ~0.435 pts.

### v14 additions (C-31, C-32)
Derived from Round 13 excellence signals:
- C-31 (YES-only register gate): C-28 closes blank-cell bypass; C-31 closes NO-cell
  bypass. Blank blocks, NO blocks, only YES passes.
- C-32 (single consolidated register): C-25 and C-30 can be satisfied by separate
  artifacts that diverge. A single register closes the split-surface gap.

N_aspirational increases from 23 -> 25. Each aspirational now worth ~0.400 pts.

### v15 additions (C-33, C-34)
Derived from Round 14 excellence signals:
- C-33 (intra-role lifecycle sub-gate): V-05 achieves C-11 PASS via REGISTER
  COMPLETENESS CONFIRMED -- two orthogonal families (structural-declaration +
  sequential-lifecycle) within one role.
- C-34 (schema-bound Present/Absent columns): Escalates C-17's sentence-format
  mandate to column-schema structural enforcement.

N_aspirational increases from 25 -> 27. Each aspirational now worth ~0.370 pts.

### v16 additions (C-35, C-36, C-37, C-38)
Derived from Round 15 excellence signals:
- C-35 (sub-gate token emission): C-33 names the sub-gate declaration; C-35 names
  whether the role body also emits the token during execution -- the sequential axis
  that makes intra-role orthogonality complete.
- C-36 (schema detectability self-attestation): C-34 names schema-bound columns;
  C-36 names whether the schema declaration explicitly states its own
  inspection-without-reading detection mechanism.
- C-37 (positional application note): C-22 names separating properties; C-37 names
  whether the JUDGE STANDARD also directs the scorer on HOW to perform positional
  verification at scoring time.
- C-38 (class-recognition application note): universal FAIL on C-12 and C-25 in R15
  is the diagnostic signal. Both require dedicated "identify and name this as [class]"
  instructions.

N_aspirational increases from 27 -> 31. Each aspirational now worth ~0.323 pts.

### v17 additions (C-39, C-40)
Derived from Round 16 excellence signals:
- C-39 (anchor-complete positional test): V-03 achieves C-37 PASS by naming both the
  anchor element AND the directional relationship (BEFORE [anchor]) -- not just the
  test class. C-37 directs the scorer to check position; C-39 names whether the check
  is fully specified (anchor + direction) so no scorer discretion remains about which
  positional test to perform.
- C-40 (inertia-pattern-equals-FAIL with structural-equivalence basis): V-04 achieves
  C-38 PASS with inertia framing -- explicitly declaring that architectural presence
  without the identification act = FAIL (not PARTIAL), grounded in structural-
  equivalence reasoning ("the criterion requirement is the identification act, not
  architectural confirmation"). C-38 requires the application note to exist; C-40
  requires the note to also close the PARTIAL bypass path via the inertia declaration.

N_aspirational increases from 31 -> 33. Each aspirational now worth ~0.303 pts.

### v18 additions (C-41, C-42)
Derived from Round 17 excellence signals:
- C-41 (positional-criteria classification label): R17 JUDGE STANDARD labels C-10 and
  C-15 application notes with "Positional verification test (C-39 applies here):" --
  the classification tag makes the position-sensitive criterion set enumerable by
  label-scan alone, without reading each note's anchor-and-direction content to
  determine class membership. C-39 names anchor-and-direction completeness of the note;
  C-41 names whether the note also carries the classification label that makes coverage
  auditing inspection-driven rather than content-reading-driven.
- C-42 (structural-class-recognition classification label): Parallel escalation from
  C-40, closing the identical gap for the structural-class-recognition family. C-41
  closes classification-enumeration for positional criteria; C-42 closes it for
  structural-class-recognition criteria. Both criteria complete the label symmetry
  between the two application-note families: positional (C-37/C-39/C-41) and
  structural-class-recognition (C-38/C-40/C-42).

N_aspirational increases from 33 -> 35. Each aspirational now worth ~0.286 pts.

### v19 additions (C-43, C-44)
Derived from Round 18 excellence signals:
- C-43 (application-note label-coverage register): R18 achieves C-42 (structural-
  class-recognition labels on C-13 and C-14), completing both label families. C-41
  and C-42 are now both obligation-complete but lack production-time enforcement --
  the same gap C-23 had before C-25 added a register. C-43 closes that gap by adding
  label-present columns (positional and structural-class-recognition) to the
  consolidated register, making unlabeled notes a structural gap detectable by
  register inspection. Both label-family obligations converge in a single column set:
  C-41/C-42 -> C-43, parallel to C-23 -> C-25.
- C-44 (YES-only gate on label-coverage register): C-43 makes unlabeled notes
  detectable; C-44 makes them blocking. NO in any label-present column blocks JUDGE
  STANDARD COMPLETE. Parallel to C-31 for the main register. Three-step closure for
  label obligations complete: C-41/C-42 (obligation) -> C-43 (detectable) ->
  C-44 (blocking), mirroring C-23 (obligation) -> C-25 (detectable) -> C-31 (blocking).

N_aspirational increases from 35 -> 37. Each aspirational now worth ~0.270 pts.
Max score remains 100.
