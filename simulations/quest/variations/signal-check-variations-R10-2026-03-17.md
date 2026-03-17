`signal-check-variations-R10-2026-03-17.md` written — 5 complete variations.

**What's in R10:**

| V | Axis | C-27 | C-28 | C-29 |
|---|------|------|------|------|
| V-01 | C-29 only (drift binary + STEP D) | PASS | FAIL | YES |
| V-02 | C-28 only (STEP 3 per-input upgrade) | PASS | YES | FAIL |
| V-03 | C-28 + C-29 combined, advisory | PASS | YES | YES |
| V-04 | All three, advisory canonical | PASS | YES | YES |
| V-05 | All three, imperative | PASS (exception) | YES | YES |

**Key structural additions over R9 V-04:**

- **C-29**: Each STEP C dimension observation closes with `STEP C drift: [CLOSED/OPEN + reason]`. STEP D opens with five per-input consumption annotations (Root pattern + four drift binaries), then assembles a drift summary table before confirming or revising the readiness label.
- **C-28**: STEP 3's grouped `"Required inputs -- consume by label, do not re-derive from prose: [list]"` is replaced with four independent `"Required input -- do not re-derive: [specific label]"` lines in V-02/V-03/V-04.
- **C-27**: ARCHITECTURE table gains four drift binary rows in V-01/V-03/V-04/V-05, completing the nine-row declaration for the full R10 pipeline.

**R10 research questions isolate the three remaining gaps**: whether drift binaries actually close an inferential gap that prose contribution notes leave open (C-29), whether per-input STEP 3 prohibition catches real partial compliance that grouped form misses (C-28), and whether adding drift binary rows to the ARCHITECTURE table satisfies C-27's pre-execution auditability at the new pipeline scope.
t STEP D currently spans by prose inference?
2. Does upgrading STEP 3's grouped prohibition to per-input form close the partial-compliance gap -- i.e., can a model comply at the step level while re-deriving one of four inputs under the grouped form?
3. Do the drift binary rows in the ARCHITECTURE table make the C-29 dataflow contract independently auditable before execution -- or does the production-site annotation already provide sufficient constraint?

---

## V-01 -- Single Axis: C-29 (STEP C Drift Binary + STEP D Consumption)

**Axis**: Lifecycle emphasis -- each STEP C dimension observation closes with a named binary
(`STEP C drift: CLOSED/OPEN`); STEP D consumes all four drift binaries by label before
confirming readiness
**Base**: R9 V-04 with ARCHITECTURE table updated to declare drift binary rows
**C-28 status**: FAIL -- STEP 3 retains R9 V-04's grouped annotation to isolate C-29
**Hypothesis**: C-24 extended into STEP C per-dimension names whether each dimension
contributed to the Root pattern. But contribution notes are prose -- STEP D cannot
structurally consume them. A named binary per dimension creates a consumable artifact:
`STEP C drift: CLOSED` when dimension coaching aligns with the STEP 3 Root pattern
label; `STEP C drift: OPEN` when it diverges or cannot confirm. STEP D then consumes
each binary by label rather than re-inferring readiness from coaching prose. The bet:
this closes the final open gap in the C-23/C-24 chain -- from STEP 3 synthesis through
per-dimension coaching back to confirmed readiness -- as a structural constraint rather
than an advisory inference.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

| Named Output                                | Produced by             | Consumed by                                                              |
|---------------------------------------------|-------------------------|--------------------------------------------------------------------------|
| [MECHANISM VERDICT]                         | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                            |
| Pre-specification gap: YES/NO               | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                     |
| Mechanism-relevant contradiction: YES/NO    | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                    |
| Mechanism-stale: YES/NO                     | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                    |
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name)|
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                 |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                 |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                 |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                 |

Consuming steps reference named outputs by the exact label above.
Each consuming step carries: "Required input -- do not re-derive: [label]"

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; state explicitly; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim.
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
8. STEP 3 closes with: Root pattern: [SHORT NAME]. PART 2 STEP B, STEP C per-dimension,
   and STEP D all consume by name.
9. PART 2 STEP C each dimension closes with a named drift binary:
   STEP C drift: [CLOSED -- dimension coaching aligns with Root pattern "[label]" /
   OPEN -- dimension coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
   PART 2 STEP D consumes each drift binary by label before confirming readiness.

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
  would populate the pool (e.g., competitor signals from scout, benchmark evidence
  from prove, usage data from listen). Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence in this pool for the pathway from {{topic}} to its claimed
  outcome, specifically better than the status-quo alternative? State: present /
  partial / absent. Name what is there and what is missing. Do not restate the
  hypothesis.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read the ordering through the mechanism lens: did the inertia-relevant pool artifacts
appear in the discovery phase, or did the team specify before the mechanism evidence
existed? If verdict is partial or absent: was the gap present before specification,
or did it emerge after?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before the earliest spec artifact;
  cite the spec artifact and the first artifact (or absence) establishing the gap /
  NO -- mechanism evidence was present when the team committed to a spec; any remaining
  gaps emerged after that commitment]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive. Reference by label.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether it is mechanism-relevant (involves an inertia-pool artifact or directly
weakens the mechanism verdict).
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- [name the specific contradiction and the
  inertia-pool artifact involved; explain how this weakens the mechanism verdict] /
  NO -- no contradiction involves inertia-pool signals; contradictions are peripheral]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive. Reference by label.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Artifacts inside / outside the window?
Inertia-pool artifacts: evaluate each -- the mechanism comparison is only as fresh
as the most recent inertia-pool artifact.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- [name inertia-pool artifact(s) outside threshold; state days
  elapsed since last update; the mechanism comparison is at risk of being outdated] /
  NO -- all inertia-pool artifacts are within the threshold; comparison is current]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive. Reference by label.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required inputs -- consume by label, do not re-derive from prose:
  Pre-specification gap: [paste label from SEQUENCE]
  Mechanism-relevant contradiction: [paste label from COHERENCE]
  Mechanism-stale: [paste label from STALENESS]
  Pool status: [empty / thin / adequate -- from CAUSAL GAP]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
<- PART 2 STEP B: Required input -- do not re-derive. Reference by label.
<- PART 2 STEP C per-dimension: Required input -- do not re-derive. Reference by label.
<- PART 2 STEP D: Required input -- do not re-derive. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence is present, status-quo comparison is addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution, then close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag -- pool status did not drive the named root]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Pre-specification gap label; if YES: "discovery closed before mechanism
  evidence existed"; if NO: gap is development-phase.
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label from STEP 3]"
    / SEQUENCE is an isolated flag -- pre-spec status did not drive the named root]
  STEP C drift: [CLOSED -- SEQUENCE coaching aligns with Root pattern "[label]" /
    OPEN -- SEQUENCE coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-relevant contradiction label; if YES: name the contradiction and
  why it matters for the inertia case; if NO: contradictions are peripheral.
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label from STEP 3]"
    / COHERENCE is an isolated flag -- contradiction status did not drive the named root]
  STEP C drift: [CLOSED -- COHERENCE coaching aligns with Root pattern "[label]" /
    OPEN -- COHERENCE coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-stale label; if YES: name stale inertia-pool artifacts, comparison
  at risk; if NO: comparison is current.
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label from STEP 3]"
    / STALENESS is an isolated flag -- mechanism-stale status did not drive the named root]
  STEP C drift: [CLOSED -- STALENESS coaching aligns with Root pattern "[label]" /
    OPEN -- STALENESS coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP
Required input -- do not re-derive: STEP C drift -- SEQUENCE
Required input -- do not re-derive: STEP C drift -- COHERENCE
Required input -- do not re-derive: STEP C drift -- STALENESS

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed the Root pattern without divergence.
If any OPEN: name the dimension(s) and reason for divergence.

Return to STEP B. Does the drift summary confirm or change your read?
Label: [CONFIRMED -- Root pattern: [name] holds; all STEP C drift: CLOSED]
  or [REVISED -- dimension(s) [list] OPEN; updated root: [new label] -- reason: ...]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-02 -- Single Axis: C-28 (STEP 3 Per-Input Prohibition Upgrade)

**Axis**: Lifecycle emphasis -- upgrade STEP 3's grouped "Required inputs -- consume by
label, do not re-derive from prose: [list]" to four independent per-input annotations
**Base**: R9 V-04 with STEP 3 rewritten; all other structure unchanged
**C-29 status**: FAIL -- no drift binaries added
**Hypothesis**: R9 V-04's STEP 3 uses a single grouped prohibition covering four named
inputs. C-28 requires each reference to carry its own independent annotation. The gap:
a model can appear compliant at the step level while re-deriving one of the four inputs
without a locally visible violation. Per-input annotations make partial compliance
impossible -- each specific re-derivation is immediately identifiable at the consumption
site. The bet: even when the ARCHITECTURE table (C-27) declares the consuming
relationship upfront, per-input prohibition at STEP 3 closes a real execution-time gap
that grouped form leaves open.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

| Named Output                            | Produced by  | Consumed by                                                              |
|-----------------------------------------|--------------|--------------------------------------------------------------------------|
| [MECHANISM VERDICT]                     | CAUSAL GAP   | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                            |
| Pre-specification gap: YES/NO           | SEQUENCE     | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                     |
| Mechanism-relevant contradiction: YES/NO| COHERENCE    | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                    |
| Mechanism-stale: YES/NO                 | STALENESS    | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                    |
| Root pattern: [label]                   | STEP 3       | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name)|

Consuming steps reference named outputs by the exact label above.
Each consuming step carries: "Required input -- do not re-derive: [label]"

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; state explicitly; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim.
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
8. STEP 3 closes with: Root pattern: [SHORT NAME]. PART 2 STEP B, STEP C per-dimension,
   and STEP D all consume by name.

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
  would populate the pool (e.g., competitor signals from scout, benchmark evidence
  from prove, usage data from listen). Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence in this pool for the pathway from {{topic}} to its claimed
  outcome, specifically better than the status-quo alternative? State: present /
  partial / absent. Name what is there and what is missing. Do not restate the
  hypothesis.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read the ordering through the mechanism lens: did the inertia-relevant pool artifacts
appear in the discovery phase, or did the team specify before the mechanism evidence
existed? If verdict is partial or absent: was the gap present before specification,
or did it emerge after?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before the earliest spec artifact;
  cite the spec artifact and the first artifact (or absence) establishing the gap /
  NO -- mechanism evidence was present when the team committed to a spec; any remaining
  gaps emerged after that commitment]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive. Reference by label.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether it is mechanism-relevant (involves an inertia-pool artifact or directly
weakens the mechanism verdict).
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- [name the specific contradiction and the
  inertia-pool artifact involved; explain how this weakens the mechanism verdict] /
  NO -- no contradiction involves inertia-pool signals; contradictions are peripheral]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive. Reference by label.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Artifacts inside / outside the window?
Inertia-pool artifacts: evaluate each -- the mechanism comparison is only as fresh
as the most recent inertia-pool artifact.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- [name inertia-pool artifact(s) outside threshold; state days
  elapsed since last update; the mechanism comparison is at risk of being outdated] /
  NO -- all inertia-pool artifacts are within the threshold; comparison is current]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive. Reference by label.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
<- PART 2 STEP B: Required input -- do not re-derive. Reference by label.
<- PART 2 STEP C per-dimension: Required input -- do not re-derive. Reference by label.
<- PART 2 STEP D: Required input -- do not re-derive. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence is present, status-quo comparison is addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~310 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state whether the dimension contributed to Root pattern or is isolated.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag -- pool status did not drive the named root]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Pre-specification gap label; if YES: "discovery closed before mechanism
  evidence existed"; if NO: gap is development-phase.
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label from STEP 3]"
    / SEQUENCE is an isolated flag -- pre-spec status did not drive the named root]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-relevant contradiction label; if YES: name the contradiction and
  why it matters for the inertia case; if NO: contradictions are peripheral.
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label from STEP 3]"
    / COHERENCE is an isolated flag -- contradiction status did not drive the named root]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-stale label; if YES: name stale inertia-pool artifacts, comparison
  at risk; if NO: comparison is current.
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label from STEP 3]"
    / STALENESS is an isolated flag -- mechanism-stale status did not drive the named root]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

Return to STEP B. Does the dimension analysis confirm or change your read?
Do the per-dimension Root pattern contributions in STEP C validate the named root
as the central coaching message -- or reveal a characterization that should change?
Label: [CONFIRMED -- Root pattern: [name] holds] or [REVISED -- updated root
characterization: [new label] -- reason: ...]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-03 -- Combined: C-28 + C-29, Advisory (STEP 3 Per-Input + Drift Binaries)

**Axes**: C-28 (STEP 3 per-input prohibition) + C-29 (STEP C drift binary + STEP D
consumption); ARCHITECTURE table updated with drift binary rows
**Hypothesis**: V-01 establishes drift binaries close the coaching-to-readiness chain.
V-02 establishes per-input prohibition closes STEP 3 partial compliance. Combined: the
chain from dimension analysis through STEP 3 synthesis through STEP C coaching to STEP D
confirmation is structurally complete at every handoff. The ARCHITECTURE table updates
to declare drift binary outputs, ensuring C-27 covers the full R10 pipeline.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

| Named Output                                | Produced by             | Consumed by                                                              |
|---------------------------------------------|-------------------------|--------------------------------------------------------------------------|
| [MECHANISM VERDICT]                         | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                            |
| Pre-specification gap: YES/NO               | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                     |
| Mechanism-relevant contradiction: YES/NO    | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                    |
| Mechanism-stale: YES/NO                     | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                    |
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name)|
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                 |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                 |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                 |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                 |

Consuming steps reference named outputs by the exact label above.
Each consuming step carries: "Required input -- do not re-derive: [label]"

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; state explicitly; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim.
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
8. STEP 3 closes with: Root pattern: [SHORT NAME]. PART 2 STEP B, STEP C per-dimension,
   and STEP D all consume by name.
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   consumes each by label before confirming readiness.

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
  Is there evidence in this pool for the pathway from {{topic}} to its claimed
  outcome, specifically better than the status-quo alternative? State: present /
  partial / absent. Name what is there and what is missing. Do not restate the
  hypothesis.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates. Did discovery precede specification?
Read the ordering through the mechanism lens: did the inertia-relevant pool artifacts
appear in the discovery phase, or did the team specify before the mechanism evidence
existed? If verdict is partial or absent: was the gap present before specification,
or did it emerge after?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before the earliest spec artifact;
  cite the spec artifact and the first artifact (or absence) establishing the gap /
  NO -- mechanism evidence was present when the team committed to a spec; any remaining
  gaps emerged after that commitment]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive. Reference by label.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether it is mechanism-relevant (involves an inertia-pool artifact or directly
weakens the mechanism verdict).
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- [name the specific contradiction and the
  inertia-pool artifact involved; explain how this weakens the mechanism verdict] /
  NO -- no contradiction involves inertia-pool signals; contradictions are peripheral]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive. Reference by label.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Artifacts inside / outside the window?
Inertia-pool artifacts: evaluate each -- the mechanism comparison is only as fresh
as the most recent inertia-pool artifact.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- [name inertia-pool artifact(s) outside threshold; state days
  elapsed since last update; the mechanism comparison is at risk of being outdated] /
  NO -- all inertia-pool artifacts are within the threshold; comparison is current]
<- STEP 3: Required input -- do not re-derive. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive. Reference by label.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
<- PART 2 STEP B: Required input -- do not re-derive. Reference by label.
<- PART 2 STEP C per-dimension: Required input -- do not re-derive. Reference by label.
<- PART 2 STEP D: Required input -- do not re-derive. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence is present, status-quo comparison is addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag -- pool status did not drive the named root]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Pre-specification gap label; if YES: "discovery closed before mechanism
  evidence existed"; if NO: gap is development-phase.
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label from STEP 3]"
    / SEQUENCE is an isolated flag -- pre-spec status did not drive the named root]
  STEP C drift: [CLOSED -- SEQUENCE coaching aligns with Root pattern "[label]" /
    OPEN -- SEQUENCE coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-relevant contradiction label; if YES: name the contradiction and
  why it matters for the inertia case; if NO: contradictions are peripheral.
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label from STEP 3]"
    / COHERENCE is an isolated flag -- contradiction status did not drive the named root]
  STEP C drift: [CLOSED -- COHERENCE coaching aligns with Root pattern "[label]" /
    OPEN -- COHERENCE coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-stale label; if YES: name stale inertia-pool artifacts, comparison
  at risk; if NO: comparison is current.
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label from STEP 3]"
    / STALENESS is an isolated flag -- mechanism-stale status did not drive the named root]
  STEP C drift: [CLOSED -- STALENESS coaching aligns with Root pattern "[label]" /
    OPEN -- STALENESS coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP
Required input -- do not re-derive: STEP C drift -- SEQUENCE
Required input -- do not re-derive: STEP C drift -- COHERENCE
Required input -- do not re-derive: STEP C drift -- STALENESS

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed the Root pattern without divergence.
If any OPEN: name the dimension(s) and reason for divergence.

Return to STEP B. Does the drift summary confirm or change your read?
Label: [CONFIRMED -- Root pattern: [name] holds; all STEP C drift: CLOSED]
  or [REVISED -- dimension(s) [list] OPEN; updated root: [new label] -- reason: ...]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-04 -- All Three Combined: C-27 + C-28 + C-29, Advisory Register (Canonical)

**Axes**: C-27 (nine-row ARCHITECTURE table confirmed as minimal implementation for full
R10 pipeline) + C-28 (per-input prohibition at every consuming step, named explicitly
per input at production-site arrows) + C-29 (STEP C drift binary per-dimension + STEP D
per-input consumption), advisory register
**Hypothesis**: V-03 combines C-28 and C-29. V-04 is the canonical form: production-site
arrows carry per-input names, STEP 3 per-input annotations each name the specific
input, and STEP D per-input drift consumption is maximally explicit. The ARCHITECTURE
table declares all nine named outputs. This is the recommended golden advisory form for
R10 -- complete chain at lowest overhead.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

| Named Output                                | Produced by             | Consumed by                                                              |
|---------------------------------------------|-------------------------|--------------------------------------------------------------------------|
| [MECHANISM VERDICT]                         | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                            |
| Pre-specification gap: YES/NO               | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                     |
| Mechanism-relevant contradiction: YES/NO    | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                    |
| Mechanism-stale: YES/NO                     | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                    |
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name)|
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                 |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                 |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                 |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                 |

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; state explicitly; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim.
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
   STEP 3 and PART 2 STEP C consume this label by name.
8. STEP 3 closes with: Root pattern: [SHORT NAME]. PART 2 STEP B, STEP C per-dimension,
   and STEP D all consume by name.
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all four drift binaries by label -- one per-input annotation each.

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
  would populate the pool (e.g., competitor signals from scout, benchmark evidence
  from prove, usage data from listen). Do not draw on non-pool artifacts.

If pool is NON-EMPTY:
  Is there evidence in this pool for the pathway from {{topic}} to its claimed
  outcome, specifically better than the status-quo alternative? State: present /
  partial / absent. Name what is there and what is missing. Do not restate the
  hypothesis.

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
Read the ordering through the mechanism lens: did the inertia-relevant pool artifacts
appear in the discovery phase, or did the team specify before the mechanism evidence
existed? If verdict is partial or absent: was the gap present before specification,
or did it emerge after?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before the earliest spec artifact;
  cite the spec artifact and the first artifact (or absence) establishing the gap /
  NO -- mechanism evidence was present when the team committed to a spec; any remaining
  gaps emerged after that commitment]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether it is mechanism-relevant (involves an inertia-pool artifact or directly
weakens the mechanism verdict).
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- [name the specific contradiction and the
  inertia-pool artifact involved; explain how this weakens the mechanism verdict] /
  NO -- no contradiction involves inertia-pool signals; contradictions are peripheral]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Artifacts inside / outside the window?
Inertia-pool artifacts: evaluate each -- the mechanism comparison is only as fresh
as the most recent inertia-pool artifact.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- [name inertia-pool artifact(s) outside threshold; state days
  elapsed since last update; the mechanism comparison is at risk of being outdated] /
  NO -- all inertia-pool artifacts are within the threshold; comparison is current]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]

From these named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
<- PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.
<- PART 2 STEP C per-dimension: Required input -- do not re-derive: Root pattern.
<- PART 2 STEP D: Required input -- do not re-derive: Root pattern. Reference by label.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1 -- paste verbatim]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence is present, status-quo comparison is addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag -- pool status did not drive the named root]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Pre-specification gap label; if YES: "discovery closed before mechanism
  evidence existed"; if NO: gap is development-phase.
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label from STEP 3]"
    / SEQUENCE is an isolated flag -- pre-spec status did not drive the named root]
  STEP C drift: [CLOSED -- SEQUENCE coaching aligns with Root pattern "[label]" /
    OPEN -- SEQUENCE coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-relevant contradiction label; if YES: name the contradiction and
  why it matters for the inertia case; if NO: contradictions are peripheral.
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label from STEP 3]"
    / COHERENCE is an isolated flag -- contradiction status did not drive the named root]
  STEP C drift: [CLOSED -- COHERENCE coaching aligns with Root pattern "[label]" /
    OPEN -- COHERENCE coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Reference Mechanism-stale label; if YES: name stale inertia-pool artifacts, comparison
  at risk; if NO: comparison is current.
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label from STEP 3]"
    / STALENESS is an isolated flag -- mechanism-stale status did not drive the named root]
  STEP C drift: [CLOSED -- STALENESS coaching aligns with Root pattern "[label]" /
    OPEN -- STALENESS coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP
Required input -- do not re-derive: STEP C drift -- SEQUENCE
Required input -- do not re-derive: STEP C drift -- COHERENCE
Required input -- do not re-derive: STEP C drift -- STALENESS

Drift summary (consume each from STEP C labels above -- do not re-infer from prose):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

If all CLOSED: per-dimension coaching confirmed the Root pattern without divergence.
If any OPEN: name the dimension(s) and reason for divergence.

Return to STEP B. Does the drift summary confirm or change your read?
Label: [CONFIRMED -- Root pattern: [name] holds; all STEP C drift: CLOSED]
  or [REVISED -- dimension(s) [list] OPEN; updated root: [new label] -- reason: ...]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-05 -- All Three Combined: C-27 + C-28 + C-29, Imperative Register

**Axes**: All three R10 axes on imperative register -- ARCHITECTURE schema extended with
drift binary outputs (C-27: PASS via imperative exception); per-input prohibition
throughout including STEP D drift consumption (C-28: PASS); STEP C drift binary per-
dimension emitted and consumed by STEP D per-input (C-29: PASS)
**Base**: R9 V-05 with C-29 added
**Hypothesis**: R9 V-05 was the strongest individual-criterion implementation. Adding
C-29 closes the final structural gap: STEP C dimension coaching emits a consumable
binary rather than prose contribution notes. STEP D consumes the four drift binaries
with per-input annotations, making the drift consumption as structurally precise as
STEP 3's per-input consumption of dimension binaries. This is the highest-precision
form; V-04 (advisory) is preferred for lower overhead.

---

```markdown
Signal integrity check -- {{topic}}.
Run these steps in order. Each step has a required output. Do not skip.

REGISTER RULE: Two numbered registers.
  REGISTER 1 (ANALYSIS): steps 0-3. Internal. Include severity ratings. Do not show to team.
  REGISTER 2 (COACHING): steps A-D. Advisory. No severity ratings or scores visible.

ARCHITECTURE: Named-output pipeline -- all outputs and consuming steps declared before
analysis runs. Each consuming step carries per-input "Required input -- do not re-derive"
annotation independently for each named input it consumes.

  Named outputs produced:
  [MECHANISM VERDICT]                      produced by: step 2a (CAUSAL GAP)
  Pre-specification gap: YES/NO            produced by: step 2b (SEQUENCE)
  Mechanism-relevant cont.: YES/NO         produced by: step 2c (COHERENCE)
  Mechanism-stale: YES/NO                  produced by: step 2d (STALENESS)
  Root pattern: [label]                    produced by: step 3  (CROSS-DIMENSION)
  STEP C drift -- CAUSAL GAP: CLOSED/OPEN  produced by: step C  (CAUSAL GAP observation)
  STEP C drift -- SEQUENCE: CLOSED/OPEN    produced by: step C  (SEQUENCE observation)
  STEP C drift -- COHERENCE: CLOSED/OPEN   produced by: step C  (COHERENCE observation)
  STEP C drift -- STALENESS: CLOSED/OPEN   produced by: step C  (STALENESS observation)

  Consuming steps and required inputs (each listed as independent annotation):
  step 2b:  [MECHANISM VERDICT]
  step 3:   Pre-specification gap
            Mechanism-relevant contradiction
            Mechanism-stale
  step A:   [MECHANISM VERDICT]
  step B:   Root pattern
  step C:   Pre-specification gap         (SEQUENCE coaching)
            Mechanism-relevant contradiction (COHERENCE coaching)
            Mechanism-stale               (STALENESS coaching)
            Root pattern                  (all four per-dimension contribution notes)
  step D:   Root pattern
            STEP C drift -- CAUSAL GAP
            STEP C drift -- SEQUENCE
            STEP C drift -- COHERENCE
            STEP C drift -- STALENESS

=======================================================
REGISTER 1 -- ANALYSIS  (internal only)
=======================================================

--- STEP 0: INERTIA ANCHOR (~30 words) ---

1. State what the team does today if {{topic}} does not ship.
2. Emit: Inertia competitor: [one sentence description]

--- STEP 1: ARTIFACT INVENTORY (~150 words) ---

1. List all signal artifacts for {{topic}} in a table:
   | Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
   Tag "Inertia Relevant?" yes if the artifact speaks to: competitors, benchmarks,
   usage data, or mechanism evidence comparing {{topic}} to the inertia competitor.

2. List empty namespaces (scout, draft, review, flow, trace, prove, listen, program,
   topic). For each: state "expected gap" or "meaningful blind spot."

3. Count inertia-relevant artifacts.
   Emit:
   Inertia-relevant count: [N]
   Staleness threshold: [14 days if N >= 1 / 30 days if N = 0]

--- STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST (~540 words) ---

Run in order: 2a -> 2b -> 2c -> 2d.

### 2a: CAUSAL GAP

1. List inertia-relevant artifacts (from step 1 column):
   Inertia-relevant pool: [artifact names, or "empty"]

2. Branch on pool status:
   IF pool is EMPTY:
     a. State: "Mechanism verdict is absent by default -- no inertia-relevant artifacts."
     b. Name artifact types that would populate the pool.
     c. Do not evaluate mechanism from non-pool artifacts.
   IF pool is NON-EMPTY:
     a. Evaluate: does the pool contain evidence that {{topic}} produces better outcomes
        than the inertia competitor? State: present / partial / absent.
     b. Name what is present and what is missing. Do not restate the hypothesis.

3. Emit severity (internal only): (internal: green / yellow / red)
4. Emit coaching observation: Observation: ...
5. If yellow or red, emit: Next action: [one concrete action]

6. Required output -- emit verbatim:
   [MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
   step 2b: Required input -- do not re-derive: [MECHANISM VERDICT]
   step A:  Required input -- do not re-derive: [MECHANISM VERDICT]

### 2b: SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[paste [MECHANISM VERDICT] from step 2a exactly]"

1. Cite 2+ artifacts with dates.
2. Determine: did discovery phase artifacts appear before the earliest spec artifact?
3. Apply mechanism lens: did inertia-relevant pool artifacts appear in discovery --
   or did the team commit to a spec before that evidence existed?
4. If verdict is partial or absent: was the gap already present at spec time, or did
   it emerge after?

5. Emit severity: (internal: green / yellow / red)
6. Emit: Observation: ...
7. If yellow or red: Next action: [one concrete action]

8. Required output -- emit exactly:
   Pre-specification gap: [YES -- [name spec artifact and date; name first artifact or
     absence establishing the gap before that date] /
     NO -- [confirm mechanism evidence was present at spec commitment; note when gaps emerged]]
   step 3:          Required input -- do not re-derive: Pre-specification gap
   step C SEQUENCE: Required input -- do not re-derive: Pre-specification gap

### 2c: COHERENCE

1. Identify 2+ signals compared on a specific claim.
2. State for each pair: aligned / contradicting / inconclusive.
3. For each contradiction: name both signals, state the specific disagreement.
4. For each contradiction: tag -- does it involve an inertia-pool artifact, or directly
   weaken [MECHANISM VERDICT]?

5. Emit severity: (internal: green / yellow / red)
6. Emit: Observation: ...
7. If yellow or red: Next action: [one concrete action]

8. Required output -- emit exactly:
   Mechanism-relevant contradiction: [YES -- [name the contradiction; name the
     inertia-pool artifact or mechanism link weakened; one sentence on impact] /
     NO -- no contradiction involves inertia-pool signals; contradictions are peripheral]
   step 3:           Required input -- do not re-derive: Mechanism-relevant contradiction
   step C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction

### 2d: STALENESS

Required input: Staleness threshold from step 1.

1. For all artifacts: state inside / outside the threshold.
2. Focus on inertia-pool artifacts: the mechanism comparison is only as fresh as the
   most recent inertia-pool artifact update.

3. Emit severity: (internal: green / yellow / red)
4. Emit: Observation: ...
5. If yellow or red: Next action: [one concrete action]

6. Required output -- emit exactly:
   Mechanism-stale: [YES -- [name inertia-pool artifact(s) outside threshold; state days
     since last update; consequence: mechanism comparison may be outdated] /
     NO -- all inertia-pool artifacts within threshold; comparison is current]
   step 3:           Required input -- do not re-derive: Mechanism-stale
   step C STALENESS: Required input -- do not re-derive: Mechanism-stale

--- STEP 3: CROSS-DIMENSION PATTERN (~90 words) ---

Required input -- do not re-derive: Pre-specification gap from step 2b
Required input -- do not re-derive: Mechanism-relevant contradiction from step 2c
Required input -- do not re-derive: Mechanism-stale from step 2d
Pool status: [from step 2a -- empty / thin / adequate]

1. Do 2+ flagged dimensions share a root? Use named inputs -- do not re-derive:
   - Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
   - Mechanism-stale YES + partial/absent verdict -> "Stale mechanism comparison"
   - Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
   - Empty pool -> "Empty inertia pool"
   - Flags present, no shared root -> "Isolated flags"
   - No flags -> "none"

2. Required output -- emit exactly:
   Root pattern: [SHORT NAME from above; do not express the pattern in prose only]
   step B:               Required input -- do not re-derive: Root pattern
   step C per-dimension: Required input -- do not re-derive: Root pattern
   step D:               Required input -- do not re-derive: Root pattern

=======================================================
REGISTER 2 -- COACHING  (advisory -- no severity labels)
=======================================================

--- STEP A: INERTIA CASE STRENGTH (~100 words) ---

Required input -- do not re-derive: [MECHANISM VERDICT] from step 2a
Quoting mechanism verdict: "[paste [MECHANISM VERDICT] from step 2a exactly]"

1. Based on that verdict and the full artifact record, is the case that {{topic}}
   beats doing nothing:
   [ ] Clearly built -- mechanism evidence present; status-quo comparison addressed
   [ ] Partially built -- some evidence exists; name the key gap
   [ ] Still open -- mechanism or comparison not established in artifacts

2. State which applies. If pool was empty: state the inertia case has not been
   established in the artifact record.
3. Name one other artifact (if any) that supports or complicates the judgment.
4. Close: Advisory -- not a gate.

--- STEP B: DRAFT READINESS (~75 words) ---

Required input -- do not re-derive: Root pattern from step 3

1. State which dimensions look clean and which have something worth noticing.
2. If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly.
3. Emit: [DRAFT -- to be confirmed after dimension observations]

--- STEP C: DIMENSION OBSERVATIONS (~340 words) ---

CAUSAL GAP-first. Advisory language. No severity, scores, or gates.
Per-dimension: include Root pattern contribution note and STEP C drift binary.

CAUSAL GAP:
  Observation for team: ...
  Reference pool status: if empty, name artifact types needed; if non-empty, state
  what evidence exists and what is missing for the mechanism case.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label]" /
    CAUSAL GAP is an isolated flag]
  Required output -- emit exactly:
  STEP C drift -- CAUSAL GAP: [CLOSED -- coaching aligns with Root pattern "[label]" /
    OPEN -- coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> Suggested next step: ...

SEQUENCE:
  Observation for team: ...
  Required input -- do not re-derive: Pre-specification gap from step 2b
  Reference Pre-specification gap by label: if YES, frame as "discovery phase closed
  before mechanism evidence existed"; if NO, gap is development-phase.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]" /
    SEQUENCE is an isolated flag]
  Required output -- emit exactly:
  STEP C drift -- SEQUENCE: [CLOSED -- coaching aligns with Root pattern "[label]" /
    OPEN -- coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> Suggested next step: ...

COHERENCE:
  Observation for team: ...
  Required input -- do not re-derive: Mechanism-relevant contradiction from step 2c
  Reference Mechanism-relevant contradiction by label: if YES, name the specific
  contradiction and why it matters for the inertia case; if NO, peripheral.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]" /
    COHERENCE is an isolated flag]
  Required output -- emit exactly:
  STEP C drift -- COHERENCE: [CLOSED -- coaching aligns with Root pattern "[label]" /
    OPEN -- coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> Suggested next step: ...

STALENESS:
  Observation for team: ...
  Required input -- do not re-derive: Mechanism-stale from step 2d
  Reference Mechanism-stale by label: if YES, name the specific inertia-pool
  artifact(s) that are stale; if NO, comparison is current.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]" /
    STALENESS is an isolated flag]
  Required output -- emit exactly:
  STEP C drift -- STALENESS: [CLOSED -- coaching aligns with Root pattern "[label]" /
    OPEN -- coaching diverges from or cannot confirm Root pattern "[label]"; reason: ...]
  If flagged -> Suggested next step: ...

--- STEP D: CONFIRMED READINESS (~90 words) ---

Required input -- do not re-derive: Root pattern from step 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from step C
Required input -- do not re-derive: STEP C drift -- SEQUENCE from step C
Required input -- do not re-derive: STEP C drift -- COHERENCE from step C
Required input -- do not re-derive: STEP C drift -- STALENESS from step C

1. Consume drift binaries from step C labels above -- do not re-infer from prose:
   CAUSAL GAP: [CLOSED / OPEN]
   SEQUENCE:   [CLOSED / OPEN]
   COHERENCE:  [CLOSED / OPEN]
   STALENESS:  [CLOSED / OPEN]

2. If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
   If any OPEN: name the dimension(s) and reason for divergence.

3. Return to STEP B draft. Does the drift summary confirm or change your read?
4. Reference Root pattern by label explicitly.
5. Emit: [CONFIRMED -- Root pattern: [name] holds; all STEP C drift: CLOSED]
   or [REVISED -- dimension(s) [list] OPEN; updated root: [new label] -- reason: ...]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## Variation Map

| V | Single Axis | Combined With | C-27 | C-28 | C-29 | Key Mechanism |
|---|-------------|---------------|------|------|------|---------------|
| V-01 | C-29 drift binary + STEP D | R9 V-04 + ARCHITECTURE updated | PASS | FAIL | YES | Named binary per dimension creates consumable STEP D input; STEP 3 grouped form left intact to isolate C-29 structural gain |
| V-02 | C-28 STEP 3 per-input | R9 V-04 base, no drift binaries | PASS | YES | FAIL | Per-input STEP 3 prohibition closes partial-compliance gap; C-29 absent to isolate |
| V-03 | C-28 + C-29 combined | Advisory register | PASS | YES | YES | Full structural chain: per-input STEP 3 + drift binaries + STEP D consumption; ARCHITECTURE table updated to 9 rows |
| V-04 | All three, canonical | Advisory register | PASS | YES | YES | Production-site arrows named per-input; STEP D per-input drift consumption; canonical advisory form for R10 |
| V-05 | All three | Imperative register | PASS (exception) | YES | YES | R9 V-05 + C-29; schema ARCHITECTURE adds drift binary rows; STEP D per-input consumption per named binary |

**R10 research questions:**
1. Does C-29's `STEP C drift: CLOSED/OPEN` close the coaching-to-readiness structural
   chain -- or does STEP C contribution-note prose already give STEP D enough information
   to confirm readiness without a named binary?
2. Does upgrading STEP 3 from grouped to per-input prohibition close a real execution-
   time partial-compliance gap -- or does the ARCHITECTURE table's upfront declaration
   make per-input STEP 3 redundant when the consuming relationship is already declared?
3. Do the four drift binary rows in the ARCHITECTURE table make the C-29 dataflow
   contract independently auditable before execution -- or is the production-site
   annotation at each STEP C dimension observation sufficient for C-25/C-27?
