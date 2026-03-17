## org:committee Round 5 — Scorecard

**Rubric version**: v5 (max 112: essential 60 + recommended 30 + aspirational 22)
**Variations evaluated**: V-01 through V-05

---

## Per-Variation Scoring

### V-01 — Lifecycle Emphasis: Sort Validation Gate + `RESPONDS-TO:` Subfield

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Committee type declared correctly | **PASS** | "Output the first line: `Committee: [TYPE] — [agenda item title]`" |
| C-02 | Participants loaded from `.craft/roles/` | **PASS** | Step 2 explicit load with graceful fallback |
| C-03 | Each participant speaks from their role lens | **PASS** | "2-4 sentences from this role's documented orientation" in every voice block |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS all present |
| C-05 | At least one challenge/condition/block | **PASS** | "At least one participant must declare CONDITION or BLOCK" enforced in Phase A |
| C-06 | Agenda item specificity | **PASS** | Step 3 investigation names specific displacements; voices respond to Step 3 findings |
| C-07 | Action items owned and actionable | **PASS** | `[Owner Role] — [specific action] — [deadline]`; vague items explicitly fail |
| C-08 | Dissents include resolution paths | **PASS** | "concrete condition — [authority role] decides when [condition is met]" |
| C-09 | Non-obvious surprise | **PASS** | Step 3(d) + GATE self-check before proceeding |
| C-10 | Decision-complete | **PASS** | Re-entry path required: who reviews, what evidence triggers re-review |
| C-11 | Challenger-first ordering | **PASS** | "strict tier order: all Tier 1 → all Tier 2 → all Tier 3" |
| C-12 | Switching-cost investigation precedes simulation | **PASS** | Full SWITCHING-COST INVESTIGATION block (Step 3) before any voice |
| C-13 | Stance declared before prose — no drift | **PASS** | "`STANCE:` must appear as a standalone line before any prose... must not soften, qualify, or contradict it" |
| C-14 | Vote tally precedes formal minutes | **PASS** | Phase B: "After all participant voices and before any formal section" |
| C-15 | `STANCE:` label is structural | **PASS** | Structural declaration, standalone line, prose follows — named and enforced |
| C-16 | Investigation self-check gate | **PASS** | C-16 Gate step: YES/NO + "Do not proceed to Step 4 until you can answer YES" |
| C-17 | Advocate voices grounded in investigation | **PASS** | `CITE:` structural subfield required for all Tier 3 voices |
| C-18 | All-approve self-correction diagnostic | **PASS** | Step 4b with named `SORT-CHECK:` checkpoint; voices blocked until SORT-CHECK output |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | `RESPONDS-TO:` structural subfield: "quote or paraphrase the concern, then state how this endorsement addresses it" |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 11/11 = **22**
**Composite: 112**

---

### V-02 — Output Format: Template with `SORT-CHECK:` Field + `RESPONDS-TO:` Subfield

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Committee type declared correctly | **PASS** | First template field: `Committee: [TYPE] — [agenda item title]` |
| C-02 | Participants loaded from `.craft/roles/` | **PASS** | Rule 1: "Load participants from `.craft/roles/`"; `Participants loaded from:` template field forces disclosure |
| C-03 | Each participant speaks from their role lens | **PASS** | Voice block template: "2-4 sentences from this role's documented orientation" |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS as template sections |
| C-05 | At least one challenge/condition/block | **PASS** | Rule 9: "At minimum: one participant must declare CONDITION or BLOCK" |
| C-06 | Agenda item specificity | **PASS** | Template fields force specificity throughout; no free-form sections |
| C-07 | Action items owned and actionable | **PASS** | "Format rule: every item has an owner, a specific deliverable, and a deadline" |
| C-08 | Dissents include resolution paths | **PASS** | "Resolution path: [concrete condition — [authority role] decides when [condition is met]]" |
| C-09 | Non-obvious surprise | **PASS** | (d) Non-obvious cost field + GATE enforces non-obviousness before proceeding |
| C-10 | Decision-complete | **PASS** | "Re-entry path (if not approved): [Owner Role] must [specific action] — committee re-reviews when [concrete condition]" |
| C-11 | Challenger-first ordering | **PASS** | "[Write one block per participant in tier order: Tier 1 → Tier 2 → Tier 3.]" |
| C-12 | Switching-cost investigation precedes simulation | **PASS** | SWITCHING-COST INVESTIGATION section before PARTICIPANT SORT and before PARTICIPANT VOICES |
| C-13 | Stance declared before prose — no drift | **PASS** | "STANCE: line is the declaration. Prose follows and must not contradict or hedge it." |
| C-14 | Vote tally precedes formal minutes | **PASS** | `TALLY:` template field between PARTICIPANT VOICES and DECISIONS |
| C-15 | `STANCE:` label is structural | **PASS** | Rule 5: "The `STANCE:` line is the declaration. It must be a standalone line, not embedded in prose." |
| C-16 | Investigation self-check gate | **PASS** | GATE template field; Rule 3: "If GATE is NO, rewrite the investigation before filling any subsequent field" |
| C-17 | Advocate voices grounded in investigation | **PASS** | Rule 6: "The `CITE:` subfield is required for every Tier 3 participant. A Tier 3 voice without `CITE:` fails C-17." |
| C-18 | All-approve self-correction diagnostic | **PASS** | `SORT-CHECK:` template field (mandatory); Rule 4: "If SORT-CHECK is YES, revise the sort and re-output the tier block before filling any voice blocks" |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | Rule 7: "`RESPONDS-TO:` subfield is required for every Tier 3 participant. It must name a specific concern — a generic acknowledgment of opposition does not pass." |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 11/11 = **22**
**Composite: 112**

---

### V-03 — Phrasing Register: Minimal Imperative with Inline C-18/C-19 Commands

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Committee type declared correctly | **PASS** | "Open with: `Committee: [TYPE] — [agenda item title]`" |
| C-02 | Participants loaded from `.craft/roles/` | **PASS** | "Load participants. Read `.craft/roles/`... If no charter: use Signal defaults and state them." |
| C-03 | Each participant speaks from their role lens | **PASS** | "[2-4 sentences from documented role orientation.]" in voice format |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS present |
| C-05 | At least one challenge/condition/block | **PASS** | "At least one voice must be CONDITION or BLOCK. All-APPROVE means roles are mis-sorted — fix it." |
| C-06 | Agenda item specificity | **PASS** | "Investigate before anyone speaks. Name what this proposal displaces" — specific (a)–(d) |
| C-07 | Action items owned and actionable | **PASS** | "[Owner Role] — [specific action] — [deadline]" with "No vague items" |
| C-08 | Dissents include resolution paths | **PASS** | "resolution path (concrete condition + named authority)" |
| C-09 | Non-obvious surprise | **PASS** | "(d) Non-obvious cost: [the surprise the author missed]" + GATE: YES gate |
| C-10 | Decision-complete | **PASS** | "Re-entry path (if not approved): [Owner Role] delivers [specific artifact] — re-review when [condition]" |
| C-11 | Challenger-first ordering | **PASS** | "Write voices in tier order: Tier 1 → Tier 2 → Tier 3." |
| C-12 | Switching-cost investigation precedes simulation | **PASS** | "Investigate before anyone speaks" — full (a)–(d) block precedes sort and voices |
| C-13 | Stance declared before prose — no drift | **PASS** | "`STANCE:` is a standalone labeled line, prose follows... must not introduce a new stance or soften the declared one." |
| C-14 | Vote tally precedes formal minutes | **PASS** | "After the last voice, before anything else: `TALLY:`" |
| C-15 | `STANCE:` label is structural | **PASS** | Standalone labeled line; inline enforcement: "Prose must not introduce a new stance or soften the declared one." |
| C-16 | Investigation self-check gate | **PASS** | "GATE: YES — non-obvious because [reason]"; "If you cannot write GATE: YES honestly, rewrite (a)–(d) until you can. Do not continue until the gate is satisfied." |
| C-17 | Advocate voices grounded in investigation | **PASS** | Inline: "(1) cite one investigation finding by label — (a), (b), (c), or (d)"; "Tier 3 voices that endorse without citing an investigation finding fail C-17." |
| C-18 | All-approve self-correction diagnostic | **PASS** | "Sort validation... check: are Tier 1 and Tier 2 both empty? ... Identify which role most naturally interrogates risk... Reassign it... output `SORT-CHECK:` ... Do not write any voices until SORT-CHECK is output." |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | "AND (2) name a specific Tier 1 or Tier 2 concern and state how this endorsement responds to it"; "Tier 3 voices that endorse without naming and responding to a Tier 1/2 concern fail C-19." |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 11/11 = **22**
**Composite: 112**

---

### V-04 — Inertia Framing: Inertia Finding Tags as C-19 Anchor + Remaining Sort Validation

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Committee type declared correctly | **PASS** | "Output the first line: `Committee: [TYPE] — [agenda item title]`" |
| C-02 | Participants loaded from `.craft/roles/` | **PASS** | Step 2 loads charter; inertia-advocate added if present; fallback stated |
| C-03 | Each participant speaks from their role lens | **PASS** | All voice formats specify role-oriented prose; inertia-advocate has distinct framing |
| C-04 | All three required sections | **PASS** | DECISIONS, ACTION ITEMS, DISSENTING OPINIONS present |
| C-05 | At least one challenge/condition/block | **PASS** | Inertia-advocate always CONDITION or BLOCK (mandatory); "At least one non-inertia participant must also declare CONDITION or BLOCK" |
| C-06 | Agenda item specificity | **PASS** | Phase 1 investigation names specific displacements; INERTIA-FINDING tags create labelled agenda-specific concerns |
| C-07 | Action items owned and actionable | **PASS** | "[Owner Role] — [specific action] — [deadline]"; "All items owned and specific" |
| C-08 | Dissents include resolution paths | **PASS** | Inertia-advocate dissent requires explicit resolution path; all dissents require concrete condition |
| C-09 | Non-obvious surprise | **PASS** | "(d) Non-obvious cost" + GATE before proceeding |
| C-10 | Decision-complete | **PASS** | "Re-entry path: what must change, who reviews, what evidence triggers re-entry" |
| C-11 | Challenger-first ordering | **PASS** | Inertia-advocate mandatory first; "Skeptics (speak next) → Advocates (speak last)" among remaining — challenger-first principle maintained throughout |
| C-12 | Switching-cost investigation precedes simulation | **PASS** | "Phase 1 — Pre-Meeting Investigation... before any participant speaks, including the inertia-advocate" |
| C-13 | Stance declared before prose — no drift | **PASS** | `STANCE:` standalone in both Phase 2 and Phase 4 voice formats |
| C-14 | Vote tally precedes formal minutes | **PASS** | Phase 5: TALLY before DECISIONS |
| C-15 | `STANCE:` label is structural | **PASS** | Standalone labeled line in all voice format blocks |
| C-16 | Investigation self-check gate | **PASS** | "GATE: [YES — ... / NO — revising]"; "Do not proceed until GATE is YES" |
| C-17 | Advocate voices grounded in investigation | **PASS** | "Advocate voices must additionally cite at least one Phase 1 investigation finding (by label — (a), (b), (c), or (d)) or one INERTIA-FINDING tag" |
| C-18 | All-approve self-correction diagnostic | **PASS** | REMAINING-SORT-CHECK detects all-remaining-advocates and forces correction before Phase 4 voices; inertia-mandate architecturally prevents overall all-APPROVE. *Note: mechanism is detection of all-remaining-advocates rather than the standard SORT-CHECK on the full three-tier lineup — structural invariant is preserved through different architecture.* |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | "Must name at least one of INERTIA-FINDING-A or INERTIA-FINDING-B by tag and respond to it"; "C-19 enforcement for advocate voices: Naming and responding to INERTIA-FINDING-A or INERTIA-FINDING-B by tag satisfies C-19." |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 11/11 = **22**
**Composite: 112**

---

### V-05 — Combined: Five Labeled Declarations + Named Step Boundaries

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Committee type declared correctly | **PASS** | Step 1 opens with `Committee: [TYPE] — [agenda item title]` code block |
| C-02 | Participants loaded from `.craft/roles/` | **PASS** | "Load participants. Read `.craft/roles/` for this committee type's charter... Fallback: Signal defaults — state them explicitly." |
| C-03 | Each participant speaks from their role lens | **PASS** | "2-4 sentences from documented role orientation" in Step 5 voice format |
| C-04 | All three required sections | **PASS** | Step 7 contains DECISIONS, ACTION ITEMS, DISSENTING OPINIONS |
| C-05 | At least one challenge/condition/block | **PASS** | "At minimum: one voice must be CONDITION or BLOCK. All-APPROVE → return to Step 4b and re-sort." |
| C-06 | Agenda item specificity | **PASS** | Step 2 investigation names specific displacements; voices respond to labeled findings |
| C-07 | Action items owned and actionable | **PASS** | "[Owner Role] — [specific action] — [deadline]"; "Every item: named owner, specific deliverable, deadline. Vague items fail." |
| C-08 | Dissents include resolution paths | **PASS** | "Resolution path: [concrete condition — [authority role] decides when [condition met]]" |
| C-09 | Non-obvious surprise | **PASS** | "(d) Non-obvious cost" + GATE YES with specific reason |
| C-10 | Decision-complete | **PASS** | "Re-entry path: [Owner Role] delivers [specific artifact] — re-review when [concrete condition]" |
| C-11 | Challenger-first ordering | **PASS** | Step 5: "strict tier order: Tier 1 → Tier 2 → Tier 3" |
| C-12 | Switching-cost investigation precedes simulation | **PASS** | Step 2 full investigation before Step 4 sort and Step 5 voices |
| C-13 | Stance declared before prose — no drift | **PASS** | "`STANCE:` is the declaration. Prose follows and must not introduce a new stance or hedge the declared one." |
| C-14 | Vote tally precedes formal minutes | **PASS** | Step 6: "After the last voice, before any other section, output exactly: TALLY:" |
| C-15 | `STANCE:` label is structural | **PASS** | Standalone labeled line in voice format code block; "The STANCE: line is the declaration." |
| C-16 | Investigation self-check gate | **PASS** | Step 3 is a dedicated gate step: "GATE: [YES / NO]"; **"This line is required; its absence means C-16 failed."** |
| C-17 | Advocate voices grounded in investigation | **PASS** | "`CITE:` is required for every Tier 3 voice. A Tier 3 block without `CITE:` fails C-17." |
| C-18 | All-approve self-correction diagnostic | **PASS** | Step 4b dedicated sort validation: "SORT-CHECK: [... YES / NO]"; **"This line is required; its absence means C-18 failed."** Corrected sort required before Step 5. |
| C-19 | Tier 3 addresses named Tier 1/2 concern | **PASS** | "`RESPONDS-TO:` is required for every Tier 3 voice. It must reference a specific named concern — 'I acknowledge there are concerns' does not pass. A Tier 3 block without `RESPONDS-TO:` fails C-19." |

**Essential**: 5/5 = **60**
**Recommended**: 3/3 = **30**
**Aspirational**: 11/11 = **22**
**Composite: 112**

---

## Rankings

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 | **V-05** | **112** | Ceiling reached. Five named declarations, dedicated step per enforcement mechanism, criterion-ID failure labels |
| 1 | **V-02** | **112** | Ceiling reached. Template approach provides maximum structural enforcement; most reliable against omission |
| 1 | **V-01** | **112** | Ceiling reached. Lifecycle architecture now complete with Step 4b + RESPONDS-TO: |
| 1 | **V-03** | **112** | Ceiling reached. Minimum instruction surface achieving full compliance |
| 1 | **V-04** | **112** | Ceiling reached. Inertia architecture satisfies C-18 and C-19 through a different structural path |

All five variations achieve the maximum composite. The rubric is fully saturated by this round.

---

## Excellence Signals from R5

### Signal 1 — Criterion-ID failure labeling (V-05)

V-05 introduces a new enforcement pattern: each required structural field explicitly names the criterion its omission violates.

> "This line is required; its absence means **C-16** failed."
> "This line is required; its absence means **C-18** failed."

R4 and earlier rounds named fields and said "if absent, the template is visibly incomplete." V-05 goes further: it attaches the scoring criterion to the absence. This makes the enforcement self-documenting — the model knows not just that a field is required, but *which criterion it is load-bearing for*. Prior labeled declarations (GATE, SORT-CHECK, STANCE:, CITE:, RESPONDS-TO:) enforce through structural visibility. Criterion-ID labeling enforces through explicit cost articulation.

**Potential C-20 candidate**: *Criterion-ID declared at point of enforcement* — each structural required output names the criterion it satisfies, so absence is unambiguously a criterion failure, not a formatting lapse.

### Signal 2 — Step-scoped enforcement (V-05)

V-05 assigns each enforcement mechanism its own numbered step heading (Step 3 = GATE, Step 4b = SORT-CHECK, Step 5 = voices with CITE: + RESPONDS-TO:, Step 6 = TALLY, Step 7 = formal minutes). Prior variations embedded enforcement rules in paragraph bodies or rule lists. In a prompt with 11 aspirational criteria, late criteria risk attention deprioritization. Giving each criterion its own step heading creates equal visual weight across enforcement points.

**Principle formalized**: In multi-criterion prompts where all criteria must be satisfied, structural enforcement is stronger when each criterion occupies its own named scope rather than sharing a scope with other instructions.

### Signal 3 — Architectural C-19 via named finding tags (V-04)

V-04 satisfies C-19 through the INERTIA-FINDING-A/B tag mechanism rather than a generic RESPONDS-TO: field. The difference: advocates must respond to the *strongest adversarial argument* (the inertia-advocate's pre-labeled findings) rather than any Tier 1/2 concern. This can produce richer C-19 passes — the response is grounded in the most adversarially loaded peer voice, not the easiest condition to acknowledge.

**Observation**: C-19 can be satisfied by either named-field architecture (RESPONDS-TO: pointing at any Tier 1/2 concern) or named-anchor architecture (INERTIA-FINDING-A/B tags serving as pre-established mandatory response targets). The anchor architecture may raise response quality even when both formally pass.

---

## Summary

All five variations reach **112/112** — the rubric ceiling introduced by v5. The pool is fully saturated. The rubric now covers all recoverable structural invariants through labeled declarations. Further scoring iterations should focus on output quality (richness of investigation findings, depth of inertia argument, specificity of resolution paths) rather than structural presence, or on identifying edge cases that pass the structure but fail the intent.

```json
{"top_score": 112, "all_essential_pass": true, "new_patterns": ["criterion-id-failure-labeling: attaching the scoring criterion ID to each required structural field's absence condition makes enforcement self-documenting and raises the cost of omission beyond a formatting lapse", "step-scoped-enforcement: assigning each enforcement mechanism its own numbered step heading prevents attention deprioritization of later criteria in multi-criterion prompts"]}
```
