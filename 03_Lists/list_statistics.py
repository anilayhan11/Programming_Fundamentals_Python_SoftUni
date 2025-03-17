n = int(input())

positives_list = []
negatives_list = []

for _ in range(n):
    current_num = int(input())

    if current_num < 0:
        negatives_list.append(current_num)
    else:
        positives_list.append(current_num)

print(positives_list)
print(negatives_list)
print(f'Count of positives: {len(positives_list)}')
print(f'Sum of negatives: {sum(negatives_list)}')
