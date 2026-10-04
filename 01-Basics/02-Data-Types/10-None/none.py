# NoneType in Python


# 1. Creating None
x = None

print(x)
# Output:
# None


# 2. Type of None
print(type(x))
# Output:
# <class 'NoneType'>


# 3. None is a singleton
a = None
b = None

print(a is b)
# Output:
# True


# 4. Assigning None to a variable
name = None

print(name)
# Output:
# None


# 5. Reassigning a variable that contains None
name = None
name = "Teja"

print(name)
# Output:
# Teja


# 6. None vs 0
print(None == 0)
# Output:
# False


# 7. None vs False
print(None == False)
# Output:
# False


# 8. None vs empty string
print(None == "")
# Output:
# False


# 9. None vs empty list
print(None == [])
# Output:
# False


# 10. None vs empty dictionary
print(None == {})
# Output:
# False


# 11. Checking None using is
value = None

print(value is None)
# Output:
# True


# 12. Checking not None
value = 10

print(value is not None)
# Output:
# True


# 13. None using ==

value = None

print(value == None)
# Output:
# True

# Prefer:
# value is None


# 14. Boolean value of None
print(bool(None))
# Output:
# False


# 15. None in if condition
value = None

if value:
    print("Value exists")
else:
    print("No value")

# Output:
# No value


# 16. None in a list
data = [10, None, 30]

print(data)
# Output:
# [10, None, 30]


# 17. None in a tuple
data = (10, None, 30)

print(data)
# Output:
# (10, None, 30)


# 18. None in a set
data = {10, None, 20}

print(data)
# Output:
# Set contains None


# 19. None as dictionary value
student = {
    "name": "Teja",
    "marks": None
}

print(student)
# Output:
# {'name': 'Teja', 'marks': None}


# 20. None as dictionary key
data = {
    None: "No value"
}

print(data[None])
# Output:
# No value


# 21. Function without return
def greet():
    print("Hello")


result = greet()

print(result)

# Output:
# Hello
# None


# 22. Function explicitly returning None
def test():
    return None


result = test()

print(result)
# Output:
# None


# 23. Bare return
def check():
    return


result = check()

print(result)
# Output:
# None


# 24. Function returning None conditionally
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return number


result = find_number([10, 20, 30], 50)

print(result)
# Output:
# None


# 25. None as a placeholder
result = None

result = 100

print(result)
# Output:
# 100


# 26. Initializing multiple variables with None
name = None
age = None
marks = None

print(name, age, marks)
# Output:
# None None None


# 27. Default function argument as None
def greet(name=None):
    if name is None:
        print("No name provided")
    else:
        print("Hello", name)


greet()

# Output:
# No name provided


# 28. Default argument with a value
greet("Teja")

# Output:
# Hello Teja


# 29. print() returns None
result = print("Hello")

print(result)

# Output:
# Hello
# None


# 30. append() returns None
numbers = [10, 20]

result = numbers.append(30)

print(numbers)
print(result)

# Output:
# [10, 20, 30]
# None


# 31. Checking None inside a list
data = [10, None, 20]

print(None in data)
# Output:
# True


# 32. Removing None values from a list
data = [10, None, 20, None, 30]

result = [x for x in data if x is not None]

print(result)
# Output:
# [10, 20, 30]


# 33. None vs string "None"
a = None
b = "None"

print(a == b)
# Output:
# False


print(type(a))
print(type(b))

# Output:
# <class 'NoneType'>
# <class 'str'>


# 34. None vs undefined variable
x = None

print(x)
# Output:
# None

# x exists and contains None.


# 35. None is hashable
print(hash(None))
# Output:
# Hash value may vary between Python runs


# 36. None with isinstance()
x = None

print(isinstance(x, type(None)))
# Output:
# True


# 37. Search function returning None
def search(numbers, target):
    for number in numbers:
        if number == target:
            return number

    return None


result = search([10, 20, 30], 20)

if result is not None:
    print("Found:", result)
else:
    print("Not found")

# Output:
# Found: 20


# 38. Search when value is not present
result = search([10, 20, 30], 50)

if result is None:
    print("Not found")

# Output:
# Not found


# 39. None with conditional expression
value = None

message = "Available" if value is not None else "Not available"

print(message)
# Output:
# Not available


# 40. Difference between None and False
value = None

if value is None:
    print("Value is None")

if not value:
    print("Value is falsey")

# Output:
# Value is None
# Value is falsey