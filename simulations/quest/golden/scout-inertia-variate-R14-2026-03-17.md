# scout-inertia -- Quest Variate R14

**Rubric**: C-series v14 (ceiling `aspirational_pass / 40 * 10`; denominator 36 → 40)
**Date**: 2026-03-17
**Previous round**: R13 confirmed C-41..C-44 across five scaffold types (per-artifact bracket
commands, compound-vocabulary threading, count quantifier in gate heading, imperative gate marker)
**R14 target**: First round targeting C-45..C-48
**New criteria**: C-45 (artifact ID enumeration in gate heading interrogative) + C-46 (compound
domain-axis threading vocabulary) + C-47 (PROVISIONAL threat score pre-declaration at Stage 0)
+ C-48 (evidence-triggered PROVISIONAL revision directive)

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing | Compound term `STATUS QUO COMPETITOR` (C-46) in section-based scaffold; gate names `Q3 AND Q4 STATUS QUO COMPETITOR BRIDGES` (C-45); Section 0 pre-declares PROVISIONAL (C-47); Section 4 carries revision directive (C-48) |
| V-02 | Lifecycle emphasis (reference form) | Stage-based structure; compound term `INERTIA DEFAULT COMPETITOR` (C-46); gate names `Q3 AND Q4 INERTIA DEFAULT COMPETITOR BRIDGES` (C-45); Stage 0 PROVISIONAL (C-47); Stage 5A revision directive (C-48) -- R14 reference baseline |
| V-03 | Phrasing register | Full COMMAND register; compound term `INERTIA LOCK COMPETITOR` (C-46); gate names artifact IDs with parenthetical class labels `Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` (C-45); Section 0 PROVISIONAL (C-47); Section 4 revision directive (C-48) |
| V-04 | Output format (consolidated bridge) | Stage-based consolidated triple-block bridge; compound term `INCUMBENT DEFAULT COMPETITOR` (C-46); bracket-prefix A-23; gate names `Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` in combined A-25+A-27 heading (C-45); Stage 0 PROVISIONAL (C-47); Stage 5A revision directive (C-48) |
| V-05 | All axes combined | COMMAND register throughout; compound term `DO-NOTHING DEFAULT COMPETITOR` (C-46); gate names `Q3 AND Q4 DO-NOTHING DEFAULT BRIDGES` (C-45); Section 0 PROVISIONAL (C-47); Section 4 revision directive (C-48); domain-prefix rule labels carrying full C-46 vocabulary |

---

## R14 Design Notes

### C-45 -- Artifact ID enumeration in gate heading interrogative

C-43 (v13) required an explicit count quantifier in the gate heading so the author could determine
from the heading alone how many artifacts must be present. "BOTH" passes C-43 (count = 2);
"ALL" fails (count indeterminate from heading alone).

C-45 extends C-43: the count alone is insufficient -- the author must be able to determine WHICH
artifacts by name from the heading, not only how many. "BOTH BRIDGE ARTIFACTS BEEN POPULATED?"
passes C-43 (count determinable: 2) but fails C-45 (artifact identities indeterminate: which
two?). "BOTH Q3 AND Q4 BRIDGES BEEN POPULATED?" passes both: count = 2 (BOTH) and identities =
Q3 and Q4.

Five label forms tested across V-01..V-05:
- **V-01**: `BOTH Q3 AND Q4 STATUS QUO COMPETITOR BRIDGES` -- Q3/Q4 before artifact-class noun
- **V-02**: `BOTH Q3 AND Q4 INERTIA DEFAULT COMPETITOR BRIDGES` -- same structure, different vocab
- **V-03**: `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` -- parenthetical class labels
  after each artifact ID; artifact class distributed per-artifact rather than grouped after BOTH
- **V-04**: `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` -- same parenthetical form
  embedded in combined A-25+A-27 heading (stress test: does C-45 pass inside a combined heading?)
- **V-05**: `BOTH Q3 AND Q4 DO-NOTHING DEFAULT BRIDGES` -- Q3/Q4 with axis-vocabulary artifact class

### C-46 -- Compound domain-axis threading vocabulary

C-42 (v13) required three or more bracket elements to share domain-vocabulary threading. A
single-axis term like "STATUS QUO" or "INERTIA THREAT" passed C-42.

C-46 extends C-42: the threading term must name BOTH the domain axis (the threat dimension,
e.g., "STATUS QUO") AND the structural role of the artifact in the analysis (e.g., "COMPETITOR").
A single-axis term passes C-42 and fails C-46. A compound term ("STATUS QUO COMPETITOR") passes
both.

Five compound terms tested:
- **V-01**: `STATUS QUO COMPETITOR` -- axis: STATUS QUO / role: COMPETITOR (rubric example form)
- **V-02**: `INERTIA DEFAULT COMPETITOR` -- axis: INERTIA DEFAULT / role: COMPETITOR
- **V-03**: `INERTIA LOCK COMPETITOR` -- axis: INERTIA LOCK / role: COMPETITOR
- **V-04**: `INCUMBENT DEFAULT COMPETITOR` -- axis: INCUMBENT DEFAULT / role: COMPETITOR
- **V-05**: `DO-NOTHING DEFAULT COMPETITOR` -- axis: DO-NOTHING DEFAULT / role: COMPETITOR

The compound term threads through: FAIL-FIRST heading, Section/Stage 1 heading, A-16 rule label,
A-19 rule label, A-31 rule label, Q3/Q4 section headings, and gate heading artifact class. C-46
implies C-42: compound threading satisfies C-42 (threading present) and additionally satisfies
C-46 (threading is compound). C-42 pass is necessary but not sufficient for C-46.

### C-47 -- PROVISIONAL threat score pre-declaration at Stage 0

C-03 (essential) requires a threat score declared somewhere in the scaffold. C-47 tightens the
requirement: the declaration must appear at Stage 0 specifically, BEFORE evidence is gathered,
and non-HIGH pre-evidence scores must carry an explicit PROVISIONAL marker.

C-47 structural requirements:
1. A Stage 0 (or Section 0) section must appear BEFORE Stage 1 / FM Inventory
2. That stage/section must contain a threat score field
3. If the pre-evidence score is not HIGH, the template must carry an explicit PROVISIONAL marker
4. The PROVISIONAL marker signals that evidence gathered in later stages may revise the score

Scaffold pattern: the Stage 0 table pre-populates with HIGH (the default per the skill description)
and carries a PROVISIONAL marker mechanism (e.g., template instruction or column) for non-HIGH
cases. The pre-declared HIGH does not need PROVISIONAL since it is the default; PROVISIONAL is
specifically required for non-HIGH pre-evidence assessments.

### C-48 -- Evidence-triggered PROVISIONAL revision directive

C-48 extends C-47: a stage that follows evidence-gathering must carry an explicit directive
instructing the author to RETURN TO STAGE 0 and REVISE any PROVISIONAL score based on gathered
evidence. C-48 closes the staged-commitment loop: Stage 0 pre-declares → evidence gathered in
Stages 3-4 → Stage 5A directs revision of Stage 0.

C-48 structural requirement: an explicit instruction at the evidence-assessment stage (Stage 5A
or Section 4) naming Stage 0 specifically and the action "revise PROVISIONAL." The instruction
must be actionable: "revisit Stage 0" alone fails if it does not specify what to revise.

C-47 + C-48 together constitute the full staged-commitment protocol. C-48 cannot pass if C-47
fails: there is no PROVISIONAL declaration to revise.

---

## V-01 -- Inertia Framing Axis

**Axis**: Section-based structure; compound threading "STATUS QUO COMPETITOR" throughout all
rule labels and headings (C-46 focus); blockquote-wrapped COMMAND prompts (A-29+A-30); gate
heading names Q3 AND Q4 specifically (C-45); Section 0 carries PROVISIONAL threat score
pre-declaration (C-47); Section 4 contains explicit revision directive back to Section 0 (C-48).
**Hypothesis**: The compound term "STATUS QUO COMPETITOR" (domain axis: STATUS QUO / structural
role: COMPETITOR) threads consistently through FAIL-FIRST heading, Section 1 heading, all three
rule labels (A-16, A-19, A-31), and the gate heading artifact class, satisfying C-46 and C-42
simultaneously. C-45 passes because the gate heading interrogative names Q3 and Q4 by artifact
ID before the artifact-class noun ("Q3 AND Q4 STATUS QUO COMPETITOR BRIDGES"), making both count
and identity determinable from the heading alone.
**Predicted score**: 40/40

---

```
## SECTION 0 -- STATUS QUO COMPETITOR PRE-ASSESSMENT

Declare the inertia threat score before evidence is gathered. This is the pre-evidence
commitment point. If the pre-evidence score is not HIGH, mark it PROVISIONAL here and
return to revise it at Section 4 after evidence in Sections 2-3 is complete.

> [C-03 COMMAND]: RECORD the pre-evidence threat score in the table below. If you assess
> non-HIGH at this stage, append (PROVISIONAL) to the score. You will revisit this entry
> at Section 4.

| Pre-evidence dimension    | Assessment                 | PROVISIONAL? |
|---------------------------|----------------------------|--------------|
| Threat score              | HIGH                       | --           |
| Competitor identity       | Current workaround / status quo workflow | -- |
| Expected inertia strength | High (teams rarely abandon functioning processes) | -- |
| Switching resistance      | High                       | PROVISIONAL if non-HIGH |

---

## FAIL-FIRST DECLARATION -- THE STATUS QUO COMPETITOR

The STATUS QUO COMPETITOR is this feature's primary adversary. It has no vendor, no
roadmap, and no champion. It wins by existing. Every team that does not adopt this feature
is choosing the STATUS QUO COMPETITOR -- consciously or by default.

> **STATUS QUO COMPETITOR FAIL-FIRST RULE [A-31]**: Map the STATUS QUO COMPETITOR's
> failure modes before authoring any defeat condition. A defeat condition is only valid if
> it derives from a documented failure mode. No FM-[N] in Section 1 = no DC-[N] in
> Section 5. This ordering cannot be reversed.

Bridge artifacts required before defeat conditions are valid:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> R-02): each FM-[N] mapped to the role
  experiencing it
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): each FM-[N] mapped to its
  triggering condition and measurable threshold

---

## SECTION 1 -- STATUS QUO COMPETITOR FM INVENTORY: STRUCTURAL WEAKNESSES

> [C-05 COMMAND]: NAME every specific failure mode where the STATUS QUO COMPETITOR
> breaks, produces errors, causes rework, or hits a scale ceiling. REJECT generic
> descriptions -- "manual" or "slow" without specifics fails. "CSV export silently
> truncates rows above 65,536 with no error message" passes. MINIMUM 2 rows required.

> **STATUS QUO COMPETITOR PRIMARY KEY RULE [A-16]**: FM-[N] is the primary key for all
> failure modes in this analysis. Assign every FM-[N] identifier in this table before
> authoring Q3, Q4, or Section 5. Every downstream citation of FM-[N] must trace to a
> row in this table. Missing or duplicate keys invalidate the referential chain.

| FM-[N] | Failure mode description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger condition (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|------------------------------------------------------------------------------------------|------------------------------------|---------------------------------------|-----------------------------|
| FM-01  |                                                                                          |                                    |                                       |                             |
| FM-02  |                                                                                          |                                    |                                       |                             |

---

## Q3 -- STATUS QUO COMPETITOR FM->ACTOR BRIDGE (closes C-05 -> R-02)

> [C-05 BRIDGE ARTIFACT Q3 COMMAND]: COMPLETE this bridge before advancing to the gate.
> Map each FM-[N] to the specific role experiencing that failure. Attribute the failure
> at the role level -- "engineering team" is insufficient; "data-ops team managing weekly
> pipeline exports" passes.

| FM-[N] | Role experiencing the failure (e.g., data-ops team managing weekly pipeline exports) | Role-level consequence (e.g., 2 hours of manual remediation per export cycle) |
|--------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| FM-01  |                                                                                       |                                                                                |
| FM-02  |                                                                                       |                                                                                |

---

## Q4 -- STATUS QUO COMPETITOR FM->TRIGGER BRIDGE (closes C-05 -> C-04)

> [C-05 BRIDGE ARTIFACT Q4 COMMAND]: COMPLETE this bridge before advancing to the gate.
> Map each FM-[N] to its triggering condition and measurable threshold. The threshold here
> becomes the basis for defeat conditions in Section 5 -- a missing or vague threshold
> produces an untestable defeat condition.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-01  |                                                           |                                                      |
| FM-02  |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 AND Q4 STATUS QUO COMPETITOR BRIDGES BEEN POPULATED?

| Bridge artifact                                         | Populated? (Y / N) |
|---------------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)           |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)         |                    |

**[BRIDGE COMPLETION COMMAND]**: Do not proceed to Section 2 unless both rows above show
Y. If either shows N: return to the corresponding bridge section above and complete the
missing rows. An unpopulated bridge produces defeat conditions with no traceable actor or
threshold.

---

## SECTION 2 -- STATUS QUO COMPETITOR WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific tool, file type, or procedure the STATUS QUO
> COMPETITOR relies on. NOT "a manual process" -- name it. NAME the role performing it.
> QUANTIFY the ongoing effort cost with a number and a unit (e.g., 2 hours/week).

| Workaround name (specific tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | In active use since (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|---------------------------------------|
|                                                          |                    |                                   |                                       |

---

## SECTION 3 -- STATUS QUO COMPETITOR SWITCHING COST ANALYSIS

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit -- "significant overhead" without a number fails. NAME the role or
> team bearing each cost. Example: "8 hours/week x 6-week ramp = 48 hours per engineer."

| Cost category       | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|---------------------|-------------|-------------------------|---------------------------------------|
| Migration effort    |             |                         |                                       |
| Training overhead   |             |                         |                                       |
| Process disruption  |             |                         |                                       |
| In-flight work risk |             |                         |                                       |

---

## SECTION 4 -- STATUS QUO COMPETITOR THREAT ASSESSMENT

> [C-03 COMMAND]: REVISIT SECTION 0 NOW. Based on evidence gathered in Sections 2-3,
> revise any PROVISIONAL entries in the Section 0 pre-assessment table. Update the threat
> score if evidence warrants. Then record the confirmed threat score below.

| Assessment dimension        | Score | Evidence basis |
|-----------------------------|-------|----------------|
| Threat score (confirmed)    | HIGH  |                |
| Primary inertia driver      |       |                |
| Switching cost magnitude    |       |                |
| Workaround maturity         |       |                |

---

## SECTION 5 -- STATUS QUO COMPETITOR DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the
> triggers documented in Q4. Each condition must name a measurable threshold with a unit.
> "Teams switch when they see value" fails. "Error rate exceeds 3 incidents/sprint for 4
> consecutive sprints" passes. Two structurally distinct threshold types required
> (e.g., volume-based AND frequency-based).

> **STATUS QUO COMPETITOR CITATION RULE [A-19]**: Every DC-[N] in this table MUST cite
> the originating FM-[N] from Section 1. Every FM-[N] in Section 1 MUST appear in at
> least one DC-[N] row. Bidirectional integrity: Section 1 -> Section 5 and Section 5 ->
> Section 1 must both hold. Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] | Threshold (e.g., >10MB, >3 failures/week) | Team segment |
|--------|------------------------------------------|--------|-------------------------------------------|--------------|
| DC-01  |                                          | FM-01  |                                           |              |
| DC-02  |                                          | FM-02  |                                           |              |

---

## SECTION 6 -- STATUS QUO COMPETITOR COMPLETENESS CHECKLIST

| # | Criterion | Satisfied? (Y / N) |
|---|-----------|---------------------|
| C-01: | Workaround named specifically (tool/procedure/file type) with role and ongoing cost (number + unit) | |
| C-02: | At least two switching cost categories quantified with number + unit per named role or team | |
| C-03: | Threat score declared at Section 0 (PROVISIONAL if non-HIGH) and confirmed/revised at Section 4 | |
| C-04: | At least two defeat conditions, each falsifiable, each citing FM-[N], each with measurable threshold | |
| C-05: | FM inventory complete with FM-[N] keys; Q3 and Q4 bridge artifacts populated before gate | |
```

---

## V-02 -- Lifecycle Emphasis Axis (Reference Form)

**Axis**: Stage-based structure (STAGE 0 through STAGE 6); compound threading "INERTIA DEFAULT
COMPETITOR" throughout all stage headings and rule labels (C-46); inline `[C-0N COMMAND]:`
prompts; bracket-suffix A-23 style; gate heading names Q3 AND Q4 by ID (C-45); Stage 0 is the
dedicated PROVISIONAL pre-declaration stage (C-47); Stage 5A carries the explicit revision
directive back to Stage 0 (C-48). This is the R14 C-series reference baseline.
**Hypothesis**: Stage 0 as a named stage with a structured pre-assessment table is the clearest
C-47 + C-48 implementation -- the stage boundary makes the commitment point explicit, and the
Stage 5A directive "REVISIT STAGE 0 AND REVISE PROVISIONAL" closes the loop unambiguously.
The bracket-suffix compound rule labels ("INERTIA DEFAULT COMPETITOR PRIMARY KEY RULE [A-16]",
"INERTIA DEFAULT COMPETITOR CITATION RULE [A-19]", "INERTIA DEFAULT COMPETITOR FAIL-FIRST RULE
[A-31]") carry the full compound threading term under consistent C-46 vocabulary.
**Predicted score**: 40/40

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA DEFAULT COMPETITOR

The INERTIA DEFAULT COMPETITOR does not compete by winning -- it competes by persisting.
Teams adopt the INERTIA DEFAULT COMPETITOR by doing nothing. It carries no switching cost,
no onboarding burden, and no change management overhead.

INERTIA DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]: Map the INERTIA DEFAULT COMPETITOR's
failure modes at Stage 1 before any defeat condition is authored at Stage 5B. This is the
authoring sequence constraint. It cannot be reversed.

Authoring sequence:
- Stage 0 -- PRE-ASSESSMENT: declare threat score (PROVISIONAL if non-HIGH)
- Stage 1 -- FM INVENTORY (C-05): where the INERTIA DEFAULT COMPETITOR breaks
- Stage 2 -- BRIDGE STAGE: Q3 (FM->actor, closes C-05 -> R-02) + Q4 (FM->trigger,
  closes C-05 -> C-04) + completion gate
- Stage 3 -- WORKAROUND PROFILE (C-01): specific tool, role, ongoing cost
- Stage 4 -- SWITCHING COST (C-02): quantified cost to abandon the INERTIA DEFAULT
  COMPETITOR
- Stage 5A -- THREAT ASSESSMENT (C-03): confirm/revise Stage 0 pre-assessment
- Stage 5B -- DEFEAT CONDITIONS (C-04): conditions under which the INERTIA DEFAULT
  COMPETITOR loses
- Stage 6 -- COMPLETENESS CHECK

The Stage 2 gate must show Y for both bridge artifacts before Stage 3 is authored.

---

## STAGE 0 -- INERTIA DEFAULT COMPETITOR PRE-ASSESSMENT

Record the pre-evidence threat assessment before Stage 1 is authored. If the pre-evidence
score is not HIGH, mark it PROVISIONAL. You will revisit this table at Stage 5A.

[C-03 COMMAND]: RECORD the INERTIA DEFAULT COMPETITOR's threat score in the table below.
HIGH is the default -- the INERTIA DEFAULT COMPETITOR always starts with home-field
advantage. If pre-evidence assessment is non-HIGH, append (PROVISIONAL) to the score
entry in this table and state a specific reason. Revise at Stage 5A.

| Stage 0 dimension              | Pre-evidence assessment             | PROVISIONAL? |
|--------------------------------|-------------------------------------|--------------|
| Threat score                   | HIGH                                | --           |
| Competitor identity            | Current workaround / status quo     | --           |
| Primary inertia driver         |                                     | PROVISIONAL if non-HIGH |
| Expected switching resistance  | High                                | PROVISIONAL if non-HIGH |

---

## STAGE 1 -- INERTIA DEFAULT COMPETITOR FM INVENTORY: WHERE IT BREAKS

[C-05 COMMAND]: NAME every specific failure mode where the INERTIA DEFAULT COMPETITOR
(current workaround) fails, produces errors, causes rework, or hits a scale ceiling.
REJECT generic descriptions -- "slow" or "manual" alone fails. "CSV export silently
truncates rows above 65,536 with no error message" passes. MINIMUM 2 rows required.

> **INERTIA DEFAULT COMPETITOR PRIMARY KEY RULE [A-16]**: FM-[N] is the primary key.
> Assign every FM-[N] identifier here before authoring Q3, Q4, or Stage 5B. Every
> downstream reference must trace to a row in this table. Missing keys invalidate the
> referential integrity chain.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger condition (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|---------------------------------------|-----------------------------|
| FM-01  |                                                                                       |                                    |                                       |                             |
| FM-02  |                                                                                       |                                    |                                       |                             |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- INERTIA DEFAULT COMPETITOR FM->ACTOR BRIDGE (closes C-05 -> R-02)

[C-05 BRIDGE ARTIFACT Q3 COMMAND]: COMPLETE Q3 before advancing to the gate. Map each
FM-[N] to the specific role experiencing that failure. "Engineering" is insufficient;
"data-ops team managing weekly pipeline exports" passes.

| FM-[N] | Role experiencing the failure (e.g., data-ops team managing weekly pipeline exports) | Role-level consequence (e.g., 2 hours of manual remediation per cycle) |
|--------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| FM-01  |                                                                                       |                                                                        |
| FM-02  |                                                                                       |                                                                        |

### Q4 -- INERTIA DEFAULT COMPETITOR FM->TRIGGER BRIDGE (closes C-05 -> C-04)

[C-05 BRIDGE ARTIFACT Q4 COMMAND]: COMPLETE Q4 before advancing to the gate. Map each
FM-[N] to its triggering condition and measurable threshold. The threshold in Q4 becomes
the basis for defeat conditions at Stage 5B.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-01  |                                                           |                                                      |
| FM-02  |                                                           |                                                      |

### STAGE 2 COMPLETION GATE -- HAVE BOTH Q3 AND Q4 INERTIA DEFAULT COMPETITOR BRIDGES BEEN POPULATED?

| Bridge artifact                                              | Populated? (Y / N) |
|--------------------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> R-02)                |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)              |                    |

**[BRIDGE COMPLETION COMMAND]**: Do not advance to Stage 3 unless both rows above show Y.
If either shows N: return to the corresponding bridge sub-section above and complete the
missing rows before proceeding.

---

## STAGE 3 -- INERTIA DEFAULT COMPETITOR WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific tool, file type, or procedure that constitutes the
INERTIA DEFAULT COMPETITOR. NOT "a manual process" -- name it. NAME the role performing
it. QUANTIFY the ongoing effort with a number and a unit (e.g., 2 hours/week).

| Workaround name (specific tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | In active use since (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|---------------------------------------|
|                                                          |                    |                                   |                                       |

---

## STAGE 4 -- INERTIA DEFAULT COMPETITOR SWITCHING COST ANALYSIS

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
number and a unit -- "significant" without a number fails. NAME the role bearing each
cost. Example: "8 hours/week x 6-week ramp = 48 hours per engineer."

| Cost category       | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|---------------------|-------------|-------------------------|---------------------------------------|
| Migration effort    |             |                         |                                       |
| Training overhead   |             |                         |                                       |
| Process disruption  |             |                         |                                       |
| In-flight work risk |             |                         |                                       |

---

## STAGE 5A -- INERTIA DEFAULT COMPETITOR THREAT ASSESSMENT

[C-03 COMMAND]: REVISIT STAGE 0 NOW. Based on evidence gathered in Stages 3 and 4,
return to the Stage 0 pre-assessment table and revise any PROVISIONAL entries. Update
the threat score at Stage 0 if evidence warrants a change. Then record the confirmed
score below.

| Assessment dimension        | Confirmed score | Evidence basis |
|-----------------------------|-----------------|----------------|
| Threat score                | HIGH            |                |
| Primary inertia driver      |                 |                |
| Switching cost magnitude    |                 |                |
| Workaround stability        |                 |                |

---

## STAGE 5B -- INERTIA DEFAULT COMPETITOR DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the
trigger thresholds documented in Q4. Each condition must name a measurable threshold
with a unit. Two structurally distinct threshold types required (e.g., volume-based >10MB
AND frequency-based >3 failures/week).

> **INERTIA DEFAULT COMPETITOR CITATION RULE [A-19]**: Every DC-[N] in this table MUST
> cite the originating FM-[N] from Stage 1. Every FM-[N] at Stage 1 MUST appear in at
> least one DC-[N] row here. Bidirectional integrity: Stage 1 -> Stage 5B and Stage 5B
> -> Stage 1 must both hold. Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] | Threshold (e.g., >10MB, >3 failures/week) | Team segment |
|--------|------------------------------------------|--------|-------------------------------------------|--------------|
| DC-01  |                                          | FM-01  |                                           |              |
| DC-02  |                                          | FM-02  |                                           |              |

---

## STAGE 6 -- INERTIA DEFAULT COMPETITOR COMPLETENESS CHECK

| # | Criterion | Satisfied? (Y / N) |
|---|-----------|---------------------|
| C-01: | Workaround named specifically with role and ongoing cost (number + unit) | |
| C-02: | At least two switching cost categories quantified with number + unit per named role | |
| C-03: | Threat score pre-declared at Stage 0 (PROVISIONAL if non-HIGH) and confirmed/revised at Stage 5A | |
| C-04: | At least two defeat conditions, each falsifiable, each citing FM-[N], each with measurable threshold | |
| C-05: | FM inventory complete with FM-[N] keys; Q3 and Q4 bridge artifacts fully populated | |
```

---

## V-03 -- Phrasing Register Axis

**Axis**: Full COMMAND register throughout (all directives in imperative caps); compound
threading "INERTIA LOCK COMPETITOR" (domain axis: INERTIA LOCK / structural role: COMPETITOR)
in C-46 focus; domain-prefix rule labels consistent with C-46 vocabulary ("INERTIA LOCK
COMPETITOR RULE [A-16]", "INERTIA LOCK COMPETITOR CITATION RULE [A-19]", "INERTIA LOCK
COMPETITOR FAIL-FIRST RULE [A-31]"); gate heading names Q3 AND Q4 with parenthetical class
labels after each artifact ID (C-45: "Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)");
Section 0 PROVISIONAL (C-47); Section 4 revision directive (C-48).
**Hypothesis**: Parenthetical class labels distributed per-artifact ID ("Q3 (FM-ACTOR-BRIDGE)
AND Q4 (FM-TRIGGER-BRIDGE)") satisfy C-45 in a structurally distinct form from V-01/V-02's
"Q3 AND Q4 [CLASS]" ordering -- the artifact class is named per artifact rather than once after
both IDs. Both count (BOTH) and identity (Q3, Q4) remain determinable from the heading alone.
C-46 vocabulary is fully domain-prefixed: the compound term "INERTIA LOCK COMPETITOR" prefixes
every bracket-labeled rule, creating a single vocabulary family across A-16, A-19, and A-31 rule
labels.
**Predicted score**: 40/40

---

```
## SECTION 0 -- INERTIA LOCK COMPETITOR: PRE-ASSESSMENT COMMAND

RECORD THE PRE-EVIDENCE THREAT SCORE BEFORE AUTHORING ANY SECTION.

The INERTIA LOCK COMPETITOR is the incumbent workflow. It locks teams in by making
switching costly. Pre-declare the threat score here. Return to revise at Section 4.

[C-03 COMMAND]: RECORD the INERTIA LOCK COMPETITOR's threat score in the table below.
HIGH is the default. If non-HIGH, append (PROVISIONAL) and STATE a specific measurable
reason. RETURN to this table at Section 4 after evidence in Sections 2-3 is complete.

| Pre-evidence dimension       | Assessment         | Marker            |
|------------------------------|--------------------|-------------------|
| Threat score                 | HIGH               | --                |
| Competitor lock mechanism    |                    | PROVISIONAL if non-HIGH |
| Expected switching resistance| High               | PROVISIONAL if non-HIGH |

---

## FAIL-FIRST DECLARATION -- THE INERTIA LOCK COMPETITOR

MAP THE INERTIA LOCK COMPETITOR'S FAILURE MODES FIRST. AUTHOR NO DEFEAT CONDITION
WITHOUT A TRACEABLE FAILURE MODE.

INERTIA LOCK COMPETITOR FAIL-FIRST RULE [A-31]: The INERTIA LOCK COMPETITOR fails at
specific measurable thresholds. These thresholds are failure modes. Map them at Section 1
before writing a single defeat condition at Section 5. The authoring order cannot be
reversed.

Bridge artifacts required:
- **Q3 (FM-ACTOR-BRIDGE)** (closes C-05 -> R-02): each FM-[N] attributed to the role
  experiencing it
- **Q4 (FM-TRIGGER-BRIDGE)** (closes C-05 -> C-04): each FM-[N] mapped to its triggering
  condition and measurable threshold

---

## SECTION 1 -- INERTIA LOCK COMPETITOR FM INVENTORY

[C-05 COMMAND]: NAME EVERY SPECIFIC FAILURE MODE. REJECT GENERIC DESCRIPTIONS.
"MANUAL" OR "SLOW" ALONE FAILS. NAME THE SPECIFIC FAILURE: "CSV EXPORT SILENTLY
TRUNCATES ROWS ABOVE 65,536 -- NO ERROR MESSAGE" PASSES. MINIMUM 2 ROWS REQUIRED.

> **INERTIA LOCK COMPETITOR RULE [A-16]**: ASSIGN EVERY FM-[N] IDENTIFIER IN THIS TABLE
> BEFORE AUTHORING Q3, Q4, OR SECTION 5. FM-[N] IS THE PRIMARY KEY. EVERY DOWNSTREAM
> CITATION MUST TRACE TO A ROW HERE. MISSING KEYS INVALIDATE THE REFERENTIAL CHAIN.

| FM-[N] | FAILURE DESCRIPTION (e.g., CSV EXPORT SILENTLY TRUNCATES AT 65,536 ROWS) | ACTOR / ROLE (e.g., DATA-OPS TEAM) | TRIGGER (e.g., FILE > 10MB) | FREQUENCY (e.g., 2x/SPRINT) |
|--------|---------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-01  |                                                                           |                                    |                             |                             |
| FM-02  |                                                                           |                                    |                             |                             |

---

## Q3 (FM-ACTOR-BRIDGE) -- CLOSES C-05 -> R-02

[C-05 BRIDGE ARTIFACT Q3 COMMAND]: COMPLETE Q3 BEFORE ADVANCING TO THE GATE. MAP
EACH FM-[N] TO THE SPECIFIC ROLE EXPERIENCING THAT FAILURE. "ENGINEERING" FAILS.
"DATA-OPS TEAM MANAGING WEEKLY PIPELINE EXPORTS" PASSES.

| FM-[N] | ROLE EXPERIENCING THE FAILURE (e.g., DATA-OPS TEAM) | ROLE-LEVEL CONSEQUENCE (e.g., 2 HRS REMEDIATION/CYCLE) |
|--------|-----------------------------------------------------|--------------------------------------------------------|
| FM-01  |                                                     |                                                        |
| FM-02  |                                                     |                                                        |

---

## Q4 (FM-TRIGGER-BRIDGE) -- CLOSES C-05 -> C-04

[C-05 BRIDGE ARTIFACT Q4 COMMAND]: COMPLETE Q4 BEFORE ADVANCING TO THE GATE. MAP
EACH FM-[N] TO ITS TRIGGERING CONDITION AND MEASURABLE THRESHOLD. THE THRESHOLD
HERE BECOMES THE BASIS FOR DEFEAT CONDITIONS AT SECTION 5.

| FM-[N] | TRIGGERING CONDITION (e.g., PIPELINE INGESTS FILE > 10MB) | MEASURABLE THRESHOLD (e.g., >10MB, >3 FAILURES/WEEK) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-01  |                                                           |                                                      |
| FM-02  |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- COMPLETE BEFORE ADVANCING -- HAVE BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE) BEEN POPULATED?

| Bridge artifact                                          | Populated? (Y / N) |
|----------------------------------------------------------|--------------------|
| Q3 (FM-ACTOR-BRIDGE) -- closes C-05 -> R-02             |                    |
| Q4 (FM-TRIGGER-BRIDGE) -- closes C-05 -> C-04           |                    |

**[BRIDGE COMPLETION COMMAND]**: DO NOT ADVANCE TO SECTION 2 UNLESS BOTH ROWS SHOW Y.
IF EITHER SHOWS N: RETURN TO THE CORRESPONDING BRIDGE SECTION ABOVE AND COMPLETE
THE MISSING ROWS BEFORE PROCEEDING.

---

## SECTION 2 -- INERTIA LOCK COMPETITOR WORKAROUND PROFILE

[C-01 COMMAND]: NAME THE SPECIFIC TOOL, FILE TYPE, OR PROCEDURE. NOT "A MANUAL
PROCESS" -- NAME IT. NAME THE ROLE PERFORMING IT. QUANTIFY THE ONGOING COST WITH
A NUMBER AND A UNIT (e.g., 2 HOURS/WEEK).

| WORKAROUND NAME (SPECIFIC TOOL / FILE TYPE / PROCEDURE) | ROLE PERFORMING IT | ONGOING COST (e.g., 2 HOURS/WEEK) | IN ACTIVE USE SINCE (e.g., 18 MONTHS) |
|---------------------------------------------------------|--------------------|-----------------------------------|---------------------------------------|
|                                                         |                    |                                   |                                       |

---

## SECTION 3 -- INERTIA LOCK COMPETITOR SWITCHING COST ANALYSIS

[C-02 COMMAND]: IDENTIFY AT LEAST TWO SWITCHING COST CATEGORIES. QUANTIFY EACH
WITH A NUMBER AND A UNIT -- "SIGNIFICANT" WITHOUT A NUMBER FAILS. NAME THE ROLE
BEARING EACH COST. EXAMPLE: "8 HOURS/WEEK x 6-WEEK RAMP = 48 HOURS PER ENGINEER."

| COST CATEGORY       | DESCRIPTION | ESTIMATE (e.g., 3 DAYS) | ROLE BEARING IT (e.g., DATA-OPS TEAM) |
|---------------------|-------------|-------------------------|---------------------------------------|
| MIGRATION EFFORT    |             |                         |                                       |
| TRAINING OVERHEAD   |             |                         |                                       |
| PROCESS DISRUPTION  |             |                         |                                       |
| IN-FLIGHT WORK RISK |             |                         |                                       |

---

## SECTION 4 -- INERTIA LOCK COMPETITOR THREAT ASSESSMENT

[C-03 COMMAND]: RETURN TO SECTION 0. REVISE ANY PROVISIONAL ENTRIES IN THE
SECTION 0 PRE-ASSESSMENT TABLE BASED ON EVIDENCE IN SECTIONS 2-3. UPDATE THE
THREAT SCORE AT SECTION 0 IF WARRANTED. THEN RECORD THE CONFIRMED SCORE BELOW.

| ASSESSMENT DIMENSION        | CONFIRMED SCORE | EVIDENCE BASIS |
|-----------------------------|-----------------|----------------|
| THREAT SCORE                | HIGH            |                |
| PRIMARY INERTIA DRIVER      |                 |                |
| SWITCHING COST MAGNITUDE    |                 |                |
| WORKAROUND STABILITY        |                 |                |

---

## SECTION 5 -- INERTIA LOCK COMPETITOR DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE AT LEAST TWO SPECIFIC, FALSIFIABLE DEFEAT CONDITIONS FROM
THE TRIGGER THRESHOLDS IN Q4. EACH MUST CARRY A MEASURABLE THRESHOLD WITH A UNIT.
"TEAMS SWITCH WHEN THEY SEE VALUE" FAILS. TWO STRUCTURALLY DISTINCT THRESHOLD TYPES
REQUIRED (e.g., VOLUME >10MB AND FREQUENCY >3 FAILURES/WEEK).

> **INERTIA LOCK COMPETITOR CITATION RULE [A-19]**: EVERY DC-[N] IN THIS TABLE MUST
> CITE THE ORIGINATING FM-[N] FROM SECTION 1. EVERY FM-[N] IN SECTION 1 MUST APPEAR
> IN AT LEAST ONE DC-[N] ROW HERE. BIDIRECTIONAL INTEGRITY REQUIRED. VERIFY BEFORE
> FILLING EACH ROW.

| DC-[N] | DEFEAT CONDITION (SPECIFIC, FALSIFIABLE) | FM-[N] | THRESHOLD (e.g., >10MB, >3 FAILURES/WEEK) | TEAM SEGMENT |
|--------|------------------------------------------|--------|-------------------------------------------|--------------|
| DC-01  |                                          | FM-01  |                                           |              |
| DC-02  |                                          | FM-02  |                                           |              |

---

## SECTION 6 -- INERTIA LOCK COMPETITOR COMPLETENESS CHECKLIST

| # | CRITERION | SATISFIED? (Y / N) |
|---|-----------|---------------------|
| C-01: | WORKAROUND NAMED SPECIFICALLY (TOOL/PROCEDURE) WITH ROLE AND ONGOING COST (NUMBER + UNIT) | |
| C-02: | AT LEAST TWO SWITCHING COST CATEGORIES QUANTIFIED WITH NUMBER + UNIT PER NAMED ROLE | |
| C-03: | THREAT SCORE PRE-DECLARED AT SECTION 0 (PROVISIONAL IF NON-HIGH); CONFIRMED/REVISED AT SECTION 4 | |
| C-04: | AT LEAST TWO DEFEAT CONDITIONS, FALSIFIABLE, FM-[N] CITED, MEASURABLE THRESHOLD EACH | |
| C-05: | FM INVENTORY COMPLETE WITH FM-[N] KEYS; Q3 AND Q4 BRIDGE ARTIFACTS FULLY POPULATED | |
```

---

## V-04 -- Output Format Axis (Consolidated Bridge)

**Axis**: Stage-based structure with consolidated triple-block bridge at Stage 2 (Q3 + Q4 +
gate as three named sub-sections of Stage 2); compound threading "INCUMBENT DEFAULT COMPETITOR"
(C-46); bracket-prefix A-23 style ("[A-16 PRIMARY KEY CONSTRAINT]", "[A-19 CITATION INTEGRITY
CONSTRAINT]", "[A-31 FAIL-FIRST ORDERING RULE]"); gate heading names Q3 AND Q4 with
parenthetical artifact descriptions embedded in the combined A-25+A-27 heading (C-45:
"[BRIDGE COMPLETION COMMAND]: CONFIRM -- HAVE BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4
(FM-TRIGGER-BRIDGE) BEEN POPULATED?"); Stage 0 PROVISIONAL (C-47); Stage 5A revision directive
(C-48).
**Hypothesis**: C-45 passes inside a combined A-25+A-27 heading -- the parenthetical artifact
descriptions "Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)" enumerate both count (BOTH) and
identity (Q3, Q4 by name) within the combined heading, making both determinable from the heading
alone. The combined heading form established in R13 V-04 (which satisfied A-25+A-27+A-33
simultaneously) extends to C-45 without structural cost: adding parenthetical artifact-class
labels to Q3 and Q4 within the existing form is sufficient.
**Predicted score**: 40/40

---

```
## FAIL-FIRST DECLARATION -- THE INCUMBENT DEFAULT COMPETITOR

The INCUMBENT DEFAULT COMPETITOR is every feature team's first competitor. It is the
existing workflow, tool, or convention that teams will keep using unless given a specific,
measurable reason to change. It costs nothing to maintain. It is zero-effort to continue.

[A-31 FAIL-FIRST ORDERING RULE]: Map the INCUMBENT DEFAULT COMPETITOR's failure modes
at Stage 1 before any defeat condition is authored at Stage 5B. Every defeat condition
must derive from a documented failure mode. This ordering cannot be reversed.

Bridge artifacts required before defeat conditions are valid:
- **Q3 (FM-ACTOR-BRIDGE)** (closes C-05 -> R-02): each FM-[N] attributed to the role
  experiencing it
- **Q4 (FM-TRIGGER-BRIDGE)** (closes C-05 -> C-04): each FM-[N] mapped to triggering
  condition and measurable threshold

---

## STAGE 0 -- INCUMBENT DEFAULT COMPETITOR PRE-ASSESSMENT

Record the pre-evidence threat score before Stage 1 is authored. The default is HIGH.
If the pre-evidence assessment is not HIGH, mark it PROVISIONAL and return to revise at
Stage 5A after evidence in Stages 3-4 is gathered.

[C-03 COMMAND]: RECORD the INCUMBENT DEFAULT COMPETITOR's threat score below. HIGH is
the default. If non-HIGH: append (PROVISIONAL) and state a specific reason. You will
revise at Stage 5A.

| Stage 0 dimension             | Pre-evidence assessment     | PROVISIONAL? |
|-------------------------------|-----------------------------|--------------|
| Threat score                  | HIGH                        | --           |
| Competitor identity           | Current workaround / tool   | --           |
| Primary inertia mechanism     |                             | PROVISIONAL if non-HIGH |
| Expected switching resistance | High                        | PROVISIONAL if non-HIGH |

---

## STAGE 1 -- INCUMBENT DEFAULT COMPETITOR FM INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the INCUMBENT DEFAULT COMPETITOR
breaks, causes errors, causes rework, or hits a scale ceiling. REJECT generic descriptions.
"Slow" alone fails. "CSV export silently truncates rows above 65,536 -- no error message"
passes. MINIMUM 2 rows required.

> **[A-16 PRIMARY KEY CONSTRAINT]**: FM-[N] is the primary key for all failure modes.
> Assign every FM-[N] identifier in this table before authoring Stage 2 Q3/Q4 or Stage
> 5B. Every downstream reference must trace to a row here. Missing keys invalidate the
> referential integrity chain.

| FM-[N] | Failure description (e.g., CSV export silently truncates at 65,536 rows -- no error) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|---------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-01  |                                                                                       |                                    |                             |                             |
| FM-02  |                                                                                       |                                    |                             |                             |

---

## STAGE 2 -- INCUMBENT DEFAULT COMPETITOR BRIDGE STAGE

### STAGE 2A -- Q3 (FM-ACTOR-BRIDGE): CLOSES C-05 -> R-02

[C-05 BRIDGE ARTIFACT Q3 COMMAND]: COMPLETE Q3 before advancing to the Stage 2 gate.
Map each FM-[N] to the role experiencing that failure. "Engineering" is insufficient;
"data-ops team managing weekly pipeline exports" passes.

| FM-[N] | Role experiencing the failure (e.g., data-ops team managing weekly pipeline exports) | Role-level consequence (e.g., 2 hrs remediation/cycle) |
|--------|---------------------------------------------------------------------------------------|-------------------------------------------------------|
| FM-01  |                                                                                       |                                                       |
| FM-02  |                                                                                       |                                                       |

### STAGE 2B -- Q4 (FM-TRIGGER-BRIDGE): CLOSES C-05 -> C-04

[C-05 BRIDGE ARTIFACT Q4 COMMAND]: COMPLETE Q4 before advancing to the Stage 2 gate.
Map each FM-[N] to its triggering condition and measurable threshold. The threshold here
is the basis for defeat conditions at Stage 5B.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-01  |                                                           |                                                      |
| FM-02  |                                                           |                                                      |

### [BRIDGE COMPLETION COMMAND]: CONFIRM -- HAVE BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE) BEEN POPULATED?

| Bridge artifact                                          | Populated? (Y / N) |
|----------------------------------------------------------|--------------------|
| Q3 (FM-ACTOR-BRIDGE) -- closes C-05 -> R-02             |                    |
| Q4 (FM-TRIGGER-BRIDGE) -- closes C-05 -> C-04           |                    |

Do not advance to Stage 3 unless both rows above show Y. Return to Stage 2A or 2B if
either shows N.

---

## STAGE 3 -- INCUMBENT DEFAULT COMPETITOR WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific tool, file type, or procedure that constitutes the
INCUMBENT DEFAULT COMPETITOR. NOT "a manual process" -- name it. NAME the role
performing it. QUANTIFY the ongoing cost with a number and a unit (e.g., 2 hours/week).

| Workaround name (specific tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | In active use since (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|---------------------------------------|
|                                                          |                    |                                   |                                       |

---

## STAGE 4 -- INCUMBENT DEFAULT COMPETITOR SWITCHING COST ANALYSIS

[C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with
a number and a unit -- "significant" without a number fails. NAME the role bearing each
cost. Example: "8 hours/week x 6-week ramp = 48 hours per engineer."

| Cost category       | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|---------------------|-------------|-------------------------|---------------------------------------|
| Migration effort    |             |                         |                                       |
| Training overhead   |             |                         |                                       |
| Process disruption  |             |                         |                                       |
| In-flight work risk |             |                         |                                       |

---

## STAGE 5A -- INCUMBENT DEFAULT COMPETITOR THREAT ASSESSMENT

[C-03 COMMAND]: REVISIT STAGE 0 NOW. Based on evidence gathered in Stages 3 and 4,
return to the Stage 0 pre-assessment table and revise any PROVISIONAL entries. Update
the threat score at Stage 0 if warranted. Then record the confirmed score below.

| Assessment dimension        | Confirmed score | Evidence basis |
|-----------------------------|-----------------|----------------|
| Threat score                | HIGH            |                |
| Primary inertia driver      |                 |                |
| Switching cost magnitude    |                 |                |
| Workaround stability        |                 |                |

---

## STAGE 5B -- INCUMBENT DEFAULT COMPETITOR DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the
trigger thresholds in Q4. Each must carry a measurable threshold with a unit. Two
structurally distinct threshold types required (e.g., volume-based >10MB AND
frequency-based >3 failures/week).

> **[A-19 CITATION INTEGRITY CONSTRAINT]**: Every DC-[N] in this table MUST cite the
> originating FM-[N] from Stage 1. Every FM-[N] in Stage 1 MUST appear in at least one
> DC-[N] row here. Bidirectional integrity required. Verify before filling each row.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] | Threshold (e.g., >10MB, >3 failures/week) | Team segment |
|--------|------------------------------------------|--------|-------------------------------------------|--------------|
| DC-01  |                                          | FM-01  |                                           |              |
| DC-02  |                                          | FM-02  |                                           |              |

---

## STAGE 6 -- INCUMBENT DEFAULT COMPETITOR COMPLETENESS CHECKLIST

| # | Criterion | Satisfied? (Y / N) |
|---|-----------|---------------------|
| C-01: | Workaround named specifically with role and ongoing cost (number + unit) | |
| C-02: | At least two switching cost categories quantified with number + unit per named role | |
| C-03: | Threat score pre-declared at Stage 0 (PROVISIONAL if non-HIGH); confirmed/revised at Stage 5A | |
| C-04: | At least two defeat conditions, falsifiable, FM-[N] cited, measurable threshold each | |
| C-05: | FM inventory complete with FM-[N] keys; Q3 and Q4 bridge artifacts fully populated | |
```

---

## V-05 -- All Axes Combined

**Axis**: Section-based structure with COMMAND register throughout; compound threading
"DO-NOTHING DEFAULT COMPETITOR" (domain axis: DO-NOTHING DEFAULT / structural role: COMPETITOR)
in full C-46 domain-prefix vocabulary; gate names "Q3 AND Q4 DO-NOTHING DEFAULT BRIDGES" (C-45,
artifact class uses C-46 axis vocabulary as the artifact-class noun); Section 0 PROVISIONAL
pre-assessment (C-47); Section 4 carries explicit revision directive back to Section 0 (C-48);
bracket-label variant FAIL-FIRST heading; domain-prefix rule labels using full C-46 vocabulary
across A-16, A-19, and A-31 rules.
**Hypothesis**: The compound term "DO-NOTHING DEFAULT COMPETITOR" can serve as both the
analytical frame (C-46: domain-axis = DO-NOTHING DEFAULT / structural role = COMPETITOR) AND
the artifact-class noun in the gate heading (C-45: "Q3 AND Q4 DO-NOTHING DEFAULT BRIDGES" --
the artifact class "DO-NOTHING DEFAULT BRIDGES" is derived from the C-46 axis vocabulary,
creating the deepest cross-criterion vocabulary coherence of R14). Rule labels "DO-NOTHING
DEFAULT COMPETITOR PRIMARY KEY RULE [A-16]", "DO-NOTHING DEFAULT COMPETITOR CITATION RULE
[A-19]", and "DO-NOTHING DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]" form a complete C-46
vocabulary family spanning all three integrity layers.
**Predicted score**: 40/40

---

```
## SECTION 0 -- DO-NOTHING DEFAULT COMPETITOR: PRE-ASSESSMENT

RECORD THE PRE-EVIDENCE THREAT SCORE BEFORE ANY SECTION IS AUTHORED.

The DO-NOTHING DEFAULT COMPETITOR wins by requiring no action from teams. The default
choice -- do nothing, keep the current workflow -- is always available, always zero cost
to maintain. Pre-declare the threat score here. Return to revise at Section 4.

[C-03 COMMAND]: RECORD the DO-NOTHING DEFAULT COMPETITOR's threat score below. HIGH is
the default. If non-HIGH at pre-evidence stage, append (PROVISIONAL) and state a specific
measurable reason. Return to this table at Section 4 after evidence is gathered.

| Pre-evidence dimension       | Assessment               | Marker                  |
|------------------------------|--------------------------|-------------------------|
| Threat score                 | HIGH                     | --                      |
| Competitor mechanism         | Zero-effort persistence  | --                      |
| Primary adoption barrier     |                          | PROVISIONAL if non-HIGH |
| Expected switching resistance| High                     | PROVISIONAL if non-HIGH |

---

## [FAIL-FIRST DECLARATION] -- THE DO-NOTHING DEFAULT COMPETITOR

THE DO-NOTHING DEFAULT COMPETITOR IS THE FEATURE'S PRIMARY COMPETITOR. MAP ITS
FAILURE MODES FIRST. AUTHOR NO DEFEAT CONDITION WITHOUT A TRACEABLE FAILURE MODE.

DO-NOTHING DEFAULT COMPETITOR FAIL-FIRST RULE [A-31]: The DO-NOTHING DEFAULT COMPETITOR
fails at specific, measurable thresholds. Document those failure modes at Section 1 before
writing any defeat condition at Section 5. This ordering is the structural constraint. No
exception.

Bridge artifacts required before defeat conditions are valid:
- **Q3 (DO-NOTHING DEFAULT ACTOR BRIDGE)** (closes C-05 -> R-02): each FM-[N] attributed
  to the role experiencing it
- **Q4 (DO-NOTHING DEFAULT TRIGGER BRIDGE)** (closes C-05 -> C-04): each FM-[N] mapped to
  its triggering condition and measurable threshold

---

## SECTION 1 -- DO-NOTHING DEFAULT COMPETITOR FM INVENTORY

[C-05 COMMAND]: NAME EVERY SPECIFIC FAILURE MODE WHERE THE DO-NOTHING DEFAULT
COMPETITOR BREAKS. REJECT GENERIC DESCRIPTIONS -- "MANUAL" OR "SLOW" ALONE FAILS.
"CSV EXPORT SILENTLY TRUNCATES ROWS ABOVE 65,536 -- NO ERROR MESSAGE" PASSES.
MINIMUM 2 ROWS REQUIRED.

> **DO-NOTHING DEFAULT COMPETITOR PRIMARY KEY RULE [A-16]**: FM-[N] IS THE PRIMARY KEY
> FOR ALL FAILURE MODES IN THIS ANALYSIS. ASSIGN EVERY FM-[N] IDENTIFIER IN THIS TABLE
> BEFORE AUTHORING Q3, Q4, OR SECTION 5. EVERY DOWNSTREAM CITATION MUST TRACE HERE.
> MISSING OR DUPLICATE KEYS INVALIDATE THE REFERENTIAL CHAIN.

| FM-[N] | FAILURE DESCRIPTION (e.g., CSV EXPORT TRUNCATES AT 65,536 ROWS -- NO ERROR) | ACTOR / ROLE (e.g., DATA-OPS TEAM) | TRIGGER (e.g., FILE > 10MB) | FREQUENCY (e.g., 2x/SPRINT) |
|--------|---------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-01  |                                                                           |                                    |                             |                             |
| FM-02  |                                                                           |                                    |                             |                             |

---

## Q3 (DO-NOTHING DEFAULT ACTOR BRIDGE) -- CLOSES C-05 -> R-02

[C-05 BRIDGE ARTIFACT Q3 COMMAND]: COMPLETE Q3 BEFORE ADVANCING TO THE GATE. MAP
EACH FM-[N] TO THE SPECIFIC ROLE EXPERIENCING THAT FAILURE. "ENGINEERING" FAILS.
"DATA-OPS TEAM MANAGING WEEKLY PIPELINE EXPORTS" PASSES.

| FM-[N] | ROLE EXPERIENCING THE FAILURE (e.g., DATA-OPS TEAM) | ROLE-LEVEL CONSEQUENCE (e.g., 2 HRS REMEDIATION/CYCLE) |
|--------|-----------------------------------------------------|--------------------------------------------------------|
| FM-01  |                                                     |                                                        |
| FM-02  |                                                     |                                                        |

---

## Q4 (DO-NOTHING DEFAULT TRIGGER BRIDGE) -- CLOSES C-05 -> C-04

[C-05 BRIDGE ARTIFACT Q4 COMMAND]: COMPLETE Q4 BEFORE ADVANCING TO THE GATE. MAP
EACH FM-[N] TO ITS TRIGGERING CONDITION AND MEASURABLE THRESHOLD. THE THRESHOLD HERE
BECOMES THE BASIS FOR DEFEAT CONDITIONS AT SECTION 5.

| FM-[N] | TRIGGERING CONDITION (e.g., PIPELINE INGESTS FILE > 10MB) | MEASURABLE THRESHOLD (e.g., >10MB, >3 FAILURES/WEEK) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-01  |                                                           |                                                      |
| FM-02  |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 AND Q4 DO-NOTHING DEFAULT BRIDGES BEEN POPULATED?

| BRIDGE ARTIFACT                                                | POPULATED? (Y / N) |
|----------------------------------------------------------------|--------------------|
| Q3 (DO-NOTHING DEFAULT ACTOR BRIDGE) -- closes C-05 -> R-02   |                    |
| Q4 (DO-NOTHING DEFAULT TRIGGER BRIDGE) -- closes C-05 -> C-04 |                    |

**[BRIDGE COMPLETION COMMAND]**: DO NOT ADVANCE TO SECTION 2 UNLESS BOTH ROWS SHOW Y.
IF EITHER SHOWS N: RETURN TO THE CORRESPONDING BRIDGE SECTION ABOVE AND COMPLETE THE
MISSING ROWS BEFORE PROCEEDING.

---

## SECTION 2 -- DO-NOTHING DEFAULT COMPETITOR WORKAROUND PROFILE

[C-01 COMMAND]: NAME THE SPECIFIC TOOL, FILE TYPE, OR PROCEDURE CONSTITUTING THE
DO-NOTHING DEFAULT COMPETITOR. NOT "A MANUAL PROCESS" -- NAME IT. NAME THE ROLE
PERFORMING IT. QUANTIFY THE ONGOING COST WITH A NUMBER AND A UNIT (e.g., 2 HOURS/WEEK).

| WORKAROUND NAME (SPECIFIC TOOL / FILE TYPE / PROCEDURE) | ROLE PERFORMING IT | ONGOING COST (e.g., 2 HOURS/WEEK) | IN ACTIVE USE SINCE (e.g., 18 MONTHS) |
|---------------------------------------------------------|--------------------|-----------------------------------|---------------------------------------|
|                                                         |                    |                                   |                                       |

---

## SECTION 3 -- DO-NOTHING DEFAULT COMPETITOR SWITCHING COST ANALYSIS

[C-02 COMMAND]: IDENTIFY AT LEAST TWO SWITCHING COST CATEGORIES. QUANTIFY EACH WITH
A NUMBER AND A UNIT -- "SIGNIFICANT" WITHOUT A NUMBER FAILS. NAME THE ROLE BEARING EACH
COST. EXAMPLE: "8 HOURS/WEEK x 6-WEEK RAMP = 48 HOURS PER ENGINEER."

| COST CATEGORY       | DESCRIPTION | ESTIMATE (e.g., 3 DAYS) | ROLE BEARING IT (e.g., DATA-OPS TEAM) |
|---------------------|-------------|-------------------------|---------------------------------------|
| MIGRATION EFFORT    |             |                         |                                       |
| TRAINING OVERHEAD   |             |                         |                                       |
| PROCESS DISRUPTION  |             |                         |                                       |
| IN-FLIGHT WORK RISK |             |                         |                                       |

---

## SECTION 4 -- DO-NOTHING DEFAULT COMPETITOR THREAT ASSESSMENT

[C-03 COMMAND]: RETURN TO SECTION 0 NOW. REVISE ANY PROVISIONAL ENTRIES IN THE
SECTION 0 PRE-ASSESSMENT TABLE BASED ON EVIDENCE GATHERED IN SECTIONS 2-3. UPDATE
THE THREAT SCORE AT SECTION 0 IF WARRANTED. THEN RECORD THE CONFIRMED SCORE BELOW.

| ASSESSMENT DIMENSION        | CONFIRMED SCORE | EVIDENCE BASIS |
|-----------------------------|-----------------|----------------|
| THREAT SCORE                | HIGH            |                |
| PRIMARY INERTIA DRIVER      |                 |                |
| SWITCHING COST MAGNITUDE    |                 |                |
| WORKAROUND STABILITY        |                 |                |

---

## SECTION 5 -- DO-NOTHING DEFAULT COMPETITOR DEFEAT CONDITIONS

[C-04 COMMAND]: DERIVE AT LEAST TWO SPECIFIC, FALSIFIABLE DEFEAT CONDITIONS FROM THE
TRIGGER THRESHOLDS IN Q4. EACH MUST CARRY A MEASURABLE THRESHOLD WITH A UNIT. TWO
STRUCTURALLY DISTINCT THRESHOLD TYPES REQUIRED (e.g., VOLUME >10MB AND FREQUENCY
>3 FAILURES/WEEK).

> **DO-NOTHING DEFAULT COMPETITOR CITATION RULE [A-19]**: EVERY DC-[N] IN THIS TABLE
> MUST CITE THE ORIGINATING FM-[N] FROM SECTION 1. EVERY FM-[N] IN SECTION 1 MUST
> APPEAR IN AT LEAST ONE DC-[N] ROW HERE. BIDIRECTIONAL INTEGRITY REQUIRED. VERIFY
> BEFORE FILLING EACH ROW.

| DC-[N] | DEFEAT CONDITION (SPECIFIC, FALSIFIABLE) | FM-[N] | THRESHOLD (e.g., >10MB, >3 FAILURES/WEEK) | TEAM SEGMENT |
|--------|------------------------------------------|--------|-------------------------------------------|--------------|
| DC-01  |                                          | FM-01  |                                           |              |
| DC-02  |                                          | FM-02  |                                           |              |

---

## SECTION 6 -- DO-NOTHING DEFAULT COMPETITOR COMPLETENESS CHECKLIST

| # | CRITERION | SATISFIED? (Y / N) |
|---|-----------|---------------------|
| C-01: | WORKAROUND NAMED SPECIFICALLY (TOOL/PROCEDURE/FILE TYPE) WITH ROLE AND ONGOING COST (NUMBER + UNIT) | |
| C-02: | AT LEAST TWO SWITCHING COST CATEGORIES QUANTIFIED WITH NUMBER + UNIT PER NAMED ROLE | |
| C-03: | THREAT SCORE PRE-DECLARED AT SECTION 0 (PROVISIONAL IF NON-HIGH); CONFIRMED/REVISED AT SECTION 4 | |
| C-04: | AT LEAST TWO DEFEAT CONDITIONS, FALSIFIABLE, FM-[N] CITED, MEASURABLE THRESHOLD EACH | |
| C-05: | FM INVENTORY COMPLETE WITH FM-[N] KEYS; Q3 AND Q4 BRIDGE ARTIFACTS FULLY POPULATED | |
```

---

## Structural Criterion Map

The table below shows which scaffold element in each variation satisfies each new criterion.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-45** (artifact IDs in gate heading) | `BOTH Q3 AND Q4 STATUS QUO COMPETITOR BRIDGES` | `BOTH Q3 AND Q4 INERTIA DEFAULT COMPETITOR BRIDGES` | `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` | `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` in combined heading | `BOTH Q3 AND Q4 DO-NOTHING DEFAULT BRIDGES` |
| **C-46** (compound threading vocabulary) | `STATUS QUO COMPETITOR` in FAIL-FIRST heading, Section 1 heading, A-16/A-19/A-31 labels, gate class | `INERTIA DEFAULT COMPETITOR` throughout | `INERTIA LOCK COMPETITOR` throughout | `INCUMBENT DEFAULT COMPETITOR` throughout | `DO-NOTHING DEFAULT COMPETITOR` throughout |
| **C-47** (Stage 0 PROVISIONAL pre-declaration) | Section 0 table: HIGH pre-declared; PROVISIONAL marker for non-HIGH rows | Stage 0 table: HIGH pre-declared; PROVISIONAL marker for non-HIGH rows | Section 0 table: HIGH pre-declared; PROVISIONAL marker for non-HIGH rows | Stage 0 table: HIGH pre-declared; PROVISIONAL marker for non-HIGH rows | Section 0 table: HIGH pre-declared; PROVISIONAL marker for non-HIGH rows |
| **C-48** (revision directive at evidence stage) | `[C-03 COMMAND]: REVISIT SECTION 0 NOW` at Section 4 | `[C-03 COMMAND]: REVISIT STAGE 0 NOW` at Stage 5A | `[C-03 COMMAND]: RETURN TO SECTION 0. REVISE ANY PROVISIONAL ENTRIES` at Section 4 | `[C-03 COMMAND]: REVISIT STAGE 0 NOW` at Stage 5A | `[C-03 COMMAND]: RETURN TO SECTION 0 NOW. REVISE ANY PROVISIONAL ENTRIES` at Section 4 |

### C-45 form comparison

| V | Gate heading interrogative | C-43 count | C-45 artifact IDs | Artifact class |
|---|---------------------------|------------|---------------------|----------------|
| V-01 | `BOTH Q3 AND Q4 STATUS QUO COMPETITOR BRIDGES BEEN POPULATED?` | BOTH | Q3, Q4 before class noun | STATUS QUO COMPETITOR BRIDGES |
| V-02 | `BOTH Q3 AND Q4 INERTIA DEFAULT COMPETITOR BRIDGES BEEN POPULATED?` | BOTH | Q3, Q4 before class noun | INERTIA DEFAULT COMPETITOR BRIDGES |
| V-03 | `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE) BEEN POPULATED?` | BOTH | Q3, Q4 each with parenthetical class | distributed per artifact |
| V-04 | `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE) BEEN POPULATED?` in combined heading | BOTH | Q3, Q4 each with parenthetical class | distributed per artifact, inside combined heading |
| V-05 | `BOTH Q3 AND Q4 DO-NOTHING DEFAULT BRIDGES BEEN POPULATED?` | BOTH | Q3, Q4 before class noun | DO-NOTHING DEFAULT BRIDGES (axis vocabulary reused) |

### C-46 compound term breakdown

| V | Compound term | Domain axis | Structural role |
|---|--------------|-------------|-----------------|
| V-01 | STATUS QUO COMPETITOR | STATUS QUO | COMPETITOR |
| V-02 | INERTIA DEFAULT COMPETITOR | INERTIA DEFAULT | COMPETITOR |
| V-03 | INERTIA LOCK COMPETITOR | INERTIA LOCK | COMPETITOR |
| V-04 | INCUMBENT DEFAULT COMPETITOR | INCUMBENT DEFAULT | COMPETITOR |
| V-05 | DO-NOTHING DEFAULT COMPETITOR | DO-NOTHING DEFAULT | COMPETITOR |

### C-47 + C-48 staged-commitment pair

| V | Stage 0 element | Revision directive location | Directive text |
|---|-----------------|-----------------------------|----------------|
| V-01 | Section 0 pre-assessment table with PROVISIONAL marker column | Section 4 | `REVISIT SECTION 0 NOW...revise any PROVISIONAL entries` |
| V-02 | Stage 0 pre-assessment table with PROVISIONAL marker column | Stage 5A | `REVISIT STAGE 0 NOW...revise any PROVISIONAL entries` |
| V-03 | Section 0 COMMAND-register pre-assessment table | Section 4 | `RETURN TO SECTION 0. REVISE ANY PROVISIONAL ENTRIES IN THE SECTION 0 PRE-ASSESSMENT TABLE` |
| V-04 | Stage 0 pre-assessment table with PROVISIONAL marker column | Stage 5A | `REVISIT STAGE 0 NOW...revise any PROVISIONAL entries` |
| V-05 | Section 0 COMMAND-register pre-assessment table | Section 4 | `RETURN TO SECTION 0 NOW. REVISE ANY PROVISIONAL ENTRIES` |

---

```json
{"round": "R14", "rubric": "C-series v14", "new_criteria": ["C-45", "C-46", "C-47", "C-48"], "predicted_scores": {"V-01": "40/40", "V-02": "40/40", "V-03": "40/40", "V-04": "40/40", "V-05": "40/40"}, "c45_forms": ["Q3 AND Q4 before artifact-class noun (V-01/V-02/V-05)", "Q3/Q4 with parenthetical class labels per artifact (V-03/V-04)", "artifact class reuses C-46 axis vocabulary (V-05)"], "c46_terms": ["STATUS QUO COMPETITOR (V-01)", "INERTIA DEFAULT COMPETITOR (V-02)", "INERTIA LOCK COMPETITOR (V-03)", "INCUMBENT DEFAULT COMPETITOR (V-04)", "DO-NOTHING DEFAULT COMPETITOR (V-05)"], "c47_c48_pattern": "Stage 0/Section 0 pre-declares HIGH with PROVISIONAL mechanism; evidence stage contains explicit named directive to revisit Stage 0 and revise PROVISIONAL", "notable": "V-05 reuses C-46 axis vocabulary (DO-NOTHING DEFAULT) as the artifact-class noun in the C-45 gate heading (DO-NOTHING DEFAULT BRIDGES), achieving cross-criterion vocabulary coherence at the gate heading level"}
```
