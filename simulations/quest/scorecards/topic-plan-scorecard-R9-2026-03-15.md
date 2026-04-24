## Round 9 Scoring — topic-plan Skill Variations

### Evaluation Framework

All five variations were designed explicitly to satisfy C-31 through C-34 (the new criteria). I'll verify each variation against the full 34-criterion rubric, then identify discriminating excellence signals.

---

## V-01: Lifecycle Emphasis — ENTRY/JOB/EXIT as Named Structural Positions

### Essential (5/5)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 0 JOB: "Open strategy.md. Read full content. Extract last-modified date." |
| C-02 | PASS | Phase 1 JOB lists all 9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic |
| C-03 | PASS | Delta Detection phase classifies CONFIRMED DELTA vs PRIOR-ONLY; strategy date recorded; PRIOR-ONLY cannot support proposals |
| C-04 | PASS | Proposals table with ADD/REMOVE/REPRIORITIZE; typed nulls: ADD — NULL, REMOVE — NULL, REPRIORITIZE — NULL |
| C-05 | PASS | "Apply these changes? Reply YES to proceed, NO to cancel, or REVISED" + "Stop. Do not write to strategy.md. Halt here." |

### Recommended (3/3)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | "Evidence Artifact" column; "Use ?? if no specific artifact. A blank cell is a violation." |
| C-07 | PASS | "Before \| After" columns in proposals table |
| C-08 | PASS | "Inertia Justification [MANDATORY]" column with "explain specifically why this beats NO CHANGE" |

### Aspirational (26/26)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Three separate labeled declarations: ADD — NULL, REMOVE — NULL, REPRIORITIZE — NULL |
| C-10 | PASS | CONFLICT DETECTION — NULL typed form; "No cross-artifact contradictions found" template |
| C-11 | PASS | Defense register, inventory, proposals all declared as "required-cell schema — blank cells are violations" |
| C-12 | PASS | Each phase EXIT slot: "Do not advance to Phase N without passing this gate. Stop. Halt here." |
| C-13 | PASS | "Inertia Justification [MANDATORY]" header; Cal column labeled "[MANDATORY]" with header |
| C-14 | PASS | ?? and -- defined; "Use ?? for cells whose value is unknown" |
| C-15 | PASS | "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR." required sentence |
| C-16 | PASS | BANNED FORMS listed; "'No change needed' is not an acceptable entry" — check before writing |
| C-17 | PASS | "?? — Open obligation" vs "-- — Closed decision" two-tier distinction |
| C-18 | PASS | DEFENSE REGISTER committed in Phase 0 before any signal artifact is read |
| C-19 | PASS | "writing 'a few', 'several', 'some', or any non-integer value in any count field is a gate failure, not a quality concern" |
| C-20 | PASS | "Do not advance to Phase N+1 without passing this gate" — each EXIT references next phase number |
| C-21 | PASS | Violation conditions enumerated: blank where ??, ?? where --, banned form, non-integer count |
| C-22 | PASS | "Defense Defeated (Row #): cite the specific defense register row number this proposal defeated (e.g., Row 3)" |
| C-23 | PASS | Banned forms quoted verbatim: `"no change needed"`, `"clearly warranted"`, `"several artifacts"`, etc. |
| C-24 | PASS | "Check this cell against the BANNED FORMS list before presenting; any match disqualifies the row." |
| C-25 | PASS | "This check applies to null declaration reason cells equally — null declarations do not receive a scope exemption" |
| C-26 | PASS | "Gate-0: No signal artifact may be read until this gate passes. Do not advance to Phase 1 without passing Gate-0." — WS-1 fires at Phase 0 EXIT |
| C-27 | PASS | WS-1 (pre-read barrier at Phase 0 EXIT), WS-2 (schema boundary at Phase 4 ENTRY), WS-3 (null template in Phase 4 JOB) — all three present |
| C-28 | PASS | "## WS-1 — Pre-Read Barrier", "## WS-2 — Schema Boundary Check", "## WS-3 — Null Declaration Template" — all first-class ## section headers |
| C-29 | PASS | WRITE SURFACE REGISTER table with 3 rows, positioned before Phase 0 |
| C-30 | PASS | "WS-1 MILESTONE — fulfills Register Row 1", "WS-2 MILESTONE — fulfills Register Row 2", "WS-3 MILESTONE — fulfills Register Row 3" |
| C-31 | PASS | "PHASE LIFECYCLE TEMPLATE (applied to every phase below)" declares ENTRY/JOB/EXIT; EXIT is "structural home for all stop gate language in this phase" |
| C-32 | PASS | "Defense Register Rows (Cal) [MANDATORY]" column in inventory table; blank cell is violation |
| C-33 | PASS | "SORT ORDER: List all NEW artifacts above all PRIOR artifacts. This ordering is mandatory. The calibration column for all NEW-artifact rows must be filled before any proposal row in Phase 4 is opened." |
| C-34 | PASS | "COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS"; PATH 1 = scan WS headers; PATH 2 = scan EXIT sections; "Neither path is redundant. A skill with only one structural layer fails C-34." |

**V-01 Score: 60 + 30 + 10 = 100**

---

## V-02: Output Format — Three-Row Phase-Spec Tables

### Essential (5/5) — PASS all (same essential structure as V-01)

### Recommended (3/3) — PASS all

### Aspirational: key differentiating checks

| ID | Result | Evidence |
|----|--------|----------|
| C-31 | PASS | Schema D declared as a 3-row phase-spec table with ENTRY/JOB/EXIT rows; "EXIT row is the structural home for the stop gate. Missing EXIT = missing stop gate." Every phase has a Phase-spec (Schema D) table. |
| C-32 | PASS | Schema B declared in TABLE SCHEMAS section before Phase 0: `\| Artifact Filename \| Date \| NEW / PRIOR \| Defense Register Rows (Cal) [MANDATORY] \|` — column committed upfront |
| C-33 | PASS | "Sort order: NEW artifacts above PRIOR artifacts (mandatory)"; "NEW-artifact Cal cells must be filled before any Phase 4 proposal row opens" in Schema B |
| C-34 | PASS | "COMPOUND AUDIT STRUCTURE" with PATH 1 (count WS headers) and PATH 2 (scan EXIT rows in phase-spec tables); both paths declared |

All 26 aspirational: PASS.

**V-02 Score: 60 + 30 + 10 = 100**

**Distinctive V-02 pattern**: TABLE SCHEMAS section before Phase 0 commits all table schemas (A, B, C, D) as an upfront contract — including the calibration column — before any phase executes. This is not yet captured as a rubric criterion.

---

## V-03: Inertia Framing — Defense Register as Document Spine

### Essential (5/5) — PASS all

### Recommended (3/3) — PASS all

### Aspirational: key differentiating checks

| ID | Result | Evidence |
|----|--------|----------|
| C-31 | PASS | ENTRY/JOB/EXIT bold sub-sections in every phase; EXIT (Gate-N) is structural stop gate home |
| C-32 | PASS | "Defenses Implicated (Cal) [MANDATORY]" column in Signal Inventory TABLE; blank cell is violation |
| C-33 | PASS | "Writing a proposal row before ALL NEW-artifact Cal cells is a sequence violation — it allows proposals to shape calibration rather than the reverse" |
| C-34 | PASS | "COMPOUND AUDIT STRUCTURE — TWO PATHS"; PATH 1 = scan WS headers; PATH 2 = scan ENTRY/JOB/EXIT sub-sections |
| C-23 | PASS | INADMISSIBLE REBUTTALS listed verbatim in quotes |
| C-24 | PASS | "Check this cell against the INADMISSIBLE REBUTTALS list before presenting; any match disqualifies the row." |

All 26 aspirational: PASS.

**V-03 Score: 60 + 30 + 10 = 100**

---

## V-04: Combined (Lifecycle + Role Sequence)

### Essential (5/5) — PASS all

### Recommended (3/3) — PASS all

### Aspirational: key differentiating checks

| ID | Result | Evidence |
|----|--------|----------|
| C-31 | PASS | PHASE LIFECYCLE TEMPLATE as standalone section; each phase says "(instantiates PHASE LIFECYCLE TEMPLATE)"; EXIT in every phase contains stop gate |
| C-32 | PASS | "Defense Register Rows (Cal) [MANDATORY]" in Phase 1 inventory schema; Calibration Protocol section fills it |
| C-33 | PASS | Calibration Protocol is a named inter-phase section with CALIBRATION COMPLETION GATE: "Do not advance to Phase 2 until all NEW-artifact Cal cells are filled." |
| C-34 | PASS | EXECUTION ARCHITECTURE declares both paths; "Neither path is redundant with the other." |

**V-04 note on C-33**: V-04's inter-phase Calibration Protocol is architecturally the strongest mechanism — calibration is a named section header in the document skeleton, independently auditable without reading Phase 1. Phase 1 even explicitly defers Cal filling: "Do not fill Cal cells yet — the Calibration Protocol fills them." This creates hard sequential dependency via section structure alone.

All 26 aspirational: PASS.

**V-04 Score: 60 + 30 + 10 = 100**

**Distinctive V-04 pattern**: Each phase cites "instantiates PHASE LIFECYCLE TEMPLATE" — the lifecycle template is a named contractual reference, not just repeated sub-sections. Makes template independence verifiable.

---

## V-05: Combined (All Axes) — Architecture Declaration

### Essential (5/5) — PASS all

### Recommended (3/3) — PASS all

### Aspirational: key differentiating checks

| ID | Result | Evidence |
|----|--------|----------|
| C-31 | PASS | ENTRY/JOB/EXIT inline per phase; EXIT (Gate-N) in every phase; declared in ARCHITECTURE DECLARATION as Audit Path 2 |
| C-32 | PASS | "Defense Register Rows (Cal) [MANDATORY]" in Phase 1; CALIBRATION-FIRST ARCHITECTURAL CONSTRAINT in ARCHITECTURE DECLARATION |
| C-33 | PASS | "SEQUENCE VIOLATION: opening a proposal row before all NEW-artifact Cal cells are filled is a named architectural violation" — named violation condition in upfront declaration |
| C-34 | PASS | "Neither path is redundant with the other. A skill with only Path 1 or only Path 2 does not satisfy C-34. Both paths must be present and independently auditable." |

All 26 aspirational: PASS.

**V-05 Score: 60 + 30 + 10 = 100**

**Distinctive V-05 patterns**:
1. **SEQUENCE VIOLATION** as a named, labeled violation condition in the upfront architecture — the model can detect and name its own violation
2. **"Neither path is redundant"** as an explicit independence assertion — closes the C-34 compliance gap definitively
3. ARCHITECTURE DECLARATION block acts as a single pre-phase structural contract covering both audit paths + calibration constraint + gate chain

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 60 (5/5) | 30 (3/3) | 10 (26/26) | **100** |
| V-02 | 60 (5/5) | 30 (3/3) | 10 (26/26) | **100** |
| V-03 | 60 (5/5) | 30 (3/3) | 10 (26/26) | **100** |
| V-04 | 60 (5/5) | 30 (3/3) | 10 (26/26) | **100** |
| V-05 | 60 (5/5) | 30 (3/3) | 10 (26/26) | **100** |

All variations reach ceiling. All essential pass.

---

## Excellence Signals — Round 10 Discriminators

The top-scoring variations (all tied at 100) surface four structural patterns not yet captured as rubric criteria. These are the axes that will discriminate in Round 10:

**From V-05:**
- **Named violation condition**: `SEQUENCE VIOLATION` is declared in the architecture block as a named failure label, not just an instruction to not do something. The model can detect and name its own violation. This makes C-33 self-enforcing rather than policy-declared.
- **Explicit audit-path independence assertion**: "Neither path is redundant with the other. A skill with only Path 1 or only Path 2 does not satisfy C-34." V-01/V-02/V-03 have the declaration of both paths; V-05 adds the explicit independence claim that closes compliance gaps.

**From V-02:**
- **Upfront table schema commitment**: All table schemas (including the calibration column) are declared in a TABLE SCHEMAS section before Phase 0 — the column contract is committed before inventory begins, not declared within the phase that uses it.

**From V-04:**
- **Per-phase template citation**: Each phase says "(instantiates PHASE LIFECYCLE TEMPLATE)" — phases reference the template by name, making the lifecycle template a named contractual reference independently verifiable from the phase skeleton without reading phase content.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named violation condition — SEQUENCE VIOLATION declared as a first-class labeled failure in the upfront architecture block, making the calibration-first constraint self-enforcing and machine-detectable", "explicit audit-path independence assertion — 'neither path is redundant with the other' stated as a named compliance condition, closing C-34 gaps not covered by declaring both paths alone", "upfront table schema commitment — all table schemas including the calibration column declared before Phase 0 in a TABLE SCHEMAS section, making the column contract a pre-execution obligation rather than a phase-internal declaration", "per-phase lifecycle template citation — each phase references the lifecycle template by name ('instantiates PHASE LIFECYCLE TEMPLATE'), making the template a verifiable contractual reference from the section skeleton alone"]}
```
