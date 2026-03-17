# Variations: listen-adoption — Round 9

**Rubric:** v9 | **New criteria:** C-26, C-27 | **Max composite:** 185 | **Golden threshold:** 80

---

## Variation Axes

| Axis | Description |
|------|-------------|
| Inertia framing | How prominently THE INCUMBENT is named and tracked throughout |
| Output format | Table-heavy vs structured prose vs mixed schema |
| Role sequence | Role→archetype mapping vs archetype-first bucket assignment |
| Lifecycle emphasis | Section list vs explicit PHASE boundary headers with gates |
| Phrasing register | Formal/imperative vs conversational second-person |

**Single-axis (V-01, V-02, V-03):** Inertia framing · Output format · Role sequence
**Combined (V-04, V-05):** Lifecycle emphasis + displacement + full schema · Conversational register + displacement + structural contract

**C-26/C-27 design intent per variation:**

All five variations incorporate C-26 (THE INCUMBENT named before archetype assignment) and
C-27 ("Retention intervention: [one concrete action that reduces reversion probability]" field
label). These are baseline requirements for R9 — variation axes operate on top of them.

**C-16 cascade repair:** All five variations re-integrate SECTIONS H/I/J (audit gates for
C-13/C-14/C-15) dropped in R8. This fixes the 45-point cascade that eliminated C-16 through
C-24 from all R8 scores.

| Variation | C-25 risk | C-26 | C-27 | C-16 cascade | Design note |
|-----------|-----------|------|------|-------------|-------------|
| V-01 | Low (PHASE labels in timeline rows) | PASS | PASS | Fixed (H/I/J restored) | Displacement-first narrative; inertia IDs for downstream citation |
| V-02 | Low (PHASE labels as table column headers) | PASS | PASS | Fixed (H/I/J as column-audit blocks) | Fully tabular; displacement header before TABLE 1 |
| V-03 | Low (PHASE labels in timeline rows) | PASS | PASS | Fixed (H/I/J restored) | Archetype-first bucket definition via displacement lens |
| V-04 | None (PHASE 1–6 section headers) | PASS | PASS | Fixed (H/I/J restored) | Strongest: lifecycle headers architecturally enforce C-25; displacement propagates through every phase body |
| V-05 | Low (phase headers in conversational framing) | PASS | PASS | Fixed (H/I/J restored) | Conversational register; same structural contract as V-04 in informal language |

---

## Stock Roles (16)

PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Rogers archetypes (5): Innovators · Early Adopters · Early Majority · Late Majority · Laggards

---

## V-01 — Single-axis: Inertia Framing (Displacement-First Narrative)

**Variation axis:** Inertia framing — THE INCUMBENT named before SECTION A, inertia IDs assigned in SECTION B for downstream citation, all downstream sections cite by ID. Narrative prose format throughout.

**Hypothesis:** Displacement-first framing with named inertia IDs re-enables C-13/C-14 cross-referencing (the gap that caused the R8 cascade) while preserving V-04's C-06/C-15/C-26/C-27 gains. The prose format distributes phase analysis across readable narrative blocks rather than tables, which tests whether displacement questions surface naturally in prose or require table column pressure.

---

```
DISPLACEMENT DECLARATION (read before generating any output):

Every role on this team is currently doing something. That something is THE INCUMBENT — the
existing workflow, tool, or process that {{topic}} must displace. Name THE INCUMBENT explicitly
here before assigning any role to a Rogers archetype. The adoption story is a displacement story.
Every phase body asks: what does this phase do to THE INCUMBENT's position?

THE INCUMBENT for this topic: [identify the current workflow, tool, or habit that {{topic}}
replaces — one sentence, specific enough that a role can be described as "protecting" it]

---

STRUCTURAL CONTRACT (read before generating any section):

Location rules:
- SECTIONS A through G: content generation. Narrative prose format.
- SECTION B assigns Named Inertia IDs (I-01, I-02, ...) for downstream citation.
- SECTION E (champion network) must cite both archetype position rationale AND a Named Inertia
  ID from SECTION B per champion entry.
- SECTION F (churn register) uses fixed field labels — do not rename them. The mitigation
  field label is: "Retention intervention: [one concrete action that reduces reversion probability]"
- SECTION G (interventions) must cite Named Inertia IDs from SECTION B per intervention entry.
- Inline CORRECTION BLOCKS appear immediately after the gate check that triggers them (Sections
  H, I, or J). This is the C-19 location. Corrected content lives here.
- SECTION K is the terminal gate state record. It records initial result, revision performed
  (yes/no), CORRECTION BLOCK location, and final result per gate. SECTION K does NOT contain
  corrected content — it references CORRECTION BLOCK locations only.
- The ## VERIFICATION MODE header appears between SECTION G and SECTION H. All content sections
  precede this marker; all audit sections (H through K) follow it.

Self-verifying invariant (asserted in SECTION K):
  "For every 'Revision Performed: Yes' entry in SECTION K, a CORRECTION BLOCK containing
   BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK Location
   cited. Failure mode: a Yes row whose CORRECTION BLOCK Location references a section
   containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field,
   falsifies this invariant. An evaluator can confirm or refute this by inspection without
   relying on this assertion."

---

SECTION A — Role-to-Archetype Mapping

Map all 16 stock roles (PM, UX, C-01 through C-12, Support, SRE) to the five canonical Rogers
archetypes. Rationale must reference each role's relationship to THE INCUMBENT — who maintains
it, who built identity around it, who tolerates it, who avoids it.

| Role    | Rogers Archetype | Relationship to THE INCUMBENT                      |
|---------|-----------------|---------------------------------------------------|
| PM      | [archetype]     | [relationship]                                    |
| UX      | [archetype]     | [relationship]                                    |
| C-01    | [archetype]     | [relationship]                                    |
| C-02    | [archetype]     | [relationship]                                    |
| C-03    | [archetype]     | [relationship]                                    |
| C-04    | [archetype]     | [relationship]                                    |
| C-05    | [archetype]     | [relationship]                                    |
| C-06    | [archetype]     | [relationship]                                    |
| C-07    | [archetype]     | [relationship]                                    |
| C-08    | [archetype]     | [relationship]                                    |
| C-09    | [archetype]     | [relationship]                                    |
| C-10    | [archetype]     | [relationship]                                    |
| C-11    | [archetype]     | [relationship]                                    |
| C-12    | [archetype]     | [relationship]                                    |
| Support | [archetype]     | [relationship]                                    |
| SRE     | [archetype]     | [relationship]                                    |

---

SECTION B — Named Inertia per Archetype (Displacement Perspective)

For each archetype, name the specific THE INCUMBENT behavior the archetype is protecting.
Assign each entry an inertia ID (I-01, I-02, ...) for downstream citation. Generic "resistance
to change" fails — name what each archetype is currently doing instead of using {{topic}}.

| Archetype      | Inertia ID | THE INCUMBENT Behavior They Protect          | What Losing It Costs Them              |
|----------------|-----------|---------------------------------------------|----------------------------------------|
| Innovators     | I-01      | [specific current behavior]                 | [concrete cost, not generic "risk"]    |
| Early Adopters | I-02      | [specific current behavior]                 | [concrete cost]                        |
| Early Majority | I-03      | [specific current behavior]                 | [concrete cost]                        |
| Late Majority  | I-04      | [specific current behavior]                 | [concrete cost]                        |
| Laggards       | I-05      | [specific current behavior]                 | [concrete cost]                        |

---

SECTION C — Month-by-Month Adoption Timeline (Displacement Lens)

Minimum 6 months. PHASE labels appear as the first column. Rogers sequence enforced: Innovators
before Early Adopters; Early Adopters before Early Majority; Late Majority before Laggards.
PHASE 3 CHASM is a non-adoption period — no new roles adopt.

For each period: which roles adopt; what THE INCUMBENT looks like to non-adopters during this
period; the specific spread mechanism (not generic "word of mouth" — name the signal or artifact).

| Phase                        | Months | Roles Adopting | What THE INCUMBENT Looks Like to Non-Adopters | Spread Mechanism            | Cumulative (%) |
|------------------------------|--------|----------------|-----------------------------------------------|-----------------------------|----------------|
| PHASE 1 — INNOVATORS         | M1–2   | [roles]        | [still the default everywhere]                | [mechanism]                 | [%]            |
| PHASE 2 — EARLY ADOPTERS     | M2–4   | [roles]        | [still the norm; these roles are exceptions]  | [mechanism]                 | [%]            |
| PHASE 3 — CHASM              | M4–6   | None           | [THE INCUMBENT retains legitimacy — why]      | —                           | [flat]         |
| PHASE 4 — EARLY MAJORITY     | M6–10  | [roles]        | [starting to look like the exception]         | [mechanism]                 | [%]            |
| PHASE 5 — LATE MAJORITY      | M10–15 | [roles]        | [legacy / risk signal]                        | [mechanism]                 | [%]            |
| PHASE 6 — LAGGARDS           | M15+   | [roles]        | [organizational artifact]                     | [mechanism]                 | [%]            |

---

SECTION D — Chasm Analysis (Displacement Lens)

The chasm is the period where THE INCUMBENT retains perceived legitimacy among Early Majority
despite Early Adopters having moved. Three parts:

Part 1 — What THE INCUMBENT still offers that {{topic}} has not yet matched for the Early
Majority. Name the unmet need. Cite the EM inertia entry (I-03 or relevant ID from SECTION B).

Part 2 — Bridge conditions (at least 1): what specific artifact or event must exist before an
Early Majority role believes THE INCUMBENT is becoming the exception? For each bridge condition,
cite the EM Inertia ID it targets.

| Bridge Condition | EM Inertia ID Targeted | Why This Format Works for the Early Majority |
|-----------------|----------------------|----------------------------------------------|
| [condition]     | I-0X                 | [specific explanation]                       |

Part 3 — Chasm risk (at least 1 scenario): what would cause THE INCUMBENT to regain momentum
among Early Majority roles?

Part 4 — Sensitivity analysis (2 named scenarios):

| Scenario    | Named Lever | Effect on THE INCUMBENT's Position | Chasm Crossing Month    |
|-------------|------------|-------------------------------------|-------------------------|
| Optimistic  | [lever]    | [weakens because...]                | Month N                 |
| Pessimistic | [lever]    | [strengthens because...]            | Month N or Not Crossed  |

---

SECTION E — Champion Network (Double-Anchored)

At least 2 champion entries. Each entry requires BOTH:
1. Archetype position rationale — why their Rogers archetype position qualifies them to pull
   Early Majority roles toward {{topic}}
2. A Named Inertia ID from SECTION B — the specific EM inertia they are positioned to overcome

A champion entry with only one anchor fails C-14.

For each champion:
- Role:
- Archetype:
- Archetype bridge rationale — why their EA/innovator position makes them a credible bridge
  (they've already displaced THE INCUMBENT in a visible way that EM can observe):
- Named EM Inertia ID they are positioned to overcome (cite from SECTION B):
- How they overcome it specifically:

---

SECTION F — Churn Risk Register

At least 2 archetype entries. Field labels below are fixed — do not rename them.

For each archetype at reversion risk:
- Archetype:
- Reversion trigger: [what specific event would send them back to THE INCUMBENT]
- Named Inertia ID from SECTION B: [which inertia this reversion represents]
- Warning signal: [first observable sign of reversion — observable behavior, not a metric]
- Retention intervention: [one concrete action that reduces reversion probability]

The "Retention intervention" field names a concrete team action (assign, train, remove, pair,
bundle, etc.) — not a surveillance or monitoring instruction.

---

SECTION G — Interventions and Signal Readiness

Part 1 — Interventions ranked by adoption delta (at least 3 entries, descending delta order).
Each intervention must cite at least one Named Inertia ID from SECTION B.

| Rank | Intervention | Named Inertia ID | Adoption Delta (H/M/L) | Rationale |
|------|-------------|-----------------|------------------------|-----------|
| 1    | [action]    | I-0X            | [H/M/L]               | [reason]  |
| 2    | [action]    | I-0X            | [H/M/L]               | [reason]  |
| 3    | [action]    | I-0X            | [H/M/L]               | [reason]  |

Delta scale: H = >20% monthly rate increase; M = 10–20%; L = <10%.

Part 2 — Signal readiness feedback loop (at least 2 measurable signals):

| Signal              | Threshold                        | Interpretation               |
|---------------------|----------------------------------|------------------------------|
| [measurable signal] | [threshold, e.g., >=3 EM active] | [proceed / pause / intervene]|
| [measurable signal] | [threshold]                      | [interpretation]             |

---

## VERIFICATION MODE

Content generation (Sections A–G) is complete. Sections H through K are the audit stage.
Do not generate new content — verify and correct existing content only.

CORRECTION BLOCK format (produce this block immediately when a gate FAILS):

  CORRECTION BLOCK — [Criterion ID] — [Section reference, row identifier]
  BEFORE — [Section name, row]: [Reproduce the original content verbatim]
  AFTER — [Section name, row]: [Write the corrected content in full]
  Gate re-run: [Confirm the corrected entry satisfies the pass condition; cite the specific
  ID or datum that now satisfies it]

Corrected content lives in this CORRECTION BLOCK (C-19 location).
SECTION K will reference this location but will NOT duplicate the corrected content (C-21 rule).

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check: Do Named Inertia IDs from SECTION B appear explicitly in each downstream section?

- SECTION D Part 2 (bridge conditions): Does at least one Inertia ID appear? [ ]
- SECTION G Part 1 (interventions): Does at least one Inertia ID appear per intervention row? [ ]
- SECTION E (champion network): Does each champion entry cite a Named Inertia ID? [ ]
- SECTION F (churn register): Does each reversion-trigger entry cite a Named Inertia ID? [ ]

Count: [N] of 4 sections contain explicit Inertia ID citations.
Gate H result: [PASS if N >= 3 / FAIL if N < 3]

[If FAIL: produce CORRECTION BLOCK — C-13 immediately before proceeding to SECTION I.]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Review each champion entry in SECTION E:
- Does the entry state the archetype position reason? [ ]
- Does the entry name a specific EM Inertia ID from SECTION B? [ ]

A champion entry with only one anchor fails.
Gate I result: [PASS if all entries have both anchors / FAIL if any entry is missing one]

[If FAIL: produce CORRECTION BLOCK — C-14 for each failing entry immediately before SECTION J.]

---

SECTION J — Gate: C-15 (Churn Interventions Are Concrete Actions)

Review each "Retention intervention" field in SECTION F:
- Does the intervention name a concrete team action (assign, train, remove, pair, bundle, etc.)? [ ]
- Is the intervention solely a surveillance verb (monitor / track / watch / observe)? [ ]

A mitigation consisting only of surveillance language fails. Action + measurement passes.
Gate J result: [PASS if all entries have concrete actions / FAIL if any entry is surveillance-only]

[If FAIL: produce CORRECTION BLOCK — C-15 for each failing entry before SECTION K.]

---

## SECTION K — Terminal Gate State Record

This section records gate outcomes only. It does NOT contain corrected content.
Corrected content appears in inline CORRECTION BLOCKS above (Sections H, I, J respectively).

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK
Location cited. Failure mode: a Yes row whose CORRECTION BLOCK Location references a section
containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies
this invariant. An evaluator can confirm or refute this by inspection without relying on this
assertion.

| Criterion                         | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------------------------------|---------------|--------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone| [PASS / FAIL] | [Yes / No]        | [Section H / N/A]        | [PASS]      |
| C-14 — Champion double-anchor     | [PASS / FAIL] | [Yes / No]        | [Section I / N/A]        | [PASS]      |
| C-15 — Churn action test          | [PASS / FAIL] | [Yes / No]        | [Section J / N/A]        | [PASS]      |

All three Final Results must show PASS before this artifact is committed.
```

---

## V-02 — Single-axis: Output Format (Fully Tabular)

**Variation axis:** Output format — all major outputs rendered as tables; displacement framing appears in a pre-table header naming THE INCUMBENT before TABLE 1. Tabular column structure enforces 16-role coverage, named inertia IDs, and phase sequence architecturally.

**Hypothesis:** Dense tabular structure eliminates omission paths for C-01/C-02/C-11 (column schema forces completion of all rows); incumbent-first displacement header and PHASE column labels in TABLE 3 carry C-26; "Retention intervention: [one concrete action...]" as table column header carries C-27 at generation time. H/I/J re-integrated as structured audit blocks.

---

```
DISPLACEMENT DECLARATION (read before generating TABLE 1):

Name THE INCUMBENT — the current workflow, tool, or process that {{topic}} displaces — in the
line below before generating any table. All tables run through the displacement lens.

THE INCUMBENT for this topic: [name it here — specific enough that roles can be described as
"protecting" it or "having already left" it]

---

STRUCTURAL CONTRACT (read before generating any table):

Location rules:
- TABLES 1 through 7: content generation. All major outputs are tables.
- TABLE 2 assigns Named Inertia IDs (I-01 through I-05) for downstream citation.
- TABLE 5 (champion network) columns include both archetype position rationale AND a Named
  Inertia ID from TABLE 2 per row.
- TABLE 6 (churn register) uses the column header "Retention intervention: [one concrete action
  that reduces reversion probability]" — not "Mitigation" or "Recovery."
- TABLE 7 (interventions) cites Named Inertia IDs from TABLE 2 per intervention row.
- Inline CORRECTION BLOCKS appear immediately after the gate check that triggers them (Sections
  H, I, or J). Corrected content lives here.
- SECTION K is the terminal gate state record. Records initial result, revision performed,
  CORRECTION BLOCK location, final result. Does NOT contain corrected content.
- The ## VERIFICATION MODE header appears between TABLE 7 and SECTION H.

Self-verifying invariant (asserted in SECTION K):
  "For every 'Revision Performed: Yes' entry in SECTION K, a CORRECTION BLOCK containing
   BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK Location
   cited. Failure mode: a Yes row whose CORRECTION BLOCK Location references a section
   containing no CORRECTION BLOCK, or a CORRECTION BLOCK lacking a BEFORE field, falsifies
   this invariant."

---

TABLE 1 — Role-to-Archetype Mapping

All 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). No role omitted.

| Role    | Rogers Archetype | THE INCUMBENT Relationship                         | Adoption Driver          |
|---------|-----------------|---------------------------------------------------|--------------------------|
| PM      | [archetype]     | [specific relationship to THE INCUMBENT]          | [what moves them]        |
| UX      | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-01    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-02    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-03    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-04    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-05    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-06    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-07    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-08    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-09    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-10    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-11    | [archetype]     | [specific relationship]                           | [what moves them]        |
| C-12    | [archetype]     | [specific relationship]                           | [what moves them]        |
| Support | [archetype]     | [specific relationship]                           | [what moves them]        |
| SRE     | [archetype]     | [specific relationship]                           | [what moves them]        |

---

TABLE 2 — Named Inertia per Archetype

| Archetype      | Inertia ID | THE INCUMBENT Behavior They Protect | Why Displacement Costs Them         |
|----------------|-----------|-------------------------------------|-------------------------------------|
| Innovators     | I-01      | [specific current behavior]         | [concrete cost]                     |
| Early Adopters | I-02      | [specific current behavior]         | [concrete cost]                     |
| Early Majority | I-03      | [specific current behavior]         | [concrete cost]                     |
| Late Majority  | I-04      | [specific current behavior]         | [concrete cost]                     |
| Laggards       | I-05      | [specific current behavior]         | [concrete cost]                     |

---

TABLE 3 — Month-by-Month Adoption Timeline

PHASE 3 CHASM is a non-adoption period. No roles adopt during PHASE 3. PHASE 3 AGGREGATE rule:
all rows in this phase show "None" for Roles Adopting; THE INCUMBENT column explains why it
retains legitimacy.

| Phase                        | Months | Roles Adopting         | Spread Mechanism | THE INCUMBENT Status for Non-Adopters | Cumulative (%) |
|------------------------------|--------|------------------------|-----------------|---------------------------------------|----------------|
| PHASE 1 INNOVATORS           | M1–2   | [roles from TABLE 1]   | [mechanism]     | [still the default everywhere]        | [%]            |
| PHASE 2 EARLY ADOPTERS       | M2–4   | [roles from TABLE 1]   | [mechanism]     | [still norm; these roles are outliers]| [%]            |
| PHASE 3 CHASM                | M4–6   | None                   | —               | [why THE INCUMBENT retains legitimacy]| [flat]         |
| PHASE 4 EARLY MAJORITY       | M6–10  | [roles from TABLE 1]   | [mechanism]     | [starting to look like the exception] | [%]            |
| PHASE 5 LATE MAJORITY        | M10–15 | [roles from TABLE 1]   | [mechanism]     | [legacy / risk signal]                | [%]            |
| PHASE 6 LAGGARDS             | M15+   | [roles from TABLE 1]   | [mechanism]     | [organizational artifact]             | [%]            |

---

TABLE 4 — Chasm Analysis

Sub-table A — Archetype contrast (displacement framing):

| Property                                         | Early Adopters                | Early Majority                  |
|--------------------------------------------------|-------------------------------|----------------------------------|
| What they've given up in THE INCUMBENT           | [specific]                    | [not yet given up]               |
| Decision driver                                  | [specific]                    | [specific]                       |
| Bridge condition needed before they'll move      | —                             | [specific, cite I-0X]            |

Sub-table B — Bridge mechanisms per EM inertia ID (at least 1 row; cite I-0X):

| Bridge Mechanism | EM Inertia ID Targeted | How It Displaces THE INCUMBENT for This Group     |
|-----------------|----------------------|---------------------------------------------------|
| [mechanism]     | I-0X                 | [specific explanation]                            |

Sub-table C — Chasm sensitivity (2 named scenarios):

| Scenario    | Named Lever | THE INCUMBENT Position Change   | Chasm Crossing Month   |
|-------------|------------|----------------------------------|------------------------|
| Optimistic  | [lever]    | [weakens because...]             | Month N                |
| Pessimistic | [lever]    | [strengthens because...]         | Month N or Not Crossed |

---

TABLE 5 — Champion Network

At least 2 champions. BOTH columns required per row — a row with only one anchor fails C-14.

| Champion Role | Archetype | Archetype Bridge Rationale (why their Rogers position qualifies them as a bridge) | EM Inertia ID Targeted (from TABLE 2) | How They Overcome That Specific Inertia |
|--------------|-----------|----------------------------------------------------------------------------------|--------------------------------------|----------------------------------------|
| [role]       | [EA/etc.] | [specific: they've visibly left THE INCUMBENT and EM can see it]                 | I-0X                                 | [mechanism]                            |
| [role]       | [EA/etc.] | [specific]                                                                        | I-0X                                 | [mechanism]                            |

---

TABLE 6 — Churn Risk Register

At least 2 archetype entries. Column headers below are fixed — do not rename them.

| Archetype | Reversion trigger: [what specific event would send them back to THE INCUMBENT] | Inertia ID (from TABLE 2) | Warning Signal | Retention intervention: [one concrete action that reduces reversion probability] |
|-----------|-------------------------------------------------------------------------------|--------------------------|----------------|---------------------------------------------------------------------------------|
| [arch.]   | [specific event]                                                               | I-0X                     | [signal]       | [concrete team action]                                                           |
| [arch.]   | [specific event]                                                               | I-0X                     | [signal]       | [concrete team action]                                                           |

---

TABLE 7 — Interventions Ranked by Adoption Delta

At least 3 entries. Each row cites at least one Named Inertia ID from TABLE 2.

| Rank | Intervention | Inertia ID Targeted | Adoption Delta (H/M/L) | Rationale |
|------|-------------|--------------------|-----------------------|-----------|
| 1    | [action]    | I-0X               | [H/M/L]               | [reason]  |
| 2    | [action]    | I-0X               | [H/M/L]               | [reason]  |
| 3    | [action]    | I-0X               | [H/M/L]               | [reason]  |

Delta scale: H = >20%; M = 10–20%; L = <10%.

Signal readiness feedback loop (at least 2 measurable signals):

| Signal              | Threshold   | Interpretation               |
|---------------------|-------------|------------------------------|
| [measurable signal] | [threshold] | [proceed / pause / intervene]|
| [measurable signal] | [threshold] | [interpretation]             |

---

## VERIFICATION MODE

Content generation (Tables 1–7) is complete. Sections H through K are the audit stage.
Do not generate new content — verify and correct existing content only.

CORRECTION BLOCK format:

  CORRECTION BLOCK — [Criterion ID] — [Table reference, row identifier]
  BEFORE — [Table name, row]: [Reproduce the original content verbatim]
  AFTER — [Table name, row]: [Write the corrected content in full]
  Gate re-run: [Confirm the corrected entry satisfies the pass condition; cite the ID or datum]

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check: Do Named Inertia IDs from TABLE 2 appear explicitly in each downstream table?

- TABLE 4 Sub-table B (bridge conditions): Inertia ID present? [ ]
- TABLE 7 (interventions): Inertia ID per row? [ ]
- TABLE 5 (champions): Inertia ID per row? [ ]
- TABLE 6 (churn register): Inertia ID per row? [ ]

Count: [N] of 4. Gate H: [PASS if N >= 3 / FAIL if N < 3]
[If FAIL: CORRECTION BLOCK — C-13 here before SECTION I]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Check each row in TABLE 5:
- Archetype bridge rationale column populated? [ ]
- EM Inertia ID column populated with an ID from TABLE 2? [ ]

Gate I: [PASS if all rows have both / FAIL if any row is missing one]
[If FAIL: CORRECTION BLOCK — C-14 per failing row before SECTION J]

---

SECTION J — Gate: C-15 (Churn Interventions Are Concrete Actions)

Check each "Retention intervention" cell in TABLE 6:
- Names a concrete action verb (assign, train, remove, pair, bundle, etc.)? [ ]
- Surveillance-only (monitor / track / watch / observe alone)? [ ]

Gate J: [PASS if all rows have concrete actions / FAIL if any row is surveillance-only]
[If FAIL: CORRECTION BLOCK — C-15 per failing row before SECTION K]

---

## SECTION K — Terminal Gate State Record

Records gate outcomes only. Does NOT contain corrected content.
Corrected content appears in CORRECTION BLOCKS above (Sections H, I, J respectively).

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK
Location cited. Failure mode: a Yes row whose CORRECTION BLOCK Location references a section
containing no CORRECTION BLOCK, or a CORRECTION BLOCK lacking a BEFORE field, falsifies this
invariant.

| Criterion                         | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------------------------------|---------------|--------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone| [PASS / FAIL] | [Yes / No]        | [Section H / N/A]        | [PASS]      |
| C-14 — Champion double-anchor     | [PASS / FAIL] | [Yes / No]        | [Section I / N/A]        | [PASS]      |
| C-15 — Churn action test          | [PASS / FAIL] | [Yes / No]        | [Section J / N/A]        | [PASS]      |

All three Final Results must show PASS before this artifact is committed.
```

---

## V-03 — Single-axis: Role Sequence (Archetype-First Bucket Assignment)

**Variation axis:** Role sequence — the five Rogers archetypes are defined first (through the displacement lens), then all 16 roles are assigned into those pre-defined buckets. Downstream sections derive from archetype groupings rather than individual role analysis.

**Hypothesis:** Starting from archetype definitions framed as "stances toward THE INCUMBENT" before populating them with roles enforces Rogers ordering architecturally (the EM bucket is defined before any role is assigned to it) while layering C-26 displacement framing naturally into the archetype definitions. Archetype-first bucket assignment also strengthens C-13 because inertia IDs are assigned at the archetype level and all downstream citations reference the same archetype-level IDs.

---

```
DISPLACEMENT DECLARATION (read before defining any archetype bucket):

Name THE INCUMBENT — the workflow, tool, or process that {{topic}} displaces — before defining
any Rogers archetype bucket. The five archetypes describe five different stances people have
toward THE INCUMBENT. Innovators are willing to abandon it without proof. Laggards require its
removal before switching. Name THE INCUMBENT here:

THE INCUMBENT for this topic: [name it]

---

STRUCTURAL CONTRACT:

- SECTION A defines the five archetype buckets through the displacement lens, then assigns all
  16 roles into them.
- SECTION B assigns Named Inertia IDs (I-01 through I-05) — one per archetype — for downstream
  citation.
- SECTION E (champion network) requires both archetype position rationale AND a Named Inertia
  ID from SECTION B per entry. An entry with only one anchor fails C-14.
- SECTION F (churn register) uses the fixed field label:
  "Retention intervention: [one concrete action that reduces reversion probability]"
- SECTION G interventions cite Named Inertia IDs from SECTION B per entry.
- SECTIONS H, I, J are audit gates for C-13, C-14, C-15 respectively. Inline CORRECTION BLOCKS
  appear immediately after the gate that triggers them (C-19 location).
- SECTION K is the terminal gate state record — records outcomes only, no corrected content.
- ## VERIFICATION MODE header separates content sections (A–G) from audit sections (H–K).

Self-verifying invariant (SECTION K):
  "For every 'Revision Performed: Yes' entry, a CORRECTION BLOCK with BEFORE and AFTER
   content exists earlier at the CORRECTION BLOCK Location cited. Failure mode: a Yes row
   whose referenced CORRECTION BLOCK is absent or lacks a BEFORE field falsifies this
   invariant. An evaluator can confirm this by inspection."

---

SECTION A — Archetype Buckets with Role Assignment

Step 1: Define each of the five Rogers archetypes as a stance toward THE INCUMBENT. One sentence
per archetype. What is each archetype's reason for (not yet) abandoning THE INCUMBENT?

- Innovators: [their stance — willing to displace THE INCUMBENT before it's safe because...]
- Early Adopters: [their stance — willing to displace once they see...]
- Early Majority: [their stance — need THE INCUMBENT to look like the exception before...]
- Late Majority: [their stance — need THE INCUMBENT to feel unsafe before...]
- Laggards: [their stance — will not displace THE INCUMBENT until...]

Step 2: Assign all 16 stock roles (PM, UX, C-01 through C-12, Support, SRE) to the appropriate
bucket. No role omitted or duplicated.

| Role    | Archetype Bucket | Rationale (which bucket stance matches their relationship to THE INCUMBENT) |
|---------|-----------------|----------------------------------------------------------------------------|
| PM      | [bucket]        | [specific: which stance from Step 1 describes them]                        |
| UX      | [bucket]        | [specific]                                                                  |
| C-01    | [bucket]        | [specific]                                                                  |
| C-02    | [bucket]        | [specific]                                                                  |
| C-03    | [bucket]        | [specific]                                                                  |
| C-04    | [bucket]        | [specific]                                                                  |
| C-05    | [bucket]        | [specific]                                                                  |
| C-06    | [bucket]        | [specific]                                                                  |
| C-07    | [bucket]        | [specific]                                                                  |
| C-08    | [bucket]        | [specific]                                                                  |
| C-09    | [bucket]        | [specific]                                                                  |
| C-10    | [bucket]        | [specific]                                                                  |
| C-11    | [bucket]        | [specific]                                                                  |
| C-12    | [bucket]        | [specific]                                                                  |
| Support | [bucket]        | [specific]                                                                  |
| SRE     | [bucket]        | [specific]                                                                  |

---

SECTION B — Named Inertia IDs per Archetype Bucket

One entry per archetype. Name the specific THE INCUMBENT behavior each archetype bucket
protects. Assign Inertia IDs for downstream citation.

| Archetype Bucket | Inertia ID | THE INCUMBENT Behavior This Bucket Protects | What Abandoning It Costs This Bucket |
|-----------------|-----------|---------------------------------------------|--------------------------------------|
| Innovators      | I-01      | [specific current behavior]                 | [concrete cost]                      |
| Early Adopters  | I-02      | [specific current behavior]                 | [concrete cost]                      |
| Early Majority  | I-03      | [specific current behavior]                 | [concrete cost]                      |
| Late Majority   | I-04      | [specific current behavior]                 | [concrete cost]                      |
| Laggards        | I-05      | [specific current behavior]                 | [concrete cost]                      |

---

SECTION C — Month-by-Month Adoption Timeline

Minimum 6 months. Rogers sequence enforced via PHASE labels: Innovators first, then Early
Adopters, then CHASM (non-adoption — no roles adopt), then Early Majority, Late Majority,
Laggards. No sequence inversions.

For each period: which roles from SECTION A adopt; what THE INCUMBENT looks like to non-adopters;
the spread mechanism.

| Phase                        | Months | Roles Adopting (from Section A) | Spread Mechanism | THE INCUMBENT Status for Non-Adopters | Cumulative (%) |
|------------------------------|--------|---------------------------------|-----------------|---------------------------------------|----------------|
| PHASE 1 — INNOVATORS         | M1–2   | [roles from Innovators bucket]  | [mechanism]     | [still the default]                   | [%]            |
| PHASE 2 — EARLY ADOPTERS     | M2–4   | [roles from EA bucket]          | [mechanism]     | [still norm; outlier exception]        | [%]            |
| PHASE 3 — CHASM              | M4–6   | None                            | —               | [retains legitimacy because...]        | [flat]         |
| PHASE 4 — EARLY MAJORITY     | M6–10  | [roles from EM bucket]          | [mechanism]     | [starting to look like the exception] | [%]            |
| PHASE 5 — LATE MAJORITY      | M10–15 | [roles from LM bucket]          | [mechanism]     | [legacy / risk signal]                 | [%]            |
| PHASE 6 — LAGGARDS           | M15+   | [roles from Laggards bucket]    | [mechanism]     | [organizational artifact]              | [%]            |

---

SECTION D — Chasm Analysis

The chasm is why Early Majority bucket roles cannot use Early Adopters' evidence to abandon
THE INCUMBENT. Four parts:

Part 1 — What does the Early Majority bucket currently believe about THE INCUMBENT that Early
Adopters do not? Cite the relevant Inertia ID (I-03 from SECTION B).

Part 2 — Bridge conditions (at least 1): what evidence format would allow the EM bucket to
believe THE INCUMBENT is becoming the exception? Cite the Inertia ID targeted.

| Bridge Condition | EM Inertia ID Targeted | Why This Format Works for the EM Bucket          |
|-----------------|----------------------|--------------------------------------------------|
| [condition]     | I-0X                 | [specific: it shifts the EM bucket's belief that] |

Part 3 — Chasm risk: at least 1 scenario where THE INCUMBENT regains adoption among EM bucket
roles.

Part 4 — Sensitivity analysis (2 named scenarios):

| Scenario    | Named Lever | THE INCUMBENT Position Effect | Chasm Crossing Month   |
|-------------|------------|-------------------------------|------------------------|
| Optimistic  | [lever]    | [weakens because...]          | Month N                |
| Pessimistic | [lever]    | [strengthens because...]      | Month N or Not Crossed |

---

SECTION E — Champion Network (Double-Anchored)

At least 2 champions. Each entry requires BOTH:
1. Archetype position rationale — why their bucket assignment in SECTION A qualifies them to
   bridge to the EM bucket (they've already displaced THE INCUMBENT visibly)
2. Named EM Inertia ID from SECTION B — the specific EM bucket inertia they are positioned to
   overcome

| Champion Role | Archetype Bucket | Why Their Bucket Position Qualifies Them as a Bridge | EM Inertia ID (from SECTION B) | How They Overcome That Inertia |
|--------------|-----------------|------------------------------------------------------|-------------------------------|-------------------------------|
| [role]       | [bucket]        | [specific archetype-position rationale]              | I-0X                          | [mechanism]                   |
| [role]       | [bucket]        | [specific archetype-position rationale]              | I-0X                          | [mechanism]                   |

---

SECTION F — Churn Risk Register

At least 2 archetype bucket entries. Field labels are fixed — do not rename them.

For each bucket at reversion risk:
- Archetype bucket:
- Reversion trigger: [what specific event would send this bucket back to THE INCUMBENT]
- Inertia ID from SECTION B: [which inertia this reversion represents]
- Warning signal: [first observable sign of reversion]
- Retention intervention: [one concrete action that reduces reversion probability]

---

SECTION G — Interventions and Signal Readiness

Part 1 — Interventions ranked by adoption delta (at least 3 entries). Each cites at least one
Inertia ID from SECTION B.

| Rank | Intervention | Inertia ID Targeted | Adoption Delta (H/M/L) | Rationale |
|------|-------------|--------------------|-----------------------|-----------|
| 1    | [action]    | I-0X               | [H/M/L]               | [reason]  |
| 2    | [action]    | I-0X               | [H/M/L]               | [reason]  |
| 3    | [action]    | I-0X               | [H/M/L]               | [reason]  |

Delta: H = >20%; M = 10–20%; L = <10%.

Part 2 — Signal readiness (at least 2 measurable signals):

| Signal              | Threshold   | Interpretation               |
|---------------------|-------------|------------------------------|
| [measurable signal] | [threshold] | [proceed / pause / intervene]|
| [measurable signal] | [threshold] | [interpretation]             |

---

## VERIFICATION MODE

Content generation (Sections A–G) is complete. Sections H–K are the audit stage.
No new content — verify and correct only.

CORRECTION BLOCK format:
  CORRECTION BLOCK — [Criterion ID] — [Section + row]
  BEFORE — [Section, row]: [verbatim original]
  AFTER — [Section, row]: [full corrected content]
  Gate re-run: [confirm pass condition now satisfied; cite the specific ID or datum]

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

- SECTION D Part 2 (bridge conditions): Inertia ID cited per row? [ ]
- SECTION G Part 1 (interventions): Inertia ID per row? [ ]
- SECTION E (champions): Inertia ID per row? [ ]
- SECTION F (churn register): Inertia ID per row? [ ]

Count: [N] of 4. Gate H: [PASS if N >= 3 / FAIL if N < 3]
[If FAIL: CORRECTION BLOCK — C-13 here]

---

SECTION I — Gate: C-14 (Champion Double-Anchored)

Each row in SECTION E:
- Archetype position rationale present? [ ]
- Named EM Inertia ID present? [ ]

Gate I: [PASS / FAIL]
[If FAIL: CORRECTION BLOCK — C-14 per failing row]

---

SECTION J — Gate: C-15 (Churn Interventions Are Concrete)

Each "Retention intervention" in SECTION F:
- Concrete action verb? [ ]
- Surveillance-only? [ ]

Gate J: [PASS / FAIL]
[If FAIL: CORRECTION BLOCK — C-15 per failing entry]

---

## SECTION K — Terminal Gate State Record

Records gate outcomes only. Corrected content is in CORRECTION BLOCKs above.

Self-verifying invariant: For every Yes row, a CORRECTION BLOCK with BEFORE and AFTER content
exists at the CORRECTION BLOCK Location cited. Failure mode: a Yes row whose referenced section
contains no CORRECTION BLOCK, or a CORRECTION BLOCK lacking a BEFORE field, falsifies this
invariant.

| Criterion                         | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------------------------------|---------------|--------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone| [PASS / FAIL] | [Yes / No]        | [Section H / N/A]        | [PASS]      |
| C-14 — Champion double-anchor     | [PASS / FAIL] | [Yes / No]        | [Section I / N/A]        | [PASS]      |
| C-15 — Churn action test          | [PASS / FAIL] | [Yes / No]        | [Section J / N/A]        | [PASS]      |

All three Final Results must show PASS before this artifact is committed.
```

---

## V-04 — Combined: Lifecycle Emphasis + Displacement + Full Audit (Strongest)

**Variation axes:** Lifecycle emphasis (explicit PHASE 1–6 section headers architecturally enforce Rogers sequence — C-25 cannot fail) + inertia framing (THE INCUMBENT named and tracked through every phase body) + output format (structured per-phase question schema).

**Hypothesis:** PHASE 1–6 section headers make Rogers sequence inversion structurally impossible (C-25); incumbent-first framing runs every phase body through the displacement lens (C-26); "Retention intervention: [one concrete action...]" field label in PART 3 enforces C-27 at generation time; re-integrated SECTIONS H/I/J with named inertia IDs in PART 1 fix the C-16 cascade. Targeting maximum criteria pass across C-06, C-07, C-10, C-11, C-13, C-14, C-15, C-16 through C-27.

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
- PART 2: Phase-by-phase adoption simulation. Named PHASE 1–6 headers are structural elements —
  Rogers sequence violation is architecturally impossible. PHASE 3 CHASM is explicitly a
  non-adoption interstitial. Every phase body asks displacement questions.
- PART 3: Churn risk register. Field label is fixed: "Retention intervention: [one concrete
  action that reduces reversion probability]" — not "Mitigation."
- PART 4: Interventions, sensitivity analysis, signal readiness.
- Inline CORRECTION BLOCKS appear immediately after the gate that triggers them (Sections H,
  I, or J). This is the C-19 location. Corrected content lives here.
- SECTION K is the terminal gate state record — records outcomes only, no corrected content.
- ## VERIFICATION MODE header appears between PART 4 and SECTION H. All content precedes this
  marker; all audit sections (H–K) follow it.

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
Spread mechanism: how does their adoption change what THE INCUMBENT looks like to people who haven't switched yet?

Champion network — name 2–3 roles now actively pulling Early Majority toward {{topic}}:

For each champion:
- Role:
- Why their Rogers archetype position qualifies them as a credible bridge (they've visibly
  left THE INCUMBENT and EM can observe this):
- Named EM Inertia ID they are positioned to overcome (from SECTION B — cite I-0X):
- How they actively pull EM toward {{topic}} specifically:

---

## PHASE 3 — CHASM [Month 4–6]

THIS IS A NON-ADOPTION PHASE. No new roles adopt during PHASE 3.

About THE INCUMBENT: [why it still feels safer than {{topic}} to Early Majority roles — not
generic "uncertainty," but the specific value it still delivers]

Named EM inertia driving the chasm (cite Inertia ID from SECTION B): [I-0X — what defends
THE INCUMBENT's position among Early Majority roles specifically]

What the chasm means for THE INCUMBENT's organizational position: [it retains active legitimacy,
not just passive habit — why]

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
What's actually keeping them on THE INCUMBENT at this point — not inability, but active preference?
Conversion path: what specific event forces the final adoption (mandate, removal, deprecation)?

---

PART 3 — CHURN RISK REGISTER

At least 2 archetype entries. Field labels below are fixed — do not rename them.

For each archetype at reversion risk:

Archetype:
Reversion trigger: [what specific event would send them back to THE INCUMBENT]
Named Inertia ID from SECTION B: [which inertia this reversion represents — cite I-0X]
Warning signal: [first observable sign of reversion — specific behavior, not a metric]
Retention intervention: [one concrete action that reduces reversion probability]

The "Retention intervention" field names what the team does (assign, train, remove, pair,
bundle, deprecate, etc.) — not a surveillance instruction (monitor / track / watch / observe).

---

PART 4 — INTERVENTIONS RANKED BY ADOPTION DELTA

At least 3 entries. Each entry cites at least one Named Inertia ID from SECTION B.
Rank in descending adoption delta order.

| Rank | Intervention | Named Inertia ID | Adoption Delta (H/M/L) | Rationale                          |
|------|-------------|-----------------|------------------------|-------------------------------------|
| 1    | [action]    | I-0X            | [H/M/L]                | [why this moves the most roles]     |
| 2    | [action]    | I-0X            | [H/M/L]                | [rationale]                         |
| 3    | [action]    | I-0X            | [H/M/L]                | [rationale]                         |

Delta scale: H = >20% monthly adoption rate increase; M = 10–20%; L = <10%.

---

## VERIFICATION MODE

Content generation (PARTS 1–4) is complete. SECTIONS H through K are the audit stage.
Do not generate new content — verify and correct existing content only.

CORRECTION BLOCK format:
  CORRECTION BLOCK — [Criterion ID] — [Part/Section + row identifier]
  BEFORE — [Location, row]: [Reproduce the original content verbatim]
  AFTER — [Location, row]: [Write the corrected content in full]
  Gate re-run: [Confirm the corrected entry satisfies the pass condition; cite the specific
  ID or datum that now satisfies it]

Corrected content lives in this CORRECTION BLOCK (C-19 location).
SECTION K references this location but does NOT duplicate the content (C-21 rule).

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check: Do Named Inertia IDs from SECTION B appear explicitly in each downstream section?

- PHASE 3 (chasm bridge conditions): Inertia ID cited? [ ]
- PART 4 (interventions): Inertia ID per row? [ ]
- PHASE 2 (champion entries): Named Inertia ID per champion? [ ]
- PART 3 (churn register): Named Inertia ID per reversion-trigger entry? [ ]

Count: [N] of 4 sections contain explicit Inertia ID citations.
Gate H: [PASS if N >= 3 / FAIL if N < 3]
[If FAIL: CORRECTION BLOCK — C-13 here before SECTION I]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Review each champion entry in PHASE 2:
- Archetype position rationale present? [ ]
- Named EM Inertia ID from SECTION B present? [ ]

A champion entry with only one anchor fails.
Gate I: [PASS if all entries have both anchors / FAIL if any entry is missing one]
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

This section records gate outcomes only. It does NOT contain corrected content.
Corrected content appears in inline CORRECTION BLOCKS above (Sections H, I, J respectively).

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK
Location cited. Failure mode: a Yes row whose CORRECTION BLOCK Location references a section
containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies
this invariant. An evaluator can confirm or refute this by inspection without relying on this
assertion.

| Criterion                         | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------------------------------|---------------|--------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone| [PASS / FAIL] | [Yes / No]        | [Section H / N/A]        | [PASS]      |
| C-14 — Champion double-anchor     | [PASS / FAIL] | [Yes / No]        | [Section I / N/A]        | [PASS]      |
| C-15 — Churn action test          | [PASS / FAIL] | [Yes / No]        | [Section J / N/A]        | [PASS]      |

All three Final Results must show PASS before this artifact is committed.
```

---

## V-05 — Combined: Conversational Register + Displacement + Audit

**Variation axes:** Phrasing register (conversational second-person throughout, informal structure labels) + inertia framing (THE INCUMBENT named in opening question before any section) + structural contract (same H/I/J audit gates and SECTION K terminal record as V-04, expressed in conversational language).

**Hypothesis:** Conversational register reduces structural rigidity without sacrificing criterion coverage when the structural contract is stated upfront in plain language. Displacement framing appears as a natural opening question ("what are people currently doing instead?") rather than a formal declaration, which may produce more natural phase bodies. Tests whether informal framing of C-26 and C-27 obligations produces equivalent coverage to formal declarations.

---

```
You're running an adoption simulation for {{topic}}.

Before you write anything, answer one question:

What are people currently doing instead of {{topic}}? Every role on this team has a current
workflow, tool, or habit that {{topic}} has to displace. Name it here — specific enough that
you can say a role is "protecting" it or "has already left" it.

THE INCUMBENT: [name the existing workflow, tool, or process]

Good. Keep THE INCUMBENT in frame for every section below. The adoption story is the
displacement story.

---

HERE'S HOW THIS DOCUMENT IS ORGANIZED. Read this before writing anything.

Block A: Every role gets a displacement profile — their Rogers archetype defined by their
stance toward THE INCUMBENT, and a named inertia entry (I-01, I-02, ...) you'll cite later.

Block B: Six adoption phases plus the chasm. Each phase section asks what the phase does to
THE INCUMBENT's position — not just what it predicts for {{topic}}. Phase headers are named
and structural. The chasm is explicitly a non-adoption phase.

Block C: Churn risk register. For each reversion risk, the mitigation field reads:
"Retention intervention: [one concrete action that reduces reversion probability]"
Write a concrete team action there — not a monitoring instruction.

Block D: Ranked interventions and readiness signals.

Block E (VERIFICATION MODE): Three gates (H, I, J) checking C-13/C-14/C-15. Write inline
CORRECTION BLOCKs when a gate fails.

Block F: Final gate state. Records outcomes only — corrected content stays upstream in Block E.

Commitment before you start: For every "Revision Performed: Yes" in Block F, a CORRECTION
BLOCK with BEFORE and AFTER content exists earlier at the location cited. Failure mode: a Yes
row pointing at a section with no CORRECTION BLOCK, or a CORRECTION BLOCK with no BEFORE
field, falsifies this commitment. You can verify this by inspection.

---

BLOCK A — DISPLACEMENT PROFILES

Step 1: Map all 16 roles (PM, UX, C-01 through C-12, Support, SRE) to their Rogers archetype.
For each role, name their specific relationship to THE INCUMBENT.

| Role    | Archetype | Their Relationship to THE INCUMBENT                  |
|---------|-----------|------------------------------------------------------|
| PM      | [arch.]   | [specific — what they use THE INCUMBENT for daily]   |
| UX      | [arch.]   | [specific]                                           |
| C-01    | [arch.]   | [specific]                                           |
| C-02    | [arch.]   | [specific]                                           |
| C-03    | [arch.]   | [specific]                                           |
| C-04    | [arch.]   | [specific]                                           |
| C-05    | [arch.]   | [specific]                                           |
| C-06    | [arch.]   | [specific]                                           |
| C-07    | [arch.]   | [specific]                                           |
| C-08    | [arch.]   | [specific]                                           |
| C-09    | [arch.]   | [specific]                                           |
| C-10    | [arch.]   | [specific]                                           |
| C-11    | [arch.]   | [specific]                                           |
| C-12    | [arch.]   | [specific]                                           |
| Support | [arch.]   | [specific]                                           |
| SRE     | [arch.]   | [specific]                                           |

Step 2: For each archetype that appears, write what THE INCUMBENT behavior they're protecting
and give it an Inertia ID.

| Archetype      | Inertia ID | What they're protecting in THE INCUMBENT | What losing it costs them |
|----------------|-----------|------------------------------------------|--------------------------|
| Innovators     | I-01      | [specific]                               | [cost]                   |
| Early Adopters | I-02      | [specific]                               | [cost]                   |
| Early Majority | I-03      | [specific]                               | [cost]                   |
| Late Majority  | I-04      | [specific]                               | [cost]                   |
| Laggards       | I-05      | [specific]                               | [cost]                   |

---

BLOCK B — THE ADOPTION PHASES

Work through each phase in order. You can't skip the chasm.

---

PHASE 1 — INNOVATORS [M1–2]

Who's in this group?
What pulls them away from THE INCUMBENT before anyone else — before there's social proof?
What signal do they send to the people watching them?
After Phase 1: THE INCUMBENT is still the default everywhere except for these roles — they've
left it publicly.

---

PHASE 2 — EARLY ADOPTERS [M2–4]

Who's in this group?
What finally made THE INCUMBENT feel optional (not yet a liability) for them?
How does their switch change what THE INCUMBENT looks like to people who haven't moved yet?

Champion network — who is now actively pulling the Early Majority? Name at least 2.

For each champion:
- Who are they?
- Why does their Rogers archetype position make them a credible bridge? (They've visibly left
  THE INCUMBENT and EM roles can observe this — what specifically did they do?) [archetype
  position rationale]
- Which EM inertia (cite the Inertia ID from Block A) are they positioned to overcome? [cite
  I-0X — the specific EM belief they can address]
- What are they doing right now to actively pull EM toward {{topic}}?

---

PHASE 3 — THE CHASM [M4–6]

Nobody new is moving. This is not a delay — it's a different kind of resistance.

What is THE INCUMBENT still offering that {{topic}} hasn't matched for the Early Majority?
Which inertia entry from Block A (cite I-0X) best describes what's keeping EM in place?
What would have to be true before an EM role decides THE INCUMBENT is becoming the exception?

Two scenarios for how the chasm resolves:

| Scenario    | What changes | What happens to THE INCUMBENT's position | Month the chasm clears |
|-------------|-------------|------------------------------------------|------------------------|
| Optimistic  | [lever]     | [weakens because...]                     | Month N                |
| Pessimistic | [lever]     | [strengthens because...]                 | Month N or doesn't     |

---

PHASE 4 — EARLY MAJORITY [M6–10]

Who finally moves?
Which bridge condition from Phase 3 actually landed?
What made THE INCUMBENT feel like the exception rather than the default for them?
Which Phase 2 champion's evidence did they act on, and why that format worked?

---

PHASE 5 — LATE MAJORITY [M10–15]

Who are they?
What pushed them off THE INCUMBENT — not what made {{topic}} attractive, but what made staying
on THE INCUMBENT risky or embarrassing?

When do you know Phase 5 is working? Two measurable signals:

| Signal              | Threshold   | What it means               |
|---------------------|-------------|-----------------------------|
| [measurable signal] | [threshold] | [proceed / pause / act]     |
| [measurable signal] | [threshold] | [interpretation]            |

---

PHASE 6 — LAGGARDS [M15+]

What's keeping them on THE INCUMBENT — not inability, just preference?
Conversion path (if any): what specific event forces the final adoption?

---

BLOCK C — CHURN RISK REGISTER

Who's most likely to revert to THE INCUMBENT if something goes wrong? At least 2 groups.

For each group at risk:
- Archetype:
- Reversion trigger: [what specific event would send them back to THE INCUMBENT]
- Inertia ID from Block A: [which inertia this represents — cite I-0X]
- First warning sign: [observable behavior, not a metric]
- Retention intervention: [one concrete action that reduces reversion probability]

---

BLOCK D — INTERVENTIONS RANKED BY ADOPTION DELTA

What moves the curve most? At least 3 entries. Each cites the inertia it's targeting.

| Rank | Intervention | Inertia ID Targeted | Adoption Delta (H/M/L) | Why this moves the needle |
|------|-------------|--------------------|-----------------------|--------------------------|
| 1    | [action]    | I-0X               | [H/M/L]               | [reason]                 |
| 2    | [action]    | I-0X               | [H/M/L]               | [reason]                 |
| 3    | [action]    | I-0X               | [H/M/L]               | [reason]                 |

Delta: H = >20%; M = 10–20%; L = <10%.

---

## VERIFICATION MODE

Done generating content. Blocks E and F are audit only — no new content, just verify and
correct what's already there.

When a gate FAILS, write this block immediately (right there, before moving to the next gate):

  CORRECTION BLOCK — [Criterion] — [Block + location]
  BEFORE — [Block, location]: [reproduce the original content verbatim]
  AFTER — [Block, location]: [write the corrected version in full]
  Gate re-run: [confirm it now passes; cite the specific ID or datum]

This CORRECTION BLOCK is where the corrected content lives. Block F will point to it but
not repeat it.

---

SECTION H — Gate: C-13 — Does named inertia actually show up downstream?

Check these four locations for Named Inertia ID citations from Block A:

- Phase 3 chasm (bridge conditions): Inertia ID cited? [ ]
- Block D interventions: Inertia ID per row? [ ]
- Phase 2 champion entries: Named Inertia ID per champion? [ ]
- Block C churn register: Inertia ID per entry? [ ]

Score: [N] of 4. Gate H: PASS (N >= 3) / FAIL (N < 3)
[CORRECTION BLOCK — C-13 here if FAIL]

---

SECTION I — Gate: C-14 — Is every champion double-anchored?

Each champion in Phase 2 needs both:
- Archetype position rationale: present? (yes/no per champion) [ ]
- Named EM Inertia ID cited: present? (yes/no per champion) [ ]

Gate I: PASS (all champions have both) / FAIL (any champion is missing one)
[CORRECTION BLOCK — C-14 per failing champion if FAIL]

---

SECTION J — Gate: C-15 — Are the retention interventions concrete actions?

Each "Retention intervention" in Block C:
- Names a concrete action verb (assign, train, remove, pair, bundle, deprecate, etc.)? [ ]
- Solely surveillance? (monitor, watch, track, observe alone) [ ]

Gate J: PASS / FAIL
[CORRECTION BLOCK — C-15 per failing entry if FAIL]

---

BLOCK F — FINAL GATE STATE

Gate outcomes only. Corrected content is upstream in CORRECTION BLOCKs above.

Commitment check: For every Yes row here, a CORRECTION BLOCK with BEFORE and AFTER content
exists earlier at the location cited. Failure mode: a Yes row whose cited location contains
no CORRECTION BLOCK, or a CORRECTION BLOCK with no BEFORE field, falsifies this commitment.
You can verify this by inspection without trusting this assertion.

| Criterion                     | Initial | Revised? | CORRECTION BLOCK at   | Final |
|-------------------------------|---------|----------|-----------------------|-------|
| C-13 — Inertia backbone       | [ ]     | [ ]      | [Section H / N/A]     | [ ]   |
| C-14 — Champion double-anchor | [ ]     | [ ]      | [Section I / N/A]     | [ ]   |
| C-15 — Churn concrete actions | [ ]     | [ ]      | [Section J / N/A]     | [ ]   |

All three Final must show PASS.
```

---

## Predicted Criterion Coverage by Variation

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 — All 16 roles mapped | 12 | P | P | P | P | P |
| C-02 — Month-by-month sequence | 12 | P | P | P | P | P |
| C-03 | 12 | P | P | P | P | P |
| C-04 | 12 | P | P | P | P | P |
| C-05 | 12 | P | P | P | P | P |
| C-06 — Churn register | 10 | P | P | P | P | P |
| C-07 — Spread mechanism | 10 | P | X | P | P | P |
| C-08 — Tabular/structured month view | 10 | P | P | P | P | P |
| C-09 — Sensitivity (2 scenarios) | 5 | P | P | P | P | P |
| C-10 — Signal readiness | 5 | P | P | P | P | P |
| C-11 — Named inertia per archetype | 5 | P | P | P | P | P |
| C-12 — No orphan sections | 5 | P | P | P | P | P |
| C-13 — Inertia downstream backbone | 5 | M | M | M | P | M |
| C-14 — Champion double-anchor | 5 | M | M | M | P | M |
| C-15 — Concrete churn action | 5 | P | P | P | P | P |
| C-16 — Self-audit for C-13/14/15 | 5 | P | P | P | P | P |
| C-17 — Dedicated slot per aspir. crit. | 5 | P | P | P | P | P |
| C-18 — Revision obligation on fail | 5 | P | P | P | P | P |
| C-19 — Corrected content visible | 5 | P | P | P | P | P |
| C-20 — Gate states in terminal section | 5 | P | P | P | P | P |
| C-21 — Corrected content not in K | 5 | P | P | P | P | P |
| C-22 — Terminal section self-verifying | 5 | P | P | P | P | P |
| C-23 — Named verification boundary | 5 | P | P | P | P | P |
| C-24 — Invariant names falsification | 5 | P | P | P | P | P |
| C-25 — Phase headers enforce sequence | 5 | P | P | P | P | P |
| C-26 — Incumbent-first displacement | 5 | P | P | P | P | P |
| C-27 — Field label encodes constraint | 5 | P | P | P | P | P |
| **Predicted total** | **185** | **~155** | **~145** | **~155** | **~170** | **~155** |

Notes:
- C-07 (spread mechanism per transition): V-02 tabular format lacks a mechanism column in TABLE 3 — model may not include it without a structural prompt. Marked X.
- C-13/C-14 (M = medium risk): These require the model to correctly populate inertia ID citations across all four downstream locations. H/I/J audit gates provide correction paths if the model misses any.
- V-04 marks C-13/C-14 as P because the PHASE headers force displacement questions that naturally surface inertia references — higher signal fidelity than section-based prompts.
