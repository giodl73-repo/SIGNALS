Written to `simulations/quest/golden/flow-trigger-variate-R4-v2rubric-2026-03-16.md`.

---

## Round 4 Variations — flow-trigger (Rubric v2)

**Pre-read summary**: R3 achieved 100 on V-01–V-04 and 94 on V-05 (C-03 partial — no explicit `Reads:` / `Produces:` template in V-05's firing entry). Four excellence signals from R3: self-auditing gate markers (V-04), role isolation as structural barrier (V-01), FM catalog with detection signals (V-03), inertia naming proven insufficient without format templates (V-05).

---

### Variation Map

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Role sequence | Adds explicit **authority contracts** — paired mandate + prohibition per role. A Scanner that *cannot* produce conditions makes C-11 impossible to violate by structural constraint, not just instruction. Gate markers from R3 V-04 carried forward. |
| **V-02** | Output format | Unifies R3 V-02's two-pass ledger with R3 V-04's gate tokens: the ledger's **required columns ARE the gate checks**. An empty required column produces an inline gate token. Compliance is scannable from column fill. |
| **V-03** | Phrasing register | Unifies R3 V-03's FM catalog with R3 V-04's gate tokens: every FM check is also a gate token — `[FM-NN: CLEAR]` or `[FM-NN: VIOLATED — desc]`. One scan for `VIOLATED` tokens surfaces all defects. Adds FM-00 (protocol skip) as the meta-defect. |
| **V-04** | Role sequence + Lifecycle emphasis | Four roles each own one lifecycle **phase** and produce one named **artifact** (Manifest → Ledger → Analysis Bundle → Verdict Bundle). Compliance is verifiable from artifact presence; Phase N+1 gate blocks if Phase N artifact is incomplete. |
| **V-05** | Inertia framing + Output format | **Fixes R3 V-05's C-03 gap**: adds a FORMAT BLOCK to every override section showing the exact required output shape. Inertia naming motivates; the format block structurally enforces. A model following both cannot omit `Reads:` / `Produces:` as R3 V-05 did. |

---

### What's new over R3

| R4 Mechanism | Source | Improvement over R3 |
|---|---|---|
| Authority contracts (mandate + prohibition per role) | V-01 | R3 V-01 used mandates only — "your only output is...". R4 adds explicit prohibitions. Prohibited content appearing in a role's output is a *named structural violation*, not just an instruction miss. |
| Gate-per-column (column fill = gate pass) | V-02 | R3 kept ledger format and gate tokens as separate variations. R4 collapses them: any unfilled required column IS a visible structural gap without needing a separate gate check. |
| FM check = gate token (unified token system) | V-03 | R3 V-03 had `[FM-NN check]` markers; R3 V-04 had `[GATE N: PASSED/FAILED]`. R4 unifies these into a single `[FM-NN: CLEAR | VIOLATED]` system — one scan reveals everything. |
| Phase-artifact pipeline (artifact presence = compliance) | V-04 | R3 V-04 had gates between phases but no named artifacts. R4 makes each phase produce a **named, citable artifact**. Compliance review reduces to: do all four artifacts exist and are they complete? |
| Format block in override sections | V-05 | R3 V-05 named what the default does wrong but never showed the required output shape for firing entries (C-03 gap). R4 adds a FORMAT BLOCK per override that is structurally contractual. |
