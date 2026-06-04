# Exception Handeling handle errors without crashing the program using try-except.
# ZeroDivisionError

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ValueError

try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid number.")


# FileNotFoundError

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

# Output :
# Cannot divide by zero.
# Enter age: 21
# Age: 21
# File not found.