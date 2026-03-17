## Scoring: topic-story — Round 1, Rubric v1

No trace artifact (placeholder) — scoring evaluates prompt design against rubric criteria: how reliably does each variation's mechanism produce passing outputs?

**Partial credit**: PARTIAL = 0.5 (mechanism present but weaker or fallible)

---

### V-01 — Pre-write synthesis worksheet

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Synthesis, not summary | **PASS** | Q2 extracts one finding per signal; Q3 explicitly gates on "no single signal shows alone." Two-stage structure prevents simultaneous extraction + composition. |
| C-02 | Five structural elements | **PASS** | Beats 1–5 named and required. Beat 4 (uncertainty) and Beat 5 (recommendation) are both mandatory by name. |
| C-03 | Explicit, grounded recommendation | **PASS** | Q4 requires provisional verb + Beat 5 must connect explicitly to Beat 3 pattern. Q4→Beat 5 anchors the recommendation to the synthesis. |
| C-04 | Cross-signal pattern | **PASS** | Q3 is the load-bearing gate: "if your answer could be derived from any single artifact alone, it is not a cross-signal pattern — find the real one." Written deliverable before prose begins. |
| C-05 | Signal coverage grounded | **PASS** | Globs `simulations/**/{topic}-*` and reads every artifact. |
| C-06 | Uncertainty is specific | **PASS** | Beat 4: "Scope each: what exactly is unknown, and why does it matter for the decision? No generic disclaimers." |
| C-07 | Recommendation proportionality | **PARTIAL** | Q4 asks direction given Q3 pattern, and Beat 5 connects to Beat 3 — but no explicit proportionality bands (strong signals → proceed, etc.). Proportionality is implied, not enforced. |
| C-08 | Narrative arc | **PASS** | Sequential five-beat structure creates natural intent → evidence → resolution arc. Voice section: "Write as an author, not as a reporter." |
| C-09 | Delta surfacing | **FAIL** | No instruction to call out "expected X but found Y." Worksheet does not prompt for surprises. |

**Essential:** 4/4 = 60 pts
**Recommended:** (1 + 1 + 0.5)/3 × 30 = 25 pts
**Aspirational:** (1 + 0)/2 × 10 = 5 pts
**Composite: 90**

---

### V-02 — Anti-summary prohibition with precise contrast

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Synthesis, not summary | **PASS** | Synthesis/summary contrast placed first (primacy anchor). "Find the pattern before writing" is explicit. Beat 3 inline failure test. Three distinct mechanisms. |
| C-02 | Five structural elements | **PASS** | All five elements numbered and explicit. |
| C-03 | Explicit, grounded recommendation | **PASS** | Four-verb constraint. Warning: "if you find yourself writing 'proceed with caution' without saying what the caution is... stop and rewrite." |
| C-04 | Cross-signal pattern | **PARTIAL** | "Find the pattern before writing" instruction exists, but it's a mental step, not a written deliverable. The model can interpret it as a soft checkpoint and skip it. Weaker than V-01's worksheet gate. |
| C-05 | Signal coverage grounded | **PASS** | Reads every artifact. |
| C-06 | Uncertainty is specific | **PASS** | Element 4: "Name what exactly is unknown and why it matters for the recommendation." |
| C-07 | Recommendation proportionality | **PARTIAL** | Element 5 connects to element 3 pattern, but no explicit proportionality rule. |
| C-08 | Narrative arc | **PARTIAL** | Five-section structure flows but no explicit arc instruction. "Confident, active voice" helps, but weaker arc guidance than V-01. |
| C-09 | Delta surfacing | **FAIL** | No instruction. |

**Essential:** (1 + 1 + 1 + 0.5)/4 × 60 = 52.5 pts
**Recommended:** (1 + 1 + 0.5)/3 × 30 = 25 pts
**Aspirational:** (0.5 + 0)/2 × 10 = 2.5 pts
**Composite: 80**

*Note: C-04 PARTIAL means C-04 is at risk in execution — not a full essential pass.*

---

### V-03 — Decision memo to named stakeholder

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Synthesis, not summary | **PARTIAL** | "What the Signals Showed" is explicitly per-signal (one finding per signal) — structurally enumeration-compatible. "These are evidence for the Bottom Line, not a tour" pushes back, but the per-signal format is a weak gate. |
| C-02 | Five structural elements | **PASS** | Bottom Line (recommendation), What We Set Out to Understand, What the Signals Showed (findings), The Pattern (cross-signal), What We Don't Know Yet (uncertainty) — all five rubric elements present under different names. |
| C-03 | Explicit, grounded recommendation | **PASS** | Bottom Line is the first section; must open with one of four verbs. Strongest C-03 mechanism in the set — cannot skip. |
| C-04 | Cross-signal pattern | **PARTIAL** | Pattern section exists with explicit cross-signal language. Consistency check ("if the pattern does not justify the Bottom Line, revise one of them") creates backward pressure. But BLUF-first means the Bottom Line is written before the Pattern — the risk identified in the hypothesis. No pre-composition gate. |
| C-05 | Signal coverage grounded | **PASS** | Reads every artifact. |
| C-06 | Uncertainty is specific | **PASS** | "What We Don't Know Yet: scope each: what exactly is unknown, and what does it cost the recommendation? If an answer would change the Bottom Line, say so explicitly." Decision-cost framing is the strongest C-06 instruction in the set. |
| C-07 | Recommendation proportionality | **PARTIAL** | Structural consistency enforced (Bottom Line and Pattern must match), but no explicit proportionality bands. Implicit, not enforced. |
| C-08 | Narrative arc | **PASS** | BLUF memo creates a distinct arc: decision stakes → question → evidence → pattern → uncertainty. The "three minutes" framing activates executive communication patterns that suppress meandering. |
| C-09 | Delta surfacing | **FAIL** | No instruction. |

**Essential:** (0.5 + 1 + 1 + 0.5)/4 × 60 = 45 pts
**Recommended:** (1 + 1 + 0.5)/3 × 30 = 25 pts
**Aspirational:** (1 + 0)/2 × 10 = 5 pts
**Composite: 75**

---

### V-04 — Worksheet (V-01) + Anti-summary prohibition (V-02)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Synthesis, not summary | **PASS** | Three-layer protection: opening synthesis/summary contrast (primacy), Step 2 pattern identification (analytical gate), synthesis check before writing Beat 3 ("Could any single signal have produced this conclusion?"). |
| C-02 | Five structural elements | **PASS** | Labeled scaffold with all five sections explicit. |
| C-03 | Explicit, grounded recommendation | **PASS** | Four-verb constraint + "connect the recommendation to the pattern named above." |
| C-04 | Cross-signal pattern | **PASS** | Step 2 Q3: must name what two+ signals show together that no single shows alone; artifact references required; failure condition stated. Plus synthesis check inline. Strongest analytical gate. |
| C-05 | Signal coverage grounded | **PASS** | Reads every artifact. |
| C-06 | Uncertainty is specific | **PASS** | "What Remains Uncertain" bullets: name the gap, scope it, state why it matters for the recommendation. |
| C-07 | Recommendation proportionality | **PARTIAL** | Synthesis check connects pattern to recommendation, but no explicit proportionality bands. Implied but not enforced. |
| C-08 | Narrative arc | **PASS** | Sequential five-section scaffold with labeled intent → evidence → pattern → uncertainty → recommendation arc. |
| C-09 | Delta surfacing | **FAIL** | No instruction in either source variation. |

**Essential:** 4/4 × 60 = 60 pts
**Recommended:** (1 + 1 + 0.5)/3 × 30 = 25 pts
**Aspirational:** (1 + 0)/2 × 10 = 5 pts
**Composite: 90**

---

### V-05 — Memo (V-03) + Anti-summary prohibition (V-02)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Synthesis, not summary | **PASS** | Opens with synthesis/summary distinction. Explicit "Find the pattern before writing" step. Per-signal section framed as "evidence, not a tour of artifacts." |
| C-02 | Five structural elements | **PASS** | Bottom Line, What We Set Out to Understand, What the Signals Showed, The Pattern, What We Don't Know Yet — all five elements present. |
| C-03 | Explicit, grounded recommendation | **PASS** | Bottom Line opens with PROCEED/PAUSE/PIVOT/ABANDON. Positioned first; unavoidable. |
| C-04 | Cross-signal pattern | **PASS** | "Find the pattern before writing" is a named pre-composition step. Pattern section has falsifiability test ("if your pattern claim could have come from any single signal, it is not a cross-signal pattern. Find the real one."). Bidirectional consistency requirement. Three distinct gates. |
| C-05 | Signal coverage grounded | **PASS** | Reads every artifact. |
| C-06 | Uncertainty is specific | **PASS** | "Scope each: what is unknown and what would it cost the recommendation? If an answer would change the Bottom Line, say so." Decision-cost framing drives specificity. |
| C-07 | Recommendation proportionality | **PASS** | Unique in the set: "This section must justify the Bottom Line. If the pattern does not support the recommendation, **revise one of them** — they must be consistent." Bidirectional enforcement, not just a connection instruction. The model must either fix the pattern or fix the Bottom Line — no escape route. |
| C-08 | Narrative arc | **PASS** | Memo arc (Bottom Line → question → evidence → pattern → uncertainty) is traversable without consulting source signals. "Declarative. Opinionated." |
| C-09 | Delta surfacing | **FAIL** | No instruction. |

**Essential:** 4/4 × 60 = 60 pts
**Recommended:** 3/3 × 30 = 30 pts
**Aspirational:** (1 + 0)/2 × 10 = 5 pts
**Composite: 95**

---

## Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | Score | All Ess. |
|-----------|------|------|------|------|------|------|------|------|------|-------|----------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PART | PASS | FAIL | **90** | YES |
| V-02 | PASS | PASS | PASS | PART | PASS | PASS | PART | PART | FAIL | **80** | NO |
| V-03 | PART | PASS | PASS | PART | PASS | PASS | PART | PASS | FAIL | **75** | NO |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PART | PASS | FAIL | **90** | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | **95** | YES |

**Rank**: V-05 > V-01 = V-04 > V-02 > V-03

---

## Excellence Signals (from V-05)

**1. Bidirectional consistency enforcement on C-07.**
V-01/V-02/V-04 all say "connect the recommendation to the pattern." V-05 says "if the pattern does not support the recommendation, *revise one of them*." The revision requirement closes the escape route where a model acknowledges the connection instruction but writes inconsistently anyway. This is the only mechanism in the set that produces a true C-07 PASS.

**2. Pre-composition pattern identification as a named prerequisite step.**
Both V-04 and V-05 place pattern identification as an explicit named step ("Find the pattern before writing") before the output artifact opens. This is stronger than V-02's inline "find the pattern" (which can be collapsed into the writing step) and stronger than V-01's worksheet (which is a heavier mechanism). The named prerequisite step is the minimum effective dose.

**3. Falsifiability test embedded at the point of writing.**
The Pattern section in V-05 includes "if your pattern claim could have come from any single signal, it is not a cross-signal pattern. Find the real one." Placing this test *inside* the section instruction — not as a general preamble — makes it a checklist item at the moment the model is writing Beat 3. This is more reliable than preamble instructions because it fires at the right moment.

**4. Memo register activates proportionality pressure organically.**
The decision-maker framing in V-03/V-05 creates forward pressure that the story format does not: the recipient needs to decide, not just understand. This register naturally prevents soft or vague recommendations even without explicit proportionality bands — the memo context makes vagueness feel wrong.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["Bidirectional consistency enforcement: requiring the model to revise Pattern or Bottom Line until they are consistent (not merely connected) is the minimum mechanism for reliable C-07 compliance", "Pre-composition pattern identification as a named prerequisite step before opening the output artifact closes C-04 failures that inline composition instructions cannot prevent"]}
```
