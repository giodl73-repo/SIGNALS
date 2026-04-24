## org:committee Round 14 — Scorecard

---

### Criteria Reference

**Essential** (12 pts each): C-01 through C-05 — 60 pts total
**Recommended** (10 pts each): C-06 through C-08 — 30 pts total
**Aspirational** (2 pts each, 1 pt partial): C-09 through C-37 — 58 pts total
**Composite max**: 148

---

## V-01 — Single-Axis: Lifecycle Emphasis (Minimal Diff from R13 V-05)

### Essential — 60/60

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | `PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type`; VALIDATE with ACCEPTABLE/FAILS pairs anchors C-01 structurally |
| C-02 | PASS | `LOAD: charter from .roles/`; fallback to Signal defaults with explicit disclosure |
| C-03 | PASS | `WRITE: 2-4 sentences per participant from their charter-documented role orientation responding to this specific agenda item` |
| C-04 | PASS | Phase 5 skeleton pre-declares DECISIONS, ACTION ITEMS, DISSENTING OPINIONS as three named subsections |
| C-05 | PASS | `VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2` |

### Recommended — 30/30

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | `responding to this specific agenda item` repeated in REQUIRE statements per phase; voices must respond to prior concerns via RESPONDS-TO |
| C-07 | PASS | `[Owner Role] — [specific action] — [deadline]`; REQUIRE all three fields; "investigate" alone fails |
| C-08 | PASS | `resolution path (concrete condition + named authority who confirms when condition is met)`; Phase 5 DISSENTING OPINIONS require this |

### Aspirational — 58/58

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | INERTIA-FINDING-D required to be "specific enough that the author would say 'I missed that'" |
| C-10 | PASS | Re-entry path Owner + Trigger required in Phase 5 DECISIONS when verdict is not APPROVED |
| C-11 | PASS | Three-tier sort (CHALLENGERS → CONDITIONALS → ADVOCATES) with tie-break rule in skeleton |
| C-12 | PASS | Phase 1 investigation fully precedes Phase 3 voices; four named switching-cost findings required |
| C-13 | PASS | STANCE: declared before prose; VALIDATE prohibits prose softening |
| C-14 | PASS | Phase 4 TALLY is a discrete phase before Phase 5 MINUTES |
| C-15 | PASS | VALIDATE with ACCEPTABLE: `STANCE: BLOCK` on own line / FAILS: prose stance / FAILS: qualified token — bilateral ✓ |
| C-16 | PASS | GATE-1 with Question/Answer/Basis; YES/NO self-verification before Phase 2 |
| C-17 | PASS | `REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose` |
| C-18 | PASS | All-APPROVE detected → `REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK` |
| C-19 | PASS | RESPONDS-TO field required for Tier 3; must name specific Tier 1/2 concern |
| C-20 | PASS | VALIDATE with ACCEPTABLE: `CITE: INERTIA-FINDING-A — workflow-disruption:...` / FAILS: paraphrase / FAILS: parenthesized letter — bilateral ✓ |
| C-21 | PASS | RESPONDS-TO with ACCEPTABLE/FAILS: named concern required; "concerns acknowledged" fails |
| C-22 | PASS | `IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1`; loop runs within Phase 1 |
| C-23 | PASS | Owner + Trigger both required when verdict is not APPROVED |
| C-24 | PASS | Skeleton pre-declares INVESTIGATION-ATTEMPT-2 as empty block; `REQUIRE: sequential label increments by 1` |
| C-25 | PASS | SORT-CHECK as discrete labeled gate with `Test:` / `Result:` fields; correct ordering without gate fails |
| C-26 | PASS | Six explicitly labeled phases (PHASE 0–5) with named headers; single-phase execution per header |
| C-27 | PASS | VALIDATE with ACCEPTABLE/FAILS for finding label format; `INERTIA-FINDING-A: legacy-approval-workflow` ACCEPTABLE; `(a)` FAILS |
| C-28 | PASS | Two-step architecture: STEP 1 prints full skeleton including INVESTIGATION-ATTEMPT-2 as empty slot, SORT-CHECK with Test/Result, STANCE:, CITE:, RESPONDS-TO:, TALLY, all PHASE-N-COMMIT blocks |
| C-29 | PASS | `ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached` — intra-phase retry, unconditional Phase 2 |
| C-30 | PASS | All fill rules are verb-first imperatives: LOAD/WRITE/PRINT/ENFORCE/VALIDATE/REQUIRE/CONFIRM; no descriptive prose |
| C-31 | PASS | PHASE-N-COMMIT: block in every phase |
| C-32 | PASS | `\| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE` in every commit block |
| C-33 | PASS | `Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked` — commit references named section; enumeration held in independently addressable INERTIA RECORD |
| C-34 | PASS | VALIDATE with ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption` / FAILS: bare label / FAILS: unfilled placeholder — bilateral ✓ |
| C-35 | PASS | `Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked` — commit references named section; per-participant entries in STANCE MANIFEST |
| C-36 | PASS | All four required VALIDATE rules carry bilateral ACCEPTABLE/FAILS: finding-label format, manifest content-anchor, STANCE: label, CITE: structure |
| C-37 | PASS | `## INERTIA RECORD` and `## STANCE MANIFEST` pre-declared as named skeleton sections before their respective PHASE-N-COMMIT blocks |

**V-01 Total: 148/148**

---

## V-02 — Single-Axis: Output Format (Flat Command Sequence)

### Essential — 60/60

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | `PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type` |
| C-02 | PASS | `LOAD: charter from .roles/`; fallback declared |
| C-03 | PASS | `WRITE: 2-4 sentences from the participant's charter role orientation` |
| C-04 | PASS | Phase 5 produces DECISIONS, ACTION ITEMS, DISSENTING OPINIONS |
| C-05 | PASS | `VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 reopen` |

### Recommended — 30/30

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Agenda item specificity enforced via `REQUIRE (Tier 2): name the specific approval condition` |
| C-07 | PASS | `[Owner Role] — [specific action] — [deadline]` three-field format |
| C-08 | PASS | `specific objection...and resolution path (concrete condition + named authority)` |

### Aspirational — 56/58

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | INERTIA-FINDING-D requirement: proposal author "missed that" specificity |
| C-10 | PASS | Owner + Trigger in re-entry path |
| C-11 | PASS | Three-tier sort; challenger-first |
| C-12 | PASS | Investigation precedes voices |
| C-13 | PASS | STANCE: standalone before prose |
| C-14 | PASS | TALLY before MINUTES |
| C-15 | PASS | VALIDATE ACCEPTABLE/FAILS: `STANCE: BLOCK` on own line / prose stance fails / qualified token fails |
| C-16 | PASS | GATE-1 with YES/NO self-check |
| C-17 | PASS | Tier 3 CITE requirement |
| C-18 | PASS | All-APPROVE triggers Phase 2 reopen |
| C-19 | PASS | RESPONDS-TO required |
| C-20 | PASS | VALIDATE ACCEPTABLE/FAILS: `CITE: INERTIA-FINDING-B — webhook-contract:...` / paraphrase fails / parenthesized letter fails |
| C-21 | PASS | RESPONDS-TO ACCEPTABLE/FAILS |
| C-22 | PASS | Gate retry loop within Phase 1 |
| C-23 | PASS | Owner + Trigger required |
| C-24 | PASS | `ENFORCE: each retry carries a new sequential INVESTIGATION-ATTEMPT-N label` |
| C-25 | PASS | SORT-CHECK with Test:/Result: fields |
| C-26 | PASS | Six labeled PHASE headers |
| C-27 | PASS | VALIDATE ACCEPTABLE/FAILS for finding label format |
| C-28 | **FAIL** | No two-step skeleton architecture; all instructions are inline sequential commands; no pre-printed skeleton with empty slots before content generation |
| C-29 | PASS | `ENFORCE: the loop runs within Phase 1; Phase 2 is unconditionally reached once any GATE-N answers YES` |
| C-30 | PASS | All rules are verb-first imperatives: PRINT/LOAD/ENFORCE/WRITE/VALIDATE/DERIVE/COUNT |
| C-31 | PASS | PHASE-N-COMMIT in every phase |
| C-32 | PASS | `\| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE` in every commit |
| C-33 | PASS | `Citation-anchor manifest declared in ## INERTIA RECORD above; all findings locked by label` |
| C-34 | PASS | VALIDATE ACCEPTABLE/FAILS: content-anchor entries |
| C-35 | PASS | `Vote-anchor manifest declared in ## STANCE MANIFEST above` |
| C-36 | PASS | Bilateral VALIDATE examples on all four required rules |
| C-37 | PASS | `## INERTIA RECORD` and `## STANCE MANIFEST` produced as named section headers independently addressable by heading — manifest is not embedded in commit block text |

**V-02 Total: 146/148** (C-28 FAIL: −2 pts)

---

## V-03 — Single-Axis: Phrasing Register (Conversational)

### Essential — 60/60

All five essential criteria pass on the same grounds as V-01 — skeleton declares the structure; phases produce required sections; STANCE/CITE/RESPONDS-TO requirements enforced.

### Recommended — 30/30

Agenda specificity, owned action items, and dissent resolution paths all present.

### Aspirational — 56/58

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-27 | PASS | All gates, tier sort, commit blocks, label requirements, and intra-phase retry loops present — consistent with V-01 for criteria preceding C-28 |
| C-28 | **PARTIAL** | Skeleton is pre-declared (STEP 1 prints skeleton before STEP 2 fills it); ## INERTIA RECORD and ## STANCE MANIFEST named sections present; SORT-CHECK with Test:/Result:, STANCE:, CITE:, RESPONDS-TO:, TALLY pre-declared. However: INVESTIGATION-ATTEMPT-2 is NOT pre-declared as an empty skeleton block — only `[NO → INVESTIGATION-ATTEMPT-2 within Phase 1; repeat until YES]` appears as a conditional note. C-28 explicitly lists "INVESTIGATION-ATTEMPT-N blocks (C-24)" as required pre-declared slots. |
| C-29 | PASS | "Keep going until a gate answers YES. Each retry needs its own labeled attempt block." |
| C-30 | **PARTIAL** | Fill rules blend imperatives (ENFORCE, PRINT at commit/gate blocks) with descriptive prose: "Load the charter file from `.roles/`...Pull every role...If no charter exists, declare that and fall back..." — Phase 0 and Phase 1 descriptions are narrative rather than verb-first imperatives. |
| C-31 | PASS | PHASE-N-COMMIT in every phase |
| C-32 | PASS | `\| ENFORCE: terminal position` in every commit |
| C-33–C-37 | PASS | Named manifest sections present; bilateral VALIDATE examples on all four rules; commit references named sections |

**V-03 Total: 146/148** (C-28 PARTIAL: −1 pt; C-30 PARTIAL: −1 pt)

---

## V-04 — Combined: Lifecycle + Inertia Framing

### Essential — 60/60

All five pass; Inertia-Advocate invariant strengthens C-05 compliance (BLOCK/CONDITION structurally guaranteed from an always-present Tier 1 role).

### Recommended — 30/30

All three pass with same rigor as V-01.

### Aspirational — 57/58

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-27 | PASS | All prior criteria satisfied; Inertia-Advocate invariant adds `REQUIRE: Inertia-Advocate grounds concern in at least two named labels from ## INERTIA RECORD` (exceeds minimum for C-17) |
| C-28 | **PARTIAL** | Two-step skeleton architecture present; ## INERTIA RECORD and ## STANCE MANIFEST pre-declared as named first-class sections with framing annotations `[First-class investigation artifact — independently addressable]`; SORT-CHECK with Test:/Result: AND `Inertia-Advocate check:` field. However: skeleton includes only `[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; repeat until YES]` as a conditional note — INVESTIGATION-ATTEMPT-2 is not pre-declared as an empty labeled block. V-04's fill rules enforce sequential labels via `REQUIRE: each rewrite carries a sequential INVESTIGATION-ATTEMPT-N label` but the slot is not an empty pre-declared container in the skeleton. |
| C-29 | PASS | `ENFORCE: loop runs within Phase 1; Phase 2 is always reached` |
| C-30 | PASS | All fill rules are verb-first imperatives: LOAD/ENFORCE/REQUIRE/PRINT/VALIDATE/ASSIGN/CONFIRM/WRITE |
| C-31 | PASS | PHASE-N-COMMIT in every phase |
| C-32 | PASS | `\| ENFORCE: terminal position` in every commit |
| C-33 | PASS | `Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked` |
| C-34 | PASS | VALIDATE ACCEPTABLE/FAILS for content-anchor entries |
| C-35 | PASS | `Vote-anchor manifest declared in ## STANCE MANIFEST above` |
| C-36 | PASS | Bilateral VALIDATE on all four rules: finding label (INERTIA-FINDING-A vs `(a)`, vs `A.`), content-anchor (keyword anchor vs bare label vs placeholder), STANCE: label (own-line vs prose vs qualified token), CITE: (named label vs prose vs parenthesized letter) |
| C-37 | PASS | `## INERTIA RECORD` and `## STANCE MANIFEST` each have own skeleton headers with framing annotations; independently addressable by section heading |

**V-04 Total: 147/148** (C-28 PARTIAL: −1 pt)

---

## V-05 — Full Synthesis (All Axes)

### Essential — 60/60

All five pass on the same grounds as V-01; C-05 structurally guaranteed by the all-APPROVE VALIDATE rule.

### Recommended — 30/30

All three pass.

### Aspirational — 58/58

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-27 | PASS | All criteria satisfied; V-05 adds bilateral VALIDATE on SORT-CHECK reassignment (C-25), STANCE MANIFEST completeness, TALLY count matching, and dissent citation — all beyond the minimum required for C-36 |
| C-28 | PASS | Full two-step skeleton with INVESTIGATION-ATTEMPT-1 AND INVESTIGATION-ATTEMPT-2 pre-declared as empty labeled blocks; ## INERTIA RECORD and ## STANCE MANIFEST as named sections with framing annotations; SORT-CHECK Test:/Result:; STANCE:, CITE:, RESPONDS-TO:; TALLY; all PHASE-N-COMMIT blocks with ENFORCE markers |
| C-29 | PASS | `ENFORCE: the gate loop runs within Phase 1; Phase 2 is unconditionally reached` |
| C-30 | PASS | Every fill rule is a verb-first imperative: LOAD/ASSIGN/ENFORCE/WRITE/PRINT/VALIDATE/REQUIRE/CONFIRM/COUNT/DERIVE |
| C-31 | PASS | PHASE-N-COMMIT in every phase |
| C-32 | PASS | `\| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE` |
| C-33 | PASS | `Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked by label` |
| C-34 | PASS | VALIDATE ACCEPTABLE/FAILS: `INERTIA-FINDING-A: release-gate-script` / bare label fails / skeleton placeholder fails |
| C-35 | PASS | `Vote-anchor manifest declared in ## STANCE MANIFEST above`; VALIDATE: every participant has exactly one entry; ACCEPTABLE: four entries for four participants / FAILS: three entries for four participants |
| C-36 | PASS | Bilateral ACCEPTABLE/FAILS on: finding-label format, manifest content-anchor, STANCE: label, CITE: structure, RESPONDS-TO: specificity, all-APPROVE check, SORT-CHECK reassignment, TALLY count, dissent citation |
| C-37 | PASS | `## INERTIA RECORD` with `[Named first-class investigation artifact — independently addressable by section heading]` framing; `## STANCE MANIFEST` with `[Named first-class vote record — independently addressable by section heading]`; both pre-declared in skeleton |

**V-05 Total: 148/148**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | **Total** | Gaps |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 | 60/60 | 30/30 | 58/58 | **148/148** | — |
| V-02 | 60/60 | 30/30 | 56/58 | **146/148** | C-28 FAIL |
| V-03 | 60/60 | 30/30 | 56/58 | **146/148** | C-28 PARTIAL, C-30 PARTIAL |
| V-04 | 60/60 | 30/30 | 57/58 | **147/148** | C-28 PARTIAL |
| V-05 | 60/60 | 30/30 | 58/58 | **148/148** | — |

**Ranking**: V-01 = V-05 (148) > V-04 (147) > V-02 = V-03 (146)

---

## Excellence Signals

**Top score: 148/148** — achieved by V-01 and V-05.

**What separated 148 from 147/146:**

The single architectural choice that distinguishes 148 from 147: **INVESTIGATION-ATTEMPT-2 pre-declared as an empty labeled skeleton block** in STEP 1, not merely mentioned as a conditional note in fill rules. V-01 and V-05 both print the ATTEMPT-2 block (with INERTIA-FINDING-A–D placeholders and GATE-2) as an empty container in the skeleton. V-03 and V-04 rely on `[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; repeat until YES]` — a conditional instruction, not a pre-declared slot. C-28 explicitly names "INVESTIGATION-ATTEMPT-N blocks (C-24)" as required pre-declared structural slots.

**The commit-references-named-section pattern**: Rather than enumerating findings or stances inline in PHASE-1-COMMIT / PHASE-3-COMMIT text (which would duplicate the named section), both 148/148 variations use the pattern `Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked` — the commit declares that the manifest EXISTS and is LOCKED, the named section holds the enumerated entries. This cleanly satisfies C-33/C-35 (manifest accessible and locked at commit) plus C-37 (independently addressable section) without redundancy.

**V-05's defense-in-depth VALIDATE coverage**: V-05 adds bilateral ACCEPTABLE/FAILS on criteria beyond the four required for C-36: SORT-CHECK reassignment (grounded in ## INERTIA RECORD labels), STANCE MANIFEST completeness (every Phase 0 participant must appear), TALLY count matching (manifest is authoritative), dissent citation format. These don't add points under v14 but signal structural completeness that would protect against future rubric expansions.

---

```json
{"top_score": 148, "all_essential_pass": true, "new_patterns": ["INVESTIGATION-ATTEMPT-2 pre-declared as empty labeled skeleton block — the retry template must exist as a pre-printed slot in STEP 1, not as a conditional note in fill rules, to satisfy C-28's INVESTIGATION-ATTEMPT-N requirement", "commit-references-named-section pattern: PHASE-N-COMMIT declares 'Citation-anchor manifest declared in ## INERTIA RECORD above; findings A-D locked' — commit locks and points, named section holds the enumeration — satisfies C-33/C-35 and C-37 without inline duplication"]}
```
