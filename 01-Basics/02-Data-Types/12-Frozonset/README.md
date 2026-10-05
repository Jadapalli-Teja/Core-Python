# Frozenset in Python

A **frozenset** is an immutable version of a Python `set`.

Like a set, it stores **unique elements**, but unlike a set, its contents cannot be changed after creation.

```python
numbers = frozenset([10, 20, 30])

print(numbers)
```

A frozenset is:

- Unordered
- Immutable
- Iterable
- Hashable
- Contains only unique elements
- Does not support indexing
- Does not support slicing

---

# 1. Creating a Frozenset

Use the `frozenset()` constructor.

```python
numbers = frozenset([10, 20, 30])

print(numbers)
```

Possible output:

```text
frozenset({10, 20, 30})
```

The order of elements should not be relied upon.

---

# 2. Type of Frozenset

```python
numbers = frozenset([10, 20, 30])

print(type(numbers))

# Output:
# <class 'frozenset'>
```

---

# 3. Empty Frozenset

Use:

```python
empty = frozenset()

print(empty)

# Output:
# frozenset()
```

Remember:

```python
{}
```

creates an empty **dictionary**, not a frozenset.

---

# 4. Frozenset from a List

```python
numbers = frozenset([10, 20, 30, 20, 10])

print(numbers)
```

Duplicate elements are automatically removed.

Possible output:

```text
frozenset({10, 20, 30})
```

---

# 5. Frozenset from a Tuple

```python
data = (10, 20, 30)

result = frozenset(data)

print(result)
```

---

# 6. Frozenset from a Set

```python
data = {10, 20, 30}

result = frozenset(data)

print(result)
```

---

# 7. Frozenset from a String

A string is iterable, so each character becomes an element.

```python
letters = frozenset("hello")

print(letters)
```

The duplicate `l` is stored only once.

Possible result:

```text
frozenset({'h', 'e', 'l', 'o'})
```

---

# 8. Frozenset from a Dictionary

When a dictionary is passed to `frozenset()`, its **keys** are used.

```python
student = {
    "name": "Teja",
    "age": 21
}

result = frozenset(student)

print(result)
```

Possible output:

```text
frozenset({'name', 'age'})
```

---

# 9. Frozenset Contains Unique Elements

```python
numbers = frozenset([1, 2, 2, 3, 3, 3])

print(numbers)

# Possible output:
# frozenset({1, 2, 3})
```

---

# 10. Frozenset Is Unordered

You cannot rely on a particular positional order.

```python
numbers = frozenset([10, 20, 30])

print(numbers)
```

The displayed order is not something your program should depend on.

---

# 11. No Indexing

A frozenset does not support indexing.

This is invalid:

```python
numbers = frozenset([10, 20, 30])

print(numbers[0])
```

It raises:

```text
TypeError
```

Unlike a list:

```python
numbers = [10, 20, 30]

print(numbers[0])
```

---

# 12. No Slicing

Frozensets do not support slicing.

```python
numbers = frozenset([10, 20, 30])

print(numbers[0:2])
```

This raises:

```text
TypeError
```

---

# 13. Frozenset Is Immutable

Once created, the elements cannot be changed.

```python
numbers = frozenset([10, 20, 30])

# numbers.add(40)
```

`add()` does not exist for frozenset.

This is because frozenset is immutable.

---

# 14. No `add()`

For a normal set:

```python
numbers = {10, 20}

numbers.add(30)
```

For a frozenset:

```python
numbers = frozenset([10, 20])

# numbers.add(30)
```

This produces:

```text
AttributeError
```

---

# 15. No `remove()`

```python
numbers = frozenset([10, 20, 30])

# numbers.remove(20)
```

This is not supported.

---

# 16. No `discard()`

```python
numbers = frozenset([10, 20, 30])

# numbers.discard(20)
```

Not available because the frozenset cannot be modified.

---

# 17. No `pop()`

```python
numbers = frozenset([10, 20, 30])

# numbers.pop()
```

A frozenset cannot remove elements.

---

# 18. No `clear()`

```python
numbers = frozenset([10, 20, 30])

# numbers.clear()
```

A frozenset cannot be cleared because it is immutable.

---

# Membership

## 19. Using `in`

```python
numbers = frozenset([10, 20, 30])

print(20 in numbers)

# Output:
# True
```

---

## 20. Using `not in`

```python
numbers = frozenset([10, 20, 30])

print(50 not in numbers)

# Output:
# True
```

---

# Length and Iteration

## 21. `len()`

```python
numbers = frozenset([10, 20, 30])

print(len(numbers))

# Output:
# 3
```

---

## 22. Iterating Through a Frozenset

```python
numbers = frozenset([10, 20, 30])

for number in numbers:
    print(number)
```

The order is not guaranteed.

---

# Set Operations

A frozenset supports most of the mathematical set operations.

## 23. Union

Union combines elements from both collections.

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

result = a | b

print(result)
```

Possible output:

```text
frozenset({1, 2, 3, 4, 5})
```

---

## 24. `union()`

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

result = a.union(b)

print(result)
```

---

## 25. Intersection

Intersection returns common elements.

```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

result = a & b

print(result)

# Possible output:
# frozenset({2, 3})
```

---

## 26. `intersection()`

```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

print(a.intersection(b))
```

---

## 27. Difference

Difference returns elements present in the first collection but not the second.

```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

print(a - b)

# Possible output:
# frozenset({1})
```

---

## 28. `difference()`

```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

print(a.difference(b))
```

---

## 29. Symmetric Difference

Returns elements that are in either collection but not in both.

```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

print(a ^ b)

# Possible output:
# frozenset({1, 4})
```

---

## 30. `symmetric_difference()`

```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

print(a.symmetric_difference(b))
```

---

# Subset and Superset

## 31. `issubset()`

Checks whether all elements of one collection exist in another.

```python
a = frozenset([1, 2])
b = frozenset([1, 2, 3])

print(a.issubset(b))

# Output:
# True
```

---

## 32. `<=` for Subset

```python
a = frozenset([1, 2])
b = frozenset([1, 2, 3])

print(a <= b)

# Output:
# True
```

---

## 33. Proper Subset `<`

```python
a = frozenset([1, 2])
b = frozenset([1, 2, 3])

print(a < b)

# Output:
# True
```

A proper subset must contain fewer elements.

---

## 34. `issuperset()`

```python
a = frozenset([1, 2, 3])
b = frozenset([1, 2])

print(a.issuperset(b))

# Output:
# True
```

---

## 35. `>=` for Superset

```python
a = frozenset([1, 2, 3])
b = frozenset([1, 2])

print(a >= b)

# Output:
# True
```

---

## 36. Proper Superset `>`

```python
a = frozenset([1, 2, 3])
b = frozenset([1, 2])

print(a > b)

# Output:
# True
```

---

# Disjoint Sets

## 37. `isdisjoint()`

Returns `True` when two collections have no common elements.

```python
a = frozenset([1, 2])
b = frozenset([3, 4])

print(a.isdisjoint(b))

# Output:
# True
```

---

## 38. Not Disjoint

```python
a = frozenset([1, 2])
b = frozenset([2, 3])

print(a.isdisjoint(b))

# Output:
# False
```

---

# Frozenset and Hashability

## 39. Frozenset Is Hashable

Unlike a normal set, a frozenset is hashable.

```python
numbers = frozenset([1, 2, 3])

print(hash(numbers))
```

This allows a frozenset to be used where a hashable object is required.

---

## 40. Frozenset as Dictionary Key

```python
permissions = frozenset(["read", "write"])

data = {
    permissions: "User permissions"
}

print(data[permissions])

# Output:
# User permissions
```

A normal set cannot be used as a dictionary key.

---

## 41. Set Cannot Be a Dictionary Key

This is invalid:

```python
permissions = {"read", "write"}

# data = {
#     permissions: "User permissions"
# }
```

It raises:

```text
TypeError: unhashable type: 'set'
```

---

# Frozenset Inside a Set

## 42. Frozenset as a Set Element

A normal set can contain a frozenset.

```python
a = frozenset([1, 2])

data = {a}

print(data)
```

Possible output:

```text
{frozenset({1, 2})}
```

This works because the frozenset is hashable.

---

## 43. Normal Set Inside a Set

A normal set cannot be an element of another set.

```python
a = {1, 2}

# data = {a}
```

This raises:

```text
TypeError: unhashable type: 'set'
```

---

# Frozenset and Equality

## 44. `==`

Two frozensets are equal if they contain the same elements.

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 2, 1])

print(a == b)

# Output:
# True
```

Order does not matter.

---

## 45. Frozenset vs Set Equality

A frozenset and a set can compare equal if they contain the same elements.

```python
a = frozenset([1, 2, 3])
b = {1, 2, 3}

print(a == b)

# Output:
# True
```

Although their types are different.

```python
print(type(a))
print(type(b))

# Output:
# <class 'frozenset'>
# <class 'set'>
```

---

# `is` vs `==`

## 46. Identity

```python
a = frozenset([1, 2])
b = frozenset([1, 2])

print(a == b)
print(a is b)

# Output:
# True
# False
```

`==` checks contents.

`is` checks whether both variables refer to the same object.

---

# Copying

## 47. `copy()`

A frozenset has a `copy()` method.

```python
a = frozenset([1, 2, 3])

b = a.copy()

print(b)

# Output:
# frozenset({1, 2, 3})
```

Since a frozenset is immutable, there is no need to modify the copied object.

---

## 48. `frozenset()` on a Frozenset

```python
a = frozenset([1, 2, 3])

b = frozenset(a)

print(a is b)

# Output:
# True
```

Python can reuse the same immutable frozenset object.

---

# Converting Frozenset

## 49. Frozenset to List

```python
data = frozenset([10, 20, 30])

result = list(data)

print(result)
```

---

## 50. Frozenset to Tuple

```python
data = frozenset([10, 20, 30])

result = tuple(data)

print(result)
```

---

## 51. Frozenset to Set

```python
data = frozenset([10, 20, 30])

result = set(data)

print(result)
```

The resulting set is mutable.

---

# Mutable and Immutable Comparison

## 52. Set Is Mutable

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

The set changes.

---

## 53. Frozenset Is Immutable

```python
numbers = frozenset([1, 2, 3])

# numbers.add(4)
```

You cannot change it.

---

# Frozenset with Different Types

## 54. Mixed Data Types

A frozenset can contain different hashable types.

```python
data = frozenset([
    10,
    3.14,
    "Python",
    True,
    (1, 2)
])

print(data)
```

The elements must be hashable.

---

## 55. List Cannot Be an Element

This is invalid:

```python
data = frozenset([
    [1, 2]
])
```

It raises:

```text
TypeError: unhashable type: 'list'
```

---

## 56. Tuple Can Be an Element

```python
data = frozenset([
    (1, 2),
    (3, 4)
])

print(data)
```

Tuples can be elements if their contents are hashable.

---

# Practical Examples

## 57. Removing Duplicates

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = frozenset(numbers)

print(unique_numbers)
```

The duplicates are removed.

---

## 58. Fixed Permissions

```python
permissions = frozenset([
    "read",
    "write",
    "execute"
])

print(permissions)
```

Because it is immutable, the permissions cannot accidentally be changed.

---

## 59. Common Elements

```python
python_students = frozenset(["Teja", "Ravi", "Kiran"])
sql_students = frozenset(["Ravi", "Kiran", "Arun"])

common = python_students & sql_students

print(common)
```

Possible output:

```text
frozenset({'Ravi', 'Kiran'})
```

---

## 60. Unique Elements from Two Groups

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

unique = a ^ b

print(unique)

# Possible output:
# frozenset({1, 2, 4, 5})
```

---

# Important Frozenset Methods

| Method | Purpose |
|---|---|
| `union()` | Combine elements |
| `intersection()` | Find common elements |
| `difference()` | Find elements only in first |
| `symmetric_difference()` | Find elements in either but not both |
| `issubset()` | Check subset |
| `issuperset()` | Check superset |
| `isdisjoint()` | Check whether no common elements |
| `copy()` | Return a frozenset copy |

Unlike `set`, frozenset does **not** have:

```text
add()
remove()
discard()
pop()
clear()
update()
```

because it is immutable.

---

# Set vs Frozenset

| Feature | `set` | `frozenset` |
|---|---|---|
| Mutable | Yes | No |
| Immutable | No | Yes |
| Unique elements | Yes | Yes |
| Ordered | No | No |
| Indexing | No | No |
| Slicing | No | No |
| Hashable | No | Yes |
| Dictionary key | No | Yes |
| Can be set element | No | Yes |
| `add()` | Yes | No |
| `remove()` | Yes | No |
| `clear()` | Yes | No |
| Union | Yes | Yes |
| Intersection | Yes | Yes |
| Difference | Yes | Yes |
| Subset checking | Yes | Yes |

---

# Time Complexity

For normal frozenset operations, average complexity is similar to `set`.

| Operation | Average Time |
|---|---:|
| Membership `x in fs` | O(1) |
| `len()` | O(1) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) |
| Difference | O(n) |
| Add | Not supported |
| Remove | Not supported |

The exact performance can depend on the operation and the sizes of the collections.

---

# Important Points to Remember

1. `frozenset` is an immutable version of `set`.
2. It stores only unique elements.
3. It is unordered.
4. It does not support indexing.
5. It does not support slicing.
6. It cannot be modified after creation.
7. `add()`, `remove()`, `discard()`, `pop()` and `clear()` are not available.
8. It supports union, intersection, difference and symmetric difference.
9. It supports subset and superset operations.
10. It supports membership testing using `in`.
11. A frozenset is hashable.
12. A frozenset can be used as a dictionary key.
13. A frozenset can be an element of another set.
14. A normal set cannot be a dictionary key.
15. A normal set cannot be an element of another set.
16. Frozenset elements must be hashable.
17. A tuple can be a frozenset element if its elements are hashable.
18. A list cannot be a frozenset element.
19. Frozenset can be created using `frozenset()`.
20. `frozenset()` with no argument creates an empty frozenset.

---

# Quick Revision

```text
set
 ↓
Mutable
 ↓
Can change elements
 ↓
Not hashable

frozenset
 ↓
Immutable
 ↓
Cannot change elements
 ↓
Hashable
 ↓
Can be dictionary key
 ↓
Can be element of another set
```

Example:

```python
numbers = frozenset([10, 20, 30])

print(20 in numbers)
print(len(numbers))

# Output:
# True
# 3
```

The main difference to remember:

```text
set       → mutable
frozenset → immutable
```