# topic-retro — Variations R18
**Date:** 2026-03-17
**Rubric:** v16 (C-01 through C-43; total available = 160)
**R17 top scorer:** V-05 -- discovered C-42 and C-43 as excellence patterns. Source criteria for this round.
**New criteria to target:** C-42 (bidirectional-manifest-citation) and C-43 (pre-execution-contract-as-manifest-navigation-index).

**Base used:** R17-V-05 -- all prior integrations carried forward:
- C-22: OOS secondary table
- C-23: Seal format-contract strings per field (all 9 phases)
- C-24: Echo why-unexpected explained
- C-25: Three-slot recommendation template
- C-26: Gap inertia columns A/B structurally isolated
- C-27: SEAL coverage extended to all phases
- C-28: `[slot:X]` token + SEAL placeholder check
- C-29: Phase 8 "do not recompute" + SEAL copy-citation check
- C-30: Three-field SEAL (This score / COPY-VERIFIED / COPY-SOURCE)
- C-31: `## PRE-EXECUTION CONTRACT` two-column table positioned before Phase 1
- C-32: Phase 8 SEAL each field has independent CHECK:/HOW: block with self-contained source
- C-33: PRE-EXECUTION CONTRACT three-column table with "Verified in" enforcement pointer
- C-36: Three-pass architectural isolation as structural property (named phase gates with entry/exit criteria)
- C-37: Accuracy reconciliation cross-check (forward count + backward count must agree)
- C-38: Backward recovery table as named structural artifact
- C-39: Signal window and Mode declared as named fields in PRE-EXECUTION CONTRACT
- C-40: AUDIT MANIFEST as primary table; all downstream sections derived as views; derivation stated
- C-41: Named-criteria phase gate (exit gate asserts aspiration criteria by exact structural artifact name)

**C-42 gap analysis:** R17-V-05 introduced the AUDIT MANIFEST (C-40) and requires downstream sections to carry `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` headers (backward citation: downstream -> manifest). C-42's additional requirement is the forward citation direction: the AUDIT MANIFEST table itself must carry a `Derived Views` column naming which downstream table(s) each row feeds. R17-V-05 has backward-only citations; an assessor at a downstream section can find the manifest, but an assessor starting at the manifest cannot navigate forward to the downstream tables without reading phase text. Adding the `Derived Views` column makes the manifest a complete navigation surface in both directions.

**C-43 gap analysis:** R17-V-05's PRE-EXECUTION CONTRACT satisfies C-33 (three-column with "Verified in") and C-39 (Signal window + Mode as named rows). C-43 requires each structural commitment row in the contract to also carry a `Manifest column` field naming the exact AUDIT MANIFEST column that will evidence fulfillment. This is not the same as "Verified in" (which names a phase SEAL item). "Manifest column" names the AUDIT MANIFEST column -- a structural data pointer. A contract row that says `Verified in: Phase 4 SEAL item 5` satisfies C-33/C-39 but fails C-43. C-43 pass requires `Manifest column: Verdict` (or `Namespace`, etc.) -- an exact column name from the manifest table header.

**Single-axis:** V-01 (C-42), V-02 (C-43), V-03 (phrasing register).
**Combined:** V-04 (C-42 + C-43), V-05 (C-42 + C-43 + bidirectional navigation protocol).

---

## Summary Table

| ID | Primary Axis | C-42 Mechanism | C-43 Mechanism | Hypothesis |
|----|-------------|----------------|----------------|------------|
| V-01 | C-42 (single) | AUDIT MANIFEST gains `Derived Views` column per row; each downstream section header gains `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` | R17-V-05 three-column contract unchanged; no Manifest column field | Adding `Derived Views` to the manifest enables forward-direction navigation; an assessor at any manifest row can jump to the downstream table without reading phase text |
| V-02 | C-43 (single) | R17-V-05 backward citations only; no `Derived Views` column in manifest | PRE-EXECUTION CONTRACT gains a fourth column: `Manifest column` -- naming the exact AUDIT MANIFEST column that evidences each commitment | Adding `Manifest column` converts the contract from a phase-pointer into a data-pointer; an assessor can jump from any contract row to the exact manifest column before execution begins |
| V-03 | Phrasing register (single) | AUDIT MANIFEST uses ROUTE: / FEEDS: inline annotations per row instead of a structural `Derived Views` column | Contract rows use SOURCES: inline annotation instead of a structural `Manifest column` field | Tests whether inline annotations achieve C-42/C-43 intent at lower structural complexity; hypothesis is that structural columns are required for PASS (annotations = PARTIAL only) |
| V-04 | C-42 + C-43 (combined) | Per-row `Derived Views` column from V-01 | Per-row `Manifest column` field from V-02 | Zero-interference test: C-42 lives in the manifest table body; C-43 lives in the contract table body; independent structural locations with no shared modification surface |
| V-05 | Full integration | Per-row `Derived Views` column + bidirectional navigation verification protocol in Phase 0 SEAL | Per-row `Manifest column` field + contract becomes explicit assessor navigation index with starting-point instructions | Bidirectional audit trail made explicit: Phase 0 SEAL verifies both directions are navigable; contract opening instructions tell an assessor how to enter the audit trail from any starting point |

---

## V-01 -- `Derived Views` Column in AUDIT MANIFEST: C-42 via Forward-Direction Navigation

**Axis:** C-42 mechanism (single). The AUDIT MANIFEST gains a `Derived Views` column naming which downstream table(s) each row feeds. Each downstream section header gains a `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` declaration. All other mechanisms (including C-43 contract structure) unchanged from R17-V-05.

**Hypothesis:** R17-V-05's backward citations (downstream -> manifest) satisfy C-40 but only partially satisfy C-42. An assessor at a downstream table can find its source manifest, but an assessor reading the manifest cannot navigate forward to the downstream table without reading phase specifications. Adding `Derived Views` completes the forward direction -- the manifest becomes a fully navigable consistency surface from both entry points.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and its required value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. A completed retro is auditable against this contract without reading individual phase specifications. Signal window and Mode are structural fields, not prose.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in |
|-----------|------------------------------------------------|-------------|
| Signal window | Date range / sprint scope bounding which signal predictions are evaluated. Must be a named structural field, not inferred from prose. | Phase 0 AUDIT MANIFEST header row |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table present. FRESH: no scope restriction. Must be a named field. | Phase 0 AUDIT MANIFEST header; Phase 2 SEAL item 6 if AMEND |
| Echo lock | Phase 1 runs before signal comparison. Echo, Pattern, Why-unexpected locked in Phase 1 SEAL. Phases 2-9 may not modify them. | Phase 1 SEAL items 1-5 |
| Manifest derivation | All downstream tables (Phase 2 coverage, Phase 3 verdict, Phase 4 scoring, backward recovery) are derived as views of the AUDIT MANIFEST, not independently authored. Derivation relationship stated per section. | `Derived Views` column in AUDIT MANIFEST; `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` in each downstream section header |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete. | Phase 2 SEAL items 1-5 |
| Accuracy ratio | Phase 4: both weighted formula score ({N}/100) and count-based ratio ({N}/{M} = {X}%) required; both named SEAL fields. Reconciliation cross-check required: forward count and backward count must agree. | Phase 4 SEAL items 4-5; Phase 4 RECONCILIATION TABLE |
| Verdict sentence | Phase 6: both score formats copied from Phase 4. Exact sentence format. Tier label checked against stated score. | Phase 6 SEAL items 1-4 |
| Gap columns | Phase 7: Column A = prior belief ("We assumed X"), Column B = discovery missed; structurally isolated; same content in both = incomplete. | Phase 7 SEAL items 3-5 |
| Recommendation slots | Phase 7: three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive to output. | Phase 7 SEAL item 8 |
| Copy guard | Phase 8: score COPIED from Phase 6 verdict sentence verbatim. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three fields each with independent CHECK:/HOW: blocks. | Phase 8 SEAL items 2-4 (This score / COPY-VERIFIED / COPY-SOURCE) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 phase SEAL blocks |
| AMEND scope | When set: every table carries scope marker; Phase 2 has OOS secondary table. | Phase 2 SEAL item 6 when AMEND set |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts for this topic and build the AUDIT MANIFEST. All downstream tables in this retro are derived from this manifest; no downstream section independently authors data present here.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md for all artifacts associated with this topic. For each artifact, determine its namespace, primary prediction, and the post-ship actual outcome.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed would happen] | [what was observed] | C / P / W / ND | [list: which downstream tables this row feeds -- e.g., "Phase 2 coverage table; Phase 3 predicted/actual row; Phase 4 scoring"] |
| ... | | | | | | |

Derived Views values:
- Every row -> "Phase 2 coverage table (Namespace count)"
- COVERED rows with verdicts -> "Phase 3 predicted/actual table; Phase 4 accuracy scoring"
- W or P rows -> "Phase 7 gap table"
- All rows -> "Phase 4 TOTAL (denominator)" except ND rows which exclude from denominator

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field present in manifest header; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, {{amend}} scope carried into all phases
  [ ] Manifest rows: one row per signal artifact found; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views: non-blank per row -- names at least one downstream table; generic "downstream tables" = incomplete
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] -- [description of the recurring failure mode -- not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted -- what was expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR exact string "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR exact string "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description -- not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted -- names what was expected, not just that it was unexpected}"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row. Derive from Phase 0 AUDIT MANIFEST -- do not re-examine artifacts independently.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "--" -- not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

For each namespace with Status = COVERED in Phase 2. Derive from AUDIT MANIFEST rows -- do not independently re-evaluate predictions.

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [required -- from AUDIT MANIFEST Prediction column] | [required -- from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter COVERED namespaces]" present above table
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

RECONCILIATION TABLE -- confirm forward and backward counts agree:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from wrong verdicts]

| Direction | Starting point | Steps | Total predictions | Correct count | Match? |
|-----------|---------------|-------|-------------------|---------------|--------|
| Forward | Manifest row 1, sequentially count each scored verdict | [list: +1 C, +1 W, etc.] | {N} | {C count} | -- |
| Backward | Start with W count = {W}; add P = {P}; add C = {C}; total scored = {W+P+C} | [recovery arithmetic shown] | {N} | C = total - W - P = {C} | YES / NO |

Reconciliation result: Forward total = {N}; Backward total = {N}; Match: YES (proceed) / NO (do not proceed -- recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND columns: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals"
  [ ] TOTAL row: present, format: {number}/100
  [ ] Count-based ratio: stated in format "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with both Forward and Backward rows and a result row
  [ ] Reconciliation result: Match = YES before proceeding -- NO = reconciliation failure, do not continue
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values...]" present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding creating tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (Source, Analysis, Resolution all non-blank) OR exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: drawn from Phase 4 TOTAL row -- same number, not recalculated
  [ ] Count ratio: drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if >= 75 | ADEQUATE if 50-74 | WEAK if < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add EMPTY namespaces where absence is material]

For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision.

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

Column A = "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as prior belief ("We assumed X"), not an outcome.
Column B = "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [/exact-skill-name] | [discovery -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

Improvement recommendation -- three required slots. Replace each `[slot:X]` token. Output must contain no `[slot:` strings.

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern] by [slot:practice-change -- name the specific practice change, not generic] so that [slot:measurable-outcome -- state what would be observably different if this practice change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X" -- NOT an outcome statement, NOT blank
  [ ] Column B format: {discovery statement} -- different content from Column A
  [ ] Column A != Column B: both columns state different things per row
  [ ] Skill format: {/exact-skill-name} -- exact Signal skill, not a namespace name
  [ ] Changed commit: {YES} or {NO} per row
  [ ] Recommendation slot check: output does not contain "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]"
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter W or P rows; add material EMPTY namespaces]" present above gap table
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source -- transfer the number verbatim. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "--"] | {number}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [delta or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR exact string "none"
      Delta: {+N or -N or 0} OR "--" when no prior retro
      Trend: up improving | down degrading | = stable OR the "first retro" statement

  [ ] This score -- independent verification:
      CHECK: The Phase 8 calibration table "This score" cell contains a value.
      HOW: Read the "This score" cell in the Phase 8 calibration table above. Confirm it is non-blank and in {number}/100 format. Do not read Phase 6 or Phase 4 to verify this item -- this check is about the cell itself only.
      Format required: {number}/100 -- blank or wrong format = FAIL.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: The score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6. Read the verdict sentence. Find the score number (value before "/100"). Compare to "This score" cell value. If they match AND the cell label contains "COPY-VERIFIED", this item passes. Do not read Phase 4 to perform this check.
      Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL regardless of number match.

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as the copy source, not Phase 4.
      HOW: Read the "This score" cell label. Confirm it names "Phase 6 verdict" or equivalent. A label naming Phase 4, absent label, or label saying "computed" = FAIL. Arriving at the same number via Phase 4 does not satisfy this check -- the source is the label, not the value's mathematical origin.
      Format required: cell label contains "source: Phase 6 verdict" -- alternative source or blank = FAIL.

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern name -- same taxonomy label] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- exact match, not synonym
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict per row, Derived Views per row. All downstream tables derived from this manifest.
- Phase 1: Echo locked. Pattern and Why-unexpected required. Locked before signal comparison.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 3: [DERIVED FROM: AUDIT MANIFEST] header required. One row per COVERED namespace.
- Phase 4: Weighted score AND N/M=X% count ratio -- both required. RECONCILIATION TABLE required. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot `[slot:X]`; no `[slot:` strings in output. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three independent fields each with CHECK:/HOW: blocks.
- All 9 seals: explicit format-string per field.
```

---

## V-02 -- `Manifest column` Field in PRE-EXECUTION CONTRACT: C-43 via Data-Pointer Navigation

**Axis:** C-43 mechanism (single). The PRE-EXECUTION CONTRACT gains a fourth column: `Manifest column` -- naming the exact AUDIT MANIFEST column that will evidence each commitment. This converts each contract row from a phase-pointer ("Verified in: Phase 4 SEAL") into a data-pointer ("Manifest column: Verdict"). All other mechanisms (including C-42 manifest Derived Views column) unchanged from R17-V-05.

**Hypothesis:** R17-V-05's three-column contract (Mechanism / Guarantee / Verified in) satisfies C-33/C-39 but fails C-43 because "Verified in" points to a SEAL item (a procedural check) not to a manifest column (a data source). C-43's pass condition requires the exact AUDIT MANIFEST column name. An assessor who reads the contract should be able to jump to the exact manifest column -- before execution -- without reading phase specifications. The `Manifest column` field delivers that navigation.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and its required value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. A completed retro is auditable against this contract. Each row names a mechanism, states what is enforced, identifies where it is verified in the phases, and names the exact AUDIT MANIFEST column that is the data source for that commitment.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope for predictions evaluated. Named structural field in manifest header. | Phase 0 SEAL item 1 | Signal window (manifest header field, not a data column) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 runs before signal comparison. Echo, Pattern, Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from Prediction column) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived from manifest by namespace grouping. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Both weighted score and count-based ratio required. Forward/backward reconciliation required. | Phase 4 SEAL items 4-5; Phase 4 RECONCILIATION TABLE | Verdict |
| Gap identification | W or P rows from manifest feed gap table. EMPTY namespaces with material absence included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 verdict sentence copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation at any stage. | Phase 6 SEAL items 1-4; Phase 8 SEAL items 2-4 | Verdict (aggregate: TOTAL weighted score) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery. Structurally isolated; must not share content. | Phase 7 SEAL items 3-5 | Verdict (gap rows only; Column A maps to assumption field, not a manifest column) |
| Recommendation slots | Three `[slot:X]` tokens in Phase 7; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (no manifest column -- recommendation is generated, not derived) |
| Copy guard | Phase 8 score COPIED from Phase 6 verdict sentence. Three-field SEAL: This score / COPY-VERIFIED / COPY-SOURCE each independently verified. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field. | All 9 SEAL blocks | (all columns -- seals verify format of values derived from manifest) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns -- scope filter applied to all manifest rows) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables derive from this manifest.

Signal window: [state the date range or sprint scope]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md for all artifacts. For each artifact, record namespace, primary prediction, and post-ship actual outcome.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) |
|---|-----------|----------|----------------------------|-------------------|-------------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND |
| ... | | | | | |

Note: Derivation relationships are declared in downstream section headers -- each downstream section carries `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]`.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present
  [ ] Manifest rows: one row per signal artifact; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] -- [description of recurring failure mode -- not an Echo restatement]
  > **Why unexpected**: [prior belief or model contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR exact string "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR exact string "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table derived from Phase 0 AUDIT MANIFEST.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order
  [ ] Status: {COVERED} or {EMPTY} per row
  [ ] Artifact count: {integer} per row
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row: present with {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table{{/if}}
  [ ] Derived From header: present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial, W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2
  [ ] Predicted: {statement} -- not blank, not "N/A"
  [ ] Actual: {statement} -- not blank, not "N/A"
  [ ] Match: C | P | W | ND
  [ ] Derived From header: present above table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note: "0 scored signals").

After scoring table:
  Correct signals: {C count} / {C+P+W count} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Manifest row 1, count each scored verdict | [+1 C, +1 W, etc.] | {N} | {C} | -- |
| Backward | W count = {W}; +P = {P}; +C = {C}; total = {N} | [arithmetic shown] | {N} | {C} = total - W - P | YES / NO |

Reconciliation result: Forward = {N}; Backward = {N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace
  [ ] C, P, W, ND: {integer} per cell
  [ ] Weighted score: {number}/100 OR "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count-based ratio: "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with Forward and Backward rows and result row
  [ ] Reconciliation result: Match = YES before proceeding
  [ ] Derived From header: present above scoring table
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Exactly one of two outputs.

Does any Phase 3 verdict or Phase 4 score suggest the locked Phase 1 Echo should name a different finding?

If YES: CONFLICT DETECTED / Source: {finding} / Analysis: {what Echo should become} / Resolution: Phase 1 Echo preserved unchanged.
If NO: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."

PHASE 5 SEAL -- format contract:
  [ ] Output: CONFLICT DETECTED block (Source/Analysis/Resolution non-blank) OR exact "CONFLICT AUDIT: No conflict..." string
  [ ] Phase 1 modification: none
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based statement. Do not recalculate.

"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: from Phase 4 TOTAL -- not recalculated
  [ ] Count ratio: from Phase 4 count-based statement -- not recalculated
  [ ] Tier label: matches stated score thresholds
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add material EMPTY namespaces]

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

Column A = prior belief ("We assumed X"), NOT an outcome. Column B = discovery missed, different from Column A.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief] | [/exact-skill-name] | [discovery -- distinct from A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

> **Recommendation**: Addresses [slot:gap-or-echo] by [slot:practice-change] so that [slot:measurable-outcome].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 present OR "no gaps" statement
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A: prior belief framed "We assumed X" -- not outcome, not blank
  [ ] Column B: different content from Column A
  [ ] Column A != Column B per row
  [ ] Skill: {/exact-skill-name}
  [ ] Changed commit: YES | NO per row
  [ ] Recommendation slot check: no "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" in output
  [ ] Derived From header: present above gap table
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY the score from Phase 6 verdict sentence. Do not recompute. Label: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior or "--"] | {number}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [delta or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic} / {YYYY-MM-DD} OR "none"
      Delta: {+N or -N or 0} OR "--"
      Trend: up improving | down degrading | = stable OR "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell is non-blank and in {number}/100 format.
      HOW: Read "This score" cell only. Do not read Phase 6 or Phase 4 to verify this item.
      Format required: {number}/100.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6 verdict sentence. Find score before "/100". Compare to "This score" value. Cell label must contain "COPY-VERIFIED". Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED".

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm it names "Phase 6 verdict". Phase 4 reference or absent label = FAIL.
      Format required: label contains "source: Phase 6 verdict".

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- verbatim] | [exact Pattern taxonomy label -- verbatim] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: verbatim match to Phase 1 Echo cell
  [ ] Pattern cell: verbatim match to Phase 1 Pattern taxonomy label
  [ ] Proposed change: specific and actionable -- not "gather more signals"
  [ ] Change type: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees:
- PRE-EXECUTION CONTRACT: four-column table (Mechanism / Guarantee / Verified in / Manifest column). Manifest column names exact AUDIT MANIFEST column evidencing each commitment.
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict per row. Downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK/HOW blocks.
```

---

## V-03 -- Receipt/Navigation Format: Phrasing Register Variation

**Axis:** Phrasing register (single). AUDIT MANIFEST rows use inline FEEDS: annotations (not a structural `Derived Views` column). PRE-EXECUTION CONTRACT rows use inline SOURCES: annotations (not a structural `Manifest column` field). All phase logic and SEAL specifications unchanged from R17-V-05.

**Hypothesis:** Structural columns (V-01's `Derived Views`, V-02's `Manifest column`) should be required for C-42/C-43 PASS -- the rubric specifies "neither can be passed by prose substitution." This variation tests that hypothesis by providing the same information as inline annotations, predicting they will score PARTIAL on C-42 and C-43 while scoring identically on all other criteria. Useful to confirm the structural-column requirement is enforced, not just implied.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. Each mechanism row states what is enforced and where it is verified.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in |
|-----------|------------------------------------------------|-------------|
| Signal window | Bounding date range or sprint scope. Named field in manifest header. SOURCES: AUDIT MANIFEST header. | Phase 0 SEAL item 1 |
| Mode | AMEND or FRESH flag. AMEND: scoped, Phase 2 OOS table. SOURCES: AUDIT MANIFEST header. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND |
| Echo lock | Phase 1 runs before comparison. Echo/Pattern/Why-unexpected locked. SOURCES: AUDIT MANIFEST Prediction column (absence). | Phase 1 SEAL items 1-5 |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY. SOURCES: AUDIT MANIFEST Namespace column. | Phase 2 SEAL items 1-5 |
| Verdict accuracy | Both weighted score and count ratio required. Reconciliation cross-check required. SOURCES: AUDIT MANIFEST Verdict column. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE |
| Gap identification | W or P manifest rows feed gap table. SOURCES: AUDIT MANIFEST Verdict column (filter W/P). | Phase 7 SEAL items 1-2 |
| Accuracy copy | No recomputation at Phase 6 or Phase 8. SOURCES: AUDIT MANIFEST Verdict column (aggregate). | Phase 6 SEAL; Phase 8 SEAL |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content. SOURCES: AUDIT MANIFEST Verdict (gap rows). | Phase 7 SEAL items 3-5 |
| Recommendation slots | Three `[slot:X]` tokens; no `[slot:` strings in output. SOURCES: generated, not manifest-derived. | Phase 7 SEAL item 8 |
| Copy guard | Phase 8: three-field SEAL, each with independent CHECK/HOW. SOURCES: AUDIT MANIFEST Verdict (aggregate). | Phase 8 SEAL items 2-4 |
| Seal format contracts | All 9 seals: explicit format-string per field. SOURCES: all manifest columns. | All 9 SEAL blocks |
| AMEND scope | Every table scoped when AMEND set. SOURCES: all manifest columns (scope filter). | Phase 2 SEAL item 6 |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST.

Signal window: [state the date range or sprint scope]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual outcome.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) |
|---|-----------|----------|----------------------------|-------------------|-------------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND |
| ... | | | | | |

Navigation notes (inline):
- Rows where Verdict = COVERED group -> FEEDS: Phase 2 coverage table
- Rows where Namespace is COVERED and Verdict is set -> FEEDS: Phase 3 predicted/actual; Phase 4 scoring
- Rows where Verdict = W or P -> FEEDS: Phase 7 gap table
- All scored rows (exclude ND) -> FEEDS: Phase 4 denominator

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named field, not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present
  [ ] Manifest rows: one row per signal artifact
  [ ] Verdict: {C | P | W | ND} per row
  [ ] Navigation notes: inline FEEDS: annotations present naming downstream tables
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying:
  (a) Not predicted by any gathered signal
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance |
|---------------------|------------------------|-----------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | HIGH / MEDIUM / LOW / N/A |

  > **Pattern**: [taxonomy label] -- [failure class description -- not Echo restatement]
  > **Why unexpected**: [prior belief or model contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {filename.md} OR "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
(Derived from AUDIT MANIFEST by grouping on Namespace column.)

Produce a fixed 9-row namespace coverage table.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to OOS table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}OOS artifacts: | Namespace | Artifact | Excluded because | -- or "No artifacts excluded -- all in scope."{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order
  [ ] Status: COVERED or EMPTY per row
  [ ] Artifact count: {integer} per row
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row present
  {{#if amend}}[ ] OOS table present{{/if}}
  [ ] Derivation note present above table: "(Derived from AUDIT MANIFEST by grouping on Namespace column.)"
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
(Derived from AUDIT MANIFEST by filtering COVERED namespaces.)

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction] | [from AUDIT MANIFEST Actual] | [from AUDIT MANIFEST Verdict] |

PHASE 3 SEAL -- format contract:
  [ ] Row count: one per COVERED namespace
  [ ] Predicted: {statement} -- not blank, not "N/A"
  [ ] Actual: {statement} -- not blank, not "N/A"
  [ ] Match: C | P | W | ND
  [ ] Derivation note present above table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
(Derived from AUDIT MANIFEST by counting Verdict values per Namespace; ND excluded from denominator.)

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

  Correct signals: {C} / {C+P+W} = X%

RECONCILIATION TABLE (derived from AUDIT MANIFEST Verdict column):
| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Row 1 sequentially | [+1 C, etc.] | {N} | {C} | -- |
| Backward | W={W}, +P={P}, +C={C}, total={N} | [shown] | {N} | {C} | YES / NO |

Reconciliation result: Match = YES / NO.

PHASE 4 SEAL -- format contract:
  [ ] Row count: one per Phase 3 namespace
  [ ] C, P, W, ND: {integer} per cell
  [ ] Weighted score: {number}/100 or "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count ratio: "{N}/{M} = {X}%" below scoring table
  [ ] RECONCILIATION TABLE present with result row
  [ ] Reconciliation Match = YES before proceeding
  [ ] Derivation note present above scoring table
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Does any Phase 3 or Phase 4 finding suggest the locked Echo should name a different finding?

If YES: CONFLICT DETECTED / Source / Analysis / Resolution: Phase 1 Echo preserved.
If NO: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."

PHASE 5 SEAL: one of two exact outputs; no Phase 1 modification.

---

PHASE 6 -- ACCURACY VERDICT
Draw from Phase 4 TOTAL and count-based statement. Do not recalculate.
"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG/ADEQUATE/WEAK]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL: verdict sentence in exact format; both values drawn from Phase 4, not recalculated; tier label matches score.

---

PHASE 7 -- GAP ANALYSIS
(Derived from AUDIT MANIFEST by filtering W or P verdict rows; add material EMPTY namespaces.)

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Column A = prior belief ("We assumed X"). Column B = discovery missed. Must differ.

| Gap | Namespace | Assumption held without evidence [A] | Skill | Would have surfaced [B] | Changed commit? |
|-----|-----------|--------------------------------------|-------|------------------------|----------------|
| [type] | [ns] | [prior belief] | [/skill-name] | [discovery] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

> **Recommendation**: Addresses [slot:gap-or-echo] by [slot:practice-change] so that [slot:measurable-outcome].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace present OR "no gaps"
  [ ] Material EMPTY namespaces with rows
  [ ] Column A: "We assumed X" framing -- not outcome
  [ ] Column B: different from Column A
  [ ] Skill: {/exact-skill-name}
  [ ] Changed commit: YES | NO
  [ ] Slot check: no "[slot:" strings in output
  [ ] Derivation note present above gap table
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY score from Phase 6 verdict sentence. Label: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro | Prior score | This score | Delta | Trend |
|-------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior: "First retro -- this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} or "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score (independent):
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read cell only. Do not read Phase 6 or Phase 4.

  [ ] COPY-VERIFIED (independent):
      CHECK: Score copied from Phase 6, not computed.
      HOW: Read Phase 6 verdict sentence; compare to cell value; verify "COPY-VERIFIED" label. Do not read Phase 4.

  [ ] COPY-SOURCE (independent):
      CHECK: Cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label; confirm "Phase 6 verdict". Phase 4 reference or absent label = FAIL.

All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN

| Echo (verbatim from Phase 1) | Pattern (verbatim from Phase 1) | Proposed change | Change type |
|------------------------------|--------------------------------|----------------|-------------|
| [exact Phase 1 Echo cell] | [exact Phase 1 taxonomy label] | [specific action] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL: Echo verbatim; Pattern verbatim; change specific; change type = one of three values. RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9.
```

---

## V-04 -- `Derived Views` Column + `Manifest column` Field: C-42 + C-43 Combined

**Axis:** C-42 + C-43 combined. AUDIT MANIFEST gains `Derived Views` column per row (V-01). PRE-EXECUTION CONTRACT gains `Manifest column` field as fourth column (V-02). All other mechanisms unchanged. Zero-interference test: the two additions live in separate tables (manifest body vs. contract body) with no shared modification surface.

**Hypothesis:** C-42 and C-43 target different structural locations in the retro and do not compete for the same text. Adding both simultaneously should produce full PASS on both without any mechanism interfering with the other, since the manifest `Derived Views` column and the contract `Manifest column` field are in independent table cells.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. A completed retro is auditable against this contract. `Verified in` names the phase SEAL item enforcing the mechanism. `Manifest column` names the exact AUDIT MANIFEST column that is the data source for that commitment -- an assessor can navigate from any contract row to the manifest column that will evidence it before execution begins.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is absent from this column) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest on Namespace. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Both weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate: TOTAL weighted score) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content. | Phase 7 SEAL items 3-5 | Verdict (gap rows; Column A is assumption, not a manifest column itself) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8: score COPIED from Phase 6. Three-field SEAL: This score/COPY-VERIFIED/COPY-SOURCE each independent. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns -- scope filter applied) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables are derived from this manifest. The `Derived Views` column names which downstream tables each row feeds -- an assessor reading any manifest row can navigate forward to the downstream tables that include it.

Signal window: [state the date range or sprint scope]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual outcome, verdict, and which downstream tables the row feeds.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [Phase 2 coverage table; Phase 3 predicted/actual; Phase 4 accuracy scoring (if scored); Phase 7 gap table (if W or P)] |
| ... | | | | | | |

Derived Views values (standard assignments):
- Every row (regardless of verdict) -> "Phase 2 coverage table (Namespace count)"
- Rows with a non-ND verdict -> "Phase 3 predicted/actual table; Phase 4 accuracy scoring (denominator)"
- Rows with Verdict = W -> "Phase 4 accuracy scoring (W count); Phase 7 gap table"
- Rows with Verdict = P -> "Phase 4 accuracy scoring (P count); Phase 7 gap table"
- Rows with Verdict = C -> "Phase 4 accuracy scoring (C count)"
- Rows with Verdict = ND -> "Phase 4 accuracy scoring (ND count -- excluded from denominator)"

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present
  [ ] Manifest rows: one per signal artifact
  [ ] Verdict: {C | P | W | ND} per row
  [ ] Derived Views: non-blank per row -- names at least one downstream table by name; "downstream tables" alone = incomplete
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

  > **Pattern**: [taxonomy label or "other: name"] -- [failure class description -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {filename.md} OR "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {label} -- {failure class description}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table derived from Phase 0 AUDIT MANIFEST.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order
  [ ] Status: COVERED or EMPTY per row
  [ ] Artifact count: {integer} per row
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row present
  {{#if amend}}[ ] OOS table present{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction] | [from AUDIT MANIFEST Actual] | [from AUDIT MANIFEST Verdict] |

PHASE 3 SEAL -- format contract:
  [ ] Row count: one per COVERED namespace from Phase 2
  [ ] Predicted: {statement} -- not blank, not "N/A"
  [ ] Actual: {statement} -- not blank, not "N/A"
  [ ] Match: C | P | W | ND
  [ ] Derived From header present above table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

  Correct signals: {C} / {C+P+W} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Manifest row 1, count each scored verdict | [+1 C, +1 W, etc.] | {N} | {C} | -- |
| Backward | W={W}; +P={P}; +C={C}; total={N} | [arithmetic shown] | {N} | {C}=total-W-P | YES / NO |

Reconciliation result: Forward={N}; Backward={N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one per Phase 3 namespace
  [ ] C, P, W, ND: {integer} per cell
  [ ] Weighted score: {number}/100 or "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count ratio: "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE present with Forward, Backward, and result rows
  [ ] Reconciliation Match = YES before proceeding
  [ ] Derived From header present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Does any Phase 3 or Phase 4 finding suggest the locked Phase 1 Echo should change?

If YES: CONFLICT DETECTED / Source / Analysis / Resolution: Phase 1 Echo preserved.
If NO: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."

PHASE 5 SEAL: exactly one of two outputs; no Phase 1 modification.
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw from Phase 4 TOTAL row and count-based statement. Do not recalculate.
"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG/ADEQUATE/WEAK]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL: verdict in exact format; both values drawn from Phase 4; tier label matches score.
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add material EMPTY namespaces]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Column A = prior belief ("We assumed X"). Column B = discovery missed. Must differ per row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X"] | [/exact-skill-name] | [discovery -- distinct from A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

  > **Recommendation**: Addresses [slot:gap-or-echo] by [slot:practice-change] so that [slot:measurable-outcome].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 OR "no gaps"
  [ ] Material EMPTY namespaces with rows
  [ ] Column A: "We assumed X" -- not outcome, not blank
  [ ] Column B: different from Column A
  [ ] Column A != Column B per row
  [ ] Skill: {/exact-skill-name}
  [ ] Changed commit: YES | NO per row
  [ ] Slot check: no "[slot:" strings in output
  [ ] Derived From header present above gap table
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY score from Phase 6 verdict sentence. Do not recompute. Label: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior: "First retro -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} or "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read "This score" cell in Phase 8 table only. Do not read Phase 6 or Phase 4.
      Format required: {number}/100.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6. Read verdict sentence. Find score before "/100". Compare to "This score" value. "COPY-VERIFIED" label must be present. Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED".

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm it names "Phase 6 verdict". Phase 4 reference or absent label = FAIL.
      Format required: label contains "source: Phase 6 verdict".

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN

| Echo (verbatim from Phase 1) | Pattern (verbatim from Phase 1) | Proposed change | Change type |
|------------------------------|--------------------------------|----------------|-------------|
| [exact Phase 1 Echo cell] | [exact Phase 1 taxonomy label] | [specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL: Echo verbatim; Pattern verbatim; change specific; change type = one of three values.
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees:
- PRE-EXECUTION CONTRACT: four-column table (Mechanism / Guarantee / Verified in / Manifest column). Each row maps to exact AUDIT MANIFEST column that evidences the commitment.
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict per row, Derived Views per row naming downstream tables. All downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE with Forward/Backward rows required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK/HOW blocks.
- All 9 seals: explicit format-string per field.
```

---

## V-05 -- Full Integration: C-42 + C-43 + Bidirectional Navigation Protocol

**Axis:** Full integration. Adds both V-01 and V-04 mechanisms, plus an explicit bidirectional navigation verification in Phase 0 SEAL and assessor entry-point instructions at the top of the document. The PRE-EXECUTION CONTRACT opening paragraph tells an assessor how to enter the audit trail from any starting point (manifest row -> downstream table, downstream section -> manifest, contract row -> manifest column). Phase 0 SEAL verifies both directions are navigable before Phase 1 begins.

**Hypothesis:** V-04 adds the structural columns required for C-42/C-43 PASS. V-05 converts the bidirectional trail into an explicit navigable surface by (a) adding assessor instructions naming every valid entry point, and (b) adding a Phase 0 SEAL item that verifies both forward and backward navigation are functional -- not just that the columns exist. The additional SEAL item prevents a prompt execution that fills the Derived Views column with generic text or maps the Manifest column field to section names rather than column names (both PARTIAL conditions per rubric).

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. This retro is a bidirectional audit system navigable from three entry points:

**Entry from AUDIT MANIFEST row**: Use the `Derived Views` column to identify which downstream tables the row feeds. Navigate forward without reading phase specifications.
**Entry from downstream section**: Use the `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` header to navigate backward to the manifest rows that sourced the section.
**Entry from contract row**: Use the `Manifest column` field to identify the exact AUDIT MANIFEST column that will evidence fulfillment of each commitment. Navigate to the manifest before execution begins.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL items 1, 5-forward | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. Derived Views column present in manifest. | Phase 0 SEAL items 3-4 (forward) + [DERIVED FROM] headers in all downstream sections (backward) | (all columns -- manifest is the derivation source) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 sentence. No recomputation at any stage. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate: TOTAL weighted score) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows; Column A frames the assumption behind a W/P verdict) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL: This score / COPY-VERIFIED / COPY-SOURCE each with independent CHECK/HOW. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns -- scope filter applied to all manifest rows) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables are derived from this manifest. The `Derived Views` column enables forward navigation: an assessor at any manifest row can identify which downstream tables include it without reading phase specifications.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual outcome, verdict, and forward-navigation destinations.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed would happen] | [what was observed post-ship] | C / P / W / ND | [Phase 2 coverage table (Namespace count); Phase 3 predicted/actual; Phase 4 accuracy scoring (specify: C/P/W/ND count); Phase 7 gap table (if W or P)] |
| ... | | | | | | |

Derived Views assignment rules:
- Every row -> "Phase 2 coverage table (Namespace count)"
- Rows with non-ND verdict -> add "Phase 3 predicted/actual; Phase 4 accuracy scoring ({verdict-type} count)"
- Rows with Verdict = W or P -> add "Phase 7 gap table"
- Rows with Verdict = ND -> add "Phase 4 accuracy scoring (ND -- excluded from denominator)"

After completing the manifest, state the bidirectional navigation check:
  Forward check: "For each manifest row, Derived Views names at least one specific downstream table by exact table name."
  Backward check: "Each downstream section (Phase 2, Phase 3, Phase 4, Phase 7) will carry [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming this manifest as its source."

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present
  [ ] Manifest rows: one per signal artifact found; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views: non-blank per row -- names at least one downstream table by exact table name (e.g., "Phase 2 coverage table", "Phase 7 gap table") -- "downstream tables" alone = incomplete; generic text = incomplete
  [ ] Forward check statement: present after manifest, confirms Derived Views naming is specific
  [ ] Backward check statement: present after manifest, confirms [DERIVED FROM] headers will appear in downstream sections
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

  > **Pattern**: [taxonomy label or "other: name"] -- [failure class description -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {filename.md} OR "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {label} -- {failure class description, not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table derived from Phase 0 AUDIT MANIFEST.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row present with {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table present immediately after main table{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial, W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one per COVERED namespace from Phase 2 -- no omissions
  [ ] Predicted: {statement} -- not blank, not "N/A"
  [ ] Actual: {statement} -- not blank, not "N/A"
  [ ] Match: C | P | W | ND
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter COVERED namespaces]" present above table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND rows from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

  Correct signals: {C count} / {C+P+W count} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count of all Verdict rows vs backward recovery starting from Verdict = W count]

| Direction | Starting point | Steps (show arithmetic) | Total scored predictions | Correct count | Match? |
|-----------|---------------|------------------------|--------------------------|---------------|--------|
| Forward | Manifest row 1, count each scored verdict sequentially | [+1 C at row N, +1 W at row M, etc.] | {total} | {C count} | -- |
| Backward | Start: W count = {W}. Add P = {P}. Add C = {C}. Total = {W+P+C} | [W+P+C = {N}; C = {N} - W - P = {C}] | {total} | {C count} | YES / NO |

Reconciliation result: Forward total = {N}; Backward total = {N}; Match: YES (proceed) / NO (do not proceed -- recheck manifest rows).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one per Phase 3 namespace
  [ ] C, P, W, ND: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count-based ratio: "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with Forward row, Backward row, and reconciliation result row
  [ ] Reconciliation result: Match = YES before proceeding -- NO = reconciliation failure, recheck
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values...]" present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always exactly one of two outputs.

Does any Phase 3 verdict or Phase 4 score suggest the locked Phase 1 Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 namespace / Phase 4 score -- specific finding creating tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: CONFLICT DETECTED block (Source/Analysis/Resolution non-blank) OR exact "CONFLICT AUDIT: No conflict..." string
  [ ] Phase 1 modification: none -- Echo table, Pattern, Why-unexpected unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based statement. Do not recalculate either number.

"Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: same number as Phase 4 TOTAL -- not recalculated
  [ ] Count ratio: same values as Phase 4 count-based statement -- not recalculated
  [ ] Tier label: STRONG if >= 75 | ADEQUATE if 50-74 | WEAK if < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add material EMPTY namespaces where absence was commit-relevant]

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

Column A = "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not an outcome.
Column B = "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [/exact-skill-name] | [discovery -- distinct from A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern] by [slot:practice-change -- specific practice change, not generic] so that [slot:measurable-outcome -- what would be observably different if this change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 present OR "no gaps" statement
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A: {prior belief} framed "We assumed X" -- NOT an outcome, NOT blank
  [ ] Column B: {discovery statement} -- different content from Column A
  [ ] Column A != Column B: both state different things per row
  [ ] Skill: {/exact-skill-name} -- exact Signal skill, not a namespace name
  [ ] Changed commit: {YES} or {NO} per row
  [ ] Slot check: output does not contain "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]"
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter W or P rows; add material EMPTY namespaces]" present above gap table
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source -- transfer the number verbatim. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "--"] | {number}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR exact string "none"
      Delta: {+N or -N or 0} OR "--" when no prior retro
      Trend: up improving | down degrading | = stable OR the "first retro" statement

  [ ] This score -- independent verification:
      CHECK: The Phase 8 calibration table "This score" cell contains a value.
      HOW: Read the "This score" cell in the Phase 8 calibration table above. Confirm it is non-blank and in {number}/100 format. Do not read Phase 6 or Phase 4 to verify this item -- this check is about the cell itself only.
      Format required: {number}/100 -- blank or wrong format = FAIL.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: The score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6. Read the verdict sentence. Find the score number (value before "/100" in that sentence). Compare to "This score" cell value. If they match AND the cell label contains "COPY-VERIFIED", this item passes. Do not read Phase 4 to perform this check.
      Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL regardless of number match.

  [ ] COPY-SOURCE -- independent verification:
      CHECK: The "This score" cell names Phase 6 verdict as the copy source, not Phase 4.
      HOW: Read the "This score" cell label. Confirm it names "Phase 6 verdict" or equivalent. A label naming Phase 4, a label absent, or a label saying "computed" = FAIL.
      Format required: cell label contains "source: Phase 6 verdict" -- alternative source or blank = FAIL.

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern taxonomy label -- same label, not synonym] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- exact match, not synonym
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- PRE-EXECUTION CONTRACT: four-column table (Mechanism / Guarantee / Verified in / Manifest column). `Manifest column` names exact AUDIT MANIFEST column evidencing each commitment. Navigation entry-point instructions in contract opening block.
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict per row, and Derived Views per row naming exact downstream tables. Phase 0 SEAL verifies both forward navigation (Derived Views present and specific) and backward navigation (DERIVED FROM headers will appear in downstream sections). Bidirectional navigation check statement required before PHASE 0 COMPLETE.
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table. [DERIVED FROM] header required.
- Phase 3: [DERIVED FROM] header required.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE with Forward, Backward, and result rows required. [DERIVED FROM] header required.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot `[slot:X]`; no `[slot:` strings in output. [DERIVED FROM] header required.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three named fields each with independent CHECK/HOW blocks.
- All 9 seals: explicit format-string per field.
```
