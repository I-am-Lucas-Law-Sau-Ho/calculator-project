# Calculator Project
A simple calculator project implemented in Python.

## Installation
```bash
git clone https://github.com/ysanne617/calculator-project.git
cd calculator-project
uv sync
```
## Usage
```python
from calculator import Calculator 
calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.subtract(5, 2))  # Output: 3
print(calc.multiply(4, 3))  # Output: 12
print(calc.divide(10, 2))  # Output: 5.0
```
## Tests
To run the tests, use the following command:
```bash
pytest tests/
```

## Workshop 10 Exercise: Generate a Release Notes Prompt

### Prerequisites

Before starting, ensure you have:
- VS Code with GitHub Copilot and Copilot Chat extensions installed
- This repository cloned locally
- Copilot Chat working
---

#### Task Description

1. Use the `/create-prompt` command in Copilot Chat to generate a prompt file that:
   - Analyzes git commits between two tags
   - Categorizes commits by type (feat, fix, docs, chore, etc.) following conventional commit format
   - Outputs the release notes as a markdown file

2. Save the generated prompt file to `.github/prompts/release-notes.prompt.md`

3. Review and revise the generated prompt file as needed.

4. Run the prompt to generate release notes between `v1.1.0` and `v1.3.0`

5. Review and verify the generated release notes. If the output is incorrect or incomplete, iterate by revising your prompt file and running again.

---

### Submission

Submit the following screenshots to Blackboard:

1. **Prompt file screenshot:** Show the saved `release-notes.prompt.md` file with its content visible

2. **Execution screenshot:** Show the prompt running with the agent executing git commands

3. **Output screenshot:** Show the generated release notes markdown file
