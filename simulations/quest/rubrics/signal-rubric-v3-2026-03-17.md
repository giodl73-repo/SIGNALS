Written to `simulations/quest/rubrics/signal-rubric-v3-2026-03-17.md`.

---

Here is the complete updated rubric:

---

**Two new aspirational criteria extracted from Round 2:**

| ID | Source | What it encodes |
|----|--------|-----------------|
| **C-14** | V-02 C-04 full ("restart" gate) vs V-04 C-04 sufficient (rule only) | Prompt must include an explicit **pre-emit compliance gate** — "if [violation], restart" — turning a declarative rule into a self-correcting loop |
| **C-15** | V-01 C-12 full (char-count example) vs V-02 C-12 partial (instruction only) | Alignment rule must supply a **measurable derivation method** (character-count algorithm or worked numeric example), not just state the alignment goal |

**Formula change**: aspirational denominator bumps from `/5` to `/7`. Max composite stays 100; Gold threshold (80) unchanged.

**Note on C-15 / C-12 relationship**: C-12 tests the *output* (is it actually aligned?). C-15 tests the *prompt* (does it specify how to compute the padding?). A variation can pass C-12 and fail C-15 — alignment happened to be correct without a reliable rule.

**Note on C-12/C-15 N/A rule**: Both apply only to `->` list format. Markdown table variations: mark both N/A, denominator drops to 5.
y description. A raw command
  list with no descriptions fails. Descriptions must be on the same line or directly associated
  with the command, not buried in prose.

### C-04 -- `--bare` mode produces command names only
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal --bare`, output contains only bare command names
  (e.g. `scout-competitors`) with no descriptions, no namespace headers, and no prose. One
  command per line. If `--bare` is not handled and the full index is emitted instead, fails.

### C-05 -- `<namespace>` filter scopes output correctly
- **Category**: behavior
- **Weight**: essential
- **Pass condition**: When invoked as `/signal <namespace>` (e.g. `/signal flow`), output
  shows only the skills in that namespace. Skills from other namespaces must not appear. If
  no filtering occurs and the full index is returned, fails.

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

### C-15 -- Alignment rule provides a measurable derivation method
- **Category**: format
- **Weight**: aspirational
- **Source**: Round 2 excellence signal. V-01 scored full on C-12; V-02 scored partial. The
  difference: V-01 included "Count characters in the longest command name in that section,
  then pad shorter names to match" plus a worked numeric example. V-02 stated the alignment
  goal ("pad command names... align vertically") without explaining how to compute the padding
  width. A goal instruction is ambiguous when command-name lengths vary across sections; a
  derivation rule is reproducible.
- **Pass condition**: The prompt's alignment instruction specifies a concrete derivation method:
  either the character-count algorithm (find longest name in section, pad others to match) or
  a worked numeric example showing explicit pad widths. Stating the alignment goal without a
  derivation method = partial pass. No alignment instruction = fail. Applies only when output
  format uses `->` lists; N/A for Markdown table format.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band   | Score                     | Meaning                    |
|--------|---------------------------|----------------------------|
| Gold   | >= 80, all essential pass | Shippable -- meets the bar |
| Silver | >= 60, all essential pass | Useful but polish needed   |
| Bronze | any essential fail        | Not yet useful             |

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
- C-12 and C-15 both apply to `->` list output format only. If a variation uses a Markdown
  table, mark both as N/A and adjust the aspirational denominator to 5.
- C-13 is a prompt-design criterion. When scoring actual model output (not prompt design),
  assess by checking whether the output format matches the spec; if the prompt is unavailable,
  mark C-13 as N/A.
- C-14 is a prompt-design criterion. Score from the prompt text; if the prompt is unavailable,
  infer from whether the output self-corrects on observed violations.
- C-15 is a prompt-design criterion and a refinement of C-12: C-12 tests whether the output
  ends up aligned; C-15 tests whether the prompt specifies a reproducible method for computing
  the padding. A variation can pass C-12 and fail C-15 (output happened to be aligned without
  a reliable rule).
