● List directory .
  └ 11 files found

● Read CLAUDE.md
  └ 12 lines read

● Read BUGS.md
  └ 99 lines read

● List directory simulations
  └ 1 file found

● Check signals directory (shell)
  │ if (Test-Path "sim-test\signals") { Get-ChildItem -Recurse "sim-test\signals" }
  │ else { "signals directory does not exist" }
  └ 2 lines...

Now let me research the competitive landscape for AI code review tools.

● Web Search AI code review market size growth 2025 2026 enterprise adoption rate
  └ {"type":"text","text":{"value":"The AI code review market is experiencing not...

● Web Search GitHub Copilot code review vs CodeRabbit vs Qodo vs Sourcery AI comparison 2025
  └ {"type":"text","text":{"value":"Here's a detailed 2025 comparison of GitHub C...

● Web Search Best AI code review tools 2025 2026 - comprehensive comparison of automated code revie…
  └ {"type":"text","text":{"value":"AI-driven code review tools have advanced dra...

Now let me get a few more targeted competitive data points to verify key claims.

● Web Search CodeRabbit AI code review adoption numbers users 2025 2026
  └ {"type":"text","text":{"value":"Here is a summary of CodeRabbit's AI code rev...

● Web Search developer survey code review bottleneck time spent percentage 2025 2026
  └ {"type":"text","text":{"value":"Recent developer surveys and industry reports...

Now I have comprehensive research. Let me create the artifact.

● Create signals directory structure (shell)
  │ New-Item -ItemType Directory -Path "sim-test\signals\discover\competitors" -Force
  └ 4 lines...

● Create ai-code-review-competitors-2026-03-19.md +220
  └ signals\discover\competitors\ai-code-review-competitors-2026-03-19.md

Artifact written. Let me verify it.

● Verify artifact structure (shell)
  │ $content = Get-Content
  │ "sim-test\signals\discover\competitors\ai-code-review-competitors-2026-03-19.md" -Raw;
  │ "Lines: $((($content -split "`n").Count))"; "Size: $($content.Length) chars"; "Has frontmatter:
  │ $($content.StartsWith('---'))"; "Sections: $(($content | Select-String -Pattern '^## '
  │ -AllMatches).Matches.Count)"
  └ 5 lines...

Artifact verified: 220 lines, 17.4K chars, frontmatter present, written to `signals/discover/competitors/ai-code-review-competitors-2026-03-19.md`.

---

**QUALITY:** 4
**COPILOT_COMPATIBLE:** Y
**NOTES:** No Copilot-specific issues. All web searches executed successfully. Five verified inline citations from LinearB 2026 benchmarks, PullFlow comparison, Startup Wired (CodeRabbit growth), Mordor Intelligence (market sizing), and McKinsey State of AI. The skill ran cleanly in Copilot CLI with parallel web_search calls and single-pass artifact creation. The `signals/` directory was created fresh (did not previously exist).

---

### Brief summary

**Artifact:** `signals/discover/competitors/ai-code-review-competitors-2026-03-19.md`

**Key findings:**
- **Inertia is the #1 threat** — code review consumes 57% of cycle time; 96% of devs don't trust AI-reviewed code
- **3 HIGH-threat competitors:** CodeRabbit (588K MAU, market leader), GitHub Copilot Review (distribution moat, 30K orgs), Qodo (enterprise/compliance)
- **Whitespace:** Cross-repo architectural review, AI-code-specific audit workflows, review analytics, compliance-as-review
- **Table stakes:** 7 must-haves including inline fix suggestions, sub-2-min latency, configurable sensitivity, OWASP security
- **Exec risk:** Diff-only features are commoditizing fast; Copilot's bundling advantage makes standalone tools invisible unless they deliver 10x better signal


Total usage est:        6 Premium requests
API time spent:         2m 50s
Total session time:     4m 1s
Total code changes:     +220 -0
Breakdown by AI model:
 claude-opus-4.6-1m       344.3k in, 6.6k out, 282.7k cached (Est. 6 Premium requests)
