cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    shuffled_deck = []
    middle_of_deck = len(cards) // 2

    first_half = cards[0:middle_of_deck]
    second_half = cards[middle_of_deck:]

    for idx in range(len(first_half)):
        shuffled_deck.append(first_half[idx])
        shuffled_deck.append(second_half[idx])

    cards = shuffled_deck

print(cards)

