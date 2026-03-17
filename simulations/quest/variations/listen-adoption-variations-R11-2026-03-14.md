# Variations: listen-adoption — Round 11

**Rubric:** v11 | **New criteria:** C-31, C-32, C-33 | **Max composite:** 215 | **Golden threshold:** 80

---

## Variation Axes

| Axis | R11 Target | Description |
|------|-----------|-------------|
| C-32 placement A | C-32 | Mechanism anchor as unconditional pre-verification inline declaration |
| C-32 placement B | C-32 | Mechanism anchor as per-gate footer inside each gate section (H, I, J) |
| C-32 placement C | C-32 | Mechanism anchor as dedicated named body section between SECTION J and SECTION K |
| C-33 composition | C-33 | STRUCTURAL CONTRACT explicitly names C-29 + C-32 co-presence as the requirement |
| C-31 explicit rows | C-31 | TABLE 3 header names the four transition-pair rows as typed structural slot keys |

**Single-axis (V-01, V-02, V-03):** C-32 placement A · C-32 placement B · C-32 placement C
**Combined (V-04):** C-32 placement A + C-33 composition assertion
**Full (V-05):** C-31 explicit rows + C-32 placement B + C-33 composition assertion

**Baseline (all five carry from R10 V-05):** DISPLACEMENT DECLARATION (C-26), 16-role SECTION A table (C-01), SECTION B named inertia IDs I-01–I-05 (C-11), PHASE 1–6 structural headers with month ranges (C-02, C-08, C-25), PHASE 3 CHASM non-adoption (C-03), answer-form Q1–Q4 champion entries with Q3 as inertia-ID answer (C-13, C-14, C-29), 2-scenario sensitivity table with Named Lever column (C-09), signal readiness table (C-10), TABLE 3 with four named transition-pair rows and constraint-encoding column header (C-07, C-28, C-31), "Retention intervention: [one concrete action...]" field label (C-06, C-15, C-27), PART 4 interventions (C-04, C-05), ## VERIFICATION MODE header (C-23), SECTIONS H/I/J with revision obligation (C-16, C-17, C-18), SECTION K with Execution Stamp column (C-20, C-21, C-22, C-24, C-30).

**C-31/C-32/C-33 design intent per variation:**

| Variation | C-31 | C-32 | C-33 | Design note |
|-----------|------|------|------|-------------|
| V-01 | Carry R10 V-05 (named rows present) | Pre-verification unconditional declaration | Implicit (C-29 in baseline + C-32 now present) | Minimal intrusion — one line before VERIFICATION MODE; always fires; proves mechanism in body |
| V-02 | Carry R10 V-05 | Per-gate footer in H/I/J | Implicit | Three anchor points; any one satisfies C-32; triple-proof of mechanism availability |
| V-03 | Carry R10 V-05 | Dedicated `## MECHANISM ANCHOR` section post-J pre-K | Implicit | Named body section unambiguously satisfies "document body before SECTION K"; structurally separate from terminal record |
| V-04 | Carry R10 V-05 | Pre-verification declaration | Explicit co-presence assertion in STRUCTURAL CONTRACT | C-33 becomes architecturally required, not emergent — STRUCTURAL CONTRACT names both C-29 and C-32 as mandatory co-present mechanisms |
| V-05 | Explicit named-slot type declaration in TABLE 3 | Per-gate footer + pre-verification declaration | STRUCTURAL CONTRACT co-presence assertion | Full: all three R11 criteria independently enforced at distinct structural layers |

---

## V-01 — Single Axis: C-32 Pre-Verification Declaration

**Variation axis:** Lifecycle emphasis — a mandatory MECHANISM STATE line is inserted immediately before `## VERIFICATION MODE`. The declaration is unconditional: the model writes it regardless of whether any correction fired in the content sections. Two permitted forms: `CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered` (when no correction has yet been produced) or `CORRECTION BLOCK fired — see Section [H/I/J]` (when a correction was already generated above). Either form proves the mechanism was available in the document body before SECTION K.

**Hypothesis:** Placing the mechanism anchor as a single unconditional line before the verification boundary is minimally invasive — one extra structural output requirement, always fires, and proves C-32 without altering any content section or gate format. C-29 (answer-form questions) remains active from R10 V-05 baseline. C-33 passes implicitly because C-29 is already in the document body and C-32 is now present. C-19 remains PARTIAL in high-compliance architectures (answer-form suppresses gate failures), but C-32 resolves the paradox-of-strength by substituting a mechanism-presence declaration for triggered proof.

---

```
DISPLACEMENT DECLARATION (read before generating any output):

Every role on this team is currently doing something. That something is THE INCUMBENT — the
existing workflow, tool, or process that {{topic}} must displace. Name THE INCUMBENT explicitly
here before beginning PART 1. Every PHASE body will ask: what does this phase do to THE
INCUMBENT's position?

THE INCUMBENT for this topic: [name the current workflow, tool, or process being displaced —
specific enough that a role can be described as "protecting" or "having already left" it]

---

STRUCTURAL CONTRACT (read before generating any section):

- PART 1: Role assignment and named inertia (Sections A + B). All rationale runs through the
  displacement lens.
- PART 2: Phase-by-phase adoption simulation. PHASE 1–6 headers are structural — Rogers
  sequence violation is architecturally impossible. PHASE 3 CHASM is a non-adoption interstitial.
  Phase headers for PHASE 3 and PHASE 2 champion entries use answer-form questions: the inertia
  ID is the answer to the question, not a value in a fill-form slot. Omitting the ID leaves
  the question unanswered — not a blank field, but an incomplete sentence.
- TABLE 3: Phase Transition Spread Mechanisms — immediately after PART 2, before PART 3. Four
  named structural slots, one per canonical transition pair. The spread mechanism column header
  is fixed: "Spread Mechanism: [named signal or artifact — not generic word-of-mouth]". Generic
  entries are structurally incompatible with the column type.
- PART 3: Churn risk register. Field label is fixed: "Retention intervention: [one concrete
  action that reduces reversion probability]" — not "Mitigation."
- PART 4: Interventions ranked by adoption delta.
- MECHANISM STATE: A single mandatory line appears immediately before ## VERIFICATION MODE.
  Write exactly one of:
    "CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered"
      (if no correction block has been produced yet in this document)
    "CORRECTION BLOCK fired — see Section [H/I/J]"
      (if a correction block was already generated above the verification boundary)
  This line proves the correction mechanism was available in the document body before SECTION K.
  It is required regardless of gate outcomes. It is not optional, not N/A, not omittable.
- Inline CORRECTION BLOCKS appear immediately after the gate that triggers them (Sections H,
  I, or J). Corrected content lives here — this is the C-19 location if any correction fires.
- SECTION K is the terminal gate state record. Every gate receives an explicit execution stamp
  regardless of outcome. "PASS — no correction triggered" is the required stamp for a passing
  gate — not optional, not N/A, not omittable. An empty execution stamp row is a SECTION K
  failure regardless of Final Result.
- ## VERIFICATION MODE header appears between MECHANISM STATE and SECTION H.

Self-verifying invariant (asserted in SECTION K):
  "For every 'Revision Performed: Yes' entry, a CORRECTION BLOCK with BEFORE and AFTER
   content exists earlier in this document at the CORRECTION BLOCK Location cited. Failure
   mode: a Yes row whose referenced CORRECTION BLOCK is absent or lacks a BEFORE field
   falsifies this invariant. An evaluator can confirm or refute this by inspection without
   relying on this assertion."

---

PART 1 — ROLE PROFILE AND DISPLACEMENT INERTIA

SECTION A — Role-to-Archetype Mapping

All 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). For each role, identify their
archetype and the specific belief or habit that gives them inertia toward THE INCUMBENT.

| Role    | Rogers Archetype | Investment in THE INCUMBENT (what they use it for) | Belief that creates inertia (why they'd hesitate) |
|---------|-----------------|---------------------------------------------------|---------------------------------------------------|
| PM      | [archetype]     | [specific current use]                            | [belief]                                          |
| UX      | [archetype]     | [specific current use]                            | [belief]                                          |
| C-01    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-02    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-03    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-04    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-05    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-06    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-07    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-08    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-09    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-10    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-11    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-12    | [archetype]     | [specific current use]                            | [belief]                                          |
| Support | [archetype]     | [specific current use]                            | [belief]                                          |
| SRE     | [archetype]     | [specific current use]                            | [belief]                                          |

SECTION B — Named Inertia IDs

One entry per archetype. Assign inertia IDs (I-01 through I-05) for downstream citation.

| Archetype      | Inertia ID | THE INCUMBENT Behavior They Protect | Why Abandoning It Is Costly (concrete, not generic) |
|----------------|-----------|-------------------------------------|-----------------------------------------------------|
| Innovators     | I-01      | [specific]                          | [cost]                                              |
| Early Adopters | I-02      | [specific]                          | [cost]                                              |
| Early Majority | I-03      | [specific]                          | [cost]                                              |
| Late Majority  | I-04      | [specific]                          | [cost]                                              |
| Laggards       | I-05      | [specific]                          | [cost]                                              |

---

PART 2 — PHASE-BY-PHASE ADOPTION SIMULATION

---

## PHASE 1 — INNOVATORS [Month 1–2]

Who are they (from SECTION A)?
What specifically pulls them away from THE INCUMBENT this early — before social proof exists?
Signal they generate: what observable behavior shows Early Adopters that someone left THE INCUMBENT?
After Phase 1: THE INCUMBENT is still the organizational default — but these roles have left it publicly.

---

## PHASE 2 — EARLY ADOPTERS [Month 2–4]

Who are they (from SECTION A)?
What made THE INCUMBENT feel optional (not yet a liability) for them specifically?

Champion network — name 2–3 roles now actively pulling Early Majority toward {{topic}}.
For each champion, answer each question — Q3 answer is the inertia ID itself, not a slot value:

Q1 — Who is this champion role?
Q2 — Why does their Rogers archetype position make them a credible bridge? (They have visibly
     left THE INCUMBENT; Early Majority roles can observe this directly.)
Q3 — Which Named Inertia ID from SECTION B is this champion positioned to overcome?
     (Answer with the ID — e.g., I-03 — then explain what makes this champion uniquely
     capable of countering that specific inertia for Early Majority roles.)
Q4 — How do they actively pull Early Majority toward {{topic}} — what do they do, specifically?

---

## PHASE 3 — CHASM [Month 4–6]

THIS IS A NON-ADOPTION PHASE. No new roles adopt during PHASE 3.

About THE INCUMBENT: [why it still feels safer than {{topic}} to Early Majority roles — not
generic "uncertainty," but the specific value it still delivers]

Which Named Inertia ID from SECTION B is driving the chasm — what specific behavior or belief
among Early Majority roles keeps THE INCUMBENT legitimate right now? (Answer with the inertia
ID — e.g., I-03 — then describe what that inertia looks like in practice for EM roles.)

What the chasm means for THE INCUMBENT's organizational position: [it retains active
legitimacy, not just passive habit — why]

Bridge conditions: [what specific artifact or event would cause an EM role to believe THE
INCUMBENT is becoming the exception rather than {{topic}}]

Sensitivity analysis — two named scenarios:

| Scenario    | Named Lever | Effect on THE INCUMBENT's Position     | Chasm Crossing Month   |
|-------------|------------|----------------------------------------|------------------------|
| Optimistic  | [lever]    | [weakens — Early Majority sees...]     | Month N                |
| Pessimistic | [lever]    | [strengthens — Early Majority sees...] | Month N or Not Crossed |

---

## PHASE 4 — EARLY MAJORITY [Month 6–10]

Who moves (from SECTION A)?
Which bridge condition from PHASE 3 landed for them specifically?
What made THE INCUMBENT feel like the exception rather than the default?
Which PHASE 2 champion's evidence did they act on — and why that format worked for this group?
After Phase 4: what happens to THE INCUMBENT's organizational position?

---

## PHASE 5 — LATE MAJORITY [Month 10–15]

Who are they (from SECTION A)?
What pushed them off THE INCUMBENT — not what made {{topic}} attractive, but what made staying
on THE INCUMBENT feel unsafe or embarrassing?
Mechanism: mandate / social proof / removal of THE INCUMBENT from the default path?

Signal readiness — 2 measurable thresholds:

| Signal              | Threshold                        | Interpretation               |
|---------------------|----------------------------------|------------------------------|
| [measurable signal] | [e.g., >=10 of 16 roles active]  | [proceed / pause / intervene]|
| [measurable signal] | [threshold]                      | [interpretation]             |

---

## PHASE 6 — LAGGARDS [Month 15+]

Who are they (from SECTION A)?
What's actually keeping them on THE INCUMBENT at this point — not inability, but active
preference?
Conversion path: what specific event forces the final adoption (mandate, removal, deprecation)?

---

TABLE 3 — Phase Transition Spread Mechanisms

One row per archetype-to-archetype transition. The spread mechanism column header is FIXED —
do not rename it. "Word-of-mouth," "organic growth," and "general awareness" are generic
descriptions incompatible with the column type declared in the header.

| Transition                          | Spread Mechanism: [named signal or artifact — not generic word-of-mouth] | Effect on THE INCUMBENT's Position |
|-------------------------------------|-------------------------------------------------------------------------|-----------------------------------|
| Innovators → Early Adopters         | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |
| Early Adopters → Early Majority     | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |
| Early Majority → Late Majority      | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |
| Late Majority → Laggards            | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |

---

PART 3 — CHURN RISK REGISTER

At least 2 archetype entries. Field labels below are fixed — do not rename them.

For each archetype at reversion risk:

Archetype:
Reversion trigger: [the specific event or condition that would send them back to THE INCUMBENT]
Named Inertia ID from SECTION B: [which inertia this reversion represents — cite I-0X]
Warning signal: [first observable sign of reversion — specific behavior, not a metric]
Retention intervention: [one concrete action that reduces reversion probability]

The "Retention intervention" field names what the team does (assign, train, remove, pair,
bundle, deprecate, etc.) — not a surveillance instruction (monitor / track / watch / observe).

---

PART 4 — INTERVENTIONS RANKED BY ADOPTION DELTA

At least 3 entries. Each entry cites at least one Named Inertia ID from SECTION B.
Rank in descending adoption delta order.

| Rank | Intervention | Named Inertia ID | Adoption Delta (H/M/L) | Rationale                       |
|------|-------------|-----------------|------------------------|---------------------------------|
| 1    | [action]    | I-0X            | [H/M/L]                | [why this moves the most roles] |
| 2    | [action]    | I-0X            | [H/M/L]                | [rationale]                     |
| 3    | [action]    | I-0X            | [H/M/L]                | [rationale]                     |

Delta scale: H = >20% monthly adoption rate increase; M = 10–20%; L = <10%.

---

MECHANISM STATE: Write exactly one of the following lines here, then proceed to
## VERIFICATION MODE:

  "CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered"
    Use this form if no correction block has been produced anywhere above this line.
    This proves the correction mechanism was present in the document body before SECTION K.

  "CORRECTION BLOCK fired — see Section [H/I/J]"
    Use this form if a correction block was already generated earlier in this document.

This line is required. It is not optional, not N/A, not omittable. An absent MECHANISM STATE
line means the mechanism's availability is unproven in the document body.

---

## VERIFICATION MODE

Content generation (PARTS 1–4 and TABLE 3) is complete. SECTIONS H through K are the audit
stage. Do not generate new content — verify and correct existing content only.

CORRECTION BLOCK format (use if any gate fails):
  CORRECTION BLOCK — [Criterion ID] — [Part/Section + row identifier]
  BEFORE — [Location, row]: [Reproduce the original content verbatim]
  AFTER — [Location, row]: [Write the corrected content in full]
  Gate re-run: [Confirm the corrected entry satisfies the pass condition]

Corrected content lives in this CORRECTION BLOCK (C-19 location).
SECTION K references this location but does NOT duplicate the content (C-21 rule).

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check: Do Named Inertia IDs from SECTION B appear explicitly in each downstream section?

- PHASE 3 (chasm — the inertia-ID answer to the question): Inertia ID present? [ ]
- PART 4 (interventions): Inertia ID per row? [ ]
- PHASE 2 (champion Q3 answers): Named Inertia ID per champion? [ ]
- PART 3 (churn register): Named Inertia ID per reversion-trigger entry? [ ]

Count: [N] of 4 sections contain explicit Inertia ID citations.
Gate H: [PASS if N >= 3 / FAIL if N < 3]
[If FAIL: CORRECTION BLOCK — C-13 here before SECTION I]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Review each champion entry in PHASE 2 (Q2 and Q3 answers):
- Q2 archetype position rationale present? [ ]
- Q3 Named Inertia ID answer present (the ID itself, not a placeholder)? [ ]

A champion entry where Q3 is unanswered or answered with a placeholder fails.
Gate I: [PASS if all entries have both Q2 and Q3 answered / FAIL if any entry is incomplete]
[If FAIL: CORRECTION BLOCK — C-14 per failing entry before SECTION J]

---

SECTION J — Gate: C-15 (Churn Interventions Are Concrete Actions)

Review each "Retention intervention" entry in PART 3:
- Names a concrete team action (assign, train, remove, pair, bundle, deprecate, etc.)? [ ]
- Solely surveillance language (monitor / track / watch / observe alone)? [ ]

A mitigation consisting only of surveillance language fails. Action + measurement passes.
Gate J: [PASS if all entries have concrete actions / FAIL if any entry is surveillance-only]
[If FAIL: CORRECTION BLOCK — C-15 per failing entry before SECTION K]

---

## SECTION K — Terminal Gate State Record

EXECUTION STAMP RULE: Every gate receives an explicit execution stamp before any other field
is recorded. Permitted stamps:
  - "PASS — no correction triggered" (gate passed on first attempt — record this explicitly)
  - "FAIL — correction triggered — see [Section H/I/J]" (correction block was produced)
An empty or missing Execution Stamp is a SECTION K failure regardless of Final Result.
This section records gate outcomes only. No CORRECTION BLOCK content appears here.

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the cited location.
Falsification condition: a Yes row whose CORRECTION BLOCK Location references a section
containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies
this invariant. An evaluator can confirm or refute this by inspection without relying on this
assertion.

| Criterion                           | Execution Stamp                                       | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-------------------------------------|------------------------------------------------------|---------------|--------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone  | [PASS — no correction triggered / FAIL — see Sec H]  | [PASS / FAIL] | [Yes / No]         | [Section H / N/A]        | [PASS]      |
| C-14 — Champion double-anchor       | [PASS — no correction triggered / FAIL — see Sec I]  | [PASS / FAIL] | [Yes / No]         | [Section I / N/A]        | [PASS]      |
| C-15 — Churn action test            | [PASS — no correction triggered / FAIL — see Sec J]  | [PASS / FAIL] | [Yes / No]         | [Section J / N/A]        | [PASS]      |
```

---

## V-02 — Single Axis: C-32 Per-Gate Anchor Footers

**Variation axis:** Phrasing register — a mandatory mechanism state line is appended to the body of each gate section (H, I, J) as the final item before the next section. Each footer names the specific gate: `CORRECTION BLOCK MECHANISM ARMED — H gate` or `CORRECTION BLOCK fired — see above`. This distributes the mechanism proof across three structural points in the document body rather than concentrating it at a single pre-verification location.

**Hypothesis:** Three per-gate mechanism anchors provide more redundant structural proof than a single pre-verification line. Any one of the three satisfies C-32 (mechanism proven in document body before SECTION K). The per-gate placement also tightens the causal link between the mechanism and the gate that invoked it — the anchor immediately follows the gate verdict, making the relationship between audit execution and mechanism availability explicit at the point of evaluation rather than ahead of it. C-29 (answer-form) and C-30 (execution stamps) remain from R10 V-05 baseline, making this variation the only one where three independent structural layers all prove audit execution: per-gate footers (C-32), SECTION K stamps (C-30), and CORRECTION BLOCKs where gates fail (C-19).

---

```
DISPLACEMENT DECLARATION (read before generating any output):

Every role on this team is currently doing something. That something is THE INCUMBENT — the
existing workflow, tool, or process that {{topic}} must displace. Name THE INCUMBENT explicitly
here before beginning PART 1. Every PHASE body will ask: what does this phase do to THE
INCUMBENT's position?

THE INCUMBENT for this topic: [name the current workflow, tool, or process being displaced —
specific enough that a role can be described as "protecting" or "having already left" it]

---

STRUCTURAL CONTRACT (read before generating any section):

- PART 1: Role assignment and named inertia (Sections A + B). All rationale runs through the
  displacement lens.
- PART 2: Phase-by-phase adoption simulation. PHASE 1–6 headers are structural — Rogers
  sequence violation is architecturally impossible. PHASE 3 CHASM is a non-adoption interstitial.
  Phase headers for PHASE 3 and PHASE 2 champion entries use answer-form questions: the inertia
  ID is the answer to the question, not a value in a fill-form slot. Omitting the ID leaves
  the question unanswered — not a blank field, but an incomplete sentence.
- TABLE 3: Phase Transition Spread Mechanisms — immediately after PART 2, before PART 3. Four
  named structural slots, one per canonical transition pair. The spread mechanism column header
  is fixed: "Spread Mechanism: [named signal or artifact — not generic word-of-mouth]".
- PART 3: Churn risk register. Field label is fixed: "Retention intervention: [one concrete
  action that reduces reversion probability]" — not "Mitigation."
- PART 4: Interventions ranked by adoption delta.
- Gate sections H, I, J each end with a mandatory MECHANISM ANCHOR line — the final item in
  the gate section body, before the next section begins. Two permitted forms:
    "CORRECTION BLOCK MECHANISM ARMED — [H/I/J] gate"
      (if this gate passed on first attempt — no correction block produced)
    "CORRECTION BLOCK fired — see above"
      (if a correction block was produced immediately above this line)
  The mechanism anchor line is required in every gate section. It is not optional, not N/A,
  not omittable. An absent anchor means the mechanism's availability is unproven at this gate.
- Inline CORRECTION BLOCKS appear immediately after the gate verdict (before the mechanism
  anchor) if the gate fails. Corrected content lives here.
- SECTION K is the terminal gate state record. Every gate receives an explicit execution stamp.
  "PASS — no correction triggered" is required for passing gates — not optional, not omittable.
- ## VERIFICATION MODE header appears between PART 4 and SECTION H.

Self-verifying invariant (asserted in SECTION K):
  "For every 'Revision Performed: Yes' entry, a CORRECTION BLOCK with BEFORE and AFTER
   content exists earlier in this document at the CORRECTION BLOCK Location cited. Failure
   mode: a Yes row whose referenced CORRECTION BLOCK is absent or lacks a BEFORE field
   falsifies this invariant. An evaluator can confirm or refute this by inspection without
   relying on this assertion."

---

PART 1 — ROLE PROFILE AND DISPLACEMENT INERTIA

SECTION A — Role-to-Archetype Mapping

All 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). For each role, identify their
archetype and the specific belief or habit that gives them inertia toward THE INCUMBENT.

| Role    | Rogers Archetype | Investment in THE INCUMBENT (what they use it for) | Belief that creates inertia (why they'd hesitate) |
|---------|-----------------|---------------------------------------------------|---------------------------------------------------|
| PM      | [archetype]     | [specific current use]                            | [belief]                                          |
| UX      | [archetype]     | [specific current use]                            | [belief]                                          |
| C-01    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-02    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-03    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-04    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-05    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-06    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-07    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-08    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-09    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-10    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-11    | [archetype]     | [specific current use]                            | [belief]                                          |
| C-12    | [archetype]     | [specific current use]                            | [belief]                                          |
| Support | [archetype]     | [specific current use]                            | [belief]                                          |
| SRE     | [archetype]     | [specific current use]                            | [belief]                                          |

SECTION B — Named Inertia IDs

One entry per archetype. Assign inertia IDs (I-01 through I-05) for downstream citation.

| Archetype      | Inertia ID | THE INCUMBENT Behavior They Protect | Why Abandoning It Is Costly (concrete, not generic) |
|----------------|-----------|-------------------------------------|-----------------------------------------------------|
| Innovators     | I-01      | [specific]                          | [cost]                                              |
| Early Adopters | I-02      | [specific]                          | [cost]                                              |
| Early Majority | I-03      | [specific]                          | [cost]                                              |
| Late Majority  | I-04      | [specific]                          | [cost]                                              |
| Laggards       | I-05      | [specific]                          | [cost]                                              |

---

PART 2 — PHASE-BY-PHASE ADOPTION SIMULATION

---

## PHASE 1 — INNOVATORS [Month 1–2]

Who are they (from SECTION A)?
What specifically pulls them away from THE INCUMBENT this early — before social proof exists?
Signal they generate: what observable behavior shows Early Adopters that someone left THE INCUMBENT?
After Phase 1: THE INCUMBENT is still the organizational default — but these roles have left it publicly.

---

## PHASE 2 — EARLY ADOPTERS [Month 2–4]

Who are they (from SECTION A)?
What made THE INCUMBENT feel optional (not yet a liability) for them specifically?

Champion network — name 2–3 roles now actively pulling Early Majority toward {{topic}}.
For each champion, answer each question — Q3 answer is the inertia ID itself, not a slot value:

Q1 — Who is this champion role?
Q2 — Why does their Rogers archetype position make them a credible bridge? (They have visibly
     left THE INCUMBENT; Early Majority roles can observe this directly.)
Q3 — Which Named Inertia ID from SECTION B is this champion positioned to overcome?
     (Answer with the ID — e.g., I-03 — then explain what makes this champion uniquely
     capable of countering that specific inertia for Early Majority roles.)
Q4 — How do they actively pull Early Majority toward {{topic}} — what do they do, specifically?

---

## PHASE 3 — CHASM [Month 4–6]

THIS IS A NON-ADOPTION PHASE. No new roles adopt during PHASE 3.

About THE INCUMBENT: [why it still feels safer than {{topic}} to Early Majority roles — not
generic "uncertainty," but the specific value it still delivers]

Which Named Inertia ID from SECTION B is driving the chasm — what specific behavior or belief
among Early Majority roles keeps THE INCUMBENT legitimate right now? (Answer with the inertia
ID — e.g., I-03 — then describe what that inertia looks like in practice for EM roles.)

What the chasm means for THE INCUMBENT's organizational position: [it retains active
legitimacy, not just passive habit — why]

Bridge conditions: [what specific artifact or event would cause an EM role to believe THE
INCUMBENT is becoming the exception rather than {{topic}}]

Sensitivity analysis — two named scenarios:

| Scenario    | Named Lever | Effect on THE INCUMBENT's Position     | Chasm Crossing Month   |
|-------------|------------|----------------------------------------|------------------------|
| Optimistic  | [lever]    | [weakens — Early Majority sees...]     | Month N                |
| Pessimistic | [lever]    | [strengthens — Early Majority sees...] | Month N or Not Crossed |

---

## PHASE 4 — EARLY MAJORITY [Month 6–10]

Who moves (from SECTION A)?
Which bridge condition from PHASE 3 landed for them specifically?
What made THE INCUMBENT feel like the exception rather than the default?
Which PHASE 2 champion's evidence did they act on — and why that format worked for this group?
After Phase 4: what happens to THE INCUMBENT's organizational position?

---

## PHASE 5 — LATE MAJORITY [Month 10–15]

Who are they (from SECTION A)?
What pushed them off THE INCUMBENT — not what made {{topic}} attractive, but what made staying
on THE INCUMBENT feel unsafe or embarrassing?
Mechanism: mandate / social proof / removal of THE INCUMBENT from the default path?

Signal readiness — 2 measurable thresholds:

| Signal              | Threshold                        | Interpretation               |
|---------------------|----------------------------------|------------------------------|
| [measurable signal] | [e.g., >=10 of 16 roles active]  | [proceed / pause / intervene]|
| [measurable signal] | [threshold]                      | [interpretation]             |

---

## PHASE 6 — LAGGARDS [Month 15+]

Who are they (from SECTION A)?
What's actually keeping them on THE INCUMBENT at this point — not inability, but active
preference?
Conversion path: what specific event forces the final adoption (mandate, removal, deprecation)?

---

TABLE 3 — Phase Transition Spread Mechanisms

One row per archetype-to-archetype transition. The spread mechanism column header is FIXED —
do not rename it. "Word-of-mouth," "organic growth," and "general awareness" are generic
descriptions incompatible with the column type declared in the header.

| Transition                          | Spread Mechanism: [named signal or artifact — not generic word-of-mouth] | Effect on THE INCUMBENT's Position |
|-------------------------------------|-------------------------------------------------------------------------|-----------------------------------|
| Innovators → Early Adopters         | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |
| Early Adopters → Early Majority     | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |
| Early Majority → Late Majority      | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |
| Late Majority → Laggards            | [named signal or artifact]                                               | [THE INCUMBENT loses...]          |

---

PART 3 — CHURN RISK REGISTER

At least 2 archetype entries. Field labels below are fixed — do not rename them.

For each archetype at reversion risk:

Archetype:
Reversion trigger: [the specific event or condition that would send them back to THE INCUMBENT]
Named Inertia ID from SECTION B: [which inertia this reversion represents — cite I-0X]
Warning signal: [first observable sign of reversion — specific behavior, not a metric]
Retention intervention: [one concrete action that reduces reversion probability]

The "Retention intervention" field names what the team does (assign, train, remove, pair,
bundle, deprecate, etc.) — not a surveillance instruction (monitor / track / watch / observe).

---

PART 4 — INTERVENTIONS RANKED BY ADOPTION DELTA

At least 3 entries. Each entry cites at least one Named Inertia ID from SECTION B.
Rank in descending adoption delta order.

| Rank | Intervention | Named Inertia ID | Adoption Delta (H/M/L) | Rationale                       |
|------|-------------|-----------------|------------------------|---------------------------------|
| 1    | [action]    | I-0X            | [H/M/L]                | [why this moves the most roles] |
| 2    | [action]    | I-0X            | [H/M/L]                | [rationale]                     |
| 3    | [action]    | I-0X            | [H/M/L]                | [rationale]                     |

Delta scale: H = >20% monthly adoption rate increase; M = 10–20%; L = <10%.

---

## VERIFICATION MODE

Content generation (PARTS 1–4 and TABLE 3) is complete. SECTIONS H through K are the audit
stage. Do not generate new content — verify and correct existing content only.

CORRECTION BLOCK format (use if any gate fails):
  CORRECTION BLOCK — [Criterion ID] — [Part/Section + row identifier]
  BEFORE — [Location, row]: [Reproduce the original content verbatim]
  AFTER — [Location, row]: [Write the corrected content in full]
  Gate re-run: [Confirm the corrected entry satisfies the pass condition]

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check: Do Named Inertia IDs from SECTION B appear explicitly in each downstream section?

- PHASE 3 (chasm — the inertia-ID answer to the question): Inertia ID present? [ ]
- PART 4 (interventions): Inertia ID per row? [ ]
- PHASE 2 (champion Q3 answers): Named Inertia ID per champion? [ ]
- PART 3 (churn register): Named Inertia ID per reversion-trigger entry? [ ]

Count: [N] of 4 sections contain explicit Inertia ID citations.
Gate H: [PASS if N >= 3 / FAIL if N < 3]
[If FAIL: CORRECTION BLOCK — C-13 here, then proceed to mechanism anchor]

MECHANISM ANCHOR — H gate: Write exactly one of:
  "CORRECTION BLOCK MECHANISM ARMED — H gate"  (if gate H passed on first attempt)
  "CORRECTION BLOCK fired — see above"           (if a correction block was produced above)
This line is required. It is not optional, not N/A, not omittable.

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Review each champion entry in PHASE 2 (Q2 and Q3 answers):
- Q2 archetype position rationale present? [ ]
- Q3 Named Inertia ID answer present (the ID itself, not a placeholder)? [ ]

A champion entry where Q3 is unanswered or answered with a placeholder fails.
Gate I: [PASS if all entries have both Q2 and Q3 answered / FAIL if any entry is incomplete]
[If FAIL: CORRECTION BLOCK — C-14 per failing entry, then proceed to mechanism anchor]

MECHANISM ANCHOR — I gate: Write exactly one of:
  "CORRECTION BLOCK MECHANISM ARMED — I gate"  (if gate I passed on first attempt)
  "CORRECTION BLOCK fired — see above"           (if a correction block was produced above)
This line is required. It is not optional, not N/A, not omittable.

---

SECTION J — Gate: C-15 (Churn Interventions Are Concrete Actions)

Review each "Retention intervention" entry in PART 3:
- Names a concrete team action (assign, train, remove, pair, bundle, deprecate, etc.)? [ ]
- Solely surveillance language (monitor / track / watch / observe alone)? [ ]

A mitigation consisting only of surveillance language fails. Action + measurement passes.
Gate J: [PASS if all entries have concrete actions / FAIL if any entry is surveillance-only]
[If FAIL: CORRECTION BLOCK — C-15 per failing entry, then proceed to mechanism anchor]

MECHANISM ANCHOR — J gate: Write exactly one of:
  "CORRECTION BLOCK MECHANISM ARMED — J gate"  (if gate J passed on first attempt)
  "CORRECTION BLOCK fired — see above"           (if a correction block was produced above)
This line is required. It is not optional, not N/A, not omittable.

---

## SECTION K — Terminal Gate State Record

EXECUTION STAMP RULE: Every gate receives an explicit execution stamp before any other field
is recorded. Permitted stamps:
  - "PASS — no correction triggered"
  - "FAIL — correction triggered — see [Section H/I/J]"
An empty or missing Execution Stamp is a SECTION K failure regardless of Final Result.
This section records gate outcomes only. No CORRECTION BLOCK content appears here.

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the cited location.
Falsification condition: a Yes row whose CORRECTION BLOCK Location references a section
containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies
this invariant. An evaluator can confirm or refute this by inspection without relying on this
assertion.

| Criterion                           | Execution Stamp                                       | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-------------------------------------|------------------------------------------------------|---------------|--------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone  | [PASS — no correction triggered / FAIL — see Sec H]  | [PASS / FAIL] | [Yes / No]         | [Section H / N/A]        | [PASS]      |
| C-14 — Champion double-anchor       | [PASS — no correction triggered / FAIL — see Sec I]  | [PASS / FAIL] | [Yes / No]         | [Section I / N/A]        | [PASS]      |
| C-15 — Churn action test            | [PASS — no correction triggered / FAIL — see Sec J]  | [PASS / FAIL] | [Yes / No]         | [Section J / N/A]        | [PASS]      |
```

---

V-01 and V-02 complete. V-03 through V-05 next — say "continue" to get them.
