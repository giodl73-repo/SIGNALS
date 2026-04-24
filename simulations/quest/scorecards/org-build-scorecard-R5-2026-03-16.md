# Quest Score — org-build R5

## Rubric: v5 | Criteria: 22 (5E / 3R / 14A) | Formula: (E/5·60) + (R/3·30) + (A/14·10)

---

## V-01: Role Sequence — Inertia-First

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Phase 4 Section 1 requires ASCII box diagram with "min 2 org levels"; flat name lists explicitly fail. Example shape provided. |
| C-02 | **PASS** | Phase 3 template lists all five fields; "MUST: every file contains all five fields. Any missing field fails." |
| C-03 | **PASS** | Phase 1 generates `.roles/governance/inertia-advocate.md` before any other role. Role name contains `inertia-advocate`. |
| C-04 | **PASS** | Phase 3: Standard 20–30, Deep 50+. T3-ROLE-COUNT recorded. Both bounds stated. |
| C-05 | **PASS** | Phase 4 Section 2 table includes Area, Headcount, Key Roles, Decides, Escalates. "MUST include Decides and Escalates columns." |

**Essential: 5 / 5**

---

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | Phase 2 produces area subdirectories; Phase 1 places IA under `.roles/governance/`. Min 2 subdirs achieved structurally. |
| C-07 | **FAIL** | No operating rhythm table, no shiproom/ROB rows, no committee charters. The variation does not address governance cadence at all. |
| C-08 | **PASS** | Phase 4 Section 3 produces `FLAT-CASE-PRESSURE: {{T0-PRESSURE}}` and `VERDICT: {{T0-VERDICT}}`. Phase 0 locks both values before Phase 4 executes. Closed-set rating and single-verdict format present. |

**Recommended: 2 / 3**

---

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **FAIL** | No Org Evolution Roadmap. No typed trigger rows. Not addressed anywhere in V-01. |
| C-10 | **FAIL** | Anti-pattern section truncated in provided spec. cat-N citation syntax (`[element] (cat-N) —`) not established. MUST directive present for category derivation but format constraint absent. |
| C-11 | **PASS** | Phase 1 explicitly provides scope template table keyed to T0-PRESSURE; inertia-advocate scope is derived from the FLAT-CASE-PRESSURE rating via pre-written per-rating templates. |
| C-12 | **FAIL** | Phase 4 Section 3 states "category selection MUST be tied to T0-VERDICT" but spec is truncated before showing explicit cat-1/cat-2 vs. cat-3/cat-4 assignments per verdict path. Intent present; execution missing. |
| C-13 | **PASS** | Phase 0 Step 0.3: "Writing both is an error. Writing neither is an error." Explicit error framing. Both failure modes named by name. |
| C-14 | **PASS** | Phase 0 → T0-VERDICT/T0-PRESSURE; Phase 2 input contract references T0-VERDICT; Phase 3 input contract references T0-VERDICT, T0-PRESSURE, T2-AREAS; Phase 4 input contract references all prior gates. Multiple named typed variable pairs fully satisfied. |
| C-15 | **PASS** | Phase 0: "Writing both is an error. Writing neither is an error." Phase 4: "FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts." Symmetric FORBIDDEN framing covering both directions in two locations. |
| C-16 | **FAIL** | Anti-pattern table truncated. Mitigation cells not shown. Cannot verify remediation actions vs. format guidance. Fails by absence. |
| C-17 | **PASS** | Rate-keyed verbatim template table provided in Phase 1. "MUST: scope field contains exact verbatim template text. Paraphrase fails." |
| C-18 | **FAIL** | Anti-pattern section truncated. Exclusion sets (CAN-OPERATE-FLAT forbids cat-1/cat-4; STRUCTURE-WARRANTED forbids cat-2/cat-3) not stated. |
| C-19 | **PASS** | All phase constraint statements use MUST or FORBIDDEN uniformly. Scope template text uses "Audit", "Require", "Accept" but those are action-verb instructions within copied template content, not advisory constraint language in phase instructions. |
| C-20 | **PASS** | Phase 0 declares T0-VERDICT/T0-PRESSURE; Phase 2 declares T2-AREAS/T2-AREA-COUNT; Phase 3 declares T3-ROLE-COUNT/T3-ROLE-LIST. All consuming phases (1, 2, 3, 4) declare explicit input contracts naming prior variables by name. Systematic coverage of gate→consumer pairs. |
| C-21 | **FAIL** | T0-VERDICT listed in Phase 1 and Phase 3 input contracts but consumption is not governed by MUST/FORBIDDEN for that specific variable in those phases. Phase 1's MUST governs T0-PRESSURE (scope template selection), not T0-VERDICT. Phase 3's MUST governs field presence and area naming, not T0-VERDICT-driven branching. Named variable present; imperative constraint on its consumption absent in two phases. |
| C-22 | **PASS** | Phase 4 Section 3 contains `FLAT-CASE-PRESSURE: {{T0-PRESSURE}}` / `VERDICT: {{T0-VERDICT}}` — named placeholder slots keyed directly to typed gate outputs. Phase 1 role template contains `scope: [VERBATIM TEXT FROM TABLE ABOVE keyed to T0-PRESSURE]` as a named slot. Gate variable names alone determine what fills each slot. |

**Aspirational: 8 / 14**

---

## Score Summary — V-01

| Band | Pass | Max | Weight | Points |
|------|------|-----|--------|--------|
| Essential | 5 | 5 | 60 | 60.0 |
| Recommended | 2 | 3 | 30 | 20.0 |
| Aspirational | 8 | 14 | 10 | 5.7 |
| **Composite** | | | | **85.7** |

---

## Rankings

| Rank | Variation | Score | E | R | A |
|------|-----------|-------|---|---|---|
| 1 | V-01: Role Sequence — Inertia-First | **85.7** | 5/5 | 2/3 | 8/14 |

*Only one variation submitted for Round 5.*

---

## Excellence Signals — V-01

**1. Verdict-first lock before structural generation**
Phase 0 closes T0-VERDICT and T0-PRESSURE into typed variables before any role file exists. All downstream phases inherit a fixed anchor rather than constructing the verdict alongside the org. This eliminates drift between the inertia assessment and the org structure it should govern.

**2. Rate-keyed verbatim scope templates with explicit anti-paraphrase constraint**
The scope table provides exact text per rating level. The MUST directive prohibits paraphrase explicitly ("Paraphrase fails."). This closes the "close enough" gap: a model cannot produce a semantically similar but textually variant scope and pass. Template text is ground truth.

**3. Symmetric bidirectional FORBIDDEN guard at two depths**
Both failure modes ("both" and "neither") are named as errors twice — once in prose ("Writing X is an error") and once in imperative form ("FORBIDDEN: writing both. FORBIDDEN: omitting both."). C-15 is satisfied with redundancy, making the guard robust to selective reading.

**4. Pre-print skeleton with {{gatevar}} slots that bind artifact shape to gate outputs**
Phase 4's template section renders `{{T0-PRESSURE}}` and `{{T0-VERDICT}}` as named slots whose names are the gate variable names. C-22 is satisfied directly: a reader who knows only Phase 0's output can fill every slot without looking up other material.

---

## Gap Analysis — Criteria Not Yet Addressed

- **C-07** (operating rhythm + committee charters): Entirely absent. No ROB/shiproom table, no charter fields.
- **C-09** (Org Evolution Roadmap with typed triggers): Entirely absent.
- **C-10/C-16/C-18** (anti-pattern completeness): Phase 4 Section 3 is truncated before anti-pattern content. These three criteria fall together.
- **C-21** (constraint-completeness seal): T0-VERDICT reaches Phase 1 and Phase 3 input contracts without a MUST/FORBIDDEN governing its specific consumption in those phases. The seal breaks at the two phases where the variable is listed for context rather than branching logic.

---

```json
{"top_score": 85.7, "all_essential_pass": true, "new_patterns": ["verdict-first lock: closing T0-VERDICT into a typed variable before any structural generation forces all downstream phases to inherit a fixed anchor rather than co-construct the verdict with the org", "symmetric bidirectional FORBIDDEN guard at two depths — prose error framing plus imperative FORBIDDEN on both 'both' and 'neither' paths provides redundancy that makes the single-verdict constraint robust to selective reading", "pre-print skeleton with {{gatevar}} named slots that key artifact shape directly to typed gate output names — a reader who knows only the gate outputs can fill every slot without ambiguity"]}
```
