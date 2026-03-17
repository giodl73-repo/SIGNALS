## Round 1 Scorecard — topic-story

| Rank | Variation | Essential | Recommended | Aspirational | Score |
|------|-----------|-----------|-------------|--------------|-------|
| 1 | V-04 Role + Editorial | 4/4 | 3/3 | 2/2 | **100** |
| 2 | V-02 Typed Template | 4/4 | 2.5/3 | 2/2 | **95** |
| 2 | V-05 Two-Pass | 4/4 | 2.5/3 | 2/2 | **95** |
| 4 | V-01 Hard Imperatives | 4/4 | 2/3 | 2/2 | **90** |
| 4 | V-03 Anti-Summary Priming | 4/4 | 2/3 | 1.5/2 | **90** |

All five variations are golden (all essential pass, composite ≥ 80).

---

**The single discriminator: C-05 (editorial voice)**

Every variation passes all four essential criteria. Every variation except V-03 passes both aspirational criteria. The entire spread from 90 to 100 is explained by C-05 and, for V-03, C-08/C-09.

V-04 wins because it is the only variation with explicit, redundant voice mechanisms — four stacked:
1. Named investigator role
2. Audience pressure ("team lead has ten minutes — they will not re-read the signals")
3. Concrete phrasing examples ("What's striking is...", "The evidence forces a conclusion I didn't expect...")
4. Trailing tone instruction ("Tone: editorial, not neutral.")

V-02 and V-05 score 95 — not 100 — because their structural mechanisms (template, pass gate) suppress verbosity and also suppress interpretive stance. Structured neutrality is not editorial voice.

---

**Three new patterns:**

1. **Audience pressure** is the strongest voice elicitor — accountability to a specific reader who won't re-read source material forces interpretation over reporting. No structural constraint reproduces this.

2. **Trailing tone instruction** is high-leverage at near-zero cost — adding "Tone: editorial, not neutral." to any other variation would likely close the C-05 gap.

3. **Causal contrast framing** (V-05's "not 'three signals agree' but 'three signals agree because [reason]'") is more reliable than a single-line imperative for C-09 — showing the distinction produces more consistent causal accounts than naming it.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Audience pressure ('team lead has ten minutes — they will not re-read the signals') is the strongest editorial voice elicitor — it creates accountability for interpretation rather than reporting, and no structural mechanism can substitute for it", "Trailing tone instruction ('Tone: editorial, not neutral.') is a high-leverage low-cost add-on — a single line after structural guidance lifts C-05 from PARTIAL to PASS at near-zero instruction cost in any variation", "C-09 causal logic is best elicited by contrast framing ('not three signals agree but three signals agree because [reason]') rather than a single-line imperative — showing the distinction produces more reliable causal accounts than naming it"]}
```
headers. Model fills fields only — structure cannot be dropped. |
| C-02 | Cross-Signal Synthesis | PASS | "[3-5 sentences. Cross-signal synthesis only. Do not restate per-signal findings.]" in template constraint. |
| C-03 | Pattern Explicitly Named | PASS | "Name the pattern explicitly: 'The signals converge on [X].'" + pre-printed `**Pattern**: [one sentence]` field forces extraction. |
| C-04 | Valid Recommendation with Rationale | PASS | `**Verdict**: [proceed / pause / pivot / abandon]` pre-printed. "Connect the verdict to the named pattern above." |
| C-05 | Author's Editorial Voice | PARTIAL | Template format actively works against editorial voice — filling typed fields produces correct structure but neutral register. No instruction for interpretive language or stance. |
| C-06 | Uncertainty Is Specific | PASS | Template constraint: "Format: 'We do not know [X] because [Y and Z signals gave conflicting results / no signal covered this angle].' Generic hedges do not count." Canonical form shown. |
| C-07 | Signal Findings Selective | PASS | Signal table enforces one sentence per finding: "If you need more than one sentence, you are summarizing. Pick the single most important thing." Tied to failure mode. |
| C-08 | Recommendation Is Action-Forcing | PASS | "'Proceed' alone is not sufficient — say what to proceed to." |
| C-09 | Pattern Has Causal Logic | PASS | Pattern section constraint: "Explain why — what shared assumption, constraint, or dynamic accounts for the convergence." Mechanism enumerated. |

**Essential**: 4/4 | **Recommended**: C-05 PARTIAL (5) + C-06 PASS (10) + C-07 PASS (10) = 25/30 | **Aspirational**: 2/2

```
composite = 60 + 25 + 10 = 95
```

**Score: 95 / 100 — GOLDEN**

---

### V-03: Anti-Summary Priming

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four-Section Structure | PASS | All four sections specified. |
| C-02 | Cross-Signal Synthesis | PASS | Strongest anti-summary framing in the set: extended negative example with explicit bad pattern ("Signal A found X. Signal B found Y... That is a summary.") + "The story tells the reader something they could not get by reading the signals individually." + final self-check before writing. |
| C-03 | Pattern Explicitly Named | PASS | "Name the pattern." |
| C-04 | Valid Recommendation with Rationale | PASS | "One of: proceed, pause, pivot, or abandon. Connected to the pattern. With a concrete next action." |
| C-05 | Author's Editorial Voice | PARTIAL | "This is a story. A story interprets." is thematic framing, not a voice instruction. No concrete phrasing examples. Model knows it should interpret but not how to sound while interpreting. |
| C-06 | Uncertainty Is Specific | PASS | "Specific, named unknowns. At least one question a follow-on investigation could actually address." |
| C-07 | Signal Findings Selective | PASS | "One sentence per signal." |
| C-08 | Recommendation Is Action-Forcing | PARTIAL | "With a concrete next action." — present but brief and un-reinforced. No negative example, no "X alone is not sufficient" framing. Risk of vague action clause. |
| C-09 | Pattern Has Causal Logic | PARTIAL | "Explain why the signals converge, not just that they do." — one-line instruction buried after the anti-summary framing. No mechanism or example. Weaker than V-04/V-05. |

**Essential**: 4/4 | **Recommended**: C-05 PARTIAL (5) + C-06 PASS (10) + C-07 PASS (10) = 25/30 | **Aspirational**: C-08 PARTIAL (2.5) + C-09 PARTIAL (2.5) = 5/10

```
composite = 60 + 25 + 5 = 90
```

**Score: 90 / 100 — GOLDEN**

Note: V-03's anti-summary priming is the strongest C-02 mechanism in the set. The extended failure mode description with concrete bad example is more durable than a single imperative. This qualitative advantage is invisible in the composite score.

---

### V-04: Role Sequence + Editorial Voice

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four-Section Structure | PASS | All sections explicit with clear headers and sequencing instructions. |
| C-02 | Cross-Signal Synthesis | PASS | "Step back from individual signals and ask: what shape does this evidence take?" + investigator framing keeps synthesis as the primary frame throughout the document. |
| C-03 | Pattern Explicitly Named | PASS | "Name it." — implicit in "what pattern emerges?" and explicit in the synthesis section instruction. |
| C-04 | Valid Recommendation with Rationale | PASS | "The verdict: proceed, pause, pivot, or abandon. State it clearly. Connect it to the pattern you named." |
| C-05 | Author's Editorial Voice | PASS | Strongest voice mechanism in the set. Four independent mechanisms: (1) named investigator stance, (2) audience pressure ("your team lead has ten minutes — they will not re-read the signals"), (3) concrete phrasing examples ("What's striking is...", "The evidence forces a conclusion I didn't expect..."), (4) trailing instruction: "Tone: editorial, not neutral." Redundant from four angles — the model cannot miss the voice register. |
| C-06 | Uncertainty Is Specific | PASS | "Name the specific unknowns — by signal gap, by conflicting result, by untested assumption. At least one concrete question that a follow-on investigation could answer." |
| C-07 | Signal Findings Selective | PASS | "For each signal: one sentence." + the investigator-voice framing models the one-sentence form by example: "The feasibility signal settled the technical risk question — the API rate limits are not a blocker." |
| C-08 | Recommendation Is Action-Forcing | PASS | "The thing someone should do Monday morning." Highest-specificity action-forcing phrase in the set. |
| C-09 | Pattern Has Causal Logic | PASS | "Why do the signals converge here? What shared assumption or structural constraint explains the alignment (or tension)?" — asks the causal question directly as a question the investigator must answer. |

**Essential**: 4/4 | **Recommended**: C-05 PASS (10) + C-06 PASS (10) + C-07 PASS (10) = 30/30 | **Aspirational**: 2/2

```
composite = 60 + 30 + 10 = 100
```

**Score: 100 / 100 — GOLDEN**

---

### V-05: Two-Pass Structure

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four-Section Structure | PASS | All five sections specified in Pass 2, explicitly labeled and gated by pass boundary. |
| C-02 | Cross-Signal Synthesis | PASS | Pass boundary structurally enforces synthesis: "what do these one-sentence findings have in common that none of them says individually?" + "A reader who had read your Pass 1 extractions but not this section would not know what the investigation found." |
| C-03 | Pattern Explicitly Named | PASS | "Name the pattern." |
| C-04 | Valid Recommendation with Rationale | PASS | "Verdict: proceed / pause / pivot / abandon. Grounded in Section 3's pattern — cite it by name or paraphrase." |
| C-05 | Author's Editorial Voice | PARTIAL | Two-pass mechanical process frames the task as extraction-then-assembly, which produces correct structure but neutral register. No explicit editorial voice instruction. Pass discipline suppresses verbosity and interpretive stance simultaneously. |
| C-06 | Uncertainty Is Specific | PASS | "Gaps in the Pass 1 extractions — signals that conflicted, questions the strategy planned for but no signal answered, or dimensions that no signal covered. Name them specifically. One concrete open question minimum." |
| C-07 | Signal Findings Selective | PASS | Pass 1 structurally enforces selectivity: "extract exactly one thing... one sentence. If you cannot compress to one sentence, compress harder." Strongest structural C-07 enforcement in the set. |
| C-08 | Recommendation Is Action-Forcing | PASS | "Action-forcing: specify the next concrete step beyond the verdict." |
| C-09 | Pattern Has Causal Logic | PASS | Most explicit causal formulation in the set: "not 'three signals agree' but 'three signals agree because [underlying reason]'" — shows the model the distinction by contrast rather than by instruction alone. |

**Essential**: 4/4 | **Recommended**: C-05 PARTIAL (5) + C-06 PASS (10) + C-07 PASS (10) = 25/30 | **Aspirational**: 2/2

```
composite = 60 + 25 + 10 = 95
```

**Score: 95 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | C-05 voice | C-09 causal |
|------|-----------|-----------|-------------|--------------|-----------|-----------|------------|
| 1 | V-04 Role + Editorial | 4/4 | 3/3 | 2/2 | **100** | PASS (4 mechanisms) | PASS (causal question) |
| 2 | V-02 Typed Template | 4/4 | 2.5/3 | 2/2 | **95** | PARTIAL (template suppresses) | PASS (enumerated) |
| 2 | V-05 Two-Pass | 4/4 | 2.5/3 | 2/2 | **95** | PARTIAL (process suppresses) | PASS (contrast framing) |
| 4 | V-01 Hard Imperatives | 4/4 | 2/3 | 2/2 | **90** | PARTIAL (no tone instruction) | PASS (one-line) |
| 4 | V-03 Anti-Summary Priming | 4/4 | 2/3 | 1.5/2 | **90** | PARTIAL (thematic only) | PARTIAL (one-line, buried) |

**C-05 (editorial voice) is the primary discriminator between 100 and 95.** V-04 is the only variation with explicit, redundant voice mechanisms. All others suppress voice or ignore it.

**C-08/C-09 (aspirational) distinguishes 95/90 from 90.** V-03 scores only PARTIAL on both aspirational criteria — its C-08 and C-09 instructions are brief and un-reinforced.

---

## C-05 Analysis: Why Format and Process Cannot Substitute for Voice

| Variation | C-05 mechanism | Why it fails to pass |
|-----------|---------------|----------------------|
| V-02 | None | Template field-filling produces structured neutrality |
| V-05 | None | Pass discipline suppresses verbosity and interpretive stance together |
| V-01 | None | Imperatives enforce content, not tone |
| V-03 | Thematic framing ("this is a story") | Model knows the goal, not the form |
| V-04 | 4-mechanism stack | PASS |

**C-05 compliance cannot be patched by format constraints.** Pre-printed templates (V-02) and pass gates (V-05) improve C-07 selectivity but produce structured neutrality, not editorial voice. Voice requires a separate mechanism orthogonal to structure: audience, role, or explicit tone instruction.

The cheapest lift: a single trailing line ("Tone: editorial, not neutral.") added to V-01, V-02, V-03, or V-05 would likely move C-05 from PARTIAL to PASS at near-zero instruction cost.

---

## Excellence Signals — Round 1

### E-1: Audience pressure is the strongest editorial voice elicitor

V-04's "your team lead has ten minutes — they will not re-read the signals" does two things simultaneously: it creates accountability (someone is making a decision from this document) and forces distillation (ten minutes leaves no room for signal-by-signal recapping). The named audience explains why the investigator has an opinion. This mechanism is absent from every other variation and cannot be reproduced by structural constraints.

### E-2: Trailing tone instruction is high-leverage at near-zero cost

V-04's "Tone: editorial, not neutral." is a single trailing line that closes the door on neutral register after all structural guidance is given. Adding this line to V-02 or V-05 — which otherwise have good structural coverage — would likely close the C-05 gap without disrupting their template or pass mechanisms.

### E-3: V-05's causal contrast framing is worth importing

V-05 contains the most explicit C-09 instruction in the set: "not 'three signals agree' but 'three signals agree because [underlying reason]'". This contrast framing shows the model exactly what the distinction looks like — correlation description vs. causal account. Adding this to V-04 or V-02 (which already pass C-09 by instruction) would make an already-passing criterion more reliable.

### E-4: Anti-summary priming (V-03) is the strongest C-02 mechanism but orthogonal to C-05

V-03's extended failure-mode description with concrete bad example is the most durable anti-summary mechanism in the set. It primes C-02 resistance throughout the task, not just at the synthesis section. However, the mechanism is purely negative — it tells the model what not to do without telling it how to voice what it does instead. This is why V-03 and V-01 score identically despite V-03's superior C-02 coverage: anti-summary priming buys nothing on C-05.

---

## Recommended Golden Candidate

**V-04** is the clear Round 1 recommended golden:
- Only variation to achieve 100/100
- Only variation with reliable C-05 elicitation through four stacked mechanisms
- Audience pressure mechanism ("team lead has ten minutes") is novel and high-value
- Passes all essential, recommended, and aspirational criteria without exception

**Open question for Round 2**: Can V-04's voice mechanisms be combined with V-05's two-pass selectivity enforcement? The hypothesis: audience pressure + pass gate produces editorial voice (C-05) and structural selectivity (C-07) simultaneously, without either mechanism weakening the other. This combination is untested.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Audience pressure ('team lead has ten minutes — they will not re-read the signals') is the strongest editorial voice elicitor — it creates accountability for interpretation rather than reporting, and no structural mechanism can substitute for it", "Trailing tone instruction ('Tone: editorial, not neutral.') is a high-leverage low-cost add-on — a single line after structural guidance lifts C-05 from PARTIAL to PASS at near-zero instruction cost in any variation", "C-09 causal logic is best elicited by contrast framing ('not three signals agree but three signals agree because [reason]') rather than a single-line imperative — showing the distinction produces more reliable causal accounts than naming it"]}
```
