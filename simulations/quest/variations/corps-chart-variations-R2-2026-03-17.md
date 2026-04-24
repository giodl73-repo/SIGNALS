Now I have everything I need. Round 1 variations are clear; Round 2 needs to target the two new criteria: C-11 (role-grounded Rebuttal with measurable re-assessment trigger) and C-12 (role-name coherence across the full document — diagram, rhythm table, charters, inertia sub-sections).

---

# Quest Variate — corps-chart (Round 2)

Five complete, runnable skill body variations targeting the new aspirational criteria C-11 and C-12 while preserving the full R1 structural contract.

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Role Name Lock (C-12) | Declaring an explicit locked role-name set immediately after classification, and annotating each downstream section with a "check lock" reminder, closes the role-drift surface at the DRI/Owner and charter Membership columns without adding instruction weight to the Inertia section |
| V-02 | Rebuttal Case Template (C-11) | Restructuring the Rebuttal sub-section as a four-field case form (Role Under Pressure / Observable Breakdown / Why Existing Mechanisms Fail / Re-Assessment Trigger) forces the model to name a loaded role before it can write the failure description, eliminating generic growth projections |
| V-03 | Lifecycle emphasis — Inertia as weight-bearing section | Giving the Inertia Assessment ~50% of total instruction space and explicitly labeling it the most consequential section of the output produces better C-11 specificity at the cost of tighter downstream sections |
| V-04 | V-01 + V-02 (Role Lock + Rebuttal Case) | Combining the post-classification name lock with the mandatory rebuttal case form targets both C-11 and C-12 simultaneously without adding format contract overhead |
| V-05 | V-04 + R1-V-05 base (Full integration) | Format contract declared upfront (from R1 V-05) + inertia-led framing (from R1 V-02) + Role Name Lock (V-01) + Rebuttal Case Template (V-02) — the most comprehensive variation; tests whether full integration produces cleaner output or over-specifies |

---

## V-01 — Role Name Lock (targeting C-12)

**Axis**: After classification, an explicit ROLE-NAME LOCK block is emitted containing the complete set of permitted role names. Every downstream section that can introduce role names (diagram, rhythm table DRI/Owner, charter Membership/Decides, inertia sub-sections) carries an inline lock-check reminder.

**Hypothesis**: Role drift at the DRI/Owner column and charter Membership fields is caused by the model generating contextually plausible role names rather than looking up loaded names. A visible locked set, emitted before any downstream content, acts as a write-once reference that the model checks against before producing each name. C-12 pass rate should improve without touching Inertia depth (C-11 unchanged as baseline).

---

You are running `/org-chart {topic}`.

STEP 1 — LOAD ROLES

Read `.roles/`. Produce a `ROLES-LOADED:` block listing every role found, one per line: `- [role name] — [one-line description from role file]`.

If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` followed by inferred roles in the same format.

DO NOT write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`.

Tier order: Engineering first, then Operations, then PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No role may appear in classification that was absent from the loaded block.

After completing classification, emit the following lock block verbatim, substituting the actual role names:

```
ROLE-NAME LOCK: The following role names are the only names permitted anywhere in this document after this point.
[list every classified role name, one per line]
Any role name not in this list must not appear in the diagram, rhythm table, charter fields, or inertia sub-sections.
```

Then emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

Before drawing any org boxes, work through the question: could this team operate effectively without formal structure? Four sub-sections in this exact order.

**Sub-section 1 — Case for Staying Flat**

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`. Minimum two data rows. Type values from closed vocabulary only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

After writing the rows, count them (header excluded). Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

DO NOT begin Sub-section 2 before this separator.

**Sub-section 2 — How We Coordinate Today**

Describe the coordination patterns currently in active use: channels, cadences, informal roles, artifacts, with frequency and participants. Do not re-list mechanism rows from Sub-section 1.

**Sub-section 3 — Rebuttal**

Name the coordination failure that the flat-team case cannot answer. Reference a specific observable — a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap. Identify which role or roles from ROLES-LOADED are the failure agents — who specifically cannot escalate, cannot decide, or cannot coordinate across the gap.

Do not write "the team is growing" unless you name what specifically breaks and which role is stuck when it does.

**Sub-section 4 — VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`

Rating from closed set only: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line. Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name in the reasoning sentence.

Write a re-assessment trigger naming a concrete threshold — a specific headcount number, a named milestone event, or a structural symptom. Do not write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

**[ROLE-NAME LOCK CHECK: All role names in this diagram must appear in the ROLE-NAME LOCK block. Do not introduce new names.]**

Draw an ASCII hierarchy with at least two levels. Committees as distinct labeled nodes, not embedded in area boxes. Role names must match ROLES-LOADED or ROLES-NOTE exactly.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA

Table with five columns: `Area | Headcount | Key Roles | Decides | Escalates`. DO NOT merge Decides and Escalates.

- Key Roles: `[role name] ([domain type])` — role name must be in ROLE-NAME LOCK
- Decides: decision types owned at this level
- Escalates: decision types referred upward, naming the destination

Minimum two area rows plus `**Total**` row with sum.

STEP 6 — OPERATING RHYTHM TABLE

**[ROLE-NAME LOCK CHECK: DRI / Owner column must use only role names from the ROLE-NAME LOCK block.]**

Columns: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three distinct rows: (a) ROB, (b) shiproom or gate, (c) governance meeting. Do not merge two meetings into one row.

STEP 7 — COMMITTEE CHARTERS

**[ROLE-NAME LOCK CHECK: Membership and Decides fields must use only role names from the ROLE-NAME LOCK block.]**

Charter for every governance meeting in the rhythm table. All five fields required:

- `Purpose`
- `Membership` — minimum two roles as `[role name] ([domain type])`; each name must be in ROLE-NAME LOCK
- `Decides`
- `Escalates` — named destination; do not write "everything not listed under Decides"
- `Quorum: [N] of [M] member roles required for binding decisions`

Fraction format (N of M) is required. Short form `N roles required` is not accepted.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` block with all four categories populated:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

No category may be empty or missing.

STEP 9 — ORG EVOLUTION ROADMAP

Trigger table: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal, structural symptom, or milestone event). Two headcount thresholds do not satisfy this requirement.

STEP 10 — ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows. Every `Why It Applies Here` cell opens with: `[element name] (cat-N) — [one sentence]` using a valid cat-N from the ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-02 — Rebuttal Case Template (targeting C-11)

**Axis**: The Rebuttal sub-section is replaced with a mandatory four-field case form. The model must complete all four fields in order before writing the VERDICT; it cannot proceed without naming a loaded role in field 1.

**Hypothesis**: The generic "as we scale" failure mode appears because the Rebuttal is written as prose with an implicit structure. A mandatory labeled form with a role field that must be filled before a breakdown field can be written forces role-grounding as a structural precondition, not an optional elaboration. C-11 pass rate should improve; C-12 impact is neutral (the lock is not added here).

---

You are running `/org-chart {topic}`.

STEP 1 — LOAD ROLES

Read `.roles/`. Produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role. If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles in the same format.

DO NOT write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`.

Tier order: Engineering first, then Operations, then PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No unloaded role may appear in classification.

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

Four sub-sections in this exact order.

**Sub-section 1 — Case for Staying Flat**

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`. Minimum two data rows. Type values: `Channel / Informal Role / Recurring Cadence / Shared Artifact` only.

Count the data rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

DO NOT begin Sub-section 2 before this separator.

**Sub-section 2 — How We Coordinate Today**

Inventory active coordination patterns — channels, cadences, informal roles, artifacts with frequency and participants. Do not re-list mechanism rows from Sub-section 1.

**Sub-section 3 — Rebuttal**

Complete the following case form. All four fields are required. Do not proceed to Sub-section 4 until all fields are present.

```
ROLE UNDER PRESSURE: [name exactly one role from ROLES-LOADED whose coordination failure motivates structure]

OBSERVABLE BREAKDOWN: [describe the specific failure this role experiences — a blocked decision this role cannot resolve, a missed SLA this role cannot prevent, a dependency this role has no escalation path for, or a knowledge silo this role is isolated from. Must be observable now or at a named near threshold — not a future growth projection.]

WHY EXISTING MECHANISMS FAIL: [name the specific mechanism(s) from Sub-section 1 that this role already uses, and explain exactly why they are insufficient to prevent the breakdown described above]

RE-ASSESSMENT TRIGGER: [name the exact measurable condition that would flip the verdict — a specific headcount (e.g., "when team exceeds 8 ICs"), a named milestone event (e.g., "first external partner integration"), or a structural symptom (e.g., "two or more ship dates missed and post-mortem attributes cause to cross-area misalignment"). Do not write "revisit as the team grows."]
```

**Sub-section 4 — VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and the OBSERVABLE BREAKDOWN from Sub-section 3]`

Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line. Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name. Reference the ROLE UNDER PRESSURE from Sub-section 3 in the reasoning sentence. Confirm the RE-ASSESSMENT TRIGGER from Sub-section 3 as the closing statement of this sub-section.

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

Draw an ASCII hierarchy with at least two levels. Committees as distinct labeled nodes, not embedded in area boxes. Role names must match ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA

Five columns: `Area | Headcount | Key Roles | Decides | Escalates`. DO NOT merge Decides and Escalates into a single column.

- Key Roles: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION
- Decides: decision types owned at this area
- Escalates: decision types referred upward — name destination role or forum

Minimum two area rows plus `**Total**` row with sum.

STEP 6 — OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three distinct rows: (a) ROB, (b) shiproom or gate, (c) governance meeting. Do not merge two meetings into one row. Reference a role from ROLES-LOADED in the DRI / Owner column.

STEP 7 — COMMITTEE CHARTERS

Charter for every governance meeting in the rhythm table. All five fields required:

- `Purpose`
- `Membership` — minimum two roles as `[role name] ([domain type])`
- `Decides`
- `Escalates` — named destination; not "everything not listed under Decides"
- `Quorum: [N] of [M] member roles required for binding decisions`

Fraction format (N of M) required. Short form `N roles required` is not accepted.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` block, all four categories populated:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

No category may be empty or missing.

STEP 9 — ORG EVOLUTION ROADMAP

Trigger table: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different category — workload signal, structural symptom, or milestone event. Two headcount thresholds do not satisfy this requirement.

STEP 10 — ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows. Every `Why It Applies Here` cell opens with: `[element name] (cat-N) — [one sentence]` using a valid cat-N from the ORG-ELEMENT REGISTER. No element cited without typed syntax.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-03 — Lifecycle Emphasis (Inertia as Weight-Bearing Section)

**Axis**: Lifecycle emphasis — the Inertia Assessment receives ~50% of total instruction space and is explicitly labeled the most important section; structure and downstream sections are terse by comparison.

**Hypothesis**: When instruction space is roughly equal across sections, the model allocates roughly equal output quality. Concentrating instruction depth on the Inertia Assessment signals where quality effort should go, producing richer C-06 and C-11 content. Downstream sections (headcount, rhythm, charters) have low failure rates in R1 and can tolerate terse instructions without score loss.

---

You are running `/org-chart {topic}`.

STEP 1 — LOAD ROLES

Read `.roles/`. Produce a `ROLES-LOADED:` block: `- [role name] — [one-line description]` per role. No files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles in same format. Nothing else before this block.

STEP 2 — CLASSIFY ROLES

After ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`. Tier order: Engineering → Operations → PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role classified; no unloaded role classified.

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

---

STEP 3 — INERTIA ASSESSMENT

**This is the most consequential section of this output.** The quality of the org design argument depends entirely on how well this section answers the question: does this team need formal structure, or is flat coordination sufficient? Work through all four sub-sections with full specificity. Structural claims made here must be grounded in the actual roles loaded above — not in generic team patterns.

**Sub-section 3a — Case for Staying Flat**

Build the strongest honest case for remaining flat. The goal is to enumerate every real coordination mechanism this team actually uses, not to argue for structure.

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.

Each row must describe a specific, observable mechanism — name the channel, the person or role who owns it, and how frequently it runs. Type values from closed vocabulary only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

Minimum two data rows. Rows that name specific roles from ROLES-LOADED are stronger evidence than generic descriptions.

After writing the rows, count them (header excluded). Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

DO NOT begin Sub-section 3b before this separator.

**Sub-section 3b — How We Coordinate Today**

This is the inventory of what is actually running — the status quo that any structure would displace. Name channels, cadences, informal roles, and shared artifacts with frequency and participants. Include roles from ROLES-LOADED where they act as de facto coordinators or information hubs. Do not re-list rows from Sub-section 3a.

**Sub-section 3c — Rebuttal**

This sub-section must do argumentative work. The goal is to identify the specific failure mode that the flat-case mechanisms in Sub-sections 3a and 3b cannot prevent.

Quality requirements for this sub-section:

1. **Name the role under pressure**: Identify the specific role from ROLES-LOADED that is at the center of the coordination failure. Who specifically lacks an escalation path, cannot get a decision, or is caught at an interface where two areas compete?

2. **Name the observable breakdown**: Describe what actually fails — a decision that blocks for more than N days, an SLA that is structurally unmeetable with current coordination, a roadmap conflict that has no resolution forum, or a knowledge silo that is forming around a specific role. The failure must be observable now or at a named near threshold.

3. **Explain why existing mechanisms cannot resolve it**: Name the specific mechanism from Sub-section 3a that this role already relies on, and explain exactly why it is insufficient. "The Weekly sync run by [role] does not give [other role] authority to unblock cross-area dependencies" is a real explanation. "Coordination will become harder" is not.

If you cannot name a specific, observable failure grounded in a loaded role, state that clearly. Do not invent a rebuttal.

**Sub-section 3d — VERDICT**

Open with the pressure rating — a quantified assessment of how strong the flat-team case was:

`FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 3a mechanism count and the specific observable failure from Sub-section 3c]`

Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line.

Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. The reasoning sentence must reference FLAT-CASE-PRESSURE by name and explain how the Sub-section 3c rebuttal overcame (or failed to overcome) it.

Write a re-assessment trigger. This must be a concrete, measurable threshold: a specific headcount number, a named milestone event, or a structural symptom that can be observed without ambiguity (e.g., "two or more ship dates missed and post-mortem attributes cause to cross-area coordination failure"). Do not write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

---

STEP 4 — ASCII ORG DIAGRAM. At least two levels. Committees as distinct labeled nodes. Role names match ROLES-LOADED.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA. Five columns: `Area | Headcount | Key Roles | Decides | Escalates`. Two separate columns for Decides and Escalates. Key Roles: `[role name] ([domain type])`. Min two area rows + `**Total**` row.

STEP 6 — OPERATING RHYTHM TABLE. Columns: `Cadence | Frequency | DRI / Owner | Purpose`. Min three rows: ROB + shiproom/gate + governance. No merged rows. DRI / Owner: loaded role where possible.

STEP 7 — COMMITTEE CHARTERS. One charter per governance meeting. Five fields: `Purpose` / `Membership` (min two roles as `[role name] ([domain type])`) / `Decides` / `Escalates` (named destination) / `Quorum: [N] of [M] member roles required for binding decisions`. Fraction format required.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER. All four categories: `cat-1 (Areas)` / `cat-2 (Committees/Cadences)` / `cat-3 (Headcount)` / `cat-4 (DRI Roles)`. No category empty.

STEP 9 — ORG EVOLUTION ROADMAP. `Trigger | Structural Change | Type`. Min two rows. Row 1: headcount threshold. Row 2: different category.

STEP 10 — ANTI-PATTERN WATCH. `Anti-Pattern | Why It Applies Here | Mitigation`. Min two rows. `Why It Applies Here` opens with `[element name] (cat-N) —` from ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-04 — Combined: Role Name Lock + Rebuttal Case Template

**Axes**: V-01 (Role Name Lock post-classification) + V-02 (Rebuttal Case form)

**Hypothesis**: C-11 and C-12 are independent failure surfaces — the Rebuttal sub-section and the downstream role name cells. V-01 alone fixes C-12 without touching C-11. V-02 alone fixes C-11 without touching C-12. Combining them should pass both aspirational criteria in a single variation without the complexity of a full format contract.

---

You are running `/org-chart {topic}`.

STEP 1 — LOAD ROLES

Read `.roles/`. Produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role found. If no files: `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles in the same format. Nothing else before this block.

STEP 2 — CLASSIFY ROLES

After ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`. Tier order: Engineering → Operations → PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No unloaded role may appear.

After completing classification, emit the following block verbatim, substituting actual role names:

```
ROLE-NAME LOCK
Permitted role names for all sections below:
[list every classified role name, one per line]
This list is closed. No role name may appear in the diagram, rhythm table DRI/Owner column,
committee charter Membership or Decides fields, or any inertia sub-section unless it is listed above.
```

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

Four sub-sections in this order.

**Sub-section 1 — Case for Staying Flat**

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`. Min two data rows. Type from closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`. At least one row must name a specific role from ROLES-LOADED in the Mechanism Name or Frequency / Participants column.

Count data rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

DO NOT begin Sub-section 2 before this separator.

**Sub-section 2 — How We Coordinate Today**

Inventory active coordination patterns — channels, cadences, informal roles, artifacts with frequency and participants. Do not re-list rows from Sub-section 1.

**Sub-section 3 — Rebuttal**

Complete all four fields of this case form before proceeding to Sub-section 4:

```
ROLE UNDER PRESSURE: [exactly one role name from the ROLE-NAME LOCK]

OBSERVABLE BREAKDOWN: [the specific failure this role experiences — a blocked decision, missed SLA, knowledge silo, or competing roadmap dependency. Observable now or at a named near threshold. Not a growth projection.]

WHY EXISTING MECHANISMS FAIL: [name the mechanism from Sub-section 1 this role uses, and explain exactly why it cannot prevent the breakdown above]

RE-ASSESSMENT TRIGGER: [the exact measurable condition that flips the verdict — specific headcount, named milestone event, or structural symptom with observable criteria. Not "revisit as the team grows."]
```

**Sub-section 4 — VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and the OBSERVABLE BREAKDOWN from Sub-section 3]`

Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line. Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name. Confirm the RE-ASSESSMENT TRIGGER from Sub-section 3 as the final sentence of this sub-section.

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

**[ROLE-NAME LOCK CHECK: All role names here must be in the ROLE-NAME LOCK block.]**

Draw ASCII hierarchy with at least two levels. Committees as distinct labeled nodes, not embedded in area boxes.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA

Five columns: `Area | Headcount | Key Roles | Decides | Escalates`. DO NOT merge Decides and Escalates.

- Key Roles: `[role name] ([domain type])` — names from ROLE-NAME LOCK only
- Decides: decision types owned at this level
- Escalates: decision types referred upward, naming destination

Min two area rows plus `**Total**` row.

STEP 6 — OPERATING RHYTHM TABLE

**[ROLE-NAME LOCK CHECK: DRI / Owner column — names from ROLE-NAME LOCK only.]**

Columns: `Cadence | Frequency | DRI / Owner | Purpose`. Min three distinct rows: ROB + shiproom/gate + governance. No merged rows.

STEP 7 — COMMITTEE CHARTERS

**[ROLE-NAME LOCK CHECK: Membership and Decides fields — names from ROLE-NAME LOCK only.]**

Charter for every governance meeting. Five fields:

- `Purpose`
- `Membership` — min two roles as `[role name] ([domain type])`; all from ROLE-NAME LOCK
- `Decides`
- `Escalates` — named destination, not "everything not listed under Decides"
- `Quorum: [N] of [M] member roles required for binding decisions` (fraction format required)

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` block, all four categories:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

No category empty or missing.

STEP 9 — ORG EVOLUTION ROADMAP

`Trigger | Structural Change | Type`. Min two rows. Row 1: headcount threshold. Row 2: different category. Two headcount thresholds do not satisfy this.

STEP 10 — ANTI-PATTERN WATCH

`Anti-Pattern | Why It Applies Here | Mitigation`. Min two rows. `Why It Applies Here` opens with `[element name] (cat-N) — [one sentence]` using valid cat-N from ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-05 — Full Integration: Format Contract + Inertia-Led + Role Lock + Rebuttal Case

**Axes**: R1-V-05 format contract declared upfront + R1-V-02 inertia-led framing (structure must earn its place) + V-01 Role Name Lock + V-02 Rebuttal Case form

**Hypothesis**: R1-V-05's format contract eliminated the most common downstream format failures (merged Decides/Escalates, short-form Quorum). Adding the Role Name Lock prevents role drift that the format contract did not address. The Rebuttal Case form prevents the generic growth-projection failure that survived R1. Combined, this variation targets the complete failure surface across all twelve criteria. Risk is over-specification: if the format contract competes with the role lock for attention, one may be ignored.

---

You are running `/org-chart {topic}`.

FORMAT CONTRACT — READ BEFORE WRITING ANYTHING

All tables and structured blocks must match these schemas exactly. Refer to this section before writing each element.

```
TABLE A — Mechanism Evidence (Inertia, Sub-section 1)
Columns: Mechanism Name | Type | Frequency / Participants
Type closed vocabulary: Channel / Informal Role / Recurring Cadence / Shared Artifact
Min: 2 data rows
At least 1 row must name a loaded role in Mechanism Name or Frequency / Participants

CASE FORM B — Rebuttal (Inertia, Sub-section 3)
Four mandatory fields:
  ROLE UNDER PRESSURE: [role name from ROLE-NAME LOCK]
  OBSERVABLE BREAKDOWN: [specific observable failure, now or at named near threshold]
  WHY EXISTING MECHANISMS FAIL: [named mechanism + reason]
  RE-ASSESSMENT TRIGGER: [concrete threshold — not "revisit as the team grows"]

TABLE C — Headcount by Area
Columns: Area | Headcount | Key Roles | Decides | Escalates
NOTE: Decides and Escalates are TWO separate columns. NEVER merge as "Decision Scope".
Key Roles: [role name] ([domain type]) — names from ROLE-NAME LOCK only
Min: 2 area rows + 1 Total row

TABLE D — Operating Rhythm
Columns: Cadence | Frequency | DRI / Owner | Purpose
Min: 3 distinct rows (ROB + shiproom/gate + governance meeting)
DRI / Owner: names from ROLE-NAME LOCK only
Never combine two meetings into one row

TABLE E — Committee Charter (one block per governance meeting)
Fields: Purpose / Membership / Decides / Escalates / Quorum
Membership: [role name] ([domain type]), min 2 roles, names from ROLE-NAME LOCK only
Escalates: named destination — never "everything not in Decides"
Quorum: Quorum: [N] of [M] member roles required for binding decisions
NOTE: Fraction format (N of M) required. Short form "N roles required" NOT accepted.

TABLE F — Org Evolution Roadmap
Columns: Trigger | Structural Change | Type
Min: 2 rows — Row 1 = headcount threshold, Row 2 = different category

TABLE G — Anti-Pattern Watch
Columns: Anti-Pattern | Why It Applies Here | Mitigation
Min: 2 rows
Why It Applies Here: [element name] (cat-N) — [one sentence]
(cat-N) must be a valid code from the ORG-ELEMENT REGISTER
```

OPENING FRAME: STRUCTURE MUST EARN ITS PLACE

Formal org structure is expensive — coordination overhead, decision latency, maintenance cost. Flat coordination wins by default. For structure to be warranted, it must answer a specific, role-grounded failure the flat team cannot resolve.

This skill works through that question before drawing any boxes.

STEP 1 — LOAD ROLES

Read `.roles/`. Produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role. If no files: `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles in the same format. Nothing else before this block.

STEP 2 — CLASSIFY ROLES

After ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`. Tier order: Engineering → Operations → PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No unloaded role may appear.

After classification, emit the following block verbatim, substituting actual role names:

```
ROLE-NAME LOCK
Permitted role names for all sections below (diagram, rhythm table, charters, inertia sub-sections):
[list every classified role name, one per line]
This list is closed. No role name may appear in any section below unless it is listed above.
```

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

The flat team wins until proven otherwise. Four sub-sections determine whether structure can beat it.

**Sub-section 3a — Case for Staying Flat (use TABLE A)**

Produce TABLE A (see Format Contract). Build the strongest possible case for remaining flat. Each row must be a specific, observable mechanism — not aspirational. At least one row must name a loaded role.

Count data rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

DO NOT begin Sub-section 3b before this separator.

**Sub-section 3b — How We Coordinate Today**

Inventory active coordination patterns. Name channels, cadences, informal roles, artifacts with frequency and participants. Do not re-list TABLE A rows.

**Sub-section 3c — Rebuttal (use CASE FORM B)**

Complete CASE FORM B (see Format Contract). All four fields required. The ROLE UNDER PRESSURE field must be completed before the OBSERVABLE BREAKDOWN field. The RE-ASSESSMENT TRIGGER must be a measurable concrete threshold — not "revisit as the team grows."

If you cannot name a specific, observable failure tied to a loaded role, state that clearly. Do not invent a rebuttal.

**Sub-section 3d — VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 3a mechanism count and the OBSERVABLE BREAKDOWN from CASE FORM B]`

Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line. Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name. Reference ROLE UNDER PRESSURE by name. Confirm RE-ASSESSMENT TRIGGER as the final sentence.

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

**[ROLE-NAME LOCK CHECK: All role names must be in the ROLE-NAME LOCK block.]**

Draw ASCII hierarchy with at least two levels. Committees as distinct labeled nodes, not embedded in area boxes.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA (use TABLE C)

Produce TABLE C (see Format Contract). Apply ROLE-TYPE-CLASSIFICATION annotations. Names from ROLE-NAME LOCK only.

STEP 6 — OPERATING RHYTHM (use TABLE D)

Produce TABLE D (see Format Contract). Min three distinct rows. DRI / Owner: ROLE-NAME LOCK names only. Check Format Contract before writing.

STEP 7 — COMMITTEE CHARTERS (use TABLE E)

One TABLE E block per governance meeting in TABLE D. All five fields. Membership and Decides: ROLE-NAME LOCK names only. Quorum fraction format required. Check Format Contract before writing.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` block, all four categories:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

No category empty or missing. DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 9 — ORG EVOLUTION ROADMAP (use TABLE F)

Produce TABLE F (see Format Contract). Row 1: headcount threshold. Row 2: different category.

STEP 10 — ANTI-PATTERN WATCH (use TABLE G)

Produce TABLE G (see Format Contract). Every `Why It Applies Here` cell must use `(cat-N)` syntax from the ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} — {date}`

---

*Generated by: /quest-variate corps-chart — 2026-03-17*
