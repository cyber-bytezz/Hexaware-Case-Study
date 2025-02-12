class EmployeeNotFoundException(Exception):
    """Raised when an employee is not found in the company."""

    def __init__(self, emp_id):
        super().__init__(f"Employee with ID {emp_id} not found.")
