# listen-feedback — Round 8 Scoring

## Scoring Notes

Only **V-01** and **V-02** have complete prompt text. **V-03** provides a hypothesis but no prompt body. **V-04** and **V-05** are absent entirely. Scoring proceeds for V-01 and V-02; V-03 through V-05 are marked unscored.

---

## V-01 — Single Axis: Role Sequence

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | 12 persona cards present | **PASS** | "Generate one card per customer persona... C-01 through C-12" — count explicit |
| C-02 | NPS score and justification per card | **PASS** | `NPS: [1–10] (band)` + `Justification:` labeled field required per card |
| C-03 | Severity-labeled feedback per card | **PASS** | Template enumerates `[BLOCKING]`, `Major:`, `Minor:`, `Cosmetic:` with descending order instruction |
| C-04 | Aggregate NPS computed and threshold applied | **PASS** | "Compute aggregate NPS as the mean of all 12 persona scores. State the value explicitly. Apply threshold..." |
| C-05 | Cross-persona theme matrix present | **PASS** | PHASE 6 mandates table with columns: Theme / Personas / Highest Severity / Distribution |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| R-01 | Blocking issues escalated | **PASS** | PHASE 2 "Blockers Requiring Resolution" — collects `[BLOCKING]` items; "None" if absent |
| R-02 | PM and UX roles included | **PASS** | PHASE 3 UX READ + PHASE 4 PM READ, each 2+ sentences |
| R-03 | Theme matrix includes severity annotation | **PASS** | "Highest Severity: the worst severity level raised under this theme" — explicit column |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-01 | Persona-specific revision recommendations | **PASS** | "Revision recommendation: Required only if NPS < 6. State one concrete, actionable spec change..." |
| A-02 | NPS sensitivity analysis | **PASS** | "Identify the 2–3 personas whose scores most drive the aggregate mean" — correct framing |
| A-03 | Inline `[BLOCKING]` flags | **PASS** | Template line: `- [BLOCKING] [item] — if blocking, mark inline here` |
| A-04 | Ascending-NPS persona ordering | **PASS** | "ascending NPS order (lowest predicted score first, highest last). Ordering is required and must be explicit" |
| A-05 | Two-pass revision recommendations | **PASS** | "Two-pass revision summary: Collect all inline revision recommendations... Both passes must be present" |
| A-06 | Inertia-baseline NPS justification | **PASS** | "Must include an explicit comparison to the inertia baseline — what the persona currently does vs. what the spec offers" |
| A-07 | Severity-first within-card ordering | **PASS** | "List feedback in descending severity order: blocking first, then major, minor, cosmetic" |
| A-08 | NPS category-band annotation with aggregate distribution | **PASS** | Band in NPS line with definitions; aggregate section requires Detractor/Passive/Promoter counts + "Dominant Detractor objection:" field |
| A-09 | Named `Current approach:` field per card | **PASS** | `Current approach:` is the first named field in the card template |
| A-10 | `Dominant Detractor objection:` labeled field in aggregate | **PASS** | PHASE 5 contains labeled "Dominant Detractor objection:" with specific naming requirement |
| A-11 | Card header id/name/role only; `Current approach:` first body field | **PASS** | "Card header contains persona ID, name, and role only. NPS score must not appear in the header line. Current approach: is the first labeled field in the card body." |
| A-12 | UX READ precedes PM READ | **PASS** | "UX READ precedes PM READ. This ordering is required." — explicit rationale given |
| A-13 | Theme matrix as final synthesis section | **PASS** | "The theme matrix is the last substantive section. No PM READ, UX READ, sensitivity analysis, revision summary, or other major section appears after the theme matrix." |
| A-14 | Per-theme severity distribution counts | **PASS** | "Distribution: per-severity count for this theme row (e.g., '1 blocking, 3 major, 2 minor') — showing only highest severity does not satisfy this column" |
| A-15 | Aggregate-contribution framing in sensitivity analysis | **PASS** | "Do not frame this as 'convert these Detractors to clear the 7.0 threshold' — that selects different personas when the distribution is skewed" — explicit negative prohibition |

Aspirational subtotal: **75 / 75**

### V-01 Total: **165 / 165**

---

## V-02 — Single Axis: Output Format (Strict Structural Fields)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | 12 persona cards present | **PASS** | "Generate 12 persona cards (C-01 through C-12)" |
| C-02 | NPS score and justification per card | **PASS** | `**NPS:**` and `**Justification:**` as separate bold labeled fields |
| C-03 | Severity-labeled feedback per card | **PASS** | `**Feedback:**` with descending order rule + `[BLOCKING]` inline marker instruction |
| C-04 | Aggregate NPS computed and threshold applied | **PASS** | `**Aggregate NPS:**` and `**Threshold:** [Met ≥ 7.0 | Spec needs revision < 7.0]` as labeled fields |
| C-05 | Cross-persona theme matrix present | **PASS** | `### CROSS-PERSONA THEME MATRIX` table with Theme / Personas / Highest Severity / Distribution columns |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| R-01 | Blocking issues escalated | **PASS** | `### BLOCKERS REQUIRING RESOLUTION` section — "If none, write 'None.'" |
| R-02 | PM and UX roles included | **PASS** | `### UX READ` + `### PM READ` prescribed sections |
| R-03 | Theme matrix includes severity annotation | **PASS** | "Highest Severity: worst severity level raised under this theme" — explicit column rule |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-01 | Persona-specific revision recommendations | **PASS** | `**Revision recommendation:**` — "Required if NPS < 6. One concrete, actionable spec change." |
| A-02 | NPS sensitivity analysis | **PASS** | "Identify the 2–3 personas whose scores most drive the aggregate mean" |
| A-03 | Inline `[BLOCKING]` flags | **PASS** | "Mark blocking items inline: [BLOCKING] item text" |
| A-04 | Ascending-NPS persona ordering | **PASS** | "Present cards in ascending NPS order: lowest predicted NPS first, highest last. The ordering constraint is explicit — not alphabetical." |
| A-05 | Two-pass revision recommendations | **PASS** | "Revision summary (two-pass collection)" — "This is the second pass — inline card recommendations are the first pass. Both passes must be present..." |
| A-06 | Inertia-baseline NPS justification | **PASS** | "Must compare the spec's value proposition against the Current approach: field above. State explicitly what the persona gains or loses relative to their current behavior." |
| A-07 | Severity-first within-card ordering | **PASS** | "Listed in descending severity order: blocking before major before minor before cosmetic" |
| A-08 | NPS category-band annotation with aggregate distribution | **PASS** | Separate `**Band:**` field with definitions; `**Band distribution:**` in aggregate; `**Dominant Detractor objection:**` |
| A-09 | Named `Current approach:` field per card | **PASS** | `**Current approach:**` as first body field in template — bold labeled format |
| A-10 | `Dominant Detractor objection:` labeled field in aggregate | **PASS** | `**Dominant Detractor objection:**` — "Must be a named pattern... not a restatement of the band definition." |
| A-11 | Card header id/name/role only; `Current approach:` first body field | **PASS** | Header: `**[PERSONA ID] — [NAME], [ROLE]**` — no NPS. Body opens with `**Current approach:**` before `**NPS:**`. Ordering deterministic across 12 cards. |
| A-12 | UX READ precedes PM READ | **PASS** | "UX READ appears before PM READ — this ordering is required." |
| A-13 | Theme matrix as final synthesis section | **PASS** | "[This is the final substantive section. No section follows it except optional closing remarks.]" |
| A-14 | Per-theme severity distribution counts | **PASS** | "Distribution: count of feedback items per severity level for this theme — showing only the highest severity does not satisfy this column" |
| A-15 | Aggregate-contribution framing in sensitivity analysis | **PASS** | "Use aggregate-contribution framing: name the personas with the greatest mathematical weight on the mean — not the personas nearest the 7.0 threshold. In skewed distributions these are different sets." |

Aspirational subtotal: **75 / 75**

### V-02 Total: **165 / 165**

---

## V-03, V-04, V-05 — Not Scored

V-03 provides a hypothesis only; no prompt body present (only "placeholder" trace artifact appears where the prompt should be). V-04 and V-05 are absent from the variation set as provided.

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tie) | V-01 | 165 / 165 | Phase-sequencing with explicit prohibitions; negative prohibition on threshold framing |
| 1 (tie) | V-02 | 165 / 165 | Bold labeled fields throughout; separate Band field; tightest structural prescription |
| — | V-03 | N/A | Hypothesis only |
| — | V-04 | N/A | Not provided |
| — | V-05 | N/A | Not provided |

---

## Excellence Signals

**V-01 distinguishing technique:** Phase-numbered sequencing with explicit "do not reorder" prohibition. Adds rationale for each ordering decision (e.g., "UX craft framing establishes the foundation that PM synthesis builds on"). The negative prohibition on threshold-proximity framing is stated as a direct command with an example of the disallowed language.

**V-02 distinguishing technique:** Every structural field is a bold markdown labeled field — `**Current approach:**`, `**NPS:**`, `**Band:**`, etc. — removing any model discretion over field naming. The separate `**Band:**` field (with inline definitions) is marginally cleaner than V-01's combined `NPS: [score] (band)` line for A-08 structural inspection. A-15 is enforced via "not the personas nearest the 7.0 threshold. In skewed distributions these are different sets." — more compact than V-01's prohibition but equally specific.

**Shared pattern worth preserving:** Both prompts encode A-15 with an explicit counter-example of the disallowed framing. This "negative exemplar" technique — naming what the wrong output looks like — is new in R8 and likely explains why both prompts score 165 while prior rounds showed A-15 as a gap.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["negative-exemplar encoding: naming the disallowed framing pattern inline within the criterion instruction increases A-15 pass reliability"]}
```
