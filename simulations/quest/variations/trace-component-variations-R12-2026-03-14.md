Written to `simulations/quest/rubrics/trace-component-rubric-v12-variate-R12-2026-03-15.md`.

---

# trace-component — Round 12 Variations

**Variation axes**: Lifecycle emphasis (V-01), Role sequence (V-02), Inertia framing (V-03), combined Role+Lifecycle (V-04), combined all three (V-05).

---

## V-01 · Lifecycle Emphasis — Manifest-Close Prohibition Line (C-38 Target)

**Axis**: Lifecycle emphasis
**Hypothesis**: The `↓ TABLE-N begins immediately below. No content may appear between this line and the TABLE-N header.` prohibition is the manifest's ABSOLUTE LAST CONTENT — not in the opening annotation, not in a charter preamble. V-01 eliminates all header-level adjacency instructions; the close-line is the only enforcement mechanism. Five manifest-table pairs. C-39 not targeted. **Expected: ~150/152 (C-38 pass, C-39 fail).**

The prompt: standard frontend domain expert role → Framework Declaration → five MANIFEST-N/TABLE-N pairs where each manifest's code block closes with the `↓ TABLE-N begins immediately below...` line as the absolute last item before the table header → TABLE-6 (four-phase UI) → TABLE-7 (Findings, five rows, UR cross-ref) → TABLE-8 (Criteria Audit).

---

## V-02 · Role Sequence — Schema Architect Produces TRAVERSAL-SCHEMA from Requirements (C-39 Target)

**Axis**: Role sequence
**Hypothesis**: C-39 requires the model to author the schema principles, not fill in a pre-written template. V-02 gives the model **requirements** (A through D) and asks it to produce the TRAVERSAL-SCHEMA content from scratch. Requirement C explicitly asks the model to declare the close-line marker text it will use. Role 2 then instantiates that text at the end of every manifest — satisfying C-38 via a self-authored rule. Violation in Role 2 contradicts the model's own Requirement C declaration. **Expected: ~150-152/152.**

Role 1 (Schema Architect) produces TRAVERSAL-SCHEMA from Requirements A (framework), B (Direction default contract), C (manifest-to-table adjacency rule + exact close-line text), D (table inventory). Role 2 (Trace Analyst) applies that schema, including the Requirement C close-line verbatim at each manifest's end.

---

## V-03 · Inertia Framing — Inertia as Null Hypothesis (C-36 Reinforced)

**Axis**: Inertia framing
**Hypothesis**: The cognitive contract shifts from "inertia is the default code" to "inertia is the null hypothesis — a departure code is a falsifying claim." Active hops must have evidence; inert hops are confirmed nulls, not omissions. This phrasing register change in the traversal table's Role column (`Null confirmed: reason` vs. `Active claim: departure + evidence`) may strengthen C-36 compliance by making false positive departures structurally visible. C-38/C-39 secondary — header annotation pattern used for adjacency. **Expected: ~146-150/152.**

Direction column framing: `Direction [null hypothesis: <-> inert | active claims: prop-pass · event-propagate · dispatch · effect-trigger · context-provide]`. Role column: `Null confirmed: reason` or `Active claim: departure + evidence`.

---

## V-04 · Combined: Close-Line + Schema Architect Role (C-38 + C-39)

**Axis**: Role sequence + Lifecycle emphasis
**Hypothesis**: V-01 targets C-38; V-02 targets C-39. V-04 combines them with a structural link: the model authors the TRAVERSAL-SCHEMA in Role 1, **Requirement C of that schema declares the close-line marker text**, and Role 2 instantiates it verbatim at each manifest's end. C-38 and C-39 are satisfied via a single causal chain — the model is both the author of the close-line rule and its implementer. Violation is self-contradiction at two levels simultaneously. **Expected: ~150-152/152.**

The key design: Role 1 Requirement C says "declare the exact text of the closing marker that must appear as the final line of every manifest block — explain why it must be the manifest's final line, not a header annotation." Role 2 manifests end with `*[Requirement C close-line — verbatim, last line of this manifest.]*`.

---

## V-05 · Combined: Schema Architect + Null-Hypothesis Inertia + Close-Line (All Three Axes)

**Axis**: Role sequence + Inertia framing + Lifecycle emphasis
**Hypothesis**: The model authors a TRAVERSAL-SCHEMA (C-39) that frames **inertia as the governing epistemic null** (Requirement B — C-36/V-03 framing) and **declares the close-line text** (Requirement C — C-38). Role 2 applies all three: Direction defaults to the null; departures are claims; each manifest closes with the self-declared marker. The null-hypothesis lens propagates into TABLE-7 (findings are "confirmed claims, not concerns"; unnecessary re-renders are "unsupported necessity claims"). Maximum conceptual integration of the three axes. **Expected: ~150-152/152.**

---

## Variation Axis Summary

| Variation | Primary axis | C-38 mechanism | C-39 mechanism | Expected delta |
|-----------|-------------|----------------|----------------|----------------|
| V-01 | Lifecycle emphasis | Close-line as manifest's absolute last content (prompt-provided) | None | C-38 +2, C-39 0 |
| V-02 | Role sequence | Close-line declared by model in Req C, instantiated per manifest | Model produces schema from requirements — not template | C-38 +2, C-39 +2 |
| V-03 | Inertia framing | Header annotation only (C-38 risk: not last-line) | None | C-38 partial, C-39 0 |
| V-04 | Role sequence + Lifecycle | Close-line verbatim from model's Req C — causal chain | Model authors schema; Req C text becomes manifest close-line | C-38 +2, C-39 +2 |
| V-05 | All three | Same as V-04 | Schema includes null-hypothesis framing + close-line text | C-38 +2, C-39 +2 |

**Key C-38 distinction between V-01 and V-02/V-04/V-05**: V-01 has the close-line in the prompt's manifest template (positionally correct, but prompt-authored). V-02/V-04/V-05 have the model declare the close-line text in Role 1, then instantiate that exact text in each Role 2 manifest — the model is author of both the rule and its implementation.

**Key C-39 distinction**: V-03 provides the epistemic framing as a preamble in the prompt (prompt-authored — C-39 would fail). V-02/V-04/V-05 require the model to write the schema's principles from requirements — C-39 passes because the model authored the rules.
