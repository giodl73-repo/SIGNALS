## prove-program R7 Scoring — v6 Rubric

### Evaluation Framework

**Essential (C-01–C-05, 12 pts each = 60)**
**Recommended (C-06–C-08, 10 pts each = 30)**
**Aspirational (C-09–C-22, 5 pts each = 70)**
**Total ceiling: 160**

---

## V-01 — 2-Role Model (ARCHITECT → EXECUTOR)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Hypothesis pre-commitment | PASS | Phase 1 has named "Hypothesis:" in positive form + "Falsification:" before any experiment. ARCHITECT phase precedes EXECUTOR. |
| C-02 Experiment plan >=2 types | PASS | Phase 1B table requires distinct types per row; rationale column present. |
| C-03 Feed-forward | PASS | E-02 INPUT cites E-01 verbatim; Feed-Forward Audit Ledger tracks all outputs. |
| C-04 Synthesis contrast | PASS | "What we thought:" (verbatim hypothesis) + "What we actually learned:" (must differ). |
| C-05 Qx.md format + path | PASS | >=4 labeled sections; artifact path `simulations/prove/research/{{topic}}-research-{{date}}.md`. |
| C-06 Principles >=2 | PASS | Principles table: "Minimum 2 principles. No generic truisms. Source finding required per row." |
| C-07 Confidence levels | PASS | Findings table with `high / medium / low` per row; GATE-CAL enforces non-uniformity. |
| C-08 Flexibility beyond prove-topic | PASS | Phase 0 names prove-topic explicitly; lists 4 specific capability limitations. |
| C-09–C-17 (unchanged from v4) | PASS×9 | Inertia gap verdict in synthesis, cross-namespace routing, audit ledger, locked values in ARCHITECT COMPLETE block, contract delivery lines, per-experiment GATE-E{N}, frontmatter all present. |
| C-18 Phase-boundary gates >=2 | PASS | GATE-0 (inertia), GATE-1 (ARCHITECT→EXECUTOR boundary), GATE-P (plan→execution), GATE-CAL (findings→synthesis). 4 named gates. |
| C-19 >=3 inline FAIL conditions | PASS | GATE-1 FAIL, GATE-P FAIL, ledger FAIL, findings FAIL, GATE-CAL FAIL, contract delivery FAIL, principles FAIL. Far exceeds 3. |
| C-20 Conjunction gate | PASS | Two-row boolean table, Conditions A+B, "GATE-1 result: PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE)". Single PASS line. Atomic. |
| C-21 Calibration gate | PASS | GATE-CAL: "FAIL: All findings carry the same confidence level (all HIGH, all MEDIUM, or all LOW)." Named gate + named uniform-label FAIL. |
| C-22 Per-block citation contract | PASS | E-02 INPUT has local clause naming E-01 by name; PROHIBITED pointer forms listed. Additional-experiment note: "The citation contract travels with each consuming block's INPUT section, not in a shared global rule." |

**V-01 Score: 160/160**

---

## V-02 — Pure Prose (No Tables)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 1 **Hypothesis:** bold-labeled prose, positive form + **Falsification:** concrete evidence. Before any experiment. |
| C-02 | PASS | Phase 1B: E-01/E-02 labeled prose blocks each with Type + Rationale. "At least 2 distinct types required." |
| C-03 | PASS | E-02 INPUT prose block cites E-01 verbatim. Feed-Forward Audit section. |
| C-04 | PASS | Synthesis: **What we thought:** + **What we actually learned:** (must differ). |
| C-05 | PASS | Phases 0, 1, GATE-1, 1B, E-01, E-02, Feed-Forward Audit, Findings, GATE-CAL, Synthesis, Principles, Artifact — >=4. |
| C-06 | PASS | Principles: "Write at least 2 labeled, actionable principles... Cite the source finding for each." |
| C-07 | PASS | Findings as labeled prose blocks, each with confidence level + evidence basis. |
| C-08 | PASS | Phase 0 names prove-topic; lists acceptable gap types by name. |
| C-09–C-17 | PASS×9 | Full structural elements preserved in prose form: locked hypothesis, gap closure verdict, audit, frontmatter. |
| C-18 | PASS | GATE-0, GATE-1, GATE-P, GATE-CAL — all named as prose blocks at phase boundaries. |
| C-19 | PASS | GATE-0 FAIL, GATE-1 FAIL, GATE-P FAIL, findings FAIL, GATE-CAL FAIL, synthesis FAIL, principles FAIL. >=3. |
| C-20 | PASS | Prose GATE-1: "exactly two conditions. Both must be TRUE. One TRUE and one absent or FALSE is FAIL — the gate is **conjunctive, not a checklist.**" Conditions A+B each with TRUE/FALSE; single "**GATE-1 result: PASS** (A AND B = TRUE)" line. Atomic conjunction preserved in prose. |
| C-21 | PASS | GATE-CAL prose: "**FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).**" Named gate + named uniform-label pattern. |
| C-22 | PASS | E-02 INPUT prose: "citation contract (local to this block)... PROHIBITED in this INPUT section: 'see above', 'per E-01'..." Additional experiments: "contract is written locally in each consumer experiment's INPUT section — not in a shared global note." |

**V-02 Score: 160/160**

---

## V-03 — RFC Formal Spec Register (MUST/SHALL/PROHIBITED)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Section 2.1: "executor MUST state a single testable hypothesis... SHALL be expressed in positive form." Hypothesis + Falsification criterion before Section 3 plan. |
| C-02 | PASS | Section 3 table with Type + Rationale columns; "MUST contain experiments of >=2 distinct types. No two plan rows SHALL share the same type." |
| C-03 | PASS | Section 4.2 E-02 INPUT cites E-01 verbatim. Section 5.1 Feed-Forward Audit Ledger. |
| C-04 | PASS | Section 5.3: "What the executor believed going in:" + "What was actually learned: [MUST differ from hypothesis text]." |
| C-05 | PASS | Sections 1–6 with numbered subsections; artifact at correct path. |
| C-06 | PASS | Section 5.4 Principles: "MUST contain at least 2 principles... SHALL be specific and actionable." |
| C-07 | PASS | Section 5.2 Findings table with Confidence column; GATE-CAL. |
| C-08 | PASS | Section 1.1: prove-topic named with specific capability limitation requirement. |
| C-09–C-17 | PASS×9 | RFC normative language applied throughout; all structural elements present. |
| C-18 | PASS | GATE-0, GATE-1, GATE-P, GATE-CAL — each labeled as Section boundary constraints with MUST NOT advance language. |
| C-19 | PASS | GATE-0 FAIL condition, GATE-1 FAIL condition, GATE-P FAIL condition, GATE-CAL FAIL condition, contract delivery FAIL condition, synthesis FAIL condition. >=3. |
| C-20 | PASS | "**GATE-1 is an atomic conjunction. Both conditions MUST be TRUE. Partial satisfaction is PROHIBITED.**" Two-row table, A+B, "GATE-1 result: PASS (A AND B = TRUE)". RFC register makes the atomic requirement maximally explicit. |
| C-21 | PASS | GATE-CAL: "Presence of confidence labels is necessary but SHALL NOT be treated as sufficient." "FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW). The uniform-label pattern explicitly fails this gate." |
| C-22 | PASS | Section 4.1 states global preamble SHALL NOT satisfy requirement. Section 4.2 E-02: "MUST reproduce exact text... following forms are PROHIBITED in this INPUT subsection: 'see above', 'per E-01'..." Additional experiments: "citation contract SHALL be embedded locally per consuming block, not in a shared global rule." |

**V-03 Score: 160/160**

---

## V-04 — Pure Prose + Maximum Gate Density

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 1: **Hypothesis:** + **Falsification criterion:** labeled prose blocks before Phase 1B. |
| C-02 | PASS | Phase 1B: E-01/E-02 labeled blocks with Type + Rationale. "at least 2 distinct experiment types." |
| C-03 | PASS | Phase 2 E-02 INPUT cites E-01 verbatim. Phase 2+ ALL EXPERIMENTS COMPLETE → synthesis. |
| C-04 | PASS | Phase 4: **What we thought:** + **What we actually learned:** (must differ from hypothesis text). |
| C-05 | PASS | Phases 0–6; >=4 labeled sections; artifact at correct path. |
| C-06 | PASS | Phase 5: "Write at least 2 labeled, actionable principles drawn from the findings." |
| C-07 | PASS | Phase 3 findings with confidence per finding; GATE-CAL enforces differentiation. |
| C-08 | PASS | Phase 0 names prove-topic with acceptable gap types enumerated. |
| C-09–C-17 | PASS×9 | All structural elements present; gate density adds GATE-E{N} per experiment for maximum phase coverage. |
| C-18 | PASS | GATE-0, GATE-1 (Phase 1→1B), GATE-P (1B→Phase 2), GATE-E01, GATE-E02, GATE-CAL (Phase 3→4). Maximum density. >=2 confirmed. |
| C-19 | PASS | GATE-0 FAIL, GATE-1 FAIL, GATE-P FAIL, GATE-E01 FAIL (contract delivery), GATE-E02 FAIL (E-01 COMPLETE required), GATE-CAL FAIL, Phase 4 synthesis FAIL, Phase 5 principles FAIL. Prose format forces full sentence FAIL statements — increases verbosity and clarity. |
| C-20 | PASS | Phase 1 GATE-1 prose: "enforces two conditions simultaneously as a single conjunction — both must be true... **The gate is conjunctive: one condition TRUE and one FALSE is FAIL, not partial credit.** State both conditions and the result: Condition A — TRUE / FALSE; Condition B — TRUE / FALSE; GATE-1 result — PASS / FAIL." Atomic conjunction + single PASS line in pure prose. |
| C-21 | PASS | GATE-CAL prose: "**FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).**" Named gate + explicit uniform-label FAIL. |
| C-22 | PASS | Phase 2 global note: "You may not satisfy this requirement with a global note... the contract clause and verbatim content must appear in each consumer block's INPUT paragraph **individually**." E-02 INPUT: local citation contract clause with "prohibited in this INPUT paragraph: 'see above', 'per E-01'..." |

**V-04 Score: 160/160**

---

## V-05 — 3-Role (STRATEGIST/INVESTIGATOR/JUDGE) + RFC Register + Inertia Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | S-2 STRATEGIST Hypothesis: "MUST state a single testable hypothesis before naming any experiment. SHALL be in positive form." Hypothesis + Falsification criterion before any INVESTIGATOR experiment. |
| C-02 | PASS | S-3 plan table with Type + Rationale columns; ">=2 distinct types; no two rows SHALL share the same type." |
| C-03 | PASS | I-2 INPUT section cites E-01 verbatim. J-1 Feed-Forward Audit Ledger. |
| C-04 | PASS | J-3 Synthesis: "What we believed going in:" + "What we actually learned: [MUST differ from hypothesis text]." |
| C-05 | PASS | Role blocks STRATEGIST (S-1 through S-3), INVESTIGATOR (I-1, I-2), JUDGE (J-1 through J-5) — many labeled sections. |
| C-06 | PASS | J-4 Principles: "MUST produce at least 2 principles. SHALL be specific and actionable. Generic truisms SHALL NOT satisfy." |
| C-07 | PASS | J-2 Findings table with Confidence column; GATE-CAL enforces differentiation. |
| C-08 | PASS | S-1 delivers a capability map table (prove-topic can / prove-topic cannot) — the most thorough prove-topic treatment across all R7 variations. Gap must reference a specific "cannot" row. |
| C-09–C-17 | PASS×9 | Prove-topic benchmark quoted verbatim at every role boundary and in each consumer INPUT (I-1, I-2); STRATEGIST COMPLETE locked values block; J-1 audit; frontmatter; all elements present. |
| C-18 | PASS | GATE-S0, GATE-1 (STRATEGIST→INVESTIGATOR), GATE-P, GATE-STRATEGIST, GATE-INVESTIGATOR, GATE-CAL. Maximum role-boundary coverage. >=2. |
| C-19 | PASS | GATE-S0 FAIL, GATE-1 FAIL, GATE-P FAIL, GATE-STRATEGIST FAIL, contract delivery FAIL, GATE-CAL FAIL, J-3 synthesis FAIL. >=3. |
| C-20 | PASS | "**GATE-1 is an atomic conjunction. Both conditions MUST be TRUE. The gate MUST NOT be treated as two independent advisory checks.**" Two-row table, A+B with TRUE/FALSE, "GATE-1 result: PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE or absent)". RFC normative language + atomic conjunction. |
| C-21 | PASS | GATE-CAL: "Presence of confidence labels SHALL NOT be treated as sufficient." "**FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).**" Named gate + named uniform-label pattern. |
| C-22 | PASS | INVESTIGATOR preamble: "A global preamble SHALL NOT satisfy this requirement." I-2 INPUT: "MUST reproduce exact text of E-01's labeled finding... following forms are PROHIBITED." I-2 also carries verbatim prove-topic benchmark in INPUT (added axis). Additional experiments: "citation contract SHALL be embedded per consuming block, not in a global rule." |

**V-05 Score: 160/160**

---

## Ranking

| Rank | Variation | Score | Distinguishing Feature |
|------|-----------|-------|----------------------|
| 1 (tied) | V-01 | 160/160 | 2-role consolidation; GATE-1 becomes sole architectural checkpoint |
| 1 (tied) | V-02 | 160/160 | Zero tables; proves ceiling is format-agnostic |
| 1 (tied) | V-03 | 160/160 | RFC normative language makes PROHIBITED and atomic conjunction maximally explicit |
| 1 (tied) | V-04 | 160/160 | Prose + gate density; forces FAIL conditions into full verbose prose statements |
| 1 (tied) | V-05 | 160/160 | Deepest combinatorial pressure; prove-topic capability map travels as named benchmark at every role boundary |

All five score **160/160**. The prediction is confirmed: C-20, C-21, and C-22 are format-agnostic, register-agnostic, and role-count-agnostic structural properties.

---

## Excellence Signals

**Top variation for structural depth: V-05** (3-role + RFC + inertia framing)

**Pattern 1 — Capability map as traveling benchmark**: V-05's prove-topic capability map (two-column what-can / what-cannot table) at S-1.2 gets locked into STRATEGIST COMPLETE and then quoted verbatim at every role boundary (I-1 INPUT, I-2 INPUT, J-3 synthesis verdict). This makes C-08 structurally loadbearing rather than a one-time declaration — the benchmark cannot drift because it is a named artifact passed as a locked value.

**Pattern 2 — RFC PROHIBITED makes C-22 self-enforcing**: V-03/V-05's use of "PROHIBITED" (RFC 2119 normative) in the per-block citation contract clause (rather than imperative "do not") makes the anti-pointer prohibition feel like a specification constraint rather than a procedural instruction. Downstream consumers reading the template interpret it as a hard requirement of the spec, not a guideline.

**Pattern 3 — Conjunctive gate named as such in prose**: V-02 and V-04 demonstrate that the two-row table is not load-bearing for C-20. The key phrase "the gate is conjunctive, not a checklist" + "one condition TRUE and one FALSE is FAIL, not partial credit" carries the atomic conjunction in pure prose as effectively as a boolean table.

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": []}
```
