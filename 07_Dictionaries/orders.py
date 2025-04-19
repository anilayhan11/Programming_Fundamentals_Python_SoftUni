product_price = {}
while True:
    items = input()

    if items == "buy":
        break

    product, price, quantity = items.split()
    total_price = float(price) * float(quantity)

    if product not in product_price.keys():
        product_price[product] = 0
    product_price[product] += total_price

for product, total_price in product_price.items():
    print(f"{product} -> {total_price:.2f}")

