Written to `simulations/quest/rubrics/signal-rubric-v11-2026-03-17.md`.

---

**Two new criteria from R10:**

| ID | Axis | Source | What it closes |
|----|------|--------|---------------|
| **C-34** | P — FULL gate format check | R10 V-05 COMPLIANCE GATE -- FULL, Check 4 | FULL gate had no format check; C-29 covered FILTER (R8), C-18 Ch1 covered BARE (R4). C-34 adds it as Check 4 to FULL gate. All three gates now have format checks. |
| **C-35** | Q — BARE gate order check | R10 V-05 COMPLIANCE GATE -- BARE, Check 3 | BARE gate had no order check; C-28/C-33 covered FULL (R8/R9), C-21 gave instructions only. C-35 adds an active gate check with restart. FULL + BARE now both have order checks; FILTER is N/A (single namespace). |

**Formula:** denominator 25 → 27. Each criterion = 1/27 × 10 = +0.37.

**Structural theme:** *close the mode symmetry gaps* — R8 added gates to all three modes, R9 elevated specification depth of existing checks, R10 completes the gate-check type coverage matrix.

**R10 retroactive under v11:** V-05 = 100.00, V-04 = 99.63, V-01/V-02/V-03 = 99.26. R11 isolates P and Q axes (V-01=P only, V-02=Q only, V-03=P+Q) to confirm each contributes exactly +0.37 independently.
* -- R8 added compliance gates to all
three modes (C-25 for FULL, C-20 for FILTER, C-14/C-18 for BARE); R9 elevated the
specification-depth of existing gate checks (C-31 labeled counts, C-32 named DNT, C-33 full
order enumeration). R10 identifies that gate checks are not symmetric across modes: BARE and
FILTER gates have format checks but FULL gate does not; FULL gate has an order check but BARE
gate does not. C-34 and C-35 complete the gate-check coverage matrix. Every check type that
applies to a mode is now present in that mode's gate.

**Retroactive R10 leaderboard under v11:** all five R10 variations carry C-34 and C-35
(inherited from R9 V-05 baseline, not varied in R10). R10 saturates v11 at 100.00 for V-05.
R11 must run single-axis isolation (V-01=P, V-02=Q, V-03=P+Q) to confirm independence and
verify each contributes +0.37.

| V | C-34 | C-35 | C-31 | C-32 | C-33 | Asp (27) | Composite |
|---|------|------|------|------|------|----------|-----------|
| **V-05** | PASS | PASS | PASS | PASS | PASS | 27/27 → 10    | **100.00** |
| **V-04** | PASS | PASS | PASS | PASS | FAIL | 26/27 → 9.63  | **99.63**  |
| **V-01** | PASS | PASS | PASS | FAIL | FAIL | 25/27 → 9.26  | **99.26**  |
| **V-02** | PASS | PASS | FAIL | PASS | FAIL | 25/27 → 9.26  | **99.26**  |
| **V-03** | PASS | PASS | FAIL | FAIL | PASS | 25/27 → 9.26  | **99.26**  |

---

## Criterion Index

| ID | Weight | Category | Description |
|----|--------|----------|-------------|
| C-01 | essential | correctness | All 12 namespaces present |
| C-02 | essential | format      | Namespace headers present with purpose phrase |
| C-03 | essential | coverage    | Every sub-skill listed under its namespace |
| C-04 | essential | behavior    | `--bare` mode produces command names only |
| C-05 | essential | behavior    | `<namespace>` filter scopes output correctly |
| C-06 | recommended | correctness | Sub-skill count per namespace accurate |
| C-07 | recommended | format      | Each namespace includes a dispatch footer |
| C-08 | recommended | coverage    | Namespace headers state the namespace purpose |
| C-09 | aspirational | correctness | Sub-skill descriptions match canonical one-liners |
| C-10 | aspirational | format      | Output is scannable without overwhelming |
| C-11 | aspirational | format      | Each footer uses a namespace-specific domain noun |
| C-12 | aspirational | format      | `->` separator is column-aligned within each namespace section |
| C-13 | aspirational | correctness | Inline reference format matches the specified output format |
| C-14 | aspirational | behavior    | Bare/filter modes include a pre-emit compliance gate |
| C-15 | aspirational | format      | Alignment rule provides a precomputed width lookup table |
| C-16 | aspirational | format      | Width table includes a per-row example-pad derivation |
| C-17 | aspirational | structure   | NAMESPACE CATALOG precedes all behavioral rules |
| C-18 | aspirational | behavior    | Bare-mode compliance gate includes 61-line count with per-namespace breakdown |
| C-19 | aspirational | behavior    | PARSE MODE enumerates all 12 canonical namespace names |
| C-20 | aspirational | behavior    | Filter-mode compliance gate includes per-namespace count check |
| C-21 | aspirational | behavior    | BARE MODE states explicit first and last namespace output anchors |
| C-22 | aspirational | structure   | NAMESPACE CATALOG section is an active transcription commitment gate |
| C-23 | aspirational | structure   | NAMESPACE CATALOG section is labeled as the literal output |
| C-24 | aspirational | behavior    | All three output modes include explicit pre-emission completeness verification |
| C-25 | aspirational | behavior    | FULL MODE includes a compliance restart gate (namespace-presence + count) |
| C-26 | aspirational | structure   | Transcription gate requires counted entry acknowledgment |
| C-27 | aspirational | behavior    | SECTION FORMAT includes a per-section sub-skill count self-check |
| C-28 | aspirational | behavior    | FULL MODE compliance gate includes canonical namespace emit-order check |
| C-29 | aspirational | behavior    | FILTER MODE compliance gate includes section-format verification |
| C-30 | aspirational | behavior    | BARE MODE includes explicit slash-strip worked examples |
| C-31 | aspirational | behavior    | Count formula uses labeled namespace breakdown in transcription gate and BARE gate |
| C-32 | aspirational | structure   | Domain nouns defined in a named formal DOMAIN NOUN TABLE in the prompt |
| C-33 | aspirational | behavior    | FULL gate Check 3 enumerates all 12 canonical namespaces in sequence |
| C-34 | aspirational | behavior    | FULL MODE compliance gate includes section-format verification |
| C-35 | aspirational | behavior    | BARE MODE compliance gate includes canonical namespace emit-order check |

---

## Scoring Formula

```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 27 x 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (0.37 pts each; 1/27 x 10 = 0.370)
- PARTIAL on a recommended criterion = 0.5 criterion credit

**Golden threshold**: all 5 essential PASS **and** composite >= 80

---

## Essential Criteria

*Must pass all five. Combined weight = 60 pts.*

### C-01 -- All 12 namespaces present
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Output includes sections for all 12 canonical namespaces:
  `scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic`,
  `quest`, `mock`, `org`. Fails if any namespace is absent or misspelled.

### C-02 -- Namespace headers present with purpose phrase
- **Category**: format
- **Weight**: essential
- **Pass condition**: Each namespace appears as a distinct header in the output. Header
  includes at minimum the namespace name. A bare namespace name without any sub-skill
  listing below it fails. Fails if any namespace has no header.

### C-03 -- Every sub-skill listed under its namespace
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Under each namespace header, every canonical sub-skill for that
  namespace is listed. In full-index and filtered modes, each sub-skill must appear with
  at least a name. Bare mode exempt from description requirement. Fails if any sub-skill
  is missing from its namespace section.

### C-04 -- `--bare` mode produces command names only
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal --bare`, output contains only bare command
  names (e.g. `scout-competitors`) with no descriptions, no namespace headers, and no
  prose. One command per line. If `--bare` is not handled and the full index is emitted
  instead, fails.

### C-05 -- `<namespace>` filter scopes output correctly
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal <namespace>` (e.g. `/signal flow`), output
  shows only the skills in that namespace. Skills from other namespaces must not appear.
  If no filtering occurs and the full index is returned, fails.

---

## Recommended Criteria

*Output is meaningfully better with these. Combined weight = 30 pts.*

### C-06 -- Sub-skill count per namespace is accurate
- **Category**: correctness
- **Weight**: recommended
- **Pass condition**: The skill count stated in each namespace header matches the actual
  number of sub-skills listed. Authoritative counts: scout=8, draft=4, review=4, flow=7,
  trace=7, prove=9, listen=3, program=2, topic=6, quest=4, mock=3, org=4. Off-by-one or
  missing count annotation is a soft fail.

### C-07 -- Each namespace includes a dispatch footer
- **Category**: format
- **Weight**: recommended
- **Pass condition**: Each namespace section ends with a "Run any sub-skill directly, or
  describe your [X] and the most relevant skill will run" guidance line. This signals the
  namespace is entry-point friendly. Missing footers in 3+ namespaces fails.

### C-08 -- Namespace headers state the namespace purpose
- **Category**: coverage
- **Weight**: recommended
- **Pass condition**: Each namespace header includes a brief purpose phrase (e.g. "Scout
  namespace -- 8 skills for discovery and research"). A bare namespace name with no
  context phrase fails. At least 8 of 12 namespaces must have annotated headers to pass.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable. Combined weight = 10 pts.*

### C-09 -- Sub-skill descriptions match canonical one-liners
- **Category**: correctness
- **Weight**: aspirational
- **Pass condition**: Sub-skill descriptions match (or are semantically equivalent to)
  the authoritative one-liners in `output/T1/CLAUDE.md`. Minor paraphrase is acceptable;
  omitting a key distinguishing detail (e.g. "inertia as primary competitor" for
  scout-competitors) is a soft fail. At least 80% of sub-skills must match to pass.

### C-10 -- Output is scannable without overwhelming
- **Category**: format
- **Weight**: aspirational
- **Pass condition**: Full-index output uses consistent visual alignment (e.g. `->`
  separator, consistent indentation). Namespace sections are visually separated. No
  sub-skill description wraps to create orphan lines that break the scan rhythm. A human
  can locate any skill within 10 seconds of scanning.

### C-11 -- Each footer uses a namespace-specific domain noun
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 1 excellence signal. V-04 scored full on C-07; V-03 scored partial
  because footers used a generic placeholder that the model had to infer.
- **Pass condition**: Each dispatch footer substitutes the generic slot with a noun
  specific to that namespace (e.g. "research goal" for scout, "draft artifact" for draft,
  "flow scenario" for flow). A footer retaining a literal placeholder token fails. Footers
  using the same noun across all 12 namespaces are also a soft fail. At least 10 of 12
  namespaces must have distinct, namespace-appropriate nouns to pass.

### C-12 -- `->` separator is column-aligned within each namespace section
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 1 excellence signal. V-04 scored full on C-10 due to an explicit
  alignment instruction; other variations lacked it and produced ragged output.
- **Pass condition**: Within each namespace section, command names are padded to equal
  width so the `->` column is vertically aligned. Ragged alignment fails. All 12
  namespace sections must maintain column alignment. Applies to full-index output only;
  N/A for `--bare` mode.

### C-13 -- Inline reference format matches the specified output format
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 1 excellence signal. V-01 scored partial on C-10 because the
  prompt's inline reference used `->` while the output spec called for a Markdown table.
- **Pass condition**: The format of the prompt's embedded skill reference section is
  identical to the format specified for output. A format mismatch is a soft fail; any
  observed mixed-format output is an auto fail.

### C-14 -- Bare/filter modes include a pre-emit compliance gate
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 2 excellence signal. V-02 scored full on C-04 via an explicit restart
  guard. V-04 stated the rule but omitted a self-check trigger.
- **Pass condition**: The prompt includes an explicit "if [violation condition], restart"
  self-verification instruction for bare mode, filter mode, or both. Both modes gated =
  full pass. Only one mode gated = partial. Rule stated without restart trigger = partial.
  No self-check at all = fail.

### C-15 -- Alignment rule provides a precomputed width lookup table
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 2 excellence signal, pass-condition clarified in Round 3. Algorithm +
  single worked example = partial (V-01, V-03); 12-row precomputed table = full (V-02,
  V-04, V-05). Precomputed table eliminates runtime miscounting: model reads, not counts.
- **Pass condition**: Full pass: prompt includes a precomputed lookup table (one row per
  namespace) with the max command-name width or pad width as a concrete number. Partial
  pass: algorithm stated plus at least one worked numeric example but no table. Fail:
  alignment goal stated without a derivation method, or no alignment instruction. N/A for
  Markdown table format.
- **Note on C-15 / C-12 relationship**: C-12 tests the *output* (is it aligned?). C-15
  tests the *prompt* (does it provide a reliable precomputed method?). A variation can
  pass C-12 and fail C-15.

### C-16 -- Width table includes a per-row example-pad derivation
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 3 excellence signal. V-05 added an "example pad" column to the C-15
  table: each row shows a representative command, its character count, and pad spaces
  required. Model copies a pattern, not arithmetic. V-04 has the table plus a single
  worked example in a separate section -- C-15 pass, C-16 fail.
- **Pass condition**: The alignment width table includes a per-row annotation (dedicated
  column or inline parenthetical) with a representative command name's character count
  and required pad-space count. All 12 rows must carry the annotation. Table with width
  numbers only satisfies C-15, fails C-16. N/A for Markdown table format.
- **Note on C-16 / C-15 relationship**: C-15 tests for precomputed widths. C-16 tests
  whether each row is self-documenting with zero arithmetic at output time.

### C-17 -- NAMESPACE CATALOG precedes all behavioral rules
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 4 excellence signal. R4 V-01 placed NAMESPACE CATALOG before PARSE
  MODE, SECTION FORMAT, and all compliance gates. Data-before-behavior ordering means the
  model processes all 61 sub-skills before encountering any output instruction, reducing
  the risk that behavioral rules overwrite catalog content mid-generation.
- **Pass condition**: NAMESPACE CATALOG (or equivalent data section with all 61
  sub-skills) appears before PARSE MODE, SECTION FORMAT, and all compliance/restart gates
  in the prompt. Fail: PARSE MODE or any compliance gate precedes the catalog. Partial:
  catalog and behavioral rules are interleaved.
- **Note**: Prompt-design criterion. Score from prompt structure; if prompt unavailable,
  mark N/A.

### C-18 -- Bare-mode compliance gate includes 61-line count with per-namespace breakdown
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 4 excellence signal. R4 V-02 upgraded the C-14 restart gate to
  include an exact line count with per-namespace breakdown (8+4+4+7+7+9+3+2+6+4+3+4=61).
  Format-only gates catch structural violations but allow silent skill omission. Count
  gate closes that gap.
- **Pass condition**: Full pass: bare compliance gate includes both (1) format check and
  (2) exact 61-line count with per-namespace breakdown. Partial pass: gate includes
  format check and total-line count but no per-namespace breakdown. C-14 pass only: gate
  has format check with restart trigger but no count. C-14 fail: no gate (auto C-18 fail).
- **Note on C-18 / C-14 relationship**: C-14 tests whether a restart gate exists. C-18
  tests whether the bare gate also verifies completeness via count. Failing C-14
  automatically fails C-18.
- **Note on C-18 / C-31 relationship**: C-18 tests whether the breakdown is present
  (anonymous or labeled form accepted). C-31 tests whether the breakdown uses labeled
  form. A variation can pass C-18 and fail C-31 (breakdown present in anonymous form).

### C-19 -- PARSE MODE enumerates all 12 canonical namespace names
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 4 excellence signal. R4 V-03 listed all 12 canonical names in PARSE
  MODE so unknown-namespace arguments fall back to FULL by explicit rule rather than
  model inference. Standard "anything else -> FULL" is functional but relies on the model
  correctly classifying a near-miss. Explicit enumeration eliminates that inference step.
- **Pass condition**: Full pass: PARSE MODE explicitly enumerates all 12 canonical
  namespace names; unknown argument triggers FULL by explicit fallback. Partial pass:
  PARSE MODE routes unknown to FULL via "anything else" without enumerating names --
  fallback correct but inference-dependent. Fail: no explicit fallback rule for unknown
  namespace arguments.
- **Note on C-19 / C-05 relationship**: C-05 tests behavioral correctness of filter mode
  (output scoped correctly). C-19 tests whether the prompt makes routing deterministic.
  A variation can pass C-05 and fail C-19 (filtering works via correct model inference,
  not explicit specification).

### C-20 -- Filter-mode compliance gate includes per-namespace count check
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 5 excellence signal. R5 V-01 added a second check to the FILTER gate:
  after verifying scope (Check 1: only the requested namespace appears), it verifies count
  (Check 2: the per-namespace breakdown matches the authoritative count for that
  namespace). C-18 established count verification for bare mode; C-20 closes the
  asymmetry by requiring the same rigor for filter mode.
- **Pass condition**: Full pass: filter compliance gate includes both (1) scope check (no
  other namespace appears) and (2) per-namespace count check against authoritative counts
  (scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3, program=2, topic=6,
  quest=4, mock=3, org=4) with restart instruction. Partial pass: gate has scope check
  and restart trigger but no count check. C-14 fail: no gate (auto C-20 fail).
- **Note on C-20 / C-18 relationship**: C-18 tests count verification for bare mode; C-20
  tests it for filter mode. Both must pass for full count-gate coverage across modes.

### C-21 -- BARE MODE states explicit first and last namespace output anchors
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 5 excellence signal. R5 V-02 added "Begin with scout-competitors.
  End with org-committee." to BARE MODE. Without this anchor, the model must infer output
  order from catalog sequence -- a source of drift on long outputs.
- **Pass condition**: Full pass: BARE MODE explicitly names both the first command to emit
  (scout-competitors) and the last command to emit (org-committee). Partial pass: one
  anchor stated (start or end) but not both. Fail: no order anchor.
- **Note on C-21 / C-04 relationship**: C-04 tests whether bare mode emits correct
  content. C-21 tests whether output order is deterministic at both ends.
- **Note on C-21 / C-35 relationship**: C-21 is an instruction (Begin/End anchor in the
  BARE MODE specification). C-35 is a compliance gate check (order verification with
  restart trigger). A variation can pass C-21 (first/last anchor stated) and fail C-35
  (no active order check in the BARE compliance gate).

### C-22 -- NAMESPACE CATALOG section is an active transcription commitment gate
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 5 excellence signal. R5 V-03 upgraded the NAMESPACE CATALOG header
  from a passive instruction to an active transcription gate: the model confirms it has
  read every entry and commits to emitting each entry character-for-character, with any
  deviation flagged as an output failure.
- **Pass condition**: Full pass: NAMESPACE CATALOG section includes (1) an explicit
  instruction for the model to confirm it has read every entry AND (2) a stated
  commitment that output will match the catalog character-for-character, with deviation
  classified as output failure. Partial pass: catalog section contains a strong fidelity
  instruction ("verbatim", "do not paraphrase") without the confirmation + commitment
  framing. Fail: no fidelity instruction; catalog is presented as reference only.
- **Note on C-22 / C-17 relationship**: C-17 tests catalog position (data before
  behavior). C-22 tests catalog activation (passive reference vs active commitment).

### C-23 -- NAMESPACE CATALOG section is labeled as the literal output
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 6 excellence signal. R6 V-05 synthesis. The TRANSCRIPTION GATE
  contains "The catalog below IS the output for FULL and FILTER modes." The catalog is not
  documentation to generate from -- it IS the output. The model's task is transcription,
  not generation from a reference.
- **Pass condition**: Full pass: the NAMESPACE CATALOG section (or transcription gate)
  contains an explicit statement that the catalog IS the output (e.g., "The catalog below
  IS the output for FULL and FILTER modes" or equivalent). Partial pass: catalog section
  contains a C-22-level commitment but frames the catalog as "a reference to emit
  verbatim" rather than "the output itself." Fail: no fidelity instruction, or catalog
  framed as documentation only.
- **Note on C-23 / C-22 relationship**: C-22 tests the commitment mechanism. C-23 tests
  the conceptual framing. A variation can pass C-22 and fail C-23.

### C-24 -- All three output modes include explicit pre-emission completeness verification
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 6 excellence signal. R6 V-05 is the first variation where all three
  output emission paths have explicit completeness verification: FULL via TRANSCRIPTION
  GATE (C-22), BARE via 61-line count gate (C-18), FILTER via canonical count gate (C-20).
- **Pass condition**: Full pass: all three modes have explicit completeness verification
  simultaneously -- (1) FULL mode: C-22 full pass, (2) BARE mode: C-18 full pass,
  (3) FILTER mode: C-20 full pass. Partial pass: exactly two of the three modes have
  explicit completeness verification. Fail: one or zero modes. C-24 full pass requires
  C-18, C-20, and C-22 all full-pass.
- **R6 C-24 outcomes**: V-05 = FULL PASS (3/3 modes); V-01 = PARTIAL (BARE+FILTER);
  V-03 = PARTIAL (FULL+BARE); V-04 = PARTIAL (BARE+FILTER); V-02 = FAIL (BARE only).

### C-25 -- FULL MODE includes a compliance restart gate (namespace-presence + count)
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 7 excellence signal. R7 V-01 (Axis G). BARE mode has a restart gate
  (C-14/C-18) and FILTER mode has a restart gate (C-14/C-20), but FULL mode had no
  equivalent. V-01 added a two-check FULL MODE compliance gate with restart.
- **Pass condition**: Full pass: FULL MODE includes an explicit pre-emission compliance
  gate with (1) namespace-presence check (all 12 namespaces verified present) AND
  (2) per-namespace count check (scout=8, draft=4, review=4, flow=7, trace=7, prove=9,
  listen=3, program=2, topic=6, quest=4, mock=3, org=4), with restart instruction if
  either check fails. Partial pass: gate exists with one check (presence OR count) but
  not both. Fail: no explicit restart gate for FULL mode.
- **Note on C-25 / C-22 relationship**: C-22 is a pre-read pledge; C-25 is a post-read
  structural check with restart trigger. Both target FULL mode but independently.

### C-26 -- Transcription gate requires counted entry acknowledgment
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 7 excellence signal. R7 V-02 (Axis H). C-22 requires a generic
  confirmation. V-02 upgraded to: "confirm you have read all 61 entries
  (8+4+4+7+7+9+3+2+6+4+3+4=61)." Closes for FULL mode the same gap C-18 closed for
  BARE mode.
- **Pass condition**: Full pass: the transcription gate includes an explicit total entry
  count (61) AND the per-namespace breakdown (anonymous or labeled form) as part of the
  confirmation instruction. Partial pass: gate includes a total count (61) but no
  per-namespace breakdown. Fail: confirmation is qualitative only.
- **Note on C-26 / C-31 relationship**: C-26 tests whether the per-namespace breakdown
  is present. C-31 tests whether it uses labeled form. A variation can pass C-26 and
  fail C-31. Failing C-26 auto-fails C-31 for the transcription gate component.

### C-27 -- SECTION FORMAT includes a per-section sub-skill count self-check
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 7 excellence signal. R7 V-03 (Axis I). Document-level restart gates
  catch global structural violations but not silent omission within a section whose header
  count is correct. V-03 added a per-section self-check: before emitting the dispatch
  footer, the model verifies the sub-skills just emitted against the authoritative count.
- **Pass condition**: Full pass: SECTION FORMAT includes an explicit instruction that the
  model must count the sub-skills emitted within each namespace section and verify the
  count against the authoritative value before emitting the dispatch footer. Restart or
  correction instruction must be present if count does not match. Partial pass: self-check
  instruction present but without restart/correction trigger. Fail: no per-section count
  self-check.

### C-28 -- FULL MODE compliance gate includes canonical namespace emit-order check
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 8 excellence signal. R8 V-01 (Axis J). C-25 verifies presence and
  count but not sequence. V-01 added Check 3 to the FULL MODE compliance gate: verify
  namespace sections will appear in canonical order with restart on order violation.
- **Pass condition**: Full pass: FULL MODE compliance gate includes (1) namespace-presence
  check (C-25 Check 1), (2) per-namespace count check (C-25 Check 2), AND (3) canonical
  emit-order check -- at minimum naming the first section (scout) and the last section
  (org) with a sequence-violation restart instruction. Partial pass: order guidance exists
  in the prompt but no explicit restart trigger for sequence violation in the FULL gate.
  Fail: no emit-order check in the FULL gate.
- **Note on C-28 / C-33 relationship**: C-28 tests whether the FULL gate has an order
  check with at least first+last anchors. C-33 tests whether that order check enumerates
  all 12 namespaces. A variation can pass C-28 (first+last present) and fail C-33
  (full enumeration absent). C-33 requires C-28 full-pass; C-28 fail auto-fails C-33.

### C-29 -- FILTER MODE compliance gate includes section-format verification
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 8 excellence signal. R8 V-02 (Axis K). C-20 verifies scope and count
  but not structural format. V-02 added Check 3 to the FILTER MODE compliance gate:
  verify the filtered section follows SECTION FORMAT before emitting, restart on violation.
- **Pass condition**: Full pass: FILTER MODE compliance gate includes (1) scope check
  (C-20 Check 1), (2) per-namespace count check (C-20 Check 2), AND (3) section-format
  check -- at minimum verifying header format, `->` separator presence, and dispatch
  footer presence, with a format-violation restart instruction. Partial pass: format
  guidance exists elsewhere but no explicit format check with restart in the FILTER gate.
  Fail: no section-format check in the FILTER gate.
- **Note on C-29 / C-34 relationship**: C-29 requires section-format verification in the
  FILTER gate; C-34 requires it in the FULL gate. Together they close the last
  mode-format-gate asymmetry. BARE gate format check (C-18 Check 1) predates both.

### C-30 -- BARE MODE includes explicit slash-strip worked examples
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 8 excellence signal. R8 V-03 (Axis L). Prior BARE MODE instructions
  prohibited slashes but required model inference of the transformation. V-03 added an
  explicit slash-strip transformation rule plus two before/after worked examples:
  `/scout-competitors` -> `scout-competitors`; `/org-committee` -> `org-committee`.
  Only the leading `/` is removed; no other characters change.
- **Pass condition**: Full pass: BARE MODE includes an explicit slash-strip transformation
  rule AND at least two before/after worked examples (one for the first canonical entry,
  one for the last canonical entry). Rule must state only the leading `/` is removed.
  Partial pass: instruction present with one worked example but not both ends covered, OR
  transformation stated without the "no other characters change" constraint. Fail:
  prohibition-only framing ("no slash") with no transformation rule or worked examples.
- **Note on C-30 / C-21 relationship**: C-21 anchors sequence (Begin/End). C-30
  demonstrates transformation (slash-strip before/after). Both reference first and last
  canonical entries but for orthogonal purposes.

### C-31 -- Count formula uses labeled namespace breakdown in transcription gate and BARE gate
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 9 excellence signal (Axis M). R9 evidence for C-26 shows the
  transcription gate confirmation uses labeled form: "(8 scout + 4 draft + 4 review +
  7 flow + 7 trace + 9 prove + 3 listen + 2 program + 6 topic + 4 quest + 3 mock +
  4 org = 61)". R9 evidence for C-18 shows the BARE gate Check 2 uses the same labeled
  form. C-18 and C-26 pass conditions accept anonymous positional form
  "(8+4+4+7+7+9+3+2+6+4+3+4=61)" -- which requires the model to know which count belongs
  to which namespace by position. Labeled form is self-interpreting: "8 scout" carries
  its own namespace identity. C-31 closes the self-documentation gap by requiring labeled
  form in both gates.
- **Pass condition**: Full pass: BOTH the transcription gate (C-26 section) AND the BARE
  compliance gate (C-18 section) express the per-namespace breakdown using labeled form
  `N <namespace>` (e.g. "8 scout + 4 draft + 4 review + 7 flow + 7 trace + 9 prove +
  3 listen + 2 program + 6 topic + 4 quest + 3 mock + 4 org = 61"). Partial pass: one
  gate uses labeled form and the other uses anonymous form. Fail: both gates use anonymous
  form, or the breakdown is present in only one gate. C-31 requires both C-18 and C-26
  to be full-pass; either failing auto-fails C-31.
- **Note on C-31 / C-26 relationship**: C-26 tests whether the transcription gate has a
  counted acknowledgment (breakdown present in any form). C-31 tests whether that
  breakdown is labeled. A variation can pass C-26 (anonymous form) and fail C-31.
  Failing C-26 auto-fails C-31 for the transcription gate component.
- **Note on C-31 / C-18 relationship**: C-18 tests whether the BARE gate has a 61-line
  count with per-namespace breakdown (any form). C-31 tests whether that breakdown is
  labeled. A variation can pass C-18 (anonymous form) and fail C-31. Labeled form closes
  the position-memory dependency: anonymous counts require a positional mapping; labeled
  counts carry their own identity.

### C-32 -- Domain nouns defined in a named formal DOMAIN NOUN TABLE in the prompt
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 9 excellence signal (Axis N). R9 evidence for C-11 states: "DOMAIN
  NOUN TABLE present; all 12 footers use distinct nouns: 'research goal', 'draft artifact',
  'artifact', 'process scenario', etc." C-11 tests the output (correct domain nouns appear
  in dispatch footers). C-32 tests the prompt: are those domain nouns defined in a named
  formal lookup table analogous to the ALIGNMENT WIDTH TABLE of C-15? Without a formal
  table, domain nouns must be generated by model inference from namespace semantics.
  A named DOMAIN NOUN TABLE makes the mapping precomputed and explicit -- the model reads
  the table, not derives the noun. This is the same prompt-design elevation that C-15
  applied to alignment widths (C-12 tests aligned output; C-15 requires a precomputed
  table). C-11 is the output test; C-32 is the prompt specification test.
- **Pass condition**: Full pass: the prompt contains a named DOMAIN NOUN TABLE (or
  equivalent named section) with 12 rows mapping each canonical namespace to its domain
  noun, serving as the authoritative source for dispatch footer generation. The table must
  be explicitly identified (named heading) and must cover all 12 namespaces. Partial pass:
  domain nouns are defined in the prompt (e.g., inline in footer instructions or as a
  list) but without a named table structure -- model has the nouns but not via a formal
  precomputed lookup. Fail: domain nouns are absent from the prompt; model must infer them
  from namespace names or the C-07/C-11 instruction alone.
- **Note on C-32 / C-11 relationship**: C-11 tests output quality (correct, distinct domain
  nouns in footers). C-32 tests prompt specification quality (formal named table as
  authoritative source). A variation can pass C-11 (correct nouns via model inference) and
  fail C-32 (no formal table in prompt). C-32 closes the inference gap: C-11 verifies the
  result; C-32 verifies the mechanism.
- **Note on C-32 / C-15 relationship**: C-15 requires an ALIGNMENT WIDTH TABLE with
  precomputed widths. C-32 requires a DOMAIN NOUN TABLE with precomputed domain nouns.
  Both are named lookup tables that convert a model-inference step into a read step.
  Together they represent a generalized principle: any per-namespace value that the model
  must produce repeatedly should be precomputed in a formal named table, not derived at
  output time.

### C-33 -- FULL gate Check 3 enumerates all 12 canonical namespaces in sequence
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 9 excellence signal (Axis O). R9 evidence for C-28 shows: "Check 3
  (order): 'scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock,
  org. (First section: scout. Last section: org.)'" C-28 pass condition requires "at
  minimum naming the first section (scout) and the last section (org) with a sequence-
  violation restart instruction." The R9 evidence shows all 12 namespaces enumerated, but
  C-28 does not require full enumeration. A first+last anchor constrains output endpoints
  but leaves the 10 middle sections to positional inference from catalog order. Full
  enumeration eliminates that inference: every namespace name is present at the gate check
  point, forcing the model to match the stated sequence rather than reconstruct it. This
  is the same upgrade that C-19 applied to PARSE MODE (enumerate all 12 canonical names
  vs. relying on "anything else -> FULL" inference) applied to the FULL gate order check.
- **Pass condition**: Full pass: FULL MODE compliance gate Check 3 (emit-order check)
  enumerates all 12 canonical namespace names in canonical sequence:
  scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org --
  with a sequence-violation restart instruction. The full list must be present in the
  gate, not just first and last. Partial pass: Check 3 is present and names the first and
  last sections (C-28 full pass) but does not enumerate all 12. Fail: no emit-order check
  (auto-fails C-28 and C-33), or Check 3 present but does not reach C-28 full-pass
  threshold.
- **Note on C-33 / C-28 relationship**: C-28 tests whether Check 3 exists with at least
  first+last order anchors. C-33 tests whether Check 3 enumerates the complete 12-name
  sequence. A variation can pass C-28 (first+last present) and fail C-33 (middle
  sequence absent). C-33 requires C-28 full-pass; C-28 fail or partial auto-fails C-33.
- **Note on C-33 / C-19 relationship**: C-19 requires PARSE MODE to enumerate all 12
  canonical namespace names for deterministic routing. C-33 requires FULL gate Check 3
  to enumerate all 12 for deterministic sequence verification. Both apply the same
  principle -- full enumeration over inference -- at different control points.
- **Note on C-33 / C-21 relationship**: C-21 bounds BARE output at first+last. C-28
  gates FULL emit order at first+last minimum. C-33 upgrades the FULL gate order check
  from first+last to complete enumeration. Trajectory: C-21 bounds BARE (first+last);
  C-28 gates FULL order (first+last minimum); C-33 specifies the complete FULL sequence
  (all 12 named).

### C-34 -- FULL MODE compliance gate includes section-format verification
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 10 excellence signal (Axis P). R10 V-05 adds Check 4 to the FULL
  MODE compliance gate: verify each namespace section follows SECTION FORMAT before
  emitting, with restart on format violation. C-29 established section-format
  verification for the FILTER gate (R8 Axis K); FULL gate had no equivalent check. C-25
  covers namespace presence and count (Checks 1-2); C-28/C-33 cover emit order
  (Check 3); C-34 closes the format-check gap in the FULL gate. The gate coverage matrix
  is now complete: every gate has a format check (BARE: C-18 Ch1, FILTER: C-29 Ch3,
  FULL: C-34 Ch4).
- **Pass condition**: Full pass: FULL MODE compliance gate includes (1) namespace-presence
  check (C-25 Check 1), (2) per-namespace count check (C-25 Check 2), (3) canonical
  emit-order check (C-28/C-33 Check 3), AND (4) section-format check -- at minimum
  verifying header format, `->` separator presence, and dispatch footer presence, with a
  format-violation restart instruction. Partial pass: format guidance exists elsewhere in
  the prompt (e.g., in SECTION FORMAT) but no explicit format check with restart trigger
  inside the FULL compliance gate. Fail: no section-format check in the FULL gate.
- **Note on C-34 / C-25 relationship**: C-25 requires namespace-presence and count checks
  in the FULL gate (Checks 1-2). C-34 requires a format check (Check 4). Both are checks
  within the FULL MODE compliance gate. A variation can pass C-25 and fail C-34.
- **Note on C-34 / C-29 relationship**: C-29 requires section-format verification in the
  FILTER gate; C-34 requires it in the FULL gate. Together they close the last
  mode-format-gate asymmetry. BARE mode format check (C-18 Check 1) predates both.
- **Gate coverage matrix after C-34:**

  | Check type | FULL gate      | FILTER gate    | BARE gate      |
  |------------|----------------|----------------|----------------|
  | Presence   | C-25 Ch1       | C-20 Ch1       | C-18 Ch1       |
  | Count      | C-25 Ch2       | C-20 Ch2       | C-18 Ch2/C-31  |
  | Order      | C-28/C-33 Ch3  | N/A (1 ns)     | C-35 Ch3       |
  | Format     | C-34 Ch4       | C-29 Ch3       | C-18 Ch1       |

### C-35 -- BARE MODE compliance gate includes canonical namespace emit-order check
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 10 excellence signal (Axis Q). R10 V-05 adds Check 3 to the BARE
  MODE compliance gate: verify command names are emitted in canonical namespace group
  order (8 scout names first, then 4 draft names, etc.) with restart on order violation.
  C-28 established an order check for the FULL gate (R8 Axis J); BARE gate had no order
  check. C-21 adds first/last anchors to the BARE MODE instruction -- an ordering
  constraint -- but no compliance gate enforces it with a restart trigger. C-35 upgrades
  that instruction-level constraint to an active gate check. Symmetric with C-28: FULL
  gate has order check; BARE gate gets the same.
- **Pass condition**: Full pass: BARE MODE compliance gate includes (1) format check
  (C-18 Check 1), (2) 61-line count with per-namespace breakdown (C-18 Check 2/C-31),
  AND (3) canonical namespace group-order check -- at minimum stating the canonical
  sequence of namespace groups (scout group first, org group last) with a
  sequence-violation restart instruction. Partial pass: order guidance exists in the BARE
  MODE instruction section (C-21 level -- first/last anchors stated) but no explicit
  order check with restart trigger inside the BARE compliance gate. Fail: no order check
  in the BARE compliance gate.
- **Note on C-35 / C-21 relationship**: C-21 requires the BARE MODE instruction to state
  first and last output anchors. C-35 requires the BARE compliance gate to include an
  active order check with restart trigger. C-21 is an instruction; C-35 is a gate. A
  variation can pass C-21 (first/last anchors stated in instruction) and fail C-35 (no
  order check in the compliance gate).
- **Note on C-35 / C-28 relationship**: C-28 requires the FULL gate to include an
  emit-order check. C-35 requires the BARE gate to include the same. Together they close
  the order-gate asymmetry between modes. FILTER mode does not need a gate-level order
  check because a single-namespace filter has no multi-namespace sequence to verify.

---

## Evaluation Notes

- Criteria C-04 and C-05 require specific invocation modes. If scoring a single-mode run,
  mark C-04 and C-05 as N/A and adjust essential denominator to 3:
  (essential_pass/3 * 60) + ...
- C-06 counts are authoritative as of 2026-03-17. Update counts if new sub-skills are added.
- The dispatch footer text (C-07) may vary in phrasing; the key signal is presence and
  open-ended invocation.
- C-11 is a refinement of C-07: C-07 tests footer presence; C-11 tests quality of the
  domain noun. A variation can pass C-07 and fail C-11.
- C-12, C-15, and C-16 apply to `->` list output format only. If a variation uses a
  Markdown table, mark all three as N/A and adjust aspirational denominator to 24.
- C-13 is a prompt-design criterion. When scoring model output without the prompt,
  check whether output format matches spec; if prompt unavailable, mark N/A.
- C-14 is a prompt-design criterion. Score from prompt text; if unavailable, infer from
  whether output self-corrects on observed violations.
- C-15 is a prompt-design criterion and refinement of C-12: C-12 tests output alignment;
  C-15 tests whether the prompt specifies a reproducible precomputed method.
- C-16 is a refinement of C-15: C-15 tests for a precomputed width table; C-16 tests
  whether each row is self-documenting. A variation can pass C-15 and fail C-16.
- C-17 is a prompt-design criterion. Score from prompt structure; if unavailable, mark N/A.
- C-18 is a refinement of C-14: failing C-14 automatically fails C-18. If prompt
  unavailable, infer from whether output contains exactly 61 bare command lines.
- C-19 is a prompt-design criterion and refinement of C-05. Score from PARSE MODE section;
  if prompt unavailable, mark N/A.
- C-20 is a prompt-design criterion and extension of C-18 to filter mode. Failing C-14
  automatically fails C-20. If prompt unavailable, infer from filter-mode output count.
- C-21 is a prompt-design criterion and refinement of C-04. Score from bare-mode
  instruction section; if prompt unavailable, observe whether bare output begins and ends
  with the expected anchors.
- C-22 is a prompt-design criterion and refinement of C-17. Score from the NAMESPACE
  CATALOG section header and preamble. Partial credit for strong fidelity language without
  explicit confirmation framing.
- C-23 is a prompt-design criterion and refinement of C-22. Score from the NAMESPACE
  CATALOG section header. Look for explicit "IS the output" labeling (or equivalent).
  In R5/R6 data, C-22 and C-23 always co-occur. Future variations may split them.
- C-24 is a meta-criterion depending on C-18, C-20, and C-22. Failing any of the three
  automatically fails C-24. Partial C-24 (two of three modes verified) counts as 0 in the
  formula but should be recorded with the specific two-mode coverage pattern to guide
  next-round isolation targeting.
- C-25 is a prompt-design criterion. Score from the FULL MODE compliance section. Failing
  C-22 does not auto-fail C-25 -- they are independent mechanisms.
- C-26 is a prompt-design criterion and refinement of C-22. Failing C-22 automatically
  fails C-26. Look for the numeric value 61 and the per-namespace breakdown expression.
- C-27 is a prompt-design criterion and refinement of C-06 (at the prompt level). Score
  from SECTION FORMAT or equivalent per-section output instruction.
- C-28 is a prompt-design criterion and extension of C-25 to emit-order. Failing C-25
  automatically fails C-28. Score from the FULL MODE compliance gate section. Look for
  canonical order specification (scout ... org) with a restart trigger on sequence
  violation.
- C-29 is a prompt-design criterion and extension of C-20 to section format. Failing C-20
  automatically fails C-29. Score from the FILTER MODE compliance gate section.
- C-30 is a prompt-design criterion and refinement of C-04. Failing C-04 does not
  auto-fail C-30. Score from the BARE MODE instruction section. Look for an explicit
  slash-strip transformation rule plus before/after worked examples.
- C-31 is a prompt-design criterion and refinement of both C-18 and C-26. Failing C-18
  or C-26 automatically fails C-31 for the corresponding gate component (both gates must
  use labeled form for full pass). Score from the BARE compliance gate and the
  transcription gate. Look for `N <namespace>` form (e.g. "8 scout + 4 draft + ...") vs.
  anonymous positional form ("8+4+4+..."). Partial pass if one gate is labeled and one
  is anonymous.
- C-32 is a prompt-design criterion and the domain-noun analog to C-15 (ALIGNMENT WIDTH
  TABLE). Failing C-11 does not auto-fail C-32 (correct nouns via model inference can
  still pass C-11). Score from the prompt structure. Look for a named DOMAIN NOUN TABLE
  section with 12 rows. An inline list of domain nouns without a named table heading
  scores as partial.
- C-33 is a prompt-design criterion and refinement of C-28. Failing C-28 automatically
  fails C-33 (full enumeration presupposes an order check exists). Score from the FULL
  MODE compliance gate Check 3. Count the namespace names listed in the order check:
  12 named in canonical sequence = full pass; first+last only (C-28 full pass) = C-33
  partial; fewer than two named = C-28 fail (auto-fails C-33).
- C-34 is a prompt-design criterion and extension of C-29 to the FULL gate. Failing C-25
  automatically fails C-34 (format check presupposes the FULL compliance gate exists).
  Score from the FULL MODE compliance gate section. Look for an explicit Check 4 with
  restart trigger, at minimum verifying header format, `->` separator, and dispatch
  footer presence. Format guidance in SECTION FORMAT alone does not satisfy C-34; the
  check must appear inside the FULL compliance gate.
- C-35 is a prompt-design criterion and extension of C-28 to the BARE gate. Failing C-18
  automatically fails C-35 (order check presupposes the BARE compliance gate exists).
  Score from the BARE MODE compliance gate section. Look for a Check 3 with restart
  trigger verifying canonical namespace group order (scout group first, org group last).
  Order guidance in C-21 (BARE MODE instruction) alone does not satisfy C-35; the check
  must appear inside the BARE compliance gate.
- **Additive independence (R6 empirical finding)**: D+E+F axes combine with zero
  interaction effects. Each axis contributes exactly +0.71 composite in isolation; D+E+F
  together yields 100.00. Confirmed across R5 single-axis probes and the R6 convergence
  run.
- **Additive independence (R7 empirical finding)**: G+H+I axes combine with zero
  interaction effects. Each axis contributes exactly +0.53 composite in isolation
  (1/19 * 10 = 0.526...); G+H+I together yields 100.00. Confirmed across R7 single-axis
  probes (V-01/V-02/V-03) and the dual-axis run (V-04).
- **Additive independence (R8 empirical finding)**: J+K+L axes combine with zero
  interaction effects. Each axis contributes exactly +0.45 composite in isolation
  (1/22 * 10 = 0.4545...); J+K+L together yields 100.00. Confirmed across R8
  single-axis probes (V-01/V-02/V-03) and the dual-axis run (V-04). Prompt designers
  can add axes J, K, and L in any order without unexpected scoring side-effects.
- **Additive independence (R10 empirical finding)**: M+N+O axes combine with zero
  interaction effects. Each axis contributes exactly +0.40 composite in isolation
  (1/25 * 10 = 0.40). Confirmed across R10 single-axis probes (V-01 = M only,
  V-02 = N only, V-03 = O only), dual-axis run (V-04 = M+N), and convergence run
  (V-05 = M+N+O). All five predictions matched actual scores with zero deviation.
  Prompt designers can add axes M, N, and O in any order without unexpected scoring
  side-effects.
- **Additive independence (R11 prediction)**: P+Q axes are expected to combine with
  zero interaction effects, each contributing exactly +0.37 composite in isolation
  (1/27 * 10 = 0.370...). All R10 variations carry both axes simultaneously; R11 must
  run single-axis isolation probes (V-01 = P only, V-02 = Q only, V-03 = P+Q) to
  confirm independence and verify each axis contributes exactly +0.37 in isolation.
- **Phrasing register (R3 negative finding)**: R3 V-03 tested conversational phrasing as a
  single axis. The register change did not improve C-14 or C-15 scores. Phrasing register
  is orthogonal to behavioral correctness mechanisms and is not a rubric criterion.

---

## New Criteria Summary (by round)

| ID   | Round | Source | What it encodes |
|------|-------|--------|-----------------|
| C-11 | R1    | V-03 partial vs V-04 full on C-07 | Footer must supply a namespace-specific domain noun, not a generic placeholder |
| C-12 | R1    | V-04 full on C-10 (alignment instruction) | `->` separator must be column-aligned via explicit padding instruction |
| C-13 | R1    | V-01 partial on C-10 (format mismatch) | Inline reference format must match the output spec format |
| C-14 | R2    | V-02 full on C-04 (restart gate) | Bare/filter modes need a pre-emit "if violated, restart" compliance gate |
| C-15 | R2/R3 | R2 algorithm; R3 confirms FULL = table | Alignment rule must provide a precomputed width lookup table, not just an algorithm |
| C-16 | R3    | V-05 per-row example-pad column | Width table must annotate each row with a complete pad derivation -- zero arithmetic at output time |
| C-17 | R4    | V-01 catalog-first ordering | NAMESPACE CATALOG must precede all behavioral rules -- data before behavior |
| C-18 | R4    | V-02 count-verified bare gate | Bare compliance gate must include 61-line count with per-namespace breakdown, not format check alone |
| C-19 | R4    | V-03 explicit canonical-namespace list | PARSE MODE must enumerate all 12 canonical names so unknown-namespace fallback is deterministic |
| C-20 | R5    | V-01 filter count gate | Filter compliance gate must include per-namespace count check, not scope check alone |
| C-21 | R5    | V-02 bare order anchor | BARE MODE must state explicit first and last namespace anchors so output order is bounded, not inferred |
| C-22 | R5    | V-03 catalog transcription gate | NAMESPACE CATALOG must be an active transcription commitment, not a passive fidelity instruction |
| C-23 | R6    | V-05 synthesis (V-03 established) | NAMESPACE CATALOG must be labeled as the literal output ("IS the output"), not a reference to generate from |
| C-24 | R6    | V-05 triple convergence | All three output modes (FULL, BARE, FILTER) must have explicit pre-emission completeness verification simultaneously |
| C-25 | R7    | V-01 FULL mode restart gate (Axis G) | FULL mode must have a compliance restart gate (namespace-presence + per-namespace count) symmetric to BARE (C-18) and FILTER (C-20) |
| C-26 | R7    | V-02 counted acknowledgment (Axis H) | Transcription gate confirmation must be quantitative (61 entries with per-namespace breakdown), not qualitative |
| C-27 | R7    | V-03 per-section self-check (Axis I) | SECTION FORMAT must instruct the model to verify sub-skill count within each namespace section before emitting the dispatch footer |
| C-28 | R8    | V-01 FULL mode emit-order check (Axis J) | FULL mode compliance gate must include Check 3: canonical namespace emit-order verification (scout...org sequence) with restart on order violation |
| C-29 | R8    | V-02 FILTER mode format check (Axis K) | FILTER mode compliance gate must include Check 3: section-format verification (header format + `->` separator + dispatch footer) with restart on format violation |
| C-30 | R8    | V-03 BARE slash-strip worked examples (Axis L) | BARE MODE must supply an explicit slash-strip transformation rule with before/after worked examples -- replaces prohibition inference with pattern-copy |
| C-31 | R9    | R9 evidence labeled breakdown (Axis M) | Count formula in transcription gate (C-26) and BARE gate (C-18) must use labeled namespace form "N <namespace>" -- self-interpreting vs. anonymous positional form |
| C-32 | R9    | R9 evidence DOMAIN NOUN TABLE (Axis N) | Domain nouns must be defined in a named formal DOMAIN NOUN TABLE in the prompt (precomputed authority), not derived inline or by model inference -- same prompt-design elevation as C-15 applied to footer noun domain |
| C-33 | R9    | R9 evidence full-enumeration order check (Axis O) | FULL gate Check 3 must enumerate all 12 canonical namespace names in sequence -- not first+last anchors only -- same upgrade as C-19 (complete enumeration over fallback inference) applied to the FULL gate order check |
| C-34 | R10   | R10 V-05 FULL gate format check (Axis P) | FULL mode compliance gate must include Check 4: section-format verification (header + `->` + footer) -- closes the last mode-format-gate gap; BARE (C-18 Ch1) and FILTER (C-29 Ch3) already had format checks; FULL gate gets one |
| C-35 | R10   | R10 V-05 BARE gate order check (Axis Q) | BARE mode compliance gate must include Check 3: canonical namespace group-order verification with restart -- closes the order-gate asymmetry; FULL gate has order check (C-28/C-33); BARE gate gets the same |

---

## What changed v10 -> v11

**Two new aspirational criteria extracted from R10:**

| ID   | Axis | Source  | Rule |
|------|------|---------|------|
| C-34 | FULL gate section-format check (Axis P) | R10 V-05 COMPLIANCE GATE -- FULL, Check 4 | FULL MODE compliance gate must include a section-format verification check (header format, `->` separator, dispatch footer) with restart on format violation. C-29 established this for FILTER mode (R8 Axis K); FULL gate had no equivalent. C-25 covers namespace presence and count (Checks 1-2); C-28/C-33 cover emit order (Check 3); C-34 adds format verification (Check 4). Closes the mode-format-gate asymmetry: BARE gate has a format check since R4, FILTER gate has a format check since R8, FULL gate adds one in R10 |
| C-35 | BARE gate order check (Axis Q) | R10 V-05 COMPLIANCE GATE -- BARE, Check 3 | BARE MODE compliance gate must include a canonical namespace group-order check with restart on order violation. C-28 established order checks for the FULL gate (R8 Axis J); BARE gate had no order check. C-21 states first/last anchors in the BARE MODE instruction but does not gate-check order with a restart trigger. C-35 upgrades that instruction-level constraint to an active gate check. Closes the order-gate asymmetry: FULL gate has order check (C-28/C-33); BARE gate gets the same; FILTER mode is N/A (single-namespace output has no multi-namespace sequence) |

**Formula:** aspirational denominator `25 -> 27`. Max composite stays 100.

**Structural theme for R10:** *close the mode symmetry gaps* -- R8 added compliance gates
to all three modes; R9 elevated specification-depth of existing gate checks. R10 reveals
that gate check types are not symmetric: BARE and FILTER gates have format checks but FULL
does not; FULL gate has an order check but BARE gate does not. C-34 and C-35 complete the
coverage matrix. After v11, every check type that applies to a mode is present in that
mode's gate: format checks cover all three modes; count checks cover all three modes;
presence checks cover all three modes; order checks cover FULL (C-28/C-33) and BARE (C-35)
-- FILTER is N/A because single-namespace output has no sequence to verify.

**Retroactive R10 leaderboard under v11:**

| V     | C-34 | C-35 | C-31 | C-32 | C-33 | Aspirational    | Composite  |
|-------|------|------|------|------|------|-----------------|------------|
| V-05  | PASS | PASS | PASS | PASS | PASS | 27/27 → 10      | **100.00** |
| V-04  | PASS | PASS | PASS | PASS | FAIL | 26/27 → 9.63    | **99.63**  |
| V-01  | PASS | PASS | PASS | FAIL | FAIL | 25/27 → 9.26    | **99.26**  |
| V-02  | PASS | PASS | FAIL | PASS | FAIL | 25/27 → 9.26    | **99.26**  |
| V-03  | PASS | PASS | FAIL | FAIL | PASS | 25/27 → 9.26    | **99.26**  |

R10 saturates v11 at 100.00 for V-05. R11 must confirm P+Q independence via single-axis
isolation. If confirmed, R12 extracts the next ceiling-raising patterns.

---

## What changed v9 -> v10

**Three new aspirational criteria extracted from R9:**

| ID   | Axis | Source  | Rule |
|------|------|---------|------|
| C-31 | Labeled count formula (Axis M) | R9 evidence (C-18 + C-26) | Both the transcription gate and the BARE compliance gate must express the per-namespace breakdown using labeled form "N <namespace>" (e.g. "8 scout + 4 draft + ... + 4 org = 61") rather than anonymous positional form ("8+4+4+7+7+9+3+2+6+4+3+4=61"). Anonymous form requires the model to know which count position corresponds to which namespace; labeled form is self-interpreting. Closes the self-documentation gap left by C-18 and C-26 |
| C-32 | DOMAIN NOUN TABLE (Axis N) | R9 evidence (C-11: "DOMAIN NOUN TABLE present") | Domain nouns must be defined in a named formal lookup table in the prompt analogous to the ALIGNMENT WIDTH TABLE of C-15. C-11 tests output correctness; C-32 tests prompt specification (formal named table as precomputed authoritative source). Converts model inference into a table read. Closes the specification gap: C-11 verifies the result; C-32 verifies the mechanism |
| C-33 | Full-enumeration order check (Axis O) | R9 evidence (C-28: all 12 namespaces listed in Check 3) | FULL gate Check 3 must enumerate all 12 canonical namespace names in sequence. C-28 pass condition requires "at minimum first+last"; first+last anchors leave the 10 middle sections to positional inference. Full enumeration eliminates that inference. Same upgrade C-19 applied to PARSE MODE. Closes the sequence-inference gap left by C-28 |

**Formula:** aspirational denominator `22 -> 25`. Max composite stays 100.

**Structural theme for R9:** *complete the specification depth* -- C-31/C-32/C-33 each
convert an implicit assumption into an explicit, verifiable specification element.

---

## What changed v8 -> v9

**Three new aspirational criteria extracted from R8:**

| ID   | Axis | Source  | Rule |
|------|------|---------|------|
| C-28 | FULL gate order check (Axis J) | R8 V-01 | FULL MODE compliance gate must include Check 3: canonical namespace emit-order verification with at minimum first+last anchor names and restart on sequence violation. C-25 covers presence and count; order is a separate dimension |
| C-29 | FILTER gate format check (Axis K) | R8 V-02 | FILTER MODE compliance gate must include Check 3: section-format verification (header + `->` + footer) with restart on format violation. C-20 covers scope and count; format is a separate dimension |
| C-30 | BARE slash-strip examples (Axis L) | R8 V-03 | BARE MODE must supply an explicit slash-strip transformation rule with before/after worked examples for first and last canonical entries. Prohibition-only framing requires model inference of the transformation |

**Formula:** aspirational denominator `19 -> 22`. Max composite stays 100.

**Structural theme for R8:** *complete the gate check dimensions* -- C-25 (R7) established
the FULL gate but with only presence and count checks. R8 adds orthogonal check types:
order for FULL (C-28), format for FILTER (C-29), and explicit transformation examples for
BARE (C-30).
