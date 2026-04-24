# Scorecard — corps-build Round 11 (Rubric v9)

---

## Per-Variation Analysis

---

### V-01 — INVARIANTS-block axis

**Axis**: Dedicated `INVARIANTS:` block with 5 named identifiers + C-33 co-extensive declaration. No CHECK-OUTPUT PROTOCOL.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role file completeness | PASS | ROLES-COMPLETE + CROSS-REF file-count row with MATCH|MISMATCH |
| C-02 | org-chart.md ASCII hierarchy | PASS | `+--`/`|` stated, verbatim names, min two levels, TRANSCRIPTION-RECEIPT gates |
| C-03 | IA in every team | PASS | ROLES-COMPLETE-PREMATURE guard; IA-PHASE-COMPLETE closure enforced |
| C-04 | org.yaml structural fidelity | PASS | Pre-write path validation with PATH-ISOLATION-VIOLATION halt |
| C-05 | Typed fields present | PASS | All five fields named; WRITE-ROLES-FIELD-MISSING error code enforced |
| C-06 | Headcount table + levels | PASS | TABLE-CLOSED: Group\|Standard\|Specialized\|IA\|Total\|Levels; IA column explicit |
| C-07 | Standard vs specialized | PASS | role-type in frontmatter; standard→specialized→IA sequence stated; SPECIALIZATION-COPY-VIOLATION enforced inline |
| C-08 | AMEND three options | PASS | `--area`, `--level`, `--group` all present with named repair logic |
| C-09 | IA team-contextualized | PASS | FAIL/PASS contrast pair explicit; IA-WRITTEN receipt records lens-source + artifact-source from PROFILE |
| C-10 | Cross-reference integrity | PASS | Literal CROSS-REF block with `MATCH \| MISMATCH` per row |
| C-11 | Named invariants block | **PASS** | Dedicated `### INVARIANTS` block; 5 named identifiers (INVARIANT-PATH-ISOLATION etc.) each paired to enforcement codes; C-33 CO-EXTENSIVE DECLARATION embedded |
| C-12 | Auditable check-output | PASS | CROSS-REF, TRANSCRIPTION-RECEIPT, ROLES-WRITTEN all emit literal parseable check strings |
| C-13 | Named failure modes | PASS | IA FAIL/PASS contrast pair is a named concrete failure mode; STRUCTURAL-ERROR codes name failures per criterion |
| C-14 | Pre-step FAILURE MODES block | PASS | STRUCTURAL-ERROR-CATALOG declared before all phase bodies; named codes, not embedded inline |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **PARTIAL** | No dedicated CHECK-OUTPUT PROTOCOL section; check strings emitted but phases do not reference by COP-NN id |
| C-16 | Phase-exit guard tokens | PASS | Full token chain: PARSE-PASS → … → BUILD-VERIFY-COMPLETE; every phase names ENTRY-GATE predecessor |
| C-17 | Per-artifact TRANSCRIPTION-RECEIPT | PASS | All 3 artifacts (ARTIFACT-A/B/C) with VERBATIM\|REVISED per artifact |
| C-18 | BUILD-VERIFY single-purpose | PASS | Single-responsibility declaration; EXCLUSION-MANIFEST table with 6 excluded actions |
| C-19 | TRANSCRIPTION-RECEIPT in-phase remediation | PASS | "If any artifact is REVISED: describe revision reason. Confirm final content is faithful to org.yaml." |
| C-20 | BUILD-VERIFY exclusion manifest | PASS | Formal EXCLUSION-MANIFEST table present |
| C-21 | TRANSCRIPTION-CLEAR all-artifact re-audit | PASS | `TRANSCRIPTION-CLEAR: All 3 artifacts confirmed. CHART-WRITTEN authorized.` |
| C-22 | IA failure mode contrast pair | PASS | FAIL (generic) / PASS (team-specific) contrast pair explicit in WRITE-IA |
| C-23 | Typed STRUCTURAL-ERROR taxonomy | PASS | All 17 violations encoded as STRUCTURAL-ERROR:* codes in catalog |
| C-24 | Premature-exit named as STRUCTURAL-ERROR | PASS | WRITE-CHART-PREMATURE-EXIT and ROLES-COMPLETE-PREMATURE both named |
| C-25 | ENTRY-GATE bidirectional enforcement | PASS | Each phase names both entry token and exit token; ENTRY-GATE-FAIL on missing predecessor |
| C-26 | Pre-execution STRUCTURAL-ERROR-CATALOG | PASS | Catalog declared before all phase bodies |
| C-27 | PROFILE typed violation taxonomy | PASS | Per-team PROFILE block with STRUCTURAL-ERROR:PROFILE-* codes enumerated |
| C-28 | ROLES-WRITTEN field-completeness receipt | PASS | Per-team ROLES-WRITTEN receipt with standard-fields-complete: YES\|NO |
| C-29 | AMEND --area PROFILE-REDERIVE gate | PASS | PROFILE-REDERIVE-COMPLETE required before WRITE-IA in AMEND --area chain |
| C-30 | CATALOG-CLOSURE terminal attestation | PASS | CATALOG-CLOSURE enumerates all 17 codes; TRIGGERED+RESOLVED requires triggered-at + resolved-by |
| C-31 | ROLES-WRITTEN NO-halt remediation cycle | PASS | "Enter remediation loop: identify deficient fields → rewrite → re-emit → confirm YES. DO NOT advance to next team until YES." |
| C-32 | AMEND-CHAIN-COMPLETE terminal token | PASS | AMEND-CHAIN-COMPLETE with PROFILE-DELTA, files-regenerated, ROLES-WRITTEN-summary, BUILD-VERIFY-summary |
| C-33 | STRUCTURAL-ERROR-CATALOG as INVARIANTS contract | PASS | CATALOG-CLOSURE INVARIANTS DECLARATION: "STRUCTURAL-ERROR-CATALOG and INVARIANTS block are the same contract. CATALOG-CLOSURE CLEAN = invariants contract satisfied." |

**Subtotals**: Essential 60/60 · Recommended 30/30 · Aspirational 122.5/125
**Composite: 212.5 / 215** — Golden PASS

---

### V-02 — CHECK-OUTPUT PROTOCOL axis

**Axis**: Dedicated `CHECK-OUTPUT PROTOCOL` section COP-01–COP-21; phase bodies reference by COP-NN id. No INVARIANTS block.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role file completeness | PASS | Same as V-01 |
| C-02 | org-chart.md ASCII hierarchy | PASS | Same |
| C-03 | IA in every team | PASS | Same |
| C-04 | org.yaml structural fidelity | PASS | Same |
| C-05 | Typed fields present | PASS | Same |
| C-06 | Headcount table + levels | PASS | Same |
| C-07 | Standard vs specialized | PASS | Same |
| C-08 | AMEND three options | PASS | Same |
| C-09 | IA team-contextualized | PASS | Same |
| C-10 | Cross-reference integrity | PASS | Same |
| C-11 | Named invariants block | **PARTIAL** | STRUCTURAL-ERROR-CATALOG header states "constitutes the complete invariants contract" but no separate labeled `INVARIANTS` block with distinct named identifiers (INVARIANT-PATH-ISOLATION etc.) |
| C-12 | Auditable check-output | PASS | Same |
| C-13 | Named failure modes | PASS | Same |
| C-14 | Pre-step FAILURE MODES block | PASS | Same |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **PASS** | Dedicated `### CHECK-OUTPUT PROTOCOL` section; COP-01–COP-21 enumerated with format + emitting phase; phase bodies reference "per CHECK-OUTPUT PROTOCOL" with COP-NN ids |
| C-16 | Phase-exit guard tokens | PASS | Same |
| C-17 | Per-artifact TRANSCRIPTION-RECEIPT | PASS | Same |
| C-18 | BUILD-VERIFY single-purpose | PASS | EXCLUSION-MANIFEST references "per CHECK-OUTPUT PROTOCOL item COP-17 format requirement" |
| C-19–C-33 | (all baseline) | PASS (×15) | All R10 baseline criteria carried forward |

**Subtotals**: Essential 60/60 · Recommended 30/30 · Aspirational 122.5/125
**Composite: 212.5 / 215** — Golden PASS

---

### V-03 — SPECIALIZATION-GATE axis

**Axis**: Named SPECIALIZATION-GATE block per team in Phase 7 with per-role comparison table and gate-verdict. No INVARIANTS block, no CHECK-OUTPUT PROTOCOL.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role file completeness | PASS | Same |
| C-02 | org-chart.md ASCII hierarchy | PASS | Same |
| C-03 | IA in every team | PASS | Same |
| C-04 | org.yaml structural fidelity | PASS | Same |
| C-05 | Typed fields present | PASS | Same |
| C-06 | Headcount table + levels | PASS | Same |
| C-07 | Standard vs specialized | PASS | SPECIALIZATION-GATE adds named auditable comparison; ROLES-COMPLETE includes `all-specialization-gates-passed: YES` |
| C-08 | AMEND three options | PASS | AMEND --area explicitly includes SPECIALIZATION-GATE per team in Phase 7 re-run |
| C-09 | IA team-contextualized | PASS | Same |
| C-10 | Cross-reference integrity | PASS | Same |
| C-11 | Named invariants block | **PARTIAL** | STRUCTURAL-ERROR-CATALOG header says "constitutes the complete invariants contract" but no separate INVARIANTS block with named identifiers |
| C-12 | Auditable check-output | PASS | SPECIALIZATION-GATE emits per-role comparison table with lens-match-against-standard and gate-verdict literal |
| C-13 | Named failure modes | PASS | Same |
| C-14 | Pre-step FAILURE MODES block | PASS | Same |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **PARTIAL** | No dedicated CHECK-OUTPUT PROTOCOL section |
| C-16–C-33 | (all baseline) | PASS (×18) | All R10 baseline criteria carried forward |

**Subtotals**: Essential 60/60 · Recommended 30/30 · Aspirational 120/125
**Composite: 210 / 215** — Golden PASS

---

### V-04 — INVARIANTS-block + CHECK-OUTPUT PROTOCOL (combined)

**Axis**: Both V-01 and V-02 axes combined. No SPECIALIZATION-GATE.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | (all essential + recommended) | PASS (×8) | Full baseline |
| C-09 | IA team-contextualized | PASS | Same; WRITE-IA references INVARIANT-IA-PRESENCE explicitly |
| C-10 | Cross-reference integrity | PASS | Same |
| C-11 | Named invariants block | **PASS** | Dedicated `### INVARIANTS` block with 5 named identifiers paired to codes; C-33 CO-EXTENSIVE DECLARATION in block header; CATALOG-CLOSURE INVARIANTS DECLARATION bridges both |
| C-12–C-14 | Same | PASS (×3) | |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **PASS** | Dedicated `### CHECK-OUTPUT PROTOCOL` section COP-01–COP-21; phase bodies reference COP-NN ids AND invariant names (e.g., "INVARIANT-PATH-ISOLATION" in Phase 7) |
| C-16–C-33 | (all baseline) | PASS (×18) | All R10 baseline criteria; C-33 reinforced by both INVARIANTS C-33 declaration and CATALOG-CLOSURE INVARIANTS DECLARATION |

**Subtotals**: Essential 60/60 · Recommended 30/30 · Aspirational 125/125
**Composite: 215 / 215** — Golden PASS — **MAX SCORE**

---

### V-05 — Full integration (all R11 axes)

**Axis**: V-01 + V-02 + V-03. INVARIANTS block + CHECK-OUTPUT PROTOCOL (COP-01–COP-22, renumbered for SPECIALIZATION-GATE) + SPECIALIZATION-GATE.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | (all essential + recommended) | PASS (×8) | Full baseline; C-07 strongest — SPECIALIZATION-GATE is a named per-team auditable gate in COP sequence |
| C-09 | IA team-contextualized | PASS | Same; WRITE-IA references INVARIANT-IA-PRESENCE |
| C-10 | Cross-reference integrity | PASS | Same |
| C-11 | Named invariants block | **PASS** | Dedicated INVARIANTS block with 5 named identifiers; C-33 triple-reinforced |
| C-12 | Auditable check-output | PASS | SPECIALIZATION-GATE per team emits per-role comparison table as a COP check string (COP-12) |
| C-13–C-14 | Same | PASS (×2) | |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **PASS** | SPECIALIZATION-GATE promoted to COP-12; COP renumbered to COP-22 to absorb the new gate; ROLES-WRITTEN is COP-13; ROLES-COMPLETE is COP-14 — gate is a first-class protocol obligation |
| C-16–C-33 | (all baseline) | PASS (×18) | C-33: triple bridge — STRUCTURAL-ERROR-CATALOG header, INVARIANTS block C-33 declaration, CATALOG-CLOSURE INVARIANTS DECLARATION |

**Subtotals**: Essential 60/60 · Recommended 30/30 · Aspirational 125/125
**Composite: 215 / 215** — Golden PASS — **MAX SCORE + C-34 candidate**

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-04 | 60/60 | 30/30 | 125/125 | **215** | YES |
| V-05 | 60/60 | 30/30 | 125/125 | **215** | YES |
| V-01 | 60/60 | 30/30 | 122.5/125 | **212.5** | YES |
| V-02 | 60/60 | 30/30 | 122.5/125 | **212.5** | YES |
| V-03 | 60/60 | 30/30 | 120/125 | **210** | YES |

**Rank**: V-04 = V-05 (215) > V-01 = V-02 (212.5) > V-03 (210). All five variations pass Golden threshold (all essential PASS + composite ≥ 178). V-03 and V-05 differ by zero rubric points but V-05 carries the C-34 excellence pattern.

---

## Excellence Signals from V-04/V-05

**Signal 1 — Dual-block contract declaration with bidirectional bridge**: V-04/V-05 place C-33 at two anchors — in the INVARIANTS block header ("The INVARIANTS block and STRUCTURAL-ERROR-CATALOG are co-extensive. They describe the same contract from complementary perspectives.") and in the CATALOG-CLOSURE INVARIANTS DECLARATION ("all five named invariants satisfied. The INVARIANTS block and this catalog are co-extensive declarations of the same contract."). Bridging from both ends eliminates ambiguity about which block governs if they ever diverge.

**Signal 2 — SPECIALIZATION-GATE as COP-sequence-ordinal gate (V-05 only)**: Promoting SPECIALIZATION-GATE to COP-12 in the CHECK-OUTPUT PROTOCOL (rather than treating it as a phase-body sub-step) makes it a mandatory check-string emission in the same protocol that governs CROSS-REF and CATALOG-CLOSURE. It acquires an audit slot in the protocol index, a named position in the phase sequence, and a ROLES-COMPLETE attestation field (`all-specialization-gates-passed: YES`). This converts a distinctness check into an independently traceable gate obligation — the same structural move that C-17 made for TRANSCRIPTION-RECEIPT. This is the C-34 candidate pattern.

**Signal 3 — INVARIANTS block references phase names as locus**: V-04/V-05 phase bodies refer back to invariant identifiers inline (e.g., "INVARIANT-PATH-ISOLATION" in Phase 7 path validation, "INVARIANT-FIELD-COMPLETENESS" in field check). This creates a bidirectional lookup: from the phase body → to the invariant name → to the enforcement code, enabling an executor to trace any failure through the invariant contract by name rather than by code alone.

---

## C-34 Candidate Pattern

**Pattern name**: SPECIALIZATION-GATE (named within-phase distinctness gate)
**Definition**: A named per-team gate block emitted after a write step and before the step's receipt, containing a per-role comparison table (lens-match-against-standard, expertise-match-against-standard, pair-identical), a typed gate verdict (gate-verdict: PASS|FAIL), and a corresponding COP-NN id in the CHECK-OUTPUT PROTOCOL. Gate-verdict FAIL triggers STRUCTURAL-ERROR emission and a named rewrite-re-emit loop before the receipt is permitted.
**Why it matters**: Converts inline distinctness enforcement into an independently auditable gate with a named protocol obligation, a position in the phase sequence, and a closure attestation in ROLES-COMPLETE. The same pattern generalizes to any within-phase validation step that currently lives as inline prose.

---

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["SPECIALIZATION-GATE promoted to COP-sequence-ordinal check string: gate block with per-role comparison table and gate-verdict token acquires a COP-NN id, mandatory protocol emission, and ROLES-COMPLETE attestation field — converts inline distinctness check into independently auditable named gate (C-34 candidate)", "Dual-anchor C-33 bridge: co-extensive declaration placed in both the INVARIANTS block header and the CATALOG-CLOSURE INVARIANTS DECLARATION, ensuring bidirectional traceability between constraint naming and enforcement coding from both ends of the spec"]}
```
