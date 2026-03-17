`simulations/quest/variations/signal-check-variations-R9-2026-03-17.md` written.

---

## What R9 delivers

All R8 variations scored 100/Gold. C-24/C-25/C-26 are now locked rubric criteria (denominator 18). R9 propagates them across all five variations.

| V | Axis | C-24 | C-25 | C-26 |
|---|------|------|------|------|
| **V-01** | C-25 ARCHITECTURE table on advisory register | baseline (STEP B, D) | YES (table) | NO |
| **V-02** | C-26 prohibition markers only, no ARCHITECTURE block | baseline (STEP B, D) | NO | YES (per-site) |
| **V-03** | C-24 extended into STEP C per-dimension coaching | extended (STEP B, C, D) | NO | NO |
| **V-04** | All three combined, advisory register | extended | YES (table) | YES (per-site) |
| **V-05** | All three combined, imperative register | extended | YES (schema) | YES (per-input, strengthened) |

**Three R9 research questions:**
1. Does the ARCHITECTURE table (V-01) satisfy C-25 with less overhead than V-05's schema — and does it help the model, not just the auditor?
2. Does per-site prohibition (V-02) close silent re-derivation that structural label consumption doesn't catch?
3. Does C-24 extended into STEP C per-dimension (V-03) close drift between synthesis and coaching — or does STEP B/D already suffice?
-site enforcement alone closes re-derivation |
| **V-03** | C-24 Root pattern consumption extended to STEP C per-dimension | Root pattern label referenced in each individual dimension coaching observation — tests whether per-dimension Root pattern awareness closes drift at the dimension-coaching level |
| **V-04** | All three R9 axes combined, advisory register | Full C-24 (extended) + C-25 (table) + C-26 (per-site prohibition) on advisory register |
| **V-05** | All three R9 axes combined, imperative register | Full C-24 (extended) + C-25 (schema) + C-26 (per-input prohibition) on imperative register |

**Fixed in all 5**: C-15 through C-23 (full locked R8 architecture, including all five
named outputs: MECHANISM VERDICT, Pre-specification gap, Mechanism-relevant contradiction,
Mechanism-stale, Root pattern).

**C-24 baseline in all 5**: STEP 3 emits `Root pattern: [SHORT NAME]`; PART 2 STEP B and
STEP D consume by name. V-03/V-04/V-05 additionally extend consumption into STEP C.

**Three R9 research questions:**
1. Does the ARCHITECTURE table (V-01/V-04/V-05) improve pre-execution auditability over
   per-step label arrows — or does the table primarily help readers, not reduce model
   re-derivation?
2. Does the per-site "Required input — do not re-derive" prohibition (V-02/V-04/V-05)
   reduce silent re-derivation — or does structural label consumption (C-23/C-24) already
   eliminate this without the explicit prohibition?
3. Does Root pattern consumption in STEP C per-dimension (V-03/V-04/V-05) close drift
   between PART 1 synthesis and individual dimension coaching — or does the STEP B/D
   consumption (C-24 baseline) already produce sufficient structural coherence?

---

## V-01 — Single Axis: C-25 ARCHITECTURE Table on Advisory Register

**Axis**: Format — upfront ARCHITECTURE block as a compact named-output table (C-25
minimal implementation on advisory register)
**Hypothesis**: C-25 requires the dataflow contract to be "auditable before execution." R8
V-05 embedded this in a schema preamble tightly coupled to the imperative register. This
variation tests a minimal table-form ARCHITECTURE block placed before PART 1 on the
advisory register — three columns (Named Output | Produced by | Consumed by) that expose
the full named-output pipeline in one scannable surface without changing per-step
instructions. The bet is that the table form satisfies C-25 with lower prompt overhead and
is independently scannable: a reader can verify C-23/C-24 compliance by cross-referencing
the columns without tracing the full analytical chain. No per-site prohibition markers
(C-26) — tests ARCHITECTURE alone.

---

```markdown
Signal-check for {{topic}}.
Advisory — observations the team can decide to act on, not a gate.

ARCHITECTURE — Named-Output Pipeline

| Named Output                            | Produced by  | Consumed by                                                   |
|-----------------------------------------|--------------|---------------------------------------------------------------|
| [MECHANISM VERDICT]                     | CAUSAL GAP   | SEQUENCE (quote verbatim); PART 2 STEP A (quote verbatim)     |
| Pre-specification gap: YES/NO           | SEQUENCE     | STEP 3 (by label); PART 2 STEP C SEQUENCE coaching            |
| Mechanism-relevant contradiction: YES/NO| COHERENCE    | STEP 3 (by label); PART 2 STEP C COHERENCE coaching           |
| Mechanism-stale: YES/NO                 | STALENESS    | STEP 3 (by label); PART 2 STEP C STALENESS coaching           |
| Root pattern: [label]                   | STEP 3       | PART 2 STEP B (by name); PART 2 STEP D (by name)              |

Consuming steps reference named outputs by the exact label in the table above.

Two parts in order. Do not merge.
PART 1 — ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 — TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural — not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
   Empty pool -> verdict absent by default; state explicitly; name what's needed.
   Non-empty pool -> evaluate; state present / partial / absent.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES -- gap existed before earliest spec
   artifact, cite both / NO -- evidence present at spec; gaps emerged after].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section. STEP A
   opens by quoting the MECHANISM VERDICT verbatim -- the inertia case judgment is grounded
   in the analytical record, not independently inferred.
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES -- names which
   contradiction involves inertia-pool signal(s) and how it weakens the verdict /
   NO -- no contradiction affects the mechanism case].
   STEP 3 and PART 2 STEP C consume this label by name.
7. STALENESS closes with: Mechanism-stale: [YES -- names inertia-pool artifact(s)
   outside threshold and days elapsed / NO -- all inertia-pool artifacts current].
   STEP 3 and PART 2 STEP C consume this label by name.
8. STEP 3 closes with: Root pattern: [SHORT NAME]. PART 2 STEP B and STEP D consume
   by name.

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
<- SEQUENCE quotes this line verbatim below.
<- PART 2 STEP A quotes this line verbatim before its inertia case judgment.

### SEQUENCE

Quoting mechanism verdict: "[MECHANISM VERDICT from above]"
Cite 2+ artifacts with dates. Did discovery precede specification?
Read the ordering through the mechanism lens: did the inertia-relevant pool artifacts
appear in the discovery phase, or did the team specify before the mechanism evidence
existed? If verdict is partial or absent: was the gap present before specification,
or did it emerge after? Inertia angle: did discovery validate against the status-quo
alternative before committing to a specification?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES -- mechanism gap existed before the earliest spec artifact;
  cite the spec artifact and the first artifact (or absence) establishing the gap /
  NO -- mechanism evidence was present when the team committed to a spec; any remaining
  gaps emerged after that commitment]
<- STEP 3 references this label by name.
<- PART 2 STEP C references this label when coaching SEQUENCE.

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
<- STEP 3 references this label by name.
<- PART 2 STEP C references this label when coaching COHERENCE.

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
<- STEP 3 references this label by name.
<- PART 2 STEP C references this label when coaching STALENESS.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Do 2+ flagged dimensions share a root? Consume named outputs by label -- do not re-derive.
Consider: Pre-specification gap (SEQUENCE) + Mechanism-relevant contradiction (COHERENCE)
+ Mechanism-stale (STALENESS) + pool status (CAUSAL GAP) together:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from the named outputs above; do not use prose only]
<- PART 2 STEP B references this label by name.
<- PART 2 STEP D references this label by name.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

This section runs before readiness and dimension observations.

Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence is present, status-quo comparison is addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. If the pool was empty, that is the finding: the inertia case
has not been established in the artifact record. Name what else in the artifacts
(beyond the verdict) supports or complicates the judgment. Advisory -- not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

Root pattern (from STEP 3): [consume by label]

From Part 1: which dimensions look clean, which have something worth noticing,
where does this topic stand?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
in the readiness draft -- the team should know the cross-dimension shape before
reading individual observations.
Label: [DRAFT -- to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~280 words) ====

CAUSAL GAP-first order. Advisory language. No severity labels, scores, or gates.

CAUSAL GAP: [coaching observation -- name pool status explicitly; if empty, suggest
  artifact types that would fill it; if non-empty, note what mechanism evidence
  exists and what is missing]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation -- reference Pre-specification gap label by name;
  if YES: "discovery closed before the mechanism evidence existed"; if NO: gap
  emerged in development and may be addressable without spec revision]
  If flagged -> suggested next step:

COHERENCE: [coaching observation -- reference Mechanism-relevant contradiction label
  by name; if YES: name the specific contradiction and why it matters for the inertia
  case -- not just general consistency; if NO: note contradictions are peripheral]
  If flagged -> suggested next step:

STALENESS: [coaching observation -- reference Mechanism-stale label by name; if YES:
  name the specific inertia-pool artifacts that are stale and note the comparison
  is at risk; if NO: mechanism comparison is current]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~75 words) ====

Root pattern (from STEP 3): [consume by label]

Return to STEP B. Does the dimension analysis confirm or change your read?
Reference the Root pattern label by name -- the confirmed readiness validates the
pattern as the central coaching message or explains what changed.
Label: [CONFIRMED -- Root pattern: [name] holds] or [REVISED -- updated root
characterization and why]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-02 -- Single Axis: C-26 "Required input -- do not re-derive" Prohibition Markers

**Axis**: Lifecycle emphasis -- every consuming step carries a per-site "Required input --
do not re-derive" annotation for each named input it consumes (C-26 without ARCHITECTURE
block)
**Hypothesis**: C-23 and C-24 establish that downstream phases must consume named outputs
by label. The structural signal exists in per-step arrows and STEP 3 root-pattern emission.
But neither prevents re-derivation -- the model can "mention" the label while re-inferring
the conclusion from prose. C-26 adds a locally enforceable constraint: the prohibition
marker appears at the consumption site, annotated on the specific input reference. This
variation tests C-26 alone -- no ARCHITECTURE block (C-25) -- to isolate whether per-site
prohibition without an upfront contract produces the same re-derivation reduction. The bet
is that local prohibition at the site of potential re-derivation is sufficient, and that
the ARCHITECTURE block (C-25) primarily helps readers rather than preventing model errors.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

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
8. STEP 3 closes with: Root pattern: [SHORT NAME]. PART 2 STEP B and STEP D consume
   by name.

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
in the readiness draft.
Label: [DRAFT -- to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~280 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what mechanism evidence exists and what is missing]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Reference Pre-specification gap label by name; if YES: frame as "discovery closed
  before mechanism evidence existed"; if NO: gap is development-phase and may not
  require spec revision.
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Reference Mechanism-relevant contradiction label by name; if YES: name the specific
  contradiction and why it matters for the inertia case -- not general consistency; if
  NO: note contradictions are peripheral to the mechanism case.
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Reference Mechanism-stale label by name; if YES: name the stale inertia-pool
  artifacts and explain that the mechanism comparison is at risk; if NO: comparison
  is current.
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

Return to STEP B. Does the dimension analysis confirm or change your read?
Reference Root pattern by label: does it hold as the central coaching message,
or did STEP C change your characterization?
Label: [CONFIRMED -- Root pattern: [name] holds] or [REVISED -- updated root
characterization and why]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-03 -- Single Axis: C-24 Root Pattern Consumption Extended to STEP C Per-Dimension

**Axis**: Lifecycle emphasis -- C-24 Root pattern label consumption extended from STEP B
and STEP D into each individual dimension coaching observation in STEP C
**Hypothesis**: C-24 requires STEP B and STEP D to consume the Root pattern label by name.
This leaves STEP C dimension coaching structurally unconnected to the cross-dimension
synthesis: each dimension observation is produced independently, without knowledge of
whether that dimension contributed to the named root pattern. A drift vector remains: STEP C
prose can characterize cross-dimension relationships without consuming the STEP 3 Root
pattern label, producing a silent re-characterization. This variation extends C-24
consumption into STEP C: each dimension observation explicitly states -- by the Root pattern
label -- whether the dimension contributed to the named root pattern or is an isolated flag.
No ARCHITECTURE block (C-25), no per-site prohibition (C-26) -- tests C-24 extension alone.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

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
8. STEP 3 closes with: Root pattern: [SHORT NAME]. PART 2 STEP B, PART 2 STEP C
   (per-dimension), and PART 2 STEP D all consume by name.

R9 single axis -- C-24 extension:
9. PART 2 STEP C dimension observations each include a "Root pattern contribution" note:
   for each dimension, state by the Root pattern label whether this dimension contributed
   to the named root pattern or is an isolated flag. Dimension coaching that characterizes
   cross-dimension relationships without naming the Root pattern label = a prose drift
   that this extension closes.

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
<- SEQUENCE quotes this line verbatim below.
<- PART 2 STEP A quotes this line verbatim before its inertia case judgment.

### SEQUENCE

Quoting mechanism verdict: "[MECHANISM VERDICT from above]"
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

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
For each contradiction: name the two signals, state the specific disagreement, tag
whether it is mechanism-relevant (involves an inertia-pool artifact or directly
weakens the mechanism verdict).
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES -- [name the contradiction and the inertia-pool
  artifact involved; explain how this weakens the mechanism verdict] /
  NO -- no contradiction involves inertia-pool signals; contradictions are peripheral]

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Artifacts inside / outside the window?
Inertia-pool artifacts: evaluate each -- the mechanism comparison is only as fresh
as the most recent inertia-pool artifact.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES -- [name inertia-pool artifact(s) outside threshold; state days
  elapsed since last update; the mechanism comparison is at risk] /
  NO -- all inertia-pool artifacts are within the threshold; comparison is current]

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Do 2+ flagged dimensions share a root? Consume named outputs by label -- do not re-derive.
Consider: Pre-specification gap + Mechanism-relevant contradiction + Mechanism-stale
+ pool status together:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Root pattern: [SHORT NAME -- drawn from named outputs; do not describe in prose only]
<- PART 2 STEP B references this label by name.
<- PART 2 STEP C per-dimension notes reference this label by name.
<- PART 2 STEP D references this label by name.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

This section runs before readiness and dimension observations.

Quoting mechanism verdict: "[MECHANISM VERDICT from PART 1]"

Based on that verdict and the full artifact record for {{topic}}, is the case
that it beats doing nothing:
  [ ] Clearly built -- mechanism evidence is present, status-quo comparison is addressed
  [ ] Partially built -- some evidence exists but specific gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established in the artifact record

State which applies. Advisory -- not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

Root pattern (from STEP 3): [consume by label]

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual dimension observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~310 words) ====

CAUSAL GAP-first order. Advisory language. No severity labels, scores, or gates.
Per-dimension: state whether the dimension contributed to Root pattern or is isolated.

CAUSAL GAP: [coaching observation -- name pool status; if empty, suggest artifact types;
  if non-empty, note what mechanism evidence exists and what is missing]
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[name from STEP 3]"
    because the pool status is the structural source of the named root / CAUSAL GAP is an
    isolated flag -- pool status did not drive the named root pattern]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation -- reference Pre-specification gap label; if YES: frame as
  "discovery closed before mechanism evidence existed"; if NO: gap is development-phase]
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[name from STEP 3]"
    -- Pre-specification gap YES connects to the named root / SEQUENCE is an isolated flag
    -- the pre-spec status did not drive the named root pattern]
  If flagged -> suggested next step:

COHERENCE: [coaching observation -- reference Mechanism-relevant contradiction label; if YES:
  name the contradiction and why it matters for the inertia case; if NO: peripheral]
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[name from STEP 3]"
    -- Mechanism-relevant contradiction YES connects to the named root / COHERENCE is an
    isolated flag -- contradiction status did not drive the named root pattern]
  If flagged -> suggested next step:

STALENESS: [coaching observation -- reference Mechanism-stale label; if YES: name stale
  inertia-pool artifacts and note the comparison is at risk; if NO: comparison is current]
  Root pattern contribution: [STALENESS contributed to Root pattern: "[name from STEP 3]"
    -- Mechanism-stale YES connects to the named root / STALENESS is an isolated flag --
    mechanism-stale status did not drive the named root pattern]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~75 words) ====

Root pattern (from STEP 3): [consume by label]

Return to STEP B. Does the dimension analysis confirm or change your read?
Reference the Root pattern label by name: do the per-dimension contributions confirm
the named root as the central coaching message -- or did STEP C reveal that the root
characterization should change?
Label: [CONFIRMED -- Root pattern: [name] holds, confirmed by per-dimension contributions]
  or [REVISED -- updated root characterization: [new label] -- reason: ...]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-04 -- Combined Axes: C-24 (Extended) + C-25 (ARCHITECTURE Table) + C-26 (Per-Site Prohibition), Advisory Register

**Axes**: C-24 Root pattern consumed in STEP B, STEP C per-dimension, and STEP D (V-03)
+ C-25 ARCHITECTURE table at the top (V-01) + C-26 "Required input -- do not re-derive"
prohibition at every consuming step (V-02), advisory register
**Hypothesis**: V-01 showed the ARCHITECTURE table makes the dataflow contract scannable
before execution. V-02 showed that per-site prohibition at each consuming step makes
re-derivation a visible local violation. V-03 showed that C-24 can be extended to STEP C
per-dimension to close drift between synthesis and coaching. Combined: the upfront contract
(C-25) tells the reader what will happen; the prohibition markers (C-26) enforce it at the
site of each consumption; the per-dimension C-24 extension closes the last structural gap
between PART 1 synthesis and PART 2 coaching at the individual-dimension level. The bet is
that the combination produces the most architecturally complete advisory-register variation
yet -- every named output is declared, every consumption is prohibited from re-derivation,
and the Root pattern label propagates through all three phases of PART 2.

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
| Root pattern: [label]                   | STEP 3       | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name) |

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

==== STEP C: DIMENSION OBSERVATIONS  (~310 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state whether the dimension contributed to Root pattern or is isolated.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed;
  if non-empty, note what evidence exists and what is missing]
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

## V-05 -- Combined Axes: C-24 (Extended) + C-25 (ARCHITECTURE Schema) + C-26 (Per-Input Prohibition), Imperative Register

**Axes**: C-24 Root pattern consumed in STEP B, STEP C per-dimension, and STEP D (V-03)
+ C-25 ARCHITECTURE schema extended from R8 V-05 (includes STEP C as Root pattern
consumer) + C-26 strengthened from R8 V-05 (per-input "Required input -- do not
re-derive: [label]" rather than grouped), imperative register
**Hypothesis**: R8 V-05 had a grouped "Required inputs (consume by label -- do not
re-derive)" notation that covered multiple labels per consuming step without per-input
specificity. C-26 requires each named-input reference to carry the prohibition -- per-input,
not per-step. This variation strengthens R8 V-05's C-26 implementation to per-input
annotation at every consumption site, extends the ARCHITECTURE block to include STEP C as
a Root pattern consumer, and extends C-24 into STEP C per-dimension (matching V-03/V-04).
The bet is that per-input prohibition (vs. per-step grouped) further reduces the chance
that a specific named input is re-derived while the step-level instruction appears
compliant -- closing the last gap between instruction and structural enforcement.

---

```markdown
Signal integrity check -- {{topic}}.
Run these steps in order. Each step has a required output. Do not skip.

REGISTER RULE: Two numbered registers.
  REGISTER 1 (ANALYSIS): steps 0-3. Internal. Include severity ratings. Do not show to team.
  REGISTER 2 (COACHING): steps A-D. Advisory. No severity ratings or scores visible.

ARCHITECTURE: Named-output pipeline -- all outputs and consuming steps declared before
analysis runs. Each consuming step carries per-input "Required input -- do not re-derive"
annotation for every named input it consumes.

  Named outputs produced:
  [MECHANISM VERDICT]               produced by: step 2a (CAUSAL GAP)
  Pre-specification gap: YES/NO     produced by: step 2b (SEQUENCE)
  Mechanism-relevant cont.: YES/NO  produced by: step 2c (COHERENCE)
  Mechanism-stale: YES/NO           produced by: step 2d (STALENESS)
  Root pattern: [label]             produced by: step 3  (CROSS-DIMENSION)

  Consuming steps and their required inputs (each: Required input -- do not re-derive):
  step 2b:  [MECHANISM VERDICT]
  step 3:   Pre-specification gap
            Mechanism-relevant contradiction
            Mechanism-stale
  step A:   [MECHANISM VERDICT]
  step B:   Root pattern
  step C:   Pre-specification gap (SEQUENCE coaching)
            Mechanism-relevant contradiction (COHERENCE coaching)
            Mechanism-stale (STALENESS coaching)
            Root pattern (all four per-dimension contribution notes)
  step D:   Root pattern

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
   step 3:  Required input -- do not re-derive: Pre-specification gap
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
     inertia-pool artifact or mechanism link weakened; one sentence on how it
     undermines the verdict] /
     NO -- no contradiction involves inertia-pool signals; contradictions are peripheral]
   step 3:  Required input -- do not re-derive: Mechanism-relevant contradiction
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
   step 3:  Required input -- do not re-derive: Mechanism-stale
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
   step B:  Required input -- do not re-derive: Root pattern
   step C (per-dimension): Required input -- do not re-derive: Root pattern
   step D:  Required input -- do not re-derive: Root pattern

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
2. If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
   -- e.g., "The cross-dimension pattern here is [Root pattern]: this is the central
   thing to address."
3. Emit: [DRAFT -- to be confirmed after dimension observations]

--- STEP C: DIMENSION OBSERVATIONS (~310 words) ---

CAUSAL GAP-first. Advisory language. No severity, scores, or gates.
Per-dimension: include a Root pattern contribution note citing the label by name.

CAUSAL GAP:
  Observation for team: ...
  Reference pool status: if empty, name artifact types needed; if non-empty, state
  what evidence exists and what is missing for the mechanism case.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label]" /
    CAUSAL GAP is an isolated flag]
  If flagged -> Suggested next step: ...

SEQUENCE:
  Observation for team: ...
  Required input -- do not re-derive: Pre-specification gap from step 2b
  Reference Pre-specification gap by label: if YES, frame as "discovery phase closed
  before mechanism evidence existed"; if NO, gap is development-phase.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]" /
    SEQUENCE is an isolated flag]
  If flagged -> Suggested next step: ...

COHERENCE:
  Observation for team: ...
  Required input -- do not re-derive: Mechanism-relevant contradiction from step 2c
  Reference Mechanism-relevant contradiction by label: if YES, name the specific
  contradiction and why it matters for the inertia case; if NO, contradictions are
  peripheral.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]" /
    COHERENCE is an isolated flag]
  If flagged -> Suggested next step: ...

STALENESS:
  Observation for team: ...
  Required input -- do not re-derive: Mechanism-stale from step 2d
  Reference Mechanism-stale by label: if YES, name the specific inertia-pool
  artifact(s) that are stale and explain the consequence -- mechanism comparison
  may no longer reflect current alternatives; if NO, the comparison is current.
  Required input -- do not re-derive: Root pattern from step 3
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]" /
    STALENESS is an isolated flag]
  If flagged -> Suggested next step: ...

--- STEP D: CONFIRMED READINESS (~75 words) ---

Required input -- do not re-derive: Root pattern from step 3

1. Return to STEP B draft. Does dimension analysis confirm or change your read?
2. Do the per-dimension Root pattern contributions in STEP C validate the named root
   as the central coaching message -- or reveal that the characterization should change?
3. Reference Root pattern by label explicitly.
4. Emit: [CONFIRMED -- Root pattern: [name] holds, validated by per-dimension contributions]
   or [REVISED -- updated root characterization: [new label] -- reason: ...]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## Variation Map

| V | Single Axis | Combined With | C-24 | C-25 | C-26 | Key Mechanism |
|---|-------------|---------------|------|------|------|---------------|
| V-01 | C-25 ARCHITECTURE table | R8 V-04 base | baseline (STEP B, D) | YES (table) | NO | Table-form ARCHITECTURE makes dataflow scannable before execution; consuming steps use label arrows only |
| V-02 | C-26 prohibition markers only | R8 V-04 base | baseline (STEP B, D) | NO | YES (per-site) | Per-site "Required input -- do not re-derive" at every consuming step; no upfront contract |
| V-03 | C-24 extended to STEP C per-dimension | R8 V-04 base | extended (STEP B, C, D) | NO | NO | Root pattern label surfaces in each dimension coaching note; per-dimension contribution explicitly named |
| V-04 | All three R9 axes combined | Advisory register | extended (STEP B, C, D) | YES (table) | YES (per-site) | Full R9 lock on advisory register; ARCHITECTURE table + per-site prohibition + per-dimension Root pattern |
| V-05 | All three R9 axes combined | Imperative register | extended (STEP B, C, D) | YES (schema) | YES (per-input) | Full R9 lock on imperative register; per-input prohibition strengthened from R8 V-05 grouped notation |

**R9 research questions:**
1. Does the ARCHITECTURE table (V-01/V-04/V-05) improve named-output consumption
   consistency over per-step label arrows -- or does the table primarily help auditors,
   not reduce model re-derivation during execution?
2. Does per-site "Required input -- do not re-derive" prohibition (V-02/V-04/V-05) close
   silent re-derivation that C-23/C-24 structural label consumption does not catch -- or
   does the structural consumption requirement already make re-derivation visible?
3. Does Root pattern consumption extended into STEP C per-dimension (V-03/V-04/V-05)
   produce structurally coherent dimension coaching -- or does the STEP B/D consumption
   (C-24 baseline) already prevent prose-drift between synthesis and individual coaching?
