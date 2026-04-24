Written to `simulations/quest/rubrics/program-plan-rubric-v1-2026-03-15.md`.

---

**Structure:**

- **4 essential** (60%): YAML validity, echo final-stage contract, valid Signal skill names only, evidence-state gates (not execution-state)
- **3 recommended** (30%): namespace dependency order, descriptive stage names, plan-not-executor identity
- **2 aspirational** (10%): at least one quantified gate, deliberate evidence arc

**Design decisions:**

- C-01/C-02/C-03/C-04 are essential because a plan failing any of them is structurally unusable — bad YAML can't be consumed, missing echo violates the plugin contract, invented skills reference nothing real, and execution-state gates destroy the only value the plan provides
- C-05 is recommended (not essential) because namespace ordering is about quality of evidence sequencing — a plan with scout/draft/review in correct order but flow/trace slightly misplaced is still useful
- C-06/C-07 are recommended because descriptive names and explicit plan identity improve readability but don't break the plan's core function
- Failure fast-paths explicitly cover the four most common failure modes from the variate scoring rounds: no YAML, bad echo, invented skills, all-execution gates
