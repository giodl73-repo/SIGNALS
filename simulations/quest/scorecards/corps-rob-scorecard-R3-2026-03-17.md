## Corps-ROB Variate R3 — Scoring (Rubric v2)

### Rubric Reference

**Essential** (C-01 through C-05): Stage labeling, role-loaded perspective, ROB format, actionable findings, TPM go/no-go.
**Recommended** (C-06 through C-09): Risk register, mission cascade, cross-stage coherence (C-08), inertia anchor (C-09).
**Aspirational** (C-10 through C-13): Cross-cutting themes, handoff packet at close, stage-boundary blocker, inertia anchor+per-stage check.

Scoring basis: R2 V-05 = 97 (baseline). C-10 FAIL = -2 pts, C-11 PARTIAL = -1 pt. Full fix of both = +3 → ceiling 100.

---

### V-01 — Cross-Cutting Themes Only (C-10 Fix, Minimal Base)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage Labeling | PASS | `## Stage: [stage-name]` + `ROLE:` in every STEP 1 |
| C-02 Role-Loaded | PASS | INERTIA CHECK grounds role perspective; findings format specifies role lens |
| C-03 ROB Format | PASS | All four elements: header, role identity, severity labels, verdict token |
| C-04 Actionable Findings | PASS | Minimum 2, owner+resolution required, artifact-specific |
| C-05 TPM Go/No-Go | PASS | Explicit `### Go/No-Go` section with labeled verdict |
| C-06 Risk Register | PASS | 3-entry minimum, HIGH/HIGH required |
| C-07 Mission Cascade | PASS | Specific mission name required, 1-row minimum |
| C-08 Cross-Stage Coherence | PASS | Cross-Stage References in Step 2 (F-IDs, confirm/escalate/contradict); handoff packet chains forward |
| C-09 Inertia Coverage | PASS | `## Inertia Anchor` block before Stage 1, concrete specificity enforced |
| C-10 Cross-Cutting Themes | **PASS** | **SECTION A has named theme table (≥2 themes), F-IDs from different stages, elevation sentence required** |
| C-11 Handoff Packet at Close | **PARTIAL** | **Handoff Packet = `PASSING TO NEXT STAGE` + `BLOCKER` only. No `CROSS-STAGE SYNTHESIS` field. Backward F-IDs live in Step 2 findings section, not at stage close.** |
| C-12 Stage-Boundary Blocker | PASS | `BLOCKER: YES — [F-ID] — ... / NO` in every handoff packet |
| C-13 Inertia Anchor+Per-Stage | PASS | Anchor before Stage 1 + `INERTIA CHECK:` in every STEP 1 |

**Composite: 90 + C-09(2) + C-10(2) + C-11(1) + C-12(2) + C-13(2) = 99**
All essential: PASS

---

### V-02 — Backward-Consolidating Packet (C-11 Fix, No Briefing Envelope)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage Labeling | PASS | `## Stage:` + `ROLE:` in SECTION 1 |
| C-02 Role-Loaded | PASS | INERTIA CHECK + role-lens instruction in findings; adequate without briefing envelope |
| C-03 ROB Format | PASS | All four structural elements present |
| C-04 Actionable Findings | PASS | Minimum 2, owner+resolution, artifact-specific |
| C-05 TPM Go/No-Go | PASS | Labeled Go/No-Go section |
| C-06 Risk Register | PASS | 3 entries, HIGH/HIGH minimum |
| C-07 Mission Cascade | PASS | Specific mission required |
| C-08 Cross-Stage Coherence | **PARTIAL** | **No briefing envelope; no cross-stage references section in findings. CROSS-STAGE SYNTHESIS only at close. Stage 2+ findings do not structurally require responding to forwarded question. Backward linkage exists but coherence chain is not enforced at stage open.** |
| C-09 Inertia Coverage | PASS | Anchor block present |
| C-10 Cross-Cutting Themes | **FAIL** | **END-OF-RUN SUMMARY only; no Cross-Cutting Themes section, no named theme table, no elevation sentences** |
| C-11 Handoff Packet at Close | **PASS** | **`CROSS-STAGE SYNTHESIS (Stage 2+ only)` in handoff packet, F-ID entries with relationship types, total ≥5 across 6-stage run** |
| C-12 Stage-Boundary Blocker | PASS | `BLOCKER:` field in handoff packet |
| C-13 Inertia Anchor+Per-Stage | PASS | Anchor + INERTIA CHECK per stage |

C-08 PARTIAL deducts ~1 from recommended base.

**Composite: 89 + C-09(2) + C-10(0) + C-11(2) + C-12(2) + C-13(2) = 97**
All essential: PASS

---

### V-03 — C-11 Fix on V-05 Base (Enriched Handoff Packet, Briefing Envelope Preserved)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage Labeling | PASS | `## Stage:` + `ROLE:` in PART 2 |
| C-02 Role-Loaded | PASS (strong) | Briefing envelope requires lens-directed KEY CONCERNS selection ("a TPM selects for schedule and dependency risk; a PM selects for adoption…"). Strongest C-02 mechanism. |
| C-03 ROB Format | PASS | All four elements |
| C-04 Actionable Findings | PASS | 2+ findings, owner+resolution, specific |
| C-05 TPM Go/No-Go | PASS | Labeled Go/No-Go |
| C-06 Risk Register | PASS | 3 entries minimum |
| C-07 Mission Cascade | PASS | Specific mission required |
| C-08 Cross-Stage Coherence | PASS (strong) | Triple mechanism: briefing envelope (lens-filtered distillation at open) + Cross-Stage References in findings + CROSS-STAGE SYNTHESIS in handoff packet at close |
| C-09 Inertia Coverage | PASS | Anchor block present |
| C-10 Cross-Cutting Themes | **FAIL** | **END-OF-RUN SUMMARY only (INERTIA STATUS, BRIEFING CHAIN HEALTH, BLOCKERS RAISED). No Cross-Cutting Themes section.** |
| C-11 Handoff Packet at Close | **PASS** | **CROSS-STAGE SYNTHESIS in PART 4 handoff packet, ≥5 entries across run, relationship-typed F-IDs** |
| C-12 Stage-Boundary Blocker | PASS | `BLOCKER:` in every handoff packet |
| C-13 Inertia Anchor+Per-Stage | PASS | Anchor + INERTIA CHECK at every stage open |

**Composite: 90 + C-09(2) + C-10(0) + C-11(2) + C-12(2) + C-13(2) = 98**
All essential: PASS

---

### V-04 — Both Gaps Fixed, V-05 Base (C-10 + C-11, Briefing Envelope Preserved)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage Labeling | PASS | `## Stage:` + `ROLE:` in PART 2 |
| C-02 Role-Loaded | PASS (strong) | Briefing envelope with explicit lens-directed selection enforced at stage open; "Must be lens-directed" stated |
| C-03 ROB Format | PASS | All four elements |
| C-04 Actionable Findings | PASS | 2+ per stage, owner+resolution required |
| C-05 TPM Go/No-Go | PASS | Labeled Go/No-Go section |
| C-06 Risk Register | PASS | 3 entries, HIGH/HIGH or HIGH/MED required |
| C-07 Mission Cascade | PASS | Specific mission name enforced |
| C-08 Cross-Stage Coherence | PASS (strong) | Briefing envelope + Cross-Stage References (PART 3) + CROSS-STAGE SYNTHESIS in packet (PART 4). Anti-copy constraint ("Must add substance not already stated in the Cross-Stage References section above") prevents surface redundancy. |
| C-09 Inertia Coverage | PASS | Anchor block with "Current state" failure example |
| C-10 Cross-Cutting Themes | **PASS** | **SECTION A: named theme table (≥2 themes), ≥2 F-IDs from different stages, elevation sentence per theme explaining what multi-stage recurrence adds to severity. Explicit convergence rationale required.** |
| C-11 Handoff Packet at Close | **PASS** | **CROSS-STAGE SYNTHESIS in PART 4 handoff packet, ≥5 entries across 6-stage run, F-IDs with relationship types, anti-copy constraint enforces genuine downstream significance** |
| C-12 Stage-Boundary Blocker | PASS | `BLOCKER: YES — [F-ID] — ... / NO` at every stage close |
| C-13 Inertia Anchor+Per-Stage | PASS | Anchor + INERTIA CHECK at every stage open |

**Composite: 90 + C-09(2) + C-10(2) + C-11(2) + C-12(2) + C-13(2) = 100**
All essential: PASS

---

### V-05 — Constraint-Minimized Full Coverage (No Briefing Envelope)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage Labeling | PASS | `## Stage:` + `ROLE:` in SECTION 1 |
| C-02 Role-Loaded | PASS | Explicit anti-generic instruction in SECTION 2: "Generic findings that any reviewer could have written… do not satisfy C-02 on their own." INERTIA CHECK grounds role perspective. Weaker than V-04's briefing envelope but sufficient. |
| C-03 ROB Format | PASS | All four structural elements |
| C-04 Actionable Findings | PASS | 2+ per stage, owner+resolution required |
| C-05 TPM Go/No-Go | PASS | Labeled Go/No-Go with F-ID or R-ID citation |
| C-06 Risk Register | PASS | 3 entries, HIGH/HIGH minimum |
| C-07 Mission Cascade | PASS | Specific mission name enforced |
| C-08 Cross-Stage Coherence | PASS | CROSS-STAGE SYNTHESIS in handoff packet provides backward F-ID linkage across all 5 later stages (≥5 total). OUTPUT RULE clarifies: "sole vehicle for backward F-ID linkage." Sufficient without briefing envelope; weaker than V-04 but passes. |
| C-09 Inertia Coverage | PASS | Anchor block before Stage 1, "Current state" failure example |
| C-10 Cross-Cutting Themes | **PASS** | **SECTION A: named theme table, ≥2 F-IDs from different stages per theme, elevation sentence per theme. Rationale for convergence significance explicitly required.** |
| C-11 Handoff Packet at Close | **PASS** | **CROSS-STAGE SYNTHESIS (Stage 2+ only) in handoff packet at close; ≥5 entries across 6-stage run; relationship-typed F-IDs** |
| C-12 Stage-Boundary Blocker | PASS | `BLOCKER:` field in every handoff packet |
| C-13 Inertia Anchor+Per-Stage | PASS | Anchor + INERTIA CHECK per stage |

**Composite: 90 + C-09(2) + C-10(2) + C-11(2) + C-12(2) + C-13(2) = 100**
All essential: PASS

---

### Rankings

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|--------------|-------|
| 1 | **V-04** | **100** | YES | Both gaps fixed; strongest C-02/C-08 via briefing envelope; anti-copy constraint prevents redundancy collapse |
| 2 | **V-05** | **100** | YES | Both gaps fixed; minimal surface; C-08 weaker but passes; C-02 held by explicit anti-generic instruction |
| 3 | V-01 | 99 | YES | C-10 fix; C-11 PARTIAL (backward F-IDs in findings section, not in closing packet) |
| 4 | V-03 | 98 | YES | C-11 fix; C-10 still FAIL; strongest structure otherwise |
| 5 | V-02 | 97 | YES | C-11 fix; C-10 FAIL; C-08 PARTIAL (no briefing envelope, no findings-level cross-stage refs) |

---

### Excellence Signals from V-04 (Top)

**What V-04 added over R2's 97 ceiling:**

1. **Bi-directional closing packet** — The handoff packet at every stage close now carries both a forward charge (`PASSING TO NEXT STAGE`) and a backward synthesis block (`CROSS-STAGE SYNTHESIS` with F-IDs and relationship types). C-11 compliance is now structural, not memory-dependent.

2. **Anti-copy constraint on dual synthesis surfaces** — V-04 has both a Cross-Stage References section (in Part 3 findings) and a CROSS-STAGE SYNTHESIS block (in Part 4 handoff packet). The explicit instruction "Must add substance not already stated in the Cross-Stage References section above" prevents the two surfaces from collapsing into copies and forces genuine escalation analysis at packet close.

3. **Cross-Cutting Themes as a required elevation ceremony** — SECTION A after all stages mandates a named theme table with F-IDs from ≥2 different stages plus a mandatory elevation sentence: "what does multi-stage recurrence add to severity that the individual finding did not establish?" This formalizes C-10 convergence and creates a structural home that cannot be satisfied by the run-level diagnostics in the ROB Summary alone.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["bi-directional-closing-packet", "anti-copy-constraint-on-dual-synthesis-surfaces", "cross-cutting-themes-elevation-sentence"]}
```
