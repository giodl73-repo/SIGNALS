Written to `simulations/quest/rubrics/trace-permissions-rubric-v1-2026-03-15.md`.

---

**Rubric summary for `trace-permissions`:**

**Essential (4 criteria, 60 pts):**
- C-01: Operation-role matrix — every operation mapped to at least one role
- C-02: Record access scope — org/BU/team/user scope stated explicitly per role
- C-03: Field-level security — 3+ sensitive fields with read/write/deny per role
- C-04: Security gap identification — at least one named gap with role, type, and risk

**Recommended (3 criteria, 30 pts):**
- C-05: Escalation path tracing — role → mechanism → resource, end-to-end
- C-06: Sharing rule conflict analysis — over-exposed records named with the rule causing it
- C-07: Team membership gap analysis — blocked operations due to missing team assignment

**Aspirational (2 criteria, 10 pts):**
- C-08: Remediation guidance — specific fix for every gap (no generic advice)
- C-09: Defense-in-depth assessment — whether role/FLS/record scope each independently enforce

The key design choice: C-04 (gap identification) is essential because without surfacing at least one concrete risk, the output is a description, not a security trace. C-05/C-06/C-07 are recommended because they require deeper analysis that many runs will partially miss. Remediation and layering assessment are aspirational since they go beyond tracing into prescription.
