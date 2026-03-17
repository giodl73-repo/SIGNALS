# prove-interview — Round 8 Scoring

## Baseline Architecture

All five R8 variations carry the R7 ceiling architecture: **C-01..C-22 all PASS = 160 pts**. The only variable is C-23 (5 pts), which was added in v8. Scoring below focuses on C-23 with abbreviated C-01..C-22 confirmation.

---

## Per-Criterion Summary (All Variations)

**C-01..C-05 — Essential (60 pts):** PASS all variations. Persona identity, prior knowledge scope, persona-voice answers, evidence extraction, and grounded answers all present per R7 architecture.

**C-06..C-08 — Recommended (30 pts):** PASS all variations. Surprising moment labeled, probing Q+followup present, two meaningfully distinct personas (SKEPTIC + CHAMPION) with distinct roles.

**C-09..C-21 — Aspirational base (55 pts):** PASS all variations. Cross-interview synthesis with Inertia Verdict Matrix, evidence confidence rated with rationale, disposition arc structured, critical contradiction named and ranked, Q1 current-practice anchors, arc claims quote-anchored, contradiction both-sides sourced, non-substitutable columns, roster-level disposition labels, skeptic-first ordering with prior-signal framing, COLUMN POLICY + DISPOSITION REQUIREMENT named compliance blocks covering full-absence + partial-compliance conditions in three-column tabular format.

**C-22 — Incumbent Coupling Table (5 pts):** PASS all variations. Named Incumbent Coupling Table with per-factor ratings sourced to S-00 HE-# attributions. Switch Cost column in Inertia Verdict Matrix with explicit sourced-from citations. Lifecycle gate confirmed before S-01 declared. COLUMN POLICY block includes additive-only row covering C-22/C-16 boundary.

---

## C-23 Scoring — The Variable Criterion

| Variation | C-23 Verdict | Evidence Note | Pts |
|-----------|-------------|---------------|-----|
| V-01 | **FAIL** | Arc Signal describes switching friction in aggregate prose ("embedded workflows create high switching costs") — no coupling factor named by table row. Friction observation present; coupling factor provenance absent. All three C-23 conditions unmet. | 0 |
| V-02 | **PARTIAL** | Arc Signal prose names switching friction magnitude (e.g., "high switching cost") but does not identify the source coupling factor by its Incumbent Coupling Table row name. Magnitude condition partially met; explicit coupling factor name and inertia component connection absent. Analogous to C-22 PARTIAL-B (derived output present, source attribution absent). | 2 |
| V-03 | **PASS (minimal)** | Explicit per-factor mandate in Arc Signal synthesis step. Coupling factor identified by table row name, magnitude stated from coupling table rating, connection to inertia verdict component present ("confirms / moderates / overturns"). All three C-23 conditions met in prose form. | 5 |
| V-04 | **PASS** | Incumbent-first transcript ordering as structural gate reinforces lifecycle guarantee that per-factor data is pre-locked before Arc Signal is written. Per-factor friction claim names coupling factor, states magnitude, and connects to inertia verdict component. Structurally cleaner than V-03 because the gate enforces provenance rather than relying on authorial discipline. | 5 |
| V-05 | **PASS (maximum)** | Arc Signal rendered as a per-factor table with explicit columns: **Coupling Factor** (names the table row) / **Friction Magnitude** (from coupling table rating) / **Inertia Component** (confirms, moderates, or overturns the inertia signal). Machine-parseable. Each row satisfies all three C-23 conditions independently. No prose ambiguity — each coupling factor gets its own row. | 5 |

---

## Composite Scores

| Variation | C-01..C-22 | C-23 | Total | Score |
|-----------|-----------|------|-------|-------|
| V-05 | 160 | 5 | **165/165** | 100% |
| V-04 | 160 | 5 | **165/165** | 100% |
| V-03 | 160 | 5 | **165/165** | 100% |
| V-02 | 160 | 2 | **162/165** | 98.2% |
| V-01 | 160 | 0 | **160/165** | 97.0% |

---

## Ranking

1. **V-05** — Maximum PASS: per-factor table in Arc Signal. Structurally strongest: tabular format enforces one-row-per-factor isolation, making all three C-23 conditions explicit and independently verifiable.
2. **V-04** — PASS with lifecycle structural gate as enforcement mechanism. Incumbent-first ordering guarantees per-factor data is pre-locked before Arc Signal authoring begins.
3. **V-03** — PASS minimal: per-factor mandate in prose. All conditions met but prose form cannot enforce one-condition-per-factor isolation the way a table can.
4. **V-02** — PARTIAL: magnitude present, coupling factor row name absent. Friction is described; provenance to the Incumbent Coupling Table is not established.
5. **V-01** — FAIL: aggregate friction prose. C-22 is structurally complete but C-23 chain is broken at the Arc Signal step.

---

## Excellence Signals (from V-05 > V-04 > V-03)

**Signal 1: Tabular Arc Signal enforces per-factor isolation.** V-05 renders the Arc Signal as a structured table with Coupling Factor / Friction Magnitude / Inertia Component columns. This makes every C-23 condition independently checkable per row — no sentence-level ambiguity about whether the factor was named, the magnitude was stated, or the inertia connection was made. The table format is the structural ceiling for C-23 for the same reason C-21 is the structural ceiling for C-19/C-20: tabular form makes each condition machine-parseable and removes the possibility of a multi-condition sentence that satisfies two C-23 requirements for one factor while leaving a second factor untraced.

**Signal 2: Lifecycle gate as provenance guarantee.** V-04 adds structural enforcement that the per-factor data available in the Arc Signal was pre-locked before any human-subject interviews ran. This closes the C-23 provenance question at the source: if the Incumbent Coupling Table was finalized under the lifecycle gate (C-22 requirement), then per-factor Arc Signal claims that cite table rows are provenance-verified by construction. V-03 achieves the same C-23 outcome but relies on the author naming the coupling factor correctly — V-04 enforces that the coupling factor existed and was rated before the Arc Signal was written.

**Signal 3: C-22 → C-23 chain requires explicit name-tracing, not magnitude-inference.** V-02 identifies the failure mode: a prose Arc Signal can characterize switching friction at the correct magnitude without ever tracing it to a named row in the Incumbent Coupling Table. Magnitude without coupling factor name = PARTIAL. The discipline required for C-23 PASS is not "describe how hard switching is" — it is "name the coupling factor from the table, state its rated magnitude, connect it to the inertia verdict." This three-part chain must be explicit in every per-factor claim.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["Tabular Arc Signal with Coupling Factor / Friction Magnitude / Inertia Component columns enforces per-factor C-23 isolation — one row per coupling factor, each row independently verifiable against all three C-23 conditions", "Lifecycle gate as provenance guarantee: incumbent-first structural ordering locks per-factor coupling data before Arc Signal is written, making coupling factor name citations provenance-verified by construction rather than by authorial discipline", "C-23 fails on magnitude-without-name: prose that correctly characterizes switching friction magnitude without tracing it to a named Incumbent Coupling Table row earns PARTIAL — the name-tracing requirement is the discriminating condition between PARTIAL and PASS"]}
```
