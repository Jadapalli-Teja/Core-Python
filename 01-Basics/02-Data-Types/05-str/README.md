# Python String

A **string (`str`)** is a built-in Python data type used to store **text or a sequence of characters**.

Examples:

```python
name = "Teja"
language = "Python"
message = "Hello World"
```

A string is:

- **Ordered**
- **Immutable**
- **Indexed**
- **Iterable**
- Allows duplicate characters
- Supports slicing
- Supports positive and negative indexing
- Can contain letters, numbers, symbols, spaces, and Unicode characters
- Can be created using single, double, or triple quotes

Example:

```python
name = "Teja"

print(name)
print(type(name))

# Output:
# Teja
# <class 'str'>
```

---

# 1. Creating a String

Strings can be created using single quotes:

```python
name = 'Teja'
```

Double quotes:

```python
name = "Teja"
```

Triple quotes:

```python
message = """Hello
Welcome to Python"""
```

All of these create strings.

---

# 2. Single Quotes

```python
name = 'Teja'

print(name)

# Output:
# Teja
```

---

# 3. Double Quotes

```python
name = "Teja"

print(name)

# Output:
# Teja
```

Single and double quotes normally behave the same.

The choice usually depends on which makes the string easier to write.

For example:

```python
message = "I'm learning Python"
```

This is easier than escaping the apostrophe.

---

# 4. Triple Quotes

Triple quotes are commonly used for multi-line strings.

```python
message = """Hello
My name is Teja
I am learning Python"""

print(message)

# Output:
# Hello
# My name is Teja
# I am learning Python
```

Triple quotes can use either:

```python
""" """
```

or:

```python
''' '''
```

---

# 5. Empty String

An empty string contains no characters.

```python
name = ""

print(name)
print(len(name))
print(type(name))

# Output:
#
# 0
# <class 'str'>
```

Even though it contains no characters, it is still a string.

---

# 6. String with Numbers

Numbers inside quotes are treated as strings.

```python
value = "100"

print(value)
print(type(value))

# Output:
# 100
# <class 'str'>
```

This is different from:

```python
value = 100
```

Here:

```text
"100" → str
100   → int
```

---

# 7. String with Spaces

Spaces are also characters.

```python
name = "Teja Kumar"

print(len(name))
```

The space between `Teja` and `Kumar` is counted.

---

# 8. Strings Can Contain Special Characters

A string can contain:

```python
text = "Python@123!"

print(text)

# Output:
# Python@123!
```

It can contain:

- Letters
- Numbers
- Spaces
- Symbols
- Special characters
- Unicode characters

---

# 9. String Indexing

A string is an ordered sequence of characters.

Each character has an index.

Example:

```python
word = "Python"
```

Conceptually:

```text
Index:    0   1   2   3   4   5
          ↓   ↓   ↓   ↓   ↓   ↓
String:   P   y   t   h   o   n
```

So:

```python
print(word[0])
print(word[1])
print(word[5])

# Output:
# P
# y
# n
```

---

# 10. Negative Indexing

Strings also support negative indexes.

```text
Positive:   0   1   2   3   4   5
            ↓   ↓   ↓   ↓   ↓   ↓
String:     P   y   t   h   o   n
            ↑   ↑   ↑   ↑   ↑   ↑
Negative:  -6  -5  -4  -3  -2  -1
```

Example:

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

---

# 11. Index Out of Range

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

# 12. String Slicing

Slicing extracts a portion of a string.

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

Conceptually:

```text
Index:   0   1   2   3   4   5
         P   y   t   h   o   n
         ↑       ↑
       start    stop
```

`0:3` means:

```text
index 0
index 1
index 2
```

Index `3` is excluded.

---

# 13. Slicing from the Beginning

We can omit the start index.

```python
word = "Python"

print(word[:3])

# Output:
# Pyt
```

This means:

```python
word[0:3]
```

---

# 14. Slicing Until the End

We can omit the stop index.

```python
word = "Python"

print(word[2:])

# Output:
# thon
```

This means:

```text
start from index 2
continue until the end
```

---

# 15. Copying a String Using Slicing

```python
word = "Python"

copy = word[:]

print(copy)

# Output:
# Python
```

---

# 16. Slicing with Step

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

Indexes selected:

```text
0 → P
2 → t
4 → o
```

---

# 17. Reverse a String

We can reverse a string using:

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

Conceptually:

```text
Python
  ↓
nohtyP
```

---

# 18. String is Immutable

This is one of the most important properties of strings.

**Immutable** means that an existing string cannot be changed.

For example:

```python
name = "Teja"

name[0] = "R"
```

This gives:

```text
TypeError: 'str' object does not support item assignment
```

We cannot directly change:

```text
T → R
```

inside the existing string.

---

# 19. How to Change a String

Although strings are immutable, we can create a **new string**.

```python
name = "Teja"

name = "Reja"

print(name)

# Output:
# Reja
```

Here Python did not modify `"Teja"`.

The variable `name` was made to refer to a new string.

---

# 20. String Concatenation

We can join strings using `+`.

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

# 21. String Repetition

We can repeat a string using `*`.

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

# 22. Membership Operators

We can check whether a character or substring exists using `in`.

```python
word = "Python"

print("P" in word)
print("z" in word)

# Output:
# True
# False
```

Using `not in`:

```python
print("z" not in word)

# Output:
# True
```

---

# 23. len()

`len()` returns the number of characters in a string.

```python
word = "Python"

print(len(word))

# Output:
# 6
```

Spaces are also counted.

```python
text = "Hello World"

print(len(text))

# Output:
# 11
```

---

# 24. String Comparison

Strings can be compared using comparison operators.

```python
print("abc" == "abc")
print("abc" == "ABC")

# Output:
# True
# False
```

String comparison is case-sensitive.

For example:

```text
"Python" != "python"
```

because uppercase `P` and lowercase `p` are different characters.

---

# 25. String Comparison with `<` and `>`

Strings can also be compared lexicographically.

```python
print("apple" < "banana")

# Output:
# True
```

Python compares characters based on their Unicode values.

You should think of this as dictionary/lexicographical order rather than numerical comparison.

---

# 26. `==` vs `is` with Strings

`==` checks whether two strings have the same value.

`is` checks whether two variables refer to the same object.

Example:

```python
a = "Python"
b = "Python"

print(a == b)
print(a is b)
```

`==` is the correct operator when comparing string values.

Do not use `is` to check whether two strings contain the same text.

---

# 27. Changing Case

Python provides several methods for changing letter case.

### lower()

```python
text = "PYTHON"

print(text.lower())

# Output:
# python
```

### upper()

```python
text = "python"

print(text.upper())

# Output:
# PYTHON
```

### capitalize()

```python
text = "python"

print(text.capitalize())

# Output:
# Python
```

### title()

```python
text = "python programming"

print(text.title())

# Output:
# Python Programming
```

---

# 28. swapcase()

`swapcase()` changes uppercase letters to lowercase and lowercase letters to uppercase.

```python
text = "Python"

print(text.swapcase())

# Output:
# pYTHON
```

---

# 29. Removing Spaces

### strip()

Removes spaces from both ends.

```python
text = "  Python  "

print(text.strip())

# Output:
# Python
```

### lstrip()

Removes spaces from the left.

```python
text = "  Python"

print(text.lstrip())

# Output:
# Python
```

### rstrip()

Removes spaces from the right.

```python
text = "Python  "

print(text.rstrip())

# Output:
# Python
```

These methods do not modify the original string because strings are immutable.

---

# 30. replace()

`replace()` replaces one substring with another.

```python
text = "I like Java"

result = text.replace("Java", "Python")

print(result)

# Output:
# I like Python
```

The original string remains unchanged.

```python
text = "I like Java"

text.replace("Java", "Python")

print(text)

# Output:
# I like Java
```

Why?

Because `replace()` creates and returns a new string.

---

# 31. split()

`split()` divides a string into a list.

```python
text = "Python is easy"

words = text.split()

print(words)

# Output:
# ['Python', 'is', 'easy']
```

By default, whitespace is used as the separator.

We can specify a separator:

```python
data = "apple,banana,mango"

print(data.split(","))

# Output:
# ['apple', 'banana', 'mango']
```

---

# 32. join()

`join()` combines strings from an iterable into one string.

```python
words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)

# Output:
# Python is easy
```

Another example:

```python
letters = ["A", "B", "C"]

print("-".join(letters))

# Output:
# A-B-C
```

Important:

```text
split() → string to list
join()  → list/iterable of strings to string
```

---

# 33. find()

`find()` returns the index of the first occurrence of a substring.

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

# 34. index()

`index()` also returns the position of a substring.

```python
text = "Python Programming"

print(text.index("Python"))

# Output:
# 0
```

But there is an important difference.

If the substring is not found:

```python
text.index("Java")
```

Python raises:

```text
ValueError: substring not found
```

### `find()` vs `index()`

```text
find()  → -1 if not found
index() → ValueError if not found
```

---

# 35. count()

`count()` returns the number of occurrences.

```python
text = "banana"

print(text.count("a"))

# Output:
# 3
```

---

# 36. startswith()

Checks whether a string starts with a particular substring.

```python
text = "Python Programming"

print(text.startswith("Python"))

# Output:
# True
```

---

# 37. endswith()

Checks whether a string ends with a particular substring.

```python
filename = "program.py"

print(filename.endswith(".py"))

# Output:
# True
```

This is useful when checking file extensions.

---

# 38. String Testing Methods

Python provides methods that return `True` or `False`.

Important methods include:

```text
isalpha()
isdigit()
isalnum()
isspace()
islower()
isupper()
istitle()
```

---

# 39. isalpha()

Checks whether all characters are alphabetic.

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

Numbers are not alphabetic characters.

---

# 40. isdigit()

Checks whether all characters are digits.

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

# 41. isalnum()

Checks whether all characters are alphabetic or numeric.

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

The space is neither alphabetic nor numeric.

---

# 42. isspace()

Checks whether all characters are whitespace.

```python
text = "   "

print(text.isspace())

# Output:
# True
```

---

# 43. islower() and isupper()

```python
print("python".islower())
print("PYTHON".isupper())

# Output:
# True
# True
```

---

# 44. istitle()

Checks whether the string follows title case.

```python
text = "Python Programming"

print(text.istitle())

# Output:
# True
```

---

# 45. Escape Characters

Escape characters are used to represent special characters inside strings.

### New line `\n`

```python
print("Hello\nWorld")

# Output:
# Hello
# World
```

### Tab `\t`

```python
print("Hello\tWorld")

# Output:
# Hello    World
```

### Backslash `\\`

```python
print("C:\\Users\\Teja")

# Output:
# C:\Users\Teja
```

### Single quote `\'`

```python
print('It\'s Python')

# Output:
# It's Python
```

### Double quote `\"`

```python
print("He said \"Hello\"")

# Output:
# He said "Hello"
```

---

# 46. Raw Strings

A raw string treats backslashes mostly as ordinary characters.

Use `r` before the string.

```python
path = r"C:\Users\Teja\Documents"

print(path)

# Output:
# C:\Users\Teja\Documents
```

Raw strings are especially useful for Windows paths and regular expressions.

---

# 47. String Formatting

Python provides several ways to format strings.

### f-string

```python
name = "Teja"
age = 21

print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is Teja and I am 21 years old.
```

This is the most commonly used modern approach.

---

# 48. Expressions Inside f-Strings

We can place expressions inside `{}`.

```python
a = 10
b = 20

print(f"Sum = {a + b}")

# Output:
# Sum = 30
```

---

# 49. Formatting Numbers

```python
price = 1234.5678

print(f"{price:.2f}")

# Output:
# 1234.57
```

`.2f` means two digits after the decimal point.

---

# 50. String Formatting with format()

Another method is `format()`.

```python
name = "Teja"
age = 21

print("My name is {} and I am {} years old.".format(name, age))

# Output:
# My name is Teja and I am 21 years old.
```

---

# 51. String Iteration

A string is iterable.

We can loop through each character.

```python
word = "Python"

for character in word:
    print(character)

# Output:
# P
# y
# t
# h
# o
# n
```

---

# 52. enumerate() with String

`enumerate()` gives the index and character.

```python
word = "Python"

for index, character in enumerate(word):
    print(index, character)

# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
```

---

# 53. String Conversion Using str()

We can convert other data types into strings using `str()`.

```python
age = 21

result = str(age)

print(result)
print(type(result))

# Output:
# 21
# <class 'str'>
```

Now:

```text
21
```

is stored as a string:

```text
"21"
```

---

# 54. String and Integer Are Different

Consider:

```python
a = "10"
b = 20
```

This is invalid:

```python
print(a + b)
```

because one is a string and the other is an integer.

We can convert:

```python
print(int(a) + b)

# Output:
# 30
```

Or convert the integer to a string:

```python
print(a + str(b))

# Output:
# 1020
```

---

# 55. Unicode

Python strings support Unicode.

This means strings can contain characters from many languages and symbol systems.

```python
text = "Hello नमस्ते"

print(text)
```

You can also store emojis:

```python
message = "Python 🐍"

print(message)
```

Python 3 strings are Unicode strings by default.

---

# 56. ord()

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

# 57. chr()

`chr()` converts a Unicode code point into a character.

```python
print(chr(65))

# Output:
# A
```

So:

```text
ord("A") → 65
chr(65)  → "A"
```

They are opposite operations.

---

# 58. String Immutability and Methods

Remember that string methods do not modify the original string.

Example:

```python
text = "python"

text.upper()

print(text)

# Output:
# python
```

Why?

Because:

```python
text.upper()
```

creates a new string.

To keep the result:

```python
text = text.upper()

print(text)

# Output:
# PYTHON
```

---

# 59. String Object and References

Consider:

```python
a = "Python"
b = a
```

Both variables refer to a string object.

Conceptually:

```text
a ──┐
    ├──> "Python"
b ──┘
```

Since strings are immutable, changing `a` creates/references another string rather than modifying the existing `"Python"` object.

```python
a = "Java"

print(a)
print(b)

# Output:
# Java
# Python
```

---

# 60. String Methods Return New Values

Many string methods return a new string.

Example:

```python
text = "hello"

result = text.upper()

print(text)
print(result)

# Output:
# hello
# HELLO
```

The original string is unchanged.

---

# 61. Common String Methods

| Method | Purpose |
|---|---|
| `lower()` | Convert to lowercase |
| `upper()` | Convert to uppercase |
| `capitalize()` | Capitalize first character |
| `title()` | Convert to title case |
| `swapcase()` | Swap uppercase/lowercase |
| `strip()` | Remove spaces from both ends |
| `lstrip()` | Remove left-side spaces |
| `rstrip()` | Remove right-side spaces |
| `replace()` | Replace substring |
| `split()` | Split string into list |
| `join()` | Join strings |
| `find()` | Find substring position |
| `index()` | Find substring position |
| `count()` | Count occurrences |
| `startswith()` | Check beginning |
| `endswith()` | Check ending |
| `isalpha()` | Check alphabetic characters |
| `isdigit()` | Check digits |
| `isalnum()` | Check alphabetic/numeric |
| `isspace()` | Check whitespace |
| `islower()` | Check lowercase |
| `isupper()` | Check uppercase |
| `istitle()` | Check title case |

---

# 62. String vs List

A string and list are both sequences, but they behave differently.

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
| `split()` | ✅ | ❌ |
| `join()` | ✅ | ❌ |

Example:

```python
text = "Python"
```

vs:

```python
letters = ["P", "y", "t", "h", "o", "n"]
```

---

# 63. String vs Tuple

Both are immutable sequences.

| Feature | String | Tuple |
|---|---|---|
| Stores | Characters/text | Any objects |
| Mutable | ❌ | ❌ |
| Indexed | ✅ | ✅ |
| Slicing | ✅ | ✅ |
| Duplicate values | ✅ | ✅ |
| Different object types | ❌ | ✅ |
| Main purpose | Text | Fixed collection |

For example:

```python
name = "Teja"
```

is text.

```python
student = ("Teja", 21, "CSE")
```

is a fixed collection of different values.

---

# 64. String Truth Value

An empty string is `False`.

A non-empty string is `True`.

```python
print(bool(""))
print(bool("Python"))

# Output:
# False
# True
```

Example:

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")

# Output:
# Name is empty
```

---

# 65. String Memory Concept

Strings are objects in Python.

For example:

```python
name = "Python"
```

Conceptually:

```text
name
 ↓
"Python"
```

If we do:

```python
name = "Java"
```

the variable is made to refer to another string object.

The existing string is not modified.

This is a result of **string immutability**.

---

# 66. Common String Mistakes

### Mistake 1: Trying to change a character

Wrong:

```python
text = "Python"

text[0] = "J"
```

Strings are immutable.

---

### Mistake 2: Treating numeric strings as integers

```python
age = "21"
```

This is a string, not an integer.

```python
print(type(age))

# Output:
# <class 'str'>
```

---

### Mistake 3: Using `is` instead of `==`

Wrong for value comparison:

```python
a is b
```

Use:

```python
a == b
```

when comparing string contents.

---

### Mistake 4: Forgetting that stop index is excluded

```python
word = "Python"

print(word[0:3])

# Output:
# Pyt
```

Index `3` is not included.

---

### Mistake 5: Confusing `split()` and `join()`

Remember:

```text
split() → String → List
join()  → Strings → String
```

---

### Mistake 6: Expecting string methods to modify the original

```python
text = "python"

text.upper()

print(text)

# Output:
# python
```

Correct:

```python
text = text.upper()
```

---

# 67. Important String Concepts

Remember these points:

```text
String
│
├── Ordered
├── Immutable
├── Indexed
├── Iterable
├── Supports slicing
├── Allows duplicate characters
├── Supports positive indexing
├── Supports negative indexing
├── Supports many built-in methods
├── Supports Unicode
└── Can be compared and concatenated
```

---

# 68. Quick Revision

Creating strings:

```python
"Python"
'Python'
"""Python"""
```

Indexing:

```python
text[0]
text[-1]
```

Slicing:

```python
text[1:4]
text[:4]
text[2:]
text[::2]
text[::-1]
```

Concatenation:

```python
"Hello" + " World"
```

Repetition:

```python
"Hi" * 3
```

Membership:

```python
"Py" in "Python"
```

Length:

```python
len("Python")
```

Conversion:

```python
str(100)
```

Common methods:

```python
lower()
upper()
strip()
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

# 69. Final Mental Model

Think of a string as:

> **An immutable, ordered sequence of Unicode characters.**

For:

```python
word = "Python"
```

you can:

```text
Index             ✅
Slice             ✅
Search            ✅
Count             ✅
Iterate           ✅
Concatenate       ✅
Repeat            ✅
Convert           ✅
Change case       ✅
```

But you cannot:

```text
Change individual character    ❌
Append directly                ❌
Remove individual character    ❌
Modify the existing string     ❌
```

Instead, string operations create a **new string**.

---

# 70. One-Line Definition

> **A string is an immutable, ordered sequence of Unicode characters used to represent text in Python.**