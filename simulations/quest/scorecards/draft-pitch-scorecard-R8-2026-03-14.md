---

# Scorecard: draft-pitch — Round 8

**Rubric version**: v8 | **Denominator**: 30 aspirational criteria (20 inherited + 10 new)

---

## New Criteria (C-28–C-37)

Three groups, 10 criteria total — all probing Phase 5 enforcement gaps:

| Group | Criteria | What it tests |
|-------|----------|---------------|
| INERTIA PROFILE | C-28–C-31 | Named pre-step present; provenance template; gate stop; per-version Why-It-Matters constraint |
| DIFFERENTIATION GATE | C-32–C-35 | Named post-step present; 3-row table; YES/NO format with passing state; rewrite loop |
| Draft sequence | C-36–C-37 | Maker-first declared; position labels on version headers |

---

## Per-Variation Results (C-28–C-37 only)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-28 INERTIA PROFILE present | PASS | FAIL | FAIL | PASS | PASS |
| C-29 Provenance template | PASS | FAIL | FAIL | PASS | PASS |
| C-30 Gate stop | PASS | FAIL | FAIL | PASS | PASS |
| C-31 Why-It-Matters constraint | PASS | FAIL | FAIL | PASS | PASS |
| C-32 DIFFERENTIATION GATE present | FAIL | PASS | FAIL | PASS | PASS |
| C-33 3-row table | FAIL | PASS | FAIL | PASS | PASS |
| C-34 YES/NO passing state | FAIL | PASS | FAIL | PASS | PASS |
| C-35 Rewrite loop | FAIL | PASS | FAIL | PASS | PASS |
| C-36 Maker-first declared | FAIL | FAIL | PASS | FAIL | PASS |
| C-37 Position labels | FAIL | FAIL | PASS | FAIL | PASS |
| **New passes** | **4** | **4** | **2** | **8** | **10** |

---

## Score Summary

| Variation | Aspirational (30 criteria) | Composite | Rank |
|-----------|---------------------------|-----------|------|
| **V-05** | 30/30 = 10.0 | **100.0** | 1 |
| **V-04** | 28/30 = 9.33 | **99.3** | 2 |
| **V-01** | 24/30 = 8.0 | **98.0** | 3 (tied) |
| **V-02** | 24/30 = 8.0 | **98.0** | 3 (tied) |
| **V-03** | 22/30 = 7.33 | **97.3** | 5 |

---

## Diagnostic: Why V-03 Scores Below V-01 and V-02

Maker-first adds only 2 scorable structural properties (C-36, C-37 — declare order, label positions). INERTIA PROFILE and DIFFERENTIATION GATE each add 4, because they introduce named phase elements with internal structural requirements. Maker-first is a quality mechanism — its value shows up at execution time (does the Maker version shape the message before exec framing is added?), not in skill-structure analysis.

---

## Excellence Signals from V-05

V-05 is the first variation where Phase 5 has the same pre-commit → constrained-fill → post-verify structure that Phase 2 acquired in R7 V-05.

**Pattern 1 — Phase-level envelopment**: named pre-step (INERTIA PROFILE) + constrained fill order (Maker-first) + named post-step (DIFFERENTIATION GATE) makes a phase auditable from skill structure alone. The same mechanism that made Phase 2 auditable — name the data flow before consuming it, fill in constraint order, declare closure — now applied to Phase 5.

**Pattern 2 — Constraint-ascending draft sequence**: Maker-first forces the Core Belief to be expressible in plain language before exec/dev framing is added. EXEC OPENING SENTENCE is pre-committed at Phase 4 regardless of draft order, so Maker-first doesn't weaken the exec version. Position labels make the constraint order auditable without execution inspection.

**Pattern 3 — Structural rewrite loop**: DIFFERENTIATION GATE converts "zero unexplained acronyms" and "show the tool, not the business case" from advisory instructions into pass/fail phase exits. YES/NO questions with declared passing state and explicit rewrite-until-pass loop make Phase 5 uncloseable unless the structural constraints are verified.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-level envelopment: a named pre-step (INERTIA PROFILE) + constrained fill order (Maker-first) + named post-step (DIFFERENTIATION GATE) makes Phase 5 auditable from skill structure alone -- the same pre-commit/fill/close structure that made Phase 2 auditable in R7 V-05, now applied to Phase 5", "Constraint-ascending draft sequence decouples message clarity from vocabulary permission: Maker-first forces plain-language coherence before exec/dev framing is added; position labels (draft first/second/last) make the constraint order auditable from the skill text without execution inspection", "Structural rewrite loop converts advisory quality constraints into pass/fail phase exits: DIFFERENTIATION GATE YES/NO questions with declared passing state and explicit rewrite-until-pass loop make zero-jargon and scenario-hook structural stops, not instructions"]}
```
= 98.0**

---

### V-02 — DIFFERENTIATION GATE only (Exec→Dev→Maker, no INERTIA PROFILE)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-28 | INERTIA PROFILE pre-step present | **FAIL** | No INERTIA PROFILE block in Phase 5. |
| C-29 | INERTIA PROFILE cites AUDIENCE BELIEF MAP [Phase 2 gate output] | **FAIL** | No INERTIA PROFILE. |
| C-30 | INERTIA PROFILE gate stop present | **FAIL** | No INERTIA PROFILE gate stop. |
| C-31 | Why-It-Matters instructed to reflect INERTIA PROFILE arc | **FAIL** | Why-It-Matters instructions do not reference INERTIA PROFILE. Dev cites "Active Dev friction from SIGNAL DEFAULTS. Named directly." Maker cites "Active Maker outcome from SIGNAL DEFAULTS." Independent arguments, not INERTIA PROFILE references. |
| C-32 | VERSION DIFFERENTIATION GATE present | **PASS** | "**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted)" — named post-step at end of Phase 5. |
| C-33 | Gate uses structured 3-row table | **PASS** | 3-row table (Exec/Dev/Maker) with Core Belief summary, Hook type, Jargon check columns present. |
| C-34 | Gate questions use YES/NO format with passing state | **PASS** | Three YES/NO questions with "Passing state: Q1=YES, Q2=NO, Q3=YES" declared explicitly. |
| C-35 | Gate has rewrite loop instruction | **PASS** | "Any gate NOT in passing state: rewrite the failing version. Re-fill the table. Re-answer all three questions. Repeat until passing state reached." — structural stop, not advisory. |
| C-36 | Draft order Maker→Dev→Exec declared | **FAIL** | Standard Exec→Dev→Maker order; no constraint-ascending declaration. |
| C-37 | Version position labels present | **FAIL** | Headers are "**Exec Version**", "**Dev Version**", "**Maker Version**" — no position labels. |

New criteria passes: 4/10 (C-32, C-33, C-34, C-35)
Total aspirational: 24/30 → 24 × (10/30) = **8.0 pts**
**Composite: 60 + 30 + 8.0 = 98.0**

---

### V-03 — Maker-first order only (no INERTIA PROFILE, no DIFFERENTIATION GATE)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-28 | INERTIA PROFILE pre-step present | **FAIL** | No INERTIA PROFILE block. Phase 5 begins directly with CTA template and version drafts. |
| C-29 | INERTIA PROFILE cites AUDIENCE BELIEF MAP [Phase 2 gate output] | **FAIL** | No INERTIA PROFILE. |
| C-30 | INERTIA PROFILE gate stop present | **FAIL** | No INERTIA PROFILE gate stop. |
| C-31 | Why-It-Matters instructed to reflect INERTIA PROFILE arc | **FAIL** | Why-It-Matters: Dev uses "Active Dev friction from SIGNAL DEFAULTS. Named directly." Maker uses "Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context." No INERTIA PROFILE reference; no cross-section constraint instruction. |
| C-32 | VERSION DIFFERENTIATION GATE present | **FAIL** | No differentiation gate. Phase 5 ends at "-- PHASE 5 COMPLETE. --" with no post-draft check. |
| C-33 | Gate uses structured 3-row table | **FAIL** | No gate, no table. |
| C-34 | Gate questions use YES/NO format with passing state | **FAIL** | No gate questions. |
| C-35 | Gate has rewrite loop instruction | **FAIL** | No gate, no rewrite loop. |
| C-36 | Draft order Maker→Dev→Exec declared | **PASS** | "Draft order: Maker first, then Dev, then Exec." — explicit constraint-ascending declaration in Phase 5 preamble. |
| C-37 | Version position labels present | **PASS** | "**Maker Version** *(draft first)*", "**Dev Version** *(draft second)*", "**Exec Version** *(draft last)*" — position labels on all three headers. |

New criteria passes: 2/10 (C-36, C-37)
Total aspirational: 22/30 → 22 × (10/30) = **7.33 pts**
**Composite: 60 + 30 + 7.33 = 97.3**

---

### V-04 — V-01 + V-02 combined (INERTIA PROFILE + DIFFERENTIATION GATE, standard order)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-28 | INERTIA PROFILE pre-step present | **PASS** | Named "Phase 5 INERTIA PROFILE" block before any version draft. |
| C-29 | INERTIA PROFILE cites AUDIENCE BELIEF MAP [Phase 2 gate output] | **PASS** | Template uses provenance brackets: "AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row". |
| C-30 | INERTIA PROFILE gate stop present | **PASS** | "-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --" |
| C-31 | Why-It-Matters instructed to reflect INERTIA PROFILE arc | **PASS** | Cross-section constraint + per-version instructions. Exec: "Name the inertia arc from INERTIA PROFILE Exec sentence... 2-3 sentences ROI framing grounded in the inertia arc." Dev: "Name the inertia arc from INERTIA PROFILE Dev sentence. Show the before-state (Inertia Excuse) and the after-state (Inertia Counter)." Maker: "Name the inertia arc from INERTIA PROFILE Maker sentence in plain language." |
| C-32 | VERSION DIFFERENTIATION GATE present | **PASS** | Named post-step gate after all three versions. |
| C-33 | Gate uses structured 3-row table | **PASS** | 3-row table (Exec/Dev/Maker) with Core Belief summary, Hook type, Jargon check. |
| C-34 | Gate questions use YES/NO format with passing state | **PASS** | Three YES/NO questions, "Passing state: Q1=YES, Q2=NO, Q3=YES" declared. |
| C-35 | Gate has rewrite loop instruction | **PASS** | Explicit rewrite loop: "rewrite the failing version. Re-fill the table. Re-answer all three questions. Repeat until passing state reached." |
| C-36 | Draft order Maker→Dev→Exec declared | **FAIL** | Standard Exec→Dev→Maker order maintained; no constraint-ascending declaration. |
| C-37 | Version position labels present | **FAIL** | Headers have no position labels; standard "**Exec Version**", "**Dev Version**", "**Maker Version**". |

New criteria passes: 8/10 (C-28 through C-35)
Total aspirational: 28/30 → 28 × (10/30) = **9.33 pts**
**Composite: 60 + 30 + 9.33 = 99.3**

---

### V-05 — Full Synthesis (Maker-first + INERTIA PROFILE + DIFFERENTIATION GATE)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-28 | INERTIA PROFILE pre-step present | **PASS** | Named "Phase 5 INERTIA PROFILE" block before any version draft. |
| C-29 | INERTIA PROFILE cites AUDIENCE BELIEF MAP [Phase 2 gate output] | **PASS** | Template cites "AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row" with exact provenance brackets. |
| C-30 | INERTIA PROFILE gate stop present | **PASS** | "-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --" |
| C-31 | Why-It-Matters instructed to reflect INERTIA PROFILE arc | **PASS** | Cross-section constraint + per-version instructions. Exec: "Name the inertia arc from INERTIA PROFILE Exec sentence... 2-3 sentences ROI framing grounded in the inertia arc." Dev: "Name the inertia arc from INERTIA PROFILE Dev sentence. Show the before-state (Inertia Excuse) and the after-state (Inertia Counter)." Maker: "Name the inertia arc from INERTIA PROFILE Maker sentence in plain language." |
| C-32 | VERSION DIFFERENTIATION GATE present | **PASS** | Named post-step gate after all three versions. |
| C-33 | Gate uses structured 3-row table | **PASS** | 3-row table (Exec/Dev/Maker) with Core Belief summary, Hook type, Jargon check. |
| C-34 | Gate questions use YES/NO format with passing state | **PASS** | Three YES/NO questions, "Passing state: Q1=YES, Q2=NO, Q3=YES" declared. |
| C-35 | Gate has rewrite loop instruction | **PASS** | Explicit rewrite loop with structural stop: "rewrite the failing version. Re-fill the table. Re-answer all three questions. Repeat until passing state reached." |
| C-36 | Draft order Maker→Dev→Exec declared | **PASS** | "Draft order: Maker first, then Dev, then Exec." — explicit constraint-ascending declaration in Phase 5 preamble. |
| C-37 | Version position labels present | **PASS** | "**Maker Version** *(draft first)*", "**Dev Version** *(draft second)*", "**Exec Version** *(draft last)*" — all three headers labeled. |

New criteria passes: 10/10 (all)
Total aspirational: 30/30 → 30 × (10/30) = **10.0 pts**
**Composite: 60 + 30 + 10.0 = 100.0**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 | 60 | 30 | 30/30 = 10.0 | **100.0** | 1 |
| V-04 | 60 | 30 | 28/30 = 9.33 | **99.3** | 2 |
| V-01 | 60 | 30 | 24/30 = 8.0 | **98.0** | 3 (tied) |
| V-02 | 60 | 30 | 24/30 = 8.0 | **98.0** | 3 (tied) |
| V-03 | 60 | 30 | 22/30 = 7.33 | **97.3** | 5 |

All variations: essential fully passing. V-05 is the only variation to pass all R8 criteria.

---

## Diagnostic: Why V-03 Scores Lower Than V-01 and V-02

V-03 adds only 2 new criteria (C-36, C-37) vs. 4 each for V-01 and V-02. Draft order resequencing is a single structural change with a thin scorable surface: it declares the order and labels the positions. INERTIA PROFILE and DIFFERENTIATION GATE each introduce four-criterion groups because they add a named phase element with internal structural requirements (template provenance, gate stop, per-section constraints, table format, YES/NO questions, rewrite loop). Draft sequence reorganization adds fewer auditable structural properties than a new named phase element.

**Implication**: Maker-first is a quality mechanism, not a structure mechanism. Its discriminating power is at execution time (does the Maker version shape the message before exec framing is added?), not at skill-structure analysis time. C-36 and C-37 are the entire structural surface of that mechanism — a thin surface compared to INERTIA PROFILE or DIFFERENTIATION GATE. V-03's score is a prediction: the value of Maker-first shows up in outputs, not in structure criteria.

---

## Excellence Signals from V-05

**What V-05 achieves that no prior variation achieves:**

V-05 is the first variation where Phase 5 has the same pre-commit → constrained-fill → post-verify structure that Phase 2 acquired in R7 V-05. In R7, the BINDING DECLARATION gave Phase 2 three structural properties: intent (C-27), exhaustiveness (C-25), and bypass prohibition (C-26). In R8, V-05 gives Phase 5 three structural properties: a named pre-step that commits the inertia arc before drafting (INERTIA PROFILE), a constraint-ascending fill order that forces the hardest constraint first (Maker→Dev→Exec), and a named post-step that verifies structural compliance at exit (DIFFERENTIATION GATE).

**Pattern 1: Phase-level envelopment — a named pre-step + constrained fill order + named post-step makes a phase auditable from skill structure alone**
Phase 2 became auditable when the BINDING DECLARATION named its intent before the table was filled and declared its binding set closed after. Phase 5 becomes auditable in V-05 by the same mechanism: INERTIA PROFILE commits the arcs before drafting begins (prevents post-hoc rationalization of Why-It-Matters sections); Maker-first enforces the hardest constraint at entry (prevents exec framing from dominating the message); DIFFERENTIATION GATE verifies structural properties at exit (prevents semantic convergence from passing as audience differentiation). Each element addresses a distinct Phase 5 failure mode from skill structure, not from execution inspection.

**Pattern 2: Constraint-ascending draft sequence decouples message clarity from vocabulary permission**
EXEC OPENING SENTENCE is pre-committed at Phase 4 and used by exact reference regardless of draft order — Maker-first does not weaken the exec version. What it does is force the Core Belief to be expressible in plain language before technical and business framing are added. The position labels ("draft first/second/last") make the constraint order auditable: a reader can determine not just what was drafted but in what constraint order, enabling diagnosis of whether exec vocabulary was imported back into earlier versions.

**Pattern 3: Structural rewrite loop converts advisory quality instructions into pass/fail phase exits**
"Zero unexplained acronyms" and "show the tool, not the business case" existed as instructions in all prior versions. Without a gate, they are advisory — the skill can complete Phase 5 whether or not they are met. The DIFFERENTIATION GATE's YES/NO questions with declared passing state and explicit rewrite loop make them structural exits: Phase 5 cannot close unless Q2=NO (Maker has no unexplained acronyms) and Q3=YES (Dev opens with a scenario). The 3-row table requiring Core Belief summaries before the gate questions adds a verification step that makes it harder to answer Q1=YES when summaries are paraphrases.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-level envelopment: a named pre-step (INERTIA PROFILE) + constrained fill order (Maker-first) + named post-step (DIFFERENTIATION GATE) makes Phase 5 auditable from skill structure alone -- the same pre-commit/fill/close structure that made Phase 2 auditable in R7 V-05, now applied to Phase 5", "Constraint-ascending draft sequence decouples message clarity from vocabulary permission: Maker-first forces plain-language coherence before exec/dev framing is added; position labels (draft first/second/last) make the constraint order auditable from the skill text without execution inspection", "Structural rewrite loop converts advisory quality constraints into pass/fail phase exits: DIFFERENTIATION GATE YES/NO questions with declared passing state and explicit rewrite-until-pass loop make zero-jargon and scenario-hook structural stops, not instructions"]}
```
