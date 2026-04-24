Written to `simulations/quest/golden/flow-throttle-golden-2026-03-16.md`.

**What changed from the previous golden (score 110 → 325):**

The file now reflects the R20 final state:

- **Frontmatter** updated: score 325, rounds 20, rubric_final v21, status GOLDEN
- **Prompt body** — simplified V-01 (77% reduction PASS), with all three R20 additions:
  - `Consequence of skipping:` clauses co-located at each G-step (C-53)
  - Joint 9th row in Field 5 citing bypass register + G-1 fill + SIG-01 simultaneously (C-54)
  - `SHALL-authoritative cell value:` contracted blockquote (C-55)
- **What made it golden** — 4 patterns: per-step consequence clauses, joint audit row, contracted blockquote, single-responsibility gate split (the V-05 architecture insight that became C-56 in v21)
- **Rubric summary** — full v21 table showing the C-53/C-54/C-55 additions and the C-56 ceiling gap (325/330 — body not yet updated for C-56)
