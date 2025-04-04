def calculate_factorial(number):

    for num in range(1, number):
        number *= num
    return number


number_one = int(input())
number_two = int(input())
factorial_first = calculate_factorial(number_one)
factorial_second = calculate_factorial(number_two)

result = factorial_first / factorial_second
print(f"{result:.2f}")
