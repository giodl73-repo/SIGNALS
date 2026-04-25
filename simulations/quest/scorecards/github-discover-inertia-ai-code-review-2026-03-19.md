● List directory .
  └ 13 files found

● Read CLAUDE.md
  └ 12 lines read

● Search (glob)
  │ "signals\**\*ai-code-review*"
  └ No matches found

● Search (glob)
  │ ".roles\**\*"
  └ No matches found

● List directory signals
  └ 5 files found

● Search (glob)
  │ "signals\**\*.md"
  └ No matches found

● List directory signals\discover
  └ 2 files found

● List directory signals\discover\competitors
  └ 1 file found

● List directory signals\discover\competitors-alt
  └ 1 file found

● Read ai-code-review-competitors-alt-2026-03-19.md
  │ signals\discover\competitors-alt\ai-code-review-competitors-alt-2026-03-19.md
  └ 82 lines read

● Read ai-code-review-competitors-2026-03-19.md
  │ signals\discover\competitors\ai-code-review-competitors-2026-03-19.md
  └ 219 lines read

Now I have rich context from the existing competitor signals. Let me build the deep inertia analysis.

● List directory simulations
  └ 1 file found

● Read customer-test-results.md
  └ 1 line read

● Read BUGS.md
  └ 99 lines read

● Read customer-test-results.md
  └ L1:80 (80 lines read)

Now I have comprehensive context from both competitor signals plus the project's quality history. Let me create the output directory and write the artifact.

● Create inertia signal directory (shell)
  │ New-Item -ItemType Directory -Path "sim-test\signals\discover\inertia" -Force
  └ 4 lines...

● Create ai-code-review-inertia-2026-03-19.md +176
  └ signals\discover\inertia\ai-code-review-inertia-2026-03-19.md

Artifact written to `signals/discover/inertia/ai-code-review-inertia-2026-03-19.md`.

---

**Summary:** Inertia threat is **HIGH**. Manual peer review is expensive (~$65K/year for a team of 8) but deeply normalized — teams have done it for 20 years and it works. Switching cost is **MEDIUM** (~$5.5K–$8.5K first year, 3–6 weeks cultural adjustment). The single condition closest to tipping teams away from inertia: **AI-generated code exceeding 50% of commits**, which breaks human review throughput. 30% of teams are already there; universal within 18 months. The workaround failure mode to exploit: AI-generated PRs receive worse review despite more time spent, because reviewers lack generation context. No current tool addresses this specifically.

**Condition for inertia to lose:** Don't convince teams to switch — get installed before the AI-code volume dam breaks. Be there when the pain becomes acute.

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: No Copilot-specific issues. Web search was not invoked (grounded on existing competitor signals which already contained cited data from LinearB 2026, Qodo, Mordor Intelligence, etc.). A live web search pass could sharpen the 50%-commit-threshold timing estimate with fresher data. All five phases completed with quantified costs. The emerging IDE-based pre-review workaround (Workaround 3) is a signal-unique finding not present in the competitor analyses.


Total usage est:        6 Premium requests
API time spent:         3m 15s
Total session time:     3m 21s
Total code changes:     +176 -0
Breakdown by AI model:
 claude-opus-4.6-1m       374.8k in, 6.8k out, 335.2k cached (Est. 6 Premium requests)
