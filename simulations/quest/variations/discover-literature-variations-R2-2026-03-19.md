Written to `simulations/quest/variations/discover-literature-variations-R2-2026-03-19.md`.

---

## discover-literature — Variations R2

### Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Anti-placeholder recovery (C-12) | Structural recovery pass checklist after table sweep — checklist format makes the step auditable and non-skippable |
| **V-02** | Per-tier acknowledgment gate (C-13) | NONE FOUND as the answer to a required question, not a fallback rule — a question cannot be unanswered |
| **V-03** | Inertia guard as PROCEED gate (C-14) | PROCEED keyword is locked until inertia scenario is named and countered — converts reminder into structural gate |
| **V-04** | Interrogative + embedded recovery (C-11+C-12) | Per-field questions embed the recovery instruction within themselves — cannot answer without performing the recovery |
| **V-05** | Full synthesis (C-11+C-12+C-13+C-14) | All four new criteria woven into V-04 R1 baseline — theoretical ceiling of the v2 rubric |

---

### Design Notes

**All variations use V-04 R1 as the baseline** (the R1 winner at 97.5/100 v1 rubric). Single-axis variations V-01, V-02, V-03 each isolate one new v2 criterion. V-04 and V-05 combine.

**V-04 R1 on the new criteria:**
- C-11 (Interrogative): PASS — already full interrogative register
- C-12 (Recovery): PARTIAL — has "search again" inline but no structural enforcement
- C-13 (Tier acknowledgment): PASS — has "NONE FOUND — explain why" blanket rule
- C-14 (Inertia guard): FAIL — no inertia scenario in gap analysis

**What each variation adds:**
- **V-01** adds a named `2b. Recovery pass` sub-step with six per-field checkboxes and explicit follow-up search instructions. The recovery is now an auditable checklist rather than an inline note.
- **V-02** restructures Phase 3 so each tier has two sequential questions: "What did I find?" + "If none found — why not?" The NONE FOUND acknowledgment becomes the forced answer to a required question rather than a fallback.
- **V-03** adds an `Inertia scenario` block inside Phase 4, positioned as a gate before the recommendation keyword. PROCEED cannot appear without naming the inertia path and countering it.
- **V-04** moves anti-placeholder recovery inside the Phase 2 questions themselves: "Who are the authors? If unknown after [search], write 'not found after secondary search — [query].'" Interrogative obligation and recovery become the same mechanism.
- **V-05** stacks all four: per-field embedded recovery (C-12), per-tier two-question gate (C-13), inertia gate on PROCEED (C-14), and enhanced interrogative density throughout (C-11).

### Projected rubric coverage

| Criterion | V-04 R1 baseline | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----------------|------|------|------|------|------|
| C-11 interrogative | PASS | same | same | same | enhanced | enhanced |
| C-12 recovery | PARTIAL | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-13 tier acknowledgment | PASS | same | **enhanced** | same | same | **enhanced** |
| C-14 inertia guard | FAIL | FAIL | FAIL | **PASS** | FAIL | **PASS** |

V-05 is the only variation that closes all four gaps. V-03 is the highest single-axis gain (turns a FAIL to PASS). V-01 and V-04 fix C-12 via different mechanisms — the scorecard should distinguish whether the checklist (V-01) or the embedded-question approach (V-04) produces better compliance in practice.
V-05 |
|-----------|-------------------|------|------|------|------|------|
| C-01 claims extracted | Phase 1 questions | same | same | same | same | same |
| C-02 citation table | Phase 2 explicit template | Phase 2a table + 2b checklist | same | same | Phase 2 per-field questions | Phase 2 per-field questions |
| C-03 four-tier map | Phase 3 four questions | same | Phase 3 two-gate per tier | same | same | Phase 3 two-gate per tier |
| C-04 gap + recommendation | Phase 4 five questions | same | same | Phase 4 + inertia gate | same | Phase 4 + inertia gate |
| C-05 artifact written | Phase 5 | same | same | same | same | same |
| C-06 contrary→claim | Q3 Phase 3 | same | Q1 CONTRARY two-gate | same | embedded in per-field Qs | Q1 CONTRARY two-gate |
| C-07 anti-placeholder | inline "search again" | recovery checklist | same inline | same inline | per-field embedded | per-field embedded |
| C-08 HIGH RISK block | Q4 Phase 4 | same | same | same | same | same |
| C-09 source threshold | no explicit check | no change | no change | no change | no change | no change |
| C-10 precedent chain | Q4 Phase 3 year confirm | same | Q1 METHODOLOGICAL two-gate | same | per-field embedded | Q1 METHODOLOGICAL two-gate |
| **C-11** interrogative | PASS | same | same | same | enhanced (per-field) | enhanced (per-field) |
| **C-12** recovery executed | PARTIAL (inline) | PASS (checklist) | PARTIAL (inline) | PARTIAL (inline) | PASS (embedded Q) | PASS (embedded Q) |
| **C-13** tier acknowledgment | PASS (NONE FOUND rule) | same | PASS (required Q gate) | same | same | PASS (required Q gate) |
| **C-14** inertia guard | FAIL | FAIL | FAIL | PASS (structural gate) | FAIL | PASS (structural gate) |

---

## V-01 — Anti-Placeholder Recovery: Structural Checklist

**Axis**: Anti-placeholder recovery (C-12)
**Hypothesis**: A named, mandatory recovery pass with a per-field checklist makes placeholder elimination auditable and non-skippable. The inline instruction "search again if unknown" can be ignored; a checklist with six checkboxes cannot.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

### 2a. Initial sweep

For each claim from Phase 1, search and answer:

1. What are the seminal works the field cites on this claim? (WebSearch: "[claim topic] seminal paper")
2. What reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the method being used? (WebSearch: "[claim topic] method")

Record all sources:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

### 2b. Recovery pass (mandatory before advancing to Phase 3)

Check each row in the table above against this checklist. For each row that fails any check, run the specified follow-up search before marking done.

- [ ] **Title**: real, complete title (not "[title]", "Unknown", or blank)
  - If missing: WebSearch "[known fragment] full title" — fill if found, else write "not found after secondary search — [query]"
- [ ] **Authors**: real last names (not "Author et al.", "et al.", "[author]", or blank)
  - If missing: WebSearch "[title] authors" — fill if found, else write "not found after secondary search — [query]"
- [ ] **Year**: four-digit year 1950-2025 (not "n.d.", "unknown", or blank)
  - If missing: WebSearch "[title] publication year" — fill if found, else write "not found after secondary search — [query]"
- [ ] **Venue**: named journal, conference, or preprint server (not "venue", "TBD", or blank)
  - If missing: WebSearch "[title] venue journal" — fill if found, else write "not found after secondary search — [query]"
- [ ] **Claim #**: a claim number or label from Phase 1 (not blank)
- [ ] **Position**: supports / contradicts / qualifies (not blank)

A row with an unacknowledged placeholder is a failure. Every cell must contain real data or "not found after secondary search — [query used]".

---

## PHASE 3 -- How does the literature organize?

Answer these questions by building the four-tier map:

1. Which sources are FOUNDATIONAL — works the field cannot discuss without citing? (justify each in one sentence)
2. Which sources are RECENT (2020+) — showing engagement with current work?
3. Which sources are CONTRARY — the ones a hostile reviewer will cite against your claims? (for each: which Claim # does it challenge?)
4. Which sources are METHODOLOGICAL — establishing that the method predates and validates this work? (for each: confirm the paper's year is before the current contribution date)

Every tier must have at least one answer. If a tier has no entries, write "NONE FOUND — explain why and what additional search is needed."

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these questions:

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK — no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the recommendation?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list — most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-02 — Per-Tier Acknowledgment Gate

**Axis**: Per-tier acknowledgment gate (C-13)
**Hypothesis**: Framing NONE FOUND as the answer to a required question — rather than a fallback rule at the phase level — creates stronger compliance. A question cannot be unanswered; a rule can be skipped. The two-question gate also makes the absence of entries as legible as their presence.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

For each claim from Phase 1, search and answer:

1. What are the seminal works the field cites on this claim? (WebSearch: "[claim topic] seminal paper")
2. What reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the method being used? (WebSearch: "[claim topic] method")

Record answers in a citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

No placeholder entries. If a cell is unknown, note it and search again.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped.

### FOUNDATIONAL tier

**Q: Which sources are foundational — works the field cannot discuss without citing?**
List each with a one-sentence justification for why it is irreplaceable.

**Q: If none found — why not, and what additional search would be needed to close this gap?**
*(Answer this question only if the tier above is empty. If sources appear above, skip this question.)*

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) — showing engagement with the current state of the field?**
List each with a note on what current consensus or shift it represents.

**Q: If none found — why might the field lack recent coverage on this topic, and what search might surface it?**
*(Answer this question only if the tier above is empty.)*

### CONTRARY tier

**Q: Which sources are contrary — the works a hostile reviewer would cite against your claims?**
List each with the Claim # it challenges and one sentence on the specific objection it raises.

**Q: If none found — why might no contrary evidence exist, and is this absence plausible given the claims being made?**
*(Answer this question only if the tier above is empty. "No contrary evidence exists" requires a reasoned justification — silence is not an acceptable answer for this tier.)*

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent — showing that the method predates and validates this work?**
List each with its publication year, confirming the year predates the current work's contribution date.

**Q: If none found — what methodological gap does this represent, and what would a reviewer need to see to accept the method?**
*(Answer this question only if the tier above is empty.)*

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these questions:

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK — no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the recommendation?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list — most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-03 — Inertia Guard as PROCEED Gate

**Axis**: Inertia guard on PROCEED (C-14)
**Hypothesis**: When PROCEED is gated behind a named inertia scenario, the model cannot short-circuit to a recommendation without first answering why the evidence overcomes the status-quo default. The gate converts an optional reminder into a structural requirement that must produce a specific answer.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

For each claim from Phase 1, search and answer:

1. What are the seminal works the field cites on this claim? (WebSearch: "[claim topic] seminal paper")
2. What reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the method being used? (WebSearch: "[claim topic] method")

Record answers in a citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

No placeholder entries. If a cell is unknown, note it and search again.

---

## PHASE 3 -- How does the literature organize?

Answer these questions by building the four-tier map:

1. Which sources are FOUNDATIONAL — works the field cannot discuss without citing? (justify each in one sentence)
2. Which sources are RECENT (2020+) — showing engagement with current work?
3. Which sources are CONTRARY — the ones a hostile reviewer will cite against your claims? (for each: which Claim # does it challenge?)
4. Which sources are METHODOLOGICAL — establishing that the method predates and validates this work? (for each: confirm the paper's year is before the current contribution date)

Every tier must have at least one answer. If a tier has no entries, write "NONE FOUND — explain why and what additional search is needed."

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK — no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list — most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

Answer both questions before writing PROCEED, SEARCH MORE, or REFRAME CLAIM:

**Q: What would a team do if they ignored this literature entirely?**
Name the default path — the behavior that requires no effort from the team. (e.g., "proceed with original claims unchanged and hope no reviewer knows the contrary papers", "abandon the work as unsubstantiated", "use the method without citing precedent and treat reviewer objections as out of scope")

**Q: What in the evidence gathered makes that default worse than acting on the literature?**
Name the specific risk the inertia path creates. If recommending PROCEED: explain why the evidence is strong enough that the inertia risk is acceptable. If recommending SEARCH MORE or REFRAME CLAIM: name what the inertia path leaves exposed.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence — must reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-04 — Interrogative Obligation + Embedded Recovery

**Axes**: Interrogative obligation (C-11) + Anti-placeholder recovery (C-12)
**Hypothesis**: Questions that embed the recovery instruction within themselves create a tighter obligation than a standalone recovery pass. When the question is "Who are the authors? If unknown after a follow-up search, write 'not found after [query]'", the model must either produce real data or produce an explicit acknowledgment — the question cannot be satisfied with a blank cell or generic placeholder. Interrogative obligation and anti-placeholder recovery become the same mechanism.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

Questions that include "if unknown" are not optional branches — they require you to perform the follow-up action and report the result. "Not answered" and "blank" are not acceptable answers to any question in this skill.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

For each source located, answer these questions per source before entering it in the table:

- What is the full title? If unknown after WebSearch "[known fragment] full title", write: "not found after secondary search — [query used]"
- Who are the authors by real last name (not "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search — [query used]"
- What year was it published? If unknown after WebSearch "[title] publication year", write: "not found after secondary search — [query used]"
- What venue (named journal, conference, or preprint server) published it? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search — [query used]"
- Which Claim # from Phase 1 does this source bear on?
- Does it support, contradict, or qualify that claim?
- What is the key finding in one sentence?

Record in citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

Every cell must contain real data or "not found after secondary search — [query used]". No other placeholder is acceptable.

---

## PHASE 3 -- How does the literature organize?

Answer these questions by building the four-tier map:

1. Which sources are FOUNDATIONAL — works the field cannot discuss without citing? (justify each in one sentence)
2. Which sources are RECENT (2020+) — showing engagement with current work?
3. Which sources are CONTRARY — the ones a hostile reviewer will cite against your claims? (for each: which Claim # does it challenge?)
4. Which sources are METHODOLOGICAL — establishing that the method predates and validates this work? (for each: confirm the paper's year is before the current contribution date)

Every tier must have at least one answer. If a tier has no entries, write "NONE FOUND — explain why and what additional search is needed."

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these questions:

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK — no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the recommendation?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list — most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-05 — Full Synthesis

**Axes**: Interrogative obligation (C-11) + Embedded recovery (C-12) + Per-tier acknowledgment gate (C-13) + Inertia guard as PROCEED gate (C-14)
**Hypothesis**: Combining all four new criteria into a single variation — built on the V-04 R1 interrogative baseline — achieves the theoretical ceiling of the v2 rubric. Each criterion reinforces the others: embedded recovery questions prevent placeholder drift, per-tier acknowledgment gates prevent silent omission, and the inertia gate prevents premature PROCEED from cutting the review short.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

Questions that include "if unknown" require you to perform the follow-up action and report the result. Questions that include "if none found" require an explanation — they cannot be answered with silence. "Blank", "N/A", and "see above" are not acceptable answers to any question in this skill.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

For each source located, answer these questions per source before entering it in the table:

- What is the full title? If unknown after WebSearch "[known fragment] full title", write: "not found after secondary search — [query used]"
- Who are the authors by real last name (not "et al." or "[author]")? If unknown after WebSearch "[title] authors", write: "not found after secondary search — [query used]"
- What year was it published? If unknown after WebSearch "[title] publication year", write: "not found after secondary search — [query used]"
- What venue (named journal, conference, or preprint server) published it? If unknown after WebSearch "[title] venue journal", write: "not found after secondary search — [query used]"
- Which Claim # from Phase 1 does this source bear on?
- Does it support, contradict, or qualify that claim?
- What is the key finding in one sentence?

Record in citation table:

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

Every cell must contain real data or "not found after secondary search — [query used]". No other placeholder is acceptable.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped.

### FOUNDATIONAL tier

**Q: Which sources are foundational — works the field cannot discuss without citing?**
List each with a one-sentence justification for why it is irreplaceable.

**Q: If none found — why not, and what additional search would address this gap?**
*(Answer only if tier above is empty. If sources appear above, skip this question.)*

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) — showing engagement with the current state of the field?**
List each with a note on what current consensus or shift it represents.

**Q: If none found — why might the field lack recent coverage on this topic, and what search might surface it?**
*(Answer only if tier above is empty.)*

### CONTRARY tier

**Q: Which sources are contrary — works a hostile reviewer would cite against your claims?**
List each with the Claim # it challenges and one sentence on the specific objection it raises.

**Q: If none found — why might no contrary evidence exist, and is this absence plausible given the claims being made?**
*(Answer only if tier above is empty. "No contrary evidence" requires a reasoned justification — silence is not acceptable for this tier.)*

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent — showing the method predates and validates this work?**
List each with its publication year, confirming the year predates the current work's contribution date.

**Q: If none found — what methodological gap does this represent, and what would a reviewer require to accept the method?**
*(Answer only if tier above is empty.)*

---

## PHASE 4 -- Where are the gaps and what should be done?

Answer these five questions, then complete the inertia scenario block before writing the recommendation keyword.

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many claims have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? List them most-dangerous-first.
4. Are any claims HIGH RISK — no support plus strong contrary evidence? For each: should it be scoped, qualified, or dropped?
5. What is the overall strength of the evidence position?

```
Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list — most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing
```

### Inertia scenario (required gate before the recommendation keyword)

Answer both questions before writing PROCEED, SEARCH MORE, or REFRAME CLAIM:

**Q: What would a team do if they ignored this literature entirely?**
Name the default path — the behavior that requires no effort from the team.

**Q: What in the evidence gathered makes that default worse than acting on the literature?**
Name the specific risk the inertia path creates. If recommending PROCEED: explain why the evidence is strong enough that the inertia risk is acceptable. If recommending SEARCH MORE or REFRAME CLAIM: name what the inertia path leaves exposed.

```
INERTIA SCENARIO: [what a team does if they ignore this literature]
INERTIA RISK: [why that default creates a worse outcome than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence — must reference the inertia scenario]
```

---

## PHASE 5 -- What are the three most important next actions?

Answer:
1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what should the response strategy be? (scope qualification / methodological distinction / domain limitation)
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```
