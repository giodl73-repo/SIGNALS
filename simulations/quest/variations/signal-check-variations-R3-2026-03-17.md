Written. Here is the R3 variations summary:

---

**signal-check-variations-R3-2026-03-17.md** — 5 complete variations for rubric v3 (/34)

**Axis matrix**:

| V | Axis | C-39 | C-40 | C-41 | C-42 |
|---|------|------|------|------|------|
| V-01 | C-39 only — production-site `Required output -- emit exactly:` at STEP E | PASS | FAIL | FAIL | FAIL |
| V-02 | C-40 only — one-phrase reason in terminal verdict | FAIL | PASS | FAIL | FAIL |
| V-03 | C-41 only — `topic namespace` system identity in ARCHITECTURE terminal row | FAIL | FAIL | PASS | FAIL |
| V-04 | C-42 only — all consumers listed for fan-out outputs | FAIL | FAIL | FAIL | PASS |
| V-05 | All four combined, advisory register (canonical) | PASS | PASS | PASS | PASS |

**Key design decisions**:

- **Baseline**: R13 V-04 already passes C-40, C-41, C-42 — so single-axis isolation requires degrading those three while lifting only C-39 in V-01.
- **C-42 degradation** affects 5 rows: [MECHANISM VERDICT], Pre-specification gap, Mechanism-relevant contradiction, Mechanism-stale, and Root pattern — all multi-consumer rows reduced to primary consumer only.
- **C-39 differentiator** is purely local to STEP E: presence vs. absence of `Required output -- emit exactly:` before the terminal verdict line. The enforcement asymmetry it closes (C-26 at consumers, C-39 at producer) mirrors what V-05 R13 established for the imperative register — V-05 now brings it to the advisory register.
- **V-05 is the predicted 34/34 canonical form** — all four annotations are local additions at zero structural overhead relative to R13 V-04.
xactly:` annotation
- C-40 FAIL: terminal verdict = `Terminal readiness: [PROCEED / LOOP / INVESTIGATE]` (reason omitted)
- C-41 FAIL: ARCHITECTURE terminal row Consumed-by = `external consumer (by label)` (generic, not system identity)
- C-42 FAIL: multi-consumer ARCHITECTURE rows list primary consumer only:
  - [MECHANISM VERDICT]: `SEQUENCE (verbatim)` only (PART 2 STEP A omitted)
  - Pre-specification gap: `STEP 3 (by label)` only (PART 2 STEP C SEQUENCE omitted)
  - Mechanism-relevant contradiction: `STEP 3 (by label)` only (PART 2 STEP C COHERENCE omitted)
  - Mechanism-stale: `STEP 3 (by label)` only (PART 2 STEP C STALENESS omitted)
  - Root pattern: `PART 2 STEP B (by name)` only (PART 2 STEP C per-dim and PART 2 STEP D omitted)

**Research questions**:
1. Does `Required output -- emit exactly:` at the STEP E production site make terminal-verdict omission locally visible without requiring cross-reference to the ARCHITECTURE table — closing the enforcement asymmetry between consumption side (C-26) and production side? (V-01 vs baseline)
2. Does the one-phrase reason attached to the terminal verdict make it self-documenting for the topic namespace consumer, removing the need to re-read the full analytical record to understand the decision driver? (V-02 vs degraded baseline)
3. Does naming `topic namespace` (rather than a generic label) in the ARCHITECTURE terminal row make the register boundary structurally explicit as a table-scan property — distinguishing inter-register from intra-register handoffs at a glance? (V-03 vs degraded baseline)
4. Does listing all consumers for fan-out outputs in the ARCHITECTURE table enable complete C-26/C-28 compliance verification from the table alone — without traversing consuming steps? (V-04 vs degraded baseline)

---

## V-01 — Single Axis: C-39 (Production-Site `Required output — emit exactly:` Annotation)

**Axes**: C-39 PASS (STEP E terminal verdict line preceded by `Required output -- emit exactly:` annotation). C-40 FAIL by design (no one-phrase reason). C-41 FAIL by design (generic `external consumer` label). C-42 FAIL by design (multi-consumer rows list primary consumer only).
**Hypothesis**: The `Required output -- emit exactly:` annotation at STEP E makes omission of the terminal verdict locally visible as a missing `Required output` line — the same enforcement mechanism that C-26 places at consumption sites but now applied symmetrically at the production site. Without it, a model can exit STEP E without the terminal verdict and the violation is only detectable by cross-referencing the ARCHITECTURE table. With it, the omission is a locally visible absent annotation. C-40, C-41, C-42 are intentionally degraded to isolate the C-39 contribution.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim) [C-42 FAIL: primary only; PART 2 STEP A omitted by design]    |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C SEQ omitted by design]  |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C COH omitted by design]  |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C STA omitted by design]  |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name) [C-42 FAIL: primary only; STEP C per-dim, STEP D omitted] |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | external consumer (by label) [C-41 FAIL: generic label; not system identity]       |

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
11. PART 2 STEP E opens with two independent per-input prohibitions (C-36 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement.
12. PART 2 STEP E closes with [C-39 PASS: production-site annotation present]:
    Required output -- emit exactly:
      Terminal readiness: [PROCEED / LOOP / INVESTIGATE]
      [C-40 FAIL: one-phrase reason omitted by design; single-axis C-39 isolation]
    -> external consumer [C-41 FAIL: generic label by design]:
    Required input -- do not re-derive: Terminal readiness. Consume by label.

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
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.

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

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE]
  [C-40 FAIL: one-phrase reason omitted by design; single-axis C-39 isolation]
-> external consumer: Required input -- do not re-derive: Terminal readiness. Consume by label.
[C-41 FAIL: generic label by design]
```

---

## V-02 — Single Axis: C-40 (One-Phrase Reason in Terminal Verdict)

**Axes**: C-40 PASS (terminal verdict = `Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]`). C-39 FAIL by design (no `Required output -- emit exactly:` annotation at STEP E). C-41 FAIL by design (`external consumer`). C-42 FAIL by design (primary consumer only).
**Hypothesis**: The one-phrase reason appended to the terminal verdict label makes the verdict self-documenting for the topic namespace: an external consumer receiving `Terminal readiness: LOOP` can identify the primary driver from the artifact alone, without re-reading the full PART 1 analysis. Without the reason, the terminal verdict is a decision without a diagnosis — the consumer must trace back through the analytical record to determine whether the LOOP was driven by mechanism absence, sequencing, staleness, or coherence. C-39, C-41, C-42 are intentionally degraded to isolate the C-40 contribution.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim) [C-42 FAIL: primary only; PART 2 STEP A omitted by design]    |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C SEQ omitted by design]  |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C COH omitted by design]  |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C STA omitted by design]  |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name) [C-42 FAIL: primary only; STEP C per-dim, STEP D omitted] |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | external consumer (by label) [C-41 FAIL: generic label; not system identity]       |

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
11. PART 2 STEP E opens with two independent per-input prohibitions (C-36 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement.
12. PART 2 STEP E closes with [C-39 FAIL by design: no production-site annotation]:
    Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]
    [C-40 PASS: one-phrase reason present; C-39 absent by design]
    -> external consumer [C-41 FAIL: generic label by design]:
    Required input -- do not re-derive: Terminal readiness. Consume by label.

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
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.

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

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]
[C-40 PASS; C-39 FAIL by design: no Required output annotation]
-> external consumer: Required input -- do not re-derive: Terminal readiness. Consume by label.
[C-41 FAIL: generic label by design]
```

---

## V-03 — Single Axis: C-41 (`topic namespace` System Identity in ARCHITECTURE Terminal Row)

**Axes**: C-41 PASS (terminal ARCHITECTURE row Consumed-by = `topic namespace (by label)`). C-39 FAIL by design (no annotation). C-40 FAIL by design (no reason). C-42 FAIL by design (primary consumer only).
**Hypothesis**: Naming `topic namespace` as the Consumed-by entity in the ARCHITECTURE terminal row makes the register boundary structurally explicit in the table: a reader can identify from the ARCHITECTURE block alone where the internal pipeline ends and where handoff to an external system begins. With a generic label (`external consumer`), the boundary is unmarked — the final row is structurally indistinguishable from an internal handoff row, and the reader must traverse the full pipeline to discover that STEP E is a boundary-crossing step rather than a step that feeds another internal analysis node. C-39, C-40, C-42 are intentionally degraded to isolate the C-41 contribution.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                 | Produced by              | Consumed by                                                                        |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim) [C-42 FAIL: primary only; PART 2 STEP A omitted by design]    |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C SEQ omitted by design]  |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C COH omitted by design]  |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label) [C-42 FAIL: primary only; PART 2 STEP C STA omitted by design]  |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name) [C-42 FAIL: primary only; STEP C per-dim, STEP D omitted] |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                           |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                           |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                           |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                           |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                           |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                           |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | topic namespace (by label) [C-41 PASS: system identity; register boundary explicit]|

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
11. PART 2 STEP E opens with two independent per-input prohibitions (C-36 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement.
12. PART 2 STEP E closes with [C-39 FAIL by design; C-40 FAIL by design]:
    Terminal readiness: [PROCEED / LOOP / INVESTIGATE]
    [C-40 FAIL: no reason; C-39 FAIL: no Required output annotation; single-axis C-41 isolation]
    -> topic namespace [C-41 PASS: system identity in forward reference]:
    Required input -- do not re-derive: Terminal readiness. Consume by label.

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
-> PART 2 STEP B: Required input -- do not re-derive: Root pattern. Reference by label.

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

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Terminal readiness: [PROCEED / LOOP / INVESTIGATE]
[C-39 FAIL: no Required output annotation by design; C-40 FAIL: no reason by design]
-> topic namespace: Required input -- do not re-derive: Terminal readiness. Consume by label.
[C-41 PASS: system identity in forward reference]
```

---

## V-04 — Single Axis: C-42 (All Consumers Listed for Fan-Out Outputs in ARCHITECTURE)

**Axes**: C-42 PASS (all multi-consumer ARCHITECTURE rows list all consuming steps). C-39 FAIL by design (no annotation). C-40 FAIL by design (no reason). C-41 FAIL by design (`external consumer`).
**Hypothesis**: Listing every consuming step for fan-out outputs in the ARCHITECTURE Consumed-by column converts the table into a complete audit contract for C-26/C-28 compliance. When the [MECHANISM VERDICT] row lists only `SEQUENCE (verbatim)`, a reader cannot determine from the table whether PART 2 STEP A also carries a C-26 prohibition — they must traverse PART 2 STEP A to confirm. When the row lists both `SEQUENCE (verbatim); PART 2 STEP A (verbatim)`, the C-26 compliance check for both consumption sites is verifiable from one table scan. The audit gap is proportional to fan-out degree: Root pattern (3 consumers) creates a larger gap than [MECHANISM VERDICT] (2 consumers). C-39, C-40, C-41 are intentionally degraded to isolate the C-42 contribution.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                 | Produced by              | Consumed by                                                                                    |
|----------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP               | SEQUENCE (verbatim); PART 2 STEP A (verbatim) [C-42 PASS: all consumers listed]               |
| Pre-specification gap: YES/NO                | SEQUENCE                 | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label) [C-42 PASS: all consumers listed]        |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE                | STEP 3 (by label); PART 2 STEP C COHERENCE (by label) [C-42 PASS: all consumers listed]       |
| Mechanism-stale: YES/NO                      | STALENESS                | STEP 3 (by label); PART 2 STEP C STALENESS (by label) [C-42 PASS: all consumers listed]       |
| Root pattern: [label]                        | STEP 3                   | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) [C-42 PASS] |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE   | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE  | PART 2 STEP D (by label)                                                                       |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS  | PART 2 STEP D (by label)                                                                       |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A            | PART 2 STEP E (by label)                                                                       |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D            | PART 2 STEP E (by label)                                                                       |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E            | external consumer (by label) [C-41 FAIL: generic label; not system identity by design]         |

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
11. PART 2 STEP E opens with two independent per-input prohibitions (C-36 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement.
12. PART 2 STEP E closes with [C-39 FAIL by design; C-40 FAIL by design]:
    Terminal readiness: [PROCEED / LOOP / INVESTIGATE]
    [C-39 FAIL: no Required output annotation; C-40 FAIL: no reason; single-axis C-42 isolation]
    -> external consumer [C-41 FAIL: generic label by design]:
    Required input -- do not re-derive: Terminal readiness. Consume by label.

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

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Terminal readiness: [PROCEED / LOOP / INVESTIGATE]
[C-39 FAIL: no Required output annotation; C-40 FAIL: no reason; single-axis C-42 isolation]
-> external consumer: Required input -- do not re-derive: Terminal readiness. Consume by label.
[C-41 FAIL: generic label by design]
```

---

## V-05 — All Four Combined: C-39 + C-40 + C-41 + C-42, Advisory Register

**Axes**: C-39 PASS (production-site `Required output -- emit exactly:` annotation at STEP E) + C-40 PASS (terminal verdict includes one-phrase reason) + C-41 PASS (`topic namespace` system identity in terminal ARCHITECTURE row) + C-42 PASS (all consumers listed for all multi-consumer rows). Advisory register throughout.
**Hypothesis**: V-05 is the canonical advisory form for R3. The four criteria complete the two-sided enforcement contract at the register boundary and in the ARCHITECTURE table: C-39 makes terminal-verdict omission locally visible at the production site (mirroring C-26 at consumption sites); C-40 makes the terminal verdict self-documenting for external consumers; C-41 makes the register boundary structurally explicit in the ARCHITECTURE table; C-42 makes all fan-out consumption relationships auditable from the table alone. Together they close the remaining audit gaps in the named-binary chain at zero structural cost relative to V-04 -- all four changes are local annotations or Consumed-by column extensions.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

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
   opens by consuming all four drift binaries by label -- one per-input annotation each.
10. PART 2 STEP D closes with:
    Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY] -> STEP E (forward arrow).
11. PART 2 STEP E opens with two independent per-input prohibitions (C-36 PASS):
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement.
12. PART 2 STEP E closes with [C-39 PASS + C-40 PASS + C-41 PASS: full two-sided contract]:
    Required output -- emit exactly:
      Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]
    -> topic namespace: Required input -- do not re-derive: Terminal readiness. Consume by label.

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

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]
-> topic namespace: Required input -- do not re-derive: Terminal readiness. Consume by label.
```
