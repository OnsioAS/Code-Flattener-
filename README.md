# Code-Flattener-
Code Flattener for AI Analysis A utility tool that consolidates directory structures into single files formatted with XML tags, making codebases easier to analyze with Large Language Models.

Overview
Instead of tediously copying individual files when analyzing code with LLMs, this tool automatically traverses directories and creates a single consolidated file with path context preserved through XML tags.
Key Features

Recursively explores directory structures
Maintains file paths with XML-style tags
Automatically detects and skips binary files
Customizable ignore patterns for directories/files
Flexible output options (console or file)
Zero-dependency installation with uv

Getting Started
Requirements

Python 3.12+
uv (recommended for dependency-free execution)

Basic Usage
Run directly with uv without installing dependencies:
uv run flatten.py ./your_project_directory
Command Options
# Standard usage (outputs to console)
uv run flatten.py ./your_project_directory

# Save output to file
uv run flatten.py ./your_project_directory --output=flattened_code.txt

# Exclude specific directories
uv run flatten.py ./your_project_directory --ignore=node_modules,venv,.git
Output Format
<file path=src/main.py>
def main():
    print("Hello World")
</file>

<file path=src/utils/helper.py>
def helper():
    return True
</file>
Using with AI Models

Generate the flattened codebase:
uv run flatten.py ./your_project_directory --output=codebase.txt

Upload or paste the contents into your preferred LLM
Ask analytical questions like:

"Find potential security issues in this codebase"
"Create documentation for this project"
"Suggest architectural improvements"



Technical Implementation
The tool uses:

typer for command-line interface
Native Python directory traversal
UTF-8 encoding handling
XML-style formatting for file context

Troubleshooting

Binary files: Automatically detected and skipped with warnings
Encoding issues: UTF-8 is used by default, problematic files are skipped
Large directories: Use ignore patterns and file output for better performance

Project Structure
flatten-dir-for-ai/
├── README.md
├── flatten.py
└── examples/
