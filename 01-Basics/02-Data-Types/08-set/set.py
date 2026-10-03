# ============================================================
# PYTHON SET
# ============================================================


# 1. Creating a Set
numbers = {10, 20, 30, 40}

print(numbers)
# Output:
# {10, 20, 30, 40}


# 2. Type of Set
numbers = {10, 20, 30}

print(type(numbers))
# Output:
# <class 'set'>


# 3. Empty Set
empty = set()

print(empty)
print(type(empty))
# Output:
# set()
# <class 'set'>


# 4. Empty {} Is Dictionary
empty = {}

print(type(empty))
# Output:
# <class 'dict'>


# 5. Duplicate Elements
numbers = {10, 20, 10, 30, 20, 40}

print(numbers)
# Output:
# {10, 20, 30, 40}


# 6. Set Using set()
numbers = set([10, 20, 30])

print(numbers)
# Output:
# {10, 20, 30}


# 7. List to Set
numbers = [10, 20, 10, 30, 20]

result = set(numbers)

print(result)
# Output:
# {10, 20, 30}


# 8. Tuple to Set
numbers = (10, 20, 10, 30)

result = set(numbers)

print(result)
# Output:
# {10, 20, 30}


# 9. String to Set
text = "hello"

result = set(text)

print(result)
# Output:
# Unique characters are stored.
# Order may vary.


# 10. Dictionary to Set
student = {
    "name": "Teja",
    "age": 21,
    "cgpa": 8.43
}

result = set(student)

print(result)
# Output:
# {'name', 'age', 'cgpa'}
# Order may vary.


# 11. Set With Different Data Types
data = {10, 3.14, "Python", True}

print(data)
# Output:
# Order may vary.


# 12. Set Cannot Store Duplicate Values
numbers = {10, 10, 10, 20, 20, 30}

print(numbers)
# Output:
# {10, 20, 30}


# 13. Set Does Not Support Indexing
numbers = {10, 20, 30}

# The following is NOT allowed:
# print(numbers[0])

# It produces:
# TypeError


# 14. Set Does Not Support Slicing
numbers = {10, 20, 30, 40}

# The following is NOT allowed:
# print(numbers[1:3])

# It produces:
# TypeError


# 15. Membership Using in
numbers = {10, 20, 30, 40}

print(20 in numbers)
print(50 in numbers)

# Output:
# True
# False


# 16. Membership Using not in
numbers = {10, 20, 30}

print(50 not in numbers)
print(20 not in numbers)

# Output:
# True
# False


# 17. add()
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
# Output:
# {10, 20, 30, 40}


# 18. add() Existing Element
numbers = {10, 20, 30}

numbers.add(20)

print(numbers)
# Output:
# {10, 20, 30}


# 19. add() Multiple Values?
numbers = {10, 20}

# add() accepts only one element.
# numbers.add(30, 40)

# This produces:
# TypeError


# 20. update()
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
# Output:
# {10, 20, 30, 40, 50}


# 21. update() With Tuple
numbers = {10, 20}

numbers.update((30, 40))

print(numbers)
# Output:
# {10, 20, 30, 40}


# 22. update() With String
letters = {"a", "b"}

letters.update("cd")

print(letters)
# Output:
# {'a', 'b', 'c', 'd'}
# Order may vary.


# 23. add() vs update()
numbers = {10, 20}

numbers.add((30, 40))

print(numbers)
# Output:
# {(30, 40), 10, 20}
# The tuple is added as ONE element.


numbers = {10, 20}

numbers.update((30, 40))

print(numbers)
# Output:
# {10, 20, 30, 40}
# Tuple elements are added separately.


# 24. remove()
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
# Output:
# {10, 30}


# 25. remove() With Missing Element
numbers = {10, 20, 30}

# numbers.remove(100)

# This produces:
# KeyError


# 26. discard()
numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
# Output:
# {10, 30}


# 27. discard() With Missing Element
numbers = {10, 20, 30}

numbers.discard(100)

print(numbers)
# Output:
# {10, 20, 30}

# No error occurs.


# 28. remove() vs discard()
numbers = {10, 20, 30}

# remove() → raises KeyError if element does not exist
# discard() → does not raise an error


# 29. pop()
numbers = {10, 20, 30}

value = numbers.pop()

print(value)
print(numbers)

# The removed element is arbitrary.
# Do not depend on which element is removed.


# 30. clear()
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
# Output:
# set()


# 31. Delete Entire Set
numbers = {10, 20, 30}

del numbers

# The variable numbers no longer exists.


# 32. len()
numbers = {10, 20, 30, 40}

print(len(numbers))
# Output:
# 4


# 33. Iterating Through a Set
numbers = {10, 20, 30}

for number in numbers:
    print(number)

# Output:
# Order may vary.


# 34. Union Using |
a = {10, 20, 30}
b = {30, 40, 50}

result = a | b

print(result)
# Output:
# {10, 20, 30, 40, 50}


# 35. Union Using union()
a = {10, 20, 30}
b = {30, 40, 50}

result = a.union(b)

print(result)
# Output:
# {10, 20, 30, 40, 50}


# 36. Union of Multiple Sets
a = {10, 20}
b = {20, 30}
c = {30, 40}

result = a.union(b, c)

print(result)
# Output:
# {10, 20, 30, 40}


# 37. Intersection Using &
a = {10, 20, 30}
b = {20, 30, 40}

result = a & b

print(result)
# Output:
# {20, 30}


# 38. Intersection Using intersection()
a = {10, 20, 30}
b = {20, 30, 40}

result = a.intersection(b)

print(result)
# Output:
# {20, 30}


# 39. Intersection of Multiple Sets
a = {10, 20, 30, 40}
b = {20, 30, 40, 50}
c = {30, 40, 60}

result = a.intersection(b, c)

print(result)
# Output:
# {30, 40}


# 40. Difference Using -
a = {10, 20, 30}
b = {20, 30, 40}

result = a - b

print(result)
# Output:
# {10}


# 41. Reverse Difference
a = {10, 20, 30}
b = {20, 30, 40}

result = b - a

print(result)
# Output:
# {40}


# 42. Difference Using difference()
a = {10, 20, 30}
b = {20, 30, 40}

result = a.difference(b)

print(result)
# Output:
# {10}


# 43. Symmetric Difference Using ^
a = {10, 20, 30}
b = {20, 30, 40}

result = a ^ b

print(result)
# Output:
# {10, 40}


# 44. Symmetric Difference Using Method
a = {10, 20, 30}
b = {20, 30, 40}

result = a.symmetric_difference(b)

print(result)
# Output:
# {10, 40}


# 45. Subset Using <=
a = {10, 20}
b = {10, 20, 30, 40}

print(a <= b)
# Output:
# True


# 46. Proper Subset Using <
a = {10, 20}
b = {10, 20, 30}

print(a < b)
# Output:
# True


# 47. Subset Using issubset()
a = {10, 20}
b = {10, 20, 30}

print(a.issubset(b))
# Output:
# True


# 48. Superset Using >=
a = {10, 20, 30, 40}
b = {10, 20}

print(a >= b)
# Output:
# True


# 49. Proper Superset Using >
a = {10, 20, 30}
b = {10, 20}

print(a > b)
# Output:
# True


# 50. Superset Using issuperset()
a = {10, 20, 30}
b = {10, 20}

print(a.issuperset(b))
# Output:
# True


# 51. Disjoint Sets
a = {10, 20}
b = {30, 40}

print(a.isdisjoint(b))
# Output:
# True


# 52. Non-Disjoint Sets
a = {10, 20}
b = {20, 30}

print(a.isdisjoint(b))
# Output:
# False


# 53. Set With Tuple
points = {
    (10, 20),
    (30, 40)
}

print(points)
# Output:
# {(10, 20), (30, 40)}
# Order may vary.


# 54. Set Cannot Contain List
# numbers = {[10, 20]}

# This produces:
# TypeError


# 55. Set Cannot Contain Dictionary
# data = {{"name": "Teja"}}

# This produces:
# TypeError


# 56. Hashable Tuple Inside Set
data = {
    (10, 20),
    (30, 40)
}

print(data)
# Output:
# {(10, 20), (30, 40)}


# 57. Tuple Containing List Cannot Be Set Element
# data = {([10, 20], 30)}

# This produces:
# TypeError


# 58. True and 1 in Set
data = {True, 1}

print(data)
print(len(data))

# Output:
# {True}
# 1

# True == 1


# 59. False and 0 in Set
data = {False, 0}

print(data)
print(len(data))

# Output:
# {False}
# 1

# False == 0


# 60. Removing Duplicates From List
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)
# Output:
# Unique values
# Order should not be relied upon.


# 61. Membership Checking
numbers = {10, 20, 30, 40, 50}

if 30 in numbers:
    print("30 is present")

# Output:
# 30 is present


# 62. Set Length After Duplicates
numbers = {10, 10, 20, 20, 30}

print(len(numbers))
# Output:
# 3


# 63. Set Comprehension
numbers = {1, 2, 3, 4, 5}

squares = {number * number for number in numbers}

print(squares)
# Output:
# {1, 4, 9, 16, 25}


# 64. Set Comprehension With Condition
numbers = {1, 2, 3, 4, 5, 6}

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)
# Output:
# {2, 4, 6}


# 65. Set From Range
numbers = set(range(1, 6))

print(numbers)
# Output:
# {1, 2, 3, 4, 5}


# 66. Set From Generator
numbers = set(number * 2 for number in range(1, 6))

print(numbers)
# Output:
# {2, 4, 6, 8, 10}


# 67. Set Copy Using copy()
numbers = {10, 20, 30}

new_numbers = numbers.copy()

print(new_numbers)
# Output:
# {10, 20, 30}


# 68. Set Copy Creates Separate Set
numbers = {10, 20, 30}

new_numbers = numbers.copy()

new_numbers.add(40)

print(numbers)
print(new_numbers)

# Output:
# {10, 20, 30}
# {10, 20, 30, 40}


# 69. Set Reference
numbers = {10, 20, 30}

new_numbers = numbers

new_numbers.add(40)

print(numbers)
print(new_numbers)

# Output:
# {10, 20, 30, 40}
# {10, 20, 30, 40}


# 70. Set Equality
a = {10, 20, 30}
b = {30, 20, 10}

print(a == b)

# Output:
# True

# Set order does not affect equality.


# 71. Set Identity
a = {10, 20, 30}
b = a

print(a is b)

# Output:
# True


# 72. Set Equality vs Identity
a = {10, 20, 30}
b = {10, 20, 30}

print(a == b)
print(a is b)

# == → compares values
# is → compares object identity


# 73. Boolean Value of Empty Set
numbers = set()

print(bool(numbers))
# Output:
# False


# 74. Boolean Value of Non-Empty Set
numbers = {10}

print(bool(numbers))
# Output:
# True


# 75. Set Inside if
numbers = {10, 20, 30}

if numbers:
    print("Set is not empty")

# Output:
# Set is not empty


# 76. isinstance() With Set
numbers = {10, 20, 30}

print(isinstance(numbers, set))
# Output:
# True


# ============================================================
# END OF PYTHON SET
# ============================================================