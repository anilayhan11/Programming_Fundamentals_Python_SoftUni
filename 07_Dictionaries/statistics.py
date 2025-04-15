product_quantity = {}
command = input()

while command != "statistics":
    key = command.split(": ")[0]
    value = int(command.split(": ")[1])

    if key not in product_quantity:
        product_quantity[key] = 0
    product_quantity[key] += value

    command = input()


print(f"Products in stock:")
for (key, value) in product_quantity.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(product_quantity.keys())}")
print(f"Total Quantity: {sum(product_quantity.values())}")
