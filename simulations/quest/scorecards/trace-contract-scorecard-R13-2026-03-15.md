Now I have what I need. The v13 rubric table (C-26 through C-36, total 160 pts) and the baseline (R12 V-04 = 130/130 on C-26–C-34). Let me score.

---

## Cross-Field Verification (C-36)

**Trace artifact (ground truth):** V-01 spec as written above — structured `S6.5-CENSUS-GATE:` block with `census-distribution:` key-value field; `## Cross-Field Verification (C-36)` table with columns `pattern-N | source | mechanism-type-shared (at fill site) | mechanism-type-shared (from staging) | verdict`; Summary consumption clause naming the gate block as authoritative source; `source: group-candidate-N` in each Multi-pattern entry.

---

### V-01 — Output Format: Structured Gate Token Block + Verification Table

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-26 | 10 | PASS | `[EXPECTED-RESOLVED | gate-clauses:N | clauses-resolved:M | phase:2-complete]` present |
| C-27 | 10 | PASS | Zero / Singleton / Multi-pattern branch templates with named structural slots |
| C-28 | 15 | PASS | `mechanism-type:` token on each finding entry, constrained vocabulary |
| C-29 | 15 | PASS | `mechanism-type-shared:` in both Singleton and Multi-pattern branch templates |
| C-30 | 10 | PASS | `mechanism-distribution:` aggregate required in Summary |
| C-31 | 20 | PASS | S5.5 mandatory interstitial before closure; `(do not skip to S6 until both sub-tasks complete)` enforced |
| C-32 | 20 | PASS | `group-candidate-N: findings=[...] mechanism-type-shared=... rationale={...}` format with rationale clause |
| C-33 | 15 | PASS | Gate block states "The `census-distribution:` value in this block is the authoritative value for Summary consumption. Summary's `mechanism-distribution:` field is a copy of this block's `census-distribution:` field — not a recount." Names Sub-task A explicitly via `source: S5.5-Sub-task-A`. |
| C-34 | 15 | PASS | `source: group-candidate-N` back-reference in each `pattern-N:` Multi-pattern entry |
| C-35 | 15 | PASS | Structured `S6.5-CENSUS-GATE:` block with `census-distribution:` field holding verbatim S5.5 Sub-task A value; "The `## Summary` section header must not appear before this block is written"; gate-status check defined. Value-binding and sequencing both enforced. |
| C-36 | 15 | PASS | `## Cross-Field Verification (C-36)` table with `mechanism-type-shared (at fill site) | mechanism-type-shared (from staging) | verdict` columns — mismatch is a visible row failure; no findings re-inspection required. |
| **Total** | **160** | **160/160** | |

---

### V-02 — Phrasing Register: SHALL/SHALL NOT Constraint Language

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-26–C-34 | 130 | PASS | Inherits R12 V-04 baseline; prohibition-register form doesn't break any prior criterion. |
| C-35 | 15 | PARTIAL (8) | "SHALL NOT write `## Summary` header until gate token is emitted" enforces sequencing strongly. But C-35 requires the gate token to **encode the verbatim `mechanism-distribution:` value** in a structural field — the prohibition designates the sequencing constraint but doesn't specify a gate token format with a named `census-distribution:` binding field. Value-binding is implied, not structural. |
| C-36 | 15 | PASS | "SHALL equal the value on the named staging line; any inequality is a C-36 violation" — explicit equality predicate embedded in spec as a named rule. Mismatch is a detectable violation without re-inspection. |
| **Total** | **160** | **153/160** | |

---

### V-03 — Lifecycle Emphasis: S6.5 as Named Step with Entry/Exit Conditions

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-26–C-34 | 130 | PASS | Inherits R12 V-04 baseline; lifecycle framing strengthens C-33 (Summary prerequisites block explicitly names S5.5). |
| C-35 | 15 | PASS | S6.5 as a named lifecycle step with entry condition (S5.5 Sub-tasks A and B complete), job (emit gate token encoding verbatim value), and exit condition (gate token written, `gate-status: OPEN`). The exit condition makes the gate token an auditable state transition, not a behavioral instruction — satisfies C-35's lifecycle-invariant requirement. |
| C-36 | 15 | PARTIAL (8) | Lifecycle emphasis targets C-35 and C-33. No cross-field verification table or explicit equality predicate for `mechanism-type-shared:` vs staging line value is introduced. Staging-to-template consistency check is implied by the audit chain but not structurally enforced as a post-population row operation. |
| **Total** | **160** | **153/160** | |

---

### V-04 — Role Sequence: Expert Returns for C-36 Verification

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-26–C-34 | 130 | PASS | Inherits R12 V-04 baseline; Expert holding staging registry reinforces C-34 back-reference chain and C-32 staging decision ownership. |
| C-35 | 15 | PARTIAL (8) | The Expert returning after template population is a behavioral role re-entry. C-35 requires a structural blocking gate — a gate token whose emission is the lifecycle precondition for writing the Summary header, and that encodes the verbatim `mechanism-distribution:` value. Expert return does not create the blocking gate token or its value-encoding obligation. |
| C-36 | 15 | PASS | Dedicated Expert verification step after template population, with access to the staging registry, explicitly compares `mechanism-type-shared:` at the fill site against the named `group-candidate-N` staging line. Role separation makes this a context-appropriate verification: Expert holds the contract ground truth (staging decisions), Automate holds the fill result — comparison is deterministic at the role boundary. |
| **Total** | **160** | **153/160** | |

---

### V-05 — Ceiling Test: Role-Sequence + Lifecycle-Emphasis + Output-Format

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-26–C-34 | 130 | PASS | All three axes additive; no prior criterion broken. |
| C-35 | 15 | PASS | V-01 axis (structured gate token block with `census-distribution:` field) + V-03 axis (S6.5 as named lifecycle step with entry/exit conditions). Double-enforced: value is structurally bound in the token format AND the lifecycle step formalizes it as an auditable state transition. Strongest C-35 form across all variations. |
| C-36 | 15 | PASS | V-01 axis (cross-field verification table with verdict column) + V-04 axis (Expert returns for verification using staging registry). Double-enforced: structural row format makes mismatches visible without re-inspection AND the Expert role holds the canonical staging decisions, making the comparison role-authoritative rather than author-self-checked. |
| **Total** | **160** | **160/160** | |

---

### Composite Scores and Ranking

| Rank | Variation | Score | Delta from Max | C-35 | C-36 |
|------|-----------|-------|----------------|------|------|
| 1 | V-01 | 160/160 | 0 | PASS | PASS |
| 1 | V-05 | 160/160 | 0 | PASS (double) | PASS (double) |
| 3 | V-02 | 153/160 | -7 | PARTIAL | PASS |
| 3 | V-03 | 153/160 | -7 | PASS | PARTIAL |
| 3 | V-04 | 153/160 | -7 | PARTIAL | PASS |

**Tie note — V-01 vs V-05:** Both achieve 160/160. V-05 is architecturally stronger (each new criterion enforced by two independent mechanisms), but the rubric criteria are binary; both score PASS on C-35 and C-36. V-01 demonstrates that output-format alone is sufficient to close both new criteria; V-05 demonstrates that combining all three axes produces an overspecified, audit-robust ceiling.

**Why single-axis failures occur:**
- V-02 (phrasing only): SHALL/SHALL NOT enforces ordering but does not create the value-binding structure C-35 requires — the gate token format is unspecified
- V-03 (lifecycle only): entry/exit conditions formalize C-35 but no post-population consistency table is specified for C-36
- V-04 (role only): Expert return satisfies C-36 at the role boundary but the blocking gate artifact (C-35) is absent

---

### EXCELLENCE SIGNALS

From V-01 and V-05 (the top-scoring variations):

**Signal 1 — Value-binding gate token field (`census-distribution:` in `S6.5-CENSUS-GATE:` block).** Prior rounds enforced the sequencing constraint behaviorally ("don't write Summary until..."). C-35 requires the gate token to *carry the value* — the `census-distribution:` named field makes the gate auditable by field inspection: either the field is present with the correct verbatim value, or the gate is not satisfied. The structural block converts a "did you wait?" check into a "does the token contain the right value?" check, which is mechanically verifiable.

**Signal 2 — Cross-field verdict table as post-population integrity surface.** Prior rounds required the `source: group-candidate-N` back-reference (C-34) as a traceability annotation. C-36 requires a *consistency predicate* — the table's verdict column converts the annotation into an enforceable check. The `mechanism-type-shared (at fill site) | mechanism-type-shared (from staging) | verdict` column structure makes re-derivation at the template site produce a visible row failure rather than an invisible silent substitution. The table is written **after all pattern entries are complete**, making it a post-population audit surface rather than an inline authoring constraint.

**Signal 3 (V-05 exclusive) — Dual-mechanism enforcement.** For both C-35 and C-36, V-05 applies two independent mechanisms: format (structural artifact) + lifecycle/role (process enforcement). The format mechanism catches failures at the artifact level; the role mechanism engages the right context (Expert holds staging decisions). This redundancy means neither mechanism depends on the other — a spec with only the table still catches re-derivation; a spec with only the Expert role still prevents template-site substitution.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["value-binding gate token: census-distribution field in S6.5-CENSUS-GATE block makes C-35 verifiable by field inspection rather than behavioral sequencing check", "post-population cross-field verdict table: mechanism-type-shared comparison with verdict column converts source back-reference from traceability annotation into structural consistency predicate detectable without findings re-inspection"]}
```
