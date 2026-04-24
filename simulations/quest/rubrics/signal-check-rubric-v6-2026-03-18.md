Reading the R5 scorecard, the excellence signals worth promoting come from the C-20 variation analysis — specifically the delta between V-04 (compact pass) and V-05 (fullest form):

1. **V-05 "before becoming active"** — the meta-rule is expressed as an activation gate, not just a policy declaration. C-20 only requires the meta-rule to exist and self-apply; this tightens it to a procedural precondition on rule validity.

2. **V-05 self-application in rule body, not only in Applies-to** — `"This requirement self-applies: Rule 3 itself declares its scope below."` appears in the rule text, making the self-reference parseable without inspecting the location annotation. V-04 passes C-20 with `"all Rule declarations"` but the self-reference is only implicit via universal quantifier.

Those become **C-22** and **C-23**. Composite denominator moves from 13 → 15.

---

```markdown
# signal-check Rubric — v6 (2026-03-18)

Evaluates the output of `/signal:check` against quality criteria derived from iterative design
experiments. Three tiers: Essential (gate), Recommended (depth), Aspirational (excellence). Gold
requires all essential passing and composite >= 80.

---

## Criterion Summary

**5 Essential** — all must pass for the output to be a usable health report:

| ID | Criterion |
|----|-----------|
| C-01 | All four dimensions present (SEQUENCE, COHERENCE, STALENESS, CAUSAL GAP) |
| C-02 | SEQUENCE grounded in artifact dates, not assumed ordering |
| C-03 | COHERENCE names specific signal pairs — not generic "seems aligned" |
| C-04 | CAUSAL GAP states mechanism evidence or explicitly names the absence |
| C-05 | Advisory/coaching register throughout — no blocking verdicts |

**3 Recommended** — meaningfully better with all three:

| ID | Criterion |
|----|-----------|
| C-06 | STALENESS applies a named, concrete age threshold |
| C-07 | Every flagged issue includes a next action |
| C-08 | Report opens with a readiness summary before dimension analysis |

**15 Aspirational** — raise the bar once essentials are stable. C-09 and C-10 retained from v1;
C-11 through C-13 added from R1; C-14 through C-16 added from R2; C-17 through C-19 added from R3;
C-20 and C-21 added from R4; C-22 and C-23 added from R5:

| ID | Criterion | Source |
|----|-----------|--------|
| C-09 | Cross-dimension patterns named when a shared root cause exists | v1 |
| C-10 | Missing signals identified by namespace + specific skill | v1 |
| C-11 | All skill references use `/namespace:skill` format consistently | EX-01 |
| C-12 | A terminal MISSING SIGNAL GUIDE section collates all gaps | EX-02 |
| C-13 | Absent evidence is declared explicitly — no dimension silently omits | EX-03 |
| C-14 | A named STANDING RULES block precedes all inventory and analysis | EX-04 |
| C-15 | Each dimension specifies required verbatim absence phrases | EX-05 |
| C-16 | Every constraint explicitly enumerates all output locations it governs | EX-06 |
| C-17 | Verbatim absence phrases are embedded at point of use within each dimension | R3-EX-01 |
| C-18 | Advisory register is carried structurally through framing vocabulary, not only declared | R3-EX-02 |
| C-19 | The triple enforcement stack (C-14 + C-15 + C-16) is declared as a unit with interdependency named | R3-EX-03 |
| C-20 | Location-enumeration requirement is expressed as a named meta-rule governing all rule declarations | R4-EX-01 |
| C-21 | Each rule in the enforcement stack is assigned a named failure class | R4-EX-02 |
| C-22 | The location-enumeration meta-rule includes a temporal activation gate | R5-EX-01 |
| C-23 | Meta-rule self-application is declared within the rule body, not solely in the location annotation | R5-EX-02 |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Criterion Detail

### Essential (C-01 to C-05)

*(unchanged from v3)*

### Recommended (C-06 to C-08)

*(unchanged from v3)*

### Aspirational (C-09 to C-23)

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

---

## Composite Score Formula

```
composite = 90 + (aspirational_pass / 15) * 10
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
```
