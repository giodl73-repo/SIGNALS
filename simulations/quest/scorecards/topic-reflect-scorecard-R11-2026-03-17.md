## /quest:score — topic-reflect Round 11 (Rubric v10)

---

### Scoring Note

Only **V-01** was provided with full prompt text. V-02 through V-05 appear in the variation summary with axis/hypothesis only — no prompt text was included. I am scoring V-01 fully. V-02–V-05 cannot be scored without their texts; placeholder analysis is noted where applicable.

---

## V-01 — Full Criterion Evaluation

**Axis:** Lifecycle Emphasis — dedicated Field Reference block before Stage 4 entry loop

---

### Essential Tier (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Stage 4 Field Reference: "Must reference a specific B-# from Stage 1 and name the gap." Surprise 0 demonstrates with "B-2 predicted…the scout-naming signals showed…the opposite sequencing." COMMIT-ENTRY checklist enforces at emission. |
| C-02 | **FAIL** | Stage 6 is absent from the prompt text. Gate Sequence Overview references COMMIT-STAGE-6 but no Stage 6 instructions appear — no verdict table, no COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED tokens, no revision direction. The symmetric contract is opened in Stage 1 but never closed. |
| C-03 | **PASS** | Field Reference: "Name: artifact name, namespace, and/or date. Do not write 'multiple sources.'" COMMIT-ENTRY checklist gate: "if 'multiple sources' or unnamed: identify the primary artifact and rewrite." Surprise 0 demonstrates: "scout-naming-{topic}-2024-11-14.md (scout namespace)." |
| C-04 | **PASS** | Field Reference: "Names a specific component, API, flow, or decision. Do not write 'the system.'" COMMIT-ENTRY: "if vague: identify the specific element and rewrite." Surprise 0: "artifact deduplication component in the topic registry must be refactored." |
| C-05 | **PASS** | Stage 3 five-check table present with VALID/INVALID verdict slots. Stage 3 EXIT defines COMMIT-STAGE-3-CLEAN and COMMIT-STAGE-3-FLAGGED paths with corrective action requirement for INVALID verdicts. |

**Essential subtotal: 48 / 60 — all_essential_pass: FALSE (C-02)**

---

### Recommended Tier (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Vocabulary Rule section: "The only valid epistemic dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness. Substitution is prohibited." Stage 1 EXIT: "Audit dimension names." Mapping table enforces canonical replacements. |
| C-07 | **PASS** | Stage 4 EXIT: "At least 2 GATE-CONFIRMED entries recorded." Entry instructions: "Extend the sweep if fewer than 2 entries pass all checks after the initial scan." |
| C-08 | **PASS** | Stage 5: "The Next Team / Skill column must name at least one specific skill (e.g., /flow:trigger) or team role (e.g., 'Flow engineer') — not just 'investigate.'" |

**Recommended subtotal: 30 / 30**

---

### Aspirational Tier (5 pts each)

| ID | Verdict | Pts | Evidence |
|----|---------|-----|----------|
| C-09 | **PARTIAL** | 2 | COMMIT-STAGE-1 through COMMIT-STAGE-5 present in stage instructions; COMMIT-STAGE-6 referenced in Gate Overview only — Stage 6 instructions absent, so that token's emission path is not instructed. COMMIT-ENTRY per row present. GATE-CONFIRMED used in Stage 4 context but defined implicitly. |
| C-10 | **FAIL** | 0 | Stage 6 absent. No explicit CLEAR or FLAGGED foreknowledge resolution in Stage 6. |
| C-11 | **PASS** | 5 | Stage 4 entries are numbered prose blocks with labeled sub-fields (Surprise, Signal Source, Design Impact, Build Risk). Field Reference establishes the template. |
| C-12 | **PASS** | 5 | COMMIT-ENTRY checklist requires full phrases for Signal Source and Design Impact. Field Reference requires full sentences. Surprise 0 models full-sentence values across all four sub-fields. |
| C-13 | **PASS** | 5 | Vocabulary Rule section is a standalone block: "The only valid epistemic dimension names are…Substitution is prohibited. Do not use synonyms, paraphrases, or adjacent terms." Not embedded as examples in Stage 1 prose. |
| C-14 | **PASS** | 5 | Stage 3 EXIT provides binary path: COMMIT-STAGE-3-CLEAN when all checks pass; COMMIT-STAGE-3-FLAGGED when foreknowledge INVALID — structurally enforced, not advisory. Global HALT CONDITION paragraph reinforces the halt. |
| C-15 | **PASS** | 5 | Gate Sequence Overview table precedes Stage 1. Lists all tokens, stage numbers, conditions, and effects. HALT CONDITION stated as standalone paragraph after the table. |
| C-16 | **PASS** | 5 | Surprise 0 is a complete, filled-in calibration entry. Signal Source names a realistic artifact with namespace and date. Design Impact names a specific component ("artifact deduplication component in the topic registry"). |
| C-17 | **PASS** | 5 | Prohibited synonyms table names: Reliability, Performance, Complexity, Maintainability, Discoverability, Testability — ≥2 named prohibited synonyms beyond a general prohibition. |
| C-18 | **PASS** | 5 | Mapping table provides canonical replacements for all named synonyms: Reliability→Correctness, Performance→Scalability, Complexity→Correctness or Feasibility, Maintainability→Adoptability, Discoverability→Usability or Adoptability, Testability→Correctness or Feasibility. ≥2 full mappings. |
| C-19 | **PASS** | 5 | Stages 1, 2, 3, and 4 each have explicit ENTER and EXIT sections. ≥3 stages meet the per-stage lifecycle contract requirement. Stage 5 has ENTER but incomplete EXIT (no COMMIT-STAGE-5 emission instruction shown); still passes threshold. |
| C-20 | **PASS** | 5 | Surprise 0 labeled "Calibration Entry (not a live entry)," formatted identically to the Stage 4 entry template, positioned within Stage 4 before the live entry instructions begin. Model encounters the complete entry before writing any live entry. |
| C-21 | **PASS** | 5 | Gate Sequence Overview intro: "At every EXIT gate, audit all dimension names against this table and correct any malformed names before emitting the stage token." Prescribes corrective action ("correct") with reference to the mapping table — converts the table into an active runtime repair protocol. |
| C-22 | **PASS** | 5 | Build Risk defined in Field Reference as a labeled prose sub-field. Requires specific component/decision/risk surface. Modeled in Surprise 0: "signal lifecycle state machine assumes query-time resolution as its terminal state…" |
| C-23 | **PASS** | 5 | Surprise 0: Design Impact = "artifact deduplication component in the topic registry must be refactored to support write-time conflict detection." Build Risk = "signal lifecycle state machine…write-time detection changes the state transition contract, risking silent inconsistency." Distinct components, non-redundant, conceptually separated (what changes vs. what is implicated). |
| C-24 | **PASS** | 5 | COMMIT-ENTRY checklist: "[ ] Build Risk: Names a specific component, decision, or risk surface (not a general risk category) — if abstract or categorical: identify the specific risk surface and rewrite." Names the failure condition and prescribes corrective action. |
| C-25 | **PASS** | 5 | All four sub-fields covered by ≥2 independent mechanisms: Surprise 0 (imitation floor) + COMMIT-ENTRY checklist (gate) + Field Reference quality requirement (specification). All four sub-fields have all three mechanisms simultaneously. |
| C-26 | **PASS** | 5 | Build Risk Field Reference under "Paired formula": "Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail." Names both fields and their structural relation in a single definitional sentence. |
| C-27 | **PASS** | 5 | Build Risk definition contains all three anchors in sequence: (a) Purpose: "Names the exposure surface opened by the change — what the Design Impact update puts at risk in the existing build." (b) Paired formula (C-26): present. (c) Structural gloss: "One field is forward-looking (what to update); the other is risk-surface (what could break or require rework). They are not paraphrases." All three present before Surprise 0. |
| C-28 | **PASS** | 5 | COMMIT-ENTRY block uses `[ ]` checklist format — each sub-field on a dedicated bullet with gate condition and inline corrective action visible at that bullet. All four fields simultaneously scannable without parsing prose. |

**Aspirational subtotal: 92 / 100**

---

### V-01 Composite Score

| Tier | Score | Max |
|------|-------|-----|
| Essential | 48 | 60 |
| Recommended | 30 | 30 |
| Aspirational | 92 | 100 |
| **Total** | **170** | **190** |

---

## V-02 through V-05 — Not Scorable

Full prompt texts for V-02, V-03, V-04, and V-05 were not included in this invocation. Scoring these variations from hypothesis descriptions alone would require fabricating criterion verdicts without textual evidence — not reliable. The ranking below reflects V-01 as the sole scored variation.

Analytical projections based on stated axes (for reference only, not scored):

- **V-02** (Phrasing Register): Style-only change; likely same Stage 6 gap as V-01. C-28 may improve slightly from imperative phrasing. Projected ≈ 165–172.
- **V-03** (Output Format): Gate Topology Map + visual checklist focus; likely strong C-15/C-28 coverage. Whether Stage 6 is included is unknown. Projected ≈ 170–180.
- **V-04** (Inertia Framing): Failure-mode labeling improves C-01/C-07 compliance. Stage 6 presence unknown. Projected ≈ 165–175.
- **V-05** (Combination): Highest potential if it includes Stage 6 (lifecycle depth axis). If C-02 passes: adds 12 essential + C-10 recovery → potential 182–190. If Stage 6 still absent: similar range to V-01.

---

## Ranking (scored variations only)

| Rank | Variation | Score | All Essential |
|------|-----------|-------|---------------|
| 1 | V-01 | 170/190 | No (C-02) |

---

## Excellence Signals from V-01

**Signal 1 — Pre-loop unified Field Reference block**
V-01 isolates all four sub-field definitions into a labeled block ("Field Reference — Read this block before writing any entry") positioned before the entry loop, with an explicit reading directive. This is structurally distinct from embedding definitions inline within per-entry instructions: the model receives a complete schema read-through as a single unit before any entry begins. C-27 tests what the Build Risk definition contains; no criterion tests the structural placement of all four definitions as a unified pre-loop block with explicit reading instruction.

**Signal 2 — Standalone global HALT instruction as post-overview paragraph**
V-01 adds a "HALT CONDITION:" paragraph immediately after the Gate Sequence Overview table: "If COMMIT-STAGE-3-FLAGGED is emitted, do not emit any further stage tokens." This is a global, unconditional rule stated before Stage 1 begins — distinct from Stage 3 EXIT's local foreknowledge handling. C-14 and C-15 test binary gate tokens and gate topology; no criterion captures the global halt as a structurally separate, pre-stage statement with unconditional scope.

---

```json
{"top_score": 170, "all_essential_pass": false, "new_patterns": ["pre-loop unified Field Reference block: all four sub-field definitions presented as a single labeled block with an explicit reading directive before the entry loop begins — structurally isolated from per-entry instructions so the model receives a complete schema read-through as a unit before writing any entry", "standalone global HALT instruction: unconditional halt condition stated as a separate labeled paragraph after the Gate Sequence Overview, applying to all subsequent stage tokens regardless of stage — distinguished from Stage 3 EXIT criterion by its global scope and pre-stage placement before any stage instructions begin"]}
```
