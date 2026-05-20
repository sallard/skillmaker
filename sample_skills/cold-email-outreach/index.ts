import * as metricsRef from './refs/metrics-and-deliverability'
import * as tieringRef from './refs/account-tiering'

export const slug = 'cold-email-outreach'
export const title = 'Cold Email Outreach'
export const applies_to = ['sales', 'gmail']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'
export const triggers = ['cold email', 'outreach', 'reply rate', 'list building', 'buying signal', 'deliverability', 'email sequence', 'personalization']
export const token_budget = 450
export const refs = [tieringRef, metricsRef]
export const body = `
# Cold Email Outreach

The only goal of a cold email is to get a reply. Not a sale. Not a demo booking. A reply. Optimize everything for that.

## Rules

- Start with 3 targeting segments: brand-engaged companies, lookalikes of your best clients, and intent-signal companies. These 3 give the highest first-campaign reply rate.
- Tier accounts 1/2/3: Tier 1 (dream clients) gets manual multichannel, Tier 2 (good fits) gets AI-personalized multichannel, Tier 3 (broad fits) gets email at scale. See refs for depth.
- Write the first 25-50 messages manually. This surfaces patterns and angles that scale. Automating before this means scaling assumptions, not proven approaches.
- Under 80 words, 4 lines maximum. Line 1: specific observation. Lines 2-3: connect to a concrete problem. Line 4: simple yes/no question.
- Never sell in the cold email. Email earns a reply, reply earns a conversation, conversation earns the sale.
- Respond to positive replies within minutes. Route to Slack or your phone. Prospect interest peaks when they reply.
- Use secondary sending domains only. Warm up every inbox 30+ days. Max 30 emails per inbox per day.
- Iterate by segment: open rate, reply rate, contact-to-lead, bounce rate each diagnose a different problem.

## Anti-patterns

- Mail-merge "personalization" with first name and company instead of a specific observation
- Opening with compliments instead of an observation about their specific situation
- Sending from your primary domain to save setup time
- Pitching product before establishing relevance to their situation
- Treating list-building as one-time setup instead of ongoing signal detection
- Measuring success by open rate alone. Opens without replies means the copy is not landing.

## 4-Line Formula

Line 1: Specific observation about their situation
Lines 2-3: Connect to a concrete problem or opportunity
Line 4: Simple yes/no question

11% reply rate for a recruiting SaaS using this 4-sentence structure.
`
