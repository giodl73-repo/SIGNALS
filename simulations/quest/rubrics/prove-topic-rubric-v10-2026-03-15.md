Written to `simulations/quest/rubrics/prove-topic-rubric-v10-2026-03-16.md`.

---

**v10 summary**

Three new aspirational criteria extracted from Round 10 excellence signals:

| ID | Axis | Pattern | Exemplar |
|----|------|---------|---------|
| **C-31** | Per-stage CE verdict as owned schema field | Named per-stage verdict fields (`s2_ce_verdict`, `s3_ce_verdict`, `s4_ce_verdict`) in the pre-committed schema with CE VERDICT OWNERSHIP TABLE at CAMPAIGN OPEN; `null_tally_final` derivation formula chains through all three named fields explicitly | V-01 |
| **C-32** | Counter-hypothesis declared at Stage 1 and closed at synthesis | `counter_hypothesis:` field in hypothesis artifact; COUNTER-HYPOTHESIS RESOLUTION section at Stage 5 with REFUTED / PARTIALLY REFUTED / OPEN RISK verdict; OPEN RISK mechanically reduces confidence one tier | V-02 |
| **C-33** | Null tally chain reconstructed in ATOMIC DUAL-LOCK | NULL TALLY CHAIN RULE at CAMPAIGN OPEN; ATOMIC DUAL-LOCK block contains NULL TALLY CHAIN reconstruction (S2→N, S3→N, S4→N = null_tally_final) with Stage 4 cross-check producing explicit match/mismatch verdict | V-03 |

**Weight outcome:** Max rises 168 → 180. Aspirational expands to 25 criteria × 4 pts = 100 pts. Golden threshold unchanged at 80.

**Structural note:** C-31/C-32/C-33 form a new **Evidence Chain Integrity** section:
- C-31 extends C-20 + C-26: per-stage CE verdicts become named schema members, closing the opaque-counter gap in `null_tally_final`'s derivation chain
- C-32 extends C-14 + C-17: counter-hypothesis pre-declared at Stage 1 so synthesis closes a declared challenge, not an emergent one; three-verdict classification with OPEN RISK mechanical propagation
- C-33 extends C-18 + C-20: null tally chain echoed inside the ATOMIC DUAL-LOCK with a Stage 4 cross-check, making the lock input auditable in place

A v9-ceiling variation (168/168) can still fail all three: CE verdict fields absent from the schema (C-31 FAIL), no `counter_hypothesis:` at Stage 1 (C-32 FAIL), null tally chain not reconstructed inside the ATOMIC DUAL-LOCK (C-33 FAIL).
