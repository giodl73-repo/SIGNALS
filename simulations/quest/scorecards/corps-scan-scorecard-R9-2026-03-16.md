## Round 9 — corps-scan Scorecard (v8 Rubric, 225 pts)

---

### Scoring Methodology

All five variations are scored against the 35-criterion v8 rubric. R8's V-01 and V-02 established the 225/225 ceiling; R9 treats all prior invariants (C-12 through C-35) as structural requirements. Each variation's new axis is evaluated for passing the existing rubric and potentially introducing a new extractable criterion.

---

## V-01 — Lifecycle Emphasis: DARK SIGNALS (Negative Space Inventory)

### Essential (60 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | **PASS** | YAML block present in ROLE 4 with `org:`, `exec-office:`, `groups:`, `teams:`, `roles:` |
| C-02 | **PASS** | Signal Schema "YAML name (C-02)" column; pre-YAML traceability statement: "All team YAML names must trace to ROLE 2 Signal Schema 'YAML name (C-02)' column" |
| C-03 | **PASS** | `groups:` section with group containers present |
| C-04 | **PASS** | "Proposed roles (C-04)" column in schema; `roles:` with named roles per team in YAML |
| C-05 | **PASS** | `STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit possible` with named consequence |

Essential: **60/60**

### Recommended (30 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | **PASS** | ROLE 3 selects pivot mode citing specific ROLE 2 schema row by "Repo signal" value; rationale present |
| C-07 | **PASS** | `exec-office:` with `name:` field in YAML |
| C-08 | **PASS** | AMEND-A / AMEND-B / AMEND-C with commands (`/corps-scan --pivot`, `--exec-office`, `--groups`) |

Recommended: **30/30**

### Aspirational (135 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | **PASS** | "Detection evidence (C-09)" column in schema; `# schema-signal: [ROLE 2 "Repo signal" value — satisfies C-09]` per team in YAML |
| C-10 | **PASS** | `# Inertia Advocate: auto-added by corps-build` on every team |
| C-11 | **PASS** | Signal Schema precedes YAML as distinct pre-YAML inventory |
| C-12 | **PASS** | "HARD BOUNDARY (C-12 satisfier)" as first substantive line before any scanning or YAML |
| C-13 | **PASS** | "C-12 draft-only statement precedes all output in this response — confirmed above. STATUS: CONFIRMED." |
| C-14 | **PASS** | GATE pre-check (pre-YAML) + Post-Write Verification in ROLE 4 (post-YAML) — both present |
| C-15 | **PASS** | Pre-check names C-05, C-01+C-02+C-03+C-04, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-16+C-30 as skill requirements |
| C-16 | **PASS** | All three amend options carry "Debt if skipped:" entries naming downstream consequences |
| C-17 | **PASS** | All SCHEDULED items are forward commitments to named future roles |
| C-18 | **PASS** | "C-NN IDs are primary keys throughout"; all pre-check items use C-NN as primary header |
| C-19 | **PASS** | Post-Write cites "C-14:", "C-33:", "C-30:", "C-34:" at point of satisfaction |
| C-20 | **PASS** | "ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs its pre-check"; ROLE 1 = COMPLIANCE OFFICER gates all scanning |
| C-21 | **PASS** | Signal Schema columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)" — all C-NN-labeled |
| C-22 | **PASS** | Signal Schema header: `(C-26: C-11 + C-21 satisfier — SCAN PHASE / precedes YAML; C-22: self-labeled)` |
| C-23 | **PASS** | ROLE 3 enumerates all 4 pivot modes before selecting; selection cites ROLE 2 schema row + DARK SIGNALS entry |
| C-24 | **PASS** | `# Inertia Advocate governance (C-24): Every team in this group receives one Inertia Advocate from corps-build. Group-level governance: Advocates share status-quo context across this group.` on each group element |
| C-25 | **PASS** | Universal labeling rule enforced; "No section in this response may be unlabeled"; confirmed across all roles |
| C-26 | **PASS** | Signal Schema header cites C-11+C-21 (multi-criterion); Post-Write header cites C-14+C-30 (multi-criterion) |
| C-27 | **PASS** | All 4 modes: Evidence For / Evidence Against (citing DARK SIGNALS by label) / Assessment tri-part structure |
| C-28 | **PASS** | CONFIRMED / SCHEDULED / ACKNOWLEDGED markers on every pre-check item |
| C-29 | **PASS** | "C-01+C-02+C-03+C-04", "C-11+C-21+C-22+C-25+C-26", "C-23+C-27", "C-16+C-30" — compound bundles on single items |
| C-30 | **PASS** | "C-30: this block cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria" |
| C-31 | **PASS** | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE — purpose-named pipeline |
| C-32 | **PASS** | CONFIRMED / SCHEDULED / ACKNOWLEDGED — all three states present on actual pre-check items |
| C-33 | **PASS** | SCAN PHASE header (C-11+C-21) = pre-YAML bracket; Post-Write header (C-14+C-30) = post-YAML bracket — symmetric |
| C-34 | **PASS** | C-02 (essential) cited in 9-criterion post-write alongside 8 aspirationals |
| C-35 | **PASS** | "C-05 STATUS: ACKNOWLEDGED — essential failure if violated; named consequence" |

Aspirational: **135/135**

**V-01 Total: 225/225 | All essential: PASS | Golden: YES**

**Excellence signal — new pattern**: DARK SIGNALS section produced after Signal Schema, documenting absent signals by type (no-service-manifest, no-DDD-language, no-domain-boundary, no-workspace-grouping), each entry naming which pivot mode the absence rules out or weakens. ROLE 3 Evidence Against entries cite DARK SIGNALS entries by label rather than generic "absent" statements. This makes pivot deliberation bidirectionally falsifiable: schema rows are the positive evidence; DARK SIGNALS are the structured negative evidence. Amend options also reference DARK SIGNALS citations as basis for alternative pivot modes.

---

## V-02 — Lifecycle Emphasis: Phase Output Contracts at Phase Footers

### Essential (60 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | **PASS** | YAML block in DRAFT PHASE |
| C-02 | **PASS** | SCAN schema "YAML name (C-02)" column; DRAFT PHASE: "All team names trace to SCAN schema 'YAML name (C-02)' column" |
| C-03 | **PASS** | `groups:` structure present |
| C-04 | **PASS** | Named roles from SCAN "Proposed roles (C-04)" |
| C-05 | **PASS** | `STATUS: ACKNOWLEDGED — essential failure if violated; violation consequence: not golden` |

Essential: **60/60**

### Recommended (30 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | **PASS** | DELIBERATE PHASE selects mode with rationale citing SCAN schema row |
| C-07 | **PASS** | `exec-office:` with name in YAML |
| C-08 | **PASS** | AMEND-A/B/C with commands and debt framing in FINALIZE PHASE |

Recommended: **30/30**

### Aspirational (135 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | **PASS** | Detection evidence column in schema; `# schema-signal` per team in YAML |
| C-10 | **PASS** | `# Inertia Advocate: auto-added by corps-build` per team |
| C-11 | **PASS** | Signal Schema before YAML in SCAN PHASE |
| C-12 | **PASS** | "HARD BOUNDARY (C-12 satisfier)" front-loaded before phase structure |
| C-13 | **PASS** | "C-12 located above this pre-check. STATUS: CONFIRMED." |
| C-14 | **PASS** | GATE pre-check (pre-YAML) + FINALIZE POST-WRITE VERIFICATION (post-YAML) — both present |
| C-15 | **PASS** | Pre-check names C-12, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-01+C-02+C-03+C-04, C-16+C-30 as requirements |
| C-16 | **PASS** | "Debt if skipped:" on all 3 amend options; DRAFT PHASE OUTPUTS and PHASE OUTPUTS footers cited as evidence basis |
| C-17 | **PASS** | SCHEDULED items are forward commitments to named future phases |
| C-18 | **PASS** | C-NN IDs as primary keys throughout pre-check |
| C-19 | **PASS** | FINALIZE POST-WRITE cites "C-14:", "C-33:", "C-30:", "C-34:" at satisfaction point |
| C-20 | **PASS** | "Phases 2–5 are blocked until Phase 1 (GATE) outputs its pre-check" |
| C-21 | **PASS** | Signal Schema: "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)" columns |
| C-22 | **PASS** | Signal Schema header announces C-11+C-21 criterion purpose before rows |
| C-23 | **PASS** | DELIBERATE PHASE enumerates all 4 modes with tri-part assessment before selecting |
| C-24 | **PASS** | Inertia Advocate governance comment at group level in YAML |
| C-25 | **PASS** | "Universal labeling rule (C-25): Every section in every phase carries a C-NN self-label. No unlabeled sections." |
| C-26 | **PASS** | SCAN PHASE header cites C-11+C-21; FINALIZE PHASE header cites C-14+C-30 |
| C-27 | **PASS** | Four-mode deliberation with Evidence For / Evidence Against / Assessment |
| C-28 | **PASS** | CONFIRMED / ACKNOWLEDGED / SCHEDULED on every pre-check item |
| C-29 | **PASS** | Compound bundles present |
| C-30 | **PASS** | "C-30: cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9 criteria" |
| C-31 | **PASS** | GATE / SCAN / DELIBERATE / DRAFT / FINALIZE PHASE — five purpose-named pipeline phases |
| C-32 | **PASS** | CONFIRMED / ACKNOWLEDGED / SCHEDULED — three-state vocabulary on pre-check items |
| C-33 | **PASS** | SCAN header (C-11+C-21) = pre-YAML bracket; FINALIZE header (C-14+C-30) = post-YAML bracket |
| C-34 | **PASS** | "C-34: essential C-02 present alongside 8 aspirational criteria" |
| C-35 | **PASS** | C-05 ACKNOWLEDGED with named consequence in GATE |

Aspirational: **135/135**

**V-02 Total: 225/225 | All essential: PASS | Golden: YES**

**Excellence signal — new pattern**: PHASE OUTPUTS footer block at the end of every phase declaring exactly what the phase produced — row counts, selected mode, exec-office name, team counts, role counts, handoff content. GATE declares: 2 CONFIRMED, 4 SCHEDULED, 1 ACKNOWLEDGED. SCAN declares: schema row count, candidate modes, exec inference value, pre-YAML bracket confirmation. DELIBERATE declares: 4 modes assessed, selected mode, row citation. DRAFT declares: YAML blocks produced, groups, teams, named roles minimum, Inertia Advocate annotations, C-05 honored. FINALIZE declares: verification count, 3 amend options produced, C-33/C-34/C-35 status, draft-only confirmed. Footer declarations confirm production at point of delivery, distinct from R8 V-03's header-level I/O contracts which pre-committed before execution.

---

## V-03 — Output Format: Downstream Consumer Annotations on YAML Elements

### Essential (60 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | **PASS** | YAML block with full org structure present in ROLE 4 |
| C-02 | **PASS** | Signal Schema "YAML name (C-02)" column; all teams trace to schema |
| C-03 | **PASS** | `groups:` section with containers |
| C-04 | **PASS** | Named roles per team from "Proposed roles (C-04)" column |
| C-05 | **PASS** | `STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit. Violation consequence: output fails golden threshold regardless of composite score.` |

Essential: **60/60**

### Recommended (30 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | **PASS** | ROLE 3 selects pivot mode with rationale citing specific ROLE 2 schema row |
| C-07 | **PASS** | `exec-office:` with name field present |
| C-08 | **PASS** | AMEND-A/B/C with commands; consumer impact named in each amend debt statement |

Recommended: **30/30**

### Aspirational (135 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | **PASS** | Detection evidence column + `# schema-signal:` per team |
| C-10 | **PASS** | `# Inertia Advocate: auto-added by corps-build — not listed here` per team |
| C-11 | **PASS** | Signal Schema before YAML |
| C-12 | **PASS** | "HARD BOUNDARY (C-12 satisfier)" front-loaded |
| C-13 | **PASS** | "C-12 confirmed above this pre-check. STATUS: CONFIRMED." |
| C-14 | **PASS** | GATE pre-check + Post-Write Verification — both present |
| C-15 | **PASS** | Pre-check names all criterion bundles as skill requirements |
| C-16 | **PASS** | "Debt if skipped:" with consumer impact on all 3 amend options |
| C-17 | **PASS** | All SCHEDULED items forward-committed to named future roles |
| C-18 | **PASS** | C-NN IDs as primary keys in pre-check — confirmed by "C-15, C-17, C-18, C-28, C-29, C-32, C-35 all satisfied per standard gate pattern" |
| C-19 | **PASS** | Post-Write cites "C-14:", "C-33:", "C-30:", "C-34:" at satisfaction point |
| C-20 | **PASS** | ROLE 2–4 blocked until ROLE 1 pre-check complete |
| C-21 | **PASS** | C-NN-labeled columns in Signal Schema |
| C-22 | **PASS** | Signal Schema header announces criterion purpose (C-26: C-11+C-21 satisfier) |
| C-23 | **PASS** | ROLE 3 deliberates all 4 modes with Evidence For/Against/Assessment |
| C-24 | **PASS** | Inertia Advocate governance annotation at group level; `# consumed-by: corps-committee` also on each group |
| C-25 | **PASS** | Universal labeling rule enforced |
| C-26 | **PASS** | Signal Schema header (C-11+C-21 multi-criterion); Post-Write header (C-14+C-30 multi-criterion) |
| C-27 | **PASS** | Tri-part Evidence For / Evidence Against / Assessment on all 4 modes |
| C-28 | **PASS** | CONFIRMED / SCHEDULED / ACKNOWLEDGED on every pre-check item |
| C-29 | **PASS** | Compound bundles in pre-check |
| C-30 | **PASS** | Post-write cites 9 criteria: C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 |
| C-31 | **PASS** | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE — purpose-named phases |
| C-32 | **PASS** | Three-state vocabulary present on pre-check items |
| C-33 | **PASS** | SCAN header (C-11+C-21) = pre-YAML bracket; Post-Write header (C-14+C-30) = post-YAML bracket |
| C-34 | **PASS** | Essential C-02 present in 9-criterion post-write inventory |
| C-35 | **PASS** | C-05 ACKNOWLEDGED with violation consequence named |

Aspirational: **135/135**

**V-03 Total: 225/225 | All essential: PASS | Golden: YES**

**Excellence signal — new pattern**: Consumer annotation rule declared as a first-class ROLE 4 instruction. Consumer map defined before YAML production: `exec-office` → consumed-by: corps-rob; `groups[].name` → consumed-by: corps-committee; `groups[].teams[]` → consumed-by: corps-build + corps-pr; `teams[].roles[]` → consumed-by: corps-build. Every YAML structural element carries a `# consumed-by:` comment naming the downstream corps-* skill(s) that read it. Amend options reference consumer impact directly (e.g., "Consumer: corps-rob reads this value directly"). Post-write verification checklist includes "Downstream consumer annotations on all YAML structural elements" and "Consumer map covers exec-office, groups, teams, roles" as explicit items.

---

## V-04 — Output Format: Criterion Cluster Naming as Primary Pre-Check Key

### Essential (60 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | **PASS** | YAML block in DRAFT PHASE with full org structure |
| C-02 | **PASS** | STRUCTURE CLUSTER explicitly targets C-01+C-02+C-03+C-04; schema-traced teams |
| C-03 | **PASS** | `groups:` section present |
| C-04 | **PASS** | Named roles from SCAN "Proposed roles (C-04)" |
| C-05 | **PASS** | In BOUNDARY CLUSTER: "STATUS: ACKNOWLEDGED — essential failure if violated; violation consequence named. Boundary constraint: no partial credit" |

Essential: **60/60**

### Recommended (30 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | **PASS** | DELIBERATE PHASE selects pivot with schema row citation |
| C-07 | **PASS** | `exec-office:` with name in YAML |
| C-08 | **PASS** | AMEND-A/B/C with commands; CLUSTER names used in amend framing |

Recommended: **30/30**

### Aspirational (135 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | **PASS** | Detection evidence column + `# schema-signal:` per team |
| C-10 | **PASS** | `# Inertia Advocate: auto-added by corps-build` per team |
| C-11 | **PASS** | Signal Schema (INVENTORY CLUSTER production) before YAML |
| C-12 | **PASS** | "HARD BOUNDARY (C-12 satisfier)" front-loaded as first substantive line |
| C-13 | **PASS** | "STATUS: CONFIRMED — C-12 confirmed above this pre-check" in BOUNDARY CLUSTER |
| C-14 | **PASS** | GATE pre-check + FINALIZE PHASE POST-WRITE VERIFICATION — both present |
| C-15 | **PASS** | Pre-check names BOUNDARY, INVENTORY, DELIBERATION, STRUCTURE, FINALIZE clusters as skill requirements by both cluster name and C-NN contents |
| C-16 | **PASS** | "Debt if skipped:" with CLUSTER cross-references for all 3 amend options |
| C-17 | **PASS** | All SCHEDULED clusters are forward commitments to named future phases |
| C-18 | **PARTIAL** | Pre-check header annotation: "(C-18: C-NN IDs as keys within clusters; cluster names are primary keys — C-NN bundles are cluster contents)". BOUNDARY CLUSTER unpacks to 3 C-NN-primary items (C-12, C-13, C-05); INVENTORY/DELIBERATION/STRUCTURE/FINALIZE use cluster names as primary keys with C-NN bundles as secondary contents. C-NN IDs identifiable but not primary key for 4 of 5 cluster items. Falls short of "5 items with C-NN as primary key" — BOUNDARY only provides 3. |
| C-19 | **PASS** | FINALIZE PHASE post-write cites "C-14:", "C-33:", "C-30:", "C-34:" at satisfaction |
| C-20 | **PASS** | "Phases 2–5 are blocked until Phase 1 (GATE) outputs its pre-check" |
| C-21 | **PASS** | Signal Schema columns labeled with C-NN IDs |
| C-22 | **PASS** | Signal Schema header: `(C-26: C-11+C-21 satisfier / INVENTORY CLUSTER / precedes YAML; C-22: self-labeled; C-33: pre-YAML bracket)` |
| C-23 | **PASS** | DELIBERATE PHASE (DELIBERATION CLUSTER) enumerates all 4 modes with tri-part assessment |
| C-24 | **PASS** | Inertia Advocate governance at group level in YAML |
| C-25 | **PASS** | Universal labeling rule enforced |
| C-26 | **PASS** | Signal Schema header (C-11+C-21); FINALIZE header (C-14+C-30) — multi-criterion headers |
| C-27 | **PASS** | Tri-part triad for all 4 modes in DELIBERATE PHASE |
| C-28 | **PASS** | CONFIRMED / SCHEDULED / ACKNOWLEDGED on every pre-check item |
| C-29 | **PASS** | Compound bundles in every cluster definition |
| C-30 | **PASS** | "FINALIZE CLUSTER cites C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 — 9" |
| C-31 | **PASS** | GATE / SCAN / DELIBERATE / DRAFT / FINALIZE PHASE — five purpose-named phases |
| C-32 | **PASS** | Three-state vocabulary: CONFIRMED / SCHEDULED / ACKNOWLEDGED on items |
| C-33 | **PASS** | SCAN (INVENTORY CLUSTER, C-11+C-21) = pre-YAML bracket; FINALIZE (C-14+C-30) = post-YAML bracket |
| C-34 | **PASS** | Essential C-02 in FINALIZE CLUSTER 9-criterion post-write |
| C-35 | **PASS** | C-05 in BOUNDARY CLUSTER: ACKNOWLEDGED with violation consequence named |

Aspirational: **132.5/135** (C-18 PARTIAL = 2.5 pts; all others PASS)

**V-04 Total: 222.5/225 | All essential: PASS | Golden: YES**

**Excellence signal — new pattern**: Semantic cluster vocabulary declared as a first-class pre-check structure. Five named clusters — BOUNDARY CLUSTER (C-05+C-12+C-13), INVENTORY CLUSTER (C-11+C-21+C-22+C-25+C-26), DELIBERATION CLUSTER (C-23+C-27), STRUCTURE CLUSTER (C-01+C-02+C-03+C-04), FINALIZE CLUSTER (C-14+C-16+C-19+C-30+C-33+C-34) — replace raw C-NN bundles as primary pre-check keys. Each cluster name encodes the purpose of its criterion group; the C-NN bundle is retained as cluster contents. Amend options cross-reference cluster names (e.g., "DELIBERATION CLUSTER amendment", "STRUCTURE CLUSTER amendment"), creating a consistent vocabulary across the entire output. The tradeoff: cluster names as primary keys cause C-18 PARTIAL since individual C-NN IDs are no longer the primary header for most items.

---

## V-05 — Combination: DARK SIGNALS + Downstream Consumer Annotations

### Essential (60 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | **PASS** | YAML block with full org structure in ROLE 4 |
| C-02 | **PASS** | Signal Schema "YAML name (C-02)" column; all teams traced |
| C-03 | **PASS** | `groups:` section with containers |
| C-04 | **PASS** | Named roles from "Proposed roles (C-04)" |
| C-05 | **PASS** | "STATUS: ACKNOWLEDGED — essential failure if violated; no partial credit. Violation consequence: output fails golden threshold regardless of composite score." |

Essential: **60/60**

### Recommended (30 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | **PASS** | ROLE 3 selects pivot mode citing specific SCAN schema row AND relevant DARK SIGNALS entry |
| C-07 | **PASS** | `exec-office:` present with `# consumed-by: corps-rob` annotation |
| C-08 | **PASS** | AMEND-A/B/C with commands; debt references both DARK SIGNALS citations and consumer annotations |

Recommended: **30/30**

### Aspirational (135 pts max)

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | **PASS** | Detection evidence column + `# schema-signal:` per team |
| C-10 | **PASS** | `# Inertia Advocate: auto-added by corps-build — status-quo competitor per team` |
| C-11 | **PASS** | Signal Schema precedes YAML |
| C-12 | **PASS** | "HARD BOUNDARY (C-12 satisfier)" front-loaded |
| C-13 | **PASS** | "STATUS: CONFIRMED — C-12 confirmed above" in pre-check |
| C-14 | **PASS** | GATE pre-check + Post-Write Verification — both present |
| C-15 | **PASS** | "C-15 satisfied: pre-check names negative-space (DARK SIGNALS), consumer annotations, and standard C-NN requirements as skill requirements" |
| C-16 | **PASS** | "Debt if skipped:" referencing DARK SIGNALS consumer impact and consumer annotation evidence on all 3 amends |
| C-17 | **PASS** | SCHEDULED items forward commitments. "C-17, C-18, C-28, C-29, C-32, C-35 satisfied per standard gate pattern." |
| C-18 | **PASS** | C-NN IDs as primary keys throughout pre-check |
| C-19 | **PASS** | Post-Write cites "C-14:", "C-33:", "C-30:", "C-34:" at satisfaction point |
| C-20 | **PASS** | ROLE 2–4 blocked until ROLE 1 complete |
| C-21 | **PASS** | C-NN-labeled columns in Signal Schema |
| C-22 | **PASS** | Signal Schema header announces C-11+C-21 criterion purpose |
| C-23 | **PASS** | ROLE 3 enumerates all 4 modes before selecting; rationale cites schema row AND DARK SIGNALS entry |
| C-24 | **PASS** | Inertia Advocate governance at group level in YAML |
| C-25 | **PASS** | Universal labeling rule enforced throughout |
| C-26 | **PASS** | Signal Schema header (C-11+C-21 multi-criterion); Post-Write header (C-14+C-30 multi-criterion) |
| C-27 | **PASS** | Tri-part triad for all 4 modes; Evidence Against cites DARK SIGNALS entries |
| C-28 | **PASS** | CONFIRMED / SCHEDULED / ACKNOWLEDGED on every pre-check item |
| C-29 | **PASS** | Compound bundles in pre-check items |
| C-30 | **PASS** | Post-write cites 9 criteria: C-14, C-02, C-24, C-27, C-25, C-26, C-29, C-32, C-33 |
| C-31 | **PASS** | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE — purpose-named |
| C-32 | **PASS** | Three-state vocabulary on pre-check items |
| C-33 | **PASS** | SCAN header (C-11+C-21) = pre-YAML bracket; Post-Write header (C-14+C-30) = post-YAML bracket |
| C-34 | **PASS** | Essential C-02 in 9-criterion post-write alongside 8 aspirationals |
| C-35 | **PASS** | C-05 ACKNOWLEDGED with named violation consequence |

Aspirational: **135/135**

**V-05 Total: 225/225 | All essential: PASS | Golden: YES**

**Excellence signal — interaction pattern**: DARK SIGNALS section extended with `Consumer impact:` annotation per absent signal type. Each DARK SIGNALS entry names not just which pivot mode the absence rules out, but which downstream corps-* skill cannot use the corresponding capability (e.g., "absent service-manifest → corps-build cannot use service-based role file clustering; corps-committee service-boundary appointments not available"). YAML also carries `# consumed-by:` annotations (V-03 pattern), plus a YAML-level `# dark-signals-summary:` header comment and per-element `# dark-signals:` comments on exec-office. Pre-YAML traceability statement references both: "DARK SIGNALS documented alternatives: [ruled-out modes]. Consumer annotations applied." Rationale at pivot selection cites both schema row (positive evidence) and DARK SIGNALS entry (eliminating evidence). The combination creates a complete evidence chain: detected (schema) → ruled out (dark signals with consumer impact) → produced (YAML with consumer labels).

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | All Essential | Golden |
|-----------|-----------|-------------|--------------|-----------|---------------|--------|
| V-01 | 60/60 | 30/30 | 135/135 | **225/225** | YES | YES |
| V-02 | 60/60 | 30/30 | 135/135 | **225/225** | YES | YES |
| V-03 | 60/60 | 30/30 | 135/135 | **225/225** | YES | YES |
| V-04 | 60/60 | 30/30 | 132.5/135 | **222.5/225** | YES | YES |
| V-05 | 60/60 | 30/30 | 135/135 | **225/225** | YES | YES |

---

## Ranking

1. **V-01, V-02, V-03, V-05** — tied at 225/225
2. **V-04** — 222.5/225 (C-18 PARTIAL: cluster names as primary keys displace C-NN as primary key for 4 of 5 cluster-level items)

Among the four tied variations, V-05 is the highest-quality excellence signal because it demonstrates the interaction between two single-axis patterns — DARK SIGNALS and consumer annotations — producing an emergent third pattern not present in either V-01 or V-03 alone: per-absent-signal consumer impact annotations that cross the boundary between negative-space documentation and downstream pipeline documentation.

---

## Excellence Signals from Top-Scoring Variations

**From V-01 (new pattern C-36 candidate):**
- **DARK SIGNALS as structured negative-space inventory**: typed absent-signal entries by category, each mapping the absence to specific ruled-out pivot mode(s). Makes pivot deliberation bidirectionally falsifiable. ROLE 3 Evidence Against cites DARK SIGNALS by label — grounding the "against" case in documented, auditable absence rather than generic counter-evidence.

**From V-02 (new pattern C-37 candidate):**
- **PHASE OUTPUTS footer blocks**: formal declaration at each phase's conclusion of exactly what the phase produced — schema row counts, selected mode value, exec-office name string, team count, role count minimum, Inertia Advocate annotation status, C-05 honored status. Complementary to R8's header I/O contracts; footers confirm production at delivery vs. headers committing to it before execution. A scorer can verify every handoff without re-reading phase bodies.

**From V-03 (new pattern C-38 candidate):**
- **Consumer annotation rule with full consumer map**: `# consumed-by: corps-{skill}` on every YAML structural element; consumer map declared before YAML production. Amend option debt framing enriched with consumer impact (e.g., "Consumer: corps-rob reads this value directly"). Post-write verification item confirms consumer map coverage.

**From V-04 (new pattern C-39 candidate):**
- **Semantic cluster vocabulary**: BOUNDARY / INVENTORY / DELIBERATION / STRUCTURE / FINALIZE CLUSTER as purpose-named criterion groups. Each cluster name encodes the criterion group's pipeline role; C-NN bundles retained as cluster contents. Cluster vocabulary propagates into amend option framing and phase completion declarations (e.g., "INVENTORY CLUSTER satisfied", "STRUCTURE CLUSTER production"). Cost: C-18 PARTIAL because semantic cluster names become the primary pre-check keys.

**From V-05 (interaction, new pattern candidate):**
- **DARK SIGNALS consumer impact per absent-signal type**: each absent-signal entry names both the ruled-out pivot mode AND the downstream corps-* skill that loses a capability if the signal is absent. Creates a three-layer artifact: Signal Schema (positive evidence) + DARK SIGNALS (negative evidence with consumer constraints) + YAML consumer annotations (positive declarations). Pivot rationale at ROLE 3 selection cites both schema row and DARK SIGNALS entry simultaneously.

---

## R9 Assessment

R9 is not a convergence round. All five variations satisfy all 35 rubric criteria at or near the ceiling (four at 225/225, one at 222.5/225 due to the C-18 tradeoff of the cluster-naming design). The four new patterns introduced are additive: none interferes with existing invariants. Each addresses a different dimension:

- **DARK SIGNALS** (V-01, V-05): evidence quality dimension — negative space
- **PHASE OUTPUTS** (V-02): pipeline transparency dimension — production confirmation
- **Consumer annotations** (V-03, V-05): pipeline contract dimension — downstream dependency
- **Semantic clusters** (V-04): architecture readability dimension — criterion group semantics

The V-04 C-18 tradeoff is structurally interesting: semantic cluster names improve human readability and architectural clarity at the cost of C-18 exactness. This is the first round where a deliberate design choice in a new pattern caused a PARTIAL on an existing criterion. A C-39 criterion for semantic cluster vocabulary would need to be defined as compatible with C-18, not a replacement of it — or C-18 would need an updated pass condition acknowledging the compound-key form.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["DARK SIGNALS negative-space inventory: after Signal Schema, absent-signal types listed by category with ruled-out pivot modes named per entry; ROLE 3 Evidence Against cites DARK SIGNALS entries by label making pivot deliberation bidirectionally falsifiable", "PHASE OUTPUTS footer blocks: each phase ends with a formal declaration of exactly what it produced (row counts, selected values, handoff content) confirming production at delivery rather than pre-committing at header", "Downstream consumer annotations on YAML structural elements: consumer map declared pre-YAML mapping exec-office to corps-rob, groups to corps-committee, teams/roles to corps-build/corps-pr; every YAML element carries consumed-by comment", "Semantic criterion cluster vocabulary as primary pre-check keys: BOUNDARY/INVENTORY/DELIBERATION/STRUCTURE/FINALIZE CLUSTER names encode criterion group purpose with C-NN bundles as cluster contents; cluster vocabulary propagates into amend framing and phase completion declarations", "DARK SIGNALS consumer impact per absent-signal type: each absent-signal entry names both the ruled-out pivot mode and the downstream corps-* skill that loses a capability, combining negative-space documentation with consumer annotation axes"]}
```
