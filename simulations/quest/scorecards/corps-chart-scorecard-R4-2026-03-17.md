## corps-chart Round 4 — Quest Score

---

### Variations Received

Only **V-01** was present in the variations document. V-02 through V-05 are referenced in the header but their content was not included. Scoring V-01 only; ranking section is single-entry.

---

## V-01 — Single Axis: Role Sequence

**Hypothesis:** Front-loading ROLE-NAME LOCK as the only permitted first action — before any structural reasoning — eliminates downstream role-name drift because the locked list is the first artifact in working memory.

---

### Criterion-by-Criterion Evaluation

#### Essential Tier (60 pts, 12 pts each)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | ROLE-TYPE-CLASSIFICATION with all four domain types | **PASS** | STEP 0 explicitly classifies every loaded role into one of four domain types from a closed vocabulary: (strategic), (operational), (advisory), (governance). Table format specified. |
| C-02 | ASCII diagram with hierarchy and committees as distinct nodes | **PASS** | STEP 2 requires box-drawing characters, "at least two levels of hierarchy," committees as "distinct labeled nodes connected by lines — not embedded inside an area box." Example diagram shown. Role names must match ROLE-NAME LOCK exactly. |
| C-03 | Headcount table with Decides and Escalates columns | **PASS** | STEP 3 explicitly states "Five columns, no merging. Separate Decides and Escalates columns are required." Full column spec shown including Total row. |
| C-04 | Operating rhythm table with minimum three distinct rows | **PASS** | STEP 3 requires at minimum three rows: (a) ROB, (b) shiproom or gate meeting, (c) governance meeting. "Two meetings must not be merged into one row" is implicit in the structure. |
| C-05 | Committee charters with all five required fields | **PASS** | STEP 4 explicitly lists all five fields. Quorum format matches the fraction pattern. Membership requires at least two annotated roles. Escalates requires a named destination. "Missing any field causes the charter to fail." |

**Essential subtotal: 60 / 60**

---

#### Recommended Tier (30 pts, 10 pts each)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Inertia assessment with verdict and pressure rating | **PASS** | STEP 1 includes all four sub-sections in prescribed order. VERDICT format is exactly specified with closed-set rating. Re-assessment trigger requires "a concrete measurable threshold — a specific hire count, a named milestone event, or a structural symptom with a countable condition — not 'revisit as the team grows'." Both declarations (CAN-OPERATE-FLAT / STRUCTURE-WARRANTED) are specified. |
| C-07 | ORG-ELEMENT REGISTER with all four categories | **PASS** | STEP 5 emits all four categories: cat-1 (Areas) with headcount, cat-2 (Committees/Cadences), cat-3 (Headcount) with total, cat-4 (DRI Roles). "No category may be empty" stated explicitly. |
| C-08 | Section order with all phase gates present | **PASS** | All four phase gates are emitted in sequence across STEP 1, 2, 3, and 4. Prompt structure prevents out-of-order sections by design. |

**Recommended subtotal: 30 / 30**

---

#### Aspirational Tier (10 pts, 1.43 pts per PASS, 0.71 pts per PARTIAL)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Anti-Pattern Watch with typed cat-N citations | **FAIL** | Anti-Pattern Watch section is absent from the prompt entirely. STEP 6 covers Org Evolution Roadmap only. No table, no cat-N citations defined. |
| C-10 | Org Evolution Roadmap with two distinct trigger categories | **PARTIAL** | STEP 6 includes the trigger table with correct columns. However, the only example row shown is a headcount threshold, and the prompt does not mandate that Row 2 come from a different trigger category. Output is structurally likely but category diversity is not enforced. |
| C-11 | Inertia Rebuttal is role-grounded with concrete re-assessment trigger | **PASS** | Four-field form includes ROLE UNDER PRESSURE (one role from ROLE-NAME LOCK) and RE-ASSESSMENT TRIGGER (concrete threshold). OBSERVABLE BREAKDOWN explicitly disallows "as we scale" framing. |
| C-12 | Role-name coherence across all document sections | **PASS** | Diagram: "Role names in boxes must match ROLE-NAME LOCK exactly." How We Coordinate Today: "Name roles from ROLE-NAME LOCK only." DRI/Owner: "must name roles from ROLE-NAME LOCK only." Charter Membership and Decides both reference ROLE-NAME LOCK. Coverage is document-wide. |
| C-13 | ROLE-NAME LOCK block emitted after classification | **PASS** | STEP 0 includes the full box-drawn ROLE-NAME LOCK block with exact box-drawing characters. Explicitly emitted "immediately — before any phase gate, before any section header." States it is "the contract" against which downstream sections are verified. |
| C-14 | Inertia Rebuttal uses mandatory four-field case form | **PASS** | All four labeled fields present with prescribed order. "Do not proceed to VERDICT without completing all four fields" is an explicit enforcement gate. OBSERVABLE BREAKDOWN disallows future-projection language. |
| C-15 | Anti-Pattern Watch uses schema-enforced CAT-N citation prefix | **FAIL** | No Anti-Pattern Watch section in the prompt (C-09 FAIL), therefore no CAT-N-CITATION-SCHEMA block possible. |

**Aspirational breakdown:**
- PASS × 4 = 4 × 1.43 = 5.72
- PARTIAL × 1 = 1 × 0.71 = 0.71
- FAIL × 2 = 0

**Aspirational subtotal: 6.43 / 10**

---

### V-01 Composite Score

| Tier | Score |
|------|-------|
| Essential | 60.00 |
| Recommended | 30.00 |
| Aspirational | 6.43 |
| **Total** | **96.43** |

---

### Ranking (single entry)

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-01 | 96.43 | Yes |

---

### Gap Analysis

**Structural gaps preventing 100:**

| Criterion | Gap | Root Cause |
|-----------|-----|-----------|
| C-09 | Anti-Pattern Watch section missing entirely | STEP 6 was defined as Org Evolution Roadmap only; no STEP 7 for Anti-Pattern Watch |
| C-15 | CAT-N-CITATION-SCHEMA absent | Downstream of C-09 absence; cannot exist without the section |
| C-10 | Trigger diversity unenforced | Example row shows only one type; no explicit instruction requires a second category type |

**C-09 + C-15 together represent 2 × 1.43 = 2.86 pts** — recoverable in one structural addition.

---

### Excellence Signals

V-01 introduces one notable pattern not previously formalized:

**Signal 1 — Mandatory-First-Action framing with enforcement prose**
Previous variants established ROLE-NAME LOCK but V-01 goes further: it labels STEP 0 as "MANDATORY FIRST ACTION," adds the explicit prose "Do not skip or defer this step. Nothing else begins until the roles block is complete," and states "The ROLE-NAME LOCK is the contract. Downstream sections are verified against it, not against the prose role descriptions above it." This converts the lock from a structural suggestion into an enforced precondition — the working-memory-first theory made explicit in the prompt itself.

**Signal 2 — Four-field Rebuttal with an intra-step enforcement gate**
The instruction "Do not proceed to VERDICT without completing all four fields" introduces a step-internal gate pattern distinct from the inter-step phase gates. This is a finer-grained enforcement mechanism and the first prompt-level gate that operates within a single section rather than between sections.

---

### Round 4 Recommendation

To close the remaining gap, the next variation should add:

**STEP 7 — ANTI-PATTERN WATCH** immediately before or after Org Evolution Roadmap, structured as:

```
CAT-N-CITATION-SCHEMA
Valid codes: [drawn from ORG-ELEMENT REGISTER above]
Mandatory format for "Why It Applies Here": [element name] (cat-N) — [explanation]
Every cell in this column must open with this prefix. No cell may name an org element without it.
```

Followed by the Anti-Pattern Watch table with ≥2 rows, enforcing C-09 and C-15 simultaneously.

---

```json
{"top_score": 96.43, "all_essential_pass": true, "new_patterns": ["Mandatory-First-Action framing: labeling STEP 0 with explicit enforcement prose ('Nothing else begins until complete') converts role-lock from a structural suggestion into an enforced precondition, making the working-memory-first mechanism explicit in the prompt", "Intra-step enforcement gate: 'Do not proceed to VERDICT without completing all four fields' introduces a within-section gate distinct from inter-section phase gates — a finer-grained enforcement pattern applicable wherever a multi-field form must be fully populated before continuing"]}
```
