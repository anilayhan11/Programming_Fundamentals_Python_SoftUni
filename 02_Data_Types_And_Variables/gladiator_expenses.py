lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_broken_counter = 0

expenses = 0

for lost_fight in range(1, lost_fights + 1):
    helmet_broken = False
    sword_broken = False

    if lost_fight % 2 == 0:
        helmet_broken = True
        expenses += helmet_price
    if lost_fight % 3 == 0:
        expenses += sword_price

        if helmet_broken:
            shield_broken_counter += 1
            expenses += shield_price

    if shield_broken_counter == 2:
        shield_broken_counter = 0
        expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
