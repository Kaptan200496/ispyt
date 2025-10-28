from datetime import datetime, date

class ReportService:
    def __init__(self, employee_service, car_service, salg_service):
        self.employee_service = employee_service
        self.car_service = car_service
        self.salg_service = salg_service
    def all_employees(self):
        return self.employee_service.get_employees()

    def all_cars(self):
        return self.car_service.get_cars()

    def all_salgs(self):
        return self.salg_service.get_salgs()

    def salgs_by_date(self, search_date):
        salgs = self.salg_service.get_salgs()
        return [target for target in salgs if target["salg_date"] == search_date]

    def parse_date(self, date_str):
        formats = ["%d%m%Y", "%Y-%m-%d", "%d.%m.%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                pass
        raise ValueError(f"Неправильний формат дати: {date_str}")

    def salgs_by_period(self, start, end):
        salgs = self.salg_service.get_salgs()
        ar_for_salgs = []
        for current in salgs:
            if self.parse_date(start) <= self.parse_date(current["salg_date"]) and self.parse_date(current["salg_date"]) <= self.parse_date(end):
                ar_for_salgs.append(current)
                print(ar_for_salgs)
        if not ar_for_salgs:
            print('Продажів за цей період немає')
            return False
        return ar_for_salgs

    def salgs_by_employee(self, employee_name):
        salgs = self.salg_service.get_salgs()
        return [salg for salg in salgs if salg["ansatt"] == employee_name]

    def top_selger(self, start_date=None, end_date=None):
        salgs = (
            self.salgs_by_period(start_date, end_date)
            if start_date and end_date
            else self.salg_service.get_salgs()
        )
        if not salgs:
            return None

        total_by_emp = {}

        for salg in salgs:
            total_by_emp[salg["ansatt"]] = total_by_emp.get(salg["ansatt"], 0) + int(salg["price"])
        top_name = max(total_by_emp, key=total_by_emp.get)
        total = total_by_emp[top_name]
        print(f"🏆 Найуспішніший продавець за період {start_date}–{end_date}: {top_name} (на {total} грн)")
        return top_name, total

    def total_profit(self, start, end):
        salgs = self.salgs_by_period(start, end)
        if not salgs:
            print("Продажів за цей період немає")
            return 0

        total_profit = 0
        cars = self.car_service.get_cars()

        for salg in salgs:
            car_name = salg["car"]
            car = next((cur_car for cur_car in cars if cur_car["car_name"] == car_name), None)
            if car:
                profit = int(salg["price"]) - int(car["selg_price"])
                total_profit += profit

        print(f"Загальний прибуток за період {start}–{end}: {total_profit} грн")
        return total_profit

    def best_selgers_car(self, start=None, end=None):
        salgs = self.salgs_by_period(start, end) if start and end else self.salg_service.get_salgs()
        if not salgs:
            print("Продажів за цей період немає")
            return None

        count_by_car = {}
        for salg in salgs:
            car = salg["car"]
            count_by_car[car] = count_by_car.get(car, 0) + 1

        top_car = max(count_by_car, key=count_by_car.get)
        print(f"Найпопулярніше авто за період {start}–{end}: {top_car} (продано {count_by_car[top_car]} шт.)")
        return top_car

    @staticmethod
    def export_to_file(data, filename="report.txt"):
        """Зберігає список словників або об’єктів у файл"""
        with open(filename, "w", encoding="utf-8") as f:
            for item in data:
                f.write(str(item) + "\n")
        print(f"Звіт збережено у файл: {filename}")