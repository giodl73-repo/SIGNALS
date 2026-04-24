Done. `review-users-rubric-v2-2026-03-14.md` is written with:

**3 new aspirational criteria:**

| # | Name | Source | Mechanism |
|---|------|--------|-----------|
| C-11 | Score table pre-committed before narrative | R1 V-02 | Table appears first — C-01/C-02 structurally unfailable |
| C-12 | Named-character grounding per persona | R1 V-04 | "Sam has 10 minutes" drives naturalistic first-person; strongest C-06 driver |
| C-13 | Inertia fields per persona | R1 V-05 | Explicit beats/loses fields make conflict detection mechanistic; strongest C-08 driver |

**Formula update:** aspirational pool grows from 2 to 5 — denominator changes from `/2 * 10` to `/5 * 10`. Total still sums to 100.

**R2 combination target** (from scorecard): V-02 pre-committed table + V-04 named characters + V-03 per-category quotes inside narrative prose + V-05 inertia fields. A variation hitting all four should score 100 and satisfy C-11, C-12, C-13 simultaneously.
e prose
- C-12: Named-character grounding per persona
- C-13: Inertia fields per persona (beats/loses vs current process)

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Essential Criteria

*All five must pass. Any essential failure = Reject.*

### C-01 — All 5 Stock Personas Present
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Output contains a section for each of the five stock personas: Maker, Developer, Compliance, Supervisor, Operator. A missing persona (or a persona renamed beyond recognition) fails this criterion.

### C-02 — Each Persona Gives a 1-5 Usability Score
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Each persona section states a single integer score on the 1-5 scale (e.g., "Score: 3/5"). All 5 scores must be present; a range, a label, or "N/A" fails.

### C-03 — Each Persona Quotes Exact Text from the Target Artifact
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Each persona section contains at least one direct quotation -- verbatim text in quotes or a blockquote -- pulled from the artifact under review. Paraphrase without a quote fails.

### C-04 — Cross-Persona Synthesis Is Present
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Output contains a synthesis section (titled or clearly delimited) that identifies at least one finding shared by 3 or more personas (universal friction). A list of per-persona summaries without synthesis fails.

### C-05 — Aggregate Usability Score Is Computed
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Output states a single aggregate usability score derived from the 5 individual scores (mean, weighted average, or explicit formula). No aggregate score fails.

---

## Recommended Criteria

*Output is better with these.*

### C-06 — First-Person Narrative Voice Per Persona
- **Category**: format
- **Weight**: recommended
- **Pass condition**: Each persona section is written in first person ("I clicked...", "I read...", "I asked..."). Third-person narration ("The Maker found...") fails this criterion.

### C-07 — Role-Specific Friction Distinguished from Universal
- **Category**: depth
- **Weight**: recommended
- **Pass condition**: The synthesis section explicitly separates friction that affected only one or two personas (role-specific) from friction that affected 3+ personas (universal). A flat list with no distinction fails.

### C-08 — Persona Conflicts Identified
- **Category**: depth
- **Weight**: recommended
- **Pass condition**: The synthesis section calls out at least one case where a design choice that helped one persona created friction for another (e.g., "what Supervisor needed for audit trails added steps Maker could not handle alone"). Absence of conflict analysis fails if conflicts exist in the individual scores.

---

## Aspirational Criteria

*Raise the bar once essential/recommended are stable.*

### C-09 — Friction Typed by Category
- **Category**: depth
- **Weight**: aspirational
- **Pass condition**: Each friction finding is tagged with one of the four signal types: confusion, friction, fear, or jargon. Output that lists findings without tagging type fails this criterion.

### C-10 — Amend Loop Triggered Correctly
- **Category**: behavior
- **Weight**: aspirational
- **Pass condition**: If any persona score is below 3/5, the output includes an explicit amend proposal -- a concrete change to the artifact that would raise that persona's score -- and re-scores. If no persona is below 3/5 this criterion passes automatically. Amend loop omitted when a sub-3 score exists fails.

### C-11 — Score Table Pre-Committed Before Narrative
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 V-02 excellence signal
- **Pass condition**: Output opens with a score summary table listing all 5 persona scores before any per-persona narrative prose begins. The table must appear as the first substantive output block. Per-persona scores written only within narrative sections (not pre-committed) fail this criterion.
- **Rationale**: Committing all scores upfront prevents post-hoc score rationalization and makes C-01/C-02 structurally unfailable regardless of model behavior in the narrative section.

### C-12 — Named-Character Grounding Per Persona
- **Category**: format
- **Weight**: aspirational
- **Source**: R1 V-04 excellence signal
- **Pass condition**: Each persona section introduces a named character with a concrete situational detail before the walkthrough begins (e.g., "Jordan, a Compliance officer preparing for a quarterly audit, opens the spec..."). A persona section that addresses the role generically ("The Compliance persona...") without a named character fails this criterion.
- **Rationale**: Named characters make first-person narration feel natural to the model; third-person drift is less likely when writing *as Sam* than writing *as Developer*. This is the strongest structural driver of C-06 compliance.

### C-13 — Inertia Fields Per Persona
- **Category**: depth
- **Weight**: aspirational
- **Source**: R1 V-05 excellence signal
- **Pass condition**: Each persona section includes two explicit inertia fields: (1) "Beats current process:" stating what the artifact does better than the status quo for this persona, and (2) "Loses to current process:" stating where the artifact is worse. Persona sections that discuss adoption without explicit beats/loses fields fail this criterion.
- **Rationale**: Inertia fields produce conflict detection by field comparison -- the synthesis can mechanically identify personas whose "beats" align with another's "loses" -- rather than relying on the model to synthesize conflicts from free-form prose. Strongest structural driver of C-08 compliance.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Outcome | Meaning |
|---------|---------|
| All essential pass + composite >= 80 | Golden -- accept |
| All essential pass + composite < 80 | Silver -- recommended gaps only |
| Any essential fails | Reject -- not useful |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria (5 essential, 3 recommended, 2 aspirational) |
| v2 | 2026-03-14 | Added C-11 (pre-committed score table), C-12 (named-character grounding), C-13 (inertia fields) from R1 excellence signals; aspirational formula updated to /5 |
