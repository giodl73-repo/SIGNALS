Scorecard written. Here is the R6 scoring summary:

---

## narrate-behavior R6 Scoring Results

**All 5 variations: 80/80. Rubric ceiling reached at 15/15 aspirational.**

| Variation | Essential | Recommended | Aspirational | Total | Aspirational Passes |
|-----------|-----------|-------------|--------------|-------|---------------------|
| V-26 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-27 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-28 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-29 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-30 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |

### Open question resolutions

| Question | Verdict |
|----------|---------|
| C-21 + C-22 compose cleanly? | YES — independent targets (table rows vs registry type data), no shared resource |
| Unconditional meta-finding REQUIRE (V-27) satisfies C-22 or exceeds it? | EXCEEDS — C-22 requires the audit table; unconditional REQUIRE is additive |
| V-30 4-outcome disposition introduce C-09/C-14 ambiguity? | NO — COVERED satisfies zero-finding rationale (C-09); INVESTIGATION covers ambiguous-coverage cases, not confirmed underspecification (C-14) |

### Excellence signals (R6)

| Signal | Pattern | Source |
|--------|---------|--------|
| SIGNAL-1 | `unconditional-discovery-pathway-ratio-require` | V-27, V-29, V-30 — promotes conditional observation to structural REQUIRE obligation across all three ratio forms |
| SIGNAL-2 | `exhaustive-inertia-disposition-completeness-check` | V-30 — REQUIRE check that every named INERTIA assumption carries FINDING/COVERED/INVESTIGATION/NONE; aggregate-level completeness |
| SIGNAL-3 | `inertia-disposition-ratio-as-coverage-score` | V-30 — REPORT disposition summary produces a spec-coverage density score (% findings / % covered / % investigation) distinct from SIGNAL-1 |

### Rank

**V-30** (top) > **V-29** > **V-27** > **V-28** > **V-26**. All tied at 80/80; V-30 carries the most excellence signal material.

### v7 candidates

3 new criteria: C-23 (unconditional meta-finding REQUIRE), C-24 (exhaustive inertia disposition REQUIRE), C-25 (inertia disposition coverage score). Aspirational tier grows to 18; threshold should increase to "any 10 of 18."

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["unconditional-discovery-pathway-ratio-require", "exhaustive-inertia-disposition-completeness-check", "inertia-disposition-ratio-as-coverage-score"]}
```
C-11 Exit Gate Per Sub-Skill Section | PASS | All 5 sections carry uniform condensed EXIT GATE: Spec-gaps / Violations / Inertia / B-IDs / Disposition. Spec-gap and violation F-ID fields explicit in all sections. |
| C-12 Report-Level Post-Conditions | PASS | REQUIRE block: 3+ sub-skills, 1+ spec-gap/violation with location, blast-radius sort confirmed, 2+ downstream non-NONE B-IDs, all Inertia F-IDs as spec-gap, 2+ registry entries with type labels, S1-S2 findings show text-name (B-NN), DISCOVERY PATHWAY AUDIT populated with 1+ row per non-empty type. |
| C-13 Downstream-Anchored Simulation | PASS | S3-S5 INERTIA blocks: "identify which BOUNDARY REGISTRY entry (B-ID and name) each pattern assumes or crosses." EXIT GATE B-IDs field enumerates B-IDs referenced in downstream findings. Named boundary references, not section-number citations. |
| C-14 Inertia-as-Spec-Gap Mapping | PASS | Inertia conversion rule mandates (a) status-quo behavior in Impact, (b) spec location, (c) "B-NN: [name]" for S3-S5 / text-name for S1-S2 in Location. EXIT GATE Inertia F-ID field in all 5 sections enforces mapping. |
| C-15 Boundary Registry as Structural Artifact | PASS | BOUNDARY REGISTRY positioned between S2 and S3. Compact format B-NN: name -- type -- description. Minimum 2 entries. S3-S5 EXIT GATE B-IDs field explicitly enumerates referenced B-IDs. |
| C-16 Inertia-Boundary Cross-Reference | PASS | S3-S5 INERTIA blocks "open by naming which B-ID and boundary name the status-quo behavior assumes" (stated in preamble). Resulting observation enters FINDING TABLE as spec-gap with B-ID in Location. |
| C-17 Structural Column Independence | PASS | Blast Radius and Severity are separate named columns in FINDING TABLE. No combined column. Column rules define each independently. |
| C-18 Boundary Registry Type Field | PASS | BOUNDARY REGISTRY format: B-NN: [name] -- [contract-boundary / permission-grant / inertia-boundary] -- [description]. Three types defined in DEFINITIONS. REQUIRE enforces 2+ entries with type labels. |
| C-19 Pre-Registry Inertia Discovery Pipeline | PASS | S1-S2 INERTIA blocks name boundaries by text-name as "candidates for BOUNDARY REGISTRY as inertia-boundary entries." Registry compiles text-names to B-IDs. S3-S5 cite B-IDs traceable to S1-S2 text-names. Full two-phase pipeline. C-19 pass condition (text-name in S1-S2 at discovery time) unaffected by BACK-ANNOTATE. |
| C-20 Dual-Purpose B-IDs Exit Gate Field | PASS | Uniform 5-field EXIT GATE across all sections. DEFINITIONS: "EXIT GATE B-IDs field -- dual-purpose semantics: S1-S2 (upstream, pre-registry): list boundaries to register; S3-S5 (downstream, post-registry): list B-IDs referenced." Dual-purpose semantics explicitly documented. |
| C-21 Back-Annotation of S1-S2 Findings | PASS | BACK-ANNOTATE step positioned after BOUNDARY REGISTRY, before S3. Targets FINDING TABLE rows only: "update Location to text-name (B-NN) format." Explicit rule: "FINDING TABLE rows only -- EXIT GATE content is unchanged." REQUIRE enforces: "All S1-S2 findings referencing registered boundaries show text-name (B-NN) in Location." |
| C-22 Discovery Pathway Audit in REPORT | PASS | DISCOVERY PATHWAY AUDIT table in REPORT with all 4 required columns: Registry Type, B-IDs, Finding Count, F-IDs. Three registry types as rows. Discovery signal observation conditional on ratio. REQUIRE: "DISCOVERY PATHWAY AUDIT populated with at least 1 row per non-empty registry type." |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 15/15 passes -- cap earned: 10/10
**V-26 Total: 80/80**

Composition verdict (C-21 + C-22): CLEAN -- BACK-ANNOTATE targets FINDING TABLE rows; DISCOVERY PATHWAY AUDIT reads registry type data; no shared resource. The two operations are fully independent.

---

### V-27 -- REQUIRE-enforced meta-finding

Base: V-26 + unconditional discovery-pathway-ratio REQUIRE in DEFINITIONS and REPORT.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-20 | PASS | All criteria from V-26 inherited intact. Same sequence, same FINDING TABLE, same EXIT GATE format, same BACK-ANNOTATE, same DISCOVERY PATHWAY AUDIT structure. |
| C-21 | PASS | BACK-ANNOTATE step unchanged from V-26. Same FINDING TABLE rows-only target and REQUIRE check. |
| C-22 | PASS | DISCOVERY PATHWAY AUDIT table present with all 4 columns. V-27 exceeds C-22 pass condition: adds discovery-pathway-ratio rule in DEFINITIONS with three explicit forms (a/b/c), all required. REQUIRE check added: "Discovery-pathway-ratio meta-finding statement present -- required regardless of ratio direction." C-22 requires the audit table; V-27 additionally requires an unconditional meta-finding statement. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 15/15 -- cap 10/10
**V-27 Total: 80/80**

Distinguishing addition vs V-26: Discovery-pathway-ratio rule in DEFINITIONS elevates V-26 conditional signal observation to an unconditional REQUIRE obligation. All three ratio directions (inertia > contract / contract > inertia / equal) produce required statements. Equality is also a signal. New pattern candidate: unconditional-discovery-pathway-ratio-require.

---

### V-28 -- Permissions-first role sequence

Base: V-26 + swapped S1/S2 (S1=trace-permissions, S2=trace-contract). Conditional meta-finding retained.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Declared sequence updated: S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT. Sections follow declared order. |
| C-02--C-12 | PASS | All inherited from V-26. FINDING TABLE schema, EXIT GATE format, DEFINITIONS unchanged. REQUIRE block includes all V-26 checks; no meta-finding REQUIRE (conditional only). |
| C-13 | PASS | S3-S5 INERTIA and SIMULATE cite B-IDs. S3 INERTIA: "Permission-layer boundaries (from S1) and contract boundaries (from S2) are both valid reference targets." Named B-ID citations present. |
| C-14 | PASS | Inertia conversion rule unchanged. INERTIA blocks in both S1 (trace-permissions) and S2 (trace-contract) apply conversion rule identically. |
| C-15 | PASS | BOUNDARY REGISTRY between S2 and S3 (S2 is now trace-contract; position invariant). Note: "B-ID numbering follows declaration order (S1 first, S2 second) regardless of type." Minimum 2 entries. |
| C-16 | PASS | S3-S5 INERTIA blocks cite B-IDs. Registry contains permission-grant and contract-boundary entries from swapped S1/S2. Cross-reference intact. |
| C-17--C-20 | PASS | Column independence, registry type labels, two-phase pipeline, dual-purpose B-IDs all inherited. C-20 dual-purpose semantics depend on section position (S1-S2 upstream / S3-S5 downstream), not sub-skill name -- symmetric across role swap. |
| C-21 | PASS | BACK-ANNOTATE step unchanged. S1 (trace-permissions) and S2 (trace-contract) FINDING TABLE rows updated with B-IDs. EXIT GATE content not modified. |
| C-22 | PASS | DISCOVERY PATHWAY AUDIT table present with all 4 columns. Conditional discovery signal retained. Permissions-first note added to REPORT: "Note whether permission-first ordering changed registry composition relative to the standard contract-first baseline." |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 15/15 -- cap 10/10
**V-28 Total: 80/80**

Permissions-first structural analysis: Role swap changes which sub-skill executes at S1/S2 positions but does not alter any structural criterion. C-20 dual-purpose semantics depend on section position, not sub-skill identity. BOUNDARY REGISTRY numbering note is the only structural addition required.

---

### V-29 -- Combo: REQUIRE meta-finding + permissions-first

Base: V-27 (unconditional meta-finding REQUIRE) + V-28 (permissions-first ordering). No new structural additions beyond the two combined axes.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Declared sequence: S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT. |
| C-02--C-20 | PASS | All criteria from V-28 inherited. Discovery-pathway-ratio rule added from V-27 (three forms, unconditional REQUIRE). |
| C-21 | PASS | BACK-ANNOTATE step present and unchanged. FINDING TABLE rows only; EXIT GATE content not modified. |
| C-22 | PASS | DISCOVERY PATHWAY AUDIT table with all 4 columns. Unconditional meta-finding REQUIRE: "Discovery-pathway-ratio meta-finding statement present -- required regardless of ratio direction." Exceeds C-22 pass condition. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 15/15 -- cap 10/10
**V-29 Total: 80/80**

Combination verdict: V-27 and V-28 compose cleanly. No new structural risk. The unconditional meta-finding REQUIRE is more information-dense when permissions-first ordering increases inertia-boundary entry count.

---

### V-30 -- Combo: all three axes + enhanced inertia framing

Base: V-29 + 4-outcome exhaustive inertia disposition (FINDING / COVERED / INVESTIGATION / NONE) per assumption in all INERTIA blocks.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Declared sequence: S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT. |
| C-02--C-07 | PASS | All inherited from V-29 intact. |
| C-08 | PASS | Severity scale defined in DEFINITIONS. Named column in FINDING TABLE. INVESTIGATION findings still carry severity. |
| C-09 | PASS | EXIT GATE Disposition field present in all 5 sections. COVERED dispositions clarify zero-finding rationale -- satisfies "rationale if zero" requirement. INVESTIGATION produces observation-type finding (non-empty disposition). |
| C-10 | PASS | FINDING TABLE schema pre-committed before S1. Impact column rule updated: "inertia FINDING dispositions name status-quo behavior as comparison point; INVESTIGATION dispositions state spec coverage uncertainty." Both produce valid Impact content. Schema structure unchanged. |
| C-11 | PASS | All 5 sections carry uniform EXIT GATE. 4-outcome disposition applies within INERTIA blocks, not to EXIT GATE structure. EXIT GATE format unchanged from V-29. |
| C-12 | PASS | REQUIRE block inherits all V-29 checks plus: "Every INERTIA assumption named in any section carries one of: FINDING / COVERED / INVESTIGATION / NONE disposition; no unnamed assumption exits the report." Additive post-condition. |
| C-13 | PASS | S3-S5 INERTIA blocks open by identifying B-ID and name, then apply 4-outcome disposition. B-ID citation precedes disposition selection -- named upstream reference preserved for C-13 compliance. |
| C-14 | PASS | FINDING dispositions (spec-silent) produce spec-gap with status-quo in Impact and B-ID in Location -- C-14 fully satisfied. COVERED (spec addresses assumption) produces no finding -- correct, no underspecification. INVESTIGATION (coverage ambiguous) produces observation -- appropriate because spec absence not confirmed. Mandatory spec-gap conversion path preserved via FINDING disposition. |
| C-15 | PASS | BOUNDARY REGISTRY between S2 and S3. Note: "inertia-boundary entries mark boundaries surfaced through assumption analysis (FINDING and INVESTIGATION dispositions in S1-S2 INERTIA blocks)." |
| C-16 | PASS | S3-S5 INERTIA blocks: "open by identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then apply 4-outcome disposition." FINDING dispositions produce spec-gap with B-ID in Location -- C-16 pass condition satisfied. |
| C-17 | PASS | Blast Radius and Severity remain separate named columns in FINDING TABLE. |
| C-18 | PASS | Registry type field present. BOUNDARY REGISTRY note clarifies INVESTIGATION dispositions also produce inertia-boundary candidates. |
| C-19 | PASS | Two-phase pipeline intact. S1-S2 INERTIA 4-outcome dispositions name boundaries by text-name for FINDING, COVERED, and INVESTIGATION outcomes. Registry promotes to B-IDs. S3-S5 cite B-IDs. |
| C-20 | PASS | Uniform EXIT GATE with dual-purpose B-IDs semantics documented. 4-outcome disposition does not alter EXIT GATE structure. |
| C-21 | PASS | BACK-ANNOTATE step unchanged. FINDING TABLE rows updated with "text-name (B-NN)". EXIT GATE not modified. |
| C-22 | PASS | DISCOVERY PATHWAY AUDIT table with all 4 columns. Unconditional meta-finding REQUIRE. REPORT adds "Inertia disposition summary: [count of FINDING / COVERED / INVESTIGATION / NONE across all 5 sections]" -- new structural output class beyond C-22 requirements. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 15/15 -- cap 10/10
**V-30 Total: 80/80**

4-outcome disposition structural analysis: INVESTIGATION dispositions produce observation-type findings, not spec-gap. This is the only new finding type introduced. C-14 unviolated because INVESTIGATION covers ambiguous-coverage cases (spec presence uncertain, not confirmed-absent underspecification). C-09 satisfied because COVERED gives an explicit zero-finding rationale. Inertia disposition summary in REPORT is a new output class: a spec-coverage completeness score across all 5 sections.

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Aspirational Passes |
|-----------|-----------|-------------|--------------|-------|---------------------|
| V-26 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-27 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-28 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-29 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |
| V-30 | 40/40 | 30/30 | 10/10 | **80/80** | 15/15 |

R6 rubric fully saturated. All five variations pass all 22 criteria. Rubric ceiling reached at 15/15 aspirational.

---

## Rank

All variations tie at 80/80. Secondary differentiation by structural enforcement strength and excellence signal contribution:

1. **V-30** (top) -- All three axes + enhanced inertia framing. Two new excellence signal candidates (exhaustive disposition completeness check; inertia disposition summary as coverage score). Tightest inertia obligation enforcement: inline per-assumption disposition eliminates the lookup path from section instruction to DEFINITIONS rule.
2. **V-29** -- Permissions-first + unconditional meta-finding REQUIRE. V-30 without the 4-outcome framing overhead.
3. **V-27** -- Contract-first + unconditional meta-finding REQUIRE. SIGNAL-1 candidate with minimal structural change from V-26.
4. **V-28** -- Permissions-first + conditional meta-finding. Structural symmetry confirmed: permissions-first does not break any criterion.
5. **V-26** -- Back-annotation integration baseline. Clean synthesis of C-21 + C-22; all 15 aspirational pass confirmed; baseline for all R6 work.

---

## Excellence Signals (R6)

### SIGNAL-1 -- unconditional-discovery-pathway-ratio-require (V-27, V-29, V-30)

V-26 has a conditional discovery signal: "If inertia > contract: state this observation explicitly." V-27 promotes this to an unconditional REQUIRE with three explicit forms (a/b/c) in DEFINITIONS, all required regardless of ratio direction. REQUIRE block enforces: "Discovery-pathway-ratio meta-finding statement present." Key structural insight: equality is also a signal (proportional spec-coverage surface), and contract-dominant topics are as informative as inertia-dominant ones. Unconditional obligation converts V-25 SIGNAL-3 from a conditional observation into a structural post-condition. New pattern: unconditional meta-finding enforcement for ratio-based structural analysis.

### SIGNAL-2 -- exhaustive-inertia-disposition-completeness-check (V-30)

V-30 adds a REQUIRE check: "Every INERTIA assumption named in any section carries one of: FINDING / COVERED / INVESTIGATION / NONE disposition; no unnamed assumption exits the report." This completeness check operates at the aggregate level -- every named assumption must have a recorded disposition, not just the ones that produce findings. Mirrors how V-25 added a REQUIRE check for C-18 type data: the check is output-verifiable, not just structurally implied. New pattern: per-assumption exhaustive disposition with aggregate REQUIRE enforcement.

### SIGNAL-3 -- inertia-disposition-ratio-as-coverage-score (V-30)

V-30 REPORT adds "Inertia disposition summary: [count of FINDING / COVERED / INVESTIGATION / NONE across all 5 sections]." The FINDING/(FINDING+COVERED) ratio is a spec-coverage density score for the INERTIA analysis pass. For a given topic: "X% of assumptions produced findings (spec-silent), Y% were spec-covered, Z% require investigation." This is a new output class -- distinct from SIGNAL-1 (which compares inertia-boundary vs contract-boundary finding counts across discovery pathways). SIGNAL-3 measures coverage quality within the inertia analysis pass itself. New pattern: inertia-disposition-ratio-as-spec-coverage-density-score.

---

## Open Question Resolutions

| Question | Verdict |
|----------|---------|
| Do C-21 + C-22 compose cleanly? | CONFIRMED YES -- V-26 demonstrates clean composition. BACK-ANNOTATE targets FINDING TABLE rows; DISCOVERY PATHWAY AUDIT reads registry type data. No shared resource. Both REQUIRE checks pass simultaneously. |
| Does unconditional meta-finding REQUIRE (V-27) satisfy C-22 or exceed it? | CONFIRMED EXCEEDS -- C-22 requires the audit table with 4 columns + 2 types. V-27 unconditional REQUIRE is additive above C-22. New excellence signal SIGNAL-1. |
| Does permissions-first ordering change registry type composition empirically? | STRUCTURALLY VERIFIED; empirical result is topic-dependent. V-28 adds permissions-first note prompting executor to compare against contract-first baseline. Structural rubric criteria unaffected by ordering. |
| Does V-30 4-outcome disposition introduce C-09/C-14 ambiguity? | CONFIRMED NO -- C-09: COVERED gives explicit zero-finding rationale. INVESTIGATION produces observation-type finding (non-empty disposition). C-14: FINDING dispositions preserve mandatory spec-gap conversion path. INVESTIGATION covers ambiguous-coverage cases, not confirmed underspecification. |
| Does REQUIRE check for exhaustive inertia disposition constitute a new excellence signal? | CONFIRMED YES -- SIGNAL-2: per-assumption completeness enforcement at aggregate level. |
| Does the inertia disposition summary constitute a new structural output class? | CONFIRMED YES -- SIGNAL-3. Distinct from SIGNAL-1; measures coverage quality within the inertia pass. |

---

## Rubric Ceiling Analysis

R6 rubric is fully saturated. All 15 aspirational criteria satisfiable simultaneously confirmed by all five R6 variations. 80/80 achievable by any variation carrying the V-26 baseline.

Candidates for v7 from R6 excellence signals:
- C-23 from SIGNAL-1: unconditional-discovery-pathway-ratio-require -- REQUIRE check mandating meta-finding statement for all three ratio directions, regardless of which pathway dominates
- C-24 from SIGNAL-2: exhaustive-inertia-disposition-completeness-check -- REQUIRE check that every INERTIA assumption named in any section carries one of FINDING / COVERED / INVESTIGATION / NONE
- C-25 from SIGNAL-3: inertia-disposition-ratio-as-coverage-score -- REPORT produces aggregate disposition count (FINDING/COVERED/INVESTIGATION/NONE) as a spec-coverage density score for the inertia analysis pass

Tier rebalancing for v7: Adding C-23 through C-25 yields 18 aspirational criteria. Threshold should increase to "any 10 of 18" to maintain structural challenge proportional to "any 8 of 15."

---

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["unconditional-discovery-pathway-ratio-require", "exhaustive-inertia-disposition-completeness-check", "inertia-disposition-ratio-as-coverage-score"]}
```