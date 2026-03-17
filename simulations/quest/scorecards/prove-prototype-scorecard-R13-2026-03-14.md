## Round 13 Scorecard — prove-prototype (v12 rubric, 260 pts)

**Date**: 2026-03-15
**Base**: R12 V-04 = 252 pts
**Remaining gap**: 8 pts — C-24-C-28 carry-forward (C-25 partial ~2 pts, C-26 full fail ~6 pts)
**R13 targets**: C-25 (role orthogonality via CLOSE split) + C-26 (explicit delta token in results-phase completion lines)

---

## Scoring Method

All five variations share the R12 V-04 base (252 pts). All criteria C-01 through C-24, C-27 through C-36 carry forward at R12 V-04 levels. The differentiating evaluation is C-25 and C-26 — the two outstanding gap criteria. C-24, C-27, C-28 are PASS in all variations (unchanged). C-25 and C-26 are assessed per-variation.

**Point allocation note**: C-24–C-28 together account for 34 pts ceiling (C-24=7, C-25=7, C-26=6, C-27=7, C-28=7). The 8-pt gap is the deficit below that ceiling. Decomposition: C-25 contributes ~2 pts to the gap (PARTIAL in base — BUILD's BUILDER+RECORDER already provides one non-coincident container, giving partial orthogonality credit; CLOSE's single ANALYST provides no orthogonality); C-26 contributes ~6 pts to the gap (FAIL in base — BUILD COMPLETE juxtaposes raw result and B-00 but carries no explicit labeled delta comparison; PHASE 7 COMPLETE says "delta rationale co-located" but embeds no delta value in the completion line itself).

---

## Per-Variation Evaluation

### V-01 — Single Axis: Role-Sequence (CLOSE Split)

**What changed from base**: CLOSE container declares ANALYST-EVALUATOR (Phases 7-8: verdict formation) and ANALYST-AUDITOR (Phases 9-11: experiment closure). Container/role coincidence broken for CLOSE in addition to existing BUILD.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | Unchanged from base |
| C-06–C-08 | Recommended | PASS | Unchanged |
| C-09, C-10, C-16–C-23 | Aspirational | PASS | Unchanged |
| C-24 | Aspirational | PASS | Four named lifecycle containers present, each enclosing only its stage's phases |
| **C-25** | Aspirational | **PASS** | CLOSE: ANALYST-EVALUATOR spans Phases 7-8; ANALYST-AUDITOR spans Phases 9-11 — container boundary (7-11) ≠ role boundary (7-8 / 9-11). Combined with BUILD's BUILDER+RECORDER split: 2 of 4 containers now demonstrate non-coincident annotation layers. Container count (4) ≠ role count (6); a container scan and a role-label scan produce different findings across the document. Prerequisite C-23 and C-24 satisfied. |
| C-26 | Aspirational | FAIL | BUILD COMPLETE: `raw result = [value]; B-00 = [value] for "[inertia competitor]"` — values juxtaposed, no labeled delta field. PHASE 7 COMPLETE: `delta rationale co-located` — body rationale noted but no explicit `delta vs. B-00 = [magnitude]` token embedded in the completion line. |
| C-27 | Aspirational | PASS | All completion lines carry `[FULL|PARTIAL]` grade tokens (unchanged) |
| C-28 | Aspirational | PASS | CALIBRATE is exclusively pre-build (unchanged) |
| C-29–C-34 | Aspirational | PASS | All inertia/table/entry-contract criteria unchanged |
| C-35 | Aspirational | PASS | `## Output Contract` manifest table precedes CONTAINER: DESIGN; names all four containers with phases, principal purpose, expected output |
| C-36 | Aspirational | PASS | CLOSE COMPLETE encodes full experimental chain: `[DESIGN] hypothesis`, `[CALIBRATE] competitor + B-00 + threshold`, `[BUILD] result + delta`, `[CLOSE] verdict + conclusion + counter-evidence` |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**V-01 Score**: 252 (base) + 2 (C-25 gap unlocked) = **254 / 260**

---

### V-02 — Single Axis: Output Format (Explicit Delta Token)

**What changed from base**: BUILD COMPLETE adds `delta vs. B-00 = [direction and magnitude — observed [above|below|at] B-00 by [amount]]`. PHASE 7 COMPLETE adds `delta vs. B-00 = [direction and magnitude]` as explicit labeled inline field. CLOSE single ANALYST role unchanged.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | Unchanged |
| C-06–C-08 | Recommended | PASS | Unchanged |
| C-09, C-10, C-16–C-23 | Aspirational | PASS | Unchanged |
| C-24 | Aspirational | PASS | Unchanged |
| C-25 | Aspirational | FAIL | CLOSE retains single ANALYST spanning Phases 7-11 — container and role boundaries coincide for CLOSE, DESIGN, and CALIBRATE. BUILD's 2-role split provides partial credit but full coincidence across 3/4 containers remains. C-25 requires both annotation layers to operate at different granularities throughout the document structure; 3 of 4 containers being coincident does not satisfy the pass condition. |
| **C-26** | Aspirational | **PASS** | PHASE 7 COMPLETE: `three-column table populated (predicted [value], observed [value], baseline ([inertia competitor name]) [value]); delta vs. B-00 = [direction and magnitude]; delta rationale co-located` — explicit labeled comparison against the inertia baseline embedded in the results-phase completion line. BUILD COMPLETE: `delta vs. B-00 = [direction and magnitude — observed [above|below|at] B-00 by [amount]]` — explicit baseline comparison in measurement-phase completion line. Both satisfy C-26's requirement that at least one results/evaluation-phase completion line carry an explicit comparison against the stated inertia baseline. |
| C-27 | Aspirational | PASS | `[FULL|PARTIAL]` grade tokens present in all completion lines (unchanged) |
| C-28–C-34 | Aspirational | PASS | Unchanged |
| C-35 | Aspirational | PASS | Manifest precedes all containers (unchanged) |
| C-36 | Aspirational | PASS | CLOSE COMPLETE full-chain format identical to base |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**V-02 Score**: 252 (base) + 6 (C-26 fully unlocked) = **258 / 260**

---

### V-03 — Single Axis: Lifecycle Emphasis (Chain-Coherent Handoff — Gap Probe)

**What changed from base**: DESIGN COMPLETE adds `→ CALIBRATE receives: hypothesis = "[text]", success threshold = [value], failure threshold = [value], Phase 3 metric = "[metric]"`. CALIBRATE COMPLETE adds `→ BUILD receives: inertia competitor = "[name]", B-00 = [value], Phase 3 metric = "[metric name]"`. BUILD COMPLETE adds `→ CLOSE receives: raw result = [value], B-00 = [value], inertia competitor = "[name]" for three-column comparison`. No role changes, no delta tokens, no manifest changes.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | Unchanged |
| C-06–C-08 | Recommended | PASS | Unchanged |
| C-24 | Aspirational | PASS | Unchanged |
| C-25 | Aspirational | FAIL | CLOSE retains single ANALYST — same as base; forward-reference fields do not affect container/role annotation granularity |
| C-26 | Aspirational | FAIL | PHASE 7 COMPLETE: `delta rationale co-located` (same as base, no explicit delta token in completion line). BUILD COMPLETE: `raw result = [value]; B-00 = [value] for "[inertia competitor]"` — forward-reference field added but no labeled delta comparison |
| C-27 | Aspirational | PASS | Unchanged |
| C-28–C-36 | Aspirational | PASS | All unchanged from base |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**GAP SIGNAL CONFIRMED**: `→ [NEXT] receives:` forward-reference fields on intermediate COMPLETE lines create a handoff-chain verification surface not scored by any v12 criterion. C-22 scores whether a line encodes its own phase results (backward-looking); no criterion scores whether a completion line commits the downstream container's input dependency (forward-looking). Confirms R12 V-03 gap signal. No new surface beyond R12 identification.

**V-03 Score**: 252 (base) + 0 = **252 / 260**

---

### V-04 — Combined: Role-Sequence + Output Format (R13 Seed)

**What changed from base**: CLOSE split into ANALYST-EVALUATOR (Phases 7-8) + ANALYST-AUDITOR (Phases 9-11) **and** BUILD COMPLETE / PHASE 7 COMPLETE carry explicit delta-vs-B-00 labeled tokens — both axes from V-01 and V-02 simultaneously.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | Unchanged |
| C-06–C-08 | Recommended | PASS | Unchanged |
| C-09, C-10, C-16–C-23 | Aspirational | PASS | Unchanged |
| C-24 | Aspirational | PASS | Unchanged |
| **C-25** | Aspirational | **PASS** | CLOSE: ANALYST-EVALUATOR (7-8) + ANALYST-AUDITOR (9-11). BUILD: BUILDER (5) + RECORDER (6). Two containers with structurally non-coincident role/container boundaries; 6 roles across 4 containers; no exact lifecycle-boundary/role-boundary coincidence at the document level. Both annotation layers operate at demonstrably different granularities. |
| **C-26** | Aspirational | **PASS** | PHASE 7 COMPLETE: explicit `delta vs. B-00 = [direction and magnitude]` field. BUILD COMPLETE: explicit `delta vs. B-00 = [direction and magnitude — observed [above|below|at] B-00 by [amount]]`. Two results/measurement-phase completion lines carry labeled baseline comparisons. |
| C-27–C-34 | Aspirational | PASS | Unchanged; no degradation to C-33 (CALIBRATE entry contract), C-34 (competitor-labeled baseline column), C-32 (CALIBRATE COMPLETE triple), C-31 (FRAMER prohibition) |
| C-35 | Aspirational | PASS | `## Output Contract` manifest precedes all containers; four rows naming container, phases, principal purpose, expected output |
| C-36 | Aspirational | PASS | CLOSE COMPLETE full-chain: `[DESIGN]…[CALIBRATE]…[BUILD]…[CLOSE]` spanning all four containers |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**Compatibility check**: C-25 (ANALYST-EVALUATOR/AUDITOR split) and C-26 (delta token in PHASE 7/BUILD COMPLETE) are structurally independent. C-35 and C-36 unaffected. C-33 (CALIBRATE header entry contract) unaffected — three-responsibility enumeration still present. ✓

**V-04 Score**: 252 (base) + 2 (C-25) + 6 (C-26) = **260 / 260 — CEILING REACHED**

---

### V-05 — Combined + Gap Probe: V-04 Base + Checkable Manifest + Terminal Manifest Conformance

**What changed from V-04**: (1) Manifest column header changes to "Expected output (verifiable at COMPLETE line)" with field-level specificity per row (DESIGN row: "Hypothesis text (quoted), count of validated exclusions, success threshold value, failure threshold value"; CALIBRATE row: "Inertia competitor name, B-00 numeric value, outperform threshold direction and condition"; BUILD row: "raw result numeric value, delta vs. B-00 direction and magnitude"; CLOSE row: "three-column table…verdict word…"). (2) CONTAINER: DESIGN COMPLETE format restructured to encode named fields: `hypothesis = "[text]", scope = [N] validated exclusions, success threshold = [threshold], failure threshold = [threshold]` — matching the manifest row's field specification exactly. (3) CLOSE COMPLETE adds `manifest conformance: DESIGN [FULL|PARTIAL], CALIBRATE [FULL|PARTIAL], BUILD [FULL|PARTIAL], CLOSE [FULL|PARTIAL]` as a second terminal audit field after the C-36 result chain.

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01–C-05 | Essential | PASS | Unchanged |
| C-06–C-08 | Recommended | PASS | Unchanged |
| C-09, C-10, C-16–C-23 | Aspirational | PASS | Unchanged |
| C-24 | Aspirational | PASS | Unchanged |
| **C-25** | Aspirational | **PASS** | CLOSE split identical to V-04 — ANALYST-EVALUATOR + ANALYST-AUDITOR |
| **C-26** | Aspirational | **PASS** | Delta tokens identical to V-04 — PHASE 7 COMPLETE and BUILD COMPLETE both carry explicit comparison |
| C-27–C-34 | Aspirational | PASS | Unchanged; no degradation |
| **C-35** | Aspirational | **PASS** | Manifest appears before all containers; column header "Expected output (verifiable at COMPLETE line)" makes the entry contract more precisely specified but the C-35 pass condition (manifest names every container with purpose and expected output) was already satisfied by V-04's manifest. The verifiable column annotation enriches C-35 satisfaction but does not change the PASS verdict. |
| **C-36** | Aspirational | **PASS** | CLOSE COMPLETE result chain is identical to V-04 — `[DESIGN] hypothesis`, `[CALIBRATE] competitor + B-00 + threshold`, `[BUILD] result + delta`, `[CLOSE] verdict + conclusion + counter-evidence`. The `manifest conformance:` field is additive content beyond C-36's requirement; C-36 is satisfied by the result chain alone. |
| C-11–C-15 | Excellence | PARTIAL | Carry-forward |

**GAP SIGNALS (two structural surfaces not scored by v12)**:

**Gap 1 — Per-container manifest-to-completion field alignment**: V-05's DESIGN COMPLETE encodes `hypothesis = "[text]"`, `scope = [N] validated exclusions`, `success threshold = [threshold]`, `failure threshold = [threshold]` — exactly the four fields listed in the manifest DESIGN row. A reader can cross-check DESIGN COMPLETE against the manifest DESIGN row field by field without reading the container body. C-35 requires only that the manifest name containers with purpose and expected output; it does not require the COMPLETE line to encode the same fields the manifest promised. V-05 closes this gap. Probes a C-37 candidate: *each CONTAINER COMPLETE line encodes fields that mirror the manifest row's expected output specification*.

**Gap 2 — Manifest conformance record in CLOSE COMPLETE**: The `manifest conformance: DESIGN [FULL|PARTIAL], CALIBRATE [FULL|PARTIAL], BUILD [FULL|PARTIAL], CLOSE [FULL|PARTIAL]` field is a second terminal audit act — it assesses whether each container delivered its manifest promise. C-36 records *what happened* (experimental result chain); the conformance field records *whether each container did what it promised*. These are structurally independent audit acts. No v12 criterion scores the promise-delivery verification. Probes C-38 candidate: *CLOSE COMPLETE cross-verifies the document-level manifest per container*.

**V-05 Score**: 252 (base) + 2 (C-25) + 6 (C-26) = **260 / 260** + 2 unscored gap surfaces

---

## Variation Rankings

| Rank | Variation | C-25 | C-26 | Score | Notes |
|------|-----------|------|------|-------|-------|
| 1 (tie) | **V-04** | PASS | PASS | **260** | Clean seed: ceiling reached, no gap probes |
| 1 (tie) | **V-05** | PASS | PASS | **260** | Ceiling + 2 gap surfaces (field-aligned COMPLETE lines; manifest conformance record) |
| 3 | V-02 | FAIL | PASS | **258** | Larger single-axis gain; delta token addresses the 6-pt majority of the gap |
| 4 | V-01 | PASS | FAIL | **254** | Smaller single-axis gain; C-25 was partially credited in base via BUILD's 2-role structure |
| 5 | V-03 | FAIL | FAIL | **252** | Gap probe only; confirms R12 handoff-chain signal |

---

## Excellence Signals

**V-04 achieves the R13 target**: 260 = 252 + 8, with no degradation to C-33 through C-36, C-32, C-31, C-30, or C-29. The combination of ANALYST-EVALUATOR/ANALYST-AUDITOR in CLOSE plus explicit delta tokens in PHASE 7 COMPLETE and BUILD COMPLETE is structurally compatible with the full v12 stack.

**V-05 adds two new structural surfaces for v14 consideration**:

**Pattern 1 — Manifest row fields specified in terms matching COMPLETE line field names**: The manifest DESIGN row promises "Hypothesis text (quoted), count of validated exclusions, success threshold value, failure threshold value" — and the DESIGN COMPLETE line encodes `hypothesis = "[text]", scope = [N] validated exclusions, success threshold = [threshold], failure threshold = [threshold]`. The four manifest field names and four COMPLETE line fields align one-to-one. This creates a per-container entry/exit bracket where the manifest's entry promise is mechanically verifiable against the COMPLETE exit record. C-35 makes the manifest scorable; this pattern makes the *connection between manifest and COMPLETE* scorable — a structural surface above C-35.

**Pattern 2 — CLOSE COMPLETE carries two independent terminal audit acts**: the C-36 result chain records what happened experimentally; the manifest conformance field records whether each container delivered its manifest promise. These answer different audit questions. The ceiling beyond 260 depends on whether C-37 (field-aligned COMPLETE lines) and C-38 (manifest conformance in terminal line) are confirmed as independent scorable surfaces in v14.

---

```json
{"top_score": 260, "all_essential_pass": true, "new_patterns": ["Per-container CONTAINER COMPLETE line encodes fields that exactly match the manifest row's expected output specification by name (DESIGN COMPLETE: hypothesis text, exclusion count, success threshold, failure threshold = the four fields promised in the manifest DESIGN row) — creates a mechanical verifiability bracket between manifest entry promise and COMPLETE exit record, one specificity level above C-35", "CLOSE COMPLETE carries manifest conformance as a second terminal audit field independent of the C-36 result chain — per-container FULL/PARTIAL assessment (DESIGN/CALIBRATE/BUILD/CLOSE) confirming whether each container delivered its manifest-promised output; C-36 records what happened, conformance field records whether what was promised was delivered — probes C-37/C-38 candidates"]}
```
