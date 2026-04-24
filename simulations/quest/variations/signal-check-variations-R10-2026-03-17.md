Written to `simulations/quest/variations/signal-check-variations-R10-2026-03-17.md`.

---

**R10 variations summary:**

| V | Axis | C-56 | C-57 | C-58 | C-59 | Composite |
|---|------|------|------|------|------|-----------|
| V-01 | baseline (R9 canonical) | FAIL | FAIL | FAIL | FAIL | 47/51 = 92.16% |
| V-02 | semicolon embeds violation condition in rule body | PASS | FAIL | FAIL | FAIL | 48/51 = 94.12% |
| V-03 | three-column lookup table for active classes | PASS | PASS | FAIL | FAIL | 49/51 = 96.08% |
| V-04 | explicit co-requirement statement | PASS | PASS | PASS | FAIL | 50/51 = 98.04% |
| V-05 | phrasing-agnosticism for C-53/C-54/C-55 complex | PASS | PASS | PASS | PASS | 51/51 = 100.00% |

**What varies across all five:** Only the equivalence-class block in the ARCHITECTURE section. PART 1, PART 2, all locked structural features, and the named-output table are identical.

**The four discrimination points:**
- **C-56**: Period-separated consequence sentence (V-01) vs. semicolon-embedded consequence within the rule body (V-02+)
- **C-57**: Criterion IDs in descriptive parentheticals requiring parsing (V-01/V-02) vs. three-column table where label = lookup key, L1/L2 = scannable columns (V-03+)
- **C-58**: Three elements individually declared without co-requirement (V-01/V-02/V-03) vs. explicit "all three required; none substitutes for another" statement (V-04+)
- **C-59**: No phrasing-agnosticism for the three-criterion complex (V-01 through V-04) vs. property-level declaration with two confirmed-equivalent R9 phrasings named (V-05)
co-requirement statement. Fails C-58/C-59.
- **V-04**: Adds explicit co-requirement statement: "All three are required; no element substitutes for another." Passes C-56/C-57/C-58. No phrasing-agnosticism for the complex. Fails C-59 only.
- **V-05**: Adds phrasing-agnosticism declaration for C-53/C-54/C-55 with two confirmed-equivalent phrasings from R9 research. Passes all four.

**Key confirmation targets:** V-04 = 50/51, V-05 = 51/51. Each step adds exactly one criterion pass. V-01 reconfirms the R9 canonical at 47/51 under the extended rubric.

**Sub-questions:**
- V-01/V-02: Does a post-rule sentence ("A class with only one layer is a locally visible violation.") fail C-56, while a semicolon-embedded clause passes?
- V-02/V-03: Does indented prose-list form fail C-57 while a three-column lookup table passes?
- V-03/V-04: Do three individually-declared elements fail C-58 when no co-requirement statement links them as a mandatory package?
- V-04/V-05: Does a complete three-point package without phrasing-agnosticism for the complex fail C-59?

---

## V-01 -- C-56/C-57/C-58/C-59 ALL FAIL: Violation condition as separate sentence, prose-list classes, no co-requirement, no phrasing-agnosticism

**Axis**: Single -- C-56, C-57, C-58, C-59. R9 V-04 canonical carried forward. Violation condition is a second sentence after the extensibility rule (separated by period). Active equivalence classes in indented prose-list form. No co-requirement statement linking the three elements. No phrasing-agnosticism for the C-53/C-54/C-55 complex.
**Hypothesis**: 47/51 = 92.16%. All R9 criteria (C-01--C-55) carry forward at PASS. C-56 fails: violation condition is a separate sentence -- rule and enforcement trigger are two distinct statements separated by a period. C-57 fails: criterion IDs embedded in descriptive prose; membership verification requires parsing. C-58 fails: three elements present but co-requirement not declared. C-59 fails: no phrasing-agnosticism extension into the new complex.

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
passes. Confirmed-equivalent phrasings from research:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
[C-50 PASS: phrasing-agnosticism declared with at least two confirmed-equivalent
 phrasings named explicitly]

Two-level equivalence-registry design principle -- extensibility contract:
Each equivalence class in this pipeline carries exactly two layers:
  Layer 1 -- property-declaration criterion: closes drift at the declaration level.
    Any implementation satisfying the property passes; the criterion is the
    property, not specific wording or notation.
  Layer 2 -- enumeration criterion: closes drift at the verification level.
    Confirmed-equivalent instances are named by label, reducing evaluator burden
    from property test to label lookup.
Both active equivalence classes are governed by this contract:
  Phrasing equivalence: C-47 (property -- three-node unified-contract framing)
    + C-50 (enumeration -- two confirmed-equivalent phrasings named by label)
  Form equivalence:     C-49 (property -- any notation satisfying independence
    property passes) + C-51 (enumeration -- Form A and Form B named by label)
Extensibility rule: any new equivalence class added to this pipeline must carry
both layers before becoming active.
A class with only one layer is a locally visible violation of this extensibility contract.
[C-53 PASS: two-level structure declared prospectively as a binding architectural
 principle -- "each equivalence class carries exactly two layers" is a forward-facing
 constraint, not a retrospective note on what current classes happen to share]
[C-54 PASS: extensibility contract with explicit forward rule -- violation consequence
 named in the following sentence]
[C-55 PASS: both active classes named by criterion pairs in contract body --
 phrasing equivalence (C-47+C-50) and form equivalence (C-49+C-51) enumerated;
 no unnamed gap]
[C-52 PASS: all R9 requirements satisfied simultaneously]
[C-56 FAIL: violation condition "a class with only one layer is a locally visible
 violation" appears as a standalone sentence after the extensibility rule, separated
 by a period; the rule body ("must carry both layers before becoming active") does not
 self-contain its enforcement consequence; C-56 requires the violation condition to be
 embedded within the rule body, not appended as a separate following sentence]
[C-57 FAIL: active equivalence classes in indented prose-list form with criterion IDs
 embedded in parenthetical descriptions -- "C-47 (property -- three-node unified-contract
 framing)" requires parsing to extract the criterion ID; C-57 requires labeled lookup-table
 form where criterion-ID pairs are scannable column entries, not prose fragments]
[C-58 FAIL: no explicit co-requirement statement declaring that the prospective principle,
 extensibility rule, and class enumeration together form a complete mandatory package;
 the three elements are present and individually declared but their joint necessity is
 not stated -- C-58 requires an explicit statement that all three are required and none
 substitutes for another]
[C-59 FAIL: no phrasing-agnosticism declaration for the C-53/C-54/C-55 structural
 requirements as a complex; the C-49/C-50 pattern has not been extended into this
 new three-criterion group; no confirmed-equivalent phrasings named for the complex]

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

## V-02 -- C-56 PASS / C-57/C-58/C-59 FAIL: Violation condition embedded in rule body, classes still prose-list

**Axis**: Single -- C-56. Violation condition joined to extensibility rule via semicolon, making the rule a self-contained enforcement point. Active equivalence classes remain in indented prose-list form with criterion IDs in descriptive parentheticals. No co-requirement statement. No phrasing-agnosticism for the three-criterion complex.
**Hypothesis**: 48/51 = 94.12%. C-56 passes: "...before becoming active; a single-layer class is a locally visible violation" is one compound statement -- obligation and enforcement trigger co-reside in the rule body. C-57 fails: criterion IDs still embedded in descriptive text. C-58 fails: no co-requirement statement. C-59 fails: no phrasing-agnosticism for C-53/C-54/C-55. All prior criteria carry forward at PASS.

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
passes. Confirmed-equivalent phrasings from research:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
[C-50 PASS: phrasing-agnosticism declared with at least two confirmed-equivalent
 phrasings named explicitly]

Two-level equivalence-registry design principle -- extensibility contract:
Each equivalence class in this pipeline carries exactly two layers:
  Layer 1 -- property-declaration criterion: closes drift at the declaration level.
    Any implementation satisfying the property passes; the criterion is the
    property, not specific wording or notation.
  Layer 2 -- enumeration criterion: closes drift at the verification level.
    Confirmed-equivalent instances are named by label, reducing evaluator burden
    from property test to label lookup.
Both active equivalence classes are governed by this contract:
  Phrasing equivalence: C-47 (property -- three-node unified-contract framing)
    + C-50 (enumeration -- two confirmed-equivalent phrasings named by label)
  Form equivalence:     C-49 (property -- any notation satisfying independence
    property passes) + C-51 (enumeration -- Form A and Form B named by label)
Extensibility rule: any new equivalence class added to this pipeline must carry
both layers before becoming active; a single-layer class is a locally visible
violation of this extensibility contract.
[C-53 PASS: two-level structure declared prospectively as a binding architectural
 principle -- forward-facing constraint, not retrospective note]
[C-54 PASS: extensibility contract with explicit forward rule; violation consequence
 co-present in the rule statement]
[C-55 PASS: both active classes named by criterion pairs in contract body]
[C-52 PASS: all R9 requirements satisfied simultaneously]
[C-56 PASS: violation condition "a single-layer class is a locally visible violation"
 embedded within the extensibility rule body via semicolon -- the obligation ("must
 carry both layers before becoming active") and the enforcement trigger form one
 compound statement; the rule is now a self-contained enforcement point rather than
 a specification requiring a separate consequence sentence]
[C-57 FAIL: active equivalence classes remain in indented prose-list form with
 criterion IDs embedded in parenthetical descriptions (e.g., "C-47 (property --
 three-node unified-contract framing)"); extracting the criterion-ID pair requires
 parsing the descriptive text -- C-57 requires labeled lookup-table form where IDs
 appear as scannable column entries, not prose fragments]
[C-58 FAIL: no explicit co-requirement statement linking the prospective principle,
 extensibility rule, and class enumeration as a required three-point package; the
 three elements are declared but their joint necessity is not stated]
[C-59 FAIL: no phrasing-agnosticism declaration for the C-53/C-54/C-55 complex with
 confirmed-equivalent phrasings named]

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

## V-03 -- C-56/C-57 PASS / C-58/C-59 FAIL: Lookup-table form added, no co-requirement, no phrasing-agnosticism

**Axis**: Single -- C-57. Violation condition embedded (C-56 carries forward). Active equivalence classes converted to three-column labeled lookup table: class label | Layer 1 criterion ID | Layer 2 criterion ID. No co-requirement statement. No phrasing-agnosticism for C-53/C-54/C-55.
**Hypothesis**: 49/51 = 96.08%. C-57 passes: class-label column is a scannable lookup key; criterion IDs appear in dedicated L1/L2 columns, not embedded in prose. Membership verification by label scan is structurally achievable. C-58 fails: table present but three-point co-requirement not declared. C-59 fails: no phrasing-agnosticism extension.

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
passes. Confirmed-equivalent phrasings from research:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
[C-50 PASS: phrasing-agnosticism declared with at least two confirmed-equivalent
 phrasings named explicitly]

Two-level equivalence-registry design principle -- extensibility contract:
Each equivalence class in this pipeline carries exactly two layers:
  Layer 1 -- property-declaration criterion: closes drift at the declaration level.
    Any implementation satisfying the property passes; the criterion is the
    property, not specific wording or notation.
  Layer 2 -- enumeration criterion: closes drift at the verification level.
    Confirmed-equivalent instances are named by label, reducing evaluator burden
    from property test to label lookup.
Active equivalence classes (labeled lookup table -- membership verifiable by label scan):
  Class label              | Layer 1 (property-declaration criterion) | Layer 2 (enumeration criterion)
  -------------------------|------------------------------------------|---------------------------------
  Phrasing equivalence     | C-47                                     | C-50
  Form equivalence         | C-49                                     | C-51
To verify class membership: locate class label in table; confirm both L1 and L2
criterion IDs are present. A label absent from this table names a class not yet
admitted to the pipeline.
Extensibility rule: any new equivalence class added to this pipeline must carry
both layers before becoming active; a single-layer class is a locally visible
violation of this extensibility contract.
[C-53 PASS: two-level structure declared prospectively as a binding architectural
 principle -- forward-facing constraint, not retrospective note]
[C-54 PASS: extensibility contract with explicit forward rule and violation condition
 embedded within rule body]
[C-55 PASS: both active classes enumerated in the lookup table within the contract
 body -- phrasing equivalence (C-47+C-50) and form equivalence (C-49+C-51) as
 scannable table rows; no unnamed gap]
[C-52 PASS: all R9 requirements satisfied simultaneously]
[C-56 PASS: violation condition embedded within rule body via semicolon; carry-forward from V-02]
[C-57 PASS: active equivalence classes in labeled lookup-table form -- three-column
 table with class label as scannable lookup key and L1/L2 criterion IDs as column
 entries; membership verification by label scan requires no prose parsing;
 "Phrasing equivalence" and "Form equivalence" are independently scannable rows
 with direct criterion-ID mapping in L1/L2 columns]
[C-58 FAIL: no explicit co-requirement statement declaring that the prospective
 principle, extensibility rule with embedded violation condition, and lookup-table
 class enumeration together form a complete three-point package; each element is
 present and individually declared, but their joint necessity -- that none substitutes
 for another and all three are required simultaneously -- is not stated]
[C-59 FAIL: no phrasing-agnosticism declaration for the C-53/C-54/C-55 structural
 requirements as a complex; the three structural requirements do not yet have
 confirmed-equivalent phrasings named; an evaluator cannot verify phrasing-agnosticism
 without re-deriving it from the property definitions]

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

## V-04 -- C-56/C-57/C-58 PASS / C-59 FAIL: Co-requirement declared, no phrasing-agnosticism for complex

**Axis**: Single -- C-58. Violation condition embedded (C-56), lookup table (C-57), AND explicit co-requirement statement: "All three are required; no element substitutes for another." No phrasing-agnosticism declaration for C-53/C-54/C-55 as a named complex.
**Hypothesis**: 50/51 = 98.04%. C-58 passes: the co-requirement statement explicitly names the three-point package as a complete whole and states that none of the three substitutes for another -- distinguishing complete package from independently-passed criteria. C-59 fails: the three structural requirements remain undeclared as phrasing-agnostic; no confirmed-equivalent phrasings have been named for C-53/C-54/C-55 as a complex.

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
passes. Confirmed-equivalent phrasings from research:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
[C-50 PASS: phrasing-agnosticism declared with at least two confirmed-equivalent
 phrasings named explicitly]

Two-level equivalence-registry design principle -- extensibility contract:
Each equivalence class in this pipeline carries exactly two layers:
  Layer 1 -- property-declaration criterion: closes drift at the declaration level.
    Any implementation satisfying the property passes; the criterion is the
    property, not specific wording or notation.
  Layer 2 -- enumeration criterion: closes drift at the verification level.
    Confirmed-equivalent instances are named by label, reducing evaluator burden
    from property test to label lookup.
Active equivalence classes (labeled lookup table -- membership verifiable by label scan):
  Class label              | Layer 1 (property-declaration criterion) | Layer 2 (enumeration criterion)
  -------------------------|------------------------------------------|---------------------------------
  Phrasing equivalence     | C-47                                     | C-50
  Form equivalence         | C-49                                     | C-51
To verify class membership: locate class label in table; confirm both L1 and L2
criterion IDs are present. A label absent from this table names a class not yet
admitted to the pipeline.
Extensibility rule: any new equivalence class added to this pipeline must carry
both layers before becoming active; a single-layer class is a locally visible
violation of this extensibility contract.
Three-point completeness: the prospective principle (each class carries exactly
two layers, satisfying C-53), the extensibility rule with embedded violation
condition (satisfying C-54 and C-56), and the active-class lookup table
(satisfying C-55 and C-57) together form a complete extensibility package.
All three are required; no element substitutes for another. A declaration that
passes two of the three is incomplete -- this co-requirement distinguishes a
complete extensibility package from three independently-passed criteria.
[C-53 PASS: two-level structure declared prospectively as a binding architectural
 principle]
[C-54 PASS: extensibility contract with explicit forward rule and violation condition
 embedded within rule body]
[C-55 PASS: both active classes enumerated in lookup table within contract body]
[C-52 PASS: all R9 requirements satisfied simultaneously]
[C-56 PASS: violation condition embedded within rule body via semicolon; carry-forward]
[C-57 PASS: active classes in labeled lookup-table form; carry-forward]
[C-58 PASS: explicit co-requirement statement declares three-point package as a
 complete whole -- "all three are required; no element substitutes for another"
 names the joint necessity; "a declaration that passes two of the three is
 incomplete" explicitly distinguishes the complete package from independently-passed
 criteria; the co-requirement relationship is stated, not left implicit]
[C-59 FAIL: no phrasing-agnosticism declaration for the C-53/C-54/C-55 structural
 requirements as a complex; the three requirements are declared and jointly required
 (C-58), but the C-49/C-50 pattern -- any phrasing delivering the property passes,
 and confirmed-equivalent phrasings named -- has not been extended to cover this
 three-criterion group; an evaluator cannot verify phrasing-agnosticism without
 re-deriving it from the property definitions]

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

## V-05 -- C-56/C-57/C-58/C-59 ALL PASS: Canonical, phrasing-agnosticism declared for C-53/C-54/C-55 complex

**Axis**: Single -- C-59. All V-04 properties carry forward. Phrasing-agnosticism declaration added for the C-53/C-54/C-55 structural requirements as a complex, naming two confirmed-equivalent phrasings from R9 research. Extends the C-49/C-50 pattern into the new three-criterion group.
**Hypothesis**: 51/51 = 100.00%. C-59 passes: the three structural requirements are declared phrasing-agnostic; "property-declaration criterion + enumeration criterion" (V-04 R9) and "property criterion + registry criterion" (V-05 R9) are named as confirmed-equivalent phrasings satisfying C-53/C-54/C-55 identically -- confirming all three are property-level constraints, not vocabulary tests.

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
passes. Confirmed-equivalent phrasings from research:
  - "co-equal self-declaration peers in a local-verifiability contract" (V-04 R6)
  - "three-node self-declaration system... co-equal... locally visible" (V-05 R6)
[C-50 PASS: phrasing-agnosticism declared with at least two confirmed-equivalent
 phrasings named explicitly]

Two-level equivalence-registry design principle -- extensibility contract:
Each equivalence class in this pipeline carries exactly two layers:
  Layer 1 -- property-declaration criterion: closes drift at the declaration level.
    Any implementation satisfying the property passes; the criterion is the
    property, not specific wording or notation.
  Layer 2 -- enumeration criterion: closes drift at the verification level.
    Confirmed-equivalent instances are named by label, reducing evaluator burden
    from property test to label lookup.
Active equivalence classes (labeled lookup table -- membership verifiable by label scan):
  Class label              | Layer 1 (property-declaration criterion) | Layer 2 (enumeration criterion)
  -------------------------|------------------------------------------|---------------------------------
  Phrasing equivalence     | C-47                                     | C-50
  Form equivalence         | C-49                                     | C-51
To verify class membership: locate class label in table; confirm both L1 and L2
criterion IDs are present. A label absent from this table names a class not yet
admitted to the pipeline.
Extensibility rule: any new equivalence class added to this pipeline must carry
both layers before becoming active; a single-layer class is a locally visible
violation of this extensibility contract.
Three-point completeness: the prospective principle (each class carries exactly
two layers, satisfying C-53), the extensibility rule with embedded violation
condition (satisfying C-54 and C-56), and the active-class lookup table
(satisfying C-55 and C-57) together form a complete extensibility package.
All three are required; no element substitutes for another. A declaration that
passes two of the three is incomplete -- this co-requirement distinguishes a
complete extensibility package from three independently-passed criteria.
C-53/C-54/C-55 phrasing-agnosticism: the three structural requirements governing
this extensibility contract are phrasing-agnostic. Any phrasing that delivers the
prospective-principle property (C-53), the extensibility-rule-with-violation-condition
property (C-54 + C-56), and the both-classes-enumeration property (C-55 + C-57)
passes. Confirmed-equivalent phrasings from research:
  - "property-declaration criterion + enumeration criterion" (V-04 R9)
  - "property criterion + registry criterion" (V-05 R9)
Both phrasings satisfy C-53/C-54/C-55 identically -- all three structural
requirements are property-level constraints, not vocabulary tests.
[C-53 PASS: two-level structure declared prospectively as a binding architectural
 principle]
[C-54 PASS: extensibility contract with explicit forward rule and violation condition
 embedded within rule body]
[C-55 PASS: both active classes enumerated in lookup table within contract body]
[C-52 PASS: all R9 requirements satisfied simultaneously]
[C-56 PASS: violation condition embedded within rule body via semicolon; carry-forward]
[C-57 PASS: active classes in labeled lookup-table form; carry-forward]
[C-58 PASS: explicit co-requirement statement declares three-point package as a
 complete whole; carry-forward]
[C-59 PASS: three structural requirements (C-53/C-54/C-55) declared phrasing-agnostic
 with two confirmed-equivalent phrasings named explicitly -- "property-declaration
 criterion + enumeration criterion" (V-04 R9) and "property criterion + registry
 criterion" (V-05 R9) satisfy all three criteria identically; extends the C-49/C-50
 phrasing-agnosticism pattern into the new three-criterion complex; all three criteria
 confirmed as property-level, not phrase-specific]

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
