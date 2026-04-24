## flow-trigger — Round 11 Scoring (v8 Rubric)

### Preliminary: Scoring Model

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/21 * 10)
PARTIAL = 0.5 pass weight
Golden threshold: all essential PASS + composite >= 80
```

All 5 variations share identical Phases 1–6 structure. Variation is confined to Phase 0. Essential and Recommended criteria are evaluated against the shared scaffold.

---

### Essential Criteria (C-01–C-05)

All five variations carry: Platform Term Contract, FIRING/NON-FIRING ENTRY schemas, Phases 1–6 with denominator scan (Phase 1), ordered sync/async enumeration (Phases 2–3), cascade tracing (Phase 4), three-verdict anomaly assessment (Phase 5), trigger map + closure (Phase 6).

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| **C-01** Trigger enumeration | PASS | PASS | PASS | PASS | PASS |
| **C-02** Execution order stated | PASS | PASS | PASS | PASS | PASS |
| **C-03** Inputs/outputs per trigger | PASS | PASS | PASS | PASS | PASS |
| **C-04** Three anomaly class verdicts | PASS | PASS | PASS | PASS | PASS |
| **C-05** Platform grounding | PASS | PASS | PASS | PASS | PASS |

Essential contribution: **60/60** all variations.

---

### Recommended Criteria (C-06–C-08)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| **C-06** Circular trigger analysis | PASS | PASS | PASS | PASS | PASS |
| **C-07** Conditional branch paths | PASS | PASS | PASS | PASS | PASS |
| **C-08** Anomaly remediation proposed | PASS | PASS | PASS | PASS | PASS |

C-06: Phase 5 verdict table mandates evidence citation for circular class. C-07: bilateral Condition (Taken)/Condition (Skipped) in both entry schemas. C-08: Phase 5 exit condition requires remediation per confirmed anomaly.

Recommended contribution: **30/30** all variations.

---

### Aspirational Criteria (C-09–C-29)

#### Shared-structure criteria (same across all variations)

| ID | All Variations | Evidence |
|----|---------------|---------|
| **C-09** Tier/latency flags | PASS | Phase 3 mandates Latency Tier column; EOR TABLE declared |
| **C-10** Cascade completeness | PASS | Phase 4 traces chains to [TERMINAL]; cascade entry schema |
| **C-11** Candidate denominator | PASS | Phase 1 declares N before filtering; Denominator Pre-Scan table |
| **C-12** Gap tokens | PASS | NON-FIRING ENTRY schema with Reason Not Firing = structural gap token |
| **C-13** Verdict evidence citation | PASS | Phase 5 verdict table has mandatory Evidence (row/chain citations) column |
| **C-14** Scope gate | PASS | EC-01 SCOPE GATE: entity type, operation, field bounds before enumeration |
| **C-15** Bilateral counterfactual | PASS | FIRING ENTRY: Condition (Taken) + Condition (Skipped); NON-FIRING ENTRY: same bilateral slots |
| **C-16** Registration witness | **FAIL** | No Registration Witness slot in FIRING or NON-FIRING ENTRY schemas across any variation |
| **C-17** EOR citation per entry | PASS | EOR TABLE (ART-04) with EOR-01–EOR-04; V-01 EC-04 mandates "Positioned because: EOR-{NN}" per firing entry; inherited by V-02–V-05 |
| **C-18** Cascade depth budget | PASS | EC-05: MAX_CASCADE_DEPTH=4, [Depth: N/4] counter format, [DEPTH EXCEEDED] overflow; storm verdict checks DE count |
| **C-22** Uniform slot mandate | PASS | STRUCTURAL INVARIANT: "Every named slot in every entry template is required. An empty named slot is a structural gap." Covers all entry types |
| **C-23** Artifact lock | PASS | ARTIFACT MANIFEST with ART-01–ART-07 assigned IDs before enumeration; CLOSURE CHECK resolves against ART-NN references |
| **C-24** Breach markers | PASS | EC-03 declares named breach token format `[PROHIBITION BREACH: Role N | name]`; CLOSURE CHECK counter "PROHIBITION BREACHES: {count} [must be 0]" reserved |
| **C-25** Lifecycle gate | PASS | Phase 0 named, five typed exit conditions (EC-01–EC-05), explicit EXIT SIGNAL statement, no enumeration before signal |

---

#### Differentiating criteria (vary across variations)

**C-19 — Exclusion log**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | PARTIAL | PARTIAL | PARTIAL | **PASS** | PARTIAL |

- V-01/V-02/V-03/V-05: EXCLUSION LOG declared as ART-02 in manifest, but Phase 1 job description doesn't explicitly mandate producing an exclusion log entry and Phase 5 verdict table has no "Exclusion log reference:" field — structure mandated, verdict citation absent.
- V-04: Role 1 (Auditor) explicitly produces a 7-layer Pre-Enumeration Exclusion Log with dispositions and reasons. PASS.

**C-20 — Zero-tolerance closure counters**

All: PARTIAL — EC-03 reserves the PROHIBITION BREACHES counter, and the ARTIFACT MANIFEST pre-declares ART-NN IDs that would be referenced in a CLOSURE CHECK. However, no full CLOSURE CHECK block template with ≥3 named counters (covering EOR citations, registration witnesses, depth-exceeded chains) appears in any variation's Phase 6 template. Structure implied but not rendered.

**C-21 — Named role prohibition contracts**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | FAIL | FAIL | **PASS** | FAIL |

- V-01/V-02/V-03/V-05: ART-03 PROHIBITION CONTRACTS listed in manifest, EC-03 declares breach token format, but no actual PROHIBITION statement appears in the prompt body. Multi-phase output without role-level prohibition declarations.
- V-04: Role 1 explicitly declares PROHIBITION 03a (Domain Expert MAY NOT add candidates after denominator declaration) and PROHIBITION 03b (Domain Expert MAY NOT modify SCOPE GATE). Explicit named prohibitions per role.

**C-26 — INERTIA CONTRAST embedded rationale**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | FAIL | PASS | **PASS** | PASS |

- V-01: Only a footnote about FM-38 narrative failure. No rationale section or equivalent.
- V-02: No Weaker alternative / Failure mode content. Focused on refutation conditions only.
- V-03: Phase 0 Obligation Registry with 6 columns including Weaker alternative and Failure mode for all 5 mechanism rows — named equivalent rationale section per C-26's "or equivalent" language; covers >2 mechanisms with concrete failure modes.
- V-04: Explicit standalone INERTIA CONTRAST section (table) covering ART-02 (ARTIFACT MANIFEST) and ART-04 (EOR TABLE) with weaker alternatives and failure modes. Named section, 2 mechanisms.
- V-05: 7-column unified registry provides rationale in-line for all 5 mechanisms — equivalent to a named rationale section, exceeds C-26's two-mechanism threshold.

**C-27 — Computable exit signal**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | **PASS** | PARTIAL | **PASS** | **PASS** | **PASS** |

- V-01: Phase 0 Exit Condition Registry with explicit Status column (SATISFIED/PENDING/BLOCKED), named enumeration EXIT-STATUS, aggregate "5/5 SATISFIED", states "recomputable by counting Status column." Full PASS.
- V-02: Exit signal checklist shows "SATISFIED (refutation condition co-located)" per item but as a narrative list, not a typed column with aggregate count. The signal says "enumeration authorized" without a "5/5 SATISFIED" aggregate reference. PARTIAL.
- V-03: Phase 0 registry has Status column, "Exit signal: 5/5 SATISFIED -- enumeration authorized." PASS.
- V-04: Named EXIT-STATUS enum, Status column, "5/5 SATISFIED", "derivable by counting Status column — no semantic evaluation." PASS.
- V-05: "Status aggregate: 5/5 SATISFIED"; Invariant 10 requires Status column aggregate; explicitly verifies computability in EXIT SIGNAL block. PASS.

**C-28 — Per-obligation refutation conditions**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | **PASS** | FAIL | FAIL | **PASS** |

- V-01: No "Violated if:" clauses in Phase 0 registry. Only an FM-38 footnote about uncomputable exit signals. EC-01–EC-05 rows have no co-located refutation conditions.
- V-02: Each EC obligation carries an explicit `> Violated if:` block naming a string-detectable breach condition (search for "SCOPE GATE" before first entry, search for "ART-" in CLOSURE CHECK, etc.) with `[REFUTATION ABSENT: EC-NN | FM-39]` self-tagging. Invariant 8 enforces it. PASS.
- V-03: 6-column registry adds Weaker alternative / Failure mode but no "Violated if" column. FAIL.
- V-04: Phase 0 registry has 4 columns (EC-ID, Exit Condition, Required Artifact, Status). FM-39 is in the catalog but no "Violated if:" clauses appear in the registry rows. FAIL.
- V-05: "Violated if" is the 5th named column in the 7-column unified registry. Each row carries a concrete string-searchable condition (e.g., "string-search for 'SCOPE GATE' before first GD- or SEQ- row"). Invariant 10 enforces it. PASS.

**C-29 — INERTIA CONTRAST as typed inline columns**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | FAIL | **PASS** | PARTIAL | **PASS** |

- V-01: No contrast columns. Only FM-38 footnote.
- V-02: No contrast columns. Focused on refutation conditions only.
- V-03: "Weaker alternative" and "Failure mode" appear as typed column headers in Phase 0 Obligation Registry. Column definition declared. All 5 rows carry non-empty values in both columns. Removing a section heading cannot strip the rationale. PASS.
- V-04: INERTIA CONTRAST is a standalone table (Role 1's section), NOT typed columns within the Phase 0 Exit Condition Registry. Achieves C-26 (named section with two mechanisms) but the Phase 0 registry itself lacks the inline columns. PARTIAL per C-29's rubric: "An output that satisfies C-26 with a consolidated INERTIA CONTRAST section but does not embed contrast columns within each mechanism row is a weak pass."
- V-05: "Weaker alternative" (column 6) and "Failure mode" (column 7) are named column headers in the 7-column unified registry. All 5 rows populated. Columns defined in table header. Non-separable at cell level. PASS.

---

### Criterion-by-Criterion Matrix

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | P | P | P |
| C-16 | F | F | F | F | F |
| C-17 | P | P | P | P | P |
| C-18 | P | P | P | P | P |
| C-19 | ~P | ~P | ~P | **P** | ~P |
| C-20 | ~P | ~P | ~P | ~P | ~P |
| C-21 | F | F | F | **P** | F |
| C-22 | P | P | P | P | P |
| C-23 | P | P | P | P | P |
| C-24 | P | P | P | P | P |
| C-25 | P | P | P | P | P |
| C-26 | F | F | **P** | **P** | **P** |
| C-27 | **P** | ~P | **P** | **P** | **P** |
| C-28 | F | **P** | F | F | **P** |
| C-29 | F | F | **P** | ~P | **P** |

*P = PASS, ~P = PARTIAL, F = FAIL*

---

### Aspirational Point Totals

| Variation | PASS count | PARTIAL count | Asp. points | Asp. contribution |
|-----------|-----------|--------------|-------------|-------------------|
| V-01 | 14 | 2 (C-19, C-20) | 15.0 | 7.14 |
| V-02 | 14 | 3 (C-19, C-20, C-27) | 15.5 | 7.38 |
| V-03 | 15 | 2 (C-19, C-20) | 16.0 | 7.62 |

Wait — V-03 adds C-26/C-29 as PASS, loses C-28. Let me recount precisely.

**V-01 PASS:** C-09,10,11,12,13,14,15,17,18,22,23,24,25,27 = 14. PARTIAL: C-19,20. FAIL: C-16,21,26,28,29.
Asp = 14 + 2(0.5) = **15.0**

**V-02 PASS:** C-09,10,11,12,13,14,15,17,18,22,23,24,25,28 = 14. PARTIAL: C-19,20,27. FAIL: C-16,21,26,29.
Asp = 14 + 3(0.5) = **15.5**

**V-03 PASS:** C-09,10,11,12,13,14,15,17,18,22,23,24,25,26,27,29 = 16. PARTIAL: C-19,20. FAIL: C-16,21,28.
Asp = 16 + 2(0.5) = **17.0**

**V-04 PASS:** C-09,10,11,12,13,14,15,17,18,19,21,22,23,24,25,26,27 = 17. PARTIAL: C-20,29. FAIL: C-16,28.
Asp = 17 + 2(0.5) = **18.0**

**V-05 PASS:** C-09,10,11,12,13,14,15,17,18,22,23,24,25,26,27,28,29 = 17. PARTIAL: C-19,20. FAIL: C-16,21.
Asp = 17 + 2(0.5) = **18.0**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|-------------|--------------|
| V-01 | 60.00 | 30.00 | 7.14 | **97.14** |
| V-02 | 60.00 | 30.00 | 7.38 | **97.38** |
| V-03 | 60.00 | 30.00 | 8.10 | **98.10** |
| V-04 | 60.00 | 30.00 | 8.57 | **98.57** |
| V-05 | 60.00 | 30.00 | 8.57 | **98.57** |

**V-04 and V-05 tie at 98.57.** Tiebreaker by new criteria performance:

| New criterion | V-04 | V-05 |
|--------------|------|------|
| C-27 computable exit | PASS | PASS |
| C-28 refutation conditions | FAIL | PASS |
| C-29 inline contrast columns | PARTIAL | PASS |

V-05 satisfies all three new criteria fully. **V-05 ranks first.**

---

### Ranking

| Rank | Variation | Composite | C-27 | C-28 | C-29 | Key differentiator |
|------|-----------|-----------|------|------|------|-------------------|
| 1 | **V-05** | 98.57 | PASS | PASS | PASS | Unified 7-column registry satisfies all three new criteria from a single table scan |
| 2 | **V-04** | 98.57 | PASS | FAIL | PARTIAL | Strongest on C-19/C-21/C-26; loses C-28 |
| 3 | V-03 | 98.10 | PASS | FAIL | PASS | Adds C-29 inline columns but no refutation conditions |
| 4 | V-02 | 97.38 | PARTIAL | PASS | FAIL | Strong refutation conditions; no contrast mechanism |
| 5 | V-01 | 97.14 | PASS | FAIL | FAIL | Best baseline for C-27; misses C-28 and C-29 |

---

### Excellence Signals from V-05

**Signal 1 — Single-scan sufficiency.** The 7-column unified registry is the sole artifact needed to verify C-27, C-28, and C-29 simultaneously. An evaluator inspects one table, one scan pass: counts Status column (C-27), reads Violated-if cells (C-28), reads contrast cells (C-29). No cross-section navigation required.

**Signal 2 — Triple-attestation EXIT SIGNAL.** V-05's Phase 0 exit block explicitly verifies all three new criteria by name: "Computability verified (C-27) / Violation detection verified (C-28) / Rationale co-location verified (C-29)." The EXIT SIGNAL becomes a self-certification artifact, not just a gate signal. This is structurally distinct from V-01 (computability only) and V-02 (refutation only).

**Signal 3 — Invariant 10 as unified enforcement gate.** V-05 introduces a single named invariant (Invariant 10) that mandates all 7 column headers, the status-aggregate exit signal, string-detectable violated-if clauses, and non-generic contrast content. One invariant enforces all three new criteria, reducing the risk that a future variation weakens one criterion while strengthening another.

**Signal 4 — FM-38/FM-39/FM-40 co-declared in one catalog extension.** By carrying all three new FM codes (38, 39, 40) in the FM Catalog and cross-referencing them in Invariant 10, V-05 ensures violation detection for any of the three new criteria produces a named, inline marker — extending the self-announcing violation pattern (C-24) cleanly to C-27/C-28/C-29.

---

```json
{"top_score": 98.57, "all_essential_pass": true, "new_patterns": ["Unified 7-column Phase 0 registry satisfies C-27/C-28/C-29 from a single table scan — no external section required for any new criterion", "Triple-attestation EXIT SIGNAL explicitly verifies computability (C-27), violation-detection (C-28), and rationale co-location (C-29) by name in one block, making Phase 0 self-certifying across all three new criteria", "Single Invariant 10 enforces all three new criteria simultaneously — one invariant replaces three scattered enforcement mechanisms, making partial satisfaction of the new criteria structurally impossible"]}
```
