import json

MENU_BASE = "menu.json"


def read_json(data: str):

    try:
        with open(data, "r", encoding="UTF8") as json_menu:
            return json.load(json_menu)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def save_database(data, database_path) -> None:
    with open(
        database_path,
        "w",
    ) as json_menu:
        json.dump(data, json_menu, indent=4)


def write_json(database_path, data):
    database_data = read_json(database_path)
    if len(database_data) == 0:
        data["id"] = 1
    else:
        data["id"] = database_data[-1]["id"] + 1

    database_data.append(data)
    save_database(database_data, database_path)
    return data