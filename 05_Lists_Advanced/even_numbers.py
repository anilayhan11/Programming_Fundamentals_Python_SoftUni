numbers = list(map(int, input().split(', ')))
indexes_found_or_not = map(
    lambda x: x if numbers[x] % 2 == 0 else 'no',
    range(len(numbers))
)

even_indexes = list(filter(lambda a: a != 'no', indexes_found_or_not))

print(even_indexes)
