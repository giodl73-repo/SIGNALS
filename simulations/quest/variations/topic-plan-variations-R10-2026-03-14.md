Written to `simulations/quest/rubrics/topic-plan-rubric-v9-R9-variate-R10-2026-03-15.md`.

---

## Round 10 Variations — topic-plan (v9 rubric)

**New criteria targeted**: C-34 (universal closed-enum at both declaration sites) and C-35 (assumption table columns independently populated)

### Variation Design

| Variation | Axis | Type | Primary target |
|-----------|------|------|----------------|
| **V-01** | Output format | Single | C-34 |
| **V-02** | Lifecycle emphasis | Single | C-35 |
| **V-03** | Phrasing register | Single | C-34 + C-35 |
| **V-04** | Output format + Lifecycle | Combination | C-34 + C-35 |
| **V-05** | Full stack | Combination | C-34 + C-35 + all R9 ceiling |

---

### What each variation does

**V-01 — Universal Closed-Enum at Both Declaration Sites**

Extends the R9 V-01 enum-lock mechanism from Reversibility to *all four enumerated columns*: `Delta candidate?` (yes/no), `Consistent with strategy?` (Yes/No/Partial), `Type` (ADD/REMOVE/REPRIORITIZE), and `Reversibility` (three values). Each carries `[select: X / Y / Z; prose not a valid value]` in both the upfront schema header AND in the Step 6 commitment statement. The hypothesis: R9 left `Consistent with strategy?` and `Delta candidate?` as open-fill columns despite being enumerations — models can write "Mostly yes" or "probably" and appear compliant. V-01 closes this by making every enumerated column structurally restrictive at both declaration sites. **Intentionally omits C-35 mechanism.**

**V-02 — Implicit Evidence Column Independence Rule**

Adds an explicit anti-pattern disqualification to the "Implicit evidence" column at both the upfront schema annotation and the extraction step. Three named fail patterns: (a) row key/ID, (b) restatement of the assumption, (c) pointer ("see rationale"). One named pass pattern: quoted or paraphrased strategy.md text that a reader could trace to a specific location. The hypothesis: R9 V-02 said "cite the strategy.md phrase" but never named what a non-citation looks like. A model filling `A-01` into the cell satisfies the letter of "cite a phrase" while violating the intent. The named anti-patterns make the disqualification condition confrontable at fill time. **Intentionally omits C-34 universal-enum mechanism.**

**V-03 — Pre-Schema COLUMN CONTRACT with Decision-Question Independence Test**

Inserts a `### COLUMN CONTRACT` block *before* the output schema, declaring two structural rules that govern all tables:

- **Rule 1**: Every enumerated column carries its closed value set at every declaration site; prose not valid
- **Rule 2**: Before filling any cell, apply the independence test — *"Can this cell be filled correctly without reading the source document?"* — if yes, it is a structural alias and is treated as absent

The conversational decision-question format generalizes both C-34 and C-35 into a single pre-reading commitment without requiring per-column enumeration. The phrasing register change is the discriminator: the CONTRACT framing uses imperative rules + a decision-question test rather than in-header annotations. V-03 also uses role sequence (Archaeologist + named phase lifecycle), testing whether the CONTRACT framing interacts with role-switching.

**V-04 — Universal Enum Lock + Implicit Evidence Independence Rule (Combination)**

Layers V-01 mechanism (universal closed-enum in upfront schema + commitment checkpoints) with V-02 mechanism (Implicit evidence independence rule with fail/pass examples at extraction), using R9 V-04 as the base (schema-first + role sequence). C-34 and C-35 operate at different structural levels — declaration vs. population — and should compose without interference. V-04 tests this assumption by combining both without the COLUMN CONTRACT wrapper.

**V-05 — Full Stack (R9 V-05 + Universal Enum Lock + Column Independence Contract + Extraction Anti-Patterns)**

Takes the R9 V-05 ceiling and adds all three R10 mechanisms:
1. COLUMN CONTRACT (V-03) with Rule 1 + Rule 2 and explicit fail/pass examples
2. All four enumerated columns carry closed enums in the upfront schema, all reproduced at the Step 6 commitment checkpoint
3. "Implicit evidence" column annotation in the upfront schema includes three fail cases + one pass case + the traceability test formulation

The commitment statement at Step 6 now names both Type and Reversibility with their full valid-value selectors, reproducing the upfront schema annotation precisely — making the "both sites" requirement structurally verifiable.

---

### Coverage Matrix — new criteria only

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **C-34** | PASS: all 4 enums at upfront schema + Step 6 commitment | FAIL: only Reversibility has closed enum | PASS: Rule 1 CONTRACT + all 4 enums in upfront schema + commitments | PASS: all 4 enums in upfront schema + Step 6 commitment | PASS: CONTRACT Rule 1 + all 4 enums + Step 6 commitment reproduces all |
| **C-35** | FAIL: no independence rule; Implicit evidence not guarded against aliasing | PASS: 3 fail examples + 1 pass example at both upfront schema and extraction step | PASS: CONTRACT Rule 2 + decision-question test + fail/pass distinction in schema | PASS: upfront schema annotation + 3 fail patterns + 1 pass pattern at Step 1b | PASS: CONTRACT Rule 2 + upfront fail/pass examples + Step 1b archaeology obligation with traceability test |

### Key design choices vs. R9

- **V-01 discriminator**: R9 V-02 failed C-32 because it named the Reversibility column without its enum — V-01 asks whether that same gap exists for `Consistent with strategy?` and `Delta candidate?` across all variations
- **V-02 discriminator**: R9 V-01 failed C-35 because the five-column schema used a row key as one of the five — V-02 names this pattern explicitly so the model confronts it before filling
- **V-03 discriminator**: whether a single pre-reading contract that generalizes both rules changes behavior more than per-column annotations added incrementally
- **V-04 discriminator**: whether the two mechanisms compose cleanly when both applied in a single variation without the CONTRACT wrapper
- **V-05 discriminator**: whether the additional precision constraints change behavior in models that were already partially passing C-32 and C-33
