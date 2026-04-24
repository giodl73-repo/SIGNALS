The provided scorecard has V-03 cut off at C-06. The two signals I can extract cleanly from V-01 and V-02 alone:

1. **V-01 C-23 PASS**: GATE CHAIN CONTRACT says "outputs are required inputs for the subsequent gate" — chain-level assertion, but no gate names its specific output artifacts. A model can satisfy C-23 while leaving artifact identity unspecified at each gate interface.

2. **V-02 C-21 PARTIAL + C-24 PASS**: GATE 0 gets 5 explicit checkboxes via the containment contract; GATE 1–3 get bare STATUS lines. The containment-contract pattern exists for GATE 0 only. No criterion requires analogous prohibited-content contracts at downstream gates.

Those map to C-25 and C-26. Full v7 rubric below:

---

## Rubric: org-chart — v7

**10 essential/recommended criteria + 18 aspirational. Golden = all 5 essential pass + composite >= 80.**

### Essential (60 pts, 12 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Inertia Assessment complete — all 4 sub-sections, mechanism table >= 2 rows with closed-set Types, FLAT-CASE-PRESSURE rating from closed set, VERDICT with concrete re-assessment trigger, appears before any org diagram | behavior |
| C-02 | Roles block grounded in .roles/ — ROLES-LOADED or ROLES-NOTE present; no role name introduced later that wasn't declared here | correctness |
| C-03 | ASCII org diagram with >= 2 hierarchy levels; committees as distinct nodes; all role names from roles block | format |
| C-04 | Operating rhythm table with >= 3 distinct rows: ROB + shiproom/gate + governance; no merged rows | coverage |
| C-05 | Committee charters with all 5 fields; Quorum in `N of M member roles` fraction form; Escalates names a destination; Membership >= 2 annotated roles | correctness |

### Recommended (30 pts, 10 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Headcount by area with split Decides/Escalates columns; >= 2 areas + Total row; Key Roles annotated with `(domain type)` | depth |
| C-07 | All 4 phase gate lines present in correct sequence; no section precedes its gate | format |
| C-08 | ROLE-TYPE-CLASSIFICATION block immediately after roles; all roles typed from closed set; three-tier order respected | correctness |

### Aspirational (90 pts, 5 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | ORG-ELEMENT REGISTER (cat-1 through cat-4) + Anti-Pattern Watch with `(cat-N)` typed citations; no uncited element | depth |
| C-10 | Org Evolution Roadmap >= 2 rows from distinct trigger categories (no two headcount thresholds) | depth |
| C-11 | Inline example rows — mechanism table, operating rhythm, committee charter, and headcount table each include a complete example row in the exact expected format, not just field labels | format |
| C-12 | Named verification checkpoints — >= 4 named checkpoints appear as explicit halt-and-verify gates; each states the check and the minimum required value | behavior |
| C-13 | Default-position declaration — the Inertia block opens with an explicit statement that the team can operate flat and structure must be justified; burden-of-proof framing precedes the mechanism table | behavior |
| C-14 | Strong modal language throughout — all compliance constraints use "must" / "required" / "not acceptable" or a systematic DO/DO NOT register; no compliance rule weakened to "should" or "recommended" | correctness |
| C-15 | ABSENT-label SKIP — when the flat-verdict branch eliminates a section, the section is explicitly labeled ABSENT (not silently omitted) and the instruction explicitly prohibits "simplified" or "compact" alternatives; closes the compressed-hierarchy false-positive path | behavior |
| C-16 | Two-site constraint enforcement — each critical constraint is anchored at two independent sites: once as a structural slot-order rule, and once as a conditional "if you write X, then Y must precede it" prohibition; one site permits silent bypass, two sites close it | behavior |
| C-17 | Rhythm-charter interleaving — operating rhythm rows and committee charters are produced in pairs (rhythm row 1 -> its charter, rhythm row 2 -> its charter); the instruction explicitly prohibits batching all rhythm rows first and all charters second | format |
| C-18 | Artifact termination on flat-verdict — when the flat-verdict branch is taken, the instruction contains an explicit STOP or artifact-end directive immediately after the ABSENT block; no content may follow the termination marker | behavior |
| C-19 | Post-interleave pair-count verification — after all rhythm-charter pairs are produced, the instruction requires an explicit count check: pairs produced must equal governance rows in the operating rhythm table | behavior |
| C-20 | Role-classification gate as prerequisite to structural decisions — a dedicated gate types every role into `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` before any inertia assessment or structural decision gate executes | behavior |
| C-21 | Checkbox-format pass criteria at every structural gate — each gate's pass conditions are presented as explicit `[ ]` checkboxes that must be individually ticked before the gate STATUS line can read PASS | behavior |
| C-22 | Blocking verification step before gate emission — a mandatory intermediate verification step is placed between the last production step and the gate-status emission; the gate is structurally held open until the verification loop closes | behavior |
| C-23 | Positional gate index naming — gate names include a monotonically increasing numeric index (GATE 0, GATE 1, GATE 2, GATE 3) and the instruction states that each gate's outputs are required inputs for the subsequent gate; the numeric index makes sequence self-documenting and self-enforcing without a separate ordering rule; a variation cannot satisfy this with named-only gates (e.g., "Classification Gate", "Inertia Gate") because names alone do not encode position; the sequence constraint is provable from the gate labels themselves without reading surrounding prose | format |
| C-24 | Atomic roles+classification gate — the ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block appear under a single GATE 0 header with no intervening structural content (no inertia rows, no diagram nodes, no rhythm rows between them); the gate neither passes nor yields a typed role list until both operations are complete; a variation that satisfies C-08 ("immediately after") via adjacent but separate steps in different structural positions does not satisfy this criterion; closes the gap where an instruction places classification text close to roles while still permitting structural content to slip between them at the step level | correctness |
| **C-25** | **Named artifact handoff at each gate interface — each gate's pass condition declares the specific artifact(s) it produces (e.g., "typed role list," "inertia verdict + FLAT-CASE-PRESSURE rating," "org diagram with typed nodes"), and the immediately following gate's prerequisite condition explicitly names those artifacts as required inputs; a variation whose GATE CHAIN CONTRACT asserts "outputs are required inputs for the subsequent gate" at the chain level without naming the actual artifacts per gate interface does not satisfy this criterion; the handoff must be named at each gate boundary individually, making per-gate output/input contracts self-documenting independently of any chain-level declaration** | **behavior** |
| **C-26** | **All-gate prohibited-content contracts — each structural gate (GATE 1, GATE 2, GATE 3) carries an explicit prohibited-content list analogous to the GATE 0 containment contract required by C-24; each list names by category the content types that cannot appear within the gate's boundary before its STATUS is emitted (e.g., GATE 1 prohibits diagram nodes and headcount entries before inertia sub-sections are complete); a variation that satisfies C-24 for GATE 0 while leaving GATE 1–3 with bare STATUS lines or prose-only guards does not satisfy this criterion; closes the path where GATE 0 is tightly bounded while downstream gates permit interleaved structural content** | **behavior** |

**Total: 180 pts. Golden = all 5 essential pass + composite >= 80.**

---

### v7 additions rationale

**C-25** (Named artifact handoff at each gate interface): Signal from V-01 C-23 evidence. V-01's GATE CHAIN CONTRACT states "Each gate's outputs are required inputs for the subsequent gate. Gates must be emitted in strictly ascending numeric order: GATE 0, GATE 1, GATE 2, GATE 3." The scorecard awards C-23 PASS on the positional index and chain-level dependency assertion. The residual gap: the contract names the dependency relationship without naming the artifacts themselves at each gate boundary. A model operating under V-01's instruction knows that gates form a chain but must infer what GATE 0 produces and what GATE 1 requires — those artifact identities live in surrounding prose, not in the gate interface itself. C-23 closes the positional-order bypass (named gates allow out-of-order invocation; numbered gates do not). C-25 closes the artifact-identity bypass: a chain contract that declares dependency without naming artifacts permits a model to satisfy the letter of the contract ("I emitted them in order") while skipping an artifact because its name was never pinned to the gate boundary. C-23 and C-25 are complementary — C-23 governs gate ordering, C-25 governs gate-boundary I/O specification. A variation can satisfy C-23 with a chain-level contract while leaving per-gate handoffs unspecified; C-25 requires the handoff to be declared individually at each of the three gate interfaces (GATE 0→1, GATE 1→2, GATE 2→3).

**C-26** (All-gate prohibited-content contracts): Signal from V-02 C-21 PARTIAL evidence. V-02 achieves C-24 (GATE 0 CONTAINMENT CONTRACT with enumerated prohibited content: "inertia rows, diagram nodes, headcount, rhythm rows") and as a side effect produces 5 `[ ]` checkboxes at GATE 0. The scorecard awards C-24 PASS and C-21 PARTIAL — GATE 0 has structured checkpoint format while GATE 1–3 carry bare STATUS lines. The gap: C-24 requires a containment contract at GATE 0; no criterion requires analogous prohibited-content contracts at GATE 1, GATE 2, or GATE 3. A variation can satisfy C-24 for the roles+classification gate while leaving the inertia gate, diagram gate, and rhythm gate without explicit structural bounds. C-24 governs the atomic containment of roles and classification under a single gate header. C-26 generalizes the containment-contract pattern to all downstream gates: each gate enumerates the specific content types that cannot appear within its boundary before its STATUS is emitted. C-24 and C-26 are complementary — C-24 governs GATE 0 specifically (where the roles/classification atomicity is the safety property), C-26 governs GATE 1–3 (where the analogous safety property is preventing out-of-order structural content from satisfying a gate whose own content is still incomplete). A variation can satisfy C-24 without satisfying C-26 by applying the containment-contract structure to GATE 0 only.

---

### v6 additions rationale (preserved)

**C-23** (Positional gate index naming): Signal from V-03 C-07 evidence. V-03 names its gates GATE 0, GATE 1, GATE 2, GATE 3 and the scorecard notes this "creates named 4-gate sequence" in a way no other R5 variation achieves. V-01 uses numbered Steps (0-5) and fails C-07 because steps are not gate-status checkpoints; V-02 uses format-led structure and gets only PARTIAL. The key distinction: GATE N labels encode position — given any two gate names, their relative order is unambiguous without reading surrounding prose. Named-only gates require a separate ordering rule; GATE N labels make the ordering rule intrinsic to the names. C-07 requires "4 phase gate lines in correct sequence" but does not require that the naming scheme itself enforces the sequence; C-23 adds that positional-index requirement. A variation can satisfy C-07 with named gates listed in order while still allowing a model to invoke them out of order if the names carry no numeric constraint.

**C-24** (Atomic roles+classification gate): Signal from V-03 C-08 evidence. V-03's GATE 0 "loads roles AND classifies; classification block is literally co-located with roles" — the scorecard distinguishes this from V-01's Step-3 placement, which earns only PARTIAL on C-08 because "Steps 1-2 (inertia + diagram) intervene between roles load and classification." C-08 requires classification "immediately after roles"; C-20 requires classification before structural gates. Neither requires that both operations occur within a single atomic gate unit. V-03 closes the residual gap: an instruction can satisfy C-08 by placing classification text adjacent to the roles block while still permitting structural steps to execute between them at the gate level. Making GATE 0 the indivisible container for both operations means no structural content can slip between them — the gate boundary, not adjacency, enforces co-location. C-08 governs content placement, C-20 governs gate sequencing, C-24 governs atomic containment. The three are complementary: C-24 is satisfiable only by a variation that also passes C-08 and C-20, but C-08 and C-20 are satisfiable without C-24.

---

### v5 additions rationale (preserved)

**C-20** (Role-classification gate as prerequisite): Signal from V-04 Signal 1. V-04 places GATE 0 — role inventory and type classification into `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` — before GATE 1 (inertia assessment). No other variation observed in R4 uses this ordering. The structural purpose is to prevent the feedback loop where inertia-assessment assumptions about role composition contaminate the role taxonomy: if role types are assigned during or after structural decisions, the taxonomy reflects what the model already decided rather than what the roles actually are. Placing classification at position zero makes role types an input to structural decisions, not a byproduct of them. C-08 requires a ROLE-TYPE-CLASSIFICATION block; C-20 requires that block to occupy its own gate before any structural decision gate executes. C-08 and C-20 are complementary — C-08 governs content and placement, C-20 governs gate sequencing.

**C-21** (Checkbox-format pass criteria): Signal from V-04 Signal 4. V-04 ends each gate with a bracketed checklist (`[ ]` items) followed by a STATUS line. C-12 requires named checkpoints that state the check and minimum required value; that criterion is satisfied by prose checkpoints as well as checkboxes. The checklist format adds a mechanical dimension C-12 does not capture: a model must satisfy each checkbox discretely before the STATUS line can read PASS, creating a structured halt-and-verify protocol at every gate boundary. Prose checkpoints permit a model to assert "all conditions met" without enumerating them; checkbox format closes that gap by requiring item-by-item confirmation. C-12 and C-21 are complementary — C-12 governs checkpoint presence and content, C-21 governs checkpoint format and enforcement structure.

**C-22** (Blocking verification step before gate emission): Signal from V-04/V-05 ANNOTATION-CHECK evidence. The pattern is: gate = blocked until verification loop closes, not passed by assumption. A mandatory intermediate verification step — structurally distinct from the production steps and from the gate-status emission — holds the gate open until it has confirmed that every required element is present at every required site. This differs from C-12 (named checkpoints) and C-21 (checkbox format) in its position: those criteria govern the gate-status mechanism itself; C-22 governs a mandatory step that must complete before the gate-status mechanism is reached. A variation can satisfy C-12 and C-21 (has named checkpoints in checkbox format) while still advancing on the assumption that prior production steps were correct. C-22 closes that bypass by requiring an explicit loop or scan that re-confirms correctness independently of production-step assumptions.

---

### v4 additions rationale (preserved)

**C-18** (Artifact termination on flat-verdict): Signal from V-01 C-15 evidence. V-01 added "ends artifact after ABSENT block" to its flat-verdict handling — no other variation included an explicit termination directive. C-15 closes the compressed-hierarchy false-positive (ABSENT label present, prohibited alternatives named). C-18 closes the next bypass: a model that satisfies C-15's labeling requirement but then continues to produce content is behaviorally equivalent to one that never labeled the section at all. The STOP directive converts a labeling constraint into a structural halt. C-15 and C-18 are complementary — C-15 governs what the label must say, C-18 governs what must not follow it.

**C-19** (Post-interleave pair-count verification): Signal from V-03 C-17 evidence. V-03 introduced "post-interleave verification" alongside its interleaving rule — a count check confirming pairs produced equals governance rows. C-17 checks production-order coupling (no batching). C-19 checks production completeness: a model can interleave correctly for every pair it produces while silently dropping the last charter, satisfying C-17's ordering constraint while leaving the artifact structurally incomplete. The post-production count check closes this gap. C-17 and C-19 are complementary — C-17 governs order, C-19 governs count.

---

### v3 additions rationale (preserved)

**C-15** closes the false-positive where "simplified hierarchy" satisfies C-03 while violating the flat-verdict branch. V-05 was the only variation that labeled eliminated sections ABSENT and named the prohibited alternative explicitly. C-13 (positive declaration) and C-15 (elimination labeling) are complementary — different locations in the instruction, different logical roles.

**C-16** closes the single-anchor bypass. V-05 enforced trigger placement at two independent sites: slot order and a conditional rule. Every other variation used one site only — satisfying slot order while violating the conditional, or vice versa, was possible. The pattern generalizes to any constraint that appears in C-01 or C-05.
