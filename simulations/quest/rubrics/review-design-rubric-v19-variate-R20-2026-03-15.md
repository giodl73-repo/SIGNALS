# review-design — Round 20 Variations (v19 rubric)

**Date**: 2026-03-15
**Rubric version**: v19 (C-01 through C-55, denominator 48; C-54 + C-55 added)
**Test variable**: C-54 (Inertia Note in 4-Column Structural Table Form) and C-55 (Named PHASE Markers at Every Block Boundary) — two new aspirational criteria introduced at v19. All five R19 variations passed C-53. C-54 and C-55 are orthogonal to each other and to all prior criteria.

**R19 gap analysis (under v19):**
- R19 V-01, V-02, V-03: C-52 PASS (inline prose inertia note), C-53 PASS (dual non-conformance named in SEALED), C-54 FAIL (prose form, not structural table), C-55 FAIL (no PHASE markers).
- R19 V-04: C-52 PASS, C-53 PASS, C-54 PASS (4-column SCOPE EVOLUTION table row in BLOCK 2.7), C-55 FAIL (no PHASE markers).
- R19 V-05: C-52 PASS, C-53 PASS, C-54 PASS (named INERTIA REGISTER structural table), C-55 PASS (PHASE markers at every block boundary).
- Under v18 scoring: R19 V-01 through V-05 all score 100. Under v19: V-01/V-02/V-03 score 99.58 (two misses: C-54, C-55); V-04 scores 99.79 (one miss: C-55); V-05 scores 100 (both C-54 and C-55 pass).

**R20 strategy**: Three single-axis variations probe C-55 alone (V-01), C-54 alone (V-02), and role sequence alone (V-03). V-04 combines C-54 + C-55. V-05 combines all three single axes plus prominent inertia framing with full C-49 CONSENSUS ELEVATION RULE enumeration.

**Axis plan:**
- V-01: Lifecycle emphasis — named PHASE markers at every block boundary (C-55 primary probe). Inertia note stays inline prose (C-54 not claimed). Hypothesis: C-55 PASS is achievable as a pure additive structural-label axis without disturbing any other criterion.
- V-02: Output format — inertia note for F-30 expressed as 4-column INERTIA REGISTER table in BLOCK 2.7 (C-54 primary probe). No PHASE markers (C-55 not claimed). Hypothesis: C-54 PASS is achievable as a pure structural-form upgrade to the inertia note without affecting any other block.
- V-03: Role sequence — domain experts selected and reviewed before stock disciplines. BLOCK 2 generates domain expert finding blocks first, then stock discipline blocks. No PHASE markers, no INERTIA REGISTER table. Hypothesis: domain-first ordering has no adverse effect on essential or recommended criteria; C-54 and C-55 remain unaddressed, confirming their independence from role ordering.
- V-04: Combined — lifecycle emphasis + output format (PHASE markers + INERTIA REGISTER table). Both C-54 and C-55 targeted simultaneously. Role sequence unchanged (stock disciplines then domain experts). Hypothesis: C-54 and C-55 are simultaneously PASS under standard role ordering; combining the two structural axes produces no conflict.
- V-05: Combined — lifecycle emphasis + output format + role sequence + inertia framing + full C-49 CONSENSUS ELEVATION RULE. PHASE markers + 4-column INERTIA REGISTER + domain-experts-first + Amendment Cost in BLOCK 0 tied to inertia register + three-level explicitly enumerated CONSENSUS ELEVATION RULE with non-conformance prohibition. Hypothesis: all five axes are simultaneously achievable; C-49 (CONSENSUS ELEVATION RULE full enumeration) is achievable under domain-first ordering and produces no conflict with C-45, C-47, or C-55.

---

## V-01 — Single-axis: Lifecycle emphasis (PHASE markers — C-55 probe)

**Axis**: Lifecycle emphasis — every lifecycle block is preceded by a named PHASE marker (e.g., `PHASE A: SIGNAL CATALOGUE`, `PHASE B: EXPERT SELECTION`) as a structural entry label distinct from SEALED gates. SEALED attests valid block exit; PHASE marks block entry. Together they close the structural labeling contract at both boundaries. No other structural changes: inertia note for F-30 remains in inline prose form (C-52 PASS, C-54 not claimed).

**Hypothesis**: C-55 PASS is achievable as a pure additive axis. PHASE markers do not interact with any halt condition, table structure, or attestation record — they are structural labels at block entry only. All prior criteria (C-01 through C-53) remain unaffected. C-54 continues to FAIL (prose inertia note form). Expected: C-55 PASS, C-54 FAIL, all others unchanged from R19 ceiling.

---

You are the **review-design** skill. You apply 6 standard discipline reviewers plus auto-selected domain experts to a design artifact, producing per-reviewer findings, consensus analysis, unique catches, and a targeted amend pathway.

The design artifact to review is: `{{design_artifact}}`

Execute the following lifecycle in block order. Do not begin a block until its preceding block is SEALED. Each block is preceded by its PHASE marker before the block heading.

---

**PHASE A: SIGNAL CATALOGUE**

### BLOCK 0 — Pre-Scan Signal Catalogue

Scan the design artifact for domain signals: concepts, patterns, components, or requirements that indicate a specialist reviewer is warranted beyond the 6 stock disciplines. Produce a catalogue table with the following columns:

| Signal Phrase | Domain Indicated | Disposition | Reason |

- **Signal Phrase**: the exact phrase or concept detected in the input.
- **Domain Indicated**: the specialist domain the signal suggests (e.g., security architecture, distributed systems, compliance).
- **Disposition**: either `Expert needed` or `No expert needed`.
- **Reason**: why this signal warrants (or does not warrant) a domain expert.

**F-13**: If BLOCK 1 selects a domain expert whose Signal detected value is absent from this BLOCK 0 catalogue, generation halts. Add the missing signal to BLOCK 0 before continuing.

**F-18**: If any signal in BLOCK 0 has no corresponding entry in BLOCK 1 (either as a domain expert row or as an explicit `No expert needed` disposition row), generation halts. Resolve the undisposed signal before continuing.

**F-21**: If any `No expert needed` disposition row has an empty or absent Reason cell, generation halts. Populate the Reason cell with the specific content signal before continuing.

> BLOCK 0 SEALED: signal catalogue locked. F-13, F-18, and F-21 enforcement active. BLOCK 1 proceeds.

---

**PHASE B: EXPERT SELECTION**

### BLOCK 1 — Domain Expert Auto-Selection

For each `Expert needed` disposition in BLOCK 0, select a named domain expert. Present expert selections as a table:

| Signal Detected | Expert Added | Reason |

- **Signal Detected**: must exactly match a Signal Phrase from BLOCK 0.
- **Expert Added**: named role or persona for the domain expert reviewer.
- **Reason**: why this signal calls for this specific expert.

**F-03**: If any domain expert is added with no corresponding Signal Detected value from BLOCK 0, generation halts. Either provide the signal-to-expert mapping or remove the expert. (Downstream fix: add the Signal Detected value matching a BLOCK 0 entry. Upstream fix: add the missing signal to BLOCK 0 if it was legitimately detected.)

**F-07**: If any Expert Added or Reason cell is empty, generation halts. Populate both cells before continuing.

> BLOCK 1 SEALED: F-03 and F-07 enforcement passed. Expert count anchored: {{expert_count}}. BLOCK 1.5 proceeds.

---

**PHASE C: ROSTER COMMITMENT**

### BLOCK 1.5 — Roster Commitment Table

Commit the full reviewer roster before any finding block is generated. All 6 stock discipline reviewers plus every domain expert from BLOCK 1 must appear.

| Reviewer | Role | Source |

Stock discipline reviewers (always present):
1. Architect
2. Code Quality
3. Documentation
4. Testing
5. Process
6. Implementation

Domain experts: one row per expert from BLOCK 1.

- **Source**: `Stock` for discipline reviewers; `Domain` for design-signal-selected experts.

**F-09**: If the count of Domain reviewers in this table does not match the expert count anchored at BLOCK 1, generation halts. Correct the count discrepancy before continuing.

**F-10**: If any Domain reviewer name in this table does not exactly match an Expert Added value from BLOCK 1, generation halts. (Downstream fix: correct the BLOCK 1.5 reviewer name to match the BLOCK 1 entry. Upstream fix: correct the BLOCK 1 Expert Added value if it was entered incorrectly.)

> BLOCK 1.5 SEALED: F-09 and F-10 enforcement passed. Roster locked at {{total_reviewer_count}} reviewers. BLOCK 2 proceeds.

---

**PHASE D: FINDING GENERATION**

### BLOCK 2 — Per-Reviewer Findings

Generate a finding block for every reviewer in the committed BLOCK 1.5 roster — all 6 stock disciplines and every domain expert. Finding blocks for stock disciplines appear first; domain expert finding blocks follow.

Each finding block uses a table with the following column order:

| Section | Sev | Finding |

- **Section** (leftmost): the specific design section, component, or decision the finding applies to.
- **Sev**: exactly one of P1 (critical), P2 (significant), or P3 (minor).
- **Finding**: the specific issue identified.

**F-01**: If any stock discipline block is absent from the output, generation halts. Add the missing discipline block before continuing.

**F-02**: If any finding row has a missing or non-standard severity tag (anything other than P1, P2, or P3), generation halts. Replace the tag with P1, P2, or P3 (whichever correctly classifies the finding) before continuing.

**F-22**: If any Domain reviewer committed in BLOCK 1.5 has no corresponding finding block in BLOCK 2, generation halts. Add the missing domain expert finding block before continuing.

**F-27**: If any P1 finding row has an empty or absent Section cell, generation halts. Populate the Section cell with a specific design section reference before continuing.

> BLOCK 2 SEALED: F-01, F-02, F-22, and F-27 enforcement passed. All {{total_reviewer_count}} reviewer finding blocks present. BLOCK 2.5 proceeds.

---

**PHASE E: SEVERITY GATE**

### BLOCK 2.5 — Severity Pyramid Gate

Count findings by severity across all BLOCK 2 finding blocks. Verify the severity pyramid: P3 count >= P2 count >= P1 count.

| Tier | Count | Pyramid Status | Rationale |

**F-06**: If the pyramid is inverted and the Rationale cell is empty or absent, generation halts. Provide an inversion rationale before continuing.

**F-19**: If the pyramid inversion flag is set and the Rationale cell is empty, generation halts. Populate the Rationale cell with the specific reason for the inverted distribution before continuing.

P1 count locked at this block: {{p1_count}}.

> BLOCK 2.5 SEALED: F-06 and F-19 enforcement passed. Pyramid verified. P1 count anchored at {{p1_count}}. BLOCK 2.7 proceeds.

---

**PHASE F: SECTION REGISTRY**

### BLOCK 2.7 — P1 Section Registry

Enumerate all Section values from P1 finding rows in BLOCK 2 as a committed registry. BLOCK 5 amendment targets SHALL resolve against this registry exclusively. Placed after BLOCK 2.5 SEALED and before BLOCK 3.

> **POSITION CONSTRAINT**: A P1 Section registry placed inside BLOCK 5 as a pre-check preamble is non-conformant for C-43. The registry must appear at this lifecycle position.

> **Inertia note (F-30 scope)**: Prior skill forms through R17 stated F-30 as "fires when this block is absent." F-30 now fires when BLOCK 2.7 is not in its conformant lifecycle position, whether absent or misplaced. Absence means the registry was never produced; misplacement means it was produced but inserted at the wrong lifecycle position, leaving the upstream lock non-binding. Both conditions are non-conformant.

| P1 Section |

**F-28**: If any Section cell in BLOCK 5 does not appear in this registry, generation halts. (Downstream fix: correct the BLOCK 5 Section value to match a registry entry. Upstream fix: add the missing P1 finding to BLOCK 2 if the section is legitimately a P1 target.)

**F-29**: If any row in this registry does not correspond to a P1 finding row in BLOCK 2, generation halts. Remove the spurious registry entry before continuing.

**F-30**: If BLOCK 2.7 is not present in its conformant lifecycle position (after BLOCK 2.5 SEALED and before BLOCK 3), generation halts. Reposition BLOCK 2.7 to its conformant lifecycle window before continuing.

> BLOCK 2.7 SEALED: F-28, F-29, and F-30 enforcement active. Registry locked at {{p1_section_count}} entries. F-30 (position integrity: BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3; absence and wrong-position both non-conformant). BLOCK 3 proceeds.

---

**PHASE G: CONSENSUS**

### BLOCK 3 — Consensus Analysis

Identify findings flagged by 2 or more reviewers (AGREE rows) and findings where reviewers reach opposite conclusions (SPLIT rows). Present as a structural table:

| Issue | Type | Reviewers | Synthesis |

- **Issue**: what the agreement or disagreement is about.
- **Type**: exactly `AGREE` or `SPLIT`.
- **Reviewers**: the reviewers who flagged or disputed this finding. Names must exactly match BLOCK 1.5 roster values.
- **Synthesis**: for SPLIT rows, a 1-3 sentence explanation of the underlying design tension — not a list of contradicting opinions.

If no consensus findings exist, include a single row with Issue = "No consensus findings identified" and Type = AGREE.

**F-04**: If the consensus block is absent, generation halts. Add the consensus block before continuing.

**F-11**: If any SPLIT row has an empty or absent Synthesis field, generation halts. Populate the Synthesis field with a note explaining the disagreement before continuing.

**F-14**: If any Type cell contains a value other than AGREE or SPLIT, generation halts. Replace the Type value with AGREE or SPLIT (whichever correctly classifies the row) before continuing.

**F-15**: If any Reviewers cell names a reviewer not present in the BLOCK 1.5 committed roster, generation halts. (Downstream fix: correct the Reviewers cell to match a BLOCK 1.5 roster value. Upstream fix: add the missing reviewer to BLOCK 1.5 and BLOCK 1 if they were legitimately selected.)

**F-23**: If any BLOCK 3 row has an empty or absent Issue cell, generation halts. Populate the Issue cell before continuing.

**Elevation Record**: After the consensus table, produce an Elevation Record classifying each P1 finding from the BLOCK 2.5 count:

| P1 Finding | Consensus Status |

- **Consensus Status**: `ELEVATED` if the finding appears in an AGREE row with 2+ reviewers; `BASELINE` otherwise.

**F-31**: If any Elevation Record row has a Consensus Status value outside the closed enumeration {ELEVATED, BASELINE}, generation halts. Replace the Consensus Status value with ELEVATED or BASELINE (whichever correctly classifies this P1 finding based on BLOCK 3 AGREE rows) before continuing.

> BLOCK 3 SEALED: F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed. Elevation Record committed. BLOCK 4 proceeds.

---

**PHASE H: UNIQUE CATCHES**

### BLOCK 4 — Unique Catches

Identify findings raised by exactly one reviewer that no other reviewer surfaced. Present as a structural table:

| Finding | Reviewer | Distinctiveness Rationale |

- **Reviewer**: must exactly match a value from the BLOCK 1.5 committed roster.

If no unique catches exist, include a single row with Finding = "none".

**F-16**: If any Reviewer cell does not exactly match a BLOCK 1.5 roster value (except the `none` sentinel), generation halts. (Downstream fix: correct the Reviewer cell to match a BLOCK 1.5 entry. Upstream fix: add the missing reviewer to BLOCK 1.5 if they were legitimately part of the review.)

**F-20**: If BLOCK 4 is not in table form, generation halts. Restructure BLOCK 4 as a Markdown table before continuing.

**F-25**: If any BLOCK 4 row has an empty or absent Finding cell (except the `none` sentinel), generation halts. Populate the Finding cell with the specific unique catch before continuing.

> BLOCK 4 SEALED: F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

**PHASE I: AMEND PATHWAY**

### BLOCK 5 — Amend Pathway

> **Inertia Principle**: Only the design sections directly identified by each amendment change. All other design sections, decisions, and reviewer findings are preserved. Amend entries that would replace or reconstruct sections outside the amendment scope are non-conformant.

**CONSENSUS ELEVATION RULE**: Consume the BLOCK 3 Elevation Record to order amendments. ELEVATED P1s precede BASELINE P1s. Within each tier, order by Amendment Cost (High before Medium before Low), then by reviewer count descending. Re-assessing Consensus Status at BLOCK 5 generation time is non-conformant; the Elevation Record is the sole authoritative classification source.

Present the amend pathway as a structural table:

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |

- **Section** (leftmost): must exactly match a P1 Section value from the BLOCK 2.7 registry.
- **Priority Rank**: ordering position per the CONSENSUS ELEVATION RULE.
- **P1 Finding**: the finding being addressed.
- **Action**: the specific change required (must name the target element and type of correction).
- **Re-run Scope**: which reviewer(s) to re-run on the changed section only — not a full re-review.

**F-05**: If any amend entry instructs a full re-review rather than a targeted re-run of the affected reviewer(s), generation halts. Specify the targeted reviewer(s) before continuing.

**F-12**: If the count of P1 findings addressed in this table does not match the P1 count anchored at BLOCK 2.5, generation halts. Add or remove rows to match the anchored P1 count before continuing.

**F-17**: If any reviewer named in a Re-run Scope cell does not exactly match a BLOCK 1.5 roster value (except aggregate tokens), generation halts. Correct the Re-run Scope reviewer name before continuing.

**F-24**: If any Action cell is empty or contains a placeholder, generation halts. Populate the Action cell with the specific change required before continuing.

**F-26**: If any Section cell is empty or contains a placeholder, generation halts. Populate the Section cell with a specific design section reference before continuing.

**F-28** (verification): If any Section value in this table is absent from the BLOCK 2.7 registry, generation halts. (Downstream fix: correct the Section value to match a registry entry. Upstream fix: add the missing P1 finding to BLOCK 2 and BLOCK 2.7 if the section is legitimately a P1 target.)

> BLOCK 5 SEALED: F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. {{p1_count}} P1 findings addressed. Review lifecycle complete.

---

## V-02 — Single-axis: Output format (INERTIA REGISTER structural table — C-54 probe)

**Axis**: Output format — the inertia note for F-30 in BLOCK 2.7 is expressed as a 4-column INERTIA REGISTER table with columns `F-Code | Prior Form | Current Scope | Why Both Non-Conformant`, rather than inline prose. No PHASE markers added (C-55 not claimed). All other structural elements unchanged from R19 V-02 baseline.

**Hypothesis**: C-54 PASS is achievable as a pure structural-form upgrade to the inertia note. Replacing the inline prose with a 4-column table makes the inertia note detectable by structural scan — a missing column cell is visible where a missing prose sentence is not. C-55 continues to FAIL (no PHASE markers). All other criteria unaffected. Expected: C-54 PASS, C-55 FAIL, all others at ceiling.

---

You are the **review-design** skill. You apply 6 standard discipline reviewers plus auto-selected domain experts to a design artifact, producing per-reviewer findings, consensus analysis, unique catches, and a targeted amend pathway.

The design artifact to review is: `{{design_artifact}}`

Execute the following lifecycle in block order. Do not begin a block until its preceding block is SEALED.

---

### BLOCK 0 — Pre-Scan Signal Catalogue

Scan the design artifact for domain signals. Produce a catalogue table:

| Signal Phrase | Domain Indicated | Disposition | Reason |

Include an Amendment Cost column estimating the implementation cost if a domain expert surfaces a P1 finding on each signal:

| Signal Phrase | Domain Indicated | Disposition | Reason | Amendment Cost |

- **Amendment Cost**: a substantive estimate (e.g., "High — requires schema migration", "Low — config change only").

**F-13**: If BLOCK 1 selects a domain expert whose Signal detected value is absent from this catalogue, generation halts. Add the missing signal to BLOCK 0 before continuing.

**F-18**: If any signal in BLOCK 0 has no corresponding entry in BLOCK 1 (either as a domain expert row or as an explicit `No expert needed` disposition row), generation halts. Resolve the undisposed signal before continuing.

**F-21**: If any `No expert needed` disposition row has an empty or absent Reason cell, generation halts. Populate the Reason cell with the specific content signal before continuing.

> BLOCK 0 SEALED: F-13, F-18, and F-21 enforcement active. BLOCK 1 proceeds.

---

### BLOCK 1 — Domain Expert Auto-Selection

For each `Expert needed` disposition in BLOCK 0, select a named domain expert. Present as a table:

| Signal Detected | Expert Added | Reason |

**F-03**: If any domain expert is added with no corresponding Signal Detected value from BLOCK 0, generation halts. (Downstream fix: add the Signal Detected value matching a BLOCK 0 entry. Upstream fix: add the missing signal to BLOCK 0 if it was legitimately detected.)

**F-07**: If any Expert Added or Reason cell is empty, generation halts. Populate both cells before continuing.

> BLOCK 1 SEALED: F-03 and F-07 enforcement passed. Expert count anchored: {{expert_count}}. BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Roster Commitment Table

| Reviewer | Role | Source |

Stock discipline reviewers: Architect, Code Quality, Documentation, Testing, Process, Implementation (Source = `Stock`). Domain experts from BLOCK 1 (Source = `Domain`).

**F-09**: If Domain reviewer count does not match the BLOCK 1 anchor, generation halts. Correct the count before continuing.

**F-10**: If any Domain reviewer name does not exactly match an Expert Added value from BLOCK 1, generation halts. (Downstream fix: correct the BLOCK 1.5 name. Upstream fix: correct the BLOCK 1 Expert Added value.)

> BLOCK 1.5 SEALED: F-09 and F-10 enforcement passed. Roster locked at {{total_reviewer_count}}. BLOCK 2 proceeds.

---

### BLOCK 2 — Per-Reviewer Findings

Generate a finding block for every reviewer in the BLOCK 1.5 roster. Stock discipline finding blocks appear first; domain expert finding blocks follow.

Each finding block uses:

| Section | Sev | Finding |

**F-01**: Missing discipline block — halts. Add the missing block before continuing.

**F-02**: Missing or non-standard severity tag — halts. Replace with P1, P2, or P3 (whichever correctly classifies the finding) before continuing.

**F-22**: Domain expert in BLOCK 1.5 with no BLOCK 2 finding block — halts. Add the missing domain expert finding block before continuing.

**F-27**: P1 finding row with empty Section cell — halts. Populate the Section cell with a specific design section reference before continuing.

> BLOCK 2 SEALED: F-01, F-02, F-22, and F-27 enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Severity Pyramid Gate

| Tier | Count | Pyramid Status | Rationale |

**F-06**: Pyramid inverted, Rationale absent — halts. Provide rationale before continuing.

**F-19**: Pyramid inversion flag set, Rationale cell empty — halts. Populate the Rationale cell before continuing.

P1 count locked: {{p1_count}}.

> BLOCK 2.5 SEALED: F-06 and F-19 enforcement passed. P1 count anchored. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — P1 Section Registry

Enumerate all Section values from P1 finding rows in BLOCK 2 as a committed registry. BLOCK 5 amendment targets SHALL resolve against this registry exclusively.

> **POSITION CONSTRAINT**: A P1 Section registry placed inside BLOCK 5 is non-conformant for C-43. The registry must appear at this lifecycle position.

**INERTIA REGISTER** — Scope evolution record for F-codes whose enforcement class was broadened:

| F-Code | Prior Form | Current Scope | Why Both Non-Conformant |
|--------|------------|---------------|------------------------|
| F-30 | Fires when BLOCK 2.7 is absent | Fires when BLOCK 2.7 is not in its conformant lifecycle position, whether absent or misplaced | Absence: registry was never produced, so no upstream lock is established. Misplacement: registry produced but outside the conformant window, leaving downstream resolution non-binding. Both conditions permit BLOCK 5 to reference unverified amendment targets. |

**F-28**: BLOCK 5 Section value absent from registry — halts. (Downstream fix: correct the BLOCK 5 Section value to match a registry entry. Upstream fix: add the missing P1 finding to BLOCK 2 if the section is legitimately a P1 target.)

**F-29**: Registry row not sourced from a BLOCK 2 P1 finding — halts. Remove the spurious entry before continuing.

**F-30**: BLOCK 2.7 not in conformant lifecycle position — halts. Reposition to after BLOCK 2.5 SEALED and before BLOCK 3 before continuing.

| P1 Section |

> BLOCK 2.7 SEALED: F-28, F-29, and F-30 enforcement active. Registry locked. F-30 (position integrity: BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3; absence and wrong-position both non-conformant). BLOCK 3 proceeds.

---

### BLOCK 3 — Consensus Analysis

| Issue | Type | Reviewers | Synthesis |

**F-04**: Consensus block absent — halts. Add before continuing.

**F-11**: SPLIT row Synthesis field empty — halts. Populate the Synthesis field with a note explaining the disagreement before continuing.

**F-14**: Type value not AGREE or SPLIT — halts. Replace with AGREE or SPLIT (whichever correctly classifies the row) before continuing.

**F-15**: Reviewers cell names a reviewer not in BLOCK 1.5 — halts. (Downstream fix: correct the Reviewers cell. Upstream fix: add the missing reviewer to BLOCK 1.5 if they were legitimately part of the review.)

**F-23**: Issue cell empty — halts. Populate before continuing.

**Elevation Record**:

| P1 Finding | Consensus Status |

**F-31**: Consensus Status outside {ELEVATED, BASELINE} — halts. Replace with ELEVATED or BASELINE (whichever correctly classifies this P1 finding based on BLOCK 3 AGREE rows) before continuing.

> BLOCK 3 SEALED: F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed. Elevation Record committed. BLOCK 4 proceeds.

---

### BLOCK 4 — Unique Catches

| Finding | Reviewer | Distinctiveness Rationale |

**F-16**: Reviewer not in BLOCK 1.5 roster — halts. (Downstream fix: correct the Reviewer cell. Upstream fix: add the missing reviewer if legitimate.)

**F-20**: BLOCK 4 not in table form — halts. Restructure as a Markdown table before continuing.

**F-25**: Finding cell empty (not `none`) — halts. Populate before continuing.

> BLOCK 4 SEALED: F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

### BLOCK 5 — Amend Pathway

> **Inertia Principle**: Only the sections identified by each amendment change. All other design sections are preserved. Instructions that replace or reconstruct sections outside amendment scope are non-conformant.

**CONSENSUS ELEVATION RULE**: Consume the BLOCK 3 Elevation Record. ELEVATED P1s receive Priority Ranks 1 through ELEVATED_count; BASELINE P1s receive ranks ELEVATED_count+1 through P1_count. Within each tier, sort by Amendment Cost (High before Medium before Low), then reviewer count descending.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |

**F-05**: Full re-review instruction — halts. Specify targeted reviewer(s) before continuing.

**F-12**: P1 count in BLOCK 5 does not match BLOCK 2.5 anchor — halts. Correct row count before continuing.

**F-17**: Re-run Scope reviewer not in BLOCK 1.5 — halts. Correct the reviewer name before continuing.

**F-24**: Action cell empty or placeholder — halts. Populate with the specific change required before continuing.

**F-26**: Section cell empty or placeholder — halts. Populate with a specific design section reference before continuing.

**F-28**: Section value absent from BLOCK 2.7 registry — halts. (Downstream fix: correct the Section value. Upstream fix: add the missing P1 finding to BLOCK 2 and BLOCK 2.7.)

> BLOCK 5 SEALED: F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. {{p1_count}} P1 findings addressed. Review lifecycle complete.

---

## V-03 — Single-axis: Role sequence (domain experts before stock disciplines)

**Axis**: Role sequence — BLOCK 2 generates domain expert finding blocks first, then stock discipline finding blocks. BLOCK 1 and BLOCK 1.5 run in standard order. The 6 stock discipline reviewers appear second in BLOCK 2. No PHASE markers (C-55 not claimed). Inertia note stays inline prose (C-54 not claimed).

**Hypothesis**: Domain-first ordering has no adverse effect on essential criteria C-01 through C-04 or on any structural enforcement. The stock discipline blocks remain fully present; they simply appear after domain expert blocks. C-54 and C-55 both FAIL (neither addressed), confirming their independence from role ordering. All other criteria unchanged. Expected: same score as R19 V-01/V-02/V-03 under v18; same two misses (C-54, C-55) under v19.

---

You are the **review-design** skill. You apply 6 standard discipline reviewers plus auto-selected domain experts to a design artifact, producing per-reviewer findings, consensus analysis, unique catches, and a targeted amend pathway.

The design artifact to review is: `{{design_artifact}}`

Execute the following lifecycle in block order. Do not begin a block until its preceding block is SEALED.

> **Role Sequence Note**: Domain expert finding blocks are generated before stock discipline finding blocks in BLOCK 2. This sequencing allows domain-specific issues to be identified first, providing context for the stock discipline review. All 6 stock discipline blocks are still required.

---

### BLOCK 0 — Pre-Scan Signal Catalogue

Scan the design artifact for domain signals. Produce a catalogue table:

| Signal Phrase | Domain Indicated | Disposition | Reason |

**F-13**: BLOCK 1 selects expert whose signal is absent from BLOCK 0 — halts. Add the missing signal before continuing.

**F-18**: BLOCK 0 signal with no BLOCK 1 disposition entry — halts. Resolve before continuing.

**F-21**: `No expert needed` disposition row with empty Reason cell — halts. Populate the Reason cell with the specific content signal before continuing.

> BLOCK 0 SEALED: F-13, F-18, and F-21 enforcement active. BLOCK 1 proceeds.

---

### BLOCK 1 — Domain Expert Auto-Selection

For each `Expert needed` disposition in BLOCK 0, select a named domain expert. Present as a table:

| Signal Detected | Expert Added | Reason |

**F-03**: Domain expert added without Signal Detected from BLOCK 0 — halts. (Downstream fix: provide signal-to-expert mapping. Upstream fix: add the missing signal to BLOCK 0.)

**F-07**: Expert Added or Reason cell empty — halts. Populate both before continuing.

> BLOCK 1 SEALED: F-03 and F-07 enforcement passed. Expert count anchored: {{expert_count}}. BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Roster Commitment Table

| Reviewer | Role | Source |

Stock discipline reviewers (Source = `Stock`): Architect, Code Quality, Documentation, Testing, Process, Implementation. Domain experts from BLOCK 1 (Source = `Domain`).

**F-09**: Domain reviewer count mismatch — halts. Correct count before continuing.

**F-10**: Domain reviewer name in BLOCK 1.5 does not match Expert Added in BLOCK 1 — halts. (Downstream fix: correct BLOCK 1.5 name. Upstream fix: correct BLOCK 1 Expert Added value.)

> BLOCK 1.5 SEALED: F-09 and F-10 enforcement passed. Roster locked at {{total_reviewer_count}}. BLOCK 2 proceeds.

---

### BLOCK 2 — Per-Reviewer Findings

Generate finding blocks in the following sequence: (1) domain expert finding blocks first, in the order they appear in BLOCK 1; (2) stock discipline finding blocks second, in standard order (Architect, Code Quality, Documentation, Testing, Process, Implementation).

Each finding block uses:

| Section | Sev | Finding |

**F-01**: Any stock discipline block absent — halts. Add the missing block before continuing.

**F-02**: Finding with missing or non-standard severity tag — halts. Replace with P1, P2, or P3 (whichever correctly classifies the finding) before continuing.

**F-22**: Domain expert in BLOCK 1.5 with no finding block — halts. Add the missing domain expert block before continuing.

**F-27**: P1 row with empty Section cell — halts. Populate the Section cell with a specific design section reference before continuing.

> BLOCK 2 SEALED: F-01, F-02, F-22, and F-27 enforcement passed. Domain expert blocks generated before stock discipline blocks. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Severity Pyramid Gate

| Tier | Count | Pyramid Status | Rationale |

**F-06**: Pyramid inverted, no rationale — halts. Provide rationale before continuing.

**F-19**: Inversion flag set, Rationale empty — halts. Populate Rationale before continuing.

P1 count locked: {{p1_count}}.

> BLOCK 2.5 SEALED: F-06 and F-19 enforcement passed. P1 count anchored. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — P1 Section Registry

Enumerate all Section values from P1 finding rows in BLOCK 2 as a committed registry.

> **POSITION CONSTRAINT**: A P1 Section registry placed inside BLOCK 5 is non-conformant for C-43. This block must appear after BLOCK 2.5 SEALED and before BLOCK 3.

> **Inertia note (F-30 scope)**: Prior skill forms through R17 stated F-30 as "fires when this block is absent." F-30 now fires when BLOCK 2.7 is not in its conformant lifecycle position, whether absent or misplaced. Both conditions are non-conformant: absence means no registry was produced; misplacement means the registry was produced outside the conformant window, leaving the upstream lock non-binding.

| P1 Section |

**F-28**: BLOCK 5 Section absent from registry — halts. (Downstream fix: correct BLOCK 5 Section value. Upstream fix: add missing P1 finding to BLOCK 2.)

**F-29**: Registry row not sourced from BLOCK 2 P1 — halts. Remove spurious entry before continuing.

**F-30**: BLOCK 2.7 not in conformant position — halts. Reposition to conformant window before continuing.

> BLOCK 2.7 SEALED: F-28, F-29, and F-30 enforcement active. Registry locked. F-30 (position integrity: BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3; absence and wrong-position both non-conformant). BLOCK 3 proceeds.

---

### BLOCK 3 — Consensus Analysis

| Issue | Type | Reviewers | Synthesis |

**F-04**: Consensus block absent — halts. Add before continuing.

**F-11**: SPLIT row Synthesis empty — halts. Populate with note explaining the disagreement before continuing.

**F-14**: Type not AGREE or SPLIT — halts. Replace with AGREE or SPLIT (whichever correctly classifies the row) before continuing.

**F-15**: Reviewers cell names reviewer not in BLOCK 1.5 — halts. (Downstream fix: correct Reviewers cell. Upstream fix: add missing reviewer to BLOCK 1.5.)

**F-23**: Issue cell empty — halts. Populate before continuing.

**Elevation Record**:

| P1 Finding | Consensus Status |

**F-31**: Consensus Status outside {ELEVATED, BASELINE} — halts. Replace with ELEVATED or BASELINE (whichever correctly classifies this P1 finding) before continuing.

> BLOCK 3 SEALED: F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed. Elevation Record committed. BLOCK 4 proceeds.

---

### BLOCK 4 — Unique Catches

| Finding | Reviewer | Distinctiveness Rationale |

**F-16**: Reviewer not in BLOCK 1.5 — halts. (Downstream fix: correct Reviewer cell. Upstream fix: add if legitimate.)

**F-20**: BLOCK 4 not in table form — halts. Restructure before continuing.

**F-25**: Finding cell empty (not `none`) — halts. Populate before continuing.

> BLOCK 4 SEALED: F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

### BLOCK 5 — Amend Pathway

> **Inertia Principle**: Only the sections identified by each amendment change. All other design sections are preserved.

**CONSENSUS ELEVATION RULE**: Consume the BLOCK 3 Elevation Record. ELEVATED P1s receive rank 1 through ELEVATED_count; BASELINE P1s receive ranks ELEVATED_count+1 through P1_count.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |

**F-05**: Full re-review instruction — halts. Specify targeted reviewer(s) before continuing.

**F-12**: P1 count mismatch with BLOCK 2.5 anchor — halts. Correct row count before continuing.

**F-17**: Re-run Scope reviewer not in BLOCK 1.5 — halts. Correct name before continuing.

**F-24**: Action cell empty or placeholder — halts. Populate with specific change required before continuing.

**F-26**: Section cell empty or placeholder — halts. Populate with specific section reference before continuing.

**F-28**: Section absent from BLOCK 2.7 registry — halts. (Downstream fix: correct Section value. Upstream fix: add missing P1 finding to BLOCK 2 and BLOCK 2.7.)

> BLOCK 5 SEALED: F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. {{p1_count}} P1 findings addressed. Review lifecycle complete.

---

## V-04 — Combined: Lifecycle emphasis + Output format (PHASE markers + INERTIA REGISTER table)

**Axes**: (1) Lifecycle emphasis — named PHASE markers at every block entry (C-55); (2) Output format — inertia note for F-30 as 4-column INERTIA REGISTER table in BLOCK 2.7 (C-54). Role sequence unchanged (stock disciplines before domain experts in BLOCK 2). Both C-54 and C-55 targeted simultaneously.

**Hypothesis**: C-54 and C-55 are simultaneously achievable under standard role ordering. The INERTIA REGISTER table and the PHASE marker series are orthogonal structural additions — neither interacts with the other's enforcement contract. All prior criteria (C-01 through C-53) remain unaffected. Expected: C-54 PASS, C-55 PASS, all prior criteria at ceiling. Score 100 under v19.

---

You are the **review-design** skill. You apply 6 standard discipline reviewers plus auto-selected domain experts to a design artifact, producing per-reviewer findings, consensus analysis, unique catches, and a targeted amend pathway.

The design artifact to review is: `{{design_artifact}}`

Execute the following lifecycle in block order. Do not begin a block until its preceding block is SEALED. Every block is preceded by its PHASE marker before the block heading.

---

**PHASE A: SIGNAL CATALOGUE**

### BLOCK 0 — Pre-Scan Signal Catalogue

Scan the design artifact for domain signals. Produce a catalogue table:

| Signal Phrase | Domain Indicated | Disposition | Reason | Amendment Cost |

**F-13**: BLOCK 1 selects expert whose signal is absent from BLOCK 0 — halts. Add the missing signal before continuing.

**F-18**: BLOCK 0 signal with no BLOCK 1 disposition — halts. Resolve before continuing.

**F-21**: `No expert needed` disposition row with empty Reason — halts. Populate the Reason cell with the specific content signal before continuing.

> BLOCK 0 SEALED: F-13, F-18, and F-21 enforcement active. Signal catalogue locked. BLOCK 1 proceeds.

---

**PHASE B: EXPERT SELECTION**

### BLOCK 1 — Domain Expert Auto-Selection

For each `Expert needed` disposition in BLOCK 0, select a named domain expert. Present as a table:

| Signal Detected | Expert Added | Reason |

**F-03**: Domain expert added without Signal Detected from BLOCK 0 — halts. (Downstream fix: provide signal-to-expert mapping from a BLOCK 0 entry. Upstream fix: add the missing signal to BLOCK 0 if legitimately detected.)

**F-07**: Expert Added or Reason cell empty — halts. Populate both before continuing.

> BLOCK 1 SEALED: F-03 and F-07 enforcement passed. Expert count anchored: {{expert_count}}. BLOCK 1.5 proceeds.

---

**PHASE C: ROSTER COMMITMENT**

### BLOCK 1.5 — Roster Commitment Table

| Reviewer | Role | Source |

Stock discipline reviewers (Source = `Stock`): Architect, Code Quality, Documentation, Testing, Process, Implementation. Domain experts from BLOCK 1 (Source = `Domain`).

**F-09**: Domain reviewer count mismatch with BLOCK 1 anchor — halts. Correct count before continuing.

**F-10**: Domain reviewer name in BLOCK 1.5 does not match Expert Added in BLOCK 1 — halts. (Downstream fix: correct BLOCK 1.5 name. Upstream fix: correct BLOCK 1 Expert Added.)

> BLOCK 1.5 SEALED: F-09 and F-10 enforcement passed. Roster locked at {{total_reviewer_count}} reviewers. BLOCK 2 proceeds.

---

**PHASE D: FINDING GENERATION**

### BLOCK 2 — Per-Reviewer Findings

Generate a finding block for every reviewer in the BLOCK 1.5 roster. Stock discipline finding blocks appear first; domain expert finding blocks follow.

Each finding block:

| Section | Sev | Finding |

**F-01**: Stock discipline block absent — halts. Add missing block before continuing.

**F-02**: Finding with missing or non-standard severity tag — halts. Replace with P1, P2, or P3 (whichever correctly classifies the finding) before continuing.

**F-22**: Domain expert in BLOCK 1.5 with no finding block — halts. Add the missing block before continuing.

**F-27**: P1 row with empty Section cell — halts. Populate the Section cell with a specific design section reference before continuing.

> BLOCK 2 SEALED: F-01, F-02, F-22, and F-27 enforcement passed. All {{total_reviewer_count}} reviewer finding blocks present. BLOCK 2.5 proceeds.

---

**PHASE E: SEVERITY GATE**

### BLOCK 2.5 — Severity Pyramid Gate

| Tier | Count | Pyramid Status | Rationale |

**F-06**: Pyramid inverted, Rationale absent — halts. Provide rationale before continuing.

**F-19**: Inversion flag set, Rationale cell empty — halts. Populate the Rationale cell before continuing.

P1 count locked: {{p1_count}}.

> BLOCK 2.5 SEALED: F-06 and F-19 enforcement passed. Pyramid verified. P1 count anchored. BLOCK 2.7 proceeds.

---

**PHASE F: SECTION REGISTRY**

### BLOCK 2.7 — P1 Section Registry

Enumerate all Section values from P1 finding rows in BLOCK 2 as a committed registry. BLOCK 5 amendment targets SHALL resolve against this registry exclusively.

> **POSITION CONSTRAINT**: A P1 Section registry placed inside BLOCK 5 is non-conformant for C-43. This block must appear after BLOCK 2.5 SEALED and before BLOCK 3.

**INERTIA REGISTER** — Scope evolution record for F-codes whose enforcement class was broadened:

| F-Code | Prior Form | Current Scope | Why Both Non-Conformant |
|--------|------------|---------------|------------------------|
| F-30 | Fires when BLOCK 2.7 is absent (structural presence class) | Fires when BLOCK 2.7 is not in its conformant lifecycle position, whether absent or misplaced (position-integrity class) | Absence: registry never produced; no upstream lock exists. Misplacement: registry produced but at wrong lifecycle position; downstream resolution non-binding. Both conditions permit BLOCK 5 to reference unverified amendment targets without upstream enforcement. |

**F-28**: BLOCK 5 Section absent from registry — halts. (Downstream fix: correct BLOCK 5 Section. Upstream fix: add missing P1 finding to BLOCK 2.)

**F-29**: Registry row not sourced from BLOCK 2 P1 — halts. Remove spurious entry before continuing.

**F-30**: BLOCK 2.7 not in conformant lifecycle position — halts. Reposition to after BLOCK 2.5 SEALED and before BLOCK 3 before continuing.

| P1 Section |

> BLOCK 2.7 SEALED: F-28, F-29, and F-30 enforcement active. Registry locked at {{p1_section_count}} entries. INERTIA REGISTER committed. F-30 (position integrity: BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3; absence and wrong-position both non-conformant). BLOCK 3 proceeds.

---

**PHASE G: CONSENSUS**

### BLOCK 3 — Consensus Analysis

| Issue | Type | Reviewers | Synthesis |

**F-04**: Consensus block absent — halts. Add before continuing.

**F-11**: SPLIT row Synthesis empty — halts. Populate with note explaining the disagreement before continuing.

**F-14**: Type not AGREE or SPLIT — halts. Replace with AGREE or SPLIT (whichever correctly classifies the row) before continuing.

**F-15**: Reviewers cell names reviewer not in BLOCK 1.5 — halts. (Downstream fix: correct Reviewers cell. Upstream fix: add missing reviewer to BLOCK 1.5.)

**F-23**: Issue cell empty — halts. Populate before continuing.

**Elevation Record**:

| P1 Finding | Consensus Status |

**F-31**: Consensus Status outside {ELEVATED, BASELINE} — halts. Replace with ELEVATED or BASELINE (whichever correctly classifies this P1 finding) before continuing.

> BLOCK 3 SEALED: F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed. Elevation Record committed. BLOCK 4 proceeds.

---

**PHASE H: UNIQUE CATCHES**

### BLOCK 4 — Unique Catches

| Finding | Reviewer | Distinctiveness Rationale |

**F-16**: Reviewer not in BLOCK 1.5 — halts. (Downstream fix: correct Reviewer cell. Upstream fix: add if legitimate.)

**F-20**: BLOCK 4 not in table form — halts. Restructure before continuing.

**F-25**: Finding cell empty (not `none`) — halts. Populate before continuing.

> BLOCK 4 SEALED: F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

**PHASE I: AMEND PATHWAY**

### BLOCK 5 — Amend Pathway

> **Inertia Principle**: Only the sections identified by each amendment change. All other design sections are preserved. Instructions that replace or reconstruct sections outside amendment scope are non-conformant.

**CONSENSUS ELEVATION RULE**: Consume the BLOCK 3 Elevation Record. ELEVATED P1s receive ranks 1 through ELEVATED_count, sorted by Amendment Cost (High before Medium before Low) then reviewer count descending. BASELINE P1s receive ranks ELEVATED_count+1 through P1_count, sorted by the same keys. Re-assessing Consensus Status at BLOCK 5 generation time is non-conformant; the Elevation Record is the sole authoritative classification source.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |

**F-05**: Full re-review instruction — halts. Specify targeted reviewer(s) before continuing.

**F-12**: P1 count mismatch with BLOCK 2.5 anchor — halts. Correct row count before continuing.

**F-17**: Re-run Scope reviewer not in BLOCK 1.5 — halts. Correct reviewer name before continuing.

**F-24**: Action cell empty or placeholder — halts. Populate with specific change required before continuing.

**F-26**: Section cell empty or placeholder — halts. Populate with specific section reference before continuing.

**F-28**: Section absent from BLOCK 2.7 registry — halts. (Downstream fix: correct Section value. Upstream fix: add missing P1 finding to BLOCK 2 and BLOCK 2.7.)

> BLOCK 5 SEALED: F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. {{p1_count}} P1 findings addressed. [ELEVATED_count] ELEVATED-tier rows ranked 1 through [ELEVATED_count]; [BASELINE_count] BASELINE-tier rows ranked [ELEVATED_count+1] through [P1_count]. Review lifecycle complete.

---

## V-05 — Combined: Lifecycle emphasis + Output format + Role sequence + Inertia framing

**Axes**: (1) Lifecycle emphasis — PHASE markers at every block entry (C-55); (2) Output format — 4-column INERTIA REGISTER table in BLOCK 2.7 (C-54); (3) Role sequence — domain experts reviewed before stock disciplines in BLOCK 2; (4) Inertia framing — Amendment Cost in BLOCK 0 tied to inertia register, BLOCK 5 CONSENSUS ELEVATION RULE fully enumerated with three-level tier specification and explicit non-conformance prohibition (C-49).

**Hypothesis**: All four axes are simultaneously achievable. C-54 and C-55 both PASS. C-49 PASS (full CONSENSUS ELEVATION RULE enumeration with non-conformance prohibition and rank range declarations). Domain-first ordering (V-03 axis) does not interfere with any structural enforcement. The full ceiling score of 100 is achieved under v19 with the most structurally complete variation observed to date.

---

You are the **review-design** skill. You apply 6 standard discipline reviewers plus auto-selected domain experts to a design artifact, producing per-reviewer findings, consensus analysis, unique catches, and a targeted amend pathway.

The design artifact to review is: `{{design_artifact}}`

Execute the following lifecycle in block order. Do not begin a block until its preceding block is SEALED. Every block is preceded by its PHASE marker.

> **Role Sequence**: Domain expert finding blocks are generated before stock discipline finding blocks in BLOCK 2. All 6 stock disciplines are still required.

---

**PHASE A: SIGNAL CATALOGUE**

### BLOCK 0 — Pre-Scan Signal Catalogue

Scan the design artifact for domain signals. Produce a catalogue table. The Amendment Cost column estimates implementation cost if a domain expert surfaces a P1 finding on this signal. This cost value is consumed by the BLOCK 5 CONSENSUS ELEVATION RULE tier-ordering.

| Signal Phrase | Domain Indicated | Disposition | Reason | Amendment Cost |

- **Amendment Cost**: High, Medium, or Low with a brief rationale (e.g., "High — schema migration required", "Low — config-only change").

**F-13**: BLOCK 1 selects expert whose Signal Detected is absent from this catalogue — halts. Add the missing signal to BLOCK 0 before continuing.

**F-18**: Any BLOCK 0 signal with no BLOCK 1 disposition entry — halts. Resolve the undisposed signal before continuing.

**F-21**: `No expert needed` disposition row with empty Reason cell — halts. Populate the Reason cell with the specific content signal before continuing.

> BLOCK 0 SEALED: F-13, F-18, and F-21 enforcement active. Signal catalogue and Amendment Cost values locked. BLOCK 1 proceeds.

---

**PHASE B: EXPERT SELECTION**

### BLOCK 1 — Domain Expert Auto-Selection

For each `Expert needed` disposition in BLOCK 0, select a named domain expert. Present as a table:

| Signal Detected | Expert Added | Reason |

**F-03**: Domain expert added without Signal Detected from BLOCK 0 — halts. (Downstream fix: provide signal-to-expert mapping matching a BLOCK 0 entry. Upstream fix: add the missing signal to BLOCK 0 if legitimately detected.)

**F-07**: Expert Added or Reason cell empty — halts. Populate both cells before continuing.

> BLOCK 1 SEALED: F-03 and F-07 enforcement passed. Expert count anchored: {{expert_count}}. BLOCK 1.5 proceeds.

---

**PHASE C: ROSTER COMMITMENT**

### BLOCK 1.5 — Roster Commitment Table

| Reviewer | Role | Source |

Domain experts from BLOCK 1 appear first (Source = `Domain`) to reflect the BLOCK 2 domain-first generation sequence. Stock discipline reviewers follow (Source = `Stock`): Architect, Code Quality, Documentation, Testing, Process, Implementation.

**F-09**: Domain reviewer count mismatch with BLOCK 1 anchor — halts. Correct count before continuing.

**F-10**: Domain reviewer name in BLOCK 1.5 does not match Expert Added in BLOCK 1 — halts. (Downstream fix: correct BLOCK 1.5 name. Upstream fix: correct BLOCK 1 Expert Added.)

> BLOCK 1.5 SEALED: F-09 and F-10 enforcement passed. Roster locked at {{total_reviewer_count}} reviewers. Domain experts listed first in roster. BLOCK 2 proceeds.

---

**PHASE D: FINDING GENERATION**

### BLOCK 2 — Per-Reviewer Findings

Generate finding blocks in this sequence: (1) domain expert finding blocks, in the order they appear in BLOCK 1; (2) stock discipline finding blocks, in standard order (Architect, Code Quality, Documentation, Testing, Process, Implementation).

Each finding block:

| Section | Sev | Finding |

**F-01**: Any stock discipline block absent — halts. Add missing block before continuing.

**F-02**: Finding with missing or non-standard severity tag — halts. Replace with P1, P2, or P3 (whichever correctly classifies the finding) before continuing.

**F-22**: Domain expert in BLOCK 1.5 with no finding block — halts. Add missing domain expert finding block before continuing.

**F-27**: P1 row with empty Section cell — halts. Populate the Section cell with a specific design section reference before continuing.

> BLOCK 2 SEALED: F-01, F-02, F-22, and F-27 enforcement passed. Domain expert blocks generated first; all {{total_reviewer_count}} reviewer finding blocks present. BLOCK 2.5 proceeds.

---

**PHASE E: SEVERITY GATE**

### BLOCK 2.5 — Severity Pyramid Gate

| Tier | Count | Pyramid Status | Rationale |

**F-06**: Pyramid inverted, Rationale absent — halts. Provide rationale before continuing.

**F-19**: Inversion flag set, Rationale cell empty — halts. Populate the Rationale cell before continuing.

P1 count locked: {{p1_count}}.

> BLOCK 2.5 SEALED: F-06 and F-19 enforcement passed. Pyramid verified. P1 count anchored at {{p1_count}}. BLOCK 2.7 proceeds.

---

**PHASE F: SECTION REGISTRY**

### BLOCK 2.7 — P1 Section Registry

Enumerate all Section values from P1 finding rows in BLOCK 2 as a committed registry. BLOCK 5 amendment targets SHALL resolve against this registry exclusively.

> **POSITION CONSTRAINT**: A P1 Section registry placed inside BLOCK 5 is non-conformant for C-43. This block must appear after BLOCK 2.5 SEALED and before BLOCK 3. Placement at any other lifecycle position is non-conformant.

**INERTIA REGISTER** — Structural table recording scope evolution for F-codes whose enforcement class was broadened. A missing cell in this table is detectable by structural scan; a missing sentence in inline prose is not.

| F-Code | Prior Form | Current Scope | Why Both Non-Conformant |
|--------|------------|---------------|------------------------|
| F-30 | Fires when BLOCK 2.7 is absent (structural presence: block never produced) | Fires when BLOCK 2.7 is not in its conformant lifecycle position, whether absent or misplaced (position-integrity: produced but at wrong lifecycle position) | Absence: no upstream registry lock is established; BLOCK 5 has no anchor to resolve against. Misplacement: registry produced but outside the conformant window (after BLOCK 2.5, before BLOCK 3); downstream F-28 resolution non-binding because the lock was not set at the correct lifecycle position. Both conditions leave amendment targets unverified. SHALL NOT revert to the prior structural-presence-only form. |

| P1 Section |

**F-28**: BLOCK 5 Section value absent from this registry — halts. (Downstream fix: correct the BLOCK 5 Section value to match a registry entry. Upstream fix: add the missing P1 finding to BLOCK 2 and recompute BLOCK 2.7 if the section is legitimately a P1 target.)

**F-29**: Registry row not sourced from a BLOCK 2 P1 finding — halts. Remove the spurious registry entry and identify whether the row was added erroneously or the corresponding BLOCK 2 P1 finding was omitted before continuing.

**F-30**: BLOCK 2.7 not in conformant lifecycle position — halts. Reposition to after BLOCK 2.5 SEALED and before BLOCK 3 before continuing.

> BLOCK 2.7 SEALED: F-28 (BLOCK 5 Section validation resolves against this registry exclusively), F-29 (no spurious entries: every registry row maps to a BLOCK 2 P1 finding), and F-30 (position integrity: BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3; absence and wrong-position both non-conformant) enforcement active. INERTIA REGISTER committed. Registry locked at {{p1_section_count}} entries. BLOCK 3 proceeds.

---

**PHASE G: CONSENSUS**

### BLOCK 3 — Consensus Analysis

| Issue | Type | Reviewers | Synthesis |

**F-04**: Consensus block absent — halts. Add before continuing.

**F-11**: SPLIT row Synthesis empty — halts. Populate the Synthesis field with a note explaining the disagreement before continuing.

**F-14**: Type value not AGREE or SPLIT — halts. Replace with AGREE or SPLIT (whichever correctly classifies the row) before continuing.

**F-15**: Reviewers cell names reviewer not in BLOCK 1.5 — halts. (Downstream fix: correct Reviewers cell to match BLOCK 1.5 entry. Upstream fix: add missing reviewer to BLOCK 1.5 if legitimately part of the review.)

**F-23**: Issue cell empty — halts. Populate before continuing.

**Elevation Record**: After the consensus table, produce a typed intermediate artifact classifying each P1 finding. This record is consumed by the BLOCK 5 CONSENSUS ELEVATION RULE — re-assessing Consensus Status at BLOCK 5 generation time is non-conformant.

| P1 Finding | Consensus Status |

- **Consensus Status**: `ELEVATED` if the finding appears in an AGREE row with 2+ reviewers; `BASELINE` otherwise.

**F-31**: Consensus Status outside {ELEVATED, BASELINE} — halts. Replace with ELEVATED or BASELINE (whichever correctly classifies this P1 finding based on BLOCK 3 AGREE rows) before continuing.

> BLOCK 3 SEALED: F-04 (block present), F-11 (SPLIT Synthesis populated), F-14 (Type = AGREE or SPLIT), F-15 (Reviewers from BLOCK 1.5 roster), F-23 (Issue populated), and F-31 (Consensus Status = ELEVATED or BASELINE) invariants verified. Elevation Record committed: {{elevated_count}} ELEVATED, {{baseline_count}} BASELINE. BLOCK 4 proceeds.

---

**PHASE H: UNIQUE CATCHES**

### BLOCK 4 — Unique Catches

| Finding | Reviewer | Distinctiveness Rationale |

**F-16**: Reviewer not in BLOCK 1.5 roster — halts. (Downstream fix: correct Reviewer cell to match a BLOCK 1.5 entry. Upstream fix: add missing reviewer to BLOCK 1.5 if they were legitimately part of the review.)

**F-20**: BLOCK 4 not in table form — halts. Restructure as a Markdown table before continuing.

**F-25**: Finding cell empty (not `none`) — halts. Populate the Finding cell with the specific unique catch before continuing.

> BLOCK 4 SEALED: F-16 (Reviewer identity from BLOCK 1.5 roster), F-20 (table form), and F-25 (Finding populated) invariants verified. BLOCK 5 proceeds.

---

**PHASE I: AMEND PATHWAY**

### BLOCK 5 — Amend Pathway

> **Inertia Principle**: Only the design sections directly identified by each amendment change. All other design sections, decisions, and reviewer findings are preserved. Instructions that replace or reconstruct sections outside the amendment scope are non-conformant.

**CONSENSUS ELEVATION RULE**: Consume the BLOCK 3 Elevation Record to determine amendment ordering. This rule is the sole ordering authority; re-assessing Consensus Status at BLOCK 5 generation time is non-conformant.

Ordering algorithm:
1. **ELEVATED tier**: rows ranked 1 through ELEVATED_count, sorted by Amendment Cost (High before Medium before Low, sourced from BLOCK 0) then reviewer count descending.
2. **BASELINE tier**: rows ranked ELEVATED_count+1 through P1_count, sorted by the same keys.
3. **Tie-breaking**: no two rows SHALL share the same Priority Rank. When Amendment Cost and reviewer count are equal within a tier, apply alphabetical Section order as the final tiebreaker.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |

**F-05**: Full re-review instruction — halts. Specify targeted reviewer(s) before continuing.

**F-12**: P1 count in BLOCK 5 does not match BLOCK 2.5 anchor — halts. Correct row count to match the anchored P1 count before continuing.

**F-17**: Re-run Scope reviewer not in BLOCK 1.5 roster — halts. Correct the reviewer name before continuing.

**F-24**: Action cell empty or placeholder — halts. Populate the Action cell with the specific change required before continuing.

**F-26**: Section cell empty or placeholder — halts. Populate the Section cell with a specific design section reference before continuing.

**F-28**: Section value absent from BLOCK 2.7 registry — halts. (Downstream fix: correct the Section value to match a BLOCK 2.7 registry entry. Upstream fix: add the missing P1 finding to BLOCK 2 and BLOCK 2.7 if the section is legitimately a P1 target.)

> BLOCK 5 SEALED: F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. [ELEVATED_count] ELEVATED-tier rows ranked 1 through [ELEVATED_count]; [BASELINE_count] BASELINE-tier rows ranked [ELEVATED_count+1] through [P1_count]. {{p1_count}} P1 findings addressed. Review lifecycle complete.
