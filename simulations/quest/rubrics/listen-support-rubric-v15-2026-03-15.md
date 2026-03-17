# listen-support Rubric v15
**Skill**: `listen:support`
**Version**: 15
**Date**: 2026-03-15
**Criteria count**: 41 (5 essential, 3 recommended, 33 aspirational)
**Changes from v14**: Added C-41 (Three-Dimensional Verification Coverage) from Round 14 excellence signal E-01 (V-05 full-synthesis implementation).

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

### C-08 -- [carries forward unchanged from v14]
- **Category**: depth
- **Weight**: recommended

---

## Aspirational Criteria (weight = 20 pts total, 1 pt each)

### C-09 through C-30 — [carry forward unchanged from v14]

---

### C-31 through C-37 — [carry forward unchanged from v14]
*(Aspirational gains from R11–R13)*

---

### C-38 -- Two-Layer Synergy Declaration
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: Cross-criterion synergy between C-33 and C-34 is declared in exactly two locations: a preamble note (LAYER 1 of 2) and the Step 11 synergy block (LAYER 2 of 2). A single-location declaration is insufficient; a scorer must be able to confirm both layers are present via an explicit two-layer presence check.
- **Pass condition**: Preamble carries a "LAYER 1 of 2" label for the synergy declaration. Step 11 carries a "LAYER 2 of 2" label. A two-layer presence check block exists (at or near Step 11) with an explicit YES/NO entry for each layer. A declaration present in only one location, or a check that does not enumerate both layers, fails.

---

### C-39 -- Grep-Closed Declaration-to-Trace Loop
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: A machine-findable anchor token `[SYNERGY-ANCHOR: C33xC34]` appears in both the preamble synergy declaration and the Step 11 echo site, so a single grep closes the declaration-to-trace loop. The grep route is explicitly stated in the preamble ("one grep finds both sites"), and the Step 11 block includes a grep-closed confirmation line verifying that the single grep yields exactly two matches.
- **Pass condition**: The token `[SYNERGY-ANCHOR: C33xC34]` (exact string) appears in both the preamble and Step 11. The preamble explicitly names the grep route and states the expected match count. A grep-closed confirmation block in Step 11 includes a YES/NO field confirming one grep closes the loop. Absence of the token in either location, or absence of the confirmation block, fails.

---

### C-40 -- Falsifiable Degradation Clause
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: The synergy declaration includes a falsifiable degradation clause structured as a full IF/THEN/AND conditional: a named trigger condition (C-33 absent), a named consequence (checkpoint degrades to prose interpretation), a named cascade effect (C-34 no-traversal property also degrades), a named failure state (binary and testable), and an explicit label marking the clause as falsifiable. The clause must appear in both the preamble (LAYER 1) and the Step 11 block (LAYER 2).
- **Pass condition**: A DEGRADATION CLAUSE sub-section exists in both preamble and Step 11 (not just a single assertion line). The sub-section contains: IF/THEN/AND structure (YES/NO), named failure state (YES/NO), C-34 cascade effect named (YES/NO), clause explicitly labeled "falsifiable" (YES/NO). A single-line assertion ("Degradation declared: YES/NO") without the full conditional structure fails.

---

### C-41 -- Three-Dimensional Verification Coverage
- **Category**: verifiability
- **Weight**: aspirational
- **Text**: The three synergy verification mechanisms -- two-layer labeling (C-38), grep-closed anchor (C-39), and falsifiable degradation clause (C-40) -- address distinct, non-overlapping verifiability questions: WHERE the synergy is declared, HOW a scorer locates both declaration and echo sites, and WHAT breaks if the mechanism is absent. No two mechanisms answer the same question; each is necessary and none is redundant with the others. The full triad must be present and each mechanism must be traceable to its own verifiability dimension.
- **Pass condition**: All three of C-38, C-39, and C-40 pass. Additionally, the output demonstrates non-overlap: the WHERE dimension is answered by layer labels alone, the HOW dimension is answered by the grep anchor alone, and the WHAT dimension is answered by the degradation clause alone. A set where two mechanisms address the same dimension, or where any mechanism is absent, fails. This criterion cannot pass if any of C-38, C-39, or C-40 fail.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (C-01–C-05) | 5 | 50 pts (10 each) |
| Recommended (C-06–C-08) | 3 | 30 pts (10 each) |
| Aspirational (C-09–C-41) | 33 | 20 pts (1 each) |
| **Total** | **41** | **100 pts** |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v15 | 2026-03-15 | Added C-41 (Three-Dimensional Verification Coverage) from R14 E-01 |
| v14 | 2026-03-15 | Added C-38, C-39, C-40 from R13 V-05 excellence signals |
| v13 | 2026-03-15 | C-31–C-37 from R11–R13 gains |
