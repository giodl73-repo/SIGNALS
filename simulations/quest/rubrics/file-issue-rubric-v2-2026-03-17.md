Written to `simulations/quest/rubrics/file-issue-rubric-v2-2026-03-17.md`.

---

**What changed v1 → v2:**

Two new aspirational criteria extracted from Round 1 excellence signals:

**C-10 — Pre-write validation gate** (from V-03)
The FINDINGS phase pattern: a named check phase, separate from drafting, that blocks the artifact write until reproducibility, tone match, and completeness all pass. A post-write summary doesn't qualify — the gate must be structural.

**C-11 — Corrective actions per validation check** (from V-04)
The Maintainer checks pattern: each validation item names not just the condition but the prescribed remedy on failure. "Rewrite title", "Ask user for steps", "Reframe body tone" — the skill knows what to do, not just whether a check passed.

**Scoring formula updated:**
- v1: `aspirational_pass / 2 * 10` (max 5 per criterion)
- v2: `aspirational_pass / 4 * 10` (max 2.5 per criterion)

All four Round 1 golden variations (V-02, V-03, V-04) score **97.5** under v2 — they hit C-08/C-09 but only V-03 and V-04 hit C-10/C-11 respectively. No variation hits all four aspirational criteria, which is correct — the new criteria define the next generation target.
ack/** | behavior | essential | Skill writes or clearly specifies an artifact path under `simulations/feedback/`. Path must be non-ambiguous (includes skill name and date or slug). |

---

## Recommended Criteria (30% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Actionable, specific issue title** | format | recommended | The GitHub issue title names the specific skill and the specific problem — not generic phrases like "Bug report" or "Issue with skill". Pass: title contains skill name + symptom or behavior. |
| C-06 | **Sufficient reproducibility context** | depth | recommended | Body includes enough detail for a maintainer to reproduce or understand the issue: what input was given, what the environment was, or what sequence of events led to the problem. A one-sentence description alone is a fail. |
| C-07 | **Repo open offer presented** | behavior | recommended | Skill explicitly offers to open the issue at the Signal repo (e.g., asks the user if they want to open it, or provides a `gh issue create` command). |

---

## Aspirational Criteria (10% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Severity-appropriate framing** | depth | aspirational | Tone and urgency match severity: `crash` uses urgent language and asks for immediate reproduction steps; `improvement` uses constructive, proposal-oriented framing. A `crash` filed with casual improvement language or vice versa is a fail. |
| C-09 | **Skill context enrichment** | coverage | aspirational | Issue body includes at least one enriching context item beyond the four required fields: skill version or date, related skills in the invocation chain, topic name, or a reference to an existing rubric or golden artifact. |
| C-10 | **Pre-write validation gate** | structure | aspirational | Skill includes a structured check phase — separate from drafting — that verifies reproducibility, tone match, and field completeness before writing the artifact. The gate must block the write step; a post-write summary check does not qualify. (Excellence signal: V-03 FINDINGS phase.) |
| C-11 | **Corrective actions per validation check** | structure | aspirational | Each validation check item includes an explicit corrective action specifying what the skill does on failure (e.g., "Rewrite title to name skill + symptom", "Ask user for reproduction steps", "Reframe body tone to match severity"). A checklist of pass/fail conditions without prescribed remedies does not qualify. (Excellence signal: V-04 Maintainer checks.) |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

### Score bands

| Composite | Verdict |
|-----------|---------|
| >= 80, all essential pass | Golden |
| >= 60, all essential pass | Acceptable |
| Any essential fail | Not acceptable (regardless of composite) |
| < 60 | Not acceptable |

---

## Rationale

- **C-01/C-02** are the core contract of the skill — capturing the right fields in the right vocabulary. Without them the issue is incomplete or unsortable by severity.
- **C-03** ensures the output is actually usable as a GitHub issue, not just a prose description.
- **C-04** closes the loop on local logging, which is an explicit part of the skill's stated purpose.
- **C-05** prevents noise in the issue tracker — vague titles are unfiled in practice.
- **C-06** distinguishes a useful bug report from a throwaway complaint.
- **C-07** verifies the skill follows through on its "offers to open" promise.
- **C-08/C-09** reflect maturity: a skill that calibrates tone to severity and enriches context produces issues that actually get fixed.
- **C-10** reflects structural maturity: a pre-write gate catches quality failures before they are committed to disk, rather than relying on post-hoc review. V-03's FINDINGS phase demonstrated this pattern produces higher-confidence artifacts.
- **C-11** reflects operational maturity: prescribed corrective actions transform validation from a judgment into a procedure. V-04's Maintainer checks demonstrated that naming the fix alongside the check eliminates ambiguity about what the skill should do next.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-10 (pre-write validation gate) and C-11 (corrective actions per check) from Round 1 excellence signals; aspirational denominator updated from 2 to 4 |
