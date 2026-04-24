"""Build trace-permissions-rubric-v19 from v18 by adding C-51, C-52, C-53."""
import re

SRC = 'C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v18-2026-03-16.md'
DST = 'C:/src/sim/simulations/quest/rubrics/trace-permissions-rubric-v19-2026-03-16.md'

lines = open(SRC, encoding='utf-8').readlines()

# -- New header block (replaces line 0 only) --
V19_HEADER = """\
The v19 rubric is written to `simulations/quest/rubrics/trace-permissions-rubric-v19-2026-03-16.md`.

---

**Summary of changes v18 -> v19:**

**3 new aspirational criteria. Denominator: 42 -> 45. Each aspirational = 0.222 pts.**

| ID | Hangs off | Pattern | What it tests |
|----|-----------|---------|---------------|
| C-51 | C-11+C-48+C-50 | R19-V-02 | Schema Registry bilateral sub-clause pair annotation -- Step 0.1 Schema Registry entries for TABLE_4 and TABLE_5 carry inline bilateral pair annotations naming sub-clause ID, side qualifier, CA-1.N audit target, and bilateral peer, propagating C-48's bilateral sub-clause labeling into the Schema Registry layer |
| C-52 | C-38+C-40 | R19-V-03 | Preamble-anchor bilateral peer cross-citation -- CA-1.9 preamble-anchor names CA-1.6 (CS-side) as bilateral co-equal peer, and CA-1.6 preamble-anchor names CA-1.9 (SE-side) as bilateral co-equal peer, each with explicit side qualifier, propagating C-44's mandate-level bilateral co-citation into each individual preamble-anchor paragraph |
| C-53 | C-49+C-51+C-52 | R19-V-05 | Phase 3 bilateral pair verification closure block -- a named structural element positioned after CA-1.9 and before the Verdict catalogs all bilateral propagation layers by structural name, mechanism, and criterion reference, making the complete bilateral propagation chain self-documenting from within the output body |

**R19 re-scored under v19:**

| Variation | v18 | v19 | Delta |
|-----------|-----|-----|-------|
| V-01 | 100.0 (42/42) | **99.3 (42/45)** | fails C-51, C-52, C-53 |
| V-02 | 100.0 (42/42) | **99.6 (43/45)** | +C-51; fails C-52, C-53 |
| V-03 | 100.0 (42/42) | **99.6 (43/45)** | +C-52; fails C-51, C-53 |
| V-04 | 100.0 (42/42) | **99.8 (44/45)** | +C-51, +C-52; fails C-53 |
| V-05 | 100.0 (42/42) | **100.0 (45/45)** | +C-51, +C-52, +C-53 |

**Structural insight:** The bilateral propagation chain now spans nine layers: C-44 (Phase 0 obligation mandate) -> C-45 (Phase 3 verification mandate) -> C-47 (NON-OVERLAP DECLARATION statements) -> C-48 (SHALL sub-clause definition text) -> C-49 (terminal Verdict summary) -> C-50 (CEM table annotation) -> C-51 (Schema Registry Step 0.1) -> C-52 (preamble-anchor cross-citation) -> C-53 (meta-level closure block). C-51 and C-52 are structurally independent (Schema Registry vs preamble anchors); C-53 requires both as catalog inputs. V-04 already combines C-51+C-52; only C-53 remains as the single open axis from V-04.

**Path to 100.0 (45/45):** V-06 = V-04 architecture (C-51+C-52) + V-05's Phase 3 bilateral pair verification closure block (C-53). Single open axis.

---

"""

# -- Three new criterion rows --
C51 = ("| C-51 | **Schema Registry bilateral sub-clause pair annotation** -- "
       "The Step 0.1 Schema Registry block co-locates inline bilateral sub-clause pair annotations "
       "with TABLE_4 and TABLE_5 schema ID entries. Each annotation names sub-clause ID, "
       "side qualifier (SE-side / CS-side), CA-1.N audit target (CA-1.9 / CA-1.6), and bilateral "
       "peer sub-clause -- propagating C-48's bilateral sub-clause labeling into the Schema Registry layer. "
       "| format | aspirational | "
       "The Step 0.1 Schema Registry block carries bilateral annotations for TABLE_4 and TABLE_5 entries. "
       "Each annotation explicitly names: (a) the sub-clause ID (SHALL-D-EXT-C35 for TABLE_4 or "
       "SHALL-F-EXT-CS2CS3 for TABLE_5), (b) side qualifier (SE-side or CS-side), (c) CA-1.N audit target "
       "(CA-1.9 or CA-1.6), and (d) the bilateral peer sub-clause. "
       "An output passing C-48 and C-50 but without Step 0.1 Schema Registry bilateral annotations fails C-51. |\n")

C52 = ("| C-52 | **Preamble-anchor bilateral peer cross-citation** -- "
       "CA-1.6 and CA-1.9 preamble-anchor paragraphs each name the other as bilateral co-equal peer "
       "with an explicit side qualifier. CA-1.9's preamble-anchor cites CA-1.6 (CS-side) as its bilateral "
       "counterpart; CA-1.6's preamble-anchor cites CA-1.9 (SE-side) as its bilateral counterpart -- "
       "propagating the bilateral parity established by C-44's mandate-level co-citation down into each "
       "individual preamble-anchor paragraph. "
       "| format | aspirational | "
       "The CA-1.9 preamble-anchor paragraph explicitly names CA-1.6 as the CS-side bilateral co-equal peer. "
       "The CA-1.6 preamble-anchor paragraph explicitly names CA-1.9 as the SE-side bilateral co-equal peer. "
       "Each cross-citation carries an explicit side qualifier. "
       "An output passing C-38+C-40 whose preamble-anchor paragraphs each cite only their own obligation "
       "without cross-citing the other fails C-52. |\n")

C53 = ("| C-53 | **Phase 3 bilateral pair verification closure block** -- "
       "A named structural element positioned after CA-1.9 and before the Verdict section catalogs all "
       "bilateral propagation layers by structural name, mechanism, and criterion reference -- a "
       "self-documenting meta-level bilateral closure that makes the complete bilateral propagation chain "
       "verifiable from within the output body. "
       "| format | aspirational | "
       "A named block appears after the CA-1.9 verification row and before the Verdict. "
       "The block enumerates all bilateral propagation layers, each entry naming the structural element, "
       "the bilateral mechanism, and the criterion it satisfies. "
       "A minimum of eight distinct bilateral layers must be cataloged (C-44, C-45, C-47, C-48, C-49, "
       "C-50, C-51, C-52). "
       "An output passing C-49+C-51+C-52 but without this structural catalog block fails C-53. |\n")

# -- New design notes --
DESIGN_NOTES_NEW = """\

**C-51 vs C-48 and C-50**: C-48 requires each SHALL sub-clause declaration text to carry bilateral side-qualifier annotations. C-50 requires the CEM table in Step 0.2 to carry a co-located bilateral annotation block. C-51 tests the parallel move at Step 0.1: the Schema Registry entries for TABLE_4 and TABLE_5 each carry bilateral pair annotations. All three criteria propagate bilateral labeling to different structural locations (sub-clause definition text, CEM table, Schema Registry); they are independent -- an output can satisfy any subset. C-11 is a formal prerequisite (Schema Registry entries are part of the pre-printed table system).

**C-52 vs C-38 and C-40**: C-38 requires CA-1.9's preamble-anchor to cite SHALL-D-EXT-C35 as the obligation it completes. C-40 requires CA-1.6's preamble-anchor to cite SHALL-F-EXT-CS2CS3 as the obligation it completes. Neither requires the two preamble-anchors to cross-cite each other. C-52 tests exactly this cross-citation: CA-1.9's preamble-anchor also names CA-1.6 as its CS-side bilateral counterpart, and CA-1.6's preamble-anchor also names CA-1.9 as its SE-side bilateral counterpart. C-52 is the preamble-layer propagation of C-44's mandate-level bilateral co-citation -- C-44 puts both sub-clauses together in the ROLE SEQUENCING MANDATE; C-52 puts each anchor's peer reference into the anchor paragraphs themselves.

**C-53 vs C-49, C-51, and C-52**: C-49 requires the Verdict to echo the bilateral framing. C-51 and C-52 each add a new bilateral layer (Schema Registry and preamble-anchor respectively). C-53 requires a named structural element positioned before the Verdict that catalogs the complete bilateral propagation chain including C-51 and C-52's new layers. C-53 is structurally dependent on C-51+C-52 because it must enumerate at least eight layers -- the six R18 layers (C-44, C-45, C-47, C-48, C-49, C-50) plus both R19 layers (C-51, C-52). An output passing C-49 but lacking C-51 or C-52 cannot produce a complete eight-layer catalog; an output passing C-51+C-52 but without the catalog block fails C-53.

**C-51, C-52, C-53 are independent at the structural level but C-53 is catalog-dependent**: C-51 requires C-11+C-48+C-50 (Schema Registry context). C-52 requires C-38+C-40 (preamble-anchor context). C-53 requires C-49+C-51+C-52 (Verdict bilateral anchor + both new layers to enumerate). R19-V-02 demonstrates C-51 without C-52 or C-53; R19-V-03 demonstrates C-52 without C-51 or C-53; R19-V-04 demonstrates C-51+C-52 without C-53; R19-V-05 demonstrates all three simultaneously.

"""

# -- Find structural indices --
scoring_idx = next(i for i, l in enumerate(lines) if '## Scoring Formula' in l)
c50_idx     = max(i for i, l in enumerate(lines) if l.startswith('| C-50 |'))
tier_idx    = next(i for i, l in enumerate(lines) if '## Tier Totals' in l)
design_idx  = next(i for i, l in enumerate(lines) if '## Design Notes' in l)

print(f"scoring_idx={scoring_idx}  c50_idx={c50_idx}  tier_idx={tier_idx}  design_idx={design_idx}")

# -- Build output --
out = []

# 1. New v19 header (replaces line 0 = "The v18 rubric..." line)
out.append(V19_HEADER)

# 2. Prior version history: from line 2 (first '---') through scoring_idx (exclusive)
out.extend(lines[2:scoring_idx])

# 3. Scoring formula -- updated denominator and per-criterion pts
for l in lines[scoring_idx:c50_idx]:
    l = l.replace('aspirational_pass/42', 'aspirational_pass/45')
    l = l.replace('Aspirational each = 0.238 pts', 'Aspirational each = 0.222 pts')
    out.append(l)

# 4. C-01 through C-50 rows (unchanged)
out.append(lines[c50_idx])   # C-50 row

# 5. Blank line after C-50, then C-51, C-52, C-53, then blank line
out.append(C51)
out.append(C52)
out.append(C53)

# 6. Everything between C-50's trailing newline and tier totals (usually blank line + ---)
# lines[c50_idx+1] is typically the blank line, lines[c50_idx+2] is '---'
out.extend(lines[c50_idx + 1 : tier_idx])

# 7. Tier totals -- update range and count
for l in lines[tier_idx:design_idx]:
    l = l.replace('C-09 -- C-50', 'C-09 -- C-53')
    l = l.replace('42 criteria (C-09 through C-50). Each aspirational = 10/42 = 0.238 pts.',
                  '45 criteria (C-09 through C-53). Each aspirational = 10/45 = 0.222 pts.')
    out.append(l)

# 8. Design notes header + existing notes
out.extend(lines[design_idx:])

# 9. Append new design notes
out.append(DESIGN_NOTES_NEW)

# -- Write output --
with open(DST, 'w', encoding='utf-8') as f:
    f.writelines(out)

total_lines = sum(1 for _ in open(DST, encoding='utf-8'))
print(f"Written: {DST}  ({total_lines} lines)")
