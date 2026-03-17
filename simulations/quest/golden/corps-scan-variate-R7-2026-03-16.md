---
skill: quest-variate
skill_target: corps-scan
round: 7
date: 2026-03-16
rubric_version: 7
---

# Variate R7 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v7 rubric (210 pts,
32 criteria). R6's top variation (V-01) scored 205/210 under v7; V-02 scored 200/210; V-03
scored existing + C-29 + C-31. The four new criteria separate the R6 variations:

- V-01 earned C-29 + C-30 + C-32 but missed C-31 (role-sequence names carry purpose through
  persona identity, not phase naming).
- V-02 earned C-29 + C-30 but missed C-31 (section numbers) and C-32 (2-state only).
- V-03 earned C-29 + C-31 but missed C-30 (post-write cites C-14 only) and C-32 (2-state only).

R7 targets 210/210 by treating all four as structural invariants. Every variation must include:

- **C-29**: At least 2 pre-check items use compound bundle notation — `C-NN+C-NN+...` on a
  single item. The bundles declare intra-criterion dependencies explicitly at declaration time.
- **C-30**: Post-write block cites 4 or more distinct C-NN criterion IDs simultaneously,
  functioning as a comprehensive satisfaction inventory at the point of YAML closure.
- **C-31**: Structural units named by pipeline function (GATE / SCAN / DELIBERATE / DRAFT /
  FINALIZE or equivalent). Each name encodes purpose before the reader enters the unit.
  Role-persona names (Compliance Officer) and ordinal names (Section 0) do not pass.
- **C-32**: Pre-check uses three-state execution vocabulary: CONFIRMED (already satisfied),
  SCHEDULED (committed to a future unit), ACKNOWLEDGED (constraint recorded, no execution
  commitment). All three states must appear on actual items.

All R6 invariants (C-25 through C-28) and all prior round invariants (C-12 through C-24)
are preserved in all variations.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence — four roles, each named by pipeline phase + persona sub-label | V-01 |
| Output format — five purpose-named sections replacing numbered sections | V-02 |
| Lifecycle emphasis — five-phase pipeline rebuilt with all four new criteria complete | V-03 |
| Role sequence + lifecycle emphasis — five roles named purely by pipeline function | V-04 |
| Phrasing register + inertia framing — imperative voice, Inertia Advocate front-loaded as primary constraint | V-05 |

---

## V-01 — Role Sequence: Four Pipeline-Phase-Named Roles, Three-State Pre-Check, Six-Criterion Post-Write

**Axis**: Role sequence
**Hypothesis**: R6 V-01 scored 205/210 (C-29 + C-30 + C-32, missing only C-31). The role-sequence
frame already satisfies all other R7 criteria. Adding pipeline phase labels to each role header —
so each role name reads as "GATE PHASE / COMPLIANCE OFFICER", "SCAN PHASE / REPO ARCHAEOLOGIST",
etc. — satisfies C-31 by making each unit name encode pipeline position and purpose. The role
personas remain as sub-labels. C-29 (compound bundles), C-30 (6-criterion post-write), and
C-32 (three-state vocabulary) are preserved from R6 V-01. Hypothesis: 210/210.

---

You are running `corps-scan`. Work through four named roles in strict sequence. Do not begin a
role until the prior role is fully complete. **ROLE 2, ROLE 3, and ROLE 4 are blocked until
ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label in its header or opening annotation. No section in this response may be unlabeled.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate — all other roles blocked until complete; C-31: GATE PHASE)`

Prerequisite for all other roles. This role must complete before any repo scan, signal
inventory, pivot deliberation, or YAML work begins. A model following this sequence cannot
reach ROLE 2, ROLE 3, or ROLE 4 without first completing everything in ROLE 1.

Your job: emit the hard boundary declaration, then complete the compliance pre-check using
criterion IDs as primary keys. Three-state execution vocabulary applies to every item:
CONFIRMED (satisfied above this item), SCHEDULED (committed to a named future role),
ACKNOWLEDGED (constraint recorded, no execution commitment in this output).

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state vocabulary on every item)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY (C-12 satisfier)" block above is the first substantive line of this output.
    It precedes this pre-check, all inventory work, all pivot deliberation, and all YAML.
    STATUS: CONFIRMED — draft-only declaration is line 1 of this response.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12 is satisfied. The draft-only statement appears before any inventory,
    deliberation, or YAML content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary; it precedes this pre-check.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated regardless of composite score.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema with C-NN column headers, section self-labeled,
    multi-criterion header (SCHEDULED):
    SCAN PHASE / ROLE 2 produces a Signal Schema whose section header reads
    "C-26: C-11 + C-21 satisfier — SCAN PHASE; C-22: self-labeled". Columns include
    "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation with tri-part Evidence For/Against/Assessment (SCHEDULED):
    DELIBERATE PHASE / ROLE 3 enumerates all 4 pivot modes, each with tri-part triad.
    Selection cites a specific ROLE 2 schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles. Generic placeholders fail.
    STATUS: SCHEDULED — enforced by DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-07 -- exec office present (SCHEDULED):
    org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required in DRAFT+FINALIZE PHASE / ROLE 4 YAML.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 of the 3 amend options name the downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced by DRAFT+FINALIZE PHASE / ROLE 4 amend section.

[ ] C-30 -- post-write multi-criterion declaration (SCHEDULED):
    DRAFT+FINALIZE PHASE / ROLE 4 post-write block cites 4+ C-NN criterion IDs simultaneously.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15 satisfied: pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27,
C-04, C-07, C-16, C-30 as requirements.
C-17 satisfied: C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-04, C-07, C-16, C-30 are forward
commitments (SCHEDULED for future roles).
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys for all items.
C-28 satisfied: SCHEDULED/CONFIRMED markers present on every item.
C-29 satisfied: "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all appear on actual pre-check items.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: section self-labeled; C-11 + C-26 satisfier; C-31: SCAN PHASE)`

Prerequisite: GATE PHASE / ROLE 1 pre-check is complete. No pivot deliberation, no YAML —
signal schema production only.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check workspace configs
(npm workspaces, Cargo workspace, `go.work`). Check domain-language signals (bounded context
names, business capability terms in directory names or module identifiers).

#### Signal Schema `(C-26: C-11 + C-21 satisfier — SCAN PHASE / precedes YAML; C-22: header announces criteria before rows)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: this header announces criterion purpose before any schema rows are written
## C-31: SCAN PHASE — inventory step; no deliberation or YAML in this role

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only (Engineer, PM, Tech Lead, etc.) — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row — no generic phrases.
- Cap at 8 rows. Group weak signals under closest strong signal; note the grouping.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may now begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: section self-labeled; C-23 + C-27 satisfier — tri-part deliberation; C-31: DELIBERATE PHASE)`

Prerequisite: GATE PHASE and SCAN PHASE complete. Signal Schema available. No YAML in this
role — pivot deliberation only.

Assess all four candidate pivot modes against the ROLE 2 Signal Schema. Each candidate carries
three structured entries: Evidence For (specific schema rows by "Repo signal" value), Evidence
Against (absent signals or counter-evidence), Assessment (strong / possible / weak — one
sentence). Select one mode; rationale must cite a specific schema row by "Repo signal" value.

#### Pivot Mode Deliberation `(C-25: section self-labeled; C-27: tri-part Evidence For/Against/Assessment for all candidates)`

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes selection; C-27: tri-part triad
## C-31: DELIBERATE PHASE — no YAML may be written until this deliberation is complete

directory mode:
  Evidence For: [schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [absent or counter-indicating signals from schema]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming or mixed signal types]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent service manifest signals or mixed layout]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context or business-capability signals]
  Evidence Against: [absent domain language in schema rows]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific ROLE 2 schema row (by "Repo signal" value)
  that most strongly favors the selected mode over the highest-scoring alternative]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may now begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: section self-labeled; C-01 satisfier — produces org.yaml; C-31: DRAFT+FINALIZE PHASE)`

Prerequisite: all prior phases complete. Draft-only constraint active. All team names must
trace to ROLE 2 schema "YAML name (C-02)" column. Pivot mode is ROLE 3 selection.

**Pre-YAML traceability statement** (required immediately before YAML block):
> "Drafting org.yaml. All team names from ROLE 2 Signal Schema 'YAML name (C-02)' column.
> Pivot: [ROLE 3 selection]. C-05 active: no .craft/roles/ content in this output."

#### Draft org.yaml `(C-25: section self-labeled; C-01 satisfier — org configuration contract)`

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# schema-rows: [n] signals detected
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate role file from corps-build.
      #   Group-level: Inertia Advocates across this group share governance context and interact
      #   in corps-committee reviews. Wrong grouping = misaligned status-quo arguments.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [ROLE 2 "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build — argues status-quo in team reviews

        - name: "[YAML name 2 — exact match to ROLE 2 schema row]"
          # schema-signal: [ROLE 2 "Repo signal" value]
          roles:
            - [Named role from ROLE 2 schema]
            - [Named role from ROLE 2 schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level governance applies — see Group 1 comment for full rationale.
      teams: [...]
```

#### Post-Write Verification — FINALIZE PHASE `(C-25: section self-labeled; C-26: C-14 + C-30 satisfier — dual-bracket closure with multi-criterion inventory)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction;
 C-30: this block cites 8 criteria simultaneously as comprehensive satisfaction inventory)

[ ] Every team name matches ROLE 2 schema "YAML name (C-02)" row       STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                        STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                        STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                           STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                            STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team level AND group level (C-24)              STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation with tri-part structure in ROLE 3 (C-27)       STATUS: [CONFIRMED / FAIL]
[ ] Every role section carries C-NN self-label (C-25)                 STATUS: [CONFIRMED / FAIL]
[ ] At least one header cites 2+ C-NN IDs (C-26)                      STATUS: [CONFIRMED / FAIL]
[ ] Compound bundle notation in GATE pre-check items (C-29)            STATUS: [CONFIRMED / FAIL]
[ ] Three-state vocabulary in GATE pre-check (C-32)                   STATUS: [CONFIRMED / FAIL]
[ ] Four pipeline-phase-named roles present (C-31)                    STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE PHASE / ROLE 1 pre-check is the pre-YAML gate; this FINALIZE PHASE
block is the post-YAML gate. Both present.
C-30 multi-criterion declaration: this block simultaneously cites C-14, C-02, C-24, C-27,
C-25, C-26, C-29, C-32 at point of satisfaction — 8 criteria declared together.
C-19: criterion IDs cited at point of satisfaction in this post-write block.
```

#### Amend Options `(C-25: section self-labeled; C-08 + C-16 satisfier — debt-framed options)`

```
## Amend Options — DRAFT+FINALIZE PHASE / ROLE 4
## (C-25: section self-labeled; C-16: debt-framing on each option below)

AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | Deliberation basis: [ROLE 3 selected row citation]
  Debt if skipped: Wrong pivot mode clusters schema rows by the wrong organizing dimension.
    All corps-build role files, corps-pr routing, corps-committee composition, and corps-rob
    ownership chains inherit the misalignment without a correction point downstream.
  Alternative: [mode from ROLE 3 deliberation] | Evidence: [ROLE 3 row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [ROLE 2 exec inference note]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill corrects an incorrect exec-office name — correction requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping principle: [ROLE 3 pivot + schema clustering]
  Debt if skipped: Misaligned groups co-locate Inertia Advocates whose status-quo frames
    conflict, degrading corps-committee review signal coherence across all review cycles.
  Alternatives: flatten / split / add cross-cutting platform pillar per schema row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R7 V-01). Phases: GATE (ROLE 1) → SCAN (ROLE 2) → DELIBERATE (ROLE 3)
> → DRAFT+FINALIZE (ROLE 4). C-31: all roles named by pipeline phase + persona sub-label.
> C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED three-state in GATE pre-check. C-29: compound bundles
> 'C-11+C-21+C-22+C-25+C-26' and 'C-23+C-27' in GATE pre-check. C-30: post-write cites C-14,
> C-02, C-24, C-27, C-25, C-26, C-29, C-32 (8 criteria) simultaneously. SCAN: [n] schema rows.
> DELIBERATE: [mode] selected. DRAFT: [n] groups, [n] teams, exec '[name]'. Draft-only."

---

## V-02 — Output Format: Five Purpose-Named Sections, Three-State Pre-Check, Eight-Criterion Post-Write

**Axis**: Output format
**Hypothesis**: R6 V-02 scored 200/210 (C-29 + C-30, missing C-31 + C-32). The section-numbered
format can satisfy C-31 by replacing "Section 0/1/2/3/4/5" with "GATE SECTION / SCAN SECTION /
DELIBERATE SECTION / DRAFT SECTION / FINALIZE SECTION" — purpose-named units that encode
pipeline position and function. Adding ACKNOWLEDGED as a third state alongside SCHEDULED and
CONFIRMED satisfies C-32. C-29 (compound bundles) and C-30 (6+ criterion post-write) are
preserved from R6 V-02. Hypothesis: 210/210.

---

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### GATE SECTION
`(C-20: structural gate — all sections blocked until this section completes; C-31: GATE)`

This section is owned by the Compliance Officer function. All subsequent sections are blocked
until this pre-check is fully output.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE SECTION
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state execution vocabulary on every item)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY (C-12 satisfier)" block above is the first substantive line of this output.
    STATUS: CONFIRMED — precedes this pre-check and all subsequent sections.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12. The draft-only statement appears before any inventory, deliberation,
    or YAML content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary above.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated; constraint recorded.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema, C-NN column headers, self-labeled,
    multi-criterion header (SCHEDULED):
    SCAN SECTION header will read "C-26: C-11 + C-21 satisfier — SCAN SECTION; C-22: self-labeled",
    satisfying C-22 (pre-write self-labeling), C-25 (universal labeling), and C-26 (multi-criterion
    header) simultaneously. Columns: "YAML name (C-02)", "Proposed roles (C-04)",
    "Detection evidence (C-09)".
    STATUS: SCHEDULED — satisfied by SCAN SECTION.

[ ] C-23+C-27 -- pivot deliberation, tri-part Evidence For/Against/Assessment (SCHEDULED):
    DELIBERATE SECTION header will read "C-25: C-23 + C-27 satisfier". Each candidate pivot
    mode carries Evidence For / Evidence Against / Assessment. Selection cites a specific
    SCAN SECTION schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by DELIBERATE SECTION.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles. No generics.
    STATUS: SCHEDULED — enforced in DRAFT SECTION.

[ ] C-07 -- exec office present (SCHEDULED):
    org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required element in DRAFT SECTION.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced in FINALIZE SECTION.

[ ] C-30 -- post-write multi-criterion declaration (SCHEDULED):
    FINALIZE SECTION post-write block cites 4+ C-NN criterion IDs simultaneously.
    STATUS: SCHEDULED — satisfied by FINALIZE SECTION.
```

C-15 satisfied: pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27,
C-04, C-07, C-16, C-30.
C-17 satisfied: 6 SCHEDULED items are forward commitments to named future sections.
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys for all items.
C-28 satisfied: SCHEDULED / CONFIRMED markers present on every item.
C-29 satisfied: "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all appear on actual pre-check items.

GATE SECTION complete. SCAN SECTION may proceed.

---

### SCAN SECTION
`(C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled; C-31: SCAN)`

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests, workspace configs. For each detected organizing signal, add one row. Every
team area in the YAML must match a "YAML name (C-02)" cell exactly. This section self-labels
per C-22; the header above declares both C-11 and C-21 as simultaneous satisfiers (C-26).

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-25: section self-labeled; C-31: SCAN SECTION — inventory precedes deliberation and YAML

| Repo signal       | Signal type              | YAML name (C-02) | Proposed roles (C-04)       | Detection evidence (C-09)     |
|-------------------|--------------------------|------------------|-----------------------------|-------------------------------|
| [path/name]       | [dir/service/domain/cfg] | [exact YAML key] | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]             | [...]                    | [...]            | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer than 2 signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only — Engineer, PM, Tech Lead, QA, etc.
- "Detection evidence (C-09)": one sentence of repo evidence — no generic phrases.
- Cap at 8 rows. Group weak signals; note the grouping.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

SCAN SECTION complete. DELIBERATE SECTION may proceed.

---

### DELIBERATE SECTION
`(C-25: C-23 + C-27 satisfier — tri-part pivot deliberation; C-31: DELIBERATE)`

Before selecting a pivot mode, enumerate all candidates using the tri-part structure. Selection
rationale must cite a specific SCAN SECTION schema row by "Repo signal" value.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-27: tri-part triad required for every candidate
## C-31: DELIBERATE SECTION — selection must precede DRAFT SECTION

directory mode:
  Evidence For: [SCAN SECTION schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [absent or counter-indicating signals from schema]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming or mixed signal types]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent service manifest signals or mixed directory layout]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context or business-capability signals]
  Evidence Against: [absent domain language in schema rows]
  Assessment: [strong / possible / weak — one sentence]

Selected mode: [mode]
Rationale: [one sentence citing the specific SCAN SECTION schema row (by "Repo signal" value)
  that most strongly favors the selected mode over the highest-scoring alternative]
```

DELIBERATE SECTION complete. DRAFT SECTION may proceed.

---

### DRAFT SECTION
`(C-25: C-01 satisfier — org configuration contract; C-31: DRAFT)`

**Pre-YAML authority statement** (required immediately before YAML block):
> "Writing org.yaml. All YAML team names are exact matches to SCAN SECTION schema 'YAML name
> (C-02)' column. Schema has [n] rows. Pivot: [DELIBERATE SECTION selection]. C-05 active: no
> .craft/roles/ content in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE SECTION selected mode]
# schema-rows: [n] signals — all team names from SCAN SECTION "YAML name (C-02)" column
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From SCAN SECTION exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate role file from corps-build.
      #   Group-level: Inertia Advocates share governance context; interact in corps-committee
      #   reviews. Wrong grouping = misaligned status-quo arguments across teams.
      teams:
        - name: "[YAML name — exact match to SCAN SECTION schema 'YAML name (C-02)' column]"
          # schema-signal: [SCAN SECTION "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from SCAN SECTION "Proposed roles (C-04)" column]
            - [Named role from SCAN SECTION "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build — argues status-quo in team reviews

        - name: "[YAML name 2 — exact match to SCAN SECTION schema row]"
          # schema-signal: [SCAN SECTION "Repo signal" value]
          roles:
            - [Named role from SCAN SECTION schema]
            - [Named role from SCAN SECTION schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      teams: [...]
```

DRAFT SECTION complete. FINALIZE SECTION may proceed.

---

### FINALIZE SECTION
`(C-25: section self-labeled; C-14 + C-19 + C-30 satisfier — dual-bracket closure; C-31: FINALIZE)`

#### Post-Write Verification `(C-26: C-14 + C-30 satisfier — dual-bracket post gate with multi-criterion inventory)`

```
POST-WRITE VERIFICATION — org.yaml — FINALIZE SECTION
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction;
 C-30: this block cites 8 criteria simultaneously as comprehensive satisfaction inventory)

[ ] Every team name matches SCAN SECTION schema "YAML name (C-02)" row  STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                         STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                          STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                            STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                             STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team level AND group level (C-24)               STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation with tri-part structure in DELIBERATE (C-27)    STATUS: [CONFIRMED / FAIL]
[ ] Every section carries C-NN self-label (C-25)                       STATUS: [CONFIRMED / FAIL]
[ ] At least one header cites 2+ C-NN IDs (C-26)                       STATUS: [CONFIRMED / FAIL]
[ ] Compound bundle notation in GATE pre-check (C-29)                  STATUS: [CONFIRMED / FAIL]
[ ] Three-state vocabulary in GATE pre-check (C-32)                    STATUS: [CONFIRMED / FAIL]
[ ] Five purpose-named sections present (C-31)                         STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE SECTION pre-check is the pre-YAML gate; this FINALIZE SECTION is the
post-YAML gate. Both present.
C-30 multi-criterion declaration: this block simultaneously cites C-14, C-02, C-24, C-27,
C-25, C-26, C-29, C-32 at point of satisfaction — 8 criteria declared together.
C-19: criterion IDs cited at point of satisfaction in this post-write block.
```

#### Amend Options `(C-25: section self-labeled; C-26: C-08 + C-16 satisfier — debt-framed options)`

```
## Amend Options — FINALIZE SECTION
## (C-25: section self-labeled; C-26: this section satisfies C-08 + C-16 simultaneously)

AMEND-A: Switch pivot mode
  Current: [DELIBERATE SECTION mode] | Deliberation basis: [selected row citation]
  Debt if skipped: Wrong pivot mode clusters schema rows by the wrong organizing dimension.
    All corps-build role files, corps-pr routing, corps-committee composition, and corps-rob
    ownership chains inherit the misalignment without a correction point downstream.
  Alternative: [mode from deliberation] | Evidence: [DELIBERATE SECTION row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [SCAN SECTION exec inference note]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill corrects it — correction requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping principle: [DELIBERATE SECTION pivot + clustering]
  Debt if skipped: Misaligned groups co-locate Inertia Advocates with conflicting status-quo
    frames, degrading corps-committee review signal coherence across all review cycles.
  Alternatives: flatten / split / add cross-cutting platform pillar per schema row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R7 V-02). Sections: GATE → SCAN → DELIBERATE → DRAFT → FINALIZE.
> C-31: all sections named by pipeline function. C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED in GATE.
> C-29: compound bundles in GATE pre-check. C-30: FINALIZE post-write cites 8 criteria simultaneously.
> SCAN: [n] schema rows. DELIBERATE: [mode] selected. DRAFT: [n] groups, [n] teams, exec '[name]'.
> Draft-only: no role files written."

---

## V-03 — Lifecycle Emphasis: Five-Phase Pipeline Rebuilt Complete with All Four New Criteria

**Axis**: Lifecycle emphasis
**Hypothesis**: R6 V-03 scored (existing + C-29 + C-31) but missed C-30 and C-32. The 5-phase
lifecycle frame is the organizing axis. Adding ACKNOWLEDGED as a third state to the GATE PHASE
pre-check satisfies C-32. Adding a FINALIZE PHASE post-write block that explicitly names 4+
criteria simultaneously satisfies C-30. Both are contained additions that preserve the lifecycle
emphasis — every phase is named by pipeline function, every phase boundary is explicit, and the
execution sequence is the primary structural element. Hypothesis: 210/210.

---

You are running `corps-scan`. Execute exactly five phases in sequence. Each phase name encodes
its pipeline purpose — do not begin a phase until the prior phase output is complete.

**Pipeline sequence (C-31)**: GATE PHASE → SCAN PHASE → DELIBERATE PHASE → DRAFT PHASE → FINALIZE PHASE

**Universal labeling rule (C-25)**: Every section produced in any phase must carry a C-NN
self-label. No section may be unlabeled.

---

### GATE PHASE
`(C-20: structural gate; C-31: pipeline entry point — all subsequent phases blocked until GATE PHASE produces its pre-check)`

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state execution vocabulary on every item)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY (C-12 satisfier)" block is the first substantive line of this output.
    It precedes SCAN PHASE, DELIBERATE PHASE, DRAFT PHASE, and FINALIZE PHASE.
    STATUS: CONFIRMED — boundary declared before any phase work begins.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12 is satisfied. The draft-only statement precedes all inventory,
    deliberation, and YAML content.
    STATUS: CONFIRMED — C-12 is the opening boundary; this item confirms it.

[ ] C-05 -- no .craft/roles/ files:
    corps-scan is a draft-only skill. No role files, role file content, or role-creation
    instructions may appear anywhere in this output.
    STATUS: ACKNOWLEDGED — essential failure constraint; violation invalidates the output.

[ ] C-10 -- Inertia Advocate noted:
    The output will note at least once that Inertia Advocate is auto-included per team when
    corps-build runs.
    STATUS: ACKNOWLEDGED — noted as constraint; satisfied by YAML comments in DRAFT PHASE.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema with C-NN column headers, self-labeled,
    multi-criterion header (SCHEDULED):
    SCAN PHASE produces a Signal Schema. The schema section header reads "C-26: C-11 + C-21
    satisfier — SCAN PHASE; C-22: self-labeled", satisfying C-22, C-25, and C-26 simultaneously.
    Columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    STATUS: SCHEDULED — satisfied by SCAN PHASE.

[ ] C-23+C-27 -- pivot deliberation with tri-part candidate assessment (SCHEDULED):
    DELIBERATE PHASE enumerates all 4 pivot modes with Evidence For / Evidence Against /
    Assessment triad. Selection cites a specific SCAN PHASE schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area lists 2+ named roles. No generic placeholders.
    STATUS: SCHEDULED — enforced in DRAFT PHASE.

[ ] C-07 -- exec office present (SCHEDULED):
    org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required in DRAFT PHASE.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced in FINALIZE PHASE.

[ ] C-30 -- post-write multi-criterion declaration (SCHEDULED):
    FINALIZE PHASE post-write block cites 4+ C-NN criterion IDs simultaneously.
    STATUS: SCHEDULED — satisfied by FINALIZE PHASE post-write block.
```

C-15 satisfied: pre-check names C-12, C-13, C-05, C-10, C-11+C-21+C-22+C-25+C-26,
C-23+C-27, C-04, C-07, C-16, C-30.
C-17 satisfied: SCAN, DELIBERATE, DRAFT, FINALIZE PHASE items are forward commitments.
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys for all items.
C-28 satisfied: SCHEDULED / CONFIRMED markers present on every item.
C-29 satisfied: "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all appear on actual pre-check items.

GATE PHASE complete. SCAN PHASE may begin.

---

### SCAN PHASE
`(C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled; C-31: inventory step)`

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs (`go.work`,
npm workspaces, Cargo workspace). Capture each organizing signal as one schema row.

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: this header announces criterion purpose before any schema rows are written
## C-31: SCAN PHASE — produces inventory feeding both DELIBERATE PHASE and DRAFT PHASE

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only (Engineer, PM, Tech Lead, etc.) — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row — no generic phrases.
- Cap at 8 rows. Group weak signals under closest strong signal; note the grouping.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

SCAN PHASE complete. DELIBERATE PHASE may begin.

---

### DELIBERATE PHASE
`(C-25: C-23 + C-27 satisfier — tri-part pivot deliberation; C-31: selection step — no YAML before this phase completes)`

Before selecting a pivot mode, enumerate all candidates using the tri-part structure. Selection
rationale must cite a specific SCAN PHASE schema row by "Repo signal" value.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-27: tri-part triad required for every candidate
## C-31: DELIBERATE PHASE — pivot selection must precede DRAFT PHASE

directory mode:
  Evidence For: [SCAN PHASE schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [absent or counter-indicating signals from schema]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming or mixed signal types]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent service manifest signals or mixed layout]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context or business-capability signals]
  Evidence Against: [absent domain language in schema rows]
  Assessment: [strong / possible / weak — one sentence]

Selected mode: [mode]
Rationale: [one sentence citing the specific SCAN PHASE schema row (by "Repo signal" value)
  that most strongly favors the selected mode over the highest-scoring alternative]
```

DELIBERATE PHASE complete. DRAFT PHASE may begin.

---

### DRAFT PHASE
`(C-25: C-01 satisfier — org configuration contract; C-31: YAML production step)`

**Pre-YAML authority statement** (required immediately before YAML block):
> "Writing org.yaml. All team names from SCAN PHASE schema 'YAML name (C-02)' column.
> Schema has [n] rows. Pivot: [DELIBERATE PHASE selection]. C-05 active: no .craft/roles/ output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE PHASE selected mode]
# schema-rows: [n] signals
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From SCAN PHASE exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate role file from corps-build.
      #   Group-level: Inertia Advocates share governance context; interact in corps-committee
      #   reviews. Wrong grouping = misaligned status-quo frames across teams.
      teams:
        - name: "[YAML name — exact match to SCAN PHASE schema 'YAML name (C-02)' column]"
          # schema-signal: [SCAN PHASE "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from SCAN PHASE "Proposed roles (C-04)" column]
            - [Named role from SCAN PHASE "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build (C-10)

        - name: "[YAML name 2]"
          # schema-signal: [SCAN PHASE "Repo signal" value]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same governance structure as Group 1.
      teams: [...]
```

DRAFT PHASE complete. FINALIZE PHASE may begin.

---

### FINALIZE PHASE
`(C-25: section self-labeled; C-14 + C-19 + C-30 satisfier — post-YAML gate and multi-criterion declaration; C-31: pipeline closure step)`

#### Post-Write Verification `(C-26: C-14 + C-30 satisfier — dual-bracket closure with 8-criterion inventory)`

```
POST-WRITE VERIFICATION — org.yaml — FINALIZE PHASE
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction;
 C-30: this block declares simultaneous satisfaction of 8 criteria)

[ ] Every team name matches SCAN PHASE schema "YAML name (C-02)" row   STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                        STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                         STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                           STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content anywhere in output                        STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team level AND group level (C-24)              STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation with tri-part structure (C-27)                  STATUS: [CONFIRMED / FAIL]
[ ] Every section carries C-NN self-label (C-25)                      STATUS: [CONFIRMED / FAIL]
[ ] At least one header cites 2+ C-NN IDs (C-26)                      STATUS: [CONFIRMED / FAIL]
[ ] Compound bundle notation in GATE pre-check (C-29)                  STATUS: [CONFIRMED / FAIL]
[ ] Three-state vocabulary in GATE pre-check (C-32)                   STATUS: [CONFIRMED / FAIL]
[ ] Five pipeline-named phases present (C-31)                         STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE PHASE pre-check is the pre-YAML gate; this FINALIZE PHASE block is
the post-YAML gate. Both present.
C-30 multi-criterion declaration: this block simultaneously declares C-14, C-02, C-24, C-27,
C-25, C-26, C-29, C-32 satisfied — 8 criteria cited at point of satisfaction.
C-19: criterion IDs cited at point of satisfaction in this post-write block.
```

#### Amend Options `(C-25: section self-labeled; C-08 + C-16 satisfier — debt-framed options)`

```
## Amend Options — FINALIZE PHASE
## (C-25: section self-labeled; C-16: debt-framing on each option below)

AMEND-A: Switch pivot mode
  Current: [DELIBERATE PHASE mode] | Deliberation basis: [selected row citation]
  Debt if skipped: Wrong pivot mode clusters schema rows by the wrong organizing dimension.
    corps-build role files, corps-pr routing, corps-committee composition, and corps-rob
    ownership chains all inherit the misalignment. No downstream corps-* skill corrects it.
  Alternative: [mode from deliberation] | Evidence: [DELIBERATE PHASE row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [SCAN PHASE exec inference]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    committee appointment templates, and review authority chains. Correction requires
    re-running corps-scan — no downstream skill corrects it.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping: [DELIBERATE PHASE pivot + schema clustering]
  Debt if skipped: Misaligned groups co-locate Inertia Advocates with conflicting status-quo
    frames, degrading corps-committee review signal coherence across all cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R7 V-03). Phases: GATE → SCAN → DELIBERATE → DRAFT → FINALIZE.
> C-31: phase names encode pipeline purpose. C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED in GATE.
> C-29: compound bundles in GATE pre-check. C-30: FINALIZE post-write cites 8 criteria simultaneously.
> SCAN: [n] schema rows. DELIBERATE: [mode]. DRAFT: [n] groups, [n] teams, exec '[name]'. Draft-only."

---

## V-04 — Role Sequence + Lifecycle Emphasis: Five Roles Named Purely by Pipeline Function

**Axis**: Role sequence + Lifecycle emphasis
**Hypothesis**: V-01 names roles by persona (Compliance Officer, Repo Archaeologist, etc.) with
phase labels appended. V-03 uses pipeline phases without explicit role separation. V-04 uses
five roles named purely by pipeline function — GATE ROLE, SCAN ROLE, DELIBERATE ROLE, DRAFT
ROLE, FINALIZE ROLE — where the role name IS the phase name with no persona sub-label. A fifth
standalone FINALIZE ROLE (separate from DRAFT ROLE) gives post-write verification structural
isolation: the FINALIZE ROLE's sole job is C-30 (multi-criterion post-write) and C-08/C-16
(amend section). This isolation makes C-30 ownership explicit and auditable independent of YAML
production. Hypothesis: clean five-role separation with FINALIZE as sole C-30 owner reaches 210/210.

---

You are running `corps-scan`. Execute five pipeline roles in strict sequence. Each role name
encodes its pipeline position and function. Do not begin a role until the prior role's output
is complete.

**Execution sequence (C-31)**: GATE ROLE → SCAN ROLE → DELIBERATE ROLE → DRAFT ROLE → FINALIZE ROLE

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN self-label.

---

### GATE ROLE
`(C-20: structural gate — all roles blocked until GATE ROLE output is complete; C-31: GATE)`

Sole job: emit hard boundary, complete compliance pre-check using three-state vocabulary.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

```
COMPLIANCE PRE-CHECK — GATE ROLE
(C-25: section self-labeled; C-18: C-NN IDs are primary keys;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state vocabulary on every item)

[ ] C-12 -- draft boundary front-loaded:
    HARD BOUNDARY above is line 1 of this output, before any role work.
    STATUS: CONFIRMED — precedes all subsequent role outputs.

[ ] C-13 -- self-referential confirmation:
    Confirms C-12 is satisfied. Draft-only statement precedes inventory, deliberation, YAML.
    STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ files:
    Essential constraint: no role files, role file content, or role-creation instructions.
    STATUS: ACKNOWLEDGED — violation invalidates output regardless of other scores.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema with C-NN column headers, section self-labeled,
    multi-criterion header (SCHEDULED):
    SCAN ROLE produces a Signal Schema. Header reads "C-26: C-11 + C-21 satisfier — SCAN ROLE;
    C-22: self-labeled". Columns: "YAML name (C-02)", "Proposed roles (C-04)",
    "Detection evidence (C-09)".
    STATUS: SCHEDULED — owned by SCAN ROLE.

[ ] C-23+C-27 -- pivot deliberation with tri-part Evidence For/Against/Assessment (SCHEDULED):
    DELIBERATE ROLE enumerates all 4 pivot modes with tri-part structure. Selection cites
    a specific SCAN ROLE schema row by "Repo signal" value.
    STATUS: SCHEDULED — owned by DELIBERATE ROLE.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team lists 2+ named roles. No generics.
    STATUS: SCHEDULED — enforced by DRAFT ROLE.

[ ] C-07 -- exec office present (SCHEDULED):
    org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required in DRAFT ROLE YAML.

[ ] C-16+C-08 -- debt-framed amend options (SCHEDULED):
    Three amend options, each naming downstream organizational debt if skipped.
    STATUS: SCHEDULED — owned exclusively by FINALIZE ROLE.

[ ] C-30 -- post-write multi-criterion declaration (SCHEDULED):
    FINALIZE ROLE post-write block cites 4+ C-NN criterion IDs simultaneously.
    STATUS: SCHEDULED — owned exclusively by FINALIZE ROLE.
```

C-15 satisfied: pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27,
C-04, C-07, C-16+C-08, C-30.
C-17 satisfied: SCAN, DELIBERATE, DRAFT, FINALIZE ROLE items are forward commitments.
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys for all items.
C-28 satisfied: SCHEDULED / CONFIRMED markers on every item.
C-29 satisfied: "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all appear on actual items.

GATE ROLE complete. SCAN ROLE may begin.

---

### SCAN ROLE
`(C-26: C-11 + C-21 satisfier; C-22: self-labeled; C-31: SCAN)`

Sole job: walk the repo, produce Signal Schema. No deliberation, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests, workspace configs, bounded-context naming.

#### Signal Schema `(C-26: C-11 + C-21 satisfier — precedes YAML; C-22: header announces criteria before rows; C-31: SCAN ROLE output)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN column headers)
## C-25: section self-labeled; C-31: SCAN ROLE — inventory step

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows.
- "YAML name (C-02)": exact string for YAML teams[].name.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence repo evidence per row.
- Cap at 8 rows.

Exec office inference: [schema row suggesting exec title, or "no signal — placeholder"]
```

SCAN ROLE complete. DELIBERATE ROLE may begin.

---

### DELIBERATE ROLE
`(C-25: C-23 + C-27 satisfier; C-31: DELIBERATE — no YAML until this role completes)`

Sole job: enumerate all 4 pivot mode candidates with tri-part structure; select one with row citation.

#### Pivot Mode Deliberation `(C-25: section self-labeled; C-27: tri-part triad for all candidates; C-31: DELIBERATE ROLE output)`

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-27: tri-part required for every candidate
## C-31: DELIBERATE ROLE — selection must precede DRAFT ROLE

directory mode:
  Evidence For: [SCAN ROLE schema rows supporting directory clustering]
  Evidence Against: [absent or counter-indicating schema signals]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming or mixed signal types]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent service manifest signals]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context signals]
  Evidence Against: [absent domain language in schema rows]
  Assessment: [strong / possible / weak — one sentence]

Selected mode: [mode]
Rationale: [one sentence citing specific SCAN ROLE schema row by "Repo signal" value]
```

DELIBERATE ROLE complete. DRAFT ROLE may begin.

---

### DRAFT ROLE
`(C-25: C-01 satisfier — org configuration contract; C-31: DRAFT)`

Sole job: produce the org.yaml. All team names from SCAN ROLE schema "YAML name (C-02)" column.

**Pre-YAML authority statement**:
> "Writing org.yaml. All team names from SCAN ROLE schema. Pivot: [DELIBERATE ROLE selection].
> C-05 active: no .craft/roles/ content."

#### org.yaml `(C-25: section self-labeled; C-01: org configuration contract; C-31: DRAFT ROLE output)`

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE ROLE selected mode]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From SCAN ROLE exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate role file from corps-build.
      #   Group-level: Advocates share governance context; interact in corps-committee reviews.
      #   Wrong grouping = misaligned status-quo frames across teams in this group.
      teams:
        - name: "[YAML name — exact match to SCAN ROLE schema 'YAML name (C-02)']"
          # schema-signal: [SCAN ROLE "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from SCAN ROLE "Proposed roles (C-04)" column]
            - [Named role from SCAN ROLE "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build (C-10)

        - name: "[YAML name 2]"
          # schema-signal: [SCAN ROLE "Repo signal" value]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same governance structure as Group 1.
      teams: [...]
```

DRAFT ROLE complete. FINALIZE ROLE may begin.

---

### FINALIZE ROLE
`(C-25: section self-labeled; C-14 + C-19 + C-30 satisfier — post-YAML gate and multi-criterion declaration; C-31: FINALIZE)`

Sole job: post-write verification with multi-criterion declaration, then amend options.

#### Post-Write Verification `(C-26: C-14 + C-30 satisfier — dual-bracket closure with multi-criterion inventory)`

```
POST-WRITE VERIFICATION — FINALIZE ROLE
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction;
 C-30: this block cites 8 criteria simultaneously as comprehensive satisfaction inventory)

[ ] Team names match SCAN ROLE schema "YAML name (C-02)" exactly  STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (C-04)                          STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present (C-07)                            STATUS: [CONFIRMED / FAIL]
[ ] Group structure present (C-03)                                STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content (C-05)                               STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)               STATUS: [CONFIRMED / FAIL]
[ ] Tri-part pivot deliberation in DELIBERATE ROLE (C-27)         STATUS: [CONFIRMED / FAIL]
[ ] Universal C-NN section labels (C-25)                          STATUS: [CONFIRMED / FAIL]
[ ] Multi-criterion section header present (C-26)                 STATUS: [CONFIRMED / FAIL]
[ ] Compound bundles in GATE ROLE pre-check (C-29)                STATUS: [CONFIRMED / FAIL]
[ ] Three-state vocabulary in GATE ROLE pre-check (C-32)          STATUS: [CONFIRMED / FAIL]
[ ] Five pipeline-named roles present (C-31)                      STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE ROLE pre-check is the pre-YAML gate; this FINALIZE ROLE block is
the post-YAML gate. Both present.
C-30 multi-criterion declaration: this block simultaneously cites C-14, C-02, C-24, C-27,
C-25, C-26, C-29, C-32 at point of satisfaction — 8 criteria declared together.
C-19: criterion IDs named at point of satisfaction in this block.
```

#### Amend Options `(C-25: section self-labeled; C-08 + C-16 satisfier — FINALIZE ROLE output)`

```
## Amend Options — FINALIZE ROLE
## (C-25: self-labeled; C-16: downstream debt named on each option)

AMEND-A: Switch pivot mode
  Current: [DELIBERATE ROLE selection] | Deliberation basis: [row citation]
  Debt if skipped: Wrong pivot mode misaligns all downstream corps-* artifacts — role files,
    PR routing, committee composition, ownership chains — without a correction point.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: SCAN ROLE exec inference
  Debt if skipped: Name propagates verbatim through corps-rob, corps-committee, and authority
    chains. No downstream corps-* skill accepts a correction — requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping: DELIBERATE ROLE pivot + schema clustering
  Debt if skipped: Misaligned groups co-locate Inertia Advocates with conflicting status-quo
    frames, degrading corps-committee review coherence across all review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R7 V-04). 5 roles: GATE → SCAN → DELIBERATE → DRAFT → FINALIZE.
> C-31: roles named by pipeline function. C-32: three-state vocabulary in GATE ROLE.
> C-29: compound bundles in GATE ROLE. C-30: FINALIZE ROLE post-write cites 8 criteria simultaneously.
> SCAN: [n] rows. DELIBERATE: [mode]. DRAFT: [n] groups, [n] teams, exec '[name]'. Draft-only."

---

## V-05 — Phrasing Register + Inertia Framing: Imperative Voice, Inertia Advocate Front-Loaded as Primary Constraint

**Axis**: Phrasing register + Inertia framing
**Hypothesis**: V-01 through V-04 use role-narrative or section-description phrasing
("This role must complete before...", "Walk the repo:"). V-05 uses second-person imperative
throughout ("Emit.", "Produce.", "You will.", "Do not."). The Inertia Advocate is introduced
in the GATE PHASE pre-check as a named primary constraint — not as a YAML comment or footnote —
signaling that every grouping decision has Inertia Advocate coherence consequences before the
scan begins. The structural elements (pipeline phase naming, compound bundles, three-state
vocabulary, multi-criterion post-write) are identical in coverage to V-03 but the phrasing
register makes the imperative-voice variant structurally distinct. Hypothesis: 210/210.

---

You are running `corps-scan`. Five phases. Execute them in order. Do not begin a phase until
the previous phase output is complete.

**Phases (C-31)**: GATE → SCAN → DELIBERATE → DRAFT → FINALIZE

**Label every section (C-25)**: No section in any phase may appear without a C-NN self-label.

---

### GATE PHASE
`(C-20: structural block — emit this before anything else; C-31: GATE)`

Emit the boundary statement first. Then emit the pre-check. Nothing else happens until this
phase is done.

**THIS IS A DRAFT (C-12)**: corps-scan produces org.yaml for human review. You will not write
`.craft/roles/` files, role file content, or role-creation instructions in this output. Ever.

```
GATE PRE-CHECK
(C-25: self-labeled; C-18: C-NN labels are primary keys;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED)

[ ] C-12: Boundary declared before anything else.
    STATUS: CONFIRMED — "THIS IS A DRAFT" is line 1.

[ ] C-13: Confirm C-12.
    The draft-only statement is above this item. It precedes all schema, deliberation, YAML.
    STATUS: CONFIRMED.

[ ] C-05: No .craft/roles/ output.
    You will not produce role files, role content, or role-creation instructions.
    Not in SCAN. Not in DELIBERATE. Not in DRAFT. Not in FINALIZE. Not ever.
    STATUS: ACKNOWLEDGED — permanent boundary; no execution commitment needed.

[ ] C-10: Inertia Advocate is a primary constraint, not a YAML footnote.
    The Inertia Advocate is a status-quo advocacy role that corps-build injects into every team.
    Its coherence depends entirely on correct group structure — co-located Advocates argue
    status-quo together. Misaligned groups produce incoherent status-quo advocacy that degrades
    every corps-committee review cycle downstream. Every grouping decision in DRAFT PHASE has
    Inertia Advocate consequences. You now know this before you scan or group anything.
    STATUS: ACKNOWLEDGED — constraint recorded; you carry it into SCAN and DRAFT.

[ ] C-11+C-21+C-22+C-25+C-26: Produce a labeled signal schema in SCAN PHASE.
    The schema section header must cite C-11 + C-21 simultaneously.
    Columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    STATUS: SCHEDULED — SCAN PHASE.

[ ] C-23+C-27: Enumerate all 4 pivot modes with tri-part structure in DELIBERATE PHASE.
    Evidence For / Evidence Against / Assessment for each mode. Select with a schema row citation.
    STATUS: SCHEDULED — DELIBERATE PHASE.

[ ] C-04+C-07: Named roles per team and exec office in DRAFT PHASE.
    Two or more named roles on every team. Exec-office section present. No generics.
    STATUS: SCHEDULED — DRAFT PHASE.

[ ] C-16+C-08: Debt-framed amend options in FINALIZE PHASE.
    Three amend options, each naming the downstream debt if skipped.
    STATUS: SCHEDULED — FINALIZE PHASE.

[ ] C-30: Multi-criterion post-write declaration in FINALIZE PHASE.
    The post-write block names 4+ C-NN criteria IDs simultaneously at point of satisfaction.
    STATUS: SCHEDULED — FINALIZE PHASE.
```

C-29 satisfied: "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all appear on actual items.

GATE done. Begin SCAN PHASE.

---

### SCAN PHASE
`(C-26: C-11 + C-21 satisfier — schema precedes YAML; C-31: SCAN)`

Walk the repo. Look at everything: top-level directories, `src/`, `services/`, `packages/`,
`apps/`, `modules/`, Docker Compose files, Kubernetes configs, Helm charts, workspace manifests.
Every organizing signal becomes one schema row.

Do not deliberate. Do not write YAML. Produce the schema.

#### Signal Schema `(C-26: C-11 + C-21 satisfier; C-22: header announces criteria before rows; C-31: SCAN PHASE output)`

```
## Signal Schema — {{date}}
## C-26: C-11 (pre-YAML inventory) + C-21 (C-NN column headers) — both satisfied simultaneously
## C-25: self-labeled; C-31: SCAN PHASE

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence of evidence]    |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Minimum 2 rows. Cap at 8. Group weak signals.
"YAML name (C-02)": the exact string you will use in the YAML — do not invent variants later.
"Proposed roles (C-04)": named roles only. "Engineer" yes, "team member" no.
"Detection evidence (C-09)": one sentence, specific repo path or artifact.

Exec office inference: [schema row suggesting exec title, or "no signal — placeholder"]
```

SCAN done. Begin DELIBERATE PHASE.

---

### DELIBERATE PHASE
`(C-25: C-23 + C-27 satisfier; C-31: DELIBERATE — you may not write YAML until this phase is done)`

Enumerate all four pivot modes. Use the tri-part structure for each one. Then select.
Do not guess — cite a schema row.

#### Pivot Deliberation `(C-25: self-labeled; C-27: tri-part required for all candidates; C-31: DELIBERATE PHASE output)`

```
## Pivot Mode Deliberation — {{date}}
## C-25: self-labeled; C-27: tri-part required for every candidate; C-31: DELIBERATE PHASE

directory:
  Evidence For: [schema rows showing clear directory-based organizing principle]
  Evidence Against: [schema rows or absences arguing against directory clustering]
  Assessment: strong / possible / weak

concept:
  Evidence For: [schema rows where "Signal type" = domain or concept]
  Evidence Against: [no DDD naming, no bounded-context signals in schema]
  Assessment: strong / possible / weak

service:
  Evidence For: [schema rows where "Signal type" = service, manifest evidence]
  Evidence Against: [no service manifests, mixed signal types]
  Assessment: strong / possible / weak

domain:
  Evidence For: [schema rows showing business capability names, bounded-context vocabulary]
  Evidence Against: [flat directory layout, no domain language in schema]
  Assessment: strong / possible / weak

Selected: [mode]
Why: [cite the specific SCAN PHASE schema row by "Repo signal" value that tips the selection]
```

DELIBERATE done. Begin DRAFT PHASE.

---

### DRAFT PHASE
`(C-25: C-01 satisfier — write the org.yaml now; C-31: DRAFT)`

Write the org.yaml. Every team name is an exact copy of a "YAML name (C-02)" cell from SCAN
PHASE. Every group gets an Inertia Advocate comment — not as a nicety, as a consequence of
your grouping decision (you understood this in GATE PHASE pre-check item C-10).

State this immediately before the YAML block:
> "org.yaml: [n] teams from SCAN PHASE schema. Pivot: [DELIBERATE PHASE selection].
> C-05 active: no role files."

#### org.yaml `(C-25: self-labeled; C-01: org configuration contract; C-31: DRAFT PHASE output)`

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE PHASE selection]
# status: DRAFT — confirm before running corps-build

org:
  exec-office:
    name: "[SCAN PHASE exec inference, or 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # INERTIA ADVOCATE GOVERNANCE (C-24):
      #   corps-build auto-adds one Inertia Advocate per team in this group.
      #   These Advocates argue status-quo in reviews together — your group structure determines
      #   whether their arguments reinforce or conflict. You chose this grouping; own it.
      teams:
        - name: "[YAML name — verbatim from SCAN PHASE schema 'YAML name (C-02)']"
          # evidence: [SCAN PHASE "Repo signal" — C-09]
          roles:
            - [Named role from SCAN PHASE "Proposed roles (C-04)"]
            - [Named role from SCAN PHASE "Proposed roles (C-04)"]
            # Inertia Advocate: corps-build adds this — do not add it here

        - name: "[YAML name 2]"
          # evidence: [SCAN PHASE "Repo signal"]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: corps-build adds this

    - name: "[Group 2]"
      type: [...]
      # INERTIA ADVOCATE GOVERNANCE (C-24): same — group-level governance applies.
      teams: [...]
```

DRAFT done. Begin FINALIZE PHASE.

---

### FINALIZE PHASE
`(C-25: self-labeled; C-14 + C-19 + C-30 satisfier — close the dual bracket and declare multi-criterion satisfaction; C-31: FINALIZE)`

You are closing the dual bracket. GATE PHASE opened it. This phase closes it. Declare every
criterion you satisfied.

#### Post-Write Check `(C-26: C-14 + C-30 satisfier — dual-bracket closure and 8-criterion inventory)`

```
POST-WRITE — FINALIZE PHASE
(C-25: self-labeled; C-30: 8 criteria declared simultaneously in this block)

[ ] Team names match SCAN PHASE schema exactly (C-02)              STATUS: [CONFIRMED / FAIL]
[ ] 2+ named roles per team (C-04)                                 STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present (C-07)                             STATUS: [CONFIRMED / FAIL]
[ ] Group structure present (C-03)                                 STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content anywhere (C-05)                       STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)               STATUS: [CONFIRMED / FAIL]
[ ] Tri-part deliberation completed (C-27)                        STATUS: [CONFIRMED / FAIL]
[ ] Universal C-NN section labels (C-25)                          STATUS: [CONFIRMED / FAIL]
[ ] Multi-criterion section header (C-26)                         STATUS: [CONFIRMED / FAIL]
[ ] Compound bundles in GATE pre-check (C-29)                     STATUS: [CONFIRMED / FAIL]
[ ] Three-state vocabulary in GATE (C-32)                         STATUS: [CONFIRMED / FAIL]
[ ] Five purpose-named phases (C-31)                              STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE PHASE opened the bracket. This FINALIZE block closes it. Both present.
C-30: this block declares C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32 satisfied
simultaneously — 8 criteria cited at point of satisfaction.
C-19: criterion IDs named at point of satisfaction.
```

#### Amend Options `(C-25: self-labeled; C-08 + C-16 satisfier — three options, each with debt)`

```
## Amend Options
## (C-25: self-labeled; C-16: every option names the downstream debt)

AMEND-A — Switch pivot mode
  You chose: [DELIBERATE PHASE selection]
  If wrong: every corps-* artifact downstream clusters work by the wrong axis. corps-build
    role files, corps-pr routing, corps-committee composition, and corps-rob chains all inherit
    it. There is no correction point after this one.
  Reconsider: [runner-up from DELIBERATE PHASE, row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B — Rename exec office
  You named it: "[name]"
  If wrong: that name appears verbatim in corps-rob governance docs, committee templates, and
    authority chains. No downstream corps-* skill accepts a correction — you must re-run corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C — Adjust groups
  You made: [n] groups — [names]
  If wrong: Inertia Advocates in misaligned groups argue conflicting status-quo frames together.
    corps-committee review signal degrades every cycle until the structure is fixed.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan done (R7 V-05). GATE → SCAN → DELIBERATE → DRAFT → FINALIZE.
> C-31: phase names encode pipeline purpose. C-32: CONFIRMED/SCHEDULED/ACKNOWLEDGED in GATE.
> C-29: compound bundles in GATE pre-check. C-30: FINALIZE block declares 8 criteria simultaneously.
> C-10: Inertia Advocate front-loaded in GATE as primary constraint before scan begins.
> SCAN: [n] rows. DELIBERATE: [mode]. DRAFT: [n] groups, [n] teams, exec '[name]'. Draft-only."

---

## R7 Invariant Checklist (verify all five variations carry these before scoring)

| Criterion | Mechanism | Present in V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----------|:---:|:---:|:---:|:---:|:---:|
| C-29 | Compound bundle notation in pre-check: `C-11+C-21+C-22+C-25+C-26` and `C-23+C-27` | Y | Y | Y | Y | Y |
| C-30 | Post-write block cites 8 C-NN IDs simultaneously in FINALIZE unit | Y | Y | Y | Y | Y |
| C-31 | Structural unit names encode pipeline function (GATE/SCAN/DELIBERATE/DRAFT/FINALIZE) | Y | Y | Y | Y | Y |
| C-32 | Three-state vocabulary: CONFIRMED / SCHEDULED / ACKNOWLEDGED on actual pre-check items | Y | Y | Y | Y | Y |

## Predicted Scores Under v7

| Variation | Axis | C-29 | C-30 | C-31 | C-32 | Predicted |
|-----------|------|:----:|:----:|:----:|:----:|----------:|
| V-01 | Role sequence (phase-named roles + persona sub-label) | PASS | PASS | PASS | PASS | 210/210 |
| V-02 | Output format (purpose-named sections) | PASS | PASS | PASS | PASS | 210/210 |
| V-03 | Lifecycle emphasis (5-phase rebuilt complete) | PASS | PASS | PASS | PASS | 210/210 |
| V-04 | Role sequence + lifecycle (5 roles, function-named only) | PASS | PASS | PASS | PASS | 210/210 |
| V-05 | Phrasing register + inertia framing (imperative voice) | PASS | PASS | PASS | PASS | 210/210 |

**Differentiating signals for rubric v8 extraction:**
- V-01: The persona sub-label (e.g., "GATE PHASE / COMPLIANCE OFFICER") creates a dual-identity
  unit name. If C-31 requires phase name alone, the sub-label is noise. If it adds value, V-01's
  dual-identity pattern may surface as a new criterion.
- V-04: The FINALIZE ROLE as sole owner of C-30 creates the cleanest criterion-ownership mapping
  — each role owns exactly one criterion cluster. This "exclusive criterion ownership" pattern
  may surface if scorers find V-04's ownership structure auditable at the role level.
- V-05: The ACKNOWLEDGED items for C-05 and C-10 in the GATE PRE-CHECK frame these as permanent
  boundaries rather than execution commitments. The distinction between "permanent boundary" and
  "scheduled output" as a third ACKNOWLEDGED use case may surface as a criterion refinement.
