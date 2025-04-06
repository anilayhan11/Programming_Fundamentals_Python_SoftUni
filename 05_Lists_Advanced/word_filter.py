tokens = input().split(' ')
valid_words = [word for word in tokens if len(word) % 2 == 0]

print('\n'.join(valid_words))

# tokens = input().split(' ')
# filtered_words = []
# for word in tokens:
#     if len(word) % 2 == 0:
#         filtered_words.append(word)
# print('\n'.join(filtered_words))

