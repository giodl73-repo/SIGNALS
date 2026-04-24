Written to `simulations/quest/golden/trace-skill-variate-R5-v4-2026-03-15.md`.

---

## trace-skill R5 Variations (rubric v4)

**Entry state**: R4 V-04/V-05 already pass all 20 criteria. R5 makes C-18/C-19/C-20 structurally enforced rather than emergent from model depth.

**Core insight**: All three new criteria share the same failure mode -- *structural presence without structural enforcement*. Each variation converts one or more of these from "present when the model goes far enough" into "transcribed from schema."

---

### V-01 -- Single axis: Output format (Relay Schema / C-18)

**Axis**: Adds a "Relay Schema" block before Execute relay rows, declaring `Binding` as a required column with format constraint `InputName = "ResolvedValue"`. Relay rows are transcribed from the schema, not generated.

**Hypothesis**: Without a schema, C-18 is model-behavior-dependent -- input-name-only binding satisfies C-10 but fails C-18. The schema converts C-18 from depth signal to structural guarantee. The Format constraint cell includes a "Do NOT write input name only" prohibition.

**New criterion targeted**: C-18 only. C-19, C-20 remain at R4 V-02/V-03 baseline (FAIL).

---

### V-02 -- Single axis: Lifecycle emphasis (Bind Schema / C-19)

**Axis**: Unified "Bind Schema" block (3 parts) before resolution rows: Status Enum (C-16), Conflict Precedence Rule (C-17), and a new **Precedence Applied Vocabulary** table (`override` / `default` / `BLOCKED`) declaring `Precedence applied` as a required column with prohibited-form annotation.

**Hypothesis**: Without a named column declaration, per-row precedence annotation is optional decoration -- present when conflicts are visible, absent on clean rows. Schema-declaring the column makes every row carry it regardless of whether Conflict? = YES.

**New criterion targeted**: C-19 only. C-18, C-20 remain at baseline (FAIL).

---

### V-03 -- Single axis: Phrasing register (formal CLOSED ASSERTION / C-20)

**Axis**: After the Coverage Matrix BLOCKED gate passes, a named "CLOSED ASSERTION" block is produced as a separate structural element before Gather. The block opens with a canonical phrase ("The following Required=YES inputs are confirmed available...") and lists each Required=YES input by name. The Verdict cites this block by name -- making C-20 a positive citation rather than absence-of-BLOCKED inference.

**Hypothesis**: Without a named block, C-20 cannot be positively cited. The formal phrasing register (declarative, canonical opening phrase) ensures the block is visually distinct and structurally independent from the gate text.

**New criterion targeted**: C-20 only. C-18, C-19 remain at baseline (FAIL).

---

### V-04 -- Combined: Relay Schema (C-18) + Bind Schema (C-19)

**Axes**: V-01 + V-02 combined. Establishes a "declare-before-rows" rhythm across both production phases: Phase Label Schema (before phases) → Bind Schema (before Bind rows) → Relay Schema (before relay rows). Both schema declarations include prohibited-form statements to prevent soft compliance.

**Hypothesis**: C-18 and C-19 become schema-transcription behaviors together. Neither requires model depth -- both require schema conformance.

---

### V-05 -- Combined golden: C-18 + C-19 + C-20

**Axes**: All three R4 excellence patterns as explicit named structural elements. Adds the CLOSED ASSERTION block (V-03) to the V-04 architecture. Completes the full binding evidence chain: **Coverage Matrix → CLOSED ASSERTION (C-20) → Gather → Bind with per-row precedence (C-19) → Relay with verbatim binding pairs (C-18) → Verdict citing all three named blocks.**

The Verdict compliance ledger covers all 20 criteria (C-01 through C-20) with named structural evidence loci. Any schema declared but not applied produces a FAIL in its Verdict row -- failure is visible, not silent.
