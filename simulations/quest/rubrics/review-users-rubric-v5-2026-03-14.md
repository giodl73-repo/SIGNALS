`review-users-rubric-v5-2026-03-14.md` written. Here's what changed:

**3 new aspirational criteria from R4 excellence signals:**

| # | Name | Source | Mechanism |
|---|------|--------|-----------|
| C-19 | Numbered step sequence for workaround-before-brief | R4 V-04/V-05 | Numbered steps make C-16 a sequence rule, not a layout convention; a model cannot place Step 2 before Step 1, closing the last model-reordering risk |
| C-20 | Domain-matched per-section contrast examples | R4 V-05 | Each persona section's contrast block uses friction from that persona's role domain -- role-specific prototype at the exact boundary where narration begins, not a generic example from 3000 tokens prior |
| C-21 | Explicit gap-statement in amend template | R4 V-03/V-05 | "What the workaround provides that the artifact does not:" field between workaround slot and proposed change -- forces workaround-replacement argument framing, closes the generic-remediation residue left by C-18 alone |

**Formula update:** `/10 * 10` -> `/13 * 10`. Max aspirational contribution stays capped at 10 points.

**Criterion lineage:** each R4 criterion is a precision upgrade of an R3 criterion:
- C-19 upgrades C-16 (convention -> rule)
- C-20 upgrades C-17 (generic examples -> domain-matched examples)
- C-21 upgrades C-18 (slot present -> slot + explicit gap articulation)

**R5 target combination:** five mechanism groups unchanged in structure, each now with a tighter inner mechanism:
1. Pre-committed table (C-11)
2. Named character + workaround-first + **numbered steps** (C-12, C-14, C-16, C-19)
3. Per-section contrast blocks + inline tags + **domain-matched examples** (C-09, C-15, C-17, C-20)
4. Beats/Loses fields (C-13)
5. Amend loop with workaround slot + **explicit gap-statement** (C-10, C-18, C-21)
**C-21**)

The three R4 criteria each target a specific failure mode: C-19 closes the last model-reordering risk for C-16 (field-position convention allows reordering; numbered steps do not); C-20 closes the domain-drift risk for C-17 (generic examples at persona boundaries leave the model without a role-specific prototype); C-21 closes the generic-remediation residue in C-18 (naming the workaround is necessary but not sufficient -- the model must also articulate the specific value gap before proposing a change).

---

## Essential Criteria

*All five must pass. Any essential failure = Reject.*

### C-01 -- All 5 Stock Personas Present
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Output contains a section for each of the five stock personas: Maker, Developer, Compliance, Supervisor, Operator. A missing persona (or a persona renamed beyond recognition) fails this criterion.

### C-02 -- Each Persona Gives a 1-5 Usability Score
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Each persona section states a single integer score on the 1-5 scale (e.g., "Score: 3/5"). All 5 scores must be present; a range, a label, or "N/A" fails.

### C-03 -- Each Persona Quotes Exact Text from the Target Artifact
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Each persona section contains at least one direct quotation -- verbatim text in quotes or a blockquote -- pulled from the artifact under review. Paraphrase without a quote fails.

### C-04 -- Cross-Persona Synthesis Is Present
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Output contains a synthesis section (titled or clearly delimited) that identifies at least one finding shared by 3 or more personas (universal friction). A list of per-persona summaries without synthesis fails.

### C-05 -- Aggregate Usability Score Is Computed
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Output states a single aggregate usability score derived from the 5 individual scores (mean, weighted average, or explicit formula). No aggregate score fails.

---

## Recommended Criteria

*Output is better with these.*

### C-06 -- First-Person Narrative Voice Per Persona
- **Category**: format
- **Weight**: recommended
- **Pass condition**: Each persona section is written in first person ("I clicked...", "I read...", "I asked..."). Third-person narration ("The Maker found...") fails this criterion.

### C-07 -- Role-Specific Friction Distinguished from Universal
- **Category**: depth
- **Weight**: recommended
- **Pass condition**: The synthesis section explicitly separates friction that affected only one or two personas (role-specific) from friction that affected 3+ personas (universal). A flat list with no distinction fails.

### C-08 -- Persona Conflicts Identified
- **Category**: depth
- **Weight**: recommended
- **Pass condition**: The synthesis section calls out at least one case where a design choice that helped one persona created friction for another (e.g., "what Supervisor needed for audit trails added steps Maker could not handle alone"). Absence of conflict analysis fails if conflicts exist in the individual scores.

---

## Aspirational Criteria

*Raise the bar once essential/recommended are stable.*

### C-09 -- Friction Typed by Category with Contrast Block
- **Category**: depth
- **Weight**: aspirational
- **Source**: v1 baseline; tightened in v3 from R2 evidence
- **Pass condition**: Each friction finding is tagged with one of the four signal types: confusion, friction, fear, or jargon. The skill prompt or output must include a correct/wrong contrast block demonstrating the tag mechanic:
  > Correct: I read "deploy on merge" and (confusion) had no idea which merge this meant.
  > Wrong: **Confusion findings:** "deploy on merge" -- the persona did not understand this.
  Output that tags inline without providing the contrast block scores PARTIAL. Output that lists findings without any tagging fails entirely.
- **Rationale**: R2 showed PARTIAL in V-02 and V-03 where the mechanic was stated once in a bullet list without contrast examples. The contrast block names the failure mode explicitly, making the criterion structurally unfailable.

### C-10 -- Amend Loop Triggered Correctly
- **Category**: behavior
- **Weight**: aspirational
- **Pass condition**: If any persona score is below 3/5, the output includes an explicit amend proposal -- a concrete change to the artifact that would raise that persona's score -- and re-scores. If no persona is below 3/5 this criterion passes automatically. Amend loop omitted when a sub-3 score exists fails.

### C-11 -- Score Table Pre-Committed Before Narrative
- **Category**: structure
- **Weight**: aspirational
- **Source**: R1 V-02 excellence signal
- **Pass condition**: Output opens with a score summary table listing all 5 persona scores before any per-persona narrative prose begins. The table must appear as the first substantive output block. Per-persona scores written only within narrative sections (not pre-committed) fail this criterion.
- **Rationale**: Committing all scores upfront prevents post-hoc score rationalization and makes C-01/C-02 structurally unfailable regardless of model behavior in the narrative section.

### C-12 -- Named-Character Grounding Per Persona
- **Category**: format
- **Weight**: aspirational
- **Source**: R1 V-04 excellence signal
- **Pass condition**: Each persona section introduces a named character with a concrete situational detail before the walkthrough begins (e.g., "Jordan, a Compliance officer preparing for a quarterly audit, opens the spec..."). A persona section that addresses the role generically ("The Compliance persona...") without a named character fails this criterion.
- **Rationale**: Named characters make first-person narration feel natural to the model; third-person drift is less likely when writing *as Sam* than writing *as Developer*. This is the strongest structural driver of C-06 compliance.

### C-13 -- Inertia Fields Per Persona
- **Category**: depth
- **Weight**: aspirational
- **Source**: R1 V-05 excellence signal
- **Pass condition**: Each persona section includes two explicit inertia fields: (1) "Beats current process:" stating what the artifact does better than the status quo for this persona, and (2) "Loses to current process:" stating where the artifact is worse. Persona sections that discuss adoption without explicit beats/loses fields fail this criterion.
- **Rationale**: Inertia fields produce conflict detection by field comparison -- the synthesis can mechanically identify personas whose "beats" align with another's "loses" -- rather than relying on the model to synthesize conflicts from free-form prose. Strongest structural driver of C-08 compliance.

### C-14 -- Pre-Walkthrough "Current Workaround" Context Field Per Persona
- **Category**: depth
- **Weight**: aspirational
- **Source**: R2 V-05 excellence signal
- **Pass condition**: Each persona section includes a named "What [Name] does today instead:" field *before* the walkthrough narrative begins, describing the manual workaround or alternative tool the persona currently uses when this feature doesn't exist. A persona section that omits this field, or that mentions current behavior only inside the narrative prose, fails this criterion.
- **Rationale**: Grounding the persona in their named current alternative changes the character of the Beats/Loses output from abstract scoring to concrete comparison. Amend-loop proposals become actionable because they close a named gap ("Sam currently exports to CSV and reformats manually") rather than an abstract usability problem. This is the strongest driver of actionable C-10 amend proposals.

### C-15 -- Inline Friction Tags in First-Person Sentences
- **Category**: format
- **Weight**: aspirational
- **Source**: R2 V-05 excellence signal
- **Pass condition**: Friction tags appear embedded inside first-person sentences rather than in separate categorized sub-sections. The correct form is: "I read 'deploy on merge' and (confusion) had no idea which merge this meant." The failing form is a separate "Confusion findings:" block after the first-person narrative. A section that uses analytical sub-sections for friction types -- even if C-09 tags are present -- fails this criterion.
- **Rationale**: Resolves the R1 structural tension between C-06 (first-person voice) and C-09 (friction typing). Sub-section typing required analytical mode, which broke first-person narration. Inline tagging is structurally compatible with first-person prose: writing *as Sam* produces "I read X and (confusion)..." naturally. When C-12 (named characters), C-09 (inline tags with contrast block), and C-13 (inertia fields) are all present, they reinforce rather than compete -- no format switching is needed.

### C-16 -- Workaround-First Ordering (Before Scenario Brief)
- **Category**: structure
- **Weight**: aspirational
- **Source**: R3 V-01, V-05 excellence signal
- **Pass condition**: The "What [Name] does today instead:" field (C-14) appears *before* the scenario brief, not merely before the walkthrough narrative. The ordering must be: workaround field -> scenario brief -> walkthrough. A persona section that places the workaround after the scenario brief -- even if before the walkthrough -- fails this criterion.
- **Rationale**: Placing the workaround before the scenario brief creates a comparison cascade: the named alternative is the freshest context when the model writes the character scenario, so the scenario brief naturally incorporates the alternative (e.g., "Sam, who currently exports to CSV..."). When the workaround comes after the scenario brief, the comparison framing arrives too late to influence character construction. R3 V-01 and V-05 produced stronger character-scenario integration than V-02 and V-03 (which placed the field after the brief) precisely because of this ordering.

### C-17 -- Per-Section Contrast Blocks
- **Category**: structure
- **Weight**: aspirational
- **Source**: R3 V-02, V-05 excellence signal
- **Pass condition**: The friction-tag contrast block (correct/wrong examples) appears inside each individual persona section, not only in a global preamble or skill-level instruction. Each persona section must contain its own correct/wrong example pair demonstrating the inline tag mechanic. A single global block at the prompt level with no per-section repetition fails this criterion.
- **Rationale**: A global contrast block placed once at the top of a long multi-persona output is far enough from the 4th and 5th persona sections that the model may revert to the analytical sub-section failure mode. Per-section blocks enforce the mechanic at every persona boundary. R3 V-02 (role-appropriate pair per section) and V-05 (three correct examples per section) showed that per-section placement is the strongest structural enforcement of C-09 compliance across the full output -- not just in the first persona.

### C-18 -- Named-Workaround Slot in Amend Template
- **Category**: behavior
- **Weight**: aspirational
- **Source**: R3 V-03, V-05 excellence signal
- **Pass condition**: When the amend loop is triggered (C-10), the amend proposal template includes an explicit named-workaround input slot: a field that captures "Sam currently [workaround]" before stating the proposed change. An amend proposal that refers only to abstract usability reasoning ("this step is too complex") without anchoring to the named workaround from C-14 fails this criterion. If C-10 passes automatically (no sub-3 score), this criterion passes automatically.
- **Rationale**: Amend proposals without a workaround anchor produce generic remediation ("simplify step 3"). Proposals anchored to a named workaround produce targeted remediation ("Sam currently exports to CSV and reformats manually -- the feature can eliminate this by providing a one-click export that matches her format"). The named-workaround slot in the template structurally prevents the generic case: the model must fill the slot before stating the proposed change. R3 V-03 and V-05 produced more actionable amend proposals than V-01/V-02/V-04 because the template required the workaround as input to the proposal, not just as context.

### C-19 -- Numbered Step Sequence for Workaround-Before-Brief
- **Category**: structure
- **Weight**: aspirational
- **Source**: R4 V-04, V-05 excellence signal
- **Pass condition**: The persona section structure uses an explicit numbered step sequence in which Step 1 is the workaround field and Step 2 is the scenario brief (e.g., "Step 1 -- Current workaround: ... Step 2 -- Scenario: ... Step 3 -- Walkthrough: ..."). A persona template that states the workaround-before-brief ordering as a prose instruction or field-position convention without numbered steps fails this criterion.
- **Rationale**: C-16 establishes that the workaround must precede the scenario brief, but a layout convention (e.g., "workaround field appears before the scenario heading") still allows a model to reorder when not strictly following the template. Numbered steps make ordering a sequence rule: there is no valid interpretation that places Step 2 before Step 1. R4 V-04 and V-05 used numbered step sequences and showed stronger character-scenario integration than V-02/V-03 (which used field-position convention) because the model could not reorder without violating an explicit sequential constraint. This closes the last model-reordering risk for C-16.

### C-20 -- Domain-Matched Per-Section Contrast Examples
- **Category**: format
- **Weight**: aspirational
- **Source**: R4 V-05 excellence signal
- **Pass condition**: Each persona section's contrast block contains at least one correct/wrong example pair drawn from friction in that persona's role domain (e.g., audit-trail friction in the Compliance block, deployment friction in the Developer block, approval-workflow friction in the Supervisor block). A contrast block that uses a generic, domain-agnostic example identical across all persona sections fails this criterion. A contrast block with a role-appropriate example passes even if the example structure is parallel across sections; only domain-agnostic repetition fails.
- **Rationale**: C-17 requires a contrast block inside each persona section. C-20 adds the requirement that the example be role-appropriate. A domain-agnostic example at each boundary still gives the model a prototype, but a role-appropriate example is semantically close to the friction the model is about to generate for that persona. R4 V-05 showed that domain-matched per-section blockquotes prevented tag drift more effectively than V-02/V-04 (per-section, but single generic example) because the model had a live, friction-relevant prototype at each persona boundary rather than a generic template from an unrelated domain context.

### C-21 -- Explicit Gap-Statement in Amend Template
- **Category**: behavior
- **Weight**: aspirational
- **Source**: R4 V-03, V-05 excellence signal
- **Pass condition**: When the amend loop is triggered (C-10), the amend proposal template includes an explicit gap-statement field -- named something like "What the workaround provides that the artifact does not:" or equivalent -- positioned between the named workaround slot (C-18) and the proposed change. An amend template that captures the named workaround but does not require an explicit gap-statement before the proposed change fails this criterion. If C-10 passes automatically (no sub-3 score), this criterion passes automatically.
- **Rationale**: C-18 requires the named workaround as the first field. C-21 adds a gap-statement field that forces the model to articulate the specific value the workaround provides that the artifact fails to replace. Without the gap-statement, the model can still produce generic remediation ("the artifact needs to be clearer about step 3") even when the workaround is named. With the gap-statement, the remediation must address the specific gap ("the workaround provides one-click export with custom format headers; the artifact does not"). R4 V-03 and V-05 (workaround-first + explicit gap-statement) produced proposals framed as workaround-replacement arguments, while V-01/V-02/V-04 (slot present but no gap-statement) still produced proposals framed as artifact annotations. The gap-statement field closes the last generic-remediation residue in C-18.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 13 * 10)
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
| C-16 | Workaround-first ordering | R3 V-01/V-05 | Workaround before scenario brief creates comparison cascade in character construction |
| C-17 | Per-section contrast blocks | R3 V-02/V-05 | Per-persona enforcement prevents friction-tag drift in long multi-persona outputs |
| C-18 | Named-workaround slot in amend template | R3 V-03/V-05 | Structural slot forces workaround-anchored proposals; eliminates generic remediation |
| C-19 | Numbered step sequence for workaround-before-brief | R4 V-04/V-05 | Converts C-16 from layout convention to sequence rule; closes last model-reordering risk |
| C-20 | Domain-matched per-section contrast examples | R4 V-05 | Role-appropriate prototype at each persona boundary; prevents tag drift better than domain-agnostic repetition |
| C-21 | Explicit gap-statement in amend template | R4 V-03/V-05 | Forces articulation of specific value gap before proposed change; closes generic-remediation residue in C-18 |

---

## R5 Target Combination

A variation hitting all thirteen aspirationals must satisfy:
1. Pre-committed score table (C-11)
2. Named character + workaround-first + numbered step sequence: Step 1 = "What [Name] does today instead:", Step 2 = scenario brief, Step 3 = walkthrough (C-12, C-14, C-16, C-19)
3. Per-section contrast blocks with domain-matched role examples inside first-person prose (C-09, C-15, C-17, C-20)
4. Beats/Loses fields after walkthrough (C-13)
5. Amend loop with named-workaround slot + explicit gap-statement, triggered when sub-3 score exists (C-10, C-18, C-21)

The five mechanism groups are structurally compatible and mutually reinforcing: workaround-first ordering with numbered steps gives the named alternative as the character's construction context with sequence-rule enforcement; per-section domain-matched contrast blocks enforce tag discipline with a role-specific prototype at every persona boundary; inline first-person tags fit inside the resulting natural prose; inertia fields follow mechanically from the named workaround baseline; and the named-workaround slot with explicit gap-statement closes the loop by tying remediation back to the specific value gap the workaround fills. No format switching needed at any step.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria (5 essential, 3 recommended, 2 aspirational) |
| v2 | 2026-03-14 | Added C-11 (pre-committed score table), C-12 (named-character grounding), C-13 (inertia fields) from R1 excellence signals; aspirational formula updated to /5 |
| v3 | 2026-03-14 | Added C-14 (current-workaround context field), C-15 (inline tags in first-person sentences) from R2 excellence signals; tightened C-09 pass condition to require contrast block; aspirational formula updated to /7 |
| v4 | 2026-03-14 | Added C-16 (workaround-first ordering), C-17 (per-section contrast blocks), C-18 (named-workaround slot in amend template) from R3 excellence signals; aspirational formula updated to /10 |
| v5 | 2026-03-14 | Added C-19 (numbered step sequence for workaround-before-brief), C-20 (domain-matched per-section contrast examples), C-21 (explicit gap-statement in amend template) from R4 excellence signals; aspirational formula updated to /13 |
