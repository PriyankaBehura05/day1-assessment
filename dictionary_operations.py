# Create Dictionary

employee = {
    "id": 1,
    "name": "Ajay",
    "department": "AI",
    "salary": 50000
}

print("Original Dictionary:")
print(employee)

# Adding a new key
employee["email"] = "ajay@gmail.com"
print("\nAfter Adding Email:")
print(employee)

# Updating an existing key
employee["salary"] = 60000
print("\nAfter Updating Salary:")
print(employee)

# Deleting a key
del employee["department"]
print("\nAfter Deleting Department:")
print(employee)

# Iterating all values
print("\nDictionary Values:")
for value in employee.values():
    print(value)

# output
# Original Dictionary :
# {'id': 1, 'name': 'Ajay', 'department': 'AI', 'salary': 50000}

# After Adding Email:
# {'id': 1, 'name': 'Ajay', 'department': 'AI', 'salary': 50000, 'email': 'ajay@gmail.com'}

# After Updating Salary:
# {'id': 1, 'name': 'Ajay', 'department': 'AI', 'salary': 60000, 'email': 'ajay@gmail.com'}

# After Deleting Department:
# {'id': 1, 'name': 'Ajay', 'salary': 60000, 'email': 'ajay@gmail.com'}

# Dictionary Values:
# 1
# Ajay
# 60000
# ajay@gmail.com