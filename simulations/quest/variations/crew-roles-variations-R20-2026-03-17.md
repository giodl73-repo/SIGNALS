Written to `simulations/quest/golden/crew-roles-variate-R20-2026-03-17.md`.

---

**R20 summary:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | **Axis-L** — Explicit phase mapping table | C-42(a) declared, removes inference requirement for C-42 scoring |
| V-02 | **Axis-M** — Full self-routing on all gates | Every EXIT GATE has PASS→continue + FAIL→remediate branches; extends C-43 pattern system-wide |
| V-03 | **Axis-N** — Baseline propagation map | Assigns S/G term to each role at STEP 1 before candidates are enumerated; converts CROSS-ROLE SPREAD CHECK from scan to conformance |
| V-04 | **Axis-L + Axis-M** | Declared phase structure + self-routing gates; both C-42 and C-43 maximally explicit |
| V-05 | **Axis-L + Axis-M + Axis-N** | Full integration; tests whether density causes execution skipping |

**Baseline**: R19 V-02 (4-step compressed), which already satisfies C-42(b) by positional inference and C-43 by dual-routing in EARLY INERTIA ANCHOR CHECK. R20 tests whether C-42(a) explicit declaration is worth adding (V-01), whether system-wide gate routing improves fidelity (V-02), and whether upfront baseline assignment eliminates the C-41 failure mode (V-03).
