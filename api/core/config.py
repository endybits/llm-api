import os
import json


path = "api/core/config.json"


def get_config_values(path_filename: str = path):
    if len(path_filename) == 0:
        path_filename = path

    if not os.path.exists(path_filename):
        raise FileNotFoundError(f"The config file {path_filename} is missing")
    return json.loads(open(path_filename, "r", encoding="UTF-8").read())
