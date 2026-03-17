## Quest Score — corps-achievements R10

**Rubric**: v9 (v8 criteria C-01–C-27 as baseline; v9 redefines C-28 as first-person owner confirmation syntax — old C-28 enumeration-in-pass-record is now absorbed baseline behavior)

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 Achievement-census-first | 60 | 20 | 19.0 (C-28 FAIL) | **99** |
| V-02 Per-topic scorecard blocks | 60 | 20 | 19.0 (C-28 FAIL) | **99** |
| V-03 C-28 testbed | 60 | 20 | 20.0 | **100** |
| V-04 Census-first + C-28 | 60 | 20 | 20.0 | **100** |
| V-05 Per-topic blocks + C-28 + retry | 60 | 20 | 20.0 | **100** |

**Declared top: V-05** — three mutually-reinforcing innovations. The retry loop is the highest-value new structural pattern in R10.

---

### Key Findings

**C-12 clean (R9 lesson applied)**: R9 V-02 got PARTIAL because dense-table format replaced arrow syntax in the ACTIONS section. R10 V-02 and V-05 scope per-topic blocks to the ACHIEVEMENT section only — the actions section retains arrow format with sub-step enforcement. All C-12: PASS.

**C-28 split is the only discriminator**: V-01 and V-02 use third-person procedural gates ("Does X match Y?"); V-03/V-04/V-05 use first-person owner gates ("Before I write this section, I confirm [C-XX]: …"). The failure signature is different — the commitment form makes a silent gate skip an agent commitment violation, not just a missed checklist item.

---

### Excellence Signals

**ES-1 → candidate C-29** (V-05): Gate-failure retry loop — `"GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section."` Converts violation from terminal event to named correction triad: name → fix → re-verify.

**ES-2 → candidate C-30** (V-01/V-04): Achievement-derived attribution constraint — gate condition explicitly prohibits inferring achievements backward from contributor identity. Phase 1 census runs before leaderboard; Phase 2 pre-write gate confirms contributor scores derive FROM Phase 1 evidence. Closes a correctness gap C-02 (topic coverage) doesn't address.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Gate-failure retry loop converts gate violation from terminal prohibition to named correction procedure: GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section — provides recovery path that maintains gate semantics without halting execution", "Achievement-derived attribution constraint: phase ordering (census before leaderboard) combined with explicit gate condition prohibiting backward inference from contributor identity to achievement evidence — closes correctness gap not covered by topic-coverage check C-02"]}
```
Variation | Gate sub-step for C-12 | Format template | Verdict |
|-----------|------------------------|-----------------|---------|
| V-01 | Sub-step (3) in ACTIONS CLUSTER GATE: "Each action uses format [Action] → Unlocks [Achievement] → Breaks [Pattern]. [C-12]" | Arrow format in template | **PASS** |
| V-02 | ACTIONS CLUSTER GATE carries C-12 in label; per-topic scorecard blocks apply only to achievement section — actions section retains arrow format; sub-step (3) enforces arrow syntax | Arrow format; per-topic blocks do not affect actions section | **PASS** |
| V-03 | Sub-step (3): "Each action uses format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]" | Arrow format | **PASS** |
| V-04 | Sub-step (3): "Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]" | Arrow format | **PASS** |
| V-05 | Sub-step (3): "Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]" | Arrow format; per-topic blocks do not replace actions section | **PASS** |

R9 lesson applied: R9 V-02 (dense-table) got C-12 PARTIAL because the table format replaced
arrow syntax in the ACTIONS section and no sub-step enforced the format. R10 V-02 and V-05
apply per-topic blocks ONLY to the achievement section — the actions section retains arrow
format with sub-step enforcement. **PASS all**.

#### C-13 Insight formatted as `**TEAM INSIGHT — [descriptive name]:**`

All five: INSIGHT GATE sub-step (1) checks formatting. **PASS all**.

#### C-14 Pattern labels from named registry, label syntax enforced

All five: Stagnation Pattern Registry present; ACTIONS CLUSTER GATE checks registry sourcing.
**PASS all**.

#### C-15 Gate fail messages name the specific instance

All five: fail messages use `— [specific path or topic]`, `— [specific milestone name]`, etc.
V-05 extends this further: the gate-failure retry loop format is "GATE FAILED [C-XX]:
[specific instance] — CORRECTION: [action]. Re-running this section." — maximally specific.
**PASS all**.

#### C-16 Leaderboard uses explicit weighted formula

All five: LEADERBOARD CLUSTER GATE sub-step (1) checks `Score = (Signals×1)+(Topics×3)+(Milestones×5)`.
V-04 adds a novel pre-write gate check: "Before I write this leaderboard, I confirm [C-16]:
all contributor scores are derived from Phase 1 achievement census — not independently
asserted." **PASS all**.

#### C-17 Pattern labels are semantic names

All five: registry defines SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, SHALLOW_POOL,
ORPHAN_TOPIC. **PASS all**.

#### C-18 1-Away callout as structured table with 4 columns

All five: template `| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |`.
**PASS all**.

#### C-19 Worked example calculation for Rank 1 contributor

All five: LEADERBOARD CLUSTER GATE sub-step (2) renders `Score = {S}×1 + {T}×3 + {M}×5 = {total}`.
**PASS all**.

#### C-20 Gate labels carry criterion ID references

All five: every gate label carries at least one [C-XX] reference. **PASS all**.

#### C-21 Reconciliation correction loop after worked example

All five: LEADERBOARD CLUSTER GATE sub-steps (3)–(5) compare total, correct if mismatch,
confirm match. V-05's gate-failure retry loop makes this even more explicit: on mismatch,
the model issues "GATE FAILED [C-21]: Score column shows X, calculation gives Y —
CORRECTION: updating Score column to Y. Re-running this section." **PASS all**.

#### C-22 Derivability test: insight must fail single-topic derivation

All five: INSIGHT GATE Step B applies per-topic derivability elimination; Step C generates
new candidate if any topic yields YES. **PASS all**.

#### C-23 Multi-condition gates use numbered sub-steps

All five: every gate block uses `"(1) … (2) … (3) …"` enumeration. **PASS all**.

#### C-24 Later-phase gate asks whether prior-phase findings alter current output

| Variation | Cross-phase reference | Verdict |
|-----------|----------------------|---------|
| V-01 | Phase 2 (leaderboard) pre-write gate confirms contributor scores derive from Phase 1 achievement census. CROSS-PHASE GATE [C-24] in Phase 4 checks whether Phase 3 milestone gaps surface topics absent from Phase 1. | **PASS** — two cross-phase references |
| V-02 | CROSS-PHASE GATE [C-24] in final phase; Phase 2 leaderboard pre-write gate references Phase 1 scan state. | **PASS** |
| V-03 | CROSS-PHASE GATE [C-24] in final phase; pre-write gates reference prior-phase data. | **PASS** |
| V-04 | CROSS-PHASE GATE [C-24] in final phase; Phase 2 pre-write gate explicitly confirms all contributor scores derived from Phase 1 achievement census (tighter cross-phase reference than any prior variation). | **PASS** — strongest cross-phase binding |
| V-05 | CROSS-PHASE GATE [C-24] in final phase; Phase 2 pre-write gate references Phase 1. | **PASS** |

**PASS all**.

#### C-25 Multi-criterion super-gate labels enumerate all covered criterion IDs

All five: LEADERBOARD CLUSTER GATE [C-16/C-19/C-21] and ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]
enumerate all IDs; sub-step (6) in each gate checks enumeration. V-03/V-04/V-05 structural audit
gate expands to [C-20/C-25/C-26/C-27/C-28] — all 5 IDs enumerated in label. **PASS all**.

#### C-26 Structural audit gate verifies all other gate labels carry criterion IDs

All five: STRUCTURAL AUDIT GATE sub-step (2) audits every gate label in the run.
V-03/V-04/V-05 expand the gate to [C-20/C-25/C-26/C-27/C-28] and add sub-step auditing
C-28 compliance across all pre-write gates. **PASS all**.

#### C-27 Structural audit names each super-gate by full label with exact expected IDs

| Variation | Super-gates named in structural audit | Verdict |
|-----------|--------------------------------------|---------|
| V-01 | LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]; ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20] | **PASS** |
| V-02 | Same two super-gates | **PASS** |
| V-03 | Same two super-gates + STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28] (audits itself by naming expected IDs) | **PASS** |
| V-04 | Same as V-03 | **PASS** |
| V-05 | Same as V-03 | **PASS** |

V-03/V-04/V-05 gain an additional super-gate in the structural audit (the expanded audit gate
itself), increasing the enumeration surface that C-27 verifies. **PASS all**.

#### C-28 (experimental) First-person owner confirmation syntax in all pre-write gates

| Variation | Pre-write gate phrasing | C-28 audit in structural gate | Verdict |
|-----------|------------------------|-------------------------------|---------|
| V-01 | Third-person procedural: "Does the topic count match scan state?" | No C-28 audit; structural gate = [C-20/C-25/C-26/C-27] | **FAIL** |
| V-02 | Third-person procedural | No C-28 audit; structural gate = [C-20/C-25/C-26/C-27] | **FAIL** |
| V-03 | First-person owner: "Before I write this section, I confirm [C-11]: …" across all pre-write gates | Structural audit gate = [C-20/C-25/C-26/C-27/C-28]; sub-step (n) audits C-28 compliance across all pre-write gates; pass confirmation names "First-person confirmations (C-28): [n] pre-write gates verified." | **PASS** |
| V-04 | Same as V-03; Phase 2 leaderboard pre-write gate: "Before I write this leaderboard, I confirm [C-11/C-16]: all contributor scores derive from Phase 1 achievement census." — C-28 syntax binds the model to the achievement-derived attribution guarantee | Same expanded audit gate as V-03 | **PASS** |
| V-05 | Same as V-03; gate-failure retry loop reinforces the ownership framing — "GATE FAILED — CORRECTION — Re-running this section" is structurally consistent with the first-person ownership model | Same expanded audit gate as V-03 | **PASS** |

---

## Composite Scores

```
Formula: (essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/20 × 20)
PARTIAL = 0.5 weight
v9 aspirational pool: C-09–C-27 (19 criteria, baseline) + C-28 experimental (20th, when introduced)
```

| Variation | Essential (60) | Recommended (20) | Aspirational (20) | Total |
|-----------|----------------|------------------|-------------------|-------|
| V-01 Achievement-census-first | 60 | 20 | 19.0 (19/20, C-28 FAIL) | **99.0** |
| V-02 Per-topic scorecard blocks | 60 | 20 | 19.0 (19/20, C-28 FAIL) | **99.0** |
| V-03 C-28 testbed (first-person owner) | 60 | 20 | 20.0 (20/20) | **100.0** |
| V-04 Achievement-census-first + C-28 | 60 | 20 | 20.0 (20/20) | **100.0** |
| V-05 Per-topic blocks + C-28 + retry loop | 60 | 20 | 20.0 (20/20) | **100.0** |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tied) | V-03, V-04, V-05 | 100.0 | C-28 first-person owner syntax PASS |
| 2 (tied) | V-01, V-02 | 99.0 | C-28 FAIL — pre-write gates remain third-person procedural |

**Tiebreak analysis** — among the three 100s:

- **V-05** is architecturally the richest: per-topic scorecard blocks + first-person owner confirmations + gate-failure retry loop. Three innovations. The retry loop is the most novel structural territory in R10 — it converts gate failure from a terminal prohibition into a named correction procedure, providing a recovery path that neither halts execution nor allows silent violation.
- **V-04** introduces achievement-derived attribution as a structural correctness guarantee: Phase 2 leaderboard derives contributor scores FROM Phase 1 achievement census. The Phase 2 pre-write gate explicitly confirms this derivation. This prevents reverse-direction inference (contributor standing → achievements implied but not enumerated). Two innovations, one of which addresses a failure mode not yet covered by any existing criterion.
- **V-03** is the pure C-28 testbed — cleanest isolation of the first-person owner pattern for signal confirmation. Single innovation.

**Declared top variation: V-05** (three mutually-reinforcing innovations; retry loop is the highest-value new structural pattern in R10; per-topic blocks strengthen C-02 compliance beyond what row-in-table format guarantees).

---

## Excellence Signals from R10

### ES-1 — Gate-failure retry loop converts violation from silent risk to named correction

**Pattern**: V-05 embeds explicit retry instructions inside gate fail paths:
`"GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action taken]. Re-running this section."`
The model re-executes the section, applies the correction, then re-runs the gate. This is
distinct from v8/v9 baseline gates which issue halt instructions or correction sub-steps
(e.g., C-21's "correct the Score column before proceeding") — those tell the model what
to fix, but the retry loop tells the model to re-run the gate as a named step.

**Why it's better**: Without a retry instruction, a gate failure has two outcomes: the model
halts (best case) or silently proceeds (worst case). With a retry instruction, the model has
a third named path — correction then re-verification — that maintains gate semantics without
halting execution. C-15 names the failure instance; C-21 instructs the correction; the retry
loop closes the loop by requiring re-verification. Together they form a correction triad
(name → fix → verify) rather than a flag-and-stop binary.

**Candidate criterion**: C-29 — "When a gate fails, the gate body includes an explicit
retry instruction that names the correction action and instructs the model to re-run the gate
after applying it — converting gate failure from a terminal event to a named correction loop;
a gate that names the failure instance (C-15) but provides no retry path does not satisfy
this criterion."

**Seen in**: V-05 exclusively.

### ES-2 — Achievement-derived attribution: Phase 2 leaderboard derives from Phase 1 evidence

**Pattern**: V-01 and V-04 invert the role sequence (achievement census runs before leaderboard),
and V-01's COMPUTE GATE adds a 4th condition not present in prior rounds: "(4) No topic's
achievement is inferred from contributor identity — all evidence cites signal counts,
namespaces, or file paths from scan state." V-04 carries this into the Phase 2 pre-write gate:
"Before I write this leaderboard, I confirm [C-16]: all contributor scores are derived from
Phase 1 achievement census."

**Why it's better**: C-02 checks that every topic appears in the achievement output. This new
constraint checks the reverse — that achievements are not inferred backward from contributor
identity (e.g., "Contributor A is Rank 1, therefore they must have earned Full Sweep"). The
achievement census runs first precisely to prevent this: contributor scores are computed
FROM verified achievement evidence, not the other way around. This closes a correctness gap
that no existing criterion explicitly addresses.

**Candidate criterion**: C-30 — "When the skill includes both a per-topic achievement section
and a contributor attribution section, at least one gate explicitly verifies that contributor
scores are computed from achievement evidence — not inferred from contributor identity or
prior-round ranking; a gate that confirms topic coverage (C-02) but does not verify the
attribution direction does not satisfy this criterion."

**Seen in**: V-01 (COMPUTE GATE condition 4); V-04 (Phase 2 pre-write gate + full integration
with C-28 ownership syntax).

---

## Key Observation: C-28 Converts Pre-Write Gates from Checklists to Ownership Commitments

The cleanest structural distinction between V-01/V-02 (99) and V-03/V-04/V-05 (100) is
syntactic: "Does the topic count match scan state?" is an external question the model answers;
"Before I write this section, I confirm [C-11]: all topic counts derive from scan state"
is a commitment the model makes before proceeding. The information content is identical; the
accountability model is different. The commitment form binds the model as the agent responsible
for the confirmation — a silent skip becomes an agent commitment violation, not a missed
checklist item. This is why C-28 is worth promoting to a scored criterion: the gate content
doesn't change, but the syntactic form changes the failure signature.

V-04 surfaces a secondary effect of this: when the Phase 2 pre-write gate says "I confirm
all contributor scores derive from Phase 1 achievement census," the first-person form makes
the cross-phase derivation obligation explicit AND auditable. The structural audit gate checks
that this confirmation was made. The old third-person form ("Are scores derived from Phase 1?")
would not appear as a named commitment in the audit.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Gate-failure retry loop converts gate violation from terminal prohibition to named correction procedure: GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section — provides recovery path that maintains gate semantics without halting execution", "Achievement-derived attribution constraint: phase ordering (census before leaderboard) combined with explicit gate condition prohibiting backward inference from contributor identity to achievement evidence — closes correctness gap not covered by topic-coverage check C-02"]}
```
