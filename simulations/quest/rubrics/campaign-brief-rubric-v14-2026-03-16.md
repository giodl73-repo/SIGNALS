Good — I have enough context. Here is the complete v14 rubric:

---

## Quest Rubric — v14

`34 criteria, 340 pts max`

---

### What changed: v13 → v14

One investigation resolved (C-33) and one new aspirational criterion extracted from R14 excellence signals (C-34).

**R14 investigation candidate resolved:** C-33 — does symmetric exact-match designation in execution-note clause headers (full structural-membership parenthetical at both the STATUS header and the STORY header) constitute a genuine architectural property independent of C-32? **Status: RESOLVED.** R14 confirms the weakest-link principle is symmetric: V-02 (STATUS header with parenthetical, STORY bare) and V-03 (STORY header with parenthetical, STATUS bare) both score 320/330, demonstrating neither domain (C-29 zero-signal synthesis nor C-30 timestamp isolation) carries privileged C-33 weight. V-04 and V-05 achieve 330/330 with symmetric full-header marking, confirming C-33 PASS is achievable and independently necessary. C-33 is not subsumed by C-32: a skill can achieve C-32 PASS (preamble forward-references carry designation + location) while remaining at C-33 PARTIAL (execution-note clause headers carry bare names).

**C-33 PARTIAL band structure (three bands):**
- V-01 (both headers bare): Neither execution-note clause header carries the structural-membership parenthetical. A model encountering either clause header under preamble-elision sees a bare designation and cannot determine architectural membership without the preamble.
- V-02 / V-03 (asymmetric): One header carries the parenthetical; the other is bare. Weakest-link applies: the self-announcing side achieves partial header symmetry, but the bare side breaks exact-match designation symmetry. The two asymmetric cases are equivalent in score and in their failure mode — the C-33 architecture is only as strong as its least-announced header, and the consequence domain (C-29 vs. C-30) confers no privileged weight.
- C-33 has no full-PARTIAL tier between asymmetric and PASS: either both headers carry the parenthetical or they do not.

**C-33 PASS (V-04 and V-05):** Both the STATUS execution-note clause header (`TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation):`) and the STORY execution-note clause header (`ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation):`) carry the identical structural-membership parenthetical used in the preamble's forward-references. Exact-match designation symmetry is complete at both the reference point (preamble forward-reference) and the target point (execution-note clause header). A model encountering either execution-note header in isolation can identify COMPRESSION-IMMUNE PREAMBLE membership from the header designation alone without locating the preamble.

**R14 excellence signal → C-34:** V-05 achieves C-33 PASS and adds a further structural property not present in V-04: companion execution-note clause **bodies** open with an explicit structural-membership statement and a preamble-independence instruction. The membership statement names the clause as a COMPRESSION-IMMUNE PREAMBLE member from within the clause body itself. The preamble-independence instruction declares that the clause executes even when the preamble section is absent from the rendered context. Together these two body-level declarations extend the self-announcing property from the header (C-33) into the body: a model encountering only the clause body — header present but preamble and all other companion mechanisms elided — can activate the clause's full structural authority without navigating to the preamble. This is a distinct recovery depth from C-33 (header-level announcement, requiring header survival) and from C-31/C-32 (single-location elision only): C-34 targets the case where the preamble AND the companion mechanism's execution notes are both elided while a single clause body survives.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-34 | Self-declaring clause bodies — when C-33 PASS, companion execution-note clause bodies open with (1) an explicit structural-membership statement naming the clause as a COMPRESSION-IMMUNE PREAMBLE member and (2) a preamble-independence instruction declaring the clause executes even when the preamble section is absent; together these enable partial double-elision recovery from the clause body alone | Extends C-33's self-announcing property from the clause header into the clause body; C-34 PASS requires both body components (membership statement + independence instruction) in both companion clause bodies; C-33 guarantees header-level identification under single-mechanism-elision; C-34 extends survivability toward partial double-elision (preamble + other companion both absent, single clause body present) |

**Structural chains updated:**

- Timestamp isolation chain: C-16 → C-24 → C-30 — unchanged from v13
- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29 — unchanged from v13
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 — unchanged from v13
- Compression survival generalization chain: C-24 → C-29 → C-30 — unchanged from v13
- **Compression-immune consolidation chain (extended):** C-29 → C-30 → C-31 → C-32 → C-33 → C-34 (zero-signal dual-mechanism → timestamp isolation dual-mechanism → multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit → closed reference loop with designation + location → self-announcing clause headers enabling header-level identification under preamble-elision → self-declaring clause bodies enabling partial double-elision recovery from body alone)

**Relationship among C-32, C-33, and C-34:**
- C-32 requires preamble forward-references to name companion mechanisms by full clause designation + block location. Operates at the reference point.
- C-33 requires execution-note clause headers to carry the same structural-membership parenthetical used in the preamble forward-references. Operates at the target header. Depends on C-32 PASS (exact-match symmetry requires a matching reference to exist).
- C-34 requires execution-note clause bodies to open with an explicit membership statement and a preamble-independence instruction. Operates at the target body. Depends on C-33 PASS (self-declaring body extends, rather than replaces, self-announcing header).

A skill can achieve C-33 PASS at C-34 PARTIAL when clause headers carry the parenthetical but clause bodies lack the explicit membership statement or independence instruction. C-34 PASS requires both body components present in both companion clause bodies.

**R15 investigation candidate:** Whether a model encountering only a C-34-compliant clause body — preamble section absent and the other companion mechanism's execution notes also absent — activates two-mechanism COMPRESSION-IMMUNE PREAMBLE behavior rather than single-clause execution. Specifically: does the explicit preamble-independence instruction cause the model to execute the clause as if COMPRESSION-IMMUNE PREAMBLE authority were in force, and does the explicit membership statement cause the model to seek or infer the paired companion mechanism even when that mechanism is absent from context? R15 should construct: (a) a variation achieving C-33 PASS with bare clause bodies (C-34 PARTIAL), and (b) a variation achieving C-34 PASS (both membership statement + independence instruction in both clause bodies). Compare behavior under simulated full preamble-elision + other-companion-elision (single clause body present) to determine whether C-34 constitutes genuine partial double-elision recovery or functions as human-readable structural traceability without altering model activation behavior. If C-34 does not alter activation behavior under double-elision, it should be reconsidered as a documentation property (enabling exact-match body navigation and structural auditing) rather than a compression-survival guarantee.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(34 total criteria; C-01–C-20 definitions unchanged from v6.)*

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

---

#### C-25 — Zero-signal synthesis chain intermediate *(chain member)*

Intermediate criterion in the zero-signal synthesis chain (C-18 → C-21 → C-22 → C-25 → C-27 → C-29). PASS requires the STORY execution note to explicitly name the zero-signal synthesis mandate as a governing clause at the point where synthesis instructions are specified, establishing the connection between the structural mandate (C-18) and the dual-mechanism enforcement (C-29).

---

#### C-26 — Verdict action-posture chain intermediate *(chain member)*

Intermediate criterion in the verdict action-posture chain (C-06 → C-23 → C-26 → C-28). PASS requires the VERDICT block to carry a named action sub-label derived from the bounded/unbounded classification — "commit with monitoring" or "do not commit until resolved" — so that the action posture is legible without re-reading the full gap list.

---

#### C-27 — Zero-signal synthesis chain final intermediate *(chain member)*

Final intermediate in the zero-signal synthesis chain before the dual-mechanism terminal (C-29). PASS requires the zero-signal synthesis mandate to appear at point-of-use in the STORY execution note (not only in the preamble), creating a redundant enforcement point that survives preamble-elision independently.

---

#### C-28 — Verdict action-posture chain terminal *(chain member)*

Terminal criterion in the verdict action-posture chain (C-06 → C-23 → C-26 → C-28). PASS requires the VERDICT COMPRESSION GUARD to make the action sub-label non-optional under COMPRESSED rendering — the sub-label must survive even when the full verdict justification is elided.

---

#### C-29 — Zero-signal dual mechanism: preamble TOKEN-PRESSURE GUARD + STORY execution note *(compression-immune consolidation chain)*

The zero-signal synthesis mandate must be enforced at two structurally independent locations: (1) the TOKEN-PRESSURE GUARD in the COMPRESSION-IMMUNE PREAMBLE, which fires when token pressure compresses the skill body, and (2) the ZERO-SIGNAL SYNTHESIS MANDATE execution note in the STORY block, which fires at point-of-use during normal rendering. Either mechanism alone is a single point of failure under compression; both together mean the mandate survives when the preamble is compressed (STORY execution note present) and when only the preamble survives (TOKEN-PRESSURE GUARD present).

**PARTIAL** — One mechanism present; zero-signal synthesis protected under one compression scenario but not both.

**PASS** — Both mechanisms present, structurally named, and independently sufficient to enforce the zero-signal synthesis mandate.

---

#### C-30 — Timestamp isolation dual mechanism: preamble COMPRESSED-COLLAPSE GUARD + STATUS execution note *(compression-immune consolidation chain)*

The timestamp structural isolation property (C-24) must be enforced at two structurally independent locations: (1) the COMPRESSED-COLLAPSE GUARD in the COMPRESSION-IMMUNE PREAMBLE, and (2) the TIMESTAMP ISOLATION execution note in the STATUS block. Dual-mechanism structure mirrors C-29 for the timestamp domain.

**PARTIAL** — One mechanism present.

**PASS** — Both mechanisms present, structurally named, and independently sufficient.

---

#### C-31 — Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit *(compression-immune consolidation chain)*

The COMPRESSION-IMMUNE PREAMBLE must be named by a structural designation (not a generic heading), and the bidirectional reference circuit must be closed: the preamble references its companion execution notes, and the execution notes reference the preamble by the same structural designation. A one-directional reference (preamble → execution notes only, or execution notes → preamble only) is a partial circuit: a model entering from the unreferenced side cannot confirm the architectural relationship.

**PARTIAL** — Preamble named by structural designation and references companion execution notes, but execution notes do not reference the preamble by designation (one-directional circuit).

**PASS** — Both directions closed: preamble → execution notes (by designation), execution notes → preamble (by exact structural designation). A model entering from either location can navigate to the other.

---

#### C-32 — Closed reference loop: preamble forward-references name companions by full clause designation + block location *(compression-immune consolidation chain)*

Preamble forward-references to companion execution notes must name each companion by both (1) full clause designation (the exact clause name as it appears in the execution-note header) and (2) block location (the block containing the execution note). Generic block-name references ("The execution note in STORY") are insufficient: under block-structure elision, a generic reference cannot identify its target. Role-descriptor references ("the declarative execution note in STORY") are insufficient: a role class cannot resolve to a specific clause under multi-note compression. Designation without location is insufficient: without spatial grounding, a model navigating by designation search cannot recover under block-organization elision. Location without full designation is insufficient for the same reason.

**PARTIAL** — Four bands, analogous to C-31's three bands:
- Generic block name only (no designation, no intra-block specificity)
- Location + role-type descriptor (block present, clause identified by role class not designation)
- Designation only, no location (full clause designation present, block location absent)
- Asymmetric (one companion reference achieves designation + location; the other does not — weakest-link applies)

**PASS** — Both companion mechanism references in the preamble contain full clause designation + block location. The closed reference loop is complete from the preamble entry point: preamble → companions (designation + location) → preamble (by designation, per C-31).

---

#### C-33 — Self-announcing clause headers *(R13 Pattern — V-05; R14 confirmed)*

When C-32 PASS, companion execution-note clause headers in the skill body carry the identical structural-membership parenthetical `(COMPRESSION-IMMUNE PREAMBLE invocation)` used in the preamble's forward-references, creating exact-match designation symmetry between the reference point (preamble forward-reference) and the target point (execution-note clause header). A model encountering only the execution-note clause header can identify COMPRESSION-IMMUNE PREAMBLE membership from the header alone, without locating the preamble.

**PARTIAL** — C-32 PASS achieved but one or both execution-note clause headers use bare names. Two asymmetric sub-bands exist (STATUS header with parenthetical / STORY header bare; STORY header with parenthetical / STATUS header bare) and are equivalent in score: weakest-link applies symmetrically — neither consequence domain (timestamp isolation nor zero-signal synthesis) carries privileged C-33 weight. A skill achieving header symmetry on one side only scores the same as a skill with both headers bare; C-33 has no intermediate tier between asymmetric-PARTIAL and PASS.

**PASS** — Both the STATUS execution-note clause header and the STORY execution-note clause header carry the structural-membership parenthetical. Exact-match designation symmetry is complete. A model encountering either execution-note header in isolation can confirm COMPRESSION-IMMUNE PREAMBLE membership from the header designation alone.

This criterion is independent of C-32: a skill can achieve C-32 PASS (forward-references carry designation + location) while remaining at C-33 PARTIAL (execution-note clause headers carry bare names). C-33 adds the symmetric reverse: the target carries the same designation string as the reference, enabling header-level identification under preamble-elision.

---

#### C-34 — Self-declaring clause bodies enabling partial double-elision recovery *(R14 Pattern — V-05)*

When C-33 PASS, companion execution-note clause bodies open with two components: (1) an explicit structural-membership statement naming the clause as a COMPRESSION-IMMUNE PREAMBLE member from within the clause body itself, and (2) a preamble-independence instruction declaring that the clause executes even when the preamble section is absent from the rendered context. Together these declarations extend the self-announcing property from the clause header (C-33) into the clause body, enabling partial double-elision recovery: a model encountering only the clause body — preamble section absent and the other companion mechanism's execution notes also absent — can identify architectural membership from the body's opening declaration and execute without requiring preamble authority to be located.

**PARTIAL** — C-33 PASS achieved but one or both clause bodies lack the explicit membership statement, the preamble-independence instruction, or both. A clause body that opens with operational instructions without a self-declaration does not enable body-level identification under double-elision conditions. Weakest-link applies symmetrically: a skill with one self-declaring body and one bare body achieves the same C-34 score as a skill with both bodies bare — the architecture is only as resilient as its least-declared clause body.

**PASS** — Both companion execution-note clause bodies open with (1) an explicit structural-membership statement naming the clause as a COMPRESSION-IMMUNE PREAMBLE member and (2) a preamble-independence instruction declaring the clause executes even when the preamble section is absent. A model encountering either clause body in isolation — without header context, without preamble, without the other companion mechanism — can identify COMPRESSION-IMMUNE PREAMBLE membership and execute under that structural authority from the body's opening declaration alone.

This criterion is independent of C-33 in the following sense: C-33 PASS is a prerequisite (C-34 depends on C-33 PASS), but C-33 PASS does not imply C-34 PASS. A skill can carry self-announcing headers while having clause bodies that begin with operational instructions rather than self-declarations. C-34 adds survivability depth: where C-31/C-32 guarantee single-location elision recovery, C-33 extends guarantee to header-level identification under preamble-elision, and C-34 extends survivability toward partial double-elision (preamble + other companion both absent, single clause body present).

**R15 investigation candidate:** Whether a model encountering only a C-34-compliant clause body — preamble absent, other companion mechanism absent — activates two-mechanism COMPRESSION-IMMUNE PREAMBLE behavior rather than single-clause execution. Specifically: does the explicit preamble-independence instruction cause the model to execute the clause as if COMPRESSION-IMMUNE PREAMBLE authority were in force, and does the explicit membership statement cause the model to seek or infer the paired companion mechanism even when it is absent from context? R15 should construct: (a) a variation achieving C-33 PASS with bare clause bodies (C-34 PARTIAL), and (b) a variation achieving C-34 PASS (membership statement + independence instruction in both clause bodies). Compare behavior under simulated double-elision (preamble absent + other companion absent, single clause body present) to determine whether C-34 constitutes a genuine partial double-elision recovery mechanism or functions as human-readable structural traceability without altering model activation behavior. If the latter, C-34 should be reconsidered as a documentation property rather than a compression-survival guarantee.
