**signal-rubric-v9-2026-03-17.md** written.

**Three new criteria extracted from R8:**

| ID | Axis | Rule |
|----|------|------|
| C-28 | Emit-order check (Axis J) | FULL gate gains Check 3: canonical namespace sequence (scout...org) verified before emit, restart on order violation. Closes the sequence gap left by C-25 (which had presence+count but not order) |
| C-29 | Filter format check (Axis K) | FILTER gate gains Check 3: section-format verification (header line format + `->` separator + dispatch footer), restart on format violation. Closes the structural gap left by C-20 (scope+count but not format) |
| C-30 | Slash-strip worked examples (Axis L) | BARE MODE gains explicit slash-strip transformation rule with first+last before/after worked examples (`/scout-competitors` -> `scout-competitors`; `/org-committee` -> `org-committee`). Replaces prohibition-only inference with pattern-copy |

**Formula:** aspirational denominator `19 -> 22`. Each criterion contributes exactly +0.45 (1/22 * 10).

**Retroactive R8 leaderboard under v9:**

| V | C-28 | C-29 | C-30 | Composite |
|---|------|------|------|-----------|
| **V-05** | PASS | PASS | PASS | **100.00** |
| V-04 | PASS | PASS | FAIL | **99.55** |
| V-01 | PASS | FAIL | FAIL | **99.09** |
| V-02 | FAIL | PASS | FAIL | **99.09** |
| V-03 | FAIL | FAIL | PASS | **99.09** |

**Structural theme for R8:** *complete the gate detail* -- each primary compliance gate (FULL, FILTER, BARE) gains one check that the R7 ceiling left implicit. The pattern is consistent: C-25/C-20/C-21 established the gates; C-28/C-29/C-30 add the missing enforcement dimension to each.
ormat      | Width table includes a per-row example-pad derivation |
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

---

## Scoring Formula

```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 22 x 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (~0.45 pts each; 1/22 x 10 = 0.4545...)
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
  asymmetry by requiring the same rigor for filter mode. A scope-only gate catches
  cross-namespace leakage but allows a filtered namespace to silently omit or duplicate
  sub-skills.
- **Pass condition**: Full pass: filter compliance gate includes both (1) scope check (no
  other namespace appears) and (2) per-namespace count check against authoritative counts
  (scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3, program=2, topic=6,
  quest=4, mock=3, org=4) with restart instruction. Partial pass: gate has scope check
  and restart trigger but no count check. C-14 pass only: gate exists without count for
  either mode. C-14 fail: no gate (auto C-20 fail).
- **Note on C-20 / C-18 relationship**: C-18 tests count verification for bare mode; C-20
  tests it for filter mode. Both must pass for full count-gate coverage across modes. A
  variation can pass C-18 and fail C-20 (bare gate count-verified; filter gate scope-only).

### C-21 -- BARE MODE states explicit first and last namespace output anchors
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 5 excellence signal. R5 V-02 added "Begin with scout-competitors.
  End with org-committee." to BARE MODE. Without this anchor, the model must infer output
  order from catalog sequence -- a source of drift on long outputs. Explicit first and
  last anchors do not constrain intermediate order but give the model two fixed reference
  points, reducing order ambiguity to a bounded range.
- **Pass condition**: Full pass: BARE MODE (or equivalent bare-output instruction section)
  explicitly names both the first command to emit (scout-competitors or equivalent first
  canonical sub-skill) and the last command to emit (org-committee or equivalent last
  canonical sub-skill). Partial pass: one anchor stated (start or end) but not both.
  Fail: no order anchor; order is implicit from catalog position or unspecified.
- **Note on C-21 / C-04 relationship**: C-04 tests whether bare mode emits correct
  content (command names only, no descriptions). C-21 tests whether the prompt makes
  output order deterministic at both ends. A variation can pass C-04 and fail C-21
  (correct format, unanchored order).

### C-22 -- NAMESPACE CATALOG section is an active transcription commitment gate
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 5 excellence signal. R5 V-03 upgraded the NAMESPACE CATALOG header
  from a passive instruction ("emit sub-skill descriptions verbatim; do not paraphrase
  or shorten") to an active transcription gate: the model confirms it has read every
  entry and commits to emitting each entry character-for-character, with any deviation
  flagged as an output failure. A passive instruction assumes compliance; an active gate
  requires the model to form an explicit commitment before emitting, reducing paraphrase
  and omission.
- **Pass condition**: Full pass: NAMESPACE CATALOG section includes (1) an explicit
  instruction for the model to confirm it has read every entry AND (2) a stated
  commitment that output will match the catalog character-for-character, with deviation
  classified as output failure. Partial pass: catalog section contains a strong fidelity
  instruction ("verbatim", "do not paraphrase") without the confirmation + commitment
  framing. Fail: no fidelity instruction; catalog is presented as reference only.
- **Note on C-22 / C-17 relationship**: C-17 tests catalog position (data before
  behavior). C-22 tests catalog activation (passive reference vs active commitment). A
  variation can pass C-17 and fail C-22 (catalog is first but not gated).

### C-23 -- NAMESPACE CATALOG section is labeled as the literal output
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 6 excellence signal. R6 V-05 synthesis (R5 V-03 established the
  pattern). The TRANSCRIPTION GATE in V-03/V-05 contains the instruction "The catalog
  below IS the output for FULL and FILTER modes." This is a conceptual shift beyond
  C-22's commitment mechanism: the catalog is not documentation to generate from -- it
  IS the output. The model's task is transcription, not generation from a reference. The
  labeling eliminates the residual ambiguity in C-22 full-pass prompts that still frame
  the catalog as "source to match" rather than "content to emit directly." Any future
  variation could satisfy C-22 (confirmation + fidelity pledge + deviation = failure)
  without this IS-the-output labeling, which C-23 would catch.
- **Pass condition**: Full pass: the NAMESPACE CATALOG section (or transcription gate)
  contains an explicit statement that the catalog IS the output (e.g., "The catalog below
  IS the output for FULL and FILTER modes" or equivalent phrasing that defines the catalog
  as the literal output, not a fidelity target). Partial pass: catalog section contains a
  C-22-level commitment (character-for-character fidelity, deviation = failure) but frames
  the catalog as "a reference to emit verbatim" rather than "the output itself." Fail: no
  fidelity instruction, or catalog framed as documentation only.
- **Note on C-23 / C-22 relationship**: C-22 tests the commitment mechanism (read
  confirmation + character-for-character pledge + deviation = failure). C-23 tests the
  conceptual framing (catalog labeled as the literal output, not a reference to generate
  from). A variation can pass C-22 and fail C-23 if it has the commitment mechanism but
  uses "emit this verbatim" framing rather than "this IS the output" framing. In R5/R6
  data: V-03 and V-05 pass both C-22 and C-23; V-01/V-02/V-04 fail both.

### C-24 -- All three output modes include explicit pre-emission completeness verification
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 6 excellence signal. R6 V-05 is the first variation where all three
  output emission paths have explicit completeness verification: FULL mode via the
  TRANSCRIPTION GATE (C-22 pass -- model confirms it has read every entry and commits to
  character-for-character fidelity), BARE mode via the 61-line count gate (C-18 pass --
  format + exact count with per-namespace breakdown), FILTER mode via the canonical count
  gate (C-20 pass -- scope + per-namespace count with restart). Prior variations covered
  at most two paths: V-04 has BARE+FILTER (C-18+C-20) but not FULL; V-03 has FULL+BARE
  (C-22+C-18) but not FILTER; V-01 has BARE+FILTER (same as V-04). V-05 achieves
  symmetric coverage, leaving no output mode to implicit model judgment.
- **Pass condition**: Full pass: all three modes have explicit completeness verification
  simultaneously -- (1) FULL mode: NAMESPACE CATALOG is an active transcription gate
  (C-22 full pass), (2) BARE mode: compliance gate includes exact 61-line count with
  per-namespace breakdown (C-18 full pass), (3) FILTER mode: compliance gate includes
  per-namespace count check (C-20 full pass). Partial pass: exactly two of the three
  modes have explicit completeness verification (any two-of-three combination). Fail: one
  or zero modes have completeness verification. C-24 full pass requires C-18, C-20, and
  C-22 all full-pass; any of the three failing auto-fails C-24.
- **R6 C-24 outcomes**: V-05 = FULL PASS (3/3 modes); V-01 = PARTIAL (BARE+FILTER);
  V-03 = PARTIAL (FULL+BARE); V-04 = PARTIAL (BARE+FILTER, same as V-01); V-02 = FAIL
  (BARE only, 1/3 modes).
- **Note on C-24 / C-18 / C-20 / C-22 relationship**: C-18 tests BARE mode completeness.
  C-20 tests FILTER mode completeness. C-22 tests FULL mode commitment. C-24 tests
  whether all three are simultaneously satisfied. Partial C-24 designates which two modes
  are covered, informing the next-round variation design (the uncovered mode is the
  isolation target).

### C-25 -- FULL MODE includes a compliance restart gate (namespace-presence + count)
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 7 excellence signal. R7 V-01 (Axis G). BARE mode has a restart gate
  (C-14/C-18) and FILTER mode has a restart gate (C-14/C-20), but FULL mode had no
  equivalent: the only safeguard was the transcription commitment (C-22). V-01 added a
  two-check FULL MODE compliance gate -- Check 1: verify all 12 namespaces are present
  before emitting; Check 2: verify per-namespace sub-skill count matches authoritative
  counts before emitting -- with a restart instruction if either check fails. This
  completes restart-gate symmetry across all three emission paths. C-22 (commitment) and
  C-25 (restart gate) are independent: a variation can have the transcription commitment
  without a restart gate (C-22 pass, C-25 fail) or a restart gate without the
  commitment framing (C-25 pass, C-22 fail).
- **Pass condition**: Full pass: FULL MODE (or equivalent full-output instruction section)
  includes an explicit pre-emission compliance gate with (1) namespace-presence check
  (all 12 namespaces verified present) AND (2) per-namespace count check (counts match
  authoritative values: scout=8, draft=4, review=4, flow=7, trace=7, prove=9, listen=3,
  program=2, topic=6, quest=4, mock=3, org=4), with restart instruction if either check
  fails. Partial pass: gate exists for FULL mode with one check (presence OR count) but
  not both. Fail: no explicit restart gate for FULL mode (transcription commitment alone
  does not satisfy this criterion).
- **Note on C-25 / C-22 relationship**: C-22 tests the transcription commitment (model
  confirms it has read every entry, pledges character-for-character fidelity). C-25 tests
  the compliance restart gate (model verifies structural completeness before emitting,
  restarts if violated). Both mechanisms target FULL mode but at different granularities:
  C-22 is a pre-read pledge; C-25 is a post-read structural check. A variation can pass
  C-22 and fail C-25 (commitment present, no structural restart gate).
- **Note on C-25 / C-18 / C-20 relationship**: C-18 and C-20 are restart gates for BARE
  and FILTER modes respectively. C-25 is the FULL mode counterpart. Together, C-18+C-20+
  C-25 represent complete restart-gate symmetry -- every emission path has a structural
  check with restart trigger.

### C-26 -- Transcription gate requires counted entry acknowledgment
- **Category**: structure
- **Weight**: aspirational
- **Source**: Round 7 excellence signal. R7 V-02 (Axis H). C-22 requires the model to
  "confirm it has read every entry" -- a generic acknowledgment. V-02 upgraded this
  confirmation to require explicit count verification: "confirm you have read all 61
  entries (8+4+4+7+7+9+3+2+6+4+3+4=61)." This closes for FULL mode the same gap that
  C-18 closed for BARE mode: a model can acknowledge reading "all" entries without having
  read all of them; a model cannot honestly claim to have read exactly 61 entries
  (with per-namespace breakdown confirmed) without having processed every namespace. The
  counted acknowledgment converts a qualitative confirmation into a quantitative one.
- **Pass condition**: Full pass: the transcription gate (C-22 section) includes an
  explicit total entry count (61) AND the per-namespace breakdown
  (8+4+4+7+7+9+3+2+6+4+3+4=61) as part of the confirmation instruction. The model is
  required to verify it has read exactly 61 entries (not just "all" entries) before
  committing. Partial pass: gate includes a total count (61) but no per-namespace
  breakdown. Fail: confirmation is qualitative only ("confirm you have read every entry"
  or equivalent) with no numeric count.
- **Note on C-26 / C-22 relationship**: C-22 tests whether a transcription commitment
  exists (confirmed reading + character-for-character pledge). C-26 tests whether the
  confirmation is quantitative (counted) rather than qualitative (generic). A variation
  can pass C-22 and fail C-26 (commitment present, generic acknowledgment). C-26 requires
  C-22 to pass; C-22 fail auto-fails C-26.
- **Note on C-26 / C-18 relationship**: C-18 closes the count gap in BARE mode (bare gate
  includes 61-line count with per-namespace breakdown). C-26 closes the count gap in FULL
  mode (transcription gate confirmation includes 61-entry count with per-namespace
  breakdown). Same principle applied at different control points.

### C-27 -- SECTION FORMAT includes a per-section sub-skill count self-check
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 7 excellence signal. R7 V-03 (Axis I). Document-level restart gates
  (C-18 for BARE, C-20 for FILTER, C-25 for FULL) catch global structural violations --
  wrong total count, missing namespaces -- but do not catch silent omission within a
  section whose header count is correct. A section header stating "flow -- 7 skills"
  followed by only 6 sub-skills passes every document-level gate because the total count
  may still sum to 61 if another section compensates. V-03 added a per-section self-check
  to SECTION FORMAT: before emitting the dispatch footer for a namespace section, the
  model verifies that the number of sub-skills just emitted equals the authoritative count
  for that namespace. This provides section-level granularity as a complement to
  document-level restart gates.
- **Pass condition**: Full pass: SECTION FORMAT (or equivalent section-output instruction)
  includes an explicit instruction that the model must count the sub-skills emitted within
  each namespace section and verify the count against the authoritative value for that
  namespace before emitting the dispatch footer. Restart or correction instruction must
  be present if count does not match. Partial pass: self-check instruction present but
  without restart/correction trigger. Fail: no per-section count self-check; section
  completeness relies on document-level gates only.
- **Note on C-27 / C-18 / C-20 / C-25 relationship**: C-18, C-20, and C-25 are
  document-level gates (verify global count before full emission). C-27 is a
  section-level gate (verify local count within each namespace section, before the
  footer). The two levels are complementary: document-level gates catch wrong totals;
  section-level gates catch imbalanced distributions (over in one namespace, under in
  another). Both are needed for full count coverage.
- **Note on C-27 / C-06 relationship**: C-06 tests whether the skill count stated in the
  namespace header matches the actual number listed (an output correctness criterion).
  C-27 tests whether the prompt instructs the model to self-verify the count before
  emitting (a prompt-design criterion). A variation can pass C-27 (self-check instruction
  present) and still fail C-06 if the self-check instruction uses an incorrect
  authoritative count value.

### C-28 -- FULL MODE compliance gate includes canonical namespace emit-order check
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 8 excellence signal. R8 V-01 (Axis J). C-25 verifies that all 12
  namespaces are present (Check 1) and that per-namespace counts are correct (Check 2),
  but does not verify the sequence in which those sections are emitted. V-01 added Check 3
  to the FULL MODE compliance gate: before emitting, verify that namespace sections will
  appear in canonical order (scout, draft, review, flow, trace, prove, listen, program,
  topic, quest, mock, org). If any section appears out of canonical sequence, restart. This
  closes the emit-order gap: a variation passing C-25 can still emit namespaces in an
  arbitrary or alphabetical sequence; C-28 requires explicit sequence verification with a
  restart trigger. V-02 and V-03 do not add this check; V-04 and V-05 include it.
- **Pass condition**: Full pass: FULL MODE compliance gate includes (1) namespace-presence
  check (C-25 Check 1), (2) per-namespace count check (C-25 Check 2), AND (3) canonical
  emit-order check -- at minimum naming the first section (scout) and the last section
  (org) with a sequence-violation restart instruction. Partial pass: order guidance is
  present in the prompt (e.g., catalog is ordered canonically and a "follow catalog order"
  note exists) but no explicit restart trigger for sequence violation in the FULL gate.
  Fail: no emit-order check in the FULL gate (C-25 full-pass gate that lacks Check 3).
- **Note on C-28 / C-25 relationship**: C-25 tests presence and count (namespace-presence
  + per-namespace count). C-28 tests sequence (canonical emit order). A variation can pass
  C-25 and fail C-28 (presence+count gate present, order unverified). C-28 requires C-25
  to be full-pass; C-25 partial or fail auto-fails C-28.
- **Note on C-28 / C-21 relationship**: C-21 tests BARE MODE output order via explicit
  first/last anchors (Begin with scout-competitors; End with org-committee). C-28 tests
  FULL MODE gate order via a canonical-sequence restart check. Both address emit order
  but at different modes and via different mechanisms. A variation can pass C-21 (BARE
  order anchored) and fail C-28 (FULL order ungated), or vice versa.

### C-29 -- FILTER MODE compliance gate includes section-format verification
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 8 excellence signal. R8 V-02 (Axis K). C-20 verifies that the filtered
  output contains only the requested namespace (Check 1) and that its sub-skill count
  matches the authoritative value (Check 2), but does not verify that the emitted section
  is structurally well-formed. V-02 added Check 3 to the FILTER MODE compliance gate:
  before emitting, verify that the filtered section follows SECTION FORMAT -- (1) header
  line `- /<namespace> -- <purpose> -- <N> skills`, (2) sub-skill lines with `->` separator,
  (3) dispatch footer. If any required element is absent or malformed, restart. This closes
  the format gap: a C-20-passing filter output can still lack the dispatch footer, use the
  wrong header format, or emit sub-skills without `->` separators; C-29 requires explicit
  format verification at the gate. V-01 and V-03 do not add this check; V-04 and V-05
  include it.
- **Pass condition**: Full pass: FILTER MODE compliance gate includes (1) scope check
  (C-20 Check 1), (2) per-namespace count check (C-20 Check 2), AND (3) section-format
  check -- at minimum verifying header format, `->` separator presence, and dispatch footer
  presence, with a format-violation restart instruction. Partial pass: section-format
  guidance exists elsewhere in the prompt (e.g., in SECTION FORMAT) but no explicit
  format check with restart trigger in the FILTER gate itself. Fail: no section-format
  check in the FILTER gate (C-20 full-pass gate that lacks Check 3).
- **Note on C-29 / C-20 relationship**: C-20 tests scope and count (no other namespace
  appears, count matches authoritative). C-29 tests format (section is structurally
  well-formed per SECTION FORMAT). A variation can pass C-20 and fail C-29 (scope+count
  correct, format unverified at the gate). C-29 requires C-20 to be full-pass; C-20
  partial or fail auto-fails C-29.
- **Note on C-29 / C-07 relationship**: C-07 tests whether dispatch footers are present
  in the output. C-29 tests whether the FILTER gate explicitly verifies format
  (including footer presence) with a restart trigger. A variation can pass C-07 (footers
  present in observed output) and fail C-29 (no format check in the filter gate). C-29
  closes the enforcement gap: C-07 is an output-level criterion; C-29 is a gate-level
  criterion targeting the same structural property.

### C-30 -- BARE MODE includes explicit slash-strip worked examples
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 8 excellence signal. R8 V-03 (Axis L). Prior BARE MODE instructions
  prohibited slashes ("output contains only bare command names... no slash") but required
  the model to infer the slash-strip transformation from the constraint. If catalog entries
  carry a leading `/` (e.g. `/scout-competitors`), the model must deduce that stripping
  the `/` produces the required output form -- a step that is implicit under prohibition
  framing and explicit under transformation framing. V-03 replaced prohibition-only with
  an explicit slash-strip transformation rule plus two before/after worked examples:
  `/scout-competitors` becomes `scout-competitors` (first catalog entry),
  `/org-committee` becomes `org-committee` (last catalog entry). The rule states that
  only the leading `/` is removed; no other characters change. Worked examples anchor the
  pattern at both ends of the output, giving the model a pattern to copy rather than a
  constraint to interpret. V-01 and V-02 retain prohibition-only framing; V-04 does not
  add slash-strip examples; V-05 includes them.
- **Pass condition**: Full pass: BARE MODE (or equivalent bare-output instruction section)
  includes an explicit slash-strip transformation rule stating that the leading `/` is
  removed from each catalog entry, AND at least two before/after worked examples (one for
  the first canonical entry, one for the last canonical entry, or equivalent). Rule must
  state that only the leading `/` is removed and no other characters change. Partial pass:
  slash-strip instruction present (remove leading slash) with one worked example but not
  both ends covered, OR transformation stated without the "no other characters change"
  constraint. Fail: bare-mode instruction uses prohibition-only framing ("no slash",
  "command names only") with no explicit transformation rule or worked examples.
- **Note on C-30 / C-04 relationship**: C-04 tests whether bare mode emits correct content
  (command names only, no descriptions, one per line). C-30 tests whether the prompt makes
  the slash-strip transformation explicit with worked examples rather than expressing it
  as a prohibition. A variation can pass C-04 (output is correct) and fail C-30
  (transformation was inferred from prohibition, not specified explicitly). C-30 is a
  prompt-design criterion; C-04 is an output-correctness criterion.
- **Note on C-30 / C-21 relationship**: C-21 tests output order in BARE MODE via first
  and last anchors (Begin with scout-competitors; End with org-committee). C-30 tests the
  slash-strip transformation in BARE MODE via first and last worked examples
  (`/scout-competitors` -> `scout-competitors`; `/org-committee` -> `org-committee`). Both
  criteria reference the first and last canonical entries, but for orthogonal purposes:
  C-21 anchors sequence, C-30 demonstrates transformation. A variation can pass C-21
  (order anchored) and fail C-30 (transformation implicit), or pass C-30 and fail C-21.

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
  Markdown table, mark all three as N/A and adjust aspirational denominator to 19.
- C-13 is a prompt-design criterion. When scoring model output without the prompt,
  check whether output format matches spec; if prompt unavailable, mark N/A.
- C-14 is a prompt-design criterion. Score from prompt text; if unavailable, infer from
  whether output self-corrects on observed violations.
- C-15 is a prompt-design criterion and refinement of C-12: C-12 tests output alignment;
  C-15 tests whether the prompt specifies a reproducible precomputed method. A variation
  can pass C-12 and fail C-15.
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
  A variation that passes C-22 (full commitment mechanism present) but uses "emit this
  verbatim" framing rather than "this IS the output" framing scores C-22 full, C-23
  partial. In R5/R6 data, C-22 and C-23 always co-occur: passing C-22 with the full
  V-03/V-05 text implies C-23 pass. Future variations may split them.
- C-24 is a meta-criterion depending on C-18, C-20, and C-22. Failing any of the three
  automatically fails C-24. Partial C-24 (two of three modes verified) counts as 0 in the
  formula but should be recorded in scorecards with the specific two-mode coverage pattern
  (BARE+FILTER, FULL+BARE, or FULL+FILTER) to guide next-round isolation targeting.
- C-25 is a prompt-design criterion. Score from the FULL MODE (or post-transcription-gate)
  compliance section. Failing C-22 does not auto-fail C-25 -- they are independent
  mechanisms. If the prompt has a structural restart gate for FULL mode without the C-22
  commitment framing, C-22 fails but C-25 may pass.
- C-26 is a prompt-design criterion and refinement of C-22. Failing C-22 automatically
  fails C-26 (counted acknowledgment requires a commitment gate to exist first). Look for
  the numeric value 61 and the per-namespace breakdown expression in the confirmation
  instruction.
- C-27 is a prompt-design criterion and refinement of C-06 (at the prompt level). Score
  from SECTION FORMAT or equivalent per-section output instruction. If prompt unavailable,
  infer from whether output sections consistently show exactly the authoritative sub-skill
  counts.
- C-28 is a prompt-design criterion and extension of C-25 to emit-order. Failing C-25
  automatically fails C-28 (Check 3 presupposes Checks 1 and 2 of the FULL gate). Score
  from the FULL MODE compliance gate section. Look for canonical order specification
  (scout ... org) with a restart trigger on sequence violation.
- C-29 is a prompt-design criterion and extension of C-20 to section format. Failing C-20
  automatically fails C-29 (Check 3 presupposes Checks 1 and 2 of the FILTER gate). Score
  from the FILTER MODE compliance gate section. Look for explicit format-element
  enumeration (header format, `->` separator, dispatch footer) with a restart trigger on
  format violation.
- C-30 is a prompt-design criterion and refinement of C-04. Failing C-04 does not
  auto-fail C-30 (the criterion targets prompt design, not output correctness). Score from
  the BARE MODE instruction section. Look for an explicit slash-strip transformation rule
  plus before/after worked examples. Prohibition-only framing ("no slash") without a
  transformation rule fails C-30 regardless of C-04 outcome.
- **Additive independence (R6 empirical finding)**: D+E+F axes combine with zero
  interaction effects. Each axis contributes exactly +0.71 composite in isolation; D+E+F
  together yields 100.00. Confirmed across R5 single-axis probes and the R6 convergence
  run. Recorded as an evaluation note; not a new criterion.
- **Additive independence (R7 empirical finding)**: G+H+I axes combine with zero
  interaction effects. Each axis contributes exactly +0.53 composite in isolation
  (1/19 * 10 = 0.526...); G+H together yields +1.05; G+H+I together yields 100.00.
  Confirmed across R7 single-axis probes (V-01/V-02/V-03) and the dual-axis run (V-04).
  Prompt designers can add axes G, H, and I in any order without unexpected scoring
  side-effects.
- **Additive independence (R8 empirical finding)**: J+K+L axes combine with zero
  interaction effects. Each axis contributes exactly +0.45 composite in isolation
  (1/22 * 10 = 0.4545...); J+K together yields +0.91; J+K+L together yields 100.00.
  Confirmed across R8 single-axis probes (V-01/V-02/V-03) and the dual-axis run (V-04).
  Prompt designers can add axes J, K, and L in any order without unexpected scoring
  side-effects.
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
| C-23 | R6    | V-05 synthesis (V-03 established) | NAMESPACE CATALOG must be labeled as the literal output ("IS the output"), not a reference to generate from -- task is transcription, not generation |
| C-24 | R6    | V-05 triple convergence | All three output modes (FULL, BARE, FILTER) must have explicit pre-emission completeness verification simultaneously -- no mode left to implicit model judgment |
| C-25 | R7    | V-01 FULL mode restart gate (Axis G) | FULL mode must have a compliance restart gate (namespace-presence + per-namespace count) symmetric to the BARE (C-18) and FILTER (C-20) restart gates |
| C-26 | R7    | V-02 counted acknowledgment (Axis H) | Transcription gate confirmation must be quantitative (61 entries with per-namespace breakdown), not qualitative -- closes for FULL mode the gap C-18 closed for BARE mode |
| C-27 | R7    | V-03 per-section self-check (Axis I) | SECTION FORMAT must instruct the model to verify sub-skill count within each namespace section before emitting the dispatch footer -- section-level complement to document-level restart gates |
| C-28 | R8    | V-01 FULL mode emit-order check (Axis J) | FULL mode compliance gate must include Check 3: canonical namespace emit-order verification (scout...org sequence) with restart on order violation -- closes the sequence gap left by C-25 |
| C-29 | R8    | V-02 FILTER mode format check (Axis K) | FILTER mode compliance gate must include Check 3: section-format verification (header format + `->` separator + dispatch footer) with restart on format violation -- closes the structural-completeness gap left by C-20 |
| C-30 | R8    | V-03 BARE slash-strip worked examples (Axis L) | BARE MODE must supply an explicit slash-strip transformation rule with before/after worked examples -- replaces prohibition inference with pattern-copy |

---

## What changed v8 -> v9

**Three new aspirational criteria extracted from R8:**

| ID   | Axis | Source  | Rule |
|------|------|---------|------|
| C-28 | Emit-order check (Axis J) | R8 V-01 | FULL MODE compliance gate gains Check 3: canonical namespace emit-order verification. Canonical order: scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org. Restart if any section emitted out of sequence. Closes the order gap in C-25 (which verifies presence and count but not sequence) |
| C-29 | Filter format check (Axis K) | R8 V-02 | FILTER MODE compliance gate gains Check 3: section-format verification. Required elements: (1) header line `- /<namespace> -- <purpose> -- <N> skills`, (2) sub-skill lines with `->` separator, (3) dispatch footer. Restart if any element absent or malformed. Closes the structural-completeness gap in C-20 (which verifies scope and count but not format) |
| C-30 | Slash-strip worked examples (Axis L) | R8 V-03 | BARE MODE gains an explicit slash-strip transformation rule with first and last worked examples: `/scout-competitors` becomes `scout-competitors`; `/org-committee` becomes `org-committee`. Only the leading `/` is removed. Replaces prohibition-only framing ("no slash") with explicit pattern-copy. Closes the inference gap in C-04/C-21 (which anchor correct output without specifying the transformation) |

**Formula:** aspirational denominator `19 -> 22`. Max composite stays 100.

**Structural theme for R8:** *complete the gate detail* -- each of the three primary compliance
gates (FULL, FILTER, BARE) gains one additional check that the previous ceiling variation left
implicit. C-28 adds sequence verification to the FULL gate (C-25 had presence+count). C-29 adds
format verification to the FILTER gate (C-20 had scope+count). C-30 adds transformation
explicitness to BARE MODE (C-21 had order anchors; C-04 had the output requirement). Every axis
converts an implicit assumption into an explicit, restart-triggered rule.

**Retroactive R8 leaderboard under v9:**

| V     | C-28 | C-29 | C-30 | Aspirational   | Composite  |
|-------|------|------|------|----------------|------------|
| V-05  | PASS | PASS | PASS | 22/22 -> 10    | **100.00** |
| V-04  | PASS | PASS | FAIL | 21/22 -> 9.55  | **99.55**  |
| V-01  | PASS | FAIL | FAIL | 20/22 -> 9.09  | **99.09**  |
| V-02  | FAIL | PASS | FAIL | 20/22 -> 9.09  | **99.09**  |
| V-03  | FAIL | FAIL | PASS | 20/22 -> 9.09  | **99.09**  |

V-05 (J+K+L) is the unique 100.00: all three axes converge. V-04 (J+K) scores 99.55,
confirming J and K are structurally independent with zero interaction. V-01/V-02/V-03
are tied at 99.09 -- single-axis isolation confirms C-28, C-29, and C-30 each contribute
exactly +0.45 composite (1/22 * 10 = 0.4545...) in isolation.

---

## What changed v7 -> v8

**Three new aspirational criteria extracted from R7:**

| ID   | Axis | Source  | Rule |
|------|------|---------|------|
| C-25 | Full-mode restart gate  | R7 V-01 | FULL mode compliance gate with namespace-presence (Check 1) and per-namespace-count restart (Check 2) -- symmetric to C-14/C-18 (BARE) and C-14/C-20 (FILTER). Transcription commitment (C-22) and restart gate (C-25) are independent: C-22 is a pre-read pledge; C-25 is a post-read structural check with restart trigger |
| C-26 | Counted acknowledgment  | R7 V-02 | Transcription gate confirmation upgraded from qualitative ("confirm you have read every entry") to quantitative ("confirm you have read all 61 entries (8+4+4+7+7+9+3+2+6+4+3+4=61)") -- same gap that C-18 closed for BARE mode, now closed for FULL mode |
| C-27 | Per-section self-check  | R7 V-03 | SECTION FORMAT instructs the model to verify sub-skill count before emitting each namespace dispatch footer -- section-level granularity vs. document-level restart gates. Catches correct-header-count / silent-omission within a section that document-level gates cannot detect |

**Formula:** aspirational denominator `16 -> 19`. Max composite stays 100.

**Retroactive R7 leaderboard under v8:**

| V     | C-25 | C-26 | C-27 | Aspirational   | Composite  |
|-------|------|------|------|----------------|------------|
| V-05  | PASS | PASS | PASS | 19/19 -> 10    | **100.00** |
| V-04  | PASS | PASS | FAIL | 18/19 -> 9.47  | **99.47**  |
| V-01  | PASS | FAIL | FAIL | 17/19 -> 8.95  | **98.95**  |
| V-02  | FAIL | PASS | FAIL | 17/19 -> 8.95  | **98.95**  |
| V-03  | FAIL | FAIL | PASS | 17/19 -> 8.95  | **98.95**  |

---

## What changed v6 -> v7

**Two new criteria extracted from R6:**

| ID   | Axis | Rule |
|------|------|------|
| C-23 | Catalog-as-output labeling | NAMESPACE CATALOG explicitly labeled "IS the output" -- model's task is transcription, not generation from a reference. Refinement of C-22: the commitment mechanism (C-22) and the conceptual framing (C-23) are now tested separately |
| C-24 | Symmetric mode completeness | All three output modes (FULL via C-22, BARE via C-18, FILTER via C-20) have explicit pre-emission completeness verification simultaneously. Partial = 2/3 modes covered |

**Formula:** aspirational denominator `14 -> 16`. Max composite stays 100.

**Retroactive R6 leaderboard under v7:**

| V     | C-23 | C-24    | Aspirational  | Composite  |
|-------|------|---------|---------------|------------|
| V-05  | PASS | PASS    | 16/16 -> 10   | **100.00** |
| V-03  | PASS | PARTIAL | 14/16 -> 8.75 | **98.75**  |
| V-04  | FAIL | PARTIAL | 13/16 -> 8.13 | **98.13**  |
| V-01  | FAIL | PARTIAL | 12/16 -> 7.50 | **97.50**  |
| V-02  | FAIL | FAIL    | 12/16 -> 7.50 | **97.50**  |

---

## What changed v5 -> v6

**Three new aspirational criteria (C-20, C-21, C-22):**

| ID   | Axis | Source | Rule |
|------|------|--------|------|
| C-20 | Filter count gate | R5 V-01 | FILTER gate includes per-namespace count check -- same rigor as C-18 for bare mode, not scope check alone |
| C-21 | Bare order anchor | R5 V-02 | BARE MODE states explicit first (scout-competitors) and last (org-committee) anchors so output order is bounded, not inferred |
| C-22 | Transcription gate | R5 V-03 | NAMESPACE CATALOG is an active commitment gate -- model confirms comprehension and pledges character-for-character fidelity, not a passive "verbatim" instruction |

**Formula:** aspirational denominator `11 -> 14`. Max composite stays 100.

**Retroactive R5 scores under v6:**

| V     | C-20 | C-21 | C-22 | Aspirational   | Composite  |
|-------|------|------|------|----------------|------------|
| V-04  | PASS | PASS | FAIL | 13/14 -> 9.29  | **99.29**  |
| V-01  | PASS | FAIL | FAIL | 12/14 -> 8.57  | **98.57**  |
| V-02  | FAIL | PASS | FAIL | 12/14 -> 8.57  | **98.57**  |
| V-03  | FAIL | FAIL | PASS | 12/14 -> 8.57  | **98.57**  |

---

## What changed v4 -> v5

**Three new aspirational criteria extracted from R4:**

| ID   | Axis | Source     | Rule |
|------|------|------------|------|
| C-17 | Catalog-first    | R4 V-01 | NAMESPACE CATALOG precedes PARSE MODE and all compliance gates -- data before behavior |
| C-18 | Count gate       | R4 V-02 | Bare compliance gate includes exact 61-line count with per-namespace breakdown, not format check alone |
| C-19 | Canonical guard  | R4 V-03 | PARSE MODE enumerates all 12 canonical names so unknown-namespace fallback is deterministic, not inferred |

**Formula:** aspirational denominator `8 -> 11`. Max composite stays 100.

**Retroactive R4 scores under v5:**

| V     | C-17 | C-18 | C-19 | Aspirational   | Composite  |
|-------|------|------|------|----------------|------------|
| V-05  | PASS | PASS | PASS | 11/11 -> 10    | **100.00** |
| V-04  | FAIL | PASS | PASS | 10/11 -> 9.09  | **99.09**  |
| V-01  | PASS | FAIL | FAIL | 9/11 -> 8.18   | **98.18**  |
| V-02  | FAIL | PASS | FAIL | 9/11 -> 8.18   | **98.18**  |
| V-03  | FAIL | FAIL | PASS | 9/11 -> 8.18   | **98.18**  |

---

## What changed v3 -> v4

**One new criterion extracted from R3:**

**C-16 -- Width table includes a per-row example-pad derivation** (aspirational)
- Source: V-05 only. Beyond the C-15 precomputed table, each row gains a
  `name (N chars) needs X spaces` annotation. The model copies a pattern rather than
  applying arithmetic. V-04 satisfies C-15 but fails C-16; V-05 satisfies both.
- Pass condition: all 12 rows carry the annotation. Table with width numbers only = C-15
  pass, C-16 fail.

**C-15 pass conditions tightened:**
The v3 text said "algorithm OR worked numeric example = concrete derivation method" which
implied full pass. R3 scoring contradicted this -- V-01/V-03 (algorithm + single example)
scored PARTIAL while V-02/V-04/V-05 (12-row precomputed table) scored FULL. v4 makes this
explicit: full = precomputed table; partial = algorithm + single worked example.

**Formula change:** aspirational denominator bumped from `/7` to `/8`.

**Note added:** R3 V-03 negative finding -- phrasing register (conversational vs
instructional) is orthogonal to behavioral correctness and is not a rubric criterion.
