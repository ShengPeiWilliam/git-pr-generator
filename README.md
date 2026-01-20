# PR Description Generator

Transform your git commits into professional Pull Request descriptions automatically.

## Quick Start

### 1. Prepare Your Commits

```bash
git log --format=%s -n 5 > commits.txt
```

This creates a file with your last 5 commit messages (without hashes).

### 2. Generate PR Description

```bash
python scripts/main.py --from-file commits.txt
```

### 3. Check Output

The generated PR description is saved to `pr_description.md`:

```bash
cat pr_description.md
```

Copy the content to your GitHub Pull Request description.

## Output Format

The generator creates a structured PR description:

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

## Requirements

- Python 3.8+

## How It Works

1. **Parses commits** in conventional commit format (`type: description`)
2. **Categorizes** by type (feat, fix, docs, etc.)
3. **Generates** professional title and summary
4. **Lists** key features and changes

See `SKILL.md` for detailed guidelines.