import json

def import_Questions_Json(file_path : str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data
