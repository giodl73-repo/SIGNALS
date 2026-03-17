## trace-skill — Round 3 Scoring / rubric-v3

### Scoring Method

```
Score = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/9 × 10)
Each essential criterion = 12 pts  |  Each recommended = 10 pts  |  Each aspirational ≈ 1.11 pts
Golden threshold: all 5 essential PASS + composite ≥ 80
```

---

### V-01 — Single axis: Lifecycle / Phase Label Schema preamble

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Four phases in sequence | **PASS** | Gather / Bind / Execute / Verdict headers present in order |
| C-02 | Gather enumerates inputs by name + source | **PASS** | Table with Input Name, Source, Value/Description, Gap? columns |
| C-03 | Bind maps every Gather input to one resolved value | **PASS** | Bind table with Gathered Value / Resolved Value / Status per row |
| C-04 | Execute produces artifact with correct naming | **PASS** | `{topic}-{signal}-{date}.md` filename; instruction to produce every required section |
| C-05 | Verdict declares PASS/FAIL with rationale | **PASS** | Overall row in Verdict table |
| C-06 | Exact schema labels | **PASS** | Phase Label Schema preamble locks headers; transcription, not generation |
| C-07 | Verdict cites criterion IDs | **PASS** | Verdict table rows C-01 through C-14 with IDs |
| C-08 | No elision markers | **PASS** | Execute instruction: "No elision markers anywhere" |
| C-09 | Coverage Matrix with closed-world preamble | **FAIL** | Not present |
| C-10 | Execute relay carry; Verdict reads relay | **FAIL** | No relay table |
| C-11 | Spec-first Gather (two tiers) | **FAIL** | Single-tier Gather; no tier separation |
| C-12 | Coverage Matrix BLOCKED gate | **FAIL** | No Coverage Matrix |
| C-13 | Artifact delimiter markers | **PASS** | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` in Execute |
| C-14 | Phase Label Schema table declared pre-trace | **PASS** | Explicit immutable preamble block before Gather; "transcribed from this table" instruction |
| C-15 | Verdict compliance ledger (ID\|Result\|Evidence) | **PASS** | Verdict table has ID, Criterion (brief), Result, Evidence columns; Evidence column cites structural loci |
| C-16 | Bind three-value Status Enum declared | **PASS** | "Status vocabulary (three values only)" block with RESOLVED / UNRESOLVED / BLOCKED defined; all three members explicit |
| C-17 | Bind conflict precedence rule declared | **FAIL** | No conflict precedence rule block in Bind |

**Aspirationals passing**: C-13, C-14, C-15, C-16 = **4 / 9**

**Score V-01**: 60 + 30 + (4/9 × 10) = **94.4**

---

### V-02 — Single axis: Output format / Verdict compliance ledger + Bind Status Enum

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Four phases in sequence | **PASS** | Gather / Bind / Execute / Verdict |
| C-02 | Gather enumerates inputs | **PASS** | Table with Input Name, Source, Value, Present? columns |
| C-03 | Bind maps all Gather inputs | **PASS** | Resolution table; one row per input; Resolved Value column |
| C-04 | Execute produces artifact | **PASS** | Filename template; no-elision instruction |
| C-05 | Verdict PASS/FAIL | **PASS** | Overall row in compliance ledger |
| C-06 | Exact schema labels | **PASS** | Headers use Gather/Bind/Execute/Verdict exactly |
| C-07 | Verdict cites criterion IDs | **PASS** | Rows C-01 through C-17 in compliance ledger |
| C-08 | No elision markers | **PASS** | Instruction: "No elision markers anywhere" |
| C-09 | Coverage Matrix | **FAIL** | Not present |
| C-10 | Execute relay carry | **FAIL** | No relay table |
| C-11 | Spec-first Gather | **FAIL** | Single-tier Gather; reads spec + invocation together |
| C-12 | Coverage Matrix BLOCKED gate | **FAIL** | No Coverage Matrix |
| C-13 | Artifact delimiters | **PASS** | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` present |
| C-14 | Phase Label Schema pre-trace | **FAIL** | Not present; no immutable preamble block |
| C-15 | Verdict compliance ledger | **PASS** | Table with ID, Criterion, Result, Evidence; Evidence column has explicit instruction: "must name a specific structural element … not 'looks correct'" |
| C-16 | Bind Status Enum (3-value) declared | **PASS** | Formal enum definition table before resolution table; all three values with Meaning and Execute-effect columns |
| C-17 | Bind conflict precedence rule declared | **PASS** | Named block "Conflict Precedence Rule (declare before resolution rows)" before row 1; invocation-override rule + contract-violation exception |

**Aspirationals passing**: C-13, C-15, C-16, C-17 = **4 / 9**

**Score V-02**: 60 + 30 + (4/9 × 10) = **94.4**

---

### V-03 — Single axis: Role sequence / spec-first Gather + Bind conflict precedence

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Four phases in sequence | **PASS** | Gather / Bind / Execute / Verdict |
| C-02 | Gather enumerates inputs | **PASS** | Two-tier Gather — Tier 1 (spec) + Tier 2 (invocation) tables, each with name + source |
| C-03 | Bind maps all Gather inputs | **PASS** | Resolution table with one row per merged input; Resolved Value column |
| C-04 | Execute produces artifact | **PASS** | Filename template; "No elision markers" instruction |
| C-05 | Verdict PASS/FAIL | **PASS** | Overall row in Verdict table |
| C-06 | Exact schema labels | **PASS** | Prompt uses Gather/Bind/Execute/Verdict headers throughout |
| C-07 | Verdict cites criterion IDs | **PASS** | Verdict table rows ID C-01 through C-17 (selected) with IDs |
| C-08 | No elision markers | **PASS** | Instruction explicit |
| C-09 | Coverage Matrix | **FAIL** | Not present |
| C-10 | Execute relay carry | **FAIL** | No relay table |
| C-11 | Spec-first Gather | **PASS** | "Spec-first rule" instruction; Tier 1 reads spec before consulting invocation; tiers structurally separated |
| C-12 | Coverage Matrix BLOCKED gate | **FAIL** | No Coverage Matrix |
| C-13 | Artifact delimiters | **PASS** | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` in Execute |
| C-14 | Phase Label Schema pre-trace | **FAIL** | No immutable schema preamble block |
| C-15 | Verdict compliance ledger | **PASS** | Verdict has ID \| Result \| Evidence columns; three-column compliance table |
| C-16 | Bind Status Enum (3-value) declared | **FAIL** | No formal Status Enum definition block; table instruction says "Status from declared enum only" but no enum definition block present; three values implicit from sample rows, not explicitly declared |
| C-17 | Bind conflict precedence rule declared | **PASS** | Named block "Conflict Precedence Rule (declared before any resolution row)" before row 1; invocation-override rule + BLOCKED exception both stated |

**Aspirationals passing**: C-11, C-13, C-15, C-17 = **4 / 9**

**Score V-03**: 60 + 30 + (4/9 × 10) = **94.4**

---

### V-04 — Combined: Phase Schema + Status Enum + Conflict Precedence (C-14, C-16, C-17)

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Four phases in sequence | **PASS** | Gather / Bind / Execute / Verdict |
| C-02 | Gather enumerates inputs | **PASS** | Two-tier Gather: Tier 1 (spec) + Tier 2 (invocation); source type column in Tier 1 |
| C-03 | Bind maps all Gather inputs | **PASS** | Resolution table; row count = merged input count; Resolved Value per row |
| C-04 | Execute produces artifact | **PASS** | Filename template; role sequence instruction; no-elision instruction |
| C-05 | Verdict PASS/FAIL | **PASS** | Overall row in compliance ledger |
| C-06 | Exact schema labels | **PASS** | Phase Label Schema preamble locks headers; Verdict C-06 row checks against schema |
| C-07 | Verdict cites criterion IDs | **PASS** | Compliance ledger rows C-01 through C-17 with IDs |
| C-08 | No elision markers | **PASS** | Instruction explicit; artifact must have no elision markers |
| C-09 | Coverage Matrix | **FAIL** | Not present |
| C-10 | Execute relay carry | **FAIL** | No relay table |
| C-11 | Spec-first Gather | **PASS** | "Spec-first rule" instruction; Tier 1 / Tier 2 split structurally enforced |
| C-12 | Coverage Matrix BLOCKED gate | **FAIL** | No Coverage Matrix |
| C-13 | Artifact delimiters | **PASS** | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` in Execute; Verdict C-13 row checks this |
| C-14 | Phase Label Schema pre-trace | **PASS** | "Phase Label Schema (IMMUTABLE — declared before trace begins)" block before Gather; Verdict C-14 row checks this |
| C-15 | Verdict compliance ledger | **PASS** | Full ID \| Criterion \| Result \| Evidence table; Evidence column instruction: "must name a specific structural element"; C-15 row self-checks this |
| C-16 | Bind Status Enum (3-value) declared | **PASS** | Formal Status Enum table before resolution table; RESOLVED / UNRESOLVED / BLOCKED with Meaning + Execute-effect columns; Verdict C-16 row checks presence |
| C-17 | Bind conflict precedence rule declared | **PASS** | "Conflict Precedence Rule (declared before resolution rows)" named block before row 1; invocation-override + BLOCKED exception; Verdict C-17 row checks presence |

**Aspirationals passing**: C-11, C-13, C-14, C-15, C-16, C-17 = **6 / 9**

**Score V-04**: 60 + 30 + (6/9 × 10) = **96.7**

---

### V-05 — Full golden: all aspirationals C-09 through C-17

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Four phases in sequence | **PASS** | Gather / Bind / Execute / Verdict; each structurally scoped |
| C-02 | Gather enumerates inputs | **PASS** | Tier 1 (spec) + Tier 2 (invocation) tables; source type in Tier 1; Supplied? in Tier 2 |
| C-03 | Bind maps all Gather inputs | **PASS** | Resolution table; merged input count; Resolved Value column; Status from declared enum |
| C-04 | Execute produces artifact | **PASS** | Relay table confirms roles; artifact filename; delimiters; no-elision instruction |
| C-05 | Verdict PASS/FAIL | **PASS** | Overall row in compliance ledger |
| C-06 | Exact schema labels | **PASS** | Phase Label Schema preamble at top; all four canonical headers declared; Verdict C-06 row checks schema |
| C-07 | Verdict cites criterion IDs | **PASS** | All C-01 through C-17 as rows in compliance ledger |
| C-08 | No elision markers | **PASS** | Execute: "no '...', no '[content here]', no omissions" instruction; B-NN marker used for gaps |
| C-09 | Coverage Matrix with closed-world preamble | **PASS** | "Coverage Matrix (closed-world authority — declared before Gather runs)" block; closed-world preamble text explicit; Verdict C-09 row checks block presence + preamble text |
| C-10 | Execute relay carry; Verdict reads relay | **PASS** | Relay table in Execute with role / signal / binding / status columns; Verdict opens with "Read the Execute relay table. Do not reconstruct evidence from the artifact body"; Verdict C-10 row cites relay status |
| C-11 | Spec-first Gather | **PASS** | "Spec-first rule (C-11)" instruction explicit; Tier 1 reads spec before invocation; Verdict C-11 row checks tier ordering |
| C-12 | Coverage Matrix BLOCKED gate | **PASS** | "Coverage Matrix BLOCKED gate" block; Gap=YES → BLOCKED halt before Gather; named unblock condition; Verdict C-12 row checks gate block presence |
| C-13 | Artifact delimiters | **PASS** | `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` in Execute; Verdict C-13 row names delimiter strings |
| C-14 | Phase Label Schema pre-trace | **PASS** | "Phase Label Schema (IMMUTABLE — pre-trace preamble)" block before Coverage Matrix; first block in document; Verdict C-14 row checks "before Coverage Matrix" position |
| C-15 | Verdict compliance ledger | **PASS** | Full ID \| Criterion \| Result \| Evidence table; "Generic entries fail C-15 structurally" instruction; Evidence column cites relay rows, table headers, row counts, delimiter strings, section headings; C-15 row self-checks |
| C-16 | Bind Status Enum (3-value) declared | **PASS** | Formal Status Enum table before resolution table; RESOLVED / UNRESOLVED / BLOCKED with Meaning + Execute-effect columns; Verdict C-16 row names definition table above resolution table |
| C-17 | Bind conflict precedence rule declared | **PASS** | Named block before resolution row 1; invocation-override rule + BLOCKED exception; per-conflict-row citation instruction ("invocation override applied" / "spec default retained"); Verdict C-17 row checks block + exception |

**Aspirationals passing**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17 = **9 / 9**

**Score V-05**: 60 + 30 + (9/9 × 10) = **100**

---

### Rankings

| Rank | Variation | Essential | Recommended | Aspirationals | Score |
|------|-----------|-----------|-------------|---------------|-------|
| 1 | V-05 Full golden | 5/5 | 3/3 | 9/9 | **100** |
| 2 | V-04 Schema + Enum + Precedence | 5/5 | 3/3 | 6/9 | **96.7** |
| 3 | V-01 Phase Label Schema | 5/5 | 3/3 | 4/9 | **94.4** |
| 3 | V-02 Compliance ledger + Status Enum | 5/5 | 3/3 | 4/9 | **94.4** |
| 3 | V-03 Spec-first + Conflict rule | 5/5 | 3/3 | 4/9 | **94.4** |

All variations clear the golden threshold (all essential PASS + composite ≥ 80).

---

### Excellence Signals — V-05

**What V-05 achieves that V-04 does not** (the 3-point gap):

1. **Coverage Matrix as pre-Gather completeness gate (C-09 + C-12)** — V-05 adds a second blocking gate before Gather runs. The Phase Label Schema declares the header vocabulary; the Coverage Matrix declares the input vocabulary. The two declarations together bracket the entire trace: what phases exist (locked at top) and what inputs exist (locked before phase 1). V-04 has no Coverage Matrix, so its Gather can silently omit inputs that the spec requires but the invocation doesn't explicitly supply.

2. **Relay carry as secondary evidence chain (C-10)** — V-05's relay table in Execute gives the Verdict a structural evidence source that is independent of the artifact body. The Verdict instruction "do not reconstruct evidence from the artifact body" makes this explicit: the relay is the primary source, the artifact body is the output. This separates evidence (relay) from product (artifact). V-04's Verdict must read the artifact body to check C-04, introducing reconstruction risk.

3. **"Declare before you use" as full structural cascade** — V-05 establishes a consistent rhythm across all four phases: Phase Label Schema (before everything) → Coverage Matrix gate (before Gather) → spec-first Tier 1 (before Tier 2) → Status Enum + Conflict Rule (before Bind rows) → relay table (before artifact) → compliance ledger (checks all prior phases). V-04 achieves three of the five declarations but skips the Coverage Matrix and relay layers, leaving two structural gaps. The cascade is compositional: each layer's declaration makes the next layer's evidence auditable.

**Distinguishing detail in V-05's Verdict instruction**: The explicit non-reconstruction directive ("Read the Execute relay table. Do not reconstruct evidence from the artifact body. The relay table is the primary evidence source for all criterion checks involving Execute content.") is an implementation refinement of C-10 that makes the relay-to-Verdict interface a first-class structural protocol. This is already captured by C-10's "Verdict reads, not reconstructs" criterion text — no new criterion needed.

---

### New Patterns Assessment

All patterns from V-05 are captured by existing rubric v3 criteria (C-09 through C-17). The V-05 structural cascade is a composition of the four pre-content declaration patterns (C-14, C-09/C-12, C-11, C-16/C-17) in sequence — this is the integration property hypothesized in V-05's axis description. No genuinely new structural patterns emerge that are not already named by a criterion.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
