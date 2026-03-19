`signal-check-variations-R7-2026-03-17.md` written. Here's what was designed:

---

**R7 axis: C-50 / C-51**

| V | C-50 | C-51 | Form | Expected |
|---|------|------|------|---------|
| V-01 | FAIL | PASS | A | 42/43 |
| V-02 | PASS | FAIL | A | 42/43 |
| V-03 | FAIL | FAIL | A | 41/43 |
| V-04 | PASS | PASS | A | 43/43 |
| V-05 | PASS | PASS | B | 43/43 |

**What each variation isolates:**

- **V-01** — C-47 unified contract present; phrasing-agnosticism declared ("any phrasing delivering the property passes") but no phrasings enumerated. Tests whether C-50 requires at least two named phrasings, not just an abstract claim.
- **V-02** — Two phrasings named (C-50 PASS); C-49 form equivalence abstract only — no Form A / Form B labels. Tests whether C-51 requires labeled classes, not just the independence-property assertion.
- **V-03** — Both absent; compound failure. Tests independence: 41/43 expected (C-47 and C-49 remain PASS, since their abstract versions satisfy them; only C-50 and C-51 fail).
- **V-04** — Canonical reference: R6 V-04 phrasings explicitly cited by round/label; Form A / Form B named.
- **V-05** — Alternative phrasing for C-50 ("Both the following phrasings deliver the unified-contract property") and C-51 ("bracket-group form / isolation-comment form"); Form B isolation-comment style used throughout. Confirms both criteria are property-level.

**Key research question:** Do V-04 and V-05 both score 43/43, confirming that enumeration language and form-class label phrasing are interchangeable as long as the property (two named phrasings / two labeled classes) is delivered?
otation) compliance notes throughout.
- **V-05**: Alternative phrasing for C-50 enumeration and C-51 labeling; uses Form B (isolation comments) at convergence steps. Tests that C-50 and C-51 are property-level — any enumeration naming at least two phrasings and any labeling naming the two form classes both pass.

**Key research question across all 5**: Do V-04 and V-05 both score 43/43, confirming C-50 and C-51 are property-level — satisfied by any enumeration naming at least two phrasings (C-50) and any labeling naming the two form classes (C-51)?

---

## V-01 — C-50 FAIL: Phrasing-agnosticism declared abstractly, no phrasings named

**Axis**: Single — C-50. C-47 unified-contract statement present and satisfies C-47. C-49 form equivalence satisfies C-51 (Form A and Form B named by label). But the phrasing-agnosticism claim for C-47 reads: "any phrasing that delivers the unified-contract property passes" — no confirmed-equivalent phrasings are enumerated.
**Hypothesis**: C-50 requires the meta-rule to name at least two confirmed-equivalent phrasings, not only to assert that phrasings are interchangeable in the abstract. An abstract claim without examples leaves evaluators applying a full property test rather than matching by confirmed label — the same gap C-51 closes for form classes. V-01 tests whether C-50 fails when phrasing-agnosticism is declared but phrasings are unnamed.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step with N named inputs carries N independently self-standing
per-input prohibitions -- each annotation parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation, without
reading adjacent annotations or relying on a shared header for scope.
Independence is the governing standard; non-grouping is a consequence of it,
not the standard itself.
[C-45 PASS: independence-in-isolation named as positive standard]

Form equivalence for convergence compliance notes: any notation satisfying the
independence property passes. Confirmed-equivalent form classes by label:
  Form A (bracket notation): [C-43 PASS: N independent per-input annotations at
    this N-input convergence step; each annotation is independently parseable
    without proximity dependency]
  Form B (isolation comments): per-annotation "(annotation stands alone: readable
    in isolation without the [X] annotation)" followed by trailing "[N annotations
    above; each stands alone -- independence property satisfied at this N-input step]"
Both forms satisfy the independence property and pass equivalently.
[C-49 PASS: form equivalence explicitly declared in meta-rule]
[C-51 PASS: Form A (bracket notation) and Form B (isolation comments) named as
 confirmed-equivalent form classes by label]

Local-verifiability contract -- three enforcement nodes as co-equal self-declaration peers:
  (1) Consuming steps: "Required input -- do not re-derive: [label]" per named input (C-26)
  (2) Terminal producer (STEP E): "Required output -- emit exactly: [label]" (C-39)
  (3) Convergence points: inline compliance note after N per-input annotations (C-46)
Each node class self-declares its obligation locally; no cross-referencing needed.
Together they form a complete local-verifiability contract for the full pipeline.
[C-47 PASS: three enforcement nodes declared as co-equal peers in unified contract]

C-47 phrasing-agnosticism: any phrasing that delivers the unified-contract property
(three nodes named as co-equal peers forming a complete local-verifiability system)
passes. The criterion is the property, not specific wording.
[C-50 FAIL: phrasing-agnosticism declared but no confirmed-equivalent phrasings named --
 C-50 requires at least two phrasings to be explicitly enumerated]

C-46 coverage commitment: 7 multi-input consuming steps in this pipeline
(STEP 3, STEP C CAUSAL GAP, STEP C SEQUENCE, STEP C COHERENCE, STEP C STALENESS,
STEP D, STEP E). After STEP E, emit:
  C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes.
[C-48 PASS: pipeline-completeness certification declared as count commitment before analysis]

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                      |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                               |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                              |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                              |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                         |

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
   per-input annotation each (pipeline-wide independence standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions, then
    emits Terminal readiness with inline forward arrow -> topic namespace.
12. After STEP E, emit: C-46 coverage: complete -- 7/7 multi-input consuming steps carry
    inline compliance notes (STEP 3, STEP C x4 dimensions, STEP D, STEP E).

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
-> STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
-> PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
-> STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
-> PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
-> STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
-> PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-43 PASS: three independent per-input annotations at this 3-input consuming step;
 each annotation is independently parseable without proximity dependency]

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
  [C-43 PASS: one independent per-input annotation at this 1-input step; independence trivially satisfied]
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
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
[C-43 PASS: two independent per-input annotations at this 2-input convergence step;
 each annotation is independently parseable without proximity dependency]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]

---

C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes
(STEP 3: 3-input, STEP C SEQUENCE: 2-input, STEP C COHERENCE: 2-input,
 STEP C STALENESS: 2-input, STEP D: 5-input, STEP E: 2-input;
 STEP C CAUSAL GAP: 1-input, trivially satisfied).
```

---

## V-02 -- C-51 FAIL: Form-equivalence declared abstractly, Form A / Form B not labeled

**Axis**: Single -- C-51. C-50 satisfies -- two confirmed-equivalent phrasings named explicitly for C-47. C-49 form equivalence is declared but abstractly only: "any notation satisfying the independence property passes" with no Form A / Form B class labels.
**Hypothesis**: C-51 requires the form-equivalence declaration to name the two confirmed-equivalent form classes by label, not merely assert that any form satisfying the independence property passes. Without labeled classes, an evaluator must apply the full independence property test to determine whether a given notation qualifies -- the same overhead C-49 reduces at the property level. V-02 tests whether C-51 fails when form equivalence is abstract and form classes are unlabeled.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step with N named inputs carries N independently self-standing
per-input prohibitions -- each annotation parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation, without
reading adjacent annotations or relying on a shared header for scope.
Independence is the governing standard; non-grouping is a consequence of it,
not the standard itself.
[C-45 PASS: independence-in-isolation named as positive standard]

Form equivalence for convergence compliance notes: any notation satisfying the
independence property passes -- bracketed group note, per-annotation isolation
comment, or equivalent form are interchangeable. The criterion is the property,
not the specific notation.
[C-49 PASS: form equivalence explicitly declared in meta-rule]
[C-51 FAIL: form equivalence declared by abstract property reference only -- no
 Form A (bracket notation) or Form B (isolation comments) named as labeled classes]

Local-verifiability contract -- three enforcement nodes as co-equal self-declaration peers:
  (1) Consuming steps: "Required input -- do not re-derive: [label]" per named input (C-26)
  (2) Terminal producer (STEP E): "Required output -- emit exactly: [label]" (C-39)
  (3) Convergence points: inline compliance note after N per-input annotations (C-46)
Each node class self-declares its obligation locally; no cross-referencing needed.
Together they form a complete local-verifiability contract for the full pipeline.
[C-47 PASS: three enforcement nodes declared as co-equal peers in unified contract]

C-47 phrasing-agnosticism: any phrasing that delivers the unified-contract property
(three nodes named as co-equal peers forming a complete local-verifiability system)
passes. Confirmed-equivalent phrasings from research:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
[C-50 PASS: phrasing-agnosticism declared with at least two confirmed-equivalent
 phrasings named explicitly]

C-46 coverage commitment: 7 multi-input consuming steps in this pipeline
(STEP 3, STEP C CAUSAL GAP, STEP C SEQUENCE, STEP C COHERENCE, STEP C STALENESS,
STEP D, STEP E). After STEP E, emit:
  C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes.
[C-48 PASS: pipeline-completeness certification declared as count commitment before analysis]

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                      |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                               |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                              |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                              |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                         |

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
   per-input annotation each (pipeline-wide independence standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions, then
    emits Terminal readiness with inline forward arrow -> topic namespace.
12. After STEP E, emit: C-46 coverage: complete -- 7/7 multi-input consuming steps carry
    inline compliance notes (STEP 3, STEP C x4 dimensions, STEP D, STEP E).

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
-> STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
-> PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
-> STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
-> PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
-> STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
-> PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-43 PASS: three independent per-input annotations at this 3-input consuming step;
 each annotation is independently parseable without proximity dependency]

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
  [C-43 PASS: one independent per-input annotation at this 1-input step; independence trivially satisfied]
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
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
[C-43 PASS: two independent per-input annotations at this 2-input convergence step;
 each annotation is independently parseable without proximity dependency]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]

---

C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes
(STEP 3: 3-input, STEP C SEQUENCE: 2-input, STEP C COHERENCE: 2-input,
 STEP C STALENESS: 2-input, STEP D: 5-input, STEP E: 2-input;
 STEP C CAUSAL GAP: 1-input, trivially satisfied).
```

---

## V-03 -- C-50 FAIL + C-51 FAIL: Both abstract, neither enumerated

**Axis**: Combined -- C-50 and C-51 both fail. C-47 unified contract present. C-49 form equivalence present. Neither carries the confirmed enumeration that C-50 and C-51 require. Tests that the two criteria are independent: failing both should score 41/43, not 40/43 (they address separate gaps -- phrasing drift for C-47 and notation drift for C-49).
**Hypothesis**: C-50 and C-51 both fail cleanly and independently. The compound failure scores exactly 41/43, two fewer than the 43/43 reference. No cascading effect: C-47 and C-49 both remain PASS since they are satisfied by the abstract declarations.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step with N named inputs carries N independently self-standing
per-input prohibitions -- each annotation parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation, without
reading adjacent annotations or relying on a shared header for scope.
Independence is the governing standard; non-grouping is a consequence of it,
not the standard itself.
[C-45 PASS: independence-in-isolation named as positive standard]

Form equivalence for convergence compliance notes: any notation satisfying the
independence property passes -- bracketed group note, per-annotation isolation
comment, or equivalent form are interchangeable. The criterion is the property,
not the specific notation.
[C-49 PASS: form equivalence explicitly declared in meta-rule]
[C-51 FAIL: form classes not named by label -- abstract property reference only;
 no "Form A (bracket notation)" or "Form B (isolation comments)" enumerated]

Local-verifiability contract -- three enforcement nodes as co-equal self-declaration peers:
  (1) Consuming steps: "Required input -- do not re-derive: [label]" per named input (C-26)
  (2) Terminal producer (STEP E): "Required output -- emit exactly: [label]" (C-39)
  (3) Convergence points: inline compliance note after N per-input annotations (C-46)
Each node class self-declares its obligation locally; no cross-referencing needed.
Together they form a complete local-verifiability contract for the full pipeline.
[C-47 PASS: three enforcement nodes declared as co-equal peers in unified contract]

C-47 phrasing-agnosticism: any phrasing delivering the unified-contract property passes.
The criterion is the property, not any specific wording.
[C-50 FAIL: phrasing-agnosticism declared but no confirmed-equivalent phrasings named --
 abstract claim only; C-50 requires at least two phrasings explicitly enumerated]

C-46 coverage commitment: 7 multi-input consuming steps in this pipeline
(STEP 3, STEP C CAUSAL GAP, STEP C SEQUENCE, STEP C COHERENCE, STEP C STALENESS,
STEP D, STEP E). After STEP E, emit:
  C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes.
[C-48 PASS: pipeline-completeness certification declared as count commitment before analysis]

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                      |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                               |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                              |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                              |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                         |

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
   per-input annotation each (pipeline-wide independence standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions, then
    emits Terminal readiness with inline forward arrow -> topic namespace.
12. After STEP E, emit: C-46 coverage: complete -- 7/7 multi-input consuming steps carry
    inline compliance notes (STEP 3, STEP C x4 dimensions, STEP D, STEP E).

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
-> STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
-> PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
-> STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
-> PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
-> STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
-> PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-43 PASS: three independent per-input annotations at this 3-input consuming step;
 each annotation is independently parseable without proximity dependency]

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
  [C-43 PASS: one independent per-input annotation at this 1-input step; independence trivially satisfied]
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
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
[C-43 PASS: two independent per-input annotations at this 2-input convergence step;
 each annotation is independently parseable without proximity dependency]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]

---

C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes
(STEP 3: 3-input, STEP C SEQUENCE: 2-input, STEP C COHERENCE: 2-input,
 STEP C STALENESS: 2-input, STEP D: 5-input, STEP E: 2-input;
 STEP C CAUSAL GAP: 1-input, trivially satisfied).
```

---

## V-04 -- C-50 PASS + C-51 PASS: Canonical reference, Form A

**Axis**: Combined -- both PASS. Phrasing-agnosticism names both confirmed-equivalent phrasings from R6. Form-equivalence declaration names Form A (bracket notation) and Form B (isolation comments) by label. Form A compliance notes used throughout.
**Hypothesis**: 43/43. C-50 and C-51 both satisfied by explicit enumeration. All prior criteria carry forward from R6 V-04 (41/41 baseline).

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step with N named inputs carries N independently self-standing
per-input prohibitions -- each annotation parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation, without
reading adjacent annotations or relying on a shared header for scope.
Independence is the governing standard; non-grouping is a consequence of it,
not the standard itself.
[C-45 PASS: independence-in-isolation named as positive standard]

Form equivalence for convergence compliance notes: any notation satisfying the
independence property passes. Confirmed-equivalent form classes by label:
  Form A (bracket notation): [C-43 PASS: N independent per-input annotations at
    this N-input convergence step; each annotation is independently parseable
    without proximity dependency]
  Form B (isolation comments): per-annotation "(annotation stands alone: readable
    in isolation without the [X] annotation)" followed by trailing "[N annotations
    above; each stands alone -- independence property satisfied at this N-input step]"
Both forms satisfy the independence property and pass equivalently. The criterion
is the property (independence / parseable completeness), not the specific notation.
[C-49 PASS: form equivalence explicitly declared in meta-rule]
[C-51 PASS: Form A (bracket notation) and Form B (isolation comments) named as
 confirmed-equivalent form classes by label]

Local-verifiability contract -- three enforcement nodes as co-equal self-declaration peers:
  (1) Consuming steps: "Required input -- do not re-derive: [label]" per named input (C-26)
  (2) Terminal producer (STEP E): "Required output -- emit exactly: [label]" (C-39)
  (3) Convergence points: inline compliance note after N per-input annotations (C-46)
Each node class self-declares its obligation locally; no cross-referencing needed.
Together they form a complete local-verifiability contract for the full pipeline.
[C-47 PASS: three enforcement nodes declared as co-equal peers in unified contract]

C-47 phrasing-agnosticism: any phrasing that delivers the unified-contract property
(three nodes named as co-equal peers forming a complete local-verifiability system)
passes. Confirmed-equivalent phrasings from research:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
[C-50 PASS: phrasing-agnosticism declared with at least two confirmed-equivalent
 phrasings named explicitly]

C-46 coverage commitment: 7 multi-input consuming steps in this pipeline
(STEP 3, STEP C CAUSAL GAP, STEP C SEQUENCE, STEP C COHERENCE, STEP C STALENESS,
STEP D, STEP E). After STEP E, emit:
  C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes.
[C-48 PASS: pipeline-completeness certification declared as count commitment before analysis]

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                      |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                               |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                              |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                              |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                         |

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
   per-input annotation each (pipeline-wide independence standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions, then
    emits Terminal readiness with inline forward arrow -> topic namespace.
12. After STEP E, emit: C-46 coverage: complete -- 7/7 multi-input consuming steps carry
    inline compliance notes (STEP 3, STEP C x4 dimensions, STEP D, STEP E).

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
-> STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
-> PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
-> STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
-> PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
-> STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
-> PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]
[C-43 PASS: three independent per-input annotations at this 3-input consuming step;
 each annotation is independently parseable without proximity dependency]

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
  [C-43 PASS: one independent per-input annotation at this 1-input step; independence trivially satisfied]
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  [C-43 PASS: two independent per-input annotations at this 2-input convergence step;
   each annotation is independently parseable without proximity dependency]
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
[C-43 PASS: two independent per-input annotations at this 2-input convergence step;
 each annotation is independently parseable without proximity dependency]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]

---

C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes
(STEP 3: 3-input, STEP C SEQUENCE: 2-input, STEP C COHERENCE: 2-input,
 STEP C STALENESS: 2-input, STEP D: 5-input, STEP E: 2-input;
 STEP C CAUSAL GAP: 1-input, trivially satisfied).
```

---

## V-05 -- C-50 PASS + C-51 PASS: Alternative phrasing, Form B

**Axis**: Combined -- both PASS, alternative phrasing throughout. C-50 uses different enumeration language than V-04. C-51 uses different form-class labeling language than V-04. Form B (isolation comments) used at all convergence steps. Tests that C-50 and C-51 are property-level, not phrase-specific.
**Hypothesis**: 43/43. C-50 satisfied by any enumeration that names at least two confirmed-equivalent phrasings. C-51 satisfied by any labeling that names the two form classes -- alternative label framing ("labeled equivalents: bracket-group form" vs. "Form A (bracket notation)") both satisfy, provided the class identity is clear. V-05 confirms that neither criterion is phrase-specific.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step with N named inputs carries N independently self-standing
per-input prohibitions -- each annotation parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation, without
reading adjacent annotations or relying on a shared header for scope.
Parseable in isolation is the governing standard -- grouping is a symptom of
failing this standard, not the standard itself.
[C-45 PASS: independence-in-isolation named as positive standard]

Form equivalence for convergence compliance notes: the independence property is the
criterion; the specific form is not. Two confirmed-equivalent labeled form classes:
  bracket-group form (Form A): a single bracketed annotation after the N per-input
    lines -- e.g., [C-43 PASS: N independent per-input annotations at this N-input
    convergence step; each annotation is independently parseable without proximity
    dependency]
  isolation-comment form (Form B): a per-annotation trailing comment on each
    prohibition line -- e.g., "(annotation stands alone: readable in isolation
    without the [X] annotation)" -- followed by a trailing group note --
    e.g., "[N annotations above; each stands alone -- independence property
    satisfied at this N-input step]"
Either class satisfies C-46 equivalently. Future forms satisfying the independence
property are equally valid without requiring a new rubric entry.
[C-49 PASS: form equivalence explicitly declared in meta-rule]
[C-51 PASS: bracket-group form (Form A) and isolation-comment form (Form B) named
 as confirmed-equivalent labeled classes -- independence property is the criterion]

Three-node self-declaration system: consuming steps, terminal producer, and
convergence points are co-equal enforcement nodes -- each locally visible,
each self-declaring its obligation without cross-reference:
  (1) Consuming steps: "Required input -- do not re-derive: [label]" per named input
  (2) Terminal producer (STEP E): "Required output -- emit exactly: [label]"
  (3) Convergence points: inline compliance note (Form A or Form B) after N prohibitions
Together these make every pipeline obligation locally self-declared without cross-
referencing. The three nodes are co-equal peers forming a complete local-verifiability
contract for the full pipeline.
[C-47 PASS: three enforcement nodes declared as unified local-verifiability contract,
 co-equal, locally visible]

C-47 phrasing is property-level, not phrase-specific. Both the following phrasings
deliver the unified-contract property and pass equivalently:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
Any phrasing naming the three nodes as co-equal peers in a complete self-declaring
system satisfies C-47. Specific wording is not required.
[C-50 PASS: phrasing-agnosticism for C-47 declared with two confirmed-equivalent
 phrasings explicitly named by citation]

C-46 coverage commitment: 7 multi-input consuming steps in this pipeline
(STEP 3, STEP C CAUSAL GAP, STEP C SEQUENCE, STEP C COHERENCE, STEP C STALENESS,
STEP D, STEP E). After STEP E, emit:
  C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes.
[C-48 PASS: pipeline-completeness certification declared as count commitment before analysis]

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                                      |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                               |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                              |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                              |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label)                                                         |

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
   per-input annotation each (pipeline-wide independence standard applies at this 5-input step).
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independently parseable per-input prohibitions, then
    emits Terminal readiness with inline forward arrow -> topic namespace.
12. After STEP E, emit: C-46 coverage: complete -- 7/7 multi-input consuming steps carry
    inline compliance notes (STEP 3, STEP C x4 dimensions, STEP D, STEP E).

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
  (annotation stands alone: readable in isolation without any other annotation)
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"
[1 annotation above; stands alone -- independence property satisfied at this 1-input step]

Cite 2+ artifacts with dates. Did discovery precede specification?
Read ordering through mechanism lens: did inertia-relevant pool artifacts appear in
the discovery phase, or did the team specify before mechanism evidence existed?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before earliest spec artifact /
  NO -- mechanism evidence was present when team committed to spec]
-> STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
-> PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether mechanism-relevant.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- name the contradiction and inertia-pool artifact /
  NO -- no contradiction involves inertia-pool signals]
-> STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
-> PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- name inertia-pool artifact(s) outside threshold /
  NO -- all inertia-pool artifacts within threshold]
-> STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
-> PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  (annotation stands alone: readable in isolation without the Mechanism-relevant
   contradiction or Mechanism-stale annotations)
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  (annotation stands alone: readable in isolation without the Pre-specification gap
   or Mechanism-stale annotations)
Required input -- do not re-derive: Mechanism-stale from STALENESS
  (annotation stands alone: readable in isolation without the Pre-specification gap
   or Mechanism-relevant contradiction annotations)
[3 annotations above; each stands alone -- independence property satisfied at this 3-input step]

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
  (annotation stands alone: readable in isolation without any other annotation)
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"
[1 annotation above; stands alone -- independence property satisfied at this 1-input step]

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
  (annotation stands alone: readable in isolation without any other annotation)
[1 annotation above; stands alone -- independence property satisfied at this 1-input step]

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
    (annotation stands alone: readable in isolation without any other annotation)
  [1 annotation above; stands alone -- independence property satisfied at this 1-input step]
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
    (annotation stands alone: readable in isolation without the Root pattern annotation)
  Required input -- do not re-derive: Root pattern from STEP 3
    (annotation stands alone: readable in isolation without the Pre-specification gap annotation)
  [2 annotations above; each stands alone -- independence property satisfied at this 2-input step]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
    (annotation stands alone: readable in isolation without the Root pattern annotation)
  Required input -- do not re-derive: Root pattern from STEP 3
    (annotation stands alone: readable in isolation without the Mechanism-relevant
     contradiction annotation)
  [2 annotations above; each stands alone -- independence property satisfied at this 2-input step]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
    (annotation stands alone: readable in isolation without the Root pattern annotation)
  Required input -- do not re-derive: Root pattern from STEP 3
    (annotation stands alone: readable in isolation without the Mechanism-stale annotation)
  [2 annotations above; each stands alone -- independence property satisfied at this 2-input step]
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]"
    / STALENESS is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
  (annotation stands alone: readable in isolation without the four STEP C drift annotations)
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
  (annotation stands alone: readable in isolation without the Root pattern and other
   STEP C drift annotations)
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
  (annotation stands alone: readable in isolation without the Root pattern and other
   STEP C drift annotations)
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
  (annotation stands alone: readable in isolation without the Root pattern and other
   STEP C drift annotations)
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
  (annotation stands alone: readable in isolation without the Root pattern and other
   STEP C drift annotations)
[5 annotations above; each stands alone -- independence property satisfied at this 5-input step]

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
  (annotation stands alone: readable in isolation without the Inertia case annotation)
Required input -- do not re-derive: Inertia case from STEP A
  (annotation stands alone: readable in isolation without the Confirmed readiness annotation)
[2 annotations above; each stands alone -- independence property satisfied at this 2-input step]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
[C-44 PASS: forward-declaration arrow inline on verdict line, naming external consumer by identity]

---

C-46 coverage: complete -- 7/7 multi-input consuming steps carry inline compliance notes
(STEP 3: 3-input, STEP C SEQUENCE: 2-input, STEP C COHERENCE: 2-input,
 STEP C STALENESS: 2-input, STEP D: 5-input, STEP E: 2-input;
 STEP C CAUSAL GAP: 1-input, trivially satisfied).
```
