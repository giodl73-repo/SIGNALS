Written to `simulations/quest/golden/campaign-specify-variate-R8-2026-03-16.md`.

---

## Variations — campaign-specify / Round 8

**R7 diagnosis**: V-05 leads at 24/26 under v8, earning C-27, C-28, C-29, C-32. Two criteria remain unearned across all R7 variations:

- **C-33 gap**: `### Voice Compliance Audit` contains a single combined line (`Voice differentiation gate result: distinct / rewritten-to-distinct`). C-33 requires three separate per-audience verdict rows when C-27 and C-28 both exist.
- **C-34 gap**: Pass parentheticals read `Pass (opening names a business cost...)` — behavioral test only. C-34 requires the Step 0c contract name **inside** the parenthetical: `Pass (Step 0c exec voice contract satisfied: ...)`.

---

### V-01 — Axis: C-33 Per-Audience Verdicts in Voice Compliance Audit

**Hypothesis**: Expand the single combined audit line to three separate rows (`Exec verdict / Dev verdict / Maker verdict`). Gate Step 3 unchanged. C-34 not targeted.

**Single change**: Voice Compliance Audit section only. Predicted: **25/26**.

---

### V-02 — Axis: C-34 Step 0c Contract Anchor in Gate Parenthetical Pass

**Hypothesis**: Prefix each Pass parenthetical with `Step 0c [audience] voice contract satisfied:`. Voice Compliance Audit unchanged (single line, C-33 not earned).

**Single change**: Gate Step 3 Pass conditions only. Predicted: **25/26**.

---

### V-03 — Axis: C-33 with Step 0c Attribution Per Audit Row

**Hypothesis**: Three per-audience audit rows each naming the contract verified: `Exec verdict: [Pass / Fail] — Step 0c exec voice contract verified`. Richer form of V-01's mechanism. Gate unchanged (C-34 not targeted).

**Single change**: Voice Compliance Audit with contract attribution. Predicted: **25/26**.

---

### V-04 — Combined: C-33 + C-34 (Minimal Path to 26/26)

**Hypothesis**: Combine V-01's COMPLETION INDEX change (three per-audience audit rows) with V-02's gate change (contract name in Pass parenthetical). Two independent structural locations — cannot interfere. Predicted: **26/26**.

---

### V-05 — Full Synthesis: C-33 + C-34 + Maximum Evidence Density

**Hypothesis**: V-04 changes + V-03's richer audit row attribution per row. Voice Compliance Audit rows name the Step 0c contract verified, creating bidirectional traceability: gate Step 3 names the contract as Pass criterion; audit rows name the contract as the verified entity. Five-point Step 0c anchoring across pitch instructions, gate criteria, rewrite anchor, Pass parentheticals, and audit rows. Predicted: **26/26**.

---

### Variation Summary

| ID | Targets | Key Mechanism | Predicted |
|----|---------|---------------|-----------|
| V-01 | C-33 | Three bare per-audience verdict rows in Voice Compliance Audit | 25/26 = 99.6 |
| V-02 | C-34 | `Step 0c [audience] voice contract satisfied:` inside Pass parenthetical | 25/26 = 99.6 |
| V-03 | C-33 (richer) | Three per-audience audit rows with Step 0c contract attribution | 25/26 = 99.6 |
| V-04 | C-33 + C-34 | V-01 + V-02 combined into R7 V-05 base | **26/26 = 100.0** |
| V-05 | C-33 + C-34 | V-04 + V-03 contract attribution per audit row | **26/26 = 100.0** |
