## Round 3 Scorecard — flow-throttle

**Result: 4 variations hit 118/118 ceiling. All essentials pass.**

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-02 C-15 isolation | **118** | YES |
| 1 | V-03 C-16 isolation | **118** | YES |
| 1 | V-04 C-15+C-16 co-location | **118** | YES |
| 1 | V-05 Full synthesis | **118** | YES |
| 5 | V-01 C-14 isolation | **~102** | NO |

---

### Key findings

**V-01 diagnostic:** Gate syntax works in prose without tables or roles. C-14 PASS confirmed. Inherited C-12 FAIL (only risk register in table form, 1/5) is the binding deficit. Partial scores on C-02 (prose, no comparison column), C-05 (trailing soft PA check), C-11, C-15, C-16 pull it to ~102.

**V-02 minimum-mechanism confirmation:** A single prepended sentence — "Do not assume Round 1 was accurate because constructs appeared to validate without correction" — is the complete C-15 mechanism. Imperative + named prior layer + confidence-not-evidence = sufficient. One sentence, no redesign.

**V-03 minimum-mechanism confirmation:** A scope declaration naming three construct populations with structural reason ("introduced after ROLE 1's construct-definition window had already closed") closes C-16 alone. The closure reason is load-bearing — "review all constructs" without structural reason does not pass.

**V-04 co-location finding:** C-15 and C-16 labeled as distinct subsections ("Independence:" / "Scope extension:") within a single preamble block score as two independent criteria. Labels prevent collapse. A single ROLE 2 preamble can carry both without point penalty.

**V-05 ceiling confirmation:** All six criteria named at top and embedded at point-of-use. PHASE 4.A carries both C-15 and C-16. The C-15 uncertainty ("GATE 1 is not a named role — does the non-deference pass?") resolves YES: GATE 1 is a named labeled layer and the sentence references it by name.

```json
{"top_score": 118, "all_essential_pass": true, "new_patterns": ["Single non-deference sentence is the minimum C-15 mechanism -- one imperative sentence naming the prior layer before second barrier opens is sufficient, no structural redesign required", "Named construct populations with structural closure reason satisfy C-16 alone -- 3 categories plus introduced-after-window justification closes the criterion", "C-15 and C-16 compose as independent criteria when labeled as distinct blocks in one preamble -- co-location does not collapse them, labels are structurally load-bearing", "Named GATE plus explicit Block-section sentence is the complete C-14 formula -- works in prose without tabular structure or role separation, distinguishes conditional instruction from advice"]}
```
ths (STEP 6), and cascade (STEP 7) are all prose. 1/5 eligible criteria in table form -- below the two-table threshold. |
| C-13 | aspirational (3) | 3 | PASS | STEP 2 plants [INERTIA-SEED] label. STEP 7 opens "The [INERTIA-SEED] assumption breaks here: ..." and GATE 3 structurally blocks STEP 8 until [INERTIA-SEED] is cited with broken assumption restated. Both ends enforced. |
| C-14 | aspirational (3) | 3 | PASS | Three named conditional gates: GATE 1 ("Block: STEP 2 is blocked"), GATE 2 ("Block: STEP 7 is blocked"), GATE 3 ("Block: STEP 8 is blocked"). Each states explicit prerequisite conditions. Section headings alone would not satisfy; gates are conditional go/no-go instructions. |
| C-15 | aspirational (3) | 1.5 | PARTIAL | No explicit non-deference sentence in STEP 9 or elsewhere. The per-construct required format ("confirmed / corrected to") implies independence but does not state it as an imperative. Partial credit for structural implication without explicit instruction. |
| C-16 | aspirational (3) | 1.5 | PARTIAL | STEP 9 covers "STEPS 1-9" which implicitly includes constructs introduced in STEPS 4, 6, 7 beyond GATE 1's STEP 1 scope. But STEP 9 does not explicitly declare which construct categories are new to its scope window or why GATE 1 could not have covered them. Scope is wider but not named. |

**V-01 Total: 101.9 / 118**

**Why V-01 is diagnostic:** Confirms C-14 gate syntax works independently of tabular structure and role separation. All other deficits (C-02, C-05, C-11, C-12, C-15, C-16) are inherited from the prose-imperative base. Not a ceiling candidate -- a gate-mechanism proof with known inherited weaknesses.

---

### V-02 — Single-axis: Validator Independence Assertion

Base: V-03 R2 (five tables, GATE 1, Round 1/Round 2 with scope declaration). Added: "Do not assume Round 1 was accurate because constructs appeared to validate without correction. Round 1's confidence is not evidence of Round 1's precision. Treat Round 1's accepted construct names as unverified at the start of this review."

| ID | Weight | Pts | Result | Evidence |
|----|--------|-----|--------|----------|
| C-01 | essential (12) | 12 | PASS | TABLE 1 bottleneck statement requires PA construct, volume, and naive-assumption sentence. |
| C-02 | essential (12) | 12 | PASS | TABLE 2 with "Why this order holds at scenario volume" column enforces ordering rationale column-by-column. |
| C-03 | essential (12) | 12 | PASS | TABLE 3 backpressure hop chain with signal-type and response-behavior columns. |
| C-04 | essential (12) | 12 | PASS | UX section requires per-tier mapping with categories-must-differ rule. |
| C-05 | essential (12) | 12 | PASS | Domain rule + Round 1 per-construct validation (GATE 1 blocks TABLE 2 until complete). |
| C-06 | recommended (10) | 10 | PASS | TABLE 4 burst path enumeration with PA construct and bypass-reason columns. |
| C-07 | recommended (10) | 10 | PASS | Retry-After gaps section with consumer/behavior/consequence required. |
| C-08 | recommended (10) | 10 | PASS | TABLE 5 cascade sequence with causal mechanism and failure mode; cascade resolution statement required. |
| C-09 | aspirational (5) | 5 | PASS | TABLE 6 risk register with Status derived from numeric comparison. |
| C-10 | aspirational (5) | 5 | PASS | PA-specific remediations table; "Add retries" / "reduce load" excluded. |
| C-11 | aspirational (3) | 3 | PASS | Round 1 (after TABLE 1) validates tier-map constructs; Round 2 (after remediations) validates all constructs including TABLE 3-5 additions. Different scopes; both per-construct and mandatory. Batch confirmation prohibited at both barriers. |
| C-12 | aspirational (3) | 3 | PASS | TABLE 2 (hit ordering), TABLE 3 (backpressure), TABLE 4 (burst paths), TABLE 5 (cascade), TABLE 6 (risk register). Five analysis criteria in table form. |
| C-13 | aspirational (3) | 3 | PASS | Bottleneck statement in TABLE 1 seeds naive assumption. TABLE 5 requires cascade resolution statement with GATE 3 blocking until present. Both ends structurally enforced. |
| C-14 | aspirational (3) | 3 | PASS | GATE 1 names prerequisites and states "This gate blocks TABLE 2." GATE 3 requires cascade resolution statement before proceeding. Named, numbered, conditional, blocking. |
| C-15 | aspirational (3) | 3 | PASS | Round 2 opens: "Do not assume Round 1 was accurate because constructs appeared to validate without correction. Round 1's confidence is not evidence of Round 1's precision. Treat Round 1's accepted construct names as unverified at the start of this review." Imperative, directed at evaluating agent, specific to prior layer. |
| C-16 | aspirational (3) | 3 | PASS | Round 2 ends: "Round 2 is specifically looking for constructs introduced in the TABLES 3-5 analysis that were not reviewed in Round 1, which only covered TABLE 1 constructs. Those post-tier constructs were introduced after Round 1's execution window and require independent review here." Named scope extension with structural reason. |

**V-02 Total: 118 / 118**

**C-15 minimum mechanism confirmed:** One sentence prepended to an existing second-barrier header is sufficient. Imperative + named prior layer + confidence-not-evidence statement = complete mechanism. No structural redesign required.

---

### V-03 — Single-axis: Barrier Scope Inheritance Boundary

Base: V-04 R2 (role sequence, GATE 1, C-14 and C-15 pass). Added: explicit scope declaration in ROLE 2.1 naming three construct populations with structural justification for why ROLE 1's scope window excluded them.

| ID | Weight | Pts | Result | Evidence |
|----|--------|-----|--------|----------|
| C-01 | essential (12) | 12 | PASS | ROLE 1.2 bottleneck with [INERTIA-SEED] template. |
| C-02 | essential (12) | 12 | PASS | ROLE 1.2 hit ordering table with "Why this order holds at scenario volume" column. |
| C-03 | essential (12) | 12 | PASS | ROLE 1.3 hop-by-hop backpressure (prose with required format). |
| C-04 | essential (12) | 12 | PASS | ROLE 2.2 UX table with "must differ from Tier 1" enforcement. |
| C-05 | essential (12) | 12 | PASS | Domain rule + ROLE 1 (?) flagging + ROLE 2.1 full construct validation table. |
| C-06 | recommended (10) | 10 | PASS | ROLE 1.4 burst path table with bypass-reason column. |
| C-07 | recommended (10) | 10 | PASS | ROLE 2.3 retry-after gap table. |
| C-08 | recommended (10) | 10 | PASS | ROLE 1.5 cascade table; [INERTIA-SEED] citation required by explicit rule. |
| C-09 | aspirational (5) | 5 | PASS | ROLE 2.4 quantified risk register with Status from numeric comparison. |
| C-10 | aspirational (5) | 5 | PASS | ROLE 2.5 PA remediations + autonomy note for platform-specific controls. |
| C-11 | aspirational (3) | 3 | PASS | ROLE 1 (?) flagging = first barrier; ROLE 2.1 validation table = second barrier with different scope covering propagation, burst, cascade constructs not in ROLE 1's definition window. Per-construct at both. |
| C-12 | aspirational (3) | 3 | PASS | ROLE 1.2 hit ordering table, ROLE 1.4 burst path table, ROLE 1.5 cascade table; ROLE 2.2 UX table, ROLE 2.4 risk register table. Five analysis tables. |
| C-13 | aspirational (3) | 3 | PASS | ROLE 1.2 [INERTIA-SEED] seed. ROLE 1.5 requires "[INERTIA-SEED] assumption breaks:" opener; non-compliant cascade explicitly flagged incomplete. |
| C-14 | aspirational (3) | 3 | PASS | GATE 1 in ROLE 1.1: "ROLE 1.2 is blocked until this condition is met." Named, conditional, states blocked section. |
| C-15 | aspirational (3) | 3 | PASS | ROLE 2.1: "do not assume ROLE 1 was accurate because it was confident. The second barrier is independent of ROLE 1's confidence." Imperative, specific to prior layer. |
| C-16 | aspirational (3) | 3 | PASS | ROLE 2.1 scope declaration names three populations: (a) tier-map constructs, (b) propagation signal types from 1.3, (c) cascade mechanism labels from 1.5 -- each with explicit structural reason "after ROLE 1's construct-definition window had already closed." |

**V-03 Total: 118 / 118**

**C-16 minimum mechanism confirmed:** A scope declaration naming construct populations + structural reason ("outside ROLE 1's scope window by construction") satisfies C-16 when independence assertion is already in place. Scope naming alone closes the criterion.

---

### V-04 — Combination: C-15 + C-16 Co-location

Fresh two-role design. Both criteria stated as labeled subsections ("Independence (C-15):" and "Scope extension (C-16):") in a single ROLE 2 second-barrier preamble block.

| ID | Weight | Pts | Result | Evidence |
|----|--------|-----|--------|----------|
| C-01 | essential (12) | 12 | PASS | ROLE 1.2 bottleneck with [INERTIA-SEED] template. |
| C-02 | essential (12) | 12 | PASS | ROLE 1.2 hit ordering table. |
| C-03 | essential (12) | 12 | PASS | ROLE 1.3 backpressure propagation table (pre-printed with hop/signal-type/response columns). |
| C-04 | essential (12) | 12 | PASS | ROLE 2.2 UX table with "must differ from Tier 1" enforcement. |
| C-05 | essential (12) | 12 | PASS | Domain rule + ROLE 2.1 per-construct validation; no (?) convention needed. |
| C-06 | recommended (10) | 10 | PASS | ROLE 1.4 burst path table. |
| C-07 | recommended (10) | 10 | PASS | ROLE 2.3 retry-after table. |
| C-08 | recommended (10) | 10 | PASS | ROLE 1.5 cascade table with [INERTIA-SEED] citation required. |
| C-09 | aspirational (5) | 5 | PASS | ROLE 2.4 risk register with numeric Status. |
| C-10 | aspirational (5) | 5 | PASS | ROLE 2.5 PA remediations + platform controls note. |
| C-11 | aspirational (3) | 3 | PASS | GATE 1 in 1.1 (first barrier: construct presence); ROLE 2.1 validation table (second barrier: precision). Different scopes declared in preamble. |
| C-12 | aspirational (3) | 3 | PASS | ROLE 1.2 hit ordering table, ROLE 1.3 backpressure table, ROLE 1.4 burst path table, ROLE 1.5 cascade table, ROLE 2.4 risk register table. Five tables covering all eligible analysis criteria. |
| C-13 | aspirational (3) | 3 | PASS | ROLE 1.2 [INERTIA-SEED] seed. ROLE 1.5 requires [INERTIA-SEED] citation; non-compliant cascade flagged incomplete. |
| C-14 | aspirational (3) | 3 | PASS | GATE 1 in ROLE 1.1: "Proceed to ROLE 1.2 only when this condition is met. ROLE 1.2 is blocked until GATE 1 is satisfied." Named, conditional, names blocked section. |
| C-15 | aspirational (3) | 3 | PASS | ROLE 2 preamble, Independence block: "Do not assume ROLE 1 was accurate because it named constructs without flagging uncertainty. ROLE 1's confidence is not evidence of ROLE 1's precision." Imperative, specific to prior layer. |
| C-16 | aspirational (3) | 3 | PASS | ROLE 2 preamble, Scope extension block: names three populations -- (a) tier-map (1.1-1.2), (b) propagation signal types (1.3), (c) cascade mechanism labels (1.5) -- each with structural reason ("These phases closed before ROLE 1 performed propagation/burst/cascade analysis"). |

**V-04 Total: 118 / 118**

**C-15 + C-16 co-location confirmed:** Stating both in a single labeled two-block preamble scores as two independent criteria. Labels are structurally load-bearing -- they force the evaluator to parse each as a distinct requirement. No collapse observed.

---

### V-05 — Full Synthesis: All Six Structural Criteria Explicitly Embedded

Base: V-05 R2 (PHASE structure with five tables and [INERTIA-SEED] thread). Added: "Block: PHASE X is blocked" language at each gate (C-14 tightening), non-deference imperative in PHASE 4.A (C-15), scope inheritance declaration in PHASE 4.A (C-16).

| ID | Weight | Pts | Result | Evidence |
|----|--------|-----|--------|----------|
| C-01 | essential (12) | 12 | PASS | PHASE 2.A bottleneck statement template with [INERTIA-SEED] required. |
| C-02 | essential (12) | 12 | PASS | TABLE 1 hit ordering with "Why this order holds at scenario volume" column. |
| C-03 | essential (12) | 12 | PASS | TABLE 2 backpressure hop chain. |
| C-04 | essential (12) | 12 | PASS | PHASE 2.C UX table with distinct-categories rule; PHASE 4.B UX validation from PA runtime perspective. |
| C-05 | essential (12) | 12 | PASS | Domain rule + GATE 1 (presence) + PHASE 4.A (precision). Two-barrier domain accuracy. |
| C-06 | recommended (10) | 10 | PASS | TABLE 3 burst path enumeration with "Guards in place" fallback. |
| C-07 | recommended (10) | 10 | PASS | PHASE 3.B retry-after table. |
| C-08 | recommended (10) | 10 | PASS | TABLE 4 cascade sequence; PHASE 3.C requires [INERTIA-SEED] opener; GATE 3 blocks PHASE 4 until resolved. |
| C-09 | aspirational (5) | 5 | PASS | TABLE 5 risk register with Status from numeric comparison. |
| C-10 | aspirational (5) | 5 | PASS | PHASE 4.D remediations + inertia verdict sentence. |
| C-11 | aspirational (3) | 3 | PASS | GATE 1 first barrier (construct presence, PHASE 1); PHASE 4.A second barrier (construct precision, different scope). Per-construct required at both. Batch confirmation explicitly prohibited. |
| C-12 | aspirational (3) | 3 | PASS | TABLE 1 (hit ordering), TABLE 2 (backpressure), TABLE 3 (burst paths), TABLE 4 (cascade), TABLE 5 (risk register). Five tables, each with columns enforcing hardest pass condition. |
| C-13 | aspirational (3) | 3 | PASS | PHASE 2.A plants [INERTIA-SEED]. PHASE 3.C requires "[INERTIA-SEED] assumption breaks here:" opener; GATE 3 blocks until cited and broken assumption restated. |
| C-14 | aspirational (3) | 3 | PASS | Three gates with explicit "Block: PHASE X is blocked" sentences. Structural requirements block at top disqualifies section-heading-only. GATE 1: "Block: PHASE 2 is blocked." GATE 2: "Block: PHASE 3 is blocked." GATE 3: "Block: PHASE 4 is blocked." |
| C-15 | aspirational (3) | 3 | PASS | PHASE 4.A: "Do not assume GATE 1 was accurate because all constructs passed the presence check. GATE 1's completeness is not evidence of precision. Treat all construct names as unverified at the start of this section." Imperative, names prior layer (GATE 1), specific: completeness != precision. |
| C-16 | aspirational (3) | 3 | PASS | PHASE 4.A scope: "GATE 1 covered construct categories present at PHASE 1 execution time... This section covers construct categories introduced in PHASES 2-3: (a) propagation signal types (TABLE 2), (b) cascade mechanism labels (TABLE 4), (c) UX and retry-after constructs (PHASE 2.C, 3.B). GATE 1 could not have reviewed these because they were not present when GATE 1 executed." Three categories + structural reason. |

**V-05 Total: 118 / 118**

**Ceiling confirmation:** V-05 reaches 118 with all six criteria named at top and embedded at point-of-use. The C-15 uncertainty ("does GATE 1's completeness-not-evidence-of-precision satisfy specific-to-prior-layer when GATE 1 is not a named role?") resolves YES -- GATE 1 is a named labeled layer and the sentence references it by name.

---

## Excellence Signals from Top-Scoring Variations

### Signal 1 -- Minimum C-15 mechanism: one imperative sentence (V-02)

The single sentence "Do not assume Round 1 was accurate because constructs appeared to validate without correction" prepended to a second-barrier header is sufficient for C-15. Requirements: (1) imperative verb, (2) named prior layer, (3) identifies why confidence is not evidence. Sentence must appear at the START of the second barrier -- not trailing. No structural redesign required.

### Signal 2 -- Minimum C-16 mechanism: named populations + closure reason (V-03)

A scope declaration naming 3 construct populations (tier-map, propagation signal types, cascade mechanism labels) plus one structural sentence ("introduced after ROLE 1's construct-definition window had already closed") satisfies C-16. The closure reason is load-bearing -- "review all constructs" without the structural reason does not pass.

### Signal 3 -- C-15 and C-16 compose independently when labeled (V-04)

Labeling the two criteria as distinct subsections ("Independence:" and "Scope extension:") within a single preamble block prevents collapse. Labels force independent parsing. An unlabeled run-on paragraph containing both concepts may collapse into one criterion -- the labels are structurally necessary for two-criterion scoring.

### Signal 4 -- Named GATE + "Block: SECTION is blocked" is the complete C-14 formula (V-01 + V-05)

V-01 confirms gate syntax works in prose without tables or roles. V-05 confirms "Block: PHASE X is blocked" is the distinguishing formulation vs. "Proceed only when satisfied" (which is advice, not a go/no-go instruction). The "Block:" sentence is what makes a gate a gate.

---

## Round 3 Finding Summary

**Ceiling reached:** V-02, V-03, V-04, V-05 all score 118/118. Four independent structural paths to the ceiling.

**Minimum-mechanism confirmation:** V-02 and V-03 each add exactly one mechanism to a base that already scores 109. Both reach 118. One sentence suffices for C-15; one scope paragraph suffices for C-16. The ceiling does not require architectural redesign.

**Co-location finding (V-04):** C-15 and C-16 score as two independent criteria when labeled. No collapse when co-stated. Architecturally: a single ROLE 2 preamble block can carry both simultaneously without point penalty.

**V-01 diagnostic value:** Confirms C-14 is mechanism-independent (works in prose, no tables or roles). The 102/118 score isolates C-14 as solved while exposing the prose base's C-12 failure as the binding deficit.

```json
{"top_score": 118, "all_essential_pass": true, "new_patterns": ["Single non-deference sentence is the minimum C-15 mechanism -- one imperative sentence naming the prior layer before second barrier opens is sufficient, no structural redesign required", "Named construct populations with structural closure reason satisfy C-16 alone -- 3 categories plus introduced-after-window justification closes the criterion", "C-15 and C-16 compose as independent criteria when labeled as distinct blocks in one preamble -- co-location does not collapse them, labels are structurally load-bearing", "Named GATE plus explicit Block-section sentence is the complete C-14 formula -- works in prose without tabular structure or role separation, distinguishes conditional instruction from advice"]}
```
