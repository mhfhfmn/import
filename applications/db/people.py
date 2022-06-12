from datetime import datetime

def get_employees():
    print('Модуль people.py')
    date_now = datetime.now()
    print(f'''{date_now.year}.{date_now.month}.{date_now.day}''')


