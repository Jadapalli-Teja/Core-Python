# List in Python

A **list** is a built-in Python data type used to store multiple values in a single variable.

A list is:

- **Ordered**
- **Mutable**
- **Indexed**
- **Allows duplicate values**
- **Allows different data types**
- **Allows nested lists**
- **Iterable**
- **Dynamic in size**

Example:

```python
numbers = [10, 20, 30, 40]

print(numbers)

# Output:
# [10, 20, 30, 40]
```

---

# 1. Creating a List

The most common way to create a list is using square brackets `[]`.

```python
numbers = [10, 20, 30]

print(numbers)

# Output:
# [10, 20, 30]
```

The values inside a list are called **elements**.

```text
numbers = [10, 20, 30]
           ↓   ↓   ↓
        element element element
```

---

# 2. Empty List

An empty list contains no elements.

```python
numbers = []

print(numbers)

# Output:
# []
```

You can add elements later.

```python
numbers = []

numbers.append(10)
numbers.append(20)

print(numbers)

# Output:
# [10, 20]
```

---

# 3. Creating a List Using `list()`

Python provides the `list()` constructor.

```python
numbers = list([10, 20, 30])

print(numbers)

# Output:
# [10, 20, 30]
```

More commonly:

```python
numbers = list((10, 20, 30))

print(numbers)

# Output:
# [10, 20, 30]
```

---

# 4. List from a String

A string is iterable, so `list()` creates one element for each character.

```python
name = "Python"

letters = list(name)

print(letters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']
```

---

# 5. List from a Tuple

```python
data = (10, 20, 30)

numbers = list(data)

print(numbers)

# Output:
# [10, 20, 30]
```

---

# 6. List from a Set

```python
data = {10, 20, 30}

numbers = list(data)

print(numbers)
```

The order should not be relied upon because a set is unordered.

---

# 7. List from a Range

```python
numbers = list(range(1, 6))

print(numbers)

# Output:
# [1, 2, 3, 4, 5]
```

---

# 8. Lists Can Store Different Data Types

A list does not require all elements to have the same type.

```python
data = [10, 3.14, "Python", True, None]

print(data)

# Output:
# [10, 3.14, 'Python', True, None]
```

This is called a **heterogeneous list**.

---

# 9. List of Same Data Type

A list can also contain elements of the same type.

```python
numbers = [10, 20, 30, 40]

names = ["Teja", "Ravi", "Kiran"]
```

---

# 10. Duplicate Elements

Lists allow duplicate values.

```python
numbers = [10, 20, 10, 30, 20]

print(numbers)

# Output:
# [10, 20, 10, 30, 20]
```

Unlike a set, duplicates are not automatically removed.

---

# 11. Lists Are Ordered

A list remembers the order in which elements are stored.

```python
numbers = [30, 10, 20]

print(numbers)

# Output:
# [30, 10, 20]
```

The order remains:

```text
30 → 10 → 20
```

---

# 12. Indexing

Every list element has an index.

Indexing starts from `0`.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

# Output:
# 10
# 20
# 30
# 40
```

The structure is:

```text
Value:    10    20    30    40
Index:     0     1     2     3
```

---

# 13. Negative Indexing

Python also supports negative indexes.

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])

# Output:
# 40
# 30
# 20
```

Structure:

```text
Positive:   0     1     2     3
           10    20    30    40
Negative:  -4    -3    -2    -1
```

---

# 14. Index Out of Range

Trying to access an index that does not exist causes `IndexError`.

```python
numbers = [10, 20, 30]

# print(numbers[5])
```

This raises:

```text
IndexError: list index out of range
```

---

# 15. Changing an Element

Lists are **mutable**, so elements can be changed.

```python
numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)

# Output:
# [10, 200, 30]
```

This is one of the most important properties of a list.

---

# 16. Adding Elements

## `append()`

`append()` adds **one element at the end**.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# Output:
# [10, 20, 30, 40]
```

---

# 17. `append()` Adds One Object

This is important:

```python
numbers = [10, 20]

numbers.append([30, 40])

print(numbers)

# Output:
# [10, 20, [30, 40]]
```

The entire `[30, 40]` becomes one element.

```text
[10, 20, [30, 40]]
          ↑
       one element
```

---

# 18. `insert()`

`insert(index, value)` adds an element at a specific position.

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)

# Output:
# [10, 15, 20, 30]
```

Here `15` is inserted at index `1`.

---

# 19. `extend()`

`extend()` adds multiple elements from an iterable.

```python
numbers = [10, 20]

numbers.extend([30, 40, 50])

print(numbers)

# Output:
# [10, 20, 30, 40, 50]
```

---

# 20. `append()` vs `extend()`

This is an important interview concept.

### `append()`

```python
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

# Output:
# [1, 2, [3, 4]]
```

### `extend()`

```python
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)

# Output:
# [1, 2, 3, 4]
```

Difference:

```text
append()
→ adds the object as one element

extend()
→ adds elements from the iterable
```

---

# 21. Concatenating Lists

Two lists can be combined using `+`.

```python
a = [1, 2]
b = [3, 4]

result = a + b

print(result)

# Output:
# [1, 2, 3, 4]
```

The original lists are not modified.

---

# 22. Repeating a List

Use `*`.

```python
numbers = [1, 2]

result = numbers * 3

print(result)

# Output:
# [1, 2, 1, 2, 1, 2]
```

---

# 23. Membership

Use `in` to check whether an element exists.

```python
numbers = [10, 20, 30]

print(20 in numbers)

# Output:
# True
```

---

# 24. `not in`

```python
numbers = [10, 20, 30]

print(50 not in numbers)

# Output:
# True
```

---

# 25. Length of a List

Use `len()`.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))

# Output:
# 4
```

---

# 26. Removing Elements

## `remove()`

`remove(value)` removes the **first matching value**.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

# Output:
# [10, 30, 20]
```

Only the first `20` is removed.

---

# 27. `remove()` with Missing Value

```python
numbers = [10, 20, 30]

# numbers.remove(50)
```

This raises:

```text
ValueError: list.remove(x): x not in list
```

---

# 28. `pop()`

`pop()` removes and returns an element.

Without an index, it removes the last element.

```python
numbers = [10, 20, 30]

value = numbers.pop()

print(value)
print(numbers)

# Output:
# 30
# [10, 20]
```

---

# 29. `pop(index)`

You can specify an index.

```python
numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
print(numbers)

# Output:
# 20
# [10, 30]
```

---

# 30. `clear()`

Removes all elements.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)

# Output:
# []
```

The list still exists; it simply becomes empty.

---

# 31. `del`

`del` can remove an element using its index.

```python
numbers = [10, 20, 30]

del numbers[1]

print(numbers)

# Output:
# [10, 30]
```

---

# 32. Delete Multiple Elements

```python
numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)

# Output:
# [10, 50]
```

---

# 33. Delete the Entire List

```python
numbers = [10, 20, 30]

del numbers
```

After this, the variable `numbers` no longer exists.

---

# Slicing

## 34. Basic Slicing

Syntax:

```text
list[start:stop]
```

`stop` is excluded.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Output:
# [20, 30, 40]
```

---

# 35. Slice from Beginning

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

# Output:
# [10, 20, 30]
```

---

# 36. Slice to the End

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2:])

# Output:
# [30, 40, 50]
```

---

# 37. Copy Using Slicing

```python
numbers = [10, 20, 30]

copy_numbers = numbers[:]

print(copy_numbers)

# Output:
# [10, 20, 30]
```

This creates a new list.

---

# 38. Step in Slicing

Syntax:

```text
list[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])

# Output:
# [10, 30, 50]
```

---

# 39. Reverse a List Using Slicing

```python
numbers = [10, 20, 30, 40]

print(numbers[::-1])

# Output:
# [40, 30, 20, 10]
```

This creates a reversed copy.

---

# Searching in a List

## 40. `index()`

Returns the index of the first occurrence.

```python
numbers = [10, 20, 30, 20]

print(numbers.index(20))

# Output:
# 1
```

---

# 41. `count()`

Counts how many times a value occurs.

```python
numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))

# Output:
# 3
```

---

# Sorting

## 42. `sort()`

`sort()` changes the original list.

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30, 40]
```

---

# 43. Descending Order

```python
numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# Output:
# [40, 30, 20, 10]
```

---

# 44. `sorted()`

`sorted()` creates a new sorted list.

```python
numbers = [40, 10, 30, 20]

result = sorted(numbers)

print(result)
print(numbers)

# Output:
# [10, 20, 30, 40]
# [40, 10, 30, 20]
```

Difference:

```text
sort()
→ modifies original list

sorted()
→ returns a new sorted list
```

---

# Reversing

## 45. `reverse()`

Reverses the original list.

```python
numbers = [10, 20, 30]

numbers.reverse()

print(numbers)

# Output:
# [30, 20, 10]
```

---

# 46. `[::-1]` vs `reverse()`

```python
numbers = [10, 20, 30]

result = numbers[::-1]

print(result)
print(numbers)

# Output:
# [30, 20, 10]
# [10, 20, 30]
```

`[::-1]` creates a new list.

But:

```python
numbers.reverse()
```

changes the original list.

---

# Nested Lists

## 47. List Inside a List

A list can contain another list.

```python
data = [10, [20, 30], 40]

print(data)

# Output:
# [10, [20, 30], 40]
```

This is called a **nested list**.

---

# 48. Accessing Nested List

```python
data = [10, [20, 30], 40]

print(data[1])

# Output:
# [20, 30]
```

---

# 49. Accessing Nested Element

```python
data = [10, [20, 30], 40]

print(data[1][0])

# Output:
# 20
```

Think step-by-step:

```text
data[1]
   ↓
[20, 30]

data[1][0]
      ↓
     20
```

---

# 50. Changing Nested Elements

```python
data = [10, [20, 30], 40]

data[1][0] = 200

print(data)

# Output:
# [10, [200, 30], 40]
```

---

# List of Lists

Lists are commonly used to represent tables or matrices.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Access:

```python
print(matrix[1][2])

# Output:
# 6
```

---

# List Comprehension

List comprehension provides a compact way to create lists.

## 51. Basic List Comprehension

```python
numbers = [x for x in range(1, 6)]

print(numbers)

# Output:
# [1, 2, 3, 4, 5]
```

---

# 52. Squares

```python
squares = [x * x for x in range(1, 6)]

print(squares)

# Output:
# [1, 4, 9, 16, 25]
```

---

# 53. List Comprehension with Condition

```python
numbers = [x for x in range(1, 11) if x % 2 == 0]

print(numbers)

# Output:
# [2, 4, 6, 8, 10]
```

Basic structure:

```text
[expression for item in iterable if condition]
```

---

# 54. Nested List Comprehension

```python
matrix = [[0 for j in range(3)] for i in range(2)]

print(matrix)

# Output:
# [[0, 0, 0], [0, 0, 0]]
```

---

# Iterating Through a List

## 55. Using `for`

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
```

---

# 56. Using `enumerate()`

`enumerate()` gives both index and value.

```python
names = ["Teja", "Ravi", "Kiran"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```text
0 Teja
1 Ravi
2 Kiran
```

---

# List Unpacking

## 57. Basic Unpacking

```python
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

# Output:
# 10
# 20
# 30
```

The number of variables must normally match the number of elements.

---

# 58. Extended Unpacking

Using `*`, multiple elements can be collected.

```python
numbers = [10, 20, 30, 40]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30]
# 40
```

---

# List References

## 59. Two Variables Can Refer to the Same List

```python
a = [10, 20, 30]

b = a

b.append(40)

print(a)
print(b)

# Output:
# [10, 20, 30, 40]
# [10, 20, 30, 40]
```

Why?

```text
a ─────┐
       ↓
    [10, 20, 30]
       ↑
       │
b ─────┘
```

Both variables refer to the same list object.

---

# 60. `==` vs `is`

```python
a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)

# Output:
# True
# False
```

`==` checks whether the contents are equal.

`is` checks whether both variables refer to the same object.

---

# 61. Creating a Separate Copy

Use `.copy()`.

```python
a = [10, 20, 30]

b = a.copy()

b.append(40)

print(a)
print(b)

# Output:
# [10, 20, 30]
# [10, 20, 30, 40]
```

Now they are separate list objects.

---

# 62. Shallow Copy

`.copy()` creates a **shallow copy**.

For a simple list:

```python
a = [10, 20, 30]

b = a.copy()
```

The outer list is different.

But with nested mutable objects, the inner objects can still be shared.

```python
a = [[1, 2], [3, 4]]

b = a.copy()

b[0].append(100)

print(a)
print(b)
```

Output:

```text
[[1, 2, 100], [3, 4]]
[[1, 2, 100], [3, 4]]
```

The nested list was shared.

---

# 63. Deep Copy

For completely independent nested lists, `deepcopy()` can be used.

```python
from copy import deepcopy

a = [[1, 2], [3, 4]]

b = deepcopy(a)

b[0].append(100)

print(a)
print(b)

# Output:
# [[1, 2], [3, 4]]
# [[1, 2, 100], [3, 4]]
```

---

# List Truthiness

## 64. Empty List

An empty list is considered `False`.

```python
data = []

print(bool(data))

# Output:
# False
```

---

# 65. Non-Empty List

A non-empty list is considered `True`.

```python
data = [10]

print(bool(data))

# Output:
# True
```

This is useful in conditions:

```python
data = []

if data:
    print("List is not empty")
else:
    print("List is empty")

# Output:
# List is empty
```

---

# Useful Built-in Functions

## 66. `min()`

```python
numbers = [10, 20, 5, 40]

print(min(numbers))

# Output:
# 5
```

---

# 67. `max()`

```python
numbers = [10, 20, 5, 40]

print(max(numbers))

# Output:
# 40
```

---

# 68. `sum()`

```python
numbers = [10, 20, 30]

print(sum(numbers))

# Output:
# 60
```

---

# 69. `any()`

Returns `True` if at least one element is truthy.

```python
data = [False, False, True]

print(any(data))

# Output:
# True
```

---

# 70. `all()`

Returns `True` if every element is truthy.

```python
data = [True, True, True]

print(all(data))

# Output:
# True
```

---

# 71. `type()` and `isinstance()`

```python
numbers = [10, 20, 30]

print(type(numbers))

# Output:
# <class 'list'>
```

Using `isinstance()`:

```python
print(isinstance(numbers, list))

# Output:
# True
```

---

# Important List Methods

| Method | Purpose |
|---|---|
| `append()` | Add one element at end |
| `extend()` | Add multiple elements |
| `insert()` | Add at a specific index |
| `remove()` | Remove first matching value |
| `pop()` | Remove and return element |
| `clear()` | Remove all elements |
| `index()` | Find first index |
| `count()` | Count occurrences |
| `sort()` | Sort original list |
| `reverse()` | Reverse original list |
| `copy()` | Create shallow copy |

---

# List Method Return Values

An important point: methods that modify a list usually return `None`.

```python
numbers = [1, 2, 3]

result = numbers.append(4)

print(result)

# Output:
# None
```

Similarly:

```python
result = numbers.sort()
```

`result` is `None`.

Correct usage:

```python
numbers.sort()

print(numbers)
```

---

# List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Dynamic modification | Yes | No |
| Hashable | No | Can be |
| Use case | Changeable collection | Fixed collection |

---

# List vs Set

| Feature | List | Set |
|---|---|---|
| Ordered | Yes | No |
| Mutable | Yes | Yes |
| Duplicates | Yes | No |
| Indexing | Yes | No |
| Slicing | Yes | No |
| Membership | O(n) average | O(1) average |
| Main use | Ordered collection | Unique elements |

---

# List vs Dictionary

| Feature | List | Dictionary |
|---|---|---|
| Stores | Elements | Key-value pairs |
| Access | Index | Key |
| Duplicates | Yes | Keys cannot duplicate |
| Mutable | Yes | Yes |
| Ordered | Yes | Yes |
| Main use | Collection of values | Key-value data |

---

# Important Time Complexities

For a list containing `n` elements:

| Operation | Average Complexity |
|---|---:|
| `list[i]` | O(1) |
| `list[i] = value` | O(1) |
| `len(list)` | O(1) |
| `append()` | O(1) amortized |
| `pop()` from end | O(1) |
| `insert()` at beginning | O(n) |
| `insert()` in middle | O(n) |
| `pop(0)` | O(n) |
| `remove()` | O(n) |
| `index()` | O(n) |
| `count()` | O(n) |
| `x in list` | O(n) |
| `sort()` | O(n log n) |
| `reverse()` | O(n) |
| Slicing | O(k) |
| Copy | O(n) |

`k` represents the number of elements in the resulting slice.

---

# Why Is `append()` Usually O(1)?

Python lists use a dynamic array internally.

Conceptually:

```text
List
 ↓
[10][20][30][40]
```

When there is available capacity, adding an element is very fast:

```text
[10][20][30][40][50]
                  ↑
               added
```

Sometimes Python needs to allocate a larger memory area and copy the existing elements.

Therefore:

```text
append()
→ O(1) amortized
```

rather than O(1) for every single operation.

---

# Why Is Inserting at the Beginning O(n)?

Suppose:

```python
numbers = [10, 20, 30, 40]
```

Insert `5` at index `0`:

```text
Before:
[10][20][30][40]

After:
[5][10][20][30][40]
```

The existing elements have to move.

Therefore:

```text
insert(0, value)
→ O(n)
```

The same idea applies to `pop(0)`.

---

# Important Characteristics of List

Remember these seven points:

```text
List
 ↓
Ordered
 ↓
Mutable
 ↓
Indexed
 ↓
Allows duplicates
 ↓
Allows different data types
 ↓
Dynamic size
```

---

# Common List Mistakes

## Mistake 1: Using `{}` for an empty list

```python
data = {}
```

This creates a dictionary.

Correct:

```python
data = []
```

---

## Mistake 2: Confusing `append()` and `extend()`

```python
a = [1, 2]

a.append([3, 4])

# [1, 2, [3, 4]]
```

But:

```python
a = [1, 2]

a.extend([3, 4])

# [1, 2, 3, 4]
```

---

## Mistake 3: Assuming `sort()` returns the sorted list

Wrong:

```python
result = numbers.sort()
```

`result` becomes `None`.

Correct:

```python
numbers.sort()
print(numbers)
```

Or:

```python
result = sorted(numbers)
```

---

## Mistake 4: Assuming Assignment Creates a Copy

```python
a = [1, 2, 3]
b = a
```

This does **not** create an independent list.

Both refer to the same object.

Use:

```python
b = a.copy()
```

for a shallow copy.

---

# Final Quick Revision

```text
LIST
│
├── Ordered
├── Mutable
├── Indexed
├── Allows duplicates
├── Allows different data types
├── Allows nested lists
├── Dynamic size
│
├── Access
│   ├── Positive indexing
│   ├── Negative indexing
│   └── Slicing
│
├── Add
│   ├── append()
│   ├── insert()
│   └── extend()
│
├── Remove
│   ├── remove()
│   ├── pop()
│   ├── clear()
│   └── del
│
├── Search
│   ├── in
│   ├── index()
│   └── count()
│
├── Ordering
│   ├── sort()
│   ├── sorted()
│   └── reverse()
│
├── Creation
│   ├── []
│   ├── list()
│   ├── list(string)
│   ├── list(tuple)
│   ├── list(set)
│   └── list(range())
│
└── Advanced
    ├── Nested lists
    ├── List comprehension
    ├── Unpacking
    ├── References
    ├── Shallow copy
    └── Deep copy
```

### One-line definition

> **A list is an ordered, mutable collection that can store duplicate values and elements of different data types.**