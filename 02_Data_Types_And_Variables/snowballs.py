snowballs_num = int(input())
best_snowball_value = 0
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0

for snowball in range(snowballs_num):
    weight = int(input())
    time = int(input())
    quality = int(input())

    current_snowball_value = (weight // time) ** quality

    if current_snowball_value > best_snowball_value:
        best_snowball_value = current_snowball_value
        best_snowball_weight = weight
        best_snowball_time = time
        best_snowball_quality = quality

print(f'{best_snowball_weight} : {best_snowball_time} = {best_snowball_value} ({best_snowball_quality})')


