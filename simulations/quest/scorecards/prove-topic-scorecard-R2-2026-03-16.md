```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Exit-signal chaining ('SCOUT READY cannot fire without found file' + 'STAGE N cannot begin until SCOUT READY fires') satisfies C-10 as a two-step structural block without GATE block headers", "Two-write synthesis makes C-09 structural by construction -- Write A enumerates per-claim confidence adjustments by artifact definition, not by closing instruction", "Role-sequence framing (SCOUT-LOADER -> ANALYST -> SYNTHESIZER) satisfies C-02 and C-07 by architecture -- the role that owns scout loading inherently precedes hypothesis formation"]}
```

---

**Round 2 results** — rubric v14 ceiling hit.

| Var | Axis | Score | C-10 |
|-----|------|-------|------|
| V-01 | Minimalism | 97.5 | PARTIAL |
| V-02 | Exit-signal framing | 100 | PASS |
| V-03 | Role sequence | 100 | PASS |
| V-04 | Two-write synthesis | 100 | PASS |
| V-05 | Combined | 100 | PASS |

**Only discriminating criterion**: C-10 (structural block). V-01's minimalist prose uses "stop and emit... Do not proceed" — a functional abort, but without a formal signal chain or role mechanism. All other variations provide a two-layer block (signal + entry condition, or role halt + ENTRY check, or halt with no fallback) that satisfies the rubric's structural block examples.

**Three new patterns saved**: exit-signal chain for C-10, two-write synthesis for C-09 by construction, role-sequence for C-02/C-07 by architecture.

**Next**: V-05 (Combined) is the golden candidate. V-01 is one two-signal line away from 100. Consider new aspirational criteria before Round 3 to restore discrimination signal.
