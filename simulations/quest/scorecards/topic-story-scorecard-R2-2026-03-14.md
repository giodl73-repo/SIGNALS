## Round 2 Scorecard — topic-story

| Rank | Variation | C-05 | C-10 | C-11 | C-12 | Score |
|------|-----------|------|------|------|------|-------|
| 1 | V-04 Inertia + Falsifiability | PASS | PASS | PARTIAL | PASS | **99** |
| 2 | V-03 Per-Section Anchors | PASS | PARTIAL | PASS | PARTIAL | **98** |
| 2 | V-05 Investigator + Checkpoints | PASS | PARTIAL | PASS | PARTIAL | **98** |
| 4 | V-01 Inertia Framing | PARTIAL | PASS | PARTIAL | PASS | **94** |
| 5 | V-02 Contrast Examples | PARTIAL | PARTIAL | PARTIAL | PASS | **93** |

All five golden. Top score 99 — one point below R1's perfect 100.

---

**The ceiling is 99 because C-10/C-11/C-12 partition cleanly across variations:**

Variations targeting **C-10 + C-12** (V-01, V-04): inertia framing + falsifiability test hit both because they're the same question at different scales ("what makes this claim defensible?"). But neither variation has per-section voice anchors, so C-11 slips to PARTIAL.

Variations targeting **C-11** (V-03, V-05): per-section stances prevent trailing-tone collapse structurally and recover full recommended score. But neither has inertia framing or a falsifiability test, so C-10 and C-12 are PARTIAL.

No single variation covers all three.

---

**Three new patterns:**

1. **C-10 and C-12 are the same epistemic habit** — "does this sentence change the verdict?" (decision salience) and "what would disprove this claim?" (causal precision) both force the author to ask what makes an assertion defensible. Inertia framing trains this habit document-wide, producing both criteria simultaneously.

2. **C-11 is structurally orthogonal** — per-section voice anchors are the only reliable C-11 mechanism, and they don't produce decision-orientation. Inertia framing doesn't prevent section-level register drift. The two mechanisms must coexist — combining V-04's frame with V-05's stances is the Round 3 hypothesis.

3. **Inline falsifiability self-check is sufficient for C-12** — V-01's rhetorical question ("what would they have to show is false?") and V-04's negative example both pass without contrast examples. V-02's contrast block is stronger but not the minimum viable instruction.

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["C-10 (decision-orientation) and C-12 (causal falsifiability) are the same question at different scales — 'what makes this claim defensible?' — so inertia framing and falsifiability instruction are synergistic; V-04 achieves both simultaneously because both mechanisms train the same epistemic habit in the author", "C-11 (register sustained across sections) is structurally orthogonal to C-10/C-12 — no variation achieves all three; per-section voice anchors prevent trailing-tone collapse but do not produce decision-orientation, and inertia framing produces decision-orientation but does not prevent section-level register drift; combining them is the Round 3 hypothesis", "Inline falsifiability self-check ('what specific evidence would disprove this?') is sufficient for C-12 without contrast examples — V-01's rhetorical form and V-04's negative example both pass; V-02's contrast block is the strongest instruction but not the minimum viable mechanism"]}
```
sion, what would they have to show is false?" — direct falsifiability test in synthesis instruction. Also: "Identify the specific assumption, constraint, or dynamic that accounts for the convergence." Together these satisfy C-12 pass condition via rhetorical question form. |

**Essential**: 4/4 = 60 | **Recommended**: C-05 PARTIAL (5) + C-06 PASS (10) + C-07 PASS (10) = 25 | **Aspirational**: C-08(2) + C-09(2) + C-10(2) + C-11(1) + C-12(2) = 9

```
composite = 60 + 25 + 9 = 94
```

**Score: 94 / 100 — GOLDEN**

---

### V-02: Causal Falsifiability Instruction (Contrast Examples)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four-Section Structure | PASS | All four sections present and labeled. |
| C-02 | Cross-Signal Synthesis | PASS | "Draw the cross-signal conclusion — the insight that requires all signals together to see." |
| C-03 | Pattern Explicitly Named | PASS | Pre-printed `**Pattern**: [one extractable sentence with falsifiable causal logic]` field. |
| C-04 | Valid Recommendation with Rationale | PASS | Explicit verdict + "connect the verdict to the named pattern. Specify the immediate next action or decision gate." |
| C-05 | Author's Editorial Voice | PARTIAL | Interpretive phrasing examples present in synthesis section only ("What's striking is...," "The convergence points to a specific structural reason...," "Take a position."). No audience pressure, no role framing, no trailing tone instruction. Synthesis section has voice; other sections lack instruction. |
| C-06 | Uncertainty Is Specific | PASS | Canonical form: "We do not know [X] because [Y] — this matters because if X is false, the recommendation changes." |
| C-07 | Signal Findings Selective | PASS | "one sentence, the single most important finding. Selective, not exhaustive." |
| C-08 | Recommendation Action-Forcing | PASS | "'proceed' alone is a verdict, not a recommendation." Negative framing present. |
| C-09 | Pattern Has Causal Logic | PASS | Strongest C-09 mechanism in the round: full contrast block (weak vs. strong causal account), "A pattern statement has two jobs: name the convergence, and explain it." Showing the distinction produces reliable causal accounts. |
| C-10 | Narrative Decision-Oriented | PARTIAL | "Selective, not exhaustive" for signal findings. No inertia framing, no explicit "does this change the decision?" filter. Selectivity instruction exists but is not tied to decision stakes. |
| C-11 | Register Sustained Across Sections | PARTIAL | Voice instruction confined to synthesis section. Uncertainty section has structural format only. Recommendation section has "connect the verdict" but no register maintenance instruction. Trailing-tone collapse risk unmitigated in trailing sections. |
| C-12 | Causal Claim Falsifiable | PASS | Explicit contrast block with weak/strong examples + self-check test: "after writing your pattern statement, ask — what specific evidence would disprove it? If the answer is 'nothing specific,' the claim is not causal." Most explicit C-12 instruction in the round. |

**Essential**: 4/4 = 60 | **Recommended**: C-05 PARTIAL (5) + C-06 PASS (10) + C-07 PASS (10) = 25 | **Aspirational**: C-08(2) + C-09(2) + C-10(1) + C-11(1) + C-12(2) = 8

```
composite = 60 + 25 + 8 = 93
```

**Score: 93 / 100 — GOLDEN**

---

### V-03: Register Checkpoint (Per-Section Voice Anchors)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four-Section Structure | PASS | All four required sections present (Sections 2–5). Introductory framing section (Section 1) is additive, not substitutive. |
| C-02 | Cross-Signal Synthesis | PASS | "Something emerged that no single signal said. Name it." + analyst stance throughout. |
| C-03 | Pattern Explicitly Named | PASS | Pre-printed `**Pattern**: [one extractable sentence naming the emergent finding]` field. |
| C-04 | Valid Recommendation with Rationale | PASS | Explicit verdict + "Connect it to the pattern you named. Specify the immediate next action: what happens now, not what could happen someday." |
| C-05 | Author's Editorial Voice | PASS | Named stances for every section: "investigator framing the question," "informed editor choosing what to surface," "analyst who sees the shape of the evidence," "honest accountant," "decision advocate who will be held accountable." Phrasing examples in synthesis ("What's striking is...," "The evidence forces a conclusion..."). Multi-section voice is structural, not incidental. |
| C-06 | Uncertainty Is Specific | PASS | "'We do not know X, and here is why that matters: if X is false, the verdict changes' is honest accounting." |
| C-07 | Signal Findings Selective | PASS | "Section 2: Most of what you read is not in this section... One sentence per signal; brevity is the stance." Stance framing reinforces selectivity. |
| C-08 | Recommendation Action-Forcing | PASS | "Specify the immediate next action: what happens now, not what could happen someday." |
| C-09 | Pattern Has Causal Logic | PASS | Contrast framing: "not 'three signals point this way' but 'three signals point this way because [specific shared constraint or mechanism]'." Inherited from R1 V-05 excellence signal E-3. |
| C-10 | Narrative Decision-Oriented | PARTIAL | "Informed editor choosing what to surface" stance creates selectivity pressure. Uncertainty section has stakes connection ("if X is false, the verdict changes"). Recommendation section has accountability framing. But no inertia framing and no explicit "does this change the decision?" filter applied per-signal. Decision-orientation is implicit in the stances rather than structural. |
| C-11 | Register Sustained Across Sections | PASS | Named stances for every section prevent trailing-tone collapse structurally. Closing self-check: "does the editorial register persist from Section 1 through Section 5?" + "Revise the trailing sections before writing the artifact." This is the primary C-11 mechanism in the round. |
| C-12 | Causal Claim Falsifiable | PARTIAL | Contrast framing ("not 'three signals point this way' but 'three signals point this way because [specific shared constraint or mechanism]'") satisfies C-09 but does not explicitly ask "what would disprove this?" No falsifiability test, no weak/strong examples. A causal account may be produced without being falsifiable. |

**Essential**: 4/4 = 60 | **Recommended**: C-05 PASS (10) + C-06 PASS (10) + C-07 PASS (10) = 30 | **Aspirational**: C-08(2) + C-09(2) + C-10(1) + C-11(2) + C-12(1) = 8

```
composite = 60 + 30 + 8 = 98
```

**Score: 98 / 100 — GOLDEN**

---

### V-04: Inertia Framing + Causal Falsifiability (Combined)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four-Section Structure | PASS | All four sections present and labeled. |
| C-02 | Cross-Signal Synthesis | PASS | "The argument. Name the emergent cross-signal finding. Take a position." |
| C-03 | Pattern Explicitly Named | PASS | Pre-printed `**Pattern**: [one extractable sentence with falsifiable causal logic]` field. |
| C-04 | Valid Recommendation with Rationale | PASS | Explicit verdict + "Ground the verdict in the named pattern... the verdict follows from the pattern because [reason]." |
| C-05 | Author's Editorial Voice | PASS | Decision-argument opening ("The question is not whether to learn more — the question is whether to build it. Write the story that makes the case — or closes it.") creates argumentative framing. Synthesis: "Take a position." Recommendation: "the verdict follows from the pattern because [reason]" forces reasoning sentence. Closing skeptic test ("would a skeptic who reads only this document know both what the signals say and exactly what evidence would change the verdict?") is implicit audience pressure. Weaker than V-05 but sufficient for PASS. |
| C-06 | Uncertainty Is Specific | PASS | Canonical form: "'We do not know X. If X is false, the recommendation changes to [Y].'" |
| C-07 | Signal Findings Selective | PASS | "Decision-relevant only... If a signal's most important finding is neutral to the build/don't-build question, say so in one sentence. Omit the rest." Most specific selectivity instruction in the round. |
| C-08 | Recommendation Action-Forcing | PASS | "the immediate next action, the thing that must happen before the decision is final" |
| C-09 | Pattern Has Causal Logic | PASS | Falsifiability block naturally requires causal mechanism: "A genuine causal claim names the specific mechanism, assumption, or structural condition that accounts for the convergence." C-09 satisfied as precondition to C-12. |
| C-10 | Narrative Decision-Oriented | PASS | Combined inertia framing ("The question is whether to build it") + per-signal filter ("does this finding change whether {topic} should be built?") + closing skeptic test. Decision-orientation is systematic and applied at document level, section level, and signal level. |
| C-11 | Register Sustained Across Sections | PARTIAL | Uncertainty section: "connect it to the decision" provides some register maintenance but no explicit stance or anti-neutral instruction. Recommendation section: "the verdict follows from the pattern because [reason]" forces a reasoning sentence but does not prevent neutral framing. No self-check, no per-section stances. Trailing-tone collapse risk remains. |
| C-12 | Causal Claim Falsifiable | PASS | Inline falsifiability explanation: "A pattern statement that explains convergence as 'the signals align because the approach is sound' cannot be disproved. It is a confidence statement, not a causal claim. A genuine causal claim names the specific mechanism, assumption, or structural condition... specific enough that a reader can name what evidence would break it." Negative example provided. Closing test reinforces: "exactly what evidence would change the verdict?" Strong PASS. |

**Essential**: 4/4 = 60 | **Recommended**: C-05 PASS (10) + C-06 PASS (10) + C-07 PASS (10) = 30 | **Aspirational**: C-08(2) + C-09(2) + C-10(2) + C-11(1) + C-12(2) = 9

```
composite = 60 + 30 + 9 = 99
```

**Score: 99 / 100 — GOLDEN**

---

### V-05: Investigator Stance + Register Checkpoints

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four-Section Structure | PASS | All four required sections present and labeled. |
| C-02 | Cross-Signal Synthesis | PASS | "Step back from individual signals. What shape does the evidence take? Name the pattern." + analyst stance in synthesis section. |
| C-03 | Pattern Explicitly Named | PASS | Pre-printed `**Pattern**: [one extractable sentence stating the cross-signal finding and its causal basis]` field. Causal basis required in the pattern label itself. |
| C-04 | Valid Recommendation with Rationale | PASS | Explicit verdict + "Connect the verdict to the named pattern — the rationale cites the pattern, not individual signals. Specify what acting on the verdict requires." Concrete example: "Given the evidence, I recommend proceeding to prototype — specifically targeting the auth flow, which the signals flagged as the one untested constraint." |
| C-05 | Author's Editorial Voice | PASS | Strongest C-05 coverage in the round. Four stacked mechanisms: (1) named investigator role ("You are the lead investigator... Now you are writing the story"), (2) audience pressure ("Your team lead will read this once. They will make a decision. Make the document worthy of the decision."), (3) explicit phrasing examples ("What's striking is..." / "The convergence is not coincidental — it reflects..." / "The evidence forces a conclusion I did not enter the investigation expecting..."), (4) closing register check ("does the investigator's voice persist from the opening question through the final recommendation?"). Directly inherits V-04 R1's winning mechanism stack. |
| C-06 | Uncertainty Is Specific | PASS | Canonical form: "'We do not know X; if X turns out to be false, the verdict changes to [Y]'." + explicit anti-hedge: "Do not hedge into vagueness." |
| C-07 | Signal Findings Selective | PASS | "For each signal: one sentence... The finding should carry the investigator's interpretive judgment, not just the signal's output." Frames selectivity as interpretive distillation rather than reduction. |
| C-08 | Recommendation Action-Forcing | PASS | "Specify what acting on the verdict requires: the immediate next action, the person or team responsible, the decision gate." Concrete example in section instruction. |
| C-09 | Pattern Has Causal Logic | PASS | Contrast framing: "not 'three signals agree' but 'three signals agree because [specific structural reason]'." Pattern pre-printed label requires "causal basis." Inherited from R1 V-05 E-3. |
| C-10 | Narrative Decision-Oriented | PARTIAL | Audience pressure ("Your team lead will read this once") creates implicit decision-orientation. "Investigator distilling each signal to its sharpest point" creates selectivity. But no inertia framing and no explicit "does this change the decision?" per-signal filter. Decision-orientation is present as a tone property, not a structural filter. |
| C-11 | Register Sustained Across Sections | PASS | Named stances for every section. Recommendation section has explicit anti-retreat instruction: "Do not retreat to neutral language here." + concrete example of non-neutral recommendation phrasing. Closing register check: "does the investigator's voice persist...? If the uncertainty or recommendation sections feel like neutral reporting, they are not in the investigator's stance. Revise them before writing." Structural prevention of trailing-tone collapse across all four sections. |
| C-12 | Causal Claim Falsifiable | PARTIAL | Pattern pre-printed label requires "causal basis" — stronger than bare causal framing but does not require falsifiability. Phrasing examples ("The convergence is not coincidental — it reflects...") promote causal voice without testing whether the claim can be disproved. No falsifiability self-check, no weak/strong contrast. A causally framed claim may still fail C-12 test. |

**Essential**: 4/4 = 60 | **Recommended**: C-05 PASS (10) + C-06 PASS (10) + C-07 PASS (10) = 30 | **Aspirational**: C-08(2) + C-09(2) + C-10(1) + C-11(2) + C-12(1) = 8

```
composite = 60 + 30 + 8 = 98
```

**Score: 98 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | C-05 | C-10 | C-11 | C-12 | Essential | Recommended | Aspirational | Score |
|------|-----------|------|------|------|------|-----------|-------------|--------------|-------|
| 1 | V-04 Inertia+Falsify | PASS | PASS | PARTIAL | PASS | 4/4 | 3/3 | 9/10 | **99** |
| 2 | V-03 Section Anchors | PASS | PARTIAL | PASS | PARTIAL | 4/4 | 3/3 | 8/10 | **98** |
| 2 | V-05 Investigator+Check | PASS | PARTIAL | PASS | PARTIAL | 4/4 | 3/3 | 8/10 | **98** |
| 4 | V-01 Inertia Framing | PARTIAL | PASS | PARTIAL | PASS | 4/4 | 2.5/3 | 9/10 | **94** |
| 5 | V-02 Contrast Examples | PARTIAL | PARTIAL | PARTIAL | PASS | 4/4 | 2.5/3 | 8/10 | **93** |

**The three-way split is entirely explained by the C-10/C-11/C-12 cluster:**

- Variations that target C-10+C-12 (V-01, V-04) achieve aspiration 9/10 but pay C-11 (no per-section register discipline).
- Variations that target C-11 (V-03, V-05) achieve full recommended score but pay C-10 and C-12 (no inertia framing, no falsifiability test).
- No variation achieves all three. The ceiling is 99, not 100.

---

## Key Tension: C-10/C-12 vs. C-11

| Criterion | Mechanism required | V-01 | V-04 | V-03 | V-05 |
|-----------|-------------------|------|------|------|------|
| C-10 | Per-signal decision filter ("does this change the verdict?") | PASS | PASS | PARTIAL | PARTIAL |
| C-11 | Per-section voice anchors + register self-check | PARTIAL | PARTIAL | PASS | PASS |
| C-12 | Falsifiability test ("what would disprove this?") | PASS | PASS | PARTIAL | PARTIAL |

The pattern is clean: inertia framing hits C-10 and C-12 (the same question at different scales: "what makes this defensible?"). Per-section anchors hit C-11. These two mechanisms are independently necessary. A variation that combines them should approach 100 in Round 3.

---

## Excellence Signals — Round 2

### E-1: C-10 and C-12 are the same question at different scales

V-04 wins because inertia framing ("has the default changed?") and falsifiability instruction ("what would a skeptic have to disprove?") are structurally the same: both force the author to ask what makes the claim defensible. Decision-orientation (C-10) strips sentences that don't change the verdict. Causal falsifiability (C-12) strips causal language that can't be disproved. The same epistemic habit produces both. They reinforce rather than compete — V-04's top score is evidence of this.

### E-2: Inline falsifiability explanation is sufficient; contrast examples are additive, not required

V-02 uses a full contrast block (weak/strong examples + self-check test). V-01 uses only the rhetorical question ("what would they have to show is false?"). V-04 uses an inline negative example. All three pass C-12. The contrast block is the clearest instruction but not the minimum viable instruction. The falsifiability self-check question ("what specific evidence would disprove it?") is sufficient on its own.

### E-3: Per-section voice anchors prevent trailing-tone collapse structurally

V-03 and V-05 are the only variations that structurally prevent the C-11 failure mode. The mechanism is naming the editorial stance before the model writes each section, not after. V-05's "Do not retreat to neutral language here" in the recommendation section with a concrete non-neutral example is the strongest single C-11 intervention in the round.

### E-4: The 100-point variation for Round 3

Combine V-04's inertia+falsifiability framing with V-05's per-section stances and register self-check:
- Opening: inertia framing (C-10, C-12 foundation)
- Synthesis: falsifiability test inline + analyst stance (C-12, C-11)
- Uncertainty: honest accountant stance + stakes connection (C-11)
- Recommendation: decision advocate stance + "Do not retreat to neutral language here" (C-11)
- Closing: "would a skeptic know exactly what evidence would change the verdict?" self-check (C-10, C-12)

This combination covers all five aspirational criteria structurally.

---

## Recommended Golden Candidate

**V-04** is the Round 2 recommended golden (99/100). It is one C-11 mechanism away from a perfect score. The deficiency is well-defined: add per-section voice anchors from V-05 to V-04's existing structure.

**Open question for Round 3**: Can V-04's inertia + falsifiability frame be combined with V-05's investigator-role stance and per-section register checkpoints without either mechanism suppressing the other? The compound variation is the clear Round 3 candidate.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["C-10 (decision-orientation) and C-12 (causal falsifiability) are the same question at different scales — 'what makes this claim defensible?' — so inertia framing and falsifiability instruction are synergistic; V-04 achieves both simultaneously because both mechanisms train the same epistemic habit in the author", "C-11 (register sustained across sections) is structurally orthogonal to C-10/C-12 — no variation achieves all three; per-section voice anchors prevent trailing-tone collapse but do not produce decision-orientation, and inertia framing produces decision-orientation but does not prevent section-level register drift; combining them is the Round 3 hypothesis", "Inline falsifiability self-check ('what specific evidence would disprove this?') is sufficient for C-12 without contrast examples — V-01's rhetorical form and V-04's negative example both pass; V-02's contrast block is the strongest instruction but not the minimum viable mechanism"]}
```
