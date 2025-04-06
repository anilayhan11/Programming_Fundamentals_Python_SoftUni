def decipher_word(word):
    number_str = ''.join([char for char in word if char.isdigit()])
    first_letter = chr(int(number_str))
    rest = word[len(number_str):]

    if len(rest) > 1:
        rest = rest[-1] + rest[1:-1] + rest[0]

    return first_letter + rest


def decipher_message(message):
    return " ".join(decipher_word(word) for word in message.split())


message_input = input()
print(decipher_message(message_input))
