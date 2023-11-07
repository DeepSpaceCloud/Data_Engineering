import json
import pickle

with open("products_18.pkl", "rb") as f:
    products = sorted(pickle.load(f), key=lambda item: item['name'])
# print(products)

with open("price_info_18.json") as f:
    price_info = sorted(json.load(f), key=lambda item: item['name'])

for index, product in enumerate(products):
    method = price_info[index]["method"]
    if method == "sum":
        product["price"] += price_info[index]["param"]
    elif method == "sub":
        product["price"] -= price_info[index]["param"]
    elif method == "percent+":
        product["price"] *= (1 + price_info[index]["param"])
    elif method == "percent-":
        product["price"] *= (1 - price_info[index]["param"])
    product["price"] = round(product["price"], 2)

# print(products)

with open("products_updated.pkl", "wb") as f:
    f.write(pickle.dumps(products))
