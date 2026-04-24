**v18 written.** Two new criteria extracted from R17:

---

**C-50 -- DOWNSTREAM CITATION CONTRACT rows carry Gate H Status field per I-0X** (V-03 Axis C, 5 pts)
Each I-0X contract row in SECTION A carries a `Gate H Status: [PASS / FAIL -- cite location or violation]` fill field completed by Gate H during audit. Contract row becomes both audit target and audit record — declaration and compliance co-present in the same structural slot. Without C-50, Gate H audits against the contract (C-49) but records outcomes in a separate location; with C-50, the contract is a live audit ledger. Dependency: C-49.

**C-51 -- SECTION K mirrors DOWNSTREAM CITATION CONTRACT compliance as terminal contract record** (V-02 Axis B, 5 pts)
SECTION K carries a per-I-0X compliance mirror of the DOWNSTREAM CITATION CONTRACT — which citation sinks were satisfied and where. Completes the contract lifecycle: source declaration (C-49, SECTION A) → per-row audit co-location (C-50, Gate H Status) → terminal compliance record (C-51, SECTION K). Without C-51, a reader must cross-reference SECTION A and Gate H to determine contract compliance; with C-51, SECTION K is sufficient as both gate execution proof and contract compliance proof. Dependency: C-49, C-20.

---

**Max: 295 → 305. Golden threshold (80%): 244 pts. Paradox ceiling: 300/305** (C-19 structural FAIL persists).

New dependency chain additions:
```
C-49 -> C-50
C-49 + C-20 -> C-51
```
