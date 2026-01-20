---
name: pr-description-generator
description: Generate professional Pull Request titles and descriptions from git changes following conventional commits format.
---

# PR Description Generator

Transform your git changes into professional PR descriptions in seconds.

## When to Use

- Creating a Pull Request on GitHub
- Writing commit messages
- Documenting branch changes
- Preparing release notes

## Output Format
```markdown
Title:
<type>: <brief description>

Description:
## Summary
<what this PR does and why>

## Key Features
- Change #1
- Change #2
- Change #3
```

## Commit Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation
- **chore**: Config/tools/dependencies
- **refactor**: Code restructuring
- **test**: Adding tests

## Example

**Input**: Git commit history from feature branch
```
feat: add search functionality
feat: implement filter options
fix: resolve search result sorting bug
docs: update search API documentation
```

**Output**:
```markdown
Title:
feat: add search functionality with filters

Description:
## Summary
Implement comprehensive search feature with filtering and sorting capabilities

## Key Features
- Add full-text search across content
- Implement advanced filter options
- Fix sorting issues in search results
- Update API documentation for search endpoints
```

## Guidelines

### Title Rules

**Format: `<type>: <brief description>`**

This is the most important rule. Always follow this exact format:
- Start with type (feat, fix, docs, etc.)
- Add colon and space: `: `
- Follow with brief description
- Max 50 characters total
- Use imperative mood ("add" not "added")
- Lowercase after type
- No peri好od at end

**Good Examples:**
- `feat: add authentication system`
- `fix: resolve login validation bug`
- `docs: update API documentation`

**Bad Examples:**
- `add authentication system` (missing type)
- `feat: Added authentication` (wrong mood - should be "add")
- `Feat: add authentication` (wrong case - type should be lowercase)

### Description Rules

- **Summary**: 1-2 sentences explaining what and why
- **Key Features**: 2-5 bullet points of main changes
- Focus on value, not implementation details
- Skip trivial changes

## How to Use
```
Analyze my git commits and create a PR description
```
```
I have these commits: feat: add auth, fix: validation bug, docs: update README
Create a PR description
```
```
Generate PR text from my feature branch commits
```