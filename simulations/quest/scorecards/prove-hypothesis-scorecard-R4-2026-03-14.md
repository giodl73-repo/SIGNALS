# /quest:score — prove:hypothesis Round 4

## Scoring All Five Variations

---

### V-01: Role Sequence — CONTEXT + Archivist

**Essential (C-01–C-05)**

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Single falsifiable claim | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" in CLAIMANT: DECLARE — enforced by template |
| C-02 | Falsification conditions | PASS | F-01/F-02 table in DECLARE; F-00 in CONTEXT; all F-IDs named with observable outcomes |
| C-03 | Confidence 0-100 | PASS | "Value: [N]/100" with 2-element rationale requirement |
| C-04 | Experiment list | PASS | NAVIGATOR table with prove sub-skills; 2+ experiments required by coverage rule |
| C-05 | No goalpost movement | PASS | CONTEXT runs before DECLARE; LOCK GATE prohibits retroactive edits |

Essential: **5/5**

**Recommended (C-06–C-08)**

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Prior signals note | PASS | Explicit in CONTEXT: "List files found...or write 'None -- starting fresh'" |
| C-07 | Confirmation conditions | PASS | CF-01 table in CLAIMANT: DECLARE |
| C-08 | Confidence references prior evidence | PASS | Rationale requires: "prior signal, trace finding, or friction point"; fallback clause if none |

Recommended: **3/3**

**Aspirational (C-09–C-19)**

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Experiment-to-F-ID mapping | PASS | "F-IDs tested" column in NAVIGATOR table |
| C-10 | Risk-ranked with rationale | PASS | Rank 1 = highest falsification; "Why this risk rank" column required |
| C-11 | Adversarial role gate | PASS | SKEPTIC: CHALLENGE with per-condition PASS/REWRITE verdicts + F-00 validation subsection |
| C-12 | Hard phase gate, read-only | PASS | "LOCKED. Claim and domain conditions above are now read-only. Post-lock problems: log as amendment notes. Do not edit here." |
| C-13 | Status-quo as F-00 | PASS | F-00 born in CONTEXT with observable test before claim is written |
| C-14 | Complete F-ID coverage in Navigator | PASS | "Every F-ID...must appear in at least one experiment row. Any F-ID with no experiment row is an explicit failure" |
| C-15 | Confidence post-lock | PASS | CLAIMANT: CONFIDENCE positioned after LOCK GATE and SEAL GATE in document order |
| C-16 | Multi-pass consolidation with verdicts | PASS | ARCHIVIST collects F-00 (CONTEXT) + F-01+ (SKEPTIC) into Final list; every condition gets CONFIRMED |
| C-17 | Dual-gate phase isolation | PASS | LOCK GATE (freezes claim + domain conditions) and SEAL GATE (freezes Final list) — separate checklists, non-overlapping scopes |
| C-18 | Named consolidation unit | PASS | `## ARCHIVIST: CONSOLIDATE` at peer ## heading level |
| C-19 | Inertia-lead framing | PASS | `## CONTEXT: CURRENT STATE` before DECLARE; "What does the team do today?"; F-00 born there |

Aspirational: **11/11**

**V-01 Score:**
```
essential:    5/5 × 60  = 60.00
recommended:  3/3 × 30  = 30.00
aspirational: 11/11 × 10 = 10.00
composite:  100.00  |  Golden: YES
```

---

### V-02: Output Format — Prose-Only + Named COLLECTOR

**Essential (C-01–C-05)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" in DECLARE |
| C-02 | PASS | F-01/F-02 as numbered list with observable outcomes; F-00 in OPENING |
| C-03 | PASS | "Confidence: [N]/100" with two-element rationale |
| C-04 | PASS | Numbered experiment list with sub-skill and F-IDs per entry |
| C-05 | PASS | OPENING runs before DECLARE; DECLARE GATE prohibits retroactive edits |

Essential: **5/5**

**Recommended (C-06–C-08)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | OPENING item 1: "Prior signals — list file names...or write 'None -- starting fresh'" |
| C-07 | PASS | "What would confirm you right: CF-01" in DECLARE |
| C-08 | PASS | Confidence requires "prior signal, trace finding, or friction point" with fallback |

Recommended: **3/3**

**Aspirational (C-09–C-19)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Each experiment entry has "F-IDs tested: [F-00, F-01, ...]" field |
| C-10 | PASS | Ordered by falsification risk; "Risk rationale" required per entry |
| C-11 | PASS | CHALLENGE prose annotations: "F-01 [text]: PASS -- observable via... / REWRITE -- problem. Revised:" — explicit verdict per condition; F-00 validation separate |
| C-12 | PASS | "LOCKED. Claim and conditions above are now read-only. Post-lock problems...log as amendment notes in Navigate." |
| C-13 | PASS | F-00 born in OPENING with observable test |
| C-14 | PASS | "COVERAGE RULE: Before writing the artifact, verify every F-ID...appears under at least one experiment." |
| C-15 | PASS | CONFIDENCE section follows both DECLARE GATE and COLLECTOR GATE in document order |
| C-16 | PASS | COLLECTOR consolidates F-00 (OPENING) and F-01+ (CHALLENGE) into Final list with CONFIRMED per row |
| C-17 | PASS | DECLARE GATE (scope: claim + conditions) + COLLECTOR GATE (scope: Final list) — separate checklists, scopes named in section headers |
| C-18 | PASS | `## COLLECTOR: CONSOLIDATE` at peer ## heading level |
| C-19 | PASS | `## OPENING: CURRENT STATE` before DECLARE; status-quo judgment + F-00 generated in OPENING |

Aspirational: **11/11**

**V-02 Score:**
```
essential:    5/5 × 60   = 60.00
recommended:  3/3 × 30   = 30.00
aspirational: 11/11 × 10  = 10.00
composite:  100.00  |  Golden: YES
```

---

### V-03: Lifecycle Emphasis — 7 Phases, INERTIA Before DECLARE

**Essential (C-01–C-05)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" in PHASE 3 |
| C-02 | PASS | F-01/F-02 table in PHASE 3; F-00 in PHASE 2 INERTIA |
| C-03 | PASS | "Value: [N]/100" with two-element rationale in PHASE 6 |
| C-04 | PASS | PHASE 7 NAVIGATE table with prove sub-skills; coverage rule enforced |
| C-05 | PASS | PHASE 3 DECLARE after PHASE 2 INERTIA; GATE 3 prohibits downstream modification |

Essential: **5/5**

**Recommended (C-06–C-08)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | PHASE 1: PRIOR — explicit prior signal scan with "None -- starting fresh" option |
| C-07 | PASS | "Confirmation conditions: CF-01" table in PHASE 3 |
| C-08 | PASS | PHASE 6 confidence rationale requires "prior signal, trace finding, or friction point" |

Recommended: **3/3**

**Aspirational (C-09–C-19)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | "F-IDs tested" column in PHASE 7 table |
| C-10 | PASS | Rank 1 = highest falsification; "Risk rationale" column in PHASE 7 |
| C-11 | PASS | PHASE 4: CHALLENGE — 4A per-condition PASS/REWRITE verdicts; 4B F-00 validation; GATE 4 pre-consolidate check |
| C-12 | PASS | GATE 3: DECLARE LOCK — "LOCKED. PHASES 4-7 may not modify Claim or domain Conditions. Post-lock problems: log as amendment notes in PHASE 7." |
| C-13 | PASS | F-00 born in PHASE 2: INERTIA with observable test |
| C-14 | PASS | "Every F-ID in the PHASE 5 Final list must appear in at least one experiment row. Any F-ID with no experiment row is an explicit failure." |
| C-15 | PASS | PHASE 6: CONFIDENCE follows GATE 3 and GATE 5 in strict phase sequence |
| C-16 | PASS | PHASE 5: CONSOLIDATE merges F-00 (PHASE 2) and F-01+ (PHASE 4A) into Final list with CONFIRMED per condition |
| C-17 | PASS | GATE 3: DECLARE LOCK (freezes claim + domain conditions) + GATE 5: CONSOLIDATE SEAL (freezes Final list) — separate checklists, scopes stated in gate headers |
| C-18 | PASS | `## PHASE 5: CONSOLIDATE` at peer ## heading level |
| C-19 | PASS | `## PHASE 2: INERTIA` before `## PHASE 3: DECLARE`; F-00 born in INERTIA; GATE 2 blocks advancement until current-practice and F-00 candidate are written |

Aspirational: **11/11**

**V-03 Note — structural differentiator:** GATE 2 (required before PHASE 3) explicitly blocks the claim from being written until current practice, status-quo judgment, and F-00 are all populated. This is the only variation where the pre-declare status-quo section has its own gate. Makes C-19 violation a gate failure, not just a structural omission.

**V-03 Score:**
```
essential:    5/5 × 60   = 60.00
recommended:  3/3 × 30   = 30.00
aspirational: 11/11 × 10  = 10.00
composite:  100.00  |  Golden: YES
```

---

### V-04: Phrasing Register — Formal/Technical, Explicit Gate Scope Declarations

**Essential (C-01–C-05)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "Claim: [One declarative sentence. Predicate form: 'X is Y' or 'X will Z'. No hedging.]" |
| C-02 | PASS | F-01/F-02 table in CLAIMANT: DECLARE; F-00 in CLAIMANT: CONTEXT |
| C-03 | PASS | "Confidence Value: [N]/100" with two mandatory rationale elements |
| C-04 | PASS | NAVIGATOR table with experiments and prove sub-skills; coverage rule enforced |
| C-05 | PASS | Claim in DECLARE after CONTEXT; DECLARE GATE (LOCK) prohibits downstream modification |

Essential: **5/5**

**Recommended (C-06–C-08)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | CLAIMANT: CONTEXT — "Document: [list files...or 'None -- starting fresh']" |
| C-07 | PASS | "Confirmation Conditions: CF-01" table in DECLARE |
| C-08 | PASS | Confidence rationale requires "prior signal, trace finding, or named friction point" |

Recommended: **3/3**

**Aspirational (C-09–C-19)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | "F-IDs Tested" column in NAVIGATOR table |
| C-10 | PASS | Rank 1 = highest falsification; "Falsification Risk Rationale" column required |
| C-11 | PASS | SKEPTIC: CHALLENGE — per-condition PASS/REWRITE in Domain Observability table + F-00 Observability subsection with verdict |
| C-12 | PASS | "LOCKED. Claim and Falsification Conditions above are frozen. Modifications prohibited in all downstream sections." |
| C-13 | PASS | F-00 born in CLAIMANT: CONTEXT with observable test before claim is written |
| C-14 | PASS | "Every F-ID in the Final Falsification List must appear in at least one Experiment row. Any F-ID with zero experiment coverage is an explicit failure." |
| C-15 | PASS | CLAIMANT: CONFIDENCE positioned structurally after both DECLARE GATE and CONSOLIDATE GATE |
| C-16 | PASS | ARCHIVIST: CONSOLIDATE collects F-00 (CONTEXT) + F-01+ (CHALLENGE) into Final list; every condition gets CONFIRMED verdict |
| C-17 | PASS | DECLARE GATE (LOCK): "Scope -- freezes Claim and all Falsification Conditions before any adversarial review pass begins" + CONSOLIDATE GATE (SEAL): "Scope -- freezes Final Falsification List after multi-pass consolidation and before Confidence and Navigator are populated" — strongest self-documenting C-17 evidence in the set |
| C-18 | PASS | `## ARCHIVIST: CONSOLIDATE` at peer ## heading level |
| C-19 | PASS | `## CLAIMANT: CONTEXT` before `## CLAIMANT: DECLARE`; F-00 born in CONTEXT |

Aspirational: **11/11**

**V-04 Note — structural differentiator:** Gate scope declarations appear in the gate header text itself ("DECLARE GATE (LOCK): Scope -- freezes X before Y"). A reviewer can confirm non-overlapping dual-gate compliance from the header alone without reading checklists. Strongest C-17 self-documentation.

**V-04 Score:**
```
essential:    5/5 × 60   = 60.00
recommended:  3/3 × 30   = 30.00
aspirational: 11/11 × 10  = 10.00
composite:  100.00  |  Golden: YES
```

---

### V-05: Conversational Register + Inertia-Lead + Named COLLECTOR

**Essential (C-01–C-05)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "Claim: [One sentence. Use 'is' or 'will'. No 'might', no hedging, no compound claims.]" in Step 3 |
| C-02 | PASS | F-01/F-02 as numbered list in Step 3; F-00 in Step 2 |
| C-03 | PASS | "Confidence: [N]/100" with two required elements in Step 5 |
| C-04 | PASS | Step 6 experiment table with prove sub-skills; coverage check enforced |
| C-05 | PASS | Claim in Step 3, after Steps 1-2; first freeze prohibits retroactive edits |

Essential: **5/5**

**Recommended (C-06–C-08)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Step 1: "Prior signals: [...list names...If nothing exists, write 'None found.'"]" |
| C-07 | PASS | "What would confirm you right: CF-01" in Step 3 |
| C-08 | PASS | Step 5 requires "Something from your prior work (signal files, trace findings, known friction)" |

Recommended: **3/3**

**Aspirational (C-09–C-19)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | "F-IDs it tests" column in Step 6 table |
| C-10 | PASS | "Order from most likely to falsify (rank 1) to least"; "Why this rank" column required |
| C-11 | PASS | "A Skeptic reviews each domain condition for observability: F-01 [text]: [PASS -- observable via... / REWRITE -- problem. Revised:]" — named Skeptic, per-condition explicit PASS/REWRITE before first freeze |
| C-12 | PASS | "LOCKED. Your claim and domain conditions above are frozen from this point. Post-lock observability problems: log as amendment notes in Step 6, not edits here." |
| C-13 | PASS | F-00 born in Step 2 with observable test ("How you would know F-00 is true") |
| C-14 | PASS | "COVERAGE CHECK: verify every F-ID from the Step 4 Final list appears under at least one experiment. An F-ID with no experiment is an uncovered blind spot -- add an experiment before completing the artifact." |
| C-15 | PASS | "Write your confidence after both freezes are in effect." — Step 5 explicitly gated |
| C-16 | PASS | Step 4: COLLECTOR assembles F-00 (Step 2) + F-01+ (Step 3) into Final list with CONFIRMED per row |
| C-17 | PASS | First freeze checklist (Step 3, after claim + domain conditions) + second freeze checklist (Step 4, after Final list) — separate checklists, non-overlapping freeze events |
| C-18 | PASS | `## Step 4: COLLECTOR -- Assemble the Final list` at peer ## heading level |
| C-19 | PASS | Steps 1-2 before Step 3; Step 2 explicitly asks "What does the team do today?"; F-00 born in Step 2 |

Aspirational: **11/11**

**V-05 Note — structural differentiator:** Plain-language freeze instructions ("LOCKED. Your claim and domain conditions are frozen.") and colloquially named COLLECTOR step carry the same structural guarantees as formal role-name variations. Demonstrates format-neutrality of the v4 structural pattern.

**V-05 Score:**
```
essential:    5/5 × 60   = 60.00
recommended:  3/3 × 30   = 30.00
aspirational: 11/11 × 10  = 10.00
composite:  100.00  |  Golden: YES
```

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** | YES |
| V-02 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** | YES |
| V-03 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** | YES |
| V-04 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** | YES |
| V-05 | 5/5 (60) | 3/3 (30) | 11/11 (10) | **100** | YES |

**All five variations score 100. All five pass the Golden threshold.**

---

## Excellence Signals

R4 introduced three structural moves that elevated all variations from partial (R3 C-17/C-18/C-19 misses) to perfect coverage. These are the patterns:

**1. F-00 born in pre-declare named section**
Every variation creates a dedicated named section — CONTEXT, OPENING, INERTIA, or numbered Steps 1-2 — that runs before the claim is declared and generates F-00 with current-practice context live. The Skeptic validates F-00; it no longer introduces it. This changes F-00 from an adversarial-pass artifact into a pre-commitment constraint.

**2. Dual-gate with explicit non-overlapping scope text**
Both freeze events have explicit scope declarations: LOCK gate names "freezes claim + domain conditions"; SEAL gate names "freezes Final list." Non-overlapping scopes are stated in gate headers or checklist preamble, not just implied by position. V-04 achieves the strongest variant: scope declared in the gate name itself ("DECLARE GATE (LOCK): Scope -- freezes Claim and all Falsification Conditions before any adversarial review pass begins").

**3. Named consolidation unit at peer heading level — omission becomes visible**
ARCHIVIST (V-01/V-04), COLLECTOR (V-02/V-05), or PHASE 5: CONSOLIDATE (V-03) sits at the same `##` heading level as all other major phases/roles. A model omitting the section omits a visible heading peer, not a hidden subsection. This converts silent-fail omission into explicit-fail absence.

**V-03 structural differentiator (strongest C-19 enforcement):** GATE 2 explicitly blocks PHASE 3 until current practice, status-quo judgment, and F-00 candidate are all written. The pre-declare interrogation phase has its own gate — C-19 violation is a gate failure, not a structural omission.

**V-04 structural differentiator (strongest C-17 self-documentation):** Gate scope declarations appear in the gate header text itself. Dual-gate compliance is verifiable from the header text alone without reading checklists.

---

## Round Rankings

No ranking possible — all five variations tied at 100. The R4 design was fully successful: moving F-00 generation to a pre-declare section fixed C-19 across all axes simultaneously, and the dual-gate + named consolidation patterns were already confirmed in R3 V-03/V-04.

The differentiator question for R5 is **enforcement strength under degenerate conditions**, not score — V-03's gated INERTIA phase and V-04's self-documenting scope headers may show different failure modes under context pressure.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["F-00 born in pre-declare named section (CONTEXT/OPENING/INERTIA/Steps 1-2) — Skeptic validates F-00, does not introduce it", "dual-gate with scope declared in gate header text — LOCK scope='claim+conditions', SEAL scope='Final list', non-overlapping by declaration", "named consolidation unit at peer heading level (ARCHIVIST/COLLECTOR/PHASE N) — missing unit is a visible absent heading, not a silent skipped subsection"]}
```
