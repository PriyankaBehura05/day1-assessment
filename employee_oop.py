# Employee Class

class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.id = emp_i
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

    def annual_salary(self):
        return self.salary * 12




emp1 = Employee(1, "Ajay", "AI", 50000)
emp2 = Employee(2, "Rahul", "HR", 40000)
emp3 = Employee(3, "Priya", "Finance", 55000)

# # Employee Class

class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

    def annual_salary(self):
        return self.salary * 12


# Creating 3 Employee Objects

emp1 = Employee(1, "Ajay", "AI", 50000)
emp2 = Employee(2, "Rahul", "HR", 40000)
emp3 = Employee(3, "Priya", "Finance", 55000)

# Displaying Employee 1 Details
print("Employee 1")
emp1.display_details()
print("Annual Salary:", emp1.annual_salary())

print()

# Displaying Employee 2 Details
print("Employee 2")
emp2.display_details()
print("Annual Salary:", emp2.annual_salary())

print()

# Displaying Employee 3 Details
print("Employee 3")
emp3.display_details()
print("Annual Salary:", emp3.annual_salary())


print("Employee 1")
emp1.display_details()
print("Annual Salary:", emp1.annual_salary())

print()


print("Employee 2")
emp2.display_details()
print("Annual Salary:", emp2.annual_salary())

print()


print("Employee 3")
emp3.display_details()
print("Annual Salary:", emp3.annual_salary())
