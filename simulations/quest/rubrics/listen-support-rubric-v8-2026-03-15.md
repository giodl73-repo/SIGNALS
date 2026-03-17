Written to `simulations/quest/rubrics/listen-support-rubric-v8-2026-03-15.md`.

---

## listen-support Rubric v8 -- Change Summary

**Three new aspirational criteria extracted from R7:**

| Criterion | Source | Pattern |
|-----------|--------|---------|
| **C-25** Per-item C-21 gate evidence rows in VM | V-02 | Five individually named VM rows (one per gate item a-e) with Required/Actual/Pass? cells each, replacing the single aggregate summary row |
| **C-26** Contract enforcement site registry with precedence declaration | V-03 | RESTATING POSITIONS section names all governed sites (STEP 3B, STEP 4, VM) + precedence declaration + back-references at each site = bidirectional traceability |
| **C-27** Consequence-form criterion-citing prohibition statement | V-04 | "fails C-20 regardless of other compliance" -- names the criterion, declares criterion-level failure, adds cancellation-immunity qualifier |

**Scoring changes:**
- Denominator: 16 → 19
- Per-pass: 0.625 → 0.526 pts; PARTIAL: 0.3125 → 0.263 pts

**Key result:** No R7 variation achieves 100 under v8. V-02-class, V-03-class, and V-04-class all land at **98.95** (17/19) via different paths -- each variation excels on exactly one or two of the three new axes but not all three. V-01-class drops to **97.9** (15/19). The composite-100 path requires a variation that simultaneously combines C-25 + C-26 + C-27.
al 1. V-03 extends the R6 V-03 COMPLIANCE CONTRACT with a RESTATING POSITIONS section that names each governed enforcement site (STEP 3B, STEP 4, VERIFICATION MANIFEST) explicitly, and adds a precedence declaration: "If any restating position conflicts with this contract, this contract governs." Each named enforcement site carries a back-reference to the contract ("Per Compliance Contract above -- ..."). The result is bidirectional traceability: the contract declares which sites are governed (contract->sites forward link), and each site cites the contract by name (sites->contract back link). V-02-class retains the full R6 V-03 contract with sample header and prohibition but adds no RESTATING POSITIONS section and no precedence declaration -- it fails C-26. V-03-class adds both the registry and the precedence declaration and passes C-26. C-26 is orthogonal to C-22: C-22 requires the contract to be pre-step and contain sample + prohibition + five-item mandate; C-26 requires the contract to additionally name its enforcement sites and declare precedence. A contract can pass C-22 while failing C-26 (no registry), or have a registry without a compliant pre-step contract (fail both C-22 and C-26).

**C-27 -- Consequence-Form Criterion-Citing Prohibition Statement**
Source: V-04 Signal 1. V-04 produces the strongest prohibition language of any R7 variation: "An output with any vocabulary ID on a subline fails C-20 regardless of other compliance." This form has three structural properties absent from permission-form prohibitions ("NOT permitted on any subline"): (1) it names the specific criterion that the violation invokes ("fails C-20"); (2) it declares the failure as deterministic regardless of other passing criteria ("regardless of other compliance"); (3) it specifies the failing unit as the full output rather than the individual ticket. V-01 uses a consequence-adjacent form ("any ticket body with the VM Row ID on a subline fails") but omits the criterion citation and the "regardless" qualifier -- it fails C-27. V-02 and V-03 use permission-form only -- they fail C-27. C-27 makes the prohibition self-scoring: a scorer reading the prohibition text can identify which criterion a violation invokes without consulting the rubric.

**Scoring changes (v7 -> v8):**
- Aspirational denominator: 16 -> 19
- Each full pass: ~0.625 -> ~0.526 pts
- Each PARTIAL: ~0.3125 -> ~0.263 pts
- No R7 variation achieves composite 100 under v8
- V-02-class ceiling: 98.95 (passes C-09-C-22 + C-23 + C-24 + C-25; fails C-26 and C-27)
- V-03-class ceiling: 98.95 (passes C-09-C-24 + C-26; fails C-25 and C-27)
- V-04-class ceiling: 98.95 (passes C-09-C-24 + C-25 + C-27; fails C-22 and C-26)
- V-01-class ceiling: 97.9 (passes C-09-C-24; fails C-22 + C-25 + C-26 + C-27)
- Ideal ceiling: 100.0 (requires C-25 + C-26 + C-27 simultaneously -- no R7 variation achieves this)

```
V-02-class under v8 scoring:
  Essential:     5/5   -> 60.0
  Recommended:   3/3   -> 30.0
  Aspirational passes: C-09-C-25 = 17 of 19  (fails C-26, C-27)
  Aspirational: 17/19 ->  8.947
  Composite:     98.95

V-03-class under v8 scoring:
  Essential:     5/5   -> 60.0
  Recommended:   3/3   -> 30.0
  Aspirational passes: C-09-C-24 + C-26 = 17 of 19  (fails C-25, C-27)
  Aspirational: 17/19 ->  8.947
  Composite:     98.95

V-04-class under v8 scoring:
  Essential:     5/5   -> 60.0
  Recommended:   3/3   -> 30.0
  Aspirational passes: C-09-C-21 + C-23 + C-24 + C-25 + C-27 = 17 of 19
                       (fails C-22, C-26)
  Aspirational: 17/19 ->  8.947
  Composite:     98.95

V-01-class under v8 scoring:
  Essential:     5/5   -> 60.0
  Recommended:   3/3   -> 30.0
  Aspirational passes: C-09-C-24 = 16 of 19  (fails C-22, C-25, C-26, C-27)

  Note: V-01-class in R7 context passes C-21 and C-22 only partially.
  R7 V-01 specifically: passes C-09-C-21 + C-23 + C-24 = 15 of 19
  (fails C-22, C-25, C-26, C-27)
  Aspirational: 15/19 ->  7.895
  Composite:     97.9
```

**Observation from R7:** No single R7 variation achieves composite 100 under v8. V-02-class, V-03-class, and V-04-class all reach 98.95 by different paths through the three new aspirational criteria. The composite-100 path under v8 requires simultaneously combining: per-item VM rows (C-25, from V-02), contract enforcement site registry with precedence (C-26, from V-03), and consequence-form criterion-citing prohibition (C-27, from V-04). No R7 variation holds all three. The rubric now tracks three independent excellence axes in the compliance evidence layer -- each variation excels on one or two axes but not all three.

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
- **Text**: The vocabulary ID (Cell ID, VM Row ID, or equivalent) appears directly in the `##` ticket headline line as an inline annotation -- not in a metadata subline below the heading. Pattern: `## T-NN -- {Title} *(Cell: XX-P#)*`. C-20 is a strict refinement of C-18 node-3: passing C-20 implies full C-18 PASS; failing C-20 is consistent with C-18 PARTIAL. The structural guarantee is zero-subline tracing: a scorer reading only the `##` lines of ticket sections can verify node-3 of the vocabulary chain without descending into sublines or body text at all.

  C-18 and C-20 relationship:
  - Pass C-20: ID is in the `##` headline line -> C-18 PASS (full, not partial) implied
  - Pass C-18, fail C-20: ID is in a metadata subline -> C-18 may be PARTIAL; C-20 requires headline placement
  - Fail C-18: no shared ID scheme -> C-20 also fails

- **Pass condition**: At least 75% of ticket section `##` headline lines contain the vocabulary ID as an inline annotation embedded on the same line as the `##` marker. Accepted formats: parenthetical inline `*(Cell: XX-P#)*`, bracket inline `[VM-SRE-P1]`, or any inline marker that is part of the `##` heading text itself. A metadata subline (`- VM Row: ...`, `> Cell: ...`, `**Cell ID:** ...`, or any text on a line other than the `##` line) does not satisfy this criterion regardless of its content or proximity to the heading. A scorer reading only `##` lines in the output (no sublines, no body text) must be able to identify the vocabulary ID for >= 75% of tickets.

---

### C-21 -- Complete Five-Item Pre-Flight Coverage
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The vocabulary pre-flight gate (C-19) covers all five constraint items, not the minimum three required for C-19. C-19 requires >= 3 of 5 to pass; C-21 requires exactly 5 of 5. C-21 is a strict refinement of C-19: passing C-21 implies C-19 PASS, but C-19 PASS (with 3 or 4 items) does not imply C-21 PASS. The structural guarantee added by item (e) is that inter-role vocabulary differentiation is verified as a constraint before bodies are written, not just visible in the matrix.

  C-19 and C-21 relationship:
  - Pass C-21: all 5 items checked -> C-19 PASS implied
  - Pass C-19 (3 or 4 items), fail C-21: vocabulary gate present but incomplete coverage
  - Fail C-19: no pre-flight gate -> C-21 also fails

- **Pass condition**: The pre-flight gate block (C-19-compliant) explicitly validates all five of the following items with individual named results: (a) vocabulary matrix completeness -- all role-phase combinations in the ticket inventory have a corresponding matrix cell; (b) commitment table completeness -- row count equals total ticket count; (c) phrase-to-cell traceability -- each committed phrase references its source matrix entry by named ID; (d) phase-register alignment -- committed phrases for each ticket are consistent with their phase-appropriate register as specified in the matrix; (e) inter-role register differentiation -- at least two roles assigned to the same phase have committed phrases with demonstrably distinct vocabulary registers (not lexical variants of the same phrase). Each item must be named explicitly and given an individual pass/fail determination. A gate that checks exactly 4 items fails C-21 because item (e) is absent.

---

### C-22 -- Front-Loaded Compliance Contract
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output contains a named compliance contract block positioned before any enumerated step. The contract simultaneously declares both the vocabulary ID annotation requirement (C-20: headline-line placement, subline prohibition) and the pre-flight gate structure requirement (C-21: exactly five items, item (e) named). It provides a compliant body header sample showing the correct `##` headline format with inline vocabulary ID. This creates a two-layer architecture: the contract declares *what must be true* across the full output; steps specify *how to achieve it* at each generation site.

  C-22 is orthogonal to C-20 and C-21:
  - Pass C-22, pass C-20 + C-21: contract block present and both downstream criteria satisfied
  - Pass C-20 + C-21, fail C-22: obligations satisfied via step instructions only, no pre-step contract block
  - Pass C-22, fail C-20: contract block correctly states the rule, but execution fails

  C-22 is orthogonal to C-15 and C-19:
  - C-15 covers structural distribution (ticket count, persona share, P0 share)
  - C-19 covers the vocabulary pre-flight gate before body generation
  - C-22 covers the meta-level contract block before all steps, including before the vocabulary gate

- **Pass condition**: A named block (titled COMPLIANCE CONTRACT, FORMAT CONTRACT, VOCABULARY CONTRACT, or equivalent) appears in the output before any enumerated step. The block must contain all three of: (a) an explicit prohibition statement for vocabulary ID placement on sublines or metadata rows; (b) a compliant body header sample showing the `##` headline format with vocabulary ID inline (e.g., `## T-NN -- {Title} *(VM: VM-xxx-P#)*` or equivalent); (c) a statement mandating the pre-flight gate check exactly five items with item (e) named as "inter-role register differentiation" (or synonym). An output where C-20 and C-21 obligations appear only within step instructions -- without a pre-step named contract block -- fails C-22 even if C-20 and C-21 both pass.

---

### C-23 -- Multi-Site Subline Prohibition Anchoring
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The vocabulary ID subline prohibition is stated at a minimum of two distinct generation sites -- where "distinct" means different named steps, sections, or blocks, not two sentences within the same paragraph. Each site that produces ticket body headers must reinforce the rule, turning a single instruction into a running obligation. The VERIFICATION MANIFEST must also carry a count row that quantifies headline annotation compliance numerically; a row with a prose assertion does not satisfy this requirement.

  C-20 and C-23 relationship:
  - Pass C-23 implies the prohibition is multi-anchored, which supports but does not guarantee C-20 PASS
  - Pass C-20 with only one prohibition site fails C-23
  - Fail C-20 (IDs on sublines) and state zero prohibitions fails C-23

- **Pass condition**: The vocabulary ID subline prohibition is stated at a minimum of two distinct positions in the output. Position 1 must be a definition step or contract block. Position 2 must be a body-writing step or performance mode section. At least one statement must be a negative specification naming the prohibited format ("Not on a subline" / "NOT permitted on a metadata row" / equivalent). The VERIFICATION MANIFEST contains at least one count row that shows the numeric result of headline ID compliance (e.g., "## headlines with inline ID = N of N total tickets"). A prohibition stated in only one location fails C-23 regardless of how emphatically it is worded. A VERIFICATION MANIFEST without a headline-ID count row fails C-23 regardless of how many prohibition sites exist.

---

### C-24 -- Output-Embedded Compliance Evidence for Vocabulary Format Criteria
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The VERIFICATION MANIFEST contains explicit rows that quantify compliance with both the vocabulary annotation format (C-20) and the pre-flight gate coverage (C-21). C-15 requires the manifest to verify structural distribution constraints. C-24 requires the manifest to additionally verify vocabulary format criteria -- making compliance evidence output-embedded rather than requiring a scorer to infer it from ticket headers or gate text.

  C-15 and C-24 relationship:
  - C-24 extends C-15's manifest requirement to vocabulary format criteria; C-15 PASS is necessary but not sufficient for C-24 PASS
  - Pass C-24 implies C-15 PASS (the manifest block exists and has numeric rows)
  - Pass C-15 (structural rows only), fail C-24: manifest exists but vocabulary format rows absent

  C-24 and C-20/C-21 relationship:
  - Pass C-24 implies the output contains evidence that C-20 and C-21 were checked, but does not imply they passed
  - A manifest showing a compliant count for C-20 but no row for C-21 gives C-24 PARTIAL
  - Full C-24 PASS requires both rows to show compliant results

- **Pass condition**: The VERIFICATION MANIFEST contains at least two explicit vocabulary format rows: (1) a C-20 compliance row showing the numeric count of ticket section `##` headline lines containing the inline vocabulary ID, with an explicit pass/fail result; (2) a C-21 compliance row confirming that the pre-flight gate covered all five items (a)-(e) with pass results, with explicit reference to item (e) by name or label (e.g., "Gate items (a)-(e) all PASS -- C-21 = 5" or "Item (e) inter-role register differentiation = PASS"). Both rows must show numeric or binary results -- prose assertions do not satisfy this criterion. An output with only the C-20 manifest row and no C-21 manifest row, or vice versa, receives PARTIAL for C-24.

---

### C-25 -- Per-Item C-21 Gate Evidence Rows in Verification Manifest
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The VERIFICATION MANIFEST carries one dedicated row per C-21 gate item -- five rows total, one each for items (a) through (e) -- rather than a single aggregate summary row. Each row names its gate item explicitly and carries independent Required/Actual/Pass? cells. V-02 introduces this pattern: instead of "Gate items (a)-(e) all PASS -- C-21 = 5", the manifest carries rows `(a) VOCABULARY MANIFEST completeness -- C-21`, `(b) Commitment table completeness -- C-21`, `(c) Phrase-to-cell traceability -- C-21`, `(d) Phase-register alignment -- C-21`, `(e) Inter-role register differentiation -- C-21`, each with individual pass/fail evidence. V-03-class passes C-24 (single summary row satisfies C-24's C-21 manifest row requirement) but fails C-25 (no per-item rows). The structural guarantee is item-level accountability: a scorer can confirm or dispute the result of any individual gate item without reading the pre-flight gate block.

  C-24 and C-25 relationship:
  - Pass C-25 implies C-24 PASS: five individual rows provide richer C-21 evidence than the single summary row C-24 requires
  - Pass C-24 (single summary row), fail C-25: aggregate result present but no per-item rows
  - Fail C-24: no C-21 manifest row -> C-25 also fails

- **Pass condition**: The VERIFICATION MANIFEST contains exactly five named rows corresponding to the five C-21 pre-flight gate items. Each row: (i) names the gate item explicitly (e.g., "(a) Vocabulary matrix completeness", "(e) Inter-role register differentiation") by the same label used in the pre-flight gate block; (ii) carries a Required field, an Actual field, and a Pass? verdict field for that item independently; (iii) is a distinct row in the manifest table (not a combined row covering multiple items). A single summary row of the form "Gate items (a)-(e) all PASS -- C-21 = 5" satisfies C-24 but does not satisfy C-25 regardless of how detailed its item-label citation is. An output with four individual rows and one combined row fails C-25 because item (e) must have its own dedicated row.

---

### C-26 -- Contract Enforcement Site Registry with Precedence Declaration
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The COMPLIANCE CONTRACT (C-22-compliant pre-step named block) contains an explicit registry of all downstream enforcement sites -- named steps, sections, and blocks that carry compliance obligations derived from the contract -- and a precedence declaration stating that the contract governs if any enforcement site conflicts with it. Each named enforcement site in the output carries a back-reference to the contract by name (e.g., "Per Compliance Contract above -- ..."). The result is bidirectional traceability: the contract names its governed sites (contract->sites), and each site cites the contract (sites->contract). V-03 introduces this pattern with a RESTATING POSITIONS section naming STEP 3B, STEP 4, and the VERIFICATION MANIFEST, plus the declaration: "If any restating position conflicts with this contract, this contract governs." V-02 retains the full R6 V-03 contract but adds no RESTATING POSITIONS section and no precedence declaration -- it fails C-26. The structural guarantee is contract supremacy: a scorer seeing a conflict between a step instruction and the contract knows which governs without reading downstream steps first.

  C-22 and C-26 relationship:
  - Pass C-26 implies C-22 PASS: a contract with a registry and precedence declaration is a more complete form of the C-22-compliant pre-step contract
  - Pass C-22, fail C-26: pre-step contract with sample + prohibition + five-item mandate present, but no enforcement site registry or precedence declaration
  - Fail C-22: no compliant pre-step contract -> C-26 also fails

  C-26 is orthogonal to C-23:
  - C-23 requires multi-site prohibition anchoring with sites reinforcing the rule
  - C-26 requires the contract to name those sites explicitly and declare precedence over them
  - Pass C-23 (multi-site prohibition), fail C-26: sites reinforce the rule but the contract does not name them
  - Pass C-26 (registry present), fail C-23: contract names sites but each site does not carry independent prohibition language

- **Pass condition**: The COMPLIANCE CONTRACT block (C-22-compliant) contains a named section or sub-block -- RESTATING POSITIONS, ENFORCEMENT SITES, GOVERNED SECTIONS, or equivalent -- that lists all named steps, generation sections, and verification blocks in the output that carry obligations derived from the contract. The section must name at least three governed sites. The contract contains an explicit precedence declaration stating that the contract governs in case of conflict (e.g., "If any restating position conflicts with this contract, this contract governs" or equivalent). Each named enforcement site in the output body carries a back-reference to the contract by name. A contract with a prohibition and sample but no site registry fails C-26. A site registry without a precedence declaration fails C-26. A precedence declaration without back-references at the named sites fails C-26.

---

### C-27 -- Consequence-Form Criterion-Citing Prohibition Statement
- **Weight**: aspirational
- **Category**: correctness
- **Text**: At least one instance of the vocabulary ID subline prohibition is stated in consequence form: naming the specific criterion that a violation invokes, and declaring the failure as deterministic regardless of other passing criteria. The canonical form is: "An output with any vocabulary ID on a subline fails C-20 regardless of other compliance." This form has three structural properties absent from permission-form prohibitions ("NOT permitted on any subline"): (1) it names the specific criterion (C-20) that is violated; (2) it declares the consequence as a criterion-level failure rather than a rule breach; (3) the "regardless of other compliance" qualifier declares that no other passing criteria can cancel the failure. V-04 uses this form and produces the strongest prohibition language of any R7 variation. V-01 uses a consequence-adjacent form ("any ticket body with the VM Row ID on a subline fails") but omits the criterion citation and the "regardless" qualifier -- it fails C-27. V-02 and V-03 use permission-form only -- they fail C-27. C-27 makes the prohibition self-scoring: a scorer reading the prohibition text can identify which criterion a violation invokes without consulting the rubric.

  C-23 and C-27 relationship:
  - C-23 requires multi-site anchoring with at least one negative specification naming the prohibited format
  - C-27 requires consequence form with criterion citation at any one site -- it does not require multi-site anchoring
  - Pass C-23 (negative specification at two sites), fail C-27: multi-site prohibition uses negative specification but not consequence-form criterion citation
  - Pass C-27 (one consequence-form statement), fail C-23: consequence-form prohibition at only one site, or VERIFICATION MANIFEST lacks headline count row
  - Pass both: consequence-form prohibition with criterion citation at two or more sites

- **Pass condition**: At least one prohibition statement in the output names a specific rubric criterion (e.g., "fails C-20") as the consequence of a subline placement violation, and includes a qualifier declaring the failure as deterministic regardless of other passing criteria (e.g., "regardless of other compliance", "even if all other criteria pass", or equivalent). The statement must: (i) name the violated criterion by ID or full name; (ii) declare the output-level or ticket-level consequence as a failure (not merely a rule breach); (iii) include a qualifier that removes any ambiguity about cancellation by other passing criteria. Permission-form statements ("NOT permitted", "prohibited", "must not appear on a subline") do not satisfy C-27 regardless of how emphatically worded. Consequence-adjacent statements that use "fails" but omit the criterion ID or the "regardless" qualifier fail C-27. The consequence-form statement may appear in the COMPLIANCE CONTRACT, in a step instruction, or in a prohibition sub-block -- placement is not prescribed.

---

## Scoring Summary Table

| ID   | Criterion                                     | Weight        | Category    | Added |
|------|-----------------------------------------------|---------------|-------------|-------|
| C-01 | Ticket inventory present                      | essential     | correctness | v1    |
| C-02 | Persona attribution per ticket                | essential     | correctness | v1    |
| C-03 | Sample ticket body in persona voice           | essential     | correctness | v1 + first-person mandate v2 |
| C-04 | Gap analysis produced                         | essential     | coverage    | v1 + T-NN cross-ref v2 |
| C-05 | Volume/severity distribution                  | essential     | correctness | v1    |
| C-06 | Ticket count in useful range                  | recommended   | depth       | v1 + explicit <= 12 v2 |
| C-07 | Cross-persona coverage                        | recommended   | coverage    | v1    |
| C-08 | Gap actionability                             | recommended   | depth       | v1    |
| C-09 | Ticket clustering and themes                  | aspirational  | depth       | v1    |
| C-10 | Ticket lifecycle and resolution               | aspirational  | depth       | v1    |
| C-11 | Multi-stage structural integrity              | aspirational  | correctness | v2    |
| C-12 | Role-phase compound coverage                  | aspirational  | coverage    | v2    |
| C-13 | Phase-calibrated severity                     | aspirational  | depth       | v2    |
| C-14 | Phase-anchored body voice                     | aspirational  | depth       | v3    |
| C-15 | Pre-generation constraint declaration         | aspirational  | correctness | v3    |
| C-16 | Per-ticket vocabulary pre-commitment          | aspirational  | correctness | v4    |
| C-17 | Role-phase vocabulary matrix                  | aspirational  | depth       | v4    |
| C-18 | Vocabulary planning artifact linkage          | aspirational  | correctness | v5    |
| C-19 | Multi-criteria vocabulary pre-flight gate     | aspirational  | correctness | v5    |
| C-20 | Headline-level vocabulary ID annotation       | aspirational  | correctness | v6    |
| C-21 | Complete five-item pre-flight coverage        | aspirational  | correctness | v6    |
| C-22 | Front-loaded compliance contract              | aspirational  | correctness | v7    |
| C-23 | Multi-site subline prohibition anchoring      | aspirational  | correctness | v7    |
| C-24 | Output-embedded compliance evidence           | aspirational  | correctness | v7    |
| C-25 | Per-item C-21 gate evidence rows in VM        | aspirational  | correctness | v8    |
| C-26 | Contract enforcement site registry            | aspirational  | correctness | v8    |
| C-27 | Consequence-form criterion-citing prohibition | aspirational  | correctness | v8    |

---

## Scoring Framework

| Tier | Criteria | Max points |
|------|----------|------------|
| Essential (C-01-C-05) | 5 | 60 |
| Recommended (C-06-C-08) | 3 | 30 |
| Aspirational (C-09-C-27) | 19 | 10 |

Partial credit (PARTIAL) = 0.5 for aspirational only.

All essential criteria must pass for golden status, regardless of composite score.

Aspirational scoring: `(pass_count + 0.5 * partial_count) / 19 * 10` (denominator increased from 16 in v7 to 19 in v8).

---

## Scoring Worked Example

Suppose an output passes C-01, C-02, C-03, C-05 (4 of 5 essential), C-06 and C-07 (2 of 3 recommended), and C-09 (1 of 19 aspirational):

```
essential_pass    = 4/5 = 0.80  ->  0.80 * 60 = 48.0
recommended_pass  = 2/3 = 0.67  ->  0.67 * 30 = 20.0
aspirational_pass = 1/19 = 0.05 ->  0.05 * 10 =  0.53
composite = 68.5
```

C-04 (gap analysis) failed -> essential gate not met -> not golden even though composite is 68.5.

---

## v8 Change Log

**New aspirational criteria (from R7 excellence signals):**

- **C-25** -- Per-item C-21 gate evidence rows in Verification Manifest. Source: Signal 1, V-02 (five individually named VM rows, one per gate item). V-02 replaces the single C-21 summary row with five rows -- one each for items (a)-(e) -- each carrying Required/Actual/Pass? cells independently. V-03-class (R6 V-03 retained) passes C-24 via the single summary row but fails C-25. The structural gain: a scorer can verify any individual gate item from the manifest alone, without reading the pre-flight gate block. C-25 is a strict refinement of C-24's C-21 row requirement: passing C-25 satisfies C-24; passing C-24 does not satisfy C-25.

- **C-26** -- Contract enforcement site registry with precedence declaration. Source: Signal 1, V-03 (RESTATING POSITIONS section + precedence declaration + back-references). V-03 extends the R6 V-03 COMPLIANCE CONTRACT with an explicit registry naming STEP 3B, STEP 4, and the VERIFICATION MANIFEST as governed sites, plus the declaration: "If any restating position conflicts with this contract, this contract governs." Each named site carries "Per Compliance Contract above" back-references, creating bidirectional traceability. V-02 retains the full R6 V-03 contract but adds no RESTATING POSITIONS section -- it fails C-26. C-26 is a strict refinement of C-22: the contract that has a registry and precedence is a more complete form of the C-22-compliant contract.

- **C-27** -- Consequence-form criterion-citing prohibition statement. Source: Signal 1, V-04 (strongest prohibition language of any R7 variation). V-04 uses: "An output with any vocabulary ID on a subline fails C-20 regardless of other compliance." This form names the criterion (C-20), declares a criterion-level failure consequence, and adds a cancellation-immunity qualifier ("regardless of other compliance"). V-01 uses consequence-adjacent language ("any ticket body... fails") without naming C-20 or the "regardless" qualifier -- fails C-27. V-02 and V-03 use permission-form only ("NOT permitted") -- fail C-27. C-27 makes the prohibition self-scoring: criterion-to-prohibition tracing requires no rubric lookup. C-27 is orthogonal to C-23: C-23 requires multi-site negative specification; C-27 requires consequence form with criterion citation at any one site.

**Aspirational tier re-weighting note:** Tier expands from 16 criteria (v7) to 19 criteria (v8). Tier still totals 10 points. Denominator 16 -> 19. Each full pass = 10/19 = 0.526 pts; each PARTIAL = 0.263 pts. No formula change needed beyond denominator.

**Ceiling analysis:**
No R7 variation achieves composite 100 under v8. V-02-class (C-09-C-25 PASS, fails C-26 and C-27), V-03-class (C-09-C-24 + C-26 PASS, fails C-25 and C-27), and V-04-class (C-09-C-24 + C-25 + C-27 PASS, fails C-22 and C-26) all reach 17/19 aspirational = composite 98.95 by different paths. V-01-class (C-09-C-24 PASS for R7, fails C-22 + C-25 + C-26 + C-27) reaches 15/19 = composite 97.9. Composite 100 under v8 requires combining all three new mechanisms: per-item VM rows (C-25) + contract enforcement site registry (C-26) + consequence-form prohibition (C-27).

---

**Summary of new criteria and their R7 sources:**

| New criterion | Signal | Source variation | Differentiates |
|---------------|--------|-----------------|----------------|
| C-25 Per-item C-21 gate evidence rows | Signal 1 | V-02 | V-02/V-04 class (pass C-25) vs V-01/V-03 class (fail C-25) |
| C-26 Contract enforcement site registry | Signal 1 | V-03 | V-03 class (pass C-26) vs V-01/V-02/V-04 class (fail C-26) |
| C-27 Consequence-form criterion-citing prohibition | Signal 1 | V-04 | V-04 class (pass C-27) vs V-01/V-02/V-03 class (fail C-27) |
