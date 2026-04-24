Reading the scorecard carefully to extract the R8 excellence signals before writing the rubric.

The scorecard surfaces three patterns not captured in v7:

1. **V-02 C-25 evidence** — "4 tiers (CONFIRMED / CONFIRMED-LOW / CORROBORATED / SOLO); Gate 5.5 register emitted" — two separable innovations: a SOLO tier with explicit disposition, and a mid-run convergence snapshot gate.
2. **V-03 C-16 evidence** — "RUN HEALTH includes Stage field and YES/ADVISORY/NO counts" — stage-aware health certificate.

These become C-28, C-29, C-30.

---

## crew-check — Quest Rubric v8

### v7 → v8 — New criteria

**Three patterns extracted from R8 scorecard evidence:**

| ID | Name | Source |
|----|------|--------|
| C-28 | SOLO convergence tier and disposition protocol | V-02 (C-25 PASS evidence) |
| C-29 | Mid-run convergence snapshot gate | V-02 (C-25 PASS evidence) |
| C-30 | Stage-aware RUN HEALTH certificate | V-03 (C-16 PASS evidence) |

---

### What each new criterion covers

**C-28 — SOLO convergence tier and disposition protocol (2 pts)**
V-02 extends the convergence register (C-25) from ≥2 tiers to 4: CONFIRMED, CONFIRMED-LOW, CORROBORATED, and SOLO. SOLO names findings that surface in exactly one role review. SOLO findings receive mandatory disposition at Gate 9: escalate to deep review, dismiss with rationale, or flag as role-specific insight. Without a SOLO tier, single-role findings are silently absorbed into the synthesis or lost. C-25 covers whether convergence levels are operationally defined; C-28 covers whether non-converging findings have a named tier and a required disposition path.

*PASS*: Convergence register includes a SOLO tier with an operational definition (present in exactly one role); Gate 9 emits a SOLO FINDINGS table; each entry carries a disposition tag (ESCALATE / DISMISS:rationale / ROLE-SPECIFIC).
*FAIL*: SOLO findings folded into CORROBORATED or suppressed; no disposition requirement; convergence register omits single-role signals.

---

**C-29 — Mid-run convergence snapshot gate (2 pts)**
V-02 introduces Gate 5.5, which fires after all role reviews complete but before the synthesis gate (Gate 9). Gate 5.5 emits a working convergence register: counts of CONFIRMED / CONFIRMED-LOW / CORROBORATED / SOLO findings grouped by surface. The snapshot serves as an early-abort signal — if convergence density is below a threshold the skill can halt before synthesis rather than producing a synthesis with no cross-role signal. C-09 covers whether a synthesis gate exists; C-25 covers whether convergence levels are operationally defined; C-29 covers whether a mid-run convergence snapshot fires at a dedicated gate before synthesis, with counts by tier and surface.

*PASS*: A named mid-run gate (e.g., Gate 5.5) fires after last role review and before synthesis; emits convergence counts by tier and surface; halt path defined if convergence count is zero.
*FAIL*: Convergence assessed only at synthesis gate; no intermediate counts; early-abort not possible.

---

**C-30 — Stage-aware RUN HEALTH certificate (2 pts)**
V-03 extends the RUN HEALTH section (C-21) to include the declared artifact stage and a scope-distribution summary: counts of YES / ADVISORY / NO / DEPRECATED findings. The stage field makes the certificate forward-looking — a reviewer can see at a glance how many findings belong to the current stage versus future stages. The scope distribution enables stage-transition planning without re-reading the full matrix. C-21 covers whether a RUN HEALTH section exists with clean and failed variants; C-26 covers the stage pre-condition; C-30 covers whether the RUN HEALTH certificate includes the active stage and scope counts as structured fields.

*PASS*: RUN HEALTH section includes a Stage field (declared value, not a placeholder) and a SCOPE DISTRIBUTION table with YES / ADVISORY / NO / DEPRECATED counts; both fields present in clean and failed variants.
*FAIL*: Stage absent from RUN HEALTH; scope counts embedded in prose rather than structured table; fields only present in one variant (clean but not failed, or vice versa).

---

### Scoring mechanics

| | v6 | v7 | v8 |
|--|-----|-----|-----|
| Aspirational criteria | 15 | 19 | 22 |
| Aspirational pts | 30 | 38 | 44 |
| Total max | 120 | 128 | 134 |
| Golden threshold | unchanged | unchanged | all 5 essential PASS + composite >= 80 |

---

### Structural relationships

**C-28 extends C-25:** SOLO tier requires the convergence register to be in place. A variation earns C-25 for ≥2 operationally defined tiers; C-28 is earned only when the non-converging case is also named and dispositioned. A variation cannot earn C-28 without earning C-25.

**C-29 extends C-09 / C-25:** Mid-run snapshot requires a convergence taxonomy to count against. A variation can earn C-09 (synthesis exists, ≥1 cross-role signal) without C-25 or C-29. Earning C-29 presupposes C-25 (named tiers to count) and implies C-09 (synthesis follows the snapshot).

**C-30 extends C-21 / C-26:** Stage-aware RUN HEALTH is only coherent when stage was validated at run entry. A variation can earn C-21 without C-26 or C-30. Earning C-30 presupposes C-26 (stage declared and validated at G0.5) so the Stage field in RUN HEALTH is a resolved value, not an unknown.

**C-24 → C-25 dependency (unchanged from v7):** Confidence must be pre-committed (C-24) before convergence tiers that reference confidence level (C-25) are scoreable. C-28 and C-29 inherit this dependency through C-25.

**C-26 → C-27 dependency (unchanged from v7):** Stage-scoped matrix (C-27) presupposes stage is gated at entry (C-26). C-30 adds a third node in this chain: C-26 → C-27 → C-30.

---

### Full criterion table

| ID | Tier | Pts | Name | Distinguishing scope |
|----|------|-----|------|---------------------|
| C-01 | Essential | 12 | Role source | Reads `.roles/`; G1 halts on absent registry |
| C-02 | Essential | 12 | Matrix structure | 6-column schema `Role·Finding·Surface·Severity·Confidence·Recommendation` |
| C-03 | Essential | 12 | Perspective fidelity | G4a lens anchor required before first finding per role |
| C-04 | Essential | 12 | Depth compliance | `deep`: all roles; `standard`: relevant with rationale; count stated |
| C-05 | Essential | 12 | Severity presence | Severity in every row; G4c BLOCKING on invalid value |
| C-06 | Recommended | 10 | Finding specificity | G4b BLOCKING on missing surface |
| C-07 | Recommended | 10 | Recommendation actionability | G4d BLOCKING on missing location reference |
| C-08 | Recommended | 10 | Severity calibration consistency | PRE-EXECUTION severity table; only HIGH/MEDIUM/LOW permitted |
| C-09 | Aspirational | 2 | Cross-role synthesis | Gate 9: ≥1 cross-role convergence; Confidence=LOW findings enumerated |
| C-10 | Aspirational | 2 | AMEND block | Full operations: add, depth, rerun, reload, halts |
| C-11 | Aspirational | 2 | Lens-anchoring | G4a explicit anchor before any finding |
| C-12 | Aspirational | 2 | Severity calibration contract | PRE-EXECUTION severity scale with scores and operational meanings |
| C-13 | Aspirational | 2 | Challenger-first | Fixed slot 1 + fixed slot N in REVIEWER PRIORITY MANIFEST |
| C-14 | Aspirational | 2 | Readiness gate | Gate 7: READY / CONDITIONAL / BLOCKED with 5 ordered rules |
| C-15 | Aspirational | 2 | Severity-sorted output | Sort: severity DESC, confidence DESC within tier |
| C-16 | Aspirational | 2 | Hard-halt gates | G1, G4a–G4g, G5 all BLOCKING |
| C-17 | Aspirational | 2 | Named halt IDs | G4c-{role}, G4f-{role}, G4g-{role}, etc. |
| C-18 | Aspirational | 2 | Gate-audit sub-command | `--amend halts` with formatted HALT AUDIT table |
| C-19 | Aspirational | 2 | Self-routing halts | Every halt emits `→ To continue: /crew-check ... --amend ...` |
| C-20 | Aspirational | 2 | Executable audit output | HALT AUDIT rows are paste-ready with re-entry commands |
| C-21 | Aspirational | 2 | Run health certificate | RUN HEALTH section after Gate 9; clean and failed variants |
| C-22 | Aspirational | 2 | Three-tier halt scope | Explicitly defines BLOCKING / SCOPED / DEFERRED with operational meanings |
| C-23 | Aspirational | 2 | Pre-committed skip-map | SUB-GATE SKIP-MAP table with resumes-at / skips / prerequisite columns |
| C-24 | Aspirational | 2 | Dual-axis calibration contract | Confidence scale pre-committed alongside severity; confidence drives sort, readiness, and convergence |
| C-25 | Aspirational | 2 | Named convergence tier register | ≥2 named convergence tiers with distinguishing criteria; Confidence=LOW findings flagged separately |
| C-26 | Aspirational | 2 | Artifact maturity stage pre-condition | G0.5 fires before G1; halts BLOCKING on absent/unrecognized stage; in HALT REGISTRY |
| C-27 | Aspirational | 2 | Stage-scoped matrix and readiness filter | STAGE-APPROPRIATE column (YES/ADVISORY/NO/DEPRECATED); scope-grouped matrix; Gate 7 reads YES only; DEPRECATED → automatic READY |
| C-28 | Aspirational | 2 | SOLO convergence tier and disposition protocol | Convergence register includes SOLO tier; Gate 9 emits SOLO FINDINGS table with per-entry disposition tag |
| C-29 | Aspirational | 2 | Mid-run convergence snapshot gate | Named mid-run gate fires after last role review, before synthesis; emits convergence counts by tier and surface; halt path on zero convergence |
| C-30 | Aspirational | 2 | Stage-aware RUN HEALTH certificate | RUN HEALTH includes Stage field and SCOPE DISTRIBUTION table (YES/ADVISORY/NO/DEPRECATED counts); present in both clean and failed variants |

**Total: 30 criteria · 134 pts max**
**Golden threshold: all 5 essential PASS + composite ≥ 80 (unchanged)**
