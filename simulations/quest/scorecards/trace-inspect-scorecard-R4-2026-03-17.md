Now I have everything needed. Let me score all five R4 variations against the v3 rubric (C-01 through C-14).

---

# Quest Score — trace-inspect, Round 4

**Rubric**: v3 (C-01 through C-14)
**Entry state**: R2 baseline — C-01 through C-13 all PASS at V-05 level; C-14 new in v3.
**Scoring formula**: (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/6 × 10)

---

## Per-Variation Evaluation

### V-01 — Output Format (table-first, field-complete)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four phases structurally present; Phase 1 binding tables with Schema 1 + Schema 2 fields; Phase 2 relay tables; Phase 3 sub-steps 3a→3b→3c→3d; Phase 4 amendment table |
| C-02 | PASS | Artifact write section with path and section-confirmation table required after all relays |
| C-03 | PASS | Locked schema table at top, explicit "any value outside these sets is a structural error" constraint; relay tables enforce SA/SG/EG/QO per field |
| C-04 | PASS | Gate table in Step 3c records PASS/FAIL for each of G-1, G-2, G-3 individually |
| C-05 | PASS | Step 3d classification rules table (R-1/R-2/R-3) in priority order; verdict classification required |
| C-06 | PASS | SA-TO-SG promotion table required for every SA gap; post-promotion inventory table required |
| C-07 | PASS | Relay table structure mandates all required fields including Schema 2 compliance row with source list and YES/NO conformance |
| C-08 | PASS | Findings table requires minimum 3 rows, 2 distinct Source types, Action distinct from Finding |
| C-09 | PASS | VC ledger in Phase 5 with "specific values, counts, named events — not 'as expected'" requirement per row |
| C-10 | PASS | Each sub-step closes with "Step Xa complete. Step Xb is valid to begin"; transition at Step 3c embedded in gate-clearance summary then echoed in closing sentence |
| C-11 | PASS | Mandatory gate-clearance table after Step 3c (before Step 3d); Phase 4 entry gate-clearance table — both required locations covered |
| C-12 | PASS | Remediation table (Gate/Failure reason/Remediation action/Post-remediation result) if any FAIL; explicit "C-12 exemption applies" notice if all gates pass on first evaluation |
| C-13 | PASS | Named-artifact prerequisite check tables open Steps 3a, 3b, 3c, 3d with Result + Named referent columns; bare YES without referent structurally prevented by table format |
| C-14 | PASS | Phase 4 header explicitly: "**Phase-entry gate-clearance summary** (must reflect post-remediation states, **not** initial states)" — constraint is embedded in the section header at the exact point of failure risk |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6
**Composite**: 60 + 30 + (6/6 × 10) = **100**

---

### V-02 — Phrasing Register (direct imperative)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All phases present; imperative structure ("write a binding block", "run the lifecycle", "work through sub-steps") forces each phase output |
| C-02 | PASS | "write the artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md`" with section WRITTEN checklist |
| C-03 | PASS | "If you catch yourself using any other value, stop and fix it before you write another line" — self-correction imperative embedded in label constraint block |
| C-04 | PASS | G-1, G-2, G-3 each checked individually with explicit PASS/FAIL instructions |
| C-05 | PASS | Step 3d lists three rules in priority order; "Write which rule fired and what the verdict is" |
| C-06 | PASS | SA-TO-SG promotion block with per-gap decision and "SA remaining: N. SG from promotion: N." summary |
| C-07 | PASS | All relay fields enumerated with imperative instructions; Schema 2 compliance field required |
| C-08 | PASS | Findings table rules: at least 3 rows, 2 different Source values, Action ≠ restatement |
| C-09 | PASS | "Fill in the VC compliance ledger. For each row, say what you actually observed — specific values, counts, named events. Do not write 'as expected.'" |
| C-10 | PASS | Each sub-step closes with "Write: Step Xa complete. Step Xb is valid to begin." — imperative form enforces emission |
| C-11 | PASS | "Now write the gate-clearance summary. This is mandatory: G-1 [result], G-2 [result], G-3 [result]" at Step 3c; Phase 4 entry summary required |
| C-12 | PASS | Four-step remediation: "Say exactly what is wrong / Say exactly what you are changing / Re-check the gate / Write the updated result"; explicit exemption notice required |
| C-13 | PASS | Each sub-step opens with "Before you begin — write this check: Prerequisite: X. Check: YES. Referent: `<path>`"; imperative forces named-artifact form |
| C-14 | PASS | Phase 4: "Use the post-remediation gate states — **not what they were before any fixes**" — direct imperative register makes the constraint unambiguous at the point of action |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6
**Composite**: 60 + 30 + (6/6 × 10) = **100**

---

### V-03 — Lifecycle Emphasis (verbose phase boundaries)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Every phase has ═══ ENTRY ═══ and ═══ CLOSE ═══ ceremonies; structurally impossible to skip a phase without a visible gap in the output |
| C-02 | PASS | Artifact write section with per-section WRITTEN status; Phase 2 close verifies "Artifact sections complete: N of N" |
| C-03 | PASS | Locked schema block at top; PHASE 1 CLOSE explicitly records Schema 1 and Schema 2 coverage distribution |
| C-04 | PASS | G-1, G-2, G-3 evaluated individually with initial results; remediation loop per FAIL; Step 3c Gate-Clearance Summary section |
| C-05 | PASS | Step 3d applies three rules in priority order; Step 3d CLOSE records "Verdict classification: `<class>`. Rule triggered: R-N" |
| C-06 | PASS | SA-TO-SG PROMOTION lifecycle event with per-gap decision block; post-promotion inventory; promoted gaps noted in Stage 2 relay instruction |
| C-07 | PASS | Relay block required fields listed; Schema 2 compliance field present (sources used, conformance YES/NO) |
| C-08 | PASS | Findings table: >= 3 rows, >= 2 distinct Source types, Action must not restate Finding |
| C-09 | PASS | VC ledger: "Observed behavior must name specific values — not 'as expected'" |
| C-10 | PASS | Every sub-step has ═══ CLOSE ═══ section stating: "Step Xa closing: [summary]. Step Xa is complete. Step Xb entry condition is now satisfiable." |
| C-11 | PASS | ═══ STEP 3c GATE-CLEARANCE SUMMARY ═══ section (explicit header, all three gates, composite step-entry verdict); Phase 4 ENTRY includes gate-clearance table labeled "post-remediation" |
| C-12 | PASS | "Gate `<X>` FAIL — remediation:" block with Failure / Action taken / Re-evaluation sub-fields; "C-12 exemption applies" notice required if all gates pass first try |
| C-13 | PASS | Each sub-step has ═══ ENTRY ═══ ceremony with prerequisite check: "Check: YES. Named referent: `<artifact path>`" — named-referent form is explicitly required |
| C-14 | PASS | Two explicit C-14 enforcement points: (1) Step 3c gate-clearance summary header: "This summary must reflect final (post-remediation) states... not the initial FAIL"; (2) Phase 4 ENTRY: "use post-remediation gate states; if remediation occurred in Phase 3, these states must **match the post-remediation states documented there** — not the initial states" — strongest cross-reference chain of all five variations |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6
**Composite**: 60 + 30 + (6/6 × 10) = **100**

---

### V-04 — Role Sequence (EG-first) + Output Format (prose-led, inline tables)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four phases present; Phase 2 runs EG Stage 1, SA Stage 1, PROMOTION, Stage 2 — Stage 1 is split into two sub-stages but the top-level Schema 3 sequence (Stage 1 → PROMOTION → Stage 2) is preserved |
| C-02 | PASS | Artifact write section with per-section WRITTEN confirmation after all relays |
| C-03 | PASS | "Label constraint (enforced throughout): Severity is P1, P2, or P3. Source is SA, SG, EG, or QO. No other values." — inline constraint block |
| C-04 | PASS | G-1, G-2, G-3 checked individually with explicit PASS/FAIL prose; remediation if any FAIL |
| C-05 | PASS | Classification rules in priority order (NEEDS-SPEC-REVISION / NEEDS-REDESIGN / USEFUL); "Name the rule and the classification" |
| C-06 | PASS | SA-TO-SG PROMOTION section evaluates every SA gap from SA Stage 1 relay; post-promotion inventory required |
| C-07 | PASS | Relay fields all present in prose-led format; Schema 2 compliance inline table per relay |
| C-08 | PASS | Findings table: >= 3 rows, >= 2 Source types, Action distinct from Finding |
| C-09 | PASS | VC ledger with "specific observed values, not 'as expected'" requirement; EG-first variant delta noted in Phase 5 rationale |
| C-10 | PASS | Sub-step transition sentences present: "Step 3a complete. Step 3b is valid to begin." etc.; Step 3c transition embedded in gate-clearance summary |
| C-11 | PASS | Gate-clearance summary at Step 3c exit: "G-1 `<result>`, G-2 `<result>`, G-3 `<result>` — Step 3d is valid to begin"; Phase 4 entry: "Phase-entry gate-clearance summary (reflects post-remediation states)" |
| C-12 | PASS | "If any gate fails, document the remediation: what specifically failed, what was changed in Step 3b, and the re-check result"; exemption notice required |
| C-13 | PASS | Prerequisite confirmations before each sub-step with named referents ("Check: YES. Path: `<path>`"; "Check: YES. N findings collected"; "Referent: gate-clearance summary above") |
| C-14 | PASS | Phase 4 header: "Phase-entry gate-clearance summary **(reflects post-remediation states)**"; Step 3c gate-clearance summary header: "use final post-remediation states" — both enforcement points covered |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6
**Composite**: 60 + 30 + (6/6 × 10) = **100**

*Structural note on C-09*: V-04's EG-first Stage 1 sequencing diverges from Schema 3's declared "Stage 1 relay" as a single event. A compiler following V-04 would record this variant sequence in VC-3. The Phase 5 rationale block's "Naive-path delta" field is designed to capture whether the reordering surfaced additional EG gaps — if it did, the VC-3 observation would name the variant sequence and a reasonable reviewer would PASS VC-3 for the declared variant. C-09 scores PASS on the spec structure; VC-3 divergence is surfaced in Phase 5 rationale, not silently ignored.

---

### V-05 — Inertia Framing (naive-path competitor) + Phrasing Register (diagnostic)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four phases present; Phase 1 binding blocks with naive-path risk field; Phase 2 relays with naive-path delta field; Phase 3 sub-steps 3a→3b→3c→3d; Phase 4 amendments |
| C-02 | PASS | "write the artifact `simulations/trace/skill/{topic}-skill-trace-{date}.md`; list all required sections with WRITTEN status" |
| C-03 | PASS | Label constraint block: "Severity: P1 (naive path misses), P2 (partial miss), P3 (catchable without trace); Source: SA, SG, EG, QO" — labels locked, semantic anchors added |
| C-04 | PASS | G-1, G-2, G-3 each checked with diagnostic note; explicit PASS/FAIL per gate |
| C-05 | PASS | Three classification rules in priority order; additional diagnostic question: "would the naive path have reached this verdict?" |
| C-06 | PASS | SA-TO-SG PROMOTION with per-gap decision; additional "Why the naive path misses this" field per promotion |
| C-07 | PASS | All relay fields present plus "Naive-path delta" field required per relay |
| C-08 | PASS | Findings table: >= 3 rows, >= 2 Source types; Action format specified: "start with a verb and name the failure mode the action prevents" — strengthens distinctness requirement |
| C-09 | PASS | VC ledger: "specific observed values only — no 'as expected'"; explicit counts required per row |
| C-10 | PASS | Step 3a/3b/3d each close with "Step Xa complete. Step Xb is valid to begin"; Step 3c transition embedded in gate-clearance summary: "Step 3d is valid to begin" followed by "Step 3c complete" |
| C-11 | PASS | Gate-clearance summary in Step 3c: "G-1 `<final>`, G-2 `<final>`, G-3 `<final>` — Step 3d is valid to begin"; Phase 4 entry gate-clearance summary present |
| C-12 | PASS | Four-item remediation structure with naive-path commentary ("what the naive path would have done at this gate — most likely: skipped it"); "C-12 exemption applies" notice required |
| C-13 | PASS | Prerequisite checks at Steps 3a, 3b, 3c, 3d with explicit "Check: YES. Referent: `<path>`" form |
| C-14 | PASS | Phase 4: "Phase-entry gate-clearance summary **(post-remediation — not initial states)**" — brief but explicit; constraint placement is at point of error |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6
**Composite**: 60 + 30 + (6/6 × 10) = **100**

---

## Variation Ranking

| Rank | Variation | Score | Essential | C-14 implementation | Structural differentiator |
|------|-----------|-------|-----------|---------------------|--------------------------|
| 1 | V-03 | **100** | PASS | Named cross-reference chain — Phase 4 states must match Phase 3 post-remediation states "documented there" | Verbose phase-boundary ceremonies make every entry/close structurally load-bearing; C-14 enforced at two separate structural landmarks |
| 2 | V-01 | **100** | PASS | Parenthetical constraint in section header at point of error | Table-first format makes field omission structurally impossible; constraint embedded in the table header |
| 2 | V-02 | **100** | PASS | Direct imperative: "Use the post-remediation gate states — not what they were before any fixes" | Imperative register eliminates ambiguity between reading the instruction and knowing what to produce |
| 4 | V-05 | **100** | PASS | Brief parenthetical at Phase 4 entry | Naive-path framing elevates diagnostic quality — P-level calibrated against external baseline, Action format strengthened |
| 5 | V-04 | **100** | PASS | Brief parenthetical at both checkpoints | EG-first role sequence is structurally novel; introduces Schema 3 variant complexity as tradeoff |

*All five variations achieve the v3 golden threshold: all 5 essential criteria pass AND composite ≥ 80.*

---

## Excellence Signals from V-03

**Signal 1 — Named authoritative source for state inheritance.**
V-03's Phase 4 ENTRY does not merely say "use post-remediation states." It says: "these states must **match the post-remediation states documented there**." The phrase "documented there" creates a named cross-reference dependency — the compiler cannot satisfy C-14 by rewriting the states from memory; they must retrieve the specific values from the upstream remediation block. This converts C-14 from a constraint ("use correct states") into a verification step ("confirm your states match the named block"). No current criterion captures this: C-14 requires coherence between blocks but does not require the compiler to cite the authoritative source. This is a distinct structural property.

**Signal 2 — Severity semantic anchor via named comparison baseline.**
V-05 defines P-levels not as abstract severity tiers but relative to a named external reference: "P1 = naive path misses, P2 = partial miss, P3 = catchable without trace." Providing an external comparison agent (the naive path) as the P-level calibration instrument gives the compiler a concrete decision procedure rather than an intuitive judgment call. No current criterion captures calibrated severity assignment — existing criteria only validate that severity labels are from the permitted set {P1, P2, P3}, not that they carry consistent meaning. This generalizes: any schema with ordered severity tiers benefits from a named calibration baseline.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named authoritative source for state inheritance — when a downstream block must inherit state from an upstream remediation event, the downstream block names the specific upstream block as the authoritative source ('must match the post-remediation states documented there'), converting the coherence requirement from a constraint into a verifiable cross-reference", "Severity semantic anchor via named comparison baseline — P-level assignments gain consistent meaning when calibrated against a named external reference agent (e.g. 'naive path misses = P1, partial miss = P2, catchable without trace = P3'), shifting severity from intuitive judgment to a concrete decision procedure"]}
```
