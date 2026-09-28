# Python Strings


# 1. Creating Strings

name = "Teja"
city = 'Nellore'

print(name)
print(city)

# Output:
# Teja
# Nellore


# 2. Checking String Type

text = "Python"

print(type(text))

# Output:
# <class 'str'>


# 3. String Containing Numbers

age = "21"
number = 100

print(age)
print(type(age))
print(type(number))

# Output:
# 21
# <class 'str'>
# <class 'int'>


# 4. Empty String

empty = ""

print(empty)
print(len(empty))
print(bool(empty))

# Output:
#
# 0
# False


# 5. Multi-line String

message = """Hello
Welcome to Python
Learning Strings"""

print(message)

# Output:
# Hello
# Welcome to Python
# Learning Strings


# 6. Escape Sequences

print("Hello\nPython")
print("Hello\tPython")
print("C:\\Users\\Teja")

# Output:
# Hello
# Python
# Hello    Python
# C:\Users\Teja


# 7. Raw String

path = r"C:\Users\Teja\Python"

print(path)

# Output:
# C:\Users\Teja\Python


# 8. Positive Indexing

word = "Python"

print(word[0])
print(word[1])
print(word[5])

# Output:
# P
# y
# n


# 9. Negative Indexing

print(word[-1])
print(word[-2])
print(word[-6])

# Output:
# n
# o
# P


# 10. String Slicing

print(word[0:3])
print(word[2:6])
print(word[:3])
print(word[2:])
print(word[:])

# Output:
# Pyt
# thon
# Pyt
# thon
# Python


# 11. Slicing With Step

print(word[0:6:2])

# Output:
# Pto


# 12. Reverse String

print(word[::-1])

# Output:
# nohtyP


# 13. String Concatenation

first = "Hello"
second = "Python"

result = first + " " + second

print(result)

# Output:
# Hello Python


# 14. String Repetition

print("Hi " * 3)
print("-" * 10)

# Output:
# Hi Hi Hi
# ----------


# 15. Membership Operators

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)

# Output:
# True
# False
# True


# 16. len() Function

word = "Python"

print(len(word))

# Output:
# 6


# 17. String Immutability

word = "Python"

# word[0] = "J"     # TypeError

word = "J" + word[1:]

print(word)

# Output:
# Jython


# 18. lower()

text = "Python"

print(text.lower())

# Output:
# python


# 19. upper()

print(text.upper())

# Output:
# PYTHON


# 20. capitalize()

text = "python programming"

print(text.capitalize())

# Output:
# Python programming


# 21. title()

print(text.title())

# Output:
# Python Programming


# 22. strip()

text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Output:
# Python
# Python
#    Python


# 23. replace()

text = "I like Java"

result = text.replace("Java", "Python")

print(result)

# Output:
# I like Python


# 24. split()

text = "Python is easy"

words = text.split()

print(words)

# Output:
# ['Python', 'is', 'easy']


# 25. split() With Separator

data = "apple,banana,mango"

print(data.split(","))

# Output:
# ['apple', 'banana', 'mango']


# 26. join()

words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)

# Output:
# Python is easy


# 27. find()

text = "Python Programming"

print(text.find("Python"))
print(text.find("Java"))

# Output:
# 0
# -1


# 28. index()

print(text.index("Python"))

# Output:
# 0

# text.index("Java")    # ValueError


# 29. count()

text = "banana"

print(text.count("a"))

# Output:
# 3


# 30. startswith()

text = "Python Programming"

print(text.startswith("Python"))
print(text.startswith("Java"))

# Output:
# True
# False


# 31. endswith()

print(text.endswith("Programming"))
print(text.endswith("Python"))

# Output:
# True
# False


# 32. isalpha()

print("Python".isalpha())
print("Python123".isalpha())

# Output:
# True
# False


# 33. isdigit()

print("12345".isdigit())
print("123abc".isdigit())

# Output:
# True
# False


# 34. isalnum()

print("Python123".isalnum())
print("Python 123".isalnum())

# Output:
# True
# False


# 35. isspace()

print("   ".isspace())
print("Python".isspace())

# Output:
# True
# False


# 36. String Comparison

a = "apple"
b = "apple"

print(a == b)
print("apple" < "banana")

# Output:
# True
# True


# 37. String Conversion

age = 21

result = str(age)

print(result)
print(type(result))

# Output:
# 21
# <class 'str'>


# 38. f-Strings

name = "Teja"
age = 21

print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is Teja and I am 21 years old.


# 39. Expression Inside f-String

a = 10
b = 20

print(f"Sum = {a + b}")

# Output:
# Sum = 30


# 40. Formatting Numbers

price = 99.5678

print(f"{price:.2f}")

# Output:
# 99.57


# 41. Iterating Through a String

word = "Python"

for char in word:
    print(char)

# Output:
# P
# y
# t
# h
# o
# n


# 42. enumerate() With String

word = "Python"

for index, char in enumerate(word):
    print(index, char)

# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n


# 43. Unicode Strings

name = "Teja"
language = "తెలుగు"
emoji = "😀"

print(name)
print(language)
print(emoji)

# Output:
# Teja
# తెలుగు
# 😀


# 44. ord()

print(ord("A"))

# Output:
# 65


# 45. chr()

print(chr(65))

# Output:
# A


# 46. split() and join() Together

sentence = "Python is very easy"

words = sentence.split()

print(words)

result = "-".join(words)

print(result)

# Output:
# ['Python', 'is', 'very', 'easy']
# Python-is-very-easy