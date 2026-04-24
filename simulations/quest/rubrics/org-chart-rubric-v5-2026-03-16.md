## Rubric: org-chart — v5

**10 essential/recommended criteria + 14 aspirational. Golden = all 5 essential pass + composite >= 80.**

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

### Aspirational (70 pts, 5 each)

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
| C-17 | Rhythm-charter interleaving — operating rhythm rows and committee charters are produced in pairs (rhythm row 1 → its charter, rhythm row 2 → its charter); the instruction explicitly prohibits batching all rhythm rows first and all charters second | format |
| C-18 | Artifact termination on flat-verdict — when the flat-verdict branch is taken, the instruction contains an explicit STOP or artifact-end directive immediately after the ABSENT block; no content may follow the termination marker; closes the ABSENT-label-then-continue bypass where a model labels a section ABSENT and proceeds to produce it anyway | behavior |
| C-19 | Post-interleave pair-count verification — after all rhythm-charter pairs are produced, the instruction requires an explicit count check: the number of pairs produced must equal the number of governance rows in the operating rhythm table; closes the silent-drop bypass where a model interleaves correctly for N−1 pairs but omits the final charter | behavior |
| C-20 | Role-classification gate as prerequisite to structural decisions — a dedicated gate types every role into the closed-set taxonomy `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` before any inertia assessment or structural decision gate executes; no structural gate may reference a role type not established in the classification gate; closes the feedback-loop bypass where inertia-assessment assumptions contaminate role taxonomy | behavior |
| C-21 | Checkbox-format pass criteria at every structural gate — each gate's pass conditions are presented as explicit `[ ]` checkboxes that must be individually ticked before the gate STATUS line (`PASS — proceed | FAIL — correct before continuing`) can read PASS; stricter than C-12 (which requires named checkpoints stating a check and minimum value) because it forces mechanical halt-and-verify at every gate boundary, not just at nominated points | behavior |
| C-22 | Blocking verification step before gate emission — a mandatory intermediate verification step (e.g., an ANNOTATION-CHECK loop confirming every role is present at all required sites) is placed between the last production step and the gate-status emission; the gate is structurally held open until the verification loop closes with all items confirmed; the instruction explicitly prohibits advancing on assumption; closes the gap where a gate passes because no check was required, not because the check was run | behavior |

**Total: 160 pts. Golden = all 5 essential pass + composite >= 80.**

---

### v5 additions rationale

**C-20** (Role-classification gate as prerequisite): Signal from V-04 Signal 1. V-04 places GATE 0 — role inventory and type classification into `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` — before GATE 1 (inertia assessment). No other variation observed in R4 uses this ordering. The structural purpose is to prevent the feedback loop where inertia-assessment assumptions about role composition contaminate the role taxonomy: if role types are assigned during or after structural decisions, the taxonomy reflects what the model already decided rather than what the roles actually are. Placing classification at position zero makes role types an input to structural decisions, not a byproduct of them. C-08 requires a ROLE-TYPE-CLASSIFICATION block; C-20 requires that block to occupy its own gate before any structural decision gate executes. C-08 and C-20 are complementary — C-08 governs content and placement, C-20 governs gate sequencing.

**C-21** (Checkbox-format pass criteria): Signal from V-04 Signal 4. V-04 ends each gate with a bracketed checklist (`[ ]` items) followed by a STATUS line. C-12 requires named checkpoints that state the check and minimum required value; that criterion is satisfied by prose checkpoints as well as checkboxes. The checklist format adds a mechanical dimension C-12 does not capture: a model must satisfy each checkbox discretely before the STATUS line can read PASS, creating a structured halt-and-verify protocol at every gate boundary. Prose checkpoints permit a model to assert "all conditions met" without enumerating them; checkbox format closes that gap by requiring item-by-item confirmation. C-12 and C-21 are complementary — C-12 governs checkpoint presence and content, C-21 governs checkpoint format and enforcement structure.

**C-22** (Blocking verification step before gate emission): Signal from V-04/V-05 ANNOTATION-CHECK evidence. The pattern is: *gate = blocked until verification loop closes, not passed by assumption.* A mandatory intermediate verification step — structurally distinct from the production steps and from the gate-status emission — holds the gate open until it has confirmed that every required element is present at every required site. This differs from C-12 (named checkpoints) and C-21 (checkbox format) in its position: those criteria govern the gate-status mechanism itself; C-22 governs a mandatory step that must complete before the gate-status mechanism is reached. A variation can satisfy C-12 and C-21 (has named checkpoints in checkbox format) while still advancing on the assumption that prior production steps were correct. C-22 closes that bypass by requiring an explicit loop or scan that re-confirms correctness independently of production-step assumptions.

---

### v4 additions rationale (preserved)

**C-18** (Artifact termination on flat-verdict): Signal from V-01 C-15 evidence. V-01 added "ends artifact after ABSENT block" to its flat-verdict handling — no other variation included an explicit termination directive. C-15 closes the compressed-hierarchy false-positive (ABSENT label present, prohibited alternatives named). C-18 closes the next bypass: a model that satisfies C-15's labeling requirement but then continues to produce content is behaviorally equivalent to one that never labeled the section at all. The STOP directive converts a labeling constraint into a structural halt. C-15 and C-18 are complementary — C-15 governs what the label must say, C-18 governs what must not follow it.

**C-19** (Post-interleave pair-count verification): Signal from V-03 C-17 evidence. V-03 introduced "post-interleave verification" alongside its interleaving rule — a count check confirming pairs produced equals governance rows. C-17 checks production-order coupling (no batching). C-19 checks production completeness: a model can interleave correctly for every pair it produces while silently dropping the last charter, satisfying C-17's ordering constraint while leaving the artifact structurally incomplete. The post-production count check closes this gap. C-17 and C-19 are complementary — C-17 governs order, C-19 governs count.

---

### v3 additions rationale (preserved)

**C-15** closes the false-positive where "simplified hierarchy" satisfies C-03 while violating the flat-verdict branch. V-05 was the only variation that labeled eliminated sections ABSENT and named the prohibited alternative explicitly. C-13 (positive declaration) and C-15 (elimination labeling) are complementary — different locations in the instruction, different logical roles.

**C-16** closes the single-anchor bypass. V-05 enforced trigger placement at two independent sites: slot order *and* a conditional rule. Every other variation used one site only — satisfying slot order while violating the conditional, or vice versa, was possible. The pattern generalizes to any constraint that appears in C-01 or C-05.

**C-17** closes the batching gap. V-04's "Do not batch all rows first and all charters second" was the only variation to state this. Without the coupling constraint, a variation can pass C-04 (three distinct rhythm rows) and C-05 (five-field charters) while producing them as two disconnected blocks, allowing drift between what the rhythm table names and what the charter specifies.

---

### v2 additions rationale (preserved)

**C-11** (inline example rows): Signal from V-02 and V-05 — schemas with worked examples prevented format drift that field-label-only schemas did not.

**C-12** (named checkpoints): Signal from V-04 — the count-and-advance pattern halted at each structural requirement; no other variation provided equivalent verification gates.

**C-13** (default-position declaration): Signal from V-05 — opening with "THE TEAM CAN OPERATE FLAT" establishes burden-of-proof before any mechanism table row, making the inertia logic explicit rather than implicit.

**C-14** (strong modal language): Derived from V-03's C-01 PARTIAL — "should use" instead of "must use" was the sole cause of failure; the four 100-scoring R1 variations all used unambiguous modal language for every compliance rule. V-05 demonstrated that a systematic DO/DO NOT register achieves this uniformly without restructuring prompt architecture.
