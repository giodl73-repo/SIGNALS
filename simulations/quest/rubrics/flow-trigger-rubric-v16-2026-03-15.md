All correct. The rubric is written to `simulations/quest/rubrics/flow-trigger-rubric-v16-2026-03-16.md`.

---

**v16 summary — two new aspirational criteria extracted from R18:**

| ID | Source | What it captures | Extends | N_aspirational | Max (raw) |
|----|--------|-----------------|---------|----------------|-----------|
| C-44 | V-03 C-42 PARTIAL (first bracket extended, second bare) | **Uniform extended-bracket coverage** — ALL assertion lines in the NOTE block carry `[must be VALUE — rationale]`; no bare brackets alongside extended ones. PARTIAL = ≥50% coverage; FAIL = <50%. Mixed coverage reintroduces separability risk at uncovered assertions. | C-42 (same domain — C-44 raises the coverage floor from "at least two" to "all"); C-22 (uniform slot mandate applied to bracket contents) | 35 → 36 | — |
| C-45 | V-03 variation axis ("each phase body opens with 'Why this phase must complete before the next begins' paragraph") | **Per-phase forward-looking lifecycle ordering rationale** — each lifecycle phase body embeds an explicit statement naming (a) the structural dependency the next phase requires from this phase and (b) the violation mode if the next phase begins early. Distinct from INERTIA CONTRAST (backward-looking mechanism contrast) and exit conditions (what must be done to exit). Makes phase collapsing a visible structural edit. | C-25/C-27 (lifecycle gate — C-45 adds forward-looking dependency framing per phase body); C-26 (INERTIA CONTRAST — backward direction; C-45 is the forward direction) | 36 → 37 | 152.5 → 157.5 |

**Structural relationship:** C-44 operates at the bracket level within the NOTE block (uniform extended-bracket coverage), tightening C-42's "at least two" threshold to "all." C-45 operates at the phase level across the full document (per-phase inter-phase dependency justification), capturing a rationale directionality — forward-looking dependency framing — that neither INERTIA CONTRAST (C-26) nor exit conditions (C-25) address.
