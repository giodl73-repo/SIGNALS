● List directory .
  └ 27 files found

● Search (glob)
  │ ".claude/skills/**/*"
  └ No matches found

● Search (glob)
  │ "signals/**/*.md"
  └ 151 files found

Now let me check for skills and examine the namespace subdirectories more closely.

● List directory signals
  └ 140 files found

● List directory .claude
  └ 2 files found

● List namespaced artifact files with dates (shell)
  │ Get-ChildItem -Path "C:\src\sim\signals" -Recurse -Filter "*.md" -File | Where-Object {
  │ $_.FullName -match "\\signals\\[a-z]+\\[a-z]+\\" } | Select-Object FullName, LastWriteTime |
  │ Sort-Object LastWriteTime -Descending
  └ 20 lines...

● Read signal.manifest.json
  └ 1 line read

● Read signal.skills.yaml
  └ L1:50 (50 lines read)

● Count artifacts per namespace for ai-code-review (shell)
  │ # Count artifacts per namespace subdirectory for topic ai-code-review
  │ $namespaces = @('discover','specify','validate','simulate','scout','trace','flow','prove','top
  │ ic','rhythm','roles')
  │ foreach ($ns in $namespaces) {
  │ $path = "C:\src\sim\signals\$ns"…
  └ 28 lines...

● Read signal.manifest.json
  └ L1:40 (40 lines read)

● Count skills and check .claude contents (shell)
  │ # Count all skill definitions in signal.skills.yaml
  │ $content = Get-Content "C:\src\sim\signal.skills.yaml" -Raw
  │ $matches = [regex]::Matches($content, '- id: ')
  │ Write-Output "Total skills defined in signal.skills.yaml: $($matches.Count)"…
  └ 27 lines...

● Analyze manifest namespaces (shell)
  │ # Get all unique namespaces from manifest
  │ $json = Get-Content "C:\src\sim\signal.manifest.json" -Raw | ConvertFrom-Json
  │ $namespaces = $json.skills | ForEach-Object { $_.namespace } | Sort-Object -Unique
  │ Write-Output "Namespaces in manifest.json:"
  │ $namespaces | ForEach-Object { Write-Output "  - $_" }…
  └ 38 lines...

Now I have all the data. Here's the health check:

---

## `/signal-health` — Topic: ai-code-review

### 1. Skills Installed?

**No `.claude/skills/` directory found.** Skills are defined externally in:
- `signal.skills.yaml` — 62 skills across 10 namespaces (discover, specify, validate, simulate, rhythm, roles, signal, tools, topic, quest)
- `signal.manifest.json` — 67 skills (63 user-facing) across 14 namespaces (scout, draft, review, flow, listen, prove, trace, topic, quest, program, mock, campaign, corps, crew)

**Result:** 0 skills installed in `.claude/skills/` / 62-67 defined in config files. Skills operate as prompt-based definitions, not installed skill directories.

### 2. signals/ Directory Present?

**Present.** Subdirectories with `ai-code-review` artifacts:

| Subdirectory | Status |
|---|---|
| `discover/` | ✓ (6 artifacts) |
| `specify/` | ✓ (1 artifact) |
| `validate/` | ✓ (4 artifacts) |
| `simulate/` | ✓ (2 artifacts) |
| `rhythm/` | ✓ (2 artifacts) |
| `roles/` | ✓ (2 artifacts) |
| scout/, trace/, flow/, prove/, topic/ | Not created |

Also contains ~100+ skill definition `.md` files at signals/ root level.

### 3. CLAUDE.md Present?

**Present** at `C:\src\sim\CLAUDE.md`. ✓

### 4. Artifact Inventory — Topic: `ai-code-review`

| Namespace | Count | Most Recent | Oldest |
|-----------|-------|-------------|--------|
| discover | 6 | 2026-03-19 | 2026-03-18 |
| specify | 1 | 2026-03-18 | 2026-03-18 |
| validate | 4 | 2026-03-19 | 2026-03-18 |
| simulate | 2 | 2026-03-19 | 2026-03-18 |
| scout | 0 | — | — |
| trace | 0 | — | — |
| flow | 0 | — | — |
| prove | 0 | — | — |
| topic | 0 | — | — |
| rhythm | 2 | 2026-03-19 | 2026-03-18 |
| roles | 2 | 2026-03-19 | 2026-03-18 |
| **Total** | **17** | **2026-03-19** | **2026-03-18** |

### Health Score

| Check | Status | Notes |
|-------|--------|-------|
| Skills installed | **WARN** | No `.claude/skills/` dir; skills defined in YAML/JSON config files only |
| signals/ present | **OK** | Present with 6 active namespace subdirs + ~100 skill definition files |
| CLAUDE.md present | **OK** | Present at workspace root |
| Artifact count ≥ 1 | **WARN** | 17 artifacts across 6/10 namespaces; 4 namespaces empty (scout, trace, flow, prove) |

**Overall: DEGRADED**

### Recommendations

1. **Run scout, trace, flow, prove skills** — 4 namespaces have zero artifacts for `ai-code-review`. Running `/scout-competitors`, `/trace-contract`, `/flow-lifecycle`, `/prove-hypothesis` would fill coverage gaps.
2. **Create `/topic-status` artifact** — No topic-namespace artifact exists to synthesize the 17 signals gathered so far. Run `/topic-status ai-code-review` to get a readiness assessment.
3. **Add more specify artifacts** — Only 1 proposal exists. Consider `/specify-spec` or `/specify-commitment` to strengthen the specification layer.
4. **Consider `.claude/skills/` installation** — If Claude Code skill dispatch is desired, skill `.md` files need to be placed in `.claude/skills/`. Current setup relies on YAML/JSON config which works for prompt-based invocation.

---

```
QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: Copilot resolved all paths and glob patterns correctly on Windows.
  Dual skill registries (YAML vs JSON manifest) with different namespace
  mappings may cause confusion -- the health check used actual directory
  structure as ground truth. No issues with tool availability; grep/glob/view
  all functioned as expected.
```


Total usage est:        6 Premium requests
API time spent:         1m 24s
Total session time:     1m 49s
Total code changes:     +0 -0
Breakdown by AI model:
 claude-opus-4.6-1m       171.5k in, 4.1k out, 151.5k cached (Est. 6 Premium requests)
