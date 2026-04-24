Here are the 5 R5 variations:

---

## V-01 — Role sequence (6-role ARTIFACT: chain)
**Axis:** Role sequence
**Hypothesis:** Declaring the `ARTIFACT:` prefix convention as the first structural element — before any role produces output — makes C-19 explicit and formal. Adding `Freshness verdict: FRESH | STALE` as a required field in every BOUNDARY CHECK closes C-21. The C-20 write-order prohibition from R4 V-01 is retained. Net effect: R4 V-01's 11/11 aspirational record + C-19/C-20/C-21.

---

## V-02 — Output format (Citation Registry table + A-xx tokens)
**Axis:** Output format
**Hypothesis:** A formal CITATION REGISTRY table at the top with `[A-xx]` tokens creates a machine-parseable namespace (C-19). C-21 is R-10 — a dedicated numbered requirement parallel to R-08 (elapsed) and R-09 (deferral prohibition). The write-order prohibition (C-20) is R-09b, explicitly separated from the placement instruction in R-06.

---

## V-03 — Phrasing register (directive-conversational + Protocol Rules)
**Axis:** Phrasing register
**Hypothesis:** Three named Protocol Rules (SC-1/SC-2/SC-3) at the top address C-19/C-20/C-21 explicitly before any role begins. Conversational imperative voice ("Stop. Do not write...") makes the write-order prohibition feel procedural rather than bureaucratic.

---

## V-04 — Combined: Lifecycle emphasis + inertia framing
**Axes:** Lifecycle emphasis + inertia framing
**Hypothesis:** The Phase 2 GATE contains a tick item for `Freshness verdict: FRESH | STALE` — making C-21 a phase prerequisite that blocks Phase 3 if any boundary lacks a verdict. The ARTIFACT: convention is declared in a preamble. The write-order prohibition is stated inline in Phase 2.

---

## V-05 — Combined: Baseline-first role sequence + Declarative constraint section
**Axes:** Role sequence + declarative structure
**Hypothesis:** A STRUCTURAL CONSTRAINTS section (SC-1/SC-2/SC-3) precedes all role output, making C-19/C-20/C-21 visible as named constraints before any content is written. `[A-xx]` token notation is shorter than `ARTIFACT:` prefix while equally machine-parseable. Baseline-first ordering grounds all vocabulary in incumbent failure evidence.

---

**C-19/C-20/C-21 coverage per variation:**

| | C-19 mechanism | C-20 mechanism | C-21 mechanism |
|--|----------------|----------------|----------------|
| V-01 | `ARTIFACT:` prefix + `Citing: ARTIFACT:` form declared upfront | "Do not write the next stage until every field in this block is complete." | `Freshness verdict: FRESH \| STALE` required field in every BOUNDARY CHECK |
| V-02 | CITATION REGISTRY table with `[A-xx]` tokens | R-09 standalone prohibition separate from placement instruction | R-10 dedicated requirement; missing verdict = non-compliant block |
| V-03 | SC-1 Protocol Rule + ARTIFACT REGISTRY with exact labels | SC-2 Protocol Rule + inline "Stop." + "SC-2 prohibits advancement" | SC-3 Protocol Rule + required verdict field in BOUNDARY CHECK |
| V-04 | `ARTIFACT:` prefix convention declared in preamble | Write-order prohibition in Phase 2 + Phase 2 GATE tick item | Phase 2 GATE tick item: every boundary must have `Freshness verdict` |
| V-05 | SC-1 with `[A-xx]` token registry in STRUCTURAL CONSTRAINTS | SC-2 constraint + "Per SC-2, Stage N+1 may not be written until both are present" | SC-3 constraint + required `Freshness verdict` field |
shold set at [N] because Citing: ARTIFACT: INCUMBENT
   BASELINE Failure F-02 established [X-duration] delays caused [business
   harm]. [N] is the maximum tolerable window."

Immediately below the threshold, write this block in full (fill in brackets):

    IMMUTABLE THRESHOLD — locked as of ARTIFACT: DOMAIN CONTEXT
    Value: [entity] must not exceed [N] [unit] at [destination]
    This value is fixed. No role after this point may revise it.
    If ROLE 3 pipeline timing implies a tighter threshold is warranted,
    record it as a recommendation in ROLE 6 only. This contract value
    does not change.

---

## ROLE 3 — Pipeline Engineer

Begin: "Citing: ARTIFACT: DOMAIN CONTEXT"

Trace the data lineage through every stage. For each stage, write:

    ARTIFACT: STAGE N — [Stage Name]
    Schema in:  [field names and types at stage entry, or diff from prior stage]
    Schema out: [all changes — renames, drops, type changes; "unchanged" if none]
    Latency:    [value, range, or characterization]
    Loss point: [specific named risk — name the entity and failure mechanism;
                "errors may occur" fails this field]
    F-analog:   [F-01 / F-02 / none — Citing: ARTIFACT: INCUMBENT BASELINE
                if this loss point has an incumbent predecessor]

After each consecutive stage pair, write the following BOUNDARY CHECK block.
Do not write the next stage until every field in this block is complete.

    ARTIFACT: BOUNDARY CHECK [Stage N → Stage N+1]
    Citing: ARTIFACT: DOMAIN CONTEXT
    Entity: [exact name from ARTIFACT: DOMAIN CONTEXT —
            "data" or "records" fails this field]
    Error handling: [specific named mechanism] OR [NONE — flag for ROLE 5]
    Latency this boundary: [value]
    Elapsed (cumulative): [sum of all prior stage latencies and boundary
                          latencies, computed here in this block — not
                          deferred to a post-stage summary]
    Freshness verdict: FRESH | STALE
                       [compare Elapsed (cumulative) against the threshold
                        in ARTIFACT: DOMAIN CONTEXT; if elapsed <= threshold:
                        FRESH; if elapsed > threshold: STALE — state it here,
                        not in a later section]

`Elapsed (cumulative)` and `Freshness verdict` are required fields in every
BOUNDARY CHECK block. Neither may be deferred. Stage N+1 may not be written
until this block is fully complete.

---

## ROLE 4 — Stale Data Analyst

Begin: "Citing: ARTIFACT: DOMAIN CONTEXT and ARTIFACT: BOUNDARY CHECK blocks
from ROLE 3"

Produce:

    ARTIFACT: STALE ANALYSIS

Write this table:

| Entity | ARTIFACT: DOMAIN CONTEXT threshold | ROLE 3 final boundary elapsed | Delta | Status | Scenario |
|--------|-------------------------------------|-------------------------------|-------|--------|----------|
| [name] | [N unit] | [from ROLE 3 final BOUNDARY CHECK] | [elapsed - N] | WITHIN SLA or STALE | Normal |
| [name] | [N unit] | [retry/failure-mode elapsed] | [delta] | [status] | Failure mode |

Close: "Citing: ARTIFACT: INCUMBENT BASELINE F-02 produced [X-duration] delay.
Pipeline failure mode elapsed: [Y]. ARTIFACT: DOMAIN CONTEXT threshold: [N].
F-02 [has been resolved / has not been resolved]."

Derive all values from ARTIFACT: DOMAIN CONTEXT and ROLE 3 blocks.
Do not assert staleness independently.

---

## ROLE 5 — Recovery Architect

Begin: "Citing: ARTIFACT: BOUNDARY CHECK blocks from ROLE 3 and
ARTIFACT: INCUMBENT BASELINE"

Produce:

    ARTIFACT: RECOVERY PRESCRIPTIONS

For each BOUNDARY CHECK from ROLE 3 with Error handling = NONE, and for each
Stage loss point:

- Prescribe one specific recovery mechanism by name (e.g., dead-letter queue,
  idempotent upsert, saga rollback — not generic "add retry logic")
- Where the loss point has a predecessor in ARTIFACT: INCUMBENT BASELINE:
  "Citing: ARTIFACT: INCUMBENT BASELINE [F-01/F-02]: [quote failure].
  Prescription closes it by [mechanism]."

---

## ROLE 6 — Pattern Advisor

Begin: "Citing: ARTIFACT: INCUMBENT BASELINE and
ARTIFACT: RECOVERY PRESCRIPTIONS"

Produce:

    ARTIFACT: PATTERN TRADE-OFF

Name one alternative pipeline pattern. Write this table:

| Dimension | Current pipeline | Alternative: [name] | Citing: ARTIFACT: INCUMBENT BASELINE |
|-----------|-----------------|---------------------|--------------------------------------|
| [dim 1 — latency or throughput] | | | [F-01 or F-02 citation, or "not applicable"] |
| [dim 2 — failure mode or ops burden] | | | [F-01 or F-02 citation, or "not applicable"] |

At least one row must cite ARTIFACT: INCUMBENT BASELINE. A table with no
incumbent reference fails this section.

If ROLE 3 timing implied a tighter threshold than ARTIFACT: DOMAIN CONTEXT's
IMMUTABLE THRESHOLD, state the recommendation here. This is the only location
where threshold recommendations are permitted.

---

## Scenario

{scenario}

## Output order

ARTIFACT: INCUMBENT BASELINE (ROLE 1) →
ARTIFACT: DOMAIN CONTEXT with IMMUTABLE THRESHOLD (ROLE 2) →
ARTIFACT: STAGE N blocks with interleaved ARTIFACT: BOUNDARY CHECK blocks (ROLE 3) →
ARTIFACT: STALE ANALYSIS (ROLE 4) →
ARTIFACT: RECOVERY PRESCRIPTIONS (ROLE 5) →
ARTIFACT: PATTERN TRADE-OFF (ROLE 6)
```

---

## V-02 — Axis: Output format (Citation Registry table + A-xx token scheme)

**Hypothesis:** A formal CITATION REGISTRY table at the top — listing every artifact name
with its owner requirement and its citation token — creates a machine-parseable namespace
that satisfies C-19 more explicitly than an inline prefix declaration. Requirement IDs
(R-01..R-13) govern structure; A-01..A-06 artifact tokens govern citations. C-21 is
enforced as a dedicated numbered requirement (R-10) parallel to R-08 (elapsed) and R-09
(deferral prohibition). The write-order prohibition (C-20) appears as R-09b — a standalone
prohibition separate from the placement instruction in R-06.

---

```
You are running the flow-dataflow skill.

## CITATION CONVENTION

All named artifacts in this trace use token-based citations from the registry
below. Registration format when producing an artifact:

    ## [A-xx]: [Artifact Name]

Citation format when referencing an artifact:

    [Citing A-xx: Artifact Name]

The A-xx tokens are the machine-parseable identifiers for this trace. Every
citation must use the token form above. Ad hoc labels ("the section above",
"the prior table") are non-compliant. The convention applies uniformly to
every role and every structured block.

### Citation Registry (declare before writing any output)

| Token | Artifact Name | Owner | Description |
|-------|--------------|-------|-------------|
| A-01 | INCUMBENT BASELINE | R-01 | Incumbent process failures and entity vocabulary |
| A-02 | DOMAIN CONTEXT | R-02/R-03/R-04 | Entity names, staleness threshold, immutability |
| A-03 | STAGE TRACE | R-05 | Stage blocks with schema, latency, and loss points |
| A-04 | BOUNDARY CHECKS | R-06..R-10 | Interleaved boundary blocks: elapsed, verdict |
| A-05 | STALE ANALYSIS | R-11/R-12 | Threshold vs. elapsed evaluation table |
| A-06 | RECOVERY + TRADE-OFF | R-13/R-14 | Recovery prescriptions and pattern comparison |

Every artifact header must begin with ## [A-xx]: and every citation must use
[Citing A-xx: ...]. No exceptions.

---

## PHASE 1 — Pre-Trace Declarations

R-01  Write section ## [A-01]: INCUMBENT BASELINE.
      Declare:
      (a) Entity name — the exact business name of what flows through this
          pipeline. "Data" and "records" are not entity names.
      (b) Incumbent process — the manual or legacy process this pipeline
          replaced.
      (c) Business cadence — how often the incumbent process produced output.
      (d) Downstream consumer — team name and decision cycle they ran.
      (e) F-01 — a specific data loss or corruption failure (name entity +
          mechanism).
      (f) F-02 — a specific lateness or staleness failure. Include a concrete
          time magnitude.
      Label F-01 and F-02 explicitly for citation by subsequent requirements.

R-02  Write section ## [A-02]: DOMAIN CONTEXT.
      First content line: "[Citing A-01: INCUMBENT BASELINE]"
      Use only entity names introduced in A-01. No substitution or renaming.
      Declare: entity vocabulary, downstream consumer, business cadence, and:
      Staleness threshold: "[entity] must not exceed [N] [unit] at [destination]"

R-03  In A-02, connect the threshold to A-01 F-02:
      "Threshold set at [N] because [Citing A-01: INCUMBENT BASELINE] F-02
      established [X-duration] delays caused [business harm]. [N] caps that
      failure window."

R-04  Immediately after the threshold in A-02, write the following sentence
      verbatim (fill in brackets):
      "This threshold ([N] [unit]) is fixed as of [A-02]: DOMAIN CONTEXT.
      It may not be revised by any requirement below. If pipeline timing
      implies a tighter value is warranted, record it as a recommendation
      in R-14 only."
      This prohibition is required. A threshold declaration without this
      exact prohibition sentence does not satisfy R-04.

---

## PHASE 2 — Pipeline Trace

R-05  Write section ## [A-03]: STAGE TRACE.
      For each stage, use this block:

        STAGE N — [Stage Name]
        Schema in:  [fields at stage entry, or diff from prior stage exit]
        Schema out: [all changes — renames, drops, type changes; "unchanged" if none]
        Latency:    [value, range, or characterization]
        Loss point: [specific named risk — "errors may occur" fails this field]
        A-01 analog: [F-01 / F-02 / none — cite [Citing A-01: ...] if applicable]

R-06  Write section ## [A-04]: BOUNDARY CHECKS.
      After every consecutive stage pair, write a BOUNDARY CHECK block:

        BOUNDARY CHECK [Stage N → Stage N+1]
        [Citing A-02: DOMAIN CONTEXT]
        Entity: [exact name from A-02 — "data" or "records" fails]
        Error handling: [named mechanism] OR [NONE]
        Latency this boundary: [value]
        Elapsed (cumulative): [per R-08]
        Freshness verdict: [per R-10]

R-07  The `Entity` field in every BOUNDARY CHECK must name a term from
      [A-02]: DOMAIN CONTEXT. "data" and "records" are non-compliant.

R-08  The `Elapsed (cumulative)` field in every BOUNDARY CHECK must contain
      the additive sum of all stage latencies and boundary latencies written
      in prior STAGE blocks and BOUNDARY CHECK blocks. Compute this field
      within the block at the time of writing — not deferred to a post-stage
      summary.

R-09  Stage N+1 may not be written until the BOUNDARY CHECK block between
      Stage N and Stage N+1 is fully written with all required fields
      present. This is an explicit write-order prohibition. A stage written
      before the preceding boundary block is complete does not comply with R-09.

R-10  Each BOUNDARY CHECK block must include a `Freshness verdict` field
      containing either FRESH or STALE, derived as follows:
        - Elapsed (cumulative) <= A-02 threshold: FRESH
        - Elapsed (cumulative) >  A-02 threshold: STALE
      A BOUNDARY CHECK block that contains `Elapsed (cumulative)` without
      a `Freshness verdict` does not satisfy R-10. A verdict appearing only
      in the final stale analysis does not satisfy R-10.

---

## PHASE 3 — Analysis and Closure

R-11  Write section ## [A-05]: STALE ANALYSIS.
      Begin: "[Citing A-02: DOMAIN CONTEXT] and [Citing A-04: BOUNDARY CHECKS]"
      Write this table:

      | Entity | A-02 threshold | A-04 final elapsed | Delta | Status | Scenario |
      |--------|----------------|--------------------|-------|--------|----------|
      | [name] | [N unit] | [from A-04 final block] | [elapsed - N] | WITHIN SLA or STALE | Normal |
      | [name] | [N unit] | [retry elapsed] | [delta] | [status] | Failure mode |

R-12  Close STALE ANALYSIS with one sentence:
      "[Citing A-01: INCUMBENT BASELINE] F-02 produced [X-duration] delay.
      Pipeline failure mode elapsed: [Y]. A-02 threshold: [N].
      F-02 [resolved / not resolved]."

R-13  Write recovery prescriptions in ## [A-06]: RECOVERY + TRADE-OFF.
      Begin: "[Citing A-04: BOUNDARY CHECKS] and [Citing A-01: INCUMBENT BASELINE]"
      For each A-04 BOUNDARY CHECK with Error handling = NONE, and each loss
      point from A-03: prescribe one specific named mechanism.
      Where the loss point has an A-01 analog:
      "[Citing A-01: INCUMBENT BASELINE] [F-01/F-02]: [quote failure].
      Prescription closes it by [mechanism]."

R-14  Write the pattern trade-off in ## [A-06] (continued).
      Begin: "[Citing A-01: INCUMBENT BASELINE]"
      Name one alternative pattern. Provide a table with at least two
      comparison dimensions. At least one row must cite A-01 by token.

      | Dimension | Current pipeline | Alternative: [name] | [Citing A-01] relevance |
      |-----------|-----------------|---------------------|------------------------|
      | [dim 1] | | | [F-01/F-02 citation] or "not applicable" |
      | [dim 2] | | | [F-01/F-02 citation] or "not applicable" |

      If analysis implies a tighter threshold than A-02's fixed value,
      state the recommendation here. R-14 is the only permitted location.

---

## Scenario

{scenario}

## Output order

## [A-01]: INCUMBENT BASELINE (R-01) →
## [A-02]: DOMAIN CONTEXT with R-04 prohibition (R-02/R-03/R-04) →
## [A-03]/[A-04]: STAGE and BOUNDARY CHECK blocks (R-05 through R-10) →
## [A-05]: STALE ANALYSIS (R-11/R-12) →
## [A-06]: RECOVERY + TRADE-OFF (R-13/R-14)
```

---

## V-03 — Axis: Phrasing register (directive-conversational + Protocol Rules)

**Hypothesis:** A conversational, imperative register ("Now declare...", "Stop. Before
writing...") that announces the citation convention as named Protocol Rules — SC-1
(citation), SC-2 (write-order), SC-3 (verdict) — satisfies C-19/C-20/C-21 while making
the prompt feel like a workshop directive rather than a specification document. The
ARTIFACT REGISTRY uses exact registered labels rather than structured tokens; SC-1
prohibits ad hoc prose citations by name. SC-2 states the write-order prohibition in
direct imperative voice. SC-3 makes the freshness verdict a named output obligation.

---

```
You are running the flow-dataflow skill.

## PROTOCOL RULES (read before writing anything)

**SC-1 — Citation convention.**
Every named artifact in this trace is listed in the ARTIFACT REGISTRY below.
Every reference to a prior artifact must include a `Citing:` line using the
exact label from the registry. Use the label verbatim. Do not use prose
references ("the section above", "the baseline we defined earlier"). If you
reference a prior artifact without a Citing: line using its registry label,
the citation is non-compliant. This rule applies to every role and every
structured block without exception.

**SC-2 — Write-order prohibition.**
You may not write Stage N+1 until the BOUNDARY CHECK for the boundary between
Stage N and Stage N+1 is fully written with all required fields present — including
the Freshness verdict. Stop at the boundary. Complete it. Then advance.

**SC-3 — Freshness verdict at every boundary.**
Every BOUNDARY CHECK must declare a binary verdict: FRESH or STALE. Derive it
by comparing the cumulative elapsed time against the staleness threshold declared
in DOMAIN CONTEXT. Elapsed <= threshold: FRESH. Elapsed > threshold: STALE.
A boundary block that computes elapsed time without stating a verdict does not
satisfy SC-3. The verdict may not appear only in the final stale analysis.

### ARTIFACT REGISTRY (exact labels for SC-1 citations)

    INCUMBENT BASELINE     — Role 1
    DOMAIN CONTEXT         — Role 2
    STAGE TRACE            — Role 3
    STALE ANALYSIS         — Role 4
    RECOVERY PLAN          — Role 5

---

## Role 1 — Tell me what existed before

Write INCUMBENT BASELINE now, before anything else.

Tell me:

- What is the exact business name of the entity that flows through this pipeline?
  Not "data." Not "records." The actual thing: Vendor Invoice, GL Journal Entry,
  Inventory Adjustment, Customer Order Event.
- What manual or legacy process did this pipeline replace? Name it.
- How often did that process run? Daily batch? Weekly close? Real-time?
- Who received the output of the incumbent process, and what decision did they make?
- What broke about the old way? Two specific failures:
  - **F-01**: a data loss or correctness failure — name the entity and what went wrong
  - **F-02**: a staleness or lateness failure — give a concrete time magnitude
    (e.g., "Purchase Orders were 14 hours stale when they reached the GL")

Label F-01 and F-02. They will be cited by label throughout.

---

## Role 2 — Lock the contract before we trace anything

Now declare DOMAIN CONTEXT.

Start the section with:
    Citing: INCUMBENT BASELINE

Using only the entity names from INCUMBENT BASELINE (carry verbatim, do not
rename):
- List the entity vocabulary — every in-scope business entity
- Name the downstream consumer and what decision cycle they run
- State the business cadence
- Declare the staleness threshold: "[entity] must not exceed [N] [unit]
  at [destination]"
  Ground it: "This threshold is derived from Citing: INCUMBENT BASELINE F-02,
  which showed [X-duration] delays caused [specific business harm]. [N] caps
  that failure window."

Right after the threshold, write this word for word (fill in brackets):

> **LOCK: This threshold ([N] [unit]) is fixed as of DOMAIN CONTEXT.
> No role after this point may change it. If Role 3 timing implies it
> needs to be tighter, flag that as a recommendation in Role 5.
> The contract value stays at [N] [unit].**

---

## Role 3 — Trace the pipeline; stop at every boundary

Start with:
    Citing: DOMAIN CONTEXT

For each stage, write this block:

    STAGE N — [Stage Name]
    Schema in:  [fields at stage entry, or diff from prior stage]
    Schema out: [every rename, drop, type change — or "unchanged"]
    Latency:    [value, range, or characterization]
    Loss point: [name the entity and the failure mechanism —
                not "errors may occur"]
    F-analog:   [F-01 / F-02 / none; Citing: INCUMBENT BASELINE if this
                matches an incumbent failure]

**After each stage, before writing the next one: stop.**

Write this BOUNDARY CHECK. Per SC-2, do not advance to the next stage until
this block is complete — including the Freshness verdict.

    BOUNDARY CHECK [Stage N → Stage N+1]
    Citing: DOMAIN CONTEXT
    Entity: [exact entity name from DOMAIN CONTEXT —
            "data" and "records" fail here]
    Error handling: [named mechanism] OR [NONE — needs a prescription in Role 5]
    Latency this boundary: [value]
    Elapsed (cumulative): [add up every stage latency and every boundary
                          latency written above — compute it here, now]
    Freshness verdict: FRESH | STALE
    [Per SC-3: compare Elapsed (cumulative) against the DOMAIN CONTEXT threshold.
     Elapsed <= threshold → FRESH. Elapsed > threshold → STALE. State it now.]

`Elapsed (cumulative)` and `Freshness verdict` are required. Both must be
written in this block. SC-2 prohibits the next stage until they are present.

---

## Role 4 — Score freshness against the contract

Start with:
    Citing: DOMAIN CONTEXT
    Citing: STAGE TRACE

Write STALE ANALYSIS:

| Entity | DOMAIN CONTEXT threshold | Final boundary elapsed | Delta | Status | Scenario |
|--------|--------------------------|------------------------|-------|--------|----------|
| [name] | [N unit] | [from last BOUNDARY CHECK] | [elapsed - N] | WITHIN SLA or STALE | Normal |
| [name] | [N unit] | [failure-mode elapsed] | [delta] | [status] | Failure mode |

Close with:
"Citing: INCUMBENT BASELINE — F-02 produced [X-duration] lag.
Pipeline failure mode: [Y]. DOMAIN CONTEXT threshold: [N].
F-02 [resolved / not resolved]."

All values derive from DOMAIN CONTEXT and the boundary check blocks.
Do not assert staleness from description alone.

---

## Role 5 — Close every open failure loop

Start with:
    Citing: STAGE TRACE (loss points and NONE boundaries)
    Citing: INCUMBENT BASELINE (F-01 / F-02 failure vocabulary)

Write RECOVERY PLAN.

For each BOUNDARY CHECK with Error handling = NONE, and for each stage loss point:

- Name the specific recovery mechanism (dead-letter queue, idempotent upsert,
  saga rollback, checkpoint-resume — name it, do not say "add retry logic")
- Where the loss point has an incumbent analog:
  "Citing: INCUMBENT BASELINE [F-01/F-02]: [quote the failure].
  This prescription closes it by [mechanism]."

Then: one alternative pipeline pattern. Two-dimension comparison:

| Dimension | Current | Alternative: [name] | Citing: INCUMBENT BASELINE |
|-----------|---------|---------------------|---------------------------|
| [dim 1 — latency or throughput] | | | [F-01/F-02 citation or "not applicable"] |
| [dim 2 — failure mode or ops] | | | [F-01/F-02 citation or "not applicable"] |

At least one row cites INCUMBENT BASELINE.

If Role 3 timing suggested a threshold tighter than the LOCKED value, state
the recommendation here.

---

## Scenario

{scenario}

## Output order

INCUMBENT BASELINE (Role 1) →
DOMAIN CONTEXT with LOCK (Role 2) →
Stage blocks with interleaved BOUNDARY CHECKs (Role 3) →
STALE ANALYSIS (Role 4) →
RECOVERY PLAN with pattern trade-off (Role 5)
```

---

## V-04 — Axis combination: Lifecycle emphasis (phase gates) + inertia framing

**Hypothesis:** Phase gates that check for `Freshness verdict` as a required gate field —
where the Phase 2 gate literally fails if any boundary block lacks a FRESH/STALE verdict —
make C-21 a structural phase prerequisite. The ARTIFACT: prefix convention is declared in
a preamble (C-19). The write-order prohibition appears in the Phase 2 stage instructions
as an explicit sequencing rule naming the gate condition (C-20). Phase gates also serve as
cross-role citation anchors: each phase gate references prior phase artifacts by name,
satisfying C-16 structurally via the gate checklist itself.

---

```
You are running the flow-dataflow skill.

This trace runs in four phases. Each phase ends with a PHASE GATE — a required
checklist you produce in your output before starting the next phase. Tick each
item explicitly. An unticked item means the phase is incomplete; repair the
artifact, tick it, then proceed.

## CITATION CONVENTION (applied before any phase output)

All named artifacts use the ARTIFACT: prefix. Registration:

    ARTIFACT: <NAME>   (first line of that section's header)

Citation:

    Citing: ARTIFACT: <NAME>

This convention applies uniformly to every phase, every block, and every
reference. Prose references ("as established above") are non-compliant.

### Artifact Registry (required registrations)

    ARTIFACT: INCUMBENT BASELINE
    ARTIFACT: DOMAIN CONTEXT
    ARTIFACT: BOUNDARY CHECK [Stage N → Stage N+1]   (one per boundary pair)
    ARTIFACT: STALE ANALYSIS
    ARTIFACT: RECOVERY AND TRADE-OFF

---

## PHASE 1 — Establish the Frame

You are a Finance, Operations, or Commerce domain expert who received the output
of the incumbent process and can characterize its failures firsthand.

### ARTIFACT: INCUMBENT BASELINE

Write this section before any stage work. Name:

- Entity: exact business name — not "data" or "records" (e.g., Vendor Invoice,
  GL Journal Entry, Customer Order Event, Inventory Adjustment)
- Incumbent process: the manual or legacy process this pipeline replaced
- Cadence: how often the incumbent ran
- Consumer: who received the output and what decision cycle it fed
- F-01: a specific data loss or correctness failure — name entity and mechanism
- F-02: a specific staleness or lateness failure — include time magnitude
  (e.g., "Supplier Shipment records were 11 hours stale entering the ERP")

Label F-01 and F-02 explicitly. They are citation targets for all subsequent phases.

### ARTIFACT: DOMAIN CONTEXT

Begin: "Citing: ARTIFACT: INCUMBENT BASELINE"

Using entity names from ARTIFACT: INCUMBENT BASELINE (no substitution), declare:

- Entity vocabulary (exact names — carry verbatim)
- Downstream consumer (carry from ARTIFACT: INCUMBENT BASELINE)
- Business cadence (carry from ARTIFACT: INCUMBENT BASELINE)
- Staleness threshold: "[entity] must not exceed [N] [unit] at [destination]"
  Grounding: "Citing: ARTIFACT: INCUMBENT BASELINE F-02: [quote]. [N] caps
  the [X-duration] delay F-02 allowed."

Immediately after the threshold:

    IMMUTABLE — locked as of ARTIFACT: DOMAIN CONTEXT
    This threshold ([N] [unit]) is fixed as of ARTIFACT: DOMAIN CONTEXT.
    No role or phase after this point may revise it.
    If Phase 2 timing implies a tighter value is needed, record it in Phase 4
    only. This contract value remains [N] [unit] throughout the trace.

### PHASE 1 GATE — tick before starting Phase 2

[ ] ARTIFACT: INCUMBENT BASELINE names F-01 and F-02 with explicit labels
[ ] ARTIFACT: DOMAIN CONTEXT uses only entity names from ARTIFACT: INCUMBENT BASELINE
[ ] Staleness threshold present and grounded in F-02 time magnitude
[ ] IMMUTABLE block present and explicitly prohibits revision by Phase 2 and Phase 3
[ ] All section headers use the ARTIFACT: prefix per the convention

All five must be ticked. Repair any unchecked item before proceeding.

---

## PHASE 2 — Trace the Pipeline

You are a pipeline engineer.

Begin: "Citing: ARTIFACT: DOMAIN CONTEXT"

For each stage, write:

    STAGE N — [Stage Name]
    Schema in:  [fields at stage entry, or diff from prior stage]
    Schema out: [all changes — renames, drops, type changes; "unchanged" if none]
    Latency:    [value, range, or characterization]
    Loss point: [specific named risk — name entity and failure mechanism]
    F-analog:   [F-01 / F-02 / none — Citing: ARTIFACT: INCUMBENT BASELINE if applicable]

After each consecutive stage pair, produce the following boundary block.
Do not write Stage N+1 until ARTIFACT: BOUNDARY CHECK [Stage N → Stage N+1]
is fully written with all required fields present. This is the write-order
rule: the boundary block is a prerequisite for stage advancement.

    ARTIFACT: BOUNDARY CHECK [Stage N → Stage N+1]
    Citing: ARTIFACT: DOMAIN CONTEXT
    Entity: [exact name from ARTIFACT: DOMAIN CONTEXT — "data"/"records" fail]
    Error handling: [named mechanism] OR [NONE]
    Latency this boundary: [value]
    Elapsed (cumulative): [additive sum of all stage and boundary latencies
                          written above — computed in this block, not deferred]
    Freshness verdict: FRESH | STALE
                       [compare Elapsed (cumulative) against ARTIFACT: DOMAIN
                        CONTEXT threshold; elapsed <= threshold: FRESH;
                        elapsed > threshold: STALE]

`Elapsed (cumulative)` and `Freshness verdict` are required fields. Neither
may be deferred. Stage N+1 may not be written until both are present in this block.

### PHASE 2 GATE — tick before starting Phase 3

[ ] Every consecutive stage pair has an interleaved ARTIFACT: BOUNDARY CHECK
[ ] Every boundary check names an Entity from ARTIFACT: DOMAIN CONTEXT
    (not "data" or "records")
[ ] Every boundary check has `Elapsed (cumulative)` computed additively
    from prior stage and boundary latencies
[ ] Every boundary check has `Freshness verdict: FRESH | STALE` derived
    from ARTIFACT: DOMAIN CONTEXT threshold
[ ] No stage was written before its preceding boundary block was complete

All five must be ticked. Repair any unchecked item before proceeding.

---

## PHASE 3 — Evaluate Freshness

You are a data quality analyst.

Begin: "Citing: ARTIFACT: DOMAIN CONTEXT and ARTIFACT: BOUNDARY CHECK blocks
from Phase 2"

Write:

    ARTIFACT: STALE ANALYSIS

| Entity | ARTIFACT: DOMAIN CONTEXT threshold | Phase 2 final elapsed | Delta | Status | Scenario |
|--------|------------------------------------|-----------------------|-------|--------|----------|
| [name] | [N unit] | [from Phase 2 final boundary] | [elapsed - N] | WITHIN SLA or STALE | Normal |
| [name] | [N unit] | [retry/failure-mode elapsed] | [delta] | [status] | Failure mode |

Close: "Citing: ARTIFACT: INCUMBENT BASELINE F-02: [quote]. Pipeline failure
mode elapsed: [Y]. ARTIFACT: DOMAIN CONTEXT threshold: [N].
F-02 [resolved / not resolved]."

All values derive from Phase 1 and Phase 2 outputs. No independent assertions.

### PHASE 3 GATE — tick before starting Phase 4

[ ] STALE ANALYSIS has one normal-operation row and one failure-mode row
[ ] Both rows cite ARTIFACT: DOMAIN CONTEXT threshold by name
[ ] Close sentence cites ARTIFACT: INCUMBENT BASELINE F-02 by label
[ ] All values derived from Phase 1 and Phase 2 outputs

All four must be ticked.

---

## PHASE 4 — Prescribe and Advise

You are a systems architect.

Begin: "Citing: ARTIFACT: BOUNDARY CHECK blocks from Phase 2 and
ARTIFACT: INCUMBENT BASELINE"

Write:

    ARTIFACT: RECOVERY AND TRADE-OFF

### Recovery Prescriptions

For each Phase 2 BOUNDARY CHECK with Error handling = NONE, and each loss
point from Phase 2 stages:

- Prescribe a specific named mechanism (dead-letter queue, idempotent upsert,
  saga rollback — name it)
- Close the incumbent loop: "Citing: ARTIFACT: INCUMBENT BASELINE [F-01/F-02]:
  [quote failure]. Prescription closes it by [mechanism]."

If Phase 2 timing implied the threshold should be tighter than the IMMUTABLE
value in ARTIFACT: DOMAIN CONTEXT, state the recommendation here. This is the
only permitted location.

### Pattern Trade-Off

Name one alternative pipeline pattern. Compare on at least two dimensions:

| Dimension | Current pipeline | Alternative: [name] | Citing: ARTIFACT: INCUMBENT BASELINE |
|-----------|-----------------|---------------------|--------------------------------------|
| [dim 1] | | | [F-01/F-02 citation or "not applicable"] |
| [dim 2] | | | [F-01/F-02 citation or "not applicable"] |

At least one row must cite ARTIFACT: INCUMBENT BASELINE.

---

## Scenario

{scenario}

## Output order

Phase 1: ARTIFACT: INCUMBENT BASELINE → ARTIFACT: DOMAIN CONTEXT → PHASE 1 GATE
Phase 2: Stage blocks with interleaved ARTIFACT: BOUNDARY CHECKs → PHASE 2 GATE
Phase 3: ARTIFACT: STALE ANALYSIS → PHASE 3 GATE
Phase 4: ARTIFACT: RECOVERY AND TRADE-OFF
```

---

## V-05 — Axis combination: Baseline-first role sequence + Structural Constraint Declaration

**Hypothesis:** Prefacing the entire prompt with a STRUCTURAL CONSTRAINTS section that
explicitly names C-19/C-20/C-21 as three enforced constraints (SC-1/SC-2/SC-3) — before
any role produces output — makes the requirements visible and parallel before any role
begins. Using [A-xx] token notation in both the registry and every citation creates a
shorter but equally machine-parseable convention than `ARTIFACT:` prefix. Baseline-first
role sequence (Role 1 = incumbent analyst before domain context) grounds all subsequent
vocabulary in known failure evidence.

---

```
You are running the flow-dataflow skill.

## STRUCTURAL CONSTRAINTS (read before writing any output)

The following three constraints govern this entire trace. They are enforced
requirements, not suggestions.

**SC-1 — Citation convention (machine-verifiable).**
Every named artifact is registered in the ARTIFACT REGISTRY below with a token
[A-01] through [A-06]. Every reference to a prior artifact must use the token
form: `[A-xx]`. References using prose ("the section above", "the baseline
we defined earlier") are non-compliant. The convention applies to every role
and every structured block without exception.

**SC-2 — Write-order prohibition.**
Stage N+1 may not be written until the BOUNDARY CHECK block between Stage N
and Stage N+1 is fully written with all required fields present. This is a
structural sequencing constraint. Writing stage content before the preceding
boundary block is complete violates SC-2.

**SC-3 — Binary freshness verdict per boundary.**
Every BOUNDARY CHECK block must include a `Freshness verdict: FRESH | STALE`
field, derived by comparing `Elapsed (cumulative)` against the staleness
threshold declared in [A-02] DOMAIN CONTEXT. A boundary block that records
elapsed time without a verdict field does not satisfy SC-3. A verdict
appearing only in the final stale analysis does not satisfy SC-3.

### ARTIFACT REGISTRY

| Token | Artifact Name | Owner | Description |
|-------|--------------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Role 1 | Incumbent process, entity vocabulary, F-01/F-02 |
| [A-02] | DOMAIN CONTEXT | Role 2 | Entity names, staleness threshold, immutability |
| [A-03] | STAGE TRACE | Role 3 | Stage blocks: schema, latency, loss points |
| [A-04] | BOUNDARY CHECKS | Role 3 | Interleaved blocks: elapsed, verdict |
| [A-05] | STALE ANALYSIS | Role 4 | Threshold vs. elapsed evaluation |
| [A-06] | CLOSURE | Role 5 | Recovery prescriptions and pattern trade-off |

All artifact headers must begin: ## [A-xx]: [Artifact Name]
All citations must use the [A-xx] token. No exceptions.

---

## ROLE 1 — Incumbent Process Analyst

Produce:

    ## [A-01]: INCUMBENT BASELINE

This role runs first — before domain context, before any stage. Write:

- Entity name: the exact business name of what flows through this pipeline.
  Not "data." Not "records." The actual term: Vendor Invoice, GL Journal Entry,
  Inventory Adjustment, Customer Order Event.
- Incumbent process: the manual or legacy pipeline or process this replaces.
- Business cadence: how often the incumbent ran.
- Downstream consumer: who received the output and what decision it fed.
- F-01: a specific data loss or corruption failure — name the entity and
  the mechanism.
- F-02: a specific staleness or lateness failure — include a concrete time
  magnitude.

Label F-01 and F-02 explicitly. They are citation targets for all roles below.

---

## ROLE 2 — Domain Contract Setter

Citing: [A-01] INCUMBENT BASELINE

Produce:

    ## [A-02]: DOMAIN CONTEXT

Use only entity names introduced in [A-01] INCUMBENT BASELINE. Carry verbatim.
Do not substitute, rename, or introduce new entity names. Declare:

1. Entity vocabulary (exact names from [A-01])
2. Downstream consumer (carry from [A-01])
3. Business cadence (carry from [A-01])
4. Staleness threshold: "[entity] must not exceed [N] [unit] at [destination]"
   Connection: "Threshold set at [N] because [A-01] INCUMBENT BASELINE F-02
   established [X-duration] delays caused [business harm]. [N] caps that window."

Immediately after the threshold, write this block in full (fill in brackets):

    IMMUTABLE THRESHOLD — locked as of [A-02]: DOMAIN CONTEXT
    Value: [entity] must not exceed [N] [unit] at [destination]
    Locked after: [A-02]: DOMAIN CONTEXT is written.
    Prohibited revisions: no role after this point may change this value.
    If [A-03] STAGE TRACE implies a tighter threshold, record it in
    [A-06] CLOSURE only. This contract value is [N] [unit].

---

## ROLE 3 — Pipeline Engineer

Citing: [A-02] DOMAIN CONTEXT

Produce:

    ## [A-03]: STAGE TRACE
    ## [A-04]: BOUNDARY CHECKS

For each stage, write:

    STAGE N — [Stage Name]
    Schema in:  [fields at stage entry, or diff from prior stage]
    Schema out: [all changes — renames, drops, type changes; "unchanged" if none]
    Latency:    [value, range, or characterization]
    Loss point: [specific named risk — name the entity and failure mechanism;
                "errors may occur" fails this field]
    [A-01] analog: [F-01 / F-02 / none — cite [A-01] if this loss point
                   has an incumbent predecessor]

Apply SC-2: do not write Stage N+1 until the following BOUNDARY CHECK block
is fully complete with all required fields.

    BOUNDARY CHECK [Stage N → Stage N+1]
    Citing: [A-02] DOMAIN CONTEXT
    Entity: [exact name from [A-02] — "data" or "records" fails this field]
    Error handling: [named mechanism] OR [NONE — flag for [A-06] CLOSURE]
    Latency this boundary: [value]
    Elapsed (cumulative): [additive sum of all stage and boundary latencies
                          written above — compute here, not in a later section]
    Freshness verdict: FRESH | STALE
                       [SC-3: compare Elapsed (cumulative) to [A-02] threshold;
                        elapsed <= threshold: FRESH;
                        elapsed > threshold: STALE]

`Elapsed (cumulative)` and `Freshness verdict` are required fields in every
boundary block. Per SC-2, Stage N+1 may not be written until both are present.

---

## ROLE 4 — Stale Data Analyst

Citing: [A-02] DOMAIN CONTEXT
Citing: [A-04] BOUNDARY CHECKS

Produce:

    ## [A-05]: STALE ANALYSIS

| Entity | [A-02] threshold | [A-04] final elapsed | Delta | Status | Scenario |
|--------|-----------------|----------------------|-------|--------|----------|
| [name] | [N unit] | [from [A-04] final block] | [elapsed - N] | WITHIN SLA or STALE | Normal |
| [name] | [N unit] | [failure-mode elapsed] | [delta] | [status] | Failure mode |

Close: "Citing: [A-01] INCUMBENT BASELINE F-02: [quote]. Pipeline failure
mode elapsed: [Y]. [A-02] threshold: [N]. F-02 [resolved / not resolved]."

Derive all values from [A-02] and [A-04]. Do not assert staleness independently.

---

## ROLE 5 — Closure Analyst

Citing: [A-01] INCUMBENT BASELINE
Citing: [A-04] BOUNDARY CHECKS

Produce:

    ## [A-06]: CLOSURE

### Recovery Prescriptions

For each [A-04] BOUNDARY CHECK with Error handling = NONE, and each loss point
from [A-03] STAGE TRACE:

- Prescribe one specific recovery mechanism by name.
- Close the incumbent loop: "Citing: [A-01] INCUMBENT BASELINE [F-01/F-02]:
  [quote failure]. Prescription closes it by [mechanism]."

If [A-03] STAGE TRACE timing implied a tighter threshold than [A-02]'s
IMMUTABLE value, state the recommendation here. This is the only permitted
location for threshold recommendations.

### Pattern Trade-Off

Name one alternative pipeline pattern. Compare on at least two dimensions:

| Dimension | Current pipeline | Alternative: [name] | Citing: [A-01] INCUMBENT BASELINE |
|-----------|-----------------|---------------------|-----------------------------------|
| [dim 1] | | | [F-01/F-02 citation] or "not applicable" |
| [dim 2] | | | [F-01/F-02 citation] or "not applicable" |

At least one row must cite [A-01] INCUMBENT BASELINE using the [A-01] token.

---

## Scenario

{scenario}

## Output order

## [A-01]: INCUMBENT BASELINE (Role 1) →
## [A-02]: DOMAIN CONTEXT with IMMUTABLE THRESHOLD (Role 2) →
## [A-03]/[A-04]: STAGE + BOUNDARY CHECK blocks (Role 3) →
## [A-05]: STALE ANALYSIS (Role 4) →
## [A-06]: CLOSURE (Role 5)
```

---

## Variation Summary — Round 5

| ID | Primary Axis | Secondary Axis | Key Innovation vs. R4 |
|----|-------------|---------------|----------------------|
| V-01 | Role sequence (6-role ARTIFACT: chain) | — | Explicit ARTIFACT: convention declaration at top (C-19); `Freshness verdict: FRESH | STALE` required in every BOUNDARY CHECK (C-21); C-20 write-order prohibition retained from R4 V-01 |
| V-02 | Output format (Citation Registry table + A-xx tokens) | — | Formal CITATION REGISTRY table (C-19); R-10 as dedicated freshness verdict requirement (C-21); R-09 as standalone write-order prohibition separate from R-06 placement instruction (C-20) |
| V-03 | Phrasing register (directive-conversational) | — | SC-1/SC-2/SC-3 named Protocol Rules at top; Citing: row convention with exact registry labels (C-19); SC-2 write-order prohibition stated in imperative voice (C-20); SC-3 verdict obligation (C-21) |
| V-04 | Lifecycle emphasis (phase gates) | Inertia framing (ARTIFACT: prefix) | Phase 2 GATE checks `Freshness verdict` as a required tick item (C-21 enforced as gate condition); ARTIFACT: prefix convention declared at top (C-19); explicit write-order prohibition in Phase 2 instructions (C-20) |
| V-05 | Role sequence (baseline-first) | Declarative constraint section (SC-1/SC-2/SC-3) | STRUCTURAL CONSTRAINTS section before all roles (C-19/C-20/C-21 named upfront); [A-xx] token scheme as registry (C-19); SC-2/SC-3 stated as constraints not instructions; baseline-first sequence grounds all vocabulary in incumbent failure evidence |

**C-19 mechanism per variation:**
- V-01: `ARTIFACT:` prefix with "Citing: ARTIFACT:" citation form
- V-02: CITATION REGISTRY table with `[A-xx]` tokens and `[Citing A-xx: Name]` form
- V-03: ARTIFACT REGISTRY with exact labels + required `Citing:` lines
- V-04: `ARTIFACT:` prefix convention with Artifact Registry + phase gate checks citation compliance
- V-05: `[A-xx]` token registry in STRUCTURAL CONSTRAINTS section

**C-20 mechanism per variation:**
- V-01: "Do not write the next stage until every field in this block is complete."
- V-02: R-09 standalone prohibition: "Stage N+1 may not be written until the BOUNDARY CHECK block... is fully written with all required fields present."
- V-03: SC-2 Protocol Rule + inline "Stop." directive + "SC-2 prohibits the next stage until they are present."
- V-04: "Do not write Stage N+1 until ARTIFACT: BOUNDARY CHECK... is fully written with all required fields present." + Phase 2 GATE checks compliance.
- V-05: SC-2 constraint + "Per SC-2, Stage N+1 may not be written until both are present."

**C-21 mechanism per variation:**
- V-01: `Freshness verdict: FRESH | STALE` required field in every BOUNDARY CHECK block
- V-02: R-10 dedicated requirement; "A BOUNDARY CHECK block that contains Elapsed (cumulative) without a Freshness verdict does not satisfy R-10."
- V-03: SC-3 Protocol Rule; `Freshness verdict: FRESH | STALE` required in boundary block; "SC-2 prohibits the next stage until [verdict is] present."
- V-04: `Freshness verdict: FRESH | STALE` in every boundary block; Phase 2 GATE item: "Every boundary check has Freshness verdict: FRESH | STALE"
- V-05: SC-3 constraint; `Freshness verdict: FRESH | STALE` required field in boundary block; "SC-2, Stage N+1 may not be written until both [elapsed and verdict] are present."
