## Flow-Trigger Skill — Round 2 Scoring (Rubric v2)

**Variations file**: `flow-trigger-variate-R2-v3-2026-03-15.md`
**Rubric version**: v2 — C-01 through C-13; N_aspirational = 5

---

### Scoring Legend

| Symbol | Meaning |
|--------|---------|
| ✅ PASS | Criterion mechanically satisfied by the prompt structure |
| ⚡ PARTIAL | Criterion addressed but enforcement weaker than structural |
| ❌ FAIL | Criterion absent or actively undermined |

---

## V-01 — Role Sequence: Scanner → Enumerator → Verdict Analyst

**Target criteria**: C-11 (denominator locked before enumeration), C-13 (Verdict Analyst contractually cites Role B rows)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | ✅ PASS | Role B: "Every C-ID from Role A must appear in the sequence — either as a firing entry or a disposal entry. No C-ID may be silently omitted." B-Summary reconciles count. |
| C-02 | ✅ PASS | Role B: "Process candidates Sync-tier first, Async-tier second. Within each tier, use Role A C-ID order." |
| C-03 | ✅ PASS | Firing entry format has explicit "Reads" and "Produces" fields with lead-word constraint and per-field citation. |
| C-04 | ✅ PASS | Role C: C-1 (Storm), C-2 (Missing), C-3 (Circular) — all three named with verdict templates. |
| C-05 | ✅ PASS | Role B vocabulary field: "exact term from Role A vocabulary" — platform terms from Role A locked. |

Essential sub-score: **5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | ✅ PASS | C-3 constructs directed edges, states graph property (DAG / CYCLIC), with tracing path. |
| C-07 | ✅ PASS | Condition field: "Evaluates [text]. Taken: [branch] — [reason]. Skipped: [branch] — [reason]." Both branches required. |
| C-08 | ✅ PASS | "Mitigation if STORM DETECTED", "Mitigation if MISSING TRIGGER", "Mitigation if CIRCULAR TRIGGER" all present. |

Recommended sub-score: **3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | ✅ PASS | Firing entry: "Execution tier: Sync (blocks transaction) or Async (~N min [standard\|premium] tier)" — numeric estimate required. |
| C-10 | ✅ PASS | "if a side-effect write matches any C-ID's trigger condition, the downstream trigger must be the immediately next numbered entry before the sequence returns to C-ID order." |
| C-11 | ✅ PASS | Role A must complete and lock its denominator table ("Denominator N = [count]. Locked.") before Role B opens. Hard structural dependency — Role B cannot begin without Role A output. Strongest C-11 mechanism among sequencing-only variations. |
| C-12 | ✅ PASS | Disposal Entry format present inline. Role B: "No C-ID may be silently omitted." B-Summary requires "Disposal entries: N (list entry #s and C-IDs)" — provides post-hoc reconciliation. Gap tokens are inline in the sequence. |
| C-13 | ✅ PASS | Role C: "Every evidence block must cite specific entry numbers from Role B's numbered sequence. A verdict that appears without entry-number citations is a `[BARE ASSERTION]`." Contractual citation constraint + detection tag. |

Aspirational sub-score: **5/5 → 10 pts**

**V-01 Composite: 100** | All essential: ✅

---

## V-02 — Output Format: Full-Roster Sequence (Pre-Allocated Slots)

**Target criteria**: C-12 (pre-allocated slots make disposal mandatory by construction), C-10 (cascade-spawns? decision per entry)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | ✅ PASS | Section 1 roster + "A C-ID absent from the sequence is a structural gap." Sequence completeness verification table reconciles. |
| C-02 | ✅ PASS | "List all candidates in roster order: Sync-tier C-IDs first, Async-tier C-IDs second." |
| C-03 | ✅ PASS | Firing Slot table: Reads row, Produces row with explicit lead-word constraint. |
| C-04 | ✅ PASS | Section 3: Trigger Storm, Missing Triggers, Circular Triggers — all three verdict templates present. |
| C-05 | ✅ PASS | "PA flow type: exact term from Section 1 vocabulary" — vocabulary anchored to pre-declared roster. |

Essential sub-score: **5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | ✅ PASS | Circular Triggers: directed edges "Entry #[N] writes {Entity.Field} → fires {trigger}", graph property DAG/CYCLIC. |
| C-07 | ✅ PASS | Condition field in Firing Slot: "No condition or: Evaluates [text]. Taken: [branch] — [reason]. Skipped: [branch] — [reason]." |
| C-08 | ✅ PASS | Mitigation fields for storm, missing trigger, circular trigger — all present under verdicts. |

Recommended sub-score: **3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | ✅ PASS | Execution tier field with "~N min [standard\|premium] tier" — numeric latency required. |
| C-10 | ✅ PASS | "Cascade spawns?" is an explicit named field in the Firing Slot table — YES triggers an inline continuation entry. Decision is per-entry, not a post-hoc note. |
| C-11 | ✅ PASS | Section 1 declares full roster before Section 2. "Section 2's Full-Roster Sequence will contain exactly N primary slots." Denominator locked before sequence opens. |
| C-12 | ✅ PASS — **strongest** | Pre-allocated slots make silent omission structurally impossible: every C-ID from Section 1 gets a slot in Section 2; the slot must contain either a Firing Slot or a Disposal Slot. There is no structural path to omission. This is the best C-12 enforcement of the five variations. |
| C-13 | ✅ PASS | Section 3: "Each verdict must cite specific Section 2 entry numbers as evidence." Verdict templates embed entry number placeholders explicitly. |

Aspirational sub-score: **5/5 → 10 pts**

**V-02 Composite: 100** | All essential: ✅

---

## V-03 — Phrasing Register: Evidence-Row-Verdict (ERV) Sub-Structure

**Target criteria**: C-13 (ROW RANGE → FINDING → VERDICT three-part structure makes citation a named slot with visible gap)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | ✅ PASS | Step 2: "For each C-ID, produce a numbered entry — either a firing entry or a disposal entry. Every C-ID must be accounted for in Step 2." |
| C-02 | ✅ PASS | "List all candidates in execution-tier order (Sync first, Async second)." |
| C-03 | ✅ PASS | Firing entry: Reads and Produces fields with lead-word constraint. |
| C-04 | ✅ PASS | Step 4: Class 1 (Storm), Class 2 (Missing), Class 3 (Circular) — all three with verdict sentences. |
| C-05 | ✅ PASS | PA flow type vocabulary terms listed in Step 2 firing entry format. |

Essential sub-score: **5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | ✅ PASS | Class 3: directed edges constructed per entry, "graph property: DAG / CYCLIC." |
| C-07 | ✅ PASS | Condition field: Taken and Skipped branches with reasons required. |
| C-08 | ✅ PASS | Mitigation present for storm and circular (MISSING TRIGGER also, though structurally lighter). |

Recommended sub-score: **3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | ✅ PASS | Execution tier field with numeric latency. |
| C-10 | ✅ PASS | Cascade rule in firing entry: downstream trigger must be immediately next numbered entry. |
| C-11 | ⚡ PARTIAL | Step 1 says "This step must appear before Step 2. A candidate list that first appears within or after Step 2 is a structural error." This is an explicit instruction with violation labeling — stronger than bare instruction, but weaker than V-01/V-04 (hard role/phase separation with completion gate). A model could still interleave. |
| C-12 | ⚡ PARTIAL | Disposal entry format is present and Step 2 says "For each C-ID, produce a numbered entry." The Step 3 reconciliation table provides post-hoc gap detection. However, unlike V-02 (pre-allocated slots) and V-04 (denominator-ordered mandatory slots), there is no structural mechanism that makes silent omission impossible — enforcement relies on instruction compliance + Step 3 audit. |
| C-13 | ✅ PASS — **strongest** | ERV three-part sub-structure (ROW RANGE → FINDING → VERDICT) makes citation a named, visible slot. Missing ROW RANGE = visibly incomplete sub-structure, flagged `[ERV VIOLATION: verdict present; row-range sub-section absent]`. A verdict cannot appear without a ROW RANGE above it. This is the strongest C-13 enforcement mechanism across all five variations. |

Aspirational sub-score: **4/5 (0.5 + 0.5 partials) → 8 pts**

**V-03 Composite: 98** | All essential: ✅

---

## V-04 — Combined: Role Sequence + Denominator-Ordered Sequence

**Target criteria**: C-11 + C-12 simultaneously through Phase 1 completion gate + Phase 2 mandatory C-ID slots

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | ✅ PASS | Phase 2 completeness verification table + "A C-ID absent from Phase 2 is a structural gap." |
| C-02 | ✅ PASS | Phase 2: "Produce entries in C-ID order: all Sync group C-IDs first (C-S**), then all Async group C-IDs (C-A**)." |
| C-03 | ✅ PASS | Firing Entry table: Reads and Produces fields with lead-word constraint. |
| C-04 | ✅ PASS | Phase 3: Trigger Storm, Missing Triggers, Circular Triggers — all three verdict sections. |
| C-05 | ✅ PASS | Phase 1 uses PA Flow Type with exact terms; Phase 2 firing entry inherits vocabulary. |

Essential sub-score: **5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | ✅ PASS | Circular Triggers: directed edges with entry numbers, graph property DAG/CYCLIC, mitigation. |
| C-07 | ✅ PASS | Condition field in Firing Entry: Taken/Skipped branches required. |
| C-08 | ✅ PASS | "Mitigation if STORM DETECTED", "Mitigation if MISSING TRIGGER", "Mitigation if CIRCULAR TRIGGER." |

Recommended sub-score: **3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | ✅ PASS | Execution tier field with "~N min [standard\|premium] tier" — numeric required. |
| C-10 | ✅ PASS | "Cascade?" field in Firing Entry table — "YES → insert Entry #[seq+1]" before next C-ID slot. |
| C-11 | ✅ PASS — **strongest shared** | Phase 1 must complete before Phase 2 begins — hard completion gate ("Complete Phase 1 before beginning Phase 2"). Two-group declaration (Sync group / Async group) with sub-counts and total denominator. Denominator is authoritative and Phase 2 produces "exactly N primary slots." Combines V-01's role-separation principle with V-02's slot-count constraint. |
| C-12 | ✅ PASS — **strongest shared** | Every C-ID from Phase 1 gets exactly one primary slot in Phase 2. Disposal Entry is the mandatory alternative fill. "N candidates in Phase 1 produces exactly N primary sequence slots in Phase 2" — stated as a mathematical identity, not an instruction. No structural path to silent omission. Equal to V-02 in structural enforcement, achieved through a different mechanism (denominator-ordered slots rather than pre-allocated roster slots). |
| C-13 | ✅ PASS | Phase 3: "Each verdict must reference specific Phase 2 entry numbers." Verdict templates for all three classes include entry number placeholders. |

Aspirational sub-score: **5/5 → 10 pts**

**V-04 Composite: 100** | All essential: ✅

---

## V-05 — Phrasing Register + Inertia Framing (Named Failure Modes 7/8/9)

**Target criteria**: C-11 + C-12 + C-13 through named failure modes with inline detection tags

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | ✅ PASS | Section 1 (pre-scan) + Section 2 (enumeration with disposal entries). Section 3 reconciliation table. |
| C-02 | ✅ PASS | Section 2: "List all candidates in execution-tier order (Sync first, Async second)." |
| C-03 | ✅ PASS | Firing entry table: Reads (Term Set C), Produces (Term Set D). |
| C-04 | ✅ PASS | Section 4: Trigger Storm, Missing Triggers, Circular Triggers — Failure Mode 2 enforces all three. |
| C-05 | ✅ PASS — **strongest** | Section 0 — Governed Term Sets (A through E) — each with explicit non-conforming inline tag (`[VOCAB FAIL: actual text]`). Strongest vocabulary enforcement across all five variations. |

Essential sub-score: **5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | ✅ PASS | Circular Triggers in Section 4 with directed edges and graph property. |
| C-07 | ✅ PASS | Failure Mode 4 (Branch Amnesia) + Term Set E — `[BRANCH MISSING]` tag enforces both branches. |
| C-08 | ✅ PASS | Mitigation fields present under each anomaly verdict. |

Recommended sub-score: **3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | ✅ PASS — **strong** | Failure Mode 5 (Latency Blindness) + Term Set B — `[TIER UNDECLARED]` tag. "N must be numeric" explicit. Best C-09 enforcement after Section 0 governs it explicitly. |
| C-10 | ✅ PASS | Failure Mode 6 (Cascade Annotation Without Continuation) + "Cascade continuation" field with `[CASCADE GAP]` tag. |
| C-11 | ✅ PASS | Failure Mode 7 (Denominator Post-Declaration) named with `[DENOMINATOR POST-DECLARED: {section}]` tag. Section 1 is a distinct named section that "SHALL appear as a distinct section before Section 2." |
| C-12 | ✅ PASS | Failure Mode 8 (Silent Candidate Omission) named with `[SILENT OMISSION: {trigger name}]` tag. Section 2 has disposal entries with "Omitting this entry for a non-firing candidate: apply [SILENT OMISSION]." Named motivation for the requirement. |
| C-13 | ✅ PASS | Failure Mode 9 (Citation-Free Verdict) named with `[CITATION FREE: {class}]` tag. Section 4 requires specific entry citations. |

Aspirational sub-score: **5/5 → 10 pts**

**V-05 Composite: 100** | All essential: ✅

---

## Summary Scorecard

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | All Essential |
|-----------|---------------|-----------------|-------------------|-----------|---------------|
| V-01 | 60 | 30 | 10 | **100** | ✅ |
| V-02 | 60 | 30 | 10 | **100** | ✅ |
| V-03 | 60 | 30 | 8 | **98** | ✅ |
| V-04 | 60 | 30 | 10 | **100** | ✅ |
| V-05 | 60 | 30 | 10 | **100** | ✅ |

**Rank (tiebreak on structural strength)**: V-04 > V-01/V-02 (tied) > V-05 > V-03

---

## Excellence Signals — Top Scorer (V-04)

**What V-04 did that the others did not (or did less completely):**

**1. Mathematical identity constraint on slot count**
V-04 states: *"N candidates in Phase 1 produces exactly N primary sequence slots in Phase 2."* This is not an instruction ("produce a disposal entry for non-firers") — it is a count identity. A model that generates 4 slots when Phase 1 declared 5 candidates has a visibly broken equation. This is a qualitatively different enforcement mechanism than V-01/V-03/V-05's instruction-based disposal entries.

**2. Dual-axis structural dependency**
V-04 stacks two structural dependencies: Phase 1 must complete before Phase 2 (V-01-style completion gate) AND every Phase 1 C-ID has exactly one slot in Phase 2 (V-02-style pre-allocation). This means neither C-11 nor C-12 can be violated by instruction drift — both require structural violations to miss.

**3. Post-enumeration completeness verification table**
V-04 requires a mandatory verification table after the last Phase 2 entry: `Phase 1 denominator | N`, `Primary slots filled | N`, `Firing entries | N`, `Disposal entries | N`, `Cascade insertions | N`, `Missing C-IDs | none`. This reconciliation table creates a third audit point (beyond C-11's pre-scan and C-12's inline tokens) that exposes any denominator-vs-sequence discrepancy without the scorer needing to count manually.

**4. Two-tier denominator grouping**
Phase 1 declares candidates in Sync group + Async group sub-tables with sub-counts. Phase 2 sequences in the same Sync-then-Async order. The structural mirroring between declaration and enumeration reduces cognitive gap — the denominator is organized to match the enumeration order, not a flat list that must be mentally reordered.

---

## New Patterns for Rubric Consideration

These patterns appear in V-04 (and partially in V-02) and are not captured by any current criterion:

- **Post-enumeration slot reconciliation table** — a required structured table after the last sequence entry that reconciles input denominator count against output slot counts (firing, disposal, cascade). Distinct from C-11 (pre-declaration) and C-12 (inline gap tokens) — this is a third verification layer that makes completeness auditable at a glance without re-reading the sequence.

- **Denominator declared in execution-tier sub-groups mirroring sequence order** — candidates grouped as Sync/Async in the pre-scan, matching the Sync-first/Async-second enumeration order. Makes the connection between the denominator and the sequence structural rather than requiring the reader to mentally reorder.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Post-enumeration slot reconciliation table: required structured table after last sequence entry reconciling input denominator count against firing/disposal/cascade slot counts — third audit layer distinct from C-11 pre-declaration and C-12 inline tokens", "Denominator declared in execution-tier sub-groups (Sync/Async) mirroring sequence order — structural mirroring between pre-scan and enumeration reduces cognitive gap and makes omissions detectable by group count"]}
```
