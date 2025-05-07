import argparse
from clipper.core import Clipper, ClipperConfig

def main():
    parser = argparse.ArgumentParser(description="Clipper - Batch Image Generation for webui_forge")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--prompt', type=str, help='A single prompt to generate an image')
    group.add_argument('--prompts', type=str, help='Path to a file with prompts, one per line')
    parser.add_argument('--config', type=str, help='Path to a JSON config file')

    args = parser.parse_args()

    config = ClipperConfig(args.config)
    clipper = Clipper(config)

    if args.prompt:
        clipper.run_batch([args.prompt])  # wrap single prompt in a list
    elif args.prompts:
        with open(args.prompts, "r", encoding="utf-8") as f:
            prompts = [line.strip() for line in f if line.strip()]
        clipper.run_batch(prompts)
