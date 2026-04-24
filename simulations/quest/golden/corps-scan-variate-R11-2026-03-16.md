---
skill: quest-variate
skill_target: corps-scan
round: 11
date: 2026-03-16
rubric_version: 10
---

# Variate R11 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v10 rubric (250 pts,
40 criteria). R10's V-01 scored 235/235 under v9; v10 adds C-38, C-39, C-40 as new required
criteria. All prior invariants through C-37 remain structural requirements. C-38, C-39, and
C-40 are now invariants — ALL R11 variations must satisfy them. The variation axes govern HOW
each variation implements the hypothesis lifecycle, not whether.

R10 axes already covered (not re-explored in R11):
- Role sequence — hypothesis-first (C-38 via GATE pivot hypothesis block)
- Phrasing register — detective/narrative ("What I found. What I didn't find.")
- Output format — DARK SIGNALS as structured evidence table (named columns)
- Inertia framing — REPO GRAIN vocabulary, with-grain vs against-grain
- Combination — hypothesis-first + DARK SIGNALS table + phase output footers

R9 axes already covered (not re-explored):
- Negative space inventory (DARK SIGNALS as block-list following Signal Schema)
- Phase output contracts at phase footers
- Downstream consumer annotations on YAML elements
- Criterion cluster naming as primary pre-check key
- Combination: negative space inventory + downstream consumer annotations

R11 explores four new single-axis variation axes and one combination. All five variations treat
C-38, C-39, and C-40 as structurally required. The variation axes concern the representation
and ordering of the hypothesis lifecycle artifacts, not their presence.

1. **Structured hypothesis claim (IF/PREDICT/FALSIFIED-BY triplet)** — C-38 is expressed
   as a three-field structured claim: PREDICTED-MODE / STRUCTURAL-PREDICTION / FALSIFICATION-
   SIGNAL (the named DARK SIGNALS label that, if ABSENT, overturns the hypothesis). Each C-39
   DARK SIGNALS entry maps its hypothesis relation to whether it IS the named FALSIFICATION-
   SIGNAL ("IS-FALSIFICATION-SIGNAL — [CONFIRMED|OVERTURNED]") or a corroborating alternative.
   C-40 AMEND-A reports the FALSIFICATION-SIGNAL by name with its outcome. The structured claim
   format makes the traceability chain machine-readable at each link.
   Hypothesis: 250/250 — the IF/PREDICT/FALSIFIED-BY triplet makes the hypothesis explicit as
   a testable contract; DARK SIGNALS entries become typed evidence against named falsification
   conditions rather than generic absences.

2. **Weighted evidence table in deliberation** — C-27 (tri-part triad) is implemented as a
   weight-scoring table with columns: Mode | Evidence For (schema rows) | DARK SIGNALS Penalty
   (label + magnitude) | Base Score | Penalty | Net Score | Verdict. The mode with the highest
   Net Score is selected. C-37 is satisfied by the DARK SIGNALS label appearing in the Penalty
   column. C-40 in AMEND-A cites the Net Score differential that drove the selection and the
   hypothesis outcome. The table format makes evidence weighting explicit and auditable.
   Hypothesis: 250/250 — quantified evidence scoring provides a concrete selection rationale
   that is harder to produce without complete criterion coverage.

3. **Amend-as-verdict ordering (hypothesis outcome leads)** — C-40 is elevated to the FIRST
   field of every amend option ("Hypothesis verdict: CONFIRMED | OVERTURNED — [label]"). The
   standard C-16 debt framing becomes the second field. A closing "Chain audit" annotation
   below all amend options traces the full C-38 → C-39 → C-40 lifecycle in one place.
   Hypothesis: 250/250 — leading with hypothesis outcome makes the causal chain visible at
   the decision layer; debt framing as secondary frames it as consequence of hypothesis result.

4. **Numbered scan walk protocol** — The SCAN phase is structured as five numbered walk steps,
   each scoped to a specific artifact class and each yielding a typed output (Signal Schema row
   OR a DARK SIGNALS entry with C-39 hypothesis relation field). Step 5 emits the hypothesis
   outcome summary after all entries are produced. The numbered walk makes the SCAN-to-DARK-
   SIGNALS pipeline deterministic and its artifact coverage explicit.
   Hypothesis: 250/250 — numbered steps constrain model behavior at each scan point; the
   hypothesis outcome summary at Step 5 produces a natural C-38→C-39 handoff artifact.

Combined:
5. **Structured claim + weight table + amend-as-verdict** — Combines axes 1, 2, and 3. The
   GATE hypothesis is a three-field structured claim with FALSIFICATION-SIGNAL named. DARK
   SIGNALS entries carry IS-FALSIFICATION-SIGNAL relation (C-39). The deliberation is a weight-
   scoring table citing DARK SIGNALS labels in the Penalty column (C-37). Each amend option
   leads with hypothesis verdict (C-40), with chain audit closing the lifecycle.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Hypothesis formalism — structured IF/PREDICT/FALSIFIED-BY claim; DARK SIGNALS entries typed as IS-FALSIFICATION-SIGNAL | V-01 |
| Evidence weighting — deliberation as weight-scoring table; Net Score drives selection; C-37 in Penalty column | V-02 |
| Amend ordering — hypothesis verdict as first field; C-16 debt secondary; chain audit block below amend options | V-03 |
| Scan walk protocol — five numbered walk steps; each step scoped + typed; hypothesis outcome at Step 5 | V-04 |
| Combination — structured claim + weight table + amend-as-verdict (axes 1+2+3) | V-05 |

---

## V-01 — Hypothesis Formalism: Structured IF/PREDICT/FALSIFIED-BY Claim

**Axis**: Hypothesis formalism (how C-38 is expressed and how C-39 links to it)
**Hypothesis**: R10 V-01 declares the pivot hypothesis as free-form prose — "Initial hypothesis:
[mode]. Basis: [sentence]. Confidence: [level]. Hypothesis-refuting signal: [label]." The same
content can be expressed as a structured three-field claim: PREDICTED-MODE (the hypothesis),
STRUCTURAL-PREDICTION (the expected observable repo structure), and FALSIFICATION-SIGNAL (the
named DARK SIGNALS label that, if ABSENT, overturns the claim). This structured form makes the
claim a contract rather than a comment: each DARK SIGNALS entry (C-39) explicitly answers
whether it IS the FALSIFICATION-SIGNAL and what that means for the hypothesis. AMEND-A (C-40)
names the FALSIFICATION-SIGNAL outcome as its primary basis. The three-field form tightens all
three new criteria simultaneously: C-38 (structured gate claim), C-39 (typed entry mapping),
C-40 (named signal outcome in amend). Hypothesis: 250/250.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and structured
hypothesis claim.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate — all roles blocked until complete; C-31: GATE PHASE; C-25: self-labeled)`

Prerequisite for all other roles. Complete the pre-check AND produce the structured hypothesis
claim before any repo scanning, inventory, deliberation, or YAML work begins.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state vocabulary on every item)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — precedes all scanning, deliberation, and YAML.

[ ] C-13 -- self-referential confirmation:
    C-12 draft-only statement precedes all output — confirmed above.
    STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files:
    No .roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit possible.
    Violation consequence: output fails golden threshold regardless of composite score.

[ ] C-38 -- structured hypothesis claim:
    Produced in this GATE PHASE / ROLE 1 output, before any repo scanning begins.
    Form: PREDICTED-MODE / STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL triplet.
    STATUS: CONFIRMED — produced below, before SCAN PHASE / ROLE 2 is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema, C-NN column headers:
    SCAN PHASE / ROLE 2 produces Signal Schema and DARK SIGNALS section.
    DARK SIGNALS entries carry C-39 Hypothesis Relation field typed as:
      IS-FALSIFICATION-SIGNAL — [CONFIRMED|OVERTURNED], corroborates-alternative, or neutral.
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part Evidence For/Against/Assessment:
    DELIBERATE PHASE / ROLE 3 opens with hypothesis closure citing FALSIFICATION-SIGNAL.
    Evidence Against entries cite DARK SIGNALS labels by name (C-37).
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39 -- DARK SIGNALS section with hypothesis relation; deliberation + amend cite:
    SCAN PHASE: DARK SIGNALS entries carry C-39 IS-FALSIFICATION-SIGNAL field.
    DELIBERATE PHASE: Evidence Against cites DARK SIGNALS labels by name (C-37).
    DRAFT PHASE: AMEND-A cites FALSIFICATION-SIGNAL label + outcome (C-40).
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with group structure, schema-traced teams, named roles:
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40 -- debt-framed amend options with hypothesis verdict; 4+-criterion post-write:
    AMEND-A carries hypothesis verdict (C-40): FALSIFICATION-SIGNAL [CONFIRMED|OVERTURNED].
    Post-write block cites 4+ criteria including one essential-tier C-NN (C-34).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names C-05, C-38, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-36+C-37+C-39,
C-01+C-02+C-03+C-04, C-16+C-30+C-40 as skill requirements.
C-17: all SCHEDULED items are forward commitments to named future roles.
C-18: C-NN IDs (including compound bundles) are primary keys throughout.
C-28: CONFIRMED / SCHEDULED / ACKNOWLEDGED on every item.
C-29: compound bundles on single items — "C-11+C-21+C-22+C-25+C-26", "C-23+C-27",
"C-36+C-37+C-39", "C-01+C-02+C-03+C-04", "C-16+C-30+C-40".
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 STATUS: ACKNOWLEDGED — essential failure named with consequence.

**Structured Hypothesis Claim** `(C-38 satisfier; C-25: self-labeled; produced before SCAN PHASE)`

```
STRUCTURED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38: hypothesis declared before any repo scanning begins)
(C-25: section self-labeled)
(Downstream: DARK SIGNALS entries in ROLE 2 map to FALSIFICATION-SIGNAL per C-39;
 AMEND-A in ROLE 4 cites FALSIFICATION-SIGNAL outcome per C-40)

PREDICTED-MODE:       [directory | concept | service | domain]

STRUCTURAL-PREDICTION: [one sentence describing the observable repo structure
                        this mode predicts — e.g., "packages grouped by functional
                        area in workspace config, with matching top-level directory
                        clusters"]

FALSIFICATION-SIGNAL: [the DARK SIGNALS label — NO-SERVICE-MANIFEST |
                       NO-DDD-LANGUAGE | NO-DOMAIN-BOUNDARY |
                       NO-WORKSPACE-GROUPING — that, if ABSENT, overturns this claim]

CONFIDENCE:           [high | medium | low]
BASIS:                [one sentence: first-pass read of top-level names, manifest
                       presence, or domain vocabulary that grounds the prediction]
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE PHASE / ROLE 1 pre-check and structured hypothesis claim complete. Produce
Signal Schema and DARK SIGNALS section. No pivot deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests (`docker-compose.yml`, `k8s/`, Helm charts). Workspace configs (npm workspaces,
Cargo workspace, `go.work`). Domain vocabulary (bounded context names, aggregate roots, domain
events in directory/module names).

Each DARK SIGNALS entry carries a C-39 Hypothesis Relation field. Use the structured claim
from GATE: if this entry IS the FALSIFICATION-SIGNAL named in the claim, mark it as
"IS-FALSIFICATION-SIGNAL — [CONFIRMED if PRESENT/PARTIAL | OVERTURNED if ABSENT]". All other
entries are "corroborates-alternative" (ABSENT signal supports an alternative mode) or
"neutral" (no bearing on the stated hypothesis).

#### Signal Schema `(C-26: C-11+C-21 satisfier — precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: criterion purpose declared in header before schema rows
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

#### DARK SIGNALS `(C-36+C-39 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals, Ruled-Out Modes, and Hypothesis Relations
## C-36: structured negative evidence with per-entry mode impact
## C-39: each entry carries Hypothesis Relation typed to GATE structured claim
## C-25: section self-labeled; C-37 downstream: Evidence Against in ROLE 3 cites labels

NO-SERVICE-MANIFEST:
  Looked for:          docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis Relation: [IS-FALSIFICATION-SIGNAL — CONFIRMED | IS-FALSIFICATION-SIGNAL — OVERTURNED
                        | corroborates-alternative ([mode]) | neutral]

NO-DDD-LANGUAGE:
  Looked for:          bounded context names, aggregate roots, domain events in dir/module names
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)
  Hypothesis Relation: [IS-FALSIFICATION-SIGNAL — CONFIRMED | IS-FALSIFICATION-SIGNAL — OVERTURNED
                        | corroborates-alternative ([mode]) | neutral]

NO-DOMAIN-BOUNDARY:
  Looked for:          explicit subdomain directories, business capability groupings
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)
  Hypothesis Relation: [IS-FALSIFICATION-SIGNAL — CONFIRMED | IS-FALSIFICATION-SIGNAL — OVERTURNED
                        | corroborates-alternative ([mode]) | neutral]

NO-WORKSPACE-GROUPING:
  Looked for:          monorepo workspace config grouping packages by area
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)
  Hypothesis Relation: [IS-FALSIFICATION-SIGNAL — CONFIRMED | IS-FALSIFICATION-SIGNAL — OVERTURNED
                        | corroborates-alternative ([mode]) | neutral]

Hypothesis outcome:
  FALSIFICATION-SIGNAL from GATE: [GATE label]
  That signal was: [PRESENT — hypothesis CONFIRMED | ABSENT — hypothesis OVERTURNED |
                    PARTIAL — hypothesis WEAKENED]
  Ruled-out modes: [list any modes whose primary signals were ABSENT]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 Signal Schema and DARK SIGNALS complete. No YAML.

Open with hypothesis closure: state whether the GATE structured claim was CONFIRMED, WEAKENED,
or OVERTURNED, naming the FALSIFICATION-SIGNAL and its detected state. Then enumerate all four
pivot modes with tri-part triad. Evidence Against entries must cite DARK SIGNALS labels by name
(C-37 satisfier). Select one mode. Cite a specific ROLE 2 schema row by "Repo signal" value.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-37: Evidence Against entries cite DARK SIGNALS labels by name

Hypothesis closure:
  PREDICTED-MODE (from GATE):    [mode]
  FALSIFICATION-SIGNAL (GATE):   [label]
  Signal detected:               [PRESENT | ABSENT | PARTIAL]
  Hypothesis outcome:            [CONFIRMED | WEAKENED | OVERTURNED]
  Implication:                   [no mode change needed | pivot reconsideration → [mode]]

directory mode:
  Evidence For:    [ROLE 2 schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [DARK SIGNALS: NO-WORKSPACE-GROUPING — [ABSENT/PARTIAL]: workspace
                    grouping absent, directory boundaries inferred not declared]
  Assessment:      [strong / possible / weak — one sentence]

concept mode:
  Evidence For:    [ROLE 2 schema rows where Signal type = domain/concept]
  Evidence Against: [DARK SIGNALS: NO-DDD-LANGUAGE — [ABSENT/PARTIAL]: no bounded context
                    names; concept clustering lacks named foundations]
  Assessment:      [strong / possible / weak — one sentence]

service mode:
  Evidence For:    [ROLE 2 schema rows where Signal type = service]
  Evidence Against: [DARK SIGNALS: NO-SERVICE-MANIFEST — [ABSENT/PARTIAL]: no service
                    manifests; service boundaries unverifiable]
  Assessment:      [strong / possible / weak — one sentence]

domain mode:
  Evidence For:    [ROLE 2 schema rows with bounded-context or subdomain signals]
  Evidence Against: [DARK SIGNALS: NO-DOMAIN-BOUNDARY — [ABSENT/PARTIAL]: no subdomain
                    directories; domain grouping would be imposed, not read]
  Assessment:      [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific ROLE 2 Signal Schema "Repo signal" value that
  most strongly supports selection; name the DARK SIGNALS label that eliminated the runner-up]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. No new scanning or deliberation. Draft YAML from
ROLE 2 schema and ROLE 3 pivot selection, then verify and provide amend options.

AMEND-A must (a) cite the DARK SIGNALS FALSIFICATION-SIGNAL label as basis for the alternative
mode recommendation (C-37 amend satisfier), and (b) carry the hypothesis verdict — whether
that signal was CONFIRMED or OVERTURNED — as the first amend field (C-40 satisfier).

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Hypothesis [CONFIRMED | WEAKENED | OVERTURNED] — FALSIFICATION-SIGNAL [label]
> was [PRESENT|ABSENT|PARTIAL]. C-05 ACKNOWLEDGED in GATE: no .roles/ content here."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# falsification-signal: [GATE label] — [CONFIRMED | WEAKENED | OVERTURNED]
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

[ ] All team names match ROLE 2 schema "YAML name (C-02)"              STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles (no generics) (C-04)                 STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                 STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                        STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                           STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                    STATUS: [CONFIRMED/FAIL]
[ ] Tri-part pivot deliberation in ROLE 3 (C-27)                       STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                          STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS with C-39 IS-FALSIFICATION-SIGNAL field (C-36+C-39)  STATUS: [CONFIRMED/FAIL]
[ ] Evidence Against cites labels; AMEND-A cites label+verdict (C-37+C-40) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this header = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36+C-39, C-37+C-40 — 10 items.
C-34: essential-tier C-02 present alongside 9 aspirational criteria.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37: AMEND-A cites label; C-40: verdict present)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40): [CONFIRMED — current mode supported | OVERTURNED —
    FALSIFICATION-SIGNAL [label] was ABSENT; hypothesis does not hold]
  Current mode: [ROLE 3 selected mode]
  DARK SIGNALS basis (C-37): [label] was [ABSENT/PARTIAL] — [mode] ruled out by
    structured claim FALSIFICATION-SIGNAL; alternative mode [X] warranted.
  Debt if skipped: corps-build, corps-pr, corps-committee, corps-rob inherit misaligned
    clustering; DARK SIGNALS FALSIFICATION-SIGNAL documented but hypothesis consequence
    ignored downstream.
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

> "corps-scan complete (R11 V-01). Structured hypothesis claim: PREDICTED-MODE /
> STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL triplet in GATE (C-38). DARK SIGNALS entries
> carry IS-FALSIFICATION-SIGNAL typed relation (C-39). AMEND-A leads with hypothesis verdict
> citing FALSIFICATION-SIGNAL outcome (C-40). Full chain: GATE claim → DARK SIGNALS typing →
> amend verdict. All C-01 through C-40 requirements met. Draft-only."

---

## V-02 — Output Format: Weighted Evidence Table in Deliberation

**Axis**: Output format of the deliberation phase (C-27 implementation)
**Hypothesis**: The tri-part Evidence For / Evidence Against / Assessment structure produces
qualitative verdicts (strong/possible/weak) without making the selection rationale explicit.
A weighted evidence table replaces the prose triad: columns are Mode | Evidence For (schema
rows cited) | DARK SIGNALS Penalty (label + penalty weight) | Base Score | Penalty | Net Score
| Verdict. The model assigns integer scores; the mode with the highest Net Score is selected.
C-37 is satisfied by the DARK SIGNALS label appearing in the Penalty column. C-40 AMEND-A
cites the Net Score differential and hypothesis verdict. The table format has two structural
advantages: (a) DARK SIGNALS labels must appear explicitly as column values to produce the
table, making C-37 non-bypassable; (b) a numeric Net Score gives AMEND-A a concrete delta to
report for C-40. Hypothesis: 250/250 — quantified evidence scoring constrains selection
reasoning to explicit label citations and numeric outputs.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and hypothesis.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate — all roles blocked until complete; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED on every item)

[ ] C-12 -- "HARD BOUNDARY" is the first substantive line of this output.
    STATUS: CONFIRMED.

[ ] C-13 -- C-12 precedes this pre-check.
    STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files, role file content, or role-creation instructions.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification regardless
    of composite score.

[ ] C-38 -- pivot hypothesis declared in GATE before any scanning:
    Produced below this pre-check. Format: initial pivot mode prediction + confidence +
    named DARK SIGNALS label whose absence would overturn it.
    STATUS: CONFIRMED — produced in GATE PHASE / ROLE 1 before SCAN PHASE is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN column headers; DARK SIGNALS section
    follows schema with C-39 Hypothesis Relation field on each entry.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation as weighted evidence table:
    Columns: Mode | Evidence For | DARK SIGNALS Penalty (C-37 satisfier) | Base | Penalty |
    Net Score | Verdict. Evidence Against = Penalty column with label citation.
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39 -- DARK SIGNALS section with C-39 hypothesis relation; Penalty column in
    ROLE 3 table cites DARK SIGNALS labels (C-37); AMEND-A cites label + hypothesis (C-40).
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml draft with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30+C-40 -- debt-framed amend options; AMEND-A carries Net Score delta + hypothesis
    verdict (C-40); post-write cites 10 criteria including one essential (C-34).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names all required outputs.
C-17: all SCHEDULED items name the delivering role.
C-18: C-NN IDs as primary keys.
C-28: three-state vocabulary on every item.
C-29: compound bundles — "C-11+C-21+C-22+C-25+C-26", "C-36+C-37+C-39", "C-16+C-30+C-40".
C-35: C-05 ACKNOWLEDGED with consequence named.

**Pivot Hypothesis** `(C-38 satisfier; C-25: self-labeled; precedes SCAN PHASE)`

```
PIVOT HYPOTHESIS — GATE PHASE / ROLE 1
(C-38: declared before scanning; C-25: section self-labeled)
(Downstream: DARK SIGNALS entries carry C-39 Hypothesis Relation;
 ROLE 3 weight table Penalty column cites labels per C-37;
 AMEND-A carries Net Score delta + hypothesis verdict per C-40)

Initial hypothesis:  [directory | concept | service | domain] mode
Basis:               [one sentence: first-pass read — top-level names, manifest presence,
                     domain vocabulary in naming conventions]
Confidence:          [high | medium | low]
Overturn condition:  [DARK SIGNALS label — NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE |
                     NO-DOMAIN-BOUNDARY | NO-WORKSPACE-GROUPING] found ABSENT overturns
                     this hypothesis and requires deliberation to select an alternative mode.
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests (`docker-compose.yml`, `k8s/`, Helm charts). Workspace configs (npm workspaces,
Cargo workspace, `go.work`). Domain vocabulary (bounded context names, aggregate roots, domain
events). No deliberation, no YAML.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN column headers)
## C-22: criterion purpose declared in header; C-25: self-labeled; C-33: pre-YAML bracket

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

- Minimum 2 rows. PLACEHOLDER row if fewer signals detected.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only — no generics, no "TBD".
- "Detection evidence (C-09)": one sentence of repo evidence per row.

Exec office inference: [term suggesting exec title, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals and Hypothesis Relations
## C-36: structured negative evidence with per-entry mode impact
## C-39: Hypothesis Relation field on each entry links to GATE hypothesis
## C-25: self-labeled; C-37 downstream: labels cited in ROLE 3 Penalty column

NO-SERVICE-MANIFEST:
  Looked for:          docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis Relation: [CONFIRMED — present, supports hypothesis |
                        OVERTURNED — absent, falsifies hypothesis |
                        corroborates-alternative ([mode]) | neutral]

NO-DDD-LANGUAGE:
  Looked for:          bounded context names, aggregate roots, domain events in naming
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-DOMAIN-BOUNDARY:
  Looked for:          explicit subdomain directories, business capability groupings
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-WORKSPACE-GROUPING:
  Looked for:          monorepo workspace config grouping packages by area
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

Hypothesis summary: [CONFIRMED — no OVERTURNED entries | WEAKENED — [label] PARTIAL |
                     OVERTURNED — [label] ABSENT; hypothesis does not hold]
Ruled-out modes:    [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 Signal Schema and DARK SIGNALS complete. No YAML.

Produce the weighted evidence table. The Penalty column satisfies C-37: each DARK SIGNALS
label must appear as a Penalty column value. Open with hypothesis closure before the table.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes YAML; C-27: tri-part → weight table
## C-37: DARK SIGNALS labels appear in Penalty column for each mode

Hypothesis closure:
  GATE hypothesis: [mode from ROLE 1]
  DARK SIGNALS outcome: [CONFIRMED | WEAKENED by [LABEL] | OVERTURNED by [LABEL]]
  Consequence: [proceed with hypothesis mode | deliberation may select different mode]

Evidence Weight Table:
(Scoring guide: Base Score 1-5 from Evidence For count + signal-type strength;
 Penalty 0-4 deducted per ABSENT/PARTIAL DARK SIGNALS entry for the mode;
 Net = Base - Penalty; select mode with highest Net)

| Mode      | Evidence For (schema rows)         | DARK SIGNALS Penalty               | Base | Penalty | Net | Verdict  |
|-----------|------------------------------------|------------------------------------|------|---------|-----|----------|
| directory | [Repo signal values from schema]   | NO-WORKSPACE-GROUPING: -[0-4]      | [N]  | [N]     | [N] | [s/p/w]  |
| concept   | [Repo signal values from schema]   | NO-DDD-LANGUAGE: -[0-4]            | [N]  | [N]     | [N] | [s/p/w]  |
| service   | [Repo signal values from schema]   | NO-SERVICE-MANIFEST: -[0-4]        | [N]  | [N]     | [N] | [s/p/w]  |
| domain    | [Repo signal values from schema]   | NO-DOMAIN-BOUNDARY: -[0-4]         | [N]  | [N]     | [N] | [s/p/w]  |

Scoring notes:
  Penalty magnitude guide: ABSENT = -4 (mode ruled out), PARTIAL = -2 (mode weakened),
    PRESENT = 0 (no deduction). Apply to the mode whose signals were absent.
  Verdict: strong (Net >= 4), possible (Net 2-3), weak (Net 0-1).

Selected pivot mode: [mode with highest Net Score]
Rationale: [one sentence: Net Score [N] from ROLE 2 schema row "[Repo signal]";
  DARK SIGNALS [label] penalty of -[N] eliminated [runner-up mode]]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Draft YAML from ROLE 2 schema and ROLE 3 pivot selection. AMEND-A must (a) cite the DARK
SIGNALS label from the Penalty column as basis (C-37), and (b) carry the Net Score delta
and hypothesis verdict as the hypothesis outcome field (C-40).

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N]
# hypothesis-outcome: [CONFIRMED | WEAKENED | OVERTURNED]
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
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 "Repo signal" value]
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
POST-WRITE VERIFICATION — DRAFT+FINALIZE PHASE / ROLE 4
(C-30: 10 criteria; C-33: post-YAML bracket; C-34: essential C-02 present)

[ ] Team names match ROLE 2 schema "YAML name (C-02)"                  STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                  STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                 STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                        STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                           STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                    STATUS: [CONFIRMED/FAIL]
[ ] Weight table with DARK SIGNALS Penalty column in ROLE 3 (C-27+C-37) STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                          STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS with C-39 Hypothesis Relation field (C-36+C-39)       STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A cites label + Net Score delta + hypothesis verdict (C-37+C-40) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this header = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27+C-37, C-25, C-36+C-39, C-37+C-40 — 10 items.
C-34: essential C-02 present alongside 9 aspirational.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37+C-40 satisfier)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40): [CONFIRMED — Net Score supports hypothesis mode |
    OVERTURNED — [label] Penalty [-N] collapsed hypothesis mode Net Score to [N];
    alternative mode [X] has Net Score [M]]
  Current: [ROLE 3 mode] — Net Score [N]
  Alternative: [mode] — Net Score [M]; delta = [M-N]
  DARK SIGNALS basis (C-37): [label] was ABSENT; Penalty [-4] applied; mode eliminated.
  Debt if skipped: corps-build, corps-pr, corps-committee, corps-rob inherit misaligned
    clustering; weight table evidence documented but Net Score consequence ignored.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: propagates verbatim into corps-rob and corps-committee templates.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocate context fragmented across misaligned groups.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R11 V-02). Weighted evidence table in DELIBERATE PHASE: columns Mode |
> Evidence For | DARK SIGNALS Penalty | Base | Penalty | Net Score | Verdict. DARK SIGNALS
> labels appear as typed Penalty column values (C-37). AMEND-A carries Net Score delta +
> hypothesis verdict (C-40). DARK SIGNALS entries carry C-39 Hypothesis Relation field.
> All C-01 through C-40 requirements met. Draft-only."

---

## V-03 — Amend Ordering: Hypothesis Outcome as Primary Field

**Axis**: Amend option ordering and framing (C-40 prominence)
**Hypothesis**: In R10, C-40 is satisfied by including the hypothesis outcome somewhere in
AMEND-A — typically after the "Current:" and "Basis:" fields. The hypothesis verdict is
structurally secondary to the debt framing. Elevating C-40 to the FIRST field of every amend
option ("Hypothesis verdict: CONFIRMED | OVERTURNED") reorders the logical chain: the amend
is first justified by hypothesis outcome, then grounded in DARK SIGNALS evidence, then warned
by debt. A closing "Chain audit" annotation below all three amend options traces the full
C-38 → C-39 → C-40 lifecycle in one auditable block. This does not change which criteria are
satisfied — it changes which criterion is stated first and adds an explicit audit trace.
Hypothesis: 250/250 — leading with hypothesis outcome makes the lifecycle chain the primary
decision driver; the chain audit block provides a single readable lifecycle trace for scoring.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and hypothesis.**

**Universal labeling rule (C-25)**: Every section must carry a C-NN self-label. No unlabeled
sections.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: self-labeled; C-18: C-NN IDs primary keys; C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED)

[ ] C-12 -- "HARD BOUNDARY" is first substantive line. STATUS: CONFIRMED.
[ ] C-13 -- C-12 precedes this pre-check. STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files, role file content, or role-creation instructions.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification.

[ ] C-38 -- pivot hypothesis declared in GATE before scanning:
    Produced below, before SCAN PHASE / ROLE 2 is unblocked.
    STATUS: CONFIRMED.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema; DARK SIGNALS with C-39 Hypothesis Relation.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad; Evidence Against cites DARK SIGNALS
    labels by name (C-37 satisfier).
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39 -- DARK SIGNALS section with hypothesis relation; labels cited in
    Evidence Against (ROLE 3) and AMEND-A hypothesis verdict (ROLE 4, C-40).
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml draft. STATUS: SCHEDULED — DRAFT+FINALIZE / ROLE 4.

[ ] C-16+C-30+C-40 -- amend options: hypothesis verdict leads each option (C-40 first field);
    post-write cites 10 criteria including one essential (C-34).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 all satisfied per standard pattern above.

**Pivot Hypothesis** `(C-38 satisfier; C-25: self-labeled; precedes SCAN PHASE)`

```
PIVOT HYPOTHESIS — GATE PHASE / ROLE 1
(C-38: precedes all scanning; C-25: self-labeled)
(Downstream: C-39 Hypothesis Relation in DARK SIGNALS; C-40 verdict leads amend options)

Initial hypothesis:  [directory | concept | service | domain] mode
Basis:               [one sentence: first-pass read of repo structure]
Confidence:          [high | medium | low]
Overturn signal:     [DARK SIGNALS label] — if ABSENT in SCAN, hypothesis overturned
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary. No deliberation, no YAML.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11+C-21 satisfier; C-22: criterion purpose in header; C-25: self-labeled

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

- Minimum 2 rows. PLACEHOLDER if fewer signals detected.
- "YAML name (C-02)": exact string used in YAML teams[].name.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence per row.

Exec office inference: [term or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}}
## C-36: negative evidence with per-entry mode impact; C-39: Hypothesis Relation on each entry
## C-25: self-labeled; C-37 downstream: labels cited in ROLE 3 Evidence Against + ROLE 4 AMEND-A

NO-SERVICE-MANIFEST:
  Looked for:          docker-compose.yml, k8s/, Helm charts, service ports
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out service (ABSENT) / weakens service (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-DDD-LANGUAGE:
  Looked for:          bounded contexts, aggregate roots, domain events in naming
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out concept (ABSENT) / weakens concept (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-DOMAIN-BOUNDARY:
  Looked for:          subdomain directories, business capability groupings
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out domain (ABSENT) / weakens domain (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-WORKSPACE-GROUPING:
  Looked for:          workspace config grouping packages by area
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out directory (ABSENT) / weakens directory (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

Hypothesis outcome: [CONFIRMED | WEAKENED by [label] | OVERTURNED by [label]]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN complete. No YAML. Enumerate all four modes with tri-part triad.
Evidence Against cites DARK SIGNALS labels by name (C-37). Select one mode.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: precedes YAML; C-27: tri-part triad; C-37: labels cited

Hypothesis closure:
  GATE hypothesis: [mode] — outcome from DARK SIGNALS: [CONFIRMED | WEAKENED | OVERTURNED]

directory mode:
  Evidence For:    [schema rows by "Repo signal" value]
  Evidence Against: [DARK SIGNALS: NO-WORKSPACE-GROUPING — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

concept mode:
  Evidence For:    [schema rows where Signal type = concept/domain]
  Evidence Against: [DARK SIGNALS: NO-DDD-LANGUAGE — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

service mode:
  Evidence For:    [schema rows where Signal type = service]
  Evidence Against: [DARK SIGNALS: NO-SERVICE-MANIFEST — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

domain mode:
  Evidence For:    [schema rows with subdomain/bounded-context signals]
  Evidence Against: [DARK SIGNALS: NO-DOMAIN-BOUNDARY — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [one sentence citing "Repo signal" value; name DARK SIGNALS label eliminating runner-up]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Draft YAML from ROLE 2 schema and ROLE 3 selection. In amend options, hypothesis verdict
(C-40) is the FIRST field of EVERY amend option — before current state, before debt framing.
A Chain Audit block below all three options traces the full C-38→C-39→C-40 lifecycle.

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# hypothesis-outcome: [CONFIRMED | WEAKENED | OVERTURNED]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team receives one Inertia Advocate from corps-build.
      teams:
        - name: "[YAML name — exact match to ROLE 2 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 "Repo signal" value]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — DRAFT+FINALIZE PHASE / ROLE 4
(C-30: 10 criteria; C-33: post-YAML bracket; C-34: essential C-02 present)

[ ] Team names match ROLE 2 schema "YAML name (C-02)"                   STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                   STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                          STATUS: [CONFIRMED/FAIL]
[ ] At least one group container (C-03)                                 STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                            STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                     STATUS: [CONFIRMED/FAIL]
[ ] Tri-part deliberation in ROLE 3 with DARK SIGNALS citations (C-27+C-37) STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                           STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS with C-39 Hypothesis Relation field (C-36+C-39)        STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: hypothesis verdict first field + label cited (C-37+C-40)   STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this header = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27+C-37, C-25, C-36+C-39, C-37+C-40 — 10 items.
C-34: essential C-02 alongside 9 aspirational.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-40 verdict leads each option)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40) [FIRST FIELD]:
    [CONFIRMED — current mode supported by evidence; switching is optional |
     OVERTURNED — DARK SIGNALS: [label] was ABSENT; hypothesis does not hold;
     alternative mode [X] is recommended]
  Current: [ROLE 3 mode]
  DARK SIGNALS basis (C-37): [label] — [ABSENT/PARTIAL] — [mode] [eliminated|weakened].
  Debt if skipped: corps-build, corps-pr, corps-committee, corps-rob inherit misaligned
    clustering; hypothesis overturn evidence documented but consequence ignored.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Hypothesis verdict (C-40) [FIRST FIELD]:
    [CONFIRMED — hypothesis mode unchanged; exec name is independent of mode |
     OVERTURNED — mode may change; exec name should be re-evaluated against new mode]
  Current: "[name]" | Source: [ROLE 2 inference or "no signal"]
  Debt if skipped: Name propagates verbatim into corps-rob and corps-committee templates.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Hypothesis verdict (C-40) [FIRST FIELD]:
    [CONFIRMED — group structure follows hypothesis mode topology |
     OVERTURNED — mode shift implies group structure revision]
  Current: [n] groups | Principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocate context fragmented across misaligned groups.
  Command: /corps-scan --groups "[description]"

Chain Audit (C-38 → C-39 → C-40):
  C-38 — GATE hypothesis: [mode] declared before scanning.
  C-39 — DARK SIGNALS: [label] Hypothesis Relation = [CONFIRMED|OVERTURNED|neutral]; ...
  C-40 — AMEND-A verdict: [CONFIRMED|OVERTURNED] — hypothesis lifecycle closed.
```

> "corps-scan complete (R11 V-03). Amend-as-verdict ordering: hypothesis verdict (C-40) is
> the first field of every amend option, with debt framing (C-16) as secondary. Chain Audit
> block below amend options traces C-38 (GATE hypothesis) → C-39 (DARK SIGNALS relation) →
> C-40 (amend verdict) as a single auditable lifecycle trace. All C-01 through C-40
> requirements met. Draft-only."

---

## V-04 — Lifecycle Emphasis: Numbered Scan Walk Protocol

**Axis**: Lifecycle emphasis — SCAN phase internal structure
**Hypothesis**: The SCAN phase in R9/R10 is an open-ended walk instruction: "Walk: top-level
directories, src/, services/, packages/, apps/, modules/. Service manifests. Workspace
configs. Domain vocabulary." The model is free to produce Signal Schema rows in any order and
may undergenerate DARK SIGNALS entries. A numbered walk protocol fixes five explicit scan
steps, each scoped to a typed artifact class, each yielding either a Signal Schema row or a
typed DARK SIGNALS entry. Step 5 aggregates the hypothesis outcome from the prior steps.
The numbered protocol has two structural effects: (a) each DARK SIGNALS entry type is
guaranteed a scan step, making C-39 coverage deterministic; (b) the hypothesis outcome
emerges from step outputs rather than being asserted post-hoc. Hypothesis: 250/250 — numbered
steps constrain SCAN output to typed artifacts and make DARK SIGNALS coverage explicit.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and hypothesis.**

**Universal labeling rule (C-25)**: Every section must carry a C-NN self-label.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: self-labeled; C-18: C-NN IDs primary keys; C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED)

[ ] C-12 -- "HARD BOUNDARY" is first substantive line. STATUS: CONFIRMED.
[ ] C-13 -- C-12 precedes this pre-check. STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification.

[ ] C-38 -- pivot hypothesis declared in GATE before numbered walk begins:
    Produced below. Step-by-step scan in ROLE 2 tests this hypothesis entry by entry.
    STATUS: CONFIRMED — produced in this GATE PHASE before SCAN PHASE is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema and DARK SIGNALS produced by numbered walk
    protocol (Steps 1-5 in SCAN PHASE / ROLE 2). C-39 Hypothesis Relation on each DARK
    SIGNALS entry. Step 5 emits hypothesis outcome.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad; Evidence Against cites DARK SIGNALS
    labels (C-37 satisfier).
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39 -- DARK SIGNALS from walk steps with C-39 field; labels cited in ROLE 3
    and AMEND-A carries hypothesis verdict (C-40).
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml draft. STATUS: SCHEDULED — DRAFT+FINALIZE / ROLE 4.

[ ] C-16+C-30+C-40 -- debt-framed amend options with C-40 hypothesis verdict; post-write
    cites 10 criteria including one essential (C-34).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 all satisfied per standard pattern.

**Pivot Hypothesis** `(C-38 satisfier; C-25: self-labeled; precedes numbered walk in ROLE 2)`

```
PIVOT HYPOTHESIS — GATE PHASE / ROLE 1
(C-38: declared before any walk step begins; C-25: self-labeled)
(Downstream: Walk Steps 1-5 test this hypothesis; DARK SIGNALS C-39 entries report relation;
 Step 5 emits outcome; AMEND-A reports hypothesis verdict per C-40)

Initial hypothesis:  [directory | concept | service | domain] mode
Basis:               [one sentence: first-pass read — top-level names, manifest presence,
                     domain vocabulary]
Confidence:          [high | medium | low]
Overturn condition:  Walk Step [2|3|4|5] finding [DARK SIGNALS label] ABSENT would
                     overturn this hypothesis.
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST (Numbered Walk Protocol)
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Execute five numbered walk steps. Each step is scoped to a specific artifact class and yields
a typed output: either one or more Signal Schema rows, or a DARK SIGNALS entry with C-39
Hypothesis Relation field, or both. After all five steps, consolidate Signal Schema and DARK
SIGNALS into their standard sections. No deliberation, no YAML.

```
## SCAN PHASE — Numbered Walk Protocol — {{date}}
## C-25: self-labeled; C-31: SCAN PHASE; C-26: C-11+C-21 satisfier; C-33: pre-YAML bracket
## Walk protocol: 5 steps; each step scoped + typed; hypothesis outcome at Step 5

WALK STEP 1 — Top-Level Directory Structure
  Artifacts: top-level directory names, src/, apps/, packages/, modules/ clusters
  Looking for: named area clusters, functional groupings, explicit team-area directories
  Signal type produced: directory / concept (depending on naming vocabulary)
  Output: [Signal Schema row(s) if area clusters detected | "no directory signals detected"]
  Contribution to hypothesis: [supports | neutral | undermines] [GATE hypothesis mode]

WALK STEP 2 — Service Manifests
  Artifacts: docker-compose.yml, k8s/, Helm charts, service port definitions
  Looking for: independently deployable service boundaries with named service identities
  Signal type produced: service signals OR DARK SIGNALS entry
  Output:
    Signal Schema row(s): [if service manifests found]
    DARK SIGNALS — NO-SERVICE-MANIFEST:
      Detected:            [PRESENT | ABSENT | PARTIAL]
      Modes affected:      rules out service (ABSENT) / weakens service (PARTIAL)
      Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

WALK STEP 3 — Workspace Configuration
  Artifacts: package.json workspaces, Cargo.toml workspace, go.work, nx.json
  Looking for: explicit area-based grouping of packages in monorepo config
  Signal type produced: directory signals OR DARK SIGNALS entry
  Output:
    Signal Schema row(s): [if workspace grouping signals found]
    DARK SIGNALS — NO-WORKSPACE-GROUPING:
      Detected:            [PRESENT | ABSENT | PARTIAL]
      Modes affected:      rules out directory (ABSENT) / weakens directory (PARTIAL)
      Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

WALK STEP 4 — Domain Language Inventory
  Artifacts: directory names, module identifiers, package names, class/file names in src/
  Looking for: bounded context names, aggregate root terms, domain event vocabulary,
               business capability language, subdomain terminology
  Signal type produced: concept / domain signals OR two DARK SIGNALS entries
  Output:
    Signal Schema row(s): [if domain vocabulary detected in naming]
    DARK SIGNALS — NO-DDD-LANGUAGE:
      Detected:            [PRESENT | ABSENT | PARTIAL]
      Modes affected:      rules out concept (ABSENT) / weakens concept (PARTIAL)
      Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]
    DARK SIGNALS — NO-DOMAIN-BOUNDARY:
      Detected:            [PRESENT | ABSENT | PARTIAL]
      Modes affected:      rules out domain (ABSENT) / weakens domain (PARTIAL)
      Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

WALK STEP 5 — Exec Office Signal + Hypothesis Outcome Summary
  Artifacts: top-level README, root config files, monorepo tooling owner references
  Looking for: exec title, org name, root-level leadership terms
  Output:
    Exec office inference: [term or "no signal — placeholder"]
    Hypothesis outcome from Steps 1-4:
      GATE hypothesis: [mode]
      Step results: [list which DARK SIGNALS entries had Hypothesis Relation = OVERTURNED, CONFIRMED]
      Outcome: [CONFIRMED — no overturn findings | WEAKENED — [label] PARTIAL |
                OVERTURNED — [label] ABSENT]
```

#### Signal Schema (Consolidated from Walk Steps) `(C-26: C-11+C-21 satisfier; C-22: self-labeled)`

```
## Signal Schema — {{date}} — Consolidated from Walk Steps 1-5
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN column headers)
## C-22: criterion purpose in header; C-25: self-labeled; C-33: pre-YAML bracket

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

- Minimum 2 rows. PLACEHOLDER row if fewer signals detected.
- "YAML name (C-02)": exact string; must match YAML teams[].name.
- "Proposed roles (C-04)": named roles only — no generics.
- "Detection evidence (C-09)": one sentence per row.

Walk step source per row: [Step N — artifact class]
Exec office inference: [from Step 5 or "no signal — placeholder"]
```

#### DARK SIGNALS (Consolidated from Walk Steps) `(C-36+C-39 satisfier; C-25: self-labeled)`

```
## DARK SIGNALS — {{date}} — Consolidated from Walk Steps 2, 3, 4
## C-36: negative evidence with per-entry mode impact; C-39: Hypothesis Relation per entry
## C-25: self-labeled; C-37 downstream: labels cited in ROLE 3 Evidence Against + ROLE 4 AMEND-A
## Walk source: Step 2 → NO-SERVICE-MANIFEST; Step 3 → NO-WORKSPACE-GROUPING;
##              Step 4 → NO-DDD-LANGUAGE + NO-DOMAIN-BOUNDARY

NO-SERVICE-MANIFEST  [from Walk Step 2]:
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out service (ABSENT) / weakens service (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-DDD-LANGUAGE  [from Walk Step 4]:
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out concept (ABSENT) / weakens concept (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-DOMAIN-BOUNDARY  [from Walk Step 4]:
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out domain (ABSENT) / weakens domain (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

NO-WORKSPACE-GROUPING  [from Walk Step 3]:
  Detected:            [PRESENT | ABSENT | PARTIAL]
  Modes affected:      rules out directory (ABSENT) / weakens directory (PARTIAL)
  Hypothesis Relation: [CONFIRMED | OVERTURNED | corroborates-alternative ([mode]) | neutral]

Hypothesis outcome (from Step 5): [CONFIRMED | WEAKENED by [label] | OVERTURNED by [label]]
Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN complete. No YAML. Enumerate four modes with tri-part triad. Evidence
Against cites DARK SIGNALS labels from consolidated section by name (C-37). Select one mode.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: precedes YAML; C-27: tri-part triad
## C-37: Evidence Against cites DARK SIGNALS labels from Walk Step consolidation

Hypothesis closure:
  GATE hypothesis: [mode] — Walk Step 5 outcome: [CONFIRMED | WEAKENED | OVERTURNED]

directory mode:
  Evidence For:    [schema rows from Walk Step 1/3 by "Repo signal" value]
  Evidence Against: [DARK SIGNALS: NO-WORKSPACE-GROUPING — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

concept mode:
  Evidence For:    [schema rows from Walk Step 4 where Signal type = concept]
  Evidence Against: [DARK SIGNALS: NO-DDD-LANGUAGE — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

service mode:
  Evidence For:    [schema rows from Walk Step 2 where Signal type = service]
  Evidence Against: [DARK SIGNALS: NO-SERVICE-MANIFEST — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

domain mode:
  Evidence For:    [schema rows from Walk Step 4 where Signal type = domain]
  Evidence Against: [DARK SIGNALS: NO-DOMAIN-BOUNDARY — [ABSENT/PARTIAL]]
  Assessment:      [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [one sentence citing "Repo signal" value; name DARK SIGNALS label eliminating runner-up]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Draft YAML from ROLE 2 schema and ROLE 3 selection. AMEND-A cites DARK SIGNALS label (C-37)
and carries hypothesis verdict (C-40).

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# walk-protocol: 5 steps; hypothesis-outcome: [CONFIRMED | WEAKENED | OVERTURNED]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 Walk Step 5 exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team receives one Inertia Advocate from corps-build.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 "Repo signal" — Walk Step N]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — DRAFT+FINALIZE PHASE / ROLE 4
(C-30: 10 criteria; C-33: post-YAML bracket; C-34: essential C-02 present)

[ ] Team names match ROLE 2 schema "YAML name (C-02)"                    STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles (C-04)                                  STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                            STATUS: [CONFIRMED/FAIL]
[ ] At least one group container (C-03)                                   STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                              STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                       STATUS: [CONFIRMED/FAIL]
[ ] Tri-part deliberation with DARK SIGNALS citations in ROLE 3 (C-27+C-37) STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                             STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS from walk steps with C-39 Hypothesis Relation (C-36+C-39) STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A cites walk-step label + hypothesis verdict (C-37+C-40)        STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this header = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27+C-37, C-25, C-36+C-39, C-37+C-40 — 10 items.
C-34: essential C-02 alongside 9 aspirational.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37 cites walk-step label; C-40 verdict)`

```
AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | Walk step basis: [Step N]
  Hypothesis verdict (C-40): [CONFIRMED | OVERTURNED — Walk Step [N] produced
    DARK SIGNALS: [label] ABSENT; hypothesis [mode] does not hold]
  DARK SIGNALS basis (C-37): [label] — Walk Step [N] — [ABSENT/PARTIAL] — [mode] ruled out.
  Debt if skipped: walk protocol documented [label] absence but mode consequence ignored;
    corps-build through corps-rob inherit misaligned clustering from undiscarded hypothesis.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: Walk Step 5 [exec inference or "no signal"]
  Debt if skipped: Name propagates verbatim into corps-rob and corps-committee templates.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocate context fragmented across misaligned groups.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R11 V-04). Numbered scan walk protocol: 5 steps scoped to artifact
> classes (top-level dirs, service manifests, workspace config, domain language, exec signal).
> Each DARK SIGNALS entry produced by its designated walk step and carries C-39 Hypothesis
> Relation. Step 5 emits hypothesis outcome summary. AMEND-A cites walk-step label +
> hypothesis verdict (C-37+C-40). All C-01 through C-40 requirements met. Draft-only."

---

## V-05 — Combination: Structured Claim + Weight Table + Amend-as-Verdict

**Axis**: Combination — V-01 (structured hypothesis claim) + V-02 (weighted evidence table)
+ V-03 (amend-as-verdict ordering)
**Hypothesis**: The three axes target three separate points in the hypothesis lifecycle:
V-01 formalizes C-38 (structured claim with FALSIFICATION-SIGNAL), V-02 makes C-37 non-
bypassable (DARK SIGNALS labels must appear as typed Penalty column values), and V-03
elevates C-40 to primary position in amend options with a chain audit. Together they produce
the tightest possible hypothesis lifecycle implementation: (a) the GATE claim names the
FALSIFICATION-SIGNAL explicitly; (b) each DARK SIGNALS entry types itself against the
FALSIFICATION-SIGNAL (C-39 IS-FALSIFICATION-SIGNAL field); (c) the weight table forces
DARK SIGNALS label citations into Penalty cells (C-37); (d) each amend option leads with
hypothesis verdict (C-40); (e) the chain audit traces C-38→C-39→C-40 in one block.
Hypothesis: 250/250 — combination of the three strongest C-38/C-39/C-40 implementations
produces maximum hypothesis lifecycle traceability.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and structured
hypothesis claim.**

**Universal labeling rule (C-25)**: Every section must carry a C-NN self-label. No unlabeled
sections.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: self-labeled; C-18: C-NN IDs primary keys; C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED)

[ ] C-12 -- "HARD BOUNDARY" is first substantive line. STATUS: CONFIRMED.
[ ] C-13 -- C-12 precedes this pre-check. STATUS: CONFIRMED.

[ ] C-05 -- no .roles/ files anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification.

[ ] C-38 -- structured hypothesis claim (IF/PREDICT/FALSIFIED-BY triplet):
    Produced below. PREDICTED-MODE / STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL.
    STATUS: CONFIRMED — produced in GATE PHASE before SCAN PHASE is unblocked.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema; DARK SIGNALS with C-39 IS-FALSIFICATION-SIGNAL
    field typed to the GATE structured claim's FALSIFICATION-SIGNAL.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation as weighted evidence table:
    Penalty column carries DARK SIGNALS label citations (C-37). Mode with highest Net Score
    selected. Hypothesis closure opens table using GATE FALSIFICATION-SIGNAL outcome.
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37+C-39 -- DARK SIGNALS with IS-FALSIFICATION-SIGNAL field (C-36+C-39); Penalty
    column in weight table cites labels (C-37); AMEND-A verdict leads (C-40).
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-01+C-02+C-03+C-04 -- org.yaml draft. STATUS: SCHEDULED — DRAFT+FINALIZE / ROLE 4.

[ ] C-16+C-30+C-40 -- amend options: hypothesis verdict first field, chain audit below all
    three options; post-write cites 10 criteria including one essential (C-34).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 satisfied per standard pattern.

**Structured Hypothesis Claim** `(C-38 satisfier; C-25: self-labeled; precedes SCAN PHASE)`

```
STRUCTURED HYPOTHESIS CLAIM — GATE PHASE / ROLE 1
(C-38: structured claim before scanning; C-25: self-labeled)
(V-05 chain: C-38 claim → C-39 IS-FALSIFICATION-SIGNAL field → C-37 Penalty column →
 C-40 verdict leads amend + chain audit)

PREDICTED-MODE:        [directory | concept | service | domain]

STRUCTURAL-PREDICTION: [one sentence: the observable repo structure this mode predicts,
                        e.g., "top-level directories map directly to team areas with
                        workspace config confirming the grouping"]

FALSIFICATION-SIGNAL:  [NO-SERVICE-MANIFEST | NO-DDD-LANGUAGE | NO-DOMAIN-BOUNDARY |
                        NO-WORKSPACE-GROUPING] — if this signal is ABSENT in SCAN,
                        PREDICTED-MODE hypothesis is OVERTURNED.

CONFIDENCE:            [high | medium | low]
BASIS:                 [one sentence: first-pass repo read grounding the prediction]
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary. No deliberation, no YAML.

Each DARK SIGNALS entry carries C-39 IS-FALSIFICATION-SIGNAL field keyed to the GATE
structured claim. If this entry IS the named FALSIFICATION-SIGNAL: mark as
"IS-FALSIFICATION-SIGNAL — CONFIRMED" (if PRESENT/PARTIAL) or
"IS-FALSIFICATION-SIGNAL — OVERTURNED" (if ABSENT). All other entries: "corroborates-
alternative ([mode])" or "neutral".

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11+C-21 satisfier; C-22: criterion purpose in header; C-25: self-labeled

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

- Minimum 2 rows. PLACEHOLDER row if fewer signals detected.
- "YAML name (C-02)": exact string used in YAML teams[].name.
- "Proposed roles (C-04)": named roles only — no generics.
- "Detection evidence (C-09)": one sentence per row.

Exec office inference: [term or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-36+C-39 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS — {{date}}
## C-36: negative evidence with per-entry mode impact
## C-39: IS-FALSIFICATION-SIGNAL field typed to GATE structured claim FALSIFICATION-SIGNAL
## C-25: self-labeled; C-37 downstream: labels appear in weight table Penalty column (ROLE 3)

NO-SERVICE-MANIFEST:
  Looked for:                docker-compose.yml, k8s/, Helm charts, service ports
  Detected:                  [PRESENT | ABSENT | PARTIAL]
  Modes affected:            rules out service (ABSENT) / weakens service (PARTIAL)
  IS-FALSIFICATION-SIGNAL:   [YES — CONFIRMED (present) | YES — OVERTURNED (absent) |
                              NO — corroborates-alternative ([mode]) | NO — neutral]

NO-DDD-LANGUAGE:
  Looked for:                bounded contexts, aggregate roots, domain events in naming
  Detected:                  [PRESENT | ABSENT | PARTIAL]
  Modes affected:            rules out concept (ABSENT) / weakens concept (PARTIAL)
  IS-FALSIFICATION-SIGNAL:   [YES — CONFIRMED | YES — OVERTURNED |
                              NO — corroborates-alternative ([mode]) | NO — neutral]

NO-DOMAIN-BOUNDARY:
  Looked for:                subdomain directories, business capability groupings
  Detected:                  [PRESENT | ABSENT | PARTIAL]
  Modes affected:            rules out domain (ABSENT) / weakens domain (PARTIAL)
  IS-FALSIFICATION-SIGNAL:   [YES — CONFIRMED | YES — OVERTURNED |
                              NO — corroborates-alternative ([mode]) | NO — neutral]

NO-WORKSPACE-GROUPING:
  Looked for:                workspace config grouping packages by area
  Detected:                  [PRESENT | ABSENT | PARTIAL]
  Modes affected:            rules out directory (ABSENT) / weakens directory (PARTIAL)
  IS-FALSIFICATION-SIGNAL:   [YES — CONFIRMED | YES — OVERTURNED |
                              NO — corroborates-alternative ([mode]) | NO — neutral]

FALSIFICATION-SIGNAL outcome:
  GATE FALSIFICATION-SIGNAL: [label from structured claim]
  Detected as:               [PRESENT — IS-FALSIFICATION-SIGNAL CONFIRMED |
                              ABSENT — IS-FALSIFICATION-SIGNAL OVERTURNED |
                              PARTIAL — IS-FALSIFICATION-SIGNAL WEAKENED]
  Hypothesis:                [CONFIRMED | WEAKENED | OVERTURNED]
Ruled-out modes: [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN complete. No YAML. Open with hypothesis closure citing FALSIFICATION-SIGNAL
outcome from DARK SIGNALS section. Produce weighted evidence table. Penalty column satisfies
C-37: each DARK SIGNALS label appears as a typed Penalty column value.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: precedes YAML; C-27: tri-part → weight table; C-37: Penalty column

Hypothesis closure:
  GATE structured claim: PREDICTED-MODE = [mode]; FALSIFICATION-SIGNAL = [label]
  DARK SIGNALS IS-FALSIFICATION-SIGNAL outcome: [CONFIRMED | WEAKENED | OVERTURNED]
  Consequence for deliberation: [proceed with hypothesis mode | deliberation open for
    alternative; [label] Penalty of -4 applied to [mode]]

Evidence Weight Table:
(Base Score 1-5 from Evidence For schema row count + signal-type strength;
 Penalty: ABSENT signal = -4 (mode ruled out), PARTIAL = -2 (weakened), PRESENT = 0;
 Net = Base - Penalty; highest Net wins)

| Mode      | Evidence For (schema "Repo signal" values)   | DARK SIGNALS Penalty (C-37)      | Base | Penalty | Net | Verdict  |
|-----------|----------------------------------------------|----------------------------------|------|---------|-----|----------|
| directory | [Repo signal 1], [Repo signal 2], ...        | NO-WORKSPACE-GROUPING: -[0/2/4]  | [N]  | [N]     | [N] | [s/p/w]  |
| concept   | [Repo signal 1], ...                         | NO-DDD-LANGUAGE: -[0/2/4]        | [N]  | [N]     | [N] | [s/p/w]  |
| service   | [Repo signal 1], ...                         | NO-SERVICE-MANIFEST: -[0/2/4]    | [N]  | [N]     | [N] | [s/p/w]  |
| domain    | [Repo signal 1], ...                         | NO-DOMAIN-BOUNDARY: -[0/2/4]     | [N]  | [N]     | [N] | [s/p/w]  |

Selected mode: [highest Net Score]
Rationale: [Net Score [N]; schema row "[Repo signal]" was primary evidence;
  DARK SIGNALS [label] Penalty -[N] collapsed [runner-up] from [Base] to Net [N]]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Draft YAML from ROLE 2 schema and ROLE 3 selection. In amend options, hypothesis verdict
(C-40) is the FIRST field of every option. A Chain Audit block below all three amend options
traces the full C-38→C-39→C-40 lifecycle. AMEND-A cites FALSIFICATION-SIGNAL label (C-37)
and Net Score delta (from weight table).

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode] — Net Score: [N]
# falsification-signal: [GATE label] — [CONFIRMED | WEAKENED | OVERTURNED]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team receives one Inertia Advocate from corps-build.
      #   Group-level: Advocates share status-quo context across this group.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 "Repo signal" value]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — DRAFT+FINALIZE PHASE / ROLE 4
(C-30: 10 criteria; C-33: post-YAML bracket; C-34: essential C-02 present)

[ ] Team names match ROLE 2 schema "YAML name (C-02)"                         STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles (C-04)                                       STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                                 STATUS: [CONFIRMED/FAIL]
[ ] At least one group container (C-03)                                        STATUS: [CONFIRMED/FAIL]
[ ] No .roles/ content anywhere (C-05)                                   STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                            STATUS: [CONFIRMED/FAIL]
[ ] Weight table with DARK SIGNALS Penalty column in ROLE 3 (C-27+C-37)        STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                                  STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS with IS-FALSIFICATION-SIGNAL field (C-36+C-39)                STATUS: [CONFIRMED/FAIL]
[ ] AMEND-A: verdict first field + FALSIFICATION-SIGNAL cited (C-37+C-40)      STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN PHASE header = pre-YAML bracket; this header = post-YAML bracket.
C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27+C-37, C-25, C-36+C-39, C-37+C-40 — 10 items.
C-34: essential C-02 alongside 9 aspirational.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; hypothesis verdict leads; C-37+C-40 satisfier)`

```
AMEND-A: Switch pivot mode
  Hypothesis verdict (C-40) [FIRST FIELD]:
    [CONFIRMED — GATE FALSIFICATION-SIGNAL [label] was PRESENT; hypothesis holds;
     switching is optional | OVERTURNED — GATE FALSIFICATION-SIGNAL [label] was ABSENT;
     IS-FALSIFICATION-SIGNAL OVERTURNED; weight table collapsed [mode] to Net [N];
     alternative [mode] Net [M] recommended]
  Current: [ROLE 3 mode] — Net Score [N]
  DARK SIGNALS basis (C-37): FALSIFICATION-SIGNAL [label] — [ABSENT/PARTIAL] — Penalty -[N]
    applied in weight table; collapsed [mode] from Base [B] to Net [N].
  Debt if skipped: structured claim FALSIFICATION-SIGNAL documented and IS-FALSIFICATION-
    SIGNAL OVERTURNED — hypothesis overturn consequence not acted on; corps-build through
    corps-rob inherit misaligned clustering from undiscarded claim.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Hypothesis verdict (C-40) [FIRST FIELD]:
    [CONFIRMED | OVERTURNED — mode shift may change exec office naming context]
  Current: "[name]" | Source: [ROLE 2 exec inference or "no signal"]
  Debt if skipped: Name propagates verbatim into corps-rob and corps-committee templates.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Hypothesis verdict (C-40) [FIRST FIELD]:
    [CONFIRMED — group structure follows hypothesis mode topology |
     OVERTURNED — mode shift implies group structure revision]
  Current: [n] groups | Principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocate context fragmented across misaligned groups.
  Command: /corps-scan --groups "[description]"

Chain Audit — C-38 → C-39 → C-40:
  C-38 — GATE structured claim: PREDICTED-MODE = [mode];
           FALSIFICATION-SIGNAL = [label]; STRUCTURAL-PREDICTION = [sentence].
  C-39 — DARK SIGNALS IS-FALSIFICATION-SIGNAL: [label] → [CONFIRMED | OVERTURNED | WEAKENED];
           [other labels] → [corroborates-alternative | neutral].
  C-40 — AMEND-A verdict (first field): [CONFIRMED | OVERTURNED] — hypothesis lifecycle closed.
  Lifecycle trace: complete. All three criteria satisfied and auditable in single block.
```

> "corps-scan complete (R11 V-05). Combination: (1) Structured hypothesis claim — PREDICTED-
> MODE / STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL triplet in GATE (C-38). (2) Weighted
> evidence table — Penalty column carries DARK SIGNALS labels as typed column values (C-37);
> Net Score drives selection. (3) Amend-as-verdict — hypothesis outcome leads every amend
> option (C-40); Chain Audit traces C-38→C-39→C-40 as single auditable block. Maximum
> hypothesis lifecycle traceability: claim formalism at GATE, typed evidence at SCAN,
> quantified scoring at DELIBERATE, verdict-first + chain trace at AMEND.
> All C-01 through C-40 requirements met. Draft-only."
