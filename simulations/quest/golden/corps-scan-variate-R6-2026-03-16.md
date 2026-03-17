---
skill: quest-variate
skill_target: corps-scan
round: 6
date: 2026-03-16
rubric_version: 6
---

# Variate R6 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v6 rubric (190 pts,
28 criteria). R5's top two variations (V-01, V-02) both scored 180/190 under v6 but via distinct
technique clusters:

- V-01 earned C-27 (tri-part pivot deliberation) + C-28 (SCHEDULED execution-state markers)
  but missed C-25 (universal section labeling) and C-26 (multi-criterion header).
- V-02 earned C-25 + C-26 but missed C-27 + C-28.
- V-03 earned none of the four new criteria.

R6 targets 190/190 by treating all four as structural invariants. Every variation must include:

- **C-25**: Every structural section — pre-YAML, YAML-adjacent, post-YAML — carries a C-NN
  self-label in its header or opening line. No unlabeled sections anywhere.
- **C-26**: At least one section header cites 2+ distinct C-NN criterion IDs simultaneously
  (e.g., `"C-26: C-11 + C-21 satisfier"`). The section is architecturally designed to satisfy
  multiple criteria at once and declares both in the header.
- **C-27**: Each candidate pivot mode in the deliberation (C-23) carries a three-part structure:
  Evidence For / Evidence Against / Assessment. All candidates follow the same triad. At least
  2 candidate modes assessed in this form.
- **C-28**: Pre-check or compliance section uses a consistent execution-state vocabulary that
  distinguishes at least 2 states on the items themselves — e.g., SCHEDULED (deferred) vs
  CONFIRMED (already satisfied) — as annotations on each item, not in a legend.

All R5 invariants (C-21 through C-24) and all prior round invariants (C-12 through C-20) are
preserved in all variations.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence — universal C-NN section labels across all 4 role outputs + C-26 in ROLE 2 schema header | V-01 |
| Output format — every section header carries C-NN label + tri-part deliberation + SCHEDULED/CONFIRMED pre-check | V-02 |
| Lifecycle emphasis — 5 phases as organizing frame, phase gate uses SCHEDULED markers, DELIBERATE phase uses tri-part | V-03 |
| Role sequence + output format — 4 roles, each role produces section-labeled outputs; two-tier execution state | V-04 |
| Phrasing register + inertia framing — direct imperative voice, Inertia Advocate introduced upfront; all invariants preserved | V-05 |

---

## V-01 — Role Sequence: Universal Section Labels Across All Roles + Tri-Part Pivot

**Axis**: Role sequence
**Hypothesis**: R5 V-01 reached 180/190 (C-27+C-28, missing C-25+C-26). Adding C-25 as a
structural rule at the role level — every role output header carries a C-NN self-label — and
C-26 by designing ROLE 2's schema header to cite C-11 + C-21 simultaneously achieves 190/190.
The four-role separation (Compliance Officer, Repo Archaeologist, Pivot Analyst, Org Drafter)
remains the organizing axis; the tri-part deliberation (C-27) belongs to ROLE 3 and execution-
state markers (C-28) belong to ROLE 1. C-25 and C-26 are injected as structural rules that
apply across all roles without changing the role assignments.

---

You are running `corps-scan`. Work through four named roles in strict sequence. Do not begin a
role until the prior role is fully complete. **ROLE 2, ROLE 3, and ROLE 4 are blocked until
ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label in its header or opening annotation. No section in this response may be unlabeled.

---

### ROLE 1 — COMPLIANCE OFFICER (C-20: structural gate — all other roles blocked until complete)

Prerequisite for all other roles: This role must complete before any repo scan, signal
inventory, pivot deliberation, or YAML work begins. A model following this sequence cannot
reach ROLE 2, ROLE 3, or ROLE 4 without first completing everything in ROLE 1.

Your job: emit the hard boundary declaration, then complete the compliance pre-check using
criterion IDs as primary keys. Items marked SCHEDULED commit to work that follows; items
marked CONFIRMED are already satisfied above this item.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-28: SCHEDULED/CONFIRMED execution-state markers on each item)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY (C-12 satisfier)" block above is the first substantive line of this output.
    It precedes this pre-check, all inventory work, all pivot deliberation, and all YAML content.
    STATUS: CONFIRMED — draft-only declaration is line 1 of this response.

[ ] C-13 -- self-referential confirmation:
    This item confirms that C-12 is satisfied. The draft-only statement named in C-12 appears
    before any inventory, deliberation, or YAML content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary; it precedes this pre-check.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — violation anywhere is an essential failure regardless of other scores.

[ ] C-25 -- universal section self-labeling:
    Every section produced by ROLE 1 through ROLE 4 carries a C-NN self-label.
    This section header carries "(C-20: structural gate)". Remaining roles carry labels below.
    STATUS: CONFIRMED — this section is already labeled; SCHEDULED for ROLE 2, 3, 4.

[ ] C-11 + C-21 + C-22 -- signal schema with C-NN column headers, section self-labeled (SCHEDULED):
    ROLE 2 produces a Signal Schema whose header cites C-11 + C-21 simultaneously (C-26 satisfier).
    Columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    The schema section header self-labels: "C-26: C-11 + C-21 satisfier — precedes YAML block".
    STATUS: SCHEDULED — satisfied by ROLE 2 output, which follows this pre-check.

[ ] C-23 + C-27 -- pivot deliberation with tri-part candidate assessment (SCHEDULED):
    ROLE 3 produces a Pivot Deliberation section with "Evidence For / Evidence Against /
    Assessment" for all 4 candidate modes. Selection cites a specific ROLE 2 schema row.
    STATUS: SCHEDULED — satisfied by ROLE 3 output, which follows ROLE 2.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles. Generic placeholders fail.
    STATUS: SCHEDULED — enforced by ROLE 4 per team area.

[ ] C-07 -- exec office present (SCHEDULED):
    The org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required element in ROLE 4 YAML draft.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 of the 3 amend options name the downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced by ROLE 4 amend section.
```

C-17 satisfied: C-11+C-21+C-22, C-23+C-27, C-04, C-07, C-16 are forward commitments (SCHEDULED).
C-18 satisfied: C-NN IDs are primary keys for all 9 pre-check items.
C-28 satisfied: SCHEDULED vs CONFIRMED execution-state markers present on every item.

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 — REPO ARCHAEOLOGIST (C-25: section self-labeled; C-11 + C-26 satisfier)

Prerequisite: ROLE 1 pre-check is complete. No pivot deliberation, no YAML in this role —
signal schema production only.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check workspace configs
(npm workspaces, Cargo workspace, go.work). Check domain-language signals (bounded context
names, business capability terms in directory names or module identifiers).

#### Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML block; C-22: section announces criterion before rows)

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-22: this header announces criterion purpose before any schema rows are written

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09) |
|----------------|--------------------------|-------------------|-----------------------------|---------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                     |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only (Engineer, PM, Tech Lead, etc.) — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row — no generic phrases.
- Cap at 8 rows. Group weak signals under closest strong signal; note the grouping.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 — PIVOT ANALYST (C-25: section self-labeled; C-23 + C-27 satisfier — tri-part deliberation)

Prerequisite: ROLE 1 and ROLE 2 complete. Signal Schema is available. No YAML in this role —
pivot deliberation only.

Assess all four candidate pivot modes against the ROLE 2 Signal Schema. Each candidate carries
three structured entries: Evidence For (specific schema rows by "Repo signal" value), Evidence
Against (absent signals or counter-evidence), Assessment (strong / possible / weak — one
sentence). Select one mode; rationale must cite a specific schema row by "Repo signal" value.

#### Pivot Mode Deliberation (C-25: section self-labeled; C-27: tri-part Evidence For/Against/Assessment)

```
## Pivot Mode Deliberation — {{date}}
## (C-25: section self-labeled; C-23: deliberation precedes selection; C-27: tri-part triad)

directory mode:
  Evidence For: [schema rows by "Repo signal" value that support directory clustering]
  Evidence Against: [schema rows or absent signals that argue against]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent directory signals or service manifest signals]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent service manifest signals or mixed directory/domain signals]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context or business-capability signals]
  Evidence Against: [absent DDD naming signals or flat directory layout]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific ROLE 2 schema row (by "Repo signal" value)
  that most strongly favors the selected mode over the highest-scoring alternative]
```

ROLE 3 complete. ROLE 4 may now begin.

---

### ROLE 4 — ORG DRAFTER (C-25: section self-labeled; C-01 satisfier — produces the org.yaml block)

Prerequisite: ROLE 1, ROLE 2, and ROLE 3 complete. Draft-only constraint active. All team
names must trace to ROLE 2 schema "YAML name (C-02)" column. Pivot mode is ROLE 3 selection.

**Pre-YAML traceability statement** (required immediately before YAML block):
> "Drafting org.yaml. All team names from ROLE 2 Signal Schema 'YAML name (C-02)' column.
> Pivot mode: [ROLE 3 selection]. C-05 active: no .craft/roles/ content in this output."

#### Draft org.yaml (C-25: section self-labeled; C-01 satisfier — org configuration contract)

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

#### Post-Write Verification (C-25: section self-labeled; C-14 + C-19 satisfier — dual-bracket post gate)

```
POST-WRITE VERIFICATION — org.yaml — ROLE 4
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction)

[ ] Every team name matches ROLE 2 schema "YAML name (C-02)" row    STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                      STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                       STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                         STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                          STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team level AND group level (C-24)           STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation with tri-part structure (C-27)               STATUS: [CONFIRMED / FAIL]
[ ] Every role section carries C-NN self-label (C-25)               STATUS: [CONFIRMED / FAIL]
[ ] At least one header cites 2+ C-NN IDs (C-26)                   STATUS: [CONFIRMED / FAIL]
[ ] SCHEDULED/CONFIRMED markers present in pre-check (C-28)         STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: ROLE 1 pre-check is the pre-YAML gate; this block is the post-YAML gate.
Both present. C-19: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at point of satisfaction.
```

#### Amend Options (C-25: section self-labeled; C-08 + C-16 satisfier — debt-framed options)

```
## Amend Options
## (C-25: section self-labeled; C-16: debt-framing on each option below)

AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | Deliberation basis: [ROLE 3 selected row]
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
  Current: [n] groups — [names] | Grouping principle: [ROLE 3 pivot mode + schema clustering]
  Debt if skipped: Misaligned groups co-locate Inertia Advocates whose status-quo frames
    conflict, degrading corps-committee review signal coherence across all review cycles.
  Alternatives: flatten / split / add cross-cutting platform pillar per schema row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R6). C-25: all sections labeled (ROLE 1: C-20 gate; ROLE 2: C-26 schema;
> ROLE 3: C-23+C-27 deliberation; ROLE 4: C-01 YAML, C-14+C-19 post-write, C-08+C-16 amend).
> C-26: ROLE 2 schema header cites C-11 + C-21. C-27: tri-part For/Against/Assessment in ROLE 3.
> C-28: SCHEDULED/CONFIRMED markers in ROLE 1 pre-check. ROLE 2: [n] schema rows. ROLE 3: [mode]
> selected. ROLE 4: [n] groups, [n] teams, exec '[name]'. Draft-only: no role files written."

---

## V-02 — Output Format: Universal Section Labels + Tri-Part Deliberation + SCHEDULED Pre-Check

**Axis**: Output format
**Hypothesis**: R5 V-02 reached 180/190 (C-25+C-26, missing C-27+C-28). Adding tri-part
structure (C-27) to Section 2's pivot deliberation and execution-state vocabulary (C-28) to
Section 0's pre-check completes the 190/190 without disrupting the numbered-section organizing
frame. The axis remains output format: every section is numbered and self-labeled (C-25), the
pivot deliberation section's per-mode blocks use the Evidence For / Evidence Against /
Assessment triad (C-27), and Section 0's pre-check annotates each item with SCHEDULED or
CONFIRMED (C-28). Sections are the primary frame — no role personas.

---

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### Section 0: Compliance Gate (C-20: structural gate — all sections blocked until this section is complete)

This section is owned by the Compliance Officer function. All subsequent sections are blocked
until this pre-check is fully output.

```
COMPLIANCE PRE-CHECK — corps-scan
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-28: SCHEDULED/CONFIRMED execution-state markers on each item)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY (C-12 satisfier)" block above is the first substantive line of this output.
    STATUS: CONFIRMED — precedes this pre-check and all subsequent content.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12. The draft-only statement appears before any inventory, deliberation,
    or YAML content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary above.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated.

[ ] C-11 + C-21 + C-22 + C-25 + C-26 -- signal schema, C-NN column headers, section labeled,
    multi-criterion header (SCHEDULED):
    Section 1 header will read "C-26: C-11 + C-21 satisfier — precedes YAML; C-22: section
    self-labeled", satisfying C-22 (pre-write section self-labeling), C-25 (universal labeling),
    and C-26 (multi-criterion header) simultaneously. Schema columns: "YAML name (C-02)",
    "Proposed roles (C-04)", "Detection evidence (C-09)".
    STATUS: SCHEDULED — satisfied by Section 1.

[ ] C-23 + C-27 -- pivot deliberation, tri-part Evidence For/Against/Assessment (SCHEDULED):
    Section 2 header will read "C-25: C-23 + C-27 satisfier". Each candidate pivot mode will
    carry Evidence For / Evidence Against / Assessment. Selection cites a specific Section 1
    schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by Section 2.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles. No generics.
    STATUS: SCHEDULED — enforced in Section 3.

[ ] C-07 -- exec office present (SCHEDULED):
    org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required element in Section 3.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced in Section 5.
```

C-15 satisfied: pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-04, C-07, C-16 as requirements.
C-17 satisfied: 5 SCHEDULED items are forward commitments.
C-28 satisfied: SCHEDULED vs CONFIRMED on every item.

Section 0 complete. All subsequent sections may proceed.

---

### Section 1: Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled)

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests, workspace configs. For each detected organizing signal, add one row. The
schema is the sole YAML authority — every team area in the YAML must match a "YAML name (C-02)"
cell exactly. This section self-labels per C-22; the header above declares both C-11 and C-21
as simultaneous satisfiers (C-26).

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)

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

---

### Section 2: Pivot Deliberation (C-25: C-23 + C-27 satisfier — tri-part candidate assessment)

Before selecting a pivot mode, enumerate all candidates using the tri-part Evidence For /
Evidence Against / Assessment structure. Selection rationale must cite a specific Signal Schema
row by "Repo signal" value. A general repo observation does not satisfy C-23.

```
## Pivot Mode Deliberation — {{date}}
## (C-25: section self-labeled; C-27: tri-part triad for every candidate)

directory mode:
  Evidence For: [schema rows by "Repo signal" value that support directory clustering]
  Evidence Against: [absent or counter-indicating signals]
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
  Evidence Against: [absent domain language in directory names or module identifiers]
  Assessment: [strong / possible / weak — one sentence]

Selected mode: [mode]
Rationale: [one sentence citing the specific schema row (by "Repo signal" value) that most
  strongly favors the selected mode over the highest-scoring alternative]
```

---

### Section 3: Draft org.yaml (C-25: C-01 satisfier — org configuration contract)

**Pre-YAML authority statement** (required immediately before YAML block):
> "Writing org.yaml. All YAML team names are exact matches to Section 1 schema 'YAML name
> (C-02)' column. Schema has [n] rows. Pivot: [Section 2 selection]. C-05 active: no
> .craft/roles/ content in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Section 2 selected mode]
# schema-rows: [n] signals — all team names from Section 1 schema "YAML name (C-02)" column
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From Section 1 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level: Inertia Advocates share governance context and interact in corps-committee
      #   reviews. Wrong grouping = misaligned status-quo arguments across teams.
      teams:
        - name: "[YAML name — exact match to Section 1 schema 'YAML name (C-02)' column]"
          # schema-signal: [Section 1 "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from Section 1 "Proposed roles (C-04)" column]
            - [Named role from Section 1 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build — argues status-quo in team reviews

        - name: "[YAML name 2 — exact match to Section 1 schema row]"
          # schema-signal: [Section 1 "Repo signal" value]
          roles:
            - [Named role from Section 1 schema]
            - [Named role from Section 1 schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      teams: [...]
```

---

### Section 4: Post-Write Verification (C-25: C-14 + C-19 satisfier — post-YAML gate)

```
POST-WRITE VERIFICATION — org.yaml
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction)

[ ] Every team name matches Section 1 schema "YAML name (C-02)" row   STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                        STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                         STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                           STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                            STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team level AND group level (C-24)             STATUS: [CONFIRMED / FAIL]
[ ] Tri-part pivot deliberation present (C-27)                        STATUS: [CONFIRMED / FAIL]
[ ] Every section carries C-NN self-label (C-25)                      STATUS: [CONFIRMED / FAIL]
[ ] At least one header cites 2+ C-NN IDs (C-26 — Section 1 header)  STATUS: [CONFIRMED / FAIL]
[ ] SCHEDULED/CONFIRMED markers in Section 0 pre-check (C-28)         STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: Section 0 pre-check is the pre-YAML gate; this Section 4 is the post-YAML gate.
C-19 self-labeling: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at satisfaction point.
```

---

### Section 5: Amend Options (C-25: C-08 + C-16 satisfier — debt-framed options)

```
## Amend Options
## (C-25: section self-labeled; C-16: debt framing on every option)

AMEND-A: Switch pivot mode
  Current: [Section 2 mode] | Deliberation basis: [Section 2 selected row]
  Debt if skipped: Wrong pivot mode clusters schema rows by the wrong organizing dimension.
    corps-build role files, corps-pr routing, corps-committee composition, and corps-rob
    ownership chains inherit the misalignment — no downstream skill provides a correction point.
  Alternative: [Section 2 second-highest Assessment mode] | Evidence: [Section 2 row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [Section 1 exec inference]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts
    and corps-committee appointment templates. No downstream corps-* skill corrects it.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping principle: [Section 2 pivot + schema clustering]
  Debt if skipped: Misaligned groups co-locate Inertia Advocates with conflicting status-quo
    frames, degrading corps-committee review coherence across all cycles.
  Alternatives: flatten / split / add cross-cutting platform pillar per schema row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R6). C-25: 6 sections labeled (0–5). C-26: Section 1 header cites C-11 +
> C-21. C-27: Section 2 uses tri-part For/Against/Assessment for all 4 modes. C-28: Section 0
> uses SCHEDULED/CONFIRMED markers. Section 1: [n] rows. Section 2: [mode] selected. Section 3:
> [n] groups, [n] teams, exec '[name]'. Section 4: all confirmed. Draft-only: no role files."

---

## V-03 — Lifecycle Emphasis: 5-Phase Pipeline with Phase Gate Criteria

**Axis**: Lifecycle emphasis
**Hypothesis**: Organizing corps-scan as 5 discrete phases (GATE → SCAN → DELIBERATE → DRAFT →
FINALIZE) makes lifecycle boundaries explicit in a way that roles and sections do not — phases
have entry conditions and exit artifacts that enforce criterion coverage. C-25 is satisfied by
labeling each phase header with its C-NN purpose. C-26 is satisfied by a DELIBERATE phase
header that cites C-23 + C-27 simultaneously. C-27 is satisfied by DELIBERATE phase's tri-part
mode assessment structure. C-28 is satisfied by GATE phase's pre-check using SCHEDULED/CONFIRMED
vocabulary as phase-status annotations. The lifecycle frame emphasizes how far each phase
advances the org.yaml contract.

---

You are running `corps-scan`. Complete the five phases in strict order. Do not begin a phase
until the prior phase is complete and its exit artifact is confirmed.

**Universal labeling rule (C-25)**: Every phase header and every structural sub-section
within a phase carries a C-NN self-label identifying its criterion purpose.

---

### GATE PHASE (C-25: C-20 satisfier — compliance gate; C-28: execution-state markers below)

Entry condition: this is the start of the output.
Exit artifact: pre-check with all items confirmed or marked SCHEDULED.

**DRAFT BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

```
GATE PHASE PRE-CHECK — corps-scan
(C-18: C-NN IDs as primary keys; C-28: SCHEDULED/CONFIRMED on each item)

[ ] C-12 -- draft boundary front-loaded:
    "DRAFT BOUNDARY (C-12 satisfier)" block above is the first substantive line of this output.
    STATUS: CONFIRMED — precedes this pre-check and all subsequent phases.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12. Draft-only statement precedes all phases and their output.
    STATUS: CONFIRMED — C-12 located and confirmed above.

[ ] C-05 -- no .craft/roles/ files:
    No role files, role file content, or role-creation instructions in any phase.
    STATUS: ACKNOWLEDGED — essential failure if any phase produces role file content.

[ ] C-11 + C-21 + C-22 + C-26 -- signal schema, C-NN columns, section self-labeled,
    multi-criterion header (SCHEDULED):
    SCAN PHASE produces a Signal Schema with header "C-26: C-11 + C-21 satisfier" and
    C-NN-labeled columns. Section self-label satisfies C-22.
    STATUS: SCHEDULED — exit artifact of SCAN PHASE.

[ ] C-23 + C-27 -- pivot deliberation, tri-part triad (SCHEDULED):
    DELIBERATE PHASE produces mode deliberation with "Evidence For / Evidence Against /
    Assessment" triad for each candidate mode. Header reads "C-26: C-23 + C-27 satisfier".
    STATUS: SCHEDULED — exit artifact of DELIBERATE PHASE.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in org.yaml has 2+ named roles.
    STATUS: SCHEDULED — DRAFT PHASE enforcement.

[ ] C-07 -- exec office present (SCHEDULED):
    org.yaml includes exec-office section.
    STATUS: SCHEDULED — DRAFT PHASE enforcement.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 FINALIZE PHASE amend options name downstream debt.
    STATUS: SCHEDULED — FINALIZE PHASE enforcement.
```

C-17 satisfied: 5 SCHEDULED items are forward commitments.
C-28 satisfied: SCHEDULED/CONFIRMED execution-state markers on every item.

GATE PHASE complete. SCAN PHASE may begin.

---

### SCAN PHASE (C-25: C-11 satisfier — pre-YAML repo signal inventory)

Entry condition: GATE PHASE pre-check complete.
Exit artifact: Signal Schema with C-NN-labeled columns.

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs. For each
detected organizing signal, add one row to the Signal Schema.

#### Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML; C-22: section self-labeled before rows)

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled column headers)
## C-22: this section announces its criterion purpose before schema rows begin

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09) |
|----------------|--------------------------|-------------------|-----------------------------|---------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: evidence]  |
| [...]          | [...]                    | [...]             | [...]                       | [...]                     |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence of repo evidence per row.
- Cap at 8 rows.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

SCAN PHASE complete. Exit artifact: Signal Schema above. DELIBERATE PHASE may begin.

---

### DELIBERATE PHASE (C-26: C-23 + C-27 satisfier — tri-part deliberation before pivot selection)

Entry condition: SCAN PHASE Signal Schema complete. No YAML in this phase — deliberation only.

Assess all four candidate pivot modes against the Signal Schema. Use the tri-part triad for
every candidate: Evidence For / Evidence Against / Assessment. Select one mode with a rationale
that cites a specific Signal Schema row by "Repo signal" value.

#### Pivot Mode Deliberation (C-25: section self-labeled; C-27: tri-part For/Against/Assessment)

```
## Pivot Mode Deliberation — {{date}}
## (C-25: section self-labeled; C-23: deliberation precedes selection;
##  C-27: Evidence For / Evidence Against / Assessment for each candidate)

directory mode:
  Evidence For: [schema rows by "Repo signal" value that support directory clustering]
  Evidence Against: [counter-indicating signals or absent directory structure]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming signals or flat structure]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent service manifests or mixed signal types]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context or business-capability signals]
  Evidence Against: [absent domain language in identifiers]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific Signal Schema row (by "Repo signal" value)
  that most strongly favors the selected mode over the highest-scoring alternative]
```

DELIBERATE PHASE complete. Exit artifact: pivot mode selection above. DRAFT PHASE may begin.

---

### DRAFT PHASE (C-25: C-01 satisfier — produces the org.yaml block)

Entry condition: DELIBERATE PHASE selection complete. Draft-only constraint active.
All team names must trace to SCAN PHASE schema "YAML name (C-02)" column.

**Pre-YAML traceability statement** (required immediately before YAML block):
> "Drafting org.yaml. All team names from SCAN PHASE Signal Schema 'YAML name (C-02)' column.
> Pivot mode: [DELIBERATE PHASE selection]. C-05 active: no .craft/roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE PHASE selected mode]
# schema-rows: [n] signals
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From SCAN PHASE exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group gets one Inertia Advocate from corps-build.
      #   Group-level: Inertia Advocates share governance context for corps-committee reviews.
      teams:
        - name: "[YAML name — exact match to SCAN PHASE schema 'YAML name (C-02)' column]"
          # schema-signal: [SCAN PHASE "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from SCAN PHASE "Proposed roles (C-04)" column]
            - [Named role from SCAN PHASE "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

        - name: "[YAML name 2 — exact match to schema row]"
          # schema-signal: [SCAN PHASE "Repo signal" value]
          roles:
            - [Named role from schema]
            - [Named role from schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): every team in this group gets one Inertia Advocate.
      teams: [...]
```

DRAFT PHASE complete. Exit artifact: org.yaml above. FINALIZE PHASE may begin.

---

### FINALIZE PHASE (C-25: C-14 + C-08 + C-16 satisfier — post-write verification and amend options)

Entry condition: DRAFT PHASE org.yaml complete.
Exit artifact: post-write verification and debt-framed amend options.

#### Post-Write Verification (C-25: C-14 + C-19 satisfier — dual-bracket post gate)

```
POST-WRITE VERIFICATION — org.yaml
(C-25: self-labeled; C-19: criterion IDs cited at satisfaction point)

[ ] Every team name matches SCAN PHASE schema "YAML name (C-02)" row  STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                        STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                         STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                           STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                            STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                   STATUS: [CONFIRMED / FAIL]
[ ] Tri-part deliberation in DELIBERATE PHASE (C-27)                  STATUS: [CONFIRMED / FAIL]
[ ] All 5 phases carry C-NN self-labels (C-25)                        STATUS: [CONFIRMED / FAIL]
[ ] DELIBERATE PHASE header cites C-23 + C-27 (C-26)                 STATUS: [CONFIRMED / FAIL]
[ ] GATE PHASE uses SCHEDULED/CONFIRMED markers (C-28)                STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE PHASE pre-check is the pre-YAML gate; this post-write is the post-YAML gate.
C-19: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at satisfaction point.
```

#### Amend Options (C-25: C-08 + C-16 satisfier — actionable options with debt framing)

```
## Amend Options
## (C-16: debt-framing on each option; C-08: 3 actionable amend options)

AMEND-A: Switch pivot mode
  Current: [DELIBERATE PHASE mode] | Basis: [deliberation row citation]
  Debt if skipped: Wrong pivot mode misaligns all corps-build role files, corps-pr routing,
    corps-committee composition, and corps-rob ownership chains without a correction point.
  Alternative: [second-highest Assessment mode] | Evidence: [deliberation row]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [SCAN PHASE exec inference]
  Debt if skipped: Name propagates verbatim to corps-rob artifacts and corps-committee templates.
    No downstream corps-* skill corrects it — requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping: [DELIBERATE PHASE pivot + schema clustering]
  Debt if skipped: Misaligned groups co-locate conflicting Inertia Advocates, degrading
    corps-committee review coherence across all governance cycles.
  Alternatives: flatten / split / add cross-cutting platform pillar
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R6 / 5-phase). C-25: all 5 phases + sub-sections labeled. C-26:
> DELIBERATE PHASE header cites C-23 + C-27. C-27: tri-part For/Against/Assessment in DELIBERATE
> PHASE. C-28: SCHEDULED/CONFIRMED markers in GATE PHASE. SCAN: [n] rows. DELIBERATE: [mode].
> DRAFT: [n] groups, [n] teams, exec '[name]'. FINALIZE: all confirmed. No role files written."

---

## V-04 — Role Sequence + Output Format: Labeled Section Outputs Within Each Role

**Axis**: Role sequence + output format (combined)
**Hypothesis**: R5 V-01 used role sequence (C-27+C-28 strong) but produced unlabeled role
outputs. R5 V-02 used numbered sections (C-25+C-26 strong) but had no role personas. V-04
combines them: four named roles are the sequence frame, but each role's outputs are structured
as C-NN-labeled sections. This produces a two-tier labeling structure — role headers carry their
C-NN label (C-20, C-11, C-23, C-01) and within each role, sub-sections carry their own C-NN
labels. The pivot deliberation (C-27 tri-part) belongs to ROLE 3, execution-state markers (C-28)
belong to ROLE 1, universal labeling (C-25) is enforced at both tiers, and at least one section
header cites 2+ C-NN IDs (C-26 — ROLE 2's schema sub-section).

---

You are running `corps-scan`. Work through four named roles in strict sequence. Do not begin a
role until the prior role is fully complete. **ROLE 2, ROLE 3, and ROLE 4 are blocked until
ROLE 1 outputs its pre-check.**

**Two-tier labeling rule (C-25)**: Role headers carry C-NN labels identifying their criterion
ownership. Sub-sections within each role also carry C-NN labels. No section at either tier
is unlabeled.

---

### ROLE 1 — COMPLIANCE OFFICER (C-20: structural gate — blocks ROLE 2, 3, 4 until complete)

#### Sub-section 1.1 — Hard Boundary Declaration (C-12 satisfier)

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.craft/roles/` files
will be written in this response.

#### Sub-section 1.2 — Compliance Pre-Check (C-18: C-NN primary keys; C-28: SCHEDULED/CONFIRMED)

```
COMPLIANCE PRE-CHECK — corps-scan — ROLE 1

[ ] C-12 -- draft boundary front-loaded:
    Sub-section 1.1 "HARD BOUNDARY" block is the first substantive content of this output.
    STATUS: CONFIRMED — precedes this pre-check and all subsequent roles.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12. Sub-section 1.1 precedes all inventory, deliberation, and YAML.
    STATUS: CONFIRMED — C-12 names and locates the boundary in Sub-section 1.1 above.

[ ] C-05 -- no .craft/roles/ files:
    No role files, role file content, or role-creation instructions in any role's output.
    STATUS: ACKNOWLEDGED — essential failure if violated.

[ ] C-11 + C-21 + C-22 + C-26 -- signal schema, C-NN columns, section labeled, multi-header
    (SCHEDULED):
    ROLE 2 Sub-section 2.1 will be headed "C-26: C-11 + C-21 satisfier — precedes YAML; C-22:
    self-labeled". Columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence
    (C-09)". C-26 multi-criterion header is Sub-section 2.1's header itself.
    STATUS: SCHEDULED — satisfied by ROLE 2 Sub-section 2.1.

[ ] C-23 + C-27 -- pivot deliberation, tri-part triad (SCHEDULED):
    ROLE 3 Sub-section 3.1 will use "Evidence For / Evidence Against / Assessment" for each
    candidate mode. Selection cites a specific ROLE 2 schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by ROLE 3 Sub-section 3.1.

[ ] C-04 -- named roles per team (SCHEDULED):
    ROLE 4 Sub-section 4.1 YAML: every team area lists 2+ named roles. No generics.
    STATUS: SCHEDULED — ROLE 4 enforcement.

[ ] C-07 -- exec office present (SCHEDULED):
    ROLE 4 Sub-section 4.1 YAML: exec-office section present.
    STATUS: SCHEDULED — ROLE 4 enforcement.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    ROLE 4 Sub-section 4.3: at least 2 amend options name downstream debt.
    STATUS: SCHEDULED — ROLE 4 enforcement.
```

C-17 satisfied: 5 SCHEDULED items are forward commitments to named sub-sections.
C-28 satisfied: SCHEDULED/CONFIRMED on every item.

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 — REPO ARCHAEOLOGIST (C-11 satisfier — pre-YAML signal schema production)

#### Sub-section 2.1 — Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled)

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`, service
manifests, workspace configs. For each detecting organizing signal, add one row. The schema
is the sole YAML authority — every team name in ROLE 4 must match a "YAML name (C-02)" cell.

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled column headers)
## C-22: this sub-section header announces its criterion purpose before schema rows

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09) |
|----------------|--------------------------|-------------------|-----------------------------|---------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: evidence]  |
| [...]          | [...]                    | [...]             | [...]                       | [...]                     |

- Minimum 2 rows. PLACEHOLDER row if repo has fewer signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence of repo evidence per row.
- Cap at 8 rows.

Exec office inference: [schema row or term, or "no signal — placeholder"]
```

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 — PIVOT ANALYST (C-23 + C-27 satisfier — tri-part deliberation before pivot selection)

#### Sub-section 3.1 — Pivot Mode Deliberation (C-25: self-labeled; C-27: tri-part triad)

Assess all four candidates against the ROLE 2 Signal Schema. Each candidate carries three
parts: Evidence For, Evidence Against, Assessment. Selection cites a specific schema row.

```
## Pivot Mode Deliberation — {{date}}
## (C-25: sub-section self-labeled; C-27: tri-part Evidence For/Against/Assessment;
##  C-23: deliberation precedes selection)

directory mode:
  Evidence For: [schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [counter-indicating signals or absent directory structure]
  Assessment: [strong / possible / weak — one sentence]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming or mixed signal types]
  Assessment: [strong / possible / weak — one sentence]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent service manifests]
  Assessment: [strong / possible / weak — one sentence]

domain mode:
  Evidence For: [schema rows with bounded-context or business-capability signals]
  Evidence Against: [absent domain language in identifiers]
  Assessment: [strong / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing specific ROLE 2 schema row (by "Repo signal" value)
  that most strongly favors selected mode over highest-scoring alternative]
```

ROLE 3 complete. ROLE 4 may now begin.

---

### ROLE 4 — ORG DRAFTER (C-01 satisfier — produces the org.yaml block)

#### Sub-section 4.0 — Pre-YAML Traceability Statement (C-25: C-02 satisfier)

> "Drafting org.yaml. All team names from ROLE 2 schema 'YAML name (C-02)' column. Pivot mode:
> [ROLE 3 selection]. C-05 active: no .craft/roles/ content in this output."

#### Sub-section 4.1 — Draft org.yaml (C-25: C-01 satisfier — org configuration contract)

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# schema-rows: [n] signals
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group gets one Inertia Advocate from corps-build.
      #   Group-level: Inertia Advocates share governance context for corps-committee reviews.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [ROLE 2 "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

        - name: "[YAML name 2 — exact match to schema row]"
          # schema-signal: [ROLE 2 "Repo signal" value]
          roles:
            - [Named role from schema]
            - [Named role from schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): every team gets one Inertia Advocate from corps-build.
      teams: [...]
```

#### Sub-section 4.2 — Post-Write Verification (C-25: C-14 + C-19 satisfier)

```
POST-WRITE VERIFICATION — org.yaml — ROLE 4
(C-25: sub-section self-labeled; C-19: criterion IDs cited at satisfaction point)

[ ] Every team name matches ROLE 2 schema "YAML name (C-02)" row    STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                      STATUS: [CONFIRMED / FAIL]
[ ] exec-office present                                               STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                         STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content                                         STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                 STATUS: [CONFIRMED / FAIL]
[ ] Tri-part deliberation in ROLE 3 (C-27)                         STATUS: [CONFIRMED / FAIL]
[ ] All sub-sections carry C-NN self-labels (C-25)                  STATUS: [CONFIRMED / FAIL]
[ ] Sub-section 2.1 header cites C-11 + C-21 (C-26)               STATUS: [CONFIRMED / FAIL]
[ ] SCHEDULED/CONFIRMED markers in ROLE 1 pre-check (C-28)          STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: ROLE 1 Sub-section 1.2 is the pre-YAML gate; this Sub-section 4.2 is the
post-YAML gate. C-19: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at satisfaction.
```

#### Sub-section 4.3 — Amend Options (C-25: C-08 + C-16 satisfier — debt-framed)

```
## Amend Options
## (C-16: debt-framing on each option; C-08: 3 actionable options)

AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | Deliberation basis: [ROLE 3 selected row]
  Debt if skipped: Wrong pivot mode misaligns corps-build role files, corps-pr routing,
    corps-committee composition, and corps-rob ownership chains without a correction point.
  Alternative: [ROLE 3 second-highest mode] | Evidence: [ROLE 3 row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [ROLE 2 exec inference]
  Debt if skipped: Name propagates verbatim to corps-rob and corps-committee artifacts.
    No downstream skill corrects it — re-running corps-scan is the only fix.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping: [ROLE 3 pivot + schema clustering]
  Debt if skipped: Misaligned groups produce conflicting Inertia Advocate interactions in
    corps-committee governance cycles, degrading review signal coherence.
  Alternatives: flatten / split / add platform pillar per schema row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R6 / 4-role / 2-tier labeled). C-25: role headers + sub-sections all
> labeled. C-26: Sub-section 2.1 header cites C-11 + C-21. C-27: ROLE 3 tri-part deliberation.
> C-28: SCHEDULED/CONFIRMED in ROLE 1 Sub-section 1.2. ROLE 2: [n] rows. ROLE 3: [mode]. ROLE 4:
> [n] groups, [n] teams, exec '[name]'. Post-write confirmed. Draft-only: no role files written."

---

## V-05 — Phrasing Register + Inertia Framing: Direct Imperative with Inertia-Forward Narrative

**Axis**: Phrasing register + inertia framing (combined)
**Hypothesis**: The prior four variations use formal structural vocabulary (ROLE N, SCHEDULED,
"pre-check", "exit artifact"). V-05 uses a direct imperative register — "Do X before Y", "Your
output is...", "The Inertia Advocate is..." — which makes the same structural invariants feel
like instructions rather than bureaucratic gates. Inertia framing is introduced prominently in
the opening, woven through the scan, and given its own entry in the amend options. The hypothesis
is that a register change does not sacrifice structural coverage: C-25 through C-28 can be
enforced as inlined labels and structured blocks within a more fluid narrative, and inertia-
forward framing makes C-10 and C-24 feel like design intent rather than incidental comments.

---

**Before you write anything else**: State this draft boundary as your first output line:
"DRAFT ONLY (C-12): This is a draft org.yaml for human review. No `.craft/roles/` files will
be written."

Then immediately follow with a compliance lock-in.

---

### Lock-In Block (C-20: compliance gate — do not begin repo scanning until this block is done)

Write the following compliance lock-in before doing any repo analysis:

```
LOCK-IN — corps-scan
(C-25: section self-labeled; C-18: C-NN IDs are primary keys; C-28: status tags on each item)

C-12 -- draft boundary stated first
  Confirmed above. "DRAFT ONLY (C-12)" is your first output line.
  STATUS: CONFIRMED

C-13 -- confirms C-12 is present and precedes all analysis
  This item confirms C-12 is satisfied. The draft statement precedes this block.
  STATUS: CONFIRMED

C-05 -- no .craft/roles/ content
  You will not write role files, include role file content, or reference role file creation.
  STATUS: ACKNOWLEDGED (essential — any violation fails the output regardless of score)

C-11 + C-21 + C-22 + C-26 -- repo signal table with C-NN column headers, self-labeled section
  After this block, produce a "Signal Table" section headed:
  "Signal Table (C-26: C-11 + C-21 satisfier — pre-YAML inventory with C-NN-labeled columns)"
  Columns must include "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
  STATUS: SCHEDULED (Signal Table follows this block)

C-23 + C-27 -- pivot deliberation, tri-part triad
  After the Signal Table, produce a "Pivot Deliberation" section with Evidence For / Evidence
  Against / Assessment for all 4 pivot modes. Select with a row citation from the Signal Table.
  STATUS: SCHEDULED (Pivot Deliberation follows Signal Table)

C-04 -- named roles per team
  Every team in the org.yaml gets 2+ named roles. Pull them from the Signal Table.
  STATUS: SCHEDULED (org.yaml follows Pivot Deliberation)

C-07 -- exec office
  The org.yaml includes an exec-office section.
  STATUS: SCHEDULED (org.yaml follows Pivot Deliberation)

C-16 -- debt in amend options
  At least 2 of 3 amend options name what goes wrong downstream if you skip the amendment.
  STATUS: SCHEDULED (Amend Options follows org.yaml)
```

Done. Now start repo analysis.

---

### Signal Table (C-26: C-11 + C-21 satisfier — pre-YAML inventory with C-NN-labeled columns; C-22: self-labeled)

Walk the repo systematically: top-level directories first, then `src/`, `services/`,
`packages/`, `apps/`, `modules/`. Check any service manifests (`docker-compose.yml`, Helm
charts, `k8s/` directories). Check workspace configs (npm workspaces, Cargo workspace,
go.work). Look for domain language in directory names and module identifiers.

For each real organizing signal you find, add a row. Do not invent names.

```
Signal Table — {{date}}
C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled column headers)

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Named Role 1, Named Role 2] | [one sentence: why this team] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

At least 2 rows. Cap at 8. Use PLACEHOLDER for repos with sparse signals.

The "YAML name (C-02)" column is the single source of truth for every team name in the org.yaml
below. Any divergence between this column and the YAML is a C-02 failure.

Exec office: [signal from table, or "no signal — use placeholder 'Office of Engineering Leadership'"]

Note on Inertia Advocate: corps-build auto-adds one Inertia Advocate role file to every team
when it runs. The Inertia Advocate argues for the status quo in any review involving that team.
The "Proposed roles (C-04)" column does not need to include it — corps-build handles it. But
you should understand that wrong group structure in the org.yaml means Inertia Advocates with
conflicting status-quo frames end up in the same corps-committee governance cycle. Get the
grouping right here and the downstream reviews will be coherent.
```

---

### Pivot Deliberation (C-25: C-23 + C-27 satisfier — tri-part mode assessment before selection)

Before you pick a pivot mode, assess all four options using the tri-part format. Every
candidate gets three entries: Evidence For (specific rows from the Signal Table by "Repo
signal" value), Evidence Against (what the Signal Table doesn't show, or signals that cut
against this mode), Assessment (strong / possible / weak — one sentence).

Your final selection must cite a specific "Repo signal" value from the Signal Table. A general
observation about the repo does not count.

```
Pivot Mode Deliberation — {{date}}
(C-25: section self-labeled; C-27: Evidence For / Evidence Against / Assessment per candidate)

directory mode
  Evidence For: [Signal Table rows by "Repo signal" value that favor directory clustering]
  Evidence Against: [absent or counter-indicating signals in Signal Table]
  Assessment: [strong / possible / weak — one sentence]

concept mode
  Evidence For: [Signal Table rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming or mixed signal types]
  Assessment: [strong / possible / weak — one sentence]

service mode
  Evidence For: [Signal Table rows where "Signal type" = service]
  Evidence Against: [absent service manifest signals or hybrid layout]
  Assessment: [strong / possible / weak — one sentence]

domain mode
  Evidence For: [Signal Table rows with bounded-context or business-capability signals]
  Evidence Against: [absent domain language in directory names or identifiers]
  Assessment: [strong / possible / weak — one sentence]

Selected mode: [mode]
Why: [one sentence citing the specific Signal Table row (by "Repo signal" value) that tips
  the decision — not a general repo observation]
```

---

### org.yaml Draft (C-25: C-01 satisfier — the org configuration contract)

Before the YAML block, write:
> "All team names below are exact matches to the Signal Table 'YAML name (C-02)' column.
> Pivot: [selected mode]. C-05 holding: no role files in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [selected mode from Pivot Deliberation]
# table-rows: [n]
# status: DRAFT — confirm with human before /corps-build

org:
  exec-office:
    name: "[from Signal Table exec inference, or 'Office of Engineering Leadership']"
    # rename with /corps-scan --exec-office "[new name]" before corps-build

  groups:
    - name: "[Group name — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team here gets one Inertia Advocate from corps-build at build time.
      #   Inertia Advocates across this group share governance context.
      #   They interact in corps-committee reviews — group structure determines which
      #   status-quo arguments collide. Misaligned groups = incoherent review debates.
      teams:
        - name: "[exact match to Signal Table 'YAML name (C-02)' column]"
          # from: [Signal Table "Repo signal" value — C-09]
          roles:
            - [from Signal Table "Proposed roles (C-04)"]
            - [from Signal Table "Proposed roles (C-04)"]
            # Inertia Advocate: corps-build adds this automatically

        - name: "[exact match to next Signal Table row]"
          # from: [Signal Table "Repo signal" value]
          roles:
            - [from Signal Table "Proposed roles (C-04)"]
            - [from Signal Table "Proposed roles (C-04)"]
            # Inertia Advocate: corps-build adds this automatically

    - name: "[Group 2, if Signal Table row count warrants it]"
      type: [...]
      # Inertia Advocate governance (C-24): every team here gets one Inertia Advocate.
      teams: [...]
```

---

### Post-Write Check (C-25: C-14 + C-19 satisfier — close the dual bracket)

Right after the YAML, confirm:

```
Post-Write Check — org.yaml
(C-25: section self-labeled; C-19: citing C-14 + C-02 + C-25 + C-26 + C-27 + C-28 here)

- Every team name matches Signal Table "YAML name (C-02)"        [yes / no]
- Every team has 2+ named roles                                   [yes / no]
- exec-office present                                             [yes / no]
- At least one group above teams                                  [yes / no]
- No .craft/roles/ content anywhere in this output               [yes / no]
- Inertia Advocate at team AND group level (C-24)                [yes / no]
- Tri-part deliberation in Pivot Deliberation section (C-27)     [yes / no]
- Every section carries C-NN self-label (C-25)                   [yes / no]
- Signal Table header cites C-11 + C-21 (C-26)                  [yes / no]
- Lock-In block uses SCHEDULED/CONFIRMED tags (C-28)             [yes / no]

C-14 dual-bracket: Lock-In block is the pre-YAML gate; this post-write check is the post-YAML gate.
Both present. C-19: this section cites the criteria it satisfies at the point of satisfaction.
```

---

### Amend Options (C-25: C-08 + C-16 satisfier — your next moves if anything looks wrong)

Three things you can change right now:

```
Amend Options
(C-25: section self-labeled; C-16: debt consequence named for each option)

A — Switch the pivot mode
  What you picked: [mode from Pivot Deliberation]
  Why it was picked: [row citation]
  What you lose if you skip this: Wrong mode means your team boundaries are organized by the
    wrong dimension. corps-build writes role files using those boundaries. corps-pr assigns
    review routing from them. corps-committee builds governance cycles from them. corps-rob
    draws ownership chains from them. None of those skills fix a bad pivot mode — you have to
    re-run corps-scan to correct it.
  How to change it: /corps-scan --pivot [alternative mode from deliberation]

B — Rename the exec office
  What you have: "[name in YAML]"
  Where it came from: [Signal Table exec inference or placeholder]
  What you lose if you skip: That name goes verbatim into corps-rob governance documents and
    corps-committee appointment templates. There is no downstream correction — only a re-run.
  How to change it: /corps-scan --exec-office "[the name you want]"

C — Restructure the groups
  What you have: [n] groups — [names]
  How they were formed: [pivot mode + Signal Table clustering logic]
  What you lose if you skip: Misaligned groups put Inertia Advocates from different ownership
    domains into the same corps-committee governance cycle. Their status-quo arguments will
    reflect different team realities and degrade review signal quality across all cycles.
  How to change it: /corps-scan --groups "[describe the grouping you want]"
```

> "corps-scan complete (R6 / imperative register). C-25: Lock-In, Signal Table, Pivot
> Deliberation, org.yaml Draft, Post-Write Check, Amend Options — all labeled. C-26: Signal
> Table header cites C-11 + C-21. C-27: Pivot Deliberation uses tri-part For/Against/Assessment
> for all 4 modes. C-28: Lock-In uses SCHEDULED/CONFIRMED. Signal Table: [n] rows. Selected
> mode: [mode]. Org: [n] groups, [n] teams, exec '[name]'. Inertia Advocate at group + team
> level. Draft-only: no role files. Review and confirm, then /corps-build."
