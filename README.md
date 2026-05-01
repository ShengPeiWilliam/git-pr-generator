# PR Description Generator

A CLI that turns Git commits into structured PR descriptions, built as 
an exercise in applying agent skill frameworks to personal workflow 
automation.

By defining the agent's behavior in a single `SKILL.md` file rather than 
writing prompts inline, the tool stays minimal — under 100 lines of 
Python — while keeping the prompt logic version-controlled and 
human-readable. PR description writing was a recurring personal task, 
making it a natural first target for this design pattern.

## Motivation

Agent skill frameworks let a single `SKILL.md` file define reusable agent 
behaviors and reduce token overhead significantly. Writing PR descriptions 
is something I do regularly, so it felt like a natural first task to 
automate with this approach.

## Design Decisions

### Why conventional commits?

The tool assumes commits follow the `type: description` format (feat, 
fix, docs, etc.). This constraint is intentional: if commits are already 
well-structured, the PR description is just a reorganization of existing 
information, not a generation problem.

### Why file-based input?

Instead of reading git history directly, the tool takes a text file of 
commit messages. This keeps the tool decoupled from any specific git 
workflow and makes it easy to filter or edit commits before generating.

## Usage

```bash
git log --format=%s -n 5 > commits.txt
python scripts/main.py --from-file commits.txt
```

The output is saved to `pr_description.md` with a structured title and 
summary organized by commit type.

## Reflections & Next Steps

The tool works well when commits follow conventional format, which is 
also where it gains most of its value: it incentivizes writing better 
commit messages upfront, since the downstream automation depends on 
them. The breakdown happens when commits are vague — at which point 
the right fix is upstream (better commit hygiene), not downstream 
(smarter parsing).

Building this also surfaced what the agent skill pattern actually buys 
you: separation between prompt logic and code, which makes iteration 
faster than wrapping LLM calls in inline string templates.

Next steps:
- **LLM fallback**: use a language model to infer intent from messy commits when conventional format isn't present.
- **Multi-language commits**: current parsing assumes English commit messages; support for other languages would require either translation or language-specific parsers.
- **Integration**: a Git hook or GitHub Action that triggers the generator on PR creation would remove the manual `git log` step.

## Tools

**Language**: Python 3.8+  
**Pattern**: Agent skill framework (`SKILL.md` defines agent behavior)  
**Dependencies**: minimal — standard library only

## References

- [Conventional Commits](https://www.conventionalcommits.org/) — commit message format used for parsing and categorization.