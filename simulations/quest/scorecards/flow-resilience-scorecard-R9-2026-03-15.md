## Flow-Resilience Skill — Round 9 Scoring (Rubric v9)

**Variations**: V-01 through V-05 in `flow-resilience-variate-R9-2026-03-15.md`
**New criteria entering R9**: C-29 (Rule-Bypass-Triggered Gate Reopening), C-30 (Multi-Act Completion Sign-Off)

---

## Criterion-by-Criterion Scoring

### Essential (C-01 through C-05) — shared across all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|---|---|---|---|---|---|---|
| C-01 Three Degradation Classes | PASS | PASS | PASS | PASS | PASS | Coverage Accountability Roster commits to all three classes in every variation |
| C-02 Four-Field Structure | PASS | PASS | PASS | PASS | PASS | Gate 2 enforces all four fields in every variation |
| C-03 Gap Identification (Three Types) | PASS | PASS | PASS | PASS | PASS | Gate 3 OEG/DCV/MRF sections present in all |
| C-04 Distributed Systems Accuracy | PASS | PASS | PASS | PASS | PASS | Correct DS vocabulary throughout; no fabricated guarantees |
| C-05 Commerce Domain Grounding | PASS | PASS | PASS | PASS | PASS | Scope declaration requires 4+ named commerce operations |

**Essential subtotal**: 60/60 for all five variations. All essential criteria pass.

---

### Recommended (C-06 through C-08) — shared across all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|---|---|---|---|---|---|---|
| C-06 Severity & Blast Radius | PASS | PASS | PASS | PASS | PASS | Gate 2 explicitly annotates both in all variations |
| C-07 Actor-Labeled Recovery Paths | PASS | PASS | PASS | PASS | PASS | Minimum two named-actor steps per recovery path enforced in all |
| C-08 Conflict Resolution Strategy | PASS | PASS | PASS | PASS | PASS | Gate 3 conflict resolution analysis with adequacy verdict in all |

**Recommended subtotal**: 30/30 for all five variations.

---

### Aspirational (C-09 through C-30) — differentiation zone

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-09 Chaos Engineering | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-10 Observability Hooks | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-11 Confidence-Annotated Discovery | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-12 Nil-Finding Norm | PASS | PASS | PASS | PASS | PASS |
| C-13 Coverage Accountability Roster | PASS | PASS | PASS | PASS | PASS |
| C-14 CR Adequacy as DCV Source | PASS | PASS | PASS | PASS | PASS |
| C-15 DS-Primitive Impossibility Args | **PASS** | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-16 Named Gate-State Vocabulary | PASS | PASS | PASS | PARTIAL | PASS |
| C-17 Permanently Barred as Coverage Gaps | PASS | PASS | PASS | PASS | PASS |
| C-18 Explicit Phase Entry/Exit Conditions | PASS | PASS | PASS | **FAIL** | PASS |
| C-19 Gate Blockage Transparency (Reason-if-OPEN) | PASS | PASS | PASS | **FAIL** | PARTIAL |
| C-20 Downstream Gate Amendment with Re-Close | PASS | PASS | PASS | PASS | PASS |
| C-21 Pre-Analysis Commerce Scope Declaration | PASS | PASS | PASS | PASS | PASS |
| C-22 Typed Nil-Finding Identifiers | PASS | PASS | PASS | PASS | PASS |
| C-23 Scope Declaration Closure Bracket | PASS | PASS | PASS | PASS | PASS |
| C-24 Template-Embedded Conditional Linkage Rules | PASS | PASS | PASS | PASS | PASS |
| C-25 Nil-Finding Supersession Protocol | PASS | PASS | PASS | PASS | PASS |
| C-26 Confidence Triage Resolution Sub-Gate | PASS | PASS | PASS | PARTIAL | PASS |
| C-27 Named Rule Block Registry | PASS | PASS | PASS | PASS | PASS |
| C-28 Post-Analysis Rule Registry Audit | PASS | PASS | PASS | PASS | PASS |
| C-29 Rule-Bypass-Triggered Gate Reopening | PASS | PASS | PASS | PASS | PASS |
| C-30 Multi-Act Completion Sign-Off | PASS | PARTIAL | PASS | PARTIAL | PASS |

**Evidence notes for key criteria:**

**C-11 PARTIAL (all)**: Every variation uses Include/BARRED/Argued-Impossible disposition with Confidence Basis column. The mechanism aligns with C-11 intent, but the rubric requires explicit high/medium/low/impossible rating vocabulary. No variation uses that vocabulary. All PARTIAL (1).

**C-15**: V-01 only has inline VALID/INVALID annotated examples: `VALID: "Under CP topology, network partitions prevent divergent writes." INVALID: "The topic doesn't mention caching."` — exactly what C-15 pass condition requires. V-02 has "DS Primitive must name a specific architecture constraint. 'Topic doesn't mention X' is invalid" but no named "DS Primitive cited:" field with annotated examples → PARTIAL. V-03–V-05: only the column or prose instruction without annotated examples → PARTIAL.

**C-16**: V-04 uses conversational "GATE N STATUS: CLOSED when..." definitions rather than per-run binary OPEN/CLOSED declarations. PARTIAL (1). All others have explicit OPEN/CLOSED binary declarations.

**C-18**: V-04 has no gate entry conditions citing prior gate identifiers. "Work through five gates in order" is not equivalent. FAIL (0). All others have explicit "Entry condition: GATE N STATUS: CLOSED" or GATE-OPEN blocks with precondition checklists.

**C-19**: V-04 has no "Reason if OPEN:" fields (gate status defined by condition, not declared). FAIL (0). V-05 has `Gate N STATUS: CLOSED / OPEN` without a "Reason if OPEN:" line in its GATE CLOSE blocks → PARTIAL (1). V-01, V-02, V-03 all have explicit "Reason if OPEN: [blocking condition]" fields → PASS.

**C-26**: V-04 describes BARRED resolution in prose ("can any BARRED entry be resolved? If yes, record the resolution") without a labeled GATE 1b: RESOLVED sub-gate. PARTIAL (1).

**C-29 (new)**: All variations pass. V-01: "Bypass Gate-Reopening Protocol (DS Expert Authority)" is a named pre-analysis section with numbered steps, bypass chain structure, and explicit "COMPLETE may not be declared while any RULE-BYPASSED entry remains unresolved." V-02: BYPASS-TRIGGER column forces non-empty cell beside every RULE-BYPASSED row, making bypass detection scannable by column audit. V-03: `GATE N-bypass: REOPENED / AMENDED -- CLOSED` blocks within registry audit OPEN/CLOSE envelope. V-04: numbered imperative steps in terminal audit with "do not proceed to COMPLETE." V-05: BYPASS-TRIGGER column + named Bypass Owner column + GATE N-bypass protocol.

**C-30 (new)**: V-01, V-03, V-05 are multi-act → dual sign-off with all three items (gates CLOSED, scope exhausted, no RULE-BYPASSED) → PASS. V-02, V-04 are single-act with explicit N/A declarations ("C-30 note: This analysis is single-act. C-30 scores N/A (PARTIAL)") → PARTIAL (1).

---

## Uncapped Aspirational Scores

| Variation | Uncapped Aspirational | Capped | Composite |
|---|---|---|---|
| V-01 | 41 | 10 | **100** |
| V-03 | 40 | 10 | **100** |
| V-02 | 39 | 10 | **100** |
| V-05 | 39 | 10 | **100** |
| V-04 | 31 | 10 | **100** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational (capped) | Composite |
|---|---|---|---|---|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

All five variations clear the golden threshold (all essential pass + composite ≥ 80). The cap absorbs all aspirational differences at the composite level; differentiation is visible only in uncapped aspirational totals.

---

## Ranking

**1. V-01** — 41 uncapped
- Only variation with inline VALID/INVALID annotated impossibility argument examples (C-15 PASS, sole differentiator from V-03)
- Bypass protocol as a named pre-analysis section with DS Expert ownership explicitly declared before any gate opens
- "Reason if OPEN:" present on every gate status declaration (C-19 PASS)
- Full dual per-act sign-off (C-30 PASS)

**2. V-03** — 40 uncapped
- Structural GATE-OPEN/GATE-CLOSE blocks with precondition checklists make entry and exit independently auditable (C-18 PASS, C-19 PASS via "Reason if OPEN" in every GATE CLOSE)
- ACT-OPEN/ACT-CLOSE blocks enforce C-30 structurally — an analyst who omits ACT-CLOSE leaves an open act visible at scan time
- Misses V-01's VALID/INVALID impossibility argument examples (C-15 PARTIAL, -1 vs V-01)

**3. V-02** — 39 uncapped (tied with V-05)
- BYPASS-TRIGGER column makes C-29 detectable by column scan — eliminates the possibility of soft-pedaling bypass events in prose
- Single-act (C-30 PARTIAL, -1 vs V-01)
- No VALID/INVALID impossibility argument examples (C-15 PARTIAL, -1 vs V-01)

**4. V-05** — 39 uncapped (tied with V-02)
- Full integration: role sequence + ACT-CLOSE blocks + BYPASS-TRIGGER column + Status-Quo Carrying Cost column
- Bypass Owner column in RULE REGISTRY assigns bypass remediation responsibility per rule before analysis
- Missing "Reason if OPEN:" in GATE CLOSE blocks (C-19 PARTIAL, -1 vs V-03) and no VALID/INVALID examples (C-15 PARTIAL)

**5. V-04** — 31 uncapped
- Conversational/imperative register reduces formal gate structure — C-16 PARTIAL, C-18 FAIL, C-19 FAIL, C-26 PARTIAL
- Inertia framing and Status-Quo Carrying Cost are structurally excellent and transfer to V-05
- Single-act (C-30 PARTIAL)
- Still hits aspirational cap at composite; structural gaps are above the ceiling

---

## Excellence Signals from V-01 (Top Variation)

**Signal 1 — Inline VALID/INVALID impossibility argument examples make the DS-primitive requirement unambiguous.** The coverage accountability roster in V-01 contains: `VALID: "Under CP topology, network partitions prevent divergent writes." INVALID: "The topic doesn't mention caching."` This template-embedded distinction closes the gap between an analyst who understands "architecture argument not description absence" and one who doesn't. No other variation has this.

**Signal 2 — Bypass authority declared as a named pre-analysis section, not inline at the terminal.** V-01 opens with a standalone "Bypass Gate-Reopening Protocol (DS Expert Authority)" section that (a) names the owning role, (b) states what Commerce Validator cannot do ("cannot invoke bypass gate-reopening for Act 1 gates"), and (c) walks through the four-step chain. When the analyst reaches the terminal audit, the protocol is already committed — there is no ambiguity about what RULE-BYPASSED forces.

**Signal 3 — Role split at bypass ownership creates single-owner accountability per act.** DS Expert owns all Act 1 bypass events; Commerce Validator owns Act 2 bypass events and cannot re-open Act 1 gates. This prevents bypass events from falling into a "who handles this" gap that a single-analyst template can ignore.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["bypass-authority-as-named-pre-analysis-section", "role-scoped-bypass-ownership-per-act"]}
```
