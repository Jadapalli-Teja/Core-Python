# Python Dictionary

A **dictionary (`dict`)** is a built-in Python data type used to store data in **key-value pairs**.

```python
student = {
    "name": "Teja",
    "age": 21,
    "branch": "CSE"
}
```

Here:

- `"name"` → key
- `"Teja"` → value
- `"age"` → key
- `21` → value

A dictionary is mainly used when we want to store and retrieve data using a **key** instead of an index.

---

## 1. Main Characteristics of Dictionary

A dictionary is:

- **Mutable** → we can add, change, and remove items.
- **Ordered** → maintains insertion order in modern Python.
- **Indexed by keys** → values are accessed using keys.
- **Does not allow duplicate keys**.
- **Allows duplicate values**.
- **Keys must be hashable**.
- **Values can be of any data type**.
- **Can contain different data types**.
- **Can contain nested dictionaries**.
- **Dynamic** → its size can change.
- **Iterable** → we can loop through it.
- **Dictionary itself is unhashable**.

Example:

```python
student = {
    "name": "Teja",
    "age": 21,
    "marks": 85
}
```

---

# 2. Creating a Dictionary

We create a dictionary using `{}`.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student)

# Output:
# {'name': 'Teja', 'age': 21}
```

The general syntax is:

```python
dictionary = {
    key1: value1,
    key2: value2
}
```

---

# 3. Empty Dictionary

An empty dictionary can be created using `{}`.

```python
data = {}

print(data)
print(type(data))

# Output:
# {}
# <class 'dict'>
```

We can also use `dict()`:

```python
data = dict()

print(data)

# Output:
# {}
```

### Important

```python
{}
```

creates an empty **dictionary**, not a set.

An empty set is:

```python
set()
```

---

# 4. Dictionary with Different Data Types

Keys and values can contain different data types.

```python
data = {
    "name": "Teja",
    "age": 21,
    "cgpa": 8.5,
    "passed": True
}

print(data)
```

Here the values have different types:

```text
"name"   → str
"age"    → int
"cgpa"   → float
"passed" → bool
```

---

# 5. Key-Value Pair

A dictionary stores information in this form:

```text
key : value
```

Example:

```python
student = {
    "name": "Teja",
    "age": 21
}
```

Conceptually:

```text
"name" ──> "Teja"
"age"  ──> 21
```

The key is used to find its corresponding value.

---

# 6. Accessing Values Using Keys

We can access a value using its key.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student["name"])
print(student["age"])

# Output:
# Teja
# 21
```

Syntax:

```python
dictionary[key]
```

---

# 7. What Happens If the Key Does Not Exist?

If we use a key that does not exist, Python raises `KeyError`.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student["marks"])
```

Output:

```text
KeyError: 'marks'
```

This is why `get()` is often useful when the key may not exist.

---

# 8. Using get()

`get()` returns the value for a key.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student.get("name"))

# Output:
# Teja
```

If the key does not exist:

```python
print(student.get("marks"))

# Output:
# None
```

We can also provide a default value:

```python
print(student.get("marks", 0))

# Output:
# 0
```

### `[]` vs `get()`

```python
student["marks"]
```

→ raises `KeyError` if key is missing.

```python
student.get("marks")
```

→ returns `None` if key is missing.

---

# 9. Dictionary Keys Must Be Unique

A dictionary cannot have duplicate keys.

```python
data = {
    "name": "Teja",
    "name": "Praveen"
}

print(data)

# Output:
# {'name': 'Praveen'}
```

The second value replaces the first value.

So:

```python
"name": "Teja"
```

is replaced by:

```python
"name": "Praveen"
```

---

# 10. Duplicate Values Are Allowed

Values can be duplicated.

```python
students = {
    "student1": "CSE",
    "student2": "CSE",
    "student3": "CSE"
}

print(students)
```

This is valid because the **keys are different**.

---

# 11. Adding a New Key-Value Pair

We can add a new item using:

```python
dictionary[key] = value
```

Example:

```python
student = {
    "name": "Teja",
    "age": 21
}

student["branch"] = "CSE"

print(student)

# Output:
# {'name': 'Teja', 'age': 21, 'branch': 'CSE'}
```

---

# 12. Changing an Existing Value

If the key already exists, assignment changes its value.

```python
student = {
    "name": "Teja",
    "age": 21
}

student["age"] = 22

print(student)

# Output:
# {'name': 'Teja', 'age': 22}
```

The same syntax performs two different operations:

```python
dictionary[key] = value
```

- New key → adds an item
- Existing key → changes the value

---

# 13. Dictionary is Mutable

A dictionary is mutable.

This means we can change it after creating it.

```python
student = {
    "name": "Teja",
    "age": 21
}

student["age"] = 22

print(student)

# Output:
# {'name': 'Teja', 'age': 22}
```

We can:

- Add items
- Modify values
- Remove items

---

# 14. Dictionary Insertion Order

Modern Python dictionaries preserve insertion order.

```python
data = {}

data["a"] = 10
data["b"] = 20
data["c"] = 30

print(data)

# Output:
# {'a': 10, 'b': 20, 'c': 30}
```

The order in which items are inserted is maintained when iterating.

However, dictionaries should primarily be thought of as **key-value mappings**, not index-based sequences.

---

# 15. Dictionary Does Not Use Numeric Indexes

A list uses indexes:

```python
numbers = [10, 20, 30]

print(numbers[0])
```

A dictionary uses keys:

```python
numbers = {
    "first": 10,
    "second": 20,
    "third": 30
}

print(numbers["first"])
```

This is invalid:

```python
print(numbers[0])
```

unless `0` itself is a key.

---

# 16. Dictionary Keys Must Be Hashable

This is an important concept.

Dictionary keys must be **hashable**.

Common hashable types:

```text
int
float
str
bool
tuple (if its elements are hashable)
frozenset
None
```

Example:

```python
data = {
    1: "one",
    "name": "Teja",
    3.14: "pi",
    True: "yes"
}

print(data)
```

These are valid keys because they are hashable.

---

# 17. Why Must Dictionary Keys Be Hashable?

Dictionaries use a **hash table** internally.

When a key is stored, Python uses its hash value to efficiently find the corresponding value.

Conceptually:

```text
Key
 ↓
hash(key)
 ↓
Hash Table
 ↓
Value
```

This is why dictionary keys must have a stable hash value.

---

# 18. Dictionary Itself Is NOT Hashable

This is a very important distinction.

A dictionary is:

- Mutable
- Unhashable

Example:

```python
data = {
    "name": "Teja"
}

print(hash(data))
```

This gives:

```text
TypeError: unhashable type: 'dict'
```

So:

> **A dictionary can contain hashable keys, but the dictionary itself is not hashable.**

---

# 19. Dictionary Cannot Be a Set Element

Set elements must be hashable.

A dictionary is unhashable.

Therefore this is invalid:

```python
data = {
    {1: "one"}
}
```

Python tries to create a set containing a dictionary.

It gives:

```text
TypeError: unhashable type: 'dict'
```

Compare:

```python
data = {1, 2, 3}
```

Valid because integers are hashable.

But:

```python
data = {[1, 2, 3]}
```

Invalid because lists are unhashable.

And:

```python
data = {{1: "one"}}
```

Invalid because dictionaries are unhashable.

---

# 20. Dictionary Cannot Be a Dictionary Key

This is also invalid:

```python
data = {
    {"name": "Teja"}: "student"
}
```

A dictionary cannot be used as a key because it is unhashable.

You may remember:

> **Dictionary keys must be hashable.**

---

# 21. Dictionary Values Can Be Any Data Type

Unlike keys, values do not have to be hashable.

A dictionary can contain lists, sets, dictionaries, etc. as values.

```python
data = {
    "numbers": [1, 2, 3],
    "skills": {"Python", "SQL"},
    "details": {
        "age": 21,
        "branch": "CSE"
    }
}

print(data)
```

This is valid.

So:

```text
Key   → must be hashable
Value → can be any type
```

This is one of the most important dictionary rules.

---

# 22. Tuple as a Dictionary Key

A tuple can be used as a key if all its elements are hashable.

```python
data = {
    (10, 20): "point"
}

print(data[(10, 20)])

# Output:
# point
```

But this is invalid:

```python
data = {
    ([10, 20],): "point"
}
```

because the tuple contains a list, and the list is unhashable.

So tuple hashability depends on its contents.

---

# 23. Dictionary Methods

Python provides many useful dictionary methods.

Important methods include:

```text
get()
keys()
values()
items()
update()
setdefault()
pop()
popitem()
clear()
copy()
fromkeys()
```

---

# 24. keys()

`keys()` returns the dictionary's keys.

```python
student = {
    "name": "Teja",
    "age": 21,
    "branch": "CSE"
}

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'branch'])
```

We can convert it to a list:

```python
print(list(student.keys()))

# Output:
# ['name', 'age', 'branch']
```

---

# 25. values()

`values()` returns the dictionary's values.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student.values())

# Output:
# dict_values(['Teja', 21])
```

---

# 26. items()

`items()` returns key-value pairs.

```python
student = {
    "name": "Teja",
    "age": 21
}

print(student.items())

# Output:
# dict_items([('name', 'Teja'), ('age', 21)])
```

Each item behaves like a tuple:

```text
("name", "Teja")
("age", 21)
```

---

# 27. Iterating Through a Dictionary

By default, looping through a dictionary gives its keys.

```python
student = {
    "name": "Teja",
    "age": 21
}

for key in student:
    print(key)

# Output:
# name
# age
```

---

# 28. Loop Through Values

Use `values()`.

```python
student = {
    "name": "Teja",
    "age": 21
}

for value in student.values():
    print(value)

# Output:
# Teja
# 21
```

---

# 29. Loop Through Keys and Values

Use `items()`.

```python
student = {
    "name": "Teja",
    "age": 21
}

for key, value in student.items():
    print(key, value)

# Output:
# name Teja
# age 21
```

This is one of the most commonly used dictionary patterns.

---

# 30. Membership Testing

`in` checks keys by default.

```python
student = {
    "name": "Teja",
    "age": 21
}

print("name" in student)
print("marks" in student)

# Output:
# True
# False
```

Important:

```python
"Teja" in student
```

checks whether `"Teja"` is a **key**, not a value.

To check values:

```python
print("Teja" in student.values())

# Output:
# True
```

---

# 31. len()

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

# 32. update()

`update()` adds new items or changes existing items.

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

# Output:
# {'name': 'Teja', 'age': 22, 'branch': 'CSE'}
```

Here:

```text
age    → changed
branch → added
```

---

# 33. setdefault()

`setdefault()` returns the value of a key.

If the key does not exist, it adds the key with the given default value.

```python
student = {
    "name": "Teja"
}

result = student.setdefault("age", 21)

print(result)
print(student)

# Output:
# 21
# {'name': 'Teja', 'age': 21}
```

If the key already exists:

```python
student = {
    "age": 21
}

student.setdefault("age", 25)

print(student)

# Output:
# {'age': 21}
```

The existing value is not replaced.

---

# 34. Removing an Item Using pop()

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

# 35. pop() with a Default Value

If the key may not exist, a default can be supplied.

```python
student = {
    "name": "Teja"
}

result = student.pop("age", 0)

print(result)

# Output:
# 0
```

Without a default, a missing key raises `KeyError`.

---

# 36. popitem()

`popitem()` removes and returns the last inserted key-value pair.

```python
student = {
    "name": "Teja",
    "age": 21
}

item = student.popitem()

print(item)
print(student)

# Output:
# ('age', 21)
# {'name': 'Teja'}
```

---

# 37. clear()

`clear()` removes all items.

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

# 38. del

`del` can remove a specific key.

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

We can also delete the entire dictionary:

```python
del student
```

After this, using `student` causes `NameError` because the variable no longer exists.

---

# 39. Nested Dictionary

A dictionary can contain another dictionary as a value.

```python
student = {
    "name": "Teja",
    "details": {
        "age": 21,
        "branch": "CSE"
    }
}

print(student["details"]["age"])

# Output:
# 21
```

Conceptually:

```text
student
│
├── name → Teja
│
└── details
      ├── age → 21
      └── branch → CSE
```

Nested dictionaries are commonly used for structured data.

---

# 40. Dictionary Inside a List

A list can contain dictionaries.

```python
students = [
    {"name": "Teja", "age": 21},
    {"name": "Praveen", "age": 22}
]

print(students[0]["name"])

# Output:
# Teja
```

This structure is very common when working with records.

---

# 41. List Inside a Dictionary

A dictionary can contain a list as a value.

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

# 42. Dictionary Comprehension

Dictionary comprehensions provide a short way to create dictionaries.

Example:

```python
squares = {
    x: x * x
    for x in range(1, 6)
}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

General syntax:

```python
{key: value for item in iterable}
```

With condition:

```python
squares = {
    x: x * x
    for x in range(1, 6)
    if x % 2 == 0
}

print(squares)

# Output:
# {2: 4, 4: 16}
```

---

# 43. Creating Dictionary Using zip()

`zip()` can combine keys and values.

```python
keys = ["name", "age", "branch"]
values = ["Teja", 21, "CSE"]

student = dict(zip(keys, values))

print(student)

# Output:
# {'name': 'Teja', 'age': 21, 'branch': 'CSE'}
```

---

# 44. Creating Dictionary from Pairs

We can create a dictionary from a sequence of key-value pairs.

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

---

# 45. fromkeys()

`fromkeys()` creates a dictionary using a sequence of keys.

```python
keys = ["name", "age", "branch"]

data = dict.fromkeys(keys)

print(data)

# Output:
# {'name': None, 'age': None, 'branch': None}
```

We can provide a common value:

```python
data = dict.fromkeys(keys, 0)

print(data)

# Output:
# {'name': 0, 'age': 0, 'branch': 0}
```

---

# 46. Dictionary References

Two variables can refer to the same dictionary.

```python
a = {
    "name": "Teja"
}

b = a

b["age"] = 21

print(a)

# Output:
# {'name': 'Teja', 'age': 21}
```

Why?

```text
a ──┐
    ├──> same dictionary object
b ──┘
```

`a` and `b` refer to the same object.

---

# 47. == vs is

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

The contents are equal, but they are different dictionary objects.

---

# 48. Copying a Dictionary

`copy()` creates a shallow copy.

```python
a = {
    "name": "Teja"
}

b = a.copy()

b["age"] = 21

print(a)
print(b)

# Output:
# {'name': 'Teja'}
# {'name': 'Teja', 'age': 21}
```

Now `a` and `b` are separate dictionary objects.

---

# 49. Shallow Copy with Nested Data

For nested mutable objects, a shallow copy does not completely duplicate everything.

```python
a = {
    "numbers": [1, 2, 3]
}

b = a.copy()

b["numbers"].append(4)

print(a)
print(b)
```

Output:

```text
{'numbers': [1, 2, 3, 4]}
{'numbers': [1, 2, 3, 4]}
```

The outer dictionaries are different, but the nested list is shared.

For completely independent nested data, `copy.deepcopy()` can be used.

---

# 50. Dictionary Truth Value

An empty dictionary is considered `False`.

A non-empty dictionary is considered `True`.

```python
print(bool({}))
print(bool({"a": 1}))

# Output:
# False
# True
```

Therefore:

```python
data = {}

if data:
    print("Not empty")
else:
    print("Empty")

# Output:
# Empty
```

---

# 51. Dictionary with None Values

`None` can be used as a value.

```python
student = {
    "name": "Teja",
    "marks": None
}

print(student)

# Output:
# {'name': 'Teja', 'marks': None}
```

`None` can also be a key because `None` is hashable:

```python
data = {
    None: "No value"
}

print(data)

# Output:
# {None: 'No value'}
```

---

# 52. Boolean Keys and Integer Keys

Be careful with `True` and `1`.

In Python:

```python
True == 1
```

is `True`.

Similarly:

```python
False == 0
```

is `True`.

Therefore:

```python
data = {
    True: "A",
    1: "B"
}

print(data)
```

The keys collide because `True` and `1` are considered equal as dictionary keys.

The same concept applies to `False` and `0`.

---

# 53. Useful Built-in Functions

Some useful functions with dictionaries:

```python
data = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(len(data))
print(type(data))
print(isinstance(data, dict))
```

Other useful functions include:

```python
min()
max()
sum()
any()
all()
```

For example:

```python
numbers = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(sum(numbers.values()))

# Output:
# 60
```

---

# 54. Sorting Dictionary Keys

`sorted()` returns a list of sorted keys by default.

```python
data = {
    "c": 30,
    "a": 10,
    "b": 20
}

print(sorted(data))

# Output:
# ['a', 'b', 'c']
```

To sort based on values:

```python
data = {
    "a": 30,
    "b": 10,
    "c": 20
}

result = sorted(data.items(), key=lambda item: item[1])

print(result)

# Output:
# [('b', 10), ('c', 20), ('a', 30)]
```

---

# 55. Dictionary Unpacking

Dictionaries can be unpacked using `**`.

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

This is useful for combining dictionaries.

---

# 56. Dictionary Merge Operator

Python also provides `|` for merging dictionaries.

```python
a = {
    "name": "Teja"
}

b = {
    "age": 21
}

result = a | b

print(result)

# Output:
# {'name': 'Teja', 'age': 21}
```

If the same key exists, the value from the right-hand dictionary is used.

```python
a = {"age": 21}
b = {"age": 22}

print(a | b)

# Output:
# {'age': 22}
```

---

# 57. Dictionary Methods Quick Reference

| Method | Purpose |
|---|---|
| `get()` | Get a value safely |
| `keys()` | Get all keys |
| `values()` | Get all values |
| `items()` | Get key-value pairs |
| `update()` | Add/change multiple items |
| `setdefault()` | Get value or insert default |
| `pop()` | Remove a specified key |
| `popitem()` | Remove last inserted pair |
| `clear()` | Remove all items |
| `copy()` | Create a shallow copy |
| `fromkeys()` | Create dictionary from keys |

---

# 58. Dictionary vs List

| Feature | Dictionary | List |
|---|---|---|
| Data storage | Key-value | Values |
| Access | Key | Index |
| Mutable | Yes | Yes |
| Duplicates | Duplicate keys not allowed | Allowed |
| Ordered | Yes | Yes |
| Hashable | No | No |
| Main use | Mapping data | Ordered collection |

Example:

```python
student = {
    "name": "Teja",
    "age": 21
}
```

vs

```python
student = ["Teja", 21]
```

The dictionary gives meaningful names to the data.

---

# 59. Dictionary vs Set

Both use hashing internally, but they are different.

### Set

```python
data = {1, 2, 3}
```

Stores only values.

### Dictionary

```python
data = {
    "a": 1,
    "b": 2
}
```

Stores key-value pairs.

Important:

```text
Set       → value
Dictionary → key : value
```

Also:

```text
set       → mutable and unhashable
dict      → mutable and unhashable
```

---

# 60. Dictionary vs Tuple

| Feature | Dictionary | Tuple |
|---|---|---|
| Mutable | Yes | No |
| Access | Key | Index |
| Duplicate keys | No | Duplicates allowed |
| Ordered | Yes | Yes |
| Hashable | No | Usually yes if contents are hashable |
| Structure | Key-value | Sequence |

---

# 61. Dictionary Time Complexity

Because dictionaries use hash tables, common operations are generally very fast.

Average time complexity:

| Operation | Average |
|---|---:|
| Access by key | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Membership by key | O(1) |

These are **average-case** complexities.

In unusual collision situations, performance can differ.

---

# 62. How Dictionary Access Works Conceptually

Suppose:

```python
student = {
    "name": "Teja",
    "age": 21
}
```

When we write:

```python
student["age"]
```

Conceptually Python uses the key's hash:

```text
"age"
  ↓
hash("age")
  ↓
hash table lookup
  ↓
21
```

This is why dictionary lookup is generally much faster than searching through a list one item at a time.

---

# 63. Common Mistakes

### Mistake 1: Using duplicate keys

```python
data = {
    "name": "Teja",
    "name": "Praveen"
}
```

Only the last value remains.

---

### Mistake 2: Using a list as a key

```python
data = {
    [1, 2]: "numbers"
}
```

Invalid:

```text
TypeError: unhashable type: 'list'
```

---

### Mistake 3: Using a dictionary as a key

```python
data = {
    {"a": 1}: "value"
}
```

Invalid because dictionary is unhashable.

---

### Mistake 4: Using a dictionary as a set element

```python
data = {
    {"a": 1}
}
```

Invalid because set elements must be hashable.

---

### Mistake 5: Assuming `in` checks values

```python
data = {
    "name": "Teja"
}

print("Teja" in data)
```

This checks keys, so the result is:

```text
False
```

To check values:

```python
print("Teja" in data.values())

# Output:
# True
```

---

# 64. Important Hashability Rule

Remember this clearly:

```text
Dictionary
   │
   ├── Keys → MUST be hashable
   │
   └── Values → Can be any data type
```

And:

```text
dict → mutable → unhashable
```

Therefore:

```text
Can dictionary be a dictionary key?     ❌ No
Can dictionary be a set element?       ❌ No
Can dictionary contain a list value?   ✅ Yes
Can dictionary contain a set value?    ✅ Yes
Can dictionary contain a list key?     ❌ No
Can dictionary contain a tuple key?    ✅ Yes, if tuple is hashable
```

This distinction is very important.

---

# 65. Practical Example

A student record can be represented naturally using a dictionary:

```python
student = {
    "name": "Teja",
    "age": 21,
    "branch": "CSE",
    "skills": ["Python", "SQL", "Git"],
    "marks": {
        "Python": 85,
        "SQL": 80
    }
}

print(student["name"])
print(student["skills"])
print(student["marks"]["Python"])

# Output:
# Teja
# ['Python', 'SQL', 'Git']
# 85
```

This shows how dictionaries can represent structured information.

---

# 66. When Should We Use a Dictionary?

Use a dictionary when data has a natural **key → value** relationship.

Examples:

```text
Student information
Employee information
Product details
Configuration settings
API/JSON data
Counting frequencies
Lookup tables
Database-like records
```

Example:

```python
product = {
    "id": 101,
    "name": "Laptop",
    "price": 50000
}
```

Here each key describes what the value represents.

---

# 67. Quick Revision

```text
Dictionary
│
├── Stores key-value pairs
├── Mutable
├── Ordered
├── No duplicate keys
├── Duplicate values allowed
├── Accessed using keys
├── Keys must be hashable
├── Values can be any type
├── Dictionary itself is unhashable
├── Supports nested data
├── Supports iteration
└── Uses hashing for efficient lookup
```

Important syntax:

```python
data = {
    "name": "Teja",
    "age": 21
}
```

Access:

```python
data["name"]
```

Add:

```python
data["branch"] = "CSE"
```

Change:

```python
data["age"] = 22
```

Delete:

```python
del data["age"]
```

Safe access:

```python
data.get("age")
```

Loop:

```python
for key, value in data.items():
    print(key, value)
```

---

# 68. One-Line Definition

> **A dictionary is a mutable, ordered collection of key-value pairs where keys must be hashable and unique, while values can be of any data type.**