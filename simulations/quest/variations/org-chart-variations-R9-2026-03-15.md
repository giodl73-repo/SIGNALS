Written to `simulations/quest/golden/org-chart-variate-R9-2026-03-16.md`.

---

## R9 Summary

**Target:** First 19/19 (100.0) — combines V-02/R8's single-layer imperative (C-27) with V-04/R8's two-step conditional remediation (C-26).

**The synthesis problem R8 left open:**
- V-02/R8: full imperative everywhere, but guard says "MUST verify count >= 2; emit" with no recovery if count < 2 → C-26 fails
- V-04/R8: Step 1/Step 2 protocol present, but ENFORCEMENT paragraphs injected inside unchanged conversational prose → C-27 fails (dual-layer)

**R9 axes (3 single-axis + 2 combined):**

| V | Axis | Key Delta |
|---|------|-----------|
| V-01 | Phrasing register | Numbered Step 1/Step 2 inside full imperative — the canonical synthesis |
| V-02 | Phrasing register | IF/THEN/DO-NOT branching syntax instead of numbered steps — more machine-legible conditional |
| V-03 | Inertia framing | Opening blocking gate ("DO NOT write org output until VERDICT") before all sections — tests C-01/C-11/C-14 quality lift |
| V-04 | Register + lifecycle | V-01 synthesis + MUST-PRECEDE gates at every section boundary |
| V-05 | Inertia + register + lifecycle | V-03 gate + V-02 if/else + compressed section descriptions — shortest complete prompt |

**Primary risk to watch:** V-03's opening gate paragraph uses slightly conversational framing ("Jumping to org boxes before the VERDICT is the anti-pattern...") — a scorer could classify this as descriptive prose coexisting with the governed inertia behavior, triggering a C-27 fail. V-01 and V-02 carry no such risk.
