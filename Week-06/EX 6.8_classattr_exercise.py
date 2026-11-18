# Programmer: Arash
# Date: 11-18-2026
# Purpose: Manage employee information and bonuses.
# Instructor: Deodat Sharma

class Employee:
    company = "DataPlus Analytics"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print("\nEmployee Information")
        print("-" * 30)
        print(f"Company: {Employee.company}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Annual bonus: ${self.annual_bonus():,.2f}")
        print("-" * 30)

    def annual_bonus(self):
        return self.salary * 0.10

print("Enter information for employee 1:")
employee1 = Employee(
    input("Name: "),
    input("Department: "),
    float(input("Salary: "))
)

print("-" * 30)
print("Enter information for employee 2:")
employee2 = Employee(
    input("Name: "),
    input("Department: "),
    float(input("Salary: "))
)

employee1.display_info()
employee2.display_info()



