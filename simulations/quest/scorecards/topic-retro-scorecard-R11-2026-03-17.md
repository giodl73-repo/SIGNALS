## topic-retro — Round 11 Scorecard (Rubric v9)

**Date**: 2026-03-17
**Rubric**: v9 (C-01–C-29; max = 132)
**Target criteria**: C-28 (recommendation-slot-completeness-guard) and C-29 (phase-8-score-copy-guard)

---

### Scoring Basis

All five variations share R7-V-05 as the evolved base, with C-22 through C-27 already incorporated. The differentiating axes are:

| ID | C-23 | C-28 | C-29 |
|----|------|------|------|
| V-01 | Baseline seals (most fields have format strings, not all) | `[slot:X]` tokens + SEAL string check | Match-check only against Phase 4 (no copy guard) |
| V-02 | Lighter baseline seals | Two-slot template, no slot guard | "COPY from Phase 6. Do not recompute." + SEAL citation check |
| V-03 | Imperative mode, minimal format specs | Prohibition phrasing + "no bracket text" SEAL | Prohibition + "confirm by reading Phase 6" SEAL |
| V-04 | Same as V-02/baseline (Phases 1–6, 9 unchanged) | V-01 `[slot:X]` + SEAL check (Phase 7) | V-02 copy guard (Phase 8) |
| V-05 | All 9 seals have explicit format-contract strings per field | V-01 `[slot:X]` + SEAL check | V-02 copy guard + Phase 8 SEAL names "Phase 6 verdict" as copy source |

---

### Criteria Evaluation

#### Essential Criteria (C-01–C-05) — identical across all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Signal accuracy section present | PASS | PASS | PASS | PASS | PASS | Phase 3 Predicted vs Actual table with both prediction and actual per namespace |
| C-02 Correct/wrong verdict per signal | PASS | PASS | PASS | PASS | PASS | C/P/W/ND enumerated label column in Phase 3; explicit constraint against vague language |
| C-03 Gaps section present and actionable | PASS | PASS | PASS | PASS | PASS | Phase 7 gap table includes "Changed commit? YES/NO" — decision impact stated per row |
| C-04 Echo present (one unexpected finding) | PASS | PASS | PASS | PASS | PASS | Phase 1 produces exactly one Echo with Pattern and Why-unexpected fields |
| C-05 Topic and commitment context established | PASS | PASS | PASS | PASS | PASS | "$ARGUMENTS" in header; Phase 1 runs before signal examination; commitment nature is post-ship retrospective |

**Essential subtotal (all): 60/60**

#### Recommended Criteria (C-06–C-08) — identical across all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Signal coverage summary | PASS | PASS | PASS | PASS | PASS | Phase 2: 9-row namespace table with COVERED/EMPTY status distinguishes gathered vs absent |
| C-07 Recommendation tied to gaps or echo | PASS | PASS | PASS | PASS | PASS | `[slot:gap-or-echo]` in V-01/V-04/V-05; "gap type or Echo pattern" named in all |
| C-08 Accuracy rate or ratio stated | PASS | PASS | PASS | PASS | PASS | Phase 4 requires "N/M = X%" count ratio immediately below scoring table |

**Recommended subtotal (all): 30/30**

#### Aspirational Criteria (C-09–C-29)

**C-09 through C-22, C-24–C-27 — common to all variations:**

| Criterion | All 5 | Evidence |
|-----------|-------|----------|
| C-09 Echo linked to systemic pattern | PASS | Phase 1 Pattern field requires named taxonomy class + failure mode description |
| C-10 AMEND scope declared and enforced per table | PASS | `{{#if amend}}` blocks add scope markers to every table; per-table enforcement confirmed |
| C-11 Systemic pattern echo field (named structural column) | PASS | `> **Pattern**: {label} — {description}` is a labeled block, not prose-embedded |
| C-12 Three-way wrong/gap/echo isolation | PASS | Phase 1 = Echo, Phase 3 = wrong verdicts, Phase 7 = gaps; distinct phases, LOCK prevents Phase 1 reuse |
| C-13 Inertia framing for gaps | PASS | Column A explicitly requires "We assumed X" framing; "not an outcome" constraint enforced in all SEAL variants |
| C-14 Verdict label explicit not prose | PASS | Phase 3 uses C/P/W/ND enum in a dedicated Match column |
| C-15 Accuracy ratio not just count | PASS | Phase 4 requires both weighted {number}/100 AND N/M = X% count ratio |
| C-16 Namespace coverage table not implied | PASS | Phase 2 is a fixed 9-row structured table, one row per namespace |
| C-17 Recommendation template (bracket-slot) | PASS | All variations carry the bracket-slot recommendation template in Phase 7 |
| C-18 Echo systemic pattern named | PASS | Pattern field constrained against blank and against restatement of Echo in all SEAL variants |
| C-19 Phase completion self-contained | PASS | All 9 phases use tabular structure + SEAL; SEAL prevents silent truncation at phase level |
| C-20 Gap inertia assumption named | PASS | Column A is a dedicated labeled field for assumption (vs Column B for outcome) |
| C-21 Phase seal explicit | PASS | All 9 phases have named PHASE SEAL sections that enumerate required fields with constraints |
| C-22 OOS secondary table for excluded signals | PASS | Phase 2 `{{#if amend}}` block produces dedicated OOS table even when no artifacts excluded |
| C-24 Echo why-unexpected explained | PASS | `> **Why unexpected**: {prior belief contradicted}` field required with constraint against label-only |
| C-25 Recommendation outcome measurable | PASS | Three-slot structure present in all: "Addresses X by Y so that Z (measurable outcome)" |
| C-26 Gap inertia column structurally isolated | PASS | Column A and Column B explicitly isolated with "must not share content" validation |
| C-27 Phase self-containment extended to all phases | PASS | All 9 phases have named seals; Phases 7 and 8 explicitly covered by seal mechanism |

**Shared aspirational subtotal (all): 36/36**

---

**Differentiating Criteria:**

#### C-23 — Phase Seal Format Strings Per Field

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PARTIAL (1)** | Most seal fields carry format strings (`{format}` notation) but not all — e.g., Phase 2 Status field says "exactly 'COVERED' or 'EMPTY'" without `{COVERED|EMPTY}` format spec; some fields enumerate values without a format-string wrapper |
| V-02 | **PARTIAL (1)** | Lighter baseline seals; Phase 1 SEAL uses `{name}` and `{failure class description}` in Pattern but Phase 4 SEAL says "TOTAL row with weighted formula applied" with no format spec |
| V-03 | **PARTIAL (1)** | Imperative mode throughout; seals list constraints without `{format}` notation per field — "[ ] Status: COVERED or EMPTY — nothing else" lacks format spec |
| V-04 | **PARTIAL (1)** | Phases 1–6, 9 use same baseline as V-02; only Phases 7–8 get updated treatments; format-string coverage across all 9 phases incomplete |
| V-05 | **PASS (2)** | Every seal field across all 9 phases carries an explicit format string; Phase 2 adds `{COVERED}|{EMPTY}`, `{filename.md}`, OOS table row format; Phase 8 SEAL adds "COPY-VERIFIED" label and explicit copy-source specification |

#### C-28 — Recommendation Slot Completeness Guard

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS (2)** | `[slot:gap-or-echo]`, `[slot:practice-change]`, `[slot:measurable-outcome]` named tokens used in Phase 7 template. Phase 7 SEAL item: "output does not contain the literal strings '[slot:gap-or-echo]', '[slot:practice-change]', or '[slot:measurable-outcome]'" — string-level assertion |
| V-02 | **PARTIAL (1)** | Two-slot template without `[slot:X]` naming; Phase 7 SEAL says "Recommendation: present with gap/echo, practice change, and measurable outcome filled" — presence check, not placeholder-string check |
| V-03 | **PARTIAL (1)** | Prohibition phrasing adds post-hoc instruction ("Do not write 'Addresses [gap type]'"), but SEAL says "no bracket text remains" without specific `[slot:` string detection — less mechanical than named tokens; a generic bracket prohibition passes if any bracket is absent, but cannot confirm all three specific slots were replaced |
| V-04 | **PASS (2)** | V-01 `[slot:X]` token mechanism applied in Phase 7 + SEAL slot check — identical to V-01 on this criterion |
| V-05 | **PASS (2)** | Same as V-04; `[slot:X]` tokens + SEAL string check. Additionally, design-guarantees summary explicitly states: "Three-slot `[slot:X]` recommendation; SEAL confirms no `[slot:` strings survive" |

#### C-29 — Phase 8 Score Copy Guard

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PARTIAL (1)** | Phase 8 SEAL says "This score: matches Phase 4 TOTAL weighted score — format: {number}/100" — a match-check against Phase 4, not a copy guard. No "do not recompute" instruction. Silent recomputation that matches Phase 4 would pass this check |
| V-02 | **PASS (2)** | Phase 8 body: "COPY the accuracy score from the Phase 6 verdict sentence into the 'This score' cell. Do not recompute or derive this number." SEAL: "confirm the number in this cell matches the number in the Phase 6 verdict sentence exactly (do not recompute from Phase 4)" |
| V-03 | **PASS (2)** | "Do not derive the score for this phase. Copy it from the Phase 6 verdict sentence." SEAL: "is the number from the Phase 6 verdict sentence — confirm by reading Phase 6, not by computing" — explicit prohibition with Phase 6 as named authority |
| V-04 | **PASS (2)** | V-02 copy guard applied in Phase 8; design guarantees summary: "Score COPIED from Phase 6 verdict sentence. Explicit 'do not recompute.' SEAL verifies by Phase 6 citation." |
| V-05 | **PASS (2)** | Same mechanism as V-04 plus the SEAL item is upgraded to "COPY-VERIFIED" label that explicitly distinguishes "do not recompute from Phase 4 TOTAL; the copy source is Phase 6 verdict, not Phase 4" — closes the ambiguity about which phase is the copy source |

---

### Composite Scores

| ID | Essential | Recommended | Shared Asp. | C-23 | C-28 | C-29 | **Total** | **Pct (of 132)** |
|----|-----------|-------------|-------------|------|------|------|-----------|------------------|
| V-01 | 60 | 30 | 36 | 1 | 2 | 1 | **130** | 98.5% |
| V-02 | 60 | 30 | 36 | 1 | 1 | 2 | **130** | 98.5% |
| V-03 | 60 | 30 | 36 | 1 | 1 | 2 | **130** | 98.5% |
| V-04 | 60 | 30 | 36 | 1 | 2 | 2 | **131** | 99.2% |
| **V-05** | **60** | **30** | **36** | **2** | **2** | **2** | **132** | **100%** |

**Ranking**: V-05 > V-04 > V-01 = V-02 = V-03

---

### All-Essential Check

All five variations PASS all five essential criteria: **YES** for all.

---

### Excellence Signals from V-05

**1. Named-token slot guards enable mechanical detection**
Generic bracket syntax (`[name]`, `[gap type]`) can survive undetected because it resembles a label that might be optional. `[slot:X]` naming makes the token distinctive — the SEAL check becomes a string-level assertion (`[slot:` must not appear in output) rather than a judgment call. V-03's "no bracket text" prohibition is weaker because it checks a category, not specific named tokens, and cannot confirm all three required slots were individually replaced.

**2. Copy-source citation chain: Phase 6 verdict sentence as named authority**
V-01's Phase 8 SEAL checked "matches Phase 4 TOTAL" — a match check that a silently-recomputed score can pass trivially. V-05 (and V-02/V-04) names the Phase 6 verdict sentence as the explicit copy source, not Phase 4. This creates an auditable chain: a scorer checks two sentences (Phase 6 verdict ↔ Phase 8 "This score"), and the copy source is a complete formatted sentence rather than a raw number in a table cell. V-05 adds "COPY-VERIFIED" label and explicitly forbids Phase 4 as the copy path.

**3. Format-contract seals covering all 9 phases close the partial-coverage gap**
V-01 through V-04 all had format strings on *most* seal fields but not *all* — value enumerations substituted for format specs in some fields (e.g., "exactly COVERED or EMPTY" vs `{COVERED|EMPTY}`). V-05 resolves this by applying the format-contract pattern uniformly: every field in every seal specifies both what must be present and what it must look like. This prevents a secondary failure mode where the field label is correct but the value form is wrong.

---

```json
{"top_score": 132, "all_essential_pass": true, "new_patterns": ["named-token slot guard: [slot:X] distinctive tokens make placeholder detection a mechanical string-level assertion rather than a judgment call", "copy-source citation chain: Phase 8 SEAL names Phase 6 verdict sentence as explicit copy authority, distinguishing auditable copy from a pass-through match check that silent recomputation can satisfy", "format-contract seal uniformity: applying explicit format strings to every field in every seal across all 9 phases closes the partial-coverage gap where value enumerations substituted for format specs"]}
```
