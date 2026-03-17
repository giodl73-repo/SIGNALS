# listen-support Rubric v12
**Skill**: `listen:support`
**Version**: 12
**Date**: 2026-03-15
**Criteria count**: 35 (5 essential, 3 recommended, 27 aspirational)
**Changes from v11**: Added C-33 (Bound-Variable Bracket-Token Propagation), C-34 (Propagation Chain Pre-Declaration), C-35 (SRE-Write-First Enforcement Gate) from Round 11 excellence signals.

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

## Aspirational Criteria (weight = 10 pts total, normalized across 27 criteria)

Each full pass = 10/27 pts (~0.370). Each partial = 10/54 pts (~0.185). Max aspirational = 10 pts.

### C-09 -- Non-Obvious Failure Mode Coverage
- **Category**: behavior
- **Weight**: aspirational
- **Text**: At least one predicted ticket surfaces a failure mode that would not appear in a basic happy-path walkthrough -- e.g., a race condition under high load, a config interaction with a neighboring system, a persona who misinterprets a default, or a missing signal during a partial-failure scenario.
- **Pass condition**: At least one ticket is classifiable as a non-obvious failure mode: the reviewer cannot derive it directly from reading the feature spec's happy path. Rationale or framing in the output makes the non-obvious nature clear.

---

### C-10 -- 90-Day Temporal Staging
- **Category**: depth
- **Weight**: aspirational
- **Text**: The output distinguishes or implies which tickets are likely to arrive in week 1-2 (first-impressions, setup friction) vs. week 4-8 (adoption edge cases) vs. week 8-12 (operational steady-state). This temporal dimension reveals when the support load peaks and when different roles engage.
- **Pass condition**: The output explicitly tags, groups, or annotates at least a subset of tickets with expected timing, or provides a narrative section describing the 90-day ticket arc. Outputs with zero temporal differentiation fail.

---

### C-11 -- Inline Validation Trace
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 1 excellence signal -- V-02, V-04, V-05 TABLE CHECK gate pattern
- **Text**: The output includes a visible validation trace -- a structured block that audits key invariants (distinct category count, P0 count, persona diversity, vocabulary compliance) and reports pass/fail before body prose is written. The trace makes correctness auditable by column-scan without reading full prose bodies.
- **Pass condition**: The output contains an explicit check block (table, list, or labeled section) that counts or verifies at least two of the following: distinct category count, P0/high-severity count, persona count, vocabulary compliance. The check must precede or be separable from the body-prose sections.
- **Anti-pattern**: A closing "self-check" paragraph that says "all fields are correct" without showing counts fails -- invisible checking is not the same as an auditable trace.

---

### C-12 -- Voice Register Density
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 1 excellence signal -- V-02 explicit per-persona voice register table; V-04/V-05 dual-mechanism voice priming
- **Text**: Ticket bodies deploy multiple role-specific vocabulary markers per body -- not just one cue. An SRE body with "runbook" alone is weaker than one with "runbook", "on-call rotation", and "SLO breach". Extends C-06's 75% floor into a richness requirement.
- **Pass condition**: At least 60% of ticket bodies deploy >= 2 distinct role-vocabulary markers appropriate to the persona. Markers must belong to different vocabulary register dimensions (operational vocabulary, frustration register, framing conventions) -- repeating the same noun twice does not count as two markers.
- **Anti-pattern**: Bodies that identify the persona by name or role label in the opening sentence ("As an SRE, I am seeing...") but then use generic language for the remainder fail the density test -- persona declaration is not persona voice.

---

### C-13 -- Phase-Severity Semantic Binding
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 1 excellence signal -- V-03 phase severity priors ("Phase 1: typical severity P2/P3"); V-05 three-mechanism convergence including phase severity guidance
- **Text**: When temporal phases are present (C-10 pass required), each phase carries an explicit severity prior that creates a principled gradient -- early phases yield P2/P3 tickets, late phases yield P0/P1 escalations. This binding makes the 90-day arc predictive of support load trajectory, not just ticket timing.
- **Pass condition**: C-10 must pass. Additionally, severity values assigned to tickets must correlate with phase in a principled direction: early-phase tickets average lower severity than late-phase tickets, OR the output explicitly states severity priors per phase.
- **Anti-pattern**: Labeling tickets with phases but assigning severity independently of phase fails -- phase labels without severity semantics are decorative, not predictive.
- **Dependency**: Only scoreable if C-10 passes. If C-10 fails, C-13 scores 0 regardless of other quality signals.

---

### C-14 -- Competitive Gap Classification
- **Category**: coverage
- **Weight**: aspirational
- **Source**: Round 2 excellence signal -- V-02, V-04 PARITY/NET-NEW tagging pattern
- **Text**: Each gap entry is classified as PARITY (the incumbent or competitor already provides this -- closing it is table stakes) or NET-NEW (the feature uniquely offers this, representing differentiation). Classification adds strategic signal beyond artifact naming (C-08): teams can distinguish which gaps they must close to reach parity vs. which represent competitive advantage.
- **Pass condition**: At least 60% of gap entries carry an explicit parity/net-new classification or equivalent label. The classification must be applied per-entry, not summarized in a preamble paragraph.
- **Anti-pattern**: A generic note at the top of the gap section ("most gaps are parity") without per-entry classification fails -- aggregate framing is not per-entry signal.

---

### C-15 -- Violated-Assumption Anchor
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 2 excellence signal -- V-02, V-04 inertia map with "violated assumption" column; structural mechanism that produces C-09 PASS reliably
- **Text**: The output includes an explicit competitor/inertia mapping step -- a structured artifact that identifies at least one user assumption imported from an incumbent tool that the new feature violates or reframes. C-09 tests the output result; C-15 tests whether the reasoning mechanism is visible and reproducible.
- **Pass condition**: The output contains a structured block that names at least one incumbent-tool assumption and pairs it with the violated expectation -- e.g., "Users expect X because incumbent does Y; this feature does Z instead, causing W." A violated assumption can appear inline in a ticket's body framing only if it is explicitly labeled as such.
- **Anti-pattern**: C-09 passing alone does not satisfy C-15. The violated-assumption framing must be visible as a named analytical step, not inferred from ticket content.
- **Relationship to C-09**: C-09 and C-15 score independently. C-09 rewards the output result; C-15 rewards the structural mechanism.

---

### C-16 -- Voice Marker Citation
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 2 excellence signal -- V-03 "Markers deployed: [list]" inline citation pattern; mechanism that lifts V-03 to C-12 PASS while V-01/V-02/V-04 remain PARTIAL
- **Text**: Beyond deploying voice markers (C-06) and deploying multiple markers (C-12), the output cites which specific markers it deployed for each ticket body -- either as an inline annotation or per-body footnote. Citation makes voice register auditable by inspection rather than dependent on reviewer recognition.
- **Pass condition**: At least 60% of ticket bodies include an explicit marker citation naming two or more deployed vocabulary items. The citation must name the markers, not merely count them ("2 markers deployed" does not pass; "Markers: runbook, on-call rotation" does).
- **Anti-pattern**: Describing the voice strategy in a preamble section without per-body citation fails -- strategy declaration is not output verification.
- **Relationship to C-12**: C-12 requires >= 2 markers to be present; C-16 requires them to be cited. Both score independently.

---

### C-17 -- Assumption Chain Ticket Forward-Link
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 3 excellence signal -- V-02 6-column assumption audit chain with Ticket ID as terminal column; the structural mechanism that makes C-15 bidirectionally verifiable
- **Text**: The violated-assumption anchor (C-15) maps each assumption to the ticket it produced. C-15 requires the reasoning mechanism to be visible as a named analytical step; C-17 requires the chain to close: each assumption entry explicitly names the Ticket ID it generated. The forward-link transforms a one-way analytical map into an auditable trail -- a reviewer can verify that every non-obvious ticket (C-09 candidate) has a corresponding assumption entry, and every assumption entry has a ticket. Without the link, the chain is an assertion; with it, it is a verifiable mapping.
- **Pass condition**: The assumption audit block includes Ticket ID as an explicit column or field for each assumption entry. At least one assumption-to-ticket link is verifiable in both directions: the assumption entry names the ticket, and the ticket body references the violated expectation or incumbent behavior. A chain that ends at "failure mode" without naming the ticket fails.
- **Anti-pattern**: An assumption map that lists failure modes as prose without connecting each failure to a specific ticket ID leaves the chain unverifiable. Naming a ticket category (e.g., "produces a bug ticket") without a specific ID does not satisfy the forward-link requirement.
- **Dependency**: Only scoreable if C-15 passes. If C-15 fails, C-17 scores 0.

---

### C-18 -- Column-Label Marker Attribution
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 3 excellence signal -- V-03 `operational=X | frustration=Y | framing=Z` format; structural advancement over R2 flat-list citation that makes same-register repetition self-detecting
- **Text**: Voice marker citations (C-16) are prefixed with a register-dimension label (e.g., `operational=runbook`, `frustration=SLO breach`, `framing=roadmap impact`). Column-label attribution makes two structural properties self-enforcing: (a) every marker is classified by register dimension at citation time, and (b) two citations carrying the same dimension prefix are immediately visible -- defeating attempts to satisfy C-12's "different register dimensions" requirement by listing two markers from the same register. Without dimension labels, marker diversity is reviewer-dependent; with labels, it is structurally verifiable.
- **Pass condition**: At least 60% of ticket body marker citations use column-label prefix format. Labels must name a recognizable register dimension (operational, frustration, framing, escalation, scope, or equivalent). Generic labels ("type1=", "voice1=") do not pass. A flat list without dimension prefixes ("Markers: runbook, on-call rotation") satisfies C-16 but fails C-18.
- **Anti-pattern**: Naming markers without dimension labels, even if two or more markers are named, fails because dimension classification is absent -- the reviewer cannot confirm two markers span different register dimensions without reading the vocabulary.
- **Dependency**: Only scoreable if C-16 passes. If C-16 fails, C-18 scores 0.

---

### C-19 -- Post-Generation Threshold Confirmation
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 3 excellence signal -- V-01 GAP CLASSIFICATION COVERAGE confirmation block (checks C-14 >= 60%); V-03 MARKER CITATION AUDIT confirmation block (checks C-16 >= 60%); post-generation complement to C-11's pre-generation trace
- **Text**: Criteria C-14 and C-16 both specify >= 60% thresholds that are difficult to verify by reading prose alone. A post-generation confirmation block explicitly counts threshold-governed items and reports pass/fail per criterion -- e.g., "Gap entries classified: 8 of 12 = 67% >= 60%: PASS". This extends C-11's pre-generation invariant trace into the post-generation phase: C-11 validates structural preconditions before body prose; C-19 validates percentage thresholds after output is complete. The two are non-overlapping: C-11 catches structural problems before they propagate; C-19 confirms coverage compliance after they are measurable.
- **Pass condition**: The output includes a structured block appearing after the main generated content that explicitly counts and confirms at least two percentage-threshold criteria (from: C-14 gap classification coverage, C-16 marker citation coverage, C-12 voice density). Each confirmation entry must show the raw count, denominator, and percentage -- not just a PASS declaration. A pre-generation note stating "I will aim for 60%" does not pass; the block must audit actual output.
- **Anti-pattern**: A pre-generation validation trace (C-11 PASS) without a post-generation threshold audit leaves percentage compliance for C-14 and C-16 unverified. Stating a target threshold before generation is not equivalent to confirming it was met after generation.

---

### C-20 -- Bidirectional Linkage Verification
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 4 excellence signal -- V-01 BIDIRECTIONAL LINKAGE VERIFICATION block after body generation; post-body complement to C-17's forward-link that confirms the chain survived body writing
- **Text**: C-17 establishes the assumption-to-ticket forward-link at generation time; C-20 requires a post-body confirmation that the link held in both directions after body prose was written. The verification block checks: (a) every assumption row names a ticket -- forward direction, (b) every linked ticket body contains reference to the violated expectation or incumbent behavior named in the assumption entry -- reverse direction, and (c) the content of the ticket body is semantically aligned with the assumption framing, not merely co-located. Body generation can drift from the upstream assumption chain; the bidirectional verification detects that drift.
- **Pass condition**: The output contains a post-body verification block that explicitly checks both link directions and reports alignment: each assumption row is confirmed to name a ticket, and each named ticket is confirmed to reflect the violated assumption in its body. At minimum one assumption-ticket pair is verified with content alignment evidence (e.g., quoting the assumption phrase that appears in or motivates the ticket body). A forward-link block alone (C-17 passing) without post-body verification of the reverse direction and content alignment does not satisfy C-20.
- **Anti-pattern**: Generating the forward-link column in the assumption audit and then proceeding to body writing without a post-body check leaves drift undetected. A summary statement ("all tickets align with assumptions") without per-pair verification fails -- invisible checking is not an auditable reverse scan.
- **Dependency**: Only scoreable if C-17 passes. If C-17 fails, C-20 scores 0.

---

### C-21 -- Dimension-Label Rejection Registry
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 4 excellence signal -- V-02 STEP 6 four EXPLICIT REJECTIONS; the structural guard that distinguishes V-02's C-18 PASS from all other R4 variations' C-18 PARTIAL
- **Text**: C-18 requires marker citations to carry dimension-prefix labels; C-21 requires the output to include an explicit rejection registry -- a named list of marker forms that do not qualify for dimension-label credit. Without the registry, borderline markers (role declarations, generic verbs, same-register synonyms) can be self-reported as valid dimension labels; the reviewer must exercise judgment case-by-case. With the registry, the output commits to a rejection boundary before scoring, making C-18 compliance binary rather than judgment-dependent. The registry also closes the gap that allowed V-01, V-03, and V-04 to achieve C-18 PARTIAL: a format display without a rejection list cannot prevent same-dimension repetition from being misclassified as dimension diversity.
- **Pass condition**: The output contains an explicit rejection registry (labeled section or embedded list) that names at least three disqualifying marker forms or patterns. Qualifying rejection types include: role declarations used as markers ("as an SRE" does not count as an operational marker), generic verbs without register specificity ("noticed", "tried", "encountered"), same-register synonym pairs presented as cross-dimension diversity, and bare nouns without context-anchoring. The registry must appear before or alongside body generation so that the rejection boundary is established at citation time.
- **Anti-pattern**: Showing the dimension-label format (e.g., `operational=X | frustration=Y`) without specifying what fails to qualify leaves the format aspirational rather than enforced. V-01, V-03, and V-04 all showed the format and all scored C-18 PARTIAL for this reason -- format display is necessary but not sufficient.
- **Dependency**: Only scoreable if C-18 passes. If C-18 fails, C-21 scores 0.

---

### C-22 -- Mismatch-Triggered Revision Gate
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 5 excellence signal -- V-01 BIDIRECTIONAL LINKAGE VERIFICATION with mandatory revision on MISMATCH; the enforcement mechanism that converts per-pair verification from advisory to binding
- **Text**: C-20 requires a post-body bidirectional verification block with per-pair evidence; C-22 requires that the verification block include an explicit correction gate triggered by any MISMATCH result. Without the gate, the verification identifies drift but permits the output to proceed with a known misalignment -- the check is informational. With the gate, MISMATCH terminates the step and mandates a body revision before proceeding. The revision gate is what transforms the verification from a diagnostic into a quality enforcer: a MATCH/MISMATCH verdict that produces no consequence is structurally equivalent to no check.
- **Pass condition**: The bidirectional verification block includes an explicit gate statement that requires revision when any pair reports MISMATCH. The gate must specify the action (e.g., "revise body before proceeding", "correct and re-verify") -- a statement that merely notes MISMATCH without directing revision fails. At least one pair's evidence block demonstrates the gate structure (even if all pairs are MATCH at execution time, the gate text must be present and unambiguous).
- **Anti-pattern**: A per-pair evidence block that reports MATCH/MISMATCH but contains no gate instruction reduces C-20 to auditing without enforcement -- the reviewer learns about drift but the process does not correct it. A bidirectional check that reaches MISMATCH and does not halt is a structural failure of the same class as invisible checking, one tier up.
- **Dependency**: Only scoreable if C-20 passes. If C-20 fails, C-22 scores 0.

---

### C-23 -- Dual-Category Rejection Structure
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 5 excellence signal -- V-02 STEP 5b seven-entry registry with Category 1 (format violations: R-01 through R-03) and Category 2 (value violations: R-04 role declarations, R-05 generic verbs, R-06 same-register synonyms, R-07 bare nouns); the structural property that distinguishes a complete rejection registry from a partial one
- **Text**: C-21 requires an explicit rejection registry with at least three disqualifying marker forms; C-23 requires the registry to commit to both structural dimensions of rejection -- format violations (wrong or absent label structure) and value violations (marker content that fails semantic register requirements). A registry containing only format violations cannot prevent well-formatted but semantically vacuous markers from passing; a registry containing only value violations cannot enforce the prefix structure. Only a registry with named entries in both categories provides complete coverage: format compliance is necessary but not sufficient; value compliance is necessary but not sufficient; both together are necessary and sufficient. Without the dual-category structure the registry is incomplete regardless of entry count.
- **Pass condition**: The rejection registry contains at least one named entry in a format-violation category (e.g., labels absent, wrong separator format, generic label names like "type1=") AND at least one named entry in a value-violation category (e.g., role declarations, generic verbs, same-register synonyms, bare nouns). The two categories must be distinguishable -- either labeled explicitly ("Category 1: Format", "Category 2: Value") or structured so entries of each type are visibly separated. A flat list of entries that mixes format and value violations without category distinction fails because the registry's coverage of both dimensions is not self-evident.
- **Anti-pattern**: A registry that lists format-violation entries only (as V-01 R5 did) without any value-violation entries fails C-23 even if it satisfies C-21's three-entry minimum. The format-only registry prevents structural non-compliance but cannot detect the subtler failure where a marker carries the correct prefix label but names a value with no register specificity (e.g., `operational=noticed`). V-01's C-21 FAIL in R5 was caused precisely by this gap.
- **Dependency**: Only scoreable if C-21 passes. If C-21 fails, C-23 scores 0.

---

### C-24 -- Two-Tier Gate Architecture
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 6 excellence signal -- V-05 full synthesis combining V-01's per-pair `Gate: PROCEED|REVISE` with V-02's block-level `REVISION GATE / Gate status: OPEN|CLOSED`, plus an ordering constraint that makes the two tiers sequentially dependent
- **Text**: C-22 requires a per-pair gate that halts on MISMATCH and mandates body revision; C-24 requires a second gate tier at block level -- a `REVISION GATE` sub-block with an explicit `Gate status: OPEN | CLOSED` binary that aggregates all per-pair verdicts. The ordering constraint is the structural key: "Any pair showing REVISE: halt -- do not advance to REVISION GATE or Step 8 until all per-pair gates show PROCEED." This constraint makes the two tiers sequentially enforcing rather than parallel: the block-level gate can only be reached when all per-pair gates are clear. Without sequential enforcement, a block-level gate that is reached before per-pair gates resolve carries no meaningful signal; with it, the block-level gate serves as a confirmed aggregate of per-pair compliance. The architecture provides structural redundancy -- per-pair granularity for detection, block-level finality for clearance.
- **Pass condition**: The output contains both a per-pair gate mechanism (C-22 pass condition met) AND a block-level `REVISION GATE` sub-block with a `Gate status: OPEN | CLOSED` or equivalent binary. The ordering constraint must be explicit: the gate text must state that per-pair gates must all resolve to PROCEED before the block-level gate is evaluated. A block-level gate without per-pair gates satisfies neither C-22 nor C-24. Per-pair gates without a block-level aggregation gate satisfy C-22 but not C-24.
- **Anti-pattern**: Two gate checks at the same granularity (two per-pair checks, or two block-level checks) do not constitute a two-tier architecture -- tier distinction requires one check at pair level and one at block level, with an ordering rule between them. A block-level gate reached in parallel with (not after) per-pair gates is a concurrent check, not a sequential two-tier gate.
- **Dependency**: Only scoreable if C-22 passes. If C-22 fails, C-24 scores 0.

---

### C-25 -- Registry Completeness Self-Check
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 6 excellence signal -- V-03/V-04/V-05 REGISTRY COMPLETENESS CHECK pattern; the structural mechanism that transforms the rejection registry from a writer-asserted list into a self-verified artifact
- **Text**: C-23 requires the rejection registry to contain named entries in both format-violation and value-violation categories; C-25 requires the registry to embed a self-check block that counts its own entries per category and confirms the totals meet minimums. Without the self-check, the registry's completeness depends on the reviewer counting entries; with it, the output asserts its own compliance and makes the assertion auditable by inspection. The self-check is structurally analogous to C-19's role for percentage thresholds: C-19 confirms post-generation that bodies met the 60% floors; C-25 confirms at registry-write time that both rejection categories are populated to minimum thresholds. Both are self-verification mechanisms that shift correctness from reviewer-assessed to output-declared.
- **Pass condition**: The rejection registry includes an embedded or immediately following count block that explicitly tallies: (a) total entries in Category 1 (format violations) with a pass/fail against a stated minimum, and (b) total entries in Category 2 (value violations) with a pass/fail against a stated minimum. The self-check must name the counts explicitly -- a preamble statement ("I will include entries in both categories") does not pass; a post-registry block showing "Category 1: 3 entries -- PASS; Category 2: 4 entries -- PASS" does. The minimum thresholds cited in the self-check must match or exceed C-21's three-entry floor, established via an explicit total row naming the C-21 floor (e.g., "Total >= 3 -- C-21 floor").
- **Anti-pattern**: Describing the registry structure before writing it ("the registry will contain format and value entries") without a post-registry count block fails -- forward declaration is not self-verification. A registry that reaches the correct entry count through reviewer inference without an explicit self-count block satisfies C-23 but fails C-25. Stating per-category minimums without an explicit total cross-referencing C-21's floor is a PARTIAL: the cross-criterion tie is implicit rather than declared.
- **Dependency**: Only scoreable if C-23 passes. If C-23 fails, C-25 scores 0.

---

### C-26 -- Tier Architecture Self-Documentation
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 8 excellence signal -- V-03/V-04/V-05 TIER 1 / TIER 2 named headers plus `TIER-SEQUENCING RULE:` named field; structural advancement over R6 prose ordering constraint that makes the two-tier architecture verifiable by header scan rather than prose parsing
- **Text**: C-24 requires an explicit ordering constraint linking the two gate tiers -- the constraint that per-pair gates must all PROCEED before the block-level gate is evaluated. C-24's pass condition is satisfied by prose (e.g., "Any pair showing REVISE: halt -- do not advance to REVISION GATE..."). C-26 requires the two-tier architecture to additionally be structurally self-documenting: named tier headers (e.g., `-- TIER 1: Per-Pair Verification --` and `-- TIER 2: Block-Level Clearance --`) mark each tier boundary as a scannable landmark, and a named sequencing rule field (e.g., `TIER-SEQUENCING RULE:`) surfaces the ordering constraint as a discrete labeled element rather than embedded prose. With named headers and a named sequencing field, a scorer can confirm C-24 compliance by header scan alone -- no prose interpretation required. Without structural naming, the tier boundary and ordering rule are only findable by reading the full verification block. The advancement is analogous to C-16 -> C-18: C-16 requires markers named (flat list acceptable); C-18 requires markers dimension-labeled (structurally self-classifying). C-24 requires the constraint to exist; C-26 requires the architecture to be structurally legible.
- **Pass condition**: The two-tier gate structure uses named tier headers that explicitly label each tier as a structural landmark (e.g., "TIER 1:" / "TIER 2:", "-- TIER 1 --" / "-- TIER 2 --", or equivalent section markers) AND includes a named sequencing rule field (e.g., `TIER-SEQUENCING RULE:`, `SEQUENCING CONSTRAINT:`, or equivalent) that states the ordering rule as a discrete labeled element. Scan-first accessibility is also required: a scorer must be able to confirm C-24 compliance by scanning the top of the verification block -- either by finding the TIER-SEQUENCING RULE field as the first element before any per-pair content, or by finding a TIER ARCHITECTURE SELF-CHECK gate block that aggregates all three landmarks (named TIER 1 header, named TIER 2 header, and named TIER-SEQUENCING RULE field) into a single scannable confirmation. The tier headers must be present in the output itself, not only described in a preamble. A prose ordering constraint embedded within verification text without structural tier headers satisfies C-24 but fails C-26.
- **Anti-pattern**: A two-tier gate where the tier boundary is implicit (the per-pair section simply ends and a block-level section begins without a named header) fails even if the ordering constraint prose is present -- the architecture cannot be confirmed by header scan alone. A TIER-SEQUENCING RULE field placed mid-block (after per-pair content has begun) without a compensating TIER ARCHITECTURE SELF-CHECK at the block top also fails the scan-first accessibility requirement: a scanner must read through per-pair evidence before reaching the sequencing rule. Naming the tiers in a preamble without labeled headers in the gate output itself also fails -- preamble declaration is not structural output labeling.
- **Dependency**: Only scoreable if C-24 passes. If C-24 fails, C-26 scores 0.

---

### C-27 -- Redundant-Granularity Floor Guarantee
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 8 excellence signal -- V-05 belt-and-suspenders pattern: per-category minimums of 2 each independently sum to 4 > C-21's floor of 3, so C-21 compliance is provable from per-category counts alone without computing the total row; contrasts with V-02 (per-category min=1, total row carries all load) which passes C-25 but provides no per-category-level guarantee
- **Text**: C-25 requires the self-check to include an explicit total row naming C-21's floor, shifting cross-criterion compliance from reviewer-computed to output-declared. C-27 requires the per-category minimums themselves to collectively guarantee C-21's floor -- so that compliance is independently verifiable at both the per-category level and the aggregate level, without either level needing to carry the full proof. With per-category minimums set high enough that their sum exceeds C-21's three-entry floor (e.g., 2 + 2 = 4 > 3), a reviewer can confirm C-21 compliance by reading only the per-category counts, and independently confirm it again via the total row. Neither level depends on the other -- the guarantee is redundant across granularities. With per-category minimums of 1 (V-02's pattern), the total row carries the entire floor guarantee: if the total row were absent or miscounted, C-21 compliance would be unverifiable from per-category counts alone (1 + 1 = 2 < 3). The redundant-granularity property ensures that no single verification level is load-bearing: the floor is provable at whichever granularity a reviewer checks first.
- **Pass condition**: The sum of the per-category minimums stated in the self-check exceeds C-21's three-entry floor (i.e., per-category min_1 + per-category min_2 > 3, which with two categories requires each per-category minimum >= 2). The explicit total row (required by C-25) must also be present and must cross-reference C-21's floor. Both conditions together produce the redundant guarantee: per-category floors provable independently, total floor confirmed by the cross-reference row. A self-check with per-category minimums of 1 and an explicit total row satisfies C-25 but fails C-27 -- the total row is load-bearing and the per-category counts alone do not prove C-21 compliance.
- **Anti-pattern**: Setting per-category minimums at 1 (or any value whose sum <= C-21's floor) means the self-check's only floor guarantee lives in the total row. If the total row names C-21's floor, C-25 passes; but C-27 fails because the per-category counts do not independently imply compliance. The anti-pattern creates a single-point-of-verification architecture -- the same structural weakness that C-24 addressed for gate architecture by adding a second tier, and that C-20 addressed for assumption chains by adding a post-body verification step.
- **Dependency**: Only scoreable if C-25 passes. If C-25 fails, C-27 scores 0.

---

### C-28 -- Pre-Block Sequencing Rule Externalization
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 9 excellence signal -- V-01/V-04/V-05 TIER-SEQUENCING RULE placed as labeled preamble above the verification block entirely; highest possible scan-first position -- scanner encounters the rule before block entry
- **Text**: C-26 requires scan-first accessibility for the TIER-SEQUENCING RULE: the rule must be reachable without reading through per-pair content, satisfied via inside-block first-element placement (V-02) or a TIER ARCHITECTURE SELF-CHECK at the block top (V-03). C-28 advances the scan-first requirement to above-block externalization: the TIER-SEQUENCING RULE appears as a labeled preamble before the verification code fence or block delimiter, so a scanner encounters it before any block parsing begins. This is the highest possible scan priority -- the rule is structurally independent of block content and visible regardless of block depth. Inside-block first-element placement satisfies C-26 but not C-28; above-block preamble placement satisfies both. V-02 (inside-block) passes C-26 but fails C-28; V-01/V-04/V-05 (preamble above block) pass both.
- **Pass condition**: The TIER-SEQUENCING RULE field (or equivalent sequencing constraint) appears as a labeled element above the opening delimiter of the verification block -- before the first code fence, before the first block header, before any per-pair content. The preamble label must make the rule's identity unambiguous (e.g., `TIER-SEQUENCING RULE:` or `SEQUENCING CONSTRAINT:`) and the content must state the ordering rule. An inside-block first-element placement, even if it precedes all per-pair content within the block, fails C-28 if it appears after the block's opening delimiter -- the test is above vs. inside the block structure, not first vs. non-first within it.
- **Anti-pattern**: Placing the TIER-SEQUENCING RULE as the first element inside the verification block (C-26 PASS via inside-block mechanism) fails C-28 because the rule is still inside the block -- a scanner who stops at the block boundary does not see it. A preamble that describes the sequencing rule in prose without a discrete labeled field also fails -- the label is required to make externalization confirm-able by scan. Naming the rule in a pre-block prose paragraph that is not labeled as the rule field itself also fails.
- **Dependency**: Only scoreable if C-26 passes. If C-26 fails, C-28 scores 0.

---

### C-29 -- Generation-Time Floor Commitment
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 9 excellence signal -- V-02/V-04/V-05 Step 5b upstream instruction naming min=2 per category with explicit arithmetic rationale ("2+2=4>3 making C-21 floor provable from per-category counts alone"); prevention-first complement to C-27's post-generation detection
- **Text**: C-27 requires detection: the completed self-check must show per-category minimums whose sum exceeds C-21's floor, confirming after generation that the redundant guarantee was achieved. C-29 requires prevention: an instruction embedded in the generation steps -- before any registry entries are written -- that explicitly names the per-category minimum (min >= 2) and states the arithmetic rationale linking it to C-21's floor. With the commitment in place, the generator is bound to the minimum before the first entry is written, making drift to min=1 structurally impossible rather than merely detectable after the fact. C-27 guards the output; C-29 guards the process. The structural analogy is C-11 (pre-generation structural trace) vs. C-19 (post-generation threshold audit): C-11 validates preconditions before body writing; C-19 confirms thresholds after. Analogously, C-29 commits the floor before registry writing; C-27 confirms the floor was met after.
- **Pass condition**: The output includes an explicit commitment statement, embedded in a generation step or instruction that precedes registry entry creation, that names the per-category minimum value and states the arithmetic relationship to C-21's floor (e.g., "set min=2 per category: 2+2=4>3, so C-21 floor provable from per-category counts without computing the total row"). The commitment must appear before the first registry entry is written -- a post-registry note ("I set min=2") does not satisfy C-29 because the commitment is retroactive rather than preventive. The floor value named in the commitment must match or exceed the per-category minimums actually used.
- **Anti-pattern**: Satisfying C-27 by detection alone (the completed self-check shows min=2 per category) without an upstream commitment instruction fails C-29 -- the floor was achieved but not committed to in advance. A preamble statement about registry quality without a named minimum value also fails -- the commitment must be numerically specific and explicitly linked to C-21's floor via the arithmetic rationale. V-01/V-03 both pass C-27 (detection) but fail C-29 (no upstream instruction).
- **Dependency**: Only scoreable if C-27 passes. If C-27 fails, C-29 scores 0.

---

### C-30 -- Independent Dual-Mechanism Synthesis
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 9 excellence signal -- V-04 (minimum sufficient synthesis: preamble externalization + upstream commitment, no table overhead) and V-05 (maximum redundancy: preamble + table self-check + upstream instruction + floor row); both chains converge when C-28 and C-29 are satisfied by non-interacting mechanisms
- **Text**: C-28 requires pre-block externalization of the TIER-SEQUENCING RULE; C-29 requires a generation-time commitment to the per-category floor minimum. C-30 requires both to be satisfied simultaneously by mechanisms that are structurally independent -- neither mechanism shares state with the other, and removing either leaves the other intact. Preamble externalization is structural-positional (the rule's location relative to the block boundary); generation-time commitment is instructional-procedural (the minimum named in generation steps before entry creation). These axes are orthogonal: the preamble can be moved inside the block without affecting whether an upstream instruction exists, and the upstream instruction can be removed without affecting whether the preamble is external. When both are present and independent, neither mechanism carries the full proof for its criterion -- both C-26 and C-27 can be verified through either mechanism independently, and the synthesis provides a redundant guarantee at the mechanism level above the criterion level. V-04 achieves C-30 at minimum complexity (preamble + upstream instruction, no additional table overhead); V-05 achieves C-30 with maximum verification surfaces (adds table self-check and explicit floor row, creating a third and fourth verifiable artifact).
- **Pass condition**: Both C-28 and C-29 pass. Additionally, the two mechanisms must be structurally non-interacting: (a) the preamble externalization can be evaluated independently of whether the upstream instruction exists, and (b) the upstream instruction can be evaluated independently of whether the preamble is external. A single artifact that simultaneously satisfies both (e.g., an above-block preamble that also contains the floor commitment) fails C-30 because the mechanisms share a single element rather than being independently verifiable -- removal of the element would collapse both C-28 and C-29. Minimum sufficient synthesis (V-04 axis) is acceptable; the criterion does not require maximum redundancy (V-05 axis) as long as independence is satisfied.
- **Anti-pattern**: Achieving C-28 and C-29 through a single above-block element that contains both the sequencing rule and the floor commitment collapses the two mechanisms into one artifact -- independence fails because the artifact carries both proofs simultaneously. A synthesis where one mechanism's value depends on the other (e.g., the upstream instruction's floor value is derived from reading the preamble field) also fails the independence requirement. Satisfying C-28 and C-29 independently but without structural confirmation of non-interaction is a PARTIAL: the mechanisms may be independent, but independence is not self-evident from the output.
- **Dependency**: Only scoreable if both C-28 and C-29 pass. If either fails, C-30 scores 0.

---

### C-31 -- Incumbent Competitor Name Propagation
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 10 excellence signal -- V-01 `INERTIA COMPETITOR:` labeled preamble before Step 1 declares the incumbent as a bound named variable; competitor name propagation check in VALIDATION TRACE; step instruction directs use of the declared name; THRESHOLD CONFIRMATION C-31 block confirms propagation
- **Text**: C-15 requires a violated-assumption anchor that names an incumbent tool as a visible structural step. C-31 advances this by requiring the incumbent competitor name to be declared as a bound named variable in a labeled preamble before the first generation step, and then propagated forward through at least three downstream checkpoints: (a) a propagation check in VALIDATION TRACE that explicitly verifies the name has been carried to required downstream steps, (b) at least one later-step instruction that references the declared name by variable (e.g., "use the name declared in INERTIA COMPETITOR when writing gap entries"), and (c) a THRESHOLD CONFIRMATION or post-generation audit block that counts and confirms C-31's propagation condition is met. With propagation, the competitor name is a live constraint that each step must reference -- its absence from any checkpoint is structurally visible. Without propagation, the competitor name in the assumption anchor is advisory framing; with it, the name is a tracked identifier. The pattern is analogous to C-17's forward-link requirement for assumption entries: C-17 closes the assumption chain by naming a Ticket ID per entry; C-31 closes the competitor chain by propagating the competitor name as a bound variable to downstream checkpoints.
- **Pass condition**: A labeled preamble before the first generation step declares the incumbent competitor by name (e.g., `INERTIA COMPETITOR: [name]`). The competitor name then propagates to all three downstream checkpoints: (a) VALIDATION TRACE or equivalent includes an explicit competitor-name propagation check, (b) at least one later generation step instruction references the declared name by variable (e.g., "use the name declared above"), and (c) a THRESHOLD CONFIRMATION or post-generation audit block confirms that C-31 propagation conditions are satisfied. All three checkpoints must be present and non-empty.
- **Anti-pattern**: Naming the incumbent in the violated-assumption anchor (C-15 PASS) without a bound-variable preamble fails -- inline mention is not a declared variable. A preamble declaration without a downstream propagation check (checkpoint a) leaves propagation unverified. A propagation check without a step instruction that references the declared name (checkpoint b) confirms presence but does not enforce use. A propagation check and step instruction without a THRESHOLD CONFIRMATION block (checkpoint c) lacks the post-generation audit that confirms propagation was achieved. C-31 requires all three checkpoints, not just the preamble declaration.
- **Dependency**: Only scoreable if C-15 passes. If C-15 fails, C-31 scores 0.

---

### C-32 -- SRE-First Structural Priority Ordering
- **Category**: depth
- **Weight**: aspirational
- **Source**: Round 10 excellence signal -- V-02 SRE row placed first in Step 2 (STATUS QUO ANCHOR) and Step 5 (PERSONA VOICE TABLE); "Complete the SRE row first" directive in Step 3; SRE ordering check in VALIDATION TRACE
- **Text**: C-09 rewards outputs that include non-obvious operational failure modes; C-12 rewards voice register density across all persona bodies. C-32 introduces a structural generation commitment that front-loads the operational baseline: the SRE persona row appears first in all persona-indexed tables, an explicit directive mandates writing the SRE row before any other persona row, and VALIDATION TRACE includes a dedicated SRE ordering check. Front-loading the SRE persona ensures that operational vocabulary, inertia behavior, and failure mode framing are established as the reference baseline before other personas inherit from them. Without structural ordering, the SRE perspective is one among many with no priority guarantee; with structural priority, the operational reference baseline is set first and other personas diverge from it. The commitment must hold across all persona-indexed structures in the output -- STATUS QUO ANCHOR, PERSONA VOICE TABLE, and any other table that assigns properties per persona. A single-table application is weaker than consistent multi-table application; the criterion requires both core tables.
- **Pass condition**: The SRE persona row appears as the first row in both: (a) the STATUS QUO ANCHOR table (Step 2 or equivalent) and (b) the PERSONA VOICE TABLE (Step 5 or equivalent). An explicit generation directive appearing in the step instructions before body writing begins mandates SRE priority at write time, not only at display time (e.g., "Complete the SRE row first before writing other rows"). The VALIDATION TRACE includes at least one SRE ordering check that verifies SRE-first position in the relevant tables. All three conditions -- first-row position in STATUS QUO, first-row position in PERSONA VOICE TABLE, and VALIDATION TRACE ordering check -- must be present.
- **Anti-pattern**: Placing the SRE row first in one table but not the other provides partial structural priority -- consistent first-row position across both core persona-indexed structures is required. A coincidental SRE-first position without an explicit directive mandating it fails because the ordering is not enforced -- a future run could produce a different ordering without violating the generation instructions. A VALIDATION TRACE that verifies persona coverage (C-11) without a dedicated SRE ordering check does not satisfy the ordering verification requirement.

---


### C-33 -- Bound-Variable Bracket-Token Propagation
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 11 excellence signal -- V-01 literal `[INERTIA COMPETITOR]` bracket-variable token embedded in table column header and step instruction body; advancement over C-31 prose-reference checkpoint (b)
- **Text**: C-31 requires at least one step instruction to reference the declared competitor name "by variable" -- a prose reference like "use the name declared in the INERTIA COMPETITOR preamble" satisfies C-31 checkpoint (b). C-33 advances this by requiring the declared competitor name to appear as a literal bracket-variable token (e.g., `[INERTIA COMPETITOR]`) embedded directly in at least one table column header or step instruction text body. With bracket-token syntax, propagation is detectable by scanning for the bracket pattern -- any column header or instruction that should reference the competitor but instead contains only prose or a hardcoded name is immediately visible without interpreting prose meaning. Without bracket-token syntax, detecting whether propagation occurred requires reading and interpreting the prose of each instruction; with it, token presence is mechanically verifiable. The advancement is structurally analogous to C-18 advance over C-16: C-16 requires markers named (prose list acceptable); C-18 requires markers dimension-labeled (structurally classifying). C-31 requires the variable referenced (prose acceptable); C-33 requires the variable referenced using token syntax (structurally scannable by bracket pattern).
- **Pass condition**: The literal token `[INERTIA COMPETITOR]` (or equivalent bracket-variable form whose bracket syntax matches the preamble declaration format) appears in at least one table column header or step instruction text body -- not only in a framing sentence before the instruction, but embedded in the instruction action clause or the column label itself (e.g., as a table column header, or as the subject within a step action). The token must match the preamble declaration form. A prose instruction that names the variable without bracket syntax satisfies C-31 checkpoint (b) but fails C-33 -- bracket-token embedding is the distinguishing requirement.
- **Anti-pattern**: Prose reference to "the competitor declared in the preamble" or "the INERTIA COMPETITOR name" in step instructions satisfies C-31 checkpoint (b) but not C-33. A bracket token appearing only in the preamble declaration itself without embedding in downstream step instructions also fails -- the test is downstream token propagation, not declaration token syntax. A bracket token in a post-generation confirmation block without embedding in step instructions also fails -- confirmation reference is not step-level propagation.
- **Dependency**: Only scoreable if C-31 passes. If C-31 fails, C-33 scores 0.

---

### C-34 -- Propagation Chain Pre-Declaration
- **Category**: behavior
- **Weight**: aspirational
- **Source**: Round 11 excellence signal -- V-01 PROPAGATION CHAIN block in the labeled preamble before Step 1 names all three downstream checkpoint labels (A, B, C) before any step executes; creates a checkpoint contract that makes missing checkpoints detectable by declaration-against-output comparison rather than discovery-by-traversal
- **Text**: C-31 requires the preamble to declare the competitor name as a bound variable and requires three downstream checkpoints to exist in the output. C-31 does not require the preamble to enumerate the checkpoint labels -- the three checkpoints can exist in the output without being contracted in advance. C-34 requires the preamble to additionally contain a PROPAGATION CHAIN sub-block that names all three checkpoint labels before Step 1 executes. With the chain contract in place, the complete checkpoint structure is committed before any step runs: a reviewer can confirm chain completeness by comparing the declared checkpoint labels against the output in a single traversal, and any missing checkpoint is a visible deviation from the declared contract. Without the contract, checkpoint completeness requires discovering each one by traversal without a reference list -- completeness is inferred, not declared. The pattern is structurally analogous to C-29 advance over C-27: C-27 requires the floor to be achieved (detected post-generation); C-29 requires the floor to be committed before generation begins (declared pre-generation). C-31 requires the checkpoints to exist in the output; C-34 requires the checkpoints to be contracted before generation, shifting verification from traversal-based discovery to declaration-against-contract comparison.
- **Pass condition**: The labeled preamble block (required by C-31 before Step 1) includes a PROPAGATION CHAIN sub-block or equivalent named structure that enumerates all three checkpoint labels (labeled as a/b/c, as A/B/C, or with equivalent explicit identifiers) before any generation step executes. The chain declaration must name the checkpoints individually -- a prose statement without labeling each checkpoint identifier fails because it declares count without making each checkpoint individually matchable by label. The checkpoint labels in the declaration must correspond to checkpoints that are verifiably present in the output.
- **Anti-pattern**: A preamble that declares the competitor variable and asserts propagation will occur through three checkpoints without naming individual checkpoint identifiers fails -- count assertion without label contract does not provide the pre-declaration property. A post-generation confirmation block (C-31 checkpoint c) that lists the three checkpoints retrospectively satisfies C-31 but fails C-34 because the contract was not established before generation. Naming the checkpoints in a post-section summary rather than the preamble also fails -- the contract must appear before Step 1, not after. Satisfying the three checkpoint labels in the output body without a matching declaration in the preamble satisfies C-31 but fails C-34.
- **Dependency**: Only scoreable if C-31 passes. If C-31 fails, C-34 scores 0.

---

### C-35 -- SRE-Write-First Enforcement Gate
- **Category**: correctness
- **Weight**: aspirational
- **Source**: Round 11 excellence signal -- V-02 SRE-WRITE-FIRST GATE block between PERSONA VOICE TABLE step (Step 5) and body-writing step (Step 6); structural enforcement gate that blocks forward progress until SRE-first position is verified; advancement over C-32 advisory write-first directive plus post-hoc VALIDATION TRACE check
- **Text**: C-32 requires SRE-first position in both core persona-indexed tables, an explicit write-first directive before body writing, and a VALIDATION TRACE ordering check. The write-first directive states intent before the table is built; the trace verifies ordering after all content is complete. Neither blocks body writing if the SRE row was placed second or third in the table. C-35 introduces a structural enforcement gate between the table-construction step and the body-writing step: a named gate block that checks whether the SRE row is first in the PERSONA VOICE TABLE and explicitly halts body writing until the check passes. With the enforcement gate, SRE-first position in the table is a pre-condition for advancing to body writing -- a table generated with a different persona first cannot proceed to body writing without a visible gate failure. Without the gate, a table built with the wrong ordering can proceed silently to body writing, with the error discovered only in the post-hoc VALIDATION TRACE (or not at all). The pattern is structurally analogous to C-22 advance over C-20: C-20 requires the bidirectional verification to occur; C-22 requires it to be binding -- MISMATCH must halt before proceeding. C-32 requires the write-first directive and ordering check to exist; C-35 requires the write-first check to be binding -- SRE-not-first must halt before body writing begins.
- **Pass condition**: A named gate block appears in the output at the boundary between the PERSONA VOICE TABLE generation step and the body-writing step (or between any persona-indexed table-construction step and the next generation step that depends on ordering). The gate block must: (a) explicitly name what it is checking (SRE-first position in the PERSONA VOICE TABLE or equivalent persona-indexed table), (b) produce a binary PASS/FAIL or PROCEED/HALT verdict, and (c) include an explicit gate instruction that requires correction and re-verification before advancing if the SRE row is not first (e.g., "if SRE is not first: reorder before proceeding to Step 6"). The gate must be a named structural element -- not embedded as a sentence in body-prose -- and must appear between steps, not after all content is generated. A VALIDATION TRACE ordering check appearing after body writing satisfies C-32 but fails C-35 -- post-hoc verification is not a pre-body enforcement gate.
- **Anti-pattern**: A write-first directive in step instructions satisfies C-32 write-first directive requirement but fails C-35 -- a directive is advisory: it states the intended order but does not gate forward progress on confirmation that the order was followed. A VALIDATION TRACE ordering check appearing anywhere after body writing satisfies C-32 but fails C-35 because the check is retrospective rather than a structural barrier before body writing. An ordering check embedded in C-11 pre-generation validation trace also fails C-35 because it does not constitute a between-step gate at the table-to-body boundary.
- **Dependency**: Only scoreable if C-32 passes. If C-32 fails, C-35 scores 0.

---

## Scoring Summary

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | Ticket structural completeness | essential | correctness |
| C-02 | Valid category/severity/volume values | essential | correctness |
| C-03 | Persona grounding from stock set | essential | correctness |
| C-04 | Gap analysis present and typed | essential | coverage |
| C-05 | Ticket set spans 3+ categories | essential | coverage |
| C-06 | Sample body in persona voice | recommended | depth |
| C-07 | Calibrated volume/severity distribution | recommended | depth |
| C-08 | Gap analysis names actionable artifacts | recommended | depth |
| C-09 | Non-obvious failure mode coverage | aspirational | behavior |
| C-10 | 90-day temporal staging | aspirational | depth |
| C-11 | Inline validation trace | aspirational | correctness |
| C-12 | Voice register density | aspirational | depth |
| C-13 | Phase-severity semantic binding | aspirational | depth |
| C-14 | Competitive gap classification | aspirational | coverage |
| C-15 | Violated-assumption anchor | aspirational | behavior |
| C-16 | Voice marker citation | aspirational | depth |
| C-17 | Assumption chain ticket forward-link | aspirational | behavior |
| C-18 | Column-label marker attribution | aspirational | depth |
| C-19 | Post-generation threshold confirmation | aspirational | correctness |
| C-20 | Bidirectional linkage verification | aspirational | correctness |
| C-21 | Dimension-label rejection registry | aspirational | depth |
| C-22 | Mismatch-triggered revision gate | aspirational | correctness |
| C-23 | Dual-category rejection structure | aspirational | depth |
| C-24 | Two-tier gate architecture | aspirational | correctness |
| C-25 | Registry completeness self-check | aspirational | depth |
| C-26 | Tier architecture self-documentation | aspirational | correctness |
| C-27 | Redundant-granularity floor guarantee | aspirational | depth |
| C-28 | Pre-block sequencing rule externalization | aspirational | correctness |
| C-29 | Generation-time floor commitment | aspirational | depth |
| C-30 | Independent dual-mechanism synthesis | aspirational | correctness |
| C-31 | Incumbent competitor name propagation | aspirational | behavior |
| C-32 | SRE-first structural priority ordering | aspirational | depth |
| C-33 | Bound-variable bracket-token propagation | aspirational | behavior |
| C-34 | Propagation chain pre-declaration | aspirational | behavior |
| C-35 | SRE-write-first enforcement gate | aspirational | correctness |

**To pass golden threshold**: C-01 through C-05 all pass, composite >= 80.

**C-13 dependency**: only scoreable when C-10 passes.

**C-17 dependency**: only scoreable when C-15 passes.

**C-18 dependency**: only scoreable when C-16 passes.

**C-20 dependency**: only scoreable when C-17 passes.

**C-21 dependency**: only scoreable when C-18 passes.

**C-22 dependency**: only scoreable when C-20 passes.

**C-23 dependency**: only scoreable when C-21 passes.

**C-24 dependency**: only scoreable when C-22 passes.

**C-25 dependency**: only scoreable when C-23 passes.

**C-26 dependency**: only scoreable when C-24 passes.

**C-27 dependency**: only scoreable when C-25 passes.

**C-28 dependency**: only scoreable when C-26 passes.

**C-29 dependency**: only scoreable when C-27 passes.

**C-30 dependency**: only scoreable when both C-28 and C-29 pass.

**C-31 dependency**: only scoreable when C-15 passes.

**C-32**: no dependency -- independently scoreable.

**C-15 vs C-09**: independent -- C-09 rewards output result, C-15 rewards visible mechanism.

**C-16 vs C-12**: C-12 requires density present; C-16 requires density cited. Both score independently.

**C-17 vs C-15**: C-15 requires the assumption mechanism visible; C-17 requires the chain closed with a Ticket ID.

**C-18 vs C-16**: C-16 requires markers named; C-18 requires markers dimension-labeled.

**C-19 vs C-11**: C-11 = pre-generation structural invariant trace; C-19 = post-generation percentage threshold audit. Non-overlapping complement pair.

**C-20 vs C-17**: C-17 establishes the forward-link at generation time; C-20 verifies the link survived body writing and holds in both directions with content alignment. Non-overlapping sequential pair.

**C-21 vs C-18**: C-18 requires dimension labels present; C-21 requires an explicit rejection registry that makes the label format binary.

**C-22 vs C-20**: C-20 requires the per-pair bidirectional check; C-22 requires the check to be binding -- MISMATCH must trigger mandatory revision before proceeding. Advisory verification vs. enforcing gate.

**C-23 vs C-21**: C-21 requires a rejection registry with three+ disqualifying forms; C-23 requires the registry to cover both format violations and value violations as named categories. Entry count vs. category completeness.

**C-24 vs C-22**: C-22 requires per-pair gates that halt on MISMATCH; C-24 requires a second block-level gate tier with a sequential ordering constraint -- per-pair gates must all clear before the block-level gate is evaluated. Single-tier enforcement vs. two-tier sequential architecture.

**C-25 vs C-23**: C-23 requires both rejection categories to be present and distinguishable; C-25 requires the registry to self-count its entries per category and report pass/fail against stated minimums, with an explicit total row naming C-21's floor. Category presence vs. self-verified completeness.

**C-26 vs C-24**: C-24 requires the ordering constraint between tiers to be explicit (prose acceptable); C-26 requires the two-tier architecture to be structurally self-documenting via named tier headers and a named sequencing rule field, with scan-first accessibility -- compliance verifiable by header scan rather than prose parsing. Constraint existence vs. structural legibility.

**C-27 vs C-25**: C-25 requires an explicit total row naming C-21's floor, shifting the cross-criterion guarantee from reviewer-computed to output-declared; C-27 requires per-category minimums set high enough that their sum independently exceeds C-21's floor, so compliance is provable at both the per-category level and the total level without either level carrying the full load. Single-level guarantee vs. redundant-granularity guarantee.

**C-28 vs C-26**: C-26 requires scan-first accessibility (inside-block first-element OR self-check table at block top both satisfy it); C-28 requires the TIER-SEQUENCING RULE to appear above the block structure entirely -- the rule is encountered before block entry, not merely before per-pair content within the block. Inside-block first-element passes C-26 but fails C-28. Scan-first within block vs. pre-block externalization.

**C-29 vs C-27**: C-27 requires the completed self-check to show per-category minimums whose sum exceeds C-21's floor (detection after generation); C-29 requires an upstream instruction committing to that minimum before any registry entries are written (prevention before generation). Detection of floor achievement vs. commitment to floor before generation begins.

**C-30 vs C-28+C-29**: Passing C-28 and C-29 independently does not satisfy C-30. C-30 additionally requires that the two mechanisms are structurally non-interacting -- each must independently satisfy its parent criterion without sharing state with the other. Satisfying two criteria independently vs. satisfying them via a provably independent dual-mechanism synthesis.

**C-31 vs C-15**: C-15 requires the violated-assumption anchor to exist as a visible named step that names an incumbent; C-31 requires the incumbent name to be declared as a bound variable in a labeled preamble and propagated forward through three downstream checkpoints (VALIDATION TRACE propagation check, step instruction referencing declared name, THRESHOLD CONFIRMATION block). Named incumbent vs. propagated bound variable.

**C-32 vs C-09**: C-09 rewards the presence of non-obvious operational failure modes in the output; C-32 rewards the structural generation commitment that front-loads the operational baseline -- SRE-first position in all persona-indexed tables, an explicit write-first directive, and a VALIDATION TRACE ordering check. Output result vs. structural ordering commitment.

**C-32 vs C-12**: C-12 requires voice register density (>= 2 markers per body, different register dimensions); C-32 requires the SRE persona to be structurally prior in generation, establishing the operational vocabulary baseline before other personas are written. Density in output vs. ordering in generation.

**C-33 dependency**: only scoreable when C-31 passes.

**C-34 dependency**: only scoreable when C-31 passes.

**C-35 dependency**: only scoreable when C-32 passes.

**C-33 vs C-31**: C-31 requires the declared competitor name to be referenced by variable in at least one step instruction (prose acceptable); C-33 requires the reference to use literal bracket-variable token syntax embedded in table headers or step instruction action clauses, making propagation detectable by bracket-pattern scan rather than prose interpretation. Prose variable reference vs. bracket-token embedding.

**C-34 vs C-31**: C-31 requires the preamble to declare the bound variable and requires three checkpoints to exist in the output; C-34 requires the preamble to additionally enumerate all three checkpoint labels as a named PROPAGATION CHAIN sub-block, creating a pre-declared contract against which output completeness can be verified by comparison rather than traversal. Checkpoint existence in output vs. checkpoint contract in preamble before generation.

**C-35 vs C-32**: C-32 requires SRE-first position in both core tables, an advisory write-first directive, and a post-hoc VALIDATION TRACE ordering check; C-35 requires a named gate block at the table-to-body boundary that produces a binary verdict and blocks body writing until SRE-first position is verified. Advisory ordering commitment plus retrospective check vs. between-step enforcement gate.

**Dependency stacks**:
- `C-09 -> C-15 -> C-17 -> C-20 -> C-22 -> C-24 -> C-26 -> C-28`
- `C-09 -> C-15 -> C-31 -> C-33`
- `C-09 -> C-15 -> C-31 -> C-34`
- `C-12 -> C-16 -> C-18 -> C-21 -> C-23 -> C-25 -> C-27 -> C-29`
- `C-28 + C-29 -> C-30`
- `C-32 -> C-35`
- `C-32` (independent)
