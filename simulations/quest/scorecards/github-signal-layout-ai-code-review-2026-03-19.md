● Search (glob)
  │ ".craft/skills/**/*"
  └ No matches found

● Search (glob)
  │ "signals/**/*-*.md"
  └ 38 files found

● Search (glob)
  │ ".claude/skills/**/*"
  └ 285 files found

```
YOUR CURRENT LAYOUT: FLAT (with signal-prefix duplicates)

How your skills are named:
  /discover-competitors    <- flat style (namespace-skill)
  /discover-risk
  /flow-lifecycle
  /prove-hypothesis
  /review-design
  /listen-feedback
  /mock-all
  /draft-spec
  /topic-status
  /rhythm-status
  ...

  Also installed: signal-prefix variants (e.g. /signal-prove-websearch)
  Also installed: aggregator menus (e.g. /discover, /validate, /simulate)

Skills detected:  ~178 skill folders in .claude/skills/
  - FLAT commands:     ~80  (discover-X, flow-X, prove-X, review-X, etc.)
  - SIGNAL-prefix:     ~70  (signal-flow-X, signal-prove-X, signal-org-X, etc.)
  - Aggregator menus:  ~20  (discover, specify, simulate, validate, etc.)
  - Utility/meta:       ~8  (signal-layout, signal-health, signal-setup, etc.)

Signals artifacts:  38 across 8 namespaces (topic: ai-code-review)
  discover:   13  (competitors, feasibility, brainstorm, causal, coherence, compare,
                    hypothesis, inertia, risk, synthesize, websearch, + alt variants)
  validate:    7  (design, customers, code, feedback, support, adoption, adoption-blocker)
  roles:       5  (build, create, generate, scan, pull-request)
  specify:     3  (proposal, pitch, commitment)
  review:      3  (design, users, customers)
  simulate:    3  (lifecycle, contract, request)
  rhythm:      3  (story, decide, behavior)
  draft:       1  (spec)

This is how you run Signal skills in this workspace:
  /discover-competitors   (primary — FLAT style)
  /signal-discover-competitors  (also works — SIGNAL prefix)

NOTE: Your workspace has both FLAT and SIGNAL-prefix variants installed.
The FLAT commands (/discover-competitors) are the shorter, primary path.
The signal-prefix variants (/signal-discover-competitors) exist as duplicates.
```

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: Glob-based detection works well in Copilot. The workspace has a hybrid layout (flat + signal-prefix duplicates + aggregator menus), likely from multiple installs or a comprehensive install script. No issues running this display-only skill in GitHub Copilot CLI.


Total usage est:        6 Premium requests
API time spent:         57s
Total session time:     1m 19s
Total code changes:     +0 -0
Breakdown by AI model:
 claude-opus-4.6-1m       66.7k in, 2.4k out, 46.2k cached (Est. 6 Premium requests)
