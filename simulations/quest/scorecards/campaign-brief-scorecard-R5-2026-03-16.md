```
campaign-brief / Round 5 — Scorecard written.
simulations/quest/scorecards/campaign-brief-scorecard-R5-2026-03-16.md
```

---

### Score Summary

| Var | Essential /50 | Recommended /30 | Aspirational /120 | Total /200 | Rank |
|-----|:---:|:---:|:---:|:---:|:---:|
| V-04 | **50** | **30** | **120** | **200** | 1 |
| V-05 | **50** | **30** | **120** | **200** | 1 |
| V-01 | **50** | **30** | 115 | 195 | 3 |
| V-02 | **50** | **30** | 115 | 195 | 3 |
| V-03 | **50** | **30** | 110 | 190 | 5 |

---

### Critical experiments — all confirmed

**Symmetry:** V-01 and V-02 each gain exactly +5 (unlike R4's asymmetric +5/+10). Both C-19 and C-20 were PARTIAL in the base, so each gains the same delta. C-19 and C-20 are structurally independent axes.

**Ceiling:** V-04 = 200/200. The v5 rubric has no unreachable criteria.

**V-04 vs V-05 identical:** Sparse-breadth clause is structurally inert on the rubric — C-04 and C-18 both hold PASS. V-05 is the preferred R6 base (zero rubric cost, structural robustness gain at sparse coverage).

---

### Excellence signals from V-04/V-05

1. **Output annotation closes the loop** — a rule in the execution note is PARTIAL; the same rule with output-visible annotation is PASS. Prompt-side enforcement is necessary but not sufficient.

2. **Explicit unit specification removes scale-dependent ambiguity** — "count blocking missing signals" implies entries but doesn't name it. The ambiguity is invisible at low gap count (entry count == line count) and only surfaces when multi-line entries appear at scale.

3. **Both changes are minimal and non-interfering** — V-04 required one sentence + one sub-section. 20-criterion ceiling reached with zero side effects.

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["output annotation closes the loop on prompt-side enforcement: execution note rule is PARTIAL; output-visible annotation is PASS", "explicit unit specification in structural thresholds removes scale-dependent ambiguity: name the type of thing and declare orthogonality", "C-19 and C-20 are structurally independent and symmetric: both PARTIAL in base, both gain exactly +5 to PASS with no interaction", "sparse-breadth robustness clause is structurally inert on the rubric: adds protection without affecting any scored criterion — prefer V-05 as R6 base"]}
```
 — first run` null value defined |
| C-10 | PASS | Standalone CONFIDENCE with 3-dimension table; arithmetic derivation required |
| C-11 | PASS | Dual `Assumption:` + `Consequence:` fields in FULL FORMAT and BLOCKING-DETAIL; reclassification rule: gaps incapable of both fields become optional |
| C-12 | PASS | "Prose is confined to the STORY block. All other blocks are structured data." |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE between STATUS and STORY; "do not embed inside STORY" |
| C-15 | PASS | FULL/COMPRESSED density contract with ≤4 blocking-gap threshold |
| C-16 | PASS | `<ns>/<artifact> <date>` per found-signal line — temporal audit without re-running |
| C-17 | PASS | Explicit PERMITTED/NOT PERMITTED list: five permitted forms, five named prohibited forms |
| C-18 | PASS | "The narrative must answer these three questions in sequence, in continuous prose" |
| C-19 | PARTIAL | Reclassification rule present in execution note ("A gap that cannot be answered with both fields is reclassified as optional") but output has no annotation for moved gaps — reader cannot see which gaps were reclassified or why |
| C-20 | PASS | Explicit sentence added: "The threshold counts blocking gap *entries* — each gap path is one entry regardless of how many fields follow it. A three-line entry (path + `Assumption:` + `Consequence:`) counts as one toward the ceiling, not three. Per-entry field count is orthogonal to the threshold." |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 115/120
**V-01 Total: 195/200**

*C-20 axis confirmed. The explicit entry-count sentence directly maps to C-20 PASS. C-19
remains PARTIAL — reclassification is enforced at execution but silent in output. Symmetric
with V-02: both gain exactly +5, confirming the two axes are structurally independent.*

---

## V-02 — Axis: C-19 reclassification output annotation

**Hypothesis tested:** Adding a `[RECLASSIFIED from BLOCKING:]` sub-section to STATUS —
with per-gap annotation naming which field was not articulable — makes the reclassification
visible in the output and closes C-19 PARTIAL independently. C-20 unchanged.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Block sequence enforced; TOPIC first |
| C-02 | PASS | STATUS `found:` enumerates `<ns>/<artifact> <date>` per line |
| C-03 | PASS | BLOCKING and OPTIONAL with explicit empty-case statement |
| C-04 | PASS | C-17 + C-18 both present unchanged |
| C-05 | PASS | TOPIC block with registration; all three fields required |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Assumption:` + `Consequence:` per blocking gap |
| C-08 | PASS | Eight named blocks; new RECLASSIFIED sub-section is structured data inside STATUS |
| C-09 | PASS | Full DELTA block mandatory; null value defined for first run |
| C-10 | PASS | Standalone CONFIDENCE block with derived table |
| C-11 | PASS | Dual fields required; reclassification rule enforced |
| C-12 | PASS | [RECLASSIFIED from BLOCKING:] is structured data inside STATUS — prose confined to STORY |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS; RECLASSIFIED sub-section adds a required visible field |
| C-14 | PASS | Standalone CONFIDENCE block |
| C-15 | PASS | Full density contract unchanged |
| C-16 | PASS | `<ns>/<artifact> <date>` per found-signal entry |
| C-17 | PASS | Explicit PERMITTED/NOT PERMITTED list unchanged |
| C-18 | PASS | Three-question mandate unchanged |
| C-19 | PASS | `[RECLASSIFIED from BLOCKING:]` sub-section in STATUS output; per-gap annotation `[reclassified: <Assumption | Consequence> not articulable]`; `RECLASSIFIED: none` when all gaps supply both fields — reclassification is visible in the output, not silent |
| C-20 | PARTIAL | Density contract says "Count blocking missing signals before formatting / Use FULL format if blocking gaps <= 4" — implies entry count but never explicitly states that per-entry field count is orthogonal; the distinction has not been named |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 115/120
**V-02 Total: 195/200**

*C-19 axis confirmed. Output annotation of reclassification moves the rule from execution-only
to output-visible, satisfying C-19 PASS. C-20 remains PARTIAL. The two axes are confirmed
symmetric: V-01 gains +5 on C-20; V-02 gains +5 on C-19. Neither change creates side effects
on any other criterion.*

---

## V-03 — Axis: C-18 sparse-breadth resilience clause (robustness only)

**Hypothesis tested:** Adding a sparse-breadth clause to the STORY execution note —
"the three-question structure applies at all coverage levels; question 1 is permitted to
be brief but must state what direction even partial evidence points" — prevents synthesis
collapse at narrow signal breadths without introducing a contradiction with C-04 or C-18.
Expected: 190/200, identical to base. C-19 and C-20 unchanged.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Block sequence enforced; TOPIC first |
| C-02 | PASS | STATUS `found:` enumerates per-line with dates |
| C-03 | PASS | BLOCKING and OPTIONAL with empty-case statement |
| C-04 | PASS | C-17 + C-18 both present; sparse-breadth clause reinforces synthesis requirement — "must state what direction even partial evidence points" — does not weaken synthesis bar |
| C-05 | PASS | TOPIC block with registration |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Assumption:` + `Consequence:` per blocking gap |
| C-08 | PASS | Eight named blocks |
| C-09 | PASS | Full DELTA block |
| C-10 | PASS | Standalone CONFIDENCE block |
| C-11 | PASS | Dual fields required; reclassification rule enforced |
| C-12 | PASS | Prose confined to STORY |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` |
| C-14 | PASS | Standalone CONFIDENCE block |
| C-15 | PASS | Full density contract unchanged |
| C-16 | PASS | `<ns>/<artifact> <date>` per found-signal entry |
| C-17 | PASS | PERMITTED/NOT PERMITTED list unchanged |
| C-18 | PASS | Three-question mandate unchanged; sparse-breadth clause adds robustness for narrow signal states without removing the structural guarantee — "the structure cannot be omitted on the grounds of sparse data" |
| C-19 | PARTIAL | Reclassification rule in execution note, no output annotation (unchanged from base) |
| C-20 | PARTIAL | Entry-count orthogonality unspecified (unchanged from base) |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 110/120
**V-03 Total: 190/200**

*Robustness improvement confirmed without rubric interaction. Sparse-breadth clause strengthens
C-18's behavior at extreme inputs but does not change C-18 score (already PASS). C-04 PASS
holds: "permitted to be brief" is bounded by "must state what direction" — synthesis cannot be
omitted. No contradictions with any scored criterion detected. V-03 is a structural improvement
to the base, not a rubric-gap closure.*

---

## V-04 — Axes: C-20 + C-19 combined (ceiling attempt)

**Hypothesis tested:** Both output-fidelity changes — explicit entry-count statement (V-01)
and reclassification annotation (V-02) — applied simultaneously achieve 200/200. All rubric
criteria are reachable with no unreachable gaps.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Block sequence enforced: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL], CONFIDENCE, STORY, VERDICT |
| C-02 | PASS | STATUS `found:` enumerates `<ns>/<artifact> <date>` per line |
| C-03 | PASS | BLOCKING and OPTIONAL with empty-case explicit; reclassification enforced |
| C-04 | PASS | C-17 PERMITTED/NOT PERMITTED + C-18 three-question mandate — both present, both active |
| C-05 | PASS | TOPIC block with registration; name, date, intent required |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Assumption:` + `Consequence:` per blocking gap — item-level inertia cost visible |
| C-08 | PASS | Eight named blocks; RECLASSIFIED sub-section is structured data in STATUS |
| C-09 | PASS | Full DELTA mandatory; `prior_brief: NONE — first run` null value defined |
| C-10 | PASS | Standalone CONFIDENCE with 3-dimension table; arithmetic derivation required |
| C-11 | PASS | Dual `Assumption:` + `Consequence:` fields; reclassification rule enforced; gaps incapable of both fields become optional |
| C-12 | PASS | Prose confined to STORY; RECLASSIFIED sub-section is structured data |
| C-13 | PASS | `coverage: X/(X+Y) = Z%`; RECLASSIFIED sub-section adds visible required field |
| C-14 | PASS | Standalone CONFIDENCE between STATUS and STORY |
| C-15 | PASS | FULL/COMPRESSED density contract with ≤4 blocking-gap threshold |
| C-16 | PASS | `<ns>/<artifact> <date>` per found-signal line |
| C-17 | PASS | Explicit PERMITTED/NOT PERMITTED: five permitted, five named prohibited forms |
| C-18 | PASS | "The narrative must answer these three questions in sequence, in continuous prose" |
| C-19 | PASS | `[RECLASSIFIED from BLOCKING:]` sub-section with per-gap annotation; `RECLASSIFIED: none` when no gaps moved; reclassification visible in output, not silent |
| C-20 | PASS | Explicit sentence: "The threshold counts blocking gap *entries* — each gap path is one entry regardless of how many fields follow it. A three-line entry counts as one toward the ceiling, not three. Per-entry field count is orthogonal to the threshold." |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 120/120
**V-04 Total: 200/200**

*Ceiling achieved. V-04 confirms the v5 rubric has no unreachable criteria. Both C-19 and C-20
were closed with targeted, minimal changes — one sentence added (C-20) and one output sub-section
added (C-19). No interaction effects between the two changes. No other criteria were affected.*

---

## V-05 — Axes: C-20 + C-19 + C-18 sparse-breadth (full three-axis sweep)

**Hypothesis tested:** V-05 applies all three axes simultaneously. Expected: 200/200,
identical to V-04. The sparse-breadth clause (C-18 robustness) should not add or subtract
from the rubric score — any difference would indicate an interaction with C-04 or C-18.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Block sequence enforced |
| C-02 | PASS | STATUS `found:` enumerates per-line with dates |
| C-03 | PASS | BLOCKING and OPTIONAL; reclassification enforced with output annotation |
| C-04 | PASS | C-17 + C-18 both active; sparse-breadth clause preserves synthesis requirement under narrow signal states — "must state what direction even partial evidence points" |
| C-05 | PASS | TOPIC block with registration |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Assumption:` + `Consequence:` per blocking gap |
| C-08 | PASS | Eight named blocks |
| C-09 | PASS | Full DELTA mandatory; null value defined |
| C-10 | PASS | Standalone CONFIDENCE block with derived table |
| C-11 | PASS | Dual fields required; reclassification rule enforced |
| C-12 | PASS | Prose confined to STORY; sparse-breadth clause is execution note, not prose |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` |
| C-14 | PASS | Standalone CONFIDENCE block |
| C-15 | PASS | Full density contract |
| C-16 | PASS | `<ns>/<artifact> <date>` per found-signal entry |
| C-17 | PASS | PERMITTED/NOT PERMITTED list; sparse-breadth clause does not modify the prohibited forms list |
| C-18 | PASS | Three-question mandate present; sparse-breadth clause adds structural protection against omission at sparse breadth — "the structure cannot be omitted on the grounds of sparse data" — does not weaken the mandate |
| C-19 | PASS | [RECLASSIFIED from BLOCKING:] sub-section with per-gap annotation (V-02 change included) |
| C-20 | PASS | Explicit entry-count orthogonality statement (V-01 change included) |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 120/120
**V-05 Total: 200/200**

*V-05 = V-04 confirmed. The sparse-breadth clause is structurally inert on the rubric — no
criterion gains or loses points. C-04 holds PASS: the clause adds protection against a failure
mode (synthesis collapse at sparse breadth) but does not introduce a contradiction. C-18 holds
PASS: the clause strengthens enforcement, not weakens. V-04 and V-05 are the recommended
implementations — select V-05 as base for R6 for the robustness benefit at no scoring cost.*

---

## Score Summary

| Var | Essential /50 | Recommended /30 | Aspirational /120 | Total /200 | Rank |
|-----|--------------|-----------------|-------------------|-----------|------|
| V-04 | **50** | **30** | **120** | **200** | 1 |
| V-05 | **50** | **30** | **120** | **200** | 1 |
| V-01 | **50** | **30** | 115 | 195 | 3 |
| V-02 | **50** | **30** | 115 | 195 | 3 |
| V-03 | **50** | **30** | 110 | 190 | 5 |

---

## Critical Experiment Results

**C-19 and C-20 symmetry: CONFIRMED**

| Test | C-19 | C-20 | Score | Delta vs base |
|------|------|------|-------|---------------|
| V-01 (C-20 only) | PARTIAL | PASS | 195 | +5 |
| V-02 (C-19 only) | PASS | PARTIAL | 195 | +5 |
| V-04 (both) | PASS | PASS | 200 | +10 |

V-01 and V-02 each gain exactly +5. The result is symmetric — unlike R4 where V-01 gained +5
and V-02 gained +10 due to asymmetric base states. In R5 both C-19 and C-20 were PARTIAL (5 pts
each) in the base, so each axis gains exactly +5 to PASS. This confirms C-19 and C-20 are
structurally independent axes with no interaction.

**V-04 ceiling: CONFIRMED**

200/200 in V-04 confirms the v5 rubric is complete. All 20 criteria are reachable. The rubric
has no unreachable ceiling — every criterion can be satisfied through targeted, non-conflicting
prompt changes.

**V-04 vs V-05 identical: CONFIRMED**

Both score 200/200. The sparse-breadth clause is structurally inert on the rubric. No criterion
changes score between V-04 and V-05. C-04 PASS holds under the clause because the clause adds
protection (cannot omit synthesis on grounds of sparse data) without granting an omission
escape hatch.

**V-03 robustness: NO INTERACTION**

V-03 = 190/200 = base score. The sparse-breadth clause targets behavior at extreme inputs without
affecting any scored criterion. This confirms V-05 is strictly additive: V-04 rubric score +
V-03 robustness improvements = 200/200 + no regressions.

---

## Excellence Signals from V-04/V-05

**What makes V-04 and V-05 the top scorers:**

1. **Output annotation closes the loop on prompt-side enforcement.** The reclassification rule
was present in R4 V-05's execution note (C-11 PASS). But C-19 PASS requires the effect to be
visible in the output — the reader must see which gaps moved and why. A rule that exists only in
the execution instruction is PARTIAL; the same rule with an output-visible annotation is PASS.
This is the pattern: prompt-side enforcement is necessary but not sufficient — the output must
also annotate the enforcement effect.

2. **Explicit unit specification in structural thresholds removes ambiguity at scale.** The
density contract said "count blocking missing signals" — which implies entry count but does not
name it. C-20 PASS requires naming the counting unit and declaring orthogonality. This ambiguity
does not surface when gap count is low and each gap has one line; it surfaces when multi-line
entries (path + Assumption + Consequence) appear at scale. The lesson: any threshold that counts
"things" must name the type of thing and declare what doesn't count against it.

3. **Both changes are minimal, targeted, and non-interfering.** V-04 required: one explicit
sentence in the density contract (C-20) + one output sub-section (C-19). No other criterion
was affected. The progressive decomposition model holds at 20-criterion ceiling: each new
criterion is independently addressable without touching the others.

4. **V-05 preferred over V-04 as R6 base.** The sparse-breadth clause adds structural
protection against a known failure mode (STORY synthesis collapse at 1-2 namespace coverage)
at zero rubric cost. R6 should include V-05 as base.

---

## R6 Design Guidance

V-05 is the base for R6. The 20-criterion ceiling has been reached.

**R6 scope:** No new rubric gaps exist. R6 should focus on:

1. **Stress testing at coverage extremes.** The density contract and reclassification rule have
been validated structurally but not against live output at 0 signals found, 1 signal found, or
all-blocking gap states. Verify each structural contract holds under extreme inputs.

2. **C-19 reclassification frequency.** In practice, how often do blocking gaps fail to supply
both Assumption and Consequence? If reclassification is rare, the `RECLASSIFIED: none` default
case dominates. If it is common, the mechanism provides high value. Either finding informs
whether C-19 warrants a weight increase in v6.

3. **COMPRESSED format C-16 interaction.** R4 guidance flagged: do per-signal timestamps
survive in COMPRESSED format or are they lost? If timestamps are lost when COMPRESSED triggers,
C-16 only partially satisfies at high gap counts. Investigate as a v6 criterion candidate.

---

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["output annotation closes the loop on prompt-side enforcement: a rule in the execution note is PARTIAL; the same rule with output-visible annotation is PASS — prompt-side enforcement is necessary but not sufficient", "explicit unit specification in structural thresholds removes scale-dependent ambiguity: any threshold counting things must name the type of thing and declare orthogonality to other representations", "C-19 and C-20 are structurally independent and symmetric: both were PARTIAL (+5) in base, both gain exactly +5 to PASS, no interaction — confirmed by V-01/V-02 symmetric scores", "sparse-breadth robustness clause is structurally inert on the rubric: V-03 and V-05 both confirm the clause adds protection without affecting any scored criterion — prefer V-05 as R6 base for zero-cost robustness"]}
```
