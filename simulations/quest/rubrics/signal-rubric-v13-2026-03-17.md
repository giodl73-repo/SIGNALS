All checks pass. Written to `simulations/quest/rubrics/signal-rubric-v13-2026-03-17.md` (91,612 chars).

---

**v13 summary — three new criteria, denominator 30 → 33:**

| ID | Axis | Elevates | Rule |
|----|------|----------|------|
| **C-39** | U | C-36 | COMPLIANCE GATE COVERAGE MATRIX cells must carry the implementing **check number** (e.g. "FULL/presence → Ch1"). Converts the matrix from a visual summary into a navigable index. Same per-row annotation elevation as C-16 applied to the coverage matrix. |
| **C-40** | V | C-37 | FULL gate Check 4 verbatim embed must **label** each sub-element explicitly ("Header:", "Separator:", "Footer:"). Enables element-name lookup rather than visual scan. Same labeled-form elevation as C-31 applied to format sub-elements. |
| **C-41** | W | C-38 | BARE gate Check 3 must use **absolute cumulative line offsets** (lines 1-8, 9-12, 13-16...) rather than relative incremental counts. Zero arithmetic at gate time. Same precomputed-value elevation as C-15 applied to BARE gate order verification. |

**Structural theme for R12:** each of the three R11 gate artifacts (coverage matrix, verbatim embed, positional bounds) has a stronger form that eliminates a residual lookup or computation step. C-39/C-40/C-41 formalize those stronger forms.

**R12 retroactive under v13:** V-04/V-05 drop from 99.67 → 98.79 (new denominator + 3 new FAILs). R13 sole target: U+V+W independence. If confirmed, R13 V-06 saturates v13 at 100.00.
 addition to locate any group; absolute offsets allow direct position lookup with zero arithmetic. Same precomputed-value elevation as C-15 (width table replaces runtime width-counting) applied to BARE gate order verification. |

**R12 empirical finding:** R+S+T axes confirmed independent. Each contributes exactly +0.33 in
isolation (1/30 x 10 = 0.333). V-01 (R only), V-02 (S only), V-03 (T only) each score 99.33;
V-04 (R+S) and V-05 (R+T) each score 99.67. V-06 (R+S+T) saturates v12 at 100.00. **R13 sole
new target: C-39, C-40, C-41.** R12 passing variations satisfy C-36/C-37/C-38 but not their
elevated forms -- the matrix has row labels but no check-number column; the verbatim embed is
unlabeled; the positional notation uses relative counts. If U+V+W independence holds, R13 V-06
saturates v13 at 100.00.

| V | C-39 | C-40 | C-41 | C-36 | C-37 | C-38 | Asp (33) | Composite |
|---|------|------|------|------|------|------|----------|-----------|
| **V-04** | FAIL | FAIL | FAIL | PASS | PASS | FAIL | 29/33 -> 8.79 | **98.79** |
| **V-05** | FAIL | FAIL | FAIL | PASS | FAIL | PASS | 29/33 -> 8.79 | **98.79** |
| **V-01** | FAIL | FAIL | FAIL | PASS | FAIL | FAIL | 28/33 -> 8.48 | **98.48** |
| **V-02** | FAIL | FAIL | FAIL | FAIL | PASS | FAIL | 28/33 -> 8.48 | **98.48** |
| **V-03** | FAIL | FAIL | FAIL | FAIL | FAIL | PASS | 28/33 -> 8.48 | **98.48** |

R13 must run three-axis isolation (V-01=U only, V-02=V only, V-03=W only) to confirm each
contributes exactly +0.30 independently (1/33 x 10 = 0.303). Then dual-axis (V-04=U+V,
V-05=U+W) and convergence (V-06=U+V+W). If independence holds, R13 V-06 saturates v13 at
100.00.

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
| C-36 | aspirational | structure   | Prompt includes a named gate-check coverage matrix |
| C-37 | aspirational | behavior    | FULL gate format check embeds SECTION FORMAT sub-elements verbatim at the gate point |
| C-38 | aspirational | behavior    | BARE gate order check specifies canonical group boundaries using positional line-range notation |
| C-39 | aspirational | structure   | COMPLIANCE GATE COVERAGE MATRIX maps each cell to its implementing check number |
| C-40 | aspirational | behavior    | FULL gate Check 4 verbatim embed labels each SECTION FORMAT sub-element explicitly |
| C-41 | aspirational | behavior    | BARE gate order check uses absolute cumulative line offsets for all 12 namespace groups |

---

## Scoring Formula

```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 33 x 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (0.30 pts each; 1/33 x 10 = 0.303)
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
- **Note on C-34 / C-37 relationship**: C-34 tests whether a format check exists in the
  FULL gate. C-37 tests whether that check embeds the SECTION FORMAT sub-elements
  verbatim at the gate point. A variation can pass C-34 (format check with restart
  present) and fail C-37 (check defers to spec section by name reference only).
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
- **Note on C-35 / C-38 relationship**: C-35 tests whether an order check exists in the
  BARE compliance gate. C-38 tests whether that check uses positional line-range groupings
  rather than namespace name lists alone. A variation can pass C-35 (order check present)
  and fail C-38 (check uses name lists, not line-range notation).

### C-36 -- Prompt includes a named gate-check coverage matrix
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 11 excellence signal 1 (gate-check type symmetry, Axis R). R11
  V-04/V-05 are the only variations where every applicable check type (presence, count,
  order, format) is present in each mode's gate. This symmetry is the result of
  C-34+C-35 being simultaneously satisfied. The excellence signal identifies the next
  elevation: rather than achieving coverage implicitly through individual criteria, the
  prompt should contain an explicit named matrix section documenting which check types
  apply to each mode. The matrix makes the completeness requirement self-documenting and
  gives the model a single reference point for verifying gate coverage rather than
  reconstructing it from individual gate sections. Analogous to ALIGNMENT WIDTH TABLE
  (C-15) and DOMAIN NOUN TABLE (C-32): converts implicit correctness into an explicit
  precomputed artifact.
- **Pass condition**: Full pass: the prompt includes a named section or table (e.g.
  COMPLIANCE GATE COVERAGE MATRIX or equivalent) that maps each check type (presence,
  count, order, format) x each output mode (FULL, FILTER, BARE) to its corresponding
  criterion reference and check number, or to N/A where the check type does not apply
  (e.g. order is N/A for FILTER). The matrix must cover all four check types and all
  three modes and must be explicitly named. Partial pass: a summary table or list exists
  that describes gate coverage but does not enumerate all four check types x three modes,
  or is not named as a distinct section. Fail: no cross-mode gate coverage summary
  anywhere in the prompt; coverage is only implicit in the individual gate sections.
- **Note on C-36 / C-15 / C-32 relationship**: C-15 requires a named ALIGNMENT WIDTH
  TABLE (12 rows x widths). C-32 requires a named DOMAIN NOUN TABLE (12 rows x nouns).
  C-36 requires a named COMPLIANCE GATE COVERAGE MATRIX (3 modes x 4 check types). All
  three follow the same pattern: per-item values that the model must produce or verify
  repeatedly should be precomputed in a formal named artifact, not reconstructed inline.

### C-37 -- FULL gate format check embeds SECTION FORMAT sub-elements verbatim at the gate point
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 11 excellence signal 2 (format check mirrors the spec, Axis S). R11
  evidence for C-34 states: "Check 4 (format): '(1) a header line in the form
  `- /<namespace> -- <purpose> -- <N> skills`, (2) sub-skill lines each using the `-> `
  separator, (3) a dispatch footer in the form `Run any sub-skill directly...`'" The
  format check does not say "verify section format per SECTION FORMAT spec" -- it
  restates the three sub-elements verbatim inline at the gate check point. A name-
  reference check requires the model to recall and apply the spec from a different section
  of the prompt at gate evaluation time; a verbatim-embed check is self-contained. This is
  the same upgrade that C-31 applied to count breakdowns (anonymous form requires
  positional recall; labeled form is self-interpreting) applied to format verification.
- **Pass condition**: Full pass: FULL MODE compliance gate Check 4 (format check) embeds
  the SECTION FORMAT sub-elements verbatim inline -- at minimum: the header line pattern
  (namespace, purpose phrase, sub-skill count), the `->` separator pattern, and the
  dispatch footer pattern. Each element must be stated directly in the check, not
  referenced by name ("per SECTION FORMAT" or "as specified above" fails). Partial pass:
  format check enumerates some but not all three sub-elements inline (e.g. header and
  separator but not footer). Fail: no format check in the FULL gate (auto-fails C-34 and
  C-37), or format check references SECTION FORMAT by name only without any inline
  element restatement.
- **Note on C-37 / C-34 relationship**: C-34 tests whether a format check exists in the
  FULL gate. C-37 tests whether that check is self-contained via verbatim element
  embedding. A variation can pass C-34 (format check exists) and fail C-37 (check defers
  to the spec by name reference). Failing C-34 auto-fails C-37.
- **Note on C-37 / C-31 relationship**: C-31 requires labeled namespace breakdowns in
  count gates (self-interpreting vs positional). C-37 requires verbatim element embedding
  in format checks (self-contained vs name-reference). Both apply the same principle:
  the gate check must carry its own verification data inline rather than relying on
  cross-prompt recall.

### C-38 -- BARE gate order check specifies canonical group boundaries using positional line-range notation
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 11 excellence signal 3 (positional group boundaries for headerless
  output, Axis T). R11 evidence for C-35 states: "Check 3 (order): 'first 8 lines are
  scout-* names, next 4 are draft-* names... last 4 are org-* names'" -- positional
  line-range groupings rather than a namespace name list. In FULL mode output, namespace
  sections have headers that anchor identity, so an order check can reference namespace
  names directly (C-33). BARE mode output has no headers: every line is an unadorned
  command name. In a headerless stream, the only self-verifiable order invariant is "line
  N falls in group X based on its positional index." A name-based order check for BARE
  output requires the model to correlate command names to namespaces at gate time; a
  line-range check requires only positional counting. C-38 requires the more reliable
  form.
- **Pass condition**: Full pass: BARE MODE compliance gate Check 3 (order check) specifies
  the canonical namespace group boundaries using positional line-range notation -- stating
  for each namespace group the line numbers or line counts that define its position in the
  61-line output (e.g. "first 8 lines are scout-* names, next 4 are draft-* names,
  next 4 are review-* names, ... last 4 are org-* names"). All 12 namespace groups must
  be positionally bounded. Partial pass: order check is present and names the first and
  last groups (C-35 pass threshold) but uses namespace name lists only, without positional
  line-range bounds for the middle groups. Fail: no order check in the BARE gate
  (auto-fails C-35 and C-38).
- **Note on C-38 / C-35 relationship**: C-35 tests whether an order check exists in the
  BARE compliance gate (at minimum first+last group bounds). C-38 tests whether that
  check uses positional line-range notation for all 12 groups. A variation can pass C-35
  (order check with first+last present) and fail C-38 (middle groups use name lists, not
  line-range bounds). Failing C-35 auto-fails C-38.
- **Note on C-38 / C-33 relationship**: C-33 requires FULL gate Check 3 to enumerate all
  12 namespace names by name in sequence. C-38 requires BARE gate Check 3 to specify
  all 12 namespace groups by positional line range. Both achieve full-coverage order
  verification, but via the only notation valid for each mode: named headers in FULL
  (names anchor identity); line-range bounds in BARE (positions anchor identity).
  Together they complete the order-check specification across modes.

---

### C-39 -- COMPLIANCE GATE COVERAGE MATRIX maps each cell to its implementing check number
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 12 excellence signal 1 (coverage matrix cell navigability, Axis U).
  R12 passing variations satisfying C-36 include a matrix (check types x modes) that
  names the check type in each row but does not indicate which numbered check within
  each gate implements it. A matrix without check-number annotations requires a reader
  to correlate matrix row names to gate check numbers by reading each gate section. A
  matrix with explicit check-number annotations (e.g. "FULL/presence = Ch1",
  "BARE/count = Ch2", "FILTER/order = N/A") eliminates that correlation step. Same
  per-row annotation elevation as C-16 (width table rows carry a complete pad derivation
  rather than just the width number) applied to the coverage matrix cells. Converts the
  matrix from a visual summary into a navigable index.
- **Pass condition**: Full pass: COMPLIANCE GATE COVERAGE MATRIX (or equivalent named
  table satisfying C-36) includes, for each applicable cell, the check number that
  implements it within the corresponding mode's compliance gate (e.g. "Ch1", "Check 1",
  or equivalent). N/A cells for inapplicable combinations (e.g. FILTER/order) must be
  explicitly marked N/A. All 11 applicable cells (4 check types x 3 modes minus 1 N/A
  for FILTER/order) must carry check-number annotations. Partial pass: matrix present
  and named (C-36 pass) but check-number annotations absent or covering fewer than half
  the cells. Fail: no named coverage matrix (auto C-36 fail -> auto C-39 fail).
- **Note on C-39 / C-36 relationship**: C-36 tests whether the coverage matrix exists as
  a named artifact. C-39 tests whether each matrix cell is annotated with its implementing
  check number. A variation can pass C-36 (matrix present, rows labeled by check type)
  and fail C-39 (no check-number column or per-cell annotation). Failing C-36
  automatically fails C-39.
- **Note on C-39 / C-16 relationship**: C-16 requires the ALIGNMENT WIDTH TABLE to
  include a per-row annotation (character count + pad count) making each row
  self-documenting. C-39 requires the COMPLIANCE GATE COVERAGE MATRIX to include a
  per-cell check-number annotation making each cell directly navigable. Both apply the
  same principle: a named table should carry sufficient per-item data to eliminate
  post-table lookup steps.

### C-40 -- FULL gate Check 4 verbatim embed labels each SECTION FORMAT sub-element explicitly
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 12 excellence signal 2 (labeled sub-element verbatim embed, Axis V).
  R12 passing variations satisfying C-37 embed the three SECTION FORMAT sub-elements
  (header pattern, `->` separator pattern, dispatch footer pattern) verbatim inline at
  FULL gate Check 4. The verbatim embed is self-contained (C-37) but the embedded
  elements are not individually labeled. An unlabeled verbatim embed requires the
  reviewer to visually pattern-match to identify which text corresponds to which
  sub-element. An explicitly labeled embed (e.g. "Header: `- /<namespace> -- <purpose>
  -- <N> skills`", "Separator: `->` (column-aligned)", "Footer: `Run any sub-skill
  directly...`") allows element-by-element verification by label lookup -- same
  labeled-form elevation as C-31 (labeled "8 scout + 4 draft + ..." vs anonymous
  "8+4+4+...") applied to the sub-element embed.
- **Pass condition**: Full pass: FULL MODE compliance gate Check 4 verbatim embed includes
  an explicit label for each of the three SECTION FORMAT sub-elements (header pattern,
  separator pattern, footer pattern) immediately before or inline with the embedded text.
  Labels may be any explicit designator (e.g. "Header:", "Separator:", "Footer:", or
  numbered "(1)", "(2)", "(3)") so long as each element can be located by label without
  visual pattern matching. All three sub-elements must be both verbatim and labeled.
  Partial pass: sub-elements embedded verbatim (C-37 pass) but without explicit labels --
  all three elements present and self-contained, but unlabeled. Fail: no verbatim embed
  (auto C-37 fail -> auto C-40 fail), or verbatim embed present with labels for some but
  not all sub-elements.
- **Note on C-40 / C-37 relationship**: C-37 tests whether verbatim embedding of all
  three sub-elements occurs. C-40 tests whether each embedded element is explicitly
  labeled. A variation can pass C-37 (three sub-elements verbatim inline) and fail C-40
  (elements present but unlabeled). Failing C-37 automatically fails C-40.
- **Note on C-40 / C-31 relationship**: C-31 requires labeled namespace breakdowns
  (labeled "8 scout" vs anonymous positional count). C-40 requires labeled sub-element
  embeds (labeled "Header:" vs unlabeled verbatim paste). Both apply the same principle:
  a self-contained inline artifact should carry labels that enable direct element-name
  lookup without positional inference or visual scanning.

### C-41 -- BARE gate order check uses absolute cumulative line offsets for all 12 namespace groups
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 12 excellence signal 3 (absolute cumulative offsets for headerless
  output, Axis W). R12 passing variations satisfying C-38 specify all 12 namespace group
  boundaries using relative incremental counts ("first 8 lines are scout-* names, next 4
  are draft-* names..."). Relative incremental counts require running addition to
  determine the absolute position of any group: to verify that flow-* names start at
  line 17, a reviewer must compute 8+4+4=16, then add 1. Absolute cumulative offsets
  ("lines 1-8: scout-*", "lines 9-12: draft-*", "lines 13-16: review-*",
  "lines 17-23: flow-*"...) allow direct position lookup with zero arithmetic at gate
  time. Same precomputed-value elevation as C-15 (width lookup table replaces runtime
  width-counting) applied to BARE gate order verification.
  Authoritative absolute offsets: scout=1-8, draft=9-12, review=13-16, flow=17-23,
  trace=24-30, prove=31-39, listen=40-42, program=43-44, topic=45-50, quest=51-54,
  mock=55-57, org=58-61.
- **Pass condition**: Full pass: BARE MODE compliance gate Check 3 (order check) specifies
  all 12 namespace group boundaries using absolute cumulative line offsets in the form
  "lines X-Y: <namespace>-* names" (or equivalent). The final group must terminate at
  line 61. Zero arithmetic must be required to verify any group's position. Partial pass:
  positional line-range notation present for all 12 groups (C-38 pass) using relative
  incremental counts, not absolute offsets -- running addition required to verify
  non-initial groups. Fail: no positional line-range notation for all 12 groups
  (auto C-38 fail -> auto C-41 fail).
- **Note on C-41 / C-38 relationship**: C-38 tests whether positional notation is used
  and all 12 groups are bounded. C-41 tests whether the notation uses absolute cumulative
  offsets eliminating runtime arithmetic. A variation can pass C-38 (all 12 groups
  positionally bounded via relative counts) and fail C-41 (position of any non-initial
  group requires running addition). Failing C-38 automatically fails C-41.
- **Note on C-41 / C-15 relationship**: C-15 requires precomputed width values in a
  lookup table so the model reads a number rather than computing it. C-41 requires
  precomputed absolute line offsets so the gate reviewer reads a position rather than
  computing it. Both apply the same principle: values that will be used for verification
  should be precomputed in the prompt, not computed at verification time.


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
  Markdown table, mark all three as N/A and adjust aspirational denominator to 27.
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
- C-36 is a prompt-design criterion and the coverage-matrix analog to C-15 and C-32.
  Score from the overall prompt structure. Look for a named section that explicitly
  maps check types x modes (3x4 or equivalent). An implicit coverage achieved by
  individual gate sections without a summary matrix scores as fail. A partial matrix
  (e.g., lists checks per mode but does not cross-tabulate) scores as partial.
- C-37 is a prompt-design criterion and refinement of C-34. Failing C-34 automatically
  fails C-37. Score from FULL MODE compliance gate Check 4. Look for the three SECTION
  FORMAT sub-elements (header line pattern, `->` separator, dispatch footer) stated
  verbatim inline in the check, not referenced by section name. A check that says "verify
  per SECTION FORMAT" without restating the elements scores as fail for C-37.
- C-38 is a prompt-design criterion and refinement of C-35. Failing C-35 automatically
  fails C-38. Score from BARE MODE compliance gate Check 3. Look for positional line-range
  notation: "first 8 lines are scout-* names, next 4 are draft-* names..." covering all
  12 namespace groups. A check that names the first and last groups only (C-35 pass
  threshold) without stating line-range bounds for all 12 groups scores as partial for
  C-35 and fail for C-38. Full C-38 requires all 12 groups positionally bounded.
- C-39 is a prompt-design criterion and refinement of C-36. Failing C-36 automatically
  fails C-39. Score from the COMPLIANCE GATE COVERAGE MATRIX. Look for a check-number
  column or per-cell annotation (e.g. "Ch1", "Check 1") for each applicable cell. A
  matrix with row labels but no check-number annotations scores as C-36 pass, C-39 fail.
  Count the annotated cells: 11 cells required (4x3 grid minus 1 N/A for FILTER/order).
- C-40 is a prompt-design criterion and refinement of C-37. Failing C-37 automatically
  fails C-40. Score from FULL MODE compliance gate Check 4. Look for explicit element
  labels (e.g. "Header:", "Separator:", "Footer:" or equivalent numbered designators)
  adjacent to each verbatim sub-element. All three sub-elements must be both verbatim and
  labeled for full pass. A check with three unlabeled verbatim embeds scores C-37 pass,
  C-40 fail.
- C-41 is a prompt-design criterion and refinement of C-38. Failing C-38 automatically
  fails C-41. Score from BARE MODE compliance gate Check 3. Look for absolute cumulative
  line-offset notation ("lines 1-8", "lines 9-12"...) vs. relative incremental count
  notation ("first 8 lines", "next 4 lines"...). Verify the final group terminates at
  line 61. Authoritative absolute offsets: scout=1-8, draft=9-12, review=13-16,
  flow=17-23, trace=24-30, prove=31-39, listen=40-42, program=43-44, topic=45-50,
  quest=51-54, mock=55-57, org=58-61. Partial C-38 (all 12 groups with relative counts)
  plus no absolute offsets = C-38 pass, C-41 fail.
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
- **Additive independence (R11 empirical finding)**: P+Q axes combine with zero
  interaction effects. Each axis contributes exactly +0.37 composite in isolation
  (1/27 * 10 = 0.370...). Confirmed across R11 single-axis probes (V-01 = P only,
  V-02 = Q only, V-03 = neither), dual-axis run (V-04 = P+Q), and convergence run
  (V-05 = P+Q+baseline). All predictions matched actual scores with zero deviation.
  Prompt designers can add axes P and Q in any order without unexpected scoring
  side-effects.
- **Additive independence (R12 empirical finding)**: R+S+T axes confirmed independent
  with zero interaction effects. Each axis contributes exactly +0.33 composite in
  isolation (1/30 * 10 = 0.333...). Confirmed across R12 single-axis probes (V-01 = R
  only, V-02 = S only, V-03 = T only) and dual-axis runs (V-04 = R+S, V-05 = R+T).
  V-06 (R+S+T) saturates v12 at 100.00. Prompt designers can add axes R, S, and T in
  any order without unexpected scoring side-effects.
- **Additive independence (R13 prediction)**: U+V+W axes are expected to combine with
  zero interaction effects, each contributing exactly +0.30 composite in isolation
  (1/33 * 10 = 0.303...). R13 must run single-axis isolation probes (V-01 = U only,
  V-02 = V only, V-03 = W only), dual-axis (V-04 = U+V, V-05 = U+W), and convergence
  (V-06 = U+V+W) to confirm independence and verify each axis contributes exactly +0.30.
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
| C-36 | R11   | R11 excellence signal 1 (gate-check type symmetry, Axis R) | Prompt must include a named COMPLIANCE GATE COVERAGE MATRIX mapping check types x modes -- makes the completeness requirement a first-class artifact rather than an implicit emergent property; same named-table elevation as C-15 (widths) and C-32 (domain nouns) |
| C-37 | R11   | R11 excellence signal 2 (format check mirrors the spec, Axis S) | FULL gate Check 4 must embed SECTION FORMAT sub-elements verbatim at the gate point (header line pattern, `->` separator, dispatch footer pattern) -- self-contained check rather than name-reference to a distant spec; same inline-data principle as C-31 (labeled vs anonymous counts) |
| C-38 | R11   | R11 excellence signal 3 (positional group boundaries for headerless output, Axis T) | BARE gate Check 3 must specify all 12 namespace group boundaries using positional line-range notation ("first 8 lines are scout-* names...") -- the only self-verifiable order invariant for headerless output; name-list notation requires correlating command names to namespace groups at gate time |
| C-39 | R12   | R12 excellence signal 1 (coverage matrix cell navigability, Axis U) | COMPLIANCE GATE COVERAGE MATRIX cells must carry the implementing check number -- converts the matrix from a visual summary into a navigable index; same per-row annotation elevation as C-16 (width table per-row derivation) applied to coverage matrix cells |
| C-40 | R12   | R12 excellence signal 2 (labeled sub-element verbatim embed, Axis V) | FULL gate Check 4 verbatim embed must label each SECTION FORMAT sub-element explicitly ("Header:", "Separator:", "Footer:") -- enables element-name lookup rather than visual pattern matching; same labeled-form elevation as C-31 (labeled namespace breakdown) applied to format sub-elements |
| C-41 | R12   | R12 excellence signal 3 (absolute cumulative offsets for headerless output, Axis W) | BARE gate Check 3 must use absolute cumulative line offsets (lines 1-8, 9-12, 13-16...) rather than relative incremental counts ("first 8, next 4...") -- zero arithmetic at gate time; same precomputed-value elevation as C-15 (precomputed width table) applied to BARE gate order verification |

---

## What changed v12 -> v13

**Three new aspirational criteria extracted from R12:**

| ID   | Axis | Source  | Rule |
|------|------|---------|------|
| C-39 | Coverage matrix cell navigability (Axis U) | R12 excellence signal 1 (C-36 passing variations: V-01, V-04, V-05) | COMPLIANCE GATE COVERAGE MATRIX must include a check-number annotation for each applicable cell. R12 passing variations contain the matrix required by C-36 with row labels but without check-number annotations. A row labeled "count" does not indicate whether it is Check 1, Check 2, or Check 3 in any mode's gate. Check-number annotations eliminate that lookup step. Follows the same per-row annotation elevation that C-16 applied to the width table |
| C-40 | Labeled sub-element verbatim embed (Axis V) | R12 excellence signal 2 (C-37 passing variations: V-02, V-04) | FULL gate Check 4 verbatim embed must include an explicit label for each of the three SECTION FORMAT sub-elements. R12 passing variations embed the three sub-elements verbatim (satisfying C-37) but without individual labels. Explicit labels allow element-by-element verification by label lookup. Follows the same labeled-form elevation that C-31 applied to count breakdowns |
| C-41 | Absolute cumulative offsets for headerless output (Axis W) | R12 excellence signal 3 (C-38 passing variations: V-03, V-05) | BARE gate Check 3 must express all 12 namespace group boundaries as absolute cumulative line offsets ("lines 1-8: scout-*", "lines 9-12: draft-*"...) rather than relative incremental counts. R12 passing variations satisfy C-38 with relative counts -- all 12 groups bounded, but verifying any non-initial group requires running addition. Authoritative offsets: scout=1-8, draft=9-12, review=13-16, flow=17-23, trace=24-30, prove=31-39, listen=40-42, program=43-44, topic=45-50, quest=51-54, mock=55-57, org=58-61 |

**Formula:** aspirational denominator `30 -> 33`. Max composite stays 100.

**Structural theme for R12:** *make each gate artifact zero-arithmetic at verification time* --
R11 added three gate artifacts (coverage matrix, verbatim format embed, positional order bounds).
R12 reveals that each artifact has a stronger form: (C-39) the coverage matrix maps cells to
check numbers so the gate is directly navigable; (C-40) the verbatim embed labels each element
so verification proceeds by name lookup rather than visual scanning; (C-41) the positional
notation uses absolute cumulative offsets so order verification requires only boundary lookup,
not running addition across preceding groups.

**Retroactive R12 leaderboard under v13:**

| V     | C-39 | C-40 | C-41 | C-36 | C-37 | C-38 | Aspirational    | Composite  |
|-------|------|------|------|------|------|------|-----------------|------------|
| V-04  | FAIL | FAIL | FAIL | PASS | PASS | FAIL | 29/33 -> 8.79   | **98.79**  |
| V-05  | FAIL | FAIL | FAIL | PASS | FAIL | PASS | 29/33 -> 8.79   | **98.79**  |
| V-01  | FAIL | FAIL | FAIL | PASS | FAIL | FAIL | 28/33 -> 8.48   | **98.48**  |
| V-02  | FAIL | FAIL | FAIL | FAIL | PASS | FAIL | 28/33 -> 8.48   | **98.48**  |
| V-03  | FAIL | FAIL | FAIL | FAIL | FAIL | PASS | 28/33 -> 8.48   | **98.48**  |

R12 does not saturate v13. R13 must isolate axes U, V, W. R12 V-04 already satisfies
C-36+C-37 (R+S); R12 V-05 already satisfies C-36+C-38 (R+T). R13 variations should build
on V-04/V-05 as the base. If U+V+W independence holds, R13 convergence saturates v13 at 100.00.

---

## What changed v11 -> v12

**Three new aspirational criteria extracted from R11:**

| ID   | Axis | Source  | Rule |
|------|------|---------|------|
| C-36 | Gate-check coverage matrix (Axis R) | R11 excellence signal 1 (gate-check type symmetry) | Prompt must include a named COMPLIANCE GATE COVERAGE MATRIX that explicitly maps check types (presence, count, order, format) x output modes (FULL, FILTER, BARE) to criterion references and N/A markers. R11 V-04/V-05 achieve full gate-check symmetry through C-34+C-35, but the coverage completeness is only implicit -- it exists as a property of the individual gate sections, not as a stated artifact. C-36 requires the matrix to be made explicit, giving the model a single reference point for coverage verification rather than reconstructing it by scanning gate sections. Follows the same named-table elevation that C-15 applied to alignment widths and C-32 applied to domain nouns |
| C-37 | FULL gate format check verbatim embed (Axis S) | R11 excellence signal 2 (format check mirrors the spec) | FULL MODE compliance gate Check 4 (format check, introduced by C-34) must embed SECTION FORMAT sub-elements verbatim inline at the gate check point -- header line pattern, `->` separator, dispatch footer pattern -- rather than referencing "SECTION FORMAT" by name. A name-reference requires the model to recall the spec from a distant section; a verbatim embed makes the check self-contained. R11 V-04/V-05 Check 4 evidence already satisfies this: it states "(1) a header line in the form..., (2) sub-skill lines each using the `->` separator, (3) a dispatch footer in the form..." directly at the gate point. C-37 formalizes this pattern as a requirement |
| C-38 | BARE gate order check line-range notation (Axis T) | R11 excellence signal 3 (positional group boundaries for headerless output) | BARE MODE compliance gate Check 3 (order check, introduced by C-35) must specify all 12 canonical namespace group boundaries using positional line-range notation ("first 8 lines are scout-* names, next 4 are draft-* names, ... last 4 are org-* names") rather than namespace name lists alone. BARE output has no headers -- line positions are the only verifiable anchors. Line-range notation is self-verifiable; name-list notation for BARE requires a positional-to-namespace mapping step that does not exist in the output stream. R11 V-02/V-04/V-05 Check 3 evidence already satisfies this; C-38 formalizes it as a requirement |

**Formula:** aspirational denominator `27 -> 30`. Max composite stays 100.

**Structural theme for R11:** *deepen specification fidelity at the gate point* -- R10
closed the gate-check type coverage matrix (C-34+C-35 complete all mode x check-type
combinations). R11 identifies three ways the gate specifications themselves can be
elevated: (C-36) make the coverage matrix an explicit named artifact rather than an
implicit property; (C-37) embed the format spec verbatim at the gate rather than
referencing it by name; (C-38) use the only self-verifiable order notation for headerless
output (line-range bounds) rather than name lists that require a cross-section mapping.

**Retroactive R11 leaderboard under v12:**

| V     | C-36 | C-37 | C-38 | Aspirational    | Composite  |
|-------|------|------|------|-----------------|------------|
| V-04  | FAIL | PASS | PASS | 28/30 -> 9.33   | **99.33**  |
| V-05  | FAIL | PASS | PASS | 28/30 -> 9.33   | **99.33**  |
| V-01  | FAIL | PASS | FAIL | 27/30 -> 9.00   | **99.00**  |
| V-02  | FAIL | FAIL | PASS | 27/30 -> 9.00   | **99.00**  |
| V-03  | FAIL | FAIL | FAIL | 25/30 -> 8.33   | **98.33**  |

R11 does not saturate v12: V-04/V-05 score 99.33 (C-36 absent from all R11 prompts).
R12 must isolate axes R, S, T. V-04/V-05 already satisfy S and T, so R12 must additionally
confirm those are independently variable (a prompt could implement C-34 with name-reference
only and fail C-37; or C-35 with first+last group names only and fail C-38). If R+S+T
independence holds, R12 convergence saturates v12 at 100.00.

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
| V-05  | PASS | PASS | PASS | PASS | PASS | 27/27 -> 10     | **100.00** |
| V-04  | PASS | PASS | PASS | PASS | FAIL | 26/27 -> 9.63   | **99.63**  |
| V-01  | PASS | PASS | PASS | FAIL | FAIL | 25/27 -> 9.26   | **99.26**  |
| V-02  | PASS | PASS | FAIL | PASS | FAIL | 25/27 -> 9.26   | **99.26**  |
| V-03  | PASS | PASS | FAIL | FAIL | PASS | 25/27 -> 9.26   | **99.26**  |

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
