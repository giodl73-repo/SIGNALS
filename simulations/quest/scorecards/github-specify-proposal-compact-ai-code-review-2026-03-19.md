● List directory .
  └ 13 files found

● Read CLAUDE.md
  └ 17 lines read

● Search (glob)
  │ "signals/**/ai-code-review-*"
  └ 41 files found

There are 41 prior signals — very strong coverage. Let me read the key discovery signals to ground this proposal.

● Read ai-code-review-competitors-2026-03-19.md
  │ signals\discover\competitors\ai-code-review-competitors-2026-03-19.md
  └ 219 lines read

● Read ai-code-review-hypothesis-2026-03-19.md
  │ signals\discover\hypothesis\ai-code-review-hypothesis-2026-03-19.md
  └ 56 lines read

● Read ai-code-review-synthesize-2026-03-19.md
  │ signals\discover\synthesize\ai-code-review-synthesize-2026-03-19.md
  └ 129 lines read

● Read ai-code-review-feasibility-2026-03-19.md
  │ signals\discover\feasibility\ai-code-review-feasibility-2026-03-19.md
  └ 157 lines read

● Read ai-code-review-causal-2026-03-19.md
  │ signals\discover\causal\ai-code-review-causal-2026-03-19.md
  └ 182 lines read

● Read ai-code-review-risk-2026-03-19.md
  │ signals\discover\risk\ai-code-review-risk-2026-03-19.md
  └ 77 lines read

Now let me read the existing proposal and a few more key signals:

● Read ai-code-review-compare-2026-03-19.md
  │ signals\discover\compare\ai-code-review-compare-2026-03-19.md
  └ 175 lines read

● Read ai-code-review-proposal-2026-03-19.md
  │ signals\specify\proposal\ai-code-review-proposal-2026-03-19.md
  └ 141 lines read

● Read ai-code-review-inertia-2026-03-19.md
  │ signals\discover\inertia\ai-code-review-inertia-2026-03-19.md
  └ 175 lines read

I have thorough context from 41 prior signals. The existing v2 proposal is solid — I'll produce a tighter v3 incorporating the full signal corpus. Let me write it.

● Edit ai-code-review-proposal-2026-03-19.md +61 -62
  └ signals\specify\proposal\ai-code-review-proposal-2026-03-19.md

Proposal v3 written to `signals/specify/proposal/ai-code-review-proposal-2026-03-19.md`.

**Key v2→v3 changes:**
- Incorporated validate REVISE verdicts (NPS 6.8, customer 3.58/5, contract FAIL) into risks and success criteria
- Added 0.85 confidence threshold default + developer engagement rate ≥60% at 60-day gate
- Softened cycle time claim from ≥30% to ≥25% per amended hypothesis (causal T2 evidence gap)
- Integrated synthesize insights: precision as data moat, self-selecting beachhead, coherence paradox strengthening Option B
- Signal count 38→41; added simulate-contract finding to Security alignment
- Recommended next actions: `/prove-prototype` (highest leverage), Copilot websearch (clears coherence), reframe for REVISE remediation

QUALITY: 4
COMPACT_WORKED: Y
OUTPUT_SIZE: medium


Total usage est:        6 Premium requests
API time spent:         3m 24s
Total session time:     3m 37s
Total code changes:     +61 -62
Breakdown by AI model:
 claude-opus-4.6-1m       269.0k in, 10.0k out, 189.9k cached (Est. 6 Premium requests)
