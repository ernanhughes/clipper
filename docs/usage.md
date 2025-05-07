# Usage Guide

Clipper is a CLI tool that generates images by sending prompts to a running instance of `webui_forge`.

---

## 🖼 Generate from a Single Prompt

```bash
clipper --prompt "A futuristic robot walking in a neon city"
````

This will:

* Call the configured web backend (`http://127.0.0.1:7860`)
* Save the resulting image in `generated_images/`
* Log the prompt in `prompt_log.jsonl`

---

## 📄 Generate from a Prompt File

```bash
clipper --prompts prompts.txt
```

Each line in `prompts.txt` should be a separate text prompt. The tool will:

* Loop through the list
* Generate one image per line
* Sleep between prompts (default: 2 seconds)

---

## ⚙️ Using a Custom Config

```bash
clipper --prompts prompts.txt --config custom_config.json
```

The config file lets you control:

* Output resolution
* Inference steps
* CFG scale
* Delay between prompts

See the [Configuration](config.md) page for details.

---

## 🐍 Using Clipper from Python

You can use Clipper as a library inside any Python script:

```python
from clipper.core import Clipper
from clipper.config import load_config

# Load default config
config = load_config()

# Create the Clipper engine
engine = Clipper(config=config)

# Run a single prompt
engine.generate_image("A serene sunset over a futuristic city")

# Run a batch
prompts = ["A glowing forest at night", "A dragon flying over the mountains"]
engine.run_batch(prompts)
```

---

## ⚡ Advanced Usage

### 🔁 Setting a Random Seed

You can modify the config to set a deterministic seed per run:

```json
{
  "seed": 42,
  "steps": 30,
  "width": 512,
  "height": 512
}
```

> Setting a seed ensures repeatable results across runs.

---

### 🌐 Changing the Backend URL

By default, Clipper sends prompts to `http://127.0.0.1:7860`.
To override this, pass a custom `backend_url` in the config:

```json
{
  "backend_url": "http://localhost:7860",
  "steps": 20
}
```

You can use this to point to:

* A remote server
* A Docker container
* A modified SD backend

---

### 📁 Custom Output Directory

To change where images are saved:

```json
{
  "output_dir": "my_results/"
}
```

This is useful if you want to separate runs by topic or project.

---

## 📂 Output Files

| File                  | Description                                   |
| --------------------- | --------------------------------------------- |
| `generated_images/`   | All output images go here (unless overridden) |
| `prompt_log.jsonl`    | One JSON line per prompt/image                |
| `clipper_config.json` | Optional config file with generation settings |

---

## 🧠 Requirements

* A working instance of [`webui_forge`](https://github.com/lllyasviel/webui-forge) running locally at `http://127.0.0.1:7860`
* Python 3.10+
* Installed package via `pip install clipper-ai`

