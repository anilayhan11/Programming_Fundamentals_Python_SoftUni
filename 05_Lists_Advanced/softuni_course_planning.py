def add_lesson(list_lessons, title):
    if title not in list_lessons:
        list_lessons.append(title)
    return list_lessons


def insert_lesson(list_lessons, title, index):
    if title not in list_lessons:
        list_lessons.insert(index, title)
    return list_lessons


def remove_lesson(list_lessons, title):
    if title in list_lessons:
        title_index = list_lessons.index(title)
        if title_index + 1 in range(len(list_lessons)):
            if "Exercise" in list_lessons[title_index + 1]:
                list_lessons.pop(title_index + 1)
        list_lessons.remove(title)
    return list_lessons


def swap_lesson(list_lessons, first_lesson, second_lesson):
    if first_lesson in list_lessons and second_lesson in list_lessons:
        first_index = list_lessons.index(first_lesson)
        second_index = list_lessons.index(second_lesson)

        first_has_exercise = False
        second_has_exercise = False
        if first_index + 1 in range(len(list_lessons)):
            first_has_exercise = "Exercise" in list_lessons[first_index + 1]
        if second_index + 1 in range(len(list_lessons)):
            second_has_exercise = "Exercise" in list_lessons[second_index + 1]

        list_lessons[first_index], list_lessons[second_index] = \
            list_lessons[second_index], list_lessons[first_index]

        if first_has_exercise and second_has_exercise:
            list_lessons[first_index + 1], list_lessons[second_index + 1] = \
                list_lessons[second_index + 1], list_lessons[first_index + 1]

        elif not first_has_exercise and second_has_exercise:
            list_lessons.insert(first_index + 1, list_lessons.pop(second_index + 1))
        elif first_has_exercise and not second_has_exercise:
            list_lessons.insert(second_index + 1, list_lessons.pop(first_index + 1))
    return list_lessons


def exercise(list_lessons, title):
    if title in list_lessons and f'{title}-Exercise' not in list_lessons:
        title_index = list_lessons.index(title)
        list_lessons.insert(title_index + 1, f'{title}-Exercise')
    elif title not in list_lessons:
        list_lessons.append(title)
        list_lessons.append(f'{title}-Exercise')

    return list_lessons


lessons = input().split(', ')
command = input()

while command != "course start":
    command = command.split(":")
    action, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]

    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    if action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(index_or_lesson_title))
    if action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    if action == "Swap":
        lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
    if action == "Exercise":
        lessons = exercise(lessons, lesson_title)

    command = input()

for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")

