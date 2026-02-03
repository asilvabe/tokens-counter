# tokens-counter

Token counter for PDF files using [tiktoken](https://github.com/openai/tiktoken).

## Installation

```bash
# Create the virtual environment (only the first time)
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate

# Install dependencies and the package
pip install -e .
```

## Usage

```bash
# Activate the venv if not already active
source .venv/bin/activate

# Basic token count
tokens-counter file.pdf

# With per-page breakdown
tokens-counter file.pdf -v

# Using a different encoding
tokens-counter file.pdf -e o200k_base
```

## Available encodings

| Encoding | Models |
|---|---|
| `cl100k_base` (default) | GPT-4, GPT-3.5-turbo |
| `o200k_base` | GPT-4o, GPT-4o-mini |

## Example output

```
File    : ses-dg.pdf
Size    : 11.25 MB
Encoding: cl100k_base
----------------------------------------
Pages   : 1273
Tokens  : 535,794
Time    : 2.22s
```

With `-v`, a per-page breakdown is appended:

```
----------------------------------------
Tokens per page:
  Page    1:       31 tokens
  Page    2:      144 tokens
  Page    3:      471 tokens
  ...
```

## Notes

- Supports large files (tested with 11+ MB PDFs) by extracting text page by page without loading the full document into memory.
- Token count is an approximation in the context of an OpenAI model: images, tables, and special PDF formatting are not considered.
