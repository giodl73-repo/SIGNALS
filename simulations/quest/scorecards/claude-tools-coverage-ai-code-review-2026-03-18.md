```
SIGNAL COVERAGE: ai-code-review
=========================================
Namespace     | Skills run | Artifacts | Last run   | Status
--------------|------------|-----------|------------|--------
discover      | 6          | 6         | 2026-03-19 | COVERED
specify       | 1          | 1         | 2026-03-18 | COVERED
validate      | 2          | 4         | 2026-03-19 | COVERED
simulate      | 1          | 2         | 2026-03-19 | COVERED
prove         | 0          | 0         | --         | EMPTY
listen        | 0          | 0         | --         | EMPTY
rhythm        | 1          | 2         | 2026-03-19 | COVERED
roles         | 1          | 1         | 2026-03-18 | COVERED
topic         | 0          | 0         | --         | EMPTY

Total: 6/9 namespaces covered | 12 skills run | 16 artifacts
```

```
COVERAGE GAPS:
  -> /prove ai-code-review         (evidence + benchmarks -- validate claims with data)
  -> /listen ai-code-review        (user signals -- observed behavior + feedback loops)
  -> /topic:status ai-code-review  (narrative synthesis -- what do all signals say together)
```

```
COMMITMENT READINESS

Essential for commit (must have):
  [x] discover (competition + feasibility scoped)
  [x] specify (spec written)
  [x] validate (design reviewed)

Readiness: 3/3 essential namespaces covered
```

The 3 essential namespaces are all covered. The gaps are in `prove`, `listen`, and `topic`:

- `prove` is the next highest-value -- the design and customers reviews likely surfaced claims (performance, accuracy thresholds) that need benchmark backing before shipping.
- `listen` surfaces whether anyone has asked for this in the wild (issues, forum posts, usage signals).
- `topic:status` synthesizes everything into a go/no-go narrative -- worth running once prove and listen are in.

---
QUALITY: 5
CLAUDE_COMPATIBLE: Y
NOTES: Clean scan -- 16 artifacts across 6 namespaces. Rhythm has 2 decide artifacts (03-18 and 03-19), validate has 2 design + 2 customers artifacts (revision pattern). All paths parsed correctly.
