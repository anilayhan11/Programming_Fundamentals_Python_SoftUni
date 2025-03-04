budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_lt_milk = price_kg_flour * 1.25
price_250ml_milk = price_lt_milk / 4
needed_budget_per_loaf = price_kg_flour + price_pack_eggs + price_250ml_milk

collected_colored_eggs = 0
loaves_count = 0

while budget >= needed_budget_per_loaf:
    loaves_count += 1
    budget -= needed_budget_per_loaf
    collected_colored_eggs += 3

    if loaves_count % 3 == 0:
        collected_colored_eggs -= loaves_count - 2

print(f'You made {loaves_count} loaves of Easter bread! '
      f'Now you have {collected_colored_eggs} eggs and {budget:.2f}BGN left.')


