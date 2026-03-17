## prove-topic Round 5 — Scoring Report

---

### Rubric Recap (v5)

| Tier | Criteria | Weight each | Max |
|------|----------|-------------|-----|
| Essential | C-01–C-05 | 10 | 50 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-19 | 4 | 44 |
| **Total** | | | **124** |

Golden threshold: 80. All-essential PASS = 50 pts.

---

### V-01 — Lifecycle Emphasis (C-19 target)

PROTOCOL DECLARATION block with NULL-CE INVARIANT A and B before Stage 0. Explicit "committed here — applies regardless of what is found" and "pre-registered appointment — not a synthesis decision" language. Both invariants propagate forward through per-stage null-result notes. GATE S confirms both invariants on file. Synthesis has a single `If ALL stages null:` block containing both Invariant A execution (adversarial reviewer, block promotion) and Invariant B execution (CE-score = -2). No `co_activation_confirmed` field; no atomic block wrapper.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS (10) | All 5 stages present in fixed sequence |
| C-02 | PASS (10) | Stage 0 scout load with table |
| C-03 | PASS (10) | Write instruction at each stage |
| C-04 | PASS (10) | Stage 5 terminal with Protocol Compliance Verification, Counter-Evidence State, Findings, CE Register, Confidence, Handoff |
| C-05 | PASS (10) | Every artifact: `simulations/prove/{topic}/{topic}-{stage}-{date}.md` |
| C-06 | PASS (10) | "Do not open Stage 1 without this gate confirmed" — forward-only constraint |
| C-07 | PASS (10) | `scout_anchor: [slug from GATE S]` in hypothesis frontmatter |
| C-08 | PASS (10) | `next: topic-story` in Handoff section |
| C-09 | PARTIAL (2) | Null-CE propagation covered via pre-committed invariants; no thin (non-null) evidence propagation to synthesis |
| C-10 | PARTIAL (2) | Confirmations are "Artifact written: {topic}-…md — advance to STAGE N" — structural tokens, no narrative of what was found |
| C-11 | PASS (4) | GATE S: "Do not open Stage 1 without this gate confirmed and both invariants verified on file" — hard block before hypothesis |
| C-12 | PASS (4) | `status_quo_comparator` at PROTOCOL DECLARATION; referenced in Part B of Stages 2, 3, 4 |
| C-13 | PASS (4) | Every Write instruction has full path |
| C-14 | PASS (4) | "Counter-Evidence Register: MANDATORY" with null fallback pointing to protocol block |
| C-15 | PASS (4) | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | PASS (4) | Null path: Invariant A execution — Block: Promotion blocked; adversarial reviewer named |
| C-17 | PASS (4) | Invariant B: CE-score = -2 applied to composite; "confidence cannot be HIGH pending adversarial review" |
| C-18 | PARTIAL (2) | Both invariants appear inside the same `If ALL stages null:` block — shared entry condition, but sequential prose paragraphs with no `co_activation_confirmed` field and no atomic wrapper. Structural co-activation implicit, not enforced |
| C-19 | PASS (4) | PROTOCOL DECLARATION names Invariant A and B as session-level invariants before Stage 0. "Do not modify after this point" language present |

**Score: 50 + 30 + (2+2+4+4+4+4+4+4+4+2+4) = 50 + 30 + 38 = 118 / 124**

---

### V-02 — Output Format (C-18 target)

CAMPAIGN OPEN registers `adversarial_reviewer_type` and `ce_penalty_rule` with "Both fields mandatory. Do not proceed without filling both" — registration language, not invariant language. Stage 5 uses the ATOMIC DUAL-LOCK ACTIVATION block: one trigger condition, both LOCK A (confidence cap) and LOCK B (adversarial escalation) as required outputs. `co_activation_confirmed: true` inside the block; `co_activation_confirmed: [must equal dual_lock_fired]` in Handoff enforces integrity. Stage 4 has no null-result note.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS (10) | |
| C-02 | PASS (10) | |
| C-03 | PASS (10) | |
| C-04 | PASS (10) | Terminal with CE State Collection, ATOMIC DUAL-LOCK, Findings, CE Register, Confidence, Handoff |
| C-05 | PASS (10) | |
| C-06 | PASS (10) | |
| C-07 | PASS (10) | `scout_anchor: [slug from GATE S]`, `gate_s_cleared: true` in hypothesis |
| C-08 | PASS (10) | `next: topic-story` in Handoff |
| C-09 | PARTIAL (2) | No thin-evidence propagation for non-null cases; Stage 4 has no null note |
| C-10 | PARTIAL (2) | Confirmations are structural tokens; no per-stage narrative |
| C-11 | PASS (4) | "Do not open Stage 1 without this gate confirmed" |
| C-12 | PASS (4) | Comparator at CAMPAIGN OPEN; referenced at each evidence stage Part B |
| C-13 | PASS (4) | Full paths in every Write instruction |
| C-14 | PASS (4) | Mandatory CE Register; null case defers to ATOMIC DUAL-LOCK block |
| C-15 | PASS (4) | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | PASS (4) | LOCK B: escalation_triggered: true; Block: Promotion blocked; reviewer named |
| C-17 | PASS (4) | LOCK A: CE-score = -2, cap_applied: true; "HIGH is not available when CE-score = -2" |
| C-18 | PASS (4) | ATOMIC DUAL-LOCK: "Both locks activate from this single entry. Partial activation is a format error." `co_activation_confirmed` required. Both LOCK A and LOCK B are outputs of same block entry |
| C-19 | PARTIAL (2) | Both fields registered before Stage 0 — but language is "Register before any stage begins. Both fields mandatory" — registration framing, not invariant/pre-commitment framing. No "cannot be modified" or "session-level invariant" language |

**Score: 50 + 30 + (2+2+4+4+4+4+4+4+4+4+2) = 50 + 30 + 38 = 118 / 124**

---

### V-03 — Phrasing Register (C-19 propagation)

SESSION INVARIANT REGISTRY declared "before Stage 0 — binding for the full session." Language throughout: "pre-registered", "cannot be modified or bypassed at synthesis time", "session-level commitment", "not a synthesis decision." GATE S confirms both invariants via `invariant_registry_confirmed: true`. Null-result notes at Stages 2, 3, 4 carry "Running tally" language and reference both invariants explicitly, framed as "pre-committed session obligations, not conditional judgments." Synthesis uses a single `if activation condition fires:` block executing Session Invariant A (adversarial escalation) and Session Invariant B (CE-score = -2) sequentially. No ATOMIC DUAL-LOCK structure, no `co_activation_confirmed`.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS (10) | |
| C-02 | PASS (10) | |
| C-03 | PASS (10) | |
| C-04 | PASS (10) | Terminal: Invariant Retrieval, CE State+Protocol Execution, Findings, CE Register, Confidence, Handoff |
| C-05 | PASS (10) | |
| C-06 | PASS (10) | |
| C-07 | PASS (10) | `scout_anchor: [slug from GATE S]` in hypothesis |
| C-08 | PASS (10) | `next: topic-story` in Handoff |
| C-09 | PARTIAL (2) | Null-CE propagation carried through per-stage running tallies; thin (non-null) evidence not addressed in synthesis |
| C-10 | PARTIAL (2) | Null-path notes have richer prose ("Running tally: S2 null. Two stages remain…"), but non-null confirmations remain structural tokens |
| C-11 | PASS (4) | "Do not open Stage 1 without both items confirmed" (gate_s_cleared + invariant_registry_confirmed) |
| C-12 | PASS (4) | Comparator at SESSION INVARIANT REGISTRY; referenced at each evidence stage |
| C-13 | PASS (4) | Full paths in every Write instruction |
| C-14 | PASS (4) | MANDATORY CE Register with null fallback |
| C-15 | PASS (4) | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | PASS (4) | "Session Invariant A executing: Effect: Promotion blocked. escalation_triggered: true" |
| C-17 | PASS (4) | "Session Invariant B executing: CE-score = -2 (pre-committed formula — not a narrative judgment). High confidence unavailable while escalation_triggered." |
| C-18 | PARTIAL (2) | Both invariants fire inside same `if activation condition fires:` block — sequential paragraphs, no atomic wrapper, no `co_activation_confirmed` field. Co-activation implicit via shared entry condition, not structurally enforced |
| C-19 | PASS (4) | SESSION INVARIANT REGISTRY: "Declared before Stage 0 — binding for the full session." Invariant A: "pre-registered…at synthesis, this is execution — not appointment." Invariant B: "pre-registered formula. Cannot be overridden, softened, or bypassed by narrative judgment at synthesis." Full pre-commitment language for both |

**Score: 50 + 30 + (2+2+4+4+4+4+4+4+4+2+4) = 50 + 30 + 38 = 118 / 124**

---

### V-04 — Protocol Manifest + Atomic Dual-Lock (direct C-18 + C-19)

CAMPAIGN OPEN — PROTOCOL MANIFEST with three invariants: A (adversarial reviewer, pre-commitment language), B (CE-score formula, "locked in"), C (co-activation rule — A and B fire together; partial activation = protocol violation). GATE S 6-checkbox checklist includes all three invariants before Stage 1 can open. Stage 5 ATOMIC DUAL-LOCK with `co_activation_confirmed: true` and INVARIANT C enforcement language: "Exit without both = protocol violation." Does NOT carry evidence ledger, per-stage scoring, or prototype thin check from R4 V-05.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS (10) | |
| C-02 | PASS (10) | |
| C-03 | PASS (10) | |
| C-04 | PASS (10) | Terminal: Protocol Manifest Verification, CE State, ATOMIC DUAL-LOCK, Findings, CE Register, Confidence, Handoff |
| C-05 | PASS (10) | |
| C-06 | PASS (10) | |
| C-07 | PASS (10) | `scout_anchor: [slug from GATE S]`, `gate_s_cleared: true` |
| C-08 | PASS (10) | `next: topic-story` in Handoff |
| C-09 | PARTIAL (2) | Null-CE tracked per-stage and fires dual-lock at synthesis. No thin (non-null) evidence propagation mechanism; Stage 4 has no null note at all |
| C-10 | PARTIAL (2) | Stage 3 null note is brief one-liner; Stage 4 has no null note; confirmations are structural tokens |
| C-11 | PASS (4) | GATE S 6-checkbox: "Do not open Stage 1 without all six items confirmed" |
| C-12 | PASS (4) | Comparator at CAMPAIGN OPEN PROTOCOL MANIFEST; referenced in Part B of all three evidence stages |
| C-13 | PASS (4) | Full paths in every Write instruction |
| C-14 | PASS (4) | MANDATORY CE Register; null case: "recorded in ATOMIC DUAL-LOCK ACTIVATION block above" |
| C-15 | PASS (4) | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | PASS (4) | LOCK B: escalation_triggered: true; Block: Promotion blocked; reviewer from protocol manifest |
| C-17 | PASS (4) | LOCK A: CE-score = -2 (pre-committed Invariant B formula); cap_applied: true; "Ceiling: MEDIUM maximum. HIGH not available while escalation_triggered." |
| C-18 | PASS (4) | ATOMIC DUAL-LOCK: one entry condition (all three null), both LOCK A and LOCK B required outputs. "Exit without both = protocol violation (Invariant C)." `co_activation_confirmed: true` inside block; Handoff confirms `co_activation_confirmed must equal dual_lock_fired` |
| C-19 | PASS (4) | CAMPAIGN OPEN PROTOCOL MANIFEST: "Both null-CE protocols are committed here. Cannot be modified after this point." Invariant A: "pre-commitment: this reviewer is named here. At synthesis, this is not an appointment — it is execution." Invariant B: "pre-commitment: this formula is locked in. At synthesis, it is not a judgment — it is the formula executing. Verbal override is not permitted." |

**Score: 50 + 30 + (2+2+4+4+4+4+4+4+4+4+4) = 50 + 30 + 40 = 120 / 124**

---

### V-05 — Full Excellence Compound (R4 V-05 + C-18 + C-19)

Combines R4 V-05 mechanisms (evidence ledger with per-stage scoring, prototype thin cap, 6-item GATE S, prototype cap WARNING propagated to synthesis) with R5 additions (CAMPAIGN OPEN → PROTOCOL MANIFEST with invariant language for C-19; LOCK 1/LOCK 2 → ATOMIC DUAL-LOCK for C-18). Three declared invariants (A: reviewer, B: cap formula, C: co-activation rule). Evidence ledger tracks `web_search: 30%, intelligence: 30%, prototype: 40%` with quality and score per stage. Stage 4 has explicit "WARNING: Prototype (40% weight) is Thin. Final composite capped at 6.9" — propagates to synthesis via `prototype_cap` field and Evidence Ledger Final table. Synthesis has Protocol Manifest Verification, CE State Collection, ATOMIC DUAL-LOCK, Evidence Ledger Final, Findings, CE Register, Status-Quo Comparison, Composite Confidence, Handoff.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS (10) | All 5 stages in fixed sequence |
| C-02 | PASS (10) | Stage 0 scout load |
| C-03 | PASS (10) | Write instruction at every stage |
| C-04 | PASS (10) | Stage 5 terminal with complete required sections; "No stages follow this one" |
| C-05 | PASS (10) | Full paths throughout; Confirm statements also name full path |
| C-06 | PASS (10) | Fixed sequence; 6-item GATE S blocks Stage 1 |
| C-07 | PASS (10) | `scout_anchor: [slug from GATE S]` AND `scout_path: [full path from GATE S]` in hypothesis |
| C-08 | PASS (10) | `next: topic-story` with `ready: [true / false — if false, specify blocker]` |
| C-09 | PASS (4) | Stage 4 thin check: "WARNING: Prototype (40% weight) is Thin. Final composite capped at 6.9 (MEDIUM max)." Synthesis: Evidence Ledger Final has `Prototype cap applied: [yes / no]`; Composite Confidence has `Prototype cap: [yes / no]`. Thin-evidence flag at Stage 4 propagated to synthesis and qualifies the confidence formula |
| C-10 | PASS (4) | Each evidence stage records: stage score / 10, counter-evidence found, evidence quality (Strong/Moderate/Thin), ledger update, formula update. Multi-field structured assessment per stage goes beyond verdict tokens. Null-result notes add prose narrative |
| C-11 | PASS (4) | GATE S 6-item checklist; "Do not open Stage 1 until all six items confirmed" |
| C-12 | PASS (4) | Comparator at PROTOCOL MANIFEST; referenced in Part B of Stages 2, 3, 4; Stage 4 WARNING traces thin evidence to synthesis via prototype_cap; Synthesis has Status-Quo Comparison section |
| C-13 | PASS (4) | Every Write instruction and Confirm statement uses full path `simulations/prove/{topic}/{topic}-{stage}-{date}.md` |
| C-14 | PASS (4) | "Counter-Evidence Register: MANDATORY. Null result is not suppressed. Uniformly supportive evidence is a campaign integrity flag." |
| C-15 | PASS (4) | `gate_s_cleared: true` in hypothesis frontmatter |
| C-16 | PASS (4) | LOCK B: adversarial escalation; `escalation_triggered: true`; `escalation_state: triggered`; Block: Promotion blocked |
| C-17 | PASS (4) | LOCK A: CE-score = -2 (pre-committed formula); `cap_applied: true`; prototype cap check inside block; Evidence Ledger Final computes final composite after CE-score penalty; "Level (from formula — no override)" |
| C-18 | PASS (4) | ATOMIC DUAL-LOCK: "PRE-COMMITTED PROTOCOL EXECUTING per Invariant C — both locks must fire. A synthesis output that exits this block with only one lock active is a protocol violation (Invariant C)." `co_activation_confirmed: true`; Handoff: `co_activation_confirmed: [must equal dual_lock_fired]` |
| C-19 | PASS (4) | CAMPAIGN OPEN PROTOCOL MANIFEST: "Both null-CE protocols are committed here. Cannot be modified after this point." Invariant A: "This reviewer is pre-registered now — not appointed at synthesis." Invariant B: "This formula is a session-level commitment. Verbal override not permitted." |

**Score: 50 + 30 + (4+4+4+4+4+4+4+4+4+4+4) = 50 + 30 + 44 = 124 / 124**

---

### Rankings

| Rank | Variation | Score | Delta from 80 |
|------|-----------|-------|---------------|
| 1 | V-05 | 124/124 | +44 |
| 2 | V-04 | 120/124 | +40 |
| 3 | V-01 | 118/124 | +38 |
| 3 | V-02 | 118/124 | +38 |
| 3 | V-03 | 118/124 | +38 |

All five variations exceed the golden threshold (80). V-05 achieves the first perfect score in this series.

---

### Separation Analysis

**V-04 over V-01/V-02/V-03 (+2 pts):**
Both C-18 and C-19 PASS in a combined design, vs. each single-axis variation earning one PASS and one PARTIAL. The protocol manifest (C-19) and atomic dual-lock (C-18) address different failure modes and do not conflict — combining them costs nothing and closes both gaps.

**V-05 over V-04 (+4 pts):**
The evidence ledger (per-stage scoring + quality tracking) is the mechanism that unlocks full C-09 and C-10. Without it:
- C-09 stays PARTIAL because non-null thin evidence has no typed propagation path to synthesis
- C-10 stays PARTIAL because confirmations remain structural tokens

The prototype thin check at Stage 4 (`prototype_cap: true` + WARNING label) creates a machine-readable state that synthesis can reference programmatically in the Evidence Ledger Final table — converting "thin evidence" from a prose note that may be forgotten into a field that the confidence formula mechanically consumes.

---

### Excellence Signals from V-05

**Signal 1 — Evidence scoring infrastructure as the thin-evidence propagation mechanism**
The per-stage scoring ledger (quality: Strong/Moderate/Thin, score/10, weight) is not primarily a scoring tool — it is the infrastructure that makes C-09 and C-10 achievable. Each stage's structured output (score, quality, ledger update) constitutes the "explicit natural-language confirmation" C-10 requires, and the `prototype_cap` field creates the typed link C-09 requires. The ledger makes thin evidence measurable and traceable without requiring extra synthesis prose.

**Signal 2 — WARNING + typed field converts prose flag to machine-readable state**
Stage 4: "If prototype quality is Thin: Set `prototype_cap: true`. WARNING: Prototype (40% weight) is Thin. Final composite capped at 6.9 (MEDIUM max)." The WARNING label creates a hard protocol break (not just a note) and the `prototype_cap: true` field is a typed boolean that synthesis consumes directly in the Evidence Ledger Final. The thin-evidence signal is no longer a prose statement that synthesis might override — it is a typed state field with a formula consequence.

**Signal 3 — Three-invariant protocol manifest closes the co-activation pre-commitment gap cleanly**
INVARIANT C (co-activation rule: "A and B fire together from one trigger; partial activation is a protocol violation") is declared at CAMPAIGN OPEN as a third session-level invariant. This creates a named, pre-committed obligation for co-activation — the ATOMIC DUAL-LOCK at synthesis is now executing a pre-committed contract, not just applying a structural format. The invariant declaration is the upstream commitment; the atomic block is the downstream execution.

---

```json
{"top_score": 124, "all_essential_pass": true, "new_patterns": ["evidence scoring ledger (per-stage score/quality/weight) is the mechanism that enables C-09 and C-10 full PASS — measurement infrastructure replaces separate thin-evidence prose checks", "WARNING + typed prototype_cap field converts thin-evidence note into machine-readable state with formula consequence, making propagation to synthesis structural rather than narrative"]}
```
