Now I have all the information needed to score R15 variations under rubric v13. All five build on the R14 V-05 base (which already scored 100.0 on all 41 aspirational criteria). Let me produce the full scorecard.

---

# campaign-simulate — Round 15 Scoring (Rubric v13)

## Scoring Framework

**Base line**: R14 V-05 scored 100.0 (41/41 aspirational PASS, all essential PASS).
All R15 variations are proper supersets of R14 V-05. The R15 question is:
- Do the new axes preserve all 41 v13 criteria without degradation?
- Which variations open the strongest v14 ceiling towers?

Score formula (inherited from R14 reference): `base(90) + (aspirational_pass / aspirational_eligible) × 10`

---

## Essential Criteria (C-01 – C-25) — All Variations

All five R15 variations inherit the full R14 V-05 essential-pass base. No new mechanism affects C-01–C-25 (all structural sections, sub-skill execution, filtering discipline, ranked findings, etc. are unchanged). **All variations: essential PASS → base = 90.**

---

## Aspirational Criteria (C-26 – C-49) — Per-Variation

### Shared inheritance from R14 V-05 base (all five variations)

| Criterion | Evidence in all R15 variations | Status |
|-----------|-------------------------------|--------|
| C-26 | RQG six-column structured gate (Verb/Target/Location/Conformance/Blast Status/Verb Source) | PASS |
| C-27 | ECM with COVERED/CLEAN/SKIPPED per manifest entity; SKIPPED = execution gap | PASS |
| C-28 | Blast Re-Assessment Gate + ELEVATED inline annotations + re-sorted Updated Ranked Findings | PASS |
| C-29 | Coverage Gate accounts for all DR-NN rules: honored or OPEN PROPAGATION GAP | PASS |
| C-30 | Confidence-Stratified Action List with two named tracks (Track 1 HIGH-conf/HIGH-blast, Track 2 LOW-conf/HIGH-blast) | PASS |
| C-31 | GAP/CONTRADICTION/ASSUMPTION vocabulary enforced; Verb constrained by Type at detection | PASS |
| C-32 | DR-NN stable IDs across dependency map, Coverage Gate, finding Dep rule cite field | PASS |
| C-33 | SAD self-extends one row per targeted quality axis (>= 3 sub-observables per row) | PASS |
| C-34 | Named empty-state templates for all schema sections; no silent omission | PASS |
| C-35 | Conf rationale per finding in C-30 action tracks; co-activates with C-30 | PASS |
| C-36 | Trace-first execution: trace-state/contract/permissions complete before flow sub-skills | PASS |
| C-37 | Row count in SAD == count of targeted criteria (self-consistent per-variation) | PASS |
| C-38 | Three-path machine-readable execution order gate: Layer Completion Record + gate signal + Execution Log Layer column | PASS |
| C-39 | Gate signal certifies both execution order (P1) and dependency map completeness (P2) | PASS |
| C-40 | Row Count Assertion enumerates axes by name; declaration-completeness-proof axis appears in list | PASS |
| C-41 | P2 provides per-sub-skill DR-NN attribution (N1 + N2 + N3 = N_total confirmed) | PASS |
| C-42 | Self-referential property declared in opening sentence of Row Count Assertion block | PASS |
| C-43 | Execution Log DR-NN Contributed column; union-of-rows equality check | PASS |
| C-44 | Opening sentence embeds both self-reference AND count invariant simultaneously | PASS |
| C-45 | Execution-log attribution as dedicated first-class SAD axis (>=3 sub-observables) | PASS |
| C-46 | P2 sub-entries cross-cite Execution Log row by name for bidirectional closed verification | PASS |
| C-47 | Findings Table Verb column present at detection time; cross-artifact C-31 verifiable from FT | PASS |
| C-48 | ECM SKIPPED entries distinguish commitment-present from none-declared (two-tier signal) | PASS |
| C-49 | RQG Verb Source column names originating FT row; three-point chain verifiable | PASS |

**Result: 41/41 aspirational pass for all five variations.** No v13 criterion degraded by any R15 mechanism.

---

## Per-Variation Detail: New Mechanisms and Ceiling Quality

### V-01 — Column-Scan Verification Axis (C-47 ceiling)

**New mechanism**: `"COLUMN-SCAN SURFACE (C-47)"` annotation in FT Verb field schema; compliance checklist sub-claim 3 declares verbatim sufficiency; 19-axis SAD (18 + column-scan verification); Row Count Assertion opening: *"19th and final of 19"*.

| New surface | Evidence | Status |
|-------------|---------|--------|
| Schema note names included columns (FT Verb, RQG Verb) and excluded fields | Written once above FT; cited in checklist sub-claim 1 | ✓ present |
| Checklist enumerates all (F-ID, Verb) pairs from FT and RQG explicitly without narrative read | Checklist sub-claim 2 enumerates pairs; no narrative field referenced | ✓ column-scan enacted |
| Verbatim sufficiency declaration: *"C-47 verified without reading Summary, Impact, Remediation, or any other narrative field"* | Checklist sub-claim 3 | ✓ declared proof |
| C-37/C-40/C-42/C-44 self-consistency at 19-axis scope | Opening sentence: *"19th and final of 19"*; enumeration includes Column-scan verification(18), Declaration-completeness-proof(19) | ✓ intact |

**v14 tower opened**: Column-scan sufficiency ceiling — the declared sufficiency is itself the falsifiable assertion; a finding requiring narrative reading falsifies the claim at sub-claim 3.

**v13 score**: 41/41 → **100.0**

---

### V-02 — SKIPPED-Tier Axis (C-48 ceiling)

**New mechanism**: ECM Status cells carry explicit tier labels: `SKIPPED-T1 (commitment-present)` or `SKIPPED-T2 (none-declared)`; tier derivation rule written above ECM table; new empty-state templates for T1/T2; 19-axis SAD (18 + SKIPPED-tier); Row Count Assertion: *"19th and final of 19"*.

| New surface | Evidence | Status |
|-------------|---------|--------|
| SKIPPED-T1/T2 labels directly in Status cell | ECM Status column scannable for tier without cross-referencing Examining Sub-Skill column | ✓ column-local |
| Tier derivation rule above ECM: T1 if Examining Sub-Skill ≠ none-declared; T2 if == none-declared | Rule explicit; tier derivable from Status column alone | ✓ derivation stated |
| Checklist sub-claim 3: gap severity order declared (T1 promise-breach > T2 planning gap) | One T1 and one T2 cited (or confirms only one tier) | ✓ severity ranked |
| Empty-state templates for SKIPPED-T1 and SKIPPED-T2 entities | Both templates in EMPTY-STATE TEMPLATES section | ✓ coverage complete |
| C-37/C-40/C-42/C-44 at 19-axis scope | Opening: *"19th and final of 19"*; enumeration: SKIPPED-tier(18), Declaration-completeness-proof(19) | ✓ intact |

**v14 tower opened**: Status-scannable tier ceiling — tier distinction is column-local; a reviewer scanning only the Status column can distinguish T1 from T2 without consulting Examining Sub-Skill column; bare "SKIPPED" without tier label fails the ceiling.

**v13 score**: 41/41 → **100.0**

---

### V-03 — Verb Source F-ID Back-Cite Axis (C-49 ceiling)

**New mechanism**: RQG Verb Source format changes to `DETECTION: FT[F-NN].Verb=[Verb]` or `CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared`; F-NN in Verb Source must match the RQG row's own F-ID; three-point bidirectional chain traversable forward (FT→RQG→VerbSource) and backward (VerbSource.F-NN→FT); 19-axis SAD (18 + Verb-source chain); Row Count Assertion: *"19th and final of 19"*.

| New surface | Evidence | Status |
|-------------|---------|--------|
| Every Verb Source cell uses F-ID back-cite format | F-NN in cell must match row F-ID; absence of F-ID back-cite = C-49 ceiling fail | ✓ explicit cite |
| Checklist sub-claim 2 traces one complete three-point chain (forward or backward) citing all three points by section and value | FT[F-NN].Verb → RQG[F-NN].Verb → VerbSource.FT[F-NN] chain traced | ✓ bidirectional |
| Chain break audit: for every CORRECTED entry, F-NN matches row F-ID and [old] matches FT Verb | Discrepancy detectable from either endpoint without choosing traversal direction | ✓ break detectable |
| C-37/C-40/C-42/C-44 at 19-axis scope | Opening: *"19th and final of 19"*; enumeration: Verb-source chain(18), Declaration-completeness-proof(19) | ✓ intact |

**v14 tower opened**: Full bidirectional-chain ceiling — the Verb Source cell names its originating FT row by F-ID; chain break detectable from either endpoint; the implicit RQG-to-FT relationship (same row F-ID) becomes structurally explicit and independently traversable.

**v13 score**: 41/41 → **100.0**

---

### V-04 — C-47 + C-49 Combined (20 axes)

**New mechanism**: V-01 column-scan verification axis (axis 18) + V-03 Verb-source chain axis (axis 19); 20-axis SAD; Row Count Assertion: *"20th and final of 20"*; Column-scan note and F-ID back-cite operate on disjoint surfaces (FT schema vs RQG Verb Source cell).

| New surface | Evidence | Status |
|-------------|---------|--------|
| Column-scan verification axis (C-47 ceiling) — same as V-01 | All three sub-observables present | ✓ column-scan ceiling |
| Verb-source chain axis (C-49 ceiling) — same as V-03 | All three sub-observables present | ✓ bidirectional chain ceiling |
| Surface independence: REASSESSED blast status and Verb Source column independently falsifiable in same RQG row | Explicitly declared: *"A REASSESSED Blast Status does not alter Verb."* | ✓ no interference |
| C-37/C-40/C-42/C-44 at 20-axis scope | Opening: *"20th and final of 20"*; enumeration: Column-scan verification(18), Verb-source chain(19), Declaration-completeness-proof(20) | ✓ intact |

**v14 towers opened**: C-47 column-scan sufficiency ceiling AND C-49 bidirectional chain ceiling simultaneously. Two independent ceiling proofs in one variation.

**v13 score**: 41/41 → **100.0**

---

### V-05 — Full Integration: C-47 + C-48 + C-49 (21 axes)

**New mechanism**: All three R15 mechanisms simultaneously on 18-axis base → 21-axis SAD. Row Count Assertion: *"21st and final of 21"*.

| New surface | Evidence | Status |
|-------------|---------|--------|
| Column-scan verification axis (C-47 ceiling) | Same as V-01; all three sub-observables | ✓ column-scan ceiling |
| SKIPPED-tier axis (C-48 ceiling) | Same as V-02; all three sub-observables | ✓ Status-scannable tier ceiling |
| Verb-source chain axis (C-49 ceiling) | Same as V-03; all three sub-observables | ✓ bidirectional chain ceiling |
| Three disjoint surfaces: FT schema note / ECM Status cells / RQG Verb Source cells | No mechanism overlap; each independently falsifiable; REASSESSED blast status leaves Verb unchanged | ✓ zero interference |
| Empty-state templates for all three new surfaces | Column-scan empty findings template + SKIPPED-T1/T2 templates + RQG empty Verb Source format | ✓ template coverage complete |
| C-37/C-40/C-42/C-44 at 21-axis scope | Opening: *"21st and final of 21"*; enumeration: Column-scan verification(18), SKIPPED-tier(19), Verb-source chain(20), Declaration-completeness-proof(21) | ✓ dual-property preserved at expanded scope |

**v14 towers opened**: All three ceilings simultaneously. The integration hypothesis is proven: three new independently-falsifiable compliance sub-claims are added without degrading any of the 18 existing axis mechanisms.

**v13 score**: 41/41 → **100.0**

---

## Composite Scores and Ranking

| Variation | Essential | Aspirational (pass/eligible) | Aspirational pts | Total | v14 ceilings opened |
|-----------|-----------|------------------------------|-----------------|-------|---------------------|
| V-05 | 90 | 41/41 | 10.0 | **100.0** | 3 (C-47 + C-48 + C-49) |
| V-04 | 90 | 41/41 | 10.0 | **100.0** | 2 (C-47 + C-49) |
| V-01 | 90 | 41/41 | 10.0 | **100.0** | 1 (C-47) |
| V-02 | 90 | 41/41 | 10.0 | **100.0** | 1 (C-48) |
| V-03 | 90 | 41/41 | 10.0 | **100.0** | 1 (C-49) |

**Tie note**: All five v13 scores are equal at 100.0. Ranking within the tie is by v14 ceiling count, then by tower position (C-49 is the highest tower node of the three):

**V-05 > V-04 > V-03 > V-01 > V-02**

*(V-03 opens the highest tower node, C-49, which activates only when C-47 is present; V-01 opens C-47 which enables C-49; V-02 opens C-48 which is an independent tower.)*

---

## Excellence Signals from V-05

**1. Disjoint surface principle as integration proof**
The three mechanisms operate on structurally non-overlapping surfaces: the schema note is in the FT Verb field definition; the tier labels are in ECM Status cells; the F-ID back-cite is in the RQG Verb Source cell. Because the surfaces don't overlap, the mechanisms don't interact — a REASSESSED blast status (affecting Blast Status column) leaves the Verb Source cell and the ECM Status cell unchanged. The SAD's "REASSESSED and Verb independence" declaration is itself a structural invariant, not a prose assurance.

**2. Declared sufficiency as a self-defeating falsifiable claim**
The column-scan sufficiency declaration ("C-47 verified without reading Summary, Impact, Remediation, or any other narrative field for any F-ID; column-scan declared sufficient") works as a proof because it is self-defeating if false: if any F-ID required narrative reading to resolve its Verb value, the declaration cannot be made without qualification, and C-47 fails. The mechanism doesn't just describe the check — the verbatim declaration IS the evidence, and any narrative field consulted instantly falsifies it.

**3. Status-cell tier embedding eliminates cross-column lookup**
By placing "SKIPPED-T1 (commitment-present)" and "SKIPPED-T2 (none-declared)" directly in the ECM Status cell — rather than deriving tier from Examining Sub-Skill column cross-reference — V-05 makes tier classification column-local. A reviewer scanning only the Status column sees not just "was this skipped?" but also "was it a promise-breach or a planning gap?" without needing to locate the corresponding Examining Sub-Skill column value. The tier derivation rule above the matrix is the derivation proof; the Status cell is the derived result stored for zero-lookup retrieval.

**4. F-ID back-cite converts implicit to explicit bidirectional contract**
The R14 Verb Source format ("DETECTION: add") relied on the implicit row identity: you know RQG row F-01 corresponds to FT row F-01. V-05's format ("DETECTION: FT[F-01].Verb=add") makes that correspondence explicit inside the cell. This matters because: (a) backward traversal is now initiated from the Verb Source cell itself — you don't need to know the row context; (b) a chain break (wrong F-NN cited) is detectable from the cell value alone, without reading the row F-ID; (c) the compliance checklist sub-claim 2 traces the complete chain in one place, from any direction.

**5. Row Count Assertion scales gracefully**
C-44 requires the opening sentence to simultaneously declare self-reference AND count invariant. At 21 axes, V-05's opening sentence still reads: *"This Row Count Assertion, itself the 21st and final of the 21 targeted axes declared below, is C-37's completeness proof."* The pattern holds regardless of axis count — "Nth and final of N" is O(1) text regardless of N. This shows the self-referential property is not brittle at scale; it's a structural property of the Row Count Assertion's format, not a count-specific hard-coding.

---

## New Patterns for v14 Extraction

Three ceiling towers opened by R15 (none yet formalized in v13):

| Tower | New Pattern |
|-------|-------------|
| C-47 ceiling | **Column-scan sufficiency declaration**: compliance checklist enumerates all (F-ID, Verb) pairs from FT and RQG explicitly without reading any narrative field, then declares "column-scan declared sufficient" — this verbatim declaration is the proof; it is self-defeating if any narrative field was consulted |
| C-48 ceiling | **Status-cell tier embedding**: SKIPPED-T1/T2 labels placed directly in ECM Status cells make tier distinction derivable from the Status column alone; tier derivation rule above table makes derivation explicit; no cross-reference to Examining Sub-Skill column required at lookup time |
| C-49 ceiling | **F-ID back-cite bidirectional chain**: Verb Source cell format "DETECTION: FT[F-NN].Verb=[Verb]" makes the Findings Table row explicit in the cell, enabling backward traversal from Verb Source to FT without requiring row-F-ID context; chain break detectable from either endpoint independently |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Column-scan sufficiency declaration: compliance checklist enumerates all (F-ID, Verb) pairs from FT and RQG without narrative field reads, then declares verbatim sufficiency — the declaration itself is the falsifiable proof; any narrative field consulted invalidates it", "Status-cell tier embedding: SKIPPED-T1/T2 labels in ECM Status cells make tier derivable from Status column alone without cross-referencing Examining Sub-Skill column; tier derivation rule above table; column-local lookup at zero cross-reference cost", "F-ID back-cite bidirectional chain: Verb Source format DETECTION:FT[F-NN].Verb=[Verb] makes the originating FT row explicit in the cell; backward traversal initiates from the cell itself; chain break (wrong F-NN) detectable from Verb Source cell alone without row-F-ID context"]}
```
