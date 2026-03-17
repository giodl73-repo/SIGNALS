# Signal-Check Variations — R12 (2026-03-17)

**Rubric version**: v11 (denominator /27)
**New criteria under test**: C-33 (STEP A named inertia-case verdict), C-34 (STEP B per-input joint consumption of C-32 + C-33), C-35 (ARCHITECTURE extended to PART 2 internal chain)
**Base**: R10 V-04 + C-32 baseline (STEP D emits `Confirmed readiness:` consumed by STEP E)

**Axis matrix**:

| V | Axis | C-33 | C-34 | C-35 |
|---|------|------|------|------|
| V-01 | C-33 only (STEP A emits named verdict; STEP E prose-restatement — no prohibition) | YES | FAIL | FAIL |
| V-02 | C-34 grouped (C-33 present; STEP E grouped prohibition — not per-input) | YES | FAIL | FAIL |
| V-03 | C-35 only (ARCHITECTURE extended; STEP A prose only; STEP E no inertia prohibition) | FAIL | FAIL | YES |
| V-04 | All three combined, advisory register (canonical) | YES | YES | YES |
| V-05 | All three combined, imperative register | YES | YES | YES |

**Structural addition over R10 V-04 (applied as locked baseline in all variations)**:
- STEP D now emits `Confirmed readiness: READY / CONDITIONALLY READY / NOT READY` with forward arrow to STEP E (C-32 baseline, tested in v10 rubric but not isolated in R10 round)
- PART 2 gains STEP E: TEAM READINESS POSITION as the final synthesis step (replaces inline "Team summary" in R10 STEP D)
- STEP B retains DRAFT function early in PART 2 (C-11 compliance); STEP E is the final consumption step
- ARCHITECTURE table advances from 9 rows (R10) to 10 rows (V-01/V-02: adds `Confirmed readiness` row) or 11 rows (V-03/V-04/V-05: adds both `Confirmed readiness` and `Inertia case` rows)

**Research questions**:
1. Does C-33's named binary from STEP A close a structural gap that prose inertia-case conclusions leave open at STEP E? (V-01 vs baseline)
2. Does per-input prohibition at STEP E (C-34) close a partial-compliance gap that grouped joint consumption leaves open — i.e., can a model consume `Confirmed readiness` by label while re-deriving `Inertia case` under a grouped annotation? (V-02 vs V-04)
3. Does extending the ARCHITECTURE block to PART 2 internal named outputs (C-35) make the STEP A → STEP E and STEP D → STEP E handoffs independently auditable before PART 2 runs — and does the declared contract force compliance or only make gaps visible? (V-03 vs V-04)

---

## V-01 — Single Axis: C-33 (STEP A Named Inertia-Case Verdict)

**Axis**: C-33 only — STEP A emits `Inertia case: BUILT / PARTIAL / OPEN` (named verdict present);
STEP E references the inertia case in prose without a per-input prohibition annotation (C-34 FAIL);
ARCHITECTURE table not extended to PART 2 internal rows beyond `Confirmed readiness` (C-35 FAIL).
**Hypothesis**: The named binary from STEP A isolates the inertia-case judgment as a consumable artifact
independent of the enforcement mechanism. Without C-34's prohibition, STEP E can acknowledge the label
while re-deriving its implications from prose context. C-33's structural gain is visible in V-01;
C-34's additional closure becomes measurable when comparing V-01 to V-04.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                | Produced by             | Consumed by                                                               |
|---------------------------------------------|-------------------------|---------------------------------------------------------------------------|
| [MECHANISM VERDICT]                         | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                             |
| Pre-specification gap: YES/NO               | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                      |
| Mechanism-relevant contradiction: YES/NO    | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                     |
| Mechanism-stale: YES/NO                     | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                     |
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                  |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                  |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                  |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                  |
| Confirmed readiness: READY/COND./NOT READY  | PART 2 STEP D           | PART 2 STEP E (by label)                                                  |

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
   opens by quoting the MECHANISM VERDICT verbatim and closes with a named verdict label.
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all four drift binaries by label -- one per-input annotation each.
10. PART 2 STEP D closes with Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY].

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
  partial / absent. Name what is there and what is missing.

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
existed?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1 (14 or 30 days). Inertia-pool artifacts inside / outside window?
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES / NO + reason]
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

Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions look clean, which have something worth noticing?
If Root pattern is not "none" or "Isolated flags": name the Root pattern explicitly
before individual observations -- the team sees the cross-dimension shape first.
Label: [DRAFT -- to be confirmed after STEP D]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity, scores, or gates.
Per-dimension: state Root pattern contribution and close with STEP C drift binary.

CAUSAL GAP: [coaching observation -- pool status; if empty, name artifact types needed]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [CAUSAL GAP contributed to Root pattern: "[label from STEP 3]"
    / CAUSAL GAP is an isolated flag]
  STEP C drift: [CLOSED -- CAUSAL GAP coaching aligns with Root pattern "[label]" /
    OPEN -- CAUSAL GAP coaching diverges; reason: ...]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [SEQUENCE contributed to Root pattern / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [COHERENCE contributed to Root pattern / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [STALENESS contributed to Root pattern / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
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

If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
If any OPEN: name dimension(s) and reason for divergence.

Confirmed readiness: [READY -- all STEP C drift CLOSED, mechanism evidence sufficient /
  CONDITIONALLY READY -- [list conditions]; one more loop recommended on [dimension] /
  NOT READY -- [dimension] OPEN; mechanism or timing gap must be addressed]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~80 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
[Inertia case from STEP A referenced in prose -- not a named-input prohibition]
Referring to the inertia case assessment in STEP A above:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: [restate from STEP A prose -- clearly built / partially built / still open]
4. Overall read: proceed / loop once more / investigate further
```

---

## V-02 — Single Axis: C-34 Grouped (C-33 Present; Per-Input Enforcement Absent)

**Axis**: C-34 grouped — STEP A emits `Inertia case: BUILT / PARTIAL / OPEN` (C-33 YES);
STEP E uses a GROUPED joint prohibition covering both `Confirmed readiness` and `Inertia case`
in a single annotation line (C-34 FAIL — grouped form);
ARCHITECTURE table not extended beyond `Confirmed readiness` row (C-35 FAIL).
**Hypothesis**: Grouped consumption is the partial-compliance trap for C-34, analogous to C-28's
grouped STEP 3 annotation in R10. A model can satisfy the `Confirmed readiness` prohibition while
re-deriving the `Inertia case` from STEP A prose under a grouped annotation — the violation is
locally invisible because the grouped annotation appears present. Per-input form (V-04) makes each
specific re-derivation detectable.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                | Produced by             | Consumed by                                                               |
|---------------------------------------------|-------------------------|---------------------------------------------------------------------------|
| [MECHANISM VERDICT]                         | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                             |
| Pre-specification gap: YES/NO               | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                      |
| Mechanism-relevant contradiction: YES/NO    | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                     |
| Mechanism-stale: YES/NO                     | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                     |
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                  |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                  |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                  |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                  |
| Confirmed readiness: READY/COND./NOT READY  | PART 2 STEP D           | PART 2 STEP E (by label)                                                  |

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH. STEP A opens by quoting the
   MECHANISM VERDICT verbatim and closes with named verdict: Inertia case: [BUILT/PARTIAL/OPEN].
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all four drift binaries by label -- one per-input annotation each.
10. PART 2 STEP D closes with Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY].

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Inertia-relevant artifact count:
  1 or more -> staleness threshold = 14 days
  0         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

### CAUSAL GAP

Inertia-relevant pool: [list every artifact tagged yes in Step 1].
Evaluate mechanism evidence from this pool only.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

Cite 2+ artifacts with dates.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Pre-specification gap: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

Name 2+ signals on a specific claim.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-relevant contradiction: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1.
(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

Mechanism-stale: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate]

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

Is the case that {{topic}} beats doing nothing:
  [ ] Clearly built
  [ ] Partially built -- name the key gap
  [ ] Still open

State which applies. Advisory -- not a gate.

Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]
-> STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions clean, which flagged?
If Root pattern is present: name it before individual observations.
Label: [DRAFT -- to be confirmed after STEP D]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP: [coaching observation]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP
Required input -- do not re-derive: STEP C drift -- SEQUENCE
Required input -- do not re-derive: STEP C drift -- COHERENCE
Required input -- do not re-derive: STEP C drift -- STALENESS

Drift summary (consume from STEP C labels -- do not re-infer):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY + reason]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~80 words) ====

Required inputs -- do not re-derive: Confirmed readiness and Inertia case
[GROUPED annotation -- C-34 FAIL: both inputs covered by one prohibition line]

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: [BUILT / PARTIAL / OPEN -- from STEP A label above]
4. Overall read: proceed / loop once more / investigate further
```

---

## V-03 — Single Axis: C-35 (ARCHITECTURE Extended; C-33 and C-34 Absent)

**Axis**: C-35 only — ARCHITECTURE table extended to include both `Inertia case: BUILT/PARTIAL/OPEN`
(PART 2 STEP A → PART 2 STEP E) and `Confirmed readiness: READY/COND./NOT READY`
(PART 2 STEP D → PART 2 STEP E) as declared rows (C-35 YES);
STEP A closes with prose judgment only -- no named binary emitted (C-33 FAIL);
STEP E has no prohibition annotation for `Inertia case` (C-34 FAIL -- no label to consume).
**Hypothesis**: The ARCHITECTURE table declares the STEP A → STEP E handoff, but STEP A does not
emit the corresponding named binary. This creates a declared-but-unfulfilled contract: the
ARCHITECTURE row promises a named output that never exists. The gap is visible from the table
without reading STEP A -- the pre-execution auditability goal of C-35 is achieved (the gap is
detectable), but the gap is not closed. V-03 tests whether declaration alone creates pressure
toward compliance, and confirms that C-33 + C-34 are required to fulfill the contract C-35 declares.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                | Produced by             | Consumed by                                                               |
|---------------------------------------------|-------------------------|---------------------------------------------------------------------------|
| [MECHANISM VERDICT]                         | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                             |
| Pre-specification gap: YES/NO               | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                      |
| Mechanism-relevant contradiction: YES/NO    | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                     |
| Mechanism-stale: YES/NO                     | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                     |
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                  |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                  |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                  |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                  |
| Inertia case: BUILT/PARTIAL/OPEN            | PART 2 STEP A           | PART 2 STEP E (by label)                                                  |
| Confirmed readiness: READY/COND./NOT READY  | PART 2 STEP D           | PART 2 STEP E (by label)                                                  |

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Locked structural features (architectural -- not instructional):
1. Artifact inventory includes "Inertia Relevant?" column (yes / no per artifact).
2. CAUSAL GAP opens with "Inertia-relevant pool: [list]" and evaluates that pool only.
3. CAUSAL GAP ends with [MECHANISM VERDICT: ...]. SEQUENCE quotes it verbatim.
4. SEQUENCE closes with: Pre-specification gap: [YES / NO + reason].
5. PART 2 opens with STEP A: INERTIA CASE STRENGTH as a dedicated named section.
   STEP A opens by quoting the MECHANISM VERDICT verbatim.
6. COHERENCE closes with: Mechanism-relevant contradiction: [YES / NO + reason].
7. STALENESS closes with: Mechanism-stale: [YES / NO + reason].
8. STEP 3 closes with: Root pattern: [SHORT NAME].
9. PART 2 STEP C each dimension closes with STEP C drift: CLOSED/OPEN. PART 2 STEP D
   opens by consuming all four drift binaries by label -- one per-input annotation each.
10. PART 2 STEP D closes with Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY].

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Inertia-relevant artifact count:
  1 or more -> staleness threshold = 14 days
  0         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

### CAUSAL GAP

Inertia-relevant pool: [list every artifact tagged yes in Step 1].
Evaluate mechanism evidence from this pool only.

(internal: green / yellow / red)
Observation: ...
If yellow or red -> next action:

[MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
<- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
<- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT from above -- paste verbatim]"

(internal: green / yellow / red)
Observation: ...

Pre-specification gap: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Pre-specification gap. Consume by label.
<- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

### COHERENCE

(internal: green / yellow / red)
Observation: ...

Mechanism-relevant contradiction: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction. Consume by label.
<- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

### STALENESS

Apply threshold from Step 1.
(internal: green / yellow / red)
Observation: ...

Mechanism-stale: [YES / NO + reason]
<- STEP 3: Required input -- do not re-derive: Mechanism-stale. Consume by label.
<- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS

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

Is the case that {{topic}} beats doing nothing:
  [ ] Clearly built
  [ ] Partially built -- name the key gap
  [ ] Still open

State which applies. Advisory -- not a gate.
[prose judgment only -- no named binary emitted; C-33 FAIL by design]

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

From Part 1: which dimensions clean, which flagged?
If Root pattern is present: name it before individual observations.
Label: [DRAFT -- to be confirmed after STEP D]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP: [coaching observation]
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

SEQUENCE: [coaching observation]
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

==== STEP D: CONFIRMED READINESS  (~90 words) ====

Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP
Required input -- do not re-derive: STEP C drift -- SEQUENCE
Required input -- do not re-derive: STEP C drift -- COHERENCE
Required input -- do not re-derive: STEP C drift -- STALENESS

Drift summary (consume from STEP C labels -- do not re-infer):
  CAUSAL GAP: [CLOSED / OPEN]
  SEQUENCE:   [CLOSED / OPEN]
  COHERENCE:  [CLOSED / OPEN]
  STALENESS:  [CLOSED / OPEN]

Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY + reason]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~80 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
[Inertia case from STEP A referenced only in prose -- no named-label consumption; C-34 FAIL]

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: [restate coaching conclusion from STEP A prose]
4. Overall read: proceed / loop once more / investigate further
```

---

## V-04 — All Three Combined: C-33 + C-34 + C-35, Advisory Register (Canonical)

**Axes**: C-33 (STEP A emits `Inertia case: BUILT / PARTIAL / OPEN` with forward arrow to STEP E) +
C-34 (STEP E opens with two separate per-input prohibitions -- one for Confirmed readiness, one for
Inertia case -- not grouped) + C-35 (ARCHITECTURE table extends to 11 rows, including both PART 2
internal named outputs and their consumer STEP E), advisory register.
**Hypothesis**: V-04 is the canonical advisory form for R12. Eleven-row ARCHITECTURE table declares
the full cross-register pipeline before either part begins. STEP A's named verdict and forward arrow
make the production site self-declaring. STEP E's per-input prohibitions make the joint grounding
requirement locally enforceable: a model cannot satisfy `Confirmed readiness` consumption while
re-deriving `Inertia case` without the second prohibition being visibly absent.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                | Produced by             | Consumed by                                                               |
|---------------------------------------------|-------------------------|---------------------------------------------------------------------------|
| [MECHANISM VERDICT]                         | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                             |
| Pre-specification gap: YES/NO               | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                      |
| Mechanism-relevant contradiction: YES/NO    | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                     |
| Mechanism-stale: YES/NO                     | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                     |
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                  |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                  |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                  |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                  |
| Inertia case: BUILT/PARTIAL/OPEN            | PART 2 STEP A           | PART 2 STEP E (by label)                                                  |
| Confirmed readiness: READY/COND./NOT READY  | PART 2 STEP D           | PART 2 STEP E (by label)                                                  |

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
   opens by consuming all four drift binaries by label -- one per-input annotation each.
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two separate per-input prohibitions (C-34):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A

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
  Root pattern contribution: [SEQUENCE contributed to Root pattern: "[label]"
    / SEQUENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

COHERENCE: [coaching observation]
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [COHERENCE contributed to Root pattern: "[label]"
    / COHERENCE is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
  If flagged -> suggested next step:

STALENESS: [coaching observation]
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [STALENESS contributed to Root pattern: "[label]"
    / STALENESS is an isolated flag]
  STEP C drift: [CLOSED / OPEN + reason]
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

If all CLOSED: per-dimension coaching confirmed Root pattern without divergence.
If any OPEN: name dimension(s) and reason for divergence.

Confirmed readiness: [READY -- all drift CLOSED, mechanism evidence sufficient /
  CONDITIONALLY READY -- [list conditions]; one more loop recommended on [dimension] /
  NOT READY -- [dimension] OPEN; mechanism or timing gap must be addressed]
-> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~80 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further
```

---

## V-05 — All Three Combined: C-33 + C-34 + C-35, Imperative Register

**Axes**: C-33 + C-34 + C-35 complete, imperative register.
ARCHITECTURE uses schema form (C-27 exception applies for imperative register).
STEP A closes with `Required output -- emit exactly: Inertia case: [BUILT / PARTIAL / OPEN]`.
STEP D closes with `Required output -- emit exactly: Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]`.
STEP E opens with two separate per-input prohibitions.
**Hypothesis**: The imperative `Required output -- emit exactly:` framing elevates C-33's named
binary from an advisory label to a required output -- the strongest form. The schema ARCHITECTURE
lists consuming steps per named output. Combined with C-34 per-input at STEP E, the imperative
form closes the same structural gaps as V-04 at highest structural precision with maximum overhead.

---

```markdown
Signal-check for {{topic}}.
Imperative -- produce each labeled output exactly as specified. Do not omit or reorder steps.

ARCHITECTURE -- Named-Output Schema

Each consuming step references named inputs with separate "Required input -- do not re-derive:
[label]" per input -- not grouped. Each producing step carries a "Required output -- emit
exactly: [label]" block for every named output.

NAMED OUTPUTS AND CONSUMING STEPS:
- [MECHANISM VERDICT]
    Produced by: STEP 2 CAUSAL GAP
    Consumed by: STEP 2 SEQUENCE (verbatim quote); PART 2 STEP A (verbatim quote)
- Pre-specification gap: YES/NO
    Produced by: STEP 2 SEQUENCE
    Consumed by: STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)
- Mechanism-relevant contradiction: YES/NO
    Produced by: STEP 2 COHERENCE
    Consumed by: STEP 3 (by label); PART 2 STEP C COHERENCE (by label)
- Mechanism-stale: YES/NO
    Produced by: STEP 2 STALENESS
    Consumed by: STEP 3 (by label); PART 2 STEP C STALENESS (by label)
- Root pattern: [label]
    Produced by: STEP 3
    Consumed by: PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name)
- STEP C drift -- CAUSAL GAP: CLOSED/OPEN
    Produced by: PART 2 STEP C CAUSAL GAP
    Consumed by: PART 2 STEP D (by label)
- STEP C drift -- SEQUENCE: CLOSED/OPEN
    Produced by: PART 2 STEP C SEQUENCE
    Consumed by: PART 2 STEP D (by label)
- STEP C drift -- COHERENCE: CLOSED/OPEN
    Produced by: PART 2 STEP C COHERENCE
    Consumed by: PART 2 STEP D (by label)
- STEP C drift -- STALENESS: CLOSED/OPEN
    Produced by: PART 2 STEP C STALENESS
    Consumed by: PART 2 STEP D (by label)
- Inertia case: BUILT/PARTIAL/OPEN
    Produced by: PART 2 STEP A
    Consumed by: PART 2 STEP E (by label -- separate prohibition)
- Confirmed readiness: READY/CONDITIONALLY READY/NOT READY
    Produced by: PART 2 STEP D
    Consumed by: PART 2 STEP E (by label -- separate prohibition)

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: all steps produce named outputs as specified.
PART 2 -- TEAM COACHING REPORT: advisory tone; all named outputs produced and consumed as specified.

======================================================================
PART 1 -- ANALYTICAL RECORD
======================================================================

STEP 0: INERTIA ANCHOR
State the status-quo alternative if {{topic}} does not ship. One sentence.

STEP 1: ARTIFACT INVENTORY
Produce a table with columns: Artifact | Namespace | Date | Signal Carried | Inertia Relevant?
Inertia Relevant: yes if artifact speaks to comparison between {{topic}} and the
status-quo alternative (competitors, benchmarks, usage data, mechanism evidence); no otherwise.
List empty namespaces after table.

Required output -- emit exactly:
  Inertia-relevant count: [N]
  Staleness threshold: [14 days (N >= 1) / 30 days (N = 0)]

STEP 2: DIMENSION ANALYSIS

Produce each dimension in order: CAUSAL GAP -> SEQUENCE -> COHERENCE -> STALENESS.

CAUSAL GAP:
  List the inertia-relevant pool (artifacts tagged yes in Step 1).
  Evaluate mechanism evidence from this pool only. State: present / partial / absent.
  If pool empty: state verdict absent by default; name needed artifact types.
  (internal: green / yellow / red)

  Required output -- emit exactly:
    [MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]

  Required output -- emit exactly (forward declarations):
    <- SEQUENCE: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.
    <- PART 2 STEP A: Required input -- do not re-derive: [MECHANISM VERDICT]. Quote verbatim.

SEQUENCE:
  Required input -- do not re-derive: [MECHANISM VERDICT]
  Quoting mechanism verdict: "[paste verbatim from CAUSAL GAP]"

  Cite 2+ artifacts with dates. Did discovery precede specification? Apply mechanism lens:
  did inertia-relevant pool artifacts appear in the discovery phase?
  (internal: green / yellow / red)

  Required output -- emit exactly:
    Pre-specification gap: [YES -- reason / NO -- reason]

  Required output -- emit exactly (forward declarations):
    <- STEP 3: Required input -- do not re-derive: Pre-specification gap.
    <- PART 2 STEP C SEQUENCE: Required input -- do not re-derive: Pre-specification gap.

COHERENCE:
  Name 2+ signals on a specific claim. For each contradiction: name both signals,
  state the specific disagreement, tag whether mechanism-relevant.
  (internal: green / yellow / red)

  Required output -- emit exactly:
    Mechanism-relevant contradiction: [YES -- name contradiction and inertia-pool artifact /
      NO -- no contradiction involves inertia-pool signals]

  Required output -- emit exactly (forward declarations):
    <- STEP 3: Required input -- do not re-derive: Mechanism-relevant contradiction.
    <- PART 2 STEP C COHERENCE: Required input -- do not re-derive: Mechanism-relevant contradiction.

STALENESS:
  Apply threshold from Step 1. Evaluate inertia-pool artifacts first.
  (internal: green / yellow / red)

  Required output -- emit exactly:
    Mechanism-stale: [YES -- name artifact(s) outside threshold / NO -- all within threshold]

  Required output -- emit exactly (forward declarations):
    <- STEP 3: Required input -- do not re-derive: Mechanism-stale.
    <- PART 2 STEP C STALENESS: Required input -- do not re-derive: Mechanism-stale.

STEP 3: CROSS-DIMENSION PATTERN

  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Mechanism-stale from STALENESS

  Apply pattern logic from named inputs:
  - Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
  - Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
  - Mechanism-relevant contradiction YES + partial/absent verdict -> "Mechanism contradiction"
  - Empty pool -> "Empty inertia pool"
  - No shared root -> "Isolated flags" or "none"

  Required output -- emit exactly:
    Root pattern: [SHORT NAME]

  Required output -- emit exactly (forward declarations):
    <- PART 2 STEP B: Required input -- do not re-derive: Root pattern.
    <- PART 2 STEP C per-dimension: Required input -- do not re-derive: Root pattern.
    <- PART 2 STEP D: Required input -- do not re-derive: Root pattern.

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory tone throughout)
======================================================================

STEP A: INERTIA CASE STRENGTH

  Required input -- do not re-derive: [MECHANISM VERDICT]
  Quoting mechanism verdict: "[paste verbatim from PART 1 CAUSAL GAP]"

  Assess whether the case that {{topic}} beats doing nothing is:
    clearly built / partially built / still open.
  Name the key gap if partially built or still open. Advisory -- not a gate.

  Required output -- emit exactly:
    Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]

  Required output -- emit exactly (forward declaration):
    -> STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

STEP B: DRAFT READINESS

  Required input -- do not re-derive: Root pattern from STEP 3

  State which dimensions look clean and which have something worth noticing.
  If Root pattern is present and not "none": name it before individual observations.

  Required output -- emit exactly:
    Draft readiness: [summary of clean vs. flagged dimensions]
    Label: DRAFT -- to be confirmed after STEP D and finalized in STEP E

STEP C: DIMENSION OBSERVATIONS

Produce per-dimension coaching in order: CAUSAL GAP, SEQUENCE, COHERENCE, STALENESS.
Advisory. No severity labels or scores.

  CAUSAL GAP:
    Required input -- do not re-derive: Root pattern from STEP 3
    State coaching observation. Pool status: empty / thin / adequate.
    Root pattern contribution: [contributed to Root pattern "[label]" / isolated flag]

    Required output -- emit exactly:
      STEP C drift -- CAUSAL GAP: [CLOSED -- coaching aligns with Root pattern "[label]" /
        OPEN -- coaching diverges; reason: ___]

    If flagged -> state suggested next step.

  SEQUENCE:
    Required input -- do not re-derive: Pre-specification gap from SEQUENCE
    Required input -- do not re-derive: Root pattern from STEP 3
    Root pattern contribution: [contributed / isolated flag]

    Required output -- emit exactly:
      STEP C drift -- SEQUENCE: [CLOSED / OPEN + reason]

    If flagged -> state suggested next step.

  COHERENCE:
    Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
    Required input -- do not re-derive: Root pattern from STEP 3
    Root pattern contribution: [contributed / isolated flag]

    Required output -- emit exactly:
      STEP C drift -- COHERENCE: [CLOSED / OPEN + reason]

    If flagged -> state suggested next step.

  STALENESS:
    Required input -- do not re-derive: Mechanism-stale from STALENESS
    Required input -- do not re-derive: Root pattern from STEP 3
    Root pattern contribution: [contributed / isolated flag]

    Required output -- emit exactly:
      STEP C drift -- STALENESS: [CLOSED / OPEN + reason]

    If flagged -> state suggested next step.

STEP D: CONFIRMED READINESS

  Required input -- do not re-derive: Root pattern from STEP 3
  Required input -- do not re-derive: STEP C drift -- CAUSAL GAP
  Required input -- do not re-derive: STEP C drift -- SEQUENCE
  Required input -- do not re-derive: STEP C drift -- COHERENCE
  Required input -- do not re-derive: STEP C drift -- STALENESS

  Produce drift summary (consume from STEP C labels -- do not re-infer):
    CAUSAL GAP: [CLOSED / OPEN]
    SEQUENCE:   [CLOSED / OPEN]
    COHERENCE:  [CLOSED / OPEN]
    STALENESS:  [CLOSED / OPEN]

  State whether drift summary confirms Root pattern or reveals divergence.

  Required output -- emit exactly:
    Confirmed readiness: [READY -- all drift CLOSED, mechanism evidence sufficient /
      CONDITIONALLY READY -- [list conditions] /
      NOT READY -- [dimension] OPEN; gap must be addressed]

  Required output -- emit exactly (forward declaration):
    -> STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

STEP E: TEAM READINESS POSITION

  Required input -- do not re-derive: Confirmed readiness from STEP D
  Required input -- do not re-derive: Inertia case from STEP A

  Produce team-facing readiness position from these two grounded inputs only.
  Do not re-derive either input from prose context.

  State:
  1. Dimensions clean vs. flagged (count)
  2. Most useful thing to address before committing
  3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
  4. Inertia case: [BUILT / PARTIAL / OPEN]
  5. Overall read: proceed / loop once more / investigate further
```

---

## Summary

| V | C-33 | C-34 | C-35 | Register | ARCHITECTURE rows | Key structural gap preserved |
|---|------|------|------|----------|-------------------|------------------------------|
| V-01 | YES (named verdict) | FAIL (prose ref at STEP E) | FAIL (10 rows, no Inertia case row) | Advisory | 10 | STEP E re-derives Inertia case from STEP A prose; no prohibition present |
| V-02 | YES (named verdict + arrow) | FAIL (grouped joint prohibition) | FAIL (10 rows) | Advisory | 10 | Grouped annotation allows selective compliance: Confirmed readiness consumed, Inertia case re-derivable without local violation |
| V-03 | FAIL (prose only) | FAIL (no Inertia case label to consume) | YES (11 rows) | Advisory | 11 | ARCHITECTURE declares Inertia case row pointing to STEP E; STEP A never emits the binary; contract declared but unfulfilled |
| V-04 | YES | YES (per-input) | YES (11 rows) | Advisory | 11 | None -- full structural closure |
| V-05 | YES | YES (per-input) | YES (11 rows, schema) | Imperative | 11 | None -- full structural closure, highest precision |

**Predicted research findings**:
- V-01 vs V-04: C-33 alone closes the named-binary gap but leaves STEP E free to re-derive the Inertia case implications from STEP A prose context; C-34's per-input prohibition is required to make re-derivation locally detectable
- V-02 vs V-04: Grouped prohibition at STEP E is the C-34 partial-compliance trap -- single annotation line appears compliant but allows one input to be re-derived; per-input form closes this by making each specific consumption independently enforceable
- V-03 vs V-04: ARCHITECTURE declaration of Inertia case row with null production site makes the compliance gap visible upfront but does not close it; C-33 (named binary at STEP A) is the prerequisite for C-35's auditability goal to be fulfillable, not just visible
