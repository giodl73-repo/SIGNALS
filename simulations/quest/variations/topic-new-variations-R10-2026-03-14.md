---

## Round 10 Variations — topic-new (v9 rubric)

Written to `simulations/quest/rubrics/topic-new-rubric-v9-variations-R10-2026-03-14.md`.

---

### Variation Legend

| Variation | Primary Axis | Hypothesis |
|-----------|-------------|------------|
| V-01 | C-29 as first-person consequence narration | "If I skip..." framing makes skip-cost personally salient rather than abstractly descriptive |
| V-02 | C-30 four-layer independence + sequential-treatment consequence | Naming the specific false-pass produced by sequential checking closes the last rationalization gap |
| V-03 | C-31 schema-row-order mirrors signal-table-column-order | F-01=Priority pre-conditions the model to place Priority first before the table template is reached |
| V-04 | All three new criteria via shared behavioral-prediction architecture + inertia framing | "Status-Quo Default" column, "ISOLATION CHECK" construct, and schema+table mirroring share one framing pattern |
| V-05 | Imperative register (STOP/CHECK) targeted at C-29/30/31 enforcement points | All-caps command markers make non-compliance register-visible; violation requires overriding an explicit command |

---

### Design rationale per variation

**V-01** uses `"If I Skip This Phase, I Will..."` as the C-29 consequence column header, with first-person cells throughout the pipeline overview. This is structurally equivalent to V-04's "If Skipped" from R9 but changes the grammatical subject from "the system" to "me." Hypothesis: first-person skip-cost narration produces stronger motivational binding because the model reads the consequence as a self-directed prediction, not a passive description of what breaks.

**V-02** extends V-03 (R9's strongest C-28 implementation) by adding a fourth layer to the independence instruction: after naming the evaluation mode (1), listing conditions (2), and issuing a closing prohibition (3), it adds a **consequence-of-sequential-treatment** statement (4) — a specific description of the false-pass that sequential checking produces (`3 rows present, cells empty, sequential check advances`). The fourth layer converts the independence instruction from a semantic rule to an operational warning: it names the exact failure mode the instruction prevents.

**V-03** tests a structural pre-conditioning hypothesis: if FIELD SCHEMA rows are ordered F-01=Priority, F-02=Namespace, F-03=Skill, F-04=Item Name, F-05=Owner Role (matching signal table column order), and the schema includes a note that "schema row order defines signal table column order," then a model reading the schema before the signal table template encounters Priority as the first field twice — once at schema-reading time and once at table-fill time. Prior rounds enforced C-31 only at the table template; this variation enforces it at the constraint-definition layer too.

**V-04** unifies all three new criteria under a **behavioral-prediction architecture**: the consequence column is named "Status-Quo Default (if phase skipped)" (what teams do when they skip, not just what breaks), C-30 uses "ISOLATION CHECK" as a named formal construct, and C-31 is enforced at both the schema level and the table level with an explicit note that the schema row order defines the column order. The inertia framing from R9 V-05 ("Teams default to 'high/medium/low'") is extended to every phase row in the overview and to every schema consequence cell.

**V-05** applies the imperative register from R9 V-03 ("STOP. READ...") specifically at the three new criteria enforcement points: `SKIP COST` as a bold column header (C-29), `INDEPENDENCE TEST` as the Phase 1 gate label (C-30), and `PRIORITY GOES FIRST` as a bold preamble before the signal table (C-31). The rest of the prompt uses CHECK/STOP markers consistently per R9 V-03 convention. The hypothesis is that register contrast — all-caps imperative at the exact enforcement point — makes non-compliance structurally legible as command override rather than guideline deviation.

---

### Structural invariants across all five variations

All five satisfy C-01–C-31. Discriminators are implementation strength, not compliance:

| Criterion | Where variations diverge |
|-----------|--------------------------|
| C-29 | Column header and cell framing: first-person (V-01), third-person (V-02/03), status-quo-default (V-04), SKIP COST all-caps (V-05) |
| C-30 | Instruction depth: two-layer (V-01/03), four-layer + false-pass consequence (V-02), named "ISOLATION CHECK" construct (V-04/05) |
| C-31 | Enforcement layer: table-only (V-01/02/05), schema-first (V-03/04) |
