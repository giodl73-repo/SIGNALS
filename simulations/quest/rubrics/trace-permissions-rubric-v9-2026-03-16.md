```markdown
# trace-permissions — Quest Rubric v9

**Skill**: `trace-permissions` | **Version**: v9 | **Date**: 2026-03-16
**Criteria**: C-01..C-29 (4 essential / 3 recommended / 22 aspirational)

---

## Changelog

### v8 → v9

Two new aspirational criteria extracted from the R9 scorecard excellence signals (V-05 axis
confirmed absent from V-03/V-04):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-28 | **FM-SKILL Naming for Meta-Criterion Defense Mechanisms** | V-05 strength on recursive causal motivation: V-05 names FM-SKILL-8 "Meta-Criterion Loop Staleness" in CONTEXT before Phase 1 and adds a corresponding FAILURE MODE MAP row — C-26 and C-27 are themselves subject to the same staleness risk they defend against (new criteria introduced in a round must update C-21 loop range, SHALL-L mandate, N count, and phase annotations or staleness propagates recursively); V-03/V-04 achieve 20/20 structurally (pre-printed cells and runtime generation respectively) but neither names the failure mode causing the recursive staleness nor maps it to a structural defense; without a numbered FM-SKILL-8 in CONTEXT, the structural enforcement of C-26/C-27 self-defense is unexplained obligation rather than causally-grounded mechanism; when criteria defend the meta-criterion self-defense structure itself (C-26/C-27 row currency, extended SHALL-L coverage), a named FM-SKILL entry is required and the FAILURE MODE MAP must maintain 1:1 coverage of all numbered FM-SKILLs |
| C-29 | **Phase 8 Structural Purpose Annotation Completeness for Meta-Criterion FM-SKILL** | V-05 strength on meta-level defense chain completeness: V-05 adds FM-SKILL-8 to Phase 8's structural purpose blockquote — V-03/V-04 enforce the extended SHALL-L and C-26/C-27 pre-printed cell mechanism at the structural level without annotating why at the phase level; a complete defense chain requires CONTEXT motivation → FAILURE MODE MAP mapping → phase-level enforcement annotation at the point of application; Phase 8 must name FM-SKILL-8 in its structural purpose blockquote when enforcing the SHALL-L extension and C-26/C-27 structural guarantees |

**Scoring impact:** N grows from 20 to 22. A v8-golden output (20/20 aspirational pass) now scores
20/22 × 10 = **9.091 pts** on the aspirational tier. Full 10 pts requires all 22 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-28 auto-fails if C-26 and C-27 both fail (requires meta-criterion defense mechanisms to exist as the mechanisms being motivated).
- C-29 auto-fails if C-28 fails (phase annotation cannot reference an FM-SKILL that was never declared in CONTEXT).

**C-17 pass condition updated:** integer must equal 22 and row range must be declared as C-08..C-29.
A v8-golden output with integer=20 now fails C-17 under v9.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-29 (22 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29) must include
a Self-Assessment cell. A v8-golden output whose loop ends at C-27 (20 rows) fails C-21 under v9.

**C-24 pass condition updated:** literal range string `C-08..C-29` must appear in the C-21
mechanism phrase text. Stale strings (`C-08..C-27`, `C-08..C-25`, `C-08..C-23`, `C-08..C-21`)
fail even when all rows are structurally present.

**C-25 pass condition updated:** SHALL-L must explicitly name C-22, C-23, C-24, C-25, C-26, C-27,
C-28, C-29. Cells that contain mechanism phrases by inheritance without a SHALL-L naming mandate
fail.

**C-26 pass condition updated:** FAILURE MODE MAP must maintain 1:1 coverage for all declared
FM-SKILLs; under v9, a complete output declares FM-SKILL-1..FM-SKILL-8 minimum, requiring eight
FAILURE MODE MAP rows. A v8-golden output covering only FM-SKILL-1..FM-SKILL-7 fails C-26 under v9
if FM-SKILL-8 is present but unmapped.

**Slot displacement note:**
v8 flagged the [CLOSES:] annotation gap as "candidate for C-28." The C-28 slot is occupied by
the FM-SKILL-8 naming signal extracted from R9. The [CLOSES:] gap remains FAIL across all R9
variations (no passing example produced) and is re-flagged as candidate for C-30 in a future round.

---

### v7 → v8

Two new aspirational criteria extracted from the R8 scorecard excellence signals (V-05 axis
confirmed absent from V-03/V-04):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-26 | **FM-SKILL Naming for Self-Defense Mechanisms** | V-05 strength on CONTEXT causal motivation: V-05 names FM-SKILL-7 "Self-Assessment Loop Staleness" in CONTEXT before Phase 1 and adds a corresponding FAILURE MODE MAP row — V-03/V-04 achieve 18/18 structurally (pre-printed cells and runtime phrase respectively) but neither names the failure mode causing the staleness nor maps it to a structural defense; without a numbered FM-SKILL in CONTEXT, the structural rules are unexplained obligations rather than causally-grounded mechanisms; when criteria defend the self-assessment structure itself (loop range currency, SHALL-L mandate extension), a named FM-SKILL entry is required and the FAILURE MODE MAP must maintain 1:1 coverage of all numbered FM-SKILLs |
| C-27 | **Phase-level Structural Purpose Annotation Completeness** | V-05 strength on defense chain completeness: V-05 adds FM-SKILL-7 to Phase 8's structural purpose blockquote — V-03/V-04 enforce the mechanism at the structural level without annotating why at the phase level; a complete defense chain requires CONTEXT motivation → FAILURE MODE MAP mapping → phase-level enforcement annotation at the point of application; any phase that enforces a new FM-SKILL must name it in that phase's structural purpose blockquote |

**Scoring impact:** N grows from 18 to 20. A v7-golden output (18/18 aspirational pass) now scores
18/20 × 10 = **9.000 pts** on the aspirational tier. Full 10 pts requires all 20 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-26 auto-fails if no structural self-defense criteria exist to name (requires C-24 or C-25 as the mechanism being motivated).
- C-27 auto-fails if C-26 fails (phase annotation cannot reference an FM-SKILL that was never declared in CONTEXT).

**C-17 pass condition updated:** integer must equal 20 and row range must be declared as C-08..C-27.
A v7-golden output with integer=18 now fails C-17 under v8.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-27 (20 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27) must include a
Self-Assessment cell. A v7-golden output whose loop ends at C-25 (18 rows) fails C-21 under v8.

**C-24 pass condition updated:** literal range string `C-08..C-27` must appear in the C-21
mechanism phrase text. Stale strings (`C-08..C-25`, `C-08..C-23`, `C-08..C-21`) fail even when all
rows are structurally present.

**C-25 pass condition updated:** SHALL-L must explicitly name C-22, C-23, C-24, C-25, C-26, C-27.
Cells that contain mechanism phrases by inheritance without a SHALL-L naming mandate fail.

**Slot displacement note:**
v7 flagged the [CLOSES:] annotation gap as "candidate for C-26." The C-26 slot is occupied by
the FM-SKILL naming signal extracted from R8. The [CLOSES:] gap remains FAIL across all R8
variations (no passing example produced) and is re-flagged as candidate for C-28 in a future round.

---

### v6 → v7

Two new aspirational criteria extracted from the R7 scorecard excellence signals (V-03 axis
confirmed absent from V-04):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-24 | **C-21 Loop Range Phrase Currency** | V-03 strength on C-21 evidence quality: V-03 updates the range string in the C-21 self-referential loop mechanism phrase from `C-08..C-21` to `C-08..C-23`; V-01, V-02, and V-04 pass C-21 structurally (all rows present, Self-Assessment cells present) but retain the stale phrase — the binary pass result is the same under v6 but the explicit range string does not reflect the current N; V-04 description explicitly calls out "C-21 mechanism phrase update not included (V-03 axis absent)," confirming this is a distinct enforcement axis; any output that introduces new criteria must update the range phrase to name the new terminal row |
| C-25 | **SHALL-L Mandate Extension for New Criteria** | V-03 strength on SHALL-L scope: V-03 extends SHALL-L to formally mandate observable mechanism phrases in C-22 and C-23 Self-Assessment cells; V-01, V-02, and V-04 contain mechanism phrases in those cells (via inheritance or structural compliance) but SHALL-L does not explicitly name C-22/C-23 as covered — without the SHALL-L mandate, mechanism phrase presence in new-criterion cells is structural coincidence, not enforced obligation; V-04 lacks this axis despite combining V-01 and V-02 |

**Scoring impact:** N grows from 16 to 18. A v6-golden output (16/16 aspirational pass) now scores
16/18 × 10 = **8.89 pts** on the aspirational tier. Full 10 pts requires all 18 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-24 auto-fails if C-21 fails (requires the self-referential loop mechanism to exist).
- C-25 auto-fails if C-19 fails (requires the SHALL-L mechanism to exist).

**C-17 pass condition updated:** integer must equal 18 and row range must be declared as C-08..C-25.
A v6-golden output with integer=16 now fails C-17 under v7.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-25 (18 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25) must include a Self-Assessment cell.
A v6-golden output whose loop ends at C-23 (16 rows) fails C-21 under v7.

**C-24 pass condition note:** Pass requires the literal range string `C-08..C-25` to appear in the
C-21 mechanism phrase text. Structural loop coverage alone does not satisfy C-24. Stale strings
(`C-08..C-21`, `C-08..C-23`) fail even when all rows are structurally present.

**C-25 pass condition note:** Pass requires SHALL-L to explicitly name the new criteria by ID
(minimum: C-22, C-23, C-24, C-25 under v7). Cells that contain mechanism phrases by inheritance
without a SHALL-L naming mandate fail. C-25 auto-fails if C-19 fails.
```

---

Key structural decisions in the v8 → v9 section:

**C-28** mirrors C-26 exactly one level up — C-26 named the FM-SKILL for the *self-defense* mechanism; C-28 names the FM-SKILL for the *meta-criterion defense* mechanism. The recursion is the point: every defense layer is itself subject to the staleness it defends against.

**C-29** mirrors C-27 — the phase-level annotation requirement follows the FM-SKILL naming requirement one-for-one, as it has in every round.

**Updated pass conditions** follow the same mechanical pattern established in v7 and v8:
- C-17 integer and range string advance by 2
- C-21 loop terminal row advances by 2
- C-24 literal string advances to `C-08..C-29`
- C-25 SHALL-L mandate extends to include C-28/C-29
- C-26 FAILURE MODE MAP 1:1 coverage now requires FM-SKILL-8 row

**Slot displacement** preserves the chain: [CLOSES:] gap moves from candidate C-28 → candidate C-30.
