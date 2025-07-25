import yaml
import os


def load_config(config_path: str) -> dict:
    if config_path and os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            return config
    else:
        raise FileNotFoundError(f"Configuration file {config_path} not found.")
