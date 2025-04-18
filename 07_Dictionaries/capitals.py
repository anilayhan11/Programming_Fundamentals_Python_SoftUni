country_names = input().split(", ")
capitals = input().split(", ")

pairs = dict(zip(country_names, capitals))
for country, capital in pairs.items():
    print(f"{country} -> {capital}")

