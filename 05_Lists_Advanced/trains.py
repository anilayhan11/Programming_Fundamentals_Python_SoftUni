wagons = int(input())
train = [0] * wagons
command = input().split()
action = command[0]

while action != 'End':
    if action == 'add':
        people = int(command[1])
        train[-1] += people

    if action == 'insert':
        index = int(command[1])
        people = int(command[2])
        train[index] += people
        #  train.insert(index, people)

    if action == 'leave':
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

    command = input().split()
    action = command[0]

print(train)
