● List directory .
  └ 13 files found

● Read CLAUDE.md
  └ 12 lines read

● Search (glob)
  │ "signals/**/ai-code-review-*"
  └ 38 files found

Extensive prior signals found. Let me read the key discovery signals to ground the proposal.

● Read ai-code-review-competitors-2026-03-19.md
  │ signals\discover\competitors\ai-code-review-competitors-2026-03-19.md
  └ 219 lines read

● Read ai-code-review-hypothesis-2026-03-19.md
  │ signals\discover\hypothesis\ai-code-review-hypothesis-2026-03-19.md
  └ 55 lines read

● Read ai-code-review-synthesize-2026-03-19.md
  │ signals\discover\synthesize\ai-code-review-synthesize-2026-03-19.md
  └ 99 lines read

● Read ai-code-review-risk-2026-03-19.md
  │ signals\discover\risk\ai-code-review-risk-2026-03-19.md
  └ 75 lines read

● Read ai-code-review-brainstorm-2026-03-19.md
  │ signals\discover\brainstorm\ai-code-review-brainstorm-2026-03-19.md
  └ 66 lines read

● Read ai-code-review-feasibility-2026-03-19.md
  │ signals\discover\feasibility\ai-code-review-feasibility-2026-03-19.md
  └ 157 lines read

Let me also read the existing proposal and inertia signals for completeness.

● Read ai-code-review-proposal-2026-03-19.md
  │ signals\specify\proposal\ai-code-review-proposal-2026-03-19.md
  └ 122 lines read

● Read ai-code-review-compare-2026-03-19.md
  │ signals\discover\compare\ai-code-review-compare-2026-03-19.md
  └ 175 lines read

● Read ai-code-review-inertia-2026-03-19.md
  │ signals\discover\inertia\ai-code-review-inertia-2026-03-19.md
  └ 175 lines read

Now I have the full picture. 38 prior signals exist. The synthesis recommends Option B (narrow AI-code auditor) with PROCEED at 72 confidence. Let me write the updated proposal grounded in all signals.

● Edit ai-code-review-proposal-2026-03-19.md +67 -48
  └ signals\specify\proposal\ai-code-review-proposal-2026-03-19.md

Artifact written to `signals/specify/proposal/ai-code-review-proposal-2026-03-19.md` (v2).

**Summary:** Updated proposal from comprehensive AI code review → **narrow AI-code auditor** (Option B), grounded in 38 prior signals. Key changes from v1:

- **Scope narrowed** per discover-compare/synthesize: targets AI-generated PRs only, ~950 hours vs. 1,580
- **Cloud-only v1** eliminates the RED-rated self-hosted LLM risk
- **Risks recalibrated**: Copilot moat neutralized by occupying uncontested whitespace; data sovereignty resolved; top risk remains FP fatigue
- **Shadow-mode phase added** at 30 days (per discover-hypothesis experiment) — 200 PRs calibrated before any public finding
- **Success criteria tightened**: FP threshold from <20% to <15%
- **Alternatives**: Option A (comprehensive tool) explicitly rejected with cross-signal evidence

QUALITY: 5
COMPACT_WORKED: Y
OUTPUT_SIZE: medium


Total usage est:        6 Premium requests
API time spent:         4m 1s
Total session time:     4m 9s
Total code changes:     +67 -48
Breakdown by AI model:
 claude-opus-4.6-1m       250.3k in, 9.6k out, 181.6k cached (Est. 6 Premium requests)
