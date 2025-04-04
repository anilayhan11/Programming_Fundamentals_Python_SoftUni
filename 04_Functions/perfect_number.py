def is_perfect_number(num):
    sum_ppd = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_ppd += divisor

    if sum_ppd == num:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect_number(number))
