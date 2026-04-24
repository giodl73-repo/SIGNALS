Good — I have the scorecard format. Now I'll write the full scorecard.

---

## Round 5 Scorecard — listen-feedback

### Criterion-by-Criterion Evaluation

**Legend:** PASS / PARTIAL / FAIL — evidence note

---

#### V-01: Phrasing register — conversational/descriptive

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 12 personas | PASS | All 12 listed in PERSONAS block |
| C-02 | Severity tags | PASS | Template shows blocking/major/minor/cosmetic labels |
| C-03 | NPS per persona + justification | PASS | Phase 1 per-persona format includes NPS + 1-sentence rationale |
| C-04 | Aggregate NPS + threshold | PASS | "Aggregate NPS = sum / 12" + PASS/FAIL + REVISION REQUIRED if below |
| C-05 | Theme matrix | PASS | Phase 4 THEME MATRIX with table format |
| R-01 | Blocking escalated | PASS | Phase 3 BLOCKING ITEMS section, explicit result required |
| R-02 | PM + UX reads | PASS | Phase 4 PM READ + UX READ both present |
| R-03 | Theme matrix severity | PASS | `Highest Severity` column in matrix; inertia/spec-specific classification |
| A-01 | Revision recs NPS < 6 | PASS | "For any persona with NPS below 6, add a revision rec" with specificity bar |
| A-02 | NPS sensitivity analysis | PASS | Phase 4 NPS SENSITIVITY ANALYSIS with leverage framing + highest-ROI change |
| A-03 | Inline [BLOCKING] | PASS | `[BLOCKING]` marker in card template; Phase 3 draws from inline tags |
| A-04 | Ascending NPS order | **FAIL** | Soft gate: "Make sure Phase 1 is complete... before moving to Phase 2." Phase 1 scores personas in list order then instructs "list them in ascending order" — but no hard stop prevents card writing before the ascending sort is committed. Model may score and begin Phase 2 in scoring order rather than sorted order. |
| A-05 | Two-pass revision recs | PASS | Inline rec in Phase 2 ("Revision rec:" template) + "REVISION RECS SUMMARY" in Phase 3 — both explicitly labeled |
| A-06 | Inertia baseline NPS | PASS | "does this feature beat what they currently do? Name the net benefit and the switching cost from the inertia baseline" |
| A-07 | Severity-first within card | PASS | "Feedback items (blocking first, then major, minor, cosmetic)" |
| A-08 | Band labels + aggregate distribution | PASS | Phase 1 shows Promoters/Passives/Detractors counts; band definitions given in preamble |
| A-09 | `Current approach:` labeled field | PASS | `Current approach:` label + colon in card template, before NPS |
| A-10 | `Dominant Detractor objection:` field | PASS | Labeled field in Phase 1 aggregate with specificity bar |
| A-11 | Header id/name/role only; body `Current approach:` first | PASS | Header template `[C-NN] [Name] ([Role])` — no NPS; body starts `Current approach:` → `NPS:` → feedback |

**V-01 Score: 140/145** (A-04 fails: −5)

---

#### V-02: Inertia-led framing — status-quo comparison as organizing principle

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 12 personas | PASS | All 12 in STOCK PERSONAS block |
| C-02 | Severity tags | PASS | Card template lists blocking/major/minor/cosmetic |
| C-03 | NPS per persona + justification | PASS | Per-persona: NPS + "Status-quo verdict" 1 sentence |
| C-04 | Aggregate NPS + threshold | PASS | "Aggregate NPS = sum / 12. Show calculation." + PASS/FAIL + REVISION REQUIRED |
| C-05 | Theme matrix | PASS | Phase 4 THEME MATRIX with table |
| R-01 | Blocking escalated | PASS | Phase 3 BLOCKING ITEMS, explicit result |
| R-02 | PM + UX reads | PASS | Phase 4 PM READ + UX READ |
| R-03 | Theme matrix severity | PASS | `Highest Severity` column + inertia-driven/spec-specific classification |
| A-01 | Revision recs NPS < 6 | PASS | "For any persona with NPS < 6: include a REVISION REC immediately after their items" |
| A-02 | NPS sensitivity analysis | PASS | Phase 4 NPS SENSITIVITY ANALYSIS with leverage + highest-ROI change |
| A-03 | Inline [BLOCKING] | PASS | `[BLOCKING]` in card template; Phase 3 verifies by leading-item scan |
| A-04 | Ascending NPS order | PASS | Hard gate: "Do not proceed to Phase 2 until all 12 scores, ascending list, category breakdown, dominant Detractor objection, and aggregate result are stated." Phase 1 commits ascending sort before cards begin. |
| A-05 | Two-pass revision recs | PASS | Inline REVISION REC in Phase 2 + "REVISION RECS SUMMARY" labeled section in Phase 3 |
| A-06 | Inertia baseline NPS | PASS | "Band label must follow from this comparison: Detractor = switching cost wins… Persona preference description alone does not qualify as a verdict." |
| A-07 | Severity-first within card | PASS | "Feedback items (most severe first)" + template shows blocking → major → minor → cosmetic |
| A-08 | Band labels + aggregate distribution | PASS | Promoters/Passives/Detractors counts in Phase 1; band definitions in preamble |
| A-09 | `Current approach:` labeled field | PASS | Labeled field in card template, before NPS |
| A-10 | `Dominant Detractor objection:` field | PASS | Labeled field in Phase 1 aggregate; specificity bar: "must be a named inertia pattern (e.g., 'migration effort…'). Not a restatement of the Detractor band definition." |
| A-11 | Header id/name/role only; body `Current approach:` first | PASS | Header `[C-NN] [Name] ([Role])` only; body: `Current approach:` → `NPS:` → feedback |

**V-02 Score: 145/145** (all criteria pass)

---

#### V-03: Phase compaction — 3-phase (SCORE, FEEDBACK CARDS, ANALYSIS)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 12 personas | PASS | All 12 in STOCK PERSONAS block |
| C-02 | Severity tags | PASS | Card template: blocking/major/minor/cosmetic |
| C-03 | NPS per persona + justification | PASS | Per-persona: NPS + "Rationale: 1 sentence grounding the category in the inertia comparison" |
| C-04 | Aggregate NPS + threshold | PASS | "Aggregate NPS = sum / 12. Show calculation." + PASS/FAIL + REVISION REQUIRED |
| C-05 | Theme matrix | PASS | Phase 3 THEME MATRIX with table |
| R-01 | Blocking escalated | PASS | Phase 3 BLOCKING ITEMS with explicit result |
| R-02 | PM + UX reads | PASS | Phase 3 PM READ + UX READ |
| R-03 | Theme matrix severity | PASS | `Highest Severity` column + inertia-driven/spec-specific classification |
| A-01 | Revision recs NPS < 6 | PASS | "For any persona with NPS < 6 (Detractor): include a REVISION REC immediately after their items" |
| A-02 | NPS sensitivity analysis | PASS | Phase 3 NPS SENSITIVITY ANALYSIS with leverage framing + highest-ROI change |
| A-03 | Inline [BLOCKING] | PASS | `[BLOCKING]` in card template; Phase 3 BLOCKING ITEMS "verification: check each card's leading feedback item(s), then confirm the inline [BLOCKING] tag" |
| A-04 | Ascending NPS order | PASS | Hard gate: "Do not proceed to Phase 2 until all 12 scores, ascending list, category breakdown, dominant Detractor objection, and aggregate result are stated." |
| A-05 | Two-pass revision recs | PASS | Inline REVISION REC in Phase 2 + "REVISION RECS SUMMARY" in Phase 3 ANALYSIS — both labeled, both required |
| A-06 | Inertia baseline NPS | PASS | "does this feature beat what they do today? Net benefit vs. switching cost from the baseline?" |
| A-07 | Severity-first within card | PASS | "Feedback items (descending severity — blocking first)" |
| A-08 | Band labels + aggregate distribution | PASS | Promoters/Passives/Detractors counts in Phase 1; band definitions in preamble |
| A-09 | `Current approach:` labeled field | PASS | Labeled field before NPS in card template |
| A-10 | `Dominant Detractor objection:` field | PASS | Labeled field in Phase 1 aggregate with specificity bar; "not a band definition restatement" |
| A-11 | Header id/name/role only; body `Current approach:` first | PASS | Header `[C-NN] [Name] ([Role])`; body: `Current approach:` → `NPS:` → feedback |

**Key test — A-05 with collapsed ESCALATE phase:** Phase 3 (ANALYSIS) opens with BLOCKING ITEMS and REVISION RECS SUMMARY as the first two sections, followed by THEME MATRIX/PM READ/UX READ/SENSITIVITY. "Complete all six sections in order. No section may be omitted." The inline rec in Phase 2 and the collected REVISION RECS SUMMARY in Phase 3 both satisfy A-05's two-pass requirement. The ESCALATE phase boundary is organizational overhead — the pass condition is two dedicated sections, not two dedicated phases.

**V-03 Score: 145/145** (all criteria pass — ESCALATE phase confirmed non-load-bearing)

---

#### V-04: Role sequence — UX READ first, theme matrix as final synthesis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 12 personas | PASS | All 12 in STOCK PERSONAS block |
| C-02 | Severity tags | PASS | Card template: blocking/major/minor/cosmetic |
| C-03 | NPS per persona + justification | PASS | Per-persona NPS + inertia-framed rationale |
| C-04 | Aggregate NPS + threshold | PASS | Aggregate + PASS/FAIL + REVISION REQUIRED |
| C-05 | Theme matrix | PASS | Phase 4 THEME MATRIX (last section) with table |
| R-01 | Blocking escalated | PASS | Phase 3 BLOCKING ITEMS |
| R-02 | PM + UX reads | PASS | Phase 4: UX READ → PM READ both present |
| R-03 | Theme matrix severity | PASS | `Highest Severity` column preserved; position change doesn't affect pass |
| A-01 | Revision recs NPS < 6 | PASS | Inline REVISION REC for NPS < 6 |
| A-02 | NPS sensitivity analysis | PASS | Phase 4 NPS SENSITIVITY ANALYSIS |
| A-03 | Inline [BLOCKING] | PASS | `[BLOCKING]` in card template; Phase 3 verification |
| A-04 | Ascending NPS order | PASS | Hard gate in Phase 1 |
| A-05 | Two-pass revision recs | PASS | Inline in Phase 2 + REVISION RECS SUMMARY in Phase 3 |
| A-06 | Inertia baseline NPS | PASS | "does this feature beat what they do today?" |
| A-07 | Severity-first within card | PASS | "descending severity — blocking first" |
| A-08 | Band labels + aggregate distribution | PASS | Phase 1 counts + band definitions |
| A-09 | `Current approach:` labeled field | PASS | First body field in card template |
| A-10 | `Dominant Detractor objection:` field | PASS | Phase 1 aggregate labeled field |
| A-11 | Header id/name/role only; body `Current approach:` first | PASS | Header template unchanged |

**Note on role sequence effect:** PM READ now explicitly draws on "the UX switching-friction analysis above" — creating a stated dependency that may improve PM READ quality, while UX READ references "steepest conceptual transition, and what specific interaction or design assumption creates that gap" (more precise than V-05 R4's UX framing). Theme matrix as final synthesis "incorporating the UX and PM lenses above" may produce better inertia-vs-spec classification.

**V-04 Score: 145/145** (all criteria pass)

---

#### V-05: Combined — inertia-led (V-02) + 3-phase (V-03) + UX-first (V-04)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 12 personas | PASS | All 12 in STOCK PERSONAS block |
| C-02 | Severity tags | PASS | Card template: blocking/major/minor/cosmetic |
| C-03 | NPS per persona + justification | PASS | Per-persona NPS + "Status-quo verdict" with explicit net-benefit/switching-cost framing |
| C-04 | Aggregate NPS + threshold | PASS | "Aggregate NPS = sum / 12. Show calculation." + PASS/FAIL + REVISION REQUIRED |
| C-05 | Theme matrix | PASS | Phase 3 THEME MATRIX (final section) |
| R-01 | Blocking escalated | PASS | Phase 3 BLOCKING ITEMS, first section in ANALYSIS |
| R-02 | PM + UX reads | PASS | Phase 3: UX READ → PM READ |
| R-03 | Theme matrix severity | PASS | `Highest Severity` column + inertia-driven/spec-specific |
| A-01 | Revision recs NPS < 6 | PASS | Inline REVISION REC for NPS < 6 |
| A-02 | NPS sensitivity analysis | PASS | Phase 3 NPS SENSITIVITY ANALYSIS |
| A-03 | Inline [BLOCKING] | PASS | `[BLOCKING]` in card template; Phase 3 BLOCKING ITEMS collects from inline tags |
| A-04 | Ascending NPS order | PASS | Hard gate: "Do not proceed to Phase 2 until all 12 scores, ascending list, category breakdown, dominant Detractor objection, and aggregate result are stated." |
| A-05 | Two-pass revision recs | PASS | Inline REVISION REC in Phase 2 + "REVISION RECS SUMMARY" in Phase 3 — both labeled, both required by "No section may be omitted" |
| A-06 | Inertia baseline NPS | PASS | "Band label must follow from the comparison: Detractor = switching cost wins; Promoter = net benefit wins. Persona preference description alone is not a verdict." |
| A-07 | Severity-first within card | PASS | "most severe first" + template shows blocking → major → minor → cosmetic |
| A-08 | Band labels + aggregate distribution | PASS | Phase 1 counts; band definitions in preamble |
| A-09 | `Current approach:` labeled field | PASS | First body field: "specific tool, workflow, or behavior; not a role description" |
| A-10 | `Dominant Detractor objection:` field | PASS | Phase 1 aggregate; "the specific status-quo attachment or switching-cost pattern…; not a band definition restatement" |
| A-11 | Header id/name/role only; body `Current approach:` first | PASS | Header `[C-NN] [Name] ([Role])` only; body: `Current approach:` → `NPS:` → feedback |

**Interference check:** Three combined axes (inertia-led framing, 3-phase compaction, UX-first sequence) were each confirmed safe at 145 individually. The combined prompt is shorter than V-05 R4. No instruction shrinkage creates criterion risk: all labels remain explicit, phase gate remains hard, card template is fully specified, "No section may be omitted" covers all six ANALYSIS outputs.

**V-05 Score: 145/145** (all criteria pass — no axis interference)

---

### Summary Scorecard

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (55) | Score | Golden? |
|------|-----------|---------------|-----------------|-------------------|-------|---------|
| 1 | V-02 Inertia-led framing | 60/60 | 30/30 | 55/55 | **145** | YES |
| 1 | V-03 Phase compaction | 60/60 | 30/30 | 55/55 | **145** | YES |
| 1 | V-04 Role sequence | 60/60 | 30/30 | 55/55 | **145** | YES |
| 1 | V-05 Combined | 60/60 | 30/30 | 55/55 | **145** | YES |
| 5 | V-01 Phrasing register | 60/60 | 30/30 | 50/55 | **140** | NO |

---

### The single discriminator: A-04

V-01 fails A-04 (ascending NPS order) due to soft phase gate language. The deciding text:

| Variation | Gate language | A-04 |
|-----------|---------------|------|
| V-01 | "Make sure Phase 1 is complete… before moving to Phase 2" | FAIL |
| V-02–V-05 | "Do not proceed to Phase 2 until…" | PASS |

**Imperative gate language is structural**, not stylistic. The risk is not that a model ignores the ascending sort instruction — it's that a model begins card writing while interleaving Phase 1 scoring, never committing the Phase 1 ascending list as an output before Phase 2 starts. Soft gates permit that interleaving; hard gates prevent it.

---

### V-03 finding: ESCALATE phase is organizational overhead

V-03 proves the 4-phase structure in V-05 R4 was over-engineering. The load-bearing requirements for all criteria are:
1. A dedicated "BLOCKING ITEMS" section (satisfies R-01 + A-03's second half)
2. A dedicated "REVISION RECS SUMMARY" section (satisfies A-05's second pass)

Neither requires a separate phase boundary — both survive inside a single ANALYSIS phase when labeled sections are explicitly required. V-05 R4's ESCALATE/SYNTHESIZE split added phase boundary overhead with no criterion benefit.

---

### Excellence Signals (from 145-scoring variations)

**From V-02:** Status-quo comparison as the organizing question ("does this proposal beat the status quo?") tightens `Current approach:` field specificity and `Dominant Detractor objection:` synthesis — the persona's current behavior is the direct answer to the organizing question, not an optional structural field. Raises output quality without changing any pass/fail boundary.

**From V-03:** Phase compaction to 3 phases (SCORE → FEEDBACK CARDS → ANALYSIS) is sufficient for all 19 criteria. The ESCALATE phase boundary can be eliminated in all future variations — this is the recommended default structure going forward.

**From V-04:** UX-before-PM role sequence creates an explicit analytical dependency: PM READ draws on "the UX switching-friction analysis above," and the THEME MATRIX at the end incorporates both lenses. This is strictly superior to PM-before-UX because PM adoption analysis benefits from UX friction findings; UX friction analysis does not benefit from PM adoption framing.

**From V-05:** The three safe axes (inertia-led framing + 3-phase + UX-first) combine cleanly at 145 with no interference. The combined prompt is shorter and more readable than V-05 R4 with the same structural guarantee ceiling.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["imperative-phase-gate-is-load-bearing-for-ascending-nps-sort", "escalate-phase-boundary-is-organizational-overhead-3-phase-sufficient"]}
```
