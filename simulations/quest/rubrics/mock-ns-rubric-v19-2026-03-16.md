The file is written. Here is the complete v19 rubric as Markdown output:

---

## Summary of changes

**Two new aspirational criteria (C-48, C-49) extracted from R19 excellence signals. Max rises from 158 to 162.**

### C-48 -- Phase-grouped lifecycle organization in S-0 (R19 V-03 Axis C)

R19 V-03 canonical: Axis C -- phase-grouped lifecycle + state annotations -- achieves 158/158 under v18. The lifecycle section organizes step boundaries into discrete named execution phases (e.g., "Entry gate", "Execution", "Exit confirmation") with each phase grouping the relevant step references under that label.

C-48 names the phase-grouped form as the golden lifecycle organization pattern and tests for its presence when lifecycle annotations are included. When a lifecycle section is present in S-0, it must use phase grouping rather than a flat enumeration of lifecycle events or step boundaries. A flat lifecycle list -- step events or boundaries listed without enclosing phase-group labels -- fails C-48. C-48 passes by default when no lifecycle annotations are present in S-0 (lifecycle annotation is optional; its absence does not affect this criterion). Distinct from C-43: C-43 tests whether lifecycle annotation REPLACES the tier-carry terminal sentence (interaction with C-32); C-48 tests the organizational structure of the lifecycle section itself (phase grouping vs. flat). They are orthogonal -- a flat lifecycle that also replaces the terminal sentence fails both C-43 and C-48; a flat lifecycle that follows the terminal sentence (supplementation) fails C-48 only; a phase-grouped lifecycle that follows the terminal sentence passes both. Failure chain for flat lifecycle with supplementation: C-48 alone (-2 pts). R19 V-03 canonical.

### C-49 -- Per-step state annotations within lifecycle phase structure (R19 V-03 Axis C)

R19 V-03 canonical: within each named lifecycle phase, individual step references carry explicit state annotations -- entry state and exit state (or equivalent current-state -> next-state transition notation) -- rather than bare step identifiers.

C-49 names the per-step state annotation as the golden depth requirement within phase-grouped lifecycle structure. When a phase-grouped lifecycle section is present in S-0 (C-48 passing by content), each step boundary reference within the phases must carry explicit state-transition annotations naming the entry and exit states. Bare step references within phases -- without named state variables -- fail C-49. C-49 passes by default when: (a) no lifecycle annotations are present in S-0, or (b) lifecycle annotations are present but flat (C-48 failing). C-49 fires specifically when a phase-grouped structure (C-48 passing by content) references step boundaries without per-step state-transition annotations. Distinct from C-48: C-48 tests phase-group organizational label presence; C-49 tests annotation depth within those phases. A phase-grouped lifecycle with bare step references satisfies C-48 but fails C-49. Failure chain for phase-grouped lifecycle without state annotations: C-49 alone (-2 pts). R19 V-03 canonical.

### C-43 discriminator note updated

R19 V-03 confirms: phase-grouped lifecycle with per-step state annotations is a supplementation form. The tier-carry terminal sentence remains present as a discrete prose sentence; the phase-grouped lifecycle section follows it. C-43 passes. The Axis C form is the richest supplementation form observed; C-48 and C-49 capture quality criteria within the lifecycle section itself.

### Discriminator notes updated

| Criterion | Update |
|-----------|--------|
| C-43 | R19: Phase-grouped lifecycle with per-step state annotations (V-03 Axis C) confirmed as supplementation form -- tier-carry terminal sentence remains present as discrete prose, C-43 passes. C-48 and C-49 capture quality criteria within the lifecycle section independently of C-43's scope. |
| C-48 | New. Phase-grouped lifecycle organization in S-0. R19 V-03 Axis C canonical. |
| C-49 | New. Per-step state annotations within lifecycle phases. R19 V-03 Axis C canonical. |

### Scoring

| Version | Aspirational max | Total max |
|---------|-----------------|-----------|
| v18 | 78 (39 x 2) | 158 |
| **v19** | **82 (41 x 2)** | **162** |

**R19 under v19:**
- V-01 (deontic closing sentence): fails C-31; no Axis C lifecycle (C-48, C-49 default pass) -- **156/162**
- V-02 (4-row collapsed FLAG table): fails C-22; no Axis C lifecycle (C-48, C-49 default pass) -- **156/162**
- V-03 (phase-grouped lifecycle + state annotations): all 49 criteria pass -- **162/162**
- V-04 (deontic + collapsed FLAG): fails C-31, C-22; no Axis C lifecycle (C-48, C-49 default pass) -- **154/162**
- V-05 (declarative + 5-row + phase-grouped golden): all 49 criteria pass -- **162/162**

---

The rest of the rubric (essential, recommended, aspirational C-09 through C-47, and the full version history) carries over unchanged from v18, with two additions:

**C-43** gains the R19 discriminator note: *"Phase-grouped lifecycle with per-step state annotations (R19 V-03 Axis C) is a supplementation form -- the tier-carry terminal sentence remains present as discrete prose, C-43 passes. C-48 and C-49 capture additional quality criteria within the lifecycle section itself, independently of C-43's replacement/supplementation scope."*

**C-48 and C-49** are appended as the 40th and 41st aspirational criteria.

---

**Written to**: `simulations/quest/rubrics/mock-ns-rubric-v19-2026-03-17.md` (534 lines)  
**v18 restored**: unchanged at 505 lines

**Key design decisions:**

1. **C-48 and C-49 both pass by default** when no lifecycle section is present -- consistent with C-43's treatment of non-lifecycle contexts. V-01/V-02/V-04 (no Axis C) lose nothing.

2. **C-49 conditional on C-48 by content** -- C-49 only fires inside a phase-grouped structure. A flat lifecycle (C-48 failing) leaves C-49 in default-pass state, avoiding a spurious double-fire.

3. **C-43 orthogonality preserved** -- The five lifecycle form × scoring table in C-48's pass condition maps all combinations of C-43/C-48/C-49 cleanly: flat-replacement = -6 pts (C-32, C-43, C-48); flat-supplementation = -2 pts (C-48 only); phase-no-annotations = -2 pts (C-49 only); phase-with-annotations = 0 pts.
