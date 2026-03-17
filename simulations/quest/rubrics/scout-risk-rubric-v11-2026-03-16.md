Three new criteria added to v11:

**C-32 — Interdependency table rows carry a dedicated Trigger Condition field**
Escalates C-17. V-02's Table 3 demonstrates a third typed column alongside From/To: the activation condition for each dependency pair as a named schema field, not embedded prose. Without it, the IF side of every interdependency is interpretable but not column-scannable.

**C-33 — Dimension column vocabulary-constrained at cell level**
Escalates C-06. V-02's column rule `"Exactly one of {Technical, Market, Compliance, Dependency, Timeline}"` is the same pattern as C-22's closed vocabulary for severity. Without it, a model can introduce unlabeled dimensions ("Operational", "Strategic") that pass C-06 but fall outside the register's defined scope.

**C-34 — AMEND confirmation is a structured header block naming suppressed dimensions explicitly**
Escalates C-10. V-01 passes with a loose prose confirmation "at the top." V-02 requires a named header block — both active and suppressed dimensions enumerated by name — making AMEND compliance column-verifiable rather than read-the-prose verifiable.

Max composite: **136 → 142**. Scoring bands shifted +6 at the top end. Escalation ladder populated with all three new rows.
