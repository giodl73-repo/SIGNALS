Written to `simulations/quest/rubrics/listen-support-rubric-v4-2026-03-15.md` (242 lines).

---

**Summary of changes from v3 to v4:**

Two new aspirational criteria, both extracted from the PARTIAL-vs-PASS divides in the R3 C-14/C-15 mechanism analysis:

---

**C-16 -- Per-Ticket Vocabulary Pre-Commitment** (correctness)

Source: The R3 scorecard shows V-02 earning only PARTIAL on C-14 despite having example phrases and a body register column. The reason: instruction-based guidance only. V-01/V-03/V-04/V-05 earn PASS because the output commits to an opening phrase per ticket in a table *before* body writing, then the body must begin with that phrase.

C-14 and C-16 are orthogonal:
- Pass C-14, fail C-16: bodies have discovery phrases, but no commitment table (instruction-following got there)
- Pass C-16, fail C-14: commitment table present, but committed phrases are not phase-appropriate

Pass condition: per-ticket commitment table with one row per ticket (ticket ID + committed phrase); each body begins with its committed phrase.

---

**C-17 -- Role-Phase Vocabulary Matrix** (depth)

Source: V-01/V-04 use a phase-only vocabulary pool (all roles in Phase-1 draw from the same pool). V-03/V-05 use a 2D role-×-phase matrix where SRE/Phase-1, EndUser/Phase-1, and SRE/Phase-3 each have distinct register. C-14 is satisfied by any discovery vocabulary in early bodies regardless of role; C-17 requires role-differentiated vocabulary within phases.

Pass condition: matrix covering 2+ roles × 2+ phases (minimum 4 cells), each cell with distinct register/example; ticket bodies traceable to their matrix cell.

---

**Aspirational tier**: 7 → 9 criteria, denominator 7 → 9. Each full pass = ~1.11 pts.

**New ceiling**: A V-04/V-05-class output (C-01–C-15 all PASS) scores **97.8** under v4. Composite 100 now requires C-16 + C-17 PASS as well -- achievable by an output combining the V-01 commitment table, V-02 manifest tables, V-03 role-phase matrix, and V-05 dual mechanism.
lary register, example phrase, or sentence scaffold distinct from adjacent cells. Ticket bodies use vocabulary consistent with their assigned role-phase cell when cross-referenced against the matrix.

**Aspirational tier denominator**: 7 -> 9. Each full pass is worth ~1.11 pts; each PARTIAL ~0.56 pts.

**Observation from R3 scoring:**
V-04 and V-05 reach composite 100 under v3 scoring by combining V-01 (vocabulary commitment table, C-14 PASS, C-16 PASS) and V-02 (manifest tables, C-15 PASS). V-03 role-phase matrix mechanism is the archetype for C-17. An output combining all five mechanisms -- per-ticket commitment table, named manifest sections, role-phase matrix, dual mechanism (template + pool), high-density verification rows -- is the candidate for composite 100 under v4.

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

## Scoring Summary Table

| ID   | Criterion                              | Weight        | Category    | Added |
|------|----------------------------------------|---------------|-------------|-------|
| C-01 | Ticket inventory present               | essential     | correctness | v1    |
| C-02 | Persona attribution per ticket         | essential     | correctness | v1    |
| C-03 | Sample ticket body in persona voice    | essential     | correctness | v1 + first-person mandate v2 |
| C-04 | Gap analysis produced                  | essential     | coverage    | v1 + T-NN cross-ref v2 |
| C-05 | Volume/severity distribution           | essential     | correctness | v1    |
| C-06 | Ticket count in useful range           | recommended   | depth       | v1 + explicit <= 12 v2 |
| C-07 | Cross-persona coverage                 | recommended   | coverage    | v1    |
| C-08 | Gap actionability                      | recommended   | depth       | v1    |
| C-09 | Ticket clustering and themes           | aspirational  | depth       | v1    |
| C-10 | Ticket lifecycle and resolution        | aspirational  | depth       | v1    |
| C-11 | Multi-stage structural integrity       | aspirational  | correctness | v2    |
| C-12 | Role-phase compound coverage           | aspirational  | coverage    | v2    |
| C-13 | Phase-calibrated severity              | aspirational  | depth       | v2    |
| C-14 | Phase-anchored body voice              | aspirational  | depth       | v3    |
| C-15 | Pre-generation constraint declaration  | aspirational  | correctness | v3    |
| C-16 | Per-ticket vocabulary pre-commitment   | aspirational  | correctness | v4    |
| C-17 | Role-phase vocabulary matrix           | aspirational  | depth       | v4    |

---

## Scoring Framework

| Tier | Criteria | Max points |
|------|----------|-----------|
| Essential (C-01-C-05) | 5 | 60 |
| Recommended (C-06-C-08) | 3 | 30 |
| Aspirational (C-09-C-17) | 9 | 10 |

Partial credit (PARTIAL) = 0.5 for aspirational only.

All essential criteria must pass for golden status, regardless of composite score.

Aspirational scoring: pass_count / 9 * 10 (denominator increased from 7 in v3 to 9 in v4).

---

## Scoring Worked Example

Suppose an output passes C-01, C-02, C-03, C-05 (4 of 5 essential), C-06 and C-07 (2 of 3 recommended), and C-09 (1 of 9 aspirational):

```
essential_pass    = 4/5 = 0.80  ->  0.80 * 60 = 48.0
recommended_pass  = 2/3 = 0.67  ->  0.67 * 30 = 20.0
aspirational_pass = 1/9 = 0.11  ->  0.11 * 10 =  1.1
composite = 69.1
```

C-04 (gap analysis) failed -> essential gate not met -> not golden even though composite is 69.1.

---

## v4 Change Log

**New aspirational criteria (from R3 excellence signals):**

- **C-16** -- Per-ticket vocabulary pre-commitment. From pattern: "V-01/V-04/V-05 STEP 2B vocabulary commitment table records the committed opening phrase per ticket before body writing; ticket body must begin with the committed phrase." R3 C-14 mechanism analysis revealed that V-02 earned only PARTIAL on C-14 because its phase vocabulary guidance was instruction-based (example phrases listed in a body register column; STEP 6 instructs vocabulary but no per-ticket structural enforcement), while V-01/V-03/V-04/V-05 earned PASS because vocabulary was committed at the per-ticket level before bodies were written. C-14 checks outcome (body text evidence); C-16 checks the mechanism (commitment table present and bodies conformant to it). The two criteria are orthogonal: an output may pass C-14 without a commitment table (instruction-following is sufficient for C-14), and an output may pass C-16 with a commitment table whose phrases happen not to be phase-appropriate (failing C-14). Both must be satisfied for highest-confidence vocabulary enforcement.

- **C-17** -- Role-phase vocabulary matrix. From pattern: "V-03 role-phase vocabulary matrix declares exact register per role-x-phase cell (SRE/Phase-1: setup-oriented; end-user/Phase-1: confusion-oriented; SRE/Phase-3: reliability/regression language). STEP 6 body instruction: begin each body with vocabulary from the assigned matrix cell." R3 C-14 mechanism analysis showed that V-01/V-04 use a phase-only vocabulary pool (all roles in Phase-1 draw from the same discovery phrase pool) while V-03/V-05 use a role-x-phase matrix (Phase-1 vocabulary differs by role). C-14 is satisfied by any discovery vocabulary in early bodies regardless of role; C-17 requires role-differentiated vocabulary within phases. An output producing ticket bodies where SRE Phase-1 and end-user Phase-1 bodies have identical register passes C-14 (both have discovery vocabulary) but fails C-17 (no role differentiation). The V-05 dual mechanism -- role-phase anchor template (structure) + committed phrase from phase vocabulary pool (vocabulary) -- satisfies both C-16 and C-17 simultaneously, making it the strongest combined enforcement.

**Aspirational tier re-weighting note:**
Aspirational tier expands from 7 criteria (v3) to 9 criteria (v4). Tier still totals 10 points. Scoring denominator changes from 7 to 9. Each full pass is worth 10/9 ~= 1.11 pts; each PARTIAL ~= 0.56 pts. No formula change needed -- pass_count/total_count handles it.

**Ceiling analysis:**
A V-04/V-05-class output passing C-01 through C-15 reaches composite 100 under v3 scoring. Under v4 scoring, the same output (C-01 through C-15 all PASS) reaches:

```
Essential:     5/5 = 1.00 -> 60.0
Recommended:   3/3 = 1.00 -> 30.0
Aspirational:  7/9 = 0.78 -> 7.8
Composite:     97.8
```

The ceiling above 97.8 requires C-16 PASS (per-ticket commitment table in output) and C-17 PASS (role-phase matrix in output). An output combining the V-01 commitment table, V-02 manifest tables, V-03 role-phase matrix, and V-05 dual mechanism is a candidate for composite 100 under v4.
