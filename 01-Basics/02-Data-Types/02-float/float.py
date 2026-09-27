# Python Float Examples


# 1. Creating float values

price = 99.50
temperature = 36.5
cgpa = 8.43
negative_value = -10.5
zero = 0.0

print(price)
print(temperature)
print(cgpa)
print(negative_value)
print(zero)

# Output:
# 99.5
# 36.5
# 8.43
# -10.5
# 0.0


# 2. Checking the type

x = 10.5

print(type(x))

# Output:
# <class 'float'>


# 3. Integer vs Float

a = 10
b = 10.0

print(type(a))
print(type(b))

# Output:
# <class 'int'>
# <class 'float'>


# 4. Scientific notation

x = 2e3
y = 1.5e2
z = 2.5e-3

print(x)
print(y)
print(z)

# Output:
# 2000.0
# 150.0
# 0.0025


# 5. Arithmetic operations

a = 10.5
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Output:
# 13.0
# 8.0
# 26.25
# 4.2


# 6. Integer and Float together

a = 10
b = 2.5

result = a + b

print(result)
print(type(result))

# Output:
# 12.5
# <class 'float'>


# 7. Converting Integer to Float

x = 10

result = float(x)

print(result)
print(type(result))

# Output:
# 10.0
# <class 'float'>


# 8. Converting String to Float

x = "25.5"

result = float(x)

print(result)
print(type(result))

# Output:
# 25.5
# <class 'float'>


# 9. Converting Float to Integer

x = 10.8

result = int(x)

print(result)

# Output:
# 10


# 10. Float does not round when converted to int

print(int(10.9))
print(int(10.2))
print(int(-10.8))

# Output:
# 10
# 10
# -10


# 11. Floating-point precision

result = 0.1 + 0.2

print(result)

# Output:
# 0.30000000000000004


# 12. Comparing floating-point values

print(0.1 + 0.2 == 0.3)

# Output:
# False


# 13. Using math.isclose()

import math

result = 0.1 + 0.2

print(math.isclose(result, 0.3))

# Output:
# True


# 14. Positive infinity

x = float("inf")

print(x)

# Output:
# inf


# 15. Negative infinity

x = float("-inf")

print(x)

# Output:
# -inf


# 16. NaN (Not a Number)

x = float("nan")

print(x)

# Output:
# nan


# 17. Checking whether a value is a float

x = 10.5

print(isinstance(x, float))

# Output:
# True