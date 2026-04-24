Written to `simulations/quest/golden/trace-skill-variate-R2-2026-03-15.md`.

---

# trace-skill -- Variations R2 (2026-03-15)

## Context

**Critical entry-state observation**: All prior rounds (R1–R8) used a **Setup/Execute/Findings/Amend** phase schema. Rubric v2 introduces a new canonical schema: **Gather / Bind / Execute / Verdict**. Round 2 is a clean-slate redesign — no prior variation satisfies C-01 or C-06.

---

## V-01 -- Single axis: Phrasing register (formal/imperative, canonical labels locked)

**Axis**: Phrasing register — formal imperative language with an immutable Phase Label Schema declared before the trace begins. Any synonym header (Setup, Resolve, Run, Summary) is a structural violation. Verdict is a compliance ledger citing criterion IDs directly.

**Hypothesis**: Declaring labels as immutable schema names makes C-01/C-06 structural rather than behavioral — a model using synonyms is producing an invalid trace, which the compliance-ledger Verdict makes visible at checking time. Forcing criterion-ID citation (C-07) prevents Verdict from collapsing into narrative. **Risk**: formal rigidity may make Bind a mechanical table-fill with no analytic content.

**Key structural choices targeting rubric criteria**:
- Phase Label Schema table (immutable headers) → C-01, C-06
- Verdict as compliance ledger with criterion-ID column → C-05, C-07
- Gather table with Source column → C-02
- Bind table with Status column (RESOLVED/UNRESOLVED) → C-03

---

## V-02 -- Single axis: Gather ordering (spec-first two-tier enumeration)

**Axis**: Gather ordering — Tier 1 enumerates all spec-defined inputs before the invocation is read. Tier 2 maps invocation tokens onto Tier 1 slots. The spec anchors the input space; the invocation constrains it.

**Hypothesis**: Starting Gather from the invocation risks missing spec-required inputs the invocation leaves implicit. Spec-first enumeration forces full spec-read before any invocation token is consulted, surfacing optional inputs not present in the test invocation. C-11 is satisfied structurally by tier separation — it cannot be violated without reversing the tiers. **Risk**: a poorly organized spec still requires navigating multiple sections; the tier structure doesn't help with that.

**Key structural choices**:
- Tier 1 (spec inputs only, invocation forbidden) → C-11, C-02
- Tier 2 (invocation mapping) with gap flags G-NN → C-02
- Conflict rule: invocation wins over spec default, stated explicitly → C-03 in Bind

---

## V-03 -- Single axis: Bind as resolution ledger

**Axis**: Bind as resolution ledger — explicit table with one row per Gather input, three-value Status vocabulary (RESOLVED / UNRESOLVED-CONTINUED / UNRESOLVED-BLOCKED). An UNRESOLVED-BLOCKED row halts Execute before it starts.

**Hypothesis**: Prose Bind descriptions satisfy C-03 by re-listing inputs with context rather than enforcing one-to-one resolution. The ledger makes C-03 structural: missing a Gather row fails on table completeness, not prose interpretation. The BLOCKED/CONTINUED distinction pulls the halt decision into Bind explicitly, preventing the silent-partial-run failure mode. **Risk**: the Status vocabulary must be kept distinct from any SA/SG/EG/QO Coverage Matrix taxonomy added in later rounds.

**Key structural choices**:
- Bind Gate hardstop on UNRESOLVED-BLOCKED → C-03, blocks partial Execute
- Three-value Status vocabulary declared as a legend → C-03
- Artifact section gap-marked (not omitted) with B-NN → C-08

---

## V-04 -- Combined: Coverage Matrix + BLOCKED gate (C-09, C-12)

**Axes**: Output format (Coverage Matrix with closed-world preamble) + Lifecycle emphasis (BLOCKED gate halts before Gather begins on any Required=YES/Gap=YES row).

**Hypothesis**: Without a Coverage Matrix, Gather's completeness is unknowable until after it runs. The matrix inverts this: full input space declared before Gather, then Gather confirms each entry. C-09 satisfied by the matrix; C-12 satisfied by the BLOCKED gate — which halts before the first Gather row is populated, preventing the partial-trace-that-looks-complete failure mode. **Risk**: conservative BLOCKED gate may trigger on optional inputs; Required/optional distinction in the matrix is load-bearing.

**Key structural choices**:
- Coverage Matrix section before Gather with closed-world preamble → C-09
- BLOCKED gate with hard-stop language → C-12
- Closed-world bidirectionality (undeclared references = defect, declared but absent = gap) → C-09

---

## V-05 -- Combined: All aspirationals (C-09 through C-13)

**Axes**: Coverage Matrix + BLOCKED (C-09, C-12) + spec-first Gather (C-11) + Execute relay carry (C-10) + delimiter markers (C-13).

**Hypothesis**: Each aspirational targets a different trace layer. No single-axis variation satisfies all five. V-05 integrates them in sequence: Coverage Matrix pre-flight → spec-anchored Gather → resolution Bind → relay-traced Execute with artifact in delimiters → Verdict reading relay, not artifact body. **Risk**: relay carry table adds per-role rows; skills with many roles produce large tables. Mitigation: 4-column compact format (role, signal, binding, status), one row per role.

**Key structural choices that collectively satisfy all 13 criteria**:

| Structural element | Satisfies |
|---|---|
| Phase headers Gather/Bind/Execute/Verdict | C-01, C-06 |
| Gather Tier 1 (spec) before Tier 2 (invocation) | C-11, C-02 |
| Bind ledger, one row per Gather input | C-03 |
| Coverage Matrix with closed-world preamble | C-09 |
| BLOCKED gate on Required=YES/Gap=YES | C-12 |
| Relay table in Execute (role/signal/binding/status) | C-10 |
| `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` | C-13 |
| Artifact sections complete, no elision | C-04, C-08 |
| Verdict reads relay table, criterion-ID ledger | C-05, C-07, C-10 |
