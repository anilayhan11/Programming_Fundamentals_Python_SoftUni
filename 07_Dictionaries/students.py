student_info = []
course = ""

while True:
    information = input()

    if information.__contains__(":"):
        name, student_id, course = information.split(":")
        student_info.append({"name": name, "ID": student_id, "course": course})
    else:
        course = information
        break

for student in student_info:
    if course.startswith(student["course"][0:3]):
        print(f"{student['name']} - {student['ID']}")

