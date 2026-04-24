---
topic: signal
date: 2026-03-14
source: scout namespace trace-skill runs (wave 1 + wave 2)
status: open
dcr: pending
---

# Signal Plugin Findings -- 2026-03-14

All findings from this session. DCR to be filed tonight.

---

## Craftworks CLI Findings (report to craftworks repo)

### CF-01: Double frontmatter in generated SKILL.md [MAJOR]
**CLI version**: v0.36.78
**Command**: `craft generate --stage program`
Every generated SKILL.md has the frontmatter block emitted twice (lines 1-6 AND 7-12).
**Expected**: Single frontmatter block.
**Log**: C:\Users\giodl\.roles\.logs\craft-cli_20260314T203308Z.log

### CF-02: --hydrate flag not in compiled CLI [MAJOR]
**CLI version**: v0.36.78
**Source**: Flag defined in `craft-cli/src/commands/generate.ts` as `--hydrate`
(LLM-assisted skill body synthesis, Stage 30b, DCR-133)
**Observed**: `craft generate --hydrate` returns `error: unknown option '--hydrate'`
**Expected**: Flag fills ## Algorithm stubs with LLM-generated skill body content.

### CF-03: program.yaml description cap of 1024 chars too small for skill methodology [MAJOR]
**Impact**: Skill descriptions that hold methodology (lifecycle, roles, examples) cannot
fit in 1024 chars. Developers must maintain a separate registry (signal.skills.yaml)
and keep program.yaml as a thin stub. The description field should support multi-line
prose without character limit, OR program.yaml should support an `action:` file reference
to a separate skill body file.
**Workaround**: signal.skills.yaml as the real source of truth; program.yaml as a thin
generation target with truncated descriptions.

---

## Signal Spec Findings (apply to signal specs)

### SF-SCOUT-01: Artifact naming used old sim- prefix [FIXED]
All 8 scout skill artifact paths used `sim-` prefix instead of `{topic}-`.
**Fixed**: Updated all artifact paths in signal-scout-2026-03-14.md to
`simulations/scout/{skill}/{topic}-{skill}-{date}.md`.

### SF-SCOUT-02: "None / status quo" competitor row missing from spec [FIXED]
scout-competitors setup did not require including inertia as a competitor row.
**Fixed**: Added to setup: "Always include 'none / status quo' as a competitor row."

### SF-SCOUT-03: WebSearch tool not explicit in spec [FIXED]
scout-competitors spec did not explicitly state to use WebSearch to verify claims.
**Fixed**: Added Tools line to spec with note to verify claims via WebSearch.

### SF-SCOUT-04: --mode risk flag missing from scout-competitors [FIXED]
No flag to reframe competitive matrix as "cost of not acting" brief for exec audiences.
**Fixed**: Added --mode risk flag to scout-competitors spec.

### SF-SCOUT-05: scout-feasibility silent fallback when stack files missing [FIXED]
When package.json / tsconfig.json not found, skill silently falls back to CLAUDE.md
assertion. Should surface: "Stack inferred from CLAUDE.md assertion only -- no
package.json found."

### SF-SCOUT-06: scout-feasibility does not surface inferred team/timeline [FIXED]
When --timeline and --team flags are omitted, the skill infers them silently.
Spec should require: show inferred values to user before proceeding.

### SF-SCOUT-07: No SKILL.md schema in repo -- Architect cannot score authoring complexity [OPEN]
scout-feasibility Architect role cannot accurately assess authoring complexity for
48 skills because no canonical SKILL.md schema or template exists in the repo.
**Dependency**: SKILL.md template is a sprint-0 prerequisite for accurate feasibility.

### SF-SCOUT-08: scout-naming missing --validate <name> flag [FIXED]
Validation of an existing name is accidental (name must be included in input to be
scored). A --validate <name> flag should pin the named candidate at row 1 and add a
"Validation Summary" block.

### SF-SCOUT-09: scout-compliance SR 11-7 misclassification risk [FIXED]
Spec does not explicitly state that SR 11-7 applies to the AI model (Claude), not to
a structured prompt methodology (Signal). Compliance officers may misclassify Signal
as the SR 11-7 scope. Add framing note to spec.

### SF-SCOUT-10: scout-market mixes dollar and headcount TAM units [FIXED]
Spec example mixes dollar-figure TAM (enterprise segments) with developer-headcount
TAM (tooling segments) in the same table. Standardize: use headcount for tooling
segments, dollar TAM for platform/enterprise segments. Never mix in one table.

### SF-SCOUT-11: scout-market scoring scale not standardized in spec [FIXED]
PM scoring for segment fit (pain severity, WTP, accessibility) has no defined scale,
weights, or composite formula. Standardize: 1-10, equal weights, composite = average.

### SF-SCOUT-12: scout-stakeholders CODEOWNERS fallback undefined [FIXED]
Spec says "infer from CODEOWNERS" but gives no fallback when CODEOWNERS is absent.
Add explicit rule: "If CODEOWNERS absent, extract org context from invocation. If
invocation also insufficient, ask one question: What org is this for?"

### SF-SCOUT-13: scout-positioning no fallback for missing prior competitors run [OPEN]
Spec says "pull from prior /scout:competitors run if available" with no fallback.
Silent degradation -- skill misses the "inertia is primary competitor" finding.
Add: note degradation, run competitor identification inline, flag "run scout-competitors
for richer positioning."

### SF-SCOUT-14: scout-positioning "quantified confidence score" claim ahead of spec [FIXED]
No single composite confidence score exists in the spec. Either add it or soften
claim to "evidence-backed brief with scored dimensions."

### SF-SCOUT-15: scout-requirements search path undefined [FIXED]
Spec says "pull context from any prior scout runs" but does not specify which directories
to search. Must search BOTH simulations/scout/ (real runs) AND simulations/trace/skill/
(hand-compiled traces).

### SF-SCOUT-16: scout-requirements binding equivalence testing gap [OPEN]
No spec for validating that flat binding and grouped binding produce equivalent skill
behavior. This is a pre-sprint blocker -- equivalence is the core claim of binding-agnostic
design.

---

## Design Findings (Signal plugin architecture)

### DF-01: program.yaml is not a good skill registry -- 1024 char description cap [see CF-03]
**Resolution**: signal.skills.yaml created as the canonical skill registry (no char limit,
full methodology per skill). program.yaml is a thin generation target derived from it.

### DF-02: Agent write permissions do not work with bypassPermissions mode [INFRASTRUCTURE]
Agents launched with mode: bypassPermissions still cannot write new files to disk.
Write operations require the main session to create placeholder files first; agents
can then Edit. This breaks the "agents write to disk" pattern from PROMPT-HANDOVER.md.
**Workaround**: Create placeholders in main session, agents Edit. Or main session writes
directly from agent results.

---

## Open Items for DCR

Priority order for DCR tonight:
1. CF-01 (double frontmatter) -- compiler bug, easy fix
2. CF-02 (--hydrate missing) -- needs dist rebuild
3. CF-03 (description cap) -- needs schema change
4. SF-SCOUT-07 (SKILL.md template as sprint-0 prereq) -- gates accurate feasibility
5. SF-SCOUT-13 (positioning fallback) -- highest impact on skill quality
6. SF-SCOUT-15 (requirements search path) -- affects all 8 scout skills
7. SF-SCOUT-16 (binding equivalence testing) -- pre-sprint blocker
