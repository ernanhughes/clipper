import json
import requests
import time
import os
import logging
import re
import base64
from datetime import datetime
from typing import List, Optional

class ClipperConfig:
    def __init__(self, config_file: Optional[str] = None):
        # Default config
        self.api_url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
        self.output_dir = "generated_images"
        self.log_file = "clipper.log"
        self.prompt_log = "prompt_log.jsonl"
        self.steps = 30
        self.width = 512
        self.height = 512
        self.cfg_scale = 7
        self.delay = 1

        if config_file and os.path.exists(config_file):
            self.load_from_file(config_file)

        os.makedirs(self.output_dir, exist_ok=True)

    def load_from_file(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for key in data:
            if hasattr(self, key):
                setattr(self, key, data[key])


class Clipper:
    def __init__(self, config: ClipperConfig):
        self.config = config
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(self.config.log_file),
                logging.StreamHandler()
            ]
        )

    def _sanitize_filename(self, prompt: str) -> str:
        slug = re.sub(r'[^\w\s-]', '', prompt).strip().lower()
        return re.sub(r'[-\s]+', '-', slug)[:50]

    def _log_prompt_metadata(self, prompt: str, filename: str, timestamp: str):
        log_entry = {
            "prompt": prompt,
            "filename": filename,
            "timestamp": timestamp,
            "width": self.config.width,
            "height": self.config.height,
            "cfg_scale": self.config.cfg_scale,
            "steps": self.config.steps
        }
        with open(self.config.prompt_log, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")

    def generate_image(self, prompt: str):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_name = self._sanitize_filename(prompt)
        filename = f"{base_name}_{timestamp}.png"
        output_path = os.path.join(self.config.output_dir, filename)

        payload = {
            "prompt": prompt,
            "steps": self.config.steps,
            "width": self.config.width,
            "height": self.config.height,
            "cfg_scale": self.config.cfg_scale
        }

        try:
            response = requests.post(self.config.api_url, json=payload)
            response.raise_for_status()
            r = response.json()

            if "images" in r:
                image_data = r["images"][0]
                image_bytes = base64.b64decode(image_data.split(",", 1)[-1])

                with open(output_path, "wb") as f:
                    f.write(image_bytes)

                logging.info(f"✅ Saved: {filename}")
                self._log_prompt_metadata(prompt, filename, timestamp)
            else:
                logging.error(f"❌ No image returned for: {prompt}")

        except Exception as e:
            logging.exception(f"❌ Error generating image for: {prompt} — {e}")

    def run_batch(self, prompts: List[str]):
        logging.info(f"📦 Starting batch: {len(prompts)} prompts")
        for i, prompt in enumerate(prompts):
            logging.info(f"[{i+1}/{len(prompts)}] {prompt[:60]}")
            self.generate_image(prompt)
            time.sleep(self.config.delay)
        logging.info("🎉 Batch complete")


# --- Example usage ---
if __name__ == "__main__":
    config = ClipperConfig("clipper_config.json")
    clipper = Clipper(config)

    prompts = [
        "A majestic lion standing on a cliff at sunrise",
        "Cyberpunk samurai walking through a neon-lit alley",
        "Abstract painting of a dreamlike forest in spring"
    ]

    clipper.run_batch(prompts)
