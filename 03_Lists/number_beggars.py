money_strings = input().split(', ')
beggars_count = int(input())
money_ints = []

for element in money_strings:
    money_ints.append(int(element))

final_money = []


for beggar in range(beggars_count):

    sum_for_current_beggar = 0

    for current_index in range(beggar, len(money_strings), beggars_count):
        sum_for_current_beggar += money_ints[current_index]

    final_money.append(sum_for_current_beggar)

print(final_money)
