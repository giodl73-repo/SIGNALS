---

# prove:hypothesis Rubric — v4

Three new aspirationals extracted from the R3 excellence signals section:

**C-17 — Dual-gate phase isolation** (`structure`)
> Two independent gates with non-overlapping scopes: LOCK freezes claim + conditions before any review pass; SEAL freezes the Final falsification list after consolidation and before confidence + Navigator. Each carries its own checklist. A single gate covering both events fails.
>
> *Source*: V-03 (GATE 2 + GATE 3 + SEAL three-tier architecture) and V-04 (LOCK + SEAL, two independent gates each with checklist).

**C-18 — Named structural unit for consolidation** (`structure`)
> Consolidation must appear as a named phase (PHASE 4: CONSOLIDATE) or named role section (ARCHIVIST: CONSOLIDATE) at the same heading level as other major phases/roles. An embedded subsection fails silently when omitted; a named phase or role fails visibly.
>
> *Source*: V-03 PHASE 4 and V-04 ARCHIVIST section — "A model omitting a named role or phase fails visibly. A model omitting a sub-subsection within the Skeptic section fails silently."

**C-19 — Inertia-lead status-quo framing** (`depth`)
> Template opens with a structured status-quo interrogation ("What does the team do today?") before the claim is declared. F-00's gap analysis is written with status-quo primed in context, producing organically grounded "why insufficient" rationale. Templates that introduce F-00 only during the Skeptic pass must infer the gap retrospectively.
>
> *Source*: V-05 Step 3 mechanism — "opening with 'What does the team do today?' before 'What do you believe?' means F-00's gap analysis is written with the status-quo already primed in working context."

**Scoring**: denominator shifts from `/8` to `/11`; each aspirational worth 0.91 pts; max composite stays 100.
ed** (C-06–C-08): prior signals note, confirmation conditions, evidence-backed confidence rationale
- **11 aspirational** (C-09–C-19): experiment-to-falsification mapping, risk-ranked order with rationale, adversarial role gate, hard phase checklist, status-quo competing hypothesis, complete F-ID coverage, confidence post-lock, multi-pass consolidation with verdicts, dual-gate phase isolation, named consolidation unit, inertia-lead framing

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
| C-17 | Dual-gate phase isolation | structure | Two independent gates lock distinct artifacts at different points: a DECLARE gate (LOCK or equivalent) freezes the claim and falsification conditions before any review pass begins; a CONSOLIDATE gate (SEAL or equivalent) freezes the Final falsification list after multi-pass consolidation and before confidence and Navigator population. Each gate carries its own checklist. A single gate that attempts to cover both freeze events fails. |
| C-18 | Named structural unit for consolidation | structure | Consolidation appears as a named phase (e.g., PHASE 4: CONSOLIDATE) or named role section (e.g., ARCHIVIST: CONSOLIDATE) at the same heading level as other major phases or roles in the template. A consolidation step embedded as a subsection within another phase, or within a role section that serves multiple purposes, fails. A named unit makes omission visible as a missing phase or role; a subsection makes omission silent. |
| C-19 | Inertia-lead status-quo framing | depth | The template opens with a structured status-quo interrogation step — "What does the team do today?" or equivalent — before the claim is declared. F-00's gap analysis is written with the status-quo already established in working context, not inferred retrospectively during the Skeptic pass. Templates that introduce F-00 only as a Skeptic-generated condition fail. |

---

## Scoring Formula

```
essential_score     = (essential_criteria_passed / 5) * 60
recommended_score   = (recommended_criteria_passed / 3) * 30
aspirational_score  = (aspirational_criteria_passed / 11) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.
