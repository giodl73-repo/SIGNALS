## corps-scan R10 Scoring — v10 Rubric (42 criteria, 420 pts)

---

### V-01 — Role Sequence

| Criterion group | Criteria | Assessment |
|----------------|----------|------------|
| **Foundation (C-01–C-25)** | Shared structural base from R9 V-05: IVR triple format, phase headers, YAML template, gate row format, scope boundary, pivot enumeration, group structure | **PASS all** |
| **C-26** | META-RULE declares informal constraints non-binding | **PASS** — "advisory context only" present |
| **C-27** | Conditional advance in completion test | **PASS** — "Advance to GATE 1 if all YES / EXIT-P1: Advance to P2 only if all YES" on every phase |
| **C-28** | META-RULE manifest enumerates all 14 IVR triples by label with count instruction | **PASS** — full 14-row manifest, "count to verify completeness" |
| **C-29** | ENTRY/EXIT structurally paired on every phase | **PASS** — ENTRY-Px and EXIT-Px present in all four phases |
| **C-30** | Completion infrastructure on every phase (predicate + YES/NO checklist + conditional advance) | **PASS** — all three elements present in all four phases |
| **C-31** | Multi-surface verification (manifest + contract table + canonical predicates) | **PASS** — three independent audit surfaces present |
| **C-32** | Phase-contract table as front-matter before Phase 1 header | **PASS** — PHASE CONTRACT TABLE placed before `### PHASE 1` |
| **C-33** | Incompleteness predicate as first structural element of each phase body | **PASS** — `>` blockquote predicate precedes ENTRY-Px in all four phases |
| **C-34** | Manifest terminal TOTAL row | **PASS** — `**14 labeled triples — count to verify completeness**` as final row |
| **C-35** | Incompleteness predicate expressed as blockquote | **PASS** — all four predicates use `>` prefix |
| **C-36** | Manifest carries VIOLATION column | **PASS** — "Violation Pattern" column present in manifest |
| **C-37** | Phase-contract table carries test-item-count column | **PASS** — "Test items" column with 2/5/6/1; counts match actual checklist items |
| **C-38** | Cross-manifest count invariant: TOTAL(14) = P1(2)+P2(5)+P3(6)+P4(1) | **PASS** — arithmetic correct on both sides |
| **C-39** | Cross-manifest verification block before Phase 1 with explicit arithmetic | **PASS** — CROSS-MANIFEST VERIFICATION block in preamble; names TOTAL=14, per-phase sums, equality assertion, halting directive |
| **C-40** | Gate token protocol: typed PASS/FAIL tokens as final line of completion test blocks | **PASS** — GATE TOKEN PROTOCOL preamble block; "If all YES: GATE-1 PASS…" as terminal lines of P2/P3 completion tests |
| **C-41** | Numbered scan protocol: 4-step SCAN PROTOCOL anchored to specific named targets | **PASS** — STEP 1 (top-level dirs), STEP 2 (src/services/…), STEP 3 (package.json/yaml/toml), STEP 4 (CLAUDE.md/roles); anchored, countable, specific |
| **C-42** | Full-window compliance: C-39 + C-40 + C-41 simultaneously present | **PASS** — pre-execution count (C-39), numbered traversal in P2 (C-41), gate tokens at boundaries (C-40) all active |

**V-01 Score: 420 / 420**

**Excellence signal**: ROLE ARCHITECTURE block enforces a hard separation between raw-signal capture (Signal Surveyor: rows only, no pivot) and pivot decision (Org Architect: annotations and enumeration, no new rows). The explicit handoff emit line ("Signal Surveyor complete. [n] rows recorded. Handoff to Org Architect.") is a new artifact type — a state-transition acknowledgement within a phase, not at a phase boundary. This prevents the main failure mode: conflating inventory with selection, which produces circular pivot rationale.

---

### V-02 — Output Format

| Criterion group | Assessment |
|----------------|------------|
| **C-01–C-25** | **PASS all** — structural base identical to V-01 |
| **C-26–C-34** | **PASS all** — manifest, contract table, ENTRY/EXIT, predicates structurally identical |
| **C-35** | **PASS** — blockquote predicates present |
| **C-36** | **PASS** — VIOLATION column present |
| **C-37** | **PASS** — test-item counts 2/5/6/1 in contract table; Phase 3 count 6 matches IVR-P3-A through P3-F (even with extended IVR-P3-B, count unchanged) |
| **C-38** | **PASS** — TOTAL=14, sum=14 |
| **C-39** | **PASS** — pre-execution verification block identical to V-01 |
| **C-40** | **PASS** — gate token protocol and terminal token lines present |
| **C-41** | **PASS** — 4-step SCAN PROTOCOL with named targets |
| **C-42** | **PASS** — all three compliance layers present |

**V-02 Score: 420 / 420**

**Excellence signal (axis)**: `signal-strength:` field (H/M/L derived from Phase 2 Org Relevance column) on every YAML team entry. This is a provenance-propagation pattern: Phase 2 inventory's confidence rating travels forward into Phase 3 YAML, giving reviewers a signal-quality indicator at confirmation time without re-reading the inventory table. The amend options table format (Option / Action / Command / Consequence) adds a fourth column — Consequence — that pairs each amend choice with its downstream effect, making amend impact scannable without reading the command.

---

### V-03 — Phrasing Register

| Criterion group | Assessment |
|----------------|------------|
| **C-01–C-25** | **PASS all** — all 14 IVR triples present; INVARIANT/VIOLATION structure intact; third element is REMEDIATION: rather than REPAIR:. Structural surface preserved; phrasing variant does not drop any triple element. |
| **C-26–C-34** | **PASS all** — manifest, contract table, structural layout unchanged |
| **C-35** | **PASS** — blockquote predicates present |
| **C-36** | **PASS** — VIOLATION column present |
| **C-37** | **PASS** — test-item count column present and correct |
| **C-38** | **PASS** — cross-manifest count invariant holds |
| **C-39** | **PASS** — CROSS-MANIFEST VERIFICATION block present with arithmetic; uses "Emit:" directive |
| **C-40** | **PASS** — GATE TOKEN PROTOCOL present; tokens appear as final lines of Completion Assertions blocks |
| **C-41** | **PASS** — 4-step SCAN PROTOCOL with named targets present |
| **C-42** | **PASS** — all three compliance layers present simultaneously |
| **C-30** | **PARTIAL** — C-30 requires "(2) YES/NO checklist completion test block". V-03 uses PASS/FAIL format ("Assert IVR-P1-A: … PASS / FAIL") throughout. The semantic is preserved but the literal checklist format specified by C-30 is absent. Evidence: every completion block reads "PASS / FAIL" where C-30 mandates "YES / NO". **5/10 pts** |

**V-03 Score: 415 / 420**

**Notes**: The phrasing register axis (Assert:/Execute:/Verify:/Emit: prefixes; REMEDIATION: for REPAIR:) is coherent and unambiguous. However, the YES→PASS substitution in checklist items constitutes a structural deviation from C-30's literal requirement. The axis would require a companion criterion that blesses PASS/FAIL as an equivalent format — without it, V-03 pays a small penalty.

---

### V-04 — Lifecycle + Inertia Framing

| Criterion group | Assessment |
|----------------|------------|
| **C-01–C-25** | **PASS all** |
| **C-26–C-34** | **PASS all** — manifest, table, ENTRY/EXIT all present |
| **C-35** | **PASS** — blockquote predicates |
| **C-36** | **PASS** — VIOLATION column |
| **C-37** | **PASS** — test-item counts correct |
| **C-38** | **PASS** — cross-manifest invariant holds |
| **C-39** | **PASS** — pre-execution verification block present |
| **C-40** | **PASS** — gate tokens as final completion test lines |
| **C-41** | **PASS** — 4-step SCAN PROTOCOL |
| **C-42** | **PASS** — all three compliance layers |
| **C-29** | **PASS** — 3-part ENTRY blocks (REQUIRED-INPUTS/REQUIRED-STATES/FORBIDDEN-STATES) remain structurally paired ENTRY blocks; EXIT directives present in all completion tests |

**V-04 Score: 420 / 420**

**Excellence signals**: Two axes both fire. (1) **3-part ENTRY blocks** expand the precondition surface from a single condition to three named sections. FORBIDDEN-STATES is particularly strong — it names conditions that must be absent, not just conditions that must be present, making phase-skip visible via a negative precondition check. (2) **Inertia framing** names the actual failure mode in the opening: "The inertia competitor is tribal knowledge: org structure that is real but undocumented." This reframes the skill output from invention to legibility, reducing hallucinated structure by grounding the model in the claim that signal already exists. The `replaces: undocumented tribal org structure` YAML header carries the inertia frame into the artifact.

---

### V-05 — Combined (Role Sequence + Output Format + Inertia Framing)

| Criterion group | Assessment |
|----------------|------------|
| **C-01–C-25** | **PASS all** — highest compliance surface of any variation: roles enforce non-conflation, inertia framing suppresses invention, 3-part ENTRY blocks maximize precondition specificity |
| **C-26** | **PASS** |
| **C-27** | **PASS** |
| **C-28** | **PASS** — 14-label manifest, count row |
| **C-29** | **PASS** — 3-part ENTRY + EXIT present on all phases |
| **C-30** | **PASS** — YES/NO checklist (not PASS/FAIL) preserved |
| **C-31** | **PASS** — three independent audit surfaces |
| **C-32** | **PASS** — contract table as front-matter |
| **C-33** | **PASS** — predicate before ENTRY on all phases |
| **C-34** | **PASS** — TOTAL row |
| **C-35** | **PASS** — blockquote predicates |
| **C-36** | **PASS** — VIOLATION column |
| **C-37** | **PASS** — test-item count column; P3 count=6 correct even with extended IVR-P3-B |
| **C-38** | **PASS** — TOTAL(14) = P1(2)+P2(5)+P3(6)+P4(1)=14 |
| **C-39** | **PASS** — pre-execution arithmetic verification block in preamble |
| **C-40** | **PASS** — typed gate tokens as final lines of P2/P3 completion tests |
| **C-41** | **PASS** — 4-step SCAN PROTOCOL anchored to specific named targets (Signal Surveyor role) |
| **C-42** | **PASS** — all three windows covered: count verification before P1 (C-39), traversal discipline during P2 (C-41), gate tokens at transitions (C-40) |

**V-05 Score: 420 / 420**

**Excellence signals**: All three axes operate on independent failure modes: role separation prevents corpus-conflation, signal-strength propagates provenance confidence, FORBIDDEN-STATES blocks phase-skip via negative preconditions. The combination is additive, not redundant. The AMEND table's Consequence column ("Restarts Phase 2; Signal Surveyor re-runs all 4 SCAN PROTOCOL steps" / "signal-strength: values and detected-from: fields preserved") is the most actionable amend section of any round — it tells the reviewer what the downstream effect is before they commit to the amend.

---

### Composite Scores

| Variation | Score | % | Key axis |
|-----------|-------|---|----------|
| **V-05** | **420 / 420** | **100%** | Role + signal-strength + inertia (3 axes) |
| V-04 | 420 / 420 | 100% | Lifecycle + inertia (2 axes) |
| V-02 | 420 / 420 | 100% | signal-strength + amend table (2 axes) |
| V-01 | 420 / 420 | 100% | Role sequence (1 axis, high-impact) |
| V-03 | 415 / 420 | 98.8% | Phrasing register (PASS/FAIL checklist deviates from C-30 YES/NO requirement) |

**Ranking**: V-05 > V-04 = V-02 = V-01 > V-03

V-05 is the candidate to beat. It covers all three primary failure modes simultaneously — hallucinated structure (role separation prevents corpus→pivot conflation), provenance loss (signal-strength propagates confidence from inventory to YAML), and phase-skip (FORBIDDEN-STATES explicitly names precondition absences) — while satisfying all 42 rubric criteria without format deviations.

---

### Excellence Signals (New Patterns)

**From V-01 / V-05 — Role authority separation:**
Signal Surveyor and Org Architect operate as named roles within Phase 2 with a declared handoff artifact. The Surveyor has authority to ADD rows only; the Architect has authority to ANNOTATE and PIVOT only. The constraint "may not add new Signal rows — only the Signal Surveyor may add rows" enforces a hard boundary that the model cannot traverse without violating a stated rule. This is a stronger non-conflation guard than ordering alone.

**From V-02 / V-05 — Signal-strength provenance propagation:**
`signal-strength: [H|M|L]` on every YAML team entry, derived from Phase 2 Org Relevance column. The field makes the confidence gradient of the inventory visible at the artifact level. A reviewer can identify which teams are strong-signal (H) vs marginal (L) without re-reading the Phase 2 table. Candidate for C-43: "Every team entry in YAML carries signal-strength: field derived from Phase 2 Org Relevance, making inventory confidence available at artifact surface."

**From V-04 / V-05 — FORBIDDEN-STATES as negative precondition:**
ENTRY blocks structured as REQUIRED-INPUTS / REQUIRED-STATES / FORBIDDEN-STATES. FORBIDDEN-STATES is the new signal: it names conditions that must be ABSENT before a phase begins (e.g., "any YAML block in output so far", "GATE-1 FAIL TOKEN in output"). Positive preconditions require evidence of readiness; negative preconditions require absence of prior failure signals. Together they bracket the entry window from both sides. Candidate for C-43 or C-44.

**From V-04 / V-05 — Inertia competitor named in opening:**
Naming tribal knowledge as the inertia competitor sets an epistemic frame: the scan is reading existing structure, not inventing it. This suppresses hallucination by making invention an error condition rather than a valid mode. The `replaces:` YAML header carries the frame into the artifact. These are advisory framing elements, not rubric criteria, but they reduce the frequency of the hallucination failure mode that earlier IVR triples were designed to catch after-the-fact.

**From V-02 / V-05 — Amend table with Consequence column:**
The amend options table format (Option / Action / Command / Consequence) adds a fourth column naming the downstream effect of each choice. This makes amend impact scannable without reading the command or inferring from context. The V-05 Consequence column explicitly notes role effects ("Signal Surveyor re-runs all 4 SCAN PROTOCOL steps") and field preservation ("signal-strength: values and detected-from: fields preserved"), connecting amend choices to the compliance machinery.

---

```json
{"top_score": 420, "all_essential_pass": true, "new_patterns": ["role authority separation: Signal Surveyor (add rows only) / Org Architect (annotate and pivot only) with explicit handoff artifact prevents corpus-conflation failure mode", "signal-strength field (H/M/L derived from Phase 2 Org Relevance) propagates inventory confidence into YAML artifact surface for reviewer prioritization", "FORBIDDEN-STATES as third section of ENTRY block names conditions that must be absent before phase begins, bracketing entry window with negative preconditions alongside positive ones", "inertia competitor (tribal knowledge) named in opening framing reframes scan from invention to legibility, suppressing hallucinated structure at the prompt-context level", "amend table Consequence column pairs each amend option with its downstream compliance effect making impact scannable without reading commands"]}
```
