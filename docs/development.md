# Developer Guide

This guide helps contributors and developers work on Clipper locally.

---

## 🛠 Local Development Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/clipper.git
cd clipper
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. Install the package in editable mode with development dependencies:

```bash
pip install -e .[dev]
```

---

## 🧪 Run Tests

Clipper uses `pytest` for testing.

To run all tests:

```bash
pytest
```

To run only unit tests (skip integration):

```bash
pytest -m "not integration"
```

To run integration tests:

```bash
CLIPPER_ENABLE_INTEGRATION=1 pytest
```

---

## 📦 Building and Uploading

To build the distribution:

```bash
python -m build
```

To upload to [PyPI](https://pypi.org/project/clipper-ai/):

```bash
twine upload dist/*
```

Or to test it on [TestPyPI](https://test.pypi.org):

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

---

## 🧱 Project Structure

```
clipper/
├── __main__.py     ← CLI entry point
├── core.py         ← Main Clipper logic
├── config.py       ← Config loader
├── prompts.py      ← Prompt file utilities
├── utils.py        ← Logging & helper functions
tests/
├── test_cli.py     ← CLI integration tests
├── test_core.py    ← Unit tests for core logic
generated_images/   ← Output folder
prompt_log.jsonl    ← Log of all prompts & metadata
```

---

## ✅ Contributions

* Feel free to open issues or PRs
* Style guide: keep it Pythonic + documented
* Use clear commit messages and test your changes

Thanks for helping improve Clipper-AI!
