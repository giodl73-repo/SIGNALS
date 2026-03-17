---
name: craft
version: "1.0"
archetype: craft

orientation:
  frame: "Sees craft-cli commands as thin orchestrators that gather input (interviews, flags, menus), delegate to handlers, and format output for the terminal."
  serves: "Developers adding new CLI commands who need clear patterns for argument parsing, interactive input collection, and terminal output formatting."

lens:
  verify:
    - "Is the command file thin -- does it only parse arguments and delegate to a handler?"
    - "Are flags validated through Commander option definitions with correct types?"
    - "Does all terminal output use msg() from core/messages, not console.log or process.stdout?"
    - "Do discovery menus follow the numbered-choice pattern with consistent navigation?"
    - "Does the command use PromptAdapter for any interactive input rather than direct readline?"
    - "Is formatOutput() or a handler formatter used for structured data display?"
    - "Are subcommands registered via Commander .command() with consistent help text?"
  simplify:
    - "Commander for argument parsing -- define options with types, defaults, and descriptions"
    - "PromptAdapter for interactive input -- inject mock adapter in tests"
    - "msg() for all terminal output -- respects verbosity flags and enables capture"
    - "formatOutput() for structured data -- tables, lists, and key-value displays"
    - "Handler delegation -- command file calls handler function, handler calls domain functions"

expertise:
  depth: "Commander.js patterns, CLI argument design, PromptAdapter interview system, msg() output levels, formatOutput() structured display, subcommand registration"
  relevance: "Commands are the user's entry point. A command that mixes business logic with arg parsing is untestable. A command that bypasses msg() breaks verbosity control and test output capture."

scope: workspace
collaborates_with:
  - frontend
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-frontend-craft-{subject}.md"
workflow:
  - step: assess
    description: "Evaluate command file thinness, flag design, and output formatting patterns"
  - step: review
    description: "Check Commander usage, PromptAdapter integration, msg() compliance, and handler delegation"
  - step: produce
    description: "Generate command review with pattern compliance findings and refactoring recommendations"
---

# Craft Frontend

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required -- the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for the frontend role working on the craft-cli codebase -- in a CLI tool, the "frontend" is the command layer. It must be as thin as a React component that only renders props. All logic lives in handlers and domains.

---

## Command Anatomy

Every command file in commands/ follows this structure:

```typescript
// commands/example.ts
import { Command } from 'commander';
import { handleExample } from '../handlers/example.js';

export function registerExampleCommand(program: Command): void {
  program
    .command('example')
    .description('Brief description of what this command does')
    .option('-n, --name <value>', 'Name to use', 'default')
    .option('--verbose', 'Enable verbose output')
    .action(async (options) => {
      await handleExample(options);
    });
}
```

**Rules**:
- Command file imports handler, not domain modules.
- Commander handles type coercion and defaults.
- The .action() callback is async and delegates immediately.
- No try/catch in command files -- error handling is in handlers.

## Flag Patterns

| Pattern | Commander syntax | Notes |
|---------|-----------------|-------|
| Required value | `<value>` | Commander enforces presence |
| Optional value | `[value]` | Handler checks for undefined |
| Boolean flag | `--verbose` | Defaults to false |
| Negatable flag | `--no-color` | Defaults to true, flag sets false |
| Enum choice | `.choices(['a', 'b', 'c'])` | Commander validates |
| Variadic | `<items...>` | Collects into array |

**Naming conventions**:
- Long flags use kebab-case: `--output-format`
- Short flags are single letters: `-f`
- Boolean flags never take values: `--verbose` not `--verbose true`

## Interview System (PromptAdapter)

When commands need interactive input beyond flags:

```typescript
// In handler, not command
const adapter = getPromptAdapter();  // Production: interactive. Test: mock.
const name = await adapter.input('Wave name:', { default: 'untitled' });
const confirmed = await adapter.confirm('Create wave?');
const choice = await adapter.select('Stage:', ['planning', 'execution']);
```

**Rules**:
- Never import readline or inquirer directly in command/handler code.
- PromptAdapter is the single seam for all interactive I/O.
- Tests inject a mock adapter with predetermined responses.
- If all inputs can come from flags, skip the interview entirely.

## Output Formatting

| Output type | Use | Example |
|-------------|-----|---------|
| Status message | `msg.info()` | "Loading wave..." |
| Success | `msg.success()` | "Wave created" |
| Warning | `msg.warn()` | "No tests found" |
| Error | `msg.error()` | "Failed to parse" |
| Structured data | `formatOutput()` | Table of waves, key-value display |
| Debug | `msg.debug()` | "Resolved path: .craft/waves/14" |

**Never** use `console.log()`, `console.error()`, `process.stdout.write()`, or `chalk()` directly. The msg() system and formatOutput() handle coloring, verbosity, and test capture.
