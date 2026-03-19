Rubric v3 written. Here's what changed:

**5 new aspirational criteria (C-14 — C-18):**

| ID | Pattern | Pass Condition |
|----|---------|----------------|
| C-14 | AMEND as proof validator | AMEND must explicitly prescribe C-12 reduction rerun on any focus shift — "update the finding" alone fails |
| C-15 | Inline anchor tag before proof block | Named SOURCE/ANCHOR slot must appear *before* the reduction arguments, not after |
| C-16 | Gate failure naming | Instruction must name the error state ("gate failure") not just the positive rule |
| C-17 | WHITESPACE grounded by attribute absence | Gap finding must name which specific attributes across which rows confirm no ownership — not bare assertion |
| C-18 | NOT ACCEPTABLE examples for anchoring | Instruction must include a concrete negative exemplar ("Competitor X reveals..." = NOT ACCEPTABLE), not just an abstract prohibition |

**Scoring changes:**
- Aspirational tier: 5 → 10 criteria, max 25 → 50
- Max composite: 115 → 140
- Formula denominator: `aspirational_pass / 10 × 50`
- Grade bands rescaled proportionally: Exceptional ≥ 131, Strong ≥ 118, Passing ≥ 90 (golden threshold unchanged)
 in a trailing section. If no focus is provided, this criterion passes by vacuous satisfaction. |
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

## Aspirational Criteria (weight = 50 points total, 5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires the competitive map and the focus dimension together. A finding that merely cites both dimensions without demonstrating that either alone is insufficient does not pass. |
| C-10 | Table-stakes grounding per finding | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Positive instruction alone does not ensure this passes — the output must demonstrate that ungrounded findings are absent. |
| C-11 | Fully-cited competitor table | correctness | Every external competitor row (not just one) includes an inline citation from a WebSearch result. The citation appears within the row or immediately adjacent entry — not in a footnote or trailing references section. This extends C-07 from minimum-one to all-external. |
| C-12 | Self-negating cross-dimensional finding | depth | The CROSS-DIMENSIONAL or equivalent whitespace finding explicitly argues why the finding cannot be derived from the competitive map alone and why it cannot be derived from the focus dimension alone. The output provides or implies the single-dimension reduction for each — showing what is lost when either dimension is removed — rather than just asserting cross-dimensionality. |
| C-13 | Claim-level finding anchors | depth | Each finding references a specific cell value, column value, or row-level attribute from a named competitor entry — not just the competitor name. For example: citing Competitor X's specific threat rating, mechanism sentence, or focus-column value as the evidentiary basis. Findings grounded only by competitor name ("Competitor X reveals...") do not satisfy; findings grounded by a specific claim within that row do. |
| C-14 | AMEND as proof validator | behavior | The AMEND section requires that any adjustment shifting the focus dimension must rerun both single-dimension reductions (C-12 proofs) for the updated CROSS-DIMENSIONAL finding. A standalone instruction to "update the finding" does not satisfy — the explicit rerun of both reduction arguments must be prescribed. |
| C-15 | Inline anchor tag before proof block | format | The proof block or cross-dimensional finding structure declares a named evidentiary source slot (e.g., SOURCE:, ANCHOR:, or equivalent label) before the reduction arguments are written. The evidentiary source is identified first; the proof follows. Constructing the argument before naming the evidence does not satisfy. |
| C-16 | Gate failure naming | format | The skill instruction names the error condition explicitly (e.g., "gate failure," "citation gate violation," or equivalent) rather than only describing the rule in positive terms. Naming the failure state makes the gate concrete and checkable; a rule stated only as a positive requirement does not satisfy. |
| C-17 | WHITESPACE grounded by attribute absence | depth | The WHITESPACE finding grounds the identified gap by naming specific attributes from competitor rows that are absent or uncontested across the table — not by assertion alone. The gap is evidenced by what is missing at the attribute level across named rows, not by a claim that no competitor owns the space. |
| C-18 | NOT ACCEPTABLE examples for anchoring | format | The skill instruction includes at least one explicit NOT ACCEPTABLE example that names the most common inadequate-but-compliant form — such as name-only anchoring ("Competitor X reveals..."). The example must name the failure pattern specifically; an abstract prohibition without a concrete negative exemplar does not satisfy. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-18 | 5 | 50 |
| **Max composite** | | | **140** |

**Composite formula:**
```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 10 x 50)
```

PARTIAL scores count as 0.5 for numerator purposes.

**Golden threshold:** All 5 essential pass AND composite >= 90

**Grade bands:**

| Score | Grade |
|-------|-------|
| 131 -- 140 | Exceptional |
| 118 -- 130 | Strong |
| 90 -- 117 | Passing |
| < 90 | Below bar |

Grade bands rescaled proportionally from v2 (v2 max = 115; v3 max = 140). Exceptional threshold
preserved at ~94% of max; Strong threshold at ~84% of max; Passing at golden threshold (90).

---

## Criterion Rationale (v2 additions)

**Why C-11 (Fully-cited table) over C-07 alone:**
Round 1 showed that requiring one citation is insufficient -- models satisfy C-07 with a single
verified claim and coast on unverified characterizations for all other rows. C-11 closes this
gap: WebSearch must be run per external competitor, not just once.

**Why C-12 (Self-negating cross-dimensional finding):**
C-09 scored PARTIAL in every variation across Round 1. The common failure: variations required
the finding to *cite* both dimensions but not to *prove* single-dimension insufficiency. C-12
makes the exclusion test explicit and output-level -- the finding must demonstrate what is lost
when either dimension is removed, not merely assert it draws on both.

**Why C-13 (Claim-level anchors) over C-10 alone:**
C-10 requires findings to name a competitor row. C-13 requires findings to name a specific
*claim within* that row -- a threat rating, mechanism sentence, or focus-column value. The
upgrade matters because "Competitor X reveals a gap" is technically grounded but epistemically
empty: the reader cannot verify the inference without re-reading the full row. Claim-level
anchors make inferences checkable in one glance.

---

## Criterion Rationale (v3 additions)

**Why C-14 (AMEND as proof validator):**
V-05 (Round 2) showed that encoding C-12 in the static CROSS-DIMENSIONAL block is insufficient
if AMEND allows the user to shift the focus dimension without re-running both reductions. The
proof degrades silently after adjustment. Requiring AMEND to prescribe the full reduction rerun
propagates C-12 compliance across every iteration, not just the initial invocation.

**Why C-15 (Inline anchor tag before proof block):**
Round 2 analysis showed that models construct reduction proofs first and name evidence
incidentally -- or not at all. Declaring a named SOURCE or ANCHOR slot before the argument
forces the evidentiary basis to be resolved before the proof is assembled. This prevents
circular proof construction where the conclusion implicitly selects its own evidence.

**Why C-16 (Gate failure naming):**
Positive-only rule framing ("every row must have a citation") leaves the error state
implicit. When a gate is violated, the model has no named failure mode to report against.
Naming the failure state explicitly ("citation gate failure -- do not output the row")
makes gates self-enforcing: the model can produce a structured error rather than silently
violating the rule.

**Why C-17 (WHITESPACE grounded by attribute absence):**
C-04 requires the whitespace finding to exist. C-13 requires findings to anchor to
specific attributes. C-17 applies claim-level anchoring specifically to the WHITESPACE
finding: the gap must be shown to be vacant by naming which attributes across which rows
confirm no competitor owns it. Asserting "no competitor covers this space" without
attribute-level evidence is the WHITESPACE analogue of the name-only anchoring failure.

**Why C-18 (NOT ACCEPTABLE examples):**
V-03 and V-05 (Round 2) showed that ACCEPTABLE/NOT ACCEPTABLE example pairs are the
single most reliable mechanism for eliminating the name-only anchoring escape hatch.
Abstract prohibitions ("findings must cite a specific attribute") are consistently
interpreted as satisfied by naming the competitor. A NOT ACCEPTABLE example naming the
exact inadequate form ("Competitor 2 reveals that...") closes the interpretation gap.

---

## Summary of Changes

**v2 -> v3:**
- C-14 added -- AMEND must prescribe C-12 proof rerun on focus shift (not just output update)
- C-15 added -- proof block must declare evidentiary source slot before reduction arguments
- C-16 added -- gate instructions must name the failure state, not only the positive rule
- C-17 added -- WHITESPACE finding must ground the gap in attribute-level absence across rows
- C-18 added -- skill instruction must include a NOT ACCEPTABLE exemplar for name-only anchoring
- Aspirational tier expands from 5 to 10 criteria; aspirational max moves from 25 to 50
- Max composite moves from 115 to 140
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 131, Strong >= 118, Passing >= 90
