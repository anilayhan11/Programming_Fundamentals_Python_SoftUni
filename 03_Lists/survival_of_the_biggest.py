input_nums = input().split()
n = int(input())
integers_list = []

for num in input_nums:
    integers_list.append(int(num))

for _ in range(n):
    integers_list.remove(min(integers_list))

print(", ".join(map(str, integers_list)))


