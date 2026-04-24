Written to `simulations/quest/golden/topic-echo-variate-R17-2026-03-16.md`.

---

## Variations: `topic:echo` -- Round 17

**Rubric:** v17 | **Max:** 320 | **5 essential / 3 recommended / 46 aspirational**

---

### Design Context

R16 V-05 scores 305/305 under v16. R17 does not re-implement R16's axes -- it **tightens** each axis against the v17 formal pass conditions and adds a named gate token per criterion, making each pass condition token-visible.

| Variation | Axis | New Gate Token(s) | C-52 | C-53 | C-54 | v17 |
|-----------|------|-------------------|:----:|:----:|:----:|:---:|
| V-01 | A only | `MANIFEST-COMPLETE` (per-type counts) | PASS | FAIL | FAIL | 310 |
| V-02 | B only | `CONSUMER-INDEX-COMPLETE` (all 3 tables) | FAIL | PASS | FAIL | 310 |
| V-03 | C only | `CHAIN-GROUNDING-COMPLETE` (both conditions) | FAIL | FAIL | PASS | 310 |
| V-04 | A+B | both tokens | PASS | PASS | FAIL | 315 |
| **V-05** | **A+B+C** | **all three tokens** | **PASS** | **PASS** | **PASS** | **320** |

---

### What's new from R16 to R17

Each of the three new criteria gets a **named gate token** that makes the pass condition verifiable from the token alone:

- **C-52** — `MANIFEST-COMPLETE` token now requires per-type counts (`[N] TYPE-A RESOLVED, [N] TYPE-B RESOLVED, [N] TYPE-C RESOLVED`) and the phrase "all RESOLVED." A reviewer reading the token alone confirms exhaustive enumeration without reading the manifest body. R16 had the manifest; R17 formalizes what the closure token must say.

- **C-53** — `CONSUMER-INDEX-COMPLETE` token names all three declaring tables explicitly: BC-COVERAGE-RECORD Schema, Phase Transition Registry, AND STILL-LIVE FILTER. This makes the "all three simultaneously" requirement structurally visible — partial Consumer-Ref is detectable from the token's absence rather than from reading each table. R16 had the columns; R17 adds the cross-table gate.

- **C-54** — `CHAIN-GROUNDING-COMPLETE` token names both required conditions and confirms both. C-54's critical clause ("either alone fails") is now enforceable: without this token, a prompt satisfying only one condition silently passes. R16 had the Belief-Ref extension; R17 adds the both-conditions-required gate.

**V-05 closed architecture:** All three axes active. TYPE-C manifest entries carry the confirming artifact inline, so a reviewer entering at any citation point can traverse the full chain — consuming header → declaring table (Axis B) → manifest completeness (Axis A) → falsifying evidence (Axis C) — from table cells alone.
