# Welcome to Clipper

Clipper is a Python CLI tool for generating images using prompts via the `webui_forge` backend.

This documentation will walk you through installing, using, and configuring Clipper.

## Features

- 🖼 Generate images from single prompts or batch files
- ⚙️ Fully configurable via `clipper_config.json`
- 🧠 Logs prompts and metadata to `prompt_log.jsonl`
- 🧪 Tested CLI with `pytest`
- 🚀 Built for local and automated workflows

## Quick Start

1. Install Clipper:
   ```bash
   pip install clipper-ai
````

2. Generate an image:

   ```bash
   clipper --prompt "A futuristic robot walking in a neon city"
   ```

3. View output in the `generated_images/` folder

---

## About This Project

Clipper is part of the **Applied AI** toolset — projects focused on amplifying creation using AI, prompt engineering, and real-world coding workflows.

It was built as part of an iterative development process, blending human creativity and AI support to rapidly build functional tools.

```

Let me know if you'd like the other pages printed too (like `usage.md`, `config.md`, or `development.md`).
```

> **Note:** Clipper depends on [`webui_forge`](https://github.com/lllyasviel/webui-forge), a modified Stable Diffusion Web UI backend. You must have it running locally at `http://127.0.0.1:7860` for image generation to work.
