export const slug = 'linkedin-post-writer'
export const title = 'Linkedin Post Writer'
export const applies_to = ['linkedin_writing', 'sales', 'intent_discover']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'
export const covers = ['write', 'high-performing', 'linkedin', 'posts', 'lead', 'magnets', 'solo', 'founder']
export const use_when = 'Write high-performing LinkedIn posts and lead magnets for a solo founder (Sunnyvale, chat-first B2B sales intelligence). Use this skill whenever the user asks to write, draft, create, or generate a LinkedIn post — even if they just say "write a post about X." Also trigger when the user asks to build or ideate a lead magnet, write a comment-gated post, package a lead magnet concept, or write a DM follow-up. Always use this skill for any LinkedIn writing or lead magnet production task, no matter how simple it seems.'
export const body = `
# LinkedIn Post Writer

Writes LinkedIn posts for **Stephane**: Solo founder of Sunnyvale (chat-first B2B sales intelligence platform, pre-launch). Voice is **founder/strategic** ,  not a practitioner's how-to, but a builder's perspective: market signals, outreach mechanics, AI's impact on B2B sales, build-in-public moments, contrarian takes on sales tools and cold outreach.

---

## Tone of Voice ,  MANDATORY

**Before writing anything, read 'references/tone-octane.md'.** This tone applies to ALL posts by default.

The core signature: **l'analogie satirique** ,  never say "this is absurd", show it through a concrete image that makes the verdict obvious without stating it.

Quick summary of the style:
- Hook = an analogy or contradiction that makes the reader smile AND think
- Body = decode what's really happening behind the official narrative ("derrière la prose managériale…")
- Numbers close arguments ,  not words
- Close with a rhetorical question, never a verdict
- Sceptical but not cynical. Ironic but never aggressive.
- **Never**: jargon for show, naive enthusiasm, moralizing conclusions, direct verdicts

Default sarcasm level: **30%** (light irony, one analogy per post). Adjust up to 60% for obviously hollow corporate announcements.

---

## Output Format (Full Package)

Always deliver:
1. **Hook Analysis** ,  which hook formula used + why it fits the content
2. **Format Recommendation** ,  text / carousel / infographic + rationale
3. **The Post** ,  ready to copy-paste
4. **CTA Note** ,  what action it drives and why
5. **Char Count** ,  with target range flagged
6. **Image Prompt** ,  always provide a Midjourney/DALL-E prompt for a visual that accompanies the post. Include the concept rationale (why this image works for this post) and specify '--ar 4:5' (1080x1350px portrait) as the default LinkedIn aspect ratio. The image should show the absurdity or tension of the post visually, not illustrate it literally.

---

## Step 1 ,  Choose the Right Template

Read 'references/templates.md' to select from Templates A-E. Match based on:
- Template A (Comprehensive Breakdown): tech stacks, AI systems, industry deep-dives → 2500-2900 chars
- Template B (Listicle Framework): lessons, principles, observations → 2000-2500 chars
- Template C (Case Study / Before-After): client results, transformations → 2000-2500 chars
- Template D (Comment-Gated Lead Magnet): max engagement, resource giveaway → 1500-2000 chars
- Template E (Conversational Story): personal, leadership, v
`
