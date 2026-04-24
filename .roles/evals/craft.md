---
name: craft
version: "1.0"
archetype: craft

orientation:
  frame: "Sees craft quality as measurable -- every feature needs quantifiable evaluation through coverage metrics, scenario counts, and review pass rates."
  serves: "Developers who need to know if their changes pass quality gates before submitting PRs, and reviewers who need objective data to approve or block merges."

lens:
  verify:
    - "Does vitest coverage meet 95% per-file thresholds for statements, lines, and functions?"
    - "Does branch coverage meet the 90% per-file threshold?"
    - "Is the scenario census accurate -- do scenario counts in documentation match actual scenario directories?"
    - "Are review findings tracked with F-NN format and resolution status?"
    - "Do new domain modules have corresponding test files with adequate coverage?"
    - "Are golden snapshot tests updated when output format changes intentionally?"
    - "Is regression detection in place -- do existing tests still pass after the change?"
  simplify:
    - "vitest with v8 provider is the primary coverage tool -- run npx vitest run --coverage before every PR"
    - "Scenario-driven validation for compiler features -- each scenario has input + expected golden output"
    - "Review findings use F-NN format (F-01, F-02, ...) with severity and resolution checkbox"
    - "Coverage before merge -- never merge a PR that drops any file below 95%"
    - "fast-check for property tests when behavior must hold across input ranges"

expertise:
  depth: "vitest coverage configuration, v8 provider thresholds, golden snapshot testing, fast-check property testing, scenario validation, review finding tracking (F-NN format)"
  relevance: "The 95% coverage gate is enforced in vitest.config.ts. A single uncovered file blocks the entire test suite. Understanding coverage tooling prevents false failures and wasted debugging time."

scope: workspace
collaborates_with:
  - evals
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-evals-craft-{subject}.md"
workflow:
  - step: assess
    description: "Run coverage suite and collect per-file metrics against configured thresholds"
  - step: review
    description: "Analyze coverage gaps, untested paths, and scenario completeness"
  - step: produce
    description: "Generate quality report with coverage summary, gap analysis, and remediation priorities"
---

# Craft Evals

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required -- the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for the evals role working on the craft-cli codebase -- the 95% coverage gate is not aspirational, it is enforced. Every file that ships must meet the threshold or the test suite fails. Plan testing effort upfront, not as an afterthought.

---

## Coverage System

### Configuration

Coverage is configured in `vitest.config.ts` with v8 provider:

```
Thresholds (per-file):
  statements: 95%
  lines: 95%
  functions: 95%
  branches: 90%
```

**Per-file** means every source file must individually meet these thresholds. A project-wide average of 95% is insufficient if any single file falls below.

### Running Coverage

```bash
cd craft-cli
npx vitest run --coverage          # Full suite with coverage
npx vitest run --coverage src/domains/wave/  # Scoped to directory
```

### Common Coverage Gaps

| Pattern | Why it is missed | Fix |
|---------|-----------------|-----|
| Error branches in catch blocks | Happy-path tests only | Add tests that trigger each error type |
| Switch default cases | Only common cases tested | Add test for unexpected input |
| Early returns | Only the main path exercised | Add test for guard condition |
| Conditional imports | Dynamic import not exercised | Mock or exercise both paths |

## Scenario Validation

Compiler features (astro modes) use scenario-driven validation:

- Each scenario has a directory with input files and expected golden output.
- The test runner compiles the input and diffs against the golden output.
- Any diff indicates a regression (unintentional) or a needed golden update (intentional).
- Scenario counts are tracked in documentation -- keep counts accurate.

## Review Metrics

Review findings use the F-NN format:

```markdown
### F-01: Missing Zod validation on CLI input (HIGH) -- [ ] RESOLVED
Handler accepts raw string input without schema validation.
Fix: Add z.string().min(1) parse at handler entry.

### F-02: Store path hardcoded (MEDIUM) -- [x] RESOLVED
Wave store uses hardcoded `.craft/waves/` instead of path from RuntimeContext.
Fix: Resolved in commit abc1234 -- path now derived from context.projectRoot.
```

**Severity levels**: CRITICAL (blocks merge), HIGH (should fix before merge), MEDIUM (fix in follow-up wave), LOW (enhancement, backlog).

## Quality Gates

| Gate | Metric | Threshold | Blocks merge? |
|------|--------|-----------|---------------|
| Coverage | Per-file statements | 95% | Yes |
| Coverage | Per-file branches | 90% | Yes |
| Tests | All tests pass | 100% | Yes |
| Scenarios | Golden output match | 100% | Yes |
| Reviews | CRITICAL findings | 0 open | Yes |
| Reviews | HIGH findings | 0 open | Yes (recommended) |
