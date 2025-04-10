import json

import requests


required_ids = ["1INCH-USDT-11109-1743062088268", "1INCH-USDT-10712-1743060574646", "1INCH-USDT-10711-1743060574111",
                "1INCH-USDT-10710-1743060573567"]



def orders_update(ids):
    order_details = []
    for id in required_ids:
        data = {
            "X-API-Key": "",
            "orderID": id
        }
        url = f"https://api.ataix.kz/api/orders/{id}"
        response = requests.get(url, headers=data)
        print(response.url)
        print(json.dumps(response.json(), indent=4))

        if response.json()["result"]["status"] == "filled":
            order_details.append({
                "order_id": id,
                "status": "filled"
            })
    with open("products.json", "w") as f:
        f.write(str(order_details))

orders_update(required_ids)
