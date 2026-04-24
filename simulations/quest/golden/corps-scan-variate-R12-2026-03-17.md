---
skill: quest-variate
skill_target: corps-scan
round: 12
date: 2026-03-17
rubric_version: 11
---

# Variate R12 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v11 rubric (270 pts,
44 criteria). R11's V-01 and V-02 both scored 270/270 under v11. C-41, C-42, C-43, and C-44 are
now invariants — ALL R12 variations must satisfy them. The variation axes govern HOW each
variation implements the typed hypothesis contract, the 4-state vocabulary, the weight-scoring
table, and the Net Score delta. They do not govern whether.

R11 axes already covered (not re-explored in R12):
- Hypothesis formalism — IF/PREDICT/FALSIFIED-BY structured claim; IS-FALSIFICATION-SIGNAL field
- Evidence weighting — deliberation as weight-scoring table; Net Score drives selection
- Amend ordering — hypothesis verdict as first amend field; C-16 debt secondary; chain audit
- Scan walk protocol — five numbered walk steps; step-scoped artifact types; outcome at Step 5
- Combination — structured claim + weight table + amend-as-verdict (axes 1+2+3)

R10 axes already covered (not re-explored):
- Hypothesis-first role sequence
- Detective register phrasing ("What I found. What I didn't find.")
- DARK SIGNALS as structured evidence table (named columns)
- REPO GRAIN vocabulary, with-grain vs against-grain
- Combination — hypothesis-first + DARK SIGNALS table + phase output footers

R9 axes already covered (not re-explored):
- Negative space inventory (DARK SIGNALS as block-list following Signal Schema)
- Phase output contracts at phase footers
- Downstream consumer annotations on YAML elements
- Criterion cluster naming as primary pre-check key
- Combination: negative space inventory + downstream consumer annotations

R12 explores four new single-axis variation axes and one combination. All five variations treat
C-41, C-42, C-43, and C-44 as structurally required. The variation axes concern the representation
and framing of these new invariants, not their presence.

1. **Typed field declarations** — C-41 is expressed as a typed schema block: each field carries
   an explicit type annotation (PREDICTED-MODE: enum[...], STRUCTURAL-PREDICTION: string(1 sentence),
   FALSIFICATION-SIGNAL: enum[...]). C-42 is declared as a STATE_ENUM contract at the top of the
   DARK SIGNALS section header before any entries are written, forcing the 4-state vocabulary into
   a named, referenceable definition. The C-43 table column headers carry type annotations
   ("DARK SIGNALS Penalty [label:string, magnitude:0-4]"). C-44 AMEND-A shows the Net Score
   arithmetic inline as a formula trace.
   Hypothesis: 270/270 — type annotations make field contracts machine-readable at definition sites;
   STATE_ENUM declared at the section header forces the vocabulary to appear once as a definition
   rather than implicitly through per-entry choices.

2. **Inertia-first framing** — The Inertia Advocate (C-24) is introduced as a named structural
   participant in GATE PHASE and appears in every subsequent phase. GATE names the Inertia
   Advocate as the primary consumer of the scan output ("This scan produces a draft that the
   Inertia Advocate will use to defend the current structure"). DARK SIGNALS entries carry a
   "Inertia Implication" sub-field (what the Inertia Advocate would argue from each absence). The
   C-43 weight table carries an "Inertia Cost" column alongside DARK SIGNALS Penalty, recording
   what the Inertia Advocate loses if that mode is selected. C-44 AMEND-A translates the Net Score
   delta into an Inertia Advocate migration burden statement.
   Hypothesis: 270/270 — inertia framing makes C-24 non-defeatable as a structural participant
   rather than a YAML comment; the Inertia Cost column extends C-43's structural forcing to C-24.

3. **Scan-compressed, deliberation-expanded** — GATE PHASE is minimal: a compact pre-check block
   and the C-41 typed claim with no elaboration. SCAN PHASE is lean: schema table and DARK SIGNALS
   block with no walk-prose preamble. DELIBERATE PHASE carries maximum depth: the C-43 weight
   table expands to 8 columns, each entry includes a scoring note, and a "Selection Proof" block
   below the table traces the full Net Score arithmetic for the winning mode and the eliminated
   runner-up with label citations. C-44 AMEND-A reproduces the Selection Proof delta by reference.
   Hypothesis: 270/270 — deliberation-heavy compression forces criterion density into the phase
   where selection logic lives; the Selection Proof block makes C-43/C-44 independently auditable.

4. **Conversational imperative register** — Instructions are written in direct second-person
   imperatives with short, declarative sentences throughout. "Make this claim before you scan."
   "Walk the repo. Write a schema row for each signal you find." "Choose one vocabulary state for
   each DARK SIGNALS entry." Criterion labels appear in parentheses after the key verb ("Fill
   this table (C-43):") rather than in elaborate section headers. The 4-state C-42 vocabulary is
   presented as a "choose one:" numbered list. The Net Score formula is written as plain arithmetic:
   "Net = Evidence For minus Penalty." AMEND-A states the delta as a comparison sentence.
   Hypothesis: 270/270 — conversational register tests criterion survival under register
   transformation; criteria that require formal notation (C-NN IDs, section headers) are preserved
   but embedded in the imperative flow rather than leading it.

Combined:
5. **Typed-contract + inertia-first + deliberation-expanded** — Combines axes 1, 2, and 3. The
   C-41 structured claim is a typed schema block with field type annotations. DARK SIGNALS entries
   carry both the C-42 STATE_ENUM (declared at section header) and an Inertia Implication sub-field
   (axis 2). The C-43 weight table expands to 9 columns — including DARK SIGNALS Penalty and Inertia
   Cost — and a Selection Proof block traces the Net Score arithmetic. C-44 AMEND-A carries the
   full Net Score delta and Inertia Advocate migration burden. GATE is minimal; DELIBERATE is the
   deepest phase.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format — typed field annotations on C-41 contract; STATE_ENUM declaration at DARK SIGNALS header; typed C-43 columns; Net Score formula trace in C-44 | V-01 |
| Inertia framing — Inertia Advocate as named participant; Inertia Implication in DARK SIGNALS; Inertia Cost column in C-43 table; migration burden in C-44 | V-02 |
| Lifecycle emphasis — minimal GATE + SCAN; expanded DELIBERATE with Selection Proof block; C-44 reproduces delta by Selection Proof reference | V-03 |
| Phrasing register — conversational second-person imperatives; C-NN in parentheses after verbs; 4-state as "choose one:" list; Net Score as plain arithmetic | V-04 |
| Combination — typed contract (axis 1) + inertia-first (axis 2) + deliberation-expanded (axis 3) | V-05 |

---

## V-01 — Output Format: Typed Field Declarations

**Axis**: Output format — type annotations on the C-41 contract, STATE_ENUM declaration at DARK
SIGNALS header, typed C-43 column headers, Net Score arithmetic trace in AMEND-A.
**Hypothesis**: R11 V-01 declares the C-41 structured claim with named fields but no field types;
R11 V-02 presents the C-43 weight table with column names but no column type annotations. Both
criteria are satisfied by their presence. Field type annotations carry a structural advantage: a
typed contract declares what each field accepts before it is filled, making the schema a verifiable
definition independent of any particular scan output. The STATE_ENUM declaration at the DARK
SIGNALS header makes C-42 a named definition that each entry references, rather than a vocabulary
applied implicitly. Column type annotations on C-43 make each column's domain explicit. Net Score
arithmetic in C-44 makes the delta independently verifiable from the table. Hypothesis: 270/270.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and typed hypothesis
claim.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN self-label
in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate — all roles blocked until complete; C-31: GATE PHASE; C-25: self-labeled)`

Prerequisite for all other roles. Complete the pre-check AND produce the typed hypothesis claim
before any repo scanning, inventory, deliberation, or YAML work begins.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state vocabulary on every item)

[ ] C-12 -- "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — precedes all scanning, deliberation, and YAML.

[ ] C-13 -- C-12 draft-only statement precedes all output in this response.
    STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files, role file content, or role-creation instructions.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification regardless
    of composite score.

[ ] C-38+C-41 -- typed hypothesis claim (3-field contract with field type annotations):
    Fields: PREDICTED-MODE (enum) / STRUCTURAL-PREDICTION (string) / FALSIFICATION-SIGNAL (enum).
    Field types declared inline before values. Produced below this pre-check.
    STATUS: CONFIRMED — produced before SCAN PHASE / ROLE 2 is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN column headers; DARK SIGNALS section
    with C-42 STATE_ENUM declared at section header before entries.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27+C-43 -- pivot deliberation as weight-scoring table with typed column headers;
    DARK SIGNALS Penalty column [label:string, magnitude:0-4] satisfies C-37 structurally.
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS with STATE_ENUM; IS-FALSIFICATION-SIGNAL 4-state on
    each entry; Penalty column cites labels (C-37); AMEND-A cites label + verdict + Net delta.
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40+C-44 -- debt-framed amend options; AMEND-A carries typed Net Score
    arithmetic trace and hypothesis verdict; post-write cites 10 criteria (C-34 essential).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names all required outputs.
C-17: all SCHEDULED items name the delivering role.
C-18: C-NN IDs (including compound bundles) are primary keys throughout.
C-28: three-state vocabulary on every item.
C-29: compound bundles — "C-38+C-41", "C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43",
"C-36+C-37+C-39+C-42", "C-01+C-02+C-03+C-04", "C-16+C-30+C-40+C-44".
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 STATUS: ACKNOWLEDGED — essential failure named with consequence.

**Typed Hypothesis Claim** `(C-38+C-41 satisfier; C-25: self-labeled; produced before SCAN PHASE)`

```
TYPED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38: hypothesis declared before any repo scanning begins)
(C-41: 3-field typed contract — each field carries type annotation before value placeholder)
(C-25: section self-labeled)
(Downstream: C-42 STATE_ENUM declared at DARK SIGNALS header in ROLE 2;
 C-43 Penalty column carries FALSIFICATION-SIGNAL label as column value in ROLE 3;
 C-44 AMEND-A carries Net Score arithmetic trace in ROLE 4)

PREDICTED-MODE:        type: enum[directory | concept | service | domain]
                       value: [directory | concept | service | domain]

STRUCTURAL-PREDICTION: type: string(1 sentence — observable repo structure this mode predicts)
                       value: "[one sentence: e.g., 'packages are grouped by functional area
                               in workspace config with matching top-level directory clusters']"

FALSIFICATION-SIGNAL:  type: enum[NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE |
                                   NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
                       value: [the label that, if ABSENT in ROLE 2, overturns this claim]

CONFIDENCE:            type: enum[high | medium | low]
                       value: [high | medium | low]

BASIS:                 type: string(1 sentence — repo evidence grounding the prediction)
                       value: "[first-pass read of top-level names, manifest presence, or
                               domain vocabulary that grounds PREDICTED-MODE]"
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE PHASE / ROLE 1 pre-check and typed hypothesis claim complete. Produce Signal
Schema and DARK SIGNALS section. No pivot deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests (`docker-compose.yml`, `k8s/`, Helm charts). Workspace configs (npm workspaces,
Cargo workspace, `go.work`). Domain vocabulary (bounded context names, aggregate roots, domain
events in directory/module names).

Each DARK SIGNALS entry uses the C-42 STATE_ENUM declared at the section header. Apply the
enum definition — do not re-state it per entry.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: criterion purpose declared in header before schema rows are written
## C-25: section self-labeled; C-31: SCAN PHASE; C-33: pre-YAML bracket position

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if fewer detected signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only — no "TBD", "role_1", or generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row.
- Cap at 8 rows. Group weak signals under nearest strong signal; note grouping.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals and Hypothesis Relations
## C-36: structured negative evidence with per-entry mode impact
## C-39: Hypothesis Relation field on each entry
## C-42: IS-FALSIFICATION-SIGNAL typed field — STATE_ENUM declared below (applies to all entries)
## C-25: self-labeled; C-37 downstream: labels appear in ROLE 3 Penalty column

C-42 STATE_ENUM (apply to "Hypothesis Relation" field of every entry below):
  YES -- CONFIRMED            : this entry IS the GATE FALSIFICATION-SIGNAL; signal PRESENT/PARTIAL
  YES -- OVERTURNED           : this entry IS the GATE FALSIFICATION-SIGNAL; signal ABSENT
  NO -- corroborates-alternative([mode]) : NOT the FALSIFICATION-SIGNAL; absence supports [mode]
  NO -- neutral               : NOT the FALSIFICATION-SIGNAL; no bearing on stated hypothesis

NO-SERVICE-MANIFEST:
  Looked for:          docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM above]

NO-DDD-LANGUAGE:
  Looked for:          bounded context names, aggregate roots, domain events in dir/module names
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM above]

NO-DOMAIN-BOUNDARY:
  Looked for:          explicit subdomain directories, business capability groupings
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM above]

NO-WORKSPACE-GROUPING:
  Looked for:          monorepo workspace config grouping packages by area
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM above]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [GATE label]
  That entry's STATE_ENUM value:  [YES -- CONFIRMED | YES -- OVERTURNED]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27+C-43 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 Signal Schema and DARK SIGNALS complete. No YAML.

Open with hypothesis closure. Then produce the typed weight-scoring table. Column headers carry
type annotations — including "DARK SIGNALS Penalty [label:string, magnitude:0-4]" — satisfying
C-37 structurally. Close with the Net Score arithmetic trace.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: deliberation present
## C-43: weight-scoring table with DARK SIGNALS Penalty column [label:string, magnitude:0-4]
## C-37: DARK SIGNALS labels appear as column values in Penalty column for each mode

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  STATE_ENUM outcome:       [YES -- CONFIRMED | YES -- OVERTURNED]
  Consequence:              [proceed with predicted mode | deliberation may select different mode]

Evidence Weight Table:
(Column types:
  Mode: enum[directory|concept|service|domain]
  Evidence For: string(schema row "Repo signal" values, comma-separated)
  DARK SIGNALS Penalty [label:string, magnitude:0-4]: string(label + int 0-4)
  Base: int(1-5, from Evidence For count + signal-type strength)
  Penalty: int(0-4, equals magnitude from Penalty column)
  Net: int(Base minus Penalty)
  Verdict: enum[strong|possible|weak] where strong>=4, possible 2-3, weak 0-1)

| Mode      | Evidence For (schema rows)        | DARK SIGNALS Penalty [label: magnitude]  | Base | Penalty | Net | Verdict  |
|-----------|-----------------------------------|------------------------------------------|------|---------|-----|----------|
| directory | [Repo signal values from schema]  | NO-WORKSPACE-GROUPING: -[0|2|4]          | [N]  | [N]     | [N] | [s/p/w]  |
| concept   | [Repo signal values from schema]  | NO-DDD-LANGUAGE: -[0|2|4]                | [N]  | [N]     | [N] | [s/p/w]  |
| service   | [Repo signal values from schema]  | NO-SERVICE-MANIFEST: -[0|2|4]            | [N]  | [N]     | [N] | [s/p/w]  |
| domain    | [Repo signal values from schema]  | NO-DOMAIN-BOUNDARY: -[0|2|4]             | [N]  | [N]     | [N] | [s/p/w]  |

Magnitude guide: ABSENT = 4 (mode ruled out), PARTIAL = 2 (mode weakened), PRESENT = 0 (no deduction).

Net Score arithmetic trace:
  Winner:    [mode] — Base=[N] minus Penalty=[N] = Net=[N]
  Runner-up: [mode] — Base=[N] minus Penalty=[N] = Net=[N]
  Delta:     [winner Net] minus [runner-up Net] = [N]

Selected pivot mode: [mode with highest Net Score]
Rationale: Net Score delta=[N]; DARK SIGNALS [label] penalty -[N] eliminated [runner-up].
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. No new scanning or deliberation.

AMEND-A must: (a) cite the DARK SIGNALS label from the Penalty column (C-37 amend satisfier);
(b) carry hypothesis verdict — STATE_ENUM outcome from ROLE 2 (C-40 satisfier); (c) carry the
Net Score arithmetic trace from ROLE 3 as the quantified delta (C-44 satisfier).

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Net Score delta: [N] ([winner] Net=[N] vs [runner-up] Net=[N]).
> Hypothesis STATE_ENUM: [YES -- CONFIRMED | YES -- OVERTURNED] — FALSIFICATION-SIGNAL [label].
> C-05 ACKNOWLEDGED in GATE: no .roles/ content here."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N]
# hypothesis-outcome: [YES -- CONFIRMED | YES -- OVERTURNED]
# falsification-signal: [GATE label]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level: Advocates share status-quo context across this group.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [ROLE 2 "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: criterion IDs cited at point of satisfaction; C-30: 10 criteria cited;
 C-33: post-YAML bracket; C-34: essential-tier C-02 cited in this inventory)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"                    STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                        STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                       STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                              STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                                 STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level in YAML (C-24)                  STATUS: [CONFIRMED/FAIL]
[ ] C-43 weight table with typed DARK SIGNALS Penalty column in ROLE 3       STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                                STATUS: [CONFIRMED/FAIL]
[ ] C-42 STATE_ENUM declared; 4-state on all DARK SIGNALS entries (C-42)     STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + STATE_ENUM verdict + Net Score arithmetic trace (C-37+C-40+C-44) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this block = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-43, C-25, C-42, C-37+C-40+C-44 — 10 items.
C-34: essential-tier C-02 present alongside aspirational criteria.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37: cites label; C-40+C-44: verdict + delta)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):    [YES -- CONFIRMED — predicted mode supported |
                                 YES -- OVERTURNED — FALSIFICATION-SIGNAL [label] absent]
  Net Score arithmetic (C-44):  [selected mode] Net=[N] vs [runner-up] Net=[N]; delta=[N]
                                 (from ROLE 3 weight table — independently verifiable)
  DARK SIGNALS basis (C-37):    [label] Penalty=-[N]; [runner-up] Net=[N] < [selected] Net=[N]
  Debt if skipped:              corps-build, corps-pr, corps-committee, corps-rob inherit
                                misaligned clustering; Net Score arithmetic available but
                                hypothesis consequence ignored downstream.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: Exec-office name propagates verbatim into corps-rob governance artifacts
    and corps-committee appointment templates — no downstream correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocates in misaligned groups carry conflicting status-quo frames,
    degrading corps-committee review signal coherence across all review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R12 V-01). C-41: typed hypothesis claim — field type annotations on all
> three fields before value placeholders. C-42: STATE_ENUM declared at DARK SIGNALS header as a
> named definition; each entry applies enum by reference. C-43: weight table column headers carry
> type annotations including DARK SIGNALS Penalty [label:string, magnitude:0-4]. C-44: AMEND-A
> carries Net Score arithmetic trace reproduced from ROLE 3 table. All C-01 through C-44
> requirements met. Draft-only."

---

## V-02 — Inertia Framing: Inertia Advocate as Structural Participant

**Axis**: Inertia framing — Inertia Advocate introduced as a named participant in GATE and present
in every subsequent phase.
**Hypothesis**: In prior rounds, the Inertia Advocate (C-24) appears exclusively in the YAML as
a comment ("Inertia Advocate: auto-added by corps-build"). This satisfies C-24 but treats the
Inertia Advocate as a YAML artifact rather than a reasoning participant. Elevating the Inertia
Advocate to a named structural participant in all four phases produces richer C-24 coverage and
extends the C-43 weight table: an "Inertia Cost" column documents what the Inertia Advocate
stands to lose if each mode is selected (forcing misalignment between current structure and scan
pivot). C-44 AMEND-A translates the Net Score delta into an Inertia Advocate migration burden
statement — the concrete cost of switching modes after the Inertia Advocate has anchored on the
current structure. Hypothesis: 270/270.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and hypothesis claim.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN self-label
in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate — all roles blocked until complete; C-31: GATE PHASE; C-25: self-labeled)`

Prerequisite for all other roles. Complete the pre-check AND the structured hypothesis claim
before any scanning begins. The Inertia Advocate is introduced here as the primary consumer
of this scan's draft output.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED on every item)

[ ] C-12 -- "HARD BOUNDARY" block above is the first substantive line.
    STATUS: CONFIRMED.

[ ] C-13 -- C-12 precedes this pre-check.
    STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files, role file content, or role-creation instructions.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification regardless
    of composite score.

[ ] C-38+C-41 -- 3-field hypothesis claim (PREDICTED-MODE / STRUCTURAL-PREDICTION /
    FALSIFICATION-SIGNAL) produced in GATE, before SCAN. Inertia Advocate introduced as
    primary consumer in hypothesis block.
    STATUS: CONFIRMED — produced below.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN column headers; DARK SIGNALS section
    with C-42 4-state vocabulary; each entry carries Inertia Implication sub-field.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27+C-43 -- pivot deliberation as weight-scoring table with DARK SIGNALS Penalty
    column AND Inertia Cost column; C-37 satisfied by DARK SIGNALS labels in Penalty column.
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS with IS-FALSIFICATION-SIGNAL 4-state field +
    Inertia Implication; Penalty column cites labels; AMEND-A cites label + verdict + delta.
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml draft with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40+C-44 -- debt-framed amend options; AMEND-A carries Net Score delta and
    Inertia Advocate migration burden statement; post-write cites 10 criteria (C-34 essential).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names all required outputs.
C-17: all SCHEDULED items name the delivering role.
C-18: C-NN IDs as primary keys throughout.
C-28: three-state vocabulary on every item.
C-29: compound bundles — "C-38+C-41", "C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43",
"C-36+C-37+C-39+C-42", "C-01+C-02+C-03+C-04", "C-16+C-30+C-40+C-44".
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 ACKNOWLEDGED — essential failure named with consequence.

**Structured Hypothesis Claim** `(C-38+C-41 satisfier; C-25: self-labeled; produced before SCAN PHASE)`

```
STRUCTURED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38: hypothesis before scanning; C-41: 3-field contract; C-25: self-labeled)

Inertia Advocate context: This scan produces a draft org.yaml that the Inertia Advocate will
  use to defend the current repo structure. The Inertia Advocate's effectiveness depends on
  the pivot mode selected — a misaligned pivot forces the Advocate to defend boundaries the
  repo does not support. Name the mode that minimizes Inertia Advocate structural debt.

PREDICTED-MODE:        [directory | concept | service | domain]

STRUCTURAL-PREDICTION: [one sentence: observable repo structure this mode predicts —
                        the structure the Inertia Advocate would point to as "the way things
                        are organized now"]

FALSIFICATION-SIGNAL:  [DARK SIGNALS label — NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE |
                        NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING — that, if ABSENT,
                        overturns this prediction and indicates the Inertia Advocate is
                        defending a mode the repo does not support]

CONFIDENCE:            [high | medium | low]
BASIS:                 [one sentence: repo evidence grounding the prediction]
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE PHASE / ROLE 1 complete. Produce Signal Schema and DARK SIGNALS section.
No deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests (`docker-compose.yml`, `k8s/`, Helm charts). Workspace configs (npm workspaces,
Cargo workspace, `go.work`). Domain vocabulary (bounded context names, aggregate roots, domain
events in naming conventions).

Each DARK SIGNALS entry carries a C-42 Hypothesis Relation field (4-state vocabulary) AND an
Inertia Implication sub-field naming what the Inertia Advocate loses if this signal is ABSENT.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: criterion purpose declared in header; C-25: self-labeled; C-33: pre-YAML bracket

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if fewer signals.
- "YAML name (C-02)": exact string for YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row.
- Cap at 8 rows. Group weak signals under nearest strong.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals, Hypothesis Relations, and Inertia Implications
## C-36: structured negative evidence with per-entry mode impact
## C-39: Hypothesis Relation field on each entry
## C-42: IS-FALSIFICATION-SIGNAL typed field — 4-state vocabulary:
##   YES -- CONFIRMED / YES -- OVERTURNED / NO -- corroborates-alternative([mode]) / NO -- neutral
## C-25: self-labeled; C-37 downstream: labels appear in ROLE 3 Penalty column

NO-SERVICE-MANIFEST:
  Looked for:            docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis Relation:   [YES -- CONFIRMED | YES -- OVERTURNED |
                          NO -- corroborates-alternative([mode]) | NO -- neutral]
  Inertia Implication:   [what the Inertia Advocate loses if ABSENT — e.g., "Advocate cannot
                          defend service-boundary clustering; status-quo argument collapses"]

NO-DDD-LANGUAGE:
  Looked for:            bounded context names, aggregate roots, domain events in naming
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)
  Hypothesis Relation:   [YES -- CONFIRMED | YES -- OVERTURNED |
                          NO -- corroborates-alternative([mode]) | NO -- neutral]
  Inertia Implication:   [Inertia Advocate consequence of absence]

NO-DOMAIN-BOUNDARY:
  Looked for:            explicit subdomain directories, business capability groupings
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)
  Hypothesis Relation:   [YES -- CONFIRMED | YES -- OVERTURNED |
                          NO -- corroborates-alternative([mode]) | NO -- neutral]
  Inertia Implication:   [Inertia Advocate consequence of absence]

NO-WORKSPACE-GROUPING:
  Looked for:            monorepo workspace config grouping packages by area
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)
  Hypothesis Relation:   [YES -- CONFIRMED | YES -- OVERTURNED |
                          NO -- corroborates-alternative([mode]) | NO -- neutral]
  Inertia Implication:   [Inertia Advocate consequence of absence]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [label]
  That entry's Hypothesis Relation: [YES -- CONFIRMED | YES -- OVERTURNED]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27+C-43 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 complete. No YAML.

Open with hypothesis closure. Produce the weight-scoring table. The DARK SIGNALS Penalty column
satisfies C-37 structurally. Add an Inertia Cost column: for each mode, name the Inertia Advocate
structural consequence of selecting that mode (what status-quo defense the Advocate would need
to abandon or reconstruct).

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: deliberation present
## C-43: weight-scoring table with DARK SIGNALS Penalty column (C-37 satisfier)
## Inertia Cost column: Inertia Advocate structural consequence per mode (C-24 extension)

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  Hypothesis Relation:      [YES -- CONFIRMED | YES -- OVERTURNED]
  Inertia Advocate impact:  [consequence for Advocate if hypothesis is overturned]

Evidence Weight Table:
(Scoring: Base 1-5 from Evidence For count + signal strength; Penalty = DARK SIGNALS magnitude
 for that mode — ABSENT=-4, PARTIAL=-2, PRESENT=0; Net = Base - Penalty;
 strong: Net>=4, possible: 2-3, weak: 0-1)

| Mode      | Evidence For (schema rows)        | DARK SIGNALS Penalty               | Inertia Cost                        | Base | Penalty | Net | Verdict  |
|-----------|-----------------------------------|------------------------------------|-------------------------------------|------|---------|-----|----------|
| directory | [Repo signal values from schema]  | NO-WORKSPACE-GROUPING: -[0|2|4]    | [Advocate defense cost if selected] | [N]  | [N]     | [N] | [s/p/w]  |
| concept   | [Repo signal values from schema]  | NO-DDD-LANGUAGE: -[0|2|4]          | [Advocate defense cost if selected] | [N]  | [N]     | [N] | [s/p/w]  |
| service   | [Repo signal values from schema]  | NO-SERVICE-MANIFEST: -[0|2|4]      | [Advocate defense cost if selected] | [N]  | [N]     | [N] | [s/p/w]  |
| domain    | [Repo signal values from schema]  | NO-DOMAIN-BOUNDARY: -[0|2|4]       | [Advocate defense cost if selected] | [N]  | [N]     | [N] | [s/p/w]  |

Selected pivot mode: [mode with highest Net Score]
Net Score delta: [winner Net] - [runner-up Net] = [N]
Rationale: DARK SIGNALS [label] penalty -[N] eliminated [runner-up]; Inertia Cost for [winner]
  is [low/moderate/high] because [one sentence].
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. AMEND-A must: (a) cite the DARK SIGNALS label (C-37);
(b) carry hypothesis verdict (C-40); (c) carry Net Score delta AND Inertia Advocate migration
burden (C-44).

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Net Score delta: [N]. Hypothesis [YES -- CONFIRMED | YES -- OVERTURNED] —
> FALSIFICATION-SIGNAL [label]. Inertia Advocate context: [one sentence on Advocate alignment
> with selected mode]. C-05 ACKNOWLEDGED in GATE: no .roles/ content here."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N]
# hypothesis-outcome: [YES -- CONFIRMED | YES -- OVERTURNED]
# inertia-advocate-alignment: [aligned | misaligned] — [one phrase]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # Inertia Advocate: exec-office Advocate anchors on current leadership structure.
    # Confirm name before running corps-build.

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level Advocates share status-quo context — confirm group boundaries match
      #   current team reporting lines before corps-build runs.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [ROLE 2 "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: C-NN IDs at satisfaction point; C-30: 10 criteria; C-33: post-YAML bracket; C-34: C-02 essential)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"                       STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                           STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present with Inertia Advocate note (C-07+C-24)          STATUS: [CONFIRMED/FAIL]
[ ] At least one group container with Inertia Advocate governance note (C-03)   STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                                    STATUS: [CONFIRMED/FAIL]
[ ] C-43 weight table with DARK SIGNALS Penalty + Inertia Cost columns (C-43)   STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                                   STATUS: [CONFIRMED/FAIL]
[ ] C-42 4-state IS-FALSIFICATION-SIGNAL on all DARK SIGNALS entries (C-42)     STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS Inertia Implication on all entries (C-24 extension)            STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + verdict + Net delta + Inertia migration burden (C-37+C-40+C-44) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) + this block (post-YAML) — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this block = post-YAML bracket.
C-30: C-02, C-04, C-07+C-24, C-03, C-05, C-43, C-25, C-42, C-24 extension, C-37+C-40+C-44 — 10 items.
C-34: essential-tier C-02 present alongside aspirational criteria.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37+C-40+C-44: label + verdict + delta)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):       [YES -- CONFIRMED — predicted mode supported |
                                    YES -- OVERTURNED — FALSIFICATION-SIGNAL [label] absent]
  Net Score delta (C-44):          [selected mode] Net=[N] vs [runner-up] Net=[N]; delta=[N]
  DARK SIGNALS basis (C-37):       [label] Penalty=-[N] eliminated [runner-up mode]
  Inertia migration burden (C-44): Switching to [alternative mode] requires Inertia Advocate
                                   to reconstruct [current structure type] defense as
                                   [alternative structure type] — [low|moderate|high] cost.
  Debt if skipped:                 corps-build inherits misaligned pivot; Inertia Advocate
                                   anchors on wrong structure across all downstream stages.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: Exec-office Inertia Advocate anchors on "[name]" — propagates into
    corps-rob governance and corps-committee templates verbatim.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Debt if skipped: Group-level Inertia Advocates anchor on current grouping; misalignment
    degrades corps-committee review signal coherence across all review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R12 V-02). C-41: 3-field hypothesis claim with Inertia Advocate context
> in GATE. C-42: IS-FALSIFICATION-SIGNAL 4-state on all DARK SIGNALS entries plus Inertia
> Implication sub-field. C-43: weight table with DARK SIGNALS Penalty + Inertia Cost columns.
> C-44: AMEND-A carries Net Score delta and Inertia Advocate migration burden. C-24: Advocate
> present at exec-office, group, team levels and in DARK SIGNALS and deliberation. Draft-only."

---

## V-03 — Lifecycle Emphasis: Scan-Compressed, Deliberation-Expanded

**Axis**: Lifecycle emphasis — GATE and SCAN phases are minimal (pre-check + schema only, no
explanatory prose); DELIBERATE phase carries maximum depth through an expanded 8-column weight
table and a standalone Selection Proof block.
**Hypothesis**: Prior rounds distribute depth roughly equally across phases. The selection logic —
where C-43 and C-44 are satisfied — lives in DELIBERATE PHASE. Concentrating depth there forces
complete criterion coverage at the point where it matters most for auditability. The Selection
Proof block below the table traces the Net Score arithmetic for winner and runner-up explicitly,
making C-44's delta independently verifiable without reading AMEND-A. GATE is reduced to its
minimum viable form; SCAN is a clean schema + DARK SIGNALS block. Hypothesis: 270/270.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and hypothesis claim.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN self-label
in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25; C-18: C-NN IDs as primary keys; C-32: three-state on every item)

[ ] C-12 -- HARD BOUNDARY front-loaded.              STATUS: CONFIRMED.
[ ] C-13 -- C-12 precedes this pre-check.            STATUS: CONFIRMED.
[ ] C-05 -- no .roles/ files.                  STATUS: ACKNOWLEDGED — essential failure;
                                                       golden disqualification if violated.
[ ] C-38+C-41 -- 3-field hypothesis claim below.     STATUS: CONFIRMED.
[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema.      STATUS: SCHEDULED — ROLE 2.
[ ] C-23+C-27+C-43 -- weight table + Selection Proof. STATUS: SCHEDULED — ROLE 3.
[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS + 4-state.  STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.
[ ] C-01+C-02+C-03+C-04 -- org.yaml draft.           STATUS: SCHEDULED — ROLE 4.
[ ] C-16+C-30+C-40+C-44 -- amend options + delta.    STATUS: SCHEDULED — ROLE 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35: all satisfied — compound bundles: "C-38+C-41",
"C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43", "C-36+C-37+C-39+C-42", "C-01+C-02+C-03+C-04",
"C-16+C-30+C-40+C-44". C-05 ACKNOWLEDGED with consequence.

**Structured Hypothesis Claim** `(C-38+C-41; C-25: self-labeled)`

```
STRUCTURED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1  (C-38+C-41; C-25)

PREDICTED-MODE:        [directory | concept | service | domain]
STRUCTURAL-PREDICTION: [one sentence — observable repo structure this mode predicts]
FALSIFICATION-SIGNAL:  [NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE |
                        NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
CONFIDENCE:            [high | medium | low]
BASIS:                 [one sentence: repo evidence]
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: ROLE 1 complete. Produce Signal Schema and DARK SIGNALS. No deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11+C-21 satisfier; C-22: criterion purpose in header; C-25: self-labeled; C-33: pre-YAML

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Min 2 rows. PLACEHOLDER if fewer. YAML name exact. Named roles only. Evidence per row. Cap 8.
Exec office inference: [term, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}}  (C-36+C-39+C-42; C-25; C-37 downstream: labels in ROLE 3 Penalty column)
## C-42 vocabulary: YES -- CONFIRMED / YES -- OVERTURNED / NO -- corroborates-alternative([mode]) / NO -- neutral

NO-SERVICE-MANIFEST:
  Looked for: docker-compose.yml, k8s/, Helm charts  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Modes affected: rules out / weakens service mode
  Hypothesis Relation: [C-42 4-state]

NO-DDD-LANGUAGE:
  Looked for: bounded contexts, aggregate roots, domain events  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Modes affected: rules out / weakens concept mode
  Hypothesis Relation: [C-42 4-state]

NO-DOMAIN-BOUNDARY:
  Looked for: subdomain directories, business capability groupings  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Modes affected: rules out / weakens domain mode
  Hypothesis Relation: [C-42 4-state]

NO-WORKSPACE-GROUPING:
  Looked for: workspace config grouping packages by area  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Modes affected: rules out / weakens directory mode
  Hypothesis Relation: [C-42 4-state]

Hypothesis outcome: FALSIFICATION-SIGNAL [label] — [YES -- CONFIRMED | YES -- OVERTURNED]
Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27+C-43 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: ROLE 2 complete. No YAML.

This phase carries maximum depth. The weight table expands to 8 columns. A Selection Proof block
below the table traces the Net Score arithmetic for winner and runner-up in full — making the
C-44 delta independently verifiable before AMEND-A repeats it. Cite schema rows by "Repo signal"
value. Cite DARK SIGNALS labels in the Penalty column.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: precedes YAML; C-27: deliberation present
## C-43: weight-scoring table with DARK SIGNALS Penalty column — C-37 satisfied by label appearance
## Selection Proof: Net Score arithmetic for winner and runner-up — C-44 source

Hypothesis closure:
  GATE hypothesis:          [mode]
  FALSIFICATION-SIGNAL:     [label]
  C-42 outcome:             [YES -- CONFIRMED | YES -- OVERTURNED]
  Mode consequence:         [proceed with hypothesis mode | deliberation may select different mode]

Evidence Weight Table (8 columns):
(Scoring guide:
  Signal Strength: +1 to +3 per Evidence For schema row by signal-type strength
  Base: sum of Signal Strength values for all Evidence For rows (cap 5)
  DARK SIGNALS Penalty: ABSENT=4, PARTIAL=2, PRESENT=0 for the mode's primary negative signal
  Net = Base - Penalty
  Verdict: strong Net>=4 / possible Net 2-3 / weak Net 0-1)

| Mode      | Evidence For (schema rows + signal-type) | Signal Strength | DARK SIGNALS Penalty           | Base | Penalty | Net | Verdict  |
|-----------|------------------------------------------|-----------------|--------------------------------|------|---------|-----|----------|
| directory | [rows, signal-types]                     | [+N per row]    | NO-WORKSPACE-GROUPING: -[0|2|4]| [N]  | [N]     | [N] | [s/p/w]  |
| concept   | [rows, signal-types]                     | [+N per row]    | NO-DDD-LANGUAGE: -[0|2|4]      | [N]  | [N]     | [N] | [s/p/w]  |
| service   | [rows, signal-types]                     | [+N per row]    | NO-SERVICE-MANIFEST: -[0|2|4]  | [N]  | [N]     | [N] | [s/p/w]  |
| domain    | [rows, signal-types]                     | [+N per row]    | NO-DOMAIN-BOUNDARY: -[0|2|4]   | [N]  | [N]     | [N] | [s/p/w]  |

Selection Proof (C-44 source — Net Score arithmetic for winner and runner-up):
  Winner:
    Mode:             [mode]
    Evidence For:     [schema row values] — Signal Strength: [+N, +N, ...]
    Base:             [sum] = [N]
    DARK SIGNALS:     [label] [ABSENT|PARTIAL|PRESENT] — Penalty: -[N]
    Net:              [N] - [N] = [N]
    Verdict:          [strong|possible|weak]

  Runner-up:
    Mode:             [mode]
    Evidence For:     [schema row values] — Signal Strength: [+N, ...]
    Base:             [sum] = [N]
    DARK SIGNALS:     [label] [ABSENT|PARTIAL|PRESENT] — Penalty: -[N]
    Net:              [N] - [N] = [N]
    Verdict:          [strong|possible|weak]

  Delta:              [winner Net] - [runner-up Net] = [N]
  DARK SIGNALS eliminator: [label] Penalty=-[N] reduced [runner-up] from competitive to [verdict]

Selected pivot mode: [winner from Selection Proof]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. AMEND-A cites the DARK SIGNALS label (C-37), carries the
C-42 hypothesis verdict (C-40), and reproduces the Selection Proof delta by reference (C-44).

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Selection Proof delta: [N] ([winner] Net=[N] vs [runner-up] Net=[N]).
> C-42 outcome: [YES -- CONFIRMED | YES -- OVERTURNED] — FALSIFICATION-SIGNAL [label].
> C-05 ACKNOWLEDGED: no .roles/ content here."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N] (Selection Proof delta vs runner-up: [N])
# hypothesis-outcome: [YES -- CONFIRMED | YES -- OVERTURNED]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [ROLE 2 "Repo signal" value]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same pattern.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: C-NN at satisfaction point; C-30: 10 criteria; C-33: post-YAML bracket; C-34: C-02 essential)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"                STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                   STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                  STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                         STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                            STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                     STATUS: [CONFIRMED/FAIL]
[ ] C-43 table with DARK SIGNALS Penalty column (C-43)                  STATUS: [CONFIRMED/FAIL]
[ ] Selection Proof block present with winner/runner-up arithmetic (C-43) STATUS: [CONFIRMED/FAIL]
[ ] C-42 4-state IS-FALSIFICATION-SIGNAL on all DARK SIGNALS entries    STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + verdict + Selection Proof delta reference (C-37+C-40+C-44) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this block = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-43, C-43 proof, C-42, C-37+C-40+C-44 — 10 items.
C-34: essential-tier C-02 present.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37+C-40+C-44: label + verdict + delta)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):   [YES -- CONFIRMED — hypothesis holds |
                                YES -- OVERTURNED — FALSIFICATION-SIGNAL [label] absent]
  Selection Proof delta (C-44): Delta=[N]: [winner] Net=[N] vs [runner-up] Net=[N]
                                 (see ROLE 3 Selection Proof — independently verifiable)
  DARK SIGNALS basis (C-37):   [label] Penalty=-[N] reduced [runner-up] below winner threshold
  Debt if skipped:             corps-build, corps-pr, corps-committee, corps-rob inherit
                               misaligned pivot; Selection Proof delta documented but not acted on.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: Name propagates into corps-rob governance and corps-committee templates.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocates in misaligned groups degrade corps-committee coherence.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R12 V-03). C-41: compact 3-field claim in minimal GATE. C-42: 4-state
> IS-FALSIFICATION-SIGNAL on all DARK SIGNALS entries. C-43: expanded 8-column weight table with
> Signal Strength sub-scoring. Selection Proof block traces full Net Score arithmetic for winner
> and runner-up — C-44 source. AMEND-A reproduces delta by Selection Proof reference. All C-01
> through C-44 requirements met. Draft-only."

---

## V-04 — Phrasing Register: Conversational Imperative

**Axis**: Phrasing register — direct second-person imperatives, short declarative sentences, plain
arithmetic notation, criterion labels in parentheses after key verbs rather than in elaborate
section headers.
**Hypothesis**: All prior rounds use formal technical register: elaborate section headers with C-NN
annotation bundles, multi-sentence role descriptions, vocabulary declared in block headers. The
same criterion coverage can be achieved in a conversational imperative register. Criteria that
require specific vocabulary (CONFIRMED / SCHEDULED / ACKNOWLEDGED, C-NN compound bundles, phase
labels) are preserved but embedded in the imperative flow. The 4-state C-42 vocabulary becomes a
"choose one:" numbered list. The Net Score formula is written as plain arithmetic. This tests
whether register transformation preserves criterion coverage or whether certain criteria are
structurally dependent on formal presentation. Hypothesis: 270/270.

---

You are running `corps-scan`. Work through four steps in order. Do not start a later step until
the earlier step is done.

Step 2, Step 3, and Step 4 are locked. Do not begin them until Step 1 is finished.

First line of this response: **HARD BOUNDARY (C-12)** — this output is a draft org.yaml for
human review. No `.roles/` files will be written here.

---

### STEP 1 — GATE: Make Your Pre-Check and Claim
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

Do Step 1 before anything else. First: fill in the pre-check. Then: make the hypothesis claim.

```
PRE-CHECK — corps-scan — STEP 1 / GATE PHASE  (C-25: self-labeled; C-18: C-NN IDs as keys)
(Three states: CONFIRMED = done now / SCHEDULED = done in a later step / ACKNOWLEDGED = noted)

[ ] C-12 -- HARD BOUNDARY is the first line.                STATUS: CONFIRMED.
[ ] C-13 -- C-12 came before this pre-check.                STATUS: CONFIRMED.
[ ] C-05 -- you will not write .roles/ files here.    STATUS: ACKNOWLEDGED — if you do,
                                                              the output fails golden threshold
                                                              regardless of everything else.
[ ] C-38+C-41 -- make the hypothesis claim below.           STATUS: CONFIRMED.
[ ] C-11+C-21+C-22+C-25+C-26 -- schema in Step 2.          STATUS: SCHEDULED — Step 2.
[ ] C-23+C-27+C-43 -- weight table (C-43) in Step 3.        STATUS: SCHEDULED — Step 3.
[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS in Step 2;          STATUS: SCHEDULED — Step 2 + 3 + 4.
    4-state entries (C-42); labels in table (C-37).
[ ] C-01+C-02+C-03+C-04 -- org.yaml in Step 4.              STATUS: SCHEDULED — Step 4.
[ ] C-16+C-30+C-40+C-44 -- amend options with Net delta.     STATUS: SCHEDULED — Step 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 satisfied. Compound bundles: "C-38+C-41",
"C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43", "C-36+C-37+C-39+C-42", "C-01+C-02+C-03+C-04",
"C-16+C-30+C-40+C-44". C-05 ACKNOWLEDGED with consequence.

**Make this claim (C-38+C-41):** `(C-25: self-labeled)`

```
HYPOTHESIS CLAIM — STEP 1 / GATE PHASE  (C-38+C-41: 3-field claim before any scanning; C-25)

Which pivot mode do you predict? (choose one)
  PREDICTED-MODE: [directory | concept | service | domain]

What repo structure does that mode predict? (one sentence)
  STRUCTURAL-PREDICTION: [e.g., "packages clustered by area in workspace config"]

Which DARK SIGNAL, if missing, would overturn your prediction? (choose one)
  FALSIFICATION-SIGNAL: [NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE |
                          NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]

How confident are you? (choose one)
  CONFIDENCE: [high | medium | low]

What repo evidence grounds this? (one sentence)
  BASIS: [top-level names / manifest presence / domain vocabulary]
```

Step 1 done. Start Step 2.

---

### STEP 2 — SCAN: Walk the Repo and Record What You Find
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Step 1 must be done first. Walk the repo. Write a schema row for every signal you find.
Then document what you did NOT find. No deliberating yet. No YAML yet.

Walk here: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`.
Check: service manifests, workspace configs, domain vocabulary in directory names.

**Fill in the Signal Schema (C-26, C-22, C-25):**

```
SIGNAL SCHEMA — STEP 2 / SCAN PHASE
(C-26: C-11+C-21 satisfier — pre-YAML inventory with C-NN column headers; C-22: purpose in header;
 C-25: self-labeled; C-33: pre-YAML bracket)

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

At least 2 rows. Exact YAML key in column 3. Named roles only in column 4. One-sentence evidence.
Cap at 8 rows. Group weak signals under nearest strong.
Exec office: [any term suggesting exec title, or "no signal — placeholder"]
```

**Now record what you did NOT find (C-36, C-39, C-42, C-25):**

For the Hypothesis Relation field on each entry, pick one state from this list (C-42):
  1. YES -- CONFIRMED            (this IS the GATE FALSIFICATION-SIGNAL and it is present)
  2. YES -- OVERTURNED           (this IS the GATE FALSIFICATION-SIGNAL and it is absent)
  3. NO -- corroborates-alternative([mode])   (not the FALSIFICATION-SIGNAL; absence supports [mode])
  4. NO -- neutral               (not the FALSIFICATION-SIGNAL; irrelevant to the hypothesis)

```
DARK SIGNALS — STEP 2 / SCAN PHASE
(C-36: negative evidence with mode impact; C-39: hypothesis relation; C-42: 4-state vocabulary above;
 C-25: self-labeled; C-37 downstream: labels go in Step 3 table Penalty column)

NO-SERVICE-MANIFEST:
  Looked for: docker-compose.yml, k8s/, Helm charts  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Mode impact: absent = rules out service mode; partial = weakens it
  Hypothesis Relation: [pick from 1-4 above]

NO-DDD-LANGUAGE:
  Looked for: bounded context names, aggregate roots, domain events  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Mode impact: absent = rules out concept mode; partial = weakens it
  Hypothesis Relation: [pick from 1-4 above]

NO-DOMAIN-BOUNDARY:
  Looked for: subdomain directories, business capability groupings  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Mode impact: absent = rules out domain mode; partial = weakens it
  Hypothesis Relation: [pick from 1-4 above]

NO-WORKSPACE-GROUPING:
  Looked for: workspace config grouping by area  |  Detected: [PRESENT|ABSENT|PARTIAL]
  Mode impact: absent = rules out directory mode; partial = weakens it
  Hypothesis Relation: [pick from 1-4 above]

Hypothesis check: FALSIFICATION-SIGNAL [label] from Step 1 — was it present or absent?
  Result: [YES -- CONFIRMED | YES -- OVERTURNED]
  Modes ruled out: [list | none]
```

Step 2 done. Start Step 3.

---

### STEP 3 — DELIBERATE: Score Each Mode and Pick the Winner
`(C-25: self-labeled; C-23+C-27+C-43 satisfier; C-31: DELIBERATE PHASE)`

Step 2 must be done first. No YAML yet.

Score each mode. Net = Evidence For minus Penalty. The mode with the highest Net wins.
DARK SIGNALS labels go in the Penalty column — this is required (C-37).

```
PIVOT MODE DELIBERATION — STEP 3 / DELIBERATE PHASE
(C-43: weight-scoring table with DARK SIGNALS Penalty column; C-25: self-labeled;
 C-23: deliberation before YAML; C-27: tri-part deliberation satisfied by this table;
 C-37: DARK SIGNALS labels appear as Penalty column values)

Hypothesis check result (from Step 2):
  GATE hypothesis: [mode]
  FALSIFICATION-SIGNAL: [label] — [YES -- CONFIRMED | YES -- OVERTURNED]
  What it means: [hypothesis holds, proceed | may need different mode]

Score each mode (C-43):
  Evidence For score: count schema rows supporting this mode, weight by signal-type strength (1-3 each), cap 5.
  Penalty: look up the DARK SIGNALS label for each mode — ABSENT=4, PARTIAL=2, PRESENT=0.
  Net = Evidence For minus Penalty.

| Mode      | Evidence For (schema rows)        | DARK SIGNALS Penalty               | Base | Penalty | Net | Verdict  |
|-----------|-----------------------------------|------------------------------------|------|---------|-----|----------|
| directory | [Repo signal values]              | NO-WORKSPACE-GROUPING: -[0|2|4]    | [N]  | [N]     | [N] | [s/p/w]  |
| concept   | [Repo signal values]              | NO-DDD-LANGUAGE: -[0|2|4]          | [N]  | [N]     | [N] | [s/p/w]  |
| service   | [Repo signal values]              | NO-SERVICE-MANIFEST: -[0|2|4]      | [N]  | [N]     | [N] | [s/p/w]  |
| domain    | [Repo signal values]              | NO-DOMAIN-BOUNDARY: -[0|2|4]       | [N]  | [N]     | [N] | [s/p/w]  |

Net Score: strong if Net>=4 / possible if Net 2-3 / weak if Net 0-1.

Winner: [mode with highest Net] — Net=[N]
Runner-up: [mode] — Net=[N]
Net Score delta: [winner Net] minus [runner-up Net] = [N]
What eliminated the runner-up: DARK SIGNALS [label] Penalty=-[N]
```

Step 3 done. Start Step 4.

---

### STEP 4 — DRAFT + FINALIZE: Write the YAML and Offer Amends
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

All prior steps must be done first.

Before writing YAML, say where the team names come from:
> "Team names from Step 2 schema 'YAML name' column. Pivot: [Step 3 winner]. Net=[N], delta=[N].
> Hypothesis [YES -- CONFIRMED | YES -- OVERTURNED] — [label]. C-05: no .roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Step 3 winner] — Net=[N], delta vs runner-up=[N]
# hypothesis: [YES -- CONFIRMED | YES -- OVERTURNED] — [label]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From Step 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm before corps-build

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24): each team here gets one Inertia Advocate
      # from corps-build. Group-level Advocates share status-quo context.
      teams:
        - name: "[exact YAML key from Step 2 schema]"
          # schema-signal: [Step 2 repo signal value]
          roles:
            - [Named role from Step 2 schema]
            - [Named role from Step 2 schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if needed]"
      type: [...]
      # Inertia Advocate governance (C-24): same pattern.
      teams: [...]
```

**Check your work (C-14, C-30, C-33):** `(C-25: self-labeled)`

```
POST-WRITE CHECK — STEP 4 / DRAFT+FINALIZE PHASE  (C-19; C-30: 10 items; C-33: post-YAML; C-34: C-02)

[ ] Team names match Step 2 schema "YAML name" column (C-02)         STATUS: [CONFIRMED/FAIL]
[ ] Teams each have 2+ named roles, no generics (C-04)               STATUS: [CONFIRMED/FAIL]
[ ] exec-office section is there (C-07)                              STATUS: [CONFIRMED/FAIL]
[ ] At least one group container (C-03)                              STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content (C-05)                                  STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                  STATUS: [CONFIRMED/FAIL]
[ ] Weight table with DARK SIGNALS Penalty column in Step 3 (C-43)  STATUS: [CONFIRMED/FAIL]
[ ] All sections have a C-NN self-label (C-25)                       STATUS: [CONFIRMED/FAIL]
[ ] 4-state vocabulary on all DARK SIGNALS entries (C-42)            STATUS: [CONFIRMED/FAIL]
[ ] Amend A has label + verdict + Net delta (C-37+C-40+C-44)         STATUS: [CONFIRMED/FAIL]
```

**Three ways to adjust this draft (C-08, C-16, C-25):** `(C-25: self-labeled)`

```
AMEND OPTIONS — STEP 4 / DRAFT+FINALIZE PHASE  (C-08+C-16+C-25)

Amend A: Switch the pivot mode.
  What the scoring said (C-40+C-44): hypothesis was [YES -- CONFIRMED | YES -- OVERTURNED];
    [GATE label] scored Net=[N]; winner Net=[N] vs runner-up Net=[N]; delta=[N].
  DARK SIGNALS basis (C-37): [label] Penalty=-[N] knocked [runner-up] out.
  Why it matters: corps-build, corps-pr, corps-committee, corps-rob all inherit this pivot.
    Wrong mode = misaligned clustering through the whole pipeline.
  How to do it: /corps-scan --pivot [mode]

Amend B: Rename the exec office.
  Right now it is: "[name]" (from Step 2, or placeholder)
  Why it matters: the name goes verbatim into corps-rob governance and corps-committee templates.
  How to do it: /corps-scan --exec-office "[new name]"

Amend C: Change the group structure.
  Right now: [n] groups, organized by [pivot + schema clustering].
  Why it matters: misaligned groups give Inertia Advocates conflicting status-quo frames,
    which degrades corps-committee review signal quality across all review cycles.
  How to do it: /corps-scan --groups "[description]"
```

> "corps-scan done (R12 V-04). C-41: 3-field claim as a 'fill in' block with question prompts.
> C-42: 4-state vocabulary as a numbered 'choose one' list before DARK SIGNALS entries.
> C-43: weight table with plain-English Net = Evidence For minus Penalty arithmetic.
> C-44: Amend A states delta as a comparison sentence. All C-01 through C-44 satisfied.
> Draft-only."

---

## V-05 — Combination: Typed-Contract + Inertia-First + Deliberation-Expanded

**Axis**: Combination of axes 1 (typed field declarations), 2 (inertia-first framing), and 3
(scan-compressed, deliberation-expanded).
**Hypothesis**: V-01 introduces typed contracts for C-41/C-42/C-43. V-02 elevates the Inertia
Advocate to a named participant in every phase and adds Inertia columns to the deliberation table.
V-03 compresses GATE/SCAN and expands DELIBERATE with a Selection Proof block. Combining all
three produces the densest criterion coverage per section: the typed C-41 contract and STATE_ENUM
declaration from V-01; the Inertia Implication sub-field in DARK SIGNALS and the Inertia Cost
column in the weight table from V-02; and the 8-column table with Selection Proof block from V-03.
AMEND-A carries the Selection Proof delta, the Inertia Advocate migration burden, and the
hypothesis verdict simultaneously. Hypothesis: 270/270.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and typed hypothesis
claim.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN self-label
in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25; C-18: C-NN IDs as primary keys; C-32: three-state on every item)

[ ] C-12 -- HARD BOUNDARY front-loaded.               STATUS: CONFIRMED.
[ ] C-13 -- C-12 precedes this pre-check.             STATUS: CONFIRMED.
[ ] C-05 -- no .roles/ files.                   STATUS: ACKNOWLEDGED — essential failure;
                                                        golden disqualification if violated.
[ ] C-38+C-41 -- typed 3-field hypothesis claim.      STATUS: CONFIRMED — produced below.
[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema.       STATUS: SCHEDULED — ROLE 2.
    DARK SIGNALS with C-42 STATE_ENUM + Inertia Implication sub-field.
[ ] C-23+C-27+C-43 -- 9-column weight table with      STATUS: SCHEDULED — ROLE 3.
    DARK SIGNALS Penalty + Inertia Cost + Selection Proof block.
[ ] C-36+C-37+C-39+C-42 -- 4-state + Inertia         STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.
    Implication; labels in Penalty column; AMEND-A carries delta + burden.
[ ] C-01+C-02+C-03+C-04 -- org.yaml draft.            STATUS: SCHEDULED — ROLE 4.
[ ] C-16+C-30+C-40+C-44 -- amend options; AMEND-A     STATUS: SCHEDULED — ROLE 4.
    carries Selection Proof delta + Inertia migration burden.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 satisfied. Compound bundles: "C-38+C-41",
"C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43", "C-36+C-37+C-39+C-42",
"C-01+C-02+C-03+C-04", "C-16+C-30+C-40+C-44". C-05 ACKNOWLEDGED with consequence.

**Typed Hypothesis Claim** `(C-38+C-41; C-25: self-labeled; produced before SCAN PHASE)`

```
TYPED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38+C-41: typed 3-field contract; C-25: self-labeled)
(Inertia Advocate context: this scan's draft is the foundation the Inertia Advocate defends.
 FALSIFICATION-SIGNAL absence means the Advocate is defending a mode the repo does not support.)
(Downstream: C-42 STATE_ENUM at DARK SIGNALS header in ROLE 2; Inertia Implication in each entry;
 C-43 Penalty + Inertia Cost columns in ROLE 3; C-44 delta + burden in AMEND-A ROLE 4)

PREDICTED-MODE:        type: enum[directory | concept | service | domain]
                       value: [directory | concept | service | domain]

STRUCTURAL-PREDICTION: type: string(1 sentence — observable repo structure this mode predicts,
                                    framed as what the Inertia Advocate will point to as
                                    "the way the repo is organized now")
                       value: "[prediction sentence]"

FALSIFICATION-SIGNAL:  type: enum[NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE |
                                   NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
                       value: [label — its ABSENCE overturns the claim and indicates the
                               Inertia Advocate is defending a mode the repo does not support]

CONFIDENCE:            type: enum[high | medium | low]
                       value: [high | medium | low]

BASIS:                 type: string(1 sentence — repo evidence)
                       value: "[evidence sentence]"
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: ROLE 1 complete. Produce Signal Schema and DARK SIGNALS. No deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11+C-21 satisfier; C-22: criterion purpose in header; C-25: self-labeled; C-33: pre-YAML

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Min 2 rows. Exact YAML key. Named roles only. One-sentence evidence per row. Cap 8.
Exec office inference: [term, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals, Typed Hypothesis Relations, and Inertia Implications
## C-36: structured negative evidence with mode impact; C-39: hypothesis relation per entry
## C-42: IS-FALSIFICATION-SIGNAL typed field — STATE_ENUM declared below (applies to all entries)
## C-25: self-labeled; C-37 downstream: labels in ROLE 3 Penalty column

C-42 STATE_ENUM (apply to "Hypothesis Relation" field on every entry below):
  YES -- CONFIRMED            : this IS the GATE FALSIFICATION-SIGNAL; signal PRESENT/PARTIAL
  YES -- OVERTURNED           : this IS the GATE FALSIFICATION-SIGNAL; signal ABSENT
  NO -- corroborates-alternative([mode]) : NOT the FALSIFICATION-SIGNAL; absence supports [mode]
  NO -- neutral               : NOT the FALSIFICATION-SIGNAL; no bearing on hypothesis

NO-SERVICE-MANIFEST:
  Looked for:            docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis Relation:   [apply C-42 STATE_ENUM above]
  Inertia Implication:   [what Inertia Advocate loses if ABSENT — e.g., "Advocate cannot defend
                          service boundaries; status-quo claim collapses without manifest evidence"]

NO-DDD-LANGUAGE:
  Looked for:            bounded context names, aggregate roots, domain events in naming
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)
  Hypothesis Relation:   [apply C-42 STATE_ENUM above]
  Inertia Implication:   [Inertia Advocate consequence of absence]

NO-DOMAIN-BOUNDARY:
  Looked for:            explicit subdomain directories, business capability groupings
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)
  Hypothesis Relation:   [apply C-42 STATE_ENUM above]
  Inertia Implication:   [Inertia Advocate consequence of absence]

NO-WORKSPACE-GROUPING:
  Looked for:            monorepo workspace config grouping packages by area
  Detected:              [PRESENT | ABSENT | PARTIAL]
  Modes affected:        rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)
  Hypothesis Relation:   [apply C-42 STATE_ENUM above]
  Inertia Implication:   [Inertia Advocate consequence of absence]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE:  [label]
  STATE_ENUM result:                [YES -- CONFIRMED | YES -- OVERTURNED]
  Inertia Advocate status:          [Advocate defense is sound | Advocate is defending wrong mode]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27+C-43 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: ROLE 2 complete. No YAML. Maximum depth in this phase.

Open with hypothesis closure. Produce the 9-column weight table (DARK SIGNALS Penalty + Inertia
Cost columns). Close with a Selection Proof block tracing the full Net Score arithmetic for winner
and runner-up. The Selection Proof is the C-44 source for AMEND-A.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: precedes YAML; C-27: deliberation present
## C-43: weight-scoring table — DARK SIGNALS Penalty column satisfies C-37 structurally
## Inertia Cost column: Advocate structural consequence per mode (C-24 extension)
## Selection Proof: Net Score arithmetic — C-44 source

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  STATE_ENUM outcome:        [YES -- CONFIRMED | YES -- OVERTURNED]
  Inertia Advocate status:   [defense sound | defending wrong mode]
  Mode consequence:          [proceed | deliberation may select different mode]

Evidence Weight Table (9 columns):
(Scoring:
  Signal Strength: +1 to +3 per Evidence For schema row by signal-type
  Base: sum of Signal Strength values, cap 5
  DARK SIGNALS Penalty: ABSENT=4, PARTIAL=2, PRESENT=0 for mode's primary negative signal
  Inertia Cost: [low|moderate|high] — Advocate defense cost if this mode is selected
  Net = Base - Penalty; strong>=4, possible 2-3, weak 0-1)

| Mode      | Evidence For (rows + signal-type) | Signal Strength | DARK SIGNALS Penalty [label: magnitude] | Inertia Cost              | Base | Penalty | Net | Verdict  |
|-----------|-----------------------------------|-----------------|-----------------------------------------|---------------------------|------|---------|-----|----------|
| directory | [Repo signal values]              | [+N per row]    | NO-WORKSPACE-GROUPING: -[0|2|4]         | [low|moderate|high: why]  | [N]  | [N]     | [N] | [s/p/w]  |
| concept   | [Repo signal values]              | [+N per row]    | NO-DDD-LANGUAGE: -[0|2|4]               | [low|moderate|high: why]  | [N]  | [N]     | [N] | [s/p/w]  |
| service   | [Repo signal values]              | [+N per row]    | NO-SERVICE-MANIFEST: -[0|2|4]           | [low|moderate|high: why]  | [N]  | [N]     | [N] | [s/p/w]  |
| domain    | [Repo signal values]              | [+N per row]    | NO-DOMAIN-BOUNDARY: -[0|2|4]            | [low|moderate|high: why]  | [N]  | [N]     | [N] | [s/p/w]  |

Selection Proof (C-44 source):
  Winner:
    Mode:             [mode]
    Evidence For:     [schema row values] — Signal Strength: [+N, +N, ...]
    Base:             [sum] = [N]
    DARK SIGNALS:     [label] [ABSENT|PARTIAL|PRESENT] — Penalty: -[N]
    Net:              [N] - [N] = [N]  (verdict: [strong|possible|weak])
    Inertia Cost:     [low|moderate|high] — [one sentence on Advocate alignment]

  Runner-up:
    Mode:             [mode]
    Evidence For:     [schema row values] — Signal Strength: [+N, ...]
    Base:             [sum] = [N]
    DARK SIGNALS:     [label] [ABSENT|PARTIAL|PRESENT] — Penalty: -[N]
    Net:              [N] - [N] = [N]  (verdict: [strong|possible|weak])
    Inertia Cost:     [low|moderate|high] — [one sentence]

  Delta:              [winner Net] - [runner-up Net] = [N]
  Eliminator:         DARK SIGNALS [label] Penalty=-[N] reduced [runner-up] from [verdict] range

Selected pivot mode: [winner from Selection Proof]
Rationale: Net delta=[N]; DARK SIGNALS [label] eliminated [runner-up]; Inertia Cost for winner
  is [low|moderate|high] because [one sentence].
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. AMEND-A carries: DARK SIGNALS label (C-37); STATE_ENUM
hypothesis verdict (C-40); Selection Proof Net Score delta AND Inertia Advocate migration burden
(C-44 — both components present).

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Selection Proof delta: [N] ([winner] Net=[N] vs [runner-up] Net=[N]).
> STATE_ENUM: [YES -- CONFIRMED | YES -- OVERTURNED] — FALSIFICATION-SIGNAL [label].
> Inertia Advocate status: [sound | needs reconstruction]. C-05 ACKNOWLEDGED: no .roles/."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N], delta vs runner-up: [N]
# hypothesis: [YES -- CONFIRMED | YES -- OVERTURNED] — falsification-signal: [label]
# inertia-advocate-alignment: [aligned | misaligned] — Inertia Cost: [low|moderate|high]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # Inertia Advocate: exec-office Advocate anchors on current leadership structure.
    # Confirm name before corps-build.

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level Advocates share status-quo context — Inertia Cost for this group
      #   is [low|moderate|high] based on Selection Proof alignment.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [ROLE 2 "Repo signal" value]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same pattern.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: C-NN at satisfaction; C-30: 10 criteria; C-33: post-YAML bracket; C-34: C-02 essential)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"                  STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                      STATUS: [CONFIRMED/FAIL]
[ ] exec-office with Inertia Advocate note (C-07+C-24)                     STATUS: [CONFIRMED/FAIL]
[ ] Group containers with Inertia Cost annotation (C-03+C-24)              STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content (C-05)                                        STATUS: [CONFIRMED/FAIL]
[ ] C-43 9-column table with DARK SIGNALS Penalty + Inertia Cost columns   STATUS: [CONFIRMED/FAIL]
[ ] Selection Proof block with winner/runner-up/delta arithmetic            STATUS: [CONFIRMED/FAIL]
[ ] C-42 STATE_ENUM declared; 4-state + Inertia Implication on all entries STATUS: [CONFIRMED/FAIL]
[ ] C-41 typed fields (type annotations) on hypothesis claim                STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + verdict + Selection Proof delta + Inertia burden       STATUS: [CONFIRMED/FAIL]
    (C-37+C-40+C-44 — both delta and burden present)

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this block = post-YAML bracket.
C-30: C-02, C-04, C-07+C-24, C-03+C-24, C-05, C-43(table), C-43(proof), C-42+Inertia, C-41, C-37+C-40+C-44 — 10 items.
C-34: essential-tier C-02 present alongside aspirational criteria.
C-25: all sections self-labeled.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37+C-40+C-44: label + verdict + delta + burden)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):       STATE_ENUM [YES -- CONFIRMED | YES -- OVERTURNED] —
                                   FALSIFICATION-SIGNAL [label]
  Selection Proof delta (C-44):    Delta=[N]: [winner] Net=[N] vs [runner-up] Net=[N]
                                   (see ROLE 3 Selection Proof — independently verifiable)
  Inertia migration burden (C-44): Switching to [alternative mode] requires Inertia Advocate
                                   to reconstruct defense from [current structure] to
                                   [alternative structure] — Inertia Cost: [low|moderate|high].
  DARK SIGNALS basis (C-37):       [label] Penalty=-[N] reduced [runner-up] to Net=[N] < winner
  Debt if skipped:                 corps-build inherits misaligned pivot; Inertia Advocates
                                   anchor on wrong structure; Selection Proof delta and Inertia
                                   Cost documented but consequence ignored downstream.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Inertia note: exec-office Advocate anchors on this name — propagates into corps-rob
    governance and corps-committee appointment templates verbatim.
  Debt if skipped: no downstream correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Inertia note: Inertia Cost for current grouping is [low|moderate|high] (from Selection Proof).
    Misaligned groups give Advocates conflicting status-quo frames.
  Debt if skipped: corps-committee review signal coherence degraded across all review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R12 V-05). C-41: typed 3-field contract with field type annotations and
> Inertia Advocate framing in GATE. C-42: STATE_ENUM declared at DARK SIGNALS header; 4-state on
> all entries plus Inertia Implication sub-field. C-43: 9-column weight table with DARK SIGNALS
> Penalty + Inertia Cost columns and Selection Proof block. C-44: AMEND-A carries Selection Proof
> Net Score delta AND Inertia Advocate migration burden — both components present. Combination of
> typed contract (V-01) + inertia-first (V-02) + deliberation-expanded (V-03). All C-01 through
> C-44 requirements met. Draft-only."
