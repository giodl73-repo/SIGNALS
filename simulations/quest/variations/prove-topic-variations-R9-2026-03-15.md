Written to `simulations/quest/golden/prove-topic-variate-R9-2026-03-15.md`.

---

## Round 9 Summary

**Anchor from R8:** V-05 (156/156 under v8, satisfies all C-01..C-27)

**Four new axes targeted** — all patterns present in R8 V-05 but exceeding any v8 criterion:

| Variation | Axis | What it closes |
|-----------|------|----------------|
| **V-01** | Schema self-registration | `schema_compliance_confirmed` pre-declared as field 9 in the CAMPAIGN OPEN schema. C-26 requires a compliance check at synthesis; it does not require the compliance-check field to be a pre-committed schema member. Dropping field 9 from synthesis is now a schema violation detectable from CAMPAIGN OPEN alone. |
| **V-02** | Symmetric independence chain | `co_activation_confirmed` gets a full `positive_derivation` + `independence_chain` record, mirroring the C-27 structure on `incumbent_defense_closed`. C-27 covers only one direction. Both campaign-sensitive fields now carry mutual independence proofs readable without dual-lock domain knowledge. |
| **V-03** | Per-stage schema integrity count | Each evidence stage appends a `SCHEMA INTEGRITY NOTE` with `N/N fields locked — no additions, no omissions since CAMPAIGN OPEN`. Symmetric to C-20's per-stage null tally chain. Makes the schema contract auditable across the collection phase, not just at CAMPAIGN OPEN and synthesis. |
| **V-04** | Annotation rule pre-committed | `SESSION INVARIANT C` declared at CAMPAIGN OPEN with invariant language. ROLE A covers all four invariants. `annotation_rule_active: true` in hypothesis frontmatter. Synthesis EXECUTES the rule, does not declare it. C-25 requires the rule at synthesis; this moves it to a pre-Stage-0 session obligation. |
| **V-05** | Full compound | All four R9 axes + full R8 V-05 base. 156/156 under v8 + all four R9 gaps closed. Candidate ceiling for v9. |
