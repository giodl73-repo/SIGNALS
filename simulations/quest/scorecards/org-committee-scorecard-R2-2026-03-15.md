# org:committee — Round 2 Scoring (V-01 through V-03)

---

## V-01 — Challenger-First Ordering

### Essential Criteria (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Step 1 explicitly declares committee type "in the first line of output" |
| C-02 | **PASS** | Step 2 reads `.craft/roles/` with explicit fallback disclosure |
| C-03 | **PASS** | Step 4: "Reflect the documented orientation of that role (not generic management speak)" |
| C-04 | **PASS** | Step 5 requires DECISIONS, ACTION ITEMS, DISSENTING OPINIONS — all three named |
| C-05 | **PASS** | "At least one Tier 1 speaker must raise a challenge, condition, or block" — enforced |

**Essential: 5/5 → 60 pts**

### Recommended Criteria (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | Simulation references the specific "agenda item" throughout; speakers must respond to prior concerns, not generic positions |
| C-07 | **PASS** | Format `[Owner Role] — [specific action] — [deadline]` + explicit failure example ("investigate further" fails) |
| C-08 | **PARTIAL** | DISSENTING OPINIONS section required, but no resolution path language — dissent captured, path not required |

**Recommended: 2.5/3 → 25 pts**

### Aspirational Criteria (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **PARTIAL** | Challenger-first ordering increases surprise probability but no explicit mechanism or self-check targeting C-09 |
| C-10 | **PASS** | "If the outcome is non-approval, state the re-entry condition explicitly" |
| C-11 | **PASS** | This is the axis. Three-tier sort (CHALLENGERS → CONDITIONALS → ADVOCATES) with explicit ambiguity tie-break rule |
| C-12 | **FAIL** | No pre-simulation investigation of switching costs; inertia resistance not grounded in specific dependencies |
| C-13 | **PARTIAL** | "Either challenge, conditionally approve, or approve" but no stance-before-prose structural requirement; stance may emerge from prose |

**Aspirational: (0.5+1+1+0+0.5)/5 × 10 = 6 pts**

**V-01 Composite: 60 + 25 + 6 = 91**

---

## V-02 — Switching-Cost Investigation Precedes Simulation

### Essential Criteria (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Step 1 declares committee type in first line |
| C-02 | **PASS** | Step 2 reads `.craft/roles/` with fallback disclosure |
| C-03 | **PASS** | Step 4: "Reflect the documented orientation of that role" |
| C-04 | **PASS** | Step 5 requires DECISIONS, ACTION ITEMS, DISSENTING OPINIONS |
| C-05 | **PASS** | "At least one participant must raise a challenge, block, or approval condition" |

**Essential: 5/5 → 60 pts**

### Recommended Criteria (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | Step 3 investigates the specific agenda item; speaker voices reference it throughout |
| C-07 | **PASS** | "Format: [Owner Role] — [specific action] — [deadline]" + "All items must be owned and specific" |
| C-08 | **PARTIAL** | DISSENTING OPINIONS section present; no explicit resolution path requirement |

**Recommended: 2.5/3 → 25 pts**

### Aspirational Criteria (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **PASS** | Step 3 item (d) explicitly requires "at least one cost that is non-obvious — something unlikely to be in the original proposal"; self-check asks C-09 by name and mandates revision if absent |
| C-10 | **PASS** | "Re-entry condition if not approved" in DECISIONS format |
| C-11 | **PARTIAL** | "Charter order" not challenger-first; no tier sorting |
| C-12 | **PASS** | This is the axis. Step 3 is the full investigation with labeled items (a)-(d) before any participant voice |
| C-13 | **PARTIAL** | Voices must "challenge, conditionally approve, or approve" but no `STANCE:` label before prose |

**Aspirational: (1+1+0.5+1+0.5)/5 × 10 = 8 pts**

**V-02 Composite: 60 + 25 + 8 = 93**

---

## V-03 — Stance-Declared-First Structure

> **Note — truncation**: V-03 ends mid-Step 4 ("After all voices, output a one-line tally:"). Step 5 with DECISIONS / ACTION ITEMS / DISSENTING OPINIONS is absent from the prompt as provided. Scored strictly on visible text; C-04 fails.

### Essential Criteria (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Step 1 declares committee type at top of output |
| C-02 | **PASS** | Step 2 reads `.craft/roles/` with fallback disclosure |
| C-03 | **PASS** | Step 3: "Rationale — 2-5 sentences from this role's documented orientation" |
| C-04 | **FAIL** | Three required sections (DECISIONS, ACTION ITEMS, DISSENTING OPINIONS) absent — Step 4 produces only a tally |
| C-05 | **PASS** | "At least one speaker must declare CONDITION or BLOCK... A minutes document where every speaker declares APPROVE on first pass is not a useful simulation" |

**Essential: 4/5 → 48 pts**

### Recommended Criteria (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PARTIAL** | Agenda implied but no explicit agenda-specificity mechanism |
| C-07 | **FAIL** | No ACTION ITEMS section in visible prompt |
| C-08 | **FAIL** | No DISSENTING OPINIONS section in visible prompt |

**Recommended: 0.5/3 → 5 pts**

### Aspirational Criteria (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **PARTIAL** | Structured dissent from CONDITION/BLOCK declarations may surface surprises, but no explicit mechanism |
| C-10 | **FAIL** | No DECISIONS section; no re-entry path structure |
| C-11 | **PARTIAL** | No tier sort; charter order only |
| C-12 | **FAIL** | No investigation phase |
| C-13 | **PASS** | This is the axis. `STANCE: [APPROVE | CONDITION | BLOCK]` line precedes all prose; explicit anti-pattern rules for trailing hedges and contradiction; invalidation logic stated |

**Aspirational: (0.5+0+0.5+0+1)/5 × 10 = 4 pts**

**V-03 Composite: 48 + 5 + 4 = 57**

---

## Summary Ranking

| Rank | Variation | Essential | Recommended | Aspirational | **Total** |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 | V-02 Switching-Cost Investigation | 60 | 25 | 8 | **93** |
| 2 | V-01 Challenger-First Ordering | 60 | 25 | 6 | **91** |
| 3 | V-03 Stance-Declared-First | 48 | 5 | 4 | **57** |

---

## Excellence Signals — V-02

**What made V-02 the top scorer:**

1. **Pre-simulation phase separates environmental gathering from voice generation** — the investigation runs in its own named step before any participant speaks. This prevents inertia arguments from being invented on the fly and grounds them in specific labeled findings (a)-(d).

2. **Labeled findings enable cross-speaker citation** — items tagged with labels like "dependency W-2" allow later speakers to reference specific concerns traceable to the investigation, creating an intertextual chain that makes the simulation readable as a real record.

3. **Self-check closes the C-09 loop explicitly** — the internal self-check names C-09 directly and requires revision of the investigation (not just the voices) if no surprise is surfaced. This is a quality chain: investigation quality → voice quality → output surprise quality.

4. **Approving voices required to acknowledge switching costs** — even supporters must engage with the pre-identified costs ("Approving participants must acknowledge the switching costs even if they argue the benefits outweigh them"). This prevents one-sided approval without awareness of consequences.

---

```json
{"top_score": 93, "all_essential_pass": false, "new_patterns": ["pre-simulation investigation phase separates environmental context from participant voices, grounding inertia arguments in specific labeled dependencies", "cross-speaker citation via labeled investigation findings creates intertextual accountability chain", "self-check that explicitly names C-09 and requires investigation revision (not just voice revision) creates a quality chain from investigation depth to output surprise quality"]}
```
