Looks clean. The file is coherent. Now I can write the report.

---

## Simplified Prompt

The simplified prompt is written to `simulations/quest/golden/trace-component-QU5-simplified-2026-03-15.md`.

---

## Simplification Report

**Before**: 2316 words  
**After**: 1853 words  
**Reduction**: 20.0% (463 words removed)

### What was removed and why

| Removed | Words | Reason |
|---|---|---|
| NQ-1 second sub-question ("What justifies that particular stance...") | 12 | The primary question (epistemic stance) drives schema content; the justification clause is elaboration |
| NHQ-2 original (identity + parseable line question) | 35 | Collapsed into NHQ-2 = former NHQ-3; the compound-header insight is fully covered by NHQ-1; the "parseable property" angle from old NHQ-2 is implicit in Area 3 authoring |
| NHQ-3 compressed into NHQ-2 | 70 | Retained full Version A/B distinction and independent-verification question; removed redundant setup sentences that restated the column-presence requirement twice |
| DQ-1 second clause ("what does the code assert...") | 20 | The epistemic-relationship framing already implies what the code asserts; schema authors can derive it from the question stem |
| DQ-2 verbose framing | 14 | Reframed as a direct question; "self-contradictory at production time vs review time" distinction preserved |
| DQ-4 redundant phrasing | 15 | "An agent satisfies one requirement" clause removed; the untenable-claim question is self-contained |
| DQ-5 cognitive-status clause | 25 | "What is the difference in cognitive status between..." clause is a restatement of the core question |
| Role 2 Enforcement Rationale reminder sentence | 35 | Already enforced by Area 3 enforcement rules in the schema template |
| Role 2 "Both constraints must be satisfied" reminder | 12 | Already driven by DQ-3/DQ-4 reasoning; Area 3 dual-constraint form is self-enforcing |
| Area 3 enforcement rule: example affirmations | 15 | "ensures the required form", "satisfies compliance", "enforces the standard" examples removed; the rule's meaning is clear without them |
| Area 3 table cell parenthetical examples | 30 | "(e.g., single-requirement form, positional claim alone...)" removed from both Enforcement Rationale hint cells; "derive from DQ-N" is sufficient |
| Phase vocabulary example terms × 5 manifests | 29 | "e.g., SyntheticEvent, addEventListener" etc. removed from each manifest; "minimum two framework-specific terms" is self-explanatory |
| Area 5 type hint elaborations | 25 | Long parenthetical examples in each gate-type definition cell removed; brief scope labels retained |
| Area 5 "Additional types" sentence | 15 | Removed; gate discipline is established by the vocabulary table itself |
| Schema phase instruction tightened | 7 | "Author it in your own words from your" → "from your" |
| CAUSAL PHASE gate tightened | 10 | "or format cues" removed; "No schema structure" covers the intent |
| Inert-hop zero case compressed | 11 | Long zero-case sentence replaced with "No inert hops detected" |
| Zero-mutation inherited clause | 8 | "-- no effects, subscriptions, or watchers triggered" removed; "none" is sufficient |
| Role intro tightened | 7 | "You have two roles. Complete Role 1 fully before beginning Role 2." → "Complete Role 1 before Role 2." |
| Framework Declaration cell hints | 15 | "[from your TRAVERSAL-SCHEMA Area 1]" × 3 → "[Area 1]" × 3 |

### Criteria verification

All essential criteria preserved:
- **C-01–C-05** (blank-blocked): TABLE-1 through TABLE-6 structures unchanged
- **C-30** (Mutation Count Dual-Track): `N=___ direct, M=___ inherited` pre-declaration intact; Type column in TABLE-3 intact
- **C-31** (Schema-Field Coverage C-20–C-29): TABLE-8 with all 8 criteria → schema field mappings intact
- **C-32** (Blank-Blocked Field Primacy): All 5 essential tables retain blank-blocked columns
- **C-59** (Schema-Artifact Comparison Column Independence): NHQ-2 retains the Version A/B distinction and independent-verification question; Area 3 enforcement rule retains "verifier with only the schema" language
- **C-60** (Gate-Block Semantic Type Annotation): Area 5 vocabulary table + gate-block format instruction intact
- **C-61** (Per-Phase Vocabulary in Manifest): PHASE VOCABULARY field in all 5 manifests, minimum-two instruction intact

```json
{"simplified_word_count": 1853, "original_word_count": 2316, "all_essential_still_pass": true, "reduction_pct": 20.0}
```
