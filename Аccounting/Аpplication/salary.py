from Аccounting.Аpplication.db.config import WORKING_DAYS_PER_YEAR, COMPANY_SALARY


def calculate_salary():
    while True:
        quantity = int(input('Введите количество рабочих дней в месяце: '))
        if quantity > 23:
            print('Больше 23 рабочих дней в месяце быть не может')
        else:
            break
    average_salary = COMPANY_SALARY
    return int(quantity/WORKING_DAYS_PER_YEAR * average_salary)

if __name__ == '__main__':
    print(f'Фонд оплаты труда за месяц составит - {calculate_salary()}')