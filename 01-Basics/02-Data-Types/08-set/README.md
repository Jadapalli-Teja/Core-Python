# Set in Python

A **set** is a built-in Python data type used to store a collection of **unique elements**.

A set is:

- **Mutable**
- **Unordered**
- **Unindexed**
- Does **not allow duplicate elements**
- Can contain different **hashable** data types
- Iterable
- Supports mathematical set operations
- Dynamically sized

Example:

```python
numbers = {10, 20, 30}

print(numbers)

# Possible output:
# {10, 20, 30}
```

The most important feature of a set is:

```text
Set → unique elements
```

---

# 1. Creating a Set

A set can be created using `{}` with elements inside.

```python
numbers = {10, 20, 30}

print(numbers)

# Possible output:
# {10, 20, 30}
```

Each value is an element of the set.

---

# 2. Empty Set

Be careful when creating an empty set.

```python
data = {}
```

This creates an **empty dictionary**, not a set.

To create an empty set:

```python
data = set()

print(data)

# Output:
# set()
```

Remember:

```text
{}       → empty dictionary
set()   → empty set
```

---

# 3. Duplicate Elements

A set automatically removes duplicate elements.

```python
numbers = {10, 20, 10, 30, 20, 10}

print(numbers)

# Possible output:
# {10, 20, 30}
```

Even though `10` was written three times, it appears only once.

This is the main difference between a list and a set.

```text
List:
[10, 20, 10, 30]

Set:
{10, 20, 30}
```

---

# 4. Set Is Unordered

A set does not maintain elements using positional indexes like a list.

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

The displayed order should not be relied upon.

For example, Python may display:

```text
{40, 10, 20, 30}
```

or another order.

The important point is:

> **Do not depend on set element order.**

---

# 5. Set Has No Indexing

You cannot access a set using an index.

This is invalid:

```python
numbers = {10, 20, 30}

# print(numbers[0])
```

It raises:

```text
TypeError
```

A list supports:

```python
numbers = [10, 20, 30]

print(numbers[0])

# Output:
# 10
```

A set does not.

---

# 6. Set Has No Slicing

Sets do not support slicing.

```python
numbers = {10, 20, 30}

# print(numbers[0:2])
```

This raises:

```text
TypeError
```

Slicing is supported by sequence types such as:

```text
str
list
tuple
range
```

but not by sets.

---

# 7. Creating a Set Using `set()`

The `set()` constructor can create a set from an iterable.

```python
numbers = set([10, 20, 30])

print(numbers)

# Possible output:
# {10, 20, 30}
```

---

# 8. Set from a List

```python
numbers = [10, 20, 30, 20, 10]

result = set(numbers)

print(result)

# Possible output:
# {10, 20, 30}
```

This is commonly used to remove duplicates from a list.

---

# 9. Set from a Tuple

```python
data = (10, 20, 30, 20)

result = set(data)

print(result)

# Possible output:
# {10, 20, 30}
```

---

# 10. Set from a String

A string is iterable, so each character becomes an element.

```python
word = "hello"

result = set(word)

print(result)
```

Possible output:

```text
{'h', 'e', 'l', 'o'}
```

The duplicate `l` is removed.

The order is not guaranteed.

---

# 11. Set from a Range

```python
numbers = set(range(1, 6))

print(numbers)

# Possible output:
# {1, 2, 3, 4, 5}
```

---

# 12. Set from a Dictionary

When a dictionary is passed to `set()`, its **keys** are used.

```python
student = {
    "name": "Teja",
    "age": 21
}

result = set(student)

print(result)

# Possible output:
# {'name', 'age'}
```

---

# 13. Set Elements Must Be Hashable

A set internally uses hashing to store and find its elements efficiently.

Therefore, set elements must be **hashable**.

Common hashable objects include:

```text
int
float
str
bool
tuple (if its elements are hashable)
frozenset
```

---

# 14. List Cannot Be a Set Element

A list is mutable and unhashable.

Therefore:

```python
# data = {[1, 2, 3]}
```

raises:

```text
TypeError: unhashable type: 'list'
```

---

# 15. Dictionary Cannot Be a Set Element

A dictionary is also mutable and unhashable.

```python
# data = {{1: "one"}}
```

This is invalid.

---

# 16. Tuple Can Be a Set Element

A tuple can be stored inside a set if its elements are hashable.

```python
data = {(1, 2), (3, 4)}

print(data)
```

Possible output:

```text
{(1, 2), (3, 4)}
```

---

# 17. Tuple Containing a List

Not every tuple is hashable.

This is invalid:

```python
# data = {(1, [2, 3])}
```

Why?

Because the tuple contains a list, and the list is unhashable.

Therefore the tuple itself cannot be hashed.

---

# 18. Frozenset as a Set Element

A `frozenset` is immutable and hashable.

Therefore it can be an element of a set.

```python
data = {frozenset([1, 2])}

print(data)

# Possible output:
# {frozenset({1, 2})}
```

---

# Adding Elements

## 19. `add()`

`add()` adds one element to a set.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# Possible output:
# {10, 20, 30, 40}
```

The exact displayed order is not guaranteed.

---

# 20. Adding a Duplicate

Adding an existing element does nothing.

```python
numbers = {10, 20, 30}

numbers.add(20)

print(numbers)

# Possible output:
# {10, 20, 30}
```

The set remains unchanged.

---

# 21. `add()` One Element at a Time

```python
numbers = set()

numbers.add(10)
numbers.add(20)
numbers.add(30)

print(numbers)

# Possible output:
# {10, 20, 30}
```

---

# 22. `update()`

`update()` adds multiple elements from an iterable.

```python
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)

# Possible output:
# {10, 20, 30, 40, 50}
```

---

# 23. `update()` with a Tuple

```python
numbers = {10, 20}

numbers.update((30, 40))

print(numbers)
```

---

# 24. `update()` with a String

Be careful with strings.

```python
letters = {"a", "b"}

letters.update("hello")

print(letters)
```

The characters are added individually.

The duplicate `l` and `h`/`e` etc. are handled according to set uniqueness.

---

# 25. `add()` vs `update()`

This is very important.

### `add()`

```python
numbers = {1, 2}

numbers.add([3, 4])
```

A list itself cannot be a set element, so this raises `TypeError`.

But:

```python
numbers = {1, 2}

numbers.add((3, 4))
```

adds the **entire tuple as one element**.

### `update()`

```python
numbers = {1, 2}

numbers.update([3, 4])

print(numbers)

# Possible output:
# {1, 2, 3, 4}
```

So:

```text
add()
→ adds one object

update()
→ adds elements from an iterable
```

---

# Removing Elements

## 26. `remove()`

`remove(value)` removes the specified element.

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

# Possible output:
# {10, 30}
```

---

# 27. `remove()` with Missing Element

If the element does not exist, `remove()` raises `KeyError`.

```python
numbers = {10, 20, 30}

# numbers.remove(50)
```

Result:

```text
KeyError
```

---

# 28. `discard()`

`discard()` also removes an element.

```python
numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)

# Possible output:
# {10, 30}
```

---

# 29. `remove()` vs `discard()`

This difference is important.

If the element exists:

```text
remove()   → removes it
discard()  → removes it
```

If the element does not exist:

```text
remove()   → KeyError
discard()  → no error
```

Example:

```python
numbers = {10, 20, 30}

numbers.discard(100)

print(numbers)

# Possible output:
# {10, 20, 30}
```

---

# 30. `pop()`

`pop()` removes and returns an arbitrary element.

```python
numbers = {10, 20, 30}

value = numbers.pop()

print(value)
print(numbers)
```

Do **not** assume which element will be removed.

Because a set is unordered, you should not write code that depends on a particular element being popped.

---

# 31. `clear()`

Removes all elements.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)

# Output:
# set()
```

The set still exists; it is just empty.

---

# 32. `del`

You can delete the entire set variable using `del`.

```python
numbers = {10, 20, 30}

del numbers
```

After this, `numbers` no longer exists.

---

# Membership

## 33. `in`

Set membership is one of the most important uses of a set.

```python
numbers = {10, 20, 30}

print(20 in numbers)

# Output:
# True
```

---

# 34. `not in`

```python
numbers = {10, 20, 30}

print(50 not in numbers)

# Output:
# True
```

Sets are especially useful when you frequently need to check whether an element exists.

---

# 35. Why Set Membership Is Fast

Conceptually, a set uses a **hash table** internally.

For example:

```text
20
 ↓
hash(20)
 ↓
find corresponding location
 ↓
check element
```

Therefore, average membership lookup is approximately:

```text
O(1)
```

This is much faster than searching through a large list in many cases.

---

# Set Operations

Sets support mathematical operations.

Suppose:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

---

# 36. Union

Union combines all unique elements from both sets.

Mathematically:

```text
A ∪ B
```

Python:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)

# Possible output:
# {1, 2, 3, 4, 5, 6}
```

---

# 37. `union()`

The same operation can be performed using `union()`.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))

# Possible output:
# {1, 2, 3, 4, 5, 6}
```

The original sets are not changed.

---

# 38. Multiple Union

```python
A = {1, 2}
B = {2, 3}
C = {3, 4}

result = A.union(B, C)

print(result)

# Possible output:
# {1, 2, 3, 4}
```

---

# 39. Intersection

Intersection returns elements common to both sets.

Mathematically:

```text
A ∩ B
```

Python:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A & B)

# Possible output:
# {3, 4}
```

---

# 40. `intersection()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))

# Possible output:
# {3, 4}
```

---

# 41. Difference

Difference returns elements that are in the first set but not in the second.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)

# Possible output:
# {1, 2}
```

Think:

```text
A - B
→ elements of A that are not in B
```

---

# 42. `difference()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.difference(B))

# Possible output:
# {1, 2}
```

---

# 43. Difference Is Directional

This is important.

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A - B)
print(B - A)

# Possible output:
# {1}
# {4}
```

They are not necessarily equal.

---

# 44. Symmetric Difference

Symmetric difference returns elements that are in either set but **not in both**.

Mathematically:

```text
A △ B
```

Python:

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A ^ B)

# Possible output:
# {1, 4}
```

---

# 45. `symmetric_difference()`

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A.symmetric_difference(B))

# Possible output:
# {1, 4}
```

---

# 46. Visual Understanding of Set Operations

Given:

```text
A = {1, 2, 3}
B = {3, 4, 5}
```

### Union

```text
A | B
→ {1, 2, 3, 4, 5}
```

### Intersection

```text
A & B
→ {3}
```

### Difference

```text
A - B
→ {1, 2}
```

### Symmetric Difference

```text
A ^ B
→ {1, 2, 4, 5}
```

---

# Subset and Superset

## 47. Subset

A set `A` is a subset of `B` if **every element of A is also present in B**.

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

# Output:
# True
```

---

# 48. `<=` for Subset

```python
A = {1, 2}
B = {1, 2, 3}

print(A <= B)

# Output:
# True
```

---

# 49. Proper Subset `<`

A proper subset must contain fewer elements than the other set.

```python
A = {1, 2}
B = {1, 2, 3}

print(A < B)

# Output:
# True
```

---

# 50. Superset

A set is a superset if it contains all elements of another set.

```python
A = {1, 2, 3}
B = {1, 2}

print(A.issuperset(B))

# Output:
# True
```

---

# 51. `>=` for Superset

```python
A = {1, 2, 3}
B = {1, 2}

print(A >= B)

# Output:
# True
```

---

# 52. Proper Superset `>`

```python
A = {1, 2, 3}
B = {1, 2}

print(A > B)

# Output:
# True
```

---

# 53. Disjoint Sets

Two sets are disjoint when they have **no common elements**.

```python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))

# Output:
# True
```

---

# 54. Not Disjoint

```python
A = {1, 2}
B = {2, 3}

print(A.isdisjoint(B))

# Output:
# False
```

Because `2` exists in both sets.

---

# Set Equality

## 55. `==`

Two sets are equal when they contain the same elements.

```python
A = {1, 2, 3}
B = {3, 2, 1}

print(A == B)

# Output:
# True
```

Order does not matter.

---

# 56. `!=`

```python
A = {1, 2}
B = {1, 2, 3}

print(A != B)

# Output:
# True
```

---

# `==` vs `is`

## 57. Equality

```python
A = {1, 2, 3}
B = {1, 2, 3}

print(A == B)

# Output:
# True
```

The contents are equal.

---

## 58. Identity

```python
A = {1, 2, 3}
B = {1, 2, 3}

print(A is B)

# Output:
# False
```

They are separate set objects.

`==` checks contents.

`is` checks object identity.

---

# Iterating Through a Set

## 59. `for` Loop

```python
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

The order is not guaranteed.

---

# 60. `enumerate()` with a Set

You technically can use `enumerate()`:

```python
numbers = {10, 20, 30}

for index, number in enumerate(numbers):
    print(index, number)
```

But remember:

> The index here is only the position produced during this particular iteration. It is **not a set index**, because sets do not support indexing.

---

# Set Comprehension

## 61. Basic Set Comprehension

Set comprehensions provide a compact way to create sets.

```python
numbers = {x for x in range(1, 6)}

print(numbers)

# Possible output:
# {1, 2, 3, 4, 5}
```

Syntax:

```text
{expression for item in iterable}
```

---

# 62. Set Comprehension with Condition

```python
even_numbers = {
    x for x in range(1, 11)
    if x % 2 == 0
}

print(even_numbers)

# Possible output:
# {2, 4, 6, 8, 10}
```

---

# 63. Creating Unique Squares

```python
numbers = [1, 2, 2, 3, 3, 4]

squares = {x * x for x in numbers}

print(squares)

# Possible output:
# {1, 4, 9, 16}
```

The set automatically removes duplicate results.

---

# Removing Duplicates from a List

## 64. Simple Method

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)

# Possible output:
# {10, 20, 30, 40}
```

This is a common use of sets.

But remember:

```text
List → ordered and duplicates allowed
Set  → unique elements and no guaranteed order
```

So converting a list to a set can lose the original order.

---

# Set and Boolean Values

## 65. `True` and `1`

In Python:

```python
True == 1
```

is:

```text
True
```

Therefore:

```python
data = {True, 1}

print(data)

# Possible output:
# {True}
```

`True` and `1` behave as equal values for set uniqueness.

---

# 66. `False` and `0`

Similarly:

```python
False == 0
```

is:

```text
True
```

Therefore:

```python
data = {False, 0}

print(data)

# Possible output:
# {False}
```

---

# Set References

## 67. Two Variables Can Refer to the Same Set

```python
A = {1, 2, 3}

B = A

B.add(4)

print(A)
print(B)
```

Possible output:

```text
{1, 2, 3, 4}
{1, 2, 3, 4}
```

Why?

```text
A ─────┐
       ↓
    {1, 2, 3}
       ↑
       │
B ─────┘
```

Both variables refer to the same set object.

---

# 68. Copying a Set

Use `.copy()`.

```python
A = {1, 2, 3}

B = A.copy()

B.add(4)

print(A)
print(B)

# Possible output:
# {1, 2, 3}
# {1, 2, 3, 4}
```

Now they are separate set objects.

---

# Set Truthiness

## 69. Empty Set

An empty set is `False` in a Boolean context.

```python
data = set()

print(bool(data))

# Output:
# False
```

---

# 70. Non-Empty Set

```python
data = {10}

print(bool(data))

# Output:
# True
```

Therefore:

```python
data = set()

if data:
    print("Set is not empty")
else:
    print("Set is empty")

# Output:
# Set is empty
```

---

# Useful Built-in Functions

## 71. `len()`

```python
numbers = {10, 20, 30}

print(len(numbers))

# Output:
# 3
```

---

# 72. `min()`

```python
numbers = {30, 10, 20}

print(min(numbers))

# Output:
# 10
```

---

# 73. `max()`

```python
numbers = {30, 10, 20}

print(max(numbers))

# Output:
# 30
```

---

# 74. `sum()`

```python
numbers = {10, 20, 30}

print(sum(numbers))

# Output:
# 60
```

---

# 75. `any()`

```python
data = {False, True}

print(any(data))

# Output:
# True
```

Returns `True` if at least one element is truthy.

---

# 76. `all()`

```python
data = {True, True}

print(all(data))

# Output:
# True
```

Returns `True` if all elements are truthy.

---

# Set Methods

| Method | Purpose |
|---|---|
| `add()` | Add one element |
| `update()` | Add multiple elements |
| `remove()` | Remove element, error if missing |
| `discard()` | Remove element, no error if missing |
| `pop()` | Remove and return arbitrary element |
| `clear()` | Remove all elements |
| `copy()` | Create a shallow copy |
| `union()` | Combine sets |
| `intersection()` | Find common elements |
| `difference()` | Find elements only in first set |
| `symmetric_difference()` | Find elements in either but not both |
| `issubset()` | Check subset |
| `issuperset()` | Check superset |
| `isdisjoint()` | Check for no common elements |

---

# Set Operators

| Operator | Meaning |
|---|---|
| `\|` | Union |
| `&` | Intersection |
| `-` | Difference |
| `^` | Symmetric difference |
| `<=` | Subset |
| `<` | Proper subset |
| `>=` | Superset |
| `>` | Proper superset |

Example:

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
```

---

# Set vs List

| Feature | List | Set |
|---|---|---|
| Ordered | Yes | No |
| Mutable | Yes | Yes |
| Duplicates | Yes | No |
| Indexing | Yes | No |
| Slicing | Yes | No |
| Membership | O(n) average | O(1) average |
| Main purpose | Ordered collection | Unique collection |
| Syntax | `[]` | `{}` / `set()` |

---

# Set vs Frozenset

| Feature | Set | Frozenset |
|---|---|---|
| Mutable | Yes | No |
| Unique elements | Yes | Yes |
| Ordered | No | No |
| Hashable | No | Yes |
| Dictionary key | No | Yes |
| Can be set element | No | Yes |
| `add()` | Yes | No |
| `remove()` | Yes | No |
| Set operations | Yes | Yes |

Remember:

```text
set
→ mutable

frozenset
→ immutable
```

---

# Time Complexity

For a set containing `n` elements:

| Operation | Average Complexity |
|---|---:|
| `x in set` | O(1) |
| `add()` | O(1) |
| `remove()` | O(1) |
| `discard()` | O(1) |
| `pop()` | O(1) |
| `len()` | O(1) |
| `copy()` | O(n) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) |
| Difference | O(n) |
| Iteration | O(n) |

These are average-case complexities; actual performance can vary.

---

# Why Is Set Membership Fast?

A set uses a **hash table** internally.

For example:

```text
value
  ↓
hash(value)
  ↓
hash table
  ↓
find value
```

Because Python can use the hash value to locate an element, membership is usually very fast.

Therefore:

```python
x in my_set
```

has average:

```text
O(1)
```

Compare this with a list:

```python
x in my_list
```

which is generally:

```text
O(n)
```

because Python may need to check elements one by one.

---

# Important Characteristics

Remember these:

```text
Set
│
├── Mutable
├── Unordered
├── Unindexed
├── No duplicates
├── Iterable
├── Hash-based
├── Dynamic size
└── Elements must be hashable
```

---

# Common Mistakes

## Mistake 1: Empty `{}` is not a set

```python
data = {}

print(type(data))

# Output:
# <class 'dict'>
```

Correct:

```python
data = set()
```

---

## Mistake 2: Trying to use indexing

```python
numbers = {10, 20, 30}

# numbers[0]
```

Sets have no indexes.

---

## Mistake 3: Adding a list

```python
numbers = {1, 2}

# numbers.add([3, 4])
```

This raises `TypeError` because lists are unhashable.

---

## Mistake 4: Assuming `pop()` removes the last element

For a list:

```python
numbers.pop()
```

removes the last element.

For a set:

```python
numbers.pop()
```

removes an **arbitrary element**.

Do not assume it is the "last" element.

---

## Mistake 5: Assuming Set Order

Do not write logic that depends on:

```python
numbers = {1, 2, 3}
```

being iterated in a particular order.

A set is not an ordered sequence.

---

# Practical Example 1: Find Common Students

```python
python_students = {
    "Teja",
    "Ravi",
    "Kiran"
}

sql_students = {
    "Ravi",
    "Kiran",
    "Arun"
}

common_students = python_students & sql_students

print(common_students)

# Possible output:
# {'Ravi', 'Kiran'}
```

Intersection gives the common students.

---

# Practical Example 2: Find Students Only in Python

```python
python_students = {
    "Teja",
    "Ravi",
    "Kiran"
}

sql_students = {
    "Ravi",
    "Kiran",
    "Arun"
}

result = python_students - sql_students

print(result)

# Possible output:
# {'Teja'}
```

---

# Practical Example 3: Remove Duplicates

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)

# Possible output:
# {10, 20, 30, 40}
```

---

# Practical Example 4: Check Membership

```python
allowed_users = {
    "Teja",
    "Ravi",
    "Kiran"
}

name = "Teja"

if name in allowed_users:
    print("Access allowed")
else:
    print("Access denied")

# Output:
# Access allowed
```

This is one reason sets are useful for fast membership checking.

---

# Final Mental Model

Think of a set like this:

```text
              SET
               │
       ┌───────┴───────┐
       │               │
   Unique          Hash-based
   values           storage
       │               │
       │          Fast membership
       │               │
       └───────┬───────┘
               │
          No duplicates
               │
        No indexing/order
               │
        Supports set math
               │
    ┌──────────┼──────────┐
    ↓          ↓          ↓
  Union   Intersection  Difference
```

---

# Quick Revision

```text
Set
 ↓
Mutable
 ↓
Unordered
 ↓
No indexing
 ↓
No duplicates
 ↓
Elements must be hashable
 ↓
Fast membership lookup
 ↓
Supports mathematical operations
```

Most important methods:

```text
add()
update()

remove()
discard()
pop()
clear()

union()
intersection()
difference()
symmetric_difference()

issubset()
issuperset()
isdisjoint()
```

Most important operators:

```text
A | B    → Union
A & B    → Intersection
A - B    → Difference
A ^ B    → Symmetric Difference

A <= B   → Subset
A < B    → Proper Subset
A >= B   → Superset
A > B    → Proper Superset
```

### One-line definition

> **A set is a mutable, unordered collection of unique hashable elements that provides efficient membership testing and mathematical set operations.**