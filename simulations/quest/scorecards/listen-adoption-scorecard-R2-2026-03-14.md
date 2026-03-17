No golden file yet. Scoring proceeds from rubric and prompt analysis.

---

## Quest Score — `listen-adoption` R2

### Rubric Reference (v2)

| ID | Weight | Criterion Summary |
|----|--------|-------------------|
| C-01 | essential (12) | All 16 stock roles mapped to Rogers archetype |
| C-02 | essential (12) | >=3 month time steps, Rogers order preserved |
| C-03 | essential (12) | Chasm named + feature-specific bridging (drawn from EM Named Inertia) |
| C-04 | essential (12) | >=2 interventions ranked by H/M/L adoption delta |
| C-05 | essential (12) | >=2 champion roles with archetype-grounded rationale |
| C-06 | recommended (10) | Churn risk: named trigger + mitigation for >=2 archetypes |
| C-07 | recommended (10) | Feature-specific spread mechanism per archetype transition |
| C-08 | recommended (10) | Structured/scannable month view (table or labeled headers) |
| C-09 | aspirational (5) | Two scenarios with named levers (optimistic/pessimistic) |
| C-10 | aspirational (5) | >=2 measurable signal-readiness indicators + abort signal |
| C-11 | aspirational (5) | Named inertia per archetype (>=3 archetypes, feature-specific, non-generic) |
| C-12 | aspirational (5) | No orphan or conditional sections (all C-01–C-10 sections unconditional) |

---

### V-01 — Inertia as fourth column in archetype table

| Criterion | Result | Pts | Evidence |
|-----------|--------|-----|----------|
| C-01 | PASS | 12 | All 16 roles listed in table template with explicit `[archetype]` placeholders; generic requirement stated |
| C-02 | PASS | 12 | Step 2 M1–M5 table; "at least 3 distinct time steps" required; Rogers sequence stated |
| C-03 | PASS | 12 | Step 3a explicitly instructs drawing from Named Inertia entries for EM roles; feature-specific bridging required |
| C-04 | PASS | 12 | Step 5 ranked table; H/M/L scale defined in-prompt with delta meaning; "descending delta order" enforced |
| C-05 | PASS | 12 | Step 3c champion table; "rationale must connect archetype position to credibility with Early Majority cluster" |
| C-06 | PASS | 10 | Step 4 churn register; named trigger required; "frame churn triggers in terms of reversion to Named Inertia" |
| C-07 | PASS | 10 | Step 2 explicitly requires feature-specific mechanism; "generic word of mouth fails — at least one transition must cite a mechanism tied to this feature context" |
| C-08 | PASS | 10 | Step 2 M1–M5 table template shown in-prompt; scannable by construction |
| C-09 | PASS | 5 | Step 6 requires two scenarios each naming a different lever; "labeling a scenario without naming the lever fails this section" — no conditional qualifier |
| C-10 | PASS | 5 | Step 7 requires >=2 measurable proceed signals and >=1 abort; no qualifier |
| C-11 | PARTIAL | 4 | Named Inertia column structure is strong with generic-entry rejection and passing example; however no GATE checkpoint blocks progress if model produces attitude statements — lower enforcement confidence than V-04 |
| C-12 | PASS | 5 | All 7 steps present and unconditional; R2 removes the "if confident" qualifier from R1 V-01 Step 7; all C-01–C-10 sections covered |

**Composite: 109** | All essential pass: **YES**

---

### V-02 — GATE chain extended to all 12 criteria + META-GATE

| Criterion | Result | Pts | Evidence |
|-----------|--------|-----|----------|
| C-01 | PASS | 12 | GATE A requires all 16 roles; each appears exactly once |
| C-02 | PASS | 12 | GATE B requires >=3 time steps; Rogers sequence blocking |
| C-03 | PASS | 12 | GATE C requires "EM Named Inertia entries from SECTION A are cited"; bridging mechanism must address those entries specifically |
| C-04 | PASS | 12 | GATE E requires >=2 entries + delta labels + descending order |
| C-05 | PASS | 12 | GATE C requires >=2 champion rows with archetype-grounded bridge rationale |
| C-06 | PASS | 10 | GATE D requires >=2 rows; trigger framed as "event that causes role to revert to Named Inertia behavior" |
| C-07 | PASS | 10 | GATE B requires feature-specific mechanism "specific to this feature context or the EM roles Named Inertia" |
| C-08 | PASS | 10 | GATE B with M1–M5 table template shown; GATE D... scannable |
| C-09 | PASS | 5 | GATE F requires two scenarios each naming a different lever; META-GATE item C-09 audits this |
| C-10 | PASS | 5 | GATE G requires >=2 measurable proceed + >=1 abort; META-GATE item C-10 audits |
| C-11 | PASS | 5 | GATE A requires feature-specific Named Inertia column; META-GATE item C-11 explicitly checks "at least 3 archetypes have distinct, non-generic entries" — strongest C-11 mechanism |
| C-12 | PASS | 5 | META-GATE item C-12 explicitly scans for "if applicable," "if confident," "optional," "if time permits," "if relevant"; blocking before artifact write |

**Composite: 110** | All essential pass: **YES**

---

### V-03 — Imperative command phrasing (no table template, no GATE)

| Criterion | Result | Pts | Evidence |
|-----------|--------|-----|----------|
| C-01 | PASS | 12 | "All 16 must be assigned an archetype before the timeline begins"; cast list explicit |
| C-02 | PASS | 12 | PART 2 requires "at least 3 distinct months"; Rogers sequence inversion prohibited |
| C-03 | PASS | 12 | PART 3a draws from Part 1 named behaviors of EM roles; feature-specific required |
| C-04 | PASS | 12 | PART 5 requires >=2 interventions ranked descending; H/M/L scale defined |
| C-05 | PASS | 12 | PART 3c requires >=2 champions; rationale connects archetype position AND EM roles named inertia — most explicit C-05 requirement across all variations |
| C-06 | PASS | 10 | PART 4 requires named event/condition trigger + reversion link to Part 1 behavior + mitigation |
| C-07 | PASS | 10 | "Feature-specific grounding required. Word of mouth as the only mechanism fails." |
| C-08 | PARTIAL | 5 | "Present with clearly labeled month headers or a timeline table" instruction present, but no table template shown in prompt — prose drift risk explicitly noted by variation author; model has more execution freedom than V-01/V-02/V-04/V-05 |
| C-09 | PASS | 5 | PART 6 requires two scenarios each naming a different lever; "labeling a scenario without naming the lever fails this section" |
| C-10 | PASS | 5 | PART 7 requires >=2 measurable signals + >=1 abort; concrete format example given |
| C-11 | PASS | 5 | "State specifically what this role does today instead of this feature. This is a named behavior -- not an attitude." Per-role command with explicit generic-entry rejection; all 16 rows commanded, covering all 5 archetypes |
| C-12 | PASS | 5 | All 7 PARTS present and unconditional; no conditional qualifiers found |

**Composite: 103** | All essential pass: **YES**

---

### V-04 — Inertia column + GATE chain (combined, expected winner)

| Criterion | Result | Pts | Evidence |
|-----------|--------|-----|----------|
| C-01 | PASS | 12 | GATE A requires all 16 roles; each to exactly one of 5 canonical archetypes |
| C-02 | PASS | 12 | GATE B requires >=3 time steps; Rogers sequence blocking |
| C-03 | PASS | 12 | GATE C requires EM Named Inertia cited as explanation; bridging mechanism "directly addresses those EM inertia entries" |
| C-04 | PASS | 12 | GATE E requires >=2 entries + delta labels + descending order; each intervention "names a specific Named Inertia entry or friction from SECTION A or SECTION C" |
| C-05 | PASS | 12 | GATE C requires >=2 champion rows with archetype-grounded bridge rationale |
| C-06 | PASS | 10 | GATE D requires trigger framed as "event that causes reversion to Named Inertia behavior"; no "monitor adoption" mitigation accepted |
| C-07 | PASS | 10 | GATE B requires "at least one mechanism must name something tied to the Named Inertia entries in SECTION A" |
| C-08 | PASS | 10 | M1–M5 table template shown; GATE B enforces timeline as primary SECTION B output |
| C-09 | PASS | 5 | GATE F requires two scenarios with named levers; "scenarios differ on which Named Inertia entries hold or break" adds comparison dimension |
| C-10 | PASS | 5 | GATE G requires >=2 measurable proceed signals + >=1 abort; no vague signals accepted |
| C-11 | PASS | 5 | GATE A blocks on generic attitude statements — "entry must describe a behavior, workflow, or tool"; table column enforced by structural template + GATE stop |
| C-12 | PASS | 5 | All GATEs mandatory and unconditional; prompt explicitly states "Do not skip, merge, or mark any section optional or conditional" |

**Composite: 110** | All essential pass: **YES**

---

### V-05 — GATE sections + 12-item self-audit with explicit pass conditions

| Criterion | Result | Pts | Evidence |
|-----------|--------|-----|----------|
| C-01 | PASS | 12 | SECTION A table with all 16 roles; self-audit item C-01 verifies exactly 16 rows and all 5 archetype labels present |
| C-02 | PASS | 12 | SECTION B requires >=3 time steps; Rogers sequence; self-audit item C-02 verifies |
| C-03 | PASS | 12 | SECTION C names chasm; self-audit item C-03 verifies "chasm" appears + feature-specific bridging |
| C-04 | PASS | 12 | SECTION E ranked interventions with delta; self-audit item C-04 verifies |
| C-05 | PASS | 12 | SECTION C champion table; self-audit item C-05 verifies >=2 rows with archetype-to-EM credibility rationale |
| C-06 | PASS | 10 | SECTION D churn register; self-audit item C-06 verifies named trigger (not "may churn") + mitigation |
| C-07 | PASS | 10 | SECTION B requires feature-specific mechanism "directly address a Named Inertia entry"; self-audit item C-07 verifies |
| C-08 | PASS | 10 | M1–M5 table template shown; self-audit item C-08 verifies scannable format |
| C-09 | PASS | 5 | SECTION F two scenarios with named levers; self-audit item C-09 verifies both name different levers |
| C-10 | PASS | 5 | SECTION G measurable signals; self-audit item C-10 verifies concrete/trackable |
| C-11 | PASS | 5 | Self-audit item C-11: "Count the archetypes that have a feature-specific Named Inertia entry... Is the count >=3?" — forces explicit archetype-level quality count, most targeted C-11 mechanism |
| C-12 | PASS | 5 | Self-audit item C-12: scans for "if applicable," "if confident," "optional," "if time permits," "you may skip," "if data is available," "if relevant" — most exhaustive forbidden-phrase list |

**Composite: 110** | All essential pass: **YES**

---

### Ranking

| Rank | Variation | Composite | All Essential | C-11 | C-12 | Key Differentiator |
|------|-----------|-----------|---------------|------|------|---------------------|
| 1 | V-02 GATE + META-GATE | 110 | YES | PASS | PASS | META-GATE audits C-11 archetype count + C-12 phrase scan before write |
| 1 | V-04 Inertia column + GATE | 110 | YES | PASS | PASS | Structural column + GATE chain; EM inertia cross-referenced in C and E |
| 1 | V-05 GATE + self-audit | 110 | YES | PASS | PASS | Self-audit forces archetype count for C-11; most exhaustive forbidden-phrase list for C-12 |
| 4 | V-01 Inertia column only | 109 | YES | PARTIAL | PASS | Structural column without GATE checkpoint reduces C-11 enforcement confidence |
| 5 | V-03 Imperative commands | 103 | YES | PASS | PASS | C-08 PARTIAL: no table template shown; prose drift risk noted by author |

---

### Excellence Signals — R2

**1. Named Inertia column as forward-propagating reference data (V-01, V-04).** Moving inertia from a standalone narrative (R1 V-04 Section 0 pattern) into a structural column in Section A creates a data entry that GATE C (chasm analysis) and GATE E (interventions) must explicitly cite. C-11 now does triple duty: satisfies C-11 directly, sharpens C-03 specificity (chasm is grounded in named EM inertia), and grounds C-04 interventions (each names the inertia it fights). A standalone inertia section front-loads the essay without enforcing downstream accountability.

**2. Archetype-count threshold in final audit (V-02, V-05).** Both top-scoring variations require an explicit count of archetypes with feature-specific Named Inertia entries (must reach >=3) in the final audit/META-GATE step. This is more reliable than trusting role-level completeness to satisfy archetype-level coverage — a model could produce 16 role entries but with only 2 archetypes having non-generic inertia, and no GATE without the count check would catch it.

**3. Forbidden-phrase scan as C-12 mechanism (V-02, V-05).** Listing specific disqualifying phrases ("if applicable," "if confident," "optional," "if time permits") and requiring the model to scan its own output before artifact write is more robust than structural section presence alone. A section can exist but be conditionalized; the phrase scan catches that failure mode. V-05 has the most exhaustive list (6 phrases including "you may skip" and "if data is available").

**4. GATE chain with Named Inertia cross-referencing (V-04).** V-04's GATE design creates inertia-awareness at three sequential checkpoints: GATE A (define inertia), GATE C (cite EM inertia in chasm explanation), GATE E (name inertia in each intervention). This enforces the inertia column's data propagation mechanically — the model cannot satisfy the later GATEs without having completed the earlier ones with feature-specific entries.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["Named Inertia column as forward-propagating reference data: inertia defined in Section A is cross-referenced by GATE C (chasm) and GATE E (interventions), making C-11 coverage do triple duty without a standalone section", "Archetype-count threshold in final audit: requiring explicit count of archetypes with feature-specific inertia (>=3) is more reliable than trusting role-level completeness to satisfy archetype-level coverage", "Forbidden-phrase scan as C-12 mechanism: listing specific disqualifying phrases and requiring model to scan output before artifact write catches conditionalized sections that structural presence checks miss"]}
```
