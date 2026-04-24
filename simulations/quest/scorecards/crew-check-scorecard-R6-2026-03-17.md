## crew-check — Quest Score: Round 6

### Preamble

R6 explicitly targets all five variations at the full v5 floor (C-01 through C-20 in all), then deepens three axes as pre-committed preamble contracts. I'll score each variation fully, then surface excellence signals and new patterns.

---

## V-01 — Sub-gate skip-map as pre-committed preamble contract

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role source traceability | **PASS** | `.roles/` named by path; G1 halts if absent; no invented roles |
| C-02 | Review matrix structure | **PASS** | Gate 4 loop produces `\| Role \| Finding \| Artifact Surface \| Severity \| Recommendation \|` |
| C-03 | Perspective fidelity | **PASS** | G4a lens anchor required before any finding per role |
| C-04 | Depth mode compliance | **PASS** | `{{depth}}: [standard \| deep]`; `deep` = all roles, `standard` = relevant with rationale |
| C-05 | Severity presence | **PASS** | Calibration contract pre-committed; HIGH/MEDIUM/LOW with scores |
| C-06 | Finding specificity | **PASS** | G4b requires named artifact surface; HALT on missing |
| C-07 | Recommendation actionability | **PASS** | G4d requires location reference; HALT on missing |
| C-08 | Severity calibration consistency | **PASS** | Contract locked before any reviewer; G4c validates against it |
| C-09 | Cross-role synthesis | **PASS** | Gate 9: 2–4 sentences, ≥1 cross-role convergence/conflict |
| C-10 | AMEND responsiveness | **PASS** | AMEND block: add, depth, rerun, rerun:G4x-{role}, reload, halts, halts:{id} |
| C-11 | Lens-anchoring step | **PASS** | G4a explicit format + halt on missing |
| C-12 | Severity calibration contract | **PASS** | PRE-EXECUTION table locked before gates execute |
| C-13 | Challenger-first sequencing | **PASS** | Gate 3 (opening bracket) + Gate 8 (closing bracket), fixed slots |
| C-14 | Readiness-gate framing | **PASS** | Gate 7: HIGH→BLOCKED, MEDIUM→CONDITIONAL, LOW→READY; emits `READINESS:` |
| C-15 | Severity-sorted matrix output | **PASS** | Gate 5: sort by score 3→1; Challenger before domain within tier |
| C-16 | Hard-halt execution gate | **PASS** | "You are not ready to…" at G1 and G2; G5 blocks on zero findings |
| C-17 | Named halt identifier system | **PASS** | PRE-EXECUTION HALT REGISTRY: G1, G4a–G4d-{role}, G5; halt messages verbatim |
| C-18 | AMEND gate-audit sub-command | **PASS** | `halts` and `halts:{gate-id}` in AMEND; HALT AUDIT table |
| C-19 | Self-routing halt messages | **PASS** | Each halt embeds `→ To continue: /crew-check {{artifact}} --amend rerun:G4x-{role}` with skip-map annotation |
| C-20 | Executable audit output | **PASS** | HALT AUDIT Re-entry command column; "Each entry is paste-ready. …equivalent to consulting the skip-map manually" |

**Essential**: 5/5 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 12/12 PASS

**V-01 Score: 114 / 114**

---

## V-02 — Run health certificate — both directions

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role source traceability | **PASS** | `.roles/` named; G1 halt if absent |
| C-02 | Review matrix structure | **PASS** | Gate 4 loop; full matrix format specified |
| C-03 | Perspective fidelity | **PASS** | G4a lens anchor per role |
| C-04 | Depth mode compliance | **PASS** | `standard`/`deep` in REVIEWER PRIORITY MANIFEST |
| C-05 | Severity presence | **PASS** | Calibration contract pre-committed |
| C-06 | Finding specificity | **PASS** | G4b surface finding; HALT on missing |
| C-07 | Recommendation actionability | **PASS** | G4d location reference; HALT on missing |
| C-08 | Severity calibration consistency | **PASS** | Contract locked; G4c validates |
| C-09 | Cross-role synthesis | **PASS** | Gate 9 explicit |
| C-10 | AMEND responsiveness | **PASS** | AMEND block with operations |
| C-11 | Lens-anchoring step | **PASS** | G4a explicit |
| C-12 | Severity calibration contract | **PASS** | PRE-EXECUTION table |
| C-13 | Challenger-first sequencing | **PASS** | Gates 3 + 8 |
| C-14 | Readiness-gate framing | **PASS** | Gate 7 verdict |
| C-15 | Severity-sorted matrix output | **PASS** | Gate 5 severity sort |
| C-16 | Hard-halt execution gate | **PASS** | G1, G2 block conditions; G5 blocks on zero |
| C-17 | Named halt identifier system | **PASS** | PRE-EXECUTION HALT REGISTRY with named IDs |
| C-18 | AMEND gate-audit sub-command | **PASS** | `halts` and `halts:{gate-id}` in AMEND; HALT AUDIT table |
| C-19 | Self-routing halt messages | **PASS** | Each G4x halt: `→ To continue: /crew-check {{artifact}} --amend rerun:{role}` |
| C-20 | Executable audit output | **PASS** | HALT AUDIT with paste-ready Re-entry column; "Each entry is paste-ready" |

**Critical test (V-02)**: Does the RUN HEALTH section appear on clean runs? **YES** — Gate 10 emits `RUN HEALTH: PASS` with gate enumeration and zero-halt confirmation. Heading encodes run state: `RUN HEALTH: PASS` vs `RUN HEALTH: [N] HALT(S) FIRED`. No "absence" semantics — the section always appears.

**Essential**: 5/5 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 12/12 PASS

**V-02 Score: 114 / 114**

---

## V-03 — Three-tier halt scope: BLOCKING / SCOPED / DEFERRED

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role source traceability | **PASS** | `.roles/` referenced; G1 BLOCKING halt |
| C-02 | Review matrix structure | **PASS** | Matrix + EXCLUDED ROWS appendix for SCOPED halts |
| C-03 | Perspective fidelity | **PASS** | G4a lens anchor per role |
| C-04 | Depth mode compliance | **PASS** | `deep`/`standard` in REVIEWER PRIORITY MANIFEST |
| C-05 | Severity presence | **PASS** | Calibration contract pre-committed |
| C-06 | Finding specificity | **PASS** | G4b (SCOPED tier) surface finding |
| C-07 | Recommendation actionability | **PASS** | G4d (DEFERRED tier) location reference |
| C-08 | Severity calibration consistency | **PASS** | Contract locked; G4c SCOPED validates |
| C-09 | Cross-role synthesis | **PASS** | Gate 9 with note for excluded row gaps |
| C-10 | AMEND responsiveness | **PASS** | AMEND with `halts` (tier-separated) |
| C-11 | Lens-anchoring step | **PASS** | G4a [BLOCKING] explicit |
| C-12 | Severity calibration contract | **PASS** | PRE-EXECUTION table |
| C-13 | Challenger-first sequencing | **PASS** | Gates 3 + 8 |
| C-14 | Readiness-gate framing | **PASS** | Gate 7 with DEFERRED forcing CONDITIONAL |
| C-15 | Severity-sorted matrix output | **PASS** | Gate 5 sort; DEFERRED rows included with tag |
| C-16 | Hard-halt execution gate | **PASS** | BLOCKING tier = run-level full stop; explicit "Run cannot continue" |
| C-17 | Named halt identifier system | **PASS** | HALT REGISTRY with tier column; G1, G4a–G4d, G5 |
| C-18 | AMEND gate-audit sub-command | **PASS** | `halts` with tier-separated HALT AUDIT format |
| C-19 | Self-routing halt messages | **PASS** | G4b–G4d all embed `→ To resolve: /crew-check {{artifact}} --amend rerun:{role}` |
| C-20 | Executable audit output | **PASS** | Tier-separated HALT AUDIT; "Each entry is paste-ready" |

**Critical test (V-03)**: Does DEFERRED produce CONDITIONAL even when all findings are LOW? Gate 7 explicitly: "DEFERRED rows force CONDITIONAL regardless of their finding severity. A run with only LOW findings but one DEFERRED row is CONDITIONAL, not READY." **YES.**

**Essential**: 5/5 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 12/12 PASS

**V-03 Score: 114 / 114**

---

## V-04 — Skip-map + three-tier halts (axes 1 + 3 combined)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role source traceability | **PASS** | `.roles/`; G1 BLOCKING halt |
| C-02 | Review matrix structure | **PASS** | Matrix + EXCLUDED ROWS |
| C-03 | Perspective fidelity | **PASS** | G4a lens anchor |
| C-04 | Depth mode compliance | **PASS** | `deep`/`standard` in manifest |
| C-05 | Severity presence | **PASS** | Calibration contract pre-committed |
| C-06 | Finding specificity | **PASS** | G4b SCOPED |
| C-07 | Recommendation actionability | **PASS** | G4d DEFERRED |
| C-08 | Severity calibration consistency | **PASS** | Contract locked; G4c validates |
| C-09 | Cross-role synthesis | **PASS** | Gate 9 |
| C-10 | AMEND responsiveness | **PASS** | AMEND with `rerun:{role}` and `rerun:G4d-{role}` distinguished |
| C-11 | Lens-anchoring step | **PASS** | G4a BLOCKING |
| C-12 | Severity calibration contract | **PASS** | PRE-EXECUTION table |
| C-13 | Challenger-first sequencing | **PASS** | Gates 3 + 8 |
| C-14 | Readiness-gate framing | **PASS** | Gate 7 with DEFERRED forcing CONDITIONAL |
| C-15 | Severity-sorted matrix output | **PASS** | Gate 5; DEFERRED rows included |
| C-16 | Hard-halt execution gate | **PASS** | BLOCKING tier explicit; G5 BLOCKING |
| C-17 | Named halt identifier system | **PASS** | Unified HALT REGISTRY WITH TIER AND RE-ENTRY table |
| C-18 | AMEND gate-audit sub-command | **PASS** | `halts` and `halts:{gate-id}` with tier-separated HALT AUDIT |
| C-19 | Self-routing halt messages | **PASS** | Each halt: `→ To continue:` with tier explanation (`full role restart — skip-map does not apply`) |
| C-20 | Executable audit output | **PASS** | Tier-separated HALT AUDIT with paste-ready re-entry; "Tier column tells the user whether skip-map applies" |

**Critical test (V-04)**: Does the skip-map correctly distinguish SCOPED (no skip) from DEFERRED (G4d skip only)?

SUB-GATE SKIP-MAP table:
- SCOPED: `--amend rerun:{role}` → G4a, no skips — "Row state was discarded at halt time"
- DEFERRED: `--amend rerun:G4d-{role}` → G4d, skips G4a–G4c — "Lens + surface + severity verified; row in output"

Note in AMEND: "SCOPED halts cannot use sub-gate precision because the row state was discarded." **YES** — distinction is structural.

**Essential**: 5/5 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 12/12 PASS

**V-04 Score: 114 / 114**

---

## V-05 — Full R6 integration

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role source traceability | **PASS** | `.roles/`; G1 BLOCKING halt |
| C-02 | Review matrix structure | **PASS** | Matrix + EXCLUDED ROWS appendix |
| C-03 | Perspective fidelity | **PASS** | G4a BLOCKING per role |
| C-04 | Depth mode compliance | **PASS** | `deep`/`standard` in manifest |
| C-05 | Severity presence | **PASS** | Calibration contract pre-committed |
| C-06 | Finding specificity | **PASS** | G4b SCOPED |
| C-07 | Recommendation actionability | **PASS** | G4d DEFERRED |
| C-08 | Severity calibration consistency | **PASS** | Contract locked; G4c validates |
| C-09 | Cross-role synthesis | **PASS** | Gate 9 with excluded row gap note |
| C-10 | AMEND responsiveness | **PASS** | AMEND with full tier-differentiated operations |
| C-11 | Lens-anchoring step | **PASS** | G4a BLOCKING |
| C-12 | Severity calibration contract | **PASS** | PRE-EXECUTION table |
| C-13 | Challenger-first sequencing | **PASS** | Gates 3 + 8 |
| C-14 | Readiness-gate framing | **PASS** | Gate 7 with DEFERRED forcing CONDITIONAL |
| C-15 | Severity-sorted matrix output | **PASS** | Gate 5 sort; DEFERRED rows included with tag |
| C-16 | Hard-halt execution gate | **PASS** | BLOCKING tier stops run; G5 BLOCKING |
| C-17 | Named halt identifier system | **PASS** | PRE-EXECUTION HALT REGISTRY with tier column |
| C-18 | AMEND gate-audit sub-command | **PASS** | `halts` and `halts:{gate-id}`; HALT AUDIT mirrors RUN HEALTH format |
| C-19 | Self-routing halt messages | **PASS** | All G4x halt messages embed tier-annotated recovery commands |
| C-20 | Executable audit output | **PASS** | "Audit format is identical to the RUN HEALTH failure block" — triple-path consistency guarantee |

**Critical test (V-05)**: Are all three recovery paths identical in content and tier ordering?

Explicitly stated: "Audit format is identical to the RUN HEALTH failure block, ensuring any path to recovery (inline halt message, RUN HEALTH section, or `--amend halts` query) leads to the same tier-ordered, paste-ready command list." **YES.**

**Essential**: 5/5 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 12/12 PASS

**V-05 Score: 114 / 114**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Golden |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 60/60 | 30/30 | 24/24 | **114/114** | YES |
| V-02 | 60/60 | 30/30 | 24/24 | **114/114** | YES |
| V-03 | 60/60 | 30/30 | 24/24 | **114/114** | YES |
| V-04 | 60/60 | 30/30 | 24/24 | **114/114** | YES |
| V-05 | 60/60 | 30/30 | 24/24 | **114/114** | YES |

All five variations achieve 114/114. This is expected given the explicit design intent ("all hold the R5 v5 floor") and reflects that the rubric correctly captured R5's advances. R6 is generating above-rubric structural innovations.

---

## Excellence Signals

R6's defining advance is the move from **behavioral side-effects** to **pre-committed preamble contracts**. In R5, features like self-routing halt messages and executable audit output emerged incidentally or as named behaviors within gate prose. In R6, all structural behavior is pre-declared in named sections (HALT REGISTRY, SUB-GATE SKIP-MAP, RUN HEALTH CONTRACT) before any gate fires. The model holds the full failure-space map at preamble time.

**Top variation: V-05** — earns the full integration designation by satisfying the structural claim: all three recovery paths (inline halt message, RUN HEALTH section, `--amend halts`) produce identical tier-ordered, paste-ready content. This triple-path consistency is a genuinely new guarantee not present in any prior variation.

### New patterns present in 2+ variations

| Pattern | Variations | Structural claim |
|---------|-----------|-----------------|
| Pre-committed preamble contracts | V-01 through V-05 | All halt behavior, skip semantics, and/or run health declared as named sections before any gate executes; behavioral map is complete before any failure is encountered |
| Bi-directional run health section | V-02, V-05 | RUN HEALTH appears at a fixed position after Gate 9 in both clean and failed runs; section heading encodes run state (`RUN HEALTH: PASS` vs `RUN HEALTH: [N] HALT(S) FIRED`); no "absence" semantics required to read outcome |
| DEFERRED halt tier — conditional continuation | V-03, V-04, V-05 | Third tier: neither stops run nor excludes row; finding included with `[DEFERRED]` flag; forces CONDITIONAL verdict regardless of severity score; addresses the "useful but incomplete" case C-16 doesn't cover |
| Tier-gated skip-map applicability | V-04, V-05 | The question of whether sub-gate re-entry is safe is a property of halt tier, not of gate position; SCOPED row state was discarded (no skip safe); DEFERRED row state is preserved in output (skip safe); this is declared structurally before execution |

---

```json
{"top_score": 114, "all_essential_pass": true, "new_patterns": ["Pre-committed preamble contracts — halt registry, sub-gate skip-map, and run health contract declared as named sections before any gate fires; model holds complete failure-space map before encountering any failure", "Bi-directional run health section — RUN HEALTH appears at fixed output position on both clean and failed runs; section heading encodes run state; no absence-semantics required to read outcome", "DEFERRED halt tier — third tier that neither stops the run nor excludes the row; finding included with [DEFERRED] flag and forces CONDITIONAL verdict regardless of severity; covers useful-but-incomplete case beyond C-16 hard-halt", "Tier-gated skip-map applicability — whether sub-gate re-entry is safe is a structural property of halt tier declared in the preamble; SCOPED row state discarded (no skip safe); DEFERRED row state preserved in output (sub-gate re-entry safe)"]}
```
