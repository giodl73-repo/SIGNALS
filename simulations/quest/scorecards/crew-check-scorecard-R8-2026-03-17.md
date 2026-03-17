## crew-check — Quest Scorecard R8 (Rubric v7)

### Scoring framework

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01–C-05 (5) | 12 | 60 |
| Recommended | C-06–C-08 (3) | 10 | 30 |
| Aspirational v6 | C-09–C-23 (15) | 2 | 30 |
| Aspirational v7 | C-24–C-27 (4) | 2 | 8 |
| **Total** | **27** | | **128** |

Golden threshold: all 5 essential PASS + composite >= 80.

---

### V-01 — Dual-axis calibration contract (C-24 only)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role source | PASS | Reads `.craft/roles/`; G1 halts on absent registry |
| C-02 | Matrix structure | PASS | 6-column schema `Role·Finding·Surface·Severity·Confidence·Recommendation` |
| C-03 | Perspective fidelity | PASS | G4a lens anchor required before first finding per role |
| C-04 | Depth compliance | PASS | `deep`: all roles; `standard`: relevant with rationale; count stated |
| C-05 | Severity presence | PASS | Severity in every row; G4c BLOCKING on invalid value |
| C-06 | Finding specificity | PASS | G4b BLOCKING on missing surface |
| C-07 | Recommendation actionability | PASS | G4d BLOCKING on missing location reference |
| C-08 | Severity calibration consistency | PASS | PRE-EXECUTION severity table; only HIGH/MEDIUM/LOW permitted |
| C-09 | Cross-role synthesis | PASS | Gate 9: >=1 cross-role convergence; Confidence=LOW findings enumerated |
| C-10 | AMEND block | PASS | Full operations: add, depth, rerun, reload, halts |
| C-11 | Lens-anchoring | PASS | G4a explicit anchor before any finding |
| C-12 | Severity calibration contract | PASS | PRE-EXECUTION severity scale with scores and operational meanings |
| C-13 | Challenger-first | PASS | Fixed slot 1 + fixed slot N in REVIEWER PRIORITY MANIFEST |
| C-14 | Readiness gate | PASS | Gate 7: READY / CONDITIONAL / BLOCKED with 5 ordered rules |
| C-15 | Severity-sorted output | PASS | Sort: severity DESC, confidence DESC within tier |
| C-16 | Hard-halt gates | PASS | G1, G4a–G4g, G5 all BLOCKING |
| C-17 | Named halt IDs | PASS | G4c-{role}, G4f-{role}, G4g-{role}, etc. |
| C-18 | Gate-audit sub-command | PASS | `--amend halts` with formatted HALT AUDIT table |
| C-19 | Self-routing halts | PASS | Every halt emits `→ To continue: /crew-check ... --amend ...` |
| C-20 | Executable audit output | PASS | HALT AUDIT rows are paste-ready with re-entry commands |
| C-21 | Run health certificate | PASS | RUN HEALTH section after Gate 9; clean and failed variants |
| C-22 | Three-tier halt scope | **PASS** | Explicitly defines BLOCKING / SCOPED / DEFERRED with operational meanings |
| C-23 | Pre-committed skip-map | PASS | SUB-GATE SKIP-MAP table with resumes-at / skips / prerequisite columns |
| C-24 | Dual-axis calibration contract | **PASS** | Confidence scale pre-committed with named tiers, operational meanings, sort spec; CONFIRMED (MEDIUM+HIGH) = HIGH-effective in Gate 7; G4f BLOCKING, G4g DEFERRED |
| C-25 | Named convergence tier register | **FAIL** | No FINDING CONVERGENCE REGISTER; no CORROBORATED/CONFIRMED-LOW labels; Gate 9 mentions Confidence=LOW but no formal tier table |
| C-26 | Artifact maturity stage pre-condition | **FAIL** | No `{{stage}}` input; no G0.5; no ARTIFACT MATURITY STAGE CONTRACT |
| C-27 | Stage-scoped matrix and readiness filter | **FAIL** | No STAGE-APPROPRIATE column; no scope-grouped matrix; no DEPRECATED value |

**V-01 composite: 122 / 128**
Essential PASS: 5/5 ✓ — Golden threshold met.

---

### V-02 — Named convergence tier register (C-24 + C-25)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | Essential + Recommended | **PASS ×8** | Same as V-01 |
| C-09 | Cross-role synthesis | PASS | Gate 9 names >=1 CONFIRMED or CORROBORATED surface; mandatory Confidence=LOW table emitted |
| C-10–C-12 | AMEND / lens / severity contract | **PASS ×3** | Same as V-01 |
| C-13 | Challenger-first | PASS | Fixed first + last slots |
| C-14–C-21 | Readiness through RUN HEALTH | **PASS ×8** | Same structural quality |
| C-22 | Three-tier halt scope | **PARTIAL** | BLOCKING and DEFERRED defined; SCOPED tier absent from HALT REGISTRY and not operationally named (no IC-CHALLENGED column in V-02) |
| C-23 | Pre-committed skip-map | PASS | SUB-GATE SKIP-MAP present |
| C-24 | Dual-axis calibration contract | **PASS** | Both scales pre-committed; confidence in matrix schema; sort spec; G4f/G4g; Gate 2 acknowledges both |
| C-25 | Named convergence tier register | **PASS** | PRE-EXECUTION FINDING CONVERGENCE CONTRACT with 4 tiers (CONFIRMED / CONFIRMED-LOW / CORROBORATED / SOLO); distinguishing criteria stated; Gate 5.5 register emitted; Confidence=LOW mandatory table at Gate 9 |
| C-26 | Artifact maturity stage pre-condition | **FAIL** | No `{{stage}}` input; no G0.5 |
| C-27 | Stage-scoped matrix and readiness filter | **FAIL** | No STAGE-APPROPRIATE column |

**V-02 composite: 123 / 128**
Essential PASS: 5/5 ✓ — Golden threshold met.

---

### V-03 — Stage pre-condition + stage-scoped matrix (C-26 + C-27)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | Essential + Recommended | **PASS ×8** | `{{stage}}` added as third input; role-loading, surfaces, severity all present |
| C-09 | Cross-role synthesis | PASS | Gate 9 names >=1 convergence on YES-scope findings; ADVISORY cross-role noted |
| C-10–C-12 | AMEND / lens / severity contract | **PASS ×3** | Severity contract present; AMEND has `stage:{value}` |
| C-13 | Challenger-first | PASS | Challenger brackets acknowledged; stage colors the inertia framing |
| C-14 | Readiness gate | PASS | Gate 7: DEPRECATED = automatic READY; non-DEPRECATED reads YES-scope only |
| C-15 | Severity-sorted output | PASS | Scope-grouped first, then severity DESC within group — severity order preserved |
| C-16–C-21 | Hard-halt through RUN HEALTH | **PASS ×6** | G0.5 adds to halt set; RUN HEALTH includes Stage field and YES/ADVISORY/NO counts |
| C-22 | Three-tier halt scope | **PARTIAL** | BLOCKING (G0.5, G1, G4a–G4d, G5) and DEFERRED (G4h) present; SCOPED tier absent |
| C-23 | Pre-committed skip-map | PASS | SUB-GATE SKIP-MAP updated for G4h |
| C-24 | Dual-axis calibration contract | **FAIL** | Confidence column absent; only severity calibration in PRE-EXECUTION; no G4f/G4g |
| C-25 | Named convergence tier register | **FAIL** | No convergence contract; no CONFIRMED/CORROBORATED labels |
| C-26 | Artifact maturity stage pre-condition | **PASS** | G0.5 first in HALT REGISTRY: "G0.5 fires before G1 — no other gate proceeds until stage is declared and recognized"; BLOCKING; explicit Gate 0.5 execution before Gate 1 |
| C-27 | Stage-scoped matrix and readiness filter | **PASS** | 4-value STAGE-APPROPRIATE (YES/ADVISORY/NO/DEPRECATED); scope-grouped matrix; Gate 7 reads YES only; DEPRECATED → automatic READY; `--amend stage:{value}` in AMEND |

**V-03 composite: 123 / 128**
Essential PASS: 5/5 ✓ — Golden threshold met.

---

### V-04 — Full dual-axis calibration + convergence register (C-24 + C-25)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | Essential + Recommended | **PASS ×8** | Same as V-01/V-02 |
| C-09 | Cross-role synthesis | PASS | Gate 9: named convergence surfaces; mandatory LOW table; CONFIRMED-LOW hypothetical change stated |
| C-10–C-21 | AMEND through RUN HEALTH | **PASS ×12** | Same structural quality; RUN HEALTH enumerates CONFIRMED, CONFIRMED-LOW, CORROBORATED counts |
| C-22 | Three-tier halt scope | **PARTIAL** | BLOCKING and DEFERRED in HALT REGISTRY; no SCOPED tier (no IC-CHALLENGED column) |
| C-23 | Pre-committed skip-map | PASS | SUB-GATE SKIP-MAP through G4g |
| C-24 | Dual-axis calibration contract | **PASS** | Both scales pre-committed; confidence in matrix schema; dual-axis sort; G4f/G4g; CONFIRMED readiness rule stated |
| C-25 | Named convergence tier register | **PASS** | 4-tier contract with formal distinguishing criteria; Gate 5.5 register uses `Roles (Severity/Confidence)` format; Confidence=LOW mandatory table in Gate 9 explicitly asks whether CONFIRMED-LOW would change verdict if elevated |
| C-26 | Artifact maturity stage pre-condition | **FAIL** | No `{{stage}}`; no G0.5 |
| C-27 | Stage-scoped matrix and readiness filter | **FAIL** | No STAGE-APPROPRIATE column |

**V-04 composite: 123 / 128**
Essential PASS: 5/5 ✓ — Golden threshold met.

*V-04 and V-02 score identically on rubric criteria but V-04 integrates C-24 and C-25 more tightly: convergence register columns show Severity/Confidence pairs, and Gate 8 explicitly reasons about CONFIRMED-LOW uplift scenarios. Both score PASS on C-25.*

---

### V-05 — Full integration (C-24 + C-25 + C-26 + C-27 + IC-CHALLENGED)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | Essential + Recommended | **PASS ×8** | `{{stage}}` added; all structural gates present; 8-column schema |
| C-09 | Cross-role synthesis | PASS | Gate 9: named CONFIRMED/CORROBORATED surfaces; 6-column Confidence=LOW table (adds IC-CHALLENGED and STAGE-APPROPRIATE); CONFIRMED-LOW IC-status change hypothetical |
| C-10–C-21 | AMEND through RUN HEALTH | **PASS ×12** | AMEND adds `stage:{value}` and `rerun:challenger`; RUN HEALTH reports 4 contract dimensions |
| C-22 | Three-tier halt scope | **PASS** | G4e is SCOPED ("SCOPED — EXCLUDED ROLES appendix will be appended"); G4g/G4h DEFERRED; all others BLOCKING; all three tiers operationally defined by usage |
| C-23 | Pre-committed skip-map | PASS | 9-row skip-map through G4h with G4e slot |
| C-24 | Dual-axis calibration contract | **PASS** | Confidence scale pre-committed; in 8-column matrix; sort is scope-grouped then severity DESC, confidence DESC within group; CONFIRMED (YES-scope non-LOW) = HIGH-effective in Gate 7; G4f BLOCKING, G4g DEFERRED |
| C-25 | Named convergence tier register | **PASS** | 4-tier contract scoped to YES rows only; Gate 5.5 includes `IC Impact` column in convergence register; CONFIRMED findings that challenge ICs yield OVERCOME-CONFIRMED; Confidence=LOW table at Gate 9 carries all 4 dimensions |
| C-26 | Artifact maturity stage pre-condition | **PASS** | G0.5 first in HALT REGISTRY with explicit ordering statement; BLOCKING; Gate 0.5 executes before Gate 1; `--amend stage:{value}` provides re-entry |
| C-27 | Stage-scoped matrix and readiness filter | **PASS** | 4-value STAGE-APPROPRIATE with DEPRECATED; scope-grouped then dual-axis sorted within group; Gate 7 YES-scope only; DEPRECATED → READY unconditionally; `--amend stage:{value}` in AMEND |

**V-05 composite: 128 / 128**
Essential PASS: 5/5 ✓ — Golden threshold met.

---

### Rankings

| Rank | Variation | Composite | v7 criteria earned | All essential |
|------|-----------|-----------|-------------------|---------------|
| 1 | **V-05** | **128 / 128** | C-24, C-25, C-26, C-27 | ✓ |
| 2 | V-02 | 123 / 128 | C-24, C-25 | ✓ |
| 2 | V-03 | 123 / 128 | C-26, C-27 | ✓ |
| 2 | V-04 | 123 / 128 | C-24, C-25 | ✓ |
| 5 | V-01 | 122 / 128 | C-24 | ✓ |

V-05 is the sole 128. Its 5-point lead over V-02/V-03/V-04 comes from earning all four new v7 criteria simultaneously (8 pts vs 4 pts) and regaining C-22 PASS via the SCOPED tier (1 pt recovery). V-02 and V-04 are functionally equivalent on the rubric — V-04's tighter C-24/C-25 integration doesn't score differently under binary PASS/FAIL.

---

### Excellence signals — V-05

**1. YES-scope-only convergence register**
Gate 5.5 explicitly computes convergence "over YES-scope rows only." ADVISORY and NO rows do not contribute. This prevents a stage-excluded ADVISORY finding corroborated across two roles from generating a false CONFIRMED signal that could promote to HIGH-effective in Gate 7. V-02/V-04 compute convergence over all matrix rows without this filter.

**2. OVERCOME-CONFIRMED compound IC status**
When a CONFIRMED surface (same surface + matching confidence tier across 2+ roles) in YES scope challenges an inertia claim, the IC receives OVERCOME-CONFIRMED rather than plain OVERCOME. This is mechanically stronger: plain OVERCOME can come from a single HIGH-severity LOW-confidence finding; OVERCOME-CONFIRMED requires convergent direct evidence. The CHALLENGE RESPONSE MAP in Gate 4.5 records this distinction and Gate 8 reasons about it explicitly.

**3. Four pre-committed contracts as independent enforcement axes**
V-05 organizes PRE-EXECUTION into four separate named sections (severity+confidence calibration, stage contract, convergence contract, inertia claim registry), each enforced by dedicated gate IDs. No two enforcement paths share a gate: confidence failure fires G4f/G4g, stage failure fires G0.5/G4h, IC failure fires G3a/G4e. This means any single failure can be isolated and re-entered without re-running unrelated contracts. Earlier variations share enforcement scope across fewer named sections.

---

```json
{"top_score": 128, "all_essential_pass": true, "new_patterns": ["YES-scope-only convergence register prevents stage-excluded advisory findings from inflating CONFIRMED tier or contributing to HIGH-effective readiness promotion", "OVERCOME-CONFIRMED compound IC status when multi-role CONFIRMED surfaces challenge an inertia claim — mechanically stronger than single-role OVERCOME", "Four independent pre-committed enforcement axes (scope, severity, confidence, inertia) each with dedicated gate IDs, enabling isolated re-entry without cross-contract restart"]}
```
