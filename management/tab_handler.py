from utils.json_handler import read_json
from datetime import date, time, datetime, timedelta, timezone

MENU_BASE = "menu.json"


def calculate_tab(table: dict):

    MENU = read_json(MENU_BASE)
    price = 0
    for product in MENU:
        for request in table:
            if product["id"] == request["id"]:
                price += product["price"] * request["amount"]
    dating = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return {"subtotal": price, "created_at": dating}