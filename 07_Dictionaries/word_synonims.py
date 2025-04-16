n = int(input())
word_pairs = {}
for _ in range(n):
    word = input()
    synonym = input()
    if word not in word_pairs:
        word_pairs[word] = []
    word_pairs[word].append(synonym)

for word in word_pairs:
    print (f"{word} - {', '.join(word_pairs[word])}")
