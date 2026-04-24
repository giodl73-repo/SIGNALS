Now the output:

---

## flow-dataflow — Round 5 Scoring

### Per-Variation Results

All five variations score **100/100** and achieve **Golden** status.

---

**V-01** (6-role ARTIFACT: chain)
- C-19: `ARTIFACT:` prefix declared as first structural element; `Citing: ARTIFACT: [NAME]` form required uniformly throughout all 6 roles. Verifiable by prefix token match.
- C-20: "Do not write the next stage until every field in this block is complete." + "Stage N+1 may not be written until this block is fully complete." — explicit deferral prohibition, gate condition named.
- C-21: `Freshness verdict: FRESH | STALE` required field in every BOUNDARY CHECK with inline comparison logic; "Neither may be deferred."

**V-02** (Citation Registry table + A-xx tokens)
- C-19: CITATION REGISTRY table at top maps every artifact to `[A-xx]` token before any output; `## [A-xx]:` for registration, `[Citing A-xx: Name]` for citation; ad hoc labels are non-compliant.
- C-20: R-09 standalone prohibition, structurally separate from R-06 placement instruction — two distinct requirements.
- C-21: R-10 dedicated requirement; "A BOUNDARY CHECK that contains `Elapsed (cumulative)` without a `Freshness verdict` does not satisfy R-10."

**V-03** (directive-conversational + Protocol Rules)
- C-19: SC-1 Protocol Rule declares ARTIFACT REGISTRY with exact labels; `Citing:` line using exact label verbatim — exact string match is machine-verifiable.
- C-20: SC-2 Protocol Rule: "Stop at the boundary. Complete it. Then advance." + inline in Role 3: "SC-2 prohibits the next stage until they are present."
- C-21: SC-3 Protocol Rule at top + `Freshness verdict: FRESH | STALE` in BOUNDARY CHECK template with inline comparison.

**V-04** (Lifecycle emphasis phase gates)
- C-19: CITATION CONVENTION + Artifact Registry; PHASE 1 GATE: "All section headers use the ARTIFACT: prefix per the convention" — gate enforces convention compliance.
- C-20: Write-order rule in PHASE 2 + PHASE 2 GATE: "No stage was written before its preceding boundary block was complete."
- C-21: `Freshness verdict` required in BOUNDARY CHECK + PHASE 2 GATE: "Every boundary check has `Freshness verdict: FRESH | STALE`" — gate makes verdict a phase prerequisite.

**V-05** (Baseline-first + STRUCTURAL CONSTRAINTS)
- C-19: SC-1 in STRUCTURAL CONSTRAINTS declares `[A-xx]` token scheme; ARTIFACT REGISTRY table with tokens [A-01]–[A-06]; "All citations must use the `[A-xx]` token. No exceptions."
- C-20: SC-2 declared upfront + ROLE 3: "Apply SC-2:" + "Per SC-2, Stage N+1 may not be written until both are present." — named constraint declared upfront, referenced twice inline.
- C-21: SC-3 declared upfront + BOUNDARY CHECK template `Freshness verdict: FRESH | STALE [SC-3: compare...]` — constraint named at declaration AND at point of use.

---

### Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 14/14 | **100** | YES |
| V-02 | 4/4 | 3/3 | 14/14 | **100** | YES |
| V-03 | 4/4 | 3/3 | 14/14 | **100** | YES |
| V-04 | 4/4 | 3/3 | 14/14 | **100** | YES |
| V-05 | 4/4 | 3/3 | 14/14 | **100** | YES |

**Rank:** All tied at 100. All five achieve Golden.

The rubric has reached saturation at 21 criteria. Every variation designed to address C-19/C-20/C-21 delivers all three and carries forward C-01–C-18. Differentiation requires a new dimension.

---

### Excellence Signals — R5 patterns beyond the rubric

**1. Formal pre-declared registry table** (V-02, V-05)
A REGISTRY TABLE mapping every artifact to a `[A-xx]` token with owner and description — produced before any role output. Different from a prefix declaration (V-01, V-04) and from a flat label list (V-03): the table makes citation targets first-class, enumerable, and column-verifiable. Candidate for **C-22**.

**2. Phase gate self-verification checklists** (V-04)
The model must produce and tick a checklist before advancing to each phase. Non-compliance appears in the output as an unticked item — visible to any reader. Compliance becomes self-documented, not just evaluator-verifiable. PHASE 2 GATE specifically checks C-11/C-12/C-14/C-21 per boundary before Phase 3 can begin. Candidate for **C-23**.

**3. Upfront constraint section with inline callback syntax** (V-05, V-03)
SC-1/SC-2/SC-3 declared once prominently before all roles, then their names reappear inline at every point of application: "Apply SC-2:", "[SC-3: compare Elapsed...]", "Per SC-2, Stage N+1 may not be written...". Prior rounds enforced inline OR declared upfront — V-05 and V-03 do both, creating two-level enforcement. Candidate for **C-24**.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Formal pre-declared registry table mapping every artifact to a machine-parseable token creates a verifiable citation namespace beyond prefix declaration or flat label list", "Phase gate self-verification checklists require the model to produce and tick compliance items inline before phase advancement -- compliance becomes self-documented in the output artifact", "Upfront constraint section with inline callback syntax creates two-level enforcement: constraint named once in STRUCTURAL CONSTRAINTS then referenced by that name at every point of use in role instructions"]}
```
 blockquote: "No role after this point may change it. The contract value stays at [N] [unit]."
- C-14/C-18: Elapsed (cumulative): "add up every stage latency and every boundary latency written above -- compute it here, now"; SC-2 prohibition converts the field to a gate
- C-15/C-16: INCUMBENT BASELINE in Role 1; every subsequent role opens with named Citing: line using exact registry label
- C-19: SC-1 Protocol Rule at top declares ARTIFACT REGISTRY with exact registered labels; "Citing: line using the exact label. Use the label verbatim." -- exact string match is machine-verifiable
- C-20: SC-2 Protocol Rule: "You may not write Stage N+1 until the BOUNDARY CHECK is fully written with all required fields present -- including the Freshness verdict. Stop at the boundary. Complete it. Then advance."
- C-21: SC-3 Protocol Rule at top; BOUNDARY CHECK template Freshness verdict: FRESH or STALE with inline comparison; "A boundary block that computes elapsed time without stating a verdict does not satisfy SC-3."

Essential: 4/4 -> 60 | Recommended: 3/3 -> 30 | Aspirational: 14/14 -> 10
Composite: 100 | Golden: YES

---

### V-04 -- Combined: Lifecycle emphasis + inertia framing

All 21 criteria: PASS

Essential/Recommended: PHASE 2 stage and boundary block structures cover all essential and recommended criteria; PHASE 3 STALE ANALYSIS with two rows.

Aspirational:
- C-08/C-09: PHASE 4 recovery prescriptions with specific named mechanisms; pattern trade-off table with ARTIFACT: INCUMBENT BASELINE column
- C-10: PHASE 1 DOMAIN CONTEXT locks all three fields; PHASE 1 GATE verifies vocabulary integrity before PHASE 2 begins
- C-11/C-12: PHASE 2 inline boundary placement with write-order rule; PHASE 2 GATE: "Every boundary check names an Entity from ARTIFACT: DOMAIN CONTEXT (not data or records)"
- C-13/C-17: PHASE 1 threshold grounded in F-02; IMMUTABLE block prohibits revision; PHASE 1 GATE: "IMMUTABLE block present and explicitly prohibits revision by Phase 2 and Phase 3"
- C-14/C-18: Elapsed computed within each BOUNDARY CHECK; PHASE 2 GATE: "Every boundary check has Elapsed (cumulative) computed additively" before phase advancement
- C-15/C-16: PHASE 1 ARTIFACT: INCUMBENT BASELINE; PHASE 2-4 each begin with named Citing: ARTIFACT: lines referencing prior phase outputs by name (including "from Phase 2")
- C-19: CITATION CONVENTION at top declares ARTIFACT: prefix; Artifact Registry lists all required registrations; PHASE 1 GATE enforces: "All section headers use the ARTIFACT: prefix per the convention"
- C-20: "Do not write Stage N+1 until ARTIFACT: BOUNDARY CHECK is fully written with all required fields present. This is the write-order rule."; PHASE 2 GATE: "No stage was written before its preceding boundary block was complete"
- C-21: BOUNDARY CHECK Freshness verdict: FRESH or STALE required; PHASE 2 GATE: "Every boundary check has Freshness verdict: FRESH or STALE derived from ARTIFACT: DOMAIN CONTEXT threshold" -- gate makes verdict a phase prerequisite

Essential: 4/4 -> 60 | Recommended: 3/3 -> 30 | Aspirational: 14/14 -> 10
Composite: 100 | Golden: YES

---

### V-05 -- Combined: Baseline-first role sequence + Declarative constraint section

All 21 criteria: PASS

Essential/Recommended: [A-03] STAGE TRACE and [A-04] BOUNDARY CHECKS provide complete lineage, error handling, loss points, schema diffs, latency, stale analysis; entity vocabulary enforcement via [A-02].

Aspirational:
- C-08/C-09: [A-06] CLOSURE with specific named recovery mechanisms; Pattern Trade-Off table with two dimensions citing [A-01] by token
- C-10: [A-02] DOMAIN CONTEXT in ROLE 2 before ROLE 3; entity vocabulary, downstream consumer, business cadence declared; BOUNDARY CHECK requires verbatim entity reuse
- C-11/C-12: "Apply SC-2: do not write Stage N+1 until the following BOUNDARY CHECK block is fully complete" -- inline placement via named constraint callback; Entity field: exact name from [A-02]
- C-13/C-17: ROLE 2 [A-02] IMMUTABLE THRESHOLD block declares threshold before ROLE 3; "Prohibited revisions: no role after this point may change this value."
- C-14/C-18: Elapsed (cumulative): "compute here, not in a later section"; [SC-3: compare Elapsed to [A-02] threshold] ties the field to the verdict; "Per SC-2, Stage N+1 may not be written until both are present"
- C-15/C-16: [A-01] INCUMBENT BASELINE in ROLE 1; every subsequent role opens with Citing: [A-xx] token references -- all named, machine-verifiable by token
- C-19: SC-1 in STRUCTURAL CONSTRAINTS (top of prompt) declares [A-xx] token scheme; ARTIFACT REGISTRY table maps every artifact to token; "All citations must use the [A-xx] token. No exceptions."
- C-20: SC-2 in STRUCTURAL CONSTRAINTS: "Stage N+1 may not be written until BOUNDARY CHECK is fully written"; ROLE 3: "Apply SC-2:"; "Per SC-2, Stage N+1 may not be written until both are present." -- named constraint declared upfront, referenced twice inline
- C-21: SC-3 in STRUCTURAL CONSTRAINTS: "Every BOUNDARY CHECK must include a Freshness verdict: FRESH or STALE field... A boundary block that records elapsed time without a verdict field does not satisfy SC-3."; BOUNDARY CHECK template: Freshness verdict: FRESH or STALE [SC-3: compare...] -- constraint named at declaration and at point of use

Essential: 4/4 -> 60 | Recommended: 3/3 -> 30 | Aspirational: 14/14 -> 10
Composite: 100 | Golden: YES

---

## Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 14/14 | 100 | YES |
| V-02 | 4/4 | 3/3 | 14/14 | 100 | YES |
| V-03 | 4/4 | 3/3 | 14/14 | 100 | YES |
| V-04 | 4/4 | 3/3 | 14/14 | 100 | YES |
| V-05 | 4/4 | 3/3 | 14/14 | 100 | YES |

Rank: All tied at 100. All five achieve Golden.

The rubric has reached saturation at 21 criteria: every variation designed to address C-19/C-20/C-21 delivers all three, and carries forward C-01 through C-18 from prior rounds. Differentiation now requires a dimension not yet in the rubric.

---

## Excellence Signals from R5 -- Patterns beyond the current rubric

1. Formal pre-declared registry table (V-02, V-05)
Both variations produce a REGISTRY TABLE before any output -- mapping every artifact to a short token ([A-xx]) with owner and description. This is a self-documenting citation namespace: every citation is verifiable by column lookup, not just prefix match. A prefix declaration (V-01, V-04) allows an ARTIFACT: prefix convention but does not pre-register targets; a flat label list (V-03) has no token column. The registry table makes citation targets first-class, enumerable, and column-verifiable. Candidate for C-22.

2. Phase gate self-verification checklists (V-04)
V-04 requires the model to produce and explicitly tick a checklist before advancing to each phase. The gate appears in the output -- a non-compliant trace contains an unticked item, visible to any reader. Compliance is no longer an implicit property (verifiable only by post-hoc evaluation); it is an explicit, self-documented property that the model must affirm in its output. PHASE 1 GATE verifies C-19 compliance; PHASE 2 GATE verifies C-11/C-12/C-14/C-21 compliance per boundary before Phase 3 begins. No prior round introduced self-verification as an output obligation. Candidate for C-23.

3. Upfront constraint section with inline callback syntax (V-05, V-03)
V-05's STRUCTURAL CONSTRAINTS and V-03's PROTOCOL RULES declare SC-1/SC-2/SC-3 once before any role. Those constraint names then reappear inline at their exact point of use in role instructions: "Apply SC-2:", "[SC-3: compare Elapsed...]", "Per SC-2, Stage N+1 may not be written...". Two-level enforcement: constraint declared at top as a named rule, then referenced by that name where it applies. A model that misses the upfront section encounters the constraint name again in the role instruction, and vice versa. Prior rounds enforced inline OR declared upfront -- V-05 and V-03 do both. Candidate for C-24.