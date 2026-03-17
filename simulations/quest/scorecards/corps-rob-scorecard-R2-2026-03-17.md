## corps-rob — Quest Score (Round 2, Rubric v2)

### Scoring Framework

| Weight tier | Points | Criteria |
|-------------|--------|----------|
| Essential (5) | 60 pts (12 ea.) | C-01 through C-05 |
| Recommended (3) | 30 pts (10 ea.) | C-06 through C-08 |
| Aspirational (5) | 10 pts (2 ea.) | C-09 through C-13 |

PARTIAL = half-points. Golden threshold = all essential pass + composite ≥ 80.

---

## Variation Scorecards

### V-01 — Per-Stage Distributed Inertia

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | `## Stage: [stage-name]` + `ROLE:` in every section; all 6 canonical names listed |
| C-02 | essential | **PASS** | Findings explicitly required to connect to "this role's lens and inertia context"; at least one finding must link to the role's inertia statement |
| C-03 | essential | **PASS** | Stage header ✓, role identity ✓, severity-labeled findings (HIGH/MED/LOW) ✓, APPROVED/BLOCKED/DEFERRED/APPROVED WITH CONDITIONS ✓ |
| C-04 | essential | **PASS** | Minimum 2 findings per stage with Owner + Resolution; total ≥ 2 × N_stages |
| C-05 | essential | **PASS** | `### Go/No-Go` + bold `**GO / NO-GO / GO WITH CONDITIONS**` with F-ID or R-ID rationale required |
| C-06 | recommended | **PASS** | TPM Risk Register table ≥3 entries, severity + likelihood + mitigation; at least 1 HIGH/HIGH required |
| C-07 | recommended | **PASS** | `### Mission Cascade` table in exec-office with named mission + ALIGNED/PARTIAL/GAP |
| C-08 | recommended | **PASS** | `[Cross-Stage References — Stage 2+ only]` block with confirm/escalate/contradict required in Findings; produces ≥5 backward entries in a full run |
| C-09 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] / NO` in Handoff Packet at every stage close; names blocking finding at stage boundary |
| C-10 | aspirational | **FAIL** | END-OF-RUN SUMMARY has `INERTIA PATTERN` but no document-level Cross-Cutting Themes section citing 2+ independent stage instances |
| C-11 | aspirational | **PARTIAL** | `### Handoff Packet` labeled section exists at every stage close; but packet contains only PASSING TO NEXT STAGE + BLOCKER — no backward cross-stage entries with source F-ID + relationship type as C-11 requires in the packet itself |
| C-12 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] / NO` at stage close (inside Handoff Packet) — populated at the boundary, not retroactively |
| C-13 | aspirational | **PARTIAL** | All 6 stages have `### Role Inertia Statement` with `INERTIA (this role's view)` — second condition (≥3 per-stage checks) met; but **no global INERTIA ANCHOR before Stage 1** — first condition explicitly omitted by design |

**Composite:** (5/5 × 60) + (3/3 × 30) + (2+0+1+2+1)/10 × 10 = 60 + 30 + **6** = **96**
All essential: ✅

---

### V-02 — Blocker-at-Open (Reversed Detection)

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | Stage headers + role identity in Part 2 for all stages; canonical names used |
| C-02 | essential | **PASS** | `INERTIA CHECK: [threatened / not at risk this stage]` per stage + findings from role's lens; global anchor provides shared reference |
| C-03 | essential | **PASS** | Stage header ✓, role identity ✓, severity-labeled findings ✓, VERDICT token ✓ |
| C-04 | essential | **PARTIAL** | Normal case: ≥2 findings with Owner+Resolution per stage. **Structural defect**: design explicitly says "do not write findings for a held stage" — a HOLD stage produces 0 findings, making total < 2 × N_stages_run. The prompt sanctions this outcome, creating a known rubric violation path |
| C-05 | essential | **PASS** | `### Go/No-Go` with bold GO/NO-GO token; TPM HOLD would be an extreme edge case (requires 4+ prior HOLDs) |
| C-06 | recommended | **PASS** | TPM Risk Register table ≥3 entries |
| C-07 | recommended | **PASS** | exec-office Mission Cascade table |
| C-08 | recommended | **PASS** | Gate Check in Part 1 engages explicitly with prior verdict + blockers; cross-stage references in Part 3 Findings (Stage 2+). Dual mechanism — strongest C-08 of the three single-axis variants |
| C-09 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] — [downstream stage] / NO` in Part 4 Verdict, populated at close |
| C-10 | aspirational | **FAIL** | `GATE HISTORY` / `BLOCKERS RAISED` in summary — not a cross-cutting theme section |
| C-11 | aspirational | **FAIL** | No dedicated HANDOFF PACKET section at stage close. Part 4 contains only VERDICT + BLOCKER. No PASSING TO NEXT STAGE element — the packet form is entirely absent |
| C-12 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] / NO` in Part 4 Verdict at stage close — at the boundary, not retroactive |
| C-13 | aspirational | **PASS** | Global INERTIA ANCHOR before Stage 1 ✓; per-stage `INERTIA CHECK: [threatened / not at risk]` in Part 2 at all 6 stages ✓ |

**Composite:** (4.5/5 × 60) + (3/3 × 30) + (2+0+0+2+2)/10 × 10 = 54 + 30 + **6** = **90**
All essential: ❌ (C-04 PARTIAL)

---

### V-03 — Handoff-Centric Structure

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | `## Stage: [stage-name]` + `ROLE:` in Section 1 of every stage |
| C-02 | essential | **PASS** | Findings in Section 2 must come from "this role's lens"; Stage 2+ requires at least one finding to directly respond to MY CHARGE — role-specific engagement enforced |
| C-03 | essential | **PASS** | Stage header ✓, role identity ✓, severity-labeled findings ✓, VERDICT token ✓ |
| C-04 | essential | **PASS** | ≥2 findings per stage with Owner + Resolution; specificity enforced ("must reference the specific artifact or behavior") |
| C-05 | essential | **PASS** | `### Go/No-Go` + bold `**GO / NO-GO / GO WITH CONDITIONS**` with F-ID/R-ID rationale |
| C-06 | recommended | **PASS** | TPM Risk Register table ≥3 entries, severity+likelihood+mitigation, at least 1 HIGH |
| C-07 | recommended | **PASS** | exec-office `### Mission Cascade` table with ALIGNED/PARTIAL/GAP |
| C-08 | recommended | **PASS** | RECEIVED FROM PRIOR STAGE / MY CHARGE (Section 1) creates active forward-chain engagement; `CROSS-STAGE (Stage 2+ only)` block in Findings (Section 2) adds backward F-ID references; dual mechanism |
| C-09 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] / NO` in `### Handoff Packet` at stage close (Section 3); names blocking finding at boundary |
| C-10 | aspirational | **FAIL** | `FORWARD CHAIN HEALTH` / `UNRESOLVED CHARGES` in summary — not a cross-cutting theme section citing repeated instances |
| C-11 | aspirational | **PARTIAL** | `### Handoff Packet` labeled section exists at every stage close with PASSING TO NEXT STAGE + CONTEXT + BLOCKER. But packet is forward-facing; no backward cross-stage reference entries with source F-ID + relationship type. CONTEXT field provides implicit linkage without the structured format C-11 requires |
| C-12 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] / NO` in Handoff Packet at stage close; per-stage, not retroactive |
| C-13 | aspirational | **PARTIAL** | Global INERTIA ANCHOR before Stage 1 ✓ (first condition met). But Stage Format (Sections 1-3) contains no INERTIA CHECK — no per-stage framing of status-quo pressure. **0 of 6 stages** have an inertia check; second condition requires ≥3. Variate summary noted this as an intentional design risk |

**Composite:** (5/5 × 60) + (3/3 × 30) + (2+0+1+2+1)/10 × 10 = 60 + 30 + **6** = **96**
All essential: ✅

---

### V-04 — Distributed Inertia + Handoff-Centric + Blocker (No Global Anchor)

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | `## Stage: [stage-name]` + `ROLE:` in Section A; all canonical stage names |
| C-02 | essential | **PASS** | `WHAT THIS ROLE DEFENDS` in Section A anchors findings to role-specific behavior; findings must connect to inertia statement (Section A) AND received forward (Section B) for Stage 2+ — strongest dual-enforcement of role-loading |
| C-03 | essential | **PASS** | Stage header ✓, role identity ✓, severity-labeled findings ✓, VERDICT token ✓ |
| C-04 | essential | **PASS** | ≥2 findings per stage with Owner + Resolution; specificity required |
| C-05 | essential | **PASS** | `### Go/No-Go` + bold GO/NO-GO/GO WITH CONDITIONS in TPM stage |
| C-06 | recommended | **PASS** | TPM Risk Register table ≥3 entries, severity+likelihood+mitigation, at least 1 HIGH/HIGH |
| C-07 | recommended | **PASS** | exec-office `### Mission Cascade` table |
| C-08 | recommended | **PASS** | Section B (Received Forward) + Section C cross-stage refs = dual backward engagement mechanism; RECEIVED FORWARD requires explicit MY RESPONSE (RESOLVE/ESCALATE/DEFER) — active, not passive |
| C-09 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] / NO` in Section D Handoff Packet at stage close, with downstream impact |
| C-10 | aspirational | **FAIL** | `INERTIA MAP` + `BLOCKER CHAIN` in summary — no cross-cutting theme section |
| C-11 | aspirational | **PARTIAL** | `### Handoff Packet` in Section D exists at every stage close with PASSING TO NEXT STAGE + INERTIA NOTE + BLOCKER. Packet is forward-facing; backward linkage is in Section B (Received Forward) at stage open, not in the packet at close. No F-ID cross-stage entries in the closing packet itself |
| C-12 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] / NO` in Section D (stage close); boundary-point detection |
| C-13 | aspirational | **PARTIAL** | All 6 stages have `### Inertia Statement (this role)` with `WHAT THIS ROLE DEFENDS` + `INERTIA PRESSURE` — second condition (≥3 per-stage checks) met. **No global INERTIA ANCHOR before Stage 1** — first condition explicitly omitted. Same asymmetry as V-01 (per-stage rich, globally unanchored) |

**Composite:** (5/5 × 60) + (3/3 × 30) + (2+0+1+2+1)/10 × 10 = 60 + 30 + **6** = **96**
All essential: ✅

---

### V-05 — Briefing Envelope + Global Anchor + Handoff + Blocker

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | `## Stage: [stage-name]` + `ROLE:` in Part 2; all canonical stages present |
| C-02 | essential | **PASS** | Briefing Envelope (Part 1) explicitly filters prior findings through "this stage's lens" — role-directed selection enforced at the prompt level. INERTIA CHECK in Part 2 adds role-specific framing. Richest role-loading mechanism of all 5 variations |
| C-03 | essential | **PASS** | Stage header ✓, role identity ✓, severity-labeled findings ✓, VERDICT token ✓ |
| C-04 | essential | **PASS** | ≥2 findings per stage with Owner + Resolution; Stage 2+ requires at least one finding to directly respond to OPEN QUESTION FORWARDED — specificity enforced |
| C-05 | essential | **PASS** | `### Go/No-Go` + bold `**GO / NO-GO / GO WITH CONDITIONS**` with F-ID/R-ID rationale |
| C-06 | recommended | **PASS** | TPM Risk Register table ≥3 entries, severity+likelihood+mitigation, at least 1 HIGH/HIGH or HIGH/MED |
| C-07 | recommended | **PASS** | exec-office `### Mission Cascade` table with named mission + ALIGNED/PARTIAL/GAP |
| C-08 | recommended | **PASS** | Three-layer mechanism: (1) Briefing Envelope KEY CONCERNS selection with F-IDs, (2) OPEN QUESTION FORWARDED verbatim from prior packet, (3) `### Cross-Stage References` section in Part 3 (min 1 per Stage 2+). Strongest C-08 architecture of all 5 variations |
| C-09 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] — [downstream stage] / NO` in Handoff Packet (Part 4); boundary-point detection, names impacted stage |
| C-10 | aspirational | **FAIL** | `BRIEFING CHAIN HEALTH` + `BLOCKERS RAISED` in summary — no document-level cross-cutting theme section citing 2+ independent stage instances with elevated severity |
| C-11 | aspirational | **PARTIAL** | `### Handoff Packet` at stage close (Part 4) with PASSING TO NEXT STAGE + BLOCKER. Backward synthesis (with F-IDs) is in the Briefing Envelope at stage **open** (Part 1). C-11 requires backward cross-stage entries in the closing packet — V-05 achieves the goal but splits it across open+close rather than consolidating at close. Packet structure exists; required format is distributed |
| C-12 | aspirational | **PASS** | `BLOCKER: YES — [F-ID] — [downstream stage] / NO` in Handoff Packet at stage close; per-stage, at the boundary |
| C-13 | aspirational | **PASS** | Global INERTIA ANCHOR before Stage 1 ✓; `INERTIA CHECK` in Part 2 at all 6 stages ✓; INERTIA STATUS field in Briefing Envelope tracks whether the displacement picture has evolved ✓. Both conditions met — the only R2 variation achieving full C-13 compliance |

**Composite:** (5/5 × 60) + (3/3 × 30) + (2+0+1+2+2)/10 × 10 = 60 + 30 + **7** = **97**
All essential: ✅

---

## Rankings

| Rank | Variation | Score | All Essential | C-13 | C-11 |
|------|-----------|-------|---------------|------|------|
| 1 | **V-05** Briefing Envelope + Full Integration | **97** | ✅ | PASS | PARTIAL |
| 2 (tie) | **V-01** Per-Stage Distributed Inertia | **96** | ✅ | PARTIAL | PARTIAL |
| 2 (tie) | **V-03** Handoff-Centric | **96** | ✅ | PARTIAL | PARTIAL |
| 2 (tie) | **V-04** Distributed + Handoff + Blocker (No Anchor) | **96** | ✅ | PARTIAL | PARTIAL |
| 5 | **V-02** Blocker-at-Open | **90** | ❌ | PASS | FAIL |

---

## Why V-05 Wins

V-05's decisive margin is **C-13 PASS** (2 pts) vs PARTIAL (1 pt) for V-01/V-03/V-04. This stems from one design difference: V-05 is the only R2 variation combining **both** a global INERTIA ANCHOR before Stage 1 (shared organizational reference) and per-stage INERTIA CHECK at each stage (role-specific framing). V-01 and V-04 have per-stage inertia but no shared anchor; V-03 has the anchor but no per-stage checks.

The **Briefing Envelope** (Part 1, Stage 2+) also contributes the strongest C-08 architecture: three independent cross-stage mechanisms (KEY CONCERNS with F-IDs, OPEN QUESTION FORWARDED verbatim, Cross-Stage References section). Each stage actively distills prior outputs through this role's specific lens rather than relying on passive recall.

**C-10 is the universal ceiling.** No R2 variation addresses cross-cutting theme elevation — all five fail. The END-OF-RUN SUMMARY fields (INERTIA PATTERN, GATE HISTORY, FORWARD CHAIN, INERTIA MAP, BRIEFING CHAIN HEALTH) are run-level diagnostics, not document-level theme aggregators. C-10 requires a named theme with ≥2 stage citations and elevated severity explanation.

**V-02's structural defect** (HOLD-stage produces 0 findings, violating C-04's 2×N floor) is design-intentional — the prompt explicitly documents it — but it costs C-04 essential credit and drops the score to 90.

---

## Excellence Signals (V-05)

| Signal | Pattern | Mechanism |
|--------|---------|-----------|
| Briefing Envelope at stage open | `briefing-envelope-at-stage-open` | Each stage (2+) opens with a structured synthesis of prior findings filtered through the incoming role's specific lens, including explicit F-ID selection, verbatim handoff capture, and INERTIA STATUS update |
| Inertia status continuity tracking | `inertia-status-continuity-tracking` | INERTIA STATUS field in Briefing Envelope asks whether any prior stage's finding has changed the displacement picture from the global anchor — evolves the shared reference rather than treating it as static throughout the run |

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["briefing-envelope-at-stage-open", "inertia-status-continuity-tracking"]}
```
