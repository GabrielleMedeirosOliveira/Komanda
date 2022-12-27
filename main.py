from utils.json_handler import read_json, write_json
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    print(read_json("menu.json"))

    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    print(write_json("menu.json", new_item))

    table_1 = [{"id": 1, "amount": 5}, {"id": 19, "amount": 5}]
    table_2 = [
        {"id": 10, "amount": 3},
        {"id": 20, "amount": 2},
        {"id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))