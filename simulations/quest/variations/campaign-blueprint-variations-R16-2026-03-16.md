## campaign-blueprint — Round 16 Variations

---

## V-01 — Role Sequence: Pitch → Spec → Proposal

**Axis:** Role sequence. Runs executive pitch first to establish the strategic frame; spec fills technical substance; proposal synthesizes the business case. SETUP and REFLECTION tables are structurally identical to the v15 ceiling pattern with prose-only directives.

**Hypothesis:** Re-ordering the generation sequence does not introduce in-table RULE sentinel rows; C-40/C-41 FULL via prose-only directives; C-42/C-43 NO CREDIT; expected score 243.

---

```
# Campaign Blueprint: {{TOPIC}}

Produce the full specification package for {{TOPIC}} using a pitch-first generation
sequence. The executive pitch establishes the strategic narrative; the technical spec
substantiates feasibility; the business proposal closes the case. All three artifacts
are produced before REFLECTION begins.

---

## SETUP

Complete both structural tables in full before generating any artifact.

### Scout Traceability Table

Map every requirement signal to its scout source. Record gaps explicitly — a requirement
with no scout source is a coverage failure, not a placeholder.

| Req-ID | Requirement | Scout Signal | Source Artifact | Friction Note | Coverage |
|--------|-------------|--------------|-----------------|---------------|----------|
| R-01   |             |              |                 |               |          |
| R-02   |             |              |                 |               |          |
| R-03   |             |              |                 |               |          |

### Inertia Model Map

Map the conviction type each artifact must shift. Name the status-quo
competitor — the incumbent approach or the cost of doing nothing.

| Conv-ID | Conviction Type       | Artifact       | Register    |
|---------|-----------------------|----------------|-------------|
| CT-Spec | Technical feasibility | Draft-Spec     | Technical   |
| CT-Prop | Business case         | Draft-Proposal | Business    |
| CT-Pitch| Strategic alignment   | Draft-Pitch    | Executive   |

The CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop,
CT-Pitch), one per MAP entry. A missing row is a named-conviction-type absence — not
a count discrepancy.

---

## Artifact Generation — Pitch-First Sequence

### Phase 1: Draft-Pitch

Run the executive pitch first. Write for an executive audience: decision-framed,
outcome-anchored, inertia-aware. The pitch establishes the strategic claim that
Spec and Proposal will substantiate.

Produce:

**{{TOPIC}} — Executive Pitch**

- Lead with the decision the executive must make and when
- Name the status-quo competitor explicitly; state its cost in outcome terms
- State the delta this feature delivers, in business language
- Close with the single strongest reason to move now rather than later

### Phase 2: Draft-Spec

Run the technical specification after the pitch frame is established. The spec
substantiates the feasibility claims the pitch has already committed to.

Produce:

**{{TOPIC}} — Technical Specification**

- Architecture, interfaces, and integration surface
- Implementation approach and phasing
- Constraint and risk enumeration (not mitigation — that belongs in Proposal)
- Test surface: what must be verified to call this done

### Phase 3: Draft-Proposal

Run the business proposal last. The proposal bridges the pitch's strategic frame
and the spec's technical substance into a decision-ready business case.

Produce:

**{{TOPIC}} — Business Proposal**

- Business case: costs, benefits, ROI model with assumptions explicit
- Resource requirements: team, timeline, dependency
- Risk register with mitigations (drawn from Spec risk list)
- Decision recommendation with a named go/no-go threshold

---

## REFLECTION

Run REFLECTION after all three artifacts are complete. Do not run REFLECTION
against a partial artifact set.

### Conviction Delta

Assess conviction shift for each MAP entry after reviewing the full artifact suite.
The Amplification Chain cell records the causal path from trigger signal to conviction
outcome — pre-populated at authoring time, not left blank.

| Conv-ID  | Pre-Evidence Conviction | Post-Evidence Conviction | Amplification Chain                                      |
|----------|------------------------|-------------------------|----------------------------------------------------------|
| CT-Spec  |                        |                         | [trigger] → [signal] → [amplification] → [outcome]      |
| CT-Prop  |                        |                         | [trigger] → [signal] → [amplification] → [outcome]      |
| CT-Pitch |                        |                         | [trigger] → [signal] → [amplification] → [outcome]      |

### Conviction Gap Diagnosis

Diagnose what is missing from each conviction type, split by register. A gap is
a signal that would shift conviction if present. Pre-declare the three artifact
rows — do not introduce rows anonymously.

| Conv-ID  | Gap Type | Gap Description | Technical Register | Business Register | Executive Register |
|----------|----------|-----------------|--------------------|-------------------|--------------------|
| CT-Spec  |          |                 |                    |                   |                    |
| CT-Prop  |          |                 |                    |                   |                    |
| CT-Pitch |          |                 |                    |                   |                    |

### Traceability Audit

Verify coverage of every Req-ID from the SETUP Scout Traceability Table across all
three artifacts. The audit row count must match the SETUP table row count. A missing
Req-ID row is a named-entry absence (R-[NN] absent) — not a count discrepancy.

| Req-ID | Requirement | Scout Friction      | Spec Coverage | Proposal Coverage | Pitch Coverage |
|--------|-------------|---------------------|---------------|-------------------|----------------|
| R-01   |             | [from SETUP R-01]   |               |                   |                |
| R-02   |             | [from SETUP R-02]   |               |                   |                |
| R-03   |             | [from SETUP R-03]   |               |                   |                |
```

---

## V-02 — Phrasing Register: Conversational

**Axis:** Phrasing register. All instructions use first-person plural, conversational framing throughout. SETUP and REFLECTION tables are structurally identical to the v15 ceiling pattern. Directives are prose-only.

**Hypothesis:** Conversational register does not affect structural table scoring; register invariance from D16 applies; C-40/C-41 FULL; C-42/C-43 NO CREDIT; expected score 243.

---

```
# Campaign Blueprint: {{TOPIC}}

Let's build the full specification package for {{TOPIC}}. We're going to produce three
artifacts — a technical spec, a business proposal, and an executive pitch — and then
reflect on what they tell us about conviction. Here's the sequence we'll follow.

---

## SETUP — Before We Write Anything

First, let's build two structural tables that will anchor everything we produce.

### Scout Traceability Table

Let's map out every requirement we've got scout signal for. If a requirement has no
scout source, we note that explicitly — it's a gap we need to be honest about.

| Req-ID | Requirement | Scout Signal | Source Artifact | Friction Note | Coverage |
|--------|-------------|--------------|-----------------|---------------|----------|
| R-01   |             |              |                 |               |          |
| R-02   |             |              |                 |               |          |
| R-03   |             |              |                 |               |          |

### Inertia Model Map

Now let's map what each artifact is trying to shift. There's always a status-quo
competitor — the thing people are already doing, or the cost of doing nothing.
Let's name it and be clear about what conviction type each artifact needs to move.

| Conv-ID  | Conviction Type       | Artifact       | Register    |
|----------|-----------------------|----------------|-------------|
| CT-Spec  | Technical feasibility | Draft-Spec     | Technical   |
| CT-Prop  | Business case         | Draft-Proposal | Business    |
| CT-Pitch | Strategic alignment   | Draft-Pitch    | Executive   |

One thing to remember: when we get to REFLECTION, the CONVICTION DELTA table needs
exactly one row per entry here — CT-Spec, CT-Prop, and CT-Pitch. If one of those rows
is missing, that's a named-conviction-type absence, not just a short table.

---

## The Artifacts

### Draft-Spec — Technical Specification

Let's write the spec for a technical audience. We want this to be implementation-precise
and testable — engineers should be able to read it and know what done looks like.

**{{TOPIC}} — Technical Specification**

- What the architecture looks like, and where it integrates with existing systems
- How we'd implement it, with any phasing considerations
- Constraints and risks we need to be honest about
- What the test surface is — what we have to verify

### Draft-Proposal — Business Proposal

Now let's write the business case. This one bridges the technical spec and the executive
pitch — it needs to speak business language without losing technical accuracy.

**{{TOPIC}} — Business Proposal**

- The business case: what it costs, what it returns, and what assumptions we're making
- What resources and timeline look like
- The risk register, with mitigations drawn from what the spec identified
- A clear decision recommendation with a named threshold

### Draft-Pitch — Executive Pitch

Finally, let's write the pitch. This one goes to people who need to make a decision,
not read a spec. Keep it decision-framed and short.

**{{TOPIC}} — Executive Pitch**

- What's the decision and when does it need to be made?
- What's the cost of doing nothing, or of staying with the current approach?
- What does success look like in business terms?
- What's the one reason to move now?

---

## REFLECTION — What Did We Learn?

Once all three artifacts are written, let's step back and assess.

### Conviction Delta

Let's check our conviction on each type after seeing the full artifact set. For each
row, fill in the Amplification Chain — the causal path from trigger signal to conviction
outcome. Don't leave these blank; pre-populate the template now.

| Conv-ID  | Pre-Evidence Conviction | Post-Evidence Conviction | Amplification Chain                                 |
|----------|------------------------|-------------------------|-----------------------------------------------------|
| CT-Spec  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Prop  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Pitch |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |

### Conviction Gap Diagnosis

What's missing from each conviction type? Let's be specific about which register
the gap lives in — technical, business, or executive. Pre-declare the three rows.

| Conv-ID  | Gap Type | Gap Description | Technical Register | Business Register | Executive Register |
|----------|----------|-----------------|--------------------|-------------------|--------------------|
| CT-Spec  |          |                 |                    |                   |                    |
| CT-Prop  |          |                 |                    |                   |                    |
| CT-Pitch |          |                 |                    |                   |                    |

### Traceability Audit

Let's check that every requirement we listed in SETUP got covered somewhere in the
artifact suite. One row per Req-ID from the Scout Traceability Table — if a row is
missing, that's a named gap (R-[NN] absent), not just a shorter table.

| Req-ID | Requirement | Scout Friction      | Spec Coverage | Proposal Coverage | Pitch Coverage |
|--------|-------------|---------------------|---------------|-------------------|----------------|
| R-01   |             | [from SETUP R-01]   |               |                   |                |
| R-02   |             | [from SETUP R-02]   |               |                   |                |
| R-03   |             | [from SETUP R-03]   |               |                   |                |
```

---

## V-03 — Inertia Framing: Maximum Status-Quo Prominence

**Axis:** Inertia framing. The status-quo competitor is named at the opening, tracked in SETUP, and carried as an explicit comparison axis through all three artifact phases and into REFLECTION. The MAP includes an incumbent column. Directives are prose-only.

**Hypothesis:** Inertia framing prominence increases artifact coherence and foregrounds the displacement case, but does not introduce in-table RULE sentinel rows; C-40/C-41 FULL; C-42/C-43 NO CREDIT; expected score 243.

---

```
# Campaign Blueprint: {{TOPIC}}

Every specification package has a hidden competitor: the thing the organization is
already doing, or the cost of continuing to do nothing. Name that competitor before
writing a single artifact line. The incumbent is the frame against which conviction
must shift.

---

## SETUP

### Incumbent Declaration

State the status-quo competitor explicitly before mapping requirements or conviction
types. All subsequent tables will reference this framing.

**Incumbent:** [Name the current approach, vendor, or null state being displaced]
**Incumbent cost:** [Quantify — time, money, risk, or capability gap — not prose generality]
**Displacement claim:** [One sentence: what {{TOPIC}} does that the incumbent cannot]

---

### Scout Traceability Table

Map requirements against the incumbent. A requirement that the incumbent already
satisfies is a parity requirement — still record it, but mark it. A requirement
the incumbent cannot satisfy is the displacement surface.

| Req-ID | Requirement | Scout Signal | Source Artifact | Incumbent Gap | Coverage |
|--------|-------------|--------------|-----------------|---------------|----------|
| R-01   |             |              |                 |               |          |
| R-02   |             |              |                 |               |          |
| R-03   |             |              |                 |               |          |

### Inertia Model Map

Map conviction types to artifacts and register the incumbent's position for each
conviction axis. The conviction shift is not abstract — it is the delta from
"incumbent is good enough" to "{{TOPIC}} is worth the transition cost."

| Conv-ID  | Conviction Type       | Artifact       | Register    | Incumbent Position               |
|----------|-----------------------|----------------|-------------|----------------------------------|
| CT-Spec  | Technical feasibility | Draft-Spec     | Technical   | [what the incumbent does today]  |
| CT-Prop  | Business case         | Draft-Proposal | Business    | [incumbent cost model]           |
| CT-Pitch | Strategic alignment   | Draft-Pitch    | Executive   | [incumbent strategic narrative]  |

The CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop,
CT-Pitch), one per MAP entry. Each row is an assessment of delta from the incumbent
position recorded above. A missing row is a named-conviction-type absence, not a
count discrepancy.

---

## Artifact Generation

Generate all three artifacts with the incumbent framing active throughout. Each
artifact must name the incumbent and make the displacement case explicit.

### Draft-Spec — Technical Specification

Write for a technical audience. Anchor the feasibility claim against the incumbent —
what does {{TOPIC}} do technically that the incumbent cannot? Where does the
incumbent's architecture make this impossible?

**{{TOPIC}} — Technical Specification**

- Architecture and interfaces; highlight where incumbent integration points are severed
- Implementation approach; note where incumbent migration is a constraint
- Risks and constraints; distinguish {{TOPIC}}-specific risk from incumbent-transition risk
- Test surface; include incumbent-parity tests and displacement-verification tests

### Draft-Proposal — Business Proposal

Write for a business audience. The business case must compare explicitly to the
incumbent — not just "here is what {{TOPIC}} costs" but "here is the delta versus
continuing with the incumbent."

**{{TOPIC}} — Business Proposal**

- Business case: total cost of ownership delta versus incumbent over 12/24/36 months
- Transition cost: what does moving from the incumbent require?
- Risk register: include incumbent-retention risk (what happens if we do not move)
- Decision recommendation: frame the threshold as incumbent-vs-{{TOPIC}}, not an
  absolute cost comparison

### Draft-Pitch — Executive Pitch

Write for an executive audience. Lead with the incumbent's strategic liability —
what does continuing with the incumbent cost strategically? The pitch wins if the
executive leaves believing the incumbent is the risk, not the change.

**{{TOPIC}} — Executive Pitch**

- Open: name the incumbent and its strategic cost in concrete terms
- Delta: what {{TOPIC}} enables that the incumbent structurally prevents
- Timing: why the incumbent advantage window closes
- Close: the decision frame — incumbent risk vs. transition cost

---

## REFLECTION

Run REFLECTION after all three artifacts are complete.

### Conviction Delta

Assess conviction shift per MAP entry. The shift is measured from the incumbent
position recorded in SETUP, not from a neutral baseline. Amplification Chain
records the causal path from the incumbent's vulnerability to the conviction outcome.

| Conv-ID  | Pre-Evidence Conviction | Post-Evidence Conviction | Amplification Chain                                 |
|----------|------------------------|-------------------------|-----------------------------------------------------|
| CT-Spec  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Prop  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Pitch |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |

### Conviction Gap Diagnosis

Diagnose gaps by register. An inertia-specific gap is a missing signal that would
have made the incumbent's position untenable — record it as a displacement gap,
not a generic evidence gap.

| Conv-ID  | Gap Type | Gap Description | Technical Register | Business Register | Executive Register |
|----------|----------|-----------------|--------------------|-------------------|--------------------|
| CT-Spec  |          |                 |                    |                   |                    |
| CT-Prop  |          |                 |                    |                   |                    |
| CT-Pitch |          |                 |                    |                   |                    |

### Traceability Audit

Verify that every Req-ID from the SETUP Scout Traceability Table is covered across
the artifact suite. Incumbent-gap requirements must show how each artifact addresses
the gap the incumbent creates. The audit row count must match the SETUP table row
count. A missing row is a named-entry absence (R-[NN] absent).

| Req-ID | Requirement | Incumbent Gap (from SETUP) | Spec Coverage | Proposal Coverage | Pitch Coverage |
|--------|-------------|---------------------------|---------------|-------------------|----------------|
| R-01   |             | [from SETUP R-01]          |               |                   |                |
| R-02   |             | [from SETUP R-02]          |               |                   |                |
| R-03   |             | [from SETUP R-03]          |               |                   |                |
```

---

## V-04 — Combined: Maximum-Density In-Table Sentinel Chain

**Axes:** In-table RULE sentinel in INERTIA MODEL MAP (SETUP) + in-table RULE sentinel in CONVICTION DELTA (REFLECTION). Maximum declaration density: sentinel rows are explicit, self-contained enforcement statements inside each table.

**Hypothesis:** Both in-table RULE sentinel rows are structurally present and precede their respective data rows; C-42 FULL + C-43 FULL; total 253. The MAP is self-enforcing: its structure simultaneously declares the named CT entries and the rule that binds CONVICTION DELTA to those entries. The CONVICTION DELTA table is independently self-enforcing: each row's Conv-ID is bound at the table level to a named MAP entry, with a declaration that a missing row is a named-conviction-type absence.

---

```
# Campaign Blueprint: {{TOPIC}}

Produce the full specification package for {{TOPIC}}: technical spec, business proposal,
and executive pitch. All structural tables must be complete in SETUP before any artifact
is generated. REFLECTION runs after all three artifacts are complete.

---

## SETUP

### Scout Traceability Table

Map every requirement signal to its scout artifact source. A requirement with no scout
source is an explicit coverage gap — record it; do not omit it.

| Req-ID | Requirement | Scout Signal | Source Artifact | Friction Note | Coverage |
|--------|-------------|--------------|-----------------|---------------|----------|
| R-01   |             |              |                 |               |          |
| R-02   |             |              |                 |               |          |
| R-03   |             |              |                 |               |          |

The Traceability Audit in REFLECTION must contain one row per Req-ID above, with
Scout Friction sourced from this table. A missing Req-ID row is a named-entry absence
(R-[NN] absent), not a count discrepancy.

### Inertia Model Map

Map conviction type per artifact. This table governs the CONVICTION DELTA structure
in REFLECTION — every REFLECTION row must correspond to a named entry here.

| Conv-ID  | Conviction Type       | Artifact       | Register    |
|----------|-----------------------|----------------|-------------|
| RULE     | The CONVICTION DELTA in REFLECTION must contain exactly 3 rows — CT-Spec, CT-Prop, CT-Pitch — one per MAP entry. A missing row is a named-conviction-type absence (CT-[X] absent), not a count discrepancy. | — | — |
| CT-Spec  | Technical feasibility | Draft-Spec     | Technical   |
| CT-Prop  | Business case         | Draft-Proposal | Business    |
| CT-Pitch | Strategic alignment   | Draft-Pitch    | Executive   |

---

## Artifact Generation

Generate all three artifacts before running REFLECTION. Artifacts may reference each
other but are produced independently.

### Draft-Spec — Technical Specification

Write for a technical audience: implementation-precise, interface-defined, testable.

**{{TOPIC}} — Technical Specification**

- Architecture and integration surface
- Implementation approach and phase dependencies
- Constraint and risk enumeration
- Test surface: the verification conditions for done

### Draft-Proposal — Business Proposal

Write for a business audience: cost-benefit-explicit, timeline-anchored, decision-ready.

**{{TOPIC}} — Business Proposal**

- Business case with ROI model and explicit assumptions
- Resource requirements: team, timeline, external dependency
- Risk register with mitigations sourced from the Spec risk list
- Decision recommendation with a named go/no-go threshold

### Draft-Pitch — Executive Pitch

Write for an executive audience: decision-framed, outcome-anchored, inertia-aware.

**{{TOPIC}} — Executive Pitch**

- The decision and its timing
- The cost of the status-quo competitor
- The outcome delta in business terms
- The single strongest reason to act now

---

## REFLECTION

Run REFLECTION after all three artifacts are complete. Do not begin REFLECTION
against a partial artifact set.

### Conviction Delta

Assess conviction shift per named MAP entry. Every row's Conv-ID must correspond
to a named INERTIA MODEL MAP entry from SETUP — no anonymous rows.

| Conv-ID  | Pre-Evidence Conviction | Post-Evidence Conviction | Amplification Chain                                 |
|----------|------------------------|-------------------------|-----------------------------------------------------|
| RULE     | Each row's Conv-ID must match a named INERTIA MODEL MAP entry (CT-Spec, CT-Prop, CT-Pitch). A missing row is a named-conviction-type absence (CT-[X] absent), not a count discrepancy. | — | — |
| CT-Spec  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Prop  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Pitch |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |

### Conviction Gap Diagnosis

Diagnose gaps per conviction type, split by register. Pre-declare the three artifact
rows — every row is named from the MAP, none introduced anonymously.

| Conv-ID  | Gap Type | Gap Description | Technical Register | Business Register | Executive Register |
|----------|----------|-----------------|--------------------|-------------------|--------------------|
| CT-Spec  |          |                 |                    |                   |                    |
| CT-Prop  |          |                 |                    |                   |                    |
| CT-Pitch |          |                 |                    |                   |                    |

### Traceability Audit

Verify coverage of every Req-ID from the SETUP Scout Traceability Table. One row per
Req-ID; Scout Friction sourced from SETUP. The audit row count must match the SETUP
Scout Traceability Table row count. A missing row is a named-entry absence (R-[NN]
absent), not a count discrepancy.

| Req-ID | Requirement | Scout Friction      | Spec Coverage | Proposal Coverage | Pitch Coverage |
|--------|-------------|---------------------|---------------|-------------------|----------------|
| R-01   |             | [from SETUP R-01]   |               |                   |                |
| R-02   |             | [from SETUP R-02]   |               |                   |                |
| R-03   |             | [from SETUP R-03]   |               |                   |                |
```

---

## V-05 — Combined: Minimum-Density In-Table Sentinel Chain

**Axes:** In-table RULE sentinel in INERTIA MODEL MAP (SETUP) + in-table RULE sentinel in CONVICTION DELTA (REFLECTION). Minimum declaration density: sentinel rows carry the structurally necessary content and nothing beyond it. Tests density invariance from D16.

**Hypothesis:** Minimal sentinel text satisfies the structural presence test — a RULE row is a RULE row regardless of surrounding prose volume; C-42 FULL + C-43 FULL; total 253. Confirms that C-42 and C-43 are structural properties independent of directive density.

---

```
# Campaign Blueprint: {{TOPIC}}

Produce the specification package for {{TOPIC}}: technical spec, business proposal,
executive pitch. Complete SETUP tables before generating artifacts. Run REFLECTION
after all three artifacts are complete.

---

## SETUP

### Scout Traceability Table

| Req-ID | Requirement | Scout Signal | Source Artifact | Friction Note | Coverage |
|--------|-------------|--------------|-----------------|---------------|----------|
| R-01   |             |              |                 |               |          |
| R-02   |             |              |                 |               |          |
| R-03   |             |              |                 |               |          |

Traceability Audit in REFLECTION: one row per Req-ID. Missing row = named absence.

### Inertia Model Map

| Conv-ID  | Conviction Type       | Artifact       | Register    |
|----------|-----------------------|----------------|-------------|
| RULE     | CONVICTION DELTA must have one row per entry below. Missing = named absence. | — | — |
| CT-Spec  | Technical feasibility | Draft-Spec     | Technical   |
| CT-Prop  | Business case         | Draft-Proposal | Business    |
| CT-Pitch | Strategic alignment   | Draft-Pitch    | Executive   |

---

## Artifact Generation

### Draft-Spec — Technical Specification

Write for a technical audience.

**{{TOPIC}} — Technical Specification**

- Architecture and integration surface
- Implementation approach
- Constraints and risks
- Test surface

### Draft-Proposal — Business Proposal

Write for a business audience.

**{{TOPIC}} — Business Proposal**

- Business case and ROI
- Resource and timeline
- Risk register with mitigations
- Decision recommendation

### Draft-Pitch — Executive Pitch

Write for an executive audience.

**{{TOPIC}} — Executive Pitch**

- The decision and timing
- Status-quo cost
- Outcome delta
- Reason to act now

---

## REFLECTION

### Conviction Delta

| Conv-ID  | Pre-Evidence Conviction | Post-Evidence Conviction | Amplification Chain                                 |
|----------|------------------------|-------------------------|-----------------------------------------------------|
| RULE     | Conv-ID must match a MAP entry. Missing = named absence. | — | — |
| CT-Spec  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Prop  |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |
| CT-Pitch |                        |                         | [trigger] → [signal] → [amplification] → [outcome] |

### Conviction Gap Diagnosis

| Conv-ID  | Gap Type | Gap Description | Technical Register | Business Register | Executive Register |
|----------|----------|-----------------|--------------------|-------------------|--------------------|
| CT-Spec  |          |                 |                    |                   |                    |
| CT-Prop  |          |                 |                    |                   |                    |
| CT-Pitch |          |                 |                    |                   |                    |

### Traceability Audit

One row per Req-ID from SETUP. Scout Friction sourced from SETUP table. Missing row =
named absence (R-[NN] absent).

| Req-ID | Requirement | Scout Friction      | Spec Coverage | Proposal Coverage | Pitch Coverage |
|--------|-------------|---------------------|---------------|-------------------|----------------|
| R-01   |             | [from SETUP R-01]   |               |                   |                |
| R-02   |             | [from SETUP R-02]   |               |                   |                |
| R-03   |             | [from SETUP R-03]   |               |                   |                |
```

---

## Variation Summary

| Variant | Axis | Hypothesis | C-40 | C-41 | C-42 | C-43 | Expected Score |
|---------|------|-----------|------|------|------|------|----------------|
| V-01 | Role sequence (Pitch→Spec→Prop) | Sequence change; prose-only directives | FULL | FULL | NO CREDIT | NO CREDIT | 243 |
| V-02 | Phrasing register (conversational) | Register invariance; prose-only directives | FULL | FULL | NO CREDIT | NO CREDIT | 243 |
| V-03 | Inertia framing (maximum prominence) | Framing depth; prose-only directives | FULL | FULL | NO CREDIT | NO CREDIT | 243 |
| V-04 | In-table sentinels (max density) | Both MAP + CONVICTION DELTA carry RULE rows; full text | FULL | FULL | FULL | FULL | **253** |
| V-05 | In-table sentinels (min density) | Structural presence invariant to prose volume | FULL | FULL | FULL | FULL | **253** |

**Ceiling prediction:** V-04 and V-05 both reach 253. The distinguishing diagnostic for C-42/C-43 is purely structural — the presence of a non-data RULE row inside the table, positioned before the CT data rows. V-01–V-03 hold at 243 via prose-only directives regardless of sequence, register, or framing variation.
