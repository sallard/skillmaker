export const slug = 'lead-magnet-system'
export const triggers = {
  keywords: ['lead magnet', 'comment gate', 'giveaway', 'resource', 'dm follow-up', 'ideation']
}
export const body = `
# Lead Magnet Production System

Complete A-Z workflow for creating lead magnets that generate comments, DMs, and booked calls. Five steps covering ideation, packaging, content creation, post writing, and DM follow-up.

Run in sequence. Each output feeds the next.

---

## Step 0, Pre-Validation (Do This Before Ideating)

The fastest lead magnet ideas are already in your LinkedIn analytics. Your audience told you what they want. Read the data and double down on what's working.

**The 3-step pre-validation process:**

**Step 1, Find your top-performing posts**
Export LinkedIn analytics CSV (or use Taplio/Shield to sort by views/likes/comments). Look at last 90 days. Identify top 10 posts. Tag existing lead magnet giveaway posts separately so you mine only organic content.

**Step 2, Filter for lead magnet potential (ALL THREE must be true)**
1. **Tactical or actionable**: value = usefulness. If someone is giving you their attention, they need to be able to do something with the asset.
2. **Within your core content pillars**: if a broad post goes viral but doesn't relate to what you want to be known for, don't build a lead magnet around it. It attracts the wrong audience.
3. **Significant engagement**: pre-validated demand signal (saves and "can you share more?" comments matter more than likes).

The pillar filter is the one people miss. A viral post outside your pillars = wrong audience = wasted lead magnet.

**Step 3, Expand using first principles**
The question isn't "how do I make this longer." It's: "How do I make this more useful? How do I make it easier to implement and get a result?"

Three ways to expand a post into a lead magnet:
- More examples (show the thing in multiple contexts relevant to your ICP)
- More detailed explanations (go deeper on the mechanism, not just the surface)
- More templates, prompts, and checklists (make it immediately actionable without your help)

Posts that generate "can you share more on this?" comments are your first lead magnets. Pre-validation beats pure ideation every time.

---

## Step 1, Ideation Prompt

Give Claude:
- Your top 5 posts by saves + comments (paste the text)
- Your ICP definition (role, company type, core problem)
- 2-3 content pillars

Ask: "Based on these posts and this ICP, what are the 5 most valuable lead magnets I could create? For each, suggest a format (checklist, template, playbook, swipe file, calculator), a comment-gate keyword, and a one-line value proposition."

---

## Step 2, Packaging Prompt

Once you've chosen a lead magnet concept:

"I'm creating a lead magnet titled [TITLE] for [ICP]. The core value is [outcome in one sentence]. Format: [checklist/template/playbook]. Create an outline with [5-7] sections. Each section should be immediately actionable. The reader should be able to implement section 1 within 30 minutes of reading it."

---

## Step 3, Content Creation Prompt

"Write the full content for [LEAD MAGNET TITLE]. Target reader: [ICP description]. Each section should include: the what (concept), the why (reason it matters), and the how (exact steps or template). Keep language direct and practitioner-level. Avoid generic advice, everything must be specific to [their industry/problem]."

---

## Step 4, Post Writing (Comment-Gate)

Use Template D from refs/templates. Key mechanics:
- Hook: bold claim or FOMO builder with a specific number
- Line 2: the dream outcome the resource delivers (make it feel premium with scale or specificity)
- Line 3 after "see more": re-hook that confirms the reader needs this
- Body: describe 3-5 things inside the resource without giving them away
- CTA: "Comment [KEYWORD] and I'll DM it to you."

The keyword should be memorable and tied to the value: "OUTREACH", "PIPELINE", "STACK", "SYSTEM", not "YES" or "SEND".

---

## Step 5, DM Follow-Up Sequence

**Immediate DM (automated or manual, within 5 minutes of comment)**:
"Hey [Name], here's the [resource name] you asked for: [link]. Let me know what you think!"

**Follow-up DM (48 hours later, only if no reply)**:
"Hey [Name], did you get a chance to look at [resource name]? Curious what [specific section] triggered for you given what you're working on."

**Booking DM (only if they reply positively)**:
"Glad it was useful. A few people who went through it had questions about [specific implementation step]. Happy to do a quick 20-min call if that would help. Here's my calendar: [link]"

Do not pitch on the first DM. The resource is the value delivery. The booking conversation is earned by the resource doing its job.
`
