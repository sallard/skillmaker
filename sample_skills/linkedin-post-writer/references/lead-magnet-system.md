# Lead Magnet Production System

Complete A-Z workflow for creating lead magnets that generate comments, DMs, and booked calls. Five prompts covering ideation → packaging → content creation → post writing → DM follow-up.

Run them in sequence. Each output feeds the next.

---

## Step 0 — Pre-Validation (Do This Before Ideating)

**The fastest lead magnet ideas are already in your LinkedIn analytics.**

Every post you publish is free market research. Your audience already told you what they want — you just need to read the data and double down on what's working.

**The 3-step pre-validation process:**

**Step 1 — Find your top-performing posts**
Export LinkedIn analytics CSV (or use Taplio to sort by views/likes/comments). Look at last 90 days. Identify top 10 posts. Tag existing lead magnet giveaway posts separately — you want net new ideas from organic content only.

**Step 2 — Filter for lead magnet potential (ALL THREE must be true)**
Not every high-engagement post is lead magnet material. Filter for posts that meet all three criteria:
1. **Tactical or actionable** — value = usefulness. If someone is giving you their email, they need to be able to do something with the asset.
2. **Within your core content pillars** — if a broad post goes viral but doesn't relate to what you want to be known for, don't build a lead magnet around it. It attracts the wrong audience.
3. **Significant engagement** — pre-validated demand signal

The pillar filter is the one people miss. A viral post outside your pillars = wrong audience = wasted lead magnet.

**Step 3 — Expand using first principles**
The question isn't "how do I make this longer." It's: **"How do I make this more useful? How do I make it easier to implement and get a result?"**

Three ways to expand a post into a lead magnet:
- More examples (show the thing in multiple contexts)
- More detailed/nuanced explanations (go deeper on the mechanism)
- More templates, prompts, and checklists (make it immediately actionable)

**For Sunnyvale specifically:**
Look at which posts get the most saves and comments from BD managers and agency founders. The topics that generate the most "can you share more on this?" comments = your first lead magnets. Pre-validation beats pure ideation every time.

**Taplio prompt for pre-validation:**
"Sort my last 90 days of posts by [likes / comments / saves]. Show me the top 10. Flag which ones are lead magnet giveaway posts vs. organic content."

---

## The 5-Step Workflow

```
Step 1: IDEATE — generate 3–5 lead magnet concepts
Step 2: PACKAGE — name it, format it, position it
Step 3: CREATE — build the actual asset
Step 4: POST — write the LinkedIn promotion post
Step 5: DM — follow up after delivery
```

---

## Prompt 1 — Ideation

Generates 3–5 lead magnet concepts from your ICP and pain points.

```
You are a B2B marketing strategist helping founders grow their presence and 
generate leads on LinkedIn.

Generate 3–5 irresistible lead magnet ideas that a B2B founder can offer on 
LinkedIn to attract their ideal clients and drive comments and engagement.

Inputs:
- ICP: [Insert detailed description]
- Top pain points: [Insert bullet points]
- Primary goals of ICP (make more money, save time, automate, grow faster): [Insert]
- Industry or niche: [Insert]

Requirements:
- Must be highly relevant to the ICP's pain points or desired outcomes
- Must feel instantly valuable — worth at least $50–$100 in perceived value
- Must be quick to consume and implement — ideally 5 to 30 minutes
- Must be easy for the founder to create (templates, swipe files, curated lists, AI tools)
- Bonus if the lead magnet includes or leverages AI

For each idea, output:
1. Title or concept
2. Format (checklist, swipe file, prompt pack, tool, calculator)
3. Why it's valuable (specific pain point it solves or result it delivers)
4. How fast/easy it is to use
5. Suggested LinkedIn hook/headline to drive engagement
```

**Sunnyvale lead magnet candidates (pre-ideated):**
- SignalScore sample profile of a real prospect they're already targeting (the product demo IS the lead magnet)
- "The 5 outreach angles that are actually getting replies from premium brand CMOs in 2026" (swipe file)
- "2-line cold email template validated across 100K+ messages" (template + rationale)
- "The 25-tool stack audit: what you're paying for vs. what you actually need" (calculator/checklist)
- "How I profiled 10 prospects in under 5 minutes using behavioral DISC" (walkthrough guide)

---

## Prompt 2 — Packaging

Takes your chosen concept and makes it feel irresistible.

```
You are a B2B growth strategist specializing in LinkedIn lead magnets for founders.

Context:
- I already have the core idea for a lead magnet
- My audience is [ICP description]
- Goal: package this so it feels irresistible, outcome-driven, and premium

Core lead magnet idea: [INSERT YOUR IDEA HERE]

Your task:

### 1. Compelling Name Options
Generate 10–15 lead magnet names that:
- Are outcome-focused (money, calls, growth, speed, simplicity)
- Use proven patterns (numbers, systems, playbooks, OS, blueprints, SOPs)
- Feel specific, premium, and "too good to ignore"
- Are suitable for LinkedIn founders (not hypey, but powerful)

### 2. Best Format Recommendation
Recommend the single best delivery format and explain why:
- Notion doc (default — maximizes perceived value, fast to consume, practical)
- Custom GPT (interactive, high engagement)
- Swipe file (fastest to create, easy to reference)
- Gamma doc (visual, professional)
- Short video walkthrough (high trust, effort signal)
- Miro board (complex systems/frameworks)

Choose the format that maximizes perceived value, is fast to consume, 
feels practical and actionable, and works well as a comment-to-get asset.

### 3. Transformation & Outcome
Clearly articulate:
- The before state of the reader
- The after state after using this lead magnet
- The specific result they should expect (calls booked, clarity, speed, simplicity, confidence)

### 4. Positioning Angle
Explain how this lead magnet should be positioned so it:
- Attracts the right founders
- Repels non-ideal people
- Feels like a "no-brainer" free asset
```

---

## Prompt 3 — Content Creation

Turns a transcript, notes, or raw content into a structured lead magnet asset.

```
I'm going to feed you content that I want to turn into a dense, actionable lead 
magnet asset.

The asset is going to be a Notion doc with multiple tabs — split the content into 
relevant chapters based on the natural flow of the source material. Create your own 
chapter structure.

Requirements:
- Include EVERYTHING from the source content
- Write from first-person POV
- Conversational tone, varying line lengths, bullets when needed, easy to read
- 100% of information from the source material only — do not add or invent
- Include placeholders for screenshots when the source alludes to a visual 
  ("here you can see...", "as you can see...", etc.)
- Each chapter should have a clear heading and a brief intro line

Source content: [PASTE TRANSCRIPT OR NOTES HERE]
```

---

## Prompt 4 — Viral Giveaway Post (Full Framework)

The complete prompt for writing a LinkedIn lead magnet promotion post. Use this version — it's more precise than a generic post prompt.

**The 6-part Viral Giveaway framework:**

| Section | Goal | Key rule |
|---|---|---|
| Hook | Get them to click "see more" | End with a colon (:). Specific number or result outperforms. |
| Big Promise | Explain the transformation | Specific + bold. Downplay the asset's value. Drop social proof here. |
| Reason Why | Explain why you're giving it away | Research-backed: explaining a reason increases compliance. Make it logical, not suspicious. |
| Offer Stack | Make it feel like a $997 product | List everything. Add dollar figures or numbers to individual items. Price anchor. |
| CTA | Tell them exactly what to do | Like + Comment keyword + Connect. Simple. No reinventing. |
| P.S. | Increase action probability | Handle #1 objection, drop social proof, create urgency, or tease a bonus. |

**Length sweet spot: 800–1,200 characters**

```
OBJECTIVE

Act as a world-class direct response copywriter with deep understanding of what 
content is getting distribution on LinkedIn right now.

Goal: write a Viral Giveaway LinkedIn post with the highest odds of generating 
high-quality leads.

CONTEXT

A Viral Giveaway post offers a free lead magnet in exchange for engagement. 
When someone comments, we send them a DM with a landing page link to get the asset. 
Their comment shows the post to their followers — keeps the flywheel spinning.

FRAMEWORK (follow exactly — 6 sections):

1/ HOOK
Goal: create a curiosity gap, get people to click "see more."
Execution: 2 short punchy paragraphs with a line break OR a 2–3 line paragraph 
under 140 characters.
Rules:
- Last sentence ALWAYS ends on ":"
- Hooks with big numbers or money figures outperform

2/ BIG PROMISE
Goal: briefly explain the big outcome or problem we're solving.
Rules:
- Short sentences and paragraphs
- No paragraph longer than 3 lines on mobile
- Use bullets or "…" to break up sentences
- Add social proof here if you have it

3/ REASON WHY
Goal: explain why you're giving this away.
Research shows: explaining the reason behind a request multiplies compliance.
Rules:
- Make it feel logical, not suspicious
- "Originally created for a paid product" works
- "Only sharing for the next 48 hours" creates urgency
- Same formatting as Big Promise

4/ OFFER STACK
Goal: make the free asset feel like an absolute no-brainer.
Execution: list out EVERYTHING people get, in bullets.
Rules:
- The more tangible each feature, the better
- Add numbers or dollar figures to items when possible ("5 email templates worth $500")
- Short sentences, bulleted list

5/ CTA
Goal: tell them exactly what to do.
Execution: short sentences, bulleted list.
Steps:
• Like the post
• Comment "[KEYWORD]"
• Connect with me if not already (so I can DM you)

6/ PS
Goal: increase action probability. Format: always start with "PS -"
Options:
- Social proof
- Handle the #1 objection
- Create urgency (48 hours only)
- Tease a bonus they didn't expect

STYLE
- Clear, concise, direct, yet conversational
- Short sentences and paragraphs (max 3 lines on mobile)
- Use bullets with "•" symbol (no markdown on LinkedIn)
- 800–1,200 characters total
- No emojis
- No em-dashes
- No hashtags, no links in body

INPUTS (use ONLY what is provided — do not invent claims):
- Target audience: [Insert]
- Lead magnet name: [Insert]
- Lead magnet format: [Insert]
- Core outcome / promise: [Insert]
- Pain points it solves: [Insert 3–6 bullets]
- What's included (specific deliverables): [Insert]
- Credibility proof: [Insert — results, testing, clients, usage]
- CTA keyword: [e.g. "SYSTEM", "PLAYBOOK", "PROFILE"]
- Why you're giving it away: [Insert — reason why section]
- Optional bonus / PS: [Insert if any]

OUTPUT: 3 variations of the post. Label each section clearly.
```

**Annotated example (study the structure):**

```
<Hook>
Yesterday I spent 6.5 hours creating 4 (massive) AI prompts to help you:

<Big Promise>
• Nail your newsletter value prop
• Brainstorm an A+ newsletter name
• Write all of your landing page copy
• And even mockup the landing page

In other words: All you need to launch a money-making niche newsletter in 2025.

<Reason Why>
Now, full transparency:
Originally, I created these prompts for a paid product I am working on.
But after testing them, I thought they were too good not to share them.
So just for the next 48 hours, I am sharing them for free.

<CTA>
Want access?
• Like this post
• Comment "newsletter"
I'll send it over via DMs ASAP.

<PS>
PS… if we are not connected yet, please send me a connection request so I can DM you.
```

---

## Prompt 5 — DM Follow-Up

The message sent immediately after delivering the lead magnet in DMs.

```
You are a B2B growth strategist and direct-response copywriter specializing 
in LinkedIn DMs.

Write one short, natural follow-up DM sent immediately after delivering a lead 
magnet. Goal: start a conversation that can naturally lead to a booked call. 
Never pitch. Never mention a call or demo.

Context:
- My offer: [describe your service or product]
- ICP: [who you serve]
- Core pain point my ICP is trying to solve: [main pain]
- Qualification criteria: [minimum requirements, deal size, activity level]
- Platform: LinkedIn DMs

Requirements:
- Must feel casual, human, and non-salesy
- Ask ONE qualifying question only
- Question should be easy to answer in one click or one short reply
- Use poll-style or multiple-choice format when possible
- The question should softly qualify based on your criteria
- Never mention a call, demo, or sales

Structure:
1. Short friendly acknowledgment
2. Confirmation the resource was sent
3. Transition line ("Quick question..." or "Doing a quick poll...")
4. ONE qualifying question with 3–5 answer options

Output: ONLY the DM message. Under 70 words. No explanations.
```

**Sunnyvale DM follow-up template (pre-written):**
```
Hey [Name] — here's the [resource name], hope it's useful.

Quick question while I have you — where does your prospecting 
actually break down right now?

a) Finding the right contacts
b) Research taking too long
c) Emails getting ignored
d) Not enough follow-up
e) Something else

Curious which one is the bottleneck for you.
```

---

## Lead Magnet Post — Swipe File

Four real examples showing the pattern in action. Study the structure, not the content.

### Example 1 — Credibility + Mechanism + Deliverables
```
I've sent over 20 million cold emails in the last 5 years.

And I finally found an AI that writes them better than I do.

[Pain agitation: calls out 3 specific ways every AI fails]

[Mechanism: explains what makes this different]

The custom Gem I created does this:
• Evaluates any cold email draft in seconds
• Rewrites automatically to 70 words or less
• Generates infinite testing variations instantly
• Catches spam triggers pre-send

Comment "GEM" + connect if we're not linked yet.
I'll send it to your DMs.

PS: We're a certified Smartlead expert. This prompt books 
400-600 appointments every month without fail.
```
**Pattern**: Big credential → common problem → mechanism → specific deliverables → 2-step CTA → social proof P.S.

### Example 2 — Contrarian + Broken Rules + System
```
I spent 6 hours compressing our internal playbook that helped us generate 
15,500 leads and $30M+ in pipeline into a workshop.

The next day, multiple agency owners asked me for the slide deck.

[Broken rules: calls out 6 things everyone does wrong]

So I built a complete breakdown of what actually works:
1. List Building
2. Deliverability
3. Personalization
4. Follow-Up Strategy
5. Metrics That Matter
6. Booking Calls

Comment "deck" + send a connection request if we're not connected.
```
**Pattern**: Specific result → social proof → broken rules list → system list → 2-step CTA

### Example 3 — Algorithm change + Lead magnet as only solution
```
I generated 376,216 impressions in 20 days.

All using these 5 Claude prompts (free).

[Algorithm change → why lead magnets are the only solution now]

So I'm giving away the exact 5 AI prompts I use to book calls:

1. Ideate lead magnets your audience actually wants
2. Name and package them so they stand out
3. Create the content inside
4. Write high-converting giveaway posts
5. Build DM sequences that convert hand-raisers into calls

Comment "MAGNET" + connect with me (so I can DM you).

PS: These are the exact prompts I use for my ghostwriting clients 
generating 6-7 figures from LinkedIn.
```
**Pattern**: Specific metric → free resource → reason why → numbered deliverables → 2-step CTA → P.S.

### Example 4 — Trend-jacking + Utility
```
Claude's new AI agent is overpowered.

This could save LinkedIn creators 10+ hours per week.

[What the tool does — 5 bullets]

It JUST launched. So I made a 20+ page guide showing how to use it 
to speed up content creation 2-3x.

Inside:
Workflow 1: Transform interview transcripts into 30+ LinkedIn posts
Workflow 2: Organize content folders in minutes
Workflow 3: Batch create branded presentations from raw notes
[+ 2 more]

Comment "COWORK" + send connection request.
```
**Pattern**: Breaking news hook → what it does → urgency (just launched) → specific workflows → 2-step CTA

---

## Lead Magnet Naming Formula

**Formula**: `[Desired Outcome] + [Topic] + [Container Word]`

**Container words** that make assets feel like a product (not just a document):
Kit, Prompt, Blueprint, Template, Playbook, Roadmap, Swipe File, Launchpad, Crash Course, Starter Pack, System, OS, Checklist, Toolkit

**Name rules:**
- 3–5 words max
- Outcome or benefit-driven — quantify when possible
- Should feel like a tangible product, not a vague guide
- Half the options should follow the exact formula above

**Real examples:**
- "Million-Dollar Sales Page AI Prompt"
- "The Infinite Newsletter Idea Generator"
- "The 6-Figure Newsletter Starter Pack"

**Sunnyvale name candidates:**
- "The 25-Second Prospect Profile System"
- "The Give-Before-Ask Outreach Playbook"
- "The 2-Line Cold Email Blueprint"
- "The BD Manager's Behavioral Profiling Toolkit"
- "The Agency New Business Starter Pack"

---

## Prompt 6 — Lead Magnet Name Generator

Generates 20 name options for any lead magnet concept.

```
I know you're a seasoned internet marketer and digital copywriter. I need your 
help coming up with name ideas for a lead magnet I'm building.

Context:
- My goal: help [target audience] [solve specific problem/achieve specific outcome] 
  by giving them [what's inside the lead magnet].
- So they can: [achieve desired outcomes].

Guidelines (keep these in mind throughout):
- Name should be 3–5 words max
- Should be outcome- or benefit-driven (quantify if possible)
- All variations should end with a container word that makes it feel like a product
  (blueprint, playbook, crash course, toolkit, starter pack, prompt, system, etc.)
- Half the variations should follow this exact formula:
  Desired Outcome + Topic/Niche + Container Word
  Example: "The Instant Trust Newsletter Blueprint"
- Other half: creative freedom on structure

Generate 20 potential names.
```

---

## Prompt 7 — Lead Magnet Mockup Generator

Creates a professional product mockup image that makes the lead magnet feel like a real, premium product. Use after naming — feed the chosen name in here.

```
Create a professional product mockup for a digital lead magnet that looks like 
a premium, tangible product.

Lead Magnet Details:
- Title: [YOUR TITLE — 2–5 words max on the cover]
- Subtitle/Description: [5–10 words max]
- Target Audience: [WHO IT'S FOR]
- Main Benefit/Promise: [KEY VALUE PROPOSITION]

Visual Style:
- Primary Colors: [e.g., deep blue, white, gold]
- Secondary Colors: [accent colors]
- Style: [modern, minimalist, bold, professional]
- Mood: [premium, authoritative, approachable]

Product Format (choose one):
Book cover / Product box / Course package / Digital bundle box / Report folder

Text Hierarchy (FOLLOW EXACTLY — less is more):
1. Main Title: [2–5 words] — largest, most prominent
2. Subtitle/Promise: [5–10 words] — secondary prominence
3. Author/Creator: [Name only] — smaller, professional
4. Optional Descriptor: [1–3 words] — tiny text like "Blueprint" or "Toolkit"

Text Restrictions:
- NO long descriptions or bullet points on the cover
- NO marketing copy or lengthy explanations
- Maximum 20 words total across ALL text elements
- Each element clearly separated and distinct

Requirements:
- Looks like a physical, premium product
- Professional typography with clear visual hierarchy
- Clean, uncluttered, plenty of white space
- Subtle shadows and depth for realism
- 1–2 minimal icons or visual elements max
- Optimized for landing page hero sections

Technical:
- High resolution, suitable for web display
- Aspect ratio: 1:1 for social, 3:4 for landing page hero

Style inspiration: Modern product packaging, premium course materials, 
professional book covers.
```

---

## Lead Magnet Landing Page — 7 Rules

Once the lead magnet is built and named, the landing page is what converts visitors to subscribers. These are the rules for high-converting lead magnet landing pages:

1. **Only 1 CTA** — remove every other potential distraction, link, or navigation
2. **Outcome-focused headline** — lead with transformation, not description
3. **Compelling lead magnet name** — use the naming formula above
4. **Opt-in box above the fold** — never make them scroll to sign up
5. **Tangible social proof** — specific numbers, not vague testimonials
6. **Address objections upfront** — what's the #1 reason someone wouldn't sign up? Handle it.
7. **Mockup image** — makes the asset feel like a real product, not a PDF

**AEO bonus (for AI search visibility):**
- Add an FAQ section (40% higher AI citation rate)
- Use H1→H2→H3 heading hierarchy (2.8× more likely to be cited in AI answers)
- Write specific, factual, quotable claims — vague positioning gives AI nothing to extract

---

- **First line = the only thing that determines if they keep reading.** Mobile preview shows ~100 chars. Make it count.
- **Deliverables list = specific, not vague.** "The exact DM script that books 30+ meetings/month" not "DM templates."
- **Credibility must be real.** Never invent numbers, clients, or results. Proof without exaggeration.
- **2-step CTA always**: (1) comment keyword + (2) connect if not linked. Both steps required for DM delivery.
- **P.S. is optional but powerful**: add urgency, a bonus, or one more credibility signal.
- **No em-dashes, no hashtags, no links in body, no emojis in hook.**
- **One idea per post.** Resist the urge to mention multiple lead magnets.

---

## Lead Magnet Campaign Performance Benchmarks

Track these metrics and use them to diagnose where the funnel is leaking.

| Funnel Stage | Metric | Target |
|---|---|---|
| Post Performance | Engagement rate (likes + comments / impressions) | 5%+ |
| Lead Magnet Conversion | Opt-ins or DMs / Comments | 60–70% |
| DM to Call | Booked calls / DMs sent | 10–20% |
| Overall ROI | Clients closed / Total comments | 1–5% |

**Optimization triggers:**
- Engagement rate below 5% → fix the hook (test 3 new variants next post)
- Opt-in rate below 60% → fix perceived value of the asset (naming formula, mockup image, specificity of deliverables)
- DM-to-call below 10% → fix the qualifying question in the DM (Prompt 5) or the ICP targeting
- Overall ROI below 1% → ICP mismatch — the people commenting aren't the people who buy

**Refresh cadence:**
- Test new hooks weekly
- Refresh visuals every 2–3 posts
- Update lead magnet content quarterly
- Build a new lead magnet monthly once the system is running

---

## Direct Response Principles for Lead Magnet Posts

**The 40-40-20 Rule**: 40% audience + 40% offer + 20% copy. Most people spend 80% on copy. Get the audience and offer right first.

**Awareness-level matching**: Lead magnets speak to "problem aware" and "solution aware" readers. Don't write for "most aware" (ready to buy) — they'll find the CTA themselves. Don't write for "unaware" — they won't comment. Target the middle.

**5 emotions hierarchy**: Great lead magnet posts hit at least 3. Fear (being left behind), Greed (the specific result they get), Anger (what's currently broken), Pride (who they become), Guilt (what they should already be doing). Weave them — don't announce them.

**Cognitive load**: Prospects don't read. They scan. Every line should make them want to read the next. Lead with the outcome, not the mechanism. If a sentence doesn't earn the next sentence, cut it.

**Specific beats generic**: "The exact DM script that booked 1,600 meetings in 12 months" beats "DM templates." "47-word email" beats "short email." The brain processes specificity as evidence; vague claims get filtered as marketing.

---

## Extended Swipe File — Additional Patterns

**Pattern: Arsenal / Resource Drop**
```
After [X hours/years] of [specific work], I finally built [the thing] 
most [authority figure] charge $[amount] to develop.

(and I probably shouldn't be giving this away for free)

Here's what you get:
→ [Specific deliverable 1]
→ [Specific deliverable 2]
→ [Specific deliverable 3]
[3–5 more]

This complete [name] puts you [X time period] ahead of the competition.

Want [the thing]?
1. Connect with me
2. Comment "[KEYWORD]" below
(I'll DM you once we're connected)

PS: Repost for priority access
```
**Pattern**: Time investment → social proof → specific deliverables list → "ahead of competition" framing → 2-step CTA

**Pattern: Autonomous System / Revenue Claim**
```
I [achieved result] with [mechanism].
→ in [timeframe]

[Dismiss the complexity: "No [thing], no [thing], no [thing]."]

Just [simple explanation of the system].

Here's how it works:
→ [Step 1]
→ [Step 2]
→ [Step 3]

[The result in specific numbers]

Comment "[KEYWORD]" and I'll DM the full strategy.
(Must be connected)
```
**Pattern**: Bold claim → simplicity framing → numbered mechanism → specific results → one-step CTA

**Pattern: Inbound-Led-Outbound**
```
Day 1: [Outcome]
Day [X]: [Bigger outcome]

Without [common wrong method 1], [wrong method 2] or [wrong method 3].

Most [audience] struggle with [problem] because [root cause].

I've perfected a [system name] that combines:
→ [Component 1 with specific result]
→ [Component 2]
→ [Component 3]
→ [Component 4]

This system helped me:
• [Specific result 1]
• [Specific result 2]
• [Specific result 3]

[The best part/differentiator].

Want [the system]?
1. Connect with me
2. Comment "[KEYWORD]" below
```
**Pattern**: Day 1/Day X timeline hook → diagnosis of problem → system components → social proof numbers → 2-step CTA
