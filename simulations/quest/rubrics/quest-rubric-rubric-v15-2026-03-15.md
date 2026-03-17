Reading the scorecard carefully to identify the two extractable excellence patterns before writing the new criteria.

**Patterns identified:**

1. **ES-R14-1 / V-05**: Phase 8.5 pre-emit gate requiring quoted evidence from two structural loci — makes DFM compliance verifiable from artifact text alone; independently resolves a previously-partial audit-trail criterion. → **C-41**

2. **ES-R14-2 / V-05 vs V-04**: Layered dual-path enforcement — per-phase SCOPE GATE (construction phase) + independent pre-emit gate (between construction and emission) operate at structurally distinct phases. V-04 demonstrates PASS C-39/C-40 with only single-path enforcement; V-05 adds the independent pre-emit path. → **C-42**

Formula bumps from `/32` to `/34`.

---

## quest-rubric Rubric v15

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/34 × 10)` — denominator /32 → /34

---

### Essential criteria (C-01–C-05) — carried from earlier rounds

Binary pass/fail. A single essential FAIL floors the score regardless of E/R/A components.

*(C-01 through C-05 text preserved verbatim from prior versions.)*

---

### Recommended criteria (C-06–C-08) — carried from earlier rounds

PARTIAL on a recommended criterion scores 0.5.

*(C-06 through C-08 text preserved verbatim from prior versions.)*

---

### Aspirational criteria (C-09–C-22) — carried from earlier rounds

*(C-09 through C-22 text preserved verbatim from prior versions.)*

---

### Round 7–11 criteria (C-23–C-35) — carried forward

*(C-23–C-28 and C-30, C-32, C-34–C-35 text preserved verbatim; C-29, C-31, C-33 text shown in v13 file.)*

---

### Three criteria from Round 12 (C-36–C-38) — carried forward

*(Full criterion text preserved verbatim from v13.)*

---

### Two criteria from Round 13 excellence signals (C-39–C-40) — carried forward

*(Full criterion text preserved verbatim from v14.)*

---

### Two criteria from Round 14 excellence signals

Both target **DFM enforcement architecture** — the structural property that the per-phase and pre-emit enforcement mechanisms for DFM propagation (required by C-39 and C-40) are independently verifiable from artifact text (C-41) and operate at structurally distinct phases rather than as a single-path system (C-42).

---

**C-41 — Pre-emit evidence-quotation gate**

*Source signal: ES-R14-1 / V-05.*

V-05 introduces a Phase 8.5 gate positioned after the final construction role and before the output instruction executes. The gate requires the generator to produce quoted evidence from two structural loci: (1) the Scope Gatekeeper prohibition clause, confirming the structural DFM label appears in the prohibition text as required by C-39; and (2) the output instruction clause, confirming the label-carry requirement appears in the emit directive as required by C-40. This makes structural compliance verifiable from artifact text alone — a reviewer can audit DFM traceability without replaying the construction phase. V-05's Phase 8.5 gate also resolves a previously-partial audit-trail criterion in the C-23–C-35 cluster, confirming that evidence-quotation requirements have cross-criterion stabilizing effects beyond the specific propagation checks they serve.

**Criterion:** A pre-emit gate (placed after the final construction role, before the artifact emission step) requires the generator to produce quoted text from: (a) the Scope Gatekeeper prohibition clause, showing that the structural DFM label appears in the prohibition text, and (b) the output instruction clause, showing that the label-carry requirement appears in the emit directive. Both quotations must be present and attributed to their structural source. The gate must block emission if either quotation is absent or if the quoted text does not contain the required label.

**PARTIAL condition:** The gate requires one of the two quotations (prohibition clause or output instruction clause) but not both; or the gate is present but operates as an advisory check rather than a blocking emission gate.

**Independence from C-39 and C-40:** C-39 tests whether the Scope Gatekeeper prohibition names the DFM block. C-40 tests whether the output instruction requires the label in the emitted purpose statement. C-41 tests whether a pre-emit gate independently verifies both constraints hold before the artifact is emitted. V-04 demonstrates PASS C-39 / PASS C-40 / FAIL C-41: structural enforcement is present at the construction phase, but no pre-emit gate independently re-verifies compliance from artifact text.

---

**C-42 — Dual-path DFM enforcement (per-phase gate + pre-emit gate)**

*Source signal: ES-R14-2 / V-05.*

V-05 achieves the highest score in Round 14 by layering two independent enforcement paths for DFM propagation: the per-phase SCOPE GATE operating within the construction phase (inherited from V-01 via C-39) and the pre-emit Phase 8.5 gate operating between construction and emission (introduced in V-05 via C-41). These paths are structurally independent: a compliance failure that evades the per-phase gate — for example, a partial label citation that satisfies a single reviewer's local check — is detected by the pre-emit quotation gate, which requires the prohibition clause text to contain the label directly, not a reviewer's judgment that it does. Dual-path enforcement is architecturally distinct from having two gate instances of the same type: the gates must operate at different phases, and the pre-emit gate must derive its pass/fail result from artifact structure independently, not by inheriting the per-phase gate's result.

**Criterion:** The rubric construction protocol contains at least two structurally distinct enforcement mechanisms for DFM propagation operating at different phases: (a) a per-phase gate within the construction phase — such as a SCOPE GATE exit condition on a ROLE block — and (b) an independent pre-emit gate operating after construction is complete — such as a Phase 8.5 evidence-quotation gate. The two gates must be structurally independent: the pre-emit gate must verify compliance directly from artifact structure; it must not treat the per-phase gate's pass result as sufficient evidence of compliance.

**PARTIAL condition:** Two enforcement mechanisms are present but operate at the same phase (e.g., two SCOPE GATE checks both within the construction phase); or the pre-emit gate is present but defers to the per-phase gate's pass/fail result rather than independently re-verifying from artifact text.

**Independence from C-41:** C-41 tests whether a pre-emit evidence-quotation gate exists. C-42 tests whether the enforcement architecture as a whole spans at least two structurally independent phases. A rubric could satisfy C-41 (pre-emit gate present) while failing C-42 (no per-phase gate; single-path enforcement through the pre-emit gate alone). Conversely, V-01 demonstrates a per-phase SCOPE GATE with no pre-emit gate: FAIL C-41 / FAIL C-42. V-05 satisfies both.

---
