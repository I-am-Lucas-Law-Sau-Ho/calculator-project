---
mode: agent
description: Generate release notes from git commits between two tags
---

# Release Notes Generator

Generate release notes for the repository by analyzing git commits between two specified tags.

## Instructions

1. Run the following git command to get all commits between the two tags:
   ```
   git log ${input:fromTag}...${input:toTag} --oneline --no-merges
   ```

2. Categorize each commit by its conventional commit type prefix:
   - **feat**: New features
   - **fix**: Bug fixes
   - **docs**: Documentation changes
   - **test**: Test additions or modifications
   - **refactor**: Code refactoring
   - **chore**: Maintenance tasks
   - **perf**: Performance improvements
   - **style**: Code style changes

3. Output the release notes as a markdown file with the following structure:

```markdown
# Release Notes: ${input:toTag}

## What's Changed

### New Features
- <list feat commits>

### Bug Fixes
- <list fix commits>

### Documentation
- <list docs commits>

### Tests
- <list test commits>

### Refactoring
- <list refactor commits>

### Other Changes
- <list chore/style/perf commits>

**Full Changelog**: ${input:fromTag}...${input:toTag}
```

4. Save the generated release notes to `release-notes-${input:toTag}.md` in the repository root.