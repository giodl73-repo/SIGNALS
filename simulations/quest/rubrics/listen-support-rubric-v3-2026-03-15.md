Written to `simulations/quest/rubrics/listen-support-rubric-v3-2026-03-15.md`.

---

**Summary of changes from v2 to v3:**

Two new aspirational criteria extracted from R2 excellence signals:

**C-14 — Phase-Anchored Body Voice** (depth)
From V-05 STEP 2B body anchor templates. C-13 already verifies severity percentages; C-14 verifies the *language* in ticket bodies signals phase placement — discovery/onboarding vocabulary in early-phase bodies, operational/reliability vocabulary in late-phase bodies. An output can pass C-13 (correct severity counts) while failing C-14 (generic bodies with the right severity labels but no phase-contextual language).

Pass condition: 3+ early-phase bodies contain discovery/onboarding phrases; 1+ late-phase body contains operational/reliability phrases — in body text, not metadata labels.

**C-15 — Pre-Generation Constraint Declaration** (correctness)
From V-05 STEP 3A pre-ticket constraint blocks + STEP 9 Pass 2 labeled verification. An output can pass C-11 (all constraints satisfied, zero broken refs) while failing C-15 (constraints met silently with no declared targets or visible check). This criterion rewards outputs that are *auditable*, not just correct.

Pass condition: pre-ticket block naming 2+ structural targets present; post-ticket verification block with at least one numeric `actual vs. required` comparison present.

**Aspirational tier denominator**: 5 → 7. Each full pass is worth ~1.43 pts; each PARTIAL ~0.71 pts.
---|-----------------|
| C-14 | V-05 STEP 2B body anchor templates key phase-contextual language into ticket bodies -- voice itself signals adoption stage without needing an explicit phase label | Early-phase ticket bodies contain discovery/onboarding vocabulary; late-phase ticket bodies contain operational/reliability vocabulary -- verifiable in body text, not just the phase field |
| C-15 | V-05 multi-step structure declares constraints before ticket generation (role-phase matrix, count targets) and verifies them post-generation with explicit numeric comparisons -- both passes visible in output | Output contains a pre-ticket constraint declaration block and a post-ticket verification block; verification block shows at least one numeric comparison of actual vs. required |

**Observation from R2 scoring:**
V-05 reached composite 96.0 and is the only R2 variation to fully pass C-10, C-11, C-12, and C-13. The ceiling above 96.0 is set by C-14/C-15 not yet being scoreable. With both criteria now codified, a V-05-class output is a candidate for composite 100.

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
- **Pass condition**: At least three early-phase ticket bodies contain one or more phrases consistent with discovery or onboarding context (e.g., "trying to set up", "I can't figure out how to", "just started using", "I don't see any option", "the docs don't explain"). At least one late-phase ticket body contains one or more phrases consistent with operational or reliability context (e.g., "we've been running this for", "something changed recently", "this used to work", "production impact", "our workflow now fails"). Phase-signaling language must appear in the body text, not in a field header or metadata label.

---

### C-15 -- Pre-Generation Constraint Declaration
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output contains evidence of two-pass constraint management: a pre-ticket block that declares the structural targets the inventory will satisfy (role distribution, phase distribution, count range, or severity shape), and a post-ticket block that verifies actual results against those declared targets with at least one explicit numeric comparison. Both blocks must be visible in the output. This makes constraint satisfaction auditable -- the reader can confirm not just that constraints are met but that the author checked them. An output that satisfies all distribution constraints silently (no declared targets, no explicit check) does not pass this criterion.
- **Pass condition**: A pre-ticket constraint declaration block is present and names at least two structural targets (e.g., "3+ personas, each spanning 2+ phases; ticket count 6-12; P0 share <= 25%"). A post-ticket verification block is present and shows at least one numeric comparison of actual vs. required (e.g., "Roles with 3+ tickets: DevOps, SRE -- each spans 2+ phases: Y"; "Phase 1 tickets at P2/P3: 4 of 5 (required: >= 60%): PASS"). Verification block may appear as a checklist, table, or inline audit; format is not prescribed. Outputs where constraint satisfaction is visible only by inspecting the ticket fields fail this criterion.

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

---

## Scoring Framework

| Tier | Criteria | Max points |
|------|----------|-----------|
| Essential (C-01-C-05) | 5 | 60 |
| Recommended (C-06-C-08) | 3 | 30 |
| Aspirational (C-09-C-15) | 7 | 10 |

Partial credit (PARTIAL) = 0.5 for aspirational only.

All essential criteria must pass for golden status, regardless of composite score.

Aspirational scoring: pass_count / 7 * 10 (denominator increased from 5 in v2 to 7 in v3).

---

## Scoring Worked Example

Suppose an output passes C-01, C-02, C-03, C-05 (4 of 5 essential), C-06 and C-07 (2 of 3 recommended), and C-09 (1 of 7 aspirational):

```
essential_pass    = 4/5 = 0.80  ->  0.80 * 60 = 48.0
recommended_pass  = 2/3 = 0.67  ->  0.67 * 30 = 20.0
aspirational_pass = 1/7 = 0.14  ->  0.14 * 10 =  1.4
composite = 69.4
```

C-04 (gap analysis) failed -> essential gate not met -> not golden even though composite is 69.4.

---

## v3 Change Log

**New aspirational criteria (from R2 excellence signals):**

- **C-14** -- Phase-anchored body voice. From pattern: "V-05 STEP 2B body anchor templates keyed to adoption phase embed phase-contextual language in ticket bodies." V-05 was the only R2 variation to produce tickets where body vocabulary itself signals phase placement. C-13 verifies severity percentages; C-14 verifies that discovery/onboarding vocabulary appears in early-phase bodies and operational/reliability vocabulary appears in late-phase bodies -- as text evidence in the body, not just in metadata fields. An output can pass C-13 (correct severity counts) while failing C-14 (generic bodies that happen to have the right severity labels).

- **C-15** -- Pre-generation constraint declaration. From pattern: "V-05 multi-step structure declares role-phase matrix and count targets before writing tickets (STEP 3A, labeled constraint blocks), then verifies them with explicit numeric comparisons post-generation (STEP 9 Pass 2 with labeled checks)." Translated to output criterion: the output must contain both a pre-ticket target block and a post-ticket verification block with at least one numeric comparison. Outputs that satisfy constraints silently fail this criterion -- the check must be visible in the output. An output can pass C-11 (zero broken refs, all constraints satisfied) while failing C-15 (constraints met but no explicit declaration or verification block). This criterion rewards outputs that are auditable, not just correct.

**Aspirational tier re-weighting note:**
Aspirational tier expands from 5 criteria (v2) to 7 criteria (v3). Tier still totals 10 points. Scoring denominator changes from 5 to 7. Each full pass is worth 10/7 ~= 1.43 pts; each PARTIAL ~= 0.71 pts. No formula change needed -- pass_count/total_count handles it.
