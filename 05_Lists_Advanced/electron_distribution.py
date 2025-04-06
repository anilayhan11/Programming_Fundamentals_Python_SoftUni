electrons = int(input())

result = []
shell = 1

while electrons > 0:
    capacity = 2 * shell * shell

    electrons_in_shell = min(electrons, capacity)
    result.append(electrons_in_shell)
    electrons -= electrons_in_shell
    shell += 1

print(result)
