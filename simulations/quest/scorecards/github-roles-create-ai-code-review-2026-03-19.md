● List directory .
  └ 13 files found

● Read CLAUDE.md
  └ 12 lines read

● Check signals directory (shell)
  │ if (Test-Path "C:\src\sim-test\signals") { Get-ChildItem -Recurse "C:\src\sim-test\signals" }
  │ else { Write-Output "signals/ does not exist" }
  └ 91 lines...

● Check if .craft/roles exists (shell)
  │ Test-Path "C:\src\sim-test\.craft\roles" ; if (Test-Path "C:\src\sim-test\.craft\roles") {
  │ Get-ChildItem -Recurse "C:\src\sim-test\.craft\roles" } else { Write-Output ".craft/roles/ does
  │ not exist" }
  └ 23 lines...

Let me examine existing roles for format conventions and understand the topic context.

● Read false-positive-analyst.md
  │ .craft\roles\product\false-positive-analyst.md
  └ 96 lines read

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L1:80 (80 lines read)

● Read ai-code-review-roles-generate-2026-03-19.md
  │ signals\roles\generate\ai-code-review-roles-generate-2026-03-19.md
  └ L1:80 (80 lines read)

● Read context-depth-reviewer.md
  │ .craft\roles\engineering\context-depth-reviewer.md
  └ 92 lines read

● Read security-scanning-analyst.md
  │ .craft\roles\security\security-scanning-analyst.md
  └ 97 lines read

Let me check the full roles-generate artifact for any gap roles and see the spec for deeper context.

● Read ai-code-review-roles-generate-2026-03-19.md
  │ signals\roles\generate\ai-code-review-roles-generate-2026-03-19.md
  └ L80:200 (121 lines read)

● Read adoption-strategist.md
  │ .craft\roles\product\adoption-strategist.md
  └ 88 lines read

● Read ai-code-review-competitors-2026-03-19.md
  │ signals\discover\competitors\ai-code-review-competitors-2026-03-19.md
  └ L1:60 (60 lines read)

Now I have full context. The key gap: **cross-repo / cross-service architectural review** — the #1 whitespace from the competitive analysis, uncovered by any existing role. Let me create the role and artifact.

● Create signals/roles/create directory (shell)
  │ New-Item -ItemType Directory -Path "C:\src\sim-test\signals\roles\create" -Force | Out-Null;
  │ Write-Output "created"
  └ 2 lines...

● Create cross-repo-review-architect.md +129
  └ .craft\roles\engineering\cross-repo-review-architect.md

● Create ai-code-review-roles-create-2026-03-19.md +151
  └ signals\roles\create\ai-code-review-roles-create-2026-03-19.md

Let me verify both files were written correctly.

● Verify files exist (shell)
  │ Test-Path "C:\src\sim-test\.craft\roles\engineering\cross-repo-review-architect.md"; Test-Path
  │ "C:\src\sim-test\signals\roles\create\ai-code-review-roles-create-2026-03-19.md"; Get-ChildItem
  │ "C:\src\sim-test\.craft\roles\engineering\"
  └ 10 lines...

Done. Created **cross-repo-review-architect** in `.craft/roles/engineering/`.

**Why this role:** The competitive analysis identified cross-repo/cross-service architectural review as the #1 uncontested whitespace — no competitor owns it. All 10 existing roles were scoped to single-repo concerns. This role fills that structural gap with 8 specific verify checks covering dependency graphs, API contract validation, schema migration impact, event contract verification, latency budgeting, graph staleness detection, and cold-start degradation.

**Files written:**
- **Role:** `.craft/roles/engineering/cross-repo-review-architect.md`
- **Artifact:** `signals/roles/create/ai-code-review-roles-create-2026-03-19.md`

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: All three AMEND refinements are substantive. 8 verify items (above 6 minimum). Collaboration edges link cleanly to context-depth-reviewer (boundary handoff), latency-guardian (30s budget), and webhook-pipeline-engineer (fan-out rate limits).


Total usage est:        6 Premium requests
API time spent:         3m 29s
Total session time:     3m 41s
Total code changes:     +280 -0
Breakdown by AI model:
 claude-opus-4.6-1m       313.3k in, 10.1k out, 267.9k cached (Est. 6 Premium requests)
