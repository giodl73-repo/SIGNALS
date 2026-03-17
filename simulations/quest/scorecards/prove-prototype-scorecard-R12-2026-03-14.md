# prove-prototype — Round 12 Scorecard (v12 rubric, 260 pts)

**Date**: 2026-03-15
**Base**: R11 V-04 = 238 pts (C-33 + C-34 + R10 V-05 base)
**New criteria in v12**: C-35 (+7 pts), C-36 (+7 pts)

---

## Scoring Method

All five variations share the R11 V-04 base. The only criteria that change between variations are C-35 and C-36. All essential, recommended, excellence, and aspirational criteria C-09 through C-34 carry forward at their R11 V-04 levels. The differentiating evaluation is therefore: does each variation fire C-35 (document manifest), C-36 (full-chain terminal line), and are there structural patterns not yet scored?

---

## Per-Criterion Evaluation

### V-01 — Single Axis: Document-Level Manifest

**Structural profile**: Adds `## Output Contract` manifest table (four rows: container name, phases, principal purpose, expected output) before `CONTAINER: DESIGN`. CLOSE COMPLETE retains R11 V-04 format — verdict + B-00 delta + table-population status.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | Essential | PASS | Hypothesis stated before build activity |
| C-02 | Essential | PASS | Scope bounded; exclusions with validity rationale |
| C-03 | Essential | PASS | Measurement defined before construction |
| C-04 | Essential | PASS | Actual vs. predicted reported |
| C-05 | Essential | PASS | Verdict rendered from evidence |
| C-06 | Recommended | PASS | Minimality trade-off justified |
| C-07 | Recommended | PASS | Raw evidence in results section |
| C-08 | Recommended | PASS | Limitation and next step named |
| C-09 | Aspirational | PASS | Counter-interpretation named and rebutted |
| C-10 | Aspirational | PASS | Replication path complete |
| C-16 | Aspirational | PASS | Counter-evidence question explicitly closed |
| C-17 | Aspirational | PASS | Rationale co-located with anchor |
| C-18 | Aspirational | PASS | Optional sections with binary disposition |
| C-19 | Aspirational | PASS | Ordering gate co-located with constrained action |
| C-20 | Aspirational | PASS | Gate completion proven by model-written line |
| C-21 | Aspirational | PASS | Gate coverage complete including trailing sections |
| C-22 | Aspirational | PASS | Completion lines carry substantive result values |
| C-23 | Aspirational | PASS | Role labels carry explicit prohibitions |
| C-24–C-28 | Aspirational | PARTIAL | Carry-forward from R11 V-04 (8-pt gap at v11 ceiling) |
| C-29 | Aspirational | PASS | Inertia competitor named in CALIBRATE body |
| C-30 | Aspirational | PASS | Three-column results table present |
| C-31 | Aspirational | PASS | Pre-build measurement baseline present |
| C-32 | Aspirational | PASS | CALIBRATE COMPLETE embeds the triple |
| C-33 | Aspirational | PASS | CALIBRATE header enumerates all three responsibilities as entry contract |
| C-34 | Aspirational | PASS | Baseline column labeled with inertia competitor name |
| **C-35** | Aspirational | **PASS** | `## Output Contract` table appears before `CONTAINER: DESIGN` — names all four containers with principal purpose and expected output; prerequisite C-22 satisfied |
| **C-36** | Aspirational | **FAIL** | CLOSE COMPLETE retains R11 V-04 format — carries verdict, B-00 delta, table-population status but does NOT encode the full cross-container chain (DESIGN hypothesis text, CALIBRATE commitment, BUILD raw result all absent from terminal line) |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward from R11 V-04 |

**V-01 Score**: 238 (base) + 7 (C-35) = **245 / 260**

---

### V-02 — Single Axis: Enriched Terminal Completion Line

**Structural profile**: No manifest. Opens with `CONTAINER: DESIGN` directly. CLOSE COMPLETE restructured as a six-field cross-container audit record: `[DESIGN] hypothesis = "..."`, `[CALIBRATE] inertia competitor + B-00 + outperform threshold`, `[BUILD] prototype result + delta vs. B-00`, `[CLOSE] verdict + prototype conclusion + counter-evidence`.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | All essential criteria unchanged from R11 V-04 |
| C-06–C-08 | Recommended | PASS | All recommended unchanged |
| C-09–C-10, C-16–C-34 | Aspirational | PASS/PARTIAL | Carry-forward at R11 V-04 levels |
| **C-35** | Aspirational | **FAIL** | No document-level manifest precedes the containers; output opens directly with `CONTAINER: DESIGN` |
| **C-36** | Aspirational | **PASS** | CLOSE COMPLETE encodes full experimental chain: hypothesis from DESIGN, competitor + B-00 + threshold from CALIBRATE, raw result + delta from BUILD, verdict + conclusion + counter-evidence from CLOSE — a reader scanning only the terminal line can verify the full arc; prerequisite C-22 and C-05 both satisfied |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**V-02 Score**: 238 (base) + 7 (C-36) = **245 / 260**

---

### V-03 — Gap-Signal Probe: Chain-Coherent Completion Lines

**Structural profile**: No manifest. No C-36 enrichment. Instead each intermediate COMPLETE line carries a forward-reference to the next container's principal input: DESIGN COMPLETE → "CALIBRATE receives: hypothesis text and measurement metric"; CALIBRATE COMPLETE → "BUILD receives: B-00 value and Phase 3 metric"; BUILD COMPLETE → "CLOSE receives: raw result and B-00 for three-column comparison". CLOSE COMPLETE retains R11 V-04 format.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | All essential criteria unchanged |
| C-06–C-08 | Recommended | PASS | All recommended unchanged |
| C-22 | Aspirational | PASS | Completion lines now carry forward-references in addition to backward result values — C-22 passes (substantive values present); forward-reference is additive content, not a gap in value encoding |
| C-09–C-10, C-16–C-34 | Aspirational | PASS/PARTIAL | Carry-forward at R11 V-04 levels |
| **C-35** | Aspirational | **FAIL** | No document-level manifest; forward-references on completion lines are per-container, not a pre-container enumeration of all containers |
| **C-36** | Aspirational | **FAIL** | CLOSE COMPLETE carries verdict + B-00 delta + table-population status only; no cross-container result chain |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**GAP SIGNAL**: The forward-reference pattern — each completion line explicitly acknowledges the downstream container's input requirement — creates a structural surface not scored by any current criterion. C-22 scores whether a line encodes its own results; no criterion scores whether a completion line encodes what the next container depends on receiving. This "chain-coherent handoff acknowledgment" probes a v13 candidate criterion: *Intermediate completion lines name the downstream container's input dependency, creating a verifiable handoff chain between containers.*

**V-03 Score**: 238 (base) + 0 (C-35 FAIL, C-36 FAIL) = **238 / 260** ← gap signal only

---

### V-04 — Combined: C-35 + C-36 (R12 Seed)

**Structural profile**: Both axes simultaneously on R11 V-04 base. `## Output Contract` manifest table precedes all containers. CLOSE COMPLETE is the full-chain six-field audit record from V-02. All R11 V-04 criteria preserved — CALIBRATE header entry contract (C-33), competitor-labeled baseline column (C-34) — both intact.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | All essential criteria unchanged |
| C-06–C-08 | Recommended | PASS | All recommended unchanged |
| C-09–C-10, C-16–C-28 | Aspirational | PASS/PARTIAL | Carry-forward; C-24–C-28 retain 8-pt gap |
| C-29–C-34 | Aspirational | PASS | Inertia competitor in CALIBRATE body; three-column table; pre-build baseline; CALIBRATE COMPLETE triple; CALIBRATE entry contract; competitor-labeled baseline column — all present |
| **C-35** | Aspirational | **PASS** | Manifest precedes CONTAINER: DESIGN; names all four containers with phases, principal purpose, expected output; C-22 prerequisite satisfied |
| **C-36** | Aspirational | **PASS** | CLOSE COMPLETE encodes full chain: `[DESIGN] hypothesis = "..."`, `[CALIBRATE] competitor + B-00 + threshold`, `[BUILD] result + delta`, `[CLOSE] verdict + conclusion + counter-evidence`; prerequisites C-22 and C-05 both satisfied |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**Compatibility check — C-33 vs C-35**: C-35 fires at document level (precedes all containers); C-33 fires at CALIBRATE container level (the header enumerates three pre-build responsibilities). Both present in V-04 — they do not interfere. C-35 is the document-level analogue of C-33; neither satisfies the other; both can coexist. ✓

**V-04 Score**: 238 (base) + 7 (C-35) + 7 (C-36) = **252 / 260**

---

### V-05 — Combined + Gap Probe: Checkable Manifest with Manifest Conformance

**Structural profile**: V-04 base, but manifest adds "Expected output (verifiable at COMPLETE line)" column with specific checkable values per container. CLOSE COMPLETE encodes both the full result chain (C-36 content) AND an explicit "manifest conformance:" record: `manifest conformance: DESIGN [FULL|PARTIAL], CALIBRATE [FULL|PARTIAL], BUILD [FULL|PARTIAL], CLOSE [FULL|PARTIAL — [item] not delivered]`.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | Unchanged |
| C-06–C-08 | Recommended | PASS | Unchanged |
| C-09–C-10, C-16–C-28 | Aspirational | PASS/PARTIAL | Carry-forward; C-24–C-28 gap persists |
| C-29–C-34 | Aspirational | PASS | All inertia/table criteria intact |
| **C-35** | Aspirational | **PASS** | Manifest precedes all containers AND includes "Expected output (verifiable at COMPLETE line)" column — passes C-35 more robustly; the verifiable annotation enriches the manifest but the pass condition (manifest precedes all containers, names each with purpose and expected output) was already satisfied by V-04's manifest |
| **C-36** | Aspirational | **PASS** | CLOSE COMPLETE encodes full result chain (identical to V-02/V-04 structure) — criterion satisfied; the manifest-conformance field is additive content beyond C-36's requirement |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**GAP SIGNALS (two structural surfaces not yet scored)**:

1. **Checkable manifest rows**: Each manifest row's "Expected output" column specifies verifiable values (e.g., "Hypothesis text, count of validated exclusions, success threshold value, failure threshold value") that a reader can cross-check against the CONTAINER: DESIGN COMPLETE line. C-35 only requires that the manifest exist and name each container's purpose and expected output — it does not require the expected output to be stated in terms that link to specific COMPLETE line fields. V-05's formulation creates a *verifiable promise structure* one level of specificity above C-35. Gap probe: does a criterion exist for "manifest rows are stated in terms verifiable against the corresponding COMPLETE line's encoded values"? Currently unscored.

2. **Manifest conformance record in CLOSE COMPLETE**: The `manifest conformance: DESIGN [FULL|PARTIAL]...` field in CLOSE COMPLETE is a second terminal audit act distinct from the result chain. C-36 requires the terminal line to encode the cross-container result chain; it does not require the terminal line to cross-verify the document-level manifest. V-05 adds this as a second field in the terminal line. Gap probe: does a criterion exist for "CLOSE COMPLETE explicitly cross-verifies the document-level manifest by container"? Currently unscored — v13 C-37 candidate.

**V-05 Score**: 238 (base) + 7 (C-35) + 7 (C-36) = **252 / 260** + two unscored gap surfaces

---

## Variation Rankings

| Rank | Variation | C-35 | C-36 | Score | Gap signals |
|------|-----------|------|------|-------|-------------|
| 1 (tie) | **V-04** | PASS | PASS | **252** | None |
| 1 (tie) | **V-05** | PASS | PASS | **252** | 2 (checkable manifest rows; manifest conformance at CLOSE) |
| 3 (tie) | V-01 | PASS | FAIL | **245** | None |
| 3 (tie) | V-02 | FAIL | PASS | **245** | None |
| 5 | V-03 | FAIL | FAIL | **238** | 1 (chain-coherent handoff lines) |

---

## Excellence Signals (from V-05, top-scoring gap probe)

**V-04 achieves the R12 target** (252 = 238 + C-35 + C-36) with no degradation to C-33, C-34, C-32, C-31, or C-30.

**V-05 adds two structural surfaces beyond V-04**:

**Pattern 1 — Manifest rows annotated as verifiable at COMPLETE lines**: V-05 states each manifest row's expected output in terms directly cross-referenceable against that container's COMPLETE line (e.g., CALIBRATE row: "Inertia competitor name, B-00 numeric value, outperform threshold direction and condition" — matching exactly the fields the CALIBRATE COMPLETE line encodes). This creates a per-container checkable promise that C-35 does not require. A manifest that lists "Expected output: Named inertia competitor, committed B-00 value, explicit outperform threshold" is a stronger structural claim than one that says "Expected output: Pre-build baseline committed." The difference is specificity: V-05's manifest rows can be mechanically verified by scanning the COMPLETE lines; V-04's rows describe output intent but not at the field level. This is a structural gap above C-35.

**Pattern 2 — CLOSE COMPLETE encodes manifest conformance per container as a second terminal audit field**: V-05's terminal line carries two independent audit records: (1) the full experimental result chain [C-36] and (2) an explicit manifest conformance record per container. These are structurally separate acts — the first reconstructs what happened; the second verifies that what was promised was delivered. C-36 scores the result chain; no criterion scores the promise-verification act. V-05 probes whether "CLOSE COMPLETE cross-verifies the document-level manifest by container" is a distinct scorable surface. If codified as C-37, the ceiling moves from 260 → ~267.

---

## R12 Seed Confirmed

V-04 is the clean seed: C-35 + C-36 both fire, all R11 V-04 criteria preserved, score = 252 / 260. V-05 reaches the same 252 and reveals two gap surfaces that are v13 candidates.

**Remaining 8 points** to ceiling: C-24 through C-28 carry-forward criteria (pass conditions not fully specified in v12 rubric).

---

```json
{"top_score": 252, "all_essential_pass": true, "new_patterns": ["Manifest rows annotated with verifiable expected-output fields linked to each container's COMPLETE line — creates per-container checkable promises one specificity level above C-35", "CLOSE COMPLETE encodes explicit manifest conformance record per container as a second terminal audit field distinct from the result chain — probes C-37 surface: terminal line cross-verifies document-level manifest"]}
```
