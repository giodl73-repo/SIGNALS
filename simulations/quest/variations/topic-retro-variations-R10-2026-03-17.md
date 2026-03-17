4 SEAL — verify before Phase 5:
  [ ] Every COVERED namespace has a row
  [ ] TOTAL row present and calculated
  [ ] Formula applied to every row (denominator = 0 noted explicitly)
  [ ] Count ratio in 'N/M = X%' form directly below the table
Phase 4 verified? PHASE 4 COMPLETE.

---

PHASE 5 — AUDIT THE ECHO
{{#if amend}}[SCOPE: {{amend}} only]{{/if}}

Re-read the locked Echo from Phase 1. Ask: do Phase 3 or Phase 4 findings suggest the Echo should change?

If YES:
  Write: CONFLICT DETECTED
  Source: [which Phase 3 verdict or Phase 4 score creates the tension]
  Proposed revision: [what the Echo would say if revised]
  Resolution: Keep Phase 1 Echo unchanged. Log this as the conflict artifact.

If NO:
  Write: CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL — verify before Phase 6:
  [ ] Audit question answered
  [ ] If YES: conflict artifact present with all three required fields
  [ ] If NO: explicit "No conflict" statement present
Phase 5 verified? PHASE 5 COMPLETE.

---

PHASE 6 — STATE THE ACCURACY VERDICT
Write the accuracy verdict using Phase 4 TOTAL only:

  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)] | Count ratio: [N/M = X%]"

Do not recompute. Do not introduce new observations. Copy Phase 4 numbers directly.

PHASE 6 SEAL — verify before Phase 7:
  [ ] Verdict sentence uses the required format
  [ ] Weighted score: '[n]/100' — copied from Phase 4 TOTAL, not recalculated
  [ ] Count ratio: '[N/M = X%]' — copied from Phase 4, not recalculated
  [ ] Tier label matches the score
Phase 6 verified? PHASE 6 COMPLETE.

---

PHASE 7 — IDENTIFY GAPS
{{#if amend}}[SCOPE: {{amend}} only]{{/if}}

For every namespace that scored W or P in Phase 3, and every EMPTY namespace with material absence, write a gap row.

COLUMN ISOLATION CONTRACT
This table contains two explanatory columns that are structurally separate and answer different questions:

  Column [Assumption held without evidence]
  Content type: PRIOR BELIEF — the inertia assumption the team held before commit that made this gap invisible
  Question answered: WHY was this signal not gathered?
  Required content form: "We assumed [X] was [Y]" or "We believed [X] did not require [signal type]"
  Prohibited content: outcome descriptions, discovery statements, or content matching the "Would have surfaced" column

  Column [Would have surfaced]
  Content type: DISCOVERY — what the signal would have revealed if gathered
  Question answered: WHAT would this signal have shown?
  Required content form: "[Signal type] would have shown [finding]" or "[Namespace] would have revealed [X]"
  Prohibited content: prior beliefs, assumption statements, or content matching the "Assumption" column

A gap row where both columns state the same type of content is structurally incomplete — rewrite before sealing.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [WHY: prior belief — content type PRIOR BELIEF — do not copy Would-have-surfaced content] | [exact skill from catalog] | [WHAT: discovery missed — content type DISCOVERY — do not copy Assumption content] | [YES / NO] |

Name an exact skill for every row. "Gather more data" fails.
Write "No gaps — signal coverage was sufficient" only if no namespace scored W or P and no EMPTY namespace is material.

Write the improvement recommendation using this template — no slot may remain as a placeholder:
  > **Recommendation**: Addresses [Gap: signal-type OR Echo: pattern-name] by [specific practice change — not "improve process"] so that [measurable outcome — not "things improve"].

PHASE 7 SEAL — verify before Phase 8:
  [ ] Every W or P namespace has a gap row
  [ ] Every materially absent EMPTY namespace has a gap row
  [ ] Assumption column: content type = PRIOR BELIEF (states WHY, not an outcome, not "unknown", not blank)
  [ ] Would-have-surfaced column: content type = DISCOVERY (states WHAT, distinct from Assumption in content type)
  [ ] Column isolation check: Assumption and Would-have-surfaced cells do not restate each other
  [ ] Skill column: exact named skill per row (not "gather more data")
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation: all three slots filled with specific content — no '[placeholder]' strings remain
Phase 7 verified? PHASE 7 COMPLETE.

---

PHASE 8 — TRACK CALIBRATION TREND
{{#if amend}}[SCOPE: {{amend}} only]{{/if}}

| Prior retro (topic / date) | Prior weighted score | This weighted score | Delta | Trend |
|---------------------------|---------------------|---------------------|-------|-------|
| [reference or "none"] | [prior or "—"] | [Phase 4 TOTAL weighted score — copy exactly, do not recompute] | [±n or "—"] | ↑ / ↓ / = |

No prior retro: write "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — verify before Phase 9:
  [ ] Prior retro: '[topic / date]' or '"none"'
  [ ] This weighted score: '[n]' — must match Phase 4 TOTAL exactly; verify against Phase 4 before writing
  [ ] Delta: '[±n]' computed from Prior and This (or "—" for first retro)
  [ ] Trend: '↑' or '↓' or '=' (or "first retro" statement)
Phase 8 verified? PHASE 8 COMPLETE.

---

PHASE 9 — DESIGN THE SIGNAL CHANGE
Translate the Phase 1 Echo and Pattern into one concrete signal gathering change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [copy Echo verbatim — do not paraphrase] | [copy Pattern name verbatim] | [one specific change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — final gate:
  [ ] Echo: '[verbatim from Phase 1]' — verify it matches Phase 1 character-for-character
  [ ] Pattern name: '[verbatim from Phase 1]' — verify it matches Phase 1 exactly
  [ ] Proposed change: specific and actionable (not "gather more data")
  [ ] Change type: exactly one of: new skill / rubric amendment / threshold adjustment
Phase 9 verified? PHASE 9 COMPLETE.

---

RETRO MASTER SEAL — confirm all phase seals before marking the retro complete:
  [ ] Phase 1 (Echo) SEAL confirmed — Echo, Pattern, Why unexpected locked
  [ ] Phase 2 (Inventory) SEAL confirmed — all 9 namespace rows present
  [ ] Phase 3 (Predicted vs Actual) SEAL confirmed — no blank cells
  [ ] Phase 4 (Accuracy) SEAL confirmed — TOTAL row + N/M = X% ratio present
  [ ] Phase 5 (Conflict Audit) SEAL confirmed — audit answered
  [ ] Phase 6 (Verdict) SEAL confirmed — verdict sentence in required format
  [ ] Phase 7 (Gap Analysis) SEAL confirmed — column isolation check passed  [Phase 7: gap analysis — confirmed in registry]
  [ ] Phase 8 (Calibration) SEAL confirmed — score matches Phase 4 TOTAL exactly  [Phase 8: calibration — confirmed in registry]
  [ ] Phase 9 (Signal Design) SEAL confirmed — Echo and Pattern match Phase 1 verbatim
All 9 phases sealed? RETRO COMPLETE.

---

Work through phases strictly in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
A phase is complete only when its SEAL is verified. Never defer required fields to a later phase.
In Phase 7: the COLUMN ISOLATION CONTRACT is a structural pre-condition. Assumption = PRIOR BELIEF (WHY). Would have surfaced = DISCOVERY (WHAT). A row where both columns state the same content type fails the column isolation check and blocks Phase 7 SEAL confirmation.
In Phase 8: copy the weighted score from Phase 4 TOTAL directly — do not recompute. A discrepancy between Phase 6 and Phase 8 is a copying error, not a scoring revision.
```

---

## Variation Summary

| Variation | Axis | Primary hypothesis | C-26 mechanism | C-27 mechanism |
|-----------|------|--------------------|----------------|----------------|
| V-01 | Inertia framing | Column Isolation Contract as pre-table block makes C-26 explicit | COLUMN ISOLATION CONTRACT block + content-type SEAL checks | Inherited from base (per-phase seals 1–9) |
| V-02 | Lifecycle emphasis | Phase Registry + Master Seal makes C-27 explicit | Inherited from base (separate columns) | PHASE REGISTRY top-level + RETRO MASTER SEAL enumeration |
| V-03 | Phrasing register | Imperative-direct voice improves phases 7/8 completion rate | Inherited from base (separate columns, WHY/WHAT framing) | Inherited from base (per-phase seals 1–9) |
| V-04 | Inertia + Lifecycle | C-26 and C-27 both explicit; no register change | V-01 mechanism | V-02 mechanism |
| V-05 | All three + precision | Full ceiling variation; adds Phase 8 score-copy guard and recommendation slot guard | V-01 mechanism | V-02 mechanism |

**Regression risk:** V-03 removes the explicit COLUMN ISOLATION CONTRACT. If a scorer reads C-26's "structurally separate columns" requirement as requiring a named pre-condition block (not just separate columns + prose instruction), V-03 may score C-26 at PARTIAL. This would confirm that V-01's explicit contract is load-bearing for C-26.
