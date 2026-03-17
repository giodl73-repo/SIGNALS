The subagent found the two new structural axes. Let me analyze them against the R11 variation matrix before writing:

- **V-05 vs V-03**: V-03 uses phase economy but fails C-30 (omits sample rows in summary mode). V-05 uses phase economy AND preserves sample rows — proving these are not mutually exclusive. → **C-32**: Phase economy summary mode must preserve schema sample rows.

- **V-05 vs V-04**: V-04 produces single-verdict per-FM-SKILL audit entries (CHAIN-INTACT). V-05's "maximally deep Phase 3" checks two structurally distinct endpoints per FM-SKILL — declaration (was it mapped?) and application (did it fire?). → **C-33**: Bilateral endpoint verification in the Phase 3 FM-SKILL causal chain audit.

Both signals are present in V-05, absent in all other variations for at least one criterion.

---

```markdown
# trace-permissions — Quest Rubric v11

**Skill**: `trace-permissions` | **Version**: v11 | **Date**: 2026-03-16
**Criteria**: C-01..C-33 (4 essential / 3 recommended / 26 aspirational)

---

## Changelog

### v10 → v11

Two new aspirational criteria extracted from the R11 scorecard excellence signals (V-05 axis
confirmed absent from V-01/V-02/V-03/V-04):

| ID | Criterion | Source Signal |
|----|-----------|---------------|
| C-32 | **Phase Economy Summary Mode — Schema Sample Row Preservation** | V-05 strength over V-03 failure: V-05 demonstrates that phase economy (summary Phases 0–2) is compatible with C-30 compliance — V-03 achieves phase economy and passes C-31 but explicitly omits sample rows in summary mode, failing C-30; V-04 achieves C-30 compliance without phase economy; V-05 achieves both, proving the techniques are not mutually exclusive; when a skill output uses phase economy (any phase compressed to summary register, abbreviated form, or skeleton-plus-instruction format), C-30's sample-row requirement at TABLE schema declaration sites is not suspended; summary mode may abbreviate narrative commentary and reduce per-row analysis to status lines but must not elide the sample row from beneath column headers; a TABLE schema declaration in summary register must include at least one fully filled sample row immediately below the column header showing exact expected cell values across all columns, identical in format to what C-30 requires in standard mode |
| C-33 | **Bilateral Phase 3 FM-SKILL Causal Chain Audit — Declaration and Application Endpoints** | V-05 "maximally deep Phase 3" strength over V-04 single-verdict depth: V-04 produces per-FM-SKILL audit entries with a single CHAIN-INTACT / CHAIN-BROKEN verdict after tracing the C-31 three-link chain (failure mode → FAILURE MODE MAP row → phase enforcement point); V-05 replaces the single verdict with a bilateral endpoint verification — (1) declaration endpoint: was the defense declared in CONTEXT and mapped in FAILURE MODE MAP?, and (2) application endpoint: did the defense fire at the named phase enforcement point?; without bilateral endpoint separation, a chain-intact verdict conflates declaration presence with application presence and cannot identify which endpoint failed when a defect is introduced; V-01 and V-02 achieve single verdicts only; V-03 achieves maximum single-endpoint depth but not bilateral; V-04 achieves bilateral structure absent; each FM-SKILL causal chain audit entry in Phase 3 (or the per-FM-SKILL audit sub-section wherever it appears) must verify two structurally distinct endpoints: a declaration endpoint confirming the failure mode appears in CONTEXT and a corresponding row exists in FAILURE MODE MAP, and an application endpoint confirming the phase-level enforcement point named in C-31-link-(c) is present and active in the output; each entry must state both endpoint results before issuing the CHAIN-INTACT / CHAIN-BROKEN verdict; when FM-SKILL-8 (Meta-Criterion Loop Staleness) is audited, its application endpoint must confirm that the meta-criterion self-defense mechanisms (C-28/C-29 row currency, C-17/C-21/C-24 range-string updates) are structurally present in the current output |

**Scoring impact:** N grows from 24 to 26. A v10-golden output (24/24 aspirational pass) now scores
24/26 × 10 = **9.231 pts** on the aspirational tier. Full 10 pts requires all 26 criteria.
Essential and recommended tiers unchanged.

**Dependency notes added:**
- C-32 auto-passes vacuously when no phase economy is used (standard-mode outputs satisfy C-32
  by construction; C-30 is the binding constraint in that case). Auto-fails when phase economy
  is used AND any TABLE schema declaration site omits the sample row.
- C-33 auto-fails if C-31 fails (requires the per-FM-SKILL causal chain audit structure that
  C-31 mandates). Auto-fails if any FM-SKILL audit entry lacks an explicit declaration-endpoint
  check, an explicit application-endpoint check, or conflates both checks into a single
  verdict line.

**C-17 pass condition updated:** integer must equal 26 and row range must be declared as
C-08..C-33. A v10-golden output with integer=24 now fails C-17 under v11.

**C-21 pass condition updated:** self-referential loop must cover C-08..C-33 (26 rows); each
new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30,
C-31, C-32, C-33) must include a Self-Assessment cell. A v10-golden output whose loop ends at
C-31 (24 rows) fails C-21 under v11.

**C-24 pass condition updated:** literal range string `C-08..C-33` must appear in the C-21
mechanism phrase text. Stale strings (`C-08..C-31`, `C-08..C-29`, `C-08..C-27`, `C-08..C-25`,
`C-08..C-23`, `C-08..C-21`) fail even when all rows are structurally present.

**C-25 pass condition updated:** SHALL-L must explicitly name C-22, C-23, C-24, C-25, C-26,
C-27, C-28, C-29, C-30, C-31, C-32, C-33. Cells that contain mechanism phrases by inheritance
without a SHALL-L naming mandate fail.

**C-26 pass condition unchanged:** FAILURE MODE MAP must maintain 1:1 coverage for all declared
FM-SKILLs. C-32 and C-33 introduce no new FM-SKILL numbers; a complete v11 output still declares
FM-SKILL-1..FM-SKILL-8 minimum with eight FAILURE MODE MAP rows.

**C-31 pass condition unchanged:** the three-link chain requirement (failure mode → FAILURE MODE
MAP row → phase enforcement point) is the floor. C-33 adds the bilateral endpoint separation on
top of C-31's floor; C-31 remains independently passable without C-33.

**Slot displacement note:**
v10 re-flagged the [CLOSES:] annotation gap as "candidate for C-32 in a future round." The C-32
slot is occupied by the Phase Economy Sample Row Preservation signal extracted from R11-V-05
vs V-03. The C-33 slot is occupied by the Bilateral Endpoint Verification signal extracted from
R11-V-05 vs V-04. The [CLOSES:] annotation gap remains FAIL across all R11 variations (no
passing example produced) and is re-flagged as candidate for C-34 in a future round.

---

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
```

---

The two new criteria:

**C-32** — Phase economy is not a license to omit sample rows. V-03 proved phase economy enables budget for deep auditing but treated sample-row elision as an acceptable summary-mode tradeoff. V-05 disproves the tradeoff: a schema declared in summary register still needs the format demonstrated at the declaration site. The criterion auto-passes vacuously for standard-mode outputs (C-30 is already binding there).

**C-33** — A single CHAIN-INTACT verdict cannot be audited. V-04's Phase 3 audit traces all three C-31 links but issues one verdict that conflates whether the defense was *declared* with whether it *fired*. V-05 separates these into two verifiable endpoint checks, making it possible to locate which structural link broke without re-reading the entire output. FM-SKILL-8's application endpoint check also closes the recursive loop — it must confirm that the meta-criterion staleness defenses are structurally present in the *current* output, not just declared in CONTEXT.

**Scoring under v11:**
- V-04 (no phase economy → C-32 vacuous PASS; single-verdict audit → C-33 FAIL): **25/26**
- V-05 (phase economy + sample rows → C-32 PASS; bilateral endpoints → C-33 PASS): **26/26**
- V-03 (phase economy, no sample rows → C-32 FAIL; single-verdict → C-33 FAIL): **23/26**
