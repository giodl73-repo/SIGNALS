# Named-Expert Reviewer Simulation

Designs reviewed through the lens of specific domain experts — compiler theorists, ML researchers, formal methods specialists, etc.

## What It Simulates

Named researchers — AI acts as specific experts (Aho, Lattner, Ullman, Liang, Solar-Lezama, etc.) reading the design through their specific lens.

## Scale

18 distinct reviewer perspectives. 100+ findings across all reviews.

## Evidence Files

### Review Protocol

| File | Purpose |
|------|---------|
| `craftworks\design\astro\reviews.md` | Review standards & protocol — OLE preamble, file naming, frontmatter, finding format |

### Named Expert Reviews

| File | Expert | Lens |
|------|--------|------|
| `craftworks\design\astro\final\review-aho.md` | Alfred V. Aho | Compiler fundamentals, formal language theory |
| `craftworks\design\astro\final\review-lattner.md` | Chris Lattner | Compiler architecture |
| `craftworks\design\astro\final\review-ullman.md` | Jeffrey Ullman | Algorithms, formal methods |
| `craftworks\design\astro\final\review-chase.md` | David Chase | Compiler optimization |
| `craftworks\design\astro\final\review-sethi.md` | Ravi Sethi | Theory |
| `craftworks\design\astro\final\review-lam.md` | Monica S. Lam | Static analysis |
| `craftworks\design\astro\final\review-khattab.md` | Omar Khattab | Prompt optimization, RAG |
| `craftworks\design\astro\final\review-liang.md` | Percy Liang | AI/ML systems |
| `craftworks\design\astro\final\review-solar-lezama.md` | Armando Solar-Lezama | Program synthesis |
| `craftworks\design\astro\final\review-berger.md` | Alexa M. Sharp | Testing |
| `craftworks\design\astro\final\review-polikarpova.md` | Nadia Polikarpova | Formal verification |
| `craftworks\design\astro\final\review-amin.md` | Ahmet Seniha Amin | Domain expertise |

### Lens-Based Reviews (discipline, not individual)

| File | Lens |
|------|------|
| `craftworks\design\astro\final\review-architecture.md` | Architecture (5-discipline board) |
| `craftworks\design\astro\final\review-code-quality.md` | Code quality |
| `craftworks\design\astro\final\review-documentation.md` | Documentation |
| `craftworks\design\astro\final\review-testing.md` | Testing |
| `craftworks\design\astro\final\review-process.md` | PM & process |
| `craftworks\design\astro\final\review-implementation.md` | Implementation |

## Finding Format

```markdown
### F-01: Description (SEVERITY) — [ ] RESOLVED

[Analysis from expert's perspective]

**One-line fix**: [concrete suggestion]
```

## Why Named Experts Work

"What would Lattner say?" produces sharper findings than "review this code" — the persona constrains the lens and makes the review specific to a domain.
