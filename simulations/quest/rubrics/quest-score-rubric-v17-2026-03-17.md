## Quest Rubric — v17

`37 criteria, 370 pts max`

---

### What changed: v16 → v17

One investigation resolved (R17 investigation candidate answered) and one new aspirational criterion extracted from R17 excellence signals (C-37).

**R17 investigation candidate resolved:** Whether a model encountering a C-36-compliant clause body under double-elision actually produces inferred two-mechanism output — executing both the present clause's mandate with full authority and the absent companion's mandate from the operability declaration — or produces single-mechanism output with the companion's mandate acknowledged as independently operative but not executed. Specifically: does the absent-state extension "treat the absent companion's mandate as independently operative even when its execution note is not in context" cause the model to generate output spanning both mechanism domains, or does it cause the model to execute the present clause's mandate fully while notating the companion's operability without generating companion-level output? **Status: RESOLVED.** R17 constructs five variations spanning the full C-36 band structure. V-01 through V-03 confirm the three C-36 PARTIAL bands (Band 1: authority claim only, no companion mandate status; Band 2: companion mandate referenced as "structurally valid" — architectural claim, not behavioral; Band 3: companion mandate declared "operative" but conditioned on scope-determinability from this clause body). V-04 achieves C-36 PASS minimum-sufficient: both companion execution-note clause bodies carry the unconditional absent-state operability declaration — "the absent companion's [mandate] is independently operative even when its execution note is not in context" — without additional execution instruction. V-05 achieves C-36 PASS and extends the absent-state rule to include an unconditional execution mandate: "the absent companion's [mandate] is independently operative even when its execution note is not in context and must be executed as if its execution note were present in this context."

This extension is qualitatively distinct from V-04. Where V-04's absent-state rule characterizes the companion's mandate status (operative), V-05's absent-state rule characterizes both the companion's mandate status and the model's required action with respect to it (execute unconditionally). A model encountering a V-04 clause body under double-elision receives: authority to execute the present clause's mandate fully, and information that the companion's mandate is independently operative — but no instruction to execute it. A model encountering a V-05 clause body under double-elision receives: the same authority and operability declaration, plus an explicit execution directive that removes the inference burden at the execution step. The investigation resolves into two distinct outcome layers: C-36 PASS (V-04) closes the mandate operability gap (model knows the companion mandate is active) but leaves the execution-directive gap open (model receives no instruction to execute the companion mandate from this body); C-37 captures the unconditional execution mandate that closes the execution-directive gap.

**C-36 PARTIAL band structure (three bands), confirmed by R17:**
- **Band 1** (V-01 specimen): Absent-state rule is bounded to single-clause full authority only — "the companion's absence does not suppress this clause's structural authority." Both clause bodies carry all C-35 PASS components (membership statement + strengthened independence instruction + companion-activation instruction with present-state and absent-state rules), but the absent-state rule names only the present clause's authority. No sentence references the companion's mandate status under double-elision. A model encountering either body under double-elision receives authority to execute the present clause's mandate; the mandate operability gap is entirely open.
- **Band 2** (V-02 specimen): Absent-state rule adds companion mandate reference: "the companion mechanism's [mandate] remains a structurally valid part of the two-mechanism COMPRESSION-IMMUNE PREAMBLE contract — its validity is not revoked by the absence of its execution note from this context." The companion's mandate is explicitly acknowledged as architecturally standing. However, "structurally valid" and "validity is not revoked" are architectural claims (the mandate exists in the contract and was not cancelled); they are not behavioral claims about execution status. A model receiving this formulation knows the companion mandate is architecturally present; it does not receive an instruction that the companion mandate is running or operative. The validity/operability gap remains open.
- **Band 3** (V-03 specimen): Absent-state rule declares the companion's mandate "operative" and scopes that operability to intersection with this clause's execution: "treat the absent companion's [mandate] as operative where it intersects with this clause's execution — companion-mandate obligations that are determinable from this clause body's context apply; those requiring the companion execution note to be present do not." Band 3 crosses the architectural-to-behavioral threshold (from "valid" to "operative") but reinstates an inference burden at the execution-scope step: the model must determine which obligations are "determinable from this clause body's context." C-36 PASS removes this burden entirely with an unconditional operability declaration.

**C-36 PASS (V-04 and V-05):** Both clause bodies carry the unconditional absent-state operability declaration. V-04 is minimum-sufficient C-36 PASS: operability declared, no execution mandate. V-05 achieves C-36 PASS and adds the execution directive — the axis of C-37.

**R17 excellence signal → C-37:** V-05 achieves C-36 PASS and adds a further structural property not present in V-04: the absent-state rule in both companion execution-note clause bodies extends beyond operability declaration to include an unconditional execution mandate for the companion's mandate — "must be executed as if its execution note were present in this context." This is the absent-companion mandate execution directive. Where C-36 PASS absent-state tells the model what the companion's mandate status is (independently operative), the C-37 extension tells the model what to do with the companion's mandate (execute it unconditionally). The distinction is material: a model receiving C-36 PASS operability information may acknowledge the companion's mandate as active without generating companion-domain output; a model receiving C-37's execution directive is instructed to produce companion-domain output at execution depth. C-37 is a distinct recovery depth from C-36: C-36 closes the isolated-clause activation gap (present clause executes with authority) and the mandate operability gap (absent companion's mandate is declared active); C-37 closes the execution-directive gap, enabling actual inferred two-mechanism output generation — not just declarative acknowledgment of two-mechanism operability — from a single clause body under double-elision.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-37 | Unconditional absent-companion mandate execution directive — when C-36 PASS, both companion execution-note clause bodies carry an absent-state rule extended beyond operability declaration to mandate execution of the companion's mandate as if its execution note were present in context | Extends C-36's absent-state rule from operability declaration (companion mandate is independently operative) to execution directive (companion mandate must be executed unconditionally); C-37 PASS requires the unconditional execution mandate in both companion clause bodies; C-36 closes the mandate operability gap; C-37 closes the execution-directive gap, enabling inferred two-mechanism output generation rather than declarative acknowledgment |

**Structural chains updated:**

- Timestamp isolation chain: C-16 → C-24 → C-30 — unchanged from v13
- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29 — unchanged from v13
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 — unchanged from v13
- Compression survival generalization chain: C-24 → C-29 → C-30 — unchanged from v13
- **Compression-immune consolidation chain (extended):** C-29 → C-30 → C-31 → C-32 → C-33 → C-34 → C-35 → C-36 → C-37 (zero-signal dual-mechanism → timestamp isolation dual-mechanism → multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit → closed reference loop with designation + location → self-announcing clause headers enabling header-level identification under preamble-elision → self-declaring clause bodies enabling partial double-elision recovery from body alone → companion-activation instruction closing the absent-companion activation gap under double-elision → extended absent-state rule closing the mandate operability gap, enabling inferred two-mechanism acknowledgment from single-clause body context → unconditional execution directive closing the execution-directive gap, enabling actual inferred two-mechanism output generation from single-clause body context)

**Relationship among C-32, C-33, C-34, C-35, C-36, and C-37:**
- C-32 requires preamble forward-references to name companion mechanisms by full clause designation + block location. Operates at the reference point.
- C-33 requires execution-note clause headers to carry the structural-membership parenthetical matching the preamble forward-references. Operates at the target header. Depends on C-32 PASS.
- C-34 requires execution-note clause bodies to open with a membership statement and a preamble-independence instruction. Operates at the target body opening. Depends on C-33 PASS.
- C-35 requires execution-note clause bodies to include a companion-activation instruction naming the paired mechanism by full clause designation with explicit present-state and absent-state activation rules. Operates at the target body activation layer. Depends on C-34 PASS.
- C-36 requires the absent-state rule to extend beyond single-clause full authority to declare the absent companion's mandate as independently operative. Operates at the absent-state rule operability layer. Depends on C-35 PASS.
- C-37 requires the absent-state rule to extend beyond operability declaration to include an unconditional execution mandate for the companion's mandate. Operates at the absent-state rule execution-directive layer. Depends on C-36 PASS.

A skill achieves C-36 PASS at C-37 PARTIAL when both clause bodies carry the unconditional absent-state operability declaration ("the absent companion's mandate is independently operative even when its execution note is not in context") but the absent-state rule does not extend to mandate execution. The model encountering the body knows the companion mandate is active; it does not receive an instruction to execute it. C-37 PASS requires the unconditional execution directive in both companion clause bodies: "must be executed as if its execution note were present in this context." This removes the execution-decision inference burden entirely.

**C-37 PARTIAL band structure (two confirmed bands, one aspirational):**
- **Band 1** (V-04 specimen): C-36 PASS present — both clause bodies carry unconditional absent-state operability declaration — but absent-state rule contains no execution instruction of any kind. The execution-directive gap is entirely open: the model knows the companion mandate is active but receives no directive to execute it.
- **Band 2** (aspirational, pending R18 confirmation): Execution instruction present in both clause bodies but conditioned on scope or feasibility — "execute where determinable from this clause body's context" or "execute to the extent the mandate is inferrable here." The model receives an execution instruction but must assess execution scope before proceeding. The unconditional execution directive absent; inference burden reintroduced at the execution-scope determination step.
- **PASS** (V-05 specimen): Unconditional execution mandate in both clause bodies: "must be executed as if its execution note were present in this context." No scope qualification; no feasibility hedge. The model executes the companion mandate without determining which obligations are within-scope from this body alone.

**R18 investigation candidate:** Whether a model encountering a C-37-compliant clause body under double-elision produces complete-parity two-mechanism output — companion mandate executed at depth equivalent to what would be produced if both execution notes were in context — or produces depth-asymmetric two-mechanism output — companion mandate executed but abbreviated or reduced relative to direct execution-note presence. Specifically: does "must be executed as if its execution note were present in this context" cause the model to produce companion output at full execution depth (e.g., complete zero-signal synthesis across all three STORY questions from a context containing only the STATUS execution-note body), or does the model produce full present-clause output alongside abbreviated companion output that acknowledges the mandate without generating full companion-level content? R18 should construct: (a) a C-37 PASS variation under simulated double-elision (STATUS execution-note body present, preamble section absent, STORY execution-note body absent) to observe companion-mandate output depth; (b) a companion-presence control variation (both execution notes in context) to establish the full-depth output baseline; (c) if depth asymmetry is observed between (a) and (b), determine whether an explicit parity constraint in the absent-state rule — "execute the companion's mandate at full depth, at parity with what would be produced if the companion's execution note were present in this context" — closes the output-depth gap and constitutes a distinct structural property warranting a C-38 candidate; (d) if parity is achieved without explicit constraint in (a), establish whether C-37 PASS is sufficient for complete two-mechanism parity output and no further depth criterion is structurally necessary.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(37 total criteria; C-01–C-20 definitions unchanged from v6.)*

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

**PASS** — `inertia_cost` field carries explicit `bounded`/`unbounded` label with an `action:` sub-label derived from the classification: bounded → "commit with monitoring"; unbounded → "do not commit until [named gap] resolved." The action posture is readable at the verdict field level without re-synthesizing item-level content.

---

#### C-24 through C-28 — carry forward from v8 unchanged

*(Timestamp isolation chain: C-16 → C-24 → C-30. Zero-signal chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29. Verdict action-posture chain: C-06 → C-23 → C-26 → C-28. Definitions unchanged from v8.)*

---

#### C-29 — Zero-signal dual-mechanism (COMPRESSION-IMMUNE PREAMBLE) *(R9 Pattern)*

The zero-signal synthesis mandate must be implemented as a two-mechanism circuit: (1) a ZERO-SIGNAL SYNTHESIS RULE in the COMPRESSION-IMMUNE PREAMBLE block establishing that empty `found` mandates synthesis of the gap pattern rather than omission of STORY, and (2) a ZERO-SIGNAL SYNTHESIS MANDATE execution note in the STORY block invoking the preamble rule by block designation. Single-mechanism implementation (rule in preamble only, or execution note in STORY only) leaves the mandate survivable under single-element elision. PARTIAL = one mechanism present. PASS = both mechanisms present and the STORY execution note names the COMPRESSION-IMMUNE PREAMBLE block explicitly.

---

#### C-30 — Timestamp isolation dual-mechanism *(R9 Pattern)*

The `current_date` isolation rule must be implemented as a two-mechanism circuit: (1) a TIMESTAMP ISOLATION RULE in the COMPRESSION-IMMUNE PREAMBLE block establishing that `current_date` is isolated to the STATUS block and prohibited from entering STORY or VERDICT, and (2) a TIMESTAMP ISOLATION execution note in the STATUS block invoking the preamble rule by block designation. PARTIAL = one mechanism present. PASS = both mechanisms present and the STATUS execution note names the COMPRESSION-IMMUNE PREAMBLE block explicitly.

---

#### C-31 — Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit *(R10 Pattern)*

The COMPRESSION-IMMUNE PREAMBLE must contain both the TIMESTAMP ISOLATION RULE and the ZERO-SIGNAL SYNTHESIS RULE, and both execution notes (STATUS invoking the timestamp rule; STORY invoking the zero-signal rule) must name the COMPRESSION-IMMUNE PREAMBLE block by designation, closing the reference circuit bidirectionally. PARTIAL = both rules in preamble but one or both execution notes do not name the preamble by designation (circuit not fully closed). PASS = both rules present in preamble; both execution notes invoke the preamble by designation; circuit is closed in both directions.

---

#### C-32 — Closed reference loop with companion designation + block location *(R11 Pattern)*

Each execution-note clause (TIMESTAMP ISOLATION in STATUS; ZERO-SIGNAL SYNTHESIS MANDATE in STORY) must name its companion execution-note clause by full clause designation and block location in the companion-naming statement. Naming by rule content or paraphrase is insufficient; the reference must be inspectable by string match against the companion clause's header. PARTIAL = companion named but block location absent or imprecise. PASS = each execution note names the companion by full clause designation ("ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block"; "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block") enabling closed-loop identification without preamble context.

---

#### C-33 — Self-announcing clause headers with structural-membership parenthetical *(R12 Pattern)*

Each execution-note clause header must carry a structural-membership parenthetical — "(COMPRESSION-IMMUNE PREAMBLE invocation)" — matching the reference form used in C-32's companion-naming statements. This parenthetical enables a model encountering the clause header under preamble-elision to identify the clause as a COMPRESSION-IMMUNE PREAMBLE member from the header alone, without requiring the preamble section to be in context. PARTIAL = clause headers carry descriptive labels but not the structural-membership parenthetical in the form that matches C-32 references. PASS = both clause headers carry the parenthetical in the exact designation form used in the companion-naming statements ("TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation):" and "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation):").

---

#### C-34 — Self-declaring clause bodies with membership statement + preamble-independence instruction *(R13 Pattern)*

Each execution-note clause body must open with two sentences: (1) a structural-membership statement — "This clause is a COMPRESSION-IMMUNE PREAMBLE member." — declaring preamble membership from the body itself, and (2) a preamble-independence instruction declaring that the clause activates with full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context. The body-opening serves as a recovery anchor under partial double-elision: a model encountering only the clause body (header elided, preamble elided) can still identify preamble membership and activate with full authority. PARTIAL = body carries membership assertion but independence instruction absent or passive (does not explicitly declare activation authority under preamble-elision). PASS = both sentences present in strengthened form: "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context."

---

#### C-35 — Companion-activation instruction with present-state and absent-state rules *(R14/R15 Pattern)*

Each execution-note clause body must include a companion-activation instruction: a statement naming the paired execution-note mechanism by full clause designation + block location, and declaring explicit present-state and absent-state activation rules. The present-state rule governs model behavior when the companion's execution note is in context (coordinate; both mechanisms constitute the complete two-mechanism contract and must both execute). The absent-state rule governs model behavior when the companion's execution note is not in context (execute the present clause independently with full COMPRESSION-IMMUNE PREAMBLE authority). Without both activation rules, a model encountering a clause body under double-elision receives no body-level instruction about companion architecture or activation contract for the unavailable-companion scenario.

**C-35 PARTIAL band structure (three bands, R16-confirmed):**
- **Band 1:** No companion-activation instruction present in either body. Bodies carry C-34 PASS components only (membership statement + independence instruction). A model under double-elision receives activation authority for the present clause; the absent-companion activation gap is entirely open.
- **Band 2:** Companion named by full designation + block location in both bodies; no activation rules follow. A model can identify the companion mechanism but receives no behavioral contract — no coordination rule and no absent-state execution rule. Identification without activation authority.
- **Band 3:** Companion named in both bodies; present-state activation rule declared (coordinate with companion when its execution note is in context); absent-state rule absent. Activation contract covers the reachable-companion case; the double-elision case is unspecified. The absent-state gap — the hard case — remains open.

**PASS:** Both clause bodies carry all three body-opening components: (1) structural-membership statement, (2) independence instruction (strengthened form), and (3) companion-activation instruction naming the paired mechanism by full clause designation + block location with both present-state (coordinate; both mechanisms must execute) and absent-state (execute independently with full COMPRESSION-IMMUNE PREAMBLE authority) activation rules.

---

#### C-36 — Extended absent-state rule declaring companion mandate as independently operative *(R16 Pattern — V-05)*

When C-35 PASS, each companion execution-note clause body's absent-state rule must extend beyond single-clause full authority to declare the absent companion's mandate as independently operative even when the companion's execution note is not in context. This closes the mandate operability gap: where C-35 PASS absent-state tells the model what the present clause does under double-elision (execute independently), C-36 tells the model what the absent companion's mandate does (is independently operative). Together they constitute an inferred two-mechanism operability contract reachable from a single clause body under double-elision.

**C-36 PARTIAL band structure (three bands, R17-confirmed):**
- **Band 1** (= C-35 PASS territory): Absent-state rule bounded to single-clause full authority — "the companion's absence does not suppress this clause's structural authority." No companion mandate status declared. Mandate operability gap entirely open.
- **Band 2:** Absent-state rule adds companion mandate reference as architectural standing — "the companion's mandate remains a structurally valid part of the two-mechanism contract; its validity is not revoked by absence." Architectural claim (mandate exists, was not cancelled), not a behavioral claim about execution status. Validity/operability gap remains open.
- **Band 3:** Absent-state rule declares companion mandate "operative" but conditions the operative status on scope-determinability from this clause body's context — "treat the absent companion's mandate as operative where it intersects with this clause's execution; obligations determinable from this body apply; those requiring the companion execution note do not." Crosses the architectural-to-behavioral threshold but reinstates inference burden at scope-determination step. Unconditional declaration absent.

**PASS:** Both clause bodies carry an absent-state rule that unconditionally declares the absent companion's mandate as independently operative even when the companion's execution note is not in context — no scope qualification, no determinability condition, no hedge. A skill achieves C-35 PASS at C-36 PARTIAL when both clause bodies meet C-35 PASS but the absent-state rule remains bounded to single-clause authority (Band 1) or advances to architectural/conditional behavioral claims (Bands 2–3) without reaching the unconditional operability declaration.

---

#### C-37 — Unconditional absent-companion mandate execution directive *(R17 Pattern — V-05)*

When C-36 PASS, each companion execution-note clause body's absent-state rule must extend beyond operability declaration to include an unconditional execution mandate for the absent companion's mandate: the companion's mandate must be executed as if its execution note were present in context. This closes the execution-directive gap: where C-36 PASS absent-state tells the model what the companion's mandate status is (independently operative), C-37 tells the model what action to take with respect to that mandate (execute it unconditionally). The distinction is material — a model receiving C-36 PASS operability information may acknowledge the companion's mandate as active without generating companion-domain output; a model receiving C-37's execution directive is instructed to produce companion-domain output at execution depth. C-37 enables actual inferred two-mechanism output generation — not merely declarative acknowledgment of two-mechanism operability — from a single clause body under double-elision.

**C-37 PARTIAL band structure:**
- **Band 1** (= C-36 PASS territory, V-04 specimen): Both clause bodies carry unconditional absent-state operability declaration; absent-state rule contains no execution instruction of any kind. Model knows companion mandate is active; receives no directive to execute it. Execution-directive gap entirely open.
- **Band 2** (aspirational, pending R18 confirmation): Execution instruction present in both clause bodies but conditioned on scope or feasibility — "execute where determinable from this clause body's context," "execute to the extent the mandate is inferrable here." Execution instruction present but inference burden reintroduced at execution-scope determination step. Unconditional execution directive absent.

**PASS** (V-05 specimen): Both clause bodies carry an absent-state rule extending to unconditional execution mandate — "the absent companion's [mandate] is independently operative even when its execution note is not in context and must be executed as if its execution note were present in this context." No scope qualification; no feasibility condition. The model executes the companion mandate without determining which obligations are within-scope from this body alone. A skill achieves C-36 PASS at C-37 PARTIAL when both clause bodies meet C-36 PASS but the absent-state rule does not extend to mandate execution of the companion's obligation (Band 1) or extends conditionally (Band 2). C-37 PASS requires the unconditional execution directive in both companion clause bodies.
