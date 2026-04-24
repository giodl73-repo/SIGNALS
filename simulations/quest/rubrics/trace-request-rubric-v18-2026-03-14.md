`trace-request-rubric-v18-2026-03-15.md` written. Here is a summary of what changed:

---

## v18 changes from v17

**One new criterion from R19 excellence signals:**

**C-44 — CHECKER ALGORITHM CONSISTENCY-RULE structural derivation token** (Tier B+ promoted)
- Source: V-02 (single-axis CONSISTENCY-RULE) and V-05 (combined) both stably produced a fourth named rule in the CHECKER ALGORITHM block — `CONSISTENCY-RULE` — declaring the machine-verifiable two-branch derivation: `matches HALT-EXPECTED-BOUNDARY: yes` → TRACE CONTRACT validation → "Contract prediction confirmed" and `matches HALT-EXPECTED-BOUNDARY: no` → TRACE CONTRACT validation → "falsified -- actual halt boundary was [BC-N label]"
- V-02's GATE-0B required all four algorithm tokens; V-02's GATE-8H required verbatim reproduction of all four; the derivation is a structural algorithm rule, not a prose instruction in GATE-TC
- Two independent variation axes = sufficient evidence to freeze the surface
- Depends on C-42 AND C-39 AND C-37 (C-42 establishes the source boolean; C-39 establishes the target validation outcome; C-37 establishes the CHECKER ALGORITHM block structure the fourth rule inhabits)

**Scale: 270 → 275** (aspirational: 36 → 37 criteria, 180 → 185 pts). Golden threshold: 220/275 (80%).

**Signal not promoted to v18 — C-45 design surface:**
- GATE-8B VALIDATION-DERIVATION requirement — V-03 isolated a surface where Step 8b derives the TRACE CONTRACT validation outcome inline within the prose block at the point the contradiction event fires (`VALIDATION-DERIVATION: [outcome]` token co-located with DECLARE CONTRADICTION); single-axis evidence only — V-05 combined CONSISTENCY-RULE without VALIDATION-DERIVATION; second independent axis needed before the surface can be frozen
