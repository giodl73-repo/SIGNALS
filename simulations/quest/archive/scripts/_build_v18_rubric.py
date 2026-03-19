with open('C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v17-2026-03-16.md', encoding='utf-8') as f:
    v17 = f.read()

v18_header = (
    "Written to `simulations/quest/rubrics/trace-permissions-rubric-v18-2026-03-16.md`.\n\n"
    "---\n\n"
    "**Summary of changes v17 -> v18:**\n\n"
    "**3 new aspirational criteria. Denominator: 39 -> 42. Each aspirational = 0.238 pts.**\n\n"
    "| ID | Hangs off | Pattern | What it tests |\n"
    "|----|-----------|---------|---------------|\n"
    "| C-48 | C-38+C-40+C-44 | R18-V-03 | SHALL sub-clause declaration bilateral side-labeling -- "
    "SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 obligation declaration text each carry inline "
    "`*(SE-side bilateral sub-clause, verified at CA-1.9)*` and `*(CS-side bilateral sub-clause, verified at CA-1.6)*` "
    "qualifiers, propagating the bilateral SE+CS labeling from C-44's mandate-level co-citation into the sub-clause definition text itself |\n"
    "| C-49 | C-44+C-45 | R18-V-02 | Verdict bilateral sub-clause verification pair echo -- "
    "the Verdict or summary section co-names CA-1.9 (SE-side: SHALL-D-EXT-C35) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3) "
    "with explicit side qualifiers and a bilateral parity-confirmation statement, propagating the bilateral SE+CS co-naming "
    "from the Phase 3 mandate (C-45) into the terminal verdict layer |\n"
    "| C-50 | C-11+C-44 | R18-V-05 | CEM bilateral M4 sub-clause annotation block -- "
    "an annotation block co-located with the CEM table co-declares SHALL-D-EXT-C35 (SE-side, M4->CA-1.9) and "
    "SHALL-F-EXT-CS2CS3 (CS-side, M4->CA-1.6) as bilateral pair M4 extensions, each entry naming sub-clause ID, "
    "side qualifier, M4 target row, and bilateral co-declaration peer |\n\n"
    "**Structural insight:** R18 extends the bilateral propagation chain to three new structural layers. "
    "The full chain now spans: C-44 (Phase 0 obligation mandate) -> C-45 (Phase 3 verification mandate) -> "
    "C-47 (NON-OVERLAP DECLARATION statements) -> C-48 (SHALL sub-clause definition text) -> "
    "C-49 (terminal Verdict summary) -> C-50 (CEM table annotation). "
    "Each layer independently propagates the SE+CS bilateral pattern into a distinct structural position.\n\n"
    "**R18 re-scored under v18:**\n\n"
    "| Variation | v17 | v18 | Delta |\n"
    "|-----------|-----|-----|-------|\n"
    "| V-01 | 100.0 (39/39) | **92.9 (39/42)** | fails C-48, C-49, C-50 |\n"
    "| V-02 | 100.0 (39/39) | **95.2 (40/42)** | +C-49; fails C-48, C-50 |\n"
    "| V-03 | 100.0 (39/39) | **95.2 (40/42)** | +C-48; fails C-49, C-50 |\n"
    "| V-04 | 100.0 (39/39) | **97.6 (41/42)** | +C-48, +C-49; fails C-50 |\n"
    "| V-05 | 100.0 (39/39) | **100.0 (42/42)** | +C-48, +C-49, +C-50 |\n\n"
    "**Path to 100.0 (42/42):** Three independent open axes. V-06 = V-04 architecture (C-48+C-49) + "
    "V-05's CEM bilateral M4 annotation block (C-50). All R18 innovations are independent; V-04 already "
    "combines C-48+C-49; only C-50 remains as the single open axis from V-04.\n\n"
    "---\n\n"
)

# Strip old header, keep everything from v16->v17 summary onwards
old_body_start = v17.index('---\n\n**Summary of changes v16 -> v17:**')
v18 = v18_header + v17[old_body_start:]

# Update scoring formula
v18 = v18.replace(
    'composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/39 * 10)',
    'composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/42 * 10)'
)
v18 = v18.replace(
    'Essential each = 12 pts | Recommended each = 10 pts | Aspirational each = 0.256 pts',
    'Essential each = 12 pts | Recommended each = 10 pts | Aspirational each = 0.238 pts'
)

# New criteria row texts
c48_text = (
    "**SHALL sub-clause declaration bilateral side-labeling** -- "
    "SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 obligation declaration text each carry inline bilateral side-qualifier annotations "
    "(e.g., `*(SE-side bilateral sub-clause, verified at CA-1.9)*` and `*(CS-side bilateral sub-clause, verified at CA-1.6)*`), "
    "propagating the bilateral SE+CS labeling from C-44's mandate-level co-citation into the sub-clause definition text itself. "
    "C-38 requires SHALL-D-EXT-C35 to be declared; C-40 requires SHALL-F-EXT-CS2CS3 to be declared; C-44 requires the mandate block "
    "to co-name both. C-48 tests that the co-naming extends into the definition text of each sub-clause, annotating each with its side "
    "role and the CA-1.N row where it is verified, making the bilateral structure discoverable at the declaration point without requiring "
    "the mandate block."
)
c48_pass = (
    "SHALL-D-EXT-C35 obligation declaration text contains an inline qualifier identifying it as the SE-side bilateral sub-clause "
    "and naming CA-1.9 as its verification row (e.g., `*(SE-side bilateral sub-clause, verified at CA-1.9)*` or equivalent inline annotation). "
    "SHALL-F-EXT-CS2CS3 obligation declaration text contains a symmetric inline qualifier identifying it as the CS-side bilateral sub-clause "
    "and naming CA-1.6 as its verification row (e.g., `*(CS-side bilateral sub-clause, verified at CA-1.6)*` or equivalent). "
    "Both annotations must appear within the SHALL obligation declaration text, not only in the mandate block (C-44) or preamble-anchor (C-38/C-40). "
    "An output where both sub-clauses are declared (C-38+C-40) and co-named in the mandate (C-44) but carry no inline side-qualifier annotations "
    "within the declaration text fails C-48. "
    "Distinction from C-44 (mandate-level bilateral co-citation) and C-38/C-40 (sub-clause declared + CA-1.N preamble-anchor cites it): "
    "C-48 tests that the bilateral side-labeling migrates from the mandate layer into the sub-clause definition text, creating self-annotated "
    "declarations that identify their side role and verification target without requiring readers to cross-reference the mandate paragraph."
)
c48_row = f"\n| C-48 | {c48_text} | architecture | aspirational | {c48_pass} |"

c49_text = (
    "**Verdict bilateral sub-clause verification pair echo** -- "
    "The Verdict or terminal summary section co-names CA-1.9 (SE-side: SHALL-D-EXT-C35) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3) "
    "as a bilateral sub-clause verification pair with explicit \"(SE-side)\" and \"(CS-side)\" qualifiers and an explicit bilateral "
    "parity-confirmation statement (e.g., \"bilateral parity confirmed\" or equivalent). "
    "This propagates the bilateral SE+CS co-naming from the Phase 3 verification mandate (C-45) into the terminal Verdict layer -- "
    "the downstream summary that reports the outcome of the CA verification pass. "
    "C-45 tests that the Phase 3 mandate co-names CA-1.9 and CA-1.6 as bilateral obligations; C-49 tests that the same bilateral framing "
    "propagates into the terminal verdict, making the bilateral parity outcome verifiable from the Verdict section alone without reading "
    "the Phase 3 mandate."
)
c49_pass = (
    "The Verdict or terminal summary section contains a bilateral sub-clause verification pair citation that: "
    "(1) names CA-1.9 with explicit \"(SE-side)\" qualifier and its SHALL sub-clause (SHALL-D-EXT-C35); "
    "(2) names CA-1.6 with explicit \"(CS-side)\" qualifier and its SHALL sub-clause (SHALL-F-EXT-CS2CS3); "
    "(3) includes an explicit bilateral parity-confirmation statement (e.g., \"bilateral parity confirmed\", "
    "\"bilateral sub-clause parity verified\", or equivalent). "
    "All three elements must appear in the Verdict or summary section. "
    "An output where the Verdict section cites CA-1.9 and CA-1.6 results separately without bilateral co-framing and parity-confirmation "
    "fails C-49. "
    "Distinction from C-45 (Phase 3 mandate bilateral verification echo): C-45 tests the obligation mandate layer "
    "(Phase 3 instruction block governing what must be verified); C-49 tests the terminal outcome layer "
    "(Verdict summary reporting what was verified), creating bilateral parity echo at both the mandate and verdict levels simultaneously."
)
c49_row = f"\n| C-49 | {c49_text} | architecture | aspirational | {c49_pass} |"

c50_text = (
    "**CEM bilateral M4 sub-clause annotation block** -- "
    "An annotation block co-located with the CEM table (C-11) co-declares SHALL-D-EXT-C35 (SE-side, M4->CA-1.9) and "
    "SHALL-F-EXT-CS2CS3 (CS-side, M4->CA-1.6) as bilateral pair M4 extensions, each entry naming its sub-clause identifier, "
    "side qualifier, M4 target CA-1.N row, distinctness note, and bilateral co-declaration peer. "
    "C-11 requires the CEM table to be present with M4 pre-assignment entries; C-44 requires the mandate block to co-name both sub-clauses. "
    "C-50 tests that the bilateral pair is also co-declared in an annotation block structurally adjacent to the CEM table itself, "
    "making the bilateral M4 extension structure discoverable from the CEM section without requiring the mandate block."
)
c50_pass = (
    "An annotation block (labeled \"Bilateral sub-clause M4 extensions\" or equivalent) appears immediately following or within "
    "the CEM table section and contains two entries: "
    "(1) SHALL-D-EXT-C35 entry naming it as SE-side, M4 target CA-1.9, distinctness note (distinct from CA-1.4 or equivalent), "
    "and co-declaration peer (SHALL-F-EXT-CS2CS3); "
    "(2) SHALL-F-EXT-CS2CS3 entry naming it as CS-side, M4 target CA-1.6, distinctness note (distinct from CA-1.5 or equivalent), "
    "and co-declaration peer (SHALL-D-EXT-C35). "
    "The block must be structurally adjacent to the CEM table, not merely contained in the mandate block (C-44) or elsewhere. "
    "An output where both sub-clauses exist in the CEM table (C-11) and are co-named in the mandate (C-44) but carry no CEM-adjacent "
    "bilateral annotation block fails C-50. "
    "Distinction from C-44 (mandate-level bilateral co-citation) and C-11 (CEM table present): "
    "C-50 tests that the bilateral M4 extension pair is declared in a structured block co-located with the CEM table itself, "
    "making bilateral CEM structure visible at the assignment layer without requiring the mandate paragraph."
)
c50_row = f"\n| C-50 | {c50_text} | architecture | aspirational | {c50_pass} |"

# Find end of C-47 row and insert C-48, C-49, C-50 after it
c47_marker = '\n| C-47 |'
idx = v18.rfind(c47_marker)
c47_line_end = v18.index('\n', idx + 1)
v18 = v18[:c47_line_end] + c48_row + c49_row + c50_row + v18[c47_line_end:]

# Update tier totals
v18 = v18.replace(
    '| Aspirational | C-09 -- C-47 | 10 |',
    '| Aspirational | C-09 -- C-50 | 10 |'
)
v18 = v18.replace(
    'Aspirational count: 39 criteria (C-09 through C-47). Each aspirational = 10/39 = 0.256 pts.',
    'Aspirational count: 42 criteria (C-09 through C-50). Each aspirational = 10/42 = 0.238 pts.'
)

# Design notes for C-48, C-49, C-50
design_notes = (
    "\n**C-48 vs C-44, C-38, and C-40**: C-38 requires SHALL-D to carry a named extension sub-clause (SHALL-D-EXT-C35) and CA-1.9 to cite it. "
    "C-40 requires SHALL-F to carry a named extension sub-clause (SHALL-F-EXT-CS2CS3) and CA-1.6 to cite it. "
    "C-44 requires the ROLE SEQUENCING MANDATE to co-name both sub-clauses in a single mandate passage. "
    "C-48 tests the next propagation layer: each sub-clause declaration text carries an inline bilateral side-qualifier annotation "
    "identifying its side role (SE-side / CS-side) and its CA-1.N verification row (CA-1.9 / CA-1.6). "
    "An output passing C-38+C-40+C-44 via declared sub-clauses and a mandate co-citation but carrying no inline side labels "
    "within the declaration text fails C-48. The structural move parallels C-44's elevation of C-38+C-40 from independent declarations "
    "to co-cited mandate-level pair -- C-48 instead pushes the bilateral label back into the definition point of each sub-clause.\n\n"
    "**C-49 vs C-45**: C-45 requires the Phase 3 execution mandate block to co-name CA-1.9 (SE-side) and CA-1.6 (CS-side) as bilateral "
    "verification obligations. C-49 requires the terminal Verdict or summary section to echo the same bilateral framing -- co-naming both "
    "CA rows with side qualifiers and adding an explicit parity-confirmation statement. C-45 operates at the mandate layer (what must be "
    "verified); C-49 operates at the verdict layer (what was verified). Neither C-45 nor C-47 requires a bilateral verdict citation; "
    "C-49 closes the bilateral propagation at the downstream outcome layer.\n\n"
    "**C-50 vs C-11 and C-44**: C-11 requires the CEM table to be present with M4 pre-assignment entries. C-44 requires the ROLE "
    "SEQUENCING MANDATE to co-name SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 as bilateral siblings. C-50 tests that the bilateral pair "
    "is also co-declared in a structured annotation block co-located with the CEM table, making the M4 bilateral structure visible from "
    "the assignment section independently of the mandate block. An output passing C-11+C-44 without a CEM-adjacent bilateral annotation "
    "block fails C-50.\n\n"
    "**C-48, C-49, C-50 are independent**: C-48 requires C-38+C-40+C-44 (both sub-clauses declared + mandate co-citation). "
    "C-49 requires C-44+C-45 (mandate bilateral + Phase 3 bilateral echo). "
    "C-50 requires C-11+C-44 (CEM table + mandate bilateral co-citation). "
    "A variation can satisfy any subset: R18-V-03 demonstrates C-48 without C-49 or C-50; R18-V-02 demonstrates C-49 without C-48 or C-50; "
    "R18-V-05 demonstrates all three simultaneously. V-06 (path to 100.0 under v18) requires all three.\n\n"
    "**C-47 and C-48 are structurally parallel at adjacent layers**: C-47 propagates the CA-1.6 bilateral pattern from the Phase 3 mandate "
    "(C-45) into the NON-OVERLAP DECLARATION statement layer. C-48 propagates the bilateral side-labeling from the mandate layer (C-44) "
    "into the SHALL sub-clause definition text layer. Both are downward propagation moves to different structural targets: C-47 targets the "
    "non-overlap declaration statements, C-48 targets the obligation definition text. They are independent -- an output can satisfy either "
    "without the other.\n"
)

v18 = v18.rstrip('\n') + '\n' + design_notes

with open('C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v18-2026-03-16.md', 'w', encoding='utf-8') as f:
    f.write(v18)

print('Done.')
print(f'v17 chars: {len(v17)}')
print(f'v18 chars: {len(v18)}')
