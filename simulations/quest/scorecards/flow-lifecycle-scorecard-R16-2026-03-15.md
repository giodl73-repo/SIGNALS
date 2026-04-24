## flow-lifecycle — Round 16 Scoring (Rubric v16, C-48 + C-49 probe)

---

### Scoring Key

| Symbol | Meaning | Credit |
|--------|---------|--------|
| PASS | Criterion fully satisfied | 1.0 |
| PARTIAL | Criterion partially satisfied; structural risk | 0.5 |
| FAIL | Criterion not satisfied by mechanism described | 0.0 |

**Composite formula:** criteria\_met / 49 × 100
**Floor (C-01 to C-47):** All variations carry complete R15 V-05 floor → 47/47 PASS = 95.9 baseline.
**Variable:** C-48 and C-49 delivery mechanism.

---

### V-01 — Compact Two-Clause Tokens + Full V-05 C-49 Floor

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 State Transition Coverage | PASS | Floor |
| C-02 Exception Flow Traces | PASS | Floor |
| C-03 Terminal State Completeness | PASS | Floor |
| C-04 Bottleneck and Gap Identification | PASS | Floor |
| C-05 Domain Role Assignment | PASS | Floor |
| C-06 Parallel Path Modeling | PASS | Floor |
| C-07 Decision Point Explicitness | PASS | Floor |
| C-08 Edge Case Enumeration | PASS | Floor |
| C-09 to C-35 | PASS (27) | Floor |
| C-36 to C-47 | PASS (12) | Floor |
| **C-48 Per-Field Anti-Pattern Vocabulary** | **PASS** | Compact "does not count; Mandatory" tokens embedded in each SQ Declaration field definition cell. C-48 requires "at least one inline enforcement token" — compact two-clause form satisfies this for every field. Truncation risk eliminated by reduced cell length. |
| **C-49 Mutual-Audit Relationship as Design Principle** | **PASS** | Full V-05 Status-Quo Gap column header maintained: contains "mutual-audit design principle," "architected as a mutual-audit pair," and "design intent of their adjacency, not a coincidence of table layout." All three pass-condition locutions present in column header. |

**Score: 49/49 = 100**
**All essential: PASS**

---

### V-02 — Pre-Table FM-ID Protocol + Inline Tokens + Full V-05 C-49 Floor

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-47 | PASS (47) | Floor |
| **C-48 Per-Field Anti-Pattern Vocabulary** | **PASS** | Defense-in-depth: pre-table FM-ID Protocol block provides anticipatory framing AND inline tokens remain embedded in field definition cells. C-48's point-of-use requirement is satisfied by the inline tokens; the pre-table block is redundant reinforcement, not a displacement. D-14 defect (preamble-only) is structurally blocked by the co-presence of inline tokens. |
| **C-49 Mutual-Audit Relationship as Design Principle** | **PASS** | Full V-05 floor. Same evidence as V-01. |

**Score: 49/49 = 100**
**All essential: PASS**

> V-02's redundancy does not reduce compliance; it adds a second closure mechanism. D-14 incidence drops because even if an author stops reading after the pre-table block, the inline tokens are also encountered when filling cells.

---

### V-03 — Full V-05 C-48 Floor + Rationale Block + Abbreviated C-49 Header

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-47 | PASS (47) | Floor |
| **C-48 Per-Field Anti-Pattern Vocabulary** | **PASS** | Full V-05 floor for SQ Declaration field definitions. Complete multi-clause tokens intact in each cell. |
| **C-49 Mutual-Audit Relationship as Design Principle** | **FAIL** | C-49 pass condition requires the architectural designation to appear **in the column header itself** — "not only in adjacent caption prose, introductory blocks, Gate B annotations, or text above the table." A rationale block before the Phase Index is explicitly excluded by the rubric. An abbreviated column header that drops "design principle" / "design intent" language reduces to structural-behavior description ("these two columns audit each other"), which the rubric explicitly marks as insufficient. The column header carries no qualifying principle designation. |

**Score: 48/49 = 97.9 → 98**
**All essential: PASS**

> C-49 failure is a placement failure, not a content failure. The mutual-audit rationale exists — it is simply mis-positioned in the pre-table block rather than in the column header cell that C-49 targets.

---

### V-04 — FM-ID Registry Framing + Minimal-Expression C-49 Header

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-47 | PASS (47) | Floor |
| **C-48 Per-Field Anti-Pattern Vocabulary** | **PARTIAL** | "FM-ID Registry framing" introduces structural ambiguity. C-48 requires tokens embedded within the field definition cell of each SQ Declaration field. If FM-ID Registry framing means tokens appear in a separate FM-ID Registry section (distinct from the SQ Declaration table itself), they are displaced from the required point-of-use location. Compact tokens may be present but their placement is uncertain — if the SQ Declaration field cells carry only field names with enforcement delegated to the registry block, C-48 fails for those fields. Half credit: some fields likely carry tokens inline; full per-field coverage is not confirmed by mechanism description. |
| **C-49 Mutual-Audit Relationship as Design Principle** | **PASS** | Minimal-expression "mutual-audit design principle by design intent" contains both qualifying locutions: "mutual-audit design principle" (principle-naming) and "design intent" (architectural attribution). The rubric's pass condition accepts "mutual-audit design principle" as sufficient vocabulary. Minimal form passes; lower verbosity does not disqualify. |

**Score: 48.5/49 = 99.0**
**All essential: PASS**

---

### V-05 — Imperative Voice in Cell Definitions + Full V-05 C-49 Header

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-47 | PASS (47) | Floor |
| **C-48 Per-Field Anti-Pattern Vocabulary** | **PARTIAL** | C-48 specifies exact enforcement vocabulary: "does not count," "Mandatory," or "is a fail." Imperative directives ("Write X. Do not write Y. Mandatory.") satisfy the criterion only for fields where "Mandatory" is also present — "Mandatory" is an enumerated qualifying token. However, "Do not write Y" alone does not map to any of the three specified tokens; it is imperative instruction, not enforcement vocabulary as defined. FM-01 and FM-02 fields typically carry "does not count" / "is a fail" anti-pattern tokens in V-05 floor — if the imperative substitution replaces those with "Do not write [qualifier]" only, those fields carry no qualifying token. At-risk fields: FM-01 and FM-02 (imperative voice substitutes for "does not count"). Incumbent Process and Inertia Driver likely retain "Mandatory" (qualifying). 2/4 fields confirmed; 2/4 at risk. Half credit. |
| **C-49 Mutual-Audit Relationship as Design Principle** | **PASS** | Full V-05 design-principle header maintained. Same evidence as V-01. |

**Score: 48.5/49 = 99.0**
**All essential: PASS**

---

### Variation Ranking

| Rank | Variation | C-48 | C-49 | Score |
|------|-----------|------|------|-------|
| 1T | V-01 | PASS | PASS | **100** |
| 1T | V-02 | PASS | PASS | **100** |
| 3T | V-04 | PARTIAL | PASS | 99 |
| 3T | V-05 | PARTIAL | PASS | 99 |
| 5 | V-03 | PASS | FAIL | 98 |

---

### Excellence Signals (V-01 and V-02)

**ES-1 — Token economy eliminates truncation risk without weakening criterion coverage.**
V-01's compact two-clause form ("does not count; Mandatory") proves the R15 V-05 multi-clause elaboration over-delivers C-48. The criterion requires one token per field; V-01 provides exactly that. Shorter cells are less vulnerable to output compression, making compliance more resilient at production time. This is the tightest-form delivery pattern that still closes C-48.

**ES-2 — Defense-in-depth framing (V-02) blocks D-14 without displacing point-of-use enforcement.**
Pre-table FM-ID Protocol block + inline tokens creates two independent closure paths. An author who stops at the pre-table block still encounters inline tokens when filling cells; an author who skips the pre-table block still has the inline tokens. Neither path leaves C-48 open. The redundancy is not noise — it is structural insurance against partial reading.

**ES-3 — Full V-05 Status-Quo Gap column header is the lowest-risk C-49 delivery under all compression scenarios.**
V-03's failure confirms that the full header text must not be abbreviated. The mutual-audit language ("design principle," "design intent," "not a coincidence of table layout") works together as a locution cluster — any one dropped phrase risks slipping below C-49's pass threshold. V-01 and V-02 preserve the complete cluster; the extra tokens in the header are load-bearing, not decorative.

**ES-4 — Minimal-expression C-49 ("mutual-audit design principle by design intent") is viable as a compression target.**
V-04 demonstrates that the full V-05 header can be condensed without C-49 failure if the keyword core ("mutual-audit design principle" + "design intent") is preserved. This establishes a safe compression floor for C-49: two noun phrases, one in-column, column-header-placed.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["compact two-clause anti-pattern tokens per SQ Declaration field reduce truncation risk while preserving C-48 point-of-use compliance — over-delivery in cell verbosity is unnecessary and adds structural fragility", "pre-table FM-ID Protocol block plus inline tokens creates defense-in-depth for C-48 without displacing field-level enforcement — redundant framing closes D-14 by ensuring C-48 compliance survives partial-reading scenarios", "minimal-expression C-49 header ('mutual-audit design principle by design intent') passes the criterion — the keyword core is load-bearing; surrounding elaboration prose is compressible without compliance loss"]}
```
