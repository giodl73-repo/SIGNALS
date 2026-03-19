## discover-competitors-alt R7 — Score

**All 5 variations: 200/200 (Exceptional)**

Second consecutive ceiling round. R6 hit 180/180; R7 hits 200/200. All four new criteria (C-27–C-30) satisfied across all variations on first attempt.

### Per-criterion result
- **C-01–C-26** (inherited): PASS all five — no regressions
- **C-27** (machine-readable phase column): PASS all five — V-04 uses "Producing phase" (accepted synonym)
- **C-28** (OUTPUT CONTRACTS inside PREFLIGHT): PASS all five — position varies (first/last/middle); criterion only requires inside, not where inside
- **C-29** (full-path back-references): PASS all five — all producing phase headings use "PREFLIGHT > OUTPUT CONTRACTS"
- **C-30** (write-token in INERTIA-REF gate): PASS all five — format varies (prose+code block, bolded directive, table row); all include explicit directive + token format

### Ranking (qualitative, all tied at 200)
1. **V-05** — write-as-table-row + spec-first + 6-slot contract + contract slot named in write-row Pass condition by full path
2. **V-03** — cleanest single-axis table-row implementation with named "Inertia write failure" state
3. **V-02** — spec-first + write directive names the forward-declared slot by path
4. **V-04** — imperative register + "Producing phase" synonym confirmation
5. **V-01** — most minimal satisfying form for C-27–C-30

### Excellence signals

1. **Write-token-as-gate-row** — encoding INERTIA-REF production as a PASS/FAIL table row with a named failure state makes it independently verifiable at review time; cannot be skipped as contextual prose
2. **Spec-first PREFLIGHT** — OUTPUT CONTRACTS first in PREFLIGHT so the production target is visible before any gate logic; GATE 4 write action resolves a forward-declared slot rather than creating a token ad hoc
3. **Focus-scope evidence slot** — 6th output contract slot forward-declares the cross-dimensional proof requirement at collection time, making the synthesis obligation visible before Phase 4 runs

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["write-token-as-gate-row: encoding INERTIA-REF production as a PASS/FAIL table row with named failure state makes token production independently checkable at review time -- the write action cannot be separated from gate logic or treated as contextual prose", "spec-first PREFLIGHT: declaring OUTPUT CONTRACTS before gate logic makes the production target visible before constraints so GATE 4 write actions resolve forward-declared slots rather than producing tokens ad hoc -- the gate acts as contract fulfillment", "focus-scope evidence slot: a dedicated 6th output contract slot forward-declares the cross-dimensional proof requirement at collection time -- Phase 4 knows before it runs that it must produce scope evidence demonstrating why both dimensions are necessary"]}
```
t"; "Producing phase" is a direct synonym. INERTIA-REF row: "GATE 4 (PREFLIGHT, below)" — column correctly names both gate and its forward position. |
| V-05 | **PASS** | OUTPUT CONTRACTS table (first subsection in PREFLIGHT) is a 6-slot, 4-column table: Slot / Label / Required format / **Filled by phase**. INERTIA-REF row: "GATE 4 (Write row, below)" — column names the specific write-action row within GATE 4 and signals its forward position. The 6th slot (Focus-scope evidence) is also phase-assigned: "Phase 4 — Cross-Dimensional Finding". Maximum phase-assignment coverage across all slots. |

**C-27: PASS — all five.**

---

### C-28 — OUTPUT CONTRACTS co-located within PREFLIGHT

Pass condition: OUTPUT CONTRACTS is a named subsection within the PREFLIGHT block. A separate OUTPUT CONTRACTS section placed outside PREFLIGHT does not satisfy even if it immediately precedes Phase 1.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | PREFLIGHT section contains four named gate subsections followed by "### OUTPUT CONTRACTS" as the final subsection. "All gates are defined here. No gate appears outside this block." The OUTPUT CONTRACTS subsection appears within PREFLIGHT, after GATE 3 and before Phase 1. It is not a standalone section. |
| V-02 | **PASS** | PREFLIGHT section opens with "### OUTPUT CONTRACTS" as the first subsection, followed by GATE 1, GATE 2, GATE 3, GATE 4. PREFLIGHT block header: "All gates and output specifications are defined here. OUTPUT CONTRACTS is declared first." OUTPUT CONTRACTS is unambiguously a named subsection within PREFLIGHT. |
| V-03 | **PASS** | PREFLIGHT section contains GATE 1, GATE 2, GATE 3, GATE 4 (with write-as-table-row), then "### OUTPUT CONTRACTS" as the final subsection. Block header: "All gates and output specifications are defined here... GATE 4 includes a write action as a structural table row." Both gates and contracts are co-located within a single PREFLIGHT section. |
| V-04 | **PASS** | PREFLIGHT section contains GATE 1, GATE 2, GATE 3, then "### OUTPUT CONTRACTS" as a subsection, then GATE 4. The OUTPUT CONTRACTS subsection is positioned inside PREFLIGHT between GATE 3 and GATE 4. Block header: "All rules and output specifications are defined here. Run this block before any phase. No gate appears outside this block." |
| V-05 | **PASS** | PREFLIGHT section opens with "### OUTPUT CONTRACTS" as the first subsection (6-slot, 4-col), followed by GATE 4 (write-as-table-row), GATE 1, GATE 2, GATE 3. Block header: "All output specifications and gates are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first." OUTPUT CONTRACTS and all four gates are within the same PREFLIGHT section. |

**C-28: PASS — all five.**

---

### C-29 — Full-path back-reference labels in producing phases

Pass condition: Back-reference labels in producing phase headings name the complete navigable path to the contract declaration — "PREFLIGHT > OUTPUT CONTRACTS" rather than just "OUTPUT CONTRACTS". Criterion is only applicable when C-28 is satisfied. Since C-28 is satisfied by all five, full-path labels are required across all five.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | All four producing phase headings use the full path: "PHASE 2: COMPETITOR TABLE (fills Anchor column value — **PREFLIGHT > OUTPUT CONTRACTS**)"; "PHASE 3: WHITESPACE (fills Absence evidence block — **PREFLIGHT > OUTPUT CONTRACTS**)"; "PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — **PREFLIGHT > OUTPUT CONTRACTS**)"; "PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — **PREFLIGHT > OUTPUT CONTRACTS**)". Structural column notes within each phase also use the full path. |
| V-02 | **PASS** | All four producing phase headings: "PHASE 2: COMPETITOR TABLE (fills Anchor column value — **PREFLIGHT > OUTPUT CONTRACTS**)"; "PHASE 3: WHITESPACE (fills Absence evidence block — **PREFLIGHT > OUTPUT CONTRACTS**)"; "PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — **PREFLIGHT > OUTPUT CONTRACTS**)"; "PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — **PREFLIGHT > OUTPUT CONTRACTS**)". In-phase structural column notes repeat the full path. |
| V-03 | **PASS** | All four producing phase headings use full path. In-phase Anchor column notes: "fills Anchor column value, **PREFLIGHT > OUTPUT CONTRACTS**". INERTIA-REF-DELTA column note: "fills INERTIA-REF-DELTA, **PREFLIGHT > OUTPUT CONTRACTS** — apply GATE 4 (token written at Write row in GATE 4; must be available before this phase runs)". The write-row reference in the INERTIA-REF-DELTA column note links back to the production step within GATE 4. |
| V-04 | **PASS** | All four producing phase headings use full path: "PHASE 2: COMPETITOR TABLE (fills Anchor column value — **PREFLIGHT > OUTPUT CONTRACTS**)"; etc. Phase 4 SOURCE block: "apply **PREFLIGHT > OUTPUT CONTRACTS**, SOURCE slot format." GATE 4 write instruction itself uses the full path: "**WRITE** the INERTIA-REF slot (**PREFLIGHT > OUTPUT CONTRACTS** above) now:" — the back-reference appears at the point of token production in the gate, not only in phase headings. |
| V-05 | **PASS** | All five producing phase headings (Phase 2–5, plus GATE 4) use full path. Phase 4 heading: "PHASE 4: CROSS-DIMENSIONAL FINDING (fills Focus-scope evidence and SOURCE slot — **PREFLIGHT > OUTPUT CONTRACTS**)". Focus-scope evidence instruction: "fills Focus-scope evidence slot, **PREFLIGHT > OUTPUT CONTRACTS**". GATE 4 write-row Pass condition: "this fills the INERTIA-REF slot (**PREFLIGHT > OUTPUT CONTRACTS** above)." Most complete full-path back-reference coverage across all phases and gate rows. |

**C-29: PASS — all five.**

---

### C-30 — Write-token instruction within INERTIA-REF gate

Pass condition: The INERTIA-REF gate includes an explicit write instruction that directs the model to record the resolved token value at gate evaluation time (e.g., "Write INERTIA-REF = [specific mechanism phrase]"). A gate that only checks for presence or correctness without a write directive does not satisfy. C-30 requires the gate itself to perform the token write — binding token resolution to gate execution.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | GATE 4 prose before check table: "**Clear this gate before all others.** Identify C0 — the status quo behavior, tool, or approach the target user relies on today — then **write the INERTIA-REF token now, as the act of clearing this gate**:" followed by code block `INERTIA-REF = [C0 name]: [specific mechanism...]`. The write directive is explicit; the code block provides the required token format. Format: prose + code block. |
| V-02 | **PASS** | GATE 4 opens: "**Fill the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above).** Identify C0 — then **write the token now, as the act of clearing this gate**:" followed by code block `INERTIA-REF = [C0 name]: [specific mechanism...]`. The write directive additionally names the contract slot being filled by full path, binding the gate action to the contract. Format: prose + code block with slot reference. |
| V-03 | **PASS** | GATE 4 is a 3-row PASS/FAIL table. Second row: Check = "**Write INERTIA-REF token**"; Pass condition = "Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — this token is now available to all phases; do not defer token production"; Failure state = "**Inertia write failure** — token must be written at this gate, not defined in a later phase; return to this gate and execute the write step." Write action is a structural gate row: independently checkable with named failure state. Format: table row. |
| V-04 | **PASS** | GATE 4 prose before check table: "Identify C0 — the status quo tool, workflow, or behavior the target user relies on today. **WRITE** the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above) now:" followed by code block `INERTIA-REF = [C0 name]: [specific mechanism...]`. Bold "**WRITE**" header directive + code block. Imperative register throughout. Format: bolded directive + code block with slot reference. |
| V-05 | **PASS** | GATE 4 is a 3-row PASS/FAIL table. Second row: Check = "**Write INERTIA-REF token**"; Pass condition = "Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — **this fills the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above)**; token is now available to all phases"; Failure state = "**Inertia write failure** — token must be written at this gate, not defined in a later phase; return to this gate and execute the write step." Write-as-table-row form binds token production to gate execution; the Pass condition names the contract slot by full path. Most complete: write directive + slot reference + full path + named failure. Format: table row with contract slot reference. |

**C-30: PASS — all five.**

---

### Per-criterion summary (full)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Status quo competitor row | PASS | PASS | PASS | PASS | PASS |
| **C-02** WebSearch evidence per competitor | PASS | PASS | PASS | PASS | PASS |
| **C-03** Whitespace section present | PASS | PASS | PASS | PASS | PASS |
| **C-04** Cross-dimensional finding (competitive x focus) | PASS | PASS | PASS | PASS | PASS |
| **C-05** AMEND section present | PASS | PASS | PASS | PASS | PASS |
| **C-06** Inertia stickiness reasoning (concrete mechanism) | PASS | PASS | PASS | PASS | PASS |
| **C-07** Web-verified competitive claim (inline citation) | PASS | PASS | PASS | PASS | PASS |
| **C-08** AMEND - 3 actionable adjustments | PASS | PASS | PASS | PASS | PASS |
| **C-09** Cross-dimensional whitespace finding | PASS | PASS | PASS | PASS | PASS |
| **C-10** Table-stakes grounding per finding | PASS | PASS | PASS | PASS | PASS |
| **C-11** Fully-cited competitor table | PASS | PASS | PASS | PASS | PASS |
| **C-12** Self-negating cross-dimensional finding | PASS | PASS | PASS | PASS | PASS |
| **C-13** Claim-level finding anchors | PASS | PASS | PASS | PASS | PASS |
| **C-14** AMEND as proof validator | PASS | PASS | PASS | PASS | PASS |
| **C-15** Inline anchor tag before proof block | PASS | PASS | PASS | PASS | PASS |
| **C-16** Gate failure naming | PASS | PASS | PASS | PASS | PASS |
| **C-17** WHITESPACE grounded by attribute absence | PASS | PASS | PASS | PASS | PASS |
| **C-18** NOT ACCEPTABLE anchoring example | PASS | PASS | PASS | PASS | PASS |
| **C-19** Synthesis-first output contracts | PASS | PASS | PASS | PASS | PASS |
| **C-20** Structural column coercion for anchoring | PASS | PASS | PASS | PASS | PASS |
| **C-21** Gate-as-section with PASS/FAIL table | PASS | PASS | PASS | PASS | PASS |
| **C-22** INERTIA-REF per-finding citation | PASS | PASS | PASS | PASS | PASS |
| **C-23** Output contract slot format specification | PASS | PASS | PASS | PASS | PASS |
| **C-24** Phase-to-contract back-references | PASS | PASS | PASS | PASS | PASS |
| **C-25** Cross-table structural coercion | PASS | PASS | PASS | PASS | PASS |
| **C-26** Consolidated PREFLIGHT gate block | PASS | PASS | PASS | PASS | PASS |
| **C-27** Machine-readable phase column in contract | PASS | PASS | PASS | PASS | PASS |
| **C-28** OUTPUT CONTRACTS inside PREFLIGHT | PASS | PASS | PASS | PASS | PASS |
| **C-29** Full-path back-reference labels | PASS | PASS | PASS | PASS | PASS |
| **C-30** Write-token instruction in INERTIA-REF gate | PASS | PASS | PASS | PASS | PASS |

---

### Composite scores

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---:|---:|---:|---:|---:|
| Essential (5/5 x 60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (3/3 x 30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (22/22 x 110) | 110 | 110 | 110 | 110 | 110 |
| **Composite** | **200** | **200** | **200** | **200** | **200** |
| **Grade** | Exceptional | Exceptional | Exceptional | Exceptional | Exceptional |
| **Golden threshold (>=90)** | YES | YES | YES | YES | YES |

Second consecutive round at ceiling. R6 = 180/180 (rubric v5 ceiling); R7 = 200/200 (rubric v6 ceiling). All four new criteria satisfied across all variations on first attempt.

---

### Ranking

All five variations tie at 200/200. Qualitative structural distinction ranking (non-scoring, for rubric-progression purposes):

| Rank | Variation | Distinguishing property |
|------|-----------|------------------------|
| 1 | **V-05** | Combined maximum: spec-first + write-as-table-row + 6-slot contract (Focus-scope evidence slot) + three independent coercion templates + extended NOT ACCEPTABLE examples. Write-row Pass condition names the contract slot by full path: "this fills the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above)". Most complete forward-declaration surface — synthesis requirements visible at collection time via dedicated slot. |
| 2 | **V-03** | Cleanest single-axis write-as-table-row implementation. Three-row GATE 4 structure (C0 mechanism / Write token / Per-finding citation) makes token production independently checkable with named failure state "Inertia write failure". The write action cannot be separated from the gate's check logic. |
| 3 | **V-02** | Spec-first ordering combined with slot-referencing write directive. GATE 4 opens: "Fill the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above)" — the write action resolves a forward-declared dependency rather than creating a token ad hoc. Output contract visible before any constraint. |
| 4 | **V-04** | Imperative register + "Producing phase" synonym test + GATE 4 last (after OUTPUT CONTRACTS). Bold `**WRITE**` directive confirms that imperative style without table-row structure still satisfies C-30. Confirms synonym tolerance for C-27. |
| 5 | **V-01** | Gate-ordering variation (GATE 4 first, OUTPUT CONTRACTS last). Clean single-axis exploration of dependency-signaling through sequence. Most minimal satisfying form for C-27 through C-30. |

---

### Excellence signals (R7)

Patterns from R7 that represent genuine structural advances over R6:

**1. Write-token-as-gate-row makes token production independently checkable (V-03, V-05)**

In R6, the write-token instruction appeared as prose or a code block before the GATE 4 check table — it functioned as preamble text that a model might treat as context rather than directive. R7 V-03/V-05 encode the write action as a distinct row within the GATE 4 PASS/FAIL table, complete with: Check label ("Write INERTIA-REF token"), Pass condition (the required token format), and named Failure state ("Inertia write failure"). A reviewer verifies the write row the same way they verify any gate row — by matching the row's Pass condition to the output. The token write is structurally identical to a gate check: a condition with a success state and a named failure.

**2. Spec-first PREFLIGHT inverts the check-before-produce mental model (V-02, V-05)**

In R6, OUTPUT CONTRACTS appeared after all gates or as a late subsection in PREFLIGHT — the model read gate constraints before reading what it was expected to produce. R7 V-02/V-05 place OUTPUT CONTRACTS as the first subsection in PREFLIGHT. The model reads the full production target before encountering any gate logic. When GATE 4 executes its write action, it resolves a previously declared slot rather than creating a token from nothing. The write instruction in V-02/V-05 explicitly acknowledges this: "Fill the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above)" / "this fills the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above)." The gate acts as a contract-fulfillment step, not a side-effect.

**3. Focus-scope evidence slot forward-declares cross-dimensional proof requirements at collection time (V-05)**

R6 required the CROSS-DIMENSIONAL finding's REDUCTION-1/REDUCTION-2 structure at synthesis time (Phase 4). V-05 adds a sixth output contract slot — Focus-scope evidence — that Phase 4 must fill before applying GATE 3: `{attribute}: neither [{competitive_attribute}] alone nor [{focus_dim}] alone produces this gap — requires both`. This slot is forward-declared in OUTPUT CONTRACTS before any phase runs. The collection-to-synthesis pipeline now explicitly carries the cross-dimensional proof obligation: Phase 4 knows before it runs that it must produce scope evidence demonstrating why both dimensions are required. The synthesis requirement is visible at the contract level, not only at the phase-instruction level.

**4. Full-path back-reference labels resolve navigation ambiguity in nested structures (all five)**

R6 variations used "OUTPUT CONTRACT" as the back-reference label in phase headings. In R6, OUTPUT CONTRACT was a top-level section — the label was unambiguous. R7 embeds OUTPUT CONTRACTS as a subsection within PREFLIGHT (C-28), making a flat label potentially ambiguous. All R7 variations resolve this by using "PREFLIGHT > OUTPUT CONTRACTS" as the full path in every producing phase heading and structural column note. In V-04, the GATE 4 write instruction itself carries the full path: "**WRITE** the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above) now." Full-path labels are machine-readable contract addresses — navigable without reading any section heading other than the label itself.

---

### Key interactions — resolved

| Interaction | Resolution |
|---|---|
| V-04 uses "Producing phase" column header vs. "Filled by phase" — does this affect C-27? | No. C-27 accepts "or equivalent" labels. "Producing phase" is a direct synonym; the semantic function — naming the phase responsible for filling each slot — is identical. |
| V-01 OUTPUT CONTRACTS is last in PREFLIGHT (after all gates) vs. V-02/V-05 first — does position within PREFLIGHT affect C-28? | No. C-28 requires OUTPUT CONTRACTS to be a named subsection within PREFLIGHT — position within PREFLIGHT is not constrained. The criterion distinguishes inside vs. outside PREFLIGHT only. |
| V-03 OUTPUT CONTRACTS comes after GATE 4 — can C-29 be satisfied when GATE 4 has no back-reference? | Yes. C-29 applies to producing phase headings (Phase 2-5). GATE 4 is a gate, not a producing phase. In V-03, GATE 4 cannot back-reference OUTPUT CONTRACTS because the contract is declared after GATE 4. The OUTPUT CONTRACTS "Filled by phase" column value for INERTIA-REF is "GATE 4 (Write row)" — the contract names the gate; the gate does not need to name the contract. C-29 is satisfied by Phase 2-5 headings, which all use full-path labels. |
| V-05 GATE 4 write-row names the contract slot by full path — does this satisfy C-29 for the INERTIA-REF back-reference? | Yes, and additionally. C-29 requires full-path labels in producing phase headings; V-05 satisfies this in Phase 2-5. The GATE 4 write-row going further — naming the contract slot by full path within the gate's Pass condition — is a superset. It satisfies C-29 at the gate level in addition to the phase level. |
| V-05 adds a 6th slot (Focus-scope evidence) — does this affect C-27, C-23, C-24? | C-27: The 6th slot has a "Filled by phase" value — phase assignment column complete. C-23: The slot specifies a required format template. C-24: Phase 4 heading names both slots it fills. All three criteria remain satisfied; the 6th slot adds coverage without introducing any gap. |

---

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["write-token-as-gate-row: encoding INERTIA-REF production as a PASS/FAIL table row with named failure state makes token production independently checkable at review time -- the write action cannot be separated from gate logic or treated as contextual prose", "spec-first PREFLIGHT: declaring OUTPUT CONTRACTS before gate logic makes the production target visible before constraints so GATE 4 write actions resolve forward-declared slots rather than producing tokens ad hoc -- the gate acts as contract fulfillment", "focus-scope evidence slot: a dedicated 6th output contract slot forward-declares the cross-dimensional proof requirement at collection time -- Phase 4 knows before it runs that it must produce scope evidence demonstrating why both dimensions are necessary"]}
```
