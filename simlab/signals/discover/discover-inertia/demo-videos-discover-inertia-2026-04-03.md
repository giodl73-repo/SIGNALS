---
skill: discover-inertia
topic: demo-videos
date: 2026-04-03
inertia_score: HIGH
switching_cost: LOW
---

# Inertia Analysis: demo-videos

**Feature:** A series of automated demo videos showing Signal skills in action, targeting Microsoft Principal PMs to drive adoption. Videos are produced via an automated pipeline (VHS + FFmpeg + ElevenLabs) and shared as OneDrive links.

**Question:** Why would a busy Principal PM at Microsoft do NOTHING instead of watching these videos and adopting Signal? What is the current workaround? What would have to be true for them to switch?

---

## PHASE 1 -- WORKAROUND MAP

| Field | Answer |
|-------|--------|
| Workaround name | **Hallway pitch + live walkthrough** -- the sponsor (or an early adopter) schedules a 30-minute Teams call, shares screen, and manually demonstrates Signal skills while narrating. Alternatively: the PM simply ignores the link entirely and continues with their existing tooling. |
| How it works | 1. Sponsor identifies a target PM. 2. Sends a Teams invite with a vague subject ("check out this AI tool"). 3. Runs a live demo, improvising narration. 4. PM watches passively, asks a few polite questions. 5. PM says "looks cool" and returns to their backlog. 6. No follow-up action occurs. |
| Who does it | The Signal sponsor or evangelist (1 person) + the target PM (1 person). Occasionally a skip-level manager who forwards a link with "take a look at this." |
| Frequency | 1-3 live demos per week during an active push. Each demo: 30-60 minutes of the sponsor's time + 30 minutes of the target PM's time. Prep time: 15-30 minutes per demo to choose a good topic and rehearse. |
| Implicit cost | Sponsor: ~3 hours/week (demo + prep + scheduling). At 50 weeks/year = 150 hours/year of evangelist time on live demos that convert at < 10%. Target PM: 30 minutes per demo, but the real cost is the calendar slot -- Principal PMs guard their calendars aggressively. Getting on the calendar at all is the bottleneck. |
| Hidden cost | (1) **Live demos fail unpredictably** -- API latency, unexpected errors, wrong example topic -- damaging credibility in front of exactly the audience that matters. (2) **No replay value** -- the demo is gone when the call ends; the PM cannot share it with their team or re-watch the key moment. (3) **Does not scale** -- one sponsor can demo to ~3 PMs/week; there are hundreds of Principal PMs. (4) **The "do nothing" path has zero friction** -- a PM who ignores the link pays no visible cost today. Their current workflow (meetings + documents + manual review) is slow but familiar and socially validated. |

### The dominant inertia path: ignore the link entirely

The most likely outcome is not "watch the video and reject Signal." It is: **never click the link at all.** A Principal PM receives 50-100 Teams messages and emails per day. An unsolicited OneDrive link to a demo video competes with urgent service reviews, incident escalations, partner requests, and skip-level prep. The video must earn the first 8 seconds of attention or it loses permanently.

---

## PHASE 2 -- SWITCHING COST TABLE

| Cost type | Estimate | Who bears it |
|-----------|----------|--------------|
| Learning / training | 2-4 hours to watch 2-3 videos and try one skill | Target PM |
| Integration / setup | 15-30 minutes (bootstrap.sh + claude install) | Target PM |
| Process change | 2-4 weeks to build a habit of reaching for Signal before scheduling a meeting | Target PM + their team |
| Risk during transition | Minimal technical risk. Social risk: PM uses a new tool in a review and it produces a weak artifact, damaging their credibility. | Target PM |
| **Total switching cost** | **~4-6 hours initial + 2-4 weeks habit formation** | |

Switching cost verdict: **LOW** (< 1 day of active effort)

The switching cost is not the barrier. The switching cost is trivially low. The barrier is **attention cost** -- getting a Principal PM to invest the first 90 seconds when their default is to ignore the link.

---

## PHASE 3 -- INERTIA THREAT SCORE

```
Inertia threat: HIGH

Rationale:
- The workaround (meetings + documents + manual review) is painful but
  universally practiced and socially reinforced at Microsoft.
- No one is actively looking for an alternative to "how PMs evaluate features."
  The pain is diffuse and normalized.
- There is no forcing function -- no regulatory change, no competitive crisis,
  no recent failure that makes the status quo intolerable.
- The target audience (Principal PMs) has extremely high attention cost and
  extremely low tolerance for tools that do not immediately prove value.
- Demo videos are an awareness play, not a pain-relief play. Awareness
  competes against a saturated information environment.

Override considered: NO.
- The workaround is not actively failing. It is slow and expensive, but
  every PM at Microsoft has internalized that slowness as normal.
- No team is actively searching for "AI feature investigation tools."
- No competitive event makes the status quo untenable.
```

---

## PHASE 4 -- CONDITIONS FOR INERTIA TO LOSE

Three specific conditions under which Principal PMs would abandon the workaround and adopt Signal after watching a demo video:

### Condition 1: The video shows THEIR problem, not yours

The PM must recognize their own current pain in the first 8 seconds. Not "look at this cool AI tool" but "you spent 6 hours last week in meetings to decide whether to add Copilot to your portal -- here is the same answer in 5 minutes." The video must open with a problem statement the PM had THIS WEEK, not a generic capability demo. If the topic in the video matches a real decision the PM is currently facing, they will watch. If it does not, they will close the tab.

**Closest to true today:** The spec already calls for the human PM to be the hero (Design Principle 1) and for authentic VHS-captured output. But the spec does not address topic selection strategy -- which real decisions are Principal PMs making right now? The topic in the demo must be a live, recognized decision, not a hypothetical.

### Condition 2: The video must produce a shareable artifact, not just a viewing experience

A Principal PM who watches a video and thinks "that was impressive" will do nothing. A Principal PM who watches a video and can immediately forward a concrete artifact (a competitor analysis, a risk register, a persona walkthrough) to their team with "I got this in 5 minutes" will adopt. The video must end with a visible, downloadable, forwardable output -- not just a terminal recording that fades to black.

**Distance from true today:** The spec focuses on the video as the deliverable. It does not address what happens AFTER the video. There is no "try it now" CTA with a pre-loaded topic, no artifact template the PM can immediately use, no bridge from "watched a video" to "ran a skill."

### Condition 3: A trusted peer must send the link, not a stranger or a tool vendor

Principal PMs at Microsoft adopt tools through peer networks, not through marketing materials. The video will convert if it arrives from a peer PM who says "I used this for my last service review and it saved me 4 hours." The video will NOT convert if it arrives from a GitHub repo, a mass email, or someone they do not know. Distribution strategy matters more than production quality.

**Distance from true today:** The spec addresses production (pipeline) and format (OneDrive links) but not distribution strategy. Who sends the link? With what message? After what trigger event?

**The most important condition is Condition 1** -- it is closest to being true today because the spec already emphasizes authentic, PM-centered demos. The gap is topic selection: choosing demo topics that match decisions Principal PMs are making right now.

---

## PHASE 5 -- AMEND

### 1. Quantified switching cost

- **Watch time:** 5-7 minutes per demo video x 2-3 videos to build conviction = 15-21 minutes
- **Install time:** 15-30 minutes (bootstrap + verify)
- **First skill run:** 10-15 minutes to run one discover or validate skill on a real topic
- **Total to first value:** ~45-65 minutes
- **Habit formation:** 2-4 weeks of intermittent use before Signal becomes default behavior
- **Calendar cost of the first click:** This is the real number. Getting 90 seconds of attention from a Principal PM who receives 100+ messages/day has an effective cost of ~$500 in equivalent advertising spend. The video must earn that click through subject line, sender identity, and timing.

### 2. Specific workaround failure mode the feature must address

**The live demo credibility failure.** When a sponsor runs a live demo and the AI generates a weak or irrelevant artifact (wrong competitors, shallow risk analysis, hallucinated personas), the target PM mentally files Signal as "not ready" and will not revisit it for 6-12 months. This failure mode is common because live demos cannot be rehearsed to perfection -- the AI output varies per run.

The automated video pipeline directly addresses this: every frame is curated, every artifact is the best run, every narration is polished. The video shows Signal at its actual capability ceiling, not at the variance floor of a live demo. This is the single strongest argument for the video pipeline over live demos.

### 3. Single condition most likely to tip teams away from inertia

**A peer PM shares a specific artifact (not a video) that saved them real time on a real decision.** The video is the awareness vehicle, but the tipping condition is: PM-A sends PM-B a risk register or persona walkthrough that PM-A actually used in their last service review, with the message "this took me 5 minutes instead of 3 meetings." The video explains what Signal is. The forwarded artifact proves it works.

This means the video pipeline is necessary but not sufficient. The pipeline must be paired with an artifact-sharing strategy: make it trivially easy for early adopters to export and forward the artifacts Signal produces, with attribution ("Generated by Signal /discover-risk in 4 minutes").

---

## Summary

| Dimension | Assessment |
|-----------|------------|
| Inertia threat | **HIGH** -- no forcing function, normalized pain, saturated attention |
| Switching cost | **LOW** -- under 1 hour to first value, but attention cost is extreme |
| Primary barrier | Not cost, not complexity -- **attention**. Getting the first click. |
| Video pipeline value | Solves the live-demo-credibility problem. Does not solve the attention problem or the peer-distribution problem. |
| Critical gap in spec | Topic selection strategy (Condition 1) and post-video bridge to action (Condition 2) are not addressed. Distribution through peer networks (Condition 3) is not addressed. |
| Recommendation | Build the pipeline (it solves a real problem: unreliable live demos). But invest equal effort in: (a) choosing demo topics that match live PM decisions, (b) adding a "try it now" bridge at the end of each video, and (c) seeding distribution through 3-5 trusted early-adopter PMs who send the links personally. |
