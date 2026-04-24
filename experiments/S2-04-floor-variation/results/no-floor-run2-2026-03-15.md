An existing artifact from a previous run is already at that path (skill_version: golden-v1). It's solid — AWS Kiro is a strong call I wouldn't have added. Let me present the consolidated findings rather than overwrite it.

---

## Competitive Brief: Signal Plugin

### Primary Competitor: Inertia (threat: HIGH — always)

Teams don't choose ProductBoard over Signal. They choose their current ad-hoc workflow: Slack threads, Confluence pages, grep the codebase, open Claude.ai, done in 2 minutes. Signal competes with "we already do this informally." What makes inertia unbeatable: no tooling gap is visible until after a feature fails. The activation energy of one new protocol exceeds the perceived benefit on any given day.

**What breaks inertia:** A team that has shipped the wrong thing once and paid for it. A principal who wants artifacts in the repo, not chat logs.

---

### The Whitespace

No competitor owns the territory between **"we have an idea"** and **"we have a spec worth trusting."**

- Coding tools (Copilot, Cursor, Kiro) own *after* the decision — spec-to-code.
- PM tools (ProductBoard, Linear) own *upstream* — roadmap, not evidence.
- General AI chat (Claude.ai, ChatGPT) owns informal research — no durable artifacts.
- Nobody instruments this gap across 9 namespaces with a permanent repo-committed trail.

---

### Named Competitors

| Competitor | Threat | Key Fact |
|---|---|---|
| **Inertia / Status Quo** | HIGH | Already installed. Zero friction. |
| **AWS Kiro** | MEDIUM-HIGH | Launched Aug 2025. EARS-notation spec-to-code. Starts *after* build decision. |
| **DIY Claude/GPT workflows** | HIGH | Teams already prompt Claude for research — no protocol, no artifacts. |
| **GitHub Copilot** | MEDIUM | 20M+ users, 90% of Fortune 100. Agent mode opens PRs. No pre-build phase. Source: github.com/newsroom |
| **Cursor** | MEDIUM | Dominating agentic IDE market. Acquired by OpenAI — platform risk for Claude Code plugins. |
| **Gemini CLI** | LOW-MEDIUM | Free, 1M context, Google Search grounding. 1M+ devs since June 2025. No namespace model. |
| **Notion AI / Confluence Rovo** | MEDIUM | Atlassian Rovo generates feature descriptions from Confluence pages. Document layer only — no typed artifacts. Source: atlassian.com/software/confluence/ai |
| **ProductBoard** | LOW | "AI 2.0" synthesizes existing feedback into specs. Downstream of decision, not upstream. ~$15K+/year. Source: productboard.com/product/ai-for-product-management/ |
| **Devin / Windsurf** | LOW-MEDIUM | Cognition raised $400M, builds after planning. No pre-commit evidence phase. |
| **Perplexity** | LOW | Sonar Pro API delivers cited answers. Lookup, not protocol. No artifact permanence. |

**Highest non-inertia threat:** AWS Kiro — closest structural competitor. It has namespaced spec generation but starts post-decision. If Kiro adds a pre-commit research phase, the whitespace closes.

**Hidden threat:** DIY Claude/GPT workflows. The objection "we already do this with Claude" must be answered not by better prompts but by artifact permanence + topic readiness across a structured corpus.

---

### --mode risk (exec framing)

**$29.5B** wasted annually on features rarely or never used (Maze product discovery research). A 10-engineer team shipping a wrong feature for 6 weeks burns ~$600K in loaded labor. Signal is not a research tool — it is a pre-commit risk audit. The alternative is carrying feature risk silently until it surfaces as rework, churn, or post-mortem. Signal produces the audit trail; chat logs don't.

---

### AMEND

Three adjustments with downstream effects:

1. **Narrow to Claude Code plugin ecosystem** — removes Kiro, Cursor, Gemini CLI, Devin. Whitespace tightens to "no Claude Code plugin does pre-build evidence protocol." Upside: sharper positioning. Downside: misses platform-risk scenario where Cursor adds this phase.

2. **Add compliance/enterprise angle** — SOC 2, regulated industries, audit-trail requirements. ProductBoard threat rises LOW → MEDIUM. New row: enterprise PM platforms (Jira Align, ProductPlan). `--mode risk` section gains compliance column.

3. **Target power users of existing AI tools** — removes General AI Chat as competitor (this audience already knows Claude.ai is insufficient for structured work). Inertia drops HIGH → MEDIUM-HIGH. Messaging shifts from "why structure matters" to "the namespace model Cursor doesn't have."

---

Artifact already exists at `simulations/scout/competitors/plugin-competitors-2026-03-14.md` (golden-v1). The new web-verified sources (ProductBoard, Perplexity, Linear, Confluence/Rovo) can be merged in as a v2 if you want — say the word.
