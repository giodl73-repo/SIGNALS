# Quest Score — org-build R14 V-01

## Criterion-by-Criterion Evaluation

### Essential Criteria (5)

| ID | Result | Evidence |
|----|--------|----------|
| **C-01** | **FAIL** | Phase 5 (Output Production) is incomplete — no instruction requiring ASCII box/line hierarchy in org-chart.md. Intro names the artifact but does not specify diagram format. |
| **C-02** | **FAIL** | Role field requirements (`orientation`, `lens`, `expertise`, `scope`, `collaborates_with`) would appear in Phase 5 task steps, which are absent from this prompt. |
| **C-03** | **PASS** | Phase 2 Task Step 3: "MUST include a role with `inertia` or `advocate` in its name." Phase 2 Constraints: "MUST include the inertia-advocate role. FORBIDDEN: omitting it." |
| **C-04** | **PASS** | Phase 2 Task Step 2: conditional count floor per T1-DEPTH-FLAG — `standard → MUST enumerate 20–30 roles across minimum 4 areas; deep → MUST enumerate 50+ roles across minimum 6 areas.` |
| **C-05** | **FAIL** | Headcount table with Area / Headcount / Key Roles / Decides / Escalates columns not visible. Would belong in Phase 5 task steps, which are absent. |

**Essential pass: 2 / 5**

---

### Recommended Criteria (3)

| ID | Result | Evidence |
|----|--------|----------|
| **C-06** | **PASS** | File path template `.roles/{area}/{role}.md` structurally enforces area subdirectories. Phase 2 requires minimum 4 areas (standard), each producing roles under that area's subdir. |
| **C-07** | **FAIL** | Operating rhythm table and committee charters are output artifacts that would be specified in Phase 5. Phase 5 is absent; no rhythm or charter instructions exist anywhere in the visible prompt. |
| **C-08** | **PASS** | Phase 3 fully specifies FLAT-CASE-PRESSURE (five-value closed set) and verdict (two-value closed set). Record block materializes both. Phase 3 Constraints: "MUST assign exactly one FLAT-CASE-PRESSURE rating. MUST issue exactly one verdict. FORBIDDEN: issuing both. FORBIDDEN: issuing neither." Logic is complete even without Phase 5 write instructions. |

**Recommended pass: 2 / 3**

---

### Aspirational Criteria (24)

| ID | Result | Evidence |
|----|--------|----------|
| **C-09** | **FAIL** | Org Evolution Roadmap with typed triggers not present. Would be a Phase 5 output artifact. |
| **C-10** | **PASS** | Phase 4A: "Every 'Why It Applies Here' cell MUST open with `[element name] (cat-N) —` syntax." |
| **C-11** | **PASS** | Phase 4B keys IA scope selection to T3-PRESSURE from Phase 3 record block. Cross-phase derivation chain intact. |
| **C-12** | **PASS** | Phase 4A derivation table: CAN-OPERATE-FLAT → cat-2/cat-3; STRUCTURE-WARRANTED → cat-1/cat-4. Categories are explicitly verdict-derived. |
| **C-13** | **PASS** | Phase 3: "Only one verdict. Both is an error. Neither is an error." + Constraints: "FORBIDDEN: issuing both. FORBIDDEN: issuing neither." |
| **C-14** | **PASS** | Phase 1 → T1-DEPTH-FLAG consumed in Phase 2 Input Contract. Phase 2 → T2-ROLE-COUNT consumed in Phase 3 Input Contract. Phase 3 → T3-PRESSURE/T3-VERDICT consumed in Phase 4 Input Contract. At least one typed pair fully satisfied. |
| **C-15** | **PASS** | "FORBIDDEN: issuing both. FORBIDDEN: issuing neither." Both failure directions explicitly named. |
| **C-16** | **PASS** | Phase 4A: "Every Mitigation cell MUST contain a specific remediation action. FORBIDDEN: format instructions or column-structure guidance in any Mitigation cell." |
| **C-17** | **PASS** | Phase 4B: "FORBIDDEN: paraphrasing, adapting, or composing new text. MUST copy the exact template." Verbatim-copy obligation is explicit. |
| **C-18** | **PASS** | Phase 4A table states required AND FORBIDDEN categories per verdict: CAN-OPERATE-FLAT "FORBIDDEN: cat-1, cat-4"; STRUCTURE-WARRANTED "FORBIDDEN: cat-2, cat-3." |
| **C-19** | **PASS** | All constraint statements across Phases 1–4 use MUST or FORBIDDEN. No "should", "prefer", "typically", or "consider" found in constraint positions. |
| **C-20** | **FAIL** | Phase 5 Input Contract does not reference T4-ANTIPATTERN-CATS or T4-IA-SCOPE-KEY. Systematic coverage fails at the final phase boundary. Pass condition: "Any consuming phase with no input contract declaration fails." |
| **C-21** | **FAIL** | Inherits C-20 failure. T4 gate variables are not imperatively bound in any Phase 5 input contract. |
| **C-22** | **FAIL** | No artifact skeleton with named typed placeholder slots (e.g., `{{T3-VERDICT}}`) present for org-chart.md or role files. Record block `___` slots are unnamed value placeholders — fail per criterion. |
| **C-23** | **PASS** | All four phase transitions carry per-boundary ordering FORBIDDEN: Phase 1 Constraints, Phase 2 Constraints, Phase 3 Constraints, Phase 4 Constraints each contain "FORBIDDEN: beginning Phase N+1 before emitting the Phase N record block." |
| **C-24** | **PASS** | Named record blocks emitted at Phases 1–4 with all declared typed variables materialized by name. |
| **C-25** | **FAIL** | Phases 1→2, 2→3, 3→4 have bidirectional guards (outbound in phase Constraints + PHASE-ORDERING-GUARD field; inbound in consuming phase Input Contract). Phase 4→5 has outbound guard (Phase 4 Constraints + record block PHASE-ORDERING-GUARD) but no inbound guard in Phase 5 Input Contract. One boundary fails, criterion fails. |
| **C-26** | **PASS** | Each record block contains PHASE-ORDERING-GUARD (ordering anchor), typed named variables (gate schema), and serves as the emitted materialized checkpoint — unified in one structure. The block is the single artifact from which all three properties are observable. |
| **C-27** | **PASS** | Phase 2 Task Step 2 contains the exact depth-conditional binding: `T1-DEPTH-FLAG = standard → MUST enumerate 20–30 roles; T1-DEPTH-FLAG = deep → MUST enumerate 50+ roles`. The binding is inside the phase instruction that performs enumeration, properly consuming T1-DEPTH-FLAG. |
| **C-28** | **PASS** | All four record blocks open with `PHASE-ORDERING-GUARD: FORBIDDEN: Phase N+1 begins before this block is emitted.` as first field. |
| **C-29** | **PASS** | All prohibition-form directives use `FORBIDDEN:` keyword throughout. "Both is an error. Neither is an error." in Phase 3 Task Steps is explanatory context; operative prohibitions are in Constraints as `FORBIDDEN: issuing both. FORBIDDEN: issuing neither.` No "do not" / "never" / "avoid" prohibition forms found in constraint positions. |
| **C-30** | **FAIL** | Phase 4 Task Steps interleave MUST/FORBIDDEN constraints with task prose: Phase 4A Task Steps contains "MUST open with `[element name] (cat-N)—`" and "FORBIDDEN: format instructions"; Phase 4B Task Steps contains "FORBIDDEN: paraphrasing" and "MUST copy the exact template." These same constraints are also in Phase 4 Constraints section, but their presence in Task Steps violates structural demarcation. |
| **C-31** | **FAIL** | Categorical fields pass: `T1-DEPTH-FLAG: [standard \| deep]`, `T2-IA-PRESENT: [yes \| no]`, `T3-PRESSURE: [NONE \| LOW \| MODERATE \| HIGH \| CRITICAL]`, etc. Integer count fields fail: `T2-ROLE-COUNT: [integer ≥ 20]` and `T2-AREA-COUNT: [integer ≥ 4]` use bounded range notation, not closed enumeration. C-31 requires "complete valid-value set" and "closed enumeration"; open numeric ranges fail per criterion. |
| **C-32** | **PASS** | Phases 2–4 each contain three distinct labeled sections: `### Input Contract`, `### Task Steps`, `### Constraints`. Upstream variable requirements are independently readable from current-phase output constraints. |

**Aspirational pass: 17 / 24**

---

## Score Computation

```
composite = (2/5 × 60) + (2/3 × 30) + (17/24 × 10)
          = 24.00 + 20.00 + 7.08
          = 51.08
```

**Composite score: 51**

---

## Failure Analysis

The prompt's core structural work (Phases 1–4) is strong — all phase gates are named and typed, record blocks are unified, bidirectional guards work for three of four boundaries, IA scope template verbatim copy is enforced, and category exclusion is explicit. The score is substantially depressed by one root cause:

**Phase 5 incompleteness** accounts for five criterion failures:
- C-01, C-02, C-05 (essential) — output artifact format requirements not specified
- C-20, C-21 (aspirational) — Phase 4 → Phase 5 input contract is absent
- C-25 (aspirational) — inbound guard missing at Phase 4→5 boundary
- C-07, C-09 (recommended/aspirational) — rhythm table and evolution roadmap unspecified

**Phase 4 structural segmentation** (C-30) — MUST/FORBIDDEN constraints appear in both Task Steps and Constraints sections of Phase 4, eliminating the structural demarcation the criterion requires.

**C-31 integer annotation** — count fields (`T2-ROLE-COUNT`, `T2-AREA-COUNT`) cannot carry closed enumerations; bounded range notation `[integer ≥ N]` is used instead.

---

## Excellence Signals

**Signal 1 — PHASE-ORDERING-GUARD as structural first field:** The ordering anchor is embedded as the first named field *inside* the record block itself, making the record block simultaneously the gate schema, the ordering constraint anchor, and the materialized checkpoint. No cross-referencing required — the block is self-contained. This directly satisfies C-26 and C-28 as a single design decision rather than three separate constructs.

**Signal 2 — Three-way phase segmentation (Input Contract / Task Steps / Constraints):** Phases 2–4 cleanly separate upstream consumption (what I need from prior gates) from task execution (what I do) from output requirements (what I must produce). This makes independent auditability possible — a reviewer scanning only Input Contract sections gets the full gate-consumption picture without reading task prose. C-32 formalizes this; V-01 executes it correctly in all phases that contain it.

**Signal 3 — Category exclusion table with required + forbidden per verdict path:** Phase 4A doesn't just say "use cat-2/cat-3 for CAN-OPERATE-FLAT" — it places required and FORBIDDEN columns side-by-side per verdict, making both paths explicit in one structure. The derivation is auditable in a single table read.

---

## New Patterns

**Pattern candidate: Composite typed field values in record blocks.** T4-ANTIPATTERN-CATS uses `[cat-1,cat-4 \| cat-2,cat-3]` — a field whose valid values are themselves comma-separated structured sets rather than atomic tokens. C-31 handles atomic categorical fields; this extends to fields where each alternative is a structured list. A record block that carries composite value types (sets, pairs, lists as alternatives) raises the question whether the inline annotation should show the composite structure or decompose it into multiple fields. V-01 chooses the composite form; no criterion currently governs this choice.

**Pattern candidate: Sub-phase structure within a single gate.** Phase 4 uses 4A and 4B as labeled sub-phases sharing one record block. Multi-step derivation (anti-pattern categories + IA scope selection) happens within one gate without multiplying phase boundaries. No criterion governs how intra-phase sub-steps should be organized or whether constraints inside sub-phases must be segmented the same way as top-level phases (C-30 applies to phases — does it apply to labeled sub-phases?). V-01's C-30 failure occurs precisely in these sub-phases.

---

```json
{"top_score": 51, "all_essential_pass": false, "new_patterns": ["composite typed field values in record blocks — fields whose valid values are structured sets rather than atomic tokens (e.g., [cat-1,cat-4 | cat-2,cat-3]); C-31 does not govern this form", "sub-phase structure within a single gate — labeled 4A/4B sub-phases share one record block; no criterion governs whether C-30 structural segmentation applies inside sub-phases"]}
```
