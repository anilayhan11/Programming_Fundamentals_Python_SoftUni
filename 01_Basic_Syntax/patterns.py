num = int(input())

# for row in range(num):
#     for col in range(row):
#         print('*', end='')
#     print()
#
# for row in range(num, 0, -1):
#     for col in range(row):
#         print('*', end='')
#     print()

for i in range(1, num):
    print(i * '*')

for i in range(num, 0, -1):
    print(i * '*')
