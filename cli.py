# cli.py

import argparse
import os
from clipper import Clipper, ClipperConfig

def main():
    parser = argparse.ArgumentParser(
        description="🧠 Clipper: Generate AI images from prompts (text or file)"
    )
    parser.add_argument("input", help="Prompt string or file path")
    parser.add_argument("--config", default="clipper_config.json", help="Path to config JSON")

    args = parser.parse_args()
    config = ClipperConfig(args.config)
    clipper = Clipper(config)

    if os.path.isfile(args.input):
        with open(args.input, "r", encoding="utf-8") as f:
            prompts = [line.strip() for line in f if line.strip()]
        clipper.run_batch(prompts)
    else:
        clipper.run_batch([args.input])

if __name__ == "__main__":
    main()
