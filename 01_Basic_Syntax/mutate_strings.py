string1 = input()
string2 = input()
last_printed_word = string1

for idx in range(len(string1)):
    left_part = string2[:idx + 1]
    right_part = string1[idx + 1:]
    new_string = left_part + right_part

    if last_printed_word != new_string:
        print(new_string)
        last_printed_word = new_string
