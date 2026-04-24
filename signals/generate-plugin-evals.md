# Generate Plugin Evals

Auto-generate probe tests (L0 structural + L2 judge/eval) for craftworks plugins. Run this whenever a new plugin is added or an existing plugin's commands change.

## Input

- **Plugin** (optional): Specific plugin name (e.g., `craft`, `boost`). Defaults to all plugins in `plugins/`.
- **Tier** (optional): Which test tiers to generate (`l0`, `l2-eval`, `all`). Defaults to `all`.
- **Force** (optional): Overwrite existing test files. Defaults to false (skip existing).

## Actions to Perform

### 1. Discover Plugins

Scan `plugins/` for all plugin directories. For each, read `.claude-plugin/plugin.json` to get:
- `name` — plugin name (used as prefix, e.g., `craft`)
- `commands` — array of command file paths
- `version` — current version
- `description` — plugin description

Also check `../craftworks-plugins/panel/` for marketplace-only plugins (requires sibling checkout; skip if not present).

Build a plugin registry:
```
{plugin_name}: {
  path: "plugins/{name}" or "../craftworks-plugins/{name}",
  commands: [{path, name, user_invocable, description}],
  has_shared: bool,
  has_config: bool,
  has_templates: bool,
  has_tests: bool,
  existing_probe_tests: count
}
```

### 2. Analyze Each Command

For each command `.md` file in the plugin:
1. Read the frontmatter to extract:
   - `name` — command name (e.g., `boost:lint`)
   - `description` — what it does
   - `user-invocable` — whether users can invoke it directly
   - `allowed-tools` — what tools it uses
2. Classify the command:
   - **read-only**: Uses only Read, Glob, Grep (status, show, help, report)
   - **write**: Uses Write, Edit, Bash (setup, create, modify)
   - **analysis**: Uses Read + produces structured output (lint, stats, verify)

### 3. Check Existing Coverage

Read `context/probe/{plugin}-dev/tests/` to inventory existing tests:
- Count tests per tier (L0, L1, L2, L3)
- Check if any tests use `judge:` assertions
- Identify commands without any L2 test coverage
- Identify commands without any judge/eval test

### 4. Generate L0 Structural Tests

For each plugin missing L0 tests, generate `context/probe/{plugin}-dev/tests/l0/`:

**l0-manifest.probe.yaml** — Plugin manifest validation:
```yaml
name: Plugin manifest is valid
tier: L0
plugin: {plugin_name}

assertions:
  - file_exists: .claude-plugin/plugin.json
  - json_valid: .claude-plugin/plugin.json
  - json_match:
      path: .claude-plugin/plugin.json
      field: name
      equals: {plugin_name}
  - json_match:
      path: .claude-plugin/plugin.json
      field: commands
      min_length: {command_count}
```

**l0-commands-exist.probe.yaml** — All commands exist:
```yaml
name: All command files exist
tier: L0
plugin: {plugin_name}

assertions:
  # One file_exists per command from plugin.json
  - file_exists: commands/{cmd}.md
```

**l0-frontmatter-valid.probe.yaml** — Frontmatter validation:
```yaml
name: All commands have valid frontmatter
tier: L0
plugin: {plugin_name}

assertions:
  # One frontmatter_valid per command
  - frontmatter_valid: commands/{cmd}.md
```

**l0-commands-not-empty.probe.yaml** — No empty command files:
```yaml
name: All command files have content
tier: L0
plugin: {plugin_name}

assertions:
  - file_not_empty: commands/{cmd}.md
```

**l0-claudemd-exists.probe.yaml** — Documentation exists:
```yaml
name: Plugin documentation exists
tier: L0
plugin: {plugin_name}

assertions:
  - file_exists: CLAUDE.md
  - file_not_empty: CLAUDE.md
```

If the plugin has `shared/`, add **l0-shared-dir.probe.yaml**.
If the plugin has `config/`, add **l0-config-dir.probe.yaml**.

### 5. Generate L2 Judge/Eval Tests

For each **user-invocable** command that lacks a judge test, generate a test file in `context/probe/{plugin}-dev/tests/l2/`:

**For read-only commands** (help, status, show):
```yaml
# L2 eval — {plugin}:{command} output quality
name: "{plugin}:{command} output quality"
tier: L2
plugin: {plugin_name}
command: {command}
timeout: 60

assertions:
  - exit_code: 0
  - output_not_contains: "ERROR"
  - judge:
      rubric: output-quality
```

**For analysis commands** (verify, lint, stats, validate):
```yaml
# L2 eval — {plugin}:{command} output quality and adherence
name: "{plugin}:{command} analysis quality"
tier: L2
plugin: {plugin_name}
command: {command}
# NOTE: args not used — probe runner doesn't propagate args to command invocation
timeout: 60

assertions:
  - exit_code: 0
  - judge:
      rubric: output-quality
  - judge:
      rubric: instruction-adherence
```

**For error-path commands** (run with bad input to test error handling):
```yaml
# L2 eval — {plugin}:{command} error handling quality
name: "{plugin}:{command} error handling"
tier: L2
plugin: {plugin_name}
command: {command}
# NOTE: args not used — probe runner doesn't propagate args to command invocation
# Intended bad input documented in comment for future runner support
timeout: 60

assertions:
  - judge:
      rubric: error-handling
```

**For commands with complex output** (report, metrics, graph):
```yaml
# L2 eval — {plugin}:{command} output quality
name: "{plugin}:{command} report quality"
tier: L2
plugin: {plugin_name}
command: {command}
timeout: 90

assertions:
  - exit_code: 0
  - judge:
      rubric: output-quality
  - judge:
      criteria:
        - name: actionability
          prompt: "Does the output provide actionable insights the user can act on?"
          scale: [1, 5]
          pass_threshold: 3
          weight: 1.0
```

### 6. Generate Skill Quality Tests

For each command, generate a **static** L0 test that evaluates the skill definition itself:

```yaml
# L0 eval — {plugin}:{command} skill definition quality
name: "{plugin}:{command} skill definition well-formed"
tier: L0
plugin: {plugin_name}

assertions:
  - file_exists: commands/{command}.md
  - frontmatter_valid: commands/{command}.md
  - frontmatter_has:
      path: commands/{command}.md
      field: name
  - frontmatter_has:
      path: commands/{command}.md
      field: description
  - content_match:
      path: commands/{command}.md
      pattern: "^## "
```

### 7. Write Test Files

For each generated test:
1. Check if the file already exists in the target directory
2. If `--force` is not set and the file exists, skip it
3. Otherwise, write the `.probe.yaml` file
4. Report what was created vs skipped

### 8. Generate Summary Report

```
## Plugin Eval Generation Report
Date: {date}

### Plugins Scanned
| Plugin | Commands | User-Invocable | Existing Tests | New Tests |
|--------|----------|----------------|----------------|-----------|
{per plugin row}

### Tests Generated
| Plugin | L0 | L2 Eval | L2 Error | Total New |
|--------|----|---------|---------  |-----------|
{per plugin row}

### Coverage After Generation
| Plugin | L0 | L1 | L2 | L3 | Judge/Eval | Total |
|--------|----|----|----|----|------------|-------|
{per plugin row}

### Skipped (already exist)
{list of skipped files}

### Next Steps
- Run `/probe:run --tier L0` to verify structural tests pass
- Run `/probe:run --tier L2 --eval` to run judge evaluations
- Review any failing tests and adjust thresholds
```

## Verification

After generation:
- All new `.probe.yaml` files are valid YAML
- L0 tests reference files that exist in the plugin
- L2 eval tests reference valid rubrics from `plugins/probe/config/rubrics/`
- No duplicate test IDs within a plugin's test suite
- Existing tests were not overwritten (unless `--force`)
