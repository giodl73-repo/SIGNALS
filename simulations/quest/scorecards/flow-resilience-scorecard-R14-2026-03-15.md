---

## flow-resilience — Round 14 Scoring (Rubric v14)

### R14 Variation Axes

| Variation | Axis | Target | Base (R13 under v14) |
|---|---|---|---|
| V-01 | Gate 1 CLOSE two-item independence | C-43 | 68/72 |
| V-02 | Gate 2b CLOSE two-checkbox independence | C-42 | 67/72 |
| V-03 | Full CLOSE independence (Gate 2b + Gate 1) | C-42 + C-41/C-43 | 65/72 |
| V-04 | Formal PART A/B GAP REGISTRY | C-44 | 70/72 |
| V-05 | Stability validation (unchanged) | confirm 72/72 | 72/72 |

---

### New Criteria Scoring (C-42 / C-43 / C-44)

**C-42** — all five variations PASS. V-02 and V-03 crack it in R14 by splitting the combined Gate 2b CLOSE checkbox into two independent items. V-01/V-04/V-05 carry it from R13.

**C-43** — all five variations PASS. V-01 cracks it in R14 by splitting the combined Gate 1 CLOSE statement into two independent items (required-basis:present / prohibited-basis:absent). V-03 also cracks it as part of its combination pass.

**C-44** — V-03/V-04/V-05 PASS; V-01/V-02 FAIL. V-04 cracks C-44 in R14 by replacing inline gap findings with formal PART A/PART B GAP REGISTRY sections with three-field structured entries (Source / Missing link / Consequence).

**C-41** — V-03 resolves this as a side effect of the C-43 fix: replacing the presence-only Gate 1 CLOSE with two independent items simultaneously satisfies both C-41 (both basis types named) and C-43 (structurally independent). One structural intervention closes two criteria.

---

### Rankings

| Rank | Variation | Uncapped | Delta |
|------|-----------|----------|-------|
| **1 (tie)** | **V-04** | **72/72** | +2 |
| **1 (tie)** | **V-05** | **72/72** | 0 |
| **3** | **V-03** | **71/72** | +6 |
| **4** | **V-01** | **70/72** | +2 |
| **5** | **V-02** | **69/72** | +2 |

All composites: **100/100**. V-04 joins V-05 at the 72/72 maximum. V-03 gains the most (+6) via co-resolution: fixing C-43 simultaneously resolves C-41 (both conditions share the same structural form).

**No new patterns** — V-03's co-resolution is a property of existing criteria, not a new structural axis. V-04/V-05 confirm v14 is discriminating and complete. Plateau count: 1 (first rubric-stable round). R15 will confirm dual convergence if C-15 PARTIAL for V-02/V-03 remains the sole remaining gap.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
th two-item form: `[ ] Impossibility argument basis confirmed: required basis: present` and `[ ] Impossibility argument prohibition confirmed: prohibited basis: absent` (targets C-41 and C-43 simultaneously). C-15 still prose-only (no formal template — same PARTIAL as R13). Formal PART A/B GAP REGISTRY retained from R13 V-03 (C-44 already PASS).

- **V-04**: Formal PART A + PART B GAP REGISTRY added. Replaces inline gap findings (`Dark chaos finding: CHAOS-OBS-GAP-NN: [scenario ID] has no linked Observable Signal` and `Unvalidated signal finding: OBS-CHAOS-GAP-NN: ...`) with named registry sections: each gap entry is a structured three-field artifact — `Source:`, `Missing link:`, `Consequence:` — in `PART A GAP REGISTRY` and `PART B GAP REGISTRY` named sections. Nil state confirmed with explicit `PART A GAP REGISTRY: none.` / `PART B GAP REGISTRY: none.` when no gaps exist. Matrix closure block updated to require four named non-placeholder fields including registry status. C-42/C-43 retained from R13 V-04.

- **V-05**: Identical body to R13 V-05. No changes. Stability confirmation — validates that the 72/72 perfect score is not dependent on contextual factors that might regress under rubric v14.

---

### Evidence Summary — New Criteria Under v14

**C-42 — Gate-Close Clause Structural Independence**

| Variation | Gate 2b CLOSE form | Score |
|---|---|---|
| V-01 | **TWO checkboxes** (inherited from R13): `[ ] Identity assertion confirmed: every TCR contains the verbatim Gate 2 threshold expression — identical string, not a paraphrase` AND `[ ] Prohibition clause confirmed: no TCR contains a paraphrased or independently calibrated expression`. Each independently falsifiable. | **PASS** |
| V-02 | **TWO checkboxes** (R14 fix): Combined `[ ] Every TCR contains verbatim Gate 2 threshold expression (identity assertion satisfied — no paraphrase, no independent calibration)` split into `[ ] Identity assertion confirmed` and `[ ] Prohibition clause confirmed` as separate items. | **PASS** |
| V-03 | **TWO checkboxes** (R14 fix): Same two-checkbox structure applied from the combination pass — positive assertion and prohibition each independently checkable. | **PASS** |
| V-04 | **TWO checkboxes** (inherited from R13): same V-01/V-04/V-05 form. | **PASS** |
| V-05 | **TWO checkboxes** (unchanged from R13 V-05). | **PASS** |

**All five R14 variations: C-42 PASS.** V-02 and V-03 crack this in R14 (were FAIL in R13); V-01/V-04/V-05 carry it from R13.

---

**C-43 — Impossibility Argument Basis Clause Independence**

| Variation | Gate 1 CLOSE form | Score |
|---|---|---|
| V-01 | **TWO independent items** (R14 fix): `[ ] Impossibility argument basis confirmed: every Argued-Impossible cites an architecture basis (CAP theorem guarantee, synchrony constraint, topology bound) — required basis: present` AND `[ ] Impossibility argument prohibition confirmed: no Argued-Impossible argument is based on description absence (the topic does not mention X) — prohibited basis: absent`. Each independently checkable. | **PASS** |
| V-02 | **TWO independent items** (inherited from R13): same form as R13 V-02/V-04/V-05 — required-basis:present + prohibited-basis:absent as separate checkboxes. | **PASS** |
| V-03 | **TWO independent items** (R14 fix): presence-only Gate 1 CLOSE replaced with two-item form — both required-basis:present and prohibited-basis:absent independently verifiable. Also resolves C-41 (previously FAIL for V-03 in R13). | **PASS** |
| V-04 | **TWO independent items** (inherited from R13): same form as R13 V-02/V-04/V-05. | **PASS** |
| V-05 | **TWO independent items** (unchanged from R13 V-05). | **PASS** |

**All five R14 variations: C-43 PASS.** V-01 and V-03 crack this in R14.

---

**C-44 — Bidirectional Gap Registry Artifact Structure**

| Variation | Matrix gap form | Score |
|---|---|---|
| V-01 | Inline gap findings: `Dark chaos finding: CHAOS-OBS-GAP-NN: [scenario ID] has no linked Observable Signal — dark chaos scenario. Emit: CHAOS-OBS-GAP-NN` and `Unvalidated signal finding: OBS-CHAOS-GAP-NN: ...`. Named ID per gap but no three-field structured registry section. Consequence field absent. | **FAIL** |
| V-02 | Inline gap findings (same abbreviated form as R13 V-02). No formal registry section in either direction. Consequence field absent. | **FAIL** |
| V-03 | **Formal PART A + PART B GAP REGISTRY** (inherited from R13 V-03): each gap entry is `CHAOS-OBS-GAP-NN: Source: [ID] / Missing link: [signal] / Consequence: [specific]`. Nil confirmed with explicit `PART A GAP REGISTRY: none.` Both directions require named registry section before COMPLETE. | **PASS** |
| V-04 | **Formal PART A + PART B GAP REGISTRY** (R14 fix): inline emit instructions replaced with three-field structured blocks — `Source:`, `Missing link:`, `Consequence:` per gap entry. Nil state: `PART A GAP REGISTRY: none.` Matrix closure block updated with four named non-placeholder fields including registry audit. | **PASS** |
| V-05 | **Formal PART A + PART B GAP REGISTRY** (unchanged from R13 V-05): same three-field registry structure as V-03. | **PASS** |

V-01 and V-02: C-44 FAIL (inline gap form retained, no formal registry). V-03/V-04/V-05: C-44 PASS.

---

**C-41 — Impossibility Argument Quality Gate Postcondition**

| Variation | R13 status | R14 status | Evidence |
|---|---|---|---|
| V-01 | PASS | PASS | Combined `architecture basis, not description absence` form remains present. Satisfies C-41 pass condition (both basis types named in same postcondition). R14 V-01 now adds C-43 compliance above, but C-41 was already satisfied by the combined statement. |
| V-02 | PASS | PASS | Two-item form names both basis types. |
| V-03 | **FAIL** | **PASS** | R14 V-03 replaces presence-only `cites DS Primitive by name` with two-item form — both required and prohibited basis now named in Gate 1 CLOSE. C-41 and C-43 both crack simultaneously by the same fix. |
| V-04 | PASS | PASS | Unchanged two-item form. |
| V-05 | PASS | PASS | Unchanged. |

V-03 resolves C-41 as a side effect of the R14 C-43 fix: adding the prohibited-basis check to Gate 1 CLOSE also names the required basis type, satisfying C-41's pass condition. A single structural intervention closes two v13/v14 failures.

---

**C-15 — DS-Primitive-Grounded Impossibility Arguments**

| Variation | Status | Evidence |
|---|---|---|
| V-01 | PASS | Formal `DS Primitive cited:` field template with VALID/INVALID annotated examples retained (R13 V-01). |
| V-02 | PARTIAL | Prose guidance only — "name DS Primitive (CAP theorem guarantee, synchrony constraint, topology bound). 'The topic does not mention X' is not a DS Primitive" — present but no formal field template with inline examples. Unchanged from R13 V-02. |
| V-03 | PARTIAL | Same prose guidance form as V-02. R14 V-03 does not target C-15. No formal template added. |
| V-04 | PASS | Formal `DS Primitive cited:` field template with VALID/INVALID annotated examples retained (R13 V-04). |
| V-05 | PASS | Formal template retained (R13 V-05). |

C-15 PARTIAL for V-02 and V-03 unchanged in R14. Neither variation targeted C-15 in their R14 axis.

---

### Full Aspirational Score Breakdown (v14: C-09 through C-44, 28 criteria)

All essential (C-01 through C-05): **PASS** all variations.
All recommended (C-06 through C-08): **PASS** all variations.
Aspirational C-09 through C-32 (excluding C-15): **PASS** all variations.
Aspirational C-33 through C-44: see delta table.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-15 | PASS (2) | PARTIAL (1) | PARTIAL (1) | PASS (2) | PASS (2) |
| C-36 | PASS (2) | PASS (2) | PASS (2) | PASS (2) | PASS (2) |
| C-37 | PASS (2) | PASS (2) | PASS (2) | PASS (2) | PASS (2) |
| C-38 | PASS (2) | PASS (2) | PASS (2) | PASS (2) | PASS (2) |
| C-39 | PASS (2) | PASS (2) | PASS (2) | PASS (2) | PASS (2) |
| C-40 | PASS (2) | PASS (2) | PASS (2) | PASS (2) | PASS (2) |
| C-41 | PASS (2) | PASS (2) | **PASS (2)** | PASS (2) | PASS (2) |
| C-42 | PASS (2) | **PASS (2)** | **PASS (2)** | PASS (2) | PASS (2) |
| C-43 | **PASS (2)** | PASS (2) | **PASS (2)** | PASS (2) | PASS (2) |
| C-44 | FAIL (0) | FAIL (0) | PASS (2) | **PASS (2)** | PASS (2) |
| **Uncapped** | **70/72** | **69/72** | **71/72** | **72/72** | **72/72** |

Bold = R14 fix (criterion newly PASS vs R13). V-03 gains the most (+6): C-41, C-42, C-43 all crack simultaneously. V-04 gains +2 from C-44. V-01 gains +2 from C-43. V-02 gains +2 from C-42. V-05 unchanged.

---

### Composite Scoring

| Variation | Essential (max 60) | Recommended (max 30) | Aspirational (capped at 10) | **Composite** |
|---|---|---|---|---|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

All composites 100/100 (aspirational band capped at 10 — no FAIL in the 28 aspirational criteria at scale sufficient to move the cap). Tiebreak by uncapped aspirational.

---

### Rankings

| Rank | Variation | Uncapped | R13 base | Delta | Distinguishing factors |
|------|-----------|----------|---------|-------|----------------------|
| **1 (tie)** | **V-04** | **72/72** | 70/72 | +2 (C-44) | Full independence + formal registry — inherits R13's C-42/C-43 PASS, adds C-44 formal REGISTRY in R14 |
| **1 (tie)** | **V-05** | **72/72** | 72/72 | 0 | Stable — confirms R13 V-05's 72/72 holds without regression under R14 conditions |
| **3** | **V-03** | **71/72** | 65/72 | +6 (C-41, C-42, C-43) | Largest R14 gain — full CLOSE independence combination resolves three criteria simultaneously; C-15 PARTIAL (-1) is sole remaining gap |
| **4** | **V-01** | **70/72** | 68/72 | +2 (C-43) | Gate 1 CLOSE independence added; C-44 absent (inline gap form retained) |
| **5** | **V-02** | **69/72** | 67/72 | +2 (C-42) | Gate 2b CLOSE independence added; C-44 absent; C-15 PARTIAL unchanged |

---

### Excellence Signals

**Convergence signal**: V-04 joins V-05 at 72/72. Two variations now achieve the v14 maximum. No criteria remain fully uncracked — V-03 R14 at 71/72 has only C-15 PARTIAL, which is a known and discriminated criterion since R9.

**V-03 gain pattern — coupling resolution**: The R14 V-03 axis targets C-42 + C-43 combination. Because V-03's Gate 1 CLOSE was presence-only (C-41 FAIL, C-43 FAIL), a single structural fix — replacing the presence check with two independent items — resolves C-41 and C-43 in one pass. This is a **co-resolution pattern**: two criteria that are logically orthogonal (C-41 requires both basis types named; C-43 requires them structurally separate) can be satisfied by a single form that satisfies both simultaneously. V-03 jumps six points (+6) from the least-advanced R13 variation to third place.

**No new structural patterns**: The co-resolution observation (C-41/C-43 satisfied by same form) does not produce a new rubric criterion — it is a property of existing criteria (independence subsumes naming). V-04 and V-05's 72/72 confirm the v14 rubric is discriminating and complete. No excellence signals emerge from R14 that v14 does not already capture.

**Remaining open criteria after R14**:
- C-44 for V-01 and V-02 (inline gap form, no formal registry)
- C-15 PARTIAL for V-02 and V-03 (prose-only DS Primitive guidance)
These are refinement targets for R15; neither produces new rubric criteria.

---

### Discriminating Question for R15

R14 establishes: **V-04 and V-05 are both at 72/72.** V-03 is at 71/72 (C-15 PARTIAL). The open question entering R15: does V-03 crack C-15 PASS (formal DS Primitive template with VALID/INVALID examples) when C-15 is targeted as the sole R15 axis? If yes, V-03 joins the 72/72 cluster and plateau_count = 2 → dual convergence. If no, V-01/V-02 must also crack C-44 before convergence.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
