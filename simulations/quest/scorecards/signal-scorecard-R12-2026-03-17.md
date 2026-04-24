## Quest Score — /signal Round 12 (v12 Rubric)

### Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/30 × 10)
```

Essential: 12 pts each (5 criteria) | Recommended: 10 pts each (3 criteria) | Aspirational: 0.33 pts each (30 criteria)

---

### Criterion-by-Criterion Evaluation

All five variations share the same strong R11 V-04/V-05 base. Criteria C-01 through C-35 are evaluated identically across variations; only C-36, C-37, C-38 differ by design.

#### Essential (C-01 – C-05) — identical across all variations

| ID | Criterion | All V | Evidence |
|----|-----------|-------|----------|
| C-01 | All 12 namespaces present | **PASS** | Catalog lists scout/draft/review/flow/trace/prove/listen/program/topic/quest/mock/org |
| C-02 | Namespace headers with purpose phrase | **PASS** | Each header carries a one-line purpose in NAMESPACE CATALOG |
| C-03 | Every sub-skill listed under its namespace | **PASS** | 61 skills cataloged: 8+4+4+7+7+9+3+2+6+4+3+4 |
| C-04 | `--bare` produces command names only | **PASS** | BARE MODE section + slash-strip gate present in all variations |
| C-05 | `<namespace>` filter scopes output | **PASS** | FILTER MODE parse rule + compliance gate present in all variations |

**Essential score: 5/5 → 60.00 pts (all variations)**

---

#### Recommended (C-06 – C-08) — identical across all variations

| ID | Criterion | All V | Evidence |
|----|-----------|-------|----------|
| C-06 | Sub-skill count per namespace accurate | **PASS** | Counts in catalog match canonical totals |
| C-07 | Each namespace includes dispatch footer | **PASS** | Domain-noun footers present throughout |
| C-08 | Namespace headers state namespace purpose | **PASS** | Confirmed by NAMESPACE CATALOG structure |

**Recommended score: 3/3 → 30.00 pts (all variations)**

---

#### Aspirational (C-09 – C-38) — variable on C-36, C-37, C-38

| ID | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-------------|------|------|------|------|------|
| C-09 | Sub-skill descriptions match canonical one-liners | PASS | PASS | PASS | PASS | PASS |
| C-10 | Output scannable without overwhelming | PASS | PASS | PASS | PASS | PASS |
| C-11 | Footer uses namespace-specific domain noun | PASS | PASS | PASS | PASS | PASS |
| C-12 | `->` separator column-aligned within section | PASS | PASS | PASS | PASS | PASS |
| C-13 | Inline reference format matches spec output | PASS | PASS | PASS | PASS | PASS |
| C-14 | Bare/filter modes include pre-emit compliance gate | PASS | PASS | PASS | PASS | PASS |
| C-15 | Alignment rule provides named precomputed width table | PASS | PASS | PASS | PASS | PASS |
| C-16 | Width table includes per-row example-pad derivation | PASS | PASS | PASS | PASS | PASS |
| C-17 | NAMESPACE CATALOG precedes behavioral rules | PASS | PASS | PASS | PASS | PASS |
| C-18 | Bare-mode gate includes 61-line count with per-namespace breakdown | PASS | PASS | PASS | PASS | PASS |
| C-19 | PARSE MODE enumerates all 12 canonical namespace names | PASS | PASS | PASS | PASS | PASS |
| C-20 | Filter-mode gate includes per-namespace count check | PASS | PASS | PASS | PASS | PASS |
| C-21 | BARE MODE states explicit first/last namespace output anchors | PASS | PASS | PASS | PASS | PASS |
| C-22 | NAMESPACE CATALOG is active transcription commitment gate | PASS | PASS | PASS | PASS | PASS |
| C-23 | NAMESPACE CATALOG labeled as literal output | PASS | PASS | PASS | PASS | PASS |
| C-24 | All three modes include explicit pre-emission completeness verification | PASS | PASS | PASS | PASS | PASS |
| C-25 | FULL MODE includes compliance restart gate | PASS | PASS | PASS | PASS | PASS |
| C-26 | Transcription gate requires counted entry acknowledgment | PASS | PASS | PASS | PASS | PASS |
| C-27 | SECTION FORMAT includes per-section sub-skill count self-check | PASS | PASS | PASS | PASS | PASS |
| C-28 | FULL MODE gate includes canonical namespace emit-order check | PASS | PASS | PASS | PASS | PASS |
| C-29 | FILTER MODE gate includes section-format verification | PASS | PASS | PASS | PASS | PASS |
| C-30 | BARE MODE includes explicit slash-strip worked examples | PASS | PASS | PASS | PASS | PASS |
| C-31 | Count formula uses labeled namespace breakdown in transcription + BARE gate | PASS | PASS | PASS | PASS | PASS |
| C-32 | Domain nouns defined in named DOMAIN NOUN TABLE | PASS | PASS | PASS | PASS | PASS |
| C-33 | FULL gate Check 3 enumerates all 12 canonical namespaces in sequence | PASS | PASS | PASS | PASS | PASS |
| C-34 | FULL MODE gate includes section-format verification | PASS | PASS | PASS | PASS | PASS |
| C-35 | BARE MODE gate includes canonical namespace emit-order check | PASS | PASS | PASS | PASS | PASS |
| **C-36** | **Prompt includes named COMPLIANCE GATE COVERAGE MATRIX** | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |
| **C-37** | **FULL gate Check 4 embeds SECTION FORMAT sub-elements verbatim** | **FAIL** | **PASS** | **FAIL** | **PASS** | **FAIL** |
| **C-38** | **BARE gate Check 3 uses positional line-range notation** | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |

**Evidence notes:**

- **C-36**: V-01, V-04, V-05 — coverage matrix table present (5 rows: scope/completeness/count/order/format × FULL/BARE/FILTER). V-02, V-03 — absent, no such named table.
- **C-37**: V-02, V-04 — Check 4 in FULL gate embeds header pattern, `->` separator, and footer pattern verbatim inline. V-01, V-03, V-05 — Check 4 uses name-reference ("conform to the SECTION FORMAT template above"), requiring cross-prompt recall.
- **C-38**: V-03, V-05 — BARE Check 3 specifies "first 8 lines are scout-* names, next 4 are draft-* names…" positional bounds for all 12 groups. V-01, V-02, V-04 — uses name-list notation requiring name→namespace correlation.

---

### Composite Score Calculation

| V | Essential (60) | Recommended (30) | Aspirational (/30) | Asp pts (10) | **Composite** |
|---|---------------|-----------------|-------------------|-------------|---------------|
| V-01 | 60.00 | 30.00 | 28/30 | 9.33 | **99.33** |
| V-02 | 60.00 | 30.00 | 28/30 | 9.33 | **99.33** |
| V-03 | 60.00 | 30.00 | 28/30 | 9.33 | **99.33** |
| V-04 | 60.00 | 30.00 | 29/30 | 9.67 | **99.67** |
| V-05 | 60.00 | 30.00 | 29/30 | 9.67 | **99.67** |

---

### Ranking

| Rank | Variation | Score | Delta vs prior |
|------|-----------|-------|----------------|
| 1 (tie) | **V-04** (R+S) | **99.67** | — |
| 1 (tie) | **V-05** (R+T) | **99.67** | — |
| 3 (tie) | V-01 (R only) | 99.33 | −0.33 |
| 3 (tie) | V-02 (S only) | 99.33 | −0.33 |
| 3 (tie) | V-03 (T only) | 99.33 | −0.33 |

---

### Independence Confirmation

Each single-axis variation adds exactly +0.33 over the base (28/30 vs 27/30 under v12). Each dual-axis variation adds exactly +0.67 (29/30). The contributions stack linearly with zero interaction:

| Axes added | Asp passed | Score |
|-----------|-----------|-------|
| none (R11 best, retroactive) | 27/30 | 99.00 |
| R only (V-01) | 28/30 | 99.33 |
| S only (V-02) | 28/30 | 99.33 |
| T only (V-03) | 28/30 | 99.33 |
| R+S (V-04) | 29/30 | 99.67 |
| R+T (V-05) | 29/30 | 99.67 |
| R+S+T (V-06, predicted) | 30/30 | **100.00** |

R, S, T independence confirmed. V-06 is predicted to saturate v12.

---

### Excellence Signals (from V-04 and V-05)

**V-04 top pattern — coverage matrix + verbatim embed are mutually reinforcing:**
The COMPLIANCE GATE COVERAGE MATRIX (C-36) tells the reader *which* check covers *which* dimension across *which* mode. The verbatim SECTION FORMAT embed in Check 4 (C-37) delivers the *what to verify* without a cross-reference. Together they make the gate fully self-contained: the matrix locates the check; the embedded spec executes it.

**V-05 top pattern — coverage matrix anchors positional order verification:**
The matrix makes the gate structure legible. The line-range notation in BARE Check 3 (C-38) makes namespace-order verification mechanical — no name→namespace correlation needed, only positional counting. The matrix and line-ranges share the same structural philosophy: explicit enumeration over implicit knowledge.

**Shared signal (V-04 and V-05) — named tables are the highest-leverage aspirational move:**
Three rounds of rubric evolution (C-15 widths, C-32 domain nouns, C-36 gate coverage) have each added a named lookup table as a standalone prompt artifact. Each table converts implicit reliance on cross-section recall into an explicit, locatable, single-source-of-truth reference. Named tables are the consistent +0.33 upgrade pattern.

---

```json
{"top_score": 99.67, "all_essential_pass": true, "new_patterns": ["Named COMPLIANCE GATE COVERAGE MATRIX makes gate completeness a first-class prompt artifact — the matrix locates each check type per mode, eliminating implicit reliance on reading all gate sections to understand overall coverage", "Verbatim SECTION FORMAT sub-element embed in FULL Check 4 makes format verification self-contained — removes cross-prompt recall dependency that arises from name-references to earlier spec sections", "Positional line-range notation in BARE Check 3 makes emit-order verification mechanical — counting line positions requires no name-to-namespace correlation, a self-verifiable check for headerless output"]}
```
