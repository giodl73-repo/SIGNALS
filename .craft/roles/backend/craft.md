---
name: craft
version: "1.0"
archetype: craft

orientation:
  frame: "Sees craft-cli backend as domain modules with pure functions, Store persistence, and worker-based AI execution."
  serves: "Developers implementing new domain logic who need clear patterns for data persistence, AI task delegation, error handling, and input validation."

lens:
  verify:
    - "Are domain functions pure -- deterministic outputs for given inputs, no side effects beyond Store calls?"
    - "Is file-based persistence routed through Store classes, never raw fs.readFile/writeFile?"
    - "Do worker contracts define JSON input/output schemas with Zod validation?"
    - "Are errors propagated as typed CraftError instances with meaningful codes and messages?"
    - "Is Zod validation applied at every external boundary (CLI args, file reads, AI responses)?"
    - "Are domain modules testable in isolation without mocking the filesystem?"
  simplify:
    - "Use Store classes for all persisted state -- they handle path resolution, serialization, and atomic writes"
    - "Use executeWorker() for AI tasks -- it manages prompt construction, provider calls, and response parsing"
    - "Apply Zod parse at input boundaries, then trust TypeScript types internally"
    - "Return typed result objects from domain functions -- never rely on thrown errors for control flow"
    - "Use CraftError with structured error codes, not raw Error or string throws"

expertise:
  depth: "TypeScript domain modeling, file-based Store persistence, worker pattern for AI delegation, Zod validation boundaries, CraftError hierarchy, pure function design"
  relevance: "Domain modules are the core of craft-cli. Impure domains or leaky persistence boundaries make the system untestable and fragile to refactoring."

scope: workspace
collaborates_with:
  - backend
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-backend-craft-{subject}.md"
workflow:
  - step: assess
    description: "Evaluate domain module purity, Store usage patterns, and boundary validation"
  - step: review
    description: "Check worker contracts, error propagation paths, and Zod schema coverage"
  - step: produce
    description: "Generate review with domain design findings, Store pattern compliance, and validation gaps"
---

# Craft Backend

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required -- the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for the backend role working on the craft-cli codebase -- domain modules are the engine. They must be pure, typed, and independently testable. Every side effect (file I/O, AI calls, git operations) passes through a defined seam.

---

## Domain Module Pattern

Each domain module in domains/ follows a consistent structure:

```
domains/{name}/
  index.ts       -- public API (re-exports)
  {name}.ts      -- core business logic (pure functions)
  {name}.store.ts -- Store class for persistence
  types.ts       -- domain-specific types (if not in schemas/)
```

**Rules**:
- Domain functions accept typed parameters and return typed results.
- No direct filesystem access -- use Store or core/files utilities.
- No terminal output -- return data, let handlers format it.
- No process.exit -- throw CraftError, let commands handle exit codes.

## Store Pattern

Store classes manage file-based persistence under .craft/:

```typescript
class WaveStore {
  constructor(private projectRoot: string) {}
  async load(waveId: string): Promise<Wave> { /* ... */ }
  async save(wave: Wave): Promise<void> { /* ... */ }
  async list(): Promise<WaveSummary[]> { /* ... */ }
}
```

**Conventions**:
- Store owns path resolution (callers pass IDs, not paths).
- Store handles YAML/JSON serialization internally.
- Store validates data with Zod on read (untrusted filesystem).
- Store writes atomically (write temp, rename) when possible.

## Worker Architecture

AI tasks use the worker pattern to isolate prompt construction from domain logic:

- Handler calls `executeWorker(workerName, input)`.
- Worker constructs prompt from typed input, calls AiProvider.
- Worker parses AI response, validates with Zod, returns typed output.
- Domain logic never touches prompts or AI responses directly.

## AI Provider Contract

The AiProvider interface abstracts LLM interactions:

```typescript
interface AiProvider {
  complete(prompt: string, options?: CompletionOptions): Promise<string>;
  stream(prompt: string, options?: StreamOptions): AsyncIterable<string>;
}
```

Handlers select the provider; workers consume it. Domain logic has no knowledge of AI providers.
