import json
import requests
import time
import os
import uuid
import logging

COMFY_API_URL = "http://127.0.0.1:8188/prompt"
DEFAULT_WORKFLOW_PATH = "workflow_base.json"
LOG_FILE = "clipper.log"

# --- Setup logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def load_workflow(workflow_path=DEFAULT_WORKFLOW_PATH):
    if not os.path.exists(workflow_path):
        logging.error(f"Missing required file: {workflow_path}")
        raise FileNotFoundError(
            f"""
[✘] Missing required file: {workflow_path}

This file defines the ComfyUI workflow to use when generating images.

➡️ What to do:
  1. Make sure 'workflow_base.json' is located in the root of your Clipper project.
  2. It should include nodes like CLIPTextEncode, KSampler, VAEDecode, SaveImage.

📁 Example location:
  ./workflow_base.json
""")
    logging.info(f"Loaded workflow from: {workflow_path}")
    with open(workflow_path, "r") as f:
        return json.load(f)

def inject_prompt(workflow, prompt):
    found = False
    logging.info(f"Injecting prompt: '{prompt}'")
    for node_id, node in workflow["nodes"].items():
        if node["class_type"] == "CLIPTextEncode":
            logging.info(f"Found CLIPTextEncode node (id: {node_id})")
            node["inputs"]["text"] = prompt
            found = True
    if not found:
        logging.error("No CLIPTextEncode node found in workflow.")
        raise ValueError("No CLIPTextEncode node found in workflow.")
    return workflow

import pprint

def run_prompt(prompt, workflow_path=DEFAULT_WORKFLOW_PATH):
    logging.info(f"Starting generation for: '{prompt}'")
    workflow = load_workflow(workflow_path)
    workflow = inject_prompt(workflow, prompt)

    # 👀 Print full workflow to console
    print("\n[📄] Workflow to be submitted:")
    print("=" * 60)
    print(json.dumps(workflow, indent=2))
    print("=" * 60 + "\n")

    try:
        response = requests.post(COMFY_API_URL, json=workflow)
    except Exception as e:
        logging.error(f"Connection error: {e}")
        return

    if response.status_code == 200:
        logging.info("Prompt submitted successfully")
    else:
        logging.error(f"HTTP {response.status_code}: {response.text}")
        try:
            logging.debug("Response JSON: %s", response.json())
        except:
            logging.debug("Raw response: %s", response.text)

def run_batch(prompt_list, workflow_path=DEFAULT_WORKFLOW_PATH):
    logging.info(f"Starting batch run ({len(prompt_list)} prompts)")
    for i, prompt in enumerate(prompt_list):
        logging.info(f"--- [{i+1}/{len(prompt_list)}] ---")
        run_prompt(prompt, workflow_path)
        time.sleep(1)
    logging.info("Batch run completed")