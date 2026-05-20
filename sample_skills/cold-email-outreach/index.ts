export const slug = 'cold-email-outreach'
export const title = 'Cold Email Outreach'
export const applies_to = ['sales', 'gmail']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'
export const covers = ['cold email', 'outreach', 'reply rate', 'list building', 'signals', 'deliverability', 'personalization', 'sequences']
export const use_when = 'Use when the user asks about cold email strategy, writing cold emails, improving reply rates, building prospect lists, cold outreach sequences, email deliverability, or signal-based personalization. Also trigger for questions about cold email metrics, sending infrastructure, or why cold emails are not getting replies.'
export const body = `
# Cold Email Outreach

Source: ColdIQ, scaled from 1 lead per 4,000 emails to $7M ARR. These are validated system principles, not generic advice.

**North star**: The only goal of a cold email is to get a reply. Not a sale. Not a demo booking. A reply. Optimize everything for that.

---

## Rules

- **The list is the strategy**: a mediocre email to the right prospect beats perfect copy sent broadly. Spend more time on list quality than on copy.
- **Target with 3-5 buying signals**: hiring patterns, tech stack gaps, funding events, website changes, job postings. Generic firmographic targeting (VP Sales, 50-200 employees) gets 0.8% reply rates. Signal-based targeting of the same role gets 4.2%.
- **Write under 80 words**: 4 lines maximum. Line 1: specific observation about their situation. Lines 2-3: connect observation to a concrete problem or opportunity. Line 4: a simple yes/no question. Reducing from 200+ words to under 80 doubled reply rates.
- **Never sell in the cold email**: no pitch, no features, no pricing. The email earns a reply. The reply earns a conversation. The conversation earns the sale.
- **Use secondary sending domains only**: never send cold email from your primary company domain. One deliverability incident on your main domain kills your business email.
- **Warm up every inbox for 30+ days** before sending any real emails. Keep volume under 30 emails per inbox per day.
- **Review metrics weekly**: open rate, reply rate, contact-to-lead ratio, bounce rate. Each metric diagnoses a different problem. See refs/metrics-and-deliverability for thresholds.
- **Iterate by segment**: review performance by subject line variant, list segment, and signal type, not just overall averages. Averages hide what's working.

---

## Anti-patterns

- "Personalization" that is just mail merge with first name and company name, not specific observations
- Starting with compliments ("I love what you're doing at [Company]") instead of a specific observation
- Sending from your primary domain to save setup time
- Writing emails that explain your product before establishing relevance to their specific situation
- Treating list-building as a one-time task rather than an ongoing signal-detection system
- Measuring success by open rate alone, opens without replies means the message is not landing

---

## Signal-Based Email Structure (4-Line Formula)

Line 1: Specific observation
"Saw you posted 4 SDR roles in the last 60 days and recently added Salesforce, but you don't have a conversation intelligence tool in your stack yet."

Line 2-3: Connect to problem or opportunity
"Most teams at that scale run into the same issue, reps are winging it on calls because there's no way to review what's working. That's usually where pipeline starts leaking."

Line 4: Simple yes/no question
"Would it be worth a quick conversation to see if we can help?"

Result: an 11% reply rate for a recruiting SaaS using a 4-sentence version of this structure.

---

## Buying Signals to Build Lists Around

- Hiring patterns (3+ SDR/AE postings in 60 days = scaling sales motion)
- Tech stack gaps (using X but missing Y = room for your tool)
- Funding events (new capital = new budget and new problems to solve)
- Website changes (new pricing page, new product launch, new market entry)
- Job description language (specific tools or methodologies mentioned = intent signals)
- LinkedIn activity (decision-maker posting about a problem you solve)

See refs/metrics-and-deliverability for sending infrastructure setup and performance benchmarks.
`
