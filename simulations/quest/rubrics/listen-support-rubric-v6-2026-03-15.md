File written. 301 lines, 21 criteria (C-01 through C-21).

---

**listen-support-rubric-v6-2026-03-15.md** written to `simulations/quest/rubrics/`.

Two new aspirational criteria extracted from R5:

**C-20 -- Headline-Level Vocabulary ID Annotation**
Source: V-01 vs V-02 C-18 differential. V-01 places the Cell ID directly in the `##` headline line (`*(Cell: SRE-P1)*`) → C-18 PASS. V-02 places the VM Row ID in a `- VM Row: ...` subline below the `##` line → C-18 PARTIAL. C-20 captures the strongest form of node-3: the ID must be in the `##` line itself. Passing C-20 implies C-18 full PASS. Pass condition: >= 75% of `##` headline lines carry the ID inline; a scorer reading only `##` lines can identify the ID without reading sublines.

**C-21 -- Complete Five-Item Pre-Flight Coverage**
Source: V-02 vs V-01 C-19 differential. V-02 validates all 5 items including inter-role register differentiation (item e); V-01 validates only 4. C-19 requires >= 3 of 5; C-21 requires all 5. C-21 is nested inside C-19: C-21 PASS implies C-19 PASS, not vice versa. Pass condition: all five items named and given individual pass/fail results; a gate checking exactly 4 items fails C-21 because item (e) is absent.

**Scoring changes:**
- Aspirational denominator: 11 → 13
- Each full pass: ~0.91 → ~0.77 pts
- V-01-class ceiling: 100.0 (v5) → 99.23 (v6)
- Composite 100 now requires C-20 + C-21: an output combining V-01 headline annotation with V-02 five-item gate
gister alignment, (e) inter-role register differentiation for at least two roles in the same phase.

**New ceiling:** V-01-class (C-01-C-20 PASS, C-21 FAIL) scores **99.23** under v6. Composite 100 requires C-20 + C-21 -- achievable by combining V-01 headline annotation with V-02 five-item gate on top of the full C-01-C-19 base.
**Aspirational denominator:** 11 -> 13. Each full pass ~= 0.77 pts; each PARTIAL ~= 0.38 pts.

```
V-01-class under v6 scoring:
  Essential:     5/5   -> 60.0
  Recommended:   3/3   -> 30.0
  Aspirational:  12/13 ->  9.23
  Composite:     99.23
```

**Observation from R5:** V-01 achieved composite 100 under v5 by placing the vocabulary ID in the `##` headline annotation, earning C-18 PASS vs V-02 PARTIAL. V-02 reached 99.55 despite the strongest C-19 gate formalism (5 items, OPEN/CLOSED binary state) because its VM Row ID appeared in a subline. An output fusing V-01 headline annotation (C-20) with V-02 five-item gate (C-21) is the candidate for composite 100 under v6.

---

## Essential Criteria (all must pass for golden)

### C-01 -- Ticket Inventory Present
- **Weight**: essential
- **Category**: correctness
- **Text**: The output contains a structured ticket inventory covering the 90-day post-launch support window. Each entry in the inventory has at minimum: a sequential ticket ID (T-NN format), a short title, an attributed persona, a volume estimate, a severity level (P0-P3), and an adoption phase assignment (early 0-30d, mid 31-60d, late 61-90d).
- **Pass condition**: A ticket inventory section is present and contains at least one ticket. Every ticket has all six required fields populated. Tickets with missing fields do not count toward the inventory total.

---

### C-02 -- Persona Attribution Per Ticket
- **Weight**: essential
- **Category**: correctness
- **Text**: Each ticket in the inventory is attributed to a named persona from the stock role set. Generic attributions such as "user" or "developer" without a role qualifier are not acceptable. The role set includes personas such as: end user, SRE, DevOps engineer, security engineer, product manager, engineering manager, and similar named roles.
- **Pass condition**: Every ticket has a named persona. No generic attributions such as "user" or "developer" without a role qualifier. At least two distinct personas appear across the full ticket list.

---

### C-03 -- Sample Ticket Body in Persona Voice
- **Weight**: essential
- **Category**: correctness
- **Text**: Each ticket includes a sample ticket body written in first person from the attributed persona's perspective. The body describes a concrete problem or question, not a generic placeholder. First-person voice is mandatory: use "I", "my", "we". Third-person role references such as "the user", "the SRE", or "the developer" are prohibited in ticket bodies.
- **Pass condition**: Every ticket body is at least two sentences, written in first person ("I" / "my" / "we"), and uses language consistent with the persona's role (e.g., SRE body uses operational vocabulary; end-user bodies reflect end-user confusion, not engineering language). Any ticket body containing a third-person role reference in place of first-person voice fails this criterion.

---

### C-04 -- Gap Analysis Produced
- **Weight**: essential
- **Category**: coverage
- **Text**: The output includes a gap analysis section with at least one entry each for: documentation gaps, design gaps, and operational gaps. Each gap entry names the gap, lists the ticket IDs it relates to using the format "Tickets: T-NN, T-NN", and states what artifact or action would close it.
- **Pass condition**: All three gap categories are present and non-empty. Every gap entry includes at least one ticket reference in the form T-NN that matches a ticket ID in the inventory. Gap entries that reference tickets by description or title only, without a T-NN identifier, do not count. Generic gaps that could apply to any feature without specificity do not count.

---

### C-05 -- Volume and Severity Distribution is Non-Trivial
- **Weight**: essential
- **Category**: correctness
- **Text**: The predicted ticket set uses more than one volume level and more than one severity level. High-volume or P0/P1 tickets are not the majority -- the distribution reflects realistic support load patterns.
- **Pass condition**: At least two distinct volume values and at least two distinct severity values appear. P0 tickets, if present, are <= 25% of total ticket count. High-volume tickets are <= 50% of total.

---

## Recommended Criteria (output is better with these)

### C-06 -- Ticket Count in Useful Range
- **Weight**: recommended
- **Category**: depth
- **Text**: The output predicts between 6 and 12 distinct support tickets. Fewer than 6 underfits the 90-day window; more than 12 dilutes prioritization value and is harder to act on.
- **Pass condition**: Ticket count is >= 6 and <= 12 inclusive. An output with 13 or more tickets fails this criterion even if all individual tickets are high quality.

---

### C-07 -- Cross-Persona Coverage
- **Weight**: recommended
- **Category**: coverage
- **Text**: The predicted tickets collectively represent at least three distinct personas from the stock role set. No single persona accounts for more than 50% of the predicted tickets.
- **Pass condition**: Three or more distinct personas appear. Dominant persona share is <= 50%.

---

### C-08 -- Gap Actionability
- **Weight**: recommended
- **Category**: depth
- **Text**: Each gap analysis entry specifies a concrete artifact or remediation action: a doc page to write, a design change to make, a runbook to create, an alert to add, etc. Specific enough that a team member could execute without further clarification.
- **Pass condition**: At least 75% of gap entries include a named artifact or action. Vague entries such as "improve documentation" without specifics do not count.

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

### C-09 -- Ticket Clustering and Theme Identification
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output groups related tickets into 2-3 named themes (e.g., "onboarding friction," "rate-limit confusion," "integration setup failures") and explains what the cluster reveals about product risk. Theme analysis appears above or alongside the individual ticket list.
- **Pass condition**: At least two named themes present. Each theme contains two or more tickets. The theme description identifies the underlying product or doc failure generating the cluster.

---

### C-10 -- Ticket Lifecycle and Resolution Path
- **Weight**: aspirational
- **Category**: depth
- **Text**: For each high-volume or P0/P1 ticket, the output includes a predicted resolution path: the team or role that would triage it, the likely root cause category, and whether resolution is self-serve (doc fix), escalation (eng fix), or structural (design change).
- **Pass condition**: All high-volume and all P0/P1 tickets include a resolution path entry with all three fields: triage owner, root cause category, resolution type.

---

### C-11 -- Multi-Stage Structural Integrity
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output is internally consistent as if validated at multiple checkpoints: the ticket inventory is complete and well-formed before the gap analysis references it; every gap entry uses T-NN identifiers that resolve to actual tickets in the inventory; and volume, severity, persona, and count constraints are all satisfied simultaneously -- not just individually. No constraint passes in isolation while another fails.
- **Pass condition**: Zero broken T-NN references in gap entries. Zero tickets in the inventory whose fields push any distribution constraint (P0 share, high-vol share) past its limit. The inventory and gap analysis agree as a unified artifact.

---

### C-12 -- Role-Phase Compound Coverage
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Per-persona ticket counts are distributed across at least two adoption phases (early 0-30d, mid 31-60d, late 61-90d), preventing compound concentration where one persona's tickets all cluster in a single phase. Each persona that appears three or more times must have tickets in at least two distinct phases.
- **Pass condition**: For every persona with three or more tickets, those tickets span at least two adoption phases. A persona's full ticket set residing in a single phase window fails this criterion.

---

### C-13 -- Phase-Calibrated Severity
- **Weight**: aspirational
- **Category**: depth
- **Text**: Ticket severity reflects the natural adoption lifecycle without needing explicit percentage overrides: early-phase tickets (day 0-30) reflect discovery confusion and trend toward P2/P3; late-phase tickets (day 60-90) include at least one operational or data-integrity failure at P0/P1. The severity profile tells a coherent story about how support burden evolves as the feature matures.
- **Pass condition**: At least 60% of early-phase tickets are P2 or P3. At least one late-phase ticket is P0 or P1. The overall severity distribution satisfies C-05 as a consequence of phase calibration, not as a separate correction.

---

### C-14 -- Phase-Anchored Body Voice
- **Weight**: aspirational
- **Category**: depth
- **Text**: Ticket bodies contain vocabulary that signals which adoption phase the ticket belongs to, independent of any phase field or label. Early-phase bodies use discovery and onboarding language -- expressions of confusion, first-time setup, inability to locate or understand. Late-phase bodies use operational and reliability language -- expressions of regression, production impact, previously-working behavior now broken. The voice itself dates the ticket without needing an explicit phase marker. A ticket that has a "Phase: Early" label but a generic body does not pass. Scoring evidence must be found in the body text.
- **Pass condition**: At least three early-phase ticket bodies contain one or more phrases consistent with discovery or onboarding context (e.g., "trying to set up", "I cannot figure out how to", "just started using", "I don't see any option", "the docs don't explain"). At least one late-phase ticket body contains one or more phrases consistent with operational or reliability context (e.g., "we have been running this for", "something changed recently", "this used to work", "production impact", "our workflow now fails"). Phase-signaling language must appear in the body text, not in a field header or metadata label.

---

### C-15 -- Pre-Generation Constraint Declaration
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output contains evidence of two-pass constraint management: a pre-ticket block that declares the structural targets the inventory will satisfy (role distribution, phase distribution, count range, or severity shape), and a post-ticket block that verifies actual results against those declared targets with at least one explicit numeric comparison. Both blocks must be visible in the output. This makes constraint satisfaction auditable -- the reader can confirm not just that constraints are met but that the author checked them. An output that satisfies all distribution constraints silently (no declared targets, no explicit check) does not pass this criterion.
- **Pass condition**: A pre-ticket constraint declaration block is present and names at least two structural targets (e.g., "3+ personas, each spanning 2+ phases; ticket count 6-12; P0 share <= 25%"). A post-ticket verification block is present and shows at least one numeric comparison of actual vs. required (e.g., "Roles with 3+ tickets: DevOps, SRE -- each spans 2+ phases: Y"; "Phase 1 tickets at P2/P3: 4 of 5 (required: >= 60%): PASS"). Verification block may appear as a checklist, table, or inline audit; format is not prescribed. Outputs where constraint satisfaction is visible only by inspecting the ticket fields fail this criterion.

---

### C-16 -- Per-Ticket Vocabulary Pre-Commitment
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Before writing each ticket body, the output commits to the opening phrase for that ticket in a visible per-ticket table. The table binds ticket ID to committed phrase before body writing occurs. The ticket body must then begin with its committed phrase, making the vocabulary choice verifiable by inspection. This provides a structural guarantee for C-14: where C-14 checks body text evidence (outcome), C-16 checks the pre-commitment mechanism (process). An output can pass C-14 by instruction-following without a commitment table; C-16 requires the table itself to be present. An output can also fail C-14 while passing C-16 if the committed phrases are not phase-appropriate -- the two criteria are orthogonal. Outputs where phase-appropriate vocabulary appears in bodies but no commitment table exists fail this criterion even if C-14 passes.
- **Pass condition**: A per-ticket vocabulary commitment table is present in the output with at least one row per ticket. Each row shows the ticket ID and the committed opening phrase for that ticket body. Each ticket body begins with its committed phrase, verifiable by cross-referencing body openings against the table. A commitment table with fewer rows than the total ticket count fails this criterion. A commitment table present but not referenced in body text (bodies do not begin with committed phrases) fails this criterion.

---

### C-17 -- Role-Phase Vocabulary Matrix
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output contains a role-phase vocabulary matrix (or equivalent register table) that specifies vocabulary register for each role-x-phase combination independently. This extends C-14 from a 1D phase constraint to a 2D role-x-phase constraint: the vocabulary in ticket bodies must be both phase-appropriate (C-14) and role-appropriate (this criterion). An SRE body in Phase-1 uses different register than an end-user body in Phase-1 -- both have discovery/onboarding vocabulary (satisfying C-14) but the SRE register is technical and setup-oriented ("I am configuring the integration") while the end-user register is confusion-oriented ("I cannot figure out what this does"). Late-phase cells similarly differ: SRE Phase-3 uses reliability and regression language; end-user Phase-3 uses habituation or frustration language. An output can pass C-14 (has phase-appropriate vocabulary in bodies) while failing C-17 (same generic discovery phrases across all roles, no role differentiation within phases). Scoring evidence requires the matrix to exist as a visible artifact in the output and ticket bodies to reflect role-phase cell vocabulary.
- **Pass condition**: A role-phase vocabulary matrix or register table is present covering at least two distinct roles and two distinct phases (minimum 4 cells). Each cell contains a vocabulary register description, example phrase, or sentence scaffold that is distinct from adjacent cells (not merely a label copy). At least one early-phase cell shows differentiation between two roles in that phase. Ticket bodies for each role use vocabulary consistent with their assigned role-phase matrix cell when cross-referenced.

---

### C-18 -- Vocabulary Planning Artifact Linkage
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When both a vocabulary matrix (C-17) and a vocabulary commitment table (C-16) are present, the two artifacts share a named identifier scheme that binds them. Each commitment table row carries an identifier (Cell ID, VM Row ID, or equivalent) that directly references its source cell or row in the vocabulary matrix. Ticket body headers cite this shared identifier. The result is a three-node chain -- matrix cell -> commitment row -> body header -- each link verifiable by ID lookup rather than by reading phrase text. An output that has both artifacts present and both correct but uses no shared identifier scheme (tracing requires phrase-text matching) fails this criterion. Distributed per-role vocabulary tables without shared IDs across tables do not satisfy this criterion even if each individual table is correct.

  C-16, C-17, and C-18 are orthogonal:
  - Pass C-16 + C-17, fail C-18: both artifacts present and correct, but no shared ID -- auditing requires phrase-text matching
  - Pass C-18, fail C-16: shared IDs present, but commitment table rows missing or bodies do not open with committed phrases
  - Pass C-18, fail C-17: shared IDs present, but matrix covers fewer than 2 roles x 2 phases

- **Pass condition**: Both a vocabulary matrix (C-17) and a commitment table (C-16) are present. Each row of the commitment table includes an explicit named identifier (e.g., Cell ID "R1-P1", VM Row ID "VM-SRE-P1") that references its source entry in the vocabulary matrix. At least 75% of ticket body headers cite a vocabulary identifier that resolves to both the commitment row and the matrix cell via ID lookup. A scorer can trace any ticket body to its matrix cell in two ID lookups without reading body text.

---

### C-19 -- Multi-Criteria Vocabulary Pre-Flight Gate
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output includes a pre-flight check block specifically for the vocabulary planning layer, positioned before ticket body generation begins. The gate validates that the vocabulary planning artifacts (matrix, commitment table) are complete and consistent with the ticket inventory before body generation proceeds. This is structurally distinct from C-15, which targets structural pre-declaration of ticket count, persona distribution, and severity shape plus a post-generation numeric verification block. C-19 targets the vocabulary artifacts that serve C-14, C-16, and C-17 simultaneously, and must gate body generation rather than follow it. An output that embeds vocabulary checks inside a general post-generation verification block does not pass C-19 -- the gate must appear before body generation, not after.

  C-15 and C-19 are orthogonal:
  - Pass C-15, fail C-19: structural pre-declaration + post-generation verification present, but no vocabulary pre-flight gate before body generation
  - Pass C-19, fail C-15: vocabulary pre-flight gate present, but no structural distribution pre-declaration or post-generation numeric verification block

- **Pass condition**: A pre-flight check block is present in the output before ticket body generation. The block explicitly validates at least three of: (a) vocabulary matrix completeness -- all role-phase combinations in the ticket inventory have a corresponding matrix cell, (b) commitment table completeness -- row count equals ticket count, (c) phrase-to-cell traceability -- each committed phrase references its source matrix entry by ID, (d) phase-register alignment -- committed phrases are consistent with the ticket's phase-appropriate register, (e) inter-role differentiation -- at least two roles in the same phase have distinct committed registers. The block must reference the vocabulary planning artifacts (matrix, commitment table, or their named sections) by name. Body generation follows the pre-flight check in output order. A vocabulary planning block that describes intended vocabulary without checking completeness against the inventory does not pass this criterion.

---

### C-20 -- Headline-Level Vocabulary ID Annotation
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The vocabulary ID (Cell ID, VM Row ID, or equivalent) appears directly in the `##` ticket headline line as an inline annotation -- not in a metadata subline below the heading. Pattern: `## T-NN -- {Title} *(Cell: XX-P#)*`. V-01 places the Cell ID in the `##` headline and achieves C-18 PASS. V-02 places the VM Row ID in a `- VM Row: {ID}` subline below the `##` line and achieves C-18 PARTIAL. C-20 is a strict refinement of C-18 node-3: passing C-20 implies full C-18 PASS; failing C-20 is consistent with C-18 PARTIAL. The structural guarantee is zero-subline tracing: a scorer reading only the `##` lines of ticket sections can verify node-3 of the vocabulary chain without descending into sublines or body text at all.

  C-18 and C-20 relationship:
  - Pass C-20: ID is in the `##` headline line -> C-18 PASS (full, not partial) implied
  - Pass C-18, fail C-20: ID is in a metadata subline -> C-18 may be PARTIAL; C-20 requires headline placement
  - Fail C-18: no shared ID scheme -> C-20 also fails

- **Pass condition**: At least 75% of ticket section `##` headline lines contain the vocabulary ID as an inline annotation embedded on the same line as the `##` marker. Accepted formats: parenthetical inline `*(Cell: XX-P#)*`, bracket inline `[VM-SRE-P1]`, or any inline marker that is part of the `##` heading text itself. A metadata subline (`- VM Row: ...`, `> Cell: ...`, `**Cell ID:** ...`, or any text on a line other than the `##` line) does not satisfy this criterion regardless of its content or proximity to the heading. A scorer reading only `##` lines in the output (no sublines, no body text) must be able to identify the vocabulary ID for >= 75% of tickets.

---

### C-21 -- Complete Five-Item Pre-Flight Coverage
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The vocabulary pre-flight gate (C-19) covers all five constraint items, not the minimum three required for C-19. V-02 validates all 5 items including inter-role register differentiation (item e); V-01 validates 4 of 5 (omits item e). C-19 requires >= 3 of 5 to pass; C-21 requires exactly 5 of 5. C-21 is a strict refinement of C-19: passing C-21 implies C-19 PASS, but C-19 PASS (with 3 or 4 items) does not imply C-21 PASS. The structural guarantee added by item (e) is that inter-role vocabulary differentiation is verified as a constraint before bodies are written, not just visible in the matrix. An output whose pre-flight gate checks items (a) through (d) but omits inter-role differentiation fails C-21 even if it passes C-19 and C-17.

  C-19 and C-21 relationship:
  - Pass C-21: all 5 items checked -> C-19 PASS implied
  - Pass C-19 (3 or 4 items), fail C-21: vocabulary gate present but incomplete coverage
  - Fail C-19: no pre-flight gate -> C-21 also fails

- **Pass condition**: The pre-flight gate block (C-19-compliant: present before body generation, referencing artifacts by name, with a blocking declaration) explicitly validates all five of the following items with individual named results: (a) vocabulary matrix completeness -- all role-phase combinations in the ticket inventory have a corresponding matrix cell; (b) commitment table completeness -- row count equals total ticket count; (c) phrase-to-cell traceability -- each committed phrase references its source matrix entry by named ID; (d) phase-register alignment -- committed phrases for each ticket are consistent with their phase-appropriate register as specified in the matrix; (e) inter-role register differentiation -- at least two roles assigned to the same phase have committed phrases with demonstrably distinct vocabulary registers (not lexical variants of the same phrase). Each item must be named explicitly (not implied by aggregate count) and given an individual pass/fail determination. A gate that checks exactly 4 items -- including all four items that V-01 covers -- fails C-21 because item (e) is absent.

---

## Scoring Summary Table

| ID   | Criterion                                   | Weight        | Category    | Added |
|------|---------------------------------------------|---------------|-------------|-------|
| C-01 | Ticket inventory present                    | essential     | correctness | v1    |
| C-02 | Persona attribution per ticket              | essential     | correctness | v1    |
| C-03 | Sample ticket body in persona voice         | essential     | correctness | v1 + first-person mandate v2 |
| C-04 | Gap analysis produced                       | essential     | coverage    | v1 + T-NN cross-ref v2 |
| C-05 | Volume/severity distribution                | essential     | correctness | v1    |
| C-06 | Ticket count in useful range                | recommended   | depth       | v1 + explicit <= 12 v2 |
| C-07 | Cross-persona coverage                      | recommended   | coverage    | v1    |
| C-08 | Gap actionability                           | recommended   | depth       | v1    |
| C-09 | Ticket clustering and themes                | aspirational  | depth       | v1    |
| C-10 | Ticket lifecycle and resolution             | aspirational  | depth       | v1    |
| C-11 | Multi-stage structural integrity            | aspirational  | correctness | v2    |
| C-12 | Role-phase compound coverage                | aspirational  | coverage    | v2    |
| C-13 | Phase-calibrated severity                   | aspirational  | depth       | v2    |
| C-14 | Phase-anchored body voice                   | aspirational  | depth       | v3    |
| C-15 | Pre-generation constraint declaration       | aspirational  | correctness | v3    |
| C-16 | Per-ticket vocabulary pre-commitment        | aspirational  | correctness | v4    |
| C-17 | Role-phase vocabulary matrix                | aspirational  | depth       | v4    |
| C-18 | Vocabulary planning artifact linkage        | aspirational  | correctness | v5    |
| C-19 | Multi-criteria vocabulary pre-flight gate   | aspirational  | correctness | v5    |
| C-20 | Headline-level vocabulary ID annotation     | aspirational  | correctness | v6    |
| C-21 | Complete five-item pre-flight coverage      | aspirational  | correctness | v6    |

---

## Scoring Framework

| Tier | Criteria | Max points |
|------|----------|------------|
| Essential (C-01-C-05) | 5 | 60 |
| Recommended (C-06-C-08) | 3 | 30 |
| Aspirational (C-09-C-21) | 13 | 10 |

Partial credit (PARTIAL) = 0.5 for aspirational only.

All essential criteria must pass for golden status, regardless of composite score.

Aspirational scoring: (pass_count + 0.5 * partial_count) / 13 * 10 (denominator increased from 11 in v5 to 13 in v6).

---

## Scoring Worked Example

Suppose an output passes C-01, C-02, C-03, C-05 (4 of 5 essential), C-06 and C-07 (2 of 3 recommended), and C-09 (1 of 13 aspirational):

```
essential_pass    = 4/5 = 0.80  ->  0.80 * 60 = 48.0
recommended_pass  = 2/3 = 0.67  ->  0.67 * 30 = 20.0
aspirational_pass = 1/13 = 0.08 ->  0.08 * 10 =  0.8
composite = 68.8
```

C-04 (gap analysis) failed -> essential gate not met -> not golden even though composite is 68.8.

---

## v6 Change Log

**New aspirational criteria (from R5 excellence signals):**

- **C-20** -- Headline-level vocabulary ID annotation. From pattern: V-01 achieves C-18 PASS because the Cell ID appears in the `##` headline annotation `*(Cell: SRE-P1)*`. V-02 achieves C-18 PARTIAL because the VM Row ID appears in a metadata subline `- VM Row: VM-SRE-P1` below the `##` line. The R5 scorecard notes scorers must still read the metadata line for V-02, while V-01 enables zero-subline tracing -- a scorer reading only `##` lines can verify node-3 of the vocabulary chain. C-18 requires body headers to cite the ID; C-20 requires the cite in the `##` headline line itself. Passing C-20 implies C-18 full PASS (not partial). An output whose vocabulary IDs appear only in sublines passes C-18 PARTIAL but fails C-20.

- **C-21** -- Complete five-item pre-flight coverage. From pattern: V-02 validates all 5 C-19 items including inter-role register differentiation (item e). V-01 validates 4 of 5 -- items (a) through (d) -- but omits item (e). C-19 requires >= 3 of 5; the 4-item pattern leaves inter-role differentiation unverified before body generation. C-21 closes that gap: all 5 items must be checked with individual named pass/fail results. An output passing C-19 with exactly 4 items (the V-01 pattern) fails C-21 because item (e) is absent. V-02 gate language (GATE: OPEN -- all 5 items PASS -- proceed to STEP 4) demonstrates the pattern; V-01 PRE-FLIGHT RESULT: ALL PASS covers only 4.

**Aspirational tier re-weighting note:** Tier expands from 11 criteria (v5) to 13 criteria (v6). Tier still totals 10 points. Denominator 11 -> 13. Each full pass = 10/13 ~= 0.77 pts; each PARTIAL ~= 0.38 pts. No formula change needed.

**Ceiling analysis:**
V-01-class output (C-01-C-20 PASS, C-21 FAIL) reaches composite 99.23 under v6.
V-02-class output (C-01-C-19 PASS, C-18 PARTIAL, C-20 FAIL, C-21 PASS) reaches composite 98.85.
Composite 100 requires C-20 PASS + C-21 PASS: combine V-01 headline annotation with V-02 five-item gate on top of the full C-01-C-19 base.
