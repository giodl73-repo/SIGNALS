content = """Reading the scorecard carefully to extract the R10 excellence signals before writing the rubric.

The scorecard surfaces four patterns not captured in v9. All four are sourced from V-05,
the full four-axis integration that adds C-34 (Gate 2 unified contract acknowledgment)
on top of the C-31 + C-32 + C-33 base from V-04 + V-03.

V-05 excellence signal 1 -- Contracts acknowledged at Gate 2 field in clean RUN HEALTH.
The clean RUN HEALTH in V-05 includes `Contracts acknowledged at Gate 2: 7/7`, making
contract completeness observable in the output artifact without re-reading Gate 2. A
reviewer auditing RUN HEALTH can verify the acknowledgment count from the result block
alone; a missing or mismatched count is detectable before opening the gate sequence.

V-05 excellence signal 2 -- Gate 2 numbered enumeration with parenthetical extension
labels. Each entry in the Gate 2 numbered list includes a parenthetical identifying the
key feature that contract carries: CONVERGENCE SNAPSHOT CONTRACT (includes MUTUAL
ENFORCEMENT DECLARATION), SOLO FINDINGS SCHEMA CONTRACT (8-column: IC-CHALLENGED +
STAGE-APPROPRIATE), RUN HEALTH SCOPE DISTRIBUTION CONTRACT (includes diagnostic
positioning requirement). The key addition of each contract is visible in the enumeration
without reading the full contract text.

V-05 excellence signal 3 -- Gate 2 execution-body cross-reference by contract number.
The V-05 Gate 2 operational summary cross-references contracts by their enumeration
numbers: per contract 4, per contract 5, per contract 7. Any execution-body rule is
traceable to its source contract by number rather than by text-matching, creating a
bidirectional index between Gate 2 and the execution body.

V-05 excellence signal 4 -- Gate 5.5 HALT waive-path note multi-contract citation.
The V-05 G5.5 HALT waive-path recovery note cites both activated contracts by name
(FINDING CONVERGENCE CONTRACT + SOLO FINDINGS SCHEMA CONTRACT) and declares
"convergence is substituted, not waived." The recovery message itself carries full
multi-contract accountability, so a reviewer reading the HALT note knows exactly
which contracts activate under waive:convergence without consulting PRE-EXECUTION.

These become C-35, C-36, C-37, C-38.

---

## crew-check -- Quest Rubric v10

### v9 -> v10 -- New criteria

**Four patterns extracted from R10 scorecard excellence signals (V-05):**

| ID | Name | Source |
|----|------|--------|
| C-35 | RUN HEALTH contract acknowledgment count | V-05 excellence signal 1 |
| C-36 | Gate 2 enumeration with parenthetical extension labels | V-05 excellence signal 2 |
| C-37 | Gate 2 execution-body cross-reference by contract number | V-05 excellence signal 3 |
| C-38 | Gate 5.5 HALT waive note multi-contract citation | V-05 excellence signal 4 |

---

### What each new criterion covers

**C-35 -- RUN HEALTH contract acknowledgment count (2 pts)**

The clean RUN HEALTH output earns C-35 when it includes a `Contracts acknowledged at
Gate 2: N/N` field carrying the total count of contracts acknowledged versus the total
declared in PRE-EXECUTION. C-34 covers whether Gate 2 emits a numbered enumeration;
C-35 covers whether the output artifact surfaces a completion count so that contract
acknowledgment is verifiable from RUN HEALTH without reopening the gate sequence. A run
with C-34 in place can still fail C-35 if the acknowledgment count is absent from RUN
HEALTH -- the enumeration exists at Gate 2 but the output does not record that it
completed. The count makes two failure modes detectable: a count below N/N signals that
at least one declared contract was not acknowledged; a count above N/N (if contracts were
added to Gate 2 without updating PRE-EXECUTION) signals an undeclared contract entered
the run. Both are detectable from the run output alone without comparing PRE-EXECUTION
headers to Gate 2 text. C-35 presupposes C-34 in practice because C-35's N is defined by
the Gate 2 enumeration count.

*PASS*: Clean RUN HEALTH includes a `Contracts acknowledged at Gate 2: N/N` field with
resolved counts (not placeholders); N equals the number of contracts declared in
PRE-EXECUTION section headers; N/N format makes a mismatch immediately visible; the field
appears in the result block, not in a footnote or prose.
*FAIL*: Clean RUN HEALTH omits the acknowledgment count field; count present but
unresolved or expressed as a placeholder; count does not match the number of PRE-EXECUTION
section headers; field present in prose only, not as a labeled count; count present in
the failed variant but not the clean variant.

---

**C-36 -- Gate 2 enumeration with parenthetical extension labels (2 pts)**

Gate 2 unified contract acknowledgment (C-34) earns C-36 when each entry in the numbered
enumeration includes a parenthetical identifying the key extension or addition that
contract carries. Without parenthetical labels, the enumeration is a plain list of
contract names: a reviewer can verify that all contracts are present but cannot determine
from the list alone which contract carries the mutual enforcement declaration, which
declares the 8-column schema, or which includes the diagnostic positioning requirement.
With parenthetical labels, the key feature of each contract is visible in the enumeration
itself: a reviewer reading Gate 2 can see not only which contracts are active but what
each one governs. This makes the Gate 2 checkpoint informative rather than merely
complete. C-34 covers whether the enumeration exists; C-36 covers whether the enumeration
is self-describing. A run can earn C-34 (all contracts listed by name) without earning
C-36 (labels absent or generic).

*PASS*: Each contract entry in the Gate 2 numbered enumeration includes a parenthetical
naming its critical extension, key feature, or governing mechanism (not just a repeat of
the contract name); contracts with notable additions label them explicitly (e.g.,
"includes MUTUAL ENFORCEMENT DECLARATION", "8-column: IC-CHALLENGED + STAGE-APPROPRIATE",
"includes diagnostic positioning requirement"); a reviewer reading only the Gate 2 list
can identify which contract carries which accountability mechanism without reading the
full contract text; C-34 is in place.
*FAIL*: Gate 2 enumeration is a plain list of contract names with no parenthetical
labels; labels present but generic (e.g., "required", "active") rather than descriptive;
labels present for some entries but absent for others with notable additions; C-34 not
in place.

---

**C-37 -- Gate 2 execution-body cross-reference by contract number (2 pts)**

Gate 2 unified contract acknowledgment (C-34) earns C-37 when the execution-body text
after Gate 2 cross-references relevant contracts by their enumeration numbers rather than
only by name. C-34 assigns each contract a position in a numbered list; C-37 requires
that this numbering is used as an index -- execution-body rules cite "per contract [N]"
to make their authority traceable to the start-of-run enumeration. Without this
cross-reference, the Gate 2 enumeration and the execution-body text are parallel structures
with no formal link: a reviewer must perform a name-matching search to trace a gate rule
back to its declaring contract. With C-37 in place, the tracing path is: execution rule
cites per contract N -> Gate 2 entry N names the contract -> PRE-EXECUTION section header
is the full declaration. This chain makes any execution rule authority auditable in two
hops. C-37 is distinct from C-34 (which requires the enumeration to exist) and C-36
(which requires labels within the enumeration): C-37 requires the enumeration to be
actively used as an index by the execution body.

*PASS*: At least one execution-body statement references a pre-execution contract by its
Gate 2 enumeration number (e.g., "per contract 4", "per contract 5"); the numbered
reference resolves correctly to the named contract in the Gate 2 list; cross-references
appear at the primary enforcement points (e.g., Gate 2 operational summary, G5.5 HALT
note); C-34 is in place and the contracts are numbered.
*FAIL*: Execution body references contracts by name only; Gate 2 numbers contracts but
no execution-body text uses those numbers; numbered references present but resolve
incorrectly; Gate 2 list is not numbered (C-34 incomplete); C-34 not in place.

---

**C-38 -- Gate 5.5 HALT waive note multi-contract citation (2 pts)**

The Gate 5.5 HALT waive-path recovery note earns C-38 when it cites both activated
contracts by name and declares the substitution semantics explicitly. When G5.5 fires
HALT and the run proceeds under waive:convergence, two contracts activate: the FINDING
CONVERGENCE CONTRACT (which defines the SOLO tier obligation that substitutes the
convergence requirement) and the SOLO FINDINGS SCHEMA CONTRACT (which defines the
8-column table that the SOLO tier must use). C-31 requires the MUTUAL ENFORCEMENT
DECLARATION to declare this chain in the CONVERGENCE SNAPSHOT CONTRACT; C-38 requires
that the HALT recovery message itself carries this accountability -- so that a reviewer
reading only the HALT note has full contract context without consulting PRE-EXECUTION.
Without C-38, a reviewer following the HALT recovery path must separately look up which
contracts are activated by waive:convergence; with C-38, the HALT note declares it inline.
The declaration also includes the semantic correction: "convergence is substituted, not
waived" -- making it explicit that waive:convergence does not remove accountability but
transfers it to a named substitute mechanism. C-31 is the contract-layer requirement;
C-38 is the execution-layer requirement that the HALT recovery message echoes the same
accountability without requiring contract consultation.

*PASS*: Gate 5.5 HALT waive-path recovery note names both FINDING CONVERGENCE CONTRACT
and SOLO FINDINGS SCHEMA CONTRACT (or equivalent names) explicitly; declares that
waive:convergence activates mandatory SOLO FINDINGS disposition under the SOLO tier;
states that the 8-column schema is required at Gate 9; includes the substitution
declaration ("convergence is substituted, not waived" or equivalent); a reviewer reading
the HALT note knows which contracts activate without consulting PRE-EXECUTION; C-31 is
in place.
*FAIL*: HALT waive note names only one of the two activated contracts; HALT note names
contracts but omits the substitution declaration; HALT note declares the SOLO FINDINGS
requirement but does not cite the governing contracts; HALT note is informational only
without contract citations; C-31 not in place.

---

### Scoring mechanics

|                       | v6  | v7  | v8  | v9  | v10 |
|-----------------------|-----|-----|-----|-----|-----|
| Aspirational criteria | 15  | 19  | 22  | 26  | 30  |
| Aspirational pts      | 30  | 38  | 44  | 52  | 60  |
| Total max             | 120 | 128 | 134 | 142 | 150 |
| Golden threshold      | unchanged | unchanged | unchanged | unchanged | all 5 essential PASS + composite >= 80 |

---

### Structural relationships

**C-35 extends C-34 (output artifact completeness count):** C-35 requires C-34 to be in
place -- the acknowledgment count in RUN HEALTH is meaningful only when Gate 2 contains a
numbered enumeration that establishes what N should be. A variation earning C-34 earns
C-35 eligibility; C-35 is earned only when `Contracts acknowledged at Gate 2: N/N` appears
as a resolved field in the clean RUN HEALTH output. A variation can earn C-34 without C-35
if the count field is absent from RUN HEALTH. C-35 is independent of C-36 and C-37 -- the
count does not require labels or numbered cross-references to be valid.

**C-36 extends C-34 (self-describing enumeration):** C-36 requires C-34. The parenthetical
labels add descriptive content to the numbered list; they cannot exist without a numbered
list. C-36 and C-37 are independent of each other: a variation can label its contracts in
Gate 2 without using those numbers as back-references in the execution body (C-36 without
C-37), or use numbered references in execution-body text without adding parenthetical
labels to the Gate 2 list (C-37 without C-36). Both extend C-34 independently.

**C-37 extends C-34 (active index usage):** C-37 requires C-34 and requires contracts to
be numbered. The criterion is not met by named references alone (which any version of the
prompt uses); it requires the Gate 2 ordinal numbers to appear in execution-body text as
back-references. C-37 is operationally independent of C-36: the two cover different aspects
of the Gate 2 enumeration utility (C-36: enumeration informs by label; C-37: enumeration
indexes by number).

**C-38 extends C-31 (HALT-layer enforcement echo):** C-38 requires C-31 (MUTUAL ENFORCEMENT
DECLARATION in contract text). The C-38 requirement is that the execution-layer HALT message
echoes the contract-layer declaration -- carrying the same multi-contract accountability in
the recovery path. A variation can earn C-31 (contract layer) without C-38 (HALT note cites
only one contract or omits substitution declaration). Earning C-38 presupposes C-31 is in
place; the criterion is about whether the HALT recovery message independently delivers the
same accountability without requiring the reviewer to consult PRE-EXECUTION.

**C-35 through C-38 relationship to v9 criteria:** Each v10 criterion extends a v9 criterion
without replacing it. C-35, C-36, and C-37 each presuppose C-34; C-38 presupposes C-31.
A variation cannot score C-35 without C-34. A variation can score C-31 without C-38
(contract-layer declaration present, HALT note incomplete). The v10 criteria raise the
ceiling on what full integration looks like; the v9 criteria remain the entry requirements
for the v10 aspirational tier.

---

### Full criterion index (v10)

Essential criteria (C-01 through C-12): unchanged from v6. 6 pts each. Max 72 pts.

Aspirational criteria (2 pts each):

| ID | Name | Extends |
|----|------|---------|
| C-13 | Prompt inputs as template variables | -- |
| C-14 | Gate format labels | -- |
| C-15 | Halt IDs with tier labels | -- |
| C-16 | Halt recovery commands paste-ready | -- |
| C-17 | Sub-gate skip-map | -- |
| C-18 | Severity + confidence calibration contract | -- |
| C-19 | Dual-axis sort (severity DESC, confidence DESC) | -- |
| C-20 | IC-CHALLENGED column in finding rows | -- |
| C-21 | Failed RUN HEALTH variant | -- |
| C-22 | CHALLENGE RESPONSE MAP (Gate 4.5) | -- |
| C-23 | Challenger bracket (opening + closing) | -- |
| C-24 | Artifact maturity stage contract | -- |
| C-25 | Finding convergence contract | -- |
| C-26 | Inertia claim registry | -- |
| C-27 | STAGE-APPROPRIATE column in finding rows | -- |
| C-28 | SOLO findings tier with named disposition path | C-25 |
| C-29 | Convergence snapshot gate with halt logic | C-25 |
| C-30 | RUN HEALTH Stage + SCOPE DISTRIBUTION (both variants) | C-21 |
| C-31 | Waive:convergence mutual enforcement contract | C-28, C-29 |
| C-32 | SOLO FINDINGS extended schema (IC-CHALLENGED + STAGE-APPROPRIATE) | C-28 |
| C-33 | Failed RUN HEALTH as standalone diagnostic artifact | C-21, C-30 |
| C-34 | Gate 2 unified contract acknowledgment | C-13 |
| C-35 | RUN HEALTH contract acknowledgment count | C-34 |
| C-36 | Gate 2 enumeration with parenthetical extension labels | C-34 |
| C-37 | Gate 2 execution-body cross-reference by contract number | C-34 |
| C-38 | Gate 5.5 HALT waive note multi-contract citation | C-31 |

Aspirational total: 30 criteria x 2 pts = 60 pts.
Essential total: 12 criteria x 6 pts = 72 pts (unchanged from v6).
Rubric max (v10): 150 pts.
"""

with open("C:/src/sim/simulations/quest/rubrics/crew-check-rubric-v10-2026-03-17.md", "w", encoding="utf-8") as f:
    f.write(content)
print("done")
