Now I have all five variations. Let me score each against the v18 rubric.

---

## topic:plan — Round 18 Scoring (Rubric v18)

### Rubric Framework
- 55 criteria total: 5 essential / 3 recommended / 47 aspirational (C-09–C-55)
- C-43–C-55 (13 criteria) require Skill Execution Contract format: Phase −1, Gate-0, §ID blocks, numbered pass/halt annotations — **none of the R18 variations implement this structure**
- C-54 and C-55 (new in v18) require typed arithmetic decomposition and attestation N cross-reference in pass-threshold annotation — **structurally absent from all variations**
- Scoring ceiling for variations in Steps 1–8 format: max ≈ 42/55 (8 essential+rec + 34 aspirational C-09–C-42)

---

### Essential Criteria (C-01–C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy.md, cite structure | PASS | PASS | PASS | PASS | PASS |
| C-02 9 namespaces with filenames+dates | PASS | PASS | PASS | PASS | PASS |
| C-03 NEW/PRIOR split, strategy date named | PASS | PASS | PASS | PASS | PASS |
| C-04 Typed proposals ADD/REMOVE/REPRIORITIZE | PASS | PASS | PASS | PASS | PASS |
| C-05 Confirmation gate, visible YES/NO/REVISED halt | PASS | PASS | PASS | PASS | PASS |

**All essential PASS — all variations qualify.**

---

### Recommended Criteria (C-06–C-08) — need 2/3

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Evidence artifact filename per proposal | PASS | PASS | PASS | PASS | PASS |
| C-07 Before/After diff structure | PASS | PASS | PASS | PASS | PASS |
| C-08 Per-row NO CHANGE inertia justification | PASS | PASS | PASS | PASS | PASS |

**All recommended PASS — 3/3 for all variations.**

---

### Aspirational Criteria Assessment

#### C-09–C-42: Baseline structural criteria (34 total)

**Features common to all variations — baseline PASS set (~21 criteria):**
- Column Contract block present with Rules 1–4 (enumerated values, independence test, null text, two-hop delta format)
- Pre-signal Defense Register (pre-registered keep-arguments + invalidation conditions)
- Anti-pattern checkpoint (inventory ≠ delta)
- SIGNAL READ-LOCK after inventory table
- Delta findings table with Delta-candidate column and null text
- Proposals table: full 11-column set including Confidence, If unchanged, Reversibility, Delta Finding
- Schema-commitment checkpoints before proposals and diff
- "Will not substitute prose for any table" declaration
- Defender Challenge Table with Defense basis column
- Calibration check present
- Conflict audit table with all columns
- Diff table with evidence brackets and proposal cross-references
- Inertia declared as co-equal option (not fallback)

**Features that vary across variations:**

**G-23: Pre-printed slot architecture ("select exactly one" at decision sites)**
- V-01: FAIL — uses conditional text, not slot format
- V-02: PASS — slots at schema commitment, all null sites, calibration, confirmation gate, diff schema checkpoint
- V-03: FAIL — uses conditional text format
- V-04: PARTIAL — calibration check uses slot; other sites do not
- V-05: PASS — full slot architecture at all decision sites

**H: Inertia recurrence pattern (pre-role placement + downstream coverage)**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Inertia declared before role line | PASS | PASS | PASS | PASS (schema→inertia→role) | PASS |
| Inertia at Step 4 (proposals) | PASS (INERTIA-GATE block) | PASS | PASS | PASS ("Recall") | PASS (INERTIA-GATE block) |
| Inertia at Step 4b (Defender) | PASS (INERTIA-GATE block) | FAIL — not present | FAIL | PASS ("Recall") | PASS (INERTIA-GATE block) |
| Inertia at Step 7 (confirmation gate) | PASS (INERTIA-GATE block) | FAIL — slot format but no inertia framing | FAIL | PASS ("Recall: NO is valid") | PASS (INERTIA-GATE block) |

V-01 and V-05 achieve full inertia coverage at all 3 downstream sites.
V-04 achieves full downstream coverage via "Recall" sentences.
V-02 and V-03 drop inertia at Steps 4b and 7.

**Degenerate register naming (REQUIRED vs DEGENERATE contract)**
- V-01: FAIL — no register contract
- V-02: FAIL — no register contract
- V-03: PASS — Narrative Format Contract + PASS/FAIL examples at Steps 3/3b/4/5/6 + PHASE 3 EXIT GATE
- V-04: FAIL — no register contract
- V-05: PASS — full register contract + FAIL examples + PHASE 3 EXIT GATE

**Schema-first sequence (output structure committed before role identity)**
- V-04: PASS — schema commitment block appears before inertia framing before role line; artifacts numbered 1–7
- V-05: PASS — schema slot before role
- Others: PARTIAL — schema committed upfront but after role line

**Step existence rationale preambles ("This step exists so that...")**
- V-05 only: PASS — each step carries a rationale block making the step's analytical purpose explicit
- All others: FAIL

#### C-09–C-42 Summary Scores

| Feature group | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------------|------|------|------|------|------|
| Baseline (21 criteria) | 21 | 21 | 21 | 21 | 21 |
| G-23 slot architecture | 0 | 1 | 0 | 0.5 | 1 |
| H inertia coverage (4 criteria) | 4 | 2 | 2 | 4 | 4 |
| Degenerate register | 0 | 0 | 1 | 0 | 1 |
| Schema-first | 0 | 0 | 0 | 1 | 0.5 |
| Step rationale preambles | 0 | 0 | 0 | 0 | 1 |
| Calibration format (partial coverage) | 0.5 | 0 | 0.5 | 0 | 0 |
| **C-09–C-42 subtotal** | **25.5** | **24** | **24.5** | **26.5** | **28.5** |

#### C-43–C-55: Advanced gate structure (13 criteria)

All require Skill Execution Contract format (Phase −1, Gate-0, §ID blocks, numbered pass/halt fields, arithmetic decomposition).

| Criterion | All Variations |
|-----------|---------------|
| C-43 Cell-exhaustive gate | FAIL — no §ID blocks |
| C-44 Numbered Gate-0 label | FAIL — no Gate-0 block |
| C-45 Schema-gate checklist atomicity | FAIL |
| C-46 Pass-threshold annotation | FAIL |
| C-47 Exhaustive item cross-reference | FAIL |
| C-48 Single-STOP halt declaration | FAIL |
| C-49 Self-containment attestation | FAIL |
| C-50 Semantic category grouping | FAIL |
| C-51 Pass/halt co-location | FAIL |
| C-52 Count derivation arithmetic | FAIL |
| C-53 Procedural pre-proposal step as schema block | FAIL |
| C-54 Typed component labels in arithmetic | FAIL |
| C-55 Attestation clause cross-references N | FAIL |

**C-43–C-55: 0/13 for all variations.**

---

### Composite Scores

| Variation | C-01–C-08 | C-09–C-42 | C-43–C-55 | Total | % |
|-----------|-----------|-----------|-----------|-------|---|
| V-01 | 8 | 25.5 | 0 | 33.5/55 | 61% |
| V-02 | 8 | 24 | 0 | 32/55 | 58% |
| V-03 | 8 | 24.5 | 0 | 32.5/55 | 59% |
| V-04 | 8 | 26.5 | 0 | 34.5/55 | 63% |
| **V-05** | **8** | **28.5** | **0** | **36.5/55** | **66%** |

**Ranking: V-05 > V-04 > V-01 > V-03 > V-02**

---

### Per-Variation Notes

**V-01** (Inertia as verbatim artifact blocks): Strongest inertia coverage among single-axis variations. INERTIA-GATE at all 3 sites. Misses slot architecture, register naming, step rationale.

**V-02** (Full slot architecture): Strongest enforceability at decision sites. Drops inertia recurrence at Steps 4b and 7. No degenerate register naming. Slot format replaces conditional branch at confirmation gate, which closes a skip path that V-01's "Write exactly" leaves open.

**V-03** (Degenerate register discrimination): PHASE 3 EXIT GATE verifies all 5 narrative sites against register requirement. Strongest guard against step-description narratives. Drops inertia downstream (Steps 4b, 7).

**V-04** (Schema-first sequence): Achieves full inertia downstream coverage via "Recall" sentences at all 3 gate sites. Schema committed before role identity prevents output scope narrowing. Partial slot (calibration only). No degenerate register naming. Loses step rationale preambles.

**V-05** (Combined): All three axes active simultaneously. Step existence rationale preambles unique to V-05 — each step declares its analytical purpose, making it self-justifying and auditable. PHASE 3 EXIT GATE cross-checks both narrative register AND INERTIA-GATE blocks by name. Full slot architecture + verbatim interrupt blocks + register naming = three independent omission guards operating at different levels.

---

### Excellence Signals from V-05

**1. Step existence rationale preambles** — Every step opens with "This step exists so that [analytical purpose]." This converts steps from procedural instructions into self-justifying analytical blocks. A reader who finds Step 2 empty can assess whether the purpose was served, not just whether the step ran. This adds an auditing layer that is independent of structural gating.

**2. PHASE 3 EXIT GATE includes INERTIA-GATE verification by name** — V-05's exit gate explicitly checks both the narrative register at each site AND that INERTIA-GATE blocks were reproduced verbatim. This makes the exit gate a cross-artifact consistency check, not just a register-format check. A missing INERTIA-GATE block would fail the exit gate even if the narrative register is correct.

**3. Layered omission guards at different enforcement levels** — V-05 stacks three independent omission-prevention mechanisms: (a) INERTIA-GATE as output artifact at gate sites, (b) pre-printed slots as structural fill-ins at decision sites, (c) degenerate register naming as category error at narrative sites. Each targets a different failure mode, making the combination more robust than any single mechanism alone.

---

```json
{"top_score": 66, "all_essential_pass": true, "new_patterns": ["Step existence rationale preambles — each step declares its analytical purpose ('This step exists so that...'), making steps self-justifying and auditable beyond structural presence", "PHASE 3 EXIT GATE cross-checks both narrative register and INERTIA-GATE block presence by name, creating a dual-artifact consistency check rather than a single-register gate", "Layered omission guards at independent levels — verbatim artifact blocks (gate sites) + pre-printed fill-in slots (decision sites) + degenerate register naming (narrative sites) target three structurally distinct failure modes simultaneously"]}
```
