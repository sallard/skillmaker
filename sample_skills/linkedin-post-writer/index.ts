export const slug = 'linkedin-post-writer'
export const title = 'LinkedIn Post Writer'
export const applies_to = ['linkedin_writing', 'sales', 'topic_posts']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'for_generating'
export const covers = ['linkedin', 'post', 'writing', 'hook', 'lead magnet', 'carousel', 'engagement', 'draft']
export const use_when = 'Use when the user asks to write, draft, create, or generate a LinkedIn post, even if they just say "write a post about X." Also trigger when the user asks to build a lead magnet, write a comment-gated post, ideate a lead magnet concept, or write a DM follow-up sequence.'
export const body = `
# LinkedIn Post Writer

Writes LinkedIn posts for any B2B founder, executive, or expert. Adapt voice to the user's context: founder/builder (product decisions, build-in-public), executive/strategic (industry insight, leadership), or practitioner/tactical (how-to, frameworks, systems).

Ask if unclear: "What's your role and what does your ICP care about most?"

---

## Tone of Voice

Match tone to the user's voice and ICP. Ask if unclear: "How would you describe your current tone on LinkedIn, or what tone do you want to aim for?"

Default guidance:
- Hook = an analogy or contradiction that makes the reader think, not a generic statement
- Body = specific facts, numbers, and mechanisms, not vague claims
- Numbers close arguments, not opinions
- Close with a rhetorical question or clear CTA, never a moralizing verdict
- Confident but not arrogant. Direct but not aggressive.
- Never: jargon for show, naive enthusiasm, generic motivational lines, direct verdicts

---

## Output Format (Full Package)

Always deliver all six:
1. **Hook Analysis**: which hook formula used and why it fits
2. **Format Recommendation**: text / carousel / infographic with rationale
3. **The Post**: ready to copy-paste
4. **CTA Note**: what action it drives and why
5. **Char Count**: with target range flagged
6. **Image Prompt**: Midjourney/DALL-E prompt for a visual companion. Include concept rationale (why this image works for this post). Default aspect ratio: --ar 4:5 (1080x1350px portrait). Show the tension or absurdity visually, not literally.

---

## Step 1, Choose the Right Template

Read refs/templates to select from Templates A-E. Match based on:
- Template A (Comprehensive Breakdown): systems, stacks, industry deep-dives, 2500-2900 chars
- Template B (Listicle Framework): lessons, principles, observations, 2000-2500 chars
- Template C (Case Study / Before-After): client results, transformations, 2000-2500 chars
- Template D (Comment-Gated Lead Magnet): max engagement, resource giveaway, 1500-2000 chars
- Template E (Conversational Story): personal, leadership, vulnerability, 1800-2300 chars

---

## Step 2, Write the Hook

Read refs/hooks before writing. Hook must land in first 210 characters. First sentence under 12 words. No yes/no questions. No "I" as opener. No hashtags.

90% of post-writing time should go to the hook. The average reader insta-likes a strong hook and skims the body.

---

## Step 3, Body Rules

- Every line adds information: no filler emphasis lines
- Numbers close arguments: not "grew significantly" but "grew 73% in 6 weeks"
- Staircase rule: vary bullet length (short-long or long-short), no uniform-length lists
- "Gist not full recipe": give direction and structure, not the complete operating manual
- Parentheses as surprise: use for asides that add a reveal or a number, "(and it only took 2 hours)"

---

## Step 4, CTA

One CTA per post. Match friction to intent:
- Ready to buy: "Book a call", "Start free trial", "Apply now"
- Curious: "Comment [KEYWORD] and I'll DM you the resource", "Download the guide"
- Browsing: "Follow for more [topic]", "What's your experience with this?"

For lead magnets: always use comment-gate. "Comment [KEYWORD]" generates 3-5x more comments than a link.

---

## Character Count Targets

| Format | Range |
|---|---|
| Stories / Template E | 1800-2300 chars |
| Tech/system breakdowns / Template A | 2400-2900 chars |
| Carousel companion text | 800-900 chars |
| Comment-gated lead magnet (Template D) | 1200-1800 chars |

Under 800 chars: feels thin unless it is a deliberate one-liner or strong take.
Over 3000 chars: loses most readers unless structured with clear visual breaks.

---

## Anti-patterns

- Never start with "I" (algorithmic penalty + weak hook)
- Never end with a direct verdict ("So always do X") - end with a question
- Never use em-dashes: use comma + space instead
- Never use generic CTAs like "What do you think?" on a non-opinion post
- Never write a hook that everyone would agree with: no engagement if no friction
- Never explain the analogy: if you have to explain it, it doesn't work
`
