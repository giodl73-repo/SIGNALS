Here are the 5 complete variations for trace-contract Round 14 (census rubric), written to `simulations/quest/golden/trace-contract-variate-R14-census-2026-03-15.md`.

---

## Round 14 Variation Map

| Variation | Axis | C-37 | C-38 | Key design decision |
|-----------|------|------|------|---------------------|
| **V-01** | Role sequence — Automate as encoding witness at S6.5 | PASS | PARTIAL | Expert names Sub-task A source + emits `gate-provenance: S5.5-Sub-task-A`; verdict-gate rule blocks Summary on FAIL but resolution path says "correct the source grouping" without naming S5.5 Sub-task B as the amendment site |
| **V-02** | Output format — schema-defined gate block with required-fields manifest | PASS | PASS | Named schema declares `census-distribution:` and `gate-provenance:` as co-required sibling fields; resolution path explicitly names S5.5 Sub-task B staging line as the only valid amendment target |
| **V-03** | Lifecycle emphasis — S6.5 as phase with ENTER/EXIT/BLOCKED conditions | PARTIAL | PASS | BLOCKED exit condition converts verdict-gate rule from advisory to structural; provenance-binding sub-step names Sub-task A but omits the `gate-provenance: S5.5-Sub-task-A` field emission |
| **V-04** | Phrasing register — formal imperative throughout ("Bind:", "Emit:", "Block:", "Require:") | PASS | PASS | "Bind: census-distribution := Sub-task A verbatim" + "Emit: gate-provenance: S5.5-Sub-task-A" + "Block: cannot proceed while FAIL" + "Require: amend S5.5 Sub-task B" |
| **V-05** | Role sequence + Lifecycle emphasis (combined) | PASS | PASS | Expert owns Step 2 provenance-binding as named step; BLOCKED exit condition; Automate witness makes Expert's attestation falsifiable; amendment target named as census stage |

**Predicted diagnostic value:** V-01's C-38 PARTIAL will confirm that amendment-target specificity is a distinct requirement from gate-blocking. V-03's C-37 PARTIAL will confirm that the `gate-provenance:` field is required independently of lifecycle framing. Together they isolate the two components of C-37 and C-38 cleanly.
