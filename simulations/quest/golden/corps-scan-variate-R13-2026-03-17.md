---
skill: quest-variate
skill_target: corps-scan
round: 13
date: 2026-03-17
rubric_version: 12
---

# Variate R13 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v12 rubric (290 pts,
48 criteria). R12's V-01 scored 285/290 (passes C-45/C-46/C-47, fails C-48) and V-02 scored
275/290 (passes C-48, fails C-45/C-46/C-47). C-45, C-46, C-47, and C-48 are now invariants —
ALL R13 variations must satisfy them. The variation axes govern HOW each variation implements
the typed magnitude scale, the verifiability chain, and the organizational cost dimension. They
do not govern whether.

R12 axes already covered (not re-explored in R13):
- Typed field declarations — type annotations on C-41 contract; STATE_ENUM at DARK SIGNALS header
- Inertia-first framing — Inertia Advocate as named participant; Inertia Implication per entry;
  Inertia Cost column in C-43 table; migration burden in C-44
- Scan-compressed, deliberation-expanded — minimal GATE/SCAN; Selection Proof block in DELIBERATE
- Conversational imperative register — second-person imperatives; C-NN in parentheses after verbs
- Combination — typed-contract + inertia-first + deliberation-expanded

R11 axes already covered (not re-explored):
- Hypothesis formalism — IF/PREDICT/FALSIFIED-BY; IS-FALSIFICATION-SIGNAL field
- Evidence weighting — deliberation as weight-scoring table; Net Score drives selection
- Amend ordering — hypothesis verdict as first amend field; C-16 debt secondary; chain audit
- Scan walk protocol — five numbered walk steps; step-scoped artifact types
- Combination — structured claim + weight table + amend-as-verdict

R13 explores three new single-axis variations and two combinations. All five variations treat
C-41, C-42, C-43, C-44, C-45, C-46, C-47, and C-48 as structurally required.

1. **Magnitude derivation protocol** — C-46 is implemented via a named 5-level Severity Scale
   defined at the DARK SIGNALS section header (ABSENT=4, PARTIAL-MAJOR=3, PARTIAL-MINOR=2,
   TRACE=1, PRESENT=0). Each entry carries an explicit "Severity: [0-4]" field with a one-phrase
   derivation note ("ABSENT — full penalty"). The deliberation table's Penalty column cell reads
   "[label: magnitude]" where the magnitude value is sourced directly from the entry's Severity
   field, making the penalty traceable to the DARK SIGNALS section without consulting the
   magnitude guide. AMEND-A declares the delta "(confirm: arithmetic traceable to ROLE 2
   Severity fields and ROLE 3 Penalty column — independently verifiable)."
   Hypothesis: 285/290 → 290/290 — explicit severity field per entry closes the C-46 magnitude
   traceability gap; the derivation note makes magnitude assignment independently auditable
   against the Detected field without trusting the table.

2. **Selection Audit phase** — A SELECTION AUDIT sub-phase is inserted between DELIBERATE PHASE
   and DRAFT+FINALIZE PHASE as ROLE 3.5. This section contains only the winner and runner-up
   rows reproduced verbatim from the ROLE 3 weight table, followed by a line-by-line arithmetic
   trace: "Winner: Base=[N] − Penalty=[N] = Net=[N]. Runner-up: Base=[N] − Penalty=[N] = Net=[N].
   Delta=[N]." AMEND-A's C-47 verifiability declaration cites the audit section by name:
   "(confirm from SELECTION AUDIT section above — independently verifiable)." C-48 is satisfied
   by an organizational cost column in ROLE 3.
   Hypothesis: 285/290 → 290/290 — the verifiability claim is structurally substantiated by
   a dedicated artifact rather than asserted inline; the audit section makes C-47 a structural
   property of the output, not a behavioral declaration.

3. **Pipeline Debt as cost dimension** — C-48 is satisfied by a "Pipeline Debt" column in the
   deliberation table rather than "Inertia Cost." Each mode row names which downstream corps-*
   stages (corps-build, corps-pr, corps-committee, corps-rob) are disrupted if that mode is
   selected and later changed. The column header declares "Pipeline Debt [stages:string]" — a
   typed annotation satisfying the orthogonal-to-evidence-structure requirement of C-48. AMEND-A
   carries both the C-47 verifiable delta and the Pipeline Debt consequence of switching modes.
   Hypothesis: 285/290 → 290/290 — Pipeline Debt is a structurally distinct organizational cost
   orthogonal to evidence weight (C-48), and it is more operationally specific than Inertia Cost:
   a reader can enumerate which pipeline stages to remediate without consulting the rubric.

Combined:
4. **Magnitude derivation + Selection Audit** — Combines axes 1 and 2. The 5-level Severity
   Scale defines magnitude per DARK SIGNALS entry; the SELECTION AUDIT phase reproduces the
   winner and runner-up rows with arithmetic sourced from those Severity fields. AMEND-A cites
   the audit section AND notes the arithmetic is traceable to ROLE 2 Severity fields.
   The audit chain is end-to-end: hypothesis (C-45) → Severity field (C-46 source) →
   Penalty column (C-46 display) → Selection Audit (C-47 verification artifact) → AMEND-A
   (C-47 assertion). C-48 satisfied by Inertia Cost or Pipeline Debt column.

5. **Magnitude derivation + Selection Audit + Pipeline Debt** — Full combination of axes 1, 2,
   and 3. Typed hypothesis contract (C-45). 5-level Severity Scale per DARK SIGNALS entry (C-46).
   Selection Audit section with arithmetic trace (C-47). Pipeline Debt column alongside DARK
   SIGNALS Penalty column (C-48). AMEND-A cites the audit section and Pipeline Debt consequence.
   The deliberation table carries: Evidence For / DARK SIGNALS Penalty [label:string, magnitude:0-4]
   / Pipeline Debt [stages:string] / Base / Penalty / Net / Verdict — 7 columns.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format — 5-level Severity Scale at DARK SIGNALS header; per-entry Severity field feeds Penalty magnitude; C-47 delta cites Severity traceability | V-01 |
| Lifecycle emphasis — SELECTION AUDIT sub-phase between DELIBERATE and DRAFT+FINALIZE; arithmetic trace in dedicated artifact; C-47 cites section by name | V-02 |
| Inertia framing — Pipeline Debt column [stages:string] as C-48 cost dimension; operationally named stages per mode; AMEND-A carries debt consequence | V-03 |
| Combination — magnitude derivation (axis 1) + Selection Audit (axis 2); end-to-end audit chain from Severity field to AMEND-A verifiability citation | V-04 |
| Combination — magnitude derivation (axis 1) + Selection Audit (axis 2) + Pipeline Debt (axis 3); 7-column deliberation table; full four-invariant implementation | V-05 |

---

## V-01 — Output Format: Magnitude Derivation Protocol

**Axis**: Output format — the C-46 magnitude scale is defined as a named 5-level Severity Scale
at the DARK SIGNALS section header; each entry carries an explicit "Severity: [0-4]" field with
a derivation note; the deliberation table Penalty column cell sources its magnitude value directly
from the entry's Severity field by cross-reference.
**Hypothesis**: R12 V-01 declared the magnitude guide ("ABSENT=4, PARTIAL=2, PRESENT=0") inline
with the table, treating magnitude as a lookup the model applies silently. The C-46 pass condition
requires the magnitude to appear in each penalty cell; it does not require the derivation to be
independently auditable at the entry level. A scorer checking the deliberation table must trust
that the magnitude value correctly reflects the "Detected" state. The Severity Scale axis addresses
this: by placing an explicit "Severity: [0-4]" field on each DARK SIGNALS entry, the magnitude
assignment is grounded at the point of detection, before the deliberation table is written. A
reader can confirm that the Penalty column magnitude matches the DARK SIGNALS entry Severity
without consulting the magnitude guide. Hypothesis: 290/290.

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

[ ] C-38+C-41+C-45 -- typed hypothesis claim (3-field contract with field type annotations):
    Fields: PREDICTED-MODE [type:pivot-mode-enum] / STRUCTURAL-PREDICTION [type:string] /
    FALSIFICATION-SIGNAL [type:absence-signal-enum]. Field types declared inline. Produced below.
    STATUS: CONFIRMED — produced before SCAN PHASE / ROLE 2 is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN column headers; DARK SIGNALS section
    with C-42 STATE_ENUM declared at section header; 5-level Severity Scale declared at header;
    each entry carries Severity field sourced from scale.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27+C-43+C-46+C-48 -- pivot deliberation as weight-scoring table; DARK SIGNALS Penalty
    column [label:string, magnitude:0-4] (magnitude sourced from ROLE 2 Severity fields);
    Inertia Cost column [cost:string] as orthogonal organizational cost dimension (C-48).
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS with STATE_ENUM; IS-FALSIFICATION-SIGNAL 4-state on each
    entry; Severity field per entry; Penalty column cites label + magnitude from Severity.
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40+C-44+C-47 -- debt-framed amend options; AMEND-A carries Net Score delta
    with verifiability declaration citing ROLE 2 Severity traceability; post-write cites 10+
    criteria (C-34 essential).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names all required outputs.
C-17: all SCHEDULED items name the delivering role.
C-18: C-NN IDs (including compound bundles) are primary keys throughout.
C-28: three-state vocabulary on every item.
C-29: compound bundles — "C-38+C-41+C-45", "C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43+C-46+C-48",
"C-36+C-37+C-39+C-42", "C-01+C-02+C-03+C-04", "C-16+C-30+C-40+C-44+C-47".
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 STATUS: ACKNOWLEDGED — essential failure named with consequence.

**Typed Hypothesis Claim** `(C-38+C-41+C-45 satisfier; C-25: self-labeled; produced before SCAN PHASE)`

```
TYPED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38: hypothesis declared before any repo scanning begins)
(C-41: 3-field labeled contract)
(C-45: each field carries machine-readable type annotation — value domain explicitly declared)
(C-25: section self-labeled)
(Downstream: C-42 STATE_ENUM + 5-level Severity Scale declared at DARK SIGNALS header in ROLE 2;
 C-46 Penalty column sources magnitude from ROLE 2 Severity fields in ROLE 3;
 C-47 AMEND-A cites Severity traceability in ROLE 4)

PREDICTED-MODE:        [type: pivot-mode-enum — values: directory | concept | service | domain]
                       value: [fill one]

STRUCTURAL-PREDICTION: [type: structural-evidence-string — one sentence naming observable repo
                        structure this mode predicts, e.g., "packages grouped under functional
                        area directories with matching workspace config clusters"]
                       value: "[one sentence]"

FALSIFICATION-SIGNAL:  [type: absence-signal-enum — values: NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE
                        | NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
                       value: [the label that, if ABSENT in ROLE 2, overturns this claim]

CONFIDENCE:            [type: confidence-enum — values: high | medium | low]
                       value: [fill one]

BASIS:                 [type: string — one sentence of repo evidence grounding PREDICTED-MODE]
                       value: "[first-pass read evidence]"
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

The 5-level Severity Scale is declared at the DARK SIGNALS section header. Each entry's
"Severity" field is sourced from this scale and carries a one-phrase derivation note. The
deliberation table in ROLE 3 will read magnitude values directly from these Severity fields.

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

#### DARK SIGNALS `(C-36+C-39+C-42+C-46 source; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals, Hypothesis Relations, and Severity Scores
## C-36: structured negative evidence with per-entry mode impact
## C-39: Hypothesis Relation field (IS-FALSIFICATION-SIGNAL) on each entry
## C-42: 4-state vocabulary — STATE_ENUM declared below (applies to all entries)
## C-46 source: Severity field per entry — magnitude values sourced into ROLE 3 Penalty column
## C-25: self-labeled; C-37 downstream: labels appear in ROLE 3 Penalty column

C-42 STATE_ENUM (apply to "Hypothesis Relation" field of every entry below):
  YES -- CONFIRMED            : this entry IS the GATE FALSIFICATION-SIGNAL; signal PRESENT/PARTIAL
  YES -- OVERTURNED           : this entry IS the GATE FALSIFICATION-SIGNAL; signal ABSENT
  NO -- corroborates-alternative([mode]) : NOT the FALSIFICATION-SIGNAL; absence supports [mode]
  NO -- neutral               : NOT the FALSIFICATION-SIGNAL; no bearing on stated hypothesis

5-LEVEL SEVERITY SCALE (C-46 source — apply to "Severity" field of every entry below):
  4 — ABSENT        : signal completely absent; mode ruled out
  3 — PARTIAL-MAJOR : signal partially present, major gaps; mode significantly weakened
  2 — PARTIAL-MINOR : signal partially present, minor gaps; mode weakened but viable
  1 — TRACE         : signal present in trace form only; mode weakly supported
  0 — PRESENT       : signal fully present; no penalty applied

NO-SERVICE-MANIFEST:
  Looked for:          docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:            [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected:      rules out service mode (ABSENT) / weakens service mode (PARTIAL-*)
  Hypothesis Relation: [apply STATE_ENUM above]
  Severity:            [0-4 — apply 5-level scale; one phrase: e.g., "4 — ABSENT, no manifest found"]

NO-DDD-LANGUAGE:
  Looked for:          bounded context names, aggregate roots, domain events in dir/module names
  Detected:            [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected:      rules out concept mode (ABSENT) / weakens concept mode (PARTIAL-*)
  Hypothesis Relation: [apply STATE_ENUM above]
  Severity:            [0-4 — apply 5-level scale; one phrase]

NO-DOMAIN-BOUNDARY:
  Looked for:          explicit subdomain directories, business capability groupings
  Detected:            [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected:      rules out domain mode (ABSENT) / weakens domain mode (PARTIAL-*)
  Hypothesis Relation: [apply STATE_ENUM above]
  Severity:            [0-4 — apply 5-level scale; one phrase]

NO-WORKSPACE-GROUPING:
  Looked for:          monorepo workspace config grouping packages by area
  Detected:            [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected:      rules out directory mode (ABSENT) / weakens directory mode (PARTIAL-*)
  Hypothesis Relation: [apply STATE_ENUM above]
  Severity:            [0-4 — apply 5-level scale; one phrase]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [GATE label]
  That entry's STATE_ENUM value:  [YES -- CONFIRMED | YES -- OVERTURNED]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27+C-43+C-46+C-48 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 Signal Schema and DARK SIGNALS complete. No YAML.

Open with hypothesis closure. Then produce the weight-scoring table. The DARK SIGNALS Penalty
column header carries "[label:string, magnitude:0-4]" (C-46). Penalty magnitude values are
sourced from ROLE 2 Severity fields — cite the DARK SIGNALS entry label and copy its Severity
value as the magnitude (e.g., "NO-SERVICE-MANIFEST: 4"). The Inertia Cost column satisfies C-48
as an orthogonal organizational cost dimension.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: evidence triad per candidate
## C-43: weight-scoring table with DARK SIGNALS Penalty column
## C-46: Penalty column carries [label:string, magnitude:0-4] — magnitude sourced from ROLE 2 Severity
## C-48: Inertia Cost column — orthogonal organizational cost, not evidence signal

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  STATE_ENUM outcome:       [YES -- CONFIRMED | YES -- OVERTURNED]
  Consequence:              [proceed with predicted mode | deliberation may select different mode]

Evidence Weight Table:
(Column types:
  Mode:                                enum[directory|concept|service|domain]
  Evidence For:                        string(schema row "Repo signal" values, comma-separated)
  DARK SIGNALS Penalty [label:string,  string(label from ROLE 2 DARK SIGNALS entry +
    magnitude:0-4]:                      magnitude copied from that entry's Severity field)
  Inertia Cost [cost:string]:          string(one phrase — what current structure the org must
                                         reconstruct if this mode is selected and later changed)
  Base:                                int(1-5, from Evidence For count + signal-type strength)
  Penalty:                             int(0-4, copied from DARK SIGNALS entry Severity field)
  Net:                                 int(Base minus Penalty)
  Verdict:                             enum[strong|possible|weak] — strong>=4, possible 2-3, weak<=1)

| Mode      | Evidence For (schema rows)       | DARK SIGNALS Penalty [label: magnitude] | Inertia Cost [cost]                   | Base | Penalty | Net | Verdict |
|-----------|----------------------------------|-----------------------------------------|---------------------------------------|------|---------|-----|---------|
| directory | [Repo signal values from schema] | NO-WORKSPACE-GROUPING: [Severity value] | [org reconstruction cost if changed]  | [N]  | [N]     | [N] | [s/p/w] |
| concept   | [Repo signal values from schema] | NO-DDD-LANGUAGE: [Severity value]       | [org reconstruction cost if changed]  | [N]  | [N]     | [N] | [s/p/w] |
| service   | [Repo signal values from schema] | NO-SERVICE-MANIFEST: [Severity value]   | [org reconstruction cost if changed]  | [N]  | [N]     | [N] | [s/p/w] |
| domain    | [Repo signal values from schema] | NO-DOMAIN-BOUNDARY: [Severity value]    | [org reconstruction cost if changed]  | [N]  | [N]     | [N] | [s/p/w] |

Magnitude sourcing note: each Penalty magnitude value above is copied directly from the
corresponding DARK SIGNALS entry Severity field in ROLE 2 — no separate derivation needed.

Net Score arithmetic trace:
  Winner:    [mode] — Base=[N] minus Penalty=[N] = Net=[N]
  Runner-up: [mode] — Base=[N] minus Penalty=[N] = Net=[N]
  Delta:     [winner Net] minus [runner-up Net] = [N]

Selected pivot mode: [mode with highest Net Score]
Rationale: Net Score delta=[N]; DARK SIGNALS [label] Severity=[N] penalty eliminated [runner-up].
  Inertia Cost for [winner] is [low/moderate/high] — [one phrase from Inertia Cost cell].
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. No new scanning or deliberation.

AMEND-A must: (a) cite the DARK SIGNALS label from the Penalty column (C-37); (b) carry
hypothesis verdict — STATE_ENUM outcome from ROLE 2 (C-40); (c) carry the Net Score arithmetic
delta from ROLE 3 (C-44); (d) declare the delta independently verifiable and cite ROLE 2
Severity traceability (C-47).

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
(C-19: criterion IDs cited at point of satisfaction; C-30: 10+ criteria cited;
 C-33: post-YAML bracket; C-34: essential-tier C-02 cited in this inventory)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"                    STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                        STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                       STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                              STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                                 STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level in YAML (C-24)                  STATUS: [CONFIRMED/FAIL]
[ ] C-43 weight table: DARK SIGNALS Penalty [label:string, magnitude:0-4] (C-46)  STATUS: [CONFIRMED/FAIL]
[ ] C-48 Inertia Cost column present and orthogonal to evidence structure    STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                                STATUS: [CONFIRMED/FAIL]
[ ] C-42 STATE_ENUM declared; 5-level Severity Scale declared (C-46 source)  STATUS: [CONFIRMED/FAIL]
[ ] Each DARK SIGNALS entry carries Severity field with derivation note       STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + verdict + Net delta + verifiability citation (C-37+C-40+C-44+C-47) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this block = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-46, C-48, C-25, C-42, Severity, C-37+C-40+C-44+C-47 — 12 items.
C-34: essential-tier C-02 present alongside aspirational criteria.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37+C-40+C-44+C-47: label + verdict + delta + verifiability)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):     [YES -- CONFIRMED — predicted mode supported |
                                  YES -- OVERTURNED — FALSIFICATION-SIGNAL [label] absent]
  Net Score arithmetic (C-44):   [selected mode] Net=[N] vs [runner-up] Net=[N]; delta=[N]
                                  (confirm: magnitude sourced from ROLE 2 Severity fields,
                                   arithmetic in ROLE 3 table — independently verifiable) (C-47)
  DARK SIGNALS basis (C-37):     [label] Severity=[N] → Penalty=-[N]; eliminated [runner-up]
  Debt if skipped:                corps-build, corps-pr, corps-committee, corps-rob inherit
                                  misaligned clustering; Severity-grounded arithmetic available
                                  but hypothesis consequence ignored downstream.
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

> "corps-scan complete (R13 V-01). C-45: typed hypothesis contract — field type annotations
> on all fields. C-46: DARK SIGNALS Penalty [label:string, magnitude:0-4] — magnitude sourced
> from per-entry Severity fields via 5-level scale. C-47: AMEND-A delta declared independently
> verifiable with Severity traceability citation. C-48: Inertia Cost column orthogonal to
> evidence structure. All C-01 through C-48 requirements met. Draft-only."

---

## V-02 — Lifecycle Emphasis: Selection Audit Phase

**Axis**: Lifecycle emphasis — a SELECTION AUDIT sub-phase (ROLE 3.5) is inserted between
DELIBERATE PHASE and DRAFT+FINALIZE PHASE. This section reproduces only the winner and runner-up
rows from the ROLE 3 weight table verbatim, followed by a line-by-line arithmetic trace. AMEND-A
cites this section by name for the C-47 verifiability declaration rather than asserting the claim
inline. C-48 is satisfied by an Inertia Cost column in ROLE 3.
**Hypothesis**: R12 V-01 declares "(independently verifiable)" inline in AMEND-A — the claim is
behavioral: the model asserts the arithmetic is checkable, but does not create the checking
artifact. A reader who wants to verify must navigate to ROLE 3, identify the relevant rows, and
perform the arithmetic themselves. The Selection Audit phase addresses this: it creates a
dedicated artifact at the output's midpoint that reproduces the relevant rows in canonical form
and states the arithmetic explicitly. AMEND-A then cites this artifact by section name, making
the verifiability claim structurally substantiated rather than asserted. Hypothesis: 290/290.

---

You are running `corps-scan`. Work through five named roles in strict sequence.
**ROLE 2, ROLE 3, ROLE 3.5, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and typed
hypothesis claim.**

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

[ ] C-38+C-41+C-45 -- typed hypothesis claim (3-field contract with machine-readable type
    annotations on each field). Produced below this pre-check.
    STATUS: CONFIRMED — produced before SCAN PHASE / ROLE 2 is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN column headers; DARK SIGNALS section
    with C-42 STATE_ENUM declared at header before entries.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27+C-43+C-46+C-48 -- pivot deliberation as weight-scoring table; Penalty column
    [label:string, magnitude:0-4] (C-46); Inertia Cost column (C-48).
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-47 -- SELECTION AUDIT section reproduces winner + runner-up rows; arithmetic trace;
    AMEND-A cites section by name as verifiability artifact.
    STATUS: SCHEDULED — SELECTION AUDIT / ROLE 3.5.

[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS with STATE_ENUM; Penalty column cites labels;
    AMEND-A cites label + verdict + delta + Selection Audit citation.
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 3.5 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40+C-44 -- debt-framed amend options; AMEND-A carries verdict + delta +
    Selection Audit citation; post-write cites 10+ criteria (C-34 essential).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names all required outputs.
C-17: all SCHEDULED items name the delivering role.
C-18: C-NN IDs (including compound bundles) are primary keys throughout.
C-28: three-state vocabulary on every item.
C-29: compound bundles — "C-38+C-41+C-45", "C-11+C-21+C-22+C-25+C-26",
"C-23+C-27+C-43+C-46+C-48", "C-36+C-37+C-39+C-42", "C-01+C-02+C-03+C-04",
"C-16+C-30+C-40+C-44".
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 STATUS: ACKNOWLEDGED — essential failure named with consequence.

**Typed Hypothesis Claim** `(C-38+C-41+C-45 satisfier; C-25: self-labeled; produced before SCAN PHASE)`

```
TYPED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38: hypothesis declared before scanning; C-41: 3-field labeled contract;
 C-45: machine-readable type annotation on each field; C-25: self-labeled)
(Downstream: SELECTION AUDIT / ROLE 3.5 will reproduce winner + runner-up rows;
 AMEND-A will cite Selection Audit by name for C-47 verifiability)

PREDICTED-MODE:        [type: pivot-mode-enum — values: directory | concept | service | domain]
                       value: [fill one]

STRUCTURAL-PREDICTION: [type: structural-evidence-string — one sentence: observable repo
                        structure the predicted mode implies]
                       value: "[one sentence]"

FALSIFICATION-SIGNAL:  [type: absence-signal-enum — values: NO-SERVICE-MANIFEST |
                        NO-DDD-LANGUAGE | NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
                       value: [the label that, if ABSENT in ROLE 2, overturns this claim]

CONFIDENCE:            [type: confidence-enum — values: high | medium | low]
                       value: [fill one]

BASIS:                 [type: string — one sentence of repo evidence]
                       value: "[evidence]"
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE PHASE / ROLE 1 complete. Produce Signal Schema and DARK SIGNALS section.
No pivot deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests (`docker-compose.yml`, `k8s/`, Helm charts). Workspace configs. Domain vocabulary.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: criterion purpose declared in header; C-25: self-labeled; C-33: pre-YAML bracket

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |

Rules:
- Minimum 2 rows. PLACEHOLDER row if fewer detected signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence of repo evidence per row.
- Cap at 8 rows.

Exec office inference: [schema row or term, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals and Hypothesis Relations
## C-36: structured negative evidence with per-entry mode impact
## C-39: Hypothesis Relation (IS-FALSIFICATION-SIGNAL) on each entry
## C-42: 4-state STATE_ENUM declared below — applies to all entries
## C-25: self-labeled; C-37 downstream: labels appear in ROLE 3 Penalty column

C-42 STATE_ENUM:
  YES -- CONFIRMED            : IS the GATE FALSIFICATION-SIGNAL; signal PRESENT/PARTIAL
  YES -- OVERTURNED           : IS the GATE FALSIFICATION-SIGNAL; signal ABSENT
  NO -- corroborates-alternative([mode]) : NOT FALSIFICATION-SIGNAL; absence supports [mode]
  NO -- neutral               : NOT FALSIFICATION-SIGNAL; no hypothesis bearing

NO-SERVICE-MANIFEST:
  Looked for:          docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM]

NO-DDD-LANGUAGE:
  Looked for:          bounded context names, aggregate roots, domain events in naming
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM]

NO-DOMAIN-BOUNDARY:
  Looked for:          explicit subdomain directories, business capability groupings
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM]

NO-WORKSPACE-GROUPING:
  Looked for:          monorepo workspace config grouping packages by area
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [GATE label]
  That entry's STATE_ENUM value:  [YES -- CONFIRMED | YES -- OVERTURNED]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27+C-43+C-46+C-48 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 complete. No YAML.

Produce the weight-scoring table with typed Penalty column [label:string, magnitude:0-4] (C-46)
and Inertia Cost column [cost:string] (C-48). The SELECTION AUDIT in ROLE 3.5 will reproduce
the winner and runner-up rows verbatim — write those rows with full detail.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23+C-27: deliberation with Evidence For/Against per candidate
## C-43: weight-scoring table; C-46: Penalty [label:string, magnitude:0-4]; C-48: Inertia Cost

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  STATE_ENUM outcome:       [YES -- CONFIRMED | YES -- OVERTURNED]
  Consequence:              [proceed with predicted mode | deliberation may select different mode]

Evidence Weight Table:
(Magnitude: ABSENT=4, PARTIAL=2, PRESENT=0)

| Mode      | Evidence For (schema rows)       | DARK SIGNALS Penalty [label: magnitude] | Inertia Cost [cost]              | Base | Penalty | Net | Verdict |
|-----------|----------------------------------|-----------------------------------------|----------------------------------|------|---------|-----|---------|
| directory | [Repo signal values from schema] | NO-WORKSPACE-GROUPING: [0|2|4]          | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |
| concept   | [Repo signal values from schema] | NO-DDD-LANGUAGE: [0|2|4]                | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |
| service   | [Repo signal values from schema] | NO-SERVICE-MANIFEST: [0|2|4]            | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |
| domain    | [Repo signal values from schema] | NO-DOMAIN-BOUNDARY: [0|2|4]             | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |

Selected pivot mode: [mode with highest Net Score]
Net Score delta: [winner Net] - [runner-up Net] = [N]
```

DELIBERATE PHASE / ROLE 3 complete. SELECTION AUDIT / ROLE 3.5 may now begin.

---

### ROLE 3.5 — SELECTION AUDIT / ARITHMETIC VERIFIER
`(C-25: self-labeled; C-47 satisfier; C-31: SELECTION AUDIT — between DELIBERATE and DRAFT+FINALIZE)`

Prerequisite: DELIBERATE PHASE / ROLE 3 complete. No YAML. No new analysis.

Reproduce only the winner and runner-up rows from the ROLE 3 weight table verbatim. State the
arithmetic explicitly, line by line. This section is the verification artifact cited by AMEND-A.

```
## Selection Audit — {{date}}
## C-47 satisfier: dedicated arithmetic verification artifact
## C-25: self-labeled; C-31: SELECTION AUDIT phase
## AMEND-A will cite this section as: "(confirm from SELECTION AUDIT above — independently verifiable)"

Reproduced from ROLE 3 weight table (verbatim — no new analysis):

Winner row:
  Mode:     [selected mode]
  Evidence For:  [exact text from ROLE 3 winner row]
  DARK SIGNALS Penalty:  [label]: [magnitude]
  Inertia Cost:  [exact text from ROLE 3 winner row]
  Base=[N], Penalty=[N], Net=[N], Verdict=[s/p/w]

Runner-up row:
  Mode:     [runner-up mode]
  Evidence For:  [exact text from ROLE 3 runner-up row]
  DARK SIGNALS Penalty:  [label]: [magnitude]
  Inertia Cost:  [exact text from ROLE 3 runner-up row]
  Base=[N], Penalty=[N], Net=[N], Verdict=[s/p/w]

Arithmetic trace:
  Winner:    Base=[N] − Penalty=[N] = Net=[N]
  Runner-up: Base=[N] − Penalty=[N] = Net=[N]
  Delta:     [winner Net] − [runner-up Net] = [N]

Verification: a reader can confirm these values from the ROLE 3 table above without trusting
  the model's assertion. The arithmetic is independently checkable from this section alone.
```

SELECTION AUDIT / ROLE 3.5 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. No new scanning or deliberation.

AMEND-A must: (a) cite the DARK SIGNALS label (C-37); (b) carry hypothesis verdict (C-40);
(c) carry Net Score delta (C-44); (d) cite the SELECTION AUDIT section by name as the
verifiability artifact (C-47).

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Net Score delta: [N] (confirm from SELECTION AUDIT above).
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
(C-19: C-NN IDs at satisfaction point; C-30: 10+ criteria; C-33: post-YAML bracket;
 C-34: essential-tier C-02 cited)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"                    STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                        STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                       STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                              STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                                 STATUS: [CONFIRMED/FAIL]
[ ] C-43 weight table: Penalty [label:string, magnitude:0-4] (C-46)          STATUS: [CONFIRMED/FAIL]
[ ] C-48 Inertia Cost column orthogonal to evidence structure                STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                                STATUS: [CONFIRMED/FAIL]
[ ] C-42 STATE_ENUM declared at DARK SIGNALS header                          STATUS: [CONFIRMED/FAIL]
[ ] SELECTION AUDIT section present; winner + runner-up rows + arithmetic (C-47) STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A cites Selection Audit by name (C-47); carries label + verdict + delta (C-37+C-40+C-44) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) + this block (post-YAML) — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this block = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-46, C-48, C-25, C-42, C-47, C-37+C-40+C-44 — 11 items.
C-34: essential-tier C-02 present alongside aspirational criteria.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37+C-40+C-44+C-47: label + verdict + delta + audit citation)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):     [YES -- CONFIRMED — predicted mode supported |
                                  YES -- OVERTURNED — FALSIFICATION-SIGNAL [label] absent]
  Net Score arithmetic (C-44):   [selected mode] Net=[N] vs [runner-up] Net=[N]; delta=[N]
                                  (confirm from SELECTION AUDIT section above —
                                   independently verifiable) (C-47)
  DARK SIGNALS basis (C-37):     [label] Penalty=-[N] eliminated [runner-up mode]
  Debt if skipped:                corps-build, corps-pr, corps-committee, corps-rob inherit
                                  misaligned clustering; Selection Audit arithmetic available
                                  but hypothesis consequence ignored downstream.
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

> "corps-scan complete (R13 V-02). C-45: typed hypothesis contract with field type annotations.
> C-46: Penalty column [label:string, magnitude:0-4] in ROLE 3 table. C-47: SELECTION AUDIT
> phase reproduces winner + runner-up rows with arithmetic trace; AMEND-A cites by name.
> C-48: Inertia Cost column orthogonal to evidence structure. Draft-only."

---

## V-03 — Inertia Framing: Pipeline Debt as Cost Dimension

**Axis**: Inertia framing — C-48 is satisfied by a "Pipeline Debt" column rather than an
"Inertia Cost" column. Each mode row names which downstream corps-* stages are disrupted if
that mode is selected and later changed. The column header declares
"Pipeline Debt [stages:string]" — typed, orthogonal to evidence structure.
**Hypothesis**: R12 V-02 used "Inertia Cost" as the C-48 organizational cost dimension. This
is a valid implementation but its meaning is implicit: "Inertia Cost" requires the reader to
interpret what "cost" means operationally. Pipeline Debt is operationally specific: it names
concrete pipeline stages by label (corps-build, corps-pr, corps-committee, corps-rob). A reader
who selects a mode knowing its Pipeline Debt can enumerate exactly which downstream stages to
re-run if the mode is later changed. The Inertia Advocate framing (C-24) is preserved in YAML
comments; Pipeline Debt is the deliberation table's orthogonal cost column. Hypothesis: 290/290.

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

[ ] C-13 -- C-12 precedes this pre-check.
    STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files, role file content, or role-creation instructions.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification regardless
    of composite score.

[ ] C-38+C-41+C-45 -- typed hypothesis claim: 3-field contract with machine-readable type
    annotations. Produced below this pre-check.
    STATUS: CONFIRMED — produced before SCAN PHASE / ROLE 2 is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN column headers; DARK SIGNALS with
    C-42 STATE_ENUM declared at section header before entries.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27+C-43+C-46+C-48 -- pivot deliberation as weight-scoring table; DARK SIGNALS
    Penalty column [label:string, magnitude:0-4] (C-46); Pipeline Debt column [stages:string]
    as orthogonal organizational cost dimension (C-48).
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS with STATE_ENUM; Penalty column cites labels;
    AMEND-A cites label + verdict + delta + verifiability declaration + Pipeline Debt.
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40+C-44+C-47 -- debt-framed amend options; AMEND-A carries Net Score delta
    (independently verifiable) and Pipeline Debt consequence; post-write cites 10+ criteria
    (C-34 essential).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names all required outputs.
C-17: all SCHEDULED items name the delivering role.
C-18: C-NN IDs (including compound bundles) are primary keys throughout.
C-28: three-state vocabulary on every item.
C-29: compound bundles — "C-38+C-41+C-45", "C-11+C-21+C-22+C-25+C-26",
"C-23+C-27+C-43+C-46+C-48", "C-36+C-37+C-39+C-42", "C-01+C-02+C-03+C-04",
"C-16+C-30+C-40+C-44+C-47".
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 STATUS: ACKNOWLEDGED — essential failure named with consequence.

**Typed Hypothesis Claim** `(C-38+C-41+C-45 satisfier; C-25: self-labeled; produced before SCAN PHASE)`

```
TYPED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38: hypothesis before scanning; C-41: 3-field labeled contract;
 C-45: machine-readable type annotation on each field; C-25: self-labeled)
(Downstream: C-46 Penalty column sourced from DARK SIGNALS entries in ROLE 2;
 C-48 Pipeline Debt column in ROLE 3; C-47 verifiability declared on AMEND-A in ROLE 4)

PREDICTED-MODE:        [type: pivot-mode-enum — values: directory | concept | service | domain]
                       value: [fill one]

STRUCTURAL-PREDICTION: [type: structural-evidence-string — one sentence: observable repo
                        structure this mode predicts]
                       value: "[one sentence]"

FALSIFICATION-SIGNAL:  [type: absence-signal-enum — values: NO-SERVICE-MANIFEST |
                        NO-DDD-LANGUAGE | NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
                       value: [the label that, if ABSENT in ROLE 2, overturns this claim]

CONFIDENCE:            [type: confidence-enum — values: high | medium | low]
                       value: [fill one]

BASIS:                 [type: string — one sentence of repo evidence]
                       value: "[evidence]"
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE PHASE / ROLE 1 complete. Produce Signal Schema and DARK SIGNALS section.
No pivot deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: criterion purpose declared in header; C-25: self-labeled; C-33: pre-YAML bracket

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |

Rules:
- Minimum 2 rows. PLACEHOLDER row if fewer signals.
- "YAML name (C-02)": exact string for YAML teams[].name.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence per row.

Exec office inference: [schema row or term, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals and Hypothesis Relations
## C-36: structured negative evidence with per-entry mode impact
## C-39: Hypothesis Relation field on each entry
## C-42: IS-FALSIFICATION-SIGNAL typed field — STATE_ENUM declared below
## C-25: self-labeled; C-37 downstream: labels appear in ROLE 3 Penalty column

C-42 STATE_ENUM:
  YES -- CONFIRMED            : IS the GATE FALSIFICATION-SIGNAL; signal PRESENT/PARTIAL
  YES -- OVERTURNED           : IS the GATE FALSIFICATION-SIGNAL; signal ABSENT
  NO -- corroborates-alternative([mode]) : NOT FALSIFICATION-SIGNAL; absence supports [mode]
  NO -- neutral               : no hypothesis bearing

NO-SERVICE-MANIFEST:
  Looked for:          docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis Relation: [apply STATE_ENUM]

NO-DDD-LANGUAGE:
  Looked for:          bounded context names, aggregate roots, domain events in naming
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out concept mode / weakens concept mode
  Hypothesis Relation: [apply STATE_ENUM]

NO-DOMAIN-BOUNDARY:
  Looked for:          explicit subdomain directories, business capability groupings
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out domain mode / weakens domain mode
  Hypothesis Relation: [apply STATE_ENUM]

NO-WORKSPACE-GROUPING:
  Looked for:          monorepo workspace config grouping packages by area
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out directory mode / weakens directory mode
  Hypothesis Relation: [apply STATE_ENUM]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [GATE label]
  That entry's STATE_ENUM value:  [YES -- CONFIRMED | YES -- OVERTURNED]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27+C-43+C-46+C-48 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 complete. No YAML.

Produce the weight-scoring table. The DARK SIGNALS Penalty column carries typed composite
annotation [label:string, magnitude:0-4] (C-46). The Pipeline Debt column names which
corps-* stages are disrupted if that mode is selected and later changed (C-48). Column header
declares "Pipeline Debt [stages:string]".

Pipeline Debt vocabulary: corps-build (role file generation) / corps-pr (PR template alignment) /
corps-committee (committee roster coherence) / corps-rob (exec-office governance chain). Name
only the stages actually disrupted per mode. Use "none" if mode is stable.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23+C-27: Evidence For/Against/Assessment per candidate
## C-43: weight-scoring table; C-46: Penalty [label:string, magnitude:0-4]
## C-48: Pipeline Debt [stages:string] — orthogonal organizational cost, not evidence signal

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  STATE_ENUM outcome:       [YES -- CONFIRMED | YES -- OVERTURNED]
  Consequence:              [proceed with predicted mode | deliberation may select different mode]

Evidence Weight Table:
(Magnitude: ABSENT=4, PARTIAL=2, PRESENT=0)

| Mode      | Evidence For (schema rows)       | DARK SIGNALS Penalty [label: magnitude] | Pipeline Debt [stages]                             | Base | Penalty | Net | Verdict |
|-----------|----------------------------------|-----------------------------------------|----------------------------------------------------|------|---------|-----|---------|
| directory | [Repo signal values from schema] | NO-WORKSPACE-GROUPING: [0|2|4]          | [corps-* stages disrupted if changed, or "none"]   | [N]  | [N]     | [N] | [s/p/w] |
| concept   | [Repo signal values from schema] | NO-DDD-LANGUAGE: [0|2|4]                | [corps-* stages disrupted if changed, or "none"]   | [N]  | [N]     | [N] | [s/p/w] |
| service   | [Repo signal values from schema] | NO-SERVICE-MANIFEST: [0|2|4]            | [corps-* stages disrupted if changed, or "none"]   | [N]  | [N]     | [N] | [s/p/w] |
| domain    | [Repo signal values from schema] | NO-DOMAIN-BOUNDARY: [0|2|4]             | [corps-* stages disrupted if changed, or "none"]   | [N]  | [N]     | [N] | [s/p/w] |

Net Score arithmetic trace:
  Winner:    [mode] — Base=[N] minus Penalty=[N] = Net=[N]
  Runner-up: [mode] — Base=[N] minus Penalty=[N] = Net=[N]
  Delta:     [winner Net] minus [runner-up Net] = [N]

Selected pivot mode: [mode with highest Net Score]
Rationale: Net Score delta=[N]; DARK SIGNALS [label] penalty -[N] eliminated [runner-up].
  Pipeline Debt for [winner] is [stages — low disruption | moderate disruption | stages named].
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. AMEND-A must: (a) cite DARK SIGNALS label (C-37);
(b) carry hypothesis verdict (C-40); (c) carry Net Score delta (C-44) with verifiability
declaration (C-47); (d) name the Pipeline Debt consequence of switching modes.

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Net Score delta: [N] ([winner] Net=[N] vs [runner-up] Net=[N]).
> Hypothesis STATE_ENUM: [YES -- CONFIRMED | YES -- OVERTURNED] — FALSIFICATION-SIGNAL [label].
> Pipeline Debt for selected mode: [stages or 'none'].
> C-05 ACKNOWLEDGED in GATE: no .roles/ content here."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N]
# hypothesis-outcome: [YES -- CONFIRMED | YES -- OVERTURNED]
# falsification-signal: [GATE label]
# pipeline-debt: [stages disrupted if mode changes, or "none"]
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
(C-19: C-NN IDs at satisfaction point; C-30: 10+ criteria; C-33: post-YAML bracket;
 C-34: essential-tier C-02 cited)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"                    STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                        STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                       STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                              STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                                 STATUS: [CONFIRMED/FAIL]
[ ] C-43 Penalty [label:string, magnitude:0-4] present (C-46)               STATUS: [CONFIRMED/FAIL]
[ ] Pipeline Debt [stages:string] column present (C-48)                      STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                                STATUS: [CONFIRMED/FAIL]
[ ] C-42 STATE_ENUM declared at DARK SIGNALS header                          STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + verdict + delta + verifiability + Pipeline Debt (C-37+C-40+C-44+C-47) STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at group and team level in YAML (C-24)                  STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) + this block (post-YAML) — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this block = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-46, C-48, C-25, C-42, C-37+C-40+C-44+C-47, C-24 — 11 items.
C-34: essential-tier C-02 present alongside aspirational criteria.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37+C-40+C-44+C-47)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):     [YES -- CONFIRMED — predicted mode supported |
                                  YES -- OVERTURNED — FALSIFICATION-SIGNAL [label] absent]
  Net Score arithmetic (C-44):   [selected mode] Net=[N] vs [runner-up] Net=[N]; delta=[N]
                                  (independently verifiable from ROLE 3 table) (C-47)
  DARK SIGNALS basis (C-37):     [label] Penalty=-[N] eliminated [runner-up mode]
  Pipeline Debt if switched:     Changing to [alternative mode] disrupts [stages] — each
                                  stage must re-run after pivot change.
  Debt if skipped:               corps-build inherits misaligned clustering; [stages] pipeline
                                  debt accumulates silently until corps-rob surfaces it.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: Exec-office name propagates into corps-rob and corps-committee verbatim.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Debt if skipped: Misaligned groups degrade corps-committee review signal coherence.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R13 V-03). C-45: typed hypothesis contract with field type annotations.
> C-46: Penalty column [label:string, magnitude:0-4] in ROLE 3 table. C-47: AMEND-A Net Score
> delta declared independently verifiable. C-48: Pipeline Debt column [stages:string] names
> concrete corps-* stages disrupted per mode — orthogonal to evidence structure. Draft-only."

---

## V-04 — Combination: Magnitude Derivation + Selection Audit

**Axis**: Combination of V-01 (magnitude derivation protocol) and V-02 (Selection Audit phase).
The 5-level Severity Scale defines per-entry magnitude in DARK SIGNALS; the SELECTION AUDIT
phase reproduces the winner and runner-up rows with arithmetic trace. AMEND-A cites the audit
section by name AND notes the arithmetic is traceable to ROLE 2 Severity fields, making the
end-to-end audit chain explicit: hypothesis contract (C-45) → Severity field (C-46 source) →
Penalty column (C-46 display) → Selection Audit (C-47 verification artifact) → AMEND-A.
C-48 is satisfied by an Inertia Cost column in ROLE 3.
**Hypothesis**: V-01 and V-02 are structurally compatible — the Severity field feeds the
Penalty column, which the Selection Audit reproduces verbatim. The combination closes the
audit chain from entry-level magnitude assignment through table display through verification
artifact to AMEND-A citation. Hypothesis: 290/290.

---

You are running `corps-scan`. Work through five named roles in strict sequence.
**ROLE 2, ROLE 3, ROLE 3.5, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and typed
hypothesis claim.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN self-label
in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25; C-18: C-NN IDs as primary keys; C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED)

[ ] C-12 -- HARD BOUNDARY front-loaded.
    STATUS: CONFIRMED.

[ ] C-13 -- C-12 precedes this pre-check.
    STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification.

[ ] C-38+C-41+C-45 -- typed hypothesis claim (3-field contract, field type annotations).
    Produced below this pre-check.
    STATUS: CONFIRMED.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema; DARK SIGNALS with C-42 STATE_ENUM +
    5-level Severity Scale at header; Severity field per entry.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27+C-43+C-46+C-48 -- weight-scoring table; Penalty [label:string, magnitude:0-4]
    sourced from ROLE 2 Severity fields; Inertia Cost column (C-48).
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-47 -- SELECTION AUDIT reproduces winner + runner-up rows; arithmetic trace;
    AMEND-A cites section and Severity traceability.
    STATUS: SCHEDULED — SELECTION AUDIT / ROLE 3.5.

[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS with STATE_ENUM; Severity per entry; Penalty
    column cites label + magnitude; AMEND-A cites label + verdict + delta + audit citation.
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 3.5 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40+C-44 -- amend options; AMEND-A carries verdict + delta + audit citation
    + Severity trace; post-write cites 10+ criteria (C-34 essential).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 satisfied. Compound bundles: "C-38+C-41+C-45",
"C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43+C-46+C-48", "C-36+C-37+C-39+C-42",
"C-01+C-02+C-03+C-04", "C-16+C-30+C-40+C-44".

**Typed Hypothesis Claim** `(C-38+C-41+C-45; C-25: self-labeled)`

```
TYPED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38; C-41: 3-field labeled contract; C-45: machine-readable type annotations; C-25)
(Downstream: ROLE 2 Severity Scale feeds ROLE 3 Penalty column;
 ROLE 3.5 Selection Audit cited by AMEND-A for C-47)

PREDICTED-MODE:        [type: pivot-mode-enum — directory | concept | service | domain]
                       value: [fill one]

STRUCTURAL-PREDICTION: [type: structural-evidence-string — one sentence]
                       value: "[one sentence]"

FALSIFICATION-SIGNAL:  [type: absence-signal-enum — NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE
                        | NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
                       value: [the label that, if ABSENT, overturns this claim]

CONFIDENCE:            [type: confidence-enum — high | medium | low]
                       value: [fill one]

BASIS:                 [type: string — one sentence of repo evidence]
                       value: "[evidence]"
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25; C-26: C-11+C-21; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: ROLE 1 complete. Signal Schema and DARK SIGNALS. No deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary.

The 5-level Severity Scale is declared at the DARK SIGNALS section header. Severity field values
are sourced directly into the ROLE 3 Penalty column magnitude. The ROLE 3.5 Selection Audit will
cite these values.

#### Signal Schema `(C-26: C-11+C-21; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11+C-21 satisfier; C-22: criterion purpose in header; C-25: self-labeled; C-33

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence]                |

Rules: minimum 2 rows; YAML name exact match; named roles only; cap 8 rows.
Exec office inference: [schema row or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42+C-46 source; C-25; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals, Hypothesis Relations, Severity Scores
## C-36: structured negative evidence; C-39: Hypothesis Relation per entry
## C-42: STATE_ENUM declared below; C-46 source: Severity field per entry
## C-25: self-labeled; C-37 downstream: labels in ROLE 3 Penalty column

C-42 STATE_ENUM:
  YES -- CONFIRMED / YES -- OVERTURNED / NO -- corroborates-alternative([mode]) / NO -- neutral

5-LEVEL SEVERITY SCALE (C-46 source):
  4 — ABSENT / 3 — PARTIAL-MAJOR / 2 — PARTIAL-MINOR / 1 — TRACE / 0 — PRESENT

NO-SERVICE-MANIFEST:
  Looked for: docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens service mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4 — scale value; one phrase derivation note]

NO-DDD-LANGUAGE:
  Looked for: bounded context names, aggregate roots, domain events in naming
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens concept mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4 — scale value; one phrase]

NO-DOMAIN-BOUNDARY:
  Looked for: explicit subdomain directories, business capability groupings
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens domain mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4 — scale value; one phrase]

NO-WORKSPACE-GROUPING:
  Looked for: monorepo workspace config grouping packages by area
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens directory mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4 — scale value; one phrase]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [GATE label]
  That entry's STATE_ENUM:  [YES -- CONFIRMED | YES -- OVERTURNED]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25; C-23+C-27+C-43+C-46+C-48; C-31: DELIBERATE PHASE)`

Prerequisite: ROLE 2 complete. No YAML. Penalty magnitudes sourced from ROLE 2 Severity fields.
Write winner and runner-up rows with full precision — ROLE 3.5 will reproduce them verbatim.

```
## Pivot Mode Deliberation — {{date}}
## C-25; C-43: weight table; C-46: Penalty [label:string, magnitude:0-4] from ROLE 2 Severity;
## C-48: Inertia Cost [cost:string] — orthogonal organizational cost

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  STATE_ENUM outcome:       [YES -- CONFIRMED | YES -- OVERTURNED]

Evidence Weight Table:
(Penalty magnitude copied from ROLE 2 Severity field for each label)

| Mode      | Evidence For                     | DARK SIGNALS Penalty [label: magnitude] | Inertia Cost [cost]              | Base | Penalty | Net | Verdict |
|-----------|----------------------------------|-----------------------------------------|----------------------------------|------|---------|-----|---------|
| directory | [schema rows]                    | NO-WORKSPACE-GROUPING: [Severity]       | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |
| concept   | [schema rows]                    | NO-DDD-LANGUAGE: [Severity]             | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |
| service   | [schema rows]                    | NO-SERVICE-MANIFEST: [Severity]         | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |
| domain    | [schema rows]                    | NO-DOMAIN-BOUNDARY: [Severity]          | [reconstruction cost if changed] | [N]  | [N]     | [N] | [s/p/w] |

Magnitude sourcing: each Penalty value above copied from ROLE 2 Severity field.

Selected pivot mode: [highest Net Score]
Net Score delta: [winner Net] - [runner-up Net] = [N]
```

DELIBERATE PHASE / ROLE 3 complete. SELECTION AUDIT / ROLE 3.5 may now begin.

---

### ROLE 3.5 — SELECTION AUDIT / ARITHMETIC VERIFIER
`(C-25; C-47 satisfier; C-31: SELECTION AUDIT)`

Prerequisite: ROLE 3 complete. No YAML. No new analysis. Reproduce winner and runner-up rows
verbatim. State arithmetic. Note Severity traceability.

```
## Selection Audit — {{date}}
## C-47 satisfier: verification artifact for AMEND-A verifiability citation
## C-25: self-labeled
## AMEND-A cites: "(confirm from SELECTION AUDIT; magnitude traceable to ROLE 2 Severity fields)"

Winner row (from ROLE 3 — verbatim):
  Mode: [winner] | Evidence For: [...] | Penalty: [label]: [Severity value] |
  Inertia Cost: [...] | Base=[N], Penalty=[N], Net=[N], Verdict=[s/p/w]

Runner-up row (from ROLE 3 — verbatim):
  Mode: [runner-up] | Evidence For: [...] | Penalty: [label]: [Severity value] |
  Inertia Cost: [...] | Base=[N], Penalty=[N], Net=[N], Verdict=[s/p/w]

Arithmetic trace:
  Winner:    Base=[N] − Penalty=[N] = Net=[N]
  Runner-up: Base=[N] − Penalty=[N] = Net=[N]
  Delta:     [winner Net] − [runner-up Net] = [N]

Severity traceability:
  [winner label] Penalty=[N] sourced from ROLE 2 DARK SIGNALS [label] Severity=[N].
  [runner-up label] Penalty=[N] sourced from ROLE 2 DARK SIGNALS [label] Severity=[N].
  Confirm: ROLE 2 Severity fields match Penalty values above — no recalculation needed.
```

SELECTION AUDIT / ROLE 3.5 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. AMEND-A cites Selection Audit by name and notes
Severity traceability.

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Net Score delta: [N] (confirm from SELECTION AUDIT; magnitude traceable to ROLE 2
> Severity fields). Hypothesis STATE_ENUM: [YES -- CONFIRMED | YES -- OVERTURNED] —
> FALSIFICATION-SIGNAL [label]. C-05 ACKNOWLEDGED in GATE: no .roles/ content here."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N]
# hypothesis-outcome: [YES -- CONFIRMED | YES -- OVERTURNED]
# falsification-signal: [GATE label]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24): auto-added per team by corps-build.
      teams:
        - name: "[YAML name — matches ROLE 2 schema 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 "Repo signal" — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25; C-14+C-30; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — DRAFT+FINALIZE PHASE / ROLE 4
(C-19; C-30: 10+ criteria; C-33; C-34: C-02 essential)

[ ] Team names match ROLE 2 schema "YAML name (C-02)"                       STATUS: [CONFIRMED/FAIL]
[ ] 2+ named roles per team, no generics (C-04)                              STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                               STATUS: [CONFIRMED/FAIL]
[ ] Group container present (C-03)                                           STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content (C-05)                                          STATUS: [CONFIRMED/FAIL]
[ ] Penalty [label:string, magnitude:0-4] in ROLE 3 (C-46)                  STATUS: [CONFIRMED/FAIL]
[ ] Inertia Cost column orthogonal to evidence (C-48)                        STATUS: [CONFIRMED/FAIL]
[ ] All sections C-NN self-labeled (C-25)                                    STATUS: [CONFIRMED/FAIL]
[ ] C-42 STATE_ENUM + 5-level Severity Scale at DARK SIGNALS header          STATUS: [CONFIRMED/FAIL]
[ ] SELECTION AUDIT: winner + runner-up rows + arithmetic + Severity trace   STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + verdict + delta + Selection Audit citation + Severity   STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML; this block = post-YAML.
C-30: C-02, C-04, C-07, C-03, C-05, C-46, C-48, C-25, C-42+Severity, SELECTION AUDIT, AMEND-A — 11 items.
C-34: essential-tier C-02 present.
```

#### Amend Options `(C-25; C-08+C-16; C-37+C-40+C-44+C-47)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):     [YES -- CONFIRMED | YES -- OVERTURNED — [label] absent]
  Net Score arithmetic (C-44):   [selected] Net=[N] vs [runner-up] Net=[N]; delta=[N]
                                  (confirm from SELECTION AUDIT above; magnitude traceable
                                   to ROLE 2 Severity fields — independently verifiable) (C-47)
  DARK SIGNALS basis (C-37):     [label] Severity=[N] → Penalty=-[N]; eliminated [runner-up]
  Debt if skipped:               corps-build, corps-pr, corps-committee, corps-rob inherit
                                  misaligned clustering; audit chain available for review.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: Name propagates into corps-rob and corps-committee verbatim.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocates in misaligned groups degrade corps-committee coherence.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R13 V-04). C-45: typed hypothesis contract. C-46: Penalty
> [label:string, magnitude:0-4] with magnitude sourced from ROLE 2 Severity fields.
> C-47: SELECTION AUDIT section created; AMEND-A cites by name with Severity traceability.
> C-48: Inertia Cost column orthogonal to evidence structure. Draft-only."

---

## V-05 — Combination: Magnitude Derivation + Selection Audit + Pipeline Debt

**Axis**: Full combination of V-01 (magnitude derivation protocol), V-02 (Selection Audit
phase), and V-03 (Pipeline Debt as cost dimension). The 5-level Severity Scale defines
per-entry magnitude (C-46). The SELECTION AUDIT phase reproduces winner and runner-up rows
with Severity traceability (C-47). Pipeline Debt [stages:string] is the orthogonal cost
dimension in the deliberation table (C-48) rather than Inertia Cost. AMEND-A cites the
Selection Audit section, the Severity traceability, and the Pipeline Debt consequence.
The deliberation table carries 7 columns: Evidence For / DARK SIGNALS Penalty [label:string,
magnitude:0-4] / Pipeline Debt [stages:string] / Base / Penalty / Net / Verdict.
**Hypothesis**: All three single-axis variations are structurally compatible. The 5-level scale
feeds the Penalty column; the Penalty column is reproduced in the Selection Audit; the audit
makes the arithmetic verifiable; the Pipeline Debt column is orthogonal to both the Penalty
column and the audit chain. The combination produces the densest criterion coverage per output
section of any R13 variation. Hypothesis: 290/290.

---

You are running `corps-scan`. Work through five named roles in strict sequence.
**ROLE 2, ROLE 3, ROLE 3.5, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and typed
hypothesis claim.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN self-label
in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

Prerequisite for all other roles. Complete the pre-check AND the typed hypothesis claim before
any scanning, deliberation, or YAML work begins.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25; C-18: C-NN IDs as primary keys; C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED)

[ ] C-12 -- HARD BOUNDARY front-loaded.
    STATUS: CONFIRMED.

[ ] C-13 -- C-12 precedes this pre-check.
    STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files.
    STATUS: ACKNOWLEDGED — essential failure; golden disqualification if violated.

[ ] C-38+C-41+C-45 -- typed hypothesis claim (3-field contract, machine-readable type
    annotations on each field). Produced below.
    STATUS: CONFIRMED.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN columns; DARK SIGNALS with C-42
    STATE_ENUM + 5-level Severity Scale at header; Severity field per entry.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27+C-43+C-46+C-48 -- weight-scoring table; Penalty [label:string, magnitude:0-4]
    sourced from ROLE 2 Severity; Pipeline Debt [stages:string] as C-48 cost dimension.
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-47 -- SELECTION AUDIT reproduces winner + runner-up rows; arithmetic + Severity trace;
    AMEND-A cites section by name.
    STATUS: SCHEDULED — SELECTION AUDIT / ROLE 3.5.

[ ] C-36+C-37+C-39+C-42 -- DARK SIGNALS with STATE_ENUM; Severity per entry; Penalty column
    cites label + Severity magnitude; AMEND-A cites label + verdict + delta + audit + debt.
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 3.5 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40+C-44 -- amend options; AMEND-A carries verdict + delta + audit citation
    + Severity trace + Pipeline Debt; post-write 10+ criteria (C-34 essential).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 satisfied. Compound bundles: "C-38+C-41+C-45",
"C-11+C-21+C-22+C-25+C-26", "C-23+C-27+C-43+C-46+C-48", "C-36+C-37+C-39+C-42",
"C-01+C-02+C-03+C-04", "C-16+C-30+C-40+C-44".

**Typed Hypothesis Claim** `(C-38+C-41+C-45; C-25: self-labeled)`

```
TYPED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38; C-41: 3-field labeled contract; C-45: machine-readable type annotations; C-25)
(Downstream: ROLE 2 5-level Severity Scale → ROLE 3 Penalty column → ROLE 3.5 Selection Audit
 + Severity trace → ROLE 4 AMEND-A with audit citation + Pipeline Debt consequence)

PREDICTED-MODE:        [type: pivot-mode-enum — directory | concept | service | domain]
                       value: [fill one]

STRUCTURAL-PREDICTION: [type: structural-evidence-string — one sentence]
                       value: "[one sentence]"

FALSIFICATION-SIGNAL:  [type: absence-signal-enum — NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE
                        | NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING]
                       value: [the label that, if ABSENT, overturns this claim]

CONFIDENCE:            [type: confidence-enum — high | medium | low]
                       value: [fill one]

BASIS:                 [type: string — one sentence of repo evidence]
                       value: "[evidence]"
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25; C-26: C-11+C-21; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: ROLE 1 complete. Signal Schema and DARK SIGNALS. No deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary.

The 5-level Severity Scale declared at the DARK SIGNALS header provides the magnitude values
the ROLE 3 Penalty column will source. ROLE 3.5 will reproduce winner/runner-up rows and cite
specific Severity field values for traceability.

#### Signal Schema `(C-26: C-11+C-21; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11+C-21 satisfier; C-22: criterion purpose in header; C-25; C-33: pre-YAML

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence]                |

Rules: min 2 rows; exact YAML name match; named roles only; cap 8 rows.
Exec office inference: [schema term or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39+C-42+C-46 source; C-25; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals, Hypothesis Relations, Severity Scores
## C-36+C-39: negative evidence + hypothesis relation; C-42: STATE_ENUM
## C-46 source: 5-level Severity Scale declared here; Severity per entry feeds ROLE 3 Penalty
## C-25: self-labeled

C-42 STATE_ENUM:
  YES -- CONFIRMED / YES -- OVERTURNED / NO -- corroborates-alternative([mode]) / NO -- neutral

5-LEVEL SEVERITY SCALE (C-46 source):
  4 — ABSENT / 3 — PARTIAL-MAJOR / 2 — PARTIAL-MINOR / 1 — TRACE / 0 — PRESENT

NO-SERVICE-MANIFEST:
  Looked for: docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens service mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4; one phrase: e.g., "4 — ABSENT"]

NO-DDD-LANGUAGE:
  Looked for: bounded context names, aggregate roots, domain events in naming
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens concept mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4; one phrase]

NO-DOMAIN-BOUNDARY:
  Looked for: explicit subdomain directories, business capability groupings
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens domain mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4; one phrase]

NO-WORKSPACE-GROUPING:
  Looked for: monorepo workspace config grouping packages by area
  Detected:   [PRESENT | ABSENT | PARTIAL-MAJOR | PARTIAL-MINOR | TRACE]
  Modes affected: rules out / weakens directory mode
  Hypothesis Relation: [STATE_ENUM]
  Severity:   [0-4; one phrase]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [GATE label]
  That entry's STATE_ENUM:  [YES -- CONFIRMED | YES -- OVERTURNED]
  Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25; C-23+C-27+C-43+C-46+C-48; C-31: DELIBERATE PHASE)`

Prerequisite: ROLE 2 complete. No YAML.

Produce the 7-column weight-scoring table:
- DARK SIGNALS Penalty [label:string, magnitude:0-4] — magnitude from ROLE 2 Severity fields (C-46)
- Pipeline Debt [stages:string] — corps-* stages disrupted if mode selected and changed (C-48)
Write winner and runner-up rows with full precision for ROLE 3.5 reproduction.

```
## Pivot Mode Deliberation — {{date}}
## C-25; C-43: weight-scoring table; C-46: Penalty [label:string, magnitude:0-4] from Severity;
## C-48: Pipeline Debt [stages:string] — orthogonal organizational cost (not evidence signal)

Hypothesis closure:
  PREDICTED-MODE (GATE):    [mode]
  FALSIFICATION-SIGNAL:     [label]
  STATE_ENUM outcome:       [YES -- CONFIRMED | YES -- OVERTURNED]

Evidence Weight Table:
(Penalty magnitude: copied from ROLE 2 Severity field for each label.
 Pipeline Debt: corps-build / corps-pr / corps-committee / corps-rob — name disrupted stages only)

| Mode      | Evidence For                     | DARK SIGNALS Penalty [label: magnitude] | Pipeline Debt [stages]                  | Base | Penalty | Net | Verdict |
|-----------|----------------------------------|-----------------------------------------|-----------------------------------------|------|---------|-----|---------|
| directory | [schema rows]                    | NO-WORKSPACE-GROUPING: [Severity]       | [disrupted stages or "none"]            | [N]  | [N]     | [N] | [s/p/w] |
| concept   | [schema rows]                    | NO-DDD-LANGUAGE: [Severity]             | [disrupted stages or "none"]            | [N]  | [N]     | [N] | [s/p/w] |
| service   | [schema rows]                    | NO-SERVICE-MANIFEST: [Severity]         | [disrupted stages or "none"]            | [N]  | [N]     | [N] | [s/p/w] |
| domain    | [schema rows]                    | NO-DOMAIN-BOUNDARY: [Severity]          | [disrupted stages or "none"]            | [N]  | [N]     | [N] | [s/p/w] |

Selected pivot mode: [highest Net Score]
Net Score delta: [winner Net] - [runner-up Net] = [N]
Pipeline Debt for [winner]: [stages named or "none"]
```

DELIBERATE PHASE / ROLE 3 complete. SELECTION AUDIT / ROLE 3.5 may now begin.

---

### ROLE 3.5 — SELECTION AUDIT / ARITHMETIC VERIFIER
`(C-25; C-47 satisfier; C-31: SELECTION AUDIT)`

Prerequisite: ROLE 3 complete. No new analysis. Reproduce winner and runner-up rows verbatim.
Arithmetic trace. Severity traceability note.

```
## Selection Audit — {{date}}
## C-47 satisfier: dedicated verification artifact
## C-25: self-labeled
## AMEND-A cites: "(confirm from SELECTION AUDIT; magnitude traceable to ROLE 2 Severity fields)"

Winner row (ROLE 3 — verbatim):
  Mode: [winner] | Evidence For: [...] | DARK SIGNALS Penalty: [label]: [Severity value] |
  Pipeline Debt: [...] | Base=[N], Penalty=[N], Net=[N], Verdict=[s/p/w]

Runner-up row (ROLE 3 — verbatim):
  Mode: [runner-up] | Evidence For: [...] | DARK SIGNALS Penalty: [label]: [Severity value] |
  Pipeline Debt: [...] | Base=[N], Penalty=[N], Net=[N], Verdict=[s/p/w]

Arithmetic trace:
  Winner:    Base=[N] − Penalty=[N] = Net=[N]
  Runner-up: Base=[N] − Penalty=[N] = Net=[N]
  Delta:     [winner Net] − [runner-up Net] = [N]

Severity traceability:
  [winner label] Severity=[N] sourced from ROLE 2 DARK SIGNALS — no recalculation needed.
  [runner-up label] Severity=[N] sourced from ROLE 2 DARK SIGNALS — no recalculation needed.
  Confirm: ROLE 2 Severity fields match Penalty values above.
```

SELECTION AUDIT / ROLE 3.5 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. AMEND-A cites Selection Audit by name, notes Severity
traceability, and names Pipeline Debt consequence of switching.

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Net Score delta: [N] (confirm from SELECTION AUDIT; magnitude traceable to ROLE 2
> Severity fields). Hypothesis: [YES -- CONFIRMED | YES -- OVERTURNED] — [label].
> Pipeline Debt for selected mode: [stages or 'none'].
> C-05 ACKNOWLEDGED: no .roles/ content here."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N]
# hypothesis-outcome: [YES -- CONFIRMED | YES -- OVERTURNED]
# falsification-signal: [GATE label]
# pipeline-debt: [stages disrupted if mode changes, or "none"]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24): auto-added per team by corps-build.
      teams:
        - name: "[YAML name — matches ROLE 2 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 Repo signal — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25; C-14+C-30; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — DRAFT+FINALIZE PHASE / ROLE 4
(C-19; C-30: 10+ criteria; C-33; C-34: C-02 essential)

[ ] Team names match ROLE 2 "YAML name (C-02)"                              STATUS: [CONFIRMED/FAIL]
[ ] 2+ named roles per team, no generics (C-04)                             STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                              STATUS: [CONFIRMED/FAIL]
[ ] Group container present (C-03)                                          STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content (C-05)                                         STATUS: [CONFIRMED/FAIL]
[ ] Penalty [label:string, magnitude:0-4] from Severity fields (C-46)       STATUS: [CONFIRMED/FAIL]
[ ] Pipeline Debt [stages:string] column present (C-48)                     STATUS: [CONFIRMED/FAIL]
[ ] All sections C-NN self-labeled (C-25)                                   STATUS: [CONFIRMED/FAIL]
[ ] C-42 STATE_ENUM + 5-level Severity Scale at DARK SIGNALS header         STATUS: [CONFIRMED/FAIL]
[ ] SELECTION AUDIT: rows + arithmetic + Severity traceability (C-47)       STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: label + verdict + delta + audit citation + Severity + Pipeline Debt STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at group and team level in YAML (C-24)                 STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML; this block = post-YAML.
C-30: C-02, C-04, C-07, C-03, C-05, C-46, C-48, C-25, C-42+Severity, C-47, AMEND-A, C-24 — 12 items.
C-34: essential-tier C-02 present.
```

#### Amend Options `(C-25; C-08+C-16; C-37+C-40+C-44+C-47)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40):     [YES -- CONFIRMED | YES -- OVERTURNED — [label] absent]
  Net Score arithmetic (C-44):   [selected] Net=[N] vs [runner-up] Net=[N]; delta=[N]
                                  (confirm from SELECTION AUDIT above; magnitude traceable
                                   to ROLE 2 Severity fields — independently verifiable) (C-47)
  DARK SIGNALS basis (C-37):     [label] Severity=[N] → Penalty=-[N]; eliminated [runner-up]
  Pipeline Debt if switched:     Changing to [alternative mode] disrupts [stages] — those
                                  stages must re-run after pivot change.
  Debt if skipped:               corps-build inherits misaligned clustering; [stages] Pipeline
                                  Debt accumulates until corps-rob surfaces the misalignment.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: Name propagates into corps-rob governance and corps-committee verbatim.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Debt if skipped: Misaligned groups degrade corps-committee review coherence across cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R13 V-05). C-45: typed hypothesis contract with field type annotations.
> C-46: Penalty [label:string, magnitude:0-4] — magnitude sourced from 5-level Severity Scale
> per DARK SIGNALS entry. C-47: SELECTION AUDIT section with arithmetic trace and Severity
> traceability; AMEND-A cites by name. C-48: Pipeline Debt [stages:string] orthogonal to
> evidence structure — names corps-* stages disrupted per mode. Draft-only."
