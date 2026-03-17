Reading the scorecard carefully to extract the V-05 excellence signals before writing the rubric.

From the scorecard:

- **V-03** establishes that COUNT RECONCILIATION CHECK is insufficient — it detects ID count overflow but not ID substitution (wrong IDs that happen to number correctly).
- **V-05** axis label is "COUNT COMPLETENESS CHECK + expanded inertia" — two distinct patterns beyond V-04.

**C-30 — COUNT COMPLETENESS CHECK**: closes the ID-substitution attack vector V-03 leaves open. Not just count equality, but per-ID membership verification: each ID cited in the EVIDENCE ANCHOR is cross-checked against Step 3b row labels, confirming the cited ID exists as an actual row key.

**C-31 — Expanded bidirectional annotation (inertia)**: V-02 introduced a single bidirectional annotation on the PROMOTION COMPLETENESS GATE ("SA remaining (certified): R — forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY"). V-05 expands this pattern to all forward-referencing blocks in the trace, making C-26 through C-29 self-certifying for future inheritance without re-inspection.

Grand total: 103.5 + 0.5 + 0.5 = **104.5**

---

```markdown
# Trace-Inspect Rubric — v10

**Skill**: `trace-inspect`
**Version**: v10 (updated from v9 — added C-30 and C-31 from R13 excellence signals;
aspirational block: C-09 and C-10 at 2 pts each; C-11 through C-31 at 0.5 pts each;
grand total 104.5)
**Applies to**: Trace outputs produced by any variation of the trace-inspect skill
**Scoring**: 104.5-point composite. Golden threshold: all 5 essential criteria pass AND
composite >= 80.

---

## Coverage Matrix

| Schema | Declared Elements                                              | Invariant                                              |
|--------|----------------------------------------------------------------|--------------------------------------------------------|
| Schema 1 | Severity labels: {P1, P2, P3}                              | No other severity value anywhere in the trace          |
| Schema 2 | Source labels: {SA, SG, EG, QO}                            | No other source value anywhere in the trace            |
| Schema 3 | Lifecycle events: Stage 1 relay, SA-TO-SG PROMOTION, Stage 2 relay | Events occur in declared order                  |
| Schema 4 | Enforcement gates: G-1, G-2, G-3                           | All three checked at Step 3c; no gate skipped          |
| Schema 5 | Phase 3 sub-steps: 3a → 3b → 3c → 3d                      | Sub-steps run in declared order with transition confirmation |

---

## Essential Criteria

> All five must pass for the trace to be useful. A single essential failure makes the trace
> non-golden regardless of score.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Phase completeness** | essential | correctness | All four phases are present and structurally closed. Phase 1 (Setup) produces per-role schema binding blocks with explicit Schema 1 and Schema 2 binding fields and per-role gap attribution. Phase 2 (Execute) runs at least one role relay. Phase 3 (Findings) runs all four sub-steps in order (3a → 3b → 3c → 3d). Phase 4 (Amend) produces at least one change or dismissal entry. A trace missing any phase, or a phase present but producing no required output, fails. |
| C-02 | **Artifact produced** | essential | correctness | Phase 2 (Execute) writes a hand-compiled artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md` (or equivalent declared path). The artifact contains every section the skill's artifact contract requires. An Execute phase that produces role relays without a written artifact fails. |
| C-03 | **Schema 1 + Schema 2 compliance** | essential | correctness | Every severity label used anywhere in the trace is from {P1, P2, P3}. Every Source label used anywhere in the trace is from {SA, SG, EG, QO}. A promoted SA gap uses the SG label in all phases after SA-TO-SG PROMOTION. Any label outside these sets, or a promoted gap retaining SA, is a structural violation and fails this criterion. |
| C-04 | **Enforcement gates checked** | essential | behavior | Step 3c records an explicit PASS or FAIL result for each of G-1, G-2, and G-3. G-1: >= 2 distinct Source types in Step 3b table. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. A trace where any gate is omitted, implicitly assumed to pass, or advanced past despite a FAIL result fails this criterion. |
| C-05 | **Verdict present and classified** | essential | correctness | Phase 5 (or Verdict section) delivers one of three classifications: USEFUL, NEEDS-REDESIGN, or NEEDS-SPEC-REVISION, with the decision rationale. The classification follows the defined rules: NEEDS-SPEC-REVISION if any P1 SA gap remains SA after promotion; NEEDS-REDESIGN if EG gaps exceed 3 and indicate a structural role gap; USEFUL otherwise. A trace ending without a verdict, or with a verdict that contradicts the gap inventory, fails. |

---

## Recommended Criteria

> Output is better with these. Failing one degrades quality but does not make the trace
> useless.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **SA-TO-SG promotion evaluated** | recommended | depth | Every SA gap from the Stage 1 relay is evaluated at the SA-TO-SG PROMOTION lifecycle event. Each gap records PROMOTES TO SG or REMAINS SA with a one-sentence reason. The post-promotion inventory states SA remaining count and SG from promotion count. A trace with SA gaps that skip this evaluation, or where all SA gaps silently disappear without a promotion record, fails this criterion. |
| C-07 | **Per-role relays complete** | recommended | coverage | Each role in the execution sequence has a relay in Phase 2 with all required fields: Received from, Received values, Schema 2 compliance (Source labels used and YES/NO conformance), SA/SG gaps affecting this role, Produced (artifact content added), EG gaps encountered. A relay missing the "Schema 2 compliance" field, or a relay summarized as "role ran normally" without field-level detail, fails this criterion. |
| C-08 | **Findings table depth** | recommended | depth | The Step 3b findings table contains >= 3 distinct findings covering at least 2 different Source types. Each finding has a distinct Action (not a restatement of the finding). A table with only spec-layer (SA) findings or only execution-layer (EG) findings, or with Action cells that repeat the Finding text verbatim, fails this criterion. |

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable. C-09 and C-10 were present in v1.
> C-11, C-12, and C-13 were added in v2 from R1 excellence signals. C-14 was added in v3 from
> R2 signals. C-15 through C-18 were added in v4 from R6 signals. C-19 through C-21 were added
> in v5 from R7 signals. C-22 and C-23 were added in v6 from R9 excellence signals. C-24 and
> C-25 were added in v7 from R10 excellence signals (V-05 structural linkage moves exceeding the
> base combination of C-22 + C-23). C-26 and C-27 were added in v8 from R11 excellence signals:
> C-26 from the NEEDS-REDESIGN EVIDENCE ANCHOR pattern (V-01/V-04/V-05 in R11) and C-27 from
> the PROMOTION COMPLETENESS GATE pattern (V-02/V-04/V-05 in R11). C-28 and C-29 were added in
> v9 from R12 excellence signals: C-28 from the VERDICT-TO-TABLE TRACEABILITY pattern
> (V-01/V-04 in R12 — when the verdict enumerates EG finding IDs under C-26, each cited ID must
> resolve to a specific Step 3b row) and C-29 from the PROMOTION COUNT FORWARD-REFERENCE pattern
> (V-02/V-04 in R12 — when both C-26 and C-27 are satisfied, the Phase 5 evidence summary must
> carry the SA remaining count from the promotion arithmetic alongside the EG count). C-30 and
> C-31 are new in v10, extracted from R13 excellence signals: C-30 from the COUNT COMPLETENESS
> CHECK pattern (V-05 in R13 — the EVIDENCE ANCHOR block must perform per-ID membership
> verification against Step 3b row labels, closing the ID-substitution attack vector that
> COUNT RECONCILIATION CHECK leaves open) and C-31 from the EXPANDED BIDIRECTIONAL ANNOTATION
> pattern (V-05 in R13 — the bidirectional annotation introduced on the PROMOTION COMPLETENESS
> GATE in R11 is extended to all forward-referencing blocks in the trace, making C-26 through
> C-29 self-certifying for future inheritance).

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | *(aspirational — see v1)* | 2 | aspirational | *(pass condition unchanged from v1)* |
| C-10 | *(aspirational — see v1)* | 2 | aspirational | *(pass condition unchanged from v1)* |
| C-11 | *(aspirational — see v2)* | 0.5 | aspirational | *(pass condition unchanged from v2)* |
| C-12 | *(aspirational — see v2)* | 0.5 | aspirational | *(pass condition unchanged from v2)* |
| C-13 | *(aspirational — see v2)* | 0.5 | aspirational | *(pass condition unchanged from v2)* |
| C-14 | *(aspirational — see v3)* | 0.5 | aspirational | *(pass condition unchanged from v3)* |
| C-15 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-16 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-17 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-18 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-19 | *(aspirational — see v5)* | 0.5 | aspirational | *(pass condition unchanged from v5)* |
| C-20 | *(aspirational — see v5)* | 0.5 | aspirational | *(pass condition unchanged from v5)* |
| C-21 | *(aspirational — see v5)* | 0.5 | aspirational | *(pass condition unchanged from v5)* |
| C-22 | *(aspirational — see v6)* | 0.5 | aspirational | *(pass condition unchanged from v6)* |
| C-23 | *(aspirational — see v6)* | 0.5 | aspirational | *(pass condition unchanged from v6)* |
| C-24 | *(aspirational — see v7)* | 0.5 | aspirational | *(pass condition unchanged from v7)* |
| C-25 | *(aspirational — see v7)* | 0.5 | aspirational | *(pass condition unchanged from v7)* |
| C-26 | **NEEDS-REDESIGN evidence anchor** | 0.5 | aspirational | When the verdict classification is NEEDS-REDESIGN, the Phase 5 verdict section contains a NEEDS-REDESIGN EVIDENCE ANCHOR block that enumerates the specific EG finding IDs from Step 3b that drove the classification, with a count of EG findings cited. A NEEDS-REDESIGN verdict that states only the count or restates the classification rationale without citing specific finding IDs fails this criterion. |
| C-27 | **Promotion completeness gate** | 0.5 | aspirational | The SA-TO-SG PROMOTION block closes with a PROMOTION COMPLETENESS GATE that explicitly certifies: (a) all SA gaps from Stage 1 have been evaluated, (b) the SA remaining count after promotion, and (c) the SG from promotion count. The gate must be a named block, not inline text within the promotion evaluation. A trace where promotion arithmetic is present but uncertified — counts visible but not asserted as complete — fails this criterion. |
| C-28 | **Verdict-to-table traceability** | 0.5 | aspirational | When the verdict enumerates EG finding IDs under C-26, the Phase 5 verdict section contains a VERDICT-TO-TABLE TRACEABILITY sub-table with one row per cited ID, each row recording: cited ID, the corresponding Step 3b finding excerpt, Source, and Severity. The classification is explicitly blocked if any cited ID lacks a resolution row. A verdict block that lists EG IDs in prose or in a count-only check without this per-ID resolution sub-table fails this criterion. A COUNT RECONCILIATION CHECK (comparing Step 3b EG row count to EVIDENCE ANCHOR list length) does not satisfy this criterion: count equality does not detect ID substitution (cited IDs that number correctly but do not match actual Step 3b row labels). |
| C-29 | **Promotion count forward-reference** | 0.5 | aspirational | When both C-26 and C-27 are satisfied, the Phase 5 verdict section contains a VERDICT EVIDENCE SUMMARY block co-locating two rows: (a) EG count sourced from the EVIDENCE ANCHOR list and (b) SA remaining count sourced from the PROMOTION COMPLETENESS GATE. Both classification inputs must appear in the same named block so the verdict is self-contained without requiring re-inspection of Phase 2. A trace where SA remaining is visible in the PROMOTION COMPLETENESS GATE but not carried forward into Phase 5 fails this criterion. |
| C-30 | **Count completeness check** | 0.5 | aspirational | The NEEDS-REDESIGN EVIDENCE ANCHOR block contains a COUNT COMPLETENESS CHECK that performs per-ID membership verification: each ID cited in the EVIDENCE ANCHOR list is individually cross-checked against the Step 3b findings table row labels, confirming the cited ID exists as an actual row key. The check must be auditable ID by ID — enumerating each cited ID and its resolution status — not merely asserting count equality between Step 3b EG rows and ANCHOR list length. A block that states "Step 3b EG rows = N, ANCHOR list length = N, match" without enumerating the ID-to-row mapping fails this criterion, as count equality cannot detect ID substitution (a model may cite F-03 when Step 3b has F-02 and the counts still match). |
| C-31 | **Expanded bidirectional annotation** | 0.5 | aspirational | Every block in the trace that forward-references another block carries an explicit inline annotation of the form "forward-referenced in [block name]" (or equivalent), and the referenced target block carries a corresponding back-reference annotation identifying its source block. This bidirectional annotation must cover at minimum: the PROMOTION COMPLETENESS GATE annotating its SA remaining count as forward-referenced in the Phase 5 VERDICT EVIDENCE SUMMARY, the NEEDS-REDESIGN EVIDENCE ANCHOR annotating its EG finding IDs as resolved in the VERDICT-TO-TABLE TRACEABILITY sub-table, and the VERDICT-TO-TABLE TRACEABILITY sub-table annotating its source as the Step 3b findings table. A trace where any qualifying forward-reference or back-reference annotation is absent fails this criterion. Bidirectional annotation makes C-26 through C-29 self-certifying for future round inheritance: a reviewer can confirm each criterion is met from the annotation alone without re-tracing the full document. |
```
