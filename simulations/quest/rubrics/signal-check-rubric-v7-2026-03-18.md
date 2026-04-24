Here is the complete updated rubric:

---

# signal-check Rubric — v7 (2026-03-18)

**Two new criteria extracted from R6 V-04:**

## What R6 revealed

**C-24** comes from the C-22 evidence in V-04: *"a rule cannot be operative until scope is discharged."* C-22 only requires a temporal gate to exist; C-24 captures the semantic property the gate must carry — **validity framing** (rule is not-operative/invalid) vs. policy framing (rule obligates compliance). Those are structurally different: obligation non-compliance is a breach; validity non-compliance means the rule simply does not exist yet as an operative rule. Stronger guarantee.

**C-25** comes from the C-23 evidence in V-04: `"Rule 3 itself declares its scope below."` C-23 requires self-application in the rule body; C-25 captures the positional anchor embedded in V-04's implementation — the word "below" creates a **co-location contract** between the rule body and the Applies-to annotation. Without the pointer, scope can drift to a different section. With it, a reader knows exactly where to look without searching.

## Criterion additions

| ID | Criterion | Source |
|----|-----------|--------|
| C-24 | Activation gate framed as a rule-validity condition — meta-rule states it is not operative until scope is discharged, making non-compliance a validity failure rather than a policy violation | R6-EX-01 |
| C-25 | Body self-application includes a proximate scope pointer (e.g., "declares its scope below") that creates a co-location contract between the rule body and the Applies-to annotation | R6-EX-02 |

## Updated parameters

- Aspirational count: 15 → **17**
- Formula: `composite = 90 + (aspirational_pass / 17) * 10`
- An output satisfying C-24 automatically satisfies C-22; C-25 automatically satisfies C-23

Written to `simulations/quest/rubrics/signal-check-rubric-v7-2026-03-18.md`.
G RULES block precedes all inventory and analysis | EX-04 |
| C-15 | Each dimension specifies required verbatim absence phrases | EX-05 |
| C-16 | Every constraint explicitly enumerates all output locations it governs | EX-06 |
| C-17 | Verbatim absence phrases are embedded at point of use within each dimension | R3-EX-01 |
| C-18 | Advisory register is carried structurally through framing vocabulary, not only declared | R3-EX-02 |
| C-19 | The triple enforcement stack (C-14 + C-15 + C-16) is declared as a unit with interdependency named | R3-EX-03 |
| C-20 | Location-enumeration requirement is expressed as a named meta-rule governing all rule declarations | R4-EX-01 |
| C-21 | Each rule in the enforcement stack is assigned a named failure class | R4-EX-02 |
| C-22 | The location-enumeration meta-rule includes a temporal activation gate | R5-EX-01 |
| C-23 | Meta-rule self-application is declared within the rule body, not solely in the location annotation | R5-EX-02 |
| C-24 | The activation gate is framed as a rule-validity condition — the meta-rule is stated as not operative until scope is discharged, making non-compliance a validity failure rather than a policy violation | R6-EX-01 |
| C-25 | The body self-application includes a proximate scope pointer (e.g., "declares its scope below") that creates a co-location contract between the rule body and the Applies-to annotation | R6-EX-02 |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Criterion Detail

### Essential (C-01 to C-05)

*(unchanged from v3)*

### Recommended (C-06 to C-08)

*(unchanged from v3)*

### Aspirational (C-09 to C-25)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09–C-16 | *(unchanged from v3)* | | |
| C-17 | Verbatim absence phrases embedded at point of use | correctness | The verbatim absence phrases required by C-15 appear inline within each dimension's instruction block — not solely in a pre-analysis reference table. Embedding phrases at point of use removes the table-lookup dependency; an output that satisfies C-15 via a standalone reference table does not satisfy C-17. An output satisfying C-17 automatically satisfies C-15; the converse is not true. Derived from R3: verbatim-phrase-at-point-of-use outperforms reference-table for C-15 compliance. |
| C-18 | Advisory register carried structurally through framing vocabulary | register | The advisory/coaching register required by C-05 is expressed through the structural vocabulary of the output — section headings, dimension labels, and status fields use framing language (e.g., preflight/pilot/clearance, coaching check, advisory) rather than relying solely on a top-of-file disclaimer. A disclaimer alone satisfies C-05 but not C-18; structural framing prevents register drift across the output more reliably than declaration alone. Derived from R3: preflight/pilot framing in V-05 carries the advisory register structurally, not just declaratively. |
| C-19 | Triple enforcement stack declared as a unit with interdependency named | coherence | The output or skill instruction explicitly names C-14, C-15, and C-16 (or their functional equivalents — named preamble block, verbatim phrases per dimension, full location enumeration) as a coordinated enforcement stack, and states that the three mechanisms address independent failure modes such that no layer substitutes for another. Passing all three independently without naming their interdependency does not satisfy C-19. Derived from R3: the triple enforcement stack addresses three distinct failure modes; no two layers substitute for the third. |
| C-20 | Location-enumeration requirement expressed as a named meta-rule | forward-compatibility | The location-enumeration requirement (C-16) is expressed as an explicit named rule in the STANDING RULES block that self-applies to all rule declarations including itself — not only as "Applies to:" lines on individual rules. The meta-rule pattern makes the location-scope requirement durable against future rule additions: any new rule added must also enumerate its locations because the meta-rule covers it. An output that satisfies C-16 via "Applies to:" annotations on individual rules but carries no meta-rule governing rule declarations does not satisfy C-20. An output satisfying C-20 automatically satisfies C-16; the converse is not true. Derived from R4: Rule 3 in V-05 closes the forward-compatibility gap present in V-04, where a hypothetical future Rule 4 would not automatically require location enumeration. |
| C-21 | Each rule in the enforcement stack is assigned a named failure class | diagnostic | The enforcement stack declaration required by C-19 assigns a named failure class to each rule (e.g., absence drift, reference ambiguity, constraint scope gaps). Naming failure modes transforms the stack from a list of prohibitions into a diagnostic taxonomy: a reviewer classifying a violation can map it to a failure mode type from the rule name alone without reading the full rule body. An output that satisfies C-19 by declaring the three-rule stack and its interdependency without enumerating what each rule prevents does not satisfy C-21. C-21 is independently testable from C-19: the stack can be named without failure-mode labels, or failure-mode labels can appear without an explicit interdependency declaration. Derived from R4: the ENFORCEMENT STACK NOTE in V-05 assigns failure-class labels (absence drift / reference ambiguity / constraint scope gaps) independently of the stack interdependency statement. |
| C-22 | Location-enumeration meta-rule includes a temporal activation gate | forward-compatibility | The meta-rule required by C-20 includes a temporal enforcement condition — e.g., "before becoming active," "before taking effect," or equivalent — that makes scope declaration a precondition for a rule's validity rather than a retroactive policy statement. A meta-rule that states the enumeration requirement as a standing obligation satisfies C-20; one that additionally specifies when the obligation must be discharged (at rule-creation time, before the rule is operative) satisfies C-22. The activation gate eliminates the ambiguity present in policy-only wording: a rule cannot be considered "in force" without having discharged the scope requirement first. An output satisfying C-22 automatically satisfies C-20; the converse is not true. Derived from R5: V-05's "before becoming active" language makes forward-compatibility operational — a future rule cannot be treated as active unless its scope is already declared. |
| C-23 | Meta-rule self-application declared in rule body, not solely in location annotation | self-reference | The meta-rule required by C-20 states its own self-applicability within the rule body text (e.g., "This requirement self-applies: Rule N itself declares its scope below"), not solely through the "Applies to:" location annotation. A meta-rule that achieves self-application only via a universal quantifier in the Applies-to line (e.g., "Applies to: all Rule declarations in this block") satisfies C-20 because the quantifier implicitly covers the meta-rule itself; however, the self-reference is only recoverable by inference — a reader must recognise that the meta-rule is itself a Rule declaration. Body-level self-declaration makes the self-reference explicit and parseable without inspecting the location annotation, eliminating the inferential step. An output satisfying C-23 automatically satisfies C-20; the converse is not true. Derived from R5: V-05's body text "This requirement self-applies: Rule 3 itself declares its scope below" makes self-reference unambiguous independently of the Applies-to line; V-04's compact form satisfies C-20 but requires inference to establish self-application. |
| C-24 | Activation gate framed as a rule-validity condition, not a policy obligation | validity-framing | The temporal activation gate required by C-22 is expressed as a validity condition: the meta-rule states that it is not operative (not in force, not valid) until scope is discharged, rather than stating that scope must be declared (an obligation that could be complied with retroactively). The distinction is: "obligation" framing means a rule exists and requires future compliance; "validity" framing means the rule does not exist as an operative rule until the condition is met. An output that satisfies C-22 via obligation language ("must declare locations before becoming active") but does not state that the rule is invalid / not-operative in the absence of scope discharge does not satisfy C-24. Validity framing makes non-compliance a rule-existence failure, not a rule-compliance failure — a stronger guarantee than temporal obligation alone. Derived from R6: V-04's evidence "a rule cannot be operative until scope is discharged" identifies the validity-conditional framing as the operative property; C-22 captures gate presence, C-24 captures gate semantics. |
| C-25 | Body self-application includes a proximate scope pointer creating a co-location contract | layout-contract | The body self-application statement required by C-23 includes a directional pointer (e.g., "declares its scope below," "scope follows immediately") that commits the Applies-to annotation to immediate co-location with the rule body. A meta-rule that states "this requirement self-applies" without a positional anchor satisfies C-23; one that additionally specifies the scope annotation's required position satisfies C-25. The proximate pointer prevents scope displacement — the Applies-to cannot be moved to a separate reference section or document footer without violating the pointer's contract. Readers can verify scope without searching the document: the rule body's directional reference tells them exactly where to look. An output satisfying C-25 automatically satisfies C-23; the converse is not true. Derived from R6: V-04's body text "Rule 3 itself declares its scope below" encodes a layout contract absent from a bare self-application statement; the "below" pointer is the criterion's key distinguishing element. |

---

## Composite Score Formula

```
composite = 90 + (aspirational_pass / 17) * 10
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
| v6 | C-22 through C-23 (R5 excellence signals); composite denominator 13 → 15 |
| v7 | C-24 through C-25 (R6 excellence signals); composite denominator 15 → 17 |
