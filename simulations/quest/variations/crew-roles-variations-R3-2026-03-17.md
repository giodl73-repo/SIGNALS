Written to `simulations/quest/golden/crew-roles-variate-R3-2026-03-17.md`.

---

**crew-roles Variate R3 — 5 variations**

| Variation | Axis | Key Mechanism |
|-----------|------|---------------|
| V-01 | C-15 Verification-Gate-Phase | Phase 4 "VERIFICATION GATE" — each check declares `PASS`/`FAIL` explicitly; delivery blocked until all 4 clear |
| V-02 | C-16 Vocabulary-Linked Q&A | Per-answer `[vocab: {term}]` annotation required in each Q1/Q2/Q3 — linkage enforced at generation time, not as post-phase exit check |
| V-03 | C-14 Scope-Gradient-Enforcement | Scope planning table **before** writing files — SCOPE AUDIT gate fires before any file exists; prevents homogeneous sets rather than correcting them |
| V-04 | C-15 + C-14 | Pre-write scope gate (Phase 3) + post-write VERIFICATION GATE (Phase 5) — two enforcement points, neither redundant |
| V-05 | C-15 + C-14 + C-16 | Full synthesis: `[vocab]` annotation in Q&A, pre-write scope gate, named blocking gate with 4 per-check PASS declarations |

**Design choices worth scoring:**

- V-01 vs V-03's Step 4 from R2: R2 V-03 had scope + table checks embedded in a "Registry Summary Table" step without explicit gate identity. V-01 R3 names it "VERIFICATION GATE" and requires per-check declarations — tests whether naming and PASS declarations matter for C-15.

- V-02's `[vocab: {term}]` annotation vs V-05 R2's exit-condition coverage: exit conditions evaluate after the fact; inline annotations enforce during generation. This tests whether C-16 robustness differs by enforcement mechanism.

- V-03's pre-write scope planning vs V-01/V-04/V-05's post-write scope enforcement: catching scope homogeneity before files exist vs. after. V-04 has both — tests whether dual-enforcement adds value or noise.
