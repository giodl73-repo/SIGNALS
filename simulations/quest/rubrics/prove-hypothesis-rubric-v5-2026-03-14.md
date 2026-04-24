Here is the complete updated rubric:

---

# prove:hypothesis Rubric — v5

Two new aspirationals extracted from the R4 excellence signals section:

**C-20 — Dedicated F-00 validation subsection within adversarial role** (`structure`)
> The adversarial role (Skeptic, CHALLENGE, or equivalent) contains a named subsection reserved exclusively for F-00 validation, structurally separate from the F-01+ verdict list. F-00 requires different adversarial logic — testing the status quo's sufficiency rather than claim-specific falsification — and that logic must be visibly isolated. A model that applies the same verdict format to F-00 and F-01+ in a single undifferentiated list passes C-11 but fails this criterion. A model with no adversarial role fails both C-11 and C-20.
>
> *Source*: V-01 (SKEPTIC: CHALLENGE includes "F-00 validation subsection" distinct from per-condition PASS/REWRITE verdicts) and V-02 (CHALLENGE prose has "F-00 validation separate" from F-01+ annotations).

**C-21 — Gate scope labeled in section header** (`structure`)
> Each gate's section header explicitly states which artifact it freezes — e.g., "DECLARE GATE — Scope: claim + falsification conditions" or "COLLECTOR GATE — Scope: Final falsification list". Scope labeling in the header makes the gate's purpose self-documenting and auditable without reading the checklist body. A gate header that names only the gate (e.g., "LOCK GATE") without a scope annotation fails; semantically distinct names alone (LOCK vs SEAL) are insufficient. Both gates must carry scope annotations to pass.
>
> *Source*: V-02 C-17 — "DECLARE GATE (scope: claim + conditions) + COLLECTOR GATE (scope: Final list) — separate checklists, scopes named in section headers".

**Scoring**: denominator shifts from `/11` to `/13`; each aspirational worth 0.77 pts; max composite stays 100.

**Criterion summary**:
- **5 essential** (C-01–C-05): single falsifiable claim, falsification conditions, confidence, experiment list, no goalpost movement
- **3 recommended** (C-06–C-08): prior signals note, confirmation conditions, evidence-backed confidence rationale
- **13 aspirational** (C-09–C-21): experiment-to-falsification mapping, risk-ranked order with rationale, adversarial role gate, hard phase checklist, status-quo competing hypothesis, complete F-ID coverage, confidence post-lock, multi-pass consolidation with verdicts, dual-gate phase isolation, named consolidation unit, inertia-lead framing, dedicated F-00 adversarial subsection, gate scope labeled in header

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
| C-20 | Dedicated F-00 validation subsection within adversarial role | structure | The adversarial role contains a named subsection reserved exclusively for F-00 validation, structurally separate from the F-01+ verdict list. F-00 requires different adversarial logic (testing status-quo sufficiency vs testing claim-specific falsification conditions) and that logic must be visibly isolated. A model that includes F-00 in the same undifferentiated verdict list as F-01+ passes C-11 but fails this criterion. |
| C-21 | Gate scope labeled in section header | structure | Each gate's section header explicitly states which artifact it freezes — e.g., "DECLARE GATE — Scope: claim + falsification conditions" or "COLLECTOR GATE — Scope: Final falsification list". Semantically distinct gate names alone (LOCK vs SEAL) are insufficient; the header must carry a scope annotation. Both gates must carry scope annotations to pass. |

---

## Scoring Formula

```
essential_score     = (essential_criteria_passed / 5) * 60
recommended_score   = (recommended_criteria_passed / 3) * 30
aspirational_score  = (aspirational_criteria_passed / 13) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

**What changed from v4**: Two new aspirationals. C-20 splits F-00 adversarial treatment from the C-11 verdict pass — both V-01 and V-02 show the Skeptic/CHALLENGE role isolating F-00 validation as a named subsection rather than treating it as an ordinary condition in the verdict list. C-21 tightens C-17's dual-gate requirement: gate headers must name their scope explicitly rather than relying on semantically distinct names. The denominator shifts from 11 to 13; the golden threshold is unchanged.
