list_of_numbers = input().split()
opposite_numbers = []

for number in list_of_numbers:
    current_number = -int(number)
    opposite_numbers.append(current_number)

print(opposite_numbers)
