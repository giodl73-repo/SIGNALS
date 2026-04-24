Scorecard written to `simulations/quest/scorecards/prove-websearch-scorecard-R1-2026-03-14.md`.

---

## Results Summary

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1 | V-05 Full Synthesis | **100** | YES |
| 2 | V-04 Template + Gates | **97.5** | YES |
| 3 | V-03 Phase Gates | **95** | YES |
| 4= | V-01 Template only | **85** | YES |
| 4= | V-02 Imperative register | **85** | YES |

All 5 variations pass golden threshold. Every variation covers all 5 essential criteria -- the differentiation is entirely in recommended (C-06/C-07) and aspirational (C-09/C-10).

**Key finding:** The 10-point gap between tier-2 (V-01/V-02, 85) and tier-3 (V-03, 95) is 100% attributable to phase gates. C-06 and C-07 go from PARTIAL to PASS when "do not proceed" checkpoints replace numbered steps -- those two recommended criteria are worth 20 combined points. V-04 vs V-05 comes down to a single 2.5-point question: whether the query refinement trail field is placed during search (PHASE 3, live observation) or after synthesis (PHASE 4, retrospective reconstruction).

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-gate-vs-step: explicit GATE checkpoints outperform numbered steps for C-06/C-07 because gates are structurally harder to skip under output pressure", "live-trail-placement: query refinement trail in PHASE 3 captures observed behavior vs PHASE 4 retrospective reconstruction", "gate-framing-names-target: naming what Q2 must attack (refutation side) in the gate itself prevents near-duplicate pro-hypothesis queries"]}
```
ced follow-up query if missing |
| C-08 | PASS | Pre-printed `Credibility:` field in every evidence block |
| C-09 | PASS | Pre-printed SYNTHESIS: Supporting/Refuting/Mixed table + Aggregate finding (2+ sources named) |
| C-10 | FAIL | Not addressed |

**Score: 85** (12+12+12+12+12+5+5+10+5+0)
All essential: YES | Golden: YES

---

### V-02: Imperative / Conversational Register

| C | Rating | Evidence |
|---|--------|---------|
| C-01 | PASS | Strong imperative: "If you can't find a URL, don't use it as evidence" |
| C-02 | PASS | "copy a direct quote. Use quotation marks." + pre-printed `"[Exact quote]"` format |
| C-03 | PASS | Step format: **Query used:**, **Sources:**, **Evidence from [URL]:** -- all 3 fields |
| C-04 | PASS | Pre-printed `Relevance:` |
| C-05 | PASS | Pre-printed `Strength:` |
| C-06 | PARTIAL | Q1/Q2/Q3 pre-planning step is explicit but ungated |
| C-07 | PARTIAL | Step 3 balance check + follow-up instruction present but no gate |
| C-08 | PASS | Pre-printed `Source type:` field |
| C-09 | PARTIAL | Step 4 synthesis is prose instruction ("write a short paragraph") -- no pre-printed sub-fields |
| C-10 | PARTIAL | Q1/Q2/Q3 list shows planned framings; no "original -> refined" trail field |

**Score: 85** (12+12+12+12+12+5+5+10+2.5+2.5)
All essential: YES | Golden: YES

---

### V-03: Explicit Phase Gates

| C | Rating | Evidence |
|---|--------|---------|
| C-01 | PASS | PHASE 2 header: "Every factual claim requires a URL -- no training-data evidence." |
| C-02 | PASS | Pre-printed `Quote: "[Verbatim text]"` in every evidence block |
| C-03 | PASS | SEARCH block per query with all 3 fields |
| C-04 | PASS | Pre-printed `Relevance:` |
| C-05 | PASS | Pre-printed `Strength:` |
| C-06 | PASS | GATE 1: "At least 2 queries with distinct framings. Do not proceed to PHASE 2 until met." |
| C-07 | PASS | GATE 3: balance verdict + ONE-SIDED escape with documented follow-up query |
| C-08 | PASS | Pre-printed `Credibility:` in every evidence block |
| C-09 | PASS | PHASE 4: Cross-source findings (Convergence/Conflict) + Aggregate conclusion (2+ URLs) |
| C-10 | FAIL | Not addressed -- design notes confirm "not explicitly addressed" |

**Score: 95** (12+12+12+12+12+10+10+10+5+0)
All essential: YES | Golden: YES

---

### V-04: Pre-Printed Template + Phase Gates

| C | Rating | Evidence |
|---|--------|---------|
| C-01 | PASS | Top-level rule: "Every factual claim must have a source URL. Do not use training data." |
| C-02 | PASS | Pre-printed `Quote:` with note "Do not paraphrase." |
| C-03 | PASS | SEARCH BLOCK: Query/Sources/Evidence Items -- all labeled and required |
| C-04 | PASS | Pre-printed `Relevance:` in every Evidence Item |
| C-05 | PASS | Pre-printed `Strength:` in every Evidence Item |
| C-06 | PASS | GATE 1: "At least Q1 and Q2 with distinct framings. Proceed to PHASE 2." |
| C-07 | PASS | GATE 3: Balance result field (BALANCED or ONE-SIDED + documented follow-up) |
| C-08 | PASS | Pre-printed `Credibility:` in every Evidence Item |
| C-09 | PASS | PHASE 4: Convergence/Conflict/Conclusion pre-printed fields |
| C-10 | PARTIAL | `Query refinement:` field exists but placed in PHASE 4 (retrospective, post-synthesis) |

**Score: 97.5** (12+12+12+12+12+10+10+10+5+2.5)
All essential: YES | Golden: YES

---

### V-05: Full Synthesis (All Axes)

| C | Rating | Evidence |
|---|--------|---------|
| C-01 | PASS | Rule 1: "Every factual claim needs a URL. Do not cite training data." + Source URL: field |
| C-02 | PASS | Rule 2: "Evidence means a verbatim quote." + Pre-printed `Quote:` field -- dual enforcement |
| C-03 | PASS | SEARCH BLOCK with Query string/Sources found/Evidence Items -- all required |
| C-04 | PASS | Pre-printed `Relevance:` in every Evidence Item |
| C-05 | PASS | Pre-printed `Strength:` in every Evidence Item |
| C-06 | PASS | GATE 1: Q1 and Q2 required; "Q2 explicitly targets the refutation side" -- target named in gate |
| C-07 | PASS | GATE 3: balance result + targeted follow-up if one-sided |
| C-08 | PASS | Pre-printed `Credibility:` in every Evidence Item |
| C-09 | PASS | PHASE 4: Convergence/Conflict/Overall conclusion with enumerated sub-requirements (3 sentences, 2 URLs, largest gap) |
| C-10 | PASS | Pre-printed `Query refinement trail:` in PHASE 3 -- placed during search (pre-synthesis), capturing live behavior |

**Score: 100** (12+12+12+12+12+10+10+10+5+5)
All essential: YES | Golden: YES

---

## Composite Ranking

| Rank | Variation | Score | All Essential | Golden | Key gap |
|------|-----------|-------|---------------|--------|---------|
| 1 | V-05 | 100 | YES | YES | None |
| 2 | V-04 | 97.5 | YES | YES | C-10 retrospective placement |
| 3 | V-03 | 95 | YES | YES | C-10 not addressed |
| 4 | V-01 | 85 | YES | YES | C-06 ungated, C-07 no follow-up gate, C-10 absent |
| 4 | V-02 | 85 | YES | YES | C-06/C-07 ungated, C-09 prose-only, C-10 no trail field |

All 5 variations meet golden threshold. Differentiation is entirely in recommended (C-06/C-07) and aspirational (C-09/C-10) tiers.

---

## Excellence Signals from V-05

**1. Phase gates beat numbered steps (C-06/C-07 gap).**
V-01 and V-02 have explicit instructions for multi-query and balance but score PARTIAL on both. V-03 through V-05 use "GATE: do not proceed" checkpoints and score PASS on both. Gates are structurally harder to skip under output pressure than numbered steps. The 10-point gap between V-02 (85) and V-03 (95) is entirely attributable to this mechanism.

**2. C-10 placement is load-bearing.**
V-04's `Query refinement:` field in PHASE 4 earns PARTIAL -- by the time PHASE 4 is reached, synthesis is written and refinement is reconstructed from memory rather than observed. V-05's `Query refinement trail:` in PHASE 3 (post-collection, pre-synthesis) is the only placement where the gap is visible and fresh. This 2.5-point difference distinguishes first from second place.

**3. Gate framing names the target.**
V-05's GATE 1 specifies "Q2 explicitly targets the refutation side" -- not just "distinct framing." This prevents a model from writing two slightly different pro-hypothesis queries and satisfying the letter of "2 distinct queries." Naming the target in the gate closes a semantic loophole that V-03 and V-04 leave open.

**4. Pre-printed synthesis sub-fields over prose instruction.**
V-01 and V-02 have synthesis sections but rely on prose instruction ("write a paragraph naming two sources"). V-03 through V-05 use pre-printed Convergence/Conflict/Conclusion fields. C-09 scores PASS for all five but the structural version is more reliable -- a model must produce three distinct sub-answers rather than a single paragraph that could address only one.

**5. Rules enumerated before content fields.**
V-05 opens with numbered rules (1-4) before Topic/Hypothesis. Rule-first order ensures constraints are parsed before content is seen, reducing the chance rules are glossed over mid-execution.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-gate-vs-step: explicit GATE checkpoints outperform numbered steps for C-06/C-07 because gates are structurally harder to skip under output pressure", "live-trail-placement: query refinement trail in PHASE 3 captures observed behavior vs PHASE 4 retrospective reconstruction", "gate-framing-names-target: naming what Q2 must attack (refutation side) in the gate itself prevents near-duplicate pro-hypothesis queries"]}
```
