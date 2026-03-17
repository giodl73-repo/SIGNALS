Scorecard written to `simulations/quest/scorecards/narrate-behavior-scorecard-R3-2026-03-17.md`.

---

## R3 Results — narrate-behavior

**All 5 variations: 100/100. All Golden.**

| Rank | Variation | Score | Aspirational | Notes |
|------|-----------|-------|-------------|-------|
| 1 | V-15 | 100 | 7/7 | Boundary registry + inertia cross-reference |
| 2 | V-14 | 100 | 7/7 | Contract-first + inertia framing (cleanest combo) |
| 3 | V-11 | 100 | 6/7 | Boundary-name propagation; C-14 N/A |
| 4 | V-12 | 100 | 6/7 | Inertia framing; C-13 FAIL |
| 5 | V-13 | 100 | 6/7 | Severity-blast ablation; C-14 N/A |

---

**Axis questions resolved:**

| Question | Answer |
|---------|--------|
| C-01: BOUNDARY REGISTRY as non-sub-skill step in declared sequence? | **PASS** — simulation sections appear in declared order; compilation steps are neutral |
| C-08: "never merge" instruction load-bearing? | **NO** — separate pre-committed columns enforce independence; prose is confirmed overhead |
| C-14: NONE on 4th EXIT GATE field satisfies gate? | **YES** — valid clean-section declaration, not a bypass |
| C-13: V-12 canonical order sufficient? | **NO** — flow sections upstream establish no named boundaries; C-13 requires named references from downstream to upstream contract boundaries |

**3 new patterns for R4:**
1. `boundary-registry-as-artifact` — BOUNDARY REGISTRY with B-IDs converts C-13 from style to structural; EXIT GATE "B-IDs referenced" makes coverage auditable
2. `inertia-boundary-crossref` — INERTIA blocks referencing named upstream boundaries satisfy C-13 + C-14 in a single finding row
3. `severity-blast-column-independence` — "never merge" prose is dead weight when columns enforce separation

**R4 candidate axes:** (1) registry compression — fold BOUNDARY REGISTRY into S1/S2 EXIT GATEs; (2) full-span inertia — extend INERTIA to S1-S2; (3) EXIT GATE field compression — 5-field condensed format

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["boundary-registry-as-artifact: BOUNDARY REGISTRY compiled between S2 and S3 with B-IDs converts C-13 cross-references from style to structural constraint; EXIT GATE 'BOUNDARY REGISTRY entries referenced' makes downstream citation auditable per section", "inertia-boundary-crossref: INERTIA blocks in downstream sections that open by identifying which named upstream boundary the status-quo assumes satisfies C-13 and C-14 simultaneously in a single finding row; B-ID format in V-15 makes this maximally mechanical", "severity-blast-column-independence: confirmed that 'independent of blast radius; never merge' prose is not load-bearing when Severity and Blast Radius are separate pre-committed columns; can be dropped as token overhead"]}
```
| PASS | Declared: `S1 trace-contract -> S2 trace-permissions -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT`. Explicit, followed. |
| V-14 | PASS | Identical sequence to V-13; declared and followed. |
| V-15 | PASS | Declared: `S1 -> S2 -> BOUNDARY REGISTRY -> S3 -> S4 -> S5 -> REPORT`. Same as V-11; BOUNDARY REGISTRY neutral for C-01. |

**C-01 open question resolved**: BOUNDARY REGISTRY in declared sequence (V-11, V-15) — PASS. C-01 requires simulation sections follow declared order. They do. Compilation steps between simulation sections are neutral.

---

### C-02 — Output Is a Single Unified Report

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | "Do not produce five separate outputs. Produce one unified simulation findings report." REPORT section carries title/date block. |

---

### C-03 — Findings Ranked by Blast Radius

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | All REPORT sections: "Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last). Label at top: 'Sorted by blast radius -- WIDE to NARROW.'" REQUIRE blocks confirm sort. |

---

### C-04 — At Least One Spec Gap or Contract Violation

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | Finding Type column in pre-committed table; REQUIRE: "1+ finding typed spec-gap or contract-violation with a specific spec location." V-12/V-14/V-15 additionally enforce via inertia conversion rule that structurally produces spec-gap findings. |

---

### C-05 — Finding Schema: Source + Location + Impact

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | All pre-committed tables: Sub-Skill (source), Spec/Contract Location, Impact as separate named columns. |

---

### C-06 — Cross-Sub-Skill Coverage

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | All REQUIRE blocks: "3+ distinct sub-skills represented in findings." |

---

### C-07 — Remediation Guidance Present

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | Remediation as a separate pre-committed column; "concrete action (spec update, contract clarification, or code change)." |

---

### C-08 — Severity Classification Applied

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-11 | PASS | Severity HIGH/MED/LOW with "independent of blast radius; never merge"; separate column. |
| V-12 | PASS | Identical; separate column. |
| V-13 | PASS | Severity HIGH/MED/LOW — "never merge / independent" instruction REMOVED. Scale defined; separate column enforces field independence structurally. |
| V-14 | PASS | "independent of blast radius; never merge" present; separate column. |
| V-15 | PASS | Same as V-14. |

**C-08 ablation resolved**: Removing "never merge" does NOT fail C-08. Scale is defined; separate columns enforce independence. "Never merge" prose is confirmed token overhead.

---

### C-09 — Empty Sub-Skill Disposition Declared

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | All five sections carry EXIT GATE with Disposition: "FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]." |

---

### C-10 — Pre-Committed Finding Table Schema

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | "Pre-commit before S1." Table columns include all five required fields as separate named columns: Sub-Skill, Spec/Contract Location, Severity, Blast Radius, Impact, Remediation. |

---

### C-11 — Exit Gate Per Sub-Skill Section

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-11 | PASS | S1-S2: spec-gaps + violations + registry field + Disposition. S3-S5: spec-gaps + violations + "BOUNDARY REGISTRY entries referenced" + Disposition. All 5 sections with spec-gap and contract-violation enumeration. |
| V-12 | PASS | All 5 sections: spec-gaps + violations + "Inertia-as-spec-gap F-IDs" + Disposition. 4-field EXIT GATE throughout. |
| V-13 | PASS | All 5 sections: 3-field (spec-gaps, violations, Disposition). |
| V-14 | PASS | S1-S2: 4-field (spec-gaps, violations, named boundaries established, Disposition). S3-S5: 5-field (spec-gaps, violations, inertia-as-spec-gap, S1-S2 boundaries referenced, Disposition). All sections present. |
| V-15 | PASS | S1-S2: spec-gaps, violations, registry items, Disposition. S3-S5: 5-field (spec-gaps, violations, inertia-as-spec-gap, BOUNDARY REGISTRY entries referenced, Disposition). |

---

### C-12 — Report-Level Post-Conditions Declared

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-11 | PASS | REQUIRE: 3+ sub-skills ✓; 1+ spec-gap/violation ✓; blast-radius sort ✓; "2+ downstream sections show non-NONE BOUNDARY REGISTRY entries referenced" ✓ |
| V-12 | PASS | REQUIRE: 3+ sub-skills ✓; 1+ spec-gap/violation ✓; blast-radius sort ✓; "All Inertia-as-spec-gap F-IDs appear in table as spec-gap type with status-quo behavior named" ✓ |
| V-13 | PASS | REQUIRE: 3+ sub-skills ✓; 1+ spec-gap/violation ✓; blast-radius sort ✓ |
| V-14 | PASS | REQUIRE: all three core ✓; 2+ downstream S1-S2 boundaries referenced ✓; inertia F-IDs with named comparison point ✓ |
| V-15 | PASS | REQUIRE: all three core ✓; 2+ downstream BOUNDARY REGISTRY entries referenced ✓; inertia F-IDs with B-ID cited ✓ |

---

### C-13 — Downstream-Anchored Simulation

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-11 | PASS | BOUNDARY REGISTRY between S2-S3. S3-S5 SIMULATE: "cite the B-ID by name" at each phase/handoff/transition. EXIT GATE "BOUNDARY REGISTRY entries referenced." REQUIRE: 2+ non-NONE. Named via "B-NN: [boundary name]" — not section-number-only. |
| V-12 | FAIL | Canonical order: S1=flow-lifecycle, S2=flow-conversation — no named contract boundaries established upstream. S3-S5 INERTIA blocks reference status-quo behavior only; no structural cross-reference mechanism. |
| V-13 | PASS | Inherits V-09 structure. S3: "name the data contract boundary from S1." S4: "Aligns with named S1 contract boundaries?" S5: "cross a contract boundary named in S1... naming the S1 boundary." Three downstream sections with naming instructions. |
| V-14 | PASS | S3-S5 INERTIA: "identify which contract boundary from S1 (by name) or permission grant from S2 (by name)." SIMULATE: "name the S1 contract boundary." EXIT GATE: "S1-S2 boundaries referenced." REQUIRE: 2+ non-NONE. |
| V-15 | PASS | Strongest: BOUNDARY REGISTRY B-IDs + INERTIA blocks with "identify which BOUNDARY REGISTRY entry (B-ID and name)." SIMULATE: "cite the B-ID by name." EXIT GATE + REQUIRE both enforce. |

---

### C-14 — Inertia-as-Spec-Gap Mapping

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-11 | N/A | No INERTIA blocks. Criterion conditioned on presence of inertia framing — vacuously satisfied. |
| V-12 | PASS | INERTIA blocks in all 5 sections. Conversion rule: (a) status-quo in Impact ✓, (b) spec location ✓. EXIT GATE "Inertia-as-spec-gap F-IDs" 4th field ✓. REQUIRE enforces mapping. NONE on 4th field is a valid clean-section declaration. |
| V-13 | N/A | No INERTIA blocks. Same as V-11. |
| V-14 | PASS | INERTIA blocks in S3-S5. Conversion rule: (a) status-quo in Impact ✓, (b) spec location with S1/S2 boundary when applicable ✓. EXIT GATE + REQUIRE enforce mapping with boundary citation. |
| V-15 | PASS | INERTIA in S3-S5. Conversion rule: (a) status-quo ✓, (b) spec location ✓, (c) B-ID from BOUNDARY REGISTRY in Location ✓. Strongest C-14: B-ID anchors inertia findings to named boundaries. |

---

## Composite Scores

### V-11 — Boundary-Name Propagation

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 4 / 4 | 60 |
| Recommended | C-05, C-06, C-07 | 3 / 3 | 30 |
| Aspirational | C-08 ✓, C-09 ✓, C-10 ✓, C-11 ✓, C-12 ✓, C-13 ✓, C-14 N/A | 6 / 7 (>=5) | 10 |
| **Total** | | | **100** |

**All essential: PASS. Golden: YES.**

Hypothesis confirmed: BOUNDARY REGISTRY makes C-13 structural. B-IDs convert named cross-references from a style expectation into a column constraint — "B-NN: [name]" in Spec/Contract Location is verifiable. C-01 open question resolved: BOUNDARY REGISTRY as a compilation step in the declared sequence is neutral for C-01.

---

### V-12 — Inertia Framing with Spec-Gap Mapping

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 4 / 4 | 60 |
| Recommended | C-05, C-06, C-07 | 3 / 3 | 30 |
| Aspirational | C-08 ✓, C-09 ✓, C-10 ✓, C-11 ✓, C-12 ✓, C-13 ✗, C-14 ✓ | 6 / 7 (>=5) | 10 |
| **Total** | | | **100** |

**All essential: PASS. Golden: YES.**

Hypothesis confirmed: 4-field EXIT GATE with "Inertia-as-spec-gap F-IDs" makes C-14 structural. REQUIRE closes the loop. NONE on the 4th field is a valid clean-section state. C-13 FAIL is the expected cost of canonical order with flow sections upstream — confirmed single-axis trade-off.

---

### V-13 — Severity-Blast Ablation

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 4 / 4 | 60 |
| Recommended | C-05, C-06, C-07 | 3 / 3 | 30 |
| Aspirational | C-08 ✓, C-09 ✓, C-10 ✓, C-11 ✓, C-12 ✓, C-13 ✓, C-14 N/A | 6 / 7 (>=5) | 10 |
| **Total** | | | **100** |

**All essential: PASS. Golden: YES.**

Ablation hypothesis confirmed: "never merge" instruction is NOT load-bearing. Pre-committed Severity and Blast Radius columns mechanically prevent conflation. C-08 passes on scale definition + column presence alone. Future variations may drop the "never merge" prose without rubric cost.

---

### V-14 — Contract-First + Inertia Framing (Combination)

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 4 / 4 | 60 |
| Recommended | C-05, C-06, C-07 | 3 / 3 | 30 |
| Aspirational | C-08 ✓, C-09 ✓, C-10 ✓, C-11 ✓, C-12 ✓, C-13 ✓, C-14 ✓ | 7 / 7 | 10 |
| **Total** | | | **100** |

**All essential: PASS. Golden: YES.**

First variation to pass all 7 aspirational criteria. Contract-first creates named boundaries in S1-S2; INERTIA blocks in S3-S5 reference those names. Result: each inertia observation is framed as "status-quo assumes [named boundary] behaves as X; spec is silent" — a single finding row satisfying both C-13 and C-14. Cleanest 7/7 with no BOUNDARY REGISTRY compilation step overhead.

---

### V-15 — Boundary Registry + Inertia Cross-Reference (Combination)

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 4 / 4 | 60 |
| Recommended | C-05, C-06, C-07 | 3 / 3 | 30 |
| Aspirational | C-08 ✓, C-09 ✓, C-10 ✓, C-11 ✓, C-12 ✓, C-13 ✓, C-14 ✓ | 7 / 7 | 10 |
| **Total** | | | **100** |

**All essential: PASS. Golden: YES.**

Maximum structural pressure on C-13 and C-14. BOUNDARY REGISTRY provides formal B-IDs; INERTIA blocks ask "what does status-quo assume about B-NN?" Each finding carries status-quo comparison point (C-14) and "B-NN: [name]" citation (C-13). REQUIRE post-condition covers both axes. Highest structural investment of all R3 variations.

---

## Variation Rankings

| Rank | Variation | Score | Golden | Aspirational | Notes |
|------|-----------|-------|--------|-------------|-------|
| 1 | V-15 | 100 | YES | 7/7 | Maximum C-13+C-14 structural pressure; B-IDs + INERTIA cross-reference |
| 2 | V-14 | 100 | YES | 7/7 | Cleanest combination; INERTIA in S3-S5 references named S1-S2 boundaries; no compilation step overhead |
| 3 | V-11 | 100 | YES | 6/7 (C-14 N/A) | Strongest single-axis C-13; BOUNDARY REGISTRY + B-IDs |
| 4 | V-12 | 100 | YES | 6/7 (C-13 ✗) | Strongest single-axis C-14; canonical order prevents C-13 |
| 5 | V-13 | 100 | YES | 6/7 (C-14 N/A) | Ablation test only; "never merge" confirmed overhead |

---

## Axis Resolution

| Scorecard Question | Answer |
|-------------------|--------|
| Does BOUNDARY REGISTRY as a non-sub-skill step in declared sequence satisfy C-01? | YES -- simulation sections appear in declared order; BOUNDARY REGISTRY is a compilation step, neutral for C-01 |
| Does removing "never merge" instruction fail C-08? | NO -- scale defined + separate columns enforce independence; "never merge" prose is confirmed token overhead |
| Does writing NONE on "Inertia-as-spec-gap F-IDs" satisfy C-14 gate? | YES -- NONE is a valid clean-section declaration; it does not bypass the gate |
| Does V-12 canonical order prevent C-13? | YES -- S1/S2 are flow sections that establish no named contract boundaries for downstream reference |

---

## Excellence Signals

### SIGNAL-1: Boundary-Registry-as-Artifact (V-11, V-15)
**Pattern**: `boundary-registry-as-artifact`
Compiling a BOUNDARY REGISTRY artifact between S2 and S3 with B-IDs converts C-13 cross-references from a style expectation into a structural constraint. "B-NN: [boundary name]" format in the Spec/Contract Location column makes citation verifiable. EXIT GATE field "BOUNDARY REGISTRY entries referenced: [B-IDs or NONE]" provides per-section coverage audit. REQUIRE post-condition "2+ downstream sections with non-NONE B-IDs" prevents a registry that is declared but never cited.

### SIGNAL-2: Inertia-Boundary Cross-Reference (V-14, V-15)
**Pattern**: `inertia-boundary-crossref`
INERTIA blocks in downstream sections (S3-S5) that open by identifying which named upstream boundary the status-quo behavior assumes creates the tightest possible C-13+C-14 intersection. Each inertia observation is framed as "status-quo assumes [named boundary] behaves as X; spec is silent." The finding produced satisfies C-13 (named upstream boundary reference) and C-14 (inertia-as-spec-gap with named comparison point) in a single table row. V-15 elevates this with B-ID format in the Location column.

### SIGNAL-3: Severity-Blast Column Independence (V-13)
**Pattern**: `severity-blast-column-independence`
Confirmed: removing "independent of blast radius; never merge" from the Severity DEFINITIONS block does not affect C-08 compliance. Pre-committed Severity and Blast Radius columns as separate named table columns enforce field independence mechanically. The prose instruction is redundant overhead at prompt design level.

---

## Round Summary

| Metric | Value |
|--------|-------|
| Top score | 100 |
| Golden variations | 5 of 5 |
| Non-golden | None |
| Recommended carry-forward | V-15 (maximum structure; both new criteria at full strength) or V-14 (cleanest 7/7 -- no compilation step overhead) |
| R4 candidate axes | (1) boundary-registry compression: fold BOUNDARY REGISTRY into S1/S2 EXIT GATEs as a named-boundary list rather than a standalone step; (2) full-span inertia: extend INERTIA blocks to S1-S2 (V-14/V-15 currently S3-S5 only); (3) EXIT GATE field compression: test 5-field condensed format ("Spec-gaps: / Violations: / Inertia: / B-IDs: / Disposition:") against verbosity overhead |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["boundary-registry-as-artifact: BOUNDARY REGISTRY compiled between S2 and S3 with B-IDs converts C-13 cross-references from style to structural constraint; EXIT GATE 'BOUNDARY REGISTRY entries referenced' makes downstream citation auditable per section", "inertia-boundary-crossref: INERTIA blocks in downstream sections that open by identifying which named upstream boundary the status-quo assumes satisfies C-13 and C-14 simultaneously in a single finding row; B-ID format in V-15 makes this maximally mechanical", "severity-blast-column-independence: confirmed that 'independent of blast radius; never merge' prose is not load-bearing when Severity and Blast Radius are separate pre-committed columns; can be dropped as token overhead"]}
```
