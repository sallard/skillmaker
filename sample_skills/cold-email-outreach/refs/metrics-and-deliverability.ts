export const slug = 'metrics-and-deliverability'
export const triggers = {
  keywords: ['metrics', 'deliverability', 'open rate', 'reply rate', 'bounce', 'spf', 'dkim', 'dmarc', 'warm up', 'sending', 'infrastructure', 'benchmarks']
}
export const body = `
# Metrics, Benchmarks & Deliverability

---

## Weekly Metrics Diagnosis

Review these four metrics weekly, by segment. Do not use overall averages.

| Metric | What it diagnoses | Action if below threshold |
|---|---|---|
| Open rate | Subject line effectiveness | Rewrite subject lines if below 40% |
| Reply rate | Message resonance with this segment | Rewrite copy if below 1% with good opens |
| Contact-to-lead ratio | Targeting accuracy | Tighten list criteria and signal filters |
| Bounce rate | Data quality and list hygiene | Switch data provider if above 3% |

**Interpretation rules**:
- Good opens + low replies = the subject line works but the email body does not
- Low opens + any replies = subject line problem, not copy problem
- High opens + high replies + low contact-to-lead = copy and targeting are right, offer needs work
- High bounce rate = data provider issue, not a copy issue

**Iteration cadence**: Test one variable at a time. Subject line OR email body OR list segment. Never change two things in the same test.

---

## Deliverability Non-Negotiables

These are table stakes. Skip any one of them and your emails land in spam regardless of copy quality.

**Domain setup (do before sending a single email)**:
- Configure SPF on every sending domain
- Configure DKIM on every sending domain
- Configure DMARC on every sending domain
- Never use your primary company domain for cold outreach
- Buy secondary domains specifically for cold outreach (e.g., getcompanyname.com, trycompanyname.com)

**Inbox warm-up**:
- Warm up every new inbox for at least 30 days before sending real emails
- Use automated warm-up tools (Instantly handles this natively)
- Do not skip warm-up even if you are in a hurry, reputation damage takes weeks to recover

**Sending volume limits**:
- Maximum 30 emails per inbox per day
- Use multiple inboxes and rotate across them for higher volume
- Spread sends across the day, do not send 30 emails at 9am

**Ongoing hygiene**:
- Monitor bounce rate continuously, above 3% signals a data quality problem
- Remove bounces and unsubscribes immediately
- Do not re-send to contacts who have not opened after 3 touches

---

## Recommended Tool Stack

These tools were validated at scale by ColdIQ from 1 lead per 4,000 emails to $7M ARR:

| Tool | Role |
|---|---|
| Clay | Enrichment orchestration, pulls from multiple data sources, builds signal-based lists |
| Instantly | Sending infrastructure, inbox warm-up, domain rotation, volume throttling |
| Prospeo | Contact verification and data enrichment |
| Expandi | LinkedIn outreach automation (complement to email sequences) |
| Apify | Web scraping for custom signal detection |
| PredictLeads | Buying signal data (hiring, funding, tech changes) |
| FullEnrich | Waterfall enrichment for contact data |

**Stack principle**: Clay orchestrates everything. Instantly handles sending and deliverability. The other tools feed Clay with data.

---

## Scaling Without Breaking Deliverability

- Add new inboxes before you need more volume (warm-up takes 30 days)
- One domain per 2-3 inboxes maximum
- Rotate domains in your sequences so no single domain carries all volume
- If a domain's open rate drops suddenly, pause it immediately and investigate before continuing
- Never buy domain reputation back with higher volume, it makes it worse
`
