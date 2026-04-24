I now have all five variations. Let me score them.

---

## Round 11 Scorecard — `review-design` (v10 rubric)

All five variations inherit R10 V-05 as baseline, which carries F-01 through F-24 and already satisfies C-01 through C-32. The three new F-IDs (F-25, F-26, F-27) are additive above v10's ceiling. I evaluate each criterion below.

---

### Criterion Evaluation

#### Essential (60% weight)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 \| 6 Stock Disciplines | PASS — F-01 declared; 6 disciplines in BLOCK 1 stock table; F-22 for domain coverage | PASS | PASS | PASS | PASS |
| C-02 \| Severity Tag on Every Finding | PASS — F-02 declared; Sev column in BLOCK 2 table enforces P1/P2/P3 exclusively | PASS | PASS | PASS | PASS |
| C-03 \| Domain Expert Auto-Selection Justified | PASS — BLOCK 1 domain expert table requires Signal detected; F-03 fires on empty signal | PASS | PASS | PASS | PASS |
| C-04 \| Consensus Block Present | PASS — BLOCK 3 required; F-04 fires on absence | PASS | PASS | PASS | PASS |

All essential: **4/4 PASS** for all five variations.

---

#### Recommended (30% weight)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05 \| Unique Catches Surfaced | PASS — BLOCK 4 required; F-08 fires on absence | PASS | PASS | PASS | PASS |
| C-06 \| Amend Pathway Described | PASS — BLOCK 5 present; F-05 bars "full review" scope | PASS | PASS | PASS | PASS |
| C-07 \| Finding Traceability to Design Section | PASS — Section column required in BLOCK 2 table; P1 rows must have Section populated | PASS | PASS | PASS | PASS |

All recommended: **3/3 PASS** for all five variations.

---

#### Aspirational (10% weight, denominator 25)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 \| Severity Distribution Sanity | PASS — BLOCK 2.5 table; F-06 fires on silent inversion | PASS | PASS | PASS | PASS |
| C-09 \| Expert Disagreement Analysis | PASS — BLOCK 3 SPLIT type; F-11 fires on empty Synthesis | PASS | PASS | PASS | PASS |
| C-10 \| Structural Column Enforcement in Finding Tables | PASS — BLOCK 2 uses Sev/Section/Finding 3-column table | PASS | PASS | PASS | PASS |
| C-11 \| Three-Field Expert Trace | PASS — BLOCK 1 domain expert table: Signal detected / Expert added / Reason | PASS | PASS | PASS | PASS |
| C-12 \| Severity Pyramid Gate as Dedicated Lifecycle Block | PASS — BLOCK 2.5 is a discrete block after BLOCK 2 before BLOCK 3 | PASS | PASS | PASS | PASS |
| C-13 \| Expert Trace in Table Column Form | PASS — BLOCK 1 domain expert table uses 3 named columns | PASS | PASS | PASS | PASS |
| C-14 \| Named Halt Conditions on Every Mandatory Block | PASS — F-01 through F-24 declared in Failure Mode Registry; all mandatory blocks covered | PASS | PASS | PASS | PASS |
| C-15 \| Roster Commitment Table Before Finding Generation | PASS — BLOCK 1.5 table appears before BLOCK 2 | PASS | PASS | PASS | PASS |
| C-16 \| Source Column in Roster Commitment Table | PASS — BLOCK 1.5 has Source column (Domain/Stock) | PASS | PASS | PASS | PASS |
| C-17 \| Cross-Block Reviewer Identity Verification | PASS — F-10 declared for orphaned domain experts | PASS | PASS | PASS | PASS |
| C-18 \| Content-Completeness Halt on SPLIT Synthesis | PASS — F-11 declared; fires on empty Synthesis in SPLIT row | PASS | PASS | PASS | PASS |
| C-19 \| Cross-Block Count-Parity for P1 Findings | PASS — F-12 declared; amend row count must equal P1 count from BLOCK 2.5 | PASS | PASS | PASS | PASS |
| C-20 \| BLOCK 5 Amend Pathway in 4-Column Table Form | PASS — BLOCK 5 is 4-column Markdown table (P1 Finding / Section / Action / Re-run Scope) | PASS | PASS | PASS | PASS |
| C-21 \| BLOCK 0 Pre-Scan Signal Catalogue | PASS — BLOCK 0 pre-scan with F-13 formal gate against uncatalogued signals | PASS | PASS | PASS | PASS |
| C-22 \| BLOCK 3 Consensus in 4-Column Structural Table Form | PASS — BLOCK 3 4-column table (Type / Issue / Reviewers / Synthesis) | PASS | PASS | PASS | PASS |
| C-23 \| Register Isolation for Formal Lifecycle Block Headers | PASS — block headers use SHALL/MUST/fires exclusively; no "aim for" or informal phrasing | PASS | PASS | PASS | PASS |
| C-24 \| BLOCK 4 Unique-Catch Reviewer Identity Verification | PASS — F-16 declared for phantom catcher | PASS | PASS | PASS | PASS |
| C-25 \| BLOCK 5 Re-run Scope Reviewer Identity Verification | PASS — F-17 declared for phantom re-run target | PASS | PASS | PASS | PASS |
| C-26 \| BLOCK 0 Signal Disposition Completeness | PASS — F-18 declared; bidirectional gate with F-13 | PASS | PASS | PASS | PASS |
| C-27 \| BLOCK 2.5 Pyramid Inversion Rationale Content Completeness | PASS — F-19 declared; Rationale cell must be populated when inverted | PASS | PASS | PASS | PASS |
| C-28 \| BLOCK 4 Unique Catches in Structural Table Form | PASS — F-20 declared for prose unique catches | PASS | PASS | PASS | PASS |
| C-29 \| BLOCK 0 No-Expert Disposition Row Reason Content Completeness | PASS — F-21 declared; disposition reason cell must be populated | PASS | PASS | PASS | PASS |
| C-30 \| BLOCK 2 Domain Expert Finding Coverage Symmetry | PASS — F-22 declared; domain expert absent from BLOCK 2 fires halt | PASS | PASS | PASS | PASS |
| C-31 \| BLOCK 3 Consensus Issue Column Content Completeness | PASS — F-23 declared; empty Issue cell fires halt (none sentinel exempt) | PASS | PASS | PASS | PASS |
| C-32 \| BLOCK 5 Amend Action Cell Content Completeness | PASS — F-24 declared; empty Action cell fires halt | PASS | PASS | PASS | PASS |

All aspirational: **25/25 PASS** for all five variations.

---

### Composite Scores

```
composite = (4/4 × 60) + (3/3 × 30) + (25/25 × 10) = 60 + 30 + 10 = 100
```

| Variation | Essential | Recommended | Aspirational | Composite | Outcome |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-01 (F-25) | 4/4 | 3/3 | 25/25 | **100** | Golden |
| V-02 (F-26) | 4/4 | 3/3 | 25/25 | **100** | Golden |
| V-03 (F-27) | 4/4 | 3/3 | 25/25 | **100** | Golden |
| V-04 (F-25+F-26) | 4/4 | 3/3 | 25/25 | **100** | Golden |
| V-05 (F-25+F-26+F-27) | 4/4 | 3/3 | 25/25 | **100** | Golden |

Prediction confirmed: all five score 100. The isolation design holds — the three new F-IDs are cleanly additive above v10's ceiling and do not perturb any existing criterion.

---

### Trace Artifact

**Feature deltas above R10 V-05 baseline:**

| Variation | New F-IDs | Lifecycle position | Enforcement class |
|-----------|-----------|-------------------|-------------------|
| V-01 | F-25 | BLOCK 4 Finding cell | Content-completeness-within-structural-presence |
| V-02 | F-26 | BLOCK 5 Section cell | Content-completeness-within-structural-presence |
| V-03 | F-27 | BLOCK 2 P1 Section cell | Prose-MUST-to-named-halt conversion |
| V-04 | F-25 + F-26 | BLOCK 4 + BLOCK 5 | Stacked content-completeness |
| V-05 | F-25 + F-26 + F-27 | BLOCK 2 + BLOCK 4 + BLOCK 5 | Full R11 feature set |

---

### Excellence Signals (from V-05, the R12 extraction source)

**1. Prose-MUST-to-named-halt conversion (F-27):** V-03/V-05 surface a new pattern class. F-27 does not add a new requirement — BLOCK 2 already said "P1 rows: Section MUST be populated." F-27 converts that existing prose MUST into a named, detectable enforcement event. This extends C-14's principle beyond new blocks to existing prose requirements within current blocks. Any prose MUST without a named F-ID is a candidate for this class.

**2. Column-level enforcement surface completion (F-25 + F-26):** Every column in every mandatory lifecycle table now has at least one named halt covering its content-completeness requirement. V-05 is the first variation where no column in any block remains unguarded. The architecture is closed.

**3. Sentinel-exempt content completeness:** Both F-25 and F-26 explicitly document that `--` and "no P1 findings" sentinel tokens are exempt from the content-completeness halt. This prevents the halt from firing on structurally legitimate placeholder rows while still enforcing completeness on real data rows. The explicit sentinel exemption is necessary for every content-completeness F-ID in a block that uses sentinel rows.

---

### Aspirational Extraction for R12

Three new criteria candidates confirmed by isolation:

- **C-33** (from F-25, confirmed by V-02/V-03 without it): BLOCK 4 Finding cell content completeness
- **C-34** (from F-26, confirmed by V-01/V-03 without it): BLOCK 5 Section cell content completeness
- **C-35** (from F-27, confirmed by V-01/V-02 without it): BLOCK 2 P1 Section named halt (prose-to-F-ID conversion)

Formula update for R12: denominator 25 → 28. Each aspirational criterion contributes ~0.36 pts. Score ceiling 100 preserved.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["prose-MUST-to-named-halt conversion: any existing prose MUST without a backing F-ID is a detectable gap; F-27 converts BLOCK 2 P1 Section requirement from skippable instruction to observable enforcement event", "column-level enforcement surface completion: F-25 and F-26 close the last unguarded content cells across all mandatory lifecycle tables -- every column in BLOCK 2/3/4/5 now has at least one named halt", "sentinel-exempt content completeness: content-completeness halts must explicitly document which sentinel tokens are exempt to prevent false fires on structurally legitimate placeholder rows"]}
```
