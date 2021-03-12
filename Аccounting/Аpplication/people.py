from Аccounting.Аpplication.db.config import NUMBER_OF_EMPLOYEES

def get_employees():
    with open('C:\\python\\3.1\\Аccounting\\Аpplication\\db\\employees.txt', 'r', encoding="utf-8") as f:
        list_ = []
        for i in range(NUMBER_OF_EMPLOYEES):
            dict_ = {}
            dict_['Должность'] = f.readline().strip().lower()
            dict_['Имя'] = f.readline().strip().lower()
            dict_['Фамилия'] = f.readline().strip().lower()
            dict_['Телефон'] = f.readline().strip()
            dict_['Коэф. ЗП'] = float(f.readline().strip())
            f.readline()
            list_.append(dict_)
        return list_

if __name__ == '__main__':
    print(get_employees())

