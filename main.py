from applications.salary import calculate_salary
from applications.db.people import get_employees

def main():
    calculate_salary()
    print('*' * 15)
    get_employees()

if __name__ == '__main__':
    main()
