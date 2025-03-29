def sum_numbers(num):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for digit in num:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_odd_digits, sum_of_even_digits


number = input()
odd_digits, even_digits = sum_numbers(number)
print(f'Odd sum = {odd_digits}, Even sum = {even_digits}')
