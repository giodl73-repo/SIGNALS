# topic-retro — Variations R13
**Date:** 2026-03-17
**Rubric:** v11 (C-01 through C-33; total available = 140)
**R12 top scorer:** V-05 (source of C-32, C-33 criteria) — three-field SEAL + pre-execution contract table.
**New criteria to target:** C-32 (phase-8-seal-fields-independent-verification) and C-33 (design-guarantees-mechanism-keyed-table).

**Base used:** R12-V-05 — all R12 integrations carried forward:
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

**C-32 gap analysis:** R12-V-05's Phase 8 SEAL carries three named fields, but the verification instructions form a sequential chain rather than three independent audit procedures. `COPY-VERIFIED` says "the 'This score' value was traced..." -- it references the prior item. `COPY-SOURCE` says "the authoritative source is Phase 6, not Phase 4; confirm by opening Phase 6" -- it implicitly depends on COPY-VERIFIED's context to know what "opening Phase 6" resolves. C-32 requires each field carry its own independent verification instruction: a reviewer must be able to verify one field without reading the others. The fix: each SEAL field needs an explicit CHECK: / HOW: block naming its own source and criterion, not referencing sibling fields.

**C-33 gap analysis:** R12-V-05's PRE-EXECUTION CONTRACT satisfies C-31 (dedicated section, specific mechanisms named). C-33's pass condition requires the two-column table with mechanism names as independently addressable row keys -- V-05 has this. The Round 13 excellence target for C-33: adding a "Verified in" column that maps each mechanism to the exact SEAL field or phase where it is enforced. This converts the table from a guarantee summary into an audit map -- each guarantee is both named by mechanism and navigable to its enforcement point without reading phase specifications.

**Single-axis:** V-01 (C-32), V-02 (C-33), V-03 (phrasing register).
**Combined:** V-04 (C-32 + C-33), V-05 (C-32 + C-33 + cross-linking extension to Phase 1 and Phase 7 SEALs).

---

## Summary Table

| ID | Primary Axis | C-32 Mechanism | C-33 Mechanism | Hypothesis |
|----|-------------|----------------|----------------|------------|
| V-01 | C-32 (single) | Phase 8 SEAL: each field gets explicit CHECK: / HOW: block with its own named source -- no cross-references between items | R12-V-05 two-column table unchanged | Per-field CHECK/HOW blocks make each item independently executable; a reviewer can audit COPY-VERIFIED without reading This score first |
| V-02 | C-33 (single) | R12-V-05 three-field SEAL unchanged | Three-column table: Mechanism / Structural guarantee / Verified in -- each row maps to the exact phase and SEAL field enforcing it | Adding a "Verified in" column converts the table from a guarantee summary into an audit map; a reviewer can jump from the table to the enforcement point without reading phase text |
| V-03 | Phrasing register (single) | Phase 8 SEAL: verification-receipt format -- ITEM / VERIFY / SOURCE / FORMAT / RESULT per field instead of checklist items | PRE-EXECUTION CONTRACT: ENFORCE IN: inline annotation added per row | Receipt format names each item's own source explicitly without CHECK/HOW tokens -- tests whether format change achieves C-32 independence at lower structural complexity |
| V-04 | C-32 + C-33 (combined) | Per-field CHECK/HOW blocks from V-01 | Three-column "Verified in" table from V-02 | Zero-interference test: C-32 lives in Phase 8 SEAL; C-33 lives in PRE-EXECUTION CONTRACT; independent structural locations |
| V-05 | Full integration | Per-field CHECK/HOW blocks in Phase 8 SEAL + extended to Phase 1 SEAL (Echo lock) and Phase 7 SEAL (recommendation slot guard) | Three-column table (V-02) + expanded to 12 rows splitting Copy guard into three independent rows + trailing DESIGN GUARANTEES section | Cross-linking: Phase 8 SEAL items cite PRE-EXECUTION CONTRACT row; contract rows name SEAL items; bidirectional audit trail |

---

## V-01 -- Per-Field CHECK/HOW Blocks: C-32 via Independent Verification Instructions in Phase 8 SEAL

**Axis:** C-32 mechanism (single). Phase 8 SEAL restructured: each of the three named fields (This score, COPY-VERIFIED, COPY-SOURCE) carries its own CHECK: / HOW: block that names its own source and criterion without referencing sibling fields. A reviewer can verify any one item by reading only its own block.

**Hypothesis:** R12-V-05's SEAL items form a logical chain -- COPY-VERIFIED says "the 'This score' value was traced," linking it to item 1. Splitting into CHECK/HOW blocks with self-contained source references makes each item independently auditable. All phases outside Phase 8 SEAL unchanged from R12-V-05.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL -- a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

The following structural guarantees must hold across all phases. Read before executing Phase 1. A completed retro is auditable against this contract without reading individual phase specifications.

| Mechanism | Structural guarantee -- what is enforced and how |
|-----------|------------------------------------------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected locked in Phase 1 SEAL; Phases 2-9 must not modify them |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete |
| Accuracy ratio | Phase 4: both weighted formula score ({N}/100) and count-based ratio ({N}/{M} = {X}%) required; both are named SEAL fields |
| Verdict sentence | Phase 6: both score formats copied from Phase 4; exact sentence format enforced; tier label (STRONG/ADEQUATE/WEAK) checked against stated score |
| Gap columns | Phase 7: Column A = prior belief ("We assumed X"), Column B = discovery missed; structurally isolated; must contain different statements |
| Recommendation slots | Phase 7: three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive |
| Copy guard | Phase 8: score COPIED from Phase 6 verdict sentence verbatim; cell labeled COPY-VERIFIED [source: Phase 6 verdict]; SEAL carries three named fields each with independent CHECK/HOW verification instructions |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence |
| AMEND scope | When set: every table has scope marker; Phase 2 has OOS secondary table |

---

PHASE 1 -- ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

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
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted -- what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo -- all post-ship outcomes were within signal bounds" -- not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" -- not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {description of failure class, not the Echo instance}" -- not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} -- must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

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

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic -- missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "--" -- not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required -- non-blank statement] | [required -- non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND -- no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND columns: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied -- format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" -- both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row -- same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A -- "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B -- "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

Improvement recommendation -- three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings -- their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern addressed] by [slot:practice-change -- name the specific practice change, not generic] so that [slot:measurable-outcome -- state what would be observably different if this practice change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement -- no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent -- NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} -- different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row -- same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} -- an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row -- no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" -- all three tokens replaced with specific content
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
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" -- not blank, not "N/A"
    Delta: {+N or -N or 0} OR "--" when no prior retro
    Trend: one of exactly: up improving | down degrading | = stable OR the "first retro" statement

  [ ] This score -- independent verification:
    CHECK: The Phase 8 calibration table "This score" cell contains a value.
    HOW: Read the "This score" cell in the Phase 8 calibration table above. Confirm it is non-blank and in {number}/100 format. Do not read Phase 6 or Phase 4 to verify this item -- this check is about the cell itself only.
    Format required: {number}/100 -- blank or wrong format = FAIL this item.

  [ ] COPY-VERIFIED -- independent verification:
    CHECK: The score in the "This score" cell was copied from Phase 6, not computed.
    HOW: Open Phase 6. Read the verdict sentence. Find the score number (the value before "/100" in that sentence). Compare to the "This score" cell value. If they match AND the cell label contains "COPY-VERIFIED", this item passes. Do not read Phase 4 to perform this check -- the comparison is between Phase 8 cell and Phase 6 verdict sentence only.
    Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL this item regardless of whether the number matches.

  [ ] COPY-SOURCE -- independent verification:
    CHECK: The "This score" cell names Phase 6 verdict as the copy source, not Phase 4.
    HOW: Read the "This score" cell label. Confirm it names "Phase 6 verdict" or equivalent. A label naming Phase 4, a label absent, or a label that says "computed" = FAIL this item. Arriving at the same number via Phase 4 does not satisfy this check -- the source is the label in the cell, not the value's mathematical origin.
    Format required: cell label contains "source: Phase 6 verdict" -- alternative source or blank label = FAIL this item.

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern name from Phase 1 -- same taxonomy label, not a synonym] | [one specific practice change -- not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- Phase 1: Echo locked. Pattern and Why-unexpected required. Locked before signal comparison.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio -- both required, both named SEAL fields.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot `[slot:X]` recommendation; no `[slot:` strings in output.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three independent fields each with CHECK/HOW blocks (This score / COPY-VERIFIED / COPY-SOURCE).
- All 9 seals: explicit format-string per field (not just field names).
- AMEND: scope marker on every table; Phase 2 OOS secondary table.
```

---

## V-02 -- Three-Column Guarantees Table: C-33 via "Verified in" Navigation Column

**Axis:** C-33 mechanism (single). The PRE-EXECUTION CONTRACT gains a third column: "Verified in" -- naming the exact phase and SEAL field where each mechanism is enforced. This converts the table from a guarantee summary into an audit map. Phase 8 SEAL and all other phases unchanged from R12-V-05.

**Hypothesis:** R12-V-05's two-column table satisfies C-33's basic requirement (mechanism-keyed rows). The Round 13 excellence target: making each guarantee independently locatable by mechanism name AND navigable to its enforcement point. The "Verified in" column creates a second audit axis -- a scorer auditing any mechanism can confirm enforcement without tracing phases.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL -- a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

The following structural guarantees must hold across all phases. Read before executing Phase 1. Each row names a mechanism, states what is enforced, and identifies where enforcement is verified.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in |
|-----------|------------------------------------------------|-------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected locked in Phase 1 SEAL; Phases 2-9 must not modify them | Phase 1 SEAL items 1-5 (Echo / Nearest signal / Commit relevance / Pattern / Why unexpected) |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete | Phase 2 SEAL items 1-5 |
| Accuracy ratio | Phase 4: both weighted formula score ({N}/100) and count-based ratio ({N}/{M} = {X}%) required; both are named SEAL fields | Phase 4 SEAL item 5 (Count-based ratio) |
| Verdict sentence | Phase 6: both score formats copied from Phase 4; exact sentence format enforced; tier label checked against stated score | Phase 6 SEAL items 1-4 |
| Gap columns | Phase 7: Column A = prior belief ("We assumed X"), Column B = discovery missed; structurally isolated; same content in both = incomplete | Phase 7 SEAL items 3-5 (Column A / Column B / Column A != Column B) |
| Recommendation slots | Phase 7: three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive to output | Phase 7 SEAL item 8 (Recommendation slot check) |
| Copy guard -- body | Phase 8: body instruction "COPY from Phase 6 verdict sentence. Do not recompute." Cell format string includes COPY-VERIFIED label and source | Phase 8 table cell format string |
| Copy guard -- SEAL | Phase 8 SEAL: three named fields -- This score (value), COPY-VERIFIED (operation confirmed), COPY-SOURCE (origin named as Phase 6 verdict sentence) | Phase 8 SEAL items 2-4 (This score / COPY-VERIFIED / COPY-SOURCE) |
| Seal format contracts | All 9 phase seals carry explicit format-string specifications per field -- not just field names | All 9 phase SEAL blocks |
| AMEND scope | When set: every phase table carries scope marker; Phase 2 includes OOS secondary table for excluded artifacts | Phase 2 SEAL item 6 (OOS table) when AMEND set |

---

PHASE 1 -- ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

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
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted -- what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo -- all post-ship outcomes were within signal bounds" -- not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" -- not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {description of failure class, not the Echo instance}" -- not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} -- must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

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

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic -- missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "--" -- not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required -- non-blank statement] | [required -- non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND -- no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND columns: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied -- format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" -- both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row -- same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A -- "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B -- "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

Improvement recommendation -- three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings -- their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern addressed] by [slot:practice-change -- name the specific practice change, not generic] so that [slot:measurable-outcome -- state what would be observably different if this practice change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement -- no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent -- NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} -- different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row -- same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} -- an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row -- no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" -- all three tokens replaced with specific content
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
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" -- not blank, not "N/A"
  [ ] This score: {number}/100 -- value must be present and non-blank
  [ ] COPY-VERIFIED: confirmed -- the "This score" value was traced to the Phase 6 verdict sentence directly; it was not recomputed from Phase 4 TOTAL; the cell carries the label "COPY-VERIFIED [source: Phase 6 verdict]"
  [ ] COPY-SOURCE: "Phase 6 verdict sentence" -- the authoritative source is Phase 6, not Phase 4; confirm by opening Phase 6 and reading the verdict sentence before marking this item complete
  [ ] Delta: {+N or -N or 0} OR "--" when no prior retro
  [ ] Trend: one of exactly: up improving | down degrading | = stable OR the "first retro" statement
All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern name from Phase 1 -- same taxonomy label, not a synonym] | [one specific practice change -- not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- Phase 1: Echo locked. Pattern and Why-unexpected required. Locked before signal comparison.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio -- both required, both named SEAL fields.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot `[slot:X]` recommendation; no `[slot:` strings in output.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three named fields (This score / COPY-VERIFIED / COPY-SOURCE -- see PRE-EXECUTION CONTRACT "Copy guard -- SEAL" row for Verified in mapping).
- All 9 seals: explicit format-string per field (not just field names).
- AMEND: scope marker on every table; Phase 2 OOS secondary table.
```

---

## V-03 -- Phrasing Register: Verification-Receipt Format for Phase 8 SEAL

**Axis:** Phrasing register (single). Phase 8 SEAL restructured using a verification-receipt format -- each item expressed as ITEM / VERIFY / SOURCE / FORMAT / RESULT rather than a checklist bullet. PRE-EXECUTION CONTRACT adds ENFORCE IN: inline annotation per row. All other phases unchanged from R12-V-05.

**Hypothesis:** The CHECK/HOW approach (V-01) introduces nested sub-items. The receipt format tests whether a flatter per-field layout achieves the same independence at lower structural complexity. Each receipt line names its own source explicitly, eliminating cross-reference chains. Risk: C-32 requires "named fields with independent verification instructions" -- a SEAL in receipt-table form may or may not satisfy the "named field" structural requirement if a scorer reads it as prose rather than a field registry.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL -- a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

The following structural guarantees must hold across all phases. Read before executing Phase 1.

| Mechanism | Structural guarantee -- what is enforced and how |
|-----------|------------------------------------------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected locked in Phase 1 SEAL; Phases 2-9 must not modify them. ENFORCE IN: Phase 1 SEAL items 1-5. |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete. ENFORCE IN: Phase 2 SEAL items 1-5. |
| Accuracy ratio | Phase 4: both weighted formula score ({N}/100) and count-based ratio ({N}/{M} = {X}%) required; both named SEAL fields. ENFORCE IN: Phase 4 SEAL item 5. |
| Verdict sentence | Phase 6: both score formats copied from Phase 4; exact sentence format enforced; tier label checked against score. ENFORCE IN: Phase 6 SEAL items 1-4. |
| Gap columns | Phase 7: Column A = prior belief, Column B = discovery missed; structurally isolated; same content in both = incomplete. ENFORCE IN: Phase 7 SEAL items 3-5. |
| Recommendation slots | Phase 7: three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. ENFORCE IN: Phase 7 SEAL item 8. |
| Copy guard | Phase 8: score COPIED from Phase 6 verdict sentence verbatim; cell labeled COPY-VERIFIED [source: Phase 6 verdict]; SEAL carries three named fields. ENFORCE IN: Phase 8 SEAL items 2-4. |
| Seal format contracts | All 9 phase seals carry explicit format-string specifications per field -- verify value form, not just presence. ENFORCE IN: all 9 SEAL blocks. |
| AMEND scope | When set: every table has scope marker; Phase 2 has OOS secondary table. ENFORCE IN: Phase 2 SEAL item 6 when AMEND set. |

---

PHASE 1 -- ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

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
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted -- what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo -- all post-ship outcomes were within signal bounds" -- not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" -- not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {description of failure class, not the Echo instance}" -- not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} -- must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

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

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic -- missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "--" -- not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required -- non-blank statement] | [required -- non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND -- no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND columns: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied -- format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" -- both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row -- same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A -- "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B -- "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

Improvement recommendation -- three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings -- their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern addressed] by [slot:practice-change -- name the specific practice change, not generic] so that [slot:measurable-outcome -- state what would be observably different if this practice change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement -- no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent -- NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} -- different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row -- same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} -- an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row -- no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" -- all three tokens replaced with specific content
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source -- transfer the number verbatim. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "--"] | {number}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [delta or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- verification receipts:

ITEM: Prior retro
VERIFY: Field contains either a topic name and date, or the exact string "none".
SOURCE: Phase 8 calibration table, "Prior retro" column -- read this cell directly.
FORMAT: {topic-name} / {YYYY-MM-DD} or "none" -- blank or "N/A" = FAIL.
RESULT: [PASS / FAIL]

ITEM: This score
VERIFY: Field contains a non-blank value in {number}/100 format.
SOURCE: Phase 8 calibration table, "This score" column -- read this cell directly. Do not read Phase 6 or Phase 4 to verify this item.
FORMAT: {number}/100 -- blank or wrong format = FAIL.
RESULT: [PASS / FAIL]

ITEM: COPY-VERIFIED
VERIFY: The score in "This score" was copied from Phase 6 verdict sentence, not computed from Phase 4.
SOURCE: Open Phase 6 only. Read the verdict sentence. Find the score (number before "/100"). Compare to "This score" cell value. The cell must also carry "COPY-VERIFIED" label. Do not open Phase 4 for this check.
FORMAT: Cell label contains "COPY-VERIFIED" and value matches Phase 6 verdict sentence -- mismatch or missing label = FAIL.
RESULT: [PASS / FAIL]

ITEM: COPY-SOURCE
VERIFY: The "This score" cell names Phase 6 verdict as copy source, not Phase 4.
SOURCE: Read the "This score" cell label only. Do not read any other field to verify this item.
FORMAT: Label contains "Phase 6 verdict" -- missing label or label naming Phase 4 = FAIL.
RESULT: [PASS / FAIL]

ITEM: Delta
VERIFY: Field contains a numeric delta or "--" for first retro.
SOURCE: Phase 8 calibration table, "Delta" column.
FORMAT: {+N or -N or 0} or "--" -- blank = FAIL.
RESULT: [PASS / FAIL]

ITEM: Trend
VERIFY: Field contains one of the three valid values or the first-retro statement.
SOURCE: Phase 8 calibration table, "Trend" column.
FORMAT: one of exactly: up improving | down degrading | = stable | "First retro for this topic -- this score establishes the calibration baseline." -- other values = FAIL.
RESULT: [PASS / FAIL]

All receipts PASS? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern name from Phase 1 -- same taxonomy label, not a synonym] | [one specific practice change -- not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- Phase 1: Echo locked. Pattern and Why-unexpected required. Locked before signal comparison.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio -- both required, both named SEAL fields.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot `[slot:X]` recommendation; no `[slot:` strings in output.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: verification-receipt format -- ITEM/VERIFY/SOURCE/FORMAT/RESULT per field.
- All 9 seals: explicit format-string per field (not just field names).
- AMEND: scope marker on every table; Phase 2 OOS secondary table.
```

---

## V-04 -- Combined: C-32 CHECK/HOW Blocks + C-33 Three-Column Guarantees Table

**Axes:** C-32 mechanism from V-01 (Phase 8 SEAL: per-field CHECK/HOW blocks with independent sources) combined with C-33 mechanism from V-02 (PRE-EXECUTION CONTRACT: three-column table adding "Verified in" column). Independent structural locations. All other phases identical to R12-V-05.

**Hypothesis:** Zero-interference test. V-01 and V-02 are structurally independent -- V-01 modifies Phase 8 SEAL only; V-02 modifies the pre-execution design section only. Combined they should achieve both C-32 and C-33 without regression on any prior-passing criterion.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL -- a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

The following structural guarantees must hold across all phases. Read before executing Phase 1. Each row names a mechanism, states what is enforced, and identifies where enforcement is verified.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in |
|-----------|------------------------------------------------|-------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected locked in Phase 1 SEAL; Phases 2-9 must not modify them | Phase 1 SEAL items 1-5 (Echo / Nearest signal / Commit relevance / Pattern / Why unexpected) |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete | Phase 2 SEAL items 1-5 |
| Accuracy ratio | Phase 4: both weighted formula score ({N}/100) and count-based ratio ({N}/{M} = {X}%) required; both are named SEAL fields | Phase 4 SEAL item 5 (Count-based ratio) |
| Verdict sentence | Phase 6: both score formats copied from Phase 4; exact sentence format enforced; tier label checked against stated score | Phase 6 SEAL items 1-4 |
| Gap columns | Phase 7: Column A = prior belief ("We assumed X"), Column B = discovery missed; structurally isolated; same content in both = incomplete | Phase 7 SEAL items 3-5 (Column A / Column B / Column A != Column B) |
| Recommendation slots | Phase 7: three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive to output | Phase 7 SEAL item 8 (Recommendation slot check) |
| Copy guard -- body | Phase 8: body instruction "COPY from Phase 6 verdict sentence. Do not recompute." Cell format string includes COPY-VERIFIED label and source | Phase 8 table cell format string |
| Copy guard -- SEAL | Phase 8 SEAL: three named fields each with independent CHECK/HOW blocks -- This score (cell value, no other phase read), COPY-VERIFIED (Phase 6 comparison only, not Phase 4), COPY-SOURCE (cell label names Phase 6) | Phase 8 SEAL: This score item / COPY-VERIFIED item / COPY-SOURCE item |
| Seal format contracts | All 9 phase seals carry explicit format-string specifications per field -- verify value form, not just presence | All 9 phase SEAL blocks |
| AMEND scope | When set: every phase table carries scope marker; Phase 2 includes OOS secondary table for excluded artifacts | Phase 2 SEAL item 6 (OOS table) when AMEND set |

---

PHASE 1 -- ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

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
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted -- what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo -- all post-ship outcomes were within signal bounds" -- not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" -- not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {description of failure class, not the Echo instance}" -- not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} -- must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

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

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic -- missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "--" -- not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required -- non-blank statement] | [required -- non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND -- no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND columns: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied -- format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" -- both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row -- same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A -- "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B -- "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

Improvement recommendation -- three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings -- their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern addressed] by [slot:practice-change -- name the specific practice change, not generic] so that [slot:measurable-outcome -- state what would be observably different if this practice change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement -- no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent -- NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} -- different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row -- same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} -- an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row -- no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" -- all three tokens replaced with specific content
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
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" -- not blank, not "N/A"
    Delta: {+N or -N or 0} OR "--" when no prior retro
    Trend: one of exactly: up improving | down degrading | = stable OR the "first retro" statement

  [ ] This score -- independent verification:
    CHECK: The Phase 8 calibration table "This score" cell contains a value.
    HOW: Read the "This score" cell in the Phase 8 calibration table above. Confirm it is non-blank and in {number}/100 format. Do not read Phase 6 or Phase 4 to verify this item -- this check is about the cell itself only.
    Format required: {number}/100 -- blank or wrong format = FAIL this item.

  [ ] COPY-VERIFIED -- independent verification:
    CHECK: The score in the "This score" cell was copied from Phase 6, not computed.
    HOW: Open Phase 6. Read the verdict sentence. Find the score number (the value before "/100" in that sentence). Compare to the "This score" cell value. If they match AND the cell label contains "COPY-VERIFIED", this item passes. Do not read Phase 4 to perform this check -- the comparison is between Phase 8 cell and Phase 6 verdict sentence only.
    Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL this item regardless of whether the number matches.

  [ ] COPY-SOURCE -- independent verification:
    CHECK: The "This score" cell names Phase 6 verdict as the copy source, not Phase 4.
    HOW: Read the "This score" cell label. Confirm it names "Phase 6 verdict" or equivalent. A label naming Phase 4, a label absent, or a label that says "computed" = FAIL this item. Arriving at the same number via Phase 4 does not satisfy this check -- the source is the label in the cell, not the value's mathematical origin.
    Format required: cell label contains "source: Phase 6 verdict" -- alternative source or blank label = FAIL this item.

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern name from Phase 1 -- same taxonomy label, not a synonym] | [one specific practice change -- not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- Phase 1: Echo locked. Pattern and Why-unexpected required. Locked before signal comparison.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio -- both required, both named SEAL fields.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot `[slot:X]` recommendation; no `[slot:` strings in output.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three independent fields each with CHECK/HOW blocks (see PRE-EXECUTION CONTRACT "Copy guard -- SEAL" row).
- All 9 seals: explicit format-string per field (not just field names).
- AMEND: scope marker on every table; Phase 2 OOS secondary table.
```

---

## V-05 -- Full Integration: C-32 + C-33 + Cross-Linking + Extended Per-Field Instructions

**Axes:** All of V-04 (C-32 CHECK/HOW blocks + C-33 three-column table), plus:

1. **Cross-linking:** Each Phase 8 SEAL item's CHECK/HOW block cites its PRE-EXECUTION CONTRACT row. Each PRE-EXECUTION CONTRACT row's "Verified in" cell names its corresponding Phase 8 SEAL item. Bidirectional: table -> SEAL and SEAL -> table.

2. **Extended per-field CHECK/HOW to Phase 1 and Phase 7 SEALs:** Phase 1 Echo item and Phase 7 recommendation slot check item receive the same CHECK/HOW treatment as Phase 8. Tests whether per-field independence improves scoring on C-19/C-21/C-27 in addition to C-32.

3. **Trailing DESIGN GUARANTEES table:** Split "Copy guard -- SEAL" into three independent rows (one per field), creating a 12-row table. Both PRE-EXECUTION CONTRACT (pre-Phase-1) and DESIGN GUARANTEES (post-Phase-9) present, with the latter providing expanded per-field granularity.

**Hypothesis:** V-04 achieves C-32 and C-33 at minimum complexity. V-05 tests whether bidirectional cross-linking and scope extension produce ceiling-level scoring without regression. A scorer auditing C-32 finds independent verification instructions in the SEAL AND can navigate to the contract row for each. A scorer auditing C-33 finds mechanism-keyed rows in two tables, each navigable to its enforcement point.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL -- a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

The following structural guarantees must hold across all phases. Read before executing Phase 1. Each row names a mechanism, states what is enforced, and identifies the exact SEAL field where enforcement is verified.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in |
|-----------|------------------------------------------------|-------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected locked in Phase 1 SEAL; Phases 2-9 must not modify them | Phase 1 SEAL: Echo item (CHECK/HOW block) |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete | Phase 2 SEAL items 1-5 |
| Accuracy ratio | Phase 4: both weighted formula score ({N}/100) and count-based ratio ({N}/{M} = {X}%) required; both are named SEAL fields | Phase 4 SEAL item 5 (Count-based ratio) |
| Verdict sentence | Phase 6: both score formats copied from Phase 4; exact sentence format enforced; tier label checked against stated score | Phase 6 SEAL items 1-4 |
| Gap columns | Phase 7: Column A = prior belief ("We assumed X"), Column B = discovery missed; structurally isolated; same content in both = incomplete | Phase 7 SEAL items 3-5 (Column A / Column B / Column A != Column B) |
| Recommendation slots | Phase 7: three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive; CHECK/HOW block enforces token absence | Phase 7 SEAL: Recommendation slot check item (CHECK/HOW block) |
| Copy guard -- body | Phase 8: body instruction "COPY from Phase 6 verdict sentence. Do not recompute." Cell format string includes COPY-VERIFIED label and source | Phase 8 table cell format string |
| Copy guard -- This score | Phase 8 SEAL: This score field -- CHECK: cell value present in {number}/100 form; HOW: read Phase 8 cell only; no other phase consulted | Phase 8 SEAL: This score item (CHECK/HOW -- reads Phase 8 cell only) |
| Copy guard -- COPY-VERIFIED | Phase 8 SEAL: COPY-VERIFIED field -- CHECK: copy operation confirmed; HOW: compare Phase 8 cell to Phase 6 verdict sentence directly; Phase 4 not consulted | Phase 8 SEAL: COPY-VERIFIED item (CHECK/HOW -- reads Phase 6 verdict sentence only) |
| Copy guard -- COPY-SOURCE | Phase 8 SEAL: COPY-SOURCE field -- CHECK: cell label names Phase 6 verdict; HOW: read Phase 8 cell label only; source = label content, not numeric origin | Phase 8 SEAL: COPY-SOURCE item (CHECK/HOW -- reads Phase 8 cell label only) |
| Seal format contracts | All 9 phase seals carry explicit format-string specifications per field -- verify value form, not just presence | All 9 phase SEAL blocks |
| AMEND scope | When set: every phase table carries scope marker; Phase 2 includes OOS secondary table for excluded artifacts | Phase 2 SEAL item 6 (OOS table) when AMEND set |

---

PHASE 1 -- ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

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
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted -- what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo -- independent verification:
    CHECK: The Echo table cell contains a post-ship finding or the exact no-Echo string.
    HOW: Read the Echo table cell directly. Confirm it is not blank and is not a restatement of a wrong prediction. Valid values: one sentence describing a post-ship finding, or the exact string "No Echo -- all post-ship outcomes were within signal bounds." Do not read any other phase to verify this item.
    Format required: {one sentence} or "No Echo -- all post-ship outcomes were within signal bounds" -- blank or restatement of wrong prediction = FAIL.
    Cross-reference: PRE-EXECUTION CONTRACT "Echo lock" row.
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" -- not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {description of failure class, not the Echo instance}" -- not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} -- must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

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

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic -- missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "--" -- not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required -- non-blank statement] | [required -- non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND -- no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND columns: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied -- format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" -- both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row -- same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A -- "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B -- "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

Improvement recommendation -- three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings -- their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern addressed] by [slot:practice-change -- name the specific practice change, not generic] so that [slot:measurable-outcome -- state what would be observably different if this practice change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement -- no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent -- NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} -- different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row -- same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} -- an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row -- no other values
  [ ] Recommendation slot check -- independent verification:
    CHECK: The recommendation output contains no `[slot:` strings -- all three tokens replaced with specific content.
    HOW: Read the recommendation line in the Phase 7 output. Search for the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", and "[slot:measurable-outcome]". If any appear, this item fails. Do not evaluate content quality -- evaluate only whether the token strings are absent.
    Format required: recommendation line contains none of "[slot:gap-or-echo]" | "[slot:practice-change]" | "[slot:measurable-outcome]" -- any `[slot:` string present = FAIL.
    Cross-reference: PRE-EXECUTION CONTRACT "Recommendation slots" row.
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
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" -- not blank, not "N/A"
    Delta: {+N or -N or 0} OR "--" when no prior retro
    Trend: one of exactly: up improving | down degrading | = stable OR the "first retro" statement

  [ ] This score -- independent verification:
    CHECK: The Phase 8 calibration table "This score" cell contains a value.
    HOW: Read the "This score" cell in the Phase 8 calibration table above. Confirm it is non-blank and in {number}/100 format. Do not read Phase 6 or Phase 4 to verify this item -- this check is about the cell itself only.
    Format required: {number}/100 -- blank or wrong format = FAIL this item.
    Cross-reference: PRE-EXECUTION CONTRACT "Copy guard -- This score" row.

  [ ] COPY-VERIFIED -- independent verification:
    CHECK: The score in the "This score" cell was copied from Phase 6, not computed.
    HOW: Open Phase 6. Read the verdict sentence. Find the score number (the value before "/100" in that sentence). Compare to the "This score" cell value. If they match AND the cell label contains "COPY-VERIFIED", this item passes. Do not read Phase 4 to perform this check -- the comparison is between Phase 8 cell and Phase 6 verdict sentence only.
    Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL this item regardless of whether the number matches.
    Cross-reference: PRE-EXECUTION CONTRACT "Copy guard -- COPY-VERIFIED" row.

  [ ] COPY-SOURCE -- independent verification:
    CHECK: The "This score" cell names Phase 6 verdict as the copy source, not Phase 4.
    HOW: Read the "This score" cell label. Confirm it names "Phase 6 verdict" or equivalent. A label naming Phase 4, a label absent, or a label that says "computed" = FAIL this item. Arriving at the same number via Phase 4 does not satisfy this check -- the source is the label in the cell, not the value's mathematical origin.
    Format required: cell label contains "source: Phase 6 verdict" -- alternative source or blank label = FAIL this item.
    Cross-reference: PRE-EXECUTION CONTRACT "Copy guard -- COPY-SOURCE" row.

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern name from Phase 1 -- same taxonomy label, not a synonym] | [one specific practice change -- not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

## DESIGN GUARANTEES

Each row names a mechanism and states the structural decision that enforces it. The "Verified in" column names the exact SEAL item a reviewer can read to confirm the guarantee without tracing phases. Copy guard rows are split per field -- each is independently auditable.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in |
|-----------|------------------------------------------------|-------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected locked in Phase 1 SEAL before signal data is read; Phases 2-9 must not modify them | Phase 1 SEAL: Echo item (CHECK/HOW block) |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete | Phase 2 SEAL items 1-5 |
| Accuracy ratio | Phase 4 requires both weighted formula score ({N}/100) AND count-based ratio ({N}/{M} = {X}%); both are named format-string fields in Phase 4 SEAL | Phase 4 SEAL item 5 (Count-based ratio format: "{N}/{M} = {X}%") |
| Verdict sentence | Phase 6 draws both score formats from Phase 4 (no recalculation); exact sentence format enforced; tier label checked against stated score | Phase 6 SEAL items 1-4 |
| Gap columns | Phase 7: Column A = prior belief ("We assumed X"), Column B = discovery missed; must contain different statements; merged rows = incomplete | Phase 7 SEAL items 3-5 (Column A / Column B / Column A != Column B) |
| Recommendation slots | Three `[slot:X]` tokens in Phase 7 recommendation template; Phase 7 SEAL slot-check item carries independent CHECK/HOW block confirming no `[slot:` strings survive | Phase 7 SEAL: Recommendation slot check item (CHECK/HOW block) |
| Copy guard -- body | Phase 8 body: "COPY from Phase 6 verdict sentence. Do not recompute." Table cell template carries inline format string including COPY-VERIFIED label and source | Phase 8 table cell format string |
| Copy guard -- This score | Phase 8 SEAL This score item: CHECK: cell value in {number}/100 form; HOW: read Phase 8 cell only -- Phase 6 and Phase 4 not consulted for this item | Phase 8 SEAL: This score item |
| Copy guard -- COPY-VERIFIED | Phase 8 SEAL COPY-VERIFIED item: CHECK: copy operation confirmed; HOW: compare Phase 8 cell to Phase 6 verdict sentence -- Phase 4 not consulted | Phase 8 SEAL: COPY-VERIFIED item |
| Copy guard -- COPY-SOURCE | Phase 8 SEAL COPY-SOURCE item: CHECK: cell label names "Phase 6 verdict"; HOW: read Phase 8 cell label only -- source = label, not numeric origin | Phase 8 SEAL: COPY-SOURCE item |
| Seal format contracts | All 9 phase seals carry explicit format-string specifications per field -- not just field names | All 9 phase SEAL blocks |
| AMEND scope | When set: every phase table carries "[AMEND: {scope} only]" marker; Phase 2 includes dedicated OOS secondary table for excluded artifacts | Phase 2 SEAL item 6 (OOS table) when AMEND set |
```
