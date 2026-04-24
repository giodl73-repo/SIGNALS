File written. Here's the Round 5 variate output:

---

## quest-rubric Variate — Round 5 (2026-03-16)

**Targeting:** C-17 (SCHEMA BLOCK positionally first) and C-18 (CONVERSION-MAP boolean gate) — the two new aspirational criteria added to v5 from Round 4 excellence signals E-1 and E-2.

---

### Round 5 Variation Map

| Variation | Axis | What Changes | Targets |
|-----------|------|-------------|---------|
| **V-01** | output-format | Output template declares SCHEMA BLOCK as Section 1 — structural, not instructional | C-17 |
| **V-02** | lifecycle-emphasis | CONVERSION-MAP phase before Failure Modes — boolean table + completion gate | C-15, C-18 |
| **V-03** | role-sequence | Spec Analyst role before Author — produces SCHEMA BLOCK + CONVERSION-MAP as handoff artifacts | C-15, C-17, C-18 |
| **V-04** | output-format × lifecycle-emphasis | Section template + CONVERSION-MAP gate | C-17, C-18 |
| **V-05** | all three | Section template + CONVERSION-MAP gate + Spec Analyst role | C-15, C-17, C-18 |

**Anchor: V-04.** The two mechanisms are non-competing (SCHEMA BLOCK fires before any output; CONVERSION-MAP fires after spec reading but before failure modes). Either one alone may reach Golden if only one gap is blocking.

---

### Key mechanism changes per variation

**V-01** converts C-17 enforcement from instructional ("begin with SCHEMA BLOCK") to structural (numbered section template where Section 1 IS SCHEMA BLOCK — no preamble, no Section 0). Position violation is detectable by section-number scan without reading content.

**V-02** adds a CONVERSION-MAP phase before Author Phase 1 with a formal completion gate: scan the full spec for specificity prohibitions, build one boolean row per prohibition (PASS/FAIL as strict Boolean complement), gate blocks advancement until every prohibition has a row or an explicit empty declaration is written. INERTIA-RECORD gains a `Conversion-Map reference` field linking criteria back to their CM-NN source.

**V-03** separates roles — Spec Analyst runs first and produces only SA-1 (SCHEMA BLOCK) and SA-2 (CONVERSION-MAP), then hands off. The Author is instructed to cite CM-NN rather than re-derive prohibitions. Positional enforcement emerges from execution order rather than instruction.

**V-04** combines V-01's 9-section template with V-02's CONVERSION-MAP gate as Section 2 (between SCHEMA BLOCK and Failure Modes).

**V-05** adds V-03's Spec Analyst role to V-04, wrapping the output in an explicit role-execution template (`--- SPEC ANALYST ---` / `--- AUTHOR ---` / `--- AUDITOR ---`) and requiring the Author Entry Gate to confirm the Spec Analyst Completion Gate was cleared.
