def process_todo_notes():
    todo_notes = []

    command = input()
    while command != 'End':
        todo_notes.append(command)
        command = input()

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
    result_sorted_notes = [note.split('-')[1] for note in sorted_notes]

    return result_sorted_notes


result = process_todo_notes()
print(result)
