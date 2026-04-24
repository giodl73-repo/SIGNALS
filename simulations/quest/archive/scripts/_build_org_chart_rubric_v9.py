import re

v8_path = 'C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v8-2026-03-16.md'
v9_path = 'C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v9-2026-03-16.md'

v8 = open(v8_path, encoding='utf-8').read()

header = """---

**What changed -- v9**

Two new aspirational criteria from R9 V-04/V-05 excellence signals:

| ID | Pattern | What it adds |
|----|---------|-------------|
| A-21 | `sub-section-4-anchor-ordering` | Fixed linear ordering within Sub-section 4 when `COST-FRAME CONCLUSION:` (A-18), `NET-COST-COMPARISON:` block (A-10), and `FLAT-CASE-PRESSURE:` line (C-01) all co-occur: COST-FRAME CONCLUSION precedes NET-COST-COMPARISON, which precedes FLAT-CASE-PRESSURE, with no interceding content between them. Converts an implicit expectation into an independently verifiable positional constraint. |
| A-22 | `per-artifact-inline-zone-label` | When A-20 (INTEGRATION-NOTE) is active, each positional artifact's own instruction block carries its canonical zone designator (`PRE-ASSESSMENT` / `SUB-SECTION-3` / `POST-VERDICT-BRANCH`) as an inline label at the artifact definition site. Zone assignment becomes readable without consulting the INTEGRATION-NOTE summary. |

**Formula:** `aspirational_pass/20 * 10` -> `aspirational_pass/22 * 10`

**Golden threshold:** unchanged -- 5/5 essential + composite >= 80.

  v8 -- added A-17/A-18/A-19/A-20 from R8 V-05 excellence signals:
  typed-floor-rows-with-displacement-guard (Mechanism Type column, closed set, diversity
  floor >= 2 distinct categories, FLAT-CASE-CLOSED emits type-diversity count),
  pre-evidence-cost-frame-grounds-verdict (COST-FRAME CONCLUSION: as first line of
  Sub-section 4, names A-16 frame by label, cites dominant error risk, names sub-section
  as evidence source),
  additive-citation-with-explicit-displacement-prohibition (ADDITIVE-TO: C-01
  FLAT-CASE-PRESSURE guard line inside the A-10 NET-COST-COMPARISON block),
  positional-disjointness-as-combination-strategy (INTEGRATION-NOTE block after
  Sub-section 4 listing all three positional artifacts with canonical zone designators
  and confirming non-overlap).
  Aspirational denominator updated from /16 to /20.
  v7 -- added A-14/A-15/A-16 from R7 excellence signals:
  UNCOVERED-function-citation-in-rebuttal (V-01 axis: UNCOVERED: labeled block in
  Sub-section 3, additive constraint with displacement prohibition),
  flat-operating-rhythm-table (V-02 axis: CAN-OPERATE-FLAT branch, >= 2 typed rows:
  alignment cadence + decision-escalation mechanism),
  STRUCTURING-COST-FRAME-with-dominant-error-risk-verdict (V-03 axis: pre-assessment
  block before Sub-section 1, names over-structuring + under-coordination risk,
  VERDICT names dominant error risk as cost frame conclusion).
  Aspirational denominator updated from /13 to /16.
  v6 -- added A-12/A-13 from R6 excellence signals:
  cost-delta-calibration-anchor (COST-DELTA CALIBRATION: block between ORG-ELEMENT
  REGISTER and roadmap; restates A-10 net delta; derives High/Medium/Low thresholds;
  emits CALIBRATION-ANCHOR: lines referenced by roadmap Probability Weight cells),
  charter-dissolution-conditions (Dissolves When: sixth field in every charter;
  specific and observable conditions only).
  Aspirational denominator updated from /11 to /13.
  v5 -- added A-10/A-11 from R5 excellence signals:
  net-cost-comparison-arithmetic-verdict-block (NET-COST-COMPARISON: block with
  flat cost / structure overhead / net delta arithmetic; verdict linked to delta sign),
  three-tier-evolution-roadmap (V-02: Capacity/Process/Strategic tiers with
  Observable Signal column, Probability Weight column, WATCH-FIRST declaration
  as re-assessment trigger form).
  Fixed C-02 rubric gap (V-03 finding): "ASCII org diagram" tightened to
  "box-drawing ASCII org diagram" with explicit box-drawing pass condition.
  Aspirational denominator updated from /9 to /11.
  v4 -- added A-08/A-09 from R4 excellence signals:
  cost-quantified-inertia-assessment (V-01 axis: 4-column cost table, cost-anchored
  pressure rating, cost-unit re-assessment trigger),
  prose-charter-format-with-preserved-field-compliance (V-02 axis: bold-label prose
  paragraphs maintaining all 5 fields including N-of-M Quorum).
  Aspirational denominator updated from /7 to /9.
  v3 -- added A-06/A-07 from R2 excellence signals:
  contract-section-code-traceability (V-01 A-03/A-04 evidence pattern),
  annotation-register-used-in-column (V-02 C-04/C-05 evidence pattern).
  Aspirational denominator updated from /5 to /7.
  v2 -- added A-03/A-04/A-05 from R1 excellence signals:
  adversarial-framing-before-mechanics, productive-flat-branch-action,
  exclusion-clause-in-template. Aspirational denominator updated from /3 to /5.
  v1 -- initial rubric with C-01 through C-05, R-01 through R-03, A-01/A-02.

"""

# Extract the body (everything from '# Scoring Rubric' onward)
body_start = v8.index('# Scoring Rubric')
body = v8[body_start:]

# Update formula denominator
body = body.replace('aspirational_pass/20 * 10)', 'aspirational_pass/22 * 10)')
body = body.replace('denominator /20)', 'denominator /22)')

# Add canonical zone lines to A-14, A-15, A-16 pass conditions
body = body.replace(
    '**Pass condition:** >= 1 labeled `UNCOVERED:` (or equivalent) citation present in Sub-section 3\n'
    'of the Inertia Assessment; citation identifies an ownerless function or decision class; citation\n'
    'is additive to -- not a substitute for -- the C-01 coordination failure evidence.',
    '**Canonical zone:** `SUB-SECTION-3`\n\n'
    '**Pass condition:** >= 1 labeled `UNCOVERED:` (or equivalent) citation present in Sub-section 3\n'
    'of the Inertia Assessment; citation identifies an ownerless function or decision class; citation\n'
    'is additive to -- not a substitute for -- the C-01 coordination failure evidence.'
)
body = body.replace(
    '**Pass condition:** Verdict is `CAN-OPERATE-FLAT` AND a labeled flat rhythm table is present;\n'
    'table is separate from the C-02 rhythm table; table contains >= 2 rows covering alignment\n'
    'cadence and decision mechanism; or criterion is N/A if verdict is `STRUCTURE-WARRANTED`.',
    '**Canonical zone:** `POST-VERDICT-BRANCH`\n\n'
    '**Pass condition:** Verdict is `CAN-OPERATE-FLAT` AND a labeled flat rhythm table is present;\n'
    'table is separate from the C-02 rhythm table; table contains >= 2 rows covering alignment\n'
    'cadence and decision mechanism; or criterion is N/A if verdict is `STRUCTURE-WARRANTED`.'
)
body = body.replace(
    '**Pass condition:** Labeled `STRUCTURING-COST FRAME:` (or equivalent) block present before\n'
    'Sub-section 1; block names over-structuring risk and under-coordination risk with >= 1 concrete\n'
    'consequence each; VERDICT declaration names the dominant error risk as an explicit conclusion.',
    '**Canonical zone:** `PRE-ASSESSMENT`\n\n'
    '**Pass condition:** Labeled `STRUCTURING-COST FRAME:` (or equivalent) block present before\n'
    'Sub-section 1; block names over-structuring risk and under-coordination risk with >= 1 concrete\n'
    'consequence each; VERDICT declaration names the dominant error risk as an explicit conclusion.'
)

new_criteria = """
### A-21 -- Sub-section 4 anchor ordering protocol
**Category:** correctness | **Weight:** aspirational

When `COST-FRAME CONCLUSION:` (A-18), `NET-COST-COMPARISON:` block (A-10), and `FLAT-CASE-PRESSURE:`
line (C-01) all co-occur in Sub-section 4, they must appear in the fixed linear order:
`COST-FRAME CONCLUSION:` line first, then `NET-COST-COMPARISON:` block immediately following,
then `FLAT-CASE-PRESSURE:` verdict line after the block closes. No other content may be inserted
between these three anchors. This converts an implicit expectation (that the cost frame grounds
the arithmetic, which grounds the verdict) into an independently verifiable positional constraint:
a reviewer can confirm the chain without parsing narrative semantics.

Documents where Sub-section 4 opens with `NET-COST-COMPARISON:` before `COST-FRAME CONCLUSION:`
fail this criterion, as do documents where prose or other labeled blocks appear between any two
of the three anchors.

**Pass condition:** `COST-FRAME CONCLUSION:` appears before `NET-COST-COMPARISON:` block; block
appears before `FLAT-CASE-PRESSURE:` line; no interceding content between any adjacent anchor
pair; or criterion is N/A if fewer than all three anchors are present in the document.

---

### A-22 -- Per-artifact inline zone label
**Category:** correctness | **Weight:** aspirational

When A-20 (INTEGRATION-NOTE) is active, each of the three positional artifacts (A-14, A-15,
A-16) carries its canonical zone designator as an inline label within the artifact's own
instruction block or section header -- not only in the INTEGRATION-NOTE summary. Zone assignment
is therefore readable at the artifact definition site without consulting the INTEGRATION-NOTE.
Canonical inline label formats: `[Zone: PRE-ASSESSMENT]`, `[Zone: SUB-SECTION-3]`,
`[Zone: POST-VERDICT-BRANCH]` (or equivalent explicit zone annotation). The inline label must
match the canonical designator used in A-20 exactly (no paraphrase, no abbreviation).

Inline zone labels serve a complementary function to A-20: the INTEGRATION-NOTE confirms global
disjointness by listing all three artifacts together; the inline labels ensure local readability
so that each artifact self-documents its positional contract at the point of definition.

**Pass condition:** A-20 active; each of A-14, A-15, and A-16 carries its canonical zone
designator as an inline label within the artifact's own block; labels match the A-20 canonical
designators exactly; or criterion is N/A if A-20 is not active.

---

**Formula update:** `aspirational_pass/20 * 10` => `aspirational_pass/22 * 10`

Golden threshold unchanged: 5/5 essential + composite >= 80.
"""

# Find the trailing formula update line and replace with A-21/A-22 + updated trailer
old_trailer = ('**Formula update:** `aspirational_pass/16 * 10` => `aspirational_pass/20 * 10`\n\n'
               'Golden threshold unchanged: 5/5 essential + composite >= 80.\n')
if old_trailer in body:
    body = body.replace(old_trailer, new_criteria)
else:
    # Just append
    body = body.rstrip() + '\n' + new_criteria

v9 = header + body
open(v9_path, 'w', encoding='utf-8').write(v9)
print('Written', len(v9), 'bytes')
print('A-21 present:', 'A-21' in v9)
print('A-22 present:', 'A-22' in v9)
print('denominator /22 present:', '/22' in v9)
