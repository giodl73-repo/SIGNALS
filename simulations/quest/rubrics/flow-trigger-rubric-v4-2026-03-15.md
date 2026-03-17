Written to `simulations/quest/rubrics/flow-trigger-rubric-v4-2026-03-16.md`.

---

**Three new criteria added (C-17–C-19), N_aspirational: 8 → 11:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-17 | V-01 STRONG PASS / C-02 | Named EOR table + per-entry `Positioned because: EOR-{NN}` citation — execution order auditable at entry level, not just globally declared | C-02 (global order statement) |
| C-18 | V-02 STRONG PASS / C-10 | CASCADE DEPTH BUDGET declared pre-enumeration + `[Depth: N/MAX]` counter per cascade entry + `[DEPTH EXCEEDED]` terminator + storm verdict checks `DE > 0` — runaway chains structurally visible and storm-detectable | C-10 (end-to-end trace) |
| C-19 | V-03 STRONG PASS / C-13 | Named EXCLUSION LOG sweeps all automation layers before candidate scan + `Exclusion log reference:` field mandatory in verdict blocks — two citation artifacts required (enumeration rows + exclusion log), three-part accounting complete | C-13 (row citations) + C-14 (scope gate) |

**Structural relationship:** C-17 makes the ordering obligation per-entry rather than global. C-18 makes cascade depth a first-class accounting artifact. C-19 closes the citation gap between the pre-enumeration scope sweep and the post-enumeration verdicts — the log is the bridge.
