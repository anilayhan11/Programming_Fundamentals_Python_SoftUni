products_input = input().split()
products = {}

for i in range(0, len(products_input), 2):
    key = products_input[i]
    value = products_input[i + 1]
    products[key] = value

requested_products = input().split()

for product in requested_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
