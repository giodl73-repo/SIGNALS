Here is the complete updated rubric as Markdown:

---

# trace-request Rubric — v9 (2026-03-15)

**Scale:** 190 (Essential 60 + Recommended 30 + Aspirational 100)
**Golden threshold:** all 4 essential PASS AND composite >= 80

---

## Two new criteria from R9 excellence signals

| New criterion | R9 excellence signal | What is testable |
|---|---|---|
| **C-26** Scope-gap Rem# three-way cross-link | ES-1 (V-03/V-05): Gap?=Y row in Step 8a cites a dedicated Rem# in Step 11 with exact scope string as Parameters; when the boundary Seq# also appears in adversarial/error traces, the link Step 8a → Step 11 → Step 7/9 is fully traceable | Is every Gap?=Y row wired to a Rem#? Does the Rem# Parameters value contain the exact scope string? Is the three-way cross-link present at boundaries shared with adversarial/error traces? |
| **C-27** Vocabulary conformance gate | ES-2 (V-04/V-05): VT# identifiers assigned at Step 0; Step 3a per-term conformance table yields D-integer; D=0 gate required before Step 4; D > 0 triggers correction cycle | Are VT# identifiers present at Step 0? Is a per-term conformance table present? Is a D=0 gate summary confirmed before Step 4? Is D > 0 paired with a completed correction cycle? |

**Scale:** 180 → **190** (aspirational tier: 18 → 20 criteria, 90 → 100 pts). Golden threshold stays at >= 80.

---

## Key design decisions

**C-26 vs C-25:** C-25 tests that the scope enumeration table exists and Gap? is populated. C-26 tests that every Gap?=Y row is wired to a Rem# with the exact scope string, and that the link is traceable across all three structures when the boundary appears in traces. Table without cross-links = C-25 PASS + C-26 FAIL.

**C-27 vs C-02:** C-02 tests that a forward-binding vocabulary declaration is made. C-27 tests that the commitment is structurally verified via VT# identifiers and a D=0 conformance gate. Precise declaration without a per-term check = C-02 PASS + C-27 FAIL.

**New dependency edges:**
- C-26 depends on C-25 (scope enumeration table with Gap? column exists) and C-23 (Rem# entries exist in the Register and are linked from traces); both required
- C-27 depends on C-02 (Step-0 binding declared, source of VT# terms); required

**Signal not promoted — C-28 design surface:** ES-3 (V-05 only): the exact VT# scope string propagates coherently across Step 3 Auth Check, Step 8a Scope/Role Invoked, and Step 11 Permission Fix Parameters for the same Gap?=Y boundary. Requires both C-26 and C-27 to produce consistent multi-round evidence before a computable binary can be defined.
