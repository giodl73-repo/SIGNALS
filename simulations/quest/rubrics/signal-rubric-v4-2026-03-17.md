Written to `simulations/quest/rubrics/signal-rubric-v4-2026-03-17.md`.

---

## What changed v3 → v4

**One new criterion extracted from R3:**

**C-16 -- Width table includes a per-row example-pad derivation** (aspirational)
- Source: V-05 only. Beyond the C-15 precomputed table, each row gains a `name (N chars) needs X spaces` annotation. The model copies a pattern rather than applying arithmetic. V-04 satisfies C-15 but fails C-16; V-05 satisfies both.
- Pass condition: all 12 rows carry the annotation. Table with width numbers only = C-15 pass, C-16 fail.

**C-15 pass conditions tightened:**
The v3 text said "algorithm OR worked numeric example = concrete derivation method" which implied full pass. R3 scoring contradicted this — V-01/V-03 (algorithm + single example) scored PARTIAL while V-02/V-04/V-05 (12-row precomputed table) scored FULL. v4 makes this explicit: full = precomputed table; partial = algorithm + single worked example.

**Formula change:** aspirational denominator bumps from `/7` to `/8`. Max composite stays 100.

**Note added:** R3 V-03 negative finding — phrasing register (conversational vs instructional) is orthogonal to behavioral correctness and is not a rubric criterion.

**Retroactive R3 scores under v4:**

| V | C-15 | C-16 | Aspirational | Composite |
|---|------|------|--------------|-----------|
| V-05 | FULL | FULL | 8/8 → 10 | **100** |
| V-04 | FULL | FAIL | 7/8 → 8.75 | **98.75** |
| V-01 | PARTIAL | FAIL | 6.5/8 → 8.1 | **98.1** |
| V-02 | FULL | FAIL | 6/8 → 7.5 | **97.5** |
| V-03 | PARTIAL | FAIL | 5.5/8 → 6.9 | **96.9** |

V-04 and V-05 are now correctly differentiated. R4 has a clear target: C-16.
Alignment rule provides a precomputed width lookup table |
| C-16 | aspirational | format | Width table includes a per-row example-pad derivation |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
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
- **Pass condition**: Output includes sections for all 12 canonical namespaces: `scout`, `draft`,
  `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic`, `quest`, `mock`, `org`.
  FAIL if any namespace is absent or misspelled.

### C-02 -- Sub-skills listed per namespace
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Every namespace section shows its sub-skills as individually named commands
  (e.g. `/scout-competitors`, `/draft-spec`). A namespace shown with zero sub-skills listed
  fails this criterion.

### C-03 -- One-line description per sub-skill
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: Every sub-skill entry includes a non-empty description. A raw command list
  with no descriptions fails. Descriptions must be on the same line or directly associated with
  the command, not buried in prose.

### C-04 -- `--bare` mode produces command names only
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal --bare`, output contains only bare command names
  (e.g. `scout-competitors`) with no descriptions, no namespace headers, and no prose. One
  command per line. If `--bare` is not handled and the full index is emitted instead, fails.

### C-05 -- `<namespace>` filter scopes output correctly
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal <namespace>` (e.g. `/signal flow`), output shows
  only the skills in that namespace. Skills from other namespaces must not appear. If no
  filtering occurs and the full index is returned, fails.

---

## Recommended Criteria

*Output is meaningfully better with these. Combined weight = 30 pts.*

### C-06 -- Sub-skill count per namespace is accurate
- **Category**: correctness
- **Weight**: recommended
- **Pass condition**: The skill count stated in each namespace header matches the actual number
  of sub-skills listed. Authoritative counts: scout=8, draft=4, review=4, flow=7, trace=7,
  prove=9, listen=3, program=2, topic=6, quest=4, mock=3, org=4. Off-by-one or missing count
  annotation is a soft fail.

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
  namespace -- 8 skills for discovery and research"). A bare namespace name with no context
  phrase fails. At least 8 of 12 namespaces must have annotated headers to pass.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable. Combined weight = 10 pts.*

### C-09 -- Sub-skill descriptions match canonical one-liners
- **Category**: correctness
- **Weight**: aspirational
- **Pass condition**: Sub-skill descriptions match (or are semantically equivalent to) the
  authoritative one-liners in `output/T1/CLAUDE.md`. Minor paraphrase is acceptable; omitting
  a key distinguishing detail (e.g. "inertia as primary competitor" for scout-competitors) is
  a soft fail. At least 80% of sub-skills must match to pass.

### C-10 -- Output is scannable without overwhelming
- **Category**: format
- **Weight**: aspirational
- **Pass condition**: Full-index output uses consistent visual alignment (e.g. `->` separator,
  consistent indentation). Namespace sections are visually separated. No sub-skill description
  wraps to create orphan lines that break the scan rhythm. A human can locate any skill within
  10 seconds of scanning.

### C-11 -- Each footer uses a namespace-specific domain noun
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 1 excellence signal. V-04 scored full on C-07; V-03 scored partial because
  footers used a generic `<domain>` placeholder that the model had to infer rather than copy.
- **Pass condition**: Each dispatch footer substitutes the generic slot with a noun specific to
  that namespace (e.g. "research goal" for scout, "draft artifact" for draft, "flow scenario"
  for flow). A footer that retains a literal `<domain>` or `<X>` token fails. Footers that use
  the same noun across all 12 namespaces are also a soft fail. At least 10 of 12 namespaces
  must have distinct, namespace-appropriate domain nouns to pass.

### C-12 -- `->` separator is column-aligned within each namespace section
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 1 excellence signal. V-04 scored full on C-10 due to an explicit alignment
  instruction ("Align the `->` separator within each section (pad with spaces)"); other
  variations lacked the instruction and produced ragged output.
- **Pass condition**: Within each namespace section, command names are padded to equal width so
  the `->` column is vertically aligned. Ragged alignment (some entries 2 spaces before `->`,
  others 20) fails. All 12 namespace sections must maintain column alignment. Applies to
  full-index output only; N/A for `--bare` mode.

### C-13 -- Inline reference format matches the specified output format
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 1 excellence signal. V-01 scored partial on C-10 because the prompt's
  inline skill reference used `->` notation while the output specification called for a
  Markdown table, leaving the model to choose between formats and risk producing mixed output.
- **Pass condition**: The format of the prompt's embedded skill reference section is identical
  to the format specified for output. If output spec calls for `->` lists, reference must use
  `->`. If output spec calls for a table, reference must be a table. A format mismatch between
  reference and output spec is a soft fail; any observed mixed-format output is an auto fail.

### C-14 -- Bare/filter modes include a pre-emit compliance gate
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 2 excellence signal. V-02 scored full on C-04 due to an explicit restart
  guard: "If your output contains any word that is not a command name, MODE: BARE is violated.
  Restart." V-04 stated the rule clearly but omitted a self-check trigger. The gate converts a
  declarative rule into a self-correcting behavioral loop.
- **Pass condition**: The prompt includes an explicit "if [violation condition], restart"
  self-verification instruction for bare mode, filter mode, or both. Both modes gated = full
  pass. Only one mode gated = partial pass. Rule stated without a restart trigger = partial
  pass. No self-check at all = fail.

### C-15 -- Alignment rule provides a precomputed width lookup table
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 2 excellence signal, pass-condition clarified in Round 3. R2 V-01 introduced
  a character-count algorithm. R3 scoring confirmed that algorithm + single worked example =
  partial (V-01, V-03), while a 12-row precomputed lookup table = full (V-02, V-04, V-05). A
  precomputed table eliminates the runtime miscounting failure mode: the model reads a value
  rather than computing it. Providing the algorithm and one namespace's derivation still
  requires the model to count correctly for the remaining 11 namespaces.
- **Pass condition**: Full pass: the prompt includes a precomputed lookup table (one row per
  namespace) with the max command-name width or pad width as a concrete number -- model reads,
  not counts. Partial pass: character-count algorithm stated plus at least one worked numeric
  example (e.g., "/scout-naming is 13 chars. 19 - 13 = 6 pad spaces.") but no precomputed
  table -- model must still count at output time. Fail: alignment goal stated without a
  derivation method, or no alignment instruction. Applies only when output format uses `->`
  lists; N/A for Markdown table format.
- **Note on C-15 / C-12 relationship**: C-12 tests the *output* (is it actually aligned?).
  C-15 tests the *prompt* (does it provide a reliable, precomputed method?). A variation can
  pass C-12 and fail C-15 -- alignment happened to be correct without a reliable rule.

### C-16 -- Width table includes a per-row example-pad derivation
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 3 excellence signal. V-05 upgraded the C-15 precomputed table by adding an
  "example pad" column: each row shows a representative command name, its character count, and
  the pad spaces required (e.g., "/scout-naming (13) needs 7 spaces"). This makes the
  derivation self-contained at the row level -- the model copies a pattern rather than applying
  arithmetic. V-04 satisfies C-15 but not C-16: it provides the 12-row width table plus a
  single worked derivation example in a separate section, but the model must still map that
  one example across all 12 namespaces.
- **Pass condition**: The alignment width table includes a per-row annotation (dedicated column
  or inline parenthetical) showing a representative command name's character count and the
  required pad-space count for that namespace. All 12 rows must carry the annotation to pass.
  A table with width numbers only and no per-row derivation satisfies C-15 but fails C-16.
  Applies only when output format uses `->` lists; N/A for Markdown table format.
- **Note on C-16 / C-15 relationship**: C-15 tests whether the prompt provides precomputed
  width information. C-16 tests whether each row is self-documenting -- complete derivation,
  zero arithmetic at output time. A variation can pass C-15 and fail C-16.

---

## Evaluation Notes

- Criteria C-04 and C-05 require specific invocation modes. If a single run is being scored
  (not a multi-mode run), mark C-04 and C-05 as N/A and adjust the essential denominator to 3.
  Composite formula becomes: `(essential_pass/3 * 60) + ...`
- C-06 counts are authoritative as of 2026-03-17. If new sub-skills are added to a namespace,
  update the counts before scoring.
- The dispatch footer text (C-07) may vary in phrasing; the key signal is that it is present
  and invites open-ended invocation.
- C-11 is a refinement of C-07: C-07 tests presence of the footer; C-11 tests quality of the
  domain noun within it. A variation can pass C-07 and fail C-11.
- C-12, C-15, and C-16 all apply to `->` list output format only. If a variation uses a
  Markdown table, mark all three as N/A and adjust the aspirational denominator to 5.
- C-13 is a prompt-design criterion. When scoring actual model output (not prompt design),
  assess by checking whether the output format matches the spec; if the prompt is unavailable,
  mark C-13 as N/A.
- C-14 is a prompt-design criterion. Score from the prompt text; if the prompt is unavailable,
  infer from whether the output self-corrects on observed violations.
- C-15 is a prompt-design criterion and a refinement of C-12: C-12 tests whether the output
  ends up aligned; C-15 tests whether the prompt specifies a reproducible, precomputed method.
  A variation can pass C-12 and fail C-15 (output happened to be aligned without a reliable
  rule).
- C-16 is a refinement of C-15: C-15 tests for the presence of a precomputed width table;
  C-16 tests whether each row is self-documenting with a complete per-row derivation. A
  variation can pass C-15 and fail C-16.
- **Phrasing register (R3 negative finding)**: Round 3 V-03 tested conversational/user-facing
  phrasing as a single axis against the R2 V-01 baseline. The register change did not improve
  C-14 or C-15 scores -- V-03 scored 97.9 vs V-01's 99.3, with the entire gap accounted for
  by C-14 status. Phrasing register is orthogonal to behavioral correctness mechanisms and
  should not be optimized as a substitute for explicit compliance gates. It is not a rubric
  criterion.

---

## New Criteria Summary (by round)

| ID | Round | Source | What it encodes |
|----|-------|--------|-----------------|
| C-11 | R1 | V-03 partial vs V-04 full on C-07 | Footer must supply a namespace-specific domain noun, not a generic placeholder |
| C-12 | R1 | V-04 full on C-10 (alignment instruction) | `->` separator must be column-aligned via explicit padding instruction |
| C-13 | R1 | V-01 partial on C-10 (format mismatch) | Inline reference format must match the output spec format |
| C-14 | R2 | V-02 full on C-04 (restart gate) | Bare/filter modes need a pre-emit "if violated, restart" compliance gate |
| C-15 | R2/R3 | R2 algorithm; R3 confirms FULL = table | Alignment rule must provide a precomputed width lookup table, not just an algorithm |
| C-16 | R3 | V-05 per-row example-pad column | Width table must annotate each row with a complete pad derivation -- zero arithmetic at output time |
