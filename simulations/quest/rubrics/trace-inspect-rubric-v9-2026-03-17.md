Reading the scorecard, I can see two candidacy signals in the R12 data:

- **C-26** (V-01 axis) passes, but the V-04 C-05 evidence note reveals a richer pattern: when the verdict enumerates EG finding IDs, those IDs should be traceable back to specific rows in the Step 3b findings table — a **verdict-to-table traceability** requirement not captured by C-26 alone.
- **C-27** (V-02 axis) passes, but the combined V-04 observation implies a missing bridge: when both C-26 and C-27 are satisfied, the verdict should pull the SA remaining count from the promotion arithmetic closure into its evidence summary alongside the EG count — a **promotion count forward-reference** not captured by either C-26 or C-27 alone.

These become **C-28** and **C-29**. Grand total moves to **103.5 pts**.

---

```markdown
# Trace-Inspect Rubric — v9

**Skill**: `trace-inspect`
**Version**: v9 (updated from v8 — added C-28 and C-29 from R12 excellence signals;
aspirational block: C-09 and C-10 at 2 pts each; C-11 through C-29 at 0.5 pts each;
grand total 103.5)
**Applies to**: Trace outputs produced by any variation of the trace-inspect skill
**Scoring**: 103.5-point composite. Golden threshold: all 5 essential criteria pass AND
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
> the PROMOTION COMPLETENESS GATE pattern (V-02/V-04/V-05 in R11). C-28 and C-29 are new in v9,
> extracted from R12 excellence signals: C-28 from the VERDICT-TO-TABLE TRACEABILITY pattern
> (V-01/V-04 in R12 — when the verdict enumerates EG finding IDs under C-26, each cited ID must
> resolve to a specific Step 3b row) and C-29 from the PROMOTION COUNT FORWARD-REFERENCE pattern
> (V-02/V-04 in R12 — when both C-26 and C-27 are satisfied, the Phase 5 evidence summary must
> carry the SA remaining count from the promotion arithmetic alongside the EG count).

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Compliance ledger populated** | 2 pts | correctness | Phase 5 includes the full VC compliance ledger (VC-1 through VC-5) with one row per usage site declared in the Coverage Matrix. The "Observed behavior" cell names specific values, label lists, or invariant results — it does not say "as expected." All VC overall results are stated. A trace with a verdict but no compliance ledger, or a ledger with generic "as expected" observations, fails this criterion. |
| C-10 | **Schema 5 sub-step transition confirmations** | 2 pts | behavior | Each Phase 3 sub-step boundary (3a→3b, 3b→3c, 3c→3d) includes an explicit Schema 5 transition sentence confirming the completed sub-step and declaring the next valid to begin (e.g., "Schema 5 transition: Step 3a complete. Step 3b is valid to begin."). A trace with sub-step transitions that lack this confirmation sentence, or where sub-steps are separated by prose rather than named transition statements, fails this criterion. |
| C-11 | **Gate clearance summary blocks** | 0.5 pts | behavior | A GATE CLEARANCE SUMMARY block appears between Step 3c and Step 3d, summarizing the PASS/FAIL result for each of G-1, G-2, and G-3. A PHASE 4 GATE CLEARANCE SUMMARY block appears at Phase 4 (Amend) entry. A trace missing either block, or one that folds gate summaries into prose rather than discrete named blocks, fails this criterion. |
| C-12 | **Remediation log with exemption clause** | 0.5 pts | behavior | If any enforcement gate (G-1, G-2, or G-3) fails at Step 3c, a REMEDIATION LOG block records each failing gate's ID, failure cause, and remediation action taken before Step 3d proceeds. If all gates pass on first evaluation, a C-12 EXEMPTION clause is present confirming no remediation log is required. A trace with a gate failure and no REMEDIATION LOG, or a trace with no failures that omits the C-12 EXEMPTION clause, fails this criterion. |
| C-13 | **Schema 5 prerequisite verification lines** | 0.5 pts | behavior | Each Phase 3 sub-step includes a Schema 5 prerequisite verification line at its entry point confirming the prior sub-step is complete before the current sub-step begins (e.g., "Schema 5 prerequisite: Step 3a complete."). A trace where any sub-step begins without a prerequisite verification line fails this criterion. |
| C-14 | *(v3 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v3 addition.)* |
| C-15 | *(v4 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v4 addition.)* |
| C-16 | *(v4 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v4 addition.)* |
| C-17 | *(v4 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v4 addition.)* |
| C-18 | *(v4 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v4 addition.)* |
| C-19 | *(v5 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v5 addition.)* |
| C-20 | *(v5 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v5 addition.)* |
| C-21 | *(v5 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v5 addition.)* |
| C-22 | *(v6 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v6 addition.)* |
| C-23 | *(v6 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v6 addition.)* |
| C-24 | *(v7 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v7 addition.)* |
| C-25 | *(v7 aspirational — criterion text preserved from prior version)* | 0.5 pts | — | *(Pass condition unchanged from v7 addition.)* |
| C-26 | **NEEDS-REDESIGN evidence anchor** | 0.5 pts | correctness | When the Phase 5 verdict classification is NEEDS-REDESIGN, the verdict names each contributing EG finding by its Step 3b finding ID (e.g., EG-01, EG-03) in an explicit list. The stated EG count is derived by counting the named IDs — the count is never asserted independently of the list. A NEEDS-REDESIGN verdict that states "4 EG gaps" without enumerating the IDs, or where the stated count does not match the named list length, fails this criterion. |
| C-27 | **Promotion completeness gate** | 0.5 pts | behavior | The SA-TO-SG PROMOTION lifecycle event includes an arithmetic self-check table with three fields: SA gaps promoted to SG (count), SA gaps remaining (count), and Stage 1 SA total (count). A PASS result is recorded when promoted + remaining equals Stage 1 SA total; a MISMATCH result is recorded otherwise. A MISMATCH result structurally blocks Phase 2 Execute from proceeding until the discrepancy is resolved. A trace where the arithmetic table is absent, or where a MISMATCH result does not halt Phase 2, fails this criterion. |
| C-28 | **Verdict-to-table finding ID traceability** | 0.5 pts | correctness | When C-26 is satisfied and the verdict enumerates EG finding IDs, each cited ID resolves to a specific row in the Step 3b findings table. The verdict may not cite an ID that does not appear as a table row, and the Step 3b table may not contain EG findings whose IDs are absent from the verdict evidence anchor. A trace where the verdict ID list and the Step 3b EG rows do not form a 1-to-1 match, in either direction, fails this criterion. |
| C-29 | **Promotion count forward-reference in verdict** | 0.5 pts | depth | When both C-26 and C-27 are satisfied, the Phase 5 evidence summary includes the SA remaining count sourced from the promotion arithmetic closure (C-27 block) alongside the EG count from the evidence anchor (C-26 block). The combined gap inventory — EG count + SA remaining — is stated explicitly and used to confirm the verdict classification threshold. A NEEDS-REDESIGN verdict that carries EG count but omits SA remaining, or that states a combined total without naming both components, fails this criterion. |
```

---

**Summary of changes from v8 to v9:**

| New ID | Pattern name | Source | Weight |
|--------|-------------|--------|--------|
| C-28 | Verdict-to-table finding ID traceability | R12 V-01/V-04 | 0.5 pts |
| C-29 | Promotion count forward-reference in verdict | R12 V-02/V-04 | 0.5 pts |

Grand total: 102.5 + 1.0 = **103.5 pts**. Baseline for R13 entry state is 102.5 / 103.5 (R12 best passes C-01–C-27).
