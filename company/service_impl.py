import logging
from company.service import ICompanyServiceProvider
from company.exceptions import EmployeeNotFoundException
from company.employee import Tester, Developer, Manager

class CompanyServiceProviderImpl(ICompanyServiceProvider):

    def __init__(self, company):
        self.company = company
        logging.info("Company Service Initialized.")

    def add_employee(self, employee):
        self.company.add_employee(employee)
        logging.info(f"Employee Added: {employee.get_name()} (ID: {employee.get_emp_id()})")

    def return_sorted_list(self):
        logging.info("Sorting employees by salary (Descending).")
        return sorted(self.company.get_employees(), key=lambda e: e.get_salary(), reverse=True)

    def search_employee(self, emp_id):
        logging.info(f" Searching for Employee with ID: {emp_id}")
        for emp in self.company.get_employees():
            if emp.get_emp_id() == emp_id:
                logging.info(f"Employee Found: {emp.get_name()} (ID: {emp_id})")
                return emp
        logging.warning(f"⚠ Employee with ID {emp_id} Not Found!")
        raise EmployeeNotFoundException(emp_id)

    def return_selenium_testers(self):
        logging.info(" Finding Testers skilled in Selenium.")
        return [emp for emp in self.company.get_employees() if isinstance(emp, Tester) and emp._skilledInSelenium]

    def return_uft_testers(self):
        logging.info(" Finding Testers skilled in UFT.")
        return [emp for emp in self.company.get_employees() if isinstance(emp, Tester) and emp._skilledInUFT]

    def return_managers_with_high_allowance(self):
        logging.info(" Finding Managers with project allowance > 50,000.")
        return [emp for emp in self.company.get_employees() if
                isinstance(emp, Manager) and emp._projectAllowance > 50000]

    def return_unallocated_developers(self):
        logging.info(" Finding Developers who are not allocated to projects.")
        return [emp for emp in self.company.get_employees() if isinstance(emp, Developer) and not emp._allotted]

    def manager_with_max_projects(self):
        logging.info(" Finding Manager with the most projects.")
        return max((emp for emp in self.company.get_employees() if isinstance(emp, Manager)),
                   key=lambda e: e._numberOfProjects, default=None)

    def return_highly_paid_employees(self):
        logging.info(" Finding Top 5 highest-paid employees.")
        return sorted(self.company.get_employees(), key=lambda e: e.get_total_payment(), reverse=True)[:5]
