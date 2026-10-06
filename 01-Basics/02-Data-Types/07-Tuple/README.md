# Python Tuple

A **tuple** is a built-in Python data type used to store multiple values in a single object.

A tuple is:

- **Ordered**
- **Immutable**
- **Indexed**
- **Allows duplicate values**
- **Can store different data types**
- **Can contain nested objects**
- **Iterable**
- **Usually hashable if all its elements are hashable**

Example:

```python
student = ("Teja", 21, "CSE")

print(student)

# Output:
# ('Teja', 21, 'CSE')
```

---

# 1. Creating a Tuple

A tuple is normally created using parentheses `()`.

```python
numbers = (10, 20, 30)

print(numbers)
print(type(numbers))

# Output:
# (10, 20, 30)
# <class 'tuple'>
```

Syntax:

```python
tuple_name = (value1, value2, value3)
```

---

# 2. Empty Tuple

An empty tuple can be created using `()`.

```python
data = ()

print(data)
print(type(data))

# Output:
# ()
# <class 'tuple'>
```

We can also use:

```python
data = tuple()
```

Both create an empty tuple.

---

# 3. Tuple with Different Data Types

A tuple can contain different types of values.

```python
data = (
    10,
    3.14,
    "Python",
    True,
    None
)

print(data)
```

A tuple is not restricted to one particular data type.

---

# 4. Duplicate Values

Tuples allow duplicate values.

```python
numbers = (10, 20, 10, 30, 20)

print(numbers)

# Output:
# (10, 20, 10, 30, 20)
```

Unlike a set, duplicates are preserved.

---

# 5. Ordered Nature of Tuple

Tuples maintain the order in which elements are stored.

```python
data = ("Python", "Java", "C")

print(data)

# Output:
# ('Python', 'Java', 'C')
```

The position of each element is important.

---

# 6. Tuple Indexing

Tuple elements can be accessed using indexes.

Indexing starts from `0`.

```python
languages = ("Python", "Java", "C")

print(languages[0])
print(languages[1])
print(languages[2])

# Output:
# Python
# Java
# C
```

Conceptually:

```text
Index:     0        1       2
           ↓        ↓       ↓
Tuple:  Python    Java      C
```

---

# 7. Negative Indexing

Tuples support negative indexing.

`-1` refers to the last element.

```python
languages = ("Python", "Java", "C")

print(languages[-1])
print(languages[-2])
print(languages[-3])

# Output:
# C
# Java
# Python
```

Conceptually:

```text
Index:      0        1       2
Negative:  -3       -2      -1
            ↓        ↓       ↓
Tuple:    Python    Java      C
```

---

# 8. Index Out of Range

If we access an index that does not exist, Python raises `IndexError`.

```python
numbers = (10, 20, 30)

print(numbers[5])
```

Output:

```text
IndexError: tuple index out of range
```

---

# 9. Tuple Slicing

We can extract part of a tuple using slicing.

Syntax:

```python
tuple[start:stop]
```

The `stop` index is excluded.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# Output:
# (20, 30, 40)
```

Indexes:

```text
0    1    2    3    4
10   20   30   40   50
     ↑         ↑
   start     stop
```

---

# 10. Tuple Slicing with Step

Syntax:

```python
tuple[start:stop:step]
```

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[::2])

# Output:
# (10, 30, 50)
```

Another example:

```python
print(numbers[1::2])

# Output:
# (20, 40)
```

---

# 11. Reversing a Tuple

A tuple can be reversed using slicing.

```python
numbers = (10, 20, 30, 40)

print(numbers[::-1])

# Output:
# (40, 30, 20, 10)
```

`[::-1]` means:

```text
start → beginning
stop  → end
step  → -1
```

---

# 12. Tuple is Immutable

This is one of the most important characteristics of a tuple.

**Immutable** means that once the tuple is created, its elements cannot be changed.

Example:

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This produces:

```text
TypeError: 'tuple' object does not support item assignment
```

So this is invalid:

```python
numbers[0] = 100
```

---

# 13. What Does Immutable Mean?

Suppose:

```python
numbers = (10, 20, 30)
```

We cannot change:

```text
10 → 100
20 → 200
30 → 300
```

directly.

But we can create a **new tuple**.

```python
numbers = (10, 20, 30)

numbers = (100, 20, 30)

print(numbers)

# Output:
# (100, 20, 30)
```

Here we did not modify the original tuple.

We assigned a new tuple to the variable.

---

# 14. Tuple Does Not Have Methods Like append()

Because tuples are immutable, they do not have methods such as:

```python
append()
extend()
insert()
remove()
pop()
clear()
sort()
```

For example:

```python
numbers = (10, 20, 30)

numbers.append(40)
```

This gives:

```text
AttributeError: 'tuple' object has no attribute 'append'
```

---

# 15. Singleton Tuple

A tuple containing **one element** requires a comma.

Correct:

```python
data = (10,)

print(type(data))

# Output:
# <class 'tuple'>
```

Without the comma:

```python
data = (10,)

```

is a tuple.

But:

```python
data = (10)
```

is simply an integer.

```python
print(type((10)))
print(type((10,)))

# Output:
# <class 'int'>
# <class 'tuple'>
```

### Important rule

> **The comma creates the tuple, not the parentheses.**

---

# 16. One Element String Tuple

```python
data = ("Python",)

print(type(data))

# Output:
# <class 'tuple'>
```

Without the comma:

```python
data = ("Python")
```

This is a string, not a tuple.

---

# 17. Tuple Packing

Putting multiple values into a tuple is called **tuple packing**.

```python
student = "Teja", 21, "CSE"

print(student)

# Output:
# ('Teja', 21, 'CSE')
```

Parentheses are optional in many cases.

Python automatically packs the values into a tuple.

---

# 18. Tuple Unpacking

Unpacking means assigning tuple elements to separate variables.

```python
student = ("Teja", 21, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)

# Output:
# Teja
# 21
# CSE
```

Conceptually:

```text
("Teja", 21, "CSE")
      ↓
 name   age   branch
```

The number of variables should normally match the number of elements.

---

# 19. Unpacking with Different Number of Variables

This is invalid:

```python
data = (10, 20, 30)

a, b = data
```

Python raises:

```text
ValueError: too many values to unpack
```

Similarly:

```python
a, b, c, d = data
```

gives:

```text
ValueError: not enough values to unpack
```

---

# 20. Extended Unpacking

We can use `*` during unpacking.

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50
```

Notice that `middle` becomes a **list**.

---

# 21. Tuple Concatenation

Two tuples can be joined using `+`.

```python
a = (10, 20)
b = (30, 40)

result = a + b

print(result)

# Output:
# (10, 20, 30, 40)
```

The original tuples are not modified.

A new tuple is created.

---

# 22. Tuple Repetition

We can repeat a tuple using `*`.

```python
data = (1, 2)

print(data * 3)

# Output:
# (1, 2, 1, 2, 1, 2)
```

Again, a new tuple is created.

---

# 23. Membership Testing

Use `in` to check whether an element exists.

```python
numbers = (10, 20, 30)

print(20 in numbers)
print(50 in numbers)

# Output:
# True
# False
```

Use `not in`:

```python
print(50 not in numbers)

# Output:
# True
```

---

# 24. len()

`len()` returns the number of elements.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))

# Output:
# 4
```

---

# 25. count()

`count()` returns how many times a value occurs.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

# Output:
# 3
```

---

# 26. index()

`index()` returns the position of the first occurrence of a value.

```python
numbers = (10, 20, 30, 20)

print(numbers.index(20))

# Output:
# 1
```

It returns the first matching index.

If the value does not exist:

```python
numbers.index(50)
```

Python raises:

```text
ValueError: tuple.index(x): x not in tuple
```

---

# 27. Iterating Through a Tuple

We can use a `for` loop.

```python
languages = ("Python", "Java", "C")

for language in languages:
    print(language)

# Output:
# Python
# Java
# C
```

---

# 28. Using enumerate()

`enumerate()` gives both index and value.

```python
languages = ("Python", "Java", "C")

for index, language in enumerate(languages):
    print(index, language)

# Output:
# 0 Python
# 1 Java
# 2 C
```

---

# 29. Converting List to Tuple

Use `tuple()`.

```python
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
print(type(result))

# Output:
# (10, 20, 30)
# <class 'tuple'>
```

---

# 30. Converting Tuple to List

Use `list()`.

```python
numbers = (10, 20, 30)

result = list(numbers)

print(result)

# Output:
# [10, 20, 30]
```

This is useful when we need to modify the data.

For example:

```python
numbers = (10, 20, 30)

data = list(numbers)
data.append(40)

numbers = tuple(data)

print(numbers)

# Output:
# (10, 20, 30, 40)
```

---

# 31. Converting String to Tuple

A string is iterable, so `tuple()` creates a tuple of its characters.

```python
word = "Python"

result = tuple(word)

print(result)

# Output:
# ('P', 'y', 't', 'h', 'o', 'n')
```

---

# 32. Converting Set to Tuple

```python
data = {10, 20, 30}

result = tuple(data)

print(result)
```

The exact order should not be relied upon because sets are unordered.

---

# 33. Converting Range to Tuple

```python
numbers = tuple(range(1, 6))

print(numbers)

# Output:
# (1, 2, 3, 4, 5)
```

---

# 34. Nested Tuple

A tuple can contain another tuple.

```python
data = (
    (10, 20),
    (30, 40)
)

print(data)
```

Accessing nested elements:

```python
print(data[0][1])

# Output:
# 20
```

Conceptually:

```text
data
│
├── (10, 20)
│      └── 20
│
└── (30, 40)
```

---

# 35. Tuple Can Contain Different Objects

A tuple can contain:

```python
data = (
    10,
    "Python",
    [1, 2, 3],
    {"a": 1},
    {10, 20}
)
```

This is valid.

The tuple itself is immutable, but its elements can be mutable objects.

This leads to an important concept.

---

# 36. Immutable Tuple Can Contain Mutable Objects

Consider:

```python
data = (
    10,
    [20, 30]
)

data[1].append(40)

print(data)

# Output:
# (10, [20, 30, 40])
```

Did we change the tuple?

No.

The tuple still contains the same list object at position `1`.

We changed the **list**, not the tuple structure.

Think of it as:

```text
Tuple
│
├── 10
│
└── ──> List [20, 30]
              ↓
          append(40)
              ↓
          [20, 30, 40]
```

So:

> **Tuple immutability means tuple positions cannot be changed, but mutable objects stored inside it may still be modified.**

---

# 37. Tuple Hashability

A tuple can be **hashable**, but only if all its elements are hashable.

Example:

```python
data = (10, 20, "Python")

print(hash(data))
```

This works because all elements are hashable.

---

# 38. Tuple Can Be a Set Element

Because a tuple can be hashable, it can be used as a set element.

```python
data = {
    (10, 20),
    (30, 40)
}

print(data)
```

This is valid.

---

# 39. Tuple Can Be a Dictionary Key

A hashable tuple can be used as a dictionary key.

```python
data = {
    (10, 20): "Point A"
}

print(data[(10, 20)])

# Output:
# Point A
```

This is useful for representing coordinates.

---

# 40. When a Tuple Is NOT Hashable

A tuple containing an unhashable object is not hashable.

For example:

```python
data = (
    10,
    [20, 30]
)

print(hash(data))
```

This gives:

```text
TypeError: unhashable type: 'list'
```

Why?

```text
Tuple
│
├── 10       → hashable
└── [20,30]  → unhashable
```

Therefore the entire tuple is unhashable.

### Important rule

> **A tuple is hashable only when all of its elements are hashable.**

---

# 41. Tuple Equality

`==` checks whether two tuples contain equal values in the same order.

```python
a = (10, 20, 30)
b = (10, 20, 30)

print(a == b)

# Output:
# True
```

Order matters:

```python
a = (10, 20)
b = (20, 10)

print(a == b)

# Output:
# False
```

---

# 42. `==` vs `is`

`==` checks **value/content equality**.

`is` checks **object identity**.

Example:

```python
a = (10, 20)
b = (10, 20)

print(a == b)
print(a is b)
```

`==` tells us whether the contents are equal.

`is` tells us whether both variables refer to the same object.

Do not use `is` when you simply want to compare tuple values.

---

# 43. Tuple References

Consider:

```python
a = (10, 20, 30)
b = a
```

Now both variables refer to the same tuple object.

```text
a ──┐
    ├──> (10, 20, 30)
b ──┘
```

Since the tuple is immutable, neither variable can modify the tuple.

---

# 44. Tuple Truth Value

An empty tuple is `False`.

A non-empty tuple is `True`.

```python
print(bool(()))
print(bool((10,)))

# Output:
# False
# True
```

Example:

```python
data = ()

if data:
    print("Tuple is not empty")
else:
    print("Tuple is empty")

# Output:
# Tuple is empty
```

---

# 45. Useful Built-in Functions

Several built-in functions can be used with tuples.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(any(numbers))
print(all(numbers))

# Output:
# 4
# 10
# 40
# 100
# True
# True
```

---

# 46. `min()` and `max()`

```python
numbers = (30, 10, 50, 20)

print(min(numbers))
print(max(numbers))

# Output:
# 10
# 50
```

---

# 47. `sum()`

`sum()` adds numeric elements.

```python
numbers = (10, 20, 30)

print(sum(numbers))

# Output:
# 60
```

It should contain compatible numeric values.

---

# 48. `any()`

`any()` returns `True` if at least one element is truthy.

```python
data = (0, 0, 10)

print(any(data))

# Output:
# True
```

---

# 49. `all()`

`all()` returns `True` if every element is truthy.

```python
data = (10, 20, 30)

print(all(data))

# Output:
# True
```

But:

```python
data = (10, 0, 30)

print(all(data))

# Output:
# False
```

---

# 50. Tuple Comparison

Tuples can be compared.

Python compares elements from left to right.

```python
a = (10, 20)
b = (10, 30)

print(a < b)

# Output:
# True
```

Python first compares:

```text
10 == 10
```

Then compares:

```text
20 < 30
```

Therefore the result is `True`.

---

# 51. Returning Multiple Values from a Function

A very useful feature of tuples is returning multiple values.

```python
def calculate(a, b):
    return a + b, a - b

result = calculate(10, 5)

print(result)

# Output:
# (15, 5)
```

The function returns a tuple.

We can unpack it:

```python
addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)

# Output:
# 15
# 5
```

---

# 52. Tuple Comprehension Confusion

Python does **not** have a normal tuple comprehension.

This:

```python
data = (x * 2 for x in range(5))
```

creates a **generator expression**, not a tuple.

Check:

```python
print(type(data))

# Output:
# <class 'generator'>
```

To create a tuple:

```python
data = tuple(x * 2 for x in range(5))

print(data)

# Output:
# (0, 2, 4, 6, 8)
```

This is an important interview-level point.

---

# 53. Tuple Methods

Tuple has only two main methods:

```text
count()
index()
```

Why so few?

Because a tuple is immutable.

It does not need mutation methods such as:

```text
append()
remove()
insert()
pop()
clear()
sort()
```

---

# 54. Tuple vs List

This is one of the most important comparisons.

| Feature | Tuple | List |
|---|---|---|
| Syntax | `()` | `[]` |
| Mutable | ❌ | ✅ |
| Ordered | ✅ | ✅ |
| Indexed | ✅ | ✅ |
| Duplicates | ✅ | ✅ |
| Different types | ✅ | ✅ |
| `append()` | ❌ | ✅ |
| `remove()` | ❌ | ✅ |
| `sort()` | ❌ | ✅ |
| Hashable | Sometimes | ❌ |
| Can be dict key | Sometimes | ❌ |

Example:

```python
numbers = (10, 20, 30)   # tuple
numbers = [10, 20, 30]   # list
```

Use a tuple when the collection should not be structurally changed.

Use a list when you need frequent modifications.

---

# 55. Tuple vs Set

| Feature | Tuple | Set |
|---|---|---|
| Ordered | ✅ | No indexing/order reliance |
| Indexed | ✅ | ❌ |
| Mutable | ❌ | ✅ |
| Duplicates | ✅ | ❌ |
| Slicing | ✅ | ❌ |
| Hashable | Sometimes | ❌ |
| Main purpose | Fixed sequence | Unique elements |

Example:

```python
(10, 20, 10)
```

keeps duplicates.

```python
{10, 20, 10}
```

removes duplicates.

---

# 56. Tuple vs Dictionary

| Feature | Tuple | Dictionary |
|---|---|---|
| Stores | Values | Key-value pairs |
| Access | Index | Key |
| Mutable | ❌ | ✅ |
| Duplicate values | ✅ | ✅ |
| Duplicate keys | Not applicable | ❌ |
| Hashable | Sometimes | ❌ |

---

# 57. Memory and Performance

Tuples are generally more memory-efficient than lists when storing a fixed collection of values.

Example:

```python
numbers = (10, 20, 30, 40)
```

If the data does not need to change, a tuple can be a good choice.

However, the main reason to choose a tuple should be its **immutability and meaning as a fixed collection**, not simply performance.

---

# 58. Time Complexity

Common tuple operations:

| Operation | Average Complexity |
|---|---:|
| Index access | O(1) |
| Negative index access | O(1) |
| Length | O(1) |
| Membership search | O(n) |
| `count()` | O(n) |
| `index()` | O(n) |
| Slicing | O(k) |
| Concatenation | O(n + m) |

Index access is fast because tuples store elements in an ordered sequence.

Searching requires checking elements, so it is generally O(n).

---

# 59. Common Tuple Mistakes

### Mistake 1: Forgetting the comma for one element

Wrong:

```python
data = (10)
```

This is an integer.

Correct:

```python
data = (10,)
```

---

### Mistake 2: Trying to modify a tuple

Wrong:

```python
data = (10, 20, 30)

data[0] = 100
```

Tuples are immutable.

---

### Mistake 3: Expecting append()

Wrong:

```python
data.append(40)
```

Tuple does not have `append()`.

---

### Mistake 4: Assuming every tuple is hashable

This is not always true:

```python
data = (10, [20, 30])
```

The tuple contains a list, so the tuple is not hashable.

---

### Mistake 5: Confusing parentheses with tuple creation

Remember:

```python
(10)
```

is an integer.

But:

```python
(10,)
```

is a tuple.

The comma is important.

---

# 60. Practical Example: Coordinates

Tuples are useful for fixed data such as coordinates.

```python
point = (10, 20)

x, y = point

print(x)
print(y)

# Output:
# 10
# 20
```

The coordinates are naturally represented as a fixed pair.

---

# 61. Practical Example: Student Details

```python
student = ("Teja", 21, "CSE")

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# Output:
# Name: Teja
# Age: 21
# Branch: CSE
```

---

# 62. Practical Example: RGB Values

A color can be represented as a tuple.

```python
red = (255, 0, 0)

print(red)

# Output:
# (255, 0, 0)
```

The three values represent:

```text
Red   → 255
Green → 0
Blue  → 0
```

---

# 63. Practical Example: Swapping Values

Python allows easy swapping using tuple unpacking.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Output:
# 20
# 10
```

Conceptually, Python uses tuple packing and unpacking.

---

# 64. Important Mental Model

Think of a tuple as:

> **A fixed, ordered collection of values.**

Example:

```python
student = ("Teja", 21, "CSE")
```

You can:

```text
Access        ✅
Index         ✅
Slice         ✅
Iterate       ✅
Count         ✅
Search        ✅
Unpack        ✅
```

You cannot:

```text
Change element    ❌
Append             ❌
Remove             ❌
Insert             ❌
Sort in place      ❌
```

---

# 65. Quick Revision

```text
Tuple
│
├── Ordered
├── Immutable
├── Indexed
├── Allows duplicates
├── Allows different data types
├── Supports positive indexing
├── Supports negative indexing
├── Supports slicing
├── Iterable
├── Supports packing/unpacking
├── Supports count() and index()
├── Can contain mutable objects
└── Hashable only when all elements are hashable
```

Important syntax:

```python
data = (10, 20, 30)
```

One-element tuple:

```python
data = (10,)
```

Access:

```python
data[0]
```

Slice:

```python
data[1:3]
```

Unpacking:

```python
a, b, c = data
```

Membership:

```python
20 in data
```

Length:

```python
len(data)
```

---

# 66. One-Line Definition

> **A tuple is an ordered and immutable collection of values that supports indexing, slicing, duplicate elements, and different data types.**