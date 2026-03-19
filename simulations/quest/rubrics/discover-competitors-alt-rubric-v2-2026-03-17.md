Looking at the scorecard, I can extract three distinct excellence patterns that separated high-scoring variations from lower-scoring ones:

1. **Fully-cited competitor table** (V-02/V-03 vs V-01/V-04 on C-07) — the top variations didn't just require *one* WebSearch citation; procedural gates pushed citations into every external row.
2. **Self-negating cross-dimensional finding** (C-09 PARTIAL everywhere) — no variation actually required the finding to *prove* it couldn't be derived from either dimension alone; it was always a citation condition, never an exclusion proof.
3. **Claim-level finding anchors** (C-10 PARTIAL in V-01, FAIL in V-04) — excellence required anchoring to a specific cell/value, not just a competitor name. V-02's explicit prohibition was the only version that reliably produced this.

Here is the complete updated rubric:

---

```markdown
# discover-competitors-alt — Rubric v2

## Purpose

Evaluates skill output for `discover:competitors-alt` — the unified competitive analysis skill
that combines inertia assessment, competitor mapping, optional focus dimensions, and whitespace
identification in a single invocation. This rubric is format-agnostic: it scores table-based,
narrative, phase-structured, and conversational outputs against the same criteria.

---

## Essential Criteria (weight = 60 points total, 12 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Inertia assessed first | correctness | The status quo / do-nothing competitor (Competitor 0, inertia competitor, or equivalent) appears before any external competitor. A structural position rule (first row, first phase, first narrative block) enforces this — a suggestion or prose instruction does not satisfy if the model can produce inertia mid-output. |
| C-02 | Focus woven, not appended | behavior | When a focus dimension (market sizing or positioning framework) is provided, that content is distributed throughout competitor rows, findings, and narrative — not isolated in a trailing section. If no focus is provided, this criterion passes by vacuous satisfaction. |
| C-03 | Threat level per competitor | correctness | Every named competitor and inertia receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor appears without a threat level. |
| C-04 | Whitespace identified | coverage | Output names an uncontested space or gap that no listed competitor owns — stated in its own finding or clearly labeled. |
| C-05 | Auto-detect without prompting | behavior | Topic domain is inferred from repo context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply the domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section names at least one concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — not just "inertia is high." The mechanism is specific to the status quo competitor's behavior or product feature, not a category label applied generically. |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor characterization is supported by an inline citation (URL or publication) from a WebSearch result. The citation appears within the competitor entry, not in a trailing footnote block. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output as a result. |

---

## Aspirational Criteria (weight = 25 points total, 5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires the competitive map and the focus dimension together. A finding that merely cites both dimensions without demonstrating that either alone is insufficient does not pass. |
| C-10 | Table-stakes grounding per finding | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Positive instruction alone does not ensure this passes — the output must demonstrate that ungrounded findings are absent. |
| C-11 | Fully-cited competitor table | correctness | Every external competitor row (not just one) includes an inline citation from a WebSearch result. The citation appears within the row or immediately adjacent entry — not in a footnote or trailing references section. This extends C-07 from minimum-one to all-external. |
| C-12 | Self-negating cross-dimensional finding | depth | The CROSS-DIMENSIONAL or equivalent whitespace finding explicitly argues why the finding cannot be derived from the competitive map alone and why it cannot be derived from the focus dimension alone. The output provides or implies the single-dimension reduction for each — showing what is lost when either dimension is removed — rather than just asserting cross-dimensionality. |
| C-13 | Claim-level finding anchors | depth | Each finding references a specific cell value, column value, or row-level attribute from a named competitor entry — not just the competitor name. For example: citing Competitor X's specific threat rating, mechanism sentence, or focus-column value as the evidentiary basis. Findings grounded only by competitor name ("Competitor X reveals…") do not satisfy; findings grounded by a specific claim within that row do. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 — C-05 | 12 | 60 |
| Recommended | C-06 — C-08 | 10 | 30 |
| Aspirational | C-09 — C-13 | 5 | 25 |
| **Max composite** | | | **115** |

**Composite formula:**
```
composite = (essential_pass / 5 × 60)
          + (recommended_pass / 3 × 30)
          + (aspirational_pass / 5 × 25)
```

PARTIAL scores count as 0.5 for numerator purposes.

**Golden threshold:** All 5 essential pass AND composite >= 90

**Grade bands:**

| Score | Grade |
|-------|-------|
| 108 — 115 | Exceptional |
| 97 — 107 | Strong |
| 90 — 96 | Passing |
| < 90 | Below bar |

---

## Criterion Rationale (v2 additions)

**Why C-11 (Fully-cited table) over C-07 alone:**
Round 1 showed that requiring one citation is insufficient — models satisfy C-07 with a single
verified claim and coast on unverified characterizations for all other rows. C-11 closes this
gap: WebSearch must be run per external competitor, not just once.

**Why C-12 (Self-negating cross-dimensional finding):**
C-09 scored PARTIAL in every variation across Round 1. The common failure: variations required
the finding to *cite* both dimensions but not to *prove* single-dimension insufficiency. C-12
makes the exclusion test explicit and output-level — the finding must demonstrate what is lost
when either dimension is removed, not merely assert it draws on both.

**Why C-13 (Claim-level anchors) over C-10 alone:**
C-10 requires findings to name a competitor row. C-13 requires findings to name a specific
*claim within* that row — a threat rating, mechanism sentence, or focus-column value. The
upgrade matters because "Competitor X reveals a gap" is technically grounded but epistemically
empty: the reader cannot verify the inference without re-reading the full row. Claim-level
anchors make inferences checkable in one glance.
```

---

**Summary of changes in v2:**

- C-06 tightened — mechanism must be specific to the status quo's behavior or feature, not a generic category label (closes the V-02 PARTIAL gap)
- C-09 pass condition tightened — citation of both dimensions is necessary but not sufficient; single-dimension reduction must be implied or shown
- C-11 added — extends C-07 from one citation to all external rows
- C-12 added — formalizes the self-negating exclusion proof that C-09 never fully captured
- C-13 added — upgrades C-10 from name-level to claim-level anchoring
- Max composite moves from 100 to 115; golden threshold moves from 80 to 90; grade bands rescaled proportionally
