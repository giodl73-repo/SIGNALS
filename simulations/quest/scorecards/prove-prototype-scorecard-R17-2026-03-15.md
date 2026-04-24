# Scorecard: prove-prototype (Round 17)

**Date**: 2026-03-15 | **Rubric**: v16 | **Ceiling**: 329 pts
**Variate file**: `simulations/quest/rubrics/prove-prototype-rubric-v16-variate-R17-2026-03-15.md`

---

## Scoring Model

C-01 through C-42 — all PASS in all variations (built on R16 base, which scored 304/304 under
v15). Focus of R17 scoring is exclusively C-43, C-44, C-45 (25 pts new).

**Partial credit convention**: PARTIAL = approximately 50% of criterion weight, applied when
structural elements are present but a required sub-component is missing.

---

## Per-Criterion Analysis — New Criteria Only

### C-43: Competitor Lifecycle Narration Layer (6 pts)

Pass condition requires three co-present elements:
1. Framing paragraph with rationale explaining WHY each container boundary gates that transition
2. Per-container incoming-state annotations (state + constraint)
3. CALIBRATE narrates both sub-transitions explicitly

| Variation | Framing paragraph present | Framing paragraph has WHY rationale | Per-container annotations | CALIBRATE sub-transitions | Result |
|-----------|--------------------------|-------------------------------------|--------------------------|--------------------------|--------|
| V-01 | YES | YES — explains contamination risk, pre-build independence, isolation | YES (1-2 sentences each + constraint) | YES (labeled, with rationale) | **PASS** (6 pts) |
| V-02 | YES | YES — 4-block elaboration per state, most detailed in set | YES (3-4 sentences each, primary axis) | YES (most elaborate, with rationale for two-step requirement) | **PASS** (6 pts) |
| V-03 | YES | NO — "Identification FORBIDDEN in DESIGN. Commitment...occurs exclusively in CALIBRATE." Names constraint, not reason | YES (1 sentence each + constraint) | YES (labeled sub-transitions) | **PARTIAL** (3 pts) |
| V-04 | YES | NO — "DESIGN: NOT YET IDENTIFIED — identification FORBIDDEN..." Compact listing, no WHY in framing paragraph; DESIGN annotation has partial rationale but rationale belongs in framing paragraph | YES (Thread 1 framing; annotations have some rationale) | YES (Thread 1 sub-transition labels in Phase 4 template) | **PARTIAL** (3 pts) |
| V-05 | YES | YES — "If the incumbent were named during DESIGN, success thresholds and exclusions could be written to favor the known baseline...BUILD produces the observation; CLOSE performs the interpretation." | YES (2 sentences each + Thread 2 role status) | YES (Thread 1 framing with two sub-transition steps fully elaborated) | **PASS** (6 pts) |

**C-43 critical gap**: The rubric pass condition states "explains the four-state lifecycle
progression with rationale for why each state transition is gated at a specific container
boundary." V-03 and V-04 provide the framing paragraph, per-container annotations, and
CALIBRATE sub-transitions, but neither framing paragraph supplies the rationale for container
boundary placement — only the constraint ("FORBIDDEN in DESIGN," "committed in CALIBRATE").
The hard fail conditions (framing paragraph absent / container annotation absent / CALIBRATE
sub-transitions absent) are not triggered, so neither is a FAIL, but the missing rationale
element constitutes a PARTIAL.

---

### C-44: Bidirectional COMPARATOR/AUDITOR Handoff (7 pts)

Pass condition requires three elements: (1) Phase 8 COMPLETE handoff declaration, (2) Phase 9
REQUIRED prerequisite gate confirming Phase 8 marker, (3) CLOSE COMPLETE sub-role contract
discharge.

| Variation | Phase 8 handoff declaration | Phase 9 prerequisite gate | CLOSE COMPLETE sub-role discharge | Result |
|-----------|----------------------------|--------------------------|----------------------------------|--------|
| V-01 | PRESENT: "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR" | PRESENT: "REQUIRED: Confirm Phase 8 COMPARATOR handoff marker is present before executing" | PRESENT: "COMPARATOR/AUDITOR sub-role contract: DISCHARGED" | **PASS** (7 pts) |
| V-02 | PRESENT (structural minimum) | PRESENT: "REQUIRED: Confirm Phase 8 COMPARATOR handoff marker is present before executing" | PRESENT: "COMPARATOR/AUDITOR sub-role contract: DISCHARGED" | **PASS** (7 pts) |
| V-03 | PRESENT: Phase 8 renamed "COMPARATOR EXIT GATE"; declaration as Event 1 of two-event protocol | PRESENT: Phase 9 renamed "AUDITOR ENTRY GATE: PREREQUISITE VERIFICATION REQUIRED"; explicit statement "Phase 8 COMPARATOR handoff marker confirmed present — AUDITOR entry authorized" required before output | PRESENT: "COMPARATOR/AUDITOR sub-role contract: DISCHARGED" | **PASS** (7 pts) |
| V-04 | PRESENT: "COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR. [Thread 2 Event 1: COMPARATOR EXIT declared.]" | PRESENT: "REQUIRED: Confirm Phase 8 COMPARATOR handoff marker present — Thread 2 Event 2: AUDITOR ENTRY VERIFICATION"; Phase 9 COMPLETE carries "[Thread 2 Event 2: AUDITOR ENTRY verified — Phase 8 handoff marker confirmed present.]" | PRESENT: "COMPARATOR/AUDITOR sub-role contract: DISCHARGED" | **PASS** (7 pts) |
| V-05 | PRESENT: Phase 8 renamed "COMPARATOR EXIT EVENT"; "[Thread 2 Event 1: COMPARATOR EXIT declared.]" | PRESENT: Phase 9 renamed "AUDITOR ENTRY EVENT: PREREQUISITE VERIFICATION REQUIRED"; requires explicit "Phase 8 COMPARATOR handoff marker confirmed present — Thread 2 Event 2: AUDITOR ENTRY authorized" before output | PRESENT: "COMPARATOR/AUDITOR sub-role contract: DISCHARGED" | **PASS** (7 pts) |

All five variations PASS C-44. V-03 and V-05 are primary-axis implementations with extended
ceremony; V-02 is structural minimum but all three required events are present.

---

### C-45: Dual-Thread Convergence Architecture (12 pts)

Pass condition requires: (1) manifest preamble names Thread 1 and Thread 2 with labels and
scope statements, (2) thread labels propagate through every non-terminal CONTAINER COMPLETE
line, (3) CLOSE COMPLETE carries three simultaneous REQUIRED confirmations (Thread 1 verbatim
chain + Thread 2 handoff confirmed + ledger discharge).

| Variation | Thread preamble naming | Propagation through COMPLETE lines | CLOSE COMPLETE multi-criterion discharge | Result |
|-----------|----------------------|----------------------------------|----------------------------------------|--------|
| V-01 | PRESENT: "Thread 1 — Competitor lifecycle... Thread 2 — COMPARATOR/AUDITOR sequencing..." with scope statements | PRESENT: DESIGN/CALIBRATE/BUILD COMPLETE all carry "Thread 1 (competitor lifecycle) — status: [X]" and "Thread 2... status: [X]" | PRESENT: REQUIRED Thread 1 verbatim chain, REQUIRED Thread 2 handoff confirmed, REQUIRED Value ledger | **PASS** (12 pts) |
| V-02 | PRESENT (condensed): "Thread 1 (competitor lifecycle, C-40)... Thread 2 (COMPARATOR/AUDITOR sequencing, C-41)..." | PRESENT: all COMPLETE lines carry Thread 1 status at exit + Thread 2 status | PRESENT: REQUIRED Thread 1 verbatim + REQUIRED Thread 2 + REQUIRED ledger | **PASS** (12 pts) |
| V-03 | PRESENT: "Thread 1 — Competitor lifecycle (C-40)... Thread 2 — COMPARATOR/AUDITOR sequencing (C-41)..." | PRESENT: DESIGN/CALIBRATE/BUILD COMPLETE carry Thread 1 + Thread 2 labels inline | PRESENT: "REQUIRED — Thread 1... REQUIRED — Thread 2... REQUIRED — Value ledger" | **PASS** (12 pts) |
| V-04 | PRESENT: Thread Architecture Declaration table (Thread 1 / Thread 2 / Ledger rows with governing criterion, what tracked, propagation path) — formal table format | PRESENT: "——" block format; all non-terminal COMPLETE lines carry Thread 1 + Thread 2 in delimited blocks | PRESENT: Numbered (1)(2)(3) format — "(1) REQUIRED — Thread 1... (2) REQUIRED — Thread 2... (3) REQUIRED — Value ledger" | **PASS** (12 pts) |
| V-05 | PRESENT: Thread 1 and Thread 2 given equal-length treatment with parallel preamble sections; "Document thread architecture (C-45)..." declares both with propagation requirements | PRESENT: all non-terminal COMPLETE lines carry "Thread 1... status at [X] exit: [state]" and "Thread 2... status: [X]" | PRESENT: "REQUIRED — Thread 1... full chain verbatim... REQUIRED — Thread 2... two-event protocol completed... REQUIRED — Value ledger" | **PASS** (12 pts) |

All five variations PASS C-45. V-04's table format and numbered terminal confirmation are
format innovations; V-05's co-equal preamble treatment is the structural differentiator.

---

## Composite Scores

| Variation | C-01-C-42 base | C-43 | C-44 | C-45 | **Total** | Delta from ceiling |
|-----------|----------------|------|------|------|-----------|-------------------|
| V-01 | 304 | 6 (PASS) | 7 (PASS) | 12 (PASS) | **329** | 0 |
| V-02 | 304 | 6 (PASS) | 7 (PASS) | 12 (PASS) | **329** | 0 |
| V-03 | 304 | 3 (PARTIAL) | 7 (PASS) | 12 (PASS) | **326** | -3 |
| V-04 | 304 | 3 (PARTIAL) | 7 (PASS) | 12 (PASS) | **326** | -3 |
| V-05 | 304 | 6 (PASS) | 7 (PASS) | 12 (PASS) | **329** | 0 |

**Ranking**: V-01 = V-02 = V-05 (**329**) > V-03 = V-04 (**326**)

All essential criteria (C-01 through C-05, 60 pts) PASS in all variations.

---

## C-43 Gap Analysis — V-03 and V-04

The 3-point gap in V-03 and V-04 traces to a single structural decision: the framing paragraph
states constraint language rather than rationale.

**V-03 framing paragraph**:
> "Four-state progression NOT YET IDENTIFIED -> IDENTIFIED AND COMMITTED -> REFERENCED ->
> DISCHARGED, gated at container boundaries. Identification FORBIDDEN in DESIGN. Commitment
> (via two sub-transitions) occurs exclusively in CALIBRATE. REFERENCED in BUILD. DISCHARGED
> in CLOSE via results table baseline column label and terminal arc record."

**C-43 pass condition** (rationale form):
> V-01 equivalent: "DESIGN is where the hypothesis, scope, and measurement criteria are
> locked — competitor identification is FORBIDDEN here because naming the incumbent before
> the metric is frozen would allow baseline measurement concerns to contaminate scope
> decisions."

"Identification FORBIDDEN in DESIGN" is constraint expression.
"naming the incumbent before the metric is frozen would allow baseline measurement concerns to
contaminate scope decisions" is rationale.

The rubric requires rationale in the framing paragraph; V-03 and V-04 provide constraint only.

V-04's DESIGN annotation does include "the competitor must not exist while design decisions
are being made" — a partial rationale — but it appears in the per-container annotation rather
than in the framing paragraph, where C-43 requires it.

---

## Excellence Signals — Top-Scoring Variations (V-01, V-02, V-05)

**Signal 1 — WHY-not-WHAT is the C-43 differentiator**: The three 329-scoring variations
explicitly name the consequence of violating container ordering (contamination of scope
decisions, failure to lock baseline before build, measurement independence). The two 326-scoring
variations name the same states and constraints without the underlying reason. The rubric tests
for explanation, not enumeration.

**Signal 2 — V-05's co-equal thread elevation is the structural form of C-45 that makes
convergence architecturally inevitable**: V-05's preamble treats Thread 1 and Thread 2 as
parallel structural spines with equal descriptive weight. This creates a document-level
commitment where both threads are prominently declared — omitting either at CLOSE COMPLETE
would be architecturally inconsistent with the opening. V-03 has C-44 as primary with
lifecycle subordinated; V-04 expresses threads as table entries. V-05's co-elevation is the
strongest C-45 structural form.

**Signal 3 — V-02 compression safety**: Phase body compression (one REQUIRED sentence +
completion-line template per phase) does not affect C-43/C-44/C-45 firing. All three new
criteria fire on structural marker presence — framing paragraph, per-container annotations,
sub-transition labels, Phase 9 prerequisite gate, thread labels on COMPLETE lines — and these
are fully present in V-02 despite compressed phase instructions. New criteria are
implementation-instruction-independent.

**Signal 4 — V-04's numbered terminal confirmation exceeds inline labeling for audit
reliability**: V-04's CLOSE COMPLETE uses "(1) REQUIRED... (2) REQUIRED... (3) REQUIRED..."
structure. This separates the three simultaneous discharges visually, making audit-by-
inspection more reliable than inline thread annotations. Not a scoring differentiator at this
ceiling (V-04 scores 326 due to C-43 gap), but the strongest structural form for the
simultaneous-discharge requirement when combined with a passing C-43.

---

## Summary

| Metric | Value |
|--------|-------|
| Top score | 329 / 329 |
| Top variations | V-01, V-02, V-05 |
| All essential pass | YES (all 5 variations) |
| Key gap in V-03, V-04 | C-43 framing paragraph missing rationale for container-boundary gating |
| R17 seed (V-01) | Confirms ceiling reachable; full combination with elaboration scores 329 |
| Best C-45 structural form | V-05 (co-equal parallel spine) > V-04 (formal table + numbered terminal) > V-03 (minimal naming) |

---

```json
{"top_score": 329, "all_essential_pass": true, "new_patterns": ["WHY-not-WHAT in C-43 framing paragraph: C-43 requires the framing paragraph to state rationale for why each container boundary gates that lifecycle transition — naming the contamination risk and isolation purpose — not just constraint language (FORBIDDEN in DESIGN); V-03 and V-04 provide state-to-container enumeration with prohibitions but no rationale, earning PARTIAL", "Co-equal thread elevation as structural enforcement: V-05 gives Thread 1 and Thread 2 equal preamble weight as parallel structural spines, making C-45 multi-criterion terminal discharge architecturally inevitable — both threads are equally declared, so omitting either at CLOSE COMPLETE would be inconsistent with the document opening commitment", "Phase body compression is C-43/C-44/C-45 safe: V-02 demonstrates that compressing phase instructions to minimum expression does not degrade new-criteria scoring; framing paragraph, per-container annotations, Phase 9 prerequisite gate, and thread labels on COMPLETE lines all fire on structural marker presence independent of instruction verbosity"]}
```
