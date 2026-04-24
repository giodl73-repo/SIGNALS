# Signal-Check Variations — R13 (2026-03-17)

**Rubric version**: v2 (denominator /30)
**New criteria under test**: C-36 (per-input independence at STEP E convergence point), C-37 (step-granular Consumed-by in ARCHITECTURE table), C-38 (STEP E emits named terminal verdict)
**Base**: R12 V-04 (all R1–R12 features locked; 11-row ARCHITECTURE; C-33/C-34/C-35 complete)

**Axis matrix**:

| V | Axis | C-36 | C-37 | C-38 |
|---|------|------|------|------|
| V-01 | C-38 only (terminal verdict added; C-36 degraded to shared-header; C-37 degraded to section-level) | FAIL | FAIL | PASS |
| V-02 | C-37 only (step-granular all rows; C-36 degraded to shared-header; C-38 absent) | FAIL | PASS | FAIL |
| V-03 | C-36 only (independent self-standing at STEP E; C-37 degraded to section-level; C-38 absent) | PASS | FAIL | FAIL |
| V-04 | All three combined, advisory register (canonical) | PASS | PASS | PASS |
| V-05 | All three combined, imperative register | PASS | PASS | PASS |

**Structural addition over R12 V-04 (applied as locked baseline in all variations)**:
- C-36 differentiator: the STEP E per-input prohibition form. PASS = each annotation is a complete independent statement (`Required input -- do not re-derive: [label]` as a standalone line). FAIL = shared introductory phrase semantically groups both inputs under a single annotation head.
- C-37 differentiator: Consumed-by entries in the ARCHITECTURE table. PASS = every row names the specific consuming step (e.g., `PART 2 STEP E`). FAIL = PART 2 internal rows use section-level granularity (e.g., `PART 2 readiness summary`).
- C-38 differentiator: STEP E closes with a named terminal verdict (`Terminal readiness: PROCEED / LOOP / INVESTIGATE`) declared in the ARCHITECTURE block as a produced output. FAIL = STEP E states the readiness position in advisory prose only; no labeled terminal output is emitted.

**Note on C-36/C-28 entanglement**: The C-36 FAIL form (shared-header annotation) also triggers a C-28 FAIL (general per-input prohibition rule). This entanglement is a research finding, not a design flaw — C-36 is the convergence-point-specific name for what C-28 prohibits globally, and V-03's C-36 PASS confirms that independent self-standing form simultaneously satisfies both. V-01 and V-02 lose C-28 as a co-fail.

**Research questions**:
1. Does C-38's terminal verdict close a pipeline asymmetry that prose readiness conclusions leave open for external consumers such as the topic namespace? (V-01 vs baseline)
2. Does C-37's step-granular Consumed-by reduce audit overhead from section-traversal to table-scan for PART 2 internal handoffs? (V-02 vs degraded baseline)
3. Does C-36 add structural enforcement beyond C-28/C-34 at the STEP E convergence point, or does it name the same constraint with tighter scope? (V-03 vs degraded baseline; C-28 co-fail pattern)

---

## V-01 — Single Axis: C-38 (STEP E Named Terminal Verdict)

**Axes**: C-38 PASS (STEP E emits `Terminal readiness: PROCEED / LOOP / INVESTIGATE` with ARCHITECTURE declaration and forward arrow to topic namespace). C-36 degraded to shared-header form (C-36 FAIL by design). C-37 degraded to section-level Consumed-by for PART 2 internal rows (C-37 FAIL by design). 12-row ARCHITECTURE (adds Terminal readiness row).
**Hypothesis**: C-38's terminal verdict closes the only asymmetric node in the named-binary chain — STEP E consumes two inputs but produces none without C-38, making the signal-check result inaccessible as a named artifact to external consumers. Adding the terminal verdict closes the register boundary symmetrically with how C-32 closed the PART 1-to-PART 2 handoff. C-36 and C-37 are intentionally degraded to isolate the C-38 contribution.

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
| Inertia case: BUILT/PARTIAL/OPEN            | PART 2 STEP A           | PART 2 readiness summary [C-37 FAIL: section-level by design]             |
| Confirmed readiness: READY/COND./NOT READY  | PART 2 STEP D           | PART 2 readiness summary [C-37 FAIL: section-level by design]             |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE| PART 2 STEP E           | topic namespace (by label)                                                |

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
11. PART 2 STEP E opens with grouped annotation [C-36 FAIL by design]:
    Required inputs -- do not re-derive: Confirmed readiness from STEP D and Inertia case from STEP A
    [GROUPED -- C-36 FAIL and C-28 co-fail by design; single-axis isolation of C-38]
12. PART 2 STEP E closes with:
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

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required inputs -- do not re-derive: Confirmed readiness from STEP D and Inertia case from STEP A
[GROUPED annotation -- C-36 FAIL and C-28 co-fail by design; single-axis C-38 isolation]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]
-> topic namespace: Required input -- do not re-derive: Terminal readiness. Consume by label.
```

---

## V-02 — Single Axis: C-37 (Step-Granular Consumed-by in ARCHITECTURE Table)

**Axes**: C-37 PASS (all ARCHITECTURE rows name their consuming step at step-level granularity; PART 2 internal rows say `PART 2 STEP E`, not `PART 2 readiness summary`). C-36 degraded to shared-header form (C-36 FAIL by design). C-38 absent (no terminal verdict, no ARCHITECTURE row for Terminal readiness). 11-row ARCHITECTURE.
**Hypothesis**: C-37's step-granular Consumed-by converts the ARCHITECTURE block into a single-read full-pipeline audit point. With section-level entries (e.g., "PART 2 readiness summary"), a reader must open the section to identify which step actually consumes the output -- the table does not close the pipeline visibility by itself. Step-granular entries make C-33/C-34/C-35 compliance checkable from the table without traversing PART 2 section by section.

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
| Root pattern: [label]                       | STEP 3                  | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN     | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                  |
| STEP C drift -- SEQUENCE: CLOSED/OPEN       | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                  |
| STEP C drift -- COHERENCE: CLOSED/OPEN      | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                  |
| STEP C drift -- STALENESS: CLOSED/OPEN      | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                  |
| Inertia case: BUILT/PARTIAL/OPEN            | PART 2 STEP A           | PART 2 STEP E (by label) [C-37 PASS: step-granular by design]             |
| Confirmed readiness: READY/COND./NOT READY  | PART 2 STEP D           | PART 2 STEP E (by label) [C-37 PASS: step-granular by design]             |

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
11. PART 2 STEP E opens with grouped annotation [C-36 FAIL by design]:
    Required inputs -- do not re-derive: Confirmed readiness from STEP D and Inertia case from STEP A
    [GROUPED -- C-36 FAIL and C-28 co-fail by design; single-axis isolation of C-37]
    No terminal verdict emitted [C-38 FAIL by design].

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

Required inputs -- do not re-derive: Confirmed readiness from STEP D and Inertia case from STEP A
[GROUPED annotation -- C-36 FAIL and C-28 co-fail by design; single-axis C-37 isolation]

From the two grounded inputs above -- state the team-facing position:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further
[No terminal verdict emitted -- C-38 FAIL by design]
```

---

## V-03 — Single Axis: C-36 (Independent Self-Standing Per-Input Prohibition at STEP E)

**Axes**: C-36 PASS (each per-input prohibition at STEP E is an independently parseable complete statement -- `Required input -- do not re-derive: [label]` as a standalone line, neither relying on the other's proximity for interpretation). C-37 degraded to section-level Consumed-by for PART 2 internal rows (C-37 FAIL by design). C-38 absent (no terminal verdict). 11-row ARCHITECTURE with section-level PART 2 rows.
**Hypothesis**: C-36 PASS implies C-28 PASS -- the independent self-standing form satisfies both the general per-input prohibition rule (C-28) and the convergence-point independence requirement (C-36). V-03 tests whether C-36 adds structural enforcement beyond what C-28/C-34 already achieve, or whether the two criteria name the same constraint at different scopes. If V-03 PASS is identical to R12 V-04 at the convergence point (same two-line form), C-36 is confirmatory rather than additive at execution time.

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
| Inertia case: BUILT/PARTIAL/OPEN            | PART 2 STEP A           | PART 2 readiness summary [C-37 FAIL: section-level by design]             |
| Confirmed readiness: READY/COND./NOT READY  | PART 2 STEP D           | PART 2 readiness summary [C-37 FAIL: section-level by design]             |

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
11. PART 2 STEP E opens with independent per-input prohibitions [C-36 PASS by design]:
    Required input -- do not re-derive: Confirmed readiness from STEP D
    Required input -- do not re-derive: Inertia case from STEP A
    Each annotation is a complete standalone statement -- neither relies on the other
    for interpretation. No terminal verdict emitted [C-38 FAIL by design].

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
[No terminal verdict emitted -- C-38 FAIL by design]
```

---

## V-04 — All Three Combined: C-36 + C-37 + C-38, Advisory Register (Canonical)

**Axes**: C-36 PASS (independent self-standing per-input prohibitions at STEP E) + C-37 PASS (all ARCHITECTURE rows step-granular; PART 2 internal rows say `PART 2 STEP E`) + C-38 PASS (STEP E emits `Terminal readiness: PROCEED / LOOP / INVESTIGATE` with ARCHITECTURE declaration), advisory register.
**Hypothesis**: V-04 is the canonical advisory form for R13. Twelve-row ARCHITECTURE table declares the full pipeline including the new terminal verdict row consumable by the topic namespace. STEP E is now the sole step that both consumes two named inputs AND produces one named output -- completing the chain symmetry that C-32 established at the PART 1-to-PART 2 boundary. C-36's independent self-standing form at STEP E makes selective compliance impossible: neither prohibition can be weakened without creating a locally visible absence. Lowest overhead for full v2 structural closure.

---

```markdown
Signal-check for {{topic}}.
Advisory -- observations the team can decide to act on, not a gate.

ARCHITECTURE -- Named-Output Pipeline

Each consuming step carries a separate "Required input -- do not re-derive: [label]"
per named input -- not grouped across multiple inputs at the same step.

| Named Output                                 | Produced by             | Consumed by                                                                |
|----------------------------------------------|-------------------------|----------------------------------------------------------------------------|
| [MECHANISM VERDICT]                          | CAUSAL GAP              | SEQUENCE (verbatim); PART 2 STEP A (verbatim)                              |
| Pre-specification gap: YES/NO                | SEQUENCE                | STEP 3 (by label); PART 2 STEP C SEQUENCE (by label)                       |
| Mechanism-relevant contradiction: YES/NO     | COHERENCE               | STEP 3 (by label); PART 2 STEP C COHERENCE (by label)                      |
| Mechanism-stale: YES/NO                      | STALENESS               | STEP 3 (by label); PART 2 STEP C STALENESS (by label)                      |
| Root pattern: [label]                        | STEP 3                  | PART 2 STEP B (by name); PART 2 STEP C per-dim (by name); PART 2 STEP D (by name) |
| STEP C drift -- CAUSAL GAP: CLOSED/OPEN      | PART 2 STEP C CAUSAL GAP| PART 2 STEP D (by label)                                                   |
| STEP C drift -- SEQUENCE: CLOSED/OPEN        | PART 2 STEP C SEQUENCE  | PART 2 STEP D (by label)                                                   |
| STEP C drift -- COHERENCE: CLOSED/OPEN       | PART 2 STEP C COHERENCE | PART 2 STEP D (by label)                                                   |
| STEP C drift -- STALENESS: CLOSED/OPEN       | PART 2 STEP C STALENESS | PART 2 STEP D (by label)                                                   |
| Inertia case: BUILT/PARTIAL/OPEN             | PART 2 STEP A           | PART 2 STEP E (by label)                                                   |
| Confirmed readiness: READY/COND./NOT READY   | PART 2 STEP D           | PART 2 STEP E (by label)                                                   |
| Terminal readiness: PROCEED/LOOP/INVESTIGATE | PART 2 STEP E           | topic namespace (by label)                                                 |

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
12. PART 2 STEP E closes with:
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
-> topic namespace: Required input -- do not re-derive: Terminal readiness. Consume by label.
```

---

## V-05 — All Three Combined: C-36 + C-37 + C-38, Imperative Register

**Axes**: C-36 PASS + C-37 PASS + C-38 PASS, imperative register. Required-output framing for terminal verdict elevates C-38 from a labeled advisory output to a mandatory production constraint. Schema ARCHITECTURE lists 12 named outputs with step-granular consuming steps. Per-input independent self-standing form throughout (C-36 via required-input framing). Highest precision, highest overhead.
**Hypothesis**: Imperative `Required output -- emit exactly: Terminal readiness: [PROCEED / LOOP / INVESTIGATE]` makes C-38 an architectural constraint -- the terminal verdict cannot be omitted without a locally visible missing `Required output`. Schema ARCHITECTURE satisfies C-25/C-35 with explicit consuming-step naming. C-37 in schema form: each entry names the specific consuming step. C-27 exception applies: schema form is valid on the imperative register.

---

```markdown
Signal-check for {{topic}}.
Imperative form -- follow exactly. Each required input must be consumed by its label.
Each required output must be emitted with its exact label before proceeding.

ARCHITECTURE -- Named-Output Pipeline (schema form; imperative register)

Meta-rule: every consuming step carries a separate "Required input -- do not re-derive:
[label]" per named input -- not grouped.

Named outputs and consuming steps:
  1.  [MECHANISM VERDICT]                          Produced: CAUSAL GAP          Consumed: SEQUENCE (verbatim), PART 2 STEP A (verbatim)
  2.  Pre-specification gap: YES/NO                Produced: SEQUENCE            Consumed: STEP 3 (by label), PART 2 STEP C SEQUENCE (by label)
  3.  Mechanism-relevant contradiction: YES/NO     Produced: COHERENCE           Consumed: STEP 3 (by label), PART 2 STEP C COHERENCE (by label)
  4.  Mechanism-stale: YES/NO                      Produced: STALENESS           Consumed: STEP 3 (by label), PART 2 STEP C STALENESS (by label)
  5.  Root pattern: [label]                        Produced: STEP 3              Consumed: PART 2 STEP B (by name), PART 2 STEP C per-dim (by name), PART 2 STEP D (by name)
  6.  STEP C drift -- CAUSAL GAP: CLOSED/OPEN      Produced: PART 2 STEP C CG    Consumed: PART 2 STEP D (by label)
  7.  STEP C drift -- SEQUENCE: CLOSED/OPEN        Produced: PART 2 STEP C SEQ   Consumed: PART 2 STEP D (by label)
  8.  STEP C drift -- COHERENCE: CLOSED/OPEN       Produced: PART 2 STEP C COH   Consumed: PART 2 STEP D (by label)
  9.  STEP C drift -- STALENESS: CLOSED/OPEN       Produced: PART 2 STEP C STA   Consumed: PART 2 STEP D (by label)
  10. Inertia case: BUILT/PARTIAL/OPEN             Produced: PART 2 STEP A       Consumed: PART 2 STEP E (by label -- separate prohibition)
  11. Confirmed readiness: READY/COND./NOT READY   Produced: PART 2 STEP D       Consumed: PART 2 STEP E (by label -- separate prohibition)
  12. Terminal readiness: PROCEED/LOOP/INVESTIGATE Produced: PART 2 STEP E       Consumed: topic namespace (by label)

Two parts in order. Do not merge.
PART 1 -- ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 -- TEAM COACHING REPORT: advisory observations. No severity labels.

Required structural outputs (emit each with its exact label):
  CAUSAL GAP   -> [MECHANISM VERDICT: ...]
  SEQUENCE     -> Pre-specification gap: YES/NO
  COHERENCE    -> Mechanism-relevant contradiction: YES/NO
  STALENESS    -> Mechanism-stale: YES/NO
  STEP 3       -> Root pattern: [SHORT NAME]
  PART 2 STEP C each dim -> STEP C drift: CLOSED/OPEN
  PART 2 STEP A -> Inertia case: BUILT/PARTIAL/OPEN
  PART 2 STEP D -> Confirmed readiness: READY/CONDITIONALLY READY/NOT READY
  PART 2 STEP E -> Terminal readiness: PROCEED/LOOP/INVESTIGATE

======================================================================
PART 1 -- ANALYTICAL RECORD  (internal -- not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

State the status-quo alternative for {{topic}} in one sentence before the inventory.
This is the inertia competitor against which all mechanism evidence is evaluated.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|
(Inertia Relevant: yes if artifact speaks to the comparison between {{topic}} and
the status-quo alternative; no otherwise.)

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each -- expected gap or meaningful blind spot?

Required output -- derive threshold from inventory:
  1 or more inertia-relevant artifacts -> staleness threshold = 14 days
  0 inertia-relevant artifacts         -> staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS -- CAUSAL GAP FIRST  (~540 words) ====

Order: CAUSAL GAP -> SEQUENCE -> COHERENCE -> STALENESS.

### CAUSAL GAP

Required output -- emit inertia-relevant pool list before analysis:
  Inertia-relevant pool: [every artifact tagged yes in Step 1]

If pool EMPTY: mechanism verdict is absent by default; state explicitly; name
  artifact types that would populate the pool; do not draw on non-pool artifacts.
If pool NON-EMPTY: evaluate whether evidence exists for the pathway from {{topic}}
  to its claimed outcome specifically better than the status-quo alternative.
  State: present / partial / absent.

(internal: green / yellow / red)
If yellow or red -> next action:

Required output -- emit before leaving CAUSAL GAP:
  [MECHANISM VERDICT: present / partial / absent -- key gap if any: ___]
  <- SEQUENCE consumes: Required input -- do not re-derive: [MECHANISM VERDICT]
  <- PART 2 STEP A consumes: Required input -- do not re-derive: [MECHANISM VERDICT]

### SEQUENCE

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT -- paste verbatim]"

Cite 2+ artifacts with dates. Evaluate: did discovery precede specification?
Through mechanism lens: did inertia-relevant pool artifacts appear in discovery,
or did the team specify before mechanism evidence existed?
(internal: green / yellow / red)
If yellow or red -> next action:

Required output -- emit before leaving SEQUENCE:
  Pre-specification gap: [YES / NO + reason]
  <- STEP 3 consumes: Required input -- do not re-derive: Pre-specification gap
  <- PART 2 STEP C SEQUENCE consumes: Required input -- do not re-derive: Pre-specification gap

### COHERENCE

Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
Tag each contradiction as mechanism-relevant or not.
(internal: green / yellow / red)
If yellow or red -> next action:

Required output -- emit before leaving COHERENCE:
  Mechanism-relevant contradiction: [YES / NO + reason]
  <- STEP 3 consumes: Required input -- do not re-derive: Mechanism-relevant contradiction
  <- PART 2 STEP C COHERENCE consumes: Required input -- do not re-derive: Mechanism-relevant contradiction

### STALENESS

Apply threshold from Step 1 (14 or 30 days).
(internal: green / yellow / red)
If yellow or red -> next action:

Required output -- emit before leaving STALENESS:
  Mechanism-stale: [YES / NO + reason]
  <- STEP 3 consumes: Required input -- do not re-derive: Mechanism-stale
  <- PART 2 STEP C STALENESS consumes: Required input -- do not re-derive: Mechanism-stale

==== STEP 3: CROSS-DIMENSION PATTERN  (~90 words) ====

Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
Required input -- do not re-derive: Mechanism-stale from STALENESS
Pool status: [empty / thin / adequate -- from CAUSAL GAP]

Pattern lookup from named outputs:
- Pre-specification gap YES + thin/empty pool -> "Commitment before evidence"
- Mechanism-stale YES + partial verdict -> "Stale mechanism comparison"
- Mechanism-relevant contradiction YES + partial/absent -> "Mechanism contradiction"
- Empty pool -> "Empty inertia pool"
- No shared root -> "Isolated flags" or "none"

Required output -- emit before leaving STEP 3:
  Root pattern: [SHORT NAME]
  <- PART 2 STEP B consumes: Required input -- do not re-derive: Root pattern
  <- PART 2 STEP C per-dimension consumes: Required input -- do not re-derive: Root pattern
  <- PART 2 STEP D consumes: Required input -- do not re-derive: Root pattern

======================================================================
PART 2 -- TEAM COACHING REPORT  (advisory -- no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~100 words) ====

Required input -- do not re-derive: [MECHANISM VERDICT]
Quoting mechanism verdict: "[MECHANISM VERDICT -- paste verbatim]"

Based on that verdict and the full artifact record: is the case that {{topic}}
beats doing nothing clearly built, partially built, or still open?
  [ ] Clearly built -- mechanism evidence present, status-quo comparison addressed
  [ ] Partially built -- gaps remain; name the key one
  [ ] Still open -- mechanism or comparison not established

Advisory -- not a gate.

Required output -- emit exactly:
  Inertia case: [BUILT / PARTIAL / OPEN + one-phrase reason]
  -> PART 2 STEP E: Required input -- do not re-derive: Inertia case. Consume by label.

==== STEP B: DRAFT READINESS  (~75 words) ====

Required input -- do not re-derive: Root pattern from STEP 3

Draft the team-facing readiness position from Part 1 findings.
If Root pattern is not "none" or "Isolated flags": name it before observations.
Label: [DRAFT -- to be confirmed after STEP D and finalized in STEP E]

==== STEP C: DIMENSION OBSERVATIONS  (~340 words) ====

CAUSAL GAP-first. Advisory. No severity labels.
Each dimension: consume named binary, state Root pattern contribution, emit drift binary.

CAUSAL GAP:
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  Required output -- emit exactly: STEP C drift -- CAUSAL GAP: [CLOSED / OPEN + reason]
  <- PART 2 STEP D consumes: Required input -- do not re-derive: STEP C drift -- CAUSAL GAP
  If flagged -> suggested next step:

SEQUENCE:
  Required input -- do not re-derive: Pre-specification gap from SEQUENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  Required output -- emit exactly: STEP C drift -- SEQUENCE: [CLOSED / OPEN + reason]
  <- PART 2 STEP D consumes: Required input -- do not re-derive: STEP C drift -- SEQUENCE
  If flagged -> suggested next step:

COHERENCE:
  Required input -- do not re-derive: Mechanism-relevant contradiction from COHERENCE
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  Required output -- emit exactly: STEP C drift -- COHERENCE: [CLOSED / OPEN + reason]
  <- PART 2 STEP D consumes: Required input -- do not re-derive: STEP C drift -- COHERENCE
  If flagged -> suggested next step:

STALENESS:
  Required input -- do not re-derive: Mechanism-stale from STALENESS
  Required input -- do not re-derive: Root pattern from STEP 3
  Root pattern contribution: [contributed / isolated flag]
  Required output -- emit exactly: STEP C drift -- STALENESS: [CLOSED / OPEN + reason]
  <- PART 2 STEP D consumes: Required input -- do not re-derive: STEP C drift -- STALENESS
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

Required output -- emit exactly:
  Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY + reason]
  -> PART 2 STEP E: Required input -- do not re-derive: Confirmed readiness. Consume by label.

==== STEP E: TEAM READINESS POSITION  (~90 words) ====

Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A

State the team-facing position from the two grounded inputs:

1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Confirmed readiness: [READY / CONDITIONALLY READY / NOT READY]
4. Inertia case: [BUILT / PARTIAL / OPEN]
5. Overall read: proceed / loop once more / investigate further

Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason]
  -> topic namespace: Required input -- do not re-derive: Terminal readiness. Consume by label.
```

---
