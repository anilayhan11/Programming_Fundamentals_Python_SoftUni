tokens = input().split(", ")
pairs = dict()
for key in tokens:
    pairs[key] = ord(key)

print(pairs)

# pairs = {key: ord(key) for key in input().split(", ")}
# print(pairs)
