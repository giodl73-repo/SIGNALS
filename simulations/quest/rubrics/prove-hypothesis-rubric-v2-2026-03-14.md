Here is the complete v2 rubric:

---

# prove:hypothesis Rubric -- v2

**Version**: v2 | **Date**: 2026-03-14

---

## What changed from v1

| Change | Reason |
|--------|--------|
| **C-10 pass condition sharpened** | V-01 and V-03 both had rank columns and both failed — the discriminator was the rationale column alongside rank. Pass condition now requires both. |
| **C-11 added** — Adversarial role gate (Skeptic) | V-04 pattern: per-condition PASS/REWRITE verdict is the strongest structural enforcement for C-02. Subjective conditions can't silently pass a named role gate. |
| **C-12 added** — Hard phase gate with read-only constraint | V-05 pattern: a checklist that locks prior phases is the strongest C-05 enforcement. Ordering hints (V-02) are the weakest form; structural locks are the strongest. |
| **C-13 added** — Status-quo as competing hypothesis | V-03 pattern: F-00 as a named falsification condition produces deeper inertia evaluation and richer C-08 evidence than generic falsification lists. |
| **Scoring denominator** | Aspirational raised from `/2` to `/5`; each aspirational is now worth 2 pts. Essential + recommended scoring unchanged. |

---

## Structure

- **5 essential** (C-01–C-05): claim, falsification conditions, numeric confidence, experiment list, no goalpost movement
- **3 recommended** (C-06–C-08): prior signals note, confirmation conditions, evidence-backed confidence rationale
- **5 aspirational** (C-09–C-13): experiment-to-falsification mapping, risk-ranked order **with rationale**, adversarial role gate, hard phase checklist, status-quo competing hypothesis

---

## Essential Criteria (60 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Single falsifiable claim | correctness | One declarative sentence. No hedging, no compound claims, no interrogative framing. |
| C-02 | Falsification conditions | correctness | One or more named F-NN conditions, each stating an observable outcome that would prove the claim false. Opinion-dependent conditions fail. |
| C-03 | Confidence level (0-100) | correctness | Numeric value 0-100 with brief rationale. Qualitative-only or unexplained numbers fail. |
| C-04 | Experiment list | coverage | Two or more named experiments tied to proving or falsifying the claim. Named prove sub-skills pass; "run tests" fails. |
| C-05 | No goalpost movement | behavior | Hypothesis declared before any evidence is discussed. Claim and falsification conditions must not be adjusted in response to findings already presented in the same artifact. |

## Recommended Criteria (30 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Prior signals note | behavior | Explicitly states whether prior prove artifacts exist ("None found" or lists files). Silence fails. |
| C-07 | Confirmation conditions | depth | At least one positive confirmation criterion alongside falsification conditions. |
| C-08 | Confidence rationale references prior evidence | depth | Cites at least one prior signal, trace finding, or named friction point. Pure intuition fails. |

## Aspirational Criteria (10 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Experiment-to-falsification mapping | depth | Each experiment mapped to one or more F-IDs it will test. Table or inline annotation acceptable. |
| C-10 | Risk-ranked order **with rationale** | format | Experiments ordered highest-risk-first AND a rationale column or inline explanation accompanies each rank. Rank column alone fails. |
| C-11 | Adversarial role gate (Skeptic) | structure | Named adversarial role writes explicit PASS/REWRITE verdict per falsification condition before confidence is recorded. Generic "review" note without per-condition verdicts fails. |
| C-12 | Hard phase gate with read-only constraint | structure | Checklist-style gate explicitly prohibits modifying prior-phase outputs. Observability failures logged as amendments, not retroactive edits. Ordering instruction without structural lock fails. |
| C-13 | Status-quo as competing hypothesis | depth | Status quo appears as a named falsification condition (e.g., F-00) with its own observable test. Output explains why status quo does not already satisfy the need. |

---

**Scoring**: `essential (n/5)*60 + recommended (n/3)*30 + aspirational (n/5)*10`
**Golden threshold**: all 5 essential pass AND composite >= 80.
eneric "review" note without per-condition verdicts fails. |
| C-12 | **Hard phase gate with read-only constraint** | structure | aspirational | Output uses a checklist-style phase gate that explicitly prohibits modifying prior-phase outputs. Claim and falsification conditions are locked by gate; observability failures are logged as amendments, not retroactive edits. An ordering instruction without a structural lock fails. |
| C-13 | **Status-quo as competing hypothesis** | depth | aspirational | Status quo is interrogated as a competing hypothesis (e.g., F-00) with its own observable test and confirmation conditions. Output must explain why the status quo does not already satisfy the need. A falsification list that omits status-quo inertia entirely fails. |

---

## Scoring Formula

```
essential_score     = (essential_criteria_passed / 5) * 60
recommended_score   = (recommended_criteria_passed / 3) * 30
aspirational_score  = (aspirational_criteria_passed / 5) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Modes (auto-fail regardless of score)

- Claim is adjusted after evidence is introduced in the same artifact (violates C-05)
- No numeric confidence value present (violates C-03)
- Fewer than two named experiments (violates C-04)

---

## Rubric Notes

**v1 derivation**: trace artifact `plugin-prove-hypothesis-2026-03-14.md`.
Findings SF-01, SF-02, SF-03 drove C-06, C-03, and C-07 respectively.
C-05 (no goalpost movement) was not surfaced as a finding but is the core behavioral
guarantee of the skill -- omitting it would make the rubric trivially passable.

**v2 derivation**: scorecard R1 excellence signals from `prove-hypothesis-scorecard-R1-2026-03-14.md`.
- C-10 sharpened after V-01 and V-03 both scored FAIL on C-10 despite having rank columns -- the
  missing discriminator was the rationale column; V-04 was the only variation that passed.
- C-11 (Skeptic gate) from V-04: per-condition PASS/REWRITE verdict is the strongest structural
  enforcement for C-02 -- it eliminates the failure mode where subjective conditions pass silently.
- C-12 (hard phase gate) from V-05: a read-only constraint on prior phases is the strongest
  structural enforcement for C-05 -- behavioral framing alone (V-02) is the weakest.
- C-13 (status-quo as F-00) from V-03: interrogating inertia as a competing hypothesis produces
  deeper calibration evidence for C-08 and surfaces a failure mode not caught by generic
  falsification lists.

**R2 hypothesis**: Combine V-04's Skeptic gate (C-11) with V-05's phase checklist (C-12) and
V-03's status-quo-as-competing-hypothesis framing (C-13) into a single variation to test whether
stacking the top mechanisms produces live-run quality gains or friction from complexity.
