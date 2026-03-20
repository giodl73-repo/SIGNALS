---
mode: agent
description: "Risk register for a feature or decision. What could go wrong? Lists top risks across dimensions: technical (implementati"
---
If --compact flag: output top 3 risks with severity and mitigation. Skip full risk register and scoring matrix.

for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


You are running /discover-risk for: {{topic}}

Produce a structured risk register. This is pre-commitment analysis — find the risks
before you build, not after.

---

## INERTIA RISK (always first)

The primary risk is always inertia: the team builds the feature and nobody adopts it
because the status quo was good enough.

Inertia risk assessment:
- Current workaround: [what teams do today instead of this feature]
- Switching cost: [time, training, disruption estimate]
- Inertia threat score: HIGH | MEDIUM | LOW
- Condition for inertia to lose: [what would make teams switch]

Score inertia HIGH unless you can specifically articulate why teams will switch.

---

## RISK REGISTER

Assess risks across 5 dimensions. For each risk: name it, score it, state the mitigation.

**Severity**: HIGH (blocks ship or adoption) | MEDIUM (requires mitigation) | LOW (monitor)
**Likelihood**: HIGH | MEDIUM | LOW

| Dimension | Risk | Severity | Likelihood | Mitigation |
|-----------|------|----------|------------|------------|
| Technical | [implementation unknowns, complexity, dependencies] | | | |
| Compliance | [regulatory, legal, data residency, audit requirements] | | | |
| Adoption | [user resistance, training cost, workflow disruption] | | | |
| Dependency | [platform risk, third-party APIs, infrastructure] | | | |
| Timeline | [schedule risk, team capacity, competing priorities] | | | |

---

## COMPLIANCE DIMENSION (expand if HIGH)

If compliance risk is HIGH or MEDIUM, expand:
- Applicable frameworks: [GDPR / SOC2 / HIPAA / CCPA / WCAG / other]
- Data handling: [what PII or sensitive data does this touch?]
- Audit requirements: [what evidence is needed for compliance?]
- Showstopper risk: YES / NO — [if yes, stop and address before specifying]

---

## RISK SUMMARY

Top 3 risks ranked by (Severity × Likelihood):
1. [Highest risk with one-sentence rationale]
2. [Second risk]
3. [Third risk]

Overall pre-commitment risk level: HIGH | MEDIUM | LOW
Recommendation: [proceed / address specific risk first / stop]

---

AMEND:
1. Focus on compliance dimension only (for regulated industries)
2. Quantify financial exposure per risk (add cost column)
3. Add a fourth option: risk acceptance rationale for each LOW item

Write artifact to: signals/discover/risk/{{topic}}-risk-{{date}}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
Include frontmatter: skill: discover-risk, topic: {{topic}}, date: {{date}}
