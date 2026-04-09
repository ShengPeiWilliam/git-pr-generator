# PR Description Generator
Turns git commits into structured PR descriptions by parsing conventional commit messages and organizing them by type.

## Motivation
Writing PR descriptions manually is repetitive, especially when commits already contain the information. This tool parses conventional commits and generates structured PR descriptions automatically.

## Design Decisions

**Why conventional commits?**

The tool assumes commits follow the `type: description` format (feat, fix, docs, etc.). This constraint is intentional: if commits are already well-structured, the PR description is just a reorganization of existing information, not a generation problem.

**Why file-based input?**

Instead of reading git history directly, the tool takes a text file of commit messages. This keeps the tool decoupled from any specific git workflow and makes it easy to filter or edit commits before generating.

## Usage
```bash
git log --format=%s -n 5 > commits.txt
python scripts/main.py --from-file commits.txt
cat pr_description.md
```

## Output Format
```markdown
Title:
feat: add feature

Description:
## Summary
Add new feature with related improvements.

## Key Features
- Add feature
- Bug fix
- Update documentation
```

## Reflections & Next Steps

The current approach works well for repos with disciplined commit hygiene. It breaks down when commits are vague ("fix stuff") or don't follow conventional format.

Next steps:
- **LLM fallback**: use a language model to infer intent from messy commits when conventional format isn't present.
- **Git integration**: read from git history directly with optional filtering by branch, date range, or author.
- **Template support**: let users define custom PR templates to match their team's format.

## Tools

Python 3.8+

## References

- [Conventional Commits](https://www.conventionalcommits.org/) — commit message format used for parsing and categorization.