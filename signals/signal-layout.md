You are running /signal-layout.

Show or change your Signal navigation layout. Three modes:

---

## MODE 1: DISPLAY (called bare -- no arguments)

Show the current binding installed in .claude/skills/:

Scan .claude/skills/ for all SKILL.md files. Group by prefix pattern to identify the binding:
- Names like /discover-competitors, /specify-spec -> FLAT binding
- Names like /competitors, /spec -> BARE binding
- Names like /signal-competitors, /signal-spec -> SIGNAL binding
- Namespace aggregators (/discover, /specify) present -> GROUPED binding

Display:
```
Current layout: [FLAT / BARE / SIGNAL / GROUPED / UNKNOWN]

Available skills by namespace:
  discover  (N skills): /discover-competitors, /discover-feasibility, ...
  specify   (N skills): /specify-spec, /specify-proposal, ...
  [etc.]

Total: N skills installed

To switch layouts: /signal-layout switch <flat|bare|signal|grouped>
To get a recommendation: /signal-layout recommend
```

---

## MODE 2: SWITCH (called with "switch <variant>")

/signal-layout switch flat
/signal-layout switch bare
/signal-layout switch signal
/signal-layout switch grouped

Display the install command to run:
```
To switch to [VARIANT] binding, run:
  ./install/install-[variant].sh

This will reinstall all skills with [VARIANT] naming convention.
Current skills will be replaced.

[VARIANT] naming:
  flat:    /discover-competitors, /specify-spec, /validate-design
  bare:    /competitors, /spec, /design
  signal:  /signal-competitors, /signal-spec, /signal-design
  grouped: /discover (menu), /discover-competitors (direct)
```

---

## MODE 3: RECOMMEND (called with "recommend")

/signal-layout recommend

Glob signals/**/*-*.md to see which skills have been used.
Count runs per namespace. Identify usage pattern.

```
Usage analysis:
  Most-used namespace: [namespace] (N runs)
  Skill runs total: N
  Cross-namespace sessions: N

Recommendation: [FLAT / BARE / SIGNAL / GROUPED]
Reason: [1-2 sentences explaining why this layout fits the usage pattern]

  If heavy CLI user with many namespaces: FLAT (clear namespace prefix)
  If minimal typers / single plugin: BARE (shortest commands)
  If multi-plugin workspace: SIGNAL (collision-safe prefix)
  If new users or teams who need discovery: GROUPED (menus)
```

DISPLAY ONLY -- no file written.
