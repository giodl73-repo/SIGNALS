● List directory .
  └ 13 files found

● Search (glob)
  │ "signals/**/*ai-code-review*"
  └ 16 files found

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L1:80 (80 lines read)

● Read ai-code-review-feasibility-2026-03-19.md
  │ signals\discover\feasibility\ai-code-review-feasibility-2026-03-19.md
  └ L1:60 (60 lines read)

● Read ai-code-review-inertia-2026-03-19.md
  │ signals\discover\inertia\ai-code-review-inertia-2026-03-19.md
  └ L1:60 (60 lines read)

● Read ai-code-review-competitors-2026-03-19.md
  │ signals\discover\competitors\ai-code-review-competitors-2026-03-19.md
  └ L1:60 (60 lines read)

Good context from existing artifacts. Now let me search for evidence to ground the key claims.

● Web Search code review market size 2026 AI-powered code review enterprise adoption rate
  └ {"type":"text","text":{"value":"### Code Review Market Size (2026) & Growth\n...

● Web Search developers trust AI generated code correctness percentage survey 2025 2026
  └ {"type":"text","text":{"value":"Recent industry surveys from 2025 and early 2...

● Web Search AI-generated pull requests wait longer for review 2025 2026 statistics
  └ {"type":"text","text":{"value":"Recent industry reports and benchmark studies...

● Web Search AI code review tools false positive rate accuracy benchmarks 2025 2026
  └ {"type":"text","text":{"value":"Here are the most recent public benchmarks an...

● Web Search LinearB software engineering benchmarks 2026 AI code review gap statistics
  └ {"type":"text","text":{"value":"The 2026 LinearB Software Engineering Benchma...

Now let me search for a couple more specific claims referenced in the artifacts.

● Web Search code review consumes 57 percent software development cycle time LinearB 2026
  └ {"type":"text","text":{"value":"Yes, it's accurate that code review is consum...

● Web Search CodeRabbit AI code review 1.7x more issues AI generated code report 2025
  └ {"type":"text","text":{"value":"CodeRabbit's \"State of AI vs Human Code Gene...

Now I have comprehensive evidence. Let me create the output directory and write the artifact.

● Create websearch output directory (shell)
  │ New-Item -ItemType Directory -Path "C:\src\sim-test\signals\discover\websearch" -Force |
  │ Out-Null; Write-Output "done"
  └ 2 lines...

● Create ai-code-review-websearch-2026-03-19.md +183
  └ signals\discover\websearch\ai-code-review-websearch-2026-03-19.md

Artifact written to `signals\discover\websearch\ai-code-review-websearch-2026-03-19.md`.

**Results: 5 of 5 claims CONFIRMED.**

| # | Claim | Verdict | Primary Source |
|---|-------|---------|----------------|
| 1 | AI PRs wait 4.6× longer in queue | ✅ CONFIRMED | LinearB 2026 (8.1M PRs) |
| 2 | 96% of devs don't fully trust AI code | ✅ CONFIRMED | Sonar 2026 + Stack Overflow 2025 |
| 3 | Review = 57% of cycle time | ✅ CONFIRMED | LinearB 2026 |
| 4 | 32.7% AI PR acceptance vs 84.4% human | ✅ CONFIRMED | LinearB 2026 |
| 5 | AI code has 1.7× more issues/PR | ✅ CONFIRMED | CodeRabbit Dec 2025 (470 PRs) |

**Risk note:** Claims 1, 3, 4 share a single primary dataset (LinearB). Claim 5 uses a relatively small sample (470 PRs). Counter-signal: AI PR acceptance rates are trending upward for some tools — recommend re-check in 90 days.

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: Web search tool worked well for all queries. No Copilot-specific issues — all searches returned rich, citable results. Minor concern: some aggregator sites (byteiota.com) repackage LinearB data without adding independent analysis, which inflates apparent source diversity.


Total usage est:        6 Premium requests
API time spent:         2m 8s
Total session time:     3m 3s
Total code changes:     +183 -0
Breakdown by AI model:
 claude-opus-4.6-1m       329.1k in, 5.9k out, 267.3k cached (Est. 6 Premium requests)
