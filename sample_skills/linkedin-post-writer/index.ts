import * as hooksRef from './refs/hooks'
import * as templatesRef from './refs/templates'
import * as leadMagnetRef from './refs/lead-magnet-system'
import * as engagementRef from './refs/engagement-data'

export const slug = 'linkedin-post-writer'
export const title = 'LinkedIn Post Writer'
export const applies_to = ['sales', 'topic_posts']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'for_generating'
export const triggers = ['write a post', 'linkedin post', 'draft a post', 'hook', 'lead magnet', 'carousel', 'post template', 'linkedin writing']
export const token_budget = 400
export const refs = [hooksRef, templatesRef, leadMagnetRef, engagementRef]
export const body = `
# LinkedIn Post Writer

Writes LinkedIn posts for any B2B founder, executive, or expert. Adapt voice: founder/builder (build-in-public, product decisions), executive/strategic (industry insight), practitioner/tactical (how-to, frameworks).

Ask if unclear: "What's your role and what does your ICP care about most?"

## Rules

- Always deliver all six: Hook Analysis, Format Recommendation, The Post, CTA Note, Char Count, Image Prompt.
- Read refs/templates before writing. Choose template A-E based on post type and length target.
- Read refs/hooks before writing the hook. 90% of writing time goes to the hook.
- Hook must land in first 210 chars. First sentence under 12 words. No "I" opener. No hashtags. No yes/no questions.
- Use the 2-line hook: Line 1 = bold claim or curiosity gap. Line 2 = sub-hook that addresses the reader's first objection before the "see more" fold.
- Every body line adds information. Numbers close arguments, not opinions. "Grew 73% in 6 weeks", not "grew significantly".
- One CTA per post. Match friction to intent: "Book a call" (ready to buy), "Comment [KEYWORD]" (curious), "Follow for more" (browsing).
- Image prompt for every post. Default format: --ar 4:5 (1080x1350px). Show tension or absurdity visually, not literally.

## Anti-patterns

- Never start with "I", algorithmic penalty and weak hook.
- Never end with a moralizing verdict, end with a question or clear CTA.
- Never use em dashes in post copy, use comma + space.
- Never write a hook everyone agrees with. No friction = no engagement.
- Never explain an analogy. If it needs explaining, it does not work.
- Generic CTAs like "What do you think?" on non-opinion posts.
`
