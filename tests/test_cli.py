import subprocess
import tempfile
import os
import subprocess
import time
import json
import pytest

integration = pytest.mark.skipif(
    not os.environ.get("CLIPPER_ENABLE_INTEGRATION"),
    reason="Integration test disabled by default"
)

@integration
def test_cli_single_prompt_log_validation():
    prompt = "Test prompt for spaceship city"
    subprocess.run(["python", "-m", "clipper", "--prompt", prompt], check=True)

    log_path = "prompt_log.jsonl"
    assert os.path.exists(log_path)

    # Wait a moment to ensure the log is written
    time.sleep(1)

    with open(log_path, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f if line.strip()]

    matching_entries = [e for e in entries if e["prompt"] == prompt]
    assert matching_entries, f"Prompt not found in log: {prompt}"

    for entry in matching_entries:
        image_path = os.path.join("generated_images", entry["filename"])
        assert os.path.exists(image_path), f"Image file does not exist: {image_path}"


@integration
def test_cli_prompt_file_log_validation():
    prompts = ["Test prompt: red dragon", "Test prompt: green mountain"]
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as f:
        for line in prompts:
            f.write(line + "\n")
        f.flush()
        subprocess.run(["python", "-m", "clipper", "--prompts", f.name], check=True)

    log_path = "prompt_log.jsonl"
    assert os.path.exists(log_path)

    # Wait a moment to ensure the log is written
    time.sleep(1)

    with open(log_path, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f if line.strip()]

    for prompt in prompts:
        match = [e for e in entries if e["prompt"] == prompt]
        assert match, f"Prompt not found in log: {prompt}"
        for entry in match:
            image_path = os.path.join("generated_images", entry["filename"])
            assert os.path.exists(image_path), f"Missing image file: {image_path}"
