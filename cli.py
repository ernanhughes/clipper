# cli.py

import sys, os
from clipper.core import run_prompt, run_batch

def main():
    if len(sys.argv) < 2:
        print("""
[✱] Usage: clipper <prompt or file path>

You can pass either:
  📄 A file path — containing one prompt per line (e.g., prompts.txt)
  📝 A single prompt — like "flat icon of a rocket in outline style"

Examples:
  clipper prompts.txt
  clipper "an icon of a calendar with checkmarks"

""")
        return

    arg = sys.argv[1]
    if os.path.isfile(arg):
        with open(arg, "r") as f:
            prompts = [line.strip() for line in f if line.strip()]
        run_batch(prompts)
    else:
        run_prompt(arg)

if __name__ == "__main__":
    main()
