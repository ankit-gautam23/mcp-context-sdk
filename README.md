# MCP Context SDK

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/mcp-context-sdk.svg)](https://pypi.org/project/mcp-context-sdk/)
[![Python Versions](https://img.shields.io/pypi/pyversions/mcp-context-sdk.svg)](https://pypi.org/project/mcp-context-sdk/)
[![CI Status](https://github.com/ankit-gautam23/mcp-context-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ankit-gautam23/mcp-context-sdk/actions)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://ankit-gautam23.github.io/mcp-context-sdk)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributors](https://img.shields.io/github/contributors/ankit-gautam23/mcp-context-sdk)](https://github.com/ankit-gautam23/mcp-context-sdk/graphs/contributors)

## Overview

The MCP Context SDK is a modular, production-ready Python SDK that enables AI agents, models, and tools to work with structured context schemas. It provides a standardized way to handle context in AI applications, making it easier to build, validate, and share context-aware AI systems.

## Features

- 🎯 **Dynamic Context Construction**: Build and validate context dynamically using JSON schemas
- 🔄 **Schema-to-Prompt Conversion**: Convert structured schemas into natural language prompts
- 🛠️ **Framework Integrations**: 
  - FastAPI for web applications
  - LangChain for AI workflows
  - AutoGen for multi-agent systems
  - CrewAI for team-based AI operations
  - LangGraph for complex AI workflows
  - OpenDevin for development automation
- 📝 **CLI Tools**: Command-line interface for schema management and context conversion
- 🎨 **Streamlit UI**: Interactive web interface for context editing and preview
- ✨ **Type Safety**: Full type hints and schema validations
- 📚 **Documentation**: Comprehensive guides and API references

## Installation

### From PyPI

```bash
pip install mcp-context-sdk
```

### From Source

```bash
# Clone the repository
git clone https://github.com/ankit-gautam23/mcp-context-sdk.git
cd mcp-context-sdk

# Install with Poetry
poetry install

# Or install with pip
pip install -e .
```

### Optional Dependencies

Install additional dependencies for specific integrations:

```bash
# FastAPI integration
pip install "mcp-context-sdk[fastapi]"

# All integrations
pip install "mcp-context-sdk[all]"
```

## Quick Start

### Basic Usage

```python
from mcp_context_sdk import ContextBuilder, SchemaLoader

# Load a schema
schema = SchemaLoader().load_schema("coding", version="v1")

# Create context
context = ContextBuilder(schema).build({
    "language": "python",
    "task_type": "development",
    "complexity": "intermediate"
})

# Convert to prompt
prompt = context.to_prompt()
```

### CLI Usage

List available schemas:
```bash
mcp list-schemas coding
```

Convert context to prompt:
```bash
mcp convert-context context.json coding --version v1
```

### Streamlit UI

Run the interactive UI:
```bash
streamlit run examples/streamlit_ui.py
```

## Documentation

- [User Guide](https://ankit-gautam23.github.io/mcp-context-sdk/user-guide)
- [API Reference](https://ankit-gautam23.github.io/mcp-context-sdk/api)
- [Examples](https://ankit-gautam23.github.io/mcp-context-sdk/examples)
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)

## Development

### Setup Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/ankit-gautam23/mcp-context-sdk.git
   cd mcp-context-sdk
   ```

2. Install development dependencies:
   ```bash
   poetry install
   ```

3. Run tests:
   ```bash
   poetry run pytest
   ```

4. Run linting:
   ```bash
   poetry run black .
   poetry run isort .
   poetry run flake8
   ```

### Project Structure

```
mcp-context-sdk/
├── mcp_context_sdk/      # Main package
│   ├── core/            # Core functionality
│   ├── integrations/    # Framework integrations
│   └── utils/           # Utility functions
├── docs/                # Documentation
├── examples/            # Example code
├── schemas/             # JSON schemas
└── tests/              # Test suite
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:
- How to submit issues
- How to submit pull requests
- Our development workflow
- Code style guidelines

## Security

Please report any security issues to [SECURITY.md](SECURITY.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use MCP Context SDK in your research, please cite:

```bibtex
@software{mcp_context_sdk,
  author = {Ankit Gautam},
  title = {MCP Context SDK},
  year = {2024},
  url = {https://github.com/ankit-gautam23/mcp-context-sdk}
}
```

## Contact

- GitHub Issues: [Create an issue](https://github.com/ankit-gautam23/mcp-context-sdk/issues)
- Email: ankit.gautam@example.com
- Twitter: [@your_twitter_handle]

## Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by various AI frameworks and context management systems 