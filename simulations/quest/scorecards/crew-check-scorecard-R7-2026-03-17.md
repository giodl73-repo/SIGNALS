## crew-check — Quest Score R7

### Scoring Summary

All five R7 variations hold the full v6 floor. The R7 design intent was explicit: close no existing gaps, extend into new review-architecture territory. Every variation passes C-01 through C-23.

---

### Per-Variation Scorecards

**Scoring key:** Each PASS = full points. PARTIAL = half. FAIL = 0.
Essential 12 pts | Recommended 10 pts | Aspirational 2 pts | Max = 120

---

#### V-01 — Inertia framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role source traceability | PASS | `.roles/` load gate, REVIEWER PRIORITY MANIFEST with role slots |
| C-02 | Review matrix structure | PASS | Schema `Role\|Finding\|Surface\|Severity\|IC-CHALLENGED\|Recommendation` |
| C-03 | Perspective fidelity | PASS | G4a lens anchor per role; challenger bracket opens and closes |
| C-04 | Depth mode compliance | PASS | `standard`/`deep` in REVIEWER PRIORITY MANIFEST |
| C-05 | Severity presence | PASS | Severity column required; G4c validates |
| C-06 | Finding specificity | PASS | G4b enforces named artifact surface; HALT on missing |
| C-07 | Recommendation actionability | PASS | G4d enforces location reference in every recommendation |
| C-08 | Severity calibration consistency | PASS | PRE-EXECUTION SEVERITY CALIBRATION CONTRACT locked before gates |
| C-09 | Cross-role synthesis | PASS | Gate 9: >= 1 convergence/conflict, names IC-CHALLENGED=none findings |
| C-10 | AMEND responsiveness | PASS | Full AMEND block: add, depth, rerun, reload, halts, rerun:challenger |
| C-11 | Lens-anchoring step | PASS | G4a per-role lens anchor before any finding |
| C-12 | Severity calibration contract | PASS | Pre-committed table with H/M/L scores and operational meanings |
| C-13 | Challenger-first sequencing | PASS | REVIEWER PRIORITY MANIFEST: Challenger at slot 1 (fixed) and last (fixed) |
| C-14 | Readiness-gate framing | PASS | Gate 7 emits `READINESS: READY\|CONDITIONAL\|BLOCKED`; IC STANDING blocks directly |
| C-15 | Severity-sorted matrix output | PASS | Gate 5: sort descending by severity score; challenger rows within tier |
| C-16 | Hard-halt execution gate | PASS | G1, G3a, G4a-G4d all BLOCKING; full stop stated |
| C-17 | Named halt identifier system | PASS | G1, G3a, G4a-{role}, G4b-{role}, G4c-{role}, G4d-{role}, G4e-{role}, G5 |
| C-18 | AMEND gate-audit sub-command | PASS | `--amend halts` and `--amend halts:{gate-id}` |
| C-19 | Self-routing halt messages | PASS | Every halt embeds `→ To continue: /crew-check {{artifact}} --amend ...` |
| C-20 | Executable audit output | PASS | HALT AUDIT: each row is paste-ready with Re-entry command column |
| C-21 | Run health certificate | PASS | RUN HEALTH section after Gate 9 on every run; clean + failed headings both specified |
| C-22 | Three-tier halt scope | PASS | BLOCKING / SCOPED (G4e) / DEFERRED — registry has Tier column; tier semantics defined |
| C-23 | Pre-committed skip-map | PASS | PRE-EXECUTION SUB-GATE SKIP-MAP: resumes-at, skips, safe-skip prerequisite columns |

**V-01 composite: 120 / 120 — GOLD**

---

#### V-02 — Output format (confidence tier + convergence register)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role source traceability | PASS | `.roles/` G1 gate, REVIEWER PRIORITY MANIFEST |
| C-02 | Review matrix structure | PASS | Schema `Role\|Finding\|Surface\|Severity\|Confidence\|Recommendation` |
| C-03 | Perspective fidelity | PASS | G4a lens anchor, challenger bracket |
| C-04 | Depth mode compliance | PASS | standard/deep referenced |
| C-05 | Severity presence | PASS | Severity column; G4c validates |
| C-06 | Finding specificity | PASS | G4b named surface enforced |
| C-07 | Recommendation actionability | PASS | G4d location reference enforced |
| C-08 | Severity calibration consistency | PASS | Extended calibration contract: severity scale + confidence scale both pre-committed |
| C-09 | Cross-role synthesis | PASS | Gate 9: names CORROBORATED/CONFIRMED convergences; names Confidence=LOW findings for verification |
| C-10 | AMEND responsiveness | PASS | Full AMEND block including G4f/G4g sub-gate re-entry |
| C-11 | Lens-anchoring step | PASS | G4a per-role |
| C-12 | Severity calibration contract | PASS | Pre-committed severity table (plus confidence table — extends the pattern) |
| C-13 | Challenger-first sequencing | PASS | Challenger bracket |
| C-14 | Readiness-gate framing | PASS | Gate 7; CONFIRMED surfaces treated as HIGH-effective |
| C-15 | Severity-sorted matrix output | PASS | Sort severity DESC, confidence DESC within tier |
| C-16 | Hard-halt execution gate | PASS | G4c, G4f BLOCKING |
| C-17 | Named halt identifier system | PASS | Adds G4f-{role} (invalid confidence) and G4g-{role} (absent confidence) |
| C-18 | AMEND gate-audit sub-command | PASS | `--amend halts` with paste-ready HALT AUDIT |
| C-19 | Self-routing halt messages | PASS | All halts embed recovery commands with skip-map annotations |
| C-20 | Executable audit output | PASS | HALT AUDIT rows are paste-ready with Re-entry command column |
| C-21 | Run health certificate | PASS | RUN HEALTH always emitted; clean run notes "Confidence and convergence contracts honored" |
| C-22 | Three-tier halt scope | PASS | G4g is DEFERRED; BLOCKING halts present; tier semantics defined |
| C-23 | Pre-committed skip-map | PASS | PRE-EXECUTION SUB-GATE SKIP-MAP extends to G4f and G4g |

**V-02 composite: 120 / 120 — GOLD**

---

#### V-03 — Lifecycle emphasis (artifact maturity stage contract)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role source traceability | PASS | `.roles/` G1 gate |
| C-02 | Review matrix structure | PASS | Schema `Role\|Finding\|Surface\|Severity\|STAGE-APPROPRIATE\|Recommendation` |
| C-03 | Perspective fidelity | PASS | G4a lens anchor; challenger notes stage-relevant inertia strengths |
| C-04 | Depth mode compliance | PASS | standard/deep referenced |
| C-05 | Severity presence | PASS | Severity column; G4c validates |
| C-06 | Finding specificity | PASS | G4b named surface enforced |
| C-07 | Recommendation actionability | PASS | G4d location reference enforced |
| C-08 | Severity calibration consistency | PASS | Severity calibration contract locked before gates |
| C-09 | Cross-role synthesis | PASS | Gate 9: names in-scope convergences; notes ADVISORY findings with cross-role corroboration |
| C-10 | AMEND responsiveness | PASS | Adds `--amend stage:{value}` for stage change; full sub-gate re-entry through G4h |
| C-11 | Lens-anchoring step | PASS | G4a per-role |
| C-12 | Severity calibration contract | PASS | Pre-committed severity table |
| C-13 | Challenger-first sequencing | PASS | Challenger bracket; stage context feeds opening pass |
| C-14 | Readiness-gate framing | PASS | Gate 7 reads only YES-scope rows; DEPRECATED always READY |
| C-15 | Severity-sorted matrix output | PASS | Sort severity DESC within YES/ADVISORY/NO scope grouping |
| C-16 | Hard-halt execution gate | PASS | G0.5 (stage missing) BLOCKING; G1, G4a-G4d BLOCKING |
| C-17 | Named halt identifier system | PASS | Adds G0.5 (pre-registry) and G4h-{role} (STAGE-APPROPRIATE column) |
| C-18 | AMEND gate-audit sub-command | PASS | `--amend halts` with paste-ready HALT AUDIT |
| C-19 | Self-routing halt messages | PASS | All halts embed recovery commands |
| C-20 | Executable audit output | PASS | HALT AUDIT rows paste-ready |
| C-21 | Run health certificate | PASS | RUN HEALTH after Gate 9; clean run includes Stage field and Excluded rows count |
| C-22 | Three-tier halt scope | PASS | G4h DEFERRED; G0.5/G1/G4a-G4d BLOCKING; tier semantics defined |
| C-23 | Pre-committed skip-map | PASS | PRE-EXECUTION SUB-GATE SKIP-MAP extends to G4h |

**V-03 composite: 120 / 120 — GOLD**

---

#### V-04 — Inertia framing + output format (V-01 × V-02)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role source traceability | PASS | `.roles/` G1 gate |
| C-02 | Review matrix structure | PASS | Schema `Role\|Finding\|Surface\|Severity\|Confidence\|IC-CHALLENGED\|Recommendation` — both new columns coexist |
| C-03 | Perspective fidelity | PASS | G4a lens anchor; challenger registers IC claims |
| C-04 | Depth mode compliance | PASS | standard/deep referenced |
| C-05 | Severity presence | PASS | Severity column; G4c validates |
| C-06 | Finding specificity | PASS | G4b named surface enforced |
| C-07 | Recommendation actionability | PASS | G4d location reference enforced |
| C-08 | Severity calibration consistency | PASS | Both severity and confidence contracts pre-committed |
| C-09 | Cross-role synthesis | PASS | Gate 9: names CONFIRMED-OVERCOME ICs; names STANDING ICs with Confidence=LOW challenges (scope gap signal) |
| C-10 | AMEND responsiveness | PASS | Full AMEND block: add, depth, reload, halts, rerun, rerun:challenger, G4a–G4g sub-gate |
| C-11 | Lens-anchoring step | PASS | G4a per-role |
| C-12 | Severity calibration contract | PASS | Both calibration contracts locked before gates |
| C-13 | Challenger-first sequencing | PASS | Challenger bracket; IC registry locked before domain review |
| C-14 | Readiness-gate framing | PASS | Gate 7 integrates STANDING IC BLOCKED + CONFIRMED surface HIGH-effective |
| C-15 | Severity-sorted matrix output | PASS | Severity DESC, confidence DESC within tier |
| C-16 | Hard-halt execution gate | PASS | G1, G3a, G4a-G4d, G4f BLOCKING |
| C-17 | Named halt identifier system | PASS | Full halt ID set: G1, G3a, G4a-G4g across all tier types |
| C-18 | AMEND gate-audit sub-command | PASS | `--amend halts` with paste-ready HALT AUDIT |
| C-19 | Self-routing halt messages | PASS | Compact halt message form: `HALT [G4x-{role}]: [trigger]. → To continue: ... (skip-map: ... skipped — [prereq])` |
| C-20 | Executable audit output | PASS | HALT AUDIT rows paste-ready with Re-entry command |
| C-21 | Run health certificate | PASS | RUN HEALTH on every run; clean run adds "ICs OVERCOME by convergence: [N]" |
| C-22 | Three-tier halt scope | PASS | BLOCKING / SCOPED (G4e) / DEFERRED (G4g) all present in HALT REGISTRY |
| C-23 | Pre-committed skip-map | PASS | SUB-GATE SKIP-MAP extends to G4g; parallel-gate note for G4e/G4f |

**V-04 composite: 120 / 120 — GOLD**

---

#### V-05 — Inertia framing + lifecycle emphasis (V-01 × V-03)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role source traceability | PASS | `.roles/` G1 gate |
| C-02 | Review matrix structure | PASS | Schema `Role\|Finding\|Surface\|Severity\|STAGE-APPROPRIATE\|IC-CHALLENGED\|Recommendation` — both new columns coexist |
| C-03 | Perspective fidelity | PASS | G4a lens anchor; challenger notes stage-relevant IC weights |
| C-04 | Depth mode compliance | PASS | standard/deep referenced |
| C-05 | Severity presence | PASS | Severity column; G4c validates |
| C-06 | Finding specificity | PASS | G4b named surface enforced |
| C-07 | Recommendation actionability | PASS | G4d location reference enforced |
| C-08 | Severity calibration consistency | PASS | Severity calibration contract locked before gates |
| C-09 | Cross-role synthesis | PASS | Gate 9: names STANDING-GENUINE ICs and roles that didn't challenge them; names STANDING-SCOPED ICs with next-stage transition note |
| C-10 | AMEND responsiveness | PASS | AMEND includes `stage:{value}` and `rerun:challenger` alongside full sub-gate coverage |
| C-11 | Lens-anchoring step | PASS | G4a per-role |
| C-12 | Severity calibration contract | PASS | Severity contract locked; ARTIFACT MATURITY STAGE CONTRACT extends scope calibration |
| C-13 | Challenger-first sequencing | PASS | Challenger bracket; stage context explicitly informs IC priority in opening pass |
| C-14 | Readiness-gate framing | PASS | Gate 7: STANDING-GENUINE blocks; STANDING-SCOPED advisory; readiness verdict includes scoped IC appendix |
| C-15 | Severity-sorted matrix output | PASS | Sort severity DESC; YES-scope before ADVISORY before NO-scope within tier |
| C-16 | Hard-halt execution gate | PASS | G0.5 (stage missing) BLOCKING; G1, G3a, G4a-G4d BLOCKING |
| C-17 | Named halt identifier system | PASS | Full halt ID set: G0.5, G1, G3a, G4a-G4e (SCOPED), G4h (DEFERRED), G5 |
| C-18 | AMEND gate-audit sub-command | PASS | `--amend halts` with paste-ready HALT AUDIT showing both SCOPED and DEFERRED entries |
| C-19 | Self-routing halt messages | PASS | All halts embed recovery commands with tier notes |
| C-20 | Executable audit output | PASS | HALT AUDIT rows paste-ready |
| C-21 | Run health certificate | PASS | RUN HEALTH on every run; clean run includes Stage, STANDING-GENUINE/SCOPED IC counts |
| C-22 | Three-tier halt scope | PASS | BLOCKING / SCOPED (G4e) / DEFERRED (G4h) all in HALT REGISTRY |
| C-23 | Pre-committed skip-map | PASS | SUB-GATE SKIP-MAP extends to G4e and G4h with parallel-gate prerequisite note |

**V-05 composite: 120 / 120 — GOLD**

---

### Ranking

| Rank | Variation | Score | New structural layers |
|------|-----------|-------|-----------------------|
| 1 | **V-04** | 120/120 | IC-CHALLENGED + Confidence + FINDING CONVERGENCE AND IC-RESOLUTION CONTRACT; CONFIRMED convergence unconditionally overrides IC Status — eliminates editorial judgement in IC resolution entirely |
| 2 | **V-05** | 120/120 | IC-CHALLENGED + STAGE-APPROPRIATE + STAGE-SCOPED IC RESOLUTION CONTRACT; STANDING-GENUINE vs STANDING-SCOPED distinction — deepest semantic refinement of IC status |
| 3 | **V-01** | 120/120 | IC-CHALLENGED + CHALLENGE RESPONSE MAP + Gate 4.5 — foundational inertia accountability layer |
| 4 | **V-02** | 120/120 | Confidence tier + FINDING CONVERGENCE REGISTER — foundational epistemic calibration layer |
| 5 | **V-03** | 120/120 | ARTIFACT MATURITY STAGE CONTRACT + STAGE-APPROPRIATE — foundational lifecycle scope layer |

V-04 ranks first because it introduces the most mechanically decisive new capability: when 3+ roles cite the same surface (CONFIRMED), the IC citing that surface is OVERCOME unconditionally — the review produces a definitive answer rather than a recommendation. V-05 is a near-peer: the STANDING-GENUINE / STANDING-SCOPED distinction is the deepest semantic extension in R7, distinguishing "no evidence exists" from "evidence exists outside the current scope."

---

### Excellence Signals from V-04

**Signal 1 — Cross-dimensional mechanical resolution (FINDING CONVERGENCE AND IC-RESOLUTION CONTRACT):**
Convergence evidence (cross-role agreement) overrides severity-based IC Status derivation when 3+ roles agree on a surface citing an IC. This is the pattern: two calibration systems (inertia accountability and cross-role agreement) are composed at Gate 4.5 so their intersection — CONFIRMED-OVERCOME — requires no editorial decision. The CHALLENGE RESPONSE MAP gains a "Convergence Override" column that makes the resolution path explicit and auditable.

**Signal 2 — Dual-column finding accountability:**
A single finding row now carries both IC-CHALLENGED (inertia accountability) and Confidence (epistemic calibration). The matrix becomes a multi-dimensional prioritization instrument: HIGH severity / HIGH confidence / IC-CHALLENGED=IC-01 is a different object than HIGH severity / LOW confidence / IC-CHALLENGED=none. Gate 9 synthesis distinguishes them by name — CONFIRMED-OVERCOME ICs vs STANDING ICs with Confidence=LOW-only challenges (the latter signals a scope gap, not evidence absence).

**Signal 3 — STANDING IC scope-gap reading in synthesis:**
Gate 9 names ICs that are STANDING with only Confidence=LOW challenges. This is a structural reading: if reviewers saw the IC but only speculative challenges exist, the IC may be STANDING due to evidence weakness, not genuine status-quo strength. Prior synthesis named convergences; V-04 synthesis names evidential gaps embedded in IC status.

---

### New Patterns (R7 Candidates for C-24+)

Five new structural patterns emerged across R7:

| Pattern | Origin | Structural claim |
|---------|--------|-----------------|
| Pre-registered IC registry + IC-CHALLENGED column | V-01, V-04, V-05 | Challenger authority becomes mechanically auditable per finding row |
| Per-finding confidence tier as calibrated contract | V-02, V-04 | Separates severity (how bad if true) from confidence (how likely true); both pre-committed |
| Finding convergence register (CORROBORATED/CONFIRMED tags) | V-02, V-04 | Cross-role agreement made mechanical rather than editorial |
| CONFIRMED-convergence unconditional IC override | V-04 | Convergence evidence resolves inertia claims without editorial judgement |
| Artifact maturity stage contract with STANDING-GENUINE / STANDING-SCOPED IC resolution | V-03, V-05 | Review scope calibrated to lifecycle; distinguishes genuine IC absence from scope-excluded IC |

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Pre-registered inertia claim registry with IC-CHALLENGED column makes challenger authority mechanically auditable per finding row", "Per-finding confidence tier as independent calibrated contract separating severity (how bad if true) from confidence (how likely true)", "Finding convergence register with CORROBORATED/CONFIRMED cross-role agreement tags derived mechanically from surface overlap", "CONFIRMED-convergence unconditional IC override: when 3+ roles cite the same surface challenging an IC, that IC is OVERCOME without editorial judgement", "Artifact maturity stage contract with STANDING-GENUINE vs STANDING-SCOPED IC resolution distinguishing genuine inertia from scope-excluded inertia"]}
```
