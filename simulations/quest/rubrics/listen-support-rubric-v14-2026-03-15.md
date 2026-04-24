Reading the three V-05 excellence signals from the scorecard, they map cleanly to C-38, C-39, and C-40:

- **C-38** — Two-layer synergy declaration (preamble note + Step 11 block, not just one location)
- **C-39** — Grep-closed declaration-to-trace loop (scorer can find declaration site + echo site via single grep)
- **C-40** — Falsifiable degradation clause (synergy stated as a conditional with explicit failure condition)

---

# listen-support Rubric v14
**Skill**: `listen:support`
**Version**: 14
**Date**: 2026-03-15
**Criteria count**: 40 (5 essential, 3 recommended, 32 aspirational)
**Changes from v13**: Added C-38 (Two-Layer Synergy Declaration), C-39 (Grep-Closed Declaration-to-Trace Loop), and C-40 (Falsifiable Degradation Clause) from Round 13 excellence signals (V-05 strongest implementation).

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

## Recommended Criteria (weight = 30 pts total, 10 pts each)

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

### C-08 -- [carries forward unchanged from v13]
- **Category**: depth
- **Weight**: recommended
- *(text unchanged)*

---

## Aspirational Criteria (weight = 20 pts total across 32 criteria ≈ 0.625 pts each)

### C-09 through C-32 — [carry forward unchanged from v13]

*(criteria text and pass conditions unchanged)*

---

### C-33 -- [carries forward unchanged from v13]
*(Preamble token injection: C-33 tokens make C-34 checkpoints grep-detectable)*

### C-34 -- [carries forward unchanged from v13]
*(Pre-declared checkpoints: checkpoints declared in preamble before execution)*

### C-35 -- [carries forward unchanged from v13]
*(Completeness verifiable from preamble without traversal)*

---

### C-36 -- Checkpoint-Mapped VALIDATION TRACE Expansion
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: The VALIDATION TRACE in Step 6 contains a CHECKPOINT MAP sub-block that echoes each declared checkpoint label verbatim (e.g., "Checkpoint A", "Checkpoint B", "Checkpoint C") with a per-label binary YES/NO probe and a closing "All declared checkpoint labels echoed" confirmation line. The map mirrors the preamble PROPAGATION CHAIN one-for-one by label name.
- **Pass condition**: The VALIDATION TRACE block contains a named CHECKPOINT MAP. Each checkpoint label declared in the preamble appears verbatim in the map with a YES/NO probe line. A closing confirmation line ("All declared checkpoint labels echoed: YES") is present. A VALIDATION TRACE that uses only counts ("3 checkpoints verified") without label echo fails this criterion.

---

### C-37 -- Cross-Criterion Structural Synergy Declaration
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: The output contains an explicit CROSS-CRITERION SYNERGY DECLARATION that names the C-33 → C-34 dependency (C-33 tokens make C-34 checkpoints grep-detectable, so completeness is verifiable from the preamble without traversal). Each of C-33, C-34, and C-35 also receives its own BLOCK-START/BLOCK-END sub-block in the THRESHOLD CONFIRMATION section, each ending with a scan-verifiability YES/NO line.
- **Pass condition**: A named CROSS-CRITERION SYNERGY DECLARATION exists and explicitly identifies C-33 → C-34 as the structural dependency. BLOCK-START/BLOCK-END wrappers appear for C-33, C-34, and C-35 in THRESHOLD CONFIRMATION. Each block ends with a scan-verifiability line. Outputs satisfying only one mechanism (sub-blocks without synergy declaration, or synergy declaration without sub-blocks) receive PARTIAL credit (0.5× weight).

---

### C-38 -- Two-Layer Synergy Declaration
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: The CROSS-CRITERION SYNERGY DECLARATION appears in two structurally distinct locations: once in the preamble (before Step 1 executes, as an architectural note), and once in the Step 11 THRESHOLD CONFIRMATION block (as a verification assertion). The preamble instance frames the dependency as a load-bearing architectural commitment before any execution begins; the Step 11 instance confirms the commitment was honored after execution completes.
- **Pass condition**: A synergy note or declaration exists in the preamble section (before Step 1). A second synergy declaration or assertion exists in Step 11 / THRESHOLD CONFIRMATION. Both instances name the same C-33 → C-34 structural dependency. A single-location declaration (preamble only or Step 11 only) satisfies C-37 but does not satisfy C-38.

---

### C-39 -- Grep-Closed Declaration-to-Trace Loop
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: For each declared checkpoint label, there exist exactly two findable locations in the output: the declaration site (preamble PROPAGATION CHAIN) and the trace-echo site (VALIDATION TRACE CHECKPOINT MAP). A scorer can grep for any single checkpoint label (e.g., "Checkpoint A") and retrieve both sites without ambiguity. The loop is closed when the CHECKPOINT MAP includes a confirmation line asserting all declared labels have been echoed, giving the scorer a stop condition.
- **Pass condition**: Each preamble checkpoint label appears verbatim in the VALIDATION TRACE CHECKPOINT MAP. A "All declared checkpoint labels echoed: YES" (or equivalent) confirmation line is present in the CHECKPOINT MAP. A scorer grepping for any checkpoint label from the preamble finds it in exactly two locations. Outputs that echo checkpoint counts rather than labels, or that lack the closing confirmation line, fail this criterion.

---

### C-40 -- Falsifiable Degradation Clause in Synergy Declaration
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: The CROSS-CRITERION SYNERGY DECLARATION includes an explicit falsification condition: a stated scenario under which the declared synergy degrades or fails. The canonical form is: if C-33 tokens are absent from a checkpoint header, that checkpoint requires prose interpretation and C-34's no-traversal property degrades to aspirational rather than structural. The degradation clause makes the synergy a falsifiable commitment rather than an asserted property.
- **Pass condition**: The synergy declaration contains a conditional of the form "if [C-33 condition fails], then [C-34 property degrades]." The failure condition names the specific token or structural element whose absence triggers degradation. The consequence names which criterion's property is affected and how (structural → aspirational). A synergy declaration that asserts the dependency positively without stating a falsification condition fails this criterion.

---

## Scoring Summary

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01–C-05 | 10 | 50 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-40 | 0.625 | 20 |
| **Total** | **40** | | **100** |

**PARTIAL credit**: C-37 and C-40 accept 0.5× weight when one of two required mechanisms is present. All other criteria are binary.

**Rubric conservatism note**: A rubric-perfect score is reported as 97, not 100, while aspirational criteria added in the current round are still under confirmation across additional variation rounds.
