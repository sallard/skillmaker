import * as metricsRef from './refs/metrics-and-deliverability'
import * as tieringRef from './refs/account-tiering'
import * as linkedinAdsRef from './refs/linkedin-ads-integration'
import * as whatsappRef from './refs/whatsapp-outreach'

export const slug = 'cold-email-outreach'
export const title = 'Cold Email Outreach'
export const applies_to = ['sales', 'gmail']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'
export const triggers = ['cold email', 'outreach', 'reply rate', 'list building', 'buying signal', 'deliverability', 'email sequence', 'personalization']
export const token_budget = 450
export const refs = [tieringRef, metricsRef, linkedinAdsRef, whatsappRef]
export const body = `
# Cold Email Outreach

The only goal of a cold email is to get a reply. Not a sale. Not a demo booking. A reply. Optimize everything for that.

## Rules

- Start with 3 targeting segments: brand-engaged companies, lookalikes of your best clients, and intent-signal companies. These 3 give the highest first-campaign reply rate.
- Tier 1/2/3: Tier 1 = manual multichannel, Tier 2 = AI-personalized multichannel, Tier 3 = email at scale. See refs.
- Write the first 25-50 messages manually. This surfaces patterns and angles that scale. Automating before this means scaling assumptions, not proven approaches.
- Under 80 words, 4 lines maximum. Line 1: specific observation. Lines 2-3: connect to a concrete problem. Line 4: simple yes/no question.
- Lead with value before asking for anything. Build the first deliverable you would create for a new client and send it for free. Demonstrating competence gets more replies than claiming it.
- Reply to positive replies within 5 minutes. Speed determines close rate. AI reply agents (Instantly) can draft instantly with human review before send. Teams using this booked 30% more meetings.
- Use secondary sending domains only. Warm up every inbox 30+ days. Max 30 emails per inbox per day. Disable open tracking pixels.
- LinkedIn Ads before outreach increases reply rates 25-40%. Add when cold email is working and budget $3k+/month. See refs.
- Iterate by segment: open rate, reply rate, contact-to-lead, bounce rate each diagnose a different problem.

## Anti-patterns

- Mail-merge "personalization" with first name and company instead of a specific observation
- Opening with compliments instead of an observation about their specific situation
- Sending from your primary domain to save setup time
- Pitching product before establishing relevance to their situation
- Treating list-building as one-time setup instead of ongoing signal detection
- Measuring success by open rate alone. Opens without replies means the copy is not landing.

`
