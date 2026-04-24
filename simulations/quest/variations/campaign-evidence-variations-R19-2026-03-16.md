Written to `simulations/quest/golden/campaign-evidence-variate-R19-2026-03-17.md`.

---

## Variates: campaign-evidence (Round 19)

**Three new criteria targeted (C-45, C-46, C-47). Three single-axis variations, then two combined.**

---

### V-01 -- Axis A: Vocabulary anchoring (C-45 only)
**Stage order:** Web-first (default) — isolates C-45 from C-43 confounding.

**Key signal:** Inertia Baseline table gets an **ID column** (`IB-ATTR`, `IB-CAL`, etc.). A **Vocabulary Contract** is declared at the top of Form Templates: "all binary cell annotations use IB IDs from the fixture; no ad hoc naming." Every binary cell shifts from `-- no attribution collapse` to `-- [IB-ATTR] absent?`. The audit table gains an `Antipattern (IB Row)` column populated with IB IDs.

**Hypothesis:** C-45 fails when names merely coincide between cells and the IB table. The ID column + vocabulary contract create a **machine-checkable link**: a cell naming `[IB-CAL]` is auditable against row `IB-CAL`; a drift in name is a visible structural violation, not an interpretive dispute.

---

### V-02 -- Axis B: Checksum extensibility narrative (C-46 only)
**Stage order:** Intel-first (C-43 in effect). Ad hoc antipattern annotations (C-44). No IB vocabulary contract.

**Key signal:** The checksum section gains an *Architectural history* paragraph reconstructing the full decomposition event:
> Prior state: 5 rules → 40 artifacts. Decomposition: SEQUENCING split into SEQUENCING-HYPO (8 artifacts) + SEQUENCING-ORDER (7 artifacts), replacing the original 8. Delta: +7 propagated automatically. Total: 40 − 8 + 15 = **47. No static integer updated manually.**

**Hypothesis:** C-46 can be satisfied without the IB vocabulary contract. The narrative demonstrates extensibility as a **concrete historical event** — a first-time reader can follow the arithmetic and reconstruct the design decision from the checksum section alone, independent of whether cells use IB-IDs.

---

### V-03 -- Axis C: N/A antipattern grounding (C-47 only)
**Stage order:** Web-first. No IB table as canonical source. Ad hoc antipattern annotations.

**Key signal:** Every N/A declaration changes format from:
> `CALIBRATION -- N/A (evidence stage)`

to:
> `CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable here)`

This applies to PRE forms, POST forms, and the audit table N/A rows — everywhere a cell was previously structural-reason-only, it now names the excluded antipattern.

**Hypothesis:** C-47 is independent of the IB fixture. The antipattern name is already available in the rule declaration text; the N/A cell just needs to cite it. Full apparatus homogeneity — every cell names an antipattern, whether guarding or excluding — is achievable without IB-ID anchoring.

---

### V-04 -- Combined A+B: C-45 + C-46
**Stage order:** Intel-first. IB-ID vocabulary contract. Checksum narrative. N/A cells: structural reason only.

**Key signal:** The IB table and the checksum narrative **cross-reference each other**. The checksum narrative explains why the IB fixture has two SEQUENCING rows (IB-SEQ-H, IB-SEQ-O): they appeared automatically when SEQUENCING was decomposed. The fixture is not arbitrary — its rows reflect the governed decomposition event documented in the checksum. C-29 (extensibility), C-45 (vocabulary fixture), and C-46 (architectural history) form a mutually reinforcing unit.

---

### V-05 -- Combined A+B+C: Full integration (C-45 + C-46 + C-47)
**Stage order:** Intel-first. IB-ID vocabulary contract. Checksum narrative. N/A cells carry IB-IDs.

**Key signal:** Complete structural homogeneity. Every cell in the apparatus — PRE binary, POST binary, and N/A — names an IB antipattern by ID. The audit table is fully populated with IB Row values: positive rows say `IB-ATTR` (guarding); N/A rows say `IB-CAL` (excluded). A reader can verify that every IB ID appears in the expected cells without consulting rule declarations. The checksum narrative grounds the 6-row fixture in the decomposition history, making the entire apparatus self-documenting.

---

**Isolation matrix:**

| | C-43 Intel-first | C-44 antipattern annotations | C-45 IB vocab contract | C-46 checksum narrative | C-47 N/A antipattern names |
|---|---|---|---|---|---|
| V-01 | — | yes | **NEW** | — | — |
| V-02 | yes | yes | — | **NEW** | — |
| V-03 | — | yes | — | — | **NEW** |
| V-04 | yes | yes | **NEW** | **NEW** | — |
| V-05 | yes | yes | **NEW** | **NEW** | **NEW** |
