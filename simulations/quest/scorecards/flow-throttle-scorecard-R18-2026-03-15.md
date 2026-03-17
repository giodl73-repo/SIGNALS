Now I have everything needed to score all five R18 variations. Let me perform the full evaluation.

---

## flow-throttle Score — Round 18 / Rubric v18

### Scoring Architecture

| Tier | Criteria | Points each | Total |
|------|----------|-------------|-------|
| Essential | C-01 – C-05 | 12 | 60 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-48 | 5 | 200 |
| **Max composite** | | | **290** |

**Baseline inheritance:** All R17 variants pass C-01 through C-44 (270/270 under v17). Every R18 variant explicitly inherits that corpus — Sections A/B/C identical to V-01 or declared as such; Steps 1A–2H and Role 3 Fields 1–4 carried forward intact.

---

### V-01 — Output Format (single-axis)

**C-01 through C-44 (baseline):** All PASS — identical role structure to proven R17 patterns, with Section A (7-site inventory), Section B (7 column contracts with violation-type annotations at anchor sites), Section C (7-row annotation inventory with PROHIBITED dropout clause co-located), Step 1A/1B gates, Steps 2A–2H with standing REGISTRY GAP reminders and phase entry conditions, Role 3 Fields 1–4. No regressions introduced.

**C-45 — "Does NOT confirm" column:** PASS. Signal distinction register has explicit `Does NOT confirm` column header. Non-conflation statement names it: "The 'Does NOT confirm' column value for SIG-01 makes this limitation a column-readable fact without requiring prose parsing." Limitation is a cell value, not embedded prose.

**C-46 — Prompt-header signal chain declaration:** PASS. Role activation chain table appears before any role body. SIG-01 appears in Role 1's Handoff cell; SIG-02 appears in Role 1.5's Handoff cell — structurally distinct, scannable before entering any role.

**C-47 — Bypass-attempt rejection register:** PASS. "Bypass-attempt rejection register" section contains a typed 3-column table: `Bypass attempt | Attempt type | Structural reason for rejection`. One row with attempt type "Looks complete". Auditable row, not prose.

**C-48 — Required-fill bypass rejection field:** PASS. "BYPASS GATE CONDITION" field placed between the register and the count verification table. Explicit SHALL NOT instruction: "An executor SHALL NOT open the count verification table until this field is filled." Two-option form. Field placement physically gates the table.

**Score: 290/290** | All 5 essential PASS

---

### V-02 — Role Sequence (single-axis)

**C-01 through C-44:** All PASS — Role 1 and Steps 1A–2H declared identical to V-01; Role 3 Fields 1–4 declared identical. Signal separation via dedicated Role 1.5 architecture is the same structure R17 carried.

**C-45:** PASS. Signal distinction table in Role 1.5 has `Does NOT confirm` column. Non-conflation statement: "makes each signal's limitation column-readable: an executor can verify SIG-01's limitation by scanning the 'Does NOT confirm' cell without parsing surrounding prose." Column reference is explicit.

**C-46:** PASS. Role activation chain table at header with 4 rows (Role 1, 1.5, 2, 3). SIG-01 in Role 1 Handoff cell ("SIG-01: FORMAT CONTRACT COMPLETE"); SIG-02 in Role 1.5 Handoff cell ("SIG-02: INVENTORY VERIFIED or INVENTORY INCOMPLETE"). Appears before any role body.

**C-47:** PASS. "Bypass-attempt rejection register" section in Role 1.5 inertia-frame section. Typed 3-column table: `Bypass attempt | Attempt type | Structural reason for rejection`. One row with attempt type "Looks complete" — fully auditable.

**C-48:** PASS. "INERTIA-FRAME REJECTION FIELD" with explicit SHALL FILL instruction: "The verification table is not available until this field is filled." Two-option form. Placement gates the verification table.

**Audit Field 5:** Notably upgraded from V-01 — uses a structured table with `Item | Criterion | Evidence required | Status` columns rather than a prose list, making audit inspection itself a row-scan task.

**Score: 290/290** | All 5 essential PASS

---

### V-03 — Lifecycle Emphasis (single-axis)

**C-01 through C-44:** All PASS — Phase 0 contains Sections A/B/C identical to V-01. Phase 2 Steps 1A–2H declared identical with phase-adapted terminology. Phase 3 Fields 1–4 declared identical.

**C-45:** PASS. "Signal specification table" in Phase 0.5 has `Does NOT confirm` column. Non-conflation statement: "makes the limitation of each signal a phase-visible fact: SIG-01's 'Does NOT confirm' cell names count non-verification; SIG-02 must be independently produced at Phase 1." Column-scannable, not prose-embedded.

**C-46:** PASS. Lifecycle stage overview table at prompt header. `Gate signal` column shows SIG-01 in Phase 0's row and SIG-02 in Phase 1's row — structurally distinct cells before any phase body begins. Note: the signal appearance is via `Gate signal` column (not "Signal chain" or "Handoff"), which is the lifecycle-adapted equivalent. C-46 requires visibility at prompt header before any role activates — satisfied.

**C-47:** PASS (with minor vocabulary adaptation). "Bypass defeat record" in Phase 0.5 uses `Bypass attempt | Stage type | Gate reason` columns. Column names differ from the canonical form (Attempt type → Stage type; Structural reason → Gate reason) but the structural property is achieved — typed register with named columns making the defeat a scannable row. Audit Field 5(c) explicitly checks for "Stage type" cell, confirming this is intentional lifecycle adaptation. The bypass defeat is auditable by row scan.

**C-48:** PASS. "PHASE GATE FIELD" with explicit SHALL NOT instruction: "Phase 1 (COUNT VERIFICATION) SHALL NOT open until this field is filled." Named as a required gate slot in the lifecycle sequence. Two-option form. Phase 0.5 output confirms: "Phase gate field filled. Phase 1 entry gate satisfied." Gate is a lifecycle-phase event.

**Novel element:** Phase 1 gate status uses a two-field record (SIG-02 status + Phase 2 entry status as separate fill fields), making gate clearance a multi-record declaration rather than a single handoff signal.

**Score: 290/290** | All 5 essential PASS

---

### V-04 — Phrasing Register + Inertia Framing (combined)

**C-01 through C-44:** All PASS — Sections A/B/C declared identical to V-01 with SHALL-language reinforcement. Steps 1A–2H declared identical with all SHALL instructions carried through. Fields 1–4 declared identical with SHALL language.

**C-45:** PASS. "SHALL-contract signal table" with `DOES NOT CONFIRM` as column header (capitalized). Non-conflation statement: "The DOES NOT CONFIRM value for SIG-01 is the authoritative statement of this limit." Capitalizing the column header name promotes it to a contract term — strongest claim of column authority across all variants.

**C-46:** PASS. "Role activation contract" table at header with `SHALL activate when`, `Handoff signal`, and `SHALL NOT activate if` columns. SIG-01 in Role 1 Handoff cell; SIG-02 in Role 1.5 Handoff cell. Novel: the `SHALL NOT activate if` column exposes consequences of non-compliance directly in the header table — each role's bypass condition is visible before entering any role body.

**C-47:** PASS (column vocabulary adapted to SHALL register). "PROHIBITED FRAMING REGISTER" with `Prohibited framing | SHALL NOT proceed because | Structural enforcement` columns. The column name "SHALL NOT proceed because" makes each row a contract prohibition row. The audit Field 5(c) checks for this exact column. Bypass defeat is a typed auditable row — C-47 achieved.

**C-48:** PASS. "MANDATORY BYPASS DECLARATION" with explicit "activation prerequisite" framing: "the count verification sequence SHALL NOT open until this declaration is filled." Two-option form. The field is an activation prerequisite rather than a section — this is the strongest framing statement across variants.

**Novel element:** Count verification atomized into 4 discrete steps (G-1 through G-4) with individual SHALL instructions at each step. Step G-4 produces a VERIFICATION STATUS record with three separate fill fields (SIG-01 confirmed / SIG-02 confirmed / Role 2 activation cleared), leaving no execution ambiguity.

**Score: 290/290** | All 5 essential PASS

---

### V-05 — Role Sequence + Output Format + Inertia Framing (combined)

**C-01 through C-44:** All PASS — explicit Section C (7-row table with PROHIBITED dropout clause, not declared as identical but written in full); Steps 1A–2H with gate tables; Fields 1–4 in consolidated audit table. Full body written rather than cross-referenced.

**C-45:** PASS. Signal distinction table in Role 1.5 with `Does NOT confirm` column. Non-conflation statement quotes the cell value verbatim: "the 'Does NOT confirm' column value for SIG-01 — 'That Section C annotation count = declared count of 7' — is the authoritative statement that SIG-01 does not cover count verification." Explicit traceability link from prose statement back to the column artifact. Strongest evidence form for C-45 across all variants.

**C-46:** PASS. Role activation chain table at header uses a `Signal chain` column (not "Handoff signal"). SIG-01 and SIG-02 appear as distinct cells in the same column — top-down scannable without column-switching. The column name "Signal chain" frames both signals as members of a sequence rather than individual handoffs. Novel architectural choice that directly exposes the chain structure.

**C-47:** PASS. "BYPASS DEFEAT REGISTER" — named typed table with `Bypass attempt | Attempt type | Structural reason for rejection` columns. One row with attempt type "Looks complete". Register is presented as "extensible by row for additional bypass variants" — this is the only variant that explicitly designs the register for future row addition. Audit Field 5(c) cites the Attempt type cell verbatim.

**C-48:** PASS. "BYPASS REJECTION FIELD" with explicit "structurally unavailable" framing: "The verification table is presented below this field and is structurally unavailable until this field is filled." Two-option form requiring active disambiguation. This is the only variant that uses "structurally unavailable" as the framing (vs "SHALL NOT open" in others) — the strongest assertion that bypass is architecturally impossible.

**Novel elements:**
- **STEP 1A GATE TABLE** and **STEP 1B GATE TABLE** — step gates expressed as 3-column tables (`Gate check | Required | Status`) rather than prose GATE statements, making gate clearance a row-scan task.
- Verbatim cell-quote in non-conflation statement links prose to column artifact explicitly.
- Signal chain column design makes the two-signal sequence visible as a top-down column scan.
- Audit as consolidated table (F-1 through F-5 with sub-items) compresses all compliance checks into one scan artifact.

**Score: 290/290** | All 5 essential PASS

---

## Composite Score Summary

| Variant | C-01–C-05 (ess) | C-06–C-08 (rec) | C-09–C-44 (asp) | C-45 | C-46 | C-47 | C-48 | **Total** |
|---------|-----------------|-----------------|-----------------|------|------|------|------|-----------|
| V-01 | 60 (all PASS) | 30 (all PASS) | 180 (all PASS) | 5 | 5 | 5 | 5 | **290** |
| V-02 | 60 | 30 | 180 | 5 | 5 | 5 | 5 | **290** |
| V-03 | 60 | 30 | 180 | 5 | 5 | 5 | 5 | **290** |
| V-04 | 60 | 30 | 180 | 5 | 5 | 5 | 5 | **290** |
| V-05 | 60 | 30 | 180 | 5 | 5 | 5 | 5 | **290** |

All five variants: 290/290. All 5 essential PASS on all variants.

---

## Ranking

All variants tie at 290/290. Quality ranking based on structural depth:

| Rank | Variant | Differentiator |
|------|---------|----------------|
| 1 | **V-05** | Three-axis combination; "Signal chain" column for top-down scan; verbatim cell-quote anchor; gate-as-table structure; consolidated audit table; "structurally unavailable" bypass framing |
| 2 | **V-04** | SHALL-NOT-activate-if column adds enforcement direction at header; DOES NOT CONFIRM in caps as contract term; G-1/G-2/G-3/G-4 atomized verification; VERIFICATION STATUS multi-field clearance record |
| 3 | **V-02** | Audit Field 5 as structured evidence table (strongest audit form after V-05) |
| 4 | **V-03** | Two-field Phase 1 gate status; lifecycle phase naming adds narrative clarity |
| 5 | **V-01** | Table-first format is clean and minimal but introduces no new structural patterns |

---

## Excellence Signals

From V-05 (top-ranked):

**1. Verbatim cell-quote anchor in non-conflation statement**
The non-conflation statement quotes the "Does NOT confirm" cell value verbatim and identifies it as "the authoritative statement that SIG-01 does not cover count verification." This creates a direct, bidirectional link between the prose enforcement claim and the scannable column artifact. An executor can confirm the prose requirement by looking up the cell; a reviewer can confirm the cell is doing enforcement work by finding it quoted in prose.

**2. Signal-chain column architecture**
Renaming "Handoff signal" → "Signal chain" and placing both SIG-01 and SIG-02 as distinct cells in that column makes the two-signal sequence visible as a single top-down column scan at the prompt header. The column name itself asserts that these two signals form a chain — structural semantics, not just structural layout.

**3. Gate-as-table with Required/Status columns**
Expressing step gates as tables (`Gate check | Required | Status`) rather than prose GATE statements converts gate clearance from a read-and-interpret task to a fill-and-scan task. Each gate condition is a row; clearance is filling the Status column. This parallels the C-48 elevation of bypass rejection from prose to a required-fill field.

From V-04 (second-ranked):

**4. SHALL-NOT-activate-if column in role activation contract**
Adding a `SHALL NOT activate if` column to the header table exposes bypass consequences at the architectural entry point, before any role body. C-46 required the chain to be visible at the header; this pattern adds enforcement weight at the same location. Parallels the C-45→C-46 elevation (visibility → entry-point visibility) for bypass conditions.

**5. Multi-step atomized count verification (G-1/G-2/G-3/G-4)**
Breaking verification into four discrete steps with individual SHALL instructions and a final VERIFICATION STATUS record with three fill fields eliminates ambiguity about where in the verification sequence an executor is. The VERIFICATION STATUS acts as a clearance certificate: all three fields must be filled, and Role 2 activation requires the third field to read CLEARED.

---

```json
{"top_score": 290, "all_essential_pass": true, "new_patterns": ["Gate-as-table: step gates expressed as tables with Required/Status row-per-condition structure rather than prose GATE statements, converting gate clearance from read-and-interpret to fill-and-scan — parallels the C-48 elevation of bypass rejection from named section to required-fill field", "Verbatim cell-quote anchor: the non-conflation statement quotes the Does NOT confirm column cell value verbatim and names it the authoritative statement, creating bidirectional traceability between the prose enforcement claim and the scannable column artifact", "SHALL-NOT-activate-if column at prompt header: a dedicated column in the role activation table exposes bypass consequences (what condition blocks each role) at the architectural entry point before any role body, extending C-46 from signal-chain visibility to enforcement-consequence visibility at the header"]}
```
