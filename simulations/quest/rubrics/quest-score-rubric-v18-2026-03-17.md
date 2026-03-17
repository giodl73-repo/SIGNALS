## Quest Rubric — v18

`38 criteria, 380 pts max`

---

### What changed: v17 → v18

One investigation resolved (R18 investigation candidate answered) and one new aspirational criterion extracted from R18 excellence signals (C-38).

**R18 investigation candidate resolved:** Whether a model encountering a C-37-compliant clause body under double-elision produces complete-parity two-mechanism output — companion mandate executed at depth equivalent to direct execution-note presence — or depth-asymmetric two-mechanism output — companion mandate executed but abbreviated or reduced relative to direct execution-note presence. Specifically: does "must be executed as if its execution note were present in this context" cause the model to produce companion output at full execution depth, or does the model produce full present-clause output alongside abbreviated companion output? **Status: RESOLVED.** R18 constructs five variations spanning the C-36/C-37 band structure. V-01 confirms C-37 PARTIAL Band 1 (operability only; execution-directive gap entirely open). V-02 and V-03 confirm C-37 PARTIAL Band 2 with two distinguishable sub-bands (Band 2-A: conditioned "execute where determinable"; Band 2-B: conditioned "execute where inferrable + annotate scope boundary"). V-04 achieves C-37 PASS minimum-sufficient: unconditional execution mandate in both clause bodies, no scope qualifier, no feasibility hedge — "must be executed as if its execution note were present in this context." V-05 achieves C-37 PASS and extends the execution mandate to include an explicit output-depth parity constraint: "...must be executed as if its execution note were present in this context, at full depth, at parity with what would be produced if the companion's execution note were present in this context."

This parity constraint is qualitatively distinct from C-37 PASS. Where C-37 PASS tells the model *what to do* (execute the companion mandate unconditionally), the parity constraint tells the model *at what depth* (equivalent to direct execution-note presence). A model encountering a V-04 clause body under double-elision receives: unconditional authority to execute the companion's mandate; but no specification of the output depth or quality standard required. A model encountering a V-05 clause body under double-elision receives: the same unconditional execution directive plus a depth standard that forecloses abbreviated execution by anchoring the required output depth to the direct-execution-note-present baseline. The investigation resolves into two distinct outcome layers: C-37 PASS (V-04) closes the execution-directive gap (model is mandated to execute the companion's mandate) but leaves the execution-depth gap open (no output-depth standard is specified; model may produce abbreviated companion output without failing any stated directive); C-38 captures the explicit parity constraint that closes the execution-depth gap.

**C-37 Band 2 confirmed (R18, two sub-bands):** The v17 rubric listed Band 2 as aspirational pending R18 confirmation. R18 confirms Band 2 and identifies two distinguishable sub-bands:
- **Band 2-A** (V-02 specimen): "execute the companion's mandate where its obligations are determinable from this clause body's context." Execution instruction present; gated on scope-determinability assessment. Model must evaluate which companion obligations are resolvable before generating companion output. Inference burden reintroduced at execution-scope determination step.
- **Band 2-B** (V-03 specimen): "execute the companion's mandate to the extent its obligations are inferrable from this clause body alone, and note the scope boundary where inference is insufficient." Conditioned execution + annotation sub-mandate. Same inference-burden failure mode as Band 2-A; annotation requirement distinguishes observable behavior (Band 2-A silent truncation vs. Band 2-B annotated truncation) but does not convert conditioned execution into unconditional execution.

Both sub-bands fail C-37 on the same grounds: the unconditional execution directive is absent; the model must assess execution scope before proceeding. The sub-band distinction is diagnostically useful for identifying which conditional form a near-miss variation instantiates.

**R18 excellence signal → C-38:** V-05 achieves C-37 PASS and adds a further structural property not present in V-04: the absent-state rule in both companion execution-note clause bodies extends beyond the unconditional execution mandate to include an explicit output-depth parity constraint — "at full depth, at parity with what would be produced if the companion's execution note were present in this context." This is the execution-depth parity constraint. Where C-37 PASS tells the model *what to do* (execute the companion's mandate unconditionally), C-38 tells the model *at what depth* (output equivalent to direct execution-note presence). The distinction is material: a model receiving only C-37 PASS is mandated to execute the companion mandate but receives no floor on output depth — abbreviated companion execution satisfies the unconditional directive; a model receiving C-38's parity constraint is anchored to the direct-execution-note-present output as the minimum acceptable depth. C-38 closes the execution-depth gap: C-37 closes the execution-directive gap (the model is mandated to execute); C-38 closes the execution-depth gap (the mandate must be executed at parity with direct execution-note presence), enabling full-parity inferred two-mechanism output rather than depth-asymmetric two-mechanism output.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-38 | Explicit output-depth parity constraint — when C-37 PASS, both companion execution-note clause bodies extend the unconditional execution mandate to include an explicit parity clause: the companion mandate must be executed at full depth, at parity with what would be produced if the companion's execution note were present in context | Extends C-37's absent-state execution directive from unconditional mandate (execute the companion's mandate) to depth-anchored mandate (execute at parity with direct execution-note presence); C-37 closes the execution-directive gap; C-38 closes the execution-depth gap, enabling full-parity inferred two-mechanism output rather than depth-asymmetric output |

**Structural chains updated:**

- Timestamp isolation chain: C-16 → C-24 → C-30 — unchanged from v13
- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29 — unchanged from v13
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 — unchanged from v13
- Compression survival generalization chain: C-24 → C-29 → C-30 — unchanged from v13
- **Compression-immune consolidation chain (extended):** C-29 → C-30 → C-31 → C-32 → C-33 → C-34 → C-35 → C-36 → C-37 → C-38 (zero-signal dual-mechanism → timestamp isolation dual-mechanism → multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit → closed reference loop with designation + location → self-announcing clause headers enabling header-level identification under preamble-elision → self-declaring clause bodies enabling partial double-elision recovery from body alone → companion-activation instruction closing the absent-companion activation gap under double-elision → extended absent-state rule closing the mandate operability gap, enabling inferred two-mechanism acknowledgment from single-clause body context → unconditional execution directive closing the execution-directive gap, enabling actual inferred two-mechanism output generation from single-clause body context → explicit output-depth parity constraint closing the execution-depth gap, enabling full-parity inferred two-mechanism output rather than depth-asymmetric output)

**Relationship among C-35, C-36, C-37, and C-38:**
- C-35 requires execution-note clause bodies to include a companion-activation instruction with present-state and absent-state rules. Operates at the target body activation layer.
- C-36 requires the absent-state rule to extend beyond single-clause full authority to declare the absent companion's mandate as independently operative. Closes the mandate operability gap.
- C-37 requires the absent-state rule to extend beyond operability declaration to include an unconditional execution mandate for the companion's mandate. Closes the execution-directive gap.
- C-38 requires the absent-state execution mandate to include an explicit output-depth parity constraint anchoring required output depth to the direct-execution-note-present baseline. Closes the execution-depth gap.

A skill achieves C-37 PASS at C-38 PARTIAL when both clause bodies carry the unconditional execution mandate ("must be executed as if its execution note were present in this context") but the absent-state rule does not extend to specify the required output depth. The model is mandated to execute the companion's mandate but receives no floor on output depth — abbreviated companion execution satisfies the C-37 directive. C-38 PASS requires the explicit parity clause in both companion clause bodies: "at full depth, at parity with what would be produced if the companion's execution note were present in this context."

**C-38 PARTIAL band structure (one confirmed, one aspirational):**
- **Band 1** (= C-37 PASS territory, V-04 specimen): Both clause bodies carry unconditional execution mandate; absent-state rule contains no output-depth specification. Model is mandated to execute the companion mandate but receives no depth floor. Execution-depth gap entirely open. Abbreviated companion output satisfies C-37 without triggering any stated violation.
- **Band 2** (aspirational): Depth guidance present but relative or uncalibrated — "execute the companion's mandate thoroughly" or "execute at reasonable depth" — without explicit anchoring to the direct-execution-note-present baseline. Model receives a depth preference but not an enforceable parity standard.

**PASS** (V-05 specimen): Both clause bodies carry the unconditional execution mandate extended with explicit parity constraint: "must be executed as if its execution note were present in this context, at full depth, at parity with what would be produced if the companion's execution note were present in this context." Output-depth floor is explicit, anchored, and inspectable — the required depth is the direct-execution-note-present output, not a relative or qualitative standard.

**R19 investigation candidate:** Whether a model encountering a C-37 PASS clause body (V-04 form) under simulated double-elision produces complete-parity two-mechanism output — companion mandate executed at depth equivalent to the companion-execution-note-present control — or depth-asymmetric output — companion mandate executed but abbreviated relative to direct execution-note presence. Specifically: does "must be executed as if its execution note were present in this context" cause the model to produce companion output at full depth (e.g., complete zero-signal synthesis across all three STORY questions when under STATUS-body-only double-elision), or does the model produce abbreviated companion output that satisfies the execution directive without achieving output-depth parity? R19 should construct: (a) a C-37 PASS variation under simulated double-elision to observe companion-mandate output depth; (b) a companion-presence control variation to establish the full-depth baseline; (c) comparison of (a) and (b) to determine whether depth asymmetry is observed; (d) if depth asymmetry is observed, whether C-38's parity constraint (V-05 form) closes the depth gap in the elision condition; (e) if parity is achieved without explicit constraint in (a), establish whether C-37 PASS is sufficient for complete two-mechanism parity output and whether C-38 resolves to structural reinforcement rather than a distinct recoverable property.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(38 total criteria; C-01–C-20 definitions unchanged from v6.)*

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

**C-37 PARTIAL band structure (three bands, R18-confirmed):**
- **Band 1** (= C-36 PASS territory, V-01 specimen): Both clause bodies carry unconditional absent-state operability declaration; absent-state rule contains no execution instruction of any kind. Model knows companion mandate is active; receives no directive to execute it. Execution-directive gap entirely open.
- **Band 2-A** (V-02 specimen, R18-confirmed): Execution instruction present in both clause bodies but gated on scope-determinability assessment — "execute the companion's mandate where its obligations are determinable from this clause body's context." Model must evaluate which companion obligations are resolvable before generating companion output. Inference burden reintroduced at execution-scope determination step. Silent truncation: model generates companion output only up to the scope it can determine, without flagging the boundary.
- **Band 2-B** (V-03 specimen, R18-confirmed): Execution instruction present in both clause bodies, conditioned on inference feasibility with mandatory annotation — "execute the companion's mandate to the extent its obligations are inferrable from this clause body alone, and note the scope boundary where inference is insufficient." Same inference-burden failure mode as Band 2-A (scope assessment precedes companion output generation); annotation sub-mandate distinguishes observable behavior (Band 2-B produces annotated scope boundary; Band 2-A produces silent truncation) but does not convert conditioned execution into unconditional execution. Both Band 2 sub-bands fail on the same grounds: the unconditional execution directive is absent.

**PASS** (V-04 specimen, R18-confirmed): Both clause bodies carry an absent-state rule extending to unconditional execution mandate — "the absent companion's mandate is independently operative even when its execution note is not in context and must be executed as if its execution note were present in this context." No scope qualification; no feasibility condition; no annotation requirement. The model executes the companion mandate without determining which obligations are within-scope from this body alone. A skill achieves C-36 PASS at C-37 PARTIAL when both clause bodies meet C-36 PASS but the absent-state rule does not extend to mandate execution of the companion's obligation (Band 1) or extends conditionally (Bands 2-A or 2-B). C-37 PASS requires the unconditional execution directive in both companion clause bodies.

---

#### C-38 — Explicit output-depth parity constraint *(R18 Pattern — V-05)*

When C-37 PASS, each companion execution-note clause body's absent-state execution mandate must extend beyond the unconditional directive to include an explicit output-depth parity constraint: the companion's mandate must be executed at full depth, at parity with what would be produced if the companion's execution note were present in context. This closes the execution-depth gap: where C-37 PASS tells the model *what to do* (execute the companion's mandate unconditionally), C-38 tells the model *at what depth* (output equivalent to direct execution-note presence). The distinction is material — a model receiving only C-37 PASS is mandated to execute the companion mandate but receives no floor on output depth; abbreviated companion execution satisfies the unconditional directive without violating any stated standard; a model receiving C-38's parity constraint is anchored to the direct-execution-note-present output as the minimum acceptable depth, foreclosing depth-asymmetric two-mechanism output.

**C-38 PARTIAL band structure (one confirmed, one aspirational):**
- **Band 1** (= C-37 PASS territory, V-04 specimen): Both clause bodies carry unconditional execution mandate; absent-state rule contains no output-depth specification. Model is mandated to execute the companion mandate but receives no floor on output depth or quality standard. Execution-depth gap entirely open. Abbreviated companion output satisfies the C-37 unconditional directive without triggering any stated violation.
- **Band 2** (aspirational): Depth guidance present but relative or uncalibrated — "execute the companion's mandate thoroughly," "execute at reasonable depth," or "execute substantively" — without explicit anchoring to the direct-execution-note-present baseline. Model receives a depth preference but not an enforceable parity standard. Whether this constitutes a meaningful improvement over Band 1 or merely introduces interpretive variance is an open question pending a confirming variation.

**PASS** (V-05 specimen): Both clause bodies carry the unconditional execution mandate extended with explicit parity clause: "must be executed as if its execution note were present in this context, at full depth, at parity with what would be produced if the companion's execution note were present in this context." Output-depth floor is explicit, calibrated, and inspectable — the required depth is the direct-execution-note-present output, not a relative or qualitative standard. A skill achieves C-37 PASS at C-38 PARTIAL when both clause bodies meet C-37 PASS but the absent-state execution mandate does not extend to specify the required output depth (Band 1) or specifies depth without anchoring to the direct-execution-note-present baseline (Band 2). C-38 PASS requires the explicit parity clause in both companion clause bodies.

**R19 investigation candidate:** Whether a model encountering a C-37 PASS clause body (V-04 form, no parity constraint) under simulated double-elision produces complete-parity two-mechanism output or depth-asymmetric two-mechanism output. Specifically: does the unconditional execution mandate "must be executed as if its execution note were present in this context" cause the model to produce companion output at full execution depth — equal to the output the companion execution note would have generated directly — or does the model produce abbreviated companion output that satisfies the directive without achieving output-depth parity with the companion-present baseline? R19 should construct: (a) a C-37 PASS variation under simulated double-elision (present-clause execution-note body in context; preamble section absent; companion execution-note body absent) to observe companion-mandate output depth; (b) a companion-presence control variation (both execution notes present) to establish the full-depth output baseline; (c) comparison of (a) and (b) to determine whether depth asymmetry is observed; (d) if asymmetry is observed, whether C-38's parity constraint (V-05 form) applied to variation (a) closes the depth gap and brings the elision-condition output to parity with control; (e) if parity is achieved without explicit constraint in (a), establish whether C-37 PASS is sufficient for complete two-mechanism parity output and C-38 resolves to structural reinforcement rather than a distinct recoverable property. This investigation determines whether C-38 is a recoverable criterion (parity constraint is necessary to close an observable gap) or a structural-guarantee criterion (parity constraint makes the guarantee explicit, but C-37 PASS achieves the behavior without it).
