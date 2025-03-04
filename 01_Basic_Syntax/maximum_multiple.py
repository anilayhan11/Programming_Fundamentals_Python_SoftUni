divisor = int(input())
boundary = int(input())

for num in range(boundary, divisor - 1, -1):
    if num > 0 and num % divisor == 0:
        print(num)
        break
