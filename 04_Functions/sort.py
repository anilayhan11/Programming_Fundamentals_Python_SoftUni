def sort_numbers(numbers):
    return sorted(numbers)


numbers_as_strings = input().split()
numbers_as_digits = []
for num in numbers_as_strings:
    numbers_as_digits.append(int(num))


print(sort_numbers(numbers_as_digits))
