def sum_numbers(number1, number2):
    return number1 + number2


def subtract(summ, number3):
    return summ - number3


def add_and_subtract(number_one, number_two, number_three):
    sum_of_first_two_numbers = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_two_numbers, number_three)
    print(result)


first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract(first_number, second_number, third_number)
