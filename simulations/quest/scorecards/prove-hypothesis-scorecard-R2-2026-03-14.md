## prove-hypothesis R2 — Scorecard

### Evaluation Framework

**Scoring**: `(essential/5)*60 + (recommended/3)*30 + (aspirational/5)*10`
**Golden threshold**: all 5 essential pass AND composite ≥ 80

---

## V-01: Adversarial Scope

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Single falsifiable claim | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" — structural slot enforces form |
| C-02 | Falsification conditions | PASS | F-00 from Pass A + F-01/F-02 from Pass B, all with "Observable test" fields |
| C-03 | Confidence level 0-100 | PASS | "Value: [N]/100" with rationale requiring two named elements |
| C-04 | Experiment list | PASS | Navigator table requires 2+ rows with named prove sub-skills |
| C-05 | No goalpost movement | PASS | "Do not adjust the Claimant's claim or falsification conditions after the Skeptic gate" + DECLARE section forbids evidence references |
| C-06 | Prior signals note | PASS | "Prior signals check: List files found, or write 'None -- starting fresh.'" |
| C-07 | Confirmation conditions | PASS | CF-01 table required in Skeptic section |
| C-08 | Confidence cites prior evidence | PASS | Rationale requires "prior signal, trace finding, or friction point"; fallback explicitly names Pass A gap as anchor |
| C-09 | Exp-to-falsification mapping | PASS | "Falsification conditions tested" column pre-printed in Navigator table |
| C-10 | Risk-ranked with rationale | PASS | "Why this risk rank" column alongside Rank column |
| C-11 | Adversarial role gate (Skeptic) | PASS | Pass B: explicit PASS/REWRITE per-condition table; "All candidates must reach PASS before continuing" |
| C-12 | Hard phase gate, read-only | **FAIL** | No checklist gate. "Do not adjust" is an instruction, not a structural lock; no amendment note slot |
| C-13 | Status-quo as F-00 with observable test | PASS | Pass A produces F-00 with Why insufficient + Observable test; pre-printed in Final falsification list |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 4/5 → 8
**Composite: 98 | Golden: YES**

---

## V-02: Hard Gate Formalism

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Single falsifiable claim | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" |
| C-02 | Falsification conditions | PASS | Candidates cleared through Skeptic PASS verdicts, observable-test enforced |
| C-03 | Confidence level 0-100 | PASS | "Value: [N]/100" with "Do not omit the prior-evidence statement" |
| C-04 | Experiment list | PASS | Navigator table with prove sub-skills, F-ID coverage requirement |
| C-05 | No goalpost movement | PASS | LOCK RULE at header + 5-item GATE: LOCK checklist + "LOCKED... cannot be modified" + read-only annotation on Navigator |
| C-06 | Prior signals note | PASS | "Prior signals check" with list-or-None requirement |
| C-07 | Confirmation conditions | PASS | CF-01 table in Skeptic section |
| C-08 | Confidence cites prior evidence | PASS | "Reference at least one specific prior signal... Do not omit the prior-evidence statement" |
| C-09 | Exp-to-falsification mapping | PASS | "Falsification conditions tested" column in Navigator table |
| C-10 | Risk-ranked with rationale | PASS | "Why this risk rank" column + "rank 1 = highest probability" |
| C-11 | Adversarial role gate (Skeptic) | PASS | Explicit per-condition PASS/REWRITE table; "All must reach PASS before the gate below" |
| C-12 | Hard phase gate, read-only | PASS | 5-item GATE: LOCK checklist + "LOCKED. claim and falsification conditions above cannot be modified." + "Amendment notes (post-lock)" slot |
| C-13 | Status-quo as F-00 with observable test | **FAIL** | No status-quo interrogation. No Pass A, no gap analysis, no F-00 pre-printed |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 4/5 → 8
**Composite: 98 | Golden: YES**

---

## V-03: Status-Quo Depth

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Single falsifiable claim | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" after STATUS-QUO BASELINE |
| C-02 | Falsification conditions | PASS | F-00 pre-printed + F-01/F-02 domain conditions, each with "Observable test" field |
| C-03 | Confidence level 0-100 | PASS | "Value: [N]/100" with two-element rationale structure; gap analysis always provides anchor |
| C-04 | Experiment list | PASS | Experiments table with prove sub-skills and F-ID coverage |
| C-05 | No goalpost movement | PASS | "Declare the hypothesis after the status-quo baseline but before any domain evidence" — ordering enforces declaration-before-evidence |
| C-06 | Prior signals note | PASS | "SETUP: PRIOR SIGNALS" section with list-or-None requirement |
| C-07 | Confirmation conditions | PASS | CF-01 table required |
| C-08 | Confidence cites prior evidence | PASS | Rationale requires F-00 gap reference; "The gap analysis always provides an anchor -- silence on the anchor fails" |
| C-09 | Exp-to-falsification mapping | PASS | "Falsification conditions tested" column in experiments table |
| C-10 | Risk-ranked with rationale | PASS | "Why this risk rank" column + "rank 1 = highest probability" |
| C-11 | Adversarial role gate (Skeptic) | **FAIL** | No Skeptic role. No per-condition PASS/REWRITE verdicts. Falsification conditions are declared without adversarial challenge |
| C-12 | Hard phase gate, read-only | **FAIL** | No checklist gate. Ordering instruction only; no LOCK annotation, no amendment note slot |
| C-13 | Status-quo as F-00 with observable test | PASS | F-00 pre-printed with three-part gap analysis block (delivers / cannot deliver / why matters) + "Insufficient because" field + Observable test — deepest C-13 coverage of all variations |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 3/5 → 6
**Composite: 96 | Golden: YES**

---

## V-04: Adversarial Scope + Hard Gate

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Single falsifiable claim | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" |
| C-02 | Falsification conditions | PASS | Final falsification list: F-00 (Pass A), F-01/F-02 (Pass B), each with observable tests |
| C-03 | Confidence level 0-100 | PASS | "Value: [N]/100" with two-element rationale; written after LOCK gate |
| C-04 | Experiment list | PASS | Navigator table with prove sub-skills; "Every F-ID must appear" enforced |
| C-05 | No goalpost movement | PASS | LOCK RULE at header + 5-item GATE: LOCK checklist + "LOCKED. Claim and falsification conditions above are now read-only." |
| C-06 | Prior signals note | PASS | "Prior signals check" with list-or-None requirement |
| C-07 | Confirmation conditions | PASS | CF-01 table in Skeptic section |
| C-08 | Confidence cites prior evidence | PASS | Rationale requires "(2) What prior signal, trace finding, or friction point anchors the numeric value?" |
| C-09 | Exp-to-falsification mapping | PASS | "Falsification conditions tested" column in Navigator table |
| C-10 | Risk-ranked with rationale | PASS | "Why this risk rank" column + ranked "by falsification risk" |
| C-11 | Adversarial role gate (Skeptic) | PASS | Pass B: explicit PASS/REWRITE table; "All must reach PASS before the gate" |
| C-12 | Hard phase gate, read-only | PASS | 5-item GATE: LOCK checklist + "LOCKED" annotation + "Amendment notes (post-lock)" field |
| C-13 | Status-quo as F-00 with observable test | PASS | Pass A: F-00 CONFIRMED verdict, Why insufficient, Observable test, F-00 in consolidated Final falsification list |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 5/5 → 10
**Composite: 100 | Golden: YES**

---

## V-05: Full Lifecycle + Skeptic + Status-Quo Competing Hypothesis

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Single falsifiable claim | PASS | "Claim: [One sentence. Use 'is' or 'will'. No hedging.]" in PHASE 2 DECLARE |
| C-02 | Falsification conditions | PASS | F-01/F-02 in PHASE 2 + F-00 declared in PHASE 3, all observable |
| C-03 | Confidence level 0-100 | PASS | "[N]/100" with "Cite at least one anchor" requirement in PHASE 2 |
| C-04 | Experiment list | PASS | PHASE 4 PLAN table with prove sub-skills; "Every falsification condition must be covered" |
| C-05 | No goalpost movement | PASS | GATE 2 checklist (5 items including "No evidence from later phases referenced here") + "LOCKED. Phases 3 and 4 may not modify claim or falsification conditions." Strongest enforcement of all 5 variations |
| C-06 | Prior signals note | PASS | PHASE 1 SETUP: "List files found with one-line summaries. Write 'None -- starting fresh' if empty." |
| C-07 | Confirmation conditions | PASS | "The claim is confirmed if ANY of: CF-01" in PHASE 2 |
| C-08 | Confidence cites prior evidence | PASS | "Cite at least one anchor from PHASE 1 prior signals or the status-quo baseline" |
| C-09 | Exp-to-falsification mapping | PASS | "Falsification conditions tested" column in PHASE 4 table |
| C-10 | Risk-ranked with rationale | PASS | "Risk rationale" column + "Rank 1 = highest probability of falsifying" |
| C-11 | Adversarial role gate (Skeptic) | PASS | Named SKEPTIC in PHASE 3 with per-condition verdict table; "All F-IDs must receive a verdict" |
| C-12 | Hard phase gate, read-only | PASS | GATE 2 (5-item checklist) + LOCKED annotation + "Observability failures: log as amendment notes, do not edit" + GATE 3 enforces read-only access for PHASE 4 |
| C-13 | Status-quo as F-00 with observable test | PASS | PHASE 3: dedicated "SKEPTIC: Status-Quo Competing Hypothesis" block, explicit INSUFFICIENT/SUFFICIENT verdict, Why insufficient, F-00 with observable test |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 5/5 → 10
**Composite: 100 | Golden: YES**

---

## Rankings

| Rank | Variation | Score | Golden | Aspirationals passed |
|------|-----------|-------|--------|----------------------|
| 1 (tied) | V-04 | 100 | YES | C-09, C-10, C-11, C-12, C-13 |
| 1 (tied) | V-05 | 100 | YES | C-09, C-10, C-11, C-12, C-13 |
| 3 (tied) | V-01 | 98 | YES | C-09, C-10, C-11, C-13 |
| 3 (tied) | V-02 | 98 | YES | C-09, C-10, C-11, C-12 |
| 5 | V-03 | 96 | YES | C-09, C-10, C-13 |

---

## Excellence Signals (from V-04 and V-05)

**1. Amendment note slot as structural pressure release**
V-04 and V-05 include a named "Amendment notes (post-lock)" field. Without it, the model has no safe outlet when it discovers a post-lock observability problem — it either silently edits the locked section (violating C-05) or fails to record the problem. The slot makes the correct behavior cheaper than the incorrect behavior.

**2. Two-pass Skeptic with status-quo first**
Pass A (status-quo verdict) primes the adversarial posture before Pass B (per-condition observability). The ordering is load-bearing: establishing that doing nothing is insufficient sharpens the criteria for what counts as a falsifiable condition in Pass B. Single-pass Skeptic (V-02) skips this priming.

**3. Confidence placed explicitly after the LOCK gate**
V-04 labels the confidence section "Written after LOCK gate. Lock is in effect." This separates locked structural elements (claim, conditions) from unlocked assessments (confidence value). It closes a backdoor: a model cannot use the confidence rationale to reframe the claim while appearing to comply with the lock.

**4. Final falsification list consolidation (V-04)**
V-04 consolidates F-00 (from Pass A) and F-01/F-02 (from Pass B) into a single "Final falsification list" table before Navigator begins. This eliminates navigation ambiguity where F-00 lives in one section and domain conditions live in another. Navigator has one authoritative reference.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["amendment-note-slot-as-pressure-release", "two-pass-skeptic-status-quo-first", "confidence-explicitly-post-lock", "final-falsification-list-consolidation"]}
```
