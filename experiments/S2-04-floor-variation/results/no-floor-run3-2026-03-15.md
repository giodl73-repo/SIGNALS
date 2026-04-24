Artifact written to `simulations/scout/competitors/plugin-competitors-2026-03-15.md`.

---

## Competitive Brief: Signal Plugin

### The Strategic Picture

Signal sits at the intersection of developer-native AI tooling and product discovery. No competitor occupies this exact coordinate. The whitespace is real — but the primary threat is not a named competitor.

---

### 1. The Primary Competitor: Inertia — THREAT: HIGH

Inertia wins because the cost of not having pre-build evidence is diffuse and invisible. Teams ship intuition and survive it often enough that no felt pain accumulates. What cracks inertia: the one "we built the wrong thing" post-mortem. Signal's zero-config first-run requirement is not a DX nicety — it is the inertia counter. Every barrier removed is adoption percentage recovered.

---

### 2. The Whitespace

> Developer-native, repo-resident, multi-namespace evidence corpus with narrative synthesis toward a go/no-go feature decision.

No competitor owns this. **/deep-plan** is closest but it's a single-pass planning workflow — it assumes the build decision is already made and optimizes the plan. Signal owns the upstream phase. PM-tier tools (ChatPRD, BuildBetter, Productboard) are discovery tools but live in a browser, serve the PM, not the developer making the architectural call.

---

### 3. Table Stakes

Any entrant must have: (1) zero-config first run, (2) artifacts in the repo, (3) terminal/IDE-native UX, (4) namespace specialization, (5) synthesis layer.

---

### 4. The Competitive Matrix

| Competitor | Overlap | Positioning | Threat |
|---|---|---|---|
| **Inertia (status quo)** | N/A | Primary incumbent | HIGH |
| **/deep-plan** ([GitHub](https://github.com/piercelamb/deep-plan)) | MEDIUM | Adjacent — planning tool, not evidence tool | MEDIUM |
| **GitHub Copilot / Cursor** | LOW | Complementary | LOW-MEDIUM |
| **Claude Code native (Plan Mode)** | LOW | Complementary | LOW |
| **ChatPRD** | MEDIUM | Adjacent — PM-tier PRD gen | LOW |
| **BuildBetter** | MEDIUM | Adjacent — customer research | LOW |
| **Productboard** | LOW | Distant — PM roadmap | LOW |
| **Linear** | LOW | Distant — issue tracking | LOW |

**/deep-plan is the only direct Claude Code competitor.** It transforms vague requirements into plans via research + multi-LLM review (Deep Trilogy: project + plan + implement). Key difference: single workflow → single plan. Signal: persistent corpus → 9-namespace evidence → narrative synthesis.

---

### 5. --mode risk: The Cost of Building the Wrong Thing

A 6-week feature built on an assumption /scout:competitors would have invalidated in 2 hours = $115K at risk in a 20-person team before one line of production code ships. Rework compounding multiplies this at every layer. The specific moat: Signal earns the "ready to build" signal rather than asserting it.

---

### 6. Amendments

1. **Narrow to Claude Code plugins only** — sharpens whitespace, removes PM-tier noise. Recommended for developer audience.
2. **Expand to Windsurf/Zed/Cursor ecosystems** — raises Cursor threat to MEDIUM. Recommended for exec.
3. **Add enterprise IDP players (Backstage, Cortex)** — introduces "platform checkbox feature" risk. Recommended for enterprise positioning.

Sources:
- [/deep-plan GitHub](https://github.com/piercelamb/deep-plan)
- [Claude Code 2026 adoption data — DEV Community](https://dev.to/alexcloudstar/claude-code-vs-cursor-vs-github-copilot-the-2026-ai-coding-tool-showdown-53n4)
- [ChatPRD usage stats](https://www.chatprd.ai/how-i-ai/workflows)
- [Linear Discovery-to-Delivery Gap](https://www.laneapp.co/blog/jira-vs-linear-which-tool-wins)
- [BuildBetter AI PM tools](https://blog.buildbetter.ai/top-ai-tools-product-managers-2026-complete-guide/)
- [Future of AI PM 2026-2030 — AI PM Tools Directory](https://aipmtools.org/articles/future-of-ai-product-management)
