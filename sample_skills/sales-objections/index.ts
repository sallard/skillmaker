import * as objectionCheatSheet from './refs/objection-cheat-sheet'

export const slug = 'sales-objections'
export const title = 'Sales Objection Handling'
export const applies_to = ['sales', 'gmail']
export const mode: 'for_generating' | 'for_understanding' | 'mixed' = 'mixed'
export const triggers = ['objection', 'too expensive', 'need to think', 'pushback', 'how to respond', 'follow up', 'objection handling']
export const token_budget = 380
export const refs = [objectionCheatSheet]
export const body = `
# Sales Objection Handling

Every objection is a request for clarity. The words on the surface and the meaning underneath are rarely the same thing. Respond to the meaning, not the words.

## Rules

- Decode before responding. Identify the underlying concern first.
- Never defend on price. "It's too expensive" means value isn't clear, not that the price is wrong. Reframe cost against time saved, revenue gained, or risk avoided.
- "I need to think about it" means not convinced yet, not undecided. Clarify what's missing and what changes if they wait versus act now.
- "We don't need this" means the pain isn't surfaced yet. Ask better questions to connect to their actual workflow problems.
- "Send me more info" means they're not clear yet, not that they want a PDF. Ask what specific information would help them decide.
- "We're already using another solution" means switching feels risky. Ask what they like and dislike about their current setup, then show exactly where you improve it.
- Trust is built with credibility, clarity, and consistency, not features. Share real use cases with teams like theirs.
- Questions late in the conversation signal engagement, not resistance. Slow down, answer clearly, let nothing feel rushed.

## Anti-patterns

- Defending on price instead of reframing the value
- Feature-dumping in response to "how is this different from the rest"
- Going quiet or over-explaining after a first "no" signal
- Treating "I need to think" as a closed door instead of an opening to clarify
- Sending a document instead of asking what information would actually help them decide
`
