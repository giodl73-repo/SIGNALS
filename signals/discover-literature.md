You are running /discover-literature for: {{topic}}

Systematic literature review with citation management. discover-websearch finds pages but doesn't build a structured literature map the way a methods section needs. This skill builds the map.

---

## PHASE 1 -- CLAIM EXTRACTION

Read any prior signals: discover-hypothesis, specify-spec, paper draft.
Extract the 3-5 key claims that require literature support. For each claim, state:
- What the claim asserts
- What kind of evidence would support it (empirical / theoretical / methodological)
- What contrary evidence would undermine it

---

## PHASE 2 -- LITERATURE SEARCH

For each claim, search for:
1. **Seminal papers** — the foundational works the field cites (use WebSearch: "[claim topic] seminal" or "[key term] original paper")
2. **Recent reviews** — surveys from the last 5 years that map the current state (use WebSearch: "[claim topic] review 2020-2025")
3. **Contrary evidence** — papers that challenge the claim or offer competing explanations (use WebSearch: "[claim topic] criticism" or "against [claim]")
4. **Methodological precedents** — papers that justify the method being used

For each source found:
| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|
| | | | | | supports/contradicts/qualifies | |

---

## PHASE 3 -- LITERATURE MAP

Organize into four tiers:

**FOUNDATIONAL** (must cite — the field depends on these)
[list with one-sentence justification for why each is foundational]

**RECENT** (last 5 years — shows engagement with current work)
[list — prioritize highly-cited or published in top venues]

**CONTRARY** (papers that challenge the claim — must address these)
[list — these are the papers a hostile reviewer will cite against you]

**METHODOLOGICAL** (papers that justify the method)
[list — demonstrates the method is established, not invented for this paper]

---

## PHASE 4 -- GAP ANALYSIS

```
Claims with strong literature support: N/M
Claims with weak or no support: [list]
Contrary evidence that must be addressed: [list — most dangerous first]
Missing methodological precedents: [what needs to be found]

RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
```

If a claim has no supporting literature and strong contrary evidence: flag as HIGH RISK — the claim may need to be scoped, qualified, or dropped.

---

## PHASE 5 -- AMEND

Three targeted additions:
1. [The claim most urgently needing more support — what to search for next]
2. [The contrary paper that must be addressed — what the response should be]
3. [The methodological gap — what precedent is needed to justify the method]

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
