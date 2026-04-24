Reading the scorecard's `new_patterns` JSON and the evidence notes to extract the three R7 excellence patterns, then promoting them to C-24, C-25, C-26.

---

## Quest Rubric — v8

`23 criteria, 230 pts max` → `26 criteria, 260 pts max`

---

### What changed: v7 → v8

Three new aspirational criteria extracted from R7 excellence signals. All three were observed in V-02/V-03/V-04/V-05 as robustness-hardening forms that tied V-01 at 230 — meaning they are structurally stronger than the v7 minimum PASS gates but carry no rubric cost at current coverage. They are promoted here so R8 can falsify the COMPRESSED × timestamp risk and verify that the named-rule and sub-label forms are stable.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-24 | Named isolation rule at two structural locations for timestamp survival under COMPRESSED | Hardening of C-16 |
| C-25 | Zero-signal mandate promoted to standalone named execution rule with two operational clauses | Hardening of C-22 |
| C-26 | Action-posture sub-labels on bounded/unbounded inertia field | Hardening of C-23 |

**Structural chains updated:**

- Timestamp survivability chain: C-16 → C-24 (item-level timestamp mandate → dual-location isolation for COMPRESSED survival)
- Synthesis robustness chain: C-18 → C-21 → C-22 → C-25 (structure mandated → sparse guard → zero guard → named-rule promotion)
- Verdict action-posture chain: C-06 → C-23 → C-26 (verdict named → verdict classifies recoverability → action posture made explicit)

**R9 investigation candidate carried forward:** Whether C-25's named-rule form (standalone rule with two sub-clauses) survives at higher token pressure than the embedded-clause form of C-22, and whether C-26's sub-label syntax is preserved when the COMPRESSED branch abbreviates the VERDICT block.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(26 total criteria; C-01–C-20 definitions unchanged from v6.)*

---

#### C-21 — Sparse-coverage synthesis protection *(v6)*

When `found` contains signals from only 1–2 namespaces, the STORY block must not default to a coverage disclaimer. Synthesis must proceed on the signals present. PARTIAL = synthesis present but hedged with "limited data" language that weakens conclusions. PASS = STORY produces definite synthesis from sparse coverage, treating the available signals as sufficient to characterize the current state of knowledge.

---

#### C-22 — Zero-signal synthesis mandate *(R6 Pattern — V-03/V-04/V-05)*

When the `found` section of STATUS is empty (zero signals across all namespaces), the STORY block must not collapse to a non-finding. The LLM failure mode is to write "no signals found — synthesis not possible" and omit or hollow STORY. But uniform absence is itself evidence: the gap pattern defines what the team does not know and why they are not ready. Question 1 must characterize what uniform absence implies — "the absence of any scout signal indicates the market surface has not been probed at all" is a valid synthesis; "insufficient data" is not.

**PARTIAL** — sparse-coverage protection present (C-21 PASS) but no explicit clause for the zero-signal case; synthesis may be vacated on grounds of empty `found`.

**PASS** — an explicit zero-signal clause in the STORY execution note declares that empty `found` is not grounds for omitting synthesis — the gap pattern is the evidence set — and mandates that question 1 characterize what uniform absence implies rather than reporting absence as a non-answer.

This is distinct from C-21, which guards synthesis when coverage is sparse (1–2 namespaces); C-22 guards synthesis when coverage is zero. Both are boundary conditions on C-18's structural mandate.

---

#### C-23 — Bounded/unbounded inertia classification at verdict level *(R6 Pattern — V-05)*

The `inertia_cost` field at VERDICT level must classify the aggregate commit risk by recoverability. Bounded = the team can detect the failure post-commit and course-correct before it propagates (e.g., "if persona assumptions are wrong, the next campaign signals will surface the delta"). Unbounded = the failure propagates to an irreversible state before detection is possible (e.g., "if the regulatory gap is real, commitment triggers an audit trail that cannot be retracted"). This distinction determines action posture: bounded inertia means "commit with monitoring"; unbounded inertia means "do not commit until resolved." A VERDICT with unnamed recoverability forces the team to re-read all item-level gap fields and synthesize the posture themselves — the verdict is not actionable on its own.

**PARTIAL** — `inertia_cost` present at VERDICT level but bounded/unbounded classification absent; risk is named but the team cannot derive their action posture without re-reading item-level fields.

**PASS** — `inertia_cost` declares `bounded: <residual risk and why recoverable post-commit>` OR `unbounded: <failure class and why irreversible once committed>`, enabling the team to act on the verdict block alone without re-reading blocking gap entries.

This is distinct from C-07, which tests that each blocking gap entry carries an inertia field; C-23 tests that the verdict-level aggregate field classifies recoverability. They are structurally independent.

---

#### C-24 — Timestamp isolation dual-location mandate *(R7 Pattern — V-02/V-05)*

C-16 guards that per-signal timestamps are present at the item level. C-24 guards their survival when the COMPRESSED format branch activates. When blocking entry count exceeds the COMPRESSED threshold (>4), the STATUS block may be abbreviated — and the model may collapse `found` timestamps alongside blocking gap entries into summary form, destroying the signal-level date record. A single-location prose instruction (e.g., in the STORY execution note only) is insufficient because the COMPRESSED context may omit that section before reaching the instruction.

The isolation rule must appear at **two structural locations**: (1) within the `found` entry format definition or question body text, specifying that timestamps are structurally separate from blocking entries and must not be abbreviated; and (2) in the STATUS or STORY execution note, restating that COMPRESSED format must not collapse `found` into the blocking summary. Double-location restatement ensures that if the COMPRESSED branch elides one location, the rule survives at the other.

**PARTIAL** — timestamp isolation rule stated at one structural location only; survival under COMPRESSED is single-point-of-failure.

**PASS** — isolation rule stated explicitly at two structural locations (entry format definition AND execution note), so the rule survives COMPRESSED abbreviation regardless of which location is reached first.

Relationship to C-16: C-16 tests that timestamps exist in the nominal (non-COMPRESSED) path. C-24 tests that the instruction architecture ensures they survive under compression. They are independent checks on the same field.

---

#### C-25 — Zero-signal mandate as standalone named execution rule *(R7 Pattern — V-03/V-05)*

C-22 requires an explicit zero-signal clause somewhere in the STORY execution note. C-25 requires that clause to be promoted from inline advisory text to a **standalone named execution rule** with two explicit operational sub-clauses.

Sub-clause 1: "Empty `found` is not grounds for omitting synthesis — the gap pattern is the evidence set."
Sub-clause 2: "Question 1 must characterize what uniform absence implies: what surface of the problem has not been probed at all, and what that means for the decision."

An embedded clause satisfies C-22 but not C-25. Named-rule form is structurally stronger for two reasons: (a) it is discoverable without reading the full execution note — a model scanning for named rules will encounter it; (b) the two sub-clauses resolve the two distinct failure modes independently (omission vs. vacuous restatement of absence), rather than relying on a single sentence to cover both.

**PARTIAL** — embedded zero-signal clause present in execution note (C-22 PASS) but not promoted to standalone named rule; clause is inline and may be overlooked under prompt compression.

**PASS** — standalone named zero-signal execution rule present with both operational sub-clauses explicit, structurally separated from surrounding prose, discoverable as a named mandate.

Relationship to C-22: C-22 requires the clause to exist. C-25 requires it to be structurally promoted. C-22 PASS is a prerequisite for C-25 scoring.

---

#### C-26 — Action-posture sub-labels on bounded/unbounded inertia field *(R7 Pattern — V-04/V-05)*

C-23 requires `inertia_cost` to declare `bounded:` or `unbounded:` with supporting rationale, enabling the team to *derive* the action posture. C-26 requires the action posture to be made **explicit** via sub-labels directly on the field, eliminating the derivation step entirely.

Required sub-label form:

```
inertia_cost: bounded: <residual risk and why recoverable>  action: commit with monitoring
```

or:

```
inertia_cost: unbounded: <failure class and why irreversible>  action: do not commit until resolved
```

The action sub-label must match the classification — `bounded` maps to `commit with monitoring`; `unbounded` maps to `do not commit until resolved`. A field with classification but no sub-label satisfies C-23 but not C-26, because the team must still infer the posture from the classification type. With the sub-label, the team's next action is readable directly from the verdict block without any inference step.

**PARTIAL** — `bounded:` or `unbounded:` classification present with rationale (C-23 PASS) but no explicit `action:` sub-label; team must infer posture from classification type.

**PASS** — `inertia_cost` carries an explicit `action:` sub-label whose value matches the classification (`commit with monitoring` for bounded; `do not commit until resolved` for unbounded), making the action posture directly readable from the verdict block.

Relationship to C-23: C-23 tests that recoverability is classified. C-26 tests that the action posture is made explicit rather than derivable. C-23 PASS is a prerequisite for C-26 scoring.

---

### Criteria Table — v8

| # | Criterion | Tier | Notes |
|---|-----------|------|-------|
| C-01 | *(carry forward)* | Essential | |
| C-02 | *(carry forward)* | Essential | |
| C-03 | *(carry forward)* | Essential | |
| C-04 | *(carry forward)* | Essential | |
| C-05 | *(carry forward)* | Essential | |
| C-06 | Verdict present and named | Essential | |
| C-07 | Item-level inertia fields on blocking gaps | Essential | |
| C-08 | *(carry forward)* | Essential | |
| C-09 | *(carry forward)* | Essential | |
| C-10 | *(carry forward)* | Essential | |
| C-11 | *(carry forward)* | Structural | |
| C-12 | *(carry forward)* | Structural | |
| C-13 | *(carry forward)* | Structural | |
| C-14 | *(carry forward)* | Structural | |
| C-15 | *(carry forward)* | Structural | |
| C-16 | Per-signal timestamps present | Structural | C-24 extends for COMPRESSED survival |
| C-17 | *(carry forward)* | Structural | |
| C-18 | STORY three-question sequential structure | Aspirational | Head of synthesis robustness chain |
| C-19 | Gap reclassification rule | Aspirational | |
| C-20 | Density ceiling on entry count | Aspirational | |
| C-21 | Sparse-coverage synthesis protection | Aspirational | |
| C-22 | Zero-signal synthesis mandate | Aspirational | C-25 extends to named-rule form |
| C-23 | Bounded/unbounded inertia at verdict level | Aspirational | C-26 extends to explicit action sub-label |
| **C-24** | **Timestamp isolation dual-location mandate** | **Aspirational** | **New — R7 V-02/V-05** |
| **C-25** | **Zero-signal mandate as standalone named rule** | **Aspirational** | **New — R7 V-03/V-05** |
| **C-26** | **Action-posture sub-labels on inertia field** | **Aspirational** | **New — R7 V-04/V-05** |
| | **MAX** | | **260 pts** |

---

### Structural Chain Summary — v8

| Chain | Sequence | Purpose |
|---|---|---|
| Timestamp survivability | C-16 → C-24 | Item-level presence → dual-location isolation for COMPRESSED survival |
| Synthesis robustness | C-18 → C-21 → C-22 → C-25 | Structure mandated → sparse guard → zero guard → named-rule promotion |
| Verdict action-posture | C-06 → C-23 → C-26 | Verdict named → recoverability classified → action posture made explicit |

---

### R9 Investigation Candidates

1. **COMPRESSED × `found` timestamp survival (live output)** — C-24's dual-location mandate is prose-level instruction. R9 must run live output at >4 blocking gaps to falsify: if timestamps drop from `found` under COMPRESSED, C-24 is insufficient and a structural `[FOUND]` block separation is required.

2. **C-25 named-rule form under token pressure** — Whether the standalone named rule with two sub-clauses survives at higher token pressure than the embedded-clause form of C-22. Hypothesis: named rules are more likely to be preserved than inline advisory text when the model abbreviates.

3. **C-26 sub-label preservation under COMPRESSED VERDICT** — Whether `action:` sub-labels on `inertia_cost` are preserved when the VERDICT block is abbreviated. If the model drops sub-labels under compression, C-26 requires structural separation of the action field.

---

```json
{"version": "v8", "criteria_count": 26, "max_score": 260, "new_criteria": ["C-24", "C-25", "C-26"], "r7_base": "V-05", "r9_primary_investigation": "COMPRESSED x found timestamp survival — live output at >4 blocking gaps"}
```
