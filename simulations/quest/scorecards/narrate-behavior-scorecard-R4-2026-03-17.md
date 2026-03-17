Now I have everything I need. Let me score all 5 variations and write the scorecard.

---

## R4 Scorecard — narrate-behavior

**Rubric version**: v4 | **Scale**: Essential 40 + Recommended 30 + Aspirational 10 cap = **80 pts max**
**Aspirational rule**: any 6 of 10 earns the 10-pt cap.

---

### Criterion-by-Criterion Analysis

---

#### C-01 — Declared Execution Sequence

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | All declare: `S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT`. Sections follow that order. BOUNDARY REGISTRY compilation step is neutral (confirmed R3). |

---

#### C-02 — Output Is a Single Unified Report

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | "Do not produce five separate outputs. Produce one unified simulation findings report." REPORT section carries a single title/date block. |

---

#### C-03 — Findings Ranked by Blast Radius

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | All REPORT sections: "Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last). Label at top: 'Sorted by blast radius -- WIDE to NARROW.'" REQUIRE blocks confirm sort. |

---

#### C-04 — At Least One Spec Gap or Contract Violation

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | Pre-committed FINDING TABLE has Finding Type column with spec-gap / contract-violation. REQUIRE: "1+ finding typed spec-gap or contract-violation with a specific spec location." Inertia conversion rule in V-16–V-20 structurally produces spec-gap findings. |

**Essential (C-01–C-04): ALL PASS — 40/40 for all variations.**

---

#### C-05 — Finding Schema: Source + Location + Impact

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | Pre-committed FINDING TABLE: Sub-Skill (source), Spec/Contract Location (location), Impact (impact) as distinct named columns. Column rules define each separately. |

---

#### C-06 — Cross-Sub-Skill Coverage

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | REQUIRE in all REPORT sections: "3+ distinct sub-skills represented in findings." |

---

#### C-07 — Remediation Guidance Present

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | Remediation is a separate pre-committed column. Column rule: "concrete action (spec update, contract clarification, or code change)." |

**Recommended (C-05–C-07): ALL PASS — 30/30 for all variations.**

---

#### C-08 — Severity Classification Applied

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | DEFINITIONS declares HIGH/MED/LOW scale with descriptions. Severity is a separate named column in the pre-committed table. "Never merge" prose absent (per C-17 confirmation from R3) — not required for C-08. |

---

#### C-09 — Empty Sub-Skill Disposition Declared

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-16, V-17, V-19 | PASS | All 5 EXIT GATEs carry "Disposition: FINDINGS [N] \| NO FINDINGS -- [one-clause rationale if zero]." |
| V-18, V-20 | PASS | Condensed: "Disposition: [N findings \| NONE -- one-clause rationale if zero]." Same coverage, uniform format. |

---

#### C-10 — Pre-Committed Finding Table Schema

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | FINDING TABLE defined before S1 with separate named columns: F-ID, Sub-Skill, Spec/Contract Location, Finding Type, Blast Radius, Severity, Impact, Remediation. All required fields present as distinct columns. |

---

#### C-11 — Exit Gate Per Sub-Skill Section

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-16 | PASS | S1-S2: spec-gaps, violations, boundaries-to-register, Disposition. S3-S5: spec-gaps, violations, inertia F-IDs, BOUNDARY REGISTRY entries referenced, Disposition. All 5 sections present with spec-gap and contract-violation enumeration. |
| V-17 | PASS | S1-S2: spec-gaps, violations, inertia-as-spec-gap F-IDs, boundaries-to-register, Disposition. S3-S5: 5-field with inertia F-IDs and B-IDs referenced. All 5 sections. |
| V-18 | PASS | Uniform condensed 5-field format: `Spec-gaps: / Violations: / Inertia: / B-IDs: / Disposition:` — rubric explicitly states condensed format satisfies; label length is not a factor. S1-S2 carry Inertia=NONE (clean-section declaration per R3 resolution). |
| V-19 | PASS | Same as V-17 (verbose asymmetric) with compact registry. All 5 sections with spec-gap, violation, and Disposition fields. |
| V-20 | PASS | Uniform condensed 5-field format (V-18 structure) with Inertia≠NONE in S1-S2 (INERTIA blocks present). Field presence identical to V-18; inertia field populated rather than NONE. |

**C-11 open question resolved (V-18)**: Inertia=NONE in S1-S2 condensed gate — PASS. Same logic as "NONE on 4th field satisfies gate" from R3. Clean-section declaration is valid; no INERTIA block in S1-S2 is a structural state, not a bypass.

**C-11 open question resolved (V-20)**: Inertia≠NONE in S1-S2 condensed gate — PASS. INERTIA blocks present in S1-S2; Inertia field populated correctly. Disposition field carries count. No ambiguity.

---

#### C-12 — Report-Level Post-Conditions Declared

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-16 | PASS | REQUIRE: 3+ sub-skills ✓; 1+ spec-gap/violation ✓; blast-radius sort ✓; 2+ downstream non-NONE BOUNDARY REGISTRY referenced ✓; all inertia F-IDs in table as spec-gap with B-ID cited ✓. |
| V-17 | PASS | REQUIRE: all three core ✓; 2+ downstream B-IDs ✓; all inertia F-IDs from all 5 sections ✓; S1-S2 inertia comparison points ✓. Most comprehensive REQUIRE block. |
| V-18 | PASS | REQUIRE: all three core ✓; 2+ downstream non-NONE B-IDs ✓; inertia F-IDs as spec-gap with status-quo named ✓. |
| V-19 | PASS | REQUIRE: all three core ✓; 2+ downstream B-IDs ✓; all inertia F-IDs from all 5 sections ✓; compact registry 2+ entries ✓. |
| V-20 | PASS | REQUIRE: all three core ✓; 2+ downstream non-NONE B-IDs ✓; all inertia F-IDs ✓; S1-S2 inertia comparison points ✓. |

---

#### C-13 — Downstream-Anchored Simulation

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-16 | PASS | S3-S5 INERTIA blocks: "name the status-quo behavior and identify which BOUNDARY REGISTRY entry (B-ID and name) it assumes." SIMULATE: "cite B-ID by name" at each boundary crossing. EXIT GATE B-IDs referenced + REQUIRE 2+ non-NONE. Named via "B-NN: [name]", not section-number-only. |
| V-17 | PASS | S3-S5 INERTIA + SIMULATE cite B-IDs. EXIT GATE B-IDs referenced. REQUIRE 2+ non-NONE. S1-S2 INERTIA uses text-names (pre-registry); S3-S5 use B-IDs — traceability chain strongest of all variations. |
| V-18 | PASS | S3-S5 INERTIA + SIMULATE cite B-IDs. Condensed EXIT GATE B-IDs field enumerates referenced B-IDs. REQUIRE 2+ non-NONE. |
| V-19 | PASS | Identical to V-17 for S3-S5 anchor. Compact registry is the reference; B-IDs are named. 2+ downstream references enforced. |
| V-20 | PASS | Identical to V-18 for S3-S5 anchor under condensed gates. S1-S2 INERTIA produces text-name findings; S3-S5 cite B-IDs. |

---

#### C-14 — Inertia-as-Spec-Gap Mapping

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-16 | PASS | INERTIA in S3-S5. Conversion rule: (a) status-quo behavior in Impact ✓, (b) spec location ✓, (c) B-ID cited in Location ✓. EXIT GATE "Inertia-as-spec-gap F-IDs". REQUIRE enforces. |
| V-17 | PASS | INERTIA in all 5 sections. Conversion rule applies to all. S1-S2: text-name in Location; S3-S5: B-ID in Location. REQUIRE covers all 5 sections + S1-S2 comparison points. Maximum C-14 breadth. |
| V-18 | PASS | INERTIA in S3-S5. Condensed EXIT GATE Inertia field. Conversion rule same as V-16. REQUIRE enforces. |
| V-19 | PASS | INERTIA in all 5 sections (V-17 structure). Conversion rule applies to all. S1-S2 use text-name; S3-S5 use B-ID from compact registry. REQUIRE covers all 5 sections. |
| V-20 | PASS | INERTIA in all 5 sections. Condensed EXIT GATE Inertia field populated in S1-S2 and S3-S5. Conversion rule applies to all. REQUIRE covers all. |

---

#### C-15 — Boundary Registry as Structural Artifact

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-16 | PASS | Compact B-ID list placed between S2 and S3. Format: `B-NN: [name] -- [type] -- [description]`. "At minimum two entries required." S3-S5 EXIT GATEs: "BOUNDARY REGISTRY entries referenced: [list B-IDs]". Pass condition does not specify table format; B-IDs present and named. |
| V-17 | PASS | Full 5-column BOUNDARY REGISTRY table between S2 and S3. 2+ B-IDs. S3-S5 EXIT GATEs enumerate B-IDs referenced. Full structural fidelity. |
| V-18 | PASS | Full BOUNDARY REGISTRY table between S2 and S3. S3-S5 condensed EXIT GATE B-IDs field enumerates referenced entries. |
| V-19 | PASS | Compact B-ID list between S2 and S3. Adds `inertia-boundary` as third type. S3-S5 EXIT GATEs enumerate B-IDs. |
| V-20 | PASS | Full BOUNDARY REGISTRY table between S2 and S3. S3-S5 condensed EXIT GATE B-IDs field enumerates referenced entries. |

**C-15 open question resolved (V-16, V-19)**: Compact B-ID list satisfies "BOUNDARY REGISTRY block with 2+ named B-IDs." Table format is NOT required — B-IDs present, names explicit, block placed between S2 and S3. PASS.

---

#### C-16 — Inertia-Boundary Cross-Reference

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | S3-S5 INERTIA blocks open by naming "which BOUNDARY REGISTRY entry (B-ID and name) the status-quo behavior assumes." Inertia conversion rule produces spec-gap finding with named boundary as comparison point. C-16 applies to downstream sections (S3-S5) only — S1-S2 INERTIA blocks in V-17, V-19, V-20 are C-14 contributors, not C-16 obligors. |

**C-16 open question resolved (V-17, V-19, V-20)**: S1-S2 INERTIA blocks do NOT create C-16 obligations. C-16 is conditioned on "INERTIA blocks in downstream sections (S3-S5)." S1-S2 are upstream sections — their INERTIA blocks produce C-14 findings only.

---

#### C-17 — Structural Column Independence for Severity and Blast Radius

| Variation | Result | Evidence |
|-----------|--------|----------|
| All 5 | PASS | Blast Radius and Severity are separate named columns in the pre-committed FINDING TABLE schema. "Never merge / independent of blast radius" prose absent from all R4 variations per C-17 confirmation from R3. Absence of prose is not penalized. |

---

### Aspirational Summary per Variation

| Criterion | V-16 | V-17 | V-18 | V-19 | V-20 |
|-----------|------|------|------|------|------|
| C-08 Severity | PASS | PASS | PASS | PASS | PASS |
| C-09 Disposition | PASS | PASS | PASS | PASS | PASS |
| C-10 Pre-committed schema | PASS | PASS | PASS | PASS | PASS |
| C-11 Exit gates | PASS | PASS | PASS | PASS | PASS |
| C-12 Report post-conditions | PASS | PASS | PASS | PASS | PASS |
| C-13 Downstream anchor | PASS | PASS | PASS | PASS | PASS |
| C-14 Inertia-as-spec-gap | PASS | PASS | PASS | PASS | PASS |
| C-15 Boundary registry | PASS | PASS | PASS | PASS | PASS |
| C-16 Inertia-boundary crossref | PASS | PASS | PASS | PASS | PASS |
| C-17 Column independence | PASS | PASS | PASS | PASS | PASS |
| **Count** | **10/10** | **10/10** | **10/10** | **10/10** | **10/10** |
| **Aspirational pts** | **10** | **10** | **10** | **10** | **10** |

---

### Composite Scores

#### V-16 — Registry Compression

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01–C-04 | 4 / 4 | 40 |
| Recommended | C-05–C-07 | 3 / 3 | 30 |
| Aspirational | C-08–C-17 | 10 / 10 | 10 |
| **Total** | | | **80** |

**All essential: PASS. Golden: YES.**

Compact B-ID list format is structurally equivalent to the full 5-column table for C-15. Table columns are not load-bearing — B-ID presence and named boundaries are sufficient. The compact format is clean and lower-token without aspirational cost. Single-axis test confirms the hypothesis.

---

#### V-17 — Full-Span Inertia

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01–C-04 | 4 / 4 | 40 |
| Recommended | C-05–C-07 | 3 / 3 | 30 |
| Aspirational | C-08–C-17 | 10 / 10 | 10 |
| **Total** | | | **80** |

**All essential: PASS. Golden: YES.**

Full-span INERTIA creates C-14 findings in S1-S2 using text-names (B-IDs not yet assigned). BOUNDARY REGISTRY table promotes those text-names to formal B-IDs. S3-S5 INERTIA blocks then cite B-IDs — completing a two-phase naming pipeline from discovery to structural citation. Introduces `inertia-boundary` as a third registry type, formally categorizing INERTIA-surfaced boundaries. C-16 obligation is confined to S3-S5 per rubric text; S1-S2 INERTIA is C-14 material only.

---

#### V-18 — EXIT GATE Compression

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01–C-04 | 4 / 4 | 40 |
| Recommended | C-05–C-07 | 3 / 3 | 30 |
| Aspirational | C-08–C-17 | 10 / 10 | 10 |
| **Total** | | | **80** |

**All essential: PASS. Golden: YES.**

Uniform 5-field condensed EXIT GATE format satisfies C-11 across all 5 sections (rubric explicitly endorses condensed format). Inertia=NONE in S1-S2 is a clean-section declaration. B-IDs field serving dual purpose (registration in S1-S2, audit in S3-S5) is disambiguated by section context — C-11 requires enumeration, not semantic uniformity. Single-axis test confirms format uniformity is cost-neutral.

---

#### V-19 — Registry Compression + Full-Span Inertia

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01–C-04 | 4 / 4 | 40 |
| Recommended | C-05–C-07 | 3 / 3 | 30 |
| Aspirational | C-08–C-17 | 10 / 10 | 10 |
| **Total** | | | **80** |

**All essential: PASS. Golden: YES.**

Tightest combination: compact registry reduces format overhead; full-span INERTIA maximizes discovery surface; S1-S2 inertia observations flow directly into compact B-ID list without table column scaffolding. The `inertia-boundary` type in the compact registry is the most natural fit — a one-line B-ID entry and a one-token type keyword. Discovery-to-citation pipeline (text-name → B-ID → downstream citation) is complete with minimum structural overhead.

---

#### V-20 — Full-Span Inertia + EXIT GATE Compression

| Tier | Criteria | Pass Count | Points |
|------|----------|-----------|--------|
| Essential | C-01–C-04 | 4 / 4 | 40 |
| Recommended | C-05–C-07 | 3 / 3 | 30 |
| Aspirational | C-08–C-17 | 10 / 10 | 10 |
| **Total** | | | **80** |

**All essential: PASS. Golden: YES.**

Maximum coverage (full-span INERTIA, all 5 sections) with minimum gate verbosity (condensed 5-field format). Inertia≠NONE in S1-S2 condensed gates is the most field-dense configuration — confirmed PASS. Dual-purpose B-IDs field with non-NONE Inertia field in S1-S2 demonstrates no C-09 or C-11 ambiguity. Full BOUNDARY REGISTRY table preserved; full-span inertia captured in uniform condensed gates.

---

### Variation Rankings

All 5 variations score 80/80. Ranking is by structural richness and coverage-efficiency ratio.

| Rank | Variation | Score | Golden | Aspirational | Notes |
|------|-----------|-------|--------|-------------|-------|
| 1 | V-19 | 80 | YES | 10/10 | Compact registry + full-span inertia + `inertia-boundary` type; maximum coverage at minimum overhead |
| 2 | V-17 | 80 | YES | 10/10 | Full-span inertia + `inertia-boundary` type + full table; maximum structural fidelity |
| 3 | V-20 | 80 | YES | 10/10 | Full-span inertia + condensed gates; dual-purpose B-IDs field confirmed clean |
| 4 | V-16 | 80 | YES | 10/10 | Compact registry confirmed C-15 equivalent; single-axis, clean result |
| 5 | V-18 | 80 | YES | 10/10 | Condensed gates confirmed C-11 equivalent; uniform format confirmed cost-neutral |

---

### Axis Resolution

| Scorecard Question | Answer |
|-------------------|--------|
| Does compact B-ID list satisfy C-15 "BOUNDARY REGISTRY block with B-IDs"? | **YES** — B-IDs present, names explicit, block placed between S2 and S3; table columns not required |
| Do S1-S2 INERTIA blocks satisfy C-16? | **NO obligation** — C-16 applies to downstream sections (S3-S5) only; S1-S2 INERTIA is C-14 material only |
| Does Inertia=NONE in S1-S2 condensed EXIT GATE satisfy C-11? | **YES** — same resolution as R3; valid clean-section declaration, not a bypass |
| Does Inertia≠NONE in S1-S2 condensed EXIT GATE (V-20) create ambiguity? | **NO** — Disposition field is populated; INERTIA block present; no C-09 or C-11 issue |
| Can B-IDs field serve dual purpose (register vs reference) in same column? | **YES** — section context disambiguates; C-11 requires enumeration, not semantic uniformity of field purpose |

---

### Excellence Signals

#### SIGNAL-1: Inertia-Boundary Type in Registry (V-17, V-19)
**Pattern**: `inertia-boundary-type-in-registry`
Introducing `inertia-boundary` as a third registry type (alongside `contract-boundary` and `permission-grant`) formally categorizes INERTIA-surfaced boundaries as a named structural artifact class. Without this type, an inertia observation that names a boundary produces a finding but the boundary enters the registry without distinguishing its discovery pathway. With `inertia-boundary`, the registry records both the boundary and how it was found. V-19's compact format is the most efficient expression: `B-03: session-persistence-assumption -- inertia-boundary -- status-quo assumes cross-turn state`.

#### SIGNAL-2: Text-Name-to-B-ID Promotion Pipeline (V-17, V-19, V-20)
**Pattern**: `text-name-to-BID-promotion-pipeline`
A two-phase naming pipeline: S1-S2 INERTIA blocks discover and name boundaries by text (B-IDs not yet assigned); BOUNDARY REGISTRY promotes those text-names to formal B-IDs; S3-S5 INERTIA blocks cite B-IDs. This creates a complete traceability chain from pre-registry discovery to post-registry structural citation. The inertia conversion rule for S1-S2 ("use boundary text-name since registry is not yet compiled") handles the transition point cleanly. S1-S2 findings with text-names in Location remain valid after registry compilation — the B-ID annotation is optional.

#### SIGNAL-3: Compact Registry as C-15-Equivalent Format (V-16, V-19)
**Pattern**: `compact-registry-structural-equivalence`
Confirmed: one-line-per-entry `B-NN: name -- type -- description` format satisfies C-15 without table columns. The pass condition is about B-ID presence and named boundaries between S2 and S3, not about column structure. The compact format is especially compatible with inertia-boundary types (V-19) and is a lower-token alternative to the 5-column table whenever tabular alignment is not needed for readability.

#### SIGNAL-4: Dual-Purpose B-IDs Exit Gate Field (V-18, V-20)
**Pattern**: `dual-purpose-BID-exit-gate-field`
A single B-IDs field can serve registration semantics in S1-S2 ("items to register") and audit semantics in S3-S5 ("B-IDs referenced in findings") within a uniform condensed EXIT GATE format. Section context disambiguates field semantics; the executor's instructions make the dual purpose explicit. This reduces the asymmetric-field design (different EXIT GATE fields per section tier) to a uniform 5-field format that is fully C-11 compliant. The dual-purpose pattern applies to any field whose content is phase-dependent rather than field-name-dependent.

---

### Round Summary

| Metric | Value |
|--------|-------|
| Top score | 80 |
| Golden variations | 5 of 5 |
| Non-golden | None |
| Recommended carry-forward | V-19 (compact registry + full-span inertia + inertia-boundary type; maximum coverage-efficiency) or V-20 (full-span inertia + condensed gates + full table; clearest structural traceability) |
| R5 candidate axes | (1) inertia-boundary type promotion to full registry column — does the `inertia-boundary` type enable a "surfaced-by" audit query across findings?; (2) S1-S2 text-name back-annotation — can S1-S2 findings annotate the B-ID retroactively after registry compilation?; (3) combined V-19+V-20 — compact registry + full-span inertia + condensed gates (all three compression axes simultaneously) |

---

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["inertia-boundary-type-in-registry: introducing inertia-boundary as a third BOUNDARY REGISTRY type (alongside contract-boundary and permission-grant) formally categorizes INERTIA-surfaced boundaries as a named structural artifact class, recording both the boundary and its discovery pathway; compact registry format is the most efficient expression", "text-name-to-BID-promotion-pipeline: two-phase naming pipeline where S1-S2 INERTIA blocks discover and name boundaries by text-name, BOUNDARY REGISTRY promotes them to formal B-IDs, and S3-S5 INERTIA blocks cite B-IDs — full traceability from pre-registry discovery to post-registry structural citation", "compact-registry-structural-equivalence: confirmed that one-line-per-entry B-NN: name -- type -- description format satisfies C-15 without table columns; pass condition requires B-ID presence and named boundaries between S2 and S3, not tabular structure", "dual-purpose-BID-exit-gate-field: a single B-IDs field can serve registration semantics in S1-S2 and audit semantics in S3-S5 within a uniform condensed EXIT GATE, disambiguated by section context; reduces asymmetric per-tier EXIT GATE design to uniform 5-field format fully compliant with C-11"]}
```
