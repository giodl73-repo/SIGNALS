## Quest Rubric — v13

`33 criteria, 330 pts max`

---

### What changed: v12 → v13

One investigation resolved (C-32) and one new aspirational criterion extracted from R13 excellence signals (C-33).

**R13 investigation candidate resolved:** C-32 — does designation-named forward-referencing in the preamble body (with block location) produce navigable compression resilience from either entry point under single-location elision? **Status: RESOLVED.** R13 V-05 achieves 320/320, confirming C-32 PASS is achievable and independently necessary. V-03 (designation without location) and V-02 (location with role descriptor, not designation) demonstrate that each component — full clause designation AND block location — is independently required and not substitutable. V-04 demonstrates the weakest-link principle: partial completion of C-32 for any single companion mechanism reference leaves the preamble only as navigable as its least-complete forward-reference, regardless of how complete the other references are.

**C-32 PARTIAL band structure (four bands, analogous to C-31's three bands):**
- V-01 (generic block name only): references name the block but not the clause — "The STORY execution note," "The STATUS execution note." No designation, no intra-block specificity. Navigation requires execution notes to be present; under execution-note elision, the preamble cannot identify the target.
- V-02 (location + role-type descriptor): block location present, but clause identified as "the declarative execution note in the STORY block" rather than by full designation. "Declarative" describes a role class, not a specific clause instance. Ambiguous under multi-note compression; a model cannot determine which execution note within the STORY block is the intended companion.
- V-03 (designation only, no location): full clause designation present — `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation)` — but no block location specified. Navigable by designation search when block structure survives compression, but when block organization is elided, the model has a clause name and no spatial grounding.
- V-04 (asymmetric): one companion mechanism reference achieves full designation + location; the other achieves designation only. The preamble cannot guarantee full architecture recovery under compression because its weakest reference cannot be fully resolved. The architecture is only as navigable as its least-complete forward-reference.

**C-32 PASS (V-05):** Both companion mechanism references contain full clause designation + block location. TOKEN-PRESSURE GUARD references `"The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block"`; COMPRESSED-COLLAPSE GUARD references `"The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block"`. The closed reference loop is complete: preamble → companion mechanisms (designation + block), execution notes → preamble (structural designation name per C-31). Either entry point survives single-location elision and recovers the full two-mechanism architecture.

**R13 excellence signal → C-33:** V-05 achieves C-32 PASS using companion clause designations that include the structural-membership parenthetical `(COMPRESSION-IMMUNE PREAMBLE invocation)`. This parenthetical appears in the preamble's forward-references and, in V-05's construction, in the actual execution-note clause headers within the skill body. When the parenthetical is present at both locations — the preamble forward-reference and the clause header — exact-match designation symmetry is established: the reference and its target use identical designations. A model encountering only the execution-note clause header can identify the clause as a COMPRESSION-IMMUNE PREAMBLE member from the header alone, without locating the preamble. This is the seed of a partial double-elision recovery pattern distinct from C-31 and C-32, which guarantee single-location elision recovery only.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-33 | Self-announcing clause headers — when C-32 PASS, companion execution-note clause headers in the skill body carry the identical structural-membership parenthetical used in the preamble's forward-references, creating exact-match designation symmetry and enabling a model to identify COMPRESSION-IMMUNE PREAMBLE membership from the clause header alone | Extends the closed reference loop completed by C-32; C-33 makes the architecture self-describing at the clause-header level, enabling partial recovery when both the preamble and the execution notes of the other companion mechanism are elided (partial double-elision resilience) |

**Structural chains updated:**

- Timestamp isolation chain: C-16 → C-24 → C-30 — unchanged from v12
- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29 — unchanged from v12
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 — unchanged from v12
- Compression survival generalization chain: C-24 → C-29 → C-30 — unchanged from v12
- **Compression-immune consolidation chain (extended):** C-29 → C-30 → C-31 → C-32 → C-33 (zero-signal dual-mechanism → timestamp isolation dual-mechanism → multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit → closed reference loop with designation + location → self-announcing clause headers enabling partial double-elision recovery)

**Relationship between C-32 and C-33:** C-33 does not replace C-32. C-32 requires preamble forward-references to name companion mechanisms by full clause designation + block location. C-33 requires the execution-note clause headers within the skill body to carry the same structural-membership parenthetical used in those forward-references — so that the designation in the preamble forward-reference exactly matches the clause header in the execution-note body. A skill can satisfy C-32 PASS at PARTIAL on C-33 when preamble forward-references achieve designation + location, but execution-note clause headers use bare clause names without the structural-membership parenthetical. C-33 PASS requires the parenthetical to appear at both the reference point (preamble forward-reference) and the target point (execution-note clause header), enabling identification of architectural membership from either location independently.

**R14 investigation candidate:** Whether a model encountering only the execution-note clause body — preamble and preamble forward-references both elided — activates two-mechanism behavior differently when the clause header contains the `(COMPRESSION-IMMUNE PREAMBLE invocation)` parenthetical versus when it does not. If the parenthetical causes the model to infer a paired COMPRESSION-IMMUNE PREAMBLE and seek its structural authority even when the preamble section is absent, C-33 constitutes a genuine partial double-elision recovery mechanism. If the parenthetical does not alter model behavior under double-elision conditions — the clause executes in isolation without activating the preamble's structural authority — C-33 should be reconsidered as a reference verification optimization (enabling exact-match navigation and human-readable structural traceability) rather than a compression-survival guarantee. R14 should construct a variation achieving C-32 PASS with bare execution-note headers (C-33 PARTIAL) and a variation achieving C-33 PASS (parenthetical in clause headers). Compare behavior under simulated preamble-elision (execution notes preserved, preamble absent) to determine whether C-33 adds survivability beyond C-31 + C-32 alone.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(33 total criteria; C-01–C-20 definitions unchanged from v6.)*

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

**PASS** — `inertia_cost` explicitly classifies recoverability as bounded or unbounded, with a one-line justification naming why the failure is or is not detectable before propagation.

---

#### C-24 — Timestamp structural field isolation *(vN)*

The current-date anchor in STATUS must occupy a structurally designated position — a standalone labeled field or an explicit isolated line — rather than being embedded in prose narrative. Prose-embedded timestamps ("As of March 17, 2026, the following signals have been gathered...") merge the temporal anchor with content; when surrounding prose is elided under compression, the timestamp becomes unrecoverable. A structurally isolated timestamp can be extracted independently of narrative context.

**PARTIAL** — Timestamp present in STATUS but embedded in a prose sentence or block header that also contains other content; the temporal anchor is not independently addressable without parsing its containing structure.

**PASS** — Timestamp occupies a designated structural position that can be identified and extracted without parsing surrounding narrative; the field or line is self-evidently the temporal anchor.

This criterion is part of the timestamp isolation chain (C-16 → C-24 → C-30) and the compression survival generalization chain (C-24 → C-29 → C-30).

---

#### C-25 — Namespace-stratified absence characterization *(vN)*

When `found` contains signals from zero or few namespaces (sparse or empty coverage), the STORY block must not characterize absence in aggregate. Synthesis must identify which namespaces are empty and what each namespace's absence independently implies about the feature's evidence state. Aggregate absence ("no signals found across all namespaces") is less informative than stratified absence ("no scout signal means the market surface has not been probed; no flow signal means no behavioral model of the feature exists"). The gap pattern has internal structure that aggregate framing destroys.

**PARTIAL** — Zero-signal synthesis present (C-22 PASS) but characterizes absence at the aggregate level; namespace-level stratification absent or collapsed into a single observation.

**PASS** — STORY identifies absent namespaces explicitly and characterizes what each namespace's absence implies independently — the gap pattern is structured by namespace, not summarized as undifferentiated absence.

---

#### C-26 — Recoverability-differentiated action prescriptions *(vN)*

When the VERDICT classifies inertia by recoverability (C-23 PASS), it must prescribe distinct action postures for each class — not generic guidance that applies equally to bounded and unbounded cases. Bounded inertia → the prescribed action must include a monitoring component (what to watch post-commit). Unbounded inertia → the prescribed action must include a gate condition (what evidence must exist before commitment is permissible). A verdict that classifies recoverability but prescribes generic action ("proceed with caution" / "do not proceed") leaves the team to derive the specific action from the classification — the verdict is classified but not executable.

**PARTIAL** — Bounded/unbounded classification present (C-23 PASS) but action prescription is generic or identical across recoverability classes; the prescriptions do not differentiate what the team must do differently for bounded vs. unbounded cases.

**PASS** — VERDICT contains distinct action prescriptions by recoverability class: monitoring-oriented prescription for bounded inertia, gate-condition prescription for unbounded inertia.

---

#### C-27 — Gap implication chain to readiness state *(vN)*

The zero-signal STORY synthesis (C-22 PASS, C-25 PASS) must trace the namespace absence pattern through a causal chain to a readiness conclusion. The chain form: [namespace X absent] → [knowledge domain Y is unprobed] → [therefore the team cannot assess Z] → [readiness state conclusion for Z]. Without the causal chain, absence characterization remains observational — the team knows what is missing but must still derive whether the gap prevents commitment. The causal chain makes the synthesis evaluative.

**PARTIAL** — Namespace-stratified absence characterization present (C-25 PASS) but synthesis ends at the observational level; the gap pattern is described but not traced to a readiness conclusion — the team must still synthesize whether the absence is blocking.

**PASS** — STORY traces at least one namespace absence through the full causal chain to a readiness state conclusion. The synthesis is evaluative: absence implies a specific knowledge gap, which implies a specific commitment risk, which implies a readiness state.

---

#### C-28 — Bounded inertia detection specification *(vN)*

When the VERDICT prescribes a monitoring step for bounded inertia (C-26 PASS), the monitoring step must name a specific detectable signal — an observable event, threshold, or state change that would indicate the predicted failure is occurring. "Monitor post-commit" is a posture, not a specification. A team given only a posture must decide what to monitor and what constitutes a detection event, reintroducing decision latency that the verdict was meant to eliminate. A named detection signal makes monitoring executable: the team knows what to watch for and when the monitoring condition has been satisfied.

**PARTIAL** — Monitoring step present for bounded inertia cases (C-26 PASS) but no named detectable signal; the step prescribes ongoing attention without a detection criterion.

**PASS** — Bounded inertia monitoring step names a specific detectable signal — an event, threshold, or observable state change — that would confirm the predicted failure is manifesting. The detection criterion is explicit and not dependent on team judgment to identify.

---

#### C-29 — Zero-signal synthesis dual-mechanism protection *(vN)*

The STORY zero-signal synthesis mandate (C-22 PASS) must be protected by two independent mechanisms: (1) a ZERO-SIGNAL SYNTHESIS MANDATE execution note within the STORY block, and (2) a TOKEN-PRESSURE GUARD clause in the COMPRESSION-IMMUNE PREAMBLE section that restates the mandate as a structural rule. Under single-mechanism protection, compression that elides the STORY execution note eliminates the only declaration of the zero-signal synthesis requirement, allowing a model operating on compressed context to omit synthesis without instruction conflict. The dual mechanism ensures the requirement survives elision of either location independently.

**PARTIAL** — Zero-signal synthesis present (C-22 PASS) but protected by a single mechanism; either the STORY execution note exists without a companion preamble guard clause, or a preamble guard clause exists without a companion STORY execution note.

**PASS** — Zero-signal synthesis mandate is declared in both the STORY block execution note and as a named guard clause in the COMPRESSION-IMMUNE PREAMBLE, with each mechanism independently sufficient to activate the mandate if the other is elided.

---

#### C-30 — Timestamp isolation dual-mechanism protection *(vN)*

The STATUS timestamp structural isolation (C-24 PASS) must be protected by two independent mechanisms: (1) a TIMESTAMP ISOLATION execution note within the STATUS block, and (2) a COMPRESSED-COLLAPSE GUARD clause in the COMPRESSION-IMMUNE PREAMBLE section that restates the isolation requirement as a structural rule. Under single-mechanism protection, compression that elides the STATUS execution note removes the only declaration of the timestamp isolation requirement, allowing the timestamp to drift into narrative embedding under token pressure. The dual mechanism ensures the isolation requirement survives elision of either location independently.

**PARTIAL** — Timestamp isolation present (C-24 PASS) but protected by a single mechanism; either the STATUS execution note exists without a companion preamble guard clause, or a preamble guard clause exists without a companion STATUS execution note.

**PASS** — Timestamp isolation requirement is declared in both the STATUS block execution note and as a named guard clause in the COMPRESSION-IMMUNE PREAMBLE, with each mechanism independently sufficient to enforce the isolation if the other is elided.

---

#### C-31 — Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit *(v12)*

When multiple execution rules require dual-mechanism compression protection (C-29 and C-30 PASS), the preamble guard clauses should be consolidated into a single designated COMPRESSION-IMMUNE PREAMBLE section rather than maintained as per-rule positional annotations. The preamble must carry an explicit structural designation (e.g., `=== COMPRESSION-IMMUNE PREAMBLE ===`) and must self-declare as a structural contract governing the rules it contains. The bidirectional circuit requirement: (1) the preamble self-declares as a structural contract, AND (2) each execution note that references the preamble invokes it by structural designation name — not positionally ("see above," "the preamble above"). Without back-invocation by designation name, the preamble's structural authority is one-directional: the preamble declares immunity, but execution notes that invoke positionally cannot be verified as referencing the correct preamble when compression elides surrounding context.

**PARTIAL (three bands):**
- Adjacency only: multiple preamble clauses co-located without any structural designation; proximity is the only organizational signal.
- Descriptive label: preamble has a label but it is presentational or descriptive in character ("EXECUTION RULES," "COMPRESSION-CRITICAL EXECUTION RULES"), not declared as a structural contract; execution notes invoke the preamble positionally.
- One-directional contract: preamble carries structural designation and self-declares as a structural contract, but execution notes invoke it positionally rather than by designation name; the contract declaration is not affirmed from the execution-note side.

**PASS** — Preamble carries an explicit structural designation, self-declares as a structural contract, and all execution notes that reference the preamble invoke it by structural designation name rather than by position.

---

#### C-32 — Closed compression reference loop *(v12)*

When C-31 PASS, the COMPRESSION-IMMUNE PREAMBLE section must contain forward-references naming each companion execution-note mechanism by its full clause designation and block location, creating a reference architecture navigable from the preamble alone when execution notes are elided. This closes the circuit initiated by C-31: C-31 establishes that execution notes name the preamble by designation (execution → preamble navigation); C-32 requires the preamble to name companion mechanisms by designation + location (preamble → execution navigation). With both directions established, either entry point survives single-location elision and can recover the full two-mechanism architecture.

Full clause designation requires the complete clause name as used in the execution-note header — e.g., `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation)` — not a generic block name ("the STORY execution note") or a role-type descriptor ("the declarative execution note in the STORY block"). Block location identifies which block the companion mechanism occupies (STORY block, STATUS block), providing spatial grounding that survives block-level compression even if intra-block content is elided.

**PARTIAL (four bands):**
- Generic block names only: references name the block but not the clause — "The STORY execution note," "The STATUS execution note." No designation, no intra-block specificity beyond block identity. Navigation requires execution notes to be present; preamble-alone recovery is not possible.
- Location + role-type descriptor: block location present, but clause is identified by role class ("the declarative execution note in the STORY block") rather than full designation. Ambiguous when a block contains multiple execution notes of the same role class; "declarative" describes a type, not a specific instance.
- Designation only: full clause designation present, but no block location specified. Navigable by designation search when block structure survives compression; not navigable when block organization is elided and only clause names are recoverable.
- Asymmetric: some companion mechanism references achieve full designation + location while others achieve designation only or less. Preamble navigability is bounded by the least-complete reference — the weakest forward-reference determines the architecture's compression resilience ceiling.

**PASS** — All companion mechanism forward-references in the preamble contain: (1) full clause designation (complete clause name, not generic or role-type), and (2) block location (which block the companion mechanism occupies). The closed reference loop is complete — either entry point (preamble or execution note) survives single-location elision and recovers the full two-mechanism architecture.

---

#### C-33 — Self-announcing execution-note clause headers *(v13)*

When C-32 PASS, the companion execution-note clause headers within the skill body carry the identical structural-membership parenthetical used in the preamble's forward-references — e.g., `(COMPRESSION-IMMUNE PREAMBLE invocation)` — creating exact-match designation symmetry between the reference point (preamble forward-reference) and the target point (execution-note clause header). Without this symmetry, the preamble names a clause with a full designation that may not match the actual header in the execution-note body, introducing a navigation gap: a model following the preamble's forward-reference arrives at a clause whose header does not confirm the match.

With exact-match designation symmetry, a model encountering the execution-note clause header in a compressed fragment can identify the clause as a COMPRESSION-IMMUNE PREAMBLE member from the header alone, without locating the preamble. The parenthetical announces the structural relationship at the point of encounter. This is the architectural seed of partial double-elision recovery: when the preamble is elided but execution-note clause headers survive, the parenthetical carries the architectural membership signal to the surviving fragment.

**PARTIAL** — Structural-membership parenthetical present in preamble forward-references (C-32 PASS) but absent from actual execution-note clause headers in the skill body; the forward-reference and clause header use different designations, breaking exact-match symmetry. A model following the preamble's forward-reference cannot confirm arrival at the correct clause from the clause header alone.

**PASS** — Companion execution-note clause headers in the skill body carry the identical designation used in the preamble's forward-references, including the structural-membership parenthetical. The designation is verifiable at both ends of the reference: preamble forward-reference names `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block`; the STORY block execution-note header reads `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation)`. A model encountering the clause header alone can identify the COMPRESSION-IMMUNE PREAMBLE relationship without the preamble being present.

**R14 investigation candidate:** Whether a model encountering only the execution-note clause body — preamble and preamble forward-references both elided — activates the two-mechanism behavior differently when the clause header contains the `(COMPRESSION-IMMUNE PREAMBLE invocation)` parenthetical versus when it does not. If the parenthetical causes the model to infer a paired COMPRESSION-IMMUNE PREAMBLE and seek its structural authority even when the preamble section is absent, C-33 constitutes a genuine partial double-elision recovery mechanism. If the parenthetical does not alter model behavior under double-elision — the clause executes in isolation without activating the preamble-declared architecture — C-33 should be reconsidered as a reference verification optimization (enabling exact-match navigation and human-readable structural traceability) rather than a compression-survival guarantee. R14 should construct a variation achieving C-32 PASS with bare execution-note headers (C-33 PARTIAL) and a variation achieving C-33 PASS (parenthetical present in clause headers). Compare behavior under simulated preamble-only-elision to determine whether the parenthetical in the clause header allows the model to recover the preamble's structural authority from the execution-note side alone — an inversion of the C-31 single-elision guarantee.
