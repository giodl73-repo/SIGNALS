Golden prompt written to `simulations/quest/golden/topic-retro-golden-2026-03-17.md`.

**Summary:**
- **Winning variation:** V-05 (Full Integration: Mutual Enforcement via Cross-Binding)
- **Score:** 164/164 (100.0%) under rubric v18
- **Rubric carried forward:** v19 (C-48 and C-49 discovered from V-05's structural excess over V-04)

**5 patterns that made it golden:**
1. **Standalone authority block** — `**Canonical downstream table set**` promoted from inline enumeration to a first-class named declaration block in the preamble (C-47 PASS)
2. **FORWARD VERIFIED names the block, not inline names** — eliminates the redundant second copy of canonical names; authority block is the sole source (C-46 + C-48)
3. **Assignment rules cite the authority block by name** — closes the triangle: SEAL item + FORWARD VERIFIED + assignment rules all reference the same named block (C-48)
4. **SEAL item 8 embeds failure conditions inline** — "generic preamble reference = FAIL this item" makes the output self-documenting; no rubric consultation needed (C-49)
5. **Design guarantees footer documents mutual enforcement** — the closed-loop architecture (C-47 registry + C-46 SEAL + FORWARD VERIFIED) is visible in the skill output, not just in the rubric
y diverge from the authority block. V-05 replaces the inline enumeration with: "exact canonical identifiers declared in the `**Canonical downstream table set**` authority block in the ASSESSOR NAVIGATION PREAMBLE." One source of truth; no redundant copy.

**3. Derived Views assignment rules cite the authority block by name (C-48)**
The assignment rules block ends: "canonical identifiers from the `**Canonical downstream table set**` authority block in the ASSESSOR NAVIGATION PREAMBLE -- use no other names." This closes the third leg of the triangle: SEAL item, FORWARD VERIFIED, and assignment rules all name the same block. Renaming a downstream table now requires one edit in one place; the SEAL catches any drift.

**4. SEAL item 8 embeds failure conditions inline (C-49)**
V-04's SEAL cross-reference item named the authority block but stated no failure modes. V-05's SEAL item 8 embeds its own disqualifying forms: "Generic preamble reference... inline enumeration, or absent cross-check item = FAIL this item. Verifying against an inline list rather than the named authority block = FAIL this item." Assessors determine pass/fail without consulting the rubric.

**5. Design guarantees footer documents mutual enforcement explicitly**
V-05 adds mutual enforcement documentation: "C-47 registry + C-46 SEAL + FORWARD VERIFIED all reference the same named authority block; drift caught at SEAL time via item 8, not discovered during audit." This makes the closed-loop architecture visible in the skill output itself, not just in the rubric.

---

## Final Rubric Criteria Summary (v19)

| Criterion | Weight | Category | Status |
|-----------|--------|----------|--------|
| C-01 through C-08 | Essential + Recommended (90 pts) | Various | PASS (carried forward) |
| C-09 through C-43 | Aspirational (70 pts) | Various | PASS (carried forward) |
| C-44 -- SEAL-Enforced Bidirectional Navigation Completeness | 2 pts | correctness | PASS |
| C-45 -- Assessor Navigation Preamble (Three-Entry-Point Declaration) | 2 pts | format | PASS |
| C-46 -- SEAL-Preamble Cross-Reference Integrity Check | 2 pts | correctness | PASS |
| C-47 -- Preamble as Canonical Name Registry (Downstream Table Authority) | 2 pts | format | PASS |
| C-48 -- Registry-Anchor Cross-Binding (All Dependents Name the Registry) | 2 pts | correctness | v19 new |
| C-49 -- Embedded Failure Conditions in SEAL Items | 2 pts | correctness | v19 new |

---

## Prompt Body

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute
phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every
item specifies the required field and its required value form. Do not proceed past a phase until
every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every
table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system is navigable from three entry points. Locate the row matching your starting
position and follow the navigation field.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of the table below) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of Phase 0 table) | The exact downstream table(s) per the **Canonical downstream table set** below |
| 3 | Any downstream section header (Phase 2, 3, 4, 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as source for that section |

**Canonical downstream table set** (authority block -- sole canonical source for all Derived Views entries, FORWARD VERIFIED references, and SEAL cross-checks):

All Derived Views entries in the AUDIT MANIFEST, all FORWARD VERIFIED declarations, and all
Phase 0 SEAL cross-check items must use the exact canonical identifiers in this table. This
block is the single source of truth. Do not re-enumerate canonical names inline elsewhere in
this document -- reference this block by name instead. Any drift between this block and inline
enumerations is an integrity failure detectable at SEAL time.

| Canonical table name | Phase | Populated from |
|---------------------|-------|----------------|
| Phase 2 Signal Coverage Table | 2 | Every manifest row (grouped by Namespace) |
| Phase 3 Predicted vs Actual Table | 3 | Rows with Status = COVERED and non-ND Verdict |
| Phase 4 Namespace Accuracy Table | 4 | Scored manifest rows (Verdict != ND) |
| Phase 4 Reconciliation Table | 4 | All manifest rows (ND rows appear; excluded from denominator) |
| Phase 7 Gap Analysis Table | 7 | Rows with Verdict = W or P; material EMPTY namespaces |

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|--------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. Derived Views column (wired to Canonical downstream table set) enables forward navigation; [DERIVED FROM] headers enable backward navigation. | Phase 0 SEAL items 3-8; [DERIVED FROM] headers in all downstream sections | (all columns) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict. No recomputation at any stage. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL each with independent CHECK:/HOW: blocks. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All
downstream tables are derived from this manifest. The `Derived Views` column enables forward
navigation: an assessor at any manifest row can identify which downstream tables include it
without reading phase specifications.

Use ONLY the exact canonical identifiers declared in the **Canonical downstream table set**
authority block in the ASSESSOR NAVIGATION PREAMBLE. Do not use abbreviations, aliases, or
informal labels. Do not re-enumerate canonical names inline -- reference the authority block.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual
outcome, verdict, and forward-navigation destinations using canonical table names.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Derived Views assignment rules (canonical identifiers from the **Canonical downstream table set**
authority block in the ASSESSOR NAVIGATION PREAMBLE -- use no other names):
- Every row -> "Phase 2 Signal Coverage Table"
- Non-ND rows -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- W or P rows -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table"

After completing the manifest, write the bidirectional navigation verification block:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views
  column uses the exact canonical identifiers declared in the **Canonical downstream table set**
  authority block in the ASSESSOR NAVIGATION PREAMBLE. An assessor reading any manifest row can
  navigate forward to downstream sections without reading phase specifications.
  Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each downstream section in the
  **Canonical downstream table set** -- Phase 2 Signal Coverage Table, Phase 3 Predicted vs
  Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap
  Analysis Table -- carries a [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming
  this manifest as its source. An assessor reading any downstream section can navigate backward
  to the manifest. Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header;
      not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, scope carried into all phases
  [ ] Manifest rows: one row per signal artifact found; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each Derived Views entry in the manifest uses an exact
      canonical identifier from the **Canonical downstream table set** authority block in the
      ASSESSOR NAVIGATION PREAMBLE. Verify by checking each entry against that block directly --
      do not verify against an inline list or the FORWARD VERIFIED enumeration.
      Non-canonical alias or informal label = FAIL this item.
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present after
      manifest table; explicitly declares manifest -> downstream direction as confirmed AND names
      the **Canonical downstream table set** authority block as the source of canonical identifiers;
      intent description without verification assertion = FAIL; inline enumeration without
      authority block reference = FAIL
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present after
      manifest table; explicitly declares downstream -> manifest direction as confirmed;
      future-tense statement without verification assertion = FAIL this item
  [ ] SEAL-Preamble authority block cross-reference: Derived Views entries in the manifest are
      cross-checked against the **Canonical downstream table set** authority block declared in the
      ASSESSOR NAVIGATION PREAMBLE. The cross-check must name that authority block explicitly by
      its title -- "**Canonical downstream table set**". Generic preamble reference ("the preamble
      says...", "per the navigation section"), inline enumeration, or absent cross-check item =
      FAIL this item. Verifying against an inline list rather than the named authority block =
      FAIL this item.
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo
candidacy]{{/if}}

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
  > **Pattern**: [name from taxonomy or "other: [your name]"] -- [recurring failure mode class -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap |
  scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR exact string "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR exact string "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description -- not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted -- names what was expected, not just that it was unexpected}"
  {{#if amend}}[ ] AMEND scope marker present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row. Derive
from Phase 0 AUDIT MANIFEST -- do not re-examine artifacts independently.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to the OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|---------------------------|---------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| draft     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| review    | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| flow      | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| trace     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| prove     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| listen    | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| program   | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| topic     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| TOTAL     |                 | N              |                           |                           |

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or "--" -- not blank
  [ ] TOTAL row: present with {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

For each namespace with Status = COVERED in Phase 2. Derive from AUDIT MANIFEST rows -- do
not independently re-evaluate predictions.

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter COVERED namespaces]" present above table
  {{#if amend}}[ ] Scope marker present above table{{/if}}
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

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Manifest row 1, count each scored verdict sequentially | [+1 C, +1 W, etc.] | {N} | {C} | -- |
| Backward | W={W}; +P={P}; +C={C}; total={N} | [recovery arithmetic shown] | {N} | C=total-W-P={C} | YES / NO |

Reconciliation result: Forward={N}; Backward={N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals"
  [ ] TOTAL row: present, format: {number}/100
  [ ] Count-based ratio: stated in format "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with Forward and Backward rows and result row
  [ ] Reconciliation result: Match = YES before proceeding -- NO = do not continue
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values...]" present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo
should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding creating tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (Source/Analysis/Resolution non-blank) OR exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based statement.
Do not recalculate either number.

"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: drawn from Phase 4 TOTAL row -- same number, not recalculated
  [ ] Count ratio: drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if >= 75 | ADEQUATE if 50-74 | WEAK if < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add EMPTY namespaces where absence is material]

For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence
is material to the commit decision.

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

Column A = "Assumption held without evidence": the inertia belief that made this gap invisible
before commit. WHY the gap existed. Framed as prior belief ("We assumed X"), not an outcome.
Column B = "Would have surfaced": the discovery missed. WHAT was missed. Different from Column A.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [/exact-skill-name] | [discovery -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

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
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not
recompute. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} OR "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read "This score" cell in Phase 8 table only. Do not read Phase 6 or Phase 4.
      Format required: {number}/100 -- blank or wrong format = FAIL.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6. Read verdict sentence. Find score before "/100". Compare to "This score"
      value. "COPY-VERIFIED" label must be present. Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL.

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm it names "Phase 6 verdict". Phase 4 reference or absent = FAIL.
      Format required: label contains "source: Phase 6 verdict" -- alternative source = FAIL.

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern taxonomy label -- verbatim] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- character-for-character match
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- exact match, not synonym
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance
against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- PRE-EXECUTION CONTRACT: ASSESSOR NAVIGATION PREAMBLE with three-row navigation table (entry
  points 1/2/3). Entry point 2 references the **Canonical downstream table set** authority block
  by name. Standalone **Canonical downstream table set** authority block (5 rows, exact canonical
  identifiers, labeled as sole canonical source for Derived Views, FORWARD VERIFIED, and SEAL
  cross-checks). Four-column mechanism table follows (Mechanism / Guarantee / Verified in /
  Manifest column).
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict, Derived Views per row. Derived
  Views assignment rules reference the **Canonical downstream table set** authority block by
  name -- no inline re-enumeration. FORWARD VERIFIED declaration names the **Canonical downstream
  table set** authority block as the source of canonical identifiers. BACKWARD VERIFIED
  declaration. SEAL item 8 (SEAL-Preamble authority block cross-reference) explicitly names the
  **Canonical downstream table set** block -- generic preamble reference or inline enumeration
  = FAIL. All downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK:/HOW: blocks.
- All 9 seals: explicit format-string per field.
- C-47 PASS: standalone **Canonical downstream table set** authority block in preamble below
  three-entry-point table; not entry-point prose; not inline enumeration.
- C-46 PASS: Phase 0 SEAL item 8 cross-checks Derived Views against the **Canonical downstream
  table set** authority block by name; wired to C-47 block; non-applicable if C-47 block absent.
- Mutual enforcement: C-47 registry + C-46 SEAL + FORWARD VERIFIED all reference the same named
  authority block; drift caught at SEAL time via item 8, not discovered during audit.
```
