## simulate-argument — Round 2 Score

### Results

| Rank | Variation | Score | Golden | C-13 |
|------|-----------|-------|--------|------|
| 1 (T) | V-03 Taxonomy | **100** | YES | PASS |
| 1 (T) | V-04 Sub-passes + hooks | **100** | YES | PASS |
| 1 (T) | V-05 All mechanisms | **100** | YES | PASS |
| 4 (T) | V-01 Phase 0 depth | 98 | YES | FAIL |
| 4 (T) | V-02 Hook scale | 98 | YES | FAIL |

### Why V-01 and V-02 miss C-13

Both pass 4/5 aspirationals. The failure:

- **V-01** Phase 4 closes by confirming/refuting the "full-soundness condition" from Phase 0 — a Phase 0 reference check, not a fault class synthesis. No class name required by the prompt.
- **V-02** Phase 4 closes by naming "the dominant reviewer depth tier (SIGNIFICANT/NOTABLE/OBVIOUS)" — a depth/severity scale, not a fault class (definitional drift, unsupported generalization, etc.). Wrong vocabulary for C-13.

### New patterns from top-scoring cluster

1. **Enumerated fault taxonomy** (V-03, V-05): A `Class` column with four fixed codes converts C-13 from judgment-dependent to mechanical — model classifies at insertion, Phase 4 counts rows.

2. **Explicit fault-class naming in Phase 4 closure** (V-04): Even without a taxonomy column, instructing Phase 4 to "name the dominant fault class (e.g., definitional drift...)" using rubric vocabulary is sufficient. Free-form + examples > Phase 0 confirmation check.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["enumerated-fault-taxonomy: adding a Class column with four enumerated codes (DEF-DRIFT/UNSUPPORTED-GEN/CIRCULAR-DEP/INVALID-FORM) converts C-13 from judgment-dependent to mechanical — model classifies at insertion time, Phase 4 closure counts rows rather than inventing a label", "fault-class-naming-in-closure: Phase 4 closing must explicitly name the dominant fault class using structural vocabulary (definitional drift, unsupported generalization, etc.) — naming a depth tier or confirming Phase 0 without a class name is insufficient for C-13"]}
```
n target stated      PASS   [Strongest C-11: structured 3-part Phase 0 (Central claim / Load-bearing premises / Full-soundness condition); Phase 4 must "reference that condition explicitly"]
C-12 inline reviewer hook present     PASS   [Inside STEP block for every WEAK/BROKEN: "Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification"]
C-13 fault pattern closure            FAIL   [Phase 4 closing asks "confirm or refute the full-soundness condition?" but does NOT require naming a dominant fault class — C-13 pass requires naming the class, not just referencing Phase 0]

essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 4/5

composite = (5/5 * 60) + (3/3 * 30) + (4/5 * 10)
composite = 60 + 30 + 8 = 98

golden = YES
```

---

### V-02 — Inline Hook Scoring Scale

```
C-01 claim map present/populated      PASS   [Phase 2: identical claim map structure]
C-02 dependency graph complete        PASS   [Same dependency instructions]
C-03 section coverage satisfied       PASS   [Same section coverage instruction]
C-04 every inference step traced      PASS   [STEP block: logical form + 3 validity checks + verdict; reviewer depth scale is additive, not substituted]
C-05 fault register matches verdicts  PASS   [Phase 4 Gap carries tier tag; table structure unchanged]

C-06 logical forms named              PASS   [STEP block retains "Logical form:" with enumerated list]
C-07 AMEND ordered + actionable       PASS   [P1→P2→P3 with F-ID + C-ID + exact repair specification]
C-08 artifact frontmatter complete    PASS   [All 6 fields present]

C-09 term drift detected              PASS   [Validity check retains DRIFT format; AMEND P3 requires originating C-ID + stable wording]
C-10 structural weakness exposed      PASS   [Strongest C-10: OBVIOUS/NOTABLE/SIGNIFICANT scale forces non-obviousness classification; domain comparison sentence required in STEP block and tier tag required in Fault Register Gap field]
C-11 falsification target stated      PASS   [Simple Phase 0 paragraph present; Phase 4 closing: "does the fault pattern confirm or refute the PHASE 0 best-case framing?"]
C-12 inline reviewer hook present     PASS   [Strongest C-12: STEP block has "Reviewer depth: [OBVIOUS/NOTABLE/SIGNIFICANT]" + "Domain comparison: [one sentence]" — richer than binary hook]
C-13 fault pattern closure            FAIL   [Phase 4 closing names "dominant reviewer depth tier (SIGNIFICANT/NOTABLE/OBVIOUS)" — a severity scale, not a fault class; C-13 pass condition requires naming the fault class (definitional drift, unsupported generalization, etc.)]

essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 4/5

composite = (5/5 * 60) + (3/3 * 30) + (4/5 * 10)
composite = 60 + 30 + 8 = 98

golden = YES
```

---

### V-03 — Fault Taxonomy Enforcement

```
C-01 claim map present/populated      PASS   [Phase 2: identical claim map]
C-02 dependency graph complete        PASS   [Same dependency instructions]
C-03 section coverage satisfied       PASS   [Same section coverage]
C-04 every inference step traced      PASS   [Standard STEP block with all 3 checks + verdict; single-pass format without 3A/3B/3C gating]
C-05 fault register matches verdicts  PASS   [Phase 4: Class column does not change verdict-coverage completeness requirement]

C-06 logical forms named              PASS   [STEP block: "Logical form: [name the structure...]" with enumerated examples]
C-07 AMEND ordered + actionable       PASS   [P1→P2→P3 with F-ID + C-ID; exact repair specification retained]
C-08 artifact frontmatter complete    PASS   [All 6 fields present]

C-09 term drift detected              PASS   [DRIFT format in validity check; AMEND P3 names originating C-ID; Class column (DEF-DRIFT) captures at register time]
C-10 structural weakness exposed      PASS   [Binary hook present; Class taxonomy forces structural categorization (DEF-DRIFT vs UNSUPPORTED-GEN vs CIRCULAR-DEP vs INVALID-FORM) rather than generic "inference is weak"]
C-11 falsification target stated      PASS   [Simple Phase 0 paragraph; Phase 4 closing: "does the fault pattern confirm or refute the PHASE 0 best-case framing?"]
C-12 inline reviewer hook present     PASS   [Standard binary hook in STEP block for WEAK/BROKEN: "Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification"]
C-13 fault pattern closure            PASS   [Strongest C-13: Class column with four enumerated codes; Phase 4 closing: "State the dominant fault class by code (most rows in the Class column)" — mechanical count, not invented label]

essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 5/5

composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
composite = 60 + 30 + 10 = 100

golden = YES
```

---

### V-04 — Combined: Sub-Passes + Phase 0 + Inline Hooks

```
C-01 claim map present/populated      PASS   [Phase 2: identical claim map]
C-02 dependency graph complete        PASS   [Same dependency instructions]
C-03 section coverage satisfied       PASS   [Same section coverage]
C-04 every inference step traced      PASS   [Strongest C-04: 3A/3B/3C gating prevents check-merging; 3B runs all 3 checks independently across ALL inferences before any verdicts issued; 3C issues verdicts after]
C-05 fault register matches verdicts  PASS   ["Every claim with WEAK or BROKEN verdict from 3C must appear here" — explicit gate]

C-06 logical forms named              PASS   [Strongest C-06: 3A dedicated exclusively to naming logical form + If/Then/Therefore skeleton across all inferences before evaluation begins; enumerated list (modus ponens / modus tollens / hypothetical syllogism / etc.)]
C-07 AMEND ordered + actionable       PASS   [P1→P2→P3 with F-ID + C-ID; "exact change needed — not 'add evidence'"]
C-08 artifact frontmatter complete    PASS   [All 6 fields present]

C-09 term drift detected              PASS   [Strongest C-09: 3B explicitly requires "DRIFT: term, definition claim C-ID, and how it shifted" — C-ID captured at check time, not retroactively; AMEND P3 same]
C-10 structural weakness exposed      PASS   [3C: "Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification" at verdict time; 3A/3B separation sharpens structural characterization]
C-11 falsification target stated      PASS   [Phase 0 paragraph; Phase 4 closing: "does the fault pattern confirm or refute the PHASE 0 best-case framing?"]
C-12 inline reviewer hook present     PASS   [3C VERDICT block: "If WEAK or BROKEN: Would a domain reviewer flag this as non-obvious? YES/NO — one sentence justification" — inside Phase 3 at verdict time]
C-13 fault pattern closure            PASS   [Phase 4 closing: "Name the dominant fault class (e.g., definitional drift, unsupported generalization, circular dependency, invalid analogy)" — examples match C-13 pass condition vocabulary; free-form but explicitly prompted]

essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 5/5

composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
composite = 60 + 30 + 10 = 100

golden = YES
```

---

### V-05 — Combined: All Mechanisms + Fault Taxonomy

```
C-01 claim map present/populated      PASS   [Phase 2: identical claim map]
C-02 dependency graph complete        PASS   [Same dependency instructions]
C-03 section coverage satisfied       PASS   [Same section coverage]
C-04 every inference step traced      PASS   [3A/3B/3C gating — same as V-04; prevents merging across all three check types]
C-05 fault register matches verdicts  PASS   ["Every claim with WEAK or BROKEN verdict from 3C must appear here" — same explicit gate]

C-06 logical forms named              PASS   [3A dedicated pass — same as V-04; strongest C-06 enforcement in set]
C-07 AMEND ordered + actionable       PASS   [Strongest C-07: each fix references F-ID + C-ID + Class code; P3 fix: "if DEF-DRIFT, name the originating definition claim (C-ID) and propose stable replacement wording; if other class, name the exact precision gap" — taxonomy extends AMEND specificity]
C-08 artifact frontmatter complete    PASS   [All 6 fields present]

C-09 term drift detected              PASS   [3B requires DRIFT+C-ID at check time; DEF-DRIFT class in register captures at insertion; AMEND P3 references class code alongside C-ID]
C-10 structural weakness exposed      PASS   [3C reviewer hook; Class taxonomy (DEF-DRIFT/UNSUPPORTED-GEN/CIRCULAR-DEP/INVALID-FORM) forces structural categorization at insertion — prevents generic gap descriptions]
C-11 falsification target stated      PASS   [Phase 0 paragraph; Phase 4 closing references Phase 0 best-case framing explicitly]
C-12 inline reviewer hook present     PASS   [3C VERDICT block: binary hook for every WEAK/BROKEN — same as V-04]
C-13 fault pattern closure            PASS   [Strongest C-13: Class column with four enumerated codes; Phase 4 closing: "State the dominant fault class by code (most rows in the Class column)" — mechanical count, identical to V-03; no label invention required]

essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 5/5

composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
composite = 60 + 30 + 10 = 100

golden = YES
```

---

### Final Ranking

| Rank | Variation | Composite | Golden | C-13 | Distinctive Strength |
|------|-----------|-----------|--------|------|---------------------|
| 1 (T) | V-03 Taxonomy | 100 | YES | PASS | Enumerated taxonomy converts C-13 to mechanical count; simplest variation to reach 100 |
| 1 (T) | V-04 Sub-passes + hooks | 100 | YES | PASS | Strongest C-04/C-06/C-09 via 3A/3B/3C gating; free-form class naming sufficient for C-13 |
| 1 (T) | V-05 All mechanisms | 100 | YES | PASS | Maximum coverage: taxonomy + 3A/3B/3C + class code in AMEND; every criterion has a specific structural mechanism |
| 4 (T) | V-01 Phase 0 depth | 98 | YES | FAIL | Strongest C-11 (3-part structured falsification target); C-13 fails — Phase 4 closes on Phase 0 condition but does not name a fault class |
| 4 (T) | V-02 Hook scale | 98 | YES | FAIL | Strongest C-10/C-12 (OBVIOUS/NOTABLE/SIGNIFICANT depth scale + domain comparison); C-13 fails — depth tier != fault class |

---

### Why V-01 and V-02 Miss C-13

Both variations reach 4/5 aspirationals — every criterion passes except C-13.

V-01 Phase 4 closing: "does the fault pattern confirm or refute the **full-soundness condition** stated in PHASE 0? Reference that condition explicitly." This is a Phase 0 confirmation check, not a fault class synthesis. A model following V-01 will connect back to Phase 0 but may not name a dominant class.

V-02 Phase 4 closing: "Name the dominant reviewer depth tier (SIGNIFICANT/NOTABLE/OBVIOUS)." A depth tier (how hard the fault is to catch) is not a fault class (what kind of inference failure it is). C-13 pass condition uses the language "definitional drift, unsupported generalization, circular dependency" — all structural class labels, not depth tiers.

Fix: either add an enumerated Class column (V-03/V-05 approach) or add free-form fault class naming to Phase 4 closing (V-04 approach).

---

### Excellence Signals

Patterns from the top-scoring cluster (V-03, V-04, V-05) that improve on R1 V-05:

1. **Enumerated fault taxonomy as a required register column (V-03, V-05)**: Adding a `Class` column with four enumerated codes (DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM) converts C-13 from a judgment-dependent criterion to a mechanical one. The model classifies each fault at insertion time; Phase 4 closure counts rows and names the code. No invented label required. This is the minimum change needed to make C-13 reliably pass.

2. **Phase 4 closure must name the dominant fault class (V-04)**: Even without a taxonomy column, explicitly instructing Phase 4 to "Name the dominant fault class (e.g., definitional drift, unsupported generalization...)" using the same vocabulary as the rubric is sufficient for C-13. Free-form naming with examples outperforms a pure Phase 0 confirmation check.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["enumerated-fault-taxonomy: adding a Class column with four enumerated codes (DEF-DRIFT/UNSUPPORTED-GEN/CIRCULAR-DEP/INVALID-FORM) converts C-13 from judgment-dependent to mechanical — model classifies at insertion time, Phase 4 closure counts rows rather than inventing a label", "fault-class-naming-in-closure: Phase 4 closing must explicitly name the dominant fault class using structural vocabulary (definitional drift, unsupported generalization, etc.) — naming a depth tier or confirming Phase 0 without a class name is insufficient for C-13"]}
```
