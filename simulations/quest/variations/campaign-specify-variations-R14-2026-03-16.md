Written to `simulations/quest/golden/campaign-specify-variate-R14-2026-03-17.md`.

---

**Round 14 — campaign-specify / Variations summary**

Baseline: R13 V-05 (39/39 under v14). All five variations preserve C-46, C-47, STEP 0A INERTIA ANCHOR, STEP 0B CITATION BINDING, and C-09 through C-45.

**Structural diagnosis driving R14:**

The v14 ceiling has three chains in incomplete form:
- **Inertia cost chain**: define → anchor (Phase 2 STEP 0A INERTIA ANCHOR) → *(no gate)* → *(no audit bind)*
- **Citation chain**: define → *(no anchor)* → requirement (CITATION FORM REQUIREMENT) → bind (STEP 0B CITATION BINDING)
- **Gate chain**: define + requirement (GATE CHAIN REQUIREMENT) → *(no audit source-binding)*

Voice contract chain is fully complete (define → anchor → gate → bind). R14 fills missing positions in the other three.

| Var | Axis | New element | Position filled |
|-----|------|-------------|-----------------|
| V-01 | INERTIA ANCHOR GATE | Gate after STEP 0A INERTIA ANCHOR | Inertia chain: anchor → **gate** |
| V-02 | STEP 0B STABILITY ANCHOR | Named anchor before Defeating Do Nothing | Citation chain: **anchor** before use |
| V-03 | PHASE GATE AUDIT SOURCE BINDING | Named source-binding in Phase Gate Audit | Gate chain: **audit bind** |
| V-04 | V-01 + V-02 | Both gate and citation anchor | Two chains extended simultaneously |
| V-05 | V-01 + V-02 + V-03 | All three | All three audit sections carry named source-binding blocks |

**Key R14 structural bet (V-05):** The named-source-binding triple (PHASE GATE AUDIT SOURCE BINDING / STEP 0B CITATION BINDING / STEP 0C SOURCE BINDING) across all three audit sections mirrors the named-requirement triple (GATE CHAIN REQUIREMENT / CITATION FORM REQUIREMENT / COLUMN-HEADER REQUIREMENT). If that symmetric pattern constitutes a v15 criterion, V-05 is the first ceiling.
