def check_employee_happiness():
    employees_happiness = list(map(int, input().split()))
    happiness_factor = int(input())

    improve_happiness = [h * happiness_factor for h in employees_happiness]

    average_happiness = sum(improve_happiness) / len(improve_happiness)
    happy_count = sum(h >= average_happiness for h in improve_happiness)

    total_count = len(improve_happiness)
    message = 'happy' if happy_count >= total_count / 2 else 'not happy'

    result = f'Score: {happy_count}/{total_count}. Employees are {message}!'

    return result


result = check_employee_happiness()
print(result)



