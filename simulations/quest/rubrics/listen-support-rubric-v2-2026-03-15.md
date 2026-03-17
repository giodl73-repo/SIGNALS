Written to `simulations/quest/rubrics/listen-support-rubric-v2-2026-03-15.md`.

---

**Summary of changes from v1 to v2:**

**Essential fixes (P0 — were blocking golden):**
- **C-03**: Added first-person mandate ("I"/"my"/"we") and explicit third-person prohibition. Without the prohibition, models produce compliant-looking bodies in third person.
- **C-04**: Added `Tickets: T-NN, T-NN` as a required field. Gap entries citing tickets by description only no longer count.

**Recommended tightening (P1):**
- **C-06**: `<= 12` upper bound now stated explicitly in the pass condition, not just the prose.

**New aspirational criteria from R1 excellence signals (C-11/C-12/C-13):**

| ID | Pattern source | Output criterion |
|----|----------------|-----------------|
| C-11 | Three-gate pipeline catches distinct failure classes at different stages | Inventory and gap analysis are a unified artifact — zero broken T-NN refs, no constraint passes in isolation while another fails |
| C-12 | Per-role minimums + phase binding prevents compound concentration | Any persona with 3+ tickets must span 2+ adoption phases |
| C-13 | Phase character guidance produces severity calibration without explicit % constraints | Early-phase tickets >= 60% P2/P3; at least one late-phase P0/P1 |

With P0 fixes applied to V-05 (baseline composite 75.5), expected R2 composite: ~88 — golden threshold reached.
 the ticket category and severity.
- **Pass condition**: Every ticket has a named persona. No generic attributions such as "user" or "developer" without a role qualifier. At least two distinct personas appear across the full ticket list.

---

### C-03 -- Sample Ticket Body in Persona Voice
- **Weight**: essential
- **Category**: correctness
- **Text**: Each ticket includes a sample ticket body written in first person from the attributed persona's perspective. The body describes a concrete problem or question, not a generic placeholder. First-person voice is mandatory: use "I", "my", "we". Third-person role references such as "the user", "the SRE", or "the developer" are prohibited in ticket bodies.
- **Pass condition**: Every ticket body is at least two sentences, written in first person ("I" / "my" / "we"), and uses language consistent with the persona's role (e.g., SRE body uses operational vocabulary; C-01 through C-12 bodies reflect end-user confusion, not engineering language). Any ticket body containing a third-person role reference in place of first-person voice fails this criterion.

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

## Scoring Summary Table

| ID   | Criterion                           | Weight        | Category    | Added  |
|------|-------------------------------------|---------------|-------------|--------|
| C-01 | Ticket inventory present            | essential     | correctness | v1     |
| C-02 | Persona attribution per ticket      | essential     | correctness | v1     |
| C-03 | Sample ticket body in persona voice | essential     | correctness | v1 + first-person mandate v2 |
| C-04 | Gap analysis produced               | essential     | coverage    | v1 + T-NN cross-ref v2 |
| C-05 | Volume/severity distribution        | essential     | correctness | v1     |
| C-06 | Ticket count in useful range        | recommended   | depth       | v1 + explicit <= 12 v2 |
| C-07 | Cross-persona coverage              | recommended   | coverage    | v1     |
| C-08 | Gap actionability                   | recommended   | depth       | v1     |
| C-09 | Ticket clustering and themes        | aspirational  | depth       | v1     |
| C-10 | Ticket lifecycle and resolution     | aspirational  | depth       | v1     |
| C-11 | Multi-stage structural integrity    | aspirational  | correctness | v2     |
| C-12 | Role-phase compound coverage        | aspirational  | coverage    | v2     |
| C-13 | Phase-calibrated severity           | aspirational  | depth       | v2     |

---

## Scoring Worked Example

Suppose an output passes C-01, C-02, C-03, C-05 (4 of 5 essential), C-06 and C-07 (2 of 3 recommended), and C-09 (1 of 5 aspirational):

```
essential_pass    = 4/5 = 0.80  ->  0.80 * 60 = 48.0
recommended_pass  = 2/3 = 0.67  ->  0.67 * 30 = 20.0
aspirational_pass = 1/5 = 0.20  ->  0.20 * 10 =  2.0
composite = 70.0
```

C-04 (gap analysis) failed -> essential gate not met -> not golden even though composite is 70.

All essential criteria must pass for golden status.

---

## v2 Change Log

**Essential fixes (unlocks previously blocked essential criteria):**

- **C-03** -- Added explicit first-person mandate ("I", "my", "we") and third-person prohibition ("the user", "the SRE"). Without this explicit prohibition, models produce technically compliant bodies in third person. Unlocks ~8 composite points blocked by C-03 failures in R1.
- **C-04** -- Added T-NN ticket ID cross-reference as required field in all gap entries. Gap entries referencing tickets by description or title only are now non-passing. Unlocks C-04 which was the sole essential gate failure blocking golden across all R1 variations.

**Recommended tightening:**

- **C-06** -- Made `<= 12` upper bound explicit in both prose and pass condition. The [6, 12] range was already stated in v1 but the upper bound was not called out in the pass condition text.

**New aspirational criteria (from R1 excellence signals in V-05):**

- **C-11** -- Multi-stage structural integrity. From pattern: "three-gate pipeline catches three distinct failure classes at different generation stages." Translated to output criterion: the inventory and gap analysis form a unified artifact with zero broken cross-references and no constraint isolated from the rest.
- **C-12** -- Role-phase compound coverage. From pattern: "per-role minimums combined with phase distribution binding prevents compound concentration where single-role tickets cluster in single phase window." Translated to output criterion: any persona appearing 3+ times must span 2+ phases.
- **C-13** -- Phase-calibrated severity. From pattern: "phase character guidance (Phase 1 P2/P3 / Phase 3 P0/P1) produces natural severity calibration without explicit percentage constraints." Translated to output criterion: early-phase tickets >= 60% P2/P3; at least one late-phase P0/P1.
