# Python Lists


# 1. Creating a List Using []

numbers = [10, 20, 30, 40]

print(numbers)

# Output:
# [10, 20, 30, 40]


# 2. Checking List Type

print(type(numbers))

# Output:
# <class 'list'>


# 3. Creating an Empty List

items = []

print(items)
print(len(items))

# Output:
# []
# 0


# 4. Creating an Empty List Using list()

items = list()

print(items)
print(type(items))

# Output:
# []
# <class 'list'>


# 5. Creating a List From a String

word = "Python"

letters = list(word)

print(letters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# 6. Creating a List From a Tuple

data = (10, 20, 30)

numbers = list(data)

print(numbers)

# Output:
# [10, 20, 30]


# 7. Creating a List From a Set

data = {10, 20, 30}

numbers = list(data)

print(numbers)

# Output:
# [10, 20, 30]


# 8. Creating a List From a Dictionary

student = {
    "name": "Teja",
    "age": 21
}

keys = list(student)

print(keys)

# Output:
# ['name', 'age']


# 9. Creating a List From Dictionary Values

values = list(student.values())

print(values)

# Output:
# ['Teja', 21]


# 10. Creating a List From Dictionary Items

items = list(student.items())

print(items)

# Output:
# [('name', 'Teja'), ('age', 21)]


# 11. Creating a List From range()

numbers = list(range(1, 6))

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# 12. range() With Step

numbers = list(range(0, 10, 2))

print(numbers)

# Output:
# [0, 2, 4, 6, 8]


# 13. Different Data Types in a List

data = [10, 3.14, "Python", True]

print(data)

# Output:
# [10, 3.14, 'Python', True]


# 14. Nested List

data = [
    10,
    "Python",
    [1, 2, 3]
]

print(data)

# Output:
# [10, 'Python', [1, 2, 3]]


# 15. Duplicate Values

numbers = [10, 20, 10, 30, 10]

print(numbers)

# Output:
# [10, 20, 10, 30, 10]


# 16. Positive Indexing

numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[1])
print(numbers[3])

# Output:
# 10
# 20
# 40


# 17. Negative Indexing

print(numbers[-1])
print(numbers[-2])
print(numbers[-4])

# Output:
# 40
# 30
# 10


# 18. List Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Output:
# [20, 30, 40]


# 19. Slicing With Step

print(numbers[0:5:2])

# Output:
# [10, 30, 50]


# 20. Omitting Start

print(numbers[:3])

# Output:
# [10, 20, 30]


# 21. Omitting Stop

print(numbers[2:])

# Output:
# [30, 40, 50]


# 22. Copying Using Slicing

copy_list = numbers[:]

print(copy_list)

# Output:
# [10, 20, 30, 40, 50]


# 23. Reversing Using Slicing

print(numbers[::-1])

# Output:
# [50, 40, 30, 20, 10]


# 24. Changing an Element

numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)

# Output:
# [10, 200, 30]


# 25. Changing Multiple Elements Using Slicing

numbers = [10, 20, 30, 40]

numbers[1:3] = [200, 300]

print(numbers)

# Output:
# [10, 200, 300, 40]


# 26. Replacing Multiple Elements With Different Size

numbers = [10, 20, 30, 40]

numbers[1:3] = [200, 300, 400]

print(numbers)

# Output:
# [10, 200, 300, 400, 40]


# 27. append()

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# Output:
# [10, 20, 30, 40]


# 28. append() Adds One Object

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

# Output:
# [1, 2, [3, 4]]


# 29. insert()

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)

# Output:
# [10, 15, 20, 30]


# 30. extend()

numbers = [10, 20]

numbers.extend([30, 40, 50])

print(numbers)

# Output:
# [10, 20, 30, 40, 50]


# 31. extend() With a String

letters = ["A", "B"]

letters.extend("CD")

print(letters)

# Output:
# ['A', 'B', 'C', 'D']


# 32. append() vs extend()

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

# Output:
# [1, 2, [3, 4]]

numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)

# Output:
# [1, 2, 3, 4]


# 33. List Concatenation

a = [1, 2, 3]
b = [4, 5, 6]

result = a + b

print(result)

# Output:
# [1, 2, 3, 4, 5, 6]


# 34. List Repetition

numbers = [1, 2]

print(numbers * 3)

# Output:
# [1, 2, 1, 2, 1, 2]


# 35. Membership Operators

numbers = [10, 20, 30]

print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)

# Output:
# True
# False
# True


# 36. len()

numbers = [10, 20, 30, 40]

print(len(numbers))

# Output:
# 4


# 37. remove()

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

# Output:
# [10, 30, 20]


# 38. pop() Without Index

numbers = [10, 20, 30]

value = numbers.pop()

print(value)
print(numbers)

# Output:
# 30
# [10, 20]


# 39. pop() With Index

numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
print(numbers)

# Output:
# 20
# [10, 30]


# 40. clear()

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

# Output:
# []


# 41. del With Index

numbers = [10, 20, 30]

del numbers[1]

print(numbers)

# Output:
# [10, 30]


# 42. del With Slice

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)

# Output:
# [10, 50]


# 43. index()

numbers = [10, 20, 30, 20]

print(numbers.index(20))

# Output:
# 1


# 44. count()

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

# Output:
# 3


# 45. sort()

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30, 40]


# 46. sort() in Descending Order

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# Output:
# [40, 30, 20, 10]


# 47. sorted()

numbers = [30, 10, 20]

result = sorted(numbers)

print(result)
print(numbers)

# Output:
# [10, 20, 30]
# [30, 10, 20]


# 48. sort() vs sorted()

numbers = [30, 10, 20]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30]

numbers = [30, 10, 20]

result = sorted(numbers)

print(result)
print(numbers)

# Output:
# [10, 20, 30]
# [30, 10, 20]


# 49. reverse()

numbers = [10, 20, 30]

numbers.reverse()

print(numbers)

# Output:
# [30, 20, 10]


# 50. reverse() vs Slicing

numbers = [10, 20, 30]

result = numbers[::-1]

print(result)
print(numbers)

# Output:
# [30, 20, 10]
# [10, 20, 30]


# 51. copy()

numbers = [10, 20, 30]

new_numbers = numbers.copy()

numbers.append(40)

print(numbers)
print(new_numbers)

# Output:
# [10, 20, 30, 40]
# [10, 20, 30]


# 52. list() as a Copy

numbers = [10, 20, 30]

new_numbers = list(numbers)

numbers.append(40)

print(numbers)
print(new_numbers)

# Output:
# [10, 20, 30, 40]
# [10, 20, 30]


# 53. Reference Assignment

a = [10, 20, 30]
b = a

a.append(40)

print(a)
print(b)

# Output:
# [10, 20, 30, 40]
# [10, 20, 30, 40]


# 54. copy() Creates a Separate List

a = [10, 20, 30]
b = a.copy()

a.append(40)

print(a)
print(b)

# Output:
# [10, 20, 30, 40]
# [10, 20, 30]


# 55. Checking Identity

a = [10, 20]
b = a
c = a.copy()

print(a is b)
print(a is c)

# Output:
# True
# False


# 56. Checking Equality

a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)

# Output:
# True
# False


# 57. Nested List

matrix = [
    [1, 2],
    [3, 4]
]

print(matrix)
print(matrix[0])
print(matrix[0][1])

# Output:
# [[1, 2], [3, 4]]
# [1, 2]
# 2


# 58. Changing Nested List

matrix = [
    [1, 2],
    [3, 4]
]

matrix[0][1] = 200

print(matrix)

# Output:
# [[1, 200], [3, 4]]


# 59. Shallow Copy

a = [[1, 2], [3, 4]]

b = a.copy()

a[0].append(100)

print(a)
print(b)

# Output:
# [[1, 2, 100], [3, 4]]
# [[1, 2, 100], [3, 4]]


# 60. Iterating Through a List

numbers = [10, 20, 30]

for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30


# 61. Iterating Using Index

numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(i, numbers[i])

# Output:
# 0 10
# 1 20
# 2 30


# 62. enumerate()

names = ["Teja", "Ravi", "Kiran"]

for index, name in enumerate(names):
    print(index, name)

# Output:
# 0 Teja
# 1 Ravi
# 2 Kiran


# 63. List Comprehension

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# 64. List Comprehension With Condition

numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x % 2 == 0]

print(even)

# Output:
# [2, 4, 6]


# 65. List Unpacking

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

# Output:
# 10
# 20
# 30


# 66. Extended Unpacking

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50


# 67. Boolean Value of an Empty List

numbers = []

print(bool(numbers))

# Output:
# False


# 68. Boolean Value of a Non-empty List

numbers = [10]

print(bool(numbers))

# Output:
# True


# 69. List in if Condition

numbers = []

if numbers:
    print("List is not empty")
else:
    print("List is empty")

# Output:
# List is empty


# 70. isinstance()

numbers = [10, 20, 30]

print(isinstance(numbers, list))

# Output:
# True


# 71. List Method Return Value

numbers = [10, 20]

result = numbers.append(30)

print(result)
print(numbers)

# Output:
# None
# [10, 20, 30]