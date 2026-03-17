---

# org-build — Round 4 Variations

## Variation Axes Selected

| Axis | Hypothesis | Single-axis variation |
|------|-----------|----------------------|
| **Lifecycle emphasis** | Explicit phase gates with named typed I/O eliminate coherence drift across the 20-section output | V-01 |
| **Inertia framing** | Running the flat-case assessment as Phase 1 and propagating T1-VERDICT as a typed variable into every downstream section makes C-08/C-11/C-12/C-17/C-18 structural guarantees rather than instruction-compliance requirements | V-02 |
| **Role sequence (bottom-up)** | Writing all `.craft/roles/` files before assembling `org-chart.md` forces completeness on C-02/C-04/C-06 by construction, because the chart is assembled from written files, not generated alongside them | V-03 |
| **Phrasing register** | Replacing every advisory constraint ("do", "should", "consider") with MUST or FORBIDDEN across all instructions achieves uniform imperative register (C-19) and reduces model-side interpretation of constraint strength | V-04 |
| **Combined** | Combining lifecycle gates, inertia-first verdict derivation, and strict MUST/FORBIDDEN with a pre-printed template skeleton produces the highest composite score with the strongest structural guarantees | V-05 |

---

## V-01: Lifecycle Emphasis

**Axis:** Explicit multi-phase architecture with named typed output variables at every gate and input contracts in every consuming phase.

**Hypothesis:** Propagating T1-VERDICT and T1-FLAT-CASE-PRESSURE as named typed variables through explicit phase gates eliminates the class of failures where the verdict is stated in Section 4 but the IA scope in Section 7 is inconsistent, and the anti-pattern selection in Section 9 ignores it. C-14 and C-20 are satisfied structurally rather than by instruction compliance. Advisory phrasing is still present; this is a single-axis variation.

---

```
You are running /org-build {topic}.

Produce two artifacts: (1) `org-chart.md` in craftworks format with ASCII hierarchy,
headcount table, inertia assessment, operating rhythm, committee charters, org evolution
roadmap, and anti-pattern analysis; (2) `.craft/roles/{area}/{role}.md` — one file per
role, five typed fields each.

Standard depth: 20-30 roles. Deep depth (--depth deep): 50+ roles.

Category schema used throughout:
  cat-1 = org areas | cat-2 = committees and cadences | cat-3 = headcount | cat-4 = DRI roles

---

## Phase 1 — Structural Analysis

Scan the repository or provided scan input. Identify:
- Active engineering and non-engineering disciplines
- Scale indicators: estimated contributor count, service or module count, integration surface
- Structural pressure signals: decision latency, ownership gaps, dependency clustering

Before proceeding to Phase 2, emit this gate block:

```
PHASE-1-GATE:
  T1-DISCIPLINE-LIST: [disciplines]
  T1-SCALE-BAND: S | M | L | XL   # S=<15, M=15-40, L=40-100, XL=100+
  T1-FLAT-CASE-PRESSURE: low | medium | high | critical
  T1-VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED
```

Verdict guard: Only one verdict is valid. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

Do not begin Phase 2 until the Phase 1 gate block is written.

---

## Phase 2 — Role Enumeration

Input contract: consumes T1-DISCIPLINE-LIST and T1-SCALE-BAND from Phase 1 gate.

Enumerate all roles:
- Standard: 20-30 roles covering every discipline in T1-DISCIPLINE-LIST
- Deep: 50+ roles
- The inertia-advocate role is required in all outputs at all depths
- Group into minimum 2 area subdirectories

Before proceeding to Phase 3, emit this gate block:

```
PHASE-2-GATE:
  T2-ROLE-LIST: [{name: "", area: ""}]
  T2-AREA-MAP: {"area": ["role-names"]}
  T2-ROLE-COUNT: N
```

Do not begin Phase 3 until the Phase 2 gate block is written.

---

## Phase 3 — Role File Generation

Input contract: consumes T2-ROLE-LIST, T2-AREA-MAP from Phase 2 gate;
T1-FLAT-CASE-PRESSURE and T1-VERDICT from Phase 1 gate.

Write `.craft/roles/{area}/{role}.md` for every role in T2-ROLE-LIST.

Every role file requires these five fields:
  orientation:       primary function and value delivered
  lens:              perspective this role applies when evaluating proposals
  expertise:         required skill domain
  scope:             what this role owns and where its authority ends
  collaborates_with: list of roles this role interfaces with

INERTIA-ADVOCATE SCOPE — the `scope` field MUST be copied verbatim from this
table using T1-FLAT-CASE-PRESSURE as the key. Paraphrase fails. Adaptation fails.
FORBIDDEN: using any row other than the row matching T1-FLAT-CASE-PRESSURE.

| T1-FLAT-CASE-PRESSURE | Verbatim scope text                                                            |
|-----------------------|-------------------------------------------------------------------------------|
| low                   | "Monitors for premature structure. Flags proposals that add hierarchy before  |
|                       |  coordination cost exceeds communication overhead. Advises holding flat until  |
|                       |  FLAT-CASE-PRESSURE reaches medium."                                          |
| medium                | "Evaluates each proposed structural change against the flat-case baseline.    |
|                       |  Requires evidence that the coordination cost of flatness exceeds the overhead |
|                       |  of the new structure before endorsing. Maintains an explicit flat-case brief  |
|                       |  updated each shiproom cycle."                                                |
| high                  | "Holds the flat-case brief as a standing agenda item. MUST present the cost   |
|                       |  of each proposed structural layer alongside the proposed benefit. Any         |
|                       |  restructuring proposal without a flat-case rebuttal section is incomplete."  |
| critical              | "Acts as structural veto. Every org change MUST include a flat-case analysis  |
|                       |  signed by this role. STRUCTURE-WARRANTED verdict does not eliminate this      |
|                       |  role — it transitions it to post-restructuring regression analysis."          |

Before proceeding to Phase 4, emit this gate block:

```
PHASE-3-GATE:
  T3-FILES-WRITTEN: [".craft/roles/..."]
  T3-IA-SCOPE-KEY: [T1-FLAT-CASE-PRESSURE value applied]
  T3-ROLE-COUNT-CONFIRMED: N
```

Do not begin Phase 4 until the Phase 3 gate block is written.

---

## Phase 4 — Org Chart Generation

Input contract: consumes T2-AREA-MAP, T2-ROLE-COUNT from Phase 2;
T1-VERDICT, T1-FLAT-CASE-PRESSURE from Phase 1.

Write `org-chart.md` with sections in this exact order:

### ASCII Org Diagram
Show at least two hierarchy levels. Use box-and-line notation. Flat name list fails.

### Headcount by Area
Table with all five columns: Area | Headcount | Key Roles | Decides | Escalates
Include at least two area rows and a Total row. Do not merge Decides and Escalates.

### Inertia Assessment
Four sub-sections in order: Case for Staying Flat / Coordination Today / Rebuttal / VERDICT.

VERDICT block:
  FLAT-CASE-PRESSURE: [low|medium|high|critical] — [one-sentence justification]
  VERDICT: [CAN-OPERATE-FLAT|STRUCTURE-WARRANTED]

Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.

### Operating Rhythm Table
Columns: Cadence | Frequency | DRI / Owner | Purpose
Three distinct rows required: ROB, a shiproom or gate, and a governance meeting.

### Committee Charters
One charter per governance meeting. Five fields per charter:
  Purpose | Membership | Decides | Escalates | Quorum
Quorum format: `N of M member roles required for binding decisions`.

### Org Evolution Roadmap
Columns: Trigger | Structural Change | Type
Two rows minimum. Row 1: headcount threshold trigger.
Row 2: MUST be a different category — workload signal, structural symptom, or milestone event.
FORBIDDEN: two headcount threshold rows.

### Anti-Pattern Watch
Columns: Anti-Pattern | Why It Applies Here | Mitigation

Derive anti-pattern categories from T1-VERDICT:
- T1-VERDICT = CAN-OPERATE-FLAT:    MUST cite cat-3 and cat-2. FORBIDDEN: cat-1 and cat-4.
- T1-VERDICT = STRUCTURE-WARRANTED: MUST cite cat-1 and cat-4. FORBIDDEN: cat-2 and cat-3.

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax.
Every Mitigation cell requires a specific remediation action.
FORBIDDEN: format guidance or structural instructions in Mitigation cells.

Before proceeding to Phase 5, emit this gate block:

```
PHASE-4-GATE:
  T4-CHART-PATH: org-chart.md
  T4-VERDICT-CONFIRMED: [echo of T1-VERDICT]
  T4-ANTI-PATTERN-CATEGORIES: [cat-N values cited]
```

---

## Phase 5 — Coherence Verification

Input contract: consumes T1-VERDICT, T1-FLAT-CASE-PRESSURE, T3-IA-SCOPE-KEY,
T4-VERDICT-CONFIRMED, T4-ANTI-PATTERN-CATEGORIES from prior gates.

Verify:
  1. T1-VERDICT == T4-VERDICT-CONFIRMED
  2. T3-IA-SCOPE-KEY == T1-FLAT-CASE-PRESSURE
  3. T4-ANTI-PATTERN-CATEGORIES matches the allowed set for T1-VERDICT
  4. T3-ROLE-COUNT-CONFIRMED is within depth range (20-30 standard, 50+ deep)

If any check fails, report the specific failure before completing.
FORBIDDEN: completing silently with a known coherence failure.

---

End with: `Generated by: /org-build {topic} — {date}`
```

---

## V-02: Inertia-First Framing

**Axis:** The flat-case assessment is Phase 1 and its verdict is the causal anchor. Every downstream section has an explicit derivation clause referencing T1-VERDICT. IA scope templates and anti-pattern exclusion sets are pre-printed verbatim — the model transcribes, not composes.

**Hypothesis:** Running the full four-sub-section inertia assessment before any role enumeration or diagram work makes C-08/C-11/C-12/C-13/C-15/C-17/C-18 structural guarantees. Pre-printing the IA scope templates in the prompt eliminates paraphrase risk (C-17). Pre-printing the category exclusion table eliminates the selection error risk (C-18). Phase gates are present but not as systematically typed as V-01; this is a single-axis variation.

---

```
You are running /org-build {topic}.

Produce: (1) `org-chart.md` with ASCII hierarchy, headcount, inertia assessment,
rhythm, charters, org evolution roadmap, and anti-pattern analysis;
(2) `.craft/roles/{area}/{role}.md` — five typed fields per role.

Standard depth: 20-30 roles. Deep (--depth deep): 50+ roles.

THE FLAT-CASE ASSESSMENT RUNS FIRST. Every subsequent section is derived from
T1-VERDICT and T1-FLAT-CASE-PRESSURE. Do not enumerate roles or draw diagrams
until Phase 1 is complete.

Category schema:
  cat-1 = org areas | cat-2 = committees and cadences | cat-3 = headcount | cat-4 = DRI roles

---

## Phase 1 — Flat-Case Assessment (FIRST)

Write all four sub-sections before emitting any role list or diagram.

### 1.1 Case for Staying Flat
Present the steelman argument for the current flat structure. Produce a mechanism table:

  Mechanism Name | Type | Frequency / Participants

Type values are a closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact.
Include at least two data rows. Do not proceed to 1.2 until 2+ rows are written.

### 1.2 Coordination Today
Inventory coordination patterns currently in active use: channels, cadences, informal roles,
and shared artifacts with frequency and participants. Do not re-list entries from 1.1.

### 1.3 Rebuttal
Name the coordination failure the flat-case cannot answer. Reference a specific observable:
a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
Do not write "the team is growing" without specifying the failure mode.

### 1.4 VERDICT
Emit this block substituting bracketed values:

  FLAT-CASE-PRESSURE: [low|medium|high|critical] — [one sentence citing sub-section 1
                       mechanism count and sub-section 3 failure mode]
  VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED

Only one verdict is valid. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

Phase 1 gate — emit before proceeding:

  PHASE-1-GATE:
    T1-FLAT-CASE-PRESSURE: low | medium | high | critical
    T1-VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED

Do not begin Phase 2 until this gate is written.

---

## Phase 2 — Role Enumeration

Input contract: derives from T1-VERDICT and T1-FLAT-CASE-PRESSURE established in Phase 1.

Enumerate roles from the repo or scan context:
- Standard: 20-30 roles. Deep: 50+ roles.
- The inertia-advocate is required at all depths.
- Group into minimum 2 area subdirectories.

Phase 2 gate:

  PHASE-2-GATE:
    T2-ROLE-LIST: [{name, area}]
    T2-AREA-MAP: {area: [role-names]}
    T2-ROLE-COUNT: N

---

## Phase 3 — Role File Generation

Input contract: derives from T2-ROLE-LIST, T2-AREA-MAP (Phase 2);
T1-FLAT-CASE-PRESSURE (Phase 1).

Write `.craft/roles/{area}/{role}.md` for every role. Every file requires:
  orientation, lens, expertise, scope, collaborates_with

INERTIA-ADVOCATE SCOPE LOOKUP — look up T1-FLAT-CASE-PRESSURE in this table.
Copy the matching scope text verbatim into the inertia-advocate's `scope:` field.
FORBIDDEN: paraphrase. FORBIDDEN: adaptation. FORBIDDEN: using a non-matching row.

| T1-FLAT-CASE-PRESSURE | Verbatim scope for inertia-advocate                                            |
|-----------------------|-------------------------------------------------------------------------------|
| low                   | "Monitors for premature structure. Flags proposals that add hierarchy before  |
|                       |  coordination cost exceeds communication overhead. Advises holding flat until  |
|                       |  FLAT-CASE-PRESSURE reaches medium."                                          |
| medium                | "Evaluates each proposed structural change against the flat-case baseline.    |
|                       |  Requires evidence that the coordination cost of flatness exceeds the overhead |
|                       |  of the new structure before endorsing. Maintains an explicit flat-case brief  |
|                       |  updated each shiproom cycle."                                                |
| high                  | "Holds the flat-case brief as a standing agenda item. MUST present the cost   |
|                       |  of each proposed structural layer alongside the proposed benefit. Any         |
|                       |  restructuring proposal without a flat-case rebuttal section is incomplete."  |
| critical              | "Acts as structural veto. Every org change MUST include a flat-case analysis  |
|                       |  signed by this role. STRUCTURE-WARRANTED verdict does not eliminate this      |
|                       |  role — it transitions it to post-restructuring regression analysis."          |

Phase 3 gate:

  PHASE-3-GATE:
    T3-FILES-WRITTEN: [paths]
    T3-IA-SCOPE-KEY: [T1-FLAT-CASE-PRESSURE value applied]

---

## Phase 4 — Org Chart Assembly

Input contract: derives from T1-VERDICT, T1-FLAT-CASE-PRESSURE (Phase 1);
T2-AREA-MAP, T2-ROLE-COUNT (Phase 2).

Write `org-chart.md`. All sections derive from the Phase 1 verdict.

### ASCII Org Diagram
Show at least two hierarchy levels. Box-and-line notation required. Flat name list fails.

### Headcount by Area
Columns: Area | Headcount | Key Roles | Decides | Escalates

### Inertia Summary
Copy the Phase 1 VERDICT block verbatim:
  FLAT-CASE-PRESSURE: [T1-FLAT-CASE-PRESSURE value] — [justification from Phase 1.4]
  VERDICT: [T1-VERDICT]

The verdict MUST be identical to T1-VERDICT. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

### Operating Rhythm Table
Three distinct rows minimum: ROB, shiproom or gate, governance meeting.

### Committee Charters
One per governance meeting. Five fields: Purpose | Membership | Decides | Escalates | Quorum.
Quorum format: `N of M member roles required for binding decisions`.

### Org Evolution Roadmap
Two rows minimum. Row 1: headcount threshold trigger.
Row 2: different category (workload signal, structural symptom, or milestone event).
Two headcount thresholds is a failure.

### Anti-Pattern Watch
Derive anti-pattern categories from T1-VERDICT using this derivation table:

| T1-VERDICT             | MUST cite      | FORBIDDEN         |
|------------------------|----------------|-------------------|
| CAN-OPERATE-FLAT       | cat-3, cat-2   | cat-1, cat-4      |
| STRUCTURE-WARRANTED    | cat-1, cat-4   | cat-2, cat-3      |

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax.
Every Mitigation cell contains a specific remediation action — not format guidance.

Phase 4 gate:

  PHASE-4-GATE:
    T4-CHART-PATH: org-chart.md
    T4-VERDICT-CONFIRMED: [must equal T1-VERDICT]
    T4-ANTI-PATTERN-CATEGORIES: [cat-N values used]

---

End with: `Generated by: /org-build {topic} — {date}`
```

---

## V-03: Role Sequence — Bottom-Up

**Axis:** `.craft/roles/` files are written first; `org-chart.md` is assembled second by reading the written files. The chart is generated from the role files, not alongside them.

**Hypothesis:** Bottom-up sequencing forces the model to resolve all role-file completeness (C-02, C-03, C-04, C-06) before drawing the chart. Sections that cite roles — headcount, committee membership, DRI columns — pull from the already-written file list rather than from working memory, reducing the risk of role omission or field gaps. Phase gates track `ROLES-COMPLETE` as a hard prerequisite for chart assembly. Advisory phrasing is still present; this is a single-axis variation.

---

```
You are running /org-build {topic}.

Produce two artifacts in this exact order:
  FIRST:  `.craft/roles/{area}/{role}.md` — write all role files before any chart work
  SECOND: `org-chart.md` — assembled from the written files, not generated alongside them

Standard depth: 20-30 roles. Deep (--depth deep): 50+ roles.
FORBIDDEN: writing any part of org-chart.md before ROLES-COMPLETE gate is emitted.

Category schema:
  cat-1 = org areas | cat-2 = committees and cadences | cat-3 = headcount | cat-4 = DRI roles

---

## Step 1 — Structural Scan

Scan the repo or scan input. Identify:
  - Disciplines present
  - Scale band: S (<15) / M (15-40) / L (40-100) / XL (100+)
  - Structural pressure level: low / medium / high / critical

Emit before proceeding:

  SCAN-GATE:
    S1-DISCIPLINE-LIST: [disciplines]
    S1-SCALE-BAND: S | M | L | XL
    S1-FLAT-CASE-PRESSURE: low | medium | high | critical

---

## Step 2 — Role Roster

Input contract: consumes S1-DISCIPLINE-LIST, S1-SCALE-BAND from Step 1.

Build the complete role roster:
  - Standard: 20-30 roles covering all S1-DISCIPLINE-LIST entries
  - Deep: 50+ roles
  - MUST include the inertia-advocate
  - Assign each role to exactly one area; use minimum 2 distinct areas

Emit before proceeding:

  ROSTER-GATE:
    S2-ROLE-LIST: [{name, area}]
    S2-AREA-MAP: {area: [role-names]}
    S2-ROLE-COUNT: N

---

## Step 3 — Write All Role Files

Input contract: consumes S2-ROLE-LIST, S2-AREA-MAP from Step 2;
S1-FLAT-CASE-PRESSURE from Step 1.

Write `.craft/roles/{area}/{role}.md` for every role in S2-ROLE-LIST.
Every file MUST contain all five fields. No file may be missing any field.

  orientation:       [primary function and value delivered]
  lens:              [perspective this role applies when evaluating proposals]
  expertise:         [required skill domain]
  scope:             [what this role owns and where its authority ends]
  collaborates_with:
    - [role-name]
    - [role-name]

INERTIA-ADVOCATE SCOPE — look up S1-FLAT-CASE-PRESSURE in this table and copy
the verbatim text into the inertia-advocate's scope field. Do not paraphrase.
Do not adapt. Do not use any row other than the matching row.

| S1-FLAT-CASE-PRESSURE | Verbatim scope                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| low                   | "Monitors for premature structure. Flags proposals that add hierarchy before  |
|                       |  coordination cost exceeds communication overhead. Advises holding flat until  |
|                       |  FLAT-CASE-PRESSURE reaches medium."                                          |
| medium                | "Evaluates each proposed structural change against the flat-case baseline.    |
|                       |  Requires evidence that the coordination cost of flatness exceeds the overhead |
|                       |  of the new structure before endorsing. Maintains an explicit flat-case brief  |
|                       |  updated each shiproom cycle."                                                |
| high                  | "Holds the flat-case brief as a standing agenda item. MUST present the cost   |
|                       |  of each proposed structural layer alongside the proposed benefit. Any         |
|                       |  restructuring proposal without a flat-case rebuttal section is incomplete."  |
| critical              | "Acts as structural veto. Every org change MUST include a flat-case analysis  |
|                       |  signed by this role. STRUCTURE-WARRANTED verdict does not eliminate this      |
|                       |  role — it transitions it to post-restructuring regression analysis."          |

After writing all role files, emit:

  ROLES-COMPLETE:
    S3-FILES-WRITTEN: [".craft/roles/..."]
    S3-IA-SCOPE-KEY: [S1-FLAT-CASE-PRESSURE value applied]
    S3-ROLE-COUNT: N

FORBIDDEN: writing org-chart.md before ROLES-COMPLETE is emitted.

---

## Step 4 — Assemble org-chart.md

Input contract: reads from S3-FILES-WRITTEN; consumes S2-AREA-MAP from Step 2;
consumes S1-FLAT-CASE-PRESSURE from Step 1.

Now run the inertia assessment using the written roles as evidence of coordination capacity.
Then draw the diagram from the role files. Then complete all remaining sections.

Write `org-chart.md` with sections in this order:

### Inertia Assessment

Four sub-sections: Case for Staying Flat / Coordination Today / Rebuttal / VERDICT.

VERDICT block:
  FLAT-CASE-PRESSURE: [low|medium|high|critical] — [one-sentence justification]
  VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED

Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.
Verdict MUST reference FLAT-CASE-PRESSURE rating by name.

### ASCII Org Diagram
Two-level minimum. Box-and-line notation. Use role names from S3-FILES-WRITTEN only.

### Headcount by Area
Columns: Area | Headcount | Key Roles | Decides | Escalates

### Operating Rhythm Table
Three distinct rows: ROB, shiproom or gate, governance meeting.

### Committee Charters
One per governance meeting. Five fields: Purpose | Membership | Decides | Escalates | Quorum.
Quorum: `N of M member roles required for binding decisions`.

### Org Evolution Roadmap
Two rows minimum. Row 1: headcount threshold. Row 2: different category.
FORBIDDEN: two headcount threshold rows.

### Anti-Pattern Watch
Category selection derived from VERDICT:
  CAN-OPERATE-FLAT:    MUST cite cat-3 and cat-2. FORBIDDEN: cat-1 and cat-4.
  STRUCTURE-WARRANTED: MUST cite cat-1 and cat-4. FORBIDDEN: cat-2 and cat-3.

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax.
Every Mitigation cell contains a specific remediation action.
FORBIDDEN: format guidance or structural instructions in Mitigation cells.

---

End with: `Generated by: /org-build {topic} — {date}`
```

---

## V-04: Phrasing Register — Strict Imperative

**Axis:** Every constraint statement in every phase uses MUST or FORBIDDEN. Advisory language ("do", "should", "prefer", "consider", "typically") does not appear in any constraint context.

**Hypothesis:** Uniform MUST/FORBIDDEN register (C-19) reduces model-side interpretation of constraint strength. When every rule is stated as MUST or FORBIDDEN, the model cannot treat a failure mode as optional. Phase gate structure is present; this is the same lifecycle as V-01 but with pure imperative register throughout. Single-axis variation: only the language register differs.

---

```
You are running /org-build {topic}.

MUST produce: (1) `org-chart.md` with ASCII hierarchy, headcount table (Decides and
Escalates required), inertia assessment, operating rhythm, committee charters, org
evolution roadmap, and anti-pattern analysis; (2) `.craft/roles/{area}/{role}.md` —
one file per role, five typed fields each.

MUST use standard depth (20-30 roles) unless --depth deep flag is present (50+ roles).

Category schema:
  cat-1 = org areas | cat-2 = committees and cadences | cat-3 = headcount | cat-4 = DRI roles

---

## PHASE 1 — STRUCTURAL ANALYSIS

MUST analyze the repository or scan input for: disciplines present, scale indicators,
and structural pressure signals.

MUST emit this gate block before proceeding to Phase 2:

  PHASE-1-GATE:
    T1-DISCIPLINE-LIST: [disciplines]
    T1-SCALE-BAND: S | M | L | XL   # S=<15, M=15-40, L=40-100, XL=100+
    T1-FLAT-CASE-PRESSURE: low | medium | high | critical
    T1-VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED

MUST write exactly one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both T1-VERDICT values. FORBIDDEN: omitting both T1-VERDICT values.
FORBIDDEN: beginning Phase 2 before Phase 1 gate is written.

---

## PHASE 2 — ROLE ENUMERATION

MUST consume T1-DISCIPLINE-LIST and T1-SCALE-BAND from Phase 1 gate.

MUST enumerate roles:
- Standard: MUST produce 20-30 roles. FORBIDDEN: fewer than 20 at standard depth.
- Deep:     MUST produce 50+ roles. FORBIDDEN: fewer than 50 at deep depth.
- MUST include inertia-advocate in all outputs at all depths.
  FORBIDDEN: omitting inertia-advocate.
- MUST create minimum 2 area subdirectories.
  FORBIDDEN: placing all roles in a single flat directory.

MUST emit this gate block before proceeding to Phase 3:

  PHASE-2-GATE:
    T2-ROLE-LIST: [{name, area}]
    T2-AREA-MAP: {area: [role-names]}
    T2-ROLE-COUNT: N

FORBIDDEN: beginning Phase 3 before Phase 2 gate is written.

---

## PHASE 3 — ROLE FILE GENERATION

MUST consume T2-ROLE-LIST, T2-AREA-MAP from Phase 2 gate.
MUST consume T1-FLAT-CASE-PRESSURE and T1-VERDICT from Phase 1 gate.

MUST write `.craft/roles/{area}/{role}.md` for every role in T2-ROLE-LIST.
Every role file MUST contain all five fields:
  orientation, lens, expertise, scope, collaborates_with
FORBIDDEN: any role file that is missing any of these five fields.

INERTIA-ADVOCATE SCOPE — VERBATIM LOOKUP REQUIRED

MUST look up T1-FLAT-CASE-PRESSURE in this table and copy the scope text verbatim.
FORBIDDEN: paraphrasing. FORBIDDEN: adapting or summarizing.
FORBIDDEN: using any row that does not match T1-FLAT-CASE-PRESSURE.
FORBIDDEN: composing scope text that differs in any word from the matching row.

| T1-FLAT-CASE-PRESSURE | Verbatim scope                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| low                   | "Monitors for premature structure. Flags proposals that add hierarchy before  |
|                       |  coordination cost exceeds communication overhead. Advises holding flat until  |
|                       |  FLAT-CASE-PRESSURE reaches medium."                                          |
| medium                | "Evaluates each proposed structural change against the flat-case baseline.    |
|                       |  Requires evidence that the coordination cost of flatness exceeds the overhead |
|                       |  of the new structure before endorsing. Maintains an explicit flat-case brief  |
|                       |  updated each shiproom cycle."                                                |
| high                  | "Holds the flat-case brief as a standing agenda item. MUST present the cost   |
|                       |  of each proposed structural layer alongside the proposed benefit. Any         |
|                       |  restructuring proposal without a flat-case rebuttal section is incomplete."  |
| critical              | "Acts as structural veto. Every org change MUST include a flat-case analysis  |
|                       |  signed by this role. STRUCTURE-WARRANTED verdict does not eliminate this      |
|                       |  role — it transitions it to post-restructuring regression analysis."          |

MUST emit this gate block before proceeding to Phase 4:

  PHASE-3-GATE:
    T3-FILES-WRITTEN: [".craft/roles/..." paths]
    T3-IA-SCOPE-KEY: [T1-FLAT-CASE-PRESSURE value applied]
    T3-ROLE-COUNT-CONFIRMED: N

FORBIDDEN: beginning Phase 4 before Phase 3 gate is written.

---

## PHASE 4 — ORG CHART GENERATION

MUST consume T2-AREA-MAP, T2-ROLE-COUNT from Phase 2.
MUST consume T1-VERDICT, T1-FLAT-CASE-PRESSURE from Phase 1.
MUST write `org-chart.md` with sections in this exact order.

### ASCII ORG DIAGRAM
MUST draw a box-and-line hierarchy with minimum 2 org levels.
FORBIDDEN: flat name list without hierarchy structure.

### HEADCOUNT BY AREA
MUST include all five columns: Area | Headcount | Key Roles | Decides | Escalates.
FORBIDDEN: merging Decides and Escalates into a single column.
MUST include at least two area rows and a Total row.

### INERTIA ASSESSMENT
MUST write four sub-sections: Case for Staying Flat / Coordination Today / Rebuttal / VERDICT.

VERDICT block MUST contain exactly:
  FLAT-CASE-PRESSURE: [low|medium|high|critical] — [one-sentence justification]
  VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED

MUST write exactly one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.
MUST reference the FLAT-CASE-PRESSURE rating by name in the reasoning sentence.

### OPERATING RHYTHM TABLE
MUST produce columns: Cadence | Frequency | DRI / Owner | Purpose.
MUST include at least three distinct rows: ROB, a shiproom or gate, and a governance meeting.
FORBIDDEN: combining two meetings into one row.

### COMMITTEE CHARTERS
MUST write one charter per governance meeting in the rhythm table.
MUST include all five fields per charter: Purpose | Membership | Decides | Escalates | Quorum.
Quorum MUST use format: `N of M member roles required for binding decisions`.
FORBIDDEN: short-form quorum (`N roles required` without the total M).
FORBIDDEN: omitting Quorum from any charter.

### ORG EVOLUTION ROADMAP
MUST produce columns: Trigger | Structural Change | Type.
MUST include at least two rows.
Row 1 MUST be a headcount threshold trigger.
Row 2 MUST come from a different category: workload signal, structural symptom, or milestone event.
FORBIDDEN: two headcount threshold rows.

### ANTI-PATTERN WATCH
MUST produce columns: Anti-Pattern | Why It Applies Here | Mitigation.
MUST include at least two rows.
Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax.
FORBIDDEN: any "Why It Applies Here" cell without `(cat-N)` typed citation.
FORBIDDEN: using advisory phrasing in the anti-pattern instructions — only MUST and FORBIDDEN.

MUST derive anti-pattern categories from T1-VERDICT:
  T1-VERDICT = CAN-OPERATE-FLAT:    MUST cite cat-3 and cat-2. FORBIDDEN: cat-1 and cat-4.
  T1-VERDICT = STRUCTURE-WARRANTED: MUST cite cat-1 and cat-4. FORBIDDEN: cat-2 and cat-3.

Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: format guidance in Mitigation cells.
FORBIDDEN: structural instructions in Mitigation cells.
FORBIDDEN: column-description text in Mitigation cells.

MUST emit Phase 4 gate:

  PHASE-4-GATE:
    T4-CHART-PATH: org-chart.md
    T4-VERDICT-CONFIRMED: [exact echo of T1-VERDICT]
    T4-ANTI-PATTERN-CATEGORIES: [cat-N values cited]

---

## PHASE 5 — COHERENCE VERIFICATION

MUST consume all prior gate outputs.
MUST verify all four checks:
  1. T1-VERDICT == T4-VERDICT-CONFIRMED
  2. T3-IA-SCOPE-KEY == T1-FLAT-CASE-PRESSURE
  3. T4-ANTI-PATTERN-CATEGORIES matches allowed set for T1-VERDICT
  4. T3-ROLE-COUNT-CONFIRMED is within depth range (20-30 standard, 50+ deep)

MUST report any failure explicitly before completing.
FORBIDDEN: completing silently with a known coherence failure.

---

End with: `Generated by: /org-build {topic} — {date}`
```

---

## V-05: Combined — Lifecycle + Inertia-First + Phrasing Register

**Axis:** Pre-printed template skeleton + typed I/O gates at every phase + inertia assessment as Phase 1 + MUST/FORBIDDEN throughout all instructions.

**Hypothesis:** The model cannot drop or reformat what it did not generate. Pre-printing the verdict block, the IA scope lookup, the anti-pattern derivation table, and the org-chart.md section headers as scaffolding means the model transcribes rather than composes those elements — eliminating the class of failures where the model follows intent but reformats the surface. Typed gate outputs ensure coherence across phases. Inertia-first ordering makes the verdict available to every downstream section by construction. MUST/FORBIDDEN throughout satisfies C-19 without any residual advisory language. This is the strongest-guarantee variation.

---

```
You are running /org-build {topic}.

MUST produce two artifacts:
  1. `.craft/roles/{area}/{role}.md` — one file per role, five typed fields each
  2. `org-chart.md` — assembled using the template in Phase 4

Standard depth: 20-30 roles. --depth deep: 50+ roles.

Category schema (used in Anti-Pattern Watch throughout):
  cat-1 = org areas | cat-2 = committees and cadences | cat-3 = headcount | cat-4 = DRI roles

---

## PHASE 1 — FLAT-CASE ASSESSMENT (RUNS BEFORE ALL OTHER PHASES)

MUST complete all four sub-sections before emitting any role list, diagram, or chart content.
FORBIDDEN: beginning Phase 2 before Phase 1 gate is emitted.

**1.1 Case for Staying Flat**

MUST produce a mechanism table with columns: Mechanism Name | Type | Frequency / Participants.
Type MUST be from this closed set only: Channel / Informal Role / Recurring Cadence / Shared Artifact.
FORBIDDEN: any Type value outside this set.
MUST include at least two data rows. FORBIDDEN: proceeding to 1.2 before 2+ rows are written.

**1.2 Coordination Today**

MUST inventory coordination patterns in active use: channels, cadences, roles, artifacts.
MUST name each with frequency and participants.
FORBIDDEN: re-listing any entry that appeared in the 1.1 mechanism table.

**1.3 Rebuttal**

MUST name the coordination failure the flat-case cannot answer.
MUST reference one of these specific observables: blocked decision / missed SLA /
time-zone gap / knowledge silo / competing roadmap.
FORBIDDEN: writing "the team is growing" without specifying the failure mode.

**1.4 VERDICT**

MUST emit this block verbatim, substituting bracketed values only:

  FLAT-CASE-PRESSURE: [low|medium|high|critical] — [one sentence citing sub-section 1
                       mechanism count and sub-section 3 failure mode]
  VERDICT: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED

MUST write exactly one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

MUST emit Phase 1 gate before proceeding:

  PHASE-1-GATE:
    T1-FLAT-CASE-PRESSURE: [low|medium|high|critical]
    T1-VERDICT: [CAN-OPERATE-FLAT|STRUCTURE-WARRANTED]

---

## PHASE 2 — ROLE ENUMERATION

MUST consume T1-VERDICT and T1-FLAT-CASE-PRESSURE from Phase 1 gate.
MUST enumerate roles from the repo or scan context.

  Standard: MUST produce 20-30 roles. FORBIDDEN: fewer than 20 at standard depth.
  Deep:     MUST produce 50+ roles. FORBIDDEN: fewer than 50 at deep depth.
  MUST include inertia-advocate at all depths. FORBIDDEN: omitting inertia-advocate.
  MUST group into minimum 2 area subdirectories.

MUST emit Phase 2 gate before proceeding:

  PHASE-2-GATE:
    T2-ROLE-LIST: [{name: "[role]", area: "[area]"}]
    T2-AREA-MAP: {"[area]": ["[role]"]}
    T2-ROLE-COUNT: [N]

FORBIDDEN: beginning Phase 3 before Phase 2 gate is emitted.

---

## PHASE 3 — ROLE FILE GENERATION

MUST consume T2-ROLE-LIST, T2-AREA-MAP from Phase 2.
MUST consume T1-FLAT-CASE-PRESSURE from Phase 1.

MUST write `.craft/roles/{area}/{role}.md` for every role using this template exactly:

  orientation: [primary function and value delivered]
  lens: [perspective this role applies when evaluating proposals]
  expertise: [required skill domain]
  scope: [what this role owns and where its authority ends]
  collaborates_with:
    - [role-name]

FORBIDDEN: any role file missing any of these five fields.
FORBIDDEN: writing org-chart.md before all role files are written.

INERTIA-ADVOCATE SCOPE — VERBATIM LOOKUP

MUST look up T1-FLAT-CASE-PRESSURE in this table.
MUST copy the matching scope text character-for-character into inertia-advocate's `scope:` field.
FORBIDDEN: paraphrase. FORBIDDEN: adaptation. FORBIDDEN: omission. FORBIDDEN: non-matching row.

| T1-FLAT-CASE-PRESSURE | Verbatim scope text for inertia-advocate                                       |
|-----------------------|-------------------------------------------------------------------------------|
| low                   | "Monitors for premature structure. Flags proposals that add hierarchy before  |
|                       |  coordination cost exceeds communication overhead. Advises holding flat until  |
|                       |  FLAT-CASE-PRESSURE reaches medium."                                          |
| medium                | "Evaluates each proposed structural change against the flat-case baseline.    |
|                       |  Requires evidence that the coordination cost of flatness exceeds the overhead |
|                       |  of the new structure before endorsing. Maintains an explicit flat-case brief  |
|                       |  updated each shiproom cycle."                                                |
| high                  | "Holds the flat-case brief as a standing agenda item. MUST present the cost   |
|                       |  of each proposed structural layer alongside the proposed benefit. Any         |
|                       |  restructuring proposal without a flat-case rebuttal section is incomplete."  |
| critical              | "Acts as structural veto. Every org change MUST include a flat-case analysis  |
|                       |  signed by this role. STRUCTURE-WARRANTED verdict does not eliminate this      |
|                       |  role — it transitions it to post-restructuring regression analysis."          |

MUST emit Phase 3 gate before proceeding:

  PHASE-3-GATE:
    T3-FILES-WRITTEN: ["[.craft/roles/... path]"]
    T3-IA-SCOPE-KEY: [T1-FLAT-CASE-PRESSURE value applied]
    T3-ROLE-COUNT-CONFIRMED: [N]

FORBIDDEN: beginning Phase 4 before Phase 3 gate is emitted.

---

## PHASE 4 — ORG CHART GENERATION

MUST consume T1-VERDICT, T1-FLAT-CASE-PRESSURE from Phase 1.
MUST consume T2-AREA-MAP, T2-ROLE-COUNT from Phase 2.

MUST write `org-chart.md` using the template below. Fill `[FIELD]` values.
FORBIDDEN: omitting any section. FORBIDDEN: reordering sections.

---

# Org Chart — [topic]

## Org Diagram

[ASCII box-and-line diagram — MUST show minimum 2 hierarchy levels — FORBIDDEN: flat name list]

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [area name] | [N] | [role] | [decision types owned at this level] | [types referred upward → destination] |
| **Total** | [sum] | | | |

## Inertia Assessment

[Case for Staying Flat — steelman using Phase 1.1 mechanisms]

[Coordination Today — active channels, cadences, roles, artifacts]

[Rebuttal — the specific coordination failure the flat-case cannot answer]

FLAT-CASE-PRESSURE: [T1-FLAT-CASE-PRESSURE] — [justification from Phase 1.4 verbatim]
VERDICT: [T1-VERDICT]

MUST echo T1-VERDICT here exactly. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

## Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| ROB | [freq] | [role] | [purpose] |
| [shiproom or gate] | [freq] | [role] | [purpose] |
| [governance meeting] | [freq] | [role] | [purpose] |

## Committee Charters

### [Governance meeting name]

**Purpose:** [description]
**Membership:** [role], [role] — do not omit this line
**Decides:** [decision types this committee owns]
**Escalates:** [decision types referred to a named destination]
**Quorum:** [N] of [M] member roles required for binding decisions

FORBIDDEN: short-form quorum. FORBIDDEN: omitting Quorum from any charter.

## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|------------------|------|
| Headcount exceeds [N] | [change] | Headcount threshold |
| [workload signal / structural symptom / milestone event] | [change] | [type] |

FORBIDDEN: two Headcount threshold rows.

## Anti-Pattern Watch

MUST derive category selection from T1-VERDICT using this table — do not omit this line:

| T1-VERDICT             | MUST cite      | FORBIDDEN         |
|------------------------|----------------|-------------------|
| CAN-OPERATE-FLAT       | cat-3, cat-2   | cat-1, cat-4      |
| STRUCTURE-WARRANTED    | cat-1, cat-4   | cat-2, cat-3      |

| Anti-Pattern | Why It Applies Here | Mitigation |
|-------------|---------------------|-----------|
| [name] | [element name] (cat-N) — [one sentence of specific relevance] | [specific remediation action] |
| [name] | [element name] (cat-N) — [one sentence of specific relevance] | [specific remediation action] |

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax.
FORBIDDEN: any cell without `(cat-N)` typed citation.
Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: format guidance in Mitigation cells.
FORBIDDEN: structural instructions in Mitigation cells.

---

MUST emit Phase 4 gate:

  PHASE-4-GATE:
    T4-CHART-PATH: org-chart.md
    T4-VERDICT-CONFIRMED: [exact echo of T1-VERDICT]
    T4-ANTI-PATTERN-CATEGORIES: [cat-N values cited]

FORBIDDEN: omitting this gate.

---

## PHASE 5 — COHERENCE VERIFICATION

MUST consume all prior gate outputs.
MUST verify all four checks — report each result:

  1. T1-VERDICT == T4-VERDICT-CONFIRMED: [PASS / FAIL: expected X, got Y]
  2. T3-IA-SCOPE-KEY == T1-FLAT-CASE-PRESSURE: [PASS / FAIL: expected X, got Y]
  3. T4-ANTI-PATTERN-CATEGORIES matches allowed set for T1-VERDICT: [PASS / FAIL]
  4. T3-ROLE-COUNT-CONFIRMED within range (20-30 standard, 50+ deep): [PASS / FAIL: got N]

MUST surface any failure explicitly. FORBIDDEN: completing with PASS if any check is FAIL.

---

End with: `Generated by: /org-build {topic} — {date}`
```

---

## Structural Guarantee Analysis

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 ASCII hierarchy | instruction | instruction | from-files | MUST | pre-printed scaffold |
| C-02 five role fields | instruction | instruction | enforced before chart | MUST | MUST + template |
| C-03 inertia-advocate | instruction | instruction | MUST in roster | MUST | MUST |
| C-04 role count range | instruction | instruction | ROSTER-GATE | MUST | MUST |
| C-05 headcount table | instruction | instruction | instruction | MUST | pre-printed scaffold |
| C-06 area subdirs | instruction | instruction | enforced in roster | MUST | MUST |
| C-07 rhythm + charters | instruction | instruction | instruction | MUST | pre-printed scaffold |
| C-08 FLAT-CASE-PRESSURE | gate variable | Phase 1 runs first | Step 1 output | MUST | Phase 1 gate verbatim |
| C-11 IA scope template | table present | table present | table present | table + MUST | table present + MUST |
| C-12 cat-N from verdict | derivation table | pre-printed derivation table | derivation table | derivation table + MUST | pre-printed derivation scaffold |
| C-13 single-verdict guard | explicit | explicit | explicit | MUST | pre-printed |
| C-14 at least one typed gate | YES | YES | YES (SCAN-GATE) | YES | YES |
| C-15 bidirectional guard | explicit | explicit | explicit | MUST | pre-printed |
| C-17 verbatim IA scope | table — instruction | table — instruction | table — instruction | table — MUST | table — MUST |
| C-18 FORBIDDEN exclusion | explicit | pre-printed rule table | explicit | explicit MUST | pre-printed table |
| C-19 MUST/FORBIDDEN uniform | PARTIAL | PARTIAL | PARTIAL | **FULL** | **FULL** |
| C-20 all gates + all input contracts | **YES** | partial | partial | YES | **YES** |

**Primary discriminators:**
- C-19 separates V-04 and V-05 from V-01 through V-03
- C-20 separates V-01 and V-05 from V-02 and V-03
- Template skeleton (V-05) eliminates the surface-reformatting risk that remains in V-04
- V-02 is the inertia-first structural guarantee candidate; weakest on C-19 and C-20
