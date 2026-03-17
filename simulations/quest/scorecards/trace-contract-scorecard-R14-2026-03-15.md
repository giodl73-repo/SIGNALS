## Scoring: trace-contract Round 14

### Rubric Baseline

All variations inherit C-26–C-36 from R13 V-05 (baseline = 145 pts). Only C-37 and C-38 are differentiated this round.

---

### Per-Criterion Analysis

#### C-37 — Provenance-binding sub-step (15 pts)
Requirements: named sub-step within S6.5; Sub-task A cited as authoritative source; `census-distribution:` is verbatim copy; `gate-provenance: S5.5-Sub-task-A` field emitted.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS** | Expert writes Step 2 with explicit provenance-binding; gate token includes `gate-provenance: S5.5-Sub-task-A`; Automate witness confirms fidelity |
| V-02 | **PASS** | Schema declares `gate-provenance:` as a required field alongside `census-distribution:`; provenance-binding instruction explicitly names Sub-task A; omitting either field is a schema violation |
| V-03 | **PARTIAL** | Sub-task A named as source; `census-distribution:` copied verbatim; but gate token emits only `source:`, `census-distribution:`, `gate-status:` — `gate-provenance: S5.5-Sub-task-A` field absent. C-37 requires the explicit field, not just Source naming in the instruction prose. (8/15) |
| V-04 | **PASS** | `Bind: census-distribution := Sub-task A mechanism-distribution verbatim` + `Emit: gate-provenance: S5.5-Sub-task-A`; `Assert: gate-provenance: S5.5-Sub-task-A is present`; `Prohibit: omitting gate-provenance:` |
| V-05 | **PASS** | Expert owns Step 2 explicitly; 3-sub-step execution protocol; `gate-provenance: S5.5-Sub-task-A` is Expert's attestation field; Automate Step 3 makes the attestation falsifiable by character-for-character comparison |

#### C-38 — Verdict-gate closure rule (15 pts)
Requirements: blocks `## Summary` while any FAIL row exists; resolution path names S5.5 Sub-task B staging line as amendment site (not fill-site patch); corrections traceable to census stage.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PARTIAL** | Gate blocks Summary on FAIL ✓; "To advance: correct the source grouping in Sub-task B" — names Sub-task B but does not explicitly prohibit fill-site patching or name the staging line as the only valid amendment target. No "do not patch the fill site" constraint. (8/15) |
| V-02 | **PASS** | "Do not patch the mechanism-type-shared: value at the Patterns fill site — a direct patch at the template is not a valid resolution. The staging line is the authoritative record; the template fill site is a copy of it. Amend at the source, re-propagate." Full staging-line specificity + fill-site prohibition. |
| V-03 | **PASS** | BLOCKED exit condition defined at phase level; "This is the only valid resolution path — amending the staging line at the census stage and re-propagating forward. Do not overwrite mechanism-type-shared: at the Patterns fill site without amending the staging line first." Structural BLOCKED state + explicit fill-site prohibition. |
| V-04 | **PASS** | `Block:` + `Require: amend S5.5 Sub-task B staging line` + `Prohibit: overwriting mechanism-type-shared: at fill site without amending staging line` + `Assert: every correction traceable to census stage`. All four requirements met in imperative command form. |
| V-05 | **PASS** | CENSUS-GATE phase EXIT condition BLOCKED defined; "This is the census stage amendment — do not patch the mechanism-type-shared: value at the Patterns fill site directly. The staging line is the authoritative record; the fill site is a derived copy." Plus traceability assertion in GATE-OPEN token. |

---

### Composite Scores

| Variation | C-26–C-36 | C-37 | C-38 | Total | % |
|-----------|-----------|------|------|-------|---|
| V-01 | 145 | 15 | 8 | **168** | 88.4% |
| V-02 | 145 | 15 | 15 | **175** | 92.1% |
| V-03 | 145 | 8 | 15 | **168** | 88.4% |
| V-04 | 145 | 15 | 15 | **175** | 92.1% |
| V-05 | 145 | 15 | 15 | **175** | 92.1% |

**Rank:** V-02 = V-04 = V-05 (175) > V-01 = V-03 (168)

---

### Diagnostic Value Confirmed

Predicted failure modes materialized exactly:

- **V-01 C-38 PARTIAL confirmed:** Amendment-target specificity (explicit prohibition of fill-site patching) is a distinct requirement from gate-blocking. Naming "Sub-task B" without "do not patch the fill site" is insufficient — the prohibition is the discriminating element.
- **V-03 C-37 PARTIAL confirmed:** `gate-provenance: S5.5-Sub-task-A` field emission is required independently of lifecycle framing. Phase ENTER/EXIT discipline does not substitute for the named provenance field — structural phase architecture and explicit field presence are orthogonal requirements.

---

### Excellence Signals (Top-Scoring Variations)

**From V-02 — Schema co-requirement as structural field constraint:**
Declaring `census-distribution:` and `gate-provenance:` as named co-required fields in a gate token schema converts their joint presence from a prose convention into a structural property: omitting either field is a schema violation detectable by field inspection, not by reading authoring prose. The schema header externalizes the constraint from the instruction into the output form itself.

**From V-04 — Formal imperative as execution-method specification:**
`Bind: X := Y` (rather than "copy Y into X") specifies the computation method, not only the expected result. A verbatim-copy command is non-compliant even when re-derivation produces the correct value — the constraint is on method, not coincident outcome. `Prohibit:` constructions eliminate behavioral hedges that allow partial compliance.

**From V-05 — Role ownership of attestation + witness falsifiability:**
Assigning the provenance-binding sub-step to the census owner by role name makes re-derivation a role-boundary violation (only the Expert can attest their own census output). The Automate witness step separates claim from verification: the Expert's `gate-provenance:` attestation is a claim; Automate's character-for-character comparison is the falsifiability test. This two-party structure makes the provenance guarantee auditable at the gate boundary without re-inspecting the findings section.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["schema co-requirement — declaring census-distribution: and gate-provenance: as co-required sibling fields in a named schema converts their joint presence from a prose convention into a structural constraint detectable by field inspection", "formal imperative as execution-method specification — Bind: X := Y constrains the computation method not just the result, making re-derivation that produces the correct value non-compliant; Prohibit: constructions eliminate behavioral hedges that allow partial compliance", "role ownership + witness falsifiability — assigning provenance-binding to the census owner by name makes re-derivation a role-boundary violation; a separate witness role provides falsifiability by character-for-character comparison, separating attestation claim from verification"]}
```
