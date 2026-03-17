---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-16
version: 1
---

# Scoring Rubric — corps-committee

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria
> All must pass. Without these the output is not useful as a pre-meeting simulation.

### C-01 — Committee Type Declared
- **Weight**: essential
- **Category**: correctness
- **Text**: Phase 0 declares a recognized committee type and a concrete agenda item. The type must be one of: ROB, shiproom, arch-board, or an explicit user-specified type. The agenda item must name the artifact or decision under review.
- **Pass condition**: Phase 0 contains `Committee Type: ROB` / `Committee Type: shiproom` / `Committee Type: arch-board` (or user type) on its own labeled line, AND `Agenda Item:` names a specific subject. Fails if type is absent, unlabeled, or uses non-standard phrasing (e.g., "product review" instead of "ROB").

---

### C-02 — Five-Phase Structure with Terminal Commits
- **Weight**: essential
- **Category**: format
- **Text**: The output contains all five phases (0–5) in sequence, each closed by a `PHASE-N-COMMIT: [locked]` line that is the terminal line of that phase. No phase content appears after its commit line.
- **Pass condition**: All six commit markers present (PHASE-0-COMMIT through PHASE-5-COMMIT), each labeled `[locked]`, each appearing as the last substantive line before the next phase separator. Fails if any phase is absent, any commit is missing, or content follows a commit line within the same phase.

---

### C-03 — INERTIA RECORD Complete and Sealed
- **Weight**: essential
- **Category**: correctness
- **Text**: Phase 1 produces a `## INERTIA RECORD` section with four labeled findings (INERTIA-FINDING-A through INERTIA-FINDING-D), each carrying a non-placeholder content anchor. The `INERTIA INVARIANT` line is present with both required contract elements: the commit reference and the modification prohibition.
- **Pass condition**: All four INERTIA-FINDING-* labels present with content anchors (not bare labels, not `[one-phrase anchor]` placeholders). INERTIA INVARIANT line present, contains `sealed at PHASE-1-COMMIT` AND `findings may not be added, removed, or modified without reopening Phase 1` (or equivalent modification prohibition). Fails on any missing finding, bare label, placeholder, or missing/incomplete INERTIA INVARIANT.

---

### C-04 — Phase 5 Delivers Actionable Minutes
- **Weight**: essential
- **Category**: coverage
- **Text**: Phase 5 contains three required sections — DECISIONS (verdict + conditions), ACTION ITEMS (at least two items each with owner/action/deadline), and DISSENTING OPINIONS (at least one dissent with objection, resolution path, and named authority — or explicit "No dissent — [reason]"). If the verdict is not APPROVED, Owner and Trigger must both be present in the DECISIONS section.
- **Pass condition**: All three Phase 5 sections present with content. Each action item has all three fields (owner role, specific action, deadline). Every CONDITION or BLOCK stance holder from Phase 3 has a corresponding dissent entry, or explicit no-dissent is declared with a reason. Fails if any section is absent, any action item is missing a field, or a non-APPROVED verdict lacks Owner and Trigger.

---

## Recommended Criteria
> Output is significantly better with these. Failing one or two lowers score but does not disqualify.

### C-05 — Inertia Continuity Bridge Correct
- **Weight**: recommended
- **Category**: correctness
- **Text**: The `## INERTIA CONTINUITY BRIDGE` section appears between Phase 2 and Phase 3. It correctly answers YES (with a qualifying charter role identified from the tier sort) or NO (with Inertia-Advocate INJECTED, appearing first in Tier 1 in Phase 3, and appearing in the ## STANCE MANIFEST). The injected or identified voice cites at least one INERTIA-FINDING-* label from ## INERTIA RECORD.
- **Pass condition**: Bridge section present and answers YES or NO with justification. If YES: the named role's orientation visibly maps to switching-cost analysis or status-quo defense. If NO: Inertia-Advocate voice appears first in Tier 1 in Phase 3, cites a named INERTIA-FINDING-* label, and appears in STANCE MANIFEST. Fails if bridge section absent, YES claimed without qualifying role, or NO declared without injection.

---

### C-06 — Phase 3 Tier Order and Non-Unanimous Stance
- **Weight**: recommended
- **Category**: correctness
- **Text**: Phase 3 voices appear in Tier 1 → Tier 2 → Tier 3 order. Each participant has a standalone `STANCE: [BLOCK / CONDITION / APPROVE]` line preceding their prose. At least one BLOCK or CONDITION stance is present; all-APPROVE is not a valid Phase 3 outcome (triggers Phase 2 restart). The ## STANCE MANIFEST lists all participants with their stance tokens.
- **Pass condition**: Voices in tier order without interleaving. Every voice block has an unqualified `STANCE:` line. Minimum one CONDITION or BLOCK in the manifest. ## STANCE MANIFEST present and complete. Fails if order violated, any STANCE: line absent or qualified (e.g., "BLOCK (pending)"), all voices are APPROVE, or manifest is incomplete.

---

### C-07 — Phase 4 Tally Matches Stance Manifest
- **Weight**: recommended
- **Category**: correctness
- **Text**: The `TALLY:` line in Phase 4 counts APPROVE, CONDITION, and BLOCK tokens by scanning ## STANCE MANIFEST, not by re-parsing Phase 3 prose. The OUTCOME is derived mechanically from that tally: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
- **Pass condition**: Token counts in TALLY line match the number of each token in ## STANCE MANIFEST exactly. OUTCOME label matches the tally rule above. Fails if any count is wrong, OUTCOME contradicts the tally, or Phase 3 prose appears to have been re-parsed to override the manifest.

---

## Aspirational Criteria
> Raise the bar once essential and recommended are stable.

### C-08 — Charter-Grounded Specificity
- **Weight**: aspirational
- **Category**: depth
- **Text**: Participants are loaded from `.craft/roles/` with orientation phrases that visibly shape each voice's Phase 3 content — distinct concerns, not generic role-name opinions. Phase 5 conditions name specific artifacts, recipients, and named triggering authorities rather than generic directives ("address concerns" fails). The re-entry path in DECISIONS is actionable: it names a concrete artifact and a concrete authority who unlocks next steps.
- **Pass condition**: Charter Source field in Phase 0 references a specific `.craft/roles/` file (or `Signal defaults` with reason). At least two Phase 3 voices contain concerns visibly tied to their role orientation (not interchangeable). Phase 5 conditions and re-entry path (if present) each name a specific artifact and a named authority. Fails if all voices sound interchangeable, Charter Source is absent, or conditions/re-entry path use vague language throughout.

---

## Scoring Reference

| Tier | Criteria | Max contribution |
|------|----------|-----------------|
| Essential (4) | C-01, C-02, C-03, C-04 | 60 pts |
| Recommended (3) | C-05, C-06, C-07 | 30 pts |
| Aspirational (1) | C-08 | 10 pts |

**Golden**: all essential pass + composite >= 80.

### Example scores

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | Score | Golden? |
|------|------|------|------|------|------|------|------|-------|---------|
| Y | Y | Y | Y | Y | Y | Y | Y | 100 | YES |
| Y | Y | Y | Y | Y | Y | Y | N | 90 | YES |
| Y | Y | Y | Y | N | Y | Y | N | 80 | YES (boundary) |
| Y | Y | Y | Y | N | N | Y | N | 70 | NO |
| Y | Y | Y | N | Y | Y | Y | Y | 85 | NO (C-04 fail) |
| N | Y | Y | Y | Y | Y | Y | Y | 85 | NO (C-01 fail) |
