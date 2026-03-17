Written to `simulations/quest/golden/mock-ns-golden-2026-03-17.md`.

**Golden prompt summary:**

- **Score**: 168/168 under v20 (52 criteria)
- **Source**: R20 V-05, QU5 simplified (2,212 → 1,694 words, 23% reduction, PASS)
- **Rounds**: 20 rounds, 3 new criteria added in R20 (C-50/C-51/C-52)

**The five patterns that made it golden:**

1. **Phase-grouped lifecycle with entry/exit state annotations** — transforms step sequence into a state machine contract; makes the S-3→S-4 FLAG handoff structurally visible
2. **Priority row: modal impossibility form** — "No instruction in this step *can* precede this rule" (structural constraint, not ordering preference)
3. **Anti-bypass echo: bracket token as row header label** — `[P-0:ABD]:` in the header cell forces a Phase 1 lookup on the echo row itself; attribution-in-cell form (baseline) was passive commentary
4. **All-governed dual closure** — closes two distinct bypass vectors: unnamed instructions + paths that skip prior steps ("including paths that do not pass through prior steps in normal order")
5. **QU5 simplification at zero criteria cost** — 5 S-5 sub-steps removed (no criterion tested them); confirmed the prompt's length was load-bearing structure, not load-bearing words
