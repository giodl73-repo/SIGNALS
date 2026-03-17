Written to `simulations/quest/variations/listen-adoption-variations-R4-2026-03-14.md`.

---

## Summary

**Five R4 variations -- targeting C-16 (self-audit pre-commit) and C-17 (dedicated structural slot per aspirational criterion)**

| ID | Axis | C-16 | C-17 | Expected |
|----|------|------|------|----------|
| **V-01** | C-17: Propagation Ledger -- dedicated output section for C-13 | FAIL | PASS | ~130 |
| **V-02** | C-16: Named pre-commit verification block | PASS | UNCERTAIN | ~130 |
| **V-03** | C-17: Explicit structural separation prohibition + C-13 standalone section | FAIL | PASS | ~130 |
| **V-04** | Combined: Propagation Ledger + pre-commit verification | PASS | PASS | **135** |
| **V-05** | Combined: GATE + separated SECTION H/I/J + revision obligation | PASS | PASS | **135** |

---

**R3 gap analysis that drives R4:**

R3 V-04 (125 pts) and V-05 (125 pts) both pass C-13/C-14/C-15. The R4 ceiling is 135 (10 more pts from C-16 + C-17). Two structural gaps in R3 block the extra 10 points:

1. **C-13 has no output structural slot in R3 V-04.** The propagation requirement is a prose instruction in Step 1 -- it produces no independently identifiable section in the model's output. C-17 requires an output-visible element. The fix: a standalone "Propagation Ledger" section the model produces.

2. **R3 V-05's SA-1/SA-2/SA-3 share a parent block.** The three criteria checks are in one "SELF-AUDIT" section. C-17's prohibition on shared structural elements creates ambiguity. The fix: separate each SA into its own named section (SECTION H/I/J) with its own GATE.

**Design contrast between V-04 and V-05:** V-04 enforces C-16/C-17 through structural slots embedded in the output flow -- the Propagation Ledger is a content section, the Pre-Commit Verification block is a standalone gate. V-05 takes the separated-verification path -- three named sections, each verifying one criterion, each with a revision obligation that blocks progress. V-04 is simpler; V-05 is more robust against a model that fills structural slots generically and then passes the pre-commit block by rationalization.
A reader might map all three criteria to the single "SELF-AUDIT" element. UNCERTAIN -- may fail C-17 if the shared parent block is treated as one structural element covering all three.

**The R4 structural requirement that R3 cannot reliably satisfy:** C-13 needs an independently identifiable output section -- not a prose footnote in the prompt instructions. A dedicated output section ("Propagation Ledger", "C-13 Citation Register") that the model produces and a reader can locate without reading surrounding prose. C-17 also requires that C-13, C-14, and C-15 structural elements are not co-located in a shared parent block.

---

## V-01

**Variation axis:** Output format -- Propagation Ledger as a dedicated output section for C-13 (C-17 structural independence)
**Hypothesis:** R3 V-04 has structural output slots for C-14 (4-column champion table column) and C-15 (action-verb column), but C-13's propagation requirement is a prose instruction in Step 1 -- it creates no independently identifiable element in the output. Adding a "Propagation Ledger" section (a named table the model must produce after Step 5, showing each downstream section and whether inertia IDs appear in it) gives C-13 its own structural output slot. A reader can locate "Propagation Ledger" without reading surrounding prose. C-17 should pass: three separately identifiable structural elements -- Ledger for C-13, champion table column 4 for C-14, action-verb column for C-15. C-16 remains absent -- there is no explicit pre-commit block naming each criterion by ID with a stated pass condition.

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

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-02

**Variation axis:** Role sequence / lifecycle emphasis -- C-16 criterion-specific pre-commit verification block
**Hypothesis:** R3 V-04's structural columns enforce correct structure but do not force the model to deliberate on whether each aspirational criterion is satisfied before committing the artifact. V-02 adds a mandatory "Pre-Commit Verification" block between Step 7 and the artifact write instruction. The block names C-13, C-14, and C-15 explicitly by criterion ID and states each pass condition in one sentence. The model must answer pass or fail for each criterion with specific evidence cited from the output. A response of "C-13: looks good" fails; "C-13: IDs cited in Steps 3a (I-05, I-06), 3c (I-07), and 5 (I-03) = 3 of 4 sections -- PASS" passes. C-16 should pass. C-17 is uncertain: the Pre-Commit block groups all three criterion checks in one section; C-14 and C-15 have independent output structural slots (champion column, action column), but C-13 still has no content-level output section separate from the pre-commit block -- a reader looking for C-13's structural element in the output content would find only the pre-commit item, which shares a parent block with C-14 and C-15.

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

**Propagation requirement:** The inertia IDs assigned here must be cited by ID in at least 3 of the following 4 downstream sections: chasm analysis (Step 3a), champion network (Step 3c), churn trigger register (Step 4), intervention list (Step 5). A downstream section satisfies this requirement only if it names at least one specific inertia ID (e.g., "I-05") -- paraphrase without ID citation does not count.

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

Complete all three checks before writing the artifact. For each check, state specific evidence from your output -- do not answer generically. A response of "C-13: looks good" or "C-15: I reviewed the mitigations" fails every check below.

**C-13 check -- Inertia propagation (pass condition: inertia IDs cited by explicit ID reference in >=3 of 4 downstream sections):**
- Step 3a cited IDs: [list or "none"]
- Step 3c cited IDs: [list or "none"]
- Step 4 cited IDs: [list or "none"]
- Step 5 cited IDs: [list or "none"]
- Total sections with citation: [N of 4]
- C-13 result: [PASS if N>=3 / FAIL -- identify which sections to revise before proceeding]

**C-14 check -- Champion double-anchor (pass condition: every champion row has archetype rationale AND a named EM inertia ID, not a generic phrase):**
- [Champion role 1]: Archetype rationale present? [yes/no]. EM Inertia ID cited? [yes/no -- if yes, which ID].
- [Champion role 2]: [same]
- [Additional rows if present]
- C-14 result: [PASS if all rows satisfy both conditions / FAIL -- identify rows to revise before proceeding]

**C-15 check -- Churn action test (pass condition: zero mitigations consist only of surveillance verbs):**
- [Archetype 1]: Contains concrete action verb? [yes/no -- if yes, which verb]. Surveillance-only? [yes/no].
- [Archetype 2]: [same]
- [Additional rows if present]
- C-15 result: [PASS if zero surveillance-only entries / FAIL -- identify rows to replace before proceeding]

Do not write the artifact until C-13, C-14, and C-15 all show PASS.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-03

**Variation axis:** Phrasing register -- explicit structural separation prohibition + C-13 as a standalone named output section
**Hypothesis:** R3 V-04's C-13 propagation requirement is a prose footnote in Step 1 that produces no independently identifiable output section. R3 V-05's SA-1/SA-2/SA-3 are labeled sub-items but share a "SELF-AUDIT" parent block. V-03 tests a third approach: move the C-13 requirement from a Step 1 footnote to a standalone named section ("Step 5.5 -- Inertia Propagation Ledger"), add an explicit structural separation prohibition at the top of the prompt ("C-13, C-14, and C-15 each require their own structural slot -- do not merge them"), and label the C-14 and C-15 slots with explicit section annotations. The prohibition makes merging an explicit instruction violation, not just a stylistic choice. C-17 should pass: three separately labeled output sections each mapping to exactly one criterion. C-16 remains absent -- there is no criterion-specific pre-commit audit stating the pass condition for each criterion before the artifact write.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

**Structural independence requirement:** Three output sections in this artifact each address one aspirational criterion. Each must be a separately labeled, independently identifiable element in your output. Do not merge them into a combined section, shared column, or joint block:
- **Step 5.5 -- Inertia Propagation Ledger** maps to criterion C-13
- **Champion table column 4 -- EM Inertia Bridged** (Step 3c) maps to criterion C-14
- **Churn register column -- Action Test** (Step 4) maps to criterion C-15

A combined "Inertia + Champion + Churn" section fails the structural requirement even if each criterion individually passes.

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

**3c. Champion network** *(structural slot: C-14 -- do not merge with Step 5.5 or Step 4)*

The champion table has four required columns. The fourth column -- EM Inertia Bridged -- is the C-14 structural slot. State the specific inertia ID from Step 1 that this champion is positioned to overcome. "Well-placed to influence the early majority" without naming the inertia ID fails the fourth column even if column 3 passes.

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

At least 2 champions. Both column 3 and column 4 must be populated per row.

---

### Step 4 -- Churn Risk Register *(structural slot: C-15 -- do not merge with Step 5.5 or Step 3c)*

For at least 2 archetypes, state the churn trigger and the mitigation.

**Churn trigger:** The specific event that causes the role to revert to the Named Inertia from Step 1. Frame as "reverts to [inertia ID]" to maintain the citation chain from Step 1.

**Action Test column:** This is the C-15 structural slot. Each entry must name a concrete team action. Valid action verbs: assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate. The following are surveillance responses and are not accepted as mitigations by themselves: monitor, track, watch, observe, measure, check, review telemetry. Mixed entries (action + measurement signal) pass.

| Archetype      | Churn Trigger (cite inertia ID)               | Action Test (concrete team action -- surveillance-only fails) |
|----------------|-----------------------------------------------|---------------------------------------------------------------|
| ...            | Reverts to [I-xx]: [trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                           | ...                                                           |

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

### Step 5.5 -- Inertia Propagation Ledger *(structural slot: C-13 -- do not merge with Step 3c or Step 4)*

This is the C-13 structural slot. Produce the following table. For each downstream section, record the inertia IDs cited by explicit ID reference (not paraphrase) and whether at least one citation is present. This table must stand alone as a separately labeled section -- do not fold it into the champion table or churn register.

| Section                          | Inertia IDs Cited (list them)       | Citation Present? |
|----------------------------------|-------------------------------------|-------------------|
| Step 3a -- Chasm explanation     | [list IDs cited, or "none"]         | [yes / no]        |
| Step 3c -- Champion EM Inertia   | [list IDs cited, or "none"]         | [yes / no]        |
| Step 4 -- Churn triggers         | [list IDs cited, or "none"]         | [yes / no]        |
| Step 5 -- Interventions          | [list IDs cited, or "none"]         | [yes / no]        |
| **Total sections with citation** |                                     | **[N of 4]**      |

C-13 requires N >= 3. If total is less than 3: revise the sections showing "no" before proceeding to Step 6.

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

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-04

**Variation axis:** Combined -- Propagation Ledger (C-17 structural slot for C-13) + Pre-Commit Verification block (C-16)
**Hypothesis:** V-01 adds the Propagation Ledger giving C-13 its own output section; V-02 adds the Pre-Commit Verification block naming C-13/C-14/C-15 by criterion ID with stated pass conditions. V-04 applies both simultaneously. C-17 should pass: C-13 = standalone Propagation Ledger table, C-14 = champion table column 4, C-15 = action-verb column in churn register -- three separately identifiable structural elements in the output. C-16 should pass: Pre-Commit Verification block names each criterion explicitly, states the pass condition, and requires evidence-based confirmation before the artifact write. This is the expected 135-point candidate via the structural enforcement path.

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

Produce the following table. For each downstream section, record the inertia IDs cited by explicit ID reference (not paraphrase) and whether at least one citation is present. This is a standalone structural section -- do not merge it with the champion table or churn register.

| Section                          | Inertia IDs Cited (list them)       | Citation Present? |
|----------------------------------|-------------------------------------|-------------------|
| Step 3a -- Chasm explanation     | [list IDs cited, or "none"]         | [yes / no]        |
| Step 3c -- Champion EM Inertia   | [list IDs cited, or "none"]         | [yes / no]        |
| Step 4 -- Churn triggers         | [list IDs cited, or "none"]         | [yes / no]        |
| Step 5 -- Interventions          | [list IDs cited, or "none"]         | [yes / no]        |
| **Total sections with citation** |                                     | **[N of 4]**      |

If total is less than 3: revise the sections showing "no" before proceeding. Propagation Ledger must show N >= 3 before you continue.

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

Complete all three checks before writing the artifact. Answer each check with specific evidence from your output -- do not answer generically. Show this block in your response.

**C-13 check -- Inertia propagation (pass condition: inertia IDs cited by explicit ID reference in >=3 of 4 downstream sections):**
- Step 3a cited IDs: [list or "none"]
- Step 3c cited IDs: [list or "none"]
- Step 4 cited IDs: [list or "none"]
- Step 5 cited IDs: [list or "none"]
- Total sections with citation: [N of 4]
- C-13 result: [PASS if N>=3 / FAIL -- identify which sections to revise before proceeding]

**C-14 check -- Champion double-anchor (pass condition: every champion row has archetype rationale AND a named EM inertia ID, not a generic phrase):**
- [Champion role 1]: Archetype rationale present? [yes/no]. EM Inertia ID cited? [yes/no -- if yes, which ID].
- [Champion role 2]: [same]
- [Additional rows if present]
- C-14 result: [PASS if all rows satisfy both conditions / FAIL -- identify rows to revise before proceeding]

**C-15 check -- Churn action test (pass condition: zero mitigations consist only of surveillance verbs):**
- [Archetype 1]: Contains concrete action verb? [yes/no -- which verb]. Surveillance-only? [yes/no].
- [Archetype 2]: [same]
- [Additional rows if present]
- C-15 result: [PASS if zero surveillance-only entries / FAIL -- identify rows to replace before proceeding]

Do not write the artifact until C-13, C-14, and C-15 all show PASS.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-05

**Variation axis:** Combined -- GATE structure with separately headed C-13/C-14/C-15 verification sections + revision obligation before artifact write
**Hypothesis:** R3 V-05 clusters SA-1/SA-2/SA-3 in one shared "SELF-AUDIT" block. A reader maps all three criteria to the same parent section, creating C-17 ambiguity. V-05 (R4) splits the three verification checks into independently headed sections: "SECTION H -- C-13 Propagation Check", "SECTION I -- C-14 Champion Anchor Check", "SECTION J -- C-15 Action Test". Each section has its own GATE. An explicit prohibition prevents merging any two sections. A revision obligation per section -- each failed GATE blocks progress to the next section -- enforces C-16's "must appear before the output is committed" requirement by making revision mandatory at each check rather than optional. The three headed sections are independently identifiable structural elements, each mapping to exactly one criterion, satisfying C-17.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the exact section order below. Each GATE must be satisfied before proceeding to the next section. Do not skip, merge, or qualify any section as optional or conditional. SECTIONS H, I, and J are structurally independent -- each verifies exactly one criterion. Do not merge H, I, and J into a combined block.

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
- Champion table has at least 2 rows; both the archetype rationale column and EM Inertia Bridged column are populated per row; EM Inertia Bridged must cite a specific inertia ID from SECTION A (not a generic phrase)

**C1. Why this chasm exists**
[Draw from EM inertia IDs in SECTION A. Name the specific IDs. Example: "The chasm is anchored by I-05, I-06, and I-07 -- each describes a workflow that already satisfies [core use case], so EA enthusiasm alone cannot displace them." Do not reproduce generic diffusion theory.]

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
- Each churn trigger cites the inertia ID the archetype reverts to (format: "reverts to I-[xx]: [trigger event]")
- Every mitigation in the Action Test column names a concrete team action; surveillance-only responses are disqualified: monitor, track, watch, observe, measure, check, review telemetry are not mitigations by themselves; mixed entries (action + measurement signal) pass

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
- Each scenario shows a distinct adoption trajectory and cites which inertia IDs from SECTION A weaken or hold under that lever

**Scenario 1 -- lever: [name it]**
Trajectory: [which waves accelerate; which inertia IDs weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves stall; which inertia IDs hold under this lever]

---

### SECTION G -- Signal Readiness

**GATE G -- all of the following must be true before proceeding:**
- At least 2 measurable proceed signals
- At least 1 measurable abort signal
- All signals are concrete and trackable; vague signals ("adoption increases," "team feels ready") fail; signals should cite inertia IDs where relevant

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

If GATE H fails: identify which sections show "no", revise those sections to include at least one explicit inertia ID citation, then re-run SECTION H. Do not proceed to SECTION I until GATE H shows PASS.

---

### SECTION I -- C-14 Champion Anchor Check

**This section verifies criterion C-14 only. Do not merge with SECTION H or SECTION J.**

**GATE I -- pass condition: every champion row in SECTION C3 has both archetype rationale and a specific named EM inertia ID**

For each champion row:

| Champion Role | Archetype Rationale Present? | EM Inertia ID Present and Specific? | Row Result |
|---------------|------------------------------|--------------------------------------|------------|
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |
| [role]        | [yes/no]                     | [yes -- I-xx / no / generic phrase]  | [PASS/FAIL] |

"Well-placed to influence the early majority" without naming an inertia ID = generic phrase = FAIL for that row.

GATE I result: [PASS if all rows show PASS / FAIL -- note which rows fail]

If GATE I fails: revise the failing champion rows to add the specific EM inertia ID, then re-run SECTION I. Do not proceed to SECTION J until GATE I shows PASS.

---

### SECTION J -- C-15 Action Test

**This section verifies criterion C-15 only. Do not merge with SECTION H or SECTION I.**

**GATE J -- pass condition: zero mitigations in SECTION D consist only of surveillance verbs**

For each mitigation row:

| Archetype   | Concrete action verb present? | Surveillance-only? | Row result |
|-------------|-------------------------------|---------------------|------------|
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS if action present and not surveillance-only / FAIL if surveillance-only] |
| [archetype] | [yes -- which verb / no]      | [yes/no]            | [PASS/FAIL] |

Disqualified surveillance verbs (alone): monitor, track, watch, observe, measure, check, review telemetry. Mixed entries (action verb + measurement signal) pass.

GATE J result: [PASS if zero rows fail / FAIL -- note which rows to replace]

If GATE J fails: replace surveillance-only mitigations with entries containing a concrete team action, then re-run SECTION J. Do not write the artifact until GATE J shows PASS.

---

All three verification sections (H, I, J) must show PASS before the artifact is written.

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`
