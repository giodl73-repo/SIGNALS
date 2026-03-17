---
skill: quest-variate
skill_target: corps-scan
round: 8
date: 2026-03-16
rubric_version: 8
---

# Variate R8 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v8 rubric (225 pts,
35 criteria). R7's V-01 and V-02 both reached 225/225 under v8 — the first convergence round at
the ceiling. C-33/C-34/C-35 were absorbed universally. V-03 remains at partial scorecard.

R8 treats all three v8 criteria as invariants alongside the full prior chain (C-12 through C-32):

- **C-33**: Multi-criterion headers bracket the YAML symmetrically — one in a pre-YAML section
  (SCAN header: C-11+C-21), one in a post-YAML section (FINALIZE/post-write header: C-14+C-30).
- **C-34**: Post-write criterion inventory includes at least one essential-tier criterion (C-NN
  from C-01 through C-05) cited by ID alongside aspirational criteria.
- **C-35**: ACKNOWLEDGED execution state applied to at least one essential-tier criterion in the
  pre-check, with a named violation consequence.

All R7 invariants (C-29 through C-32) and all prior round invariants (C-12 through C-28) are
preserved across all five variations.

R8 explores four new single-axis variation axes:

1. **All-essential pre-check coverage** — all 5 essential criteria accounted for in the pre-check
   with tier-appropriate states, not only C-05.
2. **Tier-stratified pre-check** — the pre-check organized into explicit tier-blocks (ESSENTIAL /
   RECOMMENDED / ASPIRATIONAL), making tier-sensitivity structural rather than only via annotation.
3. **Cross-phase I/O contracts** — each phase declares its formal inputs (consumed from prior phase)
   and outputs (produced for next phase), making phase dependencies explicit and auditable.
4. **Criterion satisfaction chain trace** — closing summary traces the full lifecycle for each
   major criterion: committed (pre-check line), satisfied (phase), confirmed (post-write).

Then two combinations:

5. **Phrasing register + anti-pattern exclusion gates** — imperative voice, each phase opens with
   a structural EXCLUSION GATE listing forbidden outputs for that phase.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence — all 5 essentials in pre-check with tier-appropriate states | V-01 |
| Output format — tier-stratified pre-check (ESSENTIAL / RECOMMENDED / ASPIRATIONAL blocks) | V-02 |
| Lifecycle emphasis — cross-phase I/O contracts on every phase header | V-03 |
| Role sequence + output format — criterion satisfaction chain trace in closing summary | V-04 |
| Phrasing register + lifecycle emphasis — imperative voice with anti-pattern exclusion gates | V-05 |

---

## V-01 — Role Sequence: All-Essential Pre-Check Coverage with Tier-Appropriate States

**Axis**: Role sequence
**Hypothesis**: R7 converged on C-35 (ACKNOWLEDGED applied to essential C-05 only). The natural
extension is accounting for ALL 5 essential criteria (C-01 through C-05) in the pre-check using
tier-appropriate execution states: C-01/C-02/C-03/C-04 are SCHEDULED (will be demonstrated in
DRAFT phase), C-05 is ACKNOWLEDGED (hard boundary — no execution commitment, violation consequence
named). This extension makes the essential tier structurally complete in the pre-check rather than
partially visible. Hypothesis: 225/225 + possible new criterion for all-essential coverage.

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
inventory, pivot deliberation, or YAML work begins.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state vocabulary on every item)

ESSENTIAL TIER (C-01 through C-05) — all five accounted for:

[ ] C-01 -- draft org.yaml block present (SCHEDULED):
    DRAFT+FINALIZE PHASE / ROLE 4 produces the org.yaml YAML block.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-02 -- team areas derived from repo (SCHEDULED):
    Every team in the YAML maps to a "YAML name (C-02)" row from ROLE 2 Signal Schema.
    No team areas invented without schema grounding.
    STATUS: SCHEDULED — enforced by ROLE 2 schema discipline and ROLE 4 traceability statement.

[ ] C-03 -- group structure present (SCHEDULED):
    org.yaml contains at least one named group container above team level.
    STATUS: SCHEDULED — required structural element in DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles. Generic placeholders fail.
    STATUS: SCHEDULED — enforced by DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions anywhere in output.
    STATUS: ACKNOWLEDGED — essential failure if violated regardless of composite score.
    Violation consequence: output is not golden; no partial credit; entire response fails C-05.

RECOMMENDED TIER (C-06 through C-08):

[ ] C-06 -- pivot mode declared with rationale (SCHEDULED):
    DELIBERATE PHASE / ROLE 3 names the selected mode and provides a rationale citing a
    specific ROLE 2 schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-07 -- exec office placeholder present (SCHEDULED):
    org.yaml includes an exec-office section (name + empty teams permitted).
    STATUS: SCHEDULED — required element in DRAFT+FINALIZE PHASE / ROLE 4 YAML.

[ ] C-08 -- amend options listed (SCHEDULED):
    At least 2 named, actionable amend options in DRAFT+FINALIZE PHASE / ROLE 4.
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4 amend section.

ASPIRATIONAL TIER (selected forward commitments):

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema with C-NN column headers, self-labeled,
    multi-criterion header (SCHEDULED):
    SCAN PHASE / ROLE 2 header reads "C-26: C-11 + C-21 satisfier — SCAN PHASE; C-22: self-labeled".
    Columns include "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation with tri-part Evidence For/Against/Assessment (SCHEDULED):
    DELIBERATE PHASE / ROLE 3 enumerates all 4 pivot modes, each with tri-part triad.
    Selection cites a specific ROLE 2 schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 of the 3 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced by DRAFT+FINALIZE PHASE / ROLE 4 amend section.

[ ] C-30 -- post-write multi-criterion declaration (SCHEDULED):
    DRAFT+FINALIZE PHASE / ROLE 4 post-write block cites 4+ C-NN IDs simultaneously,
    including at least one essential-tier C-NN (C-34).
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.
```

C-15 satisfied: pre-check names C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08,
C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-16, C-30 as requirements.
C-17 satisfied: all SCHEDULED items are forward commitments to named future roles.
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys for all items.
C-28 satisfied: SCHEDULED/CONFIRMED markers present on every item.
C-29 satisfied: "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all appear on actual pre-check items.
C-35 satisfied: C-05 STATUS: ACKNOWLEDGED — essential failure if violated, consequence named.
All-essential coverage: C-01 through C-05 all present with tier-appropriate states.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may now begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: section self-labeled; C-33 pre-YAML bracket position: C-11+C-21 multi-criterion header; C-31: SCAN PHASE)`

Prerequisite: GATE PHASE / ROLE 1 pre-check complete. No pivot deliberation, no YAML —
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
## C-33: this header is the pre-YAML bracket position for the C-26 multi-criterion pattern

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
> Pivot: [ROLE 3 selection]. C-05 ACKNOWLEDGED in GATE pre-check: no .craft/roles/ content."

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

#### Post-Write Verification — FINALIZE PHASE `(C-25: section self-labeled; C-26: C-14 + C-30 satisfier; C-33: post-YAML bracket position)`

```
POST-WRITE VERIFICATION — org.yaml — DRAFT+FINALIZE PHASE / ROLE 4
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction;
 C-30: this block cites 8+ criteria simultaneously as comprehensive satisfaction inventory;
 C-33: this is the post-YAML bracket position — SCAN PHASE pre-check was the pre-YAML position;
 C-34: essential-tier C-02 is included in this inventory alongside aspirational criteria)

[ ] Every team name matches ROLE 2 schema "YAML name (C-02)" row       STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                        STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                        STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                           STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                            STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team level AND group level (C-24)              STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation with tri-part structure in ROLE 3 (C-27)       STATUS: [CONFIRMED / FAIL]
[ ] Every section carries C-NN self-label (C-25)                      STATUS: [CONFIRMED / FAIL]
[ ] At least one header cites 2+ C-NN IDs (C-26)                      STATUS: [CONFIRMED / FAIL]
[ ] Compound bundle notation in GATE pre-check (C-29)                 STATUS: [CONFIRMED / FAIL]
[ ] Three-state vocabulary in GATE pre-check (C-32)                   STATUS: [CONFIRMED / FAIL]
[ ] All 5 essentials in pre-check with tier-appropriate states         STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE PHASE / ROLE 1 pre-check is the pre-YAML gate; this FINALIZE PHASE
block is the post-YAML gate. Both present.
C-33 symmetric bracket: SCAN PHASE header (C-11+C-21 multi-criterion) is pre-YAML position;
this FINALIZE PHASE header (C-14+C-30 multi-criterion) is post-YAML position. Both present.
C-30 multi-criterion declaration: this block simultaneously cites C-14, C-02, C-24, C-27,
C-25, C-26, C-29, C-32, C-33 at point of satisfaction — 9 criteria declared together.
C-34: essential-tier C-02 is present in this post-write inventory alongside 8 aspirationals.
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

> "corps-scan complete (R8 V-01). All 5 essential criteria in GATE pre-check: C-01/C-02/C-03/C-04
> SCHEDULED, C-05 ACKNOWLEDGED (essential failure if violated). Phases: GATE → SCAN → DELIBERATE
> → DRAFT+FINALIZE. C-33: SCAN PHASE header (C-11+C-21) and FINALIZE PHASE post-write header
> (C-14+C-30) bracket the YAML symmetrically. C-34: C-02 cited in 9-criterion post-write inventory.
> C-35: C-05 ACKNOWLEDGED with named violation consequence. Draft-only."

---

## V-02 — Output Format: Tier-Stratified Pre-Check with ESSENTIAL / RECOMMENDED / ASPIRATIONAL Blocks

**Axis**: Output format
**Hypothesis**: R7 V-02 and R7 V-01 both converge on a flat pre-check with C-NN as primary keys
and three-state vocabulary. The tier-stratified format organizes the pre-check into three named
blocks — ESSENTIAL BLOCK, RECOMMENDED BLOCK, ASPIRATIONAL BLOCK — each with a tier-level header.
This makes tier-sensitivity structural (block position declares tier) rather than only annotation-
level (item state implies tier). The tier-stratified format preserves all existing invariants and
may surface a new criterion: "pre-check explicitly stratified by rubric tier." Hypothesis: 225/225
plus possible new criterion for tier-stratified pre-check structure.

---

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### GATE SECTION
`(C-20: structural gate — all sections blocked until this section completes; C-31: GATE)`

This section is owned by the Compliance Officer function. All subsequent sections are blocked
until this pre-check is fully output. The pre-check is organized into three tier-blocks
matching the rubric's weight tiers: ESSENTIAL, RECOMMENDED, ASPIRATIONAL.

```
COMPLIANCE PRE-CHECK — corps-scan — GATE SECTION
(C-25: section self-labeled; C-18: C-NN IDs are primary keys throughout;
 C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED three-state vocabulary on every item)

━━━ ESSENTIAL BLOCK (C-01 through C-05) ━━━

[ ] C-01 -- draft org.yaml block present (SCHEDULED):
    DRAFT SECTION produces the org.yaml YAML block.
    STATUS: SCHEDULED — satisfied by DRAFT SECTION.

[ ] C-02 -- team areas derived from repo (SCHEDULED):
    All team names in YAML trace to "YAML name (C-02)" column in SCAN SECTION schema.
    STATUS: SCHEDULED — schema discipline enforced in SCAN SECTION; YAML in DRAFT SECTION.

[ ] C-03 -- group structure present (SCHEDULED):
    org.yaml contains at least one named group container above teams.
    STATUS: SCHEDULED — required structural element in DRAFT SECTION.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team in YAML lists 2+ named roles. No generic placeholders.
    STATUS: SCHEDULED — enforced by DRAFT SECTION template.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions in any section.
    STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit; constraint recorded.

━━━ RECOMMENDED BLOCK (C-06 through C-08) ━━━

[ ] C-06 -- pivot mode declared with rationale (SCHEDULED):
    DELIBERATE SECTION names the selected mode and cites a specific schema row for rationale.
    STATUS: SCHEDULED — satisfied by DELIBERATE SECTION.

[ ] C-07 -- exec office placeholder present (SCHEDULED):
    org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required element in DRAFT SECTION YAML.

[ ] C-08 -- amend options listed (SCHEDULED):
    At least 2 named, actionable amend options in FINALIZE SECTION.
    STATUS: SCHEDULED — satisfied by FINALIZE SECTION.

━━━ ASPIRATIONAL BLOCK (selected forward commitments) ━━━

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema, C-NN column headers, self-labeled,
    multi-criterion header (SCHEDULED):
    SCAN SECTION header reads "C-26: C-11 + C-21 satisfier — SCAN SECTION; C-22: self-labeled".
    Columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    STATUS: SCHEDULED — satisfied by SCAN SECTION.

[ ] C-23+C-27 -- pivot deliberation, tri-part Evidence For/Against/Assessment (SCHEDULED):
    DELIBERATE SECTION enumerates all 4 pivot modes with tri-part triad each.
    Selection cites a specific SCAN SECTION schema row by "Repo signal" value.
    STATUS: SCHEDULED — satisfied by DELIBERATE SECTION.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced in FINALIZE SECTION.

[ ] C-30 -- post-write multi-criterion declaration (SCHEDULED):
    FINALIZE SECTION post-write block cites 4+ C-NN IDs simultaneously, including at least
    one essential-tier C-NN (C-34 requirement).
    STATUS: SCHEDULED — satisfied by FINALIZE SECTION.
```

C-15 satisfied: pre-check names C-01 through C-08, C-11+C-21+C-22+C-25+C-26, C-23+C-27,
C-16, C-30 as requirements.
C-17 satisfied: all SCHEDULED items are forward commitments to named future sections.
C-18 satisfied: C-NN IDs (including compound bundles) are primary keys throughout.
C-28 satisfied: SCHEDULED/ACKNOWLEDGED/CONFIRMED markers present on every item.
C-29 satisfied: "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" are compound bundles on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all appear on actual pre-check items.
C-35 satisfied: C-05 STATUS: ACKNOWLEDGED with named violation consequence in ESSENTIAL BLOCK.
Tier-stratified structure: ESSENTIAL / RECOMMENDED / ASPIRATIONAL blocks each explicitly named.

GATE SECTION complete. SCAN SECTION may proceed.

---

### SCAN SECTION
`(C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled; C-31: SCAN; C-33: pre-YAML bracket)`

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests, workspace configs. For each detected organizing signal, add one row. Every
team area in the YAML must match a "YAML name (C-02)" cell exactly.

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-25: section self-labeled; C-31: SCAN SECTION — inventory precedes deliberation and YAML
## C-33: this is the pre-YAML bracket position for the C-26 multi-criterion pattern

| Repo signal       | Signal type              | YAML name (C-02) | Proposed roles (C-04)       | Detection evidence (C-09)     |
|-------------------|--------------------------|------------------|-----------------------------|-------------------------------|
| [path/name]       | [dir/service/domain/cfg] | [exact YAML key] | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]             | [...]                    | [...]            | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row.
- Cap at 8 rows.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

SCAN SECTION complete. DELIBERATE SECTION may proceed.

---

### DELIBERATE SECTION
`(C-25: C-23 + C-27 satisfier; C-31: DELIBERATE)`

Prerequisite: GATE SECTION and SCAN SECTION complete. Signal Schema available. No YAML.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-31: DELIBERATE SECTION — pivot selection precedes YAML production

directory mode:
  Evidence For: [schema rows by "Repo signal" value supporting directory clustering]
  Evidence Against: [absent or counter-indicating signals]
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

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific SCAN SECTION schema row ("Repo signal" value)
  that most strongly favors the selected mode]
```

DELIBERATE SECTION complete. DRAFT SECTION may proceed.

---

### DRAFT SECTION
`(C-25: section self-labeled; C-01 satisfier — org.yaml; C-31: DRAFT)`

Pre-YAML traceability statement (required):
> "Drafting org.yaml. Team names from SCAN SECTION Signal Schema 'YAML name (C-02)'.
> Pivot: [DELIBERATE SECTION selection]. C-05 ACKNOWLEDGED: no .craft/roles/ in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE SECTION selected mode]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From SCAN exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate from corps-build.
      #   Group-level governance: Advocates share context across teams in this group.
      teams:
        - name: "[YAML name — exact match to SCAN schema 'YAML name (C-02)' column]"
          # schema-signal: [SCAN 'Repo signal' value — satisfies C-09]
          roles:
            - [Named role from SCAN "Proposed roles (C-04)" column]
            - [Named role from SCAN "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

DRAFT SECTION complete. FINALIZE SECTION may proceed.

---

### FINALIZE SECTION
`(C-25: section self-labeled; C-26: C-14 + C-30 satisfier; C-31: FINALIZE; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — org.yaml — FINALIZE SECTION
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction;
 C-30: this block cites 9 criteria simultaneously;
 C-33: this is the post-YAML bracket position — SCAN SECTION was the pre-YAML position;
 C-34: essential-tier C-02 cited in this post-write inventory)

[ ] All team names match SCAN schema "YAML name (C-02)" rows       STATUS: [CONFIRMED / FAIL]
[ ] All teams have 2+ named roles                                  STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                    STATUS: [CONFIRMED / FAIL]
[ ] At least one group container present                           STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                        STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)                STATUS: [CONFIRMED / FAIL]
[ ] Tri-part pivot deliberation in DELIBERATE SECTION (C-27)       STATUS: [CONFIRMED / FAIL]
[ ] All sections carry C-NN self-label (C-25)                      STATUS: [CONFIRMED / FAIL]
[ ] Tier-stratified GATE pre-check (ESSENTIAL/RECOMMENDED/ASPIRATIONAL) STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: GATE SECTION pre-check is the pre-YAML gate; this FINALIZE SECTION
block is the post-YAML gate. Both present.
C-33 symmetric bracket: SCAN SECTION header (C-11+C-21) is the pre-YAML position;
this FINALIZE SECTION header (C-14+C-30) is the post-YAML position. Both present.
C-30 multi-criterion declaration: this block cites C-14, C-02, C-24, C-27, C-25, C-26,
C-29, C-32, C-33 simultaneously — 9 criteria.
C-34: essential-tier C-02 present in this post-write inventory alongside 8 aspirationals.
```

```
## Amend Options — FINALIZE SECTION
## (C-25: section self-labeled; C-16: debt-framing on each option)

AMEND-A: Switch pivot mode
  Current: [DELIBERATE SECTION mode] | Basis: [schema row citation]
  Debt if skipped: Misaligned pivot clusters schema rows incorrectly. All downstream corps-*
    skills (corps-build, corps-pr, corps-committee, corps-rob) inherit the misalignment.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [SCAN exec inference]
  Debt if skipped: Exec-office name propagates verbatim into corps-rob governance artifacts
    and corps-committee appointment templates with no downstream correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping principle: [pivot + schema clustering]
  Debt if skipped: Misaligned groups co-locate Inertia Advocates with conflicting status-quo
    frames, degrading corps-committee review signal coherence across all review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R8 V-02). Tier-stratified GATE pre-check: ESSENTIAL BLOCK (C-01–C-05),
> RECOMMENDED BLOCK (C-06–C-08), ASPIRATIONAL BLOCK (C-11+C-21+C-22+C-25+C-26, C-23+C-27,
> C-16, C-30). C-35: C-05 ACKNOWLEDGED in ESSENTIAL BLOCK, violation consequence named.
> C-33: SCAN SECTION (C-11+C-21) and FINALIZE SECTION (C-14+C-30) bracket YAML symmetrically.
> C-34: C-02 in 9-criterion post-write. Draft-only."

---

## V-03 — Lifecycle Emphasis: Cross-Phase I/O Contracts on Every Phase Header

**Axis**: Lifecycle emphasis
**Hypothesis**: Phases in R7 variations declare structural gates and execution states but do not
formally declare their inputs (consumed from prior phase) and outputs (produced for next phase).
Adding an I/O contract block to each phase header — "INPUTS: [what, from which prior phase]" /
"OUTPUTS: [what, for which next phase]" — makes phase dependencies explicit and auditable. A
reviewer can verify the contract is satisfied by checking that the named inputs arrive and the
named outputs depart. This may surface a new criterion: "phase I/O contract declared per phase."
Hypothesis: 225/225 plus possible new criterion.

---

You are running `corps-scan`. Work through five named phases in strict sequence. Each phase
header includes a formal I/O contract declaring its inputs and outputs. No phase may begin
until the preceding phase's outputs are complete.

**Universal labeling rule (C-25)**: Every section must carry a C-NN self-label.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### GATE PHASE
`(C-20: structural gate; C-31: GATE PHASE; C-25: section self-labeled)`

```
INPUTS:  none (entry point)
OUTPUTS: compliance pre-check (consumed by all subsequent phases)
```

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE
(C-25: section self-labeled; C-18: C-NN IDs primary keys; C-32: three-state vocabulary)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line.
    STATUS: CONFIRMED — precedes this pre-check and all subsequent phases.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12. Draft-only statement appears before any inventory or YAML.
    STATUS: CONFIRMED — C-12 names and locates the boundary.

[ ] C-05 -- no .craft/roles/ files:
    No .craft/roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated; constraint recorded.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema with C-NN columns, multi-criterion header
    (SCHEDULED):
    SCAN PHASE produces Signal Schema. Header reads "C-26: C-11 + C-21 satisfier — SCAN PHASE".
    Columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)".
    STATUS: SCHEDULED — satisfied by SCAN PHASE.

[ ] C-23+C-27 -- pivot deliberation with tri-part triad (SCHEDULED):
    DELIBERATE PHASE produces pivot candidate table with Evidence For/Against/Assessment.
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, teams from schema, named roles (SCHEDULED):
    DRAFT PHASE produces org.yaml block with all structural requirements.
    STATUS: SCHEDULED — satisfied by DRAFT PHASE.

[ ] C-16+C-30 -- debt-framed amend options, 4+ criterion post-write (SCHEDULED):
    FINALIZE PHASE produces amend options (debt-framed) and post-write criterion inventory.
    STATUS: SCHEDULED — satisfied by FINALIZE PHASE.
```

C-15 satisfied: pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27,
C-01+C-02+C-03+C-04, C-16+C-30 as requirements.
C-17: all SCHEDULED items are forward commitments.
C-18: C-NN IDs are primary keys throughout.
C-28: SCHEDULED/CONFIRMED/ACKNOWLEDGED on every item.
C-29: compound bundles "C-11+C-21+C-22+C-25+C-26", "C-23+C-27", "C-01+C-02+C-03+C-04",
"C-16+C-30" on single items.
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 ACKNOWLEDGED with named violation consequence.

GATE PHASE complete. SCAN PHASE may begin.

---

### SCAN PHASE
`(C-25: section self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

```
INPUTS:  compliance pre-check (from GATE PHASE — boundary constraints active)
OUTPUTS: Signal Schema (consumed by DELIBERATE PHASE for pivot deliberation;
         consumed by DRAFT PHASE for team name sourcing and role population)
```

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests, workspace configs, domain-language signals.

#### Signal Schema `(C-26: C-11 + C-21 satisfier — SCAN PHASE; C-22: self-labeled header)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-25: section self-labeled; C-31: SCAN PHASE — inventory only, no deliberation or YAML
## C-33: pre-YAML bracket position for C-26 multi-criterion pattern

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- "YAML name (C-02)": exact YAML key — no divergence.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence per row.
- Cap at 8 rows. Exec office inference row if signal available.
```

SCAN PHASE complete. DELIBERATE PHASE may begin.

---

### DELIBERATE PHASE
`(C-25: section self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

```
INPUTS:  Signal Schema (from SCAN PHASE — rows and "Repo signal" values are citation targets)
OUTPUTS: selected pivot mode + rationale citing schema row (consumed by DRAFT PHASE)
```

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation before selection; C-27: tri-part triad
## C-31: DELIBERATE PHASE — no YAML before this deliberation is complete

directory mode:
  Evidence For: [schema rows by "Repo signal" value]
  Evidence Against: [absent or counter-indicating signals]
  Assessment: [strong / possible / weak]

concept mode:
  Evidence For: [schema rows where "Signal type" = domain/concept]
  Evidence Against: [absent DDD naming]
  Assessment: [strong / possible / weak]

service mode:
  Evidence For: [schema rows where "Signal type" = service]
  Evidence Against: [absent manifests]
  Assessment: [strong / possible / weak]

domain mode:
  Evidence For: [bounded-context signals in schema]
  Evidence Against: [absent domain language]
  Assessment: [strong / possible / weak]

Selected pivot mode: [mode]
Rationale: [one sentence citing specific schema row by "Repo signal" value]
```

DELIBERATE PHASE complete. DRAFT PHASE may begin.

---

### DRAFT PHASE
`(C-25: section self-labeled; C-01 satisfier; C-31: DRAFT PHASE)`

```
INPUTS:  Signal Schema (from SCAN PHASE — "YAML name (C-02)" column is source of all team names;
                         "Proposed roles (C-04)" column populates roles)
         Selected pivot mode (from DELIBERATE PHASE — determines group clustering)
OUTPUTS: org.yaml draft block (consumed by FINALIZE PHASE for post-write verification)
```

> "Drafting org.yaml. Team names from SCAN PHASE Signal Schema 'YAML name (C-02)'. Pivot:
> [DELIBERATE PHASE selection]. C-05 ACKNOWLEDGED in GATE pre-check: no .craft/roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [DELIBERATE PHASE selected mode]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From SCAN PHASE exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24): every team in this group receives one Inertia
      # Advocate from corps-build. Group-level governance applies.
      teams:
        - name: "[YAML name — exact match to SCAN PHASE schema]"
          # schema-signal: [SCAN PHASE "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from SCAN PHASE "Proposed roles (C-04)"]
            - [Named role from SCAN PHASE "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build
```

DRAFT PHASE complete. FINALIZE PHASE may begin.

---

### FINALIZE PHASE
`(C-25: section self-labeled; C-26: C-14+C-30 satisfier; C-31: FINALIZE PHASE; C-33: post-YAML bracket)`

```
INPUTS:  org.yaml draft (from DRAFT PHASE — all teams, groups, and roles to verify)
         Pivot mode + deliberation (from DELIBERATE PHASE — to confirm C-27 triad was present)
         Compliance pre-check (from GATE PHASE — constraints to confirm were not violated)
OUTPUTS: post-write verification, amend options (terminal outputs — no subsequent phases)
```

```
POST-WRITE VERIFICATION — org.yaml — FINALIZE PHASE
(C-25: section self-labeled; C-19: criterion IDs cited at point of satisfaction;
 C-30: 9 criteria cited simultaneously; C-33: post-YAML bracket position;
 C-34: essential-tier C-02 cited in this inventory)

[ ] Team names match SCAN schema "YAML name (C-02)" rows     STATUS: [CONFIRMED / FAIL]
[ ] All teams have 2+ named roles (no generics)              STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                              STATUS: [CONFIRMED / FAIL]
[ ] At least one group container present                     STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                  STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)          STATUS: [CONFIRMED / FAIL]
[ ] Tri-part pivot deliberation present (C-27)               STATUS: [CONFIRMED / FAIL]
[ ] All phases carry C-NN self-label (C-25)                  STATUS: [CONFIRMED / FAIL]
[ ] I/O contracts present on all phases                      STATUS: [CONFIRMED / FAIL]

C-14: GATE PHASE pre-check is pre-YAML gate; this FINALIZE PHASE block is post-YAML gate.
C-33: SCAN PHASE header (C-11+C-21) is pre-YAML bracket; this header (C-14+C-30) is
  post-YAML bracket. Both positions present.
C-30: this block cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria.
C-34: essential-tier C-02 present in post-write inventory alongside 8 aspirationals.
```

```
## Amend Options — FINALIZE PHASE
## (C-25: section self-labeled; C-16: debt-framing on all options)

AMEND-A: Switch pivot mode
  Current: [DELIBERATE PHASE mode] | Basis: [schema row citation]
  Debt if skipped: All downstream corps-* skills inherit misaligned clustering.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [SCAN PHASE inference]
  Debt if skipped: Name propagates into corps-rob and corps-committee with no correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Debt if skipped: Misaligned Inertia Advocate grouping degrades corps-committee signal coherence.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R8 V-03). I/O contracts on all 5 phases: GATE (no inputs), SCAN (schema),
> DELIBERATE (schema→pivot), DRAFT (schema+pivot→yaml), FINALIZE (yaml+pivot+precheck→verify).
> C-33: SCAN PHASE header (C-11+C-21) and FINALIZE PHASE header (C-14+C-30) bracket YAML.
> C-34: C-02 in 9-criterion post-write. C-35: C-05 ACKNOWLEDGED in GATE pre-check. Draft-only."

---

## V-04 — Role Sequence + Output Format: Criterion Satisfaction Chain Trace in Closing Summary

**Axis combination**: Role sequence + output format
**Hypothesis**: R7 variations close with a summary paragraph that confirms which criteria were
satisfied. A stronger form traces each major criterion through its full lifecycle: where it was
committed (pre-check item and state), which phase/role satisfied it, and where it was confirmed
(post-write line). The chain makes every criterion's path from commitment to confirmation
auditable end-to-end without consulting the rest of the output. This may surface a new criterion:
"criterion satisfaction chain trace in closing summary." Hypothesis: 225/225 plus possible new
criterion for full lifecycle tracing.

---

You are running `corps-scan`. Work through four named roles in strict sequence.
**ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Every section output by any role must carry a C-NN
self-label. No unlabeled sections.

**HARD BOUNDARY (C-12 satisfier)**: This output is a draft org.yaml for human review.
No `.craft/roles/` files will be written in this response.

---

### ROLE 1 — GATE PHASE / COMPLIANCE OFFICER
`(C-20: structural gate; C-31: GATE PHASE; C-25: section self-labeled)`

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE / ROLE 1
(C-25: section self-labeled; C-18: C-NN IDs primary keys; C-32: three-state vocabulary)

[ ] C-12 -- draft boundary front-loaded:
    STATUS: CONFIRMED — "HARD BOUNDARY" is first substantive line.

[ ] C-13 -- self-referential confirmation:
    STATUS: CONFIRMED — C-12 named and located above this pre-check.

[ ] C-05 -- no .craft/roles/ files:
    STATUS: ACKNOWLEDGED — essential failure if violated; constraint chain: GATE (ACKNOWLEDGED)
    → propagates to all roles as a hard limit; no post-write state can override it.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema, C-NN columns, multi-criterion header (SCHEDULED):
    Satisfaction chain: GATE (ACKNOWLEDGED in this item) → SCAN (satisfied: schema production)
    → FINALIZE (confirmed: post-write item checks schema).
    STATUS: SCHEDULED — satisfied by SCAN PHASE / ROLE 2.

[ ] C-23+C-27 -- pivot deliberation, tri-part triad (SCHEDULED):
    Satisfaction chain: GATE (SCHEDULED) → DELIBERATE (satisfied) → FINALIZE (confirmed).
    STATUS: SCHEDULED — satisfied by DELIBERATE PHASE / ROLE 3.

[ ] C-01+C-02+C-03+C-04 -- org.yaml with groups, schema-traced teams, named roles (SCHEDULED):
    Satisfaction chain: GATE (SCHEDULED) → DRAFT+FINALIZE (satisfied) → FINALIZE post-write
    (confirmed: checklist items 1–4).
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.

[ ] C-16+C-30 -- debt-framed amend options, multi-criterion post-write (SCHEDULED):
    Satisfaction chain: GATE (SCHEDULED) → DRAFT+FINALIZE amend section (C-16 satisfied) +
    post-write block (C-30 satisfied) → closing summary chain trace (confirmed).
    STATUS: SCHEDULED — satisfied by DRAFT+FINALIZE PHASE / ROLE 4.
```

C-29 satisfied: compound bundles "C-11+C-21+C-22+C-25+C-26", "C-23+C-27",
"C-01+C-02+C-03+C-04", "C-16+C-30" on single items.
C-32 satisfied: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35 satisfied: C-05 ACKNOWLEDGED with named violation consequence and propagation note.

GATE PHASE / ROLE 1 complete. SCAN PHASE / ROLE 2 may begin.

---

### ROLE 2 — SCAN PHASE / REPO ARCHAEOLOGIST
`(C-25: section self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN PHASE; C-33: pre-YAML bracket)`

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`, manifests,
workspace configs, domain-language signals.

#### Signal Schema `(C-26: C-11 + C-21 satisfier — SCAN PHASE / precedes YAML; C-22: self-labeled header)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-25: section self-labeled; C-31: SCAN PHASE; C-33: pre-YAML bracket position

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |

Rules: minimum 2 rows; exact YAML name; named roles only; one-sentence evidence; cap 8 rows.
Exec office inference: [term or "no signal — placeholder"]
```

SCAN PHASE / ROLE 2 complete. DELIBERATE PHASE / ROLE 3 may begin.

---

### ROLE 3 — DELIBERATE PHASE / PIVOT ANALYST
`(C-25: section self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE PHASE)`

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23+C-27: tri-part deliberation; C-31: DELIBERATE PHASE

directory mode:
  Evidence For: [schema rows by "Repo signal" value]
  Evidence Against: [counter signals or absences]
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
Rationale: [one sentence citing specific SCAN PHASE schema row by "Repo signal" value]
```

DELIBERATE PHASE / ROLE 3 complete. DRAFT+FINALIZE PHASE / ROLE 4 may begin.

---

### ROLE 4 — DRAFT+FINALIZE PHASE / ORG DRAFTER
`(C-25: section self-labeled; C-01 satisfier; C-31: DRAFT+FINALIZE PHASE)`

> "Drafting org.yaml. Team names from ROLE 2 Signal Schema 'YAML name (C-02)'. Pivot: [ROLE 3
> selection]. C-05 ACKNOWLEDGED in GATE: no .craft/roles/ content."

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
      # Inertia Advocate governance (C-24): every team receives one from corps-build.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema]"
          # schema-signal: [ROLE 2 "Repo signal" — satisfies C-09]
          roles:
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            - [Named role from ROLE 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build
```

#### Post-Write Verification `(C-25: section self-labeled; C-26: C-14+C-30 satisfier; C-33: post-YAML bracket)`

```
POST-WRITE VERIFICATION — DRAFT+FINALIZE PHASE / ROLE 4
(C-19: criterion IDs cited at point of satisfaction; C-30: 9 criteria cited simultaneously;
 C-33: post-YAML bracket — SCAN PHASE was pre-YAML bracket; C-34: C-02 essential in inventory)

[ ] Team names match ROLE 2 schema "YAML name (C-02)"       STATUS: [CONFIRMED / FAIL]
[ ] All teams have 2+ named roles                           STATUS: [CONFIRMED / FAIL]
[ ] exec-office present                                     STATUS: [CONFIRMED / FAIL]
[ ] At least one group container                            STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content                                STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)         STATUS: [CONFIRMED / FAIL]
[ ] Tri-part pivot deliberation in ROLE 3 (C-27)            STATUS: [CONFIRMED / FAIL]
[ ] All roles carry C-NN self-label (C-25)                  STATUS: [CONFIRMED / FAIL]
[ ] Satisfaction chain trace in closing summary             STATUS: [CONFIRMED / FAIL]

C-14: GATE pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: SCAN PHASE header (C-11+C-21) and this header (C-14+C-30) bracket YAML symmetrically.
C-30: cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria.
C-34: essential C-02 present alongside 8 aspirationals in this post-write inventory.
```

#### Amend Options `(C-25: section self-labeled; C-08+C-16 satisfier)`

```
AMEND-A: Switch pivot mode | Debt: downstream corps-* inherit misalignment.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office | Debt: name propagates to corps-rob and corps-committee; no
  downstream correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure | Debt: misaligned Inertia Advocate grouping degrades
  corps-committee signal coherence across all review cycles.
  Command: /corps-scan --groups "[description]"
```

#### Criterion Satisfaction Chain Trace `(C-25: section self-labeled — closing summary)`

```
## Criterion Satisfaction Chain Trace — corps-scan — R8 V-04
## Each major criterion: committed (pre-check) → satisfied (phase) → confirmed (post-write)

C-12: GATE ROLE 1 pre-check CONFIRMED → declared as first line of output → N/A (no post-write
  confirmation needed: structural position is self-confirming).

C-05: GATE ROLE 1 pre-check ACKNOWLEDGED → constraint propagated to all roles → post-write
  item "No .craft/roles/ content" STATUS: CONFIRMED.

C-11+C-21+C-22+C-25+C-26: GATE ROLE 1 pre-check SCHEDULED (compound bundle) → SCAN PHASE
  Signal Schema satisfied (schema rows present, C-NN column headers present, header self-labeled,
  multi-criterion header) → post-write item "team names match schema" STATUS: CONFIRMED.

C-23+C-27: GATE ROLE 1 pre-check SCHEDULED (compound bundle) → DELIBERATE PHASE tri-part
  deliberation satisfied (all 4 modes, Evidence For/Against/Assessment each) → post-write
  item "tri-part pivot deliberation present" STATUS: CONFIRMED.

C-01+C-02+C-03+C-04: GATE ROLE 1 pre-check SCHEDULED (compound bundle) → DRAFT+FINALIZE
  PHASE org.yaml satisfied (YAML block present, team names from schema, groups container,
  named roles per team) → post-write items 1–4 STATUS: CONFIRMED.

C-16+C-30: GATE ROLE 1 pre-check SCHEDULED (compound bundle) → DRAFT+FINALIZE amend section
  (debt-framed options) + post-write block (9-criterion inventory) satisfied → this chain
  trace confirms C-30 at closing summary.

C-33: SCAN PHASE header (C-11+C-21 multi-criterion) = pre-YAML bracket →
  post-write header (C-14+C-30 multi-criterion) = post-YAML bracket → both confirmed.

C-34: post-write block cites C-02 (essential) alongside C-14/C-24/C-27/C-25/C-26/C-29/C-32/C-33
  — essential criterion present in inventory → confirmed at post-write declaration.

C-35: C-05 in GATE pre-check carries STATUS: ACKNOWLEDGED with named consequence →
  confirmed by post-write item "No .craft/roles/ content" STATUS: CONFIRMED — the constraint
  that was ACKNOWLEDGED was not violated.
```

---

## V-05 — Phrasing Register + Lifecycle Emphasis: Imperative Voice with Anti-Pattern Exclusion Gates

**Axis combination**: Phrasing register + lifecycle emphasis
**Hypothesis**: R7 variations encode what each phase MUST produce but not what each phase MUST NOT
produce. Adding a structural EXCLUSION GATE to every phase — a short list of output types
explicitly forbidden in that phase — converts implicit phase boundaries into structural constraints.
Combined with imperative phrasing throughout ("Walk. Detect. Do not select pivot mode yet."),
this makes the phase isolation model self-documenting. May surface a new criterion: "anti-pattern
exclusion gate per phase." Hypothesis: 225/225 plus possible new criterion.

---

Run `corps-scan`. Five phases. Strict sequence. Do not enter a phase until the prior phase is
complete. **Phases 2–5 are blocked until Phase 1 outputs its pre-check.**

**Universal labeling rule (C-25)**: Label every section with a C-NN annotation. No exceptions.

**HARD BOUNDARY (C-12 satisfier)**: Draft org.yaml for human review only.
No `.craft/roles/` files. No role file content. No role-creation instructions.

---

### PHASE 1 — GATE
`(C-20: structural gate; C-31: GATE; C-25: section self-labeled)`

```
EXCLUSION GATE — PHASE 1:
This phase MUST NOT produce: repo scanning, signal inventory, pivot deliberation, YAML.
Any of the above appearing in PHASE 1 is a phase violation.
```

```
COMPLIANCE PRE-CHECK — corps-scan — GATE PHASE
(C-25: section self-labeled; C-18: C-NN IDs primary keys; C-32: three-state vocabulary)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is first substantive line.
    STATUS: CONFIRMED — precedes all repo scanning, deliberation, and YAML.

[ ] C-13 -- self-referential confirmation:
    This item confirms C-12. Draft-only statement precedes all content in this response.
    STATUS: CONFIRMED.

[ ] C-05 -- no .craft/roles/ files:
    Forbidden output type. No .craft/roles/ content anywhere.
    STATUS: ACKNOWLEDGED — essential failure if violated; violation supersedes all other scores.

[ ] C-11+C-21+C-22+C-25+C-26 -- signal schema with C-NN columns, multi-criterion header:
    Phase 2 (SCAN) produces this. Header must read "C-26: C-11 + C-21 satisfier".
    STATUS: SCHEDULED — committed to PHASE 2.

[ ] C-23+C-27 -- pivot deliberation with tri-part triad:
    Phase 3 (DELIBERATE) produces this. All 4 modes with Evidence For/Against/Assessment.
    STATUS: SCHEDULED — committed to PHASE 3.

[ ] C-01+C-02+C-03+C-04 -- org.yaml block, groups, schema-traced teams, named roles:
    Phase 4 (DRAFT) produces this. All team names must trace to Phase 2 schema.
    STATUS: SCHEDULED — committed to PHASE 4.

[ ] C-16+C-30 -- debt-framed amend options, multi-criterion post-write:
    Phase 5 (FINALIZE) produces debt-framed amends and 4+ criterion post-write.
    STATUS: SCHEDULED — committed to PHASE 5.
```

C-29: compound bundles "C-11+C-21+C-22+C-25+C-26", "C-23+C-27", "C-01+C-02+C-03+C-04",
"C-16+C-30".
C-32: CONFIRMED / SCHEDULED / ACKNOWLEDGED all present.
C-35: C-05 ACKNOWLEDGED with named violation consequence.

PHASE 1 complete. PHASE 2 may begin.

---

### PHASE 2 — SCAN
`(C-25: section self-labeled; C-26: C-11+C-21 satisfier; C-31: SCAN; C-33: pre-YAML bracket)`

```
EXCLUSION GATE — PHASE 2:
This phase MUST NOT produce: pivot mode selection, pivot deliberation, YAML blocks,
.craft/roles/ content, amend options, post-write verification.
Any of the above appearing in PHASE 2 is a phase violation.
```

Walk the repo. Detect organizing signals. Populate the Signal Schema. Nothing else.

#### Signal Schema `(C-26: C-11 + C-21 satisfier — SCAN PHASE / precedes YAML; C-22: self-labeled header; C-33: pre-YAML bracket)`

```
## Signal Schema — {{date}}
## C-26: C-11 satisfier (pre-YAML inventory) + C-21 satisfier (C-NN-labeled columns)
## C-25: section self-labeled; C-31: SCAN — detection only; C-33: pre-YAML bracket position

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Do not select pivot mode. Do not produce YAML. Detection only.
Exec office inference: [signal or "no signal — placeholder"]
```

PHASE 2 complete. PHASE 3 may begin.

---

### PHASE 3 — DELIBERATE
`(C-25: section self-labeled; C-23+C-27 satisfier; C-31: DELIBERATE)`

```
EXCLUSION GATE — PHASE 3:
This phase MUST NOT produce: Signal Schema rows, YAML blocks, amend options,
post-write verification, .craft/roles/ content.
Any of the above appearing in PHASE 3 is a phase violation.
```

Assess all four pivot modes. Use Phase 2 schema rows as citation targets. Select one. Nothing
else.

```
## Pivot Mode Deliberation — {{date}}
## C-25: section self-labeled; C-23: deliberation precedes YAML; C-27: tri-part triad
## C-31: DELIBERATE — no YAML until this phase is complete

directory mode:
  Evidence For: [schema rows by "Repo signal"]
  Evidence Against: [counter signals or absences]
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
Rationale: [one sentence citing specific Phase 2 schema row by "Repo signal" value]
```

PHASE 3 complete. PHASE 4 may begin.

---

### PHASE 4 — DRAFT
`(C-25: section self-labeled; C-01 satisfier; C-31: DRAFT)`

```
EXCLUSION GATE — PHASE 4:
This phase MUST NOT produce: .craft/roles/ files, role file markdown, role-creation
instructions, amend options, post-write verification.
Any of the above appearing in PHASE 4 is a phase violation.
```

Draft the org.yaml. Use Phase 2 schema "YAML name (C-02)" column as sole source of team names.
Apply Phase 3 pivot mode for group clustering. Nothing else.

> "Drafting org.yaml. Team names from Phase 2 Signal Schema 'YAML name (C-02)'. Pivot: [Phase 3
> selection]. C-05 ACKNOWLEDGED: no .craft/roles/ content anywhere in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Phase 3 selected mode]
# status: DRAFT — human review required before corps-build

org:
  exec-office:
    name: "[From Phase 2 exec inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24): every team in this group receives one Inertia
      # Advocate from corps-build. Group-level governance context shared across group.
      teams:
        - name: "[YAML name — exact match to Phase 2 schema 'YAML name (C-02)' column]"
          # schema-signal: [Phase 2 "Repo signal" value — satisfies C-09]
          roles:
            - [Named role from Phase 2 "Proposed roles (C-04)"]
            - [Named role from Phase 2 "Proposed roles (C-04)"]
            # Inertia Advocate: auto-added by corps-build — argues status-quo

        - name: "[YAML name 2 — exact match to Phase 2 schema]"
          # schema-signal: [Phase 2 "Repo signal"]
          roles:
            - [Named role from Phase 2 schema]
            - [Named role from Phase 2 schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if Phase 2 schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24): same as Group 1.
      teams: [...]
```

PHASE 4 complete. PHASE 5 may begin.

---

### PHASE 5 — FINALIZE
`(C-25: section self-labeled; C-26: C-14+C-30 satisfier; C-31: FINALIZE; C-33: post-YAML bracket)`

```
EXCLUSION GATE — PHASE 5:
This phase MUST NOT produce: YAML blocks, additional role files, new schema rows, pivot
re-deliberation. All output must be verification, amendment options, and summary only.
Any of the above appearing in PHASE 5 is a phase violation.
```

Verify. Offer amendments. Close.

```
POST-WRITE VERIFICATION — org.yaml — PHASE 5 / FINALIZE
(C-25: section self-labeled; C-19: criterion IDs at point of satisfaction;
 C-30: 9 criteria cited simultaneously; C-33: post-YAML bracket position;
 C-34: essential-tier C-02 in inventory)

[ ] All team names match Phase 2 schema "YAML name (C-02)"   STATUS: [CONFIRMED / FAIL]
[ ] All teams have 2+ named roles (no generics)              STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                              STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                 STATUS: [CONFIRMED / FAIL]
[ ] No .craft/roles/ content in this output                  STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate at team AND group level (C-24)          STATUS: [CONFIRMED / FAIL]
[ ] Tri-part pivot deliberation in Phase 3 (C-27)            STATUS: [CONFIRMED / FAIL]
[ ] All phases carry C-NN self-label (C-25)                  STATUS: [CONFIRMED / FAIL]
[ ] Exclusion gates present on all phases                    STATUS: [CONFIRMED / FAIL]

C-14: Phase 1 pre-check (pre-YAML) and this block (post-YAML) — both present.
C-33: Phase 2 (SCAN) header cites C-11+C-21 = pre-YAML bracket; this header cites C-14+C-30
  = post-YAML bracket. Both positions present, bracket is symmetric.
C-30: this block cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria.
C-34: essential-tier C-02 present in this inventory alongside 8 aspirational criteria.
C-19: criterion IDs cited at point of satisfaction throughout this block.
```

```
## Amend Options — PHASE 5 / FINALIZE
## (C-25: section self-labeled; C-16: debt-framing on all options)

AMEND-A: Switch pivot mode
  Current: [Phase 3 mode] | Basis: [schema row citation]
  Debt if skipped: All downstream corps-* skills (corps-build, corps-pr, corps-committee,
    corps-rob) inherit the misaligned clustering — no correction point after corps-scan.
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Source: [Phase 2 inference]
  Debt if skipped: Name propagates verbatim through corps-rob governance and corps-committee
    appointment templates. No downstream skill corrects exec-office name.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups | Grouping: [Phase 3 pivot + schema clustering]
  Debt if skipped: Inertia Advocates in misaligned groups carry conflicting status-quo frames,
    degrading corps-committee review coherence across all future review cycles.
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete (R8 V-05). Exclusion gates on all 5 phases: PHASE 1 (no scanning),
> PHASE 2 (no pivot selection or YAML), PHASE 3 (no YAML or amends), PHASE 4 (no role files),
> PHASE 5 (no YAML or schema rows). C-33: SCAN header (C-11+C-21) and FINALIZE header (C-14+C-30)
> bracket YAML symmetrically. C-34: C-02 in 9-criterion post-write. C-35: C-05 ACKNOWLEDGED in
> GATE pre-check with named violation consequence. Draft-only."
