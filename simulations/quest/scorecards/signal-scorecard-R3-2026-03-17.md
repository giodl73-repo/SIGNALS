Now I have everything needed to score. Let me analyze all five variations against all 15 criteria.

---

## Quest Score — `/signal` Round 3

**Rubric**: `signal-rubric-v3-2026-03-17.md`
**Variations**: V-01 through V-05 from `signal-variate-R3-2026-03-17.md`
**Scoring context**: Prompt-design evaluation. All variations carry the R2 V-01 base (verbatim catalog, domain noun table, format consistency). R3 differentiation lives entirely in C-14 and C-15.

---

## Per-Variation Scoring

### V-01 — Single-axis: C-14 Dual Restart Gate (Bare AND Filter)

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | NAMESPACE CATALOG has all 12 namespaces in declared order |
| C-02 | essential | PASS | Every namespace section has a header in SECTION FORMAT template |
| C-03 | essential | PASS | Verbatim catalog with description on every command line |
| C-04 | essential | PASS | COMPLIANCE GATE -- BARE MODE: explicit restart trigger present |
| C-05 | essential | PASS | COMPLIANCE GATE -- FILTER MODE: explicit restart trigger present |
| C-06 | recommended | PASS | All 12 headers carry accurate skill counts matching authoritative list |
| C-07 | recommended | PASS | All 12 namespace sections in catalog end with dispatch footer |
| C-08 | recommended | PASS | All headers include purpose phrase ("8 skills for discovery and research", etc.) |
| C-09 | aspirational | PASS | "emit sub-skill descriptions verbatim; do not paraphrase" + pre-populated catalog |
| C-10 | aspirational | PASS | ALIGNMENT RULE + worked example with 19-char anchor; output will be scannable |
| C-11 | aspirational | PASS | Standalone DOMAIN NOUN TABLE maps all 12 namespaces; no generic placeholder survives |
| C-12 | aspirational | PASS | Explicit char-count rule: "Count characters in the longest command name in that section, then pad shorter names to match." + scout example with spacing |
| C-13 | aspirational | PASS | Catalog uses `->` format; SECTION FORMAT specifies `->` format; no mismatch |
| C-14 | aspirational | **FULL** | Both BARE and FILTER modes have "X is violated. Restart." gates — exactly the R3 target |
| C-15 | aspirational | **PARTIAL** | Char-count algorithm stated ("Count characters in the longest command name...") + one worked example; model still must count at output time. No precomputed width table — the R3 upgrade V-02 targets. |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: C-09 to C-13 (5 full) + C-14 (1.0) + C-15 (0.5) = 6.5/7 → 9.3
**Composite: 99.3** | Band: **Gold**

---

### V-02 — Single-axis: C-15 (Precomputed Namespace-by-Namespace Width Table)

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | Full verbatim catalog, all 12 namespaces |
| C-02 | essential | PASS | Headers present per SECTION FORMAT |
| C-03 | essential | PASS | Descriptions on every command |
| C-04 | essential | PASS | BARE MODE section clearly specifies no prefix/no descriptions/one per line |
| C-05 | essential | PASS | PARSE MODE declares FILTER with "one namespace only" |
| C-06 | recommended | PASS | All 12 header counts accurate |
| C-07 | recommended | PASS | All 12 dispatch footers present |
| C-08 | recommended | PASS | Purpose phrases in all headers |
| C-09 | aspirational | PASS | Verbatim catalog with "do not paraphrase" instruction |
| C-10 | aspirational | PASS | ALIGNMENT WIDTH TABLE gives exact widths; alignment rule is precomputed — output will be scannable |
| C-11 | aspirational | PASS | DOMAIN NOUN TABLE present; all 12 nouns specific |
| C-12 | aspirational | PASS | Alignment instruction + 12-row width table + worked derivation ("19 - 13 = 6 pad spaces") |
| C-13 | aspirational | PASS | Reference and output spec both use `->` format |
| C-14 | aspirational | **FAIL** | No restart gate language anywhere. Single-axis test: only C-15 was modified. Neither BARE nor FILTER mode has a self-check trigger. |
| C-15 | aspirational | **FULL** | 12-row ALIGNMENT WIDTH TABLE with precomputed widths + explicit numeric derivation: "`/scout-naming is 13 chars. 19 - 13 = 6 pad spaces.`" Model reads a value rather than computing it. |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 5 full + C-14 (0.0) + C-15 (1.0) = 6.0/7 → 8.6
**Composite: 98.6** | Band: **Gold**

---

### V-03 — Single-axis: Phrasing Register (Conversational/User-Facing)

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | All 12 namespaces in THE FULL CATALOG |
| C-02 | essential | PASS | Headers in catalog; SECTION FORMAT defines the template |
| C-03 | essential | PASS | Descriptions on every command line |
| C-04 | essential | PASS | "When /signal --bare is requested: list every sub-skill command name... No slash prefix. No descriptions. No headers. No blank lines." Clear behavioral spec. |
| C-05 | essential | PASS | WHEN TO SHOW WHAT: "/signal <namespace> -- show only the skills in that one namespace" |
| C-06 | recommended | PASS | Accurate skill counts in all namespace headers in the catalog |
| C-07 | recommended | PASS | All 12 namespace sections in catalog end with dispatch footer |
| C-08 | recommended | PASS | Purpose phrases in all headers ("3 skills for post-ship signal simulation", etc.) |
| C-09 | aspirational | PASS | "Use these descriptions verbatim -- do not paraphrase or shorten." + pre-populated catalog |
| C-10 | aspirational | PASS | ALIGNMENT paragraph present: "Count the longest command name in the section; pad shorter names to match." + scout worked example |
| C-11 | aspirational | PASS | DOMAIN NOUNS FOR FOOTERS table with all 12 specific nouns |
| C-12 | aspirational | PASS | Alignment instruction: "Count the longest command name in the section; pad shorter names to match that length, then add one space before `->`."; example shows padded scout section |
| C-13 | aspirational | PASS | Reference uses `->` format; SECTION FORMAT specifies `->` format; consistent |
| C-14 | aspirational | **FAIL** | No restart gate. Bare mode says "No slash prefix. No descriptions." as a declarative rule only; no self-check, no restart trigger. |
| C-15 | aspirational | **PARTIAL** | Same char-count algorithm as V-01 ("Count the longest command name... pad shorter names to match.") + same single worked example. No precomputed table. Model must count at runtime. |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 5 full + C-14 (0.0) + C-15 (0.5) = 5.5/7 → 7.9
**Composite: 97.9** | Band: **Gold**

---

### V-04 — Combined: C-14 Dual Gate + C-15 Width Table (Minimal R3 Champion)

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | Full verbatim catalog, all 12 namespaces |
| C-02 | essential | PASS | Headers present |
| C-03 | essential | PASS | Descriptions on every command line |
| C-04 | essential | PASS | PARSE MODE + COMPLIANCE GATE -- BARE MODE with restart trigger |
| C-05 | essential | PASS | PARSE MODE + COMPLIANCE GATE -- FILTER MODE with restart trigger |
| C-06 | recommended | PASS | Accurate counts in all 12 namespace headers |
| C-07 | recommended | PASS | All 12 dispatch footers present with domain-specific nouns |
| C-08 | recommended | PASS | Purpose phrases in all namespace headers |
| C-09 | aspirational | PASS | "emit sub-skill descriptions verbatim; do not paraphrase" + pre-populated catalog |
| C-10 | aspirational | PASS | ALIGNMENT WIDTH TABLE precomputed; output will be scannable reliably |
| C-11 | aspirational | PASS | Standalone DOMAIN NOUN TABLE, all 12 nouns explicit |
| C-12 | aspirational | PASS | "Use the ALIGNMENT WIDTH TABLE to determine how many pad spaces each command name needs." + numeric derivation example showing "13 chars. Pad 6 spaces to reach 19" |
| C-13 | aspirational | PASS | Reference and output spec both use `->` lists; format consistent |
| C-14 | aspirational | **FULL** | COMPLIANCE GATE -- BARE MODE ("Restart") + COMPLIANCE GATE -- FILTER MODE ("Restart") — both modes gated. |
| C-15 | aspirational | **FULL** | 12-row ALIGNMENT WIDTH TABLE + explicit derivation: "/scout-naming is 13 chars. Pad 6 spaces to reach 19, then 1 space, then `->`: `/scout-naming       ->` (6 pad + 1 gap = 7 spaces total)" |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 5 full + C-14 (1.0) + C-15 (1.0) = 7.0/7 → 10
**Composite: 100** | Band: **Gold**

---

### V-05 — Full Integration: All R1 + R2 + R3 Excellence Signals

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | Full verbatim catalog, all 12 namespaces |
| C-02 | essential | PASS | Headers present per SECTION FORMAT template |
| C-03 | essential | PASS | Descriptions on every command line |
| C-04 | essential | PASS | COMPLIANCE GATE -- BARE MODE: "If yes -- MODE: BARE is violated. Restart." |
| C-05 | essential | PASS | COMPLIANCE GATE -- FILTER MODE: "If yes -- MODE: FILTER is violated. Restart." |
| C-06 | recommended | PASS | Header template: "The skill count N must match the actual number of sub-skills listed." All 12 counts accurate. |
| C-07 | recommended | PASS | All 12 dispatch footers; SECTION FORMAT template reinforces footer requirement |
| C-08 | recommended | PASS | SECTION FORMAT: "`<what this namespace is for>`" — all headers carry purpose in plain words |
| C-09 | aspirational | PASS | "emit sub-skill descriptions verbatim; do not paraphrase or shorten" + pre-populated catalog |
| C-10 | aspirational | PASS | ALIGNMENT WIDTH TABLE + "example pad" column; output will be maximally scannable |
| C-11 | aspirational | PASS | Standalone DOMAIN NOUN TABLE, all 12 specific nouns; SECTION FORMAT says "Use the exact domain noun from the DOMAIN NOUN TABLE." |
| C-12 | aspirational | PASS | Step-by-step derivation rule in ALIGNMENT RULE section + 12-row table + "example pad" column showing gaps per namespace |
| C-13 | aspirational | PASS | Catalog and output spec both use `->` format; fully consistent |
| C-14 | aspirational | **FULL** | Both BARE and FILTER compliance gates with "Restart" trigger; gate language is interrogative ("does any line contain...?") which forces the self-check explicitly |
| C-15 | aspirational | **FULL** | 12-row width table + "example pad" column (e.g., "/scout-naming (13) needs 7 spaces") per row — zero derivation ambiguity; no arithmetic required at output time |

**Essential**: 5/5 → 60
**Recommended**: 3/3 → 30
**Aspirational**: 5 full + C-14 (1.0) + C-15 (1.0) = 7.0/7 → 10
**Composite: 100** | Band: **Gold**

---

## Leaderboard

| Rank | V | Composite | Band | Essential | Recommended | Aspirational | Key Differentiator |
|------|---|-----------|------|-----------|-------------|--------------|-------------------|
| 1 (tie) | **V-04** | **100** | Gold | 5/5 | 3/3 | 7/7 | Minimal R3 champion: dual restart gates + precomputed width table |
| 1 (tie) | **V-05** | **100** | Gold | 5/5 | 3/3 | 7/7 | V-04 + per-row example pad column; zero derivation ambiguity |
| 3 | V-01 | 99.3 | Gold | 5/5 | 3/3 | 6.5/7 | C-15 PARTIAL: algorithm present but model still counts at runtime |
| 4 | V-02 | 98.6 | Gold | 5/5 | 3/3 | 6.0/7 | C-14 FAIL: no restart gates; proves C-14 is weight-bearing |
| 5 | V-03 | 97.9 | Gold | 5/5 | 3/3 | 5.5/7 | C-14 FAIL + C-15 PARTIAL: conversational register alone contributes nothing to new criteria |

All 5 essential criteria pass across all 5 variations. All variations reach Gold band. The entire R3 spread (97.9–100) lives in two criteria: C-14 and C-15.

---

## Excellence Signals

### C-14 × C-15 independence confirmed

V-01 proves C-14 FULL is achievable without C-15. V-02 proves C-15 FULL is achievable without C-14. Their composite scores (99.3 and 98.6) are distinct, showing C-14 is worth slightly more per point than C-15 in the aspirational tier. Neither alone reaches 100; both together (V-04/V-05) do.

### Signal 1: Precomputed width table replaces runtime character-counting

**V-02 origin, confirmed in V-04/V-05.** Instead of instructing the model to count characters at output time ("Count the longest name in the section"), provide a 12-row lookup table with the answer already computed. The model reads `19` for scout, `17` for flow — no counting, no miscounting. This is the R3 upgrade over R2 V-01 (algorithm + single example). The algorithm instruction leaves a failure mode: the model counts wrong. The lookup table eliminates that failure mode entirely.

### Signal 2: Per-namespace "example pad" column eliminates all derivation ambiguity

**V-05 only.** The width table gains an `example pad` column: `"/scout-naming (13) needs 7 spaces"`. Every row now shows the complete calculation for a representative command name. The model never needs to perform arithmetic — it copies the pattern. This is strictly more robust than the numeric example in the worked derivation section (which shows one namespace in depth) because it covers all 12 namespaces at a glance.

### Why V-03 adds no value on new criteria

The conversational register change (V-03) improves neither C-14 nor C-15. Phrasing style does not substitute for restart gate logic. This confirms phrasing register is orthogonal to behavioral correctness mechanisms and should not be used as an alternative to explicit gates.

---

## C-14 × C-15 Score Matrix

| V | C-14 | C-15 | Aspirational pts | Composite |
|---|------|------|-----------------|-----------|
| V-04/V-05 | FULL | FULL | 7.0/7 → 10 | 100 |
| V-01 | FULL | PARTIAL | 6.5/7 → 9.3 | 99.3 |
| V-02 | FAIL | FULL | 6.0/7 → 8.6 | 98.6 |
| V-03 | FAIL | PARTIAL | 5.5/7 → 7.9 | 97.9 |

The interaction is additive: each criterion contributes independently. No interaction penalty, no interaction bonus. R4 can target other aspiration criteria — C-14 and C-15 are now solved.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Precomputed namespace-by-namespace width table replaces runtime character-counting — model reads a pre-calculated value rather than counting at output time, eliminating miscounting as a failure mode", "Per-namespace example-pad column in the width table (showing name-char-count and spaces-needed per row) makes the derivation self-contained with zero arithmetic required at output time"]}
```
