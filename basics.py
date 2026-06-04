# Variables :
name = "Priyanka"
age = 21
email = "priyanka@example.com"
salary = 50000
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Salary: {salary}")


# output:
# Name: Priyanka
# Age: 21
# Email: priyanka@example.com
# Salary: 50000

# datatypes :
text = "Hello , i am a fresher "                  # str
number = 25                   # int
price = 95.6                  # float
is_active = True                # bool
skills = ["Python", "AI","ML"]       # list
coordinates = (10, 20)          # tuple
student = {"name": "Priyanka"}     # dict
unique_numbers = {1, 2, 3}      # set

print(type(text))
print(type(number))
print(type(price))
print(type(is_active))
print(type(skills))
print(type(coordinates))
print(type(student))
print(type(unique_numbers))


# Output :
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# <class 'set'>


# Operators  :

a = 20
b = 6

print("Number 1:", a)
print("Number 2:", b)

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Modulus
print("Modulus:", a % b)

# Output:

# Number 1: 20
# Number 2: 6
# Addition: 26
# Subtraction: 14
# Multiplication: 120
# Division: 3.3333333333333335
# Modulus: 2

# Conditional Statements :
age = int(input("Enter your age: "))
if age < 18 :
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
# output:
# Enter your age: 21
# Adult

# using for loop :
print("Numbers from 1 to 50 : ")

for i in range(1, 51):    # range(start, stop)  stop value is not included 

    print(i , end=' ') 
# output :
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50

# using while loop :
print("Numbers from 1 to 50: ")

num = 1

while num <= 50:
    print(num , end=' ')
    num += 1 
#output :
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 4546 47 48 49 50 