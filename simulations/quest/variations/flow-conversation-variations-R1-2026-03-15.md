Here are the 5 variations:

---

## V-01 — Role Sequence
**Axis:** Establish Copilot Studio expert role *before* the task description.
**Hypothesis:** Priming CS vocabulary (trigger phrases, system topics, redirect nodes, session variables) in the role block causes domain terms to appear throughout the simulation organically, improving C-08. The defect labels also arrive in CS-specific language rather than generic chatbot vocabulary.

**Structure:** Role block → Step 1 (topic inventory) → Step 2 (happy path) → Step 3 (exception path) → Step 4 (defect scan, 4 types) → Step 5 (coverage summary). Prose-led with minimal table requirements.

**Expected coverage:** C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PARTIAL (may stay abstract), C-06 PARTIAL, C-07 PARTIAL, C-08 PASS, C-09 PARTIAL.

---

## V-02 — Output Format (table-heavy)
**Axis:** Require specific table schemas for trace and defect report.
**Hypothesis:** A table cell cannot be left blank without signaling an omission. The dialog trace table forces C-03 (both sides per turn) because the columns for User Utterance and Agent Response are separate. The defect report table forces C-02 (all 4 types) because every row is a named defect type with a required Verdict cell.

**Structure:** 5 sections, each with a required table schema. Prose only where the table structure can't carry the content. No phase gates.

**Expected coverage:** C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PASS, C-06 PARTIAL (2 trace tables present but divergence may be weak), C-07 PASS, C-08 PARTIAL (tables use generic column headers), C-09 PARTIAL.

---

## V-03 — Lifecycle Emphasis
**Axis:** Named phase gates with explicit entry/exit conditions.
**Hypothesis:** A phase that is labeled and has an exit condition forces the model to complete it before proceeding. The defect scan phase (Phase 4) has four sub-checks with required verdict lines — this structurally prevents the "no issues found" collapse that fails C-02.

**Structure:** 5 named phases (TOPIC INVENTORY → HAPPY PATH → EXCEPTION PATH → DEFECT SCAN → REMEDIATION + COVERAGE). Each phase has an entry condition, an exit condition, and instructions. Mix of prose and tables.

**Expected coverage:** C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PASS, C-06 PASS, C-07 PASS, C-08 PARTIAL, C-09 PARTIAL (remediation is present but specificity not enforced).

---

## V-04 — Role Sequence + Phrasing Register
**Axis:** Authoritative CS expert role + formal imperative directives throughout.
**Hypothesis:** The role establishes what specificity looks like in this domain; imperative directives ("you MUST name the node," "do not write 'add better error handling'") close the C-09 loophole. Generic advice becomes structurally impossible — the directives name the failure mode explicitly and prohibit it.

**Structure:** Role block → 5 numbered sections with directive language. Tables optional but encouraged. Every criterion has at least one "MUST" clause that corresponds to its pass condition.

**Expected coverage:** C-01–C-09 all PASS. C-09 in particular is targeted by explicit "what specificity looks like" framing.

---

## V-05 — Lifecycle + Output Format + Phrasing Register (ceiling)
**Axis:** All three structural axes combined.
**Hypothesis:** Phase gates prevent phase omission. Table schemas with required columns force completeness. Imperative directives ("ALL FOUR defect type rows MUST appear," "Do NOT leave Agent Response blank") close specificity gaps. No discretionary space remains. This variation is designed to achieve ceiling coverage on all 9 criteria in a single run.

**Structure:** 5 named phases, each with a gate condition and a required table schema. Every table column is named. Every defect type has a required Severity column. The remediation table requires a "Copilot Studio Object to Edit" column — forcing CS-specific vocabulary in C-09 answers.

**Expected coverage:** C-01–C-09 all PASS. The Copilot Studio Object column in the remediation table specifically targets C-08+C-09 together.

---

**File written to:** `simulations/quest/golden/flow-conversation-variate-R1-2026-03-15.md`

**Key design decisions:**
- V-01 through V-03 are single-axis. Each targets a different rubric gap: V-01 targets C-08 (vocabulary), V-02 targets C-02+C-03 (completeness by structure), V-03 targets C-02+C-06+C-07 (phase gates).
- V-04 combines role + register specifically to close C-09 — the criterion most likely to fail in earlier variations because the model produces generic advice without being explicitly prohibited from doing so.
- V-05 is the ceiling: the "Copilot Studio Object to Edit" column in the remediation table forces both C-08 and C-09 simultaneously, since naming a CS-specific UI path requires using CS vocabulary *and* being specific about what to change.
