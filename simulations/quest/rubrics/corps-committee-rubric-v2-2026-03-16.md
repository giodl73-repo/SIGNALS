Here is the complete updated rubric written to `simulations/quest/rubrics/corps-committee-rubric-v2-2026-03-16.md`.

---

**Three new aspirational criteria added (C-09, C-10, C-11):**

**C-09 — Role-Distinctive Voices**
Source: C-08 was PARTIAL in all five R1 variations for the same reason — no criterion required that Phase 3 voices be visibly differentiated by charter orientation. C-08 rewards loading charter files; C-09 rewards actually using them. Pass requires at least three voices with orientation-specific concerns that could not be transplanted to another participant.

**C-10 — Structural-Table Format for Mechanical Sections**
Source: V-04 excellence signal. Both STANCE MANIFEST and ACTION ITEMS rendered as Markdown tables, not lists. Tables make completeness verification visual and reduce token-counting errors. Pass requires tables with named columns for both sections, no blank cells.

**C-11 — Injection-Default Framing for Inertia Voice**
Source: V-05 excellence signal. Inertia-Advocate declared as the default participant — present unless overridden. YES is the exception path requiring named qualifying evidence. Pass requires explicit "YES without a qualifying participant fails" language plus a motivational rationale explaining why incorrect YES is the harder failure (silences the inertia voice without surfacing it).

**Scoring impact under v2:**

| Variation | v1 score | v2 score | Change |
|-----------|----------|----------|--------|
| V-01, V-02 | 90 | 86.25 | -3.75 |
| V-03 | 95 | 91.25 | -3.75 |
| V-04, V-05 | 95 | 93.75 | -1.25 |

The scoring floor drops slightly because aspirational weight is now split four ways. The open target for R2: earn C-09 (role-distinctive voices) — no variation has done it yet.

---

### C-03 -- INERTIA RECORD Complete and Sealed
- **Weight**: essential
- **Category**: correctness
- **Text**: Phase 1 produces a `## INERTIA RECORD` section with four labeled findings (INERTIA-FINDING-A through INERTIA-FINDING-D), each carrying a non-placeholder content anchor. The `INERTIA INVARIANT` line is present with both required contract elements: the commit reference and the modification prohibition.
- **Pass condition**: All four INERTIA-FINDING-* labels present with content anchors (not bare labels, not `[one-phrase anchor]` placeholders). INERTIA INVARIANT line present, contains `sealed at PHASE-1-COMMIT` AND `findings may not be added, removed, or modified without reopening Phase 1` (or equivalent modification prohibition). Fails on any missing finding, bare label, placeholder, or missing/incomplete INERTIA INVARIANT.

---

### C-04 -- Phase 5 Delivers Actionable Minutes
- **Weight**: essential
- **Category**: coverage
- **Text**: Phase 5 contains three required sections -- DECISIONS (verdict + conditions), ACTION ITEMS (at least two items each with owner/action/deadline), and DISSENTING OPINIONS (at least one dissent with objection, resolution path, and named authority -- or explicit "No dissent -- [reason]"). If the verdict is not APPROVED, Owner and Trigger must both be present in the DECISIONS section.
- **Pass condition**: All three Phase 5 sections present with content. Each action item has all three fields (owner role, specific action, deadline). Every CONDITION or BLOCK stance holder from Phase 3 has a corresponding dissent entry, or explicit no-dissent is declared with a reason. Fails if any section is absent, any action item is missing a field, or a non-APPROVED verdict lacks Owner and Trigger.

---

## Recommended Criteria
> Output is significantly better with these. Failing one or two lowers score but does not disqualify.

### C-05 -- Inertia Continuity Bridge Correct
- **Weight**: recommended
- **Category**: correctness
- **Text**: The `## INERTIA CONTINUITY BRIDGE` section appears between Phase 2 and Phase 3. It correctly answers YES (with a qualifying charter role identified from the tier sort) or NO (with Inertia-Advocate INJECTED, appearing first in Tier 1 in Phase 3, and appearing in the ## STANCE MANIFEST). The injected or identified voice cites at least one INERTIA-FINDING-* label from ## INERTIA RECORD.
- **Pass condition**: Bridge section present and answers YES or NO with justification. If YES: the named role's orientation visibly maps to switching-cost analysis or status-quo defense -- not assumed from a general "risk" orientation. If NO: Inertia-Advocate voice appears first in Tier 1 in Phase 3, cites a named INERTIA-FINDING-* label, and appears in STANCE MANIFEST. Fails if bridge section absent, YES claimed without a qualifying role whose charter explicitly covers switching-cost or status-quo defense, or NO declared without injection.

---

### C-06 -- Phase 3 Tier Order and Non-Unanimous Stance
- **Weight**: recommended
- **Category**: correctness
- **Text**: Phase 3 voices appear in Tier 1 -> Tier 2 -> Tier 3 order. Each participant has a standalone `STANCE: [BLOCK / CONDITION / APPROVE]` line preceding their prose. At least one BLOCK or CONDITION stance is present; all-APPROVE is not a valid Phase 3 outcome (triggers Phase 2 restart). The ## STANCE MANIFEST lists all participants with their stance tokens.
- **Pass condition**: Voices in tier order without interleaving. Every voice block has an unqualified `STANCE:` line. Minimum one CONDITION or BLOCK in the manifest. ## STANCE MANIFEST present and complete. Fails if order violated, any STANCE: line absent or qualified (e.g., "BLOCK (pending)"), all voices are APPROVE, or manifest is incomplete.

---

### C-07 -- Phase 4 Tally Matches Stance Manifest
- **Weight**: recommended
- **Category**: correctness
- **Text**: The `TALLY:` line in Phase 4 counts APPROVE, CONDITION, and BLOCK tokens by scanning ## STANCE MANIFEST, not by re-parsing Phase 3 prose. The OUTCOME is derived mechanically from that tally: all APPROVE -> APPROVED; any CONDITION no BLOCK -> APPROVED WITH CONDITIONS; any BLOCK -> BLOCKED or DEFERRED.
- **Pass condition**: Token counts in TALLY line match the number of each token in ## STANCE MANIFEST exactly. OUTCOME label matches the tally rule above. Fails if any count is wrong, OUTCOME contradicts the tally, or Phase 3 prose appears to have been re-parsed to override the manifest.

---

## Aspirational Criteria
> Raise the bar once essential and recommended are stable.

### C-08 -- Charter-Grounded Specificity
- **Weight**: aspirational
- **Category**: depth
- **Text**: Participants are loaded from `.roles/` with orientation phrases that visibly shape each voice's Phase 3 content -- distinct concerns, not generic role-name opinions. Phase 5 conditions name specific artifacts, recipients, and named triggering authorities rather than generic directives ("address concerns" fails). The re-entry path in DECISIONS is actionable: it names a concrete artifact and a concrete authority who unlocks next steps.
- **Pass condition**: Charter Source field in Phase 0 references a specific `.roles/` file (or `Signal defaults` with reason). At least two Phase 3 voices contain concerns visibly tied to their role orientation (not interchangeable). Phase 5 conditions and re-entry path (if present) each name a specific artifact and a named authority. Fails if all voices sound interchangeable, Charter Source is absent, or conditions/re-entry path use vague language throughout.

---

### C-09 -- Role-Distinctive Voices
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each Phase 3 participant's voice is demonstrably shaped by their charter orientation. Concerns, objections, and approvals must be traceable back to the participant's stated role -- the content of one voice could not be transplanted to another participant without change. This goes beyond loading charter files (C-08): it requires that each orientation phrase visibly filters what the participant notices and objects to, producing voice substance that could only come from that role.
- **Pass condition**: At least three Phase 3 voices contain concerns that are orientation-specific -- each raises at least one issue plausibly unique to their charter (e.g., a security-charter voice flags authentication surface, not generic "risk"). No two voices are substantively interchangeable (swapping names would not produce an equivalent document). Fails if all voices raise concerns indistinguishable by role, or if orientation phrases from Phase 0 are not reflected in Phase 3 substance.
- **Source**: R1 scorecard -- C-08 PARTIAL in all five variations due to absence of an explicit role-distinctness mandate.

---

### C-10 -- Structural-Table Format for Mechanical Sections
- **Weight**: aspirational
- **Category**: format
- **Text**: Sections where completeness is mechanically verifiable -- specifically the ## STANCE MANIFEST and ACTION ITEMS -- are formatted as Markdown tables, not prose lists. Table columns make missing cells visually unambiguous and reduce token-counting errors. STANCE MANIFEST columns: Participant | Tier | Stance. ACTION ITEMS columns: Owner Role | Action | Deadline.
- **Pass condition**: ## STANCE MANIFEST is a Markdown table with columns for at least Participant, Tier, and Stance. ACTION ITEMS is a Markdown table with columns for at least Owner Role, Action, and Deadline. No empty cells in either table. Fails if either section uses prose list or bullet format, or any required cell is blank.
- **Source**: R1 scorecard -- V-04 excellence signal: table-format STANCE MANIFEST makes token counting explicit and less error-prone; table-format ACTION ITEMS structurally enforces all-three-fields compliance without relying on fill-rule enforcement alone.

---

### C-11 -- Injection-Default Framing for Inertia Voice
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The skill frames Inertia-Advocate as a default Phase 3 participant -- always present unless the bridge explicitly overrides it with named qualifying evidence. The YES path is the exception, not the expected outcome. The skill includes a motivational rationale explaining why incorrect YES is the harder failure mode: it silences the inertia voice without surfacing it, producing a simulation that appears to have handled inertia but has not.
- **Pass condition**: The bridge section labels its default path as NO/inject and its exception path as YES/override. The YES condition states explicitly that a qualifying participant must be named -- "YES without a qualifying participant is an incorrect affirmation and fails." A motivational framing statement explains why incorrect YES is worse than unnecessary injection. Fails if YES and NO are presented as symmetric options, if incorrect YES produces only a soft warning, or if no motivational rationale is present.
- **Source**: R1 scorecard -- V-05 excellence signal: injection-as-default framing with motivational rationale ("incorrect YES is a harder failure than injection; it silences the inertia voice without surfacing it").

---

## Scoring Reference

| Tier | Criteria | Max contribution |
|------|----------|-----------------|
| Essential (4) | C-01, C-02, C-03, C-04 | 60 pts |
| Recommended (3) | C-05, C-06, C-07 | 30 pts |
| Aspirational (4) | C-08, C-09, C-10, C-11 | 10 pts |

**Golden**: all essential pass + composite >= 80.

### Example scores

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | Score | Golden? |
|------|------|------|------|------|------|------|------|------|------|------|-------|---------|
| Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | 100 | YES |
| Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | 97.5 | YES |
| Y | Y | Y | Y | Y | Y | Y | 0.5 | N | Y | Y | 93.75 | YES |
| Y | Y | Y | Y | Y | Y | Y | 0.5 | N | N | N | 91.25 | YES |
| Y | Y | Y | Y | 0.5 | Y | Y | 0.5 | N | N | N | 86.25 | YES |
| Y | Y | Y | Y | N | Y | Y | N | N | N | N | 80 | YES (boundary) |
| Y | Y | Y | Y | N | N | Y | N | N | N | N | 70 | NO |
| Y | Y | Y | N | Y | Y | Y | Y | Y | Y | Y | 87.5 | NO (C-04 fail) |
| N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | 87.5 | NO (C-01 fail) |

### R1 variations rescored under v2

| Variation | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | Aspirational pts | Score |
|-----------|------|------|------|------|------|------|------|-----------------|-------|
| V-01 | 0.5 | Y | Y | 0.5 | N | N | N | 0.5/4 x 10 = 1.25 | 86.25 |
| V-02 | 0.5 | Y | Y | 0.5 | N | N | N | 0.5/4 x 10 = 1.25 | 86.25 |
| V-03 | Y | Y | Y | 0.5 | N | N | N | 0.5/4 x 10 = 1.25 | 91.25 |
| V-04 | Y | Y | Y | 0.5 | N | Y | N | 1.5/4 x 10 = 3.75 | 93.75 |
| V-05 | Y | Y | Y | 0.5 | N | N | Y | 1.5/4 x 10 = 3.75 | 93.75 |

> C-09 (role-distinctive voices) is the open gap across all R1 variations. No variation earned it.
> R2 target: at least one variation passes C-09 to validate the criterion is achievable.
