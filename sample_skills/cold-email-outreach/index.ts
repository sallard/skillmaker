import * as metricsRef from './refs/metrics-and-deliverability'

export const slug = 'cold-email-outreach'
export const title = 'Cold Email Outreach'
export const applies_to = ['sales', 'gmail']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'
export const triggers = ['cold email', 'outreach', 'reply rate', 'list building', 'buying signal', 'deliverability', 'email sequence', 'personalization']
export const token_budget = 400
export const refs = [metricsRef]
export const body = `
# Cold Email Outreach

The only goal of a cold email is to get a reply. Not a sale. Not a demo booking. A reply. Optimize everything for that.

## Rules

- The list is the strategy. A mediocre email to the right prospect beats perfect copy sent broadly. Spend more time on list quality than on copy.
- Target with 3-5 buying signals: hiring patterns, tech stack gaps, funding events, website changes, job postings. Signal-based targeting gets 4.2% reply rate vs. 0.8% with generic firmographics.
- Write under 80 words, 4 lines maximum. Line 1: specific observation. Lines 2-3: connect to a concrete problem. Line 4: simple yes/no question. Cutting from 200+ words to 80 doubled reply rates.
- Never sell in the cold email. No pitch, no features, no pricing. Email earns a reply, reply earns a conversation, conversation earns the sale.
- Use secondary sending domains only. Never cold-email from your primary domain. One incident kills your business email.
- Warm up every inbox 30+ days before sending. Max 30 emails per inbox per day.
- Iterate by segment: open rate, reply rate, contact-to-lead, bounce rate. Each diagnoses a different problem. See refs for thresholds and deliverability setup.

## Anti-patterns

- Mail-merge "personalization" with first name and company instead of a specific observation
- Opening with compliments instead of an observation about their specific situation
- Sending from your primary domain to save setup time
- Pitching product before establishing relevance to their situation
- Treating list-building as one-time setup instead of ongoing signal detection
- Measuring success by open rate alone. Opens without replies means the copy is not landing.

## 4-Line Signal-Based Formula

Line 1: Specific observation about their situation
Lines 2-3: Connect observation to a concrete problem or opportunity
Line 4: Simple yes/no question

Result: 11% reply rate for a recruiting SaaS using this 4-sentence structure.
`
