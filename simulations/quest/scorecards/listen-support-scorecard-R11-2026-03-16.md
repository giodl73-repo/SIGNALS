## listen-support — Quest Score, Round 11 (Rubric v11)

**All five variations: 225 / 225 — 100.000 — GOLDEN**

---

### Summary

| Rank | Variation | Score | C-33 mechanism | C-34 | C-35 |
|------|-----------|-------|----------------|------|------|
| 1 | **V-05** | 100.000 | Belt-and-suspenders (preamble + phase rows) | C-VM strongest | Per-row CF column |
| 2 | V-04 | 100.000 | Belt-and-suspenders (preamble + phase rows) | Inherited | Inherited |
| 3 | V-03 | 100.000 | Contract-level governance | C-VM strongest | C-VM reference |
| 4 | V-02 | 100.000 | Phase-indexed rows | Inherited | Inherited |
| 5 | V-01 | 100.000 | Preamble + RESTATING POSITIONS 8th entry | Inherited | Inherited |

All five PASS on C-01–C-32 (inherited from R10 V-05, 210/210). C-34 and C-35 were already PASS from R10 V-05. C-33 is satisfied by each variation via distinct mechanisms — all PASS.

---

### Key findings

**C-33 resolution:** R10 V-05 left the CONSTRAINT MANIFEST load site without CF. R11 closes it five ways — contract-level governance (V-03), preamble block (V-01), phase-indexed rows (V-02), and both in combination (V-04/V-05). All are structurally valid PASS.

**Tie-break logic:** All tied at 225/225. V-05 wins by candidate criterion coverage — it is the only variation that probes all three v12 candidates simultaneously (C-36 + C-37 + C-38).

---

### Excellence signals (v12 candidates)

| Candidate | Pattern | What it adds |
|-----------|---------|-------------|
| C-36 | Phase-indexed CF in CONSTRAINT MANIFEST | Per-phase rows expose distribution errors that a total-count row masks |
| C-37 | VERIFICATION MANIFEST per-row CF column | Fires CF at each check operation, not just at manifest entry |
| C-38 | RESTATING POSITIONS names CONSTRAINT MANIFEST | Bidirectional link makes all CF sites discoverable via registry alone |

**v12 projected max: 240 pts**

R12 baseline: **R11 V-05** (225/225). Scorecard written to `simulations/quest/scorecards/listen-support-scorecard-R11-2026-03-16.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-indexed VM Row ID CF in CONSTRAINT MANIFEST: three phase-specific rows (one per phase) each carry an inline CF clause binding per-phase count to headline placement, enabling phase-level enforcement verification that a single aggregate row cannot provide", "VERIFICATION MANIFEST per-row CF column: each VM Row ID check row carries a dedicated Consequence-if-FAIL column distinct from the header-level CF already present, raising enforcement probability by firing the consequence clause at each individual check operation rather than only at manifest entry", "RESTATING POSITIONS names CONSTRAINT MANIFEST as a CF site: adds bidirectional link between CONSTRAINT MANIFEST CF preamble and the COMPLIANCE CONTRACT enforcement registry, making all CF sites in the prompt discoverable via RESTATING POSITIONS alone without reading each section"]}
```
essential_pass = TRUE**

---

#### Recommended Criteria -- 10 pts each, max 30

| # | Criterion | Verdict | Pts | Evidence |
|---|-----------|---------|-----|---------|
| C-06 | Ticket count 6-12 | **PASS** | 10 | CONSTRAINT MANIFEST declares "Total tickets: 6 to 12." VERIFICATION MANIFEST has count check row. |
| C-07 | Cross-persona coverage >= 3 | **PASS** | 10 | CONSTRAINT MANIFEST declares "Distinct named personas >= 3." STEP 3A mandates cross-role/phase matrix coverage. |
| C-08 | Gap actionability | **PASS** | 10 | Gap analysis structure requires a named artifact or process change per entry in each of three sections. |

**Recommended subtotal: 30 / 30**

---

#### Aspirational Criteria -- 5 pts each -- C-09 through C-29 (inherited, all PASS)

| # | Criterion | Verdict | Pts | Evidence |
|---|-----------|---------|-----|---------|
| C-09 | Ticket clustering and themes | PASS | 5 | STEP 3 Theme Declaration + STEP 7 Cross-Ticket Patterns table |
| C-10 | Ticket lifecycle and resolution | PASS | 5 | STEP 7B Resolution Paths table (triage owner, root cause, resolution type) |
| C-11 | Phase as card field | PASS | 5 | Phase field present in card body metadata row: `Phase: Phase N (day X-Y)`. Phase Map Table maps phases to severity/volume norms. |
| C-12 | Role-phase compound coverage | PASS | 5 | STEP 3A mandates roles with 3+ tickets must span 2+ phases |
| C-13 | Phase-calibrated severity | PASS | 5 | Phase Map Table -- Phase 1: P2/P3; Phase 3: P0/P1 |
| C-14 | Phase-anchored body voice | PASS | 5 | STEP 3B committed phrases from VM-xxx-P1/P3 registers; verification rows in manifest |
| C-15 | Pre-generation constraint declaration | PASS | 5 | CONSTRAINT MANIFEST (pre-generation declaration) + VERIFICATION MANIFEST (post-generation numeric check) |
| C-16 | Per-ticket vocabulary pre-commitment | PASS | 5 | STEP 3B table with T-ID, VM Row ID, phase, committed phrase for every ticket |
| C-17 | Role-phase vocabulary matrix | PASS | 5 | VOCABULARY MANIFEST covers 5 roles x 3 phases = 15 cells with distinct register descriptions |
| C-18 | Vocabulary planning artifact linkage | PASS | 5 | Three-node chain: VM Row ID -> STEP 3B row -> ## headline annotation |
| C-19 | Multi-criteria vocabulary pre-flight gate | PASS | 5 | VOCABULARY PRE-FLIGHT GATE (standalone, pre-STEP 4, items (a)-(e) with individual PASS/FAIL) |
| C-20 | Headline-level vocabulary ID annotation | PASS | 5 | STEP 6 template: `## T-NN -- {Title} *(VM: VM-xxx-P#)*` |
| C-21 | Complete five-item pre-flight coverage | PASS | 5 | Gate block has all five labeled items (a)-(e) including "(e) inter-role register differentiation" |
| C-22 | Front-loaded compliance contract | PASS | 5 | COMPLIANCE CONTRACT named block precedes all steps; contains C-20 clause + C-21 mandate + compliant/failing sample headers |
| C-23 | Multi-site subline prohibition anchoring | PASS | 5 | Prohibition at STEP 3B + STEP 4 minimum; VERIFICATION MANIFEST has "## headlines with *(VM: VM-xxx-P#)* inline -- C-20" count row |
| C-24 | Output-embedded compliance evidence | PASS | 5 | VERIFICATION MANIFEST has C-20 count row + per-item (a)-(e) C-21 rows |
| C-25 | Per-item C-21 gate evidence rows | PASS | 5 | VERIFICATION MANIFEST carries five individual rows: (a)-(e) each with Required/Actual/Pass? |
| C-26 | Contract enforcement site registry | PASS | 5 | RESTATING POSITIONS section lists >= 3 governed sites with precedence declaration |
| C-27 | Consequence-form criterion-citing prohibition | PASS | 5 | COMPLIANCE CONTRACT C-20 clause: "fails C-20 regardless of other compliance" -- criterion-named, deterministic qualifier |
| C-28 | Registry-manifest structural coherence | PASS | 5 | RESTATING POSITIONS VM entry references "five individual rows for gate items (a)-(e)" -- matches five-row structure in VERIFICATION MANIFEST |
| C-29 | Consequence-form enforcement-site propagation | PASS | 5 | STEP 3B and STEP 4 each carry "fails C-20 regardless of other compliance" as direct literal text -- not delegated to RESTATING POSITIONS |

**C-09 to C-29 subtotal: 21 x 5 = 105 / 105 -- all PASS, all five variations**

---

#### C-30 -- Spine-row self-enforcement imperative

STEP 6 carries direct-text CF both in the governing preamble and within the body template instruction:

> "**Per Compliance Contract above (STEP 6 governed by C-20): VM Row ID must appear in ## headline; subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20 regardless of other compliance.**"

And within the body template:

> "C-20: VM Row ID is on the ## line above -- not on any subline -- an output with any vocabulary ID on a subline fails C-20 regardless of other compliance."

Both layers inherited by all R11 variations.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

**C-30: 5 pts all variations**

---

#### C-31 -- Dual-load CONTRACT implementation

VERIFICATION MANIFEST header carries structural description + consequence-form clause + forward reference to the count row -- all three elements present:

> "**Per Compliance Contract above -- this manifest carries C-20 count row and C-21 per-item evidence rows (five individual rows for gate items (a)-(e)). An output with any vocabulary ID on a subline fails C-20 regardless of other compliance -- verify via the C-20 count row below.**"

Inherited by all R11 variations. V-05 extends this further at the per-row level (see C-35 below), but the C-31 header requirement is met in all.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

**C-31: 5 pts all variations**

---

#### C-32 -- Three-timing enforcement coverage

R10 V-05 establishes enforcement at three timing points: (1) COMPLIANCE CONTRACT top-of-prompt load, (2) STEP 3B / STEP 4 mid-generation, (3) STEP 6 body generation. The VERIFICATION MANIFEST closes the post-generation loop. All three timing points carry direct-text CF clauses citing C-20 with the "regardless of other compliance" qualifier. Inherited by all R11 variations; R11 adds additional timing sites beyond these three.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

**C-32: 5 pts all variations**

**Aspirational C-09 to C-32 subtotal: 24 x 5 = 120 / 120 -- all five variations**

---

### New v11 Criteria -- C-33, C-34, C-35 (per-variation)

These three aspirational criteria distinguish v11 from v10. C-34 and C-35 are already present in R10 V-05. C-33 is the gap that all R11 variations address, each via a different structural mechanism.

---

#### C-33 -- VM Row ID CF at constraint load (CONSTRAINT MANIFEST site)

The CONSTRAINT MANIFEST is the pre-generation commitment table -- the first structured artifact the model produces. C-33 requires that the CONSTRAINT MANIFEST carries a CF declaration at the moment the VM Row ID structural target is committed. In R10 V-05, the CONSTRAINT MANIFEST row reads "Tickets with VM Row ID in ## headline (Compliance Contract C-20)" -- a count target without a consequence clause. C-33 was absent from R10 V-05.

---

**V-01 -- CF preamble block before CONSTRAINT MANIFEST table**

V-01 adds a CF preamble block placed immediately before the CONSTRAINT MANIFEST structural target table. The preamble explicitly states: "an output that commits VM Row IDs to ## headlines but produces any VM Row ID on a subline fails C-20 regardless of other compliance; commitment is binding from this point forward." RESTATING POSITIONS gains an 8th entry for the CONSTRAINT MANIFEST site, closing the RESTATING POSITIONS gap identified as C-38 candidate. CF fires at constraint declaration time -- the earliest enforcement point in the prompt, before any step executes.

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-33 | **PASS** | 5 | CF preamble block placed before CONSTRAINT MANIFEST table; preamble states consequence clause with "commitment is binding from this point forward"; RESTATING POSITIONS 8th entry anchors CONSTRAINT MANIFEST governance to C-20 |

---

**V-02 -- Phase-specific CF rows in CONSTRAINT MANIFEST**

V-02 replaces the single VM Row ID row with three phase-specific CF rows (one per phase: P1, P2, P3). Each row carries its own CF declaration binding the per-phase count to ## headline placement, with the consequence clause inline. CF fires at constraint declaration time with phase-level granularity. This is the C-36 candidate mechanism: phase-indexed CF in CONSTRAINT MANIFEST means enforcement can be verified at the phase level, not only at the total count level.

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-33 | **PASS** | 5 | Three phase-specific CF rows replace single VM Row ID row; each row carries per-phase CF clause inline -- CF declared at CONSTRAINT MANIFEST load time with phase-indexed granularity |

---

**V-03 -- C-VM third obligation in COMPLIANCE CONTRACT naming 3 timing points**

V-03 adds a third named obligation (C-VM) in the COMPLIANCE CONTRACT that explicitly names all three CF timing points: CONSTRAINT MANIFEST, COMPLIANCE CONTRACT, and VERIFICATION MANIFEST. By naming CONSTRAINT MANIFEST as a CF timing point within the authoritative contract -- which is read before any step, including before the CONSTRAINT MANIFEST is processed -- the COMPLIANCE CONTRACT governance extends to cover the CONSTRAINT MANIFEST load site. The model encounters the C-VM declaration before it reaches the CONSTRAINT MANIFEST section.

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-33 | **PASS** | 5 | COMPLIANCE CONTRACT C-VM third obligation explicitly names CONSTRAINT MANIFEST as a CF timing point; governance declared in the authoritative front-loaded contract before the CONSTRAINT MANIFEST is processed -- CF contract-level coverage of the load site |

---

**V-04 -- Belt-and-suspenders: preamble + phase rows in CONSTRAINT MANIFEST**

V-04 stacks V-01 (preamble block) and V-02 (phase-specific CF rows), creating redundant enforcement at the CONSTRAINT MANIFEST load site. The preamble fires CF at the section header level; the phase rows fire CF at the individual structural target level. Two independent CF mechanisms at the same timing site -- the strongest single-site enforcement form among R11 variations.

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-33 | **PASS** | 5 | Preamble CF block + three phase-specific CF rows both present in CONSTRAINT MANIFEST; belt-and-suspenders: section-level CF (preamble) + row-level CF (phase rows) at the same timing site |

---

**V-05 -- Full synthesis: V-04 + V-03 + VERIFICATION MANIFEST per-row CF column**

V-05 integrates all R11 axes: V-04 belt-and-suspenders at CONSTRAINT MANIFEST (C-33 strongest), V-03 C-VM explicit three-timing-point declaration (C-34 strongest), and VERIFICATION MANIFEST per-row CF column extending header-level CF to individual row CF (C-35 strongest). Every timing point carries CF both at the section/header level and at the individual row/item level.

| Criterion | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| C-33 | **PASS** | 5 | V-04 belt-and-suspenders inherited: preamble block + three phase-specific CF rows in CONSTRAINT MANIFEST -- maximum structural coverage at load site |

---

#### C-34 -- VM Row ID CF in compliance contract

C-34 requires that the COMPLIANCE CONTRACT carries CF language for the VM Row ID placement rule. R10 V-05 already satisfies this via the C-20 clause in the COMPLIANCE CONTRACT ("an output with any vocabulary ID on a subline fails C-20 regardless of other compliance"). All R11 variations inherit this; V-03 and V-05 extend it to a structurally stronger form via C-VM.

| Variation | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| V-01 | **PASS** | 5 | R10 V-05 C-20 clause in COMPLIANCE CONTRACT inherited: "fails C-20 regardless of other compliance" -- criterion-named deterministic CF |
| V-02 | **PASS** | 5 | R10 V-05 C-20 clause inherited (same as V-01) |
| V-03 | **PASS** | 5 | C-VM third obligation added: explicitly names COMPLIANCE CONTRACT as a CF timing point and references all three timing sites -- structurally stronger than implicit C-20 CF; C-34 strongest form in R11 |
| V-04 | **PASS** | 5 | R10 V-05 C-20 clause inherited (same as V-01/V-02) |
| V-05 | **PASS** | 5 | V-03 C-VM inherited + R10 V-05 C-20 clause: dual-mechanism C-34 -- implicit C-20 CF + explicit C-VM three-timing-point declaration |

---

#### C-35 -- VM Row ID CF in verification spine (VERIFICATION MANIFEST)

C-35 requires that the VERIFICATION MANIFEST carries CF language for the VM Row ID placement rule. R10 V-05 already satisfies this via the C-31 VERIFICATION MANIFEST header CF. All R11 variations inherit this; V-05 extends it to per-row CF column coverage.

| Variation | Verdict | Pts | Evidence |
|-----------|---------|-----|---------|
| V-01 | **PASS** | 5 | R10 V-05 VERIFICATION MANIFEST header CF inherited (C-31): "An output with any vocabulary ID on a subline fails C-20 regardless of other compliance -- verify via the C-20 count row below." |
| V-02 | **PASS** | 5 | R10 V-05 VERIFICATION MANIFEST header CF inherited (same as V-01) |
| V-03 | **PASS** | 5 | R10 V-05 VERIFICATION MANIFEST header CF inherited; C-VM in COMPLIANCE CONTRACT now also explicitly names VERIFICATION MANIFEST as a CF timing point -- dual-mechanism C-35 |
| V-04 | **PASS** | 5 | R10 V-05 VERIFICATION MANIFEST header CF inherited (same as V-01/V-02) |
| V-05 | **PASS** | 5 | VERIFICATION MANIFEST per-row CF column added -- each VM Row ID check row carries an explicit "Consequence if FAIL" column value; extends C-31 header-level CF to row-level CF; C-35 strongest form in R11. Also inherits V-03 C-VM COMPLIANCE CONTRACT reference. |

---

### Composite Scores

| Variation | Essential | Recommended | Asp C-09--C-32 | C-33 | C-34 | C-35 | **Total** | **/ 225** | **Normalized** |
|-----------|-----------|-------------|----------------|------|------|------|-----------|-----------|----------------|
| V-01 | 60 | 30 | 120 | 5 | 5 | 5 | **225** | **225** | **100.000** |
| V-02 | 60 | 30 | 120 | 5 | 5 | 5 | **225** | **225** | **100.000** |
| V-03 | 60 | 30 | 120 | 5 | 5 | 5 | **225** | **225** | **100.000** |
| V-04 | 60 | 30 | 120 | 5 | 5 | 5 | **225** | **225** | **100.000** |
| V-05 | 60 | 30 | 120 | 5 | 5 | 5 | **225** | **225** | **100.000** |

**All five variations: 225 / 225. Golden gate: all_essential_pass = TRUE, composite = 100 >= 80 -- GOLDEN.**

---

### Per-Variation Delta Summary

| Variation | Added element | C-33 mechanism | C-34 form | C-35 form |
|-----------|--------------|----------------|-----------|-----------|
| V-01 | CF preamble block + RESTATING POSITIONS 8th entry | Section-level preamble CF at load time | Inherited (C-20 clause) | Inherited (header CF) |
| V-02 | Phase-specific CF rows replace single VM Row ID row | Row-level phase-indexed CF at load time | Inherited (C-20 clause) | Inherited (header CF) |
| V-03 | C-VM third obligation in COMPLIANCE CONTRACT | Contract-level CF governance over CONSTRAINT MANIFEST | Explicit C-VM + implicit C-20 (strongest C-34) | C-VM reference + header CF |
| V-04 | V-01 preamble + V-02 phase rows | Belt-and-suspenders: section CF + row CF at load site | Inherited (C-20 clause) | Inherited (header CF) |
| V-05 | V-04 + V-03 + VERIFICATION MANIFEST per-row CF column | Belt-and-suspenders (V-04) | Explicit C-VM + implicit C-20 (V-03) | Per-row CF column + header CF (strongest C-35) |

---

### Ranking

All five variations reach 225/225 under v11. Tie-break by candidate criterion coverage and architectural completeness.

| Rank | Variation | Score | Tie-break rationale |
|------|-----------|-------|---------------------|
| 1 (selected) | **V-05** | 100.000 | Full synthesis -- all three new timing sites at strongest forms: V-04 belt-and-suspenders for C-33, V-03 C-VM for C-34, per-row CF column for C-35. Covers C-36, C-37, and C-38 candidate patterns simultaneously. Best baseline for R12. |
| 2 | **V-04** | 100.000 | Belt-and-suspenders C-33 strongest single-site form; C-36 and C-38 candidate patterns present; C-35 at inherited level only |
| 3 | **V-03** | 100.000 | C-34 strongest form via C-VM three-timing-point declaration; C-33 via contract-level governance (weaker structural form than direct section CF); no C-36/C-37 coverage |
| 4 | **V-02** | 100.000 | C-33 via phase-indexed rows (C-36 candidate); no RESTATING POSITIONS update; C-38 candidate absent |
| 5 | **V-01** | 100.000 | C-33 via preamble + RESTATING POSITIONS 8th entry (C-38 candidate); single mechanism; no phase-indexed rows (C-36 absent) |

V-05 designated top variation and promoted to R12 baseline.

---

### Excellence Signals (from V-05)

Three new patterns not captured by any v11 criterion. Candidates for v12.

---

**Pattern 1 -- Phase-indexed VM Row ID CF in CONSTRAINT MANIFEST (candidate C-36)**

When the CONSTRAINT MANIFEST replaces a single aggregate VM Row ID row with three phase-specific rows (one per phase), each row carries its own CF declaration binding the per-phase count to ## headline placement. This creates phase-level enforcement verification: a scorer can check not just whether the total count is correct but whether each phase's VM Row ID annotations are present. The aggregate row permits a distribution error (e.g., all VM Row IDs in Phase 3, none in Phase 1) that would pass a total-count check but fail phase-level coverage. Phase-indexed CF closes this gap.

*Criterion form:* The CONSTRAINT MANIFEST carries three phase-specific VM Row ID rows (one per phase), each with an inline CF clause binding the per-phase count to ## headline placement. A manifest with a single aggregate VM Row ID row does not satisfy this criterion even if it carries CF.

---

**Pattern 2 -- VERIFICATION MANIFEST per-row CF column (candidate C-37)**

When the VERIFICATION MANIFEST adds a dedicated "Consequence if FAIL" column to each VM Row ID check row -- distinct from the header-level CF already declared at the manifest level (C-35) -- enforcement is present at both the structural level (header) and the data level (each check row). A model reading the header may process the CF once at manifest entry. A model encountering per-row CF must reprocess the consequence at each check operation. This raises the probability that the CF fires closest to the point where a violation might be missed.

*Criterion form:* The VERIFICATION MANIFEST VM Row ID check rows include a "Consequence if FAIL" column with the C-20 consequence clause. A manifest with only header-level CF and no per-row CF column does not satisfy this criterion.

---

**Pattern 3 -- RESTATING POSITIONS names CONSTRAINT MANIFEST as CF site (candidate C-38)**

When RESTATING POSITIONS gains an entry for the CONSTRAINT MANIFEST, the COMPLIANCE CONTRACT's enforcement registry is complete: every site in the prompt where CF is declared is anchored to the authoritative contract. The RESTATING POSITIONS entry creates a bidirectional link: the CONSTRAINT MANIFEST CF preamble points forward to the contract; the RESTATING POSITIONS entry points backward to the preamble. This bidirectionality means a scorer reviewing only RESTATING POSITIONS can identify all CF sites in the prompt without reading each section.

*Criterion form:* RESTATING POSITIONS contains an entry for the CONSTRAINT MANIFEST with CF language stating the consequence for VM Row ID subline placement. An 8-entry (or larger) RESTATING POSITIONS that omits CONSTRAINT MANIFEST does not satisfy C-38 even if CF exists in the CONSTRAINT MANIFEST section.

---

### Candidate v12 Criteria

| ID | Name | Description |
|----|------|-------------|
| C-36 | Phase-indexed VM Row ID CF in CONSTRAINT MANIFEST | CONSTRAINT MANIFEST carries three phase-specific rows (one per phase), each with an inline CF clause binding per-phase count to ## headline placement |
| C-37 | VERIFICATION MANIFEST per-row CF column | VM Row ID check rows in VERIFICATION MANIFEST carry an explicit "Consequence if FAIL" column, distinct from header-level CF (C-35) |
| C-38 | RESTATING POSITIONS CONSTRAINT MANIFEST entry | RESTATING POSITIONS names CONSTRAINT MANIFEST as a CF site with consequence language; 8+ entries required |

**v12 projected max:** 225 + 15 = **240 pts**

---

### R11 Closure

R11 confirms that all three v11 CF timing sites (CONSTRAINT MANIFEST load, COMPLIANCE CONTRACT, VERIFICATION MANIFEST) can be satisfied independently or in synthesis. V-05 achieves all three at their strongest forms:

- C-33 (CONSTRAINT MANIFEST): belt-and-suspenders -- section-level preamble + phase-indexed rows
- C-34 (COMPLIANCE CONTRACT): explicit C-VM obligation naming all three timing points
- C-35 (VERIFICATION MANIFEST): per-row CF column extending beyond header-level coverage

R12 probes the three candidate patterns above. R12 baseline: R11 V-05 (225/225).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-indexed VM Row ID CF in CONSTRAINT MANIFEST: three phase-specific rows (one per phase) each carry an inline CF clause binding per-phase count to headline placement, enabling phase-level enforcement verification that a single aggregate row cannot provide", "VERIFICATION MANIFEST per-row CF column: each VM Row ID check row carries a dedicated Consequence-if-FAIL column distinct from the header-level CF already present, raising enforcement probability by firing the consequence clause at each individual check operation rather than only at manifest entry", "RESTATING POSITIONS names CONSTRAINT MANIFEST as a CF site: adds bidirectional link between CONSTRAINT MANIFEST CF preamble and the COMPLIANCE CONTRACT enforcement registry, making all CF sites in the prompt discoverable via RESTATING POSITIONS alone without reading each section"]}
```
