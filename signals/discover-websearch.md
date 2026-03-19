You are running /discover-websearch for: {{topic}}

Ground claims about {{topic}} in public evidence.
Every claim must have a URL. Do not use training-data recall as evidence.
If a claim cannot be confirmed via search, mark it UNCONFIRMED -- that is a signal too.

---

## PHASE 1: CLAIMS TO GROUND

Identify 3-5 specific claims that need external grounding.

If a discover-hypothesis artifact exists for {{topic}}, pull the hypothesis claim and any
team prior beliefs as starting claims.

If no prior artifacts exist, infer claims from the topic name and repo context.

| # | Claim | Source of claim | Why it needs grounding |
|---|-------|-----------------|------------------------|
| 1 | [Claim text] | [hypothesis / team belief / assumed / other] | [What's at stake if wrong] |
| 2 | [Claim text] | [hypothesis / team belief / assumed / other] | [What's at stake if wrong] |
| 3 | [Claim text] | [hypothesis / team belief / assumed / other] | [What's at stake if wrong] |

---

## PHASE 2: WEB EVIDENCE

For each claim, use WebSearch to find evidence. Search for at least 2 queries per claim.

**Claim 1**: [Restate claim]
- Query 1: "[search string used]"
  - Source: [URL]
  - Direct quote: "[exact text from source, in quotes]"
  - Relevance: [how directly this addresses the claim]
- Query 2: "[search string used]"
  - Source: [URL]
  - Direct quote: "[exact text from source, in quotes]"
  - Relevance: [how directly this addresses the claim]
- Verdict: CONFIRMED | UNCONFIRMED | CONTRADICTED

**Claim 2**: [Restate claim]
- Query 1: "[search string used]"
  - Source: [URL]
  - Direct quote: "[exact text from source, in quotes]"
  - Relevance: [how directly this addresses the claim]
- Query 2: "[search string used]"
  - Source: [URL]
  - Direct quote: "[exact text from source, in quotes]"
  - Relevance: [how directly this addresses the claim]
- Verdict: CONFIRMED | UNCONFIRMED | CONTRADICTED

[Repeat pattern for Claims 3-5]

---

## PHASE 3: FINDINGS TABLE

| # | Claim | Evidence Summary | Verdict | Source |
|---|-------|-----------------|---------|--------|
| 1 | [Claim] | [One sentence] | CONFIRMED / UNCONFIRMED / CONTRADICTED | [URL] |
| 2 | [Claim] | [One sentence] | CONFIRMED / UNCONFIRMED / CONTRADICTED | [URL] |
| 3 | [Claim] | [One sentence] | CONFIRMED / UNCONFIRMED / CONTRADICTED | [URL] |

Summary: [N] of [total] claims confirmed. [N] contradicted. [N] unconfirmed.

---

## PHASE 4: UNGROUNDED CLAIMS

List any claims from Phase 1 that returned no usable search results.

For each ungrounded claim:
- **Claim**: [text]
- **Searches attempted**: [query 1, query 2]
- **Why unconfirmable**: [too recent / too niche / not indexed / search terms may be wrong]
- **Alternative**: [suggest a primary research method -- interview, prototype test, A/B experiment]

If all claims were grounded: write "No ungrounded claims."

---

## PHASE 5: AMEND

3 adjustments to improve this search:

1. **Refine the queries**: Rewrite any query that returned zero useful results. Use domain-specific terminology, add site: filters for known authoritative sources, or narrow the date range to last 12 months.

2. **Increase source diversity**: If all current sources are from the same domain or publication, search specifically for dissenting views. A confirmed claim with only corroborating sources is weaker than one tested against opposition.

3. **Escalate contradicted claims**: Any CONTRADICTED claim changes the risk picture. Surface it to the hypothesis -- run /discover-hypothesis again with the contradicting evidence as the new prior.

---

Write artifact to: signals/discover/websearch/{{topic}}-websearch-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-[this-skill]-{date}.md). No namespace subdirectory.
Include frontmatter: skill: discover-websearch, topic: {{topic}}, date: {{date}}, claims_checked: [n], confirmed: [n]
