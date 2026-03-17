`review-users-rubric-v3-2026-03-14.md` written. Here's what changed:

**2 new aspirational criteria:**

| # | Name | Source | Mechanism |
|---|------|--------|-----------|
| C-14 | Current-workaround context field | R2 Signal 1 | "What [Name] does today instead:" field *before* the walkthrough — grounds Beats/Loses in a named alternative; strongest actionable C-10 driver |
| C-15 | Inline friction tags in first-person sentences | R2 Signal 2 | Tags embedded inside first-person sentences ("I read X and (confusion)...") — resolves R1 C-06/C-09 tension, no format switching needed |

**C-09 tightened:** pass condition now requires the correct/wrong contrast block. PARTIAL for inline tagging without contrast examples (the R2 V-02/V-03 failure mode). Full PASS requires the block.

**Formula update:** aspirational denominator grows from `/5 * 10` to `/7 * 10`.

**R3 target:** a variation hitting all seven aspirationals needs: pre-committed table (C-11) + named character + current-workaround field (C-12, C-14) + inline tags with contrast block (C-09, C-15) + Beats/Loses fields (C-13) + amend loop grounded in the named workaround (C-10). All five mechanisms reinforce each other — no format switching required at any step.
 character + inline tag + inertia fields are structurally compatible (V-05)**

The R1 tension between C-06 and C-09 was structural: sub-section friction typing required analytical mode, which broke first-person voice. V-05 resolved this because all three mechanisms pull in the same direction when combined: named character grounding makes first-person feel natural, inline tags fit inside first-person sentences, and inertia fields follow naturally from "what Sam does today." No format switching needed.

**R2 C-09 tightening — contrast block required for PASS**

R2 showed PARTIAL in V-02 and V-03 where the friction-tag mechanic was stated but no correct/wrong contrast examples were provided. V-01, V-04, V-05 all provided the contrast block and scored PASS. C-09 pass condition is now updated to require the contrast block.

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

### C-09 — Friction Typed by Category with Contrast Block
- **Category**: depth
- **Weight**: aspirational
- **Source**: v1 baseline; tightened in v3 from R2 evidence
- **Pass condition**: Each friction finding is tagged with one of the four signal types: confusion, friction, fear, or jargon. The skill prompt or output must include a correct/wrong contrast block demonstrating the tag mechanic:
  > Correct: I read "deploy on merge" and (confusion) had no idea which merge this meant.
  > Wrong: **Confusion findings:** "deploy on merge" -- the persona did not understand this.
  Output that tags inline without providing the contrast block scores PARTIAL. Output that lists findings without any tagging fails entirely.
- **Rationale**: R2 showed PARTIAL in V-02 and V-03 where the mechanic was stated once in a bullet list without contrast examples. The contrast block names the failure mode explicitly, making the criterion structurally unfailable.

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

### C-14 — Pre-Walkthrough "Current Workaround" Context Field Per Persona
- **Category**: depth
- **Weight**: aspirational
- **Source**: R2 V-05 excellence signal
- **Pass condition**: Each persona section includes a named "What [Name] does today instead:" field *before* the walkthrough narrative begins, describing the manual workaround or alternative tool the persona currently uses when this feature doesn't exist. A persona section that omits this field, or that mentions current behavior only inside the narrative prose, fails this criterion.
- **Rationale**: Grounding the persona in their named current alternative changes the character of the Beats/Loses output from abstract scoring to concrete comparison. Amend-loop proposals become actionable because they close a named gap ("Sam currently exports to CSV and reformats manually") rather than an abstract usability problem. This is the strongest driver of actionable C-10 amend proposals.

### C-15 — Inline Friction Tags in First-Person Sentences
- **Category**: format
- **Weight**: aspirational
- **Source**: R2 V-05 excellence signal
- **Pass condition**: Friction tags appear embedded inside first-person sentences rather than in separate categorized sub-sections. The correct form is: "I read 'deploy on merge' and (confusion) had no idea which merge this meant." The failing form is a separate "Confusion findings:" block after the first-person narrative. A section that uses analytical sub-sections for friction types -- even if C-09 tags are present -- fails this criterion.
- **Rationale**: Resolves the R1 structural tension between C-06 (first-person voice) and C-09 (friction typing). Sub-section typing required analytical mode, which broke first-person narration. Inline tagging is structurally compatible with first-person prose: writing *as Sam* produces "I read X and (confusion)..." naturally. When C-12 (named characters), C-09 (inline tags with contrast block), and C-13 (inertia fields) are all present, they reinforce rather than compete -- no format switching is needed.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Outcome | Meaning |
|---------|---------|
| All essential pass + composite >= 80 | Golden -- accept |
| All essential pass + composite < 80 | Silver -- recommended gaps only |
| Any essential fails | Reject -- not useful |

---

## Aspirational Criteria Summary

| # | Name | Source | Key Mechanism |
|---|------|--------|---------------|
| C-09 | Friction typed with contrast block | v1 baseline (tightened v3) | Correct/wrong examples make tag mechanic structurally unfailable |
| C-10 | Amend loop triggered correctly | v1 baseline | Re-score when sub-3 score exists |
| C-11 | Score table pre-committed | R1 V-02 | Upfront table locks C-01/C-02 before narrative begins |
| C-12 | Named-character grounding | R1 V-04 | Named character drives naturalistic first-person; strongest C-06 driver |
| C-13 | Inertia fields (Beats/Loses) | R1 V-05 | Field comparison enables mechanistic conflict detection; strongest C-08 driver |
| C-14 | Current-workaround context field | R2 V-05 | Pre-walkthrough named alternative grounds Beats/Loses in specifics; strongest actionable C-10 driver |
| C-15 | Inline tags in first-person sentences | R2 V-05 | Resolves C-06/C-09 tension; tags inside narrative, no format switching |

---

## R3 Target Combination

A variation hitting all seven aspirationals must satisfy:
1. Pre-committed score table (C-11)
2. Named character with scenario brief + "What [Name] does today instead:" field (C-12, C-14)
3. Inline friction tags with contrast block inside first-person prose (C-09, C-15)
4. Beats/Loses fields after walkthrough (C-13)
5. Amend loop grounded in the named current workaround (C-10)

The five mechanisms are structurally compatible: named character grounding makes first-person natural, "current workaround" field gives the comparison baseline, inline tags fit inside first-person sentences, inertia fields follow mechanically from the baseline, and the amend loop closes the named gap. No format switching needed at any step.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria (5 essential, 3 recommended, 2 aspirational) |
| v2 | 2026-03-14 | Added C-11 (pre-committed score table), C-12 (named-character grounding), C-13 (inertia fields) from R1 excellence signals; aspirational formula updated to /5 |
| v3 | 2026-03-14 | Added C-14 (current-workaround context field), C-15 (inline tags in first-person sentences) from R2 excellence signals; tightened C-09 pass condition to require contrast block; aspirational formula updated to /7 |
