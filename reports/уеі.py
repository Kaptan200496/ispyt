# reports/report_service.py
from datetime import datetime

class ReportService:
    def __init__(self, employee_service, car_service, sale_service):
        self.employee_service = employee_service
        self.car_service = car_service
        self.sale_service = sale_service

    # 1️⃣ Повна інформація
    def all_employees(self):
        return self.employee_service.get_all()

    def all_cars(self):
        return self.car_service.get_all()

    def all_sales(self):
        return self.sale_service.get_all()

    # 2️⃣ Продажі за певну дату
    def sales_by_date(self, date_str):
        """Формат дати: 'YYYY-MM-DD'"""
        sales = self.sale_service.get_all()
        return [s for s in sales if s.date == date_str]

    # 3️⃣ Продажі за період
    def sales_by_period(self, start_date, end_date):
        """Формат дат: 'YYYY-MM-DD'"""
        sales = self.sale_service.get_all()
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        return [s for s in sales if start <= datetime.strptime(s.date, "%Y-%m-%d").date() <= end]

    # 4️⃣ Продажі конкретного співробітника
    def sales_by_employee(self, employee_id):
        sales = self.sale_service.get_all()
        return [s for s in sales if s.employee_id == employee_id]

    # 5️⃣ Найпопулярніше авто за період
    def best_selling_car(self, start_date=None, end_date=None):
        sales = self.sales_by_period(start_date, end_date) if start_date and end_date else self.sale_service.get_all()
        if not sales:
            return None
        counter = {}
        for s in sales:
            counter[s.car_id] = counter.get(s.car_id, 0) + 1
        top_car_id = max(counter, key=counter.get)
        car = self.car_service.find_by_id(top_car_id)
        return car

    # 6️⃣ Найуспішніший продавець
    def top_seller(self, start_date=None, end_date=None):
        sales = self.sales_by_period(start_date, end_date) if start_date and end_date else self.sale_service.get_all()
        if not sales:
            return None
        total_by_emp = {}
        for s in sales:
            total_by_emp[s.employee_id] = total_by_emp.get(s.employee_id, 0) + s.actual_price
        top_emp_id = max(total_by_emp, key=total_by_emp.get)
        employee = self.employee_service.find_by_id(top_emp_id)
        total_sales = total_by_emp[top_emp_id]
        return employee, total_sales

    # 7️⃣ Сумарний прибуток за період
    def total_profit(self, start_date, end_date):
        sales = self.sales_by_period(start_date, end_date)
        profit = 0
        for s in sales:
            car = self.car_service.find_by_id(s.car_id)
            profit += s.actual_price - car.cost_price
        return profit