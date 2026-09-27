# Python Boolean (bool) Examples


# 1. Boolean values

a = True
b = False

print(a)
print(b)

# Output:
# True
# False


# 2. Checking the type

print(type(True))
print(type(False))

# Output:
# <class 'bool'>
# <class 'bool'>


# 3. Boolean values from comparisons

print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
print(10 >= 10)
print(5 <= 3)

# Output:
# True
# False
# True
# False
# True
# False


# 4. Boolean expression

age = 21

result = age >= 18

print(result)
print(type(result))

# Output:
# True
# <class 'bool'>


# 5. Boolean with if

age = 21

if age >= 18:
    print("Adult")

# Output:
# Adult


# 6. bool() with numbers

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(10))

# Output:
# False
# True
# True
# True


# 7. bool() with floats

print(bool(0.0))
print(bool(2.5))
print(bool(-3.5))

# Output:
# False
# True
# True


# 8. bool() with strings

print(bool(""))
print(bool("Python"))
print(bool("False"))

# Output:
# False
# True
# True


# 9. bool() with collections

print(bool([]))
print(bool([1, 2, 3]))

print(bool(()))
print(bool((1, 2)))

print(bool({}))
print(bool({"name": "Teja"}))

print(bool(set()))
print(bool({1, 2, 3}))

# Output:
# False
# True
# False
# True
# False
# True
# False
# True


# 10. bool() with None

x = None

print(bool(x))

# Output:
# False


# 11. not operator

print(not True)
print(not False)

print(not 0)
print(not 10)

# Output:
# False
# True
# True
# False


# 12. and operator

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Output:
# True
# False
# False
# False


# 13. or operator

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Output:
# True
# True
# True
# False


# 14. and with actual values

print(10 and 20)
print(0 and 20)
print("Python" and "Java")
print("" and "Python")

# Output:
# 20
# 0
# Java
#


# 15. or with actual values

print(10 or 20)
print(0 or 20)
print("Python" or "Java")
print("" or "Python")

# Output:
# 10
# 20
# Python
# Python


# 16. Short-circuit with or

x = 10

result = x > 5 or x / 0

print(result)

# Output:
# True


# 17. Short-circuit with and

x = 0

result = x and (10 / 0)

print(result)

# Output:
# 0


# 18. Boolean in arithmetic

print(True + True)
print(True + False)
print(False + False)

# Output:
# 2
# 1
# 0


# 19. More Boolean arithmetic

print(True * 5)
print(False * 5)

print(True - False)
print(False - True)

# Output:
# 5
# 0
# 1
# -1


# 20. bool is a subclass of int

print(isinstance(True, int))
print(isinstance(False, int))

# Output:
# True
# True


# 21. True and False compared with integers

print(True == 1)
print(False == 0)

# Output:
# True
# True


# 22. Checking actual types

print(type(True))
print(type(1))

print(type(False))
print(type(0))

# Output:
# <class 'bool'>
# <class 'int'>
# <class 'bool'>
# <class 'int'>


# 23. sum() with Boolean values

values = [True, False, True, True]

print(sum(values))

# Output:
# 3


# 24. Chained comparison

age = 21

print(18 <= age <= 60)

# Output:
# True


# 25. Multiple conditions

age = 21
marks = 75

print(age >= 18 and marks >= 60)

# Output:
# True


# 26. Using or with conditions

age = 16
has_permission = True

print(age >= 18 or has_permission)

# Output:
# True


# 27. Checking whether a value is exactly True

value = True

print(value is True)

# Output:
# True


# 28. Boolean values are immutable

value = True

value = False

print(value)

# Output:
# False