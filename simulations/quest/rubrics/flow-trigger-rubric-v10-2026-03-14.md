Here is the complete updated rubric:

---

# Flow-Trigger Skill — Evaluation Rubric (v10)

Three new aspirational criteria extracted from R13 variation comparisons:

---

**C-27 — Remediation Orphan Detection Gate** *(R13 V-03)*

Signal: V-03 introduced a named "Remediation Coverage Gate" (Phase 4B) between pathology verdicts and the certificate. The design exposed a failure class that no prior variation named: an IF-* label with a DETECTED/INDETERMINATE verdict but no remediation entry. Existing criteria (C-08, C-19) require remediations to be present and complete — but neither criterion requires a named gated artifact that flags their *absence* before the certificate issues. V-03 got C-26 PARTIAL precisely because Phase 4B doesn't consolidate all four C-26 dimensions, but the remediation-orphan gate itself is a new structural pattern worth formalizing independently.

**C-28 — Certificate Owner–Data Producer Separation** *(R13 V-01/V-04)*

Signal: V-02 scored PARTIAL on C-26 because "the final certificate has no explicit designated owner separate from the chain producer; self-attestation risk remains." V-01 and V-04 both define Role 5 Audit Analyst with an explicit mandate: "does not evaluate evidence, modify verdicts, or add analysis." The lesson: C-26 can be structurally complete and still self-attest. The certificate owner's independence from the verdict producer must be a named, declared role boundary — not inferred from audit behavior. This is what separates V-04 (100.00) from V-02 (99.74).

**C-29 — Verbatim-Chain Cross-Block Traceability** *(R13 V-02)*

Signal: V-02's CHAIN-LINK-* architecture extends C-24 (verbatim-emit caption) from a single enforcement instruction into a networked dependency graph. Each block emits named key-value data (`PCR_STORM_STATUS=CLOSED`); downstream schemas reference those keys explicitly (`read PCR_STORM_STATUS from CHAIN-LINK-PCR <- required`). The new property: a missing verbatim block produces a **named reference gap** in a downstream schema — detectable without reading upstream prose. Verbatim captions that carry human-readable summaries without machine-readable key-value data (which most prior variations produce) do not satisfy this criterion.

---

**Denominator update**: /19 → /22. Formula:

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)
```

**R13 retroactive scores under v10:**

| Variation | Aspirational (v9 /19) | C-27 | C-28 | C-29 | Aspirational (v10 /22) | Composite |
|-----------|----------------------|------|------|------|------------------------|-----------|
| V-01 | 17.0 / 19 | FAIL | PASS | FAIL | 18.0 / 22 × 10 = 8.18 | 98.18 |
| V-02 | 18.5 / 19 | FAIL | FAIL | PASS | 19.5 / 22 × 10 = 8.86 | 98.86 |
| V-03 | 16.5 / 19 | PASS | FAIL | FAIL | 17.5 / 22 × 10 = 7.95 | 97.95 |
| V-04 | 19.0 / 19 | FAIL | PASS | PASS | 21.0 / 22 × 10 = 9.55 | 99.55 |

V-04 no longer scores 100 under v10 — it misses C-27 (no remediation coverage gate). The next variation that earns all 22 aspirational criteria would need to combine V-03's gate + V-04's role separation + V-02's chain traceability simultaneously.

File written to `simulations/quest/rubrics/flow-trigger-rubric-v10-2026-03-15.md`.
