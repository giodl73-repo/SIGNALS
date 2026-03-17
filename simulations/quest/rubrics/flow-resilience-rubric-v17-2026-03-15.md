50 `### C-` headings = 8 essential/recommended (C-01–C-08) + 42 aspirational (C-09–C-50). ✓

Written to `simulations/quest/rubrics/flow-resilience-rubric-v17-2026-03-15.md` (1935 lines).

---

**v17 changes summary:**

Three new aspirational criteria extracted from R17 excellence signals:

| Criterion | E-tag | Signal | Cracked by |
|-----------|-------|--------|------------|
| **C-48** -- Named Enforcement Contract with Rule Identifiers | E-34 | All five variations introduce a named enforcement contract block (Document Enforcement Contract / § 1 Enforcement Mandate) with labeled rule identifiers (Rule A/B; § 1.1/§ 1.2) enabling citation by short-form label | All five |
| **C-49** -- Enforcement Preamble Pre-Positioning with Named-Label Sub-Part Reinforcement | E-35 | V-01/V-02/V-03/V-04 position enforcement contract before all sub-parts AND each sub-part cites rules by named label inline; V-05 FAIL | V-01, V-02, V-03, V-04 |
| **C-50** -- Multi-Level Enforcement with Explicit Restatement Label | E-36 | Three or more structurally independent hierarchy levels carry enforcement content; at least one carries an explicit restatement label ("restated for co-location", "§ 1.1 restated at column-contract level"); V-05 entered R17 passing | V-01, V-02, V-03, V-04 (V-05 entering) |

**Scoring delta**: uncapped max 78 → 84 (42 criteria × 2). Composite cap unchanged at 10.

**R17 final ranking**: V-01/V-02/V-03/V-04 tied at 84/84 (first four-way perfect tie); V-05 at 82/84 (C-49 FAIL). **Open for R18**: C-49 for V-05.
S | PASS | PASS | **84/84** |
| 1 (tie) | **V-04** | PASS | PASS | PASS | **84/84** |
| 5 | **V-05** | PASS | FAIL | PASS | **82/84** |

V-01/V-02/V-03/V-04 simultaneously achieve the new perfect uncapped ceiling 84/84 -- the first
four-way tie at the ceiling across all rounds. V-05, the R16 champion at 78/78, recedes to 82/84
(fails C-49: enforcement preamble not pre-positioned before all sub-parts with inline named-label
sub-part reinforcement). Open for R18: C-49 PASS for V-05.

**Orthogonality argument:**
- **C-48** is orthogonal to all prior criteria: it requires a named enforcement contract block that
  assigns referenceable identifiers (labels) to its constituent rules. No prior criterion requires
  a preamble-level contract to exist; prior enforcement-adjacent criteria (C-31, C-27, C-39, C-40)
  require bypass protocol declarations, rule registries, gate-open acknowledgments, and gate-close
  prohibition clauses -- none of which require an enforcement contract block with named rule labels.
- **C-49** is orthogonal to C-48: C-48 requires the enforcement contract to exist and assign rule
  identifiers; C-49 requires (a) the contract to be POSITIONED before all sub-parts it governs and
  (b) sub-parts to carry inline citations of those identifiers by name. A contract can exist (C-48
  PASS) with correct labels but be mispositioned after sub-parts, or sub-parts can omit inline
  citations -- either condition fails C-49 while C-48 passes. The pre-positioning requirement and
  the inline-citation requirement are additionally orthogonal to each other within C-49: a contract
  can be pre-positioned without any sub-part inline citations (satisfies positioning, fails
  citation) -- but because both components are required by C-49 jointly, the criterion is atomic at
  the PASS level.
- **C-50** is orthogonal to C-49: C-49 requires preamble pre-positioning and sub-part citations at
  a single structural level; C-50 requires the enforcement content to appear at three or more
  DISTINCT structural hierarchy levels (e.g., preamble level, sub-part level, column-contract
  level, document-header level) with at least one location carrying an explicit restatement label
  (e.g., "restated for co-location"). A template satisfying C-49 carries two levels (preamble +
  sub-part inline); C-50 requires at least one additional independent level with explicit
  restatement attribution. C-50 is also orthogonal to C-27 (named rule block registry, which
  centralizes rules for auditability) and C-39 (gate-open acknowledgment checkpoint): C-50 requires
  rules to be restated at structurally independent downstream locations, not merely centralized or
  confirmed at gate-entry.

**C-48 -- Named Enforcement Contract with Rule Identifiers (E-34)**
- Signal: All five variations in R17 introduce a named enforcement contract block (variously "Document
  Enforcement Contract", "§ 1 -- Enforcement Mandate", or equivalent) that carries individually
  labeled constituent rules (e.g., Rule A / Rule B; § 1.1 / § 1.2). The labels are short-form
  identifiers enabling citation by name in downstream content -- "**Rule A applies**" or
  "§ 1.1 applies" -- rather than requiring paraphrase or full restatement of rule prose. The
  enforcement contract block is a preamble-level structural element distinct from the rule registry
  (C-27, which indexes conditional linkage rules for audit) and from the bypass chain declaration
  (C-31, which enumerates remediation steps): the enforcement contract declares mandatory fill
  constraints and assigns each constraint a label.
- The gap it closes: Prior criteria establish rule registries (C-27) and gate-level acknowledgment
  checkpoints (C-39), but none require the template to carry a preamble-level enforcement block
  that names its rules with referenceable identifiers. Without named identifiers, sub-part inline
  reinforcement can only paraphrase or copy rule prose -- creating divergence risk between the
  preamble declaration and the downstream restatement. Named identifiers close this risk: a sub-part
  citing "Rule A applies" is verifiably referencing the same rule as the preamble's "Rule A:
  [prose]" regardless of restatement wording. The identifier also makes the rule independently
  auditable: a reviewer can scan for all Rule A invocations across the template without parsing
  prose.
- Pass requires: A named enforcement contract block (or equivalently named preamble element) is
  present that declares mandatory constraints applicable to sub-parts of the template. The block
  assigns a unique short-form identifier to each constituent constraint (e.g., Rule A, Rule B;
  § 1.1, § 1.2; RULE-FILL-1, RULE-FILL-2; or equivalent alphanumeric label). At least two distinct
  rule identifiers must be present. The identifier must be a label (not a prose heading) -- usable
  as a citation in downstream content without restating the full rule text.
- Partial: Enforcement contract block present and named but rules are identified only by ordinal
  position ("Rule 1", "Rule 2" as structural markers without short-form citation handles) rather
  than labeled identifiers; or block present with labeled identifiers but only one rule rather than
  two or more; or labeled identifiers present but embedded inline in gate prose rather than in a
  named enforcement contract block.
- Fail: No named enforcement contract block; mandatory fill constraints declared only in prose
  preamble or section headers without a distinct named block; or constraints present without any
  rule identifiers (rules defined as anonymous prose only).

**C-49 -- Enforcement Preamble Pre-Positioning with Named-Label Sub-Part Reinforcement (E-35)**
- Signal: V-01 through V-04 each position their enforcement contract block BEFORE all sub-parts
  (Steps 1a through 1d, or equivalent), and each sub-part carries inline reinforcement citing rules
  by their named labels: "**Rule A applies**" / "**Rule B applies**"; "§ 1.1 applies -- no blank
  cells. § 1.2 applies"; etc. V-04 additionally self-attests the positioning: "Document Enforcement
  Contract (**positioned before all sub-parts** -- read before filling any of Steps 1a through 1d)".
  V-05 carries preamble enforcement structure but the contract is not pre-positioned before all
  sub-parts with inline named-label citations in sub-parts, yielding C-49 FAIL.
- The gap it closes: C-48 requires the enforcement contract to exist and carry labeled identifiers.
  A contract that exists but is positioned after or among sub-parts can be missed or applied
  selectively; a contract that exists and is pre-positioned but whose sub-parts carry no inline
  citations allows the enforcement signal to decay by the time a filler reaches a late sub-part.
  Pre-positioning ensures the contract is read before any fill action; inline named-label citations
  reinforce the contract at the precise location where a constraint becomes relevant. Together they
  close the enforcement continuity gap: the contract governs the fill sequence from its pre-position
  declaration through to every individual sub-part's fill moment.
- Pass requires: The named enforcement contract block (C-48 PASS required) is positioned in the
  template before all sub-parts (steps, columns, sections) it governs -- not interleaved with
  sub-parts and not positioned after any of them. At least one sub-part carries inline reinforcement
  that cites at least one rule by its named label identifier (e.g., "**Rule A applies**",
  "§ 1.1 applies"). The inline citation must use the label defined in the enforcement contract --
  not a paraphrase or a generic "see preamble" pointer. C-48 FAIL subsumes C-49.
- Partial: Enforcement contract pre-positioned before all sub-parts but no sub-part carries inline
  named-label citations (pre-positioning without reinforcement); or at least one sub-part carries
  inline labeled citations but the enforcement contract is not pre-positioned before all sub-parts;
  or inline citations present but use paraphrase rather than the named label identifier; or C-48
  PARTIAL with pre-positioning and one sub-part citation.
- Fail: Enforcement contract block absent (C-48 FAIL subsumes C-49); or contract exists but is
  interleaved with or positioned after sub-parts with no inline sub-part citations; or inline
  reinforcement present only in summary/terminal positions rather than within individual sub-parts
  at fill time.

**C-50 -- Multi-Level Enforcement with Explicit Restatement Label (E-36)**
- Signal: V-01 through V-04 each carry the enforcement content at three or more structurally
  independent hierarchy levels, with at least one location bearing an explicit restatement label:
  V-01 (three levels: preamble, Step 1d inline, Column Contract -- "(restated for co-location)");
  V-02 (three levels: § 1 Mandate, sub-part 1d § citations, Column Contract --
  "§ 1.1 restated at column-contract level"); V-03 (four levels: D-Phase Enforcement Note at
  document-header, preamble within Pre-Commitment Document, sub-part 1d inline, Column Contract --
  "Rule B restated for co-location at column-contract level"); V-04 (four levels: preamble,
  sub-part 1d, Column Contract -- "(restated for co-location at column-contract level)", per-stage
  Row Descriptor bullets). V-05 satisfied C-50 entering R17 but not C-49.
- The gap it closes: C-49 requires the enforcement contract to be pre-positioned and cited in
  sub-parts -- but sub-part inline citations are by definition local to each sub-part. A filler
  working in a Column Contract section or a Row Descriptor block operates at a structurally distinct
  location from the preamble and the sub-part inline citations; if the enforcement rule is not
  present at that location, it is practically invisible at fill time. C-50 requires the rule to
  appear at structurally independent downstream locations, not merely in the preamble and adjacent
  sub-parts. The explicit restatement label ("restated for co-location") closes the audit gap:
  without it, a reviewer cannot distinguish a redundant copy of a rule (which might diverge) from
  an explicit restatement that is traceable to the authoritative preamble source.
- Pass requires: The enforcement content (at least one named rule from the C-48 contract) appears
  at three or more structurally independent hierarchy levels within the template. At least one of
  those locations outside the preamble carries an explicit restatement label (e.g., "restated for
  co-location", "restated at column-contract level", "§ 1.1 restated at [location]", or equivalent
  phrase). The restatement label must name the location-level context or purpose of the restatement.
  Three levels means three structurally distinct template positions -- preamble, sub-part inline,
  and at least one additional independent structural element (column contract, row descriptor, act
  header, etc.). C-48 FAIL subsumes C-50.
- Partial: Enforcement content at three or more levels but no explicit restatement label at any
  location outside the preamble; or explicit restatement label present but only two independent
  hierarchy levels carry the enforcement content; or restatement label present but does not name
  the location context (bare "see above" without identifying the restatement site level); or C-48
  PARTIAL with multi-level presence but no explicit label.
- Fail: Enforcement content at fewer than three independent hierarchy levels; or content at three+
  levels but restatement is implicit (label absent); or C-48 FAIL subsumes C-50.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 78 -> 84
(42 criteria x PASS=2).

**R17 discrimination under v17 (uncapped aspirational tiebreak; all composite = 100/100):**

| Rank | Variation | C-48 | C-49 | C-50 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 (tie) | **V-01** | PASS | PASS | PASS | 84/84 |
| 1 (tie) | **V-02** | PASS | PASS | PASS | 84/84 |
| 1 (tie) | **V-03** | PASS | PASS | PASS | 84/84 |
| 1 (tie) | **V-04** | PASS | PASS | PASS | 84/84 |
| 5 | **V-05** | PASS | FAIL | PASS | 82/84 |

Open for R18: C-49 PASS for V-05 (enforcement contract pre-positioning + inline named-label sub-part
reinforcement absent).

---

## v15 summary

Two new criteria extracted from R15 excellence signals:

| Criterion | E-tag | Signal | Cracked by |
|-----------|-------|--------|------------|
| **C-45** -- Gate Independence Completeness Verification Block | E-31 | V-03/V-04/V-05 carry a named block at COMPLETE time enumerating all gate CLOSE blocks eligible for clause independence and confirming each one's status; V-01/V-02 achieve C-42+C-43 via sequential single-gate additions without any meta-verification | V-03, V-04, V-05 |
| **C-46** -- Gap Registry Nil Confirmation Structural Form | E-32 | V-03/V-05 produce nil confirmations in the same three-field form as gap entries (Source: N/A / Missing link: N/A / Consequence: nil -- coverage complete), eliminating the prose-vs-structured asymmetry C-44 left open | V-03, V-05 |

**Scoring delta**: uncapped max 72 → 76 (38 criteria × 2). Cap unchanged at 10.

**R15 discrimination under v15:**

| Rank | Variation | C-45 | C-46 | Uncapped |
|------|-----------|------|------|---------|
| 1 | V-05 | PASS | PASS | **76/76** |
| 2 | V-03 | PASS | PASS | **73/76** |
| 3 | V-04 | PASS | FAIL | **72/76** |
| 4 (tie) | V-01 | FAIL | FAIL | **70/76** |
| 4 (tie) | V-02 | FAIL | FAIL | **70/76** |

The three-way tie at 70 from R15/v14 is broken. V-04 advances to 72 via C-45 PASS. V-01/V-02 stay at 70 — they assembled C-42+C-43 sequentially across rounds and carry no independence completeness block.

**Orthogonality arguments:**
- **C-45** is orthogonal to C-42 and C-43 (those require independence in specific gates; C-45 requires a meta-artifact proving all eligible gates were swept), to C-28 (rule invocation audit), and to C-23 (scope declaration bracket). It also functions as an upward compatibility guard: any future gate with multi-clause CLOSE content will be missing from the completeness block, making the gap immediately detectable.
- **C-46** is orthogonal to C-44 (which requires a nil confirmation to exist; C-46 requires it to use three-field form). The distinction matters for uniform scanability: prose nils force mode-switching when scanning registry Source fields; three-field nils don't.
r targets across rounds, with no
  artifact confirming that other eligible gates were not overlooked. V-01 added Gate 2b independence
  in R13 and Gate 1 independence in R15 -- the sequential additions reveal that each gate was
  targeted in isolation rather than as part of a completeness sweep. V-03/V-04/V-05 carry an
  independence completeness block that closes the sweep, making the scope independently auditable.
  C-45 is also orthogonal to C-23 (scope declaration closure bracket, which tracks commerce
  operation coverage) and C-28 (post-analysis rule registry audit, which tracks rule invocations):
  C-45 tracks gate CLOSE clause independence coverage across all eligible gates. The completeness
  block also serves as an upward compatibility guard: when a future round adds a gate with
  multi-clause CLOSE content, its absence from the completeness block is immediately detectable.
- **C-46** is orthogonal to C-44 -- C-44 requires a nil confirmation when a registry direction has
  no uncovered entries, and requires gap entries to use three-field form (Source / Missing link /
  Consequence). C-46 requires the nil confirmation itself to use the same three-field schema as gap
  entries. A prose nil ("GAP REGISTRY: no uncovered entries") satisfies C-44 but is structurally
  asymmetric with gap entries: a reviewer scanning registry Source fields encounters either a gap
  identifier (three-field entry) or a prose nil line (unstructured), requiring mode-switching.
  A three-field nil eliminates the asymmetry: the nil state becomes a typed registry row rather
  than a prose annotation. Registry scanning becomes fully uniform -- a Source-field scan yields
  either a gap artifact identifier or a typed N/A nil marker, with no structural mode difference.
  The three-field nil also makes the "no gaps" assertion independently auditable across three
  dimensions (Source, Missing link, Consequence) rather than as a single prose statement.

**C-45 -- Gate Independence Completeness Verification Block (E-31)**
- Signal: V-03 in R15 achieves C-42 + C-43 simultaneously and carries an explicit named
  independence completeness block at COMPLETE time: "INDEPENDENCE AUDIT: Gate 2b CLOSE --
  two-checkbox independent form (C-42: confirmed). Gate 1 CLOSE -- two-checkbox independent form
  (C-43: confirmed). No further gate CLOSE blocks in this template carry both a positive
  confirmation clause and a prohibition clause. Independence scope: COMPLETE." V-04 and V-05 carry
  the same pattern from R13. V-01's R15 axis appended C-43 to Gate 1 CLOSE and does not include
  an independence scope audit. V-02's R15 axis appended C-42 to Gate 2b CLOSE and does not include
  an independence scope audit.
- The gap it closes: C-42 and C-43 each require independence in specific named gates. Neither
  criterion ensures that every other eligible gate CLOSE block has been considered. When
  independence is added gate-by-gate across rounds, no artifact confirms that the reviewer
  identified all eligible gates -- only that the two named gates were addressed. A completeness
  verification block closes this gap by enumerating every gate CLOSE block in the template,
  classifying each as eligible (positive + prohibition clauses present) or ineligible (single clause
  type), and confirming the independence status of each eligible gate. It also serves as an upward
  compatibility guard: when a future round adds a gate with multi-clause CLOSE content, its absence
  from the completeness block is immediately detectable, triggering a C-45 failure that prompts an
  update.
- Pass requires: A named post-analysis or COMPLETE-time block that (1) enumerates all gate CLOSE
  blocks in the template by gate identifier, (2) classifies each as eligible or ineligible for the
  independence pattern, (3) confirms the independence status (independent form or combined form)
  of each eligible gate, and (4) declares the independence scope COMPLETE. The block must be a
  named labeled section or audit item -- not a prose paragraph asserting completeness without
  enumeration. Each gate must be listed by its identifier. When only Gate 2b CLOSE and Gate 1
  CLOSE are eligible, the block must explicitly confirm that no other gate CLOSE blocks in the
  template carry multi-clause content.
- Partial: Independence completeness block present but does not enumerate gates by identifier (only
  asserts "all gates verified" without listing them); or block enumerates the C-42 and C-43 gates
  but omits the explicit "no other eligible gates" confirmation; or completeness verification
  embedded within a gate CLOSE block rather than as a distinct post-analysis artifact; or block
  present but covers only one of the two targeted gates.
- Fail: No independence completeness verification block; C-42 and C-43 individually satisfied but
  no artifact confirms that all eligible gate CLOSE blocks were identified and audited; or C-42
  FAIL subsumes C-45 (no structural independence exists to complete); or completeness claim present
  only in prose preamble without a named verification block.

**C-46 -- Gap Registry Nil Confirmation Structural Form (E-32)**
- Signal: V-05 (C-44 champion from R13) and V-03 (R15, maintaining C-44 PASS) produce three-field
  nil entries when a registry direction has no uncovered entries:
  `Source: N/A -- all chaos scenarios are fully linked to >= 1 Observable Signal |
   Missing link: N/A -- no dark chaos scenarios in this direction |
   Consequence: nil -- PART A bidirectional coverage complete`
  V-04 lacks the registry (C-44 FAIL); V-01/V-02 lack the registry.
- The gap it closes: C-44 requires a nil confirmation ("GAP REGISTRY: no uncovered entries")
  when a registry direction has no gaps, closing the ambiguity that inline absence creates. A prose
  nil satisfies this C-44 requirement. However, the prose form is structurally asymmetric with gap
  entries: a registry producing three-field gap entries in one direction but a prose nil in another
  is not uniformly scannable. A reviewer processing registry entries must change parsing mode when
  encountering a prose nil, and cannot apply the same Source-field scan to determine coverage state.
  The three-field nil closes this asymmetry: nil entries use the same schema as gap entries, with
  Source explicitly stating "N/A -- all entries covered", Making link N/A, and Consequence stating
  "nil -- coverage complete." The registry is then fully uniform: scanning Source fields yields
  either a gap identifier or a typed N/A nil marker, with no mode-switching required.
- Pass requires: Each registry section (PART A and PART B, or equivalent named registry sections)
  that has no uncovered entries carries a nil confirmation as a three-field registry entry with
  Source, Missing link, and Consequence fields each explicitly populated with nil content. The nil
  entry must be positioned as a registry row, not as a prose paragraph adjacent to the registry.
  The Source field must use an N/A marker or typed nil indicator (not blank). Both registry
  directions must satisfy this criterion independently; a three-field nil in PART A alongside a
  prose nil in PART B satisfies PARTIAL only. When a direction has at least one actual gap entry,
  no nil entry is required for that direction. C-44 FAIL subsumes C-46.
- Partial: Three-field nil entry present in one registry direction but the other uses a prose nil;
  or three-field nil present but one or more fields are blank rather than explicitly nil-populated;
  or nil entry structured as a row but Source field carries only a prose statement without a typed
  N/A marker; or C-44 PARTIAL (registry present for one direction) with three-field nil in the
  present direction but prose nil implied for the absent direction.
- Fail: Nil confirmations in both registry directions are prose-only; or nil confirmations absent
  in a direction with no gap entries (C-44 nil-confirmation failure); or C-44 FAIL subsumes C-46.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 72 -> 76
(38 criteria x PASS=2).

**R15 discrimination under v15 (uncapped aspirational tiebreak; all composite = 100/100):**

| Rank | Variation | C-45 | C-46 | Uncapped Asp. |
|------|-----------|------|------|--------------|
| 1 | **V-05** | PASS | PASS | 76/76 |
| 2 | **V-03** | PASS | PASS | 73/76 |
| 3 | **V-04** | PASS | FAIL | 72/76 |
| 4 (tie) | **V-01** | FAIL | FAIL | 70/76 |
| 4 (tie) | **V-02** | FAIL | FAIL | 70/76 |

Open for R16: C-44 PASS for V-01/V-02/V-04 (inline gap notation; formal registry absent);
C-45 PASS for V-01/V-02 (completeness block absent -- sequential gate additions without
completeness sweep); C-46 follows C-44 for V-01/V-02/V-04 once registry structure is present.
V-05 achieves 76/76 -- new perfect uncapped ceiling. V-03 at 73/76 is the new runner-up; V-04
at 72/76 advances past V-01/V-02 via C-45 PASS.

---

## v14 summary

Three new criteria extracted from R13 excellence signals:

| Criterion | E-tag | Signal | Cracked by |
|-----------|-------|--------|------------|
| **C-42** -- Gate-Close Clause Structural Independence | E-28 | V-01/V-04/V-05 split Gate 2b CLOSE into TWO independent checkboxes; V-02/V-03 use combined form (satisfies C-40 but conflates two audit points) | V-01, V-04, V-05 |
| **C-43** -- Impossibility Argument Basis Clause Independence | E-29 | V-02/V-04/V-05 split Gate 1 CLOSE into TWO independent checkboxes (required-basis:present + prohibited-basis:absent); V-01 uses combined statement (satisfies C-41 but not C-43) | V-02, V-04, V-05 |
| **C-44** -- Bidirectional Gap Registry Artifact Structure | E-30 | V-03/V-05 formal PART A + PART B GAP REGISTRY with three-field entries (Source / Missing link / Consequence); V-01/V-02/V-04 use inline gap notation (satisfies C-38 but not C-44) | V-03, V-05 |

**Scoring delta**: uncapped max 66 -> 72 (36 criteria x 2). Cap unchanged at 10.

**R13 discrimination under v14:**

| Rank | Variation | C-42 | C-43 | C-44 | Uncapped |
|------|-----------|------|------|------|---------|
| 1 | V-05 | PASS | PASS | PASS | **72/72** |
| 2 | V-04 | PASS | PASS | FAIL | **70/72** |
| 3 | V-01 | PASS | FAIL | FAIL | **68/72** |
| 4 | V-02 | FAIL | PASS | FAIL | **67/72** |
| 5 | V-03 | FAIL | FAIL | PASS | **65/72** |

**Design rationale highlights:**
- **C-42** is orthogonal to C-40 -- C-40 requires both a positive clause and a prohibition clause
  in the CLOSE block; C-42 requires those clauses to be STRUCTURALLY INDEPENDENT items. A combined
  form satisfies C-40 but fails C-42: when the combined item is disputed, a reviewer cannot
  determine from the CLOSE block alone whether the positive assertion failed, the prohibition
  failed, or both. Separate checkboxes (V-01/V-04/V-05) make each clause independently falsifiable.
  V-02/V-03's combined form "(identity assertion satisfied -- no paraphrase, no independent
  calibration)" passes C-40 but fails C-42.
- **C-43** is orthogonal to C-41 -- C-41 requires the Gate 1 CLOSE postcondition to name required
  basis AND prohibited basis; C-43 requires those checks to be STRUCTURALLY INDEPENDENT items.
  V-01's combined statement "(architecture basis, not description absence)" satisfies C-41 but
  fails C-43: the required-basis check and the prohibited-basis check are evaluated together.
  V-02/V-04/V-05's two-checkbox form evaluates each independently. This matters when an argument
  cites an architecture basis but also includes a supplementary description-absence component --
  the combined check may pass while the prohibition is partially violated.
- **C-44** is orthogonal to C-38 -- C-38 requires the bidirectional matrix to emit a named gap
  finding for uncovered entries; C-44 requires each gap finding to be a structured three-field
  artifact in a named registry section. V-01/V-02/V-04's inline notation ("Dark chaos finding:
  CHAOS-OBS-GAP-NN: ...") names the problem but not the consequence -- a reviewer scanning for gap
  severity must read the prose. V-03/V-05's formal PART A/B GAP REGISTRY with Source / Missing
  link / Consequence fields makes each gap's impact independently auditable and queryable. C-38 is
  satisfied by inline notation; C-44 requires the registry structure.

---

## v13 summary

Three new criteria extracted from R12 excellence signals:

| Criterion | E-tag | Signal | Cracked by |
|-----------|-------|--------|------------|
| **C-39** -- Gate-Open Precondition Acknowledgment Checkpoint | E-25 | V-02/V-04 Gate 2b OPEN precondition carries explicit named acknowledgment ("verbatim -- not a derivative") before any row filling begins -- a confirmable checkpoint, not a copy instruction | V-02, V-04, V-05 |
| **C-40** -- Gate-Close Prohibition Clause | E-26 | V-02/V-04 Gate 2b CLOSE adds "no paraphrase, no independent calibration" alongside the positive confirmation -- absence verification orthogonal to presence checking | V-02, V-04 |
| **C-41** -- Impossibility Argument Quality Gate Postcondition | E-27 | V-01/V-05 Gate 1 CLOSE postcondition names both required basis ("architecture basis") AND prohibited basis ("not description absence") in one statement -- quality enforcement at gate-close time, beyond C-15's field+examples presence requirement | V-01, V-05 |

**Scoring delta**: uncapped max 60 -> 66 (33 criteria x 2). Cap unchanged at 10.

**R12 discrimination under v13:**

| Rank | Variation | C-15 | C-36 | C-38 | C-39 | C-40 | C-41 | Uncapped |
|------|-----------|------|------|------|------|------|------|---------|
| 1 | V-05 | PASS | PASS | PASS | PASS | PARTIAL | PASS | **65/66** |
| 2 (tie) | V-02 | PARTIAL | PASS | PARTIAL | PASS | PASS | FAIL | **62/66** |
| 2 (tie) | V-04 | PARTIAL | PASS | PARTIAL | PASS | PASS | FAIL | **62/66** |
| 4 | V-01 | PASS | PARTIAL | PARTIAL | FAIL | FAIL | PASS | **60/66** |
| 5 | V-03 | PARTIAL | PARTIAL | PARTIAL | FAIL | FAIL | FAIL | **57/66** |

---

## v12 summary

Three new aspirational criteria extracted from Round 11 excellence signals:

| Criterion | E-tag | Source | Cracked by |
|-----------|-------|--------|------------|
| **C-36** -- Chaos-Trigger Threshold Identity Assertion | E-22 | V-05: Column Contract explicitly asserts Gate 2b activation boundary = same threshold expression as Trigger Condition -- identity claim, not a reference link | V-05 only |
| **C-37** -- Observable Signal Detection Horizon | E-23 | V-04/V-05: Detection Horizon as third required component of Observable Signal, defining maximum latency window before signal absence is itself a finding | V-04, V-05 |
| **C-38** -- Chaos-Observability Bidirectional Coverage Matrix | E-24 | V-05: Named cross-reference artifact linking every chaos scenario to >= 1 Observable Signal and vice versa -- V-04 has both C-09 and C-10 outputs but no bridging matrix | V-05 only |

**Scoring delta**: aspirational cap unchanged at 10; uncapped max 54 -> 60 (30 criteria x 2).

**R11 discrimination under v12** (all composites 100/100; tiebreak by uncapped aspirational):

| Rank | Variation | C-36 | C-37 | C-38 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 | **V-05** | PASS | PASS | PASS | 59/60 |
| 2 | **V-04** | PARTIAL | PASS | FAIL | 56/60 |
| 3 | **V-03** | PARTIAL | FAIL | FAIL | 54/60 |
| 4 | **V-01** | PARTIAL | FAIL | FAIL | 52/60 |
| 5 | **V-02** | FAIL | FAIL | FAIL | 51/60 |

---

## v11 changes from v10

Three new aspirational criteria added from Round 10 excellence signals:

**C-33 -- Intra-Row Column-Group Phase Gate**
- Signal: V-01/V-04/V-05's "C-phase complete before D-phase begins" advance-inhibitor embedded in
  each row descriptor.
- The gap it closes: row-level gate fires after the row is complete; column-group gate fires before
  D-phase begins within the row -- closes mid-row omission risk.
- Pass requires all elements: named column ownership phases / advance-inhibitor at row descriptor
  level / non-placeholder check for all C-phase cells before D-phase begins.

**C-34 -- Trigger Condition Column: Threshold Expression + Detection Signal**
- Signal: V-02/V-05's Trigger Condition column requiring both a quantified activation threshold
  and a named detection signal (the observable mechanism confirming threshold crossing).
- The gap it closes: the scenario's activation boundary must be operationalizable for alerting from
  column scan alone. A qualitative trigger description cannot be wired to an alert system; a
  threshold expression without a detection signal cannot confirm when the threshold is crossed in
  production. Both components are independently load-bearing.
- Pass requires: dedicated Trigger Condition column with Fill Requirement naming both components;
  at least one row fills both with non-generic content.

**C-35 -- Three-Component Recovery Stage Specification**
- Signal: V-03/V-04/V-05's Recovery Path column extension to three required components per stage:
  mechanism + SLA target + Verification Signal (VS).
- The gap it closes: C-07 requires actor-labeled recovery steps; C-35 requires each stage to be
  independently falsifiable -- the stage is complete when the named observable appears, not when
  the SLA timer expires.
- Pass requires: all three components (mechanism, SLA target, named VS) explicitly required for
  each of the four stages; VS must be named, observable, and distinct from the mechanism.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 48 -> 54
(27 criteria x PASS=2).

**R10 discrimination under v11 (uncapped aspirational tiebreak; all composite = 100/100):**

| Rank | Variation | C-33 | C-34 | C-35 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 | **V-05** | PASS | PASS | PASS | 50/54 |
| 2 | **V-04** | PASS | FAIL | PASS | 47/54 |
| 3 | **V-01** | PASS | FAIL | FAIL | 46/54 |
| 4 (tie) | V-02 | FAIL | PASS | FAIL | 45/54 |
| 4 (tie) | V-03 | FAIL | FAIL | PASS | 45/54 |

---

## v10 changes from v9

Two new aspirational criteria extracted from Round 9 excellence signals:

**C-31 -- Pre-Analysis Bypass Chain Declaration**
- Signal: V-01's named "Bypass Gate-Reopening Protocol" section declared *before Gate 1*, not
  reactively when a bypass is first detected.
- The gap it closes: C-29 requires the bypass chain to execute correctly; C-31 requires the
  chain's structure to be declared upfront -- analogous to C-21.
- Pass requires all four elements: numbered remediation steps / amendment sub-gate convention /
  authorized actors / COMPLETE-blocking statement.

**C-32 -- Bypass-Trigger Column Scanability**
- Signal: V-02/V-05's BYPASS-TRIGGER column in the registry audit table -- each cell must be a
  trigger citation or explicit N/A/SCENARIO-ABSENT, never blank.
- The gap it closes: C-28 requires invocation completeness in prose; C-32 requires bypass
  detection to be column-scannable independent of prose traversal.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 44 -> 48
(24 criteria x 2).

---

## Essential Criteria (must pass all -- 60% of score)

### C-01 -- Scenario Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three resilience scenario classes: (1) full connectivity loss
  (client offline), (2) partial failure (dependent service unavailable), and (3) concurrent writes
  across a partition (split-brain / eventual-consistency conflict).
- **Pass condition**: All three classes are represented by distinct named scenarios. A single
  scenario that attempts to cover all three classes fails. Scenarios that collapse class 2 and
  class 3 into a single "network issue" fail.

### C-02 -- Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: structure
- **Text**: Every failure scenario includes all four required fields: (1) state -- what the system
  state is when failure occurs; (2) capability -- what the user can still do; (3) data at risk --
  what data may be lost, stale, or inconsistent; (4) recovery path -- how the system returns to a
  healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with non-trivial
  content (not placeholder, "N/A", or a single word). A scenario missing any field fails this
  criterion entirely.

### C-03 -- Gap Identification (Three Types)
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data consistency
  violation, and at least one missing recovery flow as distinct named findings. These are the three
  explicit output targets the skill defines.
- **Pass condition**: All three finding types appear, each labeled and actionable -- not merely
  implied or bundled. Generic statements like "offline support may be limited" without specificity
  fail.

### C-04 -- Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals. CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly wherever referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated
  error codes, invented protocols, or impossible consistency guarantees (e.g., strong consistency
  with no latency cost across a partition) fail this criterion.

### C-05 -- Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure scenarios
  reference realistic commerce flows -- checkout, inventory reservation, payment processing, order
  fulfillment, cart state -- rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation by
  name. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality -- 30% of score)

### C-06 -- Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded / impaired /
  down) and a blast radius describing what fraction or segment of users is affected. These labels
  enable triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a blast-radius
  estimate or qualifier (e.g., "affects all users in offline mode", "affects <1% under
  split-brain"). Scenarios with severity but no blast radius, or vice versa, do not satisfy this
  criterion.

### C-07 -- Recovery Path Specificity with Actor Labels
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors -- not just outcomes. Each
  step names who or what initiates the action: client, server, operator, or user. Example: "Client
  retries with exponential back-off up to 5 attempts; on exhaustion, server surfaces a manual
  reconcile UI to the user."
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that describe
  only the end state ("system recovers", "data is synchronized") without mechanism fail.

### C-08 -- Conflict Resolution Strategy for Eventual Consistency
- **Weight**: recommended
- **Category**: coverage
- **Text**: For eventual-consistency scenarios, the output specifies what conflict resolution
  strategy is assumed (last-write-wins, merge, manual reconcile, reject-stale) and flags whether
  that strategy is adequate for the data type involved (e.g., LWW is inadequate for inventory
  counts).
- **Pass condition**: At least one eventual-consistency scenario names a conflict-resolution
  strategy and includes a brief adequacy judgment. Scenarios that describe lag or divergence
  without naming a resolution strategy fail.

---

## Aspirational Criteria (raise the bar -- 10% of score)

**Scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Aspirational band capped at 10.
Uncapped maximum across 42 criteria is 84; the cap rewards breadth while holding the composite
ceiling at 100.

### C-09 -- Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that could be
  scheduled in a test harness. Each scenario specifies: (1) what to inject (network partition,
  latency spike, service kill, packet loss), (2) expected observable behavior, and (3) a binary
  pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements.
  Vague suggestions to "test resilience" or "add chaos testing" without specifics fail.
- **Partial**: Chaos scenario present but missing one of the three required elements.
- **Fail**: No chaos engineering content, or suggestions without runnable specifics.

### C-10 -- Observability Hooks Tied to Named Gaps
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals -- metrics, logs, traces, or
  alerts -- that would surface each identified gap in production. Each recommendation is tied to a
  specific named gap or scenario from the analysis with a rationale.
- **Pass condition**: At least two observability recommendations are present, each linked to a
  named gap or scenario with a rationale for why that signal would detect the failure early.
  Generic "add monitoring" suggestions without specifics fail.
- **Partial**: Observability recommendations present but fewer than two are tied to named gaps
  with rationale.
- **Fail**: No observability content, or generic recommendations without gap linkage.

### C-11 -- Confidence-Annotated Discovery Catalog
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The distributed-systems analysis phase carries explicit confidence ratings (high /
  medium / low / impossible) for each failure mode before scenarios are committed to the output.
  Each rating cites its basis -- an architecture constraint or DS theory reference -- not just a
  label. Entries rated "impossible" are excluded from the scenario table but retained in the
  discovery phase with their rationale. Entries rated "low confidence" are barred from the scenario
  table until the confidence basis is resolved; flagging alone does not satisfy this gate. This
  triage gate prevents technically invalid scenarios from polluting the output and makes the
  discovery phase independently auditable. (Signal: V-01, V-04.)
- **Pass condition**: Every failure mode in the discovery phase carries a confidence rating with a
  cited basis; "impossible" entries are excluded from the table with retained rationale;
  "low confidence" entries are barred from the table until resolved -- not merely flagged.
- **Partial**: Confidence ratings present on some entries but not all; or impossible entries
  excluded without cited basis; or low-confidence entries flagged but not gated.
- **Fail**: No confidence annotation on discovery-phase entries; impossible scenarios enter the
  output without challenge.

### C-12 -- Nil-Finding Norm for Gap Sections
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Each of the three typed gap sections (offline experience gaps / data consistency
  violations / missing recovery flows) includes an explicit nil finding when no gaps of that type
  are identified for the given topology or load pattern. A nil finding reads as: "No
  offline-experience gaps identified for this deployment pattern -- all critical paths include
  local-fallback state." The nil finding includes a scope rationale explaining why the gap type
  does not apply; a bare "none found" statement does not satisfy this criterion. Silence is not a
  valid nil finding. (Signal: V-01, V-02, V-03.)
- **Pass condition**: All three gap sections are explicitly present; sections with no findings
  carry a labeled nil finding that includes a brief scope rationale explaining why the gap type
  does not apply for this deployment pattern.
- **Partial**: Some nil findings present but not all three sections covered, or nil findings appear
  without scope rationale (bare "none found" statement).
- **Fail**: Missing gap sections are silently absent; reader cannot distinguish "no gaps found"
  from "gaps not analyzed."

### C-13 -- Coverage Accountability Roster
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output opens with a pre-analysis roster that commits to minimum per-class coverage
  -- at least two scenarios per degradation class -- before scenario analysis begins. The roster is
  checkable: the reader can verify class coverage against the final scenario list without reading
  the full analysis. When a class slot cannot be filled, the output provides an explicit
  impossibility argument or reclassification -- it does not silently reduce coverage below the
  committed minimum. The challenge mechanism ("why can't you fill this slot?") is answered inline,
  not omitted. (Signal: V-03, V-05.)
- **Pass condition**: Pre-analysis roster is present and commits to >=2 scenarios per class; all
  committed slots are filled or explicitly argued impossible / reclassified; roster is independently
  checkable against the final scenario list.
- **Partial**: Roster present but commits to fewer than 2 per class without argument; or roster
  absent but coverage gaps are argued inline rather than silently dropped.
- **Fail**: No coverage accountability mechanism; degradation-class gaps are silently absent.

### C-14 -- Conflict-Resolution Adequacy as DCV Source
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When conflict-resolution analysis judges a strategy to be inadequate or undefined for a
  given data type, that judgment is explicitly fed back into the data-consistency-violation (DCV)
  gap section as a named DCV finding. The conflict-resolution section and the gap identification
  section are bidirectionally linked -- an inadequate or undefined strategy is always a DCV, not a
  standalone note. This prevents conflict-resolution weaknesses from being isolated in one section
  and invisible to the gap tally. When all strategies are adequate, an explicit CLOSED confirmation
  is written. (Signal: V-02, V-04 -- "inadequate/undefined -> DCV" pattern.)
- **Pass condition**: At least one conflict-resolution adequacy judgment of "inadequate" or
  "undefined" generates an explicit, named DCV entry in the gap identification section. The linkage
  is visible: the DCV entry references the conflict-resolution finding that produced it. When no
  inadequate strategies exist, an explicit CLOSED confirmation is present.
- **Partial**: Inadequate strategies noted in conflict-resolution analysis but not linked to a named
  DCV finding in the gap section; or a DCV entry is present without tracing back to its
  conflict-resolution source.
- **Fail**: Conflict-resolution analysis and gap sections are independent silos with no
  cross-referencing; inadequate strategies do not produce DCV entries.

### C-15 -- DS-Primitive-Grounded Impossibility Arguments
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a coverage slot in the accountability roster cannot be filled, the impossibility
  argument cites a specific distributed systems primitive -- a named CAP theorem guarantee, a
  deployment topology constraint, or a synchronous consistency guarantee that forecloses the
  failure class. Topic-scope arguments ("the topic doesn't mention caching", "the system
  description is too simple for this class") are not valid impossibility arguments. The argument
  must address the architecture, not the description. The template includes a named "DS Primitive
  cited:" field with inline VALID / INVALID annotated examples so that the distinction between an
  architecture argument and description absence is unambiguous. (Signal: V-03 Round 2; V-02
  Round 3.)
- **Pass condition**: Every impossibility argument cites a specific DS primitive via a named "DS
  Primitive cited:" field with an architecture basis. Inline VALID/INVALID annotated examples are
  present in the template. No topic-scope arguments appear; any argument invoking description
  absence rather than architecture constraint fails.
- **Partial**: Some impossibility arguments cite DS primitives but others rely on topic scope or
  description absence; or DS primitive field is present but lacks inline VALID/INVALID examples.
- **Fail**: Impossibility arguments rely solely on topic scope or description absence; no DS
  primitive is cited; or the challenge mechanism is absent entirely.

### C-16 -- Named Gate-State Vocabulary
- **Weight**: aspirational
- **Category**: format
- **Text**: The confidence triage and gap sections use a fixed, named disposition vocabulary --
  entries are assigned exactly one of: Include / BARRED / Argued-Impossible (or equivalent named
  states). Free-text confidence descriptions that do not resolve to one of these named dispositions
  are not valid. Each gate section carries an explicit binary OPEN / CLOSED declaration visible
  without reading the prose. "Flagged" and similar qualitative labels that do not resolve to a
  named disposition are rejected -- a gate section without a named OPEN/CLOSED state is treated as
  OPEN by definition. A gate cannot close while any entry in that section carries an unresolved
  disposition. (Signal: V-02 C-11; V-03 C-11.)
- **Pass condition**: Every entry in the discovery/triage phase carries one of the named
  dispositions; each gate section displays an explicit OPEN/CLOSED state; no free-text confidence
  label is used as a substitute for a named disposition.
- **Partial**: Named dispositions used for most but not all entries; or OPEN/CLOSED gate states
  present for some sections but not all.
- **Fail**: Discovery entries use free-text confidence descriptions without named dispositions; no
  gate sections carry an explicit OPEN/CLOSED state.

### C-17 -- Permanently Barred Entries as Named Coverage Gaps
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Discovery entries that remain BARRED after the confidence triage gate closes -- where
  the low-confidence basis was never resolved -- are not silently dropped from the output. They are
  recorded as named coverage gaps in the coverage accountability register, distinguishing "analyzed,
  barred, recorded" from "not analyzed." An unresolved BARRED entry that produces no downstream
  artifact is invisible to the reader; "analyzed and excluded for architectural reasons"
  (Argued-Impossible) and "analyzed but confidence never confirmed" (permanently BARRED) are not
  equivalent and must not be conflated. (Signal: V-02 C-11.)
- **Pass condition**: Any entry that is BARRED at the close of the triage gate and whose confidence
  basis was never resolved appears as a named coverage gap in the accountability register. No BARRED
  entry silently disappears from the analysis trace.
- **Partial**: Permanently barred entries noted in prose as unresolved but not formally recorded as
  named coverage gaps in the accountability register.
- **Fail**: BARRED entries with unresolved bases are silently dropped; the reader cannot determine
  whether low-confidence failure modes were excluded intentionally or omitted.

### C-18 -- Explicit Phase Entry and Exit Conditions
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Each analysis phase or gate section specifies (1) its entry condition -- which prior
  gates must be CLOSED before this phase begins, referenced by gate identifier -- and (2) its exit
  condition -- what must be true for this gate to be declared CLOSED, stated explicitly. Phases
  that begin or end without stated conditions are implicitly sequential-by-position, which is
  unverifiable. Silence does not mean CLOSED; an explicit CLOSED confirmation is required. This
  prevents phases from running out of order and makes the analysis closure independently auditable.
  (Signal: V-03 C-14.)
- **Pass condition**: At least two phases carry named entry conditions (citing prior gate
  identifiers) and named exit conditions; each of those phases closes with an explicit CLOSED
  confirmation statement.
- **Partial**: Entry or exit conditions present on some phases but not all; or conditions stated
  but without gate-identifier references; or no explicit CLOSED confirmations.
- **Fail**: No phase carries stated entry/exit conditions; phases are ordered by prose position
  only; closure is inferred, not declared.

### C-19 -- Gate Blockage Transparency (Reason-if-OPEN)
- **Weight**: aspirational
- **Category**: format
- **Text**: When a gate is in OPEN state -- not yet closed -- the blocking reason is declared
  inline as a named "Reason if OPEN:" field or equivalent. An OPEN gate with no stated reason is
  indistinguishable from a gate that was never evaluated or was abandoned mid-analysis. The reason
  field must name the specific blocking condition: the unresolved entry ID, the unmet coverage
  minimum, the pending adequacy verdict, or the outstanding amendment. This allows the analysis to
  be resumed deterministically once the blocking condition is resolved, without re-reading all
  prior gate prose. A gate displaying only "OPEN" without a blocking reason is treated as an error,
  not as a valid in-progress state. (Signal: V-03 Round 4 C-18.)
- **Pass condition**: Every gate that appears in OPEN state carries an explicit "Reason if OPEN:"
  field identifying the specific blocking condition. CLOSED gates do not require a reason field.
  Any OPEN gate lacking a stated reason fails this criterion.
- **Partial**: Some OPEN gates carry stated blocking reasons but not all; or blocking reason
  present but identifies only a category ("unresolved entry") without naming the specific blocking
  item.
- **Fail**: OPEN gates carry no stated reason; or all OPEN gates are declared without
  distinguishing the blocking condition from a routine in-progress state.

### C-20 -- Downstream Gate Amendment with Re-Close Record
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a downstream finding invalidates the output of an already-CLOSED gate (e.g., a
  conflict-resolution adequacy failure requires an additional DCV entry that the prior DCV gate was
  closed without), the prior gate is explicitly re-opened, the amendment is applied, and the gate
  is re-closed under a labeled amendment sub-gate (e.g., "GATE 3b: AMENDED"). The amendment record
  names the downstream finding that triggered the reopening. Late amendments silently appended to a
  closed section are unverifiable and break the gate audit trail. A re-opened gate whose amendment
  is applied without a labeled re-close record is treated as still OPEN. (Signal: V-03 Round 4
  C-14.)
- **Pass condition**: At least one downstream finding that requires an amendment to a prior CLOSED
  gate triggers an explicit re-open, applies the amendment, and re-closes the gate under a labeled
  sub-gate identifier. The amendment record references the downstream finding by ID. When no
  downstream findings require amendments, an explicit confirmation is present.
- **Partial**: Late amendment applied to a prior closed gate section but without a labeled re-open
  / re-close record; or sub-gate label present but the downstream finding that triggered it is not
  referenced.
- **Fail**: Downstream findings that invalidate prior gate outputs are silently appended without
  re-opening the gate; or no mechanism exists for downstream findings to amend prior gate sections;
  or the gate audit trail has no sub-gate amendment records.

### C-21 -- Pre-Analysis Commerce Operation Scope Declaration
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Before scenario analysis begins, the output commits to a named, exhaustive list of
  commerce operations that will be analyzed. The declaration names every operation in scope (e.g.,
  checkout, inventory reservation, payment processing, cart state, order fulfillment, loyalty
  redemption). This commitment is checkable against the final scenario table: any declared operation
  that receives no scenario coverage is a named gap, not a silent omission. Operations excluded
  from the declaration are either explicitly out-of-scope with a stated reason or their absence is
  a coverage gap. C-05 requires scenarios to be anchored to named operations; C-21 requires the
  scope commitment to precede the analysis, not emerge from it. (Signal: V-05 Round 4 C-05.)
- **Pass condition**: A named commerce operation scope list is present before the first scenario
  entry. The list covers at least four distinct operations. The final scenario table provides
  coverage for each declared operation or explicitly records it as a gap. Operations mentioned only
  within scenario bodies (not declared upfront) do not satisfy this criterion.
- **Partial**: Upfront scope declaration present but covers fewer than four operations; or
  declaration present but final coverage is not cross-checked against the declared list; or
  operations appear only in a post-hoc summary, not a pre-analysis commitment.
- **Fail**: No upfront commerce operation scope declaration; the set of covered operations is
  inferred from the scenario table only; coverage gaps are not distinguishable from scope
  exclusions.

### C-22 -- Typed Nil-Finding Identifiers
- **Weight**: aspirational
- **Category**: format
- **Text**: Nil findings carry gap-type prefix identifiers -- OEG-NIL (offline experience gap),
  DCV-NIL (data consistency violation), MRF-NIL (missing recovery flow) -- that bind each nil
  statement to its gap category by name. C-12 requires nil findings with scope rationale; C-22
  requires those nil findings to be addressable by type. A nil statement without a typed identifier
  satisfies C-12 but cannot be audited, queried, or cross-referenced by gap type. Each typed nil
  identifier is unique within an analysis run; if the same gap type produces a nil in multiple
  phases, each carries its own identifier (OEG-NIL-1, OEG-NIL-2). (Signal: V-01 Round 5 C-12
  PASS evidence.)
- **Pass condition**: Every nil finding carries a typed prefix identifier (OEG-NIL, DCV-NIL,
  MRF-NIL, or equivalent named type prefix). Each identifier is unique within the run. Nil
  statements without a typed identifier fail this criterion regardless of rationale quality.
- **Partial**: Typed identifiers present on some nil findings but not all; or typed prefix used
  but not consistently bound to the gap type.
- **Fail**: No typed nil-finding identifiers; nil statements use only prose headings or bare "none
  found" / "N/A" markers; nil findings are not queryable by gap type.

### C-23 -- Scope Declaration Closure Bracket
- **Weight**: aspirational
- **Category**: format
- **Text**: The pre-analysis commerce operation scope declaration (C-21) is bracketed by two named
  boundary blocks: an opening `SCOPE DECLARATION COMPLETE` confirmation that closes the declaration
  phase before analysis begins, and a terminal `Scope Verification` block that cross-checks the
  declared operation list against the final scenario table after analysis concludes. The terminal
  Scope Verification block must name each declared operation and its coverage outcome (covered / gap
  / out-of-scope). A scope declaration that opens but never formally closes is treated as
  unverified. (Signal: V-01 Round 5 C-21 PASS evidence.)
- **Pass condition**: An opening `SCOPE DECLARATION COMPLETE` block (or named equivalent) is
  present immediately after the operation list, before the first analysis phase. A terminal `Scope
  Verification` block (or named equivalent) is present after the final analysis phase, naming each
  declared operation with its coverage outcome. Both blocks are required; a declaration with only
  one does not satisfy this criterion.
- **Partial**: Opening declaration confirmation present but no terminal verification block; or
  terminal block present but coverage outcomes are not named per declared operation.
- **Fail**: No named boundary blocks; scope declaration embedded in prose with no opening
  confirmation; terminal cross-check absent or inferred from scenario table without a named block.

### C-24 -- Template-Embedded Conditional Linkage Rules
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-section linkages that are required by the skill's logic are encoded in the
  template as explicit named conditional rules -- `if [condition]: [action]` -- rather than
  described in prose instructions or left to analyst discretion. The canonical example is the DCV
  linkage from conflict-resolution adequacy: rather than instructing the analyst to "link inadequate
  strategies to DCV findings," the template contains a named rule: `if verdict is [no | undefined]:
  append DCV-CR-NN`. This makes correct cross-section behavior mandatory and machine-checkable.
  C-14 requires the DCV linkage to exist; C-24 requires it to be encoded as a named conditional
  rule. At least two distinct conditional linkage rules must be present to demonstrate that the
  pattern is systemic, not incidental. (Signal: V-01 Round 5 C-14 PASS evidence.)
- **Pass condition**: At least two named conditional linkage rules are present in the template in
  explicit `if [condition]: [action]` form (or a structurally equivalent named rule block). Each
  rule names both its trigger condition and its cross-section action. Prose instructions that
  describe the same logic without an explicit conditional rule form do not satisfy this criterion.
- **Partial**: One conditional linkage rule present but not two; or rules present in conditional
  form but trigger conditions are underspecified; or rules embedded in prose annotations rather
  than named rule blocks.
- **Fail**: No conditional linkage rules in the template; cross-section linkages are described in
  prose instructions only; correct behavior depends on analyst discretion.

### C-25 -- Nil-Finding Supersession Protocol
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Typed nil-finding identifiers (C-22) have a two-state lifecycle: ACTIVE (nil declared,
  gap type not present) and SUPERSEDED (downstream analysis subsequently identifies a gap in the
  same category). When a downstream phase produces a gap finding that supersedes a previously
  declared nil, the nil identifier is explicitly annotated SUPERSEDED with a cross-reference to the
  finding ID that replaced it (e.g., "OEG-NIL-1: SUPERSEDED by OEG-F-3"). When no nil findings
  are superseded, an explicit "no supersessions" confirmation is present. (Signal: V-01 Round 6
  C-22 PASS evidence.)
- **Pass condition**: At least one nil finding that is superseded by a downstream actual finding
  carries an explicit SUPERSEDED annotation citing the superseding finding ID. When no nil findings
  are superseded during the analysis run, an explicit "no supersessions" confirmation is present.
  A nil ID and a gap finding of the same type coexisting without a SUPERSEDED annotation on the
  nil fails this criterion.
- **Partial**: Supersession notation present on superseded nils but does not cite the superseding
  finding ID; or SUPERSEDED present on some superseded nils but not all; or "no supersessions"
  confirmation absent when no supersessions occur.
- **Fail**: Superseded nil findings carry no SUPERSEDED marker; nil identifiers are treated as
  write-once with no lifecycle tracking.

### C-26 -- Confidence Triage Resolution Sub-Gate
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a BARRED discovery entry has its unresolved confidence basis subsequently
  satisfied during analysis and is upgraded to Include, the upgrade path is recorded under a
  labeled triage resolution sub-gate (e.g., "GATE 1b: RESOLVED"). The resolution sub-gate must
  name: the entry ID being resolved, the confidence basis that was satisfied and how, the new
  Include disposition, and the re-closed triage gate status. When no BARRED entries are resolved
  during analysis, an explicit "no BARRED-to-Include upgrades" confirmation is present. (Signal:
  V-03 Round 6 structural excellence.)
- **Pass condition**: At least one BARRED entry that is resolved to Include during analysis appears
  under a labeled triage resolution sub-gate naming the entry ID, the satisfied basis, and the new
  disposition, with the triage gate re-closed. When no BARRED entries are resolved during analysis,
  an explicit confirmation is present.
- **Partial**: BARRED-to-Include upgrade recorded in prose but without a labeled sub-gate; or
  sub-gate present but does not name the satisfied basis or the entry ID being resolved; or
  confirmation absent when no upgrades occur.
- **Fail**: BARRED entries silently appear in the scenario table as Include with no resolution
  record; no mechanism exists for BARRED entries to be explicitly resolved.

### C-27 -- Named Rule Block Registry
- **Weight**: aspirational
- **Category**: format
- **Text**: The named conditional linkage rules required by C-24 appear in a discrete, named rule
  registry section within the template -- not embedded inline in gate-section prose. Each rule in
  the registry carries a unique identifier (e.g., RULE-CR-DCV, RULE-SCOPE-GAP,
  RULE-NIL-SUPERSEDE) that makes it independently addressable: other gate sections can cite a rule
  by its ID rather than by prose location. A template where rules are correct in form (satisfying
  C-24) but scattered inline through gate prose satisfies C-24 but fails C-27: inline rules are
  not enumerable, not independently auditable, and cannot be cited by ID. (Signal: V-03 Round 6
  structural excellence.)
- **Pass condition**: A named rule registry section is present listing all conditional linkage
  rules. Each rule carries a unique ID, explicit trigger condition, and named cross-section action
  target. Gate sections that invoke linkage behavior cite rules by their registry ID, not by
  restating the conditional logic inline. At least two rules with distinct IDs are present.
- **Partial**: Named rules present and correct in conditional form (satisfying C-24) but embedded
  inline in individual gate sections rather than in a discrete registry; or registry present but
  fewer than two rules carry unique IDs; or rules listed in the registry but gate sections restate
  the conditional logic inline.
- **Fail**: No named rule registry; all conditional linkage rules appear only as inline annotations
  within gate-section prose; the complete rule set cannot be enumerated without reading the full
  template.

### C-28 -- Post-Analysis Rule Registry Audit
- **Weight**: aspirational
- **Category**: correctness
- **Text**: A named rule registry (C-27) is a declaration; a post-analysis registry audit closes
  the loop by confirming which rules were actually invoked during the analysis run. After all
  analysis gates complete, the output includes a named post-analysis audit block that reviews the
  rule registry and reports: (1) which rules fired during the run, citing the specific gate and
  entry that triggered each invocation; (2) how many times each rule fired; and (3) whether any
  registered rules went uninvoked -- and if so, whether the condition was absent from the analysis
  (scenario-absent) or the condition arose but the rule was not applied (rule-bypassed, which is an
  audit failure). (Signal: V-03 Round 7 structural excellence.)
- **Pass condition**: A named post-analysis audit block is present after all analysis gates
  complete. The block lists each registered rule by ID and reports its invocation status: fired
  (with gate and entry citation) or uninvoked (with scenario-absent or rule-bypassed
  classification). At least two registered rules are accounted for. A rule that is invoked but
  whose invocation is not cited by gate and entry fails this criterion.
- **Partial**: Post-analysis review of rule usage present but not as a named, discrete audit block;
  or block present but covers only some registered rules; or invocations listed without citing the
  triggering gate and entry.
- **Fail**: No post-analysis rule audit; the rule registry is treated as a declaration-only
  artifact with no execution verification.

### C-29 -- Rule-Bypass-Triggered Gate Reopening
- **Weight**: aspirational
- **Category**: correctness
- **Text**: C-28 classifies a registered rule as RULE-BYPASSED when its trigger condition arose
  during a gate but the rule was not applied -- an audit failure. C-29 enforces the consequence: a
  RULE-BYPASSED finding is a gate-reopening trigger, not merely a reported deficiency. Before the
  analysis can declare COMPLETE, the affected gate must be explicitly reopened, the bypassed rule
  applied, the gate re-closed under a labeled amendment sub-gate following the C-20 mechanism
  (e.g., "GATE N-bypass: AMENDED"), and the audit entry updated from RULE-BYPASSED to INVOKED.
  C-28 says what the audit reports; C-29 says what a RULE-BYPASSED finding forces. (Signal: V-01
  Round 8 C-28 PASS evidence.)
- **Pass condition**: When the post-analysis audit produces at least one RULE-BYPASSED finding, an
  explicit gate-reopening chain follows: the affected gate is re-opened, the bypassed rule is
  applied, the gate is re-closed under a labeled amendment sub-gate citing the bypass finding ID,
  and the audit entry is updated to INVOKED before COMPLETE is declared. When no RULE-BYPASSED
  conditions exist in the run, an explicit confirmation is present. An analysis that acknowledges
  RULE-BYPASSED and declares COMPLETE without gate remediation fails this criterion.
- **Partial**: RULE-BYPASSED finding acknowledged and gate reopened but no amendment sub-gate
  label present; or gate re-closed without updating the audit entry to INVOKED; or no explicit
  confirmation when the run contains no bypasses.
- **Fail**: RULE-BYPASSED audit findings present with no gate reopening; analysis declares
  COMPLETE with acknowledged bypass failures unresolved.

### C-30 -- Multi-Act Completion Sign-Off
- **Weight**: aspirational
- **Category**: format
- **Text**: When the analysis is structured in two or more distinct named acts (e.g., Act 1 -- DS
  failure mode analysis, Act 2 -- Commerce validation), the completion declaration requires a
  per-act sign-off for each act, not a single monolithic COMPLETE at the end. Each per-act
  sign-off declares: (1) all gates within that act are CLOSED; (2) the act's scope is exhausted;
  and (3) no RULE-BYPASSED conditions remain unresolved within that act. When the analysis is
  single-act, this criterion is scored N/A and treated as PARTIAL for scoring purposes. (Signal:
  V-01 Round 8 C-28 PASS evidence.)
- **Pass condition**: When the analysis has two or more named acts, each act closes with an
  explicit per-act sign-off block declaring all gates within that act CLOSED, scope exhausted, and
  no unresolved RULE-BYPASSED conditions in that act. The terminal COMPLETE then references the
  per-act sign-offs rather than implying gate closure directly. When the analysis is single-act,
  N/A must be explicitly declared.
- **Partial**: Per-act sign-offs present but missing one of the three required elements; or per-act
  sign-off present for some acts but not all; or analysis is single-act and N/A is explicitly
  declared.
- **Fail**: No per-act sign-offs in a multi-act analysis; terminal COMPLETE subsumes all acts
  without per-act gate closure records.

### C-31 -- Pre-Analysis Bypass Chain Declaration
- **Weight**: aspirational
- **Category**: format
- **Text**: The bypass remediation chain required by C-29 is declared as a named pre-analysis
  section before execution begins -- not reactively when a RULE-BYPASSED condition is first
  detected. The pre-analysis section enumerates: (1) the numbered steps of the bypass remediation
  chain (reopen gate, apply bypassed rule, re-close under amendment sub-gate, update audit entry
  to INVOKED); (2) the amendment sub-gate naming convention to be used (e.g., GATE N-bypass:
  AMENDED); (3) the actors authorized to execute each remediation step; and (4) the explicit
  blocking statement that COMPLETE may not be declared while any RULE-BYPASSED entry remains
  unresolved. C-29 requires the bypass chain to execute correctly when triggered; C-31 requires
  the chain's structure to be visible and independently auditable from the outset, before any
  bypass condition arises. (Signal: V-01 Round 9 C-29 PASS evidence.)
- **Pass condition**: A named pre-analysis bypass chain section (or equivalent named block) is
  present before the first analysis gate. The section enumerates the numbered remediation steps,
  names the amendment sub-gate convention, identifies authorized actors, and states the
  COMPLETE-blocking condition explicitly. The section must be pre-analysis (appearing before Gate
  1), not embedded in a terminal block or post-analysis audit.
- **Partial**: Pre-analysis bypass section present but missing one of the four required elements
  (numbered steps / amendment convention / authorized actors / COMPLETE-blocking statement); or
  bypass chain described in preamble prose without a named section block; or section appears
  mid-analysis rather than before Gate 1.
- **Fail**: No pre-analysis bypass chain section; bypass remediation protocol appears only
  reactively at the point of first RULE-BYPASSED detection; the reader cannot verify the
  protocol's structure before encountering its first invocation.

### C-32 -- Bypass-Trigger Column Scanability
- **Weight**: aspirational
- **Category**: format
- **Text**: When the post-analysis registry audit is structured as a table, each registered rule
  carries a dedicated BYPASS-TRIGGER column. The BYPASS-TRIGGER cell for a given rule is either
  (1) non-empty, naming the gate and entry where the rule's trigger condition arose and the rule
  was not applied; or (2) explicitly marked N/A or SCENARIO-ABSENT, confirming that the rule's
  trigger condition never arose during the run. A blank cell is not a valid entry: blank does not
  distinguish "trigger condition never arose" from "trigger condition arose but was not recorded."
  The column enables horizontal scanability: a reader recovers all RULE-BYPASSED entries by
  scanning a single column, without reading gate prose. This is orthogonal to C-28's prose
  completeness requirement. (Signal: V-02/V-05 Round 9 C-29 PASS evidence.)
- **Pass condition**: A BYPASS-TRIGGER column is present in the rule registry audit table. Every
  registered rule's cell in this column is either non-empty (citing gate and entry that triggered
  bypass detection) or explicitly marked N/A / SCENARIO-ABSENT. Blank cells fail this criterion
  regardless of correctness in other columns.
- **Partial**: BYPASS-TRIGGER column present but some cells are blank rather than explicitly
  confirmed N/A or SCENARIO-ABSENT; or column present but entries do not name the specific gate
  and entry that triggered bypass detection; or bypass detection information is presented in a
  separate prose block rather than a dedicated table column.
- **Fail**: No BYPASS-TRIGGER column in the registry audit table; bypass detection requires
  sequential gate-by-gate prose reading; or registry audit is not table-structured and no
  equivalent scannable column mechanism exists.

### C-33 -- Intra-Row Column-Group Phase Gate *(E-19)*
The scenario table columns are partitioned into ownership phases (e.g., C-phase: Commerce Expert
columns such as State and Capability; D-phase: Distributed Systems Expert columns such as Data at
Risk, Recovery Path, Severity, Blast Radius). Within each scenario row, an advance-inhibitor
embedded directly in the row descriptor prevents D-phase column population from beginning until all
C-phase columns in that row carry non-placeholder content. This gate operates at a level below the
slot (row) and above the individual column -- closing the mid-row omission risk that row-level
advance-inhibitors do not address: the row-level gate fires after the row is complete; the
column-group gate fires before D-phase begins within the row. The gate must be embedded in the row
descriptor at slot level or below (not in preamble or a section-level note) to operate during cell
construction. The column-phase labels must be named explicitly; generic "complete all columns
before proceeding" instructions do not satisfy this criterion because they do not name the
within-row ownership boundary as a distinct gate. (Signal: V-01/V-04/V-05 Round 10 -- "C-phase
complete? Do not begin D-phase columns until State and Capability contain non-placeholder content"
embedded in each row descriptor.)

**Pass condition**: The row descriptor for at least one scenario row contains an explicit
column-group phase gate naming the column ownership phases and requiring all C-phase (or equivalent
first-phase) column cells to carry non-placeholder content before any D-phase column cell is begun.
The gate is embedded inside the row descriptor (slot level or below), not positioned above the
table or in a section header. The phase label boundary must be named. Per-row application is
preferred; partial credit applies if the gate appears once as a template instruction for all rows.

**Partial**: Column-group gate semantics present but embedded in preamble or section-level note
rather than a row descriptor; or gate embedded in a row descriptor but uses generic "complete all
columns" language without naming the column-phase boundary; or gate uses named phases but is
applied to only one row in a table where multiple rows require phase-segregated columns.

**Fail**: No intra-row column-group phase gate anywhere in the prompt; within-row ownership
transitions have no advance-inhibitor at column-group granularity; the progression from C-phase to
D-phase columns within a row is ungated.

### C-34 -- Trigger Condition Column: Threshold Expression + Detection Signal *(E-20)*
The scenario table includes a Trigger Condition column (or equivalently named entry-bounding
column) whose Fill Requirement explicitly mandates two distinct components per cell: (1) a threshold
expression -- a quantified activation condition specifying when the scenario becomes active (e.g.,
"inventory count falls below safety-stock threshold", "payment API p99 latency exceeds 500ms"); and
(2) a detection signal -- the named observable mechanism by which the threshold crossing is
confirmed in production (e.g., "inventory-service health probe returns degraded",
"payment-provider timeout counter exceeds N/window"). Together these transform each scenario from a
reactive failure description into a bounded detection specification: the threshold expression
defines the activation boundary; the detection signal defines the monitoring obligation. A reader
can scan the Trigger Condition column and wire an alert for each scenario without reading scenario
prose. A qualitative trigger description ("when the service is unavailable") cannot be
operationalized for alerting; a threshold expression without a detection signal cannot confirm when
the threshold is crossed in production. Both components are independently load-bearing; absence of
either downgrades to PARTIAL. (Signal: V-02/V-05 Round 10 -- Trigger Condition column with
threshold expression + detection signal, making scenarios operationalizable for alerting directly
from column scan.)

**Pass condition**: A Trigger Condition column (or equivalently named entry-bounding column) is
present in the scenario table and its Fill Requirement explicitly names both the threshold
expression component (quantified activation condition) and the detection signal component (named
observable mechanism) as distinct required fields. At least one scenario row descriptor or example
row fills both components with non-generic content. A qualitative trigger description or a
threshold expression without a corresponding detection signal fails.

**Partial**: Trigger Condition column present but Fill Requirement specifies only one of the two
required components; or both components listed as conceptual requirements but row fills or examples
illustrate only one component populated; or Trigger Condition column present as a header without a
Fill Requirement specification of its two-component structure.

**Fail**: No Trigger Condition column (or equivalent entry-bounding column) in the scenario table;
scenarios are bounded only by failure class labels or qualitative descriptions; scenario activation
conditions are not operationalized in column form.

### C-35 -- Three-Component Recovery Stage Specification *(E-21)*
Each of the four Recovery Path lifecycle stages (Detect, Contain, Recover, Validate) carries three
required components in the column specification or row descriptor: (1) mechanism -- the action
taken to advance the stage, with named actor (extending C-07); (2) SLA target -- a named
time-to-[X] commitment paired to the stage (e.g., TTD/Detect, TTC/Contain, TTR/Recover,
TTV/Validate); and (3) Verification Signal (VS) -- a named observable artifact that confirms the
stage is complete independent of SLA elapse (e.g., "inventory-service heartbeat returns 200",
"payment provider ACK logged to audit trail", "dual-write conflict counter resets to 0 for 60s").
The VS makes each stage independently falsifiable: the stage is closed when the named observable
appears, not when the timer expires. SLA elapse records duration; the VS confirms outcome. A
recovery specification that provides mechanism and SLA without a VS cannot be operationally
verified at stage granularity. Each VS must satisfy three properties: (a) named, not generic ("VS:
confirmation" fails; "VS: inventory-service health probe returns 200" passes); (b) observable -- a
system state, log entry, metric value, or API response code; (c) distinct from the mechanism --
evidence of completion, not a restatement of the action taken. (Signal: V-03/V-04/V-05 Round 10
-- Verification Signal per recovery stage, each stage independently falsifiable by a named
observable artifact distinct from mechanism and SLA elapse alone.)

**Pass condition**: The Recovery Path column specification or at least one scenario row descriptor
explicitly requires all three components -- mechanism (with actor), SLA target, and named
Verification Signal -- for each of the four lifecycle stages. The VS requirements must cover all
four stages; a specification that names VS for two stages but leaves the other two as
mechanism+SLA only fails. At least one row descriptor illustrates concrete VS examples for at
least two of the four stages with named observables. A VS described only generically ("stage
confirmed", "recovery verified") without naming the observable artifact fails.

**Partial**: Three-component structure present in the column specification but row descriptors or
examples show only mechanism + SLA (no VS); or VS present for some stages but not all four in the
column specification; or VS present and named for at least two stages but described generically
(non-named observable) for the remaining stages.

**Fail**: Recovery Path specification contains mechanism and SLA only, with no Verification Signal
component anywhere in the column specification or row descriptors; or VS mentioned in prose but
not encoded as a required column component; or Recovery Path stages are not individually specified
(single-block recovery description with no per-stage structure).

### C-36 -- Chaos-Trigger Threshold Identity Assertion *(E-22)*
The chaos engineering phase (C-09) activation boundary is explicitly asserted in the template to
use the same threshold expression as the Trigger Condition column value (C-34) -- not merely a
cross-reference link to it, but an identity claim. The distinction is load-bearing: a
cross-reference (Trigger Condition Reference) allows the chaos activation parameter to be a
derivative or approximation of the production trigger threshold. An identity assertion forecloses
divergence by design: the chaos scenario activates at exactly the production detection boundary,
making the test result directly interpretable without a parameter-translation step. Without this
assertion, chaos tests may use a threshold that is close to but not identical to the production
trigger -- making results non-predictive and introducing an invisible calibration gap between the
chaos harness and the production alerting system. (Signal: V-05 Round 11 -- Column Contract
explicitly states Gate 2b activation boundary is the same threshold expression as Trigger
Condition; V-01/V-03/V-04 provide a Trigger Condition Reference link without an identity
assertion.)

**Pass condition**: The chaos gate contract (column contract, gate precondition, or named rule)
contains an explicit identity assertion stating that the chaos activation boundary expression is
the same threshold expression as the Trigger Condition column value -- by name ("same threshold
expression as Trigger Condition" or equivalent). A cross-reference link or "see Trigger Condition"
pointer without an identity claim does not satisfy this criterion. The assertion must appear in the
template structure, not only in a row-level example.

**Partial**: Trigger Condition Reference column or field present in the chaos gate structure,
linking the chaos scenario to the threshold from the main scenario table, but without an explicit
identity assertion that the two expressions are identical; or identity assertion present but only
in a row-level example, not in the gate contract or column specification.

**Fail**: No cross-reference between chaos activation boundary and Trigger Condition column in the
chaos gate structure; chaos scenarios specify injection parameters independently of the Trigger
Condition threshold; or no chaos gate structure exists (C-09 FAIL subsumes C-36).

### C-37 -- Observable Signal Detection Horizon *(E-23)*
Each Observable Signal specification (C-10) carries a third required component alongside (1) named
signal and (2) rationale: a Detection Horizon -- the maximum latency window within which the signal
is expected to appear after fault onset or threshold crossing. The Detection Horizon transforms
signal absence from an ambiguous state into a named finding: if the named signal has not appeared
within the declared horizon, absence is itself an actionable event requiring escalation. Without a
Detection Horizon, operators cannot distinguish a signal not yet arrived from a signal permanently
absent -- the absence condition cannot be operationalized. The Detection Horizon is distinct from
the SLA target in C-35 (which measures recovery stage duration) and from the threshold expression
in C-34 (which defines the activation boundary): the Detection Horizon defines how quickly the
monitoring system must confirm the fault, independent of how quickly the system recovers. A generic
horizon ("shortly", "promptly", "as soon as possible") does not satisfy this criterion because it
cannot be operationalized as an alert threshold. (Signal: V-04 Round 11 -- Detection Horizon as
required field in Gate 7 Observability Manifest; V-05 Round 11 -- Detection Horizon as explicit
third component in Gate 3 Observable Signal specification.)

**Pass condition**: Detection Horizon is named as a required component in the Observable Signal
specification (column Fill Requirement, manifest row template, or equivalent named structure). The
horizon specifies a concrete time window (e.g., "within 30s of fault injection", "by next
heartbeat cycle <= 60s", "within one scrape interval"). Generic horizon language fails. At least
one row fill or example illustrates a concrete Detection Horizon value. The Detection Horizon must
be structurally distinct from the SLA target and the threshold expression -- a single field serving
multiple purposes does not satisfy this criterion.

**Partial**: Detection Horizon field present in the observability specification but populated
generically ("promptly", "soon") without a concrete time window; or Detection Horizon concept
present in prose description of the observability section without a named required field in the
column specification; or Detection Horizon named but conflated with SLA target or threshold
expression in a shared field.

**Fail**: No Detection Horizon component in the Observable Signal specification; observability
recommendations carry only named signal + rationale (two-component form); or no observability
structure exists (C-10 FAIL subsumes C-37).

### C-38 -- Chaos-Observability Bidirectional Coverage Matrix *(E-24)*
A named cross-reference artifact -- table, matrix, or manifest -- is produced that links each
chaos scenario (C-09) to >= 1 Observable Signal (C-10) by ID, and each Observable Signal to >= 1
chaos scenario by ID. The matrix enforces bidirectional completeness: a chaos scenario with no
linked Observable Signal is a "dark chaos" scenario -- it fires but cannot be confirmed as
detected, making its pass/fail signal unverifiable in production. An Observable Signal with no
linked chaos scenario cannot be exercised by the chaos harness -- it may exist in the observability
manifest but its production behavior under fault conditions is untested. Both failure modes are
invisible without the bidirectional matrix. The matrix also serves as a cross-artifact audit: when
C-09 and C-10 are each satisfied independently (as in V-04, which has Gate 6 and Gate 7 as
separate Act 3 outputs), the matrix is the only artifact that confirms their content is consistent.
Having both a C-09 output and a C-10 output without a bridging matrix does not satisfy this
criterion. (Signal: V-05 Round 11 -- named Chaos-Observability Coverage Matrix cross-referencing
observability coverage against chaos scenario IDs; V-04 has both C-09 and C-10 outputs but no
bridging matrix.)

**Pass condition**: A named cross-reference artifact is present in the output that lists each chaos
scenario by ID alongside its linked Observable Signal(s) by ID, and lists each Observable Signal
by ID alongside its linked chaos scenario(s) by ID. The artifact emits a named gap finding (e.g.,
CHAOS-OBS-GAP-NN) for any chaos scenario with no Observable Signal linkage and for any Observable
Signal with no chaos scenario linkage. Both directions of coverage must be verified by the
artifact; a one-directional listing satisfies PARTIAL only. The artifact must be a distinct named
section or table, not inferred from co-location of C-09 and C-10 outputs.

**Partial**: Cross-reference artifact present but covers only one direction (chaos ->
observability, or observability -> chaos); or both directions covered but gap findings are not
emitted for uncovered entries; or coverage linkage described in prose without a named artifact; or
C-09 and C-10 outputs co-located in the same section but without a named bridging matrix.

**Fail**: No cross-reference artifact between C-09 and C-10 outputs; chaos scenarios and
observability hooks are independently produced with no traceability between them; or C-09 or C-10
absent (parent criterion FAIL subsumes C-38).

### C-39 -- Gate-Open Precondition Acknowledgment Checkpoint *(E-25)*
The Gate OPEN precondition for a gate that enforces a structural constraint (identity assertion,
coverage minimum, quality standard, or equivalent) includes an explicit named acknowledgment
statement that the analyst confirms before the gate opens. The acknowledgment checkpoint is
distinct from a gate status check ("prior gate is CLOSED") -- it requires active confirmation of a
named constraint that governs the gate's operation, not merely verification that preceding phases
have completed. V-02 uses a checkbox form (`[ ] Identity assertion acknowledged: chaos activation
boundary = Gate 2 threshold expression for each scenario, verbatim -- not a derivative`); V-04 and
V-05 use named prose acknowledgment in the Gate OPEN position. The checkpoint closes the gap
between a constraint being declared (in a Column Contract or pre-analysis section) and a constraint
being confirmed at execution time: an analyst familiar with the template can enter a gate without
re-confirming the governing constraint. The acknowledgment checkpoint forces re-confirmation at
gate-entry time, making constraint compliance independently verifiable for each gate invocation.
C-18 requires named entry conditions (which prior gates must be CLOSED); C-39 requires a named
constraint acknowledgment (which operational rule must be confirmed at entry). C-31 requires the
bypass protocol to be declared upfront; C-39 requires specific constraints to be confirmed at the
moment of gate execution. These three criteria are orthogonal: a gate can carry entry conditions,
pre-analysis declarations, and acknowledgment checkpoints simultaneously. (Signal: V-02/V-04 Round
12 -- Gate 2b OPEN precondition carries explicit identity assertion acknowledgment with "verbatim
-- not a derivative" confirmation; V-01/V-03 carry copy instructions without a confirmable
checkpoint.)

**Pass condition**: At least one gate OPEN precondition block contains an explicit named
acknowledgment statement confirming a specific structural constraint. The acknowledgment must name
the constraint it confirms -- not a generic status or "proceed" declaration. It must be positioned
in the Gate OPEN precondition block (not in a column Fill Requirement, preamble, or row
descriptor). Checkbox form (`[ ]`) is the preferred representation; a named prose acknowledgment
positioned in the Gate OPEN block satisfies this criterion. A copy instruction or fill guidance
("copy threshold expression from Gate 2") is not an acknowledgment checkpoint.

**Partial**: Gate OPEN precondition present but carries only gate status checks (prior gate CLOSED,
required artifact present) without a named constraint acknowledgment; or acknowledgment present in
a column Fill Requirement or preamble declaration rather than a Gate OPEN precondition block; or
acknowledgment names the constraint but is phrased as an instruction rather than a confirmable
checkpoint (e.g., "copy the threshold expression" vs "Identity assertion acknowledged: boundary =
threshold expression -- not a derivative").

**Fail**: No gate OPEN preconditions in any gate; or all gate OPEN preconditions carry only status
checks with no constraint acknowledgment; or acknowledgment pattern present only in pre-analysis
declarations without any gate-entry checkpoint.

### C-40 -- Gate-Close Prohibition Clause *(E-26)*
At least one gate CLOSE condition (postcondition block) contains an explicit prohibition clause --
a named statement of the form "no [failure mode]" or "not a [invalid variant]" -- alongside a
positive confirmation clause. The prohibition clause confirms that a named failure mode is absent
from the gate's output, not merely that the success condition is present. The prohibition pattern
closes a gap that positive-only CLOSE conditions cannot cover: a positive CLOSE condition ("every
X has Y filled") can be satisfied while a prohibited variant coexists -- for example, a threshold
expression semantically equivalent to Gate 2 but differently phrased satisfies the positive
assertion while remaining an unauthorized paraphrase. "No paraphrase, no independent calibration"
in the CLOSE explicitly forecloses the semantically-similar-but-not-identical form. Prohibition
clauses are not redundant with criterion Pass conditions: a Pass condition defines the minimum for
a criterion to succeed; a CLOSE prohibition clause verifies that a specific failure mode is absent
from the produced output even where the nominal success condition is satisfied. V-05's Gate 2b
CLOSE confirms "(identity assertion satisfied)" without a prohibition clause, satisfying C-36 but
scoring PARTIAL for C-40 -- demonstrating that the positive confirmation and the prohibition clause
are independently load-bearing components. (Signal: V-02/V-04 Round 12 -- Gate 2b CLOSE: "Every
Trigger Condition Reference contains verbatim Gate 2 threshold expression (identity assertion
satisfied -- no paraphrase, no independent calibration)"; V-05 CLOSE: "(identity assertion
satisfied)" without prohibition clause.)

**Pass condition**: At least one gate CLOSE condition block contains an explicit prohibition clause
naming a specific failure mode (e.g., "no paraphrase", "no independent calibration", "not a
description-absence argument"). The CLOSE block must carry both a positive confirmation clause
("every X has Y") and at least one prohibition clause ("no Z"). The prohibition must name a
specific failure mode -- generic language ("no errors", "no omissions") does not satisfy this
criterion. The prohibition must appear in the gate CLOSE block, not only in a Pass condition or
column Fill Requirement.

**Partial**: CLOSE conditions contain prohibition-like language but describe consequences rather
than naming the absent failure mode ("if paraphrase detected, gate remains OPEN" vs "no paraphrase"
as a CLOSE-time assertion); or prohibition clause present in a column Fill Requirement or row
descriptor rather than a gate CLOSE block; or the CLOSE block contains a named prohibition but no
positive confirmation clause alongside it.

**Fail**: No gate CLOSE conditions carry prohibition clauses; all CLOSE conditions are
positive-only confirmations; failure mode absence is not verified at gate-close time; or only Pass
conditions (criterion-level) name prohibited forms without a CLOSE-block prohibition clause.

### C-41 -- Impossibility Argument Quality Gate Postcondition *(E-27)*
The Gate 1 CLOSE postcondition (or equivalent confidence triage gate closure block) explicitly
verifies the quality of impossibility arguments -- confirming both field completion and argument
basis -- rather than checking field presence only. C-15 requires the template to carry the DS
Primitive cited field with inline VALID/INVALID examples; C-41 requires the Gate 1 CLOSE
postcondition to enforce argument quality at gate-closure time by naming the required basis type
("architecture basis") and the prohibited basis type ("description absence") in the same
postcondition statement. The distinction between a postcondition that checks presence and one that
checks quality is load-bearing: "DS Primitive cited: field non-empty" is satisfied by a field
containing "the topic does not describe a distributed cache" -- a description-absence argument that
fills the field without meeting the architecture-basis standard. The quality postcondition closes
this gap by making architecture grounding a gate-closure requirement verified at run time, not only
a field design intention enforced by inline examples. When the quality postcondition is absent, an
analyst can satisfy the DS Primitive cited field with any text, with quality relying entirely on
correct interpretation of the inline VALID/INVALID examples rather than on a gate-enforced check.
(Signal: V-01/V-05 Round 12 -- Gate 1 CLOSE postcondition: "Every Argued-Impossible has DS
Primitive cited: field completed (architecture basis, not description absence)"; V-02/V-03/V-04
carry advisory prose about DS Primitive naming with no Gate 1 CLOSE postcondition auditing
argument basis.)

**Pass condition**: The Gate 1 (or equivalent confidence triage gate) CLOSE postcondition
explicitly verifies both (a) the DS Primitive cited field is completed and (b) the basis is
architecture-grounded, naming the prohibited basis type ("description absence" or equivalent) by
name in the same postcondition statement. The postcondition must appear in the CLOSE block (not
only in the column Fill Requirement or preamble). A presence-only CLOSE condition ("DS Primitive
cited: field non-empty") does not satisfy this criterion; both the completion check and the quality
check must be explicit.

**Partial**: Gate 1 CLOSE postcondition present and verifies DS Primitive cited field completion
but does not name the prohibited basis type (presence check without quality check); or the
architecture basis requirement is stated but the prohibited form ("description absence") is not
named in the postcondition; or the quality check appears in a preamble or column specification
rather than in the Gate 1 CLOSE block.

**Fail**: No Gate 1 CLOSE postcondition; or Gate 1 CLOSE postcondition checks only gate status or
coverage counts without auditing impossibility argument quality; or C-15 FAIL subsumes C-41 (no
DS Primitive cited field exists in the template).

### C-42 -- Gate-Close Clause Structural Independence *(E-28)*
A gate CLOSE block that contains both a positive confirmation clause and a prohibition clause
(satisfying C-40) carries those two clauses as STRUCTURALLY INDEPENDENT items -- separate
checkboxes, separately labeled verification blocks, or equivalent independently-auditable form.
C-40 requires both clause types to be present; C-42 requires them to be independently verifiable.
The distinction is load-bearing under dispute: a single combined item ("identity assertion
satisfied -- no paraphrase, no independent calibration") passes C-40 but conflates two distinct
audit points into one. When the combined item is disputed or when one component passes while the
other fails, a reviewer cannot determine from the CLOSE block alone which clause is in violation.
Structurally independent items close this gap: the positive assertion can be confirmed while the
prohibition check is still pending, enabling targeted remediation without invalidating the
confirmed component. The independence also surfaces partial states that combined items mask: a
gate whose positive assertion is satisfied but whose prohibition clause has not been evaluated is
distinguishable from a gate where both clauses have been evaluated and confirmed. (Signal:
V-01/V-04/V-05 Round 13 -- Gate 2b CLOSE splits into `[ ] Identity assertion confirmed: every TCR
contains the verbatim Gate 2 threshold expression` AND `[ ] Prohibition clause confirmed: no TCR
contains a paraphrased or independently calibrated expression`; V-02/V-03 combine both into one
checkbox.)

**Pass condition**: At least one gate CLOSE block contains both positive confirmation clause AND
prohibition clause as SEPARATE, independently-checkable items. Each item must be capable of being
individually confirmed or denied -- separate checkboxes, separate labeled verification entries, or
equivalent form where each clause is auditable without the other. A single combined item carrying
both clauses in one statement satisfies C-40 but does not satisfy C-42. Both items must appear in
the gate CLOSE block; a prohibition clause in a column Fill Requirement alongside a positive
confirmation in the CLOSE block does not satisfy the structural independence requirement for the
CLOSE block itself.

**Partial**: CLOSE block carries both positive confirmation and prohibition clause but in a
partially-separated form -- e.g., a single checkbox with labeled sub-components ("identity
assertion: confirmed; prohibition: confirmed") within one audit point; or independently-structured
items present for one gate CLOSE but combined form used in other gates where both clause types
apply.

**Fail**: No gate CLOSE block carries both clause types as structurally independent items; all
CLOSE blocks with both clause types use combined form (C-40-passing but C-42-failing); or C-40
FAIL subsumes C-42.

### C-43 -- Impossibility Argument Basis Clause Independence *(E-29)*
The Gate 1 CLOSE postcondition (satisfying C-41) splits required-basis verification ("architecture
basis present") and prohibited-basis verification ("description absence absent") into STRUCTURALLY
INDEPENDENT items -- separate checkboxes, separate labeled verification blocks, or equivalent
independently-auditable form. C-41 requires both basis types to be named in the same postcondition
statement; C-43 requires them to be independently verifiable. A combined statement such as
"(architecture basis, not description absence)" satisfies C-41 -- both are named -- but conflates
two independently-assessable conditions into a single audit point: (a) that a valid architecture
basis IS present and (b) that a description-absence argument IS NOT present. These conditions are
not logically equivalent and can fail independently: an argument can cite an architecture basis
while also invoking a supplementary description-absence component, passing the positive check while
partially violating the prohibition. Independent items close this gap: the presence verification
can be confirmed while the absence verification is still pending. Independent form also enables
precise remediation -- a Gate 1 CLOSE where the required-basis check confirms but the
prohibited-basis check fails can be re-opened at the prohibition level alone. (Signal: V-02/V-04/
V-05 Round 13 -- Gate 1 CLOSE splits into `[ ] Impossibility argument basis confirmed: every
Argued-Impossible cites an architecture basis ... -- required basis: present` AND `[ ]
Impossibility argument prohibition confirmed: no Argued-Impossible argument is based on description
absence ... -- prohibited basis: absent`; V-01 uses one combined postcondition statement.)

**Pass condition**: Gate 1 CLOSE postcondition contains required-basis verification AND
prohibited-basis verification as SEPARATE, independently-checkable items. Each item must name its
specific condition and be individually confirmable. A single combined postcondition naming both
satisfies C-41 but does not satisfy C-43. Both items must appear in the Gate 1 CLOSE block;
prohibited-basis language only in a column Fill Requirement or preamble without a corresponding
independent CLOSE item does not satisfy this criterion.

**Partial**: Gate 1 CLOSE contains both basis checks in a partially-separated form -- e.g., a
single item with labeled sub-clauses ("required basis: present; prohibited basis: absent") within
one checkpoint; or two independently-structured items present but covering only a subset of the
basis types verified by the postcondition.

**Fail**: Gate 1 CLOSE postcondition combines required-basis and prohibited-basis in a single
unitary statement (C-41-passing combined form); or Gate 1 CLOSE carries only one of the two basis
checks as an independent item; or C-41 FAIL subsumes C-43.

### C-44 -- Bidirectional Gap Registry Artifact Structure *(E-30)*
The bidirectional coverage matrix (C-38) gap findings are produced as structured three-field
registry entries in a named registry section, rather than as inline notations within matrix rows.
C-38 requires a named gap finding for any uncovered entry; C-44 requires each gap finding to be
a structured artifact with three independently-specified fields: (1) Source -- the uncovered
element identifier (the chaos scenario ID or Observable Signal ID that has no covering link);
(2) Missing link -- the Observable Signal or chaos scenario that should cover it but does not
exist or is not linked; (3) Consequence -- what the coverage gap makes unverifiable in production
(e.g., "dark chaos: CS-03 fires but no Observable Signal can confirm detection; pass/fail
unverifiable"). The three-field structure closes the gap that inline notation leaves open: an
inline finding names the problem but not the consequence, making gap severity invisible to a
reviewer scanning for risk priority without reading surrounding scenario prose. The formal registry
also enables registry-level queries (all consequences of dark chaos scenarios; all missing
Observable Signals) that inline notation cannot support. When the matrix has no uncovered entries,
an explicit nil confirmation must appear in each registry section ("GAP REGISTRY: no uncovered
entries") -- inline absence of gap findings is ambiguous between "no gaps" and "gaps not checked."
(Signal: V-03/V-05 Round 13 -- formal PART A GAP REGISTRY and PART B GAP REGISTRY sections
required before COMPLETE; each entry is a three-field structured artifact; V-01/V-02/V-04 use
inline named-finding notation satisfying C-38 but not C-44.)

**Pass condition**: The bidirectional coverage matrix produces gap findings as structured
three-field registry entries (Source / Missing link / Consequence, or equivalent three named
fields) in a named registry section (PART A GAP REGISTRY / PART B GAP REGISTRY, or equivalent
named sections for each matrix direction). Both matrix directions must have a named registry
section. Each uncovered entry produces a registry artifact with all three fields populated. When
a direction has no uncovered entries, an explicit nil confirmation is present in that registry
section. Inline gap notation with named finding tags satisfies C-38 but does not satisfy C-44; the
formal named registry structure is required.

**Partial**: Formal registry section present but entries carry fewer than three named fields (e.g.,
Source and Consequence without Missing link); or formal registry present with three-field entries
for one matrix direction but not both; or three-field entries present but embedded as inline
annotations within matrix rows rather than in a named registry section; or registry sections
present but nil confirmation absent when a direction has no uncovered entries.

**Fail**: No formal gap registry section in either matrix direction; gap findings appear only as
inline notations or prose annotations; or C-38 FAIL subsumes C-44.

### C-45 -- Gate Independence Completeness Verification Block *(E-31)*
When both C-42 (Gate 2b CLOSE structural independence) and C-43 (Gate 1 CLOSE basis clause
independence) are satisfied, the analysis carries a named verification block -- at COMPLETE time
or as a pre-COMPLETE audit step -- that explicitly enumerates all gate CLOSE blocks in the
template that carry multi-clause content (positive confirmation + prohibition clause pair) and
confirms the independence status of each. The block records: (1) which gate CLOSE blocks contain
both a positive assertion clause and a prohibition clause, identified by gate number or name;
(2) whether each such gate uses structural independence form (two-checkbox, two-item, or equivalent)
or combined form; and (3) a declaration that independence scope is COMPLETE -- that no eligible gate
CLOSE block was overlooked. This criterion is orthogonal to C-42 and C-43, which require
independence to exist in specific named gates; C-45 requires a meta-verification that the
independence scope is exhaustive across all eligible gates, not only the two targeted by C-42 and
C-43. It is also orthogonal to C-28 (post-analysis rule registry audit, which tracks rule
invocations) and C-23 (scope declaration closure bracket, which tracks commerce operation
coverage): C-45 tracks gate CLOSE clause independence coverage. Without C-45, independence can be
applied to whatever gates a reviewer targets across rounds with no artifact confirming that all
eligible gates were considered. When C-42 and C-43 are achieved sequentially in different rounds
(as V-01 and V-02 demonstrated -- V-01 added Gate 2b in R13 and Gate 1 in R15; V-02 added Gate 1
in R13 and Gate 2b in R15), the absence of a completeness block reveals that independence was
added reactively rather than as a systematic design sweep. V-03/V-04/V-05 carry an independence
completeness block that closes the sweep, making the independence scope independently auditable and
providing an upward compatibility guard: when a future round adds a gate with multi-clause CLOSE
content, its absence from the completeness block is immediately detectable. (Signal: V-03/V-04/
V-05 Round 15 -- named block at COMPLETE time enumerates Gate 2b CLOSE and Gate 1 CLOSE as the
only eligible gates, confirms both carry two-checkbox independent form, declares independence scope
COMPLETE; V-01/V-02 assemble C-42 and C-43 in separate rounds with no completeness verification
block.)

**Pass condition**: A named post-analysis or COMPLETE-time block is present that enumerates all
gate CLOSE blocks by gate identifier, classifies each as eligible (positive + prohibition clause
pair present) or ineligible (single clause type), confirms the independence status of each eligible
gate (independent form or combined form), and declares independence scope COMPLETE. The block must
be a named labeled section or audit item -- not a prose paragraph asserting completeness without
enumeration. Each gate must be identified by its gate number or name; omitting gates from the list
is not a valid ineligible classification. When only Gate 2b CLOSE and Gate 1 CLOSE are eligible,
the block must explicitly confirm that no other gate CLOSE blocks in the template carry multi-clause
content, making the COMPLETE declaration auditable.

**Partial**: Independence completeness block present but does not enumerate gates by identifier
(asserts "all gates verified" without naming them); or block enumerates the C-42 and C-43 gates
but omits the explicit "no other eligible gates" confirmation; or completeness verification
embedded within an individual gate CLOSE block rather than as a distinct post-analysis or
COMPLETE-time artifact; or block present but covers only one of the two eligible gates.

**Fail**: No independence completeness verification block; C-42 and C-43 individually satisfied
but no meta-artifact confirms that all eligible gate CLOSE blocks were identified and audited; or
C-42 FAIL subsumes C-45 (no structural independence exists to complete); or completeness claim
present only in prose preamble without a named verification block.

### C-46 -- Gap Registry Nil Confirmation Structural Form *(E-32)*
When a direction in the bidirectional coverage matrix (C-38) produces no uncovered entries, the
nil confirmation required in that registry section by C-44 uses the same three-field structural
form as gap entries: Source / Missing link / Consequence, with each field explicitly populated with
nil content (e.g., Source: "N/A -- all chaos scenarios are fully linked to >= 1 Observable Signal",
Missing link: "N/A -- no dark chaos scenarios in this direction", Consequence: "nil --
bidirectional coverage complete for PART A"). C-44 requires a nil confirmation to be present in
each registry section when no gaps exist; C-46 requires that confirmation to use three-field form
structurally indistinguishable from gap entries. The gap it closes: a prose nil ("GAP REGISTRY: no
uncovered entries in this direction") satisfies C-44's requirement but creates a structural
asymmetry between gap entries (three-field) and the nil state (prose). A reviewer scanning registry
Source fields encounters either a gap Source identifier or a prose nil line, requiring mode-
switching to interpret nil state. The three-field nil eliminates this asymmetry: the nil state
becomes a typed registry entry. This uniformity makes registry scanning fully deterministic -- a
Source-field scan yields either a gap artifact identifier (Source: CHAOS-OBS-GAP-NN) or a typed
nil marker (Source: N/A), with no structural difference between the two states. The three-field nil
also makes the "no gaps" assertion independently auditable across three dimensions rather than as a
single prose statement. (Signal: V-03/V-05 Round 15 -- formal PART A GAP REGISTRY and PART B GAP
REGISTRY carry three-field nil entries when a direction has no uncovered entries; V-04 lacks the
registry (C-44 FAIL); V-01/V-02 lack the registry.)

**Pass condition**: Each registry direction (PART A and PART B, or equivalent named sections) that
has no uncovered entries carries a nil confirmation as a three-field registry entry with Source,
Missing link, and Consequence fields each explicitly populated with nil content. The nil entry must
be positioned as a registry row, not as a prose paragraph adjacent to the registry. The Source
field must carry an N/A marker or typed nil indicator (not blank). Both registry directions must
independently satisfy this criterion; a three-field nil in PART A alongside a prose nil in PART B
satisfies PARTIAL only. When a direction has at least one actual gap entry, no nil confirmation
entry is required for that direction. C-44 FAIL subsumes C-46.

**Partial**: Three-field nil entry present in one registry direction but the other direction uses a
prose nil; or three-field nil present but one or more fields are blank rather than explicitly
nil-populated; or nil entry structured as a row but Source field carries a prose statement without
a typed N/A marker; or C-44 PARTIAL (registry present for one direction only) with three-field nil
in the present direction but no registry for the absent direction.

**Fail**: Nil confirmations in both registry directions are prose-only ("no uncovered entries");
or nil confirmations absent in a direction with no gap entries (C-44 nil-confirmation failure);
or C-44 FAIL subsumes C-46 (no formal gap registry exists to carry nil entries).

### C-47 -- VS Cross-Reference Registry (Act 1 Terminal) *(E-33)*
At the close of Act 1 (or equivalent first-act terminal position), the output includes a named VS
Cross-Reference Registry that enumerates every Verification Signal (VS) produced by C-35 recovery
stage specifications across all scenarios. The registry is organized bidirectionally: each entry
names (1) the scenario ID and recovery stage (Detect / Contain / Recover / Validate) that produced
the VS, and (2) the Observable Signal ID from the observability phase (C-10 / C-37) that
corresponds to it, or an explicit nil marker when no correspondence exists. This cross-reference
closes the gap that per-row VS specification (C-35) leaves open: C-35 requires VS at row level but
provides no mechanism to confirm that the VS catalog is complete, non-duplicative, or linked to the
observability layer. The VS Cross-Reference Registry makes the full VS catalog independently
auditable without traversing scenario prose, enables VS-to-observability gap detection at catalog
level, and establishes a pre-COMPLETE Act 1 audit artifact that confirms VS production is
exhaustive. This criterion is orthogonal to C-35 (per-row VS requirement), to C-28 (post-analysis
rule registry audit -- which confirms rule invocation completeness; C-47 confirms VS production
completeness and VS-to-observability linkage), and to C-38 (chaos-observability bidirectional
matrix -- which cross-references chaos scenarios to Observable Signals; C-47 cross-references
recovery stage VS to Observable Signals). The C-35/C-47 split mirrors the C-38/C-44 split: C-38
requires gap findings; C-44 requires those findings in a formal registry structure. C-35 requires
VS per stage; C-47 requires a terminal registry confirming all VS were produced and linking each
to the observability layer. (Signal: V-05 Round 16 -- named VS Cross-Reference Registry produced
at Act 1 terminal position, enumerating all VS by scenario x stage with Observable Signal
cross-references and N/A nil markers where no correspondence exists; V-01/V-02/V-03/V-04 carry
C-35 PASS but no terminal VS catalog.)

**Pass condition**: A named VS Cross-Reference Registry (or equivalently named terminal artifact)
is present at Act 1 close position. The registry enumerates every VS from every recovery stage in
every Act 1 scenario, identified by scenario ID and stage name. Each VS entry carries an Observable
Signal cross-reference field populated with an Observable Signal ID or an explicit N/A nil marker
-- not blank. The artifact is positioned at Act 1 terminal level, not embedded within an individual
scenario row or gate prose block. At least one entry illustrates a concrete Observable Signal
cross-reference by ID. C-35 FAIL subsumes C-47.

**Partial**: Terminal VS catalog present but entries are not organized by scenario ID and stage
(VS list without scenario x stage indexing); or catalog present with scenario x stage indexing but
Observable Signal cross-reference field absent for all entries (enumeration without cross-reference
layer); or catalog covers only some scenarios or some stages rather than the complete Act 1 VS
population; or catalog embedded within an individual scenario row rather than as a terminal
artifact; or C-35 PARTIAL (VS present for some stages only) with terminal catalog covering only
the stages where VS exist.

**Fail**: No terminal VS Cross-Reference Registry; VS distributed across scenario rows with no Act
1 terminal catalog artifact; or C-35 FAIL subsumes C-47.

### C-48 -- Named Enforcement Contract with Rule Identifiers *(E-34)*
A named enforcement contract block (or equivalently named preamble element) is present in the
template that declares mandatory constraints applicable to sub-parts and assigns each constraint a
unique short-form identifier (e.g., Rule A / Rule B; § 1.1 / § 1.2; RULE-FILL-1 / RULE-FILL-2;
or equivalent alphanumeric label). The identifier must be a label usable as a citation in
downstream content without restating the full rule prose -- "**Rule A applies**" or "§ 1.2
applies" is a valid citation form; "see the first rule in the preamble" is not. This criterion
establishes the referenceability prerequisite that C-49 (preamble pre-positioning with inline
named-label citations) and C-50 (multi-level restatement) depend on: without named identifiers,
inline reinforcement in sub-parts can only paraphrase or copy rule text, creating divergence risk
between the preamble declaration and downstream restatements. Named identifiers close this risk by
making sub-part citations verifiably traceable to the enforcement contract label. This criterion
is orthogonal to C-27 (named rule block registry, which centralizes conditional linkage rules for
auditability; C-48 requires a preamble-level enforcement contract for fill constraints) and C-31
(bypass chain declaration, which enumerates remediation steps; C-48 requires a fill-constraint
contract with labeled rules). (Signal: All five variations Round 17 -- "Document Enforcement
Contract" or "§ 1 Enforcement Mandate" block present with at least two labeled rules (Rule A /
Rule B; § 1.1 / § 1.2) enabling citation by short-form label in downstream sub-parts.)

**Pass condition**: A named enforcement contract block is present in the template. The block
declares mandatory constraints applicable to sub-parts and assigns a unique short-form label
identifier to each constraint. At least two distinct rule label identifiers must be present. The
identifier must function as a citation handle -- it must be short enough to appear inline in a
sub-part fill requirement without restating rule prose. The block must be a named element (not an
anonymous prose paragraph); generic headings such as "Instructions" or "Rules" without a named
block boundary do not satisfy this criterion.

**Partial**: Named enforcement contract block present with labeled identifiers but only one
distinct identifier rather than two or more; or block present with two or more constraints but
rules are identified only by ordinal position as structural markers rather than short-form citation
labels; or labeled identifiers present but embedded inline in individual gate-section prose rather
than in a named contract block.

**Fail**: No named enforcement contract block; fill constraints declared only in anonymous prose
preamble or section headers; constraints defined without any label identifiers; or no mandatory
fill constraints declared anywhere in the template.

### C-49 -- Enforcement Preamble Pre-Positioning with Named-Label Sub-Part Reinforcement *(E-35)*
The named enforcement contract (C-48 PASS required) is positioned in the template BEFORE all
sub-parts it governs, AND at least one sub-part carries inline reinforcement citing at least one
rule by its named label identifier. The two requirements are jointly necessary: pre-positioning
alone (contract before sub-parts, no sub-part inline citations) ensures the contract is read first
but allows enforcement signal to decay across a long sub-part sequence; inline citations alone
(sub-parts cite rules by label, but contract appears after or among them) allows a filler to begin
filling before encountering the contract. Together they close the enforcement continuity gap:
the contract is visible before any fill action (pre-positioning) and remains present at every fill
moment where a constraint is relevant (inline citation). This criterion is orthogonal to C-50
(which requires three or more hierarchy levels with explicit restatement labels; C-49 requires
correct positioning and citation at the preamble + sub-part levels; C-50 requires at least one
additional independent structural level). (Signal: V-01/V-02/V-03/V-04 Round 17 -- enforcement
contract positioned before Steps 1a through 1d with inline "Rule A applies" / "§ 1.1 applies"
per sub-part; V-05 fails -- enforcement structure present but pre-positioning before all sub-parts
with inline named-label citations absent.)

**Pass condition**: The enforcement contract block (C-48 PASS required) is positioned in the
template before all sub-parts (steps, fill-requirement sections, row descriptors, or equivalent)
that it governs -- no sub-part precedes the block in the template. At least one sub-part carries
inline reinforcement that cites at least one rule by its named label identifier (the label
defined in the C-48 enforcement contract). The inline citation must use the label as defined --
not a paraphrase, not a generic "see contract" pointer. C-48 FAIL subsumes C-49.

**Partial**: Enforcement contract pre-positioned before all sub-parts but no sub-part carries
inline named-label citations (pre-positioning only); or at least one sub-part carries inline
labeled citations but the enforcement contract is not pre-positioned before all sub-parts it
governs (citations without pre-positioning); or inline citations present but use paraphrase of
rule content rather than the label identifier; or C-48 PARTIAL with pre-positioning and at least
one sub-part citation.

**Fail**: Enforcement contract block absent (C-48 FAIL subsumes C-49); or contract exists but is
interleaved with or positioned after sub-parts; or contract pre-positioned but inline reinforcement
present only in summary or terminal positions rather than within individual sub-parts at fill time;
or no sub-part carries inline rule citation of any kind.

### C-50 -- Multi-Level Enforcement with Explicit Restatement Label *(E-36)*
The enforcement content (at least one named rule from the C-48 contract) appears at three or more
structurally independent hierarchy levels within the template, with at least one location outside
the preamble carrying an explicit restatement label that identifies the restatement's location
context (e.g., "(restated for co-location)", "§ 1.1 restated at column-contract level", "Rule B
restated for co-location at column-contract level", or equivalent). A structurally independent
level is a distinct template position that is not a sub-item of another qualifying level -- a
preamble block, a sub-part inline citation, a column contract entry, a row descriptor bullet, and
a document-header enforcement note each qualify as separate levels. C-49 requires the preamble
and at least one sub-part inline citation -- two levels. C-50 requires at least one additional
independent structural level beyond those required by C-49, with explicit restatement attribution.
The explicit restatement label closes the audit gap: without it, a reviewer cannot distinguish a
redundant copy (which might diverge) from an acknowledged restatement traceable to the authoritative
preamble definition. This criterion is orthogonal to C-27 (named rule registry, which centralizes
rules; C-50 requires rules to be restated at independent downstream locations) and C-39 (gate-open
acknowledgment checkpoint, which confirms constraint awareness at gate entry; C-50 requires
structural restatement at independent levels, not merely acknowledgment). (Signal: V-01/V-02/V-03/
V-04 Round 17 -- three to four independent hierarchy levels with explicit labels: V-01 Column
Contract "(restated for co-location)"; V-02 "§ 1.1 restated at column-contract level"; V-03
"Rule B restated for co-location at column-contract level" plus D-Phase header as 4th level; V-04
Column Contract "(restated for co-location at column-contract level)" plus per-stage Row Descriptor
bullets as 4th level.)

**Pass condition**: The enforcement content (at least one named rule from the C-48 contract)
appears at three or more structurally independent hierarchy levels in the template. At least one
location outside the preamble level carries an explicit restatement label naming the location
context. Preamble, sub-part inline, and at least one additional independent structural element
(column contract, row descriptor, act header, document-header enforcement note, or equivalent) must
each carry the enforcement content. The restatement label must be explicit text -- not implied by
proximity or co-location. C-48 FAIL subsumes C-50.

**Partial**: Enforcement content at three or more independent levels but no explicit restatement
label at any location outside the preamble (multi-level presence without restatement attribution);
or explicit restatement label present but the enforcement content appears at only two independent
levels; or restatement label present but does not name the location context ("restated here" without
identifying the level or purpose); or C-48 PARTIAL with multi-level presence and at least one
labeled restatement.

**Fail**: Enforcement content at fewer than two independent hierarchy levels (C-49 not satisfied);
or enforcement content at two levels only (preamble + one inline) with no additional independent
structural level; or multi-level presence without any restatement label and fewer than three levels;
or C-48 FAIL subsumes C-50.

---

## Scoring Formula

| Tier | Weight | Criteria | Per-criterion |
|------|--------|----------|--------------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 | PASS=12, PARTIAL=6, FAIL=0 |
| Recommended | 30% | C-06, C-07, C-08 | PASS=10, PARTIAL=5, FAIL=0 |
| Aspirational | 10% | C-09 through C-50 | PASS=2, PARTIAL=1, FAIL=0; capped at 10 |

```
composite = sum(essential_scores)               # max 60
          + sum(recommended_scores)             # max 30
          + min(sum(aspirational_scores), 10)   # max 10 (capped)
```

Maximum possible score: **100**

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

**Ceiling references under v17:**
- R17 V-05 (C-49 FAIL): 82/84 uncapped
  -> composite = 60 + 30 + 10 = **100** (capped)
- R17 V-01/V-02/V-03/V-04 (all 42 criteria PASS): 84/84 uncapped
  -> composite = **100** (new uncapped ceiling: 84/84 -- first four-way tie at perfect score)
- Open for R18: C-49 PASS for V-05 (enforcement contract pre-positioning + inline named-label
  sub-part reinforcement absent).

---

## Failure Fast-Paths

The following conditions automatically fail scoring regardless of composite score:

- Output contains no explicit failure scenarios (pure prose advice with no scenario structure)
- Output is domain-agnostic (no commerce or distributed systems grounding anywhere)
- Recovery paths are all identical or all trivially "restart the service" / "wait for recovery"
- Fewer than three degradation classes are represented (offline, partial failure, eventual
  consistency)

---

## Version Notes

**v17 changes from v16:**

- **C-48 (new)** -- Named enforcement contract with rule identifiers: extracted from R17 universal
  baseline signal. All five variations introduce a named enforcement contract block (Document
  Enforcement Contract / § 1 Enforcement Mandate) carrying at least two labeled rule identifiers
  (Rule A/Rule B; § 1.1/§ 1.2). The label is the enabling prerequisite for C-49 and C-50:
  without a short-form label, inline sub-part citations and cross-level restatements cannot be
  made verifiably traceable to the authoritative preamble rule. Cracked by all five variations
  simultaneously in R17.
- **C-49 (new)** -- Enforcement preamble pre-positioning with named-label sub-part reinforcement:
  extracted from V-01/V-02/V-03/V-04 R17 structural excellence. The enforcement contract is
  positioned before all sub-parts AND sub-parts cite rules by named label inline. V-05 fails: its
  enforcement structure lacks the pre-positioning + inline named-label citation combination. This
  criterion closes the enforcement continuity gap: pre-positioning ensures contract visibility
  before fill; inline citations ensure rule presence at each fill moment. Cracked by V-01, V-02,
  V-03, V-04.
- **C-50 (new)** -- Multi-level enforcement with explicit restatement label: extracted from R17
  multi-variation excellence. Enforcement content at three or more structurally independent
  hierarchy levels with at least one explicit restatement label outside the preamble (e.g.,
  "(restated for co-location)", "§ 1.1 restated at column-contract level"). The explicit label
  makes cross-level restatements auditable -- a reviewer can distinguish acknowledged restatements
  from divergent copies. V-05 entered R17 passing C-50 (pre-existing multi-level enforcement
  structure); V-01/V-02/V-03/V-04 crack C-50 in R17 simultaneously with C-48 and C-49. Cracked by
  V-01, V-02, V-03, V-04 (and V-05 entering).
- **V-01/V-02/V-03/V-04 achieve 84/84** -- new perfect uncapped ceiling under v17, first four-way
  tie at the ceiling. V-05 (R16 champion at 78/78) recedes to 82/84 (C-49 FAIL).
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 78 to 84 (42 criteria x
  PASS=2).

**v16 changes from v15:**

- **C-47 (new)** -- VS Cross-Reference Registry (Act 1 Terminal): extracted from V-05 Round 16
  structural excellence. Cracked by V-05 only.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 76 to 78 (39 criteria x
  PASS=2).

**v15 changes from v14:**

- **C-45 (new)** -- Gate independence completeness verification block: extracted from V-03/V-04/
  V-05 Round 15 structural excellence. When C-42 and C-43 are both satisfied, the analysis carries
  a named post-analysis block enumerating all gate CLOSE blocks eligible for clause independence
  and confirming each one's status. C-42 requires Gate 2b CLOSE independence; C-43 requires Gate 1
  CLOSE independence; C-45 requires a meta-artifact confirming that ALL eligible gate CLOSE blocks
  were identified and audited -- not only the two targeted by C-42 and C-43 individually. The
  signal: V-01 achieved C-42 in R13 and C-43 in R15 via sequential single-gate additions without
  ever producing an artifact confirming that all eligible gates were considered. V-03/V-04/V-05
  carry an explicit independence completeness block that closes the sweep. Also serves as an upward
  compatibility guard: when a future gate adds multi-clause CLOSE content, its absence from the
  completeness block is immediately detectable. Cracked by V-03, V-04, V-05.
- **C-46 (new)** -- Gap registry nil confirmation structural form: extracted from V-03/V-05 Round
  15 structural excellence. When a registry direction has no uncovered entries, the nil
  confirmation uses the same three-field structure as gap entries (Source: N/A / Missing link: N/A
  / Consequence: nil -- coverage complete). C-44 requires a nil confirmation to be present; C-46
  requires it to use three-field form, making the nil state structurally uniform with gap entries.
  A prose nil satisfies C-44 but creates a structural asymmetry: scanning registry Source fields
  requires mode-switching between gap identifiers and prose nils. The three-field nil eliminates
  this: every Source-field scan yields either a gap identifier or a typed N/A nil marker. Cracked
  by V-03, V-05.
- **V-05 achieves 76/76** -- new perfect uncapped ceiling under v15. Three-way tie at 70/76
  (V-04/V-01/V-02 under v14 R15) is broken: V-04 advances to 72/76 (C-45 PASS) while V-01/V-02
  remain at 70/76. V-03 advances to 73/76 (C-45 PASS + C-46 PASS; C-15 PARTIAL costs -1).
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 72 to 76 (38 criteria x
  PASS=2).

**v14 changes from v13:**

- **C-42 (new)** -- Gate-close clause structural independence: extracted from V-01/V-04/V-05
  Round 13 structural excellence. Cracked by V-01, V-04, V-05.
- **C-43 (new)** -- Impossibility argument basis clause independence: extracted from V-02/V-04/
  V-05 Round 13 structural excellence. Cracked by V-02, V-04, V-05.
- **C-44 (new)** -- Bidirectional gap registry artifact structure: extracted from V-03/V-05 Round
  13 structural excellence. Cracked by V-03, V-05.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 66 to 72 (36 criteria x
  PASS=2).

**v13 changes from v12:**

- **C-39 (new)** -- Gate-open precondition acknowledgment checkpoint. Cracked by V-02, V-04, V-05.
- **C-40 (new)** -- Gate-close prohibition clause. Cracked by V-02, V-04.
- **C-41 (new)** -- Impossibility argument quality gate postcondition. Cracked by V-01, V-05.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 60 to 66 (33 criteria x
  PASS=2).

**v12 changes from v11:**

- **C-36 (new)** -- Chaos-trigger threshold identity assertion. Cracked by V-05 only.
- **C-37 (new)** -- Observable signal detection horizon. Cracked by V-04, V-05.
- **C-38 (new)** -- Chaos-observability bidirectional coverage matrix. Cracked by V-05 only.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 54 to 60 (30 criteria x
  PASS=2).

**v11 changes from v10:**

- **C-33 (new)** -- Intra-row column-group phase gate. Cracked by V-01, V-04, V-05.
- **C-34 (new)** -- Trigger condition column: threshold expression + detection signal. Cracked by
  V-02, V-05.
- **C-35 (new)** -- Three-component recovery stage specification. Cracked by V-03, V-04, V-05.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 48 to 54 (27 criteria x
  PASS=2).

**v10 changes from v9:**

- **C-31 (new)** -- Pre-analysis bypass chain declaration. Cracked by V-01.
- **C-32 (new)** -- Bypass-trigger column scanability. Cracked by V-02, V-05.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 44 to 48 (24 criteria x 2).

**v9 changes from v8:**

- **C-29 (new)** -- Rule-bypass-triggered gate reopening.
- **C-30 (new)** -- Multi-act completion sign-off.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 40 to 44 (22 criteria x 2).

**v8 changes from v7:**

- **C-28 (new)** -- Post-analysis rule registry audit.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 38 to 40 (20 criteria x 2).

**v7 changes from v6:**

- **C-25 (new)** -- Nil-finding supersession protocol.
- **C-26 (new)** -- Confidence triage resolution sub-gate.
- **C-27 (new)** -- Named rule block registry.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 32 to 38.

**v6 changes from v5:**

- **C-22 (new)** -- Typed nil-finding identifiers.
- **C-23 (new)** -- Scope declaration closure bracket.
- **C-24 (new)** -- Template-embedded conditional linkage rules.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 26 to 32.

**v5 changes from v4:**

- **C-19 (new)** -- Gate blockage transparency (Reason-if-OPEN).
- **C-20 (new)** -- Downstream gate amendment with re-close record.
- **C-21 (new)** -- Pre-analysis commerce operation scope declaration.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 20 to 26.

**v4 changes from v3:**

- **C-16 (new)** -- Named gate-state vocabulary.
- **C-17 (new)** -- Permanently barred entries as named coverage gaps.
- **C-18 (new)** -- Explicit phase entry and exit conditions.
- **C-15 strengthened** -- Pass condition now requires named "DS Primitive cited:" field with
  inline VALID/INVALID annotated examples.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 14 to 20.

**v3 changes from v2:**

- **C-14 (new)** -- Conflict-resolution adequacy as DCV source.
- **C-15 (new)** -- DS-primitive-grounded impossibility arguments.
- **C-11 strengthened** -- Low-confidence entries barred (not merely flagged).
- **C-12 strengthened** -- Nil findings require scope rationale.
- **Aspirational scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Band capped at 10.
  Uncapped max 14 across 7 criteria.

**v2 changes from v1:**

- **C-11 (new)** -- Confidence-annotated discovery catalog.
- **C-12 (new)** -- Nil-finding norm for gap sections.
- **C-13 (new)** -- Coverage accountability roster.
- **Aspirational scoring rebalanced**: C-09 and C-10 reduced from PASS=5 to PASS=2 to accommodate
  the growing aspirational tier without changing the band cap.
