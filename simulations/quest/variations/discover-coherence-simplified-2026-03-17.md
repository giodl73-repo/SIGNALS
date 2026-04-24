---

## Simplification Report

### What was removed (11 cuts, 106 words)

| # | Removed text | Words | Reason |
|---|---|---|---|
| 1 | Preamble paragraph ("Before you commit to a spec...") | 44 | No rubric criterion requires a skill purpose description; STEP labels + column rules define all three axes |
| 2 | `(read everything -- emit nothing)` from STEP 2 header | 5 | Redundant — "Do not emit any output." at end of STEP 2 already enforces this |
| 3 | `determine product strategy viability against the status quo --` in inertia motivation | 11 | Rationale; the structural rule "render first regardless of count" is sufficient |
| 4 | `(machine-parseable, directly runnable)` from BLOCKING header | 4 | Descriptive qualifier, not a structural constraint |
| 5 | `-- reader must see what each signal said without opening the source files` from Claim rule | 13 | Rationale for "specific conflicting statement in its own words," which is already sufficient for C-02 |
| 6 | `(no token required)` from ADVISORY header | 3 | Implied by the BLOCKING section explicitly requiring a token |
| 7 | Second BLOCKING wrong example (`"Investigate the discrepancy"`) | 9 | Vagueness already covered by ADVISORY `Not acceptable: "investigate further"` |
| 8 | `See rows marked \`blocking\` above.` from readiness verdict | 5 | Pointer with no criterion backing; the blocking rows are already labeled in the table |
| 9 | `Correct: "Resolve with: /discover-inertia --focus switching-cost"` | 8 | The format template line (`/{skill-name} [--focus {parameter}]`) already specifies the correct form |
| 10 | `-- fails C-16` from wrong example comment | 3 | Rubric criterion ID is not meaningful to the LLM at runtime |
| 11 | `Filling each column:` label | 3 | Structural label with no criterion; column rules follow directly with their names |

### Criteria verification

All 17 rubric criteria verified intact:

| Criterion | Enforced by | Status |
|---|---|---|
| C-01 Gate check | STEP 1 GATE block | ✓ |
| C-02 Side-by-side quotes | "specific conflicting statement in its own words" | ✓ |
| C-03 Type taxonomy | `rating-conflict \| prediction-conflict \| evidence-conflict -- no other values` | ✓ |
| C-04 Severity classification | `blocking \| advisory -- no other values` | ✓ |
| C-05 Cross-skill | "Skill A and Skill B must be different discover skills" | ✓ |
| C-06 Tally before first entry | STEP 3 header block comes before STEP 4 tables | ✓ |
| C-07 Readiness verdict | M=0/M>=1 branches | ✓ |
| C-08 Summary line | "Compared: ... Inertia: ... Other: ..." | ✓ |
| C-09 Type column exact values | `rating-conflict \| prediction-conflict \| evidence-conflict` | ✓ |
| C-10 Skill reference for blocking | token format `/skill-name` | ✓ |
| C-11 Concrete advisory action | "Name a field to update, claim to amend, or skill to run" + example | ✓ |
| C-12 No vague resolutions | Wrong example (no slash) + ADVISORY "Not acceptable" | ✓ |
| C-13 Inertia section first | Inertia table + inertia flag in STEP 2 | ✓ |
| C-14 Empty inertia table rendered | "even if empty" | ✓ |
| C-15 Two-phase scan | STEP 2 (do not emit) → STEP 3 (tally before table) | ✓ |
| C-16 Exact token format | `"Resolve with: /{skill-name} [--focus {parameter}]"` + wrong example | ✓ |
| C-17 Artifact write | "Write to simulations/discover/coherence/..." + frontmatter | ✓ |

### Word counts

- **Original V-05**: 529 words  
- **Simplified**: 423 words  
- **Removed**: 106 words (20.0%)

```json
{"simplified_word_count": 423, "original_word_count": 529, "all_essential_still_pass": true}
```
