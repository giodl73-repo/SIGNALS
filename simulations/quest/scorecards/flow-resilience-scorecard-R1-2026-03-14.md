## Round 1 Scorecard — flow-resilience

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 Combined | 5/5 | 3/3 | 0/2 | **90** | YES |
| 2 | V-01 Table format | 5/5 | 2.5/3 | 0/2 | **85** | YES |
| 3 | V-03 Amend loop | 5/5 | 2/3 | 0/2 | **80** | YES |
| 4 | V-02 Role sequence | 4.5/5 | 2/3 | 0/2 | **74** | NO |
| 5 | V-04 Conversational | 4/5 | 1/3 | 0/2 | **58** | NO |

**3 of 5 variations reach golden threshold.**

**Top discriminators:**

- **C-07 (Recovery path specificity)** is the recommended-tier splitter. V-05 names the actor chain in the field label (`client → server → operator → user`); V-01 asks for actors without naming them (PARTIAL); V-02/V-03 name actors in prose instruction (PASS but weaker). The delta is: does the template name the classes, or ask the model to figure them out?

- **C-06 (Severity + blast radius)** is binary — either pre-printed in the template (V-01, V-05) or absent entirely (V-02, V-04).

- **C-09 / C-10 (Chaos + Observability)** are 0 across all variations — no Round 1 axis targets them. These 10 points are available in Round 2.

**New patterns from V-05:**

1. Named actor chain in Recovery field template — model fills rather than designs
2. Constrained-choice strategy vocabulary (`last-write-wins | merge | manual-reconcile | reject-stale`) — eliminates free-text description failure
3. "do not omit or merge" section label — blocks the most common gap-section failure mode by name

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Named actor chain in Recovery field template (client → server → operator → user) produces consistent actor attribution — model fills rather than designs", "Constrained-choice conflict resolution vocabulary (last-write-wins | merge | manual-reconcile | reject-stale) eliminates free-text strategy description failure mode", "do not omit or merge section label anticipates the merge failure mode by name, blocking it structurally rather than relying on a section header alone"]}
```


```
composite = (5/5 * 60) + (2.5/3 * 30) + (0/2 * 10)
          = 60 + 25 + 0
          = 85
```

**Score: 85 / 100 — GOLDEN** (all essential pass, composite >= 80)

---

### V-02: Role Sequence (Ops SME leads, Dev validates)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Three scenarios: "Full network loss", "Dependent service unavailable", "Post-reconnect conflict" |
| C-02 | Four-field structure per scenario | PARTIAL | Developer must provide "four-field technical trace" but no table enforcement; instruction-based format only — model may produce labeled prose |
| C-03 | Gap identification (3 types) | PASS | Phase 3 requires all three types with dual-role (SME + Developer) attribution |
| C-04 | Distributed systems accuracy | PASS | Developer validates/corrects SME account against technical reality — explicit accuracy-checking role |
| C-05 | Commerce domain grounding | PASS | SME role anchors to floor (cashier, shift manager, customer); scenarios mention pricing service, loyalty, receipt tape, reconciliation screen |
| C-06 | Severity + blast radius | FAIL | No severity or blast-radius annotation requirement anywhere in the prompt |
| C-07 | Recovery path specificity | PASS | Phase 2: "Recovery: exact sequence with actor labels (client / server / operator / user)" — explicit actor naming required |
| C-08 | Conflict resolution strategy | PASS | Phase 2: "Conflict resolution judgment for Scenario 3: what strategy is in use, and is it adequate given the data type?" |
| C-09 | Chaos engineering test cases | FAIL | No chaos engineering requirement |
| C-10 | Observability hooks | FAIL | No observability requirement |

**Essential**: 4.5/5 | **Recommended**: 2/3 | **Aspirational**: 0/2

```
composite = (4.5/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 54 + 20 + 0
          = 74
```

**Score: 74 / 100 — NOT GOLDEN** (C-02 partial, composite below 80 threshold)

C-06 is the structural gap: the ops-first hypothesis produces rich domain grounding (C-05) and the
developer phase ensures accuracy (C-04), but severity classification is never required. The two-voice
format also increases output length, which may dilute structural compliance in practice.

---

### V-03: Lifecycle Emphasis (Amend loop)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Phase 1 defines all three: connectivity loss, partial failure, concurrent writes across partition |
| C-02 | Four-field structure per scenario | PASS | Phase 2 requires four-field snapshot with actor labels explicitly named in the template text |
| C-03 | Gap identification (3 types) | PASS | Phase 3 requires three labeled finding types with specific sub-structure (record, inconsistency, detectability, severity rating for DCV) |
| C-04 | Distributed systems accuracy | PASS | Hypothesis-first approach with [DELTA] tags for divergence — verification mechanism that prevents post-hoc rationalization |
| C-05 | Commerce domain grounding | PASS | Domain expert role + cashier/customer/operator terminology throughout; Phase 3 explicitly says "cashier or customer impact" |
| C-06 | Severity + blast radius | PARTIAL | Data violation severity rated in Phase 3 (silent / detectable / surfaced immediately) but no per-scenario severity + blast-radius annotation; blast radius not covered at all |
| C-07 | Recovery path specificity | PASS | Phase 2: "actor labels (client initiates retry / server detects conflict / operator approves resolution / user confirms re-submission)" — actor chain named inline |
| C-08 | Conflict resolution strategy | PARTIAL | Amend loop forces resolution proposals but Phase 2 scenario setup does not require naming a strategy type from a constrained list; conflict strategy emerges through amendment, not scenario simulation |
| C-09 | Chaos engineering test cases | FAIL | No chaos engineering requirement |
| C-10 | Observability hooks | FAIL | No observability requirement |

**Essential**: 5/5 | **Recommended**: 2/3 | **Aspirational**: 0/2

```
composite = (5/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 60 + 20 + 0
          = 80
```

**Score: 80 / 100 — GOLDEN** (all essential pass, composite = 80, at threshold)

Note: V-03's Amend loop is the strongest mechanism for C-07 recovery specificity — re-simulation
forces recovery paths to be verifiable, not aspirational. C-08's PARTIAL is a timing gap: conflict
resolution strategy emerges from the Amend phase rather than being named in the scenario, arriving
too late and at insufficient precision for the criterion to fully pass.

---

### V-04: Conversational Walkthrough

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Three situations: network down, service down, concurrent writes — all three classes |
| C-02 | Four-field structure per scenario | PARTIAL | Conversational questions probe toward the four fields but do not enforce structure; "walk me through" framing produces narrative that blends fields |
| C-03 | Gap identification (3 types) | PASS | Three explicit lists at end with strong specificity demands: "tell me what the cashier actually did instead", "tell me whether the system knows it's wrong" |
| C-04 | Distributed systems accuracy | PARTIAL | Conversational register reduces technical precision guardrails; storytelling framing encourages fluency over correctness; no verification mechanism |
| C-05 | Commerce domain grounding | PASS | Richest commerce vocabulary of all variations: cashier, receipt tape, loyalty, POS cached version, Store A / Store B cross-store refund, payment gateway |
| C-06 | Severity + blast radius | FAIL | Situation 3 asks "What is the blast radius?" conversationally but does not require annotation; Situations 1 and 2 have no severity/blast-radius requirement |
| C-07 | Recovery path specificity | PARTIAL | Asks "What happens? Does someone have to do something?" but no actor-labeled step requirement |
| C-08 | Conflict resolution strategy | PARTIAL | Situation 3 asks "what does the conflict resolution strategy do — and is that the right call?" — well-framed but conversational; model may not select from constrained list or provide crisp adequacy judgment |
| C-09 | Chaos engineering test cases | FAIL | No chaos engineering requirement |
| C-10 | Observability hooks | FAIL | No observability requirement |

**Essential**: 4/5 | **Recommended**: 1/3 | **Aspirational**: 0/2

```
composite = (4/5 * 60) + (1/3 * 30) + (0/2 * 10)
          = 48 + 10 + 0
          = 58
```

**Score: 58 / 100 — NOT GOLDEN**

V-04's commerce grounding (C-05) is the strongest of any variation — the narrative framing surfaces
operational detail that formal prompts suppress. The gap section at the end works precisely because
it switches from conversational to imperative list mode. The structural weakness across C-02, C-04,
C-06, C-07, C-08 is the cost of the conversational axis.

---

### V-05: Combined (Table + Ops-first + Mandatory gap section)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Scenario coverage (3 classes) | PASS | Three sections: "Offline / Network Loss", "Partial Service Failure", "Eventual Consistency Conflict" — all three classes |
| C-02 | Four-field structure per scenario | PASS | Developer four-field trace table pre-printed per section; Recovery field template shows "[actor-labeled steps: client → server → operator → user]" — model fills, does not design |
| C-03 | Gap identification (3 types) | PASS | Section 4 labeled "mandatory — do not omit or merge with scenarios"; numbered IDs (GAP-NN, DCV-NN, MRF-NN) prevent type blending |
| C-04 | Distributed systems accuracy | PASS | Developer role explicitly validates/corrects SME account; two-pass structure makes the Developer responsible for technical accuracy |
| C-05 | Commerce domain grounding | PASS | SME role anchors to floor operations; Section 2 instructs: "Choose the dependency most critical to {topic}'s commerce operations (pricing service, loyalty service, inventory service, payment gateway)" |
| C-06 | Severity + blast radius | PASS | Classification block pre-printed per section: `Severity: [degraded | impaired | down] | Blast radius: [scope and population]` — required for all three scenarios |
| C-07 | Recovery path specificity | PASS | Recovery field template names the actor chain: "[actor-labeled steps: client → server → operator → user]" — model cannot omit what is already in the field label |
| C-08 | Conflict resolution strategy | PASS | Section 3 "Conflict resolution" subsection requires naming strategy from constrained list and assessing adequacy: "If not adequate, name the failure mode." |
| C-09 | Chaos engineering test cases | FAIL | No chaos engineering requirement |
| C-10 | Observability hooks | FAIL | No observability requirement |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 0/2

```
composite = (5/5 * 60) + (3/3 * 30) + (0/2 * 10)
          = 60 + 30 + 0
          = 90
```

**Score: 90 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-05 Combined | 5/5 | 3/3 | 0/2 | **90** | YES |
| 2 | V-01 Table format | 5/5 | 2.5/3 | 0/2 | **85** | YES |
| 3 | V-03 Amend loop | 5/5 | 2/3 | 0/2 | **80** | YES |
| 4 | V-02 Role sequence | 4.5/5 | 2/3 | 0/2 | **74** | NO |
| 5 | V-04 Conversational | 4/5 | 1/3 | 0/2 | **58** | NO |

---

## Excellence Signals — Round 1

### E-1: Named actor chain in Recovery field template

V-05's Recovery field includes the actor chain inline: "[actor-labeled steps: client → server →
operator → user]". This is structurally stronger than V-01's "Step-by-step: who acts, what
happens, in what order?" (which asks for actors but leaves their names to the model) and V-03's
inline example in prose (which the model may paraphrase). When the actor chain is part of the
template label, the model fills it rather than designs it — producing consistent actor attribution
with zero extra instruction pressure.

### E-2: Constrained-choice conflict resolution vocabulary

V-05 and V-01 both embed the strategy list directly in the prompt:
`last-write-wins | merge | manual-reconcile | reject-stale`. This forces selection from a known
taxonomy rather than free-text description. V-02 and V-03 ask for the strategy but do not
constrain the vocabulary, allowing a model to invent terminology or describe a strategy without
naming it. Constrained choice eliminates this failure mode entirely.

### E-3: "Do not omit or merge" label on Section 4

V-05's Section 4 carries an explicit prohibition: "mandatory — do not omit or merge with
scenarios." This label anticipates the most common failure mode (merging gap findings into the
scenario prose) and blocks it by name. V-01's Step 4 and V-03's Phase 3 both require gap sections
but do not defend against the merge failure. The label does work that a section header alone
cannot do.

---

## Criterion Weakness Analysis

### C-07 is the recommended-tier discriminator

C-06 (severity/blast-radius) is binary: either pre-printed in the template (V-01, V-05) or absent
(V-02, V-04). C-08 (conflict resolution) follows similarly. C-07 has a gradient: V-01 PARTIAL
(asks for actors without naming them), V-03 PASS (actor chain in prose template), V-05 PASS
(actor chain as field label). The delta between PARTIAL and PASS on C-07 is: does the prompt name
the actor classes, or only ask the model to identify actors? Naming produces consistent labeling;
asking produces variable output.

### C-09 and C-10 are unreachable in Round 1

No variation attempts chaos engineering or observability hooks. These criteria require a dedicated
axis that none of the Round 1 hypotheses explored. Reaching C-09 requires an explicit chaos
scenario template (injection / expected behavior / pass-fail signal). Reaching C-10 requires a
per-gap observability field (metric or alert tied to a named gap). A Round 2 variation targeting
both could push the ceiling from 90 to 100.

---

## Round 1 Findings

### F-01: V-05 wins by capturing V-02's commerce grounding without losing V-01's structure

The ops-first SME walkthrough in V-05 delivers the commerce domain richness of V-02 while the
pre-printed table structure delivers the four-field enforcement of V-01. The combination is
additive: neither axis sacrifices the other.

### F-02: Amend loop (V-03) is the strongest C-07 mechanism but weakest C-08 placement

Re-simulation after findings forces recovery paths to be verifiable. However, conflict resolution
strategy emerges from the Amend phase (as a proposed fix) rather than being named during scenario
simulation (as a strategy in use). This timing gap means C-08 arrives late and less precisely.

### F-03: Conversational register (V-04) produces uniquely rich C-05 signal

V-04 surfaces cashier workarounds, escalation paths, and operational edge cases that formal formats
suppress. The qualitative depth is real but rubric-unmeasurable. If a future criterion captures
"operational workaround specificity" or "cashier-impact narrative depth", V-04's approach would
score well. The gap section at the end (three explicit imperative lists) works because it switches
registers mid-prompt.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- 90/100 — highest composite of any Round 1 variation
- All five essential criteria pass
- All three recommended criteria pass
- Three structural blocking mechanisms working in concert: table blocks prose escape,
  ops-first blocks domain-agnostic analysis, mandatory Section 4 with numbered IDs blocks
  gap-type blending

**Round 2 focus**: C-09 (chaos engineering) and C-10 (observability hooks) are both at 0 and
account for 10 points combined. A targeted variation adding a chaos scenario template block and
a per-gap observability field to V-05 would push the ceiling to 100.

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Named actor chain in Recovery field template (client → server → operator → user) produces consistent actor attribution — model fills rather than designs", "Constrained-choice conflict resolution vocabulary (last-write-wins | merge | manual-reconcile | reject-stale) eliminates free-text strategy description failure mode", "do not omit or merge section label anticipates the merge failure mode by name, blocking it structurally rather than relying on a section header alone"]}
```
