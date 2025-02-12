class Company:
    """Represents a company with multiple employees."""

    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

    def __str__(self):
        return f"Company: {self.name}, Employees: {len(self.employees)}"
