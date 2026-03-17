## Scorecard — corps-scan R6 (v6 rubric, 190 pts)

---

### V-01 — Role Sequence: Universal Labels + Tri-Part Pivot

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Draft org.yaml block present | **PASS** | ROLE 4 produces `org.yaml` block under `#### Draft org.yaml` |
| C-02 | Team areas derived from repo | **PASS** | All team names must match ROLE 2 schema "YAML name (C-02)" column exactly |
| C-03 | Group structure present | **PASS** | `groups:` with `teams:` nesting in YAML template |
| C-04 | Standard roles per team | **PASS** | 2× "Named role from ROLE 2 'Proposed roles (C-04)' column" per team |
| C-05 | Does not write .craft/roles/ | **PASS** | "HARD BOUNDARY (C-12 satisfier)" explicit; post-write confirms "No .craft/roles/ content" |
| C-06 | Pivot mode declared with rationale | **PASS** | ROLE 3 selects mode with "Rationale: one sentence citing specific ROLE 2 schema row" |
| C-07 | Exec office placeholder present | **PASS** | `exec-office:` section in YAML |
| C-08 | Amend options listed | **PASS** | AMEND-A/B/C with `/corps-scan --pivot`, `--exec-office`, `--groups` commands |
| C-09 | Detection rationale per area | **PASS** | `# schema-signal: [ROLE 2 "Repo signal" value — satisfies C-09]` per team; "Detection evidence (C-09)" column in schema |
| C-10 | Inertia Advocate noted | **PASS** | "Inertia Advocate: auto-added by corps-build — argues status-quo in team reviews" per team |
| C-11 | Pre-YAML scan inventory listed | **PASS** | ROLE 2 Signal Schema is a distinct table preceding ROLE 4 YAML |
| C-12 | Draft boundary front-loaded | **PASS** | "HARD BOUNDARY (C-12 satisfier)" before pre-check, before all structural content |
| C-13 | Self-referential compliance check | **PASS** | Pre-check item `C-13 -- self-referential confirmation: STATUS: CONFIRMED` confirms C-12 is present |
| C-14 | Dual-stage YAML bracketing | **PASS** | "C-14 dual-bracket: ROLE 1 pre-check is the pre-YAML gate; this block is the post-YAML gate. Both present." |
| C-15 | Rubric criteria embedded as skill requirements | **PASS** | Pre-check names C-12, C-13, C-05, C-11+C-21+C-22, C-23+C-27, C-04, C-07, C-16 as requirements (8 criteria > 3) |
| C-16 | Debt-framed amend options | **PASS** | All 3 AMEND options carry "Debt if skipped:" with corps-build/corps-rob/corps-committee consequences |
| C-17 | Forward commitment to future-section criteria | **PASS** | "C-17 satisfied: C-11+C-21+C-22, C-23+C-27, C-04, C-07, C-16 are forward commitments (SCHEDULED)" |
| C-18 | Criterion ID as primary compliance key | **PASS** | "C-18 satisfied: C-NN IDs are primary keys for all 9 pre-check items" |
| C-19 | Post-write criterion self-labeling | **PASS** | "C-19: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at point of satisfaction" |
| C-20 | Structural role ordering as mechanical enforcement | **PASS** | "ROLE 1 — COMPLIANCE OFFICER (C-20: structural gate — all other roles blocked until complete)" |
| C-21 | Schema-typed inventory with criterion-labeled columns | **PASS** | "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)" — 3 C-NN-labeled columns |
| C-22 | Pre-write section criterion self-labeling | **PASS** | "Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML block; C-22: section announces criterion before rows)" |
| C-23 | Pivot deliberation before selection | **PASS** | ROLE 3 enumerates all 4 modes before selecting; selection cites ROLE 2 schema row |
| C-24 | Inertia Advocate embedded at group level | **PASS** | "# Inertia Advocate governance (C-24): Every team in this group receives one Inertia Advocate role file from corps-build." on each `groups:` entry |
| C-25 | Universal output section self-labeling | **PASS** | Universal labeling rule declared; ROLE 1–4 headers all carry C-NN; all sub-sections within roles carry C-NN labels |
| C-26 | Multi-criterion section header | **PASS** | "Signal Schema (C-26: C-11 + C-21 satisfier...)" — header cites C-11 + C-21 simultaneously |
| C-27 | Pivot deliberation tri-part candidate assessment | **PASS** | ROLE 3 uses `Evidence For: / Evidence Against: / Assessment:` for all 4 pivot modes |
| C-28 | Forward-committed items carry execution-state marker | **PASS** | ROLE 1 pre-check uses STATUS: CONFIRMED / STATUS: SCHEDULED / STATUS: ACKNOWLEDGED on every item |

**V-01 Composite: 190/190** — All 5 essential PASS (60), all 3 recommended PASS (30), all 20 aspirational PASS (100)

---

### V-02 — Output Format: Universal Labels + Tri-Part + SCHEDULED Pre-Check

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Section 3 produces `org.yaml` block |
| C-02 | Team areas derived from repo | **PASS** | "The schema is the sole YAML authority — every team area in the YAML must match a 'YAML name (C-02)' cell exactly" |
| C-03 | Group structure present | **PASS** | `groups:` with `teams:` nesting |
| C-04 | Standard roles per team | **PASS** | 2× named roles per team from Section 1 schema "Proposed roles (C-04)" column |
| C-05 | Does not write .craft/roles/ | **PASS** | "HARD BOUNDARY (C-12 satisfier)" explicit; Section 4 post-write confirms |
| C-06 | Pivot mode declared with rationale | **PASS** | Section 2 selects mode with "Rationale: one sentence citing specific Signal Schema row" |
| C-07 | Exec office placeholder present | **PASS** | `exec-office:` in Section 3 YAML |
| C-08 | Amend options listed | **PASS** | Section 5 AMEND-A/B/C with actionable commands |
| C-09 | Detection rationale per area | **PASS** | "Detection evidence (C-09)" column in schema; `# schema-signal:` per YAML team |
| C-10 | Inertia Advocate noted | **PASS** | "# Inertia Advocate: auto-added by corps-build" per team |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Section 1 Signal Schema precedes Section 3 YAML |
| C-12 | Draft boundary front-loaded | **PASS** | "HARD BOUNDARY (C-12 satisfier)" before Section 0, before all structural content |
| C-13 | Self-referential compliance check | **PASS** | Section 0 pre-check item `C-13 -- self-referential confirmation: STATUS: CONFIRMED` |
| C-14 | Dual-stage YAML bracketing | **PASS** | "C-14 dual-bracket: Section 0 pre-check is the pre-YAML gate; this Section 4 is the post-YAML gate." |
| C-15 | Rubric criteria embedded as skill requirements | **PASS** | "C-15 satisfied: pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-25+C-26, C-23+C-27, C-04, C-07, C-16 as requirements" |
| C-16 | Debt-framed amend options | **PASS** | All 3 AMEND options carry "Debt if skipped:" with pipeline consequences |
| C-17 | Forward commitment to future-section criteria | **PASS** | "C-17 satisfied: 5 SCHEDULED items are forward commitments" |
| C-18 | Criterion ID as primary compliance key | **PASS** | "(C-28: ... C-18: C-NN IDs are primary keys throughout)" in Section 0 |
| C-19 | Post-write criterion self-labeling | **PASS** | "C-19 self-labeling: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at satisfaction point" |
| C-20 | Structural role ordering as mechanical enforcement | **PASS** | "Section 0: Compliance Gate (C-20: structural gate — all sections blocked until this section is complete)" |
| C-21 | Schema-typed inventory with criterion-labeled columns | **PASS** | "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)" — 3 C-NN columns |
| C-22 | Pre-write section criterion self-labeling | **PASS** | "Section 1: Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled)" |
| C-23 | Pivot deliberation before selection | **PASS** | Section 2 enumerates all 4 modes before selecting; selection cites Signal Schema row |
| C-24 | Inertia Advocate embedded at group level | **PASS** | Group-level Inertia Advocate governance comment on each `groups:` entry |
| C-25 | Universal output section self-labeling | **PASS** | All 6 sections (0–5) carry C-NN labels; closing summary confirms "C-25: 6 sections labeled (0–5)" |
| C-26 | Multi-criterion section header | **PASS** | "Section 1: Signal Schema (C-26: C-11 + C-21 satisfier...)" cites C-11 + C-21 simultaneously |
| C-27 | Pivot deliberation tri-part candidate assessment | **PASS** | Section 2 uses `Evidence For: / Evidence Against: / Assessment:` for all 4 modes |
| C-28 | Forward-committed items carry execution-state marker | **PASS** | "C-28 satisfied: SCHEDULED vs CONFIRMED on every item" in Section 0 |

**V-02 Composite: 190/190** — All 5 essential PASS (60), all 3 recommended PASS (30), all 20 aspirational PASS (100)

---

### V-03 — Lifecycle Emphasis: 5-Phase Pipeline

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Draft org.yaml block present | **PASS** | DRAFT PHASE produces `org.yaml` block |
| C-02 | Team areas derived from repo | **PASS** | "All team names must trace to SCAN PHASE schema 'YAML name (C-02)' column" |
| C-03 | Group structure present | **PASS** | `groups:` with `teams:` in YAML template |
| C-04 | Standard roles per team | **PASS** | 2× named roles per team from SCAN PHASE schema |
| C-05 | Does not write .craft/roles/ | **PASS** | "DRAFT BOUNDARY (C-12 satisfier)" explicit; FINALIZE PHASE post-write confirms |
| C-06 | Pivot mode declared with rationale | **PASS** | DELIBERATE PHASE selects mode with rationale citing specific Signal Schema row |
| C-07 | Exec office placeholder present | **PASS** | `exec-office:` in DRAFT PHASE YAML |
| C-08 | Amend options listed | **PASS** | FINALIZE PHASE AMEND-A/B/C with actionable commands |
| C-09 | Detection rationale per area | **PASS** | "Detection evidence (C-09)" column; `# schema-signal:` per YAML team |
| C-10 | Inertia Advocate noted | **PASS** | "# Inertia Advocate: auto-added by corps-build" per team |
| C-11 | Pre-YAML scan inventory listed | **PASS** | SCAN PHASE Signal Schema is distinct inventory preceding DRAFT PHASE YAML |
| C-12 | Draft boundary front-loaded | **PASS** | "DRAFT BOUNDARY (C-12 satisfier)" before GATE PHASE pre-check, before all structural content |
| C-13 | Self-referential compliance check | **PASS** | GATE PHASE pre-check item `C-13 -- self-referential confirmation: STATUS: CONFIRMED` |
| C-14 | Dual-stage YAML bracketing | **PASS** | "C-14 dual-bracket: GATE PHASE pre-check is the pre-YAML gate; this post-write is the post-YAML gate." |
| C-15 | Rubric criteria embedded as skill requirements | **PASS** | GATE PHASE pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-26, C-23+C-27, C-04, C-07, C-16 as requirements |
| C-16 | Debt-framed amend options | **PASS** | All 3 AMEND options carry "Debt if skipped:" |
| C-17 | Forward commitment to future-section criteria | **PASS** | "C-17 satisfied: 5 SCHEDULED items are forward commitments" |
| C-18 | Criterion ID as primary compliance key | **PASS** | "(C-18: C-NN IDs as primary keys; C-28: SCHEDULED/CONFIRMED on each item)" in GATE PHASE |
| C-19 | Post-write criterion self-labeling | **PASS** | "C-19: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at satisfaction point" |
| C-20 | Structural role ordering as mechanical enforcement | **PASS** | "GATE PHASE (C-25: C-20 satisfier — compliance gate)"; all phases blocked until prior phase complete with exit artifact |
| C-21 | Schema-typed inventory with criterion-labeled columns | **PASS** | 3 C-NN-labeled columns in Signal Schema |
| C-22 | Pre-write section criterion self-labeling | **PASS** | "Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML; C-22: section self-labeled before rows)" |
| C-23 | Pivot deliberation before selection | **PASS** | DELIBERATE PHASE enumerates all 4 modes; selection cites specific schema row |
| C-24 | Inertia Advocate embedded at group level | **PASS** | Group-level Inertia Advocate governance comment on each `groups:` entry |
| C-25 | Universal output section self-labeling | **PASS** | Universal labeling rule declared; all 5 phase headers + all sub-sections carry C-NN labels |
| C-26 | Multi-criterion section header | **PASS** | **Two instances**: (1) Signal Schema header cites C-11 + C-21; (2) "DELIBERATE PHASE (C-26: C-23 + C-27 satisfier)" cites C-23 + C-27 |
| C-27 | Pivot deliberation tri-part candidate assessment | **PASS** | DELIBERATE PHASE uses `Evidence For: / Evidence Against: / Assessment:` for all 4 modes |
| C-28 | Forward-committed items carry execution-state marker | **PASS** | "C-28 satisfied: SCHEDULED/CONFIRMED execution-state markers on every item" in GATE PHASE |

**V-03 Composite: 190/190** — All 5 essential PASS (60), all 3 recommended PASS (30), all 20 aspirational PASS (100)

Excellence signal: **double C-26** — Signal Schema and DELIBERATE PHASE headers each independently satisfy C-26 via distinct criterion-pair intersections (C-11+C-21 and C-23+C-27). Also unique: **explicit exit artifact declarations** per phase ("Exit artifact: Signal Schema with C-NN-labeled columns") making the artifact chain independently auditable.

---

### V-04 — Role Sequence + Output Format: Two-Tier Labeling

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Sub-section 4.1 produces `org.yaml` block |
| C-02 | Team areas derived from repo | **PASS** | "Every team name in ROLE 4 must match a 'YAML name (C-02)' cell" from ROLE 2 schema |
| C-03 | Group structure present | **PASS** | `groups:` with `teams:` in YAML template |
| C-04 | Standard roles per team | **PASS** | 2× named roles per team from ROLE 2 schema "Proposed roles (C-04)" column |
| C-05 | Does not write .craft/roles/ | **PASS** | Sub-section 1.1 "HARD BOUNDARY"; Sub-section 4.2 confirms "No .craft/roles/ content" |
| C-06 | Pivot mode declared with rationale | **PASS** | ROLE 3 selects mode with rationale citing specific ROLE 2 schema row |
| C-07 | Exec office placeholder present | **PASS** | `exec-office:` in Sub-section 4.1 YAML |
| C-08 | Amend options listed | **PASS** | Sub-section 4.3 AMEND-A/B/C with actionable commands |
| C-09 | Detection rationale per area | **PASS** | "Detection evidence (C-09)" column; `# schema-signal:` per YAML team |
| C-10 | Inertia Advocate noted | **PASS** | "# Inertia Advocate: auto-added by corps-build" per team |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Sub-section 2.1 Signal Schema precedes Sub-section 4.1 YAML |
| C-12 | Draft boundary front-loaded | **PASS** | Sub-section 1.1 "HARD BOUNDARY" before pre-check, before all structural content |
| C-13 | Self-referential compliance check | **PASS** | Sub-section 1.2 pre-check item `C-13 -- self-referential confirmation: STATUS: CONFIRMED` |
| C-14 | Dual-stage YAML bracketing | **PASS** | "C-14 dual-bracket: ROLE 1 Sub-section 1.2 is the pre-YAML gate; this Sub-section 4.2 is the post-YAML gate." |
| C-15 | Rubric criteria embedded as skill requirements | **PASS** | Sub-section 1.2 pre-check names C-12, C-13, C-05, C-11+C-21+C-22+C-26, C-23+C-27, C-04, C-07, C-16 as requirements |
| C-16 | Debt-framed amend options | **PASS** | All 3 AMEND options carry "Debt if skipped:" with pipeline consequences |
| C-17 | Forward commitment to future-section criteria | **PASS** | "C-17 satisfied: 5 SCHEDULED items are forward commitments to named sub-sections" |
| C-18 | Criterion ID as primary compliance key | **PASS** | Sub-section 1.2 pre-check uses C-NN IDs as primary keys |
| C-19 | Post-write criterion self-labeling | **PASS** | "C-19: this block cites C-14, C-02, C-27, C-25, C-26, C-28 at satisfaction" in Sub-section 4.2 |
| C-20 | Structural role ordering as mechanical enforcement | **PASS** | "ROLE 1 — COMPLIANCE OFFICER (C-20: structural gate — blocks ROLE 2, 3, 4 until complete)" |
| C-21 | Schema-typed inventory with criterion-labeled columns | **PASS** | 3 C-NN-labeled columns in Sub-section 2.1 schema |
| C-22 | Pre-write section criterion self-labeling | **PASS** | "Sub-section 2.1 — Signal Schema (C-26: C-11 + C-21 satisfier — precedes YAML; C-22: self-labeled)" |
| C-23 | Pivot deliberation before selection | **PASS** | Sub-section 3.1 enumerates all 4 modes; selection cites specific schema row |
| C-24 | Inertia Advocate embedded at group level | **PASS** | Group-level Inertia Advocate governance comment on each `groups:` entry |
| C-25 | Universal output section self-labeling | **PASS** | Two-tier labeling rule declared; role headers + all sub-section headers carry C-NN labels; "No section at either tier is unlabeled" |
| C-26 | Multi-criterion section header | **PASS** | "Sub-section 2.1 — Signal Schema (C-26: C-11 + C-21 satisfier...)" cites C-11 + C-21 simultaneously |
| C-27 | Pivot deliberation tri-part candidate assessment | **PASS** | Sub-section 3.1 uses `Evidence For / Evidence Against / Assessment` for all 4 modes |
| C-28 | Forward-committed items carry execution-state marker | **PASS** | "C-28 satisfied: SCHEDULED/CONFIRMED on every item" in Sub-section 1.2 |

**V-04 Composite: 190/190** — All 5 essential PASS (60), all 3 recommended PASS (30), all 20 aspirational PASS (100)

Excellence signal: **pre-YAML traceability statement elevated to numbered sub-section** — "Sub-section 4.0 — Pre-YAML Traceability Statement (C-25: C-02 satisfier)" is a labeled structural sub-section, not just a bold inline element. All other variations treat the traceability statement as a `**bold**` element within a larger section; V-04 makes it a first-class compliance artifact.

---

### V-05 — Phrasing Register + Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Draft org.yaml block present | **PASS** | "org.yaml Draft" section produces `org.yaml` block |
| C-02 | Team areas derived from repo | **PASS** | "'YAML name (C-02)' column is the single source of truth for every team name in the org.yaml" |
| C-03 | Group structure present | **PASS** | `groups:` with `teams:` in YAML template |
| C-04 | Standard roles per team | **PASS** | 2× named roles per team from Signal Table "Proposed roles (C-04)" column |
| C-05 | Does not write .craft/roles/ | **PASS** | "DRAFT ONLY (C-12)" first line; Lock-In: "C-05 -- no .craft/roles/ content / STATUS: ACKNOWLEDGED (essential — any violation fails)" |
| C-06 | Pivot mode declared with rationale | **PASS** | "Selected mode: [mode] / Why: [one sentence citing specific Signal Table row... not a general repo observation]" |
| C-07 | Exec office placeholder present | **PASS** | `exec-office:` in org.yaml Draft |
| C-08 | Amend options listed | **PASS** | "Amend Options" section with A/B/C and "How to change it:" commands |
| C-09 | Detection rationale per area | **PASS** | "Detection evidence (C-09)" column in Signal Table; `# from: [Signal Table "Repo signal" value — C-09]` per team |
| C-10 | Inertia Advocate noted | **PASS** | Dedicated paragraph in Signal Table: "corps-build auto-adds one Inertia Advocate role file to every team..." + YAML comment |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Signal Table precedes org.yaml Draft; explicitly distinct from YAML |
| C-12 | Draft boundary front-loaded | **PASS** | "Before you write anything else: State this draft boundary as your first output line: 'DRAFT ONLY (C-12)'" |
| C-13 | Self-referential compliance check | **PASS** | Lock-In: "C-13 -- confirms C-12 is present and precedes all analysis / STATUS: CONFIRMED" |
| C-14 | Dual-stage YAML bracketing | **PASS** | "C-14 dual-bracket: Lock-In block is the pre-YAML gate; this post-write check is the post-YAML gate. Both present." |
| C-15 | Rubric criteria embedded as skill requirements | **PASS** | Lock-In names C-12, C-13, C-05, C-11+C-21+C-22+C-26, C-23+C-27, C-04, C-07, C-16 as requirements |
| C-16 | Debt-framed amend options | **PASS** | All 3 options carry "What you lose if you skip:" with multi-hop pipeline consequences |
| C-17 | Forward commitment to future-section criteria | **PASS** | Lock-In SCHEDULED items for C-11+C-21+C-22+C-26, C-23+C-27, C-04, C-07, C-16 |
| C-18 | Criterion ID as primary compliance key | **PASS** | "(C-25: section self-labeled; C-18: C-NN IDs are primary keys; C-28: status tags on each item)" in Lock-In block |
| C-19 | Post-write criterion self-labeling | **PASS** | "Post-Write Check — (C-25: section self-labeled; C-19: citing C-14 + C-02 + C-25 + C-26 + C-27 + C-28 here)" |
| C-20 | Structural role ordering as mechanical enforcement | **PASS** | "Lock-In Block (C-20: compliance gate — do not begin repo scanning until this block is done)" |
| C-21 | Schema-typed inventory with criterion-labeled columns | **PASS** | "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)" — 3 C-NN columns |
| C-22 | Pre-write section criterion self-labeling | **PASS** | "Signal Table (C-26: C-11 + C-21 satisfier — pre-YAML inventory with C-NN-labeled columns; C-22: self-labeled)" |
| C-23 | Pivot deliberation before selection | **PASS** | Pivot Deliberation section enumerates all 4 modes before selecting; selection cites specific Signal Table row |
| C-24 | Inertia Advocate embedded at group level | **PASS** | Group-level comment includes "Inertia Advocates across this group share governance context... Misaligned groups = incoherent review debates" |
| C-25 | Universal output section self-labeling | **PASS** | All 6 structural sections (Lock-In, Signal Table, Pivot Deliberation, org.yaml Draft, Post-Write Check, Amend Options) carry C-NN labels in headers; closing summary enumerates all 6 |
| C-26 | Multi-criterion section header | **PASS** | "Signal Table (C-26: C-11 + C-21 satisfier...)" cites C-11 + C-21 simultaneously |
| C-27 | Pivot deliberation tri-part candidate assessment | **PASS** | Pivot Deliberation uses `Evidence For: / Evidence Against: / Assessment:` for all 4 modes |
| C-28 | Forward-committed items carry execution-state marker | **PASS** | Lock-In uses STATUS: CONFIRMED / STATUS: ACKNOWLEDGED / STATUS: SCHEDULED on every item |

**V-05 Composite: 190/190** — All 5 essential PASS (60), all 3 recommended PASS (30), all 20 aspirational PASS (100)

Excellence signal: **extended pipeline consequence depth in amend options** — each amend option's "What you lose if you skip:" traces consequences through 4 named corps-* skills (corps-build → corps-pr → corps-committee → corps-rob), compared to other variations' typically 2–3 skill citation. Also: **Inertia Advocate governance explained as prose narrative** in the Signal Table section, establishing the organizational stakes of grouping decisions before the YAML is produced.

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (100) | **Total** | Golden? |
|-----------|---------------|------------------|-------------------|-----------|---------|
| V-01 | 60 | 30 | 100 | **190** | YES |
| V-02 | 60 | 30 | 100 | **190** | YES |
| V-03 | 60 | 30 | 100 | **190** | YES |
| V-04 | 60 | 30 | 100 | **190** | YES |
| V-05 | 60 | 30 | 100 | **190** | YES |

**All variations: 190/190. R6 is the first round where every variation achieves the maximum score.**

---

## Excellence Signals

R6 achieves the ceiling by treating C-25 through C-28 as structural invariants across all 5 axes. The patterns that distinguish individual variations — and point toward v7 criteria — are:

**1. Double multi-criterion header (V-03):** Two separate section headers each independently satisfy C-26 via distinct criterion-pair intersections. DELIBERATE PHASE header cites C-23 + C-27; Signal Schema header cites C-11 + C-21. Current C-26 requires only one such header; V-03 creates two, forming a richer criterion-intersection map across the output.

**2. Phase exit artifact declaration (V-03):** Each phase carries an explicit "Exit artifact:" annotation naming the specific deliverable the phase produces (e.g., "Exit artifact: Signal Schema with C-NN-labeled columns"). This makes the artifact chain auditable from the phase structure alone — a scorer can verify that each phase produced the correct artifact without reading the full phase content.

**3. Traceability statement elevated to numbered labeled sub-section (V-04):** Sub-section 4.0 is a full `####`-level structural section with C-NN label "(C-25: C-02 satisfier)" dedicated solely to the pre-YAML traceability statement. All other variations use a `**bold**` inline element for this element. V-04 makes it a first-class compliance artifact, extending C-22 coverage to a structural element that previously sat in a gray zone.

**4. Section count confirmation in closing summary (V-02):** The closing summary explicitly states "C-25: 6 sections labeled (0–5)" — a provable numerical claim about C-25 satisfaction that a scorer can verify by counting section headers. Other variations declare the universal labeling rule but do not provide a verifiable count.

---

```json
{"top_score": 190, "all_essential_pass": true, "new_patterns": ["Double multi-criterion header: two separate section headers each independently satisfy C-26 via distinct C-NN pairs (V-03: DELIBERATE PHASE cites C-23+C-27; Signal Schema cites C-11+C-21)", "Phase exit artifact declaration: each phase carries an explicit Exit artifact annotation naming its deliverable, making the artifact chain auditable from phase structure alone (V-03)", "Traceability statement elevated to numbered labeled sub-section: Sub-section 4.0 is a full structural section with C-NN self-label rather than an inline bold element, extending C-22 coverage to this previously gray-zone element (V-04)"]}
```
