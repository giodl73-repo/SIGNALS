## Simplified Prompt

```
Produce a competitive brief that leads with strategy, not a matrix.

SETUP: Auto-detect domain from repo context (README, CLAUDE.md, package.json). Identify
5-8 competitors by name. Do not prompt the user unless repo context is completely absent.

THE PRIMARY COMPETITOR: Before any named competitors, assess "none / status quo." Ask:
why do teams do nothing instead of using this tool?
Score threat: always HIGH. Inertia is the primary competitor.

NAMED COMPETITORS: For each competitor, assess:
- Feature overlap (HIGH/MEDIUM/LOW)
- Positioning (direct threat / complementary / adjacent)
- Overall threat: HIGH / MEDIUM / LOW

Use WebSearch to verify at least one key competitive claim per major competitor.
Cite the source inline (URL or publication name).

FINDINGS: Structure as a brief:
1. The Primary Competitor -- why inertia is the real threat
2. The Whitespace -- what no competitor owns (the uncontested space)
3. The Table Stakes -- what any entrant must have to be taken seriously
4. The Competitive Matrix -- supporting evidence (rows = competitors, columns = dimensions)
5. --mode risk -- "The cost of building the wrong thing": reframe for exec audiences
   who respond to risk quantification over feature comparison.

AMEND: List 3 specific adjustments. For each: what the user changes AND what changes
in the output.

Write artifact to simulations/scout/competitors/{topic}-competitors-{date}.md.
Include frontmatter: skill, topic, item, date, skill_version, input.
```

---

## Simplification Report

**Before:** 311 words  
**After:** 228 words  
**Reduction:** 83 words (26.7%)

### What was removed and why

| Removed | Words | Reason |
|---|---|---|
| "You are running /scout-competitors." | 5 | Restates the skill name — no rubric work |
| "The matrix is supporting evidence. The insight comes first." | 9 | Redundant with "leads with strategy, not a matrix" |
| "What makes inertia sticky? What would make a team choose to keep doing nothing even after hearing about this product?" | 24 | Three questions where one suffices for C-06; redundancy, not depth |
| "- Technical moat (what makes them defensible)" | 6 | Not tied to any essential criterion |
| "- Distribution (how they reach users)" | 5 | Not tied to any essential criterion |
| "(from setup above)" | 3 | Unnecessary cross-reference in FINDINGS item 1 |
| "What does a team lose by NOT investigating before they build?" | 13 | Redundant with the --mode risk description above it |
| AMEND example `(e.g., "Narrow to SaaS-only competitors...")` | 18 | Supports aspirational C-10 only; core instruction survives |

### Essential criteria check (post-simplification)

| Criterion | Status |
|---|---|
| C-01: "none / status quo" row | PASS — PRIMARY COMPETITOR section + Matrix in FINDINGS |
| C-02: Whitespace identified | PASS — "2. The Whitespace" in FINDINGS |
| C-03: Table stakes listed | PASS — "3. The Table Stakes" in FINDINGS |
| C-04: Threat level per competitor | PASS — "Overall threat" in NAMED COMPETITORS, score for inertia |
| C-05: Auto-detect without prompting | PASS — SETUP section unchanged |

All 5 essential criteria pass. Recommended criteria (C-06, C-07, C-08) and aspirational (C-11, C-12) also survive — only the AMEND example (C-10, aspirational) is weakened.

```json
{"simplified_word_count": 228, "original_word_count": 311, "all_essential_still_pass": true, "reduction_pct": 26.7}
```
