Now I have everything needed. Let me score all five variations.

---

# flow-trigger — Round 15 Scorecard (Rubric v12)

**Scenario:** Dynamics 365 Sales `account.statecode` Active(0) → Inactive(1)
**New criteria this round:** C-38 (Obligation statement self-containment), C-39 (Attribution chain design rationale)
**Scoring formula:** (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/31 × 10) — PARTIAL = 0.5 credit

---

## Shared baseline

All five variations carry identical structure for Phases 1–6, PROTOCOL PREAMBLE (Platform Term Contract, FM Catalog, Entry Schema Contract), INERTIA CONTRAST + DERIVATION TEST, STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, and CLOSURE CHECK counters with per-artifact inline role attribution (C-37 pattern from R14).

**Criteria uniform across all variations (all PASS):**

| Band | Criteria | Verdict |
|------|----------|---------|
| Essential | C-01–C-05 | PASS |
| Recommended | C-06–C-08 | PASS |
| Aspirational (shared) | C-09–C-31, C-33–C-37 (28 criteria) | PASS |

Evidence for shared aspirational passing: Phase 2/3 have FIRING ENTRY + NON-FIRING ENTRY schemas with all required slots (C-15, C-16, C-17, C-22); Phase 4 has Cascade Chain Table with [Depth: N/MAX] and [TERMINAL] (C-18); Phase 5 has evidence-cited anomaly verdicts (C-13); CLOSURE CHECK has zero-tolerance counters (C-20); Phase 0 has typed exit signal aggregate (C-27), per-obligation refutation conditions (C-28), "anonymous [X]" failure mode labels (C-34), DERIVATION TEST inside INERTIA CONTRAST (C-35), N/A-with-reason in every N/A cell (C-36), role-attributed CLOSURE CHECK counters (C-37).

---

## Differentiated criteria — per-variation

### C-32 — Unified Phase 0 obligation registry

| V | Evidence | Verdict |
|---|----------|---------|
| V-01 | 7-row unified table, all 6+ metadata types as named columns | PASS |
| V-02 | Vertical record blocks — all 6 metadata types present, not tabular. Pass condition requires "single named table." | PARTIAL |
| V-03 | Unified table identical to V-01, extended lifecycle narrative in preamble | PASS |
| V-04 | Unified table, formal imperative register in gate statements | PASS |
| V-05 | Same as V-04 | PASS |

### C-38 — Obligation statement self-containment

Pass condition: reading the Obligation text column alone yields: named role + modal verb (SHALL/MUST) + named artifact + temporal constraint.

| V | Obligation text (example) | Missing element | Verdict |
|---|--------------------------|-----------------|---------|
| V-01 | "EOR TABLE" (artifact category label only) | Role, modal verb, temporal constraint | FAIL |
| V-02 | "The Domain Expert SHALL produce the EOR TABLE" | Temporal constraint ("by when") | PARTIAL |
| V-03 | "The Domain Expert SHALL produce the EOR TABLE (ART-03) during Phase 0 before Phase 1 begins" | — all four present | PASS |
| V-04 | Same complete clause format as V-03 | — | PASS |
| V-05 | Same complete clause format as V-04 | — | PASS |

### C-39 — Attribution chain design rationale

Pass condition: output explicitly names both attribution layers AND names the artifact where each operates AND explains why both are required (states what breaks if either is removed).

| V | CLOSURE CHECK note content | Missing element | Verdict |
|---|---------------------------|-----------------|---------|
| V-01 | "Role attribution exists at both declaration time (ARTIFACT MANIFEST) and detection time (CLOSURE CHECK counter)." — structural observation, no consequence | Consequence of removal absent | FAIL |
| V-02 | "Both attribution points are present in this output and both artifacts are named." — structural inventory, no removal consequence | Consequence of removal absent | PARTIAL |
| V-03 | Names both layers + both artifacts. "Both attribution points are present; both artifacts are named." — stops at inventory | Consequence of removal absent | PARTIAL |
| V-04 | Separate **ATTRIBUTION CHAIN DESIGN RATIONALE** section after CLOSURE CHECK. Names both layers, names both artifacts, states: "Removing declaration-time attribution means role accountability is only discoverable when a gap is detected... Neither layer alone provides remediation self-sufficiency." | — explicit consequence present | PASS |
| V-05 | Rationale embedded as named note block INSIDE CLOSURE CHECK. "Removing either layer is understood to break remediation self-sufficiency, not merely reduce coverage." Co-located with detection mechanism — inseparable. | — explicit consequence + inseparability | PASS |

---

## Per-variation score computation

### V-01

| Band | Criteria | Pass / Partial / Fail | Composite contribution |
|------|----------|-----------------------|------------------------|
| Essential | C-01–C-05 | 5 PASS | 5/5 × 60 = 60.0 |
| Recommended | C-06–C-08 | 3 PASS | 3/3 × 30 = 30.0 |
| Aspirational | C-09–C-31, C-33–C-37 (28) | 28 PASS | |
| Aspirational | C-32 | PASS | |
| Aspirational | C-38 | FAIL | |
| Aspirational | C-39 | FAIL | |
| | Aspirational credits: 29.0 / 31 | | 29.0/31 × 10 = **9.35** |

**Composite: 99.35** | All essential: PASS

---

### V-02

| Band | Criteria | Pass / Partial / Fail | Composite contribution |
|------|----------|-----------------------|------------------------|
| Essential | C-01–C-05 | 5 PASS | 60.0 |
| Recommended | C-06–C-08 | 3 PASS | 30.0 |
| Aspirational | C-09–C-31, C-33–C-37 (28) | 28 PASS | |
| Aspirational | C-32 | PARTIAL (0.5) | |
| Aspirational | C-38 | PARTIAL (0.5) | |
| Aspirational | C-39 | PARTIAL (0.5) | |
| | Aspirational credits: 29.5 / 31 | | 29.5/31 × 10 = **9.52** |

**Composite: 99.52** | All essential: PASS

Note: V-02 scores marginally above V-01 despite C-32 PARTIAL because three PARTIALs (1.5) yield more credit than one PASS + two FAILs (1.0).

---

### V-03

| Band | Criteria | Pass / Partial / Fail | Composite contribution |
|------|----------|-----------------------|------------------------|
| Essential | C-01–C-05 | 5 PASS | 60.0 |
| Recommended | C-06–C-08 | 3 PASS | 30.0 |
| Aspirational | C-09–C-31, C-33–C-37 (28) | 28 PASS | |
| Aspirational | C-32 | PASS | |
| Aspirational | C-38 | PASS | |
| Aspirational | C-39 | PARTIAL (0.5) | |
| | Aspirational credits: 30.5 / 31 | | 30.5/31 × 10 = **9.84** |

**Composite: 99.84** | All essential: PASS

C-38 closed by complete obligation clauses. C-39 still partial — structural inventory without consequence statement.

---

### V-04

| Band | Criteria | Pass / Partial / Fail | Composite contribution |
|------|----------|-----------------------|------------------------|
| Essential | C-01–C-05 | 5 PASS | 60.0 |
| Recommended | C-06–C-08 | 3 PASS | 30.0 |
| Aspirational | C-09–C-31, C-33–C-37 (28) | 28 PASS | |
| Aspirational | C-32 | PASS | |
| Aspirational | C-38 | PASS | |
| Aspirational | C-39 | PASS | |
| | Aspirational credits: 31 / 31 | | 31/31 × 10 = **10.0** |

**Composite: 100.0** | All essential: PASS

C-39 closed by named ATTRIBUTION CHAIN DESIGN RATIONALE section with explicit consequence statements for removing either attribution layer. Section is adjacent to but separate from the CLOSURE CHECK block.

---

### V-05

| Band | Criteria | Pass / Partial / Fail | Composite contribution |
|------|----------|-----------------------|------------------------|
| Essential | C-01–C-05 | 5 PASS | 60.0 |
| Recommended | C-06–C-08 | 3 PASS | 30.0 |
| Aspirational | C-09–C-31, C-33–C-37 (28) | 28 PASS | |
| Aspirational | C-32 | PASS | |
| Aspirational | C-38 | PASS | |
| Aspirational | C-39 | PASS | |
| | Aspirational credits: 31 / 31 | | 31/31 × 10 = **10.0** |

**Composite: 100.0** | All essential: PASS

Same formula score as V-04. Structural differentiation: rationale is embedded as a named note block INSIDE the CLOSURE CHECK — physically inseparable from the detection mechanism. A future output that silently drops the rationale section must also drop part of the CLOSURE CHECK. V-05 > V-04 on regression-resistance, not on formula score.

---

## Ranking

| Rank | Variation | Composite | C-38 | C-39 | Key differentiator |
|------|-----------|-----------|------|------|--------------------|
| 1 | **V-05** | 100.0 | PASS | PASS | Rationale inline within CLOSURE CHECK — inseparable from mechanism; explicit "removes remediation self-sufficiency" language |
| 1 | **V-04** | 100.0 | PASS | PASS | Named ATTRIBUTION CHAIN DESIGN RATIONALE section with consequence statements; formal imperative register throughout |
| 3 | V-03 | 99.84 | PASS | PARTIAL | Complete obligation clauses close C-38; C-39 stops at structural inventory |
| 4 | V-02 | 99.52 | PARTIAL | PARTIAL | Role + SHALL + artifact in obligation text but no temporal constraint; three partials beat V-01's one pass + two fails |
| 5 | V-01 | 99.35 | FAIL | FAIL | Obligation text = artifact category labels only; CLOSURE CHECK note is observation, not rationale |

---

## Excellence signals — V-05 (top variation)

**Signal 1 — Obligation text as complete specification clause.**
"The Auditor SHALL produce the SCOPE GATE (ART-01) during Phase 0 before any candidate is named" — four required elements in a single text field: named role, modal verb, named artifact, temporal constraint. A reader consulting the Obligation column alone can derive the full compliance requirement without opening any other column.

**Signal 2 — Consequence-anchored attribution rationale.**
The note does not merely inventory both attribution layers — it states the failure mode of removing either: "Removing declaration-time attribution means role accountability is only discoverable when a gap is detected... Removing detection-time attribution means a reader finding an ABSENT counter must navigate to the ARTIFACT MANIFEST as a secondary lookup... Removing either layer is understood to break remediation self-sufficiency, not merely reduce coverage." This converts a structural observation into a named design commitment.

**Signal 3 — Mechanism-rationale co-location.**
The ATTRIBUTION CHAIN DESIGN RATIONALE is embedded as a named note block inside the CLOSURE CHECK structure, not as an adjacent section. Co-location ensures that any future output that retains the CLOSURE CHECK also retains its rationale — the design intent cannot silently regress without disrupting the detection mechanism itself.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Obligation text as complete specification clause: role + SHALL + artifact + temporal constraint as self-contained spec without consulting other columns", "Consequence-anchored attribution rationale: both layers named, both artifacts named, removal consequence explicitly stated as loss of remediation self-sufficiency not merely reduced coverage", "Mechanism-rationale co-location: design rationale embedded inline within detection mechanism block preventing silent regression"]}
```
