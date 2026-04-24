## Org-Chart Variate — Round 12 Scorecard

**Rubric:** v12 (C-01 through C-32) | **Denominator:** /24 aspirational | **Date:** 2026-03-16

---

### Evaluation Method

These are skill prompts, not output documents. Scoring evaluates whether each variation's directives **enforce** the required behaviors — not whether a sample output exists. The dependency chain is evaluated top-down; a failing dependency auto-fails all dependent criteria.

---

### Criteria Pass/Fail Analysis

#### Essential (C-01 through C-05)

All five variations carry identical essential-section directives. No variation introduces a change to essential structure.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-01 | Inertia precedes org | PASS | PASS | PASS | PASS | PASS | Gate 2 (`INERTIA COMPLETE`) blocks org diagram until VERDICT written |
| C-02 | Org hierarchy readable | PASS | PASS | PASS | PASS | PASS | `DO show at minimum two levels. DO NOT produce a flat list of names` |
| C-03 | Roles input honored | PASS | PASS | PASS | PASS | PASS | ROLES-LOADED / ROLES-NOTE logic with explicit fallback prose |
| C-04 | Headcount by area | PASS | PASS | PASS | PASS | PASS | `DO include at minimum two area rows` with `**Total**` row required |
| C-05 | Operating rhythm table | PASS | PASS | PASS | PASS | PASS | `DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting` |

**Essential: 5/5 all variations**

---

#### Recommended (C-06 through C-08)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-06 | Committee charters complete | PASS | PASS | PASS | PASS | PASS | V-01–V-04: four fields enforced; V-05: five fields — Purpose/Membership/Decides/Escalates still present; C-06 requires "at minimum three charter elements" (purpose, membership, authority), not exactly four |
| C-07 | All four output sections | PASS | PASS | PASS | PASS | PASS | Section order lists confirm all four: inertia / org diagram / headcount / rhythm |
| C-08 | Decision rights indicated | PASS | PASS | PASS | PASS | PASS | Separate Decides/Escalates columns enforced; `DO NOT use a single Decision Scope column` |

**Recommended: 3/3 all variations**

---

#### Aspirational (C-09 through C-32)

**Dependency pre-check:** The chain C-09→C-17→C-19, C-10→C-18→C-20→C-21→C-22→C-23→C-26, C-11→C-14→C-30, C-12→C-16, C-15→C-22, C-22→C-23→C-26, C-21+C-22→C-25→C-27→C-28→C-31, C-25→C-32 must all hold. Evaluating bottom-up:

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence / Notes |
|----|-----------|------|------|------|------|------|----------|
| C-09 | Org evolution path | PASS | PASS | PASS | PASS | PASS | Trigger table required; two-row minimum with concrete thresholds |
| C-10 | Anti-patterns flagged | PASS | PASS | PASS | PASS | PASS | APW section required; minimum two rows; domain-specific rationale |
| C-11 | Steelmans status quo | PASS | PASS | PASS | PASS | PASS | Case for Staying Flat as labeled sub-section 1; mechanism-typed table required |
| C-12 | Decides/Escalates split | PASS | PASS | PASS | PASS | PASS | Separate columns required; `DO NOT use a single Decision Scope column` |
| C-13 | Re-assessment trigger | PASS | PASS | PASS | PASS | PASS | `DO write a re-assessment trigger naming a concrete threshold. DO NOT write "revisit as the team grows"` |
| C-14 | Steelman reasons mechanism-typed | PASS | PASS | PASS | PASS | PASS | Dep C-11 ✓. Closed vocabulary (`Channel / Informal Role / Recurring Cadence / Shared Artifact`) required; each Mechanism Name MUST be "specific, observable" |
| C-15 | Three-part inertia structure labeled | PASS | PASS | PASS | PASS | PASS | Four labeled sub-sections enforced; C-15 requires all three labels present (Case for Staying Flat, How We Coordinate Today, VERDICT) — all present as headings |
| C-16 | Escalates column names destination | PASS | PASS | PASS | PASS | PASS | Dep C-12 ✓. `DO populate Escalates naming the destination role or forum. DO NOT write "everything not listed under Decides"` |
| C-17 | Org evolution trigger table ≥2 entries | PASS | PASS | PASS | PASS | PASS | Dep C-09 ✓. `DO include at minimum two rows. Row 1: headcount. Row 2: MUST come from a different category` |
| C-18 | Anti-pattern table with domain-specific rationale | PASS | PASS | PASS | PASS | PASS | Dep C-10 ✓. `Why It Applies Here` column with typed citation syntax enforced |
| C-19 | Org evolution cross-dimension diversity | PASS | PASS | PASS | PASS | PASS | Dep C-17 ✓. `DO NOT use two headcount thresholds as the two rows` |
| C-20 | Anti-pattern rationale names specific element | PASS | PASS | PASS | PASS | PASS | Dep C-18 ✓. `MUST open each Why It Applies Here cell with typed citation syntax [element name] (cat-N)` |
| C-21 | Anti-pattern watch preceded by register artifact | PASS | PASS | PASS | PASS | PASS | Dep C-20 ✓. `MUST produce an ORG-ELEMENT REGISTER block immediately after charters phase gate. DO NOT skip it. DO NOT proceed to Org Evolution Roadmap until all four category entries are populated` |
| C-22 | Four-part inertia with sequencing guard | PASS | PASS | PASS | PASS | PASS | Dep C-15 ✓. Four-sub-section structure (CfSF / HWCToday / Rebuttal / VERDICT) + FLAT-CASE-CLOSED separator guard present |
| C-23 | Sequencing guard embeds mechanism-reason count | PASS | PASS | PASS | PASS | PASS | Dep C-22 ✓. `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---` with N substituted after count |
| C-24 | APW citations use typed register syntax | PASS | PASS | PASS | PASS | PASS | Dep C-21 ✓. `[element name] (cat-N)` syntax required; mismatched cat-N codes prohibited |
| C-25 | Compliance directives imperative-mode | PASS | PASS | PASS | PASS | PASS | Dep C-22+C-21 ✓. Throughout: DO NOT / MUST / REQUIRED / DO — no "by convention" or "typically" phrasing |
| C-26 | Count-verification has conditional remediation path | PASS | PASS | PASS | PASS | PASS | Dep C-23 ✓. Three-step: (1) `DO count the data rows`; (2) `IF count < 2: DO write the missing mechanism row(s) until count reaches 2`; (3) `THEN substitute the final row count as N` — "final" enforces verify-then-substitute |
| C-27 | Imperative layer free of conflicting descriptive prose | PASS | PASS | PASS | PASS | PASS | Dep C-25 ✓. No "by convention," "the purpose is to serve as," or "typically" in any governed-behavior block |
| C-28 | Imperative-only framing universally | PASS | PASS | PASS | PASS | PASS | Dep C-27 ✓. Scanned all imperative directives: no motivational sentence justifies any rule. V-03's ROLE-LOAD-ORDER is a pure ordered imperative (`DO classify roles in this order: Engineering and Operations types first`); no motivation sentence explains why that order exists |
| C-29 | Typed role classification block with downstream propagation | PASS | PASS | PASS | PASS | PASS | Dep C-03 ✓. `ROLE-TYPE-CLASSIFICATION:` block required immediately after ROLES-LOADED; Key Roles cells AND Membership fields both require `[role name] ([domain type])` annotation |
| C-30 | Mechanism evidence table uses closed-vocabulary Type column | PASS | PASS | PASS | PASS | PASS | Dep C-14 ✓. Three-column table required; Type MUST use `Channel / Informal Role / Recurring Cadence / Shared Artifact` — no free-form values |
| C-31 | Phase gates use positional emit-then-block directives | PASS | PASS | PASS | PASS | PASS | Dep C-28 ✓. Four gates in exact form: `DO emit: === [PHASE GATE: X — Y] ===; DO NOT proceed to Y until this gate line is present.` Gate text is purely positional (names what completed and what begins). Section order list includes all four gate entries. No adjacent motivational sentence on any gate directive |
| C-32 | Format specs directive-embedded; no code-fenced templates | PASS | PASS | PASS | PASS | PASS | Dep C-25 ✓. Zero code-fenced blocks across all five variations. All format specs use inline backtick strings within directive sentences: `` `- [role name] — [domain type]` ``, `` `Mechanism Name \| Type \| Frequency / Participants` ``, `` `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---` ``, `` `Area \| Headcount \| Key Roles \| Decides \| Escalates` ``, `` `[element name] (cat-N)` ``. V-02/V-04/V-05: `` `FLAT-CASE-PRESSURE: [rating] — [justification]` `` is inline backtick. V-05: `` `Quorum: [N roles required for binding decisions]` `` is inline backtick |

**Aspirational: 24/24 all variations**

---

### V-03 C-28 Deep-Check

The hypothesis flagged a secondary risk: does ROLE-LOAD-ORDER adjacent to the gate create a C-28 violation? Resolution: ROLE-LOAD-ORDER appears in its own titled section (`ROLE-LOAD-ORDER — CLASSIFICATION SEQUENCE CONSTRAINT`) before ROLE-TYPE-CLASSIFICATION and before the gate directive. The gate `DO emit: === [PHASE GATE: ROLES COMPLETE...] ===` is separated by the entire ROLE-TYPE-CLASSIFICATION block (~6 directive lines). No adjacency. Additionally, the ROLE-LOAD-ORDER text is pure sequencing imperative (`DO classify... in this order`; `DO NOT interleave types`) with zero motivational content. C-28 PASS confirmed.

### V-05 C-06 Deep-Check

The variate doc flagged "C-17" as the risk criterion but C-17 governs the Org Evolution Roadmap, not committee charters. The actual C-06 risk is: does adding a fifth field (Quorum) violate the "all three charter elements" requirement? C-06 pass condition requires purpose, membership, and authority (Decides + Escalates). V-05 provides all five fields including both authority columns. C-06 PASS. The notation in V-05's hypothesis using "C-17" for the charter four-field requirement is a reference error in the variate document; the criterion is C-06.

---

### Composite Scores

```
composite = (5/5 × 60) + (3/3 × 30) + (24/24 × 10)
          = 60 + 30 + 10.0
          = 100.0
```

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 5/5 (60) | 3/3 (30) | 24/24 (10.0) | **100.0** | Golden |
| V-02 | 5/5 (60) | 3/3 (30) | 24/24 (10.0) | **100.0** | Golden |
| V-03 | 5/5 (60) | 3/3 (30) | 24/24 (10.0) | **100.0** | Golden |
| V-04 | 5/5 (60) | 3/3 (30) | 24/24 (10.0) | **100.0** | Golden |
| V-05 | 5/5 (60) | 3/3 (30) | 24/24 (10.0) | **100.0** | Golden |

**R12 achieves 24/24 across all five variations. First 100.0.**

---

### Rank

All five variations tie at 100.0. Ordered by axis complexity and research value:

1. **V-01** — canonical synthesis; proves the minimum C-31+C-32 combination
2. **V-04** — proves FLAT-CASE-PRESSURE and ROLE-LOAD-ORDER are structurally independent at gate boundaries
3. **V-02** — proves FLAT-CASE-PRESSURE preserves 24/24 within the C-31+C-32 base
4. **V-03** — proves sub-phase classification ordering is C-28-safe as a pure imperative
5. **V-05** — proves charter field extensibility is C-06-safe; surfaces the C-17 notation error in the hypothesis

---

### Excellence Signals

**From V-01 (canonical synthesis):**
The C-31 gate directive form — `DO emit: === [PHASE GATE: X COMPLETE — Y BEGINS] ===; DO NOT proceed to Y until this gate line is present` — simultaneously satisfies **three criteria** in one sentence: C-31 (emittable gate marker present), C-28 (purely positional text, no motivation adjacent), and C-32 (gate spec is inline backtick string within a directive sentence). This triple-criterion density in a single directive pattern is the structural discovery of R12.

**From V-03:**
Sub-phase classification ordering constraints (ROLE-LOAD-ORDER) are C-28-safe when expressed as pure imperative sequences (`DO classify in this order... DO NOT interleave types`). The absence of any motivational sentence explaining why the order exists is what makes it safe. This opens a class of sub-phase sequencing constraints as a zero-cost C-28 extension pattern.

**From V-05:**
C-06 is extensible beyond four charter fields. The criterion's pass condition requires "at minimum three charter elements" — a fifth field is additive, not a violation. This confirms that charter-level format evolution is non-breaking to the rubric, and that V-05's hypothesis notation error (attributing the four-field requirement to C-17 rather than C-06) surfaces a documentation precision gap in the variate document.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-31 gate directive form (DO emit inline backtick / DO NOT proceed) simultaneously satisfies C-31, C-28, and C-32 in a single sentence — triple-criterion density from one directive pattern", "Sub-phase classification ordering constraints (ROLE-LOAD-ORDER) are C-28-safe when expressed as pure imperative sequences with no motivational sentences explaining the ordering rationale", "Charter field extensibility is C-06-safe: adding a fifth charter field (Quorum) does not violate C-06 because the pass condition requires at-minimum three elements, not exactly four fields"]}
```
