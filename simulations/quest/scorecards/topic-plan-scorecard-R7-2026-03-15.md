## topic:plan — Round 7 Scorecard

**Rubric v7 | New criterion: C-27 (write-surface enforcement completeness)**

---

### Per-Variation Scoring

---

#### V-01 — Role Sequence: PRE-COMMIT BLOCK + SCHEMA BOUNDARY BLOCK + Inline Null Templates

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Read strategy.md | PASS | Phase 0 reads TOPICS.md → strategy.md; Schema A extracts dimensions |
| C-02 | Signal inventory | PASS | Schema B (filenames + dates) + Schema C (all 9 rows) |
| C-03 | Delta detection | PASS | Phase 3 NEW/PRIOR split; mandatory sentence names strategy date |
| C-04 | Typed change proposals | PASS | Schemas E/F with ADD/REMOVE/REPRIORITIZE; typed null declarations |
| C-05 | Confirmation gate | PASS | PENDING CONFIRMATION + YES/NO/REVISED gate; Phase 6 sealed |
| C-06 | Evidence citation | PASS | Evidence artifact column in Schema E/F; SCOPE requirement |
| C-07 | Before/after diff | PASS | Schema G; Before/After columns in E/F |
| C-08 | Inertia justification | PASS | vs. NO CHANGE — MANDATORY column; burden on change |
| C-09 | Type-labeled null declarations | PASS | ADD—NULL / REMOVE—NULL / REPRIORITIZE—NULL templates, all three labeled |
| C-10 | Conflict detection | PASS | Schema H; CONFLICT DETECTION — NULL typed null |
| C-11 | Required-cell table schemas | PASS | Schemas DR, A, B, C, D, E, F, G, H all tabular |
| C-12 | In-phase stop gates | PASS | "Do not advance to Phase N" on every gate |
| C-13 | Mandatory column enforcement | PASS | "vs. NO CHANGE — MANDATORY" labeled in E/F headers |
| C-14 | Explicit placeholder tokens | PASS | `??` defined; VIOLATION-1 names blank-when-`??` |
| C-15 | Counted-total delta summary | PASS | "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR." |
| C-16 | Hedge-phrase disqualification | PASS | BANNED OUTPUT FORMS with exact strings; match = disqualified |
| C-17 | Two-tier sentinel vocabulary | PASS | `??` (open obligation) vs `--` (closed decision) defined |
| C-18 | Pre-signal defense register | PASS | Schema DR before artifact reads; each E/F row cites defeated defense |
| C-19 | Integer-enforcement gate language | PASS | "Writing 'a few', 'several'... is a gate failure" |
| C-20 | Sequential phase-linked stop gates | PASS | All gates name next phase: "Do not advance to Phase N+1" |
| C-21 | Vocabulary contract violation enumeration | PASS | VIOLATION-1, -2, -3 each named with specific condition |
| C-22 | Row-number anchor citation | PASS | "Defense defeated (Row D-R-N)"; named defense without row number disqualified |
| C-23 | Verbatim-quoted banned forms | PASS | All banned strings in quoted form |
| C-24 | Cell-level banned-forms check instruction | PASS | SCHEMA BOUNDARY BLOCK steps 1–4; "Only then present the cell" |
| C-25 | Banned-forms scope propagation | PASS | WS-3 CHECK inside each null template applies banned forms to reason cells |
| C-26 | Gate-0 pre-signal stop gate | PASS | Gate 0 named; "READ-BARRIER ACTIVE until Gate 0 PASS" reiterated in Phase 0 |
| C-27 | Write-surface enforcement completeness | PASS | WS-1: PRE-COMMIT BLOCK before everything, strongest placement; WS-2: SCHEMA BOUNDARY BLOCK labeled header in schema section between D and E; WS-3: inline WS-3 CHECK inside each template with verbatim strings |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 19/19 → 10
**Score: 100**

---

#### V-02 — Output Format: Three WS-Blocks as First-Class Section Headers

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01–C-08 | All essential + recommended | PASS | Same core structure |
| C-09 | Type-labeled null declarations | PASS | Three separate null templates |
| C-10 | Conflict detection | PASS | Schema H; typed null |
| C-11 | Required-cell table schemas | PASS | All schemas tabular |
| C-12 | In-phase stop gates | PASS | Explicit on all gates |
| C-13 | Mandatory column enforcement | PASS | "vs. NO CHANGE — MANDATORY" in headers |
| C-14 | Explicit placeholder tokens | PASS | `??` / `--` defined with violations |
| C-15 | Counted-total delta summary | PASS | Mandatory templated sentence |
| C-16 | Hedge-phrase disqualification | PASS | BANNED OUTPUT FORMS list |
| C-17 | Two-tier sentinel vocabulary | PASS | `??` / `--` both defined |
| C-18 | Pre-signal defense register | PASS | Schema DR pre-committed; E/F cite D-R-N |
| C-19 | Integer-enforcement gate language | PASS | "Writing 'a few'... is a gate failure" |
| C-20 | Sequential phase-linked stop gates | PASS | Explicit phase references on all gates |
| C-21 | Vocabulary contract violation enumeration | PASS | VIOLATION-1, -2, -3 |
| C-22 | Row-number anchor citation | PASS | D-R-N column; named defense without row number disqualified |
| C-23 | Verbatim-quoted banned forms | PASS | All strings quoted |
| C-24 | Cell-level banned-forms check instruction | PASS | WS-2 BOUNDARY BLOCK steps 1–4; fires at boundary |
| C-25 | Banned-forms scope propagation | PASS | WS-3 NULL BLOCK inside each template applies to reason cells |
| C-26 | Gate-0 pre-signal stop gate | PASS | Gate 0 present; sequential to Phase 1 |
| C-27 | Write-surface enforcement completeness | PASS | WS-1: WS-1 GATE BLOCK section header positioned between schemas and Phase 0 — fires before Phase 0 actions; WS-2: WS-2 BOUNDARY BLOCK section header at schema D/E boundary in schema section; WS-3: WS-3 NULL BLOCK embedded inside each null declaration template. All three at correct write surfaces. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 19/19 → 10
**Score: 100**

---

#### V-03 — Lifecycle Emphasis: WRITE SURFACE REGISTER + Milestone Annotations

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01–C-08 | All essential + recommended | PASS | Full structure present |
| C-09 | Type-labeled null declarations | PASS | Three templates in [WS-3 MILESTONE] |
| C-10 | Conflict detection | PASS | Schema H; typed null |
| C-11–C-16 | Table schemas, gates, mandatory, sentinels, delta, hedge | PASS | All present |
| C-17 | Two-tier sentinel vocabulary | PASS | `??` / `--` |
| C-18 | Pre-signal defense register | PASS | Schema DR; E/F D-R-N citations |
| C-19 | Integer-enforcement gate language | PASS | Named banned count forms as gate failure |
| C-20 | Sequential phase-linked stop gates | PASS | All gates reference next phase |
| C-21 | Vocabulary contract violation enumeration | PASS | VIOLATION-1, -2, -3 |
| C-22 | Row-number anchor citation | PASS | D-R-N column with explicit disqualification rule |
| C-23 | Verbatim-quoted banned forms | PASS | All strings quoted |
| C-24 | Cell-level banned-forms check instruction | PASS | [WS-2 MILESTONE] check block at schema boundary with explicit steps |
| C-25 | Banned-forms scope propagation | PASS | [WS-3 MILESTONE] check fires inside each null template |
| C-26 | Gate-0 pre-signal stop gate | PASS | Gate 0 in sequential chain |
| C-27 | Write-surface enforcement completeness | PASS | WRITE SURFACE REGISTER upfront declares all three sites before any phase. WS-1 MILESTONE fires at Phase 0 entry (first instruction before any strategy.md read). WS-2 MILESTONE is labeled header at Schema D/E boundary in schema section. WS-3 MILESTONE inside null declaration fill section with per-template checks. Register creates verifiable contract; milestones confirm each site. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 19/19 → 10
**Score: 100**

---

#### V-04 — Phrasing Register + Inertia Framing: WHY-Motivated Enforcement

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01–C-08 | All essential + recommended | PASS | Full structure present |
| C-09 | Type-labeled null declarations | PASS | Three templates |
| C-10 | Conflict detection | PASS | Schema H |
| C-11–C-16 | Table schemas, gates, mandatory, sentinels, delta, hedge | PASS | All present |
| C-17 | Two-tier sentinel vocabulary | PASS | `??` / `--` |
| C-18 | Pre-signal defense register | PASS | Schema DR with WHY: motivation |
| C-19 | Integer-enforcement gate language | PASS | Named banned count forms |
| C-20 | Sequential phase-linked stop gates | PASS | Phase references present |
| C-21 | Vocabulary contract violation enumeration | PASS | VIOLATION-1, -2, -3 |
| C-22 | Row-number anchor citation | PASS | D-R-N column |
| C-23 | Verbatim-quoted banned forms | PASS | Strings quoted |
| C-24 | Cell-level banned-forms check instruction | PASS | Schema D/E BOUNDARY check steps 1–4 in schema section |
| C-25 | Banned-forms scope propagation | PASS | WS-3 ENFORCEMENT inside each null template |
| C-26 | Gate-0 pre-signal stop gate | PASS | Gate 0 present with sequential link |
| C-27 | Write-surface enforcement completeness | FAIL | WS-1 fires as first instruction INSIDE Phase 0 — there is no upfront read-barrier declaration before Phase 0 begins. No governing architecture block; no register declaring WS-1 before Phase 0 entry. The WHY: motivations are interpretive rather than declarative. An auditor cannot verify C-27 by scanning for a named, placed block — they must interpret the WS-1 ENFORCEMENT label inside Phase 0 and the WHY: text. WS-2 and WS-3 satisfy individually (C-24, C-25), but WS-1's placement does not satisfy "before Phase 0 actions." Completeness is not independently verifiable without interpretation. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 18/19 → 9.47
**Score: 99**

---

#### V-05 — Combined: WRITE-SURFACE ARCHITECTURE as Structural Skeleton

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01–C-08 | All essential + recommended | PASS | Full structure present |
| C-09 | Type-labeled null declarations | PASS | Three labeled WSA-3 templates |
| C-10 | Conflict detection | PASS | Schema H; typed null |
| C-11 | Required-cell table schemas | PASS | All schemas tabular; ARCHITECTURE block in prose section only |
| C-12 | In-phase stop gates | PASS | All gates with "Do not advance to Phase N" |
| C-13 | Mandatory column enforcement | PASS | "vs. NO CHANGE — MANDATORY" in E/F |
| C-14 | Explicit placeholder tokens | PASS | `??` / `--` with VIOLATION-1 through -4 (extends to D-R-N citations) |
| C-15 | Counted-total delta summary | PASS | Mandatory templated sentence |
| C-16 | Hedge-phrase disqualification | PASS | BANNED OUTPUT FORMS; "check cells before presenting — not after" |
| C-17 | Two-tier sentinel vocabulary | PASS | `??` / `--` with full violation enumeration |
| C-18 | Pre-signal defense register | PASS | Schema DR; E/F D-R-N row citations |
| C-19 | Integer-enforcement gate language | PASS | Integer enforcement block with explicit banned forms |
| C-20 | Sequential phase-linked stop gates | PASS | All gates reference next phase |
| C-21 | Vocabulary contract violation enumeration | PASS | VIOLATION-1 through -4; VIOLATION-4 adds D-R-N citation gap |
| C-22 | Row-number anchor citation | PASS | D-R-N column; `??` required if unknown; `--` not acceptable |
| C-23 | Verbatim-quoted banned forms | PASS | All strings quoted with "exact-match patterns" caveat |
| C-24 | Cell-level banned-forms check instruction | PASS | WSA-2 CELL-LEVEL CHECK BLOCK Steps 1–4; explicit pre-fill instruction |
| C-25 | Banned-forms scope propagation | PASS | WSA-3 check fires inside each null template; "not exempt" stated in architecture |
| C-26 | Gate-0 pre-signal stop gate | PASS | Gate 0 in sequential chain; WSA-1 barrier active until Gate 0 PASS |
| C-27 | Write-surface enforcement completeness | PASS | WRITE-SURFACE ARCHITECTURE declares all three primitives before schemas or phases — the architecture block IS the "read-barrier declaration before Phase 0 actions naming Gate 0" (WSA-1 condition field: "Gate 0 written and passing before any artifact read"). Phase 0 instantiates WSA-1 with explicit reference "[WSA-1 ENFORCEMENT — per ARCHITECTURE block]." WSA-2 block is at Schema D/E boundary in schema section, explicitly names the failure mode: "A check that appears only at Gate 5 or in preamble text does not satisfy WSA-2." WSA-3 inside each null template, checks reference architecture. Gate 6 verifies all three WSA conditions as explicit gate criteria. Architecture is independently auditable without interpretation. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 19/19 → 10
**Score: 100**

---

### Rankings

| Rank | Variation | Score | C-27 |
|------|-----------|-------|------|
| 1 | **V-05** | 100 | PASS — governing architecture; WSA-2 names its own failure mode; Gate 6 audits completeness |
| 2 | V-03 | 100 | PASS — register/milestone pattern; strong independent verifiability via pre-declared register |
| 3 | V-01 | 100 | PASS — strongest WS-1 placement (before all schemas); PRE-COMMIT BLOCK + Phase 0 reiteration |
| 4 | V-02 | 100 | PASS — section headers visible in outline; WS-1 GATE BLOCK immediately before Phase 0 |
| 5 | V-04 | 99 | FAIL — no governing architecture; WS-1 fires inside Phase 0 with no prior declaration; completeness requires interpretation |

---

### Excellence Signals from V-05

**New patterns not present in prior rounds:**

1. **Governing-contract architecture** — The WRITE-SURFACE ARCHITECTURE block is declared before all schemas and phases, making it the binding commitment against which all three enforcement sites are verified. Each site explicitly references it by name: `[WSA-N ENFORCEMENT — per ARCHITECTURE block above]`. C-27 becomes the skeleton, not a checklist item.

2. **Self-defeating failure mode citation at the enforcement site** — WSA-2 names its own disqualifying alternative inline: *"A check that appears only at Gate 5 or in preamble text does not satisfy WSA-2 — this block at this location is the required implementation site."* The failure mode is described at the enforcement point itself, not in a preamble.

3. **Final-gate architecture audit** — Gate 6 condition explicitly verifies: *"write-surface architecture complete (WSA-1 at Phase 0, WSA-2 at Schema D/E boundary, WSA-3 in null templates)"* — the architectural completeness check is the last gate before user output, creating a closing verification loop.

4. **Vocabulary contract extensibility** — VIOLATION-4 adds a new case (`??` required for D-R-N citation gaps; `--` not acceptable for required citations), showing the violation enumeration is open for extension as new required columns are added.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["governing-contract architecture block declared before all schemas and phases with each enforcement site referencing it by name", "self-defeating failure mode citation at the enforcement site names the alternative that does not satisfy", "final-gate architecture completeness audit verifies all three WSA sites as explicit gate condition"]}
```
