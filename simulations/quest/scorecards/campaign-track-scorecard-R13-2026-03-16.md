## Quest Scorecard — campaign-track / Round 13

### Scoring Framework

| Category | Per-criterion | Criteria count | Max pts |
|----------|--------------|---------------|---------|
| Essential | 10 | 5 (C-01–C-05) | 50 |
| Recommended | 5 | 3 (C-06–C-08) | 15 |
| Aspirational (baseline) | 3 | 24 (C-09–C-37) | 72 |
| Aspirational (new R13) | 3 | 2 (C-38–C-39) | 6 |
| **Max** | | **34** | **143** |

All five variations inherit R12 V-05 baseline. Essential + recommended + 24 baseline aspirationals = **137 pts** before new criteria. Differences isolated to C-38 and C-39 only.

---

### Per-Variation Rubric Evaluation

#### Essential Criteria (C-01–C-05) — same across all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Four-phase structure (R→P→S→N) | PASS | PASS | PASS | PASS | PASS |
| C-02 Artifact-per-phase discipline | PASS | PASS | PASS | PASS | PASS |
| C-03 Nine-namespace coverage table | PASS | PASS | PASS | PASS | PASS |
| C-04 Readiness verdict from enumerated set | PASS | PASS | PASS | PASS | PASS |
| C-05 Narrative verdict with evidence | PASS | PASS | PASS | PASS | PASS |

All essential: **50 pts** all variations.

#### Recommended Criteria (C-06–C-08) — same across all variations

| Criterion | All |
|-----------|-----|
| C-06 Artifact write paths | PASS |
| C-07 Coverage ratio + labeled readiness | PASS |
| C-08 Cross-namespace signal balance | PASS |

Recommended: **15 pts** all variations.

#### Aspirational Baseline (C-09–C-37) — all PASS, inherited from R12 V-05

| Criterion | Evidence (shared) | All |
|-----------|-------------------|-----|
| C-09 Echo integration | echoes list with ["NONE"] fallback | PASS |
| C-10 Dual-session delta | Session Delta Contract + delta.md | PASS |
| C-11 Role-gated phases | Registrar/Planner/Analyst/Narrator | PASS |
| C-12 Explicit progression gates | "SHALL NOT proceed until" GATE per phase | PASS |
| C-13 Empty-state as named section | Dedicated "First Invocation" section, per-phase | PASS |
| C-14 Per-role prohibition lists | Exactly 5 numbered forbidden actions per role | PASS |
| C-15 Typed output contracts per phase | All 4 phases have typed contracts | PASS |
| C-16 Terminal completion checklist | 27-item TERMINAL section, targeted re-run language | PASS |
| C-17–C-21 (no text) | Inherited from R12 V-05 | PASS |
| C-22–C-37 (not shown) | Inherited from R12 V-05, incl. C-36/C-37 closed last round | PASS |

Aspirational baseline: **72 pts** all variations.

**Running baseline total: 137 pts.**

---

### New Criteria: C-38 and C-39

#### C-38 — Ambiguity failure mode framing at Phase Boundary Summary

> Phase 4 obligation consequence appears at Phase Boundary Summary as ambiguity failure mode: "downstream systems cannot distinguish an interrupted campaign from a completed one — both states produce `verdict_after = NOT YET REACHED`." Two or more structurally distinct sites. Stale-value framing alone does not satisfy.

**V-01**
Phase Boundary Summary obligation bullet: *"downstream systems cannot distinguish an interrupted campaign from a completed one -- both states produce `verdict_after = NOT YET REACHED` in delta.md. A campaign that ran Phase 4 and skipped the write is indistinguishable from a campaign that never reached Phase 4."* Phase 4 header repeats same framing. Empty-state mentions "ambiguity failure mode activates." Three surfaces.
Result: **PASS** (+3)

**V-02**
Phase 4 obligation header: *"`verdict_after` in `delta.md` becomes stale -- the 'NOT YET REACHED' placeholder persists indefinitely."* Stale-value framing only. Phase Boundary Summary obligation entry also uses stale-value framing only: *"cannot resolve the campaign's readiness state."* Explicit "cannot distinguish interrupted from completed / both states produce NOT YET REACHED" absent.
Result: **FAIL** (0)

**V-03**
`#### Transition Obligation` subsection: *"downstream systems cannot distinguish an interrupted campaign from a completed one -- both states produce `verdict_after = NOT YET REACHED`."* Phase 4 header: *"the Transition Obligation at the Phase 3->4 boundary is violated -- downstream systems cannot distinguish."* Empty-state: *"Transition Obligation is violated and the ambiguity failure mode activates."* Three surfaces, two structural locations.
Result: **PASS** (+3)

**V-04**
Phase Boundary Summary **Phase 4 Obligation** bold entry: *"downstream systems cannot distinguish an interrupted campaign from a completed one -- both states produce `verdict_after = NOT YET REACHED` in delta.md. A campaign that ran Phase 4 and skipped the write is indistinguishable from a campaign that never reached Phase 4. The ambiguity is unresolvable from delta.md alone."* Phase 4 header repeats. Empty-state: "ambiguity failure mode activates." Three surfaces.
Result: **PASS** (+3)

**V-05**
`#### Transition Obligation` subsection: *"downstream systems cannot distinguish an interrupted campaign from a completed one -- both states produce `verdict_after = NOT YET REACHED` in delta.md. A campaign that ran Phase 4 and skipped the story.md write is indistinguishable from a campaign that never reached Phase 4 at all. The ambiguity is unresolvable from the delta.md artifact alone."* Phase 4 header: same framing plus explicit cross-reference *"The Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated."* Empty-state: *"without it, downstream systems cannot distinguish an interrupted first session from a completed one."* Three surfaces + explicit back-reference to Phase Boundary Summary by name.
Result: **PASS+** (credit: +3; excellence signal logged for C-40 candidate)

---

#### C-39 — Receiving Scope as independent structural site

> Phase Boundary Summary addresses receiving scope (what Phase 4 does NOT receive as inputs) independently of cascading scope (what a Phase 3 Step B re-run updates). Two orthogonal structural sites with named independence claim.

**V-01**
Phase Boundary Summary Phase 3->4: receiving scope present as bullet point: *"Phase 4 does NOT receive namespace counts... Receiving them as inputs would imply Phase 4 could revise them."* Phase 4 active-role header also mentions it briefly. No named "Receiving Scope" subsection. No explicit independence claim distinguishing it from cascade scope. Single prose argument, no independence assertion.
Result: **FAIL** (0)

**V-02**
Named **Receiving Scope** bold subsection in Phase Boundary Summary. Explicit independence claim: *"This receiving scope exclusion is independent of the Cascade Rule's cascade scope. The cascade argument applies when Phase 3 Step B is re-run after Phase 4 has completed. The receiving scope argument applies at Phase 4 entry, before Phase 4 runs. The two arguments address the same Phase 3/4 boundary from orthogonal directions."* Phase 4 active-role header reinforces: *"Receiving scope: Phase 4 does NOT receive namespace counts."* Two distinct structural sites.
Result: **PASS** (+3)

**V-03**
Named `#### Cascade Scope` and `#### Receiving Scope` subsection headers. Explicit orthogonality statement: *"These two scope dimensions are orthogonal. Cascade scope applies at re-run time after Phase 4 has completed. Receiving scope applies at Phase 4 entry. They address the same Phase 3/4 boundary from different temporal positions: one governs what flows back on error recovery; the other governs what flows forward on first execution."* Phase 4 active-role header: *"Receiving scope (from Phase Boundary Summary)."* Phase 3 header references both scopes by name. Section-level naming makes the two-dimensional coverage auditable without cross-reference.
Result: **PASS** (+3)

**V-04**
Named **Receiving Scope** bold subsection in Phase Boundary Summary. Independence claim: *"This receiving scope exclusion is independent of the Cascade Rule's cascade scope. The cascade argument applies when Phase 3 Step B is re-run after Phase 4 has completed. The receiving scope argument applies at Phase 4 entry, before Phase 4 runs. Two orthogonal directions at the same boundary."* Phase 4 active-role header: *"Receiving scope: Phase 4 does NOT receive namespace counts."* Two structural sites. Orthogonality framing explicit.
Result: **PASS** (+3)

**V-05**
Named `#### Receiving Scope` subsection header. Explicit independence label in the section opener: *"Independent of Cascade Scope: cascade scope is a re-run concern; receiving scope is an entry concern. They address the same Phase 3/4 boundary from orthogonal temporal positions."* Full receiving scope detail. Phase 4 active-role header: *"Receiving scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT receive namespace counts."* Two named structural sites, each with a distinct framing (entry vs. re-run), independence assertion made as the section's first sentence.
Result: **PASS+** (credit: +3; excellence signal logged for C-40 candidate)

---

### Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 to C-05 (essential) | 5 × 10 | 50 | 50 | 50 | 50 | 50 |
| C-06 to C-08 (recommended) | 3 × 5 | 15 | 15 | 15 | 15 | 15 |
| C-09 to C-37 (aspirational baseline, 24 criteria) | 24 × 3 | 72 | 72 | 72 | 72 | 72 |
| **Baseline subtotal** | | **137** | **137** | **137** | **137** | **137** |
| C-38 | 3 | +3 | 0 | +3 | +3 | +3 |
| C-39 | 3 | 0 | +3 | +3 | +3 | +3 |
| **TOTAL** | | **140** | **140** | **143** | **143** | **143** |

**All essential criteria: PASS for all variations.**

---

### Ranking

| Rank | Variation | Score | Rationale |
|------|-----------|-------|-----------|
| 1 | **V-05** | 143 | Full triptych (Cascade Scope / Receiving Scope / Transition Obligation) + Phase 4 back-references to both subsections by name. Maximum C-38 + C-39 density with PASS+ signals on both. Explicit cross-reference from Phase 4 active-role header to Phase Boundary Summary sections creates auditable obligation traceability. C-40 candidate surfaces on both new criteria. |
| 2 | **V-04** | 143 | C-38 + C-39 combined without structural naming overhead. Named Receiving Scope subsection (C-39) + ambiguity failure mode (C-38) with three scoring surfaces each. Two-site independence argument for C-39. Marginally behind V-05 because the Cascade Scope is not named at section level — the triptych orthogonality is stated in text but not made auditable by headers. |
| 3 | **V-03** | 143 | Triptych structure achieves structural auditability (header-level naming) and passes both C-38 and C-39. Ranked below V-04 because the ambiguity framing in the Transition Obligation subsection is slightly less dense than V-04/V-05 (missing the "A campaign that ran Phase 4... is indistinguishable from a campaign that never reached Phase 4" reinforcement sentence present in V-05). |
| 4 | **V-01** | 140 | C-38 PASS with three surfaces; C-39 FAIL (no named subsection, no independence claim). |
| 4 | **V-02** | 140 | C-39 PASS with named subsection and explicit independence claim; C-38 FAIL (stale-value framing only). |

**Confirmed leaderboard order**: V-05 > V-04 > V-03 > V-01 = V-02. Matches predicted order.

---

### Excellence Signals from V-05

**Pattern 1 — Triptych boundary taxonomy with temporal axis labeling**
The Phase 3->4 boundary in V-05 uses three named subsection headers: `#### Cascade Scope`, `#### Receiving Scope`, `#### Transition Obligation`. Each header governs a distinct dimension of the same boundary. The independence claim is elevated from a sentence inside a subsection (V-02/V-04) to the **section opener** of the Receiving Scope header: *"Independent of Cascade Scope: cascade scope is a re-run concern; receiving scope is an entry concern."* This makes the orthogonality auditable at the structural level (a reader scanning headers sees three distinct concerns) without requiring cross-reference reading. V-03 had this structure too, but V-05 adds more explicit density. Candidate criterion: **C-40 — Phase 3->4 boundary taxonomy: three named subsections with temporal-axis independence labels**.

**Pattern 2 — Phase 4 header double back-reference to Phase Boundary Summary subsections**
V-05's Phase 4 active-role header contains two explicit back-references by subsection name:
- *"Receiving scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT receive namespace counts"*
- *"The Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated"*

This creates a traceable link from the obligation assertion site (Phase 4 header, where the Narrator reads its constraints) back to the obligation declaration site (Phase Boundary Summary, where the contract is defined). No prior variation created this bidirectional traceability. V-03 had a single back-reference (*"Receiving scope (from Phase Boundary Summary)"*); V-05 adds the Transition Obligation cross-reference. Candidate criterion: **C-41 — Phase 4 active-role header cross-references Phase Boundary Summary subsections by name, creating traceable obligation links between declaration site and assertion site**.

---

```json
{"top_score": 143, "all_essential_pass": true, "new_patterns": ["Triptych Phase 3->4 boundary taxonomy: three named subsections (Cascade Scope, Receiving Scope, Transition Obligation) with temporal-axis independence labels (re-run concern vs. entry concern) making orthogonality auditable at section-header level without cross-reference reading", "Phase 4 active-role header double back-reference: cross-references both Receiving Scope and Transition Obligation subsections from Phase Boundary Summary by name, creating bidirectional obligation traceability between declaration site and assertion site"]}
```
