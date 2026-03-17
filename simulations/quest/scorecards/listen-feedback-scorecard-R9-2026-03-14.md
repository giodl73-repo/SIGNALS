# listen-feedback — Round 9 Scoring

## Summary

**V-01: 115 / 175** | **V-02: Partial (not computable)** | **V-03–V-05: Not provided**

---

### Essential + Recommended: Full pass on both (60 + 30)

All 5 essential and all 3 recommended criteria pass in V-01. No regression there.

---

### Aspirational: 25 / 85 (5 of 17 pass)

| Pass | Fail |
|------|------|
| A-03 inline blocking flags | A-01 revision recommendations |
| A-06 inertia-baseline comparison | A-02 sensitivity analysis |
| A-09 `Current approach:` field | A-04 ascending NPS ordering |
| **A-16** separate Band field ✓ | A-05 two-pass revision summary |
| **A-17** bilateral gains+losses ✓ | A-07 severity-first ordering |
| | A-08 band annotation + Detractor objection |
| | A-10 `Dominant Detractor objection:` field |
| | A-11 card header / Current approach: first |
| | A-12 UX READ before PM READ |
| | A-13 theme matrix as final section |
| | A-14 per-theme severity distribution |
| | A-15 aggregate-contribution framing |

---

### Key findings

**A-16 and A-17 both pass in V-01.** The new criteria are achievable — separate `**NPS:**` / `**Band:**` fields satisfy A-16 cleanly via template structure.

**Regression from R8.** R9 variations reset to fresh axes rather than extending R8's accumulated structure. Twelve aspirationals that R8 captured (A-01, A-02, A-04, A-05, A-07, A-08, A-10–A-15) are all dropped.

**New pattern for A-18.** V-02's partial prompt uses dedicated `**Gains from this spec:**` and `**Losses and switching costs:**` as separate required card fields — stronger structural enforcement of A-17 than a single justification field with a bilateral instruction. This is a candidate for a new aspirational criterion.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["V-02 enforces bilateral gains/losses via dedicated named fields (Gains from this spec, Losses and switching costs) as separate card template entries rather than a single justification field with bilateral requirement — structural separation makes A-17 verifiable by inspection, not by parsing prose"]}
```
 Theme matrix includes severity annotation | **PASS** | Theme matrix column "Highest Severity" is prescribed — "the highest severity level raised under this theme across all listed personas" |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-01 | Persona-specific revision recommendations | **FAIL** | Card template (fields 1–6) has no revision recommendation field. No revision instruction anywhere in Phase 2 or Phase 3. |
| A-02 | NPS sensitivity analysis | **FAIL** | Phase 3 contains "Aggregate NPS" and "Band Distribution" sections only. No instruction to identify personas whose scores most drive the aggregate mean. |
| A-03 | Inline [BLOCKING] flags | **PASS** | Feedback field uses `[severity: blocking/major/minor/cosmetic]` as inline prefix per item — blocking items are marked inline, satisfying the structural intent |
| A-04 | Ascending-NPS persona ordering | **FAIL** | Phase 2: "Produce one feedback card per persona, labeled C-01 through C-12." No ascending NPS ordering instruction. Roster order is fixed by persona ID, not score. |
| A-05 | Two-pass revision recommendations | **FAIL** | No revision recommendation field in card template; no revision summary phase. Neither pass exists. |
| A-06 | Inertia-baseline NPS justification | **PASS** | Justification field (field 6) requires comparison: "must name what this persona gains from adopting the spec AND what they lose or what switching cost they incur" — inertia baseline from `Current approach:` is the implicit reference |
| A-07 | Severity-first within-card ordering | **FAIL** | Feedback field says "List each feedback item with an explicit severity label" but does not specify descending severity order (blocking → major → minor → cosmetic). Order is unspecified. |
| A-08 | NPS category-band annotation with aggregate distribution | **FAIL** | Band Distribution section (Promoters / Passives / Detractors count) is present in Phase 3. However, no `Dominant Detractor objection:` labeled field appears in Phase 3 — the complete A-08 requires both. |
| A-09 | Named `Current approach:` field per card | **PASS** | Card field 2: `**Current approach:** [1–2 sentences — what this persona does today...]` — labeled field with exact name |
| A-10 | `Dominant Detractor objection:` labeled field in aggregate | **FAIL** | Phase 3 aggregate section contains only NPS list, mean, threshold, and band distribution counts. No `Dominant Detractor objection:` labeled field. |
| A-11 | Card header id/name/role only; `Current approach:` first body field | **FAIL** | Card field 1 is `**Persona:** [name and role]` — this is the first body field, not `Current approach:`. A-11 requires Current approach: as the first labeled field in the card body. Failed on two counts: Persona: precedes Current approach:, and PM Read is ordered before UX Read in Phase 1. |
| A-12 | UX READ precedes PM READ | **FAIL** | Phase 1 Output Order: "PM Read" then "UX Read" — PM precedes UX. A-12 requires UX before PM. Explicit ordering inversion. |
| A-13 | Theme matrix as final synthesis section | **FAIL** | Output Order: `... → Theme Matrix → Blockers Requiring Resolution`. Phase 5 (Blockers) follows Phase 4 (Theme Matrix). Theme matrix is not the last substantive section. |
| A-14 | Per-theme severity distribution counts | **FAIL** | Theme matrix column "Count" is count of personas raising the theme — not per-severity distribution (e.g., "1 blocking, 3 major, 2 minor"). No Distribution column present. |
| A-15 | Aggregate-contribution framing in sensitivity analysis | **FAIL** | No sensitivity analysis section. Not applicable. |
| A-16 | Band annotation is a separate labeled field | **PASS** | Card template field 4: `**NPS:** [integer 1–10]` and field 5: `**Band:** [Detractor / Passive / Promoter]` are distinct numbered fields on separate lines. Band is not parenthetical within the NPS line. |
| A-17 | NPS justification states both gains and losses relative to inertia baseline | **PASS** | Justification field explicitly requires both sides: "must name what this persona gains from adopting the spec AND what they lose or what switching cost they incur; for Promoter-tier personas with genuinely negligible friction, state 'no significant losses identified' with a one-sentence explanation" |

Aspirational subtotal: A-03, A-06, A-09, A-16, A-17 = **5 passes × 5 pts = 25 / 85**

### V-01 Total: **115 / 175**

---

## V-02 — Inertia Framing Axis (Partial)

V-02 is truncated at the persona roster line. The card template body and the phrase "Trace artifact (ground truth): placeholder" follow, but aggregate scoring, theme matrix, blocker escalation, PM Read, UX Read, and output ordering instructions are absent. Scoring proceeds only for criteria assessable from the visible card template.

### Partially Assessable Criteria (from card template only)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | 12 persona cards | **PASS** | "C-01 through C-12" roster referenced; 12 is explicit |
| C-02 | NPS + justification per card | **PASS** | `**NPS:** [1–10]` and `**NPS rationale:** [1–2 sentences tying score to gains/losses above]` — both present |
| C-03 | Severity-labeled feedback per card | **PASS** | `**Feedback:** - [severity: blocking/major/minor/cosmetic] [item]` |
| C-04 | Aggregate NPS computed | **UNKNOWN** | Section not present in provided text |
| C-05 | Theme matrix present | **UNKNOWN** | Section not present in provided text |
| R-01 | Blocking issues escalated | **UNKNOWN** | Not in provided text |
| R-02 | PM and UX roles included | **UNKNOWN** | Not in provided text |
| R-03 | Theme matrix severity annotation | **UNKNOWN** | Not in provided text |
| A-06 | Inertia-baseline NPS justification | **PASS** | "NPS rationale: Must reference both the inertia baseline and at least one gain or loss named above" — explicit bilateral |
| A-09 | Named `Current approach:` field | **FAIL** | First body field is `**Inertia baseline:**`, not `**Current approach:**` — the specific field name differs. A-09's pass condition requires the named label `Current approach:`. |
| A-16 | Band as separate labeled field | **PASS** | `**NPS:** [1–10]` and `**Band:** [Detractor / Passive / Promoter]` are separate bold labeled fields on distinct lines |
| A-17 | Bilateral gains and losses | **PASS** | V-02 EXCEEDS the A-17 bar: separate dedicated fields `**Gains from this spec:**` [1–3 sentences] and `**Losses and switching costs:**` [1–3 sentences] are required card fields, not just inline requirements. Structural separation makes bilateral coverage verifiable by inspection rather than by reading the justification text. |

V-02 partial score: **not computable** — C-04, C-05, R-01 through R-03 unknown; cannot calculate composite.

**Structural distinction worth noting:** V-02 satisfies A-17 via dedicated fields rather than an inline instruction within a combined Justification field. This is a stronger enforcement mechanism: the model cannot write a single Justification paragraph that mentions gains while omitting losses — the two sides are separate required fields. This structural approach is not captured by any existing A-01 through A-17 criterion.

---

## V-03, V-04, V-05 — Not Scored

V-03 through V-05 are not present in the provided variation set.

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | V-01 | **115 / 175** | All essential + recommended pass; A-16 and A-17 both pass; all other aspirationals regressed from R8 |
| — | V-02 | Partial | A-16, A-17 pass (stronger enforcement for A-17); A-09 fails on field name; C-04/C-05/R-01–R-03 unknown |
| — | V-03 | N/A | Not provided |
| — | V-04 | N/A | Not provided |
| — | V-05 | N/A | Not provided |

---

## Regression Analysis vs. R8

R8 V-01 and V-02 both achieved **165 / 165** against the v7 rubric. R9 V-01 achieves **115 / 175** against the v8 rubric. The apparent drop has two components:

1. **Rubric expansion (+10 pts new ceiling):** v8 adds A-16 (+5) and A-17 (+5). R9 V-01 PASSES both new criteria.

2. **Feature regression (–50 pts vs. R8):** R9 V-01 is a fresh-axis exploration. It drops A-01, A-02, A-04, A-05, A-07, A-08, A-10, A-11, A-12, A-13, A-14, A-15 — twelve aspirationals that R8 had accumulated. These were not intentionally removed; they are casualties of starting from a clean prompt skeleton focused on Role Sequence.

**Net finding:** The R9 variations demonstrate that A-16 and A-17 are achievable, but they do not incorporate R8's accumulated structure. To reach 175/175, a future variation must combine:
- R8's complete feature set (A-01 through A-15)
- R9's A-16 (separate Band field)
- R9's A-17 (bilateral gains+losses in justification)
- R9 V-02's dedicated fields approach as a stronger A-17 enforcement mechanism (candidate A-18)

---

## Excellence Signals

**V-01 R9 signal:** Separate `**NPS:**` and `**Band:**` fields (fields 4 and 5) as distinct numbered entries in the card template is the cleaner A-16 implementation — no prose instruction required, the template structure itself prevents inline band annotation.

**V-02 R9 signal (partial):** Dedicated `**Gains from this spec:**` and `**Losses and switching costs:**` fields as separate required card entries enforce A-17 structurally. The model cannot satisfy these fields with a single gains-only paragraph. This is a meaningfully stronger guarantee than V-01's instruction "must name gains AND losses" within a single Justification field. **This structural pattern is a candidate for A-18.**

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["V-02 enforces bilateral gains/losses via dedicated named fields (Gains from this spec, Losses and switching costs) as separate card template entries rather than a single justification field with bilateral requirement — structural separation makes A-17 verifiable by inspection, not by parsing prose"]}
```
