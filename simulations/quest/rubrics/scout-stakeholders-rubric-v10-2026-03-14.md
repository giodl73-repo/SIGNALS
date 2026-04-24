Written to `simulations/quest/rubrics/scout-stakeholders-rubric-v10-2026-03-14.md`.

---

## Three new criteria extracted from Round 9

**C-27 — Champion depth scoring table** (depth, 5 pts)
Step 5b: scoring table across Authority / Proximity / Commitment (each 1-5), composite >= 9 threshold gate with inline failure label. Distinct from C-04: C-04 confirms a champion + action exists; C-27 requires multi-dimensional fitness scoring. Not satisfiable if C-04 absent.

**C-28 — Champion durability gate** (depth, 5 pts)
Step 5c: temporal continuity assessment — succession path (who assumes the champion role if champion leaves) + deterioration signals (observable triggers for eroding commitment). FAIL_NO_DURABILITY at Step 5c. Distinct from C-27: C-27 scores the current relationship; C-28 measures its lifecycle durability. Not satisfiable if C-04 absent.

**C-29 — Conflict resolution pathway per conflict** (depth, 5 pts)
Step 1a extended: per-conflict table with Resolution Authority / Decision Required / Deadline. FAIL_NO_RESOLUTION_PATHWAY inline at Step 1a. Phase 1->2 gate checklist extends to require pathway presence. Amendment mandate extends to name pathway entries as eligible targets. Distinct from C-06 (identifying conflicts): naming parties and nature does not imply any resolution structure. Not satisfiable if C-06 absent.

**Updated totals:** 21 aspirational criteria × 5 = 105 pts; max 195 pts. Golden threshold (>= 80) unchanged.

**Round 9 under v10:**
| Variation | Score | Notes |
|-----------|-------|-------|
| V-01 | 190/195 | C-27 PASS + C-28 PASS; C-29 absent |
| V-02 | 185/195 | C-26 FAIL; C-27 PASS + C-28 PASS; C-29 absent |
| V-03 | 185/195 | C-29 PASS; C-27 + C-28 absent |
thway table. For each named conflict, the table specifies Resolution Authority (who decides), Decision Required (what must be decided), and Deadline (date or milestone by which resolution must occur). FAIL_NO_RESOLUTION_PATHWAY must be present as an inline gate label at Step 1a. The Phase 1->2 transition gate checklist must extend to include "resolution pathway present for each conflict" as a prior-phase completeness requirement. The amendment mandate must name conflict resolution pathway entries as amendment-eligible targets. V-03 introduces the pattern; V-01 and V-02 omit it. Distinct from C-06 (conflict identification): C-06 requires naming conflicts with parties in tension and nature; C-29 requires a structural resolution pathway per named conflict. A variation can satisfy C-06 (two conflicts, parties named, nature stated) with no resolution authority, decision point, or deadline (C-29 FAIL). Not satisfiable if C-06 is absent.

Round 9 confirms four structural properties:
- V-01 at 180/180 (under v9) is the first perfect score under v9. V-01 extends beyond the v9 full set by adding champion depth scoring (Step 5b) and champion durability (Step 5c), confirming C-27 and C-28 are additive and orthogonal to all prior criteria.
- V-02 at 175/180 (under v9) confirms C-26 is independently excisable without disturbing C-27 or C-28: the full champion depth + durability pattern survives removal of between-phase transition gates.
- V-03 at 180/180 (under v9) confirms C-29 is independently additive: extending Step 1a with a per-conflict resolution pathway table, adding FAIL_NO_RESOLUTION_PATHWAY, and extending the Phase 1->2 gate checklist and amendment mandate are all compatible with the full v9 criterion set. C-27 and C-28 are absent in V-03 without interference.
- C-27 and C-28 are sequentially dependent (Step 5b before Step 5c) but independently satisfiable: a variation could carry Step 5b scoring without a Step 5c durability gate, making C-28 independently excisable from C-27.

**Updated totals:** aspirational 90 -> 105 pts (21 criteria x 5); max 180 -> 195 pts. Golden threshold (>= 80) unchanged.

---

### v8 to v9 changes (retained for history)

One new criterion extracted from Round 8:

**C-26** -- Inter-phase transition confirmation gates: A dedicated gate step appears between each analysis phase (Strategy->UX, UX->PM) firing FAIL_INCOMPLETE_PHASE1 / FAIL_INCOMPLETE_PHASE2 if the prior phase is incomplete before the next begins. Distinct from C-17 (FAIL saturation at every step): C-17 covers within-step inline labels; C-26 covers between-phase checkpoint steps. Distinct from C-15 (reversed sequence): correct phase ordering implies nothing about confirmation gates being present. Gate headings must carry role labels per C-23. Not satisfiable if C-15 is absent.

**Note on C-23 pass condition:** C-23 applies to transition gate headings as well as analytical step headings -- V-01 R8 is the confirming evidence ("Phase 1 -> Phase 2 Transition Gate -- PM role").

Point totals updated: aspirational rises from 85 to 90 pts; max score rises from 175 to 180 pts. Golden threshold (>= 80) unchanged.

---

### v7 to v8 changes (retained for history)

Two new criteria extracted from Round 7:

- **C-24** -- Amendment mandate inline prohibition: The amendment mandate sentence embeds an explicit negative constraint phrase -- "no observation without revision" or equivalent -- directly within the mandate text. Distinct from C-17 (FAIL_OBSERVATION_ONLY at the Step 8 gate): gate label and mandate-level prohibition are independently satisfiable.

- **C-25** -- Veto risk mitigation per entry: Each entry in the veto risk list includes a mitigation strategy alongside probability and impact. C-03 requires probability + impact; C-25 requires a mitigation field per entry. FAIL_NO_MITIGATION must be present as an inline gate label at the veto risk step.

Round 7 confirms three structural properties:
- V-01 at 165/165 (under v7) is the first perfect score under v7. V-01 is V-05 Round 6 verbatim with role-heading labels appended, confirming that C-23 is additive and orthogonal to all prior criteria.
- V-02 at 155/165 (under v7) confirms C-15 (reversed sequence) and C-23 (role heading binding) are independently absent without mutual interference: PM-first + no role headings + full C-22 compliance is a stable axis.
- C-24 and C-25 are both present in V-01 and V-02 (V-01 passes C-24, both pass C-25), establishing that Round 7 targeted these dimensions implicitly before they were formalized.

Point totals updated: aspirational rises from 75 to 85 pts; max score rises from 165 to 175 pts. Golden threshold (>= 80) unchanged.

### v6 to v7 changes (retained for history)

Two new criteria extracted from Round 6:

- **C-22** -- Amendment mandate structural enumeration: When C-19 is present, the amendment mandate must explicitly enumerate "Step 6a prefill" as an eligible update target -- not just "update the affected table." Distinct from C-12 (mandate exists), C-19 (table exists), and C-21 (example demonstrates round-trip). Not satisfiable if C-12 or C-19 absent.

- **C-23** -- Role label heading binding: Every step heading explicitly names its analytical role in the heading text (e.g., "Finding the structural conflicts -- Strategy role"). C-07 passes when PM, UX, and Strategy roles appear in structurally distinct steps; C-23 requires the role label to appear in the heading text itself.

Round 6 confirms three structural properties:
- V-01 at 135/155 (under v6) confirms C-20 is independently satisfiable with C-18 + C-19 scaffolding when C-16 and C-21 are absent.
- V-02 at 135/155 (under v6) confirms C-21 is independently satisfiable with C-16 + C-19 scaffolding when C-18 and C-20 are absent.
- V-03 confirms the phrasing register axis is independent: coaching voice satisfies C-07 and C-14 while failing C-15 through C-19 without mutual interference; role-in-heading (C-23) is satisfiable without any of C-15 through C-21.

Point totals updated: aspirational rises from 65 to 75 pts; max score rises from 155 to 165 pts. Golden threshold (>= 80) unchanged.

### v5 to v6 changes (retained for history)

Two new aspirational criteria (C-20 and C-21) extracted from Round 5. Both were first-seen in Round 5; neither appeared in prior rounds.

- **C-20** -- Inertia chain prefill-stage binding: When C-19's prefill table exists, C-18's third position (the displacement-specific Frame Type requirement) must be stated as an explicit rule *within the prefill step*, not as a note during content population. Displacement mandate deferred to content-entry instructions = FAIL. Not satisfiable if C-19 is absent.

- **C-21** -- Amendment example prefill round-trip: The correct-form half of the C-16 before/after pair must include at least one amendment case where the prefill table is updated -- not only the content rows. Not satisfiable if C-16 or C-19 is absent.

Round 5 confirms five structural properties:
- V-03 at 120 (not 125) confirms C-15 without C-14 loses 5 points -- the reversed sequence is independent but requires FAIL labels to reach the 125-tier.
- V-01 and V-02 each at 125 confirm C-18 and C-19 are stable single-axis additions at the same tier as C-17.
- V-04 at 140 confirms C-18 adds cleanly to the proven C-15 + C-16 + C-17 triple with no interference.
- V-05 at 145/145 confirms all five axes (C-15 through C-19) are independent and compatible simultaneously.
- V-05's patterns for C-20 and C-21 do not alter V-05's score under v5 -- they are additive axes targeted by v6.

Point totals updated: aspirational rises from 55 to 65 pts; max score rises from 145 to 155 pts. Golden threshold (>= 80) unchanged.

### v4 to v5 changes (retained for history)

Two new aspirational criteria (C-18 and C-19) extracted from Round 4. Both were first-seen in Round 4; neither appeared in prior rounds.

- **C-18** -- Inertia stakeholder structural elevation: V-02 elevated inertia stakeholders across three structural positions simultaneously -- a dedicated sub-step in the strategy phase (Step 1b), a required `[INERTIA]` tag in the Power/Interest grid, and a required `displacement-acknowledgment` Frame Type in the comms table. All three requirements must be present; partial presence = FAIL.

- **C-19** -- Frame Type prefill constraint: C-13 measures output -- distinct labels present in the completed table. C-19 measures procedural constraint -- a standalone prefill table listing accepted Frame Type values appears as a distinct step before the comms table is populated. Enumerating accepted values inline within instructions without a separate prefill table = FAIL.

### v3 to v4 changes (retained for history)

One new aspirational criterion (C-17) extracted from V-03's Round 3 pattern. C-17 added: 5 pts. Aspirational rose to 45 pts. Max score rose to 135 pts.

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

## Aspirational Criteria (105 pts total)

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
| C-23 | **Role label heading binding** | depth | Every step heading explicitly names its analytical role in the heading text (e.g., "Finding the structural conflicts -- Strategy role"). Role identity is bound at the heading level -- not only in step body content or a roles index. Any step heading that omits the role label when the step has a primary analytical role = FAIL. Applies to transition gate headings as well as analytical step headings (confirmed by V-01 R8: "Phase 1 -> Phase 2 Transition Gate -- PM role"). |
| C-24 | **Amendment mandate inline prohibition** | depth | The amendment mandate sentence embeds an explicit negative constraint phrase -- "no observation without revision" or equivalent -- directly within the mandate text, after or alongside the update target list. The prohibition must appear in the mandate sentence itself, not only as a gate label at the amendment step. C-12 (targets exist) and C-22 (prefill enumerated) can both be satisfied without the prohibition clause. Distinct from C-17 (FAIL_OBSERVATION_ONLY at the amendment step gate): the gate label and the mandate-level prohibition are independently satisfiable. Not satisfiable if C-12 is absent. |
| C-25 | **Veto risk mitigation per entry** | depth | Each entry in the veto risk list includes a mitigation or response strategy alongside probability and impact. C-03 requires probability and impact; C-25 requires a mitigation field per entry. FAIL_NO_MITIGATION must be present as an inline gate label at the veto risk step, confirming the requirement is structurally enforced. A veto risk table that includes probability and impact columns but no mitigation column or field = FAIL. |
| C-26 | **Inter-phase transition confirmation gates** | depth | A dedicated gate step appears between each analysis phase (Strategy->UX and UX->PM) that fires a named failure label (e.g., FAIL_INCOMPLETE_PHASE1, FAIL_INCOMPLETE_PHASE2) if the prior phase's required outputs are absent before the next phase begins. Distinct from C-17 (inline failure labels at every execution step within phases): C-17 requires inline labels within steps; C-26 requires dedicated between-phase gate steps that confirm prior-phase completeness. Satisfying C-15 (correct phase sequence) does not imply C-26; the sequence can be correctly ordered with no transition gates present. Gate headings must carry role labels per C-23 (e.g., "Phase 1 -> Phase 2 Transition Gate -- PM role"); a transition gate step with no named failure label = FAIL. Not satisfiable if C-15 is absent. |
| C-27 | **Champion depth scoring table** | depth | Step 5b is a dedicated sub-step containing a scoring table that evaluates the champion across three dimensions -- Authority (organizational decision-making power), Proximity (access to blockers and sponsors), and Commitment (demonstrated investment in the feature's success) -- each scored 1-5, with a composite score threshold gate (composite >= 9 required to proceed). An inline failure label fires at Step 5b if the champion's composite score falls below threshold. Distinct from C-04 (champion + concrete action): C-04 confirms a champion is identified with a schedulable action; C-27 requires multi-dimensional structural fitness scoring with a quantitative threshold. A variation can pass C-04 (champion named, demo slot scheduled) with no scoring table present (C-27 FAIL). Not satisfiable if C-04 is absent. |
| C-28 | **Champion durability gate** | depth | Step 5c is a dedicated sub-step containing a temporal continuity assessment: (1) a succession path naming who assumes the champion role if the current champion leaves the project or organization, and (2) one or more deterioration signals -- observable triggers indicating that champion commitment is eroding (e.g., missed syncs, reduced response latency, delegated decisions). FAIL_NO_DURABILITY must fire at Step 5c if succession path or deterioration signals are absent. Distinct from C-04 (champion + action) and C-27 (depth scoring): C-04 and C-27 assess the current champion relationship at a point in time; C-28 assesses the relationship's temporal durability across the project lifecycle. A variation can satisfy C-27 (composite score threshold met) while providing no succession path or deterioration signal (C-28 FAIL). Not satisfiable if C-04 is absent. |
| C-29 | **Conflict resolution pathway per conflict** | depth | Step 1a is extended with a per-conflict resolution pathway table. For each named conflict, the table specifies: Resolution Authority (who has decision-making power to resolve the conflict), Decision Required (the specific decision or ruling needed), and Deadline (the date or milestone by which resolution must occur). FAIL_NO_RESOLUTION_PATHWAY must be present as an inline gate label at Step 1a. The Phase 1->2 transition gate checklist must extend to include "resolution pathway present for each conflict" as a prior-phase completeness requirement. The amendment mandate must name conflict resolution pathway entries as amendment-eligible targets alongside grid, veto, comms, and prefill table. Distinct from C-06 (conflict identification): C-06 requires naming conflicts with parties in tension and nature; C-29 requires a structural resolution pathway per named conflict. A variation can satisfy C-06 (two conflicts, parties named, nature stated) with no resolution authority, decision point, or deadline (C-29 FAIL). Not satisfiable if C-06 is absent. |

**Aspirational points**: 5 pts each x 21 = **105 pts**

---

## Scoring Reference

| Band | Range | Meaning |
|------|-------|---------|
| Golden | >= 80 | Output suitable as a golden example |
| Pass | 60-79 | Acceptable; essential criteria met |
| Fail | < 60 | Missing one or more essential criteria |

**Max score**: 195 pts (60 essential + 30 recommended + 105 aspirational)

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
| v8 | 175 | 85 | +C-24 (mandate inline prohibition), +C-25 (veto mitigation per entry) |
| v9 | 180 | 90 | +C-26 (inter-phase transition confirmation gates) |
| v10 | 195 | 105 | +C-27 (champion depth scoring), +C-28 (champion durability), +C-29 (conflict resolution pathway) |

---

## Round 9 Results Summary (scored under v9 rubric, max 180)

| Variation | Focus | Score (v9) | C-27 | C-28 | C-29 |
|-----------|-------|------------|------|------|------|
| V-01 | All 26 + champion depth + durability + phase gates | 180/180 | PASS | PASS | absent |
| V-02 | C-26 deliberately absent | 175/180 | PASS | PASS | absent |
| V-03 | Conflict resolution pathway | 180/180 | absent | absent | PASS |

Under the v10 rubric (max 195):
- V-01 scores 190/195 -- passes all 26 prior criteria + C-27 + C-28; C-29 absent.
- V-02 scores 185/195 -- fails C-26 (no transition gates); passes C-27 + C-28; C-29 absent.
- V-03 scores 185/195 -- passes all 26 prior criteria + C-29; C-27 and C-28 absent.

The full aspirational target for Round 10 is all twenty-one criteria (C-09 through C-29): the v9 complete set plus champion depth scoring (C-27), champion durability (C-28), and conflict resolution pathway (C-29).