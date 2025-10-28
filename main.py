from services.employee_service import EmployeeService
from services.car_service import CarService
from services.salg_service import SalgService
from reports.report_service import ReportService


def employees_menu(service: EmployeeService):
    while True:
        print("\n=== МЕНЮ СПІВРОБІТНИКІВ ===")
        print("1. Додати співробітника")
        print("2. Видалити співробітника")
        print("3. Показати всіх співробітників")
        print("0. Назад")
        choice = input("Оберіть дію: ")

        if choice == "1":
            fio = input("ПІБ: ")
            position = input("Посада: ")
            tlf = input("Телефон: ")
            email = input("Email: ")
            emp = service.add_employee(fio, position, tlf, email)
            print(f"Додано: {emp.fio}")

        elif choice == "2":
            emp_id = input("Введіть ID для видалення: ")
            service.delete_by_id(emp_id)

        elif choice == "3":
            employees = service.get_employees()
            print("\nСПИСОК СПІВРОБІТНИКІВ:")
            for e in employees:
                print(e)

        elif choice == "0":
            break
        else:
            print("Невірний вибір")


def cars_menu(service: CarService):
    while True:
        print("\n=== МЕНЮ АВТОМОБІЛІВ ===")
        print("1. Додати авто")
        print("2. Видалити авто")
        print("3. Показати всі авто")
        print("0. Назад")
        choice = input("Оберіть дію: ")

        if choice == "1":
            model = input("Модель: ")
            year = input("Рік випуску: ")
            car_type = input("Тип: ")
            cost_price = float(input("Собівартість: "))
            potential_price = float(input("Потенційна ціна продажу: "))
            car = service.add_car(model, year, car_type, cost_price, potential_price)
            print(f"Додано авто: {car.car_name}")

        elif choice == "2":
            car_id = input("Введіть ID авто для видалення: ")
            service.delete_by_id(car_id)

        elif choice == "3":
            cars = service.get_cars()
            print("\nСПИСОК АВТОМОБІЛІВ:")
            for c in cars:
                print(c)

        elif choice == "0":
            break
        else:
            print("Невірний вибір")


def salgs_menu(service: SalgService):
    while True:
        print("\n=== МЕНЮ ПРОДАЖІВ ===")
        print("1. Додати продаж")
        print("2. Видалити продаж")
        print("3. Показати всі продажі")
        print("0. Назад")
        choice = input("Оберіть дію: ")

        if choice == "1":
            employee = input("Ім’я працівника: ")
            car_model = input("Модель авто: ")
            date = input("Дата продажу (ДДММРРРР): ")
            price = input("Реальна ціна продажу: ")
            salg = service.add_salg(employee, car_model, date, price)
            print(f"Додано продаж: {salg.car_model} — {salg.employee}")

        elif choice == "2":
            salg_id = input("Введіть ID продажу: ")
            service.delete_by_id(salg_id)

        elif choice == "3":
            salgs = service.get_salgs()
            print("\nСПИСОК ПРОДАЖІВ:")
            for s in salgs:
                print(s)

        elif choice == "0":
            break
        else:
            print("Невірний вибір")


def reports_menu(report: ReportService):
    while True:
        print("\n=== ЗВІТИ ===")
        print("1. Усі співробітники")
        print("2. Усі автомобілі")
        print("3. Усі продажі")
        print("4. Продажі за дату")
        print("5. Продажі за період")
        print("6. Продажі конкретного працівника")
        print("7. Найпопулярніше авто за період")
        print("8. Найуспішніший продавець за період")
        print("9. Сумарний прибуток за період")
        print("0. Назад")
        choice = input("Оберіть дію: ")

        if choice == "1":
            for emp in report.all_employees():
                print(emp)

        elif choice == "2":
            for car in report.all_cars():
                print(car)

        elif choice == "3":
            for s in report.all_salgs():
                print(s)

        elif choice == "4":
            date = input("Введіть дату (ДДММРРРР): ")
            salgs = report.salgs_by_date(date)
            for s in salgs:
                print(s)

        elif choice == "5":
            start = input("Початкова дата (ДДММРРРР): ")
            end = input("Кінцева дата (ДДММРРРР): ")
            salgs = report.salgs_by_period(start, end)
            for s in salgs:
                print(s)

        elif choice == "6":
            name = input("Ім’я працівника: ")
            for s in report.salgs_by_employee(name):
                print(s)

        elif choice == "7":
            start = input("Початкова дата: ")
            end = input("Кінцева дата: ")
            report.best_selgers_car(start, end)

        elif choice == "8":
            start = input("Початкова дата: ")
            end = input("Кінцева дата: ")
            report.top_selger(start, end)

        elif choice == "9":
            start = input("Початкова дата: ")
            end = input("Кінцева дата: ")
            report.total_profit(start, end)

        elif choice == "0":
            break
        else:
            print("Невірний вибір")


def main():
    emp_service = EmployeeService()
    car_service = CarService()
    salg_service = SalgService()
    report = ReportService(emp_service, car_service, salg_service)

    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Співробітники")
        print("2. Автомобілі")
        print("3. Продажі")
        print("4. Звіти")
        print("0. Вихід")

        choice = input("Оберіть розділ: ")

        if choice == "1":
            employees_menu(emp_service)
        elif choice == "2":
            cars_menu(car_service)
        elif choice == "3":
            salgs_menu(salg_service)
        elif choice == "4":
            reports_menu(report)
        elif choice == "0":
            print("Завершення роботи програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()