from abc import ABC, abstractmethod

class ICompanyServiceProvider(ABC):
    """Abstract class defining employee management services."""
    @abstractmethod
    def add_employee(self, employee):
        pass
    @abstractmethod
    def return_sorted_list(self):
        pass
    @abstractmethod
    def search_employee(self, emp_id):
        pass
    @abstractmethod
    def return_selenium_testers(self):
        pass
    @abstractmethod
    def return_uft_testers(self):
        pass
    @abstractmethod
    def return_managers_with_high_allowance(self):
        pass
    @abstractmethod
    def return_unallocated_developers(self):
        pass
    @abstractmethod
    def manager_with_max_projects(self):
        pass
    @abstractmethod
    def return_highly_paid_employees(self):
        pass
