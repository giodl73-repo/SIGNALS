Written to `simulations/quest/golden/quest-rubric-variate-v6-R06-2026-03-16.md`.

---

**What changed from v5 → v6:**

**C-19 — Spec Analyst handoff with identifier citation** (E-1, R5)

The R5 roadmap named this explicitly: "The handoff artifact pattern (Spec Analyst produces CONVERSION-MAP, Author cites CM-NN) is the correct mechanism for C-15; absorb as E-1 for Round 6 rubric update." The pattern is distinct from C-15 (prohibitions *are* converted) and C-18 (conversion uses a boolean gate) — C-19 tests whether the Author phase *cites identifiers back* to the pre-phase artifact rather than re-deriving inline. V-02 passes C-18 but fails C-19; V-03 passes C-19 because Author writes `CM-NN` citations in criterion text.

**C-20 — Author Entry Gate structural block** (E-2, R5)

From V-03's scorecard evidence: "prompt's Author Entry Gate requiring Spec Analyst completion *further prevents* Author from writing criteria before SA-1 exists." This is distinct from C-11 (an Auditor exists) — C-20 tests whether the *Author phase start* is blocked, not just whether an external actor audits the output after the fact. The distinguishing test: does the prompt contain imperative "DO NOT BEGIN until…" language naming the blocking artifacts?

**Formula denominator updated:** `(A + 0.5·Ap)/10` → `/12` to reflect the two added aspirational criteria.
