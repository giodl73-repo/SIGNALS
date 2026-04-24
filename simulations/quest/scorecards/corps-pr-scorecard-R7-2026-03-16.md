## corps-pr — Round 7 Scorecard

### Scoring Reference

| Band | Count | Per-criterion | Total |
|------|-------|--------------|-------|
| Essential (C-01–C-05) | 5 | 12.000 | 60 |
| Recommended (C-06–C-08) | 3 | 10.000 | 30 |
| Aspirational (C-09–C-24) | 16 | 0.625 | 10 |
| **Max** | | | **100** |

PASS = full pts · PARTIAL = half pts · FAIL = 0

---

### Baseline Assumptions

All R7 variations build on R6-best (R6 V-05 equivalent): C-01–C-20 are PASS (97.5 pts), and R6 introduced C-21–C-24 at base level. The R7 base carries:

| Criterion | R6 base level | Rationale |
|-----------|--------------|-----------|
| C-21 | **PARTIAL** | Net column + derived verdict exist, but verdict names rows in prose — "verdict derived from row directions" is inferrable, not string-matchable |
| C-22 | **PARTIAL** | Dual-clause C1/C2 declared in pipeline; no output result lines — failures require reading the declaration to detect, not visible as output gaps |
| C-23 | **PARTIAL** | Receipt structure present with all required fields; "initial position" field may be post-hoc rationalization — pre-commitment timing not enforced |
| C-24 | **PASS** | Domain-Lens column in technical role findings fully satisfies pass condition from R6 V-03 |

R6 base total: 97.5 + (0.3125 × 3) + 0.625 = **99.0625**

---

### Variation Scorecards

#### V-01 — Inertia Framing (C-21 axis)

| ID | Band | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | Routing table with exact org.yaml scope patterns — unchanged from R6 |
| C-02 | Essential | PASS | Binary domain-lens gate + rewrite consequence — unchanged |
| C-03 | Essential | PASS | Divergence field + Mechanism line in consensus — unchanged |
| C-04 | Essential | PASS | GO / NO-GO / GO WITH CONDITIONS — unchanged |
| C-05 | Essential | PASS | Binary test + rewrite consequence, not naming contract — unchanged |
| C-06 | Rec. | PASS | Coverage gap notice for unmatched files — unchanged |
| C-07 | Rec. | PASS | Per-role finding summary with severity breakdown — unchanged |
| C-08 | Rec. | PASS | AMEND mode scope disclosure — unchanged |
| C-09 | Asp. | PASS | Root cause synthesis for divergent findings — unchanged |
| C-10 | Asp. | PASS | GO WITH CONDITIONS names owner role — unchanged |
| C-11 | Asp. | PASS | IA sequenced first as reference object — unchanged |
| C-12 | Asp. | PASS | Architectural mechanism named in divergence explanations — unchanged |
| C-13 | Asp. | PASS | Enumerated ban list ≥ 3 prohibited perspective-label phrases — unchanged |
| C-14 | Asp. | PASS | Per-role IA anchor in at least one finding per section — unchanged |
| C-15 | Asp. | PASS | Explicit rewrite gate (binary test + drop consequence) — unchanged |
| C-16 | Asp. | PASS | AMEND structured output block with named fields — unchanged |
| C-17 | Asp. | PASS | IA cost framing in cost terms — unchanged |
| C-18 | Asp. | PASS | Named phase-gate pipeline with entry/exit conditions — unchanged |
| C-19 | Asp. | PASS | Named-row × named-column ledger + Budget verdict + Budget strength — unchanged |
| C-20 | Asp. | PASS | Phase C entry condition declares IA phase completion + read prerequisite — unchanged |
| **C-21** | Asp. | **PASS** | 3-clause formula (`WORSE rows:` / `BETTER rows:` / `Conclusion:`) — string-matchable; verdict is a derivable consequence of named row directions |
| C-22 | Asp. | **PARTIAL** | Dual-clause C1/C2 carried from R6; no output result lines (C1 RESULT / C2 RESULT) — failure in execution requires reading the pipeline declaration, not reading the output |
| C-23 | Asp. | **PARTIAL** | Receipt structure carried from R6; pre-commitment timing not enforced — "initial position" may be rationalized after re-reading the PR diff |
| C-24 | Asp. | PASS | Domain-Lens column in technical role findings carried from R6 |

**Subtotal — R7 criteria:** C-21 0.625 + C-22 0.3125 + C-23 0.3125 + C-24 0.625 = **1.875**
**V-01 Total: 99.0625 − 1.875 (R6 base R7 partial) + 1.875 = 99.375 → 99.4**

Wait — recomputing cleanly:
- C-01–C-20 PASS: 97.500
- C-21 PASS: 0.625
- C-22 PARTIAL: 0.313
- C-23 PARTIAL: 0.313
- C-24 PASS: 0.625
- **V-01: 99.4**

---

#### V-02 — Lifecycle Emphasis (C-22 axis)

| ID | Band | Verdict | Evidence |
|----|------|---------|----------|
| C-01–C-20 | — | PASS (all) | R6 base unchanged |
| C-21 | Asp. | **PARTIAL** | Net column + derived verdict carried from R6; no 3-clause formula — verdict names rows in prose, not as labeled-line fields checkable by string match |
| **C-22** | Asp. | **PASS** | C1 produces `C1 RESULT: ALL CLEAR / BLOCKED`; C2 per-role produces `C2 RESULT: SATISFIED / UNSATISFIED` — both failure modes are visible output gaps, not silent pipeline violations |
| C-23 | Asp. | **PARTIAL** | Receipt structure carried from R6; C2 RESULT enforces that the receipt citation exists (satisfying C2), but does not enforce timing — initial position could still be written after the PR diff is re-read |
| C-24 | Asp. | PASS | Domain-Lens column carried from R6 |

- C-01–C-20: 97.500
- C-21 PARTIAL: 0.313
- C-22 PASS: 0.625
- C-23 PARTIAL: 0.313
- C-24 PASS: 0.625
- **V-02: 99.4**

---

#### V-03 — Role Sequence (C-23 axis)

| ID | Band | Verdict | Evidence |
|----|------|---------|----------|
| C-01–C-20 | — | PASS (all) | R6 base unchanged |
| C-21 | Asp. | **PARTIAL** | Net column + derived verdict from R6; no 3-clause formula — verdict row citations are prose-embedded, not labeled line fields |
| C-22 | Asp. | **PARTIAL** | Dual-clause carried from R6; no C1 RESULT / C2 RESULT output lines — failure detection still requires reading the pipeline declaration |
| **C-23** | Asp. | **PASS** | Pre-commitment receipt: written before PR diff is re-read for findings. Required `CONFIRMED / REVISED` delta field with named code artifact closes rationalization gap — initial position is now an auditable artifact with verifiable before/after record |
| C-24 | Asp. | PASS | Domain-Lens column carried from R6 (V-03 built this axis in R6) |

- C-01–C-20: 97.500
- C-21 PARTIAL: 0.313
- C-22 PARTIAL: 0.313
- C-23 PASS: 0.625
- C-24 PASS: 0.625
- **V-03: 99.4**

---

#### V-04 — Inertia Framing + Lifecycle Chain (C-21 + C-22)

| ID | Band | Verdict | Evidence |
|----|------|---------|----------|
| C-01–C-20 | — | PASS (all) | R6 base unchanged |
| **C-21** | Asp. | **PASS** | 3-clause formula present + Phase B exit checklist item B3 explicitly verifies "3-clause structure present" — C-21 compliance is gated at Phase B exit, not just asserted |
| **C-22** | Asp. | **PASS** | C2 compliance block cites the verdict's `WORSE rows:` / `BETTER rows:` labeled lines specifically, not just a raw ledger row — proves both that Phase B was read AND that the 3-clause derivation structure was recognized; creates a verifiable chain from Phase B output to Phase C entry |
| C-23 | Asp. | **PARTIAL** | Receipt structure carried from R6; not in scope for this variation — pre-commitment timing not enforced, CONFIRMED/REVISED delta absent |
| C-24 | Asp. | PASS | Domain-Lens column carried from R6 |

- C-01–C-20: 97.500
- C-21 PASS: 0.625
- C-22 PASS: 0.625
- C-23 PARTIAL: 0.313
- C-24 PASS: 0.625
- **V-04: 99.7**

---

#### V-05 — All Four R7 Axes

| ID | Band | Verdict | Evidence |
|----|------|---------|----------|
| C-01–C-20 | — | PASS (all) | R6 base unchanged |
| **C-21** | Asp. | **PASS** | 3-clause formula (`WORSE rows:` / `BETTER rows:` / `Conclusion:`) — fully string-matchable; Budget verdict is a named derivation from row evidence |
| **C-22** | Asp. | **PASS** | C1 RESULT + C2 RESULT output blocks; C2 cites verdict's labeled row lists — failures are visible output gaps auditable per phase and per role |
| **C-23** | Asp. | **PASS** | Pre-commitment receipt (written before PR diff re-read) with required `CONFIRMED / REVISED` delta + named code artifact — initial position is a timestamped pre-commitment artifact, not a rationalized post-hoc claim |
| **C-24** | Asp. | **PASS** | Universal table schema: IA findings section uses `IA-gate` column; all technical role findings sections use `Domain-Lens` column — format compliance auditable by a single named-column check regardless of section |

- C-01–C-20: 97.500
- C-21 PASS: 0.625
- C-22 PASS: 0.625
- C-23 PASS: 0.625
- C-24 PASS: 0.625
- **V-05: 100.0**

---

### Ranking

| Rank | Variation | Score | All Essential Pass | Delta vs. Base |
|------|-----------|-------|--------------------|----------------|
| 1 | **V-05** — All Four R7 Axes | **100.0** | Yes | +0.9375 |
| 2 | **V-04** — C-21 + C-22 Chain | **99.7** | Yes | +0.6250 |
| 3 (tie) | **V-01** — C-21 (Inertia) | **99.4** | Yes | +0.3125 |
| 3 (tie) | **V-02** — C-22 (Lifecycle) | **99.4** | Yes | +0.3125 |
| 3 (tie) | **V-03** — C-23 (Role Sequence) | **99.4** | Yes | +0.3125 |

---

### Excellence Signals — V-05

**1. Universal column schema closes format divergence across sections**
All findings sections — IA and technical roles alike — share the same named-column format: `IA-gate` for the Inertia Advocate, `Domain-Lens` for every technical role. A single column-check protocol verifies format compliance regardless of which section is being reviewed. Prior variations used Domain-Lens only in technical role findings, leaving the IA section on a different structural footing.

**2. Chain verifiability: each mechanism's output is the next mechanism's input**
3-clause verdict (C-21) → C2 compliance cites the verdict's labeled row lists (C-22) → pre-commitment receipt restates Budget verdict + Budget strength before findings (C-23) → Domain-Lens column makes gate compliance observable per finding (C-24). Each phase's output is a named field that the next phase reads explicitly. A compliance check at any point in the chain can trace backward to the originating named field.

**3. Pre-commitment delta record eliminates the rationalization gap**
The `CONFIRMED / REVISED` delta in the READ RECEIPT — anchored to a named code artifact — separates what the role believed before re-reading the PR diff from what it concluded after. Prior variations included the receipt fields (Budget verdict, cost row, initial position) but allowed them to be written after findings were drafted. The timing constraint makes "initial position" verifiable: if the delta shows CONFIRMED, it must match the pre-commitment claim; if REVISED, the code artifact explains why. This is not enforced by any earlier variation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["universal-column-schema: IA findings and technical-role findings use the same named-column protocol (IA-gate / Domain-Lens), making format compliance auditable by a single column-check across all sections regardless of role", "chain-verifiability: each R7 mechanism's output is a named field consumed as input by the next — 3-clause verdict cited in C2 compliance, restated in READ RECEIPT, exposed per-finding in Domain-Lens column; compliance traces backward to originating fields without re-running the gate", "pre-commitment-delta-record: READ RECEIPT written before PR diff re-read with required CONFIRMED/REVISED outcome field and named code artifact — initial position is an auditable pre-commitment artifact, not a post-hoc claim; the delta closes the rationalization gap that R6 left open"]}
```
