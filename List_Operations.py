# List Operations : 

employees = [
    "Ajay",
    "Rahul",
    "Priya",
    "Kiran",
    "Sneha"
]

print("Original List:", employees)

# Add item
employees.append("Surya")
print("After Adding:", employees)

# Remove item
employees.remove("Kiran")
print("After Removing:", employees)

# Sort list
employees.sort()
print("Sorted List:", employees)

# Reverse list
employees.reverse()
print("Reversed List:", employees)

# Find length
print("Length of List:", len(employees))

# Output :
# Original List: ['Ajay', 'Rahul', 'Priya', 'Kiran', 'Sneha']
# After Adding: ['Ajay', 'Rahul', 'Priya', 'Kiran', 'Sneha', 'Surya']
# After Removing: ['Ajay', 'Rahul', 'Priya', 'Sneha', 'Surya']
# Sorted List: ['Ajay', 'Priya', 'Rahul', 'Sneha', 'Surya']
# Reversed List: ['Surya', 'Sneha', 'Rahul', 'Priya', 'Ajay']
# Length of List: 5