# /discover-causal Variations — Round 3

---

## V-01 — Axis: Role Sequence (Inertia-First Hard Sequencing)

**Hypothesis:** Making inertia resolution a named required output before any mechanism work makes C-10 impossible to violate through output ordering alone.

---

You are running `/discover-causal`. Your job is to test whether the causal mechanism linking a feature to its claimed outcome is actually sound.

**INPUT:** A hypothesis in the form "X causes Y" — a feature and its claimed outcome.

Work through the following phases in strict order. Do not begin a phase until the prior phase's required output is written.

---

**PHASE 1 — INERTIA CHECK**

Ask and resolve: does doing nothing — no feature, no X — also produce Y?

Answer one of:
- NO — Y does not occur without X. The mechanism may be causally necessary.
- PARTIAL — Y occurs at baseline, but X modifies it along at least one dimension.
- YES — Y occurs regardless of X. The mechanism is not necessary.

Write this block before proceeding:

```
INERTIA: [NO / PARTIAL / YES]
REASONING: [one sentence explaining why]
```

Do not begin Phase 2 until this block is written.

---

**PHASE 2 — MECHANISM PATHWAY**

Trace the causal chain: how does X actually produce Y?

Requirements:
- Name at least two intermediate variables: X → M1 → M2 → Y
- Each arrow must name a process, not just assert a link
- If INERTIA was PARTIAL or YES: scope the pathway to what X contributes beyond baseline — do not trace a full chain as if inertia were NO

---

**PHASE 3 — FALSIFICATION CONDITIONS**

Name at least two conditions that would prove the mechanism wrong. For each, provide three named fields:

- **WHAT:** the specific observable that signals mechanism failure
- **HOW:** how you would measure or detect it
- **WHEN TO OBSERVE:** the point in the product lifecycle or usage cycle where this observation is possible

Vague hedges ("it might not work") do not count. Each condition must have all three fields.

---

**PHASE 4 — EVIDENCE AND CONFOUNDERS**

- **Evidence:** cite at least one piece of supporting evidence showing the mechanism has held in a comparable context — data, research, analogous feature, or domain pattern. If none exists, say so explicitly: "No prior evidence found — first-principles claim."
- **Confounders:** name at least one alternative explanation that could produce Y without X, independent of the inertia check.

---

**PHASE 5 — AMEND**

Produce an AMEND block. The amended hypothesis must:
- Be narrower and more falsifiable than the original
- Include the mechanism pathway in the claim
- Add at least one falsification condition
- If INERTIA was PARTIAL or YES: explicitly state what X contributes beyond inertia on a named dimension (speed, reliability, cost, completeness, or equivalent)

```
ORIGINAL: [the original hypothesis]
AMENDED:  [the narrowed hypothesis]
MECHANISM: [X → M1 → M2 → Y in one line]
FALSIFIES IF: [most specific falsification condition — include WHAT, HOW, WHEN TO OBSERVE]
MARGINAL CONTRIBUTION: [what X adds over doing nothing, or "N/A — inertia check was NO"]
```

---

## V-02 — Axis: Output Format (Named Artifact Table Structure)

**Hypothesis:** Requiring each phase as a named structured artifact with labeled fields forces completeness on C-14 (scope declaration), C-15 (WHEN TO OBSERVE), and C-16 (marginal dimensioning) by making omissions visually obvious.

---

You are running `/discover-causal`. Test whether the causal mechanism is sound.

**INPUT:** A hypothesis "X causes Y."

Produce five named artifacts in sequence. Each artifact is a labeled block. You may not produce Artifact N+1 until Artifact N is complete.

---

**ARTIFACT 1 — MARGINAL SCOPE DECLARATION**

```
INERTIA VERDICT:   [NO / PARTIAL / YES]
INERTIA REASONING: [one sentence]
AUTHORIZED SCOPE:  [If NO: "full mechanism." 
                    If PARTIAL: "marginal contribution only — dimensions: [list axes X affects]." 
                    If YES: "hypothesis requires revision before proceeding."]
```

You may not produce Artifact 2 until Artifact 1 is written.

---

**ARTIFACT 2 — CAUSAL CHAIN**

| Step | From | To | Mechanism (named process) |
|------|------|----|--------------------------|
| 1 | X | M1 | |
| 2 | M1 | M2 | |
| 3 | M2 | Y | |

The chain must trace at least two intermediate variables. If AUTHORIZED SCOPE was "marginal contribution only," trace only the marginal delta — not the full chain.

---

**ARTIFACT 3 — FALSIFICATION CONDITIONS**

| # | WHAT | HOW | WHEN TO OBSERVE |
|---|------|-----|-----------------|
| 1 | | | |
| 2 | | | |

Minimum two rows. Each row must be complete — a row with an empty cell does not count toward the minimum.

---

**ARTIFACT 4 — EVIDENCE AND CONFOUNDERS**

```
SUPPORTING EVIDENCE: [one cited comparable case, or "none found — first-principles claim"]

CONFOUNDERS:
| # | Alternative Explanation | Why It Could Produce Y Without X |
|---|------------------------|----------------------------------|
| 1 |                        |                                  |
```

---

**ARTIFACT 5 — AMENDED HYPOTHESIS**

```
ORIGINAL:  [original hypothesis]
AMENDED:   [narrowed, mechanism-inclusive, more falsifiable hypothesis]
MECHANISM: [X → M1 → M2 → Y — one line]
FALSIFIES IF: [most specific row from Artifact 3]
MARGINAL CONTRIBUTION:
  - [dimension 1]: [what X adds on this axis]
  - [dimension 2]: [what X adds on this axis]
  - [dimension 3 if applicable]
```

AMENDED must be more specific and falsifiable than ORIGINAL. If INERTIA was PARTIAL or YES, the MARGINAL CONTRIBUTION section must be filled — "N/A" only when INERTIA was NO.

---

## V-03 — Axis: Phrasing Register (Socratic Questioning)

**Hypothesis:** Framing the analysis as a series of questions the user must answer produces better C-12 (operationalized falsification) because each question demands a concrete answer — vague responses fail by structure, not by rubric.

---

You are running `/discover-causal`. Answer the following questions about your hypothesis in order. Each question specifies what a valid answer looks like.

**The hypothesis:** "X causes Y"

---

**Q1. Before you examine the mechanism: does Y happen anyway?**

Think through the status quo. If the team ships nothing — no X, no feature — does Y still occur through existing user behavior, natural trends, competing forces, or market dynamics?

Your answer must take one of these forms:
- "No — Y requires X to occur, because [reason]."
- "Partially — Y occurs at [level/rate] today, and X would [accelerate / improve / complete] it by [named dimension]."
- "Yes — Y would occur regardless, because [reason]."

Record this answer. Everything that follows depends on it.

---

**Q2. What is the actual mechanism?**

Do not say "X causes Y." Show the propagation: what does X do first, what does that trigger, how does that chain reach Y?

Trace at least: X → M1 → M2 → Y. Name the process at each arrow — not just the nodes.

If your Q1 answer was "Partially" or "Yes": what is the marginal mechanism — how does X produce what baseline does not already produce? Trace that specific chain, not the full unscoped pathway.

---

**Q3. What would prove the mechanism wrong?**

Name at least two falsification conditions. For each, answer three sub-questions:
1. What would you observe if the mechanism is broken?
2. How would you measure or detect that observation?
3. When in the product lifecycle or usage cycle is that observation possible?

A condition that answers fewer than all three is a worry, not a falsification condition.

---

**Q4. Is there evidence this mechanism holds?**

Has this mechanism worked in a comparable context — another feature, a domain analog, published research? If yes, cite it. If no, say explicitly: "No prior evidence found — first-principles claim."

Name at least one confounder: another force that could produce Y without X.

---

**Q5. What is the narrowed claim?**

Write an amended hypothesis that:
- Names the mechanism (not just the outcome)
- Is more falsifiable than the original
- Accounts for what X contributes beyond doing nothing (if Q1 was "Partially" or "Yes")
- Includes at least one falsification condition

The amended claim should be a sentence a skeptic can engage with — not a marketing statement.

```
ORIGINAL:  [original hypothesis]
AMENDED:   [narrowed hypothesis]
MECHANISM: [pathway in one line]
MARGINAL CONTRIBUTION: [named dimensions X adds over baseline, or "full effect — Q1 was NO"]
FALSIFIES IF: [most operationalized falsification condition, with WHAT + HOW + WHEN TO OBSERVE]
```

---

## V-04 — Axes: Inertia Framing + Lifecycle Emphasis (Scope Gate Architecture)

**Hypothesis:** Combining an explicit SCOPE DECLARATION gate with a hard structural stop — and requiring a verbatim authorized scope block before mechanism tracing — produces simultaneous passes on C-10 (ordering) and C-14 (scope artifact), because the gate cannot be skipped without the output being structurally incomplete.

---

You are running `/discover-causal`. This skill has two hard gates. You must complete each gate before the next section begins.

---

**GATE 1 — SCOPE DECLARATION**
*Complete this block before writing anything about the mechanism.*

Ask: does Y occur without X?

Grade your own answer:
- **NO** — Y is causally dependent on X. Full mechanism analysis is authorized.
- **PARTIAL** — Y occurs at baseline; X modifies it. Marginal mechanism analysis only — you may not claim full causal ownership.
- **YES** — Y does not depend on X. The hypothesis is broken. Revise the hypothesis before proceeding past Gate 1.

Produce this block verbatim:

```
SCOPE DECLARATION
──────────────────────────────────────────
Inertia Verdict:   [NO / PARTIAL / YES]
Reasoning:         [one sentence]
Authorized Scope:  [If NO: "Full mechanism."
                   If PARTIAL: "Marginal contribution only — dimensions: [list axes X affects]."
                   If YES: "Hypothesis requires revision — do not proceed."]
──────────────────────────────────────────
```

You may not begin Gate 2 until this block is written.

---

**GATE 2 — MECHANISM TRACE**
*Authorized by Scope Declaration. Do not exceed the authorized scope.*

Trace the causal pathway as authorized:
- At least two intermediate steps: X → M1 → M2 → Y
- Name the process at each arrow
- Respect the Authorized Scope — do not trace a broader chain than authorized

If Inertia Verdict was **PARTIAL**, produce two labeled chains:

```
BASELINE CHAIN:  [the mechanism that produces Y without X]
MARGINAL CHAIN:  [the mechanism for what X adds beyond baseline]
```

The AMEND section will use the MARGINAL CHAIN. The BASELINE CHAIN is context only.

---

**FALSIFICATION CONDITIONS**

Name at least two conditions that would falsify the mechanism. Required fields per condition:
- **WHAT:** observable outcome that signals mechanism failure
- **HOW:** how it is measured
- **WHEN TO OBSERVE:** lifecycle point where measurement is possible

Conditions missing any field are incomplete and do not count.

---

**EVIDENCE AND CONFOUNDERS**

- **Evidence:** one comparable case where this mechanism held, or "none found."
- **Confounders:** at least one alternative cause of Y independent of X.

---

**AMEND BLOCK**

```
ORIGINAL:  [original hypothesis]
AMENDED:   [more specific, more falsifiable]
MECHANISM: [authorized causal chain — one line]
FALSIFIES IF: [most operationalized condition — WHAT + HOW + WHEN TO OBSERVE]
MARGINAL CONTRIBUTION:
  - Dimension 1: [what X adds, direction or magnitude]
  - Dimension 2: [second axis, or "only one dimension identified"]
```

The AMENDED hypothesis must reference the Authorized Scope. An AMEND that does not address a PARTIAL inertia finding has not resolved the hypothesis.

---

## V-05 — Axes: Role Sequence + Output Format (Multi-Role Structured Deliverables)

**Hypothesis:** Assigning distinct analyst roles — each producing a named deliverable with enforced sequencing — produces fuller coverage across C-08 (multi-step chain), C-12 (operationalized falsification), and C-16 (marginal dimensioning) because each role has a narrow, unambiguous job that cannot be satisfied by vague prose.

---

You are running `/discover-causal`. Three analysts work this hypothesis in sequence. Each produces a named deliverable. Later analysts may not begin until prior deliverables are complete.

**INPUT:** hypothesis "X causes Y"

---

**ANALYST 1 — THE SKEPTIC**

Job: challenge whether X is causally necessary at all.

**Deliverable: INERTIA REPORT**

```
1. Does Y occur without X? [NO / PARTIAL / YES] — and why in one sentence.

2. If PARTIAL or YES: on which dimensions does X modify Y?
   List the axes: [speed / reliability / cost / completeness / reach / accuracy / other — name it]

3. Authorized scope for the mechanism trace:
   [If NO: "Full mechanism authorized."
    If PARTIAL: "Marginal contribution on dimensions: [list]."
    If YES: "Hypothesis does not hold — requires revision."]
```

The Skeptic's INERTIA REPORT must be complete before the Architect begins.

---

**ANALYST 2 — THE ARCHITECT**

Job: build the causal pathway authorized by the Skeptic's scope.

**Deliverable: CAUSAL CHAIN REPORT**

Rules:
- Respect the Inertia Report's Authorized Scope — do not exceed it
- Trace at least two intermediate steps: X → M1 → M2 → Y
- Name the mechanism at each arrow — "causes" does not count

If Skeptic's verdict was **PARTIAL**, produce both:

```
BASELINE CHAIN:  [mechanism that produces Y at baseline, without X]
MARGINAL CHAIN:  [mechanism for what X adds — this is the authorized scope]
```

Also produce:

```
CONFOUNDER LIST:
  1. [alternative explanation that could produce Y without X]
```

---

**ANALYST 3 — THE OBSERVER**

Job: make the mechanism falsifiable and locate evidence.

**Deliverable: FALSIFICATION AND EVIDENCE REPORT**

**Section A — Falsification Conditions** (minimum two):

| # | WHAT | HOW | WHEN TO OBSERVE |
|---|------|-----|-----------------|
| 1 | | | |
| 2 | | | |

**Section B — Evidence:**
```
[One cited comparable case, or "none found — first-principles claim."]
```

**Section C — Marginal Contribution Table** (required if Skeptic verdict was PARTIAL or YES):

| Dimension | Baseline (without X) | With X | Delta |
|-----------|---------------------|--------|-------|
| [axis 1] | | | |
| [axis 2] | | | |

---

**SYNTHESIS — AMEND BLOCK**

After all three deliverables are complete:

```
ORIGINAL:  [original hypothesis]
AMENDED:   [narrower, mechanism-inclusive, falsifiable version]
MECHANISM: [Architect's authorized causal chain — one line]
FALSIFIES IF: [Observer's most specific condition — WHAT + HOW + WHEN TO OBSERVE]
MARGINAL CONTRIBUTION: [from Observer's table, or "full effect — inertia NO"]
```

AMENDED must be visibly more falsifiable than ORIGINAL. A reviewer reading both should agree the amended version is easier to prove wrong.
