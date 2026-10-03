# Dictionary in Python

A **dictionary** is a built-in Python data type used to store data in **key-value pairs**.

```python
student = {
    "name": "Teja",
    "age": 21,
    "branch": "CSE"
}
```

Here:

- `"name"`, `"age"`, `"branch"` → keys
- `"Teja"`, `21`, `"CSE"` → values

Dictionaries are:

- Mutable
- Ordered (insertion order is preserved)
- Indexed by keys, not positions
- Able to store different data types
- Able to contain duplicate values
- Keys must be unique
- Keys must be hashable

---

## 1. Creating a Dictionary

The most common way is using `{}`.

```python
student = {
    "name": "Teja",
    "age": 21,
    "branch": "CSE"
}

print(student)

# Output:
# {'name': 'Teja', 'age': 21, 'branch': 'CSE'}
```

---

## 2. Empty Dictionary

```python
d = {}

print(d)

# Output:
# {}
```

`{}` creates an empty dictionary.

> `{}` does **not** create an empty set.

For an empty set:

```python
s = set()
```

---

## 3. Creating Dictionary Using `dict()`

Python provides the `dict()` constructor.

```python
student = dict(name="Teja", age=21)

print(student)

# Output:
# {'name': 'Teja', 'age': 21}
```

---

## 4. Dictionary with Different Types of Values

Values can have different data types.

```python
student = {
    "name": "Teja",
    "age": 21,
    "marks": 85.5,
    "passed": True,
    "skills": ["Python", "SQL"]
}

print(student)
```

A dictionary can contain:

- String
- Integer
- Float
- Boolean
- List
- Tuple
- Set
- Another dictionary
- `None`

---

## 5. Dictionary Keys

A dictionary stores data using keys.

```python
student = {
    "name": "Teja",
    "age": 21
}
```

`name` and `age` are keys.

Keys are used to access values.

```python
print(student["name"])

# Output:
# Teja
```

---

## 6. Dictionary Values

Values are the actual data stored against keys.

```python
student = {
    "name": "Teja",
    "age": 21
}
```

Values are:

```text
Teja
21
```

Multiple keys can have the same value.

```python
d = {
    "a": 10,
    "b": 10,
    "c": 10
}
```

---

## 7. Keys Must Be Unique

A dictionary cannot have duplicate keys.

```python
d = {
    "name": "Teja",
    "name": "Ravi"
}

print(d)

# Output:
# {'name': 'Ravi'}
```

The later value replaces the earlier value.

---

## 8. Values Can Be Duplicated

Values do not need to be unique.

```python
d = {
    "a": 10,
    "b": 10,
    "c": 20
}
```

This is valid.

---

## 9. Accessing Values Using `[]`

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student["name"])

# Output:
# Teja
```

The key is placed inside square brackets.

---

## 10. What Happens If the Key Does Not Exist?

```python
student = {
    "name": "Teja"
}

print(student["age"])
```

This produces:

```text
KeyError
```

because `"age"` does not exist.

---

## 11. Using `get()`

`get()` is a safer way to access dictionary values.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student.get("age"))

# Output:
# 21
```

If the key does not exist:

```python
print(student.get("marks"))

# Output:
# None
```

---

## 12. `get()` with Default Value

```python
student = {
    "name": "Teja"
}

print(student.get("marks", 0))

# Output:
# 0
```

If the key is missing, the default value is returned.

---

## 13. Adding a New Key-Value Pair

```python
student = {
    "name": "Teja"
}

student["age"] = 21

print(student)

# Output:
# {'name': 'Teja', 'age': 21}
```

---

## 14. Changing a Value

If the key already exists, assignment changes its value.

```python
student = {
    "name": "Teja",
    "age": 20
}

student["age"] = 21

print(student)

# Output:
# {'name': 'Teja', 'age': 21}
```

So:

```python
d[key] = value
```

can either:

- Add a new key
- Change an existing key's value

---

## 15. `update()`

`update()` adds or changes multiple key-value pairs.

```python
student = {
    "name": "Teja",
    "age": 21
}

student.update({
    "age": 22,
    "branch": "CSE"
})

print(student)
```

Output:

```text
{'name': 'Teja', 'age': 22, 'branch': 'CSE'}
```

---

## 16. `setdefault()`

`setdefault()` adds a key only if it does not already exist.

```python
student = {
    "name": "Teja"
}

student.setdefault("age", 21)

print(student)

# Output:
# {'name': 'Teja', 'age': 21}
```

If the key already exists, its value is not changed.

```python
student.setdefault("name", "Ravi")

print(student["name"])

# Output:
# Teja
```

---

## 17. `keys()`

Returns a view containing dictionary keys.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student.keys())

# Output:
# dict_keys(['name', 'age'])
```

---

## 18. `values()`

Returns a view containing dictionary values.

```python
print(student.values())

# Output:
# dict_values(['Teja', 21])
```

---

## 19. `items()`

Returns key-value pairs.

```python
print(student.items())

# Output:
# dict_items([('name', 'Teja'), ('age', 21)])
```

Each pair is represented as a tuple.

---

## 20. Iterating Through a Dictionary

By default, iteration is over keys.

```python
student = {
    "name": "Teja",
    "age": 21
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

---

## 21. Iterating Through Values

```python
for value in student.values():
    print(value)
```

Output:

```text
Teja
21
```

---

## 22. Iterating Through Keys and Values

Use `items()`.

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Teja
age 21
```

---

## 23. Checking Whether a Key Exists

Use `in`.

```python
student = {
    "name": "Teja",
    "age": 21
}

print("name" in student)

# Output:
# True
```

By default, `in` checks **keys**, not values.

```python
print("Teja" in student)

# Output:
# False
```

---

## 24. Checking Values

Use `.values()`.

```python
print("Teja" in student.values())

# Output:
# True
```

---

## 25. Dictionary Length

`len()` returns the number of key-value pairs.

```python
student = {
    "name": "Teja",
    "age": 21,
    "branch": "CSE"
}

print(len(student))

# Output:
# 3
```

---

## 26. Removing an Element Using `pop()`

`pop()` removes a specified key and returns its value.

```python
student = {
    "name": "Teja",
    "age": 21
}

age = student.pop("age")

print(age)
print(student)

# Output:
# 21
# {'name': 'Teja'}
```

---

## 27. `pop()` with Default Value

```python
student = {
    "name": "Teja"
}

print(student.pop("age", 0))

# Output:
# 0
```

This avoids `KeyError`.

---

## 28. `popitem()`

`popitem()` removes and returns the last inserted key-value pair.

```python
student = {
    "name": "Teja",
    "age": 21
}

item = student.popitem()

print(item)
print(student)
```

Output:

```text
('age', 21)
{'name': 'Teja'}
```

---

## 29. `clear()`

Removes all elements.

```python
student = {
    "name": "Teja",
    "age": 21
}

student.clear()

print(student)

# Output:
# {}
```

---

## 30. `del`

Delete a specific key.

```python
student = {
    "name": "Teja",
    "age": 21
}

del student["age"]

print(student)

# Output:
# {'name': 'Teja'}
```

You can also delete the complete dictionary variable:

```python
del student
```

---

# Nested Dictionaries

## 31. Dictionary Inside Dictionary

A dictionary can contain another dictionary.

```python
students = {
    "student1": {
        "name": "Teja",
        "age": 21
    },
    "student2": {
        "name": "Ravi",
        "age": 22
    }
}
```

Access nested values:

```python
print(students["student1"]["name"])

# Output:
# Teja
```

---

## 32. List Inside Dictionary

```python
student = {
    "name": "Teja",
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"])

# Output:
# ['Python', 'SQL', 'Git']
```

---

## 33. Dictionary Inside List

```python
students = [
    {"name": "Teja", "age": 21},
    {"name": "Ravi", "age": 22}
]

print(students[0]["name"])

# Output:
# Teja
```

This structure is very common when working with JSON and APIs.

---

# Converting Other Data Types to Dictionary

## 34. Dictionary from List of Pairs

```python
data = [
    ("name", "Teja"),
    ("age", 21)
]

student = dict(data)

print(student)

# Output:
# {'name': 'Teja', 'age': 21}
```

Each inner sequence must contain two elements:

```text
(key, value)
```

---

## 35. Dictionary from Tuple of Pairs

```python
data = (
    ("name", "Teja"),
    ("age", 21)
)

student = dict(data)

print(student)
```

---

## 36. Using `zip()` with Dictionary

```python
keys = ["name", "age", "branch"]
values = ["Teja", 21, "CSE"]

student = dict(zip(keys, values))

print(student)

# Output:
# {'name': 'Teja', 'age': 21, 'branch': 'CSE'}
```

---

## 37. `fromkeys()`

Creates a dictionary using given keys and a common value.

```python
keys = ["name", "age", "branch"]

student = dict.fromkeys(keys)

print(student)

# Output:
# {'name': None, 'age': None, 'branch': None}
```

With a default value:

```python
student = dict.fromkeys(keys, "Unknown")

print(student)

# Output:
# {'name': 'Unknown', 'age': 'Unknown', 'branch': 'Unknown'}
```

---

# Dictionary Comprehension

## 38. Basic Dictionary Comprehension

Dictionary comprehension provides a short way to create dictionaries.

```python
squares = {x: x * x for x in range(1, 6)}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

General syntax:

```python
{key: value for item in iterable}
```

---

## 39. Dictionary Comprehension with Condition

```python
squares = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(squares)

# Output:
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

---

# Copying Dictionaries

## 40. Reference Assignment

```python
a = {"x": 10}
b = a

b["x"] = 20

print(a)

# Output:
# {'x': 20}
```

Both variables refer to the same dictionary object.

---

## 41. Using `copy()`

```python
a = {"x": 10}
b = a.copy()

b["x"] = 20

print(a)
print(b)

# Output:
# {'x': 10}
# {'x': 20}
```

Now they are separate dictionary objects.

---

## 42. Using `dict()` to Copy

```python
a = {"x": 10}

b = dict(a)

b["x"] = 20

print(a)
print(b)
```

---

## 43. `==` vs `is`

`==` checks whether two dictionaries contain equal data.

`is` checks whether they are the same object.

```python
a = {"x": 10}
b = {"x": 10}

print(a == b)
print(a is b)

# Output:
# True
# False
```

---

# Dictionary Keys and Hashability

## 44. Keys Must Be Hashable

Dictionary keys must be hashable.

Valid examples:

```python
d = {
    1: "one",
    "name": "Teja",
    (1, 2): "tuple"
}
```

Common hashable types:

- `int`
- `float`
- `str`
- `bool`
- `tuple` (when its elements are hashable)
- `frozenset`

---

## 45. List Cannot Be a Dictionary Key

Lists are mutable and therefore cannot be used as dictionary keys.

```python
d = {
    [1, 2]: "value"
}
```

This gives:

```text
TypeError: unhashable type: 'list'
```

---

## 46. Tuple Can Be a Dictionary Key

A tuple can be used as a key if its elements are hashable.

```python
d = {
    (10, 20): "point"
}

print(d[(10, 20)])

# Output:
# point
```

---

## 47. Boolean Keys

`True` and `1` are considered equal as dictionary keys.

```python
d = {
    True: "A",
    1: "B"
}

print(d)

# Output:
# {True: 'B'}
```

Similarly:

```python
False == 0
```

is `True`.

Therefore, `False` and `0` cannot represent two separate dictionary keys.

---

## 48. `None` as a Key

`None` can be used as a dictionary key.

```python
d = {
    None: "No value"
}

print(d[None])

# Output:
# No value
```

---

# Dictionary Order

## 49. Insertion Order

Modern Python dictionaries preserve insertion order.

```python
student = {}

student["name"] = "Teja"
student["age"] = 21
student["branch"] = "CSE"

print(student)

# Output:
# {'name': 'Teja', 'age': 21, 'branch': 'CSE'}
```

The order in which keys are inserted is preserved during iteration.

> Dictionary is ordered, but it is still accessed using keys rather than numeric positions.

---

# Dictionary Views

## 50. Dictionary Views Are Dynamic

`keys()`, `values()` and `items()` return view objects.

```python
d = {
    "a": 10
}

keys = d.keys()

d["b"] = 20

print(keys)

# Output:
# dict_keys(['a', 'b'])
```

The view reflects changes made to the dictionary.

---

# Sorting Dictionaries

## 51. `sorted()` on Dictionary

When `sorted()` is used directly on a dictionary, it sorts the keys.

```python
d = {
    30: "C",
    10: "A",
    20: "B"
}

print(sorted(d))

# Output:
# [10, 20, 30]
```

---

## 52. Sorting by Values

```python
marks = {
    "Teja": 80,
    "Ravi": 95,
    "Kiran": 70
}

result = sorted(marks, key=marks.get)

print(result)

# Output:
# ['Kiran', 'Teja', 'Ravi']
```

Here the keys are sorted according to their values.

---

## 53. Minimum and Maximum

```python
marks = {
    "Teja": 80,
    "Ravi": 95,
    "Kiran": 70
}

print(min(marks, key=marks.get))
print(max(marks, key=marks.get))

# Output:
# Kiran
# Ravi
```

---

# `any()` and `all()`

## 54. `any()` with Dictionary

When used directly on a dictionary, `any()` checks its keys.

```python
d = {
    0: "A",
    1: "B"
}

print(any(d))

# Output:
# True
```

At least one key is truthy.

---

## 55. `any()` with Values

```python
d = {
    "a": 0,
    "b": 10
}

print(any(d.values()))

# Output:
# True
```

---

## 56. `all()` with Values

```python
d = {
    "a": 10,
    "b": 20
}

print(all(d.values()))

# Output:
# True
```

---

# Dictionary Truth Value

## 57. Empty Dictionary

An empty dictionary is considered `False`.

```python
d = {}

print(bool(d))

# Output:
# False
```

---

## 58. Non-Empty Dictionary

```python
d = {
    "name": "Teja"
}

print(bool(d))

# Output:
# True
```

Therefore:

```python
if d:
    print("Dictionary is not empty")
```

---

# Dictionary Unpacking

## 59. Dictionary Unpacking with `**`

```python
a = {
    "name": "Teja"
}

b = {
    "age": 21
}

student = {
    **a,
    **b
}

print(student)

# Output:
# {'name': 'Teja', 'age': 21}
```

---

## 60. Merging Dictionaries

Modern Python also supports:

```python
a = {"x": 10}
b = {"y": 20}

c = a | b

print(c)

# Output:
# {'x': 10, 'y': 20}
```

If the same key exists, the value from the right-hand dictionary is used.

---

# Dictionary Functions

## 61. `len()`

```python
d = {"a": 10, "b": 20}

print(len(d))

# Output:
# 2
```

---

## 62. `type()`

```python
d = {}

print(type(d))

# Output:
# <class 'dict'>
```

---

## 63. `isinstance()`

```python
d = {}

print(isinstance(d, dict))

# Output:
# True
```

---

# Dictionary and Mutable Objects

## 64. Nested Mutable Objects

A dictionary can contain mutable objects such as lists.

```python
student = {
    "skills": ["Python", "SQL"]
}

student["skills"].append("Git")

print(student)

# Output:
# {'skills': ['Python', 'SQL', 'Git']}
```

The dictionary itself is mutable, and the list inside it is also mutable.

---

# Important Dictionary Properties

## 65. Dictionary Is Mutable

We can add, remove and modify elements.

```python
d = {"a": 10}

d["a"] = 20
d["b"] = 30
```

---

## 66. Dictionary Does Not Use Numeric Indexing

This is incorrect:

```python
d = {
    "name": "Teja",
    "age": 21
}

print(d[0])
```

Dictionary elements are accessed using their keys.

```python
print(d["name"])
```

---

## 67. Dictionary Allows Duplicate Values

```python
d = {
    "a": 10,
    "b": 10
}
```

This is valid.

---

## 68. Dictionary Does Not Allow Duplicate Keys

```python
d = {
    "a": 10,
    "a": 20
}
```

Only the last value remains:

```python
{'a': 20}
```

---

# Dictionary Time Complexity

For a normal Python dictionary, the average time complexity of common operations is approximately:

| Operation | Average Time |
|---|---:|
| Access `d[key]` | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| `key in d` | O(1) |
| `get()` | O(1) |
| `len()` | O(1) |

However, these are **average-case** complexities. Hash collisions can affect individual operations.

---

# Dictionary vs Other Data Types

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Ordered | Yes | Yes | No positional order | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No |
| Indexing | Yes | Yes | No | By key |
| Key-Value pairs | No | No | No | Yes |
| Fast membership | Usually O(n) | Usually O(n) | Average O(1) | Average O(1) |

---

# Important Dictionary Methods

| Method | Purpose |
|---|---|
| `get()` | Get value safely |
| `keys()` | Get keys |
| `values()` | Get values |
| `items()` | Get key-value pairs |
| `update()` | Add/update multiple values |
| `setdefault()` | Add key if missing |
| `pop()` | Remove specified key |
| `popitem()` | Remove last inserted pair |
| `clear()` | Remove everything |
| `copy()` | Create a shallow copy |
| `fromkeys()` | Create dictionary from keys |

---

# Important Points to Remember

1. Dictionary stores data as **key-value pairs**.
2. Keys must be **unique**.
3. Values can be duplicated.
4. Keys must be **hashable**.
5. Dictionary is **mutable**.
6. Dictionary preserves **insertion order**.
7. Dictionary does not use positional indexing.
8. `d[key]` raises `KeyError` if the key does not exist.
9. `d.get(key)` returns `None` by default when the key is missing.
10. `get()` can also accept a default value.
11. `{}` creates an empty dictionary.
12. `set()` creates an empty set.
13. `keys()`, `values()` and `items()` return view objects.
14. `in` checks dictionary keys by default.
15. `True` and `1` are considered the same dictionary key.
16. `False` and `0` are considered the same dictionary key.
17. Lists cannot be dictionary keys because they are unhashable.
18. Tuples can be dictionary keys if their elements are hashable.
19. Dictionaries can contain lists, sets, tuples and other dictionaries as values.
20. Dictionary comprehension provides a short way to create dictionaries.

---

# Quick Revision

```text
Dictionary
    ↓
Key : Value
    ↓
Keys → Unique + Hashable
Values → Can be duplicated
    ↓
Mutable
    ↓
Ordered by insertion
    ↓
Access using keys
    ↓
Average O(1) lookup
```

Example:

```python
student = {
    "name": "Teja",
    "age": 21,
    "branch": "CSE"
}

print(student["name"])
print(student.get("age"))

student["cgpa"] = 8.43

for key, value in student.items():
    print(key, value)
```

A dictionary is especially useful when data needs to be represented as a relationship between a **key and its corresponding value**.