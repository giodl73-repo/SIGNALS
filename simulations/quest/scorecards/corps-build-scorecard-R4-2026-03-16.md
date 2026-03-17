## Quest Score — corps-build R4

---

### Scoring Method

Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)`

Aspirational pool expanded from 8 to 10 in v4. Each aspirational criterion = 1 point.

---

### V-01 — Lifecycle Emphasis: Named BUILD-VERIFY Phase

**Phase sequence**: PARSE → VALIDATE → WRITE → BUILD-VERIFY → CROSS-REF

WRITE contains: 3a profiles (no files), 3b IA files, 3c org-chart.md, 3d standard/specialized.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | 3d writes all roles by area-slug path; ROLES-COMPLETE gate |
| C-02 | PASS | 3c sections: ASCII hierarchy + table + AMEND |
| C-03 | PASS | 3b writes IA files before 3d; IA-PHASE-COMPLETE gate |
| C-04 | PASS | Paths follow org.yaml nesting; no reshuffling |
| C-05 | PASS | All five fields required; "no placeholder text" explicit |
| C-06 | PASS | 3c section 2 headcount table + section 3 level distribution |
| C-07 | PASS | 3d scope field explicit: standard/specialized/shared/exec labels |
| C-08 | PASS | 3c section 4 AMEND with --area, --levels, --restructure + specific values |
| C-09 | PASS | 3a extracts per-team resistance profiles; "no two IA files share identical lens or expertise text" |
| C-10 | PASS | CROSS-REF checks org.yaml slots vs files, IA teams vs files, dir check |
| C-11 | PASS | Phase 2 VALIDATE — 4 named checks, no files before VALIDATE-PASS |
| C-12 | PASS | 3b IA before 3d standard; IA-PHASE-COMPLETE gate before 3d begins |
| C-13 | **FAIL** | Headcount table is in 3c (org-chart.md), written AFTER IA files in 3b — not the first artifact |
| C-14 | **FAIL** | 3c requires headcount table and level distribution but no analytic prose sentences |
| C-15 | PASS | "no generic stability language," "specific concern not generic caution," lens opens verbatim with profile phrase |
| C-16 | PASS | 3a profiles — defended-artifact + change-pressure + lens-phrase — precede 3b IA writes |
| C-17 | PASS | Phase 4 BUILD-VERIFY is a dedicated post-write phase; single purpose; VERBATIM/DRIFT binary per team |
| C-18 | **FAIL** | No CONTRACT-SEAL; headcount table first appears in 3c org-chart.md write, not a sealed pre-role artifact |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 7/10 → 7

**V-01 Total: 97**

---

### V-02 — Output Format: CONTRACT-SEAL and TRANSCRIPTION-RECEIPT

**Phase sequence**: PARSE → VALIDATE → CONTRACT → CONTRACT-SEAL → PROFILE → WRITE → CROSS-REF

CONTRACT (Phase 3) produces ARTIFACT-A/B/C before any file. Phase 6b org-chart.md emits TRANSCRIPTION-RECEIPT.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | 6c writes standard/specialized/shared/exec roles |
| C-02 | PASS | 6b org-chart.md with ASCII hierarchy |
| C-03 | PASS | 6a IA files before 6c; IA-PHASE-COMPLETE gate |
| C-04 | PASS | Paths explicit per scope type; dir structure follows org.yaml |
| C-05 | PASS | All five fields; scope explicit; "no placeholder text" |
| C-06 | PASS | Phase 3 ARTIFACT-A headcount + ARTIFACT-C level distribution |
| C-07 | PASS | Scope: standard/specialized/shared/exec explicit in each file |
| C-08 | PASS | 6b AMEND with --area (+ available list), --levels (+ in-use list), --restructure (+ current nesting) |
| C-09 | PASS | Phase 5 per-team profiles; 6a IA files derived from them; "differs from every other team's IA expertise" |
| C-10 | PASS | Phase 7 CROSS-REF: slots vs files, IA vs teams, dir check, plus "table fidelity" check |
| C-11 | PASS | Phase 2 VALIDATE — 4 checks, no files before VALIDATE-PASS |
| C-12 | PASS | 6a IA-PHASE-COMPLETE gate before 6c standard roles |
| C-13 | PASS | Phase 3 CONTRACT writes headcount table pre-role; TABLE-CLOSED gate precedes PROFILE and WRITE |
| C-14 | PASS | Phase 3 ARTIFACT-B: mandatory 2-3 sentences; sentence 1 names largest area as % of total; strong/weak example provided |
| C-15 | PASS | "orientation: specific concern not generic caution"; "lens: no generic stability language"; "expertise: anchored to defended-artifact" — portrait language present |
| C-16 | PASS | Phase 5 PROFILE with three gated fields before Phase 6 IA writes; PROFILE-GATE |
| C-17 | **FAIL** | No BUILD-VERIFY phase. Phase 7 CROSS-REF checks "table fidelity" (count match) but does NOT verify IA lens phrases against profiles |
| C-18 | PASS | Phase 4 CONTRACT-SEAL with first-row lock + sentence-1 lock; Phase 6b TRANSCRIPTION-RECEIPT VERBATIM/REVISED per artifact; rewrite triggered on REVISED |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 9/10 → 9

**V-02 Total: 99**

---

### V-03 — Phrasing Register: Output-Forward Verbatim Chain

**Stage sequence**: Parse → Validate → Stage 3 (build contract) → Stage 4 (profiles) → Stage 5 (IA files) → Stage 6 (standard/spec roles) → Stage 7 (org-chart.md) → Stage 8 (build-complete verification) → Stage 9 (cross-reference)

Output-forward language describes what correct output looks like; VERBATIM/DRIFT and VERBATIM/REVISED contrasts shown.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Stage 6 writes standard, specialized, shared group, exec office roles |
| C-02 | PASS | Stage 7 org-chart.md with ASCII hierarchy |
| C-03 | PASS | Stage 5 writes all IA files before Stage 6; IA-COMPLETE gate |
| C-04 | PASS | Paths and scope match org.yaml structure |
| C-05 | PASS | "Five fields: orientation, lens, expertise, scope, collaboration pattern" — no placeholder text |
| C-06 | PASS | Stage 3 Component A (headcount table) + Component C (level distribution) |
| C-07 | PASS | "Scope explicit in every file" |
| C-08 | PASS | Stage 7 AMEND section: --area, --levels, --restructure each with specific values |
| C-09 | PASS | Stage 4 resistance profiles; "lens-phrase... cannot be produced without knowing both fields"; Stage 5 IA files from profiles |
| C-10 | PASS | Stage 9 CROSS-REF: slots vs files, IA teams vs files, table fidelity check |
| C-11 | PASS | Stage 2 Validate: 4 structural checks before any file; "list it and halt" |
| C-12 | PASS | Stage 5 IA files before Stage 6; IA-COMPLETE: [n of n] teams |
| C-13 | PASS | Stage 3 "produced in this stage only — not rewritten later"; CONTRACT-READY gate precedes Stage 4 and Stage 5 |
| C-14 | PASS | Stage 3 Component B: specific findings; correct/incorrect example pair provided |
| C-15 | PASS | "portrait of the specific person"; "cannot be transplanted unchanged to a different team's IA slot"; per-file check: "expertise names a concrete artifact (not a category): YES / NO" |
| C-16 | PASS | Stage 4 per-team profiles; PROFILE-COMPLETE gate before Stage 5 |
| C-17 | PASS | Stage 8 "After all files are written, the build-complete verification..."; BUILD-VERIFY block VERBATIM/DRIFT per team; BUILD-VERIFY-PASS/FAIL |
| C-18 | PASS | Stage 3 builds contract pre-role; Stage 7 says "copied verbatim... not written again from org.yaml... Not a rewrite... Not a summary"; TRANSCRIPTION-RECEIPT with side-by-side sentence comparison |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 10/10 → 10

**V-03 Total: 100**

---

### V-04 — Lifecycle + Output Format: CONTRACT-TRANSCRIBE-VERIFY Pipeline

**Step sequence**: PARSE → VALIDATE → CONTRACT → CONTRACT-SEAL → PROFILE → WRITE-IA → WRITE-ROLES → TRANSCRIBE → BUILD-VERIFY → CROSS-REF

Combines V-01's BUILD-VERIFY mechanism with V-02's CONTRACT-SEAL + TRANSCRIPTION-RECEIPT mechanism as a named pipeline.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Step 7 WRITE-ROLES covers standard/specialized/shared/exec; ROLES-GATE count check |
| C-02 | PASS | Step 8 TRANSCRIBE writes org-chart.md with ASCII hierarchy |
| C-03 | PASS | Step 6 WRITE-IA before Step 7; IA-PHASE-COMPLETE gate |
| C-04 | PASS | Paths explicit per scope type |
| C-05 | PASS | Five fields; no placeholder text; scope explicit |
| C-06 | PASS | Step 3 ARTIFACT-A headcount + ARTIFACT-C level distribution |
| C-07 | PASS | Scope explicit per role type |
| C-08 | PASS | Step 8 AMEND section: three options with specific values |
| C-09 | PASS | Step 5 per-team profiles; Step 6 IA files from profiles; "expertise concrete: YES / NO" per file |
| C-10 | PASS | Step 10 CROSS-REF: slots vs files, IA vs teams, dir check |
| C-11 | PASS | Step 2 VALIDATE — 4 checks, no files before VALIDATE-PASS |
| C-12 | PASS | Step 6 WRITE-IA before Step 7 WRITE-ROLES; IA-PHASE-COMPLETE gate |
| C-13 | PASS | Step 3 CONTRACT: headcount table pre-role; CONTRACT-DRAFT gate before PROFILE and WRITE |
| C-14 | PASS | Step 3 ARTIFACT-B: three specific sentences; "No generic summaries" |
| C-15 | PASS | Step 6 PORTRAIT self-check: 4-item checklist including "no generic phrases," "concrete artifact not category," "could not be transplanted unchanged" |
| C-16 | PASS | Step 5 PROFILE with three gated fields; PROFILE-GATE; "cannot be written without knowing both fields" |
| C-17 | PASS | Step 9 BUILD-VERIFY entry: CHART-GATE; "runs after all files are written — not at write time"; VERBATIM/DRIFT per team; BUILD-VERIFY-PASS/FAIL |
| C-18 | PASS | Step 4 CONTRACT-SEAL with first-row lock + sentence-1 lock; Step 8 TRANSCRIPTION-RECEIPT VERBATIM/REVISED per artifact; rewrite on REVISED |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 10/10 → 10

**V-04 Total: 100**

---

### V-05 — Full Integration: All Ten Aspirational Criteria

**Phase sequence**: PARSE → VALIDATE → BUILD CONTRACT → RESISTANCE PROFILES → WRITE ROLE FILES → WRITE ORG-CHART.MD → BUILD-VERIFY → CROSS-REFERENCE

Explicit C-09 through C-18 mechanism map. BUILD CONTRACT includes CONTRACT-SEAL (Phase 3d). IA phase includes 4-item PORTRAIT-CHECK. ROLES-GATE checks written count vs TABLE-CLOSED contract.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | 5b standard + 5c specialized + 5d shared group + 5e exec office; ROLES-GATE MATCH/MISMATCH vs TABLE-CLOSED |
| C-02 | PASS | Phase 6 org-chart.md: ASCII hierarchy minimum two nesting levels |
| C-03 | PASS | Phase 5a IA-PHASE-COMPLETE gate; "Standard and specialized roles may now be written" |
| C-04 | PASS | Standard/specialized distinction "not derivable from directory alone"; explicit scope in every file |
| C-05 | PASS | Five fields; "No placeholder text in any field" |
| C-06 | PASS | Phase 3 3a headcount table (TABLE-CLOSED) + 3b analytic prose + 3c level distribution |
| C-07 | PASS | Scope explicit per role type; four scope labels defined |
| C-08 | PASS | Phase 6 AMEND: three options each with specific values + example values |
| C-09 | PASS | Phase 4 per-team profiles; Phase 5a IA files from profiles; per-file "lens-phrase appears verbatim: YES/NO" + "expertise anchored: YES/NO" |
| C-10 | PASS | Phase 8 CROSS-REF C1 (TABLE-CLOSED vs file count), C2 (IA vs teams), C3 (areas vs dirs) |
| C-11 | PASS | Phase 2 VALIDATE — 4 named checks; "No files written"; VALIDATE-FAIL halts |
| C-12 | PASS | Phase 5a IA-PHASE-COMPLETE gate with "All portraits verified. Standard and specialized roles may now be written." |
| C-13 | PASS | Phase 3 3a produces headcount table pre-role; TABLE-CLOSED gate; "File generation must produce exactly [n] .craft/roles/ files" |
| C-14 | PASS | Phase 3 3b analytic prose mandatory: 3 specific sentences; "a structural observation the table rows alone do not convey — not generic" |
| C-15 | PASS | Phase 5a PORTRAIT-CHECK: 4-item checklist with "no generic resistance phrases," "concrete artifact not domain category," "could not be transplanted unchanged"; PORTRAIT-CHECK gate must pass before IA-PHASE-COMPLETE |
| C-16 | PASS | Phase 4 RESISTANCE PROFILES: three fields; PROFILE-GATE; "Derivation requirement" stated; generic profiles explicitly rejected |
| C-17 | PASS | Phase 7 BUILD-VERIFY entry: CHART-GATE; "Purpose: Close the C-16 derivation loop as a post-write structural invariant"; VERBATIM/DRIFT per team; BUILD-VERIFY-GATE before CROSS-REFERENCE |
| C-18 | PASS | Phase 3 3d CONTRACT-SEAL with first-row lock + sentence-1 lock; "RULE: These artifacts are FINAL"; Phase 6 TRANSCRIPTION-RECEIPT VERBATIM/REVISED per artifact |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 10/10 → 10

**V-05 Total: 100**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Fails |
|-----------|-----------|-------------|--------------|-------|-------|
| V-01 | 60/60 | 30/30 | 7/10 | **97** | C-13, C-14, C-18 |
| V-02 | 60/60 | 30/30 | 9/10 | **99** | C-17 |
| V-03 | 60/60 | 30/30 | 10/10 | **100** | — |
| V-04 | 60/60 | 30/30 | 10/10 | **100** | — |
| V-05 | 60/60 | 30/30 | 10/10 | **100** | — |

**Ranking**: V-03 = V-04 = V-05 (100) > V-02 (99) > V-01 (97)

Golden threshold (all essential pass + composite >= 80): **all 5 variations pass**.

---

## V-01 Failure Analysis

V-01's single-axis focus (C-17 only) leaves three gaps:

**C-13**: IA files are written in Phase 3b before org-chart.md in Phase 3c, so the headcount table is not the first artifact — it follows behind the first role files. The contract-before-files ordering was not part of the C-17 axis.

**C-14**: The WRITE phase's org-chart.md section specifies headcount table and level distribution but omits analytic prose. No sentence requirement, no strong/weak example. Also a casualty of the narrow axis focus.

**C-18**: Headcount table is written inline during org-chart.md creation with no prior sealing step. No TRANSCRIPTION-RECEIPT. The contract/transcription pair was explicitly deferred to V-02.

Implication: C-13, C-14, C-18 are structurally linked — they all derive from the "build contract before files" pattern. Addressing C-17 alone without pulling in the contract phase leaves three related criteria unmet.

---

## V-02 Failure Analysis

V-02's single-axis focus (C-18 only) closes the contract/transcription loop but leaves C-17 unaddressed. Phase 7 CROSS-REF checks table fidelity (count match) and IA file count but does not inspect IA lens field content against resistance profile phrases. A total-based count check cannot catch phrase drift.

Implication: C-17 and C-18 require different verification directions — C-18 guards the source (seal before write), C-17 guards the destination (verify after write). A single CROSS-REF check cannot serve both.

---

## Excellence Signals (V-03, V-04, V-05 — all 100)

### Signal 1: Output-Forward Phrasing Achieves Equivalent Coverage to Formal Gating (V-03)

V-03 reaches 10/10 aspirational through a different mechanism than V-04/V-05. Rather than formal gate labels (CONTRACT-SEAL, BUILD-VERIFY-GATE), V-03 describes what correct output looks like and shows explicit contrasts:

- "What verbatim transcription means" / "What verbatim transcription does not mean"
- "What VERBATIM means: The first words of the lens field in the written file are exactly the words in the lens-phrase" / "What DRIFT means: a paraphrase, a synonym, or a summary"

This framing produces C-17 and C-18 compliance by pattern-matching the model to a target output shape rather than by process enforcement. It is a distinct and independently sufficient axis for both criteria.

### Signal 2: First-Row Lock + Sentence-1 Lock as Sub-Total Anchors (V-02, V-04, V-05)

CONTRACT-SEAL in V-02/V-04/V-05 includes:

```
first-row lock: "[area name] | [n]"
sentence-1 lock: "[first sentence verbatim]"
```

This moves verification from total-level (count match, easily satisfied by regeneration) to string-level (exact first row, exact first sentence). A model that regenerates the table and arrives at the same total will still fail the first-row lock if any area name or row ordering changed. This is a mechanically precise anti-drift anchor.

### Signal 3: BUILD-VERIFY Positioned After CHART-GATE, Not ROLES-GATE (V-04, V-05)

V-04 and V-05 place BUILD-VERIFY entry at CHART-GATE (after org-chart.md is written) rather than after role file writes. This matters because org-chart.md is the final artifact — placing BUILD-VERIFY after it means the derivation loop is confirmed on the complete, user-visible output set, not on intermediate role files. If the model writes org-chart.md and that write triggers any lens reformulation, BUILD-VERIFY still catches it.

### Signal 4: PORTRAIT-CHECK as 4-Item Structural Gate (V-04, V-05)

V-04 and V-05 replace the per-file YES/NO lens check with a formal post-IA-phase PORTRAIT-CHECK listing:
- No two IA files share identical lens or expertise text
- Every lens field contains no generic phrases (named: "stability," "institutional knowledge," "status quo")
- Every expertise entry names a concrete artifact, not a domain category
- File could not be transplanted to a different team unchanged

This makes portrait quality a gated pass condition (PORTRAIT-CHECK: n/n pass) rather than a per-file annotation. A PORTRAIT-CHECK failure blocks the transition from the IA phase to the standard-roles phase.

---

## New Patterns for R5

Two patterns not previously codified:

1. **Verbatim lock at field level, not total level**: CONTRACT-SEAL with first-row and sentence-1 locks makes transcription verification auditable at string precision. A total match is insufficient — the specific anchor strings must match. This prevents the regeneration failure mode where the model produces numerically identical output from org.yaml rather than copying the sealed artifact.

2. **C-17 and C-18 require complementary verification directions**: C-18 guards the source artifact (seal before any file is written — drift-prevention); C-17 guards the destination artifact (verify after all files are written — drift-detection). Collapsing both into a CROSS-REF check allows each to mask the other. The correct structure is CONTRACT-SEAL → TRANSCRIBE (receipt) → BUILD-VERIFY as a three-step pipeline where each step closes a different failure mode.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Verbatim lock at field level not total level: CONTRACT-SEAL first-row and sentence-1 locks make transcription verification string-precise — a numeric total match is insufficient and regeneration with correct counts passes the total check but fails the lock", "C-17 and C-18 require complementary verification directions: C-18 seals the source before writing (drift-prevention), C-17 verifies the destination after writing (drift-detection); collapsing both into a single CROSS-REF allows each to mask the other — correct structure is CONTRACT-SEAL then TRANSCRIBE-with-receipt then BUILD-VERIFY as a three-step pipeline"]}
```
