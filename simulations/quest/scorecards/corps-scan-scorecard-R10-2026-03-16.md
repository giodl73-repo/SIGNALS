# Quest Score — corps-scan R10 (v9 rubric)

## Scoring Framework

**235 pts total** | 60E (5 × 12) + 30R (3 × 10) + 145A (29 × 5) | Golden threshold: 80 pts

---

## V-01 — Role Sequence: Hypothesis-First

**Structure**: GATE (Hypothesis Officer) → SCAN (Repo Archaeologist) → DELIBERATE (Pivot Analyst) → DRAFT+FINALIZE (Org Drafter)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | ROLE 4 YAML block has org:, exec-office:, groups:, teams:, roles: keys |
| C-02 | PASS | Signal Schema "YAML name (C-02)" column enforces tracing; ROLE 4 pre-YAML statement quotes schema column |
| C-03 | PASS | groups: section in YAML template |
| C-04 | PASS | "Proposed roles (C-04)" column; roles listed per team; Inertia Advocate excluded ("auto-added by corps-build") |
| C-05 | PASS | HARD BOUNDARY front-loaded; C-05 STATUS: ACKNOWLEDGED in gate; no role files anywhere |
| C-06 | PASS | DELIBERATE PHASE selects mode with rationale citing ROLE 2 schema row + DARK SIGNALS label |
| C-07 | PASS | exec-office: in YAML template |
| C-08 | PASS | AMEND-A, AMEND-B, AMEND-C all present with commands |
| C-09 | PASS | "Detection evidence (C-09)" labeled column in Signal Schema |
| C-10 | PASS | "# Inertia Advocate: auto-added by corps-build" in team block; group-level C-24 annotation |
| C-11 | PASS | Signal Schema section precedes YAML |
| C-12 | PASS | "HARD BOUNDARY (C-12 satisfier)" is the first substantive output line |
| C-13 | PASS | "[ ] C-12 STATUS: CONFIRMED" self-referentially confirms the constraint appeared before the check |
| C-14 | PASS | GATE pre-check (pre-YAML) + Post-Write Verification (post-YAML) — both present |
| C-15 | PASS | Pre-check names C-05, C-01+C-02+C-03+C-04, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-36+C-37, C-16+C-30 as requirements |
| C-16 | PASS | All three AMEND options carry "Debt if skipped:" consequence text |
| C-17 | PASS | All SCHEDULED items name the future role delivering them (e.g., "SCHEDULED — SCAN PHASE / ROLE 2") |
| C-18 | PASS | C-NN IDs as primary keys on every pre-check item |
| C-19 | PASS | Post-write block header "(C-19: criterion IDs cited at point of satisfaction; C-30: 10 criteria cited...)" |
| C-20 | PASS | "ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check and hypothesis" — structural lock |
| C-21 | PASS | Signal Schema columns labeled "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)" |
| C-22 | PASS | Signal Schema header: "C-26: C-11 + C-21 satisfier — SCAN PHASE / precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket" |
| C-23 | PASS | All 4 modes enumerated before selection; rationale cites specific schema row |
| C-24 | PASS | "# Inertia Advocate governance (C-24): Every team in this group..." on each named group |
| C-25 | PASS | "Universal labeling rule (C-25): Every section output by any role must carry a C-NN self-label. No section may be unlabeled." |
| C-26 | PASS | Multi-criterion headers: "(C-26: C-11 + C-21 satisfier)", "(C-25: section self-labeled; C-26: C-14+C-30 satisfier)" |
| C-27 | PASS | Evidence For / Evidence Against / Assessment triad for all 4 modes |
| C-28 | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED markers on individual pre-check items |
| C-29 | PASS | Compound bundles: "C-11+C-21+C-22+C-25+C-26", "C-23+C-27", "C-36+C-37", "C-16+C-30" |
| C-30 | PASS | Post-write cites 10 criteria: "C-14, C-02, C-24, C-27, C-25, C-26, C-33, C-34, C-36, C-37" |
| C-31 | PASS | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE — purpose-encoded names |
| C-32 | PASS | All three states on actual items: CONFIRMED (C-12), SCHEDULED (C-01+…), ACKNOWLEDGED (C-05) |
| C-33 | PASS | Signal Schema header = pre-YAML bracket; Post-Write header = post-YAML bracket |
| C-34 | PASS | Post-write cites essential C-02 alongside 9 aspirationals |
| C-35 | PASS | "C-05 STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit possible" |
| C-36 | PASS | DARK SIGNALS section after Signal Schema: 4 typed entries (NO-SERVICE-MANIFEST, NO-DDD-LANGUAGE, NO-DOMAIN-BOUNDARY, NO-WORKSPACE-GROUPING), each naming pivot mode impact + Hypothesis Relation field |
| C-37 | PASS | DELIBERATE PHASE Evidence Against cites labels by name (e.g., "DARK SIGNALS: NO-SERVICE-MANIFEST"); AMEND-A: "DARK SIGNALS basis: [LABEL] — rules out [mode]; hypothesis [CONFIRMED/OVERTURNED]" |

**V-01 Score: 235/235** | All essential: PASS

---

## V-02 — Phrasing Register: Detective/Narrative

**Structure**: Phase 1 (GATE/Case File) → Phase 2 (SCAN/What I Found) → Phase 3 (DELIBERATE/What It Means) → Phase 4 (DRAFT+FINALIZE/Deliverable) | DARK SIGNALS titled "WHAT I DIDN'T FIND"

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Phase 4 YAML block complete |
| C-02 | PASS | Signal Schema "YAML name (C-02)" column; team name traceability enforced |
| C-03 | PASS | groups: section present |
| C-04 | PASS | Named roles per team; Inertia Advocate excluded |
| C-05 | PASS | HARD BOUNDARY first line; C-05 ACKNOWLEDGED with golden-failure consequence |
| C-06 | PASS | Phase 3 selects mode with schema row citation |
| C-07 | PASS | exec-office in YAML |
| C-08 | PASS | AMEND-A/B/C with commands |
| C-09 | PASS | "Detection evidence (C-09)" column in schema |
| C-10 | PASS | "Inertia Advocate: auto-added by corps-build — not listed here" in YAML; C-24 group annotation |
| C-11 | PASS | Signal Schema pre-YAML |
| C-12 | PASS | "HARD BOUNDARY" first substantive line |
| C-13 | PASS | C-12 STATUS: CONFIRMED in compliance log |
| C-14 | PASS | Phase 1 pre-check + Phase 4 Verification Log bracket the YAML |
| C-15 | PASS | Compliance log names all required outputs as skill requirements |
| C-16 | PASS | "Debt if skipped:" on all three AMEND options |
| C-17 | PASS | SCHEDULED items name their delivery phase |
| C-18 | PASS | C-NN IDs primary keys in compliance log |
| C-19 | PASS | Verification Log header "(C-33: post-YAML bracket; C-30: 10 criteria cited; C-34: essential C-02)" |
| C-20 | PASS | "Phases 2, 3, and 4 are sealed until Phase 1 produces its compliance log" |
| C-21 | PASS | Signal Schema has C-NN-labeled columns |
| C-22 | PASS | "What I Found — Signal Schema" header: "C-26: C-11 + C-21 satisfier — precedes YAML; C-22: criterion purpose declared in this header" |
| C-23 | PASS | 4 modes enumerated; "My read:" selection cites schema row + DIDN'T FIND label |
| C-24 | PASS | "# Inertia Advocate governance (C-24):" comment at each group |
| C-25 | PASS | Universal labeling rule stated; every section carries C-NN self-label |
| C-26 | PASS | Multi-criterion headers at scan section and finalize section |
| C-27 | PASS | Evidence For / Evidence Against / Verdict triad for all 4 modes |
| C-28 | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED on individual items |
| C-29 | PASS | Compound bundles: "C-11+C-21+C-22+C-25+C-26", "C-01+C-02+C-03+C-04", "C-36+C-37", "C-16+C-30" |
| C-30 | PASS | Verification Log: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37 — 10 criteria |
| C-31 | PASS | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE |
| C-32 | PASS | Three states on actual items |
| C-33 | PASS | Phase 2 Signal Schema header = pre-YAML bracket; Verification Log = post-YAML bracket |
| C-34 | PASS | Essential C-02 in Verification Log alongside 9 aspirationals |
| C-35 | PASS | "C-05 STATUS: ACKNOWLEDGED. If I write any role file content, this output fails golden, regardless of everything else." |
| C-36 | PASS | "WHAT I DIDN'T FIND" section with 4 typed entries (NO-SERVICE-MANIFEST, NO-DDD-LANGUAGE, NO-DOMAIN-BOUNDARY, NO-WORKSPACE-GROUPING), each naming pivot mode consequence |
| C-37 | PASS | Evidence Against cites labels: "WHAT I DIDN'T FIND: NO-WORKSPACE-GROUPING was [ABSENT/PARTIAL]"; AMEND-A: "Basis: WHAT I DIDN'T FIND — [LABEL] was ABSENT" — both cross-references present |

**V-02 Score: 235/235** | All essential: PASS

---

## V-03 — DARK SIGNALS as Structured Evidence Table

**Structure**: 4 roles with table-format DARK SIGNALS (columns: Signal Name | Looked For | Found? | Pivot Modes Affected | Consequence)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | ROLE 4 YAML block complete |
| C-02 | PASS | Signal Schema column enforces tracing |
| C-03 | PASS | groups: section |
| C-04 | PASS | Named roles; no Inertia Advocate |
| C-05 | PASS | HARD BOUNDARY first; ACKNOWLEDGED with consequence |
| C-06 | PASS | ROLE 3 selects mode with rationale |
| C-07 | PASS | exec-office present |
| C-08 | PASS | Three AMEND options with commands |
| C-09 | PASS | Detection evidence column in schema |
| C-10 | PASS | "# Inertia Advocate: auto-added by corps-build" in YAML; C-24 group annotation |
| C-11 | PASS | Signal Schema before YAML |
| C-12 | PASS | HARD BOUNDARY first line |
| C-13 | PASS | C-12 STATUS: CONFIRMED self-referential |
| C-14 | PASS | GATE pre-check + Post-Write Verification bracket |
| C-15 | PASS | Pre-check names all required outputs |
| C-16 | PASS | Debt if skipped on all AMENDs |
| C-17 | PASS | SCHEDULED items name roles |
| C-18 | PASS | C-NN IDs primary keys |
| C-19 | PASS | Post-write self-labels criterion satisfaction |
| C-20 | PASS | "ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check" |
| C-21 | PASS | C-NN-labeled schema columns |
| C-22 | PASS | Signal Schema header declares criterion purpose |
| C-23 | PASS | 4 modes enumerated; selection cites schema row + table Signal Name |
| C-24 | PASS | C-24 group-level governance comment |
| C-25 | PASS | Universal labeling rule enforced across all sections |
| C-26 | PASS | Multi-criterion headers at scan and finalize positions |
| C-27 | PASS | Tri-part triad for all 4 modes |
| C-28 | PASS | Three execution states on items |
| C-29 | PASS | Compound bundles on pre-check items |
| C-30 | PASS | 10 criteria cited in post-write: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37 |
| C-31 | PASS | Phase-purpose naming throughout |
| C-32 | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED |
| C-33 | PASS | Signal Schema header (pre) + Post-Write header (post) |
| C-34 | PASS | Essential C-02 in post-write alongside 9 aspirationals |
| C-35 | PASS | C-05 ACKNOWLEDGED with golden-disqualification consequence |
| C-36 | PASS | DARK SIGNALS Evidence Table with typed columns; "Pivot Modes Affected" column makes per-entry mode impact explicit; 4 typed rows |
| C-37 | PASS | Evidence Against cites table Signal Name values: "DARK SIGNALS table: NO-WORKSPACE-GROUPING Found?=[N/P]"; AMEND-A: "DARK SIGNALS table basis: [Signal Name] Found?=N — [mode] eliminated by table" |

**V-03 Score: 235/235** | All essential: PASS

---

## V-04 — Inertia Framing: Repo Grain Vocabulary

**Structure**: 4 roles; DARK SIGNALS renamed REPO GRAIN; entries labeled GRAIN-NO-*; with-grain/against-grain amend classification

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | YAML block complete |
| C-02 | PASS | Signal Schema column tracing enforced |
| C-03 | PASS | groups: section |
| C-04 | PASS | Named roles; Inertia Advocate excluded |
| C-05 | PASS | HARD BOUNDARY front-loaded; ACKNOWLEDGED with golden-disqualification |
| C-06 | PASS | ROLE 3 selects mode with grain-classification + schema row citation |
| C-07 | PASS | exec-office present |
| C-08 | PASS | Three AMEND options with commands; AMEND-A carries with-grain/against-grain framing |
| C-09 | PASS | Detection evidence column |
| C-10 | PASS | Inertia Advocate noted at team level; C-24 group annotation |
| C-11 | PASS | Signal Schema pre-YAML |
| C-12 | PASS | HARD BOUNDARY first line |
| C-13 | PASS | C-12 STATUS: CONFIRMED |
| C-14 | PASS | GATE pre-check + ROLE 4 post-write bracket |
| C-15 | PASS | Pre-check names all required outputs |
| C-16 | PASS | Debt if skipped on all three AMENDs; AMEND-A specifically names Inertia Advocate opposition consequence |
| C-17 | PASS | SCHEDULED items forward-committed to roles |
| C-18 | PASS | C-NN IDs primary keys |
| C-19 | PASS | Post-write self-labels criteria at point of satisfaction |
| C-20 | PASS | ROLE 2+ blocked until ROLE 1 complete |
| C-21 | PASS | C-NN-labeled schema columns |
| C-22 | PASS | Signal Schema header declares criterion purpose |
| C-23 | PASS | 4 modes enumerated; "Grain classification: with-grain / against-grain" at selection |
| C-24 | PASS | "# Inertia Advocate governance (C-24): Every team receives one Inertia Advocate from corps-build" at each group |
| C-25 | PASS | Universal labeling enforced |
| C-26 | PASS | Multi-criterion headers at scan and post-write positions |
| C-27 | PASS | Tri-part triad for all 4 modes |
| C-28 | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED |
| C-29 | PASS | Compound bundles on pre-check items |
| C-30 | PASS | 10 criteria: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37 |
| C-31 | PASS | Phase-purpose naming |
| C-32 | PASS | Three execution states |
| C-33 | PASS | Signal Schema (pre-YAML) + Post-Write (post-YAML) brackets |
| C-34 | PASS | Essential C-02 in post-write |
| C-35 | PASS | C-05 ACKNOWLEDGED with golden-disqualification consequence |
| C-36 | PASS | REPO GRAIN section satisfies C-36 as equivalent named structure (rubric allows "DARK SIGNALS or equivalent"); GRAIN-NO-* entries each name topology dimension + mode impact per entry |
| C-37 | PASS | Evidence Against cites GRAIN-NO-* labels: "REPO GRAIN: GRAIN-NO-WORKSPACE-GROUPING — topology [absent/partial]: going against grain"; AMEND-A cites "REPO GRAIN basis: [GRAIN-NO-*] — current mode goes against grain" |

**V-04 Score: 235/235** | All essential: PASS

---

## V-05 — Combination: Hypothesis-First + DARK SIGNALS Table + Phase Footers

**Structure**: 5 phases (GATE, SCAN, DELIBERATE, DRAFT, FINALIZE); DARK SIGNALS table adds "Hypothesis Relation" column; PHASE OUTPUTS footer at each phase boundary

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | DRAFT PHASE YAML block complete |
| C-02 | PASS | Signal Schema "YAML name (C-02)" column; FINALIZE post-write checks match |
| C-03 | PASS | groups: section |
| C-04 | PASS | Named roles; Inertia Advocate excluded |
| C-05 | PASS | HARD BOUNDARY first; C-05 ACKNOWLEDGED with golden-disqualification |
| C-06 | PASS | DELIBERATE PHASE selects mode with hypothesis-closure rationale + schema row citation |
| C-07 | PASS | exec-office present |
| C-08 | PASS | Three AMEND options; AMEND-A cites "Hypothesis: [CONFIRMED / WEAKENED / OVERTURNED]" |
| C-09 | PASS | Detection evidence column |
| C-10 | PASS | "# Inertia Advocate: auto-added by corps-build"; C-24 group annotation |
| C-11 | PASS | Signal Schema in SCAN PHASE before YAML |
| C-12 | PASS | HARD BOUNDARY first line |
| C-13 | PASS | C-12 STATUS: CONFIRMED in gate pre-check |
| C-14 | PASS | GATE pre-check + FINALIZE post-write bracket the YAML |
| C-15 | PASS | Pre-check names C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-01+C-02+C-03+C-04, C-36+C-37, C-16+C-30 |
| C-16 | PASS | Debt if skipped on all AMENDs |
| C-17 | PASS | SCHEDULED items forward-committed to named phases |
| C-18 | PASS | C-NN IDs primary keys |
| C-19 | PASS | FINALIZE post-write cites criteria by ID at satisfaction point |
| C-20 | PASS | "Phases 2–5 are blocked until Phase 1 (GATE) outputs its pre-check and pivot hypothesis" |
| C-21 | PASS | C-NN-labeled schema columns |
| C-22 | PASS | Signal Schema header declares criterion purpose |
| C-23 | PASS | 4 modes enumerated; selection cites schema row + DARK SIGNALS table Signal Name + hypothesis outcome |
| C-24 | PASS | "# Inertia Advocate governance (C-24): Every team receives one Inertia Advocate from corps-build" at each group |
| C-25 | PASS | "Universal labeling rule (C-25): Every section in every phase carries a C-NN self-label" |
| C-26 | PASS | Multi-criterion headers at SCAN (pre-YAML) and FINALIZE (post-YAML) positions |
| C-27 | PASS | Tri-part triad for all 4 modes; opens with hypothesis closure |
| C-28 | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED on pre-check items |
| C-29 | PASS | Compound bundles: "C-11+C-21+C-22+C-25+C-26", "C-23+C-27", "C-36+C-37", "C-16+C-30" |
| C-30 | PASS | FINALIZE post-write cites 10 criteria: C-02, C-04, C-07, C-03, C-05, C-24, C-27, C-25, C-36, C-37 |
| C-31 | PASS | GATE / SCAN / DELIBERATE / DRAFT / FINALIZE — all purpose-named; 5-phase pipeline visible |
| C-32 | PASS | Three execution states present on actual items |
| C-33 | PASS | SCAN PHASE header (pre-YAML) + FINALIZE post-write (post-YAML) |
| C-34 | PASS | Essential C-02 in post-write alongside 9 aspirationals |
| C-35 | PASS | C-05 ACKNOWLEDGED with golden-disqualification consequence |
| C-36 | PASS | DARK SIGNALS Evidence Table with 6 columns including "Hypothesis Relation" (REFUTES/CORROBORATES ALT/NEUTRAL); per-row mode impact in "Pivot Modes Affected" column; Hypothesis outcome summary row |
| C-37 | PASS | Evidence Against cites table Signal Names: "DARK SIGNALS table: NO-WORKSPACE-GROUPING Found?=[N/P]"; AMEND-A: "DARK SIGNALS table basis: [Signal Name] Found?=N — [mode] eliminated. If hypothesis was OVERTURNED: [Signal Name] caused revision" |

**V-05 Score: 235/235** | All essential: PASS

---

## Composite Scorecard

| Variation | E (60) | R (30) | A (145) | Total | All Essential |
|-----------|--------|--------|---------|-------|---------------|
| V-01 | 60 | 30 | 145 | **235** | YES |
| V-02 | 60 | 30 | 145 | **235** | YES |
| V-03 | 60 | 30 | 145 | **235** | YES |
| V-04 | 60 | 30 | 145 | **235** | YES |
| V-05 | 60 | 30 | 145 | **235** | YES |

All five variations score the rubric ceiling. All achieve golden status.

---

## Ranking

All tied at 235/235. Ranked by structural novelty and ceiling-candidate potential:

1. **V-05** — Maximum traceability stack: three mechanisms combine without redundancy (hypothesis-first + table format + phase footers); Hypothesis Relation as typed column is the only variant where hypothesis tracking is machine-readable from a single column scan. 5-phase pipeline separates DRAFT from FINALIZE as distinct artifacts.
2. **V-01** — Epistemically strongest structural change: hypothesis commitment before scanning changes the logical flow of the entire output; DARK SIGNALS entries as hypothesis-refutation evidence is a new framing that tightens C-37 beyond label citation.
3. **V-04** — Domain-vocabulary alignment: REPO GRAIN reframes negative evidence as topology facts rather than absences, with-grain/against-grain amend classification adds a decision-support layer absent from all prior rounds.
4. **V-03** — Reliability improvement: table columns constrain model behavior more tightly than block-list format; column-indexed citation anchor for C-37 is more precise than label-in-prose.
5. **V-02** — Phrasing shift is orthogonal to criterion structure; lowest structural novelty of R10, though highest readability for non-technical reviewers.

---

## Excellence Signals

**From V-05 (ceiling candidate):**

1. **Hypothesis Relation as typed column** — Elevating the hypothesis-tracking field from inline prose (V-01 block-list style: "Hypothesis relation: REFUTES") to a first-class table column makes hypothesis closure scannable without parsing prose. A scorer can verify the entire hypothesis lifecycle by reading one column. This is a tighter structural commitment than the prose field.

2. **PHASE OUTPUTS footer as inter-phase handoff declaration** — Each phase ends with a formal block naming exactly what was produced and what is available to the next phase as citation targets. This makes the dependency chain between phases explicit at each boundary. The DELIBERATE PHASE footer names "schema rows + table Signal Names available as citation targets" — this anticipates C-37 by surfacing the citation vocabulary at handoff time, not only in the deliberation itself.

3. **Hypothesis-first commitment before scanning** — Declaring the pivot mode hypothesis in GATE and naming the "key refutation signal" (the DARK SIGNALS entry that would most challenge the hypothesis) commits the model to a falsification target before evidence collection begins. DARK SIGNALS entries are then classified by their relation to that commitment. This changes the deliberation from "here is what I found and didn't find, now I'll decide" to "I predicted X, here is what confirmed/overturned it, and the specific label that caused any revision."

**From V-04 (new vocabulary axis):**

4. **With-grain/against-grain amend framing** — Classifying each AMEND option's pivot mode relative to the repo's existing topology adds a cost dimension absent from prior rounds. "Against-grain" amends incur Inertia Advocate opposition as a named consequence. This is the first round where the Inertia Advocate vocabulary propagates from the YAML itself into the amend reasoning section.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": ["hypothesis-first pivot commitment in GATE with named key-refutation-signal before scanning begins", "hypothesis-relation typed column in DARK SIGNALS evidence table enabling column-scan hypothesis closure", "PHASE OUTPUTS footer as inter-phase handoff declaration naming citation targets available to next phase", "with-grain vs against-grain amend classification using REPO GRAIN vocabulary from Inertia Advocate pipeline"]}
```
