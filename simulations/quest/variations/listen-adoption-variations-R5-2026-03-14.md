Written to `simulations/quest/variations/listen-adoption-variations-R5-2026-03-14.md`.

---

## Summary

**Five R5 variations targeting C-18 (revision obligation on self-audit deficiency, 5 pts, max 140)**

| ID | Axis | C-16 | C-17 | C-18 | Expected |
|----|------|------|------|------|----------|
| **V-01** | Re-run mandate in Pre-Commit FAIL path (V-04 base) | PASS | PASS | PASS | **140** |
| **V-02** | Behavioral contract header before SECTION A (V-05 base) | PASS | PASS | PASS | **140** |
| **V-03** | Conditional WRITE GATE replaces terminal write instruction (V-04 base) | PASS | PASS | PASS | **140** |
| **V-04** | V-05 base + SECTION K meta-gate tracking initial/final state | PASS | PASS | PASS | **140** |
| **V-05** | V-04 base + per-criterion revision log format + conditional write gate | PASS | PASS | PASS | **140** |

---

**R4 gap analysis:** Both R4 V-04 and V-05 scored 135/135. The C-18 gap: neither required the model's output to *show* the correction transaction — they stated revision obligations in FAIL paths but didn't force the re-run evidence to appear in the output. A model could note "FAIL, will fix sections 3a and 4" and then write the artifact.

**R5 mechanisms for closing C-18:**

- **V-01** — Structured FAIL path with mandatory re-run evidence block. If initial result is FAIL, the model must show what it corrected and re-run the check before proceeding. Closing mechanism: output evidence of correction visible per criterion.

- **V-02** — Behavioral contract at the top frames the revision obligation as a skill contract term (not per-gate suggestion). Reduces rationalization by making the rule visible before any content is produced.

- **V-03** — WRITE GATE replaces the write instruction with a COMMIT READY boolean. If NO, the model receives a revision directive, not a write instruction. Structurally branches to correction.

- **V-04** — SECTION K meta-gate records initial/final gate state for H/I/J with an explicit behavioral commitment. Evaluator checks C-18 by going directly to SECTION K — no need to trace individual gate histories.

- **V-05** — Per-criterion revision log (INITIAL RUN → REVISION LOG → RE-RUN → FINAL RESULT) makes the correction transaction visible per criterion and required by format.

**Ranking by C-18 evaluability robustness:** V-04 >= V-05 > V-01 > V-03 > V-02. V-04 preferred as the combined target: SECTION K provides a dedicated, independently named structural slot for C-18 evidence.
 PASS (trivial satisfaction), or
(c) The output must show a re-run of the gate after revision, with the re-run showing PASS.

R5 variations explore five distinct mechanisms for satisfying (a)/(b)/(c):
1. **V-01** -- structured FAIL path with mandatory re-run evidence block (V-04 base)
2. **V-02** -- behavioral contract at top of prompt as overarching framing (V-05 base)
3. **V-03** -- conditional WRITE GATE that computes COMMIT READY before issuing write instruction (V-04 base)
4. **V-04** -- dedicated SECTION K tracking initial/final gate state with behavioral commitment (V-05 base)
5. **V-05** -- per-criterion revision log format with conditional write gate (V-04 base, densest combination)

---

## V-01

**Variation axis:** Re-run mandate -- structured FAIL path in Pre-Commit requires model to show revision and re-run evidence before proceeding (V-04 base)
**Hypothesis:** R4 V-04's Pre-Commit block says "FAIL -- identify which sections to revise before proceeding" but does not require the model to show the revision or re-run. A model can satisfy C-16 (audit exists, names criteria) while listing a FAIL result and proceeding without correction. V-01 restructures each FAIL path into two phases: (1) initial run with PASS/FAIL result, and (2) if FAIL, a required revision-and-rerun block where the model shows what it changed and reruns the check. The rerun block must show PASS before the model can proceed. A final COMMIT CONFIRMATION block requires the model to explicitly state whether any revision occurred and confirm all three final results are PASS. C-18 should pass: the output either shows all initial results as PASS (trivial) or shows the revision transaction (deficiency identified, content revised, rerun shows PASS). C-16 passes (criterion-specific audit block with explicit pass conditions). C-17 passes (three structural elements: Step 5.5 Propagation Ledger for C-13, champion table column 4 for C-14, churn action column for C-15 -- none share a parent block).

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Inertia IDs

Assign every stock role to one Rogers archetype. For each role, write the Named Inertia entry and assign it an inertia ID.

**Inertia ID format:** `I-{role}` (e.g., `I-PM`, `I-UX`, `I-01`, `I-02`, ..., `I-12`, `I-Support`, `I-SRE`).

Named Inertia must be feature-specific. Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt" are attitude labels, not named inertia. A passing entry names what the role actually does today to accomplish the goal this feature addresses.

| Role    | Archetype       | Rationale (1 sentence)              | Inertia ID | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | I-PM       | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                         | I-UX       | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                         | I-01       | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                         | I-02       | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                         | I-03       | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                         | I-04       | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                         | I-05       | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                         | I-06       | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                         | I-07       | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                         | I-08       | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                         | I-09       | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                         | I-10       | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                         | I-11       | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                         | I-12       | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                         | I-Support  | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                         | I-SRE      | [feature-specific status-quo behavior]          |

**Propagation requirement:** The inertia IDs assigned here must be cited by ID in at least 3 of the following 4 downstream sections: chasm analysis (Step 3a), champion network (Step 3c), churn trigger register (Step 4), intervention list (Step 5). A downstream section satisfies this requirement only if it names at least one specific inertia ID (e.g., "I-05") -- paraphrase without ID citation does not count. You will verify this in the Propagation Ledger (Step 5.5).

---

### Step 2 -- Month-by-Month Adoption Timeline

Simulate the adoption curve forward from innovators. At least 3 distinct time steps. Rogers sequence must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards -- no inversions.

For each archetype-to-archetype transition, name the spread mechanism. At least one transition must name a mechanism specific to this feature context or name the inertia ID it is displacing; generic word of mouth alone fails.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific; cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|-----------------------------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                                               |
| M2    | Early Adopter    | ...            | ...                                                                               |
| M3    | [wave]           | ...            | ...                                                                               |
| M4    | [wave]           | ...            | ...                                                                               |
| M5    | [wave]           | ...            | ...                                                                               |

---

### Step 3 -- Chasm Analysis

Name the chasm between Early Adopters and Early Majority.

**3a. Why this chasm exists**
Cite the inertia IDs for Early Majority roles from Step 1 by ID. The chasm exists because these specific inertia entries make incremental value hard to perceive for the EM cluster. Name them explicitly. Example structure: "The chasm is anchored by I-05, I-06, and I-07: each describes a workflow that already handles [core use case]. The EA enthusiasm signal cannot bridge this because..." Generic diffusion theory does not pass this section.

**3b. Bridging mechanism**
Name the vehicle that directly addresses the cited inertia IDs. State which ID(s) this mechanism targets and how it displaces the status-quo behavior.

**3c. Champion network**

The champion table has four required columns. The fourth column -- EM Inertia Bridged -- is mandatory. State the specific inertia ID from Step 1 that this champion is positioned to overcome. "Well-placed to influence the early majority" without naming the inertia ID fails the fourth column even if column 3 passes.

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

At least 2 champions. Both column 3 and column 4 must be populated per row.

---

### Step 4 -- Churn Risk Register

For at least 2 archetypes, state the churn trigger and the mitigation.

**Churn trigger:** The specific event that causes the role to revert to the Named Inertia from Step 1. Frame as "reverts to [inertia ID]" to maintain the citation chain from Step 1.

**Mitigation -- action test:** Each mitigation must name a concrete team action. Valid action verbs: assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate. The following are surveillance responses and are not accepted as mitigations by themselves: monitor, track, watch, observe, measure, check, review telemetry. A mitigation reading only "monitor churn signals via telemetry" fails; "assign a champion to deliver a targeted re-onboarding session within 5 business days of the trigger event" passes. Mixed entries (action + optional measurement signal) pass.

| Archetype      | Churn Trigger (cite inertia ID)               | Mitigation (concrete team action -- no surveillance-only)   |
|----------------|-----------------------------------------------|-------------------------------------------------------------|
| ...            | Reverts to [I-xx]: [trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                           | ...                                                         |

---

### Step 5 -- Interventions (Ranked by Adoption Delta)

List interventions ranked by adoption delta. Each intervention must cite the inertia ID(s) it targets.

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |
| ...  | ...         | ...   | ...                                            |

At least 2 entries. Ranked in descending delta order.

---

### Step 5.5 -- Propagation Ledger

Produce the following table. For each downstream section, record the inertia IDs cited by ID (not paraphrase) and whether at least one citation is present. This table is the standalone structural verification for the inertia propagation requirement -- do not merge it with the champion table or churn register.

| Section                          | Inertia IDs Cited (list them)       | Citation Present? |
|----------------------------------|-------------------------------------|-------------------|
| Step 3a -- Chasm explanation     | [list IDs cited, or "none"]         | [yes / no]        |
| Step 3c -- Champion EM Inertia   | [list IDs cited, or "none"]         | [yes / no]        |
| Step 4 -- Churn triggers         | [list IDs cited, or "none"]         | [yes / no]        |
| Step 5 -- Interventions          | [list IDs cited, or "none"]         | [yes / no]        |
| **Total sections with citation** |                                     | **[N of 4]**      |

If total is less than 3: revise the sections showing "no" before proceeding to Step 6. Propagation Ledger must show N >= 3 before you continue.

---

### Step 6 -- Sensitivity Scenarios

Model two scenarios for chasm crossing. Each scenario names a different lever.

**Scenario 1 -- lever: [name it]**
Trajectory: [which archetype waves accelerate and when; cite which inertia IDs weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves plateau or stall; cite which inertia IDs hold under this lever]

---

### Step 7 -- Signal Readiness

**Proceed signals (at least 2, measurable):**
1. [e.g., >=3 Early Majority roles running sustained workflows after month 3 without reverting to I-05/I-06]
2. [Measurable]

**Abort signal (at least 1, measurable):**
1. [Measurable condition]

---

### Pre-Commit Verification

Complete all three checks before writing the artifact. For each check, run the initial assessment. If the initial result is PASS, proceed to the next check. If the initial result is FAIL, complete the revision block: state what you are correcting, make the correction in the relevant section above, then re-run the check and show the updated evidence. Do not proceed past a FAIL result without completing the revision block.

---

**C-13 check -- Inertia propagation (pass condition: inertia IDs cited by explicit ID reference in >=3 of 4 downstream sections)**

Initial run:
- Step 3a cited IDs: [list or "none"]
- Step 3c cited IDs: [list or "none"]
- Step 4 cited IDs: [list or "none"]
- Step 5 cited IDs: [list or "none"]
- Total sections with citation: [N of 4]
- C-13 initial result: [PASS if N>=3 / FAIL]

>> Complete this block ONLY if C-13 initial result is FAIL:
Revision: [state which sections showed "none" and what inertia IDs you are adding to each]
After making the corrections above, re-run:
- Step 3a cited IDs: [updated list]
- Step 3c cited IDs: [updated list]
- Step 4 cited IDs: [updated list]
- Step 5 cited IDs: [updated list]
- Total sections with citation: [N of 4]
- C-13 re-run result: [PASS / if still FAIL, repeat until PASS]

C-13 final result: [PASS -- state initial result and whether revision was required]

---

**C-14 check -- Champion double-anchor (pass condition: every champion row has archetype rationale AND a named EM inertia ID)**

Initial run:
- [Champion role 1]: Archetype rationale present? [yes/no]. EM Inertia ID cited? [yes/no -- if yes, which ID].
- [Champion role 2]: [same]
- [Additional rows if present]
- C-14 initial result: [PASS if all rows satisfy both conditions / FAIL -- identify failing rows]

>> Complete this block ONLY if C-14 initial result is FAIL:
Revision: [state which champion rows lack an EM inertia ID and what IDs you are adding]
After making the corrections to the champion table above, re-run:
- [Champion role 1]: Archetype rationale present? [yes/no]. EM Inertia ID cited? [yes/no -- which ID].
- [Champion role 2]: [same]
- C-14 re-run result: [PASS / if still FAIL, repeat until PASS]

C-14 final result: [PASS -- state initial result and whether revision was required]

---

**C-15 check -- Churn action test (pass condition: zero mitigations consist only of surveillance verbs)**

Initial run:
- [Archetype 1]: Contains concrete action verb? [yes/no -- which verb]. Surveillance-only? [yes/no].
- [Archetype 2]: [same]
- [Additional rows if present]
- C-15 initial result: [PASS if zero surveillance-only entries / FAIL -- identify failing rows]

>> Complete this block ONLY if C-15 initial result is FAIL:
Revision: [state which archetypes had surveillance-only mitigations and what concrete actions you are substituting]
After making the corrections to the churn register above, re-run:
- [Archetype 1]: Contains concrete action verb? [yes/no -- which verb]. Surveillance-only? [yes/no].
- [Archetype 2]: [same]
- C-15 re-run result: [PASS / if still FAIL, repeat until PASS]

C-15 final result: [PASS -- state initial result and whether revision was required]

---

**COMMIT CONFIRMATION**

Before writing the artifact, confirm all three:
- C-13 final result: [PASS]
- C-14 final result: [PASS]
- C-15 final result: [PASS]
- Revisions made: [none -- all initial results were PASS / OR list: C-xx required revision of [section]; correction: [what changed]]

Do not write the artifact until all three final results show PASS and this COMMIT CONFIRMATION block is complete.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-02

**Variation axis:** Behavioral contract header -- an overarching revision obligation is stated at the top of the prompt, before any content section, framing the entire execution (V-05 base)
**Hypothesis:** R4 V-05's revision obligation is embedded in each GATE's FAIL path: "If GATE H fails: identify sections, revise, re-run." This is per-gate and local. A model executing the skill reads the obligation at the point of each failure, not as an overarching rule. V-02 adds a prominent behavioral contract before SECTION A that frames the entire execution: when any gate fails, the obligation to revise and re-run is a non-optional skill contract term, not a per-gate suggestion. The contract also explicitly states what "evidence of correction" means in terms of output: the re-run result must appear in the response, not just be implied. C-18 should pass: the behavioral contract makes the revision obligation visible at the top of every execution of this skill, reducing the failure mode where a model reads the per-gate obligation and rationalizes "I noted what to fix, therefore I complied." C-16 passes (SECTIONS H/I/J each have criterion-specific verification). C-17 passes (three independently headed sections, each mapping to exactly one criterion).

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

**REVISION OBLIGATION CONTRACT**

This skill contains verification gates (SECTIONS H, I, J) that check specific quality criteria before the artifact is written. The following obligation governs every gate in this skill:

When a GATE fails:
1. Name the deficiency: state which specific entry or section failed and why.
2. Make the correction: revise the failing content in the relevant section above.
3. Show the re-run: re-execute the gate check with the revised content and include the re-run result in your response.
4. Confirm PASS: the gate's final result in your output must show PASS before you proceed.

This is not a suggestion -- it is the skill contract. An output that shows a GATE result of FAIL at the point the artifact is written is an incomplete and non-compliant execution of this skill. An output that names a deficiency without showing a revision and re-run has not satisfied the gate.

Produce your output in the exact section order below. Do not skip, merge, or qualify any section as optional.

---

### SECTION A -- Archetype Map with Named Inertia

**GATE A -- all of the following must be true before proceeding:**
- All 16 roles appear in the table; each appears exactly once
- All 5 archetype labels (Innovator, Early Adopter, Early Majority, Late Majority, Laggard) are used at least once
- The Named Inertia column is populated for every row with a feature-specific statement and an inertia ID in `I-{role}` format
- Generic entries fail GATE A: "may resist change," "prefers established workflows," "slow to adopt new tooling" are not named inertia

| Role    | Archetype       | Rationale (1 sentence)              | Inertia ID | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | I-PM       | [named status-quo behavior]                     |
| UX      | [archetype]     | [rationale]                         | I-UX       | [named status-quo behavior]                     |
| C-01    | [archetype]     | [rationale]                         | I-01       | [named status-quo behavior]                     |
| C-02    | [archetype]     | [rationale]                         | I-02       | [named status-quo behavior]                     |
| C-03    | [archetype]     | [rationale]                         | I-03       | [named status-quo behavior]                     |
| C-04    | [archetype]     | [rationale]                         | I-04       | [named status-quo behavior]                     |
| C-05    | [archetype]     | [rationale]                         | I-05       | [named status-quo behavior]                     |
| C-06    | [archetype]     | [rationale]                         | I-06       | [named status-quo behavior]                     |
| C-07    | [archetype]     | [rationale]                         | I-07       | [named status-quo behavior]                     |
| C-08    | [archetype]     | [rationale]                         | I-08       | [named status-quo behavior]                     |
| C-09    | [archetype]     | [rationale]                         | I-09       | [named status-quo behavior]                     |
| C-10    | [archetype]     | [rationale]                         | I-10       | [named status-quo behavior]                     |
| C-11    | [archetype]     | [rationale]                         | I-11       | [named status-quo behavior]                     |
| C-12    | [archetype]     | [rationale]                         | I-12       | [named status-quo behavior]                     |
| Support | [archetype]     | [rationale]                         | I-Support  | [named status-quo behavior]                     |
| SRE     | [archetype]     | [rationale]                         | I-SRE      | [named status-quo behavior]                     |

---

### SECTION B -- Adoption Timeline

**GATE B -- all of the following must be true before proceeding:**
- At least 3 distinct time steps
- Rogers sequence intact: Innovators before Early Adopters; Early Adopters before Early Majority; Early Majority before Late Majority; Late Majority before Laggards
- Each archetype-level transition has a named spread mechanism; at least one mechanism must name a specific inertia ID from SECTION A it is displacing or a feature-specific mechanism; generic word of mouth alone fails

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|------------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                              |
| M2    | Early Adopter    | ...            | ...                                                              |
| M3    | [wave]           | ...            | ...                                                              |
| M4    | [wave]           | ...            | ...                                                              |
| M5    | [wave]           | ...            | ...                                                              |

---

### SECTION C -- Chasm Analysis

**GATE C -- all of the following must be true before proceeding:**
- The word "chasm" appears in this section
- Early Majority inertia IDs from SECTION A are cited by explicit ID reference in the chasm explanation
- A bridging mechanism is named that addresses the cited inertia IDs and states which IDs it targets
- Champion table has at least 2 rows; both the archetype rationale column and EM Inertia Bridged column are populated per row; EM Inertia Bridged must cite a specific inertia ID from SECTION A

**C1. Why this chasm exists**
[Draw from EM inertia IDs in SECTION A. Name the specific IDs. Example: "The chasm is anchored by I-05, I-06, and I-07 -- each describes a workflow that already satisfies [core use case], so EA enthusiasm alone cannot displace them."]

**C2. Bridging mechanism**
[Name the vehicle that directly addresses the cited inertia IDs. State which IDs it targets and what status-quo behavior it displaces.]

**C3. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

---

### SECTION D -- Churn Risk Register

**GATE D -- all of the following must be true before proceeding:**
- At least 2 archetype rows
- Each churn trigger cites the inertia ID the archetype reverts to
- Every mitigation names a concrete team action; surveillance-only responses fail: monitor, track, watch, observe, measure, check, review telemetry are not mitigations by themselves; mixed entries (action + measurement signal) pass

| Archetype      | Churn Trigger (cite inertia ID)                        | Action Test (concrete team action -- surveillance-only fails) |
|----------------|--------------------------------------------------------|---------------------------------------------------------------|
| ...            | Reverts to I-[xx]: [specific trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                                    | ...                                                           |

---

### SECTION E -- Interventions (Ranked by Adoption Delta)

**GATE E -- all of the following must be true before proceeding:**
- At least 2 entries; list is in descending delta order
- Each entry has a delta label (H, M, or L)
- Each intervention cites at least one inertia ID from SECTION A it targets

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |
| ...  | ...         | ...   | ...                                            |

---

### SECTION F -- Sensitivity Scenarios

**GATE F -- all of the following must be true before proceeding:**
- Two named scenarios present; each names a different lever
- Each scenario shows a distinct adoption trajectory and cites which inertia IDs weaken or hold under that lever

**Scenario 1 -- lever: [name it]**
Trajectory: [which waves accelerate; which inertia IDs weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves stall; which inertia IDs hold under this lever]

---

### SECTION G -- Signal Readiness

**GATE G -- all of the following must be true before proceeding:**
- At least 2 measurable proceed signals
- At least 1 measurable abort signal
- All signals are concrete and trackable; vague signals fail; signals should cite inertia IDs where relevant

**Proceed signals:**
1. [Measurable -- e.g., >=3 Early Majority roles running sustained workflows after month 3 without reverting to I-05/I-06]
2. [Measurable]

**Abort signal:**
1. [Measurable condition]

---

### SECTION H -- C-13 Propagation Check

**This section verifies criterion C-13 only. Do not merge with SECTION I or SECTION J.**

**GATE H -- pass condition: inertia IDs cited by explicit ID reference in >=3 of the following 4 sections**

For each section below, list the inertia IDs cited by explicit reference (e.g., "I-05") -- not paraphrase, not pronoun. A section passes only if at least one specific ID appears in it.

| Section                     | Inertia IDs Cited by ID     | Passes? |
|-----------------------------|-----------------------------|---------|
| SECTION C1 -- Chasm         | [list IDs or "none"]        | [yes/no] |
| SECTION C3 -- Champion EM   | [list IDs or "none"]        | [yes/no] |
| SECTION D -- Churn triggers | [list IDs or "none"]        | [yes/no] |
| SECTION E -- Interventions  | [list IDs or "none"]        | [yes/no] |
| **Total passing**           |                             | **[N of 4]** |

GATE H result: [PASS if N>=3 / FAIL]

If GATE H fails: per the revision obligation contract, name the deficiency, revise the failing sections to include at least one explicit inertia ID citation, then re-run SECTION H below and show PASS before proceeding to SECTION I.

[Re-run SECTION H here if GATE H initially failed -- show updated table and GATE H re-run result: PASS]

---

### SECTION I -- C-14 Champion Anchor Check

**This section verifies criterion C-14 only. Do not merge with SECTION H or SECTION J.**

**GATE I -- pass condition: every champion row in SECTION C3 has both archetype rationale and a specific named EM inertia ID**

| Champion Role | Archetype Rationale Present? | EM Inertia ID Present and Specific? | Row Result |
|---------------|------------------------------|--------------------------------------|------------|
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |

GATE I result: [PASS if all rows show PASS / FAIL]

If GATE I fails: per the revision obligation contract, name the deficiency, revise the failing champion rows in SECTION C3, then re-run SECTION I below and show PASS before proceeding to SECTION J.

[Re-run SECTION I here if GATE I initially failed -- show updated table and GATE I re-run result: PASS]

---

### SECTION J -- C-15 Action Test

**This section verifies criterion C-15 only. Do not merge with SECTION H or SECTION I.**

**GATE J -- pass condition: zero mitigations in SECTION D consist only of surveillance verbs**

| Archetype   | Concrete action verb present? | Surveillance-only? | Row result |
|-------------|-------------------------------|---------------------|------------|
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |

Disqualified surveillance verbs (alone): monitor, track, watch, observe, measure, check, review telemetry.

GATE J result: [PASS if zero rows fail / FAIL]

If GATE J fails: per the revision obligation contract, name the deficiency, replace surveillance-only mitigations in SECTION D with entries containing a concrete team action, then re-run SECTION J below and show PASS before proceeding.

[Re-run SECTION J here if GATE J initially failed -- show updated table and GATE J re-run result: PASS]

---

All three verification sections (H, I, J) must show PASS before the artifact is written.

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-03

**Variation axis:** Conditional write gate -- the write instruction is replaced by a blocking COMMIT READY gate that the model must compute before the write instruction is issued (V-04 base)
**Hypothesis:** R4 V-04 ends with "Do not write the artifact until C-13, C-14, and C-15 all show PASS." This is a prose prohibition. A model that has rationalized a FAIL result still receives the write instruction and must consciously violate the prohibition to write. V-03 replaces the terminal write instruction with a WRITE GATE that requires the model to compute COMMIT READY as a boolean before any write instruction appears. If COMMIT READY = NO, the write instruction is replaced by a revision instruction; the model cannot reach the write instruction at all without satisfying all three criteria. C-18 should pass: the WRITE GATE forces the model to evaluate its final results, and if any is FAIL, the model receives an explicit directive to return and correct -- not a prohibition to consciously violate, but a structural branch that routes to correction. C-16 passes (Pre-Commit block names all three criteria with stated pass conditions). C-17 passes (Step 5.5 Propagation Ledger for C-13, champion table column 4 for C-14, churn action column for C-15 -- three separately identifiable elements).

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Inertia IDs

Assign every stock role to one Rogers archetype. For each role, write the Named Inertia entry and assign it an inertia ID.

**Inertia ID format:** `I-{role}` (e.g., `I-PM`, `I-UX`, `I-01`, `I-02`, ..., `I-12`, `I-Support`, `I-SRE`).

Named Inertia must be feature-specific. Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt" are attitude labels, not named inertia. A passing entry names what the role actually does today to accomplish the goal this feature addresses.

| Role    | Archetype       | Rationale (1 sentence)              | Inertia ID | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | I-PM       | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                         | I-UX       | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                         | I-01       | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                         | I-02       | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                         | I-03       | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                         | I-04       | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                         | I-05       | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                         | I-06       | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                         | I-07       | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                         | I-08       | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                         | I-09       | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                         | I-10       | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                         | I-11       | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                         | I-12       | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                         | I-Support  | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                         | I-SRE      | [feature-specific status-quo behavior]          |

**Propagation requirement:** The inertia IDs assigned here must be cited by ID in at least 3 of the following 4 downstream sections: chasm analysis (Step 3a), champion network (Step 3c), churn trigger register (Step 4), intervention list (Step 5). Paraphrase without ID citation does not count. You will verify this in the Propagation Ledger (Step 5.5).

---

### Step 2 -- Month-by-Month Adoption Timeline

Simulate the adoption curve forward from innovators. At least 3 distinct time steps. Rogers sequence must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards.

For each archetype-to-archetype transition, name the spread mechanism. At least one transition must cite a feature-specific mechanism or name the inertia ID it displaces; generic word of mouth alone fails.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific; cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|-----------------------------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                                               |
| M2    | Early Adopter    | ...            | ...                                                                               |
| M3    | [wave]           | ...            | ...                                                                               |
| M4    | [wave]           | ...            | ...                                                                               |
| M5    | [wave]           | ...            | ...                                                                               |

---

### Step 3 -- Chasm Analysis

**3a. Why this chasm exists**
Cite the inertia IDs for Early Majority roles from Step 1 by ID. The chasm exists because these specific inertia entries make incremental value hard to perceive for the EM cluster. Example: "The chasm is anchored by I-05, I-06, and I-07: each describes a workflow that already handles [core use case]."

**3b. Bridging mechanism**
Name the vehicle that directly addresses the cited inertia IDs. State which IDs it targets and how it displaces the status-quo behavior.

**3c. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

At least 2 champions. Both column 3 and column 4 must be populated per row.

---

### Step 4 -- Churn Risk Register

For at least 2 archetypes, state the churn trigger and the mitigation.

**Churn trigger:** Frame as "reverts to [inertia ID]" to maintain the citation chain from Step 1.

**Mitigation -- action test:** Valid action verbs: assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate. Surveillance-only responses fail: monitor, track, watch, observe, measure, check, review telemetry are not accepted as mitigations by themselves. Mixed entries (action + measurement signal) pass.

| Archetype      | Churn Trigger (cite inertia ID)               | Mitigation (concrete team action -- no surveillance-only)   |
|----------------|-----------------------------------------------|-------------------------------------------------------------|
| ...            | Reverts to [I-xx]: [trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                           | ...                                                         |

---

### Step 5 -- Interventions (Ranked by Adoption Delta)

Each intervention must cite the inertia ID(s) it targets.

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |
| ...  | ...         | ...   | ...                                            |

At least 2 entries. Ranked in descending delta order.

---

### Step 5.5 -- Propagation Ledger

This standalone section verifies inertia propagation (criterion C-13). Do not merge it with the champion table or churn register.

| Section                          | Inertia IDs Cited (list them)       | Citation Present? |
|----------------------------------|-------------------------------------|-------------------|
| Step 3a -- Chasm explanation     | [list IDs cited, or "none"]         | [yes / no]        |
| Step 3c -- Champion EM Inertia   | [list IDs cited, or "none"]         | [yes / no]        |
| Step 4 -- Churn triggers         | [list IDs cited, or "none"]         | [yes / no]        |
| Step 5 -- Interventions          | [list IDs cited, or "none"]         | [yes / no]        |
| **Total sections with citation** |                                     | **[N of 4]**      |

If total is less than 3: revise the sections showing "no" before proceeding to Step 6.

---

### Step 6 -- Sensitivity Scenarios

**Scenario 1 -- lever: [name it]**
Trajectory: [which archetype waves accelerate and when; cite which inertia IDs weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves plateau or stall; cite which inertia IDs hold under this lever]

---

### Step 7 -- Signal Readiness

**Proceed signals (at least 2, measurable):**
1. [Measurable -- cite inertia IDs where relevant]
2. [Measurable]

**Abort signal (at least 1, measurable):**
1. [Measurable condition]

---

### Pre-Commit Verification

Complete all three checks. Show specific evidence -- do not answer generically.

**C-13 check -- Inertia propagation (pass condition: inertia IDs cited by explicit ID reference in >=3 of 4 downstream sections):**
- Step 3a cited IDs: [list or "none"]
- Step 3c cited IDs: [list or "none"]
- Step 4 cited IDs: [list or "none"]
- Step 5 cited IDs: [list or "none"]
- Total sections with citation: [N of 4]
- C-13 result: [PASS if N>=3 / FAIL -- identify which sections need revision]

**C-14 check -- Champion double-anchor (pass condition: every champion row has archetype rationale AND a named EM inertia ID):**
- [Champion role 1]: Archetype rationale present? [yes/no]. EM Inertia ID cited? [yes/no -- if yes, which ID].
- [Champion role 2]: [same]
- C-14 result: [PASS if all rows satisfy both conditions / FAIL -- identify rows needing revision]

**C-15 check -- Churn action test (pass condition: zero mitigations consist only of surveillance verbs):**
- [Archetype 1]: Contains concrete action verb? [yes/no -- which verb]. Surveillance-only? [yes/no].
- [Archetype 2]: [same]
- C-15 result: [PASS if zero surveillance-only entries / FAIL -- identify rows needing replacement]

---

### WRITE GATE

Compute COMMIT READY from your Pre-Commit Verification results above:

| Criterion | Pre-Commit Result | Contributes to COMMIT READY? |
|-----------|------------------|------------------------------|
| C-13      | [PASS / FAIL]    | [yes -- PASS / no -- revision required] |
| C-14      | [PASS / FAIL]    | [yes -- PASS / no -- revision required] |
| C-15      | [PASS / FAIL]    | [yes -- PASS / no -- revision required] |
| **COMMIT READY** | | **[YES if all three PASS / NO if any FAIL]** |

**If COMMIT READY = YES:**
Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

**If COMMIT READY = NO:**
DO NOT write the artifact. Return to the Pre-Commit Verification and make the revisions indicated for each criterion showing FAIL. After making corrections, re-run the Pre-Commit Verification for the failing criteria, update those results to PASS, and return to this WRITE GATE. Recompute COMMIT READY. Repeat until COMMIT READY = YES, then write the artifact.

---

## V-04

**Variation axis:** Combined -- V-05 base (SECTIONS A-J) + SECTION K meta-gate that tracks initial/final gate state per criterion and requires explicit behavioral commitment
**Hypothesis:** R4 V-05's SECTIONS H/I/J each have revision obligations that satisfy C-16 and produce separately headed structural slots for C-17. The C-18 gap: the revision obligation is per-gate prose, not a final output-visible summary of whether correction occurred. An evaluator checking C-18 must read each individual gate result, trace whether any initially failed, and verify the correction in the prose -- there is no dedicated verification point. V-04 adds SECTION K after SECTIONS H/I/J. SECTION K is the C-18 structural slot: it records the initial gate result and the final gate result for each of C-13, C-14, C-15. A model that had a GATE fail and corrected it records initial=FAIL, final=PASS. A model that had all gates pass records initial=PASS, final=PASS. The behavioral commitment statement makes the revision obligation explicit as a final confirmation. C-18 should pass: SECTION K provides the output-visible evidence of correction (or trivial satisfaction) that an evaluator can inspect directly. C-16 PASS (SECTIONS H/I/J have criterion-specific audit). C-17 PASS (four separately headed sections: H for C-13, I for C-14, J for C-15, K for C-18 -- none merged).

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the exact section order below. Each GATE must be satisfied before proceeding to the next section. Do not skip, merge, or qualify any section as optional or conditional. SECTIONS H, I, J, and K are structurally independent -- each verifies exactly one criterion. Do not merge H, I, J, or K into a combined block.

---

### SECTION A -- Archetype Map with Named Inertia

**GATE A -- all of the following must be true before proceeding:**
- All 16 roles appear; each appears exactly once
- All 5 archetype labels used at least once
- Named Inertia column populated for every row with a feature-specific statement and an inertia ID in `I-{role}` format
- Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt new tooling" are not named inertia

| Role    | Archetype       | Rationale (1 sentence)              | Inertia ID | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | I-PM       | [named status-quo behavior]                     |
| UX      | [archetype]     | [rationale]                         | I-UX       | [named status-quo behavior]                     |
| C-01    | [archetype]     | [rationale]                         | I-01       | [named status-quo behavior]                     |
| C-02    | [archetype]     | [rationale]                         | I-02       | [named status-quo behavior]                     |
| C-03    | [archetype]     | [rationale]                         | I-03       | [named status-quo behavior]                     |
| C-04    | [archetype]     | [rationale]                         | I-04       | [named status-quo behavior]                     |
| C-05    | [archetype]     | [rationale]                         | I-05       | [named status-quo behavior]                     |
| C-06    | [archetype]     | [rationale]                         | I-06       | [named status-quo behavior]                     |
| C-07    | [archetype]     | [rationale]                         | I-07       | [named status-quo behavior]                     |
| C-08    | [archetype]     | [rationale]                         | I-08       | [named status-quo behavior]                     |
| C-09    | [archetype]     | [rationale]                         | I-09       | [named status-quo behavior]                     |
| C-10    | [archetype]     | [rationale]                         | I-10       | [named status-quo behavior]                     |
| C-11    | [archetype]     | [rationale]                         | I-11       | [named status-quo behavior]                     |
| C-12    | [archetype]     | [rationale]                         | I-12       | [named status-quo behavior]                     |
| Support | [archetype]     | [rationale]                         | I-Support  | [named status-quo behavior]                     |
| SRE     | [archetype]     | [rationale]                         | I-SRE      | [named status-quo behavior]                     |

---

### SECTION B -- Adoption Timeline

**GATE B -- all of the following must be true before proceeding:**
- At least 3 distinct time steps
- Rogers sequence intact: Innovators before Early Adopters; Early Adopters before Early Majority; Early Majority before Late Majority; Late Majority before Laggards
- Each transition has a named spread mechanism; at least one must name a specific inertia ID or feature-specific mechanism; generic word of mouth alone fails

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|------------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                              |
| M2    | Early Adopter    | ...            | ...                                                              |
| M3    | [wave]           | ...            | ...                                                              |
| M4    | [wave]           | ...            | ...                                                              |
| M5    | [wave]           | ...            | ...                                                              |

---

### SECTION C -- Chasm Analysis

**GATE C -- all of the following must be true before proceeding:**
- The word "chasm" appears
- Early Majority inertia IDs cited by explicit ID reference in the chasm explanation
- A bridging mechanism states which IDs it targets
- Champion table has at least 2 rows; both archetype rationale and EM Inertia Bridged columns populated per row with specific inertia IDs

**C1. Why this chasm exists**
[Draw from EM inertia IDs in SECTION A. Name the specific IDs. Example: "The chasm is anchored by I-05, I-06, and I-07 -- each describes a workflow that already satisfies [core use case]."]

**C2. Bridging mechanism**
[Name the vehicle. State which IDs it targets and what status-quo behavior it displaces.]

**C3. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

---

### SECTION D -- Churn Risk Register

**GATE D -- all of the following must be true before proceeding:**
- At least 2 archetype rows
- Each churn trigger cites the inertia ID the archetype reverts to
- Every mitigation names a concrete team action; surveillance-only responses fail; mixed entries (action + measurement signal) pass

| Archetype      | Churn Trigger (cite inertia ID)                        | Action Test (concrete team action -- surveillance-only fails) |
|----------------|--------------------------------------------------------|---------------------------------------------------------------|
| ...            | Reverts to I-[xx]: [specific trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                                    | ...                                                           |

---

### SECTION E -- Interventions (Ranked by Adoption Delta)

**GATE E -- all of the following must be true before proceeding:**
- At least 2 entries in descending delta order
- Each entry has a delta label (H, M, or L)
- Each intervention cites at least one inertia ID it targets

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |
| ...  | ...         | ...   | ...                                            |

---

### SECTION F -- Sensitivity Scenarios

**GATE F -- all of the following must be true before proceeding:**
- Two named scenarios; each names a different lever
- Each scenario shows a distinct adoption trajectory and cites which inertia IDs weaken or hold under that lever

**Scenario 1 -- lever: [name it]**
Trajectory: [which waves accelerate; which inertia IDs weaken]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves stall; which inertia IDs hold]

---

### SECTION G -- Signal Readiness

**GATE G -- all of the following must be true before proceeding:**
- At least 2 measurable proceed signals
- At least 1 measurable abort signal
- Signals are concrete and trackable; cite inertia IDs where relevant

**Proceed signals:**
1. [Measurable]
2. [Measurable]

**Abort signal:**
1. [Measurable condition]

---

### SECTION H -- C-13 Propagation Check

**This section verifies criterion C-13 only. Do not merge with SECTION I, J, or K.**

**GATE H -- pass condition: inertia IDs cited by explicit ID reference in >=3 of the following 4 sections**

| Section                     | Inertia IDs Cited by ID     | Passes? |
|-----------------------------|-----------------------------|---------|
| SECTION C1 -- Chasm         | [list IDs or "none"]        | [yes/no] |
| SECTION C3 -- Champion EM   | [list IDs or "none"]        | [yes/no] |
| SECTION D -- Churn triggers | [list IDs or "none"]        | [yes/no] |
| SECTION E -- Interventions  | [list IDs or "none"]        | [yes/no] |
| **Total passing**           |                             | **[N of 4]** |

GATE H result: [PASS if N>=3 / FAIL]

If GATE H fails: identify which sections show "no", revise those sections to include at least one explicit inertia ID citation, then re-run SECTION H. Do not proceed to SECTION I until GATE H shows PASS.

---

### SECTION I -- C-14 Champion Anchor Check

**This section verifies criterion C-14 only. Do not merge with SECTION H, J, or K.**

**GATE I -- pass condition: every champion row in SECTION C3 has both archetype rationale and a specific named EM inertia ID**

| Champion Role | Archetype Rationale Present? | EM Inertia ID Present and Specific? | Row Result |
|---------------|------------------------------|--------------------------------------|------------|
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |

GATE I result: [PASS if all rows show PASS / FAIL]

If GATE I fails: revise the failing champion rows in SECTION C3 to add the specific EM inertia ID, then re-run SECTION I. Do not proceed to SECTION J until GATE I shows PASS.

---

### SECTION J -- C-15 Action Test

**This section verifies criterion C-15 only. Do not merge with SECTION H, I, or K.**

**GATE J -- pass condition: zero mitigations in SECTION D consist only of surveillance verbs**

| Archetype   | Concrete action verb present? | Surveillance-only? | Row result |
|-------------|-------------------------------|---------------------|------------|
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |

Disqualified surveillance verbs (alone): monitor, track, watch, observe, measure, check, review telemetry.

GATE J result: [PASS if zero rows fail / FAIL]

If GATE J fails: replace surveillance-only mitigations in SECTION D, then re-run SECTION J. Do not proceed to SECTION K until GATE J shows PASS.

---

### SECTION K -- C-18 Revision Commitment

**This section verifies criterion C-18 only. Do not merge with SECTION H, I, or J.**

Complete this section after SECTIONS H, I, and J all show PASS. Record the history of each verification gate.

| Section | Initial Gate Result | Revision Required? | Final Gate Result |
|---------|--------------------|--------------------|-------------------|
| GATE H (C-13 Propagation) | [PASS / FAIL] | [yes / no] | [PASS] |
| GATE I (C-14 Champion Anchor) | [PASS / FAIL] | [yes / no] | [PASS] |
| GATE J (C-15 Action Test) | [PASS / FAIL] | [yes / no] | [PASS] |

**Behavioral commitment:** I confirm that for every gate above showing "Revision Required: yes," the deficient content was revised and the gate was re-run before this entry shows PASS. For every gate showing "Revision Required: no," the initial run satisfied the pass condition. The artifact is being committed with all final gate results showing PASS and no unresolved deficiencies.

GATE K result: PASS if all "Final Gate Result" entries show PASS AND the behavioral commitment above is stated.

Do not write the artifact until GATE K shows PASS.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-05

**Variation axis:** Combined -- V-04 base (Propagation Ledger + Pre-Commit) restructured with per-criterion revision log format (initial run / correction / re-run triple) and conditional WRITE GATE
**Hypothesis:** V-01 adds explicit re-run evidence to V-04's Pre-Commit FAIL paths. V-03 adds a conditional WRITE GATE. V-05 combines both and adds a third element: a per-criterion revision log that forces the initial run result to appear alongside any correction. The log format (initial run → correction if needed → final run) makes the correction transaction visible even when output space is limited. An evaluator checking C-18 can scan to any criterion's block, read the initial result, check whether a correction block is present, and verify the final result shows PASS -- without reading surrounding prose. C-18 should pass: the revision log format makes the correction evidence a required structural output for each criterion, not a prose note. C-16 passes (Pre-Commit block names all three criteria with explicit pass conditions). C-17 passes (Step 5.5 Propagation Ledger for C-13, champion table column 4 for C-14, churn action column for C-15 -- three separately identifiable elements).

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Inertia IDs

Assign every stock role to one Rogers archetype. For each role, write the Named Inertia entry and assign it an inertia ID.

**Inertia ID format:** `I-{role}` (e.g., `I-PM`, `I-UX`, `I-01`, `I-02`, ..., `I-12`, `I-Support`, `I-SRE`).

Named Inertia must be feature-specific. Generic entries fail.

| Role    | Archetype       | Rationale (1 sentence)              | Inertia ID | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | I-PM       | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                         | I-UX       | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                         | I-01       | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                         | I-02       | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                         | I-03       | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                         | I-04       | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                         | I-05       | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                         | I-06       | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                         | I-07       | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                         | I-08       | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                         | I-09       | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                         | I-10       | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                         | I-11       | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                         | I-12       | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                         | I-Support  | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                         | I-SRE      | [feature-specific status-quo behavior]          |

**Propagation requirement:** The inertia IDs assigned here must be cited by ID in at least 3 of the following 4 downstream sections: chasm analysis (Step 3a), champion network (Step 3c), churn trigger register (Step 4), intervention list (Step 5). You will verify this in the Propagation Ledger (Step 5.5).

---

### Step 2 -- Month-by-Month Adoption Timeline

At least 3 distinct time steps. Rogers sequence intact. At least one transition must cite a feature-specific mechanism or name the inertia ID it displaces.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific; cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|-----------------------------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                                               |
| M2    | Early Adopter    | ...            | ...                                                                               |
| M3    | [wave]           | ...            | ...                                                                               |
| M4    | [wave]           | ...            | ...                                                                               |
| M5    | [wave]           | ...            | ...                                                                               |

---

### Step 3 -- Chasm Analysis

**3a. Why this chasm exists**
Cite the inertia IDs for Early Majority roles from Step 1 by ID. Example: "The chasm is anchored by I-05, I-06, and I-07."

**3b. Bridging mechanism**
Name the vehicle. State which IDs it targets and how it displaces the status-quo behavior.

**3c. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

At least 2 champions. Both column 3 and column 4 must be populated per row.

---

### Step 4 -- Churn Risk Register

| Archetype      | Churn Trigger (cite inertia ID)               | Mitigation (concrete team action -- no surveillance-only)   |
|----------------|-----------------------------------------------|-------------------------------------------------------------|
| ...            | Reverts to [I-xx]: [trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                           | ...                                                         |

Valid action verbs: assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate. Surveillance-only fails.

---

### Step 5 -- Interventions (Ranked by Adoption Delta)

**Delta scale:** H = full archetype wave shift in one quarter; M = meaningful acceleration, sub-wave; L = directional.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |
| ...  | ...         | ...   | ...                                            |

---

### Step 5.5 -- Propagation Ledger

Standalone section for C-13. Do not merge with champion table or churn register.

| Section                          | Inertia IDs Cited (list them)       | Citation Present? |
|----------------------------------|-------------------------------------|-------------------|
| Step 3a -- Chasm explanation     | [list IDs cited, or "none"]         | [yes / no]        |
| Step 3c -- Champion EM Inertia   | [list IDs cited, or "none"]         | [yes / no]        |
| Step 4 -- Churn triggers         | [list IDs cited, or "none"]         | [yes / no]        |
| Step 5 -- Interventions          | [list IDs cited, or "none"]         | [yes / no]        |
| **Total sections with citation** |                                     | **[N of 4]**      |

If total is less than 3: revise sections showing "no" before proceeding to Step 6.

---

### Step 6 -- Sensitivity Scenarios

**Scenario 1 -- lever: [name it]**
Trajectory: [cite inertia IDs that weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [cite inertia IDs that hold under this lever]

---

### Step 7 -- Signal Readiness

**Proceed signals (at least 2, measurable):**
1. [Measurable -- cite inertia IDs where relevant]
2. [Measurable]

**Abort signal:**
1. [Measurable]

---

### Pre-Commit Verification with Revision Logs

For each criterion below, complete the INITIAL RUN. If INITIAL RESULT is PASS, mark final result PASS and proceed. If INITIAL RESULT is FAIL, complete the REVISION LOG, make the correction in the relevant section above, complete the RE-RUN, and record the FINAL RESULT. Do not answer any check generically -- show specific evidence at every step.

---

**C-13 -- Inertia Propagation**
*(pass condition: inertia IDs cited by explicit ID reference in >=3 of 4 downstream sections)*

INITIAL RUN:
- Step 3a IDs: [list or "none"] | present? [yes/no]
- Step 3c IDs: [list or "none"] | present? [yes/no]
- Step 4 IDs:  [list or "none"] | present? [yes/no]
- Step 5 IDs:  [list or "none"] | present? [yes/no]
- Total: [N of 4]
- INITIAL RESULT: [PASS if N>=3 / FAIL]

REVISION LOG (omit if INITIAL RESULT is PASS):
- Sections lacking citation: [list]
- Correction: [which inertia IDs added to which sections]
RE-RUN (omit if INITIAL RESULT is PASS):
- Step 3a IDs: [updated] | present? [yes/no]
- Step 3c IDs: [updated] | present? [yes/no]
- Step 4 IDs:  [updated] | present? [yes/no]
- Step 5 IDs:  [updated] | present? [yes/no]
- Total: [N of 4]
- RE-RUN RESULT: [PASS / if still FAIL, repeat until PASS]

**C-13 FINAL RESULT: [PASS]**

---

**C-14 -- Champion Double-Anchor**
*(pass condition: every champion row has archetype rationale AND a specific named EM inertia ID)*

INITIAL RUN:
- [Champion 1]: Archetype rationale? [yes/no] | EM Inertia ID? [yes -- I-xx / no / generic]
- [Champion 2]: [same]
- INITIAL RESULT: [PASS if all rows satisfy both / FAIL -- identify failing rows]

REVISION LOG (omit if INITIAL RESULT is PASS):
- Rows lacking EM inertia ID: [list]
- Correction: [which IDs added to which champion rows]
RE-RUN (omit if INITIAL RESULT is PASS):
- [Champion 1]: Archetype rationale? [yes/no] | EM Inertia ID? [yes -- I-xx / no]
- [Champion 2]: [same]
- RE-RUN RESULT: [PASS / if still FAIL, repeat until PASS]

**C-14 FINAL RESULT: [PASS]**

---

**C-15 -- Churn Action Test**
*(pass condition: zero mitigations consist only of surveillance verbs)*

INITIAL RUN:
- [Archetype 1]: Action verb? [yes -- which / no] | Surveillance-only? [yes/no]
- [Archetype 2]: [same]
- INITIAL RESULT: [PASS if zero surveillance-only / FAIL -- identify failing rows]

REVISION LOG (omit if INITIAL RESULT is PASS):
- Surveillance-only rows: [list archetypes]
- Correction: [what concrete actions substituted for which archetypes]
RE-RUN (omit if INITIAL RESULT is PASS):
- [Archetype 1]: Action verb? [yes -- which / no] | Surveillance-only? [yes/no]
- [Archetype 2]: [same]
- RE-RUN RESULT: [PASS / if still FAIL, repeat until PASS]

**C-15 FINAL RESULT: [PASS]**

---

### WRITE GATE

Compute COMMIT READY:

| Criterion | Final Result | COMMIT READY contribution |
|-----------|-------------|---------------------------|
| C-13      | [PASS]      | [yes]                     |
| C-14      | [PASS]      | [yes]                     |
| C-15      | [PASS]      | [yes]                     |
| **COMMIT READY** | | **[YES / NO]** |

**If COMMIT READY = YES:**
Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

**If COMMIT READY = NO:**
DO NOT write the artifact. The failing criterion's REVISION LOG must be completed, corrections made in the relevant section above, and the RE-RUN must show PASS. Return to WRITE GATE after all criteria show PASS.

---

## Expected Scores

| Variation | C-01-C-08 | C-09-C-15 | C-16 | C-17 | C-18 | Composite | Notes |
|-----------|-----------|-----------|------|------|------|-----------|-------|
| V-01 | PASS (90) | PASS (35) | PASS (5) | PASS (5) | PASS (5) | **140** | Re-run mandate + COMMIT CONFIRMATION |
| V-02 | PASS (90) | PASS (35) | PASS (5) | PASS (5) | PASS (5) | **140** | Behavioral contract header |
| V-03 | PASS (90) | PASS (35) | PASS (5) | PASS (5) | PASS (5) | **140** | Conditional WRITE GATE |
| V-04 | PASS (90) | PASS (35) | PASS (5) | PASS (5) | PASS (5) | **140** | SECTION K meta-gate (strongest evaluability) |
| V-05 | PASS (90) | PASS (35) | PASS (5) | PASS (5) | PASS (5) | **140** | Revision log per criterion (most inspectable) |

**Distinguishing properties for C-18 evaluability:**

- **V-01** (re-run mandate): Makes correction visible by requiring a structured "revision + re-run" block in the Pre-Commit output. Evaluator checks for the presence of re-run evidence when initial result was FAIL. Risk: model may omit the re-run block if it convinces itself the initial result was borderline PASS.

- **V-02** (behavioral contract): States the obligation at the top as a skill-level rule, not a per-gate suggestion. Reduces rationalization by framing the revision requirement as a contract term. Risk: the obligation is prose, not a structural output slot -- evaluator must still trace individual gate results.

- **V-03** (conditional WRITE GATE): Makes the write instruction itself conditional. If COMMIT READY = NO, the model receives a revision directive instead of a write instruction. Structural branching prevents proceeding without satisfying the gate. Risk: WRITE GATE is at the bottom; a model that rationalized earlier checks still reaches it with FAIL results.

- **V-04** (SECTION K meta-gate): Creates a dedicated structural output slot for C-18 verification. Evaluator goes directly to SECTION K to see initial/final gate state history. If initial=FAIL and final=PASS for any row, the correction should be visible in the corresponding SECTION H/I/J. This is the clearest evaluability path for C-18. Risk: SECTION K is additive to H/I/J; a model that poorly executes H/I/J may also execute K poorly.

- **V-05** (revision log): Embeds the correction evidence directly in each criterion's check block (INITIAL RUN → REVISION LOG → RE-RUN → FINAL RESULT). The evaluator can verify C-18 per criterion without cross-referencing other sections. If INITIAL RESULT is FAIL and no REVISION LOG is present, C-18 fails for that criterion. Risk: Most verbose variation -- may increase prompt complexity for marginal robustness gain over V-04.

**Ranking by robustness against C-18 rationalization:**
V-04 >= V-05 > V-01 > V-03 > V-02

V-04 is preferred because SECTION K is an independently named structural element that an evaluator can point to for C-18 evidence, satisfying both C-17 (structural slot for C-18's parent criterion chain) and C-18 (behavioral commitment with initial/final state tracking). V-05 is equally strong on evaluability but denser.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["Re-run mandate in structured FAIL path closes C-18 by requiring the model to show revision and re-run evidence before proceeding, not just note what needs fixing", "Behavioral contract header at prompt top frames revision obligation as a skill contract term, reducing per-gate rationalization by making the rule visible at execution start", "Conditional write gate replaces terminal write instruction with a COMMIT READY boolean gate, structurally blocking artifact write until all criteria show PASS and preventing silent bypass of FAIL results", "SECTION K meta-gate provides a dedicated structural slot for C-18 verification -- tracking initial/final gate state with behavioral commitment makes correction evidence inspectable at a single location without tracing individual gate histories", "Per-criterion revision log format (initial run / revision log / re-run) makes correction transaction visible and required per criterion -- evaluator verifies C-18 by checking whether initial FAIL entries have a populated revision log and re-run showing PASS"]}
```
