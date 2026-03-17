Rubric written to `simulations/quest/rubrics/review-users-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (5) — must all pass:**
- C-01: All 5 stock personas present (Maker, Developer, Compliance, Supervisor, Operator)
- C-02: Each persona gives a 1-5 usability score
- C-03: Each persona quotes exact text from the target artifact
- C-04: Cross-persona synthesis present with universal friction (3+ personas)
- C-05: Aggregate usability score computed

**Recommended (3):**
- C-06: First-person narrative voice per persona
- C-07: Role-specific friction distinguished from universal
- C-08: Persona conflicts identified (what helps one hurts another)

**Aspirational (2):**
- C-09: Friction typed by category (confusion/friction/fear/jargon)
- C-10: Amend loop triggered correctly when any score < 3/5

**Golden threshold**: all 5 essential pass + composite >= 80.

The trace artifact drove the essential criteria directly — the Developer finding (stub body, generic output), the Compliance gap (no data-handling brief), and the Supervisor audit-trail/gate tension all informed what the synthesis section must surface.
re: 3/5"). All 5 scores must be present; a range, a label, or "N/A" fails.

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

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Outcome | Meaning |
|---------|---------|
| All essential pass + composite >= 80 | Golden -- accept |
| All essential pass + composite < 80 | Silver -- recommended gaps only |
| Any essential fails | Reject -- not useful |
