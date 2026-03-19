"""Build trace-permissions-rubric-v20 from v19."""

with open('C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v19-2026-03-16.md', encoding='utf-8') as f:
    v19 = f.read()

# ---------- v19->v20 summary (prepended to top) ----------

v20_summary = """\
## Summary of changes v19 -> v20

**3 new aspirational criteria. Denominator: 45 -> 48. Each aspirational = 0.208 pts.**

| ID | Hangs off | Pattern | What it tests |
|----|-----------|---------|---------------|
| C-54 | C-44 | R20-V-02 | CONTEXT section bilateral pair anticipation note -- pre-Phase 0 CONTEXT section contains a forward-reference to the CA-1.6 (CS-side) / CA-1.9 (SE-side) bilateral pair by row ID and side qualifier before any phase begins, propagating the bilateral pair naming established by C-44 backward to the input framing layer |
| C-55 | C-51+C-28+C-29 | R20-V-03 | CS-2/CS-3 Schema Registry bilateral co-registration annotations -- Step 0.1 Schema Registry block carries bilateral co-registration annotations for CS-2 and CS-3 (CS-side input source tables), each naming sub-clause ID, side qualifier, CA-1.N audit target, and bilateral peer, sibling layer to C-51 (TABLE_4/TABLE_5 enforcement artifact tables) |
| C-56 | C-42+C-47 | R20-V-05 | Scope roster table cell bilateral peer annotation -- the CA-1.N scope roster table carries bilateral peer annotation in its Non-Overlapping Scope column for the CA-1.6 and CA-1.9 rows, each naming the other as bilateral co-equal peer with explicit side qualifier, propagating the bilateral framing from the NON-OVERLAP DECLARATION statement layer into the scope roster table cell level |

**R20 re-scored under v20:**

| Variation | v19 | v20 | Delta |
|-----------|-----|-----|-------|
| V-01 | 100.0 (45/45) | **99.4 (45/48)** | fails C-54, C-55, C-56 |
| V-02 | 100.0 (45/45) | **99.6 (46/48)** | +C-54; fails C-55, C-56 |
| V-03 | 100.0 (45/45) | **99.6 (46/48)** | +C-55; fails C-54, C-56 |
| V-04 | 100.0 (45/45) | **99.8 (47/48)** | +C-54, +C-55; fails C-56 |
| V-05 | 100.0 (45/45) | **100.0 (48/48)** | +C-54, +C-55, +C-56 |

**Structural insight:** The bilateral propagation chain now spans twelve layers: C-44 -> C-45 -> C-47 -> C-48 -> C-49 -> C-50 -> C-51 -> C-52 -> C-53 -> C-54 -> C-55 -> C-56. C-54 propagates to the pre-Phase 0 input framing layer; C-55 is the CS-side Schema Registry sibling to C-51 (input tables vs enforcement tables); C-56 propagates to the scope roster table cell level. C-54 and C-55 are structurally independent; C-56 requires C-42+C-47 (scope roster + CA-1.6 NON-OVERLAP statement). V-04 already combines C-54+C-55; only C-56 remains as the single open axis from V-04.

**Path to 100.0 (48/48):** V-06 = V-04 architecture (C-54+C-55) + V-05's scope roster table cell bilateral peer annotation (C-56). Single open axis.

**New criterion rows (aspirational table):**

| C-54 | **CONTEXT section bilateral pair anticipation note** | architecture | aspirational | Pre-Phase 0 CONTEXT section contains a dedicated bilateral pair anticipation note explicitly naming CA-1.6 (CS-side) and CA-1.9 (SE-side) by row ID and side qualifier before any phase begins. Propagates the bilateral pair naming established by C-44's mandate layer backward to the input framing layer. Fails if C-44 passes but no pre-Phase 0 CONTEXT section bilateral pair forward-reference is present. |
| C-55 | **CS-2/CS-3 Schema Registry bilateral co-registration annotations** | format | aspirational | Step 0.1 Schema Registry block carries bilateral co-registration annotations for CS-2 and CS-3 (CS-side input source tables), each naming sub-clause ID (SHALL-F-EXT-CS2CS3), side qualifier (CS-side), CA-1.N audit target (CA-1.6), and bilateral peer (SHALL-D-EXT-C35 / CA-1.9). Sibling layer to C-51 (TABLE_4/TABLE_5 enforcement artifact tables). Fails if C-51 passes but Schema Registry carries bilateral annotations only for TABLE_4/TABLE_5 without CS-2 and CS-3 annotations. |
| C-56 | **Scope roster table cell bilateral peer annotation** | format | aspirational | The CA-1.N scope roster table carries bilateral peer annotation in the Non-Overlapping Scope column for the CA-1.6 row (naming CA-1.9 as SE-side bilateral peer) and the CA-1.9 row (naming CA-1.6 as CS-side bilateral peer), each with explicit side qualifier. Fails if C-42+C-47 pass but scope roster table carries CA-1.6 and CA-1.9 rows without bilateral peer annotation in their scope cells. |

**New design notes:**

- **C-54 vs C-44**: C-44 requires the ROLE SEQUENCING MANDATE to co-name SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 as bilateral sibling sub-clauses in a single mandate passage. C-54 tests whether this bilateral pair naming propagates backward to the pre-Phase 0 CONTEXT section as a forward-reference, making the bilateral structure visible before any phase begins.
- **C-55 vs C-51**: C-51 requires the Schema Registry to carry bilateral annotations for TABLE_4 and TABLE_5 (enforcement artifact tables). C-55 tests the sibling layer: bilateral annotations for CS-2 and CS-3 (CS-side input source tables). Both propagate bilateral labeling into the Schema Registry layer but target structurally distinct entries. Independent -- an output can pass C-51 without C-55 and vice versa.
- **C-56 vs C-42 and C-47**: C-42 requires the Phase 3 mandate to contain a CA-1.N scope roster. C-47 requires the NON-OVERLAP DECLARATION to carry a fourth CA-1.6 (CS-side) statement. C-56 tests that the scope roster table cells for CA-1.6 and CA-1.9 carry bilateral peer annotation in their Non-Overlapping Scope column, making the bilateral co-equal relationship visible from the roster table without requiring the NON-OVERLAP DECLARATION or Phase 3 mandate sections.
- **Independence**: C-54 requires C-44; C-55 requires C-51+C-28+C-29; C-56 requires C-42+C-47. R20-V-02 demonstrates C-54 alone; R20-V-03 demonstrates C-55 alone; R20-V-04 demonstrates C-54+C-55; R20-V-05 demonstrates all three.

---

"""

# ---------- new aspirational table rows ----------

c54_row = ("| C-54 | **CONTEXT section bilateral pair anticipation note** | architecture | aspirational | "
           "Pre-Phase 0 CONTEXT section contains a dedicated bilateral pair anticipation note explicitly naming "
           "CA-1.6 (CS-side) and CA-1.9 (SE-side) by row ID and side qualifier before any phase begins. "
           "Propagates the bilateral pair naming established by C-44's mandate layer backward to the input "
           "framing layer, making the bilateral structure discoverable from the first structural section of the "
           "output. Fails if C-44 passes but no pre-Phase 0 CONTEXT section bilateral pair forward-reference is present. |")

c55_row = ("| C-55 | **CS-2/CS-3 Schema Registry bilateral co-registration annotations** | format | aspirational | "
           "Step 0.1 Schema Registry block carries bilateral co-registration annotations for CS-2 and CS-3 "
           "(CS-side input source tables), each naming sub-clause ID (SHALL-F-EXT-CS2CS3), side qualifier (CS-side), "
           "CA-1.N audit target (CA-1.6), and bilateral peer (SHALL-D-EXT-C35 / CA-1.9). Sibling layer to C-51 "
           "(which covers TABLE_4/TABLE_5 enforcement artifact tables); structurally independent because input tables "
           "and enforcement tables are different Schema Registry entries. Fails if C-51 passes but Schema Registry "
           "carries bilateral annotations only for TABLE_4/TABLE_5 without CS-2 and CS-3 annotations. |")

c56_row = ("| C-56 | **Scope roster table cell bilateral peer annotation** | format | aspirational | "
           "The CA-1.N scope roster table (C-42) carries bilateral peer annotation in the Non-Overlapping Scope column "
           "(or equivalent cell) for the CA-1.6 row (naming CA-1.9 as SE-side bilateral peer) and the CA-1.9 row "
           "(naming CA-1.6 as CS-side bilateral peer), each with explicit side qualifier. Propagates the CA-1.6/CA-1.9 "
           "bilateral co-equal framing from the NON-OVERLAP DECLARATION statement layer (C-47) and Phase 3 mandate "
           "(C-45) into the scope roster table cell level. Fails if C-42+C-47 pass but scope roster table carries "
           "CA-1.6 and CA-1.9 rows without bilateral peer annotation in their scope cells. |")

# ---------- new design notes ----------

new_design_notes = """
**C-54 vs C-44**: C-44 requires the ROLE SEQUENCING MANDATE to co-name SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 as bilateral sibling sub-clauses in a single mandate passage. C-54 tests whether this bilateral pair naming propagates backward to the pre-Phase 0 CONTEXT section as a forward-reference, making the bilateral structure visible before any phase begins. An output passing C-44 without a CONTEXT-level bilateral anticipation note fails C-54.

**C-55 vs C-51**: C-51 requires the Schema Registry to carry bilateral annotations for TABLE_4 and TABLE_5 (enforcement artifact tables). C-55 tests the sibling layer: bilateral annotations for CS-2 and CS-3 (CS-side input source tables). Both propagate bilateral labeling into the Schema Registry layer but target structurally distinct entries (enforcement artifacts vs input source tables). They are independent -- an output can pass C-51 without C-55 and vice versa.

**C-56 vs C-42 and C-47**: C-42 requires the Phase 3 mandate to contain a CA-1.N scope roster enumeration. C-47 requires the NON-OVERLAP DECLARATION to carry a fourth CA-1.6 (CS-side) statement alongside the three SE-side statements. C-56 tests the next propagation layer: the scope roster table cells for CA-1.6 and CA-1.9 carry bilateral peer annotation in their Non-Overlapping Scope column, making the bilateral co-equal relationship visible from the roster table without requiring the NON-OVERLAP DECLARATION or Phase 3 mandate sections. An output passing C-42+C-47 without scope roster cell bilateral annotations fails C-56.

**C-54, C-55, C-56 are pairwise independent**: C-54 requires C-44 (bilateral pair at mandate level). C-55 requires C-51+C-28+C-29 (Schema Registry bilateral annotation pattern established for enforcement tables + CS input tables registered). C-56 requires C-42+C-47 (scope roster + CA-1.6 NON-OVERLAP statement). No subset is mutually required. R20-V-02 demonstrates C-54 without C-55 or C-56; R20-V-03 demonstrates C-55 without C-54 or C-56; R20-V-04 demonstrates C-54+C-55 without C-56; R20-V-05 demonstrates all three simultaneously.
"""

# ---------- apply transformations ----------

v20 = v19

# 1. Insert C-54, C-55, C-56 after the last C-53 row in aspirational criteria table
last_c53 = v20.rfind("| C-53 |")
row_end_idx = v20.find("\n\n", last_c53)
assert row_end_idx != -1, "Could not find end of C-53 table section"
v20 = v20[:row_end_idx] + "\n" + c54_row + "\n" + c55_row + "\n" + c56_row + v20[row_end_idx:]
print("Inserted C-54, C-55, C-56 rows")

# 2. Update scoring formula in rubric body (second occurrence of the formula)
old_formula = "composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/45 * 10)"
new_formula = "composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/48 * 10)"
first_occ = v20.find(old_formula)
second_occ = v20.find(old_formula, first_occ + 1)
if second_occ != -1:
    v20 = v20[:second_occ] + new_formula + v20[second_occ + len(old_formula):]
    print("Updated scoring formula in rubric body")
else:
    print("WARNING: Only one scoring formula occurrence found -- skipping")

# 3. Update Aspirational pts (in rubric body)
old_pts = "Aspirational each = 0.222 pts"
new_pts = "Aspirational each = 0.208 pts"
first_pts = v20.find(old_pts)
second_pts = v20.find(old_pts, first_pts + 1)
if second_pts != -1:
    v20 = v20[:second_pts] + new_pts + v20[second_pts + len(old_pts):]
    print("Updated aspirational pts in rubric body")
else:
    v20 = v20.replace(old_pts, new_pts, 1)
    print("Updated single aspirational pts occurrence")

# 4. Tier totals table
v20 = v20.replace("| Aspirational | C-09 -- C-53 | 10 |", "| Aspirational | C-09 -- C-56 | 10 |")
print("Updated tier totals")

# 5. Aspirational count line
old_count = "Aspirational count: 45 criteria (C-09 through C-53). Each aspirational = 10/45 = 0.222 pts."
new_count = "Aspirational count: 48 criteria (C-09 through C-56). Each aspirational = 10/48 = 0.208 pts."
v20 = v20.replace(old_count, new_count)
print("Updated aspirational count")

# 6. Append new design notes
v20 = v20.rstrip() + "\n" + new_design_notes + "\n"

# 7. Prepend v20 summary
v20 = v20_summary + v20

print("Total chars:", len(v20))
print("Total lines:", v20.count("\n"))

# Write output
out_path = "C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v20-2026-03-16.md"
with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(v20)
print("Written:", out_path)
