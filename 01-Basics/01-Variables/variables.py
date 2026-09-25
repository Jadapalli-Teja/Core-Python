# Variables

name = "Teja"
age = 21
cgpa = 8.43

print(name)
print(age)
print(cgpa)

# Output:
# Teja
# 21
# 8.43


# Multiple assignment

a, b, c = 10, 20, 30

print(a, b, c)

# Output:
# 10 20 30


# Same value to multiple variables

x = y = z = 100

print(x, y, z)

# Output:
# 100 100 100


# Dynamic typing

value = 10
print(value, type(value))

value = "Python"
print(value, type(value))

# Output:
# 10 <class 'int'>
# Python <class 'str'>


# Reassigning a variable

marks = 80
marks = 95

print(marks)

# Output:
# 95


# Swapping two variables

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Output:
# 20
# 10


# Checking type

student_name = "Teja"
student_age = 21

print(type(student_name))
print(type(student_age))

# Output:
# <class 'str'>
# <class 'int'>


# Checking object identity

x = 100
y = x

print(x == y)
print(x is y)

# Output:
# True
# True


# Constants

PI = 3.14159
MAX_MARKS = 100

print(PI)
print(MAX_MARKS)

# Output:
# 3.14159
# 100


# Global and local variables

college = "NBKR"

def display():
    branch = "CSE"
    print(college)
    print(branch)

display()

# Output:
# NBKR
# CSE