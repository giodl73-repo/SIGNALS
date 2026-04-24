Written to `simulations/quest/golden/listen-support-variate-R4-2026-03-16.md`.

---

## Round 4 — listen-support Variations (V-01 through V-05)

**Rubric target:** v4 (C-01 through C-18, max 140 pts)
**Base:** V-05 R3 — all C-01 through C-16 at ceiling; C-05 PARTIAL (gate at >=6); C-17/C-18 absent

---

### Axes

**3 single-axis:**

| Variation | Axis | Target criteria | Key change |
|-----------|------|-----------------|------------|
| V-01 | Output format | C-17 | STEP 1 restructured as **PHASE-SEVERITY LOOKUP TABLE** with explicit `KEY DECLARATION: Phase is the lookup key for severity assignment. No override path exists.` |
| V-02 | Lifecycle emphasis | C-17 | Prose prior kept in STEP 1; Phase-as-key embedded in the **card template itself** — `Severity: [derived from Phase-Severity Lookup Table -- no override path]` at point of use |
| V-03 | Phrasing register | C-18 | Formal **TABLE CHECK block** appended after STEP 3: `Total >= 7 -> YES/NO. If NO: revise. Do not proceed until YES.` Gate corrected from >=6 to >=7 throughout |

**2 combined:**

| Variation | Axes combined | Expected golden? |
|-----------|---------------|------------------|
| V-04 | V-01 + V-03 | YES — C-17 (lookup table) + C-18 (TABLE CHECK) |
| V-05 | V-01 + V-02 + V-03 + full R3 baseline (assumption audit, column-attributed markers) | YES — dual-site C-17 + C-18 + strongest structural guarantee |

---

### Key design decisions

**C-17 dual-site strategy in V-05:** The KEY DECLARATION fires at STEP 1 (top-level table header); the card template annotation fires again at STEP 8 (once per ticket). A model that forgets STEP 1 encounters the card reminder; a model that drops the annotation still violates a named top-level rule. Two independent enforcement sites.

**C-18 double-gate in V-05:** TABLE CHECK in STEP 3 is a procedural halt before ticket generation. The VALIDATION TRACE in STEP 7 independently checks `Total rows: [N] (required: >= 7)` post-hoc. If the model somehow proceeds past the STEP 3 gate, the trace catches it.

**Why V-01 and V-02 are predicted to block on golden:** Both retain Total >= 6 in STEP 3 (single-axis probe, only changing the C-17 axis). C-05 PARTIAL = `all_essential_pass FALSE` = golden blocked regardless of composite. These are diagnostic probes, not golden candidates.
