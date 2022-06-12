from datetime import datetime

def calculate_salary():
    print('Модуль salary.py')
    date_now = datetime.now()
    print(f'''{date_now.year}.{date_now.month}.{date_now.day}''')
