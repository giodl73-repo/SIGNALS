Now I have all 5 variation designs. Scoring each against the v3 rubric criteria.

---

## Quest Score — scout-inertia R3

*Scoring variation designs (no trace artifact — structural enforcement evaluated)*

**Formula (v3):**
```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 4 * 10)
```
**Golden threshold**: all 5 essential pass AND composite >= 80.

---

## V-01 — Question-Primed Tables

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | **PASS** | Section 1 table requires tool/process, role (with A-04 gate blocking progression), frequency, output artifact. Prose-first question forces formulated role answer before table entry. |
| C-02 Costs quantified | **PASS** | Section 2 Estimate column: `[number or range — "high"/"low" not accepted]`. Three dimension rows. C-02 self-score enforces ≥2 cells with numbers. |
| C-03 Inertia HIGH | **PASS** | Section 2 states "Inertia threat score: HIGH (default)" inline. C-03 self-score present. |
| C-04 Why inertia loses | **PASS** | Section 4 DC table: `Observable trigger [falsifiable — a third party can confirm]` column header. Falsifiability check instructs per-row verification. C-04 self-score requires ≥2 falsifiable conditions. |
| C-05 Failure modes | **PASS** | Section 3: `Trigger [specific input, volume threshold, or workflow event — not a general category]` and `User-visible symptom [observable without reading a log]` column contracts. Column contract prose makes "manual is slow" visibly inconsistent. |
| R-01 Team type scoped | **PASS** | Section 4 DC table has `Team type [specific role or team context — not "all users" or "teams"]` column. R-01 self-score. |
| R-02 Role-level precision | **PASS** | A-04 gate blocks Section 2 entry if role cell contains department/vague label. R-02 self-score checks all actors in Sections 1 and 4. |
| R-03 Cost cited to role | **PASS** | Section 2 Basis column: `[analogy, comparable migration, stated assumption, or explicit uncertainty range]`. R-03 self-score requires role name + Basis anchor in at least one row. |
| A-01 Per-section gate | **PASS** | Self-score checkboxes (PASS/FAIL) in Sections 1–4 with stated pass conditions. Section 5 is composite gate. |
| A-02 Column constraints | **PASS** | Multiple columns carry embedded type constraints: role not department, number not label, observable trigger, user-visible symptom. Column contract prose reinforces at point of entry. |
| A-03 Composite gate w/ back-pointers | **PASS** | Section 5 table: "Return to if FAIL" column names specific sections. A-03 declared as completion blocker, not advisory score. |
| A-04 Role precision as continuation gate | **PASS** | Explicit "A-04 — Role precision gate" in Section 1 with named failure words ("teams", "users", "people") and explicit stop instruction before Section 2. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/4 = 10
**Score: 100** | **Golden: YES**

---

## V-02 — Team-Segmented with Synthesis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | **PASS** | Shared workaround table (name, tool, data handled, output) + A1/B1 actor tables (role, frequency, volume). A-04 gates in both passes. C-01 self-scores for Pass A and Pass B. |
| C-02 Costs quantified | **PASS** | A2 and B2 tables: `Estimate [number or range]` column. At least one Basis anchor required. C-02 self-score for each pass. |
| C-03 Inertia HIGH | **PASS** | Dedicated Inertia Threat Score section with HIGH default, table for mitigation documentation. C-03 self-score. |
| C-04 Why inertia loses | **PASS** | Mandatory synthesis section (explicit "Do not skip it") requires ≥2 team-type-scoped falsifiable conditions referencing DC-A and DC-B IDs. C-04 self-score in synthesis with own gate. Direct repair of R2 V-02 failure. |
| C-05 Failure modes | **PASS** | A3/B3 tables with specific trigger + user-visible symptom contracts per pass. C-05 self-scores for both. |
| R-01 Team type scoped | **PASS** | Team segmentation is the organizing axis (Pass A / Pass B). Synthesis R-01 self-score notes "structurally satisfied by Pass A / Pass B." R-01 cannot fail if synthesis references DC-A and DC-B IDs. |
| R-02 Role-level precision | **PASS** | A-04 gates in both passes. Composite gate checks R-02 for both segments. |
| R-03 Cost cited to role | **PASS** | A2/B2 Basis columns. R-03 self-scores in both passes. |
| A-01 Per-section gate | **PASS** | Self-scores in A1, A2, A3, A4, B1, B2, B3, Synthesis, and composite. Most gates per variation. |
| A-02 Column constraints | **PASS** | A2/B2 Unit columns carry role reference ("hours or days per [role from A1]"). A3/B3 trigger and symptom constraints. DC tables have Falsifiable? column. |
| A-03 Composite gate w/ back-pointers | **PASS** | Composite gate table with Pass A / Pass B / Synthesis columns and "Return to if FAIL." A-03 gate function stated. |
| A-04 Role precision as continuation gate | **PASS** | A-04 gate in both Pass A (A1) and Pass B (B1) with identical language. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/4 = 10
**Score: 100** | **Golden: YES**

---

## V-03 — Failure-First with Explicit C-01 Gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | **PASS** | Step 2 is a formal C-01 declaration with all 4 pass conditions quoted verbatim. C-01 self-score explicitly states FAIL redirects to Step 1 to find more specific failures — the only variation with a cascading C-01 gate. |
| C-02 Costs quantified | **PASS** | Step 3 table: `Estimate [number or range — "high"/"low" not accepted]` column. C-02 self-score. |
| C-03 Inertia HIGH | **PASS** | Step 3 states "Inertia threat score: HIGH (default)." C-03 self-score. |
| C-04 Why inertia loses | **PASS** | Step 4 DC table: `Defeat condition must be falsifiable` contract. Column contract requires observable threshold. C-04 self-score. All NO entries in Falsifiable? column must be rewritten before continuing. |
| C-05 Failure modes | **PASS** | Step 1 is the opening section — fail-first ordering ensures FM quality before anything else. Trigger and symptom column contracts present. C-05 self-score blocks Step 2 if triggers are not specific. |
| R-01 Team type scoped | **PASS** | Step 4 DC table: `Team type this applies to [specific role or context]` column. R-01 self-score. |
| R-02 Role-level precision | **PASS** | A-04 gate in Step 2 (the reconstruction step). R-02 self-score in Step 4. |
| R-03 Cost cited to role | **PASS** | Step 3 Basis column with R-03 self-score. |
| A-01 Per-section gate | **PASS** | Self-score checkboxes in Steps 1–4. |
| A-02 Column constraints | **PASS** | Step 1: `Specific trigger [concrete input, volume threshold, or workflow event — not a category]`. Step 4: `Defeat condition` with falsifiability requirement. |
| A-03 Composite gate w/ back-pointers | **PASS** | Composite gate table with step-level back-pointers. Noteworthy: C-01 FAIL in Step 2 → "Step 2 → Step 1 if blocked" — only variation where C-01 failure cascades back two steps. |
| A-04 Role precision as continuation gate | **PASS** | A-04 gate in Step 2 with step-continuation blocking. Framing note: "The failures from Step 1 reveal who is responsible — use that to name the role precisely." |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/4 = 10
**Score: 100** | **Golden: YES**

---

## V-04 — Adversarial Advocate / Rebuttal

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | **PASS** | Section 1 "Workaround identity" table with role constraint and A-04 gate. C-01 self-score: "The advocate cannot argue for a workaround it has not named." |
| C-02 Costs quantified | **PARTIAL → FAIL** | ARG table `Quantified switching cost [number + unit + basis]` column enforces numbers. But rubric C-02 requires ≥2 of *three specific dimensions* (time/training/disruption). V-04's C-02 self-score reframes to "At least 2 ARG rows carry a number" — this drops the dimensional coverage requirement. Two ARG rows could both address time cost; training and disruption dimensions may go unquantified. |
| C-03 Inertia HIGH | **PASS** | Section 1: "Inertia threat score: HIGH (the advocate is winning this section by design)." C-03 self-score. |
| C-04 Why inertia loses | **PASS** | Section 2 REB table: `Defeat condition (falsifiable) — Teams switch when [observable threshold]` column. Each rebuttal must address its specific ARG by name. C-04 self-score requires ≥2 REB rows with falsifiable conditions. Adversarial framing produces specificity under contest. |
| C-05 Failure modes | **PASS** | Section 2 FM table with `Trigger [specific input, volume, or event that the advocate case assumed would not happen]` — framing is novel (failures as advocate vulnerabilities). `User-visible symptom` column present. C-05 self-score. |
| R-01 Team type scoped | **PASS** | REB table `Team type this applies to` column. R-01 self-score. |
| R-02 Role-level precision | **PASS** | A-04 gate in Section 1. R-02 self-score in Section 2. |
| R-03 Cost cited to role | **PASS** | ARG table has inline basis (`[number + unit + basis]`). R-03 self-score checks ARG table basis field. |
| A-01 Per-section gate | **PASS** | Self-scores in Sections 1 and 2. |
| A-02 Column constraints | **PASS** | `Advocate argument [must be a specific reason — "it works" fails]`, `Quantified switching cost [must carry a number]`, `Defeat condition (falsifiable)`, `Team type [specific type, not "all users"]`. |
| A-03 Composite gate w/ back-pointers | **PASS** | Composite gate with section back-pointers. A-03 note: "quality of Section 2 depends on quality of Section 1." |
| A-04 Role precision as continuation gate | **PASS** | A-04 gate in Section 1: "A strong advocate knows exactly who bears the switching cost." |

**Essential**: 4/5 (C-02 PARTIAL → FAIL) = 48 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/4 = 10
**Score: 88** | **Golden: NO** — fails all-essential-pass gate; C-02 structural gap allows two ARG rows to cover the same dimension without triggering FAIL.

---

## V-05 — Progressive Commitment Chain

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | **PASS** | Step 1 declares ACTOR-01, WA-01, WA-01-tool, WA-01-output, WA-01-freq as named identifiers. C-01 self-score checks all five. A-04 gate: "a vague actor corrupts the entire chain." |
| C-02 Costs quantified | **PASS** | Step 2 table: every row must name ACTOR-01 in the Unit cell. `Estimate for ACTOR-01 [number or range]`. Three dimension rows. C-02 self-score. |
| C-03 Inertia HIGH | **PASS** | Step 2: "Inertia threat score: HIGH (default)." C-03 self-score. |
| C-04 Why inertia loses | **PASS** | Step 4 DC table requires FM ID citation for each defeat condition. "A defeat condition with no FM citation has no evidence anchor — it is a hypothesis without a root cause." Verdict section must use declared IDs. C-04 is structurally unreachable without evidence-grounded FM anchors. |
| C-05 Failure modes | **PASS** | Step 3 FM table: `Applies to which ACTOR [must reference ACTOR-01 or ACTOR-02 — not "users"]` column. Trigger and symptom contracts present. C-05 self-score requires ACTOR citation alongside trigger and symptom. |
| R-01 Team type scoped | **PASS** | Step 4 DC table: `Team type [specific — must name a role context, not "all users"]` column. R-01 self-score. |
| R-02 Role-level precision | **PASS** | Chain validation in Step 4 confirms every ACTOR reference traces back to Step 1. R-02 self-score: "Every ACTOR reference in Steps 2, 3, and 4 traces back to a declared ID." Strongest R-02 enforcement of all variations. |
| R-03 Cost cited to role | **PASS** | Step 2 Basis column. R-03 self-score. ACTOR-01 already embedded in every Unit cell by design. |
| A-01 Per-section gate | **PASS** | Self-score checkboxes in Steps 1–4. |
| A-02 Column constraints | **PASS** | Most comprehensive column constraints: `Role [not department]`, `[number or range]`, `Trigger [specific input, volume, or workflow event]`, `User-visible symptom [observable without a log]`, `Source FM IDs [must match declared IDs]`, `Team type [specific]`. ID citation requirement is itself a structural constraint. |
| A-03 Composite gate w/ back-pointers | **PASS** | Composite gate: "For R-02 failures, the chain validation in Step 4 names the exact step where the chain broke." C-01 failure propagates — explicit note that all downstream steps depend on declared identifiers. |
| A-04 Role precision as continuation gate | **PASS** | A-04 gate in Step 1: "Every subsequent section references ACTOR-01 — a vague actor corrupts the entire chain." Widest scope of any A-04 implementation. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/4 = 10
**Score: 100** | **Golden: YES**

---

## Rankings

| Rank | Variation | Score | Golden | Key differentiator |
|------|-----------|-------|--------|-------------------|
| T-1 | V-01 | 100 | YES | Prose-first two-pass attention; simplest, lowest friction |
| T-1 | V-02 | 100 | YES | Mandatory synthesis gate; strongest R-01 structural enforcement |
| T-1 | V-03 | 100 | YES | Failure-first ordering; cascading C-01 gate (unique) |
| T-1 | V-05 | 100 | YES | Commitment chain; FM citation as type requirement; strongest R-02 |
| 5 | V-04 | 88 | NO | C-02 structural gap: ARG rows enforce numbers but not dimensional coverage |

---

## Excellence Signals

Four variations tie at 100. The most structurally novel patterns come from **V-05** (commitment chain as top archetype) and **V-03** (cascading C-01 gate — unique across all variations):

**1. FM citation as structural type requirement (V-05)**
A defeat condition that cannot cite an FM ID is incomplete by construction — not instructionally vague but structurally broken. This makes unsupported defeat conditions visible as missing references rather than as quality gaps the reviewer must catch. The pattern is reusable in any skill where output section B must derive from output section A.

**2. Commitment chain with declared identifiers (V-05)**
Declaring ACTOR-01/WA-01/FM-01 as named identifiers before analysis begins, then enforcing reference discipline downstream, converts cross-section coherence from a review concern to a visible artifact property. A chain with a missing ID is structurally incoherent, not just weak.

**3. Cascading C-01 gate on reconstruction (V-03)**
C-01 FAIL in Step 2 does not send the analyst to Step 2 — it sends them back to Step 1 to find more specific failure modes. This is the only variation where improving workaround specificity requires improving failure mode specificity first. The gate encodes the epistemological relationship: actor/frequency/artifact emerge from understanding where the workaround breaks.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["FM citation as structural type requirement — defeat conditions must cite a failure mode ID; without an evidence anchor the entry is structurally incomplete, not just weak", "Commitment chain with declared identifiers — ACTOR-ID/WA-ID/FM-ID declared in Step 1 and referenced by name throughout; broken reference is visible cross-section incoherence rather than a vague entry", "Cascading C-01 gate on workaround reconstruction — C-01 FAIL redirects to failure-mode discovery, encoding that actor/frequency/artifact specificity is downstream of failure-mode specificity"]}
```
