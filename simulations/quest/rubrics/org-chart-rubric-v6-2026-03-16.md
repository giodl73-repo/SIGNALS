## Rubric: org-chart — v6

**10 essential/recommended criteria + 16 aspirational. Golden = all 5 essential pass + composite >= 80.**

### Essential (60 pts, 12 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Inertia Assessment complete — all 4 sub-sections, mechanism table >= 2 rows with closed-set Types, FLAT-CASE-PRESSURE rating from closed set, VERDICT with concrete re-assessment trigger, appears before any org diagram | behavior |
| C-02 | Roles block grounded in .craft/roles/ — ROLES-LOADED or ROLES-NOTE present; no role name introduced later that wasn't declared here | correctness |
| C-03 | ASCII org diagram with >= 2 hierarchy levels; committees as distinct nodes; all role names from roles block | format |
| C-04 | Operating rhythm table with >= 3 distinct rows: ROB + shiproom/gate + governance; no merged rows | coverage |
| C-05 | Committee charters with all 5 fields; Quorum in `N of M member roles` fraction form; Escalates names a destination; Membership >= 2 annotated roles | correctness |

### Recommended (30 pts, 10 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Headcount by area with split Decides/Escalates columns; >= 2 areas + Total row; Key Roles annotated with `(domain type)` | depth |
| C-07 | All 4 phase gate lines present in correct sequence; no section precedes its gate | format |
| C-08 | ROLE-TYPE-CLASSIFICATION block immediately after roles; all roles typed from closed set; three-tier order respected | correctness |

### Aspirational (80 pts, 5 each)

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
| **C-23** | **Positional gate index naming — gate names include a monotonically increasing numeric index (GATE 0, GATE 1, GATE 2, GATE 3) and the instruction states that each gate's outputs are required inputs for the subsequent gate; the numeric index makes sequence self-documenting and self-enforcing without a separate ordering rule; a variation cannot satisfy this with named-only gates (e.g., "Classification Gate", "Inertia Gate") because names alone do not encode position; the sequence constraint is provable from the gate labels themselves without reading surrounding prose** | **format** |
| **C-24** | **Atomic roles+classification gate — the ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block appear under a single GATE 0 header with no intervening structural content (no inertia rows, no diagram nodes, no rhythm rows between them); the gate neither passes nor yields a typed role list until both operations are complete; a variation that satisfies C-08 ("immediately after") via adjacent but separate steps in different structural positions does not satisfy this criterion; closes the gap where an instruction places classification text close to roles while still permitting structural content to slip between them at the step level** | **correctness** |

**Total: 170 pts. Golden = all 5 essential pass + composite >= 80.**

---

### v6 additions rationale

**C-23** (Positional gate index naming): Signal from V-03 C-07 evidence. V-03 names its gates GATE 0, GATE 1, GATE 2, GATE 3 and the scorecard notes this "creates named 4-gate sequence" in a way no other R5 variation achieves. V-01 uses numbered Steps (0-5) and fails C-07 because steps are not gate-status checkpoints; V-02 uses format-led structure and gets only PARTIAL. The key distinction: GATE N labels encode position — given any two gate names, their relative order is unambiguous without reading surrounding prose. Named-only gates require a separate ordering rule; GATE N labels make the ordering rule intrinsic to the names. C-07 requires "4 phase gate lines in correct sequence" but does not require that the naming scheme itself enforces the sequence; C-23 adds that positional-index requirement. A variation can satisfy C-07 with named gates listed in order while still allowing a model to invoke them out of order if the names carry no numeric constraint.

**C-24** (Atomic roles+classification gate): Signal from V-03 C-08 evidence. V-03's GATE 0 "loads roles AND classifies; classification block is literally co-located with roles" — the scorecard distinguishes this from V-01's Step-3 placement, which earns only PARTIAL on C-08 because "Steps 1-2 (inertia + diagram) intervene between roles load and classification." C-08 requires classification "immediately after roles"; C-20 requires classification before structural gates. Neither requires that both operations occur within a single atomic gate unit. V-03 closes the residual gap: an instruction can satisfy C-08 by placing classification text adjacent to the roles block while still permitting structural steps to execute between them at the gate level. Making GATE 0 the indivisible container for both operations means no structural content can slip between them — the gate boundary, not adjacency, enforces co-location. C-08 governs content placement, C-20 governs gate sequencing, C-24 governs atomic containment. The three are complementary: C-24 is satisfiable only by a variation that also passes C-08 and C-20, but C-08 and C-20 are satisfiable without C-24.
cation block is literally co-located with roles" -- the scorecard distinguishes this from V-01's Step-3 placement, which earns only PARTIAL on C-08 because "Steps 1-2 (inertia + diagram) intervene between roles load and classification." C-08 requires the classification block "immediately after roles" and C-20 requires classification to precede structural gates. Neither criterion requires that both operations occur within a single atomic gate unit. V-03's pattern closes the residual gap: an instruction can satisfy C-08 by placing classification text adjacent to the roles block in the output while still permitting structural steps to execute between them at the gate level. Making GATE 0 the indivisible container for both roles and classification means no structural content can slip between them -- the gate boundary, not adjacency, enforces co-location. C-08 governs content placement (immediately after), C-20 governs gate sequencing (before structural gates), C-24 governs atomic containment (same gate, no intervening structural content permitted). The three criteria are complementary: C-24 is satisfiable only by a variation that also passes C-08 and C-20, but C-08 and C-20 are satisfiable without C-24.

---

### v5 additions rationale (preserved)

**C-20** (Role-classification gate as prerequisite): Signal from V-04 Signal 1. V-04 places GATE 0 -- role inventory and type classification into `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` -- before GATE 1 (inertia assessment). No other variation observed in R4 uses this ordering. The structural purpose is to prevent the feedback loop where inertia-assessment assumptions about role composition contaminate the role taxonomy: if role types are assigned during or after structural decisions, the taxonomy reflects what the model already decided rather than what the roles actually are. Placing classification at position zero makes role types an input to structural decisions, not a byproduct of them. C-08 requires a ROLE-TYPE-CLASSIFICATION block; C-20 requires that block to occupy its own gate before any structural decision gate executes. C-08 and C-20 are complementary -- C-08 governs content and placement, C-20 governs gate sequencing.

**C-21** (Checkbox-format pass criteria): Signal from V-04 Signal 4. V-04 ends each gate with a bracketed checklist (`[ ]` items) followed by a STATUS line. C-12 requires named checkpoints that state the check and minimum required value; that criterion is satisfied by prose checkpoints as well as checkboxes. The checklist format adds a mechanical dimension C-12 does not capture: a model must satisfy each checkbox discretely before the STATUS line can read PASS, creating a structured halt-and-verify protocol at every gate boundary. Prose checkpoints permit a model to assert "all conditions met" without enumerating them; checkbox format closes that gap by requiring item-by-item confirmation. C-12 and C-21 are complementary -- C-12 governs checkpoint presence and content, C-21 governs checkpoint format and enforcement structure.

**C-22** (Blocking verification step before gate emission): Signal from V-04/V-05 ANNOTATION-CHECK evidence. The pattern is: gate = blocked until verification loop closes, not passed by assumption. A mandatory intermediate verification step -- structurally distinct from the production steps and from the gate-status emission -- holds the gate open until it has confirmed that every required element is present at every required site. This differs from C-12 (named checkpoints) and C-21 (checkbox format) in its position: those criteria govern the gate-status mechanism itself; C-22 governs a mandatory step that must complete before the gate-status mechanism is reached. A variation can satisfy C-12 and C-21 (has named checkpoints in checkbox format) while still advancing on the assumption that prior production steps were correct. C-22 closes that bypass by requiring an explicit loop or scan that re-confirms correctness independently of production-step assumptions.

---

### v4 additions rationale (preserved)

**C-18** (Artifact termination on flat-verdict): Signal from V-01 C-15 evidence. V-01 added "ends artifact after ABSENT block" to its flat-verdict handling -- no other variation included an explicit termination directive. C-15 closes the compressed-hierarchy false-positive (ABSENT label present, prohibited alternatives named). C-18 closes the next bypass: a model that satisfies C-15's labeling requirement but then continues to produce content is behaviorally equivalent to one that never labeled the section at all. The STOP directive converts a labeling constraint into a structural halt. C-15 and C-18 are complementary -- C-15 governs what the label must say, C-18 governs what must not follow it.

**C-19** (Post-interleave pair-count verification): Signal from V-03 C-17 evidence. V-03 introduced "post-interleave verification" alongside its interleaving rule -- a count check confirming pairs produced equals governance rows. C-17 checks production-order coupling (no batching). C-19 checks production completeness: a model can interleave correctly for every pair it produces while silently dropping the last charter, satisfying C-17's ordering constraint while leaving the artifact structurally incomplete. The post-production count check closes this gap. C-17 and C-19 are complementary -- C-17 governs order, C-19 governs count.

---

### v3 additions rationale (preserved)

**C-15** closes the false-positive where "simplified hierarchy" satisfies C-03 while violating the flat-verdict branch. V-05 was the only variation that labeled eliminated sections ABSENT and named the prohibited alternative explicitly. C-13 (positive declaration) and C-15 (elimination labeling) are complementary -- different locations in the instruction, different logical roles.

**C-16** closes the single-anchor bypass. V-05 enforced trigger placement at two independent sites: slot order and a conditional rule. Every other variation used one site only -- satisfying slot order while violating the conditional, or vice versa, was possible. The pattern generalizes to any constraint that appears in C-01 or C-05.

**C-17** closes the batching gap. V-04's "Do not batch all rows first and all charters second" was the only variation to state this. Without the coupling constraint, a variation can pass C-04 (three distinct rhythm rows) and C-05 (five-field charters) while producing them as two disconnected blocks, allowing drift between what the rhythm table names and what the charter specifies.

---

### v2 additions rationale (preserved)

**C-11** (inline example rows): Signal from V-02 and V-05 -- schemas with worked examples prevented format drift that field-label-only schemas did not.

**C-12** (named checkpoints): Signal from V-04 -- the count-and-advance pattern halted at each structural requirement; no other variation provided equivalent verification gates.

**C-13** (default-position declaration): Signal from V-05 -- opening with "THE TEAM CAN OPERATE FLAT" establishes burden-of-proof before any mechanism table row, making the inertia logic explicit rather than implicit.
