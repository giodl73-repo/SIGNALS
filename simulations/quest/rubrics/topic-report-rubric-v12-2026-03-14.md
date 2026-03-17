Written to `simulations/quest/rubrics/topic-report-rubric-v12-2026-03-15.md`.

---

**What was extracted from R11 and why:**

**3 base axes → C-40, C-41, C-42:**

| New ID | Axis | What it captures |
|--------|------|-----------------|
| C-40 | D | Consequence-grounding: C-34's prohibition gains a named failure-mode line (`SLOT 3 contamination consequence:`). Precondition: C-34. |
| C-41 | E | Format pre-delivery: Branch B register entries gain format-type qualifiers `(one card row, no markdown)`. Precondition: C-35. |
| C-42 | F | Header temporal role: the register header carries `[TEMPORAL ROLE: planning phase...]`, making the register self-annotating at read time. Precondition: C-36. |

**3 pairwise composites → C-43, C-44, C-45:**

| New ID | Preconditions | Minimal design | System property |
|--------|--------------|----------------|-----------------|
| C-43 | C-40 + C-41 | V-03 (D+E) | Two independent failure modes closed simultaneously |
| C-44 | C-40 + C-42 | V-04 (D+E+F) | Contamination consequence situated within a declared temporal system |
| C-45 | C-41 + C-42 | V-04 (D+E+F) | Format constraints as entries in a named planning-phase document |

**R11 ordering under v12 (denominator /37):**

| Variation | Score | Notes |
|-----------|-------|-------|
| V-04 (D+E+F) | 37/37 = 100.0 | All 37 pass |
| V-03 (D+E) | 34/37 = 99.2 | +C-40, C-41, C-43; fails C-42, C-44, C-45 |
| V-01 (D only) | 32/37 = 98.6 | 31 v11 criteria + C-40 |
| V-05 (neutral) = V-02 (E only) | 31/37 = 98.4 | V-05: 31 v11; V-02: 30 v11 (C-34 fails) + C-41 |

The V-01=V-02 tie from R10 is broken. A new tie forms at V-05=V-02 (different paths to 31/37). R12 discriminator candidates are at the bottom of the file.
