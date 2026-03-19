# Signal — Binding Specification

**Date**: 2026-03-14
**Status**: Design

---

## The Core Principle

Skills are binding-agnostic. The methodology content of each skill (what it does,
how it works, what it produces) is defined once in `signal.program.yaml` as the
source of truth. How that skill gets packaged and invoked is a binding decision,
separate from the skill design.

Same skill body. Different invocation shapes. Different target audiences.

---

## Atomic Skill Model

Every skill is designed as an atomic, self-contained unit:

- **Self-contained**: the skill has everything it needs to run -- stock roles, lifecycle,
  artifact naming, output path. No dependency on other skills running first.
- **Single responsibility**: one skill does one thing. `prove-hypothesis` states a
  hypothesis. `prove-synthesize` merges findings. They do not call each other.
- **Binding-agnostic**: the skill does not know whether it is a standalone command,
  a subcommand, or part of a plugin namespace. The methodology is the same.

48 atomic skills across 9 namespaces. Each skill is a complete unit of work.

---

## Binding Variants

### B-01: Flat (Skills-in-Repo, Standalone)

**Invocation**: `/prove-hypothesis`, `/scout-competitors`, `/topic-story`
**Install**: Copy individual SKILL.md files to `.claude/skills/{name}/SKILL.md`
**Source**: `binding-flat.program.yaml` (48 commands, one per atomic skill)
**Generated**: 48 SKILL.md files, one CLAUDE.md listing all skills

```
.claude/
  skills/
    prove-hypothesis/SKILL.md    -> /prove-hypothesis
    prove-websearch/SKILL.md     -> /prove-websearch
    prove-synthesize/SKILL.md    -> /prove-synthesize
    scout-competitors/SKILL.md   -> /scout-competitors
    scout-feasibility/SKILL.md   -> /scout-feasibility
    topic-new/SKILL.md           -> /topic-new
    topic-status/SKILL.md        -> /topic-status
    topic-story/SKILL.md         -> /topic-story
    ... (48 total)
```

**Constraints**:
- Names must be `[a-z][a-z0-9-]*` (no colon, no slash)
- Each skill is independently installable -- teams pick only what they need
- No namespace grouping -- all skills are peers in the listing
- Best for: teams that want selective adoption, power users who know what they want

**Audience**: Senior developers, architects, power users

---

### B-02: Grouped (Skills-in-Repo, Namespace Dispatcher)

**Invocation**: `/prove hypothesis`, `/scout competitors`, `/topic story`
**Install**: Copy 9 dispatcher SKILL.md files to `.claude/skills/{namespace}/SKILL.md`
**Source**: `binding-grouped.program.yaml` (9 commands + subcommands)
**Generated**: 9 dispatcher SKILL.md files + 48 atomic reference files

```
.claude/
  skills/
    prove/SKILL.md              -> /prove {subcommand}
    scout/SKILL.md              -> /scout {subcommand}
    topic/SKILL.md              -> /topic {subcommand}
    ... (9 total dispatchers)
  skills/prove/references/
    prove-hypothesis.md         -> loaded by /prove when subcommand=hypothesis
    prove-websearch.md
    prove-synthesize.md
    ... (T3 content, demand-paged)
```

**Constraints**:
- 9 install points instead of 48 -- lower friction
- Dispatcher reads the subcommand argument and loads the right T3 reference file
- Subcommand names are cleaner: `hypothesis` not `prove-hypothesis`
- T3 demand-paging: only the requested subcommand loads, not all 8 prove skills
- Best for: teams that want namespace organization, moderate users

**Audience**: Mixed teams, Dynamics developers familiar with namespace conventions

---

### B-03: Plugin (Namespaced, Plugin Format)

**Invocation**: `/signal:prove`, `/signal:scout`, `/signal:topic`
**Install**: Install the signal plugin via `.claude-plugin/manifest.json`
**Source**: `binding-plugin.program.yaml` (9 commands, plugin namespace prefix)
**Generated**: Plugin manifest + 9 SKILL.md files in plugin layout

```
.claude-plugin/
  manifest.json               -> plugin registration
  skills/
    prove/SKILL.md            -> /signal:prove
    scout/SKILL.md            -> /signal:scout
    topic/SKILL.md            -> /signal:topic
    ... (9 total)
```

**Constraints**:
- CommandNameID requires `{plugin}:{command}` format (Spec 46 regex)
- Colon syntax works in plugin manifests but not in filesystem paths on Windows
  -- emitter converts `signal:prove` to `prove/SKILL.md` under plugin layout
- All 9 namespaces always installed together -- no selective adoption
- Plugin updates via `signal.manifest.json` upgrade contract
- Best for: zero-setup all-hands rollout, consistent namespace across all repos

**Audience**: All-hands audience, teams that want zero config

---

### B-04: Cursor Rules

**Invocation**: Cursor IDE context / agent mode
**Install**: `.cursor/rules/signal-{namespace}.mdc` per namespace
**Source**: `binding-cursor.program.yaml` (cross-compiled from flat via Spec 105)
**Generated**: 9 `.mdc` rule files, one per namespace

**Constraints**: Per Spec 105 (Cursor Rules Workspace Conformance) and the
Cross-Format Translation Loss Matrix (Spec 108). Slash-command invocation is not
native to Cursor -- rules activate by context, not by explicit invocation.

**Status**: Planned (v0.3 release)

---

### B-05: Cline/Roo

**Invocation**: Mode-based activation in Cline/Roo Code
**Install**: `.roo/rules/rules-{mode}.md` per mode
**Source**: Cross-compiled from flat via Spec 107
**Generated**: Mode files mapping Signal namespaces to Roo modes

**Status**: Planned (v0.4 release)

---

### B-06: CREST

**Invocation**: TBD -- new format defined in Spec 109 (craftworks-make)
**Install**: `CREST.md` or expanded C/R/E/S/T files
**Source**: `signal.crest.md` -- Signal workspace authored in CREST format
**Generated**: Same binding outputs as program.yaml but from CREST input
**Purpose**: Validates CREST as an alternative input to program.yaml for the
same generation pipeline. Signal is the test case.

**Status**: Experimental (concurrent with v0.1)

---

## Source of Truth Architecture

```
signal.program.yaml          <- atomic skill definitions (content)
        |
        +-- binding-flat.program.yaml      -> B-01 output: 48 standalone skills
        +-- binding-grouped.program.yaml   -> B-02 output: 9 namespace dispatchers
        +-- binding-plugin.program.yaml    -> B-03 output: plugin with manifest
        +-- binding-cursor.program.yaml    -> B-04 output: Cursor rules
        +-- binding-cline.program.yaml     -> B-05 output: Roo/Cline modes

signal.crest.md              <- CREST format alternative input
        |
        +-- same outputs as above (validates CREST parity with program.yaml)

signal.manifest.json         <- upgrade contract (binding-agnostic)
```

The skill bodies are defined once in `signal.program.yaml`. Each binding variant
is a separate program.yaml that references the same content with different
packaging configuration. When a skill body changes, all binding variants regenerate.

---

## Release Strategy

| Release | Bindings | Audience | Key milestone |
|---------|----------|----------|---------------|
| v0.1 | B-01 (flat) | Senior devs, power users | 48 atomic skills working |
| v0.2 | B-02 (grouped) + B-03 (plugin) | All-hands | Zero-setup install + namespace UX |
| v0.3 | B-04 (Cursor) | Cursor users | Cross-platform parity |
| v0.4 | B-05 (Cline/Roo) | Cline/Roo users | Full cross-platform |
| v0.5 | B-06 (CREST) | craftworks validation | CREST input parity |

---

## Naming Conventions Per Binding

| Binding | Skill name format | Example |
|---------|------------------|---------|
| B-01 flat | `{namespace}-{skill}` | `prove-hypothesis` |
| B-02 grouped | dispatcher: `{namespace}`, subcommand: `{skill}` | `prove` + `hypothesis` |
| B-03 plugin | `{plugin}:{namespace}` | `signal:prove` |
| B-04 Cursor | `{namespace}-{skill}` (rule name) | `signal-prove-hypothesis` |
| B-05 Cline | mode name | `signal-prove` |

The atomic skill identity is always `{namespace}-{skill}`. Bindings wrap this identity
in whatever invocation shape the target platform requires.

---

## What This Means for Skill Authoring

When writing a skill body in `signal.program.yaml`, write for the atomic identity:
- The skill does one thing
- It does not assume a namespace prefix in its instructions
- It references other skills by their atomic identity (`prove-hypothesis`,
  `prove-synthesize`) not by their binding invocation (`/prove hypothesis`)
- Stock roles are embedded -- the skill is self-contained regardless of binding

The binding layer handles invocation. The skill layer handles methodology.
