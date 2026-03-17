## listen-support — Round 3 Scoring (rubric v3, 15 criteria)

**Baseline:** R2 V-05 (composite 96.0, C-01 through C-13 all PASS)
**R3 objective:** Close C-14 (phase-anchored body voice) and C-15 (pre-generation constraint declaration)

---

### Scoring framework (v3)

| Tier | Max pts | Notes |
|------|---------|-------|
| Essential C-01–C-05 | 60 | 12 pts each; all must pass for golden |
| Recommended C-06–C-08 | 30 | 10 pts each |
| Aspirational C-09–C-15 | 10 | pass_count / 7 * 10; PARTIAL = 0.5 |

All R3 variations inherit the full R2 V-05 foundation, confirmed by the Fixed Changes table. C-01 through C-13 carry over as PASS for every variation. The only open question is C-14 and C-15.

---

### C-14 mechanism analysis (per variation)

**C-14 pass condition:** 3+ early-phase bodies contain discovery/onboarding phrases in body text; 1+ late-phase body contains operational/reliability phrases in body text — not in metadata.

| Variation | Mechanism | Assessment | Verdict |
|-----------|-----------|------------|---------|
| V-01 | Per-ticket vocabulary commitment table in STEP 2B: model selects opening phrase from phase-gated pool and records it; STEP 5 TABLE CHECK includes "All Phase 1 tickets have committed discovery phrase: Y/N"; STEP 9 Pass 2 counts bodies with committed phrases | Structural guarantee — the committed phrase IS the body text evidence. Pre-flight check and TABLE CHECK make failure visible before submission. Pass by construction. | **PASS** |
| V-02 | No per-ticket commitment. STEP 1 body register column has example phrases ("I'm trying to set up", "just started using"); STEP 6 instructs "Phase 1: discovery/onboarding vocabulary required"; VERIFICATION MANIFEST row checks body count post-generation | Instruction-based. The vocab examples and STEP 6 instructions guide vocabulary but no per-ticket structural enforcement. A conformant output would satisfy C-14, but the mechanism is softer — evidence is in body text only if model follows instructions, not if it commits in advance. | **PARTIAL** |
| V-03 | Role-phase vocabulary matrix: each cell declares exact register for role × phase (SRE/Phase-1: "I set up {topic} and now my monitoring is..."; C-xx/Phase-1: "I just switched from [old approach]..."; SRE/Phase-3: "We've been running {topic} in prod for [N] weeks..."). STEP 6 body instruction: "Begin each body with vocabulary from the STEP 2 matrix cell for this role-phase combination." | Structural guarantee. The matrix cell is the mandatory opener; Phase 1 cells contain discovery language, Phase 3 cells contain operational language. SRE-first generation order also ensures Phase 1 SRE bodies open with setup vocabulary. Pass by construction, though vocabulary is role-specific rather than drawn from a shared phase pool. | **PASS** |
| V-04 | Inherits V-01 vocabulary commitment table (STEP 2B). Same mechanism: committed phrase per ticket, pre-flight check, TABLE CHECK vocabulary lines. | Structural guarantee, same as V-01. | **PASS** |
| V-05 | Inherits V-01 vocabulary commitment table + R2 V-05 STEP 2B role-phase anchor templates. STEP 2B explicitly states: "Two inputs for every ticket: (1) the anchor template from the role-phase table below as sentence scaffold; (2) a committed opening phrase from the phase vocabulary pool, recorded before writing the body." VERIFICATION MANIFEST row "Phase 1 bodies with discovery/onboarding vocab" counts the evidence. | Dual mechanism: role-phase anchor template provides role-appropriate structure; committed phrase from phase pool provides phase-appropriate vocabulary. Both appear in body text. Strongest C-14 enforcement in the set. | **PASS** |

---

### C-15 mechanism analysis (per variation)

**C-15 pass condition:** Pre-ticket block naming 2+ structural targets; post-ticket verification block with at least one numeric actual vs. required comparison — both visible.

| Variation | Pre-ticket block | Post-ticket block | Assessment | Verdict |
|-----------|-----------------|-------------------|------------|---------|
| V-01 | STEP 1 Phase Distribution Target: 4 declared targets (Phase 1/2/3 counts, total). STEP 3A cross-matrix with 3 constraints. Structurally present but distributed across two labeled sections. | STEP 9 Pass 2: "Phase 1: declared ___ / actual ___ MATCH/MISMATCH"; "Phase 1 tickets at P2/P3: ___ of ___ (required: >= 60%) PASS/FAIL"; C-14 check lines with counts. Numeric comparisons present. | Letter of C-15 is technically met: STEP 1 names 2+ structural targets; STEP 9 Pass 2 has numeric declared/actual comparisons. However, declarations are distributed across STEP 1 and STEP 3A (not a single labeled block), and STEP 9 is a fill-in checklist rather than a table with Required/Actual/Status columns. The post-ticket structure is present but not a clearly delineated "verification block" — it's step 9 of 9, not a standalone section. | **PARTIAL** |
| V-02 | CONSTRAINT MANIFEST: First section in the output, labeled header, 12-row table with "Structural target / Required / Your committed value" columns. Cannot be generated without completing it. | VERIFICATION MANIFEST: Last section after gap analysis, 17-row table with "Structural target / Required / Actual / Status" columns. Every row is a numeric comparison; "If any row shows FAIL: revise before submitting." | Both blocks are structural output landmarks by design. The CONSTRAINT MANIFEST cannot be mistaken for anything other than a pre-ticket declaration; the VERIFICATION MANIFEST enforces numeric comparison by column structure. Pass by form. | **PASS** |
| V-03 | STEP 1 Constraint Declaration: Single labeled block with 7 explicitly named targets (total, Phase 1/2/3, P0 ceiling, high-vol ceiling, distinct personas). More comprehensive than V-01's STEP 1. | STEP 9 Pass 2: Same structure as V-01 — "Phase distribution: Phase 1 declared ___ / actual ___"; "P0 count: ceiling ___ / actual ___ PASS/FAIL"; numeric percentage checks. | Same structural position as V-01. STEP 1 is a single named block pre-ticket with 7 targets (exceeds requirement). STEP 9 has numeric actual vs. required comparisons. But STEP 9 is still a fill-in-the-blank checklist rather than a standalone verification block, and the two sections are distributed steps in a 9-step process rather than named manifest sections. Variation summary also notes "partial C-15." | **PARTIAL** |
| V-04 | Inherits V-02 CONSTRAINT MANIFEST table. | Inherits V-02 VERIFICATION MANIFEST table. | Structural guarantee, same as V-02. | **PASS** |
| V-05 | Inherits V-02 CONSTRAINT MANIFEST table (12 structural targets). STEP 1 phase distribution target block also present as confirmation. | Inherits V-02 VERIFICATION MANIFEST table (17 rows, each with Required/Actual/Status numeric comparisons). Explicitly states: "Every row is a numeric actual vs. required comparison." | Strongest C-15 enforcement. CONSTRAINT MANIFEST names 12 targets (far exceeds requirement of 2+); VERIFICATION MANIFEST has 17 numeric comparisons (far exceeds requirement of 1+). Pass with maximum margin. | **PASS** |

---

### Per-variation scorecard

**Inherited from R2 V-05 (all variations):**
C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PASS (all essential) | C-06 PASS, C-07 PASS, C-08 PASS (all recommended) | C-09 PASS (theme declaration STEP 3), C-10 PASS (STEP 7B resolution paths), C-11 PASS (dual-pass verification), C-12 PASS (STEP 3A constraint 2), C-13 PASS (VERIFICATION MANIFEST rows 12-13 / STEP 9 phase-severity checks)

---

#### V-01 — Lifecycle Emphasis (Vocabulary Pre-Commitment)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Ticket inventory present | PASS | Inherited |
| C-02 | Persona attribution per ticket | PASS | Inherited |
| C-03 | Sample ticket body in persona voice | PASS | Inherited; STEP 4 PERFORMANCE MODE Declaration reinforced |
| C-04 | Gap analysis produced | PASS | Inherited |
| C-05 | Volume/severity distribution | PASS | Inherited |
| C-06 | Ticket count in useful range | PASS | Inherited; STEP 1 total target >= 6 and <= 12 |
| C-07 | Cross-persona coverage | PASS | Inherited; STEP 3A minimum constraints |
| C-08 | Gap actionability | PASS | Inherited; STEP 8 artifact specification required |
| C-09 | Ticket clustering and themes | PASS | Inherited; STEP 3 Theme Declaration |
| C-10 | Ticket lifecycle and resolution | PASS | Inherited; STEP 7B Resolution Paths |
| C-11 | Multi-stage structural integrity | PASS | Inherited; dual-pass verification + TABLE CHECK |
| C-12 | Role-phase compound coverage | PASS | Inherited; STEP 3A Constraint 2 |
| C-13 | Phase-calibrated severity | PASS | Inherited; STEP 9 Pass 2 phase-severity checks |
| C-14 | Phase-anchored body voice | **PASS** | Vocabulary commitment table in STEP 2B: per-ticket committed phrase from phase pool required before body writing; body must begin with committed phrase. STEP 5 TABLE CHECK verifies vocabulary phrase presence. Structural guarantee. |
| C-15 | Pre-generation constraint declaration | **PARTIAL** | STEP 1 names 4 phase distribution targets (satisfies "2+ structural targets"). STEP 9 Pass 2 has numeric declared/actual comparisons. Letter technically met but declarations distributed across STEP 1 + STEP 3A; post-ticket checks are fill-in checklist steps, not a single named verification block. Variation summary notes "C-15 partially implied." |

**Essential gate: PASS (all 5 essential pass)**

```
Essential:     5/5 = 1.00 → 1.00 × 60 = 60.0
Recommended:   3/3 = 1.00 → 1.00 × 30 = 30.0
Aspirational:  (6 + 0.5) / 7 × 10 = 9.3
Composite:     99.3
```

---

#### V-02 — Output Format (Constraint Manifest + Verification Manifest Tables)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Ticket inventory present | PASS | Inherited |
| C-02 | Persona attribution per ticket | PASS | Inherited |
| C-03 | Sample ticket body in persona voice | PASS | Inherited |
| C-04 | Gap analysis produced | PASS | Inherited |
| C-05 | Volume/severity distribution | PASS | Inherited |
| C-06 | Ticket count in useful range | PASS | Inherited |
| C-07 | Cross-persona coverage | PASS | Inherited |
| C-08 | Gap actionability | PASS | Inherited |
| C-09 | Ticket clustering and themes | PASS | Inherited |
| C-10 | Ticket lifecycle and resolution | PASS | Inherited |
| C-11 | Multi-stage structural integrity | PASS | Inherited; VERIFICATION MANIFEST explicitly strengthens zero broken-ref enforcement |
| C-12 | Role-phase compound coverage | PASS | Inherited |
| C-13 | Phase-calibrated severity | PASS | Inherited; VERIFICATION MANIFEST rows 12-13 check phase-severity distribution |
| C-14 | Phase-anchored body voice | **PARTIAL** | STEP 1 body register column provides example discovery/operational phrases; STEP 6 mandates "Phase 1: discovery/onboarding vocabulary required"; CONSTRAINT MANIFEST commits to >= 3 Phase 1 bodies with discovery vocab; VERIFICATION MANIFEST row checks post-generation. However, no per-ticket committed phrase — enforcement is instructional, not structural. Bodies will likely satisfy C-14 but without the body-text guarantee of a committed phrase. |
| C-15 | Pre-generation constraint declaration | **PASS** | CONSTRAINT MANIFEST: first output section, 12-row table naming structural targets, cannot be skipped. VERIFICATION MANIFEST: final output section, 17-row table with Required/Actual/Status columns for every structural property. Pass by form — two manifest tables are structural output landmarks. |

**Essential gate: PASS**

```
Essential:     5/5 = 1.00 → 60.0
Recommended:   3/3 = 1.00 → 30.0
Aspirational:  (6 + 0.5) / 7 × 10 = 9.3
Composite:     99.3
```

---

#### V-03 — Role Sequence (Role-Phase Vocabulary Matrix)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Ticket inventory present | PASS | Inherited |
| C-02 | Persona attribution per ticket | PASS | Inherited |
| C-03 | Sample ticket body in persona voice | PASS | Inherited; role-phase matrix provides role-specific openers |
| C-04 | Gap analysis produced | PASS | Inherited |
| C-05 | Volume/severity distribution | PASS | Inherited |
| C-06 | Ticket count in useful range | PASS | Inherited |
| C-07 | Cross-persona coverage | PASS | Inherited; SRE-first generation order enforces role presence |
| C-08 | Gap actionability | PASS | Inherited |
| C-09 | Ticket clustering and themes | PASS | Inherited |
| C-10 | Ticket lifecycle and resolution | PASS | Inherited |
| C-11 | Multi-stage structural integrity | PASS | Inherited |
| C-12 | Role-phase compound coverage | PASS | Inherited + reinforced: role-phase matrix with SRE-first generation order explicitly distributes role tickets across phases |
| C-13 | Phase-calibrated severity | PASS | Inherited |
| C-14 | Phase-anchored body voice | **PASS** | Role-phase vocabulary matrix cells contain phase-keyed vocabulary: Phase 1 SRE "I set up {topic} and now my monitoring is..." / Phase 1 Support "I keep seeing when customers first try to..." / Phase 1 C-xx "I just switched from [old approach]..." all contain discovery language. Phase 3 SRE "We've been running {topic} in production for [N] weeks..." contains operational language. STEP 6 mandates "Begin each body with vocabulary from the STEP 2 matrix cell." Structural guarantee. |
| C-15 | Pre-generation constraint declaration | **PARTIAL** | STEP 1 Constraint Declaration: single labeled block, 7 named targets (most comprehensive pre-ticket declaration outside manifest format). STEP 9 Pass 2: numeric "ceiling ___ / actual ___" and percentage comparisons. Letter of C-15 is met. However: constraints are still distributed across STEP 1 + STEP 3 cross-matrix (separate step); STEP 9 is a numbered process step, not a standalone named verification block. Variation summary notes "partial C-15." |

**Essential gate: PASS**

```
Essential:     5/5 = 1.00 → 60.0
Recommended:   3/3 = 1.00 → 30.0
Aspirational:  (6 + 0.5) / 7 × 10 = 9.3
Composite:     99.3
```

---

#### V-04 — Combined: Lifecycle Vocabulary Pre-Commitment + Constraint Manifest Format

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-13 | All inherited | PASS | R2 V-05 baseline |
| C-14 | Phase-anchored body voice | **PASS** | Inherits V-01 vocabulary commitment table: per-ticket committed phrase from phase pool required before body writing. STEP 5 TABLE CHECK vocabulary lines verify. VERIFICATION MANIFEST vocab row counts post-generation. Dual enforcement: instructional (body register column) + structural (commitment table). |
| C-15 | Pre-generation constraint declaration | **PASS** | Inherits V-02 manifest tables: CONSTRAINT MANIFEST (12 structural targets) + VERIFICATION MANIFEST (17 rows with Required/Actual/Status). Structural landmarks by form; cannot be satisfied silently. |

**Essential gate: PASS**

```
Essential:     5/5 = 1.00 → 60.0
Recommended:   3/3 = 1.00 → 30.0
Aspirational:  7/7 × 10 = 10.0
Composite:     100.0
```

---

#### V-05 — Full Synthesis: R2 V-05 + Vocabulary Pre-Commitment + Manifest Tables

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-13 | All inherited | PASS | R2 V-05 baseline — full structural foundation retained |
| C-14 | Phase-anchored body voice | **PASS** | Dual mechanism (unique to V-05): (1) Role-phase anchor templates from STEP 2B provide role-appropriate sentence scaffolds with phase-keyed openers; (2) Per-ticket committed phrase from phase vocabulary pool recorded before body writing — body must begin with committed phrase. VERIFICATION MANIFEST row "Phase 1 bodies with discovery/onboarding vocab >= 3" provides post-generation count. The committed phrase appears in body text by construction; counting it is trivial. Strongest C-14 enforcement in set. |
| C-15 | Pre-generation constraint declaration | **PASS** | CONSTRAINT MANIFEST: first output section, 12 named structural targets including C-14 vocabulary rows. STEP 1 phase distribution target provides redundant confirmation. VERIFICATION MANIFEST: final output section, 17 rows each with Required/Actual/Status columns, explicitly captioned "Every row is a numeric actual vs. required comparison." Far exceeds minimum thresholds (2+ targets, 1+ numeric comparison). Pass with maximum margin. |

**Essential gate: PASS**

```
Essential:     5/5 = 1.00 → 60.0
Recommended:   3/3 = 1.00 → 30.0
Aspirational:  7/7 × 10 = 10.0
Composite:     100.0
```

---

### Summary Table

| Variation | C-14 | C-15 | Essential | Recommended | Aspirational | **Composite** |
|-----------|------|------|-----------|-------------|-------------|--------------|
| V-01 | PASS | PARTIAL | 60.0 | 30.0 | 9.3 | **99.3** |
| V-02 | PARTIAL | PASS | 60.0 | 30.0 | 9.3 | **99.3** |
| V-03 | PASS | PARTIAL | 60.0 | 30.0 | 9.3 | **99.3** |
| V-04 | PASS | PASS | 60.0 | 30.0 | 10.0 | **100.0** |
| V-05 | PASS | PASS | 60.0 | 30.0 | 10.0 | **100.0** |

**Ranking:** V-04 = V-05 (100) > V-01 = V-02 = V-03 (99.3)

---

### Excellence Signals

**From V-05 (golden candidate):**

**Signal 1 — Pre-commitment makes vocabulary evidence structural, not stylistic.**
The vocabulary commitment table converts a generation instruction ("use discovery language") into a verifiable prediction. The model writes the committed phrase before writing the body; the committed phrase then appears in the body text by construction. C-14 cannot fail silently: the evidence is traceable from commitment table to body. Any auditor can verify C-14 by checking that each Phase 1 body begins with a phrase from the commitment table row for that ticket.

**Signal 2 — Dual vocabulary inputs compound without interference.**
V-05 STEP 2B provides two orthogonal inputs: a role-phase anchor template (role register) and a phase vocabulary pool committed phrase (phase register). The anchor template guides role-appropriate elaboration; the committed phrase guarantees phase-appropriate opening. A SRE/Phase-1 body gets both the SRE discovery register ("I set up... and now my monitoring") and the Phase 1 vocabulary signal ("I'm trying to set up for the first time"). Neither mechanism undermines the other.

**Signal 3 — Manifest tables make constraint auditability a structural output property.**
By placing the CONSTRAINT MANIFEST as the first section and VERIFICATION MANIFEST as the last section, V-05 makes constraint satisfaction observable without inspecting ticket fields. The Required/Actual/Status column structure means every row is a self-contained numeric comparison. An evaluator applying C-15 does not need to count tickets — the count is in the VERIFICATION MANIFEST. This is auditability by form.

**Signal 4 — The vocabulary commitment row in the VERIFICATION MANIFEST bridges C-14 and C-15.**
The VERIFICATION MANIFEST row "Phase 1 bodies with discovery/onboarding vocab: >= 3 / actual: ___ / PASS" references the bodies written from committed phrases. The commitment table (C-14 mechanism) and the verification manifest row (C-15 mechanism) form a closed loop: commitment → body → count → verification. Both criteria are satisfied by the same artifact chain.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-ticket vocabulary pre-commitment table: recording committed opening phrase before body writing makes phase-contextual vocabulary a structural guarantee rather than a stylistic instruction — committed phrase is simultaneously generation constraint and C-14 body text evidence, auditable without inspecting body content", "manifest table format for constraint declaration and verification: CONSTRAINT MANIFEST pre-ticket and VERIFICATION MANIFEST post-ticket with Required/Actual/Status columns create output section landmarks that satisfy C-15 by form — auditability is structural, not inspectional, and the two blocks form a closed loop with the vocabulary commitment mechanism"]}
```
