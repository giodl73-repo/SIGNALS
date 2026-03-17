# flow-throttle Variate — Round 8
**Date:** 2026-03-15
**Rubric:** v22 (C-01 through C-32, essential/recommended/aspirational)
**Baseline ceiling:** R7 V-05 (C-28+C-29+C-30 in place; denominator now /24 aspirationals)

---

## State Analysis: What R7 V-05 Has vs. What R8 Must Add

**R7 V-05 coverage (confirmed):**
- C-28: All table contracts and role output specs expressed as validity predicates
- C-29: All gates expressed as cleared-when predicates
- C-30: Pre-committed audit contract declared before analytical roles

**C-31 failure in R7 V-05:**
GATE 3 has the negative invariant: "GATE 3 is not cleared while any `- [ ]` item remains
without a disposition." GATE 1 and GATE 2 have only the positive cleared-when form — no
explicit failure-state declaration. C-31 requires all gates to carry both; partial adoption
fails. GATE 1 and GATE 2 must gain the negative invariant in R8.

**C-32 failure in R7 V-05:**
GATE 3's closing predicate says "no `[FAIL]` item has an unwritten rewrite section" — this
requires a rewrite to exist but does not prescribe where it must appear. C-32 requires the
correction gate to instruct that rewrites appear "immediately below the `[FAIL]` annotation."
R7 V-02 had "Rewrite flagged sections below their `[FAIL]` annotations before any further
output" (line 510) which satisfied C-32 — but that instruction was replaced in V-05's
predicate rewrite by the location-agnostic "no `[FAIL]` item has an unwritten rewrite section."
The spatial prescription must be restored in R8.

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis | Target new criteria | Predicted composite |
|-----------|------|------------|---------------------|---------------------|
| V-01 | Lifecycle emphasis — inline negative invariant appended to GATE 1 and GATE 2 | Appending the failure-state clause inline (dash-separator form: "— no X may be absent, no Y may be blank") to structural gates achieves C-31 without disrupting the conditions-list form of cleared-when predicates already on GATE 1 and GATE 2; tests whether the inline dash form used in GATE 3 generalizes to structural gates whose conditions are lists rather than checkbox dispositions | C-31 | ~92/100 |
| V-02 | Lifecycle emphasis — spatially co-located rewrite mandate in correction gate | Restoring an explicit "immediately below" prescription as a validity predicate on the correction gate closes C-32 while preserving C-22 (per-token attestation), C-27 (role-scoped suspension), and C-29 (cleared-when form); the predicate form is "a rewrite is valid only when corrected content appears immediately below its `[FAIL]` annotation" | C-32 | ~90/100 |
| V-03 | Phrasing register — dual-block failure-state declaration on all gates | Instead of appending the failure state inline to the positive predicate (V-01 form), each gate gets a separate "**GATE N is not cleared when:**" block that lists the failure conditions as an independent statement; separating the two state declarations into visually distinct blocks may be more resilient to token pressure than the inline dash form when the positive predicate is already a long conditions list | C-31 (alt form) | ~89/100 |
| V-04 | Combined: inline negative invariant (C-31) + spatial rewrite prescription (C-32) | Both new criteria together on the R7 V-05 base; tests whether C-31 and C-32 interact positively and whether the combined gate language (GATE 1/GATE 2 with inline negation, GATE 3 with rewrite prescription) survives token pressure without degrading C-28 or C-30 | C-31 + C-32 | ~96/100 |
| V-05 | Combined: dual-block C-31 + spatial C-32 on full predicate base (maximum coverage) | Dual-block failure-state declarations (V-03 form) on all three gates PLUS the spatial rewrite prescription (V-02) on the correction gate, on the R7 V-05 base; tests whether the more verbose but independently-scannable dual-block form for C-31 produces higher composite than the inline form when combined with C-32 | C-31 (dual) + C-32 on C-28+C-29+C-30 base | ~99/100 |

**Primary questions this round asks:**

Q1: Does appending the negative invariant inline to GATE 1 and GATE 2 (V-01 dash form) achieve
C-31 compliance, or does the structural gate's conditions-list form resist the negative invariant
pattern that works on GATE 3's checkbox form? The key test: does "no X may be absent" at the
end of a five-condition cleared-when predicate survive token pressure equally well as at the
end of GATE 3's single-condition predicate?

Q2: Does expressing C-32 as a validity predicate ("a rewrite is valid only when it appears
immediately below its `[FAIL]` annotation") produce stronger spatial co-location than the R7 V-02
imperative form ("Rewrite flagged sections below their `[FAIL]` annotations before any further
output"), or does predicate form create enough ambiguity about who enforces the predicate that
the imperative was actually stronger?

Q3: When the negative invariant appears as a SEPARATE declared block ("GATE N is not cleared
when:") rather than appended to the positive predicate, does the model treat the two
declarations as a full-state specification (positive + negative) or does it interpret the
separation as two competing gate definitions?

Q4: In V-04, do the inline negative invariants on GATE 1/GATE 2 and the spatial rewrite
prescription on GATE 3 interact? Specifically: does adding the negative invariant to the
structural gates create precedent that makes GATE 3's existing negative invariant more visible,
or does the increased gate surface area crowd out other structural elements?

Q5: Does V-05's dual-block form for C-31 — more verbose, but with each state as an independent
declaration — produce higher composite than V-04's inline form, and does the extra verbosity
cost the pre-committed audit contract (C-30) through token pressure on the framing section?

---

## V-01 — Single-axis: Inline Negative Invariant on GATE 1 and GATE 2

**Axis:** Lifecycle emphasis — the cleared-when predicates on GATE 1 and GATE 2 gain an
explicit failure-state invariant appended with a dash separator: "— no [failure condition]".
GATE 3 already has this form in R7 V-05. Only GATE 1 and GATE 2 change. No C-32 changes.

**Hypothesis:** The inline dash-appended form "cleared when [positive conditions] — no X may
remain [negative constraint]" is the minimum change to achieve full-surface C-31 compliance.
It mirrors the pattern already in GATE 3, creating a consistent negative-invariant form across
all gates. The test is whether a five-condition cleared-when predicate (GATE 1) and a
three-condition cleared-when predicate (GATE 2) accept the appended negative form as cleanly
as GATE 3's single-condition checkbox form.

---

## PRE-COMMITTED AUDIT CONTRACT — ROLE 4

*This contract is declared before any analytical role begins. It is fixed and cannot be
modified at execution time.*

**Structural fact (this section is a system-state declaration, not an instruction):** Role 4
has no output in TABLE A, TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, or TABLE G. It did not
produce any component limits, propagation hops, tier-matrix arithmetic, or mitigation entries.
It cannot rationalize its own prior choices because it made none.

**Role 4 mandate: flags and verdict only.** Role 4 produces no root-cause explanations, fix
proposals, diagnostic analysis, or supplementary output of any kind. Its entire output
consists of flag items and a PASS/FAIL verdict.

**Verification checks (fixed before analytical output is produced):**

1. Cross-table component check: every component named in TABLE C must appear in TABLE A.
Flag any TABLE C component absent from TABLE A as a phantom, citing the exact hop number and
component name.

2. Arithmetic citation check: every numeric limit used in TABLE F calculations must trace to
a named TABLE A row, cited as "T-NN: [value]". Flag any TABLE F arithmetic asserting a limit
not in TABLE A, citing the TABLE F row and the asserted value.

3. Verdict format: PASS if no flags raised. FAIL with specific hop-number and row-number
citations for every flag raised.

*End of PRE-COMMITTED AUDIT CONTRACT — ROLE 4.*

---

Throughput analysis that tests only uniform load makes the status quo look safer than it is.
A connector integration with no Retry-After handling, no concurrency cap on the flow trigger,
and an undocumented limit on the backend API tier will pass uniform-rate testing. It will fail
in production on the first batch event, the first concurrent submission storm, the first
scheduled job that arrives while the previous run is still holding connections.

The burst-shape bottleneck is not a more extreme version of the steady-state bottleneck. It
is a different failure mode. The binding constraint can be a different tier, the propagation
chain can start from a different component, and the user-visible failure can arrive through a
different signal. This analysis requires both.

Unknown limits are not acceptable omissions. A tier with an undocumented limit is an
inventory member with `?-unresolved` status — it appears in TABLE A, it appears in TABLE B,
it appears in TABLE E, and its uncertainty status is the primary determinant of analysis risk
level.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

This analysis produces four required tables (TABLE A, TABLE C, TABLE F, TABLE G) and three
supplementary tables (TABLE B, TABLE D, TABLE E). All seven must appear with their declared
column structure intact. All table production contracts and role output specifications are
expressed as validity predicates. All gate invariants are expressed as cleared-when predicates.
Role 4's specification is pre-committed above.

---

**PASS 1 — COMPONENT-LIMIT INVENTORY**

TABLE A is valid when: (1) every system component that handles requests, enforces rate limits,
or sits on the request path appears as a row; (2) every Limit cell contains [number + unit],
`[estimated: value + basis]`, or `?-unresolved` — blank Limit cells are not valid; (3) every
Status cell contains exactly one of `confirmed`, `estimated`, `?-unresolved` — inline prose
uncertainty descriptions are not valid Status values; (4) every `?-unresolved` row has a
Notes cell with a named reason from: `undocumented`, `environment-specific`,
`requires-runtime-measurement`, `signal-insufficient`; (5) no component known from the input
signal is absent.

| Tier-ID | Component | Limit | Status | Scope | First-hit? | Notes |
|---------|-----------|-------|--------|-------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE A is valid only when every condition above holds; a prose component inventory does not constitute a valid TABLE A regardless of its analytical quality)* | | | | | | |
| T-01 | | | | | | |
| T-02 | | | | | | |

**GATE 1** is cleared when and only when: TABLE A has at least two rows; every Limit cell
is non-blank; every Status cell is one of the three named tokens; every `?-unresolved` row
has a named reason in Notes; no component known from the signal is absent — no TABLE A row
may be absent, no Limit cell may be blank, no Status cell may contain prose, no
`?-unresolved` row may have an empty Notes cell. TABLE B is valid only when GATE 1 is cleared.

---

**PASS 2 — TEMPORAL FAILURE PROFILE**

TABLE B is valid when: (1) every TABLE A tier has exactly one row; (2) every
Failure-visibility-window cell is non-blank; (3) every Recovery-time cell is non-blank;
(4) every Confidence cell is one of `CONFIRMED`, `ESTIMATED`, `UNKNOWN`; (5) every `UNKNOWN`
row has a non-empty Notes cell. A TABLE B that omits any TABLE A tier or leaves a temporal
cell blank is not valid.

| Tier-ID | Failure-visibility-window | Recovery-time | Confidence | Notes |
|---------|--------------------------|---------------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE B is valid only when every TABLE A tier appears with non-blank temporal values; omitting any tier or leaving temporal cells blank produces a not-valid TABLE B)* | | | | |
| T-01 | | | | |
| T-02 | | | | |

**GATE 2** is cleared when and only when: every TABLE A tier has a TABLE B row with non-blank
Failure-visibility-window and Recovery-time cells; every `UNKNOWN` entry has a reason in Notes
— no TABLE A tier may be absent from TABLE B, no Failure-visibility-window cell may be blank,
no Recovery-time cell may be blank, no `UNKNOWN` entry may lack a Notes reason. Downstream
phases are valid only when GATE 2 is cleared.

---

**DOWNSTREAM PHASES**

**Phase 1a output is valid when** it names: the Tier-ID of the uniform-rate binding constraint
(citing its TABLE A Limit value), and the causal reason this tier binds before all others.

**Phase 1b output is valid when** it names: the Tier-ID of the burst-arrival binding constraint
(citing TABLE A Limit value), and includes at least one numeric effective-rate comparison
between uniform and burst delivery for the relevant tiers.

**Phase 1c output is valid only when** it contains exactly this structure:

> Binding tier at uniform arrival: ___
> Binding tier at burst arrival: ___
> Verdict: SAME TIER / DIFFERENT TIER
> Explanation: ___

The Phase 1c explanation is valid when: if DIFFERENT TIER, it names both Tier-IDs and cites
their specific TABLE A Limit values; if SAME TIER, it cites the binding tier's TABLE A Limit
value and explains why burst shape does not shift the constraint. A Phase 1c explanation
without TABLE A Limit citations is not valid.

---

TABLE C is valid when: (1) it traces from the Phase 1b burst-rate binding tier; (2) it contains
at least two rows; (3) every Mechanism cell contains exactly one of: `queue-fill`,
`connection-hold`, `retry-amplification`, `dependency-stall`; (4) no cell in TABLE C contains:
"also throttled", "cascade occurs", "propagates to", "downstream effect", "flow is affected",
"rate limiting applies"; (5) every Observable-effect cell names a distinct outcome. A TABLE C
where any Mechanism cell contains a generic token from the prohibited vocabulary is not valid.

| Hop | From-component | To-component | Mechanism | Observable-effect |
|-----|---------------|--------------|-----------|-------------------|
| *(ANTI-SUBSTITUTION: TABLE C is valid only when every Mechanism cell contains a named token from the four-item vocabulary; narrative paragraph substitution produces a not-valid TABLE C)* | | | | |
| 1 | | | | |
| 2 | | | | |

---

TABLE D is valid when: (1) at least one row is present; (2) every Gap-reason names a specific
structural absence; (3) every `?-unresolved` TABLE A tier on an unprotected path is flagged
in the Gap-tier column. A TABLE D row with a generic Gap-reason is not valid.

| Path-ID | Entry-component | Gap-reason | Gap-tier? | Consequence-at-burst-volume |
|---------|----------------|------------|-----------|-----------------------------|
| *(ANTI-SUBSTITUTION: TABLE D is valid only when each Gap-reason names the specific absent control; "no protection" or similar generic entries do not produce a valid TABLE D row)* | | | | |
| P-01 | | | | |

---

TABLE E is valid when: (1) every TABLE A tier has exactly one row, including `?-unresolved`
tiers; (2) every Retry-After cell is `Y`, `N`, or `UNKNOWN`; (3) every Failure-if-ignored
cell is one of: `immediate-retry-storm`, `exponential-backoff-absent`, `silent-infinite-loop`,
`flow-run-failure`; (4) `?-unresolved` tier rows have Confirmed = `ESTIMATED`. A TABLE E that
omits any TABLE A tier or uses free-form failure descriptions is not valid.

| Tier-ID | Error-signal | Retry-After? | Visible-in-history? | Failure-if-ignored | Confirmed? |
|---------|-------------|--------------|---------------------|-------------------|------------|
| *(ANTI-SUBSTITUTION: TABLE E is valid only when all TABLE A tiers appear including gap tiers; free-form failure-mode descriptions are not valid Failure-if-ignored values)* | | | | | |
| T-01 | | | | | |

---

TABLE F is valid when: (1) it contains exactly four rows with Volume values `1×`, `3×`, `5×`,
`10×`; (2) every Binding-tier cell names a TABLE A Tier-ID; (3) every Threshold-hit cell
cites the TABLE A Limit as "T-NN: [value]"; (4) every Error-rate% cell contains arithmetic
steps that name each limit used — an asserted percentage without arithmetic steps is not a
valid Error-rate% cell; (5) all Threshold-hit citations trace to named TABLE A rows. A TABLE F
without exactly four fixed-multiplier rows or without arithmetic-derived Error-rate% values
is not valid.

| Volume | Binding-tier | Threshold-hit | Behavior | Error-rate% |
|--------|-------------|---------------|----------|-------------|
| *(ANTI-SUBSTITUTION: TABLE F is valid only when it has exactly four fixed-multiplier rows with step-by-step arithmetic in Error-rate%; a free-form tier summary does not constitute a valid TABLE F)* | | | | |
| 1× | | | | |
| 3× | | | | |
| 5× | | | | |
| 10× | | | | |

---

**CASCADE SCENARIO.** The cascade scenario is valid when: it names at least three tiers in a
causal chain where throttling at tier N triggers throttling at tier N+1; each link states a
specific mechanism from the TABLE C vocabulary; no step uses the generic prohibited token
vocabulary. A cascade scenario using generic tokens is not valid.

**RETRY-AFTER GAP ASSESSMENT.** This section is valid when it names either the specific
Retry-After header and confirms correct caller handling, or names the TABLE E Failure-if-ignored
token that results from absent handling.

---

TABLE G is valid when: (1) at least two gaps are covered; (2) every Remediation names a
specific Power Automate setting, connector configuration parameter, API field, or implementation
pattern — entries without a named specific control are not valid Remediation cells; (3) every
Specific-config cell is non-blank. A TABLE G with generic prescription entries is not valid.

| Gap-ID | Type | Remediation | Specific-config-or-API |
|--------|------|-------------|------------------------|
| *(ANTI-SUBSTITUTION: TABLE G is valid only when each Remediation names a specific actionable control; generic recommendations produce a not-valid TABLE G row)* | | | |
| G-01 | | | |
| G-02 | | | |

---

**CORRECTION GATE**

Role 2 output is valid when every item below has an explicit disposition. Role 2 produces no
further output while any item is unresolved.

**GATE 3** is cleared when and only when every item below carries either `[CLEAR]` or a
`[FAIL: location]` annotation — GATE 3 is not cleared while any `- [ ]` item remains without
a disposition, and Role 4 execution is not valid unless GATE 3 is cleared:

- [ ] "also throttled" → `[CLEAR]` if absent; `[FAIL: TABLE C hop N — rewritten below]` if present
- [ ] "cascade occurs" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "propagates to" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "downstream effect" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "flow is affected" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "rate limiting applies" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "no protection" (without naming the absent control) → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "unknown" (without a stated reason) → `[CLEAR]` if absent; `[FAIL: location]` if present

**GATE 3** is cleared when and only when all eight items carry explicit dispositions and no
`[FAIL]` item has an unwritten rewrite section. Role 4 is valid only when GATE 3 is cleared.

---

**ROLE 4 — EXECUTE PRE-COMMITTED AUDIT CONTRACT**

*(GATE 3 must be cleared before Role 4 executes. Execute the PRE-COMMITTED AUDIT CONTRACT
declared before all analytical roles above. The contract terms — structural fact, mandate
scope restriction, verification checks, and verdict format — are fixed as declared and cannot
be supplemented or modified at execution time.)*

---

## V-02 — Single-axis: Spatially Co-located Rewrite Mandate

**Axis:** Lifecycle emphasis — the correction gate gains an explicit validity predicate
prescribing the spatial location of rewrite output relative to each `[FAIL]` annotation.
GATE 1 and GATE 2 are unchanged (no C-31 changes). Only the correction gate changes.

**Hypothesis:** The R7 V-05 correction gate says "no `[FAIL]` item has an unwritten rewrite
section" — this requires the rewrite to exist but does not specify where. C-32 requires "the
rewrite instruction prescribes the output location... immediately below it." Adding a predicate
form — "a rewrite is valid only when the corrected content appears immediately below its
`[FAIL]` annotation" — restores the spatial constraint lost in the V-05 predicate rewrite
while maintaining C-22 (per-token attestation), C-27 (role-scoped suspension), and C-29
(cleared-when form).

---

## PRE-COMMITTED AUDIT CONTRACT — ROLE 4

*This contract is declared before any analytical role begins. It is fixed and cannot be
modified at execution time.*

**Structural fact (this section is a system-state declaration, not an instruction):** Role 4
has no output in TABLE A, TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, or TABLE G. It did not
produce any component limits, propagation hops, tier-matrix arithmetic, or mitigation entries.
It cannot rationalize its own prior choices because it made none.

**Role 4 mandate: flags and verdict only.** Role 4 produces no root-cause explanations, fix
proposals, diagnostic analysis, or supplementary output of any kind. Its entire output
consists of flag items and a PASS/FAIL verdict.

**Verification checks (fixed before analytical output is produced):**

1. Cross-table component check: every component named in TABLE C must appear in TABLE A.
Flag any TABLE C component absent from TABLE A as a phantom, citing the exact hop number and
component name.

2. Arithmetic citation check: every numeric limit used in TABLE F calculations must trace to
a named TABLE A row, cited as "T-NN: [value]". Flag any TABLE F arithmetic asserting a limit
not in TABLE A, citing the TABLE F row and the asserted value.

3. Verdict format: PASS if no flags raised. FAIL with specific hop-number and row-number
citations for every flag raised.

*End of PRE-COMMITTED AUDIT CONTRACT — ROLE 4.*

---

Throughput analysis that tests only uniform load makes the status quo look safer than it is.
A connector integration with no Retry-After handling, no concurrency cap on the flow trigger,
and an undocumented limit on the backend API tier will pass uniform-rate testing. It will fail
in production on the first batch event, the first concurrent submission storm, the first
scheduled job that arrives while the previous run is still holding connections.

The burst-shape bottleneck is not a more extreme version of the steady-state bottleneck. It
is a different failure mode. The binding constraint can be a different tier, the propagation
chain can start from a different component, and the user-visible failure can arrive through a
different signal. This analysis requires both.

Unknown limits are not acceptable omissions. A tier with an undocumented limit is an
inventory member with `?-unresolved` status — it appears in TABLE A, it appears in TABLE B,
it appears in TABLE E, and its uncertainty status is the primary determinant of analysis risk
level.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

This analysis produces four required tables (TABLE A, TABLE C, TABLE F, TABLE G) and three
supplementary tables (TABLE B, TABLE D, TABLE E). All seven must appear with their declared
column structure intact. All table production contracts and role output specifications are
expressed as validity predicates. All gate invariants are expressed as cleared-when predicates.
Role 4's specification is pre-committed above.

---

**PASS 1 — COMPONENT-LIMIT INVENTORY**

TABLE A is valid when: (1) every system component that handles requests, enforces rate limits,
or sits on the request path appears as a row; (2) every Limit cell contains [number + unit],
`[estimated: value + basis]`, or `?-unresolved` — blank Limit cells are not valid; (3) every
Status cell contains exactly one of `confirmed`, `estimated`, `?-unresolved` — inline prose
uncertainty descriptions are not valid Status values; (4) every `?-unresolved` row has a
Notes cell with a named reason from: `undocumented`, `environment-specific`,
`requires-runtime-measurement`, `signal-insufficient`; (5) no component known from the input
signal is absent.

| Tier-ID | Component | Limit | Status | Scope | First-hit? | Notes |
|---------|-----------|-------|--------|-------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE A is valid only when every condition above holds; a prose component inventory does not constitute a valid TABLE A regardless of its analytical quality)* | | | | | | |
| T-01 | | | | | | |
| T-02 | | | | | | |

**GATE 1** is cleared when and only when: TABLE A has at least two rows; every Limit cell
is non-blank; every Status cell is one of the three named tokens; every `?-unresolved` row
has a named reason in Notes; no component known from the signal is absent. TABLE B is valid
only when GATE 1 is cleared.

---

**PASS 2 — TEMPORAL FAILURE PROFILE**

TABLE B is valid when: (1) every TABLE A tier has exactly one row; (2) every
Failure-visibility-window cell is non-blank; (3) every Recovery-time cell is non-blank;
(4) every Confidence cell is one of `CONFIRMED`, `ESTIMATED`, `UNKNOWN`; (5) every `UNKNOWN`
row has a non-empty Notes cell. A TABLE B that omits any TABLE A tier or leaves a temporal
cell blank is not valid.

| Tier-ID | Failure-visibility-window | Recovery-time | Confidence | Notes |
|---------|--------------------------|---------------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE B is valid only when every TABLE A tier appears with non-blank temporal values; omitting any tier or leaving temporal cells blank produces a not-valid TABLE B)* | | | | |
| T-01 | | | | |
| T-02 | | | | |

**GATE 2** is cleared when and only when: every TABLE A tier has a TABLE B row with non-blank
Failure-visibility-window and Recovery-time cells; every `UNKNOWN` entry has a reason in Notes.
Downstream phases are valid only when GATE 2 is cleared.

---

**DOWNSTREAM PHASES**

**Phase 1a output is valid when** it names: the Tier-ID of the uniform-rate binding constraint
(citing its TABLE A Limit value), and the causal reason this tier binds before all others.

**Phase 1b output is valid when** it names: the Tier-ID of the burst-arrival binding constraint
(citing TABLE A Limit value), and includes at least one numeric effective-rate comparison
between uniform and burst delivery for the relevant tiers.

**Phase 1c output is valid only when** it contains exactly this structure:

> Binding tier at uniform arrival: ___
> Binding tier at burst arrival: ___
> Verdict: SAME TIER / DIFFERENT TIER
> Explanation: ___

The Phase 1c explanation is valid when: if DIFFERENT TIER, it names both Tier-IDs and cites
their specific TABLE A Limit values; if SAME TIER, it cites the binding tier's TABLE A Limit
value and explains why burst shape does not shift the constraint. A Phase 1c explanation
without TABLE A Limit citations is not valid.

---

TABLE C is valid when: (1) it traces from the Phase 1b burst-rate binding tier; (2) it contains
at least two rows; (3) every Mechanism cell contains exactly one of: `queue-fill`,
`connection-hold`, `retry-amplification`, `dependency-stall`; (4) no cell in TABLE C contains:
"also throttled", "cascade occurs", "propagates to", "downstream effect", "flow is affected",
"rate limiting applies"; (5) every Observable-effect cell names a distinct outcome. A TABLE C
where any Mechanism cell contains a generic token from the prohibited vocabulary is not valid.

| Hop | From-component | To-component | Mechanism | Observable-effect |
|-----|---------------|--------------|-----------|-------------------|
| *(ANTI-SUBSTITUTION: TABLE C is valid only when every Mechanism cell contains a named token from the four-item vocabulary; narrative paragraph substitution produces a not-valid TABLE C)* | | | | |
| 1 | | | | |
| 2 | | | | |

---

TABLE D is valid when: (1) at least one row is present; (2) every Gap-reason names a specific
structural absence; (3) every `?-unresolved` TABLE A tier on an unprotected path is flagged
in the Gap-tier column. A TABLE D row with a generic Gap-reason is not valid.

| Path-ID | Entry-component | Gap-reason | Gap-tier? | Consequence-at-burst-volume |
|---------|----------------|------------|-----------|-----------------------------|
| *(ANTI-SUBSTITUTION: TABLE D is valid only when each Gap-reason names the specific absent control; "no protection" or similar generic entries do not produce a valid TABLE D row)* | | | | |
| P-01 | | | | |

---

TABLE E is valid when: (1) every TABLE A tier has exactly one row, including `?-unresolved`
tiers; (2) every Retry-After cell is `Y`, `N`, or `UNKNOWN`; (3) every Failure-if-ignored
cell is one of: `immediate-retry-storm`, `exponential-backoff-absent`, `silent-infinite-loop`,
`flow-run-failure`; (4) `?-unresolved` tier rows have Confirmed = `ESTIMATED`. A TABLE E that
omits any TABLE A tier or uses free-form failure descriptions is not valid.

| Tier-ID | Error-signal | Retry-After? | Visible-in-history? | Failure-if-ignored | Confirmed? |
|---------|-------------|--------------|---------------------|-------------------|------------|
| *(ANTI-SUBSTITUTION: TABLE E is valid only when all TABLE A tiers appear including gap tiers; free-form failure-mode descriptions are not valid Failure-if-ignored values)* | | | | | |
| T-01 | | | | | |

---

TABLE F is valid when: (1) it contains exactly four rows with Volume values `1×`, `3×`, `5×`,
`10×`; (2) every Binding-tier cell names a TABLE A Tier-ID; (3) every Threshold-hit cell
cites the TABLE A Limit as "T-NN: [value]"; (4) every Error-rate% cell contains arithmetic
steps that name each limit used — an asserted percentage without arithmetic steps is not a
valid Error-rate% cell; (5) all Threshold-hit citations trace to named TABLE A rows. A TABLE F
without exactly four fixed-multiplier rows or without arithmetic-derived Error-rate% values
is not valid.

| Volume | Binding-tier | Threshold-hit | Behavior | Error-rate% |
|--------|-------------|---------------|----------|-------------|
| *(ANTI-SUBSTITUTION: TABLE F is valid only when it has exactly four fixed-multiplier rows with step-by-step arithmetic in Error-rate%; a free-form tier summary does not constitute a valid TABLE F)* | | | | |
| 1× | | | | |
| 3× | | | | |
| 5× | | | | |
| 10× | | | | |

---

**CASCADE SCENARIO.** The cascade scenario is valid when: it names at least three tiers in a
causal chain where throttling at tier N triggers throttling at tier N+1; each link states a
specific mechanism from the TABLE C vocabulary; no step uses the generic prohibited token
vocabulary. A cascade scenario using generic tokens is not valid.

**RETRY-AFTER GAP ASSESSMENT.** This section is valid when it names either the specific
Retry-After header and confirms correct caller handling, or names the TABLE E Failure-if-ignored
token that results from absent handling.

---

TABLE G is valid when: (1) at least two gaps are covered; (2) every Remediation names a
specific Power Automate setting, connector configuration parameter, API field, or implementation
pattern — entries without a named specific control are not valid Remediation cells; (3) every
Specific-config cell is non-blank. A TABLE G with generic prescription entries is not valid.

| Gap-ID | Type | Remediation | Specific-config-or-API |
|--------|------|-------------|------------------------|
| *(ANTI-SUBSTITUTION: TABLE G is valid only when each Remediation names a specific actionable control; generic recommendations produce a not-valid TABLE G row)* | | | |
| G-01 | | | |
| G-02 | | | |

---

**CORRECTION GATE**

Role 2 output is valid when every item below has an explicit disposition. Role 2 produces no
further output while any item is unresolved.

**GATE 3** is cleared when and only when every item below carries either `[CLEAR]` or a
`[FAIL: location]` annotation — GATE 3 is not cleared while any `- [ ]` item remains without
a disposition, and Role 4 execution is not valid unless GATE 3 is cleared:

- [ ] "also throttled" → `[CLEAR]` if absent; `[FAIL: TABLE C hop N — rewritten below]` if present
- [ ] "cascade occurs" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "propagates to" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "downstream effect" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "flow is affected" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "rate limiting applies" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "no protection" (without naming the absent control) → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "unknown" (without a stated reason) → `[CLEAR]` if absent; `[FAIL: location]` if present

A rewrite is valid only when the corrected content appears immediately below its `[FAIL]`
annotation in the output stream — a rewrite is not valid when it appears in a separate
correction section, a later phase, or at end of output. Spatial co-location makes each
annotation and its corrected content auditable as a contiguous block by linear scan.

**GATE 3** is cleared when and only when all eight items carry explicit dispositions, every
`[FAIL]` annotation has its corrected content immediately below it, and no `- [ ]` item
may remain undisposed. Role 4 is valid only when GATE 3 is cleared.

---

**ROLE 4 — EXECUTE PRE-COMMITTED AUDIT CONTRACT**

*(GATE 3 must be cleared before Role 4 executes. Execute the PRE-COMMITTED AUDIT CONTRACT
declared before all analytical roles above. The contract terms — structural fact, mandate
scope restriction, verification checks, and verdict format — are fixed as declared and cannot
be supplemented or modified at execution time.)*

---

## V-03 — Single-axis: Dual-block Failure-State Declaration on All Gates

**Axis:** Phrasing register — instead of appending the negative invariant inline to the
positive cleared-when predicate (dash-separator form), each gate receives a separate, visually
distinct "**GATE N is not cleared when:**" block listing failure conditions as an independent
statement. Both the cleared state and the not-cleared state are declared as independent
predicate blocks rather than as a single compound statement.

**Hypothesis:** When the positive cleared-when predicate is already a long conditions list
(five conditions for GATE 1, three for GATE 2), appending the negative invariant inline may
cause it to read as a redundant note rather than an independent failure-state declaration.
Separating them into distinct labeled blocks — "GATE N is cleared when..." and "GATE N is
not cleared when..." — makes both states independently scannable by an evaluator without
inference. The test is whether the dual-block form produces more durable C-31 compliance under
token pressure on the structural gates where inline appending is least natural.

---

## PRE-COMMITTED AUDIT CONTRACT — ROLE 4

*This contract is declared before any analytical role begins. It is fixed and cannot be
modified at execution time.*

**Structural fact (this section is a system-state declaration, not an instruction):** Role 4
has no output in TABLE A, TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, or TABLE G. It did not
produce any component limits, propagation hops, tier-matrix arithmetic, or mitigation entries.
It cannot rationalize its own prior choices because it made none.

**Role 4 mandate: flags and verdict only.** Role 4 produces no root-cause explanations, fix
proposals, diagnostic analysis, or supplementary output of any kind. Its entire output
consists of flag items and a PASS/FAIL verdict.

**Verification checks (fixed before analytical output is produced):**

1. Cross-table component check: every component named in TABLE C must appear in TABLE A.
Flag any TABLE C component absent from TABLE A as a phantom, citing the exact hop number and
component name.

2. Arithmetic citation check: every numeric limit used in TABLE F calculations must trace to
a named TABLE A row, cited as "T-NN: [value]". Flag any TABLE F arithmetic asserting a limit
not in TABLE A, citing the TABLE F row and the asserted value.

3. Verdict format: PASS if no flags raised. FAIL with specific hop-number and row-number
citations for every flag raised.

*End of PRE-COMMITTED AUDIT CONTRACT — ROLE 4.*

---

Throughput analysis that tests only uniform load makes the status quo look safer than it is.
A connector integration with no Retry-After handling, no concurrency cap on the flow trigger,
and an undocumented limit on the backend API tier will pass uniform-rate testing. It will fail
in production on the first batch event, the first concurrent submission storm, the first
scheduled job that arrives while the previous run is still holding connections.

The burst-shape bottleneck is not a more extreme version of the steady-state bottleneck. It
is a different failure mode. The binding constraint can be a different tier, the propagation
chain can start from a different component, and the user-visible failure can arrive through a
different signal. This analysis requires both.

Unknown limits are not acceptable omissions. A tier with an undocumented limit is an
inventory member with `?-unresolved` status — it appears in TABLE A, it appears in TABLE B,
it appears in TABLE E, and its uncertainty status is the primary determinant of analysis risk
level.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

This analysis produces four required tables (TABLE A, TABLE C, TABLE F, TABLE G) and three
supplementary tables (TABLE B, TABLE D, TABLE E). All seven must appear with their declared
column structure intact. All table production contracts and role output specifications are
expressed as validity predicates. All gate invariants declare both the cleared state and the
not-cleared state as independent predicate blocks. Role 4's specification is pre-committed
above.

---

**PASS 1 — COMPONENT-LIMIT INVENTORY**

TABLE A is valid when: (1) every system component that handles requests, enforces rate limits,
or sits on the request path appears as a row; (2) every Limit cell contains [number + unit],
`[estimated: value + basis]`, or `?-unresolved` — blank Limit cells are not valid; (3) every
Status cell contains exactly one of `confirmed`, `estimated`, `?-unresolved` — inline prose
uncertainty descriptions are not valid Status values; (4) every `?-unresolved` row has a
Notes cell with a named reason from: `undocumented`, `environment-specific`,
`requires-runtime-measurement`, `signal-insufficient`; (5) no component known from the input
signal is absent.

| Tier-ID | Component | Limit | Status | Scope | First-hit? | Notes |
|---------|-----------|-------|--------|-------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE A is valid only when every condition above holds; a prose component inventory does not constitute a valid TABLE A regardless of its analytical quality)* | | | | | | |
| T-01 | | | | | | |
| T-02 | | | | | | |

**GATE 1** is cleared when and only when: TABLE A has at least two rows; every Limit cell
is non-blank; every Status cell is one of the three named tokens; every `?-unresolved` row
has a named reason in Notes; no component known from the signal is absent.

**GATE 1 is not cleared when** any of the following failure states are present: any system
component from the input signal is absent from TABLE A; any Limit cell is blank; any Status
cell contains prose uncertainty rather than a named token; any `?-unresolved` row has an
empty Notes cell. TABLE B is valid only when GATE 1 is cleared and no GATE 1 failure state
is present.

---

**PASS 2 — TEMPORAL FAILURE PROFILE**

TABLE B is valid when: (1) every TABLE A tier has exactly one row; (2) every
Failure-visibility-window cell is non-blank; (3) every Recovery-time cell is non-blank;
(4) every Confidence cell is one of `CONFIRMED`, `ESTIMATED`, `UNKNOWN`; (5) every `UNKNOWN`
row has a non-empty Notes cell. A TABLE B that omits any TABLE A tier or leaves a temporal
cell blank is not valid.

| Tier-ID | Failure-visibility-window | Recovery-time | Confidence | Notes |
|---------|--------------------------|---------------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE B is valid only when every TABLE A tier appears with non-blank temporal values; omitting any tier or leaving temporal cells blank produces a not-valid TABLE B)* | | | | |
| T-01 | | | | |
| T-02 | | | | |

**GATE 2** is cleared when and only when: every TABLE A tier has a TABLE B row; every
Failure-visibility-window cell is non-blank; every Recovery-time cell is non-blank; every
`UNKNOWN` entry has a reason in Notes.

**GATE 2 is not cleared when** any of the following failure states are present: any TABLE A
tier is absent from TABLE B; any Failure-visibility-window cell is blank; any Recovery-time
cell is blank; any `UNKNOWN` entry lacks a Notes reason. Downstream phases are valid only when
GATE 2 is cleared and no GATE 2 failure state is present.

---

**DOWNSTREAM PHASES**

**Phase 1a output is valid when** it names: the Tier-ID of the uniform-rate binding constraint
(citing its TABLE A Limit value), and the causal reason this tier binds before all others.

**Phase 1b output is valid when** it names: the Tier-ID of the burst-arrival binding constraint
(citing TABLE A Limit value), and includes at least one numeric effective-rate comparison
between uniform and burst delivery for the relevant tiers.

**Phase 1c output is valid only when** it contains exactly this structure:

> Binding tier at uniform arrival: ___
> Binding tier at burst arrival: ___
> Verdict: SAME TIER / DIFFERENT TIER
> Explanation: ___

The Phase 1c explanation is valid when: if DIFFERENT TIER, it names both Tier-IDs and cites
their specific TABLE A Limit values; if SAME TIER, it cites the binding tier's TABLE A Limit
value and explains why burst shape does not shift the constraint. A Phase 1c explanation
without TABLE A Limit citations is not valid.

---

TABLE C is valid when: (1) it traces from the Phase 1b burst-rate binding tier; (2) it contains
at least two rows; (3) every Mechanism cell contains exactly one of: `queue-fill`,
`connection-hold`, `retry-amplification`, `dependency-stall`; (4) no cell in TABLE C contains:
"also throttled", "cascade occurs", "propagates to", "downstream effect", "flow is affected",
"rate limiting applies"; (5) every Observable-effect cell names a distinct outcome. A TABLE C
where any Mechanism cell contains a generic token from the prohibited vocabulary is not valid.

| Hop | From-component | To-component | Mechanism | Observable-effect |
|-----|---------------|--------------|-----------|-------------------|
| *(ANTI-SUBSTITUTION: TABLE C is valid only when every Mechanism cell contains a named token from the four-item vocabulary; narrative paragraph substitution produces a not-valid TABLE C)* | | | | |
| 1 | | | | |
| 2 | | | | |

---

TABLE D is valid when: (1) at least one row is present; (2) every Gap-reason names a specific
structural absence; (3) every `?-unresolved` TABLE A tier on an unprotected path is flagged
in the Gap-tier column. A TABLE D row with a generic Gap-reason is not valid.

| Path-ID | Entry-component | Gap-reason | Gap-tier? | Consequence-at-burst-volume |
|---------|----------------|------------|-----------|-----------------------------|
| *(ANTI-SUBSTITUTION: TABLE D is valid only when each Gap-reason names the specific absent control; "no protection" or similar generic entries do not produce a valid TABLE D row)* | | | | |
| P-01 | | | | |

---

TABLE E is valid when: (1) every TABLE A tier has exactly one row, including `?-unresolved`
tiers; (2) every Retry-After cell is `Y`, `N`, or `UNKNOWN`; (3) every Failure-if-ignored
cell is one of: `immediate-retry-storm`, `exponential-backoff-absent`, `silent-infinite-loop`,
`flow-run-failure`; (4) `?-unresolved` tier rows have Confirmed = `ESTIMATED`. A TABLE E that
omits any TABLE A tier or uses free-form failure descriptions is not valid.

| Tier-ID | Error-signal | Retry-After? | Visible-in-history? | Failure-if-ignored | Confirmed? |
|---------|-------------|--------------|---------------------|-------------------|------------|
| *(ANTI-SUBSTITUTION: TABLE E is valid only when all TABLE A tiers appear including gap tiers; free-form failure-mode descriptions are not valid Failure-if-ignored values)* | | | | | |
| T-01 | | | | | |

---

TABLE F is valid when: (1) it contains exactly four rows with Volume values `1×`, `3×`, `5×`,
`10×`; (2) every Binding-tier cell names a TABLE A Tier-ID; (3) every Threshold-hit cell
cites the TABLE A Limit as "T-NN: [value]"; (4) every Error-rate% cell contains arithmetic
steps that name each limit used — an asserted percentage without arithmetic steps is not a
valid Error-rate% cell; (5) all Threshold-hit citations trace to named TABLE A rows. A TABLE F
without exactly four fixed-multiplier rows or without arithmetic-derived Error-rate% values
is not valid.

| Volume | Binding-tier | Threshold-hit | Behavior | Error-rate% |
|--------|-------------|---------------|----------|-------------|
| *(ANTI-SUBSTITUTION: TABLE F is valid only when it has exactly four fixed-multiplier rows with step-by-step arithmetic in Error-rate%; a free-form tier summary does not constitute a valid TABLE F)* | | | | |
| 1× | | | | |
| 3× | | | | |
| 5× | | | | |
| 10× | | | | |

---

**CASCADE SCENARIO.** The cascade scenario is valid when: it names at least three tiers in a
causal chain where throttling at tier N triggers throttling at tier N+1; each link states a
specific mechanism from the TABLE C vocabulary; no step uses the generic prohibited token
vocabulary. A cascade scenario using generic tokens is not valid.

**RETRY-AFTER GAP ASSESSMENT.** This section is valid when it names either the specific
Retry-After header and confirms correct caller handling, or names the TABLE E Failure-if-ignored
token that results from absent handling.

---

TABLE G is valid when: (1) at least two gaps are covered; (2) every Remediation names a
specific Power Automate setting, connector configuration parameter, API field, or implementation
pattern — entries without a named specific control are not valid Remediation cells; (3) every
Specific-config cell is non-blank. A TABLE G with generic prescription entries is not valid.

| Gap-ID | Type | Remediation | Specific-config-or-API |
|--------|------|-------------|------------------------|
| *(ANTI-SUBSTITUTION: TABLE G is valid only when each Remediation names a specific actionable control; generic recommendations produce a not-valid TABLE G row)* | | | |
| G-01 | | | |
| G-02 | | | |

---

**CORRECTION GATE**

Role 2 output is valid when every item below has an explicit disposition. Role 2 produces no
further output while any item is unresolved.

**GATE 3** is cleared when and only when every item below carries either `[CLEAR]` or a
`[FAIL: location]` annotation — GATE 3 is not cleared while any `- [ ]` item remains without
a disposition, and Role 4 execution is not valid unless GATE 3 is cleared:

- [ ] "also throttled" → `[CLEAR]` if absent; `[FAIL: TABLE C hop N — rewritten below]` if present
- [ ] "cascade occurs" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "propagates to" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "downstream effect" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "flow is affected" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "rate limiting applies" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "no protection" (without naming the absent control) → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "unknown" (without a stated reason) → `[CLEAR]` if absent; `[FAIL: location]` if present

**GATE 3 is not cleared when** any `- [ ]` item remains without a disposition. Role 4 produces
no output while GATE 3 is not cleared.

**GATE 3** is cleared when and only when all eight items carry explicit dispositions and no
`[FAIL]` item has an unwritten rewrite section. Role 4 is valid only when GATE 3 is cleared.

---

**ROLE 4 — EXECUTE PRE-COMMITTED AUDIT CONTRACT**

*(GATE 3 must be cleared before Role 4 executes. Execute the PRE-COMMITTED AUDIT CONTRACT
declared before all analytical roles above. The contract terms — structural fact, mandate
scope restriction, verification checks, and verdict format — are fixed as declared and cannot
be supplemented or modified at execution time.)*

---

## V-04 — Combined: Inline Negative Invariant (C-31) + Spatial Rewrite Prescription (C-32)

**Axis:** Combined lifecycle emphasis — GATE 1 and GATE 2 gain the inline negative invariant
(dash-separator form from V-01), and the correction gate gains the explicit spatial rewrite
prescription (predicate form from V-02). Both new criteria addressed simultaneously on the
R7 V-05 base.

**Hypothesis:** C-31 and C-32 operate on different gates and different sections of the
correction mechanism, so they should not compete for instruction surface. V-01 addresses
structural gates GATE 1/GATE 2; V-02 addresses the correction gate's rewrite instruction.
The combined form tests whether adding both simultaneously on top of C-28+C-29+C-30 degrades
any earlier criterion through token pressure, or whether the changes are additive without
interference.

---

## PRE-COMMITTED AUDIT CONTRACT — ROLE 4

*This contract is declared before any analytical role begins. It is fixed and cannot be
modified at execution time.*

**Structural fact (this section is a system-state declaration, not an instruction):** Role 4
has no output in TABLE A, TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, or TABLE G. It did not
produce any component limits, propagation hops, tier-matrix arithmetic, or mitigation entries.
It cannot rationalize its own prior choices because it made none.

**Role 4 mandate: flags and verdict only.** Role 4 produces no root-cause explanations, fix
proposals, diagnostic analysis, or supplementary output of any kind. Its entire output
consists of flag items and a PASS/FAIL verdict.

**Verification checks (fixed before analytical output is produced):**

1. Cross-table component check: every component named in TABLE C must appear in TABLE A.
Flag any TABLE C component absent from TABLE A as a phantom, citing the exact hop number and
component name.

2. Arithmetic citation check: every numeric limit used in TABLE F calculations must trace to
a named TABLE A row, cited as "T-NN: [value]". Flag any TABLE F arithmetic asserting a limit
not in TABLE A, citing the TABLE F row and the asserted value.

3. Verdict format: PASS if no flags raised. FAIL with specific hop-number and row-number
citations for every flag raised.

*End of PRE-COMMITTED AUDIT CONTRACT — ROLE 4.*

---

Throughput analysis that tests only uniform load makes the status quo look safer than it is.
A connector integration with no Retry-After handling, no concurrency cap on the flow trigger,
and an undocumented limit on the backend API tier will pass uniform-rate testing. It will fail
in production on the first batch event, the first concurrent submission storm, the first
scheduled job that arrives while the previous run is still holding connections.

The burst-shape bottleneck is not a more extreme version of the steady-state bottleneck. It
is a different failure mode. The binding constraint can be a different tier, the propagation
chain can start from a different component, and the user-visible failure can arrive through a
different signal. This analysis requires both.

Unknown limits are not acceptable omissions. A tier with an undocumented limit is an
inventory member with `?-unresolved` status — it appears in TABLE A, it appears in TABLE B,
it appears in TABLE E, and its uncertainty status is the primary determinant of analysis risk
level.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

This analysis produces four required tables (TABLE A, TABLE C, TABLE F, TABLE G) and three
supplementary tables (TABLE B, TABLE D, TABLE E). All seven must appear with their declared
column structure intact. All table production contracts and role output specifications are
expressed as validity predicates. All gate invariants are expressed as cleared-when predicates
with explicit negative invariants. Role 4's specification is pre-committed above.

---

**PASS 1 — COMPONENT-LIMIT INVENTORY**

TABLE A is valid when: (1) every system component that handles requests, enforces rate limits,
or sits on the request path appears as a row; (2) every Limit cell contains [number + unit],
`[estimated: value + basis]`, or `?-unresolved` — blank Limit cells are not valid; (3) every
Status cell contains exactly one of `confirmed`, `estimated`, `?-unresolved` — inline prose
uncertainty descriptions are not valid Status values; (4) every `?-unresolved` row has a
Notes cell with a named reason from: `undocumented`, `environment-specific`,
`requires-runtime-measurement`, `signal-insufficient`; (5) no component known from the input
signal is absent.

| Tier-ID | Component | Limit | Status | Scope | First-hit? | Notes |
|---------|-----------|-------|--------|-------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE A is valid only when every condition above holds; a prose component inventory does not constitute a valid TABLE A regardless of its analytical quality)* | | | | | | |
| T-01 | | | | | | |
| T-02 | | | | | | |

**GATE 1** is cleared when and only when: TABLE A has at least two rows; every Limit cell
is non-blank; every Status cell is one of the three named tokens; every `?-unresolved` row
has a named reason in Notes; no component known from the signal is absent — no TABLE A row
may be absent, no Limit cell may be blank, no Status cell may contain prose, no
`?-unresolved` row may have an empty Notes cell. TABLE B is valid only when GATE 1 is cleared.

---

**PASS 2 — TEMPORAL FAILURE PROFILE**

TABLE B is valid when: (1) every TABLE A tier has exactly one row; (2) every
Failure-visibility-window cell is non-blank; (3) every Recovery-time cell is non-blank;
(4) every Confidence cell is one of `CONFIRMED`, `ESTIMATED`, `UNKNOWN`; (5) every `UNKNOWN`
row has a non-empty Notes cell. A TABLE B that omits any TABLE A tier or leaves a temporal
cell blank is not valid.

| Tier-ID | Failure-visibility-window | Recovery-time | Confidence | Notes |
|---------|--------------------------|---------------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE B is valid only when every TABLE A tier appears with non-blank temporal values; omitting any tier or leaving temporal cells blank produces a not-valid TABLE B)* | | | | |
| T-01 | | | | |
| T-02 | | | | |

**GATE 2** is cleared when and only when: every TABLE A tier has a TABLE B row with non-blank
Failure-visibility-window and Recovery-time cells; every `UNKNOWN` entry has a reason in Notes
— no TABLE A tier may be absent from TABLE B, no Failure-visibility-window cell may be blank,
no Recovery-time cell may be blank, no `UNKNOWN` entry may lack a Notes reason. Downstream
phases are valid only when GATE 2 is cleared.

---

**DOWNSTREAM PHASES**

**Phase 1a output is valid when** it names: the Tier-ID of the uniform-rate binding constraint
(citing its TABLE A Limit value), and the causal reason this tier binds before all others.

**Phase 1b output is valid when** it names: the Tier-ID of the burst-arrival binding constraint
(citing TABLE A Limit value), and includes at least one numeric effective-rate comparison
between uniform and burst delivery for the relevant tiers.

**Phase 1c output is valid only when** it contains exactly this structure:

> Binding tier at uniform arrival: ___
> Binding tier at burst arrival: ___
> Verdict: SAME TIER / DIFFERENT TIER
> Explanation: ___

The Phase 1c explanation is valid when: if DIFFERENT TIER, it names both Tier-IDs and cites
their specific TABLE A Limit values; if SAME TIER, it cites the binding tier's TABLE A Limit
value and explains why burst shape does not shift the constraint. A Phase 1c explanation
without TABLE A Limit citations is not valid.

---

TABLE C is valid when: (1) it traces from the Phase 1b burst-rate binding tier; (2) it contains
at least two rows; (3) every Mechanism cell contains exactly one of: `queue-fill`,
`connection-hold`, `retry-amplification`, `dependency-stall`; (4) no cell in TABLE C contains:
"also throttled", "cascade occurs", "propagates to", "downstream effect", "flow is affected",
"rate limiting applies"; (5) every Observable-effect cell names a distinct outcome. A TABLE C
where any Mechanism cell contains a generic token from the prohibited vocabulary is not valid.

| Hop | From-component | To-component | Mechanism | Observable-effect |
|-----|---------------|--------------|-----------|-------------------|
| *(ANTI-SUBSTITUTION: TABLE C is valid only when every Mechanism cell contains a named token from the four-item vocabulary; narrative paragraph substitution produces a not-valid TABLE C)* | | | | |
| 1 | | | | |
| 2 | | | | |

---

TABLE D is valid when: (1) at least one row is present; (2) every Gap-reason names a specific
structural absence; (3) every `?-unresolved` TABLE A tier on an unprotected path is flagged
in the Gap-tier column. A TABLE D row with a generic Gap-reason is not valid.

| Path-ID | Entry-component | Gap-reason | Gap-tier? | Consequence-at-burst-volume |
|---------|----------------|------------|-----------|-----------------------------|
| *(ANTI-SUBSTITUTION: TABLE D is valid only when each Gap-reason names the specific absent control; "no protection" or similar generic entries do not produce a valid TABLE D row)* | | | | |
| P-01 | | | | |

---

TABLE E is valid when: (1) every TABLE A tier has exactly one row, including `?-unresolved`
tiers; (2) every Retry-After cell is `Y`, `N`, or `UNKNOWN`; (3) every Failure-if-ignored
cell is one of: `immediate-retry-storm`, `exponential-backoff-absent`, `silent-infinite-loop`,
`flow-run-failure`; (4) `?-unresolved` tier rows have Confirmed = `ESTIMATED`. A TABLE E that
omits any TABLE A tier or uses free-form failure descriptions is not valid.

| Tier-ID | Error-signal | Retry-After? | Visible-in-history? | Failure-if-ignored | Confirmed? |
|---------|-------------|--------------|---------------------|-------------------|------------|
| *(ANTI-SUBSTITUTION: TABLE E is valid only when all TABLE A tiers appear including gap tiers; free-form failure-mode descriptions are not valid Failure-if-ignored values)* | | | | | |
| T-01 | | | | | |

---

TABLE F is valid when: (1) it contains exactly four rows with Volume values `1×`, `3×`, `5×`,
`10×`; (2) every Binding-tier cell names a TABLE A Tier-ID; (3) every Threshold-hit cell
cites the TABLE A Limit as "T-NN: [value]"; (4) every Error-rate% cell contains arithmetic
steps that name each limit used — an asserted percentage without arithmetic steps is not a
valid Error-rate% cell; (5) all Threshold-hit citations trace to named TABLE A rows. A TABLE F
without exactly four fixed-multiplier rows or without arithmetic-derived Error-rate% values
is not valid.

| Volume | Binding-tier | Threshold-hit | Behavior | Error-rate% |
|--------|-------------|---------------|----------|-------------|
| *(ANTI-SUBSTITUTION: TABLE F is valid only when it has exactly four fixed-multiplier rows with step-by-step arithmetic in Error-rate%; a free-form tier summary does not constitute a valid TABLE F)* | | | | |
| 1× | | | | |
| 3× | | | | |
| 5× | | | | |
| 10× | | | | |

---

**CASCADE SCENARIO.** The cascade scenario is valid when: it names at least three tiers in a
causal chain where throttling at tier N triggers throttling at tier N+1; each link states a
specific mechanism from the TABLE C vocabulary; no step uses the generic prohibited token
vocabulary. A cascade scenario using generic tokens is not valid.

**RETRY-AFTER GAP ASSESSMENT.** This section is valid when it names either the specific
Retry-After header and confirms correct caller handling, or names the TABLE E Failure-if-ignored
token that results from absent handling.

---

TABLE G is valid when: (1) at least two gaps are covered; (2) every Remediation names a
specific Power Automate setting, connector configuration parameter, API field, or implementation
pattern — entries without a named specific control are not valid Remediation cells; (3) every
Specific-config cell is non-blank. A TABLE G with generic prescription entries is not valid.

| Gap-ID | Type | Remediation | Specific-config-or-API |
|--------|------|-------------|------------------------|
| *(ANTI-SUBSTITUTION: TABLE G is valid only when each Remediation names a specific actionable control; generic recommendations produce a not-valid TABLE G row)* | | | |
| G-01 | | | |
| G-02 | | | |

---

**CORRECTION GATE**

Role 2 output is valid when every item below has an explicit disposition. Role 2 produces no
further output while any item is unresolved.

**GATE 3** is cleared when and only when every item below carries either `[CLEAR]` or a
`[FAIL: location]` annotation — GATE 3 is not cleared while any `- [ ]` item remains without
a disposition, and Role 4 execution is not valid unless GATE 3 is cleared:

- [ ] "also throttled" → `[CLEAR]` if absent; `[FAIL: TABLE C hop N — rewritten below]` if present
- [ ] "cascade occurs" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "propagates to" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "downstream effect" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "flow is affected" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "rate limiting applies" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "no protection" (without naming the absent control) → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "unknown" (without a stated reason) → `[CLEAR]` if absent; `[FAIL: location]` if present

A rewrite is valid only when the corrected content appears immediately below its `[FAIL]`
annotation in the output stream — a rewrite is not valid when it appears in a separate
correction section, a later phase, or at end of output. Spatial co-location makes each
annotation and its corrected content auditable as a contiguous block by linear scan.

**GATE 3** is cleared when and only when all eight items carry explicit dispositions, every
`[FAIL]` annotation has its corrected content immediately below it, and no `- [ ]` item
may remain undisposed. Role 4 is valid only when GATE 3 is cleared.

---

**ROLE 4 — EXECUTE PRE-COMMITTED AUDIT CONTRACT**

*(GATE 3 must be cleared before Role 4 executes. Execute the PRE-COMMITTED AUDIT CONTRACT
declared before all analytical roles above. The contract terms — structural fact, mandate
scope restriction, verification checks, and verdict format — are fixed as declared and cannot
be supplemented or modified at execution time.)*

---

## V-05 — Combined: Dual-block C-31 + Spatial C-32 on Full Predicate Base (Maximum Coverage)

**Axis:** Combined phrasing register (dual-block failure-state from V-03) × lifecycle emphasis
(spatial rewrite prescription from V-02) on the R7 V-05 base (C-28+C-29+C-30). Uses the more
verbose, independently-scannable dual-block form for C-31 rather than inline dash-appended
negation (V-04 form). Tests whether the extra verbosity of dual-block declarations on all three
gates costs token budget on the pre-committed audit contract or earlier criteria.

**Hypothesis:** The dual-block form ("GATE N is cleared when... / GATE N is not cleared when...")
makes each gate's full state space explicitly declared in two independent scannable statements.
When combined with the spatial rewrite prescription (C-32) and the full C-28+C-29+C-30 base,
this variation should reach the highest achievable composite for rubric v22. The dual-block
form's additional verbosity may be worth the cost if it prevents the failure-state declaration
from being treated as a parenthetical appendage under token pressure.

---

## PRE-COMMITTED AUDIT CONTRACT — ROLE 4

*This contract is declared before any analytical role begins. It is fixed and cannot be
modified at execution time.*

**Structural fact (this section is a system-state declaration, not an instruction):** Role 4
has no output in TABLE A, TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, or TABLE G. It did not
produce any component limits, propagation hops, tier-matrix arithmetic, or mitigation entries.
It cannot rationalize its own prior choices because it made none.

**Role 4 mandate: flags and verdict only.** Role 4 produces no root-cause explanations, fix
proposals, diagnostic analysis, or supplementary output of any kind. Its entire output
consists of flag items and a PASS/FAIL verdict.

**Verification checks (fixed before analytical output is produced):**

1. Cross-table component check: every component named in TABLE C must appear in TABLE A.
Flag any TABLE C component absent from TABLE A as a phantom, citing the exact hop number and
component name.

2. Arithmetic citation check: every numeric limit used in TABLE F calculations must trace to
a named TABLE A row, cited as "T-NN: [value]". Flag any TABLE F arithmetic asserting a limit
not in TABLE A, citing the TABLE F row and the asserted value.

3. Verdict format: PASS if no flags raised. FAIL with specific hop-number and row-number
citations for every flag raised.

*End of PRE-COMMITTED AUDIT CONTRACT — ROLE 4.*

---

Throughput analysis that tests only uniform load makes the status quo look safer than it is.
A connector integration with no Retry-After handling, no concurrency cap on the flow trigger,
and an undocumented limit on the backend API tier will pass uniform-rate testing. It will fail
in production on the first batch event, the first concurrent submission storm, the first
scheduled job that arrives while the previous run is still holding connections.

The burst-shape bottleneck is not a more extreme version of the steady-state bottleneck. It
is a different failure mode. The binding constraint can be a different tier, the propagation
chain can start from a different component, and the user-visible failure can arrive through a
different signal. This analysis requires both.

Unknown limits are not acceptable omissions. A tier with an undocumented limit is an
inventory member with `?-unresolved` status — it appears in TABLE A, it appears in TABLE B,
it appears in TABLE E, and its uncertainty status is the primary determinant of analysis risk
level.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

This analysis produces four required tables (TABLE A, TABLE C, TABLE F, TABLE G) and three
supplementary tables (TABLE B, TABLE D, TABLE E). All seven must appear with their declared
column structure intact. All table production contracts and role output specifications are
expressed as validity predicates. All gate invariants declare both the cleared state and the
not-cleared state as independent predicate blocks. Rewrite output is co-located with its
triggering annotation. Role 4's specification is pre-committed above.

---

**PASS 1 — COMPONENT-LIMIT INVENTORY**

TABLE A is valid when: (1) every system component that handles requests, enforces rate limits,
or sits on the request path appears as a row; (2) every Limit cell contains [number + unit],
`[estimated: value + basis]`, or `?-unresolved` — blank Limit cells are not valid; (3) every
Status cell contains exactly one of `confirmed`, `estimated`, `?-unresolved` — inline prose
uncertainty descriptions are not valid Status values; (4) every `?-unresolved` row has a
Notes cell with a named reason from: `undocumented`, `environment-specific`,
`requires-runtime-measurement`, `signal-insufficient`; (5) no component known from the input
signal is absent.

| Tier-ID | Component | Limit | Status | Scope | First-hit? | Notes |
|---------|-----------|-------|--------|-------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE A is valid only when every condition above holds; a prose component inventory does not constitute a valid TABLE A regardless of its analytical quality)* | | | | | | |
| T-01 | | | | | | |
| T-02 | | | | | | |

**GATE 1** is cleared when and only when: TABLE A has at least two rows; every Limit cell
is non-blank; every Status cell is one of the three named tokens; every `?-unresolved` row
has a named reason in Notes; no component known from the signal is absent.

**GATE 1 is not cleared when** any of the following failure states are present: any system
component from the input signal is absent from TABLE A; any Limit cell is blank; any Status
cell contains prose uncertainty rather than a named token; any `?-unresolved` row has an
empty Notes cell. TABLE B is valid only when GATE 1 is cleared and no GATE 1 failure state
is present.

---

**PASS 2 — TEMPORAL FAILURE PROFILE**

TABLE B is valid when: (1) every TABLE A tier has exactly one row; (2) every
Failure-visibility-window cell is non-blank; (3) every Recovery-time cell is non-blank;
(4) every Confidence cell is one of `CONFIRMED`, `ESTIMATED`, `UNKNOWN`; (5) every `UNKNOWN`
row has a non-empty Notes cell. A TABLE B that omits any TABLE A tier or leaves a temporal
cell blank is not valid.

| Tier-ID | Failure-visibility-window | Recovery-time | Confidence | Notes |
|---------|--------------------------|---------------|------------|-------|
| *(ANTI-SUBSTITUTION: TABLE B is valid only when every TABLE A tier appears with non-blank temporal values; omitting any tier or leaving temporal cells blank produces a not-valid TABLE B)* | | | | |
| T-01 | | | | |
| T-02 | | | | |

**GATE 2** is cleared when and only when: every TABLE A tier has a TABLE B row; every
Failure-visibility-window cell is non-blank; every Recovery-time cell is non-blank; every
`UNKNOWN` entry has a reason in Notes.

**GATE 2 is not cleared when** any of the following failure states are present: any TABLE A
tier is absent from TABLE B; any Failure-visibility-window cell is blank; any Recovery-time
cell is blank; any `UNKNOWN` entry lacks a Notes reason. Downstream phases are valid only
when GATE 2 is cleared and no GATE 2 failure state is present.

---

**DOWNSTREAM PHASES**

**Phase 1a output is valid when** it names: the Tier-ID of the uniform-rate binding constraint
(citing its TABLE A Limit value), and the causal reason this tier binds before all others.

**Phase 1b output is valid when** it names: the Tier-ID of the burst-arrival binding constraint
(citing TABLE A Limit value), and includes at least one numeric effective-rate comparison
between uniform and burst delivery for the relevant tiers.

**Phase 1c output is valid only when** it contains exactly this structure:

> Binding tier at uniform arrival: ___
> Binding tier at burst arrival: ___
> Verdict: SAME TIER / DIFFERENT TIER
> Explanation: ___

The Phase 1c explanation is valid when: if DIFFERENT TIER, it names both Tier-IDs and cites
their specific TABLE A Limit values; if SAME TIER, it cites the binding tier's TABLE A Limit
value and explains why burst shape does not shift the constraint. A Phase 1c explanation
without TABLE A Limit citations is not valid.

---

TABLE C is valid when: (1) it traces from the Phase 1b burst-rate binding tier; (2) it contains
at least two rows; (3) every Mechanism cell contains exactly one of: `queue-fill`,
`connection-hold`, `retry-amplification`, `dependency-stall`; (4) no cell in TABLE C contains:
"also throttled", "cascade occurs", "propagates to", "downstream effect", "flow is affected",
"rate limiting applies"; (5) every Observable-effect cell names a distinct outcome. A TABLE C
where any Mechanism cell contains a generic token from the prohibited vocabulary is not valid.

| Hop | From-component | To-component | Mechanism | Observable-effect |
|-----|---------------|--------------|-----------|-------------------|
| *(ANTI-SUBSTITUTION: TABLE C is valid only when every Mechanism cell contains a named token from the four-item vocabulary; narrative paragraph substitution produces a not-valid TABLE C)* | | | | |
| 1 | | | | |
| 2 | | | | |

---

TABLE D is valid when: (1) at least one row is present; (2) every Gap-reason names a specific
structural absence; (3) every `?-unresolved` TABLE A tier on an unprotected path is flagged
in the Gap-tier column. A TABLE D row with a generic Gap-reason is not valid.

| Path-ID | Entry-component | Gap-reason | Gap-tier? | Consequence-at-burst-volume |
|---------|----------------|------------|-----------|-----------------------------|
| *(ANTI-SUBSTITUTION: TABLE D is valid only when each Gap-reason names the specific absent control; "no protection" or similar generic entries do not produce a valid TABLE D row)* | | | | |
| P-01 | | | | |

---

TABLE E is valid when: (1) every TABLE A tier has exactly one row, including `?-unresolved`
tiers; (2) every Retry-After cell is `Y`, `N`, or `UNKNOWN`; (3) every Failure-if-ignored
cell is one of: `immediate-retry-storm`, `exponential-backoff-absent`, `silent-infinite-loop`,
`flow-run-failure`; (4) `?-unresolved` tier rows have Confirmed = `ESTIMATED`. A TABLE E that
omits any TABLE A tier or uses free-form failure descriptions is not valid.

| Tier-ID | Error-signal | Retry-After? | Visible-in-history? | Failure-if-ignored | Confirmed? |
|---------|-------------|--------------|---------------------|-------------------|------------|
| *(ANTI-SUBSTITUTION: TABLE E is valid only when all TABLE A tiers appear including gap tiers; free-form failure-mode descriptions are not valid Failure-if-ignored values)* | | | | | |
| T-01 | | | | | |

---

TABLE F is valid when: (1) it contains exactly four rows with Volume values `1×`, `3×`, `5×`,
`10×`; (2) every Binding-tier cell names a TABLE A Tier-ID; (3) every Threshold-hit cell
cites the TABLE A Limit as "T-NN: [value]"; (4) every Error-rate% cell contains arithmetic
steps that name each limit used — an asserted percentage without arithmetic steps is not a
valid Error-rate% cell; (5) all Threshold-hit citations trace to named TABLE A rows. A TABLE F
without exactly four fixed-multiplier rows or without arithmetic-derived Error-rate% values
is not valid.

| Volume | Binding-tier | Threshold-hit | Behavior | Error-rate% |
|--------|-------------|---------------|----------|-------------|
| *(ANTI-SUBSTITUTION: TABLE F is valid only when it has exactly four fixed-multiplier rows with step-by-step arithmetic in Error-rate%; a free-form tier summary does not constitute a valid TABLE F)* | | | | |
| 1× | | | | |
| 3× | | | | |
| 5× | | | | |
| 10× | | | | |

---

**CASCADE SCENARIO.** The cascade scenario is valid when: it names at least three tiers in a
causal chain where throttling at tier N triggers throttling at tier N+1; each link states a
specific mechanism from the TABLE C vocabulary; no step uses the generic prohibited token
vocabulary. A cascade scenario using generic tokens is not valid.

**RETRY-AFTER GAP ASSESSMENT.** This section is valid when it names either the specific
Retry-After header and confirms correct caller handling, or names the TABLE E Failure-if-ignored
token that results from absent handling.

---

TABLE G is valid when: (1) at least two gaps are covered; (2) every Remediation names a
specific Power Automate setting, connector configuration parameter, API field, or implementation
pattern — entries without a named specific control are not valid Remediation cells; (3) every
Specific-config cell is non-blank. A TABLE G with generic prescription entries is not valid.

| Gap-ID | Type | Remediation | Specific-config-or-API |
|--------|------|-------------|------------------------|
| *(ANTI-SUBSTITUTION: TABLE G is valid only when each Remediation names a specific actionable control; generic recommendations produce a not-valid TABLE G row)* | | | |
| G-01 | | | |
| G-02 | | | |

---

**CORRECTION GATE**

Role 2 output is valid when every item below has an explicit disposition. Role 2 produces no
further output while any item is unresolved.

**GATE 3** is cleared when and only when every item below carries either `[CLEAR]` or a
`[FAIL: location]` annotation — GATE 3 is not cleared while any `- [ ]` item remains without
a disposition, and Role 4 execution is not valid unless GATE 3 is cleared:

- [ ] "also throttled" → `[CLEAR]` if absent; `[FAIL: TABLE C hop N — rewritten below]` if present
- [ ] "cascade occurs" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "propagates to" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "downstream effect" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "flow is affected" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "rate limiting applies" → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "no protection" (without naming the absent control) → `[CLEAR]` if absent; `[FAIL: location]` if present
- [ ] "unknown" (without a stated reason) → `[CLEAR]` if absent; `[FAIL: location]` if present

A rewrite is valid only when the corrected content appears immediately below its `[FAIL]`
annotation in the output stream — a rewrite is not valid when it appears in a separate
correction section, a later phase, or at end of output. Spatial co-location makes each
annotation and its corrected content auditable as a contiguous block by linear scan.

**GATE 3 is not cleared when** any `- [ ]` item remains without a disposition, or when any
`[FAIL]` annotation does not have its corrected content appearing immediately below it.

**GATE 3** is cleared when and only when: all eight items carry explicit dispositions; every
`[FAIL]` annotation has its corrected content immediately below it; no `- [ ]` item may
remain undisposed. Role 4 is valid only when GATE 3 is cleared.

---

**ROLE 4 — EXECUTE PRE-COMMITTED AUDIT CONTRACT**

*(GATE 3 must be cleared before Role 4 executes. Execute the PRE-COMMITTED AUDIT CONTRACT
declared before all analytical roles above. The contract terms — structural fact, mandate
scope restriction, verification checks, and verdict format — are fixed as declared and cannot
be supplemented or modified at execution time.)*
