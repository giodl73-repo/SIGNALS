Reading the scorecard carefully to identify the two strongest new structural axes before writing the updated rubric.

**R10 excellence signals extracted:**

- **V-02**: Sample-row pre-print at schema declaration sites — FM-SKILL-1 defense gains a second layer (format demonstrated at declaration, not just rule-enforced at runtime). V-01/V-03/V-04 pass C-08..C-29 structurally via Gap? flag alone; none pre-print format examples at schema declaration.

- **V-03**: Phase economy pattern — Phases 0–3 summary mode releases budget for Phase 4 per-FM-SKILL causal chain audit sub-section, making the defense chain auditable rather than merely asserted. V-01/V-02/V-04 deliver only PASS cells in Phase 4; none include a per-FM-SKILL causal chain trace.

These pair as C-30 and C-31 — complementary improvements to the declaration layer (before execution) and the auditability layer (after execution). No new FM-SKILL numbers are required; both criteria strengthen existing structural obligations.

---

```markdown
# trace-permissions — Quest Rubric v10

**Skill**: `trace-permissions` | **Version**: v10 | **Date**: 2026-03-16
**Criteria**: C-01..C-31 (4 essential / 3 recommended / 24 aspirational)

---

## Changelog

### v9 → v10

Two new aspirational criteria extracted from the R10 scorecard excellence signals (V-02 and V-03
axes confirmed absent from V-01/V-04):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-30 | **Sample-Row Pre-Print at Schema Declaration Sites** | V-02 strength on two-layer FM-SKILL-1 defense: V-02 includes a fully filled sample row immediately below the column header at each TABLE_1–5 declaration site, demonstrating exact expected cell values (Granted/Denied/Conditional with inline conditions/N/A) before Phase 1 begins — V-01/V-03/V-04 achieve FM-SKILL-1 defense structurally via the boolean Gap? per-row commit flag but none pre-print format examples at the declaration site itself; without a sample row at declaration, blank-cell prevention relies on rule memory rather than local format demonstration, and an implementer must consult a separate section to know whether "Conditional" requires an inline reason clause; the Schema Registry must function simultaneously as schema declaration and value demonstration; each TABLE schema declared in Phase 0 must include at least one fully filled sample row immediately below the column header showing exact expected cell values across all columns |
| C-31 | **Phase 4 Per-FM-SKILL Causal Chain Audit Sub-Section** | V-03 strength on defense chain auditability: V-03's Phase 4 budget expansion enables a per-FM-SKILL causal chain audit sub-section that traces the path from failure mode identification in CONTEXT through FAILURE MODE MAP mapping to phase-level enforcement point, confirming each link in the defense chain — V-01/V-02/V-04 achieve 22/22 structurally with PASS cells in all Self-Assessment rows but Phase 4 delivers cell values without per-FM-SKILL causal chain commentary; without an explicit causal chain trace in Phase 4, defense completeness is asserted but not independently verifiable; a passing output must include, for each declared FM-SKILL-N, a Phase 4 audit entry naming (a) the failure mode as defined in CONTEXT, (b) the corresponding FAILURE MODE MAP row that maps it to a structural defense, and (c) the phase-level enforcement point where the defense fires; the audit confirms that every link in the CONTEXT → FAILURE MODE MAP → phase annotation chain is structurally present and traceable |

**Scoring impact:** N grows from 22 to 24. A v9-golden output (22/22 aspirational pass) now scores
22/24 × 10 = **9.167 pts** on the aspirational tier. Full 10 pts requires all 24 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-30 auto-fails if no TABLE schema declarations exist in Phase 0 (requires a schema declaration
  structure to attach sample rows to; a skill that produces no tabular output has no obligation).
- C-31 auto-fails if Phase 4 is absent or contains no Self-Assessment rows (requires the
  self-assessment phase structure that C-21 mandates; if C-21 fails, C-31 also fails).

**C-17 pass condition updated:** integer must equal 24 and row range must be declared as
C-08..C-31. A v9-golden output with integer=22 now fails C-17 under v10.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-31 (24 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31)
must include a Self-Assessment cell. A v9-golden output whose loop ends at C-29 (22 rows) fails
C-21 under v10.

**C-24 pass condition updated:** literal range string `C-08..C-31` must appear in the C-21
mechanism phrase text. Stale strings (`C-08..C-29`, `C-08..C-27`, `C-08..C-25`, `C-08..C-23`,
`C-08..C-21`) fail even when all rows are structurally present.

**C-25 pass condition updated:** SHALL-L must explicitly name C-22, C-23, C-24, C-25, C-26, C-27,
C-28, C-29, C-30, C-31. Cells that contain mechanism phrases by inheritance without a SHALL-L
naming mandate fail.

**C-26 pass condition unchanged:** FAILURE MODE MAP must maintain 1:1 coverage for all declared
FM-SKILLs. C-30 and C-31 introduce no new FM-SKILL numbers; a complete v10 output still declares
FM-SKILL-1..FM-SKILL-8 minimum with eight FAILURE MODE MAP rows.

**Slot displacement note:**
v9 re-flagged the [CLOSES:] annotation gap as "candidate for C-30." The C-30 slot is occupied by
the Sample-Row Pre-Print signal extracted from R10-V-02. The C-31 slot is occupied by the Phase 4
Causal Chain Audit signal extracted from R10-V-03. The [CLOSES:] gap remains FAIL across all R10
variations (no passing example produced) and is re-flagged as candidate for C-32 in a future round.

---

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
- C-28 auto-fails if C-26 and C-27 both fail (requires meta-criterion defense mechanisms to exist
  as the mechanisms being motivated).
- C-29 auto-fails if C-28 fails (phase annotation cannot reference an FM-SKILL that was never
  declared in CONTEXT).

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
- C-26 auto-fails if no structural self-defense criteria exist to name (requires C-24 or C-25 as
  the mechanism being motivated).
- C-27 auto-fails if C-26 fails (phase annotation cannot reference an FM-SKILL that was never
  declared in CONTEXT).

**C-17 pass condition updated:** integer must equal 20 and row range must be declared as C-08..C-27.
A v7-golden output with integer=18 now fails C-17 under v8.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-27 (20 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27) must include a
Self-Assessment cell. A v7-golden output whose loop ends at C-25 (18 rows) fails C-21 under v8.
```

---

**Summary of v9 → v10 changes:**

| | v9 | v10 |
|---|---|---|
| Aspirational N | 22 | 24 |
| v9-golden score | 22/22 × 10 = 10.000 | 22/24 × 10 = 9.167 |
| C-17 range | C-08..C-29 | C-08..C-31 |
| C-21 rows | 22 | 24 |
| C-24 literal | `C-08..C-29 (22 rows)` | `C-08..C-31 (24 rows)` |
| C-25 SHALL-L tail | ..C-29 | ..C-31 |
| [CLOSES:] candidate | C-30 | C-32 |

No new FM-SKILL numbers are added. C-26 FAILURE MODE MAP coverage (FM-SKILL-1..FM-SKILL-8) is unchanged.
