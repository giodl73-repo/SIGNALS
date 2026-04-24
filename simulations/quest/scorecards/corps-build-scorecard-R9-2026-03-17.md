# corps-build R9 Scorecard — Rubric v7

## Variation Overview

| Variation | Axis | New catalog codes |
|-----------|------|-------------------|
| V-01 | ROLES-WRITTEN per-team receipt | +ROLES-COMPLETE-PREMATURE (17 total) |
| V-02 | AMEND PROFILE-REDERIVE | 16 total |
| V-03 | CATALOG-CLOSURE attestation | 16 total |
| V-04 | V-01 + V-02 | +ROLES-COMPLETE-PREMATURE (17 total) |
| V-05 | V-01 + V-02 + V-03 (full) | +ROLES-COMPLETE-PREMATURE (17 total) |

---

## V-01 — ROLES-WRITTEN per-team receipt

### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | CROSS-REF emits `org.yaml slots: [n], files written: [n] -- [MATCH\|MISMATCH]` + `table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n]`; literal gap detection before BUILD-COMPLETE |
| C-02 | PASS | Step 8a: `+--` / `\|` notation, all names verbatim from org.yaml, minimum two nesting levels required |
| C-03 | PASS | IA-WRITTEN four-check gate per team, non-transplantable enforcement halts build; IA-PHASE-COMPLETE before WRITE-ROLES |
| C-04 | PASS | Path pattern `.roles/{area-slug}/inertia-advocate.md`; VALIDATE checks area slug uniqueness across org before any files written |
| C-05 | PASS | Five fields specified with content bars; ROLES-WRITTEN adds per-team `standard-fields-complete: YES/NO` check on all five fields |

**Essential subtotal: 60/60**

### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | ARTIFACT-A: Area, Standard, Specialized, Inertia-Adv, Total, Levels columns; exec-office and shared rows explicit |
| C-07 | PASS | `role-type: standard/specialized` in frontmatter; sequence: standard → specialized per team; ROLES-WRITTEN enforces specialized-distinctness with NO-halts-build gate |
| C-08 | PASS | AMEND: `--area` (IA-WRITTEN + ROLES-WRITTEN re-run), `--levels`, `--restructure`; three named options present |

**Recommended subtotal: 30/30**

### Aspirational (5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | IA-WRITTEN `lens-team-specific (non-transplantable)` check; named contrast pair (transplantable vs. "claim routing table's 847 active rule entries") |
| C-10 | PASS | CROSS-REF emits literal `MATCH\|MISMATCH` format; table fidelity line; CROSS-REF: PASS\|FAIL |
| C-11 | PASS | STRUCTURAL-ERROR-CATALOG with distinct named codes + ENTRY-GATE tokens per phase gate; named block with distinct identifiers |
| C-12 | PASS | IA-WRITTEN, ROLES-WRITTEN, BUILD-VERIFY, CROSS-REF all emit literal parseable check strings |
| C-13 | PASS | PROFILE contrast pair, IA non-transplantable contrast, ROLES-WRITTEN specialized-distinctness contrast (generic scalar extension vs. schema negotiation contract ownership) |
| C-14 | PASS | PROFILE phase opens with typed violation codes block; BUILD-VERIFY EXCLUSION-MANIFEST; STRUCTURAL-ERROR-CATALOG pre-execution |
| C-15 | PASS | IA-WRITTEN, ROLES-WRITTEN, BUILD-VERIFY, CROSS-REF are named check-output protocol sections |
| C-16 | PASS | PARSE-PASS → VALIDATE-PASS → TABLE-CLOSED → CONTRACT-SEAL-PASS → PROFILE-GATE → IA-PHASE-COMPLETE → ROLES-COMPLETE → CHART-WRITTEN → BUILD-VERIFY-COMPLETE; 9 phase-exit tokens |
| C-17 | PASS | TRANSCRIPTION-RECEIPT with per-artifact VERBATIM\|REVISED verdicts for all three artifacts |
| C-18 | PASS | "exactly one responsibility" stated; EXCLUSION-MANIFEST table with 6 BV-* codes |
| C-19 | PASS | PATH-B: rewrite deviant artifact → re-emit TRANSCRIPTION-RECEIPT → all VERBATIM → TRANSCRIPTION-CLEAR |
| C-20 | PASS | EXCLUSION-MANIFEST: file writes, count checks, dir audits, headcount, AMEND, summary — all coded |
| C-21 | PASS | TRANSCRIPTION-CLEAR names all three artifacts; fewer-than-three is structurally incomplete |
| C-22 | PASS | IA non-transplantable contrast pair with FAIL (transplantable phrase) vs PASS (team-specific vocabulary) |
| C-23 | PASS | 17-code STRUCTURAL-ERROR-CATALOG with Code, Phase, Trigger columns; typed taxonomy |
| C-24 | PASS | STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT + STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE both present |
| C-25 | PASS | Every phase has `ENTRY-GATE: X required. If not present: ENTRY-GATE-FAIL: Y requires X.` — bidirectional; both exit and entry named |
| C-26 | PASS | STRUCTURAL-ERROR-CATALOG table before Phase 1; 17 codes; phase bodies reference by name with `(catalog)` notation |
| C-27 | PASS | PROFILE phase: dedicated "Typed violation codes for this phase" block listing PROFILE-CATEGORY, PROFILE-LENS-UNDERIVED, PROFILE-DUPLICATE-LENS with enforcement and contrast pair |

**Aspirational subtotal: 95/95**

**V-01 Total: 185/185**

---

## V-02 — AMEND full-chain propagation

### Essential

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | CROSS-REF with explicit count matching; BUILD-COMPLETE gated on CROSS-REF PASS |
| C-02 | PASS | Step 8a with `+--`/`\|`; verbatim names; two-level minimum |
| C-03 | PASS | IA-WRITTEN four-check gate; non-transplantable enforcement |
| C-04 | PASS | Path pattern stated; VALIDATE area slug uniqueness check |
| C-05 | PASS | Five fields with content bars stated in phase instructions |

**Essential subtotal: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | ARTIFACT-A with all required columns |
| C-07 | PASS | role-type in frontmatter; standard → specialized sequence; distinctness enforcement ("requires rewrite") |
| C-08 | PASS | AMEND: `--area` (PROFILE-REDERIVE → IA-WRITTEN → BUILD-VERIFY), `--levels`, `--restructure`; three options with PROFILE-REDERIVE-COMPLETE gate |

**Recommended subtotal: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | IA-WRITTEN non-transplantable contrast pair present (lines 742–746) |
| C-10 | PASS | Literal MATCH\|MISMATCH CROSS-REF strings |
| C-11 | PASS | STRUCTURAL-ERROR-CATALOG named codes + ENTRY-GATE tokens |
| C-12 | PASS | Literal check strings throughout |
| C-13 | PARTIAL | PROFILE and IA contrast pairs present; no WRITE-ROLES specialized-distinctness named concrete example (V-02 omits ROLES-WRITTEN section where this would appear) |
| C-14 | PASS | Per-phase typed violation codes block; EXCLUSION-MANIFEST |
| C-15 | PASS | Named check output sections present |
| C-16 | PASS | Full 9-token phase-exit chain |
| C-17 | PASS | TRANSCRIPTION-RECEIPT per artifact |
| C-18 | PASS | Single-responsibility + EXCLUSION-MANIFEST |
| C-19 | PASS | PATH-B remediation loop |
| C-20 | PASS | EXCLUSION-MANIFEST table |
| C-21 | PASS | TRANSCRIPTION-CLEAR all three artifacts |
| C-22 | PASS | IA contrast pair present |
| C-23 | PASS | 16-code STRUCTURAL-ERROR-CATALOG |
| C-24 | PASS | WRITE-CHART-PREMATURE-EXIT in catalog |
| C-25 | PASS | ENTRY-GATE bidirectional in every phase |
| C-26 | PASS | Pre-execution catalog before Phase 1 |
| C-27 | PASS | PROFILE typed violation codes block |

**Aspirational subtotal: 92.5/95 (C-13 PARTIAL = 2.5)**

**V-02 Total: 182.5/185**

---

## V-03 — CATALOG-CLOSURE attestation

### Essential

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | CROSS-REF count matching + CATALOG-CLOSURE gate before BUILD-COMPLETE |
| C-02 | PASS | ASCII hierarchy Step 8a |
| C-03 | PASS | IA-WRITTEN four-check gate |
| C-04 | PASS | Path pattern; VALIDATE area slug uniqueness |
| C-05 | PASS | Five fields specified |

**Essential subtotal: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | ARTIFACT-A with all columns |
| C-07 | PASS | role-type; standard → specialized; distinctness enforced |
| C-08 | PASS | Three AMEND options present |

**Recommended subtotal: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | IA contrast pair present |
| C-10 | PASS | Literal CROSS-REF strings |
| C-11 | PASS | Named codes + ENTRY-GATE tokens |
| C-12 | PASS | Literal check strings; CATALOG-CLOSURE adds additional literal disposition strings |
| C-13 | PARTIAL | No WRITE-ROLES specialized-distinctness named concrete example (V-03 omits ROLES-WRITTEN) |
| C-14 | PASS | Per-phase typed violation codes + EXCLUSION-MANIFEST |
| C-15 | PASS | Named check output sections |
| C-16 | PASS | Full 9-token phase-exit chain |
| C-17 | PASS | TRANSCRIPTION-RECEIPT per artifact |
| C-18 | PASS | Single-responsibility + EXCLUSION-MANIFEST |
| C-19 | PASS | PATH-B remediation loop |
| C-20 | PASS | EXCLUSION-MANIFEST table |
| C-21 | PASS | TRANSCRIPTION-CLEAR all three |
| C-22 | PASS | IA contrast pair |
| C-23 | PASS | 16-code STRUCTURAL-ERROR-CATALOG |
| C-24 | PASS | WRITE-CHART-PREMATURE-EXIT |
| C-25 | PASS | ENTRY-GATE bidirectional |
| C-26 | PASS | Pre-execution catalog |
| C-27 | PASS | PROFILE typed codes block |

**Aspirational subtotal: 92.5/95 (C-13 PARTIAL = 2.5)**

**V-03 Total: 182.5/185**

---

## V-04 — ROLES-WRITTEN + AMEND full-chain

### Essential

All five: PASS (same as V-01; adds PROFILE-REDERIVE to --area amend path)

**Essential subtotal: 60/60**

### Recommended

All three: PASS (AMEND: PROFILE-REDERIVE-COMPLETE → IA-WRITTEN → ROLES-WRITTEN → BUILD-VERIFY; three named options)

**Recommended subtotal: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-12 | PASS | Same as V-01 |
| C-13 | PASS | PROFILE contrast + IA contrast + ROLES-WRITTEN specialized-distinctness contrast (generic scalar extension vs. schema negotiation contract); three named concrete examples |
| C-14–C-24 | PASS | Same as V-01; 17-code catalog includes ROLES-COMPLETE-PREMATURE |
| C-25–C-27 | PASS | Same as V-01 |

**Aspirational subtotal: 95/95**

**V-04 Total: 185/185**

---

## V-05 — Full integration (V-01 + V-02 + V-03)

### Essential

All five: PASS

**Essential subtotal: 60/60**

### Recommended

All three: PASS (AMEND is strongest: PROFILE-REDERIVE + IA-WRITTEN + ROLES-WRITTEN + BUILD-VERIFY + DERIVATION-LOOP-CLOSED re-emission; area regeneration option references all invariant re-checks explicitly)

**Recommended subtotal: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Full IA-WRITTEN four-check contract; non-transplantable contrast pair with full descriptive context |
| C-10 | PASS | Literal CROSS-REF strings |
| C-11 | PASS | 17-code STRUCTURAL-ERROR-CATALOG + ENTRY-GATE per phase + CATALOG-CLOSURE disposition per code; most complete named-constraint coverage of any variation |
| C-12 | PASS | Literal check strings; CATALOG-CLOSURE disposition strings add a second layer of post-execution auditable output |
| C-13 | PASS | PROFILE contrast, IA contrast, ROLES-WRITTEN specialized-distinctness contrast — three concrete named examples covering major quality bars |
| C-14 | PASS | PROFILE typed violation codes block + EXCLUSION-MANIFEST + STRUCTURAL-ERROR-CATALOG pre-execution |
| C-15 | PASS | Named check output sections throughout |
| C-16 | PASS | Full 9-token phase-exit chain; BUILD-COMPLETE signature extended: "CROSS-REF PASS. CATALOG-CLOSURE CLEAN." |
| C-17 | PASS | TRANSCRIPTION-RECEIPT per artifact; PATH-B re-emission |
| C-18 | PASS | "exactly one responsibility" + EXCLUSION-MANIFEST |
| C-19 | PASS | PATH-B remediation loop |
| C-20 | PASS | EXCLUSION-MANIFEST table with 6 entries |
| C-21 | PASS | TRANSCRIPTION-CLEAR all three artifacts |
| C-22 | PASS | IA contrast pair with FAIL (transplantable) vs PASS (team-specific) |
| C-23 | PASS | 17-code STRUCTURAL-ERROR-CATALOG; CATALOG-CLOSURE converts catalog from reference to audit record |
| C-24 | PASS | WRITE-CHART-PREMATURE-EXIT + ROLES-COMPLETE-PREMATURE; premature exits named in catalog |
| C-25 | PASS | ENTRY-GATE bidirectional in all 9 phase transitions |
| C-26 | PASS | Pre-execution catalog before Phase 1; 17 codes with Code/Phase/Trigger |
| C-27 | PASS | PROFILE typed violation codes block with enforcement and contrast pair |

**Aspirational subtotal: 95/95**

**V-05 Total: 185/185**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | **Total** | Golden (≥153)? |
|-----------|-----------|-------------|--------------|-----------|----------------|
| V-01 | 60 | 30 | 95 | **185** | YES |
| V-02 | 60 | 30 | 92.5 | **182.5** | YES |
| V-03 | 60 | 30 | 92.5 | **182.5** | YES |
| V-04 | 60 | 30 | 95 | **185** | YES |
| V-05 | 60 | 30 | 95 | **185** | YES |

## Ranking

1. **V-05** (185) — All three new axes integrated; only variation with CATALOG-CLOSURE + ROLES-WRITTEN + AMEND PROFILE-REDERIVE simultaneously; BUILD-COMPLETE signature includes CATALOG-CLOSURE CLEAN
2. **V-04** (185) — ROLES-WRITTEN + AMEND PROFILE-REDERIVE; strongest amend chain of non-CATALOG-CLOSURE variants
3. **V-01** (185) — ROLES-WRITTEN with named distinctness contrast and ROLES-COMPLETE-PREMATURE code; catalog is cleanest structural symmetry with IA-WRITTEN
4. **V-02** (182.5) — AMEND PROFILE-REDERIVE closes derivation gap but C-13 is PARTIAL without ROLES-WRITTEN named concrete example
5. **V-03** (182.5) — CATALOG-CLOSURE is a structurally novel pattern but C-13 PARTIAL for same reason as V-02

---

## Excellence Signals from V-05

**Signal 1 — CATALOG-CLOSURE closed-loop audit (C-30 candidate)**
V-03 and V-05 introduce the first criterion pair in the rubric where a structural promise has both a pre-execution declaration gate (C-26 catalog) and a post-execution closure gate. Every catalog code receives an explicit runtime disposition (CONFIRMED-NOT-TRIGGERED or TRIGGERED+RESOLVED); any code without a disposition is OPEN and blocks BUILD-COMPLETE. This converts the catalog from an untested claim into a verifiable contract.

**Signal 2 — ROLES-WRITTEN per-team receipt (C-28 candidate)**
V-01/V-04/V-05 extend the IA-WRITTEN per-team feedback loop to WRITE-ROLES, creating structural symmetry between both write phases. ROLES-WRITTEN emits two verdicts: `standard-fields-complete` and `specialized-distinctness`. Named failure mode contrast (generic scalar extension vs. specific contract ownership) mirrors the C-22 IA contrast structure. STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE added to catalog — a premature-exit code for WRITE-ROLES matching the existing WRITE-CHART pattern.

**Signal 3 — AMEND PROFILE-REDERIVE full-chain propagation (C-29 candidate)**
V-02/V-04/V-05 close the PROFILE-IA consistency gap in the amend path. The `--area` amend option now begins with PROFILE-REDERIVE, emitting all three PROFILE typed violation checks and PROFILE-REDERIVE-COMPLETE before any role file is regenerated. This makes amend-path PROFILE compliance as observable as forward-path compliance. In V-04/V-05 the chain extends through ROLES-WRITTEN as well.

**Signal 4 — Three-window lifecycle audit closure (V-05 only)**
V-05 is the first variation to close all three lifecycle audit windows simultaneously: per-write-team quality (ROLES-WRITTEN during WRITE-ROLES), amend chain origin (PROFILE-REDERIVE before WRITE-IA on --area), and build-end catalog accountability (CATALOG-CLOSURE before BUILD-COMPLETE). No audit window — forward write, amend regeneration, or build completion — is left without an observable named closure token.

---

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["CATALOG-CLOSURE post-execution audit converts STRUCTURAL-ERROR-CATALOG from pre-execution promise to closed-loop record; first criterion pair with both a declaration gate (C-26) and a closure gate; BUILD-COMPLETE gated on CATALOG-CLOSURE: CLEAN", "ROLES-WRITTEN per-team receipt mirrors IA-WRITTEN pattern in WRITE-ROLES, creating symmetric per-team quality verification across both write phases with field-completeness and specialized-distinctness checks and named STRUCTURAL-ERROR:ROLES-COMPLETE-PREMATURE", "AMEND PROFILE-REDERIVE closes PROFILE-IA consistency gap in amend path; re-derivation precedes any role file regeneration making amend-path PROFILE compliance as observable as forward-path compliance", "Full three-window lifecycle audit closure in V-05: per-write-team quality (ROLES-WRITTEN), amend chain origin (PROFILE-REDERIVE), and build-end catalog accountability (CATALOG-CLOSURE) close all audit windows simultaneously"]}
```
