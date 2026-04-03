# Demo Video Pipeline Design

One shell command renders a professional demo video from three text inputs.
No camera, no mic, no editing software. The pipeline shows Microsoft Principal PMs
what Signal does for their daily work -- and proves we built the demo with the
same AI-driven process we are demonstrating.

**Date:** 2026-04-03
**Status:** Draft (revised with 4 role reviews + 3 signal artifacts)
**Owner:** Gio
**Target:** Demo 0 + Demo 3 ready by 2026-04-18; full series by 2026-05-02

## Positioning

For Principal PMs evaluating whether AI tools accelerate product design,
Signal is the only skill-based CLI that produces auditable investigation artifacts
in minutes, unlike ChatGPT/Copilot chat which produce disposable conversation threads.

**Claim each video proves:** You can investigate, spec, simulate, and validate a feature
decision with AI -- and the artifacts are real documents you would actually use.

**Inertia competitor (adoption level):** A PM receives the OneDrive link, skims the
subject line, and does nothing. The link competes with 100+ daily messages for a
90-second attention window. The most likely outcome is not "watch and reject"
but "never click the link."

**Why the pipeline beats live demos:** Live demos fail unpredictably (API latency,
weak AI output), permanently damaging credibility. The video pipeline shows Signal
at its capability ceiling, not its variance floor.

## Jobs to Be Done

**Primary persona:** Principal PM (L66-L67) who writes specs, runs design reviews,
and makes feature go/no-go decisions weekly.

**JTBD:** "When I am evaluating a new tool for my product design workflow, I want to
see it solve a problem I recognize in under 2 minutes, so I can decide whether to
invest 10 minutes installing it."

**Explicitly not serving (in v1):** Partners (org-wide tooling decisions) and VPs
(portfolio-level metrics). They receive a separate 30-second executive summary clip.
If a Principal PM adopts and succeeds, they become the internal champion who sells up.

### Alternatives Considered

| Alternative | Why Not |
|-------------|---------|
| Live demo by a human | Fails unpredictably. One bad AI response kills credibility permanently. |
| Interactive sandbox/playground | Requires infrastructure. PM must install before seeing value. |
| Guided first-run in terminal | Good for post-adoption onboarding, not pre-adoption persuasion. |
| README + screenshots | Static. Cannot show the PM steering the AI in real time. |
| **Produced video (chosen)** | Shows Signal at its ceiling. Reproducible. No live variance. |

## Architecture

```
scenario.txt          narration script (.md)
     |                        |
     v                        v
terminal-demo            ElevenLabs API
     |                        |
     v                        v
  .cast file             narration.mp3
     |                        |
     v                        |
  svg-term                    |
     |                        |
     v                        |
  animated .svg               |
     |                        |
     v                        |
  Puppeteer + FFmpeg          |
     |                        |
     v                        |
  terminal.mp4                |
     |                        |
     +----------+-------------+
                |
             FFmpeg
                |
     +----------+----------+-----------+
     |          |          |           |
     v          v          v           v
  video     subtitles  title cards  endorsement
                |
     +----------+-----------+
     |                      |
     v                      v
  full-demo.mp4         clip-30s.mp4
```

**One command:** `./render-demo.sh <demo-name>` produces both `demos/final/<name>.mp4`
(full) and `demos/final/<name>-clip.mp4` (30-second highlight).

**Platform note:** VHS (Charm) was the original capture tool but freezes on Windows 11
due to ttyd/ConPTY issues (#631). The pipeline uses terminal-demo + svg-term + Puppeteer
instead, which runs entirely on native Windows with no WSL2 or Docker required. Scenario
files are authored text (commands + expected output from real sessions), matching the
spec's "curated, not faked" principle.

## Two-Tier Format

Every demo ships as two files:

| Tier | Duration | Audience | Purpose |
|------|----------|----------|---------|
| **Clip** | 30 seconds | VP, skeptic, first-touch | Hook. Shows the money moment only. Links to full version. |
| **Full** | 90s-5 min | Principal PM who clicked through | Walkthrough. Shows the PM steering AI through the whole flow. |

The clip is what gets sent in Teams messages. The full version is what converts.

**Duration constraint (revised from 5-8 min to 90s-3 min):** B2B engagement drops
sharply after 2 minutes. Demos 1-5 target 3 minutes max. Demo 0 (Install) stays
at 90 seconds. If a flow needs more time, split into two videos rather than
extending one.

## Opening Frame: PM Context First

Terminal-first visuals signal "developer tool" and PMs self-select out in seconds.
Every demo opens with a PM-recognizable context before showing terminal:

| Demo | Opening Frame (5-8 seconds) | Transition |
|------|----------------------------|------------|
| 0: Install | "You got a link from a colleague." | Browser -> terminal |
| 1: Investigate | "Your skip-level asked: should we build this?" | Question on screen -> terminal |
| 3: Spec + Persona | "You wrote a spec. Before the review meeting..." | Spec excerpt on screen -> terminal |
| 4: Simulate | "The spec passed review. But does the flow work?" | Architecture diagram -> terminal |
| 5: Validate | "Engineering is ready to build. Are customers ready?" | Roadmap slide -> terminal |
| 6: Meta | "You had an idea. You opened Claude Code." | This conversation -> terminal |

## Social Proof Layer

AI narrating about AI is a credibility problem for skeptics. Each video opens with
a 10-15 second endorsement card before the demo begins:

```
[Dark background, white text, no camera]

"I ran this on my actual feature spec.
 It found three issues my team missed in review."
 -- [Name], Principal PM, [Product Area]
```

This is text only. No camera, no recording. Just a real PM's words.
Collect 3-5 endorsements from early adopters before the launch push.

## Narration and Authenticity

**Voice:** ElevenLabs API as primary TTS provider. Voice: "Daniel" (professional,
neutral). Fallback: Azure AI Speech "Guy" (neural).

**API contract the render script expects:**
- Input: text string + voice ID
- Output: mp3 file
- This contract makes the provider swappable.

**Cost estimate:** 6 demos x 3 min narration = ~18 min audio. ElevenLabs Starter
($5/mo) includes 30 min. Sufficient for full series + re-renders.

**Authenticity stance:** The narration acknowledges the session is curated:
"This is a representative session showing how a PM uses Signal for [task]."
No pretense of spontaneity. The audience respects honesty.

**Failure demo (Demo 7):** One video explicitly shows the tool producing a weak
result and the PM catching it, redirecting, getting a better outcome. This is
the strongest credibility move for skeptics. Title: "When AI Gets It Wrong."

## Scenario-to-Narration Sync Contract

With terminal-demo, scenario timing is deterministic (authored text, not live API
calls), which eliminates the original sync risk.

**Resolution: narration-driven timing.**

1. terminal-demo renders the scenario to .cast with authored timing.
2. svg-term + Puppeteer render .cast to terminal video. Duration is known.
3. ElevenLabs generates narration audio per section. Duration is fixed and known.
4. The render script treats narration duration as the master clock.
5. FFmpeg speed-adjusts the terminal video to match total narration duration.

**Scenario file format** (terminal-demo):

```
$ /discover-hypothesis api-copilot

## Hypothesis: API Copilot Integration

Claim: Adding Copilot to the API management portal will reduce
time-to-first-API-call by 40% for new developers.

Falsification: If onboarding time does not decrease measurably
in a 30-day pilot with 50 developers, the claim is false.

Inertia competitor: Teams currently use Swagger UI with manual
review. This works. The question is whether Copilot is 
sufficiently better to justify the switching cost.

$ The inertia framing is wrong -- teams already use Swagger UI with manual review. Reframe around that existing workaround.

Reframing around the Swagger UI workaround...
```

Commands prefixed with `$` are typed with realistic delays.
Output lines appear instantly (as they would in a real terminal).
The scenario is authored from real session output -- curated, not faked.

**Narration timestamps are derived at render time**, not authored. The narration
script specifies section order and text only. The render script calculates
timestamps from actual audio clip durations.

## Compounding Narrative

Signal's differentiator is that signals compound -- each skill builds on prior
artifacts. Standalone demos hide this claim.

**Solution:** Demos are watchable standalone, but Demos 1-5 open with a
"Previously gathered" title card (3-5 seconds) showing what signals already
exist for the topic:

```
[Title card before Demo 3: Spec + Persona Test]
Signals gathered so far:
  - discover-hypothesis: claim stated, falsification defined
  - discover-competitors: 4 alternatives mapped, inertia is #1
  - discover-synthesize: PROCEED with conditions
Now: validate the spec with 5 personas.
```

A "full campaign" supercut (all demos concatenated) is available for the viewer
who wants the complete story.

## Directory Structure

```
demos/
  scenarios/          # terminal-demo scenario files (.txt)
  narration/          # Narration scripts per demo (.md)
  titles/             # Title card text and endorsement cards
  lib/                # Pipeline scripts (parse, render, composite)
    svg-to-mp4.js     # Puppeteer SVG renderer
    parse-narration.sh # Markdown section parser
    generate-audio.sh  # ElevenLabs TTS
    composite-video.sh # FFmpeg assembly
    extract-clip.sh    # 30-second clip extraction
    generate-srt.sh    # Subtitle generation
    generate-title-card.sh  # Title card images
  raw/                # Intermediate files (git-ignored)
  audio/              # Generated voiceover (git-ignored)
  final/              # Finished mp4s and clips (git-ignored)
  render-demo.sh      # Main render script
  config.env          # API keys, voice ID, theme settings
```

## Technology Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Scenario authoring | **terminal-demo** (npm) | Renders scenario text files to asciinema .cast |
| Cast to SVG | **svg-term-cli** (npm) | Converts .cast to animated SVG |
| SVG to video | **Puppeteer** (npm) + **FFmpeg** | Renders SVG frames, encodes to mp4 |
| Video compositing | **FFmpeg** | Speed ramping, title cards, subtitles, clip extraction |
| AI voiceover | **ElevenLabs API** (primary) | Natural narration from script |
| AI voiceover | **Azure AI Speech** (fallback) | Same API contract, in-ecosystem |
| Subtitles | **FFmpeg + .srt** | Auto-generated from narration text |
| Script parsing | **jq** + bash | Parse narration markdown into sections |

### Dependencies

- `terminal-demo` -- `npm install -g terminal-demo`
- `svg-term-cli` -- `npm install -g svg-term-cli`
- `puppeteer` -- `npm install puppeteer` (local to demos/lib)
- `ffmpeg` -- `winget install Gyan.FFmpeg`
- `curl` + `jq` -- for ElevenLabs API calls
- ElevenLabs API key ($5/mo starter tier, 30 min/mo)

### Verified Working On

- Windows 11 Enterprise 10.0.26100
- Node.js v24.14.0
- FFmpeg 8.1
- No WSL2 or Docker required

## Demo Series

All demos use the same feature topic for narrative continuity.

| # | Demo | Duration | Claim | Objection Preempted | CTA |
|---|------|----------|-------|--------------------|----|
| 0 | **Install** | 90s clip | Zero to 63 skills in 90 seconds | "Looks hard to set up" | Copy the bootstrap command |
| 1 | **Investigate** | 3 min | 6 dimensions researched, no meetings | "AI research is shallow" | Run `/discover-hypothesis` on your feature |
| 3 | **Spec + Persona** | 3 min | 5 personas found 12 issues before engineering | "AI reviews are generic" | Run `/validate-users` on your spec |
| 4 | **Simulate** | 3 min | Bug found in spec before code exists | "You still need real testing" | Run `/simulate-lifecycle` on your flow |
| 5 | **Validate** | 3 min | Predicted top 10 support tickets | "You can't predict user behavior" | Run `/validate-support` on your feature |
| 6 | **Meta** | 3 min | We designed this video series with the same tools | "This is a toy" | Watch how this spec was reviewed by 4 roles |
| 7 | **Limits** | 2 min | AI got it wrong. The PM caught it. | "What happens when it fails?" | The PM is always in control |

### MVP Scope

**In scope (v1):**
- Render pipeline (`render-demo.sh`)
- Demo 0 (Install) -- the gateway
- Demo 3 (Spec + Persona Test) -- the signature video
- 30-second clips for both

**Out of scope (v1):**
- Demos 1, 4, 5, 6, 7
- Custom branding/logo
- Multi-language narration
- Analytics/engagement tracking

**Explicitly not doing:**
- Live recording or human on camera
- Interactive content
- Org-wide deployment guides (Partner/VP tier content)

## Success Metrics

| Metric | Baseline | Target | How Measured |
|--------|----------|--------|-------------|
| Clip completion rate | n/a | 80% watch full 30s | Ask 5 pilot viewers |
| Full demo completion | n/a | 60% watch to CTA | Ask 5 pilot viewers |
| Install after watching | 0 | 3 of 10 pitched PMs install within 2 weeks | bootstrap.sh telemetry or follow-up |
| First skill run | 0 | 2 of 10 pitched PMs run a skill within 1 week of install | Follow-up conversation |
| Forwarded to colleague | 0 | 2 of 10 forward the clip | Ask in follow-up |

## Distribution Strategy

**The inertia-breaking insight:** A peer must send the link. Marketing links die.

### Phase 1: Validate (before full series)
- Produce Demo 0 + Demo 3 (MVP)
- Share with 3-5 friendly Principal PMs (early adopters already using Signal)
- Measure: did they finish? Did they forward? What timestamp did they stop?
- Iterate based on findings before producing remaining demos

### Phase 2: Launch
- Collect 3-5 endorsement quotes from Phase 1 viewers
- Arm each early adopter with the 30-second clip + one-line send message:
  "I used this on my [feature] spec. Found 3 issues before review. 90 seconds: [link]"
- Peer-to-peer distribution through existing Teams/Slack channels
- Embed Demo 0 clip in an internal blog post for passive discovery

### Phase 3: Expand
- Track who installed, follow up with non-responders
- Produce remaining demos based on which topics early adopters ask about
- Create "full campaign" supercut for the engaged viewer

**The send moment:** After a 1:1 where a PM complains about spec review quality,
feature decisions taking too long, or "I wish I had data before committing."
The early adopter sends the 30-second clip with a personal note.

## Acceptance Criteria

1. `render-demo.sh investigate` completes in under 15 minutes on a standard dev machine
2. Output is 1080p H.264 at 30fps, AAC audio, file size under 150MB
3. 30-second clip is extracted automatically alongside full version
4. Human typing is visible at real speed (audience can read PM decisions)
5. AI generation sections play at 2-6x (show progress, not every token)
6. Opening frame shows PM-recognizable context for at least 5 seconds before terminal
7. Endorsement card displays for 10-15 seconds at video start
8. Subtitles are present and synced to narration
9. A viewer unfamiliar with Signal can describe what the PM did after watching Demo 0

## Design Principles

1. **The human is the hero.** Every demo shows a PM making decisions -- not AI running solo. (Validated by persona test: 4 of 5 personas responded to PM-steering frame.)
2. **Curated, not faked.** Sessions are representative, not spontaneous. The narration says so. Authenticity comes from real output, not pretending the session was unscripted.
3. **Clips first, full second.** The 30-second clip is the primary distribution unit. The full demo is for people who clicked through.
4. **PM context before terminal.** Every demo opens in a world the PM recognizes before transitioning to the tool.
5. **Signals compound.** The "Previously gathered" card shows the accumulation story even in standalone viewing.
6. **Reproducible.** Change the script, re-render. Skills evolve, videos update. One command builds everything.
7. **No camera, no mic.** Everything is authored as text, rendered by machines.

## Evidence Base

This spec was revised using findings from:

| Signal | Artifact | Key Finding Applied |
|--------|----------|-------------------|
| Executive review | (inline, 2026-04-03) | Added owner/timeline, sync contract, TTS provider decision |
| PM review | (inline, 2026-04-03) | Added JTBD, success metrics, scope boundaries, acceptance criteria |
| Product Marketing review | (inline, 2026-04-03) | Added positioning, messaging strategy (claim/objection/CTA), compounding narrative |
| UX Researcher review | (inline, 2026-04-03) | Added two-tier format, duration cap, persona validation plan |
| discover-inertia | `signals/discover/discover-inertia/demo-videos-*` | Peer distribution strategy, "never click the link" as dominant path |
| validate-adoption-blocker | `signals/validate/validate-adoption-blocker/demo-videos-*` | PM-context opening frame, terminal-first is a kill blocker |
| validate-users | `signals/validate/validate-users/demo-videos-*` | 30-second executive tier, endorsement card, failure demo (Demo 7) |

## Resolved Questions

1. **Topic continuity:** Same topic across all demos. Continuity is the point of a series.
2. **Voice provider:** ElevenLabs primary, Azure fallback. Same API contract.
3. **Branding:** Deferred to v2. Clean dark theme is sufficient for v1.
