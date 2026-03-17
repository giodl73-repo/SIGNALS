# signal — Navigation, Setup, and Layout

## The short version

The signal namespace is Signal's meta-layer: three skills that help you navigate the
52-skill set, configure Signal in your workspace after install, and switch between layout
variants that change how the skills are invoked. No artifacts produced. No investigation
required. Start here when you are not sure where to start.

---

## When to use this namespace

Use the signal skills at the beginning of your Signal experience and when you want to
explore different invocation styles.

- You just installed Signal and want to configure it in your workspace.
- You are not sure which skill to run and want to see the full command index.
- You want to switch from `/discover-competitors` style invocation to `/competitors` style.
- You want to see which layout fits your actual usage pattern.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `signal` | Show the Signal command index. All 52 skills organized by namespace with one-line descriptions. `/signal <namespace>` to see skills in one namespace. `/signal --bare` to see bare command names. | Anytime you are not sure which skill to run. The starting point. |
| `signal-setup` | Configure Signal in your workspace after installation. Checks for existing CLAUDE.md and .github/copilot-instructions.md. Shows a preview of the Signal section it will add. Asks confirmation before writing. Safe to re-run -- detects existing Signal sections and skips if already configured. | Once, after installing Signal skills. |
| `signal-layout` | Show or change your Signal navigation layout. Five variants: A) grouped, B) phases, C) signal, D) flat, E) bare. `/signal-layout recommend` analyzes your usage pattern and suggests the best layout. `/signal-layout switch <variant>` applies the layout. | When exploring invocation styles. After install if you want to customize the layout. |

---

## The five layout variants

Signal ships with five invocation styles. All produce the same output -- only the command
format changes.

**A) Grouped** (default) -- skills organized under 7 namespace prefixes:

```
/discover-competitors     /specify-spec      /validate-design
/simulate-lifecycle       /govern-status     /tools-coverage
/signal
```

**B) Phases** -- 5 phase prefixes that match the investigation arc:

```
/discover-competitors     /specify-spec      /validate-design
/simulate-lifecycle       /govern-status
```

This is the same as grouped but with the signal and tools namespaces handled differently.

**C) Signal** -- everything routes through `/signal`:

```
/signal discover-competitors
/signal specify-spec
/signal simulate-lifecycle
```

Use when you want a single entry point and discoverability via tab-completion.

**D) Flat** -- old-style namespace-prefixed names preserved:

```
/scout-competitors    /draft-spec       /review-design
/flow-lifecycle       /trace-contract   /prove-hypothesis
/listen-adoption      /program-plan     /topic-status
```

Use when you are migrating from a previous Signal layout and want backward compatibility.

**E) Bare** -- shortest possible names:

```
/competitors      /spec       /design-review
/lifecycle        /contract   /hypothesis
/adoption         /plan       /status
```

Use when you run Signal frequently and want minimal typing.

---

## Switching layouts

```
/signal-layout
```

Shows your current layout and the available variants with one-line descriptions.

```
/signal-layout switch D
```

Applies the flat layout (old-style namespace-prefixed names). Runs the install script for
that variant.

```
/signal-layout recommend
```

Analyzes which skills you have used most. Suggests the layout that best matches your
pattern: if you use 30+ skills, grouped is efficient; if you use 5-6 skills repeatedly,
bare saves typing; if you are onboarding a team, signal-routed maximizes discoverability.

---

## What signal-setup writes

signal-setup appends a Signal section to your CLAUDE.md (or .github/copilot-instructions.md
for GitHub Copilot users). The section advertises available skills in your current layout
and reinforces the inertia rule.

Example output section (abbreviated):

```markdown
## Signal — Evidence Before Commitment

Available skills: /discover-competitors, /discover-feasibility, /specify-spec,
/validate-design, /simulate-lifecycle, /govern-status, and 46 more.

Run /signal to see the full command index.

The inertia rule: before any feature decision, assess "why would teams do nothing?"
The primary competitor is always the status quo.
```

Signal-setup is safe to re-run. If a Signal section already exists in CLAUDE.md, it detects
and skips it. Use it after upgrading to a new version of Signal that adds skills.

---

## Common patterns

**Run /signal before asking what to do.** The signal skill shows the full 52-skill index
organized by namespace. Before asking "what skill should I run next?", run `/signal` to
see the options. `/signal discover` narrows to the 9 discover skills.

**Run signal-setup once per workspace.** After installing Signal, run signal-setup to add
the skill advertisements to your CLAUDE.md. This makes Signal's skills visible to Claude
Code on every future session in that workspace.

**Try signal-layout recommend after 2-3 weeks of use.** The layout recommendation is most
useful after you have established a usage pattern. If you find yourself typing long prefixed
names repeatedly, the recommend command will identify which shorter layout suits your pattern.

---

## What's next

- **[discover](discover.md)** -- the first namespace for most investigations.
- **[govern](govern.md)** -- govern-status shows investigation coverage. Start here if a
  topic is already registered.
- **[QUICKSTART](../QUICKSTART.md)** -- the five-step minimal workflow from idea to first
  readiness signal.
