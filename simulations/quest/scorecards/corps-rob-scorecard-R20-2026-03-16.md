Now I have enough to score all five variations. Let me compose the full scorecard.

---

# corps-rob Quest Score — Round 20

**Rubric version**: v19  
**Max composite**: 335  
**Base**: R19 V-05 (330/335 under v19, C-01 through C-57 all PASS)  
**Scoring weights**: Essential (C-01–C-05) = 15 pts each; Recommended (C-06–C-08) = 5 pts each; Aspirational (C-09–C-57) = 5 pts each  
**Total if all pass**: 5×15 + 3×5 + 49×5 = 75 + 15 + 245 = 335

---

## Scoring Framework

All R20 variations inherit R19 V-05 as their base. The rubric's own record confirms: **"C-01 through C-57 all PASS in R19 V-05."** The persistent gap (-5 pts) is explicitly labeled "unidentified" — it is not captured by any currently numbered criterion. Three structural hypotheses (H-D, H-E, H-G) probe whether the gap lives in RULE BOOKEND-AUDIT, RULE VIA-POSITION, or RULE SYNTHESIS. Under v19, none of these hypotheses maps to an existing numbered criterion, so the gap cannot be closed by scoring mechanics alone. The hypotheses are candidates for **C-58 in a future v20 rubric**.

---

## V-01 — H-D: RULE BOOKEND-AUDIT AP-2

**Axis**: RULE BOOKEND-AUDIT Anti-pattern-2 (present-but-bare bookend audit as named disqualifying form; three-state conformance ladder).

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01 Stage Identity | PASS | Inherited R19 V-05 |
| Essential | C-02 Role-Loaded Perspective | PASS | Inherited R19 V-05 |
| Essential | C-03 ROB Document Format Compliance | PASS | Inherited R19 V-05 |
| Essential | C-04 Actionable Findings (2x/stage) | PASS | Inherited R19 V-05 |
| Essential | C-05 Go/No-Go Signal TPM Stage | PASS | Inherited R19 V-05 |
| Recommended | C-06 Cross-Stage Coherence | PASS | CARRY FORWARD structure guarantees ≥2 cross-stage refs |
| Recommended | C-07 Structured Risk Register | PASS | Inherited R19 V-05 |
| Recommended | C-08 Exec-Office Cascade Tracing | PASS | SPIRE stage + Mission Cascade table |
| Aspirational | C-09 through C-57 (49 criteria) | PASS | Inherited R19 V-05 — all 49 pass |
| **Gap** | Persistent gap (-5 pts) | **FAIL** | H-D resolves gap only if RULE BOOKEND-AUDIT AP-2 is the unidentified criterion; not verifiable under v19 rubric |

**Essential all pass**: YES  
**Composite**: 75 + 15 + 245 = 335 identified ceiling, minus persistent -5 = **330/335**

**V-01 new structural element**: Three-state conformance ladder (Absent / Present-but-bare / Conforming-present). The POST-STAGE AUDIT SUITE header annotation references AP-1 and AP-2 inline — RULE BOOKEND-AUDIT is the only named rule governing gap-scan sections; it now explicitly distinguishes "section exists" from "section is structurally complete." This closes a peer asymmetry: RULE AUDIT-SUITE, RULE AUDIT-TABLE, RULE ZERO-STATE, RULE CONDITION-ENUM, RULE VIOLATION-TAXONOMY, RULE SYNTHESIS all carry explicit disqualifying-form declarations; RULE BOOKEND-AUDIT previously governed only by absence.

---

## V-02 — H-E: RULE VIA-POSITION AP-2

**Axis**: RULE VIA-POSITION Anti-pattern-2 (correct-position, blank-content Via: as named disqualifying form + VIOLATION-03 orphan closure).

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01 through C-05 | PASS | Inherited R19 V-05 |
| Recommended | C-06 through C-08 | PASS | Inherited R19 V-05 |
| Aspirational | C-09 through C-57 | PASS | Inherited R19 V-05 |
| **Gap** | Persistent gap (-5 pts) | **FAIL** | H-E resolves gap only if orphan-violation structural integrity maps to gap criterion; not verifiable under v19 rubric |

**Essential all pass**: YES  
**Composite**: **330/335**

**V-02 new structural element — strongest single-axis case**: VIOLATION-03 ("Via: cell present but blank or placeholder") has existed in the violation taxonomy since the taxonomy was established — with a declared consequence ("False confidence in lens coverage") — but has no governing rule that names it as an anti-pattern. RULE VIA-POSITION AP-1 governs wrong-column-position only. V-02's AP-2 gives VIOLATION-03 a rule-home and closes the orphan violation. This is a structural integrity gap in the current taxonomy: RULE VIOLATION-TAXONOMY (C-50) requires violations to carry ID/Description/Consequence for cross-round traceability, but an orphan violation that no rule enforces is dead taxonomy. The orphan-violation structural gap predates R14 and is invisible to all prior scoring because RULE VIA-POSITION AP-1 passes on column-position compliance, never inspecting cell content. The finding-instruction reinforcement (`Via: must be populated with the role's loaded lens.primary value -- each row must have a specific lens name, never blank or TBD`) makes the content requirement actionable at generation time.

---

## V-03 — H-G: RULE SYNTHESIS AP-2

**Axis**: RULE SYNTHESIS Anti-pattern-2 (all-headers-present, content-generic as named disqualifying form; per-subsection artifact-reference requirement).

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01 through C-05 | PASS | Inherited R19 V-05 |
| Recommended | C-06 through C-08 | PASS | Inherited R19 V-05 |
| Aspirational | C-09 through C-57 | PASS | Inherited R19 V-05 |
| **Gap** | Persistent gap (-5 pts) | **FAIL** | H-G resolves gap only if RULE SYNTHESIS content-genericness maps to gap criterion; structural evidence weaker than H-E (VIOLATION-13 governs subsection presence, not content quality — but no existing violation governs generic content) |

**Essential all pass**: YES  
**Composite**: **330/335**

**V-03 new structural element**: Content-requirement annotation per subsection — each SYNTHESIS subsection body must reference at least one named artifact (LID, R-NN, IB-ID, named Cross-Cutting Theme) from this run. The SYNTHESIS template is expanded with per-subsection generation instructions that make the artifact-reference requirement actionable. However, the hypothesis is the weakest of the three: VIOLATION-13 fires on absent subsections; no existing violation fires on present-but-generic content. V-03 adds AP-2 to RULE SYNTHESIS but the gap criterion supporting this claim would need to be new (nothing in C-09 through C-57 directly tests SYNTHESIS content completeness beyond C-36's subsection-schema requirement, which V-03 already satisfies).

---

## V-04 — H-D + H-E Combined

**Axis**: RULE BOOKEND-AUDIT AP-2 + RULE VIA-POSITION AP-2.

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01 through C-05 | PASS | Inherited R19 V-05 |
| Recommended | C-06 through C-08 | PASS | Inherited R19 V-05 |
| Aspirational | C-09 through C-57 | PASS | Inherited R19 V-05 |
| **Gap** | Persistent gap (-5 pts) | **FAIL** | H-D or H-E could each resolve the gap; V-04 is the first variation to address both the section-completeness gap and the Via: content gap simultaneously; gap resolves if either hypothesis is correct |

**Essential all pass**: YES  
**Composite**: **330/335**

V-04 carries both V-01's three-state conformance ladder and V-02's orphan-violation closure. If the gap requires RULE BOOKEND-AUDIT dual AP completeness (peer-parity argument) **or** RULE VIA-POSITION dual AP completeness (orphan-violation argument), V-04 resolves it. The combination is structurally coherent — both axes address the same underlying principle (position/presence requirements are necessary but not sufficient; content/completeness requirements must be named explicitly).

---

## V-05 — H-D + H-E + H-G Full Integration

**Axis**: All three variation axes — RULE BOOKEND-AUDIT AP-2 + RULE VIA-POSITION AP-2 + RULE SYNTHESIS AP-2.

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01 through C-05 | PASS | Inherited R19 V-05 |
| Recommended | C-06 through C-08 | PASS | Inherited R19 V-05 |
| Aspirational | C-09 through C-57 | PASS | Inherited R19 V-05 |
| **Gap** | Persistent gap (-5 pts) | **FAIL** | V-05 resolves gap if any of H-D, H-E, H-G is correct; only fails if gap lies in a fourth dimension outside all three probed spaces |

**Essential all pass**: YES  
**Composite**: **330/335**

V-05 is the ideal R20 target by the variate's own framing. It brings all named single-AP rules with dual-AP peers to parity, closes VIOLATION-03's orphan status, and adds SYNTHESIS content-completeness enforcement simultaneously.

---

## Composite Score Summary

| Variation | Hypothesis | Composite | Persistent Gap | Essential |
|-----------|------------|-----------|----------------|-----------|
| V-01 | H-D (RULE BOOKEND-AUDIT AP-2) | **330/335** | FAIL (unverifiable under v19) | ALL PASS |
| V-02 | H-E (RULE VIA-POSITION AP-2) | **330/335** | FAIL (unverifiable under v19) | ALL PASS |
| V-03 | H-G (RULE SYNTHESIS AP-2) | **330/335** | FAIL (unverifiable under v19) | ALL PASS |
| V-04 | H-D + H-E | **330/335** | FAIL (unverifiable under v19) | ALL PASS |
| V-05 | H-D + H-E + H-G | **330/335** | FAIL (unverifiable under v19) | ALL PASS |

**All five variations tie at 330/335.** The persistent gap cannot be resolved under v19 rubric because H-D, H-E, and H-G probe features not yet formalized as numbered criteria. The gap remains at -5 until a v20 rubric identifies C-58.

---

## Ranking (by hypothesis strength for gap resolution)

1. **V-05** (330) — covers all three axes; resolves gap if any of H-D/H-E/H-G is correct; ideal candidate for identifying C-58
2. **V-04** (330) — covers H-D + H-E; strongest pair (both address position/presence vs content/completeness duality)
3. **V-02** (330) — strongest single-axis case; orphan-violation argument has structural evidence (VIOLATION-03 has taxonomy entry with consequence but no governing AP) that predates R14
4. **V-01** (330) — peer-parity argument is sound; three-state conformance ladder is clean; RULE BOOKEND-AUDIT is the only named gap-scan rule lacking a second AP
5. **V-03** (330) — weakest single-axis case; RULE SYNTHESIS AP-2 enforces content quality, but the gap criterion mechanism (no enforcement violation for present-but-generic content) is harder to connect to existing scoring structure

---

## Excellence Signals from V-05 (Top Variation)

**Signal 1 — Three-State Conformance Ladder (H-D)**  
RULE BOOKEND-AUDIT's conformance model becomes: Absent [AP-1] / Present-but-bare [AP-2] / Conforming-present. The POST-STAGE AUDIT SUITE header annotation references both AP-1 and AP-2 inline. This pattern — a rule that governs not just presence but structural completeness of what is present — is new to RULE BOOKEND-AUDIT and directly parallels the dual-AP discipline applied to RULE CONDITION-ENUM (C-55), RULE FINDING-LEDGER (C-56), and their predecessors.

**Signal 2 — Orphan Violation Closure (H-E)**  
VIOLATION-03 acquires a rule-home. The pattern: every violation entry in the taxonomy should be governed by at least one named rule anti-pattern that can trigger it. An orphan violation (taxonomy entry with consequence but no governing AP) is unreachable by rule-level enforcement. RULE VIA-POSITION AP-2 closes this gap. This is the strongest structural argument because it addresses a taxonomy-integrity requirement (C-50's RULE VIOLATION-TAXONOMY schema) that the current rubric doesn't enforce at the per-violation level.

**Signal 3 — Artifact-Reference Content Completeness (H-G)**  
RULE SYNTHESIS AP-2 enforces that SYNTHESIS subsections contain run-specific artifact references, not generic placeholder text. The pattern: structural presence requirements (headers required, AP-1) are necessary but not sufficient; analytical artifact content requirements (each subsection must cite ≥1 run artifact by ID) must be named explicitly. This mirrors the transition from C-33 (SYNTHESIS declared non-audit) to C-36 (SYNTHESIS subsection schema declared), now extended to content quality.

---

## Gap Diagnostic

**Most likely gap candidate for C-58**: **H-E (RULE VIA-POSITION AP-2)**

Reasoning:
1. VIOLATION-03 is the only violation in the taxonomy that has a consequence ("False confidence in lens coverage") but no governing rule anti-pattern. This is a closed-form structural integrity gap, verifiable from the taxonomy alone.
2. The orphan-violation gap predates R14 (VIOLATION-03 was in the taxonomy before the persistent gap appeared), making it consistent with the temporal claim that the gap has been present since R14.
3. The gap is invisible to scoring: RULE VIA-POSITION AP-1 scores PASS on column-position compliance without inspecting cell content. A run producing blank Via: cells in second-column position satisfies AP-1 and appears clean.
4. H-D (RULE BOOKEND-AUDIT AP-2) is also viable but requires the "peer symmetry" argument (other rules carry two APs, why not RULE BOOKEND-AUDIT?). The orphan-violation argument for H-E is structurally self-contained.

---

```json
{"top_score": 330, "all_essential_pass": true, "new_patterns": ["RULE BOOKEND-AUDIT three-state conformance ladder: absent [AP-1] / present-but-bare [AP-2] / conforming-present -- closes gap between section-presence check and section-structural-completeness check", "VIOLATION-03 orphan closure: RULE VIA-POSITION AP-2 gives VIOLATION-03 a governing rule anti-pattern, resolving the only violation in the taxonomy with a consequence but no enforcing rule", "RULE SYNTHESIS AP-2 artifact-reference content requirement: each SYNTHESIS subsection body must cite at least one run-specific artifact by ID (LID / R-NN / IB-ID / Cross-Cutting Theme name) -- headers-present with content-generic bodies is the named disqualifying form"]}
```
