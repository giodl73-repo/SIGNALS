# topic-retro — Variations R11
**Date:** 2026-03-17
**Rubric:** v9 (C-01 through C-29; total available = 132)
**R10 top scorer:** V-05 (source of C-28, C-29 criteria) — recommendation slot + Phase 8 score copy.
**New criteria to target:** C-28 (recommendation-slot-completeness-guard) and C-29 (phase-8-score-copy-guard).

**Base used:** R7-V-05 evolved through v6–v8 rubric additions (C-22 through C-27 incorporated into all variations):
- C-22: OOS secondary table (already in R7-V-05)
- C-23: Seal format strings per field (tightened in all variations)
- C-24: Echo why-unexpected explained (Phase 1 "Why unexpected" field added to all)
- C-25: Recommendation outcome measurable (three-slot template in all)
- C-26: Gap inertia column isolation (Column A/B structural separation in all)
- C-27: Self-containment extended to all 9 phases (already in R7-V-05; confirmed in all)

**Single-axis:** V-01 (C-28), V-02 (C-29), V-03 (phrasing register).
**Combined:** V-04 (C-28 + C-29), V-05 (C-28 + C-29 + C-23 format-contract tightening across all 9 seals).

---

## Summary Table

| ID | Primary Axis | C-28 Mechanism | C-29 Mechanism | C-23/Seals | Hypothesis |
|----|-------------|----------------|----------------|------------|------------|
| V-01 | C-28 (single) | `[slot:X]` named tokens + SEAL placeholder-string check | None (Phase 8 seal checks score match only) | R7-V-05 baseline | Distinctive token names make the placeholder check mechanical — if `[slot:` appears in output, fill failed |
| V-02 | C-29 (single) | None (two-slot template, no placeholder check) | "COPY from Phase 6" + "do not recompute" in Phase 8 body + SEAL copy-citation check | R7-V-05 baseline | Explicit copy instruction with "do not recompute" makes score-transfer auditable; SEAL verifies citation |
| V-03 | Phrasing register (single) | Imperative prohibition: "Write the recommendation. Replace all brackets. If a bracket string remains, the phase is not complete." | Imperative prohibition: "Do not derive this number. Copy it from Phase 6." | Imperative mode throughout | Tests whether command-register phrasing without additional structural tokens is sufficient for both criteria |
| V-04 | C-28 + C-29 (combined) | `[slot:X]` tokens + SEAL placeholder check (from V-01) | "COPY from Phase 6. Do not recompute." + SEAL copy-citation (from V-02) | R7-V-05 baseline | Zero-interference test: C-28 lives in Phase 7; C-29 lives in Phase 8; independent phases |
| V-05 | Full integration | `[slot:X]` tokens + SEAL placeholder check | "COPY from Phase 6. Do not recompute." + SEAL copy-citation | All 9 seals receive explicit format-contract strings; Phase 6 seal names the copy-source citation format | Maximum ceiling: both mechanisms plus tightened seal format contracts across all phases |

---

## V-01 — Slot-Guard: C-28 via Named Token Placeholder Check

**Axis:** C-28 mechanism — the recommendation template uses three explicitly named bracket tokens (`[slot:gap-or-echo]`, `[slot:practice-change]`, `[slot:measurable-outcome]`). The Phase 7 SEAL carries an explicit placeholder-string check: if any `[slot:` string survives to the final output, the phase is not complete.

**Hypothesis:** Generic bracket placeholders like `[name]` can survive undetected because they resemble optional labels. Naming the tokens `[slot:X]` makes them distinctive and testable: the SEAL check is a string-level assertion ("output must not contain `[slot:`") that can be confirmed by inspection. C-17 provides the template; C-28 requires the slots to be verifiably filled — this check is the enforcement mechanism. All phases outside Phase 7 are unchanged from R7-V-05 baseline.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

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

Immediately after the table, state the pattern and why the finding was unexpected:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern entry, and Why-unexpected field are final. Phases 2–9 may not change them.

PHASE 1 SEAL — all fields required before Phase 2 begins:
  [ ] Echo cell: exactly one sentence OR the exact string "No Echo — all post-ship outcomes were within signal bounds" — format: {one sentence describing the post-ship finding}
  [ ] Nearest signal: a named artifact filename OR the exact string "none"
  [ ] Commit relevance: exactly HIGH, MEDIUM, or LOW (or "N/A" only when paired with "No Echo")
  [ ] Pattern: "> **Pattern**: {name} — {description naming the failure class, not the Echo instance}" — not blank, not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} — identifies what was expected, not just that it was unexpected"
  {{#if amend}}[ ] AMEND scope marker present immediately above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — all items required before Phase 3 begins:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY" — no other value, no blank
  [ ] Every Artifact count cell: a number — format: {integer} (0 is valid for EMPTY; blank is not)
  [ ] TOTAL row present with summed count — format: {integer}
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
  [ ] No Predicted cell is blank or contains only "N/A" — format: {one phrase or sentence describing what signals claimed}
  [ ] No Actual cell is blank or contains only "N/A" — format: {one phrase or sentence describing what was observed}
  [ ] Every Match cell: exactly C, P, W, or ND — no other values
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {count of C rows} / {count of C+P+W rows} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present with weighted formula applied — format: {number}/100
  [ ] Count-based accuracy ratio stated in exact N/M = X% format immediately below scoring table
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
  [ ] One of two outputs present: either CONFLICT DETECTED block (with Source, Analysis, Resolution all present) OR exactly "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Nothing in Phase 5 modifies the Phase 1 Echo table or Pattern entry
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
State the overall accuracy judgment:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence present in exact format — format: "Signal accuracy for {topic}: {score}/100 — {STRONG/ADEQUATE/WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score matches Phase 4 TOTAL row (same number, not recalculated)
  [ ] Count ratio matches Phase 4 N/M = X% statement (same values)
  [ ] Tier label (STRONG / ADEQUATE / WEAK) matches the stated weighted score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

The gap table has two structurally isolated columns that must contain different statements:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible before commit. Why the team did not gather this signal. Framed as a prior belief ("We assumed X"), not as an outcome. Explains WHY the gap existed.
  - Column B — "Would have surfaced": what this signal would have revealed. The discovery missed. Explains WHAT was missed.
  These columns address different questions. If they share content, one column is wrong.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" — NOT an outcome] | [exact Signal skill] | [discovery statement — distinct from column A] | YES / NO |

Validation: Column A and Column B must state different things. A row where both columns say the same thing is incomplete — do not proceed.

"Gather more data" does not satisfy the Skill column. Name an exact Signal namespace skill.
No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` with specific content. The final output must not contain any `[slot:` strings.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern addressed] by [slot:practice-change — name the specific practice change, not generic] so that [slot:measurable-outcome — what would be observably different if this practice change succeeded].

PHASE 7 SEAL:
  [ ] Every W or P namespace from Phase 3 has a gap row (or explicit "no gaps" statement)
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Column A per row: a prior belief framed as "We assumed X" — not an outcome, not blank, not "unknown"
  [ ] Column B per row: a discovery statement distinct from Column A (different content)
  [ ] Columns A and B do not share content — same statement in both = incomplete row
  [ ] Skill column: exact Signal skill name per row (not a namespace name, not "gather more data")
  [ ] Changed commit: exactly YES or NO per row
  [ ] Recommendation slot check: the output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" — all three slots replaced with specific content
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named as "{topic} / {YYYY-MM-DD}" or exactly the string "none"
  [ ] This score: matches Phase 4 TOTAL weighted score — format: {number}/100
  [ ] Trend: exactly ↑, ↓, or = with a label OR "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro is complete when all confirmed:
  [ ] Echo cell: matches Phase 1 Echo cell content exactly — format: {copied verbatim}
  [ ] Pattern cell: matches Phase 1 Pattern name exactly — format: {same taxonomy label used in Phase 1}
  [ ] Proposed change: specific and actionable — not "gather more signals"
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected fields required.
- Phase 2: Fixed 9-row namespace table. COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio — both required.
- Phase 6: Verdict sentence draws both score formats from Phase 4. No recalculation.
- Phase 7: Two structurally isolated gap columns (Column A = belief, Column B = outcome). Three-slot recommendation; SEAL confirms no [slot:X] strings survive.
- Phase 8: Score copied from Phase 4 TOTAL, not derived.
- All 9 phases sealed with format-string specifications.

Each phase seal is a self-containedness contract. A phase that cannot pass its own seal is incomplete — do not proceed.
```

---

## V-02 — Copy-Guard: C-29 via Explicit Score Transfer Instruction in Phase 8

**Axis:** C-29 mechanism — Phase 8 body carries an explicit "COPY from Phase 6. Do not recompute." instruction before the calibration table. The score in the "This score" cell is sourced by direct citation from Phase 6 verdict sentence. The Phase 8 SEAL includes a copy-citation check: the scorer confirms the Phase 8 score matches the Phase 6 sentence by inspection, not by recomputing from Phase 4.

**Hypothesis:** R7-V-05 Phase 8 SEAL checks "This score: matches Phase 4 TOTAL weighted score." This is a match check, not a copy guard — a silently recomputed score that happens to match passes this check trivially. C-29 requires an explicit "do not recompute" instruction and a copy mechanism. Moving the citation source from Phase 4 to Phase 6 (the verdict sentence) makes the copy transfer auditable: the scorer checks two sentences, not a number against a table cell. All phases outside Phase 8 unchanged from R7-V-05 baseline (recommendation template keeps two slots — C-25 is not targeted here).

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — not a restatement of the Echo]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final.

PHASE 1 SEAL:
  [ ] Echo cell: exactly one sentence OR "No Echo — all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: named artifact filename OR "none"
  [ ] Commit relevance: exactly HIGH, MEDIUM, or LOW (or "N/A" with "No Echo")
  [ ] Pattern: "> **Pattern**: {name} — {failure class description}" — not blank, not a restatement
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}" — not a label only
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL:
  [ ] All 9 namespace rows present in order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY"
  [ ] Every Artifact count cell: a number (0 valid for EMPTY)
  [ ] TOTAL row present with summed count
  {{#if amend}}[ ] OOS table present immediately after main table{{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank] | [required — non-blank] | [C / P / W / ND] |

C = Correct, P = Partial, W = Wrong, ND = No post-ship data.

PHASE 3 SEAL:
  [ ] Every COVERED namespace has exactly one row
  [ ] No Predicted cell blank or "N/A"
  [ ] No Actual cell blank or "N/A"
  [ ] Every Match cell: exactly C, P, W, or ND
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based ratio, not weighted.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row with weighted formula applied
  [ ] Count-based ratio in N/M = X% format immediately below table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Does Phase 3 or Phase 4 suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [which Phase 3 row or Phase 4 score creates the tension]
  Analysis: [what the finding suggests the Echo should be]
  Resolution: Phase 1 Echo preserved unchanged.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of the two required outputs present, complete
  [ ] Phase 1 Echo and Pattern entry not modified
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw weighted score from Phase 4 TOTAL. Draw count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence in exact required format
  [ ] Weighted score matches Phase 4 TOTAL (not recalculated)
  [ ] Count ratio matches Phase 4 statement
  [ ] Tier label matches stated weighted score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace where absence is material:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Two structurally isolated columns required per gap row:
  - Column A — "Assumption held without evidence": the inertia belief (WHY the gap existed). Framed as "We assumed X."
  - Column B — "Would have surfaced": the discovery missed (WHAT was missed). Different from Column A.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X"] | [exact Signal skill] | [discovery — distinct from A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

  > **Recommendation**: Addresses [gap type or Echo pattern] by [specific practice change] so that [measurable outcome — what would be observably different if this change succeeded].

PHASE 7 SEAL:
  [ ] Every W or P namespace has a gap row (or "no gaps")
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Column A per row: prior belief as "We assumed X" — not an outcome, not blank
  [ ] Column B per row: discovery statement distinct from Column A
  [ ] Skill column: exact Signal skill per row
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation: present with gap/echo, practice change, and measurable outcome filled
  {{#if amend}}[ ] AMEND scope marker present{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source; Phase 8 transfers it verbatim.

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | [copied from Phase 6 verdict] | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: "{topic} / {YYYY-MM-DD}" or exactly "none"
  [ ] This score: copied from Phase 6 verdict sentence — confirm the number in this cell matches the number in the Phase 6 verdict sentence exactly (do not recompute from Phase 4)
  [ ] Trend: exactly ↑, ↓, or = with a label OR "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL:
  [ ] Echo cell: matches Phase 1 Echo cell content exactly (not paraphrased)
  [ ] Pattern cell: matches Phase 1 Pattern name exactly (same taxonomy label)
  [ ] Proposed change: specific and actionable
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo locked. Pattern and Why-unexpected required.
- Phase 2: Fixed 9-row table. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% ratio — both required.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation.
- Phase 7: Two isolated gap columns. Three-slot recommendation.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Explicit "do not recompute." SEAL verifies by citation, not recomputation.
- All 9 phases sealed.

Each phase seal is a self-containedness contract. Do not proceed past a phase until its seal passes.
```

---

## V-03 — Phrasing Register: Imperative Prohibition Mode for C-28 and C-29

**Axis:** Phrasing register — all structural enforcement instructions are rewritten in direct second-person prohibitive form ("Do not. Replace. Confirm.") rather than descriptive/conditional form. C-28 is expressed as a prohibition ("Do not leave any bracket string in the recommendation") and C-29 as a prohibition ("Do not derive this score. Copy it."). No new structural tokens or table columns added.

**Hypothesis:** Both C-28 and C-29 describe failure modes caused by silent omission — the model completes a phase without noticing an enforcement gap. A prohibition directly names the failure mode it prevents. Testing whether imperative prohibition phrasing ("Do not X") is sufficient to achieve PASS on these criteria without additional structural scaffolding (no `[slot:]` tokens, no "copy-citation" check). If this achieves PASS, the structural mechanisms in V-01/V-02 are unnecessary overhead. If it scores PARTIAL, the structural mechanisms are the required enforcement layer.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Work through each phase in order. Each phase ends with a SEAL. Do not proceed past a phase until its SEAL passes. Do not skip fields. Do not defer outputs to later phases.

{{#if amend}}AMEND SCOPE: {{amend}} only. Every table carries this constraint as a scope marker above it.{{/if}}

---

PHASE 1 — ECHO

Run this phase before reading any signal artifacts.

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Find the one post-ship observable that was not predicted by any gathered signal, not named as a risk, and only visible after ship. Select the one with highest commit-decision impact. If none: use "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [one sentence or the exact no-Echo string] | [filename or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Name the pattern. Do not restate the Echo sentence — name the class of failure it belongs to.
  > **Pattern**: [name] — [failure class description]

Explain why it was unexpected. Do not write "unexpected" as a label. Name the prior belief that was contradicted.
  > **Why unexpected**: [prior belief or model that this finding contradicted]

Lock this phase. Do not alter it in Phases 2–9.

PHASE 1 SEAL:
  [ ] Echo: one sentence or exact no-Echo string — not blank, not a wrong-prediction restatement
  [ ] Nearest signal: artifact filename or "none"
  [ ] Commit relevance: HIGH, MEDIUM, or LOW (or "N/A")
  [ ] Pattern: named failure class — not blank, not a restatement of Echo
  [ ] Why unexpected: prior belief named — not just the label "unexpected"
  {{#if amend}}[ ] Scope marker above table{{/if}}
PHASE 1 COMPLETE when all confirmed.

---

PHASE 2 — SIGNAL INVENTORY

{{#if amend}}[AMEND: {{amend}} only — excluded artifacts go to the OOS table below]{{/if}}

Produce exactly 9 rows — one per namespace. Do not omit any namespace. Do not combine rows.

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside scope] |
If none excluded: write "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL:
  [ ] All 9 namespace rows present in order
  [ ] Status: COVERED or EMPTY — nothing else
  [ ] Artifact count: a number in every cell (0 valid; blank invalid)
  [ ] TOTAL row present
  {{#if amend}}[ ] OOS table present{{/if}}
PHASE 2 COMPLETE when all confirmed.

---

PHASE 3 — PREDICTED VS ACTUAL

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

For each COVERED namespace: write what signals predicted and what actually happened. Do not leave either cell blank. Do not write "N/A."

| Namespace | Predicted | Actual | Match: C / P / W / ND |
|-----------|-----------|--------|----------------------|
| [name] | [what signals claimed] | [what was observed] | [C / P / W / ND] |

PHASE 3 SEAL:
  [ ] One row per COVERED namespace
  [ ] No blank Predicted cells
  [ ] No blank Actual cells
  [ ] Match: C, P, W, or ND only
  {{#if amend}}[ ] Scope marker above table{{/if}}
PHASE 3 COMPLETE when all confirmed.

---

PHASE 4 — NAMESPACE ACCURACY

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

Exclude ND from the denominator. Write "0 scored signals" if denominator is 0.

State the count ratio immediately after the table. Do not omit it.
  Correct: {C} / {C+P+W} = X%

PHASE 4 SEAL:
  [ ] One row per Phase 3 namespace
  [ ] TOTAL row with weighted formula
  [ ] Count ratio in N/M = X% format below table
  {{#if amend}}[ ] Scope marker{{/if}}
PHASE 4 COMPLETE when all confirmed.

---

PHASE 5 — CONFLICT AUDIT

Does Phase 3 or Phase 4 suggest the Phase 1 Echo should name a different finding? Answer this question. Do not skip it.

If yes:
  CONFLICT DETECTED
  Source: [which finding creates the tension]
  Analysis: [what the Echo should become under this analysis]
  Resolution: Phase 1 Echo preserved unchanged.

If no:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

Do not modify Phase 1 Echo in this phase.

PHASE 5 SEAL:
  [ ] One of the two required outputs present
  [ ] Phase 1 not modified
PHASE 5 COMPLETE when all confirmed.

---

PHASE 6 — ACCURACY VERDICT

Write this sentence:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG / ADEQUATE / WEAK]. Count accuracy: [N/M = X%]."

Take the weighted score from Phase 4 TOTAL. Take the count ratio from Phase 4 count statement. Do not recalculate either number.

PHASE 6 SEAL:
  [ ] Verdict sentence present in required format
  [ ] Weighted score taken from Phase 4 TOTAL — not recalculated
  [ ] Count ratio taken from Phase 4 statement — not recalculated
  [ ] Tier label matches the stated score
PHASE 6 COMPLETE when all confirmed.

---

PHASE 7 — GAP ANALYSIS

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

For each W or P namespace from Phase 3, and each EMPTY namespace where absence affected the commit:

Gap table requires two separate columns with different content:
  - Assumption: why the gap existed — the prior belief held without evidence ("We assumed X")
  - Would have surfaced: what was missed — the discovery. Different statement from the Assumption.

Do not merge these into one cell. Do not write the same content in both.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? |
|--------------------------|-----------|----------------------------------|-------------|---------------------|----------------|
| [type] | [ns] | [We assumed X — prior belief] | [exact Signal skill] | [discovery — not the assumption] | YES / NO |

Write the recommendation. Replace all three bracketed fields with specific content. Do not leave any bracket text in the output.

  > **Recommendation**: Addresses [name the gap or Echo pattern] by [name the practice change] so that [name the measurable outcome — what changes observably if this succeeds].

Do not write "Addresses [gap type]" — replace [gap type] with the actual gap or pattern name.
Do not write "by [practice change]" — replace [practice change] with the actual change.
Do not write "so that [measurable outcome]" — replace [measurable outcome] with the actual observable difference.

PHASE 7 SEAL:
  [ ] W and P namespaces have gap rows (or "no gaps")
  [ ] Material EMPTY namespaces have gap rows
  [ ] Assumption column: prior belief per row, not an outcome
  [ ] Would have surfaced: distinct from Assumption per row
  [ ] Skill: exact Signal skill per row
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation: all three fields replaced — no bracket text remains in the output
  {{#if amend}}[ ] Scope marker{{/if}}
PHASE 7 COMPLETE when all confirmed.

---

PHASE 8 — CALIBRATION TREND

Do not derive the score for this phase. Copy it from the Phase 6 verdict sentence. The number in "This score" must be the number written in Phase 6 — not recalculated, not estimated.

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | [Phase 6 score — copied] | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named topic/date or "none"
  [ ] This score: is the number from the Phase 6 verdict sentence — confirm by reading Phase 6, not by computing
  [ ] Trend: ↑, ↓, or = with label, or "first retro"
PHASE 8 COMPLETE when all confirmed.

---

PHASE 9 — ECHO → SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Phase 1 Echo — do not paraphrase] | [exact Phase 1 Pattern name] | [specific change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL:
  [ ] Echo: exact copy of Phase 1 Echo cell
  [ ] Pattern: exact Phase 1 taxonomy label
  [ ] Proposed change: specific, not "gather more signals"
  [ ] Change type: one of the three options
RETRO COMPLETE when all confirmed.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
Do not proceed past a phase until its SEAL passes.
Do not modify locked phases.
Do not leave bracket text in any output field.
Do not recompute the Phase 8 score — copy it from Phase 6.
```

---

## V-04 — Combined: C-28 Slot Guard + C-29 Copy Guard

**Axes:** C-28 and C-29 combined — V-01 `[slot:X]` token mechanism in Phase 7 plus V-02 "COPY from Phase 6. Do not recompute." instruction in Phase 8. Both mechanisms are additive with no shared phase. Zero-interference test.

**Hypothesis:** C-28 lives entirely in Phase 7 (recommendation SEAL) and C-29 lives entirely in Phase 8 (score transfer). The two mechanisms modify independent phases and independent structural elements, so there is no interference risk. V-04 is the minimal combined variation: it applies exactly V-01's Phase 7 change and V-02's Phase 8 change, with no other modifications. If V-04 scores the same as V-05 on C-28 and C-29, the tightened seals in V-05 are not load-bearing for these two criteria.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode — not a restatement of the Echo]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final.

PHASE 1 SEAL:
  [ ] Echo cell: exactly one sentence OR "No Echo — all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: named artifact filename OR "none"
  [ ] Commit relevance: exactly HIGH, MEDIUM, or LOW (or "N/A" with "No Echo")
  [ ] Pattern: "> **Pattern**: {name} — {failure class description}" — not blank, not a restatement
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}" — not a label only
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL:
  [ ] All 9 namespace rows in order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY"
  [ ] Every Artifact count cell: a number (0 valid for EMPTY)
  [ ] TOTAL row present with summed count
  {{#if amend}}[ ] OOS table present immediately after main table{{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank] | [required — non-blank] | [C / P / W / ND] |

C = Correct, P = Partial, W = Wrong, ND = No post-ship data.

PHASE 3 SEAL:
  [ ] Every COVERED namespace has exactly one row
  [ ] No Predicted cell blank or "N/A"
  [ ] No Actual cell blank or "N/A"
  [ ] Every Match cell: exactly C, P, W, or ND
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table:
  Correct signals: {C count} / {C+P+W count} = X%

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row with weighted formula applied
  [ ] Count-based ratio in N/M = X% format below table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Does Phase 3 or Phase 4 suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [which finding creates the tension]
  Analysis: [what the Echo should become]
  Resolution: Phase 1 Echo preserved unchanged.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of the two required outputs present, complete
  [ ] Phase 1 Echo and Pattern not modified
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw weighted score from Phase 4 TOTAL. Draw count ratio from Phase 4 count statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence in exact required format
  [ ] Weighted score matches Phase 4 TOTAL (not recalculated)
  [ ] Count ratio matches Phase 4 statement
  [ ] Tier label matches stated score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace where absence is material:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

Two structurally isolated columns per gap row:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible (WHY). Framed as "We assumed X."
  - Column B — "Would have surfaced": the discovery missed (WHAT). Different statement from Column A.
  These columns must not share content.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X"] | [exact Signal skill] | [discovery — distinct from A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` with specific content. The final output must not contain any `[slot:` strings.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern] by [slot:practice-change — name the specific practice change] so that [slot:measurable-outcome — what would be observably different if this change succeeded].

PHASE 7 SEAL:
  [ ] Every W or P namespace has a gap row (or "no gaps")
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Column A per row: prior belief as "We assumed X" — not an outcome, not blank
  [ ] Column B per row: discovery statement distinct from Column A
  [ ] Skill: exact Signal skill per row
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation slot check: output does not contain "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" as literal strings — all three slots replaced with specific content
  {{#if amend}}[ ] AMEND scope marker present{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence. Do not recompute or derive it. The "This score" cell must contain the number written in the Phase 6 verdict sentence — transferred verbatim.

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | [copied from Phase 6 verdict sentence] | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: "{topic} / {YYYY-MM-DD}" or exactly "none"
  [ ] This score: confirm it matches the number in the Phase 6 verdict sentence exactly — do not recompute from Phase 4
  [ ] Trend: ↑, ↓, or = with label, or "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL:
  [ ] Echo cell: matches Phase 1 Echo cell exactly (not paraphrased)
  [ ] Pattern cell: matches Phase 1 Pattern name exactly (same taxonomy label)
  [ ] Proposed change: specific and actionable
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo locked. Pattern and Why-unexpected required.
- Phase 2: Fixed 9-row table. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% ratio — both required.
- Phase 6: Verdict draws both formats from Phase 4. No recalculation.
- Phase 7: Two isolated gap columns. Three-slot `[slot:X]` recommendation; SEAL confirms no [slot:X] strings survive.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Explicit "do not recompute." SEAL verifies by Phase 6 citation.
- All 9 phases sealed.

Each phase seal is a self-containedness contract. Do not proceed past a phase until its seal passes.
```

---

## V-05 — Full Integration: C-28 + C-29 + C-23 Format-Contract Tightening Across All 9 Seals

**Axes:** All of V-04 (C-28 slot-token check + C-29 copy guard), plus C-23 tightening: every seal field across all 9 phases receives an explicit format string specifying the required value form — not just a field name. Additionally, Phase 6 seal explicitly names the copy-source citation format to prevent score-path ambiguity, and Phase 9 seal names "copied verbatim" as the exact mechanism for the Echo and Pattern cells.

**Hypothesis:** V-04 passes C-28 and C-29 in isolation. V-05 tests whether stronger format-contract coverage across all 9 seals (C-23) produces additional gains on criteria that scored PARTIAL in V-04 — particularly on fields where the format string was present but not maximally explicit. The primary risk is prompt volume: the added format strings increase total length. If V-05 regresses on any prior-passing criterion relative to V-04, the regression identifies which seal additions interfered with earlier phase execution.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode — not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2–9 may not change them.

PHASE 1 SEAL — format contract (every field must match its format before Phase 2 begins):
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo — all post-ship outcomes were within signal bounds" — not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" — not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A — no other values; "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} — {description of failure class, not the Echo instance}" — field not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model that the finding contradicted} — must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic — missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row — no other value, no blank
  [ ] Artifact count: {integer} per row — format: a non-negative integer; blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "—" — not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table with format per row: "{namespace} | {filename} | {reason}" — even if "No artifacts excluded — all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL — format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 — no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} — not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} — not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND — no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL — format contract:
  [ ] Row count: one row per Phase 3 namespace — no omissions
  [ ] C, P, W, ND columns: {integer} per cell — blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied — format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" — both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score — specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL — format contract:
  [ ] Output: exactly one of — CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none — Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL — format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 — {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row — same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement — same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 — must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B — "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" — NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement — distinct from Column A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings — their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern addressed] by [slot:practice-change — name the specific practice change, not generic] so that [slot:measurable-outcome — state what would be observably different if this practice change succeeded].

PHASE 7 SEAL — format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement — no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent — NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} — different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A ≠ Column B: both columns must state different things per row — same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} — an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row — no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" — all three tokens replaced with specific content
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source for the score in this phase — transfer the number verbatim.

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "—"] | [copied from Phase 6 verdict sentence — do not recompute] | [delta or "—"] | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" — not blank, not "N/A"
  [ ] This score: {number}/100 — COPY-VERIFIED: confirm this number matches the score in the Phase 6 verdict sentence by reading Phase 6 directly (do not recompute from Phase 4 TOTAL; the copy source is Phase 6 verdict, not Phase 4)
  [ ] Delta: {+N or -N or 0} OR "—" when no prior retro
  [ ] Trend: one of exactly: ↑ improving | ↓ degrading | = stable OR the "first retro" statement
All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label, not a synonym] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} — must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} — must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} — not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio — both required.
- Phase 6: Verdict sentence draws both formats from Phase 4. No recalculation.
- Phase 7: Two structurally isolated gap columns (Column A = belief, Column B = outcome); must not share content. Three-slot `[slot:X]` recommendation; SEAL confirms no `[slot:` strings survive.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Explicit "do not recompute." SEAL verifies by Phase 6 citation, not Phase 4 recomputation.
- All 9 seals use explicit format-contract strings per field (not just field names).
- AMEND: every table has a scope marker; Phase 2 has OOS secondary table.

Each phase seal is a format contract, not a checklist. Verify each item against its stated format before proceeding.
```
