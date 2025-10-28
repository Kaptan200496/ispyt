from models.employee import Employee
from storage.storage import Storage

class EmployeeService:
    @staticmethod
    def get_employees():
        data = Storage.get_all(Employee.get_file_name())
        return data

    @staticmethod
    def add_employee(fio, position, tlf, email):
        new_employee = Employee(False,fio=fio, position=position, tlf=tlf, email=email)
        Storage.add_to_file(Employee.get_file_name(),new_employee)
        return new_employee

    @staticmethod
    def delete_by_id(id):
        Storage.delete_from_file(Employee.get_file_name(),id)

    @staticmethod
    def find_by_id(id):
        return Storage.find_in_file(Employee.get_file_name(), id)