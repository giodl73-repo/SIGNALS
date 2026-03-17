Good. I have the complete picture: current skill body baseline (org-chart.t3/SKILL.md, 188 lines), rubric v14 with all 42 criteria, and the two new C-41/C-42 checkpoint enforcement targets. Writing the 5 full variations now.

---

# org-chart — Round 14 Variations (V-01 through V-05)

---

## V-01 — Single axis: CHECKPOINT-INERTIA (minimal blocking form)

**Variation axis:** CHECKPOINT-INERTIA presence and FAIL condition — added as named intermediate verification step at GATE 1 completion before GATE 1 STATUS can emit. All other structure unchanged from current base.

**Hypothesis:** The minimal CHECKPOINT-INERTIA form — a named blocking step with verbatim FAIL condition and blocking gate language — is sufficient to satisfy C-41 without requiring any additional structural reinforcement. Tests whether the FAIL condition text alone ("STRUCTURING-COST FRAME must precede mechanism table rows in output produced; FAIL if any mechanism row appears before frame block is closed") achieves C-41 when placed as a named intermediate step.

---

```
You are running `/org-chart {topic}`.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no role files are found.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with one inferred entry per role.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

Classify roles in this strict three-tier order: Engineering types first, then Operations types, then PM / Design / Research / Other types.
If no Engineering roles are present, begin with Operations types.
If neither Engineering nor Operations roles are present, classify all roles in any order.
DO NOT interleave tiers — complete all entries in one tier before writing any entry from the next tier.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

Produce `ROLE-TYPE-CLASSIFICATION:` immediately after ROLES-LOADED or ROLES-NOTE, following the three-tier constraint.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
Format each entry: `- [role name] — [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table: `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters: `[role name] ([domain type])`.

GATE 0 PASS CHECKLIST:
[ ] ROLES-LOADED or ROLES-NOTE block present
[ ] ROLE-TYPE-CLASSIFICATION block present
[ ] All roles typed from closed set
[ ] Three-tier order respected (Engineering → Operations → remaining)
[ ] No role name introduced later that was not declared here

When all checklist items are ticked, emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to Inertia Assessment until this gate line is present.

─────────────────────────────────────────────
GATE 1 — INERTIA ASSESSMENT
─────────────────────────────────────────────

INPUT REQUIRED: typed role list from GATE 0.
DO NOT begin GATE 1 before `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===` is present.

INERTIA FIRST — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact order:
  Sub-section 1 — Case for Staying Flat
  Sub-section 2 — How We Coordinate Today
  Sub-section 3 — Rebuttal
  Sub-section 4 — VERDICT and Re-assessment Trigger

Sub-section 1 — Case for Staying Flat

STRUCTURING-COST FRAME — REQUIRED FIRST ELEMENT IN SUB-SECTION 1

DO emit a named `STRUCTURING-COST FRAME:` block as the FIRST element in Sub-section 1, before any mechanism table rows.
The frame MUST explicitly enumerate at minimum three overhead categories imposed by formal structure:
  - Coordination overhead (recurring meeting load per added layer)
  - Decision latency overhead (approval chain vs. direct call)
  - Role boundary overhead (ownership ambiguity at layer transitions)
DO NOT write mechanism table rows before this frame block is closed.
The frame establishes overhead categories as the interpretive lens through which each mechanism row is read.

After the STRUCTURING-COST FRAME block is closed, DO produce a three-column mechanism evidence table:
  Columns: `Mechanism Name | Type | Frequency / Participants`
  DO include at minimum two data rows.
  Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
  DO NOT use Type values outside this vocabulary.
  Each Mechanism Name MUST name a specific, observable coordination mechanism.
  DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, count the data rows (header excluded).
IF count < 2: write the missing row(s) until count reaches 2.
THEN substitute the final row count as N and emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present.

Sub-section 2 — How We Coordinate Today

DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 — Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT and Re-assessment Trigger

MUST open with pressure rating line in this format:
`FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.

After emitting the pressure line, choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

If verdict is `CAN-OPERATE-FLAT`: emit an ABSENT block naming what structure is not warranted, then STOP. No further content follows.

─────────────────────────────────────────────
CHECKPOINT-INERTIA — BLOCKING VERIFICATION BEFORE GATE 1 STATUS
─────────────────────────────────────────────

This checkpoint is a blocking intermediate verification step between GATE 1 content production and GATE 1 STATUS emission.
GATE 1 STATUS cannot emit until this checkpoint passes.

CHECKPOINT-INERTIA FAIL CONDITION:
  STRUCTURING-COST FRAME must precede mechanism table rows in output produced.
  FAIL if any mechanism row appears before the STRUCTURING-COST FRAME block is closed.

CHECKPOINT-INERTIA PASS CHECKLIST:
[ ] STRUCTURING-COST FRAME block is present
[ ] STRUCTURING-COST FRAME block is closed before first mechanism table row
[ ] Mechanism table has >= 2 data rows with Types from closed vocabulary
[ ] FLAT-CASE-CLOSED separator is present
[ ] FLAT-CASE-PRESSURE rating is present and from closed set
[ ] VERDICT is declared (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED)
[ ] Re-assessment trigger names a concrete threshold

IF CHECKPOINT-INERTIA passes, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
DO NOT emit this gate line until CHECKPOINT-INERTIA passes.

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM
─────────────────────────────────────────────

INPUT REQUIRED: inertia verdict and FLAT-CASE-PRESSURE rating from GATE 1.
DO NOT draw any org boxes until `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===` is present.

DO draw an ASCII hierarchy.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE — DO NOT introduce new role names.

GATE 2 PASS CHECKLIST:
[ ] ASCII diagram shows >= 2 hierarchy levels
[ ] Committees appear as distinct labeled nodes
[ ] All role names appear in ROLES-LOADED or ROLES-NOTE
[ ] No flat list without hierarchy

When the org diagram is complete, emit:
`=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present.

─────────────────────────────────────────────
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
─────────────────────────────────────────────

INPUT REQUIRED: org diagram with typed nodes from GATE 2.
DO NOT begin GATE 3 until `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===` is present.

HEADCOUNT BY AREA

DO produce a headcount table with columns: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single `Decision Scope` column — Decides and Escalates are separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table with columns: `Cadence | Frequency | DRI / Owner | Purpose`
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

COMMITTEE CHARTERS — FIVE FIELDS REQUIRED, PRODUCED IN RHYTHM-CHARTER PAIRS

For each governance meeting row in the rhythm table, produce its charter immediately after that row.
DO NOT batch all rhythm rows first and then all charters — produce each charter immediately after its rhythm row.

Each charter MUST include all five fields:
  Purpose — one sentence
  Membership — list at minimum two roles annotated as `[role name] ([domain type])`
  Decides — decision types owned by this committee
  Escalates — named destination (role title or named committee); DO NOT write "everything not listed under Decides"
  Quorum — in this exact format: `Quorum: [N] of [M] member roles required for binding decisions`
    where N is the minimum required count and M is the total number of roles listed in Membership
    DO NOT use the short `Quorum: [N roles required]` form

GATE 3 CHARTER AUDIT — PER-CHARTER ITERATION REQUIRED

After all rhythm-charter pairs are produced, run CHARTER-FORMAT-AUDIT as a per-charter iteration loop:

  FOR each charter produced (iterate in sequence):
    CHARTER-FORMAT-AUDIT for [charter name]:
    [ ] Quorum field present and matches `N of M member roles` fraction pattern
    [ ] All Membership roles carry `([domain type])` annotation from ROLE-TYPE-CLASSIFICATION closed set
    [ ] All Membership role names appear in GATE 0 typed role list
    [ ] Escalates field names a concrete destination
    [ ] Decides field is populated
    IF any check fails: emit `REJECT: [charter name] — [field] — [failure reason]` and correct before proceeding to next charter.
    IF all checks pass: emit `PROCEED: [charter name] — all fields verified`

After all charters pass CHARTER-FORMAT-AUDIT, verify:
  Pairs produced = governance rows in Operating Rhythm Table (pair-count check).
  Emit: `PAIR-COUNT-VERIFIED: [N] rhythm rows, [N] charters produced.`

When all charters and the pair-count check are complete, emit:
`=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

─────────────────────────────────────────────
ORG-ELEMENT REGISTER — REQUIRED
─────────────────────────────────────────────

DO NOT skip this section.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:

  cat-1 (Areas) — all area names from the Headcount table: `- [area name] — headcount: [N]`
  cat-2 (Committees/Cadences) — all committee and cadence names from Rhythm Table and Charters: `- [name]`
  cat-3 (Headcount) — total headcount: `- Total headcount: [N]`
  cat-4 (DRI Roles) — all DRI role names from Operating Rhythm Table: `- [DRI role]`

─────────────────────────────────────────────
ORG EVOLUTION ROADMAP — REQUIRED
─────────────────────────────────────────────

DO produce a trigger table with columns: `Trigger | Structural Change | Type`
DO NOT label it optional.
DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category — workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.

─────────────────────────────────────────────
ANTI-PATTERN WATCH — TYPED CITATIONS REQUIRED
─────────────────────────────────────────────

DO produce this section after the Org Evolution Roadmap with columns: `Anti-Pattern | Why It Applies Here | Mitigation`
MUST open each `Why It Applies Here` cell with typed citation syntax: `[element name] (cat-N) — [one sentence of specific relevance]`
DO NOT write a cell that names an element without `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.

─────────────────────────────────────────────
SECTION ORDER — INVIOLABLE
─────────────────────────────────────────────

Produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER three-tier constraint applied
3. ROLE-TYPE-CLASSIFICATION
4. GATE 0 PASS CHECKLIST → `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5. Inertia Assessment: STRUCTURING-COST FRAME → mechanism table → FLAT-CASE-CLOSED → How We Coordinate Today → Rebuttal → VERDICT (FLAT-CASE-PRESSURE first)
6. CHECKPOINT-INERTIA → `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7. ASCII Org Diagram → `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
8. Headcount by Area
9. Operating Rhythm Table (interleaved with charters, rhythm row then immediate charter)
10. CHARTER-FORMAT-AUDIT per-charter loop → PAIR-COUNT-VERIFIED → `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
11. ORG-ELEMENT REGISTER
12. Org Evolution Roadmap
13. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-02 — Single axis: CHECKPOINT-0 (preamble consultation enforcement)

**Variation axis:** CHECKPOINT-0 presence — GATE CHAIN block placed as named preamble before GATE 0, with CHECKPOINT-0 as a blocking verification step before GATE 0 execution begins. CHECKPOINT-INERTIA not yet added. Tests whether the preamble + consultation checkpoint pattern alone satisfies C-42.

**Hypothesis:** The GATE CHAIN block placed before GATE 0 as a named ARTIFACT-HANDOFF INVENTORY, combined with a named CHECKPOINT-0 with verbatim FAIL condition, is sufficient to satisfy C-42. The FAIL condition "ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution; FAIL if INVENTORY was not consulted prior to GATE 0 content" converts the preamble from decoration into an enforced precondition.

---

```
You are running `/org-chart {topic}`.

─────────────────────────────────────────────
ARTIFACT-HANDOFF INVENTORY — PREAMBLE (Read before GATE 0 begins)
─────────────────────────────────────────────

This block is a forward-declaring contract. Read it before GATE 0 execution.
DO NOT treat this as a retrospective record. It governs all four gate transitions.

GATE CHAIN — artifact produced by each gate and consumed by the next:

  GATE 0 → GATE 1:  typed role list
    GATE 0 produces: ROLES-LOADED block + ROLE-TYPE-CLASSIFICATION block
    GATE 1 consumes: typed role list (all roles + domain types)

  GATE 1 → GATE 2:  inertia verdict + FLAT-CASE-PRESSURE rating
    GATE 1 produces: VERDICT (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + FLAT-CASE-PRESSURE rating
    GATE 2 consumes: inertia verdict + pressure rating (determines whether structure section runs)

  GATE 2 → GATE 3:  org diagram with typed nodes
    GATE 2 produces: ASCII org diagram using role names from GATE 0
    GATE 3 consumes: org diagram (charter membership references diagram nodes)

  GATE 3 → STATUS:  charter set
    GATE 3 produces: operating rhythm table + committee charters (all five fields)
    STATUS consumes: charter set (pair-count and format verified before STATUS emits)

Each gate may not execute until its upstream artifact is present.
Each gate's STATUS may not emit until its downstream artifact is verified complete.

─────────────────────────────────────────────
CHECKPOINT-0 — BLOCKING VERIFICATION BEFORE GATE 0 EXECUTION
─────────────────────────────────────────────

This checkpoint is a blocking intermediate verification step that must complete before GATE 0 content begins.

CHECKPOINT-0 FAIL CONDITION:
  ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution.
  FAIL if INVENTORY was not consulted prior to GATE 0 content.

CHECKPOINT-0 PASS CHECKLIST:
[ ] ARTIFACT-HANDOFF INVENTORY preamble block is present above this checkpoint
[ ] All four GATE CHAIN transitions are declared (GATE 0→1, 1→2, 2→3, 3→STATUS)
[ ] Each transition names the artifact produced and the artifact consumed
[ ] Preamble was read before GATE 0 content begins

IF CHECKPOINT-0 passes: proceed to GATE 0.
IF CHECKPOINT-0 fails: HALT — do not begin GATE 0 until preamble is present and consulted.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no role files are found.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with one inferred entry per role.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

Classify roles in this strict three-tier order: Engineering types first, then Operations types, then PM / Design / Research / Other types.
If no Engineering roles are present, begin with Operations types.
DO NOT interleave tiers — complete all entries in one tier before writing any entry from the next tier.

ROLE-TYPE-CLASSIFICATION

Produce `ROLE-TYPE-CLASSIFICATION:` immediately after ROLES-LOADED or ROLES-NOTE.
DO assign each role exactly one domain type from: `Engineering / PM / Design / Operations / Research / Other`
Format: `- [role name] — [domain type]`
DO NOT skip this block.
DO NOT proceed until every role is classified.
DO annotate Key Roles cells and Committee Membership fields with `[role name] ([domain type])`.

GATE 0 PASS CHECKLIST:
[ ] CHECKPOINT-0 passed (ARTIFACT-HANDOFF INVENTORY consulted)
[ ] ROLES-LOADED or ROLES-NOTE block present
[ ] ROLE-TYPE-CLASSIFICATION block present, all roles typed
[ ] Three-tier order respected
[ ] No role name introduced later that was not declared here

When all checklist items pass, emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

─────────────────────────────────────────────
GATE 1 — INERTIA ASSESSMENT
─────────────────────────────────────────────

INPUT REQUIRED: typed role list from GATE 0.

INERTIA FIRST — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
Structure in this exact order:
  Sub-section 1 — Case for Staying Flat
  Sub-section 2 — How We Coordinate Today
  Sub-section 3 — Rebuttal
  Sub-section 4 — VERDICT and Re-assessment Trigger

Sub-section 1 — Case for Staying Flat

STRUCTURING-COST FRAME — REQUIRED FIRST ELEMENT

DO emit a named `STRUCTURING-COST FRAME:` block as the FIRST element in Sub-section 1.
DO NOT write mechanism table rows before this frame block is closed.
The frame MUST explicitly enumerate at minimum three overhead categories:
  - Coordination overhead (meeting load per added layer)
  - Decision latency overhead (approval chain vs. direct call)
  - Role boundary overhead (ownership ambiguity at layer transitions)

After the STRUCTURING-COST FRAME block is closed, produce the mechanism table:
  Columns: `Mechanism Name | Type | Frequency / Participants`
  At minimum two data rows.
  Type values: `Channel / Informal Role / Recurring Cadence / Shared Artifact` only.
  DO NOT move mechanism-typed content into Sub-section 2.

After writing the table, count data rows.
IF count < 2: add rows until count reaches 2.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator is present.

Sub-section 2 — How We Coordinate Today

DO inventory coordination patterns in active use.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 — Rebuttal

DO name the coordination failure the flat-team case cannot answer.
DO reference a specific observable (blocked decision, missed SLA, time-zone gap, knowledge silo, competing roadmap).
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT and Re-assessment Trigger

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Choose one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference FLAT-CASE-PRESSURE rating by name.
Write a concrete re-assessment trigger (DO NOT write "revisit as the team grows").

If verdict is `CAN-OPERATE-FLAT`: emit ABSENT block naming what structure is not warranted, then STOP.

GATE 1 PASS CHECKLIST:
[ ] STRUCTURING-COST FRAME present and closed before mechanism table
[ ] Mechanism table has >= 2 data rows with Types from closed vocabulary
[ ] FLAT-CASE-CLOSED separator present
[ ] How We Coordinate Today present and does not re-list Sub-section 1 entries
[ ] Rebuttal names a specific observable failure
[ ] FLAT-CASE-PRESSURE line present and from closed set
[ ] VERDICT declared with reasoning referencing pressure rating
[ ] Re-assessment trigger is concrete (not "revisit as the team grows")

When all pass, emit:
`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM
─────────────────────────────────────────────

INPUT REQUIRED: inertia verdict from GATE 1.
DO NOT draw org boxes until inertia gate is present.

DO draw an ASCII hierarchy (>= 2 levels).
DO show committees as distinct labeled nodes.
DO use only role names from ROLES-LOADED or ROLES-NOTE.

GATE 2 PASS CHECKLIST:
[ ] ASCII diagram >= 2 hierarchy levels
[ ] Committees as distinct nodes
[ ] All role names in ROLES-LOADED or ROLES-NOTE

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

─────────────────────────────────────────────
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
─────────────────────────────────────────────

INPUT REQUIRED: org diagram from GATE 2.

HEADCOUNT BY AREA

Columns: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single Decision Scope column.
DO populate Decides and Escalates as separate fields.
Annotate Key Roles: `[role name] ([domain type])`.
At minimum two area rows + `**Total**` row.

OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three distinct rows: ROB + shiproom/gate + governance.
DO NOT combine rows. DO NOT produce only ROB.
Reference a role from ROLES-LOADED in DRI / Owner where possible.

COMMITTEE CHARTERS — RHYTHM-CHARTER PAIRS

Produce each charter immediately after its rhythm row.
DO NOT batch all rhythm rows, then all charters.

Each charter: Purpose, Membership (`[role name] ([domain type])`, >= 2 roles), Decides, Escalates (named destination), Quorum (`N of M member roles required for binding decisions`).

CHARTER-FORMAT-AUDIT — PER-CHARTER ITERATION:

  FOR each charter (iterate in sequence):
    [ ] Quorum matches `N of M member roles` fraction pattern
    [ ] All Membership roles carry `([domain type])` from closed set
    [ ] All Membership role names appear in GATE 0 typed role list
    [ ] Escalates names a concrete destination
    [ ] Decides is populated
    REJECT: [charter name] — [field] — [failure] (if any check fails; correct before next charter)
    PROCEED: [charter name] — all fields verified (if all pass)

Pair-count check: emit `PAIR-COUNT-VERIFIED: [N] rhythm rows, [N] charters.`

When all charters and pair-count verified, emit:
`=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

─────────────────────────────────────────────
ORG-ELEMENT REGISTER
─────────────────────────────────────────────

  cat-1 (Areas): all area names from Headcount table — `- [area name] — headcount: [N]`
  cat-2 (Committees/Cadences): all names from Rhythm Table + Charters — `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): all DRI roles from Rhythm Table — `- [DRI role]`

─────────────────────────────────────────────
ORG EVOLUTION ROADMAP
─────────────────────────────────────────────

Columns: `Trigger | Structural Change | Type`
At minimum two rows: Row 1 headcount threshold; Row 2 different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

─────────────────────────────────────────────
ANTI-PATTERN WATCH
─────────────────────────────────────────────

Columns: `Anti-Pattern | Why It Applies Here | Mitigation`
Open each Why It Applies Here cell: `[element name] (cat-N) — [one sentence]`
DO NOT omit `(cat-N)` typed syntax. cat-N must match ORG-ELEMENT REGISTER categories.
At minimum two rows.

─────────────────────────────────────────────
SECTION ORDER
─────────────────────────────────────────────

1. ARTIFACT-HANDOFF INVENTORY (preamble, before GATE 0)
2. CHECKPOINT-0 (blocking verification before GATE 0 execution)
3. ROLES-LOADED or ROLES-NOTE → ROLE-LOAD-ORDER → ROLE-TYPE-CLASSIFICATION
4. GATE 0 PASS CHECKLIST → gate line
5. STRUCTURING-COST FRAME → mechanism table → FLAT-CASE-CLOSED → How We Coordinate Today → Rebuttal → VERDICT
6. GATE 1 PASS CHECKLIST → gate line
7. ASCII Org Diagram → gate line
8. Headcount by Area
9. Operating Rhythm Table (interleaved with charters)
10. CHARTER-FORMAT-AUDIT loop → PAIR-COUNT-VERIFIED → gate line
11. ORG-ELEMENT REGISTER
12. Org Evolution Roadmap
13. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-03 — Combined axis: both checkpoints in explicit blocking form

**Variation axis:** Both CHECKPOINT-0 and CHECKPOINT-INERTIA present, each with full named FAIL conditions. Phrasing register: imperative with DO/DO NOT vocabulary. Tests whether both new criteria are satisfied when both checkpoints co-exist in minimal blocking form, without the full positional chain reinforcement at declaration level beyond what the checkpoints themselves state.

**Hypothesis:** The combination of CHECKPOINT-0 (blocking GATE 0 until INVENTORY is consulted) and CHECKPOINT-INERTIA (blocking GATE 1 STATUS until STRUCTURING-COST FRAME precedes mechanism rows) satisfies both C-41 and C-42 simultaneously. The checkpoint names, FAIL condition text, and blocking position are sufficient without additional declaration-level reinforcement.

---

```
You are running `/org-chart {topic}`.

─────────────────────────────────────────────
ARTIFACT-HANDOFF INVENTORY — PREAMBLE
─────────────────────────────────────────────

This is a forward-declaring contract. It governs all four gate transitions.
Read this block before GATE 0 execution begins.
DO NOT treat it as a retrospective record encountered after gates have executed.

GATE CHAIN:
  GATE 0 → GATE 1:  typed role list (ROLES-LOADED + ROLE-TYPE-CLASSIFICATION)
  GATE 1 → GATE 2:  inertia verdict (VERDICT declaration + FLAT-CASE-PRESSURE rating)
  GATE 2 → GATE 3:  org diagram (ASCII hierarchy with typed node names)
  GATE 3 → STATUS:  charter set (all rhythm-charter pairs, pair-count verified)

Each gate requires its upstream artifact before execution.
Each gate STATUS requires its downstream artifact verified before emission.

─────────────────────────────────────────────
CHECKPOINT-0
─────────────────────────────────────────────

BLOCKING STEP — executes before GATE 0 content. GATE 0 may not begin until this checkpoint passes.

FAIL CONDITION:
  ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution.
  FAIL if INVENTORY was not consulted prior to GATE 0 content.

CHECKPOINT-0 VERIFICATION:
[ ] ARTIFACT-HANDOFF INVENTORY block appears above this checkpoint
[ ] All four GATE CHAIN transitions are declared with named artifacts
[ ] Preamble has been read before GATE 0 content begins
[ ] No GATE 0 content has been produced before this checkpoint passes

PROCEED to GATE 0 when all items checked. HALT if any item fails.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

DO check `.craft/roles/` before writing anything.
Produce `ROLES-LOADED:` block: `- [role name] — [description]` per role.
If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred entries.
DO NOT write any section until this block exists.

ROLE-LOAD-ORDER:
  Tier 1: Engineering types
  Tier 2: Operations types
  Tier 3: PM / Design / Research / Other types
  Complete each tier before beginning the next. DO NOT interleave.

Immediately after ROLES-LOADED, produce `ROLE-TYPE-CLASSIFICATION:`:
  Format: `- [role name] — [domain type]`
  Domain types (closed set): `Engineering / PM / Design / Operations / Research / Other`
  Classify every role. DO NOT skip any.

Annotation requirement: All Key Roles cells → `[role name] ([domain type])`. All Membership fields → same format.

GATE 0 DO:
  DO produce ROLES-LOADED or ROLES-NOTE
  DO produce ROLE-TYPE-CLASSIFICATION immediately after
  DO apply three-tier order

GATE 0 DO NOT:
  DO NOT invent role names if roles files exist
  DO NOT skip ROLE-TYPE-CLASSIFICATION
  DO NOT introduce role names later that were not declared here
  DO NOT proceed to GATE 1 without all roles typed

GATE 0 STATUS:
[ ] CHECKPOINT-0 passed
[ ] ROLES-LOADED or ROLES-NOTE present
[ ] ROLE-TYPE-CLASSIFICATION present, all roles typed, three-tier order respected

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

─────────────────────────────────────────────
GATE 1 — INERTIA ASSESSMENT
─────────────────────────────────────────────

INPUT: typed role list from GATE 0.
DO NOT begin before GATE 0 STATUS gate line is present.

GATE 1 DO:
  DO write Inertia Assessment before any org boxes
  DO produce STRUCTURING-COST FRAME as the first element in Sub-section 1
  DO position STRUCTURING-COST FRAME before mechanism table rows
  DO structure in exact order: Sub-section 1 / 2 / 3 / 4

GATE 1 DO NOT:
  DO NOT write an org diagram before the Inertia Assessment
  DO NOT write mechanism table rows before STRUCTURING-COST FRAME block is closed
  DO NOT begin Sub-section 2 before FLAT-CASE-CLOSED separator is present
  DO NOT emit GATE 1 STATUS before CHECKPOINT-INERTIA passes

Sub-section 1 — Case for Staying Flat

STRUCTURING-COST FRAME (REQUIRED — FIRST ELEMENT):
  Emit a named block: `STRUCTURING-COST FRAME:`
  Enumerate at minimum three overhead categories:
    - Coordination overhead
    - Decision latency overhead
    - Role boundary overhead
  Close the frame block before writing mechanism table rows.
  The frame is the interpretive lens through which mechanism rows are read.

  AFTER frame block is closed — produce mechanism evidence table:
    Columns: `Mechanism Name | Type | Frequency / Participants`
    At minimum two data rows.
    Type values (closed): `Channel / Informal Role / Recurring Cadence / Shared Artifact`
    DO NOT move mechanism-typed content to Sub-section 2.

  After table, count data rows:
    IF count < 2: add rows until count >= 2.
    Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
    DO NOT emit before count >= 2.
    DO NOT begin Sub-section 2 before separator present.

Sub-section 2 — How We Coordinate Today

  Inventory coordination patterns in active use.
  Name channels, cadences, informal roles, and artifacts with frequency and participants.
  DO NOT re-list Sub-section 1 table entries.

Sub-section 3 — Rebuttal

  Name the coordination failure the flat-team case cannot answer.
  Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
  DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT and Re-assessment Trigger

  Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
  Rating (closed set): `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
  DO NOT omit this line. DO NOT emit VERDICT before it.

  Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`
  Reasoning MUST reference FLAT-CASE-PRESSURE rating by name.
  Write concrete re-assessment trigger. DO NOT write "revisit as the team grows."

  If `CAN-OPERATE-FLAT`: emit ABSENT block, then STOP — no further content.

─────────────────────────────────────────────
CHECKPOINT-INERTIA
─────────────────────────────────────────────

BLOCKING STEP — executes after GATE 1 content, before GATE 1 STATUS. GATE 1 STATUS may not emit until this checkpoint passes.

FAIL CONDITION:
  STRUCTURING-COST FRAME must precede mechanism table rows in output produced.
  FAIL if any mechanism row appears before the STRUCTURING-COST FRAME block is closed.

CHECKPOINT-INERTIA VERIFICATION:
[ ] STRUCTURING-COST FRAME block is present in produced output
[ ] STRUCTURING-COST FRAME block is closed before first mechanism table row in produced output
[ ] No mechanism row appears before STRUCTURING-COST FRAME block close
[ ] Mechanism table has >= 2 data rows
[ ] Types column draws only from closed vocabulary
[ ] FLAT-CASE-CLOSED separator present
[ ] FLAT-CASE-PRESSURE rating present and from closed set
[ ] VERDICT declared
[ ] Re-assessment trigger is concrete

PROCEED to GATE 1 STATUS when all items checked. HALT if FAIL condition triggered.

GATE 1 STATUS:
When CHECKPOINT-INERTIA passes, emit:
`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM
─────────────────────────────────────────────

INPUT: inertia verdict from GATE 1.
DO NOT draw org boxes before GATE 1 STATUS gate line is present.

GATE 2 DO:
  DO draw ASCII hierarchy (>= 2 levels)
  DO show committees as distinct labeled nodes
  DO use only role names from ROLES-LOADED or ROLES-NOTE

GATE 2 DO NOT:
  DO NOT produce flat list of names without hierarchy
  DO NOT introduce new role names
  DO NOT embed committees inside an area without their own labeled node

GATE 2 STATUS:
[ ] ASCII diagram >= 2 levels
[ ] Committees as distinct nodes
[ ] Role names match GATE 0 typed role list

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

─────────────────────────────────────────────
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
─────────────────────────────────────────────

INPUT: org diagram from GATE 2.
DO NOT begin before GATE 2 STATUS gate line is present.

GATE 3 DO:
  DO produce Headcount table with split Decides/Escalates columns
  DO produce Rhythm table with >= 3 distinct rows
  DO produce charters as rhythm-charter pairs (each charter immediately after its rhythm row)
  DO run CHARTER-FORMAT-AUDIT loop per charter

GATE 3 DO NOT:
  DO NOT use single Decision Scope column
  DO NOT batch all rhythm rows then all charters
  DO NOT combine two meetings into one rhythm row
  DO NOT omit any charter for any governance rhythm row
  DO NOT emit GATE 3 STATUS before CHARTER-FORMAT-AUDIT loop completes

HEADCOUNT BY AREA

Columns: `Area | Headcount | Key Roles | Decides | Escalates`
Key Roles annotated: `[role name] ([domain type])`.
At minimum two area rows + `**Total**` row.
Decides: decision types owned at this level.
Escalates: decision types referred upward, naming destination.

OPERATING RHYTHM TABLE + CHARTERS (INTERLEAVED)

Rhythm table columns: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: ROB + shiproom or gate + governance meeting.
DRI / Owner references a role from ROLES-LOADED where possible.

For each governance row, produce its charter immediately:
  Purpose (one sentence)
  Membership (>= 2 roles, `[role name] ([domain type])`)
  Decides
  Escalates (named destination, not "everything not listed under Decides")
  Quorum: `Quorum: [N] of [M] member roles required for binding decisions`

CHARTER-FORMAT-AUDIT LOOP:

  FOR each charter (iterate in sequence, do not skip):
    CHARTER-FORMAT-AUDIT [charter name]:
    [ ] Quorum: matches `N of M member roles required for binding decisions` exactly
    [ ] Membership: all roles carry `([domain type])` from ROLE-TYPE-CLASSIFICATION closed set
    [ ] Membership: all role names present in GATE 0 typed role list
    [ ] Escalates: names concrete destination (not blank, TBD, or circular)
    [ ] Decides: populated with decision types
    IF any check fails: REJECT: [charter name] — [field] — [reason] — correct and re-check.
    IF all pass: PROCEED: [charter name] — all fields verified.

  After loop: `PAIR-COUNT-VERIFIED: [N] rhythm rows, [N] charters produced.`

GATE 3 STATUS:
[ ] CHARTER-FORMAT-AUDIT loop complete (all charters PROCEED)
[ ] PAIR-COUNT-VERIFIED emitted

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

─────────────────────────────────────────────
ORG-ELEMENT REGISTER
─────────────────────────────────────────────

  cat-1 (Areas): `- [area name] — headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

─────────────────────────────────────────────
ORG EVOLUTION ROADMAP
─────────────────────────────────────────────

Columns: `Trigger | Structural Change | Type`
Row 1: headcount threshold.
Row 2: different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

─────────────────────────────────────────────
ANTI-PATTERN WATCH
─────────────────────────────────────────────

Columns: `Anti-Pattern | Why It Applies Here | Mitigation`
Each Why It Applies Here cell opens: `[element name] (cat-N) — [one sentence]`
cat-N must match ORG-ELEMENT REGISTER category schema.
At minimum two rows.

─────────────────────────────────────────────
SECTION ORDER
─────────────────────────────────────────────

1. ARTIFACT-HANDOFF INVENTORY (preamble)
2. CHECKPOINT-0 (blocking before GATE 0)
3. GATE 0: ROLES-LOADED → ROLE-TYPE-CLASSIFICATION → STATUS gate line
4. GATE 1: STRUCTURING-COST FRAME → mechanism table → FLAT-CASE-CLOSED → Sub-section 2 → Sub-section 3 → Sub-section 4 (FLAT-CASE-PRESSURE first) → CHECKPOINT-INERTIA → STATUS gate line
5. GATE 2: ASCII Org Diagram → STATUS gate line
6. GATE 3: Headcount → Rhythm+Charters (interleaved) → CHARTER-FORMAT-AUDIT → PAIR-COUNT-VERIFIED → STATUS gate line
7. ORG-ELEMENT REGISTER
8. Org Evolution Roadmap
9. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-04 — Combined axis: both checkpoints + positional chain at declaration AND enforcement level

**Variation axis:** Both checkpoints present with full FAIL conditions; additionally, both positional constraints are declared at instruction scope (DO NOT guard, named boundary, prohibited form, causal explanation) AND enforced at checkpoint scope. Tests whether declaration-level reinforcement beyond the checkpoints themselves improves output compliance.

**Hypothesis:** Stating the positional constraint at TWO levels — a DO NOT guard at instruction scope naming the prohibited form and causal explanation, AND a CHECKPOINT with FAIL condition at enforcement scope — creates double binding that eliminates ambiguity about where the STRUCTURING-COST FRAME and GATE CHAIN preamble must appear. The declaration-level rule names the "why" (frame as premise vs. conclusion; preamble as forward-declaring contract vs. retrospective record); the checkpoint enforces the "what" (FAIL if frame appears after mechanism rows; FAIL if inventory not consulted before GATE 0).

---

```
You are running `/org-chart {topic}`.

─────────────────────────────────────────────
ARTIFACT-HANDOFF INVENTORY — PREAMBLE
─────────────────────────────────────────────

This block is a forward-declaring contract. It must be read before GATE 0 execution begins.
DO NOT treat this as a retrospective inventory encountered after gates have completed.
REASON: A post-execution inventory is read too late to govern any gate. A preamble inventory is consulted before execution and changes what each gate checks before proceeding.

GATE CHAIN — four transitions, each naming the artifact produced and consumed:

  GATE 0 → GATE 1:
    Produces: typed role list (ROLES-LOADED block + ROLE-TYPE-CLASSIFICATION block)
    Consumes at GATE 1: typed role list with all role names and domain types

  GATE 1 → GATE 2:
    Produces: inertia verdict + FLAT-CASE-PRESSURE rating
    Consumes at GATE 2: VERDICT declaration (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + pressure rating

  GATE 2 → GATE 3:
    Produces: ASCII org diagram with typed node names
    Consumes at GATE 3: org diagram (charter Membership references diagram node names)

  GATE 3 → STATUS:
    Produces: charter set (rhythm-charter pairs, all five fields, pair-count verified)
    Consumes at STATUS: complete charter set (format verified by CHARTER-FORMAT-AUDIT loop)

Each gate may not begin until its upstream artifact is present in output.
Each gate STATUS may not emit until its downstream artifact is verified by the gate's blocking checkpoint.

─────────────────────────────────────────────
CHECKPOINT-0 — BLOCKING BEFORE GATE 0
─────────────────────────────────────────────

This is a blocking intermediate verification step. It precedes GATE 0 content.
GATE 0 content may not begin until CHECKPOINT-0 passes.

FAIL CONDITION:
  ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution.
  FAIL if INVENTORY was not consulted prior to GATE 0 content.

CHECKPOINT-0 PASS:
[ ] ARTIFACT-HANDOFF INVENTORY preamble block appears above this checkpoint
[ ] All four GATE CHAIN transitions declared with named produce/consume artifacts
[ ] No GATE 0 content exists before this checkpoint

PROCEED to GATE 0 when all checked. HALT if FAIL condition triggered.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

PREREQUISITE: CHECKPOINT-0 passed.

DO check `.craft/roles/` before writing anything.
Produce `ROLES-LOADED:` block: `- [role name] — [description]` per role.
If no files: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred entries.
DO NOT write any section before this block.

ROLE-LOAD-ORDER (three-tier):
  Tier 1 — Engineering types (complete before beginning Tier 2)
  Tier 2 — Operations types (complete before beginning Tier 3)
  Tier 3 — PM / Design / Research / Other types
  DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION (immediately after ROLES-LOADED):
  Format: `- [role name] — [domain type]`
  Closed set: `Engineering / PM / Design / Operations / Research / Other`
  Classify every role. Do not skip any.

Annotation: Key Roles cells and Membership fields → `[role name] ([domain type])`.

GATE 0 DO / DO NOT:
  DO: produce ROLES-LOADED, produce ROLE-TYPE-CLASSIFICATION immediately after, apply three-tier order
  DO NOT: invent roles if files exist; skip classification; introduce role names later not declared here

GATE 0 STATUS checklist:
[ ] CHECKPOINT-0 passed
[ ] ROLES-LOADED or ROLES-NOTE present
[ ] ROLE-TYPE-CLASSIFICATION immediately after; all roles typed; three-tier order respected
[ ] No undeclared role names in any downstream section

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

─────────────────────────────────────────────
GATE 1 — INERTIA ASSESSMENT
─────────────────────────────────────────────

INPUT: typed role list from GATE 0.
PREREQUISITE: GATE 0 STATUS gate line present in output.

GATE 1 POSITIONAL CONSTRAINT — DO NOT GUARD:
  DO NOT begin Step 1.1 (Sub-section 1 — Case for Staying Flat) with mechanism table rows.
  PROHIBITED FORM: mechanism table rows appearing before STRUCTURING-COST FRAME block is closed.
  REASON: When mechanism rows precede the frame, the frame becomes a cost-summary derived from rows already written — the overhead is a conclusion, not a premise. The STRUCTURING-COST FRAME must serve as the interpretive lens through which each mechanism row is read, which requires it to be present before any row is written.

GATE 1 DO / DO NOT:
  DO: write Inertia Assessment before any org boxes
  DO: emit STRUCTURING-COST FRAME as the FIRST named element in Sub-section 1 (Step 1.1 boundary)
  DO: close STRUCTURING-COST FRAME before writing any mechanism table row
  DO NOT: write mechanism table rows before STRUCTURING-COST FRAME block is closed (GATE 1 POSITIONAL CONSTRAINT)
  DO NOT: draw org diagrams before GATE 1 STATUS emits
  DO NOT: emit GATE 1 STATUS before CHECKPOINT-INERTIA passes

INERTIA STRUCTURE — four sub-sections in exact order:

Sub-section 1 — Case for Staying Flat (Step 1.1)

  STRUCTURING-COST FRAME (REQUIRED FIRST — Step 1.1 boundary):
    Named block: `STRUCTURING-COST FRAME:`
    Enumerate at minimum three overhead categories imposed by formal structure:
      - Coordination overhead (recurring meeting load per added reporting layer)
      - Decision latency overhead (approval chain delay vs. direct call)
      - Role boundary overhead (ownership ambiguity at layer transitions)
    Close this block. All overhead categories must be enumerated and closed before mechanism table begins.

  MECHANISM TABLE (after STRUCTURING-COST FRAME block is closed):
    Columns: `Mechanism Name | Type | Frequency / Participants`
    At minimum two data rows.
    Type (closed): `Channel / Informal Role / Recurring Cadence / Shared Artifact`
    DO NOT use Type values outside this vocabulary.
    DO NOT move mechanism-typed content to Sub-section 2.

  Row count check: if count < 2, add rows until count >= 2.
  Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
  DO NOT emit before count >= 2. DO NOT begin Sub-section 2 before separator.

Sub-section 2 — How We Coordinate Today
  Inventory coordination patterns in active use.
  Name channels, cadences, informal roles, artifacts with frequency and participants.
  DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal
  Name the coordination failure flat-team case cannot answer.
  Reference specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
  DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT and Re-assessment Trigger
  Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
  Rating (closed set): `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
  DO NOT omit this line. DO NOT emit VERDICT before it is present.
  Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`
  Reasoning references FLAT-CASE-PRESSURE by name.
  Concrete re-assessment trigger (DO NOT write "revisit as the team grows").
  If `CAN-OPERATE-FLAT`: emit ABSENT block, then STOP.

─────────────────────────────────────────────
CHECKPOINT-INERTIA — BLOCKING BEFORE GATE 1 STATUS
─────────────────────────────────────────────

This is a blocking intermediate verification step between GATE 1 content production and GATE 1 STATUS emission.
GATE 1 STATUS may not emit until CHECKPOINT-INERTIA passes.

FAIL CONDITION:
  STRUCTURING-COST FRAME must precede mechanism table rows in output produced.
  FAIL if any mechanism row appears before the STRUCTURING-COST FRAME block is closed.

CHECKPOINT-INERTIA VERIFICATION:
[ ] STRUCTURING-COST FRAME block present in produced output
[ ] STRUCTURING-COST FRAME block closed before first mechanism table row in produced output — if any mechanism row precedes frame close: FAIL
[ ] Mechanism table has >= 2 data rows
[ ] Type column draws only from closed vocabulary
[ ] FLAT-CASE-CLOSED separator present
[ ] FLAT-CASE-PRESSURE line present, rating from closed set
[ ] VERDICT declared; reasoning references FLAT-CASE-PRESSURE by name
[ ] Re-assessment trigger is concrete

PROCEED to GATE 1 STATUS when all verified. HALT if FAIL condition triggered.

GATE 1 STATUS:
Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM
─────────────────────────────────────────────

INPUT: inertia verdict from GATE 1.
PREREQUISITE: GATE 1 STATUS gate line present.

GATE 2 DO / DO NOT:
  DO: draw ASCII hierarchy (>= 2 levels); show committees as distinct labeled nodes; use role names from ROLES-LOADED only
  DO NOT: produce flat list without hierarchy; introduce new role names; embed committees inside an area node

GATE 2 STATUS:
[ ] ASCII diagram >= 2 hierarchy levels
[ ] Committees as distinct nodes
[ ] Role names match GATE 0 typed role list

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

─────────────────────────────────────────────
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
─────────────────────────────────────────────

INPUT: org diagram from GATE 2.
PREREQUISITE: GATE 2 STATUS gate line present.

GATE 3 DO / DO NOT:
  DO: split Decides/Escalates; annotate Key Roles; produce rhythm-charter pairs interleaved; run CHARTER-FORMAT-AUDIT loop
  DO NOT: merge Decides/Escalates into single column; batch all rhythm rows then all charters; omit charter for any governance row; emit GATE 3 STATUS before CHARTER-FORMAT-AUDIT loop completes

HEADCOUNT BY AREA:
  Columns: `Area | Headcount | Key Roles | Decides | Escalates`
  Key Roles: `[role name] ([domain type])`
  >= 2 area rows + **Total** row
  Decides: owned decision types. Escalates: referred decisions, naming destination.
  DO NOT write "owns the area."

OPERATING RHYTHM TABLE + COMMITTEE CHARTERS (rhythm-charter pairs):
  Rhythm columns: `Cadence | Frequency | DRI / Owner | Purpose`
  >= 3 distinct rows: ROB + shiproom/gate + governance
  DRI / Owner references ROLES-LOADED role where possible.

  For each governance row, immediately produce its charter:
    Purpose (one sentence)
    Membership (>= 2 roles, `[role name] ([domain type])`)
    Decides (decision types)
    Escalates (named destination — not "everything not listed")
    Quorum: `Quorum: [N] of [M] member roles required for binding decisions` (fraction form required; short form prohibited)

CHARTER-FORMAT-AUDIT LOOP:
  FOR each charter in sequence:
    CHARTER-FORMAT-AUDIT [charter name]:
    [ ] Quorum matches `N of M member roles required for binding decisions`
    [ ] All Membership roles carry `([domain type])` from closed set
    [ ] All Membership role names exist in GATE 0 typed role list
    [ ] Escalates: concrete destination
    [ ] Decides: populated
    IF fail: REJECT: [charter] — [field] — [reason] — correct and re-audit.
    IF pass: PROCEED: [charter] — all fields verified.

  After loop: `PAIR-COUNT-VERIFIED: [N] rhythm rows, [N] charters.`

GATE 3 STATUS:
[ ] CHARTER-FORMAT-AUDIT loop complete; all charters PROCEED
[ ] PAIR-COUNT-VERIFIED present

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

─────────────────────────────────────────────
ORG-ELEMENT REGISTER
─────────────────────────────────────────────

  cat-1 (Areas): `- [area name] — headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

─────────────────────────────────────────────
ORG EVOLUTION ROADMAP
─────────────────────────────────────────────

Columns: `Trigger | Structural Change | Type`
Row 1: headcount threshold trigger.
Row 2: different category — workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

─────────────────────────────────────────────
ANTI-PATTERN WATCH
─────────────────────────────────────────────

Columns: `Anti-Pattern | Why It Applies Here | Mitigation`
Each Why It Applies Here opens: `[element name] (cat-N) — [one sentence of specific relevance]`
cat-N must match ORG-ELEMENT REGISTER category schema. No freeform category codes.
>= 2 rows.

─────────────────────────────────────────────
SECTION ORDER — INVIOLABLE
─────────────────────────────────────────────

1. ARTIFACT-HANDOFF INVENTORY (preamble — before any gate)
2. CHECKPOINT-0 (blocking before GATE 0)
3. GATE 0: ROLES-LOADED → ROLE-TYPE-CLASSIFICATION → STATUS
4. GATE 1: STRUCTURING-COST FRAME (Step 1.1 first element) → mechanism table → FLAT-CASE-CLOSED → Sub-section 2 → Sub-section 3 → Sub-section 4 (FLAT-CASE-PRESSURE first) → CHECKPOINT-INERTIA → STATUS
5. GATE 2: ASCII Org Diagram → STATUS
6. GATE 3: Headcount → Rhythm+Charters interleaved → CHARTER-FORMAT-AUDIT loop → PAIR-COUNT-VERIFIED → STATUS
7. ORG-ELEMENT REGISTER
8. Org Evolution Roadmap
9. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-05 — Maximum integration: full blocking chain with atomic gate structure and explicit subsumption

**Variation axis:** Full integration of all deepening chains — ARTIFACT-HANDOFF INVENTORY as explicit preamble document, CHECKPOINT-0 as enforced precondition naming the inventory document, STRUCTURING-COST FRAME at step-embedded position with DO NOT guard and causal explanation, CHECKPOINT-INERTIA as named blocking step with verbatim FAIL condition, all gates with atomic DO/DO NOT + checkbox + blocking-step structure. Per-charter audit loop with per-charter role-continuity integrated into the same iteration. Each checkpoint names its specific deepening target and references the criterion it closes.

**Hypothesis:** The maximum integration form — where every enforcement mechanism is present, every positional constraint is declared at instruction scope AND verified at checkpoint scope, and the full gate chain is both declared as preamble and enforced via CHECKPOINT-0 — satisfies C-41 and C-42 simultaneously while preserving all C-01 through C-40 compliance via the subsumption property: satisfying C-41 necessarily satisfies C-39 and C-37; satisfying C-42 necessarily satisfies C-40 and C-38.

---

```
You are running `/org-chart {topic}`.

═══════════════════════════════════════════════
ARTIFACT-HANDOFF INVENTORY — PREAMBLE
(Forward-declaring contract: read before GATE 0 begins)
═══════════════════════════════════════════════

This block declares the complete artifact dependency graph for all four gate transitions.
Position: preamble — before GATE 0 execution.
Form: forward-declaring contract.
Prohibited form: a retrospective record appended after GATE 3 completes.
REASON: A post-GATE 3 inventory is encountered after all gates have executed and cannot govern any gate's precondition. A preamble inventory is read before execution begins and makes each gate's artifact prerequisite checkable at the moment the gate executes.

GATE CHAIN — artifact produced → artifact consumed:

  GATE 0:
    Produces → typed role list
    Artifact: ROLES-LOADED block (all role names + descriptions) + ROLE-TYPE-CLASSIFICATION block (all roles + domain types in three-tier order)

  GATE 0 → GATE 1:
    GATE 1 consumes: typed role list
    Prerequisite: ROLES-LOADED or ROLES-NOTE present; ROLE-TYPE-CLASSIFICATION present; all roles typed

  GATE 1:
    Produces → inertia verdict
    Artifact: VERDICT declaration (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + FLAT-CASE-PRESSURE rating + re-assessment trigger

  GATE 1 → GATE 2:
    GATE 2 consumes: inertia verdict
    Prerequisite: VERDICT declaration present; FLAT-CASE-PRESSURE rating present and from closed set

  GATE 2:
    Produces → org diagram
    Artifact: ASCII hierarchy (>= 2 levels, committees as distinct nodes, role names from GATE 0)

  GATE 2 → GATE 3:
    GATE 3 consumes: org diagram
    Prerequisite: ASCII diagram present; committees as distinct nodes; role names match GATE 0 list

  GATE 3:
    Produces → charter set
    Artifact: operating rhythm table + committee charters (all five fields, rhythm-charter pairs, PAIR-COUNT-VERIFIED)

  GATE 3 → STATUS:
    STATUS consumes: charter set
    Prerequisite: CHARTER-FORMAT-AUDIT loop complete; PAIR-COUNT-VERIFIED present

═══════════════════════════════════════════════
CHECKPOINT-0 — BLOCKING BEFORE GATE 0 EXECUTION
═══════════════════════════════════════════════

This checkpoint is a blocking intermediate verification step.
It precedes GATE 0 content. GATE 0 may not execute before this checkpoint passes.

FAIL CONDITION:
  ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution.
  FAIL if INVENTORY was not consulted prior to GATE 0 content.

CHECKPOINT-0 VERIFICATION:
[ ] ARTIFACT-HANDOFF INVENTORY preamble block exists above this checkpoint
[ ] All four gate transitions declared (GATE 0→1, 1→2, 2→3, 3→STATUS)
[ ] Each transition names: artifact produced by upstream gate + artifact consumed by downstream gate
[ ] Preamble has been read; no GATE 0 content exists before this checkpoint

PROCEED to GATE 0 if all items checked.
HALT and do not execute GATE 0 if FAIL condition triggered.

═══════════════════════════════════════════════
GATE 0 — ROLES AND CLASSIFICATION
═══════════════════════════════════════════════

PREREQUISITE: CHECKPOINT-0 passed (ARTIFACT-HANDOFF INVENTORY consulted).

─── GATE 0 DO / DO NOT ───────────────────────
DO:
  - Check `.craft/roles/` before writing any content
  - Produce ROLES-LOADED block: `- [role name] — [one-line description]` per role
  - If no files found: produce ROLES-NOTE instead
  - Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE
  - Apply three-tier classification order: Engineering → Operations → PM/Design/Research/Other
  - Annotate all Key Roles cells and Membership fields: `[role name] ([domain type])`

DO NOT:
  - Invent role names if .craft/roles/ files exist
  - Skip ROLE-TYPE-CLASSIFICATION for any role
  - Interleave classification tiers
  - Write any other section before ROLES-LOADED or ROLES-NOTE block exists
  - Introduce role names in any downstream section not declared here

─── GATE 0 BLOCKING VERIFICATION ────────────
[ ] CHECKPOINT-0 passed (preamble consulted)
[ ] ROLES-LOADED or ROLES-NOTE block present
[ ] ROLE-TYPE-CLASSIFICATION block present, immediately following ROLES-LOADED or ROLES-NOTE
[ ] All roles typed from closed set: Engineering / PM / Design / Operations / Research / Other
[ ] Three-tier order respected (Engineering complete → Operations complete → remaining)
[ ] No undeclared role names will appear in downstream sections

─── GATE 0 STATUS ────────────────────────────
Emit when all verification items checked:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
Do not emit before all items pass.

═══════════════════════════════════════════════
GATE 1 — INERTIA ASSESSMENT
═══════════════════════════════════════════════

INPUT: typed role list (GATE 0 artifact).
PREREQUISITE: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===` present in output.

─── GATE 1 POSITIONAL CONSTRAINT (Step 1.1 boundary) ────────────
DO NOT begin Sub-section 1 mechanism table rows before STRUCTURING-COST FRAME block is closed.
PROHIBITED FORM: mechanism table rows appearing before STRUCTURING-COST FRAME block close.
REASON: When mechanism rows precede the frame, the frame becomes a cost-summary derived from rows already written — overhead as conclusion, not premise. The STRUCTURING-COST FRAME serves as the interpretive lens for each mechanism row; it must be written first so the overhead categories are established before any row is read.

─── GATE 1 DO / DO NOT ───────────────────────
DO:
  - Write Inertia Assessment before any org boxes
  - Emit STRUCTURING-COST FRAME as the first named element in Sub-section 1
  - Close STRUCTURING-COST FRAME before writing any mechanism table row
  - Structure in exact order: Sub-section 1 / Sub-section 2 / Sub-section 3 / Sub-section 4
  - Open Sub-section 4 with FLAT-CASE-PRESSURE line before VERDICT declaration
  - Write concrete re-assessment trigger (not "revisit as the team grows")

DO NOT:
  - Write mechanism table rows before STRUCTURING-COST FRAME block is closed [GATE 1 POSITIONAL CONSTRAINT]
  - Draw org diagrams before GATE 1 STATUS emits
  - Move mechanism-typed content into Sub-section 2
  - Emit VERDICT before FLAT-CASE-PRESSURE line is present
  - Emit GATE 1 STATUS before CHECKPOINT-INERTIA passes

─── SUB-SECTION 1 — Case for Staying Flat ────

STRUCTURING-COST FRAME (Step 1.1 first element — REQUIRED BEFORE MECHANISM TABLE):

  Emit named block: `STRUCTURING-COST FRAME:`
  Enumerate at minimum three overhead categories imposed by formal structure:
    - Coordination overhead: recurring meeting load per reporting layer added
    - Decision latency overhead: approval chain delay relative to direct call
    - Role boundary overhead: ownership ambiguity at layer transitions, duplicated escalation paths
  Close this block. Every overhead category must be enumerated before the block closes.
  The closed frame establishes interpretive categories through which each mechanism row is read.

  NET-COST-COMPARISON (after STRUCTURING-COST FRAME, before mechanism table rows):
    Produce a brief comparison table or two-line statement placing inertia costs alongside restructuring costs.
    This is a symmetric cost view: flat-team overhead vs. formal-structure overhead.

  MECHANISM EVIDENCE TABLE (after STRUCTURING-COST FRAME is closed):
    Columns: `Mechanism Name | Type | Frequency / Participants`
    At minimum two data rows.
    Type (closed vocabulary): `Channel / Informal Role / Recurring Cadence / Shared Artifact`
    DO NOT use Type values outside this vocabulary.
    DO NOT move mechanism-typed content into Sub-section 2.

    After table: count data rows (header excluded).
    IF count < 2: add missing rows until count >= 2.
    Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
    DO NOT emit before count >= 2. DO NOT begin Sub-section 2 before separator present.

─── SUB-SECTION 2 — How We Coordinate Today ──
  Inventory coordination patterns in active use.
  Name channels, cadences, informal roles, artifacts with frequency and participants.
  DO NOT re-list Sub-section 1 table entries.

─── SUB-SECTION 3 — Rebuttal ─────────────────
  Name the coordination failure the flat-team case and current mechanisms cannot answer.
  Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
  DO NOT write "the team is growing" without specifying the failure mode.

─── SUB-SECTION 4 — VERDICT and Re-assessment Trigger ──────────

  SUB-SECTION-4-ANCHOR-SEQUENCE (ordered anchors before VERDICT):
    Anchor 1: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
      Rating (closed set): `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
      DO NOT omit. DO NOT emit VERDICT before this line.
    Anchor 2: VERDICT declaration — choose one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`
      Reasoning sentence MUST reference FLAT-CASE-PRESSURE rating by name.
    Anchor 3: Re-assessment trigger — concrete threshold (DO NOT write "revisit as the team grows").

  If VERDICT is `CAN-OPERATE-FLAT`:
    Emit ABSENT block naming what structure is not warranted.
    STOP — no further content follows the termination marker.

─── CHECKPOINT-INERTIA — BLOCKING BEFORE GATE 1 STATUS ─────────

This checkpoint is a blocking intermediate verification step between GATE 1 content production and GATE 1 STATUS emission.
GATE 1 STATUS may not emit until this checkpoint passes.

FAIL CONDITION:
  STRUCTURING-COST FRAME must precede mechanism table rows in output produced.
  FAIL if any mechanism row appears before the STRUCTURING-COST FRAME block is closed.

CHECKPOINT-INERTIA VERIFICATION (reads produced output):
[ ] STRUCTURING-COST FRAME block is present in output produced
[ ] STRUCTURING-COST FRAME block is closed before first mechanism table row — read output and confirm; if any mechanism row precedes frame close: FAIL
[ ] NET-COST-COMPARISON present
[ ] Mechanism table has >= 2 data rows with Types from closed vocabulary
[ ] FLAT-CASE-CLOSED separator present
[ ] FLAT-CASE-PRESSURE line present, rating from closed set, references Sub-section 1 mechanism count and Sub-section 3 failure mode
[ ] VERDICT declared; reasoning references FLAT-CASE-PRESSURE by name
[ ] Re-assessment trigger is concrete
[ ] If CAN-OPERATE-FLAT: ABSENT block present; STOP marker present; no content follows

PROCEED to GATE 1 STATUS when all items verified. HALT if FAIL condition triggered.

─── GATE 1 STATUS ─────────────────────────────
Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

═══════════════════════════════════════════════
GATE 2 — ASCII ORG DIAGRAM
═══════════════════════════════════════════════

INPUT: inertia verdict (GATE 1 artifact).
PREREQUISITE: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===` present.

─── GATE 2 DO / DO NOT ───────────────────────
DO:
  - Draw ASCII hierarchy (>= 2 levels)
  - Show committees as distinct labeled nodes
  - Use only role names from ROLES-LOADED or ROLES-NOTE

DO NOT:
  - Produce a flat list of names without hierarchy
  - Introduce role names not in ROLES-LOADED or ROLES-NOTE
  - Embed committees inside an area node (committees require distinct labeled nodes)

─── GATE 2 BLOCKING VERIFICATION ────────────
[ ] ASCII diagram shows >= 2 hierarchy levels
[ ] Committees appear as distinct labeled nodes
[ ] All role names match GATE 0 typed role list

─── GATE 2 STATUS ─────────────────────────────
Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

═══════════════════════════════════════════════
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
═══════════════════════════════════════════════

INPUT: org diagram (GATE 2 artifact).
PREREQUISITE: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===` present.

─── GATE 3 DO / DO NOT ───────────────────────
DO:
  - Produce Headcount table with split Decides and Escalates columns
  - Annotate Key Roles: `[role name] ([domain type])`
  - Produce Rhythm table with >= 3 distinct rows (ROB + shiproom/gate + governance)
  - Produce charters interleaved with rhythm rows (each charter immediately after its row)
  - Run CHARTER-FORMAT-AUDIT loop per charter, in sequence
  - Emit PAIR-COUNT-VERIFIED after loop

DO NOT:
  - Merge Decides and Escalates into a single Decision Scope column
  - Write "owns the area" or generic ownership phrases
  - Combine two meetings into one rhythm row
  - Batch all rhythm rows before charters
  - Omit any charter for any governance rhythm row
  - Use short Quorum form (`N roles required`) — full fraction form required
  - Write "everything not listed under Decides" in Escalates
  - Emit GATE 3 STATUS before CHARTER-FORMAT-AUDIT loop completes and PAIR-COUNT-VERIFIED is present

─── HEADCOUNT BY AREA ────────────────────────
Columns: `Area | Headcount | Key Roles | Decides | Escalates`
Key Roles: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
>= 2 area rows + `**Total**` row (sum of area headcounts).
Decides: decision types owned at this level.
Escalates: decision types referred upward; name the destination role or forum.

─── OPERATING RHYTHM TABLE + CHARTERS (interleaved) ──────────────
Rhythm columns: `Cadence | Frequency | DRI / Owner | Purpose`
>= 3 distinct rows: ROB + shiproom or gate + governance meeting.
DRI / Owner: reference a role from ROLES-LOADED where possible.

For each governance row, produce its charter IMMEDIATELY:
  Purpose: one sentence
  Membership: >= 2 roles, each `[role name] ([domain type])`
  Decides: decision types owned
  Escalates: named destination; not "everything not listed under Decides"
  Quorum: `Quorum: [N] of [M] member roles required for binding decisions`
    N = minimum count required; M = total Membership roles listed
    DO NOT use short form

─── CHARTER-FORMAT-AUDIT LOOP ──────────────
After all rhythm-charter pairs produced, run per-charter iteration:

  FOR each charter (iterate in production sequence — do not skip):

    CHARTER-FORMAT-AUDIT [charter name]:
    [ ] Quorum matches `N of M member roles required for binding decisions` exactly
    [ ] All Membership roles carry `([domain type])` — type from ROLE-TYPE-CLASSIFICATION closed set
    [ ] All Membership role names exist in GATE 0 typed role list (cross-gate continuity)
    [ ] Escalates: names concrete destination (not TBD, not blank, not circular)
    [ ] Decides: populated with decision types

    IF any check fails:
      REJECT: [charter name] — [field] — [failure reason]
      Correct the failing field. Re-run audit for this charter before advancing to next.
    IF all checks pass:
      PROCEED: [charter name] — all fields verified

  After all charters pass:
  `PAIR-COUNT-VERIFIED: [N] rhythm rows, [N] charters produced.`
  N must equal the count of governance rows in the Operating Rhythm Table.

─── GATE 3 BLOCKING VERIFICATION ────────────
[ ] CHARTER-FORMAT-AUDIT loop complete; all charters emit PROCEED
[ ] PAIR-COUNT-VERIFIED present; N charters = N governance rhythm rows
[ ] All Membership role names confirmed in GATE 0 typed role list

─── GATE 3 STATUS ─────────────────────────────
Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STOP — ARTIFACT COMPLETE (emit immediately after GATE 3 STATUS on successful-completion path).

═══════════════════════════════════════════════
ORG-ELEMENT REGISTER
═══════════════════════════════════════════════

DO NOT skip. DO NOT proceed to Org Evolution Roadmap until all four categories populated:

  cat-1 (Areas): all area names from Headcount table
    Format: `- [area name] — headcount: [N]`

  cat-2 (Committees/Cadences): all committee and cadence names from Rhythm Table and Charters
    Format: `- [name]`

  cat-3 (Headcount): total headcount
    Format: `- Total headcount: [N]`

  cat-4 (DRI Roles): all DRI role names from Operating Rhythm Table
    Format: `- [DRI role]`

═══════════════════════════════════════════════
ORG EVOLUTION ROADMAP
═══════════════════════════════════════════════

Columns: `Trigger | Structural Change | Type`
DO NOT label optional.
Row 1: headcount threshold trigger.
Row 2: different category — workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

═══════════════════════════════════════════════
ANTI-PATTERN WATCH
═══════════════════════════════════════════════

Columns: `Anti-Pattern | Why It Applies Here | Mitigation`
Each Why It Applies Here cell MUST open: `[element name] (cat-N) — [one sentence of specific relevance]`
DO NOT write a Why It Applies Here cell naming an element without `(cat-N)` typed syntax.
DO NOT use a cat-N code not present in the ORG-ELEMENT REGISTER category schema.
>= 2 rows.

═══════════════════════════════════════════════
SECTION ORDER — INVIOLABLE
═══════════════════════════════════════════════

Sections must be produced in this exact sequence. No section may begin before its predecessor is complete.

  1. ARTIFACT-HANDOFF INVENTORY (preamble — before any gate content)
  2. CHECKPOINT-0 (blocking step — before GATE 0 content)
  3. GATE 0:
       ROLES-LOADED or ROLES-NOTE
       → ROLE-LOAD-ORDER three-tier applied
       → ROLE-TYPE-CLASSIFICATION
       → GATE 0 blocking verification
       → GATE 0 STATUS gate line
  4. GATE 1:
       STRUCTURING-COST FRAME (Step 1.1 first element)
       → NET-COST-COMPARISON
       → mechanism table (after frame block closed)
       → FLAT-CASE-CLOSED separator
       → Sub-section 2 (How We Coordinate Today)
       → Sub-section 3 (Rebuttal)
       → Sub-section 4 (FLAT-CASE-PRESSURE first → VERDICT → re-assessment trigger)
       → CHECKPOINT-INERTIA blocking verification
       → GATE 1 STATUS gate line
  5. GATE 2:
       ASCII Org Diagram
       → GATE 2 blocking verification
       → GATE 2 STATUS gate line
  6. GATE 3:
       Headcount by Area
       → Operating Rhythm Table + Charters (rhythm-charter pairs, interleaved)
       → CHARTER-FORMAT-AUDIT loop (per-charter in sequence)
       → PAIR-COUNT-VERIFIED
       → GATE 3 blocking verification
       → GATE 3 STATUS gate line
       → STOP — ARTIFACT COMPLETE
  7. ORG-ELEMENT REGISTER
  8. Org Evolution Roadmap
  9. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## Summary table

| Variation | Axis | C-41 | C-42 | Key structural move |
|-----------|------|------|------|---------------------|
| V-01 | CHECKPOINT-INERTIA only (minimal) | Named blocking step + FAIL condition + pass checklist | Absent | Tests whether C-41 is satisfied without C-42; all other structure held constant |
| V-02 | CHECKPOINT-0 only (minimal) | Absent | ARTIFACT-HANDOFF INVENTORY preamble + named CHECKPOINT-0 + FAIL condition | Tests whether C-42 is satisfied without C-41; preamble consultation enforced as precondition |
| V-03 | Both checkpoints in explicit blocking form | Named blocking step + FAIL condition | Named blocking step + FAIL condition | Combined form; minimal reinforcement; tests co-presence sufficiency |
| V-04 | Both checkpoints + declaration-level positional chain | Named blocking step + FAIL condition + DO NOT guard with causal explanation | Named blocking step + FAIL condition + prohibited-form declaration | Double-binding: instruction scope declares constraint; checkpoint scope enforces it |
| V-05 | Maximum integration | CHECKPOINT-INERTIA with NET-COST-COMPARISON, SUB-SECTION-4-ANCHOR-SEQUENCE, full audit | CHECKPOINT-0 with full GATE CHAIN preamble, produces/consumes for all four transitions | Subsumption: C-41 satisfies C-39+C-37; C-42 satisfies C-40+C-38; all prior criteria preserved |
