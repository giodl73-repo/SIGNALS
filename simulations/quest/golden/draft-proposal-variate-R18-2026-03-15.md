# draft-proposal Variate — Round 18

Rubric version: v18 · Formula: (E/4×60) + (R/3×30) + (A/38×10) · New criteria: C-44
(T-40 CONDITION exemplar includes explanation of why quoted deficient T-38 form is abstract),
C-45 (T-42 CONDITION carries inline exemplar of a deficient T-40 CONDITION form)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: T-40 and T-42 CONDITION both abstract (lifecycle emphasis — amendment table spec
  gives no exemplar content guidance for T-40 or T-42; LLM mirrors abstract form) — designed
  fail: C-42 → C-43 → C-44 cascade (C-42 FAIL because T-40 CONDITION names the deficiency
  category without quoting a deficient T-38 CONDITION form; C-43 and C-44 cascade from C-42
  FAIL deterministically) + C-45 (T-42 CONDITION abstract, no exemplar of deficient T-40
  form produced)
- **V-02**: T-40 CONDITION exemplar-guided but no explanation-of-abstractness directive and no
  prescription directive, T-42 abstract (output format — spec provides "quote deficient T-38
  form" instruction but no "explain why it is abstract" and no "show passing T-38 CONDITION"
  instruction; LLM stops at exemplar) — designed fail: C-44 only (independent — C-42 PASS,
  C-44 FAIL), C-43 FAIL (no prescription guidance produced), C-45 FAIL (T-42 abstract)
- **V-03**: T-40 fully documented (both exemplar+explanation and prescription), T-42 abstract
  (phrasing register — T-40 CONDITION spec is maximally explicit with labeled parts; T-42 spec
  uses abstract-only category language) — designed fail: C-45 only (C-42 PASS; C-43 PASS;
  C-44 PASS; T-42 CONDITION names condition without quoting deficient T-40 form → C-45 FAIL)
- **V-04**: Stale T-24 row-count check (43 not 45) + T-40 exemplar-only + T-42 exemplar-guided
  (lifecycle emphasis + output format — v17-era amendment table spec carried forward without
  T-44/T-45 additions; T-40 gets exemplar direction but no explanation-of-abstractness or
  prescription; T-42 gets exemplar direction) — designed fail: C-24 FAIL (43 rows ≠ 45),
  C-44 FAIL (independent — exemplar present without explanation), C-43 FAIL (no prescription
  guidance)
- **V-05**: C-23 cascade root (phrasing register + cascade propagation — Phase 2 RISK template
  instructs inline P×I instead of [R-NN pending]; Phase 9b absent from spec; T-40 and T-42
  abstract) — designed fail: maximum cascade path under v18 (C-23 FAIL → C-26 + C-31..C-43;
  C-42 FAIL → C-44 cascade; C-45 FAIL independent; 17 total fails)

Predicted scores:
- V-01 → 34/38 → **98.95**
- V-02 → 35/38 → **99.21**
- V-03 → 37/38 → **99.74**
- V-04 → 35/38 → **99.21**
- V-05 → 21/38 → **95.53**

---

## V-01 — C-42+C-43+C-44+C-45 Cascade | Axis: Lifecycle Emphasis (T-40 and T-42 CONDITION Abstract) | Designed fail: C-42 → C-43 → C-44 cascade + C-45

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides abstract CONDITION descriptions
for both T-40 and T-42 — naming the deficiency category without quoting any deficient exemplar
form — the LLM mirrors that abstract form in its output. T-40 CONDITION will read "fires if
Phase 9b Domain 2 per-column enumeration lacks 'Risk row:' anchor prefix" — a category
statement with no quoted T-38 form. C-42 FAIL fires. C-43 FAIL and C-44 FAIL cascade
deterministically from C-42 FAIL. T-42 CONDITION will read "fires if T-40 CONDITION lacks
inline failure exemplar" — abstract, no quoted T-40 deficient form. C-45 FAIL. T-44 and T-45
rows exist in the table (45 rows total, C-24 PASS) but their CONDITION fields are also abstract.
All other 34 A-tier criteria PASS. Score: 34/38 → **98.95**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 45)
All other triggers T-01..T-45 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor, labeled
`do-nothing`. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix — it is the incumbent state that wins by default; active
options must demonstrate sufficient advantage over the inertia competitor to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix — "Domain N —" form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                             [R-NN pending] → [R-NN entries] transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                             compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix before the column list)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-02 — C-44+C-43+C-45 Independent | Axis: Output Format (T-40 Exemplar-Only, T-42 Abstract) | Designed fail: C-44 (independent), C-43, C-45

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides an exemplar-quoting directive
for T-40 CONDITION ("quote the deficient T-38 form") but no explanation-of-abstractness
directive and no prescription directive, the LLM quotes the deficient T-38 form (C-42 PASS)
and stops. The output reads: "fires if T-38 CONDITION lacks an inline failure exemplar" — the
form is quoted, but no explanation of WHY it is abstract appears alongside it. C-44 FAIL
(independent: C-42 PASS does not guarantee C-44 PASS). Without a prescription directive,
T-40 CONDITION also lacks the correct-format guidance — C-43 FAIL. T-42 receives only an
abstract description in the spec; it produces an abstract CONDITION — C-45 FAIL. Three
independent fails, no cascade. Score: 35/38 → **99.21**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 45)
All other triggers T-01..T-45 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor, labeled
`do-nothing`. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor — it is the incumbent state that wins by default; active options must
demonstrate sufficient advantage to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix — "Domain N —" form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                             [R-NN pending] → [R-NN entries] transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                             compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix before the column list.
                             CONDITION must quote the deficient T-38 CONDITION form that
                             fires T-40 — a T-38 CONDITION that names the per-site condition
                             without quoting a deficient per-site entry. Example: "fires if
                             T-38 CONDITION lacks an inline failure exemplar")
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-03 — C-45 Isolated | Axis: Phrasing Register (T-40 Fully Documented, T-42 Abstract) | Designed fail: C-45 only

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION fully documents the T-40 CONDITION
requirement — providing an explicit two-part structure with a labeled Part 1 exemplar that
includes the explanation-of-abstractness phrase, and a labeled Part 2 prescription — the LLM
produces a T-40 CONDITION that satisfies C-42, C-43, and C-44. The designed fail is isolated
to T-42: the spec gives T-42 only an abstract description ("fires if T-40 CONDITION lacks
inline failure exemplar of a deficient T-38 CONDITION form") without directing the LLM to
quote a deficient T-40 CONDITION form inside T-42's CONDITION cell. The LLM mirrors the
abstract form. C-45 FAIL is the sole aspirational fail. Score: 37/38 → **99.74**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 45)
All other triggers T-01..T-45 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor, labeled
`do-nothing`. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor — it is the incumbent state that wins by default; active options must
demonstrate sufficient advantage to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix — "Domain N —" form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                             [R-NN pending] → [R-NN entries] transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                             compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix before the column list.
                             CONDITION must carry two required parts:
                             Part 1 — inline exemplar of a deficient T-38 CONDITION form
                             WITH explanation of why it is abstract. Required form:
                             "fires if T-38 CONDITION lacks an inline failure exemplar
                             — abstract: names the condition without quoting what a
                             deficient T-37 CONDITION entry looks like"
                             Part 2 — correct-format prescription showing what a passing
                             T-38 CONDITION entry looks like. Required form:
                             "passing T-38 CONDITION quotes the deficient T-37 form,
                             e.g., 'row-level confirmation fires T-37 — abstract: names
                             the confirmation type without quoting a deficient per-site
                             entry'")
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-04 — C-24+C-44+C-43 Multi-Fail | Axis: Lifecycle Emphasis + Output Format (Stale Row Count, T-40 Exemplar-Only, T-42 Exemplar-Guided) | Designed fail: C-24, C-44 (independent), C-43

**Hypothesis**: A v17-era skill prompt carried forward without updating the T-24 row-count
check (still says "!= 43") builds a 43-row amendment table — T-44 and T-45 rows absent.
Under v18, 43 rows fails C-24 at PRE-DOCUMENT (needs 45). The stale coverage table spec
(C-01..C-43) omits rows for C-44 and C-45. The T-40 CONDITION receives exemplar-quoting
direction (C-42 PASS) but no explanation-of-abstractness directive (C-44 FAIL, independent)
and no prescription directive (C-43 FAIL, independent). T-42 receives explicit exemplar
direction ("quote a deficient T-40 CONDITION form") → C-45 PASS. Three independent fails:
C-24 (structural), C-44 (exemplar without explanation), C-43 (prescription absent).
Score: 35/38 → **99.21**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-43 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 43)
All other triggers T-01..T-43 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor, labeled
`do-nothing`. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor — it is the incumbent state that wins by default; active options must
demonstrate sufficient advantage to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-43.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix — "Domain N —" form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                             [R-NN pending] → [R-NN entries] transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                             compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix before the column list.
                             CONDITION must quote the deficient T-38 CONDITION form that
                             fires T-40. Example: "fires if T-38 CONDITION lacks an inline
                             failure exemplar")
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like.
                             CONDITION must quote a deficient T-40 CONDITION form, e.g.:
                             "fires if Phase 9b Domain 2 per-column enumeration lacks
                             'Risk row:' anchor prefix — abstract: names the anchor-prefix
                             condition without quoting what a deficient T-38 CONDITION
                             entry looks like")
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-05 — C-23 Cascade Root | Axis: Phrasing Register + Cascade Propagation (Inline P×I, No Phase 9b, T-40/T-42 Abstract) | Designed fail: C-23 + C-26 + C-31..C-43 + C-44 + C-45 = 17 fails

**Hypothesis**: When Phase 2 RISK template instructs inline P×I computation (no [R-NN pending]
placeholder) and Phase 9b is absent from the spec, the LLM produces RISK fields with computed
scores rather than register linkage. C-23 FAIL is the cascade root. The document has no
Phase 9b: all Phase 9b-dependent criteria fail (C-26, C-31..C-37). The T-37..T-40 trigger
rows in the amendment table have no exemplar guidance — abstract CONDITION entries throughout
— so C-38..C-43 fail. C-42 FAIL → C-44 FAIL cascade. C-45 FAIL (T-42 abstract). Under v18,
the cascade chain is two criteria longer than v17 (C-44 and C-45 are new links). 45-row table
(T-44 and T-45 present but abstract) keeps C-24 PASS. Total: 17 aspirational fails, 21 pass.
Score: 21/38 → **95.53**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 45)
All other triggers T-01..T-45 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor, labeled
`do-nothing`. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Assess adoption risk (PM) and technical risk (Architect). Assign P (1-5) and I
        (1-5) per risk factor. Compute P×I inline.
        Example: "Adoption friction: P:3 × I:4 = 12 (PM); Integration cost: P:2 × I:3 = 6
        (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor — it is the incumbent state that wins by default; active options must
demonstrate sufficient advantage to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (P×I scores),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its P×I score and describe the inertia impact. Structure each
entry:
  [inertia risk name, P:N × I:N = P×I]: [inertia impact description]

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, assumption register has at least 2 A-NN
entries, phases appear in declared sequence. Reference each option by its Phase 2 label
verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix — "Domain N —" form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                             [R-NN pending] → [R-NN entries] transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                             compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix before the column list)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```
