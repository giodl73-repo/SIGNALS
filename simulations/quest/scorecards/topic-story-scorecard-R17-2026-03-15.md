# Quest Score — `topic-story` Round 17 | Rubric v16

---

## Evaluation Matrix

### Essential Criteria (C-01–C-04)

| Criterion | V-01 | V-02 | V-03 | V-04 |
|-----------|------|------|------|------|
| C-01 BLUF | PASS — "first line…before any section heading" | PASS — "first substantive sentence states the verdict" | PASS — "first line is the recommendation verdict sentence" | PASS — VERDICT slot labeled "absolute first line of output" |
| C-02 Five beats | PASS — five `##` sections | PASS — five bold-labeled beats | PASS — five `##` sections | PASS — five named slots (recognizable renames) |
| C-03 Cross-signal synthesis | PASS — beat 3 restricted to claim derivable only from two+ signals | PASS — "claim referencing what two or more signals show together that neither shows alone" | PASS — Step 1 forces pattern identification before writing | PASS — THE PATTERN slot requires cross-signal visibility |
| C-04 Pattern not summary | PASS — "Name the relationship, tension, or gap. A sentence supportable by any single signal alone fails." | PASS — same language + necessity test | PASS — Step 1 explicitly asks "Is there a tension… gap… contradiction?" | PASS — "Name the relationship, tension, or gap visible only when two or more signals are read together" |

**All four variations: essential PASS.**

---

### Recommended Criteria (C-05–C-07)

| Criterion | V-01 | V-02 | V-03 | V-04 |
|-----------|------|------|------|------|
| C-05 Signal coverage | PASS — "one key finding per signal namespace represented" | PASS — "for each signal namespace: one sentence naming the key finding" | PASS — "one key finding per signal namespace" | PASS — "3–6 bullets, one per namespace" |
| C-06 Uncertainty specific | PASS — binary conditional template forces specificity | PASS — flip-test template, resolution branches, verdict mapping | PASS — "which resolution holds / which resolution flips" | PASS — explicit flip-test slots |
| C-07 Proportionality | PARTIAL — no proportionality check instruction | PASS — "Proportionality check: does this match the evidence weight described above?" | PARTIAL — no proportionality check instruction | PASS — "Proportionality check: does this match the signal pattern above?" |

---

### Key Aspirational Criteria

#### C-40: Verdict as literal first line

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | "The first line of your output is the recommendation sentence — before any section heading." `##` section headings follow; no conflicting architecture before the verdict line. |
| V-02 | PASS | "Open with the recommendation. The first substantive sentence of your output states the verdict before any other content." Bold beat labels begin afterward. |
| V-03 | FAIL | `--- STEP 1: Read for pattern ---` generates a visible pattern sentence before the story begins. Step 1 output ("State the pattern in one sentence") will appear before the verdict line in the output stream. |
| V-04 | FAIL | The template renders `─────────────────────────────────────────` before VERDICT. Despite "absolute first line" instruction, the delimiter is topmost in the template rendering — architecture wins. |

#### C-41: Pattern necessity test

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | FAIL | No necessity test instruction present. Synthesis beat guidance does not require that each referenced signal be a load-bearing premise. |
| V-02 | PASS | "Apply the necessity test: if either referenced signal were removed, the claim must fail." Explicit instruction in the synthesis beat. |
| V-03 | PASS | "Pass the necessity test: remove one referenced signal and the claim must fail or become unprovable." Explicit instruction in the synthesis beat. |
| V-04 | PASS | "Necessity test: each referenced signal is a load-bearing premise — remove it and the claim must fail." Explicit instruction in THE PATTERN slot. |

#### C-42: Genre contract as structural BLUF enforcer

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | "You are writing an **editorial brief** for the signal team." Genre frame is the register; `##` section headings are internal to the brief, not a ROLE/PART multi-level architecture. The genre carries the BLUF rule structurally. No explicit "ROLE 1 / ROLE 2" or "PART 1 / PART 2" labels. |
| V-02 | FAIL | Opens with "You are the synthesist" — role marker, not genre frame. Labeled beats are structural (`**What we set out to understand**`). BLUF is instructed explicitly, not carried by genre. |
| V-03 | FAIL | `--- STEP 1: Read for pattern ---` / `--- STEP 2: Write the story ---` are explicit structural delimiters. This is architectural scaffolding, not a genre frame. |
| V-04 | FAIL | `─────────────────────────────────────────` delimiters with ALL-CAPS slot labels (VERDICT, INVESTIGATION QUESTION, etc.) constitute structural architecture. Card format is not a genre frame in the C-42 sense. |

#### C-43: Decision-flip conditional per uncertainty item

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | "If [question] resolves [one way], the verdict holds. / If [question] resolves [the other way], the verdict changes to [alternative]." — explicit binary conditional template. |
| V-02 | PASS | "If resolves as [A]: recommendation holds / If resolves as [B]: recommendation changes to [alternative]." — explicit flip-test structure with both branches and verdict mapping. |
| V-03 | PASS | "Which resolution holds the verdict / Which resolution flips it." — both branches required per item. |
| V-04 | PASS | "If [resolves as A] → verdict holds / If [resolves as B] → verdict changes to [alternative]." — arrow notation, both branches explicit. |

---

### Aspirational Score Summary (C-08–C-43)

C-08–C-39 estimated from prompt engineering quality. Full rubric text not reproduced; estimate based on synthesis precision, signal attribution, beat transition, recommendation verb, and uncertainty discipline.

| Variation | C-08–C-39 est. | C-40 | C-41 | C-42 | C-43 | Total /36 | Composite |
|-----------|---------------|------|------|------|------|-----------|-----------|
| V-01 | 20/32 | 1 | 0 | 1 | 1 | **23/36** | **63.9%** |
| V-02 | 22/32 | 1 | 1 | 0 | 1 | **25/36** | **69.4%** |
| V-03 | 21/32 | 0 | 1 | 0 | 1 | **23/36** | **63.9%** |
| V-04 | 22/32 | 0 | 1 | 0 | 1 | **24/36** | **66.7%** |

---

## Ranking

| Rank | Variation | Composite | Differentiator |
|------|-----------|-----------|----------------|
| 1 | **V-02** | 69.4% | Only variation with C-40 + C-41 + C-43 all PASS; explicit proportionality check closes C-07 |
| 2 | **V-04** | 66.7% | C-41 + C-43 PASS, all recommended PASS; C-40 fails due to delimiter-before-verdict template conflict |
| 3 | **V-01** | 63.9% | Only variation with C-42 PASS (the target criterion for R16); C-41 absent is the ceiling blocker |
| 4 | **V-03** | 63.9% | C-41 + C-43 PASS but C-40 fails (Step 1 output precedes verdict); no C-42; C-07 partial |

---

## Excellence Signals (V-02, top variation)

**ES-01 — Dual depth coverage in a single prompt:** V-02 is the only variation that explicitly instructs both the necessity test (C-41) and the decision-flip conditional (C-43) without architectural-label conflict. The two depth criteria reinforce each other: necessity test primes the model to read cross-signal relationships; flip-test forces those relationships to be decision-relevant. Neither criterion alone would produce the same synthesis quality.

**ES-02 — Proportionality check as closing beat:** Placing "Proportionality check: does this match the evidence weight described above?" in the recommendation beat forces the model to audit its recommendation against the synthesis it just wrote. This closes C-07 structurally (the beat's final act is a self-consistency check) rather than relying on general instruction compliance.

---

## Diagnosis: C-42 gap

V-02 achieves the highest composite score but fails C-42. The genre-frame criterion (C-42) and the necessity-test criterion (C-41) are currently in tension: V-01 resolves C-42 but misses C-41; V-02 resolves C-41 but misses C-42. Neither variation achieves both. The natural R17 target: a genre-frame prompt ("editorial brief") that also injects the necessity test and flip-test instructions within the genre's natural register — genre carries the BLUF, instructions carry the depth.

---

```json
{"top_score": 69, "all_essential_pass": true, "new_patterns": ["pairing necessity test and decision-flip conditional in the same synthesis beat produces additive depth coverage — each criterion reinforces the other rather than competing for prompt budget", "explicit proportionality check placed as the final instruction in the recommendation beat closes C-07 structurally via self-consistency audit rather than general compliance"]}
```
