v9 = open('C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v9-2026-03-15.md', 'r').read()
lines = v9.split('\n')
start = next(i for i, l in enumerate(lines) if l.strip() == '## What changed in v9')
v9_body = '\n'.join(lines[start:])

v10_header = """# trace-state rubric -- v10 (2026-03-15)

---

## What changed in v10

One new criterion extracted from R11 V-04 excellence signal:

| ID | Criterion | Source | Signal |
|----|-----------|--------|--------|
| **C-27** | Named failure-mode baseline | R11 V-04 INERTIA BASELINE section | "Every section that is skipped or left as a placeholder IS a return to the inertia baseline" -- a named failure-mode anchor that reframes completeness as deviation from a declared baseline state, not mere compliance with individual constraints |

**Scoring: 20 aspirational criteria, `aspirational_pass/20 x 10`, 0.50 pts per PASS, 0.25 pts per PARTIAL.**

| Variant | v9 score | C-27 | v10 score | Tier |
|---------|----------|------|-----------|------|
| R11 V-01 | 99.27 (PARTIAL C-24) | FAIL | **98.75** | Golden |
| R11 V-02 | 99.47 | FAIL | **99.00** | Golden |
| R11 V-03 | 100.00 | FAIL | **99.50** | Golden |
| R11 V-04 | 100.00 | PASS | **100.00** | Ceiling |
| R10 V-01 | 98.95 | FAIL | **98.50** | Golden |
| R10 V-02 | 98.95 | FAIL | **98.50** | Golden |
| R10 V-03 | 97.89 | FAIL | **97.50** | Excellent |

Note: R11 V-03 drops from Ceiling to Golden under v10 -- it achieves all 19 prior criteria
but lacks the INERTIA BASELINE section. R11 V-04 is the first variant to achieve 100.00
under v10 with all 20 aspirational criteria satisfied.

**C-27** is the defining addition of v10. It requires a named failure-mode baseline -- a
dedicated preamble declaration that names the incomplete state the document exists to
escape. R11 V-04 achieves this with an INERTIA BASELINE section stating "Every section
that is skipped or left as a placeholder IS a return to the inertia baseline." This
reframes completeness as positive deviation from a named failure state rather than
compliance with a list of prohibitions. No prior variant includes this pattern.

**Scoring changes:**
- 20 aspirational criteria, 0.50 pts per PASS, 0.25 pts per PARTIAL (10 pts total)
- Formula: `aspirational_pass/20 x 10`
- Ceiling: 20/20 = 10.00 pts aspirational, composite 100.00 -- achieved by R11 V-04
- R11 V-04: 20/20 (100.00, Ceiling); R11 V-03: 19/20 (99.50, Golden);
  R11 V-02: 18/20 (99.00, Golden); R11 V-01: 17/20 + 1 PARTIAL (98.75, Golden)

**Tier boundaries (composite score):**
- **Ceiling**: 100.00 (all 20 aspirational criteria PASS)
- **Golden**: >= 98.50
- **Excellent**: >= 97.50
- **Below Excellent**: < 97.50

---

## Scoring verification against Round 11 (under v10)

Aspirational criteria use 0.50 pts per PASS, 0.25 pts per PARTIAL.
Exact formula: `aspirational_pass/20 x 10`.

| Variant | C-24 | C-25 | C-26 | C-27 | Aspirational (v10) | Composite |
|---------|------|------|------|------|--------------------|-----------|
| R11 V-01 | PARTIAL | PASS | FAIL | FAIL | 17P+1PART = 8.75 | 98.75 |
| R11 V-02 | FAIL | PASS | PASS | FAIL | 18/20 x 10 = 9.00 | 99.00 |
| R11 V-03 | PASS | PASS | PASS | FAIL | 19/20 x 10 = 9.50 | 99.50 |
| R11 V-04 | PASS | PASS | PASS | PASS | 20/20 x 10 = 10.00 | 100.00 |

R11 V-04 full (v10): C-08 PASS, C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS,
C-14 PASS, C-15 PASS, C-16 PASS, C-17 PASS, C-18 PASS, C-19 PASS, C-20 PASS,
C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS, C-26 PASS, C-27 PASS = 20 PASS.
20/20 x 10 = 10.00. Composite: 100.00. Ceiling.

R11 V-03 full (v10): C-08..C-26 all PASS, C-27 FAIL = 19 PASS.
19/20 x 10 = 9.50. Composite: 99.50. Golden.

R11 V-02 full (v10): C-08..C-23 PASS, C-24 FAIL, C-25 PASS, C-26 PASS, C-27 FAIL = 18 PASS.
18/20 x 10 = 9.00. Composite: 99.00. Golden.

R11 V-01 full (v10): C-08..C-23 PASS, C-24 PARTIAL, C-25 PASS, C-26 FAIL, C-27 FAIL
= 17 PASS + 1 PARTIAL. (17 x 0.50) + (1 x 0.25) = 8.75. Composite: 98.75. Golden.

---

## Scoring verification against Round 10 (retroactive under v10)

R10 variants under v10: C-27 requires an INERTIA BASELINE section. No R10 variant
includes this pattern. All R10 variants fail C-27.

| Variant | C-22 | C-23 | C-24 | C-25 | C-26 | C-27 | Aspirational (v10) | Composite |
|---------|------|------|------|------|------|------|--------------------|-----------|
| R10 V-01 | PASS | PASS | FAIL | PASS | FAIL | FAIL | 17/20 x 10 = 8.50 | 98.50 |
| R10 V-02 | PASS | FAIL | PASS | FAIL | PASS | FAIL | 17/20 x 10 = 8.50 | 98.50 |
| R10 V-03 | FAIL | PASS | PASS | FAIL | FAIL | FAIL | 15/20 x 10 = 7.50 | 97.50 |

R10 V-01 and V-02 Golden under v10 (98.50). R10 V-03 Excellent under v10 (97.50).

---

## Scoring verification against Round 9 (retroactive under v10)

R9 variants lack HANDOFF DECLARATION (C-22), vocabulary-locked handoff gate (C-25),
post-handoff role-state flip (C-26), and INERTIA BASELINE (C-27).

| Variant | C-25 | C-26 | C-27 | Aspirational (v10) | Composite |
|---------|------|------|------|--------------------|-----------|
| R9 V-01 | FAIL | FAIL | FAIL | 15/20 x 10 = 7.50 | 97.50 |
| R9 V-02 | FAIL | FAIL | FAIL | 15/20 x 10 = 7.50 | 97.50 |
| R9 V-03 | FAIL | FAIL | FAIL | 15/20 x 10 = 7.50 | 97.50 |

All R9 variants Excellent under v10.

---

"""

c27_criterion = """
---

### C-27 . Named failure-mode baseline
- **Weight**: aspirational
- **Category**: structure
- **Text**: A named section or inline declaration early in the document identifies
  the structural failure state the trace exists to escape. The failure-mode
  baseline is given a stable name (e.g., INERTIA BASELINE) and is defined in
  terms of the document's own completeness: any section that is skipped,
  abbreviated, or left as a placeholder constitutes a regression to the named
  baseline. The declaration inverts the framing of completeness -- rather than
  listing what must be done, it names what a partial document already is.
  R11 V-04 achieves this with an INERTIA BASELINE section and the declaration
  "Every section that is skipped or left as a placeholder IS a return to the
  inertia baseline." This makes the cost of omission visible at the structural
  level before any output sections begin.
  This is distinct from C-16 (numbered constraint preamble, which lists
  prohibitions but does not name a failure-mode anchor state), C-12 (hard-stop
  phrasing, which blocks forward progress but does not characterize the failure
  state that results from a skip), and C-10/C-20 (gates, which enforce
  sequencing but do not define what incompleteness means at the document level):
  C-27 requires a named failure-mode baseline that gives semantic content to
  incompleteness -- skipping a section is not merely a constraint violation, it
  is a return to a declared named state.
- **Pass condition**: A named section or inline declaration (labeled INERTIA
  BASELINE, FAILURE-MODE BASELINE, or equivalent stable name) appears in the
  preamble or opening section of the document before any output sections begin.
  It defines the structural failure state the document exists to prevent. It
  explicitly states that any skipped or placeholder section constitutes a return
  to that baseline. The declaration must be positional -- appearing before the
  first output section, not inline within a gate or constraint entry. A
  constraint that says "do not skip sections" without naming a failure-mode
  baseline state does not satisfy this criterion. A gate that blocks a section
  without defining what a skip means at the document level does not satisfy
  this criterion.
"""

# Find where Essential Criteria begins in v9 body
ess_idx = v9_body.find('## Essential Criteria')
v9_history = v9_body[:ess_idx].rstrip()
v9_criteria = v9_body[ess_idx:]

# Update aspirational section header for v10 point values
v9_criteria_updated = v9_criteria.replace(
    '## Aspirational Criteria (10 pts total -- 0.53 pts each)',
    '## Aspirational Criteria (10 pts total -- 0.50 pts per PASS, 0.25 pts per PARTIAL)'
)

full_v10 = v10_header + v9_history + '\n\n---\n\n' + v9_criteria_updated.rstrip() + c27_criterion

with open('C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v10-2026-03-15.md', 'w') as f:
    f.write(full_v10)

print('Written. Lines:', len(full_v10.split('\n')), '/ Size:', len(full_v10), 'bytes')
