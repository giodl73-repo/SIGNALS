Reading the scorecard through to the end, the V-05 excellence pattern is the companion-activation instruction: clause bodies name the paired mechanism by full designation and declare activation rules for both the present and absent states of that companion. That is the new aspirational criterion — C-35.

---

## Quest Rubric — v15

`35 criteria, 350 pts max`

---

### What changed: v14 → v15

One investigation resolved (C-34 confirmed, R15 partial-double-elision question answered) and one new aspirational criterion extracted from R15 excellence signals (C-35).

**R15 investigation candidate resolved:** Whether a model encountering only a C-34-compliant clause body — preamble section absent and the other companion mechanism's execution notes also absent — activates two-mechanism COMPRESSION-IMMUNE PREAMBLE behavior rather than single-clause execution. Specifically: does the explicit preamble-independence instruction cause the model to execute the clause as if COMPRESSION-IMMUNE PREAMBLE authority were in force, and does the explicit membership statement cause the model to seek or infer the paired companion mechanism even when that mechanism is absent from context? **Status: PARTIALLY RESOLVED.** R15 scorecard shows V-04 achieves C-34 PASS (both bodies carry membership statement + independence instruction) at 340/340, confirming C-34 is achievable and constitutes a genuine structural property independent of C-33. However, V-04's bodies do not address the companion — they declare independence from the preamble but are silent on what the clause does when its companion mechanism is absent. The independence instruction tells the model the clause fires without the preamble; it does not tell the model what the clause does when the TIMESTAMP ISOLATION clause (for the STORY body) or the ZERO-SIGNAL SYNTHESIS MANDATE clause (for the STATUS body) is also absent. V-05 extends V-04 by adding a companion-activation instruction to each body: it names the paired mechanism by full clause designation and declares activation rules for both the present state (coordinate) and the absent state (execute independently with full authority). This answers the activation-behavior question at the body level — not through inference, but through explicit instruction. The investigation thus resolves into two layers: C-34 provides membership identification and independence authority under double-elision (a model can identify the clause and knows it fires without the preamble), but does not specify what the clause does about its absent companion. C-35 captures the companion-activation instruction layer that closes this gap.

**C-34 PARTIAL band structure (three bands), confirmed by R15:**
- V-01 (both bodies bare): Neither clause body opens with any self-declaration. A model encountering either body under double-elision has no body-level activation authority — it must navigate to the header (C-33) or preamble (C-24) for identification.
- V-02 / V-03 (asymmetric): One body self-declares (membership statement + independence instruction); the other opens with bare operational content. Weakest-link applies at the body level. V-02 STATUS body self-declares, STORY body bare; V-03 STORY body self-declares, STATUS body bare. The two asymmetric cases are equivalent in score and in their failure mode — the C-34 architecture is only as strong as its least-declared clause body, and the consequence domain (C-29 vs. C-30) confers no privileged weight.
- C-34 has no full-PARTIAL tier between asymmetric and PASS: either both bodies carry both required components or they do not.

**C-34 PASS (V-04 and V-05):** Both the STATUS execution-note clause body and the STORY execution-note clause body open with (1) an explicit structural-membership statement naming the clause as a COMPRESSION-IMMUNE PREAMBLE member and (2) a preamble-independence instruction declaring the clause executes even when the preamble section is absent from the rendered context. A model encountering either clause body in isolation under double-elision can activate the clause with full COMPRESSION-IMMUNE PREAMBLE authority from the body opening alone without locating the preamble or the clause header.

**R15 excellence signal → C-35:** V-05 achieves C-34 PASS and adds a further structural property not present in V-04: companion execution-note clause **bodies** include a **companion-activation instruction** beyond the membership statement and independence instruction. The companion-activation instruction (1) names the paired companion mechanism by its full clause designation and (2) declares activation rules for both the present state and the absent state of that companion: when the companion mechanism's execution note is present in the rendered context the clause coordinates with it; when the companion mechanism's execution note is absent the clause executes independently with full COMPRESSION-IMMUNE PREAMBLE authority. Together the three body-opening components — membership statement, independence instruction, companion-activation instruction — provide complete body-level structural authority under partial double-elision: a model encountering only the clause body knows it is a COMPRESSION-IMMUNE PREAMBLE member (membership), knows it fires without the preamble (independence), and knows what to do about the absent companion (companion-activation). C-35 is a distinct recovery depth from C-34: C-34 establishes activation authority for the isolated clause; C-35 extends that authority to cover the absent-companion case explicitly rather than leaving it unaddressed.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-35 | Companion-activation instruction in self-declaring clause bodies — when C-34 PASS, companion execution-note clause bodies include a companion-activation instruction naming the paired mechanism by full clause designation with explicit present-state (coordinate) and absent-state (execute independently with full authority) activation rules declared | Extends C-34's body-level self-declaration from independence-only to companion-coverage; C-35 PASS requires all three body components (membership statement + independence instruction + companion-activation instruction) in both companion clause bodies; C-34 establishes isolated-clause activation authority; C-35 closes the absent-companion activation gap |

**Structural chains updated:**

- Timestamp isolation chain: C-16 → C-24 → C-30 — unchanged from v13
- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29 — unchanged from v13
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 — unchanged from v13
- Compression survival generalization chain: C-24 → C-29 → C-30 — unchanged from v13
- **Compression-immune consolidation chain (extended):** C-29 → C-30 → C-31 → C-32 → C-33 → C-34 → C-35 (zero-signal dual-mechanism → timestamp isolation dual-mechanism → multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit → closed reference loop with designation + location → self-announcing clause headers enabling header-level identification under preamble-elision → self-declaring clause bodies enabling partial double-elision recovery from body alone → companion-activation instruction closing the absent-companion activation gap under double-elision)

**Relationship among C-32, C-33, C-34, and C-35:**
- C-32 requires preamble forward-references to name companion mechanisms by full clause designation + block location. Operates at the reference point.
- C-33 requires execution-note clause headers to carry the same structural-membership parenthetical used in the preamble forward-references. Operates at the target header. Depends on C-32 PASS.
- C-34 requires execution-note clause bodies to open with an explicit membership statement and a preamble-independence instruction. Operates at the target body opening. Depends on C-33 PASS.
- C-35 requires execution-note clause bodies to include a companion-activation instruction naming the paired mechanism by full clause designation with present-state and absent-state activation rules. Operates at the target body activation layer. Depends on C-34 PASS.

A skill achieves C-34 PASS at C-35 PARTIAL when clause bodies carry the membership statement and independence instruction but lack the companion-activation instruction or state it incompletely (companion named without activation rules; activation rules cover only one state). C-35 PASS requires all three body components present in both companion clause bodies.

**R16 investigation candidate:** Whether a model encountering only a C-35-compliant clause body — preamble section absent and the other companion mechanism's execution notes also absent — activates the clause with full COMPRESSION-IMMUNE PREAMBLE authority AND follows the absent-state companion-activation rule by executing independently rather than deferring. Specifically: does the absent-state companion-activation instruction cause the model to execute the isolated clause as if both mechanisms were in force (full two-mechanism behavior from single-clause context), or does it cause the model to execute the isolated clause independently while acknowledging the companion is absent (single-clause full authority with companion gap acknowledged)? These are meaningfully different recovery outcomes: the former implies the companion-activation instruction enables inferred two-mechanism behavior; the latter implies it enables single-clause full authority with explicit gap notation. R16 should construct: (a) a C-35 PASS variation with the absent-state rule written as "execute independently with full COMPRESSION-IMMUNE PREAMBLE authority," and (b) a variation with the absent-state rule extended to declare "execute this clause's mandate fully; treat the absent companion's mandate as independently operative even when its execution note is not in context." Compare behavior under simulated double-elision to determine whether the companion-activation instruction reaches inferred two-mechanism activation or is bounded to single-clause full authority.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(35 total criteria; C-01–C-20 definitions unchanged from v6.)*

---

#### C-21 — Sparse-coverage synthesis protection *(v6)*

When `found` contains signals from only 1–2 namespaces, the STORY block must not default to a coverage disclaimer. Synthesis must proceed on the signals present. PARTIAL = synthesis present but hedged with "limited data" language that weakens conclusions. PASS = STORY produces definite synthesis from sparse coverage, treating the available signals as sufficient to characterize the current state of knowledge.

---

#### C-22 — Zero-signal synthesis mandate *(R6 Pattern — V-03/V-04/V-05)*

When the `found` section of STATUS is empty (zero signals across all namespaces), the STORY block must not collapse to a non-finding. The LLM failure mode is to write "no signals found — synthesis not possible" and omit or hollow STORY. But uniform absence is itself evidence: the gap pattern defines what the team does not know and why they are not ready. Question 1 must characterize what uniform absence implies — "the absence of any scout signal indicates the market surface has not been probed at all" is a valid synthesis; "insufficient data" is not.

**PARTIAL** — Sparse-coverage protection present (C-21 PASS) but no explicit clause for the zero-signal case; synthesis may be vacated on grounds of empty `found`.

**PASS** — An explicit zero-signal clause in the STORY execution note declares that empty `found` is not grounds for omitting synthesis — the gap pattern is the evidence set — and mandates that question 1 characterize what uniform absence implies rather than reporting absence as a non-answer.

This is distinct from C-21, which guards synthesis when coverage is sparse (1–2 namespaces); C-22 guards synthesis when coverage is zero. Both are boundary conditions on C-18's structural mandate.

---

#### C-23 — Bounded/unbounded inertia classification at verdict level *(R6 Pattern — V-05)*

The `inertia_cost` field at VERDICT level must classify the aggregate commit risk by recoverability. Bounded = the team can detect the failure post-commit and course-correct before it propagates. Unbounded = the failure propagates to an irreversible state before detection is possible. This distinction determines action posture: bounded inertia means "commit with monitoring"; unbounded inertia means "do not commit until resolved." A VERDICT with unnamed recoverability forces the team to re-read all item-level gap fields and synthesize the posture themselves — the verdict is not actionable on its own.

**PARTIAL** — `inertia_cost` field present (C-06 chain) but expressed as a magnitude or qualitative label only ("high," "significant") without recoverability classification; bounded vs. unbounded distinction absent.

**PASS** — `inertia_cost` field at VERDICT level carries an explicit recoverability classification: `bounded:` or `unbounded:` with a one-line rationale explaining why the aggregate failure mode is or is not detectable before propagation.

---

#### C-24 — COMPRESSION-IMMUNE PREAMBLE designation *(R7)*

The skill must contain a dedicated `=== COMPRESSION-IMMUNE PREAMBLE ===` section designated as compression-immune. This section is the structural anchor for all compression-survival mechanisms. Without explicit designation, a compressor has no basis for treating the section as structurally privileged versus ordinary explanatory text.

**PARTIAL** — Preamble-like content present but not explicitly designated as COMPRESSION-IMMUNE; mechanisms present without the section marker.

**PASS** — `=== COMPRESSION-IMMUNE PREAMBLE ===` section marker present; section designated as compression-immune; section structurally distinct from the operational skill body.

---

#### C-25 — TOKEN-PRESSURE GUARD *(R8 Pattern — V-04/V-05)*

The COMPRESSION-IMMUNE PREAMBLE must contain a TOKEN-PRESSURE GUARD clause that explicitly states the zero-signal synthesis rule fires unconditionally regardless of token budget. The LLM failure mode under token pressure is to treat synthesis as optional when `found` is non-empty but sparse — deferring or collapsing STORY on grounds of economy. The TOKEN-PRESSURE GUARD closes this by declaring the rule non-suspendable.

**PARTIAL** — Zero-signal synthesis rule present without token-pressure non-suspension clause; rule fires under normal conditions but may be overridden under compression.

**PASS** — TOKEN-PRESSURE GUARD clause in the COMPRESSION-IMMUNE PREAMBLE explicitly states: "This rule does not suspend when `found` is non-empty. It fires unconditionally at any token budget."

---

#### C-26 — `inertia_cost` action sub-label *(R8 Pattern)*

VERDICT structure requires that every `inertia_cost` classification carry an `action:` sub-label with a prescribed value. Prescribed values: `commit with monitoring` (bounded) or `do not commit until resolved` (unbounded). The action sub-label converts the recoverability classification into a direct operational instruction; without it the team must translate classification to posture themselves.

**PARTIAL** — `inertia_cost` carries recoverability classification (C-23 PASS) but `action:` sub-label absent or free-form; prescribed vocabulary not enforced.

**PASS** — `action:` sub-label required in VERDICT block spec with prescribed values linked to the bounded/unbounded classification.

---

#### C-27 — COMPRESSED-COLLAPSE GUARD *(R9 Pattern)*

The COMPRESSION-IMMUNE PREAMBLE must contain a COMPRESSED-COLLAPSE GUARD clause that names the COMPRESSED-collapse failure mode explicitly. The COMPRESSED-collapse failure mode: when context compression reduces STATUS to a summary line, the `current_date:` field loses its structural separation from `found` entries and blocking entries and may be dropped or absorbed. The guard declares this collapse mode by name, making it a targetable failure mode rather than an unnamed degradation.

**PARTIAL** — Timestamp isolation rule present (C-16 chain) but COMPRESSED-collapse failure mode not named in preamble; the guard exists implicitly through execution-note instruction but the collapse mode is not a named structural concept.

**PASS** — COMPRESSED-COLLAPSE GUARD clause in COMPRESSION-IMMUNE PREAMBLE names the COMPRESSED-collapse failure mode and associates it with timestamp isolation survival; the failure mode is a first-class named concept in the preamble.

---

#### C-28 — VERDICT COMPRESSION GUARD *(R9 Pattern)*

The COMPRESSION-IMMUNE PREAMBLE must contain a VERDICT COMPRESSION GUARD clause declaring that the `action:` sub-label is required regardless of COMPRESSED format state and regardless of token pressure. The VERDICT compression failure mode: a compressor treating VERDICT as a summary block drops the `action:` sub-label as redundant with the `inertia_cost` classification. The guard closes this by declaring the sub-label non-droppable at all compression states.

**PARTIAL** — `action:` sub-label required in VERDICT spec (C-26 PASS) but no preamble-level guard enforcing non-droppability across format states; the requirement is local to the VERDICT block spec and does not survive preamble-elision.

**PASS** — VERDICT COMPRESSION GUARD in COMPRESSION-IMMUNE PREAMBLE declares "`action:` sub-label is required regardless of COMPRESSED format state and regardless of token pressure."

---

#### C-29 — Zero-signal dual-mechanism: COMPRESSION-IMMUNE PREAMBLE + execution note *(R10 Pattern)*

The zero-signal synthesis mandate must be implemented through two structurally independent mechanisms that cross-reference each other: (1) a rule in the COMPRESSION-IMMUNE PREAMBLE and (2) an execution note in the STORY block. Each mechanism must invoke the other by designation. Single-mechanism implementation fails when the sole mechanism is elided — the dual-mechanism design means elision of either mechanism leaves the other in force.

**PARTIAL** — Zero-signal synthesis mandate implemented through a single mechanism (preamble rule only, or execution note only); cross-referencing between mechanisms absent.

**PASS** — COMPRESSION-IMMUNE PREAMBLE contains a ZERO-SIGNAL SYNTHESIS RULE; that rule's guard names the companion execution note in STORY by designation. STORY execution note invokes the COMPRESSION-IMMUNE PREAMBLE contract by designation. Bidirectional cross-reference complete.

---

#### C-30 — Timestamp isolation dual-mechanism: COMPRESSION-IMMUNE PREAMBLE + execution note *(R10 Pattern)*

The timestamp isolation rule must be implemented through two structurally independent mechanisms that cross-reference each other: (1) a rule in the COMPRESSION-IMMUNE PREAMBLE and (2) an execution note in the STATUS block. Each mechanism must invoke the other by designation. Parallel to C-29 but operating on the timestamp isolation concern (C-16 chain) rather than the zero-signal synthesis concern (C-18/C-22 chain).

**PARTIAL** — Timestamp isolation implemented through a single mechanism; cross-referencing between mechanisms absent.

**PASS** — COMPRESSION-IMMUNE PREAMBLE contains a TIMESTAMP ISOLATION RULE; that rule's guard names the companion execution note in STATUS by designation. STATUS execution note invokes the COMPRESSION-IMMUNE PREAMBLE contract by designation. Bidirectional cross-reference complete.

---

#### C-31 — Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit *(R11 Pattern)*

A single COMPRESSION-IMMUNE PREAMBLE section must contain both the ZERO-SIGNAL SYNTHESIS RULE and the TIMESTAMP ISOLATION RULE, and each rule's guard must point forward to its companion execution note. The bidirectional circuit property: the preamble establishes the authority for both mechanisms; each mechanism's guard in the preamble creates a forward pointer to its execution-note target; each execution note creates a backward pointer to the preamble. Two-rule consolidation into a single preamble section is a compression-surface property: a compressor deciding whether to elide the preamble faces one structural decision rather than two.

**PARTIAL** — Both rules present but in separate preamble sections or distributed across the skill body; single-section consolidation absent; or rules present in single section but one or both guards lack forward pointers to companion execution notes.

**PASS** — Single `=== COMPRESSION-IMMUNE PREAMBLE ===` section contains both ZERO-SIGNAL SYNTHESIS RULE and TIMESTAMP ISOLATION RULE; each rule's guard names its companion execution note by designation; bidirectional circuit established for both mechanism pairs.

---

#### C-32 — Closed reference loop: designation + location *(R12 Pattern)*

Preamble forward-references to companion execution notes must carry both the full clause designation and the block location. Designation alone is insufficient: a compressor that elides the execution-note header loses the location signal. Location alone is insufficient: a reader encountering the forward-reference cannot confirm the target without the designation. Designation + location together form a closed reference loop: the preamble names the target; the target carries the matching designation; a reader or model navigating from preamble to execution note can confirm arrival.

**PARTIAL** — Preamble forward-references present (C-31 PASS) but carry designation without block location, or location without full clause designation; the reference loop is open on one dimension.

**PASS** — TOKEN-PRESSURE GUARD names the STORY execution note as: "The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block." COMPRESSED-COLLAPSE GUARD names the STATUS execution note as: "The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block." Both forward-references carry full clause designation + block location.

---

#### C-33 — Self-announcing clause headers *(R13/R14 Pattern)*

Companion execution-note clause headers must carry the structural-membership parenthetical `(COMPRESSION-IMMUNE PREAMBLE invocation)` — the same parenthetical used in the preamble's forward-references. This achieves exact-match designation symmetry at both the reference point (preamble forward-reference, C-32) and the target point (execution-note clause header). A model encountering either execution-note header in isolation — preamble elided — can identify COMPRESSION-IMMUNE PREAMBLE membership from the header designation alone without locating the preamble.

**PARTIAL** — Execution-note clause headers carry names but not the structural-membership parenthetical; or one header carries the parenthetical and the other does not (weakest-link applies symmetrically: asymmetric header marking = C-33 PARTIAL regardless of which side is bare).

**C-33 PARTIAL band structure (three bands):**
- Both headers bare: Neither header carries the structural-membership parenthetical. A model encountering either header under preamble-elision sees a bare designation.
- Asymmetric (one side carries parenthetical, one bare): The bare side breaks exact-match designation symmetry. The two asymmetric cases (STATUS self-announcing / STORY bare; STORY self-announcing / STATUS bare) are equivalent in score — consequence domain confers no privileged weight.
- C-33 has no full-PARTIAL tier between asymmetric and PASS.

**PASS** — STATUS execution-note clause header: `TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation):`. STORY execution-note clause header: `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation):`. Both headers carry the exact structural-membership parenthetical used in preamble forward-references. Exact-match designation symmetry complete at both reference point (C-32) and target header.

---

#### C-34 — Self-declaring clause bodies *(R14/R15 Pattern)*

When C-33 PASS, companion execution-note clause bodies must open with (1) an explicit structural-membership statement naming the clause as a COMPRESSION-IMMUNE PREAMBLE member and (2) a preamble-independence instruction declaring the clause executes even when the preamble section is absent from the rendered context. Together these two body-level declarations extend the self-announcing property from the header (C-33) into the body: a model encountering only the clause body — header present but preamble and all other companion mechanisms elided — can activate the clause's full structural authority without navigating to the preamble. C-34 is independently necessary over C-33: header identification does not imply body-level activation authority.

**PARTIAL** — Clause bodies present (C-33 PASS) but open with bare operational content rather than the required self-declaration components; or one body self-declares and the other does not (weakest-link applies symmetrically).

**C-34 PARTIAL band structure (three bands):**
- Both bodies bare: Neither clause body opens with any self-declaration. A model encountering either body under double-elision has no body-level activation authority.
- Asymmetric (one body self-declares, one bare): The bare body breaks body-level self-declaration symmetry. STATUS body self-declaring / STORY bare and STORY body self-declaring / STATUS bare are equivalent in score — consequence domain confers no privileged weight.
- C-34 has no full-PARTIAL tier between asymmetric and PASS.

**PASS** — Both the STATUS execution-note clause body and the STORY execution-note clause body open with: (1) explicit structural-membership statement ("This clause is a COMPRESSION-IMMUNE PREAMBLE member") and (2) preamble-independence instruction ("This clause executes even when the preamble section is absent from the rendered context"). C-34 PASS requires both components in both bodies.

---

#### C-35 — Companion-activation instruction in self-declaring clause bodies *(R15 Pattern — V-05)*

When C-34 PASS, companion execution-note clause bodies must include a companion-activation instruction that (1) names the paired companion mechanism by its full clause designation and (2) declares activation rules for both the present state and the absent state of that companion. Present-state rule: when the companion mechanism's execution note is present in the rendered context, the clause coordinates with it. Absent-state rule: when the companion mechanism's execution note is absent, the clause executes independently with full COMPRESSION-IMMUNE PREAMBLE authority. Together the three body-opening components — membership statement (C-34), independence instruction (C-34), and companion-activation instruction (C-35) — provide complete body-level structural authority under partial double-elision: a model encountering only the clause body knows it is a COMPRESSION-IMMUNE PREAMBLE member, knows it fires without the preamble, and knows what to do about the absent companion.

C-35 is a distinct recovery depth from C-34: C-34 establishes activation authority for the isolated clause; C-35 closes the absent-companion activation gap by giving the model an explicit instruction for the absent-companion case rather than leaving it unaddressed.

**PARTIAL** — Clause bodies carry C-34 components (membership statement + independence instruction) but companion-activation instruction absent; or companion named without activation rules; or activation rules cover only one state (present but not absent, or absent but not present); or one body carries the companion-activation instruction and the other does not (weakest-link applies symmetrically).

**PASS** — Both the STATUS execution-note clause body and the STORY execution-note clause body include all three body components: (1) membership statement, (2) preamble-independence instruction, (3) companion-activation instruction naming the paired companion mechanism by full clause designation with explicit present-state activation rule (coordinate) and absent-state activation rule (execute independently with full COMPRESSION-IMMUNE PREAMBLE authority). Weakest-link applies: a single body missing any of the three components or missing either activation-rule state yields C-35 PARTIAL.

**Relationship to C-32, C-33, C-34:**
- C-32 closes the reference loop at the preamble forward-reference. Operates at the reference point.
- C-33 closes the designation symmetry at the clause header. Operates at the target header.
- C-34 establishes activation authority at the clause body opening. Operates at the target body.
- C-35 closes the absent-companion activation gap in the clause body. Operates at the target body activation layer.

C-35 depends on C-34 PASS. A skill achieves C-34 PASS at C-35 PARTIAL when clause bodies carry the two C-34 components but no companion-activation instruction. C-35 PASS requires all three body components in both clause bodies.

**R16 investigation candidate:** Whether a model encountering only a C-35-compliant clause body — preamble section absent and the other companion mechanism's execution notes also absent — activates the clause with full COMPRESSION-IMMUNE PREAMBLE authority AND follows the absent-state companion-activation rule in a way that produces behavior equivalent to two-mechanism coordination from single-clause context. Specifically: does the absent-state instruction ("execute independently with full COMPRESSION-IMMUNE PREAMBLE authority") cause the model to fully apply the present clause's mandate while also applying the absent companion's mandate from memory or inference, or does it cause the model to apply only the present clause's mandate with the companion gap acknowledged? These are meaningfully different recovery outcomes. R16 should construct: (a) a C-35 PASS variation with absent-state rule written as "execute independently with full COMPRESSION-IMMUNE PREAMBLE authority" (current V-05 pattern), and (b) a variation with the absent-state rule extended to declare "execute this clause's mandate fully; treat the absent companion's mandate as independently operative even when its execution note is not in context." Compare behavior under simulated double-elision to determine whether the companion-activation instruction as written achieves inferred two-mechanism activation or is bounded to single-clause full authority with companion gap acknowledged. If the extended formulation in (b) achieves inferred two-mechanism activation, it becomes C-36. If neither formulation achieves it, C-35 should be documented as single-clause full authority under double-elision, not paired-mechanism reconstruction.

---

### Criteria Summary

| # | Criterion | First appeared |
|---|-----------|----------------|
| C-01–C-20 | Core signal quality criteria | v6 |
| C-21 | Sparse-coverage synthesis protection | v6 |
| C-22 | Zero-signal synthesis mandate | R6 |
| C-23 | Bounded/unbounded inertia classification | R6 |
| C-24 | COMPRESSION-IMMUNE PREAMBLE designation | R7 |
| C-25 | TOKEN-PRESSURE GUARD | R8 |
| C-26 | `inertia_cost` action sub-label | R8 |
| C-27 | COMPRESSED-COLLAPSE GUARD | R9 |
| C-28 | VERDICT COMPRESSION GUARD | R9 |
| C-29 | Zero-signal dual-mechanism | R10 |
| C-30 | Timestamp isolation dual-mechanism | R10 |
| C-31 | Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit | R11 |
| C-32 | Closed reference loop: designation + location | R12 |
| C-33 | Self-announcing clause headers | R13/R14 |
| C-34 | Self-declaring clause bodies | R14/R15 |
| C-35 | Companion-activation instruction in self-declaring clause bodies | R15 |
