# crew-roles — Quest Score, Rubric v6, Round 9

---

## Scoring Summary

| Criterion | Type | V-01 | V-02 |
|-----------|------|------|------|
| C-01 All 5 fields | Essential | PASS | — |
| C-02 Inertia-advocate present | Essential | PASS | — |
| C-03 Correct output path | Essential | PASS | — |
| C-04 Domain specificity | Essential | PASS | — |
| C-05 Minimum 3 roles | Essential | PASS | — |
| C-06 Lens actionability | Recommended | PASS | — |
| C-07 Collaborates_with resolves | Recommended | PASS | — |
| C-08 Perspective diversity | Recommended | PASS | — |
| C-09 Scope gradient | Aspirational | PASS | — |
| C-10 Inertia domain-grounded | Aspirational | PASS | — |
| C-11 Vocabulary-forced-field | Aspirational | PASS | — |
| C-12 Inertia pre-characterization | Aspirational | PASS | — |
| C-13 Registry summary table | Aspirational | PASS | — |
| C-14 Scope-gradient-enforcement | Aspirational | PASS | — |
| C-15 Verification-gate-phase | Aspirational | PASS | — |
| C-16 Vocabulary-linked inertia Q&A | Aspirational | PASS | — |
| C-17 Pre-write scope audit | Aspirational | PASS | — |
| C-18 Vocabulary check in verification gate | Aspirational | PASS | — |
| C-19 Inertia frame Q-slot template | Aspirational | PASS | — |
| C-20 Q-domain-aligned vocabulary distribution | Aspirational | PASS | — |
| C-21 Bucketed vocabulary extraction | Aspirational | PASS | — |
| C-22 Domain-alignment audit table at Phase 2 exit | Aspirational | PASS | — |
| C-23 Frame Fill dedicated phase | Aspirational | PASS | — |
| C-24 Audit-table full re-evaluation after replacement | Aspirational | PASS | — |
| C-25 Frame-slot source citation in Frame Fill output | Aspirational | PASS | — |

**V-02 note:** V-02 is truncated. The skill text ends after the schema-format premise ("All required output artifacts are defined below as named schemas") with no schemas present. V-02 cannot be evaluated — no structural evidence exists for any criterion. It is excluded from ranking.

---

## V-01 — Detailed Evidence

**Variation axis:** Named phases with explicit ENTRY / EXIT / BLOCK conditions

**Essential (50/50)**

- **C-01** — Phase 5 template lists all five fields explicitly (`name`, `orientation`, `expertise`, `scope`, `collaborates_with`). PASS.
- **C-02** — Phase 5 inertia-advocate requirements mandate `orientation.frame` = filled frame string from Phase 3, and `orientation.verify` must reference ≥ 2 Q dimensions. PASS.
- **C-03** — Phase 5 and Delivery Confirmation both state `.craft/roles/{area}/`. PASS.
- **C-04** — Phase 5 requires `expertise.relevance` to reference at least one Phase 1 vocabulary term; vocabulary is domain-extracted, anchoring relevance to the specific input domain. PASS.
- **C-05** — Phase 5 states "Write at least 3 role files." PASS.

**Recommended (30/30)**

- **C-06** — Phase 5 template explicitly encodes `verify: [question ending with ?]` and `simplify: [imperative phrase]`. PASS.
- **C-07** — Phase 6 Check 1 orphan-reference detection: "For every `collaborates_with` value: confirm a matching file exists in the registry. Any unresolved reference blocks the gate." PASS.
- **C-08** — Phase 5 states "Roles must span at least 3 distinct categories. No category monopoly." PASS.

**Aspirational (17/17 → 17/17 × 10 = 10.0)**

- **C-09** — Phase 4 pre-write scope audit requires ≥ 2 distinct scope values; Phase 6 Check 2 enforces it post-write. PASS.
- **C-10** — Phase 2 Q1 demands "specific system, tool, or approach"; Phase 5 requires `expertise.relevance` to name the specific current system from Phase 2. PASS.
- **C-11** — Phase 1 vocabulary extraction + Phase 6 Check 3 vocabulary coverage check create the structural wire. PASS.
- **C-12** — Phase 2 Q1/Q2/Q3 answers explicitly address current system, migration cost, user habit; Phase 5 requires verify to reference ≥ 2 of 3 dimensions. PASS.
- **C-13** — Phase 6 Check 1 produces Role | Frame excerpt | Scope | Collaborates With table. PASS.
- **C-14** — Phase 4 BLOCK: "if all planned roles share one scope value, revise 1–2 planned roles to introduce a second distinct value" before any role file is written. PASS.
- **C-15** — Phase 6 is a single named gate ("CREW-ROLES VERIFICATION") with three checks evaluated simultaneously: "Gate exit condition: Check 1 PASS + Check 2 PASS + Check 3 PASS, evaluated simultaneously." PASS.
- **C-16** — Phase 2 requires each Q answer to draw from its designated bucket (Q1 → Bucket A, Q2 → Bucket B, Q3 → Bucket C), wiring C-11 vocabulary extraction into the Q answers structurally. PASS.
- **C-17** — Phase 4 is explicitly "PRE-WRITE SCOPE AUDIT" with BLOCK before any role file. PASS.
- **C-18** — Phase 6 Check 3 explicitly verifies vocabulary coverage; gate cannot PASS without it. PASS.
- **C-19** — Phase 3 template: `"Adopting this approach means abandoning [Q1: current system] — at a cost of [Q2: migration cost] — for users whose workflow depends on [Q3: user habit]."` Named Q-slots present. PASS.
- **C-20** — Phase 2 bucket assignments (Q1→A, Q2→B, Q3→C) + audit table YES/NO rows enforce domain-aligned distribution; same-term reuse across buckets is caught at the gate. PASS.
- **C-21** — Phase 1 produces three named buckets: Current-System Terms (A), Migration-Cost Terms (B), User-Habit Terms (C); each term assigned during extraction. PASS.
- **C-22** — Phase 2 audit table (Q | Term Used | Expected Bucket | Match YES/NO) is a structural artifact in the output; any NO row triggers replacement; BLOCK on Phase 3 entry until all YES. PASS.
- **C-23** — Phase 3 "FRAME FILL" is a standalone named phase with ENTRY, EXIT, and BLOCK conditions; frame string produced before any role file is written. PASS.
- **C-24** — Phase 2 re-evaluation protocol: "After any replacement, re-evaluate starting from Q1. Do not re-score only the replaced row. The gate condition is all three rows simultaneously YES in a single evaluation pass." Full restart enforced, not incremental. PASS.
- **C-25** — Phase 3 explicitly requires slot citations: `Q1 slot ← Phase 2 Q1: [verbatim answer]` / `Q2 slot ← Phase 2 Q2: [verbatim answer]` / `Q3 slot ← Phase 2 Q3: [verbatim answer]`. Slot-binding check is a blocking error before continuing. PASS.

---

## Composite Scores

| Variation | Essential (50) | Recommended (30) | Aspirational (10) | Total |
|-----------|---------------|------------------|-------------------|-------|
| V-01 | 50 | 30 | 10.0 | **90.0** |
| V-02 | — (incomplete) | — | — | **N/A** |

**Rank:** V-01 (only scoreable variation, 90.0)

---

## Excellence Signals — V-01

**ES-1: Artifact-chained phase entry makes phase skipping structurally impossible**

Every phase's ENTRY condition names the specific artifact produced by the prior phase's EXIT condition (Phase 2 ENTRY: "Phase 1 vocabulary table complete"; Phase 3 ENTRY: "Phase 2 audit table complete with YES/YES/YES"; Phase 4 ENTRY: "Frame Fill complete"; Phase 5 ENTRY: "Pre-write scope audit passed"). A skipped phase leaves the ENTRY condition referencing a nonexistent artifact — the gap is structural, not instructional. This goes beyond the individual phase gates captured in C-22, C-23, C-24, C-25; it is the mechanism that connects them into a chain.

**ES-2: Three-slot frame fill with Q3 source citation extends C-25 to the user-habit dimension**

C-25 specifies slot-source binding for Q1 and Q2 verbatim answers. V-01 explicitly extends this to Q3: `Q3 slot ← Phase 2 Q3: [verbatim answer]` appears in Phase 3's citation block, and the slot-binding check covers all three slots before Phase 4 entry. The user-habit dimension (the third slot, most commonly under-specified in frame generation) is now structurally verified alongside current-system and migration-cost.

---

```json
{"top_score": 90.0, "all_essential_pass": true, "new_patterns": ["Artifact-chained phase entry: each phase ENTRY condition names the exit artifact from the prior phase, making phase skipping a structural gap rather than silent non-compliance — connects individual phase gates (C-22 through C-25) into a dependency chain where each phase cannot begin without evidence the prior phase completed", "Three-slot frame fill source citation: the slot-binding check in Frame Fill explicitly covers Q3 (user-habit slot) in addition to Q1 and Q2, extending C-25's two-slot verification model to all three frame dimensions before role writing begins"]}
```
