`signal-rubric-v6-2026-03-17.md` written (434 lines). Here's a summary of what changed:

**Three new aspirational criteria (C-20, C-21, C-22):**

| ID | Axis | Source | Rule |
|----|------|--------|------|
| C-20 | Filter count gate | R5 V-01 | FILTER gate includes per-namespace count check -- same rigor as C-18 for bare mode, not scope check alone |
| C-21 | Bare order anchor | R5 V-02 | BARE MODE states explicit first (scout-competitors) and last (org-committee) anchors so output order is bounded, not inferred |
| C-22 | Transcription gate | R5 V-03 | NAMESPACE CATALOG is an active commitment gate -- model confirms comprehension and pledges character-for-character fidelity, not a passive "verbatim" instruction |

**Formula:** aspirational denominator `11 -> 14`. Max composite stays 100.

**Retroactive R5 leaderboard under v6:** V-04 leads at 99.29 (satisfies D+E); V-01/V-02/V-03 each drop to 98.57 (one axis each). Clean differentiation -- R6 target is a single variation combining D+E+F for triple convergence.

**Structural theme across R4 and R5:**
- R4: *replace implicit with explicit* (catalog-first, count gate, canonical enumeration)
- R5: *replace passive with active* (count verification extended to filter mode, order bounded at both ends, catalog becomes a commitment not a reference)

**Evaluation notes added** for C-20 (C-14 fail auto-fails C-20; can infer from filter-mode count), C-21 (score from bare instruction section; infer from observed output anchors), C-22 (partial credit for strong fidelity language without explicit confirmation framing).
-05 (target) combines D+E+F.

**Retroactive R5 scores under v6:**

| V     | C-20 | C-21 | C-22 | Aspirational   | Composite  |
|-------|------|------|------|----------------|------------|
| V-01  | PASS | FAIL | FAIL | 12/14 -> 8.57  | **98.57**  |
| V-02  | FAIL | PASS | FAIL | 12/14 -> 8.57  | **98.57**  |
| V-03  | FAIL | FAIL | PASS | 12/14 -> 8.57  | **98.57**  |
| V-04  | PASS | PASS | FAIL | 13/14 -> 9.29  | **99.29**  |

V-04 uniquely satisfies two of the three new axes. R6 target: a single variation combining
all three axes (D+E+F) to establish triple convergence under v6.

---

## What changed v4 -> v5

**Three new aspirational criteria extracted from R4:**

| ID   | Axis | Source     | Rule |
|------|------|------------|------|
| C-17 | Catalog-first    | R4 V-01 | NAMESPACE CATALOG precedes PARSE MODE and all compliance gates -- data before behavior |
| C-18 | Count gate       | R4 V-02 | Bare compliance gate includes exact 61-line count with per-namespace breakdown, not format check alone |
| C-19 | Canonical guard  | R4 V-03 | PARSE MODE enumerates all 12 canonical names so unknown-namespace fallback is deterministic, not inferred |

**Formula:** aspirational denominator `8 -> 11`. Max composite stays 100.

**Structural insight from R4**: All three excellence signals replace implicit behavior with
explicit specification. Explicit always beats implicit for robustness. R4 V-05 satisfies all
three axes simultaneously; each axis was isolated in a single-axis variation. R3 V-05
satisfies none of them.

**Retroactive R4 scores under v5:**

| V     | C-17 | C-18 | C-19 | Aspirational   | Composite  |
|-------|------|------|------|----------------|------------|
| V-05  | PASS | PASS | PASS | 11/11 -> 10    | **100**    |
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

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band   | Score                     | Meaning                    |
|--------|---------------------------|----------------------------|
| Gold   | >= 80, all essential pass | Shippable -- meets the bar |
| Silver | >= 60, all essential pass | Useful but polish needed   |
| Bronze | any essential fail        | Not yet useful             |

---

## Essential Criteria

*All must pass. Combined weight = 60 pts.*

### C-01 -- All 12 namespaces present
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Output includes sections for all 12 canonical namespaces: `scout`,
  `draft`, `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic`, `quest`,
  `mock`, `org`. FAIL if any namespace is absent or misspelled.

### C-02 -- Sub-skills listed per namespace
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Every namespace section shows its sub-skills as individually named
  commands (e.g. `/scout-competitors`, `/draft-spec`). A namespace shown with zero
  sub-skills listed fails this criterion.

### C-03 -- One-line description per sub-skill
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Every sub-skill entry includes a non-empty description. A raw command
  list with no descriptions fails. Descriptions must be on the same line or directly
  associated with the command, not buried in prose.

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
  Markdown table, mark all three as N/A and adjust aspirational denominator to 11.
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
