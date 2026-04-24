## Round 3 Scoring — topic:plan (Rubric v3)

---

### V-01: Sentinel `??` Tokens in Pre-Committed Schemas

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Read strategy.md | PASS | Step 1 requires filling Schema A and quoting "at least one concrete sentence from strategy.md" |
| C-02 | Signal inventory | PASS | Schema B (artifact filenames + dates) + Schema C (all 9 rows pre-committed with `??`) |
| C-03 | Delta detection | PASS | Schema D (NEW/PRIOR partition) + Schema E (templated sentence); "[N] and [M] must be integers" |
| C-04 | Typed change proposals | PASS | Schema F: "Action must be exactly ADD, REMOVE, or REPRIORITIZE"; labeled null declarations per type |
| C-05 | Confirmation gate | PASS | Step 6: explicit YES/NO/REVISED gate; "Stop. Write nothing further until the user replies." |
| C-06 | Evidence citation | PASS | "Evidence artifact must be a filename from the NEW list in Schema D" |
| C-07 | Before/after diff | PASS | Schema G pre-committed; "If proposals exist, fill Schema G" |
| C-08 | Inertia justification | PASS | "vs. NO CHANGE must state the specific consequence of NOT changing; a generic claim is not sufficient" |
| C-09 | Type-labeled null declarations | PASS | ADDITIONS/REMOVALS/REPRIORITIZATIONS labeled separately with specific reasons |
| C-10 | Conflict detection | FAIL | No conflict audit phase or null form present |
| C-11 | Required-cell table schemas | PASS | "Do not replace any table with prose. Do not merge tables." — all schemas pre-printed |
| C-12 | In-phase stop gates | PARTIAL | Global final scan for `??` at Step 6; per-step "do not advance" only at Step 3 stop condition; not per-phase |
| C-13 | Mandatory column enforcement | FAIL | Inertia column not labeled "mandatory" with its own header |
| C-14 | Explicit placeholder tokens | PASS | `??` vs `--` two-tier distinction; pre-printed in all 7 schemas; "A `??` remaining is a machine-detectable gap" |
| C-15 | Counted-total delta summary | PASS | Schema E: `Strategy was written on ??. ?? artifacts are NEW. ?? are PRIOR.` with integer enforcement |
| C-16 | Hedge-phrase disqualification | FAIL | "A generic claim is not sufficient" — no named blacklist; escape hatch remains open |

**Score**: (5/5 × 60) + (3/3 × 30) + (4.5/8 × 10) = 60 + 30 + **5.6** = **95.6**
All essential: YES | Golden: YES

---

### V-02: Conversational + Named Banned-Phrase Blacklist

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Read strategy.md | PASS | Step 1: "A direct quote (at least one full sentence) from strategy.md" |
| C-02 | Signal inventory | PASS | Step 2: table schema with filenames + dates; all 9 namespaces enumerated |
| C-03 | Delta detection | PASS | Step 3: delta summary sentence with STRATEGY DATE named; "[N] and [M] must be plain integers" |
| C-04 | Typed change proposals | PARTIAL | Action column present but not explicitly restricted to ADD/REMOVE/REPRIORITIZE in table schema; null declarations imply the types but don't enforce the column |
| C-05 | Confirmation gate | PASS | Step 6: explicit YES/NO/REVISED gate; "Stop. Do not write anything else until the user replies." |
| C-06 | Evidence citation | PASS | Evidence artifact column in proposal table |
| C-07 | Before/after diff | PASS | "If proposals exist, also write a before/after diff" with table schema |
| C-08 | Inertia justification | PASS | "Why this beats NO CHANGE" column; requires naming specific consequence |
| C-09 | Type-labeled null declarations | PASS | ADDITIONS/REMOVALS/REPRIORITIZATIONS labeled null declarations with specific reasons required |
| C-10 | Conflict detection | FAIL | No conflict audit |
| C-11 | Required-cell table schemas | PARTIAL | Proposal and artifact tables have schemas; namespace audit is described as prose ("Write '0 artifacts — ABSENT'"), not a pre-committed table |
| C-12 | In-phase stop gates | FAIL | No per-phase "do not advance" gates |
| C-13 | Mandatory column enforcement | FAIL | No "mandatory" labeling |
| C-14 | Explicit placeholder tokens | FAIL | No `??` sentinels |
| C-15 | Counted-total delta summary | PASS | Step 3: exact templated sentence required with integer enforcement |
| C-16 | Hedge-phrase disqualification | PASS | Inline named blacklist: "compelling reason", "clearly warranted", "update is needed", "obvious improvement", etc. — 8 phrases banned at proposal gate |

**Score**: (4.5/5 × 60) + (3/3 × 30) + (3.5/8 × 10) = 54 + 30 + **4.4** = **88.4**
All essential: NO (C-04 partial) | Golden: NO

---

### V-03: DELTA SUMMARY as Standalone Gated Phase

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Read strategy.md | PASS | Phase 1 deliverable: file path + date + quote; Phase 1 exit gate requires both |
| C-02 | Signal inventory | PASS | Phase 2: inventory table + namespace audit, all 9 rows; exit gate: "Any missing namespace row is a gate failure" |
| C-03 | Delta detection | PASS | Phase 3 sole deliverable is DELTA SUMMARY BLOCK; exact date from Phase 1 STRATEGY DATE |
| C-04 | Typed change proposals | PASS | Phase 5: "ADD / REMOVE / REPRIORITIZE" explicitly named in table schema; null declarations per type |
| C-05 | Confirmation gate | PASS | Phase 6: explicit YES/NO/REVISED; "Stop. Write nothing further until the user replies." |
| C-06 | Evidence citation | PASS | "Only filenames from the NEW artifacts line of the DELTA SUMMARY BLOCK may appear in the Evidence artifact column" |
| C-07 | Before/after diff | PASS | "If proposals exist, also produce a before/after diff" with table schema |
| C-08 | Inertia justification | PASS | "vs. NO CHANGE: [specific consequence of NOT changing]" required per row |
| C-09 | Type-labeled null declarations | PASS | Labeled null declarations per type required |
| C-10 | Conflict detection | FAIL | No conflict audit |
| C-11 | Required-cell table schemas | PASS | Phases 2 and 5 use pre-defined table schemas |
| C-12 | In-phase stop gates | PASS | Each phase ends: "Do not advance to Phase N without passing this gate." with specific exit conditions |
| C-13 | Mandatory column enforcement | FAIL | No column labeled "mandatory" |
| C-14 | Explicit placeholder tokens | FAIL | No `??` sentinels in schemas |
| C-15 | Counted-total delta summary | PASS | Phase 3 DELTA SUMMARY BLOCK is the sole deliverable; "Writing 'a few', 'several', 'some', or any non-integer value... is a gate failure" |
| C-16 | Hedge-phrase disqualification | FAIL | "Specific consequence" required but no named banned-phrase list |

**Score**: (5/5 × 60) + (3/3 × 30) + (4/8 × 10) = 60 + 30 + **5.0** = **95.0**
All essential: YES | Golden: YES

---

### V-04: Defense Register + Sentinel Tokens

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Read strategy.md | PASS | Step 1: "Quote at least one complete sentence from strategy.md"; fills STRATEGY FILE and DATE with `??` replacement |
| C-02 | Signal inventory | PASS | Step 3: artifact table + namespace audit, all 9 rows pre-printed with `??` |
| C-03 | Delta detection | PASS | Step 4: delta sentence with exact integers; strategy date from Step 1 |
| C-04 | Typed change proposals | PASS | Step 6: "ADD" explicitly named; null declarations enumerate ADDITIONS/REMOVALS/REPRIORITIZATIONS; "CANDIDATE ADDITION" terminology present |
| C-05 | Confirmation gate | PASS | Step 7: explicit YES/NO/REVISED gate; "Stop. Write nothing further until the user replies." |
| C-06 | Evidence citation | PASS | Step 5 challenge table maps artifact to dimension; Step 6 evidence artifact column with enforcement |
| C-07 | Before/after diff | PASS | "If proposals exist, produce a before/after diff" with Schema `??`-prefilled |
| C-08 | Inertia justification | PASS | "vs. NO CHANGE cell must name the defense argument from Step 2 that the NEW artifact defeated" — strongest per-row inertia linkage in any variation |
| C-09 | Type-labeled null declarations | PASS | "ADDITIONS: none — Step 2 defenses held..." per type |
| C-10 | Conflict detection | FAIL | No conflict audit |
| C-11 | Required-cell table schemas | PASS | All steps use `??`-pre-printed tables; implicit "no prose substitution" via sentinel system |
| C-12 | In-phase stop gates | PARTIAL | Step 2 defense register: "Complete this table in full before reading any signal artifact" is a hard pre-signal gate; final `??` scan at Step 7; but no per-step "do not advance" declarations for all steps |
| C-13 | Mandatory column enforcement | FAIL | Inertia column not labeled "mandatory" |
| C-14 | Explicit placeholder tokens | PASS | `??` in all tables; `??` vs `--` distinction explained; final scan instruction |
| C-15 | Counted-total delta summary | PASS | Step 4: exact templated sentence with integer requirement |
| C-16 | Hedge-phrase disqualification | PASS | Step 6: "BANNED phrases" list with 5 named phrases including "no change needed", "compelling reason", "clearly warranted" |

**Score**: (5/5 × 60) + (3/3 × 30) + (5.5/8 × 10) = 60 + 30 + **6.9** = **96.9**
All essential: YES | Golden: YES

---

### V-05: Full Combination

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Read strategy.md | PASS | Phase 1 fills Schema A; exit gate: "STRATEGY DATE is recorded as YYYY-MM-DD AND a direct quote from strategy.md appears. If either missing, re-read and retry." |
| C-02 | Signal inventory | PASS | Phase 2: Schema B (inventory) + Schema C (all 9 rows pre-printed `??`); exit gate: "Any missing namespace row is a gate failure" |
| C-03 | Delta detection | PASS | Phase 3: Schema D is sole deliverable; "[N] and [M] must be integers. Writing 'several', 'a few', 'some'... is a gate failure." |
| C-04 | Typed change proposals | PASS | Schema E explicitly for ADDITIONS; Schema F explicitly for REMOVALS/REPRIORITIZATIONS — type enforcement is structural, not column-label-only; exit gate requires null declarations for all three types |
| C-05 | Confirmation gate | PASS | Phase 7: explicit YES/NO/REVISED gate; "Stop. Write nothing further until the user replies." |
| C-06 | Evidence citation | PASS | Phase 6 exit gate: "Every evidence artifact in Schema E and Schema F appears in Schema D NEW artifacts list. A PRIOR filename in the Evidence column is a gate failure." |
| C-07 | Before/after diff | PASS | Schema G pre-committed; "Fill Schema G (before/after diff) for each row in Schema E and Schema F" |
| C-08 | Inertia justification | PASS | Opening premise: "NO CHANGE is the default outcome"; Phase 6 reminder: "NO CHANGE is the default verdict"; "vs. NO CHANGE" column requires naming what would go wrong |
| C-09 | Type-labeled null declarations | PASS | Phase 6 exit gate explicitly requires: "Null declarations for all three change types are present"; specific topic-grounded reasons required |
| C-10 | Conflict detection | PASS | Schema H (conflict audit) pre-committed with `??`-prefilled rows; null form: "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts." |
| C-11 | Required-cell table schemas | PASS | 8 pre-committed schemas; "No table may be replaced by prose. No table may be omitted." |
| C-12 | In-phase stop gates | PARTIAL | Phases 1, 2, 3, 6 have explicit "Do not advance to Phase N without passing this gate." declarations; Phases 4, 5, 7, 8 have no per-phase gate instructions |
| C-13 | Mandatory column enforcement | FAIL | "vs. NO CHANGE" column is structurally required but not labeled "(MANDATORY)" with a standalone header distinct from the column name |
| C-14 | Explicit placeholder tokens | PASS | All 8 schemas pre-printed with `??`; `??` vs `--` two-tier distinction defined; Phase 7 scan: "Scan all schemas for remaining `??` tokens. Resolve any before displaying." |
| C-15 | Counted-total delta summary | PASS | Schema D is the sole deliverable of Phase 3; exact integers enforced at gate; "Strategy was written on ??. ?? artifacts are NEW. ?? are PRIOR." with integer gate failure clause |
| C-16 | Hedge-phrase disqualification | PASS | Phase 6: "BANNED phrases" inline at proposal gate with 7 named phrases; note extends ban to null declarations: "'No change needed' is not acceptable as a null reason." |

**Score**: (5/5 × 60) + (3/3 × 30) + (6.5/8 × 10) = 60 + 30 + **8.1** = **98.1**
All essential: YES | Golden: YES

---

## Rankings

| Rank | Variation | Essential | Rec | Asp | Score | Golden |
|------|-----------|-----------|-----|-----|-------|--------|
| 1 | V-05 | 5/5 | 3/3 | 6.5/8 | **98.1** | YES |
| 2 | V-04 | 5/5 | 3/3 | 5.5/8 | **96.9** | YES |
| 3 | V-01 | 5/5 | 3/3 | 4.5/8 | **95.6** | YES |
| 4 | V-03 | 5/5 | 3/3 | 4.0/8 | **95.0** | YES |
| 5 | V-02 | 4.5/5 | 3/3 | 3.5/8 | **88.4** | NO |

---

## Excellence Signals from V-05

**1. Typed-schema split for proposal types** — Separate Schema E (ADDITIONS) and Schema F (REMOVALS/REPRIORITIZATIONS) makes change-type enforcement structural rather than column-label-only. An empty additions schema is visually self-evident without requiring a null declaration; the null declaration then serves as cross-verification.

**2. Two-tier gap tokens (`??` vs `--`)** — The `??`/`--` distinction separates "not yet filled" from "genuinely absent." A model can leave `--` in a namespace row without that being a detectable error; `??` remaining is specifically flagged as a gap. Prior variations had only one concept of emptiness, making mechanical gap scanning ambiguous.

**3. Phase 6 exit gate bundles all three closure properties in one place** — The single gate checks: (a) all evidence artifacts are in the NEW list, (b) no banned phrases remain in any cell, (c) null declarations for all three types are present. This means the gate is the integration point for C-06, C-16, and C-09 simultaneously — a model cannot pass the gate by satisfying only two of them.

**4. Banned-phrase list extends to null declarations explicitly** — "Note: 'No change needed' is not acceptable as a null reason." This is the only variation that closes the null-declaration escape hatch, not just the proposal escape hatch. V-02 and V-04 ban phrases in the proposal column only; V-05's note applies the ban structurally across both contexts.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["two-tier gap tokens (??=unfilled vs --=genuinely absent) separate cognitive gap from structural absence, enabling unambiguous machine scanning without human diff-reading", "typed-schema split for proposal types (separate schemas for ADDITIONS vs REMOVALS/REPRIORITIZATIONS) makes null enforcement structural — an empty schema is self-evident before a null declaration is checked"]}
```
