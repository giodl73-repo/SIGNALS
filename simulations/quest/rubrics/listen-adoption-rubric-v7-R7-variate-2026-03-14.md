# Variations: listen-adoption — Round 7

**Rubric:** v7 | **New criteria:** C-21, C-22, C-23 | **Max composite:** 165 | **Golden threshold:** 80

---

## Variation Axes

| Axis | Description |
|------|-------------|
| Output format | Table-heavy vs structured prose vs conversational |
| Role sequence | Role→archetype mapping vs archetype-first bucket assignment |
| Inertia framing | Named status-quo competitor tracked throughout vs archetype-local inertia |
| Lifecycle emphasis | Flat section list vs explicit PHASE boundary headers |
| Phrasing register | Formal/imperative vs conversational second-person |

**Single-axis (V-01, V-02, V-03):** Output format · Role sequence · Inertia framing
**Combined (V-04, V-05):** Lifecycle + format + structural contract · Conversational register + inertia + VERIFICATION MODE

**C-21/C-22/C-23 design intent per variation:**

| Variation | C-21 risk | C-22 risk | C-23 risk | Design note |
|-----------|-----------|-----------|-----------|-------------|
| V-01 | Low | Low | Low | Full structural contract, explicit negative rule, labeled invariant, named boundary |
| V-02 | Low | Low | Low | Same structural contract as V-01; archetype-first is the sole axis |
| V-03 | **High** | **High** | **Medium** | No structural contract; no negative rule on terminal section; terminal section has no named invariant; verification stage uses labeled header but without explicit mode-shift instruction |
| V-04 | Low | Low | Low | Strongest — names C-19/C-20/C-21/C-22/C-23 by criterion ID in structural contract |
| V-05 | Low | Low | Low | VERIFICATION MODE boundary with explicit mode-shift instruction; conversational A-G is the secondary axis |

---

## Stock Roles (16)

PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Rogers archetypes (5): Innovators · Early Adopters · Early Majority · Late Majority · Laggards

---

## V-01 — Single-axis: Output Format (Table-heavy)

**Variation axis:** Output format — all major outputs rendered as tables; tabular layout locks in 16-role coverage, timeline ordering, and ranked interventions.

**Hypothesis:** Dense tabular structure eliminates omission paths for C-01, C-02, and C-04; combined with R6 V-04's structural contract it produces maximum structural clarity at the cost of reduced analytical narrative.

---

```
STRUCTURAL CONTRACT (read before generating any output):

Location rules:
- SECTIONS A through G: content generation. All major outputs are rendered as tables.
- Inline CORRECTION BLOCKS appear immediately after the gate check that triggers them (Sections H, I, or J). This is the C-19 location. Corrected content lives here.
- SECTION K is the terminal gate state record. It records initial result, revision performed (yes/no), CORRECTION BLOCK location (section reference), and final result per gate. SECTION K does NOT contain corrected content — it references CORRECTION BLOCK locations only.
- The ## VERIFICATION MODE header appears between SECTION G and SECTION H. All content sections precede this marker; all audit sections (H through K) follow it.

Self-verifying invariant (asserted in SECTION K):
  "For every 'Revision Performed: Yes' entry in SECTION K, a CORRECTION BLOCK
   containing BEFORE and AFTER content exists earlier in this document at the
   CORRECTION BLOCK Location column entry."
An evaluator can confirm or refute this claim by inspection without trusting the model's assertion.

---

SECTION A — Role-to-Archetype Mapping

Produce a table covering all 16 stock roles. Each role maps to exactly one of the five canonical Rogers archetype labels. No role omitted; no role duplicated.

| Role | Rogers Archetype | Rationale |
|------|-----------------|-----------|
| PM | [archetype] | [rationale] |
| UX | [archetype] | [rationale] |
| C-01 | [archetype] | [rationale] |
| C-02 | [archetype] | [rationale] |
| C-03 | [archetype] | [rationale] |
| C-04 | [archetype] | [rationale] |
| C-05 | [archetype] | [rationale] |
| C-06 | [archetype] | [rationale] |
| C-07 | [archetype] | [rationale] |
| C-08 | [archetype] | [rationale] |
| C-09 | [archetype] | [rationale] |
| C-10 | [archetype] | [rationale] |
| C-11 | [archetype] | [rationale] |
| C-12 | [archetype] | [rationale] |
| Support | [archetype] | [rationale] |
| SRE | [archetype] | [rationale] |

---

SECTION B — Named Inertia per Archetype

For each of the five archetypes that appear in SECTION A, identify the specific status-quo behavior this feature must displace. Assign each entry an inertia ID (I-01, I-02, ...) for downstream citation. Generic "resistance to change" fails — name what each archetype is currently doing instead of using this feature.

At least 3 archetypes must have a distinct entry. Innovators and Early Adopters may share an entry only if the friction is genuinely identical.

| Archetype | Inertia ID | Current Behavior (what they do today) | Why This Blocks Feature Adoption |
|-----------|-----------|--------------------------------------|----------------------------------|
| Innovators | I-01 | [specific current behavior] | [specific friction] |
| Early Adopters | I-02 | [specific current behavior] | [specific friction] |
| Early Majority | I-03 | [specific current behavior] | [specific friction] |
| Late Majority | I-04 | [specific current behavior] | [specific friction] |
| Laggards | I-05 | [specific current behavior] | [specific friction] |

---

SECTION C — Month-by-Month Adoption Timeline

Minimum 6 months. Rogers sequence enforced: Innovators before Early Adopters; Early Adopters before Early Majority; Early Majority before Late Majority; Late Majority before Laggards. No sequence inversions.

Spread mechanism in each row must be feature-specific or role-specific. Generic "word of mouth" alone does not satisfy the requirement — at least one transition must name a specific mechanism tied to this feature.

| Month | Active Archetype(s) | Roles Adopting | Spread Mechanism | Cumulative Coverage (%) |
|-------|--------------------|--------------|-----------------|-----------------------|
| Month 1 | [archetype(s)] | [roles] | [mechanism] | [%] |
| Month 2 | [archetype(s)] | [roles] | [mechanism] | [%] |
| Month 3 | [archetype(s)] | [roles] | [mechanism] | [%] |
| Month 4 | [archetype(s)] | [roles] | [mechanism] | [%] |
| Month 5 | [archetype(s)] | [roles] | [mechanism] | [%] |
| Month 6 | [archetype(s)] | [roles] | [mechanism] | [%] |

---

SECTION D — Chasm Analysis

The chasm is the adoption gap between Early Adopters and Early Majority. Produce three sub-tables.

Sub-table 1 — Archetype contrast:
| Property | Early Adopters | Early Majority |
|----------|---------------|---------------|
| Decision driver | [specific] | [specific] |
| Risk tolerance | [specific] | [specific] |
| Adoption trigger | [specific] | [specific] |

Sub-table 2 — Bridging mechanism (at least one entry; cite the EM Inertia ID from SECTION B that the bridge must overcome):
| Bridge Mechanism | EM Inertia ID Targeted | How It Overcomes the Inertia |
|-----------------|----------------------|------------------------------|
| [mechanism] | I-0X | [specific explanation] |

Sub-table 3 — Gap risks (at least one scenario where the chasm widens):
| Risk Scenario | Trigger | Consequence |
|--------------|---------|-------------|
| [scenario] | [trigger] | [consequence] |

---

SECTION E — Champion Network

At least 2 champion entries. Each entry must have BOTH archetype position rationale AND a named EM Inertia ID from SECTION B. An entry with only archetype rationale or only inertia reference fails C-14.

| Champion Role | Rogers Archetype | Archetype Bridge Rationale | EM Inertia ID Targeted | How Champion Overcomes That Inertia |
|--------------|-----------------|---------------------------|----------------------|-------------------------------------|
| [role] | [archetype] | [why their archetype position qualifies them to bridge] | I-0X | [specific mechanism] |
| [role] | [archetype] | [why their archetype position qualifies them to bridge] | I-0X | [specific mechanism] |

---

SECTION F — Churn Risk and Mitigation

At least 2 archetype entries. Churn trigger must reference the Named Inertia ID that the churn represents reversion to. Mitigation Action must name a concrete team action — not solely a surveillance verb. A mitigation reading only "monitor usage" or "track adoption" fails C-15.

| Archetype | Churn Trigger | Inertia Reversion ID | Warning Signal | Mitigation Action (concrete team action) |
|-----------|-------------|---------------------|---------------|------------------------------------------|
| [archetype] | [specific trigger] | I-0X | [observable signal] | [concrete action the team takes] |
| [archetype] | [specific trigger] | I-0X | [observable signal] | [concrete action the team takes] |

---

SECTION G — Interventions, Sensitivity, and Signal Readiness

Sub-table 1 — Interventions ranked by adoption delta (at least 3 entries, descending delta order):
Each intervention must cite at least one Named Inertia ID from SECTION B.

| Rank | Intervention | Named Inertia Targeted | Adoption Delta | Rationale |
|------|-------------|----------------------|---------------|-----------|
| 1 | [intervention] | I-0X | [H/M/L or %] | [rationale] |
| 2 | [intervention] | I-0X | [H/M/L or %] | [rationale] |
| 3 | [intervention] | I-0X | [H/M/L or %] | [rationale] |

Delta scale definition: H = >20% increase in monthly adoption rate; M = 10-20%; L = <10%.

Sub-table 2 — Chasm sensitivity analysis (2 scenarios):
| Scenario | Named Lever | Adoption Trajectory | Chasm Crossing Month |
|----------|------------|--------------------|--------------------|
| Optimistic | [lever from SECTIONS B-F] | [trajectory] | Month [N] |
| Pessimistic | [lever from SECTIONS B-F] | [trajectory] | Month [N] or Not Crossed |

Sub-table 3 — Signal readiness feedback loop (at least 2 measurable signals):
| Signal | Threshold | Interpretation |
|--------|-----------|----------------|
| [measurable signal] | [threshold, e.g., >=3 EM teams active] | [proceed / pause / intervene] |
| [measurable signal] | [threshold] | [interpretation] |

---

## VERIFICATION MODE

Content generation (Sections A–G) is complete. Sections H through K are the audit stage. Do not generate new content — verify and correct existing content only.

CORRECTION BLOCK format (produce this block immediately when a gate FAILS):

  CORRECTION BLOCK — [Criterion ID] — [Section reference, row identifier]
  BEFORE — [Section name, row]: [Reproduce the original content verbatim]
  AFTER — [Section name, row]: [Write the corrected content in full]
  Gate re-run: [Confirm the corrected entry satisfies the pass condition; quote the specific ID or datum that now satisfies it]

Corrected content lives in this CORRECTION BLOCK (C-19 location).
SECTION K will reference this location but will NOT duplicate the corrected content (C-21 rule).

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check each of the four downstream sections for explicit Named Inertia ID citations from SECTION B:
- SECTION D (chasm bridging): Does at least one Inertia ID appear directly? [ ]
- SECTION G Part 1 (interventions): Does at least one Inertia ID appear per intervention? [ ]
- SECTION E (champion network): Does each champion row cite an Inertia ID? [ ]
- SECTION F (churn): Does each churn trigger row cite an Inertia ID? [ ]

Count: [N] of 4 sections contain explicit Inertia ID citations.
Gate H result: [PASS if N >= 3 / FAIL if N < 3]

[If FAIL: produce CORRECTION BLOCK — C-13 immediately before proceeding to SECTION I.]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Review each row in SECTION E:
- Does the row state the archetype position reason? [ ]
- Does the row name a specific EM Inertia ID the champion targets? [ ]

A row with only one of the two anchors fails.
Gate I result: [PASS if all rows have both anchors / FAIL if any row is missing one]

[If FAIL: produce CORRECTION BLOCK — C-14 for each failing champion row immediately before proceeding to SECTION J.]

---

SECTION J — Gate: C-15 (Churn Mitigations Are Concrete Actions)

Review each Mitigation Action in SECTION F:
- Does the action name something the team does (assign, train, remove, bundle, pair, etc.)? [ ]
- Is the action solely a surveillance verb (monitor / track / watch / observe / measure)? [ ]

A mitigation consisting only of surveillance language fails. A mitigation with action + measurement passes.
Gate J result: [PASS if all rows have concrete actions / FAIL if any row is surveillance-only]

[If FAIL: produce CORRECTION BLOCK — C-15 for each failing mitigation row immediately before proceeding to SECTION K.]

---

## SECTION K — Terminal Gate State Record

This section records gate outcomes. It does NOT contain corrected content.
Corrected content appears in inline CORRECTION BLOCKS above (Sections H, I, J respectively).

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK
Location cited. An evaluator can verify this invariant by inspection without relying on this assertion.

| Criterion | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------|---------------|-------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone | [PASS / FAIL] | [Yes / No] | [Section H / N/A] | [PASS] |
| C-14 — Champion double-anchor | [PASS / FAIL] | [Yes / No] | [Section I / N/A] | [PASS] |
| C-15 — Churn action test | [PASS / FAIL] | [Yes / No] | [Section J / N/A] | [PASS] |

All three Final Results must show PASS before this artifact is committed.
```

---

## V-02 — Single-axis: Role Sequence (Archetype-First)

**Variation axis:** Role sequence — begin with the five Rogers archetype buckets and assign each of the 16 roles into a bucket before doing anything else. Downstream sections derive from the archetype groupings rather than from role-level analysis.

**Hypothesis:** Starting from archetype definitions and populating them with roles (rather than mapping roles upward) enforces Rogers ordering at the structural level and reduces the inversion risk for C-01/C-02; the model cannot place an Innovator role in the EM bucket because EM is defined first.

---

```
STRUCTURAL CONTRACT (read before generating any output):

Location rules:
- SECTIONS A through G: content generation. Section A defines the five archetype buckets first, then assigns all 16 roles to them.
- Inline CORRECTION BLOCKS appear immediately after the gate check that triggers them (Sections H, I, or J). This is the C-19 location. Corrected content lives here.
- SECTION K is the terminal gate state record. It records initial result, revision performed (yes/no), CORRECTION BLOCK location, and final result per gate. SECTION K does NOT contain corrected content — it references CORRECTION BLOCK locations only.
- The ## VERIFICATION MODE header appears between SECTION G and SECTION H. All content sections precede this marker; all audit sections follow it.

Self-verifying invariant (asserted in SECTION K):
  "For every 'Revision Performed: Yes' entry in SECTION K, a CORRECTION BLOCK
   containing BEFORE and AFTER content exists earlier in this document at the
   CORRECTION BLOCK Location column entry."

---

SECTION A — Archetype Buckets with Role Assignment

Define each Rogers archetype in one sentence for this feature. Then assign the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE) to the appropriate bucket.

Every role must appear in exactly one bucket. No role may be omitted.

INNOVATORS — [one-sentence definition for this feature]
Roles in this bucket: [list roles]
Why these roles qualify as innovators for this feature: [shared rationale]

EARLY ADOPTERS — [one-sentence definition for this feature]
Roles in this bucket: [list roles]
Why these roles qualify as early adopters for this feature: [shared rationale]

EARLY MAJORITY — [one-sentence definition for this feature]
Roles in this bucket: [list roles]
Why these roles qualify as early majority for this feature: [shared rationale]

LATE MAJORITY — [one-sentence definition for this feature]
Roles in this bucket: [list roles]
Why these roles qualify as late majority for this feature: [shared rationale]

LAGGARDS — [one-sentence definition for this feature]
Roles in this bucket: [list roles]
Why these roles qualify as laggards for this feature: [shared rationale]

Confirm all 16 roles accounted for: [list all 16 with their assigned archetype]

---

SECTION B — Named Inertia per Archetype

For each archetype bucket from SECTION A, name the specific status-quo behavior the roles in that bucket are currently doing instead of using this feature. Assign an Inertia ID (I-01 ...).

Generic labels ("resistance to change," "risk-averse") fail. Name the specific tool, process, or assumption.

At least 3 of the 5 archetypes must have a distinct entry.

| Archetype | Inertia ID | What They Do Today | Why This Delays Adoption |
|-----------|-----------|-------------------|--------------------------|
| Innovators | I-01 | [specific behavior] | [specific friction] |
| Early Adopters | I-02 | [specific behavior] | [specific friction] |
| Early Majority | I-03 | [specific behavior] | [specific friction] |
| Late Majority | I-04 | [specific behavior] | [specific friction] |
| Laggards | I-05 | [specific behavior] | [specific friction] |

---

SECTION C — Month-by-Month Adoption Timeline

Derive the timeline directly from the archetype bucket order established in SECTION A. The sequence
Innovators → Early Adopters → Early Majority → Late Majority → Laggards is locked by the bucket
definitions. No inversion is possible.

Minimum 6 months. At least one transition must name a feature-specific spread mechanism.

| Month | Active Archetype(s) | Roles Adopting (from bucket) | Spread Mechanism | Cumulative Coverage (%) |
|-------|--------------------|-----------------------------|-----------------|------------------------|
| Month 1 | Innovators | [roles from Innovator bucket] | [mechanism] | [%] |
| Month 2 | Innovators + Early Adopters | [roles] | [mechanism] | [%] |
| Month 3 | Early Adopters | [roles] | [mechanism] | [%] |
| Month 4 | Early Majority (begins) | [roles] | [mechanism] | [%] |
| Month 5 | Early Majority | [roles] | [mechanism] | [%] |
| Month 6+ | Late Majority / Laggards | [roles] | [mechanism] | [%] |

---

SECTION D — Chasm Analysis

The chasm lies between the Early Adopters bucket and the Early Majority bucket (from SECTION A).

1. Bucket contrast: State the one key difference between what the EA bucket values and what the
   EM bucket requires before they adopt. Cite the EM Inertia ID (from SECTION B) that defines
   what the EM bucket is protecting.

2. Bridging mechanism: At least one concrete mechanism that uses the EA bucket's characteristics
   to reach the EM bucket. Name the specific EM Inertia ID being overcome.

3. Gap risk: At least one scenario where the EA-to-EM bridge fails.

---

SECTION E — Champion Network

At least 2 champions. Each champion must satisfy both anchors:
(a) Why their Rogers archetype position (from their SECTION A bucket) qualifies them to bridge
(b) Which specific EM Inertia ID (from SECTION B) they are positioned to overcome

An entry with only (a) or only (b) fails C-14.

| Champion Role | Archetype Bucket | Archetype Bridge Rationale (a) | EM Inertia ID (b) | How This Champion Overcomes That Inertia |
|--------------|-----------------|-------------------------------|------------------|------------------------------------------|
| [role] | [bucket] | [rationale] | I-0X | [mechanism] |
| [role] | [bucket] | [rationale] | I-0X | [mechanism] |

---

SECTION F — Churn Risk and Mitigation

At least 2 entries. Each churn trigger represents reversion to the archetype's named inertia (SECTION B).
Mitigation must name a concrete team action. Surveillance-only mitigations (monitor / track / observe) fail.

| Archetype Bucket | Churn Trigger | Inertia Reversion (ID) | Warning Signal | Mitigation Action |
|-----------------|-------------|----------------------|---------------|-------------------|
| [archetype] | [trigger] | I-0X | [signal] | [concrete action] |
| [archetype] | [trigger] | I-0X | [signal] | [concrete action] |

---

SECTION G — Interventions, Sensitivity, and Signal Readiness

Part 1 — Ranked interventions (minimum 3, descending adoption delta):
| Rank | Intervention | Inertia Targeted (ID) | Adoption Delta | Rationale |
|------|-------------|----------------------|----------------|-----------|
| 1 | [intervention] | I-0X | [H/M/L] | [rationale] |
| 2 | [intervention] | I-0X | [H/M/L] | [rationale] |
| 3 | [intervention] | I-0X | [H/M/L] | [rationale] |

Delta scale: H = >20% monthly adoption rate increase; M = 10-20%; L = <10%.

Part 2 — Sensitivity analysis:
| Scenario | Lever (from SECTIONS B-F) | EA-to-EM Bridge | Chasm Crossing Month |
|----------|--------------------------|-----------------|---------------------|
| Optimistic | [lever] | [how bridge strengthens] | Month [N] |
| Pessimistic | [lever] | [how bridge weakens] | Month [N] or Not Crossed |

Part 3 — Signal readiness (at least 2 measurable signals):
| Signal | Threshold | Proceed / Pause / Intervene |
|--------|-----------|----------------------------|
| [signal] | [threshold] | [interpretation] |
| [signal] | [threshold] | [interpretation] |

---

## VERIFICATION MODE

Content generation (Sections A–G) is complete. Sections H through K are the audit stage.
Do not generate new domain content. Verify and correct existing content only.

CORRECTION BLOCK format (produce when a gate FAILS):

  CORRECTION BLOCK — [Criterion ID] — [Section reference, row identifier]
  BEFORE — [Section, row]: [Original content verbatim]
  AFTER — [Section, row]: [Corrected content in full]
  Gate re-run: [Confirm pass condition now satisfied]

Corrected content lives in this CORRECTION BLOCK.
SECTION K references this location but does NOT duplicate corrected content.

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)
Check: Are Inertia IDs from SECTION B explicitly cited in >= 3 of {SECTION D, SECTION G Part 1, SECTION E, SECTION F}?
Tally: [N] of 4 sections cite explicit Inertia IDs.
Gate H: [PASS / FAIL]
[If FAIL: produce CORRECTION BLOCK — C-13 before proceeding to SECTION I.]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)
Check: Does every champion row in SECTION E have both archetype position rationale AND a named EM Inertia ID?
Gate I: [PASS if all rows have both / FAIL if any row is missing one anchor]
[If FAIL: produce CORRECTION BLOCK — C-14 for each failing row before proceeding to SECTION J.]

---

SECTION J — Gate: C-15 (Churn Mitigations Are Concrete Actions)
Check: Does every Mitigation Action in SECTION F include a concrete team action (not solely surveillance)?
Gate J: [PASS / FAIL]
[If FAIL: produce CORRECTION BLOCK — C-15 for each failing row before proceeding to SECTION K.]

---

## SECTION K — Terminal Gate State Record

This section records gate outcomes only. It does NOT contain corrected content.
Corrected content appears in CORRECTION BLOCKS in Sections H, I, and J above.

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the stated location.
This invariant is evaluable: an evaluator reading this table can verify every Yes-row against
the document and find a CORRECTION BLOCK at the cited location.

| Criterion | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------|---------------|-------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone | [PASS / FAIL] | [Yes / No] | [Section H / N/A] | [PASS] |
| C-14 — Champion double-anchor | [PASS / FAIL] | [Yes / No] | [Section I / N/A] | [PASS] |
| C-15 — Churn action test | [PASS / FAIL] | [Yes / No] | [Section J / N/A] | [PASS] |

All three Final Results must show PASS before this artifact is committed.
```

---

## V-03 — Single-axis: Inertia Framing (Status-Quo Competitor Named Throughout)

**Variation axis:** Inertia framing — a named Status-Quo Competitor is declared at the outset and referenced explicitly in every subsequent section as the specific obstacle adoption must displace.

**Hypothesis:** Naming the status-quo as a competitor rather than a property of each archetype produces more feature-specific inertia entries (C-11) and sharper interventions (C-04), at the cost of a lighter verification structure that creates C-21/C-22 risk.

**Expected C-21/C-22/C-23 behavior:** At-risk. No top-of-prompt structural contract; no explicit negative rule on the terminal section; the terminal section ("Audit Outcomes") does not include a named self-verifying invariant. The verification stage opens with a labeled section header ("## Verification Stage") but lacks explicit mode-shift instruction, and the correction format is embedded in prose guidance rather than a named structural block. These properties replicate R6 V-03's failure mode and extend it to the three new criteria.

---

```
You are simulating adoption of this feature by a software team. Before starting, name the
Status-Quo Competitor: the specific tool, process, or behavior that each archetype is currently
using instead of this feature. The Status-Quo Competitor is the adoption opponent — every section
of this analysis must reference how the competitor creates or reduces friction.

Stock roles (16): PM, UX, C-01 through C-12, Support, SRE.
Rogers archetypes (5): Innovators, Early Adopters, Early Majority, Late Majority, Laggards.

---

Step 1 — Name the Status-Quo Competitor

State in one sentence what teams are doing today instead of using this feature.
Name: [Status-Quo Competitor name]
What it does: [one-sentence description]
Why it is sticky: [one specific reason teams won't replace it easily]

This competitor name will appear in every subsequent step.

---

Step 2 — Role-to-Archetype Mapping with Competitor Relationship

Map all 16 stock roles to Rogers archetypes. For each role, state how their relationship to the
Status-Quo Competitor determines their archetype position.

| Role | Rogers Archetype | Relationship to Status-Quo Competitor |
|------|-----------------|--------------------------------------|
| PM | [archetype] | [how competitor dependency shapes their position] |
| UX | [archetype] | [how competitor dependency shapes their position] |
| C-01 | [archetype] | [how competitor dependency shapes their position] |
| C-02 | [archetype] | [how competitor dependency shapes their position] |
| C-03 | [archetype] | [how competitor dependency shapes their position] |
| C-04 | [archetype] | [how competitor dependency shapes their position] |
| C-05 | [archetype] | [how competitor dependency shapes their position] |
| C-06 | [archetype] | [how competitor dependency shapes their position] |
| C-07 | [archetype] | [how competitor dependency shapes their position] |
| C-08 | [archetype] | [how competitor dependency shapes their position] |
| C-09 | [archetype] | [how competitor dependency shapes their position] |
| C-10 | [archetype] | [how competitor dependency shapes their position] |
| C-11 | [archetype] | [how competitor dependency shapes their position] |
| C-12 | [archetype] | [how competitor dependency shapes their position] |
| Support | [archetype] | [how competitor dependency shapes their position] |
| SRE | [archetype] | [how competitor dependency shapes their position] |

---

Step 3 — Named Inertia per Archetype (Competitor-Specific)

For each archetype, name the specific Status-Quo Competitor behavior that must be displaced.
Assign each entry an Inertia ID (I-01 ...). At least 3 archetypes must have distinct entries.

| Archetype | Inertia ID | Specific Competitor Behavior | Why This Feature Can't Replace It Easily |
|-----------|-----------|------------------------------|------------------------------------------|
| Innovators | I-01 | [specific competitor behavior] | [specific displacement challenge] |
| Early Adopters | I-02 | [specific competitor behavior] | [specific displacement challenge] |
| Early Majority | I-03 | [specific competitor behavior] | [specific displacement challenge] |
| Late Majority | I-04 | [specific competitor behavior] | [specific displacement challenge] |
| Laggards | I-05 | [specific competitor behavior] | [specific displacement challenge] |

---

Step 4 — Month-by-Month Adoption Timeline

Show adoption month by month (at least 6 months). For each month, name which archetype group is
adopting and what reduced their dependence on the Status-Quo Competitor enough to switch.
Rogers sequence holds: Innovators before Early Adopters; Early Adopters before Early Majority, etc.

| Month | Archetype(s) Active | Roles | Competitor Displacement Event | Cumulative Coverage (%) |
|-------|--------------------|----|------------------------------|------------------------|
| Month 1 | [archetype] | [roles] | [what weakened competitor hold] | [%] |
| Month 2 | [archetype] | [roles] | [what weakened competitor hold] | [%] |
| Month 3 | [archetype] | [roles] | [what weakened competitor hold] | [%] |
| Month 4 | [archetype] | [roles] | [what weakened competitor hold] | [%] |
| Month 5 | [archetype] | [roles] | [what weakened competitor hold] | [%] |
| Month 6 | [archetype] | [roles] | [what weakened competitor hold] | [%] |

---

Step 5 — Chasm Analysis

The chasm is the gap between Early Adopters and Early Majority. Name the specific way the
Status-Quo Competitor is stronger for the Early Majority than for Early Adopters — this is why
the chasm exists for this feature in particular.

State:
1. What makes the Status-Quo Competitor stickier for EM than for EA (cite I-0X from Step 3)
2. The bridging mechanism: a concrete way to weaken the competitor's hold on EM
3. A gap risk: a scenario where the competitor's stickiness prevents bridge completion

---

Step 6 — Champion Network

Name at least 2 champion roles. Each champion must:
(a) Have an archetype position that gives them credibility with Early Majority
(b) Be positioned to directly challenge the EM's Named Inertia entry (cite I-0X from Step 3)

| Champion Role | Archetype | Why Their Position Gives EM Credibility | EM Inertia They Target (ID) | How They Challenge That Inertia |
|--------------|-----------|----------------------------------------|---------------------------|--------------------------------|
| [role] | [archetype] | [rationale] | I-0X | [mechanism] |
| [role] | [archetype] | [rationale] | I-0X | [mechanism] |

---

Step 7 — Churn Risks and Mitigations

For at least 2 archetypes, name the churn trigger (when reversion to the Status-Quo Competitor
becomes attractive) and the team action that prevents it. Mitigations must name what the team does —
not solely what the team watches. Include the Inertia ID that the churn represents reversion to.

| Archetype | Churn Trigger | Inertia Reversion (ID) | Warning Signal | Team Mitigation Action |
|-----------|-------------|----------------------|---------------|------------------------|
| [archetype] | [trigger] | I-0X | [signal] | [team action] |
| [archetype] | [trigger] | I-0X | [signal] | [team action] |

---

Step 8 — Interventions, Sensitivity, and Signal Readiness

Ranked interventions (at least 3, descending delta, each citing a Named Inertia ID):
| Rank | Intervention | Inertia Targeted | Adoption Delta | Rationale |
|------|-------------|-----------------|---------------|-----------|
| 1 | [intervention] | I-0X | [H/M/L or %] | [rationale] |
| 2 | [intervention] | I-0X | [H/M/L or %] | [rationale] |
| 3 | [intervention] | I-0X | [H/M/L or %] | [rationale] |

Sensitivity analysis (2 scenarios tied to competitor stickiness lever):
Optimistic: [how competitor hold weakens faster; chasm crossing month]
Pessimistic: [how competitor hold persists longer; chasm crossing delayed or blocked]

Signal readiness (at least 2 measurable signals indicating competitor displacement is sufficient):
Signal 1: [signal] — threshold: [threshold] — interpretation: [proceed/pause/intervene]
Signal 2: [signal] — threshold: [threshold] — interpretation: [proceed/pause/intervene]

---

## Verification Stage

Review your output for Steps 2 through 8 against the three aspirational criteria below.
For each criterion, state whether the pass condition is met. If not, show the original content
and the corrected content before continuing.

Check 1 — C-13: Named Inertia as Downstream Backbone
Pass condition: Inertia IDs from Step 3 are explicitly cited in at least 3 of {Step 5, Step 8
interventions, Step 6, Step 7}.
Result: [PASS / FAIL]
If FAIL, show the correction:
  Criterion: C-13
  Step and location: [step name, row or paragraph]
  Original: [reproduce the original text]
  Corrected: [write the corrected text]

Check 2 — C-14: Champion Rationale Double-Anchored
Pass condition: Every champion row in Step 6 has both (a) archetype position rationale and
(b) a named EM Inertia ID.
Result: [PASS / FAIL]
If FAIL, show the correction:
  Criterion: C-14
  Champion row: [role name]
  Original: [reproduce the original row]
  Corrected: [write the corrected row]

Check 3 — C-15: Churn Mitigations Are Concrete Actions
Pass condition: Every Team Mitigation Action in Step 7 names a concrete team action (not solely
a surveillance verb).
Result: [PASS / FAIL]
If FAIL, show the correction:
  Criterion: C-15
  Archetype row: [archetype]
  Original: [reproduce the original mitigation]
  Corrected: [write the corrected mitigation]

---

Audit Outcomes

| Criterion | Initial Result | Revision Performed | Final Result |
|-----------|---------------|-------------------|-------------|
| C-13 — Inertia downstream backbone | [PASS / FAIL] | [Yes / No] | [PASS] |
| C-14 — Champion double-anchor | [PASS / FAIL] | [Yes / No] | [PASS] |
| C-15 — Churn action test | [PASS / FAIL] | [Yes / No] | [PASS] |

All three Final Results must show PASS.
```

**Design note for evaluators (C-21/C-22/C-23 analysis):**

- **C-21 risk:** "Audit Outcomes" table has no explicit rule against containing corrected content. A model that fails a check and writes the corrected row directly into the Audit Outcomes table would co-locate corrected content with gate state, failing C-21. The prose correction format ("show the original and corrected content") does not name a distinct structural block, so the model may fold correction content into the Outcomes table.
- **C-22 risk:** The Audit Outcomes table has no self-verifying invariant. It records initial/revision/final columns but makes no verifiable claim about the rest of the document. An evaluator reading only the Outcomes table cannot confirm whether the correction content exists elsewhere without trusting the model's report.
- **C-23 risk:** "## Verification Stage" is a named section header and likely satisfies C-23's label requirement. However, the header lacks explicit mode-shift instruction — a model may not recognize it as a mode boundary and may continue generating domain content after it. Lower confidence than V-01/V-02/V-04/V-05.

---

## V-04 — Combined: Lifecycle Phase Boundaries + Tables + Explicit Structural Contract

**Variation axes:** Output format (phase-bounded tables) + Lifecycle emphasis (PHASE 1 through PHASE 6 structural headers).

**Hypothesis:** Explicit phase headers lock Rogers ordering at the structural level (a model cannot write a Late Majority row before completing the Early Majority phase), combined tables provide scannable coverage, and the most explicit structural contract (naming C-21/C-22/C-23 by criterion ID) produces the strongest enforcement of the three new criteria.

---

```
STRUCTURAL CONTRACT (read before generating any content):

Location rules (C-19 / C-20 / C-21 separation):
- C-19 location: Inline CORRECTION BLOCKs, placed immediately after the gate check that triggers
  them (Sections H, I, or J). Corrected content lives exclusively here.
- C-20 location: SECTION K, the terminal gate state record. SECTION K records initial result,
  revision performed (yes/no), CORRECTION BLOCK location (section reference), and final result
  per gate criterion.
- C-21 rule: SECTION K does NOT contain corrected content. SECTION K references CORRECTION BLOCK
  locations only. An evaluator reading SECTION K reads gate state, not corrected rows.

Verification boundary (C-23):
- The ## VERIFICATION MODE header is a named boundary between content generation (Phases 1-6)
  and the audit stage (Sections H through K). It signals an explicit mode shift. All domain
  content appears before this header. No domain content appears after it.

Self-verifying invariant (C-22, asserted in SECTION K):
- "For every 'Revision Performed: Yes' entry in SECTION K, a CORRECTION BLOCK containing
  BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK Location
  cited." This claim is verifiable by inspection. A 'Yes' row with no matching CORRECTION
  BLOCK at the stated location falsifies this invariant.

Correction block format (used when any gate in H/I/J FAILS):
  CORRECTION BLOCK — [Criterion ID] — [Phase, table, row identifier]
  BEFORE — [Phase, row]: [Original content verbatim]
  AFTER — [Phase, row]: [Corrected content in full]
  Gate re-run: [State the specific ID or datum that now satisfies the pass condition]

---

SECTION A — Named Inertia Registry

Before adopting the phase structure, establish the inertia registry that all phases will cite.
Assign an Inertia ID (I-01 ...) to each archetype's status-quo friction.
Generic labels ("resistance to change") fail — name the specific behavior, tool, or assumption.
At least 3 archetypes must have distinct entries.

| Archetype | Inertia ID | Specific Status-Quo Behavior | Displacement Challenge |
|-----------|-----------|------------------------------|------------------------|
| Innovators | I-01 | [behavior] | [challenge] |
| Early Adopters | I-02 | [behavior] | [challenge] |
| Early Majority | I-03 | [behavior] | [challenge] |
| Late Majority | I-04 | [behavior] | [challenge] |
| Laggards | I-05 | [behavior] | [challenge] |

---

PHASE 1 — INNOVATORS

Stock roles in this phase: [list roles mapped here from PM, UX, C-01 through C-12, Support, SRE]
Adoption month(s): Month [N]

| Role | Rogers Archetype | Archetype Rationale | Inertia to Overcome (ID) |
|------|-----------------|--------------------|-----------------------------|
| [role] | Innovators | [rationale] | I-0X |

Spread mechanism into PHASE 2: [specific feature-specific or role-specific mechanism]

---

PHASE 2 — EARLY ADOPTERS

Stock roles in this phase: [list roles]
Adoption month(s): Month [N] – Month [N]

| Role | Rogers Archetype | Archetype Rationale | Inertia to Overcome (ID) |
|------|-----------------|--------------------|-----------------------------|
| [role] | Early Adopters | [rationale] | I-0X |

Spread mechanism into PHASE 3: [mechanism]

---

PHASE 3 — CHASM

This phase is not an adoption phase. It is the gap that separates PHASE 2 from PHASE 4.
Duration estimate: Month [N] – Month [N]

Chasm definition:
| Property | Early Adopters (PHASE 2) | Early Majority (PHASE 4) |
|----------|------------------------|--------------------------|
| Decision driver | [specific] | [specific] |
| Risk tolerance | [specific] | [specific] |
| Inertia protecting them | I-0X [name] | I-0X [name] |

Bridging mechanism (cite EM Inertia ID):
The bridge must overcome [I-0X] specifically because [explain].
Mechanism: [concrete bridge tied to this feature]

Gap risk:
| Risk | Trigger | Consequence |
|------|---------|-------------|
| [risk] | [trigger] | [consequence] |

---

PHASE 4 — EARLY MAJORITY

Stock roles in this phase: [list roles]
Adoption month(s): Month [N] – Month [N]

| Role | Rogers Archetype | Archetype Rationale | Inertia to Overcome (ID) |
|------|-----------------|--------------------|-----------------------------|
| [role] | Early Majority | [rationale] | I-0X |

Spread mechanism into PHASE 5: [mechanism]

---

PHASE 5 — LATE MAJORITY

Stock roles in this phase: [list roles]
Adoption month(s): Month [N] – Month [N]

| Role | Rogers Archetype | Archetype Rationale | Inertia to Overcome (ID) |
|------|-----------------|--------------------|-----------------------------|
| [role] | Late Majority | [rationale] | I-0X |

Spread mechanism into PHASE 6: [mechanism]

---

PHASE 6 — LAGGARDS

Stock roles in this phase: [list roles]
Adoption month(s): Month [N]+

| Role | Rogers Archetype | Archetype Rationale | Inertia to Overcome (ID) |
|------|-----------------|--------------------|-----------------------------|
| [role] | Laggards | [rationale] | I-0X |

---

SECTION B — Consolidated Role-to-Archetype Map (derived from PHASES 1-6)

Confirm all 16 roles are assigned. Aggregate the phase tables into a single reference.

| Role | Phase | Rogers Archetype | Adoption Month |
|------|-------|-----------------|----------------|
| PM | [phase] | [archetype] | Month [N] |
| UX | [phase] | [archetype] | Month [N] |
| C-01 through C-12 | [phase] | [archetype] | Month [N] |
| Support | [phase] | [archetype] | Month [N] |
| SRE | [phase] | [archetype] | Month [N] |

---

SECTION C — Champion Network

At least 2 champions. Double-anchor required: (a) archetype position rationale AND
(b) specific EM Inertia ID the champion targets (from SECTION A).

| Champion Role | Archetype Phase | (a) Bridge Rationale | (b) EM Inertia ID | How Champion Overcomes That Inertia |
|--------------|----------------|---------------------|------------------|--------------------------------------|
| [role] | PHASE [N] | [rationale] | I-0X | [mechanism] |
| [role] | PHASE [N] | [rationale] | I-0X | [mechanism] |

---

SECTION D — Churn Risk and Mitigation

At least 2 entries. Cite the Inertia ID that churn represents reversion to.
Mitigation must name a concrete team action. Surveillance-only fails.

| Archetype | Churn Trigger | Inertia Reversion (ID) | Warning Signal | Mitigation Action |
|-----------|-------------|----------------------|---------------|-------------------|
| [archetype] | [trigger] | I-0X | [signal] | [concrete action] |
| [archetype] | [trigger] | I-0X | [signal] | [concrete action] |

---

SECTION E — Interventions, Sensitivity, and Signal Readiness

Part 1 — Ranked interventions (minimum 3, descending delta, each citing an Inertia ID):
| Rank | Intervention | Inertia Targeted | Adoption Delta | Rationale |
|------|-------------|-----------------|---------------|-----------|
| 1 | [intervention] | I-0X | [H/M/L or %] | [rationale] |
| 2 | [intervention] | I-0X | [H/M/L or %] | [rationale] |
| 3 | [intervention] | I-0X | [H/M/L or %] | [rationale] |

Delta scale: H = >20%; M = 10-20%; L = <10%.

Part 2 — Sensitivity analysis:
| Scenario | Named Lever | Bridge Outcome | PHASE 4 Start Month |
|----------|------------|---------------|-------------------|
| Optimistic | [lever] | [how bridge strengthens] | Month [N] |
| Pessimistic | [lever] | [how bridge weakens] | Month [N] or Blocked |

Part 3 — Signal readiness (at least 2):
| Signal | Threshold | Interpretation |
|--------|-----------|----------------|
| [signal] | [threshold] | [proceed/pause/intervene] |
| [signal] | [threshold] | [proceed/pause/intervene] |

---

## VERIFICATION MODE

Content generation (Phases 1-6, Sections A-E) is complete.
This header marks the boundary between content generation and the audit stage.
Sections H through K are audit-only. Do not generate new domain content after this point.

CORRECTION BLOCK format (produce immediately when a gate FAILS):
  CORRECTION BLOCK — [Criterion ID] — [Section or Phase, row identifier]
  BEFORE — [location]: [Original content verbatim]
  AFTER — [location]: [Corrected content in full]
  Gate re-run: [Confirm pass condition satisfied, cite specific ID or datum]

Per structural contract: SECTION K does NOT contain corrected content.

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check: Inertia IDs from SECTION A explicitly cited in >= 3 of {PHASE 3 chasm (C-03), SECTION E
interventions (C-04), SECTION C champions (C-05), SECTION D churn (C-06)}.

Tally:
- PHASE 3 chasm: cites Inertia IDs? [ ]
- SECTION E interventions: each entry cites Inertia ID? [ ]
- SECTION C champions: each entry cites Inertia ID? [ ]
- SECTION D churn: each entry cites Inertia ID? [ ]

Count: [N] of 4 sections.
Gate H: [PASS if N >= 3 / FAIL if N < 3]
[If FAIL: CORRECTION BLOCK — C-13 immediately here.]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Check: Every champion row in SECTION C has both (a) archetype bridge rationale AND (b) EM Inertia ID.
Review each row. A row missing either anchor fails.
Gate I: [PASS / FAIL]
[If FAIL: CORRECTION BLOCK — C-14 for each failing row immediately here.]

---

SECTION J — Gate: C-15 (Churn Mitigations Are Concrete Actions)

Check: Every Mitigation Action in SECTION D names a concrete team action.
A mitigation consisting only of "monitor," "track," "watch," "observe," or "measure" fails.
A mitigation that includes an action verb plus measurement passes.
Gate J: [PASS / FAIL]
[If FAIL: CORRECTION BLOCK — C-15 for each failing row immediately here.]

---

## SECTION K — Terminal Gate State Record

This section records gate outcomes only. It does NOT contain corrected content (C-21 rule).
Corrected content appears in CORRECTION BLOCKS in Sections H, I, and J above.

Self-verifying invariant (C-22): For every "Revision Performed: Yes" entry in this table,
a CORRECTION BLOCK containing BEFORE and AFTER content exists earlier in this document
at the CORRECTION BLOCK Location cited. This claim is verifiable by inspection — an evaluator
can confirm or refute it without relying on this assertion. Failure mode: a "Yes" row whose
CORRECTION BLOCK Location points to a section that contains no CORRECTION BLOCK, or whose
CORRECTION BLOCK contains no BEFORE field, falsifies this invariant.

| Criterion | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------|---------------|-------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone | [PASS / FAIL] | [Yes / No] | [Section H / N/A] | [PASS] |
| C-14 — Champion double-anchor | [PASS / FAIL] | [Yes / No] | [Section I / N/A] | [PASS] |
| C-15 — Churn action test | [PASS / FAIL] | [Yes / No] | [Section J / N/A] | [PASS] |

All three Final Results must show PASS before this artifact is committed.
```

---

## V-05 — Combined: Conversational Register + VERIFICATION MODE + Inertia Framing

**Variation axes:** Phrasing register (conversational A-G, formal H-K) + Inertia framing (Status-Quo Competitor named throughout) + VERIFICATION MODE boundary (explicit mode-shift header with instruction).

**Hypothesis:** Conversational register in content sections produces richer Named Inertia entries (C-11) and more nuanced champion rationale (C-14) by allowing analytical narrative; the explicit VERIFICATION MODE boundary with mode-shift instruction preserves C-19/C-21/C-22/C-23 enforcement without requiring formal section labels in the content phase. The status-quo competitor framing from V-03 is carried over but surrounded by the full structural contract to avoid V-03's expected failure modes.

---

```
STRUCTURAL CONTRACT (read before generating any output):

Location rules:
- Sections A through G use conversational second-person register. You are reasoning through
  adoption dynamics, not filling in a form. Prose, tables, and mixed format are all acceptable.
- The Status-Quo Competitor (named in Section A) must be referenced in every subsequent section
  by name — not just implied.
- C-19 location: Inline CORRECTION BLOCKs, placed immediately after the gate check that
  triggers them (Sections H, I, or J). Corrected content lives exclusively here.
- C-20 location: SECTION K, the terminal gate state record. Records initial result, revision
  performed, CORRECTION BLOCK location, and final result per gate.
- C-21 rule: SECTION K does NOT contain corrected content. SECTION K references CORRECTION
  BLOCK locations only.

Verification boundary (C-23):
- The ## VERIFICATION MODE header marks the explicit transition from content generation to the
  audit stage. It is not a horizontal rule or blank line — it is a named mode shift.
  After this header, you are auditing, not generating. Domain analysis ends at this boundary.

Self-verifying invariant (asserted in SECTION K):
  "For every 'Revision Performed: Yes' entry in SECTION K, a CORRECTION BLOCK containing
   BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK Location
   cited."

Correction block format (used when any gate FAILS):
  CORRECTION BLOCK — [Criterion ID] — [Section and element identifier]
  BEFORE — [Section, element]: [Original content verbatim]
  AFTER — [Section, element]: [Corrected content in full]
  Gate re-run: [Confirm pass condition satisfied; cite the specific ID or datum]

---

SECTION A — Status-Quo Competitor and Archetype Overview

Start by naming the Status-Quo Competitor: the specific thing teams are doing today instead of
this feature. Give it a short name you will use in every subsequent section.

Then walk through the five Rogers archetypes as they apply to this feature. For each archetype,
explain — conversationally — which of the 16 stock roles (PM, UX, C-01 through C-12, Support,
SRE) belong there and why their relationship to the Status-Quo Competitor places them in that
bucket. Every role must appear in exactly one archetype. Cover all 16.

After your archetype walk-through, produce a compact reference table:
| Role | Rogers Archetype | Competitor Dependency (brief) |
|------|-----------------|-------------------------------|
| [all 16 roles] | | |

---

SECTION B — Named Inertia per Archetype

For each of the five archetypes, describe — in a sentence or two — the specific Status-Quo
Competitor behavior that makes adoption non-trivial for that group. This is not generic
"resistance to change" — it is the concrete thing the competitor does for them today.

Assign each entry an Inertia ID (I-01 ...) for downstream citation. At least 3 archetypes
must have entries that are genuinely distinct (not paraphrases of each other).

You might write something like:
  "I-03 (Early Majority): The [Competitor] automatically generates the weekly handoff report
   that half the C-01 through C-06 roles currently paste into Jira. This feature would need
   to match that output format exactly before EM roles will consider switching."

---

SECTION C — Month-by-Month Adoption Timeline

Walk through the adoption timeline month by month for at least 6 months. Describe who adopts
in each period, what weakened their dependency on the Status-Quo Competitor enough to try
the feature, and how that story connects to the next group.

After your narrative, produce a summary table:
| Month | Archetype(s) Active | Roles Adopting | Competitor Displacement Event | Cumulative Coverage (%) |
|-------|--------------------|----|------------------------------|------------------------|
| [rows] | | | | |

Constraint: Rogers sequence must hold in the table. Innovators precede Early Adopters; Early
Adopters precede Early Majority; Early Majority precedes Late Majority; Late Majority precedes
Laggards. The narrative should explain why this sequence emerges naturally from competitor
dependency levels.

---

SECTION D — Chasm Analysis

Explain the chasm in plain terms: what specifically makes the Status-Quo Competitor stickier for
the Early Majority than for the Early Adopters, and what that means for the crossing strategy.

Your analysis should cover:
1. Why the chasm exists for this feature (reference the EM Named Inertia ID from SECTION B)
2. The bridging mechanism: a concrete approach that uses Early Adopters' success to weaken
   the competitor's hold on Early Majority
3. A gap risk: a plausible scenario where the competitor's stickiness prevents the bridge

You may use a mix of prose and a contrast table for the archetype properties. At minimum,
use the word "chasm" once and cite at least one Named Inertia ID.

---

SECTION E — Champion Network

Identify the champion network: the roles who bridge from Early Adopters into Early Majority.
Name at least 2 champions. For each, explain in 2-3 sentences why they are positioned to
bridge — covering both their archetype position (why EM teams will listen to them) and the
specific EM Named Inertia (from SECTION B) they are positioned to overcome.

A champion rationale that names only the archetype position without identifying which competitor
behavior they help EM teams leave behind is incomplete. Similarly, a rationale that names the
inertia without explaining why the champion's position matters fails.

Summarize in a table:
| Champion Role | Archetype | Archetype Bridge Rationale | EM Inertia Targeted (ID) |
|--------------|-----------|---------------------------|--------------------------|
| [role] | [archetype] | [why position qualifies them] | I-0X |

---

SECTION F — Churn Risk and Mitigation

For at least 2 archetypes, describe what would pull them back to the Status-Quo Competitor
after initial adoption. Name the specific reversion event, the Inertia ID it represents
returning to, what the team should watch for, and what the team should DO.

The "what the team should do" is a concrete action — assigning a champion, running a targeted
training session, removing a switching cost, integrating with an existing workflow, etc.
"Monitor adoption metrics" is not a mitigation — it is surveillance. If you find yourself
writing a monitoring action, add the concrete intervention that follows when the signal fires.

Summarize in a table:
| Archetype | Churn Trigger | Inertia Reversion (ID) | Warning Signal | Team Mitigation Action |
|-----------|-------------|----------------------|---------------|------------------------|
| [archetype] | [trigger] | I-0X | [signal] | [concrete action] |

---

SECTION G — Interventions, Sensitivity, and Signal Readiness

Walk through the highest-leverage interventions for crossing the chasm and sustaining adoption.
For each intervention, name the Inertia ID it targets, estimate the adoption delta (H/M/L or %),
and explain why. Present them in descending delta order.

Then model two scenarios for chasm crossing: one optimistic (a named lever from your analysis
accelerates competitor displacement) and one pessimistic (a named lever fails or takes longer).
Name the lever in each scenario and state the chasm crossing month.

Close with at least 2 measurable adoption signals that would tell the team whether the competitor
is being displaced at the expected rate. Make the thresholds concrete enough to track.

Summarize in tables:
Part 1 — Interventions:
| Rank | Intervention | Inertia Targeted (ID) | Adoption Delta | Rationale |
|------|-------------|----------------------|---------------|-----------|
| [rows] | | | | |

Part 2 — Sensitivity:
| Scenario | Lever | Competitor Displacement Rate | Chasm Crossing |
|----------|-------|------------------------------|----------------|
| Optimistic | [lever] | [faster/slower] | Month [N] |
| Pessimistic | [lever] | [faster/slower] | Month [N] or Blocked |

Part 3 — Signal readiness:
| Signal | Threshold | Interpretation |
|--------|-----------|----------------|
| [signal] | [threshold] | [proceed/pause/intervene] |

---

## VERIFICATION MODE

You have finished generating content (Sections A–G). This header marks the mode boundary.
From this point forward, you are auditing, not creating. Do not introduce new domain analysis,
new inertia entries, or new champion rationale after this point.

Your task in Sections H, I, and J is to run each gate check against the content you generated
above. If a gate fails, produce a CORRECTION BLOCK immediately after the gate check result.
Then proceed to SECTION K.

CORRECTION BLOCK format:
  CORRECTION BLOCK — [Criterion ID] — [Section and element]
  BEFORE — [Section, element]: [Original content verbatim]
  AFTER — [Section, element]: [Corrected content in full]
  Gate re-run: [Confirm pass condition satisfied; cite the specific ID or datum]

Per structural contract: SECTION K does NOT contain corrected content.
Corrected content lives in CORRECTION BLOCKS here in Sections H, I, J.

---

SECTION H — Gate: C-13 (Named Inertia as Downstream Backbone)

Check whether Inertia IDs from SECTION B appear explicitly (not paraphrased) in at least 3 of
these 4 downstream sections: SECTION D (chasm), SECTION G Part 1 (interventions), SECTION E
(champions), SECTION F (churn).

Go through each section and mark whether an explicit Inertia ID citation appears.
Count: [N] of 4 sections.
Gate H: [PASS if N >= 3 / FAIL if N < 3]

[If FAIL: CORRECTION BLOCK — C-13 immediately here, before SECTION I.]

---

SECTION I — Gate: C-14 (Champion Rationale Double-Anchored)

Check whether every champion entry in SECTION E has both (a) archetype position rationale
AND (b) a named EM Inertia ID.

Go through each champion row in SECTION E's summary table.
Gate I: [PASS if all rows have both anchors / FAIL if any row is missing one]

[If FAIL: CORRECTION BLOCK — C-14 for each failing champion entry, immediately here, before SECTION J.]

---

SECTION J — Gate: C-15 (Churn Mitigations Are Concrete Actions)

Check whether every Team Mitigation Action in SECTION F's table names a concrete team action
(not solely a surveillance verb: monitor, track, watch, observe, measure).

Go through each mitigation row.
Gate J: [PASS if all rows have concrete actions / FAIL if any row is surveillance-only]

[If FAIL: CORRECTION BLOCK — C-15 for each failing mitigation, immediately here, before SECTION K.]

---

## SECTION K — Terminal Gate State Record

This section records gate outcomes only. It does NOT contain corrected content.
Corrected content appears in CORRECTION BLOCKS in Sections H, I, and J above.
SECTION K references those locations but does not duplicate them.

Self-verifying invariant: For every "Revision Performed: Yes" entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK
Location cited. An evaluator can verify this invariant by inspecting the cited location.

| Criterion | Initial Result | Revision Performed | CORRECTION BLOCK Location | Final Result |
|-----------|---------------|-------------------|--------------------------|-------------|
| C-13 — Inertia downstream backbone | [PASS / FAIL] | [Yes / No] | [Section H / N/A] | [PASS] |
| C-14 — Champion double-anchor | [PASS / FAIL] | [Yes / No] | [Section I / N/A] | [PASS] |
| C-15 — Churn action test | [PASS / FAIL] | [Yes / No] | [Section J / N/A] | [PASS] |

All three Final Results must show PASS before this artifact is committed.
```

---

## Summary: C-21/C-22/C-23 Design Properties per Variation

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| Explicit structural contract naming C-19/C-20 locations separately | Yes | Yes | No | Yes (names C-21/C-22/C-23 by ID) | Yes |
| Explicit negative rule: "SECTION K does NOT contain corrected content" | Yes | Yes | No | Yes | Yes |
| Self-verifying invariant in terminal section (C-22) | Named, simple | Named, with evaluability note | Absent | Named, with counter-example | Named, simple |
| Named verification boundary (C-23) | Yes: "## VERIFICATION MODE" | Yes: "## VERIFICATION MODE" | Partial: "## Verification Stage" (no mode-shift instruction) | Yes: "## VERIFICATION MODE" with mode-shift instruction | Yes: "## VERIFICATION MODE" with explicit mode-shift instruction |
| Inertia framing | Per-archetype | Per-archetype (bucket-derived) | Status-Quo Competitor named throughout | Per-archetype (inertia registry before phases) | Status-Quo Competitor named throughout |
| C-21 expected | PASS | PASS | **FAIL risk** | PASS | PASS |
| C-22 expected | PASS | PASS | **FAIL** | PASS | PASS |
| C-23 expected | PASS | PASS | PASS-RISK | PASS | PASS |
