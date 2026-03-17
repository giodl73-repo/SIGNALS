Now I have complete context. The rubric describes the **spine-centric track** (C-25 = criterion-ID spine, C-26 = self-referential enforcement, C-27 = sole gate, C-28/C-29 = v9 additions). The existing R9 file is a different structural track (manifest-centric). I'll generate fresh R9 variations in the spine-centric track, probing for C-28 and C-29.

---

# listen-support — Variations, Round 9 (rubric v9 — 29 criteria)

**Date:** 2026-03-16  
**Rubric target:** v9 (C-01 through C-29 — 29 criteria; aspirational denominator = 21)  
**Baseline:** R8 V-05 (spine-centric track — passes C-01 through C-27 under v8; fails C-28 and C-29)  
**R9 objective:** Achieve composite 100 under v9 by adding C-28 (Compliance Contract spine-criterion anchoring) and C-29 (Triple self-referential mechanism stack). Single-axis variations isolate each new mechanism independently before combining.

**The two new v9 criteria and their R8 excellence sources:**

- **C-28 — Compliance Contract spine-criterion anchoring**: A COMPLIANCE CONTRACT section explicitly anchors `[C-26: BELT]` and `[C-27: BELT]`, making the spine's self-verification and sole-gate properties contractually obligated rather than structurally incidental. The obligation chain is traceable: CONTRACT → SOLE GATE DECLARATION → spine row.

- **C-29 — Triple self-referential mechanism stack**: All three C-26 mechanisms stack simultaneously: (1) pre-check block before any body is generated, (2) inline `Required:` condition imperative inside the spine row instruction, (3) CONTRACT anchor. No single mechanism alone satisfies C-29 — all three must coexist.

**R9 questions:**
1. Does a COMPLIANCE CONTRACT with only `[C-26: BELT]` + `[C-27: BELT]` anchors — without any triple-stack — satisfy C-28 but not C-29? (V-01)
2. Does adding a pre-check block before body generation (one C-29 mechanism) without the CONTRACT anchor create a partial C-29 signal? (V-02)
3. Does adding an inline `Required:` condition inside the spine row (one C-29 mechanism) without the other two establish the weakest C-29 signal path? (V-03)
4. Do C-28 + the pre-check mechanism compose cleanly without the inline `Required:`? (V-04)
5. Do all three C-29 mechanisms + C-28 CONTRACT anchors compose simultaneously — the composite-100 path? (V-05)

**R8 gap analysis (what is and is not settled):**

- R8 V-05 base: passes C-01 through C-27 under v8. Spine present, self-referential C-26 row present, sole gate declaration present. No CONTRACT anchors. No triple mechanism stack. Fails C-28 and C-29 under v9.
- V-01: adds CONTRACT anchors only. Predicted pass C-28; fail C-29.
- V-02: adds pre-check block only. Predicted fail C-28; partial C-29 signal.
- V-03: adds inline `Required:` only. Predicted fail C-28; partial C-29 signal.
- V-04: adds CONTRACT anchors + pre-check block. Predicted pass C-28; fail C-29 (only 2 of 3 mechanisms).
- V-05: adds CONTRACT anchors + all three C-29 mechanisms. Predicted 100/100.

**R9 variation axes:**

| Axis | Variation | New angle vs R8 | Target criteria |
|------|-----------|-----------------|-----------------|
| Role sequence | V-01 | Support-first generation with CONTRACT anchors | C-28 |
| Output format | V-02 | Pre-body inventory table + pre-check block | C-29 mechanism 1 |
| Phrasing register | V-03 | Consequence-form at body step + inline Required in spine | C-29 mechanism 2 |
| Combined: role sequence + output format | V-04 | CONTRACT anchors + pre-check block | C-28 + partial C-29 |
| Full synthesis | V-05 | All three axes + C-28 + triple C-29 stack | C-28 + C-29 |

Combined: V-04 stacks V-01 (Support-first role sequence + CONTRACT anchors) + V-02 (pre-body inventory table + pre-check). V-05 adds V-03 (consequence-form at body step + inline `Required:`) — the composite-100 candidate.

---

## Fixed Components Applied to All R9 Variations

All R9 variations inherit the full R8 V-05 spine-centric mechanism set.

| Component | R8 V-05 source | R9 status |
|-----------|----------------|-----------|
| CONTROLLED VOCABULARY table (Phase/Category/Volume/Severity) — C-02 | R8 V-05 | Retained (all) |
| PHASE SEVERITY KEY declaration — C-17 | R8 V-05 | Retained (all) |
| STATUS QUO section — inertia framing | R8 V-05 | Retained (all) |
| Ticket planning table (role-phase matrix) | R8 V-05 | Retained (all) |
| TABLE CHECK halt instruction — C-19 | R8 V-05 | Retained (all) |
| Card format with Title as discrete named field — C-01 | R8 V-05 | Retained (all) |
| Phase field on every card — C-11 | R8 V-05 | Retained (all) |
| Phase+Title coexistence requirement — C-14 | R8 V-05 | Retained (all) |
| First-person voice constraint stated explicitly — C-03 | R8 V-05 | Retained (all) |
| Severity grounded in phase key — C-12, C-15 | R8 V-05 | Retained (all) |
| Mid-output verification block — C-13 | R8 V-05 | Retained (all) |
| Prior-tool coverage check in verification — C-16 | R8 V-05 | Retained (all) |
| Gate minimum ≥7 — C-18 | R8 V-05 | Retained (all) |
| Gap analysis with three named sections — C-04 | R8 V-05 | Retained (all) |
| Gap analysis coverage verification block — C-20 | R8 V-05 | Retained (all) |
| Orphan-gap check — C-21 | R8 V-05 | Retained (all) |
| Sentinel language prohibition — C-22 | R8 V-05 | Retained (all) |
| Belt-and-suspenders for C-01/C-03/C-04 — C-23 | R8 V-05 | Retained (all) |
| Materialized-view traceability instruction — C-24 | R8 V-05 | Retained (all) |
| Criterion-ID-named FINAL VERIFICATION SPINE — C-25 | R8 V-05 | Retained (all) |
| Self-referential C-26 row in spine — C-26 | R8 V-05 | Retained (all); inline Required added in V-03/V-04/V-05 |
| SOLE GATE DECLARATION — C-27 | R8 V-05 | Retained (all) |
| COMPLIANCE CONTRACT with BELT anchors — C-28 | **NEW** | Added in V-01/V-04/V-05 |
| Pre-check block before body generation — C-29 mechanism 1 | **NEW** | Added in V-02/V-04/V-05 |
| Inline Required condition in spine row — C-29 mechanism 2 | **NEW** | Added in V-03/V-05 |
| CONTRACT anchor for C-26/C-27 — C-29 mechanism 3 | **NEW** | Added in V-01/V-04/V-05 (via CONTRACT) |

---

## R9 Variation Axes

R1: role sequence, output format, lifecycle emphasis.  
R2: phrasing register, inertia framing, theme-first generation.  
R3: vocabulary commitment, manifest tables, role-phase matrix.  
R4: per-ticket commitment fused with role-phase matrix.  
R5: gate mechanism + standalone halt instruction.  
R6: gap analysis verification, orphan check, sentinel prohibition.  
R7: belt-and-suspenders, materialized-view, criterion-ID spine.  
R8: self-referential spine enforcement (C-26), sole gate declaration (C-27). R8 V-05 is composite 100 under v8.  
R9: Compliance Contract BELT anchors (C-28) and triple self-referential mechanism stack (C-29).

| Axis | Variation | New angle vs R8 | Target criteria |
|------|-----------|-----------------|-----------------|
| Role sequence | V-01 | Support-anchored ordering + CONTRACT BELT anchors | C-28 |
| Output format | V-02 | Pre-body inventory table + pre-check block | C-29 mech-1 |
| Phrasing register | V-03 | Consequence-form at body step + spine inline Required | C-29 mech-2 |
| Combined: role sequence + output format | V-04 | V-01 + V-02: CONTRACT anchors + pre-check | C-28 + partial C-29 |
| Full synthesis | V-05 | All three + full triple-stack | C-28 + C-29 |

---

## V-01 — Single Axis: Role Sequence (Support-Anchored Ordering + CONTRACT BELT Anchors)

**Axis:** Role sequence — Support generates the initial ticket batch (Phase 1 priority), SRE adds reliability/monitoring tickets, PM adds adoption-risk tickets, UX adds interaction-friction tickets. Each role announces its scope before generating. This ordering ensures operational reality grounds the inventory before strategic framing enters.

Additionally, a COMPLIANCE CONTRACT section is added at the top, anchoring C-26 and C-27 with BELT markers. This is the single new compliance mechanism — no pre-check block, no inline Required in the spine row.

**Hypothesis:** Support-first ordering surfaces the highest-volume tickets naturally (migration confusion, missing docs, repeated questions). Later roles add signal without overwriting the operational foundation. CONTRACT anchors C-26 and C-27 contractually — creating C-28 signal — but without the triple-stack, C-29 is not yet achieved.

**Predicted composite under v9:** 95.90 (passes C-01 through C-28; fails C-29 — only CONTRACT anchor present, no pre-check block or inline Required).

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).

---

### COMPLIANCE CONTRACT

Read before any step. These obligations govern the entire output.

**[C-26: BELT] — Self-referential spine enforcement:**
The FINAL VERIFICATION SPINE at the end of this output must contain a row for C-26 that
verifies itself. A spine that omits the C-26 self-check row fails C-26 regardless of all
other compliance.

**[C-27: BELT] — Spine as sole gate:**
The FINAL VERIFICATION SPINE is the only acceptance gate for this output. Output is not
complete until the spine is present and all Essential rows (C-01 through C-04) show PASS.
A declared acceptance made without a present and passing spine fails C-27 regardless of
all other compliance.

---

### CONTROLLED VOCABULARY

| Field    | Allowed values                                                         |
|----------|------------------------------------------------------------------------|
| Phase    | Phase 1 (day 0-30) / Phase 2 (day 31-60) / Phase 3 (day 61-90)        |
| Category | how-to / bug / config / integration / feature-request                  |
| Volume   | high / medium / low                                                    |
| Severity | P0 (data loss or outage) / P1 (blocked workflow) / P2 (degraded) / P3 (friction) |

No values outside this table are permitted in any scored field.

**PHASE SEVERITY KEY — declared before any ticket is generated:**
Phase 1 defaults to P2/P3. A Phase 1 ticket may only be P1 if the workflow is completely
blocked; P0 requires data loss. Phase 2 defaults to P1/P2. Phase 3 may escalate to P0/P1
when a reliability concern reaches leadership-visibility threshold. Phase drives severity
— do not assign severity independent of phase context.

---

### STATUS QUO ANALYSIS

```
Prior approach users are replacing: ___
Habit they carry in (the assumption that causes the first wall): ___
Primary migration friction: ___
```

---

### STEP 1 — Support: Initial Ticket Batch

You are Support. You have been answering the same questions all week. Before any other role
generates tickets, fill this table with the tickets Support will own:

**Support planning table:**

| T-ID | Role | Phase | Category | Volume | Severity | Persona | Theme |
|------|------|-------|----------|--------|----------|---------|-------|
| T-01 | Support | Phase 1 | ___ | ___ | ___ | C-__ | ___ |
| T-02 | Support | Phase 1 | ___ | ___ | ___ | C-__ | ___ |
| T-03 | Support | Phase 2 | ___ | ___ | ___ | C-__ | ___ |

Minimum 2 Support tickets. At least one Phase 1, at least one Phase 2.

---

### STEP 2 — SRE: Reliability and Monitoring Tickets

You are the SRE. Review the Support tickets. Add tickets for reliability, monitoring,
and runbook gaps that Support flagged but did not explicitly file:

**SRE planning table:**

| T-ID | Role | Phase | Category | Volume | Severity | Persona | Theme |
|------|------|-------|----------|--------|----------|---------|-------|
| T-xx | SRE | Phase ___ | ___ | ___ | ___ | SRE | ___ |

Minimum 2 SRE tickets. At least one Phase 2 or Phase 3.

---

### STEP 3 — PM: Adoption-Risk Tickets

You are the PM. Review all tickets so far. Add tickets filed when activation metrics
are below forecast and you cannot tell if it is a product problem or communication problem:

**PM planning table:**

| T-ID | Role | Phase | Category | Volume | Severity | Persona | Theme |
|------|------|-------|----------|--------|----------|---------|-------|
| T-xx | PM | Phase ___ | ___ | ___ | ___ | PM | ___ |

Minimum 1 PM ticket.

---

### STEP 4 — UX: Interaction-Friction Tickets

You are the UX designer. Review all tickets. Add tickets filed from session-recording
observations — places where users stall before they understand the system:

**UX planning table:**

| T-ID | Role | Phase | Category | Volume | Severity | Persona | Theme |
|------|------|-------|----------|--------|----------|---------|-------|
| T-xx | UX | Phase ___ | ___ | ___ | ___ | UX | ___ |

Minimum 1 UX ticket.

---

### STEP 5 — Full Inventory Table

Consolidate all planning tables:

| T-ID | Title | Role | Phase | Category | Volume | Severity | Persona | Migration? |
|------|-------|------|-------|----------|--------|----------|---------|------------|

Total tickets: 6–12. At least 3 Phase 1, 2 Phase 2, 1 Phase 3.
At least 3 distinct personas. P0 tickets ≤ floor(total × 0.25). High-volume ≤ floor(total × 0.50).

**TABLE CHECK — halt if any check fails before continuing:**
- [ ] All Phase values use controlled vocabulary: PASS / FAIL
- [ ] All Category values use controlled vocabulary: PASS / FAIL
- [ ] All Volume values use controlled vocabulary: PASS / FAIL
- [ ] All Severity values use controlled vocabulary: PASS / FAIL
- [ ] P0 count within ceiling: PASS / FAIL
- [ ] High-volume count within ceiling: PASS / FAIL
- [ ] Phase severity key honored (Phase 1 not P0 without data loss): PASS / FAIL

If any check shows FAIL: revise the planning table. Do not generate bodies until all checks pass.

---

### STEP 6 — Ticket Bodies

Write each ticket card in the following format. Write as me — first person throughout.
No role titles in body text ("I", "my", "we" — never "the SRE", "the user", "the developer").

```
Title: [descriptive subject line — not a ticket ID]
Phase: [Phase N (day X-Y)]
Category: [controlled vocabulary]
Persona: [C-xx or role name]
Volume: [controlled vocabulary]
Severity: [controlled vocabulary — per phase key]
Body: [3-5 sentences. First person. Opens with the migration context or the immediate
frustration. States what was tried. States what happened. States what is needed.]
```

**REQUIRED (C-01):** Title must appear as a named field inside the card body. A markdown
heading that contains the title does not satisfy this requirement. The Title: field must be
a discrete entry in the card.

**REQUIRED (C-03):** All body text must be first person. A body containing "the user",
"the developer", "the SRE", or any third-person role reference fails C-03 regardless of
all other compliance.

**REQUIRED (C-14):** Phase and Title must both appear as named fields on the same card.
A card with Phase but no Title field fails C-14. A card with Title but no Phase field fails C-14.

Prior-tool framing: at least one ticket body must reference the specific prior approach or tool
named in STATUS QUO ANALYSIS. The body should name what the user expected from the old behavior.

Generate tickets in role order: Support tickets first, then SRE, then PM, then UX.
Within each role, sort by Phase ascending.

---

### MID-OUTPUT VERIFICATION BLOCK

Execute after generating the first 4 ticket bodies. Do not continue to the remaining bodies
until this block is complete.

For each card generated so far:
- [ ] Title field present as discrete named field (not only in heading)
- [ ] Phase field present
- [ ] Category is controlled vocabulary
- [ ] Volume is controlled vocabulary
- [ ] Severity is controlled vocabulary and consistent with Phase severity key
- [ ] Body is first-person throughout; no third-person role references

**Prior-tool coverage check:** Does at least one body reference the prior approach named
in STATUS QUO ANALYSIS by name? If not, revise the most relevant Phase 1 body before continuing.

**Temporal adoption window check:** Are Phase 1 tickets at P2/P3 baseline unless documented
exception applies? Are Phase 3 tickets permitted to escalate to P0/P1? Verify alignment.

**Gate minimum:** Count cards passing all checks above. Required: ≥7 cards must pass all
checks before proceeding to gap analysis. If fewer than 7 pass, halt and correct.

---

### STEP 7 — Gap Analysis

Produce three sections. Each section must name ≥1 specific artifact.

**Doc Gaps**
For each gap:
- Entry: [what is missing]
- Artifact: [name of the doc, guide, or reference that should exist]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3 — per phase key; do not use "N/A" or "varies"]

**Design Gaps**
For each gap:
- Entry: [what behavior or constraint is missing]
- Change: [what the product or system needs to do differently]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3]

**Operational Gaps**
For each gap:
- Entry: [what runbook, alert, or process is missing]
- Process change: [what the team needs to do]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3]

Minimum 2 entries per category.

**REQUIRED (C-22):** No gap entry may use "N/A", "none", "TBD", or "varies" in any
consequence field (Severity, Artifact, Change, Process change). If a value is unknown,
state the best estimate and flag it as [estimate].

**REQUIRED (C-21):** Every gap must be grounded by at least one ticket (Grounded by: row).
A gap with no T-NN citation is an orphan — remove it or add the ticket that sources it.

**Materialized view (C-24):** After all gaps are written, produce a one-row summary per gap
showing: Gap entry | Section | Grounded by tickets | Severity. This materializes the gap
inventory as a scannable table rather than prose.

---

### GAP ANALYSIS VERIFICATION BLOCK

After completing the gap analysis and materialized view:

- [ ] Doc Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Design Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Operational Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] No orphan gaps (all gaps have Grounded by: entries): PASS / FAIL
- [ ] No sentinel language in any consequence field: PASS / FAIL
- [ ] Materialized gap view present: PASS / FAIL

If any check shows FAIL: correct before proceeding to the FINAL VERIFICATION SPINE.

---

### FINAL VERIFICATION SPINE

| C-ID | Criterion | Pass? |
|------|-----------|-------|
| C-01 | Title field present as discrete named field on every card | ___ |
| C-02 | Controlled vocabulary declared and enforced throughout | ___ |
| C-03 | First-person voice throughout; constraint stated explicitly in prompt | ___ |
| C-04 | Gap analysis present with three named sections, each ≥1 named artifact | ___ |
| C-11 | Phase field present on every card | ___ |
| C-12 | Severity grounded in phase key; phase context documented | ___ |
| C-13 | Mid-output verification block executed | ___ |
| C-14 | Phase and Title coexist as named fields on every card | ___ |
| C-15 | Severity accounts for temporal adoption window per phase | ___ |
| C-16 | Prior-tool coverage present and verified | ___ |
| C-17 | Phase-as-severity-key declared before ticket generation | ___ |
| C-18 | Gate minimum ≥7 cards passed before gap analysis | ___ |
| C-19 | TABLE CHECK halt instruction present | ___ |
| C-20 | Gap analysis coverage verification block present | ___ |
| C-21 | Every gap cites ≥1 ticket; orphan check executed | ___ |
| C-22 | No sentinel language in consequence fields | ___ |
| C-23 | Belt-and-suspenders for C-01 (REQUIRED note + spine row); C-03 (REQUIRED note + spine row); C-04 (verification block + spine row) | ___ |
| C-24 | Materialized-view traceability instruction present | ___ |
| C-25 | This spine names all criteria by C-NN ID | ___ |
| C-26 | This spine contains a row for C-26 verifying that this spine row is present | ___ |
| C-27 | This spine is declared as the sole acceptance gate (SOLE GATE DECLARATION below) | ___ |
| C-28 | COMPLIANCE CONTRACT section present with [C-26: BELT] and [C-27: BELT] anchors | ___ |
| C-29 | All three C-26 mechanisms present simultaneously (pre-check block + inline Required + CONTRACT anchor) | ___ |

**SOLE GATE DECLARATION (C-27):** This spine is the only acceptance gate. Output is complete
only when all Essential rows (C-01 through C-04) show PASS. If any Essential row shows FAIL,
halt and correct before marking the spine complete. No other section of this output constitutes
an acceptance signal.
```

---

## V-02 — Single Axis: Output Format (Pre-Body Inventory Table + Pre-Check Block)

**Axis:** Output format — a TICKET INVENTORY TABLE materializes all planned tickets as a dense pre-flight table (T-ID, Title, Phase, Category, Volume, Severity, Persona, Theme) before any body is generated. Titles are locked in the table before bodies expand them. Additionally, a PRE-CHECK BLOCK executes after the table and before the first body — this is the first of the three C-29 mechanisms (pre-check block). No COMPLIANCE CONTRACT added; no inline `Required:` in the spine C-26 row.

**Hypothesis:** Materializing the full inventory before writing bodies locks vocabulary and prevents drift during the longer body-writing phase. The pre-check block at the boundary between planning and generation is the load-bearing C-29 mechanism — it confirms that the spine will contain a C-26 self-check row before any body is written. Confirmed without the CONTRACT, this test isolates pre-check as the C-29 signal source.

**Predicted composite under v9:** 92.86 (passes C-01 through C-27 + C-24 [materialized inventory]; fails C-28 and full C-29 — only one of three mechanisms present).

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).

---

### CONTROLLED VOCABULARY

| Field    | Allowed values                                                         |
|----------|------------------------------------------------------------------------|
| Phase    | Phase 1 (day 0-30) / Phase 2 (day 31-60) / Phase 3 (day 61-90)        |
| Category | how-to / bug / config / integration / feature-request                  |
| Volume   | high / medium / low                                                    |
| Severity | P0 (data loss or outage) / P1 (blocked workflow) / P2 (degraded) / P3 (friction) |

No values outside this table are permitted in any scored field.

**PHASE SEVERITY KEY — declared before any ticket is generated:**
Phase 1 defaults to P2/P3. Phase 1 may reach P1 only if workflow is completely blocked;
P0 requires data loss. Phase 2 defaults to P1/P2. Phase 3 may escalate to P0/P1 at
leadership-visibility threshold. Severity must be derived from the phase — it is not
independent.

---

### STATUS QUO ANALYSIS

```
Prior approach users are replacing: ___
Habit carried in (assumption that causes first wall): ___
Primary migration friction: ___
```

---

### STEP 1 — TICKET INVENTORY TABLE

Complete this table before writing any ticket body. This table is the authoritative
pre-flight record of all tickets. Bodies expand entries from this table — they do not
introduce new tickets or change vocabulary values.

| T-ID | Title | Role | Phase | Category | Volume | Severity | Persona | Theme | Migration? |
|------|-------|------|-------|----------|--------|----------|---------|-------|------------|
| T-01 | ___   | ___  | ___   | ___      | ___    | ___      | ___     | ___   | Y/N        |
| T-02 | ___   | ___  | ___   | ___      | ___    | ___      | ___     | ___   | Y/N        |
| T-03 | ___   | ___  | ___   | ___      | ___    | ___      | ___     | ___   | Y/N        |
| ...  |       |      |       |          |        |          |         |       |            |

**Inventory constraints:**
- Total: 6–12 tickets
- Phase 1: ≥3 rows | Phase 2: ≥2 rows | Phase 3: ≥1 row
- SRE: ≥2 rows | Support: ≥2 rows | C-xx personas: ≥2 rows
- P0 rows: ≤ floor(total × 0.25) | High-volume rows: ≤ floor(total × 0.50)
- Distinct personas: ≥3
- Migration? = Y on ≥1 row (prior approach named in STATUS QUO ANALYSIS)

**REQUIRED (C-01):** Title column must contain a human-readable subject line for every row.
Title values from this table will appear as named `Title:` fields inside each card body.
A ticket body that omits the `Title:` field or uses the T-ID as the title fails C-01.

Do not proceed until all rows are complete with controlled vocabulary values.

---

### STEP 2 — TABLE CHECK

Verify the TICKET INVENTORY TABLE before generating any body:

- [ ] All Phase values match controlled vocabulary: PASS / FAIL
- [ ] All Category values match controlled vocabulary: PASS / FAIL
- [ ] All Volume values match controlled vocabulary: PASS / FAIL
- [ ] All Severity values match controlled vocabulary: PASS / FAIL
- [ ] Phase severity key honored (Phase 1 not P0 without data loss; Phase 3 P0/P1 permitted): PASS / FAIL
- [ ] P0 row count within ceiling: PASS / FAIL
- [ ] High-volume row count within ceiling: PASS / FAIL
- [ ] At least one Migration? = Y row: PASS / FAIL

**TABLE CHECK — HALT:** If any check shows FAIL, revise the inventory table and re-run this
check. Do not proceed to the PRE-CHECK BLOCK or body generation until all checks pass.

---

### PRE-CHECK BLOCK

Execute after TABLE CHECK, before generating any ticket body.

This block confirms that the output structure is ready for C-26 compliance before
generation begins.

Pre-check item 1 — Spine self-reference readiness:
The FINAL VERIFICATION SPINE at the end of this output will contain a row for C-26.
That row will verify that the spine contains a C-26 self-check row.
State: [ CONFIRMED — spine structure is pre-committed to include C-26 self-check row ]

Pre-check item 2 — Sole gate readiness:
The FINAL VERIFICATION SPINE will carry a SOLE GATE DECLARATION.
No section of this output other than the spine will serve as an acceptance signal.
State: [ CONFIRMED — sole gate structure is pre-committed ]

Pre-check item 3 — First-person constraint readiness:
All ticket bodies will be written in first person. No role titles will appear in body text.
State: [ CONFIRMED — voice constraint is active for all bodies ]

**PRE-CHECK GATE:** All three items must show CONFIRMED before body generation begins.
If any item cannot be confirmed, halt and resolve the structural issue first.

---

### STEP 3 — TICKET BODIES

Write each ticket card in the format below. Source T-ID, Title, Phase, Category, Persona,
Volume, and Severity from the TICKET INVENTORY TABLE. Do not change vocabulary values from
the table during body expansion.

Write as me — first person throughout. No role titles in body text.
("I", "my", "we" — never "the SRE", "the user", "the developer".)

```
Title: [from inventory table — descriptive subject line]
Phase: [Phase N (day X-Y) — from inventory table]
Category: [from inventory table]
Persona: [from inventory table]
Volume: [from inventory table]
Severity: [from inventory table]
Body: [3-5 sentences. First person. Opens with migration context or immediate frustration.
      Names the specific prior approach from STATUS QUO ANALYSIS if Migration? = Y.
      States what was tried. States what happened. States what is needed.]
```

**REQUIRED (C-01):** Title must be a discrete named field in the card body. A markdown
heading that includes the title does not satisfy this — Title must be a separate `Title:` line.

**REQUIRED (C-03):** All body text must be first person. A body containing "the user",
"the developer", "the SRE", or any third-person role reference fails C-03 regardless of
all other compliance.

**REQUIRED (C-14):** Phase and Title must both be discrete named fields on the same card.

Sort output: Phase 1 tickets first, Phase 2 next, Phase 3 last. Within each phase, sort by
role: Support → SRE → PM → UX → C-xx.

---

### MID-OUTPUT VERIFICATION BLOCK

Execute after generating cards T-01 through T-04. Do not generate additional cards until
this block is complete.

For each card generated so far:
- [ ] Title field present as discrete named field
- [ ] Phase field present
- [ ] Category is controlled vocabulary value from inventory table
- [ ] Volume is controlled vocabulary value from inventory table
- [ ] Severity is controlled vocabulary value from inventory table and consistent with phase key
- [ ] Body is first-person; no third-person role references

**Prior-tool coverage check:** Is at least one body written so far referencing the prior
approach from STATUS QUO ANALYSIS by name? If not, revise the most relevant Phase 1 body.

**Temporal adoption window check:** Phase 1 severity at P2/P3 baseline (exceptions documented)?
Phase 3 escalation to P0/P1 permitted only at operational threshold?

**Gate minimum:** ≥7 cards must pass all checks above before gap analysis. Count passing cards.
If fewer than 7 pass: halt and correct before continuing.

---

### STEP 4 — GAP ANALYSIS

Produce three sections. Each section must name ≥1 specific artifact.

**Doc Gaps**
For each gap:
- Entry: [what is missing]
- Artifact: [name of the specific document or guide that should exist]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3; estimate if unknown — do not use "N/A" or "TBD"]

**Design Gaps**
For each gap:
- Entry: [what behavior or constraint is missing]
- Change: [what the product needs to do differently]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3]

**Operational Gaps**
For each gap:
- Entry: [what runbook, alert, or process is missing]
- Process change: [what the team needs to do]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3]

Minimum 2 entries per category.

**REQUIRED (C-22):** No consequence field (Artifact, Change, Process change, Severity) may
use "N/A", "none", "TBD", or "varies". Use best estimate + [estimate] flag if uncertain.

**REQUIRED (C-21):** Every gap must have a Grounded by: row with ≥1 T-NN citation.
An orphan gap (no ticket citation) must be removed or grounded.

**Materialized view (C-24):** After completing all gaps, produce this summary table:

| Entry | Section | Grounded by | Severity |
|-------|---------|-------------|----------|

One row per gap. This is the materialized gap inventory.

---

### GAP ANALYSIS VERIFICATION BLOCK

- [ ] Doc Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Design Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Operational Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] No orphan gaps: PASS / FAIL
- [ ] No sentinel language: PASS / FAIL
- [ ] Materialized gap view present: PASS / FAIL

If any check shows FAIL: correct before proceeding to the FINAL VERIFICATION SPINE.

---

### FINAL VERIFICATION SPINE

| C-ID | Criterion | Pass? |
|------|-----------|-------|
| C-01 | Title field present as discrete named field on every card | ___ |
| C-02 | Controlled vocabulary declared and enforced throughout | ___ |
| C-03 | First-person voice throughout; constraint stated explicitly in prompt | ___ |
| C-04 | Gap analysis present with three named sections, each ≥1 named artifact | ___ |
| C-11 | Phase field present on every card | ___ |
| C-12 | Severity grounded in phase key | ___ |
| C-13 | Mid-output verification block executed | ___ |
| C-14 | Phase and Title coexist as named fields on every card | ___ |
| C-15 | Severity accounts for temporal adoption window | ___ |
| C-16 | Prior-tool coverage present and verified | ___ |
| C-17 | Phase-as-severity-key declared before generation | ___ |
| C-18 | Gate minimum ≥7 cards passed before gap analysis | ___ |
| C-19 | TABLE CHECK halt instruction present | ___ |
| C-20 | Gap analysis coverage verification block present | ___ |
| C-21 | Every gap cites ≥1 ticket; orphan check executed | ___ |
| C-22 | No sentinel language in consequence fields | ___ |
| C-23 | Belt-and-suspenders for C-01 (REQUIRED note + spine row); C-03 (REQUIRED note + spine row); C-04 (verification block + spine row) | ___ |
| C-24 | Materialized-view traceability instruction present | ___ |
| C-25 | This spine names all criteria by C-NN ID | ___ |
| C-26 | This spine contains a row for C-26 verifying that this spine row is present | ___ |
| C-27 | This spine is declared as the sole acceptance gate (SOLE GATE DECLARATION below) | ___ |
| C-28 | COMPLIANCE CONTRACT section present with [C-26: BELT] and [C-27: BELT] anchors | ___ |
| C-29 | All three C-26 mechanisms present simultaneously (pre-check block + inline Required + CONTRACT anchor) | ___ |

**SOLE GATE DECLARATION (C-27):** This spine is the only acceptance gate. Output is complete
only when all Essential rows (C-01 through C-04) show PASS. If any Essential row shows FAIL,
halt and correct before marking the spine complete. No other section constitutes acceptance.
```

---

## V-03 — Single Axis: Phrasing Register (Consequence-Form at Body Step + Inline Required in Spine)

**Axis:** Phrasing register — the body-generation step carries consequence-form language directly at the site of generation: "A body containing any third-person role reference fails C-03 regardless of other compliance." Additionally, the spine's C-26 row carries an inline `Required:` condition imperative. This is the second of the three C-29 mechanisms tested in isolation: inline `Required:` in the spine row itself. No COMPLIANCE CONTRACT added; no pre-check block.

**Hypothesis:** Consequence-form language at the generation step (not only at contract-read time or verification time) creates independent enforcement visibility. A model generating the body sees the failure consequence at the moment of writing. The inline `Required:` in the spine row forces the spine to be self-verifying by instruction, not only by structure. This tests whether consequence-form register at two new sites (body step + spine row) creates C-29 signal without the CONTRACT anchor.

**Predicted composite under v9:** 92.86 (passes C-01 through C-27; fails C-28 — no CONTRACT; achieves one of three C-29 mechanisms — partial C-29 signal only).

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).

---

### CONTROLLED VOCABULARY

| Field    | Allowed values                                                         |
|----------|------------------------------------------------------------------------|
| Phase    | Phase 1 (day 0-30) / Phase 2 (day 31-60) / Phase 3 (day 61-90)        |
| Category | how-to / bug / config / integration / feature-request                  |
| Volume   | high / medium / low                                                    |
| Severity | P0 (data loss or outage) / P1 (blocked workflow) / P2 (degraded) / P3 (friction) |

No values outside this table are permitted in any scored field.

**PHASE SEVERITY KEY — declared before any ticket is generated:**
Phase 1 defaults to P2/P3. Phase 1 may reach P1 only if workflow is completely blocked;
P0 requires data loss. Phase 2 defaults to P1/P2. Phase 3 may escalate to P0/P1 at
leadership-visibility threshold. Severity is derived from phase context — do not assign
it independently.

---

### STATUS QUO ANALYSIS

```
Prior approach users are replacing: ___
Habit carried in (assumption that causes first wall): ___
Primary migration friction: ___
```

---

### STEP 1 — TICKET PLANNING

| T-ID | Role | Phase | Category | Volume | Severity | Persona | Theme |
|------|------|-------|----------|--------|----------|---------|-------|

Total: 6–12. Phase 1: ≥3. Phase 2: ≥2. Phase 3: ≥1.
SRE: ≥2. Support: ≥2. C-xx personas: ≥2. Distinct personas: ≥3.
P0: ≤ floor(total × 0.25). High-volume: ≤ floor(total × 0.50).

---

### TABLE CHECK — HALT

Verify before generating any body:
- [ ] All Phase values use controlled vocabulary: PASS / FAIL
- [ ] All Category values use controlled vocabulary: PASS / FAIL
- [ ] All Volume values use controlled vocabulary: PASS / FAIL
- [ ] All Severity values use controlled vocabulary: PASS / FAIL
- [ ] Phase severity key honored: PASS / FAIL
- [ ] Ceiling constraints met: PASS / FAIL

If any check shows FAIL: revise the plan before continuing.

---

### STEP 2 — TICKET BODIES

Write each ticket card. Write as me — first person throughout.
No role titles in body text ("I", "my", "we" — never "the user", "the developer", "the SRE").

```
Title: [descriptive subject line]
Phase: [Phase N (day X-Y)]
Category: [controlled vocabulary]
Persona: [C-xx or role]
Volume: [controlled vocabulary]
Severity: [controlled vocabulary — grounded in phase key]
Body: [3-5 sentences. First person. Migration context or immediate frustration.
      Prior-approach reference if applicable. What was tried. What happened. What is needed.]
```

**REQUIRED (C-01):** Title must be a discrete `Title:` field in the card body.
A heading containing the title does not satisfy C-01 — Title must be a separate named field.

**REQUIRED (C-03):** All body text must be first person.
**A body containing "the user", "the developer", "the SRE", or any other third-person role
reference fails C-03 regardless of all other compliance in the output.**

**REQUIRED (C-14):** Phase and Title must coexist as discrete named fields on every card.

**Consequence check at generation site:** Before writing each body, confirm: this body will
be written in first person with no role title references. If a draft body contains a
third-person reference, rewrite it before outputting. Do not output a body that fails C-03.

Prior-tool requirement: at least one body must name the specific prior approach from STATUS
QUO ANALYSIS. That body should open with what the user expected from the old approach.

---

### MID-OUTPUT VERIFICATION BLOCK

Execute after generating the first 4 cards. Do not continue until complete.

For each card so far:
- [ ] Title field present as discrete named field
- [ ] Phase field present
- [ ] Category is controlled vocabulary
- [ ] Volume is controlled vocabulary
- [ ] Severity is controlled vocabulary and consistent with phase key
- [ ] Body is first-person; no third-person role references

**Prior-tool coverage check:** At least one body names the prior approach? If not, revise.

**Temporal adoption window check:** Phase 1 at P2/P3 baseline (exceptions documented)?
Phase 3 escalation to P0/P1 permitted?

**Gate minimum:** ≥7 cards must pass all checks. If fewer than 7 pass: halt and correct.

---

### STEP 3 — GAP ANALYSIS

Produce three sections. Each must name ≥1 specific artifact.

**Doc Gaps**
- Entry: [missing doc]
- Artifact: [specific document name]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3 estimate — do not use "N/A", "none", "TBD"]

**Design Gaps**
- Entry: [missing behavior or constraint]
- Change: [what the product needs]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3 estimate]

**Operational Gaps**
- Entry: [missing runbook, alert, or process]
- Process change: [what the team needs to do]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3 estimate]

Minimum 2 entries per category.

**Consequence check at gap writing site:** Before finalizing each gap entry, confirm:
this gap has a Grounded by: citation, a named artifact/change/process, and a severity estimate.
**A gap entry with no Grounded by: ticket citation is an orphan and fails C-21 regardless of
all other compliance in the output.**

**Materialized view (C-24):** After completing all gaps:

| Entry | Section | Grounded by | Severity |
|-------|---------|-------------|----------|

---

### GAP ANALYSIS VERIFICATION BLOCK

- [ ] Doc Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Design Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Operational Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] No orphan gaps: PASS / FAIL
- [ ] No sentinel language: PASS / FAIL
- [ ] Materialized gap view present: PASS / FAIL

Correct any FAIL before proceeding to the FINAL VERIFICATION SPINE.

---

### FINAL VERIFICATION SPINE

| C-ID | Criterion | Pass? |
|------|-----------|-------|
| C-01 | Title field present as discrete named field on every card | ___ |
| C-02 | Controlled vocabulary declared and enforced throughout | ___ |
| C-03 | First-person voice throughout; constraint stated explicitly in prompt | ___ |
| C-04 | Gap analysis present with three named sections, each ≥1 named artifact | ___ |
| C-11 | Phase field present on every card | ___ |
| C-12 | Severity grounded in phase key | ___ |
| C-13 | Mid-output verification block executed | ___ |
| C-14 | Phase and Title coexist as named fields on every card | ___ |
| C-15 | Severity accounts for temporal adoption window | ___ |
| C-16 | Prior-tool coverage present and verified | ___ |
| C-17 | Phase-as-severity-key declared before generation | ___ |
| C-18 | Gate minimum ≥7 cards passed before gap analysis | ___ |
| C-19 | TABLE CHECK halt instruction present | ___ |
| C-20 | Gap analysis coverage verification block present | ___ |
| C-21 | Every gap cites ≥1 ticket; orphan check executed | ___ |
| C-22 | No sentinel language in consequence fields | ___ |
| C-23 | Belt-and-suspenders for C-01 (REQUIRED note + spine row); C-03 (REQUIRED + consequence-form + spine row); C-04 (gap verification block + spine row) | ___ |
| C-24 | Materialized-view traceability instruction present | ___ |
| C-25 | This spine names all criteria by C-NN ID | ___ |
| C-26 | **Required:** This spine row for C-26 must show PASS before output is accepted. A spine that omits or FAILs this row fails C-26 regardless of other compliance. — This row verifies that the C-26 self-check row is present in this spine. | ___ |
| C-27 | This spine is declared as the sole acceptance gate (SOLE GATE DECLARATION below) | ___ |
| C-28 | COMPLIANCE CONTRACT section present with [C-26: BELT] and [C-27: BELT] anchors | ___ |
| C-29 | All three C-26 mechanisms present simultaneously (pre-check block + inline Required + CONTRACT anchor) | ___ |

**SOLE GATE DECLARATION (C-27):** This spine is the only acceptance gate. Output is complete
only when all Essential rows (C-01 through C-04) show PASS. If any Essential row shows FAIL,
halt and correct. No other section constitutes acceptance.
```

---

## V-04 — Combined: Role Sequence + Output Format (CONTRACT Anchors + Pre-Check Block)

**Axis:** Role sequence (V-01 Support-anchored ordering) + Output format (V-02 pre-body inventory table + pre-check block). Additionally adds the COMPLIANCE CONTRACT with `[C-26: BELT]` and `[C-27: BELT]` anchors (C-28). This combines two of the three C-29 mechanisms (CONTRACT anchor + pre-check block) but omits the inline `Required:` condition — deliberately leaving one mechanism absent to test whether two of three is sufficient for C-29.

**Hypothesis:** The CONTRACT anchor (from V-01's COMPLIANCE CONTRACT) and the pre-check block (from V-02's PRE-CHECK BLOCK) are two independent enforcement sites. Combined, they constitute two of the three C-29 mechanisms. C-28 is fully satisfied. C-29 requires all three simultaneously — V-04 tests whether the omission of the inline `Required:` in the spine row creates a detectable structural gap.

**Predicted composite under v9:** 96.94 (passes C-01 through C-28; fails C-29 — two of three mechanisms present, not all three).

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).

---

### COMPLIANCE CONTRACT

Read before any step. These obligations govern the entire output.

**[C-26: BELT] — Self-referential spine enforcement:**
The FINAL VERIFICATION SPINE must contain a row for C-26 that verifies itself. A spine
that omits the C-26 self-check row fails C-26 regardless of all other compliance.

**[C-27: BELT] — Spine as sole gate:**
The FINAL VERIFICATION SPINE is the only acceptance gate. Output is not complete until
the spine is present and all Essential rows (C-01 through C-04) show PASS. A declared
acceptance without a present, passing spine fails C-27 regardless of all other compliance.

---

### CONTROLLED VOCABULARY

| Field    | Allowed values                                                         |
|----------|------------------------------------------------------------------------|
| Phase    | Phase 1 (day 0-30) / Phase 2 (day 31-60) / Phase 3 (day 61-90)        |
| Category | how-to / bug / config / integration / feature-request                  |
| Volume   | high / medium / low                                                    |
| Severity | P0 (data loss or outage) / P1 (blocked workflow) / P2 (degraded) / P3 (friction) |

No values outside this table are permitted in any scored field.

**PHASE SEVERITY KEY — declared before any ticket is generated:**
Phase 1 defaults to P2/P3. Phase 1 may reach P1 only if workflow is completely blocked;
P0 requires data loss. Phase 2 defaults to P1/P2. Phase 3 may escalate to P0/P1 at
leadership-visibility threshold. Severity is derived from phase.

---

### STATUS QUO ANALYSIS

```
Prior approach users are replacing: ___
Habit carried in (assumption that causes first wall): ___
Primary migration friction: ___
```

---

### STEP 1 — TICKET INVENTORY TABLE

Complete before generating any body. This table locks all titles and vocabulary values.
Bodies expand entries from this table; they do not introduce new tickets or change values.

Build the inventory in role order: Support rows first, then SRE, then PM, then UX, then C-xx.

| T-ID | Title | Role | Phase | Category | Volume | Severity | Persona | Theme | Migration? |
|------|-------|------|-------|----------|--------|----------|---------|-------|------------|
| T-01 | ___   | Support | Phase 1 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-02 | ___   | Support | Phase 1 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-03 | ___   | Support | Phase 2 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-04 | ___   | SRE | Phase ___ | ___ | ___ | ___ | SRE | ___ | Y/N |
| T-05 | ___   | SRE | Phase ___ | ___ | ___ | ___ | SRE | ___ | Y/N |
| T-06 | ___   | PM | Phase ___ | ___ | ___ | ___ | PM | ___ | Y/N |
| T-07 | ___   | UX | Phase ___ | ___ | ___ | ___ | UX | ___ | Y/N |
| T-08 | ___   | C-xx | Phase ___ | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-09 | ___   | C-xx | Phase ___ | ___ | ___ | ___ | C-__ | ___ | Y/N |
| ...  |       |      |           |     |    |     |     |     |    |

**Constraints:** Total 6–12. Phase 1: ≥3. Phase 2: ≥2. Phase 3: ≥1.
P0: ≤ floor(total × 0.25). High-volume: ≤ floor(total × 0.50). Distinct personas: ≥3.

**REQUIRED (C-01):** Every Title in this table must be a human-readable subject line.
These values will appear as discrete `Title:` fields in the card bodies.

Do not proceed until all rows are complete.

---

### STEP 2 — TABLE CHECK — HALT

- [ ] All Phase values match controlled vocabulary: PASS / FAIL
- [ ] All Category values match controlled vocabulary: PASS / FAIL
- [ ] All Volume values match controlled vocabulary: PASS / FAIL
- [ ] All Severity values match controlled vocabulary: PASS / FAIL
- [ ] Phase severity key honored across all rows: PASS / FAIL
- [ ] P0 ceiling satisfied: PASS / FAIL
- [ ] High-volume ceiling satisfied: PASS / FAIL
- [ ] Role ordering correct (Support rows precede SRE rows precede PM rows): PASS / FAIL
- [ ] Migration? = Y on ≥1 row: PASS / FAIL

If any check shows FAIL: revise the inventory table. Do not proceed until all checks pass.

---

### PRE-CHECK BLOCK

Execute after TABLE CHECK, before generating any ticket body.

Pre-check item 1 — Spine self-reference readiness:
The FINAL VERIFICATION SPINE will contain a row for C-26 that verifies itself.
Per COMPLIANCE CONTRACT [C-26: BELT] above, this row is contractually required.
State: [ CONFIRMED — C-26 self-check row pre-committed ]

Pre-check item 2 — Sole gate readiness:
The FINAL VERIFICATION SPINE will carry a SOLE GATE DECLARATION.
Per COMPLIANCE CONTRACT [C-27: BELT] above, the spine is the only acceptance gate.
State: [ CONFIRMED — sole gate structure pre-committed ]

Pre-check item 3 — Role ordering readiness:
Ticket bodies will be generated in Support → SRE → PM → UX → C-xx role order.
Within each role, Phase ascending.
State: [ CONFIRMED — role-ordered generation active ]

**PRE-CHECK GATE:** All three items must show CONFIRMED. If any cannot be confirmed, halt.

---

### STEP 3 — TICKET BODIES

Generate bodies in role order: Support tickets first, then SRE, then PM, then UX, then C-xx.
Within each role, Phase ascending. Source all field values from the TICKET INVENTORY TABLE.

Write as me — first person throughout. No role titles in body text.

```
Title: [from inventory table]
Phase: [Phase N (day X-Y)]
Category: [from inventory table]
Persona: [from inventory table]
Volume: [from inventory table]
Severity: [from inventory table]
Body: [3-5 sentences. First person. Migration context or frustration. Prior approach named
      if Migration? = Y. What was tried. What happened. What is needed.]
```

**REQUIRED (C-01):** Title must be a discrete `Title:` field in the card body.

**REQUIRED (C-03):** All body text must be first person. A body containing "the user",
"the developer", "the SRE", or any third-person role reference fails C-03 regardless of
all other compliance.

**REQUIRED (C-14):** Phase and Title must coexist as discrete named fields on every card.

---

### MID-OUTPUT VERIFICATION BLOCK

Execute after the first 4 cards. Do not continue until complete.

- [ ] Title field present as discrete named field on each card checked
- [ ] Phase field present on each card
- [ ] Category is controlled vocabulary
- [ ] Volume is controlled vocabulary
- [ ] Severity is controlled vocabulary and consistent with phase key
- [ ] Body is first-person; no third-person role references
- [ ] Role order is Support → SRE → PM → UX → C-xx

**Prior-tool coverage check:** At least one body names the prior approach? If not, revise.
**Temporal window check:** Phase 1 at P2/P3 baseline (exceptions documented)? Phase 3 escalation permitted?
**Gate minimum:** ≥7 cards pass all checks. If fewer than 7: halt and correct.

---

### STEP 4 — GAP ANALYSIS

Three sections. Each must name ≥1 specific artifact.

**Doc Gaps**
- Entry: [missing artifact type]
- Artifact: [specific document name]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3; use estimate + [estimate] if uncertain — no "N/A" or "TBD"]

**Design Gaps**
- Entry: [missing behavior or constraint]
- Change: [what the product needs]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3]

**Operational Gaps**
- Entry: [missing runbook, alert, or process]
- Process change: [what the team needs]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3]

Minimum 2 entries per category.

**REQUIRED (C-22):** No consequence field uses "N/A", "none", "TBD", or "varies".
**REQUIRED (C-21):** Every gap has a Grounded by: row with ≥1 T-NN. Orphan gaps are removed.

**Materialized view (C-24):**

| Entry | Section | Grounded by | Severity |
|-------|---------|-------------|----------|

---

### GAP ANALYSIS VERIFICATION BLOCK

- [ ] Doc Gaps ≥1 named artifact: PASS / FAIL
- [ ] Design Gaps ≥1 named artifact: PASS / FAIL
- [ ] Operational Gaps ≥1 named artifact: PASS / FAIL
- [ ] No orphan gaps: PASS / FAIL
- [ ] No sentinel language: PASS / FAIL
- [ ] Materialized view present: PASS / FAIL

Correct any FAIL before the FINAL VERIFICATION SPINE.

---

### FINAL VERIFICATION SPINE

| C-ID | Criterion | Pass? |
|------|-----------|-------|
| C-01 | Title field present as discrete named field on every card | ___ |
| C-02 | Controlled vocabulary declared and enforced throughout | ___ |
| C-03 | First-person voice throughout; constraint stated explicitly in prompt | ___ |
| C-04 | Gap analysis present with three named sections, each ≥1 named artifact | ___ |
| C-11 | Phase field present on every card | ___ |
| C-12 | Severity grounded in phase key | ___ |
| C-13 | Mid-output verification block executed | ___ |
| C-14 | Phase and Title coexist as named fields on every card | ___ |
| C-15 | Severity accounts for temporal adoption window | ___ |
| C-16 | Prior-tool coverage present and verified | ___ |
| C-17 | Phase-as-severity-key declared before generation | ___ |
| C-18 | Gate minimum ≥7 cards passed before gap analysis | ___ |
| C-19 | TABLE CHECK halt instruction present | ___ |
| C-20 | Gap analysis coverage verification block present | ___ |
| C-21 | Every gap cites ≥1 ticket; orphan check executed | ___ |
| C-22 | No sentinel language in consequence fields | ___ |
| C-23 | Belt-and-suspenders for C-01 (REQUIRED note + inventory table + spine row); C-03 (REQUIRED note + spine row); C-04 (gap verification block + spine row) | ___ |
| C-24 | Materialized-view traceability instruction present | ___ |
| C-25 | This spine names all criteria by C-NN ID | ___ |
| C-26 | This spine contains a row for C-26 verifying that this spine row is present [per COMPLIANCE CONTRACT C-26: BELT] | ___ |
| C-27 | This spine is declared as the sole acceptance gate [per COMPLIANCE CONTRACT C-27: BELT] (SOLE GATE DECLARATION below) | ___ |
| C-28 | COMPLIANCE CONTRACT present with [C-26: BELT] and [C-27: BELT] anchors | ___ |
| C-29 | All three C-26 mechanisms present simultaneously (pre-check block + inline Required + CONTRACT anchor) | ___ |

**SOLE GATE DECLARATION (C-27):** This spine is the only acceptance gate. Output is complete
only when all Essential rows (C-01 through C-04) show PASS. If any Essential row shows FAIL,
halt and correct. No other section constitutes acceptance.
```

---

## V-05 — Full Synthesis: Role Sequence + Output Format + Phrasing Register + C-28 + C-29

**Axis:** All three single axes combined — Support-anchored role sequence (V-01), pre-body inventory table (V-02), consequence-form at body generation step and inline `Required:` in spine (V-03) — plus full C-28 and C-29 mechanism stacking.

**C-28:** COMPLIANCE CONTRACT with `[C-26: BELT]` and `[C-27: BELT]` anchors. The obligation chain is explicit: CONTRACT → SOLE GATE DECLARATION → spine row.

**C-29 — Triple mechanism stack (all three simultaneously):**
1. **PRE-CHECK BLOCK** (before any body): "The FINAL VERIFICATION SPINE will contain a row for C-26 that verifies itself — State: CONFIRMED"
2. **Inline `Required:` in the spine C-26 row**: "Required: this spine row for C-26 must show PASS before output is accepted"
3. **CONTRACT anchor** `[C-26: BELT]` in the COMPLIANCE CONTRACT

All three coexist simultaneously, eliminating every single point of self-referential failure.

**Predicted composite under v9:** 100.00 (passes C-01 through C-29 — full triple-stack satisfies C-29; CONTRACT anchors satisfy C-28; all prior criteria satisfied by inherited R8 V-05 structure).

**Candidate v10 patterns surfaced:**
- **C-30 candidate:** Consequence-form at body generation site (STEP 3 inline failure declaration independent of CONTRACT and spine)
- **C-31 candidate:** Gap-writing-site consequence-form — orphan failure declared at the gap writing step, not only in the verification block
- **C-32 candidate:** Pre-check registry completeness — PRE-CHECK BLOCK names all sites governed by consequence-form, creating a registry parallel to the CONTRACT's RESTATING POSITIONS
- **C-33 candidate:** Role-ordered generation as a structural constraint — generation order is mechanically enforced by the inventory table's role-sorted rows, not only by instruction

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).

---

### COMPLIANCE CONTRACT

Read before any step. These obligations govern the entire output.
This contract takes precedence over any conflicting instruction in any subsequent section.

**[C-26: BELT] — Self-referential spine enforcement:**
The FINAL VERIFICATION SPINE must contain a row for C-26 that verifies itself.
A spine that omits the C-26 self-check row fails C-26 regardless of all other compliance.
Consequence: output is not accepted without a PASS on the C-26 spine row.

**[C-27: BELT] — Spine as sole gate:**
The FINAL VERIFICATION SPINE is the only acceptance gate for this output.
Output is not complete until the spine is present and all Essential rows (C-01 through C-04)
show PASS. A declared completion without a present, passing spine fails C-27 regardless of
all other compliance. Consequence: any acceptance signal outside the spine is invalid.

These two obligations are restated at each governed site below. The contract governs in
case of conflict.

**Governed sites:**
- PRE-CHECK BLOCK: carries C-26 and C-27 readiness confirmations derived from this contract
- STEP 3 — Ticket Bodies: consequence-form for C-03 at the generation site
- FINAL VERIFICATION SPINE: carries C-26 inline Required condition and SOLE GATE DECLARATION

---

### CONTROLLED VOCABULARY

| Field    | Allowed values                                                         |
|----------|------------------------------------------------------------------------|
| Phase    | Phase 1 (day 0-30) / Phase 2 (day 31-60) / Phase 3 (day 61-90)        |
| Category | how-to / bug / config / integration / feature-request                  |
| Volume   | high / medium / low                                                    |
| Severity | P0 (data loss or outage) / P1 (blocked workflow) / P2 (degraded) / P3 (friction) |

No values outside this table are permitted in any scored field.

**PHASE SEVERITY KEY — declared before any ticket is generated:**
Phase 1 defaults to P2/P3. Phase 1 may reach P1 only if workflow is completely blocked;
P0 requires data loss. Phase 2 defaults to P1/P2. Phase 3 may escalate to P0/P1 at
leadership-visibility threshold. Severity is always derived from phase context —
it is not assigned independently.

---

### STATUS QUO ANALYSIS

```
Prior approach users are replacing: ___
Habit carried in (assumption that causes first wall): ___
Primary migration friction: ___
```

---

### STEP 1 — TICKET INVENTORY TABLE

Complete before generating any body. This table locks titles and all vocabulary values.
Bodies expand entries from this table; they do not introduce new tickets or change values.

Build rows in Support → SRE → PM → UX → C-xx order. Within each role, Phase ascending.

| T-ID | Title | Role | Phase | Category | Volume | Severity | Persona | Theme | Migration? |
|------|-------|------|-------|----------|--------|----------|---------|-------|------------|
| T-01 | ___   | Support | Phase 1 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-02 | ___   | Support | Phase 1 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-03 | ___   | Support | Phase 2 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-04 | ___   | SRE | Phase 1 | ___ | ___ | ___ | SRE | ___ | Y/N |
| T-05 | ___   | SRE | Phase 2 | ___ | ___ | ___ | SRE | ___ | Y/N |
| T-06 | ___   | SRE | Phase 3 | ___ | ___ | ___ | SRE | ___ | Y/N |
| T-07 | ___   | PM | Phase 1 | ___ | ___ | ___ | PM | ___ | Y/N |
| T-08 | ___   | UX | Phase 2 | ___ | ___ | ___ | UX | ___ | Y/N |
| T-09 | ___   | C-xx | Phase 1 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| T-10 | ___   | C-xx | Phase 2 | ___ | ___ | ___ | C-__ | ___ | Y/N |
| ...  |       |      |          |     |     |     |      |     |     |

**Constraints:** Total 6–12. Phase 1: ≥3. Phase 2: ≥2. Phase 3: ≥1.
P0: ≤ floor(total × 0.25). High-volume: ≤ floor(total × 0.50). Distinct personas: ≥3.
SRE: ≥2. Support: ≥2. C-xx: ≥2 (≤2 per individual C-xx persona). Migration? = Y on ≥1 row.

**REQUIRED (C-01):** Every Title must be a human-readable subject line — not a ticket ID.
These values will appear as discrete `Title:` named fields inside each card body.

Do not proceed until all rows are filled with controlled vocabulary values.

---

### STEP 2 — TABLE CHECK — HALT

- [ ] All Phase values match controlled vocabulary: PASS / FAIL
- [ ] All Category values match controlled vocabulary: PASS / FAIL
- [ ] All Volume values match controlled vocabulary: PASS / FAIL
- [ ] All Severity values match controlled vocabulary: PASS / FAIL
- [ ] Phase severity key honored (Phase 1 not P0 without data loss): PASS / FAIL
- [ ] P0 ceiling satisfied: PASS / FAIL
- [ ] High-volume ceiling satisfied: PASS / FAIL
- [ ] Role ordering correct (Support rows before SRE rows before PM rows): PASS / FAIL
- [ ] Migration? = Y on ≥1 row: PASS / FAIL

**TABLE CHECK — HALT:** If any check shows FAIL, revise the inventory table and re-run.
Do not proceed to the PRE-CHECK BLOCK until all checks pass.

---

### PRE-CHECK BLOCK

Execute after TABLE CHECK, before generating any ticket body.

This block confirms structural readiness for C-26 and C-27 compliance before generation.
Per COMPLIANCE CONTRACT above — all three items below are contractually required.

**Pre-check item 1 — Spine self-reference readiness [C-26: BELT]:**
The FINAL VERIFICATION SPINE will contain a row for C-26 that verifies itself.
Per COMPLIANCE CONTRACT [C-26: BELT] above, this row is not optional.
State: [ CONFIRMED — C-26 self-check row pre-committed to the output spine ]

**Pre-check item 2 — Sole gate readiness [C-27: BELT]:**
The FINAL VERIFICATION SPINE will carry a SOLE GATE DECLARATION.
Per COMPLIANCE CONTRACT [C-27: BELT] above, no other section constitutes an acceptance signal.
State: [ CONFIRMED — SOLE GATE DECLARATION pre-committed to the output spine ]

**Pre-check item 3 — Role-ordered generation readiness:**
Ticket bodies will be generated in Support → SRE → PM → UX → C-xx role order, within each
role sorted Phase ascending. This ordering is structurally locked by the inventory table rows.
State: [ CONFIRMED — role-ordered body generation sequence active ]

**PRE-CHECK GATE:** All three items must show CONFIRMED before body generation begins.
If any item cannot be confirmed, halt and resolve the structural issue.

---

### STEP 3 — TICKET BODIES

Generate bodies in the order of the TICKET INVENTORY TABLE (Support → SRE → PM → UX → C-xx,
Phase ascending within each role). Source all field values from the table.

Write as me — first person throughout. No role titles in body text.
("I", "my", "we" — never "the user", "the developer", "the SRE", "the UX researcher".)

```
Title: [from inventory table — descriptive subject line]
Phase: [Phase N (day X-Y) — from inventory table]
Category: [from inventory table]
Persona: [from inventory table]
Volume: [from inventory table]
Severity: [from inventory table — grounded in phase key]
Body: [3-5 sentences. First person. Opens with migration context or immediate frustration.
      If Migration? = Y: names the prior approach from STATUS QUO ANALYSIS and what the
      user expected from it. States what was tried. States what happened. States what is needed.]
```

**REQUIRED (C-01):** Title must be a discrete `Title:` named field in the card body.
A markdown heading that contains the title does not satisfy C-01.

**REQUIRED (C-03):** All body text must be first person.
**A body containing "the user", "the developer", "the SRE", or any third-person role reference
fails C-03 regardless of all other compliance in this output.**
Before writing each body: check that no draft sentence uses a third-person role reference.
Rewrite before outputting. Do not output a body that fails C-03.

**REQUIRED (C-14):** Phase and Title must coexist as discrete named fields on every card.

---

### MID-OUTPUT VERIFICATION BLOCK

Execute after generating the first 4 ticket bodies. Do not generate additional bodies
until this block is complete.

For each card generated so far:
- [ ] Title field present as discrete named field (not only in heading)
- [ ] Phase field present
- [ ] Category matches inventory table value
- [ ] Volume matches inventory table value
- [ ] Severity matches inventory table value and is consistent with phase key
- [ ] Body is first-person; no third-person role references
- [ ] Role order maintained (Support cards precede SRE cards)

**Prior-tool coverage check:** At least one body written so far references the prior approach
from STATUS QUO ANALYSIS by name? If not, revise the most relevant Phase 1 Support body.

**Temporal adoption window check:** Phase 1 at P2/P3 baseline (documented exception for P1)?
Phase 3 escalation to P0/P1 only at operational threshold?

**Gate minimum:** Count cards passing all checks above.
Required: ≥7 cards pass before proceeding to gap analysis.
If fewer than 7 pass: halt and correct failing cards, then recount.

---

### STEP 4 — GAP ANALYSIS

Produce three sections. Each must name ≥1 specific artifact.

**Doc Gaps**
For each gap:
- Entry: [what is missing — name the gap concisely]
- Artifact: [specific document, guide, or reference that should exist — name it]
- Grounded by: T-NN, T-NN [at least one ticket ID]
- Severity of absence: [P0–P3 estimate — use [estimate] if uncertain]

**Design Gaps**
For each gap:
- Entry: [missing behavior or constraint]
- Change: [what the product needs to do differently — name the change]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3 estimate]

**Operational Gaps**
For each gap:
- Entry: [missing runbook, alert, or process]
- Process change: [what the team needs to do — name the change]
- Grounded by: T-NN, T-NN
- Severity of absence: [P0–P3 estimate]

Minimum 2 entries per category.

**REQUIRED (C-22):** No consequence field uses "N/A", "none", "TBD", or "varies".
Use best estimate with [estimate] flag if the exact value is uncertain.
Do not leave any consequence field empty.

**REQUIRED (C-21 — consequence form):** Every gap must have a Grounded by: row with ≥1 T-NN.
**A gap entry with no ticket citation is an orphan and fails C-21 regardless of all other
compliance in this output.** Before finalizing each gap entry, verify the Grounded by: row
is present and non-empty.

**Materialized view (C-24):** After completing all gaps, produce this summary table.
This is the canonical gap inventory — a scorer reading only this table must see every gap:

| Entry | Section | Grounded by | Severity |
|-------|---------|-------------|----------|

---

### GAP ANALYSIS VERIFICATION BLOCK

After completing gaps and the materialized view:

- [ ] Doc Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Design Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] Operational Gaps present with ≥1 named artifact: PASS / FAIL
- [ ] No orphan gaps (every gap has Grounded by: with ≥1 T-NN): PASS / FAIL
- [ ] No sentinel language in any consequence field: PASS / FAIL
- [ ] Materialized gap view present and complete: PASS / FAIL

If any check shows FAIL: correct before proceeding to the FINAL VERIFICATION SPINE.

---

### FINAL VERIFICATION SPINE

| C-ID | Criterion | Pass? |
|------|-----------|-------|
| C-01 | Title field present as discrete named field on every card | ___ |
| C-02 | Controlled vocabulary declared and enforced throughout | ___ |
| C-03 | First-person voice throughout; constraint stated explicitly in prompt | ___ |
| C-04 | Gap analysis present with three named sections, each ≥1 named artifact | ___ |
| C-11 | Phase field present on every card | ___ |
| C-12 | Severity grounded in phase key; phase context documented | ___ |
| C-13 | Mid-output verification block executed | ___ |
| C-14 | Phase and Title coexist as discrete named fields on every card | ___ |
| C-15 | Severity accounts for temporal adoption window per phase | ___ |
| C-16 | Prior-tool coverage present and verified in mid-output block | ___ |
| C-17 | Phase-as-severity-key declared before ticket generation | ___ |
| C-18 | Gate minimum ≥7 cards passed before gap analysis | ___ |
| C-19 | TABLE CHECK halt instruction present | ___ |
| C-20 | Gap analysis coverage verification block present | ___ |
| C-21 | Every gap cites ≥1 ticket; orphan check executed; consequence-form at gap step | ___ |
| C-22 | No sentinel language in consequence fields | ___ |
| C-23 | Belt-and-suspenders for C-01 (REQUIRED + inventory table + spine row); C-03 (REQUIRED + consequence-form at step + spine row); C-04 (gap verification block + spine row) | ___ |
| C-24 | Materialized-view traceability instruction present; canonical gap table produced | ___ |
| C-25 | This spine names all criteria by C-NN ID | ___ |
| C-26 | **Required:** This spine row for C-26 must show PASS before output is accepted. A spine that omits or FAILs this row fails C-26 regardless of all other compliance. — This row verifies that the C-26 self-check row is present in this spine. [Per COMPLIANCE CONTRACT C-26: BELT] | ___ |
| C-27 | This spine is declared as the sole acceptance gate [per COMPLIANCE CONTRACT C-27: BELT] — SOLE GATE DECLARATION below | ___ |
| C-28 | COMPLIANCE CONTRACT present with [C-26: BELT] and [C-27: BELT] anchors; governed sites listed; precedence declared | ___ |
| C-29 | All three C-26 mechanisms present simultaneously: (1) PRE-CHECK BLOCK item 1 confirms spine self-reference before generation; (2) C-26 spine row carries inline Required condition; (3) COMPLIANCE CONTRACT [C-26: BELT] anchor | ___ |

**SOLE GATE DECLARATION (C-27):** This spine is the only acceptance gate. Output is complete
only when all Essential rows (C-01 through C-04) show PASS. If any Essential row shows FAIL,
halt and correct before marking the spine complete. No other section of this output
constitutes an acceptance signal. The spine is the sole suspenders.
```

---

## Summary

| Variation | Axis | New vs R8 V-05 | C-28 | C-29 | Predicted composite v9 |
|-----------|------|----------------|------|------|------------------------|
| V-01 | Role sequence | CONTRACT with BELT anchors | PASS | FAIL (1 of 3 mechanisms) | ~95.90 |
| V-02 | Output format | Pre-body inventory table + pre-check block | FAIL | Partial (1 of 3) | ~92.86 |
| V-03 | Phrasing register | Consequence-form at body step + inline Required | FAIL | Partial (1 of 3) | ~92.86 |
| V-04 | Role sequence + output format | CONTRACT + pre-check block | PASS | FAIL (2 of 3) | ~96.94 |
| V-05 | Full synthesis | All three + full triple-stack | PASS | PASS | 100.00 |

**V-05 is the composite-100 candidate.** It satisfies C-28 via the COMPLIANCE CONTRACT with `[C-26: BELT]` and `[C-27: BELT]` anchors, and C-29 via all three simultaneous mechanisms: the PRE-CHECK BLOCK (pre-generation confirmation), the inline `Required:` condition inside the C-26 spine row, and the CONTRACT anchor itself. The obligation chain is fully traceable: CONTRACT → PRE-CHECK BLOCK → inline Required → SOLE GATE DECLARATION → spine row.

**Candidate v10 criteria exposed by V-05:**
- C-30: Consequence-form at body generation site (independent of CONTRACT, independent of spine)
- C-31: Gap-writing-site consequence-form (orphan failure declared at the step, not only in the verification block)
- C-32: Pre-check registry completeness (PRE-CHECK BLOCK names all consequence-form enforcement sites as a registry)
- C-33: Role-ordered generation as structural constraint (inventory table row ordering mechanically enforces role sequence, not only by instruction)
