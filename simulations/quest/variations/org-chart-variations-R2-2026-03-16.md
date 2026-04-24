Now I have the full skill body. Generating all 5 variations:

---

# Quest Variate — `/org-chart` Round 2

## Source Skill Analysis

The current body (`signals/org-chart.md`) is highly constrained: phase-gated, inertia-first, strict section ordering, closed-vocabulary type fields, fraction-format quorum. It is a **compliance-first** structure. Variations below challenge the ordering, phrasing register, output format density, lifecycle lens, and inertia prominence.

---

## V-01 — Single Axis: Role Sequence

**Variation axis:** Role sequence — Classification runs *after* the inertia section, not before it.  
**Hypothesis:** Teams reach the org diagram faster when they defer role taxonomy to the chartering phase where it's actually consumed. Front-loading classification before even knowing whether structure is warranted creates overhead for teams that VERDICT → `CAN-OPERATE-FLAT`.

---

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role:
  - [role name] — [one-line description from role file]
If no files are found, produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block with inferred entries.
DO NOT write any other section until this block exists.

DO NOT classify roles by domain type yet. Classification occurs after VERDICT.

=== [PHASE GATE: ROLES LOADED — INERTIA ASSESSMENT BEGINS] ===

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

Sub-section 1 — Case for Staying Flat

DO produce a three-column table: `Mechanism Name | Type | Frequency / Participants`.
Type MUST come from this closed vocabulary only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO include at minimum two data rows.
DO NOT move mechanism-typed content into Sub-section 2.
After writing the table, count data rows (excluding header). If count < 2, add rows until count = 2.
Then emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

DO inventory active coordination patterns: channels, cadences, informal roles, artifacts.
Include frequency and participants for each.
DO NOT re-list entries from Sub-section 1's table.

Sub-section 3 — Rebuttal

Name the coordination failure the flat-team case cannot answer.
Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Then choose exactly one verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference FLAT-CASE-PRESSURE rating by name.
Write a re-assessment trigger with a concrete threshold.
DO NOT write "revisit as the team grows."

IF VERDICT is `CAN-OPERATE-FLAT`: emit `=== [SKILL COMPLETE: FLAT VERDICT — NO ORG DIAGRAM PRODUCED] ===` and stop.

IF VERDICT is `STRUCTURE-WARRANTED`: emit `=== [PHASE GATE: INERTIA COMPLETE — ROLE CLASSIFICATION BEGINS] ===`

ROLE-TYPE-CLASSIFICATION — ONLY WHEN STRUCTURE IS WARRANTED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block now.
DO apply three-tier ordering: Engineering roles first, then Operations roles, then PM / Design / Research / Other roles.
DO NOT interleave tiers.
Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] — [domain type]`

When classification is complete, emit: `=== [PHASE GATE: ROLES CLASSIFIED — ORG DIAGRAM BEGINS] ===`

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy with at minimum two levels.
DO show committees as distinct labeled nodes.
DO use only role names from ROLES-LOADED or ROLES-NOTE.
DO NOT produce a flat list.

When diagram is complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

DO produce a table: `Area | Headcount | Key Roles | Decides | Escalates`
Key Roles format: `[role name] ([domain type])`
DO include at minimum two area rows plus a `**Total**` row.
DO NOT write generic ownership phrases in Decides or Escalates.
Decides: decision types owned at this level.
Escalates: decision types referred upward, naming destination role or forum.

OPERATING RHYTHM TABLE

DO produce: `Cadence | Frequency | DRI / Owner | Purpose`
Include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.

COMMITTEE CHARTERS

Write a charter for each governance meeting in the rhythm table.
Each charter requires all five fields: Purpose / Membership / Decides / Escalates / Quorum
Membership format: `[role name] ([domain type])`, at minimum two roles.
Escalates must name a destination — DO NOT write "everything not listed."
Quorum format: `Quorum: [N] of [M] member roles required for binding decisions`

When charters are complete, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Populate all four categories:
  cat-1 (Areas) — each area: `- [area name] — headcount: [N]`
  cat-2 (Committees/Cadences) — each name: `- [name]`
  cat-3 (Headcount) — `- Total headcount: [N]`
  cat-4 (DRI Roles) — each DRI: `- [DRI role]`

ORG EVOLUTION ROADMAP

Trigger table: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell MUST open with: `[element name] (cat-N) — [one sentence]`
DO NOT reference an element without the `(cat-N)` typed syntax.
At minimum two rows.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-02 — Single Axis: Output Format

**Variation axis:** Output format — Replaces the ASCII hierarchy with a scored org readiness table; adds a density-coded summary block at the top.  
**Hypothesis:** Executives who consume org-chart artifacts care more about decision-surface area and coordination load than box topology. A scored table format communicates coverage gaps faster than an ASCII hierarchy.

---

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description]`
If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred entries.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION — IMMEDIATELY AFTER ROLES-LOADED

DO classify every loaded role. Three-tier order: Engineering first, then Operations, then PM / Design / Research / Other.
Format: `- [role name] — [domain type]`
Closed type set: `Engineering / PM / Design / Operations / Research / Other`
DO NOT skip. DO NOT interleave tiers.

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT

Sub-section 1 — Case for Staying Flat

Mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`
Types: `Channel / Informal Role / Recurring Cadence / Shared Artifact` only.
Minimum two data rows. After writing, emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

Sub-section 2 — How We Coordinate Today

Inventory active patterns. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Name the specific coordination failure. Cite a concrete observable (blocked decision, SLA miss, silo, time-zone gap, competing roadmap).

Sub-section 4 — VERDICT

Line 1: `FLAT-CASE-PRESSURE: [rating] — [justification citing mechanism count + failure mode]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Line 2: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` with reasoning citing FLAT-CASE-PRESSURE.
Line 3: Re-assessment trigger with a concrete threshold.

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ORG READINESS SCORECARD — REPLACES ASCII DIAGRAM

DO NOT draw an ASCII hierarchy.
Instead, produce an `ORG READINESS SCORECARD` table:

`Area | Proposed Head | Coverage Score (1-5) | Decision Clarity (1-5) | Coordination Load (H/M/L) | Gap`

Scoring rules:
- Coverage Score: 1 = no role covers this domain, 5 = fully staffed with identified DRI
- Decision Clarity: 1 = unclear who decides, 5 = explicit authority documented
- Coordination Load: H = requires cross-area sync weekly or more, M = monthly, L = quarterly or less
- Gap: one-line description of the most important missing element, or "None identified"

DO include at minimum two area rows.
DO annotate each key role in the Area column in format: `[area name] ([role name] / [domain type])`

After the scorecard, DO produce a two-sentence `ORG SUMMARY` block:
  Sentence 1: Total headcount, number of areas, FLAT-CASE-PRESSURE rating.
  Sentence 2: Highest-gap area and its Gap entry.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Table: `Area | Headcount | Key Roles | Decides | Escalates`
Key Roles format: `[role name] ([domain type])`
Decides: decision types owned at this level.
Escalates: decision types referred upward with named destination.
DO NOT write generic ownership phrases.
At minimum two area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE

Table: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three distinct rows: ROB, shiproom or gate, governance meeting.
DO NOT combine meetings.

COMMITTEE CHARTERS

One charter per governance meeting:
  Purpose / Membership / Decides / Escalates / Quorum
Membership: `[role name] ([domain type])`, at minimum two roles.
Escalates: named destination required.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

  cat-1 (Areas): `- [area name] — headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP

Table: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: workload signal, symptom, or milestone.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
"Why It Applies Here" MUST open with: `[element name] (cat-N) — [sentence]`
At minimum two rows.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-03 — Single Axis: Phrasing Register

**Variation axis:** Phrasing register — Converts from imperative constraint directives (`DO / DO NOT`) to a conversational discovery register that asks the model to reason aloud before producing each section.  
**Hypothesis:** Directive-heavy prompts produce compliant but shallow outputs. A discovery register that asks "what do you observe?" before each section may surface more org-specific context, at the cost of predictability.

---

```
You are running `/org-chart {topic}`.

Start by finding the roles for this org. Check `.roles/` for any existing role definitions.

What roles did you find? List each one with a one-line description as a `ROLES-LOADED:` block. If you found nothing, say so with a `ROLES-NOTE:` block and infer the roles the org would likely need.

Once you have the roles, think about what kind of work each one does. Is it primarily engineering, operations, PM, design, research, or something else? Produce a `ROLE-TYPE-CLASSIFICATION:` block that assigns each role exactly one type from that list. Go in this order: engineering roles first, then operations, then everything else. Don't mix the tiers.

When you're done with classification, mark the transition:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

Before drawing any org structure, think carefully about whether one is actually needed.

Make the steelman case first. What coordination mechanisms does this team already have that let them operate without formal structure? Build a table — `Mechanism Name | Type | Frequency / Participants` — where Type is one of: Channel, Informal Role, Recurring Cadence, or Shared Artifact. Find at least two real mechanisms, not hypothetical ones.

After the table, mark the count: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

Now ask: what does this team actually do today to stay coordinated? Inventory those patterns — channels, cadences, people who informally coordinate. Don't repeat what's already in the table above, but add texture.

Then challenge the flat-team case. What's the one coordination failure these mechanisms genuinely cannot prevent? Be specific — name a blocked decision, a missed SLA, a time-zone gap, a knowledge silo, or competing roadmaps. "The team is growing" is not a failure mode.

Now give your verdict. Open with a pressure line:
`FLAT-CASE-PRESSURE: [rating] — [one sentence citing the mechanism count from Sub-section 1 and the failure mode from the Rebuttal]`

Pick a rating: Strong (5), Moderate (4), Weak (3), Negligible (2), or Insufficient (1).

Then state your verdict — `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` — and explain why, referencing the pressure rating by name. Then name a concrete re-assessment trigger: when exactly should this verdict be revisited?

Mark the transition:
`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

Now draw the org. Use an ASCII hierarchy with at least two levels. Show committees as separate labeled nodes, not buried inside an area. Use only the role names you loaded earlier — don't introduce new ones.

Mark the transition:
`=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

Build a headcount table: `Area | Headcount | Key Roles | Decides | Escalates`

For Key Roles, use the format `[role name] ([domain type])`. For Decides and Escalates, be concrete — name decision types, not ownership. Escalates should name where the decision goes, not just say "everything else." Include at least two area rows and a total.

Next, lay out the operating rhythm: `Cadence | Frequency | DRI / Owner | Purpose`

Include at least three distinct events: a review of business (ROB), a shiproom or gate review, and a governance meeting. Each gets its own row.

For each governance meeting in the rhythm table, write a charter. A charter has five parts:
- Purpose: what problem this meeting solves
- Membership: who attends, using `[role name] ([domain type])` format, at least two roles
- Decides: what this forum is authorized to decide
- Escalates: where decisions go when they leave this room — name the destination
- Quorum: `Quorum: [N] of [M] member roles required for binding decisions`

When charters are done:
`=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

Now catalog what you've built in an `ORG-ELEMENT REGISTER`:
- cat-1 (Areas): each area with headcount
- cat-2 (Committees/Cadences): each meeting or cadence name
- cat-3 (Headcount): total headcount
- cat-4 (DRI Roles): each DRI role from the rhythm table

Then think about what would cause this org to need to change. Build an `Org Evolution Roadmap` trigger table: `Trigger | Structural Change | Type`. Give at least two rows: one triggered by headcount, one triggered by something else — a workload signal, structural symptom, or milestone. Don't use two headcount triggers.

Finally, think about what could go wrong with this structure. Write an `Anti-Pattern Watch` table: `Anti-Pattern | Why It Applies Here | Mitigation`. For each "Why It Applies Here" cell, open with `[element name] (cat-N) —` referencing the register above. At least two rows.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-04 — Single Axis: Lifecycle Emphasis

**Variation axis:** Lifecycle emphasis — Restructures the skill around three explicit org lifecycle phases (Bootstrap / Scale / Steady-State), giving each phase its own section allocation and phase-specific criteria, rather than treating org design as a single-point artifact.  
**Hypothesis:** Org charts age badly because they're designed for current headcount, not for the trajectory. Framing the output around lifecycle phases forces the model to produce an artifact that remains useful across multiple headcount doublings.

---

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description]`
If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred entries.

ROLE-TYPE-CLASSIFICATION — IMMEDIATELY AFTER ROLES-LOADED

Three-tier order: Engineering first, then Operations, then PM / Design / Research / Other.
Format: `- [role name] — [domain type]`
Closed type set: `Engineering / PM / Design / Operations / Research / Other`

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT

Sub-section 1 — Case for Staying Flat

Table: `Mechanism Name | Type | Frequency / Participants`
Types (closed): `Channel / Informal Role / Recurring Cadence / Shared Artifact`
At minimum two data rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today
Inventory active patterns. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal
Name the specific coordination failure the flat-team case cannot answer.
Reference a specific observable. DO NOT write "the team is growing" without a failure mode.

Sub-section 4 — VERDICT
Open with: `FLAT-CASE-PRESSURE: [rating] — [justification]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` with concrete re-assessment trigger.

Emit: `=== [PHASE GATE: INERTIA COMPLETE — LIFECYCLE STRUCTURE BEGINS] ===`

ORG LIFECYCLE DESIGN — THREE PHASES

Instead of a single static org diagram, produce a three-phase lifecycle org design. Each phase has its own ASCII diagram, headcount band, and decision model.

PHASE 1 — BOOTSTRAP (current state, ≤ [N] headcount)

DO draw an ASCII hierarchy representing the org as it should be structured today.
Headcount band: estimate the current or near-term headcount this phase applies to.
Key constraint in this phase: minimize coordination overhead; maximize DRI coverage per role.
DO note which roles are doing double-duty and what triggers relief.

PHASE 1 DECISION MODEL — simplified table: `Decision Type | DRI | Escalation Path`
At minimum two decision types.

PHASE 2 — SCALE ([N+1] to [M] headcount)

DO draw an ASCII hierarchy for this phase.
What new areas or committees emerge as the org grows from Phase 1?
What roles split or specialize?
DO NOT simply copy Phase 1 and add names — show structural changes explicitly.

PHASE 2 DECISION MODEL — same format as Phase 1. Show how authority distribution changes.

PHASE 3 — STEADY-STATE ([M+1]+ headcount)

DO draw a steady-state ASCII hierarchy.
Show full committee structure with distinct labeled nodes.
Show at minimum three areas.

Emit: `=== [PHASE GATE: LIFECYCLE DIAGRAMS COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA — PHASE 3 (STEADY-STATE)

Table: `Area | Headcount | Key Roles | Decides | Escalates`
Key Roles: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
At minimum two area rows plus `**Total**` row.
Decides: decision types owned at this level.
Escalates: named destination.

OPERATING RHYTHM TABLE

Table: `Cadence | Frequency | DRI / Owner | Purpose | First Appears In Phase`
At minimum three rows: ROB, shiproom or gate, governance meeting.
`First Appears In Phase` column: Phase 1, Phase 2, or Phase 3.
DO NOT combine meetings.

COMMITTEE CHARTERS

One charter per governance meeting:
  Purpose / Membership / Decides / Escalates / Quorum
Membership: `[role name] ([domain type])`, at minimum two roles.
Escalates: named destination.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

  cat-1 (Areas): `- [area name] — headcount: [N]` (Phase 3 counts)
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP

Table: `Trigger | Structural Change | Type | Phase Transition`
`Phase Transition` column: which phase boundary this trigger crosses (1→2, 2→3, or within-phase).
At minimum two rows. Row 1: headcount threshold. Row 2: workload signal or milestone.

ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
"Why It Applies Here" opens with: `[element name] (cat-N) — [sentence]`
At minimum two rows.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-05 — Combined Axis: Inertia Prominence + Output Format + Role Sequence

**Variation axis:** Inertia prominence (elevated) + Output format (summary cards replace ASCII) + Role sequence (classification deferred post-verdict).  
**Hypothesis:** The most decision-useful org artifact for a PM audience leads with the inertia VERDICT as a prominent decision card, defers taxonomy busywork to after the flatness question is settled, and replaces topology diagrams (which PMs rarely read) with structured decision-surface cards per area.

---

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description]`
If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred entries.
DO NOT classify roles by domain type yet — classification is deferred until after VERDICT.

=== [PHASE GATE: ROLES LOADED — INERTIA ASSESSMENT BEGINS] ===

INERTIA ASSESSMENT — PROMINENCE LEVEL: HIGH

The inertia question is the primary output of this skill. Every subsequent section depends on it. Do not rush past it.

Sub-section 1 — Case for Staying Flat

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`
Type vocabulary (closed): `Channel / Informal Role / Recurring Cadence / Shared Artifact`
At minimum two data rows. Count data rows after writing.
If count < 2, add rows until count ≥ 2.
Then emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory active patterns: channels, cadences, informal roles, artifacts with frequency and participants.
DO NOT re-list Sub-section 1 table entries.

Sub-section 3 — Rebuttal

Name the one coordination failure the flat-team case cannot handle.
Cite a specific observable: blocked decision, SLA miss, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" as the failure mode.

Sub-section 4 — VERDICT CARD

DO NOT write a paragraph. Write a structured VERDICT CARD block in this exact format:

```
VERDICT CARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLAT-CASE-PRESSURE : [rating] — [one-sentence justification]
VERDICT            : [CAN-OPERATE-FLAT or STRUCTURE-WARRANTED]
REASONING          : [one sentence citing FLAT-CASE-PRESSURE rating]
RE-ASSESS WHEN     : [concrete threshold — not "as the team grows"]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Rating MUST be exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

IF VERDICT is `CAN-OPERATE-FLAT`: emit `=== [SKILL COMPLETE: FLAT VERDICT] ===` and stop.

IF VERDICT is `STRUCTURE-WARRANTED`: emit `=== [PHASE GATE: INERTIA COMPLETE — ROLE CLASSIFICATION BEGINS] ===`

ROLE-TYPE-CLASSIFICATION — ONLY WHEN STRUCTURE IS WARRANTED

Three-tier order: Engineering first, then Operations, then PM / Design / Research / Other.
Format: `- [role name] — [domain type]`
Closed type set: `Engineering / PM / Design / Operations / Research / Other`

Emit: `=== [PHASE GATE: ROLES CLASSIFIED — AREA CARDS BEGIN] ===`

AREA DECISION CARDS — REPLACES ASCII HIERARCHY AND HEADCOUNT TABLE

DO NOT draw an ASCII org diagram.
DO NOT produce a headcount table.
Instead, produce one AREA DECISION CARD per organizational area. Format each card exactly:

```
AREA CARD: [Area Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Headcount      : [N]
Key Roles      : [role name] ([domain type]), ...
Decides        : [decision types owned at this level]
Escalates      : [decision types referred upward → named destination]
Coordination   : [primary coordination mechanism for this area]
Risk           : [one-line risk if this area is understaffed or has unclear DRI]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

DO produce at minimum two area cards.
Decides: specific decision types, not "owns the area."
Escalates: name the destination role or forum.
Key Roles: use `[role name] ([domain type])` format from ROLE-TYPE-CLASSIFICATION.

After all area cards, produce a one-line `AREA SUMMARY: [N] areas | [total headcount] headcount | [N] unclear-DRI risks`

Emit: `=== [PHASE GATE: AREA CARDS COMPLETE — RHYTHM AND CHARTERS BEGIN] ===`

OPERATING RHYTHM TABLE

Table: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: ROB, shiproom or gate, governance meeting.
DO NOT combine meetings.
Reference a loaded role in DRI / Owner where possible.

COMMITTEE CHARTERS

One charter per governance meeting in the rhythm table:
  Purpose / Membership / Decides / Escalates / Quorum
Membership: `[role name] ([domain type])`, at minimum two roles.
Escalates: named destination — DO NOT write "everything not listed."
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

  cat-1 (Areas): `- [area name] — headcount: [N]` (from Area Cards)
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP

Table: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
"Why It Applies Here" opens with: `[element name] (cat-N) — [sentence]`
DO NOT omit `(cat-N)` typed syntax.
At minimum two rows.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## Variation Summary

| Variation | Axis | Key Hypothesis |
|-----------|------|----------------|
| V-01 | Role Sequence | Deferring classification past VERDICT eliminates taxonomy overhead for flat-team outcomes |
| V-02 | Output Format | Scored readiness table communicates coverage gaps faster than ASCII topology |
| V-03 | Phrasing Register | Discovery register surfaces org-specific context that directive constraints suppress |
| V-04 | Lifecycle Emphasis | Three-phase design produces artifacts that remain useful across headcount doublings |
| V-05 | Combined (Inertia + Format + Sequence) | VERDICT card + Area Decision Cards + deferred classification is the optimal PM-facing format |
