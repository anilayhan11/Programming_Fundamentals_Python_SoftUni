def return_range(character_one, character_two):
    characters_list = []
    for character in range(ord(character_one) + 1, ord(character_two)):
        characters_list.append(chr(character))
    return characters_list


first_character = input()
second_character = input()

result = return_range(first_character, second_character)
print(' '.join(result))
