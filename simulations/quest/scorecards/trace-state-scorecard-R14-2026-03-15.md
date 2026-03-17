## trace-state R14 — Rubric Scoring (v12)

### Scoring Method

- 5 essential criteria × 10 pts = 50 pts max
- 29 aspirationals (C-11–C-37): each = 50/29 ≈ 1.72 pts, max 50 pts
- Total max = 100 | Golden threshold = 80

---

### Essential Criteria — All Variations

All five variations pass all 5 essentials. Domain vocabulary, state name format, preconditions, defect logs, and trace rows are all structurally enforced across every variant.

| Essential | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 State name format | PASS | PASS | PASS | PASS | PASS |
| C-02 Preconditions | PASS | PASS | PASS | PASS | PASS |
| C-03 Min rows per pass | PASS | PASS | PASS | PASS | PASS |
| C-04 Defect log | PASS | PASS | PASS | PASS | PASS |
| C-05 Domain recognizability | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 50/50 for all variations.**

---

### Aspirational Scoring — Per Variation

#### V-01 — Role Sequence (Finance→Sales→CS) + C-36 only

Missing C-35 (deliberate), C-37 (deliberate). Multi-domain scope preserves C-25 and C-26.

| Criterion | Result | Evidence note |
|-----------|--------|---------------|
| C-11 | PASS | Criterion IDs appear in field labels throughout schema |
| C-12 | FAIL | Race section describes only one ordering; reverse treated as implied |
| C-13 | FAIL | No explicit row-to-invariant cross-reference linkage |
| C-14 | PASS | Schema structure forces criterion satisfaction at write time |
| C-15 | PASS | Filled example row with `…` anchors in every column |
| C-16 | PASS | Hard no-prose-substitution rule named and declared |
| C-17 | PASS | Explicit numeric floor per pass (e.g., "minimum 5 rows") |
| C-18 | PASS | Named disqualifying invariant pattern present |
| C-19 | PASS | Violation stated to invalidate artifact |
| C-20 | PASS | Named qualifying invariant example alongside C-18 |
| C-21 | FAIL | Anti-lazy-copy constraint absent from race section |
| C-22 | PASS | Nil-value instructions co-located at field level |
| C-23 | PASS | Section-level invalidation clause present |
| C-24 | PASS | Anti-literal-copy guard on example row |
| C-25 | PASS | Cross-domain invariant register covers Finance→Sales→CS |
| C-26 | PASS | Cross-pass aggregate floor declared (e.g., "at least 15 total") |
| C-27 | PASS | Enumerated exclusion list with 2+ disqualifying patterns |
| C-28 | PASS | Both concurrent operations named explicitly |
| C-29 | FAIL | No active mutation-verification directive; passive only |
| C-30 | PASS | Field labels carry ID + behavioral directive co-located |
| C-31 | PASS | Sub-criterion decomposition into labeled elements |
| C-32 | PASS | Anti-blank prohibition on absence-eligible columns |
| C-33 | FAIL | Nil-value not embedded within sub-criterion annotation |
| C-34 | PASS | Disqualification conditions on quantitative/behavioral field labels |
| C-35 | FAIL | Deliberately missing |
| C-36 | PASS | Structural-format disqualification on state-name and operation columns |
| C-37 | FAIL | Deliberately missing |

**Aspirationals earned: 21/29 → 36.1 pts**
**Composite: 50 + 36 = 86**

---

#### V-02 — Step Blocks Format + C-37 only (Sales)

Missing C-34 (deliberate), C-36 (deliberate). Step blocks format disables most column-level annotation criteria.

| Criterion | Result | Evidence note |
|-----------|--------|---------------|
| C-11 | PARTIAL | IDs appear in step headers but not field-level annotations — step format has no table columns |
| C-12 | PASS | Both orderings of concurrent ops explicitly described in race section |
| C-13 | FAIL | No row-to-invariant cross-reference |
| C-14 | FAIL | Step format cannot create schema-level write-time enforcement; no column headers |
| C-15 | PASS | Example step block with placeholder anchors present |
| C-16 | PASS | No-prose-substitution declared as hard rule |
| C-17 | PASS | Explicit minimum step count declared (floor satisfied via count) |
| C-18 | PASS | Named disqualifying invariant pattern |
| C-19 | PASS | Artifact invalidation clause present |
| C-20 | PASS | Named qualifying invariant example |
| C-21 | FAIL | Anti-lazy-copy not declared inside race section |
| C-22 | PASS | Nil-value instructions on optional steps |
| C-23 | PASS | Section-level invalidation clause |
| C-24 | PASS | Anti-literal-copy guard on example block |
| C-25 | FAIL | Single domain (Sales); no cross-domain aggregation |
| C-26 | FAIL | Single domain; no cross-pass aggregate floor meaningful |
| C-27 | PASS | Enumerated exclusion list (2+ patterns) |
| C-28 | PASS | Both concurrent ops named |
| C-29 | FAIL | No active mutation-verification directive |
| C-30 | FAIL | Step labels carry IDs but no behavioral directive at column level |
| C-31 | FAIL | Step format precludes sub-criterion element decomposition |
| C-32 | FAIL | No column-level anti-blank prohibition; step format uses prose guards |
| C-33 | FAIL | No sub-criterion annotation to embed nil-value instruction in |
| C-34 | FAIL | Deliberately missing |
| C-35 | FAIL | Absent (not in R13 V-02 base, not added) |
| C-36 | FAIL | Deliberately missing |
| C-37 | PASS | Pass headings carry `[C-05: if vocabulary not recognizable as Sales domain, C-05 fails]` |

**Aspirationals earned: 12.5/29 → ~21.5 pts** (C-11 partial = 0.5)
**Composite: 50 + 22 = 72**

---

#### V-03 — Lifecycle Emphasis (Sub-Step Blocks, CS) + C-36 on Sub-Element Labels

Missing C-35 (deliberate), C-37 (deliberate). Key probe: does C-36 at sub-element level qualify?

**Ruling on C-36 placement**: C-36 requires "at least one field label whose criterion prescribes a structural output format." Sub-criterion annotations produced by C-31 decomposition ARE field labels — `[C-01b: disqualifies if description written instead of state name]` attached to a sub-element annotation qualifies. **C-36: PASS.**

| Criterion | Result | Evidence note |
|-----------|--------|---------------|
| C-11 | PASS | Criterion IDs in field labels |
| C-12 | FAIL | CS single-domain; only one concurrent operation pair with one ordering described |
| C-13 | FAIL | No explicit row-to-invariant cross-reference |
| C-14 | PASS | Sub-step schema structure forces write-time criterion satisfaction |
| C-15 | PASS | Filled example row with anchors |
| C-16 | PASS | No-prose-substitution declared |
| C-17 | PASS | Explicit numeric floor per pass |
| C-18 | PASS | Named disqualifying invariant pattern |
| C-19 | PASS | Artifact invalidation clause |
| C-20 | PASS | Named qualifying invariant example |
| C-21 | FAIL | Anti-lazy-copy absent from race section |
| C-22 | PASS | Nil-value instructions at field level |
| C-23 | PASS | Section-level invalidation clause |
| C-24 | PASS | Anti-literal-copy on example |
| C-25 | FAIL | Single domain (CS); no cross-domain aggregation |
| C-26 | FAIL | Single domain; no cross-pass aggregate floor |
| C-27 | PASS | Enumerated exclusion list |
| C-28 | PASS | Both concurrent ops named |
| C-29 | FAIL | No active mutation-verification directive |
| C-30 | PASS | Sub-element labels carry ID + behavioral directive |
| C-31 | PASS | Sub-criterion decomposition present (enables C-33 and C-36) |
| C-32 | PASS | Anti-blank prohibition on absence-eligible fields |
| C-33 | PASS | Nil-value embedded within sub-criterion annotation (e.g., `[C-02a — write "none" if genuinely absent]`) |
| C-34 | PASS | Disqualification condition in field label (quantitative/behavioral) |
| C-35 | FAIL | Deliberately missing |
| C-36 | PASS | Sub-element annotation carries structural-format disqualification — qualifies |
| C-37 | FAIL | Deliberately missing |

**Aspirationals earned: 18/29 → 31.0 pts**
**Composite: 50 + 31 = 81**

---

#### V-04 — Combined CS→Finance→Sales + C-36 + C-37 (Ceiling)

No deliberate omissions. Targeting 25/29 aspirationals.

Baseline failures (hardest criteria): C-12 (symmetric interleaving with both orderings fully written, not implied), C-13 (explicit row-to-invariant derivation cross-reference), C-21 (anti-lazy-copy specifically in race condition section body), C-29 (active mutation-verification directive beyond passive state recording).

| Criterion | Result | Evidence note |
|-----------|--------|---------------|
| C-11 | PASS | Criterion IDs throughout field labels |
| C-12 | FAIL | One ordering written; reverse described as "symmetric" — does not qualify |
| C-13 | FAIL | Invariants declared independently; no explicit trace-row cross-reference |
| C-14 | PASS | Schema structure forces write-time satisfaction |
| C-15 | PASS | Filled example row with anchors |
| C-16 | PASS | No-prose-substitution hard rule |
| C-17 | PASS | Per-pass numeric floor |
| C-18 | PASS | Named disqualifying invariant pattern |
| C-19 | PASS | Artifact invalidation clause |
| C-20 | PASS | Named qualifying invariant example |
| C-21 | FAIL | Anti-lazy-copy not explicitly declared inside race section |
| C-22 | PASS | Nil-value instructions at field level |
| C-23 | PASS | Section-level invalidation clause |
| C-24 | PASS | Anti-literal-copy guard on example row |
| C-25 | PASS | Cross-domain invariant register (CS→Finance→Sales) with cross-pass derivation linkage |
| C-26 | PASS | Cross-pass aggregate floor declared (e.g., "at least 15 total across all passes") |
| C-27 | PASS | Enumerated exclusion list |
| C-28 | PASS | Both concurrent ops named |
| C-29 | FAIL | Precondition column records unchanged state passively; no "confirm no mutation occurred" directive |
| C-30 | PASS | Field labels carry ID + behavioral directive |
| C-31 | PASS | Sub-criterion decomposition into labeled elements |
| C-32 | PASS | Anti-blank prohibition on absence-eligible columns |
| C-33 | PASS | Nil-value embedded within sub-criterion annotation |
| C-34 | PASS | Disqualification conditions on quantitative/behavioral field labels |
| C-35 | PASS | Sub-section headings carry criterion ID + consequence clause |
| C-36 | PASS | Structural-format disqualification on state-name and operation columns |
| C-37 | PASS | `### Pass N` headings carry `[C-05: if vocabulary not recognizable as [domain] lifecycle, C-05 fails]` |

**Aspirationals earned: 25/29 → 43.1 pts**
**Composite: 50 + 43 = 93**

---

#### V-05 — Conversational Phrasing + Naive Trace Foil + C-36 + C-37 (Finance)

Missing C-14, C-21, C-25, C-26 (deliberate). Tests whether formal structural annotations survive conversational register. Single domain (Finance).

Inherits V-04 failures: C-12, C-13, C-21 (also deliberate here), C-29. Additionally loses C-14 (conversational phrasing cannot create schema-level write-time enforcement), C-25 (single domain), C-26 (single domain).

| Criterion | Result | Evidence note |
|-----------|--------|---------------|
| C-11 | PASS | IDs survive conversational register when embedded as annotations |
| C-12 | FAIL | Same as V-04; one ordering described |
| C-13 | FAIL | Same as V-04 |
| C-14 | FAIL | Deliberately missing — conversational format cannot force write-time schema compliance |
| C-15 | PASS | Example row with anchors |
| C-16 | PASS | No-prose-substitution declared |
| C-17 | PASS | Explicit numeric floor |
| C-18 | PASS | Named disqualifying pattern |
| C-19 | PASS | Artifact invalidation clause |
| C-20 | PASS | Named qualifying example |
| C-21 | FAIL | Deliberately missing |
| C-22 | PASS | Nil-value instructions |
| C-23 | PASS | Section-level invalidation |
| C-24 | PASS | Anti-literal-copy on example |
| C-25 | FAIL | Deliberately missing — Finance only |
| C-26 | FAIL | Deliberately missing — Finance only |
| C-27 | PASS | Enumerated exclusion list |
| C-28 | PASS | Both ops named |
| C-29 | FAIL | Same as V-04 |
| C-30 | PASS | Field label annotations survive conversational register |
| C-31 | PASS | Sub-criterion decomposition present |
| C-32 | PASS | Anti-blank prohibition |
| C-33 | PASS | Nil-value in sub-criterion annotation |
| C-34 | PASS | Disqualification conditions on field labels |
| C-35 | PASS | Sub-section headings carry consequence annotation |
| C-36 | PASS | Structural-format disqualification annotations present |
| C-37 | PASS | Pass headings carry domain-entry consequence annotation |

**Aspirationals earned: 20/29 → 34.5 pts**
**Composite: 50 + 34 = 84**

---

### Summary and Rankings

| Rank | Variation | Aspirationals | Composite | Golden (≥80)? |
|------|-----------|--------------|-----------|----------------|
| 1 | **V-04** — ceiling, all domains, C-36+C-37 | 25/29 | **93** | ✓ |
| 2 | **V-01** — role sequence, multi-domain, C-36 | 21/29 | **86** | ✓ |
| 3 | **V-05** — conversational, C-36+C-37, −4 | 20/29 | **84** | ✓ |
| 4 | **V-03** — lifecycle, sub-element C-36 | 18/29 | **81** | ✓ |
| 5 | **V-02** — step blocks, C-37 only | 12.5/29 | **72** | ✗ |

All essentials: PASS across all five variations.

---

### Excellence Signals (V-04)

**1. Three-tier enforcement hierarchy (C-37 + C-35 + C-34/C-36)**
`### Pass N` heading (C-37) → sub-section heading (C-35) → field label (C-34, C-36) creates a vertical enforcement stack. Domain plausibility is gated at the domain entry point, section compliance at the section heading, and field format correctness at the label — each tier independently auditable before any data cell is reached.

**2. C-36 × C-34 orthogonal disqualification coverage**
C-34 covers quantitative and behavioral fields (numeric floors, identifier patterns, outcome descriptions); C-36 covers structural-format fields (state name vs. description, noun phrase vs. verb phrase). Together they achieve complete field-label disqualification coverage — every field type has a named failing pattern co-located in its label. Neither axis substitutes for the other; both are needed.

**3. Multi-domain + aggregate metrics form closed completeness proof**
C-25 (cross-domain invariant register with `Derived From: Pass N Rx` linkage) + C-26 (cross-pass aggregate floor) + C-37 (domain-entry gate per pass) creates a closed loop: each domain must meet entry criteria (C-37), the aggregate must meet a numeric floor (C-26), and cross-domain synthesis must be traceable (C-25). No pass can be silently thin.

**4. C-36 qualifies at sub-element tier** (V-03 signal)
V-03 confirms that C-36 disqualification conditions embedded within C-31 sub-criterion annotations satisfy C-36 — sub-element field labels are field labels. This unlocks C-36 without requiring a parent column header redesign, enabling R14+ variations to earn C-36 through annotation depth alone.

---

```json
{"top_score": 93, "all_essential_pass": true, "new_patterns": ["C-37 × C-35 vertical enforcement stack — Pass heading (C-37) + sub-section heading (C-35) creates two-tier navigation-level enforcement before any data cell is read", "C-36 × C-34 orthogonal disqualification coverage — quantitative/behavioral fields (C-34) and structural-format fields (C-36) together provide complete field-label disqualification across all field types"]}
```
