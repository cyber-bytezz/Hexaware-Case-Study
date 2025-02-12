import logging
from company.company import Company
from company.employee import Developer, Tester, Manager
from company.service_impl import CompanyServiceProviderImpl

# Allows DEBUG messages to appear
logging.basicConfig(level=logging.DEBUG)

company = Company("Hexaware")
service = CompanyServiceProviderImpl(company)

dev = Developer(101, "Aro", 80000, 5000, 2000, False)
tester = Tester(102, "Barath", 75000, True, False, True, 3000)
manager = Manager(103, "Chandru", 120000, 60000, 5)

service.add_employee(dev)
service.add_employee(tester)
service.add_employee(manager)

# Print sorted employee list in readable format
sorted_employees = service.return_sorted_list()
print("\n🔹 Sorted Employees by Salary (Descending):")
for emp in sorted_employees:
    print(emp)  # This will use the __str__ method of each class
