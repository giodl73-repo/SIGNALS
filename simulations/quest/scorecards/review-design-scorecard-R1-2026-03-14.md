Reading the variations and rubric. The golden file is a placeholder — scoring will be structural (prompt design analysis, not live output).

## Signal Quest Scorecard — `review-design` Round 1

---

### Criterion-by-Criterion Evaluation

#### C-01 | All 6 Disciplines Present

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | All 6 named in Step 1; per-reviewer block required for each |
| V-02 | PASS | `Stock: Architect | Code-Quality | ...` in BLOCK 1; BLOCK 2 contract runs all 6 first |
| V-03 | PASS | All 6 listed explicitly in Phase 1; Phase 3 runs each |
| V-04 | PASS | F-01 halt fires on fewer than 6 discipline blocks; named in BLOCK 2 header |
| V-05 | PASS | F-01 halt + structural table enforces all 6 stock before domain experts |

---

#### C-02 | Severity Tag on Every Finding

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PARTIAL | Prose rule: "Every finding must carry exactly one of: P1/P2/P3" — stated but not structurally enforced |
| V-02 | PASS | `Sev` table column; rule: "blank or freeform text is structurally wrong" — structural |
| V-03 | PARTIAL | "Every finding requires a P1/P2/P3 tag" repeated in Phase 2 and Phase 3 — prose only |
| V-04 | PASS | F-02 halt: "Finding present with no P1/P2/P3 tag → stop and restructure" |
| V-05 | PASS | F-02 + `Sev` column; "any other value is a format error" — dual enforcement |

---

#### C-03 | Domain Expert Justified by Input Signal

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PARTIAL | Step 1 asks for signal-driven selection but no labeled field for the signal mapping |
| V-02 | PASS | `Signal:` field required; "empty or generic Signal fails" stated in rules |
| V-03 | PASS | `Signal detected: [exact phrase]` + `Expert added:` + `Reason:` — explicit three-field trace |
| V-04 | PASS | F-03 halt: "Domain expert named with no input-signal mapping → stop and restructure" |
| V-05 | PASS | F-03 + `Signal:` field in BLOCK 1 with "exact phrase or concept" requirement |

---

#### C-04 | Consensus Block Present

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Step 3 explicitly required; "If no consensus exists… write: No consensus findings" |
| V-02 | PASS | BLOCK 3 required; "If no consensus findings: write CONSENSUS | none | —" |
| V-03 | PASS | Phase 4 required after expert + discipline phases; explicit fallback wording |
| V-04 | PASS | F-04 halt + "Do not omit this block — F-04 fires on omission" |
| V-05 | PASS | F-04 + "Never omit this entire block" + table row fallback — strongest enforcement |

---

#### C-05 | Unique Catches Surfaced

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Step 4 required; "If no unique catches exist, write: No unique catches" |
| V-02 | PASS | BLOCK 4 required; "If none: write UNIQUE | none | —" |
| V-03 | PASS | Phase 5 required; "If none: No unique catches" |
| V-04 | PASS | BLOCK 4 required with fallback wording |
| V-05 | PASS | BLOCK 4 table with `UNIQUE | none | —` fallback row |

---

#### C-06 | Amend Pathway — Targeted, Not Full Re-review

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Step 5: "Do not instruct a full re-review. Each amend targets the reviewer(s) whose concern applies to the changed section only." |
| V-02 | PASS | BLOCK 5: "One entry per P1 finding. Do not prescribe a full re-review." |
| V-03 | PASS | Phase 6: "Re-run: [reviewer(s) whose concern this touches] on [section or component — not full review]" |
| V-04 | PASS | F-05 halt: "Amend pathway says 're-run everything' → stop"; "target specific reviewer on specific section" |
| V-05 | PASS | F-05 + `Re-run: [scope — never "full review"]` + explicit P1=0 fallback |

---

#### C-07 | Finding Traceability to Design Section

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PARTIAL | Rules state "Every P1 must name section; ≥50% P2 must name section" — prose, no structural hook |
| V-02 | PASS | `Section` table column enforces section reference per row; P1 rule stated alongside column definition |
| V-03 | PARTIAL | "Every P1 finding requires a section reference" stated in Phase 2 — prose only, no structural column |
| V-04 | PARTIAL | "Every P1 must name a section. At least 50% of P2s must name a section." — prose, no table anchor |
| V-05 | PASS | `Section` column + F-02 extension: "P1 with no Section is a traceability failure" — structural + named failure |

---

#### C-08 | Severity Pyramid Sanity (P3 ≥ P2 ≥ P1)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | FAIL | No mention of severity distribution or pyramid check |
| V-02 | FAIL | No mention of severity distribution |
| V-03 | FAIL | No mention of severity distribution |
| V-04 | FAIL | No mention of severity distribution |
| V-05 | FAIL | No mention of severity distribution |

**Pattern**: C-08 fails universally. The rubric allows explicit rationale to satisfy it — none of the five variations prompt for either a pyramid or a rationale when inverted.

---

#### C-09 | Split Opinion Synthesis (not just listing)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | `SPLIT: [decision] … Synthesis: [1-3 sentences explaining the underlying design tension]` — explicit synthesis field |
| V-02 | PASS | SPLIT row includes `Synthesis: [1-3 sentences on the design tension]` in the table format |
| V-03 | PASS | Phase 4: `Synthesis: [1-3 sentences on the design trade-off this split reveals]` — same explicit field |
| V-04 | PASS | BLOCK 3: `Synthesis: [1-3 sentences on the underlying design tension]` |
| V-05 | PASS | `Synthesis: [1-3 sent.]` in table cell; synthesis field present |

---

### Composite Scores

Scoring formula: `essential_pass/4 × 60 + recommended_pass/3 × 30 + aspirational_pass/2 × 10`
PARTIAL = 0.5 pass for scoring; FAIL on pass condition for golden gate.

| Var | C-01 | C-02 | C-03 | C-04 | Essential (×60) | C-05 | C-06 | C-07 | Recommended (×30) | C-08 | C-09 | Aspirational (×10) | **Composite** | All Essential? | Outcome |
|-----|------|------|------|------|-----------------|------|------|------|-------------------|------|------|-------------------|---------------|----------------|---------|
| V-01 | P | PR | PR | P | 3.0/4 → 45 | P | P | PR | 2.5/3 → 25 | F | P | 1/2 → 5 | **75** | No | Acceptable |
| V-02 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | F | P | 1/2 → 5 | **95** | Yes | **Golden** |
| V-03 | P | PR | P | P | 3.5/4 → 52.5 | P | P | PR | 2.5/3 → 25 | F | P | 1/2 → 5 | **82.5** | No | Acceptable |
| V-04 | P | P | P | P | 4/4 → 60 | P | P | PR | 2.5/3 → 25 | F | P | 1/2 → 5 | **90** | Yes | **Golden** |
| V-05 | P | P | P | P | 4/4 → 60 | P | P | P | 3/3 → 30 | F | P | 1/2 → 5 | **95** | Yes | **Golden** |

`P = PASS, PR = PARTIAL, F = FAIL`

---

### Ranking

| Rank | Variation | Score | Outcome |
|------|-----------|-------|---------|
| 1 | V-05 (combined) | 95 | Golden — defense-in-depth: F-IDs + table columns |
| 1 | V-02 (output format) | 95 | Golden — table columns alone achieve same structural score |
| 3 | V-04 (inertia framing) | 90 | Golden — F-IDs cover essentials but C-07 left to prose |
| 4 | V-03 (role sequence) | 82.5 | Acceptable — C-02 prose-only breaks essential gate |
| 5 | V-01 (baseline) | 75 | Acceptable — both C-02 and C-03 rely on unanchored prose |

---

### Excellence Signals

**From V-02 and V-05 (top scorers):**

1. **Table column enforcement closes C-02 and C-07 without prose rules** — `Sev` column makes an unseveritied finding visually incomplete; `Section` column makes an untraced finding structurally wrong. Prose rules of the same content (V-01, V-03, V-04) leave gaps.

2. **Named Signal field in expert roster closes C-03** — `Signal: [exact phrase]` as a structured field (not a prose instruction) forces signal-to-expert traceability. V-03's `Signal detected:` three-field block achieves the same effect with labeled prose.

3. **F-ID co-location at the block that can fail** — V-04 and V-05 place failure mode IDs directly at each block header rather than only in a preamble. The halt fires at the moment of risk, not before or after.

4. **C-08 is universally unaddressed** — all five variations fail the severity pyramid criterion. No prompt asks for a distribution check or rationale when the pyramid inverts. This is the single criterion that would lift a 95 to a theoretical 100.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["table-column enforcement makes C-02 and C-07 structurally impossible to fail without relying on prose rules", "C-08 severity pyramid fails universally — requires explicit distribution check or inversion-rationale prompt to fire"]}
```
