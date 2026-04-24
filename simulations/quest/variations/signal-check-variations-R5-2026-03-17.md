Done. Here's the R5 output:

---

**Variations written** to `signal-check-variations-R5-2026-03-17.md` (1546 lines) and **scorecard written** to `signal-check-scorecard-R5-2026-03-17.md`.

---

## R5 Summary

**Axis**: C-46 — convergence step self-declaration of C-43 compliance.

**What changed in rubric v5**: C-46 requires every multi-input consuming step to carry an inline self-declaration that it satisfies C-43. The R4 V-04 baseline (37/37) had brackets at STEP 3, STEP C per-dim, and STEP D — but **not STEP E**. That gap is the R5 axis.

**Axis matrix**:

| V | Single/Combined | C-46 Form | STEP E | C-46 verdict | Expected |
|---|---|---|---|---|---|
| V-01 | Single — partial coverage | Form A | **absent** | FAIL | 37/38 |
| V-02 | Single — absent pipeline-wide | Absent | absent | FAIL | 37/38 |
| V-03 | Single — Form B (per-annotation) | Form B | PASS | PASS | 38/38 |
| V-04 | Combined — Form A full coverage | Form A + STEP E bracket | PASS | PASS | 38/38 |
| V-05 | Combined — Form B alt phrasing | "self-contained" variant | PASS | PASS | 38/38 |

**Key finding**: C-46 is all-or-nothing — V-01 (STEP E missing only) and V-02 (nothing anywhere) score identically (37/38). The STEP E bracket is not optional even when all upstream steps carry self-declarations.

**New pattern**: Convergence step self-declaration as local-verifiability closure. Symmetric with C-26 at consumers and C-39 at the terminal producer — C-46 completes the three-node enforcement symmetry so every node in the pipeline makes its own obligation locally visible.
ed group note? (V-03 vs V-04)
4. Do V-04 and V-05 both score 38/38, confirming that Forms A and B are equivalent for C-46? (V-04 vs V-05)
5. Does the per-annotation form (V-03/V-05) place any meaningful enforcement overhead on production, or is it structurally equivalent at zero overhead? (V-03 vs V-05)

---

## V-01 -- C-46 Partial Coverage: STEP E Self-Declaration Absent (FAIL by design)

**Axes**: C-46 Form A at STEP 3 (PASS), STEP C per-dim (PASS), STEP D (PASS) -- but absent at STEP E (FAIL by design). All other criteria (C-43, C-44, C-45) carry over from R4 V-04 at PASS.
**Hypothesis**: C-46 requires a self-declaration at every multi-input consuming step in the pipeline. Partial coverage -- present at STEP 3, STEP C, and STEP D but absent at STEP E -- is insufficient. V-01 confirms that the bracket at STEP E is not optional even when STEP E's two annotations are structurally independent and independently parseable. The absence of a C-46 bracket at STEP E should register as a C-46 FAIL despite full coverage at all upstream convergence steps.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Pipeline-wide: each per-input annotation must be parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation -- without
reading adjacent annotations or relying on a shared header for scope.
Grouping is a symptom of failing this standard, not the standard itself.
[C-45 PASS: meta-rule states parseable-completeness-in-isolation as the positive standard]

| Named Output                                 | Produced by              | Consumed by                                                                                    |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                                  |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                                           |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                                          |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                                          |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name)              |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                                       |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                                       |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                                       |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                                     |

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim and closes with:
   Inertia case: [BUILT / PARTIAL / OPEN + reason] -> STEP E (forward arrow).
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all five named inputs by label -- one independently parseable
   per-input annotation each (pipeline-wide standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions:
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
12. PART 2 STEP E opens with two independent per-input prohibitions -- C-46 FAIL by design
    (no inline self-declaration at STEP E; single-axis C-46 coverage isolation):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement independently parseable.
    [C-46 FAIL: STEP E has no C-43 self-declaration; partial coverage test]

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|
(Inertia Relevant: does this artifact speak to the comparison between {{topic}} and
the status-quo alternative -- competitors, benchmarks, usage data, mechanism evidence?
Mark yes / no.)

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Inertia-relevant artifact count (from column above):
  1 or more -> staleness threshold = 14 days
  0         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

Analysis order: CAUSAL GAP -> SEQUENCE -> COHERENCE -> STALENESS.
For each: cite artifacts by name, severity internally (not a gate), coaching
observation, one concrete next action if flagged.

### CAUSAL GAP

Inertia-relevant pool: [list every artifact tagged yes in Step 1].
Evaluate mechanism evidence from this pool only.

Inertia anchor: [restate Step 0 in one phrase].

If pool is EMPTY:
  Mechanism verdict is absent by default. State explicitly. Name what artifact types
  would populate the pool. Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence for the pathway from {{topic}} to its claimed outcome, specifically
  better than the status-quo alternative? State: present / partial / absent.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read ordering through mechanism lens: did inertia-relevant pool artifacts appear in
the discovery phase, or did the team specify before mechanism evidence existed?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before earliest spec artifact /
  NO -- mechanism evidence was present when team committed to spec]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-43 PASS: three independent per-input annotations at this 3-input consuming step]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.
-> PART 2 STEP C per-dim: Required input -- do not re-derive: Root pattern.
-> PART 2 STEP D: Required input -- do not re-derive: Root pattern. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence present, status-quo comparison addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]
-> STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after STEP D and finalized in STEP E]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input consuming step]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input consuming step]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input consuming step]
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]"
    / STALENESS is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
[C-43 PASS: five independent per-input annotations at this 5-input convergence step;
 each annotation is independently parseable without proximity dependency]

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
If any OPEN: name dimension(s) and reason for divergence.

Confirmed readiness: [READY -- all drift CLOSED, mechanism evidence sufficient /
  CONDITIONALLY READY -- [list conditions]; one more loop recommended on [dimension] /
  NOT READY -- [dimension] OPEN; mechanism or timing gap must be addressed]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A
Each annotation is a complete standalone statement independently parseable.
[C-46 FAIL: STEP E has no C-43 self-declaration; partial coverage test]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]
```

---

## V-02 -- C-46 Absent Pipeline-Wide (No Self-Declarations at Any Convergence Step)

**Axes**: C-46 absent at all convergence steps (STEP 3, STEP C per-dim, STEP D, STEP E) -- FAIL by design. All other criteria (C-43, C-44, C-45) carry over from R4 V-04 at PASS. The annotations at each convergence step remain structurally independent and independently parseable; only the C-46 self-declaration brackets are omitted pipeline-wide.
**Hypothesis**: C-46 requires an explicit inline self-declaration at every multi-input consuming step. Structural independence of annotations alone -- annotations that are independently parseable in isolation but carry no C-46 bracket -- does not satisfy C-46. V-02 tests whether a rubric evaluator scores C-46 FAIL when annotations are structurally sound but the self-declaration note is absent at all convergence steps. The expected result is approximately 37/38 (one C-46 failure spanning the pipeline).

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Pipeline-wide: each per-input annotation must be parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation -- without
reading adjacent annotations or relying on a shared header for scope.
Grouping is a symptom of failing this standard, not the standard itself.
[C-45 PASS: meta-rule states parseable-completeness-in-isolation as the positive standard]

| Named Output                                 | Produced by              | Consumed by                                                                                    |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                                  |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                                           |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                                          |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                                          |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name)              |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                                       |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                                       |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                                       |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                                     |

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim and closes with:
   Inertia case: [BUILT / PARTIAL / OPEN + reason] -> STEP E (forward arrow).
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all five named inputs by label -- one independently parseable
   per-input annotation each (pipeline-wide standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions:
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
12. PART 2 STEP E opens with two independent per-input prohibitions -- no C-46 self-declarations
    at any convergence step in this variation (C-46 absent by design pipeline-wide):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement independently parseable.
    [C-46 FAIL: no inline self-declarations at any convergence step; C-46 absent test]

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|
(Inertia Relevant: does this artifact speak to the comparison between {{topic}} and
the status-quo alternative -- competitors, benchmarks, usage data, mechanism evidence?
Mark yes / no.)

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Inertia-relevant artifact count (from column above):
  1 or more -> staleness threshold = 14 days
  0         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

Analysis order: CAUSAL GAP -> SEQUENCE -> COHERENCE -> STALENESS.
For each: cite artifacts by name, severity internally (not a gate), coaching
observation, one concrete next action if flagged.

### CAUSAL GAP

Inertia-relevant pool: [list every artifact tagged yes in Step 1].
Evaluate mechanism evidence from this pool only.

Inertia anchor: [restate Step 0 in one phrase].

If pool is EMPTY:
  Mechanism verdict is absent by default. State explicitly. Name what artifact types
  would populate the pool. Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence for the pathway from {{topic}} to its claimed outcome, specifically
  better than the status-quo alternative? State: present / partial / absent.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read ordering through mechanism lens: did inertia-relevant pool artifacts appear in
the discovery phase, or did the team specify before mechanism evidence existed?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before earliest spec artifact /
  NO -- mechanism evidence was present when team committed to spec]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-46 FAIL: no self-declaration at this convergence step; C-46 absent test]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.
-> PART 2 STEP C per-dim: Required input -- do not re-derive: Root pattern.
-> PART 2 STEP D: Required input -- do not re-derive: Root pattern. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence present, status-quo comparison addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]
-> STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after STEP D and finalized in STEP E]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-46 FAIL: no self-declaration; C-46 absent test]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-46 FAIL: no self-declaration; C-46 absent test]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-46 FAIL: no self-declaration; C-46 absent test]
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]"
    / STALENESS is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
[C-46 FAIL: no self-declaration at STEP D; C-46 absent test]

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
If any OPEN: name dimension(s) and reason for divergence.

Confirmed readiness: [READY -- all drift CLOSED, mechanism evidence sufficient /
  CONDITIONALLY READY -- [list conditions]; one more loop recommended on [dimension] /
  NOT READY -- [dimension] OPEN; mechanism or timing gap must be addressed]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A
Each annotation is a complete standalone statement independently parseable.
[C-46 FAIL: no inline self-declarations at any convergence step; C-46 absent test]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]
```

---

## V-03 -- C-46 Form B: Per-Annotation Isolation Comments at All Convergence Steps (PASS)

**Axes**: C-46 Form B at all convergence steps (STEP 3, STEP C per-dim, STEP D, STEP E) -- PASS. Form B uses per-annotation isolation comments (`-- (annotation N of M: parseable without other annotations; isolation confirmed)`) rather than a trailing bracketed group note. All other criteria (C-43, C-44, C-45) carry over from R4 V-04 at PASS.
**Hypothesis**: Form B per-annotation isolation comments satisfy C-46 equivalently to Form A bracketed group notes. The per-annotation form makes isolation explicit at the annotation level rather than in a trailing bracket -- each annotation carries its own isolation confirmation. V-03 tests whether this distributed self-declaration form is accepted as a C-46 PASS at every convergence step in the pipeline.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Pipeline-wide: each per-input annotation must be parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation -- without
reading adjacent annotations or relying on a shared header for scope.
Grouping is a symptom of failing this standard, not the standard itself.
[C-45 PASS: meta-rule states parseable-completeness-in-isolation as the positive standard]

| Named Output                                 | Produced by              | Consumed by                                                                                    |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                                  |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                                           |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                                          |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                                          |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name)              |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                                       |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                                       |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                                       |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                                     |

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim and closes with:
   Inertia case: [BUILT / PARTIAL / OPEN + reason] -> STEP E (forward arrow).
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all five named inputs by label -- one independently parseable
   per-input annotation each (pipeline-wide standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions:
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
12. PART 2 STEP E opens with two per-annotation isolation comments (Form B; C-46 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
      -- (annotation 1 of 2: parseable without annotation 2; isolation confirmed)
    Required input -- do not re-derive: Inertia case from STEP A
      -- (annotation 2 of 2: parseable without annotation 1; isolation confirmed)
    [C-46 PASS: per-annotation isolation form at this 2-input convergence step]

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|
(Inertia Relevant: does this artifact speak to the comparison between {{topic}} and
the status-quo alternative -- competitors, benchmarks, usage data, mechanism evidence?
Mark yes / no.)

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Inertia-relevant artifact count (from column above):
  1 or more -> staleness threshold = 14 days
  0         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

Analysis order: CAUSAL GAP -> SEQUENCE -> COHERENCE -> STALENESS.
For each: cite artifacts by name, severity internally (not a gate), coaching
observation, one concrete next action if flagged.

### CAUSAL GAP

Inertia-relevant pool: [list every artifact tagged yes in Step 1].
Evaluate mechanism evidence from this pool only.

Inertia anchor: [restate Step 0 in one phrase].

If pool is EMPTY:
  Mechanism verdict is absent by default. State explicitly. Name what artifact types
  would populate the pool. Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence for the pathway from {{topic}} to its claimed outcome, specifically
  better than the status-quo alternative? State: present / partial / absent.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read ordering through mechanism lens: did inertia-relevant pool artifacts appear in
the discovery phase, or did the team specify before mechanism evidence existed?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before earliest spec artifact /
  NO -- mechanism evidence was present when team committed to spec]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  -- (annotation 1 of 3: parseable without annotations 2-3; isolation confirmed)
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  -- (annotation 2 of 3: parseable without annotations 1 and 3; isolation confirmed)
Required input -- do not re-derive: Mechanism-stale from STALENESS
  -- (annotation 3 of 3: parseable without annotations 1-2; isolation confirmed)
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-46 PASS: per-annotation isolation form at this 3-input convergence step]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.
-> PART 2 STEP C per-dim: Required input -- do not re-derive: Root pattern.
-> PART 2 STEP D: Required input -- do not re-derive: Root pattern. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence present, status-quo comparison addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]
-> STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after STEP D and finalized in STEP E]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
    -- (annotation 1 of 2: parseable without annotation 2; isolation confirmed)
  Required input -- do not re-derive: Root pattern from STEP 3
    -- (annotation 2 of 2: parseable without annotation 1; isolation confirmed)
  [C-46 PASS: per-annotation isolation form at this 2-input consuming step]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
    -- (annotation 1 of 2: parseable without annotation 2; isolation confirmed)
  Required input -- do not re-derive: Root pattern from STEP 3
    -- (annotation 2 of 2: parseable without annotation 1; isolation confirmed)
  [C-46 PASS: per-annotation isolation form at this 2-input consuming step]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
    -- (annotation 1 of 2: parseable without annotation 2; isolation confirmed)
  Required input -- do not re-derive: Root pattern from STEP 3
    -- (annotation 2 of 2: parseable without annotation 1; isolation confirmed)
  [C-46 PASS: per-annotation isolation form at this 2-input consuming step]
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]"
    / STALENESS is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
  -- (annotation 1 of 5: parseable without other 4; isolation confirmed)
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
  -- (annotation 2 of 5: parseable without other 4; isolation confirmed)
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
  -- (annotation 3 of 5: parseable without other 4; isolation confirmed)
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
  -- (annotation 4 of 5: parseable without other 4; isolation confirmed)
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
  -- (annotation 5 of 5: parseable without other 4; isolation confirmed)
[C-46 PASS: per-annotation isolation form at this 5-input convergence step]

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
If any OPEN: name dimension(s) and reason for divergence.

Confirmed readiness: [READY -- all drift CLOSED, mechanism evidence sufficient /
  CONDITIONALLY READY -- [list conditions]; one more loop recommended on [dimension] /
  NOT READY -- [dimension] OPEN; mechanism or timing gap must be addressed]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
  -- (annotation 1 of 2: parseable without annotation 2; isolation confirmed)
Required input -- do not re-derive: Inertia case from STEP A
  -- (annotation 2 of 2: parseable without annotation 1; isolation confirmed)
[C-46 PASS: per-annotation isolation form at this 2-input convergence step]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]
```

---

## V-04 -- C-46 Form A: Bracketed Group Note at All Convergence Steps (PASS, Full Pipeline Coverage)

**Axes**: C-46 Form A at all convergence steps (STEP 3, STEP C per-dim, STEP D, STEP E) -- PASS. Form A uses a trailing bracketed group note with full step identification. All other criteria (C-43, C-44, C-45) PASS. This is the expected 38/38 baseline for R5.
**Hypothesis**: Adding a C-46 self-declaration bracket at STEP E (the gap in R4 V-04) closes the final C-46 coverage gap and achieves 38/38 against v5 rubric. V-04 is the complete pipeline coverage baseline using Form A (bracketed group notes) at every convergence step. The STEP E bracket reads: [C-43 PASS: two independent per-input annotations at this 2-input convergence step; C-46 PASS: self-declaration present at STEP E; full pipeline coverage].

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Pipeline-wide: each per-input annotation must be parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation -- without
reading adjacent annotations or relying on a shared header for scope.
Grouping is a symptom of failing this standard, not the standard itself.
[C-45 PASS: meta-rule states parseable-completeness-in-isolation as the positive standard]

| Named Output                                 | Produced by              | Consumed by                                                                                    |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                                  |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                                           |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                                          |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                                          |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name)              |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                                       |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                                       |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                                       |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                                     |

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim and closes with:
   Inertia case: [BUILT / PARTIAL / OPEN + reason] -> STEP E (forward arrow).
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all five named inputs by label -- one independently parseable
   per-input annotation each (pipeline-wide standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions:
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
12. PART 2 STEP E opens with two independent per-input prohibitions and a C-46 self-declaration
    (Form A; C-46 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
     C-46 PASS: self-declaration present at STEP E; full pipeline coverage]

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|
(Inertia Relevant: does this artifact speak to the comparison between {{topic}} and
the status-quo alternative -- competitors, benchmarks, usage data, mechanism evidence?
Mark yes / no.)

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Inertia-relevant artifact count (from column above):
  1 or more -> staleness threshold = 14 days
  0         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

Analysis order: CAUSAL GAP -> SEQUENCE -> COHERENCE -> STALENESS.
For each: cite artifacts by name, severity internally (not a gate), coaching
observation, one concrete next action if flagged.

### CAUSAL GAP

Inertia-relevant pool: [list every artifact tagged yes in Step 1].
Evaluate mechanism evidence from this pool only.

Inertia anchor: [restate Step 0 in one phrase].

If pool is EMPTY:
  Mechanism verdict is absent by default. State explicitly. Name what artifact types
  would populate the pool. Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence for the pathway from {{topic}} to its claimed outcome, specifically
  better than the status-quo alternative? State: present / partial / absent.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read ordering through mechanism lens: did inertia-relevant pool artifacts appear in
the discovery phase, or did the team specify before mechanism evidence existed?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before earliest spec artifact /
  NO -- mechanism evidence was present when team committed to spec]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-43 PASS: three independent per-input annotations at this 3-input consuming step;
 C-46 PASS: self-declaration present at STEP 3]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.
-> PART 2 STEP C per-dim: Required input -- do not re-derive: Root pattern.
-> PART 2 STEP D: Required input -- do not re-derive: Root pattern. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence present, status-quo comparison addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]
-> STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after STEP D and finalized in STEP E]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input consuming step; C-46 PASS]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input consuming step; C-46 PASS]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input consuming step; C-46 PASS]
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]"
    / STALENESS is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
[C-43 PASS: five independent per-input annotations at this 5-input convergence step;
 each annotation is independently parseable without proximity dependency;
 C-46 PASS: self-declaration present at STEP D]

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
If any OPEN: name dimension(s) and reason for divergence.

Confirmed readiness: [READY -- all drift CLOSED, mechanism evidence sufficient /
  CONDITIONALLY READY -- [list conditions]; one more loop recommended on [dimension] /
  NOT READY -- [dimension] OPEN; mechanism or timing gap must be addressed]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A
[C-43 PASS: two independent per-input annotations at this 2-input convergence step;
 C-46 PASS: self-declaration present at STEP E; full pipeline coverage]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]
```

---

## V-05 -- C-46 Form B Alt: Per-Annotation Isolation with Alt Phrasing at All Convergence Steps (PASS)

**Axes**: C-46 Form B alt at all convergence steps (STEP 3, STEP C per-dim, STEP D, STEP E) -- PASS. Form B alt uses alt-phrased per-annotation isolation comments (`-- (self-contained: reads without annotation N; no proximity reliance)`) rather than the numbered isolation form in V-03. All other criteria (C-43, C-44, C-45) PASS. This is the second expected 38/38 variation alongside V-04.
**Hypothesis**: The core property C-46 requires is that each annotation carries an explicit self-declaration of isolation -- the specific phrasing is not mandated. V-05 tests whether alt-phrased per-annotation comments (`self-contained: reads without...`) satisfy C-46 equivalently to the numbered form in V-03 and the bracketed group note in V-04. If both V-04 and V-05 score 38/38, Forms A and B are confirmed equivalent for C-46.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Pipeline-wide: each per-input annotation must be parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation -- without
reading adjacent annotations or relying on a shared header for scope.
Grouping is a symptom of failing this standard, not the standard itself.
[C-45 PASS: meta-rule states parseable-completeness-in-isolation as the positive standard]

| Named Output                                 | Produced by              | Consumed by                                                                                    |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                                  |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                                           |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                                          |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                                          |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name)              |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                                       |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                                       |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                                       |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                                     |

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim and closes with:
   Inertia case: [BUILT / PARTIAL / OPEN + reason] -> STEP E (forward arrow).
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all five named inputs by label -- one independently parseable
   per-input annotation each (pipeline-wide standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions:
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
12. PART 2 STEP E opens with two per-annotation isolation comments (Form B alt; C-46 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
      -- (self-contained: reads without annotation 2; no proximity reliance)
    Required input -- do not re-derive: Inertia case from STEP A
      -- (self-contained: reads without annotation 1; no proximity reliance)
    [C-46 PASS: alt-phrased per-annotation isolation at this 2-input convergence step]

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|
(Inertia Relevant: does this artifact speak to the comparison between {{topic}} and
the status-quo alternative -- competitors, benchmarks, usage data, mechanism evidence?
Mark yes / no.)

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Inertia-relevant artifact count (from column above):
  1 or more -> staleness threshold = 14 days
  0         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

Analysis order: CAUSAL GAP -> SEQUENCE -> COHERENCE -> STALENESS.
For each: cite artifacts by name, severity internally (not a gate), coaching
observation, one concrete next action if flagged.

### CAUSAL GAP

Inertia-relevant pool: [list every artifact tagged yes in Step 1].
Evaluate mechanism evidence from this pool only.

Inertia anchor: [restate Step 0 in one phrase].

If pool is EMPTY:
  Mechanism verdict is absent by default. State explicitly. Name what artifact types
  would populate the pool. Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence for the pathway from {{topic}} to its claimed outcome, specifically
  better than the status-quo alternative? State: present / partial / absent.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read ordering through mechanism lens: did inertia-relevant pool artifacts appear in
the discovery phase, or did the team specify before mechanism evidence existed?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before earliest spec artifact /
  NO -- mechanism evidence was present when team committed to spec]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  -- (self-contained: reads without annotations 2-3; no proximity reliance)
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  -- (self-contained: reads without annotations 1 and 3; no proximity reliance)
Required input -- do not re-derive: Mechanism-stale from STALENESS
  -- (self-contained: reads without annotations 1-2; no proximity reliance)
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-46 PASS: alt-phrased per-annotation isolation at this 3-input convergence step]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.
-> PART 2 STEP C per-dim: Required input -- do not re-derive: Root pattern.
-> PART 2 STEP D: Required input -- do not re-derive: Root pattern. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence present, status-quo comparison addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]
-> STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after STEP D and finalized in STEP E]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
    -- (self-contained: reads without other annotation; no proximity reliance)
  Required input -- do not re-derive: Root pattern from STEP 3
    -- (self-contained: reads without other annotation; no proximity reliance)
  [C-46 PASS: alt-phrased per-annotation isolation at this 2-input consuming step]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
    -- (self-contained: reads without other annotation; no proximity reliance)
  Required input -- do not re-derive: Root pattern from STEP 3
    -- (self-contained: reads without other annotation; no proximity reliance)
  [C-46 PASS: alt-phrased per-annotation isolation at this 2-input consuming step]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
    -- (self-contained: reads without other annotation; no proximity reliance)
  Required input -- do not re-derive: Root pattern from STEP 3
    -- (self-contained: reads without other annotation; no proximity reliance)
  [C-46 PASS: alt-phrased per-annotation isolation at this 2-input consuming step]
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]"
    / STALENESS is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
  -- (self-contained: reads without other annotations; no proximity reliance)
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
  -- (self-contained: reads without other annotations; no proximity reliance)
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
  -- (self-contained: reads without other annotations; no proximity reliance)
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
  -- (self-contained: reads without other annotations; no proximity reliance)
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
  -- (self-contained: reads without other annotations; no proximity reliance)
[C-46 PASS: alt-phrased per-annotation form at this 5-input convergence step]

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
If any OPEN: name dimension(s) and reason for divergence.

Confirmed readiness: [READY -- all drift CLOSED, mechanism evidence sufficient /
  CONDITIONALLY READY -- [list conditions]; one more loop recommended on [dimension] /
  NOT READY -- [dimension] OPEN; mechanism or timing gap must be addressed]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
  -- (self-contained: reads without annotation 2; no proximity reliance)
Required input -- do not re-derive: Inertia case from STEP A
  -- (self-contained: reads without annotation 1; no proximity reliance)
[C-46 PASS: alt-phrased per-annotation isolation at this 2-input convergence step]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]
```
