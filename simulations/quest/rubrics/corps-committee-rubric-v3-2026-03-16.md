Now I have everything I need. Here is the complete v3 rubric:

---

```markdown
---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-16
version: 3
---

# Scoring Rubric — corps-committee (v3)

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PARTIAL counts as 0.5 toward aspirational_pass.

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Version History

| Version | Aspirational criteria | Source round | Change |
|---------|----------------------|--------------|--------|
| v1 | C-08 | — | baseline |
| v2 | C-08–C-11 | R1 scorecard | +C-09 role-distinctive voices; +C-10 structural tables; +C-11 injection-default framing |
| v3 | C-08–C-14 | R2 scorecard | +C-12 pre-skeleton rule block; +C-13 rewrite-before-proceed loop; +C-14 coupling integrity symmetry |

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
- **Pass condition**: Bridge section present and answers YES or NO with justification. If YES: the named role's orientation visibly maps to switching-cost analysis or status-quo defense — not assumed from a general "risk" orientation. If NO: Inertia-Advocate voice appears first in Tier 1 in Phase 3, cites a named INERTIA-FINDING-* label, and appears in STANCE MANIFEST. Fails if bridge section absent, YES claimed without a qualifying role whose charter explicitly covers switching-cost or status-quo defense, or NO declared without injection.

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
- **Text**: Participants are loaded from `.roles/` with orientation phrases that visibly shape each voice's Phase 3 content — distinct concerns, not generic role-name opinions. Phase 5 conditions name specific artifacts, recipients, and named triggering authorities rather than generic directives ("address concerns" fails). The re-entry path in DECISIONS is actionable: it names a concrete artifact and a concrete authority who unlocks next steps.
- **Pass condition**: Charter Source field in Phase 0 references a specific `.roles/` file (or `Signal defaults` with reason). At least two Phase 3 voices contain concerns visibly tied to their role orientation (not interchangeable). Phase 5 conditions and re-entry path (if present) each name a specific artifact and a named authority. Fails if all voices sound interchangeable, Charter Source is absent, or conditions/re-entry path use vague language throughout.

---

### C-09 — Role-Distinctive Voices
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each Phase 3 participant's voice is demonstrably shaped by their charter orientation. Concerns, objections, and approvals must be traceable back to the participant's stated role — the content of one voice could not be transplanted to another participant without change. This goes beyond loading charter files (C-08): it requires that each orientation phrase visibly filters what the participant notices and objects to, producing voice substance that could only come from that role.
- **Pass condition**: At least three Phase 3 voices contain concerns that are orientation-specific — each raises at least one issue plausibly unique to their charter (e.g., a security-charter voice flags authentication surface, not generic "risk"). No two voices are substantively interchangeable (swapping names would not produce an equivalent document). Fails if all voices raise concerns indistinguishable by role, or if orientation phrases from Phase 0 are not reflected in Phase 3 substance.
- **Source**: R1 scorecard — C-08 PARTIAL in all five variations due to absence of an explicit role-distinctness mandate.

---

### C-10 — Structural-Table Format for Mechanical Sections
- **Weight**: aspirational
- **Category**: format
- **Text**: Sections where completeness is mechanically verifiable — specifically the ## STANCE MANIFEST and ACTION ITEMS — are formatted as Markdown tables, not prose lists. Table columns make missing cells visually unambiguous and reduce token-counting errors. STANCE MANIFEST columns: Participant | Tier | Stance. ACTION ITEMS columns: Owner Role | Action | Deadline.
- **Pass condition**: ## STANCE MANIFEST is a Markdown table with columns for at least Participant, Tier, and Stance. ACTION ITEMS is a Markdown table with columns for at least Owner Role, Action, and Deadline. No empty cells in either table. Fails if either section uses prose list or bullet format, or any required cell is blank.
- **Source**: R1 scorecard — V-04 excellence signal: table-format STANCE MANIFEST makes token counting explicit and less error-prone; table-format ACTION ITEMS structurally enforces all-three-fields compliance without relying on fill-rule enforcement alone.

---

### C-11 — Injection-Default Framing for Inertia Voice
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The skill frames Inertia-Advocate as a default Phase 3 participant — always present unless the bridge explicitly overrides it with named qualifying evidence. The YES path is the exception, not the expected outcome. The skill includes a motivational rationale explaining why incorrect YES is the harder failure mode: it silences the inertia voice without surfacing it, producing a simulation that appears to have handled inertia but has not.
- **Pass condition**: The bridge section labels its default path as NO/inject and its exception path as YES/override. The YES condition states explicitly that a qualifying participant must be named — "YES without a qualifying participant is an incorrect affirmation and fails." A motivational framing statement explains why incorrect YES is worse than unnecessary injection. Fails if YES and NO are presented as symmetric options, if incorrect YES produces only a soft warning, or if no motivational rationale is present.
- **Source**: R1 scorecard — V-05 excellence signal: injection-as-default framing with motivational rationale ("incorrect YES is a harder failure than injection; it silences the inertia voice without surfacing it").

---

### C-12 — Pre-Skeleton Numbered Rule Block
- **Weight**: aspirational
- **Category**: format
- **Text**: Critical structural constraints are declared as a numbered rule block positioned before the skeleton print instruction, not embedded in individual fill-rule sections. Rules declared pre-skeleton are active throughout all phases of execution — including skeleton reproduction — whereas rules embedded in fill-rule sections activate only when that section is reached. At minimum, two rules governing distinct structural mechanisms (e.g., role-distinctiveness, coupling integrity, injection default) must appear in the pre-skeleton block.
- **Pass condition**: A numbered rule block (e.g., `STRUCTURAL RULES`, `ACTIVE CONSTRAINTS`) appears before the first `## SKELETON` or `PRINT SKELETON` instruction. The block contains at least two named rules, each identifying the mechanism it governs. Rules are framed as active constraints ("ENFORCE", "VALIDATE"), not advisory notes. Fails if critical structural rules appear only in fill-rule sections, if the block appears after the skeleton instruction, or if the block contains only one rule.
- **Source**: R2 scorecard — V-05 excellence signal: THREE STRUCTURAL RULES declared before the skeleton primes all three mechanisms simultaneously, making constraints active through skeleton reproduction and all fill steps.

---

### C-13 — Rewrite-Before-Proceed Loop
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Structural validation rules that can detect failure mid-generation must include an explicit correction path, not just a VALIDATE directive. When a distinctiveness check, bridge gate, or other inline validator fails, the skill instructs the model to rewrite the failing scope before proceeding to the next section. Without this, failures propagate silently: a Phase 3 voice that fails the distinctiveness rule continues into the STANCE MANIFEST, Phase 4, and Phase 5 without correction.
- **Pass condition**: At least one structural validation rule (VALIDATE line or equivalent) is paired with an explicit `IF FAIL: rewrite [scope] before proceeding to [next section]` instruction. Both the scope to rewrite and the downstream section to gate are named. Fails if all VALIDATE directives are terminal (no correction path), if the correction instruction omits the scope or the gate target, or if the correction path uses only a soft warning ("note", "ensure") rather than an imperative rewrite instruction.
- **Source**: R2 scorecard — V-05 excellence signal: `IF FAIL: rewrite failing voices before proceeding to STANCE MANIFEST` creates in-generation self-correction absent from V-01/V-04, which share the same ROLE-DISTINCTIVENESS RULE but propagate failures silently.

---

### C-14 — Coupling Integrity Symmetry Annotation
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The skill explicitly annotates that PHASE-3-COMMIT bidirectionality is structurally identical to PHASE-1-COMMIT bidirectionality — both are coupling integrity contracts, not just sequential markers. Without this annotation, agents tend to enforce bidirectionality at Phase 1 (where the INERTIA INVARIANT makes it salient) but treat Phase 3 as an ordinary commit, silently breaking the symmetric contract. The annotation names this as a recognizable pattern so the contract receives consistent enforcement.
- **Pass condition**: The skill contains an explicit annotation (comment, label, or structural rule) stating that the PHASE-3-COMMIT coupling clause mirrors PHASE-1-COMMIT bidirectionality in kind. The annotation uses a recognizable pattern name (e.g., `COUPLING INTEGRITY SYMMETRY`, `bidirectionality contract`) and is positioned where Phase 3 commit rules are declared or in the pre-skeleton rule block. Fails if the Phase-3-COMMIT bidirectionality clause is present but unlabeled as structurally equivalent to Phase-1-COMMIT, or if no annotation appears anywhere in the skill.
- **Source**: R2 scorecard — V-05 excellence signal: COUPLING INTEGRITY SYMMETRY annotation names the bidirectionality contract as a structural pattern, reducing selective adherence risk; V-05 is the only R2 variation to make this symmetry explicit.

---

## Scoring Reference

| Tier | Criteria | Max contribution |
|------|----------|-----------------|
| Essential (4) | C-01, C-02, C-03, C-04 | 60 pts |
| Recommended (3) | C-05, C-06, C-07 | 30 pts |
| Aspirational (7) | C-08–C-14 | 10 pts |

Each full aspirational pass = 10/7 ≈ 1.43 pts. PARTIAL = 0.5 pass = 0.71 pts. A variation earning all 7 earns the full 10-pt pool.

**Golden**: all essential pass + composite >= 80.

### Example scores

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Score | Golden? |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|---------|
| Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | 100 | YES |
| Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | 98.57 | YES |
| Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | 94.29 | YES |
| Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | N | 92.86 | YES |
| Y | Y | Y | Y | Y | Y | Y | 0.5 | N | Y | N | N | N | N | 91.43 | YES |
| Y | Y | Y | Y | Y | Y | Y | N | N | N | N | N | N | N | 90 | YES |
| Y | Y | Y | Y | N | Y | Y | N | N | N | N | N | N | N | 80 | YES (boundary) |
| Y | Y | Y | Y | N | N | Y | N | N | N | N | N | N | N | 70 | NO |
| Y | Y | Y | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | 87.5 | NO (C-04 fail) |
| N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | 87.5 | NO (C-01 fail) |

### R2 variations scored under v3

| Variation | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Asp pts | Score |
|-----------|------|------|------|------|------|------|------|---------|-------|
| V-01 | Y | Y | N | N | ? | N | ? | ≥2/7×10=2.86 | ≥92.86 |
| V-02 | 0.5 | N | Y | N | ? | ? | ? | ≥1.5/7×10=2.14 | ≥92.14 |
| V-03 | 0.5 | N | N | Y | ? | ? | ? | ≥1.5/7×10=2.14 | ≥92.14 |
| V-04 | Y | Y | Y | N | ? | N | N | ≥3/7×10=4.29 | ≥94.29 |
| V-05 | Y | Y | Y | Y | Y | Y | Y | 7/7×10=10 | **100** |

> C-12, C-13, C-14 were sourced from V-05. Variations marked `?` require explicit R3 evaluation — the criteria did not exist when R2 was run. Scores for V-01 through V-04 are lower bounds; actual scores may be higher if `?` criteria resolve to PASS.

> Open targets for R3: C-12 (pre-skeleton rule block) — no variation other than V-05 confirmed. C-13 (rewrite-before-proceed) — confirmed MISS for V-01 and V-04; others unscored. C-14 (coupling symmetry annotation) — V-05 uniquely earns this; all others MISS or unscored.
```

---

Three new aspirational criteria added from R2 V-05 excellence signals:

| Criterion | Pattern | Key pass condition |
|-----------|---------|-------------------|
| **C-12** | Pre-skeleton numbered rule block | Named constraint block appears before the skeleton print instruction; at least two rules; framed as ENFORCE/VALIDATE |
| **C-13** | Rewrite-before-proceed loop | At least one VALIDATE is paired with an explicit `IF FAIL: rewrite [scope] before proceeding to [section]`; both scope and gate named |
| **C-14** | Coupling integrity symmetry annotation | Phase-3-COMMIT bidirectionality is annotated as structurally identical to Phase-1-COMMIT; named as a recognizable pattern |

The scoring pool stays at 10 pts aspirational, now split seven ways (≈1.43 pts each). V-05 maintains 100; the lower bounds for V-01 through V-04 drop because the `?` criteria were unscored in R2. R3 open target: earn C-12 and C-14 — no variation other than V-05 has confirmed either.
