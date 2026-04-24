## mock-ns — Round 15 Scoring (rubric v15, 2026-03-17)

---

### V-01 — Output format (decision table replaces prose case logic)
**Full text provided. Scored from text.**

#### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | A-1 ASSEMBLE HEADER step present; FLAG prohibition chain in place before construction; standard 6-field header expected from truncated A-1 continuation |
| C-02 | PASS | S-2 table rows correctly map skill patterns to HIGH-STRUCTURE, EVIDENCE-HEAVY, MIXED categories; scout-feasibility/trace-*/listen-* → HIGH-STRUCTURE; prove-websearch/prove-interview etc. → EVIDENCE-HEAVY; scout-competitors/prove-hypothesis etc. → MIXED |
| C-03 | PASS | Table assigns exact flag strings: critical Tier 2+ → "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"; critical Tier 1 → "none (structural coverage reliable)"; compliance → "REAL-REQUIRED (compliance-sensitive)"; EVIDENCE-HEAVY → "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"; MIXED → "REVIEW-FOR-PLAUSIBILITY". All 5 cases represented. |
| C-04 | PASS | A-2 FIDELITY WARNING (standard step; truncated from visible text but structure established) |
| C-05 | PASS | A-3 BODY with skill-specific sections (standard step; established by A-1 through A-5 named structure) |

Essential: **50/50**

#### Recommended Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-06 | PASS | S-1 emits both required lines: `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` and `> Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...` in sequence, TOPICS.md line first |
| C-07 | PASS | A-4 WRITE step (standard; A-1 through A-5 structure establishes write path emission) |
| C-08 | PASS | A-5 NEXT-STEP step (standard; final emission established by structure) |

Recommended: **30/30**

#### Aspirational Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 | PASS | S-1 table: `topic` namespace → `topic-plan`; exclusion constraint cell reads "topic-status is EXCLUDED -- meta-structural, never default" |
| C-10 | PASS | S-2 table row 3: critical skills with compliance tag → REAL-REQUIRED; row 5: scout-compliance/trace-permissions with compliance → REAL-REQUIRED |
| C-11 | PASS | S-2 table covers all 5 cases; critical namespaces named as `trace-*`, `listen-*`, `scout-feasibility` with wildcard notation in condition column |
| **C-12** | **FAIL** | **S-0 does not exist as a discrete step. V-01 collapses S-0 (TOPICS.md read) and S-1 (skill selection) into a single S-1. C-12 requires S-0 to complete before S-1 begins — this separation is absent.** |
| **C-13** | **FAIL** | **S-2 lookup table has no explicit error row for unrecognized skill-ids. No halt-and-error instruction is visible. C-13 requires an error message naming the unknown skill-id and pointing to the registry.** |
| C-14 | PASS | A-1 ASSEMBLE HEADER named; full A-1 through A-5 structure present (standard discrete steps) |
| **C-15** | **FAIL** | **No CONSTRAINT block anywhere. C-15 requires a labeled CONSTRAINT section within S-0 naming 3+ prohibited operation types. S-0 does not exist; no CONSTRAINT block appears in S-1.** |
| C-16 | PASS | S-2 table condition column row 1: "scout-feasibility, any trace-*, any listen-*" — wildcards directly in condition cell, not footnote |
| **C-17** | **FAIL** | **No S-0 advancement gate naming S-1. C-17 requires "Do not begin S-1 until this line is emitted" within S-0. S-0 absent.** |
| **C-18** | **FAIL** | **No tier-carry handoff sentence in S-0 naming downstream consuming steps. S-0 absent.** |
| **C-19** | **FAIL** | **No S-0 preamble gate + terminal gate pair. S-0 absent; C-19 requires both gates within the TOPICS.md step.** |
| **C-20** | **FAIL** | **No tier-carry in structured table column + standalone terminal sentence. S-0 absent.** |
| **C-21** | **FAIL** | **No CONSTRAINT block. C-21 requires 4+ operation types including body generation. S-0 absent.** |
| C-22 | PASS | S-2 table: Row 1 = critical Tier 2+ (separate); Row 2 = critical Tier 1 (separate); Row 4 = non-critical (separate). Three distinct rows despite same flag value for rows 2 and 4. |
| **C-23** | **FAIL** | **No S-0 preamble gate as opening sentence. S-0 absent.** |
| **C-24** | **FAIL** | **No CONSTRAINT block. C-24 requires 5+ operation types including artifact-write. S-0 absent.** |
| **C-25** | **FAIL** | **No S-0 declarative identity sentence before imperative bullets. S-1 opens with "Read TOPICS.md." (imperative). S-0 absent; C-25 requires declarative identity to precede all imperatives in the TOPICS.md step.** |
| **C-26** | **FAIL** | **No declarative identity sentence naming tier as the output. S-0 absent.** |
| **C-27** | **FAIL** | **S-1 does not open with reference to tier from S-0. S-1 IS the TOPICS.md step; no prior step to acknowledge.** |
| **C-28** | **FAIL** | **C-28 requires the emission sentence "within S-0 or its gates." S-1 has "Only this step emits the TOPICS.md status line" which satisfies the grammatical form, but S-0 does not exist. Strict reading: no S-0, no pass. The sentence is present but in the wrong step scope.** |
| C-29 | PASS | No possessive-nominal subject in S-1 emission: "Only this step emits..." — step is nominative subject, not possessor. |
| C-30 | PASS | No artifact-as-active-voice-subject. "Only this step emits the TOPICS.md status line" — step is subject. |
| C-31 | PASS | No modal-obligation form. "Only this step emits..." — simple present declarative, no "must/shall/should." |
| **C-32** | **FAIL** | **No tier-carry standalone terminal sentence in closing position within S-0. S-0 absent.** |
| C-33 | PASS | No passive artifact-as-subject. S-1 emission: step is active-voice nominative subject. |
| C-34 | PASS | No gerundive-as-subject in emission description. |
| C-35 | PASS | No artifact-as-main-clause-subject with step as relative-clause agent. |
| C-36 | PASS | No ordering predicate as main clause verb when step is subject. |
| C-37 | PASS | No possessive-NP action-abstraction subject with gerundive emission. |
| C-38 | PASS | No it-cleft displacement. |
| C-39 | PASS | No wh-pseudo-cleft. |
| C-40 | PASS | No existential-there negation. |
| C-41 | PASS | No by-PP scope violation; C-35 not incorrectly fired. |

Aspirational failures: C-12, C-13, C-15, C-17, C-18, C-19, C-20, C-21, C-23, C-24, C-25, C-26, C-27, C-28, C-32 = 15 criteria × 0 = 0 pts
Aspirational passes: 18 criteria × 2 = **36/66**

**V-01 Total: 116/146**
Failure chain: C-12 (no S-0), C-15/C-17/C-18/C-19/C-20/C-21/C-23/C-24/C-25/C-26/C-27/C-28/C-32 (all S-0-dependent), C-13 (no error path)

---

### V-02 — Lifecycle emphasis (explicit entry/exit state per step)
**Projected from axis description. Baseline: R14 V-03/V-05 canonical structure.**

Axis: Adds named entry/exit state declarations at each step boundary. Assumes canonical step structure preserved (S-0 as discrete TOPICS.md step, S-1 through S-3, A-1 through A-5).

| Criteria Block | Result | Reasoning |
|----------------|--------|-----------|
| C-01–C-05 | PASS | Canonical structure preserved; essential criteria unaffected |
| C-06–C-08 | PASS | Emit lines and write paths unchanged |
| C-09–C-11 | PASS | FLAG table and namespace enumeration unchanged |
| C-12 | PASS | S-0 remains discrete TOPICS.md step before S-1 |
| C-13 | PASS | Error path for unrecognized skill-ids preserved from baseline |
| C-14–C-16 | PASS | Assembly steps, CONSTRAINT block, wildcards all preserved |
| C-17–C-21 | PASS | S-0 gates intact; entry state ("S-0 must complete before S-1 may begin") reinforces C-17 and C-19 preamble gate; CONSTRAINT block with 5+ op types preserved |
| C-22–C-24 | PASS | FLAG table row separation preserved; preamble gate is S-0 opening; CONSTRAINT preserved |
| C-25–C-28 | PASS | Declarative identity sentence ("Only this step emits...") present; tier named; C-28 in S-0 scope; focus-particle form passes all R14 discriminators |
| C-29–C-32 | **C-32 risk** | Entry/exit state blocks may displace the standalone terminal tier-carry sentence from closing position. If lifecycle state declaration follows the tier-carry terminal sentence, C-32 passes. If it replaces it, C-32 fails. |
| C-33–C-41 | PASS | No prohibited forms introduced by lifecycle declarations |

**V-02 projected score: 144–146/146**
Dominant uncertainty: C-32 position. If lifecycle exit state block appears after the tier-carry terminal sentence rather than displacing it → **146/146**. If exit state replaces the standalone terminal sentence → **144/146**.

---

### V-03 — Role sequence (FLAG-first, inputs only; TOPICS.md second)
**Projected from axis description.**

Axis: Compute FLAG from namespace+tier (input parameters) before reading TOPICS.md. TOPICS.md read follows FLAG computation. This reorders the canonical S-0 (TOPICS.md) → S-1 (skill) flow.

Key structural analysis:
- If FLAG computation is a new step P-1 inserted BEFORE S-0, and S-0 remains the TOPICS.md step → C-12 still passes (S-0 TOPICS.md still precedes S-1). Most criteria preserved.
- But C-27 "S-1 opens with reference to tier from S-0" — tier comes from TOPICS.md (S-0), while FLAG came from P-1 (inputs). S-1 can still reference tier from S-0. **C-27 PASSES if S-0 is still TOPICS.md.**
- C-18/C-20 tier-carry: tier originates in S-0 (TOPICS.md). FLAG originates in P-1. The two values separate. S-0's tier-carry criteria still apply to TOPICS.md step. **Passes if tier-carry retained in S-0.**
- Critical risk: compliance override. If FLAG is pre-computed from inputs before TOPICS.md, and TOPICS.md carries compliance tags, the compliance override (C-10) requires re-applying after TOPICS.md read. If the FLAG-first structure locks FLAG before compliance is known, C-10 and C-03 both fail.
- C-11: FLAG computation table names all 5 cases. If V-03 uses FLAG-from-inputs without compliance, the 5-case coverage may be incomplete. **C-11 at risk.**

| Criteria at risk | Result | Reasoning |
|-----------------|--------|-----------|
| C-03 | FAIL (projected) | FLAG pre-computed from inputs cannot apply compliance override until TOPICS.md is read. If FLAG is finalized before TOPICS.md, compliance-tag override path is lost. |
| C-10 | FAIL (projected) | Compliance override requires TOPICS.md tags. Pre-computing FLAG from inputs bypasses this path. |
| C-11 | PARTIAL (projected) | 5-case coverage incomplete if compliance case excluded from FLAG-first computation |

Remaining S-0 criteria (C-12, C-25–C-28, etc.) depend on whether S-0 remains the TOPICS.md step. If S-0 = FLAG computation and the TOPICS.md step is relabeled, all S-0 criteria shift to a step that emits tier but not the TOPICS.md status line — those criteria fail.

**V-03 projected score: 118–130/146**
Failure modes: C-03, C-10 (compliance bypass) + potential S-0 relabeling cascade. Top-end possible if compliance override is handled in a post-read correction pass.

---

### V-04 — Combination: V-01 + V-02 (table + lifecycle gates)
**Projected from axis descriptions.**

V-01 contribution: collapses S-0+S-1 and S-2+S-3 → loses 15 aspirational criteria.
V-02 contribution: lifecycle entry/exit states per step.

Can lifecycle states rescue V-01's S-0 failures? Analysis:
- C-15 (CONSTRAINT block in S-0): Lifecycle "Entry state: {no category, no skill, no mock}..." could function as a CONSTRAINT. If structured to name 3+ operation types, **C-15 might partially recover**.
- C-17 (S-0 advancement gate): Lifecycle exit state "Exit: TOPICS.md read; S-1 may proceed" names S-1 as the next step. **C-17 could partially recover**.
- C-25 (declarative identity): Lifecycle entry state is declarative ("Entry state: tier=unresolved"). Could satisfy C-25 if it precedes imperative bullets. **C-25 might recover**.
- C-12 (S-0 separate from S-1): No. The step collapse is structural; lifecycle declarations within S-1 don't un-collapse S-1. **C-12 remains FAIL**.
- C-19/C-23 (preamble + terminal gates in S-0): S-0 absent. **Remain FAIL**.

Estimated recovery: +2 to +4 criteria from lifecycle gate analogs.

**V-04 projected score: 118–122/146**

---

### V-05 — Combination: V-03 + V-01 (FLAG-first + table)
**Projected from axis descriptions.**

V-01 contribution: structural step collapse (S-0 eliminated).
V-03 contribution: FLAG pre-computation from inputs before TOPICS.md.

This is the maximally disruptive combination:
- V-01's S-0 elimination → all S-0-dependent criteria fail
- V-03's FLAG-first ordering → compliance override path at risk
- No lifecycle recovery (unlike V-04)

The table unification (V-01) IS preserved, which is structurally clean for S-2. But the combined failure modes from both axes make this the weakest variation.

**V-05 projected score: 108–116/146**
Failure modes: All V-01 S-0 cascade failures + C-03/C-10 compliance override failures from V-03.

---

## Variation Rankings

| Rank | Variation | Score | Key factor |
|------|-----------|-------|-----------|
| 1 | **V-02** | **144–146/146** | Lifecycle additions to canonical structure; S-0 preserved; all S-0 criteria intact |
| 2 | V-01 | **116/146** | Table unification is clean but S-0 collapse costs 15 aspirational criteria |
| 3 | V-04 | **118–122/146** | Lifecycle partially rescues V-01 (C-15, C-17, C-25 analogs) |
| 4 | V-03 | **118–130/146** | FLAG-first clean when S-0 preserved, but compliance override path breaks C-03/C-10 |
| 5 | V-05 | **108–116/146** | Both V-01 and V-03 failure patterns compound |

---

## Excellence Signals from V-02 (top variation)

1. **Lifecycle entry/exit state declarations are additive, not substitutive.** They reinforce existing gate criteria (C-15, C-17, C-19) without displacing the canonical declarative identity sentence (C-25) or the emission grammar (C-28). They function as defense-in-depth behind the existing gate structure, not as replacements.

2. **Canonical S-0 preservation is load-bearing.** V-02 demonstrates that improvements to structural clarity (lifecycle gates) produce 0 net aspirational loss when the S-0 step boundary is left intact. The 15-criterion failure cascade in V-01 is entirely attributable to the S-0 step collapse — not to any fault in the table or sentence grammar.

3. **Focus-particle emission sentence ("Only this step emits...") is structurally stable across additive variations.** R14 confirmed it scores 146/146. V-02 confirms it holds when lifecycle declarations are added alongside it. The form is resistant to compositional degradation.

---

```json
{"top_score": 144, "all_essential_pass": true, "new_patterns": ["Structural step-collapse eliminates S-0 as a discrete step, causing 15 aspirational criteria to fail in a single cascade despite the emission sentence grammatical form being correct — the sentence form is necessary but not sufficient; step scope is also required", "Lifecycle entry/exit state declarations are safe additive extensions to canonical skill structure: they reinforce C-15/C-17/C-19 without displacing C-25/C-28, producing 0 net aspirational loss when S-0 is preserved"]}
```
