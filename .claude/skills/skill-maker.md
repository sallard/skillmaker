---
name: skill-maker
description: Generate or update TypeScript kb skills from any content source (URL, PDF, raw text)
---

## What this skill does

Processes submitted content and produces TypeScript skill files following the kb-skill-authoring-spec format. New content is evaluated against existing skills first. If it adds no value, nothing is generated and the reason is explained.

## Supported content sources

- Blog or article URL (Firecrawl)
- YouTube URL (transcript via RapidAPI)
- LinkedIn post URL (Harvest API)
- Tweet / X post URL (Firecrawl)
- Local PDF file path
- Pasted raw text

## Instructions

### Step 1: Identify the input

Check if the user provided a URL, PDF path, or raw text in the same message.
If nothing was provided, ask: "What content would you like to process? Provide a URL (blog, YouTube, tweet, LinkedIn post), a path to a PDF file, or paste the raw text."

### Step 2: Confirm skills directory

Check for SKILLS_DIR in the environment. Default: `supabase/functions/_shared/chat/kb/skills`.
Tell the user which path will be used.

### Step 3: Run the CLI

For a URL or raw text:
```bash
skillmaker process "<source>" --skills-dir "<skills_dir>"
```

For a PDF:
```bash
skillmaker process --file "<path_to_pdf>" --skills-dir "<skills_dir>"
```

### Step 4: Present the result

**If the output says "does not add value":**
Tell the user the reason and stop. No files to generate.

**If value is added:**
Show clearly:
- Action taken (create new skill / update existing)
- Which existing skills are affected
- Key insights extracted
- The generated slug and any ref slugs
- The full pasteable bundle

### Step 5: Ask before writing

Ask: "Should I write these files to disk at `<skills_dir>`? (yes/no)"

**If yes** - run with --write:
```bash
skillmaker process "<source>" --skills-dir "<skills_dir>" --write
```
Confirm the paths of all written files.

**If no** - show the bundle only for manual application.

### Step 6: Remind about manual wiring

After writing, always remind:
"After tests pass, add to `kb/index.ts`:
```
import * as <camelSlug> from './skills/<slug>/index.ts'
SKILLS.push(<camelSlug> as Skill)
```
And update the §11 inventory table in the spec."
