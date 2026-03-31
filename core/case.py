import json
import os

CASE_DIR = "cases"

def create_case(name):
    case = {
        "name": name,
        "timeline": [],
        "iocs": {}
    }

    path = f"{CASE_DIR}/{name}.json"
    with open(path, "w") as f:
        json.dump(case, f, indent=4)

    return case, path

def load_case(name):
    path = f"{CASE_DIR}/{name}.json"
    with open(path) as f:
        return json.load(f), path

def save_case(case, path):
    with open(path, "w") as f:
        json.dump(case, f, indent=4)
