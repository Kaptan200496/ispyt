#Перший варіант
# Створити додаток для обліку продажу автомобілів в автосалоні. Основне
# завдання — обліковувати процес продажу автомобілів, фіксувати співробітника,
# який здійснив операцію, рахувати прибуток.
# Необхідно зберігати таку інформацію:
# Співробітник:
# ● ПІБ;
# ● Посада;
# ● Контактний телефон;
# ● Email.
# Автомобіль:
# ● Назва виробника;
# ● Рік випуску;
# ● Модель;
# ● Собівартість;
# ● Потенційна ціна продажу.
# Продажі:
# ● Співробітник;
# ● Автомобіль;
# ● Дата продажу;
# ● Реальна ціна продажу.

# Необхідно зберігати таку функціональність:
#1
# ● Додавання, видалення інформації про співробітників.
# ● Додавання, видалення інформації про автомобілі.
# ● Додавання, видалення інформації про продажі.
#2
# ● Звіти. Дані можуть виводитися на екран або у файл, залежно від вибору
# користувача:
#2/1
# ■ Повна інформація про співробітників фірми;
# ■ Повна інформація про автомобілі;
# ■ Повна інформація про продажі;
#2/2
# ■ Усі продажі за певну дату;
# ■ Усі продажі за певний період часу;
# ■ Усі продажі конкретного співробітника;
#2/3
# ■ Назва найбільш продаваного автомобіля за вказаний період часу;
# ■ Інформація про найуспішнішого торговця за вказаний період часу;
# ■ Сумарний прибуток за вказаний період часу.


# ● Збереження даних у файл.
# ● Завантаження даних із файлу.
# Правильне використання патернів проектування, принципів SOLID, механізмів
# тестування під час реалізації завдання дасть змогу отримати вищу оцінку.



from services.employee_service import EmployeeService
from services.car_service import CarService
from services.salg_service import SalgService
from reports.report_service import ReportService

emp_service = EmployeeService()
car_service = CarService()
salg_service = SalgService()
#add
#SalgService.add_salg("vova", "nisan", "21.01.2022","90000")
# EmployeeService.add_employee("zhenia pupkin tyt", "direktor", "068034561","bibiknik@gmail.com")
# CarService.add_car("toyota", "2021", "universal","190000","185000")
#get_all
EmployeeService.get_employees()
CarService.get_cars()
SalgService.get_salgs()
#delete
#EmployeeService.delete_by_id("89592bfe-db69-4966-ac4f-1356a769b37a")
#report
report_obj = ReportService(emp_service, car_service, salg_service)
by_date = report_obj.salgs_by_date("20.01.2021")
by_period = report_obj.salgs_by_period("10.02.1996","20.01.2021")
#EmployeeService.find_by_id("6c42e25f-7339-4387-9578-a87e30cbb6b4")
#report_obj.sales_by_employee("vova")
#print(by_period)
#print(report_obj.top_selger("21011997","21012019"))
#print(report_obj.total_profit("21011995","21012022"))
#print(report_obj.best_selgers_car("21011995","21012022"))
report_obj.export_to_file(report_obj.top_selger("21011995","21012022"),'report_best_selling')