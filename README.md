# Git Work Analyzer

A CLI tool that analyzes a Git commit and reports which Playwright tests are impacted by that change.  
It supports both direct test file changes and indirect impacts caused by shared helper or fixture updates.

This tool is designed to help quickly identify which tests need to be run instead of executing the full test suite.

---
## Loom Video Link
https://www.loom.com/share/42d2296c3ae44cab813747434b2b4996

## Problem Statement

AI agents generate or modify Playwright tests frequently. Reviewing these changes can be difficult in large repositories with hundreds of tests and shared helpers.

Given a Git commit SHA, this tool identifies:
- Tests that were **added**, **modified** or **removed**
- Tests indirectly impacted due to changes in shared helper files

---

## Features

- Accepts a Git commit SHA as input
- Detects direct test file changes
- Tracks indirect test impact via helper dependencies
- Prints results to the CLI
- Automatically saves output in:
  - Human-readable CLI format
  - Structured JSON format

---

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/GAURAV0440/Git_work_analyzer.git
cd Git_work_analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## Usage:

Run the analyzer by providing a commit SHA and the path to the target repository:

python main.py --commit <COMMIT_SHA> --repo <PATH_TO_REPO>


## Example:

python main.py --commit d85f33a --repo ../flash-tests


### Output

## CLI Output

Printed directly in the terminal, grouped by test file and impact type.

Saved Files

All outputs are automatically saved to the output/ directory:


# output/
 ├── <commit>_cli.txt
 └── <commit>.json

 <commit>_cli.txt → Human-readable output

 <commit>.json → Structured output for automation


 ## Example JSON Output

{
  "commit": "d85f33a",
  "impacted_tests": [
    {
      "file": "tests/test-runs.spec.ts",
      "describe": "Test Runs Page",
      "test_name": "create and cancel a test run",
      "impact": "modified"
    }
  ]
}



