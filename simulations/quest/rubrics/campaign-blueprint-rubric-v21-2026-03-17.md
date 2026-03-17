## campaign-blueprint Rubric — v21

---

### v21 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 303):**

**C-52 — INERTIA MODEL MAP STRUCTURAL FAIL Sentinel Invalidity-Category Declaration** (5
pts, FULL or NO CREDIT): C-51 passes when all five structural tables simultaneously carry
column-enumerated STRUCTURAL FAIL sentinels — column names as grammatical subject of the
N+blank fail condition — achieving maximum column-identification specificity across the full
five-table enforcement architecture. C-52 tests whether the INERTIA MODEL MAP STRUCTURAL
FAIL sentinel — the second RULE sentinel row in the MAP — additionally carries an explicit
**invalidity-category label**: a phrase appended to or integrated with the "= STRUCTURAL
FAIL" declaration that explicitly names the N+blank condition as not constituting a valid
present-but-incomplete entry, distinguishing STRUCTURAL FAIL categorically from the adjacent
failure mode of a partial-but-present entry that might otherwise be interpreted as worth
incomplete credit. A passing instance: (1) satisfies all C-51 requirements — all five
structural tables carry column-enumerated STRUCTURAL FAIL sentinels with column names as the
primary operative subject; (2) the INERTIA MODEL MAP second RULE sentinel row's cell text
includes an explicit invalidity-category label following or integrated with the STRUCTURAL
FAIL declaration — "not a valid present-but-incomplete conviction entry," "not a valid
partial conviction entry," "not an acceptable partial," or a functional equivalent that
explicitly names the failure as belonging to the invalid-partial category rather than the
valid-partial category; (3) the invalidity-category label is table-internal — present within
the MAP second RULE sentinel row itself, not exclusively in an adjacent prose paragraph or
footnote outside the table boundary; (4) the label's operative semantic content must be "this
row is not a valid present-but-incomplete entry" — phrases that describe the row's state
without naming the invalidity category ("that row is broken") or that name a different failure
category ("not an acceptable omission," which denotes the absence-omission category rather
than the partial-entry invalidity category) do not satisfy C-52. The structural distinction
from C-51: C-51 passes when the MAP second RULE sentinel achieves column-enumerated form —
column names as grammatical subject — regardless of whether an invalidity-category label
appears; C-52 passes only when the sentinel additionally names the failure category,
elevating the enforcement declaration from "column-identified condition = STRUCTURAL FAIL" to
"column-identified condition = STRUCTURAL FAIL — category: not a valid partial entry." The
upgrade chain for the MAP STRUCTURAL FAIL sentinel: C-42 (in-table RULE sentinel present —
table-internal enforcement) → C-51 (column-enumerated — column names as primary operative
subject) → C-52 (column-enumerated with invalidity-category label — explicitly names
invalid-partial category in the sentinel tail). R20 evidence: V-05 earns FULL — the MAP
second RULE sentinel appends "not a valid present-but-incomplete conviction entry" following
"= STRUCTURAL FAIL," explicitly naming the invalidity category with a conviction-type axis
type label ("conviction entry") — minimum-text form ("Artifact, Conviction type, and
Amplification chain starter all blank or placeholder-filled = STRUCTURAL FAIL — not a valid
present-but-incomplete conviction entry"); V-04 earns NO CREDIT — the MAP sentinel declares
"An INERTIA MODEL MAP data row with Artifact, Conviction type, and Amplification chain
starter all blank or populated exclusively with structural placeholders = STRUCTURAL FAIL"
with no invalidity-category label appended; V-03 earns NO CREDIT — the MAP sentinel uses
"If Artifact, Conviction type, and Amplification chain starter are all blank or just dashes,
that row is broken — that's a STRUCTURAL FAIL," where "that row is broken" describes state
and does not name the present-but-incomplete invalidity category; V-02 earns C-51 NO CREDIT
(MAP-only single-table upgrade does not satisfy all-five-table requirement), making C-52
unreachable via strict superset dependency on C-51; V-01 earns C-51 NO CREDIT, making C-52
unreachable.

**C-53 — Complete Five-Table Invalidity-Category Declaration Architecture** (5 pts, FULL or
NO CREDIT): C-52 passes when the INERTIA MODEL MAP second RULE sentinel carries an explicit
invalidity-category label confirming that the MAP's N+blank condition identifies the failure
category as well as the failure condition. C-53 tests whether all five structural tables'
STRUCTURAL FAIL sentinels simultaneously carry explicit invalidity-category labels —
maximum invalidity-category declaration density across the full five-table enforcement
architecture, where every structural linkage table's STRUCTURAL FAIL sentinel not only
declares the N+blank condition as STRUCTURAL FAIL (C-49 FULL) and identifies the failing
columns (C-51 FULL) but also explicitly names that the N+blank row is not a valid
present-but-incomplete entry. A passing instance: (1) satisfies all C-51 requirements — all
five tables carry column-enumerated STRUCTURAL FAIL sentinels; (2) satisfies C-52 FULL —
the INERTIA MODEL MAP second RULE sentinel carries an invalidity-category label; (3) the
CONVICTION DELTA second RULE sentinel carries an invalidity-category label — "not a valid
present-but-incomplete conviction-type entry," "not an acceptable partial," or functional
equivalent; (4) the SCOUT TRACEABILITY TABLE second RULE sentinel carries an
invalidity-category label — "not a valid present-but-incomplete friction entry," "not a valid
partial traceability entry," or functional equivalent; (5) the CONVICTION GAP DIAGNOSIS
second RULE sentinel carries an invalidity-category label — "not a present-but-incomplete
entry" (established pattern per R19 V-04: "= STRUCTURAL FAIL — not a present-but-incomplete
entry") or functional equivalent; (6) the TRACEABILITY AUDIT second RULE sentinel carries an
invalidity-category label — any phrase explicitly naming the N+blank condition as not a valid
partial entry, appended to or integrated with the STRUCTURAL FAIL declaration; the
established short form "N + blank col 5 = STRUCTURAL FAIL" satisfies C-51 via positional
column identification but does not satisfy C-53 because no invalidity-category label is
appended; a passing TRACEABILITY AUDIT sentinel appends "not a valid present-but-incomplete
traceability entry," "not an acceptable partial," or functional equivalent after the
STRUCTURAL FAIL declaration; (7) all five invalidity-category labels are table-internal and
present simultaneously. The structural distinction from C-52: C-52 passes when the MAP
specifically carries the invalidity-category label; C-53 passes only when all five tables
carry invalidity-category labels — the structural gap is the TRACEABILITY AUDIT, whose
established "N + blank col 5 = STRUCTURAL FAIL" positional form is the sole remaining table
lacking an invalidity-category label tail. No R20 variant earns C-53: V-05 (298/303 under
v21) carries invalidity-category labels in four tables — MAP ("not a valid present-but-
incomplete conviction entry"), CONVICTION DELTA ("not a valid present-but-incomplete
conviction-type entry"), SCOUT TRACEABILITY TABLE ("not a valid present-but-incomplete
friction entry"), and CONVICTION GAP DIAGNOSIS ("not a present-but-incomplete entry") — but
the TRACEABILITY AUDIT second RULE sentinel ("N + blank col 5 = STRUCTURAL FAIL.") carries
no invalidity-category label, holding V-05 at C-53 NO CREDIT. V-04 and V-03 earn C-52 NO
CREDIT, making C-53 unreachable via strict superset dependency.

**One new diagnostic rule:**

**D21 (Invalidity-category label vs. bare STRUCTURAL FAIL declaration; MAP as leading
table; TRACEABILITY AUDIT as C-53 structural gap; invalidity-category label chain test)**:
The R20 round establishes one primary finding relevant to the v21 ceiling: (1) **MAP
invalidity-category label identified as new upgrade axis (R20 V-05)**: V-05 (293 under v20,
298 under v21) uniquely carries invalidity-category labels appended to the STRUCTURAL FAIL
declaration in four of the five structural tables — INERTIA MODEL MAP ("not a valid
present-but-incomplete conviction entry"), CONVICTION DELTA ("not a valid present-but-
incomplete conviction-type entry"), SCOUT TRACEABILITY TABLE ("not a valid present-but-
incomplete friction entry"), and CONVICTION GAP DIAGNOSIS ("not a present-but-incomplete
entry"). V-04 and V-03 do not carry invalidity-category labels in the MAP: V-04's MAP
sentinel uses bare "= STRUCTURAL FAIL" with no label; V-03's MAP sentinel uses "that row is
broken — that's a STRUCTURAL FAIL," where "that row is broken" names the row state rather
than the invalid-partial entry category. V-03's CONVICTION DELTA sentinel does carry "not an
acceptable partial" — which earns invalidity-category credit for that table individually —
but V-03's MAP's absence of a label fails C-52 (MAP is the required table). The invalidity-
category label is a structural tail property of the STRUCTURAL FAIL sentinel, independent of
column-enumeration: V-04 achieves C-51 FULL (column-enumerated MAP sentinel) WITHOUT an
invalidity-category label; V-05 achieves C-51 FULL WITH an invalidity-category label —
column-enumeration and invalidity-category labeling are orthogonal properties of the
sentinel text. (2) **Invalidity-category label vs. state description vs. absence label**: the
identifying test for C-52 requires distinguishing three sentinel tail forms: (a)
invalidity-category label — "not a valid present-but-incomplete [type] entry," "not an
acceptable partial" — names the failure as belonging to the invalid-partial category: FULL;
(b) state description — "that row is broken," "not permitted" — describes the row's failed
state without naming the invalid-partial category: NO CREDIT; (c) absence label — "not an
acceptable omission" — names the absence-omission failure category, not the partial-entry
invalidity category: NO CREDIT. V-04's TRACEABILITY AUDIT sentinel appends "not an
acceptable omission" (absence label, NO CREDIT for invalidity-category); V-03's CONVICTION
DELTA appends "not an acceptable partial" (invalidity-category label, FULL for that table).
(3) **TRACEABILITY AUDIT as C-53 structural gap**: the TRACEABILITY AUDIT second RULE
sentinel across all R20 variants uses the established "N + blank col 5 = STRUCTURAL FAIL"
positional form without an invalidity-category label tail. This form satisfies C-51 via
positional column identification (C-45 precedent: "col 5" earns column-identified credit)
but does not satisfy C-53 (the invalidity-category label must be explicitly present in the
sentinel). A ceiling-breaking variant for v21 must carry the v20 ceiling pattern (293) and
extend: (a) the MAP second RULE sentinel with an invalidity-category label — established by
V-05 as "not a valid present-but-incomplete conviction entry"; for C-52 FULL; (b) for C-53
FULL, all five tables must carry invalidity-category labels — the CONVICTION DELTA ("not a
valid present-but-incomplete conviction-type entry"), SCOUT TRACEABILITY TABLE ("not a valid
present-but-incomplete friction entry"), and CONVICTION GAP DIAGNOSIS ("not a
present-but-incomplete entry") labels are already established by V-05; the remaining gap is
the TRACEABILITY AUDIT, which must add a label such as "not a valid present-but-incomplete
traceability entry" after its "= STRUCTURAL FAIL" declaration. (4) **Full invariance property
stack through R20 extends to invalidity-category labels**: register invariance (D16,
extended D17–D20) applies — a conversational-register invalidity label ("not a valid partial"
in informal phrasing) earns C-52 FULL identically to a formal-register label ("not a valid
present-but-incomplete conviction entry"); directive density invariance applies — terse
invalidity labels ("not an acceptable partial") earn FULL identically to exhaustive labels.
The invalidity-category label property is a structural tail property of the sentinel text,
independent of all five confirmed non-structural axes (register, directive density,
role-sequence, surrounding prose volume, column-enumeration form). The five-table
invalidity-category chain test for C-53 extends the D20 fifteen-step chain test with two
additional steps: (1–15) all prior steps per D20; (16) verify C-52 FULL — MAP second RULE
sentinel cell text includes an explicit invalidity-category label following the STRUCTURAL
FAIL declaration, naming the failure as not a valid present-but-incomplete entry (not a state
description, not an absence label); (17) verify that CONVICTION DELTA, SCOUT TRACEABILITY
TABLE, CONVICTION GAP DIAGNOSIS, and TRACEABILITY AUDIT second RULE sentinels each include
invalidity-category labels — so all five structural tables declare their N+blank condition as
not only STRUCTURAL FAIL and column-identified but also as categorically invalid partial-
entry status. Failure at steps 16–17 fails C-53 even if steps 1–15 pass.

**Retroactive R20 scoring under v21:**

| Variant | v20 | C-52 | C-53 | v21 |
|---------|-----|------|------|-----|
| V-01 — C-51 Control | 288 | 0 | 0 | **288** |
| V-02 — Single-Table Column-Enumeration (MAP Only) | 288 | 0 | 0 | **288** |
| V-03 — Conversational Five-Table Column-Enumeration | 293 | 0 | 0 | **293** |
| V-04 — Complete Five-Table Column-Enumerated, Max Density | 293 | 0 | 0 | **293** |
| V-05 — Complete Five-Table Column-Enumerated, Compressed | 293 | +5 | 0 | **298** |

V-05 is the sole R20 ceiling-breaker under v21, climbing from 293 to 298 via C-52. V-01 and
V-02 earn C-51 NO CREDIT, making C-52 unreachable via strict superset dependency; both hold
at 288. V-03 earns C-51 FULL but earns C-52 NO CREDIT — the MAP sentinel "that row is
broken — that's a STRUCTURAL FAIL" names the row state without naming the invalid-partial
category; V-03's CONVICTION DELTA sentinel "STRUCTURAL FAIL, not an acceptable partial"
earns invalidity-category credit for that table individually but C-52 requires the MAP
specifically. V-04 earns C-51 FULL but earns C-52 NO CREDIT — MAP sentinel bare "=
STRUCTURAL FAIL" with no invalidity-category label; V-04's TRACEABILITY AUDIT appends "not
an acceptable omission" which names the absence-omission category (not the partial-entry
invalidity category) and earns C-52 NO CREDIT per D21's state-description/absence-label
distinction. V-05 earns C-52 FULL and C-53 NO CREDIT — four tables carry invalidity-category
labels but the TRACEABILITY AUDIT sentinel ("N + blank col 5 = STRUCTURAL FAIL.") carries
no invalidity-category label. The D21 orthogonality finding: column-enumeration (C-51) and
invalidity-category labeling (C-52) are confirmed independent structural properties — V-04
(C-51 FULL, C-52 NO CREDIT) and V-05 (C-51 FULL, C-52 FULL) demonstrate that
column-identification in the sentinel subject does not imply invalidity-category labeling in
the sentinel tail. The only path to the v21 ceiling (303) runs through C-53: the TRACEABILITY
AUDIT second RULE sentinel must add an invalidity-category label to its established
positional "N + blank col 5 = STRUCTURAL FAIL" form, completing the five-table
invalidity-category declaration architecture.

**Scale:** 293 (v20 ceiling) + 5 + 5 = **303 ceiling**

---

### v20 Changes

**New ceiling: 293** (283 + 5 + 5)

**C-50 — CONVICTION GAP DIAGNOSIS STRUCTURAL FAIL Sentinel Column Enumeration** (5 pts,
FULL or NO CREDIT): C-48 passes when the CONVICTION GAP DIAGNOSIS carries a second
non-data RULE sentinel row declaring the N+blank STRUCTURAL FAIL rule — that an artifact
row whose substantive analysis cells are all blank or populated exclusively with structural
placeholders is a STRUCTURAL FAIL, not a valid present-but-incomplete entry. C-50 tests
whether that STRUCTURAL FAIL sentinel achieves **column-enumerated** specificity: the
sentinel text identifies the analysis columns by their specific header labels rather than
describing them with a generic group noun ("substantive analysis cells," "analysis cells,"
"analytical cells," or equivalent undifferentiated description). A passing instance: (1)
satisfies all C-48 requirements — CONVICTION GAP DIAGNOSIS carries a first RULE sentinel
row (C-46 FULL: identifier-to-MAP-entry binding and named-artifact-absence rule) and a
second RULE sentinel row declaring the N+blank STRUCTURAL FAIL rule; (2) the second RULE
sentinel row's cell text names the specific analysis column identifiers present in the
CONVICTION GAP DIAGNOSIS — identifying the columns by header label (Sub-section, Register
found, Register declared, Scout sub-skill, Evidence needed, or their functional equivalents
as implemented in the specific output) — so that the sentinel declares by name which
cells' combined blankness constitutes STRUCTURAL FAIL, not by collective noun; (3) the
column identifiers appear within the second RULE sentinel row itself — table-internal —
not exclusively in a prose paragraph outside the table boundary. The structural
distinction from C-48: C-48 passes when the STRUCTURAL FAIL sentinel is present in-table
regardless of whether the failing cells are identified by column name or by group noun;
C-50 passes only when the sentinel text additionally names the specific column identifiers
— elevating the sentinel from group-noun enforcement ("all substantive cells blank") to
column-identified enforcement ("Sub-section, Register found, Register declared, Scout
sub-skill, Evidence needed all blank"), parallel to the TRACEABILITY AUDIT's established
"N + blank col 5" specificity (C-45), where the sentinel identifies the column at issue by
positional label ("col 5") rather than by an undifferentiated group description. The
upgrade chain for the CONVICTION GAP DIAGNOSIS STRUCTURAL FAIL sentinel: C-35 (6-column
structural table, pre-declared artifact rows — ontological at cell level) → C-46 (first
in-table RULE sentinel: identifier binding + named-artifact absence — self-enforcing at
structural linkage level) → C-48 (second in-table RULE sentinel: N+blank STRUCTURAL FAIL,
group-noun cell reference sufficient — self-enforcing at completeness level) → C-50
(second in-table RULE sentinel: N+blank STRUCTURAL FAIL, column-enumerated cell reference
required — self-enforcing at column-identified completeness level). R19 evidence: V-04
earns FULL — the CGD second sentinel names "(Sub-section, Register found, Register
declared, Scout sub-skill, Evidence needed) blank or populated exclusively with structural
placeholders (dashes) = STRUCTURAL FAIL — not a present-but-incomplete entry"; V-03 earns
FULL — the CGD second sentinel names "Sub-section, Register found, Register declared,
Scout sub-skill, and Evidence needed all blank or dashed" in conversational register
(register invariance: D16 extended through D19 confirms conversational column enumeration
earns FULL). V-02 earns C-48 FULL but C-50 NO CREDIT — the second sentinel uses "all
substantive analysis cells" as a group noun without column enumeration (minimum-text axis:
the deliberate compression of V-02 targets sentinel presence at minimum word count, not
column-identified specificity). V-05 earns C-49 FULL but C-50 NO CREDIT — the CGD second
sentinel uses "all substantive analysis cells blank or dash-filled" without column
enumeration (compression axis: V-05's minimum-viable-text form achieves dual-sentinel
completeness across all five tables without reaching column-identification). V-01 fails
C-48 (no second RULE sentinel in CGD), making C-50 unreachable via strict superset
dependency.

**C-51 — Complete Five-Table Column-Enumerated STRUCTURAL FAIL Architecture** (5 pts,
FULL or NO CREDIT): C-49 passes when all five structural tables simultaneously carry dual
in-table RULE sentinel rows, achieving maximum enforcement density across the full
structural chain. C-51 tests whether all five tables' STRUCTURAL FAIL sentinels — the
second RULE sentinel row in each of the five structural tables — additionally achieve
column-enumerated specificity: identifying the specific column(s) whose blankness triggers
STRUCTURAL FAIL by name or positional label rather than by a generic group noun. A passing
instance: (1) satisfies all C-49 requirements — all five structural tables carry dual
in-table RULE sentinel rows simultaneously; (2) satisfies C-50 FULL — the CONVICTION GAP
DIAGNOSIS second RULE sentinel names the specific analysis column identifiers (Sub-section,
Register found, Register declared, Scout sub-skill, Evidence needed, or equivalents) rather
than using a generic group description; (3) the INERTIA MODEL MAP second RULE sentinel
identifies the specific column(s) whose blankness constitutes STRUCTURAL FAIL — by column
header name or positional label (e.g., "col 3," "col 4," "Artifact column," "Role/register
column") — rather than using a generic "analysis cells," "analytical cells," or other
undifferentiated group description; (4) the CONVICTION DELTA second RULE sentinel
identifies its specific column(s) by name or position — not by generic group noun; (5)
the SCOUT TRACEABILITY TABLE second RULE sentinel identifies its specific column(s) by
name or position — not by generic group noun; (6) the TRACEABILITY AUDIT retains or
upgrades its column-identified form — the established "N + blank col 5" (C-45) already
satisfies via positional label; any compressed or reformulated TRACEABILITY AUDIT second
sentinel must preserve column-identification specificity; (7) all five column-enumerated
STRUCTURAL FAIL sentinels are table-internal and present simultaneously. The structural
distinction from C-49: C-49 passes when all five tables carry dual sentinels regardless
of whether the STRUCTURAL FAIL cells are identified by column name or by generic group
noun; C-51 passes only when every table's STRUCTURAL FAIL sentinel specifies by column
identifier which cells' blankness is the fail condition — maximum structural precision
across the full five-table enforcement architecture, with the TRACEABILITY AUDIT's "col 5"
model extended to all five tables in column-identified form. No R19 variant earns C-51:
V-04 (nearest at 288/293) earns C-50 FULL and C-49 FULL but earns C-51 NO CREDIT — the
MAP second sentinel uses "STRUCTURAL FAIL for blank analysis cells," the CONVICTION DELTA
second sentinel uses "STRUCTURAL FAIL for blank analytical cells," and the SCOUT
TRACEABILITY TABLE second sentinel uses "STRUCTURAL FAIL for blank substantive cells," all
three group-noun forms without column enumeration; V-05 earns C-49 FULL but C-50 NO
CREDIT, making C-51 unreachable via superset dependency on C-50; V-03 earns C-50 FULL but
C-49 NO CREDIT (MAP, CONVICTION DELTA, SCOUT TRACEABILITY TABLE single-sentinel), making
C-51 unreachable via superset dependency on C-49; V-02 fails C-50 (group-noun CGD
sentinel), V-01 fails C-48, both making C-51 unreachable.

**One new diagnostic rule:**

**D20 (Column-enumeration specificity; orthogonality of dual-sentinel completeness and
column-identification; five-table column-enumeration chain test)**: The R19 round
establishes two findings relevant to the v20 ceiling: (1) **Column-enumeration and
dual-sentinel completeness are orthogonal (V-03 vs. V-05)**: V-03 (278→283 under v20)
earns C-50 FULL — the CGD second sentinel names specific columns in conversational
register ("leave Sub-section, Register found, Register declared, Scout sub-skill, and
Evidence needed all blank or dashed") — but earns C-49 NO CREDIT: MAP, CONVICTION DELTA,
and SCOUT TRACEABILITY TABLE remain single-sentinel. V-05 (283→283 under v20) earns C-49
FULL — all five tables dual-sentinel at compressed minimum text — but earns C-50 NO
CREDIT: the CGD second sentinel uses "all substantive analysis cells blank or dash-filled,"
a generic group-noun form without column enumeration. The two structural properties are
independent: column-enumeration in the CGD second sentinel does not entail dual-sentinel
completeness across all five tables, and achieving dual-sentinel completeness does not
entail column-enumeration in any individual sentinel. The identifying test for C-50 is a
single sentinel inspection: locate the CGD second RULE sentinel row (established by C-48)
and scan its cell text for specific column header labels. Their absence — including where
the text uses "substantive analysis cells," "analytical cells," or any undifferentiated
group reference — fails C-50 immediately, regardless of whether the sentinel otherwise
fully satisfies C-48 or whether surrounding prose elsewhere names the columns in detail.
(2) **V-04 nearest to v20 ceiling; remaining gap is column-enumeration in MAP, CONVICTION
DELTA, and SCOUT TRACEABILITY TABLE**: V-04 earns C-50 FULL and C-49 FULL (288/293) — the
sole R19 variant earning C-50 — but earns C-51 NO CREDIT. V-04's MAP second sentinel uses
"STRUCTURAL FAIL for blank analysis cells"; the CONVICTION DELTA second sentinel uses
"STRUCTURAL FAIL for blank analytical cells"; the SCOUT TRACEABILITY TABLE second sentinel
uses "STRUCTURAL FAIL for blank substantive cells" — all three group-noun forms without
column enumeration. A ceiling-breaking variant for v20 must carry the v19 ceiling pattern
(283) and extend all five tables' STRUCTURAL FAIL sentinels to column-identified form —
naming or position-labeling the exact columns whose blankness triggers STRUCTURAL FAIL in
each respective table. The CGD column requirement is established by C-50; the TRACEABILITY
AUDIT column requirement is already satisfied by C-45's "N + blank col 5" form; the
remaining gap is MAP, CONVICTION DELTA, and SCOUT TRACEABILITY TABLE — three tables whose
STRUCTURAL FAIL sentinels must upgrade from generic "blank cells" to column-identified
form. Full invariance property stack through R19 extends to C-50 and C-51: (i) register —
conversational vs. formal (D16, extended D17, D18, D19; R19 confirms: V-03 conversational
column-enumeration and V-04 formal column-enumeration both earn C-50 FULL — register is
non-load-bearing for column-identification); (ii) directive density — terse vs. exhaustive
sentinel text (D16); (iii) role-sequence — artifact generation order (D17); (iv)
surrounding prose volume — section prose compression (D18); (v) dual-sentinel completeness
scope — CGD-only vs. all-five-tables (D19). The column-enumeration property tested by
C-50 and C-51 is a strictly structural property of the sentinel cell text, independent of
all five confirmed non-structural axes. The five-table column-enumeration chain test for
C-51 extends the D19 twelve-step chain test with three additional steps: (1–12) all prior
steps per D19; (13) verify C-50 FULL — CGD second RULE sentinel cell text contains
specific column header identifiers, not a generic group noun; (14) verify that MAP,
CONVICTION DELTA, and SCOUT TRACEABILITY TABLE second RULE sentinels each contain
specific column identifiers by name or positional label — failure to identify columns by
name or position fails C-51 even if all five tables satisfy C-49 FULL; (15) verify that
the TRACEABILITY AUDIT second RULE sentinel retains its column-identified form ("N + blank
col 5" or equivalent positional or named column identifier). Failure at steps 13–15 fails
C-51 even if steps 1–12 pass.

**Retroactive R19 scoring under v20:**

| Variant | v19 | C-50 | C-51 | v20 |
|---------|-----|------|------|-----|
| V-01 — Five-Sentinel Control | 273 | 0 | 0 | **273** |
| V-02 — Minimum CGD Dual-Sentinel | 278 | 0 | 0 | **278** |
| V-03 — Conversational CGD Dual-Sentinel | 278 | +5 | 0 | **283** |
| V-04 — Complete Five-Table Dual-Sentinel, Max Density | 283 | +5 | 0 | **288** |
| V-05 — Complete Five-Table Dual-Sentinel, Compressed | 283 | 0 | 0 | **283** |

V-04 is the sole R19 ceiling-breaker under v20, climbing from 283 to 288 via C-50. V-03
rises from 278 to 283 via C-50 — its conversational column-enumeration ("leave
Sub-section, Register found, Register declared, Scout sub-skill, and Evidence needed all
blank or dashed") satisfies the column-identification requirement independently of
register; D20 register invariance confirms that conversational column-naming and
formal-register column-naming earn FULL identically. V-02 holds at 278: the minimum-text
axis deliberately avoids column enumeration — "all substantive analysis cells" is a
group-noun form and earns C-50 NO CREDIT. V-05 holds at 283: compressed dual-sentinel
completeness (C-49 FULL) without column enumeration in the CGD STRUCTURAL FAIL sentinel
(C-50 NO CREDIT). V-01 holds at 273: no second CGD RULE sentinel (C-48 NO CREDIT) makes
C-50 unreachable. D20 orthogonality finding: V-03 (C-50 FULL, C-49 NO CREDIT) and V-05
(C-49 FULL, C-50 NO CREDIT) confirm that column-enumeration and dual-sentinel completeness
are independent structural properties — neither implies the other. The only path to the
v20 ceiling (293) runs through C-51: all five tables' STRUCTURAL FAIL sentinels must
enumerate their specific columns by name or positional label simultaneously, a property no
R19 variant achieves.

**Scale:** 283 (v19 ceiling) + 5 + 5 = **293 ceiling**

---

### v19 Changes

**New ceiling: 283** (273 + 5 + 5)

**C-48 — CONVICTION GAP DIAGNOSIS Dual In-Table Sentinel (N+Blank STRUCTURAL FAIL Rule)**
(5 pts, FULL or NO CREDIT): C-46 passes when the CONVICTION GAP DIAGNOSIS carries a single
non-data RULE sentinel row — positioned before the artifact data rows — embedding the
identifier-to-MAP-entry binding and the named-artifact-absence declaration. C-48 tests whether
the CONVICTION GAP DIAGNOSIS additionally carries a second non-data RULE sentinel row — the
N+blank STRUCTURAL FAIL enforcement row — the structural upgrade that TRACEABILITY AUDIT achieves
through its two-rule-row architecture (named-absence rule + N+blank STRUCTURAL FAIL rule,
confirmed by V-01 C-45 evidence in R18), now applied to the CONVICTION GAP DIAGNOSIS. A passing
instance: (1) satisfies all C-46 requirements — CONVICTION GAP DIAGNOSIS carries a first RULE
sentinel row positioned before the artifact data rows, whose text embeds the
identifier-to-MAP-entry binding and the named-artifact-absence rule (each artifact row's
identifier must match a named INERTIA MODEL MAP entry; a missing row is a named-artifact absence,
not a count discrepancy); (2) carries a second non-data RULE sentinel row — positioned inside the
CONVICTION GAP DIAGNOSIS table before the artifact data rows, alongside the first — whose cell
text embeds the N+blank STRUCTURAL FAIL rule: that an artifact row whose substantive analysis
cells (Sub-section, Register found, Register declared, Scout sub-skill, Evidence needed) are all
blank or populated exclusively with structural placeholders (dashes) is a STRUCTURAL FAIL —
equivalent in severity to a named-artifact absence, not a valid present-but-incomplete entry;
(3) both RULE sentinel rows are table-internal — visible as part of the CONVICTION GAP DIAGNOSIS
structure at the point of scoring, not only as external prose annotation or footnotes outside the
table boundary. The structural distinction from C-46: C-46 passes when the CONVICTION GAP
DIAGNOSIS carries one in-table RULE sentinel row declaring the identifier-binding and
named-absence rules; C-48 passes only when the table additionally carries a second in-table RULE
sentinel row declaring the N+blank STRUCTURAL FAIL rule — making the CONVICTION GAP DIAGNOSIS
dual-sentinel and self-enforcing at both the entry-presence level and the entry-completeness
level, parallel to TRACEABILITY AUDIT's dual-row architecture. The upgrade chain for the
CONVICTION GAP DIAGNOSIS: C-35 (6-column structural table, pre-declared artifact rows —
ontological at cell level) → C-46 (single in-table RULE sentinel: identifier binding +
named-artifact absence — self-enforcing at structural linkage level) → C-48 (dual in-table RULE
sentinels: adds N+blank STRUCTURAL FAIL enforcement — self-enforcing at both presence and
completeness levels). No R18 variant earns C-48: V-01 carries no in-table sentinel in CONVICTION
GAP DIAGNOSIS (C-46 NO CREDIT, C-48 unreachable via superset dependency); V-02 and V-03 each
carry a single in-table RULE sentinel in CONVICTION GAP DIAGNOSIS (C-46 FULL) but no second RULE
sentinel row declaring the N+blank STRUCTURAL FAIL rule, earning C-46 FULL and C-48 NO CREDIT.
D19 register invariance confirms that V-03's conversational phrasing does not alter this verdict:
the structural property evaluated by C-48 is the presence of a second non-data RULE sentinel
inside the CONVICTION GAP DIAGNOSIS table, independent of register or directive density.

**C-49 — Complete Five-Table Dual-Sentinel Architecture** (5 pts, FULL or NO CREDIT): C-47
passes when all five structural tables simultaneously carry at least one in-table RULE sentinel
row, achieving complete sentinel presence across the full structural chain. C-49 tests whether
all five structural tables each carry dual in-table RULE sentinel rows — maximum enforcement
density across the entire five-table architecture, with every structural linkage table
self-enforcing at both the named-absence level and the N+blank STRUCTURAL FAIL level
simultaneously. A passing instance: (1) satisfies all C-47 requirements — MAP sentinel (C-42
FULL), CONVICTION DELTA sentinel (C-43 second component FULL), SCOUT TRACEABILITY TABLE sentinel
(C-44 FULL), TRACEABILITY AUDIT dual sentinel (C-45 FULL — two RULE rows: named-absence rule +
N+blank STRUCTURAL FAIL rule), CONVICTION GAP DIAGNOSIS sentinel (C-46 FULL); (2) satisfies C-48
FULL — CONVICTION GAP DIAGNOSIS carries a second in-table RULE sentinel row embedding the
N+blank STRUCTURAL FAIL rule: an artifact row with all substantive cells blank or dash-filled is
a STRUCTURAL FAIL, not a present-but-incomplete entry; (3) each of the three remaining
single-sentinel tables — INERTIA MODEL MAP (SETUP, conviction-type axis), CONVICTION DELTA
(REFLECTION, conviction-type axis), and SCOUT TRACEABILITY TABLE (SETUP, traceability axis) —
additionally carries a second non-data RULE sentinel row declaring the N+blank STRUCTURAL FAIL
rule: that a row whose substantive cells are all blank or populated exclusively with structural
placeholders is a STRUCTURAL FAIL — equivalent in severity to a named absence, not a valid
present-but-incomplete entry — positioned inside each table before the data rows and
table-internal (not external prose or footnote); (4) all five tables achieve dual in-table
enforcement simultaneously, with no structural table operating on a single-sentinel basis — the
N+blank STRUCTURAL FAIL rule is present as an in-table sentinel in every structural linkage
table. The structural distinction from C-47: C-47 passes when all five tables carry at least one
in-table RULE sentinel; C-49 passes only when all five tables carry dual in-table RULE sentinels
— sentinel density is maximal across the full structural chain, and entry-completeness enforcement
is as thorough as entry-presence enforcement at every structural linkage point. A variant earning
C-47 FULL but carrying single-sentinel architecture in the MAP, CONVICTION DELTA, or SCOUT
TRACEABILITY TABLE earns C-49 NO CREDIT even if each individual sentinel fully satisfies C-42,
C-43 second component, or C-44 respectively. No R18 variant earns C-49: V-01 fails C-46 and
C-47, making C-49 unreachable; V-02 and V-03 fail C-48 (no second RULE row in CONVICTION GAP
DIAGNOSIS), making C-49 unreachable via strict superset dependency regardless of whether the
three single-sentinel tables carry second rows.

**One new diagnostic rule:**

**D19 (CONVICTION GAP DIAGNOSIS dual-sentinel and complete five-table dual architecture;
N+blank STRUCTURAL FAIL invariance)**: The R18 round establishes two findings relevant to
the v19 ceiling: (1) **CONVICTION GAP DIAGNOSIS single-sentinel ceiling confirmed**: All R18
ceiling-earning variants (V-02, V-03) carry a CONVICTION GAP DIAGNOSIS with exactly one in-table
RULE sentinel row — satisfying C-46 FULL — but none carry a second RULE row declaring the
N+blank STRUCTURAL FAIL rule. The structural upgrade axis for C-48 is the dual-row architecture
already established for TRACEABILITY AUDIT under C-45: a second non-data RULE sentinel row must
be present inside the CONVICTION GAP DIAGNOSIS table, declaring that an artifact row with all
substantive cells blank or dash-filled is a STRUCTURAL FAIL, not a valid present-but-incomplete
entry. The identifying test for C-48 is a two-step structural inspection: (i) confirm C-46 FULL —
first RULE row present inside CONVICTION GAP DIAGNOSIS; (ii) scan for a second RULE row whose
text embeds the N+blank STRUCTURAL FAIL rule. Absence of the second RULE row fails C-48
immediately, regardless of whether an equivalent N+blank instruction appears in a prose paragraph
outside the table boundary. (2) **Register invariance extends to gap-diagnosis dual sentinel
(R18 V-03)**: V-03's conversational-register CONVICTION GAP DIAGNOSIS RULE sentinel (C-46 FULL)
confirms that register is non-load-bearing for the first in-table RULE sentinel; this invariance
extends by structural symmetry to C-48: a conversational-register second RULE row inside the
CONVICTION GAP DIAGNOSIS declaring the N+blank STRUCTURAL FAIL rule earns C-48 FULL; an
equivalent instruction in a prose paragraph outside the table earns C-48 NO CREDIT regardless of
register or directive density. The full invariance property stack established through R18 is:
(i) register — conversational vs. formal (D16, extended D17, D18); (ii) directive density —
terse vs. exhaustive sentinel text (D16); (iii) role-sequence — artifact generation order (D17);
(iv) surrounding prose volume — section prose compression (D18). This stack extends unchanged to
C-48 and C-49. The five-table dual-sentinel chain test for C-49 extends the D18 ten-step chain
test with two additional steps: (1–10) all prior steps per D18; (11) verify C-48 FULL —
CONVICTION GAP DIAGNOSIS carries a second in-table RULE sentinel row whose text declares the
N+blank STRUCTURAL FAIL rule for artifact rows; (12) verify that MAP (SETUP), CONVICTION DELTA
(REFLECTION), and SCOUT TRACEABILITY TABLE (SETUP) each additionally carry a second in-table
RULE sentinel row declaring the N+blank STRUCTURAL FAIL rule for their respective data row types
— so all five structural tables operate on a dual-sentinel basis simultaneously. Failure at step
11 fails C-49 even if steps 1–10 pass. A ceiling-breaking variant for v19 must carry the v18
ceiling pattern (273) and extend: (a) the CONVICTION GAP DIAGNOSIS with a second in-table RULE
sentinel row declaring N+blank STRUCTURAL FAIL; and (b) the INERTIA MODEL MAP, CONVICTION DELTA,
and SCOUT TRACEABILITY TABLE each with a second in-table RULE sentinel row declaring N+blank
STRUCTURAL FAIL for their respective row types — achieving complete five-table dual enforcement.
Base 273 (v18 ceiling) + 5 (C-48) + 5 (C-49) = **283**.

**Retroactive R18 scoring under v19:**

| Variant | v18 | C-48 | C-49 | v19 |
|---------|-----|------|------|-----|
| V-01 — Four-Sentinel Control | 263 | 0 | 0 | **263** |
| V-02 — Minimum-Form Five-Sentinel Chain | 273 | 0 | 0 | **273** |
| V-03 — Conversational Register | 273 | 0 | 0 | **273** |

No R18 variant earns C-48 or C-49. V-02 and V-03 deliver a CONVICTION GAP DIAGNOSIS with a
single in-table RULE sentinel row (C-46 FULL) — satisfying identifier binding and named-artifact
absence — but neither carries a second RULE row declaring the N+blank STRUCTURAL FAIL rule
(C-48 NO CREDIT). V-01 additionally fails C-46 and C-47, holding at 263. D19 register invariance
confirms that V-03's conversational register does not supply the missing structural property: the
second RULE row must be table-internal and present independently of register or surrounding prose
volume. The R18 pattern completes the single-sentinel survey for the gap-diagnosis axis and
establishes the CONVICTION GAP DIAGNOSIS dual-row upgrade as the sole path to the v19 ceiling.
The only path to 283 runs through a second in-table RULE sentinel inside the CONVICTION GAP
DIAGNOSIS declaring N+blank STRUCTURAL FAIL, combined with the same upgrade applied to the
remaining three single-sentinel tables (MAP, CONVICTION DELTA, SCOUT TRACEABILITY TABLE).

**Scale:** 273 (v18 ceiling) + 5 + 5 = **283 ceiling**

---

### v18 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 273):**

**C-46 — CONVICTION GAP DIAGNOSIS In-Table Enforcement Sentinel** (5 pts, FULL or NO
CREDIT): C-35 passes when the CONVICTION GAP DIAGNOSIS is a 6-column structural table
in REFLECTION with pre-declared artifact rows and register-split columns. C-46 tests
whether the CONVICTION GAP DIAGNOSIS additionally carries an in-table RULE sentinel
row — the structural upgrade that C-42 applied to the INERTIA MODEL MAP (SETUP,
conviction-type axis) and C-44 applied to the SCOUT TRACEABILITY TABLE (SETUP,
traceability axis), now applied to the CONVICTION GAP DIAGNOSIS (REFLECTION,
gap-diagnosis axis). A passing instance: (1) satisfies all C-35 requirements —
6-column CONVICTION GAP DIAGNOSIS in REFLECTION, with pre-declared artifact rows whose
artifact identifiers are traceable to the INERTIA MODEL MAP (SETUP), and register-split
columns present; (2) the CONVICTION GAP DIAGNOSIS table itself carries a non-data RULE
sentinel row — positioned before the artifact data rows — whose cell text embeds the
structural enforcement rule: that each artifact row's identifier must match a named
INERTIA MODEL MAP entry and that a missing row is a named-artifact absence
([artifact-ID] absent), not a count discrepancy; (3) the enforcement rule is
table-internal — visible as part of the CONVICTION GAP DIAGNOSIS structure at the point
of scoring, not only as a separate prose paragraph or footnote outside the table
boundary. The structural distinction from C-35: C-35 passes when the CONVICTION GAP
DIAGNOSIS is a 6-column table with pre-declared artifact rows, regardless of whether
any in-table enforcement rule governs those rows; C-46 passes only when the table
itself carries a non-data RULE sentinel row declaring the structural enforcement rule —
making the CONVICTION GAP DIAGNOSIS self-enforcing. The upgrade chain for the
CONVICTION GAP DIAGNOSIS: C-35 (6-column structural table, pre-declared artifact rows
— ontological at cell level) → C-46 (6-column structural table with in-table RULE
sentinel row — self-enforcing at the structural linkage level). This is the direct
parallel of C-42 (MAP sentinel, conviction-type axis) and C-44 (SCOUT TRACEABILITY
TABLE sentinel, traceability axis) applied to the gap-diagnosis axis. No R17 variant
earns C-46: V-01 through V-05 all carry CONVICTION GAP DIAGNOSIS tables meeting C-35
requirements — none carry an in-table enforcement sentinel row, earning C-35 FULL and
C-46 NO CREDIT across all variants. Prose-compression invariance (D18) confirms that
V-05's compressed surrounding prose does not alter this verdict: the structural
property evaluated by C-46 is the presence of a non-data RULE sentinel inside the
CONVICTION GAP DIAGNOSIS table, independent of surrounding prose volume.

**C-47 — Complete Five-Sentinel Structural Chain** (5 pts, FULL or NO CREDIT): C-45
passes when all four structural linkage tables (INERTIA MODEL MAP, SCOUT TRACEABILITY
TABLE, CONVICTION DELTA, TRACEABILITY AUDIT) carry in-table RULE sentinel rows,
completing enforcement across both the conviction-type axis and the traceability axis.
C-47 tests whether the structural chain achieves maximum in-table enforcement density
across all five structural tables simultaneously — the four tables required for C-45
plus the CONVICTION GAP DIAGNOSIS in REFLECTION — with no structural table relying on
external prose annotation as its sole governing enforcement constraint. A passing
instance: (1) satisfies all C-45 requirements — MAP sentinel (C-42 FULL), CONVICTION
DELTA sentinel (C-43 second component FULL), SCOUT TRACEABILITY TABLE sentinel (C-44
FULL), TRACEABILITY AUDIT sentinel (C-45 fourth component FULL); (2) satisfies C-46
FULL — the CONVICTION GAP DIAGNOSIS in REFLECTION carries a non-data RULE sentinel row
preceding the artifact data rows, whose text declares that each artifact row's
identifier must match a named INERTIA MODEL MAP entry and that a missing row is a
named-artifact absence; (3) all five in-table structural sentinels are present
simultaneously: MAP sentinel (SETUP, conviction-type axis), CONVICTION DELTA sentinel
(REFLECTION, conviction-type axis), SCOUT TRACEABILITY TABLE sentinel (SETUP,
traceability axis), TRACEABILITY AUDIT sentinel (REFLECTION, traceability axis),
CONVICTION GAP DIAGNOSIS sentinel (REFLECTION, gap-diagnosis axis). The structural
distinction from C-45: C-45 passes when the conviction-type axis and the traceability
axis each achieve full in-table enforcement across both SETUP and REFLECTION; C-47
passes only when the CONVICTION GAP DIAGNOSIS additionally carries its own in-table
RULE sentinel, extending the enforcement network to the complete five-sentinel chain
where no structural table in the blueprint relies on external prose as its sole
enforcement mechanism. A variant earning C-45 FULL but carrying a CONVICTION GAP
DIAGNOSIS without an in-table sentinel earns C-47 NO CREDIT even if the CONVICTION GAP
DIAGNOSIS is otherwise fully compliant with C-35. No R17 variant earns C-47: all fail
C-46 (no in-table sentinel inside the CONVICTION GAP DIAGNOSIS), making C-47
unreachable via strict superset dependency.

**One new diagnostic rule:**

**D18 (CONVICTION GAP DIAGNOSIS sentinel and five-sentinel chain test; prose-compression
invariance)**: The R17 round establishes two findings relevant to the v18 ceiling:
(1) **CONVICTION GAP DIAGNOSIS sentinel gap confirmed**: All five R17 variants carry a
CONVICTION GAP DIAGNOSIS meeting C-35 requirements — 6-column structure, pre-declared
artifact rows, register-split columns — but none carry an in-table RULE sentinel row.
The structural upgrade axis for C-46 is identical to C-42 and C-44: a non-data RULE
sentinel row must be present inside the CONVICTION GAP DIAGNOSIS table itself, not as
an adjacent prose paragraph or footnote. The identifying test for C-46 is a single
structural inspection: locate the CONVICTION GAP DIAGNOSIS table in REFLECTION and scan
its rows for a non-data RULE sentinel row whose primary cell content is an enforcement
rule rather than an artifact entry. Its absence fails C-46 immediately, regardless of
whether an equivalent prose directive appears outside the table boundary. (2)
**Prose-compression invariance established (R17 V-05)**: V-05 (Minimum-Density
Compression) confirms that the volume of surrounding prose — section preambles,
inter-table commentary, annotation paragraphs — has no effect on the structural verdict
for C-44, C-45, or any prior criterion in the chain. The evaluated property is the
structural placement of in-table sentinel rows; surrounding prose is non-load-bearing
regardless of compression level. This invariance extends to C-46 and C-47. The full
invariance property stack established through R17 is: (i) register — conversational
vs. formal (D16, extended D17); (ii) directive density — terse vs. exhaustive sentinel
text (D16); (iii) role-sequence — artifact generation order (D17); (iv) surrounding
prose volume — section prose compression (D18, V-05 R17). No combination of these
non-structural axes produces an in-table sentinel row where none structurally exists.
The five-sentinel chain test for C-47 extends the D17 eight-step chain test with two
additional steps: (1) verify C-34 FULL — 4-col CONVICTION DELTA with in-cell
Amplification chain template; (2) verify C-35 FULL — 6-col CONVICTION GAP DIAGNOSIS
with pre-declared artifact rows and register-split columns; (3) verify C-38 FULL —
named Req-ID rows with SETUP SCOUT TRACEABILITY TABLE match directive; (4) verify C-40
FULL — 4-col INERTIA MODEL MAP in SETUP with CONVICTION DELTA rows pre-named from MAP
entries and explicit match directive; (5) verify C-42 FULL — in-table RULE sentinel
inside the MAP preceding CT data rows; (6) verify C-43 second component FULL —
in-table RULE sentinel inside CONVICTION DELTA binding each Conv-ID to a MAP entry;
(7) verify C-44 FULL — non-data RULE sentinel inside the SCOUT TRACEABILITY TABLE
preceding Req-ID data rows; (8) verify C-45 fourth component FULL — TRACEABILITY AUDIT
carries its own in-table RULE sentinel binding each Req-ID to a SCOUT TABLE entry and
declaring named-identifier absence as the failure mode; (9) verify C-46 FULL —
non-data RULE sentinel inside the CONVICTION GAP DIAGNOSIS preceding artifact data
rows, text declares each artifact row must match a named INERTIA MODEL MAP entry and
that a missing row is a named-artifact absence; (10) verify that no structural table in
the blueprint relies on external prose as its sole enforcement mechanism. Failure at
step 9 fails C-47 even if steps 1–8 pass. The distinguishing boundary: a variant
carrying the v17 ceiling pattern (263) with a C-35-compliant CONVICTION GAP DIAGNOSIS
but no in-table sentinel earns C-46 NO CREDIT and C-47 NO CREDIT; extending that
variant with an in-table RULE sentinel inside the CONVICTION GAP DIAGNOSIS earns C-46
FULL and, combined with C-45, C-47 FULL. A ceiling-breaking variant for v18 must carry
the v17 ceiling pattern (263) and extend the CONVICTION GAP DIAGNOSIS table with an
in-table RULE sentinel row binding artifact rows to INERTIA MODEL MAP entries and
declaring named-artifact absence as the failure mode. Base 263 (v17 ceiling) + 5
(C-46) + 5 (C-47) = **273**.

**Retroactive R17 scoring under v18:**

| Variant | v17 | C-46 | C-47 | v18 |
|---------|-----|------|------|-----|
| V-01 — SCOUT TABLE Sentinel Only | 258 | 0 | 0 | **258** |
| V-02 — Minimum-Form Four-Sentinel | 263 | 0 | 0 | **263** |
| V-03 — Conversational Register | 263 | 0 | 0 | **263** |
| V-04 — Maximum-Density Four-Sentinel | 263 | 0 | 0 | **263** |
| V-05 — Minimum-Density Compression | 263 | 0 | 0 | **263** |

No R17 variant earns C-46 or C-47. All variants deliver a CONVICTION GAP DIAGNOSIS
meeting C-35 requirements without an in-table RULE sentinel row. V-05's compressed
prose envelope does not alter this verdict — surrounding prose volume is non-load-bearing
for C-46 (D18 prose-compression invariance). V-01 additionally fails C-45 (missing
TRACEABILITY AUDIT sentinel) and holds at 258; V-02–V-05 hold at 263. The R17 pattern
confirms that the four-sentinel chain is structurally complete and invariant across all
four confirmed non-structural axes. The only path to the v18 ceiling (273) runs through
an in-table RULE sentinel inside the CONVICTION GAP DIAGNOSIS.

**Scale:** 263 (v17 ceiling) + 5 + 5 = **273 ceiling**

---

### v17 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 263):**

**C-44 — SCOUT TRACEABILITY TABLE In-Table Enforcement Sentinel** (5 pts, FULL or NO
CREDIT): C-38 passes when the TRACEABILITY AUDIT in REFLECTION carries named Req-ID
rows sourced from the SETUP SCOUT TRACEABILITY TABLE, with an explicit directive —
prose or in-table — establishing that the audit row count must match the SETUP entry
count and that a missing row is a named-identifier absence. C-44 tests whether that
enforcement directive is structurally embedded inside the SCOUT TRACEABILITY TABLE
itself as an in-table RULE sentinel row, rather than existing only as a prose annotation
attached to the table from outside. A passing instance: (1) satisfies all C-38
requirements — named Req-ID rows (R-01, R-02, R-03) in the TRACEABILITY AUDIT sourced
from the SETUP SCOUT TRACEABILITY TABLE; Scout-Requirements Friction column values
sourced from the SETUP table; an explicit match directive present; (2) the SCOUT
TRACEABILITY TABLE in SETUP itself carries a non-data RULE sentinel row — positioned
before the Req-ID data rows — whose cell text embeds the structural enforcement rule:
that the TRACEABILITY AUDIT in REFLECTION must contain exactly one row per SETUP entry
and that a missing row is a named-identifier absence (R-[NN] absent), not a count
discrepancy; (3) the enforcement rule is table-internal — visible as part of the SCOUT
TRACEABILITY TABLE structure at the point of authoring, not only as a separate prose
paragraph or footnote outside the table boundary. The structural distinction from C-38:
C-38 passes when the match directive is explicit and binding, whether delivered as prose
or in-table; C-44 passes only when the directive is embedded as an in-table RULE
sentinel inside the SCOUT TRACEABILITY TABLE, making the table self-enforcing. The
upgrade chain for the traceability axis: C-29 (prose traceability instruction —
epistemic) → C-36 (6-column structural table, anonymous template rows — ontological at
cell level) → C-38 (6-column structural table, named SETUP-linked rows — ontological at
entry level) → C-44 (SCOUT TRACEABILITY TABLE carries in-table RULE sentinel row,
making the table self-enforcing). This is the direct parallel of C-42 on the
traceability axis: C-42 embeds an in-table sentinel inside the INERTIA MODEL MAP
(conviction-type axis); C-44 embeds an in-table sentinel inside the SCOUT TRACEABILITY
TABLE (traceability axis). Neither R16 variant earns C-44: V-01 carries a formal prose
paragraph as its traceability match directive; V-02 carries a conversational prose
directive — both are outside the SCOUT TRACEABILITY TABLE boundary, earning C-38 FULL
and C-44 NO CREDIT. Role-sequence invariance (D17) does not alter this verdict:
generation-phase reordering cannot produce a table-internal sentinel where none exists.

**C-45 — Complete Four-Sentinel Structural Chain** (5 pts, FULL or NO CREDIT): C-43
passes when both the INERTIA MODEL MAP (SETUP) and the CONVICTION DELTA (REFLECTION)
carry in-table RULE sentinel rows, completing the conviction-type linkage chain with
full in-table enforcement. C-45 tests whether the structural chain achieves maximum
in-table enforcement density across both structural axes — conviction-type and
traceability — simultaneously, with all four structural linkage tables carrying in-table
RULE sentinel rows and no structural linkage phase relying on external prose annotation
as the governing constraint. A passing instance: (1) satisfies all C-43 requirements —
MAP in-table RULE sentinel (C-42 FULL) and CONVICTION DELTA in-table RULE sentinel
(C-43 second component present); (2) satisfies C-44 FULL — the SCOUT TRACEABILITY
TABLE in SETUP carries a non-data RULE sentinel row preceding the Req-ID data rows,
whose text declares that the TRACEABILITY AUDIT must contain one row per SETUP entry
and that a missing row is a named-identifier absence; (3) the TRACEABILITY AUDIT table
in REFLECTION independently carries an in-table RULE sentinel row whose text states
that each row's Req-ID must match a named SCOUT TRACEABILITY TABLE entry and that a
missing row is a named-identifier absence — parallel in function to the CONVICTION
DELTA sentinel (C-43 second component) but applied to the traceability verification
phase; (4) all four in-table structural sentinels are present simultaneously: MAP
sentinel (SETUP, conviction-type axis), CONVICTION DELTA sentinel (REFLECTION,
conviction-type axis), SCOUT TRACEABILITY TABLE sentinel (SETUP, traceability axis),
TRACEABILITY AUDIT sentinel (REFLECTION, traceability axis). The structural distinction
from C-43: C-43 passes when the conviction-type linkage chain is fully sentinel-enforced
across both SETUP and REFLECTION phases; C-45 passes only when both axes —
conviction-type and traceability — achieve complete in-table enforcement across both
phases, completing a four-sentinel chain where no structural linkage point relies on
external prose as its sole enforcement mechanism. A variant earning C-43 FULL but
carrying prose-only match directives for the traceability axis earns C-45 NO CREDIT
even if those directives are otherwise semantically identical to passing sentinels.
Neither R16 variant earns C-45: both fail C-44 (no in-table sentinel inside the SCOUT
TRACEABILITY TABLE), making C-45 unreachable via strict superset dependency.

**One new diagnostic rule:**

**D17 (Role-sequence invariance and traceability sentinel chain; four-sentinel chain
test)**: The R16 round establishes two invariance properties relevant to
ceiling-breaking: (1) **Role-sequence invariance**: The artifact generation order
within the blueprint — Pitch-first, Spec-first, Proposal-first, or any permutation —
has no effect on structural table scoring. SETUP table structure and REFLECTION table
structure are evaluated independently of which artifact is generated first. A
ceiling-breaking variant cannot be constructed by reordering generation phases;
in-table RULE sentinel rows must appear inside the structural tables regardless of
sequence. This invariance applies to both axes: conviction-type (MAP sentinel,
CONVICTION DELTA sentinel) and traceability (SCOUT TRACEABILITY TABLE sentinel,
TRACEABILITY AUDIT sentinel). No generation-phase reordering causes a sentinel to
appear or disappear — the structural property is evaluated at the table level, not the
sequence level. (2) **Register invariance re-confirmed under full conversational
framing**: V-02 (R16) extends D16's register invariance finding to a complete
conversational-register blueprint in which the SETUP match directive itself is phrased
conversationally ("One thing to remember…"). The in-table vs. prose-only distinction
for C-42, C-43, C-44, and C-45 is strictly structural — a conversational prose
directive is outside the table boundary and earns C-44 NO CREDIT regardless of semantic
equivalence to a passing in-table sentinel. Register invariance extends symmetrically:
a conversational-register in-table RULE sentinel earns C-44 FULL; a formal-register
prose directive earns C-44 NO CREDIT. The four-sentinel chain test for C-45 extends the
D16 six-step chain test with two additional steps: (1) verify C-34 FULL — 4-column
CONVICTION DELTA with in-cell Amplification chain template; (2) verify C-35 FULL —
6-column CONVICTION GAP DIAGNOSIS with pre-declared artifact rows and register-split
columns; (3) verify C-38 FULL — named Req-ID rows with SETUP SCOUT TRACEABILITY TABLE
match directive; (4) verify C-40 FULL — 4-column INERTIA MODEL MAP in SETUP with
CONVICTION DELTA rows pre-named from MAP entries and explicit match directive; (5)
verify C-42 FULL — in-table RULE sentinel inside the MAP preceding CT data rows; (6)
verify C-43 second component FULL — in-table RULE sentinel inside CONVICTION DELTA
binding each Conv-ID to a MAP entry; (7) verify C-44 FULL — non-data RULE sentinel
inside the SCOUT TRACEABILITY TABLE preceding Req-ID data rows; (8) verify that the
TRACEABILITY AUDIT in REFLECTION carries its own in-table RULE sentinel binding each
Req-ID row to a SCOUT TRACEABILITY TABLE entry and declaring named-identifier absence
as the failure mode. Failure at steps 7–8 fails C-45 even if steps 1–6 pass. The
distinguishing boundary: a variant carrying the v16 ceiling pattern (253) with
prose-only match directives for the traceability axis earns C-44 NO CREDIT and C-45 NO
CREDIT; extending that variant with in-table RULE sentinels in both the SCOUT
TRACEABILITY TABLE (SETUP) and the TRACEABILITY AUDIT (REFLECTION) earns C-44 FULL
and, combined with C-43, C-45 FULL. **Full invariance property stack established
through R16**: the presence or absence of an in-table RULE sentinel row is a strictly
structural property independent of (i) register — conversational vs. formal (D16,
extended D17); (ii) directive density — terse vs. exhaustive prose (D16); (iii)
artifact generation order — Pitch-first, Spec-first, or any permutation (D17). A
ceiling-breaking variant for v17 must carry the v16 ceiling pattern (253) and extend
both the traceability SETUP table (SCOUT TRACEABILITY TABLE) and the traceability
REFLECTION table (TRACEABILITY AUDIT) with in-table RULE sentinel rows, without
reliance on any of the three confirmed non-structural axes.

**Retroactive R16 scoring under v17:**

| Variant | v16 | C-44 | C-45 | v17 |
|---------|-----|------|------|-----|
| V-01 — Pitch-First Role Sequence | 243 | 0 | 0 | **243** |
| V-02 — Conversational Register | 243 | 0 | 0 | **243** |

Neither R16 variant earns C-44 or C-45. V-01 delivers the match directive as a formal
prose paragraph following the SCOUT TRACEABILITY TABLE; V-02 delivers it as a
conversational prose directive ("One thing to remember…") — in both cases the directive
is outside the table boundary, earning C-38 FULL and C-44 NO CREDIT. The D17
role-sequence and register invariance findings confirm that neither generation-phase
reordering nor register change can supply the missing structural property.

The R16 pattern completes the invariance axis survey for the current structural level:
register (D16), directive density (D16), and role-sequence (D17) are all confirmed as
non-ceiling-breaking axes. The only path to the v17 ceiling (263) runs through
structural sentinel placement on the traceability axis — in-table RULE rows inside the
SCOUT TRACEABILITY TABLE (SETUP) and the TRACEABILITY AUDIT (REFLECTION), parallel to
the conviction-type axis sentinels introduced by V-04 in R15. Base 253 (v16 ceiling) +
5 (C-44) + 5 (C-45) = **263**.

**Scale:** 253 (v16 ceiling) + 5 + 5 = **263 ceiling**

---

### v16 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 253):**

**C-42 — INERTIA MODEL MAP In-Table Enforcement Sentinel** (5 pts, FULL or NO CREDIT):
C-40 passes when the INERTIA MODEL MAP in SETUP carries a 4-column structure with named
conviction-type entries and an explicit match directive — prose or otherwise —
establishing that CONVICTION DELTA rows must correspond one-to-one to MAP entries. C-42
tests whether that enforcement directive is structurally embedded inside the MAP table
itself as an in-table RULE sentinel row, rather than existing only as a prose annotation
attached to the table from outside. A passing instance: (1) satisfies all C-40
requirements — 4-column INERTIA MODEL MAP (Conv-ID | Conviction type | Artifact |
Role/register) with named CT-identifiers (CT-Spec, CT-Prop, CT-Pitch) present in SETUP;
CONVICTION DELTA rows in REFLECTION pre-named from MAP entries; an explicit SETUP match
directive present; (2) the MAP table itself carries a non-data RULE sentinel row —
positioned before the CT data rows — whose cell text embeds the structural enforcement
rule: that the CONVICTION DELTA in REFLECTION must contain exactly one row per MAP entry
and that a missing row is a named-conviction-type absence (CT-[X] absent), not a count
discrepancy; (3) the enforcement rule is table-internal — it is visible as part of the
MAP structure at the point of authoring, not only as a separate prose paragraph or
footnote outside the table boundary. The structural distinction from C-40: C-40 passes
when the match directive is explicit and binding, whether delivered as prose or in-table;
C-42 passes only when the directive is embedded as an in-table RULE sentinel, making the
MAP self-enforcing — its structure simultaneously declares the named conviction-type
entries and the rule that binds CONVICTION DELTA to those entries. The upgrade chain for
the INERTIA MODEL MAP phase: C-40 (4-column MAP, named CT entries, external or in-table
directive) → C-42 (4-column MAP, named CT entries, in-table RULE sentinel row preceding
data rows). V-04 (R15) earns FULL — the MAP carries an explicit RULE sentinel row: "The
CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop,
CT-Pitch). A missing row is a named-conviction-type absence." V-02, V-03, and V-05
(R15) earn C-40 FULL but C-42 NO CREDIT — all three deliver the match directive as
prose only, with no in-table sentinel row inside the MAP structure.

**C-43 — DUAL IN-TABLE SENTINEL CHAIN** (5 pts, FULL or NO CREDIT): C-41 passes when
both SETUP-anchored structural tables (INERTIA MODEL MAP → CONVICTION DELTA; SCOUT
TRACEABILITY TABLE → TRACEABILITY AUDIT) carry pre-named rows from their respective
SETUP sources, completing a chain where both REFLECTION-phase verification tables rely
on named-entry presence rather than anonymous count comparison. C-43 tests whether the
chain achieves maximum structural enforcement density — both the INERTIA MODEL MAP in
SETUP and the CONVICTION DELTA table in REFLECTION carry in-table RULE sentinel rows,
so every conviction-type linkage point declares its own structural enforcement rule
in-table with no phase relying on external prose annotation as the governing constraint.
A passing instance: (1) satisfies all C-41 requirements — INERTIA MODEL MAP (4-col,
named CT entries, SETUP match directive), CONVICTION DELTA (CT-named rows, MAP-linked,
SETUP match directive), TRACEABILITY AUDIT (Req-ID-named rows, SETUP-linked, row-count
match directive), plus the full C-34/C-35/C-38 structural chain; (2) the INERTIA MODEL
MAP carries an in-table RULE sentinel satisfying C-42 FULL — a non-data row inside the
MAP table whose text declares that CONVICTION DELTA must contain one row per MAP entry
and that a missing row is a named-conviction-type absence; (3) the CONVICTION DELTA
table in REFLECTION independently carries an in-table RULE sentinel row whose text
states that each row's Conv-ID must match a named INERTIA MODEL MAP entry and that a
missing row is a named-conviction-type absence — parallel in function to the MAP
sentinel but applied at the REFLECTION verification phase; (4) all three in-table
structural sentinels are present simultaneously: MAP sentinel (SETUP, enforcing
CONVICTION DELTA row count and naming), CONVICTION DELTA sentinel (REFLECTION,
enforcing MAP-linkage per row), and the C-38-level Req-ID-named rows in the
TRACEABILITY AUDIT (REFLECTION, enforcing SETUP SCOUT TRACEABILITY TABLE alignment).
The structural distinction from C-41: C-41 passes when both SETUP-anchored phases carry
pre-named rows with explicit match directives, whether those directives are prose or
in-table; C-43 passes only when both the MAP (SETUP) and the CONVICTION DELTA
(REFLECTION) carry in-table RULE sentinel rows — completing a chain where every
conviction-type linkage phase is self-enforcing by table structure, not only by external
prose instruction. A variant that passes C-41 via prose-only directives in the MAP and
CONVICTION DELTA earns C-43 NO CREDIT even if the directive text is otherwise identical
to a C-43-passing sentinel. V-04 (R15) earns FULL — MAP sentinel and CONVICTION DELTA
sentinel are both present, both in-table, both declaring named-conviction-type absence
as the failure mode. V-02, V-03, and V-05 (R15) earn C-41 FULL but C-43 NO CREDIT —
all three rely on prose-only match directives for the MAP and CONVICTION DELTA linkage
enforcement.

**One new diagnostic rule:**

**D16 (In-table RULE sentinel vs. prose-only enforcement directive; register and density
invariance)**: C-42 requires an in-table RULE sentinel row inside the INERTIA MODEL
MAP; a prose directive attached outside the MAP table earns C-40 FULL but C-42 NO
CREDIT. The identifying test for C-42 is a single structural inspection: locate the
INERTIA MODEL MAP table in SETUP and scan its rows for a non-data RULE sentinel row —
a row whose primary cell content is an enforcement rule rather than a conviction-type
entry. Its absence fails C-42 immediately, regardless of whether an equivalent prose
directive appears as a paragraph or footnote adjacent to the table. The chain test: C-43
is a strict superset of C-41; a C-43 evaluation proceeds in six steps extending the D15
chain test: (1) verify C-34 FULL — 4-column CONVICTION DELTA with in-cell Amplification
chain template in each CT-row; (2) verify C-35 FULL — 6-column CONVICTION GAP
DIAGNOSIS with pre-declared artifact rows and register-split columns; (3) verify C-38
FULL — named Req-ID rows with SETUP SCOUT TRACEABILITY TABLE match directive; (4)
verify C-40 FULL — 4-column INERTIA MODEL MAP in SETUP with CONVICTION DELTA rows
pre-named from MAP entries and explicit match directive; (5) verify C-42 FULL —
in-table RULE sentinel row inside the MAP preceding the CT data rows; (6) verify that
the CONVICTION DELTA table in REFLECTION carries its own in-table RULE sentinel binding
each row's Conv-ID to a MAP entry and declaring named-conviction-type absence as the
failure mode. Failure at steps 5–6 fails C-43 even if steps 1–4 pass. The
distinguishing boundary: a variant carrying the v15 ceiling pattern (243) with
prose-only match directives earns C-42 NO CREDIT and C-43 NO CREDIT; extending that
variant with in-table RULE sentinels in both the MAP and the CONVICTION DELTA table
earns C-42 FULL and, combined with C-41, C-43 FULL. **Property invariance established
in R15**: V-03 (conversational register) and V-05 (minimum directive density) both earn
C-40/C-41 FULL at 243 — confirming that register and prose volume do not affect
structural verdict. This invariance extends to C-42 and C-43: the presence or absence
of an in-table RULE sentinel row is a strictly structural property independent of the
blueprint's register (conversational vs. formal) and independent of the density of
surrounding prose. A conversational-register MAP sentinel earns C-42 FULL; a
formal-register MAP with prose-only directive earns C-42 NO CREDIT regardless of
directive length or specificity.

**Retroactive R15 scoring under v16:**

| Variant | v15 | C-42 | C-43 | v16 |
|---------|-----|------|------|-----|
| V-01 — INERTIA MODEL MAP SETUP Only | 233 | 0 | 0 | **233** |
| V-02 — Full C-40+C-41 Minimum Form | 243 | 0 | 0 | **243** |
| V-03 — Conversational Register | 243 | 0 | 0 | **243** |
| V-04 — Maximum-Density C-40+C-41 | 243 | +5 | +5 | **253** |
| V-05 — Minimum-Density C-40+C-41 | 243 | 0 | 0 | **243** |

V-04 is the sole R15 ceiling-breaker, climbing from 243 to 253 via C-42 + C-43. V-02,
V-03, and V-05 hold at 243 — each delivers the correct MAP and CONVICTION DELTA
structural axes but relies on prose-only match directives, earning C-40/C-41 FULL and
C-42/C-43 NO CREDIT. V-01 holds at 233 (C-40 NO CREDIT from D15 step 2 failure; all
higher-chain criteria unreachable).

The R15 pattern mirrors the structural upgrade trajectory of R12 (C-36: TRACEABILITY
AUDIT table form) and R14 (C-38: TRACEABILITY AUDIT named-row SETUP linkage): in each
case a single variant introduces in-table structural enforcement at a phase previously
governed by prose or anonymous-template forms. V-04 introduces the upgrade
simultaneously at two phases — SETUP MAP and REFLECTION CONVICTION DELTA — yielding two
new criteria whose combination (C-43) closes the in-table enforcement chain across the
full conviction-type linkage axis. V-03 and V-05 contribute a complementary diagnostic
finding: the structural properties tested by C-40 through C-43 are invariant across
register and directive density, confirming that the rubric evaluates table structure
rather than prose style or volume. A ceiling-breaking variant must carry the v15
ceiling pattern (243) and extend both the INERTIA MODEL MAP in SETUP and the CONVICTION
DELTA table in REFLECTION with in-table RULE sentinel rows: base 243 (v15 ceiling) + 5
(C-42) + 5 (C-43) = **253**.

**Scale:** 243 (v15 ceiling) + 5 + 5 = **253 ceiling**

---

### v15 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 243):**

**C-40 — CONVICTION DELTA INERTIA-MAP SETUP LINKAGE** (5 pts, FULL or NO CREDIT): C-34
passes when CONVICTION DELTA is implemented as a structural 4-column table with a
pre-templated in-cell Amplification chain cell. C-40 tests whether the CONVICTION DELTA
table achieves SETUP linkage through the INERTIA MODEL MAP — the exact structural
upgrade that C-38 applied to the TRACEABILITY AUDIT, now applied to the CONVICTION
DELTA phase. A passing instance: (1) a 4-column INERTIA MODEL MAP appears in SETUP,
pre-declaring conviction type per artifact and establishing named source rows for the
REFLECTION CONVICTION DELTA table — the map is present at rubric time, not deferred to
REFLECTION; (2) the CONVICTION DELTA table in REFLECTION carries rows whose
conviction-type entries are pre-named from the INERTIA MODEL MAP, not introduced
anonymously in REFLECTION — each row's conviction type is a named identifier traceable
to a SETUP map entry, parallel to how C-38 requires each TRACEABILITY AUDIT row's
Req-ID to be drawn from the SETUP SCOUT TRACEABILITY TABLE; (3) an explicit directive
states that the CONVICTION DELTA row count must match the INERTIA MODEL MAP entry
count, and that a missing row is a named-conviction-type absence — visible at a glance
by named-entry absence, not discoverable only by count comparison. The structural
distinction from C-34: C-34 passes when CONVICTION DELTA is a 4-column table with
pre-templated Amplification chain cells in each version row; C-40 passes only when each
row's conviction type is bound to a SETUP-sourced INERTIA MODEL MAP entry, converting
row omission from an anonymous-count failure into a named-conviction-type absence. The
upgrade chain for the CONVICTION DELTA phase: C-31 (prose Req-ID citation — epistemic)
→ C-34 (4-column structural table, anonymous version rows — ontological at cell level)
→ C-40 (4-column structural table, named INERTIA MODEL MAP-linked rows — ontological at
entry level). V-02 (R14) has the INERTIA MODEL MAP in SETUP (FULL) but earns C-40 NO
CREDIT — REFLECTION is absent, so no CONVICTION DELTA table exists to carry named rows.
