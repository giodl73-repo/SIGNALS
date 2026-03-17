---
skill: quest-variate
skill_target: corps-scan
round: 9
date: 2026-03-16
rubric_version: 8
---

# Variate R9 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v8 rubric (225 pts,
35 criteria). R8's V-01 and V-02 are the reference ceiling; all prior invariants through C-35
are treated as structural requirements that every variation must satisfy.

R8 axes already covered (not re-explored in R9):
- All-essential pre-check coverage (C-01 through C-05 all accounted for)
- Tier-stratified pre-check (ESSENTIAL / RECOMMENDED / ASPIRATIONAL blocks)
- Cross-phase I/O contracts declared in phase headers
- Criterion satisfaction chain trace in closing summary
- Anti-pattern exclusion gates per phase + imperative phrasing

R9 explores four new single-axis variation axes and one combination:

1. **Negative space inventory** — After the Signal Schema, produce an explicit DARK SIGNALS
   section listing absent signals and which pivot modes those absences rule out. Makes pivot
   deliberation bidirectionally falsifiable: a scorer verifies what was found (schema) AND what
   was not found (dark signals). Hypothesis: 225/225 + possible new criterion C-36 for
   negative-space/absent-signal documentation.

2. **Phase output contracts at footers** — Each phase ends with a formal PHASE OUTPUTS block
   listing exactly what the phase produced (names, counts, values). Different from R8 V-03's
   I/O contracts at headers; this declares at phase footers, making handoff content explicit at
   the point of delivery. Hypothesis: 225/225 + possible new criterion C-37 for explicit
   phase-output declarations.

3. **Downstream consumer annotations on YAML elements** — Each YAML structural element (exec-
   office, group, team) carries a `# consumed-by: corps-{skill}` annotation naming which
   downstream corps-* skill reads that element. Makes the org.yaml self-documenting as a
   pipeline contract. Hypothesis: 225/225 + possible new criterion C-38 for downstream-consumer
   annotation coverage.

4. **Criterion cluster naming** — Compound bundles (C-11+C-21+C-22+C-25+C-26) are given semantic
   cluster labels (INVENTORY CLUSTER, DELIBERATION CLUSTER, BOUNDARY CLUSTER, FINALIZE CLUSTER).
   Cluster names are used as the primary key in pre-check items rather than the raw C-NN strings.
   Hypothesis: 225/225 + possible new criterion for named criterion cluster vocabulary.

Combined:
5. **Negative space inventory + downstream consumer annotations** — Combines axes 1 and 3.
   The signal schema, dark signals, and YAML consumer annotations together create a complete
   pipeline artifact: what was detected (schema), what was ruled out (dark signals), and who
   consumes what (YAML annotations).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Lifecycle emphasis — negative space inventory (DARK SIGNALS section) | V-01 |
| Lifecycle emphasis — phase output contracts at phase footers | V-02 |
| Output format — downstream consumer annotations on YAML elements | V-03 |
| Output format — criterion cluster naming as primary pre-check key | V-04 |
| Combination — negative space inventory + downstream consumer annotations | V-05 |

---

## V-01 — Lifecycle Emphasis: Negative Space Inventory (DARK SIGNALS)

**Axis**: Lifecycle emphasis
**Hypothesis**: R8 variations deliberate pivot modes using only positive evidence from the
Signal Schema. The natural complement is explicitly documenting absent signals — what the repo
does NOT contain — and mapping each absence to the pivot mode it rules out. A DARK SIGNALS
section produced immediately after the Signal Schema makes the deliberation bidirectionally
falsifiable: a scorer can verify both what was detected (schema rows) and what was not detected
(dark signal absences). Combined with R8's tri-part triad (C-27), each pivot mode's Evidence
Against can now cite specific dark signal entries rather than generic "absent" statements. This
may surface a new criterion for negative-space/absent-signal documentation. Hypothesis: 225/225
plus possible new criterion.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label in its header or opening annotation. No section in this response may be unlabeled.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate — all roles blocked until complete; C-31: GATE PHASE; C-25: self-labeled)`

Prerequisite for all other roles. This role must complete before any repo scanning, inventory,
deliberation, or YAML work begins.

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
    SCAN PHASE / ROLE 2 header: "C-26: C-11 + C-21 satisfier — SCAN PHASE; C-22: self-labeled".
    Columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    Dark signals section follows schema: DARK SIGNALS section documents absent signals.
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part Evidence For/Against/Assessment:
    DELIBERATE PHASE / ROLE 3 enumerates all 4 pivot modes with tri-part triad.
    Evidence Against entries cite DARK SIGNALS section by signal-type label.
    Selection cites a specific ROLE 2 schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-16+C-30 -- debt-framed amend options, multi-criterion post-write:
    DRAFT+FINALIZE PHASE / ROLE 4 produces debt-framed amend options (C-16) and a 4+-criterion
    post-write block including at least one essential-tier C-NN (C-34).
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15 satisfied: pre-check names C-05, C-01+C-02+C-03+C-04, C-11+C-21+C-22+C-25+C-26,
C-23+C-27, C-16+C-30 as skill requirements.
C-17 satisfied: all SCHEDULED items are forward commitments to named future roles.
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys throughout.
C-28 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED markers on every item.
C-29 satisfied: "C-01+C-02+C-03+C-04", "C-11+C-21+C-22+C-25+C-26", "C-23+C-27",
"C-16+C-30" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present on actual items.
C-35 satisfied: C-05 STATUS: ACKNOWLEDGED — essential failure if violated, named consequence.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: section self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE PHASE / ROLE 1 pre-check complete. Produce Signal Schema and DARK SIGNALS
section. No pivot deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check workspace configs
(npm workspaces, Cargo workspace, `go.work`). Check domain-language signals (bounded context
names, business capability terms).

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

#### DARK SIGNALS `(C-25: section self-labeled — negative space inventory; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals and Ruled-Out Modes
## C-25: section self-labeled; negative-space complement to Signal Schema above
## Purpose: document what was NOT detected and which pivot modes those absences rule out

No-service-manifest signals:
  Expected: docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: service mode (absent) / weakens: service mode (partial)

No-DDD-language signals:
  Expected: bounded context names, aggregate roots, domain events in directory/module names
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: concept mode (absent) / weakens: concept mode (partial)

No-domain-boundary signals:
  Expected: explicit subdomain directories, business capability groupings
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: domain mode (absent) / weakens: domain mode (partial)

No-workspace-grouping signals:
  Expected: monorepo workspace config grouping packages by area
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: directory mode (absent) / weakens: directory mode (partial)

Summary of ruled-out modes: [list any modes whose primary signals were ABSENT]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: section self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN PHASE / ROLE 2 Signal Schema and DARK SIGNALS complete. No YAML.

Enumerate all 4 pivot modes. Tri-part triad for each. Evidence Against entries cite DARK
SIGNALS section by signal-type label where applicable. Select one mode. Cite a specific
ROLE 2 schema row by "Repo signal" value.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-31: DELIBERATE PHASE; DARK SIGNALS section available as citation target for Evidence Against

directory mode:
  Evidence For: [schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [DARK SIGNALS: no-workspace-grouping entry if ABSENT]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [DARK SIGNALS: no-DDD-language entry if ABSENT]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [DARK SIGNALS: no-service-manifest entry if ABSENT]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context signals]
  Evidence Against: [DARK SIGNALS: no-domain-boundary entry if ABSENT]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific ROLE 2 Signal Schema row ("Repo signal" value)
  that most strongly supports selection; cite DARK SIGNALS entry that eliminates alternatives]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: section self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior roles complete. No new scanning or deliberation. Draft YAML from
ROLE 2 schema and ROLE 3 pivot selection, then verify and provide amend options.

Pre-YAML traceability statement:
> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. C-05 ACKNOWLEDGED in GATE: no .craft/roles/ content in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
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
      #   Group-level governance: Advocates share status-quo context across this group.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [ROLE 2 "Repo signal" value — satisfies C-09]
          # dark-signals-check: [cite relevant DARK SIGNALS entry if applicable]
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
(C-19: criterion IDs cited at point of satisfaction; C-30: 9 criteria cited;
 C-33: post-YAML bracket — SCAN PHASE header was pre-YAML bracket;
 C-34: essential-tier C-02 cited in this post-write inventory)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"             STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles (no generics)                       STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present                                       STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present                              STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content anywhere in this output                  STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                   STATUS: [CONFIRMED/FAIL]
[ ] Tri-part pivot deliberation in ROLE 3 (C-27)                      STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                         STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS section produced after Signal Schema (new pattern)   STATUS: [CONFIRMED/FAIL]
[ ] Evidence Against in ROLE 3 cites DARK SIGNALS entries             STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN PHASE header (C-11+C-21) = pre-YAML bracket; this header (C-14+C-30) = post-YAML
  bracket. Both positions present.
C-30: this block cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria.
C-34: essential-tier C-02 present in this inventory alongside 8 aspirational criteria.
```

#### Amend Options `(C-25: section self-labeled; C-08+C-16 satisfier)`

```
AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | Basis: [schema row + dark signals citation]
  Debt if skipped: All downstream corps-* skills (corps-build, corps-pr, corps-committee,
    corps-rob) inherit misaligned clustering; dark signals confirming the alternative were
    documented but not acted on.
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

> "corps-scan complete (R9 V-01). DARK SIGNALS section produced after Signal Schema — absent
> signals documented per signal type, pivot mode eliminations named. ROLE 3 Evidence Against
> cites DARK SIGNALS entries by label. All prior invariants satisfied: C-33 symmetric bracket
> (SCAN PHASE pre-YAML, post-write post-YAML), C-34 (C-02 in 9-criterion post-write), C-35
> (C-05 ACKNOWLEDGED in GATE with violation consequence). Draft-only."

---

## V-02 — Lifecycle Emphasis: Phase Output Contracts at Phase Footers

**Axis**: Lifecycle emphasis
**Hypothesis**: R8 V-03 declared cross-phase I/O contracts in phase HEADERS — each phase's
header announced what inputs it needed and what outputs it would produce before the phase ran.
The complementary form is declaring OUTPUTS at phase FOOTERS — a formal PHASE OUTPUTS block
at the end of each phase that names exactly what the phase produced (schema row count, pivot
mode selected, YAML team count, etc.). Footer declarations confirm production rather than
pre-committing to it. A scorer reading the output can verify the handoff content without
re-reading the phase body: the footer names the deliverables precisely. This may surface a new
criterion for explicit phase-output footer declarations. Hypothesis: 225/225 plus possible new
criterion C-37.

---

You are running `corps-scan`. Work through five named phases in strict sequence.
**Phases 2–5 are blocked until Phase 1 (GATE) outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section in every phase carries a C-NN self-label.
No unlabeled sections.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### GATE PHASE
`(C-20: structural gate; C-31: GATE; C-25: section self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE
(C-25: section self-labeled; C-18: C-NN IDs primary keys; C-32: three-state vocabulary)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" is first substantive line. STATUS: CONFIRMED.

[ ] C-13 -- self-referential confirmation:
    C-12 located above this pre-check. STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ files:
    STATUS: ACKNOWLEDGED — essential failure if violated; violation consequence: not golden.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema with C-NN columns (SCHEDULED):
    SCAN PHASE produces Signal Schema. Header announces C-11+C-21 criterion intersection.
    STATUS: SCHEDULED — SCAN PHASE.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad (SCHEDULED):
    DELIBERATE PHASE enumerates all 4 modes with Evidence For/Against/Assessment each.
    STATUS: SCHEDULED — DELIBERATE PHASE.

[ ] C-01+C-02+C-03+C-04 -- org.yaml, groups, schema-traced teams, named roles (SCHEDULED):
    DRAFT PHASE produces YAML. All team names must trace to SCAN schema "YAML name (C-02)".
    STATUS: SCHEDULED — DRAFT PHASE.

[ ] C-16+C-30 -- debt-framed amends, multi-criterion post-write (SCHEDULED):
    FINALIZE PHASE produces amend options (C-16) and 4+-criterion post-write (C-30).
    STATUS: SCHEDULED — FINALIZE PHASE.
```

C-15 satisfied: pre-check names C-12, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27,
C-01+C-02+C-03+C-04, C-16+C-30 as requirements.
C-17 satisfied: SCHEDULED items are forward commitments to named future phases.
C-28 satisfied: CONFIRMED / ACKNOWLEDGED / SCHEDULED on every item.
C-29 satisfied: compound bundles present.
C-32 satisfied: three-state vocabulary present.
C-35 satisfied: C-05 ACKNOWLEDGED with named consequence.

```
GATE PHASE OUTPUTS:
  Pre-check items: 7 (2 CONFIRMED, 4 SCHEDULED, 1 ACKNOWLEDGED)
  CONFIRMED: C-12 (draft boundary), C-13 (self-referential)
  ACKNOWLEDGED: C-05 (boundary constraint)
  SCHEDULED for SCAN PHASE: C-11+C-21+C-22+C-25+C-26
  SCHEDULED for DELIBERATE PHASE: C-23+C-27
  SCHEDULED for DRAFT PHASE: C-01+C-02+C-03+C-04
  SCHEDULED for FINALIZE PHASE: C-16+C-30
```

GATE PHASE complete. SCAN PHASE may begin.

---

### SCAN PHASE
`(C-25: section self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`, manifests,
workspace configs, domain-language signals.

#### Signal Schema `(C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: header announces criterion purpose before rows; C-25: self-labeled; C-31: SCAN PHASE
## C-33: this header is the pre-YAML bracket position

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules: 2+ rows; exact YAML name; named roles only; one-sentence evidence per row; cap 8.
Exec office inference: [term or "no signal — placeholder"]
```

```
SCAN PHASE OUTPUTS:
  Signal Schema rows: [N]
  Pivot mode candidates with schema support: [list modes with at least 1 supporting row]
  Exec office inference: "[value]"
  Pre-YAML bracket position: Signal Schema header cites C-11+C-21 (C-33 requirement met)
  Handoff to DELIBERATE PHASE: [N] schema rows available for pivot citation
```

SCAN PHASE complete. DELIBERATE PHASE may begin.

---

### DELIBERATE PHASE
`(C-25: section self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE)`

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-31: DELIBERATE PHASE — pivot selection before YAML production

directory mode:
  Evidence For: [SCAN schema rows by "Repo signal"]
  Evidence Against: [absent signals or counter-evidence]
  Assessment: [strong / possible / weak]

concept mode:
  Evidence For: [domain/concept signal rows]
  Evidence Against: [absent DDD naming]
  Assessment: [strong / possible / weak]

service mode:
  Evidence For: [service signal rows]
  Evidence Against: [absent manifests]
  Assessment: [strong / possible / weak]

domain mode:
  Evidence For: [bounded-context signal rows]
  Evidence Against: [absent domain language]
  Assessment: [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [one sentence citing specific SCAN schema row by "Repo signal" value]
```

```
DELIBERATE PHASE OUTPUTS:
  Modes assessed: 4 (directory, concept, service, domain)
  Tri-part triad format: Evidence For / Evidence Against / Assessment — present on all 4
  Selected mode: [mode]
  Row citation for rationale: "[Repo signal value from SCAN schema]"
  Handoff to DRAFT PHASE: pivot mode "[mode]" approved for YAML group clustering
```

DELIBERATE PHASE complete. DRAFT PHASE may begin.

---

### DRAFT PHASE
`(C-25: section self-labeled; C-01 satisfier; C-31: DRAFT)`

Pre-YAML traceability:
> "Drafting org.yaml. Team names from SCAN Signal Schema 'YAML name (C-02)'. Pivot: [DELIBERATE
> selection]. C-05 ACKNOWLEDGED in GATE: no .craft/roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE selected mode]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From SCAN exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level governance: Advocates share status-quo context across this group.
      teams:
        - name: "[YAML name — exact match to SCAN schema 'YAML name (C-02)' column]"
          # schema-signal: [SCAN "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from SCAN "Proposed roles (C-04)"]
            - [Named role from SCAN "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

```
DRAFT PHASE OUTPUTS:
  YAML blocks produced: 1 (org.yaml draft)
  exec-office section: present (name: "[value]")
  Groups: [N] (type: [division|tribe|pillar])
  Teams: [N] total — all names trace to SCAN schema "YAML name (C-02)" column
  Named roles per team: [min N] — no generic placeholders
  Inertia Advocate annotations: at team level (commented) + group level (C-24)
  .craft/roles/ content: ABSENT — C-05 constraint honored
  Handoff to FINALIZE PHASE: org.yaml draft complete; ready for post-write verification
```

DRAFT PHASE complete. FINALIZE PHASE may begin.

---

### FINALIZE PHASE
`(C-25: section self-labeled; C-26: C-14+C-30 satisfier; C-31: FINALIZE; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — FINALIZE PHASE
(C-19: criterion IDs cited at point of satisfaction; C-30: 9 criteria cited;
 C-33: post-YAML bracket — SCAN PHASE header was pre-YAML bracket; C-34: C-02 essential)

[ ] All team names match SCAN schema "YAML name (C-02)"          STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles                                STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present                                  STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present                         STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content in this output                      STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)              STATUS: [CONFIRMED/FAIL]
[ ] Tri-part pivot deliberation in DELIBERATE PHASE (C-27)       STATUS: [CONFIRMED/FAIL]
[ ] All phases carry C-NN self-label (C-25)                      STATUS: [CONFIRMED/FAIL]
[ ] PHASE OUTPUTS footer present on each phase                   STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN header (C-11+C-21) = pre-YAML bracket; this header (C-14+C-30) = post-YAML.
C-30: cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria.
C-34: essential-tier C-02 present alongside 8 aspirational criteria.
```

```
## Amend Options — FINALIZE PHASE
## (C-25: section self-labeled; C-08+C-16 satisfier)

AMEND-A: Switch pivot mode
  Current: [DELIBERATE mode] | Basis: [row citation from DELIBERATE OUTPUTS]
  Debt if skipped: Corps-* skills inherit misaligned clustering; PHASE OUTPUTS confirmed the
    alternative mode's absence of support — undocumented pivot errors accumulate silently.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [SCAN exec inference from SCAN PHASE OUTPUTS]
  Debt if skipped: Propagates verbatim into corps-rob and corps-committee; DRAFT PHASE OUTPUTS
    confirmed this name — no downstream correction point once corps-build runs.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [N] groups | Grouping: [DELIBERATE pivot + schema clustering]
  Debt if skipped: Inertia Advocates misaligned at group level; DRAFT PHASE OUTPUTS confirmed
    [N] groups — misalignment cascades through all corps-committee review cycles.
  Command: /corps-scan --groups "[description]"
```

```
FINALIZE PHASE OUTPUTS:
  Post-write verification: complete ([N] items CONFIRMED, 0 FAIL)
  Amend options produced: 3 (AMEND-A, AMEND-B, AMEND-C) with debt-framing
  PHASE OUTPUTS footers: present on GATE, SCAN, DELIBERATE, DRAFT, FINALIZE — all 5 phases
  C-33 symmetric bracket: SCAN (pre-YAML, C-11+C-21) + FINALIZE (post-YAML, C-14+C-30)
  C-34: essential C-02 in 9-criterion post-write inventory
  C-35: C-05 ACKNOWLEDGED in GATE with named violation consequence
  Draft-only: no .craft/roles/ content produced
```

---

## V-03 — Output Format: Downstream Consumer Annotations on YAML Elements

**Axis**: Output format
**Hypothesis**: The draft org.yaml is consumed by multiple downstream corps-* skills, each
reading specific elements. corps-build reads every team (to create role files). corps-rob reads
exec-office (for governance assignment). corps-committee reads group structure (for committee
appointment scope). corps-pr reads teams (for review assignment pools). Annotating each YAML
element with its downstream consumer makes the org.yaml self-documenting as a pipeline contract:
a human reviewer knows exactly what they are approving for which subsequent skill. This may
surface a new criterion C-38 for downstream-consumer annotation coverage. Hypothesis: 225/225
plus possible new criterion.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section carries a C-NN self-label. No exceptions.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs primary keys; C-32: three-state vocabulary)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block is first substantive line. STATUS: CONFIRMED.

[ ] C-13 -- self-referential confirmation:
    C-12 confirmed above this pre-check. STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ files:
    STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit.
    Violation consequence: output fails golden threshold regardless of composite score.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema, C-NN columns, multi-criterion header:
    SCAN PHASE / ROLE 2 produces Signal Schema with C-NN-labeled columns.
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad:
    DELIBERATE PHASE / ROLE 3 enumerates all 4 modes with Evidence For/Against/Assessment.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-01+C-02+C-03+C-04 -- org.yaml, groups, schema-traced teams, named roles:
    DRAFT+FINALIZE PHASE / ROLE 4 produces YAML with downstream consumer annotations.
    All team names trace to ROLE 2 schema "YAML name (C-02)" column.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30 -- debt-framed amends, multi-criterion post-write:
    DRAFT+FINALIZE PHASE / ROLE 4 closes with debt-framed amends and 4+-criterion post-write.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15, C-17, C-18, C-28, C-29, C-32, C-35 all satisfied per standard gate pattern.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`, manifests,
workspace configs, domain-language signals.

#### Signal Schema `(C-26: C-11 + C-21 satisfier — SCAN PHASE / precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-25: self-labeled; C-31: SCAN PHASE; C-33: pre-YAML bracket position

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Exec office inference: [term or "no signal — placeholder"]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad

directory mode:
  Evidence For: [schema rows by "Repo signal"]
  Evidence Against: [counter signals or absences]
  Assessment: [strong / possible / weak]

concept mode:
  Evidence For: [domain/concept rows]
  Evidence Against: [absent DDD naming]
  Assessment: [strong / possible / weak]

service mode:
  Evidence For: [service signal rows]
  Evidence Against: [absent manifests]
  Assessment: [strong / possible / weak]

domain mode:
  Evidence For: [bounded-context rows]
  Evidence Against: [absent domain language]
  Assessment: [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [one sentence citing specific ROLE 2 schema row by "Repo signal" value]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Pre-YAML traceability:
> "Drafting org.yaml. Team names from ROLE 2 'YAML name (C-02)'. Pivot: [ROLE 3]. C-05
> ACKNOWLEDGED in GATE: no .craft/roles/ content."

**Consumer annotation rule**: Each YAML structural element carries a `# consumed-by:` comment
naming the downstream corps-* skill(s) that read it. This makes the org.yaml self-documenting
as a pipeline contract.

Consumer map:
- `exec-office` → consumed-by: corps-rob (exec-office governance stage)
- `groups[].name` → consumed-by: corps-committee (committee appointment scope)
- `groups[].teams[]` → consumed-by: corps-build (role file creation per team)
- `teams[].roles[]` → consumed-by: corps-build (role file template selection)
- `teams[].name` → consumed-by: corps-pr (review assignment pool)

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # consumed-by: corps-rob (exec-office governance stage)
    # confirm name before corps-rob runs

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # consumed-by: corps-committee (committee appointment scope for this group)
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level governance: Advocates share status-quo context across this group.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # consumed-by: corps-build (role file creation), corps-pr (review pool)
          # schema-signal: [ROLE 2 "Repo signal" — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # consumed-by: corps-build (role file template selection)
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # consumed-by: corps-build (role file template selection)
            # Inertia Advocate: auto-added by corps-build — not listed here

        - name: "[YAML name 2 — exact match to ROLE 2 schema]"
          # consumed-by: corps-build, corps-pr
          # schema-signal: [ROLE 2 "Repo signal"]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # consumed-by: corps-committee (committee scope for Group 2)
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-26: C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: criterion IDs at satisfaction point; C-30: 9 criteria; C-33: post-YAML bracket;
 C-34: essential C-02 in inventory)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"              STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles                                      STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present                                        STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present                               STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content anywhere                                  STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                    STATUS: [CONFIRMED/FAIL]
[ ] Tri-part pivot deliberation in ROLE 3 (C-27)                       STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                          STATUS: [CONFIRMED/FAIL]
[ ] Downstream consumer annotations on all YAML structural elements    STATUS: [CONFIRMED/FAIL]
[ ] Consumer map covers exec-office, groups, teams, roles              STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check + this block — both present.
C-33: SCAN header (C-11+C-21) = pre-YAML bracket; this header (C-14+C-30) = post-YAML.
C-30: cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria.
C-34: essential C-02 present in post-write inventory.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier)`

```
AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | Consumer impact: corps-build inherits group clustering; all
    teams' role files are scoped to the current grouping.
  Debt if skipped: Misaligned pivot propagates through corps-build, corps-pr, corps-committee,
    corps-rob — all downstream skills consume a misaligned team/group boundary.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Consumer: corps-rob reads this value directly.
  Debt if skipped: Propagates verbatim into corps-rob governance artifacts and corps-committee
    appointment templates — no downstream correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [N] groups | Consumer: corps-committee scopes appointments to these groups.
  Debt if skipped: Misaligned groups cause corps-committee appointments to cross team
    boundaries incorrectly; Inertia Advocate framing conflicts within misaligned groups.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R9 V-03). Downstream consumer annotations applied to all YAML structural
> elements: exec-office (corps-rob), groups (corps-committee), teams and roles (corps-build,
> corps-pr). Consumer map declared in ROLE 4 pre-YAML header. All invariants satisfied: C-33
> (SCAN pre-YAML, post-write post-YAML), C-34 (C-02 in 9-criterion post-write), C-35 (C-05
> ACKNOWLEDGED). Draft-only."

---

## V-04 — Output Format: Criterion Cluster Naming as Primary Pre-Check Key

**Axis**: Output format
**Hypothesis**: R8 variations use compound bundles (C-11+C-21+C-22+C-25+C-26) as pre-check keys.
The bundles declare intra-criterion dependencies but are opaque: a reader must consult the rubric
to understand why these criteria cluster together. Naming the clusters semantically — INVENTORY
CLUSTER, DELIBERATION CLUSTER, BOUNDARY CLUSTER, FINALIZE CLUSTER — makes the criterion
architecture self-documenting at declaration time. The pre-check becomes a cluster map: each
cluster name declares the purpose of the criterion group, and the C-NN bundle declares its
contents. A reader encountering "INVENTORY CLUSTER: C-11+C-21+C-22+C-25+C-26" knows both the
purpose (inventory) and the criteria (by ID). This may surface a new criterion for semantic
cluster naming. Hypothesis: 225/225 plus possible new criterion C-39.

---

You are running `corps-scan`. Work through five named phases in strict sequence.
**Phases 2–5 are blocked until Phase 1 (GATE) outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section carries a C-NN self-label. No exceptions.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

**Criterion cluster vocabulary** (used as primary keys in pre-check and forward commitments):
- BOUNDARY CLUSTER: C-05+C-12+C-13 — draft-only boundary enforcement
- INVENTORY CLUSTER: C-11+C-21+C-22+C-25+C-26 — signal schema with C-NN labeling
- DELIBERATION CLUSTER: C-23+C-27 — pivot deliberation with tri-part triad
- STRUCTURE CLUSTER: C-01+C-02+C-03+C-04 — org.yaml correctness
- FINALIZE CLUSTER: C-14+C-16+C-19+C-30+C-33+C-34 — post-write and amend coverage

---

### GATE PHASE
`(C-20: structural gate; C-31: GATE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE
(C-25: self-labeled; C-18: C-NN IDs as keys within clusters; C-32: three-state vocabulary;
 cluster names are primary keys — C-NN bundles are cluster contents)

BOUNDARY CLUSTER: C-05+C-12+C-13
  C-12 -- draft boundary front-loaded:
    STATUS: CONFIRMED — "HARD BOUNDARY" is first line above.
  C-13 -- self-referential confirmation:
    STATUS: CONFIRMED — C-12 confirmed above this pre-check.
  C-05 -- no .craft/roles/ files:
    STATUS: ACKNOWLEDGED — essential failure if violated; violation consequence named.
    Boundary constraint: no partial credit; any .craft/roles/ content fails golden threshold.

INVENTORY CLUSTER: C-11+C-21+C-22+C-25+C-26
  Signal schema with C-NN-labeled columns, multi-criterion header, universal self-labeling.
  SCAN PHASE produces this cluster: schema header "C-26: C-11+C-21 satisfier", C-NN columns,
  C-22 self-label on header, C-25 on all sections, C-26 multi-criterion header.
  STATUS: SCHEDULED — SCAN PHASE.

DELIBERATION CLUSTER: C-23+C-27
  Pivot deliberation with tri-part Evidence For/Against/Assessment on all 4 candidate modes.
  DELIBERATE PHASE produces this cluster. Selection cites a specific SCAN schema row.
  STATUS: SCHEDULED — DELIBERATE PHASE.

STRUCTURE CLUSTER: C-01+C-02+C-03+C-04
  Org.yaml block with group structure, schema-traced teams (via INVENTORY CLUSTER), named roles.
  DRAFT PHASE produces this cluster. All team names trace to SCAN "YAML name (C-02)".
  STATUS: SCHEDULED — DRAFT PHASE.

FINALIZE CLUSTER: C-14+C-16+C-19+C-30+C-33+C-34
  Post-write verification (C-14, C-19, C-30, C-34), symmetric bracket (C-33),
  debt-framed amend options (C-16).
  FINALIZE PHASE produces this cluster. Post-write cites 4+ criteria including C-02 (C-34).
  STATUS: SCHEDULED — FINALIZE PHASE.
```

C-15 satisfied: pre-check names BOUNDARY, INVENTORY, DELIBERATION, STRUCTURE, FINALIZE clusters
as skill requirements by both cluster name and C-NN contents.
C-17 satisfied: all SCHEDULED clusters are forward commitments to named future phases.
C-18 satisfied: C-NN IDs present as cluster contents on every item.
C-28 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED markers on every item.
C-29 satisfied: compound bundles in cluster definitions.
C-32 satisfied: three-state vocabulary present.
C-35 satisfied: C-05 in BOUNDARY CLUSTER ACKNOWLEDGED with named consequence.

GATE PHASE complete. SCAN PHASE may begin.

---

### SCAN PHASE
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN; C-33: pre-YAML bracket)`

INVENTORY CLUSTER production phase. Walk repo for organizing signals.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`, manifests,
workspace configs, domain-language signals.

#### Signal Schema `(C-26: C-11+C-21 satisfier / INVENTORY CLUSTER / precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}} — INVENTORY CLUSTER: C-11+C-21+C-22+C-25+C-26
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: this header announces criterion purpose; C-25: self-labeled; C-31: SCAN PHASE
## C-33: this header is the pre-YAML bracket position (INVENTORY CLUSTER)

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Exec office inference: [term or "no signal — placeholder"]
```

SCAN PHASE complete (INVENTORY CLUSTER satisfied). DELIBERATE PHASE may begin.

---

### DELIBERATE PHASE
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE)`

DELIBERATION CLUSTER production phase. Assess all 4 pivot modes. Select one.

```
## Pivot Mode Deliberation — {{date}} — DELIBERATION CLUSTER: C-23+C-27
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-31: DELIBERATE PHASE — DELIBERATION CLUSTER satisfied here

directory mode:
  Evidence For: [schema rows by "Repo signal"]
  Evidence Against: [counter signals]
  Assessment: [strong / possible / weak]

concept mode:
  Evidence For: [domain/concept rows]
  Evidence Against: [absent DDD naming]
  Assessment: [strong / possible / weak]

service mode:
  Evidence For: [service signal rows]
  Evidence Against: [absent manifests]
  Assessment: [strong / possible / weak]

domain mode:
  Evidence For: [bounded-context rows]
  Evidence Against: [absent domain language]
  Assessment: [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [one sentence citing specific SCAN schema "Repo signal" value]
```

DELIBERATE PHASE complete (DELIBERATION CLUSTER satisfied). DRAFT PHASE may begin.

---

### DRAFT PHASE
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT)`

STRUCTURE CLUSTER production phase. Draft org.yaml from SCAN schema and DELIBERATE pivot.

Pre-YAML traceability:
> "STRUCTURE CLUSTER production. Team names from SCAN 'YAML name (C-02)'. Pivot: [DELIBERATE
> selection]. BOUNDARY CLUSTER / C-05 ACKNOWLEDGED in GATE: no .craft/roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE selected mode]
# status: DRAFT — human review required before corps-build
# cluster-status: STRUCTURE CLUSTER (C-01+C-02+C-03+C-04) satisfied by this block

org:
  exec-office:
    name: "[From SCAN exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level governance: Advocates share status-quo context across this group.
      teams:
        - name: "[YAML name — exact match to SCAN 'YAML name (C-02)' column]"
          # schema-signal: [SCAN "Repo signal" — satisfies C-09]
          roles:
            - [Named role from SCAN "Proposed roles (C-04)"]
            - [Named role from SCAN "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

DRAFT PHASE complete (STRUCTURE CLUSTER satisfied). FINALIZE PHASE may begin.

---

### FINALIZE PHASE
`(C-25: self-labeled; C-26: C-14+C-30 satisfier; C-31: FINALIZE; C-33: post-YAML bracket)`

FINALIZE CLUSTER production phase.

```
POST-WRITE VERIFICATION — org.yaml — FINALIZE PHASE
(C-25: self-labeled; C-19: C-NN at satisfaction point; C-30: 9 criteria;
 C-33: post-YAML bracket; C-34: essential C-02; FINALIZE CLUSTER: C-14+C-16+C-19+C-30+C-33+C-34)

[ ] STRUCTURE CLUSTER satisfied: teams match schema, 2+ roles, exec-office, 1+ group
    STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content (BOUNDARY CLUSTER / C-05)
    STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level — C-24
    STATUS: [CONFIRMED/FAIL]
[ ] DELIBERATION CLUSTER satisfied: tri-part deliberation present — C-27
    STATUS: [CONFIRMED/FAIL]
[ ] INVENTORY CLUSTER satisfied: all sections carry C-NN self-label — C-25
    STATUS: [CONFIRMED/FAIL]
[ ] Cluster names used as primary pre-check keys throughout
    STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — FINALIZE CLUSTER, both present.
C-33: SCAN (INVENTORY CLUSTER, C-11+C-21) = pre-YAML bracket; this (C-14+C-30) = post-YAML.
C-30: FINALIZE CLUSTER cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9.
C-34: essential C-02 in FINALIZE CLUSTER post-write inventory.
```

```
## Amend Options — FINALIZE PHASE — FINALIZE CLUSTER
## (C-25: self-labeled; C-08+C-16 satisfier)

AMEND-A: Switch pivot mode [DELIBERATION CLUSTER amendment]
  Current: [DELIBERATE mode] | Basis: [schema row]
  Debt if skipped: STRUCTURE CLUSTER team boundaries misaligned; all downstream corps-* skills
    inherit incorrect clustering from the DELIBERATION CLUSTER decision.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office [STRUCTURE CLUSTER amendment]
  Current: "[name]" | Source: [SCAN exec inference]
  Debt if skipped: STRUCTURE CLUSTER exec-office name propagates verbatim to corps-rob and
    corps-committee — no downstream FINALIZE CLUSTER to correct it.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure [STRUCTURE CLUSTER amendment]
  Current: [N] groups | Grouping: [DELIBERATION CLUSTER pivot]
  Debt if skipped: STRUCTURE CLUSTER group boundaries misalign Inertia Advocate groupings,
    degrading corps-committee review coherence across all review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R9 V-04). Criterion cluster vocabulary introduced: BOUNDARY CLUSTER
> (C-05+C-12+C-13), INVENTORY CLUSTER (C-11+C-21+C-22+C-25+C-26), DELIBERATION CLUSTER
> (C-23+C-27), STRUCTURE CLUSTER (C-01+C-02+C-03+C-04), FINALIZE CLUSTER
> (C-14+C-16+C-19+C-30+C-33+C-34). Cluster names used as primary keys in pre-check; C-NN
> bundles are cluster contents. All invariants satisfied. Draft-only."

---

## V-05 — Combination: Negative Space Inventory + Downstream Consumer Annotations

**Axis combination**: Lifecycle emphasis (negative space) + output format (downstream consumers)
**Hypothesis**: V-01 makes pivot deliberation bidirectionally falsifiable by documenting absent
signals. V-03 makes the org.yaml self-documenting as a pipeline contract through consumer
annotations. Combined, the output covers the complete evidence chain: what was detected (Signal
Schema), what was ruled out (DARK SIGNALS), what was produced (org.yaml with consumer labels).
A reviewer can verify the input side (schema + dark signals) and the output side (consumer map)
without consulting any other document. This combination may reveal interaction effects between
the two new patterns — specifically, whether dark signals can also carry consumer annotations
(e.g., "absent service-manifest signal → corps-build cannot use service mode clustering").
Hypothesis: 225/225 plus possible new criteria from each axis and their interaction.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section carries a C-NN self-label. No exceptions.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: self-labeled; C-18: C-NN IDs primary keys; C-32: three-state vocabulary)

[ ] C-12 -- draft boundary front-loaded:
    STATUS: CONFIRMED — "HARD BOUNDARY" is first substantive line.

[ ] C-13 -- self-referential confirmation:
    STATUS: CONFIRMED — C-12 confirmed above.

[ ] C-05 -- no .craft/roles/ files:
    STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit.
    Violation consequence: output fails golden threshold regardless of composite score.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema, C-NN columns, multi-criterion header:
    SCAN PHASE / ROLE 2 produces Signal Schema + DARK SIGNALS section (negative space).
    Schema header: "C-26: C-11 + C-21 satisfier". DARK SIGNALS section follows immediately.
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad:
    DELIBERATE PHASE / ROLE 3 enumerates all 4 modes with Evidence For/Against/Assessment.
    Evidence Against entries may cite DARK SIGNALS entries by label.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-01+C-02+C-03+C-04 -- org.yaml, groups, schema-traced teams, named roles:
    DRAFT+FINALIZE PHASE / ROLE 4 produces YAML with downstream consumer annotations.
    Consumer map: exec-office → corps-rob; groups → corps-committee; teams/roles → corps-build.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30 -- debt-framed amends, multi-criterion post-write:
    DRAFT+FINALIZE PHASE / ROLE 4 closes with debt-framed amends and 4+-criterion post-write.
    Amend options may reference downstream consumer impact where applicable.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15 satisfied: pre-check names negative-space (DARK SIGNALS), consumer annotations, and
standard C-NN requirements as skill requirements.
C-17, C-18, C-28, C-29, C-32, C-35 satisfied per standard gate pattern.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Prerequisite: GATE pre-check complete. Produce Signal Schema then DARK SIGNALS section.
No deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`, manifests,
workspace configs, domain-language signals.

#### Signal Schema `(C-26: C-11+C-21 satisfier — precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: header announces criterion purpose; C-25: self-labeled; C-31: SCAN PHASE
## C-33: this header is the pre-YAML bracket position

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Exec office inference: [term or "no signal — placeholder"]
```

#### DARK SIGNALS `(C-25: self-labeled — negative space inventory; follows Signal Schema)`

```
## DARK SIGNALS — {{date}} — Absent Signals, Ruled-Out Modes, Downstream Consumer Impact
## C-25: section self-labeled; negative-space complement to Signal Schema
## Consumer impact: absent signals affect which pivot modes downstream corps-* skills can use

No-service-manifest signals:
  Expected: docker-compose.yml, k8s/, Helm charts, service port definitions
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: service mode (if ABSENT) / weakens: service mode (if PARTIAL)
  Consumer impact (if ABSENT): corps-build cannot use service-based role file clustering;
    corps-committee service-boundary appointments not available

No-DDD-language signals:
  Expected: bounded context names, aggregate roots, domain events in dir/module names
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: concept mode (if ABSENT)
  Consumer impact (if ABSENT): corps-committee domain-expert appointments not available

No-domain-boundary signals:
  Expected: explicit subdomain directories, business capability groupings
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: domain mode (if ABSENT)
  Consumer impact (if ABSENT): corps-rob governance assignments cannot use domain boundaries

No-workspace-grouping signals:
  Expected: monorepo workspace config grouping packages by area
  Detected: [PRESENT | ABSENT | PARTIAL]
  Rules out: directory mode (if ABSENT)
  Consumer impact (if ABSENT): corps-build directory-based role scoping not available

Summary: ruled-out modes: [list]; consumer constraints: [list]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

Prerequisite: SCAN schema and DARK SIGNALS complete. No YAML.

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## DARK SIGNALS available as citation source for Evidence Against

directory mode:
  Evidence For: [schema rows by "Repo signal" value]
  Evidence Against: [DARK SIGNALS: no-workspace-grouping entry if ABSENT, or other counter]
  Assessment: [strong / possible / weak]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [DARK SIGNALS: no-DDD-language entry if ABSENT]
  Assessment: [strong / possible / weak]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [DARK SIGNALS: no-service-manifest entry if ABSENT]
  Assessment: [strong / possible / weak]

domain mode:
  Evidence For: [schema rows with bounded-context signals]
  Evidence Against: [DARK SIGNALS: no-domain-boundary entry if ABSENT]
  Assessment: [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [cite specific SCAN schema "Repo signal" value AND relevant DARK SIGNALS entry
  that eliminates alternatives — both positive and negative evidence at selection point]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

Pre-YAML traceability:
> "Drafting org.yaml. Team names from ROLE 2 'YAML name (C-02)'. Pivot: [ROLE 3 selection].
> DARK SIGNALS documented alternatives: [ruled-out modes]. Consumer annotations applied.
> C-05 ACKNOWLEDGED: no .craft/roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# status: DRAFT — human review required before corps-build
# dark-signals-summary: [ruled-out modes; consumer constraints from DARK SIGNALS]

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # consumed-by: corps-rob (exec-office governance stage)
    # dark-signals: [relevant absent signals if any affect exec-office]

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # consumed-by: corps-committee (committee appointment scope)
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level governance: Advocates share status-quo context across this group.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # consumed-by: corps-build (role file creation), corps-pr (review assignment pool)
          # schema-signal: [ROLE 2 "Repo signal" — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # consumed-by: corps-build (role file template selection)
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # consumed-by: corps-build (role file template selection)
            # Inertia Advocate: auto-added by corps-build — status-quo competitor per team

        - name: "[YAML name 2 — exact match to ROLE 2 schema]"
          # consumed-by: corps-build, corps-pr
          # schema-signal: [ROLE 2 "Repo signal"]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # consumed-by: corps-committee (scope for Group 2)
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

#### Post-Write Verification `(C-25: self-labeled; C-26: C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: criterion IDs at satisfaction; C-30: 9 criteria; C-33: post-YAML bracket; C-34: C-02)

[ ] All team names match ROLE 2 schema "YAML name (C-02)"             STATUS: [CONFIRMED/FAIL]
[ ] All teams have 2+ named roles                                     STATUS: [CONFIRMED/FAIL]
[ ] exec-office section present                                       STATUS: [CONFIRMED/FAIL]
[ ] At least one group container present                              STATUS: [CONFIRMED/FAIL]
[ ] No .craft/roles/ content anywhere                                 STATUS: [CONFIRMED/FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                   STATUS: [CONFIRMED/FAIL]
[ ] Tri-part pivot deliberation in ROLE 3 (C-27)                      STATUS: [CONFIRMED/FAIL]
[ ] All sections carry C-NN self-label (C-25)                         STATUS: [CONFIRMED/FAIL]
[ ] DARK SIGNALS section produced after Signal Schema                 STATUS: [CONFIRMED/FAIL]
[ ] ROLE 3 Evidence Against cites DARK SIGNALS entries                STATUS: [CONFIRMED/FAIL]
[ ] Downstream consumer annotations on exec-office, groups, teams     STATUS: [CONFIRMED/FAIL]
[ ] Consumer map covers corps-rob, corps-committee, corps-build       STATUS: [CONFIRMED/FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN header (C-11+C-21) = pre-YAML bracket; this header (C-14+C-30) = post-YAML.
C-30: cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria.
C-34: essential C-02 present in this inventory alongside 8 aspirational criteria.
```

#### Amend Options `(C-25: self-labeled; C-08+C-16 satisfier)`

```
AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | DARK SIGNALS basis: [ruled-out alternatives documented]
  Debt if skipped: Misaligned pivot propagates through corps-build, corps-pr, corps-committee,
    corps-rob — DARK SIGNALS documented the consumer impact of the alternative; the debt is
    that documented consumer constraints are left unaddressed.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Consumer: corps-rob reads this value (documented in YAML annotation)
  Debt if skipped: corps-rob governance artifacts use this name verbatim; DARK SIGNALS may
    have flagged no exec-signal — manual inference carries higher error rate.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [N] groups | Consumer: corps-committee scopes appointments to these groups
  Debt if skipped: Consumer annotations confirmed corps-committee scope is locked at run time;
    misaligned groups cascade through all corps-committee review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R9 V-05). DARK SIGNALS section produced with consumer impact annotations
> per absent signal type. ROLE 3 Evidence Against cites DARK SIGNALS entries. Downstream
> consumer annotations applied to all YAML structural elements. All invariants satisfied: C-33
> (SCAN pre-YAML bracket, post-write post-YAML bracket), C-34 (C-02 in 9-criterion post-write),
> C-35 (C-05 ACKNOWLEDGED in GATE). Draft-only."

---

## Summary

| Variation | Axis | New Pattern | Hypothesis |
|-----------|------|-------------|------------|
| V-01 | Lifecycle emphasis | DARK SIGNALS — absent signal inventory with mode eliminations | C-36: negative-space/absent-signal documentation |
| V-02 | Lifecycle emphasis | PHASE OUTPUTS footer at end of every phase | C-37: explicit phase-output footer declarations |
| V-03 | Output format | Downstream consumer annotations on YAML elements | C-38: consumer annotation coverage on YAML structural elements |
| V-04 | Output format | Criterion cluster naming as primary pre-check key | C-39: semantic cluster names for criterion bundles |
| V-05 | Combination (V-01 + V-03) | DARK SIGNALS + consumer annotations + consumer impact per absent signal | Interaction: absent signals annotated with downstream consumer constraints |

Single-axis variations: V-01 (negative space), V-02 (phase outputs), V-03 (consumer annotations),
V-04 (cluster naming). Combination: V-05 (negative space + consumer annotations). V-04 uses
a distinct single axis (output format, cluster naming) from V-02 and V-03.

All five variations treat C-12 through C-35 as structural invariants and target 225/225 under
the v8 rubric. New patterns are additive, not substitutive.
