# NoneType in Python

`None` is a special value in Python that represents the **absence of a value** or **no value**.

The type of `None` is `NoneType`.

```python
x = None

print(x)

# Output:
# None

print(type(x))

# Output:
# <class 'NoneType'>
```

---

## 1. What is `None`?

`None` means that a variable currently has **no meaningful value**.

```python
result = None

print(result)

# Output:
# None
```

It does not mean:

- `0`
- `False`
- `""`
- `[]`
- `{}`

`None` is a separate special value.

---

## 2. Type of `None`

The type of `None` is `NoneType`.

```python
x = None

print(type(x))

# Output:
# <class 'NoneType'>
```

There is only one object of `NoneType`:

```python
None
```

---

## 3. `None` Is a Singleton

Python uses a single `None` object.

Therefore:

```python
a = None
b = None

print(a is b)

# Output:
# True
```

Both variables refer to the same `None` object.

---

## 4. Assigning `None` to a Variable

A variable can directly store `None`.

```python
name = None

print(name)

# Output:
# None
```

Later, it can be assigned another value.

```python
name = None

name = "Teja"

print(name)

# Output:
# Teja
```

---

## 5. `None` Is Different from `0`

```python
print(None == 0)

# Output:
# False
```

`0` is an integer.

```python
type(0)
# <class 'int'>
```

`None` is a `NoneType`.

```python
type(None)
# <class 'NoneType'>
```

---

## 6. `None` Is Different from `False`

```python
print(None == False)

# Output:
# False
```

Their types are different:

```python
print(type(None))
print(type(False))

# Output:
# <class 'NoneType'>
# <class 'bool'>
```

---

## 7. `None` Is Different from an Empty String

```python
print(None == "")

# Output:
# False
```

An empty string is still a string.

```python
print(type(""))

# Output:
# <class 'str'>
```

---

## 8. `None` Is Different from an Empty List

```python
print(None == [])

# Output:
# False
```

An empty list is a list object.

```python
print(type([]))

# Output:
# <class 'list'>
```

---

## 9. `None` Is Different from an Empty Dictionary

```python
print(None == {})

# Output:
# False
```

`{}` is an empty dictionary.

---

# Checking for `None`

## 10. Using `is`

The preferred way to check whether a value is `None` is:

```python
x = None

if x is None:
    print("No value")

# Output:
# No value
```

---

## 11. Using `is not`

To check that a value is not `None`:

```python
x = 10

if x is not None:
    print("Value exists")

# Output:
# Value exists
```

---

## 12. Why Use `is` Instead of `==`?

Use:

```python
x is None
```

rather than:

```python
x == None
```

`is` checks **object identity**.

`==` checks **value equality**.

Since `None` is a singleton, the standard Python style is:

```python
if x is None:
    ...
```

and:

```python
if x is not None:
    ...
```

---

# Truth Value of `None`

## 13. `bool(None)`

`None` has a Boolean value of `False`.

```python
print(bool(None))

# Output:
# False
```

Therefore:

```python
if None:
    print("True")
else:
    print("False")

# Output:
# False
```

---

## 14. `None` in an `if` Statement

```python
result = None

if result:
    print("Value exists")
else:
    print("No value")

# Output:
# No value
```

However, remember that other values can also be falsey.

For example:

```python
0
False
""
[]
{}
None
```

So:

```python
if value is None:
```

is more specific when you specifically want to detect `None`.

---

# `None` and Functions

## 15. Function Without `return`

A function that does not explicitly return a value returns `None`.

```python
def greet():
    print("Hello")

result = greet()

print(result)

# Output:
# Hello
# None
```

The function prints `"Hello"` but does not return a value.

Therefore:

```python
result
```

contains `None`.

---

## 16. Function with `return None`

A function can explicitly return `None`.

```python
def check():
    return None

result = check()

print(result)

# Output:
# None
```

These are effectively equivalent:

```python
def check():
    pass
```

and:

```python
def check():
    return None
```

Both return `None` when called.

---

## 17. `return` Without a Value

You can also write:

```python
def test():
    return

result = test()

print(result)

# Output:
# None
```

A bare `return` returns `None`.

---

## 18. Functions Can Return `None` Conditionally

```python
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return number

numbers = [10, 20, 30]

result = find_number(numbers, 50)

print(result)

# Output:
# None
```

If the function does not find the value, it reaches the end and returns `None`.

---

# `None` as a Placeholder

## 19. Placeholder Value

Sometimes we create a variable before we know its actual value.

```python
result = None

# Later
result = 100

print(result)

# Output:
# 100
```

This is useful when a value will be assigned later.

---

## 20. Initializing Variables with `None`

```python
name = None
age = None
marks = None
```

Later:

```python
name = "Teja"
age = 21
marks = 85
```

`None` can represent "not available yet."

---

# `None` in Data Structures

## 21. `None` in a List

```python
data = [10, None, 30]

print(data)

# Output:
# [10, None, 30]
```

---

## 22. `None` in a Tuple

```python
data = (10, None, 30)

print(data)

# Output:
# (10, None, 30)
```

---

## 23. `None` in a Set

`None` is hashable, so it can be stored in a set.

```python
data = {10, None, 20}

print(data)
```

The exact display order of a set should not be relied upon.

---

## 24. `None` as a Dictionary Value

```python
student = {
    "name": "Teja",
    "marks": None
}

print(student)

# Output:
# {'name': 'Teja', 'marks': None}
```

This can represent a value that is currently unavailable.

---

## 25. `None` as a Dictionary Key

`None` can also be used as a dictionary key.

```python
data = {
    None: "No key value"
}

print(data[None])

# Output:
# No key value
```

---

# `None` and Comparisons

## 26. Equality Comparison

```python
x = None

print(x == None)

# Output:
# True
```

This works, but when checking for `None`, prefer:

```python
print(x is None)

# Output:
# True
```

---

## 27. `None` and Other Values

```python
print(None == 10)
print(None == "None")
print(None == False)
print(None == [])

# Output:
# False
# False
# False
# False
```

---

## 28. Ordering Comparisons

Do not use ordering comparisons between `None` and numbers.

For example:

```python
None < 10
```

raises:

```text
TypeError
```

`None` does not have a natural ordering relationship with integers, strings, etc.

---

# `None` vs Missing Variable

## 29. Variable Containing `None`

This variable exists:

```python
x = None

print(x)

# Output:
# None
```

---

## 30. Variable That Was Never Defined

This is different:

```python
print(x)
```

if `x` was never created.

Python raises:

```text
NameError
```

So:

```text
x = None
```

means:

> The variable exists and currently contains `None`.

Whereas an undefined variable means:

> The variable does not exist in that scope.

---

# `None` in Function Arguments

## 31. Default Argument as `None`

`None` is commonly used as a default argument.

```python
def greet(name=None):
    if name is None:
        print("Hello")

greet()

# Output:
# Hello
```

When a name is provided:

```python
greet("Teja")

# Output:
# Hello
```

The function can distinguish between:

- argument not supplied
- a meaningful value supplied

---

## 32. Optional Processing

```python
def calculate(value=None):
    if value is None:
        return None

    return value * 2

print(calculate())
print(calculate(10))

# Output:
# None
# 20
```

---

# `None` and `print()`

## 33. `print()` Returns `None`

`print()` displays something but does not return that displayed value.

```python
result = print("Hello")

print(result)

# Output:
# Hello
# None
```

The first `print()` displays `"Hello"`.

Its return value is `None`.

---

# `None` and Methods

## 34. Some Methods Return `None`

Many mutable methods modify an object instead of returning the modified object.

For example:

```python
numbers = [10, 20]

result = numbers.append(30)

print(numbers)
print(result)

# Output:
# [10, 20, 30]
# None
```

`append()` changes the list and returns `None`.

This is an important Python concept.

---

# `None` and `pass`

## 35. `pass` vs `None`

`pass` and `None` are different.

`pass` is a statement that does nothing.

```python
if True:
    pass
```

`None` is an actual object/value.

```python
x = None
```

So:

```text
pass → statement
None → object/value
```

---

# `None` vs `"None"`

## 36. `None` and `"None"` Are Different

```python
a = None
b = "None"

print(a == b)

# Output:
# False
```

`None` is a special Python object.

`"None"` is a string containing four characters.

```python
print(type(a))
print(type(b))

# Output:
# <class 'NoneType'>
# <class 'str'>
```

---

# Checking `None` in Collections

## 37. Check Whether a List Contains `None`

```python
data = [10, None, 30]

if None in data:
    print("None exists")

# Output:
# None exists
```

---

## 38. Removing `None` Values

For example:

```python
data = [10, None, 20, None, 30]

result = [x for x in data if x is not None]

print(result)

# Output:
# [10, 20, 30]
```

Here `is not None` specifically checks for `None`.

---

# Important Differences

## 39. `None` vs `0`

```text
None → no value
0    → integer value zero
```

```python
type(None)
# NoneType

type(0)
# int
```

---

## 40. `None` vs `False`

```text
None  → absence of a value
False → Boolean false
```

```python
type(None)
# NoneType

type(False)
# bool
```

---

## 41. `None` vs Empty String

```text
None → no value
""   → empty string
```

---

## 42. `None` vs Empty List

```text
None → no value
[]   → empty list
```

---

## 43. `None` vs Empty Dictionary

```text
None → no value
{}   → empty dictionary
```

---

# Important Properties of `None`

## 44. `None` Is Immutable

`None` represents a single special object. You cannot modify it.

You can only change what a variable refers to:

```python
x = None

x = 10
```

The variable changed its reference; `None` itself was not modified.

---

## 45. `None` Is a Singleton

There is only one `None` object.

Therefore:

```python
a = None
b = None

print(a is b)

# Output:
# True
```

This is one reason `is None` is the standard check.

---

## 46. `None` Is Hashable

`None` can be used in sets and as dictionary keys.

```python
print(hash(None))
```

The exact hash value should not be relied upon because hash values are implementation/runtime dependent.

---

# Practical Pattern

## 47. Checking Whether a Result Exists

A common pattern is:

```python
result = None

if result is None:
    print("No result")
else:
    print(result)
```

Output:

```text
No result
```

---

## 48. Search Function Pattern

```python
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
```

Output:

```text
Found: 20
```

If the number is not found:

```text
Not found
```

---

# Important Points to Remember

1. `None` represents the absence of a value.
2. The type of `None` is `NoneType`.
3. `None` is a singleton.
4. Use `is None` to check for `None`.
5. Use `is not None` to check that a value is not `None`.
6. `None` is different from `0`.
7. `None` is different from `False`.
8. `None` is different from `""`.
9. `None` is different from `[]`.
10. `None` is different from `{}`.
11. A function without a return value returns `None`.
12. A bare `return` returns `None`.
13. `print()` returns `None`.
14. Many mutating methods such as `list.append()` return `None`.
15. `None` is falsey.
16. `None` can be stored in lists, tuples, sets and dictionaries.
17. `None` can be used as a dictionary key.
18. `None` is hashable.
19. `None` is not the same as an undefined variable.
20. `pass` is a statement, while `None` is an object/value.

---

# Quick Revision

```text
None
  ↓
Represents absence of a value
  ↓
type(None)
  ↓
NoneType
  ↓
Singleton object
  ↓
False in Boolean context
  ↓
Use:
    is None
    is not None
```

Example:

```python
result = None

if result is None:
    print("No result available")
```

Output:

```text
No result available
```