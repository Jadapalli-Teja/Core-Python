# ============================================================
# PYTHON TUPLE
# ============================================================


# 1. Creating a Tuple
numbers = (10, 20, 30, 40)

print(numbers)
# Output:
# (10, 20, 30, 40)


# 2. Type of Tuple
numbers = (10, 20, 30)

print(type(numbers))
# Output:
# <class 'tuple'>


# 3. Empty Tuple
empty = ()

print(empty)
print(type(empty))
# Output:
# ()
# <class 'tuple'>


# 4. Creating Tuple Using tuple()
numbers = tuple()

print(numbers)
print(type(numbers))
# Output:
# ()
# <class 'tuple'>


# 5. Single-Element Tuple
number = (10,)

print(number)
print(type(number))
# Output:
# (10,)
# <class 'tuple'>


# 6. Parentheses Without Comma
number = (10)

print(number)
print(type(number))
# Output:
# 10
# <class 'int'>


# 7. Tuple Without Parentheses
numbers = 10, 20, 30

print(numbers)
print(type(numbers))
# Output:
# (10, 20, 30)
# <class 'tuple'>


# 8. Tuple From List
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
# Output:
# (10, 20, 30)


# 9. Tuple From String
text = "Python"

result = tuple(text)

print(result)
# Output:
# ('P', 'y', 't', 'h', 'o', 'n')


# 10. Tuple From Set
numbers = {10, 20, 30}

result = tuple(numbers)

print(result)
# Output:
# Order may vary because sets are unordered.


# 11. Tuple From Dictionary
student = {
    "name": "Teja",
    "age": 21,
    "cgpa": 8.43
}

result = tuple(student)

print(result)
# Output:
# ('name', 'age', 'cgpa')


# 12. Tuple From Dictionary Values
student = {
    "name": "Teja",
    "age": 21
}

result = tuple(student.values())

print(result)
# Output:
# ('Teja', 21)


# 13. Tuple From Dictionary Items
student = {
    "name": "Teja",
    "age": 21
}

result = tuple(student.items())

print(result)
# Output:
# (('name', 'Teja'), ('age', 21))


# 14. Tuple From range()
numbers = tuple(range(1, 6))

print(numbers)
# Output:
# (1, 2, 3, 4, 5)


# 15. Tuple With Different Data Types
data = (10, 3.14, "Python", True, None)

print(data)
# Output:
# (10, 3.14, 'Python', True, None)


# 16. Tuple With Duplicate Values
numbers = (10, 20, 10, 30, 20)

print(numbers)
# Output:
# (10, 20, 10, 30, 20)


# 17. Positive Indexing
languages = ("Python", "Java", "C", "SQL")

print(languages[0])
print(languages[1])
print(languages[2])
print(languages[3])
# Output:
# Python
# Java
# C
# SQL


# 18. Negative Indexing
languages = ("Python", "Java", "C", "SQL")

print(languages[-1])
print(languages[-2])
print(languages[-3])
print(languages[-4])
# Output:
# SQL
# C
# Java
# Python


# 19. Tuple Slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
# Output:
# (20, 30, 40)


# 20. Tuple Slicing From Beginning
numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
# Output:
# (10, 20, 30)


# 21. Tuple Slicing Until End
numbers = (10, 20, 30, 40, 50)

print(numbers[2:])
# Output:
# (30, 40, 50)


# 22. Tuple Slicing With Step
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[::2])
# Output:
# (10, 30, 50)


# 23. Reverse Tuple Using Slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])
# Output:
# (50, 40, 30, 20, 10)


# 24. Tuple Length
numbers = (10, 20, 30, 40)

print(len(numbers))
# Output:
# 4


# 25. Membership Using in
numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 in numbers)
# Output:
# True
# False


# 26. Membership Using not in
numbers = (10, 20, 30, 40)

print(50 not in numbers)
print(20 not in numbers)
# Output:
# True
# False


# 27. Tuple Concatenation
a = (10, 20)
b = (30, 40)

result = a + b

print(result)
# Output:
# (10, 20, 30, 40)


# 28. Tuple Repetition
numbers = (10, 20)

result = numbers * 3

print(result)
# Output:
# (10, 20, 10, 20, 10, 20)


# 29. Tuple count()
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
# Output:
# 3


# 30. Tuple index()
numbers = (10, 20, 30, 20)

print(numbers.index(20))
# Output:
# 1


# 31. Tuple Iteration
numbers = (10, 20, 30)

for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30


# 32. Tuple Iteration With Index
languages = ("Python", "Java", "C")

for i in range(len(languages)):
    print(i, languages[i])

# Output:
# 0 Python
# 1 Java
# 2 C


# 33. Tuple With enumerate()
languages = ("Python", "Java", "C")

for index, language in enumerate(languages):
    print(index, language)

# Output:
# 0 Python
# 1 Java
# 2 C


# 34. Tuple Packing
student = "Teja", 21, 8.43

print(student)
# Output:
# ('Teja', 21, 8.43)


# 35. Tuple Unpacking
student = ("Teja", 21, 8.43)

name, age, cgpa = student

print(name)
print(age)
print(cgpa)

# Output:
# Teja
# 21
# 8.43


# 36. Extended Unpacking
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50


# 37. Unpacking With First Element
numbers = (10, 20, 30, 40)

first, *remaining = numbers

print(first)
print(remaining)

# Output:
# 10
# [20, 30, 40]


# 38. Unpacking With Last Element
numbers = (10, 20, 30, 40)

*remaining, last = numbers

print(remaining)
print(last)

# Output:
# [10, 20, 30]
# 40


# 39. Swapping Two Variables
a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Output:
# 20
# 10


# 40. Nested Tuple
numbers = (
    (10, 20),
    (30, 40)
)

print(numbers)
# Output:
# ((10, 20), (30, 40))


# 41. Accessing Nested Tuple
numbers = (
    (10, 20),
    (30, 40)
)

print(numbers[0])
print(numbers[0][1])
print(numbers[1][0])

# Output:
# (10, 20)
# 20
# 30


# 42. Tuple Containing a List
data = ([10, 20], 30)

print(data)
# Output:
# ([10, 20], 30)


# 43. Modifying Mutable List Inside Tuple
data = ([10, 20], 30)

data[0].append(40)

print(data)
# Output:
# ([10, 20, 40], 30)


# 44. Tuple Immutability
numbers = (10, 20, 30)

# The following statement is NOT allowed:
# numbers[0] = 100

# It produces:
# TypeError: 'tuple' object does not support item assignment


# 45. del Individual Tuple Element
numbers = (10, 20, 30)

# The following statement is NOT allowed:
# del numbers[0]

# It produces:
# TypeError


# 46. Deleting Entire Tuple
numbers = (10, 20, 30)

del numbers

# The variable numbers no longer exists.


# 47. Tuple Comparison
a = (10, 20, 30)
b = (10, 20, 30)

print(a == b)
# Output:
# True


# 48. Tuple Comparison - Order Matters
a = (10, 20)
b = (20, 10)

print(a == b)
# Output:
# False


# 49. Tuple Identity
a = (10, 20, 30)
b = a

print(a is b)
# Output:
# True


# 50. Tuple Equality vs Identity
a = (10, 20)
b = (10, 20)

print(a == b)
print(a is b)

# == checks values
# is checks object identity


# 51. Tuple Copy Using tuple()
numbers = (10, 20, 30)

new_numbers = tuple(numbers)

print(new_numbers)
# Output:
# (10, 20, 30)


# 52. Tuple Does Not Have copy()
numbers = (10, 20, 30)

# The following is NOT allowed:
# numbers.copy()

# Tuple has no copy() method.


# 53. hash() With Hashable Tuple
numbers = (10, 20, 30)

print(hash(numbers))
# Output:
# A hash value


# 54. Tuple As Dictionary Key
points = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print(points[(10, 20)])
# Output:
# Point A


# 55. Tuple As Set Element
points = {
    (10, 20),
    (30, 40)
}

print(points)
# Output:
# {(10, 20), (30, 40)}
# Order may vary.


# 56. sorted() With Tuple
numbers = (30, 10, 20)

result = sorted(numbers)

print(result)
print(type(result))

# Output:
# [10, 20, 30]
# <class 'list'>


# 57. Convert sorted Result Back to Tuple
numbers = (30, 10, 20)

result = tuple(sorted(numbers))

print(result)
# Output:
# (10, 20, 30)


# 58. min()
numbers = (40, 10, 30, 20)

print(min(numbers))
# Output:
# 10


# 59. max()
numbers = (40, 10, 30, 20)

print(max(numbers))
# Output:
# 40


# 60. sum()
numbers = (10, 20, 30, 40)

print(sum(numbers))
# Output:
# 100


# 61. any()
values = (False, False, True)

print(any(values))
# Output:
# True


# 62. all()
values = (True, True, True)

print(all(values))
# Output:
# True


# 63. Boolean Value of Empty Tuple
t = ()

print(bool(t))
# Output:
# False


# 64. Boolean Value of Non-Empty Tuple
t = (0,)

print(bool(t))
# Output:
# True


# 65. Function Returning Multiple Values
def calculate():
    return 10, 20


result = calculate()

print(result)
# Output:
# (10, 20)


# 66. Unpacking Function Return Values
def calculate():
    return 10, 20


a, b = calculate()

print(a)
print(b)

# Output:
# 10
# 20


# 67. Tuple Reassignment
numbers = (10, 20, 30)

numbers = (100, 200, 300)

print(numbers)
# Output:
# (100, 200, 300)


# 68. isinstance() With Tuple
numbers = (10, 20, 30)

print(isinstance(numbers, tuple))
# Output:
# True


# 69. Tuple Inside Tuple
data = (
    10,
    ("Python", "Java"),
    30
)

print(data)
# Output:
# (10, ('Python', 'Java'), 30)


# 70. Accessing Tuple Inside Tuple
data = (
    10,
    ("Python", "Java"),
    30
)

print(data[1])
print(data[1][0])
print(data[1][1])

# Output:
# ('Python', 'Java')
# Python
# Java


# ============================================================
# END OF PYTHON TUPLE
# ============================================================