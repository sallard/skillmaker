import * as contentDiscoveryRef from './refs/content-discovery'
import * as icpRef from './refs/icp-and-pillars'
import * as calendarRef from './refs/calendar-templates'

export const slug = 'linkedin-content-strategy'
export const title = 'LinkedIn Content Strategy'
export const applies_to = ['sales', 'topic_posts', 'calendar']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'
export const triggers = ['content strategy', 'content calendar', 'what to post', 'posting schedule', 'content pillars', 'linkedin growth', 'audience building', 'inbound leads']
export const token_budget = 400
export const refs = [contentDiscoveryRef, icpRef, calendarRef]
export const body = `
# LinkedIn Content Strategy

Use LinkedIn as pipeline, not a branding channel. Content pre-answers sales objections. Prospects research you before replying to cold outreach.

**North star**: Every post pre-warms cold outreach. A prospect who has seen 5+ relevant posts before your email replies at 5x the rate.

## Rules

- Post 3x/week minimum at the same time every day. Repost 6-8h later to reach different-timezone audiences without penalizing reach.
- Pick 2-3 content pillars the algorithm can distribute reliably. Straying outside pillars resets distribution.
- 70/20/10 content split: value (educational/insight), build-in-public, conversion.
- The 3 compounding content types: milestones with mechanism, honest pivots and decisions, public screwups. Screwups consistently outperform.
- Profile converts more than posts. Most conversions happen on profile visits triggered by posts, not the post itself. Optimize headline and about section first.
- Before writing, find what works. Filter 3-5 niche accounts in Scripe by 300+ likes, last 3 months. Transpose proven formats to your niche, do not copy.
- Every like and comment is a pipeline signal. Extract engagers, filter for ICP, route to DM sequence referencing the post.
- LinkedIn's visually poor feed is the opportunity. Any quality infographic or video stops the scroll more than on any other B2B channel.

## Anti-patterns

- Posting without a defined ICP. Broad content attracts followers, not buyers.
- Measuring success by reach or impressions. Replies and DMs are revenue signals.
- Skipping profile optimization before posting at scale.
- Copying viral formats without transposing to your niche and adding your own social proof.
- Starting to post before defining which 3 content types fit your ICP.
`
