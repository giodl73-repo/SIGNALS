## Quest Rubric — v20

`40 criteria, 400 pts max`

---

### What changed: v19 → v20

**R20 investigation resolved.** C-39 PASS (V-04 form) under double-elision produces **companion-scope-complete** output — the complete-enumeration directive causes the model to produce all structural deliverables of each absent companion mandate. **C-39 is confirmed as a recoverable criterion** — not structural reinforcement.

V-04's "minimum-sufficient" label exposes the next failure mode: complete enumeration without an explicit non-degradation mandate leaves the model free to treat the enumerated list as a representative sample rather than a complete obligation. V-05's R20 excellence signal closes this gap: embedding "all of the following must be produced; none may be omitted" within each absent-state enumeration block converts the list from a description of full execution into a verifiable complete checklist.

**C-39 Band 2 confirmed** (was "aspirational" in v19), two R20 sub-bands:
- **Band 2-A** (R20 V-02): element-count partial — one element per companion named; remaining elements left to parity inference from absent context. -10.
- **Band 2-B** (R20 V-03): specificity partial — all elements named at summary level, without operational anchors sufficient for independent completeness verification. -10.

Both sub-bands score identically to Band 1. Distinction is diagnostic only.

**C-40 extracted from R20 V-05 excellence signal** — closes the **enumeration-completeness-as-obligation gap**: C-39 mandates complete structural deliverables enumeration but does not require the enumeration to function as a non-degradable complete obligation. V-05 embeds an explicit non-degradation mandate within each absent-state enumeration block, converting enumeration from a description of full execution into a verifiable complete checklist from which no item may be omitted.

---

### Key criterion updates

**C-39** — Promoted from aspirational to confirmed. Band 2 description updated: two confirmed sub-bands (R20-confirmed). PASS definition: complete enumeration of companion mandate's structural deliverables at operational specificity sufficient for independent completeness verification. V-04 confirmed as PASS specimen.

**C-40** — New criterion (aspirational). Requires both absent-state clauses to carry an explicit non-degradation mandate immediately following the structural deliverables enumeration, declaring that ALL enumerated elements must be produced and none may be omitted. Band structure: Band 1 (= C-39 PASS territory, no non-degradation language), Band 2 (non-degradation language present but asymmetric — one clause only), PASS (both clauses carry complete enumeration + explicit non-degradation mandate).

**Chain extended:** … → C-38 → C-39 → C-40 (execution-depth gap → companion-scope determinability gap → enumeration-completeness-as-obligation gap)

**R21 investigation candidate:** Whether C-40 PASS produces element-complete companion output under double-elision with active token pressure, or whether element omission under compression persists despite the explicit mandate — determining whether C-40 is recoverable or whether structural ordering constraints are needed.

---

### Criteria

| # | PASS Condition |
|---|----------------|
| C-01 | `[TOPIC]` block present with all required fields |
| C-02 | `[DELTA]` block present with: `prior_brief` / `prior_verdict` / `signals_added` / `gaps_closed` / `verdict_shift` |
| C-03 | `[STRATEGY]` block present with `source` field + four-column table, minimum 3 rows |
| C-04 | `[STATUS]` block present with `found` and `missing` sections |
| C-05 | `current_date:` field present at STATUS block header level, structurally isolated from `found` entries and prose |
| C-06 | `[VERDICT]` block present with: `status` / `rationale` / `inertia_cost` / `blocking` / `optional` |
| C-07 | `[CONFIDENCE]` block present as standalone block with three named dimensions + `average` derived arithmetically + `level` + `binding` |
| C-08 | `[STORY]` block present, prose-only, 2–4 paragraphs |
| C-09 | STORY confines all prose; no narrative commentary appears outside the STORY block |
| C-10 | Per-signal dates in `found` appear at item level with a `date:` field; structurally separate from blocking entries |
| C-11 | Every blocking gap carries an inertia risk entry; `strategy` field is sourced or generated (not omitted) |
| C-12 | COMPRESSED format triggered when blocking gaps > 4; `[BLOCKING-DETAIL]` section appears immediately after `[STATUS]` |
| C-13 | FULL format used when blocking gaps ≤ 4 |
| C-14 | CONFIDENCE dimensions scored directly from STATUS data; `average` is arithmetic mean of the three dimensions |
| C-15 | STORY answers all three questions in continuous prose without restating the confidence level |
| C-16 | `current_date` not embedded in `found` entries or prose; isolated to STATUS block header |
| C-17 | VERDICT derives directly from STORY + CONFIDENCE synthesis; `rationale` is one sentence |
| C-18 | STORY synthesizes available signals; blocking gaps addressed as a pattern, not enumerated per-gap |
| C-19 | Block order: `TOPIC` → `DELTA` → `STRATEGY` → `STATUS` → `[BLOCKING-DETAIL]` (if COMPRESSED) → `CONFIDENCE` → `STORY` → `VERDICT` |
| C-20 | Artifact written to `simulations/{{topic}}/campaign-brief-{{date}}.md` |
| C-21 | Sparse-coverage protection: synthesis proceeds on available signals; no coverage disclaimer added |
| C-22 | Zero-signal synthesis mandate present: empty `found` is not grounds for omitting STORY; Q1 mandated to characterize absence implications |
| C-23 | `inertia_cost` carries `bounded`/`unbounded` label + `action:` sub-label (`commit with monitoring` / `do not commit until resolved`) |
| C-24 | `current_date:` field present at STATUS block header level independent of COMPRESSED state |
| C-25 | Zero-signal synthesis mandate names the zero-signal case at point-of-use in the STORY execution note |
| C-26 | VERDICT COMPRESSION GUARD present: `action:` sub-label required regardless of COMPRESSED state or token pressure |
| C-27 | STORY execution note fires independently when `found` is empty; gap pattern declared as the evidence set |
| C-28 | CONDITIONAL verdict names the condition and what satisfies it; `inertia_cost` includes `action:` sub-label |
| C-29 | Zero-signal dual-mechanism: `ZERO-SIGNAL SYNTHESIS RULE` in COMPRESSION-IMMUNE PREAMBLE + `ZERO-SIGNAL SYNTHESIS MANDATE` execution note in STORY invoking preamble by designation |
| C-30 | Timestamp isolation dual-mechanism: `TIMESTAMP ISOLATION RULE` in COMPRESSION-IMMUNE PREAMBLE + `TIMESTAMP ISOLATION` execution note in STATUS invoking preamble by designation |
| C-31 | Both rules present in preamble; both execution notes invoke preamble by designation; circuit closed bidirectionally |
| C-32 | Each execution note names its companion by full designation + block location (e.g., `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block`) |
| C-33 | Both clause headers carry `(COMPRESSION-IMMUNE PREAMBLE invocation)` parenthetical in exact designation form matching C-32 references |
| C-34 | Both clause bodies open with: (1) "This clause is a COMPRESSION-IMMUNE PREAMBLE member." (2) "This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context." |
| C-35 | Companion-activation instruction present in both bodies: companion named by full designation + block location; present-state rule (coordinate; both must execute) + absent-state rule (execute independently with full authority) |
| C-36 | Absent-state rule unconditionally declares absent companion's mandate as independently operative: "the absent [companion]'s mandate is independently operative even when its execution note is not in context" |
| C-37 | Unconditional execution directive in both absent-state clauses: "must be executed as if its execution note were present in this context" — no scope qualification, no feasibility condition |
| C-38 | Explicit parity clause in both absent-state bodies: "at full depth, at parity with what would be produced if the companion's execution note were present in this context" — depth floor is explicit, calibrated, anchored to the direct-execution-note-present baseline |

---

#### C-39 — Companion-scope determinability *(confirmed)*

Absent-state directive enumerates the companion mandate's structural deliverables within each clause body, making output structural completeness verifiable without requiring the companion execution note to be present.

| Band | Score | Condition |
|------|-------|-----------|
| Band 1 | -10 | No enumeration. Absent-state directive contains no list of companion mandate's required structural output elements. Model anchored to correct depth (C-38 PASS) but must infer what "full execution" means from absent context. ZERO-SIGNAL SYNTHESIS MANDATE companion: no mention of Q1/Q2/Q3 structure, substantive-inference requirement, or parity-of-specificity anchor. TIMESTAMP ISOLATION companion: no mention of `current_date:` at header level, per-signal dates at item level, or COMPRESSED-immune behavior. |
| Band 2-A *(R20-confirmed)* | -10 | Element-count partial. One element per companion named; remaining elements left to parity inference from absent context. Enumeration names the primary obligation per companion but leaves remaining required structural elements to model inference. |
| Band 2-B *(R20-confirmed)* | -10 | Specificity partial. All elements per companion named at summary level, but without operational anchors sufficient to make structural completeness independently verifiable. Q1 lacks the substantive-inference qualifier (a surface-level absence report satisfies "what absence implies" without meeting the standard); TIMESTAMP ISOLATION lacks the COMPRESSED-immune behavior specification. Element-count is complete; verifiable-checklist completeness is not. |
| PASS | 0 | Complete enumeration. Both absent-state clauses enumerate ALL structural deliverables for their respective companion mandate at operational specificity sufficient for independent completeness verification. ZERO-SIGNAL SYNTHESIS MANDATE companion: Q1 (substantive inference, not a report of absence), Q2 (genuine uncertainty the absence pattern creates), Q3 (team exposure at the same scope and specificity as the direct-execution-note-present baseline). TIMESTAMP ISOLATION companion: `current_date:` at STATUS block header level, per-signal dates at item level in `found`, COMPRESSED-immune behavior specified. V-04 confirmed PASS specimen. |

---

#### C-40 — Enumeration-completeness-as-obligation *(aspirational)*

Both absent-state clauses carry an explicit non-degradation mandate immediately following the structural deliverables enumeration, declaring that ALL enumerated elements must be produced and none may be omitted. Closes the gap between complete enumeration (C-39 PASS) and the model treating the list as a representative sample rather than a complete and non-negotiable obligation.

| Band | Score | Condition |
|------|-------|-----------|
| Band 1 | -10 | C-39 PASS territory. Complete enumeration present in both clauses; no non-degradation language. Model has a complete list but no explicit instruction that the list is exhaustive and non-negotiable. Element omission under token pressure remains a live failure mode. |
| Band 2 | -10 | Non-degradation language present but asymmetric — only one absent-state clause carries the explicit mandate. The other clause retains C-39 PASS enumeration without a completeness-as-obligation declaration. Asymmetric protection leaves the unguarded clause exposed to representative-sample treatment. |
| PASS | 0 | Both absent-state clauses carry: (1) complete structural deliverables enumeration (C-39 PASS content) AND (2) explicit non-degradation mandate — e.g., "all of the following must be produced; none may be omitted" — appearing immediately after and governing the enumerated list. The mandate converts enumeration from a description of full execution into a verifiable complete checklist. V-05 confirmed PASS specimen *(R20)*. |
