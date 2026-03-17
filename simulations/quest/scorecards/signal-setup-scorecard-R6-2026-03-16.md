## signal-setup — Round 6 Scoring

**Rubric**: v6 (C-01–C-20) | **Date**: 2026-03-16 | **Variations**: V-01–V-05

---

### Shared Baseline Assessment (C-01–C-18)

All five variations carry forward the V-05 R4 baseline intact. These criteria are evaluated once and applied uniformly.

| ID | Category | Status | Evidence |
|----|----------|--------|---------|
| C-01 | correctness | PASS | GATE 0 reads CLAUDE.md and branches on presence before any write |
| C-02 | behavior | PASS | GATE 3 displays the full preview block before GATE 4 confirmation |
| C-03 | behavior | PASS | GATE 4 requires explicit `[y/N]` before writing |
| C-04 | correctness | PASS | Signal section includes skills reference, `/decide`, `/signal`, inertia rule |
| C-05 | correctness | PASS | GATE 2 detects existing Signal section and halts with status message |
| C-06 | coverage | PASS | "The one rule: the primary competitor is always inertia..." present in appended section |
| C-07 | coverage | PASS | GATE 6 checks for `.github/copilot-instructions.md` and offers update |
| C-08 | format | PASS | GATE 2, GATE 5, GATE 7 each output distinct status with what was done and where |
| C-09 | correctness | PASS | GATE 3 preview block is exactly the content written at GATE 5; no divergence |
| C-10 | behavior | PASS | GATE 1 handles missing CLAUDE.md as a named edge-case gate with its own path |
| C-11 | structure | PASS | GATE 0–7 are numbered, labeled, and sequenced; no phase can be skipped |
| C-12 | structure | PASS | GATE 1 (missing file) and GATE 2 (already configured) are first-class gates with full treatment |
| C-13 | structure | PASS | "Teams skip Signal not because they reject it — because there is always a reason to configure later..." preamble leads |
| C-14 | behavior | PASS | GATE 4 decline: "Inertia remains unnamed... no reminder to ask 'why would teams do nothing?'..." names the absence |
| C-15 | behavior | PASS | GATE 2 (all variations) affirms positive consequence: "Inertia already has a named opponent..." |
| C-16 | structure | PASS | Preamble frames inertia as the thing that "wins every build where it is not named" — adversary framing |
| C-17 | structure | PASS | "gives Claude a persistent reminder... before every feature, every session. Configure once." — permanence argument present |
| C-18 | behavior | PASS | GATE 4 decline: "before the next build" — future-moment anchor confirmed |

---

### Per-Variation Assessment

**C-19 criterion interpretation**: The rubric explicitly names GATE 1 and GATE 4 as the "equivalent exits" — both are "no Signal configured" exits. GATE 6 is a secondary optional path that runs *after* Signal IS configured; declining GATE 6 does not leave Signal unconfigured. Therefore C-19's narrow reading applies: GATE 1 and GATE 4 both need the future-moment anchor.

---

#### V-01 — Axis A: GATE 1 anchor added

| ID | Status | Evidence |
|----|--------|---------|
| C-01..C-18 | PASS | Baseline preserved |
| C-19 | **PASS** | GATE 1 decline: "no reminder to ask 'why would teams do nothing?' **before you write the first line**" — anchor present. GATE 4: "before the next build" — anchor present. Both primary Signal-absent exits covered. |
| C-20 | **FAIL** | GATE 2: "your CLAUDE.md carries the reminder" — consequence affirmed (C-15 satisfied) but auto-load mechanism not named. No mention of automatic session loading. |

**Aspirational passing**: 11/12 (C-09–C-18 + C-19)
**Composite**: (5/5 × 60) + (3/3 × 30) + (11/12 × 10) = 60 + 30 + 9.17 = **99.2**
**Golden**: YES (all essentials pass, composite ≥ 80)

---

#### V-02 — Axis B: GATE 2 mechanism named

| ID | Status | Evidence |
|----|--------|---------|
| C-01..C-18 | PASS | Baseline preserved |
| C-19 | **FAIL** | GATE 1 decline: "Inertia has no named opponent in this workspace. Run /signal-setup when you are ready to add it." — no future-moment anchor. Only GATE 4 carries "before the next build." Asymmetric. |
| C-20 | **PASS** | GATE 2: "every session that opens this workspace **loads CLAUDE.md automatically**, so the inertia question is present from the first message, without you having to remember to invoke it." — mechanism explicitly named. |

**Aspirational passing**: 11/12 (C-09–C-18 + C-20)
**Composite**: (5/5 × 60) + (3/3 × 30) + (11/12 × 10) = 60 + 30 + 9.17 = **99.2**
**Golden**: YES

---

#### V-03 — Axis C: GATE 6 anchor added

| ID | Status | Evidence |
|----|--------|---------|
| C-01..C-18 | PASS | Baseline preserved |
| C-19 | **FAIL** | GATE 1 decline unchanged: no future-moment anchor. GATE 6 now has "before the next Copilot session reaches for a build suggestion" but GATE 6 is a post-Signal optional step — not an equivalent Signal-absent exit. The GATE 1 gap is the failing condition for C-19 regardless of GATE 6 treatment. |
| C-20 | **FAIL** | GATE 2 unchanged: no auto-load mechanism named. |

**Aspirational passing**: 10/12 (C-09–C-18)
**Composite**: (5/5 × 60) + (3/3 × 30) + (10/12 × 10) = 60 + 30 + 8.33 = **98.3**
**Golden**: YES (essentials pass, composite ≥ 80)

> **C-19 boundary note**: V-03 fails C-19 even under the broadest reading because GATE 1 — unambiguously a Signal-absent exit — still lacks the anchor. Fixing GATE 6 alone cannot satisfy "no decline path weaker than any other" when GATE 1 remains unanchored.

---

#### V-04 — Axes A+B: GATE 1 anchor + GATE 2 mechanism

| ID | Status | Evidence |
|----|--------|---------|
| C-01..C-18 | PASS | Baseline preserved |
| C-19 | **PASS** | GATE 1: "no reminder to ask 'why would teams do nothing?' before you write the first line" — anchor present. GATE 4: "before the next build" — anchor present. Both primary exits covered. |
| C-20 | **PASS** | GATE 2: "every session that opens this workspace loads CLAUDE.md automatically, so the inertia question is present from the first message, without you having to remember to invoke it." — mechanism named. |

**Aspirational passing**: 12/12
**Composite**: (5/5 × 60) + (3/3 × 30) + (12/12 × 10) = 60 + 30 + 10 = **100.0**
**Golden**: YES

---

#### V-05 — Axes A+B+C: All exits — GATE 1 anchor + GATE 2 mechanism + GATE 6 anchor

| ID | Status | Evidence |
|----|--------|---------|
| C-01..C-18 | PASS | Baseline preserved |
| C-19 | **PASS** | GATE 1: "before you write the first line." GATE 4: "before the next build." GATE 6: "before the next Copilot session reaches for a build suggestion." All exit paths carry distinct future-moment anchors; no path weaker than any other. |
| C-20 | **PASS** | GATE 2: identical auto-load mechanism phrasing as V-04 — "every session... loads CLAUDE.md automatically." |

**Aspirational passing**: 12/12
**Composite**: (5/5 × 60) + (3/3 × 30) + (12/12 × 10) = 60 + 30 + 10 = **100.0**
**Golden**: YES

> **V-05 vs V-04 distinction**: Both score 100. V-05 adds a GATE 6 Copilot anchor that doesn't score under the current rubric, but makes the design semantically complete — three exits, three distinct contextually-calibrated future moments.

---

### Rankings

| Rank | Variation | Score | Golden | Notes |
|------|-----------|-------|--------|-------|
| 1 (tie) | V-04 | 100.0 | YES | Minimum-change path to 100 |
| 1 (tie) | V-05 | 100.0 | YES | Semantically complete; holds under broad C-19 reading |
| 3 (tie) | V-01 | 99.2 | YES | C-19 only |
| 3 (tie) | V-02 | 99.2 | YES | C-20 only |
| 5 | V-03 | 98.3 | YES | Neither C-19 nor C-20; GATE 6 fix is post-Signal, not equivalent exit |

---

### Excellence Signals from V-04/V-05

**E-1: Temporal anchors are contextually calibrated, not duplicated**
V-05 does not copy "before the next build" to GATE 1. Instead it selects a moment that matches the specific context of that exit: GATE 1 (no CLAUDE.md at all) gets "before you write the first line" — the actual threshold moment for an unconfigured workspace. GATE 4 (CLAUDE.md exists, Signal absent) keeps "before the next build." Each anchor names the right moment for the user standing at that particular gate.

**E-2: The positive path explains mechanism, not merely consequence**
V-04/V-05's GATE 2 shift — from "your CLAUDE.md carries the reminder" to "every session loads CLAUDE.md automatically" — converts a reassurance into a model. The user doesn't just know Signal is doing something good; they understand *why* it continues working without them. This closes the gap between affirming value (C-15) and earning trust in the configuration's permanence (C-20).

**E-3: Secondary optional exits receive equal rhetorical architecture** (V-05 only)
By extending the future-moment pattern to GATE 6, V-05 establishes that no exit — even one for an optional secondary target — delivers a weaker consequence argument. This isn't scored by C-19 under the current rubric, but it makes the design robust against future rubric expansion and eliminates the asymmetry where Signal's absence from Copilot context is treated as lesser than its absence from Claude context.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Temporal anchors are contextually calibrated to each exit gate's specific moment — not duplicated from the primary gate", "Secondary optional exit gates receive equal future-moment architecture as primary Signal-absent exits"]}
```
