File written to `simulations/quest/rubrics/trace-request-rubric-v15-variate-R17-2026-03-15.md`.

---

## Round 17 — 5 Variations (Rubric v15, C-39 target)

### Variation Design Table

| V | Axis | Type | C-39 Mechanism | C-40 Probe |
|---|------|------|----------------|------------|
| **V-01** | Lifecycle: Phase 0 TRACE CONTRACT gate | Single | `GATE-0` phase token forces HALT-EXPECTED-BOUNDARY + HALT-EXPECTED-CONDITION before Step 0; validation closure tied to Phase 3 exit gate | Does Phase 0 also migrate CHECKER ALGORITHM before Step 1 (Tier C)? |
| **V-02** | Phrasing register: DECLARE CONTRADICTION token in Step 8b | Single | TRACE CONTRACT carried from baseline; DECLARE CONTRADICTION: token explicitly required in Step 8b prose before Step 8c table row | C-40 Tier B: does `DECLARE CONTRADICTION:` appear at Step 8b prose surface, not Step 8c? |
| **V-03** | Output format: pre-filled TRACE CONTRACT template | Single | TRACE CONTRACT pre-printed as fill-in template with canonical HALT-EXPECTED-CONDITION form shown; validation stub left as `___` until after Step 8c | Does template transcription produce correct dual-surface HALT-EXPECTED-CONDITION without authorship discretion? |
| **V-04** | Role sequence + pre-trace CHECKER ALGORITHM | Combined | Algorithm-Declarant role (Phase 0B) emits CHECKER ALGORITHM before Step 0; HALT-RULE references HALT-EXPECTED-BOUNDARY by name; Platform Expert reproduces verbatim at Step 8 | C-40 Tier C: does pre-trace HALT-RULE encode HALT-EXPECTED-BOUNDARY as a named token in the halt predicate? |
| **V-05** | Formal register + DECLARE CONTRADICTION + TRACE CONTRACT | Combined | Three-axis: formal register throughout + DECLARE CONTRADICTION in Step 8b (with `matches HALT-EXPECTED-BOUNDARY: yes/no` cross-reference) + TRACE CONTRACT pre-declaration | C-40 Tier B: does intertextual reference (DECLARE CONTRADICTION naming HALT-EXPECTED-BOUNDARY) produce stable Step 8b prose-token surface? |

### Key structural differences from R16

**V-01** — Converts the TRACE CONTRACT from an inline block into a named Phase 0 lifecycle event with its own `GATE-0` closure condition, establishing it as a first-class phase parallel to GATE-3/GATE-8H/GATE-8B/GATE-8C.

**V-02** — Carries the TRACE CONTRACT baseline from R16 V-03 but adds the C-40 Tier B probe: `DECLARE CONTRADICTION: BC-N -- [label] -- [arm]` required in Step 8b prose before the Step 8c table row for that boundary is populated.

**V-03** — Pre-prints the TRACE CONTRACT as a mandatory fill-in template with labeled `BC-__` slots and the canonical HALT-EXPECTED-CONDITION form shown verbatim, converting C-39 from authorship to transcription.

**V-04** — Introduces a two-role sequence: Algorithm-Declarant (Phase 0: emits TRACE CONTRACT + CHECKER ALGORITHM with HALT-RULE referencing `HALT-EXPECTED-BOUNDARY` by name) then Platform Expert (Steps 0–12, reproduces CHECKER ALGORITHM verbatim at Step 8 Header). Tests C-40 Tier C: whether pre-trace HALT-RULE references the predicted boundary as a named token in the algorithm itself.

**V-05** — Formal declarative register throughout + DECLARE CONTRADICTION in Step 8b with an explicit cross-reference flag (`matches HALT-EXPECTED-BOUNDARY: yes/no`) + TRACE CONTRACT. Tests whether the intertextual reference makes the contradiction event machine-detectable across both the Step 8b prose surface and the TRACE CONTRACT boundary prediction simultaneously.

### Excellence signal target for R18

Whether `DECLARE CONTRADICTION:` (V-02, V-05) appears stably in **Step 8b** prose surface — not Step 8c — across different variation axes, producing the multi-round evidence needed to freeze the C-40 Tier B testable surface. And whether pre-trace `HALT-RULE` (V-04) encoding `HALT-EXPECTED-BOUNDARY` by name constitutes a qualitatively distinct criterion from C-38's generic dual-surface predicate.
