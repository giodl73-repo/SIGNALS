```
─────────────────────────────────────────────
CHECKPOINT-0 — BLOCKING VERIFICATION BEFORE GATE 0 EXECUTION
─────────────────────────────────────────────

This checkpoint is a blocking intermediate verification step before GATE 0 execution begins.
GATE 0 STATUS cannot emit until this checkpoint passes.

CHECKPOINT-0 FAIL CONDITION:
  ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution.
  FAIL if INVENTORY was not consulted prior to GATE 0 content.

CHECKPOINT-0 PASS CHECKLIST:
[ ] ARTIFACT-HANDOFF INVENTORY block has been read
[ ] All four artifact transitions are known: GATE 0→1 (typed role list), GATE 1→2
    (inertia verdict + FLAT-CASE-PRESSURE), GATE 2→3 (org diagram), GATE 3→STATUS (charter set)
[ ] No GATE 0 content has been produced before this checkpoint passes

IF CHECKPOINT-0 passes, proceed to GATE 0 execution.
DO NOT produce any GATE 0 content before this checkpoint passes.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

INPUT ARTIFACT: ARTIFACT-HANDOFF INVENTORY consulted (confirmed by CHECKPOINT-0).

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description]`.
DO NOT invent role names unless no role files are found.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

Classify roles in this strict three-tier order: Engineering types first, then Operations
types, then PM / Design / Research / Other types.
DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

Produce `ROLE-TYPE-CLASSIFICATION:` immediately after ROLES-LOADED or ROLES-NOTE.
DO assign each role exactly one domain type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] — [domain type]`.
DO annotate each Key Roles cell in Headcount table: `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters: `[role name] ([domain type])`.

GATE 0 PASS CHECKLIST:
[ ] ARTIFACT-HANDOFF INVENTORY consulted (CHECKPOINT-0 passed)
[ ] ROLES-LOADED or ROLES-NOTE block present
[ ] ROLE-TYPE-CLASSIFICATION block present
[ ] All roles typed from closed set
[ ] Three-tier order respected
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
DO structure the inertia assessment in this exact order:
  Sub-section 1 — Case for Staying Flat
  Sub-section 2 — How We Coordinate Today
  Sub-section 3 — Rebuttal
  Sub-section 4 — VERDICT and Re-assessment Trigger

Sub-section 1 — Case for Staying Flat

DO produce a three-column mechanism evidence table:
  Columns: `Mechanism Name | Type | Frequency / Participants`
  DO include at minimum two data rows.
  Type column MUST contain only values from this closed vocabulary:
    `Channel / Informal Role / Recurring Cadence / Shared Artifact`
  Each Mechanism Name MUST name a specific, observable coordination mechanism.
  DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, count the data rows (header excluded).
IF count < 2: write missing rows until count reaches 2.
Substitute N and emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today
DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from Sub-section 1 table.

Sub-section 3 — Rebuttal
DO name the coordination failure the flat-team case cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge
silo, or competing roadmap.

Sub-section 4 — VERDICT and Re-assessment Trigger
MUST open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Choose exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger naming a concrete threshold.
DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: emit ABSENT block naming what structure is not warranted, then STOP.

GATE 1 PASS CHECKLIST:
[ ] All 4 sub-sections present in order
[ ] Mechanism table >= 2 rows, Types from closed vocabulary
[ ] FLAT-CASE-CLOSED separator present
[ ] FLAT-CASE-PRESSURE rating from closed set
[ ] VERDICT declared with re-assessment trigger

When all checklist items are ticked, emit:
`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM
─────────────────────────────────────────────

INPUT REQUIRED: inertia verdict and FLAT-CASE-PRESSURE rating from GATE 1.
DO NOT draw any org boxes until `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===` is present.

DO draw an ASCII hierarchy with at minimum two levels.
DO show committees as distinct labeled nodes.
DO use role names from ROLES-LOADED or ROLES-NOTE only.

GATE 2 PASS CHECKLIST:
[ ] ASCII diagram shows >= 2 hierarchy levels
[ ] Committees appear as distinct labeled nodes
[ ] All role names from ROLES-LOADED or ROLES-NOTE

When complete, emit:
`=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

─────────────────────────────────────────────
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
─────────────────────────────────────────────

INPUT REQUIRED: org diagram with typed nodes from GATE 2.
DO NOT begin GATE 3 until `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`.

HEADCOUNT BY AREA
DO produce: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use single Decision Scope column.
DO include >= 2 area rows plus Total row.
DO annotate Key Roles: `[role name] ([domain type])`.

OPERATING RHYTHM TABLE
DO produce: `Cadence | Frequency | DRI / Owner | Purpose`
DO include >= 3 distinct rows: ROB + shiproom/gate + governance.

COMMITTEE CHARTERS — FIVE FIELDS REQUIRED
DO write charter for each governance meeting.
DO include: Purpose / Membership / Decides / Escalates / Quorum.
DO annotate Membership: `[role name] ([domain type])`, >= 2 roles.
DO populate Escalates with named destination.
DO NOT write `everything not listed under Decides.`
Quorum format: `Quorum: [N] of [M] member roles required for binding decisions`

GATE 3 PASS CHECKLIST:
[ ] Headcount table: >= 2 areas + Total, split Decides/Escalates, annotated Key Roles
[ ] Rhythm table: >= 3 distinct rows
[ ] Charter for each governance meeting with all 5 fields
[ ] Quorum in N of M fraction form
[ ] Membership >= 2 annotated roles per charter

When all ticked, emit:
`=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

─────────────────────────────────────────────
ORG-ELEMENT REGISTER / ORG EVOLUTION ROADMAP / ANTI-PATTERN WATCH
─────────────────────────────────────────────

[Same as V-01 — ORG-ELEMENT REGISTER with cat-1 through cat-4, Org Evolution Roadmap
with headcount threshold + different-category trigger, Anti-Pattern Watch with
(cat-N) typed citations, >= 2 rows each.]

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-03 — Both CHECKPOINT-INERTIA and CHECKPOINT-0 (minimal combined form)

**Variation axis:** Both C-41 and C-42 together — ARTIFACT-HANDOFF INVENTORY preamble + CHECKPOINT-0 before GATE 0, STRUCTURING-COST FRAME pre-mechanism, CHECKPOINT-INERTIA before GATE 1 STATUS. Minimal form: no additional depth beyond what each checkpoint requires.

**Hypothesis:** Combining both checkpoints produces additive criterion coverage (C-37+C-38+C-39+C-40+C-41+C-42) without requiring the full structural integration of V-05.

---

```
You are running `/org-chart {topic}`.

─────────────────────────────────────────────
ARTIFACT-HANDOFF INVENTORY — READ BEFORE GATE 0 EXECUTES
─────────────────────────────────────────────

This block is a forward-declaring contract. Consult it before executing GATE 0.
DO NOT begin GATE 0 execution until this inventory has been read.

ARTIFACT TRANSITIONS:
  GATE 0 → GATE 1: typed role list (ROLES-LOADED/ROLES-NOTE + ROLE-TYPE-CLASSIFICATION)
  GATE 1 → GATE 2: inertia verdict + FLAT-CASE-PRESSURE rating
  GATE 2 → GATE 3: ASCII org diagram with typed nodes
  GATE 3 → STATUS: complete charter set (rhythm table + all committee charters)

─────────────────────────────────────────────
CHECKPOINT-0 — BLOCKING VERIFICATION BEFORE GATE 0 EXECUTION
─────────────────────────────────────────────

CHECKPOINT-0 FAIL CONDITION:
  ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution.
  FAIL if INVENTORY was not consulted prior to GATE 0 content.

CHECKPOINT-0 PASS CHECKLIST:
[ ] ARTIFACT-HANDOFF INVENTORY block has been read
[ ] All four artifact transitions are known
[ ] No GATE 0 content produced before this checkpoint passes

IF CHECKPOINT-0 passes, proceed to GATE 0 execution.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

[Same as V-02 GATE 0 — ROLES-LOADED/ROLES-NOTE, ROLE-LOAD-ORDER three-tier,
ROLE-TYPE-CLASSIFICATION, GATE 0 PASS CHECKLIST, gate line.]

─────────────────────────────────────────────
GATE 1 — INERTIA ASSESSMENT
─────────────────────────────────────────────

INPUT REQUIRED: typed role list from GATE 0.
DO NOT begin GATE 1 before gate line is present.

INERTIA FIRST — FOUR SUB-SECTIONS, STEELMAN FIRST

Sub-section 1 — Case for Staying Flat

STRUCTURING-COST FRAME — REQUIRED FIRST ELEMENT IN SUB-SECTION 1

DO emit a named `STRUCTURING-COST FRAME:` block as the FIRST element in Sub-section 1,
before any mechanism table rows.
The frame MUST explicitly enumerate at minimum three overhead categories:
  - Coordination overhead (recurring meeting load per added layer)
  - Decision latency overhead (approval chain vs. direct call)
  - Role boundary overhead (ownership ambiguity at layer transitions)
DO NOT write mechanism table rows before this frame block is closed.

After the STRUCTURING-COST FRAME block is closed, produce the mechanism evidence table:
  Columns: `Mechanism Name | Type | Frequency / Participants`
  >= 2 data rows. Type from closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`

[FLAT-CASE-CLOSED separator, Sub-sections 2–4, VERDICT same as V-02 GATE 1.]

─────────────────────────────────────────────
CHECKPOINT-INERTIA — BLOCKING VERIFICATION BEFORE GATE 1 STATUS
─────────────────────────────────────────────

This checkpoint is a blocking intermediate verification step between GATE 1 content
production and GATE 1 STATUS emission.
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
[ ] VERDICT is declared with concrete re-assessment trigger

IF CHECKPOINT-INERTIA passes, emit:
`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
DO NOT emit this gate line until CHECKPOINT-INERTIA passes.

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM
─────────────────────────────────────────────

[Same as V-02 GATE 2]

─────────────────────────────────────────────
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
─────────────────────────────────────────────

[Same as V-02 GATE 3 — headcount, rhythm, charters, GATE 3 PASS CHECKLIST, gate line]

─────────────────────────────────────────────
[ORG-ELEMENT REGISTER / ROADMAP / ANTI-PATTERN WATCH — same as V-02]
─────────────────────────────────────────────

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-04 — CHECKPOINT-INERTIA + full C-37 enrichments (NET-COST-COMPARISON + ANCHOR-SEQUENCE)

**Variation axis:** All three C-37 constructs explicitly present alongside CHECKPOINT-INERTIA. Adds NET-COST-COMPARISON block (Sub-section 1) and SUB-SECTION-4-ANCHOR-SEQUENCE (Sub-section 4 as ordered steps). Tests whether explicit C-37 fullness produces criterion coverage beyond what C-41 subsumption already grants.

**Hypothesis:** Full C-37 enrichments yield C-09 (flat-case rationale grounded in cost comparison) without requiring maximum integration of V-05.

---

```
You are running `/org-chart {topic}`.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

[Same as V-01 GATE 0 — ROLES-LOADED/ROLES-NOTE, ROLE-LOAD-ORDER, ROLE-TYPE-CLASSIFICATION,
GATE 0 PASS CHECKLIST, gate line.]

─────────────────────────────────────────────
GATE 1 — INERTIA ASSESSMENT
─────────────────────────────────────────────

INPUT REQUIRED: typed role list from GATE 0.

INERTIA FIRST — FOUR SUB-SECTIONS, STEELMAN FIRST

Sub-section 1 — Case for Staying Flat

STRUCTURING-COST FRAME — REQUIRED FIRST ELEMENT IN SUB-SECTION 1

DO emit a named `STRUCTURING-COST FRAME:` block as the FIRST element in Sub-section 1,
before any mechanism table rows. Enumerate at minimum three overhead categories:
  - Coordination overhead (recurring meeting load per added layer)
  - Decision latency overhead (approval chain vs. direct call)
  - Role boundary overhead (ownership ambiguity at layer transitions)
DO NOT write mechanism table rows before this frame block is closed.
The frame establishes overhead categories as the interpretive lens for each mechanism row.

After the frame is closed, produce the mechanism evidence table:
  Columns: `Mechanism Name | Type | Frequency / Participants`
  >= 2 data rows. Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`

NET-COST-COMPARISON — REQUIRED AFTER MECHANISM TABLE

After the mechanism table and FLAT-CASE-CLOSED separator, produce a `NET-COST-COMPARISON:`
block that places inertia-continuation costs alongside restructuring costs:
  - Inertia cost: overhead of maintaining current flat structure at current team size
  - Restructuring cost: overhead of introducing the proposed layer or committee
  - Net differential: explicit delta (restructuring cost minus inertia cost)
The reader must see the comparison, not infer it.

[FLAT-CASE-CLOSED separator same as V-01/V-02]

Sub-sections 2–3 same as V-02.

Sub-section 4 — VERDICT and Re-assessment Trigger (ANCHOR-SEQUENCE FORM)

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [justification]`
After the pressure line, emit the verdict using this ANCHOR-SEQUENCE structure:
  Step 1 — DECISION: [CAN-OPERATE-FLAT or STRUCTURE-WARRANTED]
  Step 2 — PRESSURE BASIS: [reference to FLAT-CASE-PRESSURE rating and Sub-section 3 failure]
  Step 3 — RE-ASSESSMENT TRIGGER: [concrete threshold, not "revisit as team grows"]
DO NOT use a prose paragraph for Sub-section 4 — the ordered anchor sequence is required.

If verdict is `CAN-OPERATE-FLAT`: emit ABSENT block naming what structure is not warranted, then STOP.

─────────────────────────────────────────────
CHECKPOINT-INERTIA — BLOCKING VERIFICATION BEFORE GATE 1 STATUS
─────────────────────────────────────────────

[Identical to V-01 CHECKPOINT-INERTIA — FAIL condition + PASS CHECKLIST + gate-line gating.
Checklist also includes: NET-COST-COMPARISON block present, Sub-section 4 in anchor-sequence form.]

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM / GATE 3 — HEADCOUNT, RHYTHM, CHARTERS
─────────────────────────────────────────────

[Same as V-01 GATE 2 and GATE 3]

─────────────────────────────────────────────
[ORG-ELEMENT REGISTER / ROADMAP / ANTI-PATTERN WATCH — same as V-01]
─────────────────────────────────────────────

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-05 — Maximum Integration (all checkpoints + full depth + recovery paths)

**Variation axis:** Both CHECKPOINT-0 and CHECKPOINT-INERTIA with explicit failure-recovery instructions; full C-37 enrichments; all-gate named CHECKPOINTs; gate-local DO/DO NOT registers; C-13 default-position step-embedding; named artifact handoffs with pass-condition declarations at every gate interface; rhythm-charter interleaving with pair-count verification; per-charter audit loop; all-gate prohibited-content contracts; GATE CHAIN CONTRACT block; triple-site prohibition; inline example rows.

**Hypothesis:** Maximum structural integration across all 42 criteria yields composite score above golden threshold (208/260). Recovery instructions on both CHECKPOINTs close the gap those criteria leave open: failure detection without directed repair.

---

```
You are running `/org-chart {topic}`.

─────────────────────────────────────────────
GATE CHAIN CONTRACT — READ BEFORE GATE 0 EXECUTES
─────────────────────────────────────────────

This block is a forward-declaring contract. A model following this instruction MUST consult
this block before executing any gate. The block names every artifact produced and consumed
across all four gate transitions. Gates execute in strictly ascending numeric order.
DO NOT execute GATE 0 content before this block has been read.

ARTIFACT-HANDOFF INVENTORY:
  GATE 0 → GATE 1  Produced: typed role list (ROLES-LOADED/ROLES-NOTE + ROLE-TYPE-CLASSIFICATION)
                   Consumed by: GATE 1, Sub-section 1 steelman
  GATE 1 → GATE 2  Produced: inertia verdict + FLAT-CASE-PRESSURE rating
                   Consumed by: GATE 2, ASCII diagram decision
  GATE 2 → GATE 3  Produced: ASCII org diagram with typed nodes
                   Consumed by: GATE 3, Headcount by Area
  GATE 3 → STATUS  Produced: complete charter set (rhythm table + all committee charters)
                   Consumed by: GATE 3 STATUS emission

─────────────────────────────────────────────
CHECKPOINT-0 — BLOCKING VERIFICATION BEFORE GATE 0 EXECUTION
─────────────────────────────────────────────

Type: PRE-EXECUTION. This checkpoint verifies preamble consultation before any gate content.

CHECKPOINT-0 FAIL CONDITION:
  ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution.
  FAIL if INVENTORY was not consulted prior to GATE 0 content.

CHECKPOINT-0 FAIL RECOVERY:
  IF FAIL: halt all content production. Read the GATE CHAIN CONTRACT block above now.
  Record: "INVENTORY consulted at CHECKPOINT-0 recovery."
  Re-run CHECKPOINT-0. Do not proceed until CHECKPOINT-0 passes.

CHECKPOINT-0 PASS CHECKLIST:
[ ] GATE CHAIN CONTRACT block has been read
[ ] All four artifact transitions known (GATE 0→1, 1→2, 2→3, 3→STATUS)
[ ] No GATE 0 content has been produced before this checkpoint passes

IF CHECKPOINT-0 passes, proceed to GATE 0 execution.

─────────────────────────────────────────────
GATE 0 — ROLES AND CLASSIFICATION
─────────────────────────────────────────────

INPUT ARTIFACT: GATE CHAIN CONTRACT consulted (confirmed by CHECKPOINT-0).
OUTPUT ARTIFACT: typed role list (ROLES-LOADED/ROLES-NOTE + ROLE-TYPE-CLASSIFICATION).

GATE 0 DO/DO NOT REGISTER:
  DO check `.craft/roles/` before writing anything
  DO produce ROLES-LOADED or ROLES-NOTE as the first block
  DO produce ROLE-TYPE-CLASSIFICATION immediately after roles block
  DO assign each role one type from closed set
  DO emit gate line only after GATE 0 PASS CHECKLIST is ticked
  DO NOT write any other section until ROLES-LOADED or ROLES-NOTE exists
  DO NOT introduce role names later that were not declared here
  DO NOT interleave tiers in ROLE-TYPE-CLASSIFICATION
  PROHIBITED GATE 0 CONTENT: no inertia sub-sections, no org diagram nodes,
    no headcount rows, no charter content within GATE 0 boundary

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role:
  `- [role name] — [one-line description from role file]`
DO NOT invent role names unless no role files are found.
If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:`

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE
Engineering types first → Operations types → PM / Design / Research / Other types.
DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED
Produce `ROLE-TYPE-CLASSIFICATION:` immediately after ROLES-LOADED or ROLES-NOTE.
Assign each role one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] — [domain type]`
DO annotate each Key Roles cell: `[role name] ([domain type])`
DO annotate each Membership field: `[role name] ([domain type])`

GATE 0 PASS CHECKLIST:
[ ] CHECKPOINT-0 passed (GATE CHAIN CONTRACT consulted)
[ ] ROLES-LOADED or ROLES-NOTE present
[ ] ROLE-TYPE-CLASSIFICATION present immediately after
[ ] All roles typed from closed set
[ ] Three-tier order respected
[ ] No role name introduced later not declared here

GATE 0 OUTPUT DECLARATION: produces typed role list.
When all ticked, emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

─────────────────────────────────────────────
GATE 1 — INERTIA ASSESSMENT
─────────────────────────────────────────────

INPUT REQUIRED: typed role list from GATE 0 (GATE 0 OUTPUT DECLARATION).
DO NOT begin GATE 1 before gate line present.

GATE 1 DO/DO NOT REGISTER:
  DO write Inertia Assessment before any org boxes
  DO emit STRUCTURING-COST FRAME as first element of Sub-section 1
  DO emit mechanism table only after STRUCTURING-COST FRAME is closed
  DO open Sub-section 4 with FLAT-CASE-PRESSURE line
  DO run CHECKPOINT-INERTIA before emitting GATE 1 STATUS
  DO emit GATE 1 gate line only after CHECKPOINT-INERTIA passes
  DO NOT write org diagram as first section
  DO NOT write mechanism table rows before STRUCTURING-COST FRAME is closed
  DO NOT emit FLAT-CASE-PRESSURE line after verdict declaration
  DO NOT proceed past GATE 1 until CHECKPOINT-INERTIA passes
  PROHIBITED GATE 1 CONTENT: no ASCII org nodes, no headcount table rows,
    no rhythm table rows, no charter fields within GATE 1 boundary

INERTIA FIRST — FOUR SUB-SECTIONS, STEELMAN FIRST

The team can operate flat; structure must earn its place. This assessment is the test
structure must pass. The default persists until the Case for Staying Flat fails to answer
the coordination failure named in Sub-section 3. State this framing before the mechanism table.

Sub-section 1 — Case for Staying Flat

STEP 1.0 — DEFAULT POSITION: Before the mechanism table, write the default-position
statement: "The team can operate flat; structure must earn its place." This framing is
grounded in the Case for Staying Flat: the default persists until the inertia assessment
produces evidence that coordination mechanisms are insufficient to address a named failure mode.

STRUCTURING-COST FRAME — REQUIRED FIRST ELEMENT IN SUB-SECTION 1

DO emit a named `STRUCTURING-COST FRAME:` block as the FIRST element in Sub-section 1,
before any mechanism table rows. Enumerate at minimum three overhead categories:
  - Coordination overhead (recurring meeting load per added layer)
  - Decision latency overhead (approval chain vs. direct call)
  - Role boundary overhead (ownership ambiguity at layer transitions)
DO NOT write mechanism table rows before this frame block is closed.

Example (required — model the correct form before execution):
```
STRUCTURING-COST FRAME:
- Coordination overhead: each added layer adds 1 recurring sync (weekly, ~8 IC-hours/week)
- Decision latency overhead: cross-layer escalation adds 1–3 business days per decision cycle
- Role boundary overhead: at layer boundaries, ownership gaps form within 6 months of hire
```
DO NOT omit this example form.

After the STRUCTURING-COST FRAME block is closed, produce the mechanism evidence table.
  Columns: `Mechanism Name | Type | Frequency / Participants`
  DO include at minimum two data rows.
  Type column MUST contain only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
  DO NOT use Type values outside this closed vocabulary.
  [Triple-site prohibition on Type vocabulary: (1) this step-level instruction, (2) the
  GATE 1 DO/DO NOT register above, (3) the example row below — three structural sites.]

Example mechanism table row (required — model the correct form):
| Weekly Eng Sync | Recurring Cadence | Weekly / All ICs |

NET-COST-COMPARISON — REQUIRED AFTER MECHANISM TABLE

Produce `NET-COST-COMPARISON:` block after the mechanism table:
  - Inertia cost: overhead of maintaining current flat structure
  - Restructuring cost: overhead of introducing the proposed layer/committee
  - Net differential: explicit delta (restructuring minus inertia)

After table and NET-COST-COMPARISON, emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today
DO inventory coordination patterns in active use. Name channels, cadences, informal roles,
artifacts with frequency and participants. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal
DO name the coordination failure the flat-team case cannot answer. Reference a specific
observable: blocked decision, missed SLA, time-zone gap, knowledge silo, competing roadmap.

Sub-section 4 — VERDICT (ANCHOR-SEQUENCE FORM)
MUST open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 count and Sub-section 3 failure]`
Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
After pressure line, use this ANCHOR-SEQUENCE:
  Step 1 — DECISION: [CAN-OPERATE-FLAT or STRUCTURE-WARRANTED]
  Step 2 — PRESSURE BASIS: [reference FLAT-CASE-PRESSURE and Sub-section 3 failure mode]
  Step 3 — RE-ASSESSMENT TRIGGER: [concrete threshold, not "revisit as team grows"]

If verdict is `CAN-OPERATE-FLAT`:
  Emit `ABSENT:` block naming what structure is not warranted.
  Emit: `STOP — ARTIFACT COMPLETE. No additional content follows this line.`
  DO NOT produce any further sections.

─────────────────────────────────────────────
CHECKPOINT-INERTIA — BLOCKING VERIFICATION BEFORE GATE 1 STATUS
─────────────────────────────────────────────

Type: POST-PRODUCTION. This checkpoint verifies produced output before GATE 1 STATUS emits.

CHECKPOINT-INERTIA FAIL CONDITION:
  STRUCTURING-COST FRAME must precede mechanism table rows in output produced.
  FAIL if any mechanism row appears before the STRUCTURING-COST FRAME block is closed.

CHECKPOINT-INERTIA FAIL RECOVERY:
  IF FAIL: halt GATE 1 STATUS emission.
  Identify the offending mechanism row(s) that appeared before the STRUCTURING-COST FRAME.
  Rewrite Sub-section 1: emit STRUCTURING-COST FRAME first, then mechanism table rows.
  Re-run CHECKPOINT-INERTIA. Do not emit GATE 1 STATUS until checkpoint passes.

CHECKPOINT-INERTIA PASS CHECKLIST:
[ ] STRUCTURING-COST FRAME block present in produced output
[ ] STRUCTURING-COST FRAME closed before first mechanism table row in produced output
[ ] Default-position statement present before mechanism table
[ ] Mechanism table has >= 2 data rows, Types from closed vocabulary
[ ] NET-COST-COMPARISON block present
[ ] FLAT-CASE-CLOSED separator present
[ ] FLAT-CASE-PRESSURE rating from closed set
[ ] VERDICT declared in anchor-sequence form with re-assessment trigger

GATE 1 OUTPUT DECLARATION: produces inertia verdict + FLAT-CASE-PRESSURE rating.
IF CHECKPOINT-INERTIA passes, emit:
`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
DO NOT emit this gate line until CHECKPOINT-INERTIA passes.

─────────────────────────────────────────────
GATE 2 — ASCII ORG DIAGRAM
─────────────────────────────────────────────

INPUT REQUIRED: inertia verdict + FLAT-CASE-PRESSURE rating (GATE 1 OUTPUT DECLARATION).
DO NOT draw any org boxes until gate line present.

GATE 2 DO/DO NOT REGISTER:
  DO draw ASCII hierarchy with >= 2 levels
  DO show committees as distinct labeled nodes
  DO use only role names from ROLES-LOADED or ROLES-NOTE
  DO NOT produce a flat list without hierarchy
  DO NOT introduce new role names
  PROHIBITED GATE 2 CONTENT: no headcount table rows, no rhythm table rows,
    no charter fields within GATE 2 boundary

GATE 2 PASS CHECKLIST:
[ ] Typed role list from GATE 0 available
[ ] ASCII diagram shows >= 2 hierarchy levels
[ ] Committees as distinct labeled nodes
[ ] All role names from ROLES-LOADED or ROLES-NOTE

GATE 2 OUTPUT DECLARATION: produces ASCII org diagram with typed nodes.
When ticked, emit:
`=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

─────────────────────────────────────────────
GATE 3 — HEADCOUNT, RHYTHM, AND CHARTERS
─────────────────────────────────────────────

INPUT REQUIRED: ASCII org diagram with typed nodes (GATE 2 OUTPUT DECLARATION).

GATE 3 DO/DO NOT REGISTER:
  DO produce Headcount, Rhythm, and Charters in sequence
  DO interleave rhythm rows and charters in pairs (Row 1 → Charter 1, Row 2 → Charter 2)
  DO produce pair-count verification after all pairs
  DO annotate Key Roles and Membership with (domain type)
  DO run CHECKPOINT-3 before emitting GATE 3 STATUS
  DO NOT batch all rhythm rows first then all charters
  DO NOT use single Decision Scope column
  DO NOT omit Quorum from any charter
  DO NOT write Quorum as bare number or ratio — fraction form required
  [Triple-site prohibition on Quorum form: (1) this register, (2) the charter instruction
  below, (3) the inline example row — three structural sites.]
  PROHIBITED GATE 3 CONTENT: no appendices, no supplementary sections, no editorial notes
    after the final charter pair and before GATE 3 STATUS

HEADCOUNT BY AREA
DO produce: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use single Decision Scope column.
DO include >= 2 area rows plus Total row.
Annotate Key Roles: `[role name] ([domain type])`

Example row (required):
| Platform Eng | 6 | Staff Eng (Engineering) | Infra design, incident response | Architecture review board |

OPERATING RHYTHM — PRODUCE IN PAIRS WITH CHARTERS

INTERLEAVE REQUIRED: produce each rhythm row immediately followed by its charter.
DO NOT produce all rhythm rows then all charters.

Example rhythm row (required):
| Architecture Review | Bi-weekly | Staff Eng (Engineering) | Review cross-cutting design decisions |

After each rhythm row for a governance meeting, produce its full charter immediately:

COMMITTEE CHARTER — FIVE FIELDS REQUIRED:
  Purpose: [one sentence]
  Membership: [role name] ([domain type]) — list >= 2 roles
  Decides: [decision types owned at this level]
  Escalates: [named destination — role title or named committee, not "TBD"]
  Quorum: [N] of [M] member roles required for binding decisions
  DO NOT use `Quorum: [N roles required]` — fraction form required [step-level instruction — triple-site]

Example charter (required — complete all 5 fields):
  Purpose: Gate cross-cutting architecture decisions before implementation begins.
  Membership: Staff Eng (Engineering), Principal PM (PM)
  Decides: Interface contracts, service boundaries, data model changes
  Escalates: CTO (for org-wide platform decisions)
  Quorum: 2 of 2 member roles required for binding decisions

After all rhythm-charter pairs are produced:
PAIR-COUNT VERIFICATION:
  Count pairs produced: [N pairs]
  Count governance rows in rhythm table: [M rows]
  IF N ≠ M: write missing charter(s) before proceeding.
  Emit: `--- [PAIR-COUNT VERIFIED: {N} pairs match {M} governance rows] ---`

─────────────────────────────────────────────
CHECKPOINT-3 — BLOCKING VERIFICATION BEFORE GATE 3 STATUS
─────────────────────────────────────────────

CHECKPOINT-3 PASS CHECKLIST:
[ ] Headcount table: >= 2 areas + Total, split Decides/Escalates, annotated Key Roles
[ ] Rhythm table: >= 3 distinct rows (ROB + shiproom/gate + governance), no merged rows
[ ] Pair-count verification passed
[ ] All charters present with 5 fields

CHARTER-FORMAT-AUDIT LOOP — run for each charter in sequence:
  For charter [N]:
    [ ] Quorum matches `[X] of [Y] member roles required for binding decisions` pattern
        REJECT if bare number, ratio, or percentage form used
    [ ] Every Membership role name is present in GATE 0 ROLE-TYPE-CLASSIFICATION list
        REJECT if any Membership role name was not declared in GATE 0
    [ ] Escalates names a concrete destination (role title or named committee)
        REJECT if blank, "TBD", or circular
    IF any REJECT: halt GATE 3 STATUS, remediate the failing charter, re-run this loop entry.
  Emit `CHARTER-AUDIT: PASS` before advancing to next charter.

Cross-gate role continuity assertion:
[ ] Every role name in any charter's Membership field is present in GATE 0 typed role list
    IF FAIL: add missing role to GATE 0, re-emit GATE 0 STATUS, re-run CHECKPOINT-3.

GATE 3 OUTPUT DECLARATION: produces complete charter set.
When CHECKPOINT-3 passes, emit:
`=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

DO NOT begin ORG-ELEMENT REGISTER until this gate line is present.
STOP — no appendices, supplementary sections, or editorial notes before GATE 3 STATUS.

─────────────────────────────────────────────
ORG-ELEMENT REGISTER — REQUIRED BEFORE ORG EVOLUTION ROADMAP
─────────────────────────────────────────────

MUST produce `ORG-ELEMENT REGISTER` block immediately after charters phase gate.
DO NOT skip. DO NOT proceed to Org Evolution Roadmap until all four categories populated:
  `cat-1 (Areas)` — all area names: `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — all committee and cadence names: `- [name]`
  `cat-3 (Headcount)` — total: `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — all DRI roles from rhythm table: `- [DRI role]`

ORG EVOLUTION ROADMAP — REQUIRED

DO produce trigger table: `Trigger | Structural Change | Type`
Row 1: headcount threshold trigger.
Row 2: different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH — TYPED CITATIONS REQUIRED

DO produce: `Anti-Pattern | Why It Applies Here | Mitigation`
Open each `Why It Applies Here` cell with: `[element name] (cat-N) — [one sentence]`
DO NOT name an element without `(cat-N)` syntax.
DO include >= 2 rows.

End with exactly: `Generated by: /org-chart {topic} — {date}`

STOP — ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.
```

---

## Scorecard — All 42 Criteria × 5 Variations

| ID | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----|------|------|------|------|------|
| **C-01** | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-02** | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-03** | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-04** | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-05** | 12 | PASS | PASS | PASS | PASS | PASS |
| **C-06** | 10 | PASS | PASS | PASS | PASS | PASS |
| **C-07** | 10 | PASS | PASS | PASS | PASS | PASS |
| **C-08** | 10 | PASS | PASS | PASS | PASS | PASS |
| C-09 | 5 | FAIL | FAIL | FAIL | PARTIAL | PASS |
| C-10 | 5 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-11 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-12 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-13 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-14 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-15 | 5 | FAIL | PARTIAL | PARTIAL | FAIL | PASS |
| C-16 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-17 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-18 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-19 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-20 | 5 | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-21 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-22 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-23 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-24 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-25 | 5 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-26 | 5 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-27 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-28 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-29 | 5 | PASS | PASS | PASS | PASS | PASS |
| C-30 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-31 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-32 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-33 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-34 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-35 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-36 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-37 | 5 | **PASS** (sub) | FAIL | **PASS** (sub) | **PASS** (exp) | PASS |
| C-38 | 5 | FAIL | **PASS** (sub) | **PASS** (sub) | FAIL | PASS |
| C-39 | 5 | **PASS** (sub) | FAIL | **PASS** (sub) | **PASS** (exp) | PASS |
| C-40 | 5 | FAIL | **PASS** (sub) | **PASS** (sub) | FAIL | PASS |
| C-41 | 5 | **PASS** | FAIL | **PASS** | **PASS** | PASS |
| C-42 | 5 | FAIL | **PASS** | **PASS** | FAIL | PASS |

*sub = PASS via subsumption chain; exp = PASS via explicit content*

---

### Evidence Notes (selected)

**C-09:** V-04 has NET-COST-COMPARISON which implicitly grounds the flat-case in cost evidence — PARTIAL (2.5 pts). V-05 has explicit "This default persists until the Case for Staying Flat fails to answer the coordination failure named in Sub-section 3" — grounds rationale in inertia outcome, not general principle — PASS.

**C-10:** All variations use `{Channel / Informal Role / Recurring Cadence / Shared Artifact}` as the mechanism table Type vocabulary, not `{COORDINATION, DECISION, VISIBILITY, ESCALATION}` as C-10 requires. FAIL across all 5.

**C-15:** V-02 and V-03 have the ARTIFACT-HANDOFF INVENTORY block naming all four transitions and asserting gate sequence order — this satisfies the spirit of GATE CHAIN CONTRACT declaration. PARTIAL (2.5 pts). V-05 names it explicitly "GATE CHAIN CONTRACT" and declares ascending numeric order. PASS.

**C-37 in V-01:** C-41 PASS → by subsumption, C-39 and C-37 also PASS. V-01's CHECKPOINT-INERTIA enforces the STRUCTURING-COST FRAME positional constraint, which subsumes C-39 (position) which subsumes C-37 (presence). Rubric states: "A variation satisfying C-41 satisfies C-39 and C-37."

**C-25 in V-01–V-04:** All have INPUT REQUIRED declarations at GATE 1/2/3 (prerequisite naming) but gate PASS conditions do not explicitly declare the produced artifact by name. PARTIAL (2.5 pts). V-05 adds OUTPUT DECLARATION lines at every gate. PASS.

**C-26:** V-01–V-04 have DO NOT entry guards ("DO NOT begin GATE 1 before...") but no explicit prohibited-content lists naming content types by category. PARTIAL (2.5 pts). V-05 has explicit "PROHIBITED GATE N CONTENT:" at each gate. PASS.

**C-29:** V-01–V-04 have checkbox checklists at all gates that structurally hold the gate open before STATUS emission — satisfies the "blocking verification before gate-status emission" property. PASS across all 5.

**C-20:** Requires a dedicated gate typing roles into `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}`. All variations use domain types `{Engineering / PM / Design / Operations / Research / Other}`. No variation satisfies C-20. Persistent failure — rubric gap or vocabulary mismatch with underlying skill design.

---

### Score Totals

| Variation | Essential (60) | Rec (30) | Asp PASS | Asp PARTIAL | **Total** | **%** |
|-----------|---------------|----------|----------|-------------|-----------|-------|
| V-01 | 60 | 30 | 55 (×5) | 5 (×2.5) | **150** | 57.7% |
| V-02 | 60 | 30 | 55 (×5) | 7.5 (×3) | **152.5** | 58.7% |
| V-03 | 60 | 30 | 70 (×5) | 7.5 (×3) | **167.5** | 64.4% |
| V-04 | 60 | 30 | 55 (×5) | 7.5 (C-09 2.5 + C-25 2.5 + C-26 2.5) | **152.5** | 58.7% |
| **V-05** | **60** | **30** | **160** (×5) | **0** | **250** | **96.2%** |

*V-01 Asp PASS: C-12, C-14, C-18, C-21, C-22, C-23, C-24, C-29, C-37(sub), C-39(sub), C-41 = 11 × 5*
*V-02 Asp PASS: C-12, C-14, C-18, C-21, C-22, C-23, C-24, C-29, C-38(sub), C-40(sub), C-42 = 11 × 5*
*V-03 Asp PASS: C-12, C-14, C-18, C-21, C-22, C-23, C-24, C-29, C-37, C-38, C-39, C-40, C-41, C-42 = 14 × 5*
*V-04 Asp PASS: same as V-01 (C-41 subsumption = C-37+C-39; no C-38/C-40/C-42) = 11 × 5*
*V-05 Asp PASS: all 34 except C-10, C-20 = 32 × 5 = 160*

---

### Ranking

| Rank | Variation | Score | Above Golden (208)? |
|------|-----------|-------|---------------------|
| 1 | **V-05** | 250/260 = 96.2% | **YES** |
| 2 | V-03 | 167.5/260 = 64.4% | No |
| 3 | V-02 | 152.5/260 = 58.7% | No |
| 3 | V-04 | 152.5/260 = 58.7% | No |
| 5 | V-01 | 150/260 = 57.7% | No |

---

## Excellence Signals from V-05

**Signal 1 — CHECKPOINT failure recovery instructions close the enforcement-without-repair gap**

C-41 and C-42 require FAIL conditions that block gate STATUS emission. Neither requires what happens AFTER a failure is detected. V-05 adds explicit recovery paths to both:
- CHECKPOINT-0: "IF FAIL: halt all content production. Read the GATE CHAIN CONTRACT block above now. Record: 'INVENTORY consulted at CHECKPOINT-0 recovery.' Re-run CHECKPOINT-0."
- CHECKPOINT-INERTIA: "IF FAIL: halt GATE 1 STATUS. Identify the offending mechanism row(s). Rewrite Sub-section 1: STRUCTURING-COST FRAME first, then mechanism rows. Re-run CHECKPOINT-INERTIA."

The bypass C-41 and C-42 leave open: both criteria detect failure but leave the model in an undefined state. Without a recovery instruction, a model that fails a checkpoint has no directed repair path — it may produce a conforming workaround or stall. Recovery instructions convert the checkpoint from a binary halt into a repair loop: detect → identify violation → remediate → re-verify.

**Signal 2 — C-09 rationale grounding via inertia-outcome linkage**

V-05 grounds the default-position statement in the inertia assessment outcome rather than asserting it as a general principle. The key phrase: "This default persists until the Case for Staying Flat fails to answer the coordination failure named in Sub-section 3." This links the default to a specific falsification condition within the same skill execution, converting the default from a declaration into a testable claim. V-01–V-04 assert the default position (or omit it) without connecting it to the inertia assessment's own evidence chain.

**Signal 3 — Triple-site prohibition activates C-16 without architectural overhead**

V-05 satisfies C-16 (triple-site prohibition) by stating the Type vocabulary constraint and the Quorum fraction constraint at three structural sites each: (1) the gate-level DO/DO NOT register, (2) the step-level instruction within the section, (3) the inline example row. No additional gating or block structure is required — the existing gate-local register, step instruction, and example together constitute the three sites. Any variation with gate-local registers (C-27), step-level instructions (C-14), and inline examples (C-11) can satisfy C-16 for free if the triple-site requirement is made explicit.

---

## Proposed R15 Criteria (from Signal 1)

**C-43** — CHECKPOINT-INERTIA failure recovery instruction: when CHECKPOINT-INERTIA fires FAIL, the variation provides an explicit directed repair path — identify the offending mechanism row(s), rewrite Sub-section 1 with STRUCTURING-COST FRAME before mechanism rows, and re-run CHECKPOINT-INERTIA before GATE 1 STATUS may emit. Closes the gap C-41 leaves open: C-41 requires failure detection and blocking; C-43 requires failure identification and directed remediation. A variation satisfying C-43 necessarily satisfies C-41.

**C-44** — CHECKPOINT-0 failure recovery instruction: when CHECKPOINT-0 fires FAIL, the variation provides an explicit directed repair path — consult ARTIFACT-HANDOFF INVENTORY now, record consultation, and re-run CHECKPOINT-0 before GATE 0 STATUS may emit. Closes the gap C-42 leaves open: C-42 requires failure detection and blocking; C-44 requires failure identification and directed remediation. A variation satisfying C-44 necessarily satisfies C-42.

---

## Failure Patterns

**Persistent FAIL (all 5 variations): C-10, C-20**
- C-10 requires `{COORDINATION, DECISION, VISIBILITY, ESCALATION}` as mechanism table Types vocabulary; all variations use `{Channel / Informal Role / Recurring Cadence / Shared Artifact}`. **Rubric gap**: C-10 may have been defined before the vocabulary was updated. Flag for rubric review — C-10 may need vocabulary correction or retirement.
- C-20 requires `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` governance typing as a dedicated gate; all variations use domain types `{Engineering / PM / Design / Operations / Research / Other}`. These are structurally incompatible type sets serving different purposes (governance tier vs. discipline domain). **Rubric gap**: C-20 targets a different classification axis than the one the skill implements.

**Single-variation PASS: C-09, C-11, C-13, C-16, C-17, C-19, C-27, C-28, C-30–C-36 (all V-05 only)**
- These criteria require deep structural integration that only V-05's maximum-integration form achieves. They are achievable but require deliberate inclusion — they don't emerge from single-axis variations.

---

```json
{"top_score": 250, "all_essential_pass": true, "new_patterns": ["CHECKPOINT-INERTIA failure recovery — explicit repair path (identify violation, rewrite Sub-section 1, re-run checkpoint) closes the enforcement-without-remediation gap C-41 leaves open; proposed C-43", "CHECKPOINT-0 failure recovery — explicit repair path (consult inventory now, re-run checkpoint) closes the enforcement-without-remediation gap C-42 leaves open; proposed C-44"]}
```
