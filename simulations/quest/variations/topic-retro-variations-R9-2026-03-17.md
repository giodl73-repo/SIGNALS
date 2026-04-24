Now I have everything I need. Let me write the R9 variations. The base is R7-V05 (full integration, 116/116 ceiling). New targets: C-24 (Echo Why-Unexpected) and C-25 (Recommendation Outcome Measurable).

---

# topic-retro — Variations R9
**Date:** 2026-03-17
**Rubric:** v7 (C-01 through C-25; total available = 124)
**R8 basis:** V-02 from R8 (best non-combined at v6 scoring). R7-V05 is the structural ceiling — all prior PARTIAL criteria resolved. New criteria from R8 promotion: C-24 (echo-why-unexpected-named) and C-25 (recommendation-outcome-measurable).

**New criteria to target:**
- C-24: Echo section carries an explicit field naming *why* the finding was unexpected — the prior belief or model contradicted. Label alone = PARTIAL. `Why unexpected: [prior model or assumption contradicted]` form = PASS.
- C-25: Recommendation includes a third slot: measurable outcome. Full contract: "address [gap/echo] by [practice change] so that [measurable outcome]." Gap + change without measurable outcome = PARTIAL.

**Variation strategy:**
Single-axis: V-01 (C-24 via labeled prose field), V-02 (C-25 via three-slot template), V-03 (C-24 via output format restructure — two-row Echo table).
Combined: V-04 (C-24 + C-25), V-05 (C-24 + C-25 + full R7-V05 integration).

---

## V-01 — Echo-Belief: C-24 via "Why unexpected" labeled field after Echo table

**Axis:** C-24 mechanism — Phase 1 adds a required labeled field immediately after the Echo table and Pattern entry:

```
Why unexpected: [prior model or assumption contradicted — the belief the team held that this Echo overturned]
```

The field is structurally required: a blank or label-only value ("unexpected" restated) fails the Phase 1 SEAL. The "Why unexpected" field is not the Echo itself (which names the finding) and not the Pattern (which names the failure class) — it names what the author *expected to see* before ship and why reality diverged from that expectation.

**Hypothesis:** C-24 scores PARTIAL on variants that label the Echo as unexpected but never require the author to state the contradicted belief. Adding a named field after the Pattern entry forces belief-correction to be written explicitly. The SEAL checks that the field is populated with a belief statement (`We believed X` or equivalent) — not blank, not a restatement of the Echo, not the Pattern. This is the minimal single-axis change from the R7-V05 base that directly targets C-24.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, identify gaps. Each phase ends with a PHASE SEAL — an explicit field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

PHASE 1 — ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only — outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table, name the systemic pattern:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — not a restatement of the Echo, but the class of failure it belongs to]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

Then state why the Echo was unexpected:
  > **Why unexpected**: [the prior model, belief, or assumption the team held that this Echo contradicted — not a restatement of the finding, not the Pattern label, but the belief that made this outcome surprising]

The "Why unexpected" field must name what was expected before ship and why reality contradicted it. If no Echo: write "N/A — no Echo, no prior belief contradicted."

LOCK: Echo table, Pattern entry, and Why unexpected field are final. Phases 2–8 may not change them.

PHASE 1 SEAL — all fields must be explicitly populated before Phase 2 begins:
  [ ] Echo cell: exactly one sentence OR the exact string "No Echo — all post-ship outcomes were within signal bounds" (not blank, not a paraphrase of a wrong prediction)
  [ ] Nearest signal: a named artifact filename OR the exact string "none" (not blank)
  [ ] Commit relevance: exactly HIGH, MEDIUM, or LOW (or "N/A" only paired with "No Echo")
  [ ] Pattern: "> **Pattern**: [name] — [failure class description]" (not blank, not generic, not a restatement of the Echo)
  [ ] Why unexpected: "> **Why unexpected**: [named prior belief or model contradicted]" (not blank, not "unexpected", not a restatement of the Echo or Pattern — must name what the team believed before ship)
  {{#if amend}}[ ] AMEND scope marker present immediately above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status     | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| draft     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| review    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| flow      | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| trace     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| prove     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| listen    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| program   | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| topic     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| TOTAL     |            | N |                   |                    |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — all items required before Phase 3 begins:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY" (no other value, no blank)
  [ ] Every Artifact count cell: a number (0 is valid for EMPTY; blank is not)
  [ ] TOTAL row present with summed count
  {{#if amend}}[ ] OOS table present immediately after main table (even if "No artifacts excluded"){{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL:
  [ ] Every COVERED namespace from Phase 2 has exactly one row
  [ ] No Predicted cell is blank or contains only "N/A"
  [ ] No Actual cell is blank or contains only "N/A"
  [ ] Every Match cell: exactly C, P, W, or ND (no other values)
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table, state the count-based accuracy ratio:
  Correct signals: [count of C rows] / [count of C+P+W rows] = X%
  (Count-based ratio — not weighted. Both numbers required.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present with weighted formula applied
  [ ] Count-based accuracy ratio stated in N/M = X% format immediately below scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces one of two outputs.

Review the locked Phase 1 Echo.
Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [Phase 3 row / Phase 4 score — which specific finding creates the tension]
  Analysis: [what the finding suggests the Echo should be]
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of the two outputs present: either CONFLICT DETECTED block (with Source, Analysis, Resolution all present) or the exact "No conflict" declaration
  [ ] Nothing in Phase 5 modifies the Phase 1 Echo table, Pattern entry, or Why unexpected field
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence present in the exact required format (both weighted score and count ratio)
  [ ] Weighted score matches Phase 4 TOTAL row (same number, not recalculated)
  [ ] Count ratio matches Phase 4 N/M = X% statement (same values)
  [ ] Tier label (STRONG / ADEQUATE / WEAK) matches the stated weighted score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

A gap entry has two required explanatory fields that must state different things:
  - "Assumption held without evidence": the inertia belief that made this gap invisible before commit. Why the team did not gather this signal. Framed as a prior belief ("We assumed X"), not as an outcome.
  - "Would have surfaced": what this signal would have revealed. The discovery that was missed. This is the outcome; the Assumption is the belief that prevented gathering it.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [prior belief, e.g., "We assumed X was true without evidence"] | [exact skill, e.g., /listen-support] | [what the signal would have revealed — distinct from the Assumption column] | YES / NO |

The Assumption and "Would have surfaced" columns must contain different statements addressing different questions. If they are the same statement, one column is wrong.

"Gather more data" does not satisfy the Skill column. Name an exact Signal namespace skill.
No gaps: "No gaps — signal coverage was sufficient for this commit decision."

> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 7 SEAL:
  [ ] Every W or P namespace from Phase 3 has a gap row (or "no gaps" statement)
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Assumption column: a prior belief per row — framed as a belief ("We assumed X"), not an outcome, not blank, not "unknown"
  [ ] "Would have surfaced" column: a discovery statement per row — distinct from Assumption (answers "what", not "why")
  [ ] Skill column: exact Signal skill name per row (not a namespace name, not "gather more data")
  [ ] Changed commit: exactly YES or NO per row
  [ ] Recommendation template present with Gap/Echo name and practice change filled in
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named topic/date or exactly "none"
  [ ] This score: matches Phase 4 TOTAL weighted score (same number)
  [ ] Trend: exactly ↑, ↓, or = with a label, or "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro is complete when all confirmed:
  [ ] Echo cell: matches Phase 1 Echo cell content exactly (not paraphrased, not summarized)
  [ ] Pattern cell: matches Phase 1 Pattern name exactly (same taxonomy label used in Phase 1)
  [ ] Proposed change: specific and actionable (not generic, not "gather more data")
  [ ] Change type: exactly one of: new skill, rubric amendment, threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo table + Pattern + Why unexpected field — all three locked before Phase 2 begins. Why unexpected names the prior belief contradicted, not the Echo itself.
- Phase 2: fixed 9-row namespace table (COVERED or EMPTY only; TOTAL row required).
- Phase 4: weighted score AND N/M=X% count ratio — both required.
- Phase 6: verdict sentence includes both score formats drawn from Phase 4.
- Phase 7: two distinct columns per gap — Assumption (why invisible) and Would have surfaced (what was missed).
- Every phase seal enumerates exact required content with format strings.
- When AMEND is set: every table has a scope marker and Phase 2 has an OOS secondary table.

Each phase seal is a self-containedness contract. A phase that cannot pass its own seal is incomplete — do not proceed.
```

---

## V-02 — Three-Slot-Rec: C-25 via measurable outcome slot in recommendation template

**Axis:** C-25 mechanism — Phase 7 recommendation template expands from two slots to three. Current: "Addresses [gap/echo] by [practice change]." New: "Addresses [gap/echo] by [practice change] so that [measurable outcome]." The Phase 7 SEAL adds a check item verifying all three slots are present and the measurable outcome states what would be observably different if the practice change succeeded.

**Hypothesis:** C-25 scores PARTIAL on variants where the recommendation template enforces gap linkage and practice change (C-07/C-17) but leaves the measurable outcome as optional prose. The "so that" clause makes the outcome slot structural — it appears in the template itself, not in annotation or guidance text. The SEAL checks that all three slots are filled: a recommendation with gap and change but no measurable outcome fails the seal check. This is the minimal single-axis change from the R7-V05 base that directly targets C-25.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, identify gaps. Each phase ends with a PHASE SEAL — an explicit field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

PHASE 1 — ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only — outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table, name the systemic pattern:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — not a restatement of the Echo, but the class of failure it belongs to]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table and Pattern entry are final. Phases 2–8 may not change them.

PHASE 1 SEAL — all fields must be explicitly populated before Phase 2 begins:
  [ ] Echo cell: exactly one sentence OR the exact string "No Echo — all post-ship outcomes were within signal bounds" (not blank, not a paraphrase of a wrong prediction)
  [ ] Nearest signal: a named artifact filename OR the exact string "none" (not blank)
  [ ] Commit relevance: exactly HIGH, MEDIUM, or LOW (or "N/A" only paired with "No Echo")
  [ ] Pattern: "> **Pattern**: [name] — [failure class description]" (not blank, not generic, not a restatement of the Echo)
  {{#if amend}}[ ] AMEND scope marker present immediately above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status     | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| draft     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| review    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| flow      | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| trace     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| prove     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| listen    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| program   | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| topic     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| TOTAL     |            | N |                   |                    |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — all items required before Phase 3 begins:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY" (no other value, no blank)
  [ ] Every Artifact count cell: a number (0 is valid for EMPTY; blank is not)
  [ ] TOTAL row present with summed count
  {{#if amend}}[ ] OOS table present immediately after main table (even if "No artifacts excluded"){{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL:
  [ ] Every COVERED namespace from Phase 2 has exactly one row
  [ ] No Predicted cell is blank or contains only "N/A"
  [ ] No Actual cell is blank or contains only "N/A"
  [ ] Every Match cell: exactly C, P, W, or ND (no other values)
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table, state the count-based accuracy ratio:
  Correct signals: [count of C rows] / [count of C+P+W rows] = X%
  (Count-based ratio — not weighted. Both numbers required.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present with weighted formula applied
  [ ] Count-based accuracy ratio stated in N/M = X% format immediately below scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces one of two outputs.

Review the locked Phase 1 Echo.
Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [Phase 3 row / Phase 4 score — which specific finding creates the tension]
  Analysis: [what the finding suggests the Echo should be]
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of the two outputs present: either CONFLICT DETECTED block (with Source, Analysis, Resolution all present) or the exact "No conflict" declaration
  [ ] Nothing in Phase 5 modifies the Phase 1 Echo table or Pattern entry
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence present in the exact required format (both weighted score and count ratio)
  [ ] Weighted score matches Phase 4 TOTAL row (same number, not recalculated)
  [ ] Count ratio matches Phase 4 N/M = X% statement (same values)
  [ ] Tier label (STRONG / ADEQUATE / WEAK) matches the stated weighted score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

A gap entry has two required explanatory fields that must state different things:
  - "Assumption held without evidence": the inertia belief that made this gap invisible before commit. Why the team did not gather this signal. Framed as a prior belief ("We assumed X"), not as an outcome.
  - "Would have surfaced": what this signal would have revealed. The discovery that was missed. This is the outcome; the Assumption is the belief that prevented gathering it.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [prior belief, e.g., "We assumed X was true without evidence"] | [exact skill, e.g., /listen-support] | [what the signal would have revealed — distinct from the Assumption column] | YES / NO |

The Assumption and "Would have surfaced" columns must contain different statements addressing different questions.

"Gather more data" does not satisfy the Skill column. Name an exact Signal namespace skill.
No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Use this template exactly — all three slots are required:
  > **Recommendation**: Addresses [Gap: signal-type / Echo: pattern-name] by [specific practice change — what process or skill is added or modified] so that [measurable outcome — what would be observably different if this practice change succeeded].

The measurable outcome is not the practice change restated. It names the observable change in future accuracy, coverage, or decision quality that confirms the practice change worked.

PHASE 7 SEAL:
  [ ] Every W or P namespace from Phase 3 has a gap row (or "no gaps" statement)
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Assumption column: a prior belief per row — framed as a belief ("We assumed X"), not an outcome, not blank, not "unknown"
  [ ] "Would have surfaced" column: a discovery statement per row — distinct from Assumption (answers "what", not "why")
  [ ] Skill column: exact Signal skill name per row (not a namespace name, not "gather more data")
  [ ] Changed commit: exactly YES or NO per row
  [ ] Recommendation: three slots present — [Gap/Echo name] + [practice change] + [measurable outcome] (partial template with only two slots fails this check)
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named topic/date or exactly "none"
  [ ] This score: matches Phase 4 TOTAL weighted score (same number)
  [ ] Trend: exactly ↑, ↓, or = with a label, or "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro is complete when all confirmed:
  [ ] Echo cell: matches Phase 1 Echo cell content exactly (not paraphrased, not summarized)
  [ ] Pattern cell: matches Phase 1 Pattern name exactly (same taxonomy label used in Phase 1)
  [ ] Proposed change: specific and actionable (not generic, not "gather more data")
  [ ] Change type: exactly one of: new skill, rubric amendment, threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 2: fixed 9-row namespace table (COVERED or EMPTY only; TOTAL row required).
- Phase 4: weighted score AND N/M=X% count ratio — both required.
- Phase 6: verdict sentence includes both score formats drawn from Phase 4.
- Phase 7: two distinct columns per gap (Assumption + Would have surfaced); recommendation requires three slots — gap/echo, practice change, measurable outcome.
- Every phase seal enumerates exact required content with format strings.
- When AMEND is set: every table has a scope marker and Phase 2 has an OOS secondary table.

The recommendation template's "so that [measurable outcome]" clause is structural, not optional. A recommendation with gap and change but no observable success condition fails the Phase 7 SEAL.
Each phase seal is a self-containedness contract. A phase that cannot pass its own seal is incomplete — do not proceed.
```

---

## V-03 — Belief-Row: C-24 via two-row Echo table restructure

**Axis:** Output format — Phase 1 Echo section restructures from a single-row table to a two-row table. Row 1 carries the Echo finding, artifact, and commit relevance (the current structure). Row 2 carries "Why unexpected" — the prior belief the Echo contradicted — as a named structural row, not prose. The table schema forces the belief-correction into a labeled cell rather than a free-form post-table statement.

**Hypothesis:** V-01 places "Why unexpected" as a labeled prose field after the Pattern entry. This satisfies C-24 structurally but places the field in a secondary position where it can be treated as annotation. Making "Why unexpected" a named row in the Echo table itself (same visual weight as the Echo sentence) signals that it is primary output, not annotation. The two-row structure also makes the SEAL check unambiguous: the row must be present with non-blank content, the same guarantee as C-14's verdict-column mechanism applied to Echo content. This is a distinct mechanism from V-01 that tests whether table structure outperforms post-table prose for C-24.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, identify gaps. Each phase ends with a PHASE SEAL — an explicit field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

PHASE 1 — ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only — outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: set Echo row to "No Echo — all post-ship outcomes were within signal bounds" and Why unexpected row to "N/A".

Output a two-row Echo table. Both rows are required:

| Field | Content |
|-------|---------|
| Echo | [one-sentence finding OR "No Echo — all post-ship outcomes were within signal bounds"] |
| Why unexpected | [the prior model, belief, or assumption this finding contradicted — what the team expected before ship and why reality diverged. Not the Echo restated. Not "unexpected" as a label. Named prior belief required.] |

Supporting fields (same table, additional columns in practice — presented as separate labeled rows here for clarity):

| Field | Content |
|-------|---------|
| Nearest signal | [artifact filename or "none"] |
| Commit relevance | [HIGH / MEDIUM / LOW or "N/A" when paired with No Echo] |

Immediately after the table, name the systemic pattern:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — not a restatement of the Echo, but the class of failure it belongs to]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: All Echo table rows and Pattern entry are final. Phases 2–8 may not change them.

PHASE 1 SEAL — all fields must be explicitly populated before Phase 2 begins:
  [ ] Echo row: exactly one sentence OR the exact string "No Echo — all post-ship outcomes were within signal bounds" (not blank, not a paraphrase of a wrong prediction)
  [ ] Why unexpected row: a named prior belief or model that the Echo contradicted (not blank, not "unexpected" as a label, not a restatement of the Echo sentence — must state what was expected before ship)
  [ ] Nearest signal row: a named artifact filename OR the exact string "none" (not blank)
  [ ] Commit relevance row: exactly HIGH, MEDIUM, or LOW (or "N/A" only paired with No Echo)
  [ ] Pattern: "> **Pattern**: [name] — [failure class description]" (not blank, not generic, not a restatement of the Echo)
  {{#if amend}}[ ] AMEND scope marker present immediately above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status     | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| draft     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| review    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| flow      | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| trace     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| prove     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| listen    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| program   | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| topic     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| TOTAL     |            | N |                   |                    |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — all items required before Phase 3 begins:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY" (no other value, no blank)
  [ ] Every Artifact count cell: a number (0 is valid for EMPTY; blank is not)
  [ ] TOTAL row present with summed count
  {{#if amend}}[ ] OOS table present immediately after main table (even if "No artifacts excluded"){{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL:
  [ ] Every COVERED namespace from Phase 2 has exactly one row
  [ ] No Predicted cell is blank or contains only "N/A"
  [ ] No Actual cell is blank or contains only "N/A"
  [ ] Every Match cell: exactly C, P, W, or ND (no other values)
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table, state the count-based accuracy ratio:
  Correct signals: [count of C rows] / [count of C+P+W rows] = X%
  (Count-based ratio — not weighted. Both numbers required.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present with weighted formula applied
  [ ] Count-based accuracy ratio stated in N/M = X% format immediately below scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces one of two outputs.

Review the locked Phase 1 Echo table.
Does any Phase 3 verdict or Phase 4 score suggest the Echo row should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [Phase 3 row / Phase 4 score — which specific finding creates the tension]
  Analysis: [what the finding suggests the Echo should be]
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of the two outputs present: either CONFLICT DETECTED block (with Source, Analysis, Resolution all present) or the exact "No conflict" declaration
  [ ] Nothing in Phase 5 modifies any Phase 1 Echo table row or Pattern entry
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence present in the exact required format (both weighted score and count ratio)
  [ ] Weighted score matches Phase 4 TOTAL row (same number, not recalculated)
  [ ] Count ratio matches Phase 4 N/M = X% statement (same values)
  [ ] Tier label (STRONG / ADEQUATE / WEAK) matches the stated weighted score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

A gap entry has two required explanatory fields that must state different things:
  - "Assumption held without evidence": the inertia belief that made this gap invisible before commit. Why the team did not gather this signal. Framed as a prior belief ("We assumed X"), not as an outcome.
  - "Would have surfaced": what this signal would have revealed. The discovery that was missed. This is the outcome; the Assumption is the belief that prevented gathering it.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [prior belief, e.g., "We assumed X was true without evidence"] | [exact skill, e.g., /listen-support] | [what the signal would have revealed — distinct from the Assumption column] | YES / NO |

The Assumption and "Would have surfaced" columns must contain different statements addressing different questions.

"Gather more data" does not satisfy the Skill column. Name an exact Signal namespace skill.
No gaps: "No gaps — signal coverage was sufficient for this commit decision."

> **Recommendation**: Addresses [Gap: signal-type / Echo: pattern-name] by [specific practice change].

PHASE 7 SEAL:
  [ ] Every W or P namespace from Phase 3 has a gap row (or "no gaps" statement)
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Assumption column: a prior belief per row — framed as a belief ("We assumed X"), not an outcome, not blank, not "unknown"
  [ ] "Would have surfaced" column: a discovery statement per row — distinct from Assumption (answers "what", not "why")
  [ ] Skill column: exact Signal skill name per row (not a namespace name, not "gather more data")
  [ ] Changed commit: exactly YES or NO per row
  [ ] Recommendation template present with Gap/Echo name and practice change filled in
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named topic/date or exactly "none"
  [ ] This score: matches Phase 4 TOTAL weighted score (same number)
  [ ] Trend: exactly ↑, ↓, or = with a label, or "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo row content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro is complete when all confirmed:
  [ ] Echo cell: matches Phase 1 Echo row content exactly (not paraphrased, not summarized)
  [ ] Pattern cell: matches Phase 1 Pattern name exactly (same taxonomy label used in Phase 1)
  [ ] Proposed change: specific and actionable (not generic, not "gather more data")
  [ ] Change type: exactly one of: new skill, rubric amendment, threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: two-row Echo table — "Echo" row (the finding) and "Why unexpected" row (the prior belief contradicted) are structural peers, not primary artifact and annotation.
- Phase 2: fixed 9-row namespace table (COVERED or EMPTY only; TOTAL row required).
- Phase 4: weighted score AND N/M=X% count ratio — both required.
- Phase 6: verdict sentence includes both score formats drawn from Phase 4.
- Phase 7: two distinct columns per gap — Assumption (why invisible) and Would have surfaced (what was missed).
- Every phase seal enumerates exact required content with format strings.
- When AMEND is set: every table has a scope marker and Phase 2 has an OOS secondary table.

The "Why unexpected" row is not optional annotation. It is a primary Phase 1 output on equal footing with the Echo sentence. A Phase 1 table missing the Why unexpected row has not completed Phase 1.
Each phase seal is a self-containedness contract. A phase that cannot pass its own seal is incomplete — do not proceed.
```

---

## V-04 — Belief+Rec: C-24 + C-25 combined

**Axes:** C-24 (V-01 mechanism: labeled "Why unexpected" prose field after Pattern) + C-25 (V-02 mechanism: three-slot recommendation template with measurable outcome). Both mechanisms operate in different phases (1 and 7 respectively) — no structural interference expected. This is the minimal combined variation that simultaneously targets both new R9 criteria without adding other structural changes.

**Hypothesis:** C-24 and C-25 are independent additions to different phases. The risk is not interference between the two mechanisms but length creep making the SEAL items harder to track. The combined SEAL should explicitly cross-reference both new requirements as the final checklist items for their respective phases. If V-04 scores at or above the sum of V-01 and V-02 single-axis scores minus baseline, the zero-interference assumption holds for the R9 combined case.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, identify gaps. Each phase ends with a PHASE SEAL — an explicit field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

PHASE 1 — ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only — outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table, name the systemic pattern:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — not a restatement of the Echo, but the class of failure it belongs to]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

Then state why the Echo was unexpected:
  > **Why unexpected**: [the prior model, belief, or assumption the team held that this Echo contradicted — not a restatement of the finding, not the Pattern label, but the belief that made this outcome surprising. If no Echo: "N/A — no Echo, no prior belief contradicted."]

The "Why unexpected" field names what was expected before ship and why reality contradicted it. It is not the Echo restated and not the Pattern — it is the belief the author held before commit that the Echo overturned.

LOCK: Echo table, Pattern entry, and Why unexpected field are final. Phases 2–8 may not change them.

PHASE 1 SEAL — all fields must be explicitly populated before Phase 2 begins:
  [ ] Echo cell: exactly one sentence OR the exact string "No Echo — all post-ship outcomes were within signal bounds" (not blank, not a paraphrase of a wrong prediction)
  [ ] Nearest signal: a named artifact filename OR the exact string "none" (not blank)
  [ ] Commit relevance: exactly HIGH, MEDIUM, or LOW (or "N/A" only paired with "No Echo")
  [ ] Pattern: "> **Pattern**: [name] — [failure class description]" (not blank, not generic, not a restatement of the Echo)
  [ ] Why unexpected: "> **Why unexpected**: [named prior belief or model contradicted]" (not blank, not "unexpected" as a label, not a restatement of the Echo or Pattern — must name what the team believed before ship)
  {{#if amend}}[ ] AMEND scope marker present immediately above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status     | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| draft     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| review    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| flow      | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| trace     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| prove     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| listen    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| program   | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| topic     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| TOTAL     |            | N |                   |                    |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — all items required before Phase 3 begins:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY" (no other value, no blank)
  [ ] Every Artifact count cell: a number (0 is valid for EMPTY; blank is not)
  [ ] TOTAL row present with summed count
  {{#if amend}}[ ] OOS table present immediately after main table (even if "No artifacts excluded"){{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL:
  [ ] Every COVERED namespace from Phase 2 has exactly one row
  [ ] No Predicted cell is blank or contains only "N/A"
  [ ] No Actual cell is blank or contains only "N/A"
  [ ] Every Match cell: exactly C, P, W, or ND (no other values)
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table, state the count-based accuracy ratio:
  Correct signals: [count of C rows] / [count of C+P+W rows] = X%
  (Count-based ratio — not weighted. Both numbers required.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present with weighted formula applied
  [ ] Count-based accuracy ratio stated in N/M = X% format immediately below scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces one of two outputs.

Review the locked Phase 1 Echo.
Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [Phase 3 row / Phase 4 score — which specific finding creates the tension]
  Analysis: [what the finding suggests the Echo should be]
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of the two outputs present: either CONFLICT DETECTED block (with Source, Analysis, Resolution all present) or the exact "No conflict" declaration
  [ ] Nothing in Phase 5 modifies the Phase 1 Echo table, Pattern entry, or Why unexpected field
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence present in the exact required format (both weighted score and count ratio)
  [ ] Weighted score matches Phase 4 TOTAL row (same number, not recalculated)
  [ ] Count ratio matches Phase 4 N/M = X% statement (same values)
  [ ] Tier label (STRONG / ADEQUATE / WEAK) matches the stated weighted score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

A gap entry has two required explanatory fields that must state different things:
  - "Assumption held without evidence": the inertia belief that made this gap invisible before commit. Why the team did not gather this signal. Framed as a prior belief ("We assumed X"), not as an outcome.
  - "Would have surfaced": what this signal would have revealed. The discovery that was missed. This is the outcome; the Assumption is the belief that prevented gathering it.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [prior belief, e.g., "We assumed X was true without evidence"] | [exact skill, e.g., /listen-support] | [what the signal would have revealed — distinct from the Assumption column] | YES / NO |

The Assumption and "Would have surfaced" columns must contain different statements addressing different questions.

"Gather more data" does not satisfy the Skill column. Name an exact Signal namespace skill.
No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Use this template exactly — all three slots required:
  > **Recommendation**: Addresses [Gap: signal-type / Echo: pattern-name] by [specific practice change — what process or skill is added or modified] so that [measurable outcome — what would be observably different if this practice change succeeded].

The measurable outcome is not the practice change restated. It names the observable change in future accuracy, coverage, or decision quality that confirms the practice change worked.

PHASE 7 SEAL:
  [ ] Every W or P namespace from Phase 3 has a gap row (or "no gaps" statement)
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Assumption column: a prior belief per row — framed as a belief ("We assumed X"), not an outcome, not blank, not "unknown"
  [ ] "Would have surfaced" column: a discovery statement per row — distinct from Assumption (answers "what", not "why")
  [ ] Skill column: exact Signal skill name per row (not a namespace name, not "gather more data")
  [ ] Changed commit: exactly YES or NO per row
  [ ] Recommendation: three slots present — [Gap/Echo name] + [practice change] + [measurable outcome] (two-slot template fails this check)
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named topic/date or exactly "none"
  [ ] This score: matches Phase 4 TOTAL weighted score (same number)
  [ ] Trend: exactly ↑, ↓, or = with a label, or "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro is complete when all confirmed:
  [ ] Echo cell: matches Phase 1 Echo cell content exactly (not paraphrased, not summarized)
  [ ] Pattern cell: matches Phase 1 Pattern name exactly (same taxonomy label used in Phase 1)
  [ ] Proposed change: specific and actionable (not generic, not "gather more data")
  [ ] Change type: exactly one of: new skill, rubric amendment, threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo table + Pattern + Why unexpected — all three locked before Phase 2 begins. Why unexpected names the prior belief contradicted, not the Echo itself and not the Pattern.
- Phase 2: fixed 9-row namespace table (COVERED or EMPTY only; TOTAL row required).
- Phase 4: weighted score AND N/M=X% count ratio — both required.
- Phase 6: verdict sentence includes both score formats drawn from Phase 4.
- Phase 7: two distinct columns per gap (Assumption + Would have surfaced); recommendation three-slot template with measurable outcome required.
- Every phase seal enumerates exact required content with format strings.
- When AMEND is set: every table has a scope marker and Phase 2 has an OOS secondary table.

Phase 1 Why unexpected is a belief-correction statement, not a label. Phase 7 "so that [measurable outcome]" is a success condition, not a restatement of the practice change. Both fields require distinct content that cannot be satisfied by repeating adjacent fields.
Each phase seal is a self-containedness contract. A phase that cannot pass its own seal is incomplete — do not proceed.
```

---

## V-05 — Full-Integration-R9: C-24 + C-25 + all R7-V05 mechanisms + strengthened seals

**Axes:** All prior R7-V05 mechanisms retained, both R9 targets added, seals upgraded with format strings for new fields:
- C-24: dedicated "Why unexpected" field after Pattern in Phase 1 — belief-correction form required, not label
- C-25: three-slot recommendation template in Phase 7 — gap/echo + practice change + measurable outcome
- C-20: Assumption column in Phase 7 gap table (from R7-V05)
- C-10: per-table AMEND scope markers + OOS secondary table in Phase 2 (from R7-V05)
- C-15: N/M=X% count ratio in Phase 4 alongside weighted score (from R7-V05)
- C-16: fixed 9-row namespace coverage table in Phase 2 (from R7-V05)
- C-21/C-23: format-string seals — every seal field carries an exact format specification (from R7-V05), extended to new fields

**Hypothesis:** All six mechanisms operate in different phases or different columns within phases. Primary risk is prompt volume reducing salience of Phase 1's "Why unexpected" field, which appears relatively early and could be treated as optional context before the Phase 1 SEAL enforces it. The seal's explicit format-string check for "Why unexpected" (`> **Why unexpected**: [named prior belief — not a label, not Echo restated]`) is the enforcement mechanism. If V-05 regresses on any prior-passing criterion, regression analysis identifies which new field introduced the interference. This is the maximum ceiling test for R9.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, identify gaps. Each phase ends with a PHASE SEAL — an explicit field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

PHASE 1 — ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only — outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table, add two required entries:

1. Name the systemic pattern:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — the class of failure it belongs to, not a restatement of the Echo]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

2. State why the Echo was unexpected — the belief-correction event:
  > **Why unexpected**: [the prior model, belief, or assumption the team held before ship that this Echo contradicted — what was expected vs what was observed, stated as a named prior belief. Not the Echo restated. Not the Pattern label. Not "unexpected" as a label. If no Echo: "> **Why unexpected**: N/A — no Echo."]

The distinction:
  - Echo = what happened
  - Pattern = what failure class it belongs to
  - Why unexpected = what the author believed before ship that the Echo overturned

LOCK: Echo table, Pattern entry, and Why unexpected field are final. Phases 2–8 may not change them.

PHASE 1 SEAL — all five fields must be explicitly populated in their required format before Phase 2 begins:
  [ ] Echo cell: `{one sentence — the single post-ship observable}` OR the exact string "No Echo — all post-ship outcomes were within signal bounds" (not blank, not a paraphrase of a wrong prediction, not multiple sentences)
  [ ] Nearest signal: `{artifact filename}` OR the exact string "none" (not blank, not "N/A")
  [ ] Commit relevance: exactly one of: HIGH, MEDIUM, LOW (or the exact string "N/A" paired only with "No Echo")
  [ ] Pattern: `> **Pattern**: {name from taxonomy or "other: [name]"} — {description of failure class, not Echo restatement}` (not blank, not generic, name from taxonomy required)
  [ ] Why unexpected: `> **Why unexpected**: {prior belief or model contradicted — names what was expected before ship}` (not blank, not "unexpected" restated, not Echo sentence, not Pattern — must name the belief the team held that the Echo overturned)
  {{#if amend}}[ ] AMEND scope marker: `[AMEND: {{amend}} only — ...]` present immediately above Echo table{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status     | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| draft     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| review    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| flow      | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| trace     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| prove     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| listen    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| program   | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| topic     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| TOTAL     |            | N |                   |                    |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — all items required before Phase 3 begins:
  [ ] All 9 namespace rows present in exact order: `scout | draft | review | flow | trace | prove | listen | program | topic`
  [ ] Every Status cell: exactly one of `COVERED` or `EMPTY` (no other value, no blank)
  [ ] Every Artifact count cell: `{integer}` (0 is valid for EMPTY rows; blank is not valid)
  [ ] TOTAL row present: `{summed integer across all namespace rows}`
  {{#if amend}}[ ] OOS table present immediately after main table: either rows of excluded artifacts or the exact string "No artifacts excluded — all in scope"{{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL:
  [ ] Every COVERED namespace from Phase 2 has exactly one row: `{namespace-name} | {predicted} | {actual} | {C/P/W/ND}`
  [ ] No Predicted cell is blank or contains only "N/A"
  [ ] No Actual cell is blank or contains only "N/A"
  [ ] Every Match cell: exactly one of `C`, `P`, `W`, `ND` (no other values, no prose)
  {{#if amend}}[ ] Scope marker `[AMEND: {{amend}} only]` present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table, state the count-based accuracy ratio:
  Correct signals: [count of C rows] / [count of C+P+W rows] = X%
  (Count-based ratio — not weighted. Both numbers required.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row: `{namespace} | {C} | {P} | {W} | {ND} | {score or blank}`
  [ ] TOTAL row present with weighted formula result: `TOTAL | {sum-C} | {sum-P} | {sum-W} | {sum-ND} | {weighted-score}`
  [ ] Count-based ratio stated in exact form: `Correct signals: {N} / {M} = {X}%` immediately below scoring table
  {{#if amend}}[ ] Scope marker `[AMEND: {{amend}} only]` present above table{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces one of two outputs.

Review the locked Phase 1 Echo.
Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [Phase 3 row / Phase 4 score — which specific finding creates the tension]
  Analysis: [what the finding suggests the Echo should be]
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of two outputs present:
      - CONFLICT DETECTED block: `Source: {finding}` + `Analysis: {proposed revision}` + `Resolution: Phase 1 Echo preserved unchanged`
      - OR the exact string: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Nothing in Phase 5 modifies any Phase 1 field (Echo cell, Nearest signal, Commit relevance, Pattern, Why unexpected)
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence: `Signal accuracy for {topic}: {weighted-score}/100 — {STRONG/ADEQUATE/WEAK}. Count accuracy: {N}/{M} = {X}%.`
  [ ] Weighted score: matches Phase 4 TOTAL row exactly (same number — not recalculated here)
  [ ] Count ratio: matches Phase 4 N/M = X% statement exactly (same N, M, X values)
  [ ] Tier label: STRONG (score >=75), ADEQUATE (50–74), or WEAK (<50) — must match stated score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

A gap entry has two required explanatory fields that must state different things:
  - "Assumption held without evidence": the inertia belief that made this gap invisible before commit. Why the team did not gather this signal. Framed as a prior belief ("We assumed X"), not as an outcome.
  - "Would have surfaced": what this signal would have revealed. The discovery that was missed. This is the outcome; the Assumption is the belief that prevented gathering it.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X", framed as a belief not an outcome] | [exact skill, e.g., /listen-support] | [what the signal would have revealed — distinct from the Assumption column] | YES / NO |

Validation: the Assumption and "Would have surfaced" columns must address different questions. Assumption = why the gap existed (belief). Would have surfaced = what was missed (discovery). If both columns say the same thing, one is wrong.

"Gather more data" does not satisfy the Skill column. Name an exact Signal namespace skill (e.g., /scout-feasibility, /flow-resilience, /listen-adoption).
No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Use this template exactly — all three slots are required:
  > **Recommendation**: Addresses [Gap: {signal-type} / Echo: {pattern-name}] by [{specific practice change — what process or skill is added, modified, or made mandatory}] so that [{measurable outcome — the observable change in future accuracy, coverage, or decision quality that confirms the practice change succeeded}].

Slot definitions:
  - [Gap: ... / Echo: ...] = the specific gap or Echo this recommendation addresses (named, not generic)
  - [by {practice change}] = the concrete process, skill, or threshold change proposed
  - [so that {measurable outcome}] = what would be observably different in a future retro if this practice change was adopted. Not the practice change restated. An observable test.

PHASE 7 SEAL:
  [ ] Every W or P namespace from Phase 3 has a gap row (or the exact string "No gaps — signal coverage was sufficient for this commit decision.")
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Assumption column: `{prior belief — "We assumed X" or equivalent}` per row (not an outcome, not blank, not "unknown", not "we did not gather this signal")
  [ ] "Would have surfaced" column: `{discovery statement — what was missed}` per row, distinct from Assumption column content (different answer to a different question)
  [ ] Skill column: `/{exact-skill-name}` per row (must be a named Signal skill — not a namespace, not "gather more data", not generic)
  [ ] Changed commit: exactly `YES` or `NO` per row
  [ ] Recommendation: `> **Recommendation**: Addresses [Gap/Echo] by [practice change] so that [measurable outcome]` — all three slots populated with distinct, non-generic content
  {{#if amend}}[ ] AMEND scope marker `[AMEND: {{amend}} only — ...]` present above gap table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: `{topic} / {YYYY-MM-DD}` OR the exact string "none"
  [ ] This score: `{integer}` matching Phase 4 TOTAL weighted score exactly
  [ ] Trend: exactly one of `↑ improving`, `↓ degrading`, `= stable`, OR the exact string "First retro for this topic — this score establishes the calibration baseline."
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro is complete when all confirmed:
  [ ] Echo cell: `{exact Echo content from Phase 1}` — character-level match, not paraphrased, not summarized
  [ ] Pattern cell: `{exact Pattern name from Phase 1}` — same taxonomy label as used in Phase 1, not a synonym
  [ ] Proposed change: `{specific actionable change}` — not generic, not "gather more data", names a specific skill or threshold
  [ ] Change type: exactly one of: `new skill`, `rubric amendment`, `threshold adjustment`
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo table + Pattern + Why unexpected — all three locked before Phase 2. The three fields are distinct: Echo = what happened, Pattern = failure class, Why unexpected = belief contradicted. Each answers a different question.
- Phase 2: fixed 9-row namespace table (COVERED or EMPTY only; TOTAL row required). AMEND excludes via OOS secondary table, not by omitting rows.
- Phase 4: weighted score AND N/M=X% count ratio — both required and both drawn into Phase 6 verdict.
- Phase 6: verdict sentence carries both score formats with exact matching back to Phase 4.
- Phase 7: two distinct columns per gap (Assumption = why; Would have surfaced = what); recommendation carries three slots (gap/echo, practice change, measurable outcome — not two).
- Every phase seal carries format strings per field — not field labels, but exact value specifications.
- When AMEND is set: every table has a `[AMEND: ...]` scope marker and Phase 2 has an OOS secondary table.

The new R9 fields:
- "Why unexpected" in Phase 1 is a belief-correction. It names the prior model the Echo overturned. It is not the Echo restated and not the Pattern label. A value of "we didn't expect this" is not a belief-correction.
- "so that [measurable outcome]" in Phase 7 names the observable test that would confirm the practice change worked. It is not a restatement of the practice change. A value of "better coverage next time" without a named observable is not measurable.

Each phase seal is a self-containedness contract. A phase that cannot pass its own seal is incomplete — do not proceed.
```

---

## Summary Table

| ID | Primary Axes | C-24 Mechanism | C-25 Mechanism | C-20 | C-10 | C-15 | C-16 | C-21/C-23 | Hypothesis |
|----|-------------|----------------|----------------|------|------|------|------|-----------|------------|
| V-01 | C-24 (single axis) | `> **Why unexpected**: [prior belief]` labeled prose field after Pattern in Phase 1; Phase 1 SEAL checks belief-form not label | None (two-slot template unchanged) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Labeled post-Pattern field forces belief-correction statement; SEAL prevents label-only fill |
| V-02 | C-25 (single axis) | None (no Why unexpected field) | Three-slot template: `Addresses [gap/echo] by [change] so that [measurable outcome]`; Phase 7 SEAL checks all three slots | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | "so that" clause makes measurable outcome structural in template — SEAL enforces three-slot fill |
| V-03 | C-24 output format variant | Two-row Echo table — `Echo` row + `Why unexpected` row as structural peers; SEAL checks both rows present | None (two-slot template unchanged) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Yes (R7-V05) | Table row = same weight as Echo finding; tests whether row-structure outperforms post-table prose for C-24 PASS |
| V-04 | C-24 + C-25 (combined) | V-01 mechanism: `> **Why unexpected**:` post-Pattern field with SEAL belief-check | V-02 mechanism: three-slot template with SEAL three-slot check | Yes | Yes | Yes | Yes | Yes | Zero-interference test: C-24 modifies only Phase 1, C-25 modifies only Phase 7 — no structural overlap expected |
| V-05 | C-24 + C-25 + full R7-V05 integration | V-01 mechanism with format-string SEAL spec: `> **Why unexpected**: {prior belief — not a label, not Echo restated}` | Three-slot template with format-string SEAL spec: `> **Recommendation**: Addresses [...] by [...] so that [observable test]` | Yes (strengthened) | Yes (strengthened) | Yes (strengthened) | Yes (strengthened) | Yes (strengthened) | Maximum ceiling test — all six mechanisms active; regression on any prior-passing criterion identifies interference |
