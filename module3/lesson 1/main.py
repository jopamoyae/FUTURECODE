# employer = {'name': 'Elvira', 'salary': '200_000', 'on_vacation': False}
# print(f'{employer.get("name")}: {employer.get("salary")}')
# on_vacation = 'on_vacation' if employer.get('on_vacation') else 'on_work'
# print(on_vacation)

# employees_list = [
#     {
#         'name': 'Elvira',
#         'salary': '200_000'
#     },
#     {
#         'name': 'Ivan',
#         'salary': '150_000'
#     },
#     {
#         'name': 'Danil',
#         'salary': '300_000'
#     }
# ]
#
# for employee in employees_list:
#     print(f'{employee.get("name")}: {employee.get("salary")}')
#

class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee

    def info(self):
        print(f'У {self.name} зарплата: {self.salary}. Работник: {self.on_vacation}, его репутация: {self.is_good_employee}')


employees_list = [
    Employee('Эльвира', 200_000, 'в отпуске', True),
    Employee('Данил', 300_000, 'в отпуске', True),
    Employee('Иван', 150_000, 'на работе', True),
    Employee('Алексей', 150_000, 'на работе', True),
    Employee('Карина', 150_000, 'в отпуске', False)
    ]

for i in employees_list:
    if i.is_good_employee == False:
        employees_list.remove(i)
        break

for j in employees_list:
    j.info()


# my_list = []
#
# my_list.append(employee1)
# my_list.append(employee2)
# my_list.append(employee3)
#
# for employee in my_list:
#     employee.info()
#
# my_list.remove(employee3)
# print(my_list)
