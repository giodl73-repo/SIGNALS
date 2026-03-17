---

## Round 4 Scorecard — `topic-report`

### Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-04 Combined triple | 5/5 | 3/3 | 9/9 | **100** | YES |
| 1 | V-05 Contract ceiling | 5/5 | 3/3 | 9/9 | **100** | YES |
| 3 | V-02 LOCK + inline | 5/5 | 3/3 | 8/9 | **98.9** | NO |
| 3 | V-03 Scan + inline | 5/5 | 3/3 | 8/9 | **98.9** | NO |
| 5 | V-01 Inline + examples | 5/5 | 3/3 | 7/9 | **97.8** | NO |

**Prediction confirmed exactly.** C-17 passed for all five variations; C-15 and C-16 are the discriminators.

### Per-variation C-15 / C-16 / C-17 verdicts

| Variation | C-15 LOCK | C-16 Scan | C-17 Inline | Gap |
|-----------|-----------|-----------|-------------|-----|
| V-01 | FAIL — "This list is closed" is an embedded clause, not a standalone named directive | FAIL — no COMPLETENESS CHECK / EXCLUSIVITY CHECK procedure | PASS — [RULE] markers at all governed slots + worked examples inside each annotation | -2 |
| V-02 | PASS — step 2d: "LOCK: ... frozen. No additions, removals, or revisions... permitted in PHASE 3 or PHASE 4." | FAIL — inline [RULE] annotations are declarative; no two-step enumeration scan | PASS — [RULE] markers at all governed slots; LOCKED list referenced by name in annotations | -1 |
| V-03 | FAIL — "This list is closed. Do not revise in PHASE 3." — no LOCK label, no phase-spanning scope | PASS — COMPLETENESS CHECK + EXCLUSIVITY CHECK scan immediately after inline [RULE] in both branches | PASS — [RULE] markers + scan at every write point; "branches are sealed" + "[This branch is self-contained...]" at correct positions | -1 |
| V-04 | PASS — step 2d standalone LOCK with named scope | PASS — scan references "LOCKED BLOCKERS list from Phase 2" in both branches | PASS — three-layer co-location at SLOT 3: [RULE] declares, LOCKED reference anchors, scan verifies | 0 |
| V-05 | PASS — "frozen and final... any subsequent phase" — strongest LOCK scope in R4 | PASS — G-7a COMPLETENESS SCAN / G-7b EXCLUSIVITY SCAN headers match contract labels | PASS — contract label chaining: register -> inline [RULE G-7a/G-7b] -> scan header | 0 |

### Excellence Signals

**E-1: Three-layer co-location at the write point (V-04, V-05)** — `[RULE]` declares, LOCKED reference anchors, scan verifies, all at SLOT 3. No cross-phase recall needed at any layer.

**E-2: Contract label chaining (V-05)** — G-7a/G-7b names at the contract register match the inline `[RULE G-7a/G-7b]` annotation names and the scan header labels. The invariant is independently recoverable at three structural levels without cross-position lookup.

**E-3: Worked example within `[RULE]` annotation (V-01 isolation finding)** — compact correct/violation examples embedded inside each annotation reduce translation distance from constraint to output action beyond co-location alone. Does not compensate for missing C-15/C-16, but is a candidate **C-18** discriminator for R5.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Contract label chaining to inline annotations -- G-7a/G-7b names at contract register match [RULE G-7a/G-7b] annotation names and G-7a/G-7b scan header labels; the invariant is independently recoverable at register, annotation, and scan header positions without cross-position lookup (V-05 ceiling design)", "Three-layer co-location at the write point -- [RULE] annotation declares constraint, LOCK reference anchors list immutability, scan verifies compliance, all at the same structural position; no cross-phase recall needed for any enforcement layer (V-04 minimal golden, V-05 ceiling)", "Worked example within [RULE] annotation -- compact correct/violation examples embedded inside each inline annotation reduce translation distance from rule to action beyond co-location alone; distinct from C-17 and a candidate C-18 discriminator for R5 (V-01 isolation finding)"]}
```
 named at every application site |
| C-14 | Branch sealing instruction present | PASS | [RULE BRANCH-SEAL] at dispatch: "Execute ONE branch only. Do not reference the other branch's format descriptions"; [RULE BRANCH-B-SEAL] at Branch B entry: "This branch is self-contained. Do not reference Branch A's format descriptions" |
| C-15 | BLOCKERS LOCK directive present | FAIL | "This list is closed. Do not revise it in any phase that follows." -- embedded clause appended to the BLOCKERS section, not a standalone named directive. Rubric explicitly states: "the embedded clause 'this list is closed' within the pre-computation step does not satisfy this criterion because it does not name the directive or assert it as a phase-spanning constraint." V-01 is the C-17-isolated design; LOCK is deliberately absent. |
| C-16 | In-render verification scan present | FAIL | No COMPLETENESS CHECK / EXCLUSIVITY CHECK procedural scan before writing the readiness sentence. [RULE COMPLETENESS] and [RULE EXCLUSIVITY] at READINESS are declarative annotations, not an active two-step enumeration procedure. V-01 is the C-17-isolated design; scan is deliberately absent. |
| C-17 | Rules co-located with governed template positions | PASS | [RULE] markers at every governed slot: [RULE TABLE-SOURCE] at PROGRESS TABLE, [RULE OPEN-FORMAT] at OPEN SIGNALS, [RULE COMPLETENESS]/[RULE EXCLUSIVITY] at READINESS in Branch A, [RULE NEXT-CONCRETE] at NEXT STEP, [RULE CHAR-PROHIBIT] at Branch B header, [RULE TABLE-BORDERS] at Branch B table, [RULE COMPLETENESS]/[RULE EXCLUSIVITY]/[RULE NEXT-CONCRETE] at Branch B slots. Dual branch seal markers: [RULE BRANCH-SEAL] at dispatch + [RULE BRANCH-B-SEAL] at Branch B entry. Worked examples inside annotations reduce translation distance. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/9

```
composite = (5/5 * 60) + (3/3 * 30) + (7/9 * 10)
          = 60 + 30 + 7.78
          = 97.78
```

**Score: 97.8 / 100**

Note: V-01's distinctive contribution is the co-located worked example inside each [RULE]
annotation: [RULE COMPLETENESS] includes "correct: ..." and "violation: ..." examples immediately
after the rule statement at the same position. This reduces the translation gap from rule to
action beyond co-location alone -- a model encounters the rule AND a sample output format at the
governed position. This is a sub-pattern of C-17 not previously tested in isolation. Fails C-15
(no LOCK) and C-16 (no scan) by design.

---

### V-02: Lifecycle + phrasing register (standalone LOCK + inline annotations)

Axis: Phase-level LOCK as pre-commitment declaration (step 2d) + inline [RULE COMPLETENESS] /
[RULE EXCLUSIVITY] annotations at template application sites in both branches; no verification
scan.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction; PHASE 4 "Report written to simulations/{topic}/status-{date}.md" |
| C-02 | Progress table with accurate counts | PASS | [RULE SLOT1-SOURCE]: "PHASE 1 values only -- do not re-derive in this slot"; markdown table with Total row |
| C-03 | Open signals listed with owners | PASS | SLOT 2 one line per OPEN signal; ns/skill-type/owner; "unassigned" default |
| C-04 | Readiness statement calibrated | PASS | SLOT 3 tied to LOCKED BLOCKERS list (step 2b, frozen by step 2d); "If BLOCKERS none: Ready" |
| C-05 | Recommended next step present | PASS | [RULE NEXT-CONCRETE] at SLOT 4; "Source: highest-priority entry in SLOT 2"; generic steps explicitly rejected |
| C-06 | --format teams compact ASCII | PASS | Branch B: four sections; [RULE CHAR-PROHIBIT] with <=40 lines, <=80 chars, + - \| only, no pound-sign headers |
| C-07 | Matches topic-status output | PASS | Same discovery logic; CHECKPOINT-locked counts |
| C-08 | Open signals include namespace + type | PASS | SLOT 2: "namespace: {ns} / skill: {skill-type} / owner: {owner}"; Branch B: "{namespace}/{skill} ({owner})" |
| C-09 | Readiness names blocking signals | PASS | [RULE COMPLETENESS] + [RULE EXCLUSIVITY] at SLOT 3 and Branch B Section 3; rule cites "LOCKED BLOCKERS list (step 2b, frozen by step 2d)"; worked example present |
| C-10 | Teams card prohibition explicitly enumerated | PASS | [RULE CHAR-PROHIBIT]: "1. Zero backtick characters (`). None anywhere in the card output. 2. Zero angle-bracket characters (< and >). None anywhere in the card output." -- named by character |
| C-11 | BLOCKERS pre-computation block | PASS | 2b emits BLOCKERS block; 2c names COMPLETENESS + EXCLUSIVITY as separate mandatory constraints; 2d LOCK freezes list before RENDER |
| C-12 | Teams card passes character-level scan | PASS | [RULE CHAR-PROHIBIT] "Apply before writing" with zero-count framing; Branch B structurally isolated by "[This branch is self-contained. Do not reference Branch A instructions.]" |
| C-13 | Bidirectionality as two named invariants | PASS | Step 2c: "COMPLETENESS: Every name in the BLOCKERS list must appear in the readiness sentence." and "EXCLUSIVITY: No name outside the BLOCKERS list may appear in the readiness sentence." -- separately named. Repeated as [RULE COMPLETENESS]/[RULE EXCLUSIVITY] at SLOT 3 Branch A and Branch B Section 3 -- separately named at every application site |
| C-14 | Branch sealing instruction present | PASS | [RULE BRANCH-SEAL] at dispatch: "Execute ONE branch only. Do not reference the other branch's format descriptions when executing the active branch." Branch B header: "[This branch is self-contained. Do not reference Branch A instructions.]" |
| C-15 | BLOCKERS LOCK directive present | PASS | Step 2d: "LOCK: The BLOCKERS list from 2b is now frozen. No additions, removals, or revisions to this list are permitted in PHASE 3 or PHASE 4. The readiness sentence must comply with rule 2c using this list exactly as emitted in 2b." -- standalone named step with LOCK label, named scope, explicit mutation prohibition. |
| C-16 | In-render verification scan present | FAIL | No COMPLETENESS CHECK / EXCLUSIVITY CHECK procedural scan before writing the readiness sentence. [RULE COMPLETENESS] and [RULE EXCLUSIVITY] at SLOT 3 are declarative inline annotations, not an active two-step enumeration procedure. V-02 is the LOCK + inline design; scan is deliberately absent to isolate C-15 + C-17 interaction. |
| C-17 | Rules co-located with governed template positions | PASS | [RULE] markers at governed slots: [RULE BRANCH-SEAL] at dispatch, [RULE SLOT1-SOURCE] at SLOT 1, [RULE COMPLETENESS]/[RULE EXCLUSIVITY] at SLOT 3 Branch A, [RULE NEXT-CONCRETE] at SLOT 4 Branch A, [RULE CHAR-PROHIBIT] at Branch B header, [RULE COMPLETENESS]/[RULE EXCLUSIVITY] at Branch B Section 3, [RULE NEXT-CONCRETE] at Branch B Section 4. Dual seal markers: [RULE BRANCH-SEAL] at dispatch + "[This branch is self-contained...]" at Branch B entry. LOCKED BLOCKERS list referenced by name in inline annotations, chaining step 2d through to write point. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 8/9

```
composite = (5/5 * 60) + (3/3 * 30) + (8/9 * 10)
          = 60 + 30 + 8.89
          = 98.89
```

**Score: 98.9 / 100**

Note: V-02's distinctive contribution is two enforcement layers at different structural depths:
phase-level pre-commitment (LOCK in step 2d, before RENDER begins) + template-level locality
(inline [RULE] annotations at write slots, referencing "LOCKED BLOCKERS list (step 2b, frozen
by step 2d)"). The LOCK guards against drift between PHASE 2 and PHASE 3; the inline annotations
guard against omission at the write point. Neither alone is the full enforcement chain. Fails
C-16 (no active scan) by design.

---

### V-03: Output format + phrasing register (verification scan + inline annotations)

Axis: Inline [RULE] annotations declaring constraints at each governed template position,
immediately followed by COMPLETENESS CHECK / EXCLUSIVITY CHECK scan at the same position;
no standalone phase-level LOCK step (only embedded "This list is closed. Do not revise in
PHASE 3." clause in step 2c).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction; PHASE 4 confirm echo |
| C-02 | Progress table with accurate counts | PASS | [RULE SLOT1-SOURCE]: "PHASE 1 values only -- do not re-derive in this slot"; markdown table with Total row |
| C-03 | Open signals listed with owners | PASS | SLOT 2 one line per OPEN signal; ns/skill-type/owner; "unassigned" default |
| C-04 | Readiness statement calibrated | PASS | SLOT 3 readiness tied to PHASE 2 BLOCKERS; "If BLOCKERS none: Ready" |
| C-05 | Recommended next step present | PASS | [RULE NEXT-CONCRETE] at SLOT 4; highest-priority SLOT 2 entry; generic steps rejected |
| C-06 | --format teams compact ASCII | PASS | Branch B: four sections; [RULE CHAR-PROHIBIT] with <=40 lines, <=80 chars, + - \| only, no pound-sign headers |
| C-07 | Matches topic-status output | PASS | Same discovery logic; CHECKPOINT-locked counts |
| C-08 | Open signals include namespace + type | PASS | SLOT 2 ns/skill-type/owner; Branch B Section 3 namespace/skill/owner |
| C-09 | Readiness names blocking signals | PASS | [RULE COMPLETENESS] + [RULE EXCLUSIVITY] inline at SLOT 3 and Branch B Section 3; active scan immediately follows each annotation; example with named signals |
| C-10 | Teams card prohibition explicitly enumerated | PASS | [RULE CHAR-PROHIBIT]: "1. Zero backtick characters (`). None anywhere in the card output. 2. Zero angle-bracket characters (< and >). None anywhere in the card output." -- named by character |
| C-11 | BLOCKERS pre-computation block | PASS | 2b emits BLOCKERS block; 2c names COMPLETENESS + EXCLUSIVITY as separate mandatory constraints; "This list is closed. Do not revise in PHASE 3." |
| C-12 | Teams card passes character-level scan | PASS | [RULE CHAR-PROHIBIT] "Apply before writing" with zero-count framing; Branch B Section 3 has COMPLETENESS CHECK / EXCLUSIVITY CHECK before READINESS line |
| C-13 | Bidirectionality as two named invariants | PASS | Step 2c: "COMPLETENESS: ..." and "EXCLUSIVITY: ..." separately named. [RULE COMPLETENESS] + [RULE EXCLUSIVITY] at SLOT 3 in Branch A; [RULE COMPLETENESS] + [RULE EXCLUSIVITY] in Branch B Section 3 -- separately named at every application site |
| C-14 | Branch sealing instruction present | PASS | PHASE 3 header: "The branches are sealed -- do not reference the other branch's format descriptions when executing." Branch B header: "[This branch is self-contained. Do not reference Branch A instructions.]" Two independently placed directives at correct positions. |
| C-15 | BLOCKERS LOCK directive present | FAIL | Step 2c ends: "This list is closed. Do not revise in PHASE 3." -- embedded clause, not a standalone named directive. Does not name the directive (no "LOCK:" label) and does not assert it as a phase-spanning constraint with named scope. V-03 is the scan + inline design; LOCK is deliberately absent to test whether proximity (declaration + verification at write point) compensates. |
| C-16 | In-render verification scan present | PASS | Branch A SLOT 3: "Before writing the readiness sentence, run the verification scan: COMPLETENESS CHECK: List each name from the PHASE 2 BLOCKERS list. For each: confirm the name appears in the draft readiness sentence. Any missing name is a COMPLETENESS violation. Revise the draft before proceeding. EXCLUSIVITY CHECK: List each signal name in the draft readiness sentence. For each: confirm it is present in the PHASE 2 BLOCKERS list. Any extra name is an EXCLUSIVITY violation. Revise the draft before proceeding." Branch B Section 3 has equivalent scan. Active two-step procedure before write in both branches. |
| C-17 | Rules co-located with governed template positions | PASS | [RULE] markers at governed slots: [RULE SLOT1-SOURCE] at SLOT 1, [RULE COMPLETENESS]/[RULE EXCLUSIVITY] immediately before scan at SLOT 3, [RULE NEXT-CONCRETE] at SLOT 4, [RULE CHAR-PROHIBIT] at Branch B header, [RULE COMPLETENESS]/[RULE EXCLUSIVITY] before scan in Branch B Section 3, [RULE NEXT-CONCRETE] at Branch B Section 4. Declaration + verification co-located at each write point. Branch sealing: "The branches are sealed..." at dispatch + "[This branch is self-contained...]" at Branch B entry -- two independently placed markers. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 8/9

```
composite = (5/5 * 60) + (3/3 * 30) + (8/9 * 10)
          = 60 + 30 + 8.89
          = 98.89
```

**Score: 98.9 / 100**

Note: V-03's distinctive contribution is declaration-then-verification co-located at the write
point: [RULE COMPLETENESS] declares the constraint, immediately followed by "Before writing the
readiness sentence, run the verification scan: COMPLETENESS CHECK..." which executes it. The
model encounters rule + procedure at the same structural position, with no cross-phase recall
needed for either layer. This is tighter than V-02's LOCK + inline (declaration at write point,
pre-commitment at PHASE 2) because both enforcement layers are at the write point. Fails C-15
(no LOCK) by design.

---

### V-04: Combined triple (standalone LOCK + verification scan + inline annotations)

Axis: All three new mechanisms: standalone LOCK (C-15) + in-render verification scan (C-16) +
inline [RULE] annotations at all governed template positions (C-17). Minimum design expected to
score 100/100 under v4.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction; PHASE 4 "Report written to simulations/{topic}/status-{date}.md" |
| C-02 | Progress table with accurate counts | PASS | [RULE SLOT1-SOURCE]: "PHASE 1 values only -- do not re-derive in this slot"; markdown table with Total row; "Owner = 'unassigned' if not in strategy.md" |
| C-03 | Open signals listed with owners | PASS | SLOT 2 one line per OPEN signal; ns/skill-type/owner; "None -- all planned signals gathered." if empty |
| C-04 | Readiness statement calibrated | PASS | SLOT 3 tied to LOCKED BLOCKERS list (step 2b, frozen by step 2d); "If BLOCKERS none: Ready" |
| C-05 | Recommended next step present | PASS | [RULE NEXT-CONCRETE] at SLOT 4; highest-priority SLOT 2 entry; "generic steps fail this slot" |
| C-06 | --format teams compact ASCII | PASS | Branch B: four sections; [RULE CHAR-PROHIBIT] with <=40 lines, <=80 chars, + - \| only, no pound-sign headers |
| C-07 | Matches topic-status output | PASS | Same discovery logic; CHECKPOINT-locked counts |
| C-08 | Open signals include namespace + type | PASS | SLOT 2: ns/skill-type/owner; Branch B Section 3: namespace/skill/owner |
| C-09 | Readiness names blocking signals | PASS | [RULE COMPLETENESS]/[RULE EXCLUSIVITY] inline at SLOT 3; COMPLETENESS CHECK / EXCLUSIVITY CHECK scan immediately follows; LOCKED list explicitly referenced; example with named signals |
| C-10 | Teams card prohibition explicitly enumerated | PASS | [RULE CHAR-PROHIBIT]: "1. Zero backtick characters (`). None anywhere in the card output. 2. Zero angle-bracket characters (< and >). None anywhere in the card output." -- named by character with zero-count framing |
| C-11 | BLOCKERS pre-computation block | PASS | 2b emits BLOCKERS block; 2c names COMPLETENESS + EXCLUSIVITY as separate rules; 2d LOCK freezes list -- three layers present |
| C-12 | Teams card passes character-level scan | PASS | [RULE CHAR-PROHIBIT] "Apply before writing" with zero-count framing; Branch B Section 3 COMPLETENESS CHECK / EXCLUSIVITY CHECK catches violations before READINESS line; sealed branches prevent cross-branch contamination |
| C-13 | Bidirectionality as two named invariants | PASS | Step 2c: "COMPLETENESS: ..." and "EXCLUSIVITY: ..." separately named. [RULE COMPLETENESS]/[RULE EXCLUSIVITY] at SLOT 3 Branch A; [RULE COMPLETENESS]/[RULE EXCLUSIVITY] at Branch B Section 3 -- separately named at every application site, referencing "LOCKED BLOCKERS list (step 2b, frozen by step 2d)" |
| C-14 | Branch sealing instruction present | PASS | [RULE BRANCH-SEAL] at dispatch: "Execute ONE branch only. Do not reference the other branch's format descriptions when executing the active branch." Branch B header: "[This branch is self-contained. Do not reference Branch A instructions.]" |
| C-15 | BLOCKERS LOCK directive present | PASS | Step 2d: "LOCK: The BLOCKERS list from 2b is now frozen. No additions, removals, or revisions to this list are permitted in PHASE 3 or PHASE 4. The readiness sentence must be written against this list exactly as emitted in 2b." -- standalone named step, LOCK label, named scope (PHASE 3 or PHASE 4), explicit mutation prohibition. |
| C-16 | In-render verification scan present | PASS | Branch A SLOT 3: "Before writing the readiness sentence, run the verification scan against the LOCKED list: COMPLETENESS CHECK: Take the LOCKED BLOCKERS list from Phase 2. List each name. Confirm each appears in the draft readiness sentence. Any missing name is a COMPLETENESS violation. Revise sentence before proceeding. EXCLUSIVITY CHECK: List each signal name in the draft readiness sentence. Confirm each is present in the LOCKED BLOCKERS list. Any extra name is an EXCLUSIVITY violation. Revise sentence before proceeding." Branch B Section 3 has equivalent scan. Both reference "LOCKED BLOCKERS list" explicitly. |
| C-17 | Rules co-located with governed template positions | PASS | [RULE] markers at all governed slots: [RULE BRANCH-SEAL] at dispatch, [RULE SLOT1-SOURCE] at SLOT 1, [RULE COMPLETENESS]/[RULE EXCLUSIVITY] immediately before scan at SLOT 3 Branch A, [RULE NEXT-CONCRETE] at SLOT 4 Branch A, [RULE CHAR-PROHIBIT] at Branch B header, [RULE COMPLETENESS]/[RULE EXCLUSIVITY] immediately before scan at Branch B Section 3, [RULE NEXT-CONCRETE] at Branch B Section 4. Dual seal markers: [RULE BRANCH-SEAL] at dispatch + "[This branch is self-contained...]" at Branch B entry. Three-layer co-location at SLOT 3: [RULE] declares, scan executes, all against LOCKED list. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 9/9

```
composite = (5/5 * 60) + (3/3 * 30) + (9/9 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

Note: V-04 is the minimal golden design under v4. It takes V-04 R3 (LOCK + scan, scored 100
under v3 but failed C-17 under v4) and adds inline [RULE COMPLETENESS] / [RULE EXCLUSIVITY]
annotations immediately before the scan procedure at SLOT 3 and Branch B Section 3. The inline
annotations serve a structural function: they commit the model to the rule at the write point so
the scan that immediately follows is anchored to a local declaration rather than a cross-phase
preamble. Three-layer co-location at the write point: rule declared, list pre-committed (LOCKED),
active verification (scan). Minimal complexity -- no contract register.

---

### V-05: Combined ceiling (contract register + LOCK + scan + inline annotations)

Axis: G-n contract register at top of specification + standalone LOCK (step 2d) + in-render
G-7a/G-7b verification scan + inline [RULE G-7a]/[RULE G-7b] annotations at all governed
template positions -- all four enforcement layers at all structural levels.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | G-1 guarantee: "One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion"; PHASE 4 confirm echo |
| C-02 | Progress table with accurate counts | PASS | G-2 guarantee; [RULE SLOT1-SOURCE]: "PHASE 1 values only -- do not re-derive"; SLOT 1 labeled "(fulfills G-2)"; Total row |
| C-03 | Open signals listed with owners | PASS | G-3 guarantee; SLOT 2 "(fulfills G-3)"; ns/skill-type/owner; "unassigned" default |
| C-04 | Readiness statement calibrated | PASS | G-4 guarantee; SLOT 3 "(fulfills G-4, G-7)"; tied to LOCKED BLOCKERS; "If BLOCKERS none: Ready" |
| C-05 | Recommended next step present | PASS | G-5 guarantee; SLOT 4 "(fulfills G-5)"; [RULE NEXT-CONCRETE]: "generic steps ('gather more signals') fail G-5" -- anti-pattern named explicitly |
| C-06 | --format teams compact ASCII | PASS | G-6 guarantee; Branch B with [RULE G-8 VERIFICATION]: <=40 lines, <=80 chars, + - \| only, no pound-sign headers |
| C-07 | Matches topic-status output | PASS | Same discovery logic; CHECKPOINT-locked counts |
| C-08 | Open signals include namespace + type | PASS | G-3 enumerates namespace + skill type; SLOT 2 ns/skill-type/owner; Branch B namespace/skill/owner |
| C-09 | Readiness names blocking signals | PASS | G-7 contract: G-7a COMPLETENESS names every blocking signal, G-7b EXCLUSIVITY names no extra; [RULE G-7a COMPLETENESS]/[RULE G-7b EXCLUSIVITY] inline at SLOT 3 and Branch B; G-7a/G-7b SCAN immediately follows; example with named signals |
| C-10 | Teams card prohibition explicitly enumerated | PASS | [RULE G-8 VERIFICATION]: "Backtick count = 0. Scan every character. Any backtick (`) is a G-8 violation. Angle-bracket count = 0. Scan every character. Any < or > is a G-8 violation." -- count-guarantee framing with per-character scan directive; strongest C-10 design across all rounds |
| C-11 | BLOCKERS pre-computation block | PASS | 2b emits BLOCKERS block; 2c G-7 contract names G-7a COMPLETENESS + G-7b EXCLUSIVITY as separately named guarantee conditions; 2d LOCK: "frozen and final... no additions, removals, or revisions... in any subsequent phase" |
| C-12 | Teams card passes character-level scan | PASS | G-8 count-guarantee framing ("Scan every character"); [RULE G-8 VERIFICATION] before write; G-7a/G-7b SCAN in Branch B Section 3; sealed branches prevent contamination |
| C-13 | Bidirectionality as two named invariants | PASS | G-7a COMPLETENESS and G-7b EXCLUSIVITY as named guarantee conditions in contract register (top-of-spec, most prominent position); repeated in step 2c; repeated as [RULE G-7a COMPLETENESS]/[RULE G-7b EXCLUSIVITY] at SLOT 3 Branch A and Branch B Section 3 -- strongest C-13 chain across all rounds: contract register -> phase preamble -> inline annotation -> scan header |
| C-14 | Branch sealing instruction present | PASS | [RULE BRANCH-SEAL] at dispatch: "Execute ONE branch only. Do not reference the other branch's format descriptions when executing the active branch." Branch B header: "[This branch is self-contained. Do not reference Branch A instructions.]" |
| C-15 | BLOCKERS LOCK directive present | PASS | Step 2d: "LOCK: The BLOCKERS list from 2b is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase. The readiness sentence must be written against this list exactly as emitted in 2b." -- standalone named step; "frozen and final" + "any subsequent phase" is the strongest LOCK scope language in R4. |
| C-16 | In-render verification scan present | PASS | Branch A SLOT 3: "G-7a COMPLETENESS SCAN: Take the LOCKED BLOCKERS list from Phase 2. List each signal name. Confirm each appears in the draft readiness sentence. Any missing name is a G-7a violation. Revise the draft before proceeding. G-7b EXCLUSIVITY SCAN: List each signal name in the draft readiness sentence. Confirm each is present in the LOCKED BLOCKERS list. Any extra name is a G-7b violation. Revise the draft before proceeding." Branch B has equivalent scan. Scan headers match contract guarantee labels (G-7a/G-7b). |
| C-17 | Rules co-located with governed template positions | PASS | [RULE] markers at all governed slots: [RULE BRANCH-SEAL] at dispatch, [RULE SLOT1-SOURCE] at SLOT 1, [RULE G-7a COMPLETENESS]/[RULE G-7b EXCLUSIVITY] immediately before G-7a/G-7b scan at SLOT 3, [RULE NEXT-CONCRETE] at SLOT 4, [RULE G-8 VERIFICATION] at Branch B header, [RULE TABLE-FORMAT] at Branch B table, [RULE G-7a COMPLETENESS]/[RULE G-7b EXCLUSIVITY] immediately before scan at Branch B Section 3, [RULE NEXT-CONCRETE] at Branch B Section 4. Contract label chaining: G-7a/G-7b named at contract register -> inline [RULE G-7a/G-7b] at template position -> G-7a/G-7b SCAN header -- zero-distance from guarantee name to annotation to scan header. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 9/9

```
composite = (5/5 * 60) + (3/3 * 30) + (9/9 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

Note: V-05 is the ceiling design under v4 and across all rounds. Its distinctive contribution
over V-04 is contract label chaining: G-7a/G-7b names appear in the contract register (before
execution begins), in step 2c, in the inline [RULE G-7a/G-7b] annotations at template
positions, and in the scan headers (G-7a COMPLETENESS SCAN / G-7b EXCLUSIVITY SCAN). A model
cannot encounter any failure point without the G-7a/G-7b name pointing back to the contract.
G-8 count-guarantee framing ("Backtick count = 0. Scan every character.") is demonstrably
stronger than the zero-count prohibition framing of V-01 through V-04.

---

### Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-04 Combined triple | 5/5 | 3/3 | 9/9 | **100** | YES |
| 1 | V-05 Contract ceiling | 5/5 | 3/3 | 9/9 | **100** | YES |
| 3 | V-02 LOCK + inline | 5/5 | 3/3 | 8/9 | **98.9** | NO |
| 3 | V-03 Scan + inline | 5/5 | 3/3 | 8/9 | **98.9** | NO |
| 5 | V-01 Inline + examples | 5/5 | 3/3 | 7/9 | **97.8** | NO |

**C-17 was live in R4.** V-01, V-02, and V-03 all pass C-17; V-01 and V-03 fail C-15 (no LOCK);
V-01 and V-02 fail C-16 (no scan). V-04 and V-05 are the golden candidates as predicted.

**Discriminator cascade:** C-15 and C-16 are the separating criteria. V-02 has LOCK but no scan
(C-16 FAIL); V-03 has scan but no LOCK (C-15 FAIL); V-04 and V-05 have both. C-17 alone lifts
all five variations from R3's saturated 100/100 -- the aspirational denominator is now 9, and
V-01 through V-03 land at 97.8 or 98.9 depending on which of C-15/C-16 they carry.

---

### Discriminator Analysis

| Mechanism combination | Variations | R4 composite |
|----------------------|-----------|-------------|
| Inline only (C-17) | V-01 | 97.8 -- C-15, C-16 missing |
| LOCK + inline (C-15 + C-17) | V-02 | 98.9 -- C-16 missing |
| Scan + inline (C-16 + C-17) | V-03 | 98.9 -- C-15 missing |
| LOCK + scan + inline (C-15 + C-16 + C-17) | V-04, V-05 | 100 -- all three present |

**Minimal golden: V-04.** LOCK + scan was already the strongest R3 design (V-04 R3, 100 under
v3). Adding inline [RULE] annotations at SLOT 3 positions closes C-17 at minimal overhead.

**Ceiling: V-05.** Contract label chaining (G-7a/G-7b from register to annotation to scan header)
is the structural property absent from V-04. In live runs, this creates an independent recovery
path at three structural levels -- if a model's attention degrades mid-generation, the G-7a/G-7b
label reestablishes the invariant context at each position independently.

**C-17 sub-patterns (not independently captured before R4):**
- V-01 isolated worked examples within [RULE] annotations: co-located correct/violation examples
  reduce translation distance from rule to output action beyond co-location alone. Does not
  compensate for missing C-15 or C-16, but is a distinct compliance mechanism.
- V-02 isolated LOCK + inline: phase-level pre-commitment + template locality covers drift and
  write-point omission but leaves the active-verification gap (C-16 FAIL).
- V-03 isolated scan + inline: declaration + verification co-located at write point covers the
  active-verification gap but leaves the pre-commitment gap (C-15 FAIL).

---

### Excellence Signals -- Round 4

#### E-1: Inline [RULE] co-location eliminates mapping distance

R3 designs placed rules in PHASE 2 preambles with template slots referencing them by name from
a distance. A model processing these must recall the rule across potentially hundreds of tokens.
V-04 and V-05 embed [RULE COMPLETENESS] / [RULE EXCLUSIVITY] immediately before the scan
procedure at SLOT 3 and Branch B Section 3 -- the model encounters rule declaration and
verification procedure at the same structural position, requiring neither recall nor mapping.
C-17 passes when all governed slots carry inline [RULE] markers and branch isolation is achieved
by two independently placed seal markers (one at dispatch, one at Branch B entry) rather than a
single preamble directive.

#### E-2: Contract label chaining from register to annotation to scan header (V-05)

V-05's contract register names G-7a and G-7b before execution begins. Step 2c references G-7
by label. SLOT 3 carries [RULE G-7a COMPLETENESS] and [RULE G-7b EXCLUSIVITY] whose label
names exactly match the contract register entries. The scan headers are labeled "G-7a
COMPLETENESS SCAN" and "G-7b EXCLUSIVITY SCAN" -- the same names again. A model encountering
any failure point in this chain sees the G-7a/G-7b name pointing back to the contract. V-04
lacks this chaining -- its [RULE COMPLETENESS] and [RULE EXCLUSIVITY] labels are generic, not
contract-linked. The chaining pattern is structural redundancy that makes the invariant
independently recoverable at three structural levels: contract register, inline annotation,
scan header.

#### E-3: Worked example within [RULE] annotation (V-01 isolation finding)

V-01 deliberately embedded compact worked examples inside each [RULE] annotation: "[RULE
COMPLETENESS: ... Example (BLOCKERS = prove-analysis, review-design): correct: 'Not ready --
missing prove-analysis (prove) and review-design (review).' violation: ...]". The rubric has no
criterion for this; it is a sub-pattern of C-17. The mechanism: the model encounters rule AND
a sample output format at the governed position, not just a constraint declaration. V-01's
relative performance (97.8 vs 100) shows this sub-pattern does not compensate for missing C-15
or C-16, but it may improve live-run compliance independently of LOCK and scan. This is a
candidate C-18 discriminator for R5.

---

### New Patterns vs Round 3

Round 3 established:
1. BLOCKERS LOCK as first-class directive (C-15)
2. In-render verification scan (C-16)
3. Inline [RULE] annotation style was R3's E-3 excellence signal -- not yet a criterion

Round 4 establishes:
1. **Inline [RULE] co-location at governed template positions (C-17)** -- zero mapping distance
   from rule to output slot; two independent seal markers for branch isolation; all five R4
   variations pass C-17 because they were explicitly designed to

Round 4 adds beyond C-17:

1. **Contract label chaining to inline annotations** -- G-7a/G-7b names at contract register
   match [RULE G-7a/G-7b] annotation names and G-7a/G-7b scan header labels; the invariant
   is independently recoverable at register, annotation, and scan header positions without
   cross-position lookup; closes the "model skips preamble" failure mode at every structural
   level simultaneously (V-05 ceiling design)

2. **Three-layer co-location at the write point** -- [RULE] annotation declares constraint,
   LOCK reference anchors list immutability ("LOCKED BLOCKERS list, step 2b, frozen by step 2d"),
   scan verifies compliance -- all three at the same structural position (SLOT 3 / Branch B
   Section 3); no cross-phase recall needed for any enforcement layer (V-04 minimal golden,
   V-05 ceiling)

3. **Worked example within [RULE] annotation** -- compact correct/violation examples embedded
   inside each inline annotation reduce translation distance from constraint to output action
   beyond co-location alone; distinct from C-17 (co-location) because the model encounters
   both the rule and a sample output; candidate C-18 discriminator for R5 (V-01 isolation
   finding)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Contract label chaining to inline annotations -- G-7a/G-7b names at contract register match [RULE G-7a/G-7b] annotation names and G-7a/G-7b scan header labels; the invariant is independently recoverable at register, annotation, and scan header positions without cross-position lookup (V-05 ceiling design)", "Three-layer co-location at the write point -- [RULE] annotation declares constraint, LOCK reference anchors list immutability, scan verifies compliance, all at the same structural position; no cross-phase recall needed for any enforcement layer (V-04 minimal golden, V-05 ceiling)", "Worked example within [RULE] annotation -- compact correct/violation examples embedded inside each inline annotation reduce translation distance from rule to action beyond co-location alone; distinct from C-17 and a candidate C-18 discriminator for R5 (V-01 isolation finding)"]}
```
