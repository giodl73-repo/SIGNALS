---
skill: discover-risk
topic: ai-code-review
date: 2026-03-19
---

# Risk Register: ai-code-review

---

## INERTIA RISK (always first)

- **Current workaround**: Ad-hoc paste-to-LLM (browser tab) + GitHub PR human review
- **Switching cost**: ~2-3 days direct setup + 3-4 weeks habit formation (source: discover-inertia 2026-03-18)
- **Inertia threat score**: MEDIUM (override from default HIGH; quantified cost of $70K/year and active competitive pressure from Copilot GA -- source: discover-inertia 2026-03-18)
- **Condition for inertia to lose**: Post-mortem trigger ("how did this ship?") forces demand for auditable review artifacts; or Copilot comparison forces a structured evaluation where Signal's artifact model wins on permanence and pattern detection

---

## RISK REGISTER

| Dimension | Risk | Severity | Likelihood | Mitigation |
|-----------|------|----------|------------|------------|
| **Inertia** | Teams stay with paste-to-LLM + human review because it "works fine" | HIGH | MEDIUM | Target post-mortem teams; lead with audit trail value, not review quality |
| **Technical** | False positive rate exceeds 15%, causing developer alert fatigue and tool abandonment | HIGH | MEDIUM | Tune prompts for precision over recall; industry benchmark is 5-15% FP rate (source: Digital Applied 2025); run quest loop with FP-specific rubric criteria |
| **Technical** | Cross-PR pattern memory violates P-03 (Self-Contained Skills), creating architectural debt | MEDIUM | HIGH | Ship Phase 1 without memory; design Phase 2 as separate synthesis skill (source: discover-feasibility 2026-03-19) |
| **Adoption** | Developers perceive structured review as slower than paste-to-LLM; friction causes abandonment after first use | MEDIUM | MEDIUM | Ensure review completes in <60 seconds; make artifact output optional for first runs (P-05 zero barrier) |
| **Dependency** | LLM provider rate limits, cost spikes, or model quality regression degrade review quality unpredictably | MEDIUM | LOW | Support multiple model backends (Claude, GPT, Gemini); implement model fallback; cache common review patterns |
| **Competitive** | GitHub ships Copilot Code Review improvements that close the artifact gap (persistent review history, pattern detection) | HIGH | MEDIUM | Ship differentiation features (topic-scoped aggregation, custom reviewer personas) before Copilot catches up; monitor GitHub changelog monthly |
| **Compliance** | Review artifacts contain sensitive code snippets stored in plaintext; creates data residency concerns for enterprise teams | MEDIUM | LOW | Artifacts stored locally in repo (git-controlled); add `--redact` flag for sensitive output; document data handling in skill spec |
| **Timeline** | Quest loop takes 20+ rounds (as with other skills); timeline extends from 4 to 6+ sprints | MEDIUM | MEDIUM | Cap quest at 20 rounds per the established pattern; accept "good enough" golden score if customer simulation passes (P-11) |

---

## COMPLIANCE DIMENSION (expanded -- MEDIUM)

- **Applicable frameworks**: SOC2 (audit trail for review process), GDPR (if review artifacts contain PII from code comments or variable names), internal code-sharing policies
- **Data handling**: Review artifacts may contain code excerpts. All artifacts stored in the local repository under git version control -- no cloud transmission unless user pushes to remote.
- **Audit requirements**: Signal's artifact model (P-09 provenance) naturally produces audit-ready records (skill, topic, date, input). This is a competitive advantage over paste-to-LLM (no audit trail) and Copilot (ephemeral PR comments).
- **Showstopper risk**: NO -- local storage and git-native approach avoids most data residency issues. Enterprise teams with strict code-sharing policies should validate that review artifact content stays within their git access controls.

---

## RISK SUMMARY

Top 3 risks ranked by (Severity x Likelihood):

1. **Competitive displacement by Copilot** (HIGH severity x MEDIUM likelihood) -- If GitHub adds persistent review history to Copilot Code Review, Signal's primary differentiator evaporates. Mitigation: ship topic-scoped aggregation and custom personas before Copilot closes the gap. Monitor monthly.

2. **False positive alert fatigue** (HIGH severity x MEDIUM likelihood) -- AI code review tools with >15% false positive rates lose developer trust rapidly (source: Qodo State of AI Code Quality 2025; Cubic false positive analysis 2025). If Signal's review skill produces noisy output, developers will disable it after 2-3 uses. Mitigation: quest loop must include FP-rate measurement; tune for precision.

3. **Inertia wins by default** (HIGH severity x MEDIUM likelihood) -- The paste-to-LLM workaround is invisible, free, and habitual. Even if Signal's review is objectively better, switching requires behavior change. Mitigation: target teams in the post-mortem moment when the absence of audit trail is freshly painful.

Overall pre-commitment risk level: **MEDIUM**
Recommendation: **Proceed with Phase 1 (base review without cross-PR memory), address false positive rate in quest loop, ship before Copilot closes the artifact gap.**

---

## AMENDMENTS

1. **Focus on competitive timing**: Add a Copilot feature watch to the risk register. If Copilot ships persistent review history before Signal ships ai-code-review, re-evaluate the entire feature -- the competitive window may have closed.

2. **Quantify false positive threshold**: Establish a hard gate: if quest loop testing shows >12% false positive rate on 5 representative PRs, the skill does not ship until prompts are tuned below that threshold. This is stricter than the 15% industry average because a new entrant must be better than the incumbent.

3. **Risk acceptance for P-03 tension**: Formally document the decision to defer cross-PR memory to Phase 2 as a risk acceptance, not a deferral. If Phase 2 never ships, the base review skill still provides value (structured artifact per PR). The pattern memory is an enhancement, not a requirement.
