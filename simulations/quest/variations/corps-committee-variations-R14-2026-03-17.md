```
DECLARE YES if found. INJECT Inertia-Advocate as Tier 1 if not found.
  ENFORCE (injected): cites at least one INERTIA-FINDING-* label in voice.
  ENFORCE (injected): appears in ## STANCE MANIFEST.
  FAILS [C-46]: Phase 3 begins without INERTIA CONTINUITY BRIDGE present
  FAILS [C-49]: YES declared when no qualifying participant exists in TIER SORT

---

**ROLE VOICE GUARD fill rule [C-37 Mechanism 2 for C-02]:**

PRINT ROLE VOICE GUARD table -- one row per Phase 0 participant.
ASSIGN In-scope domain from charter orientation.
ASSIGN Forbidden-topic scope -- the domain this role must NOT lead as primary concern.
  ENFORCE examples:
    PM: in-scope adoption/user value; FORBIDDEN deployment topology, on-call burden
    SRE: in-scope reliability/incident surface; FORBIDDEN product vision, business strategy
    Architect: in-scope trade-offs/technical debt; FORBIDDEN customer NPS, market positioning
PRINT ROLE VOICE SEAL.
VALIDATE each Phase 3 voice against forbidden-topic scope.
  FAILS [C-02]: voice leads with forbidden-topic concern
    [C-37: detectable from ROLE VOICE GUARD table AND from TIER-N-SEQUENCE-COMMIT independently]
  FAILS [C-37]: ROLE VOICE GUARD table absent -- single-mechanism C-02 enforcement only
  FAILS [C-37]: forbidden-topic scope cells empty throughout table

---

**PHASE 3 fill rules:**

ENFORCE SEQUENTIAL TIER GATE [C-37 Mechanism 1 for C-02]:
  REQUIRE TIER-1-SEQUENCE-COMMIT before any Tier 2 voice.
  REQUIRE TIER-2-SEQUENCE-COMMIT before any Tier 3 voice.
  FAILS [C-02]: Tier N+1 voice appears before TIER-N-SEQUENCE-COMMIT
  FAILS [C-25]: TIER-N-SEQUENCE-COMMIT absent despite correct ordering

VALIDATE STANCE cell: BLOCK / CONDITION / APPROVE only; no qualifications.
  FAILS [C-02]: stance embedded in prose without STANCE field in table row
  FAILS [C-02]: qualified value such as `CONDITION (pending)` in stance cell

REQUIRE Tier 1 rows: INERTIA-FINDING cite cell populated with named label.
REQUIRE Tier 2 rows: Condition cell names specific approval condition.
  FAILS [C-07]: "address concerns" in Condition cell -- not a specific deliverable
REQUIRE Tier 3 rows: RESPONDS-TO: "[named concern]" opens Primary concern cell; CITE populated.

VALIDATE at least one CONDITION or BLOCK in ## STANCE MANIFEST.
  REOPEN Phase 2 if all-APPROVE.

WRITE ## STANCE MANIFEST table. WRITE STANCE INVARIANT.
  FAILS [C-47]: STANCE INVARIANT absent from STANCE MANIFEST block
PRINT PHASE-3-COMMIT with bidirectionality clause (both directions named).
  FAILS [C-45]: one coupling direction only

---

**PHASE 4 fill rules:**

TALLY from ## STANCE MANIFEST STANCE-TOKEN column only. DO NOT re-parse prose.
DERIVE OUTCOME:
  All APPROVE -> APPROVED
  Any CONDITION, no BLOCK -> APPROVED WITH CONDITIONS
  Any BLOCK -> BLOCKED or DEFERRED
VALIDATE counts match ## STANCE MANIFEST exactly.

---

**PHASE 5 fill rules:**

WRITE Verdict matching OUTCOME exactly.
WRITE Conditions as specific deliverables -- "address concerns" fails.
REQUIRE (verdict not APPROVED): Owner (named role, Phase 0 roster) AND Trigger
  (named artifact + recipient + authority).
  FAILS [C-23]: Owner or Trigger absent when verdict not APPROVED

PRINT ACTION ITEMS table. POPULATE all three columns per row.
  FAILS [C-04]: Owner Role cell empty -- column structure violation [Mechanism 1]
  FAILS [C-04]: Deadline cell empty -- column structure violation

PRINT OWNERSHIP TALLY [C-37 Mechanism 2 for C-04]:
  FORMAT: "[N] action items. Named owners: [N]. Anonymous items: [0 required]."
  VALIDATE total in TALLY = ACTION ITEMS row count.
  VALIDATE Anonymous items = 0; REOPEN Phase 5 if nonzero.
  FAILS [C-37]: OWNERSHIP TALLY absent -- single-mechanism C-04 enforcement only
  FAILS [C-04]: TALLY count less than ACTION ITEMS row count
    [C-37: Owner column shows empty cell; Tally shows count gap -- two independent signals]

WRITE DISSENTING OPINIONS table -- one row per CONDITION/BLOCK stance.
  REQUIRE if no dissent: `[No dissent | [reason all agreed] | -- | -- | --]`
  FAILS [C-05]: CONDITION or BLOCK in Phase 3 but no dissent row present

---

**AMEND fill rules (C-30, C-33, C-34):**

ROUTE AMEND through block dependency graph:
  | Amendment Type           | Invalidates            | Re-execution scope  |
  |--------------------------|------------------------|---------------------|
  | Add attendee             | Phase 0, Phase 3       | Phase 0 -> Phase 3+ |
  | Change scope             | Phase 0 -> Phase 5     | Full re-execution   |
  | Change committee type    | Phase 0 -> Phase 5     | Full re-execution   |
  | Inject role post-Phase 2 | Phase 3 -> Phase 5     | Phase 3 -> Phase 5  |

MARK all stale sites before re-execution:
  [Phase -- table -- column -- token -- reason stale]
  FAILS [C-33]: stale site not marked before re-execution proceeds

EMIT RECOMMIT MANIFEST before each downstream phase resumes:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta: cells added: [list], cells removed: [list], cells modified: [list]
    Version: v[K+1] supersedes v[K].
    Gate: downstream phases gate on v[K+1] only; v1 seal is insufficient after AMEND.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST after AMEND
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND has been issued
```

---

## Structural Diff Summary

| Section | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| BEFORE YOU START imperative block | Descriptive | Descriptive | **Direct imperative** | Descriptive | **Direct imperative** |
| FAILS SYNTAX TEMPLATE self-referential entries | **SELF-REFERENTIAL section** | CORRECT: examples only | CORRECT: examples only | **SELF-REFERENTIAL section** | **SELF-REFERENTIAL section** |
| PHASE-1-COMMIT forward annotation (skeleton) | Absent | **Present** | Absent | **Present** | **Present** |
| PHASE-1 fill rule C-41 annotation | Absent | **Present** | Absent | **Present** | **Present** |
| Fill rule phrasing register | Mixed | Mixed | **Uniform imperative** | Mixed | **Uniform imperative** |
| C-40 addressable | YES | NO | NO | YES | YES |
| C-41 addressable | NO | YES | NO | YES | YES |
| Register ambiguity eliminated | NO | NO | YES | NO | YES |

**Single-axis isolation:**
- V-01 tests C-40 alone: does the self-referential section in the template make C-38/C-39 violation detection criterion-knowledge-independent?
- V-02 tests C-41 alone: does the skeleton-level forward annotation make a weak PHASE-1-COMMIT detectable before Phase 2 fill rules are reached?
- V-03 tests register alone: does uniform imperative phrasing affect compliance with C-13, C-14, or C-15 independent of C-40/C-41?

**Expected scoring pattern:**
- V-01: PASS C-40, FAIL C-41
- V-02: FAIL C-40, PASS C-41
- V-03: FAIL C-40, FAIL C-41 — but strongest on C-13 and phrasing-sensitive criteria
- V-04: PASS C-40, PASS C-41 — combined without register change
- V-05: PASS C-40, PASS C-41 — full integration; expected highest composite
