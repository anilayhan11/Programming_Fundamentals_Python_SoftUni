n = int(input())
word = input()

list_all_strings = [input() for _ in range(n)]

filtered_strings = []
for string in list_all_strings:
    if word in string:
        filtered_strings.append(string)

print(list_all_strings)
print(filtered_strings)
