Written to `simulations/quest/golden/quest-rubric-variate-v13-R13-2026-03-16.md`.

---

## Round 13 Variations — Design Summary

Five complete prompt bodies targeting C-36, C-37, and C-38.

### Variation Map

| Var | Axis | C-36 pred | C-37 pred | C-38 pred | Key structural move |
|-----|------|-----------|-----------|-----------|---------------------|
| **V-01** | Phrasing register | **FAIL** | baseline | baseline | Every gate: `⛔ STOP` → "please ensure" / "consider pausing" / "it is recommended" |
| **V-02** | Output format | baseline | **FAIL** | baseline | Builder E+R audit + Dual Auditor: per-criterion `C-NN: flags [Y/N]` → numbered prose paragraphs bundling multiple properties |
| **V-03** | Inertia framing | baseline | baseline | **PASS** | Named `## DOMINANT FAILURE MODE` block (Threshold Tightening Without New Territory) placed before DEFINER ROLE — self-contained, labeled, explains primacy |
| **V-04** | Format + framing | baseline | **FAIL** | **PASS** | V-02 prose audit + V-03 DFM callout; tests C-37/C-38 independence |
| **V-05** | All three | **FAIL** | **FAIL** | **PASS** | Advisory gates + prose audit + DFM callout; tests joint activation stability |

### Three New Criteria Targeted

**C-36 (STOP-phrasing register uniformity):** V-01 and V-05 use advisory phrasing ("please ensure", "consider pausing", "you may wish to") at all gate positions. Predicted cascade: C-31 (no independent STOP per absent position), C-33 (Phase 1 gate destination naming weakened by advisory framing).

**C-37 (Atomic gate-item structure):** V-02 and V-04/V-05 replace the per-criterion `C-NN: Text flags: [Y/N, Y/N, Y/N]` structured format with prose quality-review paragraphs. Each paragraph bundles direction + contrast + causal-chain + location + observable + qualitative checks into narrative. Predicted degradation: C-05, C-16, C-17 PARTIAL (bundled items cannot be evaluated as independent binary gates).

**C-38 (Pre-role dominant failure mode callout):** V-03, V-04, V-05 add a discrete named block before any role declaration. The block names the failure mode ("Threshold Tightening Without New Territory"), explains why it is dominant (same spec language motivates essential + aspirational threshold forms), and provides an observable indicator (two criteria share a property name, differ only in threshold). Self-contained — readable without the criteria. The two ablation axes in V-04 and V-05 do not touch the pre-role structural slot, so C-38 PASS is predicted for all three DFM variations regardless of what happens inside the roles.
