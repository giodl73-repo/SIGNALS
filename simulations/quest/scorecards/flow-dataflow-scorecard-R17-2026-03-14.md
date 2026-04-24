# flow-dataflow — Round 17 Scoring

## Scoring methodology

Trace artifact is `placeholder`; variations are scored as **prompt designs** — does the prompt's structure reliably elicit outputs that satisfy each criterion?

Weight: Essential 60 pts (15 each), Recommended 30 pts (10 each), Aspirational 10 pts (44 criteria × 0.227 pts each, PARTIAL = 0.114 pts).

---

## Essential Criteria (C-01 to C-04) — all variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Data lineage chain | PASS | PASS | PASS | PASS | PASS |
| C-02 | Boundary error handling | PASS | PASS | PASS | PASS | PASS |
| C-03 | Data loss point identification | PASS | PASS | PASS | PASS | PASS |
| C-04 | Schema state at each stage | PASS | PASS | PASS | PASS | PASS |

All variations: **60/60** essential. `all_essential_pass: true`.

Evidence: Every variation mandates 7-column boundary tables (including `Error Handling`, `Data Loss Flag`, `Schema Delta`) and 4-column stage tables (`Schema In | Schema Out`). V-03 adapts these to labeled-sentence form via Part C substitution — still satisfies C-04.

---

## Recommended Criteria (C-05 to C-07) — all variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-05 | Latency characterization | PASS | PASS | PASS | PASS | PASS |
| C-06 | Stale data windows | PASS | PASS | PASS | PASS | PASS |
| C-07 | Domain framing | PASS | PASS | PASS | PASS | PASS |

All variations: **30/30** recommended.

Evidence: SC-7 requires `Stage Latency` column (V-03: labeled latency sentence per Part C). [A-11] STALE ANALYSIS with normal-op and failure-mode rows is mandatory. All pipelines use domain-specific entities (hotel F&B, B2B distribution, SaaS subscription, retail loyalty points, telecom CDR).

---

## Aspirational Criteria (C-08 to C-51) — differentiated analysis

### Common PASSes (all 5 variations)

These 40 criteria are satisfied by all variations. Notes given only where evidence bears emphasis.

| ID | Criterion | All 5 | Evidence note |
|----|-----------|-------|---------------|
| C-08 | Recovery prescriptions | PASS | [A-12] + `Fall back to [A-01] if [condition]` formula mandated |
| C-09 | Pattern trade-off analysis | PASS | [A-14] requires ≥1 alternative pattern, ≥2 dimensions |
| C-10 | Pre-trace domain context gate | PASS | [A-02] before Stage 1; ≥2 entity names from [A-01] reused in [A-02] |
| C-11 | Interleaved boundary gates | PASS | SC-2 forces boundary table before each stage advance inline |
| C-12 | Domain entity exposure per boundary | PASS | Part A `Entity` column: "Named entity from [A-02] vocabulary" |
| C-13 | Pre-declared staleness contract | PASS | [A-02] SLA declared before Stage 1 per SC-5 verbatim requirement |
| C-14 | Additive elapsed time calculation | PASS | SC-3 accumulates `Elapsed (cumul.)` continuously; [A-11] cites final value |
| C-15 | Incumbent or manual-process baseline | PASS | SC-13 requires [A-01] in [A-12] AND [A-14] — closes C-08/C-09 loop |
| C-16 | Cross-role reference chain | PASS | SC-1 `Citing:` opener with named artifact tokens at every non-first role |
| C-17 | Immutability declaration | PASS | SC-5 verbatim phrase: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." |
| C-18 | Incremental boundary elapsed computation | PASS | SC-3 with [Apply SC-3 at every boundary block] callback |
| C-19 | Machine-verifiable citation convention | PASS | `[A-xx]` token convention used throughout; violations by definition of absent token |
| C-20 | Stage-write progression gate | PASS | SC-2 as explicit inline progression gate |
| C-21 | Binary freshness verdict per boundary | PASS | SC-4: exactly `FRESH` or exactly `STALE` |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY table before all role output |
| C-23 | Phase gate self-verification checklists | PASS | [A-05] and [A-08] checklists (V-05 adds [A-00]) |
| C-24 | Upfront constraint section with inline callback syntax | PASS | STRUCTURAL CONSTRAINTS + `[Apply SC-N ...]` callbacks throughout |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | [A-05], [A-08] (and [A-00] for V-05) each appear in ARTIFACT REGISTRY |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | Formula `Fall back to [A-01] if [specific named failure condition]` required |
| C-28 | Named-column boundary block schema | PASS | Standalone BOUNDARY BLOCK SCHEMA section with exact column order |
| C-29 | Trade-off analysis as prompt-required section | PASS | SC-8 + [A-14] as required named section |
| C-30 | Output register declaration with format-specific field-compliance markers | PASS | REGISTER DECLARATION with Part A/B in all variations |
| C-31 | Pre-declared boundary block schema section | PASS | Standalone section before any role output |
| C-32 | Register-specific compliance marker mapping | PASS | Part A table: required field → column header → cell form → disqualifying form |
| C-34 | Per-boundary incumbent equivalent column | PASS | Part A `Incumbent Equiv.`: `[A-01]: [named manual step + duration]` |
| C-35 | INCUMBENT TOTAL as required pre-trade-off artifact | PASS | Part B: [A-13] with additive role breakdown + Grand Total row |
| C-36 | Baseline-first artifact ordering | PASS | SC-11 positional lock: [A-01] before any stage trace or boundary block |
| C-37 | REGISTER DECLARATION Parts A/B as single-location authority | PASS | "This section is the sole authoritative reference for C-34 and C-35" verbatim |
| C-38 | Skip-level citation requirement | PASS | SC-12 in all variations; Commerce/Finance cites first-role boundary artifacts |
| C-39 | Skip-level SC names governed role | PASS | SC-12 names governing role by name in its body |
| C-40 | Skip-level SC declares position distance | PASS | "Position distance is two" stated explicitly in SC-12 body |
| C-41 | Phase Gate 2 skip-level item cites SC identifier | PASS | [A-08] checklist item uses `[SC-12]` by numbered identifier |
| C-42 | C-37+C-41 closed verification chain co-occurrence | PASS | REGISTER DECLARATION Parts A/B (C-37) + Phase Gate 2 [SC-12] (C-41) both present |
| C-43 | All three skip-level SC attributes co-present in single block | PASS | SC-12 block: governed artifact token + governed role + position distance — no distribution |
| C-44 | Baseline-closure SC as named upfront constraint | PASS | SC-13 BASELINE CLOSURE in STRUCTURAL CONSTRAINTS — enforces C-15 connection |
| C-46 | SC-13 BASELINE CLOSURE as named entry in closed-chain paragraph | PASS | Named entry with governed artifacts [A-12], [A-14] and enforcement mechanism |
| C-48 | Governed artifact tokens named in each SC closed-chain entry | PASS | Every SC entry names its governed `[A-xx]` tokens |
| C-49 | Enforcement mechanism named in each SC closed-chain entry | PASS | Every SC entry describes its enforcement pathway |
| C-50 | Baseline authority token dual-slot presence | PASS | SC-8: `[A-01]` in governed-token declaration AND enforcement clause. SC-9: `[A-01]` in cell-form requirement AND detectability sentence. SC-11: `[A-01]` named in positional lock AND violation description. SC-13: `[A-01]` in governed-artifact list AND header-callback enforcement. |
| C-51 | Violation-detectability location in enforcement mechanism | PASS | All 13 SC entries carry explicit location qualifier. SC-1: "role-opener line without reading the role body". SC-13: "header line alone". Full per-SC table matches R17 variation summary. |

---

### Differentiating criteria

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-26 | Non-natural role ordering as citation stress test | **FAIL** | **PASS** | **FAIL** | **FAIL** | **PASS** |
| C-33 | Register-invariant declaration for non-tabular registers | **FAIL** | **FAIL** | **PASS** | **FAIL** | **FAIL** |
| C-45 | Format-mode declaration with criterion substitution map | **FAIL** | **FAIL** | **PASS** | **FAIL** | **FAIL** |
| C-47 | SC-14 FORMAT MODE DECLARATION as named closed-chain entry | **FAIL** | **FAIL** | **PASS** | **FAIL** | **FAIL** |

**C-26 evidence**: V-02 (Ops→Fin→Com) and V-05 (Ops→Com→Fin) are non-natural orderings where the first role is not Finance. V-01, V-03, V-04 all run Finance→Operations→Commerce (natural Finance-leads ordering).

**C-33/C-45/C-47 evidence**: V-03 (prose register) activates SC-14 FORMAT MODE DECLARATION via [A-15] artifact, Part C criterion substitution map (tabular→prose pass condition mapping), and SC-14 as a 14th named entry in the exhaustive closed-chain paragraph. V-01, V-02, V-04, V-05 are tabular-only — no non-tabular register declared, so no register-invariant or format-mode substitution needed or present.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational (x/44 × 10) | **Total** |
|-----------|-----------|-------------|--------------------------|-----------|
| V-01 | 60.00 | 30.00 | 40/44 × 10 = 9.09 | **99.09** |
| V-02 | 60.00 | 30.00 | 41/44 × 10 = 9.32 | **99.32** |
| V-03 | 60.00 | 30.00 | 43/44 × 10 = 9.77 | **99.77** |
| V-04 | 60.00 | 30.00 | 40/44 × 10 = 9.09 | **99.09** |
| V-05 | 60.00 | 30.00 | 41/44 × 10 = 9.32 | **99.32** |

---

## Ranking

1. **V-03** — 99.77 (prose register, SC-14, Part C substitution map, C-33/C-45/C-47 all PASS)
2. **V-02** — 99.32 (non-natural Ops→Fin→Com, skip-level stress test, C-26 PASS)
2. **V-05** — 99.32 (non-natural Ops→Com→Fin + Phase Gate 0, C-26 PASS)
4. **V-01** — 99.09 (natural sequence, hotel F&B, baseline template)
4. **V-04** — 99.09 (max inertia ≥5 steps, richer [A-01] but no new structural patterns)

---

## Excellence Signals from V-03 (top scorer)

V-03's margin over V-02/V-05 comes from three accumulated pattern passes (C-33, C-45, C-47) that require the prose register pathway — activating SC-14 as a 14th structural constraint and [A-15] as a production artifact. Two new patterns emerge from V-03 that are not yet captured by any existing criterion:

### New Pattern 1 — Register-adaptive detectability-location language

C-51 requires a detectability-location qualifier in every SC closed-chain entry. V-03 extends this: when the active register is prose, each SC entry's location qualifier references the register's structural unit rather than a tabular one. Compare:

| SC | Tabular (V-01) | Prose (V-03) |
|----|----------------|--------------|
| SC-3 | "at the column-header and cell-value level" | "at the Elapsed (cumul.) sentence within the boundary section" |
| SC-4 | "at the cell-value level without reading surrounding prose" | "at the Verdict sentence level without reading surrounding prose" |
| SC-7 | "at the table-header row without reading row contents" | "from the stage block's first two sentences without reading further" |
| SC-9 | "at the cell level" | "from the Incumbent Equiv. sentence without reading surrounding prose" |

C-51 says *a* location must be named. It does not require the location to match the active register. A tabular-location qualifier applied to a prose output would be structurally incorrect. The pattern: **every SC detectability-location qualifier must reference the structural unit of the active register** — column/cell for tabular, sentence/label for prose.

### New Pattern 2 — Verbatim detectability statement in [A-15] FORMAT MODE DECLARATION artifact

V-03 requires [A-15] to include this verbatim: "Format-mode violations in prose stage blocks are detectable from the stage block's first two sentences without reading further." This creates a **machine-readable violation-detection rule as a first-class output artifact** — not buried in the closed-chain paragraph, but in a named artifact (token [A-15]) that appears before [A-03] and can be cited. The closed-chain paragraph's SC-14 entry then governs [A-15] and names this detectability location. A format-mode violation check requires: (a) [A-15] exists before [A-03], (b) [A-15] contains the verbatim detectability statement, (c) SC-14 in the closed-chain paragraph points to [A-15] for the substitution map. No existing criterion captures the **verbatim detectability statement as content within the FORMAT MODE DECLARATION artifact itself**.

---

```json
{"top_score": 99.77, "all_essential_pass": true, "new_patterns": ["register-adaptive detectability-location language: each SC closed-chain entry's violation-detectability location qualifier must reference the structural unit of the active register (column/cell for tabular; sentence/label for prose) — C-51 captures that a location exists but not that it must match the register", "verbatim detectability statement as required content in [A-15] FORMAT MODE DECLARATION artifact: the artifact itself must contain a machine-readable verbatim statement declaring the structural location where format-mode violations surface, making the detectability claim navigable by artifact token rather than only by closed-chain paragraph entry"]}
```
