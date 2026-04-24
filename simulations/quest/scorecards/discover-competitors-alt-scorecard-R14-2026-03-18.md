# /quest:score — discover-competitors-alt R14 Scorecard

## Scoring Basis

- **Rubric:** v14 (31 aspirational criteria, C-09–C-39)
- **Per-aspirational weight:** 10/31 = 0.3226 pts
- **Max composite:** 100

---

## Criterion-by-Criterion Assessment

### Essential Criteria (C-01–C-05, 12 pts each)

All five variations run the full gate sequence with C0, competitive map, findings, and AMEND. No structural gaps.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Named C0 entry with inertia mechanism | PASS | PASS | PASS | PASS | PASS |
| C-02 | ≥3 named external competitors with threat levels | PASS | PASS | PASS | PASS | PASS |
| C-03 | Competitive map with focus dimension woven in | PASS | PASS | PASS | PASS | PASS |
| C-04 | Findings reference named competitor rows | PASS | PASS | PASS | PASS | PASS |
| C-05 | AMEND section present and non-empty | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 (all)**

---

### Recommended Criteria (C-06–C-08, 10 pts each)

All variations include mechanism-level C0 reasoning, inline WebSearch citation, and full 4-component AMEND schema.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Mechanism-level inertia reasoning (switching cost / habit / workaround) | PASS | PASS | PASS | PASS | PASS |
| C-07 | Web-verified competitive claim with inline citation | PASS | PASS | PASS | PASS | PASS |
| C-08 | AMEND with input-to-output pairs (≥2 entries, both sides named) | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 (all)**

---

### Aspirational Criteria (C-09–C-39, 10/31 pts each)

C-09 through C-30 pass uniformly across all variations — DOMAIN-TERMS artifact, domain-adaptive token, unconditional pre-phase declaration, manifest table in native markdown, per-gate REQUIRED OUTPUTS tables, bracket-notation substitution, AMEND schema with all four domain-neutral component names. No separating signals in that range.

The R14 separation begins at C-31.

#### C-31 — GATE-0 REQUIRED OUTPUTS retains template form with propagation declaration

**V-01 (compact Yes-cell):** The TOKEN row Yes-cell declares "committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers and in the manifest `[TOKEN] propagation` column header." This is an explicit propagation declaration readable from GATE-0's table. **PASS** — the cell contains both the declaration (TOKEN committed here) and the substitution rule.

**V-02–V-05 (dedicated propagation row):** GATE-0's REQUIRED OUTPUTS table contains a separate propagation row that is structurally distinct from the TOKEN commitment row. Fully self-contained. **PASS.**

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-31 | PASS | PASS | PASS | PASS | PASS |

#### C-32 — Gate manifest includes a TOKEN-propagation column

All variations include a `[TOKEN] propagation` column in the EXECUTION PLAN manifest. **PASS (all).**

#### C-33 — Manifest TOKEN-propagation column cells use rubric-vocabulary verbatim

All variations label GATE-0 "Declaration site" and GATE-1+ "Substitution/inheritance site" in the manifest column cells. **PASS (all).**

#### C-34 — TOKEN-PROPAGATION ARCHITECTURE block declared before manifest table

All variations include an explicitly labeled architecture block positioned before the EXECUTION PLAN table. **PASS (all).**

#### C-35 — Manifest TOKEN-propagation column header uses bracket-notation syntax

All variations use `[TOKEN] propagation` as the manifest column header — not a static string. **PASS (all).**

#### C-36 — Dual-layer propagation contract: manifest column and GATE-0 table each independently self-contained

This is the first separating criterion for V-01.

**V-01 (compact Yes-cell):** The Yes-cell explicitly cross-references the manifest — it says "and in the manifest `[TOKEN] propagation` column header." GATE-0's table is not independent of the manifest; it names the manifest as a co-destination. Independence test fails. **FAIL.**

**V-02–V-05 (dedicated propagation row):** The dedicated row in GATE-0's REQUIRED OUTPUTS table declares the full substitution rule without referencing the manifest as a co-artifact. Reading only GATE-0's table yields the complete propagation contract; reading only the manifest column yields the complete propagation contract. Neither layer loads the other. **PASS.**

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-36 | **FAIL** | PASS | PASS | PASS | PASS |

#### C-37 — Full triple-mechanism manifest hardening: C-33 + C-34 + C-35 simultaneously

C-37 requires C-35. C-35 requires C-32. C-32 requires C-31. C-31 PASSES for V-01 (the Yes-cell does declare substitution); therefore the dependency chain to C-35 holds.

All three manifest hardening mechanisms are simultaneously active in every variation — verbatim vocabulary cells (C-33), architecture block before manifest (C-34), bracket-notation header (C-35). No mechanism delegates to another.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-37 | PASS | PASS | PASS | PASS | PASS |

#### C-38 — Architecture block explicitly primes both manifest TOKEN-propagation column and GATE-0 REQUIRED OUTPUTS table

C-38 requires C-36. V-01 fails C-36 → **C-38 scored 0 for V-01 by dependency rule.**

For V-02–V-05 (C-36 PASS), the test is whether the architecture block explicitly names both downstream structural artifacts.

**V-02:** Block text explicitly names "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" by label. A reader consulting only the block can identify both target artifacts. **PASS.**

**V-03 (R13 V-05 form):** Architecture block uses verbatim vocabulary and a dedicated propagation row, but never names "the manifest TOKEN-propagation column" or "GATE-0's REQUIRED OUTPUTS table" by those structural labels. Block is self-contained as a contract, but does not name both artifacts as targets. **FAIL.**

**V-04 (prose form — explicit naming + verbatim vocab):** Block explicitly names both artifacts AND uses verbatim vocabulary. **PASS.**

**V-05 (mini-table form — explicit naming + verbatim vocab):** Architecture block's mini-table enumerates both artifacts as table rows by structural label (manifest TOKEN-propagation column / GATE-0 REQUIRED OUTPUTS table). A reader consulting only the mini-table can identify both targets. **PASS** — format is structurally equivalent for C-38's operative test.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-38 | **FAIL (dep)** | PASS | **FAIL** | PASS | PASS |

#### C-39 — Architecture block prose uses rubric-vocabulary verbatim: "Declaration site" and "Substitution/inheritance site"

C-39 requires C-34 and C-33. Both pass for all variations. The separating test is the architecture block's own vocabulary.

**V-01:** Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim — co-registered with manifest cells. **PASS.**

**V-02:** Architecture block uses synonyms — "declaring gate" and "consuming gates." Not the verbatim terms. **FAIL.**

**V-03 (R13 V-05 form):** Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim. **PASS.**

**V-04:** Block uses verbatim vocabulary alongside explicit artifact naming. **PASS.**

**V-05:** Block includes verbatim vocabulary in prose following the mini-table. **PASS.**

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-39 | PASS | **FAIL** | PASS | PASS | PASS |

---

### Aspirational Summary Table

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 through C-30 | PASS×22 | PASS×22 | PASS×22 | PASS×22 | PASS×22 |
| C-31 | PASS | PASS | PASS | PASS | PASS |
| C-32 | PASS | PASS | PASS | PASS | PASS |
| C-33 | PASS | PASS | PASS | PASS | PASS |
| C-34 | PASS | PASS | PASS | PASS | PASS |
| C-35 | PASS | PASS | PASS | PASS | PASS |
| C-36 | **FAIL** | PASS | PASS | PASS | PASS |
| C-37 | PASS | PASS | PASS | PASS | PASS |
| C-38 | **FAIL** | PASS | **FAIL** | PASS | PASS |
| C-39 | PASS | **FAIL** | PASS | PASS | PASS |
| **Aspirational passing** | **29/31** | **30/31** | **30/31** | **31/31** | **31/31** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 29 × (10/31) = **9.355** | **99.355** |
| V-02 | 60 | 30 | 30 × (10/31) = **9.677** | **99.677** |
| V-03 | 60 | 30 | 30 × (10/31) = **9.677** | **99.677** |
| V-04 | 60 | 30 | 31 × (10/31) = **10.000** | **100.000** |
| V-05 | 60 | 30 | 31 × (10/31) = **10.000** | **100.000** |

---

## Rankings

| Rank | Variation | Composite | Failing aspirational |
|------|-----------|-----------|----------------------|
| 1 (tie) | **V-04** | **100.000** | None |
| 1 (tie) | **V-05** | **100.000** | None |
| 3 (tie) | V-02 | 99.677 | C-39 |
| 3 (tie) | V-03 | 99.677 | C-38 |
| 5 | V-01 | 99.355 | C-36, C-38 |

---

## Decisive Question Resolution

**Q1 — Does C-37 scoring produce visible composite separation when C-36 fails?**
Yes. V-01 scores 99.355 vs V-02/V-03 at 99.677 — a 0.322 pt gap. C-37 PASS for V-01 but C-36/C-38 failing costs two aspirational slots. The separation is small but structurally visible. C-37 produces its own margin only when C-36 also passes; when C-36 fails, C-38 is zeroed by dependency, creating a two-criterion hole not a one-criterion hole.

**Q2 — Are C-38 and C-39 symmetric orthogonal axes?**
Yes, confirmed. V-02 (C-38 PASS, C-39 FAIL) and V-03 (C-38 FAIL, C-39 PASS) both score 30/31 at identical composite (99.677). The axes are independent and equal-weight. Neither axis enables or blocks the other.

**Q3 — Does mini-table format (V-05) outperform prose form (V-04) on C-38?**
No. Both reach 31/31 = 100. The mini-table's structural enumeration of both target artifacts satisfies C-38's operative test identically to V-04's prose paragraph with explicit artifact naming. Format does not differentiate C-38 compliance; artifact-name explicitness is the operative variable, not presentation form.

---

## Excellence Signals (V-04 / V-05)

**Signal 1 — Dual-target explicit naming in the architecture block.** The architecture block must name both "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" by their structural labels. Naming the propagation contract in plain prose is not sufficient for C-38; the specific downstream artifacts must be called out by label so a reader consulting only the block can identify the two structural locations without consulting the manifest or per-gate tables.

**Signal 2 — Vocabulary co-registration closes the interpretation gap.** Using "Declaration site" and "Substitution/inheritance site" verbatim in the architecture block (C-39) means the prose block and the manifest column cells use identical terms — zero translation step when moving between artifacts. This creates a closed vocabulary ring across three layers: architecture block → manifest cells → GATE-0 propagation row.

**Signal 3 — Dedicated propagation row for independence.** Separating the propagation declaration into its own GATE-0 REQUIRED OUTPUTS row (rather than embedding it in the TOKEN Yes-cell) eliminates the cross-reference to the manifest that causes C-36's independence test to fail. Each layer's contract must be self-contained; a cell that names the manifest as a co-target violates that independence.

**Signal 4 — Format neutrality for C-38.** Mini-table enumeration of both target artifacts (V-05) and prose enumeration (V-04) are equivalent for C-38 compliance. The rubric's operative test is artifact-name presence, not structural format. This extends the C-38 compliance surface: any explicit naming form satisfies the criterion.

---

## Scorecard Written

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Architecture block satisfies C-38 only when it explicitly names both 'the manifest TOKEN-propagation column' and 'GATE-0\\'s REQUIRED OUTPUTS table' by structural label — plain-prose propagation contract without artifact-name targets fails", "C-38 and C-39 are symmetric orthogonal axes at equal composite weight: explicit dual-target naming and verbatim vocabulary co-registration are independent and neither enables the other", "Mini-table format in architecture block for dual-target declaration is equivalent to prose for C-38 compliance — operative variable is artifact-name explicitness, not presentation form"]}
```
