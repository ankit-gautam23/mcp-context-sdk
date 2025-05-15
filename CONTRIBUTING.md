# Contributing to MCP Context SDK

First off, thank you for considering contributing to MCP Context SDK! It's people like you that make MCP Context SDK such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for MCP Context SDK. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

#### Before Submitting A Bug Report

* Check the [documentation](https://ankit-gautam23.github.io/mcp-context-sdk) for a list of common questions and problems.
* Perform a [cursory search](https://github.com/ankit-gautam23/mcp-context-sdk/issues) to see if the problem has already been reported.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://github.com/ankit-gautam23/mcp-context-sdk/issues). Create an issue and provide the following information by filling in the template.

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as much detail as possible.
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem.
* **If the problem is related to performance or memory**, include a CPU profile capture with your report.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for MCP Context SDK, including completely new features and minor improvements to existing functionality.

#### Before Submitting An Enhancement Suggestion

* Check the [documentation](https://ankit-gautam23.github.io/mcp-context-sdk) for tips.
* Perform a [cursory search](https://github.com/ankit-gautam23/mcp-context-sdk/issues) to see if the enhancement has already been suggested.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/ankit-gautam23/mcp-context-sdk/issues). Create an issue and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as much detail as possible.
* **Provide specific examples to demonstrate the steps**.
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of MCP Context SDK which the suggestion is related to.
* **Explain why this enhancement would be useful** to most MCP Context SDK users.

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Include screenshots and animated GIFs in your pull request whenever possible.
* Follow our [coding conventions](#code-conventions)
* Document new code based on the [Documentation Styleguide](#documentation-styleguide)
* End all files with a newline

## Development Process

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/mcp-context-sdk.git
   ```
3. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Install development dependencies:
   ```bash
   poetry install
   ```

### Code Conventions

* Use [Black](https://github.com/psf/black) for code formatting
* Use [isort](https://pycqa.github.io/isort/) for import sorting
* Use [flake8](https://flake8.pycqa.org/) for linting
* Write tests for all new features
* Keep test coverage high

### Documentation Styleguide

* Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
* Include examples in docstrings
* Update README.md and other documentation files when adding new features

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Testing

Run the test suite:

```bash
poetry run pytest
```

Run linting:

```bash
poetry run black .
poetry run isort .
poetry run flake8
```

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

* `bug` - Issues that are bugs
* `documentation` - Issues for improving or updating our documentation
* `enhancement` - Issues for new features
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed
* `invalid` - Issues that can't or won't be addressed
* `question` - Further information is requested
* `wontfix` - Issues that won't be fixed

## Attribution

This Contributing Guide is adapted from the [Atom Contributing Guide](https://github.com/atom/atom/blob/master/CONTRIBUTING.md). 