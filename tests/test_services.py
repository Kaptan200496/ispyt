import unittest
from services.employee_service import EmployeeService
from models.employee import Employee

class TestEmployeeService(unittest.TestCase):
    def setUp(self):
        self.service = EmployeeService()

    def test_add_employee(self):
        emp = self.service.add_employee("Тест Тестович", "менеджер", "123", "test@mail.com")
        self.assertIsInstance(emp, Employee)

    def test_find_by_id(self):
        emp = self.service.add_employee("Тест Тестович", "менеджер", "123", "test@mail.com")
        found = self.service.find_by_id(emp.id)
        self.assertEqual(found.id, emp.id)

if __name__ == "__main__":
    unittest.main()