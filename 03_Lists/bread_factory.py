energy = 100
coins = 100
events_list = input().split('|')
day_is_completed = True

for event in events_list:
    event_items = event.split('-')

    event_type = event_items[0]
    event_value = int(event_items[1])

    if event_type == 'rest':
        current_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif event_type == 'order':
        if energy < 30:
            print('You had to rest!')
            energy += 50
        else:
            print(f'You earned {event_value} coins.')
            energy -= 30
            coins += event_value

    else:
        if coins >= event_value:
            print(f'You bought {event_type}.')
            coins -= event_value
        else:
            print(f'Closed! Cannot afford {event_type}.')
            day_is_completed = False
            break

if day_is_completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
