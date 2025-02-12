import unittest
from company.company import Company
from company.employee import Developer, Tester, Manager
from company.service_impl import CompanyServiceProviderImpl
from company.exceptions import EmployeeNotFoundException

class TestCompany(unittest.TestCase):

    def setUp(self):
        self.company = Company("TechCorp")
        self.service = CompanyServiceProviderImpl(self.company)

        self.dev = Developer(101, "Aro", 80000, 5000, 2000, False)
        self.tester = Tester(102, "Barath", 75000, True, False, True, 3000)
        self.manager = Manager(103, "Chandru", 120000, 60000, 5)

        self.service.add_employee(self.dev)
        self.service.add_employee(self.tester)
        self.service.add_employee(self.manager)

    def test_sorted_list(self):
        sorted_list = self.service.return_sorted_list()
        self.assertEqual(sorted_list[0].get_name(), "Chandru")  # Highest salary

    def test_search_employee(self):
        emp = self.service.search_employee(101)
        self.assertEqual(emp.get_name(), "Aro")

    def test_search_employee_not_found(self):
        with self.assertRaises(EmployeeNotFoundException):
            self.service.search_employee(999)  # Non-existent ID

    def test_highly_paid_employees(self):
        highly_paid = self.service.return_highly_paid_employees()
        self.assertEqual(len(highly_paid), 3)  # Only 3 employees exist

if __name__ == '__main__':
    unittest.main()
