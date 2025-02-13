# Employee Management System (Python) 🚀

## 📌 Project Overview
This is a **Python-based Employee Management System** that allows a company to manage its employees efficiently. The system supports different employee roles (**Developer, Tester, Manager**) and provides functionalities like **sorting employees, searching, filtering, handling exceptions, and logging**.

The project is built using **Object-Oriented Programming (OOP)**, follows **exception handling** best practices, and maintains **modular code structure** for scalability.

---

## 📂 Folder Structure

```
EmployeManagement/
│── customererror/        # Custom exception handling
│   ├── exceptions.py     # Defines EmployeeNotFoundException
│
│── entities/             # Defines Company & Employee classes
│   ├── company.py        # Company class (Manages employees)
│   ├── employee.py       # Employee, Developer, Tester, Manager classes
│
│── services/             # Service interfaces & implementations
│   ├── service.py        # Abstract class (Defines business methods)
│   ├── service_impl.py   # Implementation of business logic
│
│── utils/                # Utility configurations
│   ├── logger_config.py  # Configures logging
│
│── main.py               # Entry point (Handles input/output)
│── requirements.txt       # Dependencies (if needed)
│── .gitignore             # Ignore unnecessary files
```

---

## 🎯 **Key Features**
✔ **Employee Management** - Add & manage employees with different roles  
✔ **Sorting by Salary** - Employees sorted in **descending order**  
✔ **Filtering Employees** - Find **Selenium/UFT testers, unallocated developers, high-allowance managers**  
✔ **Finding Highly Paid Employees** - Returns top 5 based on salary + allowances  
✔ **Exception Handling** - Raises `EmployeeNotFoundException` for invalid employee searches  
✔ **Logging** - Logs key operations using Python’s logging module  
✔ **Loose Coupling & Abstraction** - Uses service interfaces for flexibility  

---

## 🛠️ **How It Works**

### **1️⃣ Employee & Subclasses**
- `Employee` (Base Class) → Contains **id, name, salary, designation**
- `Developer` → Additional **OTAllowance, NightShiftAllowance, Allocated**
- `Tester` → Additional **Selenium, UFT, JMeter skills, Test Allowance**
- `Manager` → Additional **Project Allowance, Number of Projects**

👉 **Why?** This structure ensures that **each role has unique attributes** while sharing common properties.

---

### **2️⃣ Company Class (Aggregation)**
- Holds a **list of employees** in a company  
- Provides methods like `add_employee()`, `get_employees()`  

👉 **Why?** This allows **efficient management of multiple employees** in a company.

---

### **3️⃣ Abstract Service Class (`ICompanyServiceProvider`)**
Defines **business methods** that need to be implemented:
- **Add employees**
- **Sort employees by salary**
- **Find employees by ID**
- **Filter employees based on skills, salary, and roles**
- **Get highly paid employees**

👉 **Why?** This ensures **loose coupling** and flexibility in implementation.

---

### **4️⃣ Implementation Class (`CompanyServiceProviderImpl`)**
Implements all methods from `ICompanyServiceProvider`:
- **Sorting Employees**
- **Searching Employees** (Raises Exception if not found)
- **Filtering Employees by Skills**
- **Finding Top 5 Paid Employees**
- **Logging All Operations**

👉 **Why?** Encapsulates **business logic** and separates concerns.

---

### **5️⃣ Exception Handling (`EmployeeNotFoundException`)**
- Raised when searching for an **invalid employee ID**  
- Handled in `main.py` to prevent program crashes  

---

### **6️⃣ Logging (`logger_config.py`)**
- Logs key **business operations** like adding employees, sorting, and searching.  
- Helps in debugging and **tracking application flow**.  

## 📌 **Expected Output**
```sh
🔹 Sorted Employees by Salary (Descending):
ID: 103, Name: Chandru, Salary: 120000, Designation: Manager, Project Allowance: 60000, Projects: 5
ID: 101, Name: Aro, Salary: 80000, Designation: Developer, OT Allowance: 5000, Night Shift Allowance: 2000, Allocated: False
ID: 102, Name: Barath, Salary: 75000, Designation: Tester, Selenium: True, UFT: False, JMeter: True, Test Allowance: 3000

INFO:root:Company Service Initialized.
INFO:root:Employee Added: Aro (ID: 101)
INFO:root:Employee Added: Barath (ID: 102)
INFO:root:Employee Added: Chandru (ID: 103)
INFO:root:Sorting employees by salary.
```

---

## 🧪 **Unit Testing**
To run unit tests:
```sh
python -m unittest discover tests
```
✔ **All test cases should pass successfully** ✅  

---

## 📜 **Conclusion**
This **Employee Management System** is designed to handle **employee operations efficiently** using **OOP, exception handling, and logging**. The modular structure ensures **scalability and flexibility** for future improvements.

📌 **For any questions or issues, feel free to open a GitHub issue.** 🚀  

---

### 📝 **Author**
👨‍💻 **[Aro]** - Python Developer  
🔗 GitHub: [github.com/cyber-bytezz](https://github.com/cyber-bytezz)  


