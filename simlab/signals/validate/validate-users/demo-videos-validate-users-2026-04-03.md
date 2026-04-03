---
skill: validate-users
topic: demo-videos
date: 2026-04-03
aggregate_score: 3.4
---

# validate-users: demo-videos

TARGET ARTIFACT: C:\src\signals\docs\superpowers\specs\2026-04-03-demo-video-pipeline-design.md

Demo Video Pipeline Design -- a series of 5-8 minute automated demo videos showing Signal skills in action, produced via VHS + FFmpeg + ElevenLabs, distributed as OneDrive links. Target audience: Microsoft Principal PMs, Partners, VPs.

---

## SCORE SUMMARY TABLE

| Character | Role | Score (1-5) | Current workaround (today, without this) | Top friction phrase (verbatim) |
|-----------|------|-------------|------------------------------------------|-------------------------------|
| Priya | AI-enthusiast Principal PM | 4 | Watches recorded Teams calls where a colleague screen-shares a tool, then asks in Slack for the repo link | "I already get this -- show me the 30-second install, not the 5-minute tour" |
| Marcus | Skeptical Principal PM | 2 | Ignores tool pitches; asks for a live 1:1 from someone he trusts who already uses it on a real project | "An AI-narrated video about an AI tool -- that is the uncanny valley of credibility" |
| Diana | Partner engineering leader | 3 | Delegates tool evaluation to a senior IC, reads the IC's one-page summary, decides based on that | "I need to know what happens when 40 PMs install this, not what happens when one PM runs a command" |
| Raj | VP with 30-second patience | 3 | Opens a link, watches 10 seconds, decides forward-or-delete based on whether the first frame looks relevant | "Ninety seconds for an install video is eighty seconds too long for me" |
| Keiko | Non-technical business PM | 5 | Asks a technical PM to explain a tool verbally, then decides whether to attend a deeper session | "This is the first time I could see what the tool does without someone translating for me" |
| -- | **Aggregate** | **(17/5 = 3.4)** | | |

---

## PERSONA WALKTHROUGHS

---

### Priya (AI-enthusiast Principal PM)

**Step 1 -- Current workaround (before anything else):**
Priya watches recorded Teams calls where a colleague screen-shares a tool while talking through it, then asks in Slack for the repo link. She has done this for Copilot, GitHub Actions, and three internal prototypes. The screen-shares are usually 20-40 minutes with dead air while things load.

**Step 2 -- Scenario brief:**
Priya gets a OneDrive link from a colleague with the message "You should look at this Signal thing." Priya is on a bus, AirPods in, phone in hand. She has the install video and the investigate video available. She will watch both if the first one hooks her.

**Step 3 -- Walkthrough:**

I tap the OneDrive link and it opens the install video. I read "automated demo videos showing Signal skills in action" and (excitement) I am immediately ready to watch because I have been wanting to see this kind of tool in a polished format instead of shaky screen-shares. The video opens with "You are a principal PM. Someone sent you a link. Here is what happens in the next 90 seconds." I like the framing -- it is talking to me specifically.

I watch the terminal commands run. I see `./bootstrap.sh` execute and I read "63 skills ready" on screen. I think: that is a lot of skills. But (friction) I do not get a sense of what any single skill does at this point. The install video tells me the tool exists but does not tell me why I would reach for it tomorrow morning when I have a real feature decision.

I tap into the investigate video. The PM character types `/discover-hypothesis api-copilot` and I watch the hypothesis form. Then I see the PM push back: "The inertia framing is wrong -- teams already use Swagger UI with manual review. Reframe around that existing workaround." That is the moment I lean in. That pushback is exactly what I do in my own work. The spec says "The human is the hero" and I can see it working here.

But (confusion) the narration is AI-generated and I know it immediately. The ElevenLabs voice is good but it is not a person I recognize. In my world, credibility comes from a name attached to a voice. I do not know who made this or who is vouching for it. The spec mentions "No camera, no mic" as a design principle, but for me that removes the social proof layer entirely.

I finish the investigate video and I am ready to install. But (friction) the video does not tell me how. There is no "click here to get started" card at the end. The install video showed the commands but I am watching the investigate video. I have to go back and find Demo 0 again.

**Step 4 -- Inertia fields:**
Beats current process: The 5-7 minute format is vastly better than Priya's 20-40 minute recorded Teams calls. She can watch on mobile. The pacing is deliberate instead of accidental.
Loses to current process: Priya's current workaround includes a real person she can ask follow-up questions to in Slack. The video is one-directional. She cannot ask "does this work with Azure DevOps boards?" after watching.

**Step 5 -- Score: 4**

---

### Marcus (Skeptical Principal PM)

**Step 1 -- Current workaround (before anything else):**
Marcus ignores tool pitches entirely. When a tool actually matters, someone he trusts -- usually a specific senior IC on his team -- tells him over coffee. Then he asks that person to show him on their machine, on their project, with their data. He has never adopted a tool from a video.

**Step 2 -- Scenario brief:**
Marcus receives the OneDrive link in a group email from a well-meaning skip-level. The subject line says "Check this out -- AI-powered product design." Marcus sees "AI-powered" and his skepticism activates. He has been pitched Copilot Workspace, GitHub Copilot, Cursor, Devin, and four internal prototypes in the last six months. He opens the link to be polite but he is looking for reasons to close the tab.

**Step 3 -- Walkthrough:**

I click the link. The video opens and an AI voice starts narrating. I immediately think: this is an AI-generated voice narrating an AI tool. That is a credibility problem. The spec says "ElevenLabs API" for voiceover and I can hear it. It sounds polished but it does not sound like a person I would trust with a product recommendation.

I watch the PM character type commands. The spec describes this as "authentic output" because "VHS runs real commands." Fine. But (friction) I have no way to verify this. It could be a carefully scripted happy path. In my experience, every tool demo shows the happy path. I want to see what happens when the hypothesis is wrong, when the competitor data is stale, when the skill produces garbage. The spec lists six demos and every single one has a "Money Moment" -- there is no "Failure Moment" where the tool is honest about its limits.

I watch the PM push back on framing and I think: that is staged. The pushback in the tape file was authored by the same person who wrote the AI response. The spec says "The human is the hero" but (confusion) the human and the AI are both authored by the same script writer. There is no genuine adversarial interaction.

I read the narration: "Six dimensions investigated. One recommendation. No meetings required." That claim makes me less likely to adopt, not more. I have been a PM for fifteen years. Meetings are not the bottleneck. The bottleneck is knowing which meetings to skip and which to have. A tool that claims to replace meetings tells me the maker does not understand my job.

I close the video at the four-minute mark. I do not watch Demo 0. I do not install. If someone I trust tells me they shipped a feature using this, I will reconsider.

**Step 4 -- Inertia fields:**
Beats current process: The video is shorter than a live 1:1 demo. Marcus can reject it faster, which he considers a feature.
Loses to current process: Marcus's current workaround (a trusted person showing him on their machine) provides credibility, context, and the ability to ask "but what about my specific situation." The video provides none of these.

**Step 5 -- Score: 2**

---

### Diana (Partner engineering leader)

**Step 1 -- Current workaround (before anything else):**
Diana delegates tool evaluation to a senior IC she trusts. That IC spends 2-3 hours with the tool, writes a one-page summary (what it does, what it costs, what breaks, who benefits), and Diana makes the org-wide decision based on that summary plus a 15-minute conversation. Diana does not personally evaluate tools.

**Step 2 -- Scenario brief:**
Diana receives the link from a Principal PM on her team who says "I think this could help the whole org." Diana has 200 PMs across 8 teams. She needs to decide whether to (a) ignore it, (b) forward it to her evaluator IC, or (c) pilot it with one team. She will watch the first 2 minutes of one video to make the triage call.

**Step 3 -- Walkthrough:**

I open the investigate video because the install video sounds too basic for my level. The video shows a PM running investigation skills. I watch the hypothesis form and the competitive analysis run. The output is structured, which I appreciate. But (confusion) I cannot tell from the video what the operational model is. How do my PMs get this? Is it a VS Code extension? A CLI? The spec says "Claude Code" in the tape file but I see `claude` in a terminal and I do not know what that means for my org.

I read the spec's distribution section: "Shared via OneDrive links. Each demo is standalone." That works for me -- I can forward a link. But (friction) there is no deployment section. If I decide to pilot this, the spec tells me nothing about: licensing for 200 PMs, IT approval process, data residency (my teams work on FedRAMP-scoped products), or what happens to the artifacts the tool produces. The spec says "ElevenLabs API key ($5/mo starter plan)" which tells me there is a per-user SaaS dependency. That is a procurement conversation I do not want to have.

The "Demo Series" table lists six videos. I count: Demo 0 is 90 seconds, Demos 1-5 are 5-8 minutes each. That is 30-45 minutes of video total. (friction) I would not watch all of these and I would not ask my evaluator IC to watch all of these either. I need a single 3-minute "what is this and why should my org care" video. The spec does not have that tier.

I notice the spec says "Reproducible. Change the script, re-render." That is genuinely interesting to me because it means the videos can be updated as the tool evolves. But the spec does not address versioning -- if I share a link today and the video changes next month, do my PMs see the new version or the old one?

I would forward this to my evaluator IC with the note: "Watch Demo 3 (Spec + Persona Test) and tell me if this is real."

**Step 4 -- Inertia fields:**
Beats current process: The video gives Diana a faster triage signal than asking her IC to do a full evaluation. She can watch 2 minutes and decide whether to delegate deeper investigation.
Loses to current process: Diana's IC evaluation produces a one-page summary tailored to Diana's org (cost, risk, who benefits). The video is generic -- it does not address Diana's specific constraints (scale, compliance, procurement).

**Step 5 -- Score: 3**

---

### Raj (VP with 30-second patience)

**Step 1 -- Current workaround (before anything else):**
Raj gets pitched tools weekly. His current process: opens the link, looks at the first visual for 10 seconds, decides if it is worth 60 more seconds. If yes, he watches up to 90 seconds total. If the tool seems promising, he forwards it to a Partner on his team with "thoughts?" He never installs anything himself.

**Step 2 -- Scenario brief:**
Raj receives an email from a Partner (Diana) with the subject "Tool for PM investigation workflow -- video demo." Raj has a 10-minute gap between meetings. He opens the link on his Surface laptop.

**Step 3 -- Walkthrough:**

I click the link. The first thing I see is a terminal window. (friction) That is already a problem. I am a VP. I do not use terminals. A terminal window tells me this is a developer tool, and I am not a developer. The spec says the theme is "Catppuccin Mocha" which is a dark terminal theme. Dark terminal themes say "engineering" to me, not "product leadership."

The narration starts: "You are watching an AI-driven investigation session." (confusion) I do not know what an "investigation session" is in this context. Investigation of what? The spec says the narration opens the investigate video with context about a PM exploring a feature decision, but the framing assumes I know what Signal is. I do not. I have never heard of it. The video jumps into `/discover-hypothesis` without establishing why I should care.

I watch for 20 seconds. The PM types a command and text starts streaming. It is dense text in a terminal. I cannot read it at this resolution on my Surface. The spec says "Brief pause on key outputs (findings, recommendations, scores)" but (friction) the pause happens on a wall of terminal text that I cannot parse at a glance. I need the key finding extracted and shown as a title card, not as raw terminal output.

I would watch longer if: (a) the first 10 seconds showed a before/after -- "This PM used to spend 3 weeks on feature investigation, now it takes 45 minutes," or (b) the first frame was a clean title card with the value proposition, not a terminal.

The spec mentions Demo 0 (Install) as the "Gateway Video" at 90 seconds. That is closer to my attention budget. But (friction) even Demo 0 starts with terminal commands. For a VP audience, the gateway should be a 30-second sizzle reel: title cards with the five things Signal does, one screenshot of structured output, a "forward this to your PM team" call to action. No terminal.

I close the tab after 30 seconds. I do not forward to Diana because I do not have a clear sentence to attach. If someone asked me "what is Signal?" after watching, I could not answer.

**Step 4 -- Inertia fields:**
Beats current process: If Raj did watch a full video, it would be faster than a live pitch meeting. The async format respects his calendar.
Loses to current process: Raj's current process (a Partner filtering tools for him) provides a pre-digested recommendation. The video asks Raj to form his own opinion from raw tool output, which he will not do.

**Step 5 -- Score: 3**

---

### Keiko (Non-technical business PM)

**Step 1 -- Current workaround (before anything else):**
Keiko asks a technical PM on her team to explain developer tools verbally. The technical PM translates: "It is like if you could get a junior analyst to do the competitive research and spec review before you start." If the translation sounds useful, Keiko attends a 30-minute demo session. She has never installed a CLI tool.

**Step 2 -- Scenario brief:**
Keiko's technical PM sends her the investigate video with the message "This is what I was telling you about -- watch the first 3 minutes." Keiko opens it on her laptop at home, sound on, full screen.

**Step 3 -- Walkthrough:**

I press play. The narration says "You are watching an AI-driven investigation session. A principal PM wants to know: should we add Copilot to the API management portal? Instead of scheduling six meetings, they run one command." I understand that immediately. The narration is doing the translation work that my technical PM usually does. I do not need anyone to explain this to me -- the video explains itself.

I watch the PM type `/discover-hypothesis api-copilot`. I do not know what a "hypothesis skill" is technically, but the narration explains: "The discover-hypothesis skill states a falsifiable claim and defines what would prove it wrong." I can follow that. The output appears as structured text. I can read the hypothesis, the falsification criteria, the confidence level. This looks like what I produce manually in PowerPoint after three days of research.

Then the PM pushes back: "The inertia framing is wrong -- teams already use Swagger UI with manual review." I think: that is exactly the kind of judgment call I make. The video is showing me that the PM is driving, not the AI. The spec says "human as hero" and I experience that. I feel represented.

The competitive analysis runs and I see a structured table of competitors with inertia as option zero. (excitement) This is what I spend two weeks building in Excel. The tool produced it in 90 seconds. Even if I need to edit 40% of it, I just saved myself the blank-page problem.

The narration says "Six dimensions investigated. One recommendation. No meetings required." I think: if this is real, I want it. But (friction) the video does not show me how a non-technical person would install this. Demo 0 shows terminal commands -- `./bootstrap.sh` -- and I do not know what that means. I would need my technical PM to install it for me.

I watch the full video. I send it to two PMs on my team with: "Can one of you set this up for me?" That is the highest compliment I give a tool.

**Step 4 -- Inertia fields:**
Beats current process: Keiko can watch the video without a translator. The narration layer does what her technical PM used to do verbally. The structured output is self-explanatory.
Loses to current process: Keiko's current workaround (asking a technical PM) includes a personalized recommendation: "You should use this for your compliance spec." The video is generic. It does not tell Keiko which of her specific projects would benefit.

**Step 5 -- Score: 5**

---

## CROSS-PERSONA SYNTHESIS

### Universal friction (3+ personas flagged this)

| Finding | Personas | Friction type |
|---------|----------|---------------|
| No clear call-to-action or next step at the end of non-install videos | Priya, Marcus, Raj | friction |
| Terminal-first visual framing signals "developer tool" not "PM tool" | Marcus, Diana, Raj | confusion |
| AI-generated narration voice undermines credibility for skeptical viewers | Marcus, Raj, Diana | fear |
| No video tier for the 30-second executive audience | Diana, Raj, Priya | friction |

### Role-specific friction (1-2 personas only)

| Finding | Persona(s) | Why role-specific |
|---------|------------|-------------------|
| No failure mode shown -- every demo has a "Money Moment" but no honest limitation | Marcus | Skeptics specifically look for intellectual honesty about limits |
| No org-scale deployment information (licensing, data residency, procurement) | Diana | Only Partner-level leaders evaluate tools for 200+ person orgs |
| Dense terminal text unreadable at laptop resolution during "pause" moments | Raj | Only the shortest-attention viewer notices resolution issues at speed |
| Non-technical users cannot self-install from Demo 0 | Keiko | Only non-technical PMs lack CLI familiarity |
| Scripted pushback feels staged rather than genuine | Marcus | Only skeptics question the authenticity of the authored interaction |

### Persona conflicts

Priya's "Beats" (polished async format, faster than screen-shares) is Marcus's "Loses" (polished format feels staged, removes the authenticity of a real person demoing on their machine). The same design choice -- automated production quality -- increases trust for enthusiasts and decreases trust for skeptics.

Keiko's "Beats" (narration translates technical content into plain language) is Raj's "Loses" (narration starts with jargon like "investigation session" that assumes familiarity). The narration works for someone willing to listen for 30 seconds but fails for someone who needs the value proposition in the first frame.

### Inertia summary

- **Strongest adoption pull:** Keiko (non-technical business PM) -- the video replaces her dependence on a human translator and gives her direct access to understanding the tool. She is the likeliest early adopter because the video solves her specific access problem.
- **Highest inertia:** Marcus (skeptical Principal PM) -- his trust model requires a personal recommendation from a specific trusted person. No video format can substitute for that. He will only adopt after someone he trusts adopts first.
- **Rollout implication:** Target Priya-type enthusiasts first; they will become the trusted voices that convert Marcus-type skeptics. Create a separate 30-second sizzle reel for Raj/Diana-tier executives who will never watch a 5-minute video. Do not rely on the video alone -- pair it with a named champion who can answer follow-up questions.

---

## AMEND LOOP

---
**Amend proposal -- Marcus (Skeptical Principal PM) scored 2/5**

Current workaround being displaced:
Marcus ignores tool pitches entirely. When a tool actually matters, someone he trusts -- usually a specific senior IC on his team -- tells him over coffee. Then he asks that person to show him on their machine, on their project, with their data. He has never adopted a tool from a video.

What the workaround provides that the artifact does not:
Marcus's workaround provides a named, trusted human who has used the tool on a real project and can answer adversarial questions -- the video provides no social proof from a recognizable person and no demonstration of failure modes.

Verbatim artifact text with highest friction:
> "No camera, no mic. Everything is authored as text, rendered by machines."

Proposed artifact change:
Add a "Demo 6: Limits" video (3 minutes) that shows a skill producing a bad recommendation, the PM catching it and correcting course, and a voiceover that says "Signal is wrong about 20% of the time -- here is how you catch it." Additionally, add a 15-second intro card to each video showing the name and title of a real Microsoft PM who uses Signal, with a quote: "I used this on [project]. Here is what happened." This does not require the person on camera -- just a name, title, and one-sentence endorsement as a title card. Place this card before the narration begins. This addresses the "No camera, no mic" principle by keeping the production automated while adding the social proof layer Marcus requires.

Expected new score: 3/5
Reasoning: A named endorser and an honest failure demo address Marcus's two core objections (no social proof, no intellectual honesty about limits) without requiring live recording.

---
