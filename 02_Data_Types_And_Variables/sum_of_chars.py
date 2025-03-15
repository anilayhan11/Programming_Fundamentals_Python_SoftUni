lines_count = int(input())
sum_characters = 0

for symbol in range(lines_count):
    letter = input()
    sum_characters += ord(letter)

print(f'The sum equals: {sum_characters}')
