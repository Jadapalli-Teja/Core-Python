# Python Strings

A **string** is a sequence of characters enclosed inside quotes.

---

## 1. What is a String?

A string is used to store text in Python.

```python
name = "Teja"
city = "Nellore"

Here:

"Teja" → string
"Nellore" → string

A string can contain:

Alphabets
Numbers
Spaces
Special characters
Symbols
Unicode characters
name = "Teja"
age = "21"
symbol = "@"
message = "Hello Python!"

Even though age contains digits, "21" is a string, not an integer.

print(type("21"))

Output:

<class 'str'>
2. Creating Strings

Python allows strings to be created using single or double quotes.

Single Quotes
name = 'Teja'
Double Quotes
name = "Teja"

Both create a string:

print(type('Teja'))
print(type("Teja"))

Output:

<class 'str'>
<class 'str'>

Python does not treat single quotes and double quotes as different string types.

3. Multi-line Strings

Triple quotes can be used to create multi-line strings.

message = """Hello
Welcome to Python
Learning Strings"""
print(message)

Output:

Hello
Welcome to Python
Learning Strings

You can use either:

""" """

or:

''' '''
4. Empty Strings

A string can contain zero characters.

name = ""

The length of an empty string is 0.

print(len(name))

Output:

0

An empty string is also considered False in a Boolean context.

print(bool(""))

Output:

False
5. Strings Can Contain Numbers

A string can contain numeric characters, but that does not make it an integer.

a = 100
b = "100"

print(type(a))
print(type(b))

Output:

<class 'int'>
<class 'str'>

This difference is important.

print(100 + 200)

Output:

300

But:

print("100" + "200")

Output:

100200

The second operation joins two strings together.

6. Escape Sequences

Escape sequences are special combinations beginning with \.

New Line - \n
print("Hello\nPython")

Output:

Hello
Python
Tab - \t
print("Hello\tPython")

Output:

Hello    Python
Backslash - \\
print("C:\\Users\\Teja")

Output:

C:\Users\Teja
Single Quote - \'
print('It\'s Python')

Output:

It's Python
Double Quote - \"
print("He said \"Hello\"")

Output:

He said "Hello"
7. Raw Strings

A raw string treats backslashes more literally.

An r is placed before the string.

path = r"C:\Users\Teja\Python"

print(path)

Output:

C:\Users\Teja\Python

Raw strings are useful when working with:

Windows file paths
Regular expressions
8. Strings Are Sequences

A string is a sequence of characters.

For example:

word = "Python"

Conceptually:

P   y   t   h   o   n
0   1   2   3   4   5

Each character has a position called an index.

Python indexing starts from 0.

Therefore:

print(word[0])
print(word[2])
print(word[5])

Output:

P
t
n
9. Positive Indexing

Positive indexes start from 0 and move from left to right.

String:    P    y    t    h    o    n
Index:     0    1    2    3    4    5

Example:

word = "Python"

print(word[0])
print(word[1])
print(word[3])

Output:

P
y
h
10. Negative Indexing

Negative indexes start from -1 and move from right to left.

String:     P    y    t    h    o    n
Positive:   0    1    2    3    4    5
Negative:  -6   -5   -4   -3   -2   -1

Example:

word = "Python"

print(word[-1])
print(word[-2])
print(word[-6])

Output:

n
o
P

-1 is commonly used to access the last character.

11. IndexError

If an index does not exist, Python raises IndexError.

word = "Python"

print(word[10])

There is no index 10, so Python raises:

IndexError: string index out of range

The valid positive indexes are:

0 to len(string) - 1

For "Python":

len("Python") = 6

Last index = 6 - 1 = 5
12. String Slicing

Slicing is used to extract a part of a string.

Syntax
string[start:stop]

The start index is included, but the stop index is excluded.

Example:

word = "Python"

print(word[0:3])

Output:

Pyt

Indexes 0, 1, and 2 are included.

Index 3 is not included.

Slicing With Step

Syntax:

string[start:stop:step]

Example:

word = "Python"

print(word[0:6:2])

Output:

Pto

Indexes used:

0 → P
2 → t
4 → o
Omitting Start
word = "Python"

print(word[:3])

Output:

Pyt

This means:

word[0:3]
Omitting Stop
print(word[2:])

Output:

thon
Copying the Whole String
print(word[:])

Output:

Python
13. Reverse a String

A string can be reversed using slicing.

word = "Python"

print(word[::-1])

Output:

nohtyP

Here:

[::-1]

means that the step is -1, so Python moves from right to left.

14. String Concatenation

Concatenation means joining strings together.

The + operator is used.

first = "Hello"
second = "Python"

result = first + " " + second

print(result)

Output:

Hello Python

A string cannot be directly added to an integer.

age = 21

print("Age: " + age)

This gives a TypeError.

Instead, convert the integer into a string:

print("Age: " + str(age))

Output:

Age: 21
15. String Repetition

The * operator can repeat a string.

word = "Hi"

print(word * 3)

Output:

HiHiHi

Another example:

print("-" * 10)

Output:

----------
16. Membership Operators

The in and not in operators check whether a character or substring exists inside a string.

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)

Output:

True
False
True

Example with a condition:

email = "teja@gmail.com"

if "@" in email:
    print("Contains @")

Output:

Contains @
17. len() Function

The len() function returns the number of characters in a string.

word = "Python"

print(len(word))

Output:

6

Spaces are also counted as characters.

text = "Hello World"

print(len(text))

Output:

11

Because:

Hello  → 5
Space  → 1
World  → 5

Total  → 11
18. Strings Are Immutable

One of the most important properties of strings is:

Strings are immutable.

Immutable means that once a string object is created, its individual characters cannot be changed.

For example:

word = "Python"

word[0] = "J"

This produces:

TypeError: 'str' object does not support item assignment

You cannot directly change "Python" into "Jython" by modifying index 0.

Instead, create a new string:

word = "Python"

word = "J" + word[1:]

print(word)

Output:

Jython

The original string was not modified.

A new string was created and word was made to refer to it.

19. String Methods

Python provides many built-in methods for working with strings.

Some important methods are:

Method	Purpose
lower()	Converts to lowercase
upper()	Converts to uppercase
capitalize()	Capitalizes first character
title()	Capitalizes each word
strip()	Removes leading/trailing whitespace
replace()	Replaces part of a string
split()	Splits a string into a list
join()	Joins strings together
find()	Finds the position of a substring
index()	Finds the position of a substring
count()	Counts occurrences
startswith()	Checks the beginning
endswith()	Checks the ending
isalpha()	Checks alphabetic characters
isdigit()	Checks digits
isalnum()	Checks letters/numbers
isspace()	Checks whitespace
20. Changing Case
lower()
text = "Python"

print(text.lower())

Output:

python
upper()
print(text.upper())

Output:

PYTHON
capitalize()
text = "python programming"

print(text.capitalize())

Output:

Python programming
title()
print(text.title())

Output:

Python Programming
21. Removing Whitespace
strip()

Removes whitespace from both ends.

text = "   Python   "

print(text.strip())

Output:

Python
lstrip()

Removes whitespace from the left side.

print(text.lstrip())
rstrip()

Removes whitespace from the right side.

print(text.rstrip())
22. replace()

The replace() method replaces part of a string.

text = "I like Java"

result = text.replace("Java", "Python")

print(result)

Output:

I like Python

The original string is not changed because strings are immutable.

23. split()

split() divides a string and returns a list.

text = "Python is easy"

words = text.split()

print(words)

Output:

['Python', 'is', 'easy']

You can also specify a separator.

data = "apple,banana,mango"

print(data.split(","))

Output:

['apple', 'banana', 'mango']
24. join()

join() joins multiple strings into one string.

words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)

Output:

Python is easy

Another example:

words = ["Python", "Java", "C"]

print(", ".join(words))

Output:

Python, Java, C
split() vs join()
split() → String → List

join()  → List of strings → String
25. find() and index()

Both can be used to find the position of a substring.

text = "Python Programming"

print(text.find("Python"))

Output:

0

If the substring is not found:

print(text.find("Java"))

Output:

-1

But index() behaves differently.

print(text.index("Java"))

It raises:

ValueError
Difference
find()  → returns -1 if not found
index() → raises ValueError if not found
26. count()

count() returns the number of occurrences of a substring.

text = "banana"

print(text.count("a"))

Output:

3
27. startswith() and endswith()
startswith()

Checks whether a string starts with a particular value.

text = "Python Programming"

print(text.startswith("Python"))

Output:

True
endswith()

Checks whether a string ends with a particular value.

print(text.endswith("Programming"))

Output:

True
28. Character Checking Methods
isalpha()

Checks whether all characters are alphabetic.

print("Python".isalpha())
print("Python123".isalpha())

Output:

True
False
isdigit()

Checks whether all characters are digits.

print("12345".isdigit())
print("123abc".isdigit())

Output:

True
False
isalnum()

Checks whether all characters are alphabetic or numeric.

print("Python123".isalnum())
print("Python 123".isalnum())

Output:

True
False

The second string contains a space.

isspace()

Checks whether all characters are whitespace.

print("   ".isspace())
print("Python".isspace())

Output:

True
False
29. String Comparison

Strings can be compared using:

==
!=
<
>
<=
>=

Example:

a = "apple"
b = "apple"

print(a == b)

Output:

True

Python compares strings based on their character ordering.

print("apple" < "banana")

Output:

True
30. String Conversion Using str()

The str() function converts a value into a string.

age = 21
price = 99.5
value = True

print(str(age))
print(str(price))
print(str(value))

Output:

21
99.5
True

Check the type:

result = str(100)

print(type(result))

Output:

<class 'str'>
31. String Formatting

f-strings provide a convenient way to insert values into strings.

name = "Teja"
age = 21

print(f"My name is {name} and I am {age} years old.")

Output:

My name is Teja and I am 21 years old.

Expressions can also be used inside {}.

a = 10
b = 20

print(f"Sum = {a + b}")

Output:

Sum = 30

Methods can also be used:

name = "teja"

print(f"Name: {name.upper()}")

Output:

Name: TEJA
32. Formatting Numbers in Strings

f-strings can format numbers.

price = 99.5678

print(f"{price:.2f}")

Output:

99.57

.2f means that the number should be displayed with 2 digits after the decimal point.

33. Iterating Through a String

Since a string is a sequence, we can loop through its characters.

word = "Python"

for char in word:
    print(char)

Output:

P
y
t
h
o
n

Each iteration gives one character.

34. enumerate() With Strings

enumerate() can be used when we need both the index and character.

word = "Python"

for index, char in enumerate(word):
    print(index, char)

Output:

0 P
1 y
2 t
3 h
4 o
5 n
35. Unicode Strings

Python strings support Unicode characters.

Therefore, strings can contain characters from many languages and symbols.

name = "Teja"
language = "తెలుగు"
emoji = "😀"

print(name)
print(language)
print(emoji)

Output:

Teja
తెలుగు
😀
36. ord() and chr()

ord() returns the Unicode code point of a character.

print(ord("A"))

Output:

65

chr() converts a Unicode code point back into a character.

print(chr(65))

Output:

A

So:

ord() → Character → Number

chr() → Number → Character
37. == vs is With Strings

== checks whether two strings have the same value.

a = "Python"
b = "Python"

print(a == b)

Output:

True

is checks whether two variables refer to the same object.

Therefore, when comparing string values, use:

a == b

rather than relying on:

a is b

is is an identity operator, not a general string-value comparison operator.

38. Important Properties of Strings

Python strings have the following important properties:

str is the string data type.
Strings are sequences of characters.
Strings are ordered.
Indexing starts from 0.
Negative indexing starts from -1.
Strings support slicing.
Strings are immutable.
Strings support iteration.
Strings support membership testing.
Strings support concatenation using +.
Strings support repetition using *.
Strings support Unicode characters.
Python provides many useful string methods.
39. Important Points to Remember
String
name = "Teja"
Type
type(name)
Length
len(name)
Indexing
name[0]
Negative Indexing
name[-1]
Slicing
name[1:3]
Reverse
name[::-1]
Concatenation
"Hello " + name
Repetition
"Hi " * 3
Membership
"e" in name
Conversion
str(100)
Immutability
# name[0] = "R"  → TypeError
Quick Revision
String
   ↓
Sequence of characters
   ↓
Created using quotes
   ↓
Supports indexing
   ↓
Supports negative indexing
   ↓
Supports slicing
   ↓
Supports + and *
   ↓
Supports in / not in
   ↓
Immutable
   ↓
Supports iteration
   ↓
Has many built-in methods
   ↓
Supports Unicode
Most Important String Methods
lower()
upper()
capitalize()
title()
strip()
lstrip()
rstrip()
replace()
split()
join()
find()
index()
count()
startswith()
endswith()
isalpha()
isdigit()
isalnum()
isspace()