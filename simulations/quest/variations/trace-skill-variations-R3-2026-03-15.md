Written to `simulations/quest/golden/trace-skill-variate-R3-v3-2026-03-15.md`.

---

# trace-skill — Variations R3 / rubric-v3

**Entry state**: R2 V-05 covers C-01–C-13. Rubric v3 adds four aspirationals from R2 excellence signals. R3 targets all four.

**New criteria being targeted:**

| ID | What it requires | R2 V-05 state |
|----|-----------------|---------------|
| C-14 | Phase Label Schema table (immutable preamble) before trace | PASS (inherited V-01 design) |
| C-15 | Verdict is compliance ledger table (ID \| Result \| Evidence) | PARTIAL (table exists; no Evidence column) |
| C-16 | Bind three-value Status enum formally declared | PARTIAL (RESOLVED/UNRESOLVED implicit; BLOCKED in prose gate) |
| C-17 | Bind conflict precedence rule declared before rows | PASS in V-02/V-05 (inline prose; not a named block) |

---

## Variation axes chosen

**Single-axis:**
- **V-01** — Lifecycle emphasis → **C-14**: Phase Label Schema as formal immutable preamble block; phase headers transcribed, not generated
- **V-02** — Output format → **C-15 + C-16**: Verdict rewritten as compliance ledger with structural Evidence column; Bind opens with a formal Status Enum definition table
- **V-03** — Role sequence → **C-11 + C-17**: spec-first two-tier Gather; Bind opens with a named Conflict Precedence Rule block before row 1

**Combined:**
- **V-04** — Phase Schema + Status Enum + Conflict Precedence (**C-14 + C-16 + C-17**): three pre-content declarations in sequence — schema locks headers, enum locks Bind vocabulary, precedence rule locks conflict resolution
- **V-05** — Full golden (**C-09–C-17**): carries R2 V-05 foundation (Coverage Matrix, relay carry, spec-first Gather, delimiter markers) and adds all four new v3 criteria in structural order

---

## Hypotheses summary

| Variation | Primary target | Key structural bet |
|-----------|---------------|-------------------|
| V-01 | C-14 | Schema-before-trace makes C-06 a transcription, not a convention |
| V-02 | C-15, C-16 | Evidence column forces structural reference; BLOCKED as enum member > prose gate |
| V-03 | C-11, C-17 | Tier separation prevents invocation-anchored Gather; named rule block before rows |
| V-04 | C-14, C-16, C-17 | "Declare before you use" rhythm is compositional — three declarations reinforce each other |
| V-05 | All C-09–C-17 | Each criterion targets an independent structural layer; no overlap; compliance ledger is the final check |

**Risk note on V-05**: nine aspirationals add length. The compliance ledger Verdict is the backstop — missing rows are structurally visible even if a model skips a middle layer.
