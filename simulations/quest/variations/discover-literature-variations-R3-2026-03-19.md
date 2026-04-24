Written to `simulations/quest/variations/discover-literature-variations-R3-2026-03-19.md`.

---

## discover-literature — Variations R3

### Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Hardened dual-domain preamble (C-15) | Numbered OBLIGATION A / OBLIGATION B contract is more reliable than prose preamble — two named, co-equal obligations cannot be selectively waived |
| **V-02** | Full template-label expansion (C-16) | Named tokens (`TIER ENTRY:` / `TIER EMPTY:` / `RECOVERY NOTE:`) on every structural gate extend grep-checkability beyond the inertia gate |
| **V-03** | Depth mode source threshold (C-09) | `--mode quick/standard/deep` with explicit thresholds (5/15/25) gives the model a concrete stopping condition rather than an open-ended search |
| **V-04** | C-15 + C-16 combined | Formal preamble + full token coverage — preamble declares obligations, tokens make compliance observable |
| **V-05** | Full synthesis (C-15 + C-16 + C-09) | Theoretical ceiling of the v3 rubric — all three R3 targets on top of V-05 R2 |

### Projected coverage

| Criterion | V-05 R2 baseline | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----------------|------|------|------|------|------|
| C-09 depth mode | FAIL | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| C-15 dual-domain preamble | PARTIAL | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-16 template-label checkability | PASS (min) | PASS (min) | **PASS (full)** | PASS (min) | **PASS (full)** | **PASS (full)** |

### Key design decisions

- **V-01 vs V-05 R2 preamble**: V-05 R2 has a prose preamble covering both obligations but not as a named contract. V-01 adds `OBLIGATION A` / `OBLIGATION B` labels and explicit acceptable/unacceptable value lists — making it a checkable contract, not guidance.
- **V-02 token discipline**: The `TIER ENTRY:` / `TIER EMPTY:` tokens replace the V-05 R2 conditional "if none found, write..." prose. The token is the output; the prose was describing the output. Less ambiguity about what a compliant run produces.
- **V-03 depth mode**: Adds two search angles (adjacent topics, cited-by chains) that only activate when the threshold isn't met after the standard four angles. The threshold failure note (`THRESHOLD NOT MET:`) is itself a named token for C-16 purposes.
- **V-05 adds `mode:` to frontmatter** — C-09 pass requires sources_found in frontmatter; adding the mode field makes the threshold checkable from the frontmatter alone without parsing the body.
- **C-09 was the stated open gap in the v3 rubric changelog** — V-03 and V-05 are the only variations that address it. If the scorecard shows V-03 gaining a full pass on C-09, that validates the threshold mechanism as the right fix.
urce thresholds; depth mode defaults to standard (>= 15); the Phase 2 search loop runs until the threshold is met or all search angles exhausted
- **V-04** stacks V-01 (hardened preamble) + V-02 (full token coverage) on the V-05 R2 baseline
- **V-05** stacks all three: hardened preamble + full tokens + depth mode

### Projected rubric coverage

| Criterion | V-05 R2 baseline | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----------------|------|------|------|------|------|
| C-01..C-05 essential | PASS | same | same | same | same | same |
| C-06..C-08 recommended | PASS | same | same | same | same | same |
| C-09 depth mode | FAIL | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| C-10..C-14 aspirational | PASS | same | same | same | same | same |
| **C-15** dual-domain preamble | PARTIAL | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| **C-16** template-label checkability | PASS (min) | PASS (min) | **PASS (full)** | PASS (min) | **PASS (full)** | **PASS (full)** |

V-05 is the only variation that closes all three gaps. V-01 and V-03 are highest single-axis gains: V-01 lifts C-15 from PARTIAL to PASS; V-03 turns C-09 FAIL to PASS. V-02 upgrades C-16 from minimum to full coverage.

---

## V-01 — Hardened Dual-Domain Preamble

**Axis**: Dual-domain obligation preamble (C-15)
**Hypothesis**: A numbered, contract-style preamble with two named obligations — OBLIGATION A and OBLIGATION B — is more likely to produce C-15 PASS than a prose preamble. The formal contract structure signals that both obligations are co-equal and non-waivable, not just stylistic guidance.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A — Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, write exactly: "not found after secondary search — [query used]". Acceptable cell values: real data, or "not found after secondary search — [query]". Unacceptable: blank, "n/a", "unknown", "Author et al.", "[title]", "TBD", or any generic placeholder without a recovery note.

**OBLIGATION B — Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, write: "NONE FOUND — [reason why no sources qualified] — [what additional search would address this gap]". Acceptable tier outcome: >= 1 cited source, or "NONE FOUND" with a reason sentence. Unacceptable: a tier heading followed by silence, blank space, or "see above".

Both obligations apply before Phase 1 begins and remain in force through Phase 5.

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

Every cell must contain real data or "not found after secondary search — [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers.)

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

---

## V-02 — Full Template-Label Expansion

**Axis**: Template-label checkability (C-16)
**Hypothesis**: Named tokens on every structural gate — not just the inertia gate — make all compliance checkpoints grep-verifiable. Phase 2 recovery notes and Phase 3 tier entries benefit from the same token discipline as the Phase 4 inertia block. When every gate produces a scannable label, no compliance check requires inference from surrounding prose.

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

For any cell that required a secondary search, append a recovery note immediately after the table row using this format:
```
RECOVERY NOTE: [field] for "[title fragment]" — [outcome: filled with real data / not found after secondary search — [query]]
```

Every cell must contain real data or "not found after secondary search — [query used]". No other placeholder is acceptable.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped.

### FOUNDATIONAL tier

**Q: Which sources are foundational — works the field cannot discuss without citing?**
For each entry, use this format:
```
TIER ENTRY: FOUNDATIONAL — [Author Year] "[Title]" — [one-sentence justification]
```

**Q: If none found — why not, and what additional search would address this gap?**
*(Answer only if tier above is empty. Use this format:)*
```
TIER EMPTY: FOUNDATIONAL — [reason why no sources qualified] — [what search would address the gap]
```

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) — showing engagement with the current state of the field?**
For each entry, use this format:
```
TIER ENTRY: RECENT — [Author Year] "[Title]" — [note on current consensus or shift represented]
```

**Q: If none found — why might the field lack recent coverage on this topic, and what search might surface it?**
*(Answer only if tier above is empty. Use this format:)*
```
TIER EMPTY: RECENT — [reason] — [search suggestion]
```

### CONTRARY tier

**Q: Which sources are contrary — works a hostile reviewer would cite against your claims?**
For each entry, use this format:
```
TIER ENTRY: CONTRARY — [Author Year] "[Title]" — Claim # [n] — [specific objection in one sentence]
```

**Q: If none found — why might no contrary evidence exist, and is this absence plausible given the claims being made?**
*(Answer only if tier above is empty. "No contrary evidence" requires a reasoned justification — silence is not acceptable for this tier.)*
```
TIER EMPTY: CONTRARY — [reason] — [plausibility assessment]
```

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent — showing the method predates and validates this work?**
For each entry, use this format:
```
TIER ENTRY: METHODOLOGICAL — [Author Year] "[Title]" — [year confirmation: predates current work]
```

**Q: If none found — what methodological gap does this represent, and what would a reviewer require to accept the method?**
*(Answer only if tier above is empty.)*
```
TIER EMPTY: METHODOLOGICAL — [gap description] — [what reviewer would require]
```

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

---

## V-03 — Depth Mode Source Threshold

**Axis**: Depth mode source threshold (C-09)
**Hypothesis**: Naming an explicit source threshold eliminates the open-ended search problem. When the model knows it needs >= 15 sources for standard mode, it continues searching until the threshold is met or all search angles are exhausted — rather than stopping when the search feels complete. The depth mode also communicates resource intent to the caller (quick for idea validation, deep for publication).

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3. If the threshold is not met after exhausting the Phase 2 search angles, note this explicitly and explain which angles were tried.

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

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If after searching all four angles the source count is still below the threshold:
5. Search for adjacent or related topics that bear on the same claims: (WebSearch: "[related concept] [claim topic]")
6. Search for cited works in the papers already found: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Continue until threshold is met or all angles exhausted. If threshold cannot be met, note: "THRESHOLD NOT MET: found [n] of [threshold] sources — search angles exhausted: [list]"

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
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## V-04 — Hardened Preamble + Full Token Coverage

**Axes**: Dual-domain obligation preamble (C-15) + Template-label checkability (C-16)
**Hypothesis**: The preamble names the obligations; the tokens make compliance observable. Each reinforces the other: the preamble declares that both obligations are non-waivable globally, the tokens give every structural gate a grep-verifiable output. Together they close the two behavioral gaps remaining in V-05 R2.

```
You are running /discover-literature for: {{topic}}

Your job: answer a specific set of questions about the literature on {{topic}}. Each question requires evidence. Do not proceed past a phase until every question has a concrete answer.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A — Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, write exactly: "not found after secondary search — [query used]". Acceptable cell values: real data, or "not found after secondary search — [query]". Unacceptable: blank, "n/a", "unknown", "Author et al.", "[title]", "TBD", or any generic placeholder without a recovery note.

**OBLIGATION B — Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, use this exact format: "TIER EMPTY: [tier name] — [reason why no sources qualified] — [what additional search would address this gap]". Acceptable tier outcome: >= 1 cited source, or a TIER EMPTY label. Unacceptable: a tier heading followed by silence, blank space, or "see above".

Both obligations apply before Phase 1 begins and remain in force through Phase 5.

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

For any cell that required a secondary search, append a recovery note immediately after the table using this format:
```
RECOVERY NOTE: [field] for "[title fragment]" — [outcome: filled / not found after secondary search — [query]]
```

Every cell must contain real data or "not found after secondary search — [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B governs all four tiers — use TIER ENTRY: or TIER EMPTY: for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational — works the field cannot discuss without citing?**
For each entry, use this format:
```
TIER ENTRY: FOUNDATIONAL — [Author Year] "[Title]" — [one-sentence justification]
```

**Q: If none found — use this format:**
```
TIER EMPTY: FOUNDATIONAL — [reason why no sources qualified] — [what additional search would address this gap]
```

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) — showing engagement with the current state of the field?**
For each entry, use this format:
```
TIER ENTRY: RECENT — [Author Year] "[Title]" — [note on current consensus or shift]
```

**Q: If none found — use this format:**
```
TIER EMPTY: RECENT — [reason] — [search suggestion]
```

### CONTRARY tier

**Q: Which sources are contrary — works a hostile reviewer would cite against your claims?**
For each entry, use this format:
```
TIER ENTRY: CONTRARY — [Author Year] "[Title]" — Claim # [n] — [specific objection in one sentence]
```

**Q: If none found — "No contrary evidence" requires a reasoned justification — silence is not acceptable for this tier:**
```
TIER EMPTY: CONTRARY — [reason] — [plausibility assessment given the claims being made]
```

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent — showing the method predates and validates this work?**
For each entry, use this format:
```
TIER ENTRY: METHODOLOGICAL — [Author Year] "[Title]" — [year confirmation: predates current work]
```

**Q: If none found — use this format:**
```
TIER EMPTY: METHODOLOGICAL — [gap description] — [what reviewer would require to accept the method]
```

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

---

## V-05 — Full Synthesis (C-15 + C-16 + C-09)

**Axes**: Hardened dual-domain preamble (C-15) + Full template-label expansion (C-16) + Depth mode source threshold (C-09)
**Hypothesis**: All three R3 targets integrated into V-05 R2: the formal OBLIGATION A/B contract closes C-15; named tokens on every structural gate expand C-16 from minimum to full coverage; the depth mode threshold closes C-09. Together with the C-11 through C-14 coverage inherited from V-05 R2, this is the theoretical ceiling of the v3 rubric.

```
You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3. If the threshold is not met after exhausting all search angles, note this explicitly: "THRESHOLD NOT MET: found [n] of [threshold] sources — search angles exhausted: [list]"

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic.

**OBLIGATION A — Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, write exactly: "not found after secondary search — [query used]". Acceptable cell values: real data, or "not found after secondary search — [query]". Unacceptable: blank, "n/a", "unknown", "Author et al.", "[title]", "TBD", or any generic placeholder without a recovery note.

**OBLIGATION B — Empty-Tier Acknowledgment**
Every tier of the four-tier literature map must produce output. If a tier has no qualifying entries, use this exact format: "TIER EMPTY: [tier name] — [reason why no sources qualified] — [what additional search would address this gap]". Acceptable tier outcome: >= 1 cited source, or a TIER EMPTY label. Unacceptable: a tier heading followed by silence, blank space, or "see above".

Both obligations apply before Phase 1 begins and remain in force through Phase 5. Questions that include "if unknown" require you to perform the follow-up action and report the result. Questions that include "if none found" require a TIER EMPTY label — they cannot be answered with silence.

---

## PHASE 1 -- What are the claims that need support?

Answer these questions:

1. What are the 3-5 key claims this work makes about {{topic}} that require literature support?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to challenge it?

Read any prior signals (discover-hypothesis, specify-spec, paper draft) before answering.

---

## PHASE 2 -- What does the literature actually say?

Target: reach the source threshold for {{mode}} mode (quick >= 5, standard >= 15, deep >= 25).

For each claim from Phase 1, search and answer:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers directly challenge or contradict this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent for this work? (WebSearch: "[claim topic] method")

If after searching all four angles the source count is still below the threshold:
5. Search for adjacent topics: (WebSearch: "[related concept] [claim topic]")
6. Search for cited works: (WebSearch: "[found paper title] cited by" or "[found author] related work")

Continue until threshold is met or all angles exhausted.

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

For any cell that required a secondary search, append a recovery note immediately after the table using this format:
```
RECOVERY NOTE: [field] for "[title fragment]" — [outcome: filled / not found after secondary search — [query]]
```

Every cell must contain real data or "not found after secondary search — [query used]". No other placeholder is acceptable. (OBLIGATION A)

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. Neither question may be skipped. (OBLIGATION B — use TIER ENTRY: or TIER EMPTY: for every tier.)

### FOUNDATIONAL tier

**Q: Which sources are foundational — works the field cannot discuss without citing?**
For each entry, use this format:
```
TIER ENTRY: FOUNDATIONAL — [Author Year] "[Title]" — [one-sentence justification]
```

**Q: If none found:**
```
TIER EMPTY: FOUNDATIONAL — [reason why no sources qualified] — [what additional search would address this gap]
```

### RECENT tier (2020 or later)

**Q: Which sources are recent (2020+) — showing engagement with the current state of the field?**
For each entry, use this format:
```
TIER ENTRY: RECENT — [Author Year] "[Title]" — [note on current consensus or shift]
```

**Q: If none found:**
```
TIER EMPTY: RECENT — [reason] — [search suggestion]
```

### CONTRARY tier

**Q: Which sources are contrary — works a hostile reviewer would cite against your claims?**
For each entry, use this format:
```
TIER ENTRY: CONTRARY — [Author Year] "[Title]" — Claim # [n] — [specific objection in one sentence]
```

**Q: If none found — "No contrary evidence" requires a reasoned justification — silence is not acceptable for this tier:**
```
TIER EMPTY: CONTRARY — [reason] — [plausibility assessment given the claims being made]
```

### METHODOLOGICAL tier

**Q: Which sources establish methodological precedent — showing the method predates and validates this work?**
For each entry, use this format:
```
TIER ENTRY: METHODOLOGICAL — [Author Year] "[Title]" — [year confirmation: predates current work]
```

**Q: If none found:**
```
TIER EMPTY: METHODOLOGICAL — [gap description] — [what reviewer would require to accept the method]
```

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
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```
