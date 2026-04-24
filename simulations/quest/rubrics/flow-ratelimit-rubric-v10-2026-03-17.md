---

**Three new criteria added (C-27, C-28, C-29). Aspirational pool: 18 → 21. Scoring denominator: `/21`.**

---

**C-27 — UX Template as Named Format Contract Schema** *(V-02 signal)*
C-26 closes the gate-enumeration gap (four fields as individually blocking gate conditions). C-27 closes the Format Contract-level scan-time detection gap: Schema B is declared as a named structural schema in the Format Contract with its own STRUCTURAL REJECTION CLAUSE, making missing UX fields detectable at scan time without reading prose — parallel to Schema A's column-level enforcement. Terminal reconciler must include an explicit Schema B audit as check (d), distinct from the gate audit. Requires C-16, C-19, C-26.

**C-28 — UX Completeness as Named Verdict Claim** *(V-03 signal A)*
Claim (d) in the Verdict block commits to UX template completeness and tier count. This makes UX coverage automatically subject to C-18 bidirectional revision marking and C-22 gate-checkpoint currency — a tier added mid-analysis that lacks full four-field coverage triggers a REVISED marker on Claim (d) at the gate boundary, not only at terminal reconciliation. Without Claim (d), a Verdict-only reader has no visibility into UX commitments or their revisions. Requires C-15, C-18, C-22, C-26.

**C-29 — Six-Item UX Gate with Tier-Count and Structure-Compliance Items** *(V-03 signal B)*
Extends C-26's four-item gate to six explicitly enumerated blocking conditions: the four FIELD conditions plus (e) tier-count verification against the burst path audit section (not merely the two-tier minimum) and (f) structure-compliance confirmation (template structure used, not free prose) as a separately named blocking condition. Eliminates two residual bypass paths the four-item gate leaves open: undercounting tiers and prose-formatting compliant-field tiers. Both (e) and (f) must be named separately — collapsing them into a compound condition does not pass. Requires C-26.
