Written to `simulations/quest/variations/listen-adoption-variations-R6-2026-03-14.md`.

---

## Round 6 Variations — listen-adoption

**New criteria:** C-19 (correction transaction content visible, 5 pts) and C-20 (single named terminal section consolidates gate states, 5 pts). Max: 140 → 150.

---

### R5 gap that drives R6 design

R5 V-04's SECTION K satisfies **C-20** (single named terminal section, records gate states) but fails **C-19**: it records `Revision Required: yes/no` — not the corrected content. An evaluator reading SECTION K cannot verify what was corrected without trusting the model's self-report.

R5 V-05's per-criterion revision log satisfies **C-19** (content visible per-criterion) but fails **C-20**: evidence is distributed across SECTIONS H/I/J — no single named terminal section.

The rubric's C-20 note makes the distinction sharp: "this section is distinct from the self-audit block required by C-16 (which performs the check — this section records the outcome)."

---

### Five variations

| ID | Axis | C-19 Mechanism | C-20 Mechanism |
|----|------|----------------|----------------|
| **V-01** | Content transaction format (single-axis) | Inline `CORRECTION BLOCK` with BEFORE/AFTER content at point of revision | SECTION K records gate states + references inline block by name |
| **V-02** | Terminal section as content consolidator (single-axis) | Corrected content written INTO SECTION K's "Corrected content" cell | SECTION K contains both gate state and corrected content — one location for everything |
| **V-03** | Phrasing register — conversational walkthrough (single-axis) | "Show the original and corrected entry" framing in prose audit | "Audit Outcomes" named closing section in conversational form |
| **V-04** | Combined A+B — inline correction + terminal pointer | Inline CORRECTION BLOCKs (identical to V-01) | SECTION K explicitly does NOT duplicate content — references block location only; concern separation is explicit in the structural contract |
| **V-05** | Combined A+B+C — inline + terminal + register shift | Inline CORRECTION BLOCKs in formal verification mode | SECTION K in formal verification mode; content sections A–G in conversational register |

---

### Key design decisions

**V-01 vs V-04 distinction:** Both use inline BEFORE/AFTER blocks. V-01's SECTION K adds a `Correction Location` column. V-04 adds an explicit structural contract at the top: *"Corrected content lives in inline CORRECTION BLOCKs. SECTION K does NOT duplicate corrected content — it references block locations."* V-04 enforces separation of C-19 and C-20 concerns by rule; V-01 achieves the same separation implicitly.

**V-02 trade-off:** One place to check (C-20 maximized; evaluator sees corrected content in SECTION K). But: BEFORE content is gone — SECTION K has no BEFORE column, only a "Corrected content" cell. An evaluator can verify the correction satisfies the pass condition, but cannot compare before/after in situ. C-19 passes (content visible) but C-20 evaluability is higher than C-19 verifiability.

**V-03 risk vector:** Conversational "show the before and after" is less binding than a formal BEFORE: / AFTER: template. The model may produce a narrative description of what changed rather than the structural content itself. C-19 is the expected failure mode; C-20 is borderline (the "Audit Outcomes" section exists but may not be clearly named or distinct from the verification prose).

**V-05 register shift hypothesis:** The verification sections (H–K) retain formal structure identical to V-04. The content sections (A–G) shift to conversational register with explicit reasoning prompts. Secondary test: does conversational framing improve Named Inertia quality (C-11) and champion rationale depth (C-14)?

---

### Expected differential on C-19/C-20

| Variation | C-19 Expected | C-20 Expected | Notes |
|-----------|--------------|--------------|-------|
| V-01 | PASS | PASS | Inline BEFORE/AFTER = content visible; SECTION K = terminal section |
| V-02 | PASS | PASS | Content in SECTION K; evaluator checks one place |
| V-03 | UNCERTAIN | PASS-RISK | Conversational framing may not enforce content materialization |
| V-04 | PASS | PASS | Highest evaluability — explicit separation of C-19 location (inline) and C-20 location (SECTION K) |
| V-05 | PASS | PASS | Formal verification mode preserves C-19/C-20 enforcement; register shift may improve content quality |
Inertia

**GATE A -- all of the following must be true before proceeding:**
- All 16 roles appear; each appears exactly once
- All 5 archetype labels (Innovator, Early Adopter, Early Majority, Late Majority, Laggard) are used at least once
- Named Inertia column populated for every row with a feature-specific statement and an inertia ID in `I-{role}` format
- Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt new tooling" are not named inertia

**Propagation requirement:** Inertia IDs assigned here must be cited by explicit ID reference in at least 3 of the following 4 downstream sections: chasm analysis (SECTION C1), champion network (SECTION C3 column 4), churn trigger register (SECTION D), intervention list (SECTION E). You will verify this in SECTION H.

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

---

### SECTION B -- Adoption Timeline

**GATE B -- all of the following must be true before proceeding:**
- At least 3 distinct time steps
- Rogers sequence intact: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards; no inversions
- Each archetype-level transition has a named spread mechanism; at least one must cite a specific inertia ID from SECTION A or a feature-specific mechanism; generic word of mouth alone fails

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
- Early Majority inertia IDs from SECTION A cited by explicit ID reference in the chasm explanation
- A bridging mechanism states which IDs it targets and how it displaces the status-quo behavior
- Champion table has at least 2 rows; both archetype rationale (column 3) and EM Inertia Bridged (column 4) are populated per row with specific inertia IDs from SECTION A

**C1. Why this chasm exists**
[Cite EM inertia IDs by explicit ID. Example: "The chasm is anchored by I-05, I-06, and I-07 -- each describes a workflow that already satisfies [core use case], so EA enthusiasm cannot displace them."]

**C2. Bridging mechanism**
[Name the vehicle. State which IDs it targets and what status-quo behavior it displaces.]

**C3. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

"Well-placed to influence the early majority" without naming the inertia ID fails column 4 even if column 3 passes. Both columns must be populated per row.

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
- At least 2 entries in descending delta order
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
- Two named scenarios; each names a different lever
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
- All signals are concrete and trackable; vague signals fail; cite inertia IDs where relevant

**Proceed signals:**
1. [Measurable -- e.g., >=3 Early Majority roles running sustained workflows after month 3 without reverting to I-05/I-06]
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

GATE H initial result: [PASS if N>=3 / FAIL]

**If GATE H fails:** identify which sections show "no" and what specific IDs are missing. Revise those sections, then produce the following correction block immediately below and re-run GATE H.

> **CORRECTION BLOCK -- C-13 (SECTION H)**
>
> BEFORE -- [section name, e.g., "SECTION E -- Interventions"]:
> [Reproduce the original table row(s) or content that lacked inertia ID citations]
>
> AFTER -- [section name]:
> [Write the corrected content with explicit inertia ID citations added]
>
> GATE H re-run:
> [Reproduce the updated citation table above; show N of 4 >= 3]
> GATE H re-run result: PASS

The BEFORE content must reproduce the original text. The AFTER content must satisfy the pass condition. A statement "added inertia IDs to SECTION E" without showing the corrected rows fails C-19.

If GATE H initial result is PASS, write: "GATE H: no correction required."

GATE H final result: [PASS]

Do not proceed to SECTION I until GATE H final result shows PASS.

---

### SECTION I -- C-14 Champion Anchor Check

**This section verifies criterion C-14 only. Do not merge with SECTION H, J, or K.**

**GATE I -- pass condition: every champion row in SECTION C3 has both archetype rationale (column 3) and a specific named EM inertia ID (column 4)**

| Champion Role | Archetype Rationale Present? | EM Inertia ID Present and Specific? | Row Result |
|---------------|------------------------------|--------------------------------------|------------|
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |

GATE I initial result: [PASS if all rows show PASS / FAIL]

**If GATE I fails:** identify which champion rows lack a specific EM inertia ID. Revise those rows, then produce the following correction block immediately below and re-run GATE I.

> **CORRECTION BLOCK -- C-14 (SECTION I)**
>
> BEFORE -- SECTION C3 champion table, row [role]:
> | [role] | [archetype] | [original column 3] | [original column 4 -- blank or generic] |
>
> AFTER -- SECTION C3 champion table, row [role]:
> | [role] | [archetype] | [column 3] | I-[xx]: [specific named inertia this champion bridges] |
>
> GATE I re-run:
> [Reproduce the updated champion row audit table; show all rows PASS]
> GATE I re-run result: PASS

The AFTER row must include the full corrected table row. "Updated column 4 with inertia ID" without showing the row fails C-19.

If GATE I initial result is PASS, write: "GATE I: no correction required."

GATE I final result: [PASS]

Do not proceed to SECTION J until GATE I final result shows PASS.

---

### SECTION J -- C-15 Action Test

**This section verifies criterion C-15 only. Do not merge with SECTION H, I, or K.**

**GATE J -- pass condition: zero mitigations in SECTION D consist only of surveillance verbs**

| Archetype   | Concrete action verb present? | Surveillance-only? | Row result |
|-------------|-------------------------------|---------------------|------------|
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |

Disqualified surveillance verbs (alone): monitor, track, watch, observe, measure, check, review telemetry.

GATE J initial result: [PASS if zero rows fail / FAIL]

**If GATE J fails:** identify which archetypes have surveillance-only mitigations. Replace those mitigations, then produce the following correction block immediately below and re-run GATE J.

> **CORRECTION BLOCK -- C-15 (SECTION J)**
>
> BEFORE -- SECTION D, row [archetype]:
> | [archetype] | [original churn trigger] | [surveillance-only mitigation] |
>
> AFTER -- SECTION D, row [archetype]:
> | [archetype] | [churn trigger] | [assign / deliver / remove / ...]: [concrete team action] |
>
> GATE J re-run:
> [Reproduce the updated action test table; show zero surveillance-only rows]
> GATE J re-run result: PASS

The AFTER row must show the full corrected mitigation. "Replaced surveillance with action verb" without showing the corrected row fails C-19.

If GATE J initial result is PASS, write: "GATE J: no correction required."

GATE J final result: [PASS]

Do not proceed to SECTION K until GATE J final result shows PASS.

---

### SECTION K -- Gate State Record

**This section records the outcome of SECTIONS H, I, and J. It is distinct from SECTIONS H/I/J (which performed the checks); this section consolidates the final state. Do not merge with SECTION H, I, or J.**

Complete this section after all three final results (H, I, J) show PASS.

| Criterion | Initial Gate Result | Revision Performed | Correction Location | Final Gate Result |
|-----------|--------------------|--------------------|---------------------|-------------------|
| C-13 (GATE H) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-13, SECTION H" / If No: "--"] | [PASS] |
| C-14 (GATE I) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-14, SECTION I" / If No: "--"] | [PASS] |
| C-15 (GATE J) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-15, SECTION J" / If No: "--"] | [PASS] |

**Behavioral commitment:** For every row showing "Revision Performed: Yes," the deficient content was revised, the corrected content appears in the corresponding CORRECTION BLOCK above, and the gate was re-run showing PASS. For every row showing "Revision Performed: No," the initial gate satisfied the pass condition. All three Final Gate Results show PASS. The artifact is complete.

GATE K result: PASS when all final results show PASS and the behavioral commitment is stated.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-02

**Variation axis:** Terminal section as content consolidator -- corrected content written INTO the terminal section (single-axis)

**Hypothesis:** V-01 places corrected content inline (adjacent to the gate check) and records a pointer in SECTION K. V-02 inverts this: when a gate fails, the model does NOT write inline correction blocks. Instead, it writes the corrected content directly into SECTION K's "Corrected Content" column. SECTION K therefore contains both the gate state record (C-20) and the corrected structural content (C-19) in a single location. An evaluator checking C-19/C-20 reads one section. Trade-off: the corrected content is not adjacent to the original; an evaluator comparing before/after must cross-reference the content section and SECTION K rather than reading a co-located BEFORE/AFTER block. SECTIONS A-G and H-J structure is inherited from V-01. The key difference is in the REVISION OBLIGATION (no inline blocks) and SECTION K design (wider table with corrected content column).

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the exact section order below. Do not skip, merge, or qualify any section as optional or conditional. SECTIONS H, I, J, and K are structurally independent. Do not merge H, I, J, or K into a combined block.

**CORRECTION RULE:** When any of GATES H, I, or J fail, do NOT write inline correction blocks. Write the corrected content into the "Corrected Content" column of SECTION K. The artifact's correction evidence lives in SECTION K only -- an evaluator checking whether the revision content is visible goes to SECTION K.

---

### SECTION A -- Archetype Map with Named Inertia

**GATE A -- all of the following must be true before proceeding:**
- All 16 roles appear; each appears exactly once
- All 5 archetype labels used at least once
- Named Inertia column populated for every row with a feature-specific statement and an inertia ID in `I-{role}` format
- Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt new tooling" are not named inertia

**Propagation requirement:** Inertia IDs assigned here must be cited by explicit ID reference in at least 3 of the following 4 downstream sections: chasm analysis (SECTION C1), champion network (SECTION C3 column 4), churn trigger register (SECTION D), intervention list (SECTION E). You will verify this in SECTION H.

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

---

### SECTION B -- Adoption Timeline

**GATE B -- all of the following must be true before proceeding:**
- At least 3 distinct time steps
- Rogers sequence intact: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards; no inversions
- Each transition has a named spread mechanism; at least one must cite a specific inertia ID or feature-specific mechanism; generic word of mouth alone fails

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
- A bridging mechanism states which IDs it targets and what it displaces
- Champion table has at least 2 rows; both column 3 (archetype rationale) and column 4 (EM Inertia Bridged) populated per row with specific inertia IDs

**C1. Why this chasm exists**
[Cite EM inertia IDs by explicit ID.]

**C2. Bridging mechanism**
[Name the vehicle. State which IDs it targets.]

**C3. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

---

### SECTION D -- Churn Risk Register

**GATE D -- all of the following must be true before proceeding:**
- At least 2 archetype rows
- Each trigger cites the inertia ID the archetype reverts to
- Every mitigation names a concrete team action; surveillance-only responses fail; mixed entries pass

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

---

### SECTION F -- Sensitivity Scenarios

**GATE F -- two named scenarios; each names a different lever; each cites which inertia IDs weaken or hold.**

**Scenario 1 -- lever: [name it]**
Trajectory: [waves and inertia IDs that weaken]

**Scenario 2 -- lever: [name it]**
Trajectory: [waves and inertia IDs that hold]

---

### SECTION G -- Signal Readiness

**GATE G -- at least 2 measurable proceed signals and 1 measurable abort signal; cite inertia IDs where relevant.**

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

GATE H initial result: [PASS if N>=3 / FAIL -- identify failing sections]

**If GATE H fails:** note the deficiency here. Revise the failing sections above to include explicit inertia ID citations. You will record the corrected content in SECTION K -- do not write an inline correction block here. Re-run this table after revision:

GATE H final result: [PASS]

Do not proceed to SECTION I until GATE H final result shows PASS.

---

### SECTION I -- C-14 Champion Anchor Check

**This section verifies criterion C-14 only. Do not merge with SECTION H, J, or K.**

**GATE I -- pass condition: every champion row in SECTION C3 has both archetype rationale and a specific named EM inertia ID**

| Champion Role | Archetype Rationale Present? | EM Inertia ID Present and Specific? | Row Result |
|---------------|------------------------------|--------------------------------------|------------|
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |

GATE I initial result: [PASS if all rows show PASS / FAIL -- identify failing rows]

**If GATE I fails:** note the deficiency here. Revise the failing champion rows in SECTION C3. You will record the corrected rows in SECTION K -- do not write an inline correction block here.

GATE I final result: [PASS]

Do not proceed to SECTION J until GATE I final result shows PASS.

---

### SECTION J -- C-15 Action Test

**This section verifies criterion C-15 only. Do not merge with SECTION H, I, or K.**

**GATE J -- pass condition: zero mitigations in SECTION D consist only of surveillance verbs**

| Archetype   | Concrete action verb present? | Surveillance-only? | Row result |
|-------------|-------------------------------|---------------------|------------|
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |

Disqualified surveillance verbs (alone): monitor, track, watch, observe, measure, check, review telemetry.

GATE J initial result: [PASS if zero rows fail / FAIL -- identify failing rows]

**If GATE J fails:** note the deficiency here. Replace surveillance-only mitigations in SECTION D. You will record the corrected mitigations in SECTION K -- do not write an inline correction block here.

GATE J final result: [PASS]

Do not proceed to SECTION K until GATE J final result shows PASS.

---

### SECTION K -- Gate State Record with Corrected Content

**This section records the outcome of SECTIONS H, I, and J AND contains any corrected content resulting from revisions. It is distinct from SECTIONS H/I/J. Do not merge with SECTION H, I, or J.**

Complete this section after all three final results (H, I, J) show PASS.

For each criterion: record the initial result, whether revision was performed, and -- if revision was performed -- the corrected structural content. The corrected content must be the actual revised table rows or section content, not a description of the change.

**C-13 (GATE H):**
- Initial result: [PASS / FAIL]
- Revision performed: [Yes / No]
- Corrected content (if Yes): [If revision was required, write the corrected inertia citation entries here -- the updated rows or text that now include explicit inertia ID references. Example: "SECTION E row 2 updated: I-07: replaces the manual config-file rotation script that C-07 runs today." If No: "--"]
- Final result: [PASS]

**C-14 (GATE I):**
- Initial result: [PASS / FAIL]
- Revision performed: [Yes / No]
- Corrected content (if Yes): [If revision was required, write the corrected champion table row(s) here -- full row: Role | Archetype | Column 3 | Column 4 with explicit inertia ID. Example: "C-01 | Early Adopter | C-01's EA adoption record with PM team gives credibility as a practitioner peer | I-07: the manual config script C-07 runs today -- C-01 can demo that the feature wraps it." If No: "--"]
- Final result: [PASS]

**C-15 (GATE J):**
- Initial result: [PASS / FAIL]
- Revision performed: [Yes / No]
- Corrected content (if Yes): [If revision was required, write the corrected SECTION D row(s) here -- full row: Archetype | Churn Trigger | corrected Mitigation with concrete team action. Example: "Early Majority | Reverts to I-07 when onboarding session exceeds 2 hours | Redesign onboarding flow to complete in 45 min and embed a feature-specific script migration helper." If No: "--"]
- Final result: [PASS]

A "Corrected content" cell reading only "updated the champion entry to include inertia ID" without showing the updated row fails C-19.

**Behavioral commitment:** For every criterion showing "Revision Performed: Yes," the deficient content was revised and the corrected structural content appears in the "Corrected content" cell above. All three Final Gate Results show PASS. The artifact is complete.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-03

**Variation axis:** Phrasing register -- conversational second-person walkthrough (single-axis)

**Hypothesis:** Formal SECTION/GATE labels are not the only mechanism for structural enforcement. A conversational second-person register ("Your first task is to...") may elicit richer domain reasoning by framing the work as guided analysis rather than form-filling. V-03 tests whether conversational phrasing can produce C-19/C-20-compliant outputs without formal template labels. The audit and terminal sections use an explicit "verification mode" framing to signal structural rigor without formal GATE notation. Risk vectors: C-20 (named terminal section may be harder to locate if label is informal); C-19 (conversational "show the before/after" may not enforce content materialization as reliably as formal BEFORE/AFTER block templates).

---

You are running the `listen-adoption` skill for Signal. Your task is to simulate the adoption curve for this feature across team archetypes and produce a structured artifact that a team can act on.

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Work through each stage below in order. Every stage is required -- do not skip, merge, or label any stage as optional.

---

**Stage 1: Map every role to an archetype and name its inertia**

Your first task is to position each of the 16 stock roles on the Rogers adoption curve. For each role, assign it to one of the five canonical archetypes -- Innovator, Early Adopter, Early Majority, Late Majority, or Laggard -- and write a one-sentence rationale. All five archetypes must appear at least once.

Then, for each role, name the specific status-quo behavior this role would have to abandon to adopt the feature. Call this the Named Inertia for that role and give it a stable ID: I-PM, I-UX, I-01 through I-12, I-Support, I-SRE. The Named Inertia must describe what the role actually does today to accomplish the goal this feature would address -- not how they might feel about change. Generic entries like "may resist new tooling" or "prefers established workflows" are attitude labels, not named inertia. A passing entry for C-07 might read: "runs a homegrown bash script to rotate config files; the feature would need to replace or wrap this script, not just offer an alternative." Use that level of specificity.

Present this as a table with columns: Role | Archetype | Rationale | Inertia ID | Named Inertia.

Reminder: the inertia IDs you assign here must appear by name in at least 3 of the following downstream stages -- the chasm analysis, the champion rationale, the churn triggers, and the interventions list. You will check this in the verification stage.

---

**Stage 2: Walk the adoption month by month**

Now trace the adoption curve forward from the Innovators. Show at least 3 distinct time steps. The Rogers sequence must hold -- Innovators appear first, then Early Adopters, then Early Majority, then Late Majority, then Laggards -- no inversions.

For each wave of adoption, describe the specific mechanism that carries the feature from one archetype group to the next. At least one transition must cite the mechanism in feature-specific terms or name the inertia ID it is displacing. Generic "word of mouth" without context does not pass.

Present this as a table: Month | Archetype Wave | Roles in This Wave | Spread Mechanism.

---

**Stage 3: Analyze the chasm**

The chasm is where adoption most commonly stalls -- the gap between Early Adopters and Early Majority. Your task here is to explain why this chasm exists for this specific feature.

Name the chasm explicitly. Then cite the inertia IDs held by Early Majority roles from Stage 1. For each EM inertia, explain what bridging argument, artifact, demo, or event would displace it -- not in general terms, but specifically for this feature. Generic diffusion theory ("show value," "build trust") does not pass this section.

Follow the chasm explanation with a champion network table. Identify at least 2 champion roles -- people or teams positioned to carry the feature across the chasm. For each champion, explain: (a) why their archetype position gives them credibility with Early Majority teams, and (b) which specific EM inertia ID they are positioned to overcome and how. Both rationale parts are required per row. "Well-placed to influence early majority" without naming the inertia ID fails the second part even if the first part passes.

Champion table columns: Role | Archetype | Archetype Bridge Rationale | EM Inertia Bridged (ID and description).

---

**Stage 4: Map churn risks**

For at least 2 archetypes, describe the specific condition that would cause them to stop using the feature and revert to their named inertia behavior. Frame the trigger as "reverts to [inertia ID]" to keep the citation chain from Stage 1.

For each churn trigger, name a concrete team action that would prevent or interrupt the reversion. The mitigation must describe something the team does -- not something the team watches. Monitoring, tracking, and observing are not mitigations by themselves. Valid action verbs include: assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate. Mixed entries (action plus measurement signal) are fine as long as the action is present.

Present as a table: Archetype | Churn Trigger (cite inertia ID) | Mitigation (concrete team action).

---

**Stage 5: Rank interventions by adoption delta**

List at least 2 interventions that would materially improve adoption, ranked from highest to lowest expected adoption delta. Assign each intervention a delta rating: H (shifts adoption by at least one full archetype wave within one quarter), M (meaningful acceleration, sub-wave impact), or L (directional, marginal near-term impact). Define H/M/L consistently.

For each intervention, name the specific inertia ID or IDs it is designed to displace.

Table columns: Rank | Intervention | Delta | Inertia ID(s) Targeted.

---

**Stage 6: Model two chasm-crossing scenarios**

Sketch two named scenarios for how the chasm crossing might unfold -- one optimistic, one pessimistic. Each scenario must name the specific lever that makes it optimistic or pessimistic, and cite which inertia IDs weaken (optimistic) or hold (pessimistic) under that lever. A reader comparing the two scenarios must be able to name the factor that explains the difference.

---

**Stage 7: Name the signals that indicate readiness**

Close the analysis with at least 2 concrete, measurable signals that would indicate the feature has crossed (or is crossing) the chasm -- signals a real team could track. Add at least 1 measurable signal that would indicate the chasm has not been crossed and adoption should pause or pivot. Cite inertia IDs where relevant.

---

**Verification stage -- check three specific criteria before committing**

Before writing the final artifact, step back and verify three things systematically. For each check, state the specific criterion, the evidence from your output, and a clear PASS or FAIL. Generic self-assessment ("I reviewed the output for quality") does not pass this stage -- each criterion must be named and checked by evidence.

**Check 1 -- Named Inertia propagation (criterion C-13):**
Count how many of the following four stages contain at least one explicit inertia ID citation (e.g., "I-07"): the chasm analysis (Stage 3a), the champion network (Stage 3, column 4), the churn triggers (Stage 4), the interventions list (Stage 5). A stage passes only if a specific ID appears in it -- paraphrase without the ID does not count. The pass condition is 3 of 4 stages containing at least one explicit ID citation.

State: which stages have ID citations, which do not, and your total count.
Result: PASS (count >= 3) or FAIL.

**If Check 1 fails:** name which stages are missing citations and what IDs you are adding. Revise those stages now. Then show the updated count. When revising, write the corrected stage content here in the following format:

> Stage [name], corrected:
> ORIGINAL: [reproduce the original content that lacked inertia IDs]
> CORRECTED: [write the revised content with explicit inertia ID citations]

After revision, re-run Check 1 and show the updated count reaching >= 3.

**Check 2 -- Champion double anchor (criterion C-14):**
For each champion row in Stage 3, confirm that column 3 (archetype bridge rationale) contains reasoning tied to this role's Rogers position, and that column 4 (EM Inertia Bridged) contains a specific inertia ID from Stage 1. A row fails if column 4 is blank, generic ("relevant inertia considerations"), or contains only a paraphrase without the ID.

State: list each champion role and confirm both columns present.
Result: PASS (all rows pass) or FAIL.

**If Check 2 fails:** name which champion rows lack a specific EM inertia ID. Revise those rows now. Write the corrected rows here:

> Champion table, corrected rows:
> ORIGINAL row [role]: [reproduce the original row]
> CORRECTED row [role]: [write the corrected row with explicit EM inertia ID]

After revision, re-run Check 2 confirming all rows pass.

**Check 3 -- Churn mitigations as concrete actions (criterion C-15):**
For each mitigation in Stage 4, confirm that it contains at least one action verb from the approved list (assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate). A mitigation fails if it contains only surveillance verbs (monitor, track, watch, observe, measure, check, review telemetry) with no action verb.

State: list each mitigation and confirm action verb present.
Result: PASS (zero surveillance-only mitigations) or FAIL.

**If Check 3 fails:** name which archetypes have surveillance-only mitigations. Write the corrected rows here:

> Churn register, corrected rows:
> ORIGINAL row [archetype]: [reproduce the original row]
> CORRECTED row [archetype]: [write the corrected row with concrete team action]

After revision, re-run Check 3 confirming zero surveillance-only entries.

---

**Audit Outcomes**

After completing all three checks, record your outcomes in a named closing section called "Audit Outcomes." This section is distinct from the verification stage above (which performed the checks); this section records the consolidated result.

For each of the three criteria, record:
- Initial result (PASS or FAIL)
- Whether a revision was performed (Yes or No)
- Final result (PASS)

| Criterion | Initial Result | Revision Performed | Final Result |
|-----------|---------------|-------------------|-------------|
| C-13 -- Inertia propagation | [PASS / FAIL] | [Yes / No] | [PASS] |
| C-14 -- Champion double-anchor | [PASS / FAIL] | [Yes / No] | [PASS] |
| C-15 -- Churn action test | [PASS / FAIL] | [Yes / No] | [PASS] |

All three Final Results must show PASS before writing the artifact.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-04

**Variation axis:** Combined A+B -- inline BEFORE/AFTER correction blocks (C-19) + terminal section as gate-state pointer (C-20)

**Hypothesis:** V-01 satisfies both C-19 (inline BEFORE/AFTER shows content) and C-20 (SECTION K exists as terminal section). V-02 satisfies both via the terminal section alone. V-04 explicitly separates the two concerns: inline BEFORE/AFTER blocks are the authoritative source for C-19 (correction content visible at point of revision); SECTION K is the authoritative source for C-20 (gate state record). The critical design constraint: SECTION K does NOT duplicate the corrected content -- it records the gate state and references the inline BEFORE/AFTER block by location. This separation prevents SECTION K from becoming unwieldy when multiple revisions occur, and makes each criterion's checking location unambiguous: "Is the corrected content visible? -> go to the inline CORRECTION BLOCK. What is the final gate state? -> go to SECTION K."

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the exact section order below. Do not skip, merge, or qualify any section as optional or conditional. SECTIONS H, I, J, and K are structurally independent.

**Structural contract:**
- Corrected content lives in inline CORRECTION BLOCKS (adjacent to the gate check that triggered the revision) -- this is the C-19 location.
- SECTION K records gate states and references inline CORRECTION BLOCK locations -- this is the C-20 location.
- SECTION K does NOT duplicate corrected content. A reader checking what was corrected reads the CORRECTION BLOCK; a reader checking the gate outcome reads SECTION K.

---

### SECTION A -- Archetype Map with Named Inertia

**GATE A -- all of the following must be true before proceeding:**
- All 16 roles appear; each appears exactly once
- All 5 archetype labels used at least once
- Named Inertia column populated for every row with a feature-specific statement and inertia ID in `I-{role}` format
- Generic entries fail

**Propagation requirement:** Inertia IDs must be cited by explicit ID in at least 3 of: SECTION C1, SECTION C3 column 4, SECTION D, SECTION E. Verified in SECTION H.

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

---

### SECTION B -- Adoption Timeline

**GATE B -- Rogers sequence intact; >=3 time steps; at least one transition cites a specific inertia ID or feature-specific mechanism.**

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|------------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                              |
| M2    | Early Adopter    | ...            | ...                                                              |
| M3    | [wave]           | ...            | ...                                                              |
| M4    | [wave]           | ...            | ...                                                              |
| M5    | [wave]           | ...            | ...                                                              |

---

### SECTION C -- Chasm Analysis

**GATE C -- "chasm" named; EM inertia IDs cited explicitly; bridging mechanism states targeted IDs; champion table >=2 rows with column 3 and column 4 both populated.**

**C1. Why this chasm exists**
[Cite EM inertia IDs by explicit ID.]

**C2. Bridging mechanism**
[Name vehicle; state which IDs it targets.]

**C3. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

---

### SECTION D -- Churn Risk Register

**GATE D -- >=2 archetype rows; each trigger cites inertia ID; every mitigation has a concrete team action; surveillance-only fails.**

| Archetype      | Churn Trigger (cite inertia ID)                        | Action Test (concrete team action -- surveillance-only fails) |
|----------------|--------------------------------------------------------|---------------------------------------------------------------|
| ...            | Reverts to I-[xx]: [specific trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                                    | ...                                                           |

---

### SECTION E -- Interventions (Ranked by Adoption Delta)

**GATE E -- >=2 entries; descending delta order; each cites at least one inertia ID.**

**Delta scale:** H = one full archetype wave within one quarter; M = meaningful sub-wave acceleration; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |

---

### SECTION F -- Sensitivity Scenarios

**GATE F -- two named scenarios; each names a different lever; each cites which inertia IDs weaken or hold.**

**Scenario 1 -- lever: [name it]**
Trajectory: [waves and inertia IDs that weaken]

**Scenario 2 -- lever: [name it]**
Trajectory: [waves and inertia IDs that hold]

---

### SECTION G -- Signal Readiness

**GATE G -- >=2 measurable proceed signals; >=1 measurable abort signal; cite inertia IDs where relevant.**

**Proceed signals:**
1. [Measurable]
2. [Measurable]

**Abort signal:**
1. [Measurable]

---

### SECTION H -- C-13 Propagation Check

**This section verifies criterion C-13 only. Do not merge with SECTION I, J, or K.**

**GATE H -- pass condition: inertia IDs cited by explicit ID in >=3 of 4 downstream sections**

| Section                     | Inertia IDs Cited by ID     | Passes? |
|-----------------------------|-----------------------------|---------|
| SECTION C1 -- Chasm         | [list IDs or "none"]        | [yes/no] |
| SECTION C3 -- Champion EM   | [list IDs or "none"]        | [yes/no] |
| SECTION D -- Churn triggers | [list IDs or "none"]        | [yes/no] |
| SECTION E -- Interventions  | [list IDs or "none"]        | [yes/no] |
| **Total passing**           |                             | **[N of 4]** |

GATE H initial result: [PASS if N>=3 / FAIL]

**If GATE H fails:** produce the following CORRECTION BLOCK immediately below. The CORRECTION BLOCK is the C-19 location -- it contains the corrected content. SECTION K will reference this block by name.

> **CORRECTION BLOCK -- C-13 (GATE H)**
>
> Deficiency: [which sections lacked citations; which IDs are needed]
>
> BEFORE -- [section name]:
> [Reproduce the original rows/text that lacked explicit inertia ID citations -- verbatim]
>
> AFTER -- [section name]:
> [Write the corrected rows/text with explicit inertia ID citations added]
>
> GATE H re-run:
> [Reproduce the full citation table above with updated values; confirm N >= 3]
> GATE H re-run result: PASS

If GATE H initial result is PASS, write: "GATE H: PASS -- no correction required."

GATE H final result: [PASS]

---

### SECTION I -- C-14 Champion Anchor Check

**This section verifies criterion C-14 only. Do not merge with SECTION H, J, or K.**

**GATE I -- pass condition: every champion row in SECTION C3 has both archetype rationale and specific named EM inertia ID**

| Champion Role | Archetype Rationale Present? | EM Inertia ID Present and Specific? | Row Result |
|---------------|------------------------------|--------------------------------------|------------|
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |

GATE I initial result: [PASS if all rows PASS / FAIL]

**If GATE I fails:** produce the following CORRECTION BLOCK immediately below.

> **CORRECTION BLOCK -- C-14 (GATE I)**
>
> Deficiency: [which champion rows lack specific EM inertia IDs]
>
> BEFORE -- SECTION C3, row [role]:
> | [role] | [archetype] | [column 3] | [column 4 -- blank or generic] |
>
> AFTER -- SECTION C3, row [role]:
> | [role] | [archetype] | [column 3] | I-[xx]: [specific named inertia this champion bridges] |
>
> GATE I re-run:
> [Reproduce the full champion anchor table above; confirm all rows PASS]
> GATE I re-run result: PASS

If GATE I initial result is PASS, write: "GATE I: PASS -- no correction required."

GATE I final result: [PASS]

---

### SECTION J -- C-15 Action Test

**This section verifies criterion C-15 only. Do not merge with SECTION H, I, or K.**

**GATE J -- pass condition: zero mitigations in SECTION D consist only of surveillance verbs**

| Archetype   | Concrete action verb present? | Surveillance-only? | Row result |
|-------------|-------------------------------|---------------------|------------|
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |

Disqualified surveillance verbs (alone): monitor, track, watch, observe, measure, check, review telemetry.

GATE J initial result: [PASS if zero rows fail / FAIL]

**If GATE J fails:** produce the following CORRECTION BLOCK immediately below.

> **CORRECTION BLOCK -- C-15 (GATE J)**
>
> Deficiency: [which archetypes have surveillance-only mitigations]
>
> BEFORE -- SECTION D, row [archetype]:
> | [archetype] | [churn trigger] | [surveillance-only mitigation] |
>
> AFTER -- SECTION D, row [archetype]:
> | [archetype] | [churn trigger] | [assign / deliver / ...]: [concrete team action] |
>
> GATE J re-run:
> [Reproduce the full action test table above; confirm zero surveillance-only rows]
> GATE J re-run result: PASS

If GATE J initial result is PASS, write: "GATE J: PASS -- no correction required."

GATE J final result: [PASS]

---

### SECTION K -- Gate State Record

**This section records the outcome of SECTIONS H, I, and J. It is distinct from SECTIONS H/I/J (which performed the checks); this section consolidates the final state. SECTION K does NOT contain or duplicate corrected content -- it references the CORRECTION BLOCK locations above. Do not merge with SECTION H, I, or J.**

Complete this section after all three final results (H, I, J) show PASS.

| Criterion | Initial Gate Result | Revision Performed | Correction Block Location | Final Gate Result |
|-----------|--------------------|--------------------|---------------------------|-------------------|
| C-13 (GATE H) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-13 (GATE H), above SECTION H re-run" / If No: "--"] | [PASS] |
| C-14 (GATE I) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-14 (GATE I), above SECTION I re-run" / If No: "--"] | [PASS] |
| C-15 (GATE J) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-15 (GATE J), above SECTION J re-run" / If No: "--"] | [PASS] |

**Structural contract verification:** For every "Revision Performed: Yes" entry above, a CORRECTION BLOCK containing BEFORE and AFTER content exists in the output at the referenced location. For every "Revision Performed: No" entry, the initial gate was PASS and no correction was required. All Final Gate Results show PASS.

GATE K result: PASS when all final results show PASS and the structural contract verification is stated.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-05

**Variation axis:** Combined A+B+C -- inline BEFORE/AFTER correction blocks + terminal section pointer + phrasing register shift

**Hypothesis:** V-04 combines inline corrections (C-19) and terminal section pointer (C-20) within a fully formal SECTION/GATE register. V-05 tests whether a register shift -- conversational for content sections (SECTIONS A-G), formal structured for verification sections (SECTIONS H-K) -- improves content quality without sacrificing audit enforcement. The register shift is marked by an explicit "VERIFICATION MODE" header between SECTION G and SECTION H. Prediction: conversational content sections elicit richer domain-specific inertia entries (C-11) and champion rationale (C-14) because the model reasons through the analysis rather than filling table slots. Formal verification sections maintain C-16/C-17/C-18/C-19/C-20 compliance because structural templates are explicit. Risk: the register transition may break inertia ID citation discipline if the model interprets conversational mode as reducing ID citation requirements in the content sections.

---

You are running the `listen-adoption` skill for Signal. Your task is to analyze the adoption curve for this feature, understand where it will stall, and produce an artifact a team can act on.

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

The output has two parts: the adoption analysis (Sections A-G, conversational register) and the verification audit (Sections H-K, formal structured register). Every section is required -- do not skip or qualify any section as optional.

---

### SECTION A -- Archetype Map and Named Inertia

Before anything else, position each of the 16 stock roles on the Rogers adoption curve -- Innovator, Early Adopter, Early Majority, Late Majority, or Laggard. All five archetypes must appear at least once. For each role, write a one-sentence rationale for that placement.

Then name the specific behavior each role would need to stop or replace to adopt this feature. This is the Named Inertia for that role. Give each entry an inertia ID: I-PM, I-UX, I-01 through I-12, I-Support, I-SRE. A useful Named Inertia describes what the role does TODAY to address the same problem this feature solves. "Resistance to change" is not named inertia. "C-07 runs a weekly cron job to reconcile config state manually; the feature would render that job redundant" is named inertia.

Present as: Role | Archetype | Rationale | Inertia ID | Named Inertia.

Note: inertia IDs assigned here will need to appear in at least 3 of the following 4 places in your analysis: the chasm explanation, the champion network, the churn triggers, and the interventions. You will verify this count in SECTION H.

---

### SECTION B -- Month-by-Month Adoption

Walk the reader through how adoption would unfold over time. Show at least 3 months. Innovators come first, then Early Adopters, then Early Majority, then Late Majority, then Laggards -- respect this sequence. For each wave, describe the mechanism that carries the feature from one group to the next. At least one transition must explain the mechanism in terms specific to this feature or name the inertia ID it is displacing.

Present as a table: Month | Archetype Wave | Roles Adopting | Spread Mechanism.

---

### SECTION C -- Chasm Analysis

The hardest part of adoption is crossing the chasm from Early Adopters to Early Majority. Walk through why this chasm exists for this specific feature. Name it explicitly -- use the word "chasm" or an equivalent. Cite the inertia IDs held by Early Majority roles from SECTION A. For each EM inertia, explain what specifically would displace it -- what demo, artifact, argument, or event would make that role give up the named behavior. Don't rely on generic adoption playbooks; the mechanism must be tailored to this feature and these named inertia entries.

Follow this with a champion network: at least 2 roles who can carry the feature across the chasm. For each champion, explain why their position in the Rogers model gives them credibility with Early Majority teams, and name the specific EM inertia ID they are positioned to overcome. Both parts of the rationale are required per champion. Naming an archetype position without naming a specific inertia ID does not complete the champion entry.

Champion table: Role | Archetype | Archetype Bridge Rationale | EM Inertia Bridged (ID and description).

---

### SECTION D -- Churn Risk Register

For at least 2 archetypes, describe the specific condition that would cause them to abandon the feature and revert to their named inertia behavior. Frame each trigger as "reverts to [inertia ID]" to keep the citation chain intact.

For each trigger, name a concrete team action that prevents or interrupts the reversion. The team must do something -- not watch something. Monitoring and tracking alone are not mitigations. Assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, and escalate are the kinds of verbs that belong here. Entries that mix a concrete action with a measurement confirmation ("assign a champion and track re-engagement rate as a confirmation signal") are fine.

Table: Archetype | Churn Trigger (cite inertia ID) | Mitigation (concrete team action).

---

### SECTION E -- Interventions Ranked by Adoption Delta

Name at least 2 interventions that would materially improve adoption, ranked highest to lowest impact. Rate each intervention as H (moves adoption by at least one full archetype wave within a quarter), M (meaningful acceleration within a wave), or L (directional, marginal). For each intervention, name the inertia ID(s) it is designed to displace.

Table: Rank | Intervention | Delta | Inertia ID(s) Targeted.

---

### SECTION F -- Two Chasm Scenarios

Sketch two adoption scenarios -- one where the chasm crossing goes well, one where it stalls. Each scenario must name the specific lever that drives the difference, and cite which inertia IDs weaken or hold under that lever. A reader comparing the two should be able to name the single most important factor separating the outcomes.

---

### SECTION G -- Signal Readiness

Finish the analysis with signals a team could actually track. Name at least 2 measurable signals that indicate the feature is crossing (or has crossed) the chasm, and at least 1 measurable signal that indicates adoption has stalled and the team should reconsider. Cite inertia IDs where the signal connects to a specific named behavior.

---

---
**VERIFICATION MODE**

The following sections (H through K) operate under formal structured requirements. Templates must be completed as specified. Do not substitute prose descriptions for template cells. Each section verifies or records exactly one criterion and must not be merged with adjacent sections.

---

### SECTION H -- C-13 Propagation Check

**This section verifies criterion C-13 only. Do not merge with SECTION I, J, or K.**

**GATE H -- pass condition: inertia IDs cited by explicit ID in >=3 of the following 4 sections**

| Section                     | Inertia IDs Cited by ID     | Passes? |
|-----------------------------|-----------------------------|---------|
| SECTION C (chasm)           | [list IDs or "none"]        | [yes/no] |
| SECTION C (champion col 4)  | [list IDs or "none"]        | [yes/no] |
| SECTION D (churn triggers)  | [list IDs or "none"]        | [yes/no] |
| SECTION E (interventions)   | [list IDs or "none"]        | [yes/no] |
| **Total passing**           |                             | **[N of 4]** |

GATE H initial result: [PASS if N>=3 / FAIL]

**If GATE H fails:** produce the CORRECTION BLOCK below. SECTION K will reference this block by name.

> **CORRECTION BLOCK -- C-13 (GATE H)**
>
> Deficiency: [sections missing citations; IDs needed]
>
> BEFORE -- [section name]:
> [Reproduce original content lacking explicit inertia ID citations -- verbatim]
>
> AFTER -- [section name]:
> [Write corrected content with explicit inertia ID citations]
>
> GATE H re-run:
> [Updated citation table; N >= 3]
> GATE H re-run result: PASS

If initial PASS: "GATE H: PASS -- no correction required."
GATE H final result: [PASS]

---

### SECTION I -- C-14 Champion Anchor Check

**This section verifies criterion C-14 only. Do not merge with SECTION H, J, or K.**

**GATE I -- pass condition: every champion row in SECTION C has both archetype rationale and a specific named EM inertia ID**

| Champion Role | Archetype Rationale Present? | EM Inertia ID Present and Specific? | Row Result |
|---------------|------------------------------|--------------------------------------|------------|
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |

GATE I initial result: [PASS / FAIL]

**If GATE I fails:** produce the CORRECTION BLOCK below.

> **CORRECTION BLOCK -- C-14 (GATE I)**
>
> Deficiency: [failing champion rows]
>
> BEFORE -- champion table, row [role]:
> | [role] | [archetype] | [column 3] | [column 4 -- blank or generic] |
>
> AFTER -- champion table, row [role]:
> | [role] | [archetype] | [column 3] | I-[xx]: [specific named inertia] |
>
> GATE I re-run: [all rows PASS]
> GATE I re-run result: PASS

If initial PASS: "GATE I: PASS -- no correction required."
GATE I final result: [PASS]

---

### SECTION J -- C-15 Action Test

**This section verifies criterion C-15 only. Do not merge with SECTION H, I, or K.**

**GATE J -- pass condition: zero mitigations in SECTION D consist only of surveillance verbs**

| Archetype   | Concrete action verb present? | Surveillance-only? | Row result |
|-------------|-------------------------------|---------------------|------------|
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |

Disqualified surveillance verbs (alone): monitor, track, watch, observe, measure, check, review telemetry.

GATE J initial result: [PASS / FAIL]

**If GATE J fails:** produce the CORRECTION BLOCK below.

> **CORRECTION BLOCK -- C-15 (GATE J)**
>
> Deficiency: [archetypes with surveillance-only mitigations]
>
> BEFORE -- churn register, row [archetype]:
> | [archetype] | [trigger] | [surveillance-only mitigation] |
>
> AFTER -- churn register, row [archetype]:
> | [archetype] | [trigger] | [assign / deliver / ...]: [concrete team action] |
>
> GATE J re-run: [zero surveillance-only rows]
> GATE J re-run result: PASS

If initial PASS: "GATE J: PASS -- no correction required."
GATE J final result: [PASS]

---

### SECTION K -- Gate State Record

**This section records the outcome of SECTIONS H, I, and J. It is distinct from SECTIONS H/I/J. SECTION K does NOT duplicate or contain corrected content -- it references CORRECTION BLOCK locations. Do not merge with SECTION H, I, or J.**

Complete after all three final results show PASS.

| Criterion | Initial Gate Result | Revision Performed | Correction Block Location | Final Gate Result |
|-----------|--------------------|--------------------|---------------------------|-------------------|
| C-13 (GATE H) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-13 (GATE H)" / If No: "--"] | [PASS] |
| C-14 (GATE I) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-14 (GATE I)" / If No: "--"] | [PASS] |
| C-15 (GATE J) | [PASS / FAIL] | [Yes / No] | [If Yes: "CORRECTION BLOCK -- C-15 (GATE J)" / If No: "--"] | [PASS] |

**Structural contract:** For every "Revision Performed: Yes" entry, a CORRECTION BLOCK with BEFORE and AFTER content exists at the referenced location. For every "Revision Performed: No" entry, the initial gate was PASS. All Final Gate Results show PASS.

GATE K result: PASS when all final results show PASS and structural contract is stated.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`
