"""Build signal-rubric-v13 from v12 by applying structured diffs."""

v12 = open('C:/src/sim/simulations/quest/rubrics/signal-rubric-v12-2026-03-17.md', encoding='utf-8').read()

# Strip v12 header section (keep everything from ## Criterion Index onward)
idx_start = v12.find('## Criterion Index')
v12_body = v12[idx_start:]

# ── 1. Fix scoring formula denominator ───────────────────────────────────────
v12_body = v12_body.replace(
    'aspirational_pass / 30 x 10',
    'aspirational_pass / 33 x 10'
)
v12_body = v12_body.replace(
    '0.33 pts each; 1/30 x 10 = 0.333',
    '0.30 pts each; 1/33 x 10 = 0.303'
)

# ── 2. Add C-39/C-40/C-41 rows to criterion index ────────────────────────────
old_idx_end = (
    '| C-38 | aspirational | behavior    | BARE gate order check specifies canonical'
    ' group boundaries using positional line-range notation |\n\n---'
)
new_idx_end = (
    '| C-38 | aspirational | behavior    | BARE gate order check specifies canonical'
    ' group boundaries using positional line-range notation |\n'
    '| C-39 | aspirational | structure   | COMPLIANCE GATE COVERAGE MATRIX maps each'
    ' cell to its implementing check number |\n'
    '| C-40 | aspirational | behavior    | FULL gate Check 4 verbatim embed labels each'
    ' SECTION FORMAT sub-element explicitly |\n'
    '| C-41 | aspirational | behavior    | BARE gate order check uses absolute cumulative'
    ' line offsets for all 12 namespace groups |\n\n---'
)
v12_body = v12_body.replace(old_idx_end, new_idx_end, 1)

# ── 3. New criterion sections to insert before ## Evaluation Notes ────────────
new_criteria_sections = """
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

"""

eval_marker = '\n## Evaluation Notes\n'
v12_body = v12_body.replace(eval_marker, new_criteria_sections + eval_marker, 1)

# ── 4. Add C-39/C-40/C-41 evaluation notes (before additive independence block) ──
old_eval_anchor = '- **Additive independence (R6 empirical finding)**'
new_eval_notes = (
    '- C-39 is a prompt-design criterion and refinement of C-36. Failing C-36 automatically\n'
    '  fails C-39. Score from the COMPLIANCE GATE COVERAGE MATRIX. Look for a check-number\n'
    '  column or per-cell annotation (e.g. "Ch1", "Check 1") for each applicable cell. A\n'
    '  matrix with row labels but no check-number annotations scores as C-36 pass, C-39 fail.\n'
    '  Count the annotated cells: 11 cells required (4x3 grid minus 1 N/A for FILTER/order).\n'
    '- C-40 is a prompt-design criterion and refinement of C-37. Failing C-37 automatically\n'
    '  fails C-40. Score from FULL MODE compliance gate Check 4. Look for explicit element\n'
    '  labels (e.g. "Header:", "Separator:", "Footer:" or equivalent numbered designators)\n'
    '  adjacent to each verbatim sub-element. All three sub-elements must be both verbatim and\n'
    '  labeled for full pass. A check with three unlabeled verbatim embeds scores C-37 pass,\n'
    '  C-40 fail.\n'
    '- C-41 is a prompt-design criterion and refinement of C-38. Failing C-38 automatically\n'
    '  fails C-41. Score from BARE MODE compliance gate Check 3. Look for absolute cumulative\n'
    '  line-offset notation ("lines 1-8", "lines 9-12"...) vs. relative incremental count\n'
    '  notation ("first 8 lines", "next 4 lines"...). Verify the final group terminates at\n'
    '  line 61. Authoritative absolute offsets: scout=1-8, draft=9-12, review=13-16,\n'
    '  flow=17-23, trace=24-30, prove=31-39, listen=40-42, program=43-44, topic=45-50,\n'
    '  quest=51-54, mock=55-57, org=58-61. Partial C-38 (all 12 groups with relative counts)\n'
    '  plus no absolute offsets = C-38 pass, C-41 fail.\n'
    '- **Additive independence (R6 empirical finding)**'
)
v12_body = v12_body.replace(old_eval_anchor, new_eval_notes, 1)

# ── 5. Upgrade R12 from prediction to empirical finding, add R13 prediction ──
old_r12 = (
    '- **Additive independence (R12 prediction)**: R+S+T axes are expected to combine with\n'
    '  zero interaction effects, each contributing exactly +0.33 composite in isolation\n'
    '  (1/30 * 10 = 0.333...). R11 V-04/V-05 carry S and T (achieved through their C-34/C-35\n'
    '  implementations); R11 carries none of R. R12 must run single-axis isolation probes\n'
    '  (V-01 = R only, V-02 = S only, V-03 = T only), dual-axis (V-04 = R+S, V-05 = R+T),\n'
    '  and convergence (V-06 = R+S+T) to confirm independence and verify each axis\n'
    '  contributes exactly +0.33 in isolation.'
)
new_r12 = (
    '- **Additive independence (R12 empirical finding)**: R+S+T axes confirmed independent\n'
    '  with zero interaction effects. Each axis contributes exactly +0.33 composite in\n'
    '  isolation (1/30 * 10 = 0.333...). Confirmed across R12 single-axis probes (V-01 = R\n'
    '  only, V-02 = S only, V-03 = T only) and dual-axis runs (V-04 = R+S, V-05 = R+T).\n'
    '  V-06 (R+S+T) saturates v12 at 100.00. Prompt designers can add axes R, S, and T in\n'
    '  any order without unexpected scoring side-effects.\n'
    '- **Additive independence (R13 prediction)**: U+V+W axes are expected to combine with\n'
    '  zero interaction effects, each contributing exactly +0.30 composite in isolation\n'
    '  (1/33 * 10 = 0.303...). R13 must run single-axis isolation probes (V-01 = U only,\n'
    '  V-02 = V only, V-03 = W only), dual-axis (V-04 = U+V, V-05 = U+W), and convergence\n'
    '  (V-06 = U+V+W) to confirm independence and verify each axis contributes exactly +0.30.'
)
v12_body = v12_body.replace(old_r12, new_r12, 1)

# ── 6. Extend new criteria summary table with C-39/C-40/C-41 ─────────────────
old_tbl_end = (
    '| C-38 | R11   | R11 excellence signal 3 (positional group boundaries for headerless'
    ' output, Axis T) | BARE gate Check 3 must specify all 12 namespace group boundaries'
    ' using positional line-range notation ("first 8 lines are scout-* names...") -- the'
    ' only self-verifiable order invariant for headerless output; name-list notation'
    ' requires correlating command names to namespace groups at gate time |'
)
new_tbl_end = (
    old_tbl_end + '\n'
    '| C-39 | R12   | R12 excellence signal 1 (coverage matrix cell navigability, Axis U)'
    ' | COMPLIANCE GATE COVERAGE MATRIX cells must carry the implementing check number'
    ' -- converts the matrix from a visual summary into a navigable index; same per-row'
    ' annotation elevation as C-16 (width table per-row derivation) applied to coverage'
    ' matrix cells |\n'
    '| C-40 | R12   | R12 excellence signal 2 (labeled sub-element verbatim embed, Axis V)'
    ' | FULL gate Check 4 verbatim embed must label each SECTION FORMAT sub-element'
    ' explicitly ("Header:", "Separator:", "Footer:") -- enables element-name lookup rather'
    ' than visual pattern matching; same labeled-form elevation as C-31 (labeled namespace'
    ' breakdown) applied to format sub-elements |\n'
    '| C-41 | R12   | R12 excellence signal 3 (absolute cumulative offsets for headerless'
    ' output, Axis W) | BARE gate Check 3 must use absolute cumulative line offsets'
    ' (lines 1-8, 9-12, 13-16...) rather than relative incremental counts ("first 8,'
    ' next 4...") -- zero arithmetic at gate time; same precomputed-value elevation as'
    ' C-15 (precomputed width table) applied to BARE gate order verification |'
)
v12_body = v12_body.replace(old_tbl_end, new_tbl_end, 1)

# ── 7. Prepend "What changed v12->v13" before "What changed v11->v12" ────────
v13_changelog = """## What changed v12 -> v13

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

"""

v12_body = v12_body.replace('## What changed v11 -> v12', v13_changelog + '## What changed v11 -> v12', 1)

# ── 8. Assemble complete v13 document ────────────────────────────────────────
v13_header = """---

**v13 adds three criteria (C-39, C-40, C-41), denominator 30 -> 33:**

| ID | Axis | Source | What it captures |
|----|------|--------|-----------------|
| **C-39** | U | Signal 1: coverage matrix cell navigability | COMPLIANCE GATE COVERAGE MATRIX cells must each carry the implementing **check number** (e.g. "FULL/presence -> Ch1", "BARE/count -> Ch2"). C-36 requires the matrix to exist; C-39 requires each cell to be directly navigable to its gate check. Same per-row annotation elevation as C-16 (width table rows carry a pad derivation) applied to the coverage matrix. Eliminates the name-to-check correlation step at review time. |
| **C-40** | V | Signal 2: labeled sub-element verbatim embed | FULL gate Check 4 verbatim embed must **label** each SECTION FORMAT sub-element explicitly (e.g. "Header:", "Separator:", "Footer:") adjacent to the embedded text. C-37 requires verbatim embedding; C-40 requires the embedding to be labeled for direct element-name verification rather than visual pattern matching. Same labeled-form elevation as C-31 (labeled namespace breakdown vs anonymous positional form) applied to the format check embed. |
| **C-41** | W | Signal 3: absolute cumulative offsets for headerless output | BARE gate Check 3 positional notation must use **absolute cumulative line offsets** ("lines 1-8: scout-*, lines 9-12: draft-*...") rather than relative incremental counts ("first 8 lines, next 4 lines..."). Relative counts require running addition to locate any group; absolute offsets allow direct position lookup with zero arithmetic. Same precomputed-value elevation as C-15 (width table replaces runtime width-counting) applied to BARE gate order verification. |

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

"""

v13 = v13_header + v12_body

out_path = 'C:/src/sim/simulations/quest/rubrics/signal-rubric-v13-2026-03-17.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(v13)

print(f'Written {len(v13)} chars to {out_path}')
checks = {
    'C-39 criterion section': '### C-39 --' in v13,
    'C-40 criterion section': '### C-40 --' in v13,
    'C-41 criterion section': '### C-41 --' in v13,
    'C-39 index row': '| C-39 | aspirational' in v13,
    'denominator 33': '/ 33 x 10' in v13,
    'What changed v12->v13': '## What changed v12 -> v13' in v13,
    'R12 empirical finding': 'R12 empirical finding' in v13,
    'R13 prediction': 'R13 prediction' in v13,
    'C-39 eval note': 'C-39 is a prompt-design criterion' in v13,
    'C-41 absolute offsets': 'absolute cumulative line offsets' in v13,
}
for k, v in checks.items():
    print(f'  {"OK" if v else "FAIL"} {k}')
