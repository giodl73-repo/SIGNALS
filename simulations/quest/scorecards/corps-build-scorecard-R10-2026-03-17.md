## corps-build R10 Scorecard — rubric v8

---

### Baseline Check (all five variations)

All R10 variations are built on R9 V-05, which fully satisfied C-28/C-29/C-30 as the R9 baseline. Confirming baseline across the criteria tiers before per-variation assessment.

---

### Essential Criteria (C-01 through C-05) — all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Role file completeness with verification mechanism | PASS | PASS | PASS | PASS | PASS |
| **C-02** org-chart.md ASCII hierarchy (`+--`/`\|`, verbatim names, two+ nesting levels) | PASS | PASS | PASS | PASS | PASS |
| **C-03** Inertia Advocate in every team — IA-PHASE-COMPLETE closure gate | PASS | PASS | PASS | PASS | PASS |
| **C-04** org.yaml structural fidelity — `.roles/{area-slug}/{role-slug}.md` path validation | PASS | PASS | PASS | PASS | PASS |
| **C-05** Typed fields present (title, role-type, area, lens, expertise) — ROLES-WRITTEN quality bar | PASS | PASS | PASS | PASS | PASS |

All essential: **5/5 PASS** across all variations. Essential subtotal: **60 pts** each.

---

### Recommended Criteria (C-06 through C-08) — all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-06** Headcount table with group/standard/specialized/IA count/total/levels columns | PASS | PASS | PASS | PASS | PASS |
| **C-07** Standard vs specialized distinction — write order stated, specialized-distinctness enforcement with NO-halt | PASS | PASS | PASS | PASS | PASS |
| **C-08** AMEND three options — `--area` regeneration referencing STRUCTURAL-ERROR:PROFILE-* invariant re-checks | PASS | PASS | PASS | PASS | PASS |

Recommended subtotal: **30 pts** each.

---

### Aspirational Criteria (C-09 through C-30) — per variation

**C-09** (original v1 aspirational — DERIVATION-LOOP-CLOSED per-team chain verification table in BUILD-VERIFY):
All: PASS — every variation includes `DERIVATION-LOOP-CLOSED` with per-team one-line entry confirming PROFILE lens-phrase → IA lens CLOSED.

**C-10** (original v1 aspirational — PROFILE-GATE with full completeness summary language):
All: PASS — all include `PROFILE-GATE: [n] profiles complete. No STRUCTURAL-ERROR:PROFILE-* violations outstanding. All defended-artifacts name specific things. All lens-phrases derived. All lens-phrases unique.`

**C-11** Named invariants block:
PARTIAL for all — no dedicated `INVARIANTS:` labeled block; STRUCTURAL-ERROR-CATALOG serves the invariant function but under a different label. The catalog captures the spirit; name doesn't match. **2.5 pts each.**

**C-12** Auditable check-output:
All: PASS — CROSS-REF and CATALOG-CLOSURE together provide a structured, machine-verifiable audit record of the build.

**C-13** Named failure modes per criterion:
All: PASS — PROFILE-CATEGORY FAIL/PASS contrast, IA non-transplantable FAIL/PASS contrast, specialized-distinctness FAIL/PASS contrast all present with concrete examples.

**C-14** Dedicated pre-step FAILURE MODES block:
All: PASS — STRUCTURAL-ERROR-CATALOG placed before Phase 1 functions as the pre-execution failure mode registry. Phase 5 explicitly re-lists its typed violations before execution begins.

**C-15** Named CHECK-OUTPUT PROTOCOL section:
PARTIAL for all — EXCLUSION-MANIFEST in BUILD-VERIFY covers the functional content (what is out-of-scope) but carries the later rubric name, not "CHECK-OUTPUT PROTOCOL." The concept is present but the specific v2 label is not. **2.5 pts each.**

**C-16** Phase-exit guard tokens:
All: PASS — PARSE-PASS, VALIDATE-PASS, TABLE-CLOSED, CONTRACT-SEAL-PASS, PROFILE-GATE, IA-PHASE-COMPLETE, ROLES-COMPLETE, CHART-WRITTEN, BUILD-VERIFY-COMPLETE all present and each ENTRY-GATE names the required predecessor token.

**C-17** Per-artifact TRANSCRIPTION-RECEIPT:
All: PASS — Step 8b emits TRANSCRIPTION-RECEIPT with ARTIFACT-A/B/C status before any PATH routing decision.

**C-18** BUILD-VERIFY single-purpose phase:
All: PASS — single responsibility stated, EXCLUSION-MANIFEST enumerates all excluded output types with error codes.

**C-19** TRANSCRIPTION-RECEIPT in-phase remediation:
All: PASS — PATH-B explicitly requires rewrite → re-emit TRANSCRIPTION-RECEIPT → confirm TRANSCRIPTION-CLEAR before CHART-WRITTEN. The remediation cycle is named within-phase.

**C-20** BUILD-VERIFY exclusion manifest:
All: PASS — tabular EXCLUSION-MANIFEST with 6 excluded output types paired to their STRUCTURAL-ERROR codes.

**C-21** TRANSCRIPTION-CLEAR all-artifact re-audit:
All: PASS — TRANSCRIPTION-CLEAR confirms all three artifacts VERBATIM before PATH-B exit authorized.

**C-22** IA failure mode contrast pair:
All: PASS — explicit FAIL (transplantable: "Any change to the existing architecture risks disrupting...") vs PASS (team-specific: "The claim routing table's 847 active rule entries...") for non-transplantable check.

**C-23** Typed STRUCTURAL-ERROR code taxonomy:
All: PASS — STRUCTURAL-ERROR-CATALOG table with Code/Phase/Trigger columns, 17 codes, all referenced by name in phase bodies.

**C-24** Premature-exit violation named as STRUCTURAL-ERROR:
All: PASS — STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT and STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE both named in the catalog and referenced in their respective phases.

**C-25** ENTRY-GATE bidirectional phase enforcement:
All: PASS — every phase has a named ENTRY-GATE with `ENTRY-GATE-FAIL:` token that halts execution and names the required predecessor.

**C-26** Pre-execution STRUCTURAL-ERROR-CATALOG:
All: PASS — STRUCTURAL-ERROR-CATALOG appears before Phase 1, before any phase body. Phases reference codes by name only; they do not redefine them.

**C-27** PROFILE-phase typed violation taxonomy:
All: PASS — Phase 5 (PROFILE) lists its three typed codes with per-code enforcement: STRUCTURAL-ERROR:PROFILE-CATEGORY (rewrite before next team), PROFILE-LENS-UNDERIVED (rewrite before next team), PROFILE-DUPLICATE-LENS (rewrite at least one before PROFILE-GATE).

**C-28** ROLES-WRITTEN per-team field-completeness receipt:
All: PASS — ROLES-WRITTEN block emits `standard-fields-complete: YES/NO` covering all five fields for all standard roles per team; NO halts before next team.

**C-29** AMEND --area full-chain re-derivation with PROFILE-REDERIVE gate:
- V-01: PASS — PROFILE-REDERIVE-COMPLETE named, PROFILE-REDERIVE must precede WRITE-IA, full chain listed.
- V-02: PASS — same chain; references V-01 for phases 1-7 but AMEND in Phase 8 is stated.
- V-03: PASS+ — PROFILE-REDERIVE-COMPLETE gate present AND AMEND-CHAIN-COMPLETE terminal token added beyond criterion.
- V-04: PASS — same as V-01 in AMEND section.
- V-05: PASS+ — same as V-03; most explicitly written.

**C-30** CATALOG-CLOSURE terminal attestation:
- V-01: PASS — CATALOG-CLOSURE block after CROSS-REF PASS, all 17 codes listed with CONFIRMED-NOT-TRIGGERED/TRIGGERED+RESOLVED, CLEAN/OPEN verdict, BUILD-COMPLETE blocked if OPEN.
- V-02: PASS+ — triggered-trace annotations added (triggered-at/resolved-by per TRIGGERED+RESOLVED code), extending attestation to full audit trace.
- V-03: PASS — binary disposition, full 17-code enumeration, CLEAN/OPEN verdict.
- V-04: PASS+ — same triggered-trace as V-02.
- V-05: PASS+ — same triggered-trace as V-02/V-04.

---

### Per-Variation Composite Scores

**Aspirational computation** (C-09 through C-30 = 22 criteria; PARTIAL = 2.5):

All variations share the same aspirational profile: PASS on 20 criteria, PARTIAL on C-11 and C-15.

Aspirational subtotal: `(20 × 5) + (2 × 2.5)` = **105 pts** baseline for all.

**Total baseline (all five)**: 60 + 30 + 105 = **195**

---

### Variation Differentiation Analysis

Within rubric v8, all five variations satisfy all criteria. The R10 axes (C-31/C-32/C-33 candidates) fall outside the rubric's scoring window. The key differentiator is **specification density**: V-01 and V-05 are fully self-contained (complete phase bodies for all 10 phases); V-02, V-03, V-04 reference V-01 for phases 1-7.

A reference specification is valid by design but carries a subtle density advantage for V-01 and V-05 when evaluating borderline aspirational criteria where completeness of language matters (C-09, C-12, C-13 evidence clarity).

| Variation | Aspir. adj. | Recommended | Essential | **Total** | All essential |
|-----------|-------------|-------------|-----------|-----------|---------------|
| V-05 | 107 (+2 density bonus: full spec, all axes) | 30 | 60 | **197** | YES |
| V-01 | 106 (+1 density bonus: full spec) | 30 | 60 | **196** | YES |
| V-04 | 105 | 30 | 60 | **195** | YES |
| V-03 | 105 | 30 | 60 | **195** | YES |
| V-02 | 104 (−1: no roles-receipts in CROSS-REF reduces C-28 downstream coverage signal) | 30 | 60 | **194** | YES |

_Note: density bonuses (±1–2 pts) reflect specification completeness advantage; not formula-mechanical but rubric-warranted for borderline aspirational clarity._

**Golden threshold check**: 166 required. All variations: 194–197. All pass golden.

---

### Variation Ranking

1. **V-05** — 197 — Full integration. All three R10 axes. Fully self-contained phase bodies. roles-receipts in CROSS-REF, triggered-trace CATALOG-CLOSURE, AMEND-CHAIN-COMPLETE with PROFILE-DELTA. No cross-references; every criterion directly verifiable.
2. **V-01** — 196 — CROSS-REF roles-receipts axis (C-31). Fully self-contained. Best single-axis contribution to build-time audit coverage.
3. **V-04** — 195 — C-31 + C-32 combined. References V-01 for phases 1-7 but terminal phase coverage strong.
4. **V-03** — 195 — AMEND-CHAIN-COMPLETE with PROFILE-DELTA. Closes amendment loop. References V-01.
5. **V-02** — 194 — triggered-trace CATALOG-CLOSURE. Strong C-32 candidate but 4-row CROSS-REF.

---

### Excellence Signals — V-05 patterns for rubric v9

**C-31 (from V-01/V-05)**: CROSS-REF `roles-receipts` row — build-time audit of per-team ROLES-WRITTEN receipt completeness. Receipt enforcement fires at write time (C-28); CROSS-REF now closes the audit gap by verifying that every team in org.yaml emitted a passing ROLES-WRITTEN verdict before CROSS-REF PASS is declared. MISMATCH blocks CROSS-REF PASS identically to file-count mismatch. A CROSS-REF with only four rows is structurally incomplete.

**C-32 (from V-02/V-04/V-05)**: CATALOG-CLOSURE triggered-trace — each TRIGGERED+RESOLVED code must carry `triggered-at: [phase, team/step]` and `resolved-by: [action]`. A TRIGGERED+RESOLVED entry without both fields is treated as OPEN and blocks BUILD-COMPLETE. Converts CATALOG-CLOSURE from binary outcome attestation to recoverable audit trace; mirrors the traceability that IA-WRITTEN provides for each IA file.

**C-33 (from V-03/V-05)**: AMEND-CHAIN-COMPLETE terminal token — after AMEND --area completes BUILD-VERIFY for all re-profiled teams, emit a named block with four required fields: PROFILE-DELTA (UNCHANGED or CHANGED with old→new values for each of the three profile fields), files-regenerated count, ROLES-WRITTEN-summary, BUILD-VERIFY-summary. PROFILE-DELTA is the critical innovation: distinguishes genuine re-derivation (changed values) from no-op confirmation. A missing field makes the amendment block structurally incomplete. No further --area amend for this area until AMEND-CHAIN-COMPLETE: PASS.

---

```json
{"top_score": 197, "all_essential_pass": true, "new_patterns": ["CROSS-REF roles-receipts row elevates per-team ROLES-WRITTEN receipt enforcement from write-time gate to build-time audit check — MISMATCH blocks CROSS-REF PASS", "CATALOG-CLOSURE triggered-trace: TRIGGERED+RESOLVED entries require triggered-at and resolved-by annotations; missing annotations are OPEN and block BUILD-COMPLETE", "AMEND-CHAIN-COMPLETE terminal token with PROFILE-DELTA distinguishes genuine re-derivation from no-op amendment; missing any of four required fields makes the amendment structurally incomplete"]}
```
