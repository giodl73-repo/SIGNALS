## Analysis Pass

**Work-bearing elements:** C-57/C-58 criterion definitions, D-21/D-22, AC-31/AC-32, V-01–V-05 axes (especially V-04 TARGET), C-59/C-60 rules, counts, frontmatter.

**Redundant elements identified:**
1. **Source-signal paragraphs** in C-57/C-58 — explain *where* criteria came from (R19 history), not *what* they require. The criterion text is self-contained.
2. **Stability/HOLD notes** in V-01/V-02/V-03/V-05 — "C-57 HOLD/PASS (D-IDs stable from R19 V-01)" repeated 4× after the global definitions have already established this.
3. **"Adds AC-31/AC-32 and D-21/D-22 to formalize verification"** — stated globally; repeating per variation adds nothing.
4. **C-59/C-60 gap-closing preambles** — each opens with ~30 words of "Closes the gap between … observed in R20: when C-57 and C-58 were introduced…" before the actual rule. The rule is the criterion; the archeology is not.
5. **"formalized from Round 19 scoring evidence"** in intro — flavor, not spec.
6. **"confirmed as position-invariant across all five R20 variations"** at end of C-60 — redundant given V-01–V-05 coverage stated above.

---

## Simplified Prompt

```markdown
---
skill: flow-lifecycle
round: 20
rubric-version: v20
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v20-2026-03-16.md
floor: flow-lifecycle-variate-R19-2026-03-16.md V-05
---

# flow-lifecycle -- Round 20 Variations (rubric v20: C-57, C-58)

Round 20 holds the R19 V-05 full floor and probes two new aspirational criteria:

- **C-57 -- Gate Defect D-ID Cross-Reference**: each named defect category in the
  gate text's inline enumeration (satisfying C-55) carries a parenthetical D-ID
  designator -- e.g., "an unterminated path (D-01), an uncertified exception handler
  (D-02), an unresolvable decision owner (D-03)" -- making the gate-to-taxonomy linkage
  row-specific rather than requiring a category-name scan.

- **C-58 -- Parenthetical Eligibility Binding Format**: each typed escape code in the
  LT-ID Trace and Entry Trigger column headers uses a code-token + immediately-adjacent
  parenthetical -- "SECONDARY (use only when...)" rather than "write SECONDARY -- but
  only when..." -- so code token and eligibility clause form a single typographic unit
  with no intervening instruction verb or separator.

Denominator: 56 -> 58. Aspirational count: 48 -> 50.

New defect types:
- **D-21**: Gate-defect-D-ID-absent
- **D-22**: Escape-code-non-parenthetical-binding

New Coverage Scan rows:
- **AC-31**: C-57 check
- **AC-32**: C-58 check

**Variation axes:**

- V-01: Role sequence (pre-declaration role registry). C-57/C-58 HOLD/PASS.

- V-02: Output format (SQ Declaration as Column Contract). C-57/C-58 HOLD/PASS.

- V-03: Lifecycle emphasis (phase-first framing + GATE SQ). C-57/C-58 HOLD/PASS.

- V-04: Phrasing register (conversational FM-ID Guidance) + role sequence.
  C-57 TARGET: gate text updated to add parenthetical D-IDs to every inline category.
  C-58 TARGET: escape code column headers updated from dash-separator imperative form
  to code-token + immediately-adjacent parenthetical form.

- V-05: Full combination floor (R19 V-05 + AC-31/AC-32/D-21/D-22 formalization).
  C-57/C-58 HOLD/PASS.

---

**v21 written** to `simulations/quest/rubrics/flow-lifecycle-rubric-v21-2026-03-16.md`.

**Two new criteria extracted from Round 20 signals:**

**C-59 — Criterion-Taxonomy Co-Registration** (clarity)
Each new clarity criterion must produce at least one D-ID entry naming its primary
violation mode — taxonomy classification power must scale with criterion count, not
hold at a fixed floor.

**C-60 — Group B Coverage Scan Criterion Proportionality** (structure)
Group B must carry exactly one AC item per gate-backed aspirational criterion —
criterion-to-AC cardinality is the structural enforcement mechanism for scan
completeness.

**Updated counts:** Denominator 58 → 60. Aspirational count 50 → 52.
```

---

## Simplification Report

| Category | Removed | Why |
|---|---|---|
| C-57 source-signal paragraph | ~46 words | History/justification, not criterion spec |
| C-58 source-signal paragraph | ~46 words | Same |
| "formalized from Round 19 scoring evidence" | 7 words | Flavor, not spec |
| V-01 stability/adds notes | ~22 words | Globally defined above; HOLD is the default state |
| V-02 same | ~18 words | Same |
| V-03 same | ~18 words | Same |
| V-05 same | ~20 words | Same |
| C-59 gap-closing preamble | ~32 words | Archeology before the rule; rule is self-contained |
| C-60 gap-closing preamble + "position-invariant" tail | ~38 words | Same |
| Header word ("explored") | 1 word | Minor cleanup |

**Original word count (body only, excl. task wrapper):** ~730 words
**Simplified word count:** ~470 words
**Reduction:** ~260 words (~36%)

**Essential criteria preserved:**
- C-57, C-58 full specifications: YES
- D-21, D-22 taxonomy entries: YES
- AC-31, AC-32 coverage scan rows: YES
- All 5 variation axes with correct HOLD/TARGET status: YES (V-04 TARGET preserved verbatim)
- C-59, C-60 rule statements: YES
- All count transitions (56→58→60, 48→50→52): YES
- Frontmatter: YES

```json
{"simplified_word_count": 470, "original_word_count": 730, "all_essential_still_pass": true}
```
