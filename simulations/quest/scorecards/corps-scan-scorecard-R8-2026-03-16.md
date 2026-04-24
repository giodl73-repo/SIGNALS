---

## Scorecard — corps-scan R8 (rubric v8, 225 pts)

### Per-Variation Results

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 draft org.yaml | PASS | PASS | PASS | PASS | PASS |
| C-02 team areas from repo | PASS | PASS | PASS | PASS | PASS |
| C-03 group structure | PASS | PASS | PASS | PASS | PASS |
| C-04 named roles per team | PASS | PASS | PASS | PASS | PASS |
| C-05 no .roles/ | PASS | PASS | PASS | PASS | PASS |
| C-06 pivot + rationale | PASS | PASS | PASS | PASS | PASS |
| C-07 exec office | PASS | PASS | PASS | PASS | PASS |
| C-08 amend options | PASS | PASS | PASS | PASS | PASS |
| C-09 detection rationale | PASS | PASS | PASS | PASS | PASS |
| C-10 Inertia Advocate noted | PASS | PASS | PASS | PASS | PASS |
| C-11 pre-YAML inventory | PASS | PASS | PASS | PASS | PASS |
| C-12 draft boundary front-loaded | PASS | PASS | PASS | PASS | PASS |
| **C-13 self-referential check** | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-14 dual-stage bracketing | PASS | PASS | PASS | PASS | PASS |
| C-15–C-35 (all remaining) | PASS | PASS | PASS | PASS | PASS |

**C-13 miss analysis**: V-01 and V-02 place the draft boundary as a "HARD BOUNDARY" block before the pre-check, satisfying C-12. But neither embeds a C-12 or C-13 item as a self-confirming checklist entry. V-03/V-04/V-05 explicitly include `C-12 STATUS: CONFIRMED` and `C-13 STATUS: CONFIRMED — C-12 named and located above` as pre-check items.

### Composite Scores

| Variation | Score | All Essential? | Rank |
|-----------|-------|----------------|------|
| V-03 (I/O contracts) | **225/225** | Yes | 1 (tied) |
| V-04 (chain trace) | **225/225** | Yes | 1 (tied) |
| V-05 (exclusion gates) | **225/225** | Yes | 1 (tied) |
| V-01 (all-essential coverage) | 220/225 | Yes | 4 (tied) |
| V-02 (tier-stratified pre-check) | 220/225 | Yes | 4 (tied) |

### Excellence Signals

**Universal across all R8 (strongest R9 candidate)**: All 5 essential criteria in GATE pre-check with tier-appropriate states — C-01/C-02/C-03/C-04 SCHEDULED, C-05 ACKNOWLEDGED. R7 applied ACKNOWLEDGED only to C-05; R8 extends to full essential-tier accounting.

**V-03 — cross-phase I/O contracts**: Each phase header declares `INPUTS: [artifact, from phase]` / `OUTPUTS: [artifact, for phase]`. Makes the phase dependency graph auditable from headers alone.

**V-04 — criterion satisfaction chain trace**: Closing section traces each criterion: commitment (pre-check item + state) → phase satisfaction → post-write confirmation. Pre-check items also embed mini chains inline.

**V-05 — anti-pattern exclusion gates**: Each phase opens with an EXCLUSION GATE listing forbidden output types, tailored to that phase's contamination risks (e.g., PHASE 2 forbids pivot selection and YAML; PHASE 4 forbids role files).

Scorecard written to `simulations/quest/scorecards/corps-scan-scorecard-R8-2026-03-16.md`.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["All 5 essential criteria in GATE pre-check with tier-appropriate states: C-01/C-02/C-03/C-04 SCHEDULED, C-05 ACKNOWLEDGED — universal across all R8 variations", "Cross-phase I/O contracts on every phase header declaring INPUTS consumed and OUTPUTS produced for next phase (V-03)", "Criterion satisfaction chain trace in closing summary: commitment → phase satisfaction → post-write confirmation per criterion (V-04)", "Anti-pattern exclusion gate per phase listing output types explicitly forbidden in that phase (V-05)"]}
```
6" and "C-23+C-27" compound bundles on single items |
| C-30 post-write multi-criterion | PASS | Post-write cites 9 criteria: C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 |
| C-31 purpose-named phases | PASS | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE |
| C-32 three-state vocabulary | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED on actual pre-check items |
| C-33 symmetric bracket | PASS | SCAN header (C-11+C-21 pre-YAML) + FINALIZE header (C-14+C-30 post-YAML) |
| C-34 essential in post-write | PASS | C-02 cited in 9-criterion post-write inventory |
| C-35 ACKNOWLEDGED on essential | PASS | C-05 STATUS: ACKNOWLEDGED — essential failure if violated |

**Score: 220 / 225** (C-13 FAIL: −5)
All 5 essential: PASS · All 3 recommended: PASS · 26/27 aspirational: PASS

---

## V-02 — Output Format: Tier-Stratified Pre-Check

**Axis**: Output format — pre-check organized into ━━━ ESSENTIAL / RECOMMENDED / ASPIRATIONAL ━━━ tier-blocks

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 draft org.yaml block | PASS | YAML block in DRAFT SECTION |
| C-02 team areas from repo | PASS | Schema-traced teams via "YAML name (C-02)" column |
| C-03 group structure | PASS | Group container in YAML template |
| C-04 named roles per team | PASS | Named roles from schema column |
| C-05 no .roles/ | PASS | ACKNOWLEDGED in ESSENTIAL BLOCK — "essential failure if violated; no partial credit; constraint recorded" |
| C-06 pivot mode + rationale | PASS | DELIBERATE SECTION cites specific schema row |
| C-07 exec office placeholder | PASS | exec-office in YAML template |
| C-08 amend options | PASS | AMEND-A, B, C with commands |
| C-09 detection rationale | PASS | "Detection evidence (C-09)" column with one-sentence evidence |
| C-10 Inertia Advocate noted | PASS | "Inertia Advocate: auto-added by corps-build" in YAML |
| C-11 pre-YAML scan inventory | PASS | Signal Schema in SCAN SECTION precedes YAML |
| C-12 draft boundary front-loaded | PASS | "HARD BOUNDARY" as first substantive line |
| C-13 self-referential check | FAIL | Tier-stratified pre-check lists C-01–C-08 and bundles; no C-12/C-13 self-confirming item present |
| C-14 dual-stage bracketing | PASS | GATE SECTION pre-check + FINALIZE SECTION post-write |
| C-15 rubric criteria in skill | PASS | Pre-check names C-01–C-08 + bundles as requirements |
| C-16 debt-framed amend options | PASS | "Debt if skipped" on all 3 amend options |
| C-17 forward commitment | PASS | All SCHEDULED items committed to named future sections |
| C-18 criterion ID as primary key | PASS | C-NN IDs as primary keys in all three tier blocks |
| C-19 post-write self-labeling | PASS | Post-write cites C-NN IDs at satisfaction |
| C-20 structural role ordering | PASS | GATE SECTION blocks all subsequent sections |
| C-21 schema-typed inventory | PASS | Signal Schema with C-NN-labeled columns |
| C-22 pre-write section labeling | PASS | SCAN SECTION header "C-26: C-11 + C-21 satisfier" |
| C-23 pivot deliberation first | PASS | All 4 candidates in DELIBERATE SECTION before selection |
| C-24 Inertia Advocate at group level | PASS | Group-level Inertia Advocate comment in YAML |
| C-25 universal section labeling | PASS | Universal C-NN labeling rule; all sections labeled |
| C-26 multi-criterion header | PASS | SCAN SECTION + FINALIZE SECTION each cite 2+ criteria |
| C-27 tri-part deliberation | PASS | Evidence For / Against / Assessment on all 4 modes |
| C-28 exec-state on pre-check items | PASS | SCHEDULED/ACKNOWLEDGED on all items in tier blocks |
| C-29 criterion-pair bundling | PASS | "C-11+C-21+C-22+C-25+C-26" and "C-23+C-27" compound bundles |
| C-30 post-write multi-criterion | PASS | Post-write cites 9 criteria simultaneously |
| C-31 purpose-named phases | PASS | GATE / SCAN / DELIBERATE / DRAFT / FINALIZE sections |
| C-32 three-state vocabulary | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED across all tier blocks |
| C-33 symmetric bracket | PASS | SCAN SECTION (C-11+C-21 pre-YAML) + FINALIZE SECTION (C-14+C-30 post-YAML) |
| C-34 essential in post-write | PASS | C-02 cited in 9-criterion post-write |
| C-35 ACKNOWLEDGED on essential | PASS | C-05 STATUS: ACKNOWLEDGED in ESSENTIAL BLOCK |

**Score: 220 / 225** (C-13 FAIL: −5)
All 5 essential: PASS · All 3 recommended: PASS · 26/27 aspirational: PASS

---

## V-03 — Lifecycle Emphasis: Cross-Phase I/O Contracts

**Axis**: Lifecycle emphasis — each phase header carries formal INPUTS/OUTPUTS contracts

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 draft org.yaml block | PASS | YAML block in DRAFT PHASE |
| C-02 team areas from repo | PASS | Schema-traced via "YAML name (C-02)"; I/O contract names schema as input to DRAFT |
| C-03 group structure | PASS | Group container in YAML template |
| C-04 named roles per team | PASS | Named roles from schema |
| C-05 no .roles/ | PASS | ACKNOWLEDGED — "essential failure if violated; constraint recorded" |
| C-06 pivot mode + rationale | PASS | DELIBERATE PHASE cites specific schema row for rationale |
| C-07 exec office placeholder | PASS | exec-office in YAML template |
| C-08 amend options | PASS | AMEND-A, B, C in FINALIZE PHASE |
| C-09 detection rationale | PASS | "Detection evidence (C-09)" column per row |
| C-10 Inertia Advocate noted | PASS | "Inertia Advocate: auto-added by corps-build" in YAML |
| C-11 pre-YAML scan inventory | PASS | Signal Schema in SCAN PHASE precedes YAML |
| C-12 draft boundary front-loaded | PASS | "HARD BOUNDARY" as first substantive line |
| C-13 self-referential check | PASS | C-12 and C-13 both listed as CONFIRMED items in GATE PHASE pre-check; C-13 explicitly confirms C-12 |
| C-14 dual-stage bracketing | PASS | GATE PHASE pre-check (pre-YAML) + FINALIZE PHASE post-write (post-YAML) |
| C-15 rubric criteria in skill | PASS | Pre-check names C-12, C-13, C-05, C-11+C-21+..., C-23+C-27, C-01+C-02+C-03+C-04, C-16+C-30 |
| C-16 debt-framed amend options | PASS | "Debt if skipped" on all 3 amend options |
| C-17 forward commitment | PASS | SCHEDULED items commit to named future phases |
| C-18 criterion ID as primary key | PASS | C-NN IDs as primary keys throughout |
| C-19 post-write self-labeling | PASS | Post-write cites C-NN IDs at satisfaction |
| C-20 structural role ordering | PASS | GATE PHASE structural gate; subsequent phases blocked |
| C-21 schema-typed inventory | PASS | Signal Schema with C-NN-labeled columns |
| C-22 pre-write section labeling | PASS | Signal Schema header self-labels criteria |
| C-23 pivot deliberation first | PASS | All 4 modes deliberated in DELIBERATE PHASE before YAML |
| C-24 Inertia Advocate at group level | PASS | Group-level governance comment on each group element |
| C-25 universal section labeling | PASS | Universal C-NN labeling rule; all phases labeled |
| C-26 multi-criterion header | PASS | SCAN PHASE header (C-11+C-21) + FINALIZE PHASE header (C-14+C-30) |
| C-27 tri-part deliberation | PASS | Evidence For / Against / Assessment on all 4 pivot modes |
| C-28 exec-state on pre-check items | PASS | CONFIRMED/SCHEDULED/ACKNOWLEDGED on every item |
| C-29 criterion-pair bundling | PASS | 4 compound bundles: "C-11+C-21+C-22+C-25+C-26", "C-23+C-27", "C-01+C-02+C-03+C-04", "C-16+C-30" |
| C-30 post-write multi-criterion | PASS | Post-write cites 9 criteria: C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 |
| C-31 purpose-named phases | PASS | GATE / SCAN / DELIBERATE / DRAFT / FINALIZE — all purpose-named |
| C-32 three-state vocabulary | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED on actual items |
| C-33 symmetric bracket | PASS | SCAN PHASE header (C-11+C-21) + FINALIZE PHASE header (C-14+C-30) |
| C-34 essential in post-write | PASS | C-02 cited in 9-criterion post-write inventory |
| C-35 ACKNOWLEDGED on essential | PASS | C-05 STATUS: ACKNOWLEDGED — "essential failure if violated; constraint recorded" |

**Score: 225 / 225**
All 5 essential: PASS · All 3 recommended: PASS · All 27 aspirational: PASS

**New structural feature — cross-phase I/O contracts:**
Each phase header carries a formal contract block:
```
INPUTS:  [what this phase consumes, from which prior phase]
OUTPUTS: [what this phase produces, for which next phase]
```
GATE: INPUTS: none / OUTPUTS: compliance pre-check → all phases
SCAN: INPUTS: compliance pre-check / OUTPUTS: Signal Schema → DELIBERATE + DRAFT
DELIBERATE: INPUTS: Signal Schema / OUTPUTS: pivot mode + rationale → DRAFT
DRAFT: INPUTS: Signal Schema + pivot mode / OUTPUTS: org.yaml draft → FINALIZE
FINALIZE: INPUTS: yaml + pivot + pre-check / OUTPUTS: post-write + amends (terminal)

---

## V-04 — Role Sequence + Output Format: Criterion Satisfaction Chain Trace

**Axis combination**: Role sequence + output format — criterion satisfaction chain trace in closing summary

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 draft org.yaml block | PASS | YAML block in ROLE 4; chain trace confirms |
| C-02 team areas from repo | PASS | Schema-traced; chain trace: "DRAFT+FINALIZE → post-write items 1–4 STATUS: CONFIRMED" |
| C-03 group structure | PASS | Group container in YAML template |
| C-04 named roles per team | PASS | Named roles from schema |
| C-05 no .roles/ | PASS | ACKNOWLEDGED — "essential failure if violated; constraint chain: GATE (ACKNOWLEDGED) → propagates to all roles" |
| C-06 pivot mode + rationale | PASS | DELIBERATE PHASE selects mode citing schema row |
| C-07 exec office placeholder | PASS | exec-office in YAML template |
| C-08 amend options | PASS | AMEND-A, B, C with debt framing |
| C-09 detection rationale | PASS | "Detection evidence (C-09)" column |
| C-10 Inertia Advocate noted | PASS | "Inertia Advocate: auto-added by corps-build" in YAML |
| C-11 pre-YAML scan inventory | PASS | Signal Schema in SCAN PHASE |
| C-12 draft boundary front-loaded | PASS | "HARD BOUNDARY" as first substantive line |
| C-13 self-referential check | PASS | C-12 and C-13 in GATE pre-check as CONFIRMED items; C-13 confirms C-12 |
| C-14 dual-stage bracketing | PASS | GATE pre-check + post-write block — both present; chain trace confirms both |
| C-15 rubric criteria in skill | PASS | Pre-check names C-12, C-13, C-05, bundles as requirements |
| C-16 debt-framed amend options | PASS | "Debt:" inline on all 3 amend options |
| C-17 forward commitment | PASS | SCHEDULED items with satisfaction chain descriptions |
| C-18 criterion ID as primary key | PASS | C-NN IDs as primary keys throughout |
| C-19 post-write self-labeling | PASS | Post-write cites C-NN IDs at satisfaction |
| C-20 structural role ordering | PASS | ROLE 2/3/4 blocked until ROLE 1 pre-check complete |
| C-21 schema-typed inventory | PASS | Signal Schema with C-NN-labeled columns |
| C-22 pre-write section labeling | PASS | Signal Schema header self-labels criteria |
| C-23 pivot deliberation first | PASS | All 4 modes in DELIBERATE PHASE |
| C-24 Inertia Advocate at group level | PASS | Group-level Inertia Advocate governance comment |
| C-25 universal section labeling | PASS | Universal C-NN labeling rule; all roles labeled |
| C-26 multi-criterion header | PASS | SCAN header (C-11+C-21) + post-write header (C-14+C-30) |
| C-27 tri-part deliberation | PASS | Evidence For / Against / Assessment per mode; chain trace confirms |
| C-28 exec-state on pre-check items | PASS | CONFIRMED/SCHEDULED/ACKNOWLEDGED on every item |
| C-29 criterion-pair bundling | PASS | 4 compound bundles; chain trace references bundle items |
| C-30 post-write multi-criterion | PASS | Post-write cites 9 criteria; chain trace traces C-30 satisfaction |
| C-31 purpose-named phases | PASS | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE |
| C-32 three-state vocabulary | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED |
| C-33 symmetric bracket | PASS | SCAN header (C-11+C-21) + FINALIZE header (C-14+C-30) |
| C-34 essential in post-write | PASS | C-02 in 9-criterion post-write inventory |
| C-35 ACKNOWLEDGED on essential | PASS | C-05 ACKNOWLEDGED with propagation note |

**Score: 225 / 225**
All 5 essential: PASS · All 3 recommended: PASS · All 27 aspirational: PASS

**New structural feature — criterion satisfaction chain trace:**
Closing summary section traces every major criterion from commitment → satisfaction → confirmation:
```
C-05: GATE (ACKNOWLEDGED) → constraint propagated → post-write "No .roles/" CONFIRMED.
C-11+C-21+C-22+C-25+C-26: GATE (SCHEDULED) → SCAN PHASE (schema) → post-write CONFIRMED.
C-23+C-27: GATE (SCHEDULED) → DELIBERATE PHASE (tri-part) → post-write CONFIRMED.
C-01+C-02+C-03+C-04: GATE (SCHEDULED) → DRAFT+FINALIZE (org.yaml) → post-write items 1-4 CONFIRMED.
C-35: C-05 ACKNOWLEDGED → constraint not violated → post-write "No .roles/" CONFIRMED.
```
Pre-check items also embed mini satisfaction chains inline per item (e.g., "Satisfaction chain: GATE (SCHEDULED) → SCAN (satisfied: schema production) → FINALIZE (confirmed: post-write item checks schema)").

---

## V-05 — Phrasing Register + Lifecycle Emphasis: Imperative Voice + Anti-Pattern Exclusion Gates

**Axis combination**: Phrasing register + lifecycle emphasis — imperative voice throughout, EXCLUSION GATE per phase

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 draft org.yaml block | PASS | YAML block in PHASE 4 |
| C-02 team areas from repo | PASS | Schema-traced via "YAML name (C-02)"; exclusion gate enforces no schema rows in PHASE 4 |
| C-03 group structure | PASS | Group container in YAML template |
| C-04 named roles per team | PASS | Named roles from schema |
| C-05 no .roles/ | PASS | ACKNOWLEDGED — "violation supersedes all other scores" |
| C-06 pivot mode + rationale | PASS | PHASE 3 selects mode citing specific schema row |
| C-07 exec office placeholder | PASS | exec-office in YAML template |
| C-08 amend options | PASS | AMEND-A, B, C in PHASE 5 |
| C-09 detection rationale | PASS | "Detection evidence (C-09)" column |
| C-10 Inertia Advocate noted | PASS | "Inertia Advocate: auto-added by corps-build" in YAML |
| C-11 pre-YAML scan inventory | PASS | Signal Schema in PHASE 2 precedes YAML |
| C-12 draft boundary front-loaded | PASS | "HARD BOUNDARY" as first substantive line |
| C-13 self-referential check | PASS | C-12 and C-13 in GATE pre-check as CONFIRMED items |
| C-14 dual-stage bracketing | PASS | PHASE 1 pre-check (pre-YAML) + PHASE 5 post-write (post-YAML) |
| C-15 rubric criteria in skill | PASS | Pre-check names C-12, C-13, C-05, bundles as requirements |
| C-16 debt-framed amend options | PASS | "Debt if skipped" on all 3 amend options |
| C-17 forward commitment | PASS | SCHEDULED items committed to named future phases |
| C-18 criterion ID as primary key | PASS | C-NN IDs as primary keys throughout |
| C-19 post-write self-labeling | PASS | Post-write cites C-NN IDs at satisfaction |
| C-20 structural role ordering | PASS | "Phases 2–5 are blocked until Phase 1 outputs its pre-check" |
| C-21 schema-typed inventory | PASS | Signal Schema with C-NN-labeled columns |
| C-22 pre-write section labeling | PASS | Signal Schema header "C-26: C-11 + C-21 satisfier" |
| C-23 pivot deliberation first | PASS | All 4 modes in PHASE 3 before YAML |
| C-24 Inertia Advocate at group level | PASS | Group-level Inertia Advocate comment per group |
| C-25 universal section labeling | PASS | Universal C-NN labeling rule; all phases labeled |
| C-26 multi-criterion header | PASS | PHASE 2 header (C-11+C-21) + PHASE 5 header (C-14+C-30) |
| C-27 tri-part deliberation | PASS | Evidence For / Against / Assessment per mode |
| C-28 exec-state on pre-check items | PASS | CONFIRMED/SCHEDULED/ACKNOWLEDGED on every item |
| C-29 criterion-pair bundling | PASS | 4 compound bundles |
| C-30 post-write multi-criterion | PASS | Post-write cites 9 criteria |
| C-31 purpose-named phases | PASS | PHASE 1 GATE / PHASE 2 SCAN / PHASE 3 DELIBERATE / PHASE 4 DRAFT / PHASE 5 FINALIZE |
| C-32 three-state vocabulary | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED |
| C-33 symmetric bracket | PASS | PHASE 2 header (C-11+C-21) + PHASE 5 header (C-14+C-30) |
| C-34 essential in post-write | PASS | C-02 in 9-criterion post-write inventory |
| C-35 ACKNOWLEDGED on essential | PASS | C-05 STATUS: ACKNOWLEDGED — "violation supersedes all other scores" |

**Score: 225 / 225**
All 5 essential: PASS · All 3 recommended: PASS · All 27 aspirational: PASS

**New structural feature — anti-pattern exclusion gates per phase:**
Each phase opens with an EXCLUSION GATE block listing output types explicitly forbidden in that phase:
- PHASE 1 GATE: "MUST NOT produce: repo scanning, signal inventory, pivot deliberation, YAML."
- PHASE 2 SCAN: "MUST NOT produce: pivot mode selection, pivot deliberation, YAML blocks, .roles/ content, amend options, post-write verification."
- PHASE 3 DELIBERATE: "MUST NOT produce: Signal Schema rows, YAML blocks, amend options, post-write verification, .roles/ content."
- PHASE 4 DRAFT: "MUST NOT produce: .roles/ files, role file markdown, role-creation instructions, amend options, post-write verification."
- PHASE 5 FINALIZE: "MUST NOT produce: YAML blocks, additional role files, new schema rows, pivot re-deliberation."

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (135) | **Total** | All-Ess? |
|-----------|----------------|------------------|--------------------|-----------|----------|
| V-01 | 60 | 30 | 130 | **220** | Yes |
| V-02 | 60 | 30 | 130 | **220** | Yes |
| V-03 | 60 | 30 | 135 | **225** | Yes |
| V-04 | 60 | 30 | 135 | **225** | Yes |
| V-05 | 60 | 30 | 135 | **225** | Yes |

**Golden threshold (80 pts + all essential)**: All 5 variations pass.

---

## Ranking

1. **V-03, V-04, V-05** — tied at 225/225 (ceiling)
2. **V-01, V-02** — tied at 220/225 (C-13 miss)

---

## Excellence Signals

**From V-03 (cross-phase I/O contracts)**:
- Each phase header carries a formal `INPUTS: / OUTPUTS:` contract block naming the exact artifact flowing between phases.
- INPUTS names the consuming phase's source artifact; OUTPUTS names what it produces and who consumes it.
- Makes phase dependency chain independently auditable: a reviewer can verify each phase's inputs arrived from the expected prior phase and outputs were consumed by the expected next phase.

**From V-04 (criterion satisfaction chain trace)**:
- Closing summary section traces each major criterion through its full lifecycle: committed (pre-check item + state) → satisfied (phase + what was produced) → confirmed (post-write line + status).
- Pre-check items also embed mini satisfaction chains inline, so each SCHEDULED item already declares its downstream confirmation path at commitment time.
- Makes the entire rubric-to-output mapping auditable from a single closing section: no need to scan the full output to verify criterion satisfaction.

**From V-05 (anti-pattern exclusion gates)**:
- Each phase opens with an EXCLUSION GATE block explicitly listing output types forbidden in that phase.
- Converts implicit phase isolation (currently enforced only by role/phase sequencing) into structural anti-pattern assertions.
- PHASE 2 gate forbids pivot selection and YAML; PHASE 4 gate forbids role files and amend options — each gate is tailored to the specific violations most likely to contaminate that phase.

**Universal across all R8 variations (all-essential pre-check coverage)**:
- All 5 variations account for all 5 essential criteria (C-01 through C-05) in the GATE pre-check with tier-appropriate states:
  - C-01/C-02/C-03/C-04: STATUS SCHEDULED to named future phase/role
  - C-05: STATUS ACKNOWLEDGED with named violation consequence
- R7 converged on C-35 (ACKNOWLEDGED applied to C-05 only); R8 extends this to full essential-tier coverage.
- V-01 lists essentials individually; V-02 uses tier blocks; V-03/V-04/V-05 bundle C-01+C-02+C-03+C-04 as a single compound item plus C-05 ACKNOWLEDGED separately.

---

## New Patterns for R9 Rubric

Four distinct new structural patterns identified:

1. **All-essential pre-check coverage** (universal): All 5 essential criteria in GATE pre-check with tier-appropriate states — C-01–C-04 SCHEDULED (will be demonstrated), C-05 ACKNOWLEDGED (hard boundary). Distinct from C-35 (ACKNOWLEDGED on essential only) — this requires ALL essentials present with appropriate state discrimination.

2. **Cross-phase I/O contracts** (V-03): Each phase header declares INPUTS (consumed from prior phase) and OUTPUTS (produced for next phase) as a formal contract block. Makes the phase dependency graph explicitly auditable from phase headers alone.

3. **Criterion satisfaction chain trace** (V-04): A dedicated closing section that traces each criterion from its pre-check commitment state through the phase that satisfied it to its post-write confirmation line. Inline pre-check items also embed mini satisfaction chains per item.

4. **Anti-pattern exclusion gates per phase** (V-05): Each phase opens with an EXCLUSION GATE block listing output types explicitly forbidden in that phase, tailored to the specific contamination risks of that phase's position in the pipeline.

**Strongest R9 candidate**: All-essential pre-check coverage (universal across all R8 variations — same convergence signal as C-29 in R6 and C-33/C-34/C-35 in R7).

---

## Change Log

| Round | Date | Key Change |
|-------|------|-----------|
| R1 | 2026-03-16 | Initial round — 100 pts |
| R2–R7 | 2026-03-16 | Progressive accumulation to 225 pts / 35 criteria |
| R8 | 2026-03-16 | C-13 miss reveals V-01/V-02 gap; V-03/V-04/V-05 pass all 35; 4 new structural patterns for R9 |
