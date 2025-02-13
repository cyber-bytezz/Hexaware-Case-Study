import logging
from entities.company import Company
from entities.employee import Developer, Tester, Manager
from services.service_impl import CompanyServiceProviderImpl

# Configure logging
logging.basicConfig(level=logging.DEBUG)

company = Company("Hexaware")
service = CompanyServiceProviderImpl(company)

dev = Developer(101, "Aro", 80000, 5000, 2000, False)
tester = Tester(102, "Barath", 75000, True, False, True, 3000)
manager = Manager(103, "Chandru", 120000, 60000, 5)

service.add_employee(dev)
service.add_employee(tester)
service.add_employee(manager)

sorted_employees = service.return_sorted_list()
print("\n🔹 Sorted Employees by Salary (Descending):")
for emp in sorted_employees:
    print(emp)
