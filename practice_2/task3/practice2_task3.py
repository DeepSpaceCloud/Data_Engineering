import json
import msgpack
import os

with open("products_18.json") as file:
    data = json.load(file)

products = dict()

for item in data:
    if item['name'] in products:
        products[item['name']].append(item['price'])
    else:
        products[item['name']] = list()
        products[item['name']].append(item['price'])

result = list()

for name, prices in products.items():
    result.append({
        "name": name,
        "max": max(prices),
        "min": min(prices),
        "avr": sum(prices)/len(prices)
    })

with open("products_result.json", "w") as r_json:
    r_json.write(json.dumps(result))

with open("products_result.msgpack", "wb") as r_msgpack:
    r_msgpack.write(msgpack.dumps(result))

print(f"json    = {os.path.getsize('products_result.json')}")
print(f"msgpack = {os.path.getsize('products_result.msgpack')}")
