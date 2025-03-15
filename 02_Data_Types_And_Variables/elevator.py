people_count = int(input())
capacity = int(input())

courses = people_count // capacity
if people_count % capacity != 0:
    courses += 1

print(courses)
