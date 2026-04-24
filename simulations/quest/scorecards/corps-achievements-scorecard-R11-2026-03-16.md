## Scorecard — corps-achievements Variate R11 (Rubric v10)

---

### Scoring Key

| Symbol | Meaning |
|--------|---------|
| PASS | Criterion clearly satisfied |
| PARTIAL | Criterion partially satisfied (0.5 weight) |
| FAIL | Criterion not satisfied |

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/22 × 20)`, PARTIAL = 0.5

---

### Essential Criteria (C-01–C-05) — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 Glob scan gate present | PASS | PASS | PASS | PASS | PASS |
| C-02 Topic coverage gate with every-topic check | PASS | PASS | PASS | PASS | PASS |
| C-03 Team milestones table, 3 named rows | PASS | PASS | PASS | PASS | PASS |
| C-04 Contributor leaderboard section | PASS | PASS | PASS | PASS | PASS |
| C-05 Next actions: ≥3, namespace+topic explicit, unlock named | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 for all variations.**

---

### Recommended Criteria (C-06–C-08) — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Achievement definitions (First Signal, Signal Depth, Full Sweep, Solo Pioneer, Team Topic) | PASS | PASS | PASS | PASS | PASS |
| C-07 Achievements grouped: Earned / Locked as named categories | PASS | PASS | PASS | PASS | PASS |
| C-08 Sprint/date framing present ({{date}} in section headers) | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 20/20 for all variations.**

---

### Aspirational Criteria (C-09–C-30)

#### C-09–C-27: Baseline from v8/v9 (inherited by all five)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-09 "1-away" dedicated table with exact gap and count | PASS | PASS | PASS | PASS | PASS | All have 4-column `Almost There` table |
| C-10 Cross-topic/contributor named insight, distinct from stagnation | PASS | PASS | PASS | PASS | PASS | Team Insight section with Step A–D in all |
| C-11 At least one inline pre-write self-test gate | PASS | PASS | PASS | PASS | PASS | Pre-write confirmations throughout |
| C-12 Anti-inertia format: `[Action] → Unlocks → Breaks [Pattern]` | PASS | PASS | PASS | PASS | PASS | V-05 table equivalent satisfies structure |
| C-13 Insight as titled artifact `**TEAM INSIGHT — [name]:**` | PASS | PASS | PASS | PASS | PASS | Template present in all |
| C-14 Stagnation patterns from named registry, label syntax enforced | PASS | PASS | PASS | PASS | PASS | Registry table + "Do not invent labels" in all |
| C-15 Gate failure names specific instance (topic/contributor/row) | PASS | PASS | PASS | PASS | PASS | `[specific instance]` token in all fail paths |
| C-16 Weighted formula `Signals×1 + Topics×3 + Milestones×5` | PASS | PASS | PASS | PASS | PASS | Formula in all |
| C-17 Semantic pattern labels (SOLO_ISLAND, NAMESPACE_MOAT, etc.) | PASS | PASS | PASS | PASS | PASS | Five semantic labels in registry |
| C-18 1-away table: 4 columns (topic, achievement, gap, exact action) | PASS | PASS | PASS | PASS | PASS | Column headers match specification |
| C-19 Worked example calculation inline for Rank-1 contributor | PASS | PASS | PASS | PASS | PASS | `{S}×1 + {T}×3 + {M}×5 = {total}` in all |
| C-20 Gate labels carry criterion ID references `[C-XX]` | PASS | PASS | PASS | PASS | PASS | All gates carry criterion IDs |
| C-21 Formula gate instructs table correction on mismatch | PASS | PASS | PASS | PASS | PASS | "Corrected: {old}→{new}" instruction in all |
| C-22 Insight gate applies single-topic derivability test (per-topic YES/NO) | PASS | PASS | PASS | PASS | PASS | Step B loop in all insight sections |
| C-23 Multi-condition gates use numbered sub-steps | PASS | PASS | PASS | PASS | PASS | `(1)... (2)...` numbered in all gates |
| C-24 Cross-phase gate explicitly asks whether Phase 2 findings alter Phase 1 output | PASS | PASS | PASS | PASS | PASS | CROSS-PHASE GATE sub-steps (2)–(4) in all |
| C-25 Multi-criterion gate labels enumerate all covered IDs | PASS | PASS | PASS | PASS | PASS | Cluster gates show all IDs; V-05 adds C-30 to leaderboard label |
| C-26 Gate condition verifies that all other gate labels carry criterion IDs (meta-audit) | PASS | PASS | PASS | PASS | PASS | STRUCTURAL AUDIT sub-step (2) in all |
| C-27 Structural audit names each super-gate by full label and exact expected IDs | PASS | PASS | PASS | PASS | PASS | V-01/V-03: 2 super-gates verified; V-02: 3; V-04: 4; V-05: 2 with updated C-30 label |

#### C-28–C-30: New / Redefined in v10

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|---------|
| C-28 First-person ownership syntax "Before I write this section, I confirm [C-28]: …" | PASS | PASS | PASS | PASS | PASS | V-01: 1B+1C; V-02: 1B+ATTRIBUTION gate; V-03: pervasive (1A–3B); V-04: 1A+2A+ATTRIBUTION gate; V-05: 1B+1C |
| C-29 Named correction triad + re-run instruction in all fail paths | PASS | PASS | PASS | PASS | PASS | V-01/V-04: global protocol + labeled `> RETRY: … > END RETRY` blocks; V-02/V-03/V-05: triad format `GATE FAILED [C-XX]: … — CORRECTION: … Re-running this section.` in every fail path; V-05 global protocol adds "Then re-run the affected section" |
| C-30 Pre-write leaderboard gate explicitly prohibits backward-inference from contributor identity | PASS | PASS | **PARTIAL** | PASS | PASS | **V-01**: inline "Attribution integrity check [C-30]" before LEADERBOARD gate, with explicit conditional recovery. **V-02/V-04**: standalone ATTRIBUTION INTEGRITY GATE [C-28/C-30], numbered sub-steps, pass/fail. **V-03**: prohibition embedded in C-28 ownership statement ("I am not inferring backward from contributor identity. [C-30]") — prohibition present but no formal gate condition with recovery mechanics. **V-05**: sub-step (6) in LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-30], explicit census-only constraint |

---

### Aspiration Subtotals

| Variation | Pass | Partial | Fail | Effective | Aspirational Score |
|-----------|------|---------|------|-----------|-------------------|
| V-01 | 22 | 0 | 0 | 22.0/22 | **20.00** |
| V-02 | 22 | 0 | 0 | 22.0/22 | **20.00** |
| V-03 | 21 | 1 | 0 | 21.5/22 | **19.55** |
| V-04 | 22 | 0 | 0 | 22.0/22 | **20.00** |
| V-05 | 22 | 0 | 0 | 22.0/22 | **20.00** |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.00 | 20.00 | 20.00 | **100.0** |
| V-02 | 60.00 | 20.00 | 20.00 | **100.0** |
| V-03 | 60.00 | 20.00 | 19.55 | **99.5** |
| V-04 | 60.00 | 20.00 | 20.00 | **100.0** |
| V-05 | 60.00 | 20.00 | 20.00 | **100.0** |

---

### Rankings

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| T-1 | **V-01** | 100.0 | C-29 as labeled RETRY blocks |
| T-1 | **V-02** | 100.0 | C-30 as standalone ATTRIBUTION INTEGRITY GATE |
| T-1 | **V-04** | 100.0 | Labeled RETRY + standalone gate + stagnation-first |
| T-1 | **V-05** | 100.0 | C-29/C-30 absorbed into super-gate labels, C-27 updated |
| 5 | V-03 | 99.5 | C-28 pervasive first-person ownership |

**V-03 loses the single point on C-30**: its backward-inference prohibition is embedded in a C-28 ownership statement rather than structured as a gate condition with its own recovery path. The statement reads "I am not inferring backward from contributor identity. [C-30]" — the tag is there, but there is no conditional halt+correction instruction if the model detects it is doing exactly that.

---

### Excellence Signals (from top-scoring variations)

**ES-1 — C-30 absorption into cluster label (V-05)**
V-05 merges C-30 into the LEADERBOARD CLUSTER GATE as `[C-16/C-19/C-21/C-30]` and then updates C-27 to verify this new four-ID label. A model that writes the old `[C-16/C-19/C-21]` label produces a wrong-enumeration failure that C-27 detects without any standalone gate proliferation. **Pattern**: integrate new criteria into existing cluster labels and extend C-27's named verification to cover the new label — wrong omission becomes structurally auditable.

**ES-2 — ATTRIBUTION INTEGRITY GATE as dedicated isolation step (V-02, V-04)**
Pulling C-30 into its own named gate `ATTRIBUTION INTEGRITY GATE [C-28/C-30]` with numbered sub-steps and a formal pass/fail prevents the attribution constraint from being swept along by adjacent criteria in a larger cluster. A cluster gate can pass if most sub-steps pass; a dedicated gate cannot. **Pattern**: when a criterion guards the integrity of inputs (not outputs), isolate it in its own gate so no downstream criterion's pass can silently satisfy it.

**ES-3 — Labeled RETRY blocks as observable artifacts (V-01, V-04)**
`> RETRY: [section name]` / `> END RETRY` wrapping makes the re-execution boundary visible in model output — the reader can audit both the failure declaration and the corrected content side by side. An instructed re-run that produces no labeled output can be silently skipped; a labeled block cannot. **Pattern**: when the correction procedure is critical to correctness, make it an observable output artifact, not just an instruction.

**ES-4 — Stagnation-first framing enriches retry context (V-04)**
Phase 0 diagnosis names the dominant pattern before any achievement work runs. When a gate fails later, the pattern annotation "Is this failure predicted by [PATTERN_LABEL]?" connects the correction to known team state. This turns the correction triad from a data-repair event into evidence about the team's actual situation. **Pattern**: running a diagnostic phase before the primary phases provides a grounding frame that makes all downstream corrections interpretable.

**ES-5 — Structural audit expansion to cover v10 additions (V-05)**
Expanding the structural audit label from `[C-20/C-25/C-26/C-27]` to `[C-20/C-25/C-26/C-27/C-28/C-29/C-30]` makes all three v10 additions verifiable by a single self-enforcing audit pass. Specifically: sub-step (4) checks that a "Before I write… I confirm [C-28]" statement exists, sub-step (5) checks that all fail paths used the correction triad, sub-step (6) confirms the LEADERBOARD CLUSTER label contains C-30. **Pattern**: when a new version adds criteria that concern structural properties of the skill itself, audit them in the structural audit gate, not in standalone gates scattered through execution.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Absorb new criteria into existing cluster gate labels and extend C-27 named-verification to the new label — wrong omission becomes a detectable enumeration failure", "Isolate attribution-integrity constraints in a dedicated standalone gate so adjacent criteria passing cannot silently sweep the prohibition", "Wrap re-execution in labeled RETRY/END RETRY blocks to make corrections observable artifacts auditable by the reader", "Run stagnation diagnosis in Phase 0 before achievement work so every downstream retry can be annotated with whether the failure was predicted by the dominant pattern", "Expand the structural audit gate label to include new structural criteria so all v10 additions are self-enforcing without adding standalone gates"]}
```
