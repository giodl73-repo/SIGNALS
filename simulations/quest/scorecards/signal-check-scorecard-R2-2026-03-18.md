## signal-check R2 — Scoring Complete

**Scorecard:** `simulations/quest/scorecards/signal-check-scorecard-R2-2026-03-18.md`

### Results

| V | Label | Composite | Gold? | Failed |
|---|-------|-----------|-------|--------|
| V-04 | Absence + skill format | **100** | YES | — |
| V-05 | Full v2 canonical stack | **100** | YES | — |
| V-01 | Explicit absence enforcement | **98** | YES | C-11 |
| V-02 | Strict skill-format enforcement | **98** | YES | C-13 |
| V-03 | Lifecycle emphasis shift | **96** | YES | C-11, C-13 |

All five pass gold. Three new patterns extracted.

### Research question answers

1. **Does absence prohibition alone close C-13?** Yes — V-01 passes C-13. The key was propagating the prohibition to all four dimensions, not just CAUSAL GAP. V-02 confirms the inverse: a rule confined to one section leaves the other three unprotected.

2. **Does a preamble-level skill-format rule propagate to inline references?** Yes — but only when the constraint explicitly names every output location ("applies to readiness summary, all action fields, cross-dimension patterns, and MISSING SIGNAL GUIDE. No exceptions."). V-01 without that preamble block fails C-11 at readiness summary and cross-dimension patterns.

3. **Does depth inversion improve C-09 without degrading C-06/C-07?** C-09 and C-06/C-07 both pass in V-03. Depth does not degrade compressed dimensions. But depth is orthogonal to enforcement — V-03 still fails C-11 and C-13 because the axis was instructional depth, not constraint propagation.

### New patterns

- **EX-04:** Named STANDING RULES block before inventory — what separates 100 from 98
- **EX-05:** Required verbatim forms per dimension — exact phrases over structural guidance
- **EX-06:** Constraint scope must name every output location explicitly

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named STANDING RULES block before inventory — elevates enforcement constraints to named rules that propagate system-wide without per-section repetition", "Required verbatim forms per dimension — exact required phrases force explicit absence declarations rather than structural guidance alone", "Constraint scope must enumerate each output location explicitly — a rule naming only one dimension does not propagate to others"]}
```
----|---------------|
| C-01 | E | PASS | All four sections present |
| C-02 | E | PASS | Basis: "if no discovery artifacts exist, state this"; Finding: "absence declaration if no discovery" |
| C-03 | E | PASS | "State agreement or contradiction specifically — named pairs required" |
| C-04 | E | PASS | "(a) or (b) — required; silence does not pass" |
| C-05 | E | PASS | "Coaching check, not a gate" |
| C-06 | R | PASS | Threshold: "signals older than [N] days" — number required |
| C-07 | R | PASS | Action with /namespace:skill required in all sections |
| C-08 | R | PASS | READINESS SUMMARY with skill-format REMINDER |
| C-09 | A | PASS | CROSS-DIMENSION PATTERNS with /namespace:skill action for shared root |
| C-10 | A | PASS | MISSING SIGNAL GUIDE with format REMINDER |
| C-11 | A | PASS | SKILL REFERENCE FORMAT block at preamble: "applies to readiness summary, all action fields, cross-dimension patterns, and MISSING SIGNAL GUIDE. No exceptions." Per-section repetition. |
| C-12 | A | PASS | Terminal MISSING SIGNAL GUIDE with "Do not use bare skill names here" REMINDER |
| C-13 | A | **FAIL** | Absence rule enforced only in CAUSAL GAP ("silence does not pass"). SEQUENCE: "state this" — weak, no prohibition. STALENESS: no absence rule. COHERENCE: "or absence" — no prohibition. Not system-wide. |

**Composite: 60 + 30 + 8 = 98. Gold: YES.**

---

### V-03: Lifecycle emphasis shift (depth inversion)

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | E | PASS | DEEP: CAUSAL GAP and SEQUENCE; COMPACT: STALENESS and COHERENCE — all four present |
| C-02 | E | PASS | Deep SEQUENCE: step-by-step dating; option (c) verbatim form; "Do not assert an order without dating evidence" |
| C-03 | E | PASS | Compact COHERENCE has agreement/contradiction/no-pair verbatim forms |
| C-04 | E | PASS | Deep CAUSAL GAP: four-step procedure; "Silence does not pass. Hedging does not pass." |
| C-05 | E | PASS | "Not a gate. Nothing here produces a verdict that blocks you." |
| C-06 | R | PASS | "Name it; 'recent enough' without a number does not pass." |
| C-07 | R | PASS | Action fields in all four sections |
| C-08 | R | PASS | READINESS SUMMARY placed first |
| C-09 | A | PASS | "Look especially for root connections between CAUSAL GAP and SEQUENCE"; common pattern named |
| C-10 | A | PASS | MISSING SIGNAL GUIDE with namespace+skill format |
| C-11 | A | **FAIL** | No STANDING RULES. CROSS-DIMENSION PATTERNS: "name the action" — no /namespace:skill requirement. READINESS SUMMARY: no format reminder. Action field hints present but not preamble-level. |
| C-12 | A | PASS | Terminal MISSING SIGNAL GUIDE |
| C-13 | A | **FAIL** | CAUSAL GAP: "Silence does not pass." SEQUENCE: option (c) form available but no prohibition. STALENESS compact block: no absence rule for undated artifacts. COHERENCE: "No comparable pair" form but no prohibition. System-wide rule never declared. |

**Composite: 60 + 30 + 6 = 96. Gold: YES.**

---

### V-04: Absence enforcement + strict skill format (combination)

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | E | PASS | All four in DIMENSION ANALYSIS |
| C-02 | E | PASS | SEQUENCE Finding: "Absence rule: if no discovery artifacts, this form is required." Verbatim form enforced. |
| C-03 | E | PASS | COHERENCE: "Absence rule required when no pair exists." Named pairs required. |
| C-04 | E | PASS | "(b) must be written when no mechanism evidence exists; blank finding does not pass" |
| C-05 | E | PASS | "Coaching check — not a gate. Advisory throughout." |
| C-06 | R | PASS | "Name threshold first: 'signals older than [N] days are stale because [reason].'" |
| C-07 | R | PASS | "Action: required if FLAG or OPEN; must use /namespace:skill format" |
| C-08 | R | PASS | READINESS SUMMARY: "Name any gap-closing skill using /namespace:skill format." |
| C-09 | A | PASS | CROSS-DIMENSION PATTERNS: "If two or more share a common root, name it." Action using /namespace:skill for root. |
| C-10 | A | PASS | MISSING SIGNAL GUIDE: "[Dimension] gap: run /[namespace]:[skill]" |
| C-11 | A | PASS | STANDING RULES Rule 2: "Every skill reference uses /namespace:skill format... applies to readiness summary, all action fields, cross-dimension patterns, MISSING SIGNAL GUIDE. No exceptions." Per-section reminders. |
| C-12 | A | PASS | Terminal MISSING SIGNAL GUIDE with "All skill references must use /namespace:skill format" |
| C-13 | A | PASS | STANDING RULES Rule 1: "For every dimension where relevant evidence is absent, write the absence explicitly... Silence does not pass." System-wide. Per-dimension required forms enforced. |

**Composite: 60 + 30 + 10 = 100. Gold: YES.**

---

### V-05: Full v2 canonical stack

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | E | PASS | Items 1-4: CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE in THE PREFLIGHT CHECK |
| C-02 | E | PASS | Form (c) "required when no discovery artifacts exist — do not write SEQUENCE OK when nothing was checked" |
| C-03 | E | PASS | Agreement/contradiction/no-pair verbatim forms; named artifact pairs required |
| C-04 | E | PASS | "Form (b) is required when no mechanism evidence exists. Silence does not pass." |
| C-05 | E | PASS | Preflight metaphor; "The checklist does not decide whether to fly." Coaching throughout. |
| C-06 | R | PASS | "For {topic}'s domain: signals older than [N] days are stale because [reason]." |
| C-07 | R | PASS | "What you can do:" section per item; Action required for FLAG/OPEN |
| C-08 | R | PASS | READINESS SUMMARY first, with /namespace:skill format reminder |
| C-09 | A | PASS | CROSS-ITEM PATTERNS: three named patterns with examples and root-action using /namespace:skill |
| C-10 | A | PASS | MISSING SIGNAL GUIDE with four worked format examples |
| C-11 | A | PASS | STANDING RULES Rule 2 + "No bare names anywhere" + per-action-field reminders + MISSING SIGNAL GUIDE examples |
| C-12 | A | PASS | Dedicated terminal MISSING SIGNAL GUIDE with four worked examples |
| C-13 | A | PASS | STANDING RULES Rule 1 + per-item absence forms with required verbatim phrases at every dimension |

**Composite: 60 + 30 + 10 = 100. Gold: YES.**

---

## Research question answers

**RQ1 — Does absence prohibition alone (V-01) close C-13 independently, or do structural slots do the same work?**

V-01 PASSES C-13. Explicit prohibition language ("Silence does not pass") applied system-wide at every dimension is sufficient to close C-13. The prohibition works because it was propagated to all four sections — not just CAUSAL GAP. V-02 confirms the inverse: confining the rule to one dimension means the other three remain unprotected.

**RQ2 — Does a preamble-level skill-format rule (V-02) propagate to inline references?**

V-02 PASSES C-11. A preamble-level SKILL REFERENCE FORMAT block propagates to all output locations IF the constraint explicitly names each location ("applies to the readiness summary, all action fields, the cross-dimension patterns section, and the MISSING SIGNAL GUIDE"). V-01 confirms the inverse: per-section action-field hints without a preamble constraint do not propagate to the readiness summary or cross-dimension patterns.

**RQ3 — Does depth inversion (V-03) improve C-09 without degrading C-06/C-07?**

V-03 PASSES C-09 and C-06/C-07. Depth inversion does not degrade compressed dimensions. However, V-03 failed C-11 and C-13 because the axis was instructional depth — not enforcement. Deeper analysis does not substitute for explicit enforcement rules. C-09 improvement is plausible (the CROSS-DIMENSION PATTERNS note explicitly connects CAUSAL GAP and SEQUENCE) but could not be confirmed without runtime evidence.

---

## Excellence signals

**EX-04: Named STANDING RULES block before inventory**
Elevating enforcement constraints to named rules (Rule 1, Rule 2) before the analysis begins propagates them to every output location without per-section repetition. Both V-04 and V-05 use this pattern; it is what separates composite 100 from 98. The lesson: a constraint needs a named, preamble-level identity to propagate — unnamed per-section hints do not generalize.

**EX-05: Required verbatim forms per dimension**
Each dimension gets a specific required phrase template (e.g., "No mechanism evidence found. The causal gap is open.") that must be written verbatim. Required verbatim forms close the gap between implied structural guidance and enforced output. This is what makes absence declarations reliable: the model has exact words, not a general instruction.

**EX-06: Constraint scope must be explicitly named**
A constraint stated at preamble level passes C-11/C-13 only when it explicitly enumerates every output location where it applies ("applies to readiness summary, all action fields, cross-dimension patterns, and MISSING SIGNAL GUIDE. No exceptions."). A rule that mentions only CAUSAL GAP does not propagate to STALENESS or COHERENCE. Scope specificity in the constraint determines coverage in the output.

---

## Next round direction

All five variations pass gold. The three R2 research questions are answered. V-04 and V-05 are tied at 100 and establish the v2 rubric ceiling.

V-05 is qualitatively superior to V-04 in three ways that criteria alone do not capture:
1. "What we're checking / What we found / What you can do" structure frames each item as a decision-support briefing, not a checklist
2. Three named cross-item patterns with worked examples reduce C-09 drift
3. Worked MISSING SIGNAL GUIDE examples reduce bare-name drift at the terminal guide

V-05 is the R2 canonical prompt. Future rounds should test runtime compliance against live artifact inventories.

---

## Output JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named STANDING RULES block before inventory — elevates enforcement constraints to named rules that propagate system-wide without per-section repetition", "Required verbatim forms per dimension — exact required phrases force explicit absence declarations rather than structural guidance alone", "Constraint scope must enumerate each output location explicitly — a rule naming only one dimension does not propagate to others"]}
```
