## listen-support — Round 2 Score Sheet

---

### Scoring Framework

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential (C-01–C-05) | 5 | 60 pts |
| Recommended (C-06–C-08) | 3 | 30 pts |
| Aspirational (C-09–C-13) | 5 | 10 pts |

Partial credit (PARTIAL) = 0.5 for aspirational only.

---

### Universal Baseline Assessment (all R2 variations)

All five variations share the three universal fixes. Evaluating these first since they are not the differentiating axis:

| Criterion | Prompt mechanism | Verdict |
|-----------|-----------------|---------|
| C-03 | PERFORMANCE MODE DECLARATION with first-person mandate + prohibition | **PASS all** |
| C-04 | Gap format requires `Tickets: T-NN, T-NN` in every entry | **PASS all** |
| C-06 | TABLE CHECK enforces `>= 6 and <= 12` before bodies generated | **PASS all** |

Additionally, all variations pass C-01 (STEP 5 vocabulary table), C-02 (Persona column in table), C-05 (TABLE CHECK with P0 <= 25%, high-vol <= 50%), C-07 (role minimums guarantee 3+ personas), and C-08 (gap format specifies named artifacts).

**Result: all 5 essential and all 3 recommended pass for every variation. Essential gate cleared. All variations are golden-eligible.**

---

### Aspirational Criteria — Variation-by-Variation

#### C-09 — Ticket Clustering and Theme Identification

| Variation | Mechanism | Verdict |
|-----------|-----------|---------|
| V-01 | STEP 7 Cross-Ticket Patterns table: named pattern, affected T-NNs, root cause, adoption cost. Post-hoc but pattern name + root cause maps to C-09 pass condition. | **PASS** |
| V-02 | No theme declaration. Migration friction sub-section in gap analysis is not ticket clustering. | **FAIL** |
| V-03 | STEP 2 Theme Declaration before any ticket; tickets written within themes; underlying failure declared per theme. C-09 satisfied by construction. | **PASS** |
| V-04 | STEP 7 Cross-Ticket Patterns (same as V-01, plus migration flag column). | **PASS** |
| V-05 | STEP 3 theme declaration + tickets organized by theme in STEP 6 + pattern table in STEP 7. Double coverage. | **PASS** |

#### C-10 — Ticket Lifecycle and Resolution Path

| Variation | Mechanism | Verdict |
|-----------|-----------|---------|
| V-01 | No resolution path step. | **FAIL** |
| V-02 | No resolution path step. | **FAIL** |
| V-03 | No resolution path step. | **FAIL** |
| V-04 | No resolution path step. | **FAIL** |
| V-05 | STEP 7B explicitly generates triage owner + root cause category + resolution type for every high-volume/P0/P1 ticket. Required table, all three fields. | **PASS** |

#### C-11 — Multi-Stage Structural Integrity

| Variation | Mechanism | Verdict |
|-----------|-----------|---------|
| V-01 | STEP 9 checks C-01–C-05 + phase match. Does NOT explicitly count broken T-NN refs. Gap format compliance is instructed but not verified. | **PARTIAL** |
| V-02 | STEP 8 verification pass. Same limitation — no zero-broken-T-NN check. | **PARTIAL** |
| V-03 | STEP 8 has theme integrity check but no zero-broken-T-NN check. | **PARTIAL** |
| V-04 | STEP 9 same as V-01. | **PARTIAL** |
| V-05 | STEP 9 Pass 2 explicitly: "Broken T-NN refs in gap entries: ___ (required: 0)". Only variation with an explicit zero check. Self-corrects before submission. | **PASS** |

#### C-12 — Role-Phase Compound Coverage

| Variation | Mechanism | Verdict |
|-----------|-----------|---------|
| V-01 | Role-phase cross-matrix (STEP 3) + constraint "any role with 3+ tickets must span at least 2 phases." Structurally enforced. | **PASS** |
| V-02 | Same role-phase cross-matrix + same constraint. | **PASS** |
| V-03 | STEP 3 role coverage check verifies counts only. Theme declaration has per-theme phase distribution but NO per-role phase constraint. No cross-matrix. | **FAIL** |
| V-04 | Role-phase cross-matrix + constraint (same as V-01). | **PASS** |
| V-05 | Role-phase cross-matrix (STEP 3A) + Constraint 2 explicitly labeled "(C-12)" + STEP 9 Pass 2 checks "Roles with 3+ tickets: [list] — each spans 2+ phases: Y/N". | **PASS** |

#### C-13 — Phase-Calibrated Severity

| Variation | Mechanism | Verdict |
|-----------|-----------|---------|
| V-01 | Phase map table with severity norms (P2/P3 → P0/P1 gradient) + inference rule. No verification of the 60% threshold. | **PARTIAL** |
| V-02 | Same phase map + migration context column. No percentage verification. | **PARTIAL** |
| V-03 | No phase map table. Theme declaration has phase distribution but zero severity guidance per phase. | **FAIL** |
| V-04 | Phase map with migration context column. No verification. | **PARTIAL** |
| V-05 | Phase map + STEP 2B body anchor templates embedding phase character ("We've been running this for two months and now something serious broke") + STEP 9 Pass 2 explicitly: "Phase 1 tickets at P2/P3: ___ of ___ (required: >= 60%)" and "At least 1 Phase 3 ticket at P0/P1: Y/N". | **PASS** |

---

### Per-Variation Scorecards

#### V-01 — Phrasing Register (Character-Embodiment)

| Tier | Criteria | Pass | Score |
|------|----------|------|-------|
| Essential | C-01 C-02 C-03 C-04 C-05 | 5/5 | 60.0 |
| Recommended | C-06 C-07 C-08 | 3/3 | 30.0 |
| Aspirational | C-09 PASS C-10 FAIL C-11 PARTIAL C-12 PASS C-13 PARTIAL | 3.0/5 | 6.0 |
| **Composite** | | | **96.0** |

Golden: YES. C-10 and C-11(partial) / C-13(partial) are the ceiling.

---

#### V-02 — Inertia Framing (Status-Quo Competitor)

| Tier | Criteria | Pass | Score |
|------|----------|------|-------|
| Essential | C-01 C-02 C-03 C-04 C-05 | 5/5 | 60.0 |
| Recommended | C-06 C-07 C-08 | 3/3 | 30.0 |
| Aspirational | C-09 FAIL C-10 FAIL C-11 PARTIAL C-12 PASS C-13 PARTIAL | 2.0/5 | 4.0 |
| **Composite** | | | **94.0** |

Golden: YES. Migration-specific failure classes surface (C-09 benefit lost by not declaring themes). C-09 is the biggest gap vs V-01.

---

#### V-03 — Theme-First Generation

| Tier | Criteria | Pass | Score |
|------|----------|------|-------|
| Essential | C-01 C-02 C-03 C-04 C-05 | 5/5 | 60.0 |
| Recommended | C-06 C-07 C-08 | 3/3 | 30.0 |
| Aspirational | C-09 PASS C-10 FAIL C-11 PARTIAL C-12 FAIL C-13 FAIL | 1.5/5 | 3.0 |
| **Composite** | | | **93.0** |

Golden: YES. Theme-first wins C-09 by construction, but trading the phase map structure costs C-12 and C-13. Net loss vs V-01 despite theme innovation.

**Key insight:** Theme organization alone is not sufficient — phase-severity structure must travel with themes, not be replaced by them.

---

#### V-04 — Character-Embodiment + Inertia Framing

| Tier | Criteria | Pass | Score |
|------|----------|------|-------|
| Essential | C-01 C-02 C-03 C-04 C-05 | 5/5 | 60.0 |
| Recommended | C-06 C-07 C-08 | 3/3 | 30.0 |
| Aspirational | C-09 PASS C-10 FAIL C-11 PARTIAL C-12 PASS C-13 PARTIAL | 3.0/5 | 6.0 |
| **Composite** | | | **96.0** |

Golden: YES. Matches V-01 score. The V-01+V-02 combination adds migration depth without structural regressions. Ceiling is C-10 (no resolution path) and verification gaps (C-11, C-13 partial).

---

#### V-05 — Full Synthesis (Golden Candidate)

| Tier | Criteria | Pass | Score |
|------|----------|------|-------|
| Essential | C-01 C-02 C-03 C-04 C-05 | 5/5 | 60.0 |
| Recommended | C-06 C-07 C-08 | 3/3 | 30.0 |
| Aspirational | C-09 PASS C-10 PASS C-11 PASS C-12 PASS C-13 PASS | 5/5 | 10.0 |
| **Composite** | | | **100.0** |

Golden: YES, full. Every aspirational criterion has structural enforcement, not just guidance. The dual-pass verification step is the critical differentiator: it converts criterion compliance from best-effort into self-correcting.

*Note: 100 is the structural upper bound assuming model follows all prompt steps. Execution against actual topics would score 93–100 range depending on model compliance with the verification passes.*

---

### Ranking

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|--------------|-------|
| 1 | V-05 | 100.0 | YES | All 13 criteria pass structurally |
| 2 | V-01 | 96.0 | YES | Character-embodiment alone; loses C-10 |
| 2 | V-04 | 96.0 | YES | V-01+V-02 combined; same ceiling as V-01 |
| 4 | V-02 | 94.0 | YES | Inertia framing; loses C-09 (no theme declaration) |
| 5 | V-03 | 93.0 | YES | Theme-first wins C-09 but loses C-12+C-13 |

---

### Excellence Signals from V-05

**Signal 1 — Phase body anchor sentence scaffold (STEP 2B)**
Per-phase per-role sentence templates ("I set up {topic} and now my monitoring is..." / "We've been running {topic} in prod for N weeks and we just saw...") reduce the generation surface for each ticket body. This drives phase-calibrated language more reliably than severity norm columns alone. V-01 through V-04 say "assign severity from the norm column" — V-05 shows the model what the voice sounds like at each phase.

**Signal 2 — Dual-pass verification with explicit numeric thresholds**
STEP 9 Pass 2 is the key structural innovation: "Phase 1 tickets at P2/P3: ___ of ___ (required: >= 60%)" and "Broken T-NN refs in gap entries: ___ (required: 0)". These turn aspirational criteria into self-correcting prompts — the model must verify compliance before submitting. None of the single-axis variations have this; all leave C-11 and C-13 as best-effort.

**Signal 3 — Resolution path as a required three-field table**
STEP 7B with required fields (triage owner / root cause category / resolution type) makes C-10 structurally guaranteed. The pattern from R1 was: "prose guidance for aspirational = best-effort = inconsistent." V-05's pattern: "required structured table with named fields = compliance by construction."

**Signal 4 — Theme declaration and phase map coexist (V-03 lesson)**
V-03 showed that theme-first organization wins C-09 but costs C-12 and C-13 because removing the phase map removes severity guidance. V-05 carries both: STEP 3 theme declaration AND phase map in STEP 2 with STEP 2B anchors. The synthesis doesn't replace structure — it adds another organizational layer on top of it.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase body anchor sentence scaffolds per phase per role reduce ticket body generation entropy more reliably than severity norm columns alone", "Dual-pass verification with explicit numeric thresholds (required: 0 broken refs, >= 60% phase P2/P3) converts aspirational criteria from best-effort guidance into self-correcting constraints", "Resolution path as a required three-field table (triage owner, root cause category, resolution type) makes C-10 structurally guaranteed rather than prose-dependent best-effort", "Theme declaration and phase map must coexist — theme-first alone wins C-09 but loses C-12 and C-13 when it replaces the phase severity structure rather than adding to it"]}
```
