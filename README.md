# Clipper

**Clipper** is a Python CLI tool for batch image generation using text prompts. It connects to `webui_forge` (a Stable Diffusion API backend) to generate images from single prompts or prompt files, and logs each result for easy tracking.

---

## 🚀 Features

- 🖼 Generate images using `webui_forge` from:
  - A single prompt (`--prompt`)
  - A file of prompts (`--prompts`)
- 🧠 Logs metadata to `prompt_log.jsonl`
- ⚙️ Configurable via a JSON file (`--config`)
- 🧪 Comes with unit + CLI tests (`pytest`)
- 🧰 Built for automation and reuse

---

## 🔧 Installation

Install in development mode:

```bash
git clone https://github.com/yourusername/clipper.git
cd clipper
pip install -e .
````

You’ll also need a running `webui_forge` instance at:

```
http://127.0.0.1:7860
```

---

## 🖥 Usage

### Generate from a single prompt:

```bash
clipper --prompt "A futuristic city under a red sky"
```

### Generate from a file of prompts:

```bash
clipper --prompts prompts.txt
```

### Use a custom configuration file:

```bash
clipper --prompts prompts.txt --config my_config.json
```

Example `clipper_config.json`:

```json
{
  "steps": 40,
  "width": 640,
  "height": 640,
  "cfg_scale": 8.5,
  "delay": 2
}
```

---

## 📁 Output

* Images are saved in: `generated_images/`
* Log entries are written to: `generated_images/prompt_log.jsonl`

Sample log entry:

```json
{
  "prompt": "A futuristic city",
  "filename": "clipper_2025-05-07_12-00-00.png",
  "timestamp": "2025-05-07T12:00:00Z",
  "width": 640,
  "height": 640
}
```

---

## 🧪 Tests

Run all tests with:

```bash
pytest
```

Tests cover:

* Core logic (`clipper/core.py`)
* CLI interface (`clipper/cli.py`)
* Prompt logging and file generation

---

## 📦 Publishing to PyPI

To release a new version:

1. Push a new tag (e.g. `v0.1.0`)
2. GitHub Actions will run tests and publish automatically using your `PYPI_API_TOKEN`.

See `.github/workflows/python-package.yml` for full details.

---

## 📜 License

MIT License

---

## 🤖 Powered by AI

This project was built with heavy collaboration between a human developer and AI assistants. It is part of the *Applied AI* series of tools.

```

