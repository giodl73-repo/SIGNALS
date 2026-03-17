I now have all the information I need. Let me score all five variations.

---

# Scorecard — corps-rob R5 (rubric v4, 2026-03-17)

## Context

All five R5 variations build on V-02 R4's proven base (99 under v4: C-16 PASS, C-17 PASS, C-18 FAIL). The sole probe is C-18 (Explicit Lens Declaration Fill Field). Every variation preserves V-02 R4's essential and recommended structure unchanged. Differences are limited to where and how the `Lens:` fill field appears in the output.

**V-02 R4 baseline under v4**: all essential PASS, all recommended PASS, C-09 through C-17 all PASS, C-18 FAIL → 9/10 → 99.

---

## Scoring Formula (v4)

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-18 | N_pass / 10 x 10 |

PARTIAL = 0.5 pass. Ceiling = 100.

---

## V-01 -- Lens: as 5th Briefing Envelope Field

**Mechanism**: Adds `Lens: [role title] -- [domain-specific dimension]` as the 5th field in the briefing envelope (after PRIOR STAGE SUMMARY, KEY CONCERNS, OPEN QUESTION FORWARDED, INERTIA STATUS). Stage 1 receives a standalone `Lens:` field in Part 2 Stage Identity.

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Six canonical stage headers with role title per stage. |
| C-02 | PASS | 4-field briefing envelope with KEY CONCERNS lens-directed selection; lens governs findings orientation. |
| C-03 | PASS | Full 5-part structure per stage; VERDICT token; numbered findings with HIGH/MED/LOW. |
| C-04 | PASS | Minimum 2 findings per stage with Owner + Resolution; Stage 2+ requires >=1 addressing OPEN QUESTION FORWARDED. |
| C-05 | PASS | Go/No-Go section in TPM stage with F-ID or R-ID rationale. |

All 5 essential: **PASS**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Risk Register table (min 3 entries; >=1 HIGH/HIGH or HIGH/MED). |
| C-07 | PASS | Mission Cascade table with named (non-generic) mission. |
| C-08 | PASS | Prior-Stage Lens Impact (min 1 per stage, traces to role lens) + DOWNSTREAM RISK SHIFT in packet (>=5 entries for 6-stage run). |

All 3 recommended: **PASS**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER: YES/NO field in every handoff packet. |
| C-10 | PASS | Cross-Cutting Themes (Section A), min 2 themes with >=2 F-IDs from different stages. |
| C-11 | PASS | Handoff Packet at every stage close with DOWNSTREAM RISK SHIFT entries. |
| C-12 | PASS | BLOCKER field at every stage boundary. |
| C-13 | PASS | INERTIA ANCHOR before Stage 1; INERTIA CHECK per stage. |
| C-14 | PASS | 4-field briefing envelope preserved from V-02 R4: PRIOR STAGE SUMMARY + KEY CONCERNS (lens-directed, "Generic selection fails") + OPEN QUESTION FORWARDED + INERTIA STATUS. Stage-open position before findings. |
| C-15 | PASS | "Do not copy the lens impact into the risk shift" explicit negative constraint in Part 4 preamble. |
| C-16 | PASS | `### Prior-Stage Lens Impact` in findings body (source stage + F-ID + how orientation changes reading) + `DOWNSTREAM RISK SHIFT` in handoff packet (downstream consequence visible at this stage). Both present and distinct. |
| C-17 | PASS | "Do not copy the lens impact into the risk shift" -- explicit anti-copy guard for C-16 pair. |
| C-18 | **PASS** | `Lens: [role title] -- [domain-specific dimension]` is an explicit, labeled fill field added as the 5th briefing envelope field. C-14 passes independently via KEY CONCERNS mechanism, so this Lens: field is ADDITIONAL to C-14, not the same as it. Examples required ("Generic form fails"). Stage 1 standalone Lens: in Stage Identity covers the no-envelope stage. Risk note: Lens: appears after KEY CONCERNS (position 5), meaning the declaration is post-context-loading rather than pre-context. However, C-18 requires "labeled declaration field in the output naming the orientation dimension" -- position within the envelope does not override the field's existence. PASS. |

Aspirational: **10/10**

### Composite

```
(5/5 x 60) + (3/3 x 30) + (10/10 x 10)
= 60 + 30 + 10
= 100
```

---

## V-02 -- LENS ACTIVATION Block as Part 0 (Before Briefing Envelope)

**Mechanism**: Adds a dedicated `LENS ACTIVATION` block as Part 0 at every stage, before any context loading or briefing envelope. Stage sequence becomes 6 parts: Part 0 (LENS ACTIVATION) → Part 1 (Briefing Envelope) → Part 2 (Stage Identity) → Part 3 (Findings) → Part 4 (Stage Close). KEY CONCERNS in Part 1 is explicitly directed to use the Lens declared in Part 0. All V-02 R4 mechanisms preserved intact. ROB Summary now tracks "LENS ACTIVATION CHAIN HEALTH."

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Six canonical stage headers + role title. |
| C-02 | PASS | LENS ACTIVATION block forces lens declaration before any context-loading. KEY CONCERNS selection now explicitly traced to the declared Lens ("selected through the Lens declared in Part 0"). Role-loaded perspective is structurally prior to all findings work. |
| C-03 | PASS | All structural elements present per stage; VERDICT token; numbered findings. |
| C-04 | PASS | Min 2 findings per stage with Owner + Resolution. |
| C-05 | PASS | Go/No-Go in TPM stage. |

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Risk Register table. |
| C-07 | PASS | Mission Cascade table. |
| C-08 | PASS | Prior-Stage Lens Impact (Part 3, references "the role's orientation declared in Part 0") + DOWNSTREAM RISK SHIFT in handoff. The Part 0 → KEY CONCERNS → Prior-Stage Lens Impact chain is now mechanically explicit. Strongest C-08 implementation in R5. |

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER field per stage. |
| C-10 | PASS | Cross-Cutting Themes section end-of-run. |
| C-11 | PASS | Handoff Packet at every stage close. |
| C-12 | PASS | BLOCKER at every stage boundary. |
| C-13 | PASS | INERTIA ANCHOR + INERTIA CHECK preserved. |
| C-14 | PASS | 4-field briefing envelope unchanged from V-02 R4. KEY CONCERNS instruction now references "the Lens declared in Part 0" -- this strengthens C-14 by making the lens reference mechanically upstream. |
| C-15 | PASS | Explicit "do not copy the lens impact into the risk shift" in Part 4 preamble. |
| C-16 | PASS | Prior-Stage Lens Impact + Downstream Risk Shift pair both present. Part 3 Prior-Stage Lens Impact entry explicitly requires tracing to "the Lens declared in Part 0, not generic escalation." |
| C-17 | PASS | Anti-copy guard preserved and strengthened (same guard text as V-02 R4). |
| C-18 | **PASS (strong)** | `LENS ACTIVATION` block with `Lens: [role title] -- [domain-specific dimension]` is a dedicated, standalone output block appearing BEFORE briefing envelope and findings. This is structurally prior to context loading -- the declaration governs KEY CONCERNS selection, not follows it. Stage 1 (no briefing envelope) receives Part 0 before Stage Identity. This is the clearest C-18 implementation in R5: lens declared before context, traceable to KEY CONCERNS, traceable to Prior-Stage Lens Impact. |

Aspirational: **10/10**

### Composite

```
= 60 + 30 + 10 = 100
```

---

## V-03 -- Lens: as Inline ROLE Line Declaration

**Mechanism**: Smallest-footprint approach. Extends the ROLE line in Stage Identity with a pipe-separated Lens: declaration: `ROLE: [name] -- [orientation] | Lens: [role title] -- [domain-specific dimension]`. No new block or section added. 4-field briefing envelope unchanged. C-14 satisfied independently.

### Essential Criteria

All 5: **PASS** (5-part structure unchanged; role attribution, findings, verdict all preserved)

### Recommended

All 3: **PASS**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER per stage. |
| C-10 | PASS | Cross-Cutting Themes section end-of-run. |
| C-11 | PASS | Handoff Packet per stage. |
| C-12 | PASS | BLOCKER per stage boundary. |
| C-13 | PASS | INERTIA ANCHOR + INERTIA CHECK preserved. |
| C-14 | PASS | 4-field briefing envelope unchanged. |
| C-15 | PASS | Anti-copy guard preserved. |
| C-16 | PASS | Prior-Stage Lens Impact + Downstream Risk Shift pair. The Prior-Stage Lens Impact instruction explicitly requires tracing to "the Lens declared in ROLE line above." |
| C-17 | PASS | Anti-copy guard preserved. |
| C-18 | **PARTIAL** | `Lens:` label is present and requires a fill value with domain examples ("Generic form fails"). Distinct from C-14 (in Stage Identity, not briefing envelope). However, inline pipe-separator extension of an existing field (`ROLE:`) is not a "dedicated declaration field" in the same sense as a standalone labeled field on its own line. C-18's canonical form (V-04 R4 STAGE-OPEN FORWARD `Lens:` field) has the declaration on its own line within a block. The inline form satisfies C-18's label and fill requirements but not its structural independence requirement. PARTIAL. |

Aspirational: **9.5/10**

### Composite

```
(5/5 x 60) + (3/3 x 30) + (9.5/10 x 10)
= 60 + 30 + 9.5
= 99.5
```

---

## V-04 -- LENS ACTIVATION Block + Briefing Envelope Lens: Field (Belt-and-Suspenders)

**Mechanism**: Combines V-01 and V-02. Part 0 LENS ACTIVATION block (pre-context) + `Lens:` as 5th briefing envelope field (post-context, "confirm or refine the LENS ACTIVATION declaration after seeing context"). Dual-presence: declared before context loads, then verified/refined after context loads. ROB Summary monitors "LENS DECLARATION CHAIN: Did LENS ACTIVATION declarations match briefing envelope Lens: confirmations?" Stage 1 has Part 0 LENS ACTIVATION only (no envelope).

### Essential Criteria

All 5: **PASS**

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Risk Register table. |
| C-07 | PASS | Mission Cascade table. |
| C-08 | PASS | Prior-Stage Lens Impact (traces to "Lens declared in LENS ACTIVATION") + DOWNSTREAM RISK SHIFT. Chain from LENS ACTIVATION → KEY CONCERNS → Prior-Stage Lens Impact is explicit. |

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER per stage. |
| C-10 | PASS | Cross-Cutting Themes section. |
| C-11 | PASS | Handoff Packet per stage. |
| C-12 | PASS | BLOCKER per stage boundary. |
| C-13 | PASS | INERTIA ANCHOR + INERTIA CHECK preserved. |
| C-14 | PASS | Briefing envelope: PRIOR STAGE SUMMARY + KEY CONCERNS (directed by LENS ACTIVATION) + OPEN QUESTION FORWARDED + INERTIA STATUS + Lens: (confirmation field). C-14 passes on the first four fields independently; the 5th field strengthens it further. |
| C-15 | PASS | Anti-copy guard preserved. |
| C-16 | PASS | Prior-Stage Lens Impact + Downstream Risk Shift pair. |
| C-17 | PASS | Anti-copy guard. |
| C-18 | **PASS (strong)** | Two independent C-18-satisfying declarations: (1) Part 0 LENS ACTIVATION standalone block with `Lens:` fill field before context loads -- this alone satisfies C-18; (2) briefing envelope 5th field `Lens:` confirm/refine after context loads. Belt-and-suspenders ensures C-18 regardless of which placement the rubric scores. Additionally, the dual-stage declaration (pre-context vs post-context) creates a new structural dimension: the lens can be refined when prior-stage context shifts the orientation. |

Aspirational: **10/10**

### Composite

```
= 60 + 30 + 10 = 100
```

---

## V-05 -- Lens: as 5th+ Envelope Field + Inertia Evolution Thread

**Mechanism**: Combines V-01 (Lens: in briefing envelope) with V-03 R4's inertia evolution thread (INERTIA EVOLUTION field per stage, INERTIA TRAJECTORY section end-of-run). Briefing envelope grows to 6 fields: PRIOR STAGE SUMMARY, KEY CONCERNS, OPEN QUESTION FORWARDED, INERTIA EVOLUTION, INERTIA STATUS, Lens:. Stage 1 gets standalone Lens: in Stage Identity. End-of-run sections: A (Cross-Cutting Themes) + B (INERTIA TRAJECTORY table) + C (ROB Summary).

### Essential Criteria

All 5: **PASS**

### Recommended

All 3: **PASS**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | BLOCKER per stage. |
| C-10 | PASS | Cross-Cutting Themes (Section A). |
| C-11 | PASS | Handoff Packet per stage. |
| C-12 | PASS | BLOCKER per stage boundary. |
| C-13 | **PASS (strong)** | INERTIA ANCHOR + INERTIA CHECK + INERTIA STAGE READING per stage + INERTIA EVOLUTION in envelope + INERTIA TRAJECTORY end-of-run section. Exceeds C-13 pass condition comprehensively. |
| C-14 | PASS | 6-field briefing envelope. The original 4 C-14 fields are present; INERTIA EVOLUTION and Lens: are additional. C-14 passes on first four fields independently. |
| C-15 | PASS | Anti-copy guard preserved. |
| C-16 | PASS | Prior-Stage Lens Impact + Downstream Risk Shift pair, traced to declared Lens. |
| C-17 | PASS | Anti-copy guard preserved. |
| C-18 | **PASS** | `Lens: [role title] -- [domain dimension]` as 6th field in briefing envelope. C-14 passes independently; this Lens: field is additional (same analysis as V-01). Stage 1 standalone Lens: in Stage Identity. Examples required, generic form fails. PASS. Same position-risk as V-01 (lens after context, not before) -- does not override field presence for C-18. |

Aspirational: **10/10**

### Composite

```
= 60 + 30 + 10 = 100
```

---

## Summary Table

| Variation | Ess | Rec | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | N/10 | Score |
|-----------|-----|-----|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | 5/5 | 3/3 | P | P | P | P | P | P | P | P | P | **P** | 10/10 | **100** |
| V-02 | 5/5 | 3/3 | P | P | P | P | P | P | P | P | P | **P (strong)** | 10/10 | **100** |
| V-03 | 5/5 | 3/3 | P | P | P | P | P | P | P | P | P | **PARTIAL** | 9.5/10 | **99.5** |
| V-04 | 5/5 | 3/3 | P | P | P | P | P | P | P | P | P | **P (strong)** | 10/10 | **100** |
| V-05 | 5/5 | 3/3 | P | P | P | P | P+ | P | P | P | P | **P** | 10/10 | **100** |

**Rank**: V-02 = V-04 > V-01 = V-05 (all 100, by C-18 implementation strength) > V-03 (99.5)

---

## Key Discriminator: C-18

**C-03 note**: V-03's inline ROLE-line form earns PARTIAL -- the pipe-separated inline extension (`ROLE: ... | Lens: ...`) has the required label and fill field but is not a structurally independent field on its own line. C-18 canonical form (V-04 R4 STAGE-OPEN FORWARD) has Lens: as a standalone labeled entry. The inline form satisfies the content requirement but not the structural independence requirement.

**C-18 ordering note**: V-01 and V-05 place Lens: at the end of the briefing envelope (after KEY CONCERNS). This means the lens declaration appears AFTER context is loaded, not before -- the declaration follows the selection it should govern. V-02 and V-04 place the lens declaration BEFORE context loads (Part 0), making it causally prior. V-02 and V-04 are therefore the stronger C-18 implementations, though all four earn PASS on the criterion's letter (labeled fill field in output, naming orientation by practice domain).

---

## Excellence Signals (Top Scorers)

**V-02: `lens-activation-pre-context-block`** -- A standalone `LENS ACTIVATION` block (Part 0) appears before the briefing envelope at every stage. The lens is declared before any prior-stage context is loaded. KEY CONCERNS in Part 1 is explicitly directed to use the lens from Part 0. Prior-Stage Lens Impact in Part 3 is explicitly directed to trace to Part 0. This creates a complete causal chain: lens declared (Part 0) → governs context selection (Part 1) → governs prior-stage re-reading (Part 3). The declaration is causally prior to everything it governs.

**V-04: `lens-pre-post-context-dual-confirmation`** -- LENS ACTIVATION (pre-context, Part 0) + briefing envelope Lens: field (post-context, "confirm or refine the LENS ACTIVATION declaration after seeing context"). Dual-stage lens tracking tests whether prior-stage context shifts the role's orientation dimension. ROB Summary tracks "LENS DECLARATION CHAIN" health. New qualitative dimension: a lens refinement occurs when context reveals a more specific dimension than the pre-context declaration anticipated. This becomes a structural signal of context-sensitivity -- if the lens never refines, the activation is boilerplate; if it refines meaningfully, the stage is applying genuine contextual judgment.

**V-05: `inertia-trajectory-lens-integration`** -- Combines C-18 (Lens: envelope field) with the `inertia-evolution-trajectory` pattern from R4 (INERTIA EVOLUTION per stage + INERTIA TRAJECTORY section). The INERTIA TRAJECTORY compiles posture arc across all six stages. V-05 is the ceiling candidate for a potential C-19 elevation: displacement posture arc (which stage hardened/softened the anchor, and the net direction) is qualitatively distinct from per-stage inertia checks. Pattern combination coverage: C-13 (strong), C-14, C-16, C-17, C-18 all PASS.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["lens-activation-pre-context-block", "lens-pre-post-context-dual-confirmation"]}
```
