Here is the complete v9 rubric written to `simulations/quest/rubrics/signal-check-rubric-v9-2026-03-18.md`.

---

**What changed from v8 to v9:**

Five new criteria extracted from R8 V-05, all independently sourced from distinct structural properties that V-04 lacks:

| ID | Criterion | Category | Subsumes |
|----|-----------|----------|---------|
| C-28 | Rule name encodes existence assertion (heading-level ontological claim) | heading-encoding | none (independently testable from C-27) |
| C-29 | Dual register as structurally labeled sections with non-substitutability declaration | dual-register-structure | C-26 -> C-24 -> C-22 |
| C-30 | Step-up disclaimer naming inadequacy of status framing before introducing existence claim | step-up-framing | C-27 -> C-24 -> C-22 |
| C-31 | Temporal gate tightened to "at rule-creation time" (creation-time contract) | creation-time | C-22 -> C-20 |
| C-32 | Location annotation covers rules not yet written (forward-scope Applies-to) | forward-scope | C-20 |

**Updated parameters:**
- Aspirational count: 19 → **24**
- Formula: `composite = 90 + (aspirational_pass / 24) * 10`
- V-05 scores 24/24 = 100.00 under v9; V-04 drops to 19/24 = 97.92

**C-28 structural note:** It sits outside all subsumption chains. The heading can encode the existence claim without the body carrying C-27 framing, and C-27 body framing is achievable with a generic rule label. They test different structural locations and neither implies the other.
cy of status framing before introducing existence framing. The reader sees *why* the existence claim is stronger, not just that it is stronger. An output satisfying C-30 automatically satisfies C-27; naming the inadequacy requires the stronger claim to be present. Derived from R8: V-05 encodes the C-24/C-27 distinction as a visible upgrade within the rule body.

**C-31** comes from V-05's "scope must be discharged at rule-creation time, not retroactively." C-22 requires a temporal gate ("before becoming active"); C-31 captures the **creation-time contract** — the discharge point is tightened from activation to creation, foreclosing the edge case where creation and activation are construed as distinct events. An output satisfying C-31 automatically satisfies C-22; the converse is not true.

**C-32** comes from V-05's "including Rule 3 itself and any rule added in the future." C-20 requires the meta-rule to govern all existing rule declarations; C-32 captures **forward-scope** — the location annotation explicitly covers rules not yet written, making the meta-rule self-extending without requiring amendment when a new rule is added. An output satisfying C-32 automatically satisfies C-20; the converse is not true.

## Criterion additions

| ID | Criterion | Source |
|----|-----------|--------|
| C-28 | Rule name (heading in STANDING RULES block) encodes the existence assertion — ontological claim recoverable from rule name without body inspection | R8-EX-01 |
| C-29 | Dual-register enforcement expressed as structurally labeled, named sections with explicit non-substitutability declaration — dual-register made surface-parseable without reading prose | R8-EX-02 |
| C-30 | Rule body explicitly names the inadequacy of rule-status framing before introducing existence framing — step-up disclaimer making the C-24/C-27 distinction visible as a named upgrade | R8-EX-03 |
| C-31 | Temporal gate tightened from "before becoming active" to "at rule-creation time" — creation-time contract that forecloses activation/creation ambiguity | R8-EX-04 |
| C-32 | Location annotation explicitly covers rules not yet written ("any rule added in the future") — forward-scope Applies-to making the meta-rule self-extending | R8-EX-05 |

## Updated parameters

- Aspirational count: 19 -> **24**
- Formula: `composite = 90 + (aspirational_pass / 24) * 10`
- C-29 automatically satisfies C-26 (and therefore C-24, C-22, C-20)
- C-30 automatically satisfies C-27 (and therefore C-24, C-22, C-20)
- C-31 automatically satisfies C-22 (and therefore C-20)
- C-32 automatically satisfies C-20
- C-28 is independently testable from C-27 (heading-level vs body-level)

## Subsumption chains

```
C-20 <- C-22 <- C-24 <- C-26 <- C-29
                C-24 <- C-27 <- C-30
C-20 <- C-23 <- C-25
C-22 <- C-31
C-20 <- C-32
C-28  (independently testable -- heading-level, not body-level)
```

R8 V-05 scores 24/24 under v9. V-04 scores 19/24 (FAIL C-28, C-29, C-30, C-31, C-32). V-01 and V-03 score 18/24. V-02 scores 17/24.

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
| C-17 | Verbatim absence phrases are embedded at point of use within each dimension | R3-EX-01 |
| C-18 | Advisory register is carried structurally through framing vocabulary, not only declared | R3-EX-02 |
| C-19 | The triple enforcement stack (C-14 + C-15 + C-16) is declared as a unit with interdependency named | R3-EX-03 |
| C-20 | Location-enumeration requirement is expressed as a named meta-rule governing all rule declarations | R4-EX-01 |
| C-21 | Each rule in the enforcement stack is assigned a named failure class | R4-EX-02 |
| C-22 | The location-enumeration meta-rule includes a temporal activation gate | R5-EX-01 |
| C-23 | Meta-rule self-application is declared within the rule body, not solely in the location annotation | R5-EX-02 |
| C-24 | The activation gate is framed as a rule-validity condition -- the meta-rule is stated as not operative until scope is discharged, making non-compliance a validity failure rather than a policy violation | R6-EX-01 |
| C-25 | The body self-application includes a proximate scope pointer (e.g., "declares its scope below") that creates a co-location contract between the rule body and the Applies-to annotation | R6-EX-02 |
| C-26 | The activation gate carries both obligation framing ("must declare... before becoming active") and validity framing ("is not operative / does not exist as an active rule") in the same rule body, creating dual-register enforcement | R7-EX-01 |
| C-27 | The validity condition uses rule-existence framing -- the rule "does not exist as an active rule" -- rather than solely rule-status framing ("is not operative") | R7-EX-02 |
| C-28 | The rule name (heading in STANDING RULES block) encodes the existence assertion in declarative form (e.g., "RULES WITHOUT DECLARED SCOPE DO NOT EXIST"), making the ontological claim recoverable without reading the body | R8-EX-01 |
| C-29 | The dual register required by C-26 is expressed as structurally labeled, named sections (e.g., "Obligation:" / "Existence condition:") with an explicit non-substitutability declaration and an explanation of what each register distinctly conveys | R8-EX-02 |
| C-30 | The rule body explicitly names the inadequacy of rule-status framing before introducing the existence claim -- step-up disclaimer stating why "not operative" understates the condition and making the C-24/C-27 distinction visible as a named upgrade | R8-EX-03 |
| C-31 | The temporal gate is expressed as "at rule-creation time" (or equivalent), tightening beyond "before becoming active" and foreclosing any edge case where creation and activation are construed as distinct events | R8-EX-04 |
| C-32 | The location annotation of the meta-rule explicitly covers rules not yet written (e.g., "including any rule added in the future"), making the meta-rule self-extending without requiring amendment when a new rule is added | R8-EX-05 |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Criterion Detail

### Essential (C-01 to C-05)

*(unchanged from v3)*

### Recommended (C-06 to C-08)

*(unchanged from v3)*

### Aspirational (C-09 to C-32)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09-C-16 | *(unchanged from v3)* | | |
| C-17 | Verbatim absence phrases embedded at point of use | correctness | The verbatim absence phrases required by C-15 appear inline within each dimension's instruction block -- not solely in a pre-analysis reference table. Embedding phrases at point of use removes the table-lookup dependency; an output that satisfies C-15 via a standalone reference table does not satisfy C-17. An output satisfying C-17 automatically satisfies C-15; the converse is not true. Derived from R3: verbatim-phrase-at-point-of-use outperforms reference-table for C-15 compliance. |
| C-18 | Advisory register carried structurally through framing vocabulary | register | The advisory/coaching register required by C-05 is expressed through the structural vocabulary of the output -- section headings, dimension labels, and status fields use framing language (e.g., preflight/pilot/clearance, coaching check, advisory) rather than relying solely on a top-of-file disclaimer. A disclaimer alone satisfies C-05 but not C-18; structural framing prevents register drift across the output more reliably than declaration alone. Derived from R3: preflight/pilot framing in V-05 carries the advisory register structurally, not just declaratively. |
| C-19 | Triple enforcement stack declared as a unit with interdependency named | coherence | The output or skill instruction explicitly names C-14, C-15, and C-16 (or their functional equivalents -- named preamble block, verbatim phrases per dimension, full location enumeration) as a coordinated enforcement stack, and states that the three mechanisms address independent failure modes such that no layer substitutes for another. Passing all three independently without naming their interdependency does not satisfy C-19. Derived from R3: the triple enforcement stack addresses three distinct failure modes; no two layers substitute for the third. |
| C-20 | Location-enumeration requirement expressed as a named meta-rule | forward-compatibility | The location-enumeration requirement (C-16) is expressed as an explicit named rule in the STANDING RULES block that self-applies to all rule declarations including itself -- not only as "Applies to:" lines on individual rules. The meta-rule pattern makes the location-scope requirement durable against future rule additions: any new rule added must also enumerate its locations because the meta-rule covers it. An output that satisfies C-16 via "Applies to:" annotations on individual rules but carries no meta-rule governing rule declarations does not satisfy C-20. An output satisfying C-20 automatically satisfies C-16; the converse is not true. Derived from R4: Rule 3 in V-05 closes the forward-compatibility gap present in V-04, where a hypothetical future Rule 4 would not automatically require location enumeration. |
| C-21 | Each rule in the enforcement stack is assigned a named failure class | diagnostic | The enforcement stack declaration required by C-19 assigns a named failure class to each rule (e.g., absence drift, reference ambiguity, constraint scope gaps). Naming failure modes transforms the stack from a list of prohibitions into a diagnostic taxonomy: a reviewer classifying a violation can map it to a failure mode type from the rule name alone without reading the full rule body. An output that satisfies C-19 by declaring the three-rule stack and its interdependency without enumerating what each rule prevents does not satisfy C-21. C-21 is independently testable from C-19. Derived from R4: the ENFORCEMENT STACK NOTE in V-05 assigns failure-class labels (absence drift / reference ambiguity / constraint scope gaps) independently of the stack interdependency statement. |
| C-22 | Location-enumeration meta-rule includes a temporal activation gate | forward-compatibility | The meta-rule required by C-20 includes a temporal enforcement condition -- e.g., "before becoming active," "before taking effect," or equivalent -- that makes scope declaration a precondition for a rule's validity rather than a retroactive policy statement. The activation gate eliminates the ambiguity present in policy-only wording: a rule cannot be considered "in force" without having discharged the scope requirement first. An output satisfying C-22 automatically satisfies C-20; the converse is not true. Derived from R5: V-05's "before becoming active" language makes forward-compatibility operational -- a future rule cannot be treated as active unless its scope is already declared. |
| C-23 | Meta-rule self-application declared in rule body, not solely in location annotation | self-reference | The meta-rule required by C-20 states its own self-applicability within the rule body text (e.g., "This requirement self-applies: Rule N itself declares its scope below"), not solely through the "Applies to:" location annotation. Body-level self-declaration makes the self-reference explicit and parseable without inspecting the location annotation, eliminating the inferential step required when self-application is implicit in a universal quantifier. An output satisfying C-23 automatically satisfies C-20; the converse is not true. Derived from R5: V-05's body text "This requirement self-applies: Rule 3 itself declares its scope below" makes self-reference unambiguous independently of the Applies-to line. |
| C-24 | Activation gate framed as a rule-validity condition, not a policy obligation | validity-framing | The temporal activation gate required by C-22 is expressed as a validity condition: the meta-rule states that it is not operative (not in force, not valid) until scope is discharged, rather than stating only that scope must be declared (an obligation that could be complied with retroactively). Validity framing makes non-compliance a rule-existence failure, not a rule-compliance failure -- a stronger guarantee than temporal obligation alone. An output that satisfies C-22 via obligation language but does not state that the rule is invalid / not-operative in the absence of scope discharge does not satisfy C-24. Derived from R6: C-22 captures gate presence, C-24 captures gate semantics. |
| C-25 | Body self-application includes a proximate scope pointer creating a co-location contract | layout-contract | The body self-application statement required by C-23 includes a directional pointer (e.g., "declares its scope below," "scope follows immediately") that commits the Applies-to annotation to immediate co-location with the rule body. The proximate pointer prevents scope displacement -- the Applies-to cannot be moved to a separate reference section or document footer without violating the pointer's contract. An output satisfying C-25 automatically satisfies C-23; the converse is not true. Derived from R6: V-04's body text "Rule 3 itself declares its scope below" encodes a layout contract absent from a bare self-application statement; "below" is the criterion's key distinguishing element. |
| C-26 | Activation gate carries both obligation framing and validity framing -- dual-register enforcement | dual-register | The activation gate required by C-24 also carries obligation language ("must declare all output locations... before becoming active" or equivalent) alongside the validity condition, so that both registers are present in the same rule body. A reader who discounts validity language as metaphorical still encounters the obligation constraint; a reader who treats obligation language as weak policy still encounters the existence-denial. An output satisfying C-26 automatically satisfies C-24 (and therefore C-22); the converse is not true. C-26 and C-27 are independently testable. Derived from R7: V-04 carries both obligation and validity registers; the dual-register structure is absent from V-01 (validity-only) and V-02 (obligation-only). |
| C-27 | Validity condition uses rule-existence framing rather than rule-status framing | ontological-validity | The validity condition required by C-24 states that the rule "does not exist as an active rule" (an ontological claim) rather than solely that it "is not operative" (a rule-status claim). "Not operative" admits the rule as a declared object with suspended force; "does not exist as an active rule" means the rule has no legal standing whatsoever until scope is discharged, eliminating partial-compliance arguments. An output satisfying C-27 automatically satisfies C-24; the converse is not true. C-27 is independently testable from C-26. Derived from R7: V-04's "it does not exist as an active rule" is the operative distinguishing element beyond C-24's "not operative" floor. |
| C-28 | Rule name encodes the existence assertion -- ontological claim recoverable from heading alone | heading-encoding | The rule name (label or heading used in the STANDING RULES block) encodes the existence assertion in declarative form -- e.g., "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" -- such that a reader scanning headings recovers the ontological claim before reading any body text. A rule satisfying C-27 via body text but carrying a generic label (e.g., "Rule 3: Location enumeration requirement") does not satisfy C-28. C-28 is independently testable from C-27: the heading can encode the claim without body framing repeating it, and C-27 body framing is achievable without a heading that encodes it. An output satisfying C-28 does not automatically satisfy C-27, nor vice versa -- both tests apply to different structural locations. Derived from R8: V-05's rule name "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" makes the existence claim visible before any body inspection; V-04 satisfies C-27 in the body but uses a label that does not encode it. |
| C-29 | Dual register expressed as structurally labeled named sections with non-substitutability declaration | dual-register-structure | The dual-register enforcement required by C-26 is expressed as explicitly labeled, structurally distinct sections -- e.g., "Obligation:" and "Existence condition:" -- accompanied by a declaration that neither register substitutes for the other and an explanation of what each distinctly conveys (e.g., "the obligation tells you what to do; the existence condition tells you what you lose if you do not"). An output that satisfies C-26 by carrying both registers in combined prose without labeling them does not satisfy C-29. An output satisfying C-29 automatically satisfies C-26 (and therefore C-24, C-22); the converse is not true. Derived from R8: V-05's labeled "Obligation:" and "Existence condition:" sections with explicit non-substitutability make the dual-register structure surface-parseable as a structural fact, not inferrable from prose. |
| C-30 | Rule body names the inadequacy of status framing before introducing existence framing -- step-up disclaimer | step-up-framing | The rule body required to carry the existence claim (C-27) additionally names why rule-status framing ("not operative") understates the condition before introducing the existence claim -- e.g., "'Not operative' understates the condition -- an inoperative rule is still a declared object with suspended force." The reader sees the distinction between C-24 and C-27 semantics as a named, explained upgrade rather than an unannounced assertion. An output that satisfies C-27 by stating the existence claim without naming the contrast with status framing does not satisfy C-30. An output satisfying C-30 automatically satisfies C-27 (and therefore C-24, C-22); the converse is not true. Derived from R8: V-05 encodes the step-up within the rule body; the distinction that makes C-27 stronger than C-24 is stated as a visible upgrade, not merely implied by the existence framing. |
| C-31 | Temporal gate expressed as "at rule-creation time" -- creation-time contract | creation-time | The temporal activation gate required by C-22 is expressed as "at rule-creation time" (or equivalent) rather than "before becoming active." "Before becoming active" permits edge cases where creation and activation are construed as separate events; "at rule-creation time" forecloses this by tying the discharge point to the act of rule creation itself, making any undischarged scope an immediate creation failure rather than a deferred activation failure. An output satisfying C-31 automatically satisfies C-22 (and therefore C-20); the converse is not true. Derived from R8: V-05's "scope must be discharged at rule-creation time, not retroactively" tightens the temporal gate beyond C-22's floor; the activation/creation distinction is the operative precision added. |
| C-32 | Location annotation explicitly covers rules not yet written -- forward-scope Applies-to | forward-scope | The location annotation of the meta-rule required by C-20 explicitly covers rules not yet written -- e.g., "Applies to: Rule 1, Rule 2, Rule 3 (including Rule 3 itself and any rule added in the future)." The forward-scope clause makes the meta-rule self-extending: a future Rule 4 is automatically governed without requiring an amendment to the Applies-to annotation. An output satisfying C-20 via an Applies-to listing only currently existing rules does not satisfy C-32. An output satisfying C-32 automatically satisfies C-20; the converse is not true. Derived from R8: V-05's "any rule added in the future" clause closes the forward-compatibility gap that C-20 opens but does not fully resolve -- a meta-rule governs existing rules by default; C-32 requires it to explicitly assert jurisdiction over future rules as well. |

---

## Composite Score Formula

```
composite = 90 + (aspirational_pass / 24) * 10
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
