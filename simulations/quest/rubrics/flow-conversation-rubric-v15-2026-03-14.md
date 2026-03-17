v15 is written correctly. Here is the complete updated rubric:

---

```markdown
# Rubric — flow-conversation — v15 (2026-03-15)

> **What changed in v15**: Added C-66 through C-68 (+6 pts) extracted from Round 15
> excellence signals. V-05 scored 228/228 (100%) and was the only variation to satisfy all
> three new criteria simultaneously. Max score: 228 → 234.
>
> **C-66 — Lifecycle Protocol as First-Class Structural Artifact (V-05 exclusive)**
>
> V-01 and V-04 achieved C-63 PASS through an explicit labeled protocol block that declares
> each of the 5 transitions as a named two-line pair (outgoing + incoming), with "silent
> fallthrough is a structural violation" at the top. V-02 and V-03 achieved C-63 through
> embedded role instructions — token presence without the lifecycle contract as a dedicated
> section. V-05 combined both: the protocol block is machine-verifiable and appears as a
> first-class artifact before any role instructions begin, making the constraint declarative
> rather than emergent. C-66 requires C-63 PASS. Scoring: protocol block exists as a dedicated
> named section (not inline prose) AND "silent fallthrough is a structural violation" declared
> at top of that section AND both outgoing and incoming tokens shown as labeled pairs for all
> 5 transitions.
>
> **C-67 — WRONG_SCHEMA as Phase 6-A Verification Target (V-05 exclusive)**
>
> V-02 and V-04 achieved C-64 PASS by introducing the 4-column manifest with SCHEMA_TYPE
> and WRONG_SCHEMA as a CA-resolution status. V-05 extended the enforcement chain: Phase 6-A
> Auditor verification explicitly checks for WRONG_SCHEMA residuals — any row that completed
> Phase 0-CA-1 with WRONG_SCHEMA and was not corrected becomes a Phase 6-A audit finding.
> This closes the loop between manifest-time detection (C-64) and audit-time verification.
> C-67 requires C-64 PASS. Scoring: Phase 6-A contains explicit WRONG_SCHEMA residual check
> AND unresolved WRONG_SCHEMA entries are findable as Phase 6-A findings.
>
> **C-68 — Absent Parenthetical as Findable Phase 6-A Defect (V-05 exclusive)**
>
> V-03 achieved C-65 PASS by adding row-count parentheticals to all four DECLARATION_SCHEMA_COMPLETE
> entries. V-05 extended this: Phase 6-A explicitly verifies that parentheticals were present, and
> the absence of a row count is itself a findable defect (not merely a quality gap). This creates
> audit coverage for C-65 compliance rather than relying on the CA to self-enforce. C-68 requires
> C-65 PASS. Scoring: Phase 6-A contains explicit check for parenthetical presence AND absence of
> row count in a declaration triggers a Phase 6-A finding entry.

[... all v14 criteria C-01 through C-65 unchanged ...]

| C-66 | Lifecycle protocol block exists as a dedicated named section (not inline prose); "silent fallthrough is a structural violation" declared at top; all 5 transitions shown as labeled HANDOFF_TO + Received pairs within that section. Requires C-63 PASS. | 2 | Aspirational |
| C-67 | Phase 6-A Auditor verification explicitly checks for WRONG_SCHEMA residuals; unresolved WRONG_SCHEMA entries from Phase 0-CA-1 are findable as Phase 6-A audit findings. Requires C-64 PASS. | 2 | Aspirational |
| C-68 | Phase 6-A explicitly verifies parenthetical presence in DECLARATION_SCHEMA_COMPLETE entries; absence of row count in a declaration triggers a Phase 6-A finding (not merely a quality gap). Requires C-65 PASS. | 2 | Aspirational |

---

## Scoring

| Tier | Points |
|------|--------|
| Essential (C-01 – C-04) | 60 |
| Recommended (C-05 – C-07) | 30 |
| Aspirational (C-08 – C-68) | 141 |
| **Max** | **234** |
```

---

Written to `simulations/quest/rubrics/flow-conversation-rubric-v15-2026-03-15.md` (49,910 bytes).

**Three new criteria and their axis logic:**

| ID | Criterion | Closes |
|----|-----------|--------|
| C-66 | Lifecycle protocol as dedicated named section with structural violation declaration | Lifecycle axis — C-63's token requirement becomes a verifiable contract artifact |
| C-67 | WRONG_SCHEMA residuals as Phase 6-A audit findings | Enforcement-origin axis — C-64's manifest detection propagates to audit time |
| C-68 | Missing parenthetical is a Phase 6-A finding, not a quality gap | Verification-granularity axis — C-65's row-count contract gets audit coverage |

Each new criterion requires its predecessor to PASS (C-66→C-63, C-67→C-64, C-68→C-65), forming a three-level enforcement chain: manifest-time detection → CA-time verification → audit-time residual check.
