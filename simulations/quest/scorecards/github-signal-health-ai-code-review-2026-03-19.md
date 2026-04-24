● List directory .
  └ 13 files found

● Check CLAUDE.md and signals/ (shell)
  │ Test-Path "C:\src\sim-test\CLAUDE.md" ; Test-Path "C:\src\sim-test\signals"
  └ 3 lines...

● Check skills directory (shell)
  │ Test-Path "C:\src\sim-test\.claude\skills" ; if (Test-Path "C:\src\sim-test\.claude\skills") {
  │ Get-ChildItem "C:\src\sim-test\.claude\skills" -Directory | Measure-Object | Select-Object
  │ -ExpandProperty Count } else { "no-skills-dir" }
  └ 3 lines...

● List directory signals
  └ 8 files found

● List skill directories (shell)
  │ # Count total skill directories
  │ Get-ChildItem "C:\src\sim-test\.claude\skills" -Directory | Select-Object -ExpandProperty Name |
  │ Sort-Object
  └ 286 lines...

● Inventory artifacts per namespace (shell)
  │ # Count .md files per namespace and get dates
  │ Get-ChildItem "C:\src\sim-test\signals" -Directory | ForEach-Object {
  │ $ns = $_.Name
  │ $files = Get-ChildItem $_.FullName -Filter "*.md" -ErrorAction SilentlyContinue
  │ $count = ($files | Measure-Object).Count…
  └ 22 lines...

● Count all signal artifacts recursively (shell)
  │ # Check for any .md files deeper in signals/ (maybe nested)
  │ Get-ChildItem "C:\src\sim-test\signals" -Recurse -Filter "*.md" | Measure-Object | Select-Object
  │ -ExpandProperty Count
  └ 2 lines...

● Count skill variants (shell)
  │ # Count unique skill names (excluding .t3 variants)
  │ $all = Get-ChildItem "C:\src\sim-test\.claude\skills" -Directory | Select-Object
  │ -ExpandProperty Name
  │ $base = $all | Where-Object { $_ -notmatch '\.t3$' }
  │ "Total skill dirs: $($all.Count)"…
  └ 6 lines...

● List all signal artifacts with dates (shell)
  │ # Show the 38 artifacts with their namespaces
  │ Get-ChildItem "C:\src\sim-test\signals" -Recurse -Filter "*.md" | ForEach-Object {
  │ $ns = $_.Directory.Name
  │ $parent = if ($_.Directory.Parent.Name -eq "signals") { $ns } else {
  │ "$($_.Directory.Parent.Name)/$ns" }…
  └ 47 lines...

Now I have everything. Let me compile the health report.

---

# 🏥 Signal Health Check — `ai-code-review`

## 1. Skills Installed?

✅ **285 skill directories** found in `.claude/skills/`
- **220** base skills
- **65** `.t3` variants

All critical namespaces covered: discover, draft, flow, listen, mock, org, prove, quest, review, rhythm, roles, scout, signal, simulate, specify, topic, trace, validate.

## 2. signals/ Directory Present?

✅ **Present** — 8 top-level namespaces found:
`discover`, `draft`, `review`, `rhythm`, `roles`, `simulate`, `specify`, `validate`

## 3. CLAUDE.md Present?

✅ **Present** at workspace root.

## 4. Artifact Inventory

| Namespace | Artifact Count | Most Recent | Oldest |
|-----------|---------------|-------------|--------|
| discover | 13 | brainstorm (07:19) | competitors (06:28) |
| draft | 1 | spec (06:29) | spec (06:29) |
| review | 3 | customers (07:12) | design (07:06) |
| rhythm | 3 | behavior (07:02) | websearch-story (06:51) |
| roles | 5 | pull-request (07:38) | scan (06:29) |
| simulate | 3 | request (07:41) | contract (06:42) |
| specify | 3 | commitment (06:38) | proposal (06:32) |
| validate | 7 | customers (07:31) | adoption (06:50) |
| **Total** | **38** | **request (07:41)** | **competitors (06:28)** |

All artifacts dated **2026-03-19**, spanning ~1h13m of activity.

## Health Score

| Check | Status | Notes |
|-------|--------|-------|
| Skills installed | ✅ **OK** | 220 base + 65 t3 = 285 dirs |
| signals/ present | ✅ **OK** | 8 namespaces, 38 artifacts |
| CLAUDE.md present | ✅ **OK** | Present at root |
| Artifact count ≥ 1 | ✅ **OK** | 38 artifacts across all namespaces |

### Overall: 🟢 HEALTHY

## Observations

- **Deep coverage** in `discover` (13 artifacts) — full discovery campaign completed.
- **Validate** is strong at 7 artifacts including adoption-blocker analysis.
- **No `flow/`, `prove/`, `listen/`, `scout/`, `trace/`, `topic/` namespace artifacts** in signals/ — these namespaces have no subdirectories yet. Skills exist but haven't been run for this topic.
- All work happened in a single day — this is a freshly-spun campaign.

## Recommendations

1. **Run `prove-hypothesis`** — no prove-namespace artifacts yet; grounding claims with evidence would strengthen the case.
2. **Run `flow-lifecycle` or `flow-conversation`** — no flow artifacts; behavioral simulations would validate integration paths.
3. **Run `listen-feedback`** — no listen artifacts; pre-ship customer reaction simulation adds validation depth.
4. **Run `topic-new` → `topic-status`** — no topic artifacts; registering the topic enables roadmap tracking.

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: All filesystem checks work identically in Copilot CLI. Parallel tool calls for directory scanning performed well. No Copilot-specific issues encountered — `Get-ChildItem` and `Test-Path` are reliable across both runtimes.


Total usage est:        6 Premium requests
API time spent:         1m 0s
Total session time:     1m 36s
Total code changes:     +0 -0
Breakdown by AI model:
 claude-opus-4.6-1m       161.9k in, 2.6k out, 141.6k cached (Est. 6 Premium requests)
