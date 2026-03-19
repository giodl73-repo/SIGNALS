**validate-inertia R18 -- scored. 5/5 match. Zero prediction errors.**

---

## Results

| Variation | C-45 | C-46 | C-47 | C-48 | Score | Predicted | Match |
|-----------|------|------|------|------|-------|-----------|-------|
| V-86 (ceiling) | PASS | PASS | PASS | PASS | **480** | 480 | YES |
| V-87 (no FAIL disqualifier) | PASS | PASS | FAIL | PASS | **470** | 470 | YES |
| V-88 (PARTIAL paths merged) | PASS | PASS | PASS | PARTIAL | **475** | 475 | YES |
| V-89 (baseline re-scored) | PASS | PASS | FAIL | PARTIAL | **465** | 465 | YES |
| V-90 (gap: disqualifier-only naming) | FAIL | PASS | PASS | PASS | **470** | 470 | YES |

---

## Key Scoring Decisions

**V-90 C-45 FAIL** -- The block opens with "has a completion requirement governing how..." rather than "has two functions serving structurally distinct roles." Function names appear only in disqualifier sentences, never as a positive duality assertion. Disqualifier-context-only naming does not satisfy C-45.

**V-89 C-48 PARTIAL** -- Two separate sentences present but framed as outcome descriptions ("earns partial credit") rather than explicit disqualifiers ("is a separate disqualifier"). C-48 pass requires "distinct disqualifiers" -- descriptive framing earns PARTIAL. This reveals a gap: the rubric's C-48 PARTIAL definition covers only the merged "or" shape (V-88), not the two-sentences-without-disqualifier-framing shape (V-89). Both earn 5 pts via structurally different mechanisms.

---

```json
{"top_score": 480, "all_essential_pass": true, "new_patterns": ["C-48 PARTIAL has two distinct structural shapes: (a) merged or-condition (V-88 shape) and (b) two separate sentences using descriptive outcome language without explicit disqualifier framing (V-89 shape) -- the rubric currently describes only shape (a) as earning PARTIAL, leaving shape (b) undocumented", "V-90 confirms the disqualifier-context-only naming pattern: function names appearing exclusively in FAIL/PARTIAL disqualifier sentences (never in a positive duality declaration) satisfies C-47 and C-48 but fails C-45 -- same predicted score as V-87 (470) via orthogonal structural failure mode"]}
```
ualifiers in block body

**PASS (10 pts) -- V-86, V-87, V-90:**
Both PARTIAL paths appear in separate sentences each labeled explicitly as "a separate disqualifier" and "a further separate disqualifier." The word "further" + "also" in the second sentence signals deliberate enumeration, not summary. Three variations achieve this: the ceiling (V-86), the C-47-only test (V-87), and the gap variation (V-90).

**PARTIAL (5 pts) -- V-88, V-89:**
Two distinct structural shapes both earn C-48 PARTIAL:

- **V-88 shape (merged "or" condition):** "A block body that names the self-documenting label function without naming the self-enforcing block body function, or that names both functions without declaring them as structurally distinct roles, earns partial credit." Single sentence, "or" conjunction. Both PARTIAL paths present but not as distinct disqualifiers.

- **V-89 shape (two sentences, no disqualifier framing):** Two separate sentences present, but framed as outcome descriptions: "omits one structural role and earns partial credit" / "also earns partial credit." Neither uses "disqualifier" language. Better than merged but does not meet the "distinct disqualifiers" threshold. C-48 pass condition requires PARTIAL paths "enumerated as distinct disqualifiers" -- descriptive outcome framing does not satisfy this.

**Key finding:** The rubric's C-48 PARTIAL definition ("a merged single condition earns PARTIAL") describes V-88 but not V-89. V-89 has two separate sentences yet still earns PARTIAL -- the gap in the rubric's PARTIAL definition. Both shapes earn 5 pts.

### C-46 -- Non-propagation between closure criteria declared

All 5 variations: PASS. The non-propagation paragraph is identical across all variations ("These two closure functions are genuinely independent. Satisfying [C-43] does not discharge [C-44]..."). Held constant by design.

---

## Discrimination Tests -- Confirmed

| Test | V-pair | Expected delta | Actual delta | Confirmed |
|------|--------|----------------|--------------|-----------|
| C-47 PASS vs FAIL | V-86 vs V-87 | 10 pts | 480 vs 470 = 10 | YES |
| C-48 PASS vs PARTIAL | V-86 vs V-88 | 5 pts | 480 vs 475 = 5 | YES |
| C-47 isolates from C-48 | V-87 vs V-88 | C-47 FAIL vs PASS, C-48 identical | 470 vs 475 = 5 | YES |
| C-47 FAIL + C-48 PARTIAL = 465 | V-89 vs V-86 | -15 pts | 465 vs 480 = -15 | YES |
| Orthogonal 470: C-47 FAIL vs C-45 FAIL | V-87 vs V-90 | 0 pts delta, different failure modes | 470 vs 470 = 0 | YES |

---

## New Patterns

**Pattern 1 -- C-48 PARTIAL has two structural shapes:**
The rubric defines C-48 PARTIAL as "a merged single condition" (V-88 shape). V-89 reveals a second shape that also earns PARTIAL: two separate sentences using descriptive outcome language ("earns partial credit") without explicit "disqualifier" framing. The rubric's PARTIAL definition is incomplete. A C-49 candidate: "Both C-48 PARTIAL shapes declared as distinct cases in block body" -- but whether this warrants a new criterion vs a rubric clarification is a design decision.

**Pattern 2 -- V-90 confirms disqualifier-context naming is insufficient for C-45:**
Function names appearing only in FAIL/PARTIAL disqualifier sentences (V-90) fail C-45. The positive duality assertion ("has two functions serving structurally distinct roles") is required for C-45 PASS. Disqualifier-context-only naming satisfies C-47 and C-48 (function names appear in the correct structural positions) but provides no positive declaration -- C-45 tests for affirmative duality, not incidental mention. This is the R18 gap variation: C-45 FAIL + C-47 PASS + C-48 PASS = 470, orthogonal to V-87's C-45 PASS + C-47 FAIL = 470.

---

## R19 Gap Candidate

The C-48 PARTIAL definition gap (V-89 shape: two separate sentences without "disqualifier" framing) is a candidate for R19. A C-49 criterion would distinguish:
- PASS: both PARTIAL paths in separate sentences each explicitly labeled "disqualifier"
- PARTIAL: both PARTIAL paths in separate sentences framed as outcome descriptions only
- FAIL: both paths in a merged single condition (or absent)

This would isolate 5 pts between V-89-like shapes and V-86/V-87/V-90-like shapes. Predicted impact: re-scores V-89 baseline from 465 to 465 (PARTIAL on C-49) -- but creates a new PASS ceiling at 490 for a variation that names both PARTIAL disqualifier sentences with explicit "disqualifier" framing while also using descriptive outcome language in the same sentences.

---

```json
{"top_score": 480, "all_essential_pass": true, "new_patterns": ["C-48 PARTIAL has two distinct structural shapes: (a) merged or-condition (V-88 shape) and (b) two separate sentences using descriptive outcome language without explicit disqualifier framing (V-89 shape) -- the rubric currently describes only shape (a) as earning PARTIAL, leaving shape (b) undocumented", "V-90 confirms the disqualifier-context-only naming pattern: function names appearing exclusively in FAIL/PARTIAL disqualifier sentences (never in a positive duality declaration) satisfies C-47 and C-48 but fails C-45 -- same predicted score as V-87 (470) via orthogonal structural failure mode"]}
```
