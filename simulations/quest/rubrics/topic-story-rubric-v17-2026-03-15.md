Reading the two excellence signals from the R17 scorecard and mapping them to criteria:

- **ES-01** → C-44: Dual depth coverage without architectural conflict (depth, aspirational)
- **ES-02** → C-45: Proportionality check as structural closing act of recommendation beat (correctness, aspirational)

```markdown
# Quest Rubric — `topic-story` v17

**Version:** v17
**Source rounds:** R1–R17
**Rubric version history:**
- v16 → v17: +2 aspirational criteria (C-44, C-45); N_aspirational 36 → 38
- v15 → v16: +2 aspirational criteria (C-42, C-43); N_aspirational 34 → 36
- v14 → v15: +2 aspirational criteria (C-40, C-41); N_aspirational 32 → 34
- v13 → v14: +1 aspirational criterion (C-39); N_aspirational 31 → 32
- v12 → v13: +3 aspirational criteria (C-36, C-37, C-38); N_aspirational 28 → 31
- v11 → v12: +3 aspirational criteria (C-33, C-34, C-35); N_aspirational 25 → 28
- v10 → v11: +3 aspirational criteria (C-30, C-31, C-32); N_aspirational 22 → 25
- v9 → v10: +2 aspirational criteria (C-28, C-29); N_aspirational 20 → 22

**What changed from v16 to v17:**

| | v16 | v17 |
|--|-----|-----|
| Version | v16 | v17 |
| Source rounds | R1–R16 | R1–R17 |
| Aspirational count | 36 | 38 |
| Total criteria | 43 | 45 |
| Composite formula denominator | 36 | 38 |

**New aspirational criteria from R17 (V-02 excellence signals):**

| C | Name | Axis | Category |
|---|------|------|----------|
| C-44 | Dual depth coverage without architectural conflict | V-02 | depth |
| C-45 | Proportionality check as structural closing act of recommendation beat | V-02 | correctness |

---

## Essential Criteria

Output is not usable if any essential criterion fails.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Bottom Line Up Front** | correctness | essential | The recommendation or verdict appears in the opening paragraph or first named section — not buried at the end. A story that builds to a conclusion fails. A story where the first substantive sentence is hedging or context-setting fails. |
| C-02 | **Labeled sections present** | format | essential | The story contains the five named beats: *What we set out to understand / What the signals revealed / What the signals say together / What remains uncertain / The recommendation*. Any beat missing or renamed beyond recognition fails. |
| C-03 | **Cross-signal synthesis present** | correctness | essential | Beat 3 states a claim that references what two or more signals show *together* that no single signal shows alone. A sentence that could be derived from reading any single artifact fails. Restating artifact summaries side by side fails. |
| C-04 | **Pattern, not summary** | depth | essential | The synthesis claim names a relationship, tension, or gap across signals — not a collection of findings. A sentence equivalent to "Signal A said X and Signal B said Y" fails. The pattern must name a synthetic claim (e.g., "users want X but the technical cost is Y — the gap is the risk"). Restating individual findings side by side fails. |

---

## Recommended Criteria

Output is meaningfully better when these pass.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Signal coverage is grounded** | coverage | recommended | At least three distinct signal namespaces or artifact types are referenced to show what evidence base the story draws from. Not exhaustive enumeration — enough to make the synthesis credible. Fewer than three identifiable signal sources fails. |
| C-06 | **Uncertainty is specific** | depth | recommended | The "what remains uncertain" section names at least one specific open question that, if resolved, would change the recommendation. Generic hedges such as "more research may be needed" without naming what research or what it would change fail. |
| C-07 | **Recommendation proportionality** | correctness | recommended | The recommendation weight is consistent with the evidence described. Strong positive signals → proceed; mixed → pause; conflicting → pivot; weak or negative → abandon. A proceed recommendation following a story of conflicts and gaps fails; an abandon recommendation following a story of strong positive signals fails. |

---

## Aspirational Criteria

These define the ceiling. Each pass raises the composite score above the essential+recommended floor.
Composite score = (aspirational passes) / 38.

*C-08 through C-39: unchanged from v15.*

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-40 | **Verdict as literal first line** | format | The verdict sentence is the topmost line of output — before any section heading, structural label, role marker, or part delimiter. An output that passes C-01 (verdict in opening section) but places the verdict after even one structural heading (`## ANALYST BRIEF`, `ROLE 2: AUTHOR`, `PART 1: DECISION CARD`) fails. First line means topmost line. |
| C-41 | **Pattern necessity test** | depth | The synthesis claim in BLOCK P passes a necessity test: the claim is false or unprovable if either signal it references were removed. A claim that references two signals but is supportable by either alone fails. "Signal A shows X and Signal B shows Y, therefore Z" fails if Z follows from X alone or Y alone. Each referenced signal must be a load-bearing premise for the claim. |
| C-42 | **Genre contract as structural BLUF enforcer** | format | The story prompt uses a genre frame (e.g., "editorial brief") rather than explicit multi-part architectural labels (ROLE 1/2, PART 1/2, DECISION CARD) to produce verdict-first output. Explicit structural scaffolding and literal-first-line verdict placement are in tension: a labeled section architecture creates pressure to place a heading before the verdict. A genre frame resolves the tension by making the rule structurally redundant — the genre carries it. A prompt that instructs "verdict first" while also imposing a labeled multi-section architecture before the verdict fails: the instruction and the architecture are in conflict, and the architecture wins in the output stream. |
| C-43 | **Decision-flip conditional per uncertainty item** | depth | Each open question in the uncertainty beat is articulated as a binary conditional: "if this resolves one way, the verdict holds; if it resolves the other, the verdict changes." C-06 (recommended) requires uncertainty to be specific and decision-linked — naming what question and what it would change. C-43 requires the decision-link to be a flip test: the model states which resolution direction holds the verdict and which direction flips it. Prohibition form (names what fails) and standard form (names the test criterion) both pass C-06 but not C-43. Naming an uncertainty without mapping both resolution branches to verdict outcomes fails. |
| C-44 | **Dual depth coverage without architectural conflict** | depth | The prompt explicitly instructs both the necessity test (C-41) and the decision-flip conditional (C-43) within a single prompt that does not impose a multi-part labeled architecture (ROLE/PART delimiters) that creates structural tension with BLUF placement. The two depth criteria are mutually reinforcing: the necessity test primes the model to read cross-signal relationships; the flip-test forces those relationships to be decision-relevant. A prompt that instructs only one of the two depth criteria fails. A prompt that instructs both but wraps them in a labeled multi-section architecture that conflicts with C-40 or C-42 fails. Both criteria must be present and the structural frame must not undermine them. |
| C-45 | **Proportionality check as structural closing act of recommendation beat** | correctness | The recommendation beat's final instruction is an explicit proportionality audit directed at the model: the prompt requires the model to verify that its recommendation weight matches the evidence described in the synthesis beat immediately before closing the recommendation section. This closes C-07 structurally — the beat's final act is a self-consistency check — rather than relying on general instruction compliance or a standalone proportionality note elsewhere in the prompt. A prompt that includes a proportionality instruction as a general preamble, standalone note, or anywhere other than as the closing instruction within the recommendation beat itself fails. The check must be the last instruction the model executes inside the recommendation beat. |

---

## Composite Score Formula

```
Composite = (count of aspirational criteria that PASS) / 38
```

Essential and recommended criteria are pass/fail gates; they do not contribute to the composite
numerator. A story that fails any essential criterion scores 0 regardless of aspirational performance.
```
