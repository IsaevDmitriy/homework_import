from datetime import datetime
from Аpplication.salary import calculate_salary
from Аpplication.people import get_employees


def main():
    print(datetime.now().strftime('%d.%m.%Y'))
    post = input('Введите должность: ').lower()
    month_salary = 0
    for dict_employees in get_employees():
        if post == dict_employees['Должность']:
            month_salary = dict_employees['Коэф. ЗП'] * calculate_salary()
            print(f'В этом месяце зарплата на должности {post} составит {month_salary}')
            break
    if month_salary == 0:
        print(f'В компании нет такой должности')

main()
