Now I have everything needed. Let me perform the full QU5 simplification analysis.

---

## Simplification Analysis

### Step 1: Identify Dead Weight

The winning prompt (R20 V-01, "Lifecycle Emphasis") serves two masters: the 5 essential criteria, and a dense stack of aspirational/recommended criteria (C-11 through C-39). Separating them reveals which text serves which.

**Doing NO work for C-01 through C-05:**

| Removed Element | Reason |
|---|---|
| `"You are executing the **org-build** skill."` | Skill name is known from invocation. Zero constraint force. |
| `"Generate a complete org from scan results or directly from a repo."` | Commentary. Preamble already lists outputs. |
| GLOBAL CONSTANTS section — TABLE-A / CONST-1 entire (~210 words) | Verbatim IA scope templates only enforce C-17 (aspirational). C-03 requires the role file EXISTS, not that its scope matches a template. |
| GLOBAL CONSTANTS section — TABLE-B / CONST-2 entire (~50 words) | Category derivation table only enforces C-10/C-12 (aspirational). Essential criteria don't require anti-pattern category compliance. |
| GLOBAL CONSTANTS `FORBIDDEN: re-defining or embedding...` | Guards TABLE-A/B re-use. Tables removed; guard has no referent. |
| Lifecycle anchor paragraphs (Phase 2/3/4) — `"Phase N uses Phase N-1 gate outputs..."` | Commentary prose. The FORBIDDEN directives already enforce the ordering. 3 instances × ~15 words each = ~45 words. |
| Duplicate FORBIDDEN at phase start (before Input Contract) | Each appears once before Input Contract AND once inside Input Contract. Triple repetition. 3 instances = ~36 words. |
| Gate section `**Outbound**: FORBIDDEN:` + `**Inbound at Phase N+1**: FORBIDDEN:` | Third and fourth redundant statements of the same phase-boundary guard. 3 phases × 2 lines × ~12 words = ~72 words. |
| `PHASE-ORDERING-GUARD:` inside record blocks | Fourth restatement of same FORBIDDEN (already in lifecycle anchor, Input Contract, Constraints, and Gate section). 3 instances × ~10 words = ~30 words. |
| RECORD blocks entirely (`=== RECORD: PHASE-N ===`) | Record blocks enforce C-20/C-24/C-26/C-28/C-33/C-36 (aspirational). Essential criteria make no reference to typed gate outputs. |
| Input Contract tables (Phase 2/3/4) | Contract tables enforce C-32/C-33 (aspirational). Essential criteria don't require variable provenance to be declared. |
| T3-ROLE-OUTCOME composite token definition (~24 words) | Enforces C-38 (aspirational). |
| Constraints sections — sub-step-level FORBIDDENs that duplicate phase-level FORBIDDENs | E.g., `FORBIDDEN: beginning sub-step AREA before completing sub-step COUNT` duplicates the Constraints summary line `MUST complete sub-steps in order`. ~50 words. |
| Output Checklist entirely (~130 words) | Verification aid. No enforcement. The constraints already cover every item. |
| Sub-step 2-C CONST-1 lookup instruction | References CONST-1 which is removed. Replace with: five-field MUST. |
| Sub-step 3-C CONST-2 reference and `cat-N` syntax requirement | References CONST-2 (removed). Aspirational. |
| `"Terminal phase. No downstream gate required."` | True but does nothing. |

---

### Step 2: Simplified Prompt

```markdown
org-build

Produces:
- `org-chart.md` — ASCII hierarchy (min 2 levels), headcount table (Area | Headcount | Key Roles | Decides | Escalates), operating rhythm, committee charters, anti-pattern watch, org evolution roadmap, inertia verdict block
- `.craft/roles/{area}/{role}.md` — one file per role with: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`

Depth modes: standard (20–30 roles, default) | deep (50+ roles, via `--depth deep`)

---

## Phase 1 — Structural Verdict

1. Read `--depth` flag: `deep` → T1-DEPTH-FLAG = `deep`; absent → `standard`.
2. Examine repo for structural pressure indicators.
3. Assign exactly one T2-PRESSURE (NONE / LOW / MODERATE / HIGH / CRITICAL). One only — multiple or none is an error.
4. Derive T2-VERDICT: NONE or LOW → `CAN-OPERATE-FLAT`; MODERATE–CRITICAL → `STRUCTURE-WARRANTED`. One only — both or neither is an error.

FORBIDDEN: beginning Phase 2 before Phase 1 is complete.

---

## Phase 2 — Role Enumeration

FORBIDDEN: beginning Phase 2 before Phase 1 is complete.

- T1-DEPTH-FLAG = `standard`: MUST enumerate 20–30 roles.
- T1-DEPTH-FLAG = `deep`: MUST enumerate 50+ roles.
- MUST include exactly one role with `inertia` or `advocate` in its name.
- MUST group roles into area subdirs (min 2). Every role assigned to exactly one area.
- MUST write `.craft/roles/{area}/{role}.md` for every role. Every file MUST contain: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.

FORBIDDEN: beginning Phase 3 before Phase 2 is complete.

---

## Phase 3 — Org-Chart Assembly

FORBIDDEN: beginning Phase 3 before Phase 2 is complete.

Write `org-chart.md` containing:
1. ASCII box-and-line hierarchy (min 2 levels)
2. Headcount table: `Area` | `Headcount` | `Key Roles` | `Decides` | `Escalates`
3. Anti-pattern watch table
4. Org evolution roadmap (2+ rows; row 1 = headcount threshold trigger; row 2 = different trigger type)
5. Inertia assessment block: `FLAT-CASE-PRESSURE: [value]` + exactly one verdict. One only — both or neither is an error. Values MUST match Phase 1 outputs.

FORBIDDEN: beginning Phase 4 before Phase 3 is complete.

---

## Phase 4 — Operating Rhythm and Committee Charters

FORBIDDEN: beginning Phase 4 before Phase 3 is complete.

1. Operating rhythm table: 3+ rows. Row 1 = ROB. Row 2 = shiproom or execution cadence. Row 3 = governance meeting.
2. Committee charter per governance row: Name, Purpose, Cadence, Owner, Quorum (expressed as `N of M`).
FORBIDDEN: Quorum as percentage or plain number.
```

---

### Step 3: Essential Criteria Verification

| Criterion | Pass Condition | Evidence in Simplified |
|---|---|---|
| **C-01** org-chart.md with ASCII hierarchy | File exists, ASCII diagram, min 2 levels | Preamble: "ASCII hierarchy (min 2 levels)". Phase 3 item 1: "ASCII box-and-line hierarchy (min 2 levels)" | **PASS** |
| **C-02** All five role fields | orientation, lens, expertise, scope, collaborates_with in every file | Preamble lists all 5. Phase 2: "Every file MUST contain: orientation, lens, expertise, scope, collaborates_with" | **PASS** |
| **C-03** inertia-advocate always present | Role file with inertia or advocate exists | Phase 2: "MUST include exactly one role with `inertia` or `advocate` in its name" | **PASS** |
| **C-04** Role count within depth range | standard 20–30, deep 50+ | Phase 1 detects T1-DEPTH-FLAG. Phase 2: explicit MUST per flag value | **PASS** |
| **C-05** Headcount table (Decides/Escalates) | Columns include Decides/Escalates | Preamble and Phase 3 item 2 both specify all 5 columns explicitly | **PASS** |

**All essential criteria: 5/5 PASS** ✓

---

### Step 4: What Was Removed and Why

| Category | Words Removed | Reason |
|---|---|---|
| GLOBAL CONSTANTS block (TABLE-A + TABLE-B + header) | ~270 | Serves aspirational C-17, C-10, C-12 only. C-03 requires role file presence, not scope content match. |
| RECORD blocks (3 phases) | ~90 | Serve aspirational C-20/C-24/C-26/C-28/C-33. Essential criteria make no reference to typed gate outputs. |
| Input Contract tables (3 phases) | ~130 | Serve aspirational C-32/C-33. Variable provenance tracking not required for C-01–C-05. |
| Lifecycle anchor paragraphs (3 phases) | ~50 | Commentary restating constraints already expressed as FORBIDDEN. Zero additive constraint force. |
| Redundant FORBIDDEN repetitions (outbound/inbound at gates) | ~100 | Each phase boundary had 4 statements of the same prohibition. 2 remain per boundary (before/after). |
| PHASE-ORDERING-GUARD inside record blocks | ~30 | Fourth restatement of the phase-boundary prohibition. Record blocks removed anyway. |
| Output Checklist | ~130 | Verification aid. Every item already enforced by constraints above. |
| T3-ROLE-OUTCOME composite token definition | ~25 | Serves aspirational C-38. Not referenced by essential criteria. |
| Duplicate sub-step FORBIDDENs in Constraints | ~50 | `FORBIDDEN: beginning sub-step AREA before COUNT` duplicates the Constraints ordering summary. |
| Opening "You are executing..." and intro prose | ~20 | Skill name known from invocation. Commentary. |
| **Total removed** | **~895** | |

**Original word count (R19 V-02 complete analog + R20 V-01 additions):** ~1,750  
**Simplified word count:** ~355  
**Reduction:** ~80%

**Note on the 20–40% expectation:** The gap exceeds expectation because the winning prompt was engineered to pass 25/31 aspirational criteria (C-11–C-39). Every one of those is removable for essential-only purposes. The essential criteria require only: produce the files, include the fields, include the role, hit the count floor, include the headcount columns. Nothing in CONST-1, CONST-2, record blocks, Input Contracts, or the Output Checklist touches those five requirements.

---

```json
{"simplified_word_count": 355, "original_word_count": 1750, "all_essential_still_pass": true}
```
