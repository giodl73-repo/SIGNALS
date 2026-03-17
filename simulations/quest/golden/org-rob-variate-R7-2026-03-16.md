---
skill: quest-variate
skill_target: org-rob
round: 7
date: 2026-03-16
rubric_version: 6
---

# Variate R7 — org-rob

5 complete prompt body variations for the `org-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Context Entering R7

Under rubric v6 (max 114), R6 scores were:

| Variation | v6 Score | C-20 |
|-----------|----------|------|
| V-03 | 114 | ++ (VIOLATION-01..08) |
| V-05 | 112 | o (no violation taxonomy) |
| V-04 | 110 | o |
| V-01 | 108 | o |
| V-02 | 107 | o |

R7 goal: every variation earns C-20 ++ and reaches 114 via at least one new
structural path. V-01 takes the minimal route (add VIOLATION REGISTRY to V-05 R6 base).
V-02 and V-03 explore whether 114 survives role-sequence and phrasing-register variation.
V-04 and V-05 add inertia framing as a structural first-class element.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (VIOLATION REGISTRY appendix on V-05 R6 base) | V-01 |
| Role sequence (teams-first on V-03 R6 prohibition base) | V-02 |
| Phrasing register (explanatory violation descriptions vs bare declarations) | V-03 |
| Inertia framing + violation taxonomy | V-04 |
| Full integration: teams-first + inertia + prohibition | V-05 |

---

## V-01 — Output Format: VIOLATION Registry Appended to V-05 R6 Base

**Axis**: Output format
**Hypothesis**: V-05 R6 achieves all of C-09–C-19 via structural mechanisms but earns
C-20=o because no violation taxonomy exists. Adding a VIOLATION REGISTRY section before
the stage templates — mapping every existing structural rule to a named VIOLATION-NN
identifier — earns C-20++ without changing any stage template or role mechanics. The
registry is a pure output-format addition with no side effects on C-09–C-19 mechanisms.
Expected score: 114.

---

You are running `/org-rob`. Execute a full Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → spire

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

---

## VIOLATION REGISTRY

Every structural rule in this schema has a corresponding named violation type.
Compliance is mechanistic: a reviewer can ask "was VIOLATION-NN committed?" without
prose interpretation.

| ID | Violation Name | Anti-Pattern |
|----|---------------|--------------|
| VIOLATION-01 | MISSING ORIENTATION FRAME | A `ROLE:` block that does not include `Frame: orientation.frame = "{value}"` — the loaded role's orientation frame is unstated and cannot be verified |
| VIOLATION-02 | MALFORMED FINDING ROW | A finding row where `Via:` is NOT the second column (position: after `ID`, before the finding text) — lens anchor is not structurally enforced |
| VIOLATION-03 | BLANK LENS CITATION | A finding row where the `Via:` cell is blank or omitted — the concern cannot be traced to a specific lens item |
| VIOLATION-04 | PROSE VERDICT | A stage verdict expressed as prose text instead of a Verdict Table row — omission of rationale or finding-ID citation is structurally possible |
| VIOLATION-05 | UNSIGNED EXIT CONDITIONS | An EXIT block that uses generic readiness language without citing specific finding IDs from that stage — handoff is not independently checkable |
| VIOLATION-06 | BURIED GO/NO-GO | A tpm go/no-go recommendation embedded in paragraph prose rather than a labeled top-level block — the decision is not immediately locatable |
| VIOLATION-07 | ABSENT RESIDUAL SECTION | A synthesis output that omits the Residual Open Items section — escalation gaps are invisible even when all items are resolved |
| VIOLATION-08 | SINGLE-STAGE THEME | A cross-cutting concern named only inside one stage's findings — any concern surfaced in 2+ stages must be elevated to the document-level Cross-Cutting Themes table |

Any output exhibiting a named violation fails the criterion the violation governs.

---

## SETUP

1. Initialize the **Write-ahead Ledger** before Stage 1 runs:

```
## Finding Ledger

| Ledger-Row | Stage | ID   | Via                | Finding (short)    | Severity | Resolved By | Resolution |
|------------|-------|------|--------------------|--------------------|----------|-------------|------------|
[no rows yet — stages append as they run]
```

2. Read `org.yaml` — identify the role assigned to each stage.
3. Read `.craft/roles/` — extract `orientation.frame` and lens items for each assigned role.
4. Fallback if absent: leadership=VP Product, teams=Team Leads, pm=Senior PM,
   tpm=TPM Lead, arch-board=Principal Architect, spire=Chief of Staff.

---

## STAGE TEMPLATE (applies to all stages)

```
## PHASE GATE: {stage-name}

ROLE: {name from .craft/roles/}
Frame: orientation.frame = "{extracted value — must match .craft/roles/ field}"
[Omitting Frame: is VIOLATION-01]

### ENTRY CONDITIONS
1. {named condition — what must be true before this stage proceeds}
2. {second named condition}
[Stage 1 writes "First stage — no upstream entry conditions."]

### Findings

| ID   | Via                   | Finding                          | Severity | Owner  | Ledger-Row | Resolution Path          |
|------|-----------------------|----------------------------------|----------|--------|------------|--------------------------|
| F-01 | {specific lens item}  | {specific concern, role-grounded}| HIGH     | {role} | L-{N}      | {concrete action}        |
| F-02 | {specific lens item}  | {specific concern, role-grounded}| MED      | {role} | L-{N}      | {concrete action}        |
[minimum 2 rows; Via: MUST be second column — VIOLATION-02; blank Via: is VIOLATION-03]
[append each finding row to the Write-ahead Ledger immediately]

### EXIT CONDITIONS
Escalates to {next-stage}: {finding IDs being forwarded}
Certifies resolved: {any prior finding IDs this stage closes, or "none"}
[Generic language without finding IDs is VIOLATION-05]

### Stage Verdict

| Stage        | Status                                              | Finding-IDs    | Rationale                      |
|--------------|-----------------------------------------------------|----------------|--------------------------------|
| {stage-name} | APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {F-NN, F-NN} | {one sentence, role-specific} |
[Prose verdict is VIOLATION-04 — this table row IS the verdict]

### Blocker Check
Does any finding in this stage block a downstream stage?
YES → BLOCKS {downstream-stage}: {finding-ID} — {reason downstream cannot proceed}
NO  → No downstream blocker identified.
```

---

## TPM STAGE — ADDITIONAL REQUIRED SECTIONS

After Findings, before Exit Conditions:

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation              | Source Finding |
|------|-----------------|----------|------------|-------------------------|----------------|
| R-01 | {specific risk} | HIGH     | HIGH       | {concrete mitigation}   | {F-NN or stage/F-NN} |
| R-02 | {specific risk} | MED      | MED        | {concrete mitigation}   | {F-NN} |
| R-03 | {specific risk} | LOW      | LOW        | {concrete mitigation}   | {F-NN} |
[minimum 3 entries; at least 1 HIGH]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Primary rationale: {cite R-NN or F-NN}
Conditions (if GO WITH CONDITIONS): {what must be resolved before full GO}
[Go/no-go buried in prose is VIOLATION-06]
```

---

## SPIRE STAGE — ADDITIONAL REQUIRED SECTION

```
### Mission Alignment

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| {named mission}    | {program name} | {topic}        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named — "strategic priorities" fails this criterion]
```

---

## SYNTHESIS (--stage all only, written after all stages complete)

```
## Synthesis

### Inter-Stage Blockers

| Upstream Stage | Finding-ID | Downstream Stage | Impact                    |
|----------------|------------|------------------|---------------------------|
| {stage}        | {F-NN}     | {stage}          | {why downstream is blocked} |
[or "No inter-stage blockers identified." if none]

### Dual-Direction Check

| Ledger-Row | Sent By  | Finding-ID | Received By | Acknowledged As | Note   |
|------------|----------|------------|-------------|-----------------|--------|
| L-{N}      | {stage}  | {F-NN}     | {stage}     | {F-NN or empty} | {note} |
[Rows where Acknowledged As = empty are RESIDUAL]

### Residual Open Items

| Ledger-Row | Origin Stage | Finding-ID | Intended Receiver | Gap  |
|------------|--------------|------------|-------------------|------|
[List all rows where Acknowledged As = empty]
[If empty: "No residual open items — all escalations acknowledged." MUST be present — VIOLATION-07 if section absent]

### Cross-Cutting Themes

| Theme         | Via Value (shared)  | Stages             | Severity Pattern  | Recommended Action |
|---------------|---------------------|--------------------|-------------------|--------------------|
| {theme name}  | {shared lens item}  | {stage, stage, ...}| escalating/stable | {action}           |
[Detect by filtering Ledger by Via value — any Via: item in findings from 2+ distinct stages is a cross-cutting theme]
[A concern named only inside one stage is VIOLATION-08 — it must be elevated to this table]
[or "No cross-cutting themes identified." if no Via: value recurs across 2+ stages]

### Verdict Registry

| Stage      | Status                 | Finding-IDs  | Rationale      |
|------------|------------------------|--------------|----------------|
| leadership | {status}               | {IDs}        | {one sentence} |
| teams      | {status}               | {IDs}        | {one sentence} |
| pm         | {status}               | {IDs}        | {one sentence} |
| tpm        | {status + go/no-go}    | {IDs}        | {one sentence} |
| arch-board | {status}               | {IDs}        | {one sentence} |
| spire      | {status}               | {IDs}        | {one sentence} |
```

**OUTPUT RULES:** Each stage is its own labeled `## PHASE GATE:` section. Stages are
never merged. Every VIOLATION in the VIOLATION REGISTRY is an independent compliance
check applied to this output.

---

## V-02 — Role Sequence: Teams-First on V-03 R6 Prohibition Base

**Axis**: Role sequence
**Hypothesis**: Running teams before leadership lets implementation-level concerns
surface without being filtered through executive framing. PM then aligns on adoption
gaps discovered by teams before architecture review shapes constraints. Leadership
provides strategic framing immediately before the tpm risk synthesis, which now has
maximum prior context. This tests whether the VIOLATION-NN prohibition machinery
(inherited intact from V-03 R6) still produces strong C-06 cross-stage coherence
and C-09 blocker detection when the information flow runs ground-up rather than
top-down. Expected score: 114.

---

You are running `/org-rob`. Execute a full Review of Business for the given topic.

**STAGE ORDER (TEAMS-FIRST):** teams → pm → arch-board → leadership → tpm → spire

If `--stage [name]` is given, run only that stage.
If `--stage all` is given, run full sequence in the order above.
If `--scope [group]` is given, restrict org.yaml roles to that division or tribe.

---

## VIOLATION REGISTRY

| ID | Violation Name | Anti-Pattern |
|----|---------------|--------------|
| VIOLATION-01 | INCOMPLETE ROLE BLOCK | A `ROLE:` block without `Frame: orientation.frame = "{value}"` — orientation is unstated |
| VIOLATION-02 | MALFORMED FINDING ROW | `Via:` is NOT the second column in a finding row — lens anchor is not structurally enforced |
| VIOLATION-03 | BLANK VIA CELL | A finding row with a blank `Via:` field — concern cannot be traced to a lens item |
| VIOLATION-04 | PROSE VERDICT | Stage verdict expressed as prose instead of a Verdict Table row |
| VIOLATION-05 | UNSIGNED EXIT | EXIT block with generic language and no finding IDs cited |
| VIOLATION-06 | BURIED GO/NO-GO | tpm go/no-go embedded in prose paragraph, not a labeled top-level block |
| VIOLATION-07 | ABSENT RESIDUAL SECTION | Synthesis without a Residual Open Items section |
| VIOLATION-08 | SINGLE-STAGE THEME | Cross-cutting concern named only inside one stage, not elevated to document-level themes table |

---

## SETUP

1. Initialize the **Write-ahead Ledger** (columns: Ledger-Row, Stage, ID, Via, Finding (short), Severity, Resolved By, Resolution) before teams stage runs.
2. Read `org.yaml`. Read `.craft/roles/` for each stage's role. Fallback: teams=Team Leads, pm=Senior PM, arch-board=Principal Architect, leadership=VP Product, tpm=TPM Lead, spire=Chief of Staff.

**SEQUENCE NOTE:** Because teams runs before leadership, the risk baseline is not yet
established when teams and pm review. When tpm runs, it should explicitly note which
team-level findings escalate to risks and which leadership findings confirm or
contradict the team-level picture.

---

## STAGE TEMPLATE (applies to all stages)

```
## PHASE GATE: {stage-name}

ROLE: {name from .craft/roles/}
Frame: orientation.frame = "{extracted value — must match .craft/roles/ field}"
[VIOLATION-01 if Frame: absent]

### ENTRY CONDITIONS
1. {named condition}
2. {second named condition}
[First stage (teams) writes "First stage — no upstream entry conditions."]

### Findings

| ID   | Via                  | Finding                           | Severity | Owner  | Ledger-Row | Resolution Path          |
|------|----------------------|-----------------------------------|----------|--------|------------|--------------------------|
| F-01 | {specific lens item} | {concern grounded in role lens}   | HIGH     | {role} | L-{N}      | {concrete action}        |
| F-02 | {specific lens item} | {concern grounded in role lens}   | MED      | {role} | L-{N}      | {concrete action}        |
[minimum 2 rows; VIOLATION-02 if Via: not second; VIOLATION-03 if Via: blank]
[append each row to Write-ahead Ledger immediately]

### EXIT CONDITIONS
Escalates to {next-stage}: {finding IDs}
Certifies resolved: {closed finding IDs, or "none"}
[VIOLATION-05 if no finding IDs cited]

### Stage Verdict

| Stage        | Status                                              | Finding-IDs      | Rationale                       |
|--------------|-----------------------------------------------------|------------------|---------------------------------|
| {stage-name} | APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {F-NN, ...} | {one sentence, role-specific}  |
[VIOLATION-04 if prose]

### Blocker Check
YES → BLOCKS {downstream-stage}: {finding-ID} — {reason}
NO  → No downstream blocker identified.
```

---

## TPM STAGE — ADDITIONAL REQUIRED SECTIONS

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            | Source Finding |
|------|-----------------|----------|------------|-----------------------|----------------|
| R-01 | {specific risk} | HIGH     | HIGH       | {concrete mitigation} | {stage/F-NN}   |
| R-02 | {specific risk} | MED      | MED        | {concrete mitigation} | {stage/F-NN}   |
| R-03 | {specific risk} | LOW      | LOW        | {concrete mitigation} | {stage/F-NN}   |
[minimum 3 rows; at least 1 HIGH; Source Finding traces to upstream stage findings]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Primary rationale: {cite R-NN or stage/F-NN}
Conditions (if applicable): {what must be resolved}
[VIOLATION-06 if this block appears in paragraph prose instead of here]
```

---

## SPIRE STAGE — ADDITIONAL REQUIRED SECTION

```
### Mission Alignment

| S-Office Mission | Program        | Artifact/Topic | Alignment               |
|------------------|----------------|----------------|-------------------------|
| {named mission}  | {program name} | {topic}        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named — "company goals" or "strategic priorities" fails]
```

---

## SYNTHESIS (--stage all only)

```
## Synthesis

### Inter-Stage Blockers

| Upstream Stage | Finding-ID | Downstream Stage | Impact               |
|----------------|------------|------------------|----------------------|
| {stage}        | {F-NN}     | {stage}          | {blocking reason}    |
[or "No inter-stage blockers identified." if none]

### Dual-Direction Check

| Ledger-Row | Sent By | Finding-ID | Received By | Acknowledged As | Note   |
|------------|---------|------------|-------------|-----------------|--------|
| L-{N}      | {stage} | {F-NN}     | {stage}     | {F-NN or empty} | {note} |

### Residual Open Items

| Ledger-Row | Origin Stage | Finding-ID | Intended Receiver | Gap  |
|------------|--------------|------------|-------------------|------|
[Rows where Acknowledged As = empty; "No residual open items." if none — VIOLATION-07 if section absent]

### Cross-Cutting Themes

| Theme        | Via Value (shared)  | Stages             | Severity Pattern  | Recommended Action |
|--------------|---------------------|--------------------|-------------------|--------------------|
| {theme name} | {shared lens item}  | {stage, stage, ...}| escalating/stable | {action}           |
[Filter Ledger by Via value — any item appearing from 2+ stages is a cross-cutting theme]
[VIOLATION-08 if a recurring concern is named only inside one stage's findings]

### Verdict Registry

| Stage      | Status              | Finding-IDs | Rationale      |
|------------|---------------------|-------------|----------------|
| teams      | {status}            | {IDs}       | {one sentence} |
| pm         | {status}            | {IDs}       | {one sentence} |
| arch-board | {status}            | {IDs}       | {one sentence} |
| leadership | {status}            | {IDs}       | {one sentence} |
| tpm        | {status + go/no-go} | {IDs}       | {one sentence} |
| spire      | {status}            | {IDs}       | {one sentence} |
```

**OUTPUT RULE:** Each stage is its own `## PHASE GATE:` section in teams-first order.
Stages are never merged or reordered.

---

## V-03 — Phrasing Register: Explanatory Violation Descriptions

**Axis**: Phrasing register
**Hypothesis**: V-03 R6 achieves 114 with terse VIOLATION declarations ("VIOLATION-01:
ROLE: block without Frame: is INCOMPLETE"). Enriching each violation with an explanatory
sentence — why the anti-pattern undermines the review, not just what it is — preserves
all C-20 compliance (violation IDs are still distinct and enumerated) while making the
schema self-documenting. The model reading richer violation context understands the
enforcement intent and is less likely to produce borderline-compliant output.
Expected score: 114.

---

You are running `/org-rob`. Execute a full Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → spire

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

---

## VIOLATION REGISTRY

Every structural rule in this schema has a named violation. Violations make compliance
independently checkable without prose interpretation.

**VIOLATION-01 — MISSING ORIENTATION FRAME**
A `ROLE:` block that does not include `Frame: orientation.frame = "{value}"` from the
loaded `.craft/roles/` file is INCOMPLETE. Without the orientation frame explicitly
stated, a reader cannot verify which lens was loaded for this stage. A stage that
produces role-appropriate findings but never states the frame is unauditable — the
correct orientation cannot be confirmed from the output alone.

**VIOLATION-02 — MALFORMED FINDING ROW**
A finding row where `Via:` is NOT the second column (position: after `ID`, before
the finding text) is MALFORMED. The structural position of `Via:` enforces 100%
lens coverage by making a blank cell visible before the finding can be read
left-to-right. Moving `Via:` to column 3 or later defeats this enforcement.

**VIOLATION-03 — BLANK LENS CITATION**
A finding row where the `Via:` cell is blank or omitted is INCOMPLETE. Every
finding must trace to a specific lens item from the loaded role file. A finding
that could have been written by any role — regardless of how plausible it sounds —
does not satisfy the role-loaded perspective criterion without a lens citation.

**VIOLATION-04 — PROSE VERDICT**
A stage verdict expressed as a prose block (`APPROVED\nRationale: ...`) rather than
a named-column Verdict Table row is PROHIBITED. Prose verdicts allow silent omission
of rationale or finding-ID citation. The table row structure makes both structurally
required: a blank column is visible where a filled cell should be.

**VIOLATION-05 — UNSIGNED EXIT CONDITIONS**
An EXIT block that uses generic readiness language ("stage complete", "findings
documented") without citing specific finding IDs from that stage is INVALID. Exit
conditions that do not name finding IDs cannot be independently verified; a reader
cannot trace what was certified resolved before the handoff.

**VIOLATION-06 — BURIED GO/NO-GO**
A tpm go/no-go decision embedded within a paragraph of prose rather than expressed
as a labeled top-level block is PROHIBITED. A go/no-go decision that requires
reading surrounding context to locate is not a decision — it is an opinion. The
block must be immediately locatable as a labeled element.

**VIOLATION-07 — ABSENT RESIDUAL SECTION**
A synthesis output that omits the Residual Open Items section is MISSING a required
structural element, even when all escalations have been acknowledged. An empty
Residual section ("No residual open items.") is a stronger signal than an absent
one: it certifies completeness rather than leaving it ambiguous.

**VIOLATION-08 — SINGLE-STAGE THEME BURIAL**
A cross-cutting concern named only inside one stage's findings is NOT ELEVATED. When
the same concern surfaces in findings from 2+ distinct stages, the repetition is
itself meaningful — the concern is more serious than any single stage's perspective
can express. Such concerns must appear in the document-level Cross-Cutting Themes
table, not only in individual stage findings.

---

## SETUP

1. Initialize the **Write-ahead Ledger** before Stage 1:

```
## Finding Ledger

| Ledger-Row | Stage | ID   | Via                | Finding (short)    | Severity | Resolved By | Resolution |
|------------|-------|------|--------------------|--------------------|----------|-------------|------------|
[stages append rows as they run]
```

2. Read `org.yaml`. Read `.craft/roles/` for each stage. Extract `orientation.frame` and
   lens items. Fallback: leadership=VP Product, teams=Team Leads, pm=Senior PM,
   tpm=TPM Lead, arch-board=Principal Architect, spire=Chief of Staff.

---

## STAGE TEMPLATE

```
## PHASE GATE: {stage-name}

ROLE: {name from .craft/roles/}
Frame: orientation.frame = "{extracted value}"
[Absent Frame: is VIOLATION-01 — orientation unverifiable]

### ENTRY CONDITIONS
1. {named condition — what prior stage must have certified}
2. {second named condition}
[Stage 1: "First stage — no upstream entry conditions."]

### Findings

| ID   | Via                  | Finding                           | Severity | Owner  | Ledger-Row | Resolution Path          |
|------|----------------------|-----------------------------------|----------|--------|------------|--------------------------|
| F-01 | {specific lens item} | {concern from this role's lens}   | HIGH     | {role} | L-{N}      | {concrete action}        |
| F-02 | {specific lens item} | {concern from this role's lens}   | MED      | {role} | L-{N}      | {concrete action}        |
[minimum 2 rows]
[Via: must be SECOND column — VIOLATION-02 if not; blank Via: is VIOLATION-03]
[append each row to Write-ahead Ledger immediately]

### EXIT CONDITIONS
Escalates to {next-stage}: {finding IDs forwarded}
Certifies resolved: {finding IDs closed at this stage, or "none"}
[VIOLATION-05 if no finding IDs cited]

### Stage Verdict

| Stage        | Status                                              | Finding-IDs      | Rationale                      |
|--------------|-----------------------------------------------------|------------------|--------------------------------|
| {stage-name} | APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {F-NN, ...} | {one sentence, role-specific} |
[VIOLATION-04 if this appears as prose instead of a table row]

### Blocker Check
YES → BLOCKS {downstream-stage}: {finding-ID} — {reason downstream cannot proceed}
NO  → No downstream blocker identified.
```

---

## TPM STAGE — ADDITIONAL REQUIRED SECTIONS

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            | Source Finding |
|------|-----------------|----------|------------|-----------------------|----------------|
| R-01 | {specific risk} | HIGH     | HIGH       | {concrete mitigation} | {stage/F-NN}   |
| R-02 | {specific risk} | MED      | MED        | {concrete mitigation} | {stage/F-NN}   |
| R-03 | {specific risk} | LOW      | LOW        | {concrete mitigation} | {stage/F-NN}   |
[minimum 3; at least 1 HIGH]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Primary rationale: {cite R-NN or F-NN}
Conditions (if GO WITH CONDITIONS): {what must be resolved}
[VIOLATION-06 if embedded in prose — this block must be a labeled top-level element]
```

---

## SPIRE STAGE — ADDITIONAL REQUIRED SECTION

```
### Mission Alignment

| S-Office Mission | Program        | Artifact/Topic | Alignment               |
|------------------|----------------|----------------|-------------------------|
| {named mission}  | {program name} | {topic}        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named; "strategic priorities" fails this criterion]
```

---

## SYNTHESIS (--stage all only)

```
## Synthesis

### Inter-Stage Blockers

| Upstream Stage | Finding-ID | Downstream Stage | Impact               |
|----------------|------------|------------------|----------------------|
| {stage}        | {F-NN}     | {stage}          | {blocking reason}    |

### Dual-Direction Check

| Ledger-Row | Sent By | Finding-ID | Received By | Acknowledged As | Note   |
|------------|---------|------------|-------------|-----------------|--------|
| L-{N}      | {stage} | {F-NN}     | {stage}     | {F-NN or empty} | {note} |

### Residual Open Items

| Ledger-Row | Origin Stage | Finding-ID | Intended Receiver | Gap  |
|------------|--------------|------------|-------------------|------|
[all rows where Acknowledged As = empty]
[VIOLATION-07 if this section is absent — even an empty section is required]

### Cross-Cutting Themes

| Theme        | Via Value (shared)  | Stages             | Severity Pattern  | Recommended Action |
|--------------|---------------------|--------------------|-------------------|--------------------|
| {theme}      | {shared lens item}  | {stage, stage, ...}| escalating/stable | {action}           |
[Filter Ledger by Via value — any item in 2+ stages' findings is a cross-cutting theme]
[VIOLATION-08 if such a concern is named only inside one stage's section]

### Verdict Registry

| Stage      | Status              | Finding-IDs | Rationale      |
|------------|---------------------|-------------|----------------|
| leadership | {status}            | {IDs}       | {one sentence} |
| teams      | {status}            | {IDs}       | {one sentence} |
| pm         | {status}            | {IDs}       | {one sentence} |
| tpm        | {status + go/no-go} | {IDs}       | {one sentence} |
| arch-board | {status}            | {IDs}       | {one sentence} |
| spire      | {status}            | {IDs}       | {one sentence} |
```

**OUTPUT RULES:** Each stage is its own `## PHASE GATE:` section. Every VIOLATION in the
registry is an independent compliance check. A stage that triggers a violation fails
the criterion the violation governs regardless of other merits.

---

## V-04 — Inertia Framing + Violation Taxonomy

**Axes**: Inertia framing + violation taxonomy (C-20)
**Hypothesis**: Adding a structural INERTIA ANCHOR and per-stage INERTIA: check to the
V-05 R6 base (112 under v6) provides a ninth structural rule (VIOLATION-09: omitted
INERTIA: check) that reinforces C-20 while also enriching C-02 per-stage role loading
with a status-quo pressure frame. The inertia check is a named structural element —
not a prose aside — making it independently verifiable. Combined with the eight-
violation core registry, C-20 ++ is structurally assured and the inertia axis tests
whether the V-05 R6 machinery remains undisturbed. Expected score: 114.

---

You are running `/org-rob`. Execute a full Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → spire

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

---

## VIOLATION REGISTRY

| ID | Violation Name | Anti-Pattern |
|----|---------------|--------------|
| VIOLATION-01 | MISSING ORIENTATION FRAME | A `ROLE:` block without `Frame: orientation.frame = "{value}"` — orientation unverifiable |
| VIOLATION-02 | MALFORMED FINDING ROW | `Via:` is NOT second column in a finding row |
| VIOLATION-03 | BLANK LENS CITATION | `Via:` cell blank or omitted in a finding row |
| VIOLATION-04 | PROSE VERDICT | Stage verdict in prose instead of Verdict Table row |
| VIOLATION-05 | UNSIGNED EXIT CONDITIONS | EXIT block without specific finding IDs cited |
| VIOLATION-06 | BURIED GO/NO-GO | tpm go/no-go in paragraph prose, not a labeled top-level block |
| VIOLATION-07 | ABSENT RESIDUAL SECTION | Synthesis without Residual Open Items section |
| VIOLATION-08 | SINGLE-STAGE THEME | Cross-cutting concern named only in one stage, not elevated to document-level table |
| VIOLATION-09 | OMITTED INERTIA CHECK | A stage that does not include an `INERTIA:` check block — status-quo pressure assessment is missing for this stage |

---

## SETUP

**Step 1 — Write the INERTIA ANCHOR** (permanent for the full run):

```
## Inertia Anchor

INERTIA BASELINE: {what the organization currently does instead of this topic —
the process, tool, or behavior this topic would displace. One sentence, specific.}
```

**Step 2 — Initialize the Write-ahead Ledger:**

```
## Finding Ledger

| Ledger-Row | Stage | ID   | Via                | Finding (short)    | Severity | Inertia Impact | Resolved By | Resolution |
|------------|-------|------|--------------------|--------------------|----------|---------------|-------------|------------|
[stages append as they run; Inertia Impact: THREATENS BASELINE / PRESERVES BASELINE / NEUTRAL]
```

**Step 3 — Load roles:** Read `org.yaml`. Read `.craft/roles/`. Extract `orientation.frame`.
Fallback: leadership=VP Product, teams=Team Leads, pm=Senior PM, tpm=TPM Lead,
arch-board=Principal Architect, spire=Chief of Staff.

---

## STAGE TEMPLATE

```
## PHASE GATE: {stage-name}

ROLE: {name from .craft/roles/}
Frame: orientation.frame = "{extracted value}"
[VIOLATION-01 if Frame: absent]

### ENTRY CONDITIONS
1. {named condition}
2. {second named condition}
[Stage 1: "First stage — no upstream entry conditions."]

### Findings

| ID   | Via                  | Finding                           | Severity | Owner  | Ledger-Row | Inertia Impact        | Resolution Path    |
|------|----------------------|-----------------------------------|----------|--------|------------|-----------------------|--------------------|
| F-01 | {specific lens item} | {concern from role lens}          | HIGH     | {role} | L-{N}      | THREATENS BASELINE    | {concrete action}  |
| F-02 | {specific lens item} | {concern from role lens}          | MED      | {role} | L-{N}      | NEUTRAL               | {concrete action}  |
[minimum 2 rows; Via: must be SECOND column — VIOLATION-02; blank Via: — VIOLATION-03]
[append each row to Write-ahead Ledger immediately, including Inertia Impact value]

### INERTIA CHECK
INERTIA BASELINE: THREATENED / PRESERVES / PARTIALLY THREATENED
Assessment: {one sentence — how this stage's findings interact with the inertia baseline}
[VIOLATION-09 if this block is absent]

### EXIT CONDITIONS
Escalates to {next-stage}: {finding IDs}
Certifies resolved: {finding IDs closed, or "none"}
[VIOLATION-05 if no finding IDs]

### Stage Verdict

| Stage        | Status                                              | Finding-IDs      | Rationale                      |
|--------------|-----------------------------------------------------|------------------|--------------------------------|
| {stage-name} | APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {F-NN, ...} | {one sentence, role-specific} |
[VIOLATION-04 if prose]

### Blocker Check
YES → BLOCKS {downstream-stage}: {finding-ID} — {reason}
NO  → No downstream blocker identified.
```

---

## TPM STAGE — ADDITIONAL REQUIRED SECTIONS

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            | Source Finding | Inertia Link |
|------|-----------------|----------|------------|-----------------------|----------------|--------------|
| R-01 | {specific risk} | HIGH     | HIGH       | {concrete mitigation} | {stage/F-NN}   | {THREATENS / NEUTRAL} |
| R-02 | {specific risk} | MED      | MED        | {concrete mitigation} | {stage/F-NN}   | {THREATENS / NEUTRAL} |
| R-03 | {specific risk} | LOW      | LOW        | {concrete mitigation} | {stage/F-NN}   | {NEUTRAL} |
[minimum 3 rows; at least 1 HIGH; Inertia Link flags risks arising from baseline displacement]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Primary rationale: {cite R-NN or F-NN}
Inertia note: {one sentence on whether baseline displacement is accounted for}
Conditions (if GO WITH CONDITIONS): {what must be resolved}
[VIOLATION-06 if embedded in prose]
```

---

## SPIRE STAGE — ADDITIONAL REQUIRED SECTION

```
### Mission Alignment

| S-Office Mission | Program        | Artifact/Topic | Alignment               |
|------------------|----------------|----------------|-------------------------|
| {named mission}  | {program name} | {topic}        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named]
```

---

## SYNTHESIS (--stage all only)

```
## Synthesis

### Inertia Pressure Summary
INERTIA BASELINE: {restate the anchor}
Stages where baseline is THREATENED: {list}
Risk register entries with Inertia Link = THREATENS: {R-NN list}
Net inertia verdict: HIGH DISPLACEMENT RISK / MODERATE / LOW

### Inter-Stage Blockers

| Upstream Stage | Finding-ID | Downstream Stage | Impact               |
|----------------|------------|------------------|----------------------|
| {stage}        | {F-NN}     | {stage}          | {blocking reason}    |

### Dual-Direction Check

| Ledger-Row | Sent By | Finding-ID | Received By | Acknowledged As | Note   |
|------------|---------|------------|-------------|-----------------|--------|
| L-{N}      | {stage} | {F-NN}     | {stage}     | {F-NN or empty} | {note} |

### Residual Open Items

| Ledger-Row | Origin Stage | Finding-ID | Intended Receiver | Gap  |
|------------|--------------|------------|-------------------|------|
[VIOLATION-07 if section absent even when empty]

### Cross-Cutting Themes

| Theme        | Via Value (shared) | Stages              | Severity Pattern  | Inertia Relevance | Recommended Action |
|--------------|--------------------|---------------------|-------------------|-------------------|--------------------|
| {theme}      | {shared lens item} | {stage, stage, ...} | escalating/stable | {THREATENS / NEUTRAL} | {action}       |
[Filter Ledger by Via value; VIOLATION-08 if recurring concern stays inside one stage]

### Verdict Registry

| Stage      | Status              | Finding-IDs | Inertia Check    | Rationale      |
|------------|---------------------|-------------|------------------|----------------|
| leadership | {status}            | {IDs}       | THREATENED/NEUTRAL | {one sentence} |
| teams      | {status}            | {IDs}       | THREATENED/NEUTRAL | {one sentence} |
| pm         | {status}            | {IDs}       | THREATENED/NEUTRAL | {one sentence} |
| tpm        | {status + go/no-go} | {IDs}       | THREATENED/NEUTRAL | {one sentence} |
| arch-board | {status}            | {IDs}       | THREATENED/NEUTRAL | {one sentence} |
| spire      | {status}            | {IDs}       | THREATENED/NEUTRAL | {one sentence} |
```

**OUTPUT RULES:** INERTIA ANCHOR is written once before Stage 1 and never changed.
Every stage includes an INERTIA CHECK block — VIOLATION-09 if absent.
All other VIOLATION-01 through VIOLATION-08 checks apply unchanged.

---

## V-05 — Full Integration: Teams-First + Inertia Framing + Prohibition Mode

**Axes**: Role sequence (teams-first) + inertia framing + phrasing register (prohibition)
**Hypothesis**: Combining three axes on the V-03 R6 prohibition base tests whether axis
interactions introduce regressions. Teams-first ensures ground-level concerns reach tpm
with maximum escalation depth. Inertia framing adds VIOLATION-09 (a ninth structural
rule) and enriches the risk register's Inertia Link column. The VIOLATION taxonomy
preserves C-20 ++ through the structural additions. The three axes are designed to be
independent: role sequence affects stage ordering but not schema structure; inertia
adds a new structural element but does not displace any existing one; prohibition mode
governs phrasing register, not content. No regression on C-09–C-19 is expected.
Expected score: 114.

---

You are running `/org-rob`. Execute a full Review of Business for the given topic.

**STAGE ORDER (TEAMS-FIRST):** teams → pm → arch-board → leadership → tpm → spire

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence in teams-first order above
- `--scope [group]` — restrict org.yaml roles to this division or tribe

---

## VIOLATION REGISTRY

| ID | Violation Name | Anti-Pattern |
|----|---------------|--------------|
| VIOLATION-01 | INCOMPLETE ROLE BLOCK | `ROLE:` block without `Frame: orientation.frame = "{value}"` — orientation is unstated |
| VIOLATION-02 | MALFORMED FINDING ROW | `Via:` not in second column of a finding row |
| VIOLATION-03 | BLANK VIA CELL | `Via:` cell blank or omitted in any finding row |
| VIOLATION-04 | PROSE VERDICT | Stage verdict in prose instead of Verdict Table row |
| VIOLATION-05 | UNSIGNED EXIT | EXIT block without specific finding IDs cited |
| VIOLATION-06 | BURIED GO/NO-GO | tpm go/no-go recommendation embedded in paragraph prose |
| VIOLATION-07 | ABSENT RESIDUAL SECTION | Synthesis missing Residual Open Items section |
| VIOLATION-08 | SINGLE-STAGE THEME BURIAL | Cross-cutting concern not elevated to document-level Cross-Cutting Themes table |
| VIOLATION-09 | OMITTED INERTIA CHECK | A stage without an `INERTIA:` check block — baseline pressure unassessed for this stage |

---

## SETUP

**Step 1 — Write the INERTIA ANCHOR:**

```
## Inertia Anchor

INERTIA BASELINE: {what the organization currently does instead of this topic —
the specific process, tool, or behavior that would be displaced. One sentence.}
```

**Step 2 — Initialize the Write-ahead Ledger:**

```
## Finding Ledger

| Ledger-Row | Stage | ID   | Via                | Finding (short) | Severity | Inertia Impact | Resolved By | Resolution |
|------------|-------|------|--------------------|--------------------|----------|---------------|-------------|------------|
[no rows yet; stages append as they run]
```

**Step 3 — Load roles:** Read `org.yaml`. Read `.craft/roles/`. Extract `orientation.frame`
per stage. Fallback: teams=Team Leads, pm=Senior PM, arch-board=Principal Architect,
leadership=VP Product, tpm=TPM Lead, spire=Chief of Staff.

**SEQUENCE NOTE:** Because teams runs first, the risk baseline has not been established
when teams reviews. tpm will synthesize the fullest picture — having received findings
from teams, pm, arch-board, and leadership before constructing the risk register. tpm's
Source Finding column must trace risks to the upstream stages that surfaced them.

---

## STAGE TEMPLATE

```
## PHASE GATE: {stage-name}

ROLE: {name from .craft/roles/}
Frame: orientation.frame = "{extracted value — must match .craft/roles/ field}"
[VIOLATION-01 if Frame: absent]

### ENTRY CONDITIONS
1. {named condition — what prior stage must have certified}
2. {second named condition}
[Stage 1 (teams): "First stage — no upstream entry conditions."]

### Findings

| ID   | Via                  | Finding                           | Severity | Owner  | Ledger-Row | Inertia Impact           | Resolution Path          |
|------|----------------------|-----------------------------------|----------|--------|------------|--------------------------|--------------------------|
| F-01 | {specific lens item} | {concern from this role's lens}   | HIGH     | {role} | L-{N}      | THREATENS BASELINE       | {concrete action}        |
| F-02 | {specific lens item} | {concern from this role's lens}   | MED      | {role} | L-{N}      | NEUTRAL                  | {concrete action}        |
[minimum 2 rows; VIOLATION-02 if Via: not second; VIOLATION-03 if Via: blank]
[append each row to Write-ahead Ledger immediately, with Inertia Impact value]

### INERTIA CHECK
INERTIA BASELINE: THREATENED / PRESERVES / PARTIALLY THREATENED — {one sentence}
[VIOLATION-09 if this block is absent from any stage]

### EXIT CONDITIONS
Escalates to {next-stage}: {finding IDs forwarded}
Certifies resolved: {finding IDs closed at this stage, or "none"}
[VIOLATION-05 if no finding IDs cited — generic language is INVALID]

### Stage Verdict

| Stage        | Status                                              | Finding-IDs      | Rationale                       |
|--------------|-----------------------------------------------------|------------------|---------------------------------|
| {stage-name} | APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {F-NN, ...} | {one sentence, role-specific}  |
[VIOLATION-04 if this appears as a prose block — table row IS the verdict, no prose alternative]

### Blocker Check
Does any finding in this stage block a downstream stage?
YES → BLOCKS {downstream-stage}: {finding-ID} — {reason downstream cannot proceed}
NO  → No downstream blocker identified.
```

---

## TPM STAGE — ADDITIONAL REQUIRED SECTIONS

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            | Source Finding | Inertia Link      |
|------|-----------------|----------|------------|-----------------------|----------------|-------------------|
| R-01 | {specific risk} | HIGH     | HIGH       | {concrete mitigation} | {stage/F-NN}   | THREATENS BASELINE |
| R-02 | {specific risk} | MED      | MED        | {concrete mitigation} | {stage/F-NN}   | NEUTRAL           |
| R-03 | {specific risk} | LOW      | LOW        | {concrete mitigation} | {stage/F-NN}   | NEUTRAL           |
[minimum 3 rows; at least 1 HIGH; Source Finding traces risk to the upstream stage that surfaced it]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Primary rationale: {cite R-NN or stage/F-NN}
Inertia note: {one sentence on displacement risk in the go/no-go picture}
Conditions (if GO WITH CONDITIONS): {what must be resolved}
[VIOLATION-06 if this block is embedded in prose — it MUST be a labeled top-level element]
```

---

## SPIRE STAGE — ADDITIONAL REQUIRED SECTION

```
### Mission Alignment

| S-Office Mission | Program        | Artifact/Topic | Alignment               |
|------------------|----------------|----------------|-------------------------|
| {named mission}  | {program name} | {topic}        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be specifically named — "company strategy" fails]
```

---

## SYNTHESIS (--stage all only)

```
## Synthesis

### Inertia Pressure Summary
INERTIA BASELINE: {restate the anchor from setup}
Stages where baseline is THREATENED: {list stage names}
Risk register Inertia Link = THREATENS: {R-NN list}
Net displacement risk: HIGH / MODERATE / LOW — {one sentence}

### Inter-Stage Blockers

| Upstream Stage | Finding-ID | Downstream Stage | Impact               |
|----------------|------------|------------------|----------------------|
| {stage}        | {F-NN}     | {stage}          | {blocking reason}    |
[or "No inter-stage blockers identified." if none]

### Dual-Direction Check

| Ledger-Row | Sent By | Finding-ID | Received By | Acknowledged As | Note   |
|------------|---------|------------|-------------|-----------------|--------|
| L-{N}      | {stage} | {F-NN}     | {stage}     | {F-NN or empty} | {note} |
[Rows where Acknowledged As = empty are RESIDUAL]

### Residual Open Items

| Ledger-Row | Origin Stage | Finding-ID | Intended Receiver | Gap  |
|------------|--------------|------------|-------------------|------|
[list all rows where Acknowledged As = empty]
[VIOLATION-07 if this section is absent — even an empty section must be present]

### Cross-Cutting Themes

| Theme        | Via Value (shared)  | Stages              | Severity Pattern  | Inertia Relevance | Recommended Action |
|--------------|---------------------|---------------------|-------------------|-------------------|--------------------|
| {theme}      | {shared lens item}  | {stage, stage, ...} | escalating/stable | THREATENS/NEUTRAL | {action}           |
[Filter Ledger by Via value — any item in 2+ stages' findings is a cross-cutting theme]
[VIOLATION-08 if a recurring concern is named only inside one stage's section and not here]
[or "No cross-cutting themes identified." if no Via: value recurs across 2+ stages]

### Verdict Registry

| Stage      | Status              | Finding-IDs | Inertia Check       | Rationale      |
|------------|---------------------|-------------|---------------------|----------------|
| teams      | {status}            | {IDs}       | THREATENED/NEUTRAL  | {one sentence} |
| pm         | {status}            | {IDs}       | THREATENED/NEUTRAL  | {one sentence} |
| arch-board | {status}            | {IDs}       | THREATENED/NEUTRAL  | {one sentence} |
| leadership | {status}            | {IDs}       | THREATENED/NEUTRAL  | {one sentence} |
| tpm        | {status + go/no-go} | {IDs}       | THREATENED/NEUTRAL  | {one sentence} |
| spire      | {status}            | {IDs}       | THREATENED/NEUTRAL  | {one sentence} |
```

**OUTPUT RULES:**
- Stages run in teams-first order: teams → pm → arch-board → leadership → tpm → spire.
- INERTIA ANCHOR is written once before Stage 1, never restated except in synthesis.
- Every stage includes an INERTIA CHECK block — VIOLATION-09 if absent.
- VIOLATION-01 through VIOLATION-08 apply to all stages as documented above.
- Each stage is its own `## PHASE GATE:` section. Stages are never merged.
