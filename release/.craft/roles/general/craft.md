---
name: craft
version: "1.0"
archetype: craft

orientation:
  frame: "Sees the craft-cli codebase as a unified system where consistent patterns (layering, schemas, stores, testing) matter more than any individual feature."
  serves: "All developers contributing to craft-cli who need one place to find naming conventions, import patterns, error handling rules, and cross-platform requirements."

lens:
  verify:
    - "Are files named in kebab-case with camelCase exports (e.g., wave-store.ts exports waveStore)?"
    - "Do all ESM imports include the .js extension (TypeScript ESM requirement)?"
    - "Are user-facing errors thrown as CraftError subclasses with structured error codes?"
    - "Is path construction using node:path (path.join, path.resolve) rather than string concatenation?"
    - "Are platform-specific operations guarded or abstracted (no hardcoded /dev/null, no chmod)?"
    - "Does new code follow the existing pattern in its layer (check neighboring files for conventions)?"
    - "Are Zod schemas in schemas/ rather than defined inline in handlers or domains?"
  simplify:
    - "Follow existing patterns -- check 2-3 neighboring files before writing new code"
    - "ESM imports require .js extensions: import { foo } from './foo.js' (even for .ts source files)"
    - "CraftError for user-facing errors -- includes error code, message, and optional cause"
    - "Platform-agnostic paths via node:path -- never construct paths with string concatenation or hardcoded separators"
    - "Zod schemas at boundaries -- parse external input, trust types internally"

expertise:
  depth: "TypeScript ESM conventions, kebab-case file naming, CraftError hierarchy, cross-platform path handling, Zod boundary validation, vitest testing patterns"
  relevance: "Inconsistency is the most expensive kind of technical debt in a CLI tool. Every deviation from established patterns requires a mental context switch and increases the chance of bugs."

scope: workspace
collaborates_with:
  - general
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-general-craft-{subject}.md"
workflow:
  - step: assess
    description: "Evaluate new code against established codebase conventions and patterns"
  - step: review
    description: "Check naming, imports, error handling, path construction, and cross-platform compliance"
  - step: produce
    description: "Generate consistency review with pattern deviations and standardization recommendations"
---

# Craft General

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required -- the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for the general role working on the craft-cli codebase -- consistency is the craft-cli superpower. When every module follows the same patterns, new code writes itself by imitation. When patterns diverge, every change requires archaeology.

---

## Codebase Conventions

### File Naming
- Source files: `kebab-case.ts` (e.g., `wave-store.ts`, `run-orchestration.ts`)
- Test files: `kebab-case.test.ts` (co-located or in `__tests__/`)
- Schema files: `kebab-case.schema.ts` (e.g., `wave.schema.ts`)
- Index files: `index.ts` for public API re-exports

### Export Naming
- Functions: `camelCase` (e.g., `loadWave`, `formatOutput`)
- Classes: `PascalCase` (e.g., `WaveStore`, `CraftError`)
- Types/interfaces: `PascalCase` (e.g., `Wave`, `RuntimeContext`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `CRAFT_FEATURES`, `DEFAULT_STAGES`)
- Zod schemas: `camelCase` suffixed with `Schema` (e.g., `waveSchema`, `configSchema`)

## Import Patterns

```typescript
// Node built-ins: use node: prefix
import { readFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';

// External packages: bare specifier
import { z } from 'zod';
import { Command } from 'commander';

// Internal: relative path with .js extension (ESM requirement)
import { WaveStore } from '../domains/wave/wave-store.js';
import { msg } from '../core/messages.js';
import { waveSchema } from '../schemas/wave.schema.js';
```

**Critical**: The `.js` extension is required for all relative imports in TypeScript ESM. The TypeScript compiler does not rewrite extensions. Omitting `.js` causes runtime module resolution failures.

## Error Handling

```typescript
// Domain/handler code: throw CraftError
import { CraftError } from '../core/errors.js';

throw new CraftError('WAVE_NOT_FOUND', `Wave ${id} does not exist`, { cause: err });

// Command layer: catches CraftError, maps to exit code
// Never catch and swallow errors silently -- always log or rethrow
```

**Error code convention**: `UPPER_SNAKE_CASE` describing the failure domain and condition (e.g., `WAVE_NOT_FOUND`, `SCHEMA_VALIDATION_FAILED`, `STORE_WRITE_ERROR`).

## Cross-Platform Rules

craft-cli runs on Windows, macOS, and Linux. These rules are non-negotiable:

| Do | Do not |
|----|--------|
| `path.join(dir, 'file.txt')` | `dir + '/file.txt'` |
| `path.resolve(base, relative)` | Template literal paths with `/` |
| Check `process.platform` for platform-specific behavior | Assume Unix |
| Use `node:fs/promises` for file operations | Shell out to `cat`, `cp`, `rm` |
| Use `node:child_process` with `shell: true` for shell commands | Assume bash is available |
| Normalize line endings when comparing text | Assume `\n` everywhere |

**Path separators**: Always use `node:path` functions. Never hardcode `/` or `\\` in path construction. Tests that construct paths with `/` will fail on Windows if not using path.join().
