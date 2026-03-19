● Search (glob)
  │ ".craft/skills/*/SKILL.md"
  └ No matches found

● Search (glob)
  │ ".craft/**/*.md"
  └ 11 files found

● Search (glob)
  │ ".claude/skills/*/SKILL.md"
  └ 285 files found

● Search (glob)
  │ ".claude/**/*.md"
  └ 285 files found

Now let me extract descriptions from the base skills (excluding `signal-` prefixed aliases and `.t3` variants):

● Extract skill descriptions from base skills (shell)
  │
  │ # Get all base skill directories (no signal- prefix, no .t3 suffix)
  │ $skills = Get-ChildItem ".\.claude\skills" -Directory | Where-Object { $_.Name -notmatch
  │ '^signal-' -and $_.Name -notmatch '\.t3$' } | Sort-Object Name
  │ $skills | ForEach-Object {…
  └ 150 lines...

The first lines are just YAML frontmatter. Let me extract the `description` field:

● Extract description field from YAML (shell)
  │
  │ $skills = Get-ChildItem ".\.claude\skills" -Directory | Where-Object { $_.Name -notmatch
  │ '^signal-' -and $_.Name -notmatch '\.t3$' } | Sort-Object Name
  │ $skills | ForEach-Object {
  │ $file = Join-Path $_.FullName "SKILL.md"…
  └ 154 lines...

Let me look at the actual structure of a few skill files to understand the format:

● Read SKILL.md
  │ .claude\skills\discover-competitors\SKILL.md
  └ L1:20 (20 lines read)

● Read SKILL.md
  │ .claude\skills\draft-spec\SKILL.md
  └ L1:20 (20 lines read)

● Read SKILL.md
  │ .claude\skills\tools-preview\SKILL.md
  └ L1:20 (19 lines read)

● Read SKILL.md
  │ .claude\skills\signal\SKILL.md
  └ L1:20 (20 lines read)

Now I can see the format. Let me extract all descriptions properly:

● Count skill categories (shell)
  │
  │ # Count all skill categories
  │ $all = Get-ChildItem ".\.claude\skills" -Directory
  │ $base = $all | Where-Object { $_.Name -notmatch '^signal-' -and $_.Name -notmatch '\.t3$' }
  │ $signalPrefixed = $all | Where-Object { $_.Name -match '^signal-' -and $_.Name -notmatch …
  └ 12 lines...

● Extract descriptions from YAML frontmatter (shell)
  │
  │ $skills = Get-ChildItem ".\.claude\skills" -Directory | Where-Object { $_.Name -notmatch
  │ '^signal-' -and $_.Name -notmatch '\.t3$' } | Sort-Object Name
  │ $skills | ForEach-Object {
  │ $file = Join-Path $_.FullName "SKILL.md"…
  └ 155 lines...

Let me check the official namespace structure from the signal index:

● Read SKILL.md
  │ .claude\skills\signal\SKILL.md
  └ 65 lines read

Now I have all the data. Here's the complete preview:

---

```
INSTALLED SIGNAL SKILLS
========================
Binding:  SIGNAL (skills bound via .claude/skills/ directory)
Location: .claude/skills/
Total:    141 base skills + 79 signal-prefixed aliases + 65 t3 variants = 285 dirs

Official index: 62 skills across 9 namespaces (per /signal)

════════════════════════════════════════════════════════════════════
 CAMPAIGNS — Orchestrated multi-skill runs (6 entry points)
════════════════════════════════════════════════════════════════════
  /rhythm-decide          Full pre-commitment decision campaign
  /rhythm-behavior        Technical simulation campaign
  /rhythm-qa              Design validation campaign
  /rhythm-brief           Topic narrative campaign
  /rhythm-story           Editorial synthesis of all signals
  /rhythm-status          Topic coverage and commitment readiness (display only)
  /rhythm-achievements    Show achievements earned for a topic (display only)
  /evidence               Full evidence campaign (hypothesis → synthesis)
  /decide                 Full decision suite (scout + prove + draft)

════════════════════════════════════════════════════════════════════
 DISCOVERY (16 skills)
════════════════════════════════════════════════════════════════════
  /discover-competitors      Competitive landscape with inertia-first framing
  /discover-competitors-alt  Unified competitive analysis (alt variant)
  /discover-feasibility      Technical feasibility assessment
  /discover-feasibility-alt  Unified feasibility analysis (alt variant)
  /discover-hypothesis       State a falsifiable hypothesis
  /discover-inertia          Deep analysis of the "do nothing" option
  /discover-risk             Risk register across technical/adoption/market
  /discover-brainstorm       Idea pool generation (more than you need)
  /discover-websearch        Ground claims with web evidence
  /discover-analysis         Analyze data/telemetry/schemas for patterns
  /discover-causal           Test causal mechanism linking feature to outcome
  /discover-synthesize       Cross-signal insight synthesis (PROCEED/PAUSE/PIVOT)
  /discover-coherence        Check if discover signals agree (needs 2+ signals)
  /discover-compare          Compare options with inertia as Option 0
  /discover-orchestrate      Sequence remaining discover skills (display only)

════════════════════════════════════════════════════════════════════
 SCOUT (9 skills) — PM proves the idea
════════════════════════════════════════════════════════════════════
  /scout-competitors      Competitive landscape (inertia as primary competitor)
  /scout-compliance       Regulatory and policy constraint scan
  /scout-feasibility      Technical feasibility with traffic-light ratings
  /scout-market           Market sizing and segment ranking
  /scout-naming           Name generation with multi-persona scoring
  /scout-positioning      Per-audience positioning statements
  /scout-requirements     Requirements extraction with MoSCoW prioritization
  /scout-stakeholders     Stakeholder mapping with power/interest grid

════════════════════════════════════════════════════════════════════
 SPECIFICATION (5 skills) — Author writes the design
════════════════════════════════════════════════════════════════════
  /specify-spec           Author a specification with guided structure
  /specify-proposal       Feature proposal with problem/solution/options
  /specify-pitch          Pitch deck narrative (exec/developer/maker)
  /specify-commitment     Staged program plan with gates

════════════════════════════════════════════════════════════════════
 DRAFT (5 skills) — Guided authoring
════════════════════════════════════════════════════════════════════
  /draft-spec             Specification authoring with self-review
  /draft-proposal         Proposal/ADR with three-option minimum
  /draft-pitch            Pitch deck narrative in 3 versions
  /draft-brainstorm       Idea pool with inertia baseline scoring

════════════════════════════════════════════════════════════════════
 PROVE (11 skills) — Hypothesis-first investigation
════════════════════════════════════════════════════════════════════
  /prove-hypothesis       Hypothesis framing with falsification condition
  /prove-websearch        Web evidence with quotes, URLs, strength rating
  /prove-analysis         Data pattern analysis (correlation vs causation)
  /prove-intelligence     Internal source evidence with file-path citations
  /prove-interview        Persona-driven stakeholder interview simulation
  /prove-program          General-purpose research orchestrator
  /prove-prototype        Smallest-possible prototype with measure
  /prove-publish          Investigation write-up as paper
  /prove-synthesize       Answer-first evidence synthesis with confidence
  /prove-topic            Full prove campaign (hypothesis → synthesis)

════════════════════════════════════════════════════════════════════
 VALIDATION (10 skills) — Team validates the design
════════════════════════════════════════════════════════════════════
  /validate-design        Multi-expert review through 6 disciplines
  /validate-code          Multi-discipline code review (pass/fail)
  /validate-users         5 persona advocates walk through design
  /validate-customers     12 customer personas evaluate feature
  /validate-feedback      Customer reaction simulation (pre-ship NPS)
  /validate-support       Predict top support tickets (first 90 days)
  /validate-adoption      Adoption curve simulation (Rogers archetypes)
  /validate-adoption-blocker  Identify what blocks adoption (P1/P2)
  /validate-inertia       Stress-test the inertia/"do nothing" scenario

════════════════════════════════════════════════════════════════════
 REVIEW (5 skills) — Expert review
════════════════════════════════════════════════════════════════════
  /review-design          Multi-expert design review (6 disciplines)
  /review-code            Multi-discipline code review (file-level)
  /review-users           5 persona advocates with usability scores
  /review-customers       12 customer personas evaluate feature

════════════════════════════════════════════════════════════════════
 SIMULATION (8 skills) — Technical behavior simulation
════════════════════════════════════════════════════════════════════
  /simulate-lifecycle     Full business process lifecycle simulation
  /simulate-request       Hand-compile request through service boundaries
  /simulate-state         State transition hand-compilation
  /simulate-contract      Verify implementation against spec contract
  /simulate-conversation  Multi-turn agent conversation simulation
  /simulate-permissions   RBAC/security role trace
  /simulate-stress        Degraded condition simulation (offline/failure)

════════════════════════════════════════════════════════════════════
 FLOW (8 skills) — Business process flows
════════════════════════════════════════════════════════════════════
  /flow-lifecycle         Business document lifecycle with phase contracts
  /flow-conversation      Agent conversation with dead-end/loop detection
  /flow-dataflow          ETL pipeline tracing with data loss detection
  /flow-integration       Cross-system integration with gap analysis
  /flow-resilience        Degraded-condition simulation (offline/failure)
  /flow-throttle          Rate-limit throughput with backpressure
  /flow-trigger           Automation trigger fire order and side effects

════════════════════════════════════════════════════════════════════
 TRACE (9 skills) — Platform-level tracing
════════════════════════════════════════════════════════════════════
  /trace-request          Request hand-compilation through boundaries
  /trace-state            State transition with pre/postconditions
  /trace-contract         Expected vs actual output comparison
  /trace-component        UI component tree action tracing
  /trace-deployment       Deployment sequence with rollback paths
  /trace-migration        Schema change with data loss detection
  /trace-permissions      RBAC walk-through with privilege escalation
  /trace-skill            Hand-compile a skill execution before building

════════════════════════════════════════════════════════════════════
 LISTEN (4 skills) — Post-ship feedback simulation
════════════════════════════════════════════════════════════════════
  /listen-feedback        Customer reaction simulation (per-persona NPS)
  /listen-support         Top support ticket prediction (90 days)
  /listen-adoption        Adoption curve across Rogers archetypes

════════════════════════════════════════════════════════════════════
 TOPIC & NARRATIVE (8 skills)
════════════════════════════════════════════════════════════════════
  /topic-new              Register topic with strategy + signal plan
  /topic-plan             Signal strategy revision as info arrives
  /topic-status           Coverage display from signal glob (terminal)
  /topic-report           Shareable status document with readiness
  /topic-story            Editorial synthesis with recommendation
  /topic-echo             Unexpected findings synthesis
  /topic-scanner          Discover all signals for a topic via glob

════════════════════════════════════════════════════════════════════
 GOVERNANCE / ROLES (10 skills)
════════════════════════════════════════════════════════════════════
  /roles-scan             Walk repo, produce draft org.yaml
  /roles-generate         Generate typed role registry for a domain
  /roles-build            Build role YAML in .craft/roles/
  /roles-create           Create new role or sub-role
  /roles-chart            Inspect installed role registry (display only)
  /roles-check            Run artifact through full org
  /roles-committee        Simulate committee meeting (ROB/shiproom/arch)
  /roles-product-review   Run Review of Business stages
  /roles-pull-request     Run PR through full org
  /roles-leaderboard      Team achievement leaderboard (display only)

════════════════════════════════════════════════════════════════════
 MOCK (4 skills) — Synthetic signal generation
════════════════════════════════════════════════════════════════════
  /mock-all               Synthetic artifacts for all 9 namespaces
  /mock-ns                Mock artifact for a single namespace
  /mock-review            Mock coverage review (MOCK-ACCEPTED/REAL-REQUIRED)

════════════════════════════════════════════════════════════════════
 QUEST (6 skills) — Prompt engineering
════════════════════════════════════════════════════════════════════
  /quest-golden           Find the golden prompt (full loop)
  /quest-rubric           Define what good output looks like
  /quest-score            Score N outputs against a rubric
  /quest-variate          Generate N distinct prompt variations
  /quest-engine           Runs quest loop: variate → score → evolve

════════════════════════════════════════════════════════════════════
 PROGRAM (2 skills) — Program management
════════════════════════════════════════════════════════════════════
  /program-plan           Staged program plan with gates + topic tracking

════════════════════════════════════════════════════════════════════
 TOOLS + SIGNAL (6 skills)
════════════════════════════════════════════════════════════════════
  /signal                 Command index — lists all skills by namespace
  /signal-health          Check workspace health
  /signal-setup           Initial workspace setup
  /signal-layout          Show workspace layout
  /tools-coverage         Signal coverage statistics for a topic
  /tools-preview          This skill — shows installed skills
  /tools-accept           Review mock coverage, produce acceptance

════════════════════════════════════════════════════════════════════
 UTILITIES (4 skills)
════════════════════════════════════════════════════════════════════
  /achievements           Show achievements earned for a topic
  /artifact-writer        Write signal artifacts with standard frontmatter
  /skill-tracer           Execute trace-skill hand-compilation protocol
  /track                  Manage topic narrative + program plan

════════════════════════════════════════════════════════════════════
 ALSO INSTALLED
════════════════════════════════════════════════════════════════════
  79 signal-prefixed aliases   (e.g., /signal-draft-spec → /draft-spec)
  65 .t3 test variants         (e.g., /discover-causal.t3)
  11 .craft/roles/             (security, product, platform, engineering)


QUICK START for topic: ai-code-review
═══════════════════════════════════════
  1. /discover-competitors ai-code-review   Scout inertia + named competitors
  2. /specify-spec ai-code-review           Write the specification
  3. /tools-coverage ai-code-review         Check which signals are missing

Or run a full campaign:
  /rhythm-decide ai-code-review            Full pre-commitment decision suite
```

---

**QUALITY:** 4
**COPILOT_COMPATIBLE:** Y
**NOTES:** All 285 skill directories scanned successfully. Glob + PowerShell extraction worked on Windows without issues. The `signal-` prefixed aliases and `.t3` variants inflate the directory count but the core index of ~62 curated skills is intact. No Copilot-specific issues — skill files are plain Markdown with YAML frontmatter, readable by any tool.


Total usage est:        6 Premium requests
API time spent:         2m 13s
Total session time:     2m 28s
Total code changes:     +0 -0
Breakdown by AI model:
 claude-opus-4.6-1m       299.6k in, 7.1k out, 265.1k cached (Est. 6 Premium requests)
