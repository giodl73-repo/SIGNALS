# Signal Navigation Study — Simulated Results
## A/B/C/D/E Variant Test — 2026-03-17

**Task**: "Your team is considering building a dark mode feature for your product. Use Signal to gather enough evidence to decide whether to build it. You have 30 minutes."

**Study protocol**: C:/src/sim/study/README.md
**Pre-registered predictions (S3-12)**:
- C wins time-to-first-artifact
- E wins repeat-session speed
- A/B split by role (engineers -> A, PMs -> B)
- D is lowest error rate

---

## Participant Summaries

---

### VARIANT A — grouped
**Participant**: Alex, Senior Engineer
**Binding**: `/scout` -> namespace menu

#### Session Transcript

**[T+0:00]** Alex opens Claude Code. Reads the CLAUDE.md stub. Sees a list of `/scout`, `/draft`, `/review`, `/flow`, `/trace`, `/prove`, `/listen`, `/program`, `/topic` entries with one-line descriptions.

> "OK. Namespaces. Like a tool hierarchy. I'll start with the obvious one — scout the landscape."

**[T+0:45]** Types:
```
/scout dark-mode
```
Gets back: "Scout namespace — which skill? competitors / feasibility / naming / compliance / market / stakeholders / positioning / requirements"

> "Ah, there's a menu. That's reasonable."

**[T+1:15]** Types:
```
/scout-competitors dark-mode
```
Artifact writes to `simulations/scout/competitors/dark-mode-competitors-2026-03-17.md`. First artifact produced.

**[T+5:30]** Reads through the competitors artifact. Notes the inertia analysis leads the document. "Oh, the primary competitor is doing-nothing. That's actually the right framing. Our users already have OS-level dark mode, that's the workaround."

**[T+6:00]** Types:
```
/scout-feasibility dark-mode
```
Artifact writes. Alex skims: traffic-light rating for each feasibility dimension. "Green on API surface, amber on CSS theming complexity, red on legacy component library compatibility."

**[T+9:00]** Pauses. Looks back at the namespace list. Thinks: "Should I draft a spec now? Or prove the hypothesis first?"

**[T+9:30]** Types:
```
/prove-hypothesis dark-mode
```
[ERROR] Claude responds: "This skill needs a hypothesis statement. Usage: `/prove-hypothesis <topic> --claim '<claim>'`"

> Alex hesitates. "What's my claim?" Types on whiteboard: "Dark mode will increase evening usage sessions by 15%+."

**[T+11:00]** Retypes:
```
/prove-hypothesis dark-mode --claim "dark mode increases evening session duration by 15% or more"
```
Artifact writes. Good output. Three falsification conditions listed.

**[T+15:00]** Types:
```
/listen-adoption dark-mode
```
Artifact writes. Rogers archetype breakdown: early adopters high, late majority resistance noted around "theme inconsistency across modules."

**[T+18:00]** Types:
```
/topic-status dark-mode
```
Terminal display: 3 signals found, 9 recommended. "Coverage: 33% — not ready for design commit."

> "Thirty-three percent. I need more signals but I'm running out of time."

**[T+20:00]** Types:
```
/draft-spec dark-mode
```
Artifact writes. Alex reads the spec outline and notes a section titled "Inertia case" — the OS-level dark mode workaround is already surfaced from the competitors artifact context.

**[T+24:00]** Types:
```
/review-design dark-mode
```
Artifact writes. Multi-expert review fires. Alex is pleased: "This caught a theming system gap I hadn't thought about — the charts and data visualization components aren't covered by the CSS variable approach."

**[T+28:00]** Types:
```
/topic-status dark-mode
```
Coverage: 5 signals / 9 recommended. 56%. "Not quite. But enough to have an informed conversation."

**[T+30:00]** Session ends.

#### Metrics

- **First command typed**: `/scout dark-mode` (then corrected to `/scout-competitors dark-mode`)
- **Time to first artifact**: 1 min 15 sec
- **Skills used**: `/scout-competitors`, `/scout-feasibility`, `/prove-hypothesis`, `/listen-adoption`, `/topic-status` (x2), `/draft-spec`, `/review-design`
- **Namespaces covered**: scout, prove, listen, topic, draft, review (6 of 9)
- **Artifacts produced**: 6
- **Error count**: 1 (missing `--claim` on `/prove-hypothesis`)
- **Confusion points**:
  - Initial `/scout dark-mode` hit the menu layer instead of running directly — one extra step
  - `/prove-hypothesis` requires an explicit claim string; Alex did not know this upfront, caused ~90-second pause
- **NPS**: 8 — "I liked that the inertia framing showed up automatically in the competitors artifact. The namespace grouping matched how I think. The prove-hypothesis friction was real but not a blocker."

---

### VARIANT B — groups
**Participant**: Priya, PM
**Binding**: `/discover`, `/specify`, `/validate`, `/simulate`, `/govern` (phase-based grouping)

#### Session Transcript

**[T+0:00]** Priya opens Claude Code. Reads the CLAUDE.md. Sees five commands with phase descriptions: discover, specify, validate, simulate, govern.

> "OK. I'm trying to decide whether to build something. That's discovery. Start there."

**[T+0:30]** Types:
```
/discover dark-mode
```
The `/discover` phase group routes to scout namespace skills. Gets back a sub-menu: "Discovery phase — competitors / feasibility / market / requirements / stakeholders / compliance / naming / positioning."

> "Great — competitors first."

**[T+1:00]** Types:
```
/discover competitors dark-mode
```
[ERROR] Claude responds: "Unknown command `/discover competitors`. Try `/scout-competitors dark-mode` or type `/discover` alone to see options."

> Priya blinks. "Oh. The phase command doesn't chain to sub-skills directly." Hesitation. Reads the error message again.

**[T+2:00]** Types:
```
/scout-competitors dark-mode
```
Artifact writes. First artifact at T+2:00.

**[T+4:00]** Reads competitors artifact. "The OS-level dark mode as primary competitor — that's a great point. I need to address this in the brief."

**[T+5:00]** Types:
```
/discover market dark-mode
```
[ERROR] Same routing error. "OK, the `/discover` wrapper doesn't work as a prefix. Got it."

**[T+5:30]** Types:
```
/scout-market dark-mode
```
Artifact writes. Market sizing: developer tools segment highest fit, consumer-facing products medium fit.

**[T+8:00]** Priya switches mental model. "I'll just use the full skill names. The phase grouping was an onramp that didn't quite work."

**[T+8:30]** Types:
```
/scout-feasibility dark-mode
```
Artifact writes.

**[T+11:00]** Types:
```
/specify dark-mode
```
Gets sub-menu: "Specify phase — spec / proposal / brainstorm / pitch."

> "This one seems to work as a menu." Types `/draft-spec dark-mode`. Artifact writes.

**[T+15:00]** Types:
```
/validate dark-mode
```
Gets sub-menu. Types `/review-design dark-mode`. Artifact writes.

**[T+18:00]** Types:
```
/review-customers dark-mode
```
Artifact writes. Priya is engaged: "12 personas evaluating dark mode. C-04 (accessibility-focused user) has the most interesting reaction — dark mode is actually critical for her, not cosmetic."

**[T+22:00]** Types:
```
/listen-adoption dark-mode
```
Artifact writes.

**[T+25:00]** Types:
```
/topic-status dark-mode
```
Coverage: 5 signals / 9 recommended. 56%.

**[T+27:00]** Types:
```
/topic-story dark-mode
```
Artifact writes. Priya reads: "This is the synthesis I'd put in a brief. The inertia case, the accessibility angle from the customer review, the adoption chasm risk — it's all threaded together."

**[T+30:00]** Session ends.

#### Metrics

- **First command typed**: `/discover dark-mode`
- **Time to first artifact**: 2 min 0 sec (one error before first artifact)
- **Skills used**: `/scout-competitors`, `/scout-market`, `/scout-feasibility`, `/draft-spec`, `/review-design`, `/review-customers`, `/listen-adoption`, `/topic-status`, `/topic-story`
- **Namespaces covered**: scout, draft, review, listen, topic (5 of 9)
- **Artifacts produced**: 8
- **Error count**: 2 (both from attempting to chain phase commands: `/discover competitors dark-mode`, `/discover market dark-mode`)
- **Confusion points**:
  - Phase commands (`/discover`, `/specify`, `/validate`) read as chainable but are not — they return menus, not routers
  - After two errors Priya abandoned the phase wrappers and used full skill names directly
  - Once she switched to direct skill names, session was fluent
- **NPS**: 7 — "The phase labels (discover, specify, validate) matched my PM mental model perfectly — that's what I call my workflow. But the commands themselves didn't chain the way I expected. Once I figured that out, it was great. Fix the chaining and this is a 9."

---

### VARIANT C — signal conversational
**Participant**: Marcus, Junior Dev
**Binding**: Single `/signal` entry point with intent routing

#### Session Transcript

**[T+0:00]** Marcus opens Claude Code. Reads the CLAUDE.md. Sees one command: `/signal`. Small description: "Show the Signal command index. Lists all available skills organized by namespace."

> "There's only one command? OK. Let's see what this does."

**[T+0:20]** Types:
```
/signal dark mode feature decision
```
Signal routes by intent. Returns: "Detected intent: feature pre-commitment investigation. Recommended entry: `/scout-competitors dark-mode` to assess the inertia case first. Or type `/signal` alone to browse all skills."

> "Oh! It figured out what I want." Marcus is delighted. Types the recommended command.

**[T+1:00]** Types:
```
/scout-competitors dark-mode
```
Artifact writes. First artifact at T+1:00.

**[T+3:00]** Reads competitors output. "Primary competitor is OS dark mode — that's smart. I didn't think of that as a competitor." Types:

```
/signal what should I do next for dark-mode investigation
```

Signal returns: "You have 1 signal. To complete minimum viable coverage, run: (1) `/scout-feasibility dark-mode`, (2) `/prove-hypothesis dark-mode --claim <your-claim>`, (3) `/topic-status dark-mode` to check readiness."

> "Whoa, it knows what I've run and tells me what's next." Marcus follows the suggestions.

**[T+5:00]** Types:
```
/scout-feasibility dark-mode
```
Artifact writes.

**[T+7:00]** Types:
```
/signal what's a good hypothesis for dark mode
```
Signal returns: "A falsifiable hypothesis for dark mode might be: 'Shipping dark mode reduces evening churn in our developer audience by 10% or more.' Try `/prove-hypothesis dark-mode --claim 'dark mode reduces evening churn by 10% in developer audience'`"

> "It even wrote the claim for me." Marcus runs it.

**[T+8:30]** Types:
```
/prove-hypothesis dark-mode --claim "dark mode reduces evening churn by 10% in developer audience"
```
Artifact writes. Marcus did not stumble on the `--claim` syntax because Signal pre-composed it.

**[T+12:00]** Types:
```
/signal what namespaces haven't I covered yet for dark-mode
```
Signal returns coverage gap summary: "Missing: draft, review, listen, flow, trace, program. For a design commit decision, recommend: `/draft-spec`, `/review-users`, `/listen-adoption`."

**[T+13:00]** Types:
```
/draft-spec dark-mode
```
Artifact writes.

**[T+16:00]** Types:
```
/review-users dark-mode
```
Artifact writes. Marcus reads: "Persona 3 (developer doing long coding sessions) rated 'critical.' Persona 5 (light-usage admin user) rated 'nice to have.'"

**[T+19:00]** Types:
```
/listen-adoption dark-mode
```
Artifact writes.

**[T+22:00]** Types:
```
/topic-status dark-mode
```
Coverage: 5 signals. 56%.

**[T+24:00]** Types:
```
/signal I need to make a decision on dark mode
```
Signal returns: "Your current coverage (5/9 namespaces, 56%) supports a design commit decision but not a ship decision. Key open gaps: flow simulation (behavior at runtime), trace-contract (implementation match). For a design commit today, you have enough. Run `/topic-story dark-mode` to produce the decision brief."

**[T+25:30]** Types:
```
/topic-story dark-mode
```
Artifact writes. Marcus reads: "This is a brief I could show my team lead right now."

**[T+28:00]** Marcus runs two more out of curiosity:
```
/review-customers dark-mode
```
Artifact writes.

**[T+30:00]** Session ends.

#### Metrics

- **First command typed**: `/signal dark mode feature decision`
- **Time to first artifact**: 1 min 0 sec (fastest of all variants)
- **Skills used**: `/scout-competitors`, `/scout-feasibility`, `/prove-hypothesis`, `/draft-spec`, `/review-users`, `/listen-adoption`, `/topic-status`, `/topic-story`, `/review-customers`
- **Namespaces covered**: scout, prove, draft, review, listen, topic (6 of 9)
- **Artifacts produced**: 8
- **Error count**: 0
- **Confusion points**:
  - None observed. Signal's intent routing deflected every point where other participants stumbled
  - Marcus did not know what `/prove-hypothesis` needed; Signal composed the `--claim` for him
  - One moment of potential confusion (coverage gaps) was answered by the `/signal what namespaces...` query before it became an error
- **NPS**: 9 — "It felt like the tool knew what I was trying to do. I never had to figure out the command syntax — it handed me the commands. I'd use this every time."

---

### VARIANT D — flat
**Participant**: Elena, Tech Lead
**Binding**: Full prefixed skill names (`/scout-competitors`, `/trace-contract`, etc.)

#### Session Transcript

**[T+0:00]** Elena opens Claude Code. Reads the CLAUDE.md. Sees a flat list of 80+ commands with prefixes. All visible.

> "Long list. But I can scan it. I know what I want — scout the competitive landscape first. Look for a dark mode entry point."

**[T+0:30]** Scans list. Finds `/scout-competitors` immediately. "There it is."

**[T+0:50]** Types:
```
/scout-competitors dark-mode
```
Artifact writes. First artifact at T+0:50. Fastest raw start of any variant.

**[T+3:00]** "The inertia analysis is good. OS dark mode is the primary competitor, plus the argument that developers just invert colors in their terminal settings. This changes my framing."

**[T+4:00]** Types:
```
/scout-feasibility dark-mode
```
Artifact writes.

**[T+6:30]** Elena moves methodically. Scans list again. Thinks: "I should check requirements before drafting."

**[T+7:00]** Types:
```
/scout-requirements dark-mode
```
Artifact writes. Requirements extraction: Must-have: CSS variable layer; Should-have: system preference auto-detect; Won't-have (this iteration): per-component overrides.

**[T+10:00]** Types:
```
/draft-spec dark-mode
```
Artifact writes.

**[T+12:30]** Types:
```
/trace-state dark-mode
```
[MISMATCH] Claude returns: "trace-state requires a state machine description or component name. What state are you tracing? Example: `/trace-state dark-mode --component ThemeProvider`"

Elena: "Right, this is a design-time skill, not a discovery skill. I jumped ahead."

**[T+13:00]** Types:
```
/trace-state dark-mode --component ThemeProvider
```
Artifact writes. "Theme state: system-detected | user-override | unset. Transition coverage looks good."

**[T+16:00]** Types:
```
/prove-hypothesis dark-mode --claim "dark mode reduces perceived eyestrain complaints in 30-day post-ship feedback"
```
Artifact writes.

**[T+19:00]** Types:
```
/flow-lifecycle dark-mode
```
Artifact writes. Elena is surprised: "Flow lifecycle for dark mode? Let's see what it generates." Reads: "Theme resolution flow: browser system preference detected -> user preference stored in localStorage -> CSS variable layer applied -> per-component override checked. Exception paths: localStorage blocked by privacy settings."

> "That privacy-settings exception is one I would have missed. Good catch."

**[T+22:00]** Types:
```
/review-design dark-mode
```
Artifact writes.

**[T+25:00]** Types:
```
/topic-status dark-mode
```
Coverage: 6 signals / 9 recommended. 67%. Highest single-session coverage so far.

**[T+27:00]** Types:
```
/listen-support dark-mode
```
Artifact writes. Top predicted support tickets: "My app looks different than the screenshots," "Charts are unreadable in dark mode," "Dark mode toggled unexpectedly after OS update."

**[T+30:00]** Session ends.

#### Metrics

- **First command typed**: `/scout-competitors dark-mode`
- **Time to first artifact**: 0 min 50 sec (raw fastest; she scanned the flat list and typed directly)
- **Skills used**: `/scout-competitors`, `/scout-feasibility`, `/scout-requirements`, `/draft-spec`, `/trace-state`, `/prove-hypothesis`, `/flow-lifecycle`, `/review-design`, `/topic-status`, `/listen-support`
- **Namespaces covered**: scout, draft, trace, prove, flow, review, listen, topic (8 of 9)
- **Artifacts produced**: 9
- **Error count**: 1 (missing component on `/trace-state`, immediately self-corrected)
- **Confusion points**:
  - One minor mismatch on `/trace-state`: Elena expected it to auto-detect context; it needed a component hint
  - No conceptual confusion. Flat naming removed all ambiguity about what each command does
  - Elena naturally covered the most namespaces because she could scan all available commands and pick strategically
- **NPS**: 8 — "The flat list is a lot to look at, but for a tech lead who knows what she wants, it's faster than any menu. I hit 8 namespaces in 30 minutes. The one error was easy to fix. High trust in the tool."

---

### VARIANT E — bare
**Participant**: Kevin, Staff Engineer
**Binding**: `/competitors`, `/contract`, `/hypothesis`, etc. (shortest possible command names)

#### Session Transcript

**[T+0:00]** Kevin opens Claude Code. Sees a flat list of bare command names. No `/scout-` prefix, no `/draft-` prefix. Just `/competitors`, `/feasibility`, `/spec`, `/hypothesis`, `/adoption`, etc.

> "Clean. Minimal. I like it already."

**[T+0:25]** Types:
```
/competitors dark-mode
```
Artifact writes. First artifact at T+0:25. Fastest first-artifact of all participants.

**[T+2:30]** Reads output. "Good. Inertia leads. OS dark mode is the real competitor."

**[T+3:00]** Types:
```
/feasibility dark-mode
```
Artifact writes.

**[T+4:30]** Types:
```
/hypothesis dark-mode --claim "dark mode adoption predicts 30-day retention in our developer segment"
```
Artifact writes. Kevin knew the syntax. No errors.

**[T+7:00]** Types:
```
/spec dark-mode
```
Artifact writes.

**[T+9:00]** Types:
```
/contract dark-mode
```
[MISMATCH] Claude returns: "trace-contract requires expected vs. actual output to compare, or a spec path. Do you want to run this against the dark-mode spec you just wrote? Try `/contract dark-mode --against simulations/draft/specs/dark-mode-spec-2026-03-17.md`"

Kevin: "Fair. Let me give it the spec."

**[T+9:30]** Types:
```
/contract dark-mode --against simulations/draft/specs/dark-mode-spec-2026-03-17.md
```
Artifact writes. "Contract check against spec: CSS variable layer coverage 100%. localStorage persistence: not specified in spec (gap). Theme provider state machine: spec does not enumerate error states (gap)."

> "Two gaps in my own spec. Useful."

**[T+12:00]** Types:
```
/lifecycle dark-mode
```
Artifact writes. Kevin notes: "Privacy-blocked localStorage is an exception path I need to handle."

**[T+14:00]** Types:
```
/adoption dark-mode
```
Artifact writes.

**[T+16:00]** Types:
```
/requirements dark-mode
```
Artifact writes.

**[T+18:00]** Types:
```
/state dark-mode --component ThemeProvider
```
Artifact writes.

**[T+20:00]** Types:
```
/design dark-mode
```
Artifact writes. Multi-expert review across 6 disciplines.

**[T+22:00]** Types:
```
/customers dark-mode
```
Artifact writes. 12-persona evaluation.

**[T+25:00]** Types:
```
/status dark-mode
```
Coverage: 8 signals / 9 recommended. 89%. Highest single-session coverage of any participant.

**[T+27:00]** Types:
```
/story dark-mode
```
Artifact writes.

**[T+29:00]** Types:
```
/support dark-mode
```
Artifact writes with 90-day support ticket predictions.

**[T+30:00]** Session ends.

#### Metrics

- **First command typed**: `/competitors dark-mode`
- **Time to first artifact**: 0 min 25 sec (absolute fastest)
- **Skills used**: `/competitors`, `/feasibility`, `/hypothesis`, `/spec`, `/contract`, `/lifecycle`, `/adoption`, `/requirements`, `/state`, `/design`, `/customers`, `/status`, `/story`, `/support`
- **Namespaces covered**: scout, prove, draft, trace, flow, listen, review, topic (8 of 9 — only `program` untouched)
- **Artifacts produced**: 13
- **Error count**: 1 (missing `--against` on `/contract`; self-corrected in 30 seconds)
- **Confusion points**:
  - `/contract` needs an explicit spec path when run at design-time; Kevin needed one prompt to supply it
  - No conceptual confusion at any point
  - Kevin's primary behavior: methodical breadth, leveraging the short commands to move quickly across namespaces without hesitation cost
- **NPS**: 9 — "The short names remove every character of friction. I can think about what I need to run, not about how to spell the command. One hiccup on `/contract` but the error message was clear and I fixed it in seconds. This is how I'd want every tool to work."

---

## Metrics Summary Table

| Metric | A (Alex) | B (Priya) | C (Marcus) | D (Elena) | E (Kevin) |
|---|---|---|---|---|---|
| Variant | grouped | groups | signal | flat | bare |
| Role | Senior Engineer | PM | Junior Dev | Tech Lead | Staff Engineer |
| First command | `/scout dark-mode` | `/discover dark-mode` | `/signal dark mode feature decision` | `/scout-competitors dark-mode` | `/competitors dark-mode` |
| Time to first artifact | 1 min 15 sec | 2 min 0 sec | 1 min 0 sec | 0 min 50 sec | 0 min 25 sec |
| Artifacts produced | 6 | 8 | 8 | 9 | 13 |
| Namespaces covered | 6 | 5 | 6 | 8 | 8 |
| Error count | 1 | 2 | 0 | 1 | 1 |
| NPS | 8 | 7 | 9 | 8 | 9 |

---

## Synthesis

### Which variant won on time-to-first-artifact?

**E (bare) won at 0 min 25 sec**, followed by D (flat) at 0 min 50 sec.

C (signal conversational) was 1 min 0 sec — third fastest, but with zero errors and no prior knowledge of the command surface required. B (groups) was slowest at 2 min 0 sec due to one error before the first artifact landed.

**Key observation**: Pre-registered prediction said C wins time-to-first-artifact. That prediction was **NOT confirmed**. D and E are faster because experienced users skip the discovery layer entirely — they type the full command on sight. C is faster than A and B because the router absorbs the menu-navigation and error-correction cost. The pre-registered prediction underestimated how much raw command speed matters for experienced users.

### Which variant had highest NPS?

**C (signal) and E (bare) tied at NPS 9.**

C won on NPS for a different reason than E: Marcus (junior dev) experienced the tool as "thinking for me," which produced delight. Kevin (staff engineer) experienced the tool as "zero ceremony," which produced satisfaction. Same NPS score from entirely different emotional paths.

A and D tied at NPS 8. B was lowest at NPS 7, driven by the two chaining errors. Notably, Priya explicitly said the phase model matched her mental model — the friction was entirely in the command-chaining behavior, not the concept.

### Which variant produced most coverage?

**E (bare) produced most coverage**: 8 namespaces, 13 artifacts, 89% signal coverage.

D (flat) tied on namespaces (8) with 9 artifacts. The difference was Kevin's velocity with short commands — he was able to run more skills within the same 30-minute window because each command cost fewer keystrokes to compose.

C and A tied at 6 namespaces / 8 artifacts and 6 artifacts respectively. C's routing guidance drove coverage evenly; A's coverage was shaped by Alex's own intuitions (he went deep into prove and listen but never touched flow or trace).

B produced 8 artifacts across 5 namespaces — good artifact count but narrowest namespace coverage, because Priya's phase-based mental model kept her in discover and validate phases and she never stepped into flow or trace.

### Failure modes per variant

**A (grouped)**:
- Menu layer adds one extra step per namespace entry
- `/prove-hypothesis` friction: requires explicit `--claim` string that is not surfaced in the menu description
- Recovery was fast (90-second pause), but created a break in momentum

**B (groups)**:
- Phase wrappers (e.g., `/discover competitors dark-mode`) appear chainable but are not
- Two errors from the same misunderstanding; Priya never got a clear signal that the chaining model was wrong until she tried it twice
- After abandoning the phase wrapper she was fluent — the error was at the surface, not in the model
- Risk: participants who do not get an error message that explains the correct pattern may try variations for longer before giving up

**C (signal)**:
- No observed failure modes in this session
- Latent risk: if the intent router misclassifies the user's goal, the recommended command may be wrong and the user has no fallback vocabulary to correct it
- Marcus never needed to test the failure case; the routing succeeded every time

**D (flat)**:
- `/trace-state` required a component hint that was not obvious at design-time
- The flat list requires scanning time at the start of each session; experienced users like Elena treated it as a fast lookup table, but a less-experienced user might feel overwhelmed by 80+ options
- No conceptual failure modes: naming was unambiguous throughout

**E (bare)**:
- `/contract` needed an explicit `--against` path when no prior spec had been supplied in that session context
- The bare names occasionally lose their namespace context (is `/contract` about trace-contract or something else?) — Kevin had the experience to know, but a first-time user with less context might misfire
- The high coverage Kevin achieved is partly a function of his seniority, not just the variant

### Pre-registered prediction evaluation

| Prediction | Result | Confirmed? |
|---|---|---|
| C wins time-to-first-artifact | E won (0:25), D second (0:50), C third (1:00) | NOT CONFIRMED |
| E wins repeat-session speed | E had fastest first-artifact and highest coverage; architectural match | CONFIRMED (directional) |
| A/B split by role (engineers->A, PMs->B) | Alex (engineer) rated A at 8; Priya (PM) rated B at 7; A beat B for both roles | PARTIALLY CONFIRMED — engineers do prefer A; but B failed to win the PM segment |
| D is lowest error rate | D had 1 error (tied with A and E). C had 0 errors. | NOT CONFIRMED — C had zero errors; D was tied-second |

**Summary**: 1 of 4 predictions confirmed outright. 1 directionally confirmed. 2 not confirmed.

The primary surprise: C's error-free performance (prediction 3 should have considered that zero-error routing is a distinct category from "low error rate"). D was predicted to be lowest error because experienced users know full prefixed names — but signal-conversational routing removes the error opportunity entirely.

The secondary surprise: The groups variant (B) failed specifically on command chaining, not on the phase model itself. Priya's PM mental model was validated — but the implementation of `/discover` as a non-chainable menu broke her expectation. This is fixable and does not invalidate the phase grouping concept.

### Design recommendations surfaced by simulation

1. **The inertia framing is the strongest first-impression for all participants.** Every participant who ran `/scout-competitors` first commented on the "primary competitor = doing nothing" framing. No one expected it. All found it useful. This is a retention hook.

2. **`/prove-hypothesis` needs its `--claim` in the menu description.** Two participants (A and B) would have stumbled here; C avoided it only because Signal composed the claim. The parameter should be mentioned in the skill description in `/scout` menu output.

3. **Chaining errors in B are a correctable surface bug.** The fix is either: make `/discover competitors dark-mode` a valid routing alias, or change the error message to explicitly say "use the full skill name: `/scout-competitors dark-mode`" rather than returning a generic "unknown command."

4. **E's coverage dominance is velocity, not luck.** Kevin covered 8/9 namespaces because short commands removed hesitation cost. The implication: discoverability is not the bottleneck for repeat users; command length is.

5. **C's zero-error run is the strongest case for conversational routing as an onramp.** The signal router should be positioned as a training-wheels layer, not a permanent entry point — Marcus would eventually want to graduate to direct skill names as fluency increases.

---

---

## Variant B Fixed — Re-run with Chaining Bug Corrected

**Re-run date**: 2026-03-17 (post-fix)
**Bug fixed**: `/discover` aggregator now shows correct invocation syntax for each sub-skill. Typing `/discover` returns a listing where each entry reads `/discover-competitors <topic>` (not `/discover competitors <topic>`). The chaining misread is eliminated because the help text matches the actual invocation pattern.
**What changed**: `/discover competitors dark-mode` (two-word chain) no longer appears to be a valid pattern — the menu text never showed it as one. Priya now sees `/discover-competitors dark-mode` as the literal command to type.

---

### VARIANT B FIXED — groups (bug fixed)
**Participant**: Priya, PM (re-run)
**Binding**: `/discover` -> lists all `discover-*` skills with correct `/discover-<skill> <topic>` syntax

#### Session Transcript (Fixed)

**[T+0:00]** Priya opens Claude Code. Reads the CLAUDE.md. Sees five phase commands: `/discover`, `/specify`, `/validate`, `/simulate`, `/govern`.

> "Discovery first. Same as before."

**[T+0:30]** Types:
```
/discover
```
Gets back:

```
Discovery phase — gather competitive and market intelligence before committing.

  /discover-competitors <topic>    competitive landscape + inertia analysis
  /discover-market <topic>         market sizing + segment fit
  /discover-feasibility <topic>    technical + resource feasibility
  /discover-requirements <topic>   requirement extraction from intent
  /discover-stakeholders <topic>   stakeholder map + influence model
  /discover-compliance <topic>     regulatory + policy surface
  /discover-naming <topic>         naming analysis + trademark signals
  /discover-positioning <topic>    positioning + differentiation framing
```

> "Oh, that's clean. `/discover-competitors dark-mode` — that's the command."

**[T+1:00]** Types:
```
/discover-competitors dark-mode
```
Artifact writes to `simulations/scout/competitors/dark-mode-competitors-2026-03-17.md`. First artifact at T+1:00.

> "OS-level dark mode is the primary competitor — love that framing. Same insight as the briefing I read."

**[T+3:30]** Reads competitors artifact fully. Notes the accessibility angle (WCAG contrast compliance). Thinks: "I want to see the market side."

**[T+4:00]** Types:
```
/discover-market dark-mode
```
Artifact writes. Market sizing: developer tools segment strongest fit, consumer-facing products medium, enterprise dashboards high latent demand.

> "Enterprise dashboards — that's a use case I hadn't weighted. Good to have."

**[T+6:00]** Types:
```
/discover-feasibility dark-mode
```
Artifact writes. Traffic-light summary: green on API surface, amber on CSS theming depth, red on legacy component library compatibility.

> "Red on legacy components. That's the build risk. I'll flag this in the spec."

**[T+8:30]** Priya pauses. Looks at the phase list. "I've done three in discovery. Time to specify."

**[T+9:00]** Types:
```
/specify
```
Gets sub-menu:
```
Specify phase — translate signals into structured artifacts.

  /specify-spec <topic>            full feature specification
  /specify-proposal <topic>        lightweight proposal document
  /specify-brainstorm <topic>      ideation + option surfacing
  /specify-pitch <topic>           elevator pitch for stakeholders
```

> "Perfect. `/specify-spec dark-mode`."

**[T+9:30]** Types:
```
/specify-spec dark-mode
```
Artifact writes. Spec pulls in the competitors and feasibility signals already gathered. Priya notices: "It already surfaced the legacy component risk in the spec's risk section — it read my earlier artifacts."

**[T+13:00]** Reads spec carefully. Annotates the risk section mentally. "I want to validate this against users before I take it further."

**[T+13:30]** Types:
```
/validate
```
Gets sub-menu:
```
Validate phase — test signals against human and technical perspectives.

  /validate-users <topic>          user persona evaluation (12 personas)
  /validate-customers <topic>      customer segment fit analysis
  /validate-design <topic>         multi-discipline design review
  /validate-code <topic>           technical implementation review
```

**[T+14:00]** Types:
```
/validate-users dark-mode
```
Artifact writes. Priya reads: "Persona C-04 (accessibility-critical user) rated dark mode as critical — not cosmetic. Persona C-09 (enterprise admin) flagged chart legibility in dark mode as a launch blocker."

> "C-09's chart concern aligns with the amber CSS signal in feasibility. That's a real pattern."

**[T+17:30]** Types:
```
/validate-customers dark-mode
```
Artifact writes. Customer segment analysis: 3 of 4 customer segments rate dark mode as high-value; the enterprise dashboard segment rates it as revenue-risk if absent.

> "Revenue-risk if absent. That changes the priority framing significantly."

**[T+20:00]** Priya looks at the phase list again. "I should check listen — adoption risk is the thing I'd want to bring to the PM review."

**[T+20:30]** Types:
```
/listen dark-mode
```
Gets sub-menu (Priya correctly infers the pattern now):
```
Listen phase — understand adoption dynamics and support surface.

  /listen-adoption <topic>         Rogers archetype adoption analysis
  /listen-feedback <topic>         feedback signal modeling
  /listen-support <topic>          90-day support ticket prediction
```

**[T+21:00]** Types:
```
/listen-adoption dark-mode
```
Artifact writes. Rogers breakdown: early adopters very high, early majority high, late majority resistance around "theme inconsistency across modules," laggards resistant to any UI change.

**[T+23:30]** Types:
```
/topic-status dark-mode
```
Coverage: 6 signals / 9 recommended. 67%.

> "67%. Better than expected for 23 minutes. Let me see if the story holds together."

**[T+24:00]** Types:
```
/topic-story dark-mode
```
Artifact writes. Priya reads the synthesis: "This is exactly the brief structure I'd bring to a product review — the inertia case, the enterprise dashboard urgency, the accessibility mandate, the legacy component build risk. All threaded."

> "This is a 9/10 for me. The phase model maps exactly to how I think. Discover, specify, validate, listen — that's my workflow. And now the commands work."

**[T+27:00]** Priya goes back to validate one more time.

**[T+27:30]** Types:
```
/validate-design dark-mode
```
Artifact writes. Multi-expert review: "Theming system gap — charts and data visualization components are not covered by the CSS variable layer approach."

> "Same gap Alex found. Consistent signal."

**[T+30:00]** Session ends.

#### Metrics (Fixed)

- **First command typed**: `/discover` (then `/discover-competitors dark-mode`)
- **Time to first artifact**: 1 min 0 sec (from session start; `/discover` at T+0:30, artifact at T+1:00)
- **Skills used**: `/discover-competitors`, `/discover-market`, `/discover-feasibility`, `/specify-spec`, `/validate-users`, `/validate-customers`, `/listen-adoption`, `/topic-status`, `/topic-story`, `/validate-design`
- **Namespaces covered**: scout, draft, review (users + customers + design), listen, topic (6 of 9)
- **Artifacts produced**: 10
- **Error count**: 0
- **Confusion points**:
  - None. The `/discover` menu showed the correct invocation pattern and Priya followed it immediately
  - Sub-menus for `/specify`, `/validate`, `/listen` all worked the same way — Priya generalized the pattern from the first interaction and never hit a wall
  - The phase-based mental model (discover -> specify -> validate -> listen) drove natural namespace coverage without Priya ever having to think about namespace vocabulary
- **NPS**: 9 — "The phase model matches how I work. Discover first, then specify, then validate — that's exactly my PM workflow. Once the commands showed me the right syntax, it clicked immediately. I would use this before every feature brief."

---

#### Comparison: Original B vs Fixed B

| Metric | Original B (Priya) | Fixed B (Priya) | Delta |
|---|---|---|---|
| Time to first artifact | 2 min 0 sec | 1 min 0 sec | -1:00 |
| Artifacts produced | 8 | 10 | +2 |
| Namespaces covered | 5 | 6 | +1 |
| Error count | 2 | 0 | -2 |
| NPS | 7 | 9 | +2 |
| Phase model used | Partially (abandoned after errors) | Fully (used for all 4 phases) | Full adoption |
| Session fluency | Disrupted at T+1:00 and T+5:00, recovered at T+8:00 | Uninterrupted from T+0:30 onward | Eliminated friction points |

**Root cause confirmed**: The original 2-error session, 2-minute delay, and NPS 7 were entirely attributable to the chaining bug. The underlying phase model was sound — Priya validated it fully once the commands reflected it correctly. The fix eliminated all three symptoms simultaneously.

---

#### Does Fixed B Now Challenge the Predictions?

**Pre-registered prediction**: "A/B split by role (engineers->A, PMs->B)"

- Original B: NPS 7 — prediction PARTIALLY CONFIRMED (PM preferred A-style direct names after abandoning phase model)
- Fixed B: NPS 9 — prediction NOW CONFIRMED. Priya's PM-native phase model (discover/specify/validate) drove her session fluently and she preferred it over flat skill names. The prediction was correct about the mental model fit; the original session failed to confirm it only because of the implementation bug.

**Time-to-first-artifact prediction**: Fixed B at 1 min 0 sec now ties Variant C (Marcus, 1 min 0 sec). The original B at 2:00 was an outlier caused by a bug, not a structural property of the groups binding.

**Error-rate prediction**: Fixed B at 0 errors ties Variant C. Phase-based aggregators with correct syntax displayed are not inherently error-prone — the original B was a surface-bug artifact.

---

#### Updated Variant Ranking with Fixed B

| Rank | Variant | NPS | Time to first artifact | Errors | Namespaces | Notes |
|---|---|---|---|---|---|---|
| 1 (tied) | C (signal) | 9 | 1 min 0 sec | 0 | 6 | Zero errors; routing handles all navigation |
| 1 (tied) | B Fixed (groups) | 9 | 1 min 0 sec | 0 | 6 | Phase model matches PM workflow; tied C on all key metrics |
| 1 (tied) | E (bare) | 9 | 0 min 25 sec | 1 | 8 | Fastest raw speed; highest coverage; senior-user advantage |
| 4 (tied) | A (grouped) | 8 | 1 min 15 sec | 1 | 6 | Solid engineer path; menu layer adds one step |
| 4 (tied) | D (flat) | 8 | 0 min 50 sec | 1 | 8 | Strategic coverage; scanning cost for new users |

**Note**: E still wins on raw speed and coverage. C and B Fixed are now tied on NPS, time to first artifact, error count, and namespace coverage. The distinguishing factor between them is user profile: C (signal conversational) is the best onramp for users who don't know the skill surface; B Fixed (groups) is the best fit for users who already have a phase-based workflow model and just need the commands to reflect it.

---

#### Updated Synthesis: Where Does B Rank Overall?

With the chaining bug fixed, Variant B is no longer the weakest performer — it is now co-equal with Variant C as the second-best option for new users (behind E for experienced users on velocity metrics).

The original synthesis stated: "B failed to win the PM segment" because of implementation friction. That conclusion is reversed. Fixed B wins the PM segment clearly: NPS 9, 0 errors, full phase-model adoption, 10 artifacts in 30 minutes. The A/B-by-role prediction (S3-12) is now confirmed rather than partially confirmed.

The more important finding is structural: the groups binding (phase-based aggregators) is a valid and high-performing navigation pattern when the aggregator's help text displays correct invocation syntax. The original failure was not a design flaw — it was a documentation bug in the `/discover` command output. One line of corrected help text produced a 2-point NPS lift, halved time-to-first-artifact, eliminated all errors, and added 2 artifacts and 1 additional namespace.

This is the highest return-on-fix of any correction identified across all five variants. For PM-profile users specifically, the groups binding is now the recommended default.

---

## Raw Study Logs

```
Participant: Alex     Variant: A (grouped)  Date: 2026-03-17
First command: /scout dark-mode
Time to first artifact: 1 min 15 sec
Artifacts produced: 6
Namespaces covered: scout, prove, listen, topic, draft, review (6)
Error count: 1
NPS: 8
Notes: One-step menu layer before skill runs. prove-hypothesis --claim friction.
```

```
Participant: Priya    Variant: B (groups)   Date: 2026-03-17
First command: /discover dark-mode
Time to first artifact: 2 min 0 sec
Artifacts produced: 8
Namespaces covered: scout, draft, review, listen, topic (5)
Error count: 2
NPS: 7
Notes: Two errors from chaining phase commands. Fluent after switching to direct skill names.
```

```
Participant: Marcus   Variant: C (signal)   Date: 2026-03-17
First command: /signal dark mode feature decision
Time to first artifact: 1 min 0 sec
Artifacts produced: 8
Namespaces covered: scout, prove, draft, review, listen, topic (6)
Error count: 0
NPS: 9
Notes: Signal routing absorbed all friction points. Zero errors. Routing composed --claim for prove-hypothesis.
```

```
Participant: Elena    Variant: D (flat)     Date: 2026-03-17
First command: /scout-competitors dark-mode
Time to first artifact: 0 min 50 sec
Artifacts produced: 9
Namespaces covered: scout, draft, trace, prove, flow, review, listen, topic (8)
Error count: 1
NPS: 8
Notes: Strategic breadth enabled by flat list scan. One component hint error on trace-state, self-corrected.
```

```
Participant: Kevin    Variant: E (bare)     Date: 2026-03-17
First command: /competitors dark-mode
Time to first artifact: 0 min 25 sec
Artifacts produced: 13
Namespaces covered: scout, prove, draft, trace, flow, listen, review, topic (8)
Error count: 1
NPS: 9
Notes: Highest coverage, fastest velocity. One --against path error on /contract. Short command names removed hesitation cost.
```

```
Participant: Priya    Variant: B Fixed (groups, chaining bug corrected)   Date: 2026-03-17
First command: /discover (then /discover-competitors dark-mode)
Time to first artifact: 1 min 0 sec
Artifacts produced: 10
Namespaces covered: scout, draft, review, listen, topic (6)
Error count: 0
NPS: 9
Notes: Zero errors after fix. Full phase-model adoption (discover/specify/validate/listen). 2-point NPS lift vs original. Time-to-first-artifact halved. A/B-by-role prediction now confirmed.
```
