**Round 1 scoring complete.**

---

## Results Summary

| Rank | Variation | Score | Band | Differentiator |
|------|-----------|-------|------|---------------|
| 1 (tied) | V-03 — Phase Gates | **100** | Gold | C-09 PASS |
| 1 (tied) | V-04 — Critic-First | **100** | Gold | C-09 PASS |
| 1 (tied) | V-05 — Inertia Framing | **100** | Gold | C-09 PASS |
| 4 (tied) | V-01 — Table-First | **90** | Silver | C-09 FAIL |
| 4 (tied) | V-02 — Conversational | **90** | Silver | C-09 FAIL |

**All 5 essential criteria pass in every variation.** The sole differentiator in Round 1 is C-09 — whether the variation explicitly prompts the model to classify the Echo as a *systemic category* of retrospective blind spot, not just explain why it was unpredicted.

V-01 and V-02 ask *why* the signal system missed the Echo. V-03, V-04, V-05 ask *what class of thing* the Echo represents — one sentence that turns a one-off observation into a compounding retrospective asset.

**Three new patterns identified:**
1. `systemic-pattern-echo-field` — named field in Echo section requiring category classification
2. `three-way-wrong-gap-echo-isolation` — explicit "not a wrong prediction, not a gap" structural distinction (V-05)
3. `inertia-framing-for-gaps` — prior-state anchor sharpens Gaps from "missing data" to "what would have overcome the team's assumption" (V-05)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["systemic-pattern-echo-field", "three-way-wrong-gap-echo-isolation", "inertia-framing-for-gaps"]}
```
-----|
| C-06 | Namespace coverage summary (all 9) | **PASS** | "If a namespace has no signal row, explicitly add: `(none gathered)` as a row" — forces all 9 represented |
| C-07 | Improvement tied to specific gap or Echo | **PASS** | Step 5: "Tie it to a specific Gap row (by namespace) or to the Echo" — explicit linkage required |
| C-08 | Numeric accuracy ratio stated | **PASS** | "State the accuracy ratio at the bottom: X of Y signals correct (Z%)" |

All recommended: 3/3

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Echo linked to systemic pattern | **FAIL** | Step 4 asks "why no signal would have caught this" but does not prompt for systemic pattern or recurring class |
| C-10 | AMEND scope handled correctly | **N/A** | AMEND instructions present; no AMEND in this invocation |

### V-01 Score

```
composite = (5/5 × 60) + (3/3 × 30) + (0/1 × 10) = 60 + 30 + 0 = 90
```

**V-01: 90 / 100** — Silver band (all essential pass, composite >= 65)

---

## V-02 — Axis: Phrasing Register (Conversational/Interrogative)

**Hypothesis:** Question-driven prompts produce more honest self-assessment. Imperative prompts
encourage performing completeness; questions expose what the model actually knows vs. constructing.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal Accuracy section with predicted vs actual | **PASS** | "What did it predict? Was it right?" — prediction and outcome required per signal |
| C-02 | Explicit verdict per signal | **PASS** | "Label each signal: Correct, Wrong, or Partial" — explicit instruction |
| C-03 | Gaps section with decision-impact reasoning | **PASS** | "would it have changed the decision or just the confidence level?" — decision impact required; "More research doesn't count" |
| C-04 | Echo — one genuinely unexpected finding | **PASS** | "Not a wrong prediction — wrong predictions are things you got wrong." One Echo only. |
| C-05 | Topic and commitment anchor established | **PASS** | "What was the commitment?" — topic and decision required |

All essential: 5/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Namespace coverage summary (all 9) | **PASS** | "Cover all nine signal types: scout, draft, review, flow, trace, prove, listen, program, topic. If you didn't gather a signal in a namespace, say so — that's information too." |
| C-07 | Improvement tied to specific gap or Echo | **PASS** | "Connect it either to a specific gap (which namespace was missing?) or to the Echo. Make it actionable — a future team should be able to read this and know what to add." |
| C-08 | Numeric accuracy ratio stated | **PASS** | "give yourself a score: how many signals called it correctly out of how many you gathered?" |

All recommended: 3/3

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Echo linked to systemic pattern | **FAIL** | Asks "why the signal system didn't have a way to catch it in advance" — explains the gap but does not prompt for recurring pattern or systemic class |
| C-10 | AMEND scope handled correctly | **N/A** | AMEND instructions present; no AMEND in this invocation |

### V-02 Score

```
composite = (5/5 × 60) + (3/3 × 30) + (0/1 × 10) = 60 + 30 + 0 = 90
```

**V-02: 90 / 100** — Silver band

---

## V-03 — Axis: Lifecycle Emphasis (Explicit Phase Gates with Isolation Enforcement)

**Hypothesis:** Hard "do not proceed" gates between phases prevent the model from importing
downstream reasoning backward — specifically, preventing Echo contamination of the Signal Accuracy
phase and preventing Gaps from being rationalized as Echo.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal Accuracy section with predicted vs actual | **PASS** | Phase 2: "What the signal predicted (as understood at commitment time), What actually happened (post-ship)" — both required per signal |
| C-02 | Explicit verdict per signal | **PASS** | "Verdict: Correct \| Wrong \| Partial" — only these three values |
| C-03 | Gaps section with decision-impact reasoning | **PASS** | Phase 3: "Decision impact: Would have blocked \| Would have changed scope \| Would have accelerated \| Would have confirmed" — phase gate blocks proceeding until each gap has concrete decision impact |
| C-04 | Echo — one genuinely unexpected finding | **PASS** | Phase 4 gate: "if you could describe it as a wrong prediction, it belongs in Phase 2, not here" — strictest structural enforcement of the wrong-prediction/Echo boundary |
| C-05 | Topic and commitment anchor established | **PASS** | Phase 1: topic, commitment (one sentence), date made, date shipped — four required fields |

All essential: 5/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Namespace coverage summary (all 9) | **PASS** | "Include all nine namespaces. If a namespace has no signal: `[namespace]: no signal gathered`" |
| C-07 | Improvement tied to specific gap or Echo | **PASS** | Phase 4: "Must be tied to either: a specific Gap from Phase 3 (cite the namespace), or the Echo from this phase (cite what signal type would have approached it)" |
| C-08 | Numeric accuracy ratio stated | **PASS** | "After the list: state the accuracy ratio. Example: 7 of 9 signals correct (78%)" |

All recommended: 3/3

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Echo linked to systemic pattern | **PASS** | Phase 4 Echo explicitly requires: "Systemic pattern (if identifiable): [is this a class of thing that retrospectives routinely miss?]" — named field, not optional prose |
| C-10 | AMEND scope handled correctly | **N/A** | AMEND section present; no AMEND in this invocation |

### V-03 Score

```
composite = (5/5 × 60) + (3/3 × 30) + (1/1 × 10) = 60 + 30 + 10 = 100
```

**V-03: 100 / 100** — Gold band

---

## V-04 — Combination: Output Format (Hybrid Table+Prose) + Role Sequence (Critic-First)

**Hypothesis:** Running a skeptic role before the narrator role forces the retrospective to surface
weaknesses before they can be rationalized. The hybrid format gives the critic's findings structured
capture while allowing the narrator to provide context prose only where tables cannot carry meaning.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal Accuracy section with predicted vs actual | **PASS** | B2 Full Signal Accuracy table extends A1 to all signals; Predicted and Actual columns required |
| C-02 | Explicit verdict per signal | **PASS** | Table verdict: "✓ / ✗ / ~"; accuracy ratio computed in B2 |
| C-03 | Gaps section with decision-impact reasoning | **PASS** | A2 gaps table has "Impact If Gathered" column; B3 adds decision context sentence per row |
| C-04 | Echo — one genuinely unexpected finding | **PASS** | B4 reclassification check: "If the Critic's Echo candidate is actually a wrong prediction (covered in B2): reclassify it there and state 'No Echo detected' with justification" — structural reclassification guard |
| C-05 | Topic and commitment anchor established | **PASS** | B1 Commitment Anchor: "topic, the commitment, and the ship date. One sentence each." |

All essential: 5/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Namespace coverage summary (all 9) | **PASS** | B2: "If any namespace has no signal: mark it explicitly" — absence acknowledgement required |
| C-07 | Improvement tied to specific gap or Echo | **PASS** | B5: "Tied to the most impactful gap (cite namespace) or to the Echo. State it as a concrete addition to future signal-gathering plans." |
| C-08 | Numeric accuracy ratio stated | **PASS** | B2: "Accuracy ratio: X of Y correct (Z%)" |

All recommended: 3/3

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Echo linked to systemic pattern | **PASS** | B4: "Whether it represents a systemic class of thing that signal systems routinely miss" — explicitly required |
| C-10 | AMEND scope handled correctly | **N/A** | AMEND section present; no AMEND in this invocation |

### V-04 Score

```
composite = (5/5 × 60) + (3/3 × 30) + (1/1 × 10) = 60 + 30 + 10 = 100
```

**V-04: 100 / 100** — Gold band

---

## V-05 — Combination: Phrasing Register (Formal/Imperative) + Inertia Framing (Prominent)

**Hypothesis:** Foregrounding "what the team was already doing before signals" vs. "what signals
changed" creates a sharper counterfactual frame. Gaps become specifically "signals that would have
overcome the team's prior assumption" rather than generic missing data.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal Accuracy section with predicted vs actual | **PASS** | Section 2: "Prediction: [what the signal said would be true]" and "Actual: [what happened]" required per signal |
| C-02 | Explicit verdict per signal | **PASS** | "Verdict: Correct \| Wrong \| Partial" per signal; plus inertia relationship field |
| C-03 | Gaps section with decision-impact reasoning | **PASS** | Section 3: "Decision impact: Blocked \| Changed scope \| Accelerated confirmation \| Unchanged (explain why listed)" — strongest filter: gaps with Unchanged impact excluded unless systemic |
| C-04 | Echo — one genuinely unexpected finding | **PASS** | Section 4: "It is not a wrong prediction (those belong in Section 2). It is not a gap (those belong in Section 3)." — explicit three-way structural isolation, strongest of all five |
| C-05 | Topic and commitment anchor established | **PASS** | Section 1: Topic, Commitment, Prior state (inertia) — all three required |

All essential: 5/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Namespace coverage summary (all 9) | **PASS** | "Cover all nine namespaces: scout, draft, review, flow, trace, prove, listen, program, topic. For any namespace with no signal: state `[namespace]: not sampled`" — lists all 9 by name |
| C-07 | Improvement tied to specific gap or Echo | **PASS** | Section 5: "Must be tied to either: (a) The highest-impact Gap in Section 3 — specify namespace and inertia target, or (b) The Echo" |
| C-08 | Numeric accuracy ratio stated | **PASS** | "Compute and state the accuracy ratio: X / Y signals correct (Z%)." Plus inertia breakdown computed separately. |

All recommended: 3/3

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Echo linked to systemic pattern | **PASS** | Section 4: "Systemic class: [is this a category of thing that retrospectives routinely fail to catch? If yes, name the category.]" — most explicit systemic prompt of all five variations |
| C-10 | AMEND scope handled correctly | **N/A** | AMEND Handling section present; no AMEND in this invocation |

### V-05 Score

```
composite = (5/5 × 60) + (3/3 × 30) + (1/1 × 10) = 60 + 30 + 10 = 100
```

**V-05: 100 / 100** — Gold band

---

## Rankings

| Rank | Variation | Score | Band | Essential | C-09 |
|------|-----------|-------|------|-----------|------|
| 1 (tied) | V-03 — Phase Gates | **100** | Gold | 5/5 | PASS |
| 1 (tied) | V-04 — Critic-First + Hybrid | **100** | Gold | 5/5 | PASS |
| 1 (tied) | V-05 — Inertia Framing | **100** | Gold | 5/5 | PASS |
| 4 (tied) | V-01 — Table-First | **90** | Silver | 5/5 | FAIL |
| 4 (tied) | V-02 — Conversational | **90** | Silver | 5/5 | FAIL |

**The sole differentiator in Round 1**: C-09 (Echo linked to systemic pattern). Every variation
passes all essential and recommended criteria. The gap is entirely in whether the variation prompts
the model to connect the Echo to a broader category of retrospective blind spots.

---

## Excellence Signals

Three patterns distinguish the top-scoring variations:

**1. Systemic pattern prompt in Echo (C-09 driver)**
V-03, V-04, V-05 all add an explicit named field requiring the model to classify the Echo as a
category of recurring blind spot — not just explain why it was unpredicted. V-05 is the strongest:
"Systemic class: [is this a category of thing that retrospectives routinely fail to catch? If yes,
name the category.]" V-01 and V-02 ask *why* the signal system missed the Echo but do not ask *what
class of thing* the Echo represents. The upgrade is one sentence and changes Echo from an isolated
observation into a compounding retrospective asset.

**2. Three-way wrong/gap/Echo isolation (V-05)**
V-05 explicitly names all three: "It is not a wrong prediction (those belong in Section 2). It is not
a gap (those belong in Section 3)." This is structurally cleaner than V-01/V-02 (which define Echo
against wrong predictions only) and V-03/V-04 (which use phase gates or reclassification checks).
The three-way distinction reduces ambiguity at the model level and at the reviewer level.

**3. Inertia framing for Gaps (V-05)**
Adding "Prior state (inertia)" to the anchor changes the frame for the entire retrospective. Gaps
become "signals that would have overcome inertia" rather than "signals we wish we had gathered."
This makes the counterfactual more honest: not "could we have gathered this?" but "would this signal
have changed what the team was already assuming?" The inertia breakdown in Section 2 (how many
signals confirmed vs. challenged the prior assumption) is a second-order accuracy metric that no
other variation produces.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["systemic-pattern-echo-field", "three-way-wrong-gap-echo-isolation", "inertia-framing-for-gaps"]}
```
