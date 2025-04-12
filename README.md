# Code Flattener for AI Analysis

> A utility tool that consolidates directory structures into single files formatted with XML tags, making codebases easier to analyze with Large Language Models.

This tool automatically traverses directories and creates a single consolidated file with path context preserved through XML tags, eliminating the need for tedious manual copying of individual files when analyzing code with LLMs.

## Key Features

- Recursively explores directory structures
- Maintains file paths with XML-style tags
- Automatically detects and skips binary files
- Customizable ignore patterns for directories/files
- Flexible output options (console or file)
- Zero-dependency installation with `uv`

## Prerequisites

- Python (v3.12 or later)
- uv (recommended for zero-install usage)

## Usage

### Quick Start with uv

The script specifies its dependencies at the top of the file, so you can run it directly with uv without installing anything:

```bash
uv run flatten.py ./your_project_directory
```

### Command Options

```bash
# Standard usage (outputs to console)
uv run flatten.py ./your_project_directory

# Save output to file
uv run flatten.py ./your_project_directory --output=flattened_code.txt

# Exclude specific directories
uv run flatten.py ./your_project_directory --ignore=node_modules,venv,.git
```

### Output Format

```xml
<file path=src/main.py>
def main():
    print("Hello World")
</file>

<file path=src/utils/helper.py>
def helper():
    return True
</file>
```

## Using with AI Models

1. Generate the flattened codebase:
```bash
uv run flatten.py ./your_project_directory --output=codebase.txt
```

2. Upload or paste the contents into your preferred LLM

3. Ask analytical questions like:
   - "Find potential security issues in this codebase"
   - "Create documentation for this project"
   - "Suggest architectural improvements"

## Project Structure

```
flatten-dir-for-ai/
├── README.md          # Project documentation
├── flatten.py         # Main script with embedded dependencies
└── examples/          # Example usage and outputs
```

## Technical Implementation

The tool uses:
- `typer` for command-line interface (auto-installed via uv)
- Native Python directory traversal
- UTF-8 encoding handling
- XML-style formatting for file context

## Troubleshooting

1. **Binary Files**
   - Automatically detected and skipped with warnings
   - Warning message displayed

2. **Encoding Issues**
   - Files are read as UTF-8
   - Non-text files are gracefully skipped

3. **Large Directories**
   - Use ignore patterns for `node_modules`, `venv`, etc.
   - Output to file instead of console for better performance

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Resources

- [UV Documentation](https://github.com/astral-sh/uv)
- [Typer Documentation](https://typer.tiangolo.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/guides/text-generation)
- [Claude Documentation](https://docs.anthropic.com/claude/docs)
