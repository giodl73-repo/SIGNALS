## topic:plan — Scoring Report (Round 1, V-01 through V-05)

> **Note**: V-03, V-04, V-05 prompts were not included in this run. V-02 appears truncated at Step 3 of an incomplete multi-step prompt. Scores reflect prompt text as provided.

---

### V-01 — Output Format (Rigid Table Schema)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Read strategy.md | **PASS** | Phase 1 explicitly says "Read simulations/topic/strategy.md" and requires a filled inventory table with version, date, gaps, and signal count |
| C-02 | Signal inventory | **PASS** | Phase 2 table lists all 9 namespaces by name; requires artifact filenames with dates; "All 9 namespaces must appear even if no artifacts exist" |
| C-03 | Delta detection | **PASS** | Phase 3 uses "only NEW rows from Phase 2"; Phase 2 defines NEW/PRIOR/NONE relative to strategy date |
| C-04 | Typed change proposals | **PASS** | Phase 4 requires ADD/REMOVE/REPRIORITIZE column; "Silence is not acceptable. Every type must have at least one proposal row or one null declaration row." |
| C-05 | Confirmation gate | **PASS** | Phase 6 presents explicit YES/NO/REVISED gate; "Do NOT modify strategy.md until the user responds" |
| C-06 | Evidence citation | **PASS** | Phase 4 table has "Evidence artifact" as a required column in the row schema |
| C-07 | Before/after diff | **PASS** | Phase 4 table has explicit "Before" and "After" columns in row schema |
| C-08 | Inertia justification | **PASS** | Phase 4 requires "mandatory inertia column" with header "Why NO CHANGE is insufficient" |
| C-09 | Type-labeled null declarations | **PASS** | Phase 4 shows three separate labeled rows: `ADD — NULL`, `REMOVE — NULL`, `REPRIORITIZE — NULL` |
| C-10 | Conflict detection | **PASS** | Phase 5 has its own conflict audit table with explicit null form: `CONFLICT DETECTION — NULL` |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**

---

### V-02 — Phrasing Register (Conversational Imperative)

> **Warning**: Prompt is truncated at Step 3. Steps covering change proposals (C-04), confirmation gate (C-05), and aspirational criteria (C-09, C-10) are absent from the provided text. Scored as-received.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Read strategy.md | **PASS** | Step 1: "Read simulations/topic/strategy.md right now. Quote the strategy's declared date and version." |
| C-02 | Signal inventory | **PASS** | Step 2 lists all 9 namespaces by name; "Name every artifact you found and give its date. Say NONE if you found nothing. Do not skip a namespace." |
| C-03 | Delta detection | **PASS** | Step 3: "The strategy has a date. Any artifact created after that date is NEW. Anything before is PRIOR." Strategy date anchored. |
| C-04 | Typed change proposals | **FAIL** | Step 4+ not present in provided text |
| C-05 | Confirmation gate | **FAIL** | Not present in provided text |
| C-06 | Evidence citation | **FAIL** | No proposal structure visible |
| C-07 | Before/after diff | **FAIL** | Not present |
| C-08 | Inertia justification | **FAIL** | Not present |
| C-09 | Type-labeled null declarations | **FAIL** | Not present |
| C-10 | Conflict detection | **FAIL** | Not present |

**Essential**: 3/5 | **Recommended**: 0/3 | **Aspirational**: 0/2
**Score**: (3/5 × 60) + (0/3 × 30) + (0/2 × 10) = **36**

---

### V-03, V-04, V-05 — Not Provided

Prompt text for these variations was not included in this scoring run. Cannot evaluate.

---

### Variation Rankings

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-01 | **100** | YES |
| 2 | V-02 | **36** | NO (truncated + 2 essential fail) |
| — | V-03 | N/A | — |
| — | V-04 | N/A | — |
| — | V-05 | N/A | — |

---

### Excellence Signals (from V-01)

1. **Required-cell table schemas** — every phase uses a table where blank cells are visually obvious violations; prose allows elision, tables do not
2. **In-phase stop gates** — "Do not proceed until you have filled every cell" creates hard phase boundaries that prevent skipping
3. **Mandatory column enforcement** — the inertia column is labeled "mandatory" with its own header row, making omission detectable
4. **Typed null declarations by label** — `ADD — NULL` / `REMOVE — NULL` / `REPRIORITIZE — NULL` are separate rows, not a single "nothing to do" statement; this satisfies C-09 structurally
5. **Conflict detection as a dedicated phase** — moving conflict audit to its own numbered phase with its own null form prevents it from being buried or omitted

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["required-cell table schemas make omission visually obvious", "in-phase stop gates prevent phase skipping", "typed null declarations by label satisfy aspirational criteria structurally", "conflict detection as a dedicated numbered phase with own null form"]}
```
