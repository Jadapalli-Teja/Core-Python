# Python String

A **string (`str`)** is a built-in Python data type used to represent **text**.

A string is a sequence of characters enclosed inside quotes.

```python
name = "Teja"

print(name)

# Output:
# Teja
```

Strings can contain:

- Letters
- Numbers
- Symbols
- Spaces
- Special characters
- Unicode characters

Example:

```python
data = "Python 3.14 @2026"

print(data)
```

---

# 1. Creating a String

Strings can be created using:

- Single quotes `' '`
- Double quotes `" "`
- Triple single quotes `''' '''`
- Triple double quotes `""" """`

Example:

```python
name = 'Teja'
city = "Hyderabad"

print(name)
print(city)

# Output:
# Teja
# Hyderabad
```

Single and double quotes create the same `str` type.

```python
print(type("Python"))
print(type('Python'))

# Output:
# <class 'str'>
# <class 'str'>
```

---

# 2. Empty String

An empty string contains no characters.

```python
data = ""

print(data)
print(len(data))
print(type(data))

# Output:
#
# 0
# <class 'str'>
```

An empty string is still a string.

---

# 3. String with Numbers

Numbers inside quotes are treated as characters, not numbers.

```python
a = "123"

print(a)
print(type(a))

# Output:
# 123
# <class 'str'>
```

Compare:

```python
a = 123
b = "123"

print(type(a))
print(type(b))

# Output:
# <class 'int'>
# <class 'str'>
```

So:

```text
123  → integer
"123" → string
```

---

# 4. Strings Are Sequences

A string is a sequence of characters.

Example:

```python
word = "Python"
```

Conceptually:

```text
P   y   t   h   o   n
0   1   2   3   4   5
```

Each character has a position called an **index**.

This is why we can use:

- Indexing
- Slicing
- Iteration
- Membership testing

---

# 5. String Indexing

Indexing starts from `0`.

```python
word = "Python"

print(word[0])
print(word[1])
print(word[2])

# Output:
# P
# y
# t
```

Conceptually:

```text
Index:  0   1   2   3   4   5
        ↓   ↓   ↓   ↓   ↓   ↓
       P   y   t   h   o   n
```

---

# 6. Negative Indexing

Strings support negative indexing.

`-1` refers to the last character.

```python
word = "Python"

print(word[-1])
print(word[-2])
print(word[-6])

# Output:
# n
# o
# P
```

Conceptually:

```text
Positive:  0   1   2   3   4   5
Negative: -6  -5  -4  -3  -2  -1
           ↓   ↓   ↓   ↓   ↓   ↓
           P   y   t   h   o   n
```

---

# 7. Index Out of Range

If we access an index that does not exist, Python raises `IndexError`.

```python
word = "Python"

print(word[10])
```

Output:

```text
IndexError: string index out of range
```

---

# 8. String Slicing

Slicing extracts a part of a string.

Syntax:

```python
string[start:stop]
```

The `stop` index is excluded.

Example:

```python
word = "Python"

print(word[0:3])

# Output:
# Pyt
```

Indexes:

```text
P   y   t   h   o   n
0   1   2   3   4   5
↑       ↑
start   stop
```

`word[0:3]` includes indexes `0, 1, 2`.

---

# 9. Slicing with Start

```python
word = "Python"

print(word[2:])

# Output:
# thon
```

This means:

```text
start = 2
stop = end
```

---

# 10. Slicing with Stop

```python
word = "Python"

print(word[:4])

# Output:
# Pyth
```

This means:

```text
start = beginning
stop = 4
```

---

# 11. Slicing with Step

Syntax:

```python
string[start:stop:step]
```

Example:

```python
word = "Python"

print(word[::2])

# Output:
# Pto
```

Characters at every second position are selected.

---

# 12. Reverse a String Using Slicing

A string can be reversed using:

```python
[::-1]
```

Example:

```python
word = "Python"

print(word[::-1])

# Output:
# nohtyP
```

---

# 13. String Immutability

A string is **immutable**.

This means that once a string object is created, its characters cannot be changed directly.

Example:

```python
word = "Python"

word[0] = "J"
```

This produces:

```text
TypeError: 'str' object does not support item assignment
```

You cannot directly change:

```text
Python
  ↓
Jython
```

using indexing.

---

# 14. Creating a New String

Although strings cannot be modified directly, we can create a new string.

```python
word = "Python"

word = "Jython"

print(word)

# Output:
# Jython
```

The original string was not modified.

The variable was simply made to refer to another string object.

---

# 15. String Concatenation

Strings can be joined using `+`.

```python
first = "Hello"
second = "World"

result = first + " " + second

print(result)

# Output:
# Hello World
```

This is called **string concatenation**.

---

# 16. String Repetition

The `*` operator can repeat a string.

```python
word = "Hi"

print(word * 3)

# Output:
# HiHiHi
```

Another example:

```python
print("-" * 10)

# Output:
# ----------
```

---

# 17. Membership Operators

Use `in` to check whether a substring or character exists.

```python
word = "Python"

print("Py" in word)
print("Java" in word)

# Output:
# True
# False
```

Using `not in`:

```python
print("Java" not in word)

# Output:
# True
```

---

# 18. len()

`len()` returns the number of characters in a string.

```python
word = "Python"

print(len(word))

# Output:
# 6
```

Spaces are also characters.

```python
data = "Hello World"

print(len(data))

# Output:
# 11
```

There are:

```text
5 letters + 1 space + 5 letters = 11
```

---

# 19. Strings Can Contain Spaces

Spaces are part of the string.

```python
name = "Teja Jadapalli"

print(name)
print(len(name))
```

The space between the names is also counted.

---

# 20. Escape Characters

Python provides special escape sequences.

Common ones:

| Escape | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\b` | Backspace |

Example:

```python
print("Hello\nWorld")

# Output:
# Hello
# World
```

---

# 21. Tab Escape

```python
print("Name:\tTeja")

# Output:
# Name:   Teja
```

`\t` represents a tab.

---

# 22. Quotes Inside Strings

We can use different types of quotes.

```python
message = "I'm learning Python"

print(message)

# Output:
# I'm learning Python
```

Or:

```python
message = 'He said "Hello"'

print(message)

# Output:
# He said "Hello"
```

If necessary, escape the quote:

```python
message = "He said \"Hello\""

print(message)

# Output:
# He said "Hello"
```

---

# 23. Multiline Strings

Triple quotes can create multiline strings.

```python
message = """Hello
Welcome to Python
Learning strings"""

print(message)
```

Output:

```text
Hello
Welcome to Python
Learning strings
```

Triple quotes are also commonly used for docstrings.

---

# 24. Raw Strings

A raw string treats backslashes mostly as normal characters.

Use `r` before the string.

```python
path = r"C:\Users\Teja\Python"

print(path)

# Output:
# C:\Users\Teja\Python
```

Without a raw string, backslashes can introduce escape sequences.

Raw strings are especially useful for:

- Windows paths
- Regular expressions
- Text containing many backslashes

---

# 25. String Methods

Python provides many useful methods for working with strings.

Important methods include:

```text
lower()
upper()
capitalize()
title()
swapcase()
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
```

---

# 26. lower()

Converts characters to lowercase.

```python
text = "PYTHON"

print(text.lower())

# Output:
# python
```

The original string is not changed because strings are immutable.

---

# 27. upper()

Converts characters to uppercase.

```python
text = "python"

print(text.upper())

# Output:
# PYTHON
```

---

# 28. capitalize()

Makes the first character uppercase and the remaining characters lowercase.

```python
text = "python programming"

print(text.capitalize())

# Output:
# Python programming
```

---

# 29. title()

Capitalizes the first letter of each word.

```python
text = "python programming language"

print(text.title())

# Output:
# Python Programming Language
```

---

# 30. swapcase()

Changes uppercase characters to lowercase and lowercase characters to uppercase.

```python
text = "PyThOn"

print(text.swapcase())

# Output:
# pYtHoN
```

---

# 31. strip()

`strip()` removes whitespace from both ends.

```python
text = "   Python   "

print(text.strip())

# Output:
# Python
```

It does not remove spaces in the middle.

```python
text = "   Python Programming   "

print(text.strip())

# Output:
# Python Programming
```

---

# 32. lstrip()

Removes whitespace from the left side.

```python
text = "   Python"

print(text.lstrip())

# Output:
# Python
```

---

# 33. rstrip()

Removes whitespace from the right side.

```python
text = "Python   "

print(text.rstrip())

# Output:
# Python
```

---

# 34. replace()

`replace()` replaces part of a string.

```python
text = "I like Java"

result = text.replace("Java", "Python")

print(result)

# Output:
# I like Python
```

The original string remains unchanged.

---

# 35. split()

`split()` divides a string into a list.

```python
text = "Python Java C"

result = text.split()

print(result)

# Output:
# ['Python', 'Java', 'C']
```

By default, whitespace is used as the separator.

---

# 36. split() with a Separator

```python
data = "Python,Java,C"

result = data.split(",")

print(result)

# Output:
# ['Python', 'Java', 'C']
```

---

# 37. join()

`join()` combines strings into one string.

```python
languages = ["Python", "Java", "C"]

result = "-".join(languages)

print(result)

# Output:
# Python-Java-C
```

Important:

```python
separator.join(iterable)
```

The elements being joined should be strings.

---

# 38. split() and join() Relationship

`split()`:

```text
String → List
```

Example:

```python
"Python Java C".split()
```

gives:

```python
["Python", "Java", "C"]
```

`join()`:

```text
List of strings → String
```

Example:

```python
" ".join(["Python", "Java", "C"])
```

gives:

```text
Python Java C
```

---

# 39. find()

`find()` returns the index of the first occurrence.

```python
text = "Python Programming"

print(text.find("Python"))

# Output:
# 0
```

If the substring is not found:

```python
print(text.find("Java"))

# Output:
# -1
```

---

# 40. index()

`index()` also returns the position of a substring.

```python
text = "Python Programming"

print(text.index("Python"))

# Output:
# 0
```

But there is an important difference.

If the substring does not exist:

```python
text.index("Java")
```

raises:

```text
ValueError: substring not found
```

### Difference

```text
find()  → returns -1
index() → raises ValueError
```

---

# 41. count()

`count()` returns the number of occurrences.

```python
text = "banana"

print(text.count("a"))

# Output:
# 3
```

Example:

```python
text = "Python Python"

print(text.count("Python"))

# Output:
# 2
```

---

# 42. startswith()

Checks whether a string starts with a particular value.

```python
text = "Python Programming"

print(text.startswith("Python"))

# Output:
# True
```

---

# 43. endswith()

Checks whether a string ends with a particular value.

```python
filename = "resume.pdf"

print(filename.endswith(".pdf"))

# Output:
# True
```

This is useful for checking file extensions.

---

# 44. isalpha()

Returns `True` if all characters are alphabetic.

```python
text = "Python"

print(text.isalpha())

# Output:
# True
```

But:

```python
text = "Python123"

print(text.isalpha())

# Output:
# False
```

Numbers are not alphabetic.

---

# 45. isdigit()

Returns `True` if all characters are digits.

```python
text = "12345"

print(text.isdigit())

# Output:
# True
```

But:

```python
text = "123abc"

print(text.isdigit())

# Output:
# False
```

---

# 46. isalnum()

Returns `True` if all characters are alphabetic or numeric.

```python
print("Python123".isalnum())

# Output:
# True
```

But:

```python
print("Python 123".isalnum())

# Output:
# False
```

The space is not alphanumeric.

---

# 47. isspace()

Checks whether all characters are whitespace.

```python
print("   ".isspace())

# Output:
# True
```

But:

```python
print("Python".isspace())

# Output:
# False
```

---

# 48. String Comparison

Strings can be compared using:

```text
==
!=
<
>
<=
>=
```

Example:

```python
a = "apple"
b = "banana"

print(a == b)
print(a != b)

# Output:
# False
# True
```

String ordering is based on character comparison using Unicode values.

---

# 49. String Equality

`==` checks whether two strings contain the same characters.

```python
a = "Python"
b = "Python"

print(a == b)

# Output:
# True
```

---

# 50. `==` vs `is` for Strings

`==` checks values.

`is` checks object identity.

```python
a = "Python"
b = "Python"

print(a == b)
print(a is b)
```

Do not use `is` to compare string contents.

Use:

```python
a == b
```

for value comparison.

`is` is mainly used when checking object identity, such as:

```python
value is None
```

---

# 51. Converting Other Types to String

Use `str()` to convert a value to a string.

```python
age = 21

text = str(age)

print(text)
print(type(text))

# Output:
# 21
# <class 'str'>
```

Now `text` contains characters:

```text
"21"
```

not the integer `21`.

---

# 52. String and Integer Are Different

This is invalid:

```python
age = 21

print("Age: " + age)
```

because `str` and `int` cannot be directly concatenated using `+`.

We can convert:

```python
age = 21

print("Age: " + str(age))

# Output:
# Age: 21
```

Or use an f-string.

---

# 53. f-Strings

F-strings provide a convenient way to insert variables into strings.

```python
name = "Teja"
age = 21

print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is Teja and I am 21 years old.
```

Syntax:

```python
f"some text {variable}"
```

---

# 54. Formatting Expressions in f-Strings

We can also use expressions.

```python
a = 10
b = 20

print(f"Sum = {a + b}")

# Output:
# Sum = 30
```

---

# 55. String Iteration

A string is iterable.

We can loop through each character.

```python
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
```

---

# 56. enumerate() with String

`enumerate()` provides both index and character.

```python
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
```

---

# 57. Strings and Unicode

Python strings support Unicode.

This means strings can contain characters from many languages and symbol systems.

```python
text = "Hello नमस्ते"

print(text)
```

We can also store emojis:

```python
message = "Python 🐍"

print(message)
```

Python 3 strings are Unicode strings by default.

---

# 58. ord()

`ord()` returns the Unicode code point of a character.

```python
print(ord("A"))

# Output:
# 65
```

Another example:

```python
print(ord("a"))

# Output:
# 97
```

---

# 59. chr()

`chr()` converts a Unicode code point into a character.

```python
print(chr(65))

# Output:
# A
```

Therefore:

```text
ord() → character → number
chr() → number → character
```

---

# 60. String Immutability and Methods

String methods do not change the original string.

Example:

```python
text = "python"

text.upper()

print(text)

# Output:
# python
```

Why?

Because `upper()` creates and returns a new string.

Correct:

```python
text = text.upper()

print(text)

# Output:
# PYTHON
```

---

# 61. Important String Methods

| Method | Purpose |
|---|---|
| `lower()` | Converts to lowercase |
| `upper()` | Converts to uppercase |
| `capitalize()` | Capitalizes first character |
| `title()` | Capitalizes each word |
| `swapcase()` | Swaps uppercase/lowercase |
| `strip()` | Removes whitespace from both ends |
| `lstrip()` | Removes left whitespace |
| `rstrip()` | Removes right whitespace |
| `replace()` | Replaces text |
| `split()` | Splits string into list |
| `join()` | Joins strings |
| `find()` | Finds substring, returns `-1` if missing |
| `index()` | Finds substring, raises error if missing |
| `count()` | Counts occurrences |
| `startswith()` | Checks beginning |
| `endswith()` | Checks ending |
| `isalpha()` | Checks alphabetic characters |
| `isdigit()` | Checks digits |
| `isalnum()` | Checks letters/numbers |
| `isspace()` | Checks whitespace |

---

# 62. Useful String Operators

| Operator | Purpose |
|---|---|
| `+` | Concatenation |
| `*` | Repetition |
| `in` | Membership |
| `not in` | Membership negation |
| `==` | Equality |
| `!=` | Inequality |
| `<` | Less than |
| `>` | Greater than |
| `[]` | Indexing |
| `[:]` | Slicing |

---

# 63. Common String Mistakes

### Mistake 1: Trying to modify a string

Wrong:

```python
text = "Python"
text[0] = "J"
```

Strings are immutable.

---

### Mistake 2: Forgetting that indexing starts at 0

```python
text = "Python"

print(text[0])
```

Output:

```text
P
```

not `y`.

---

### Mistake 3: Confusing `"123"` with `123`

```text
"123" → str
123   → int
```

---

### Mistake 4: Using `is` instead of `==`

Use:

```python
a == b
```

when comparing string values.

---

### Mistake 5: Forgetting that `split()` returns a list

```python
text = "Python Java C"

result = text.split()

print(type(result))

# Output:
# <class 'list'>
```

---

### Mistake 6: Forgetting that `join()` is called on the separator

Correct:

```python
"-".join(["Python", "Java", "C"])
```

Not:

```python
["Python", "Java", "C"].join("-")
```

---

# 64. String vs List

Both strings and lists are sequences, but they are different.

| Feature | String | List |
|---|---|---|
| Stores | Characters/text | Any objects |
| Ordered | ✅ | ✅ |
| Indexed | ✅ | ✅ |
| Mutable | ❌ | ✅ |
| Duplicates | ✅ | ✅ |
| Slicing | ✅ | ✅ |
| `append()` | ❌ | ✅ |
| `replace()` | ✅ | ❌ |
| Main use | Text | Collection of objects |

Example:

```python
text = "Python"
numbers = [10, 20, 30]
```

---

# 65. String vs Tuple

Both are immutable sequences.

| Feature | String | Tuple |
|---|---|---|
| Main purpose | Text | Collection |
| Elements | Characters | Any objects |
| Mutable | ❌ | ❌ |
| Indexed | ✅ | ✅ |
| Slicing | ✅ | ✅ |
| Duplicates | ✅ | ✅ |

Example:

```python
text = "Python"
data = (10, 20, 30)
```

---

# 66. String Time Complexity

For a string of length `n`:

| Operation | Typical Complexity |
|---|---:|
| Index access | O(1) |
| `len()` | O(1) |
| Membership search | O(n) |
| `find()` | O(n) typical/simple cases |
| `count()` | O(n) |
| Slicing | O(k) |
| Concatenation | Depends on operation/size |
| Iteration | O(n) |

Because strings are immutable, operations that appear to modify a string generally create a **new string**.

---

# 67. Why String Concatenation Can Create New Objects

Consider:

```python
a = "Hello"
b = "World"

c = a + b
```

Python creates a new string for the result.

Conceptually:

```text
a ──> "Hello"

b ──> "World"

a + b
   ↓
new string
   ↓
"HelloWorld"
```

The original strings remain unchanged.

For joining many strings, `"separator".join(...)` is generally preferred over repeatedly using `+` in a loop.

---

# 68. Practical Example: Username Validation

```python
username = "Teja123"

if username.isalnum():
    print("Valid username")
else:
    print("Invalid username")

# Output:
# Valid username
```

---

# 69. Practical Example: Checking File Extension

```python
filename = "resume.pdf"

if filename.endswith(".pdf"):
    print("PDF file")
else:
    print("Not a PDF file")

# Output:
# PDF file
```

---

# 70. Practical Example: Counting Characters

```python
text = "banana"

print(text.count("a"))

# Output:
# 3
```

---

# 71. Practical Example: Reverse a String

```python
text = "Python"

reverse = text[::-1]

print(reverse)

# Output:
# nohtyP
```

---

# 72. Practical Example: Palindrome

A palindrome reads the same forward and backward.

```python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Palindrome
```

---

# 73. Practical Example: Remove Extra Spaces

```python
text = "   Python Programming   "

text = text.strip()

print(text)

# Output:
# Python Programming
```

---

# 74. Practical Example: Word Count

```python
text = "Python is easy to learn"

words = text.split()

print(len(words))

# Output:
# 5
```

Here:

```python
text.split()
```

produces:

```python
["Python", "is", "easy", "to", "learn"]
```

---

# 75. Quick Revision

```text
String
│
├── Text data
├── Sequence of characters
├── Ordered
├── Indexed
├── Immutable
├── Allows duplicate characters
├── Supports positive indexing
├── Supports negative indexing
├── Supports slicing
├── Iterable
├── Supports membership testing
├── Supports many built-in methods
├── Supports Unicode
└── Can be compared and formatted
```

Important examples:

```python
text = "Python"
```

Index:

```python
text[0]
```

Negative index:

```python
text[-1]
```

Slice:

```python
text[1:4]
```

Reverse:

```python
text[::-1]
```

Length:

```python
len(text)
```

Membership:

```python
"Py" in text
```

Concatenation:

```python
"Hello" + " World"
```

Repetition:

```python
"Hi" * 3
```

Conversion:

```python
str(123)
```

---

# 76. One-Line Definition

> **A string is an ordered and immutable sequence of Unicode characters used to represent text in Python.**