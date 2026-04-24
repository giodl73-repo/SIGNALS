## crew-review — Quest Score R11 (v10 rubric)

### Scoring Key

| Tier | Criteria | Weight | Max |
|------|----------|--------|-----|
| Essential | C-01 to C-05 | 12 pts each × 5 | 60 |
| Recommended | C-06 to C-10, C-14 | 10 pts each × 6 | 60 |
| Aspirational | C-11 to C-13, C-15 to C-32 | 2.5 pts each × 21 | 52.5 |
| **Total** | | | **172.5** |

Golden threshold: 80. Disqualifying condition: any essential FAIL.

---

### Common Infrastructure (all 5 variations)

Before per-variation scoring, I identify the shared mechanisms present in all variations:

| Mechanism | Criteria it satisfies |
|-----------|----------------------|
| PHASE 1 L1-L4 load with unconditional error halts (no soft fallback) | C-01, C-14 |
| 6-column output schema with `NOT:` anti-patterns on all 6 columns | C-02, C-03, C-13, C-19, C-25 |
| PHASE 2 -- CHALLENGE header + G1 OPEN/CLOSED + 4-condition closure predicate + "Domain review does not begin until G1 transitions to CLOSED" | C-15, C-17, C-20 |
| 4-slot null hypothesis form (SLOT-A/B/C/D) | C-11 |
| C4 escalation rule with separate 6-column rows for each unfilled slot + "Do not embed..." + "Do not append..." prohibitions | C-16, C-18, C-21 |
| PHASE 3 -- REVIEW with per-slot Lens cell enforcement | C-04, C-05, C-09, C-10, C-12 |
| PHASE 3.5 -- SYNTHESIZE header at same heading level as PHASE 3 and PHASE 4 | **C-31** |
| G2 OPEN/CLOSED states + "AMEND does not begin until G2 transitions to CLOSED" | **C-32** |
| Per-slot verdict assignment (converged / conflicted / unique) | C-07, C-22, C-27 |
| PHASE 4 -- VALIDATE header | C-23 |
| Criterion-check table inside PHASE 4 covering C-11 through C-32 (21 rows) | C-24, C-26 |
| 5-column criterion-check schema: `Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO` | C-28, C-29, C-30 |
| PHASE 5 RENDER with AMEND section (5+ specific slot-numbered options) | C-06, C-08 |

This shared base passes all 32 criteria. Every variation inherits these mechanisms. Variation-specific differences produce structural differentiation but not scoring gaps.

---

### V-01 — Lifecycle (Direct PHASE 3.5 Integration)

**Axis**: Minimal PHASE 3.5 addition to V-01 R10 canonical. No new schemas beyond the 6-column review matrix.

#### Essential

| ID | Status | Evidence |
|----|--------|----------|
| C-01 | **PASS** | L1-L4 load, roles from `.roles/` only, zero invented |
| C-02 | **PASS** | 6-column matrix: Slot, Role, Lens, Findings, Severity, Recommendation |
| C-03 | **PASS** | Severity enum: exactly HIGH/MEDIUM/LOW; NOT: freestyle labels |
| C-04 | **PASS** | Lens column, one sentence from `lens.verify`, specific per role |
| C-05 | **PASS** | Recommendation schema: "(1) what to do and (2) where in the artifact" |

Essential subtotal: **60/60**

#### Recommended

| ID | Status | Evidence |
|----|--------|----------|
| C-06 | **PASS** | Standard 2-4 / deep = all non-Slot-1 roles per manifest |
| C-07 | **PASS** | PHASE 3.5 S1 assigns convergence/conflict/unique per slot; G2-verified |
| C-08 | **PASS** | PHASE 5 R4: 5 specific AMEND options with slot numbers |
| C-09 | **PASS** | Slot 1 = all roles with `archetype: challenger`; manifest declares Slot 1 first |
| C-10 | **PASS** | Findings schema: "names a specific artifact surface: section title, field name, diagram element, or named assumption" |
| C-14 | **PASS** | L3 unconditional halts for absent/empty directory and missing required fields |

Recommended subtotal: **60/60**

#### Aspirational

| ID | Status | Evidence |
|----|--------|----------|
| C-11 | **PASS** | SLOT-A/B/C/D 4-slot form in PHASE 2 C2-C3 |
| C-12 | **PASS** | Lens column in schema; anti-pattern excludes "merely restate the role name" |
| C-13 | **PASS** | Typed schema table with column-level contracts; PHASE 4 validates per-row before write |
| C-15 | **PASS** | "PHASE 2 -- CHALLENGE" heading at same level as PHASE 3 |
| C-16 | **PASS** | C4: per-slot HIGH finding; "applies to each slot individually" |
| C-17 | **PASS** | G1 OPEN/CLOSED + "Domain review does not begin until G1 transitions to CLOSED" |
| C-18 | **PASS** | C4: "separate, dedicated matrix row" -- 6-column entry at 1a/1b/1c/1d |
| C-19 | **PASS** | Lens NOT: generic restatements; Findings NOT: abstract observations |
| C-20 | **PASS** | G1 has OPEN/CLOSED states + 4-condition closure predicate |
| C-21 | **PASS** | C4: "Do not embed..."; "Do not append..." inside escalation rule |
| C-22 | **PASS** | Slot column present; synthesis verdicts use "Slot [N] converged/conflicts/unique..." |
| C-23 | **PASS** | "PHASE 4 -- VALIDATE" heading at same level as PHASE 2 and PHASE 3 |
| C-24 | **PASS** | Criterion-check table inside PHASE 4 with per-criterion evidence |
| C-25 | **PASS** | All 6 review matrix columns carry NOT: exclusions |
| C-26 | **PASS** | Table rows C-11 through C-32 present (21 rows); self-referential C-26 row present |
| C-27 | **PASS** | PHASE 3.5 S1 covers every slot; G2 checks N verdicts for N slots |
| C-28 | **PASS** | "Remediation if NO" column present; every row has a specific instruction |
| C-29 | **PASS** | All 21 rows carry populated remediation; "all 21 rows in this table carry a populated Remediation if NO cell" |
| C-30 | **PASS** | 5-column header: `Criterion \| Description \| Status \| Evidence in this draft \| Remediation if NO` |
| C-31 | **PASS** | "PHASE 3.5 -- SYNTHESIZE" heading between PHASE 3 and PHASE 4 at same heading level |
| C-32 | **PASS** | G2 OPEN/CLOSED + "AMEND does not begin until G2 transitions to CLOSED" |

Aspirational subtotal: **52.5/52.5** (21 × 2.5)

**V-01 total: 60 + 60 + 52.5 = 172.5/172.5** ✓ Golden

---

### V-02 — Output Format (Typed Synthesis Schema)

**Axis**: Adds 3-column typed synthesis schema (Slot | Verdict Type | Statement) alongside the 6-column review matrix schema. G2 closure verifies synthesis table row count vs. manifest slot count. Both schemas declared before execution with full NOT: anti-pattern exclusions.

#### Essential — **60/60** (same as V-01; matrix + severity + roles unchanged)

#### Recommended — **60/60** (same mechanism, C-07 strengthened by synthesis table)

#### Aspirational

All C-11 through C-30 pass identically to V-01.

| ID | Status | Evidence — V-02 specific |
|----|--------|--------------------------|
| C-25 | **PASS** | All 6 review matrix columns + all 3 synthesis schema columns carry NOT: exclusions (C-25 evidence text confirms this) |
| C-30 | **PASS** | 5-column criterion-check table intact; synthesis schema is a second output schema, not the criterion-check table |
| C-31 | **PASS** | "PHASE 3.5 -- SYNTHESIZE" header present |
| C-32 | **PASS** | G2 closure: synthesis table row count check + "AMEND does not begin until G2 transitions to CLOSED" |

**V-02 total: 172.5/172.5** ✓ Golden

**V-02 structural difference**: Introduces typed synthesis schema as a second output artifact. G2 closure predicate checks synthesis table structural completeness (row count = slot count; Verdict Type enum; Statement format) rather than prose verification only. This extends C-25's exhaustive anti-pattern coverage to the synthesis schema columns — going beyond what C-25 formally requires but not adding a separate score.

---

### V-03 — Inertia Framing (Slot 1 Synthesis Anchor)

**Axis**: PHASE 3.5 G2 closure condition 1 explicitly requires Slot 1 verdict to name its relationship to at least one domain slot's finding. The slot manifest Slot 1 entry includes an "inertia competitor" field. PHASE 5 R1 header includes "Inertia competitor: [status-quo alternative]." PHASE 2 adds a framing sentence: "Domain review cannot assess value without first naming what value must exceed."

#### Essential — **60/60**

#### Recommended — **60/60**

C-07 is specifically strong here: synthesis begins with Slot 1 inertia verdict that names convergence or conflict against domain slots by slot number.

#### Aspirational

| ID | Status | Evidence — V-03 specific |
|----|--------|--------------------------|
| C-27 | **PASS** | G2 predicate: 4 conditions; condition 1 specifically verifies Slot 1 inertia verdict names domain relationship. G2 closure note: "[N] slots, [N] verdicts; Slot 1 inertia verdict present" |
| C-31 | **PASS** | "PHASE 3.5 -- SYNTHESIZE" header |
| C-32 | **PASS** | G2 OPEN/CLOSED + "AMEND does not begin until G2 transitions to CLOSED" |

All other aspirational criteria pass identically to V-01.

**V-03 total: 172.5/172.5** ✓ Golden

**V-03 structural difference**: G2 closure is semantically stricter than V-01's per-slot coverage check — condition 1 requires Slot 1 to explicitly name the inertia relationship to a domain slot (a semantic predicate), not just "assigned exactly one verdict" (structural count). This is a superstructural addition beyond C-32's pass condition, making V-03 the strongest synthesis gate design.

---

### V-04 — Lifecycle + Output Format (Two-Axis)

**Axis**: V-01 + V-02 merged. Synthesis contract declared in three locations: (1) AMEND output contract in schema section ("AMEND does not begin until PHASE 3.5 G2 transitions to CLOSED. The synthesis schema contract is binding..."), (2) PHASE 3.5 G2 predicate and gate, (3) synthesis typed table completeness check at G2 closure.

#### Essential — **60/60**

#### Recommended — **60/60**

#### Aspirational

| ID | Status | Evidence — V-04 specific |
|----|--------|--------------------------|
| C-25 | **PASS** | All 6 review matrix + all 3 synthesis schema columns carry NOT: exclusions |
| C-30 | **PASS** | 5-column criterion-check schema intact |
| C-31 | **PASS** | "PHASE 3.5 -- SYNTHESIZE" header |
| C-32 | **PASS** | G2 + "AMEND does not begin until G2 transitions to CLOSED" + synthesis schema contract binding in AMEND output contract block |

All other aspirational criteria pass identically.

**V-04 total: 172.5/172.5** ✓ Golden

**V-04 structural difference**: Triple-location synthesis enforcement — no execution path reaches AMEND without hitting the synthesis obligation. The synthesis schema contract is stated as "binding in both this schema declaration and in PHASE 3.5 S1," then restated in the AMEND output contract. C-32 is met in multiple structural locations simultaneously.

---

### V-05 — Three-Axis (Lifecycle + Output Format + Role Sequence)

**Axis**: V-04 + verbatim `expertise.relevance` quotes in slot manifest for all non-challenger slots + L5 registry verification step (character-for-character quote match; halt on mismatch). G2 closure note references "L5-verified manifest used." PHASE 5 R1 header includes roles "with verbatim expertise.relevance quotes."

#### Essential — **60/60**

**C-01 evidence is strongest here**: role selection is not just documented with a reason but proven via verbatim field citation verified before execution. L5 makes the manifest a falsifiable selection artifact.

#### Recommended — **60/60**

**C-06 evidence is strongest here**: verbatim `expertise.relevance` quote in manifest entry proves selection was based on actual registry field intersection with artifact type.

#### Aspirational

| ID | Status | Evidence — V-05 specific |
|----|--------|--------------------------|
| C-25 | **PASS** | All 6 review matrix + all 3 synthesis schema columns carry NOT: exclusions |
| C-31 | **PASS** | "PHASE 3.5 -- SYNTHESIZE" header |
| C-32 | **PASS** | G2 OPEN/CLOSED + "AMEND does not begin" + L5-verified manifest referenced in G2 closure note |

All other aspirational criteria pass identically to V-04.

**V-05 total: 172.5/172.5** ✓ Golden

**V-05 structural difference**: Adds an end-to-end provenance chain for role selection: registry file → verbatim quote in manifest → L5 verification → G2 closure note confirms L5-verified manifest used. The selection claim is provable (falsifiable on quote mismatch) rather than just declared. This is the strongest structural evidence for C-01 and C-06 across all rounds.

---

### Summary Scorecard

| Variation | Axis | Essential | Recommended | Aspirational | **Total** | All Essential | Golden |
|-----------|------|-----------|-------------|--------------|-----------|---------------|--------|
| V-01 | Lifecycle (direct) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES | YES |
| V-02 | Output format (synthesis schema) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES | YES |
| V-03 | Inertia framing | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES | YES |
| V-04 | Two-axis (lifecycle + format) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES | YES |
| V-05 | Three-axis (+ verbatim + L5) | 60/60 | 60/60 | 52.5/52.5 | **172.5** | YES | YES |

All five variations achieve the maximum score. R11 design target met.

---

### Ranking (tie resolution by structural depth)

1. **V-05** — strongest: typed synthesis schema + triple-location enforcement + verbatim L5 provenance chain; falsifiable selection contract; richest structural coverage
2. **V-04** — typed synthesis schema + triple-location enforcement; cleanest dual-schema + triple-enforcement design
3. **V-03** — inertia framing with semantic G2 condition 1; inertia competitor propagated to manifest + header + synthesis; deepest challenger-synthesis integration
4. **V-02** — typed synthesis schema parallel; G2 structural completeness check; introduces Pattern 7
5. **V-01** — minimal, clean; every subsequent variation builds on it

---

### Excellence Signals (confirmed from V-05 as top variation)

**Signal 1 — G2 downstream target correction** (all variations, design-critical)
V-03 R10 blocked PHASE 4 with G2 — the wrong downstream target. C-32 mirrors C-17 exactly: G1 blocks domain review (PHASE 3); G2 must block AMEND (the post-render command interface). R11 corrects all five. This was a constraint satisfaction error, not a missing feature.

**Signal 2 — Typed synthesis schema parallel to review matrix** (V-02, V-04, V-05)
Applying C-13's typed-column discipline to synthesis output (3-column: Slot | Verdict Type | Statement) creates a second typed output schema. G2 closure becomes a structural table-completeness check (row count = slot count) rather than a prose verification. C-33 candidate: typed schema discipline applied to every phase output that produces a structured artifact, not just the review matrix.

**Signal 3 — Inertia node as required synthesis anchor** (V-03)
Slot 1's synthesis verdict must explicitly name its relationship to at least one domain slot's finding — not just receive "unique" passively. This converts the challenger bracket from a first-phase reviewer to a synthesis reference point. C-33 candidate: synthesis verdict for Slot 1 (challenger) must name inertia implications for domain findings, not generic signal assignment.

**Signal 4 — Triple-location synthesis enforcement** (V-04, V-05)
Three independent enforcement paths for the synthesis obligation: (1) AMEND output contract in schema section, (2) PHASE 3.5 G2 predicate, (3) synthesis table completeness check at G2 closure. No execution path reaches AMEND without encountering the synthesis obligation. Structural pattern: exhaustive enforcement path coverage applied to phase-boundary contracts.

**Signal 5 — Verbatim field citation provenance chain** (V-05)
Selection evidence chain: registry file → verbatim `expertise.relevance` quote in manifest → L5 character-for-character verification → G2 closure note confirms L5-verified manifest used. Role selection is falsifiable (halt on quote mismatch), not just declared. Strongest possible C-01/C-06 evidence form.

---

### C-33 Candidates

| Candidate | Evidence base | Chain |
|-----------|---------------|-------|
| Typed schema discipline applied to every structured phase output | V-02/V-04/V-05 synthesis schema; parallel to C-30 extending C-13 to criterion-check table | C-30 → C-33 |
| Slot 1 synthesis verdict must name inertia-domain relationship (semantic gate condition) | V-03 G2 condition 1 | C-32 → C-33 |

---

```json
{"top_score": 172.5, "all_essential_pass": true, "new_patterns": ["typed synthesis schema parallel to review matrix: schema discipline applied to every structured phase output that produces a typed artifact, not just the review matrix -- C-33 candidate extending C-30", "Slot 1 inertia as required synthesis anchor: G2 closure condition 1 requires challenger verdict to name its relationship to domain findings, not just receive a slot assignment -- C-33 candidate extending C-32"]}
```
