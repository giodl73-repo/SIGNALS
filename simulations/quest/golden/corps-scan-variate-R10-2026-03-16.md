---
skill: quest-variate
skill_target: corps-scan
round: 10
date: 2026-03-16
rubric_version: 9
---

# Variate R10 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v9 rubric (235 pts,
37 criteria). R9's V-01 scored 235/235 under v9 and is the reference ceiling. All prior
invariants through C-37 are treated as structural requirements every variation must satisfy.

R9 axes already covered (not re-explored in R10):
- Lifecycle emphasis — negative space inventory (DARK SIGNALS as list following Signal Schema)
- Lifecycle emphasis — phase output contracts at phase footers
- Output format — downstream consumer annotations on YAML elements
- Output format — criterion cluster naming as primary pre-check key
- Combination — negative space inventory + downstream consumer annotations

R10 explores four new single-axis variation axes and one combination:

1. **Hypothesis-first role sequence** — The model declares its pivot mode hypothesis BEFORE
   scanning. The SCAN PHASE then explicitly confirms or refutes the hypothesis; DARK SIGNALS
   entries are framed as "hypothesis refutation evidence" rather than standalone negative space.
   The deliberation phase closes the loop by referencing the hypothesis outcome. Hypothesis:
   235/235 — the causal chain (hypothesis → scan → confirm/refute → select) is a more
   natural epistemic structure and may surface a new tightening of C-37 (deliberation
   citing DARK SIGNALS as refutation).

2. **Detective register phrasing** — Narrative-imperative style: each phase header frames the
   role as an investigation ("What to look for. What counts as found. What absence means.").
   DARK SIGNALS section is titled "WHAT I DIDN'T FIND" with the same per-entry mode-impact
   structure. Evidence Against entries in deliberation read as deductions from negative finds.
   Hypothesis: 235/235 — phrasing change is orthogonal to criterion structure; may affect
   scorer comprehension and future phrasing guidance extraction.

3. **DARK SIGNALS as evidence table** — The DARK SIGNALS section is formatted as a structured
   table with columns: Signal Name | Looked For | Found? | Pivot Modes Affected | Consequence.
   The table format makes each entry's mode-impact explicit in a column rather than inline prose.
   Evidence Against in deliberation cites the "Signal Name" column value as label. The table
   replaces the R9 block-list format for the same four signal types plus optional extension rows.
   Hypothesis: 235/235 — table format may produce more reliable model behavior by constraining
   each absence to a named row with a typed "Modes Affected" cell.

4. **Grain-of-the-repo inertia framing** — DARK SIGNALS section is titled "REPO GRAIN" and
   framed as the topology the repo has already committed to. Amend options are explicitly
   labeled as going "with grain" (match the repo topology) vs "against grain" (impose a
   different structure). DARK SIGNALS labels in deliberation are cited as "grain evidence
   against" rather than generic absence. The AMEND-A entry cites a REPO GRAIN entry as its
   basis. Hypothesis: 235/235 — inertia vocabulary is natural in the corps-* pipeline context
   (Inertia Advocate, corps-rob); aligning DARK SIGNALS with "grain" may produce richer amend
   option reasoning.

Combined:
5. **Hypothesis-first + DARK SIGNALS table + phase output footers** — Combines axes 1, 3, and
   the R9 V-02 footer pattern. The model declares its hypothesis in GATE, scans into a table-
   format DARK SIGNALS, closes the deliberation loop citing table rows, and each phase ends
   with a PHASE OUTPUTS footer. The three mechanisms together form the maximum traceability
   stack: forward hypothesis, structured negative evidence, and confirmed-deliverable footers.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence — hypothesis-first (hypothesis declared before scan, DARK SIGNALS confirms/refutes) | V-01 |
| Phrasing register — detective/narrative ("What I found. What I didn't find. What that means.") | V-02 |
| Output format — DARK SIGNALS as structured table (named columns, typed mode-impact cell) | V-03 |
| Inertia framing — REPO GRAIN vocabulary, with-grain vs against-grain amend options | V-04 |
| Combination — hypothesis-first + DARK SIGNALS table + phase output footers | V-05 |

---

## V-01 — Role Sequence: Hypothesis-First (Pivot Hypothesis Before Scan)

**Axis**: Role sequence
**Hypothesis**: R9 variations sequence GATE → SCAN → DELIBERATE → DRAFT, with pivot deliberation
occurring only after the full signal inventory is complete. The natural epistemic complement
is declaring the pivot hypothesis in GATE — before any scanning — and then running SCAN as a
hypothesis-testing exercise. Under this framing, DARK SIGNALS entries are not merely "absent
signals" but "refutation evidence against the stated hypothesis" or "corroboration of the
rejected alternatives." The deliberation phase closes the loop explicitly: was the hypothesis
confirmed, weakened, or overturned by the SCAN findings? This changes the logical structure
without touching the criterion structure: all prior invariants (C-01 through C-37) remain
satisfiable. Hypothesis: 235/235 — hypothesis-first ordering may tighten C-37 by making
the deliberation's DARK SIGNALS citations function as named refutation events rather than
generic absence observations.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and hypothesis.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / HYPOTHESIS OFFICER
`(C-20: structural gate — all roles blocked until complete; C-31: GATE PHASE; C-25: self-labeled)`

Prerequisite for all other roles. Complete the pre-check AND state the pivot hypothesis
before any repo scanning, inventory, deliberation, or YAML work begins.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state vocabulary on every item)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — precedes all scanning, deliberation, and YAML.

[ ] C-13 -- self-referential confirmation:
    C-12 draft-only statement precedes all output in this response — confirmed above.
    STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit possible.
    Violation consequence: output fails golden threshold regardless of composite score.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with group structure, schema-traced teams, named roles:
    SCAN PHASE / ROLE 2 and DELIBERATE PHASE / ROLE 3 feed DRAFT+FINALIZE PHASE / ROLE 4.
    All team YAML names must trace to ROLE 2 Signal Schema "YAML name (C-02)" column.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema, C-NN column headers, multi-criterion header:
    SCAN PHASE / ROLE 2 produces Signal Schema and DARK SIGNALS section.
    DARK SIGNALS entries are framed as hypothesis refutation evidence where applicable.
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part Evidence For/Against/Assessment:
    DELIBERATE PHASE / ROLE 3 closes hypothesis loop: CONFIRMED / WEAKENED / OVERTURNED.
    Evidence Against entries cite DARK SIGNALS section by signal-type label.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-36+C-37 -- DARK SIGNALS section, deliberation + amend cross-reference:
    SCAN PHASE produces DARK SIGNALS section after Signal Schema.
    DELIBERATE PHASE Evidence Against cites DARK SIGNALS labels by name.
    AMEND-A cites a DARK SIGNALS label as basis for alternative mode recommendation.
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2 + DELIBERATE PHASE / ROLE 3 +
    DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30 -- debt-framed amend options, multi-criterion post-write:
    DRAFT+FINALIZE PHASE / ROLE 4 produces debt-framed amend options (C-16) and a
    4+-criterion post-write block including at least one essential-tier C-NN (C-34).
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15 satisfied: pre-check names C-05, C-01+C-02+C-03+C-04, C-11+C-21+C-22+C-25+C-26,
C-23+C-27, C-36+C-37, C-16+C-30 as skill requirements.
C-17 satisfied: all SCHEDULED items are forward commitments to named future roles.
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys throughout.
C-28 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED on every item.
C-29 satisfied: "C-01+C-02+C-03+C-04", "C-11+C-21+C-22+C-25+C-26", "C-23+C-27",
"C-36+C-37", "C-16+C-30" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present on actual items.
C-35 satisfied: C-05 STATUS: ACKNOWLEDGED — essential failure named with consequence.

**Pivot Hypothesis** `(C-25: self-labeled; precedes SCAN PHASE)`

```
PIVOT HYPOTHESIS — GATE PHASE / ROLE 1
(C-25: section self-labeled; stated before any scanning; will be confirmed/weakened/overturned
 by DARK SIGNALS findings in SCAN PHASE / ROLE 2)

Initial hypothesis: [directory | concept | service | domain] mode
Basis: [one sentence — first-pass repo read: top-level directory names, presence/absence
  of service manifests, DDD vocabulary in naming conventions]
Confidence: [high | medium | low]
Hypothesis-refuting signal: [name the DARK SIGNAL that, if found ABSENT, would most
  strongly challenge this hypothesis]
```

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: section self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE PHASE / ROLE 1 pre-check and hypothesis complete. Produce Signal Schema
and DARK SIGNALS section. No pivot deliberation, no YAML. Frame DARK SIGNALS entries relative
to the GATE hypothesis: mark each absence as "REFUTES HYPOTHESIS", "CORROBORATES ALTERNATIVE",
or "NEUTRAL" based on GATE PHASE / ROLE 1 pivot hypothesis.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check workspace configs
(npm workspaces, Cargo workspace, `go.work`). Check domain-language signals (bounded context
names, aggregate roots, domain events in directory/module names).

#### Signal Schema `(C-26: C-11 + C-21 satisfier — SCAN PHASE / precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: this header announces criterion purpose before schema rows are written
## C-25: section self-labeled; C-31: SCAN PHASE; C-33: pre-YAML bracket position

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if fewer detected signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only (Engineer, PM, Tech Lead, etc.) — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row — no generic phrases.
- Cap at 8 rows. Group weak signals under nearest strong signal; note the grouping.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-25: section self-labeled; C-36 satisfier — negative space inventory; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals and Ruled-Out Modes
## C-25: section self-labeled; C-36: structured negative evidence with per-entry mode impact
## Purpose: document what was NOT detected; frame relative to GATE PHASE hypothesis
## C-37 downstream use: Evidence Against in ROLE 3 must cite labels from this section by name

No-service-manifest signals:
  Label: NO-SERVICE-MANIFEST
  Looked for: docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected: [PRESENT | ABSENT | PARTIAL]
  Pivot modes affected: rules out service mode (ABSENT) / weakens service mode (PARTIAL)
  Hypothesis relation: [REFUTES HYPOTHESIS | CORROBORATES ALTERNATIVE | NEUTRAL]

No-DDD-language signals:
  Label: NO-DDD-LANGUAGE
  Looked for: bounded context names, aggregate roots, domain events in directory/module names
  Detected: [PRESENT | ABSENT | PARTIAL]
  Pivot modes affected: rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)
  Hypothesis relation: [REFUTES HYPOTHESIS | CORROBORATES ALTERNATIVE | NEUTRAL]

No-domain-boundary signals:
  Label: NO-DOMAIN-BOUNDARY
  Looked for: explicit subdomain directories, business capability groupings
  Detected: [PRESENT | ABSENT | PARTIAL]
  Pivot modes affected: rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)
  Hypothesis relation: [REFUTES HYPOTHESIS | CORROBORATES ALTERNATIVE | NEUTRAL]

No-workspace-grouping signals:
  Label: NO-WORKSPACE-GROUPING
  Looked for: monorepo workspace config grouping packages by area
  Detected: [PRESENT | ABSENT | PARTIAL]
  Pivot modes affected: rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)
  Hypothesis relation: [REFUTES HYPOTHESIS | CORROBORATES ALTERNATIVE | NEUTRAL]

Hypothesis outcome: [CONFIRMED — no refutation signals found ABSENT |
                     WEAKENED — [label] found ABSENT, partial revision needed |
                     OVERTURNED — [label] found ABSENT, pivot mode must change]
Summary of ruled-out modes: [list any modes whose primary signals were ABSENT]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: section self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 Signal Schema and DARK SIGNALS complete. No YAML.

Open with hypothesis closure: state whether GATE hypothesis was CONFIRMED, WEAKENED, or
OVERTURNED by DARK SIGNALS findings, naming the specific label responsible if WEAKENED or
OVERTURNED. Then enumerate all 4 pivot modes with tri-part triad. Evidence Against entries
must cite DARK SIGNALS labels by name (C-37 satisfier). Select one mode. Cite a specific
ROLE 2 schema row by "Repo signal" value.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-31: DELIBERATE PHASE; C-37: Evidence Against entries cite DARK SIGNALS labels by name

Hypothesis closure:
  GATE hypothesis: [mode]
  DARK SIGNALS outcome: [CONFIRMED | WEAKENED by [LABEL] | OVERTURNED by [LABEL]]
  Consequence: [no change needed | pivot reconsideration → [mode]]

directory mode:
  Evidence For: [schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [DARK SIGNALS: NO-WORKSPACE-GROUPING — [ABSENT/PARTIAL/PRESENT]]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [DARK SIGNALS: NO-DDD-LANGUAGE — [ABSENT/PARTIAL/PRESENT]]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [DARK SIGNALS: NO-SERVICE-MANIFEST — [ABSENT/PARTIAL/PRESENT]]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context signals]
  Evidence Against: [DARK SIGNALS: NO-DOMAIN-BOUNDARY — [ABSENT/PARTIAL/PRESENT]]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific ROLE 2 Signal Schema row ("Repo signal" value)
  that most strongly supports selection; cite DARK SIGNALS label that eliminates alternatives]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: section self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. No new scanning or deliberation. Draft YAML from
ROLE 2 schema and ROLE 3 pivot selection, then verify and provide amend options.
AMEND-A must cite a DARK SIGNALS label as basis for the alternative mode recommendation
(C-37 amend satisfier).

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. Hypothesis [CONFIRMED | WEAKENED | OVERTURNED] in ROLE 3. C-05 ACKNOWLEDGED
> in GATE: no .craft/roles/ content in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
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

#### Post-Write Verification `(C-25: section self-labeled; C-26: C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: criterion IDs cited at point of satisfaction; C-30: 10 criteria cited;
 C-33: post-YAML bracket; C-34: essential-tier C-02 cited in this inventory)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"             STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles (no generics)                       STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present                                       STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present                              STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content anywhere in this output                  STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                   STATUS: [CONFIRMED/FAIL]
[ ] Tri-part pivot deliberation in ROLE 3 (C-27)                      STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                         STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS section produced with hypothesis-relation field (C-36) STATUS: [CONFIRMED/FAIL]
[ ] Evidence Against cites DARK SIGNALS labels; AMEND-A cites label (C-37) STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN PHASE header (C-11+C-21) = pre-YAML bracket; this header (C-14+C-30) = post-YAML bracket.
C-30: this block cites C-14, C-02, C-24, C-27, C-25, C-26, C-33, C-34, C-36, C-37 — 10 criteria.
C-34: essential-tier C-02 present alongside 9 aspirational criteria.
```

#### Amend Options `(C-25: section self-labeled; C-08+C-16 satisfier; C-37: AMEND-A cites DARK SIGNALS label)`

```
AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | DARK SIGNALS basis: [LABEL — e.g., NO-SERVICE-MANIFEST was ABSENT]
  Basis: DARK SIGNALS label [LABEL] ruled out [mode]; hypothesis [CONFIRMED/OVERTURNED].
  Debt if skipped: All downstream corps-* skills (corps-build, corps-pr, corps-committee,
    corps-rob) inherit misaligned clustering; DARK SIGNALS refutation evidence was documented
    but not acted on.
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

> "corps-scan complete (R10 V-01). Hypothesis-first role sequence: pivot hypothesis declared in
> GATE before scanning, DARK SIGNALS in SCAN PHASE carry hypothesis-relation field (CONFIRMS/
> WEAKENS/OVERTURNS), DELIBERATE PHASE opens with hypothesis closure citing DARK SIGNALS label.
> AMEND-A cites DARK SIGNALS label as mode-switch basis. All C-36 and C-37 requirements met.
> Draft-only."

---

## V-02 — Phrasing Register: Detective/Narrative Mode

**Axis**: Phrasing register
**Hypothesis**: R9 and prior rounds use formal, technical, checklist-dominant phrasing.
The same criterion structure can be expressed in a detective/narrative register: each phase
is framed as an investigation, each role asks "What am I looking for? What counts as finding
it? What does absence tell me?" The DARK SIGNALS section becomes "WHAT I DIDN'T FIND" with
identical per-entry mode-impact content. Evidence Against reads as deductions from negative
finds rather than formal citations. The criterion coverage is unchanged; only the surface
phrasing shifts. Hypothesis: 235/235 — phrasing is orthogonal to criterion structure; may
affect future extraction of phrasing guidance as a variation dimension.

---

You are running `corps-scan`. Work through four investigation phases in strict sequence.
**Phases 2, 3, and 4 are sealed until Phase 1 produces its compliance log.**

**HARD BOUNDARY**: This run produces a draft org.yaml for human sign-off.
Nothing written to `.craft/roles/` in this response. (C-12 satisfier.)

---

### Phase 1 — GATE: The Case File
`(C-20: structural gate; C-31: GATE PHASE; C-25: section self-labeled)`

Every good investigation starts with the case file: what are you authorized to do, what are
the limits, what do you need to produce? Complete this before touching the repo.

```
COMPLIANCE LOG — corps-scan — Phase 1 / GATE
(C-25: section self-labeled; C-18: C-NN IDs primary keys; C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED)

What I'm authorized to produce:
[ ] C-12 -- "HARD BOUNDARY" declared above this log, first thing in the output.
    STATUS: CONFIRMED.

[ ] C-13 -- C-12 statement is before this compliance log.
    STATUS: CONFIRMED.

What I must never do:
[ ] C-05 -- No .craft/roles/ files, no role file content, no role-creation instructions.
    STATUS: ACKNOWLEDGED. If I write any role file content, this output fails golden,
    regardless of everything else.

What I need to find (investigation targets):
[ ] C-11+C-21+C-22+C-25+C-26 -- a Signal Schema: one row per repo area I find, with
    columns for "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    A WHAT I DIDN'T FIND section follows the schema for absent signals.
    STATUS: SCHEDULED — Phase 2 / SCAN.

[ ] C-23+C-27 -- a Pivot Deliberation: four pivot modes examined, Evidence For/Against/
    Assessment for each, one mode selected, rationale citing a specific schema row.
    Evidence Against cites WHAT I DIDN'T FIND entries by label.
    STATUS: SCHEDULED — Phase 3 / DELIBERATE.

[ ] C-01+C-02+C-03+C-04 -- the org.yaml draft: groups, exec office, teams tracing to schema,
    named roles per team. No generics. No Inertia Advocate in roles list (auto-added later).
    STATUS: SCHEDULED — Phase 4 / DRAFT+FINALIZE.

[ ] C-36+C-37 -- WHAT I DIDN'T FIND section in Phase 2; Evidence Against in Phase 3 cites
    its labels by name; AMEND-A in Phase 4 cites a label as basis.
    STATUS: SCHEDULED — Phases 2, 3, and 4.

[ ] C-16+C-30 -- debt-framed amend options; 4+-criterion post-write with one essential (C-34).
    STATUS: SCHEDULED — Phase 4 / DRAFT+FINALIZE.
```

C-15: compliance log names C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-01+C-02+C-03+C-04,
C-36+C-37, C-16+C-30 as required outputs.
C-17: all SCHEDULED items name the phase that will deliver them.
C-29: compound bundles "C-11+C-21+C-22+C-25+C-26", "C-01+C-02+C-03+C-04", "C-36+C-37",
"C-16+C-30" are single checklist items.
C-35: C-05 STATUS: ACKNOWLEDGED with golden-failure consequence named.

Phase 1 / GATE sealed. Phase 2 / SCAN may now open.

---

### Phase 2 — SCAN: What I Found and What I Didn't
`(C-25: section self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk the repo like a detective. Check: top-level directories, `src/`, `services/`,
`packages/`, `apps/`, `modules/`. Service manifests (`docker-compose.yml`, `k8s/`, Helm
charts). Workspace configs (npm workspaces, Cargo workspace, `go.work`). Domain vocabulary
(bounded context names, aggregate roots, business capability terms in directory names).

Write down what you found. Then write down what you looked for but didn't find.

#### What I Found — Signal Schema
`(C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled; C-25: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: criterion purpose declared in this header before schema rows
## C-33: pre-YAML bracket; C-25: section self-labeled

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if fewer signals detected.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence allowed.
- "Proposed roles (C-04)": substantive role names only — no "TBD" or "role_1" tokens.
- "Detection evidence (C-09)": one sentence of repo evidence — no generic phrases.

Exec office read: [what in the repo suggested the exec name, or "nothing — placeholder used"]
```

#### What I Didn't Find — DARK SIGNALS
`(C-36 satisfier; C-25: section self-labeled; follows Signal Schema)`

```
## WHAT I DIDN'T FIND — {{date}}
## C-36: structured negative evidence inventory with per-entry mode impact
## C-25: section self-labeled; C-37 downstream: these labels must be cited in Phase 3 + Phase 4

NO-SERVICE-MANIFEST:
  What I looked for: docker-compose.yml, k8s/, Helm charts, service port definitions
  What I found: [PRESENT | ABSENT | PARTIAL]
  What that means: rules out service mode (ABSENT) / weakens service mode (PARTIAL)

NO-DDD-LANGUAGE:
  What I looked for: bounded context names, aggregate roots, domain event terms in naming
  What I found: [PRESENT | ABSENT | PARTIAL]
  What that means: rules out concept mode (ABSENT) / weakens concept mode (PARTIAL)

NO-DOMAIN-BOUNDARY:
  What I looked for: subdomain directories, business capability groupings
  What I found: [PRESENT | ABSENT | PARTIAL]
  What that means: rules out domain mode (ABSENT) / weakens domain mode (PARTIAL)

NO-WORKSPACE-GROUPING:
  What I looked for: workspace config grouping packages by area
  What I found: [PRESENT | ABSENT | PARTIAL]
  What that means: rules out directory mode (ABSENT) / weakens directory mode (PARTIAL)

Bottom line: modes eliminated by absent signals: [list | none]
```

Phase 2 / SCAN sealed. Phase 3 / DELIBERATE may now open.

---

### Phase 3 — DELIBERATE: What It All Means
`(C-25: section self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

No new scanning. No YAML. Reason from what Phase 2 found and didn't find to a pivot mode
selection. Each mode gets: what points toward it, what points away (name the WHAT I DIDN'T
FIND label), and a plain-English verdict. Then pick one.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation before YAML; C-27: tri-part triad
## C-37: Evidence Against entries cite WHAT I DIDN'T FIND labels by name

directory mode:
  Evidence For: [schema rows supporting directory clustering, by "Repo signal" value]
  Evidence Against: [WHAT I DIDN'T FIND: NO-WORKSPACE-GROUPING was [ABSENT/PARTIAL] —
    workspace config absent, so directory boundaries are inferred not declared]
  Verdict: [strong / possible / weak — one plain sentence]

concept mode:
  Evidence For: [schema rows where Signal type = domain/concept]
  Evidence Against: [WHAT I DIDN'T FIND: NO-DDD-LANGUAGE was [ABSENT/PARTIAL] —
    no bounded context names, so concept clustering lacks named foundations]
  Verdict: [strong / possible / weak — one plain sentence]

service mode:
  Evidence For: [schema rows where Signal type = service]
  Evidence Against: [WHAT I DIDN'T FIND: NO-SERVICE-MANIFEST was [ABSENT/PARTIAL] —
    no service manifests, so service boundary claims can't be verified]
  Verdict: [strong / possible / weak — one plain sentence]

domain mode:
  Evidence For: [schema rows with bounded-context or subdomain signals]
  Evidence Against: [WHAT I DIDN'T FIND: NO-DOMAIN-BOUNDARY was [ABSENT/PARTIAL] —
    no subdomain directories, so domain grouping would be imposed not read]
  Verdict: [strong / possible / weak — one plain sentence]

My read: [selected pivot mode]
Because: [one sentence citing the ROLE 2 schema row that clinched it; name the WHAT I DIDN'T
  FIND label that eliminated the runner-up]
```

Phase 3 / DELIBERATE sealed. Phase 4 / DRAFT+FINALIZE may now open.

---

### Phase 4 — DRAFT+FINALIZE: The Deliverable
`(C-25: section self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

No new scanning or deliberation. Draft the org.yaml from Phase 2 schema and Phase 3
selection. Verify it. Provide amend options. AMEND-A cites a WHAT I DIDN'T FIND label
as the basis for the alternative pivot (C-37 amend satisfier).

> "Writing org.yaml. Team names come from Phase 2 schema 'YAML name (C-02)' column.
> Pivot: [Phase 3 selection]. C-05 acknowledged in Phase 1: no .craft/roles/ in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Phase 3 selection]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From Phase 2 exec read, or: 'Office of Engineering Leadership']"
    # confirm name before corps-build

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate via corps-build.
      teams:
        - name: "[exact YAML name from Phase 2 schema]"
          # schema-signal: [Phase 2 "Repo signal" value]
          roles:
            - [Named role from Phase 2 "Proposed roles" column]
            - [Named role from Phase 2 "Proposed roles" column]
            # Inertia Advocate: auto-added by corps-build — not listed here

    - name: "[Group 2, if schema warrants]"
      type: [...]
      teams: [...]
```

#### Verification Log `(C-25: section self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
VERIFICATION LOG — Phase 4 / DRAFT+FINALIZE
(C-33: post-YAML bracket; C-30: 10 criteria cited; C-34: essential-tier C-02 present)

[ ] Team names match Phase 2 schema "YAML name (C-02)" (C-02)         STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles, no generics (C-04)                 STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present (C-07)                                STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present (C-03)                       STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content anywhere (C-05)                          STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                   STATUS: [CONFIRMED/FAIL]
[ ] Tri-part deliberation with verdict in Phase 3 (C-27)              STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                         STATUS: [CONFIRMED/FAIL]
[ ] WHAT I DIDN'T FIND section present with mode-impact (C-36)        STATUS: [CONFIRMED/FAIL]
[ ] Phase 3 Evidence Against + AMEND-A cite DIDN'T FIND labels (C-37) STATUS: [CONFIRMED/FAIL]

C-14: Phase 1 pre-check (pre-YAML) + this log (post-YAML) — both present.
C-33: Phase 2 Signal Schema header = pre-YAML bracket; this header = post-YAML bracket.
C-30: 10 criteria cited — C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37.
C-34: essential-tier C-02 present alongside 9 aspirational criteria.
```

#### What Could Be Different `(C-25: section self-labeled; C-08+C-16 satisfier; C-37: AMEND-A cites DIDN'T FIND label)`

```
AMEND-A: Use a different pivot mode
  Current: [Phase 3 mode]
  Basis: WHAT I DIDN'T FIND — [LABEL] was ABSENT, which weakens current mode.
    If [alternative mode signal] were present, [alternative mode] would be stronger.
  Debt if skipped: Corps-build, corps-pr, corps-committee, corps-rob all inherit the current
    clustering; the absent-signal evidence for the alternative was documented but ignored.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename the exec office
  Current: "[name]" | Source: [Phase 2 exec read or "no signal found"]
  Debt if skipped: Name propagates into corps-rob governance and corps-committee appointment
    templates verbatim — no later correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Change the group structure
  Current: [n] groups | Principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocates in misaligned groups carry conflicting status-quo
    context, reducing corps-committee signal coherence across all review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R10 V-02). Detective register: GATE is 'case file', SCAN is 'what I
> found / what I didn't find', DELIBERATE is 'what it all means', DRAFT+FINALIZE is 'the
> deliverable'. DARK SIGNALS titled WHAT I DIDN'T FIND — same per-entry mode-impact structure,
> different phrasing register. Evidence Against cites labels by name. AMEND-A cites label.
> All C-36 and C-37 satisfied. Draft-only."

---

## V-03 — Output Format: DARK SIGNALS as Structured Evidence Table

**Axis**: Output format
**Hypothesis**: R9 V-01's DARK SIGNALS section uses a block-list format — one labeled block per
signal type, each with prose "Detected:", "Rules out:", and "Hypothesis relation:" fields. A
structured table format with typed columns (Signal Name | Looked For | Found? | Pivot Modes
Affected | Consequence) provides the same per-entry mode-impact content in a denser, column-
indexed form. Column headers make the types explicit; a scorer can scan the "Pivot Modes
Affected" column without parsing inline prose. Evidence Against entries in deliberation cite
the "Signal Name" column value as the label anchor. The table format may constrain model
behavior more reliably: each absence produces exactly one table row with a typed "Found?"
cell rather than a free-form prose entry. Hypothesis: 235/235 — table format is structurally
equivalent to block-list; column naming may provide a more reliable label anchor for C-37.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label in its header or opening annotation. No section may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: self-labeled; C-18: C-NN IDs primary keys; C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED)

[ ] C-12 -- "HARD BOUNDARY" is the first substantive line of this output.
    STATUS: CONFIRMED.

[ ] C-13 -- C-12 statement precedes this pre-check.
    STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ files, no role file content, no role-creation instructions.
    STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema with C-NN column headers; DARK SIGNALS table
    follows schema. Table columns: Signal Name | Looked For | Found? | Pivot Modes Affected
    | Consequence. Table label cited in ROLE 3 Evidence Against and ROLE 4 AMEND-A.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad; Evidence Against cites DARK SIGNALS
    "Signal Name" column values by name; one amend cites a "Signal Name" value.
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles.
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-36+C-37 -- DARK SIGNALS table present after Signal Schema (C-36); Evidence Against
    cites "Signal Name" column values; AMEND-A cites "Signal Name" value (C-37).
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-16+C-30 -- debt-framed amend options; 4+-criterion post-write with one essential (C-34).
    STATUS: SCHEDULED — DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15: pre-check names all required outputs as skill requirements.
C-17: all SCHEDULED items forward-committed to named roles.
C-29: compound bundles on single items.
C-35: C-05 ACKNOWLEDGED with golden-failure consequence.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests (`docker-compose.yml`, `k8s/`, Helm charts). Workspace configs (npm workspaces,
Cargo workspace, `go.work`). Domain vocabulary (bounded context names, aggregate roots,
business capability terms in naming). No deliberation, no YAML.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN column headers)
## C-22: criterion purpose in header before schema rows; C-25: self-labeled; C-33: pre-YAML

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

- Minimum 2 rows. PLACEHOLDER row if fewer signals detected.
- "YAML name (C-02)": exact string used in YAML teams[].name.
- "Proposed roles (C-04)": named roles only — no generics, no "TBD".
- "Detection evidence (C-09)": one sentence per row — no generic phrases.

Exec office inference: [schema row or term, or "no signal — placeholder"]
```

#### DARK SIGNALS Evidence Table `(C-36 satisfier; C-25: self-labeled; follows Signal Schema)`

```
## DARK SIGNALS Evidence Table — {{date}}
## C-36: structured negative evidence; per-row mode impact in "Pivot Modes Affected" column
## C-25: self-labeled; C-37 downstream: "Signal Name" values must appear in ROLE 3 + ROLE 4

| Signal Name           | Looked For                                               | Found?  | Pivot Modes Affected                                    | Consequence                                         |
|-----------------------|----------------------------------------------------------|---------|---------------------------------------------------------|-----------------------------------------------------|
| NO-SERVICE-MANIFEST   | docker-compose.yml, k8s/, Helm charts, service ports     | [Y/N/P] | Rules out: service (N); weakens: service (P)            | service mode [eliminated | weakened | viable]       |
| NO-DDD-LANGUAGE       | bounded contexts, aggregate roots, domain events         | [Y/N/P] | Rules out: concept (N); weakens: concept (P)            | concept mode [eliminated | weakened | viable]       |
| NO-DOMAIN-BOUNDARY    | subdomain dirs, business capability groupings            | [Y/N/P] | Rules out: domain (N); weakens: domain (P)              | domain mode [eliminated | weakened | viable]        |
| NO-WORKSPACE-GROUPING | monorepo workspace config grouping packages by area      | [Y/N/P] | Rules out: directory (N); weakens: directory (P)        | directory mode [eliminated | weakened | viable]     |

Legend: Found? Y=present, N=absent, P=partial
Modes eliminated (Found?=N): [list | none]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

No new scanning, no YAML. Enumerate all 4 pivot modes. Tri-part triad for each. Evidence
Against entries cite DARK SIGNALS Evidence Table "Signal Name" values by name (C-37 satisfier).
Select one mode; cite specific ROLE 2 schema row by "Repo signal" value.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-37: Evidence Against entries cite DARK SIGNALS Evidence Table "Signal Name" column values

directory mode:
  Evidence For: [schema rows by "Repo signal" value]
  Evidence Against: [DARK SIGNALS table: NO-WORKSPACE-GROUPING Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where Signal type = domain/concept]
  Evidence Against: [DARK SIGNALS table: NO-DDD-LANGUAGE Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where Signal type = service]
  Evidence Against: [DARK SIGNALS table: NO-SERVICE-MANIFEST Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context signals]
  Evidence Against: [DARK SIGNALS table: NO-DOMAIN-BOUNDARY Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific ROLE 2 schema "Repo signal" value that most
  supports selection; cite the DARK SIGNALS table "Signal Name" that eliminates the runner-up]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Draft YAML from ROLE 2 schema and ROLE 3 selection. AMEND-A must cite a DARK SIGNALS Evidence
Table "Signal Name" value as the basis for the alternative mode (C-37 amend satisfier).

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Each team in this group receives one Inertia Advocate from corps-build.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 "Repo signal" value]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — DRAFT+FINALIZE / ROLE 4
(C-30: 10 criteria cited; C-33: post-YAML bracket; C-34: essential C-02 present)

[ ] Team names match ROLE 2 schema "YAML name (C-02)"                    STATUS: [CONFIRMED/FAIL]
[ ] Teams have 2+ named roles, no generics (C-04)                        STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                           STATUS: [CONFIRMED/FAIL]
[ ] At least one group container (C-03)                                  STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content anywhere (C-05)                             STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team + group level (C-24)                        STATUS: [CONFIRMED/FAIL]
[ ] Tri-part deliberation in ROLE 3 (C-27)                               STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                            STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS table present with mode-impact column (C-36)            STATUS: [CONFIRMED/FAIL]
[ ] Evidence Against + AMEND-A cite table "Signal Name" values (C-37)    STATUS: [CONFIRMED/FAIL]

C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37 — 10 criteria.
C-34: essential C-02 alongside 9 aspirational.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier; C-37: AMEND-A cites table Signal Name)`

```
AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode]
  DARK SIGNALS table basis: [Signal Name] Found?=N — [mode] eliminated by table.
  Debt if skipped: corps-build, corps-pr, corps-committee, corps-rob inherit misaligned
    clustering; DARK SIGNALS table evidence was produced but not acted on.
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

> "corps-scan complete (R10 V-03). DARK SIGNALS formatted as structured evidence table with
> columns: Signal Name | Looked For | Found? | Pivot Modes Affected | Consequence. Evidence
> Against entries cite table 'Signal Name' column values by name. AMEND-A cites table Signal
> Name as mode-switch basis. Table format makes per-entry mode impact column-indexed rather
> than prose-embedded. All C-36 and C-37 requirements met. Draft-only."

---

## V-04 — Inertia Framing: Repo Grain Vocabulary

**Axis**: Inertia framing
**Hypothesis**: The corps-* pipeline is built around the Inertia Advocate — the status-quo
competitor embedded in every review cycle. The DARK SIGNALS section documents "what the repo
already is" — its committed topology. Renaming DARK SIGNALS to REPO GRAIN and framing each
entry as a dimension of the repo's existing topology (rather than mere absence) aligns the
negative evidence section with the pipeline's inertia vocabulary. Amend options are explicitly
labeled as "with-grain" (match what the repo already is) vs "against-grain" (impose a different
structure). AMEND-A cites a REPO GRAIN entry as the basis for the alternative mode: if the
grain is strong for an alternative mode, going against it incurs organizational debt. Evidence
Against entries in deliberation cite REPO GRAIN labels in the same way as DARK SIGNALS labels.
Hypothesis: 235/235 — inertia vocabulary is natural in the corps-* context; grain-framing
may produce richer amend reasoning by naming the cost of going against the repo topology.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section must carry a C-NN self-label. No unlabeled
sections.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: self-labeled; C-18: C-NN IDs primary keys; C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED)

[ ] C-12 -- "HARD BOUNDARY" is the first substantive line. STATUS: CONFIRMED.
[ ] C-13 -- C-12 precedes this pre-check. STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ files anywhere in this output.
    STATUS: ACKNOWLEDGED — essential failure if violated; golden disqualification.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema; REPO GRAIN section follows as named section.
    REPO GRAIN entries name which pivot modes the repo's existing topology supports vs
    undermines. C-37: REPO GRAIN labels cited in ROLE 3 Evidence Against and ROLE 4 AMEND-A.
    STATUS: SCHEDULED — SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad; Evidence Against cites REPO GRAIN labels.
    STATUS: SCHEDULED — DELIBERATE PHASE / ROLE 3.

[ ] C-01+C-02+C-03+C-04 -- org.yaml draft. STATUS: SCHEDULED — DRAFT+FINALIZE / ROLE 4.

[ ] C-36+C-37 -- REPO GRAIN section (C-36 satisfier — same negative evidence, grain framing);
    ROLE 3 Evidence Against cites REPO GRAIN labels; AMEND-A cites REPO GRAIN label +
    with-grain/against-grain classification (C-37 satisfier).
    STATUS: SCHEDULED — ROLE 2 + ROLE 3 + ROLE 4.

[ ] C-16+C-30 -- debt-framed amends; 4+-criterion post-write with one essential.
    STATUS: SCHEDULED — DRAFT+FINALIZE / ROLE 4.
```

C-35: C-05 ACKNOWLEDGED with golden-disqualification consequence named.
C-29: compound bundles on single items.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary. Produce Signal Schema then REPO GRAIN section.
The REPO GRAIN section documents the repo's existing topology — what it already is — and which
pivot modes that topology supports or undermines.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML) + C-21 satisfier (C-NN columns)
## C-22: criterion purpose declared before rows; C-25: self-labeled; C-33: pre-YAML bracket

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |

- Minimum 2 rows. PLACEHOLDER row if fewer signals.
- "YAML name (C-02)": exact string in YAML teams[].name.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence per row.

Exec office inference: [term from repo, or "no signal — placeholder"]
```

#### REPO GRAIN `(C-36 satisfier; C-25: self-labeled; grain-topology framing of absent signals)`

```
## REPO GRAIN — {{date}} — Existing Topology and Mode Implications
## C-36: structured negative evidence inventory with per-entry mode impact
## C-25: self-labeled; C-37 downstream: these REPO GRAIN labels must appear in ROLE 3 + ROLE 4
## Framing: each entry names a dimension of the repo's committed topology

GRAIN-NO-SERVICE-MANIFEST:
  Topology: [service manifest present | absent | partial]
  What it means: repo [is | is not | partially is] organized as distinct services
  Modes supported: [service mode gains/loses strength]
  Modes undermined: [service mode [eliminated | weakened] if absent/partial]

GRAIN-NO-DDD-LANGUAGE:
  Topology: [DDD vocabulary present | absent | partial in naming]
  What it means: repo [does | does not | partially] use domain-driven naming conventions
  Modes supported: [concept mode gains/loses strength]
  Modes undermined: [concept mode [eliminated | weakened] if absent/partial]

GRAIN-NO-DOMAIN-BOUNDARY:
  Topology: [subdomain directories present | absent | partial]
  What it means: repo [has | lacks | partially has] explicit domain boundary structure
  Modes supported: [domain mode gains/loses strength]
  Modes undermined: [domain mode [eliminated | weakened] if absent/partial]

GRAIN-NO-WORKSPACE-GROUPING:
  Topology: [workspace grouping present | absent | partial]
  What it means: repo [is | is not | partially is] grouped by area in workspace config
  Modes supported: [directory mode gains/loses strength]
  Modes undermined: [directory mode [eliminated | weakened] if absent/partial]

Grain summary:
  Repo topology leans: [mode(s) most supported by existing structure]
  Going with grain: [mode(s) that match what the repo already is]
  Going against grain: [mode(s) that would impose structure the repo doesn't have]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

No YAML. Tri-part triad for all 4 modes. Evidence Against entries cite REPO GRAIN labels
by name. Selection cites a specific schema row by "Repo signal" value and names whether the
selection is with-grain or against-grain.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-37: Evidence Against cites REPO GRAIN labels (GRAIN-NO-*) by name

directory mode:
  Evidence For: [schema rows supporting directory clustering]
  Evidence Against: [REPO GRAIN: GRAIN-NO-WORKSPACE-GROUPING — topology [absent/partial]:
    going against grain — workspace grouping not declared in repo]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where Signal type = domain/concept]
  Evidence Against: [REPO GRAIN: GRAIN-NO-DDD-LANGUAGE — topology [absent/partial]:
    going against grain — no DDD naming conventions in repo]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where Signal type = service]
  Evidence Against: [REPO GRAIN: GRAIN-NO-SERVICE-MANIFEST — topology [absent/partial]:
    going against grain — no service boundaries declared in manifests]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context signals]
  Evidence Against: [REPO GRAIN: GRAIN-NO-DOMAIN-BOUNDARY — topology [absent/partial]:
    going against grain — no subdomain structure in repo]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Grain classification: [with-grain | against-grain]
Rationale: [one sentence: schema row value that clinches selection; REPO GRAIN entry that
  eliminates the runner-up; cost of going against grain if applicable]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Draft YAML. AMEND-A cites a REPO GRAIN label + with-grain/against-grain framing as the
basis for the alternative mode recommendation (C-37 amend satisfier).

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# grain-classification: [with-grain | against-grain]
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
        - name: "[YAML name — exact match ROLE 2 'YAML name (C-02)']"
          # schema-signal: [ROLE 2 "Repo signal" value]
          # grain-note: [with-grain | against-grain — brief reason]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2]"
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — ROLE 4
(C-30: 10 criteria; C-33: post-YAML bracket; C-34: essential C-02)

[ ] Team names match ROLE 2 schema (C-02)                               STATUS: [CONFIRMED/FAIL]
[ ] Teams have 2+ named roles (C-04)                                    STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                          STATUS: [CONFIRMED/FAIL]
[ ] Group container present (C-03)                                      STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content (C-05)                                     STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate governance at team + group level (C-24)            STATUS: [CONFIRMED/FAIL]
[ ] Tri-part deliberation with grain-classification (C-27)              STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                           STATUS: [CONFIRMED/FAIL]
[ ] REPO GRAIN section present with mode impact (C-36)                  STATUS: [CONFIRMED/FAIL]
[ ] Evidence Against + AMEND-A cite REPO GRAIN labels (C-37)            STATUS: [CONFIRMED/FAIL]

C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37 — 10 criteria.
C-34: essential C-02 alongside 9 aspirational.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16; C-37: AMEND-A cites REPO GRAIN label)`

```
AMEND-A: Switch pivot mode (with-grain alternative)
  Current: [ROLE 3 mode] — [with-grain | against-grain]
  REPO GRAIN basis: [GRAIN-NO-*] — topology [absent/partial] — current mode goes against grain.
  With-grain alternative: [mode] — aligns with what the repo already is.
  Debt if skipped: Imposing against-grain structure activates Inertia Advocates in opposition;
    corps-rob governance artifacts will reflect ongoing friction with repo topology.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Grain: [with-grain name from repo | no signal — placeholder imposed]
  Debt if skipped: Propagates into corps-rob + corps-committee templates verbatim.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grain: [groups [match | don't match] repo's natural clustering]
  Debt if skipped: Against-grain grouping means Inertia Advocates carry conflicting frames;
    corps-committee review coherence degrades over time.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R10 V-04). DARK SIGNALS renamed REPO GRAIN; each entry named GRAIN-NO-*
> and framed as existing repo topology dimension with with-grain/against-grain mode implication.
> Amend options carry with-grain/against-grain labels; AMEND-A cites REPO GRAIN entry as basis
> for alternative. Evidence Against cites GRAIN-NO-* labels by name. Inertia vocabulary aligned
> with corps-* pipeline (Inertia Advocate, corps-rob). All C-36 and C-37 satisfied. Draft-only."

---

## V-05 — Combination: Hypothesis-First + DARK SIGNALS Table + Phase Output Footers

**Axis**: Combination
**Hypothesis**: Combines V-01's hypothesis-first role sequence (pivot hypothesis declared in
GATE, DARK SIGNALS entries carry hypothesis-relation field), V-03's structured evidence table
format for DARK SIGNALS (columns: Signal Name | Looked For | Found? | Pivot Modes Affected
| Consequence | Hypothesis Relation), and R9 V-02's phase output footer pattern (each phase
ends with a formal PHASE OUTPUTS block naming exactly what was delivered). Together these
three mechanisms form the maximum traceability stack: (1) forward hypothesis commitment before
scanning, (2) column-indexed negative evidence with hypothesis-relation typed in a cell, and
(3) confirmed-deliverable footers at each phase boundary. A scorer can verify the hypothesis
outcome from the DARK SIGNALS table "Hypothesis Relation" column without reading prose; the
PHASE OUTPUTS footer names the deliverables precisely without re-reading the phase body; and
the deliberation closes the loop by citing table "Signal Name" values. Hypothesis: 235/235 —
the three mechanisms are orthogonal in structure; their combination maximizes traceability
surface area and may surface further criterion tightening around hypothesis tracking.

---

You are running `corps-scan`. Work through five named phases in strict sequence.
**Phases 2–5 are blocked until Phase 1 (GATE) outputs its pre-check and pivot hypothesis.**

**Universal labeling rule (C-25)**: Every section in every phase carries a C-NN self-label.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### GATE PHASE
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE
(C-25: self-labeled; C-18: C-NN IDs primary keys; C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED)

[ ] C-12 -- "HARD BOUNDARY" is the first substantive line. STATUS: CONFIRMED.
[ ] C-13 -- C-12 precedes this pre-check. STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ content anywhere.
    STATUS: ACKNOWLEDGED — golden disqualification if violated.

[ ] C-11+C-21+C-22+C-25+C-26 -- Signal Schema; DARK SIGNALS evidence table follows.
    Table carries "Hypothesis Relation" column typed per row.
    STATUS: SCHEDULED — SCAN PHASE.

[ ] C-23+C-27 -- pivot deliberation; Evidence Against cites table "Signal Name" values;
    deliberation opens with hypothesis closure (CONFIRMED/WEAKENED/OVERTURNED).
    STATUS: SCHEDULED — DELIBERATE PHASE.

[ ] C-01+C-02+C-03+C-04 -- org.yaml draft. STATUS: SCHEDULED — DRAFT PHASE.

[ ] C-36+C-37 -- DARK SIGNALS table (C-36); table "Signal Name" cited in DELIBERATE Phase
    Evidence Against and DRAFT PHASE AMEND-A (C-37). STATUS: SCHEDULED — SCAN + DELIBERATE
    + DRAFT.

[ ] C-16+C-30 -- debt-framed amends; 4+-criterion post-write with one essential (C-34).
    STATUS: SCHEDULED — FINALIZE PHASE.
```

C-35: C-05 ACKNOWLEDGED with consequence.
C-29: compound bundles on single items.

**Pivot Hypothesis** `(C-25: self-labeled; hypothesis stated before SCAN)`

```
PIVOT HYPOTHESIS — GATE PHASE
(C-25: self-labeled; C-32: stated before scanning; will be typed in DARK SIGNALS table)

Hypothesis: [directory | concept | service | domain] mode
Basis: [one sentence — first-pass repo read]
Confidence: [high | medium | low]
Key refutation signal: [the DARK SIGNALS table "Signal Name" that, if Found?=N, most
  challenges this hypothesis]
```

```
PHASE OUTPUTS — GATE PHASE
(C-25: self-labeled; phase footer pattern from R9 V-02)

Outputs produced:
  - Compliance pre-check: CONFIRMED/SCHEDULED/ACKNOWLEDGED on 8 items
  - Pivot hypothesis: [mode], confidence [level], key refutation signal named
  - All phases unblocked: no
```

GATE PHASE complete. SCAN PHASE may now begin.

---

### SCAN PHASE
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Service
manifests. Workspace configs. Domain vocabulary. Produce Signal Schema then DARK SIGNALS
evidence table with "Hypothesis Relation" column.

#### Signal Schema `(C-26: C-11+C-21 satisfier; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML) + C-21 satisfier (C-NN columns)
## C-22: criterion purpose in header; C-25: self-labeled; C-33: pre-YAML bracket

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |

- Minimum 2 rows. PLACEHOLDER if fewer signals.
- "YAML name (C-02)": exact string in YAML teams[].name.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence per row.

Exec office inference: [term from repo, or "no signal — placeholder"]
```

#### DARK SIGNALS Evidence Table `(C-36 satisfier; C-25: self-labeled; includes Hypothesis Relation column)`

```
## DARK SIGNALS Evidence Table — {{date}}
## C-36: structured negative evidence; per-row mode impact in "Pivot Modes Affected" column
## C-25: self-labeled; "Hypothesis Relation" column closes the loop from GATE hypothesis
## C-37 downstream: "Signal Name" values cited in DELIBERATE PHASE + DRAFT PHASE AMEND-A

| Signal Name           | Looked For                                           | Found?  | Pivot Modes Affected                             | Consequence                               | Hypothesis Relation               |
|-----------------------|------------------------------------------------------|---------|--------------------------------------------------|-------------------------------------------|-----------------------------------|
| NO-SERVICE-MANIFEST   | docker-compose.yml, k8s/, Helm, service ports        | [Y/N/P] | Rules out: service (N); weakens: service (P)     | service mode [eliminated|weakened|viable] | [REFUTES|CORROBORATES ALT|NEUTRAL]|
| NO-DDD-LANGUAGE       | bounded contexts, aggregate roots, domain events     | [Y/N/P] | Rules out: concept (N); weakens: concept (P)     | concept mode [eliminated|weakened|viable] | [REFUTES|CORROBORATES ALT|NEUTRAL]|
| NO-DOMAIN-BOUNDARY    | subdomain dirs, business capability groupings        | [Y/N/P] | Rules out: domain (N); weakens: domain (P)       | domain mode [eliminated|weakened|viable]  | [REFUTES|CORROBORATES ALT|NEUTRAL]|
| NO-WORKSPACE-GROUPING | workspace config grouping packages by area           | [Y/N/P] | Rules out: directory (N); weakens: directory (P) | directory mode [eliminated|weakened|viable]| [REFUTES|CORROBORATES ALT|NEUTRAL]|

Legend: Found? Y=present N=absent P=partial | Hypothesis Relation: relative to GATE hypothesis
Hypothesis outcome: [CONFIRMED | WEAKENED by [Signal Name] | OVERTURNED by [Signal Name]]
Modes eliminated (Found?=N): [list | none]
```

```
PHASE OUTPUTS — SCAN PHASE
(C-25: self-labeled; phase footer)

Outputs produced:
  - Signal Schema: [n] rows, exec office inference: [value]
  - DARK SIGNALS Evidence Table: 4 rows, modes eliminated: [list | none]
  - Hypothesis outcome: [CONFIRMED | WEAKENED | OVERTURNED]
  - Handoff to DELIBERATE PHASE: schema rows + table Signal Names available as citation targets
```

SCAN PHASE complete. DELIBERATE PHASE may now begin.

---

### DELIBERATE PHASE
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

No YAML. Open with hypothesis closure. Tri-part triad for all 4 modes. Evidence Against
cites DARK SIGNALS table "Signal Name" values by name. Select one mode.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-37: Evidence Against cites DARK SIGNALS table "Signal Name" column values

Hypothesis closure:
  GATE hypothesis: [mode]
  Table outcome: [CONFIRMED | WEAKENED by [Signal Name] | OVERTURNED by [Signal Name]]
  Pivot adjustment: [none needed | reconsidering toward [mode]]

directory mode:
  Evidence For: [schema rows by "Repo signal" value]
  Evidence Against: [DARK SIGNALS table: NO-WORKSPACE-GROUPING Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak]

concept mode:
  Evidence For: [schema rows where Signal type = domain/concept]
  Evidence Against: [DARK SIGNALS table: NO-DDD-LANGUAGE Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak]

service mode:
  Evidence For: [schema rows where Signal type = service]
  Evidence Against: [DARK SIGNALS table: NO-SERVICE-MANIFEST Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak]

domain mode:
  Evidence For: [schema rows with bounded-context signals]
  Evidence Against: [DARK SIGNALS table: NO-DOMAIN-BOUNDARY Found?=[N/P] — [consequence]]
  Assessment: [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [schema row "Repo signal" value that clinches it; DARK SIGNALS Signal Name that
  eliminates the runner-up; whether hypothesis outcome held or required revision]
```

```
PHASE OUTPUTS — DELIBERATE PHASE
(C-25: self-labeled; phase footer)

Outputs produced:
  - Hypothesis closure: [CONFIRMED | WEAKENED | OVERTURNED]
  - Pivot deliberation: 4 modes, tri-part triad each, Evidence Against cited Signal Names
  - Selected mode: [mode]
  - Handoff to DRAFT PHASE: pivot selection + schema team names + DARK SIGNALS table
    Signal Names available for AMEND-A citation
```

DELIBERATE PHASE complete. DRAFT PHASE may now begin.

---

### DRAFT PHASE
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT PHASE)`

Draft YAML. No new scanning or deliberation.

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE PHASE selection]
# hypothesis-outcome: [CONFIRMED | WEAKENED | OVERTURNED]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From SCAN PHASE exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team receives one Inertia Advocate from corps-build.
      teams:
        - name: "[YAML name — exact match SCAN PHASE schema 'YAML name (C-02)']"
          # schema-signal: [SCAN PHASE "Repo signal" value]
          roles:
            - [Named role from SCAN PHASE "Proposed roles (C-04)"]
            - [Named role from SCAN PHASE "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      teams: [...]
```

```
PHASE OUTPUTS — DRAFT PHASE
(C-25: self-labeled; phase footer)

Outputs produced:
  - org.yaml block: [n] groups, [n] teams, exec-office: "[name]"
  - Pivot mode in YAML header: [mode]
  - Hypothesis outcome in YAML header: [CONFIRMED | WEAKENED | OVERTURNED]
  - All team names: [list — must match SCAN PHASE 'YAML name (C-02)' exactly]
  - Handoff to FINALIZE PHASE: YAML complete, AMEND-A must cite DARK SIGNALS Signal Name
```

DRAFT PHASE complete. FINALIZE PHASE may now begin.

---

### FINALIZE PHASE
`(C-25: self-labeled; C-14+C-30+C-33 satisfier)`

Verify and provide amend options. AMEND-A cites a DARK SIGNALS Evidence Table "Signal Name"
value as the basis for the alternative mode (C-37 amend satisfier).

#### Post-Write Verification `(C-25: self-labeled; C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — FINALIZE PHASE
(C-30: 10 criteria; C-33: post-YAML bracket; C-34: essential C-02)

[ ] Team names match SCAN schema "YAML name (C-02)"                      STATUS: [CONFIRMED/FAIL]
[ ] Teams have 2+ named roles, no generics (C-04)                        STATUS: [CONFIRMED/FAIL]
[ ] exec-office present (C-07)                                           STATUS: [CONFIRMED/FAIL]
[ ] Group container present (C-03)                                       STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content anywhere (C-05)                             STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team + group level (C-24)                        STATUS: [CONFIRMED/FAIL]
[ ] Tri-part deliberation with hypothesis closure (C-27)                 STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                            STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS table with Hypothesis Relation column (C-36)            STATUS: [CONFIRMED/FAIL]
[ ] Evidence Against + AMEND-A cite table Signal Names (C-37)            STATUS: [CONFIRMED/FAIL]

C-30: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37 — 10 criteria.
C-34: essential C-02 alongside 9 aspirational.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16; C-37: AMEND-A cites DARK SIGNALS Signal Name)`

```
AMEND-A: Switch pivot mode
  Current: [DELIBERATE PHASE mode] | Hypothesis: [CONFIRMED | WEAKENED | OVERTURNED]
  DARK SIGNALS table basis: [Signal Name] Found?=N — [mode] eliminated.
  If hypothesis was OVERTURNED: [Signal Name] caused revision; alternative is [mode].
  Debt if skipped: corps-build, corps-pr, corps-committee, corps-rob inherit misaligned
    clustering; table evidence documented but not acted on.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [SCAN PHASE inference or "no signal"]
  Debt if skipped: propagates into corps-rob + corps-committee templates verbatim.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Principle: [pivot + schema clustering]
  Debt if skipped: Inertia Advocate frames misaligned across groups; corps-committee coherence
    degrades over all review cycles.
  Command: /corps-scan --groups "[description]"
```

```
PHASE OUTPUTS — FINALIZE PHASE
(C-25: self-labeled; phase footer)

Outputs produced:
  - Post-write verification: 10 criteria checked
  - Amend options: 3 (AMEND-A cites DARK SIGNALS Signal Name, AMEND-B exec rename,
    AMEND-C group structure)
  - C-14 satisfied: GATE pre-check (pre-YAML) + this verification (post-YAML)
  - C-33 satisfied: SCAN PHASE header = pre-YAML bracket; this header = post-YAML bracket
  - All phase footers present: GATE + SCAN + DELIBERATE + DRAFT + FINALIZE
```

> "corps-scan complete (R10 V-05). Triple combination: hypothesis-first (pivot hypothesis in
> GATE, hypothesis-relation column in DARK SIGNALS table, closure in DELIBERATE), structured
> evidence table format (Signal Name column as typed citation anchor for C-37), phase output
> footers (PHASE OUTPUTS block at end of each phase naming exact deliverables). AMEND-A cites
> DARK SIGNALS Signal Name. All C-36 and C-37 requirements met. Draft-only."
