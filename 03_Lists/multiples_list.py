factor = int(input())
count = int(input())

list_numbers = []

for multiplier in range(factor, count * factor + 1, factor):
    list_numbers.append(multiplier)

print(list_numbers)
