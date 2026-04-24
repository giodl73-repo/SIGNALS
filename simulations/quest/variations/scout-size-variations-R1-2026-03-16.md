Written to `simulations/quest/variations/scout-size-variations-R1-2026-03-16.md`.

---

## scout-size — Variations R1

Five complete, runnable skill body prompts. Three single-axis, two combination.

---

### V-01 — Inertia-First (axis A)
**Hypothesis**: Opening with the workaround forces C-03 before narrative momentum builds toward the build story. Silent inertia is the most common failure mode — this variant blocks it structurally by making inertia the first required section.

The prompt opens with `INERTIA CHECK FIRST`, then flows: surface area → complexity tier → team+timeline → confidence. The signal boundary warning closes.

---

### V-02 — Table-Centric (axis B)
**Hypothesis**: Column headers act as structural contracts. The model cannot omit LOW/MEDIUM/HIGH/XL if it's a column name. Plan creep is prevented because there's no "tasks" table to drift into.

Four tables: Surface Area (integration points with type), Complexity (single row, tier must be on-scale), Team+Timeline (by discipline + sprint range), Confidence (level + basis + gap + what-would-raise-it). Inertia opens as a one-line statement before the tables.

---

### V-03 — Driver-First Role Sequence (axis C)
**Hypothesis**: When the complexity driver is named first, surface area enumeration becomes motivated — the model asks "what does this driver touch?" rather than listing generically. C-08 and C-01 reinforce each other.

Sequence: Complexity Analyst → Surface Mapper → PM Estimator → Inertia Auditor → Confidence Reviewer. PM Estimator includes the sensitivity check. Inertia Auditor is deliberately last before confidence — making it a required closing check rather than an optional lead.

---

### V-04 — Interrogative Register (axis D)
**Hypothesis**: Six explicit questions eliminate criterion omission — you cannot forget the checklist because the questions ARE the structure. Bare confidence is blocked because Q6 asks "what do you know that supports that?"

Six questions map directly to rubric criteria: Q1→C-03, Q2→C-01, Q3→C-02+C-08, Q4→C-09, Q5→C-06+C-07, Q6→C-04+C-10.

---

### V-05 — Combination: Inertia-First + Table + Sensitivity Block (axes A+B+E)
**Hypothesis**: The combination closes all four failure modes simultaneously. Inertia-first blocks silent inertia (C-03). Table structure blocks plan creep (C-05) and enforces tier vocabulary (C-02). Mandatory calibration rows block bare confidence (C-04). The sensitivity rows in Table 2 pull C-09 into the required table structure rather than leaving it as an aspirational add-on.

Table 2 includes dedicated rows for `Tier UP condition` and `Tier DOWN condition` — sensitivity is structural, not optional. Table 3 has a `What would raise it` row that makes C-10 impossible to skip.
� Table-Centric

**Axis**: B — Output format (all sections expressed as labeled tables with required columns)
**Hypothesis**: Column headers act as structural contracts — a model cannot sneak a sprint date into a "complexity" row without it being visible, and the LOW/MEDIUM/HIGH/XL vocabulary is enforced by column definition rather than instruction.

```
Auto-detect topic from context. Do not prompt unless context absent.

Produce a sizing signal as four tables plus one inertia statement. No prose sections outside the defined structure.

INERTIA STATEMENT (one line, before the tables): "[Workaround name] — [cheaper / comparable / more expensive] than building the feature."

TABLE 1 — SURFACE AREA
Columns: Integration Point | Type (API / data / auth / UI / job / external) | Notes
Rows: one per named integration point. Final row: "Total: N integration points."

TABLE 2 — COMPLEXITY
Columns: Tier (must be exactly LOW / MEDIUM / HIGH / XL) | Primary Driver | Secondary Driver (optional)
Rows: exactly one row.

TABLE 3 — TEAM + TIMELINE
Columns: Specialist Type | FTE Signal | Sprint Range
Rows: one per discipline needed. Sprint Range applies only to the total row.

TABLE 4 — CONFIDENCE
Columns: Level (HIGH / MEDIUM / LOW) | Basis (what you know) | Gap (what is unverified) | What Would Raise It
Rows: exactly one row.

SIGNAL BOUNDARY: no task breakdowns, sprint assignments, owner names, or milestone dates anywhere in the artifact.

Stock roles: Surface Mapper (Table 1), Complexity Analyst (Table 2), PM Estimator (Table 3), Confidence Reviewer (Table 4), Inertia Auditor (statement).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Driver-First Role Sequence

**Axis**: C — Role sequence (Complexity Analyst leads; surface area flows from complexity discovery; PM follows; Inertia Auditor closes)
**Hypothesis**: When the primary driver is named first, surface area enumeration becomes motivated — the model asks "what does this driver touch?" rather than listing generically, producing a more coherent C-01 + C-08 pairing.

```
Auto-detect topic from context. Do not prompt unless context absent.

Run stock roles in this sequence:

STEP 1 — COMPLEXITY ANALYST: Name the one or two factors that most drive implementation complexity. Rate the tier: LOW / MEDIUM / HIGH / XL — exactly this vocabulary. A MEDIUM with a named driver is more useful than a HIGH without one.

STEP 2 — SURFACE MAPPER: From the complexity drivers identified in Step 1, enumerate every integration point the feature touches — APIs, data stores, auth layers, UI surfaces, background jobs, webhooks, external services. Name each one. Total the count. Surface area should connect to the complexity narrative, not float independently.

STEP 3 — PM ESTIMATOR: Given the complexity tier and surface area, state the specialist disciplines required (not headcount — discipline names: "1 backend engineer, 0.5 platform engineer, 1 PM") and a sprint range ("3–5 sprints"). Sensitivity: name one condition that would push the sprint range up and one that would compress it.

STEP 4 — INERTIA AUDITOR: Name the current workaround or status-quo behavior. State whether building this feature is cheaper, comparable, or more expensive than continuing the workaround. This is a required check. Silent omission fails the signal.

STEP 5 — CONFIDENCE REVIEWER: Aggregate the above into a single confidence statement: HIGH / MEDIUM / LOW, with the basis (what is known) and the gap (what is unverified). State what specific information would materially raise the confidence level.

SIGNAL BOUNDARY: this is a sizing signal, not a plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Interrogative Register

**Axis**: D — Phrasing register (questions-as-structure; the model answers each question in sequence)
**Hypothesis**: Interrogative framing eliminates criterion omission — you cannot skip a question by forgetting the checklist; the questions are the structure. The model cannot produce a bare confidence label if the question asks "what makes you say that?"

```
Auto-detect topic from context. Do not prompt unless context absent.

Answer each question in sequence. Each answer is a required output section. Do not skip.

Q1 — WORKAROUND: What does a team do today in the absence of this feature? Name it specifically. Is building this feature cheaper, comparable, or more expensive than maintaining that workaround indefinitely?

Q2 — INTEGRATION POINTS: What systems, services, APIs, data stores, auth layers, UI surfaces, and background jobs does this feature touch? Name each one. How many total integration points?

Q3 — COMPLEXITY TIER: Is this LOW, MEDIUM, HIGH, or XL? (Use exactly this vocabulary.) What one or two factors most drive that rating?

Q4 — SENSITIVITY: What single condition would push this tier one step up? What single condition would push it one step down?

Q5 — TEAM COMPOSITION: What specialist disciplines are needed? (Name types, not headcount — e.g., "1 backend engineer, 1 frontend engineer, 0.5 PM.") What is the sprint range for delivery?

Q6 — CONFIDENCE: How confident are you in this sizing? (HIGH / MEDIUM / LOW.) What do you know that supports that rating? What is unverified? What specific investigation result would change it?

SIGNAL BOUNDARY: do not answer with task breakdowns, sprint assignments, owner names, or milestone dates. This is a sizing signal, not a plan.

Stock roles: Inertia Auditor (Q1), Surface Mapper (Q2), Complexity Analyst (Q3-Q4), PM Estimator (Q5), Confidence Reviewer (Q6).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Inertia-First + Table + Sensitivity Block (Combination)

**Axes**: A (inertia framing) + B (table format) + E (aspirational depth: explicit sensitivity and calibration)
**Hypothesis**: Combining inertia-first ordering with table structure plus explicit sensitivity/calibration prompts closes all four failure modes simultaneously — silent inertia (C-03) is blocked by the opening requirement, plan creep (C-05) is blocked by table structure, tier vocabulary (C-02) is enforced by column definition, and bare confidence (C-04) is blocked by the mandatory calibration section.

```
Auto-detect topic from context. Do not prompt unless context absent.

REQUIRED OPENING — INERTIA CHECK (before any table):
State the current workaround or status-quo behavior in one sentence. State whether building this feature is cheaper, comparable, or more expensive than continuing that workaround. No table needed — one or two sentences. This section is mandatory; omitting it fails the signal.

Then produce three tables:

TABLE 1 — SURFACE AREA
| Integration Point | Type | Notes |
One row per named touchpoint (API, data store, auth layer, UI surface, background job, webhook, external service).
Final row must be: | **Total** | — | **N integration points** |

TABLE 2 — SIZING
| Dimension | Value | Notes |
| Complexity tier | LOW / MEDIUM / HIGH / XL | Primary driver (the factor most responsible) |
| Team composition | Specialist types + FTE signal | e.g., "1 backend engineer, 0.5 PM" — no headcount only |
| Timeline signal | Sprint range | e.g., "3–5 sprints" — no calendar dates, no point estimates |
| Tier UP condition | Condition that raises the tier one step | Required |
| Tier DOWN condition | Condition that lowers the tier one step | Required |

TABLE 3 — CONFIDENCE
| Dimension | Value |
| Confidence level | HIGH / MEDIUM / LOW |
| Basis | What you know that supports this rating |
| Open gap | What is unverified |
| What would raise it | Specific investigation or result that would increase confidence |

SIGNAL BOUNDARY: no task breakdowns, sprint assignments, owner names, or milestone dates anywhere in the artifact.

Stock roles: Inertia Auditor (opening), Surface Mapper (Table 1), Complexity Analyst (Table 2 rows 1 and 4-5), PM Estimator (Table 2 rows 2-3), Confidence Reviewer (Table 3).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```
