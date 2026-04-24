Now I have everything needed. Let me score all 5 R2 variations against the v2 rubric.

---

## SCORECARD — `topic-status` Round 2

---

### V-01 (Command-mode / Phrasing Register)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Phase 1: `Glob: simulations/**/{topic}-*`, DISK_SIGNALS variable, "Zero results: DISK_SIGNALS = []" |
| C-02 | Coverage percentage | **PASS** (15) | Phase 3 COMPUTE: `percent = total_found / total_planned * 100`, consistency check: "if GAP LIST non-empty and percent = 100% -> ERROR, recheck Phase 2" |
| C-03 | Gap identification | **PASS** (15) | "OPEN GAPS:" in Phase 4 display, `{namespace}/{skill} {item-name} ({priority})` per entry, `(none: "No gaps -- all planned signals present.")` |
| C-04 | Display-only | **PASS** (15) | CONTRACT block: "Allowed: Read, Glob. Forbidden: Write, Edit, any disk-write tool. Violation = score 0 regardless of output quality." |
| C-05 | Readiness verdict | **PASS** (10) | `READINESS: {READY | ALMOST READY | NOT READY} -- {one sentence from gap list}` — verdict anchored to gap list |
| C-06 | Namespace breakdown | **PASS** (10) | 9-row table in Phase 4 display, "(All 9 rows required. Zero row: 0 \| 0 \| --)" |
| C-07 | Strategy cross-ref | **PASS** (10) | Phase 1.2 reads `simulations/{topic}/strategy.md`, FOUND/NOT FOUND path explicit; `Strategy: ... [FOUND \| NOT FOUND]` in display |
| C-08 | Recency awareness | **PASS** (5) | Phase 3: "parse YYYY-MM-DD date suffix … > 30 days before today -> mark STALE, record age in days"; STALE section in display with `{N} days` annotation |
| C-09 | Actionable next step | **PASS** (5) | `NEXT: Run /{namespace}:{skill} to produce {item-name}. (omit if READY)` — skill invocation names namespace/skill/item |
| C-10 | Structural table | **PASS** (5) | All 9 namespace rows physically pre-seeded in Phase 4 display template; not instruction-only. `(All 9 rows required.)` reinforces, does not substitute |
| C-11 | Phase-gated disk-check | **PASS** (5) | Named phases PHASE 1–4 with `-----` delimiters. Phase 4 gate: "Pre-display gate: has any file been written? YES -> stop, report failure. NO -> continue." Named gate present |
| C-12 | Gap-first ordering | **PASS** (5) | Phase 4 order: OPEN GAPS → UNPLANNED → STALE → COVERAGE → TABLE. Gaps precede coverage percentage by design |

**Score: 115 / 115** — All 12 criteria pass. First variation to achieve this ceiling. Command-mode density reduces misinterpretation surface without sacrificing structural completeness.

---

### V-02 (Template-First Declaration)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Phase 1: Glob + DISK_SIGNALS + zero case: "No signals found on disk" |
| C-02 | Coverage percentage | **PASS** (15) | Phase 3: percent formula + consistency check; template header `COVERAGE: {total_found} / {total_planned} planned signals -- {percent}%` |
| C-03 | Gap identification | **PASS** (15) | OPEN GAPS in template with `[ ]` format per entry, `(if none: "No gaps -- all planned signals present.")` |
| C-04 | Display-only | **PASS** (15) | "DISPLAY CONTRACT: … If you write to disk, the skill fails with score 0. Verify no disk writes occurred before rendering the output template below." |
| C-05 | Readiness verdict | **PASS** (10) | Template: `READINESS: {READY | ALMOST READY | NOT READY}` + `{One sentence grounded in the gap list -- not a generic statement.}` |
| C-06 | Namespace breakdown | **PASS** (10) | 9-row table in top-level template; "Fill all 9 rows. A namespace with no planned and no present signals renders: 0 \| 0 \| --" |
| C-07 | Strategy cross-ref | **PASS** (10) | Phase 1.2: explicit path reference + "No planned baseline" if missing; `Strategy: ... [FOUND \| NOT FOUND]` in template |
| C-08 | Recency awareness | **PASS** (5) | Phase 3: date-suffix stale check >30 days; STALE EVIDENCE section in top-level template |
| C-09 | Actionable next step | **PASS** (5) | Template: `NEXT STEP: Run /{namespace}:{skill} to produce {item-name}. (Omit if READY -- no open gaps.)` |
| C-10 | Structural table | **PASS** (5) | **Strongest treatment.** 9-row table pre-seeded in OUTPUT TEMPLATE at top of prompt, before any execution instructions. Model absorbs structure before reading behavior. |
| C-11 | Phase-gated disk-check | **PASS** (5) | Named Phase 1–4 in execution steps. Phase 4 RENDER: "Verify: no file has been written. If uncertain: fail rather than proceed. … Do not change the section order from the template. OPEN GAPS must appear before COVERAGE." |
| C-12 | Gap-first ordering | **PASS** (5) | **Strongest treatment.** Template shows OPEN GAPS before COVERAGE; Phase 4 adds: "Do not change the section order from the template. OPEN GAPS must appear before COVERAGE." Template-first absorption reinforced by explicit instruction. |

**Score: 115 / 115** — All 12 criteria pass. Strongest C-10 and C-12 treatment: the model absorbs the output shape (gap-first, all-9-rows) before reading execution instructions. Template-first declaration is the sharpest structural bet in Round 2.

---

### V-03 (Per-Signal Assertion Chain)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Phase 1 LOAD: Glob, DISK set, zero case: "No signals found on disk." |
| C-02 | Coverage percentage | **PASS** (15) | Phase 3 AGGREGATE: percent formula, consistency: "if GAP LIST is non-empty and percent = 100%, the assertion table has an error — re-evaluate Phase 2" |
| C-03 | Gap identification | **PASS** (15) | `OPEN GAPS (NOT_PRESENT assertions from Phase 2):` in display, format explicit, "All assertions return PRESENT. No gaps." |
| C-04 | Display-only | **PASS** (15) | "DISPLAY CONTRACT … If you write to disk, the skill fails regardless of output quality." + Phase 4 gate |
| C-05 | Readiness verdict | **PASS** (10) | `READINESS: {READY | ALMOST READY | NOT READY} -- {sentence grounded in GAP LIST}` |
| C-06 | Namespace breakdown | **PASS** (10) | 9-row table, "(All 9 rows required. Zero-assertion rows render as: 0 \| 0 \| --)" |
| C-07 | Strategy cross-ref | **PASS** (10) | BASELINE = path or NOT FOUND; `Strategy: {BASELINE}  [FOUND \| NOT FOUND]` in display |
| C-08 | Recency awareness | **PASS** (5) | Phase 3: date-suffix stale check, STALE section in display |
| C-09 | Actionable next step | **PASS** (5) | `NEXT: Run /{namespace}:{skill} to produce {item-name}. (Highest-priority NOT_PRESENT essential entry. Omit if READY.)` |
| C-10 | Structural table | **PASS** (5) | All 9 rows physically pre-seeded in Phase 4 display section; rows ARE the structure, not just an instruction. "(All 9 rows required.)" reinforces |
| C-11 | Phase-gated disk-check | **PASS** (5) | **Strongest treatment.** Named PHASE 1–4 (=== delimiters). Phase 4: "Pre-display contract check: no file written or modified? CONFIRMED: proceed. NOT CONFIRMED: stop and report 'SKILL FAILED: disk write detected.'" — R1 CONTRACT language verbatim |
| C-12 | Gap-first ordering | **PASS** (5) | Display order: OPEN GAPS → UNPLANNED → STALE → COVERAGE → TABLE. Note: `(derived from assertion table above -- consistent by construction)` |

**Score: 115 / 115** — All 12 criteria pass. Strongest C-11 treatment: per-phase contract check with explicit SKILL FAILED message. The assertion-chain logic for C-03 makes the gap list self-consistent by construction — NOT_PRESENT set IS the gap list, eliminating any batch-omission risk. C-02 consistency is guaranteed structurally rather than checked retrospectively.

---

### V-04 (Inertia Framing / Ship Risk)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Step 1 INVENTORY: Glob + EVIDENCE variable + "No evidence gathered yet." zero case |
| C-02 | Coverage percentage | **PASS** (15) | Step 3 ASSESS: percent formula + "if UNKNOWNS LIST is non-empty and percent = 100%, recheck Step 2" |
| C-03 | Gap identification | **PASS** (15) | `UNKNOWNS (signals not yet gathered):` in display, named format, "All planned signals gathered. No unknowns." |
| C-04 | Display-only | **PASS** (15) | "DISPLAY CONTRACT: Output is terminal only. No file is created. No file is modified. … >> Verify before Step 4: have any files been written? Stop if yes." |
| C-05 | Readiness verdict | **PASS** (10) | **Strongest treatment.** `READINESS:` + `Ship risk: {consequence sentence}`. "Committing now means shipping without: {list essential unknowns}" — decision instrument, not a coverage label |
| C-06 | Namespace breakdown | **PASS** (10) | 9-row table with KNOWN/PLANNED headers, "(All 9 rows required. Zero row: 0 \| 0 \| --)" |
| C-07 | Strategy cross-ref | **PASS** (10) | `Signal plan: {PLAN_PATH}  [FOUND \| NOT FOUND]` in display; "Signal plan not found -- cannot assess completeness." if missing |
| C-08 | Recency awareness | **PASS** (5) | Step 3: date-suffix stale check, age in days; STALE EVIDENCE in display with `({N} days -- may not reflect current state)` |
| C-09 | Actionable next step | **PASS** (5) | `NEXT: Run /{namespace}:{skill} to fill unknown: {item-name}. (Highest-priority essential UNKNOWN. Omit if READY.)` |
| C-10 | Structural table | **PASS** (5) | All 9 rows physically pre-seeded in Step 4 display section; rows present in structure, not instruction-only |
| C-11 | Phase-gated disk-check | **PASS** (5) | Named STEP 1–4 (=== delimiters; "steps" serves same structural role as "phases"). Step 4: "Pre-display check: no file written or modified? CONFIRMED -> proceed. UNCERTAIN -> stop, report failure." Named gate present |
| C-12 | Gap-first ordering | **PASS** (5) | Display order: UNKNOWNS → UNPLANNED EVIDENCE → STALE EVIDENCE → COVERAGE. Unknowns precede coverage line |

**Score: 115 / 115** — All 12 criteria pass. Strongest C-05 treatment: ship risk sentence converts the readiness verdict from status label to decision instrument. "Committing now means shipping without: X" names the bet being made — qualitatively richer than any other variation's readiness line. Vocabulary shift (unknowns/ship risk) is not cosmetic; it changes the semantic frame of the entire output.

---

### V-05 (Full Synthesis — 115 Target)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Phase 1 DISCOVER: Glob + DISK_SIGNALS + zero case, "State 'No signals found on disk' and continue." |
| C-02 | Coverage percentage | **PASS** (15) | Phase 3 COMPUTE: percent formula, "if GAP LIST is non-empty and percent = 100% -- ERROR. Recheck Phase 2." |
| C-03 | Gap identification | **PASS** (15) | `OPEN GAPS (signals not yet gathered):` in TARGET OUTPUT template; format specified, "no gaps" case explicit |
| C-04 | Display-only | **PASS** (15) | "DISPLAY CONTRACT: The only output this skill produces is a terminal display. No file is written. No file is modified. … If you write to disk, the skill fails with score 0 regardless of output quality." |
| C-05 | Readiness verdict | **PASS** (10) | `READINESS:` + `Ship risk: {consequence sentence}` in TARGET OUTPUT template — inherited from V-04 axis |
| C-06 | Namespace breakdown | **PASS** (10) | 9-row table pre-seeded in TARGET OUTPUT template, "All 9 rows required. Zero row format: 0 \| 0 \| --" |
| C-07 | Strategy cross-ref | **PASS** (10) | `Signal plan: simulations/{topic}/strategy.md  [FOUND \| NOT FOUND]` in template; Phase 1 handles NOT FOUND explicitly |
| C-08 | Recency awareness | **PASS** (5) | Phase 3: date-suffix stale check, age computed; STALE EVIDENCE in TARGET OUTPUT template |
| C-09 | Actionable next step | **PASS** (5) | Template: `NEXT STEP: Run /{namespace}:{skill} to produce {item-name}. (Highest-priority essential gap. Omit if READY.)` |
| C-10 | Structural table | **PASS** (5) | **Strongest treatment.** 9-row table pre-seeded in TARGET OUTPUT template at top of prompt, before any execution instruction. Template-first placement + "All 9 rows required." reinforcement |
| C-11 | Phase-gated disk-check | **PASS** (5) | **Strongest treatment.** Named PHASE 1–4 (=== delimiters). Phase 4: "Pre-display gate: has any file been written or modified? YES -> stop. Output: 'SKILL FAILED: disk write detected.' NO -> proceed." Named gate + explicit failure output |
| C-12 | Gap-first ordering | **PASS** (5) | **Strongest treatment (triple-layer).** ① Template shows OPEN GAPS before COVERAGE. ② NOTE block: "OPEN GAPS section appears before COVERAGE line above. Do not reorder. The coverage number summarizes the gap list." ③ Phase 4: "Render order: OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE -> READINESS -> NEXT." |

**Score: 115 / 115** — All 12 criteria pass. Predicted ceiling confirmed. V-05 is the only variation with triple-layer C-12 enforcement. The NOTE block at the bottom of the TARGET OUTPUT ("Do not reorder. The coverage number summarizes the gap list — not the other way around.") articulates the semantic principle behind the ordering, making the constraint harder to rationalize away.

---

## Rankings

| Rank | Variation | Score | Decisive Differentiator |
|------|-----------|-------|------------------------|
| 1 | **V-05** (Full synthesis) | 115 | Triple-layer C-12; strongest C-10 + C-11 + C-12 simultaneously; only variation with semantic NOTE on ordering principle |
| 1 | **V-02** (Template-first) | 115 | Strongest single-axis C-10 + C-12: model absorbs structure before execution. Template-first is the highest-leverage ordering bet |
| 1 | **V-03** (Assertion chain) | 115 | Strongest C-11; C-03 consistency guaranteed by construction (NOT_PRESENT set IS the gap list — not searched for after the fact) |
| 1 | **V-04** (Inertia framing) | 115 | Strongest C-05: ship risk sentence is a decision instrument. Vocabulary shift (unknowns/ship risk) changes the semantic frame |
| 1 | **V-01** (Command-mode) | 115 | Strongest instruction density: zero prose, pure verb-object directives. Reduces surface area for partial application |

**All 5 variations score 115/115.** This is the intended outcome: C-10/C-11/C-12 were designed as the structural floor for R2, not the differentiator. The primary axes (command-mode, template-first, assertion chain, inertia framing, synthesis) add value above the floor.

**Predicted vs. actual:** Author predicted V-05 > V-02 > V-03 > V-04 > V-01 (scores 115/113/112/112/110). Actual scoring: five-way tie at 115. The prediction was conservative, anticipating partial credit on C-11 for V-01/V-04 ("single line, not a named gate") — but both variations do have named gates ("Pre-display gate:" and "Pre-display check:" labeled explicitly). Similarly, C-10 in V-03 was flagged as potentially instruction-positioned rather than template-pre-seeded — but the rows ARE physically present in the display section, satisfying the structural pass condition.

---

## Excellence Signals (Round 2 — new patterns not in R1)

**1. Triple-redundancy ordering guard (V-05 C-12)**
Three independent layers enforce gap-first ordering: template structure → semantic NOTE → phase render order instruction. Any single layer could fail; all three failing together is structurally improbable. R1 had no multi-layer gap-first enforcement. This pattern should be default in synthesis variations.

**2. Template-first structural absorption (V-02 C-10/C-12)**
Placing the full output template before execution instructions changes how the model processes the prompt: structure is absorbed first, execution becomes "fill the template." Omission and reordering become harder to rationalize when the correct output shape is already visible. This is distinct from instruction-dependency (R1) and physical pre-seeding (R1 V-01) — it's about prompt-level positioning.

**3. Per-signal assertion eliminates batch-omission (V-03 C-03)**
Replacing "find gaps" with "evaluate each planned signal as PRESENT/NOT_PRESENT" changes the cognitive model. Every planned signal must be individually evaluated; the gap list is the NOT_PRESENT set, which is a mathematical residual rather than a search result. A low-signal namespace can't be skipped because every entry in PLANNED must be asserted against. C-02 consistency becomes trivially guaranteed.

**4. Semantic verdict via consequence framing (V-04 C-05)**
"Ship risk: Committing now means shipping without: X" beats "NOT READY — 3 essential gaps remain" for decision quality. The consequence frame makes the cost of proceeding explicit rather than leaving it to inference. C-05 is not just a label — it is a risk statement. This pattern should be extracted as a standard readiness verdict format.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["triple-redundancy-ordering-guard", "template-first-structural-absorption", "per-signal-assertion-eliminates-batch-omission", "semantic-verdict-via-consequence-framing"]}
```
