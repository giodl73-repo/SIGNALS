---
skill: quest-rubric
skill_target: listen-support
date: 2026-03-15
version: 1
---

# Rubric: listen-support

Scoring rubric for the `listen-support` skill, which predicts the top support tickets filed in the first 90 days after a feature ships.

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (must all pass)

### C-01 -- Ticket Inventory Present
- **Weight**: essential
- **Category**: correctness
- **Text**: The output contains a numbered list of predicted support tickets, each with at minimum: a title, a category drawn from {how-to, bug, feature-request, config, integration}, a predicted volume drawn from {high, medium, low}, and a severity drawn from {P0, P1, P2, P3}.
- **Pass condition**: Every ticket entry includes all four required fields with values from the specified enumerations. Zero tickets with missing or out-of-enumeration values.

---

### C-02 -- Persona Attribution Per Ticket
- **Weight**: essential
- **Category**: correctness
- **Text**: Each predicted ticket identifies a specific persona as the most likely filer, drawn from the stock roles: Support, SRE, PM, UX, or C-01 through C-12. The persona choice is plausible given the ticket category and severity.
- **Pass condition**: Every ticket has a named persona. No generic attributions such as "user" or "developer" without a role qualifier. At least two distinct personas appear across the full ticket list.

---

### C-03 -- Sample Ticket Body in Persona Voice
- **Weight**: essential
- **Category**: correctness
- **Text**: Each ticket includes a sample ticket body written in first person from the attributed persona's perspective. The body describes a concrete problem or question, not a generic placeholder.
- **Pass condition**: Every ticket body is at least two sentences, written in first person, and uses language consistent with the persona's role (e.g., SRE body uses operational vocabulary; C-01 through C-12 bodies reflect end-user confusion, not engineering language).

---

### C-04 -- Gap Analysis Produced
- **Weight**: essential
- **Category**: coverage
- **Text**: The output includes a gap analysis section with at least one entry each for: documentation gaps, design gaps, and operational gaps. Each gap entry names the gap, which ticket(s) it relates to, and what artifact or action would close it.
- **Pass condition**: All three gap categories are present and non-empty. Each gap entry references at least one ticket by ID or title. Generic gaps that could apply to any feature without specificity do not count.

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
- **Text**: The output predicts between 6 and 12 distinct support tickets. Fewer than 6 underfits the 90-day window; more than 12 dilutes prioritization value.
- **Pass condition**: Ticket count is in [6, 12] inclusive.

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

## Scoring Summary Table

| ID   | Criterion                           | Weight        | Category    |
|------|-------------------------------------|---------------|-------------|
| C-01 | Ticket inventory present            | essential     | correctness |
| C-02 | Persona attribution per ticket      | essential     | correctness |
| C-03 | Sample ticket body in persona voice | essential     | correctness |
| C-04 | Gap analysis produced               | essential     | coverage    |
| C-05 | Volume/severity distribution        | essential     | correctness |
| C-06 | Ticket count in useful range        | recommended   | depth       |
| C-07 | Cross-persona coverage              | recommended   | coverage    |
| C-08 | Gap actionability                   | recommended   | depth       |
| C-09 | Ticket clustering and themes        | aspirational  | depth       |
| C-10 | Ticket lifecycle and resolution     | aspirational  | depth       |

---

## Scoring Worked Example

Suppose an output passes C-01, C-02, C-03, C-05 (4 of 5 essential), C-06 and C-07 (2 of 3 recommended), and C-09 (1 of 2 aspirational):

```
essential_pass   = 4/5 = 0.80  ->  0.80 * 60 = 48.0
recommended_pass = 2/3 = 0.67  ->  0.67 * 30 = 20.0
aspirational_pass = 1/2 = 0.50 ->  0.50 * 10 =  5.0
composite = 73.0
```

C-04 (gap analysis) failed -> essential gate not met -> not golden even though composite is 73.

All essential criteria must pass for golden status.
