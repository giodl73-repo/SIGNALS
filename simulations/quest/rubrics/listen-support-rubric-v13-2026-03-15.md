Looking at the scorecard, the Round 12 excellence signals from V-05 that go beyond what C-33/C-34/C-35 already capture are:

1. **VALIDATION TRACE explicitly maps each declared checkpoint by name with YES/NO lines** — goes beyond C-17 (VALIDATION TRACE block present) and beyond C-34 (checkpoints pre-declared) by requiring the trace to echo back each checkpoint label with a binary probe.

2. **Per-criterion THRESHOLD CONFIRMATION sub-blocks** — each new criterion gets its own named block with 6+ verification lines including a scan-verifiability YES/NO, rather than a single monolithic THRESHOLD CONFIRMATION section.

3. **Cross-criterion synergy declared explicitly** — V-05's strongest distinction is calling out that C-33 tokens make C-34 checkpoints grep-detectable, so "completeness verifiable from preamble without traversal" is answerable YES structurally, not just aspirationally.

These become C-36 and C-37. Here is the complete updated rubric:

---

# listen-support Rubric v13
**Skill**: `listen:support`
**Version**: 13
**Date**: 2026-03-15
**Criteria count**: 37 (5 essential, 3 recommended, 29 aspirational)
**Changes from v12**: Added C-36 (Checkpoint-Mapped VALIDATION TRACE Expansion) and C-37 (Cross-Criterion Structural Synergy Declaration) from Round 12 excellence signals (V-05 strongest implementation).

---

## Essential Criteria (weight = 50 pts total, 10 pts each)

### C-01 -- Ticket Structural Completeness
- **Category**: correctness
- **Weight**: essential
- **Text**: Each predicted ticket contains all required structural fields: a title, a category (from the defined set), a severity level, a volume estimate, an assigned persona, and a sample body. Missing any of these fields in any ticket constitutes a structural failure for that ticket.
- **Pass condition**: All tickets in the predicted set contain all six required fields: title, category, severity, volume, persona, sample body. A ticket missing any required field fails this criterion for the full set -- the criterion requires the entire predicted ticket set to be structurally complete, not just a subset.

---

### C-02 -- Valid Category/Severity/Volume Values
- **Category**: correctness
- **Weight**: essential
- **Text**: Each ticket uses only values from the defined controlled vocabularies: category from `{how-to, bug, feature-request, config, integration}`, severity from `{P0, P1, P2, P3}`, volume from `{low, medium, high}`. Values outside these sets indicate unconstrained generation.
- **Pass condition**: Every ticket uses valid values from the controlled vocabulary sets for all three enumerated fields. Any invalid, missing, or invented value -- including synonyms not in the set (e.g., "critical" for P0) -- constitutes a failure.

---

### C-03 -- Persona Grounding from Stock Set
- **Category**: correctness
- **Weight**: essential
- **Text**: Each ticket is assigned to a persona from the defined stock persona set (SRE, PM, Developer, Support Engineer, Data Engineer, or equivalents named in the skill's persona registry). Invented personas, unlabeled entries, or role labels not in the stock set fail this criterion.
- **Pass condition**: All persona assignments match entries in the defined stock persona set. No invented or unlabeled personas appear in the ticket set. A set where any persona label cannot be traced to the stock registry fails.

---

### C-04 -- Gap Analysis Present and Typed
- **Category**: coverage
- **Weight**: essential
- **Text**: The output includes an explicit gap analysis section that addresses all three gap types: documentation gaps, design gaps, and operational gaps. Each type must have at least one entry.
- **Pass condition**: A section labeled (or clearly equivalent to) "Gap Analysis" exists with subsections or labeled entries for doc gaps, design gaps, and operational gaps, each containing at least one non-empty item.

---

### C-05 -- Ticket Set Covers Multiple Categories
- **Category**: coverage
- **Weight**: essential
- **Text**: The predicted ticket set spans at least three distinct categories from `{how-to, bug, feature-request, config, integration}`. A list that clusters entirely in one or two categories fails to represent the realistic support surface.
- **Pass condition**: Count of distinct category values used across all tickets >= 3.

---

## Recommended Criteria (weight = 30 pts total)

### C-06 -- Sample Body Written in Persona Voice
- **Category**: depth
- **Weight**: recommended
- **Text**: Each sample ticket body reads as if the assigned persona wrote it -- vocabulary, frustration level, and framing reflect that role's perspective. An SRE body sounds like an SRE; a PM body sounds like a PM.
- **Pass condition**: At least 75% of ticket bodies contain role-specific vocabulary, framing, or tone cues (e.g., SRE references runbooks or on-call; PM references roadmap). Generic boilerplate bodies that could belong to any persona fail this criterion.

---

### C-07 -- Calibrated Volume/Severity Distribution
- **Category**: depth
- **Weight**: recommended
- **Text**: The assignment of volume and severity values reflects realistic triage logic: not all tickets are high/P0. P0 tickets are rare; high-volume tickets tend to be how-to or config rather than bugs.
- **Pass condition**: At most one P0 ticket appears in the set. The volume distribution contains at least one "low" or "medium" entry. A set where every ticket is high/P0 fails this criterion.

---

### C-08 -- Gap Analysis Names Actionable Artifacts
- **Category**: depth
- **Weight**: recommended
- **Text**: Each gap entry specifies a concrete artifact or fix (e.g., "add troubleshooting section to getting-started guide", "add retry-budget config field to schema", "add /health endpoint for SRE monitoring") rather than generic statements ("improve docs", "fix bugs").
- **Pass condition**: At least 60% of gap entries name a specific artifact, section, field, endpoint, or design change. Vague entries like "better documentation" without a target artifact fail the per-entry test.

---

## Aspirational Criteria (weight = 10 pts total, normalized across 29 criteria)

Each full pass = 10/29 pts (~0.345). Each partial = 10/58 pts (~0.172). Max aspirational = 10 pts.

---

### C-09 -- Phase-Severity Gradient Prior
- **Category**: depth
- **Weight**: aspirational
- **Text**: The prompt encodes an explicit prior that severity correlates with adoption phase: early-phase tickets skew toward how-to/P2-P3; late-phase tickets include more integration/P0-P1. This prior shapes ticket generation rather than being a post-hoc annotation.
- **Pass condition**: A phase-severity gradient table or explicit phase-labeled constraint appears before ticket generation steps. Tickets assigned to early phases do not all carry P0/P1 severity.

---

### C-10 -- STATUS QUO ANCHOR Inertia Map
- **Category**: depth
- **Weight**: aspirational
- **Text**: The prompt includes a STATUS QUO ANCHOR block that maps the incumbent tool or behavior to the current user assumption being overridden. This inertia map drives assumption audit entries rather than leaving them to unconstrained inference.
- **Pass condition**: A named block (or equivalent) labeled STATUS QUO ANCHOR appears and contains at least one tool/behavior-to-assumption mapping that is referenced downstream in the assumption audit.

---

### C-11 -- Assumption Audit 6-Column Chain with SRE-First
- **Category**: depth
- **Weight**: aspirational
- **Text**: The assumption audit table uses a six-column structure (persona, prior behavior, assumed design, actual design, delta, ticket trigger) and lists SRE as the first row, establishing the operational failure mode before PM and Developer rows.
- **Pass condition**: Assumption audit table has >= 6 columns matching the required schema. SRE row appears before PM and Developer rows. Any 5-column or 4-column audit fails; any ordering that does not lead with SRE fails.

---

### C-12 -- Voice Register Density >= 2 Dimensions Per Body
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each sample ticket body exhibits at least two distinct voice register dimensions simultaneously (e.g., vocabulary + frustration level, or framing + urgency cue). Single-dimension bodies that rely on job title alone to signal persona fail this criterion.
- **Pass condition**: At least 75% of ticket bodies contain two or more identifiable voice register signals (role-specific vocabulary, urgency/frustration framing, tool-reference pattern, escalation language, or metric-grounding).

---

### C-13 -- Phase Distribution Target with Narrative Consistency
- **Category**: coverage
- **Weight**: aspirational
- **Text**: The prompt specifies a target distribution of tickets across adoption phases (e.g., 40% early, 40% mid, 20% late) and enforces that the ticket narrative across phases is consistent: a late-phase integration ticket presupposes resolution of the early-phase how-to tickets.
- **Pass condition**: A phase distribution target appears in the prompt. The ticket set contains entries in at least two distinct phases. No late-phase ticket describes a problem that contradicts a resolved early-phase assumption.

---

### C-14 -- Gap Classification PARITY/NET-NEW
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each gap entry is classified as either PARITY (gap exists in the incumbent tool's doc/design too) or NET-NEW (gap is unique to the new design). This classification prevents conflating inherited doc debt with new design omissions.
- **Pass condition**: At least one gap entry carries a PARITY label and at least one carries a NET-NEW label. Gap entries without classification fail the per-entry test; a set with no PARITY entries fails because all gaps cannot be NET-NEW.

---

### C-15 -- FORWARD-LINK GATE
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt contains a FORWARD-LINK GATE block that verifies each gap entry is referenced by at least one predicted ticket. Orphaned gap entries (gaps with no corresponding ticket) indicate structural incompleteness.
- **Pass condition**: A named FORWARD-LINK GATE block or equivalent exists and explicitly checks that every gap entry maps to at least one ticket. The gate must block or flag orphaned gap entries before output is finalized.

---

### C-16 -- Voice Marker Citation Format "Voice markers:"
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each sample ticket body is followed by (or contains inline) a "Voice markers:" citation listing the specific words or phrases that anchor the persona voice judgment. This makes the voice claim auditable rather than implicit.
- **Pass condition**: At least 75% of ticket bodies include a "Voice markers:" citation with at least two quoted or named markers. Bodies without a "Voice markers:" line fail the per-body test.

---

### C-17 -- VALIDATION TRACE Pre-Generation Block
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt includes a VALIDATION TRACE block that runs before ticket generation begins, verifying structural preconditions (category count, persona stock set, severity floor/ceiling, gap type coverage) rather than validating after the fact.
- **Pass condition**: A named VALIDATION TRACE block appears before the first ticket generation step. The block checks at minimum: distinct category count >= 3, all personas in stock set, P0 count <= 1, gap types (doc/design/ops) each >= 1.

---

### C-18 -- Phase-Labeled Constraint Floor
- **Category**: depth
- **Weight**: aspirational
- **Text**: The prompt specifies a minimum ticket count per adoption phase as a hard floor, not a target. The floor ensures no phase is skipped entirely, which would leave the support surface for that phase unpredicted.
- **Pass condition**: At least two phases carry an explicit minimum ticket count >= 1. Phases with no floor constraint fail this criterion. A single undifferentiated "generate N tickets" instruction with no phase floors fails.

---

### C-19 -- TIER-SEQUENCING RULE Preamble
- **Category**: depth
- **Weight**: aspirational
- **Text**: The prompt opens with a TIER-SEQUENCING RULE block that declares the processing order (e.g., TIER 1: assumption audit → TIER 2: ticket generation → TIER 3: gap analysis) before any content steps. This makes the generation pipeline inspectable from the preamble alone.
- **Pass condition**: A named TIER-SEQUENCING RULE block appears in the preamble (before Step 1) and names at least three tiers with their corresponding step ranges or functions.

---

### C-20 -- Per-Pair BIDIRECTIONAL LINKAGE with TIER 1/TIER 2
- **Category**: correctness
- **Weight**: aspirational
- **Text**: For each assumption audit row (TIER 1), there is a corresponding ticket (TIER 2) that references the same persona and delta. The linkage is explicit (ticket ID cites assumption row or vice versa), not inferred from thematic similarity.
- **Pass condition**: At least 50% of assumption audit rows have an explicit bidirectional link to a ticket. Unlinked audit rows that do not generate a ticket and unlinked tickets that do not trace to an audit row both fail the per-pair test.

---

### C-21 -- REJECTION REGISTRY with Dual-Category
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt maintains a REJECTION REGISTRY that tracks rejected ticket candidates with a dual-category label: the rejection reason (e.g., out-of-scope, duplicate, invalid-vocab) and the category the ticket would have occupied. This prevents silent category suppression.
- **Pass condition**: A named REJECTION REGISTRY block or table exists. Each entry carries both a rejection-reason label and a would-be category label. A registry with single-category labels (rejection reason only) fails.

---

### C-22 -- Floor Guarantee Arithmetic
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt includes an arithmetic check that verifies the minimum ticket count commitments (per-phase floors × phase count) do not exceed the total ticket budget, and that the budget is sufficient to meet all floors. This prevents contradictory constraints.
- **Pass condition**: An explicit arithmetic check or formula appears that computes total floor commitments and compares against the ticket budget. A prompt with floors that sum to more than the budget without an override rule fails.

---

### C-23 -- TIER ARCHITECTURE SELF-CHECK Table
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt includes a TIER ARCHITECTURE SELF-CHECK table that lists each tier, its input, its output, and its gate condition (what must be true before proceeding to the next tier). This makes the pipeline's progression rules explicit.
- **Pass condition**: A named TIER ARCHITECTURE SELF-CHECK table exists with columns for tier name/number, input artifact, output artifact, and gate condition. A table missing any column fails.

---

### C-24 -- Per-Category Minimum Commitment
- **Category**: coverage
- **Weight**: aspirational
- **Text**: The prompt specifies a minimum ticket count per category from the controlled vocabulary. This prevents a model from satisfying C-05 (3 distinct categories) by assigning one token ticket to minority categories while clustering the majority elsewhere.
- **Pass condition**: At least three categories carry an explicit minimum count >= 1. A prompt that only specifies a total ticket count without per-category floors fails.

---

### C-25 -- REGISTRY GATE Named Block
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt contains a REGISTRY GATE block that must be passed before ticket bodies are written. The gate verifies that the REJECTION REGISTRY is consistent with the ticket set (no accepted ticket appears in the registry; no registry entry maps to an accepted ticket).
- **Pass condition**: A named REGISTRY GATE block appears between the rejection step and the ticket body writing step. The gate condition explicitly checks registry/ticket-set consistency.

---

### C-26 -- REVISION GATE OPEN/CLOSED
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt includes a REVISION GATE with an explicit OPEN/CLOSED state that determines whether the model may revise an earlier tier before proceeding. The gate closes when all tier outputs are frozen; it opens if a downstream check fails and requires upstream correction.
- **Pass condition**: A named REVISION GATE block with an explicit OPEN/CLOSED state appears. The gate conditions for opening and closing are named. A prompt with only a monolithic "revise if needed" instruction without a named gate state fails.

---

### C-27 -- Per-Pair Content Alignment Evidence with Gate: PROCEED/REVISE
- **Category**: correctness
- **Weight**: aspirational
- **Text**: For each assumption audit / ticket pair (per C-20), the prompt requires an explicit content alignment check with a binary Gate: PROCEED or Gate: REVISE verdict. This makes tier-crossing decisions inspectable.
- **Pass condition**: At least 50% of audit/ticket pairs carry an explicit Gate: PROCEED or Gate: REVISE line. Pairs with implicit alignment (no gate verdict) fail the per-pair test.

---

### C-28 -- PHASE NARRATIVE Behavioral Driver Block
- **Category**: depth
- **Weight**: aspirational
- **Text**: The prompt includes a PHASE NARRATIVE block that describes the behavioral driver for each adoption phase (what the user is trying to accomplish, not just what phase they are in). This prevents phase labels from being decorative rather than generative.
- **Pass condition**: A named PHASE NARRATIVE block appears with at least two phase entries, each containing a behavioral driver statement (verb phrase describing user intent, not a phase name synonym).

---

### C-29 -- Phase Narrative Self-Check Block
- **Category**: correctness
- **Weight**: aspirational
- **Text**: After ticket generation, the prompt requires a phase narrative self-check that verifies each ticket's sample body is consistent with the behavioral driver declared for its phase. Tickets that contradict the phase narrative are flagged.
- **Pass condition**: A named phase narrative self-check block appears after ticket generation. It references the PHASE NARRATIVE block declared in C-28 and checks narrative consistency per ticket. A self-check that does not reference the declared behavioral drivers fails.

---

### C-30 -- THRESHOLD CONFIRMATION Block
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt includes a THRESHOLD CONFIRMATION block that verifies all aspirational criteria targets have been met before the output is finalized. This block is distinct from the VALIDATION TRACE (C-17), which checks structural preconditions; THRESHOLD CONFIRMATION checks post-generation quality targets.
- **Pass condition**: A named THRESHOLD CONFIRMATION block appears after ticket generation and gap analysis. It references at least the criteria with quantitative thresholds (C-09, C-12, C-13, C-22, C-24). A block that only repeats the VALIDATION TRACE checks fails.

---

### C-31 -- INERTIA COMPETITOR Preamble Declaration + Propagation
- **Category**: depth
- **Weight**: aspirational
- **Text**: The preamble declares an INERTIA COMPETITOR -- the named incumbent tool or behavior that users are migrating from -- and this name propagates to the STATUS QUO ANCHOR (C-10), assumption audit column headers (C-11), and gap classification (C-14). Consistent propagation of the competitor name prevents assumption-audit entries from being generic.
- **Pass condition**: A named INERTIA COMPETITOR appears in the preamble. The same name (or a defined abbreviation) appears in at least three downstream structural positions: the STATUS QUO ANCHOR block, at least one assumption audit column header, and at least one gap classification entry.

---

### C-32 -- SRE-First Ordering Advisory + VALIDATION TRACE Check
- **Category**: depth
- **Weight**: aspirational
- **Text**: The prompt includes an explicit advisory that SRE tickets must be generated before PM and Developer tickets (not just ordered first in the audit per C-11), and the VALIDATION TRACE verifies this ordering in the output.
- **Pass condition**: An SRE-first ordering advisory appears in the ticket generation step instructions. The VALIDATION TRACE (C-17) contains an explicit check that the first ticket in the set is assigned to the SRE persona.

---

### C-33 -- Bound-Variable Bracket-Token Propagation
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The INERTIA COMPETITOR name is represented as a literal bracket-token (e.g., `[INERTIA COMPETITOR]`) and that exact token -- not a synonym, paraphrase, or prose substitution -- is embedded in at least three distinct structural positions: a Step 2 column header, a Step 3 column header, and at least one additional downstream structural location (step instruction clause, gap table column, or VALIDATION TRACE check). Bracket-token embedding makes propagation verifiable by grep without prose interpretation.
- **Pass condition**: The literal bracket-token `[INERTIA COMPETITOR]` (or the declared bound-variable form) appears verbatim in >= 3 distinct table-header or step-label positions. VALIDATION TRACE contains a bracket-scan check that explicitly names the token and the locations being scanned. Variations that substitute synonyms ("STATUS QUO behavior", "incumbent behavior") in column headers without the literal bracket-token fail.

---

### C-34 -- Propagation Chain Pre-Declaration
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The preamble contains a named PROPAGATION CHAIN block that pre-declares all checkpoints where the bound variable (C-33 bracket-token) must appear, each labeled (Checkpoint A, B, C, …) with its structural location (e.g., "Checkpoint A: Step 2 column header"). This pre-declaration makes completeness verifiable from the preamble alone without traversing all steps.
- **Pass condition**: A named PROPAGATION CHAIN block appears in the preamble before Step 1. It declares >= 3 labeled checkpoints, each with a named structural location. VALIDATION TRACE references the declared checkpoints by label when checking propagation. A prompt where checkpoints can only be discovered by reading all steps fails.

---

### C-35 -- SRE-Write-First Enforcement Gate
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The prompt includes a named SRE-WRITE-FIRST gate that must be passed before any non-SRE ticket body is written. The gate verifies that the SRE ticket body is complete and passes the voice register check (C-12) before the model proceeds to PM or Developer bodies. This prevents the SRE ordering advisory (C-32) from being satisfied by label placement alone while the body remains generic.
- **Pass condition**: A named SRE-WRITE-FIRST gate or equivalent enforcement block appears between the SRE ticket body and the first non-SRE ticket body instruction. The gate condition references voice register density (>= 2 dimensions) for the SRE body. A prompt where the SRE-first instruction is advisory only (no gate) fails.

---

### C-36 -- Checkpoint-Mapped VALIDATION TRACE Expansion
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The VALIDATION TRACE block (C-17) is expanded to echo back each preamble-declared propagation checkpoint (from C-34) by label, with a binary YES/NO probe per checkpoint naming the structural location being verified (e.g., "Checkpoint A — Step 2 header contains `[INERTIA COMPETITOR]`: YES/NO"). This makes the VALIDATION TRACE a direct verification of the pre-declaration contract, not a general structural check. The number of named checkpoint-probe lines in VALIDATION TRACE must equal the number of declared checkpoints.
- **Pass condition**: VALIDATION TRACE contains one named per-checkpoint probe line for each checkpoint declared in the PROPAGATION CHAIN block (C-34). Each probe line names the checkpoint label, the structural location, and the token being scanned, with an explicit YES/NO resolution. A VALIDATION TRACE that asserts "propagation chain complete" without per-checkpoint lines fails. A VALIDATION TRACE with fewer probe lines than declared checkpoints fails.

---

### C-37 -- Cross-Criterion Structural Synergy Declaration
- **Category**: depth
- **Weight**: aspirational
- **Text**: The THRESHOLD CONFIRMATION block (C-30) contains a named per-criterion sub-block for each new aspirational criterion introduced in the current rubric version, and at least one sub-block explicitly declares a cross-criterion synergy: specifically, that bracket-token embedding (C-33) makes propagation chain checkpoints (C-34) grep-detectable, so that preamble-level completeness verification (C-34) is answerable as scan-verifiable rather than requiring step traversal. The sub-block must include a "Completeness verifiable from preamble without traversal: YES/NO" line and a "Detectable by bracket-scan without prose interpretation: YES/NO" line, both answerable YES structurally.
- **Pass condition**: THRESHOLD CONFIRMATION contains a named sub-block for each criterion added in the current rubric version. At least one sub-block contains both the "no traversal needed" line and the "bracket-scan detectable" line. The synergy between C-33 and C-34 is declared by name (not implied). A monolithic THRESHOLD CONFIRMATION block without per-criterion sub-blocks fails. A sub-block that includes only one of the two required lines fails.
