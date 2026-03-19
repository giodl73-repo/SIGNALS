"""Build flow-throttle-rubric-v7-2026-03-15.md from v6 source."""

import re

v6_path = "C:/src/sim/simulations/quest/rubrics/flow-throttle-rubric-v6-2026-03-15.md"
v7_path = "C:/src/sim/simulations/quest/rubrics/flow-throttle-rubric-v7-2026-03-15.md"

v6 = open(v6_path, encoding="utf-8").read()

# ── v7 changelog header ──────────────────────────────────────────────────────

V7_HEADER = """\
# flow-throttle Rubric -- v7

---

## What changed in v7

**Three new aspirational criteria from Round 7, denominator 14 -> 17:**

---

**C-23 -- Volume arithmetic pre-computation** (format/correctness)

Elevated from R7 V-01's VOLUME ARITHMETIC section. Before TABLE A is populated, a named volume
arithmetic block computes the 1x baseline request rate with explicit units and derives the 2x
and 5x values referenced in TABLE A STATUS columns. Without pre-computation, each tier author
can implicitly choose their own baseline, producing internally inconsistent STATUS entries; LOAD
SHAPE comparisons lack a common numeric anchor. With VOLUME ARITHMETIC established first, the
STATUS column becomes self-enforcing: a column where all three band entries are identical is
structurally suspicious and can be flagged inline ("if all identical, VOLUME ARITHMETIC was not
used").

**Pass condition:** A named VOLUME ARITHMETIC section (or equivalent block) appears before TABLE
A and specifies: (a) the 1x baseline request rate with explicit units (req/min, req/sec, etc.),
(b) derived 2x and 5x values, and (c) a unit conversion where the rate limit type and the
baseline use different time granularities. TABLE A STATUS columns reference these computed
values. A bare volume figure embedded in a prose preamble without a named section does not pass.

---

**C-24 -- Cross-section tier-ID coverage audit** (format)

Elevated from R7 V-02's TIER-ID COVERAGE AUDIT structure. C-12 requires identifier consistency
(no synonyms, no unmatchable names) but does not require that every tier established in TABLE A
appears in every downstream section. The coverage audit enforces downstream representation: for
each T-NN in TABLE A, a matrix or equivalent structure checks its presence in TABLE B
(propagation), TABLE C (UX), TABLE D (burst paths), TABLE E (test gaps), and TABLE F
(mitigations). A tier absent from a downstream section is an explicit coverage gap made visible
by the audit structure rather than a silent omission that passes C-12 on identifier grounds
alone.

**Pass condition:** A named coverage audit section (or equivalent per-tier per-section matrix)
appears after the full analysis and verifies T-NN presence in each downstream section. At least
one absence, if it exists, is called out explicitly as a coverage gap. A prose assertion that
"all tiers are covered" without a per-tier per-section matrix does not satisfy this criterion.

---

**C-25 -- Counterfactual harm column in mitigation registry** (depth)

Elevated from R7 V-03's TABLE F `Without this change (at 2x nominal)` column. A mitigation list
without counterfactuals is a recommendation; a mitigation list with counterfactuals is a risk
register. The column requires a named failure scenario at a specific volume multiplier: the
component that degrades or fails, the failure mode, and the threshold at which it occurs. This
makes urgency explicit -- the reader sees the consequence of not acting rather than inferring it
from the mitigation description. The column also requires a `Source` field tracing each
mitigation back to its Tier-ID or Path-ID, completing the traceability chain from TABLE A
through TABLE F.

**Pass condition:** The mitigation registry includes a column or field for the failure scenario
that results from not implementing the mitigation, stated at a named volume multiplier (e.g.,
"at 2x nominal"). Each entry names: (a) the component or tier affected, (b) the failure mode,
and (c) a threshold or volume reference. Generic entries ("throttle errors will increase") do
not pass; named component + failure mode + threshold passes. A `Source` column tracing each row
to a Tier-ID or Path-ID is also required.

---

**Scoring impact:**

| Variation | Axes | v6 score | v7 score |
|-----------|------|----------|----------|
| V-01 | C-23 only | 100 | **98** |
| V-02 | C-24 only | 100 | **98** |
| V-03 | C-25 only | 100 | **98** |
| V-04 (projected) | C-23 + C-24 | 100 | **99** |
| V-05 (projected) | C-23 + C-24 + C-25 | 100 | **100** |

Each single-axis variation misses two of the three new criteria (15/17 aspirational). A
variation carrying all three reaches 100. 100 remains achievable.

---

"""

# ── three new criterion rows ─────────────────────────────────────────────────

C23 = (
    "| C-23 | **Volume arithmetic pre-computation** -- Before TABLE A is populated, a named "
    "VOLUME ARITHMETIC section computes the 1x baseline request rate with explicit units and "
    "derives the 2x and 5x values referenced in TABLE A STATUS columns. Without pre-computation, "
    "each tier author can implicitly choose their own baseline, producing internally inconsistent "
    "STATUS entries; LOAD SHAPE comparisons lack a common numeric anchor. With VOLUME ARITHMETIC "
    "established first, the STATUS column becomes self-enforcing: a column where all three band "
    "entries are identical is structurally suspicious and can be flagged inline. | format | "
    "aspirational | A named VOLUME ARITHMETIC section (or equivalent block) appears before TABLE "
    "A and specifies: (a) the 1x baseline request rate with explicit units, (b) derived 2x and "
    "5x values, and (c) a unit conversion where the rate limit type and the baseline use different "
    "time granularities. TABLE A STATUS columns reference these computed values. A bare volume "
    "figure embedded in a prose preamble without a named section does not pass. *Round 7 "
    "excellence signal: V-01 VOLUME ARITHMETIC pre-computation established a single arithmetic "
    "ground truth before any tier analysis; the STATUS column annotation (\"if all identical, "
    "VOLUME ARITHMETIC was not used\") made the multi-volume sweep of C-11 structurally "
    "self-enforcing rather than instructionally enforced. V-02 and V-03 inherit C-11 from the "
    "baseline but lack the arithmetic anchor; V-04 and V-05 would inherit C-23 from V-01.* |"
)

C24 = (
    "| C-24 | **Cross-section tier-ID coverage audit** -- After the full analysis is complete, a "
    "named coverage audit section (or equivalent per-tier per-section matrix) verifies that every "
    "T-NN identifier established in TABLE A appears in each downstream section: TABLE B "
    "(propagation), TABLE C (UX), TABLE D (burst paths), TABLE E (test gaps), and TABLE F "
    "(mitigations). C-12 enforces identifier consistency within each section; C-24 enforces "
    "downstream representation -- a tier absent from a section is a coverage gap made structurally "
    "visible rather than a silent omission that passes C-12 on identifier grounds alone. | format | "
    "aspirational | A named coverage audit section (or equivalent matrix) verifies T-NN presence "
    "across all downstream sections and appears after the full analysis. At least one absence, "
    "where it exists, is called out explicitly as a coverage gap rather than a silent omission. "
    "A prose assertion that \"all tiers are covered\" without a per-tier per-section matrix does "
    "not satisfy this criterion. *Round 7 excellence signal: V-02 TIER-ID COVERAGE AUDIT verified "
    "T-NN presence section-by-section; the inline annotation \"The reason: C-12 ensures identifier "
    "consistency but does not enforce downstream representation\" distinguishes C-24 from the C-12 "
    "traceability requirement. V-01 and V-03 inherit C-12 but lack the audit structure; V-04 and "
    "V-05 would inherit C-24 from V-02.* |"
)

C25 = (
    "| C-25 | **Counterfactual harm column in mitigation registry** -- The mitigation registry "
    "(TABLE F or equivalent) includes a column or field naming the failure scenario that results "
    "from not implementing each mitigation, stated at a named volume multiplier. A mitigation list "
    "without counterfactuals is a recommendation; a mitigation list with counterfactuals is a risk "
    "register -- the column makes urgency explicit. A `Source` field tracing each mitigation back "
    "to its Tier-ID or Path-ID is also required, completing the traceability chain from TABLE A "
    "through TABLE F. | depth | aspirational | Each entry in the mitigation registry includes: "
    "(a) the component or tier affected by inaction, (b) the failure mode, and (c) a threshold or "
    "volume reference (e.g., \"at 2x nominal\"). Generic entries (\"throttle errors will increase\") "
    "do not pass; named component + failure mode + threshold passes. A `Source` column linking each "
    "row to a Tier-ID or Path-ID is required. *Round 7 excellence signal: V-03 TABLE F `Without "
    "this change (at 2x nominal)` column elevated the mitigation section to a risk register; the "
    "adjacent WRONG/PASS contrast (\"Throttle errors will increase\" WRONG -> named component + "
    "failure mode + threshold PASS) made the specificity requirement self-enforcing. V-01 and V-02 "
    "inherit TABLE F from the baseline but lack the counterfactual column; V-04 and V-05 would "
    "inherit C-25 from V-03.* |"
)

# ── updated scoring worksheet and formula ────────────────────────────────────

SCORING = """\

---

## Scoring Worksheet

| Criterion | Tier | Pass? (Y/N) | Notes |
|-----------|------|-------------|-------|
| C-01 Bottleneck sequencing | essential | | |
| C-02 Backpressure propagation | essential | | |
| C-03 UX per tier | essential | | |
| C-04 Unprotected burst path | essential | | |
| C-05 Quantified limits | essential | | |
| C-06 Retry-after handling | recommended | | |
| C-07 Cascade failure scenario | recommended | | |
| C-08 Throttle tier matrix | recommended | | |
| C-09 Mitigation prescriptions | aspirational | | |
| C-10 Load shape sensitivity | aspirational | | |
| C-11 Multi-volume sweep | aspirational | | |
| C-12 Cross-section tier traceability | aspirational | | |
| C-13 Test coverage gap identification | aspirational | | |
| C-14 Test infrastructure inertia catalog | aspirational | | |
| C-15 Labeled gap entry completeness | aspirational | | |
| C-16 Negative exemplar contrast injection | aspirational | | |
| C-17 Stage-boundary completion declaration | aspirational | | |
| C-18 Load shape null-case grounding | aspirational | | |
| C-19 Multi-section exemplar coverage | aspirational | | |
| C-20 Instruction-adjacent rationale annotation | aspirational | | |
| C-21 Section-adjacent inertia callout placement | aspirational | | |
| C-22 Dual-role execution sequence | aspirational | | |
| C-23 Volume arithmetic pre-computation | aspirational | | |
| C-24 Cross-section tier-ID coverage audit | aspirational | | |
| C-25 Counterfactual harm column | aspirational | | |

```
essential_pass    = sum(C-01..C-05 pass) / 5
recommended_pass  = sum(C-06..C-08 pass) / 3
aspirational_pass = sum(C-09..C-25 pass) / 17

composite = (essential_pass * 60) + (recommended_pass * 30) + (aspirational_pass * 10)
golden    = all essential pass AND composite >= 80
```

---

## Round 7 Score Reference

| Variation | Axes | Aspirational pass | Composite | Score |
|-----------|------|-------------------|-----------|-------|
| V-01 | Volume arithmetic pre-computation (C-23) | C-09..C-22 + C-23 = 15/17 | 98.82 | **98** |
| V-02 | Cross-section tier-ID coverage audit (C-24) | C-09..C-22 + C-24 = 15/17 | 98.82 | **98** |
| V-03 | Counterfactual harm column (C-25) | C-09..C-22 + C-25 = 15/17 | 98.82 | **98** |

Each single-axis variation carries exactly one of the three new criteria and misses the other
two (15/17 aspirational). A variation carrying all three reaches 17/17 and scores 100.

## Round 6 Score Reference

| Variation | Axes | Aspirational pass | Composite | Score |
|-----------|------|-------------------|-----------|-------|
| V-01 | WHY-first register (C-20) | C-09..C-19 + C-20 = 12/14 | 98.57 | **98** |
| V-02 | Distributed inertia (C-21) | C-09..C-19 + C-21 = 12/14 | 98.57 | **98** |
| V-03 | Dual-role sequence (C-22) | C-09..C-19 + C-22 = 12/14 | 98.57 | **98** |
| V-04 | WHY-first + distributed inertia (C-20 + C-21) | C-09..C-21 = 13/14 | 99.29 | **99** |
| V-05 | V-04 + dual-role (all 14) | C-09..C-22 = 14/14 | 100 | **100** |
"""

# ── assemble ─────────────────────────────────────────────────────────────────

# Extract from v6: everything starting at "## What changed in v6" up to the
# old Scoring Worksheet marker.
v6_changelog_start = v6.find("## What changed in v6")
assert v6_changelog_start != -1, "Could not find v6 changelog marker"

old_scoring_marker = "\n---\n\n## Scoring Worksheet"
old_scoring_start = v6.find(old_scoring_marker, v6_changelog_start)
assert old_scoring_start != -1, "Could not find old scoring worksheet"

# v6 body = changelog + essential + recommended + aspirational tables (C-09..C-22)
v6_body = v6[v6_changelog_start:old_scoring_start]

# The aspirational table in v6 ends with the C-22 row followed by a blank line and ---
# We append the three new rows right after C-22.
c22_row_end = v6_body.rfind("| C-22 |")
assert c22_row_end != -1, "Could not find C-22 row"
# Advance past the C-22 row to end of line
c22_row_end = v6_body.find("\n", c22_row_end) + 1  # position after newline

v6_body_before_c22_end = v6_body[:c22_row_end]
v6_body_after_c22_end  = v6_body[c22_row_end:]

final = (
    V7_HEADER
    + v6_body_before_c22_end
    + C23 + "\n"
    + C24 + "\n"
    + C25 + "\n"
    + v6_body_after_c22_end
    + SCORING
)

with open(v7_path, "w", encoding="utf-8") as f:
    f.write(final)

print(f"Written {len(final)} bytes to {v7_path}")

# Quick sanity checks
assert "## What changed in v7" in final
assert "C-23" in final
assert "C-24" in final
assert "C-25" in final
assert "aspirational_pass = sum(C-09..C-25 pass) / 17" in final
assert "Round 7 Score Reference" in final
print("All assertions passed.")
