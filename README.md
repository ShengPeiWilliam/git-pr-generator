# PR Description Generator
Turns git commits into structured PR descriptions automatically, reducing the time spent writing PR descriptions manually.

## Motivation
Agent skill frameworks let a single SKILL.md file define reusable agent behaviors and reduce token overhead significantly. Writing PR descriptions is something I do regularly, so it felt like a natural first task to automate with this approach.

## Design Decisions

**Why conventional commits?**

The tool assumes commits follow the `type: description` format (feat, fix, docs, etc.). This constraint is intentional: if commits are already well-structured, the PR description is just a reorganization of existing information, not a generation problem.

**Why file-based input?**

Instead of reading git history directly, the tool takes a text file of commit messages. This keeps the tool decoupled from any specific git workflow and makes it easy to filter or edit commits before generating.

## Architecture

Pass a text file of commit messages to the generator:
```bash
git log --format=%s -n 5 > commits.txt
python scripts/main.py --from-file commits.txt
```

The output is saved to `pr_description.md` with a structured title and summary organized by commit type.

## Reflections & Next Steps

The tool works well when commits follow conventional format. It breaks down when commit messages are vague or inconsistent.

Next steps:
- **LLM fallback**: use a language model to infer intent from messy commits when conventional format isn't present.

## Tools

Python 3.8+

## References

- [Conventional Commits](https://www.conventionalcommits.org/) — commit message format used for parsing and categorization.