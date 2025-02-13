import logging
from services.service import ICompanyServiceProvider
from customerror.exceptions import EmployeeNotFoundException
from entities.employee import Tester, Developer, Manager


class CompanyServiceProviderImpl(ICompanyServiceProvider):
    """Implements business logic for managing employees in a company."""

    def __init__(self, company):
        self.company = company
        logging.info("Company Service Initialized.")

    def add_employee(self, employee):
        """Adds an employee to the company."""
        self.company.add_employee(employee)
        logging.info(f"Employee Added: {employee.get_name()} (ID: {employee.get_emp_id()})")

    def return_sorted_list(self):
        """Returns employees sorted by salary in descending order."""
        logging.info("Sorting employees by salary.")
        return sorted(self.company.get_employees(), key=lambda e: e.get_salary(), reverse=True)

    def search_employee(self, emp_id):
        """Searches for an employee by ID or raises an exception if not found."""
        logging.info(f"Searching for Employee ID: {emp_id}")
        for emp in self.company.get_employees():
            if emp.get_emp_id() == emp_id:
                return emp
        logging.warning(f"⚠ Employee with ID {emp_id} Not Found!")
        raise EmployeeNotFoundException(emp_id)

    def return_selenium_testers(self):
        """Returns all testers skilled in Selenium."""
        return [emp for emp in self.company.get_employees() if isinstance(emp, Tester) and emp._skilledInSelenium]

    def return_uft_testers(self):
        """Returns all testers skilled in UFT."""
        return [emp for emp in self.company.get_employees() if isinstance(emp, Tester) and emp._skilledInUFT]

    def return_managers_with_high_allowance(self):
        """Returns managers with project allowance > 50,000."""
        return [emp for emp in self.company.get_employees() if
                isinstance(emp, Manager) and emp._projectAllowance > 50000]

    def return_unallocated_developers(self):
        """Returns developers not assigned to any projects."""
        return [emp for emp in self.company.get_employees() if isinstance(emp, Developer) and not emp._allotted]

    def manager_with_max_projects(self):
        """Returns the manager handling the highest number of projects."""
        return max((emp for emp in self.company.get_employees() if isinstance(emp, Manager)),
                   key=lambda e: e._numberOfProjects, default=None)

    def return_highly_paid_employees(self):
        """Returns the top 5 highest-paid employees."""
        return sorted(self.company.get_employees(), key=lambda e: e.get_total_payment(), reverse=True)[:5]
