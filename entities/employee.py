class Employee:
    """Base class for all employees."""
    def __init__(self, emp_id, name, salary, designation):
        self._emp_id = emp_id
        self._name = name
        self._salary = salary
        self._designation = designation

    def get_emp_id(self): return self._emp_id
    def get_name(self): return self._name
    def get_salary(self): return self._salary
    def get_designation(self): return self._designation
    def set_salary(self, salary): self._salary = salary

    def __str__(self):
        return f"ID: {self._emp_id}, Name: {self._name}, Salary: {self._salary}, Designation: {self._designation}"

class Developer(Employee):
    def __init__(self, emp_id, name, salary, OTAllowance, NightShiftAllowance, allotted):
        super().__init__(emp_id, name, salary, "Developer")
        self._OTAllowance = OTAllowance
        self._NightShiftAllowance = NightShiftAllowance
        self._allotted = allotted

    def get_total_payment(self):
        return self._salary + self._OTAllowance + self._NightShiftAllowance

    def __str__(self):
        return super().__str__() + f", OT Allowance: {self._OTAllowance}, Night Shift Allowance: {self._NightShiftAllowance}, Allocated: {self._allotted}"

class Tester(Employee):
    def __init__(self, emp_id, name, salary, skilledInSelenium, skilledInUFT, skilledInJemeter, testAllowance):
        super().__init__(emp_id, name, salary, "Tester")
        self._skilledInSelenium = skilledInSelenium
        self._skilledInUFT = skilledInUFT
        self._skilledInJemeter = skilledInJemeter
        self._testAllowance = testAllowance

    def get_total_payment(self):
        return self._salary + self._testAllowance

    def __str__(self):
        return super().__str__() + f", Selenium: {self._skilledInSelenium}, UFT: {self._skilledInUFT}, JMeter: {self._skilledInJemeter}, Test Allowance: {self._testAllowance}"

class Manager(Employee):
    def __init__(self, emp_id, name, salary, projectAllowance, numberOfProjects):
        super().__init__(emp_id, name, salary, "Manager")
        self._projectAllowance = projectAllowance
        self._numberOfProjects = numberOfProjects

    def get_total_payment(self):
        return self._salary + self._projectAllowance

    def __str__(self):
        return super().__str__() + f", Project Allowance: {self._projectAllowance}, Projects: {self._numberOfProjects}"
