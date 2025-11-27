import yaml

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

MODEL_NAME = config["model_name"]
MEMORY_FILE = config["memory_file"]
