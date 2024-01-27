class Employee:
    emp_count = 0

    def __init__(self, firstname, lastname, sal, dept):
        self.firstname = firstname
        self.lastname = lastname
        self.sal = sal
        self.dept = dept
        Employee.emp_count += 1

    def emp_info(self):
        print(f"Name: {self.firstname} {self.lastname}, Salary: {self.sal}, Department: {self.dept}")

    @classmethod
    def avg_sal(cls, emp_list):
        total_salary = sum(emp.sal for emp in emp_list)
        return total_salary / len(emp_list) if len(emp_list) > 0 else 0

class FulltimeEmployee(Employee):
    ft_emp_count = 0

    def __init__(self, firstname, lastname, sal, dept, ben):
        super().__init__(firstname, lastname, sal, dept)  # Call the base class's __init__ method
        self.ben = ben
        FulltimeEmployee.ft_emp_count += 1

    def ft_emp_info(self):
        super().emp_info()
        print(f"Benefits: {self.ben}")

# Create instances of the Employee class
emp1 = Employee("SANJANA", "MORTHA", 500000, "IT")
emp2 = Employee("REVATHI", "JASTHI", 600000, "IT")
emp3 = Employee("AKHIL", "MARNEEDI", 100000, "HR")
emp4 = Employee("DEEPIKA", "RAMU", 100000, "HR")

# Print employee information
emp1.emp_info()
emp2.emp_info()
emp3.emp_info()
emp4.emp_info()

# Print total number of employees
print(f"Total number of employees: {Employee.emp_count}")

# Create instances of the FulltimeEmployee class
fulltime_employee1 = FulltimeEmployee("JAYADEEP", "NAGUBATHULA", 850000, "MANAGER", "Health Insurance")
fulltime_employee2 = FulltimeEmployee("JANA", "MOR", 800000, "PRODUCTION", "Provident fund")

# Print full-time employee information
fulltime_employee1.ft_emp_info()
fulltime_employee2.ft_emp_info()

# Print total number of employees and full-time employees
print(f"Total number of employees: {Employee.emp_count}")
print(f"Total number of full-time employees: {FulltimeEmployee.ft_emp_count}")

# Calculate and print average salary
emp_list = [emp1, emp2, emp3, emp4, fulltime_employee1, fulltime_employee2]
average_salary = Employee.avg_sal(emp_list)
print(f"Average Salary: {average_salary}")
