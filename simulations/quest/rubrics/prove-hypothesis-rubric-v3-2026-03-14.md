Reading through the scorecard carefully to identify the new excellence signals before writing the rubric.

Key observations:
- **V-04** (100/100) has three specific pass-evidence details not reflected in any v2 pass condition
- **C-04 V-04**: "Every F-ID must appear" enforced — stronger than C-09 (mapping column exists); this is full coverage, not just a column
- **C-03 V-04**: "written after LOCK gate" — confidence is structurally sequenced post-lock, preventing premature recording
- **C-13 V-04**: "F-00 in consolidated Final falsification list" — multi-pass outputs merged into one unified list with CONFIRMED verdicts before Navigator population

Three new aspirationals: **C-14** (complete F-ID coverage), **C-15** (confidence post-lock), **C-16** (multi-pass consolidation with verdicts).

Scoring update: denominator shifts from `/5` to `/8`; each aspirational worth 1.25 pts, max composite stays 100.

```markdown
# prove:hypothesis Rubric — v3

**Version**: v3 | **Date**: 2026-03-14

---

## What changed from v2

| Change | Reason |
|--------|--------|
| **C-14 added** — Complete F-ID coverage enforcement | V-04 C-04 evidence: "Every F-ID must appear" is enforced in the Navigator table. C-09 only requires the mapping column exists; C-14 requires every declared F-ID is covered by at least one experiment row. Partial coverage silently leaves conditions untested. |
| **C-15 added** — Confidence recorded post-lock | V-04 C-03 evidence: confidence value is written in a slot that appears structurally after the phase gate checklist. This prevents a confidence value from being set before the Skeptic gate clears or before the lock is confirmed. |
| **C-16 added** — Multi-pass consolidation with verdicts | V-04 C-13 evidence: when multiple passes generate falsification conditions (Pass A for status-quo, Pass B for adversarial), all outputs merge into a single Final falsification list with explicit CONFIRMED verdicts per condition before Navigator population. Without consolidation, the Navigator may reference F-IDs from one pass but silently omit the other. |
| **Scoring denominator** | Aspirational raised from `/5` to `/8`; each aspirational is now worth 1.25 pts. Essential + recommended scoring unchanged. Max composite remains 100. |

---

## Structure

- **5 essential** (C-01–C-05): claim, falsification conditions, numeric confidence, experiment list, no goalpost movement
- **3 recommended** (C-06–C-08): prior signals note, confirmation conditions, evidence-backed confidence rationale
- **8 aspirational** (C-09–C-16): experiment-to-falsification mapping, risk-ranked order with rationale, adversarial role gate, hard phase checklist, status-quo competing hypothesis, complete F-ID coverage, confidence post-lock, multi-pass consolidation

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
| C-10 | Risk-ranked order with rationale | format | Experiments ordered highest-risk-first AND a rationale column or inline explanation accompanies each rank. Rank column alone fails. |
| C-11 | Adversarial role gate (Skeptic) | structure | Named adversarial role writes explicit PASS/REWRITE verdict per falsification condition before confidence is recorded. Generic "review" note without per-condition verdicts fails. |
| C-12 | Hard phase gate with read-only constraint | structure | Checklist-style gate explicitly prohibits modifying prior-phase outputs. Observability failures logged as amendments, not retroactive edits. Ordering instruction without structural lock fails. |
| C-13 | Status-quo as competing hypothesis | depth | Status quo appears as a named falsification condition (e.g., F-00) with its own observable test. Output explains why status quo does not already satisfy the need. |
| C-14 | Complete F-ID coverage in Navigator | coverage | Every declared F-NN condition appears in at least one experiment row in the Navigator table. An enforcement note or structural rule makes partial coverage explicit-fail. A mapping column (C-09) that leaves any F-ID uncovered fails this criterion. |
| C-15 | Confidence recorded post-lock | structure | The confidence slot is positioned structurally after the phase gate checklist, preventing the numeric value from being written before the Skeptic gate clears and the lock is confirmed. Confidence that precedes the gate in document order fails. |
| C-16 | Multi-pass consolidation with verdicts | structure | When multiple passes generate falsification conditions (e.g., Pass A for status-quo, Pass B for adversarial), all conditions are merged into a single enumerated Final falsification list with explicit CONFIRMED verdicts per condition before the Navigator table is populated. A template that populates the Navigator from per-pass outputs without a consolidation step fails. |

---

## Scoring Formula

```
essential_score     = (essential_criteria_passed / 5) * 60
recommended_score   = (recommended_criteria_passed / 3) * 30
aspirational_score  = (aspirational_criteria_passed / 8) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.
```
