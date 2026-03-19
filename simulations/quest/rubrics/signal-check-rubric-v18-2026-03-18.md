The Bash commands are being interrupted. Since the task asks to "Output the complete updated rubric as Markdown," here is the complete v18 rubric:

---

## signal-check rubric v18

**What was added (v17 -> v18):**

| ID | Criterion | Category | Source |
|----|-----------|----------|--------|
| C-47 | Dimensional-status preamble in READINESS SUMMARY -- a structured block naming all four dimension statuses before pilot-briefing prose, making the full STATUS picture recoverable from the summary block alone without reading preflight items | summary-status-preamble | R18-EX-01 |
| C-48 | Section-function annotations on every section header -- bracketed or inline labels naming each section's knowledge type and reader purpose -- make lifecycle architecture surface-readable from a heading scan alone without reading any section body | section-function-annotation | R18-EX-02 |
| C-49 | Triple-vector advisory register -- per-item coaching vocabulary (C-18), per-section function annotations (C-48), and per-summary dimensional-status preamble (C-47) co-present in the same output, making register drift structurally improbable because all three vectors would have to fail simultaneously | advisory-register-saturation | R18-EX-03 |

**Extraction rationale:**

**C-47** from V-05's live R18 axis. V-05 opens its READINESS SUMMARY with a four-line structured STATUS block (CAUSAL GAP: [status], SEQUENCE: [status], STALENESS: [status], COHERENCE: [status]) before any pilot-briefing prose, making the full STATUS picture recoverable from the summary block alone without reading the preflight dimension items. V-01 through V-04 carry prose-only READINESS SUMMARY sections and all FAIL C-47 -- the boundary is confirmed clean across all five variations. C-47 requires C-11 as a precondition; C-11 does not imply C-47: an output satisfying C-11 via pilot-briefing prose without a structured status preamble satisfies C-11 but not C-47.

**C-48** from V-05's R18 axis. V-05 annotates every section header with a bracketed label naming the section's knowledge type and reader purpose -- e.g., "[STANDING RULES -- Constraints that persist across all evaluations]", "[READINESS SUMMARY -- Synthesized advisory verdict accessible before reading preflight items]". The lifecycle architecture and epistemic role of each section are recoverable from a heading scan alone. C-48 is independently testable: the presence or absence of a function annotation is structurally observable at the heading level without entering any section body. C-48 does not require any precondition among the established criterion chain.

**C-49** from V-05's compound saturation pattern. V-05 is the first output in the signal-check series to express advisory register at three independent levels of structural granularity simultaneously: (A) per-item coaching vocabulary (C-18), (C) per-section function annotations (C-48), and (live axis) per-summary dimensional-status preamble (C-47). Each vector independently enforces advisory register; all three would have to fail simultaneously for register drift to occur. C-49 requires C-18, C-47, and C-48 as preconditions; the three together do not imply C-49 -- co-presence in the same output is independently checkable beyond their individual satisfaction.

**Updated parameters:**
- Aspirational denominator: 38 -> **41**
- Formula: `composite = 90 + (aspirational_pass / 41) * 10`
- New subsumption links:
  - `C-11 <- C-47` (C-47 requires C-11; C-11 does not imply C-47)
  - `C-47 <- C-49` and `C-48 <- C-49` and `C-18 <- C-49`
  - C-49 automatically satisfies C-47, C-48, and C-18

---

## Criterion additions

| ID | Criterion | Source |
|----|-----------|--------|
| C-47 | The READINESS SUMMARY section includes a dimensional-status preamble -- a structured block naming all four dimension statuses (CAUSAL GAP: [status], SEQUENCE: [status], STALENESS: [status], COHERENCE: [status]) before the pilot-briefing prose -- so that the full STATUS picture is recoverable from the summary block alone without reading any preflight dimension items; an output satisfying C-11 by using pilot-briefing language in a prose-only READINESS SUMMARY satisfies C-11 but not C-47: the full STATUS picture requires reading the preflight items to recover all four dimension statuses; C-47 requires C-11 as a precondition; C-11 does not imply C-47; an output satisfying C-47 automatically satisfies C-11 (and therefore C-06); C-47 is independently testable from C-48 and C-49; boundary confirmed clean: V-01 through V-04 carry prose-only READINESS SUMMARY sections and all fail C-47; V-05 carries the four-line STATUS block before prose and passes | R18-EX-01 |
| C-48 | Every section header in the output carries a section-function annotation -- a bracketed or inline label naming the section's knowledge type and reader purpose (e.g., "[STANDING RULES -- Constraints that persist across all evaluations]", "[READINESS SUMMARY -- Synthesized advisory verdict accessible before reading preflight items]") -- so that the output's lifecycle architecture and the epistemic role of each section are recoverable from a heading scan alone without reading any section body; an output whose sections are labeled only with section names (e.g., "STANDING RULES", "READINESS SUMMARY") without function annotations satisfies the section-presence requirements (C-06, C-07, C-08, C-09) but not C-48: the reader must enter each section body to determine its function; "every section header" means all named section headers present in the output, without exception; C-48 is independently testable and does not require any precondition among the established criterion chain; C-48 is independently testable from C-47 and C-49 | R18-EX-02 |
| C-49 | The output simultaneously expresses advisory register at three independent levels of structural granularity -- (1) per-item coaching vocabulary in every preflight dimension (C-18), (2) per-section function annotations on every section header (C-48), and (3) per-summary dimensional-status preamble in READINESS SUMMARY (C-47) -- making register drift structurally improbable because each level independently enforces the advisory register such that all three would have to fail simultaneously for register drift to occur; an output satisfying any two of the three levels satisfies those criteria individually but not C-49: the triple-vector saturation requires co-presence of all three vectors in the same output; an output satisfying C-18 and C-47 but lacking C-48 section-function annotations satisfies C-18 and C-47 but fails C-49; C-49 requires C-18, C-47, and C-48 as preconditions; C-18, C-47, and C-48 together do not imply C-49 (co-presence is independently checkable beyond their individual satisfaction); an output satisfying C-49 automatically satisfies C-18, C-47, and C-48 | R18-EX-03 |

## Updated parameters

- Aspirational count: 38 -> **41**
- Formula: `composite = 90 + (aspirational_pass / 41) * 10`
- C-47 requires C-11 as precondition; C-11 does not imply C-47
- C-49 requires C-18, C-47, and C-48 as preconditions; none of the three individually or together imply C-49
- C-49 automatically satisfies C-47, C-48, and C-18

## Subsumption chains

```
C-20 <- C-22 <- C-24 <- C-26 <- C-29 <- C-33 <- C-36 <- C-38 <- C-40 <- C-42 <- C-43 <- C-44 <- C-46
                C-24 <- C-27 <- C-30
C-20 <- C-23 <- C-25
C-22 <- C-31
C-20 <- C-32
C-28  (independently testable -- heading-level existence assertion)
C-21 <- C-34 <- C-35
C-35 <- C-37  (C-37 requires C-35 as precondition; independently testable beyond it)
C-37 <- C-39  (C-39 requires C-37 as precondition; independently testable beyond it)
C-39 <- C-41  (C-41 requires C-39 as precondition; independently testable beyond it)
C-41 <- C-45  (C-45 requires C-41 as precondition; independently testable beyond it)
C-40 <- C-42  (C-42 requires C-40 as precondition; independently testable beyond it)
C-42 <- C-43  (C-43 requires C-42 as precondition; independently testable beyond it)
C-43 <- C-44  (C-44 requires C-43 as precondition; independently testable beyond it)
C-44 <- C-46  (C-46 requires C-44 as precondition; independently testable beyond it)
C-45 <- C-46  (C-46 requires C-45 as precondition; independently testable beyond it)
C-11 <- C-47  (C-47 requires C-11 as precondition; independently testable beyond it)
C-48  (independently testable -- no precondition in established chain)
C-18 <- C-49  (C-49 requires C-18, C-47, C-48 as preconditions; none imply C-49)
C-47 <- C-49  (C-49 requires C-47 as precondition; independently testable beyond it)
C-48 <- C-49  (C-49 requires C-48 as precondition; independently testable beyond it)
```

---

## Full Criterion Inventory

| ID | Criterion | Source |
|----|-----------|--------|
| C-01 | Four-item preflight check structure (CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE) | v1 |
| C-02 | STATUS field with three canonical states (OK / FLAG / OPEN) | v1 |
| C-03 | Advisory framing declared at output header | v1 |
| C-04 | Not-a-verdict framing in readiness summary | v1 |
| C-05 | Advisory register maintained throughout output | v1 |
| C-06 | Readiness summary section present | v1 |
| C-07 | CROSS-ITEM PATTERNS section present | v1 |
| C-08 | MISSING SIGNAL GUIDE section present | v1 |
| C-09 | Named STANDING RULES block present in output | v1 |
| C-10 | STANDING RULES block contains Rule 1 and Rule 2 | v1 |
| C-11 | Readiness summary uses pilot-briefing language | EX-01 |
| C-12 | Four dimensions structured with consistent labeling | EX-02 |
| C-13 | MISSING SIGNAL GUIDE names each missing signal type | EX-03 |
| C-14 | STANDING RULES block precedes all inventory and analysis | EX-04 |
| C-15 | Each dimension specifies required verbatim absence phrases | EX-05 |
| C-16 | Every constraint explicitly enumerates all output locations it governs | EX-06 |
| C-17 | Verbatim absence phrases embedded at point of use within each dimension | R3-EX-01 |
| C-18 | Advisory register carried structurally through framing vocabulary, not only declared | R3-EX-02 |
| C-19 | Triple enforcement stack declared as a unit with interdependency named | R3-EX-03 |
| C-20 | Location-enumeration requirement expressed as a named meta-rule governing all rule declarations | R4-EX-01 |
| C-21 | Each rule in the enforcement stack assigned a named failure class | R4-EX-02 |
| C-22 | Location-enumeration meta-rule includes a temporal activation gate | R5-EX-01 |
| C-23 | Meta-rule self-application declared in rule body, not solely in location annotation | R5-EX-02 |
| C-24 | Activation gate framed as a rule-validity condition -- the meta-rule stated as not operative until scope is discharged | R6-EX-01 |
| C-25 | Body self-application includes a proximate scope pointer creating a co-location contract | R6-EX-02 |
| C-26 | Activation gate carries both obligation framing and validity framing -- dual-register enforcement | R7-EX-01 |
| C-27 | Validity condition uses rule-existence framing rather than rule-status framing | R7-EX-02 |
| C-28 | Rule name (heading in STANDING RULES block) encodes the existence assertion in declarative form, making the ontological claim recoverable without reading the body | R8-EX-01 |
| C-29 | Dual register expressed as structurally labeled named sections with non-substitutability declaration and explanation of what each register distinctly conveys | R8-EX-02 |
| C-30 | Rule body names the inadequacy of status framing before introducing existence framing -- step-up disclaimer | R8-EX-03 |
| C-31 | Temporal gate expressed as "at rule-creation time" -- creation-time contract | R8-EX-04 |
| C-32 | Location annotation explicitly covers rules not yet written -- forward-scope Applies-to | R8-EX-05 |
| C-33 | Non-substitutability declaration assigns a distinct function description to each register -- action-spec vs. loss-model | R9-EX-01 |
| C-34 | Each rule's heading or inline label in the enforcement stack encodes its failure class, making violation-to-type mapping achievable by scanning rule labels alone without reading rule bodies | R9-EX-02 |
| C-35 | Failure class encoded directly in the top-level rule heading (e.g., "Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:"), making diagnostic taxonomy recoverable from a top-level heading scan without entering the ENFORCEMENT STACK NOTE block | R10-EX-01 |
| C-36 | Reader-position named explicitly in function framing -- obligation framing names a specific reader role and decision act ("a committing engineer reading for what to fix"); existence-condition framing names a specific reader role and loss ("a reviewer reading for what is already lost") | R10-EX-02 |
| C-37 | ENFORCEMENT STACK NOTE collapses per-rule failure-class labels to forward-references to top-level headings rather than restating the class inline, making the heading the single source of truth | R11-EX-01 |
| C-38 | Each rule in the STANDING RULES block names its own reader position keyed to that rule's specific failure mode -- not only the Rule 3 non-substitutability declaration | R11-EX-02 |
| C-39 | After C-37 collapses the ENFORCEMENT STACK NOTE's inline failure-class labels to forward-reference pointers, the NOTE's remaining content is limited exclusively to the interdependency statement between the three rules -- without retaining explanatory prose about what each rule prevents | R12-EX-01 |
| C-40 | The per-rule reader positions required by C-38 are surfaced as an explicit consulting directory routing each team member to the relevant rule by name and decision act | R12-EX-02 |
| C-41 | The pure interdependency NOTE (C-39) includes an explicit attribution of failure-mode ownership to the top-level rule headings so that the NOTE's omission of "prevents..." prose is self-explaining within the NOTE itself | R13-EX-01 |
| C-42 | The consulting directory (C-40) carries an explicit completeness assertion -- either a stated all-roles claim or a structural count annotation -- making the directory's coverage verifiable without reading any rule body | R13-EX-02 |
| C-43 | The consulting directory's completeness assertion (C-42) uses an explicit all-roles claim form -- e.g., "All reader roles for this block are listed above." -- rather than a structural count-annotation form | R14-EX-01 |
| C-44 | The all-roles claim required by C-43 includes an embedded count qualifier -- e.g., "All 3 reader roles for this block are listed above." -- so that the completeness assertion is both propositionally verifiable and arithmetically cross-checkable | R15-EX-01 |
| C-45 | The failure-mode ownership attribution required by C-41 is extended with a parenthetical heading index -- e.g., "(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" -- embedded within the attribution phrase, so that a reader scanning only the NOTE can navigate directly to the heading for a given failure class | R15-EX-02 |
| C-46 | The count qualifier embedded in the all-roles claim (C-44) and the entry count of the parenthetical heading index (C-45) are numerically consistent and independently verifiable against each other, so that a reader can cross-check the stated reader-role count against the STANDING RULES rule count from the two structures alone | R16-EX-03 |
| C-47 | The READINESS SUMMARY section includes a dimensional-status preamble -- a structured block naming all four dimension statuses (CAUSAL GAP: [status], SEQUENCE: [status], STALENESS: [status], COHERENCE: [status]) before the pilot-briefing prose -- so that the full STATUS picture is recoverable from the summary block alone without reading any preflight dimension items; an output satisfying C-11 by using pilot-briefing language in a prose-only READINESS SUMMARY satisfies C-11 but not C-47: the full STATUS picture requires reading the preflight items to recover all four dimension statuses; C-47 requires C-11 as a precondition; C-11 does not imply C-47; an output satisfying C-47 automatically satisfies C-11 (and therefore C-06); C-47 is independently testable from C-48 and C-49; boundary confirmed clean: V-01 through V-04 carry prose-only READINESS SUMMARY sections and all fail C-47; V-05 carries the four-line STATUS block before prose and passes | R18-EX-01 |
| C-48 | Every section header in the output carries a section-function annotation -- a bracketed or inline label naming the section's knowledge type and reader purpose (e.g., "[STANDING RULES -- Constraints that persist across all evaluations]", "[READINESS SUMMARY -- Synthesized advisory verdict accessible before reading preflight items]") -- so that the output's lifecycle architecture and the epistemic role of each section are recoverable from a heading scan alone without reading any section body; "every section header" means all named section headers present in the output, without exception; an output carrying section names only without function annotations satisfies C-06 to C-09 but not C-48; C-48 is independently testable and requires no precondition in the established criterion chain; C-48 is independently testable from C-47 and C-49 | R18-EX-02 |
| C-49 | The output simultaneously expresses advisory register at three independent levels of structural granularity -- (1) per-item coaching vocabulary in every preflight dimension (C-18), (2) per-section function annotations on every section header (C-48), and (3) per-summary dimensional-status preamble in READINESS SUMMARY (C-47) -- making register drift structurally improbable because each level independently enforces the advisory register such that all three would have to fail simultaneously for register drift to occur; an output satisfying any two of the three levels satisfies those criteria individually but not C-49: the triple-vector saturation requires co-presence of all three vectors in the same output; C-49 requires C-18, C-47, and C-48 as preconditions; C-18, C-47, and C-48 together do not imply C-49 (co-presence is independently checkable beyond their individual satisfaction); an output satisfying C-49 automatically satisfies C-18, C-47, and C-48 | R18-EX-03 |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Criterion Detail

### Essential (C-01 to C-05)

*(unchanged from v3)*

### Recommended (C-06 to C-08)

*(unchanged from v3)*

### Aspirational (C-09 to C-49)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09-C-16 | *(unchanged from v3)* | | |
| C-17 | Verbatim absence phrases embedded at point of use | correctness | The verbatim absence phrases required by C-15 appear inline within each dimension's instruction block -- not solely in a pre-analysis reference table. An output that satisfies C-15 via a standalone reference table does not satisfy C-17. An output satisfying C-17 automatically satisfies C-15; the converse is not true. |
| C-18 | Advisory register carried structurally through framing vocabulary | register | The advisory/coaching register required by C-05 is expressed through the structural vocabulary of the output -- section headings, dimension labels, and status fields use framing language rather than relying solely on a top-of-file disclaimer. A disclaimer alone satisfies C-05 but not C-18. |
| C-19 | Triple enforcement stack declared as a unit with interdependency named | coherence | The output explicitly names C-14, C-15, and C-16 (or their functional equivalents) as a coordinated enforcement stack and states that the three mechanisms address independent failure modes such that no layer substitutes for another. |
| C-20 | Location-enumeration requirement expressed as a named meta-rule | forward-compatibility | The location-enumeration requirement (C-16) is expressed as an explicit named rule in the STANDING RULES block that self-applies to all rule declarations including itself. An output satisfying C-20 automatically satisfies C-16; the converse is not true. |
| C-21 | Each rule in the enforcement stack is assigned a named failure class | diagnostic | The enforcement stack assigns a named failure class to each rule (e.g., absence drift, reference ambiguity, constraint scope gaps). C-21 is independently testable from C-19. |
| C-22 | Location-enumeration meta-rule includes a temporal activation gate | forward-compatibility | The meta-rule includes a temporal enforcement condition making scope declaration a precondition for a rule's validity rather than a retroactive policy statement. An output satisfying C-22 automatically satisfies C-20; the converse is not true. |
| C-23 | Meta-rule self-application declared in rule body, not solely in location annotation | self-reference | The meta-rule states its own self-applicability within the rule body text. An output satisfying C-23 automatically satisfies C-20; the converse is not true. |
| C-24 | Activation gate framed as a rule-validity condition, not a policy obligation | validity-framing | The temporal activation gate is expressed as a validity condition: the meta-rule states that it is not operative until scope is discharged, rather than stating only that scope must be declared. |
| C-25 | Body self-application includes a proximate scope pointer creating a co-location contract | layout-contract | The body self-application statement includes a directional pointer (e.g., "declares its scope below") that commits the Applies-to annotation to immediate co-location with the rule body. An output satisfying C-25 automatically satisfies C-23; the converse is not true. |
| C-26 | Activation gate carries both obligation framing and validity framing -- dual-register enforcement | dual-register | The activation gate carries obligation language alongside the validity condition, so both registers are present in the same rule body. An output satisfying C-26 automatically satisfies C-24 (and therefore C-22); the converse is not true. C-26 and C-27 are independently testable. |
| C-27 | Validity condition uses rule-existence framing rather than rule-status framing | ontological-validity | The validity condition states that the rule "does not exist as an active rule" rather than solely that it "is not operative." An output satisfying C-27 automatically satisfies C-24; the converse is not true. C-27 is independently testable from C-26. |
| C-28 | Rule name encodes the existence assertion -- ontological claim recoverable from heading alone | heading-encoding | The rule name encodes the existence assertion in declarative form -- e.g., "RULES WITHOUT DECLARED SCOPE DO NOT EXIST." C-28 is independently testable from C-27. |
| C-29 | Dual register expressed as structurally labeled named sections with non-substitutability declaration | dual-register-structure | The dual-register enforcement is expressed as explicitly labeled, structurally distinct sections -- e.g., "Obligation:" and "Existence condition:" -- accompanied by a non-substitutability declaration and explanation of what each distinctly conveys. An output satisfying C-29 automatically satisfies C-26 (and therefore C-24, C-22); the converse is not true. |
| C-30 | Rule body names the inadequacy of status framing before introducing existence framing -- step-up disclaimer | step-up-framing | The rule body names why rule-status framing ("not operative") understates the condition before introducing the existence claim. An output satisfying C-30 automatically satisfies C-27 (and therefore C-24, C-22); the converse is not true. |
| C-31 | Temporal gate expressed as "at rule-creation time" -- creation-time contract | creation-time | The temporal activation gate is expressed as "at rule-creation time" (or equivalent) rather than "before becoming active." An output satisfying C-31 automatically satisfies C-22 (and therefore C-20); the converse is not true. |
| C-32 | Location annotation explicitly covers rules not yet written -- forward-scope Applies-to | forward-scope | The location annotation explicitly covers rules not yet written -- e.g., "Applies to: Rule 1, Rule 2, Rule 3 (including Rule 3 itself and any rule added in the future)." An output satisfying C-32 automatically satisfies C-20; the converse is not true. |
| C-33 | Non-substitutability declaration assigns a distinct function description to each register -- action-spec vs. loss-model | reader-function-framing | The non-substitutability declaration assigns a distinct function description to each register: obligation register as action-spec ("tells you what to do") and existence-condition register as loss-model ("tells you what you lose if you do not"). An output satisfying C-33 automatically satisfies C-29 (and therefore C-26, C-24, C-22, C-20); the converse is not true. |
| C-34 | Each rule's heading or inline label encodes its failure class, making violation-to-type mapping achievable from rule label alone | diagnostic-label | Each rule's heading or inline label encodes its assigned failure class. An output satisfying C-34 automatically satisfies C-21; the converse is not true. |
| C-35 | Failure class encoded directly in the top-level rule heading, making diagnostic taxonomy recoverable from a top-level heading scan | diagnostic-heading | The top-level rule heading encodes the rule's failure class directly -- e.g., "Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:". An output satisfying C-35 automatically satisfies C-34 (and therefore C-21); the converse is not true. |
| C-36 | Reader-position named explicitly in function framing -- specific reader role named for each register | reader-position-framing | The function framing names a specific reader position and decision act for each register rather than using the generic "you." An output satisfying C-36 automatically satisfies C-33 (and therefore C-29, C-26, C-24, C-22, C-20); the converse is not true. |
| C-37 | ENFORCEMENT STACK NOTE collapses per-rule failure-class labels to forward-references to top-level headings, making the heading the single source of truth | forward-reference-dedup | Once C-35 is satisfied, the NOTE uses forward-reference pointers for each rule rather than restating the failure-class label inline. C-37 cannot be satisfied without C-35; C-35 does not imply C-37. |
| C-38 | Each rule in the STANDING RULES block names its own reader position keyed to that rule's specific failure mode | per-rule-reader-position | Every rule -- not only Rule 3's non-substitutability declaration -- names a specific reader position and consulting act keyed to that rule's failure mode. An output satisfying C-38 automatically satisfies C-36 (and therefore C-33, C-29, C-26, C-24, C-22, C-20); the converse is not true. |
| C-39 | ENFORCEMENT STACK NOTE reduced to a pure interdependency statement after C-37 collapses inline labels to forward-references | note-pure-interdependency | Once C-37 is satisfied, the NOTE's remaining content is limited exclusively to the interdependency relationship between the three rules -- without retaining explanatory prose about what each rule prevents. C-39 requires C-37 as a precondition; C-37 does not imply C-39. |
| C-40 | Per-rule reader positions surfaced as an explicit consulting directory naming all three reader routes together | consulting-directory | The per-rule reader positions required by C-38 are additionally surfaced as an explicit consulting directory routing each team member to the relevant rule by role name, rule number, and decision act. C-40 requires C-38 as a precondition; C-38 does not imply C-40. An output satisfying C-40 automatically satisfies C-38 (and therefore C-36, C-33, C-29, C-26, C-24, C-22, C-20). |
| C-41 | Pure interdependency NOTE attributes failure-mode ownership to top-level headings, making its reduced content self-explaining | note-self-explaining-transfer | The NOTE includes an explicit attribution of failure-mode ownership to the top-level rule headings so that the NOTE's omission of "prevents..." prose is self-explaining. C-41 requires C-39 as a precondition; C-39 does not imply C-41. An output satisfying C-41 automatically satisfies C-39 (and therefore C-37). |
| C-42 | Consulting directory carries an explicit completeness assertion making role coverage verifiable from the directory alone | directory-completeness-claim | The consulting directory carries an explicit completeness assertion -- either a stated all-roles claim or a structural count annotation -- making the directory's coverage verifiable from the directory alone. C-42 requires C-40 as a precondition; C-40 does not imply C-42. An output satisfying C-42 automatically satisfies C-40 (and the full chain to C-20). |
| C-43 | Consulting directory's completeness assertion uses all-roles claim form, not count-annotation form | directory-all-roles-claim | The completeness assertion is expressed as an explicit all-roles claim -- e.g., "All reader roles for this block are listed above." -- rather than a structural count annotation, so that coverage is asserted as a direct proposition requiring no reader arithmetic. C-43 requires C-42 as a precondition; C-42 does not imply C-43. An output satisfying C-43 automatically satisfies C-42 (and therefore C-40 and the full chain to C-20). |
| C-44 | All-roles claim includes an embedded count qualifier, making the assertion both propositional and arithmetically cross-checkable | directory-count-qualified-claim | The all-roles claim includes an embedded count qualifier -- e.g., "All 3 reader roles for this block are listed above." -- so that the assertion is both propositionally verifiable and arithmetically cross-checkable; the count is nested within the proposition as a qualifier rather than serving as the assertion mechanism. C-44 requires C-43 as a precondition; C-43 does not imply C-44; C-44 is independently testable from C-45. |
| C-45 | Failure-mode ownership attribution extended with a parenthetical heading index naming which specific top-level heading owns each failure class | note-heading-index | The failure-mode ownership attribution is extended with a parenthetical heading index -- e.g., "(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)" -- so that a reader scanning only the NOTE can navigate directly to the heading for a given failure class. C-45 requires C-41 as a precondition; C-41 does not imply C-45; C-45 is independently testable from C-44. |
| C-46 | Dual count consistency -- count qualifier in the all-roles claim (C-44) and entry count of the parenthetical heading index (C-45) are numerically consistent and independently cross-checkable | cross-count-consistency | The count qualifier in the all-roles claim and the entry count of the parenthetical heading index are numerically consistent and independently verifiable against each other. C-46 requires both C-44 and C-45 as preconditions; C-44 and C-45 together do not imply C-46; an output satisfying C-46 automatically satisfies C-44 and C-45 (and therefore C-43, C-42, C-41, C-40, and the full chain to C-20). |
| C-47 | READINESS SUMMARY includes a dimensional-status preamble naming all four dimension statuses before pilot-briefing prose | summary-status-preamble | The READINESS SUMMARY section includes a dimensional-status preamble -- a structured block naming all four dimension statuses before the pilot-briefing prose -- so that the full STATUS picture is recoverable from the summary block alone without reading any preflight dimension items; an output satisfying C-11 via a prose-only READINESS SUMMARY satisfies C-11 but not C-47; C-47 requires C-11 as a precondition; C-11 does not imply C-47; an output satisfying C-47 automatically satisfies C-11 (and therefore C-06); C-47 is independently testable from C-48 and C-49; boundary confirmed clean across V-01 through V-04 (all fail); V-05 passes. Derived from R18. |
| C-48 | Every section header carries a section-function annotation naming the section's knowledge type and reader purpose | section-function-annotation | Every section header carries a section-function annotation -- a bracketed or inline label naming the section's knowledge type and reader purpose -- so that the output's lifecycle architecture and the epistemic role of each section are recoverable from a heading scan alone without reading any section body; "every section header" means all named section headers, without exception; an output carrying section names only satisfies C-06 to C-09 but not C-48; C-48 is independently testable and requires no precondition in the established criterion chain; C-48 is independently testable from C-47 and C-49. Derived from R18. |
| C-49 | Triple-vector advisory register -- per-item coaching vocabulary, per-section function annotations, and per-summary dimensional-status preamble co-present in one output | advisory-register-saturation | The output simultaneously expresses advisory register at three independent levels of structural granularity -- (1) per-item coaching vocabulary (C-18), (2) per-section function annotations (C-48), and (3) per-summary dimensional-status preamble (C-47) -- making register drift structurally improbable; an output satisfying any two of the three levels satisfies those criteria individually but not C-49: the triple-vector saturation requires co-presence of all three vectors; C-49 requires C-18, C-47, and C-48 as preconditions; C-18, C-47, and C-48 together do not imply C-49 (co-presence is independently checkable); an output satisfying C-49 automatically satisfies C-18, C-47, and C-48. Derived from R18. |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Composite Score Formula

```
composite = 90 + (aspirational_pass / 41) * 10
```

- Perfect aspirational sweep: 100
- No aspirational criteria: 90
- Gold threshold: composite >= 80 (reachable with 0 aspirational passes if all essential pass)

---

## Version History

| Version | Change |
|---------|--------|
| v1 | C-01 through C-10 |
| v2 | C-11 through C-13 (R1 excellence signals) |
| v3 | C-14 through C-16 (R2 excellence signals) |
| v4 | C-17 through C-19 (R3 excellence signals) |
| v5 | C-20 through C-21 (R4 excellence signals) |
| v6 | C-22 through C-23 (R5 excellence signals); composite denominator 13 -> 15 |
| v7 | C-24 through C-25 (R6 excellence signals); composite denominator 15 -> 17 |
| v8 | C-26 through C-27 (R7 excellence signals); composite denominator 17 -> 19 |
| v9 | C-28 through C-32 (R8 excellence signals); composite denominator 19 -> 24 |
| v10 | C-33 through C-34 (R9 excellence signals); composite denominator 24 -> 26 |
| v11 | C-35 through C-36 (R10 excellence signals); composite denominator 26 -> 28 |
| v12 | C-37 through C-38 (R11 excellence signals); composite denominator 28 -> 30 |
| v13 | C-39 through C-40 (R12 excellence signals); composite denominator 30 -> 32 |
| v14 | C-41 through C-42 (R13 excellence signals); composite denominator 32 -> 34 |
| v15 | C-43 (R14 excellence signal); composite denominator 34 -> 35 |
| v16 | C-44 through C-45 (R15 excellence signals); composite denominator 35 -> 37 |
| v17 | C-46 (R16 excellence signal); composite denominator 37 -> 38 |
| v18 | C-47 through C-49 (R18 excellence signals); composite denominator 38 -> 41 |

---

**Summary of v18 changes:**

- **3 new criteria**: C-47 (summary-status-preamble), C-48 (section-function-annotation), C-49 (advisory-register-saturation)
- **Denominator**: 38 -> 41
- **New subsumption root**: C-49 subsumes C-47, C-48, and C-18 simultaneously — the first multi-parent subsumption in the chain not rooted in C-20
- **C-47** introduces the first criterion outside the STANDING RULES axis that subsumes from C-11 (rather than C-20)
- **C-48** is the first criterion with no precondition in the established chain — independently testable from the ground up
