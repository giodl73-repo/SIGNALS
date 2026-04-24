# campaign-blueprint — Round 14 Variates (v14 rubric)

---

## V-01 — Single axis: Named-Row SETUP Linkage (C-38 isolation)

**Variation axis**: TRACEABILITY AUDIT named-row SETUP linkage only  
**Hypothesis**: Pre-named Req-ID rows sourced from the SETUP SCOUT TRACEABILITY TABLE earn C-38 FULL independent of whether CONVICTION DELTA and CONVICTION GAP DIAGNOSIS are structural tables. Establishes the minimum footprint for C-38 — no C-34, no C-35, therefore no C-37, no C-39.

---

You are running **campaign-blueprint** for: **$TOPIC**

Produce draft-spec, draft-proposal, and draft-pitch in sequence. Document the conviction lifecycle from SETUP through REFLECTION.

---

### CAMPAIGN SETUP

**Feature**: $TOPIC  
**Status-quo competitor**: Name the incumbent tool, workflow, or behavior that $TOPIC displaces. This name appears in every artifact.  
**Conviction register**: Choose one dominant register (urgency / confidence / relief / momentum). State it explicitly — this is the target register for all three artifacts.

**SCOUT TRACEABILITY TABLE**

Draw from available scout-requirements and scout-positioning artifacts. Assign Req-IDs now — these identifiers are pre-declared and will appear by name in the TRACEABILITY AUDIT in REFLECTION. Do not leave them blank for later assignment.

| Req-ID | Scout-Requirements Friction | Source Artifact | Must-have criterion |
|--------|-----------------------------|-----------------|---------------------|
| R-01   | [specific friction finding from scout-requirements] | [source file] | [what the spec must address to close this friction] |
| R-02   | [specific friction finding from scout-requirements] | [source file] | [what the spec must address to close this friction] |
| R-03   | [specific friction finding from scout-positioning]  | [source file] | [what the spec must address to close this friction] |

Add rows to match all available friction findings. The TRACEABILITY AUDIT must have one pre-named row per Req-ID declared here — no more, no fewer.

---

### OPEN

One paragraph. Name the status-quo competitor. State the conviction register. Name the three audiences: draft-spec → engineering, draft-proposal → product leadership, draft-pitch → executive.

---

### DRAFT-SPEC

Technical specification for $TOPIC.

**Sections**: Overview | Requirements | Design | Constraints | Open Questions

In the Requirements section, create one subsection per Req-ID from the SETUP table. Label each: **R-NN: [friction source name]**. A Req-ID absent from Requirements is a structural gap — named, not counted.

---

### DRAFT-PROPOSAL

Business proposal for $TOPIC.

**Sections**: Problem | Solution | Value | Risk | Ask

In Problem, name the status-quo competitor explicitly. In Value, cite at least one Req-ID from the SETUP table as the grounding for the primary value claim.

---

### DRAFT-PITCH

Executive pitch for $TOPIC. Four to six sections.

**Sections**: The Moment | The Gap | The Feature | The Signal | The Ask

The pitch makes the conviction register visceral. It does not repeat the spec. The Gap section names the status-quo competitor. The Signal section invokes the conviction register from SETUP by name.

---

### CLOSE

**CONVICTION GAP DIAGNOSIS**

Review all three artifacts. For each sub-section where the conviction register weakens, write:

> In [artifact] / [sub-section]: the register found is [observed]. The declared register is [conviction register from SETUP]. The gap originates in [scout sub-skill] evidence. Evidence needed: [specific].

Write at least one gap entry per artifact.

---

### REFLECTION

**CONVICTION DELTA**

For each artifact, state the conviction established, the Req-ID(s) that ground it, and the amplification mechanism. Write as prose:

> The [artifact]'s conviction is [type], grounded in [Req-ID]. The amplification is: [how the emotional register makes the factual claim visceral].

---

**TRACEABILITY AUDIT**

Verify each must-have criterion against the draft-spec. The rows below are pre-declared using the Req-IDs and Scout-Requirements Friction descriptions from the SETUP SCOUT TRACEABILITY TABLE — sourced from that table, not written fresh at audit time.

| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| R-01   | [friction from SETUP R-01 — pre-populated] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-requirements |
| R-02   | [friction from SETUP R-02 — pre-populated] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-requirements |
| R-03   | [friction from SETUP R-03 — pre-populated] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-positioning  |

**AUDIT DIRECTIVE**: This table has one pre-named row per Req-ID in the SETUP SCOUT TRACEABILITY TABLE. The row count must equal that table's row count. A missing row is a named-identifier absence — "R-02 is absent" is structurally visible at a glance; it is not a count shortfall requiring external comparison.

---

*END OF CAMPAIGN*

---

---

## V-02 — Single axis: Complete Three-Table Structural Chain (C-39 target, 233 ceiling)

**Variation axis**: All three structural tables simultaneously at maximum resolution  
**Hypothesis**: A single variant carrying C-34-compliant CONVICTION DELTA, C-35-compliant CONVICTION GAP DIAGNOSIS, and C-38-compliant TRACEABILITY AUDIT satisfies C-37 (chain completeness) and C-39 (chain at maximum resolution) simultaneously, reaching the 233 ceiling. The structural tables are the only change from a v11-era baseline — no framing or sequence changes.

---

You are running **campaign-blueprint** for: **$TOPIC**

Produce draft-spec, draft-proposal, and draft-pitch in sequence. Structural tables govern every conviction-lifecycle verification point.

---

### CAMPAIGN SETUP

**Feature**: $TOPIC  
**Status-quo competitor**: Name it.  
**Conviction register**: Choose one (urgency / confidence / relief / momentum). State the specific user population it targets.

**INERTIA MODEL MAP**

One row per artifact. This map pre-declares the conviction type for each artifact — the CONVICTION DELTA table in REFLECTION is built from it.

| Version       | Conviction type | Status-quo friction addressed | Req-ID grounding |
|---------------|-----------------|-------------------------------|------------------|
| draft-spec    | [e.g., Confidence] | [technical friction]       | [R-NN]           |
| draft-proposal | [e.g., Urgency]  | [business friction]          | [R-NN]           |
| draft-pitch   | [e.g., Momentum] | [strategic friction]         | [R-NN]           |

**SCOUT TRACEABILITY TABLE**

| Req-ID | Scout-Requirements Friction | Source Artifact | Must-have criterion |
|--------|-----------------------------|-----------------|---------------------|
| R-01   | [specific friction] | [source] | [must-have for spec] |
| R-02   | [specific friction] | [source] | [must-have for spec] |
| R-03   | [specific friction] | [source] | [must-have for spec] |

Declare all Req-IDs before producing any artifact. The TRACEABILITY AUDIT in REFLECTION contains exactly one pre-named row per Req-ID declared here.

---

### OPEN

One paragraph. Name the status-quo competitor. State the conviction register. Define the three audiences.

---

### DRAFT-SPEC

Technical specification for $TOPIC.

**Sections**: Overview | Requirements | Design | Constraints | Open Questions

Requirements: one subsection per Req-ID, labeled **R-NN: [friction source name]**.

---

### DRAFT-PROPOSAL

Business proposal for $TOPIC.

**Sections**: Problem | Solution | Value | Risk | Ask

Problem: name the status-quo competitor. Value: cite Req-IDs as grounding evidence.

---

### DRAFT-PITCH

Executive pitch for $TOPIC.

**Sections**: The Moment | The Gap | The Feature | The Signal | The Ask

Gap: name the status-quo competitor. Signal: invoke the conviction register from SETUP by name.

---

### CLOSE

**CONVICTION GAP DIAGNOSIS**

Structural table. Pre-declare three rows — one per artifact. A row with a blank Evidence needed cell is a structural gap (cell-level incompleteness, visible at a glance).

| Artifact       | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
|----------------|----------------------------------|----------------|-------------------|-----------------|-----------------|
| draft-spec     | [sub-section name]               | [observed register] | [declared register] | [scout-requirements / scout-positioning / etc.] | [specific evidence] |
| draft-proposal | [sub-section name]               | [observed register] | [declared register] | [scout sub-skill] | [specific evidence] |
| draft-pitch    | [sub-section name]               | [observed register] | [declared register] | [scout sub-skill] | [specific evidence] |

**Columns**: Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed

---

### REFLECTION

**CONVICTION DELTA**

Structural table. One row per artifact — rows are pre-declared from the INERTIA MODEL MAP in SETUP. The Amplification chain column carries a pre-defined cell template; fill it completely or the cell is structurally incomplete.

| Version        | Conviction established | Grounding Req-ID(s) | Amplification chain |
|----------------|------------------------|---------------------|---------------------|
| draft-spec     | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |
| draft-proposal | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |
| draft-pitch    | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |

**Columns**: Version | Conviction established | Grounding Req-ID(s) | Amplification chain  
**Cell template (Amplification chain)**: `[Req-ID]'s [specific factual claim] is made visceral by [emotional register]` — all three components required; no paraphrase; a cell missing any component is structurally incomplete.

---

**TRACEABILITY AUDIT**

Structural table. Pre-named rows from the SETUP SCOUT TRACEABILITY TABLE — one row per Req-ID declared in SETUP. The Scout-Requirements Friction cell in each row is pre-populated from that table; it is not written fresh at audit time. The row count of this table must equal the row count of the SETUP table. A missing row is a named-identifier absence — identified by its Req-ID, not by count comparison.

| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| R-01   | [pre-populated from SETUP R-01] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-requirements |
| R-02   | [pre-populated from SETUP R-02] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-requirements |
| R-03   | [pre-populated from SETUP R-03] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-positioning  |

**AUDIT DIRECTIVE**: Each row is pre-named with its SETUP-sourced Req-ID. Scout-Requirements Friction is sourced from the SETUP SCOUT TRACEABILITY TABLE — pre-populated before the audit runs. The row count must match that table. A missing Req-ID row is a named-entry absence (e.g., "R-02 is absent"), not a count shortfall requiring external comparison.

---

*END OF CAMPAIGN*

---

---

## V-03 — Single axis: Inertia Framing Prominence

**Variation axis**: Status-quo competitor explicitly named and tracked at every lifecycle phase — no structural tables introduced  
**Hypothesis**: Foregrounding the inertia model throughout all artifact sections and lifecycle phases sharpens conviction independently of structural enforcement. Tests whether framing depth alone changes the artifact suite's conviction quality. This variant uses C-36-level TRACEABILITY AUDIT (anonymous template row, no named SETUP linkage) and C-31-level CONVICTION DELTA (prose with Req-ID citation). No C-34, no C-35, no C-38, no C-37, no C-39.

---

You are running **campaign-blueprint** for: **$TOPIC**

The status-quo competitor is the central actor in this campaign. Every artifact section opens by naming what the status-quo does in that area and where it fails. $TOPIC is framed as displacement, not addition.

---

### CAMPAIGN SETUP

**Feature**: $TOPIC  
**Status-quo competitor**: Name it. This name appears in the opening sentence of every artifact section.

**INERTIA MODEL**

| Status-quo strength | Status-quo friction | Switching cost $TOPIC overcomes |
|---------------------|---------------------|---------------------------------|
| [what it does well] | [where it breaks down] | [how $TOPIC makes switching worth it] |
| [what it does well] | [where it breaks down] | [how $TOPIC makes switching worth it] |
| [what it does well] | [where it breaks down] | [how $TOPIC makes switching worth it] |

Map at least three rows. The friction column feeds the SCOUT TRACEABILITY TABLE. The switching cost column feeds the CONVICTION DELTA in REFLECTION.

**Conviction register**: Choose one (urgency / confidence / relief / momentum). The register is driven by the switching cost narrative — the emotional consequence of the status-quo no longer applying.

**SCOUT TRACEABILITY TABLE**

| Req-ID | Scout-Requirements Friction | Source Artifact | Must-have criterion |
|--------|-----------------------------|-----------------|---------------------|
| R-01   | [friction] | [source] | [criterion] |
| R-02   | [friction] | [source] | [criterion] |
| R-03   | [friction] | [source] | [criterion] |

---

### OPEN

Name the status-quo competitor in the first sentence. State why users are stuck with it — be specific about the friction cost. State what displacement looks like. Name the three audiences.

---

### DRAFT-SPEC

Technical specification for $TOPIC.

Each major section opens with one sentence naming what the status-quo competitor does in this area and where it fails. The spec describes $TOPIC as the replacement, not an addition.

**Sections**:
- **Overview**: "$TOPIC replaces [status-quo] for [use case]. [Status-quo] produces [friction] here."
- **Requirements**: One subsection per Req-ID. Each opens with: "This requirement exists because [status-quo] [specific failure mode]."
- **Design**: Where design decisions are driven by status-quo displacement or compatibility
- **Constraints**: What the status-quo imposes that $TOPIC must respect during transition
- **Migration**: How users move from [status-quo] to $TOPIC — one step at a time

---

### DRAFT-PROPOSAL

Business proposal for $TOPIC.

The status-quo competitor is named in every section header or opening sentence.

**Sections**:
- **Problem**: "[Status-quo] costs [users] [X]. The friction is [specific]."
- **Solution**: "$TOPIC displaces [status-quo] by [mechanism]."
- **Value**: Quantify the displacement. Cite at least one Req-ID.
- **Risk**: "If we do not ship $TOPIC, users remain on [status-quo] for [duration] at [cost]."
- **Ask**: Resources and timeline required to complete displacement.

---

### DRAFT-PITCH

Executive pitch for $TOPIC. Four to six sections.

The pitch opens and closes with the status-quo competitor. The arc: users are stuck → $TOPIC unsticks them → the decision is whether to act now.

**Sections**:
- **The Moment**: "[Status-quo] is why users experience [problem state] today."
- **The Gap**: What [status-quo] does that perpetuates this
- **The Feature**: What $TOPIC replaces — in one sentence
- **The Signal**: The conviction register: what users feel when the status-quo is displaced
- **The Ask**: The decision

---

### CLOSE

**CONVICTION GAP DIAGNOSIS**

For each artifact, identify the section where the status-quo competitor framing is weakest — where the conviction register slips from displacement to neutral description. For each gap:

> In [artifact] / [sub-section]: the register found is [descriptive / neutral]. The declared register is [conviction register from SETUP]. The gap originates in [scout sub-skill] evidence. Evidence needed: [specific friction data about the status-quo].

---

### REFLECTION

**CONVICTION DELTA**

For each artifact, state the conviction established, cite the Req-ID(s) that ground it, and name the switching cost that amplifies it. Write as prose:

> The [artifact]'s conviction is [type], grounded in [Req-ID]. The switching cost it names — [specific friction from INERTIA MODEL] — makes the factual claim visceral by [emotional mechanism].

---

**TRACEABILITY AUDIT**

For each Req-ID in the SETUP SCOUT TRACEABILITY TABLE, verify whether its must-have criterion appears in the draft-spec. Fill this table at audit time:

| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| [Req-ID] | [friction] | Y / N | [exact phrase or blank] | [gap if N] | [namespace] |

A row with N in "Must-have found?" and a blank "Gap" cell is structurally incomplete — the blank is a cell-level gap, not a passing omission.

---

*END OF CAMPAIGN*

---

---

## V-04 — Combination: Pitch-First Role Sequence + C-38

**Variation axes (combined)**: Role sequence reorder (pitch-first) + Named-Row SETUP Linkage (C-38)  
**Hypothesis**: Running draft-pitch before draft-spec establishes the conviction register before technical constraints are introduced, potentially preventing register degradation in the spec. C-38 TRACEABILITY AUDIT closes the traceability loop. Tests whether pitch-first sequence combined with C-38 (but without C-35 structural CONVICTION GAP DIAGNOSIS) produces a different conviction profile than the standard spec-first sequence. Earns C-34 + C-36 + C-38 but not C-35, C-37, or C-39.

---

You are running **campaign-blueprint** for: **$TOPIC**

Produce the specification package in conviction-first order: draft-pitch first, then draft-spec, then draft-proposal. The pitch establishes the emotional register that the spec and proposal must sustain.

---

### CAMPAIGN SETUP

**Feature**: $TOPIC  
**Status-quo competitor**: Name it.  
**Conviction register**: Choose one (urgency / confidence / relief / momentum). The pitch declares it; the spec grounds it; the proposal amplifies it.

**CONVICTION-FIRST RATIONALE**: The pitch is produced first because conviction is the hardest artifact to maintain under technical specification pressure. By declaring the emotional register in the pitch before writing the spec, the spec and proposal can be audited against a concrete baseline rather than a theoretical declaration.

**INERTIA MODEL MAP** (one row per artifact, in production order)

| Version        | Conviction type | Status-quo friction addressed | Req-ID grounding |
|----------------|-----------------|-------------------------------|------------------|
| draft-pitch    | [establish register] | [strategic friction the pitch names] | [R-NN] |
| draft-spec     | [ground register]    | [technical friction the spec closes] | [R-NN] |
| draft-proposal | [amplify register]   | [business friction the proposal quantifies] | [R-NN] |

**SCOUT TRACEABILITY TABLE**

| Req-ID | Scout-Requirements Friction | Source Artifact | Must-have criterion |
|--------|-----------------------------|-----------------|---------------------|
| R-01   | [friction] | [source] | [must-have for spec] |
| R-02   | [friction] | [source] | [must-have for spec] |
| R-03   | [friction] | [source] | [must-have for spec] |

Req-IDs are declared here and pre-named in the TRACEABILITY AUDIT.

---

### OPEN

Frame the campaign. State that the pitch is produced first — not as a summary of the spec, but as the conviction baseline. The spec and proposal are evidence for the pitch's claim.

---

### DRAFT-PITCH *(first)*

Executive pitch for $TOPIC. Produced first to establish the conviction register before any technical constraints are introduced.

**Sections**: The Moment | The Gap | The Feature | The Signal | The Ask

After producing the pitch, record a **Conviction checkpoint** — one sentence stating the conviction register it establishes. This checkpoint is the baseline against which the spec and proposal are evaluated in CLOSE.

> **Conviction checkpoint**: The pitch establishes [conviction type] for [audience] by naming [status-quo friction] as the displacement trigger.

---

### DRAFT-SPEC *(second)*

Technical specification for $TOPIC. The spec must sustain the conviction register declared in the pitch's Conviction checkpoint.

**Sections**: Overview | Requirements | Design | Constraints | Open Questions

Requirements: one subsection per Req-ID, labeled **R-NN: [friction source name]**. Each requirement section includes one sentence connecting the technical requirement to the conviction register from the pitch.

---

### DRAFT-PROPOSAL *(third)*

Business proposal for $TOPIC. The proposal amplifies the conviction established in the pitch and grounded in the spec.

**Sections**: Problem | Solution | Value | Risk | Ask

Value: cite at least one Req-ID and name the conviction register from the pitch checkpoint as the business signal. Risk: state how long users remain on the status-quo if the feature does not ship.

---

### CLOSE

**CONVICTION GAP DIAGNOSIS**

The pitch established the conviction register. For each gap where the spec or proposal weakens it:

> In [artifact] / [sub-section]: the register found is [observed]. The pitch checkpoint declared [target register]. Gap: [scout sub-skill] evidence needed: [specific].

The pitch itself is the register baseline — gaps are measured against the pitch's conviction, not against a theoretical declaration. Include at least one observation per artifact.

---

### REFLECTION

**CONVICTION DELTA**

Structural table. One row per artifact — rows are pre-declared from the INERTIA MODEL MAP in SETUP. The Amplification chain cell carries a pre-defined template; fill it completely.

| Version        | Conviction established | Grounding Req-ID(s) | Amplification chain |
|----------------|------------------------|---------------------|---------------------|
| draft-pitch    | [from INERTIA MODEL MAP] | [R-NN]            | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |
| draft-spec     | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |
| draft-proposal | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |

**Columns**: Version | Conviction established | Grounding Req-ID(s) | Amplification chain  
**Cell template (Amplification chain)**: `[Req-ID]'s [specific factual claim] is made visceral by [emotional register]` — three components required.

---

**TRACEABILITY AUDIT**

Pre-named rows from the SETUP SCOUT TRACEABILITY TABLE. One row per Req-ID. Scout-Requirements Friction is sourced from the SETUP table, pre-populated before the audit runs. Row count must equal the SETUP table row count.

| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| R-01   | [friction from SETUP R-01 — pre-populated] | Y / N | [exact phrase from spec, or blank if N] | [gap if N] | scout-requirements |
| R-02   | [friction from SETUP R-02 — pre-populated] | Y / N | [exact phrase from spec, or blank if N] | [gap if N] | scout-requirements |
| R-03   | [friction from SETUP R-03 — pre-populated] | Y / N | [exact phrase from spec, or blank if N] | [gap if N] | scout-positioning  |

**AUDIT DIRECTIVE**: Each Req-ID row is pre-named from the SETUP SCOUT TRACEABILITY TABLE. Scout-Requirements Friction is pre-populated from that table — not written at audit time. Row count must match the SETUP table. A missing Req-ID row is a named-entry absence (e.g., "R-02 absent"), not a count difference.

---

*END OF CAMPAIGN*

---

---

## V-05 — Combination: Full C-39 Chain + Expanded REFLECTION Lifecycle

**Variation axes (combined)**: Complete three-table chain (C-39) + lifecycle emphasis redistribution (expanded REFLECTION)  
**Hypothesis**: Maximum structural enforcement at all three conviction phases, combined with an expanded REFLECTION that adds an explicit CONVICTION SCORE and a CLOSE-OUT directive, makes conviction completeness self-auditing. The REFLECTION is the weight-bearing phase; expanding it tests whether additional lifecycle depth changes artifact quality independent of the structural tables. Targets 233 via a different structural shape than V-02.

---

You are running **campaign-blueprint** for: **$TOPIC**

Produce draft-spec, draft-proposal, and draft-pitch in sequence. REFLECTION is the weight-bearing phase of this campaign. It carries three structural enforcement tables and closes every open thread from CLOSE.

---

### CAMPAIGN SETUP

**Feature**: $TOPIC  
**Status-quo competitor**: Name it. State the one friction it produces that $TOPIC eliminates.  
**Conviction register**: Choose one (urgency / confidence / relief / momentum). State the specific user population it targets and what switching cost drives the register.

**INERTIA MODEL MAP**

Pre-declare conviction type, status-quo friction, and Req-ID grounding for each artifact before any artifact is produced. The CONVICTION DELTA table in REFLECTION is built directly from this map.

| Version        | Conviction type | Status-quo friction addressed | Req-ID grounding |
|----------------|-----------------|-------------------------------|------------------|
| draft-spec     | [conviction type] | [technical friction]        | [R-NN]           |
| draft-proposal | [conviction type] | [business friction]         | [R-NN]           |
| draft-pitch    | [conviction type] | [strategic friction]        | [R-NN]           |

**SCOUT TRACEABILITY TABLE**

| Req-ID | Scout-Requirements Friction | Source Artifact | Must-have criterion |
|--------|-----------------------------|-----------------|---------------------|
| R-01   | [specific friction] | [source] | [must-have for spec] |
| R-02   | [specific friction] | [source] | [must-have for spec] |
| R-03   | [specific friction] | [source] | [must-have for spec] |

All Req-IDs are declared before artifact production begins. The INERTIA MODEL MAP references these Req-IDs. The TRACEABILITY AUDIT in REFLECTION pre-names these Req-IDs.

---

### OPEN

One paragraph. Name the status-quo competitor. State the conviction register and its target user population. State that REFLECTION is the closing authority — conviction gaps from CLOSE are resolved or named open in REFLECTION's CLOSE-OUT section.

---

### DRAFT-SPEC

Technical specification for $TOPIC.

**Sections**: Overview | Requirements | Design | Constraints | Open Questions

Requirements: one subsection per Req-ID, labeled **R-NN: [friction source name]**.

---

### DRAFT-PROPOSAL

Business proposal for $TOPIC.

**Sections**: Problem | Solution | Value | Risk | Ask

Problem: name the status-quo competitor. Value: cite Req-IDs. Risk: quantify duration of status-quo exposure if feature does not ship.

---

### DRAFT-PITCH

Executive pitch for $TOPIC.

**Sections**: The Moment | The Gap | The Feature | The Signal | The Ask

Signal: invoke the conviction register by name. Gap: name the status-quo competitor.

---

### CLOSE

**CONVICTION GAP DIAGNOSIS**

Structural table. Pre-declare three rows — one per artifact. A row with blank Evidence needed is a structural gap.

| Artifact       | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
|----------------|----------------------------------|----------------|-------------------|-----------------|-----------------|
| draft-spec     | [sub-section name] | [observed register] | [declared register] | [scout-requirements / scout-positioning / etc.] | [specific evidence] |
| draft-proposal | [sub-section name] | [observed register] | [declared register] | [scout sub-skill]     | [specific evidence] |
| draft-pitch    | [sub-section name] | [observed register] | [declared register] | [scout sub-skill]     | [specific evidence] |

**Columns**: Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed

---

### REFLECTION

REFLECTION carries three structural tables and one scoring table. It is the only place conviction completeness is verified — not CLOSE, not the artifact sections.

---

**CONVICTION DELTA**

Structural table. One row per artifact — rows are pre-declared from the INERTIA MODEL MAP in SETUP. The Amplification chain cell carries a pre-defined template; fill all three components or the cell is structurally incomplete.

| Version        | Conviction established | Grounding Req-ID(s) | Amplification chain |
|----------------|------------------------|---------------------|---------------------|
| draft-spec     | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |
| draft-proposal | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |
| draft-pitch    | [from INERTIA MODEL MAP] | [R-NN, R-NN]      | [Req-ID]'s [specific factual claim] is made visceral by [emotional register mechanism] |

**Columns**: Version | Conviction established | Grounding Req-ID(s) | Amplification chain  
**Cell template (Amplification chain)**: `[Req-ID]'s [specific factual claim] is made visceral by [emotional register]` — three components required; no paraphrase accepted.

---

**TRACEABILITY AUDIT**

Structural table. Pre-named rows from the SETUP SCOUT TRACEABILITY TABLE — one row per Req-ID declared in SETUP. Scout-Requirements Friction is pre-populated from that table, not written at audit time. Row count must equal the SETUP table row count. A missing row is a named-identifier absence.

| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| R-01   | [pre-populated from SETUP R-01] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-requirements |
| R-02   | [pre-populated from SETUP R-02] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-requirements |
| R-03   | [pre-populated from SETUP R-03] | Y / N | [exact phrase from spec, or blank if N] | [gap description if N] | scout-positioning  |

**AUDIT DIRECTIVE**: Each row is pre-named with its SETUP-sourced Req-ID. Scout-Requirements Friction is sourced from the SETUP SCOUT TRACEABILITY TABLE — pre-populated before the audit runs. Row count must match that table. A missing Req-ID row is a named-entry absence (e.g., "R-02 is absent") — not a count shortfall requiring external comparison.

---

**CONVICTION SCORE**

After completing the CONVICTION DELTA and TRACEABILITY AUDIT, score each artifact's conviction output. One row per artifact.

| Artifact       | Conviction type | Register match (Y/N) | Req-ID grounding (Y/N) | Amplification complete (Y/N) | Score (0–3) |
|----------------|----------------|----------------------|------------------------|------------------------------|-------------|
| draft-spec     | [type] | Y/N | Y/N | Y/N | [count of Y] |
| draft-proposal | [type] | Y/N | Y/N | Y/N | [count of Y] |
| draft-pitch    | [type] | Y/N | Y/N | Y/N | [count of Y] |

**Score interpretation**: 3 = conviction complete; 2 = minor gap, named; 1 = register mismatch; 0 = conviction absent. A campaign with all three artifacts at 3/3 has achieved full conviction closure.

---

**CLOSE-OUT**

One paragraph. State which gaps from CONVICTION GAP DIAGNOSIS (CLOSE) are resolved in this REFLECTION — name the specific Req-IDs or artifacts. State which remain open and name the scout sub-skill that would close each open gap. A CLOSE-OUT that names no open gaps must explain why the CONVICTION GAP DIAGNOSIS found no unresolvable friction.

---

*END OF CAMPAIGN*

---

---

## Variant Summary

| Variant | Axis | C-34 | C-35 | C-36 | C-37 | C-38 | C-39 | Notes |
|---------|------|------|------|------|------|------|------|-------|
| V-01 | C-38 isolation | NO | NO | FULL | NO | FULL | NO | Minimum C-38 footprint; prose CONVICTION DELTA and GAP DIAGNOSIS |
| V-02 | Full C-39 chain | FULL | FULL | FULL | FULL | FULL | FULL | 233 ceiling; pure structural-table axis, standard sequence |
| V-03 | Inertia framing | NO | NO | FULL | NO | NO | NO | Prominent status-quo competitor throughout; anonymous audit row |
| V-04 | Pitch-first + C-38 | FULL | NO | FULL | NO | FULL | NO | Sequence reorder; C-38 but no C-35; prose GAP DIAGNOSIS |
| V-05 | Full C-39 + expanded REFLECTION | FULL | FULL | FULL | FULL | FULL | FULL | 233 ceiling; adds CONVICTION SCORE and CLOSE-OUT to REFLECTION |

**R14 expected findings**: V-02 and V-05 independently reach 233 via distinct lifecycle shapes (standard vs. expanded REFLECTION). V-01 establishes the C-38-alone baseline. V-03 establishes the inertia-framing-alone baseline (no C-38). V-04 tests whether pitch-first sequence interacts with C-38 scoring at all. If V-03 scores unexpectedly high despite having no C-38, that indicates the rubric has a framing axis worth formalizing in v15.
