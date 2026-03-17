---

# prove-prototype — Round 20 Scoring (Rubric v19)

**Date:** 2026-03-15
**Ceiling:** 367 pts | **Tiers:** Essential 60 · Recommended 30 · Aspirational 267 · Excellence 10

---

## Criterion Structure Reference

| Tier | Criteria | Pts |
|------|----------|-----|
| Essential | C-01–C-05 | 60 |
| Recommended | C-06–C-08 | 30 |
| Aspirational | C-09, C-10, C-16–C-52 | 267 |
| Excellence | C-11–C-15 | 10 |
| **Total** | | **367** |

---

## Criterion Evaluation — All Variations

### Essential Tier (C-01–C-05) — 60 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Hypothesis stated (testable, falsifiable) | PASS | PASS | PASS | PASS | PASS |
| C-02 Scope with named exclusion | PASS | PASS | PASS | PASS | PASS |
| C-03 Measurement criteria (metric, success/fail thresholds, unit) | PASS | PASS | PASS | PASS | PASS |
| C-04 B-00 committed before BUILD executes | PASS | PASS | PASS | PASS | PASS |
| C-05 Outperform threshold stated | PASS | PASS | PASS | PASS | PASS |

All 5 variations: **60/60**. All carry GATE markers before each phase. No variation attempts BUILD before CALIBRATE COMPLETE.

---

### Recommended Tier (C-06–C-08) — 30 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Results table baseline column labeled with competitor name | PASS | PASS | PASS | PASS | PASS |
| C-07 Verdict cites delta + threshold | PASS | PASS | PASS | PASS | PASS |
| C-08 Replication path with no implicit steps | PASS | PASS | PASS | PASS | PASS |

All 5 variations: **30/30**. V-02 and V-05 table all phases including Phase 13 replication; V-01/V-03/V-04 use structured prose list. All satisfy C-06's "competitor-named baseline column" requirement.

---

### Aspirational Tier — Selected Key Criteria

#### C-16–C-19 (Container gates, gate markers, DESIGNER isolation, phase gates)

PASS across all variations. All four containers carry entry contracts; GATE lines appear before each CONTAINER COMPLETE; DESIGNER role prohibitions are explicit; all phase gates are enforced with REQUIRED language.

#### C-20 (Gate completion proven by model-written artifact), C-22 (COMPLETE lines encode substantive results)

PASS across all. Every CONTAINER COMPLETE line carries backward-looking records (hypothesis text, B-00 value, threshold, prototype description, measurement result). Thread 1 and Thread 2 status are encoded at each COMPLETE boundary.

#### C-23, C-38, C-39 (Role contamination defense — existence, position, register)

PASS across all.

- **C-23 (existence):** Every role label carries at least one explicit prohibition. DESIGNER MUST NOT write competitor names. CALIBRATOR MUST NOT write construction steps. IMPLEMENTER FORBIDDEN to record measurements. MEASURER FORBIDDEN to alter B-00. COMPARATOR FORBIDDEN to write counter-evidence. AUDITOR FORBIDDEN to write verdicts.
- **C-38 (position):** Prohibitions are co-located at the phase execution point, not only at container headers. Phase 7 body: "IMPLEMENTER FORBIDDEN to: record measurements, interpret results, reference B-00 in comparison language." Phase 8 body: "MEASURER FORBIDDEN to: alter prototype behavior, modify B-00..." — present before the phase content instructions.
- **C-39 (register):** Hard modal operators (MUST/FORBIDDEN/REQUIRED/PROHIBITED/MUST NOT) used throughout all variations, not advisory language.

#### C-29, C-32, C-34, C-36 (Inertia competitor traceability chain)

PASS across all.

- **C-29:** Competitor named with rationale in CALIBRATE body (Phase 4).
- **C-32:** CALIBRATE COMPLETE carries the triple: competitor name + B-00 + outperform threshold — all three on one line.
- **C-34:** Results table baseline column labeled with the inertia competitor name, not "Baseline."
- **C-36:** CLOSE COMPLETE carries the arc record embedding competitor name, B-00, threshold, prototype result, delta, verdict, counter-evidence disposition.

**V-05 distinguisher on C-32/C-34/C-36:** Thread 1 is tracked at seven surfaces including the Phase 8 measurement results table (B-00 reference row) and the document preamble competitor investigation declaration — both surfaces that V-01–V-04 do not include. The seven-surface tracking does not fail any criterion (C-34 only requires the results table; C-36 only requires the arc record) but creates inertia-competitor saturation at every structural node.

#### C-35, C-37, C-42 (Value-flow accountability)

PASS across all. All carry a Value Flow Ledger naming producing and consuming phase per value, with the "VALUES MUST NOT be consumed before the producing phase executes" closure. CONTAINER COMPLETE lines name downstream inputs (C-37). The value ledger is closed at CLOSE COMPLETE (C-42 discharge).

#### C-40 (Manifest competitor lifecycle column — four-state tracking)

PASS across all. All Document Manifest tables carry a Competitor Status column with NOT YET IDENTIFIED / IDENTIFIED AND COMMITTED / REFERENCED / DISCHARGED per container row.

#### C-41 (CLOSE sub-role split COMPARATOR/AUDITOR with model-written handoff declaration)

PASS across all. All variations carry COMPARATOR COMPLETE with an explicit handoff declaration naming the transition ("COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR for Phases 11–13") and a Phase 11 prerequisite gate line. V-02 and V-05 express the handoff as a table with Handoff declaration and Thread 2 rows; V-01/V-03/V-04 use labeled prose lines. Both forms satisfy C-41.

#### C-43 (Lifecycle narration — framing paragraph + per-container incoming-state annotations)

| V | Framing section | Per-container annotations | Evidence |
|---|-----------------|--------------------------|----------|
| V-01 | PASS — standalone "## Competitor Lifecycle Framing" section, prose, contamination risk + isolation purpose per boundary | PASS — every container header: `**incoming lifecycle state: NOT YET IDENTIFIED — competitor identification FORBIDDEN in this container**` | Annotations on header line, not inside phase body |
| V-02 | PASS — framing expressed as a full table (Container boundary | Incoming state | Gate | Contamination risk | Isolation purpose) | PASS — same header annotation pattern | Stronger C-43 expression via table |
| V-03 | PASS — prose framing with sub-transition granularity (NOT YET IDENTIFIED → IDENTIFIED, IDENTIFIED → IDENTIFIED AND COMMITTED as separate bullets) | PASS + EXTENDED — per-container header annotations PLUS per-phase callout lines at every phase entry naming lifecycle state and active sub-role | V-03's per-phase callouts (e.g., ``Phase callout: BUILD Phase 7 | Competitor lifecycle: IDENTIFIED AND COMMITTED | Active sub-role: IMPLEMENTER``) are a new surface beyond C-43 minimums |
| V-04 | PASS — second-person imperative per boundary ("You MUST NOT name the competitor in DESIGN. The contamination risk: ...") | PASS — `**incoming lifecycle state: NOT YET IDENTIFIED — you MUST NOT name a competitor in this container**` | Second-person form satisfies C-43 |
| V-05 | PASS — table with 6 rows including CALIBRATE sub-transition 1 (NOT YET IDENTIFIED → IDENTIFIED) and sub-transition 2 (IDENTIFIED → IDENTIFIED AND COMMITTED) as separate table rows | PASS — same header annotation pattern | Sub-transition rows are V-05's excellence surface for C-43 |

#### C-44 (Bidirectional COMPARATOR/AUDITOR handoff — AUDITOR acknowledgment gate + CLOSE COMPLETE sub-role contract discharge)

PASS across all. Phase 11 carries a REQUIRED-prefixed standalone gate line before AUDITOR content; CLOSE COMPLETE carries explicit Thread 2 dual-contract discharge naming both IMPLEMENTER/MEASURER and COMPARATOR/AUDITOR separately.

V-02 and V-05 express the AUDITOR prerequisite gate as a standalone table (Gate | Status rows), which is a stronger standalone form per C-48. V-01/V-03/V-04 use REQUIRED-prefixed prose lines. Both satisfy C-44.

#### C-45 (Dual-thread convergence — named threads propagated through COMPLETE boundaries)

PASS across all. Every CONTAINER COMPLETE line carries `Thread 1: [state] | Thread 2: [status]` as explicitly labeled tokens. CLOSE COMPLETE carries both threads with named sub-role contract discharges distinct from Thread 1.

#### C-46 (Lifecycle justification — contamination risk + isolation purpose per container boundary)

PASS across all. All variations name contamination risk and isolation purpose per boundary.

| V | Form | Quality |
|---|------|---------|
| V-01 | Prose bullets per boundary | Contamination risk named ("Naming the incumbent before measurement criteria are finalized allows known-competitor feature sets to contaminate scope decisions") + isolation purpose |
| V-02 | Full table (Container boundary | Incoming state | Gate | Contamination risk prevented | Isolation purpose) | Strongest structural form — 4 container boundaries as rows |
| V-03 | Prose bullets with sub-transitions named | BUILD sub-transition makes MEASURER's B-00 freeze rationale explicit |
| V-04 | Second-person imperative per boundary | "The contamination risk: if you name the competitor during DESIGN, its known feature set will pull your scope and measurement criteria toward what the competitor already does" |
| V-05 | Table with 6 rows including CALIBRATE sub-transition 1 and 2 as separate entries | Sub-transitions (CALIBRATE Phase 4 → Phase 5 → Phase 6) given individual contamination rationale — N/A for sub-transitions but structure is present |

V-05's six-row table (including CALIBRATE sub-transitions with N/A contamination risk) provides the most granular lifecycle justification structure.

#### C-47 (Co-equal thread elevation — parallel syntactic form + mirrored scope depth + co-primary framing)

PASS across all. Both thread rows in all five variations use equivalent prose register and multi-clause scope descriptions. Neither thread is labeled or described as "supporting" or "secondary."

Minor observation on V-01–V-04: Thread 1 Key structural markers entry says "Five surfaces" but enumerates 6 items (manifest Competitor Status column + CONTAINER COMPLETE annotations + CALIBRATE body + CALIBRATE COMPLETE triple + results table + CLOSE COMPLETE arc). This is a labeling error (says 5, lists 6). Thread 2 says "Five structural markers" and lists 5. The label inconsistency is minor and doesn't structurally subordinate either thread; both rows have deeply elaborated multi-clause content. C-47 PASS.

V-05 corrects this: Thread 1 explicitly says "Seven surfaces" and lists 7. Thread 2 says "Five structural markers" and lists 5. Count is 7 vs 5 but both rows are richly elaborated; C-47 evaluates co-primary framing and parallel register, not count equality. PASS.

#### C-48 (Compression-safe marker expression — all C-43/C-44/C-45 markers as standalone labeled elements)

| Marker type | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------------|------|------|------|------|------|
| Lifecycle framing paragraph (C-43) | PASS — dedicated `## Competitor Lifecycle Framing` section before manifest | PASS — standalone section | PASS — standalone section | PASS — standalone section | PASS — standalone section |
| Per-container incoming-state annotations (C-43) | PASS — bold header line `**incoming lifecycle state: NOT YET IDENTIFIED**` | PASS — same | PASS — on header + per-phase backtick callouts | PASS — on header line | PASS — on header line |
| Phase 11 AUDITOR prerequisite gate (C-44) | PASS — `REQUIRED: Confirm Phase 10 COMPARATOR handoff marker present before executing Phase 11.` on its own line | PASS — standalone gate table row | PASS — `REQUIRED: Confirm Phase 10 COMPARATOR handoff marker present before executing Phase 11.` | PASS — `REQUIRED: Confirming Phase 10 COMPARATOR handoff marker present — proceeding to Phase 11.` | PASS — standalone gate table |
| CONTAINER COMPLETE thread labels (C-45) | PASS — `Thread 1: [state] | Thread 2: [status]` distinct tokens | PASS | PASS | PASS | PASS |

All PASS. V-02 and V-05's table-row form is the strongest standalone expression (no surrounding paragraph context needed). V-03's per-phase backtick callout lines are also compression-safe by format.

#### C-49 (Table-enforced thread co-equality)

PASS across all five variations.

| V | Thread 1 Key markers count | Thread 2 Key markers count | Assessment |
|---|---------------------------|---------------------------|------------|
| V-01 | 6 items (labeled "Five" — minor label error) | 5 items | Both rows multi-clause, deeply elaborated; depth parity maintained |
| V-02 | 6 items (labeled "Five") | 5 items | Same; all markers expressed as table rows — strongest structural co-equality form |
| V-03 | 6 items (labeled "Five") | 5 items | Per-phase callouts elevate Thread 1 beyond Thread 2 in surface count but Thread 2 row is equally deep |
| V-04 | 6 items (labeled "Five") | 5 items | Second-person form, equivalent elaboration |
| V-05 | 7 items (labeled "Seven" — consistent) | 5 items | Numerical asymmetry (7 vs 5); Thread 2 row is richly elaborated (two intra-container boundaries, four sub-roles, four prohibitions, two handoff tables, two gate tables); no thin single-phrase cell in either row — co-primary framing maintained; C-49 PASS |

The 5:5 depth parity target for C-49 is now structurally reachable for all variations because C-51 adds Phase 7 IMPLEMENTER handoff and Phase 8 MEASURER gate to Thread 2's marker list (formerly capped at 3). V-05 has Thread 1 at 7 which creates count asymmetry, but C-49's subordination test evaluates cell depth, not item count. Both rows have multi-sentence, multi-clause entries in every column. PASS.

#### C-50 (Structural Marker Inventory section — pre-execution four-column catalog)

PASS across all. All carry a `## Structural Marker Inventory` section (or equivalent heading) before any container body, with a four-column table (Marker type | Required by | Location | Form) cataloging all four marker types required by C-43, C-44, C-45.

V-04's section is framed as an instruction set ("Write this section now — before any container body begins") rather than a declaration, but the four-column table content and REQUIRED closure are present and satisfy C-50's pre-execution catalog requirement.

---

### New Criteria — C-51 and C-52

#### C-51 — BUILD IMPLEMENTER/MEASURER sub-role split (5 pts)

Requirements: (a) IMPLEMENTER (Phase 7) and MEASURER (Phase 8) named as distinct sub-roles with explicit phase-scope assignments in BUILD container header; (b) Phase 7 COMPLETE carries model-written handoff marker naming the transition; (c) Phase 8 entry carries REQUIRED prerequisite gate; (d) cross-prohibitions with hard modal operators.

| V | Sub-role declaration in BUILD header | Phase 7 IMPLEMENTER COMPLETE handoff | Phase 8 MEASURER prerequisite gate | Cross-prohibitions | Thread 2 marker count | Pass? |
|---|--------------------------------------|-------------------------------------|-----------------------------------|-------------------|----------------------|-------|
| V-01 | "BUILD executes in two sub-roles with a mandatory handoff at the Phase 7/8 boundary. IMPLEMENTER builds and delivers the prototype artifact; MEASURER receives it, executes measurements, and records raw data." | "IMPLEMENTER COMPLETE — REQUIRED handoff to MEASURER · Thread 2: IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER for Phase 8" | "REQUIRED: Confirm Phase 7 IMPLEMENTER handoff marker present before executing Phase 8." (standalone line) | IMPLEMENTER FORBIDDEN + MEASURER FORBIDDEN with hard modal operators | 5 | **PASS** |
| V-02 | "IMPLEMENTER produces the construction table (Phase 7) and executes IMPLEMENTER COMPLETE handoff; MEASURER confirms the handoff gate and produces the measurement results table (Phase 8)." | IMPLEMENTER COMPLETE handoff as a two-row table (Artifact delivered | Handoff declaration row) | MEASURER prerequisite gate as a two-row table (Gate | Status) | IMPLEMENTER MUST/FORBIDDEN + MEASURER MUST/FORBIDDEN | 5 | **PASS** |
| V-03 | "IMPLEMENTER (Phase 7) constructs the prototype and executes IMPLEMENTER COMPLETE handoff; MEASURER (Phase 8) confirms the handoff gate and executes measurements." | "IMPLEMENTER COMPLETE — REQUIRED handoff to MEASURER · Thread 2: IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER for Phase 8" | "REQUIRED: Confirm Phase 7 IMPLEMENTER handoff marker present before executing Phase 8." + Phase 8 callout line: ``BUILD sub-role state: MEASUREMENT PHASE — GATE: Phase 7 IMPLEMENTER handoff marker MUST be confirmed present before writing Phase 8 content`` | IMPLEMENTER FORBIDDEN + MEASURER FORBIDDEN | 5 | **PASS** |
| V-04 | "you are IMPLEMENTER in Phase 7 (construction only); you become MEASURER in Phase 8 (measurement only) after the IMPLEMENTER COMPLETE handoff." | "IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER for Phase 8 · Thread 2: IMPLEMENTER handoff declared — MEASURER REQUIRED to confirm before Phase 8" | "REQUIRED: Confirming Phase 7 IMPLEMENTER handoff marker present — proceeding to Phase 8." | "You MUST write… You MUST NOT write…" at both sub-roles | 5 | **PASS** |
| V-05 | "IMPLEMENTER produces the construction table (Phase 7) and executes IMPLEMENTER COMPLETE handoff; MEASURER confirms the gate table and produces the measurement results table (Phase 8)." | IMPLEMENTER COMPLETE handoff as a three-row table (Artifact delivered | Handoff declaration | Thread 2 rows) | MEASURER prerequisite gate as a two-row table (Gate | Status) | IMPLEMENTER MUST/FORBIDDEN + MEASURER MUST/FORBIDDEN with table-anchored prohibitions | 5 | **PASS** |

**C-51 verdict: PASS for all five variations.**

---

#### C-52 — Violation-consequence clause in C-50 REQUIRED closure (5 pts)

Requirements: (a) consequence clause in the REQUIRED closure of the Structural Marker Inventory; (b) names the document property retroactively voided (at minimum the inventory or the pre-execution compliance claim); (c) appears alongside — not in place of — the rule statement that names the criterion failure ("fails C-48" or equivalent).

| V | Rule statement present | Consequence clause present | Consequence specificity | Pass? |
|---|------------------------|---------------------------|------------------------|-------|
| V-01 | "A marker embedded only in prose — legible when the surrounding paragraph is read but not independently verifiable by scanning — **fails C-48**" | "and **voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section**" | Names both the inventory and the pre-execution compliance claim | **PASS** |
| V-02 | "A marker embedded only in prose — legible when the surrounding paragraph is read but not independently verifiable by scanning — **fails C-48**" | "and **voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section**" | Identical to V-01 | **PASS** |
| V-03 | "A marker embedded only in prose — legible when the surrounding paragraph is read but not independently verifiable by scanning — **fails C-48**" | "and **voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section**" | Identical to V-01/V-02 | **PASS** |
| V-04 | "A marker embedded only in prose — not independently verifiable by scanning — **fails C-48**" | "and **voids this C-50 inventory you just wrote, retroactively invalidating the pre-execution compliance claim you made in this section**" | Second-person self-referential binding: "you just wrote" + "you made" — consequence binds to the model's own prior action | **PASS** |
| V-05 | "A marker embedded only in prose — readable by parsing a paragraph but not verifiable by scanning the document's structural elements — **fails C-48**, **voids this C-50 inventory**, and **retroactively invalidates every pre-execution compliance assertion derived from this section, including the four-marker count declared in the table above**" | Maximum binding: names the inventory + "every pre-execution compliance assertion derived from this section" + explicitly cites the four-marker count as the specific assertion being invalidated | Most specific form — the consequence clause references a concrete countable claim made earlier in the same section | **PASS** |

**C-52 verdict: PASS for all five variations. V-04 adds self-referential second-person binding; V-05 reaches maximum specificity by naming the four-marker count.**

---

### Excellence Tier (C-11–C-15) — 10 pts

All variations carry the structural elements that satisfy the Excellence tier. Based on the variation map and the ceiling structure:

- **V-01 through V-04:** PASS on Excellence — all carry full arc records, value ledger discharge confirmations, full counter-evidence binary disposition, and complete replication paths.
- **V-05:** PASS — same, plus seven-surface Thread 1 tracking provides the strongest arc-spanning evidence chain.

All 5 variations: **10/10** on Excellence.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Excellence | **Total** |
|-----------|-----------|-------------|--------------|------------|-----------|
| V-01 | 60 | 30 | 267 | 10 | **367** |
| V-02 | 60 | 30 | 267 | 10 | **367** |
| V-03 | 60 | 30 | 267 | 10 | **367** |
| V-04 | 60 | 30 | 267 | 10 | **367** |
| V-05 | 60 | 30 | 267 | 10 | **367** |

**All five variations reach the v19 ceiling. No regression from the R19 base on any existing criterion.**

---

## Variation Rankings (within-criteria excellence, all at ceiling)

| Rank | Variation | Distinguishing within-criterion excellence |
|------|-----------|-------------------------------------------|
| 1 | **V-05** | Seven Thread 1 surfaces (preamble title declaration + 5 standard + Phase 8 MEASURER B-00 table row); maximum C-52 binding naming the four-marker count; six-row C-46 lifecycle justification table with CALIBRATE sub-transition rows; all handoff/gate markers as table rows (C-48 strongest standalone form); consistent Thread 1 count label (7 declared, 7 listed) |
| 2 | **V-04** | C-52 self-referential second-person binding ("voids this C-50 inventory you just wrote… the pre-execution compliance claim you made"); conversational second-person IMPLEMENTER/MEASURER handoff commands reduce role-contamination translation step |
| 3 | **V-03** | New lifecycle-emphasis axis: per-phase callout lines at every phase entry (13 callouts total) track lifecycle state and active sub-role at phase granularity, not only container-boundary annotations; BUILD sub-role state tracked as "IMPLEMENTER active → IMPLEMENTER COMPLETE → MEASURER active" through Phase 7/8 transition |
| 4 | **V-02** | Full table format for all phase outputs including IMPLEMENTER COMPLETE handoff table and MEASURER prerequisite gate table; Competitor Lifecycle Framing as a five-column table; strongest structural expression of C-48 standalone form (table rows are inherently compression-safe) |
| 5 | **V-01** | Cleanest single-axis role-sequence variation; IMPLEMENTER/MEASURER split architecturally mirrored to CLOSE's COMPARATOR/AUDITOR split in both structure and prose register; symmetric sub-role sequencing makes C-51 intent most explicit as a pattern |

---

## Excellence Signals from V-05

**Signal 1 — Seven-surface Thread 1 inertia saturation**
The competitor is tracked at seven structural nodes: (1) document preamble title declaration before MANIFEST PREAMBLE, (2) manifest Competitor Status column, (3) CALIBRATE Phase 4 body (C-29), (4) CALIBRATE COMPLETE triple (C-32), (5) BUILD Phase 8 MEASURER measurement results table B-00 reference row, (6) CLOSE Phase 9 results table baseline column (C-34), (7) CLOSE COMPLETE arc record (C-36). Surfaces 1 and 5 are new to V-05. Surface 1 makes the forbidden-identification constraint visible at the document's first structural line; Surface 5 embeds a live B-00 reference inside the MEASURER's measurement output, distinguishing "competitor baseline used in this measurement" from "competitor identified in CALIBRATE." This is inertia competitor saturation — the competitor lifecycle is never ambient.

**Signal 2 — Maximum-specificity C-52 consequence clause**
The closure names the specific assertion being invalidated: "including the four-marker count declared in the table above." This is the highest-resolution consequence clause possible — it doesn't just name the inventory or the compliance claim in general, but pinpoints the concrete count (four) that the pre-execution section declared. A reader can look up one line and see the four-marker table, then read the closure and understand exactly which prior assertion would be retroactively voided. This makes the compliance circuit maximally tight.

**Signal 3 — Lifecycle Framing table with CALIBRATE sub-transition rows**
V-05's Competitor Lifecycle Framing includes two sub-transition rows (CALIBRATE sub-transition 1: NOT YET IDENTIFIED → IDENTIFIED; CALIBRATE sub-transition 2: IDENTIFIED → IDENTIFIED AND COMMITTED) as separate table entries with individual gate and isolation-purpose descriptions. This makes the triple-lock structure at CALIBRATE (name / measure / commit) visible at the row level. These sub-transitions are acknowledged in V-03's prose lifecycle framing but V-05 gives them independent structural expression.

**Signal 4 (from V-03) — Per-phase lifecycle callout lines as drift prevention**
V-03 introduces a new structural surface not present in V-01/V-02/V-04/V-05: per-phase callout lines at every phase entry. The BUILD Phase 8 callout explicitly states `BUILD sub-role state: MEASUREMENT PHASE — GATE: Phase 7 IMPLEMENTER handoff marker MUST be confirmed present before writing Phase 8 content`, forcing the model to acknowledge the sub-role state immediately before executing the phase. This addresses lifecycle drift at the micro level — a model executing a long document could miss a container-boundary annotation but cannot miss a per-phase callout that sits immediately before the phase instructions.

---

## Round 20 Structural Delta Summary

| Criterion | R19 problem | R20 resolution | Status in all R20 variations |
|-----------|-------------|----------------|------------------------------|
| C-51 | R19 V-02/V-03 had monolithic BUILDER → Thread 2 capped at 3 markers, C-49 structurally unreachable | All R20 variations have IMPLEMENTER/MEASURER split → Thread 2 has 5 markers | PASS all five |
| C-52 | R19 V-01–V-04 had "fails C-48" rule only; V-05 had consequence clause | All R20 variations carry rule statement + consequence clause; V-04 adds self-referential binding; V-05 names specific assertion | PASS all five |
| C-49 Thread 2 marker count | R19 V-02/V-03: Thread 2 at 3 markers, structurally below Thread 1's 5 → C-49 failed | R20: Thread 2 at 5 markers for all five → depth parity achievable | PASS all five |

---

```json
{"top_score": 367, "all_essential_pass": true, "new_patterns": ["seven-surface Thread 1 saturation: preamble title declaration + five standard competitor surfaces + Phase 8 MEASURER measurement-table B-00 reference row creates exhaustive inertia competitor tracking across every structural node, making competitor lifecycle never ambient", "maximum-specificity C-52 consequence clause names the concrete countable assertion being retroactively voided (the four-marker count declared in the inventory table) rather than the inventory in general — the compliance circuit closes on a specific prior claim", "per-phase lifecycle callout lines at every phase entry (not only container-boundary annotations) force explicit sub-role acknowledgment before each phase executes, addressing lifecycle drift at phase granularity and making the IMPLEMENTER COMPLETE → MEASURER transition visible at the moment it occurs"]}
```
