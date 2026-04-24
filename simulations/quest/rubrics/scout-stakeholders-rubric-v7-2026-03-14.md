Written to `simulations/quest/rubrics/scout-stakeholders-rubric-v7-2026-03-14.md`.

---

**Two new criteria extracted from Round 6:**

**C-22 — Amendment mandate structural enumeration** (depth, 5 pts)
Source: V-02's C-12 evidence. When C-19 is present, the amendment mandate must explicitly enumerate "Step 6a prefill" as an eligible update target — not just "update the affected table." V-01 passes C-12 but fails C-22 (non-enumerating mandate). Distinct from C-12 (mandate exists), C-19 (table exists), and C-21 (example demonstrates round-trip): a variation can satisfy all three and still fail C-22 with a generic mandate. Not satisfiable if C-12 or C-19 absent.

**C-23 — Role label heading binding** (depth, 5 pts)
Source: V-03's C-07 evidence. Every step heading explicitly names its analytical role ("Finding the structural conflicts — Strategy role"). C-07 passes with roles in distinct steps; C-23 requires the label in the heading itself. V-01 and V-02 fail C-23 (formal FAIL-label format, no heading-embedded roles). V-03 demonstrates the inverse tradeoff: C-23 satisfied, C-17 absent.

**Updated totals**: aspirational 65 → 75 pts; max 155 → 165 pts. Golden threshold (>= 80) unchanged.

**Round 6 scores under v7**: V-01 = 135/165 (unchanged), V-02 = 140/165 (+C-22), V-03 = 125/165 (+C-23).
role to step at the heading level. Every step heading explicitly names its analytical role (e.g., "Finding the structural conflicts — Strategy role"). C-07 passes when PM, UX, and Strategy roles appear in structurally distinct steps; C-23 requires the role label to appear in the heading text itself. A variation can satisfy C-07 (roles in distinct steps) and fail C-23 (headings omit role labels). V-01 and V-02 use formal FAIL-label format without heading-embedded roles; V-03 demonstrates the inverse tradeoff — role-in-heading binding present, FAIL saturation (C-17) absent.

Round 6 also confirms three structural properties:
- V-01 at 135/155 (under v6) confirms C-20 is independently satisfiable with C-18 + C-19 scaffolding when C-16 and C-21 are absent.
- V-02 at 135/155 (under v6) confirms C-21 is independently satisfiable with C-16 + C-19 scaffolding when C-18 and C-20 are absent.
- V-03 confirms the phrasing register axis is independent: coaching voice satisfies C-07 and C-14 while failing C-15 through C-19 without mutual interference; role-in-heading (C-23) is satisfiable without any of C-15 through C-21.

Point totals updated: aspirational rises from 65 to 75 pts; max score rises from 155 to 165 pts. Golden threshold (>= 80) is unchanged.

### v5 to v6 changes (retained for history)

Two new aspirational criteria (C-20 and C-21) extracted from Round 5. Both were first-seen in Round 5; neither appeared in prior rounds.

- **C-20** — Inertia chain prefill-stage binding: V-05 established that when C-19's prefill table exists, C-18's third position (the displacement-specific Frame Type requirement) must be stated as an explicit rule *within the prefill step*, not as a note during content population. V-04 passes C-18 with a `displacement-acknowledgment` mandate inline at the communications step — the requirement exists but lives at content-entry time. V-05 moves it upstream: Step 6a rule 3 explicitly assigns `displacement-acknowledgment` to the inertia row *before* any rows are populated, and FAIL_MISSING_DISPLACEMENT_PREFILL fires at that gate. All three inertia positions must be present (C-18), the prefill table must exist (C-19), *and* the displacement assignment must be made in the prefill step — not deferred to content entry. Displacement mandate in content instructions only = FAIL.

- **C-21** — Amendment example prefill round-trip: V-05's C-16 correct-form pair extends through both structural levels. The correct-form amendment example must include at least one case where the prefill table (Step 6a) is updated — not only the content rows (Step 6b). V-05 demonstrates: "Step 6a prefill updated — Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly." V-04 passes C-16 but its amendment example targets grid/veto/comms updates only; no prefill table exists in V-04, so the round-trip cannot be demonstrated. C-21 is only satisfiable when C-16 and C-19 are both present; a correct-form example that shows only 6b content updates without a corresponding 6a prefill update = FAIL.

Round 5 also confirms five structural properties:
- V-03 at 120 (not 125) confirms C-15 without C-14 loses 5 points — the reversed sequence is independent but requires FAIL labels to reach the 125-tier.
- V-01 and V-02 each at 125 confirm C-18 and C-19 are stable single-axis additions at the same tier as C-17.
- V-04 at 140 confirms C-18 adds cleanly to the proven C-15 + C-16 + C-17 triple with no interference.
- V-05 at 145/145 confirms all five axes (C-15 through C-19) are independent and compatible simultaneously.
- V-05's patterns for C-20 and C-21 do not alter V-05's score under v5 — they are additive axes targeted by v6.

Point totals updated: aspirational rises from 55 to 65 pts; max score rises from 145 to 155 pts. Golden threshold (>= 80) is unchanged.

### v4 to v5 changes (retained for history)

Two new aspirational criteria (C-18 and C-19) extracted from Round 4. Both were first-seen in Round 4; neither appeared in prior rounds.

- **C-18** — Inertia stakeholder structural elevation: V-02 elevated inertia stakeholders across three structural positions simultaneously — a dedicated sub-step in the strategy phase (Step 1b), a required `[INERTIA]` tag in the Power/Interest grid, and a required `displacement-acknowledgment` Frame Type in the comms table. No prior variation treated inertia as a first-class structural element rather than an incidentally-included grid row. All three requirements must be present; partial presence (e.g., displacement note in comms but no grid tag) = FAIL.

- **C-19** — Frame Type prefill constraint: V-03's diagnostic in v4 explicitly flagged this as a v5 candidate: "The prefill pattern targets C-13 in a different way than the rubric currently measures." C-13 measures output — distinct labels present in the completed table. C-19 measures procedural constraint — a standalone prefill table listing accepted Frame Type values appears as a distinct step *before* the comms table is populated, constraining which values are allowed. Enumerating accepted values inline within instructions (V-01, V-02, V-04 pattern) does not satisfy C-19.

### v3 to v4 changes (retained for history)

One new aspirational criterion (C-17) extracted from V-03's Round 3 pattern. The criterion was explicitly flagged in v3 as a v4 candidate pending confirmation; Round 3 confirmed it. C-17 added: 5 pts. Aspirational rose to 45 pts. Max score rose to 135 pts.

### v2 to v3 changes (retained for history)

Two new aspirational criteria (C-15 and C-16) extracted from V-04's Round 2 perfect score. C-15 enforces analysis-before-synthesis structurally (reversed sequence: Strategy -> UX -> PM). C-16 requires the amendment anti-pattern shown as an adjacent before/after pair, not just a positive rule.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **CODEOWNERS fallback** | correctness | Org context check is the first step. Ask one question if absent. "Never infer silently" or equivalent must be present. |
| C-02 | **Power/Interest grid present** | correctness | Grid has 4+ rows with quadrant labels. Power and Interest values or descriptors present for each row. Prose-only stakeholder list with no grid = FAIL. |
| C-03 | **Veto risks ranked by probability** | correctness | Veto risk list is present, ordered by probability rank. Each entry includes probability + impact. Order must reflect probability rank, not alphabetical or grid order. |
| C-04 | **Champion with concrete action** | correctness | One or more stakeholders labelled champion with a specific action (e.g., "give demo slot", "co-present", "early access"). Generic "engage champion" language = FAIL. |
| C-05 | **Communication strategy per quadrant** | depth | Four quadrant rows are present, each with a distinct message and at least a relative timing signal (e.g., "3 weeks before", "now", "day of"). |

**Essential points**: 12 pts each x 5 = **60 pts**

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Conflict identification** | depth | Two or more distinct conflicts named, each identifying the stakeholder groups in tension and the nature of the conflict. Single-stakeholder risks do not count as conflicts. |
| C-07 | **Role framing** | coverage | All three roles (PM / Strategy / UX) structurally separated into distinct sections or steps. Collapsed into one section = FAIL. Named but not separated (partial) = 5 pts. |
| C-08 | **Critical-path gatekeepers flagged** | correctness | One or more gatekeepers tagged critical-path with a deadline or lead-time note. Generic "important" label without timing = FAIL. |

**Recommended points**: 10 pts each x 3 = **30 pts**

---

## Aspirational Criteria (75 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment phase** | depth | One or more distinct findings not in the initial grid -- adds, splits, or reframes a stakeholder. Absent amendment section = FAIL. |
| C-10 | **"What we are NOT doing" framing** | coverage | One or more sentences or rows describing what the product does not do for a gatekeeper. Generic "out of scope" = FAIL. |
| C-11 | **Source-tracking column in grid** | depth | Grid has a Source column or per-row origin label. Each row has an origin (e.g., "CODEOWNERS", "initial-inventory", "conflict discovery"). Missing = FAIL. |
| C-12 | **Amendment loop with update mandate** | correctness | Amendment section explicitly instructs updating the grid, veto list, or comms table -- not just observing findings. "Note the finding" alone = FAIL. |
| C-13 | **Prefilled frame types in comms table** | coverage | Communication table has a Frame Type column with a distinct label per quadrant row. Same frame on two or more rows = FAIL. |
| C-14 | **Named failure modes inline** | coverage | Two or more inline anti-pattern labels placed at the steps where those failures occur. Generic warnings in a preamble do not count. |
| C-15 | **Reversed sequence (analysis-before-synthesis)** | depth | Steps are explicitly ordered: conflict/strategy analysis first, UX segment analysis second, PM grid construction last. PM must build the grid after conflicts and segments are identified. Grid-first order = FAIL. |
| C-16 | **Amendment anti-pattern as before/after pair** | correctness | Amendment section shows the bad form (observation without revision) immediately adjacent to the correct form (update + note what changed) as a paired example. Positive instruction alone without a bad-form example = FAIL. |
| C-17 | **Anti-pattern saturation at every phase gate** | coverage | Every execution step carries at least one named failure mode inline. A single gate without an inline failure label = FAIL. Two+ labels total (C-14) is necessary but not sufficient; coverage must be complete across all steps. |
| C-18 | **Inertia stakeholder structural elevation** | depth | Three requirements all present: (1) a dedicated sub-step in the strategy phase for inertia stakeholder mapping, (2) a required `[INERTIA]` tag or equivalent in the Power/Interest grid for inertia-classified stakeholders, and (3) a required displacement-specific Frame Type (e.g., `displacement-acknowledgment`) for inertia rows in the comms table. Any one of the three absent = FAIL. |
| C-19 | **Frame Type prefill constraint table** | coverage | A standalone prefill table listing accepted Frame Type values appears as a distinct step before the comms table is populated. The prefill table must function as a constraint -- values not in the prefill table are prohibited. Enumerating accepted values inline within instructions without a separate prefill table = FAIL. |
| C-20 | **Inertia chain prefill-stage binding** | depth | When a prefill table is present (C-19 satisfied), the displacement-specific Frame Type requirement for inertia stakeholders must be stated as an explicit rule *within the prefill step* -- not as a note during content population. The prefill step must mandate the inertia row's Frame Type assignment before any rows are populated, with a corresponding inline failure label (e.g., FAIL_MISSING_DISPLACEMENT_PREFILL) at the prefill gate. Displacement mandate deferred to content-entry instructions = FAIL. Not satisfiable if C-19 is absent. |
| C-21 | **Amendment example prefill round-trip** | correctness | The correct-form half of the C-16 before/after pair must include at least one amendment case where the prefill table is updated -- not only the content rows. The example must show both the prefill table revision (Frame Type reassigned) and the corresponding content-row update as a complete round-trip. A correct-form example that updates only content rows without a corresponding prefill update = FAIL. Not satisfiable if C-16 or C-19 is absent. |
| C-22 | **Amendment mandate structural enumeration** | depth | When a prefill table is present (C-19 satisfied), the amendment mandate (C-12) explicitly enumerates Step 6a prefill as one of the eligible structural update targets alongside grid, veto, and comms rows. A mandate that states only "update the affected table" without naming structural levels = FAIL. Enumerating content-level targets only (grid, veto, comms) without naming the prefill table = FAIL. Not satisfiable if C-12 or C-19 is absent. |
| C-23 | **Role label heading binding** | depth | Every step heading explicitly names its analytical role in the heading text (e.g., "Finding the structural conflicts -- Strategy role"). Role identity is bound at the heading level -- not only in step body content or a roles index. Any step heading that omits the role label when the step has a primary analytical role = FAIL. |

**Aspirational points**: 5 pts each x 15 = **75 pts**

---

## Scoring Reference

| Band | Range | Meaning |
|------|-------|---------|
| Golden | >= 80 | Output suitable as a golden example |
| Pass | 60-79 | Acceptable; essential criteria met |
| Fail | < 60 | Missing one or more essential criteria |

**Max score**: 165 pts (60 essential + 30 recommended + 75 aspirational)

---

## Version History

| Version | Max | Aspirational | Changes |
|---------|-----|--------------|---------|
| v2 | 120 | 30 | Baseline essential + recommended |
| v3 | 130 | 40 | +C-15 (reversed sequence), +C-16 (amendment pair) |
| v4 | 135 | 45 | +C-17 (FAIL saturation) |
| v5 | 145 | 55 | +C-18 (inertia elevation), +C-19 (prefill constraint) |
| v6 | 155 | 65 | +C-20 (prefill binding), +C-21 (amendment round-trip) |
| v7 | 165 | 75 | +C-22 (mandate enumeration), +C-23 (role heading binding) |

---

## Round 6 Results Summary (scored under v6 rubric, max 155)

| Variation | Focus | Score (v6) | C-20 | C-21 | C-22 | C-23 |
|-----------|-------|------------|------|------|------|------|
| V-01 | C-20 alone: prefill-stage inertia binding | 135/155 | PASS | FAIL | FAIL | FAIL |
| V-02 | C-21 alone: amendment prefill round-trip | 135/155 | FAIL | PASS | PASS | FAIL |
| V-03 | Phrasing register: conversational/coaching | 120/155 | FAIL | FAIL | FAIL | PASS |

Under the v7 rubric (max 165): V-01 scores 135/165 (fails C-22 and C-23). V-02 scores 140/165 (gains C-22; fails C-23). V-03 scores 125/165 (gains C-23; C-22 not satisfiable due to absent C-19).

The full aspirational target for Round 7 is all fifteen criteria (C-09 through C-23): the v6 complete set plus amendment mandate structural enumeration (C-22) and role label heading binding (C-23).
