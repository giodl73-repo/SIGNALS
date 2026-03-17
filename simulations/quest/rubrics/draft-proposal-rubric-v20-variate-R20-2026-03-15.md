# draft-proposal Variate — Round 20

Rubric version: v20 · Formula: (E/4×60) + (R/3×30) + (A/44×10) · New criteria: C-50 (Phase
4b entry canonical bracket form — `[R-NN] — [name, P×I]: [description]` required; fires T-50
when R-NN identifiers present but bracket delimiters, em-dash separator, or inline P×I position
violated), C-51 (Phase 4 explicit inertia-competitor declaration form — "inertia competitor" or
"inertia vector" language required when Phase 4b is present; implicit comparative framing alone
fires T-51; vacuously satisfied when no Phase 4b exists)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Phrasing register — Phase 4 implicit-only inertia framing (do-nothing framed as
  "current-state baseline" and "default outcome" in Phase 4 without explicit "inertia competitor"
  or "inertia vector" declaration; Phase 4b present with canonical `[R-NN] — [name, P×I]:
  [description]` format; PM-first Phase 9; Phase 2 labels verbatim) — designed fail: C-51 only
  (C-48 PASS — Phase 4b structurally present; C-49 PASS — R-NN identifiers in Phase 4b; C-50
  PASS — canonical bracket form intact; C-46 PASS; C-47 PASS; C-41 PASS)
- **V-02**: Output format — Phase 4b non-canonical bracket form (Phase 4 uses explicit "inertia
  competitor" declaration satisfying C-51; Phase 4b present and R-NN identifiers present
  satisfying C-49; Phase 4b entries use `R-NN (P×I = N×N) — name: description` placing P×I
  before the name and outside brackets, violating C-50) — designed fail: C-50 only (C-48 PASS;
  C-49 PASS — R-NN identifiers present; C-51 PASS — explicit "inertia competitor" in Phase 4;
  C-46 PASS; C-47 PASS; C-41 PASS)
- **V-03**: Lifecycle emphasis — full inertia compliance with C-41 designed failure (do-nothing
  explicitly declared inertia competitor in Phase 4; Phase 4b present with R-NN citations in
  canonical bracket form; PM-first Phase 9; verbatim labels; Domain 1 after-state uses P×I scores
  only, omitting R-NN pairing) — designed fail: C-41 only (C-48 PASS; C-49 PASS; C-50 PASS;
  C-51 PASS; C-46 PASS; C-47 PASS; C-41 FAIL isolated to Domain 1)
- **V-04**: Inertia framing + lifecycle — inertia competitor designated in Phase 4, Phase 4b
  absent (Phase 4 explicitly designates do-nothing as "active inertia competitor"; Phase 4b
  structural section omitted entirely; Phase 9b Domain 1 uses full R-NN compound; PM-first;
  verbatim labels) — designed fail: C-48 cascade to C-49 + C-50 + C-51 (four fails; C-41 PASS;
  C-46 PASS; C-47 PASS; C-48 FAIL — Phase 4b absent; C-49/C-50/C-51 FAIL via cascade)
- **V-05**: PM-only role + compressed lifecycle — C-23 cascade (no R-NN linkage declared, no
  [R-NN pending] placeholders, no Phase 9b, no Phase 4b; cascades through 23 fails: C-23 →
  C-26 → C-31..C-37 → C-38..C-47 → C-48 → C-49 → C-50 → C-51) — designed fail: 23 fails

## Predicted score summary

| Variation | Axis | Open triggers | A/44 | Composite |
|-----------|------|---------------|------|-----------|
| V-01 | Phrasing register — implicit inertia declaration | T-51 | 43/44 | **99.77** |
| V-02 | Output format — non-canonical Phase 4b bracket form | T-50 | 43/44 | **99.77** |
| V-03 | Lifecycle emphasis — canonical Phase 4b, P×I-only Domain 1 | T-41 | 43/44 | **99.77** |
| V-04 | Inertia framing + lifecycle — Phase 4b absent cascade | T-48, T-49, T-50, T-51 | 40/44 | **99.09** |
| V-05 | PM-only + compressed lifecycle — C-23 cascade | 23 fails | 21/44 | **94.77** |

**C-50 and C-51 isolation evidence:**

V-01: Phase 4b is present and in canonical `[R-NN] — [name, P×I]: [description]` form (C-50
PASS). Phase 4's implicit framing — "current-state baseline," "default outcome if no action is
taken" — satisfies the semantic trigger condition for Phase 4b without using the prescribed
declaration vocabulary (C-51 FAIL). The failure is isolated: all 43 other criteria pass.

V-02: Phase 4 uses explicit "inertia competitor" declaration (C-51 PASS). Phase 4b is present
(C-48 PASS) and its entries carry R-NN identifiers (C-49 PASS). The bracket structure is
`R-NN (P×I = N×N) — name: description` — R-NN present, but P×I placed before the name and
without square brackets, violating the canonical form (C-50 FAIL). The failure is isolated.

V-03: Both C-50 and C-51 pass fully. Phase 4 uses "inertia competitor" declaration; Phase 4b
entries carry `[R-NN] — [name, P×I]: [description]` form. The designed failure is C-41 (Domain
1 per-site after-state omits R-NN pairing — P×I scores only), orthogonal to Phase 4b discipline.

V-04: Phase 4b absent cascades C-48 FAIL → C-49 FAIL → C-50 FAIL → C-51 FAIL. Four fails from
one structural omission; the cascade is strictly sequential.

V-05: C-50 and C-51 fall at the tail of the 23-fail v20 cascade path. The v20 extension adds two
fails to R19's 21-fail chain without introducing a new root — C-50 cascades from C-49; C-51
cascades from C-48; both absorb into the pre-existing Domain 2 / Phase 4b sub-chain.

---

## V-01 — Phase 4 Implicit-Only Inertia Framing | Axis: Phrasing Register | Designed fail: C-51 only

**Hypothesis**: A variation that frames do-nothing in Phase 4 as "the current-state baseline" and
"default outcome if no action is taken" — without using "inertia competitor" or "inertia vector"
vocabulary — while maintaining a structurally present Phase 4b with canonical `[R-NN] — [name,
P×I]: [description]` entry format will fail C-51 only. Phase 4's implicit framing satisfies the
semantic trigger condition (Phase 4b required and present, C-48 PASS), the Phase 4b entries carry
R-NN identifiers (C-49 PASS), and those entries follow the canonical bracket structure (C-50 PASS).
The sole deficit is the missing explicit declaration vocabulary in Phase 4, which C-51 governs.
PM-first Phase 9 (C-46 PASS). Phase 2 labels propagate verbatim into Domain 2 (C-47 PASS).
Domain 1 after-state pairs R-NN with P×I (C-41 PASS). One open trigger: T-51. Score: 43/44 → 99.77.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, inertia analysis framing, comparison matrix,
  and recommendation. Runs first in every phase.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) as a typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-51 — one per v20 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
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
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration lacks "Risk row:" anchor
                               prefix before the column list)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator — [Option-X: R-NN IDs] form fires T-42)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form — bare `row:` prefix fires T-43)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9 — PM output must appear first)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)
  T-50 PHASE = FINALIZATION  (fires if Phase 4b entries carry R-NN identifiers but not in
                               canonical bracket form `[R-NN] — [name, P×I]: [description]` —
                               forms like `R-NN (P×I = N×N) — name: description` pass T-49
                               but fire T-50; bracket delimiters, em-dash separator, and inline
                               P×I position are all required)
  T-51 PHASE = FINALIZATION  (fires if Phase 4b is present but Phase 4's do-nothing designation
                               uses only implicit comparative language — "current-state baseline,"
                               "preserves current state," "default outcome," "status quo
                               alternative" without explicit "inertia competitor" / "inertia
                               vector" declaration fires T-51; vacuous when Phase 4b is absent)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context, the
forcing function making this decision necessary now, and what the default outcome costs
the team if no deliberate choice is made.

Architect: Confirm the problem statement is technically grounded and scope is bounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be the do-nothing option. For each option,
produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: the labels declared here (Option-A, Option-B, do-nothing) are the
canonical labels for this document. Use them unchanged in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
articulates what the default outcome would be.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies specifically to the do-nothing option (opportunity cost, technical debt
accumulation, competitive erosion). Assign P and I scores on a 1-5 scale. Compute P×I.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing.
The do-nothing column represents the current-state baseline — the lowest-cost path that
preserves existing workflows without new integration investment. It is the default outcome
if no decision is reached; the comparison matrix must show whether active options provide
sufficient advantage over this default.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Structure each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Address:
- What does the do-nothing option preserve over the short term?
- What does it forfeit at 6-month and 12-month horizons?
- Under what conditions does this default path remain acceptable?

Every inertia risk entry must carry an R-NN identifier cross-referencing the main risk
register, enclosed in square brackets, followed by an em-dash, the risk name with P×I
score inline, a colon, and the description. Do not express inertia risks as P×I scores
only — the R-NN pairing and canonical bracket structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries including at least one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, phases appear in declared sequence. Reference each option by
its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-51.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State whether the recommended option provides sufficient
advantage over the current-state default to justify the transition cost.

Architect: Confirm technical feasibility of the recommended option. State which options
are technically viable given the risk register findings.

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

Trigger rules T-01..T-51 — exactly 51 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-41 PHASE = FINALIZATION  (fires if Domain 1 after-state omits R-NN pairing — P×I only)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is the default competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

**Scoring trace:**
- E-04 PASS (recommendation produced with default-outcome comparison)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-41 PASS (Domain 1 after-state pairs R-NN with P×I)
- C-42 PASS (`column:` designator in every Domain 2 bracket)
- C-43 PASS (compound `Risk row:` prefix)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present in Domain 2)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-48 PASS (Phase 4b structurally present — the implicit framing satisfies the semantic gate)
- C-49 PASS (Phase 4b entries carry R-NN identifiers in bracket form)
- C-50 PASS (Phase 4b entries follow canonical `[R-NN] — [name, P×I]: [description]` format)
- C-51 FAIL (T-51 fires — Phase 4b present but Phase 4's do-nothing designation used only
  "current-state baseline" and "default outcome" language; no "inertia competitor" or "inertia
  vector" declaration in Phase 4)
- Score: 43/44 → **99.77**

---

## V-02 — Phase 4b Non-Canonical Entry Format | Axis: Output Format | Designed fail: C-50 only

**Hypothesis**: A variation that uses explicit "inertia competitor" declaration in Phase 4
(satisfying C-51) while expressing Phase 4b inertia risk entries in the form `R-NN (P×I =
N×N) — name: description` — placing P×I before the name and outside square brackets — will
fail C-50 only. The R-NN identifier is present (C-49 PASS), but the bracket delimiters, P×I
inline position, and em-dash separator discipline required by C-50 are violated. Phase 4b
presence satisfies C-48. PM-first Phase 9 (C-46 PASS). Phase 2 labels verbatim in Domain 2
(C-47 PASS). Domain 1 after-state pairs R-NN with P×I (C-41 PASS). One open trigger: T-50.
Score: 43/44 → 99.77.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, inertia competitor analysis, comparison
  matrix, and recommendation. Runs first in every phase.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation.

INERTIA COMPETITOR DESIGNATION: The do-nothing option is designated the active inertia
competitor for this proposal. It represents the incumbent state that prevails if no
deliberate choice is made. The comparison matrix and Phase 9 recommendation must address
whether the recommended option beats the inertia competitor and on which dimensions.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia competitor designation as
a typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-51 — one per v20 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
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
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration lacks "Risk row:" anchor
                               prefix before the column list)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)
  T-50 PHASE = FINALIZATION  (fires if Phase 4b entries carry R-NN identifiers but not in
                               canonical bracket form `[R-NN] — [name, P×I]: [description]` —
                               forms like `R-NN (P×I = N×N) — name: description` pass T-49
                               but fire T-50; bracket delimiters, em-dash separator, and inline
                               P×I position are all required)
  T-51 PHASE = FINALIZATION  (fires if Phase 4b is present but Phase 4's do-nothing designation
                               uses only implicit comparative language without explicit "inertia
                               competitor" / "inertia vector" declaration)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

Architect: Confirm the problem statement is technically grounded and scope is bounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be the do-nothing option, designated as the
inertia competitor. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the inertia competitor
option carries plausible rationale, not a straw-man dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
inertia risk that applies specifically to the do-nothing option. Assign P and I scores
on a 1-5 scale. Compute P×I compound score.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix header note — it is the incumbent state against which
active options must demonstrate sufficient advantage to justify commitment cost.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Express each inertia risk entry in the following format:
  R-NN (P×I = N×N) — [inertia risk name]: [inertia impact description]

Address:
- What does the inertia competitor preserve in the near term?
- What does it forfeit at 6-month and 12-month horizons?
- Under what conditions does the inertia competitor remain a valid choice?

Every inertia risk entry must carry an R-NN identifier cross-referencing the main risk
register. Do not express inertia risks as P×I scores only — the R-NN identifier is required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations, phases appear in declared sequence. Reference each option by its Phase 2 label.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-51.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State explicitly whether the recommendation beats the
inertia competitor and on what basis.

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

Trigger rules T-01..T-51 — exactly 51 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-41 PHASE = FINALIZATION  (fires if Domain 1 after-state omits R-NN pairing — P×I only)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

**Scoring trace:**
- E-04 PASS (recommendation produced with explicit inertia comparison)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-41 PASS (Domain 1 after-state pairs R-NN with P×I)
- C-42 PASS (`column:` designator in every Domain 2 bracket)
- C-43 PASS (compound `Risk row:` prefix)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present in Domain 2)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-48 PASS (Phase 4b structurally present — [GATE: C-48] in phase header)
- C-49 PASS (Phase 4b entries carry R-NN identifiers — `R-NN (P×I = N×N) — name: description`
  form has R-NN present)
- C-50 FAIL (T-50 fires — `R-NN (P×I = N×N) — name: description` violates canonical bracket
  form: R-NN identifier not enclosed in square brackets; P×I placed before name outside
  bracket rather than inline after em-dash separator; `[R-NN] — [name, P×I]: [description]`
  form required but not produced)
- C-51 PASS (Phase 4 uses explicit "inertia competitor" declaration in matrix header note)
- Score: 43/44 → **99.77**

---

## V-03 — Full Inertia-Lifecycle Compliance | Axis: Lifecycle Emphasis | Designed fail: C-41 only

**Hypothesis**: A variation that satisfies both C-50 (canonical Phase 4b entry format) and C-51
(explicit "inertia competitor" declaration in Phase 4) while deliberately producing Domain 1
per-site after-states with P×I scores only — omitting R-NN pairing — will fail C-41 only. The
C-50 and C-51 compliance is confirmed by the Phase 4b entries using the full canonical bracket
form `[R-NN] — [name, P×I]: [description]` and Phase 4 using "inertia competitor" language.
The C-41 failure is isolated to Phase 9b Domain 1 and does not propagate to Phase 4b. PM-first
Phase 9 (C-46 PASS). Phase 2 labels verbatim (C-47 PASS). One open trigger: T-41. Score: 43/44
→ 99.77.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, inertia competitor analysis, comparison
  matrix, and recommendation. Runs first in every phase. PM gives the do-nothing option
  equal analytical weight as the inertia competitor — not a straw man.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation.

INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken. Every
analysis section must address why the inertia competitor is or is not adequate. The
recommendation must explicitly state whether it beats the inertia competitor and on which
dimensions.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-51 — one per v20 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
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
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration lacks "Risk row:" anchor
                               prefix before the column list)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)
  T-50 PHASE = FINALIZATION  (fires if Phase 4b entries carry R-NN identifiers but not in
                               canonical bracket form `[R-NN] — [name, P×I]: [description]` —
                               bracket delimiters, em-dash separator, and inline P×I position
                               are all required)
  T-51 PHASE = FINALIZATION  (fires if Phase 4b is present but Phase 4's do-nothing designation
                               uses only implicit comparative language without explicit "inertia
                               competitor" / "inertia vector" declaration)

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

  For the do-nothing option specifically, RATIONALE must articulate the inertia case:
  why is the status quo a legitimate choice? What conditions would make it the right answer?

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on a 1-5 scale. Compute P×I.
PM: Add at least one adoption or schedule risk entry.

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

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Structure each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Address:
- What does the inertia competitor preserve?
- What does it forfeit over 6 months? 12 months?
- Under what conditions does the inertia competitor remain valid?

Every inertia risk entry must carry an R-NN identifier enclosed in square brackets, followed
by an em-dash, the risk name with P×I score inline, a colon, and the description. Do not
express inertia risks as P×I scores only — the R-NN pairing and canonical bracket structure
are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations in canonical bracket form, phases appear in declared sequence. Reference each
option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-51.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → P×I scores for applicable risks
    [Option-B] RISK field: [R-NN pending] → P×I scores for applicable risks
    [do-nothing] RISK field: [R-NN pending] → P×I scores for applicable risks, including
                              inertia risks unique to this option
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each Domain 2 column entry.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State explicitly whether the recommendation beats the
inertia competitor and on what basis.

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

Trigger rules T-01..T-51 — exactly 51 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-41 PHASE = FINALIZATION  (fires if Domain 1 after-state omits R-NN pairing — P×I only)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

**Scoring trace:**
- E-04 PASS (recommendation produced with explicit inertia comparison)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present in Domain 2)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-48 PASS (Phase 4b structurally present — [GATE: C-48] in phase header)
- C-49 PASS (Phase 4b entries carry R-NN identifiers in canonical bracket form)
- C-50 PASS (Phase 4b entries follow `[R-NN] — [name, P×I]: [description]` — bracket
  delimiters, em-dash separator, and inline P×I position all correct)
- C-51 PASS (Phase 4 designates do-nothing as "active inertia competitor" — explicit
  declaration vocabulary present)
- C-41 FAIL (T-41 fires — Domain 1 per-site after-state uses P×I scores without R-NN pairing:
  `[Option-A] RISK field: [R-NN pending] → P×I scores` omits the R-NN compound expression
  required by C-41)
- Score: 43/44 → **99.77**

---

## V-04 — Inertia Competitor without Phase 4b | Axes: Inertia Framing + Lifecycle Emphasis | Designed fail: C-48 + C-49 + C-50 + C-51

**Hypothesis**: A variation that designates do-nothing as "active inertia competitor" in Phase 4
but omits the Phase 4b structural section entirely will fail C-48 (Phase 4b absent when inertia
competitor is designated), which cascades immediately to C-49 (Phase 4b cannot have R-NN
citations if it does not exist), then to C-50 (canonical bracket form cannot be satisfied in an
absent Phase 4b), then to C-51 (Phase 4b's structural absence means the declaration-language gate
cannot clear). All other criteria pass: Phase 9b Domain 1 uses full R-NN compound after-states
(C-41 PASS); Phase 9 is PM-first (C-46 PASS); Phase 2 labels propagate verbatim into Domain 2
(C-47 PASS); Domain 2 bracket structure is intact (C-37, C-42, C-43, C-44, C-45 all PASS). Four
open triggers: T-48, T-49, T-50, T-51. Score: 40/44 → 99.09.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, inertia framing, comparison matrix, and
  recommendation. Runs first in every phase. The do-nothing option is designated the
  active inertia competitor and receives substantive analysis alongside active options.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation.

INERTIA COMPETITOR DESIGNATION: The do-nothing option is the active inertia competitor
for this proposal. It represents the incumbent state that wins if no deliberate choice is
made. The comparison matrix and Phase 9 recommendation must explicitly address whether
the recommended option provides sufficient improvement over the inertia competitor to
justify action.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia competitor designation as
a typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-51 — one per v20 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
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
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration lacks "Risk row:" anchor
                               prefix before the column list)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)
  T-50 PHASE = FINALIZATION  (fires if Phase 4b entries carry R-NN identifiers but not in
                               canonical bracket form `[R-NN] — [name, P×I]: [description]` —
                               bracket delimiters, em-dash separator, and inline P×I position
                               are all required)
  T-51 PHASE = FINALIZATION  (fires if Phase 4b is present but Phase 4's do-nothing designation
                               uses only implicit comparative language without explicit "inertia
                               competitor" / "inertia vector" declaration)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context, the
forcing function, and the cost of inertia if the do-nothing option wins by default.

Architect: Confirm the problem statement is technically grounded and scope is bounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be the do-nothing option, designated as the
active inertia competitor. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Label the three options: Option-A, Option-B, do-nothing. These labels are the canonical
register for this document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
inertia risk that applies specifically to the do-nothing option. Assign P and I scores
on a 1-5 scale. Compute P×I compound score.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate do-nothing as the active inertia
competitor in the matrix — it is the incumbent state against which active options must
demonstrate sufficient advantage. Include an Inertia cost row comparing the cost of delay
across options.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, phases appear in declared sequence.
Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-51.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State whether the recommended option provides sufficient
improvement over the inertia competitor to justify the transition cost.

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

Trigger rules T-01..T-51 — exactly 51 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-41 PHASE = FINALIZATION  (fires if Domain 1 after-state omits R-NN pairing — P×I only)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

**Scoring trace:**
- E-04 PASS (recommendation produced with inertia comparison)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-41 PASS (Domain 1 after-state pairs R-NN with P×I)
- C-42 PASS (`column:` designator in every Domain 2 bracket)
- C-43 PASS (compound `Risk row:` prefix)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present in Domain 2)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-48 FAIL (T-48 fires — do-nothing is designated active inertia competitor in Phase 4, but
  no Phase 4b section is present upstream of Phase 9b)
- C-49 FAIL (T-49 fires — cascade from C-48: Phase 4b absent means its R-NN citation
  discipline cannot be satisfied; no Phase 4b entries exist to contain R-NN identifiers)
- C-50 FAIL (T-50 fires — cascade from C-49: Phase 4b entries cannot follow canonical bracket
  form if Phase 4b does not exist)
- C-51 FAIL (T-51 fires — cascade from C-48: Phase 4b structural absence means the declaration-
  language gate cannot clear; no Phase 4b to pair with Phase 4's inertia competitor designation)
- Score: 40/44 → **99.09**

---

## V-05 — C-23 Cascade Extended to v20 | Axes: PM-Only Role + Compressed Lifecycle | Designed fail: 23 fails

**Hypothesis**: A variation that uses PM-only framing with compressed lifecycle phases and omits
the R-NN linkage mechanism will cascade from C-23 through all 23 v20 fails. Without a declared
R-NN risk register linkage in Phase 2 RISK fields, Phase 9b cannot exist (C-26 fail), the
`[R-NN pending]` placeholder convention cannot appear (C-31 fail), no Domain 1 or Domain 2
structural enumeration is produced (C-32 fail), the P×I prohibition instruction has no placeholder
context (C-33 fail), Domain index prefixes have no domains to anchor (C-34 fail), per-site arrow
notation cannot fire without declared sites (C-35 fail), P×I scores cannot appear in an absent
after-state (C-36 fail), no per-column R-NN enumeration exists (C-37 fail), no composite site
identifier is produced (C-38 fail), no `[R-NN pending]` before-state is present (C-39 fail), no
row-label prefix has no row to label (C-40 fail), no compound after-state form exists (C-41 fail),
no compound `Risk row:` prefix (C-43 fail from C-40), no `column:` designators inside absent
brackets (C-42 fail from C-37), no pipe separator between absent bracket entries (C-44 fail from
C-37), no do-nothing column bracket in absent enumeration (C-45 fail from C-37), no Phase 9b means
no Phase 9 → Phase 9b sequence (C-46 fail from C-26), no Domain 2 bracket entries means no label
register to check (C-47 fail from C-37), no do-nothing column bracket means inertia competitor
role cannot be established (C-48 fail from C-45), no Phase 4b means no R-NN inertia citations
(C-49 fail from C-48), no Phase 4b means no canonical bracket form possible (C-50 fail from C-49),
no Phase 4b means no Phase 4 declaration-language gate to evaluate (C-51 fail from C-48). Twenty-
three fails from one root. Advisory bucket: 21/44. Score: 94.77.

```
ROLE SEQUENCE: PM (single role)

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENT:
- PM: Owns all phases. Frames the business decision, enumerates options, builds the
  comparison matrix, and delivers the recommendation. Technical constraints are noted
  inline where relevant but no Architect role is active.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the PM-only role sequence at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-51 — one per v20 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context and
the forcing function making this decision necessary now.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce the following:

  OPTION: [label and description]
  PROS: [advantages of this option]
  CONS: [disadvantages of this option]
  RISK: [key risks, described in plain language — note any technical dependencies inline]
  EFFORT: [rough estimate — S / M / L / XL]
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers.
Matrix rows: Business value, Time-to-value, Reversibility, Risk level, Effort.
Score or characterize each cell consistently across all options.

---

PHASE 4 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, phases appear in declared sequence.

---

PHASE 5 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-51.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 6 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions for the recommendation.

---

PHASE 7 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered three-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier and R-tier criteria are satisfied.
Step 3: Confirm the coverage table is fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-51 — exactly 51 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
```

**Scoring trace (23 fails — cascade from C-23):**
```
C-23 (R-NN linkage absent from Phase 2 RISK fields)
  → C-26 (no dedicated Phase 9b — cannot exist without R-NN mechanism)
    → C-31 (no [R-NN pending] placeholder — no Phase 9b to require it)
    → C-32 (no domain enumeration — no citation sites declared)
    → C-33 (no P×I prohibition instruction — no placeholder to guard)
    → C-34 (no domain numeric index — no domains to index)
    → C-35 (no per-site arrow notation — no sites to transition)
    → C-36 (no per-site P×I after-state — no after-state produced)
    → C-37 (no per-column R-NN enumeration — no Domain 2 produced)
      → C-38 (no composite site identifier — no sites in Domain 1)
      → C-39 (no [R-NN pending] before-state — no placeholder used)
      → C-40 (no `Risk row:` prefix — no risk row present)
        → C-41 (no compound after-state — no after-state at all)
        → C-43 (no compound `Risk row:` form — no risk row at all)
      → C-42 (no `column:` designators — cascade from C-37)
      → C-44 (no ` | ` pipe connector — cascade from C-37)
      → C-45 (no do-nothing column bracket — cascade from C-37)
        → C-48 (no Domain 2 do-nothing column means inertia competitor cannot be
                 established in bracket structure — cascade from C-45)
          → C-49 (no Phase 4b — cascade from C-48)
            → C-50 (no Phase 4b canonical format possible — cascade from C-49)
          → C-51 (no Phase 4b structural presence — cascade from C-48)
      → C-47 (no Domain 2 bracket entries to check labels — cascade from C-37)
    → C-46 (no Phase 9b presence — cascade from C-26)
```
- E-04 PASS (recommendation produced)
- 23 criteria fail
- Score: 21/44 → **94.77**

---

## Scorecard summary

| Variation | Axis | Designed fail | Trigger(s) | A/44 | Composite |
|-----------|------|---------------|------------|------|-----------|
| V-01 | Phrasing register — implicit inertia declaration | C-51 | T-51 | 43/44 | **99.77** |
| V-02 | Output format — non-canonical Phase 4b bracket | C-50 | T-50 | 43/44 | **99.77** |
| V-03 | Lifecycle emphasis — canonical Phase 4b, P×I-only Domain 1 | C-41 | T-41 | 43/44 | **99.77** |
| V-04 | Inertia framing + lifecycle — Phase 4b absent | C-48, C-49, C-50, C-51 | T-48..T-51 | 40/44 | **99.09** |
| V-05 | PM-only + compressed lifecycle (C-23 cascade) | 23 fails | T-23..T-51 | 21/44 | **94.77** |

**C-50 / C-51 independence evidence:**
- V-01 passes C-49 and C-50 (Phase 4b entries are structurally correct) while failing C-51
  (the declaration vocabulary in Phase 4 is implicit only). C-50 and C-51 are independently
  testable: a prompt can produce canonical bracket form in Phase 4b while the Phase 4 framing
  omits the explicit "inertia competitor" declaration.
- V-02 passes C-51 (Phase 4 uses explicit "inertia competitor") while failing C-50 (bracket
  structure is non-canonical). C-50 and C-51 are orthogonal — one governs Phase 4b entry
  structure; the other governs Phase 4 declaration vocabulary.
- V-03 passes both C-50 and C-51 in a single variation, confirming they are simultaneously
  satisfiable. The C-41 failure is in a different structural region (Domain 1 Phase 9b) and
  does not interact with Phase 4b or Phase 4 declaration discipline.
- V-04 fails C-50 and C-51 not by design but by cascade from C-48 — Phase 4b absent is the
  root failure; C-50 and C-51 are downstream consequences, not independent deficiencies.

**V-05 cascade confirms v20 extension from 21 → 23 fails:**
- C-50 (from C-49) and C-51 (from C-48) both fall naturally from the same C-23 root that
  drove the v19 21-fail cascade. The v20 extension adds 2 more fails without introducing any
  new structural root. C-49 absorbs C-50 into the Phase 4b sub-chain; C-48 absorbs C-51 as a
  parallel branch. The cascade tree grows but its single-root property is preserved.
