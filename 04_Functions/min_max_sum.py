def min_max_numbers(nums):
    min_number = min(nums)
    max_number = max(nums)
    sum_numbers = sum(nums)

    return min_number, max_number, sum_numbers


numbers_as_strings = input().split()
numbers_as_digits = []
for num in numbers_as_strings:
    numbers_as_digits.append(int(num))

min_num, max_num, sum_nums = min_max_numbers(numbers_as_digits)
print(f'The minimum number is {min_num}')
print(f'The maximum number is {max_num}')
print(f'The sum number is: {sum_nums}')

