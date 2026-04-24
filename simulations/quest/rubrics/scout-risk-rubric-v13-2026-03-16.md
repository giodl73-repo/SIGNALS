**scout-risk-rubric-v13-2026-03-17.md** — written.

Four new criteria extracted from the R13 scorecard:

| ID | Pattern Source | Escalates | Core Insight |
|----|---------------|-----------|--------------|
| **C-38** | V-02/V-04/V-05 Phase 1b completion gate | C-36 | Seed step is an assertion without an equality gate; "dimension count = HIGH row count" converts it to a verified postcondition |
| **C-39** | V-02/V-04/V-05 Phase 2 header | C-36 | Expansion step must name seed output as starting state and restrict additions to MEDIUM/LOW — otherwise Phase 2 can silently replace the seed |
| **C-40** | V-02/V-05 Phase 2b exclusion clause | C-25 | When an upstream phase guarantees a property, the downstream audit must explicitly exclude that property from repair scope — confirm, don't re-derive |
| **C-41** | V-05 Phase 0b forward-reference | C-37 | Schema block should enumerate its consumers (forward pointer), not just be referenced by them (backward pointer) — gaps visible from both directions |

**Scoring delta:**
- Aspirational criteria: 29 → 33 (+4)
- Aspirational max: 58 → 66 pts (+8)
- Max composite: 148 → **156**
- Golden band: 142–148 → **150–156**
- Strong band: 127–141 → **135–149**
