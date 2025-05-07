# Configuration Reference

Clipper uses a JSON configuration file to control how images are generated via the `webui_forge` backend.

You can pass a config file using the `--config` flag:

```bash
clipper --prompts prompts.txt --config clipper_config.json
````

---

## 🔧 Example `clipper_config.json`

```json
{
  "steps": 40,
  "width": 512,
  "height": 512,
  "cfg_scale": 7.5,
  "delay": 2
}
```

---

## 🔍 Config Options

| Key         | Type    | Description                                                       |
| ----------- | ------- | ----------------------------------------------------------------- |
| `steps`     | `int`   | Number of inference steps (e.g., 20–50)                           |
| `width`     | `int`   | Output image width in pixels                                      |
| `height`    | `int`   | Output image height in pixels                                     |
| `cfg_scale` | `float` | Classifier-Free Guidance scale — how closely to follow the prompt |
| `delay`     | `int`   | Delay (in seconds) between prompts in batch mode                  |

---

## 📁 Default Behavior

If no config file is provided, Clipper uses built-in defaults:

* steps: 30
* width: 512
* height: 512
* cfg\_scale: 7.5
* delay: 1

You can override any of these by passing a custom config file.

