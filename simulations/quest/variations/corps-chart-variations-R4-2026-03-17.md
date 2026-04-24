# corps-chart Skill Variations — Round 4 (V-01 through V-05)

---

## V-01 — Single Axis: Role Sequence
**Hypothesis:** Front-loading role classification and the ROLE-NAME LOCK as the only permitted first action — before any structural reasoning begins — eliminates downstream role-name drift because the locked list is the first artifact in working memory, not a later annotation.

---

```
You are generating an org-chart artifact for a product or domain.

## STEP 0 — LOAD ROLES (MANDATORY FIRST ACTION)

Before writing any structural content, load roles from .roles/.
Do not skip or defer this step. Nothing else begins until the roles block is complete.

Emit this block:

---
ROLES-LOADED: [comma-separated list of every role file found, or "none found"]
---

Then classify every loaded role into one of four domain types:
- (strategic) — sets direction, owns outcomes
- (operational) — executes day-to-day delivery
- (advisory) — provides input without vote
- (governance) — approves, escalates, or audits

Emit the classification table:

| Role Name | Domain Type |
|-----------|-------------|
| ...       | ...         |

If no roles are found, emit:
  ROLES-NOTE: No .roles/ files found. Inferring roles from context; treat as provisional.

Then emit the lock block immediately — before any phase gate, before any section header:

  ROLE-NAME LOCK
  ┌─────────────────────────────────────────────────────────────────┐
  │ The following roles are the complete permitted set for this     │
  │ document. Every role reference in every subsequent section —   │
  │ diagram, rhythm table, charter, inertia analysis — must match  │
  │ exactly one entry in this list. No new role names may appear.  │
  │                                                                 │
  │ [list every role, one per line]                                 │
  └─────────────────────────────────────────────────────────────────┘

The ROLE-NAME LOCK is the contract. Downstream sections are verified against it,
not against the prose role descriptions above it.

---

## STEP 1 — INERTIA ASSESSMENT

Emit: === [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

Write an Inertia Assessment with four sub-sections in this exact order:

**1. Case for Staying Flat**
Make the strongest honest case for not building this org structure.
Include a mechanism table:

| Type                | Mechanism             | Currently Working? |
|---------------------|-----------------------|--------------------|
| [type from vocabulary] | [how coordination happens now] | Yes / Partial / No |

Type vocabulary (closed set): Decision escalation | Cross-role sync | Conflict resolution | Resource allocation | Shipping accountability

Include at minimum two rows.

**2. How We Coordinate Today**
Describe the current coordination pattern in concrete terms — who talks to whom,
how decisions surface, where blockers resolve. Name roles from ROLE-NAME LOCK only.

**3. Rebuttal**
Challenge the flat-case using the mandatory four-field form. Every field is required.
Do not proceed to VERDICT without completing all four fields.

  ROLE UNDER PRESSURE: [exactly one role from ROLE-NAME LOCK]
  OBSERVABLE BREAKDOWN: [a current coordination failure this role already experiences —
    not "as we scale" — something happening now or at current headcount]
  WHY EXISTING MECHANISMS FAIL: [explain why the mechanisms listed in the Case for
    Staying Flat do not resolve this breakdown]
  RE-ASSESSMENT TRIGGER: [a concrete measurable threshold — a specific hire count,
    a named milestone event, or a structural symptom with a countable condition —
    not "revisit as the team grows"]

**4. VERDICT**
Open with exactly this format:
  FLAT-CASE-PRESSURE: [rating] — [one-sentence justification]

Rating is from this closed set: Strong | Moderate | Weak | Negligible | Insufficient

Then declare exactly one of:
  CAN-OPERATE-FLAT — [condition under which this holds]
  STRUCTURE-WARRANTED — [what the structure resolves that flat cannot]

---

## STEP 2 — ORG STRUCTURE

Emit: === [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

Draw an ASCII org diagram. Requirements:
- At least two levels of hierarchy (e.g., top-level domain → areas)
- Committees appear as distinct labeled nodes connected by lines — not embedded
  inside an area box, not in prose only
- Role names in boxes must match ROLE-NAME LOCK exactly
- Use box-drawing characters: ┌─┐ └─┘ │ ├── └──

Example structure (adapt to the domain):
  ┌─────────────────────────────┐
  │   [Domain Name]             │
  │   [Lead Role]               │
  └───────┬─────────────────────┘
          │
    ┌─────┴──────┐
    │            │
  [Area A]    [Area B]
  [Role]      [Role]
          │
  ┌───────┴────────┐
  │ [Committee C]  │
  │ (governance)   │
  └────────────────┘

---

## STEP 3 — HEADCOUNT AND RHYTHM

Emit: === [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

**Headcount Table**
Five columns, no merging. Separate Decides and Escalates columns are required.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [Area A] | N | [role] (strategic) | [what this area resolves without escalation] | [what it cannot resolve alone] |
| [Area B] | N | [role] (operational) | ... | ... |
| **Total** | **N** | — | — | — |

Key Roles annotation format: [role name] ([domain type])
Total row must sum all area headcounts.

**Operating Rhythm Table**
Four columns. At least three rows covering at minimum:
(a) ROB (review of business / weekly ops)
(b) a shiproom or gate meeting
(c) a governance meeting

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| ROB | Weekly | [role from ROLE-NAME LOCK] | ... |
| Ship Gate | [frequency] | [role] | ... |
| [Governance meeting] | [frequency] | [role] | ... |

DRI / Owner column must name roles from ROLE-NAME LOCK only.

---

## STEP 4 — COMMITTEE CHARTERS

For every governance meeting in the rhythm table, write a charter with all five fields.
Missing any field causes the charter to fail.

**[Committee Name] Charter**
- Purpose: [what problem this committee exists to resolve]
- Membership: [role 1] ([domain type]), [role 2] ([domain type]) [at least two roles]
- Decides: [what this committee has authority to resolve]
- Escalates: [named destination — e.g., "escalates to [role]" — not "everything not listed under Decides"]
- Quorum: [N] of [M] member roles required for binding decisions

Emit: === [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

## STEP 5 — ORG-ELEMENT REGISTER

Emit the register immediately after the charters phase gate.

  ORG-ELEMENT REGISTER
  cat-1 (Areas): [Area A] (N), [Area B] (N), ...
  cat-2 (Committees/Cadences): [Committee C], [ROB], [Ship Gate], ...
  cat-3 (Headcount): Total = N
  cat-4 (DRI Roles): [role 1], [role 2], ...

No category may be empty. cat-4 must list at least one role per governance meeting.

---

## STEP 6 — ORG EVOLUTION ROADMAP

Write a trigger table:

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold, e.g., "area exceeds 8 ICs"] | [specific change] | Headcount threshold |
| [workload signal, milestone, or structural symptom] | [specific change] | [different category] |

Row 1 must be a headcount threshold.
Row 2 must come from a different category: Workload signal | Structural symptom | Milestone event
Two headcount thresholds do not satisfy this requirement.

---

## STEP 7 — ANTI-PATTERN WATCH

Emit the citation schema before the table:

  CAT-N-CITATION-SCHEMA
  ┌────────────────────────────────────────────────────────────────────┐
  │ Valid cat-N codes drawn from ORG-ELEMENT REGISTER:                │
  │   cat-1 = Areas  |  cat-2 = Committees/Cadences                  │
  │   cat-3 = Headcount  |  cat-4 = DRI Roles                        │
  │                                                                    │
  │ Mandatory prefix for every "Why It Applies Here" cell:            │
  │   [element name] (cat-N) — [explanation]                          │
  │                                                                    │
  │ No cell may name an org element without this typed citation.      │
  └────────────────────────────────────────────────────────────────────┘

Then write the table:

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [name] | [element name] (cat-N) — [why this specific element is at risk] | [concrete action] |
| [name] | [element name] (cat-N) — ... | ... |

At least two rows. Every "Why It Applies Here" cell must open with the typed citation prefix.

---

## AMEND MODE

If the user provides an AMEND instruction, apply the change to the existing org-chart.md:
- Headcount changes: update the headcount table and Total row; note the delta
- Reorganization: redraw the ASCII diagram; update all affected charters and rhythm entries
- Role changes: update ROLE-NAME LOCK first, then propagate to all sections

Do not regenerate unchanged sections. Mark amended sections with `[AMENDED]`.

---

## ROLE-NAME COMPLIANCE CHECK (final)

Before closing the artifact, scan every section — diagram, rhythm table DRI/Owner,
charter Membership and Decides, Inertia sub-sections — and confirm each named role
appears in ROLE-NAME LOCK. If any mismatch is found, correct it inline before output.
```

---

## V-02 — Single Axis: Inertia Framing
**Hypothesis:** Treating the flat-org case as a genuine adversarial competitor — with a named advocate voice and a structured rebuttal round — produces more honest inertia verdicts than positioning inertia as a procedural checkbox before the "real" structure section.

---

```
You are generating an org-chart artifact for a product or domain.
This document takes a position: org structure either earns its complexity or doesn't.
The inertia section is not a formality. It is the primary challenge the structure must defeat.

---

## PHASE 0 — ROLES

Load roles from .roles/. List every file found.

  ROLES-LOADED: [list]

Classify each role:

| Role Name | Domain Type |
|-----------|-------------|
| ...       | (strategic / operational / advisory / governance) |

If no roles found: emit ROLES-NOTE and infer from context.

Emit:

  ROLE-NAME LOCK — complete enumeration, no additions permitted downstream
  [role 1]
  [role 2]
  ...

  ROLE-TYPE-CLASSIFICATION is complete. ROLE-NAME LOCK is set.

---

## PHASE 1 — THE FLAT-ORG CASE

Emit: === [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

### ADVOCATE: FLAT ORG

Speak in the voice of a skeptic who has seen over-engineered orgs fail.
Make the strongest possible case that this team does not need the structure
you are about to propose.

**Coordination mechanisms already in place:**

| Type | Mechanism | Currently Working? |
|------|-----------|-------------------|
| [from closed set] | [how this team coordinates today] | Yes / Partial / No |

Closed set for Type: Decision escalation | Cross-role sync | Conflict resolution | Resource allocation | Shipping accountability

Minimum two mechanisms. Be honest: if a mechanism is partially working, say Partial.

**How we coordinate today:**
Describe the actual current state. Name only roles from ROLE-NAME LOCK.
Where do decisions get made? Where do things get stuck? What are people already doing
that an org chart would just formalize?

---

### ADVOCATE: STRUCTURE

Now rebut the flat-case. You are not allowed to use growth projections ("as we scale").
You must identify a coordination failure that is happening now, at current headcount,
with these specific roles.

Use the mandatory case form. All four fields required. No field may be skipped.

  ROLE UNDER PRESSURE: [one role from ROLE-NAME LOCK]
  OBSERVABLE BREAKDOWN: [what this role cannot do today because structure is missing —
    a current, observable failure, not a projected one]
  WHY EXISTING MECHANISMS FAIL: [pick one mechanism from the flat-case table and explain
    precisely why it does not resolve this breakdown]
  RE-ASSESSMENT TRIGGER: [if you are wrong and the flat case holds longer than expected,
    what is the concrete measurable signal that triggers a new assessment — a specific
    hire count, a named milestone, or a structural symptom with a countable condition]

---

### VERDICT

  FLAT-CASE-PRESSURE: [Strong / Moderate / Weak / Negligible / Insufficient] — [one sentence]

Then declare one of:
  CAN-OPERATE-FLAT — [under what condition, with what monitoring]
  STRUCTURE-WARRANTED — [what specific coordination failure this structure resolves]

The verdict must be consistent with the rebuttal. If OBSERVABLE BREAKDOWN names a current
failure and WHY EXISTING MECHANISMS FAIL is well-argued, the verdict cannot be
CAN-OPERATE-FLAT without explicitly acknowledging the contradiction.

---

## PHASE 2 — STRUCTURE

Emit: === [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

Draw the org as an ASCII diagram. The inertia verdict just determined whether structure
is warranted. Now show exactly the structure that resolves the coordination failure named
in the rebuttal — not a generic hierarchy.

Rules:
- Minimum two hierarchy levels
- Committees appear as distinct labeled nodes with connectors — not inside area boxes
- Every role name in the diagram matches ROLE-NAME LOCK exactly
- The role named in ROLE UNDER PRESSURE must appear in the diagram with a clear position

Use box-drawing characters (┌ ─ ┐ └ ┘ │ ├ └).

---

## PHASE 3 — HEADCOUNT AND RHYTHM

Emit: === [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

**Headcount Table** — five columns, no merging Decides and Escalates:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

- Key Roles format: [role name] ([domain type])
- Decides: what this area resolves without escalation
- Escalates: what it cannot resolve and where it sends it
- Close with **Total** row summing all headcounts

**Operating Rhythm** — minimum three rows covering ROB, a shiproom or gate, and governance:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DRI / Owner must name roles from ROLE-NAME LOCK only. No invented roles.

---

## PHASE 4 — CHARTERS

For every governance meeting in the rhythm table, write a charter. Five fields required.
A charter with fewer than five fields is incomplete.

**[Committee Name] Charter**
- Purpose: [what problem it resolves]
- Membership: [role] ([domain type]), [role] ([domain type]) — at least two
- Decides: [specific scope of authority]
- Escalates: [named destination — not "everything else"]
- Quorum: [N] of [M] member roles required for binding decisions

Emit: === [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

## PHASE 5 — REGISTER

  ORG-ELEMENT REGISTER
  cat-1 (Areas): [each area with headcount]
  cat-2 (Committees/Cadences): [each committee and rhythm meeting]
  cat-3 (Headcount): Total = N
  cat-4 (DRI Roles): [roles that own rhythm entries or committee decisions]

All four categories must be populated.

---

## PHASE 6 — EVOLUTION ROADMAP

The inertia section named a re-assessment trigger. The roadmap extends that into a
full trigger table. Row 1 must be a headcount threshold. Row 2 must be a different
category (workload signal, structural symptom, or milestone event).

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [specific change] | Headcount threshold |
| [different category] | [specific change] | [Workload signal / Structural symptom / Milestone event] |

If the Re-Assessment Trigger from the rebuttal was a headcount threshold, it must appear
as Row 1. Do not invent a different threshold.

---

## PHASE 7 — ANTI-PATTERN WATCH

Declare the citation schema before writing the table:

  CAT-N-CITATION-SCHEMA
  Valid codes from ORG-ELEMENT REGISTER:
    cat-1 = Areas | cat-2 = Committees/Cadences | cat-3 = Headcount | cat-4 = DRI Roles
  Required prefix for "Why It Applies Here":
    [element name] (cat-N) — [explanation]
  No cell may name an element without this prefix.

Then:

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [name] | [element] (cat-N) — [why this element is at risk] | [action] |
| [name] | [element] (cat-N) — ... | ... |

Minimum two rows. The anti-patterns chosen should connect back to the coordination
failure identified in the inertia rebuttal — this org was designed to fix something
specific; the anti-patterns should reflect the failure mode if the fix erodes.

---

## AMEND MODE

AMEND instruction changes go into effect immediately. Update ROLE-NAME LOCK if roles
change. Redraw the diagram if structure changes. Update the headcount Total. Mark all
changed sections [AMENDED]. Do not regenerate unchanged sections.
```

---

## V-03 — Single Axis: Output Format (Schema-Declared Tables)
**Hypothesis:** Declaring column schemas as named contracts before populating each table — rather than relying on instructions to describe correct column structure — eliminates partial compliance on structured sections because the schema is checkable independently of the prose instructions that required it.

---

```
You are generating an org-chart artifact for a product or domain.
Every structured section in this document is preceded by its column schema.
Schemas are contracts: downstream content is verified against them, not against
the prose instructions that defined them.

---

## SECTION 1 — ROLES

Load roles from .roles/. If none found, infer and emit ROLES-NOTE.

  ROLES-LOADED: [comma-separated list or "none found"]

SCHEMA: ROLE-TYPE-CLASSIFICATION
  columns: Role Name | Domain Type
  Domain Type vocabulary (closed): strategic | operational | advisory | governance

| Role Name | Domain Type |
|-----------|-------------|
| ...       | ...         |

ROLE-NAME LOCK
Enumeration of every permitted role reference for this document.
No role name not listed here may appear in any subsequent section.
[list every role, one per line]

Emit: === [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

---

## SECTION 2 — INERTIA ASSESSMENT

**2a. Case for Staying Flat**

SCHEMA: COORDINATION-MECHANISMS
  columns: Type | Mechanism | Currently Working?
  Type vocabulary (closed): Decision escalation | Cross-role sync | Conflict resolution |
    Resource allocation | Shipping accountability
  Currently Working? vocabulary (closed): Yes | Partial | No
  minimum rows: 2

| Type | Mechanism | Currently Working? |
|------|-----------|-------------------|
| ... | ... | ... |

**2b. How We Coordinate Today**
Prose. Name only roles from ROLE-NAME LOCK. Describe the actual current state —
who talks to whom, how decisions surface, where blockers resolve.

**2c. Rebuttal**

SCHEMA: REBUTTAL-CASE-FORM
  fields (all required, in this order):
    ROLE UNDER PRESSURE: [one role from ROLE-NAME LOCK]
    OBSERVABLE BREAKDOWN: [current failure — no "as we scale" phrasing]
    WHY EXISTING MECHANISMS FAIL: [reference at least one row from COORDINATION-MECHANISMS]
    RE-ASSESSMENT TRIGGER: [concrete measurable threshold — hire count, milestone, or
      structural symptom with countable condition]

  ROLE UNDER PRESSURE: _
  OBSERVABLE BREAKDOWN: _
  WHY EXISTING MECHANISMS FAIL: _
  RE-ASSESSMENT TRIGGER: _

**2d. VERDICT**

  FLAT-CASE-PRESSURE: [Strong / Moderate / Weak / Negligible / Insufficient] — [justification]

  [CAN-OPERATE-FLAT or STRUCTURE-WARRANTED] — [one-sentence declaration]

Emit: === [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

---

## SECTION 3 — ORG DIAGRAM

SCHEMA: ORG-DIAGRAM
  format: ASCII box-drawing (┌ ─ ┐ └ ┘ │ ├ └)
  required: minimum two hierarchy levels
  required: committees as distinct labeled nodes with connectors (not embedded in area boxes)
  required: all role names match ROLE-NAME LOCK

Draw the diagram below the schema declaration.

Emit: === [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

---

## SECTION 4 — HEADCOUNT TABLE

SCHEMA: HEADCOUNT
  columns: Area | Headcount | Key Roles | Decides | Escalates
  Key Roles format: [role name] ([domain type])
  Decides: what this area resolves without escalation
  Escalates: what this area cannot resolve and where it routes
  NOTE: "Decides" and "Escalates" are separate columns. Merging them fails this schema.
  required: minimum two area rows + one Total row
  Total row: Area = "**Total**", Headcount = sum, Key Roles = "—", Decides = "—", Escalates = "—"

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| ...  | N         | ...       | ...     | ...       |
| **Total** | **N** | — | — | — |

---

## SECTION 5 — OPERATING RHYTHM

SCHEMA: OPERATING-RHYTHM
  columns: Cadence | Frequency | DRI / Owner | Purpose
  DRI / Owner: must name a role from ROLE-NAME LOCK
  required rows (minimum one per category, no merging two categories into one row):
    category-A: ROB (review of business or weekly operational sync)
    category-B: shiproom or gate meeting
    category-C: governance meeting

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| ...     | ...       | ...         | ...     |

---

## SECTION 6 — COMMITTEE CHARTERS

For every row in OPERATING-RHYTHM where category = governance:

SCHEMA: COMMITTEE-CHARTER
  fields (all five required):
    Purpose: [problem this committee resolves]
    Membership: [role] ([domain type]), [role] ([domain type]) — minimum two annotated roles
    Decides: [specific scope of authority]
    Escalates: [named destination — not "everything not listed under Decides"]
    Quorum: [N] of [M] member roles required for binding decisions

Write one charter per governance meeting. A charter missing any field fails its schema.

Emit: === [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

## SECTION 7 — ORG-ELEMENT REGISTER

SCHEMA: ORG-ELEMENT-REGISTER
  categories (all four required, none may be empty):
    cat-1 (Areas): [area name] ([headcount]), ...
    cat-2 (Committees/Cadences): [name], ...
    cat-3 (Headcount): Total = N
    cat-4 (DRI Roles): [role], ...

  ORG-ELEMENT REGISTER
  cat-1 (Areas): _
  cat-2 (Committees/Cadences): _
  cat-3 (Headcount): Total = _
  cat-4 (DRI Roles): _

---

## SECTION 8 — ORG EVOLUTION ROADMAP

SCHEMA: EVOLUTION-ROADMAP
  columns: Trigger | Structural Change | Type
  Type vocabulary (closed): Headcount threshold | Workload signal | Structural symptom |
    Milestone event
  required: Row 1 Type = Headcount threshold
  required: Row 2 Type ≠ Headcount threshold (must be a different category)
  constraint: two rows with Type = Headcount threshold does not satisfy minimum diversity

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | ... | Headcount threshold |
| [different category] | ... | [Workload signal / Structural symptom / Milestone event] |

---

## SECTION 9 — ANTI-PATTERN WATCH

CAT-N-CITATION-SCHEMA
  SCHEMA: CAT-N-CITATION
  source: ORG-ELEMENT REGISTER (populated in Section 7)
  valid codes:
    cat-1 = Areas
    cat-2 = Committees/Cadences
    cat-3 = Headcount
    cat-4 = DRI Roles
  required prefix for "Why It Applies Here":
    [element name] (cat-N) — [explanation]
  constraint: no cell may name an org element without this typed prefix

SCHEMA: ANTI-PATTERN-WATCH
  columns: Anti-Pattern | Why It Applies Here | Mitigation
  "Why It Applies Here" cells: must open with [element name] (cat-N) — per CAT-N-CITATION
  minimum rows: 2

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [name] | [element] (cat-N) — [why at risk] | [action] |
| [name] | [element] (cat-N) — ...           | ...        |

---

## AMEND MODE

If AMEND instruction received:
1. Identify which schema is affected (HEADCOUNT / ORG-DIAGRAM / OPERATING-RHYTHM / etc.)
2. Re-emit only the affected schema block(s) with [AMENDED] marker
3. Update ORG-ELEMENT REGISTER if cat-1, cat-2, cat-3, or cat-4 changes
4. Update Total row in HEADCOUNT if headcount changes
5. Do not regenerate unaffected sections
```

---

## V-04 — Combined Axes: Role Sequence + Lifecycle Emphasis
**Hypothesis:** Numbering execution phases as explicit commands (EXECUTE PHASE N) with gate lines as completion assertions — rather than section headers — shifts model behavior from narrative toward procedural: each phase has an unambiguous entry condition, body, and exit signal, reducing section ordering failures and role drift simultaneously.

---

```
You are executing the corps-chart procedure. This document has 8 phases.
Each phase has an entry condition, a body, and an exit signal.
Do not begin a phase until its entry condition is satisfied.
Do not exit a phase without emitting its gate line.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0 — ROLE LOADING
Entry condition: none (this is the first phase)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Load .roles/. Emit:

  ROLES-LOADED: [list every file, or "none found"]

If no files: emit ROLES-NOTE and infer roles from the provided context.

Classify each role. Permitted domain types: strategic | operational | advisory | governance

  ROLE-TYPE-CLASSIFICATION
  | Role Name | Domain Type |
  |-----------|-------------|
  | ...       | ...         |

Emit the lock block:

  ╔══════════════════════════════════════════════════════════════╗
  ║ ROLE-NAME LOCK                                               ║
  ║ These are the only role names permitted in this document.    ║
  ║ Every subsequent section is verified against this list.      ║
  ║                                                              ║
  ║ [role 1]                                                     ║
  ║ [role 2]                                                     ║
  ║ ...                                                          ║
  ╚══════════════════════════════════════════════════════════════╝

Phase 0 exit signal: ROLE-NAME LOCK emitted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — INERTIA ASSESSMENT
Entry condition: ROLE-NAME LOCK emitted
Gate: === [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTE: emit the phase gate line above, then write the Inertia Assessment.

**Sub-phase 1a — Case for Staying Flat**
Build the mechanism table. Use only these Type values:
  Decision escalation | Cross-role sync | Conflict resolution |
  Resource allocation | Shipping accountability

| Type | Mechanism | Currently Working? |
|------|-----------|-------------------|
| ...  | ...       | Yes / Partial / No |

Minimum two rows. Partial or No entries inform the rebuttal.

**Sub-phase 1b — How We Coordinate Today**
Describe the current state in concrete terms. Reference only roles in ROLE-NAME LOCK.

**Sub-phase 1c — Rebuttal**
EXECUTE the four-field form. All fields required. Sequence is locked.

  ROLE UNDER PRESSURE: [one role from ROLE-NAME LOCK]
  OBSERVABLE BREAKDOWN: [current failure — not a growth projection]
  WHY EXISTING MECHANISMS FAIL: [name the mechanism from 1a that fails here, explain why]
  RE-ASSESSMENT TRIGGER: [specific hire count, named milestone, or countable structural symptom]

**Sub-phase 1d — VERDICT**
  FLAT-CASE-PRESSURE: [Strong / Moderate / Weak / Negligible / Insufficient] — [justification]
  [CAN-OPERATE-FLAT or STRUCTURE-WARRANTED]

Phase 1 exit signal: VERDICT emitted with one of the two declarations.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — ORG DIAGRAM
Entry condition: VERDICT emitted
Gate: === [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTE: emit the phase gate line, then draw the ASCII org diagram.

Requirements (checklist — verify each before exit):
[ ] Minimum two hierarchy levels with parent-child connectors
[ ] Committees appear as distinct labeled nodes — not inside area boxes
[ ] Every role name in the diagram is in ROLE-NAME LOCK
[ ] Box-drawing characters used: ┌ ─ ┐ └ ┘ │ ├ └

Phase 2 exit signal: diagram drawn, all checklist items verified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — HEADCOUNT AND RHYTHM
Entry condition: diagram complete
Gate: === [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTE: emit the phase gate line, then write both tables.

**Headcount Table**
Column order: Area | Headcount | Key Roles | Decides | Escalates
PROHIBITION: do not merge Decides and Escalates into a single column.
Key Roles annotation: [role name] ([domain type])
Close with **Total** row. Total headcount = sum of all area rows.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| ...  | N | ... | ... | ... |
| **Total** | **N** | — | — | — |

**Operating Rhythm Table**
Column order: Cadence | Frequency | DRI / Owner | Purpose
DRI / Owner: roles from ROLE-NAME LOCK only.

Row requirements (minimum one per category):
- Category A: ROB or equivalent weekly operational meeting
- Category B: shiproom, ship gate, or milestone review
- Category C: governance meeting (this row feeds Phase 4 charters)

Do not merge two categories into one row.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| ...     | ...       | ...         | ...     |

Phase 3 exit signal: headcount Total row emitted, at least three rhythm rows present.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — COMMITTEE CHARTERS
Entry condition: rhythm table complete with at least one governance row
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTE: for each governance row in the rhythm table, write one charter.
A charter is complete only when all five fields are present.

**[Committee Name] Charter**
- Purpose: ...
- Membership: [role] ([domain type]), [role] ([domain type]) [at minimum two annotated roles]
- Decides: [specific scope]
- Escalates: [named destination — not "everything not in Decides"]
- Quorum: [N] of [M] member roles required for binding decisions

Phase 4 exit signal: one charter per governance row, all five fields present in each.
Gate: === [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===
EXECUTE: emit this gate line after the last charter.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — ORG-ELEMENT REGISTER
Entry condition: charters gate emitted
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTE: populate all four categories. None may be empty.

  ORG-ELEMENT REGISTER
  cat-1 (Areas): [area] (N headcount), ...
  cat-2 (Committees/Cadences): [each committee and rhythm meeting by name]
  cat-3 (Headcount): Total = N
  cat-4 (DRI Roles): [each role that owns a rhythm entry or committee decision]

Phase 5 exit signal: all four cat-N lines populated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — ORG EVOLUTION ROADMAP
Entry condition: ORG-ELEMENT REGISTER complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTE: build the trigger table. Type vocabulary:
  Headcount threshold | Workload signal | Structural symptom | Milestone event

Row 1: Type must be Headcount threshold.
Row 2: Type must be different from Row 1.
Constraint: two Headcount threshold rows do not satisfy minimum diversity.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| ...     | ...               | Headcount threshold |
| ...     | ...               | [different type] |

Phase 6 exit signal: table present with two rows of different Type values.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — ANTI-PATTERN WATCH
Entry condition: Evolution Roadmap complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTE: emit the citation schema first, then the table.

  CAT-N-CITATION-SCHEMA
  Source: ORG-ELEMENT REGISTER (Phase 5)
  Valid codes: cat-1 = Areas | cat-2 = Committees/Cadences | cat-3 = Headcount | cat-4 = DRI Roles
  Mandatory prefix: [element name] (cat-N) — [explanation]
  Constraint: every "Why It Applies Here" cell must open with this prefix.

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [name] | [element] (cat-N) — [why] | [action] |
| [name] | [element] (cat-N) — [why] | [action] |

Minimum two rows. Verify each "Why It Applies Here" cell against CAT-N-CITATION-SCHEMA
before output.

Phase 7 exit signal: two rows present, all "Why It Applies Here" cells correctly prefixed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AMEND MODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Identify the phase(s) affected by the AMEND instruction.
Re-execute only those phases. Emit [AMENDED] after each modified section header.
If Phase 0 is re-executed (role change), propagate the updated ROLE-NAME LOCK
and re-verify all downstream role references before output.
```

---

## V-05 — Combined Axes: Phrasing Register + Inertia Framing
**Hypothesis:** A conversational imperative register — short directives, active voice, explicit "now do X" commands — reduces hedging in the inertia section (where formal specifications tend to invite perfunctory compliance) and produces more honest verdicts by asking the model to argue a position rather than satisfy a schema.

---

```
Generate an org-chart for this product or domain.

Before you start: this document argues a position. Either the team needs structure
or it doesn't. The inertia section is where that argument gets made. Don't treat it
as a box to check before the diagram.

---

### FIRST: LOAD YOUR ROLES

Look in .roles/. Tell me what you found:

  ROLES-LOADED: [list every file, or "none found"]

Now classify each role. Pick one type for each: strategic | operational | advisory | governance

| Role Name | Domain Type |
|-----------|-------------|
| ...       | ...         |

Didn't find any roles? Say so with ROLES-NOTE and infer from context.

Now lock the list. This is the complete set of role names for this document.
Any role you invent after this point is a bug.

  ROLE-NAME LOCK
  [role 1]
  [role 2]
  ...

  (This is the complete list. Everything that follows can only reference these names.)

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

### ARGUE THE FLAT CASE FIRST

Before you draw a single box in an org diagram, make the case for not having one.
What does this team have going for it today that an org chart would just formalize?

Build a mechanism table — two rows minimum:

| Type | Mechanism | Currently Working? |
|------|-----------|-------------------|

Types (pick from this list only):
  Decision escalation | Cross-role sync | Conflict resolution | Resource allocation | Shipping accountability

Be honest about "Currently Working?" — Yes, Partial, or No. If everything is Yes,
that's a strong flat case and your rebuttal has work to do.

Then describe how coordination actually happens today. Use only roles from your ROLE-NAME LOCK.
Where do decisions get made? Where do things break down?

---

### NOW ARGUE BACK

Here's the constraint: you cannot use "as we scale" or any growth projection.
Find a coordination problem that exists right now, at current headcount.

Fill in this form. All four fields. No skipping.

  ROLE UNDER PRESSURE: [pick one role from ROLE-NAME LOCK]
  OBSERVABLE BREAKDOWN: [what coordination failure is that role experiencing today]
  WHY EXISTING MECHANISMS FAIL: [pick one mechanism from your table above — why doesn't
    it fix this breakdown]
  RE-ASSESSMENT TRIGGER: [if you're wrong about needing structure, what specific thing
    would prove it — a hire count, a milestone, a structural symptom you can count]

---

### CALL IT

  FLAT-CASE-PRESSURE: [Strong / Moderate / Weak / Negligible / Insufficient] — [one sentence]

Then pick one:
  CAN-OPERATE-FLAT — [say when and under what conditions]
  STRUCTURE-WARRANTED — [say what specific failure the structure fixes]

If your mechanisms table has mostly "Yes" entries but you're picking STRUCTURE-WARRANTED,
explain the contradiction. The verdict should be consistent with the evidence.

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

### DRAW THE ORG

Show me the structure as an ASCII diagram.

Rules:
- At least two levels of hierarchy
- Committees are their own labeled nodes with connectors — they don't live inside an area box
- Every role name you put in the diagram must be in your ROLE-NAME LOCK
- Use real box-drawing characters: ┌ ─ ┐ └ ┘ │ ├ └

Make sure the role you named under ROLE UNDER PRESSURE has a clear home in this diagram.
That's the coordination failure the structure is supposed to fix.

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

### HEADCOUNT TABLE

Five columns. Do not merge Decides and Escalates into one column — they answer
different questions.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

Format for Key Roles: [role name] ([domain type])
Close the table with a **Total** row. Add up the headcounts.

### OPERATING RHYTHM

Three rows minimum. Cover at least: the weekly ops meeting, a gate or shiproom,
and the governance meeting. Don't combine two of these into one row.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DRI / Owner: ROLE-NAME LOCK only.

---

### COMMITTEE CHARTERS

For each governance meeting in your rhythm table, write a charter. Five fields.
Missing a field means the charter is incomplete.

**[Committee Name] Charter**
- Purpose: [what problem it resolves]
- Membership: [role] ([domain type]), [role] ([domain type]) — two minimum
- Decides: [what it has authority to resolve]
- Escalates: [where it routes what it can't decide — name the destination, not "everything else"]
- Quorum: [N] of [M] member roles required for binding decisions

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

### ORG-ELEMENT REGISTER

Four categories. Don't leave any empty.

  ORG-ELEMENT REGISTER
  cat-1 (Areas): [each area with headcount]
  cat-2 (Committees/Cadences): [each committee and rhythm meeting by name]
  cat-3 (Headcount): Total = N
  cat-4 (DRI Roles): [roles that own entries in the rhythm table or charter decisions]

---

### HOW THIS ORG WOULD EVOLVE

Two rows. Row 1 is a headcount threshold. Row 2 is something different.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | ... | Headcount threshold |
| [workload signal, structural symptom, or milestone] | ... | [different type] |

Two headcount thresholds don't count. Pick a different category for Row 2.

---

### WHAT COULD GO WRONG

Before the table: declare the citation schema.

  CAT-N-CITATION-SCHEMA
  Pull codes from your ORG-ELEMENT REGISTER:
    cat-1 = Areas | cat-2 = Committees/Cadences | cat-3 = Headcount | cat-4 = DRI Roles
  Every "Why It Applies Here" cell must open with: [element name] (cat-N) —
  No org element gets named in that column without its cat-N code.

Then the table:

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [name] | [element] (cat-N) — [why this element is specifically at risk] | [action] |
| [name] | [element] (cat-N) — ... | ... |

Two rows minimum. Connect these back to the coordination problem you named in the rebuttal —
the org was designed to fix something specific; the anti-patterns should be the ways
that fix could erode.

---

### AMEND MODE

If you get an AMEND instruction: change only what's asked. Mark changed sections [AMENDED].
If roles change, update ROLE-NAME LOCK first and then check every section for stale references.
If headcount changes, update the Total row.
Don't regenerate sections that didn't change.
```

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence | Front-loading ROLE-NAME LOCK as first artifact reduces downstream drift |
| V-02 | Inertia framing | Adversarial advocate framing produces more honest verdicts |
| V-03 | Output format | Schema-declared tables before each section eliminate partial-compliance |
| V-04 | Role sequence + Lifecycle emphasis | Numbered phases with gate lines as execution assertions reduce ordering failures |
| V-05 | Phrasing register + Inertia framing | Conversational imperative register with position-taking framing reduces hedging |
