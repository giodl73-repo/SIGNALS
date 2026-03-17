Reading the scorecard, I can see two explicit candidacy signals flagged in the differentiation notes:

- **C-26 candidacy** (C-05 note): NEEDS-REDESIGN EVIDENCE ANCHOR — verdict names EG finding IDs explicitly, count derived from the list.
- **C-27 candidacy** (C-06 note): PROMOTION COMPLETENESS GATE — arithmetic self-check `(promoted + remaining = Stage 1 SA count)` with MISMATCH blocks Phase 2b.

Grand total moves to **102.5 pts**. Here is the complete v8 rubric:

---

```markdown
# Trace-Inspect Rubric — v8

**Skill**: `trace-inspect`
**Version**: v8 (updated from v7 — added C-26 and C-27 from R11 excellence signals;
aspirational block: C-09 and C-10 at 2 pts each; C-11 through C-27 at 0.5 pts each;
grand total 102.5)
**Applies to**: Trace outputs produced by any variation of the trace-inspect skill
**Scoring**: 102.5-point composite. Golden threshold: all 5 essential criteria pass AND
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
> base combination of C-22 + C-23). C-26 and C-27 are new in v8, extracted from R11 excellence
> signals: C-26 from the NEEDS-REDESIGN EVIDENCE ANCHOR pattern (V-01/V-04/V-05 in R11) and
> C-27 from the PROMOTION COMPLETENESS GATE pattern (V-02/V-04/V-05 in R11).

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Compliance ledger populated** | 2 pts | correctness | Phase 5 includes the full VC compliance ledger (VC-1 through VC-5) with one row per usage site declared in the Coverage Matrix. The "Observed behavior" cell names specific values, label lists, or invariant results — it does not say "as expected." All VC overall results are stated. A trace with a verdict but no compliance ledger, or a ledger with generic "as expected" observations, fails this criterion. |
| C-10 | **Schema 5 sub-step transition confirmations** | 2 pts | behavior | Each Phase 3 sub-step boundary (3a→3b, 3b→3c, 3c→3d) includes an explicit Schema 5 transition sentence confirming the completed sub-step and declaring the next valid to begin (e.g., "Schema 5 transition: Step 3a complete. Step 3b is valid to begin."). A trace with sub-step transitions that lack this confirmation sentence, or where sub-steps are separated by prose rather than named transition statements, fails this criterion. |
| C-11 | **Gate clearance summary blocks** | 0.5 pts | behavior | A GATE CLEARANCE SUMMARY block appears between Step 3c and Step 3d, summarizing the PASS/FAIL result for each of G-1, G-2, and G-3. A PHASE 4 GATE CLEARANCE SUMMARY block appears at Phase 4 (Amend) entry. A trace missing either block, or one that folds gate summaries into prose rather than discrete named blocks, fails this criterion. |
| C-12 | **Remediation log with exemption clause** | 0.5 pts | behavior | If any enforcement gate (G-1, G-2, or G-3) fails at Step 3c, a REMEDIATION LOG block records each failing gate's ID, failure cause, and remediation action taken before Step 3d proceeds. If all gates pass on first evaluation, a C-12 EXEMPTION clause is present confirming no remediation log is required. A trace with a gate failure and no REMEDIATION LOG, or a trace with no failures that omits the C-12 EXEMPTION clause, fails this criterion. |
| C-13 | **Schema 5 prerequisite verification lines** | 0.5 pts | behavior | Each Phase 3 sub-step includes a Schema 5 prerequisite verification line at its entry point confirming the prior sub-step is complete before the current sub-step begins (e.g., "Schema 5 prerequisite: Step 3a complete."). A trace where any sub-step begins without a prerequisite verification line fails this criterion. |
| C-14 | **Phase 1 gap attribution per role** | 0.5 pts | correctness | Each role's schema binding block in Phase 1 includes an explicit gap attribution line naming which SA gaps (if any) affect that role, or a "no gaps affecting this role" confirmation. A trace where Phase 1 binding blocks contain schema declarations but no gap attribution per role fails this criterion. |
| C-15 | **EG gap encounter declared at relay** | 0.5 pts | coverage | Each Phase 2 role relay includes an "EG gaps encountered" field. The field either lists specific EG gap IDs discovered during that relay or states "none encountered at this relay." A relay where EG gap status is omitted or folded into the Produced field fails this criterion. |
| C-16 | **Stage boundary confirmations** | 0.5 pts | behavior | The Schema 3 lifecycle event sequence (Stage 1 relay → SA-TO-SG PROMOTION → Stage 2 relay) includes an explicit named boundary marker at each transition point. A trace where stage transitions are implied by section headers alone, without a declared boundary confirmation, fails this criterion. |
| C-17 | **G-1 source-type enumeration** | 0.5 pts | behavior | The G-1 gate check at Step 3c names the distinct Source types found in the Step 3b table and states the count explicitly (e.g., "Source types present: {SA, EG} — 2 distinct types. G-1: PASS"). A G-1 check that states only PASS or FAIL without enumerating the source types fails this criterion. |
| C-18 | **G-2 duplicate-action scan declared** | 0.5 pts | behavior | The G-2 gate check at Step 3c declares the scan performed: names each Source type checked for duplicate Action text and confirms no duplicates found (or names the violating pair if FAIL). A G-2 check that states only PASS or FAIL without declaring the scan fails this criterion. |
| C-19 | **Phase 4 amendment linkage** | 0.5 pts | depth | Each Phase 4 amendment or dismissal entry references the finding ID or gap ID it resolves. A Phase 4 entry that describes a change without naming the upstream finding it closes fails this criterion. |
| C-20 | **Verdict rationale quantified** | 0.5 pts | depth | The verdict rationale names a specific count or threshold that drove the classification (e.g., "4 EG gaps exceed the 3-gap NEEDS-REDESIGN threshold"). A verdict whose rationale uses only qualitative language without citing the numeric basis fails this criterion. |
| C-21 | **Coverage Matrix enforcement class column** | 0.5 pts | correctness | The Coverage Matrix includes an Enforcement Class column for each schema row, declaring whether compliance is checked by a gate (G-1/G-2/G-3), by the promotion lifecycle event, or by structural contract. A Coverage Matrix with schema rows but no enforcement class annotation fails this criterion. |
| C-22 | **EG-FIRST execution constraint block** | 0.5 pts | behavior | A named EG-FIRST EXECUTION CONSTRAINT block appears in Phase 2 before the first role relay, declaring that EG gaps are recorded at the relay where they are encountered rather than deferred to Phase 3. A trace that handles EG gaps correctly but without a named constraint block stating this rule fails this criterion. |
| C-23 | **PHASE 2a/2b membership declarations** | 0.5 pts | correctness | Phase 2 includes explicit PHASE 2a MEMBERSHIP and PHASE 2b MEMBERSHIP declaration blocks naming the roles assigned to each sub-phase before any relay runs. A trace that runs relays in two groups without named membership declarations fails this criterion. |
| C-24 | **EG-FIRST constraint cites Coverage Matrix column** | 0.5 pts | correctness | The EG-FIRST EXECUTION CONSTRAINT block (C-22) explicitly references the Coverage Matrix Enforcement Class column as the source for the constraint declaration — connecting the constraint to its annotation origin rather than asserting it independently. A trace whose EG-FIRST block states the constraint without citing the Enforcement Class column fails this criterion. |
| C-25 | **G-1 compliance anchored to membership list** | 0.5 pts | behavior | The VC-4 G-1 compliance ledger entry includes a count-check that validates the PHASE 2a/2b MEMBERSHIP declarations (C-23) — the G-1 PASS is explicitly anchored to the named membership list, not derived from an independent source count. A G-1 ledger entry that records a PASS without referencing the membership declarations fails this criterion. |
| C-26 | **NEEDS-REDESIGN evidence anchor** | 0.5 pts | depth | When the verdict classification is NEEDS-REDESIGN, the verdict block includes a named NEEDS-REDESIGN EVIDENCE ANCHOR that lists the specific EG finding IDs driving the classification. The EG finding count cited in the verdict rationale is derived from this anchor list, not independently asserted. A NEEDS-REDESIGN verdict whose rationale states a count without a named anchor listing the contributing finding IDs fails this criterion. Verdicts classified as USEFUL or NEEDS-SPEC-REVISION are exempt. |
| C-27 | **Promotion completeness gate** | 0.5 pts | correctness | After the SA-TO-SG promotion inventory, a named PROMOTION COMPLETENESS GATE block appears containing the arithmetic self-check: `promoted + remaining = Stage 1 SA count`. If the check resolves to MATCH, Phase 2b proceeds. If the check resolves to MISMATCH, a MISMATCH block is emitted and Phase 2b does not begin until the discrepancy is resolved. A trace whose promotion inventory records counts without a named gate block performing this self-check fails this criterion. |
```
