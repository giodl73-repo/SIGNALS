You are running /signal-layout.

Signal skills can be installed with different command naming styles to match how you like to work. This skill shows what you currently have and what each style looks like so you can try a different one.

---

## MODE 1: DISPLAY (bare -- just type /signal-layout)

Scan .claude/skills/ to identify your current layout:

```
YOUR CURRENT LAYOUT: [FLAT / BARE / SIGNAL / GROUPED / PREFIXED]

How your skills are named:
  /discover-competitors    <- flat style (namespace-skill)
  /specify-spec
  /validate-design
  ...

This is how you run Signal skills in this workspace.
```

Detect by prefix pattern:
- `/discover-competitors`, `/specify-spec`  -> FLAT
- `/competitors`, `/spec`                   -> BARE
- `/signal-competitors`, `/signal-spec`     -> SIGNAL prefix
- Aggregator menus (`/discover`, `/specify`) present -> GROUPED

---

## MODE 2: COMPARE (type /signal-layout compare)

Show all 4 styles side by side so you can see what each looks like:

```
SIGNAL LAYOUT STYLES
================================

FLAT (current default)          BARE (shortest)
  /discover-competitors           /competitors
  /specify-spec                   /spec
  /validate-design                /design
  /simulate-lifecycle             /lifecycle
  /rhythm-status                  /status

SIGNAL (prefix for multi-plugin) GROUPED (menus + direct)
  /signal-competitors             /discover        <- shows menu
  /signal-spec                    /discover-competitors
  /signal-design                  /specify         <- shows menu
  /signal-lifecycle               /specify-spec

Which style fits you:
  FLAT:    You want clear namespace context (/discover-X, /specify-X)
  BARE:    You type a lot and want the shortest commands possible
  SIGNAL:  You use multiple Claude Code plugins -- avoids name collisions
  GROUPED: You're new to Signal and want discoverable menus
```

---

## MODE 3: SWITCH (type /signal-layout switch <style>)

/signal-layout switch flat
/signal-layout switch bare
/signal-layout switch signal
/signal-layout switch grouped

Tell the user how to switch:
```
To switch to [STYLE]:

  Run this from your project root:
    bash <(curl -s https://raw.githubusercontent.com/your-org/signal/main/install/install-[style].sh)

  Or if you have Signal source locally:
    bash /path/to/signal/install/install-[style].sh

This replaces your current .claude/skills/ with the [STYLE] variant.
Your signals/ artifacts are untouched -- only the command names change.
```

---

## MODE 4: RECOMMEND (type /signal-layout recommend)

Look at how you work and suggest the best layout:

Glob signals/**/*-*.md -- how many artifacts exist? Which namespaces have you used?
Check if you use long or short invocations (inferred from artifact patterns).

```
Based on your signals/ usage:
  Skills run: N across M namespaces
  Usage pattern: [focused (1-2 namespaces) / broad (5+ namespaces)]

Recommendation: [FLAT / BARE / SIGNAL / GROUPED]
Why: [one sentence specific to your usage]
```

DISPLAY ONLY -- no file written.
