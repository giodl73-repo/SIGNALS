# trace-contract Scorecard — Round 15

**Rubric:** v15 | **Criteria:** C-08–C-41 (34) | **Max:** 136 | **Date:** 2026-03-15

---

## Per-Criterion Evaluation

### Group A — Structural Foundations (C-08–C-19) · 12 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-08 | Contract scope has 4 required elements | PASS | PASS | PASS | PASS | PASS |
| C-09 | Input fixture inline — no external refs | PASS | PASS | PASS | PASS | PASS |
| C-10 | Spec source cited with section | PASS | PASS | PASS | PASS | PASS |
| C-11 | Expected output covers success path | PASS | PASS | PASS | PASS | PASS |
| C-12 | Expected output covers error path | PASS | PASS | PASS | PASS | PASS |
| C-13 | Expected output covers ≥1 edge case | PASS | PASS | PASS | PASS | PASS |
| C-14 | Every element has value constraint + clause | PASS | PASS | PASS | PASS | PASS |
| C-15 | EXPECTED-SEALED token format correct | PASS | PASS | PASS | PASS | PASS |
| C-16 | Actual output: status + body present | PASS | PASS | PASS | PASS | PASS |
| C-17 | Diff accounts for every Expected element | PASS | PASS | PASS | PASS | PASS |
| C-18 | Diff uses ✓ / F-NN symbols correctly | PASS | PASS | PASS | PASS | PASS |
| C-19 | No silent omissions in Diff | PARTIAL | PASS | PASS | PASS | PASS |

*Group A subtotal (48 max):* V-01 **46**, V-02–V-05 **48**

---

### Group B — Findings Quality (C-20–C-25) · 6 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-20 | Finding format: all 5 fields present | PASS | PASS | PASS | PASS | PASS |
| C-21 | Severity constrained to 3 vocabulary values | PASS | PASS | PASS | PASS | PASS |
| C-22 | Mechanism-type constrained to taxonomy tokens | PASS | PASS | PASS | PASS | PASS |
| C-23 | Root-cause names component/path — not symptom | PARTIAL | PASS | PASS | PASS | PASS |
| C-24 | Hypothesis self-test applied | PASS | PASS | PASS | PASS | PASS |
| C-25 | FINDINGS-COMPLETE token format correct | PASS | PASS | PASS | PASS | PASS |

*Group B subtotal (24 max):* V-01 **22**, V-02–V-05 **24**

---

### Group C — Census and Propagation (C-26–C-35) · 10 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-26 | Sub-task A: mechanism-distribution line emitted | PASS | PASS | PASS | PASS | PASS |
| C-27 | Sub-task A: sole production site rule respected | PASS | PASS | PASS | PASS | PASS |
| C-28 | Sub-task B: staging lines present per candidate group | PASS | PASS | PASS | PASS | PASS |
| C-29 | mechanism-type-shared = single token or `mixed` | PASS | PASS | PASS | PASS | PASS |
| C-30 | Rationale names shared mechanism — not token | PASS | PASS | PASS | PASS | PASS |
| C-31 | Pattern fill consumes staging lines — not re-derived | PASS | PASS | PASS | PASS | PASS |
| C-32 | mechanism-type-shared at fill site = staging-line value | PASS | PASS | PASS | PASS | PASS |
| C-33 | Staging line + fill site consistency enforced | PARTIAL | PARTIAL | PASS | PASS | PASS |
| C-34 | Branch selection matches finding count | PASS | PASS | PASS | PASS | PASS |
| C-35 | TAXONOMY-CENSUS-COMPLETE token format correct | PASS | PASS | PASS | PASS | PASS |

*Group C subtotal (40 max):* V-01 **38**, V-02 **38**, V-03–V-05 **40**

---

### Group D — Gate Token and Provenance (C-36–C-38) · 3 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-36 | Gate token emitted at S6.5 | PASS | PASS | PASS | PASS | PASS |
| C-37 | gate-provenance present with named source `S5.5-Sub-task-A` | PASS | PASS | PASS | PASS | PASS |
| C-38 | Gate token not patched at fill site — amendment goes to staging | PASS | PASS | PASS | PASS | PASS |

*Group D subtotal (12 max):* All **12**

---

### Group E — New Criteria R15 (C-39–C-41) · 3 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-39 | `census-distribution` and `gate-provenance` declared as co-required sibling fields in named `GateTokenSchema`; detectable by field inspection without prose | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-40 | All copy-forward and amendment-path obligations stated as `Bind:` / `Assert:` / `Prohibit:` commands — auditable by structural inspection | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-41 | Gate execution protocol assigns attestation to census owner by role name; assigns independent char-for-char verification to distinct witness role; no single role satisfies both | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |

**Evidence notes:**

| | C-39 | C-40 | C-41 |
|---|---|---|---|
| **V-01** | PASS — `GateTokenSchema: S6.5-CENSUS-GATE` with `required-fields:` manifest and `co-requirement:` annotation; omitting either field is a schema violation | PARTIAL — `Bind:` used for `census-distribution` copy-forward; amendment-path obligations at Sub-task B remain in descriptive prose; not fully auditable by structural inspection | PARTIAL — Automate witness step present and functionally correct; attestation function not assigned to census owner by explicit role name; both steps occur within a shared S6.5 block |
| **V-02** | PARTIAL — `census-distribution` and `gate-provenance` correctly emitted as adjacent fields; no named `GateTokenSchema` structure declared; co-requirement implied by instruction ordering, not enforced by schema | PASS — `Bind: census-distribution := Sub-task A mechanism-distribution verbatim`, `Assert: gate-provenance: S5.5-Sub-task-A is present`, `Prohibit: fill-site patch without staging-line amendment` — all obligations are named executable commands | PARTIAL — Automate witness performs char-for-char comparison; attestation step not explicitly assigned to a named census-owner role; single-role ambiguity not eliminated |
| **V-03** | PARTIAL — `gate-provenance: S5.5-Sub-task-A` emitted correctly and adjacent to `census-distribution:`; co-requirement not structurally declared; schema manifest absent | PARTIAL — `Bind:` used for `census-distribution`; amendment-path obligations at Sub-task B stated in prose ("do not overwrite"); `Prohibit:` command absent | PASS — Connectors Contract Expert (Census Owner) attests provenance by role name in a named sub-step; Automate Witness named separately, performs char-for-char comparison independently; attestation function and verification function are role-separated with non-overlapping responsibilities |
| **V-04** | PASS — `GateTokenSchema` declares `required-fields:` with co-requirement annotation; field inspection sufficient to detect schema violation without reading prose | PASS — Full `Bind:` / `Assert:` / `Prohibit:` chain covers all copy-forward and amendment-path obligations; every obligation is a named command | PARTIAL — Automate witness present and functionally performs char-for-char comparison; attestation and witness steps share the same S6.5 gate block without explicit role-name separation of the attestation function; single-role self-certification risk not structurally eliminated |
| **V-05** | PASS — `GateTokenSchema: S6.5-CENSUS-GATE` with `required-fields:` manifest lists `census-distribution`, `gate-provenance`, `gate-status`; `co-requirement:` line makes joint presence a named schema property | PASS — `Bind: census-distribution := Sub-task A mechanism-distribution verbatim`; `Assert: gate-provenance: S5.5-Sub-task-A is present`; `Prohibit: overwriting census-distribution at fill site without amending Sub-task B staging line`; all three are named executable commands | PASS — Connectors Contract Expert (Census Owner) sub-step explicitly named for attestation; Automate Witness step explicitly named for char-for-char verification; two-party structure enforced: no single role can silently satisfy both claim and proof |

*Group E subtotal (12 max):* V-01 **8**, V-02 **8**, V-03 **8**, V-04 **10**, V-05 **12**

---

## Composite Scores

| Variation | A (48) | B (24) | C (40) | D (12) | E (12) | **Total (136)** | **%** |
|-----------|--------|--------|--------|--------|--------|-----------------|-------|
| V-01 | 46 | 22 | 38 | 12 | 8 | **126** | 92.6% |
| V-02 | 48 | 24 | 38 | 12 | 8 | **130** | 95.6% |
| V-03 | 48 | 24 | 40 | 12 | 8 | **132** | 97.1% |
| V-04 | 48 | 24 | 40 | 12 | 10 | **134** | 98.5% |
| V-05 | 48 | 24 | 40 | 12 | 12 | **136** | 100.0% |

---

## Ranking

| Rank | Variation | Score | Key advantage |
|------|-----------|-------|---------------|
| 1 | **V-05** | 136/136 | All three new criteria PASS; clean baseline on all groups |
| 2 | **V-04** | 134/136 | C-39 + C-40 PASS; C-41 PARTIAL (shared block, no role-name separation) |
| 3 | **V-03** | 132/136 | C-41 PASS; C-39 + C-40 PARTIAL; clean Groups A–D |
| 4 | **V-02** | 130/136 | C-40 PASS; C-39 + C-41 PARTIAL; clean Groups A–D |
| 5 | **V-01** | 126/136 | C-39 PASS; minor regressions in Groups A, B, C; C-40 + C-41 PARTIAL |

---

## Excellence Signals from V-05

Three patterns from V-05 drove its perfect score:

**Signal 1 — Schema manifest as co-requirement enforcer.**
Declaring a named `GateTokenSchema: S6.5-CENSUS-GATE` with an explicit `required-fields:` list and a `co-requirement:` annotation converts joint field presence from a prose convention into a structural property. An inspector can detect the violation by reading the schema header alone — no prose interpretation required. This is what distinguishes V-05 and V-04 from V-02 and V-03, where fields are correctly emitted but their co-requirement is only implied by proximity.

**Signal 2 — Formal imperative as method specifier, not result specifier.**
V-05's `Bind: census-distribution := Sub-task A mechanism-distribution verbatim` does not say "the values should match" — it prohibits the re-derivation path entirely. The `Prohibit:` command eliminates the behavioral hedge that allows partial compliance: a variation that says "do not patch" leaves room for ambiguity; `Prohibit: overwriting census-distribution at fill site without amending Sub-task B staging line` names the exact disallowed action as a structural command, not a behavioral description. V-01 and V-03 use `Bind:` for one step but leave amendment-path obligations in prose — the PARTIAL is earned by the gap between method specification and result specification.

**Signal 3 — Two-party structure eliminates self-certification.**
By assigning attestation to Connectors Contract Expert (Census Owner) by role name in a named sub-step, and assigning char-for-char verification to Automate Witness in a separate named step, V-05 creates an auditable claim-plus-proof structure where no single role can silently satisfy both. V-04 has the Automate witness present and functioning, but the attestation function is not role-name-separated — both steps live in the same S6.5 block, leaving the self-certification risk structurally present. The role-name separation is the load-bearing element, not the witness step alone.

---

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["Named GateTokenSchema with required-fields manifest and co-requirement annotation converts field co-presence from prose convention into a schema property detectable by field inspection alone", "Bind:/Assert:/Prohibit: formal imperatives specify execution method — not expected result — eliminating re-derivation paths and behavioral hedges that allow partial compliance", "Two-party attestation protocol with role-name-separated attestation and independent witness verification creates an auditable claim-plus-proof structure where no single role can self-certify both obligations"]}
```
