# Shallow Copy and Deep Copy in Python — Complete Guide

This guide explains copying in Python from basic to advanced concepts, including object references, mutable and immutable objects, shallow copy, deep copy, nested lists, dictionaries, memory behavior, and practical examples.

# 1. What Is Copying in Python?

Copying means creating another object or another reference to an existing object.

Consider this example:

```python
numbers = [10, 20, 30]

another = numbers

print(numbers)
print(another)
```

Output:

```text
[10, 20, 30]
[10, 20, 30]
```

Both variables display the same values. But are they referring to two different lists?

Let's check:

```python
numbers = [10, 20, 30]

another = numbers

print(numbers is another)
```

Output:

```text
True
```

Both variables refer to the **same list object**.

This is assignment, not copying.

# 2. Assignment Is Not Copying

Consider:

```python
original = [10, 20, 30]

copied = original

copied.append(40)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: [10, 20, 30, 40]
Copied: [10, 20, 30, 40]
```

Why did the original list change?

Because this statement:

```python
copied = original
```

does not create a new list. It makes `copied` refer to the same list as `original`.

When we modify the list through either variable, we observe that modification through both variables.

Think of it like two labels attached to one object.

```text
original ─────┐
              ├────> [10, 20, 30, 40]
copied ───────┘
```

**Remember:** Assignment creates a new reference to an object; it does not automatically copy the object.

# 3. Checking Object Identity with `is`

The `is` operator checks whether two references point to the same object.

```python
a = [1, 2, 3]
b = a

print(a is b)
print(a == b)
```

Output:

```text
True
True
```

Both are true because the references point to the same list, and their contents are equal.

Now consider two independently created lists:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)
```

Output:

```text
False
True
```

Explanation:

- `a is b` checks object identity.
- `a == b` checks value equality.

The lists have equal contents but are separate objects.

Use `==` when comparing values. Use `is` when checking object identity.

# 4. Mutable and Immutable Objects

Before learning copying, understand mutable and immutable objects.

## Mutable objects

A mutable object can be modified after it is created.

Examples include:

- Lists
- Dictionaries
- Sets
- Most user-defined objects

Example:

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

The list was modified.

## Immutable objects

An immutable object cannot be modified in place.

Common examples include:

- Integers
- Floats
- Booleans
- Strings
- Tuples whose elements are all immutable
- Frozen sets

Example:

```python
number = 10
number = number + 5

print(number)
```

Output:

```text
15
```

The integer object `10` was not changed into `15`. The expression produces the integer value `15`, and the variable `number` is rebound to that value.

This distinction matters because shallow and deep copies mainly become interesting when objects contain mutable objects.

# 5. What Is a Shallow Copy?

A **shallow copy** creates a new outer object but does not recursively copy the objects stored inside it.

For a list containing other lists, a shallow copy creates a new outer list while keeping references to the same inner lists.

Example:

```python
import copy

original = [10, 20, 30]

copied = copy.copy(original)

print(original)
print(copied)

print(original is copied)
print(original == copied)
```

Output:

```text
[10, 20, 30]
[10, 20, 30]
False
True
```

The two lists have equal values, but they are different outer list objects.

```text
original ─────> [10, 20, 30]
copied ────────> [10, 20, 30]
```

The arrows point to different lists.

# 6. Modifying a Shallow-Copied List

Consider:

```python
import copy

original = [10, 20, 30]

copied = copy.copy(original)

copied.append(40)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: [10, 20, 30]
Copied: [10, 20, 30, 40]
```

Why did the original not change?

Because `copy.copy()` created a new outer list.

Appending `40` modifies only the copied outer list.

This is an important difference between assignment and shallow copying.

# 7. Shallow Copy with Nested Lists

Now consider a nested list:

```python
import copy

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

print(original is copied)
print(original[0] is copied[0])
```

Output:

```text
False
True
```

This is the key concept.

- `original` and `copied` are different outer lists.
- `original[0]` and `copied[0]` refer to the same inner list.

Memory structure:

```text
original ─────> Outer List A ─────┐
                                  ├──> Inner List [1, 2]
copied ────────> Outer List B ─────┘

original[1] ──────────────────────┐
                                  ├──> Inner List [3, 4]
copied[1] ────────────────────────┘
```

The outer list is copied. The inner lists are shared.

# 8. The Most Important Shallow Copy Example

```python
import copy

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

copied[0].append(100)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: [[1, 2, 100], [3, 4]]
Copied: [[1, 2, 100], [3, 4]]
```

Why did both change?

Because `original[0]` and `copied[0]` refer to the same inner list.

The statement:

```python
copied[0].append(100)
```

modifies that shared inner list.

However, adding a new element to the copied outer list affects only the copy:

```python
import copy

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

copied.append([5, 6])

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: [[1, 2], [3, 4]]
Copied: [[1, 2], [3, 4], [5, 6]]
```

The new inner list is added only to the copied outer list.

# 9. Three Common Ways to Make a Shallow Copy of a List

For ordinary lists, these methods produce a shallow copy.

## Method 1: `copy.copy()`

```python
import copy

original = [1, 2, 3]
copied = copy.copy(original)

print(copied)
print(original is copied)
```

Output:

```text
[1, 2, 3]
False
```

## Method 2: List slicing

```python
original = [1, 2, 3]
copied = original[:]

print(copied)
print(original is copied)
```

Output:

```text
[1, 2, 3]
False
```

## Method 3: `list()`

```python
original = [1, 2, 3]
copied = list(original)

print(copied)
print(original is copied)
```

Output:

```text
[1, 2, 3]
False
```

All three create a new outer list. None recursively copies nested mutable objects.

For nested data, all three have the same important shallow-copy behavior.

# 10. What Is a Deep Copy?

A **deep copy** recursively copies an object and the objects it contains, as needed, instead of sharing the nested mutable objects in the same way as a shallow copy.

Python provides `copy.deepcopy()`.

Example:

```python
import copy

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

print(original is copied)
print(original[0] is copied[0])
```

Output:

```text
False
False
```

Now:

- The outer lists are different objects.
- The first inner lists are different objects.
- The second inner lists are also different objects.

Memory structure:

```text
original ───> Outer List A
               ├──> Inner List [1, 2]
               └──> Inner List [3, 4]

copied ─────> Outer List B
               ├──> Inner List [1, 2]
               └──> Inner List [3, 4]
```

The diagram represents separate lists containing equal values.

# 11. Modifying a Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

copied[0].append(100)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: [[1, 2], [3, 4]]
Copied: [[1, 2, 100], [3, 4]]
```

The original remains unchanged because the copied inner list is a separate object.

This is the primary reason to use a deep copy when you need independent nested mutable data.

# 12. Shallow Copy vs Deep Copy

| Feature | Shallow copy | Deep copy |
|---|---|---|
| Creates a new outer object | Yes | Yes |
| Copies nested objects recursively | No | Generally, yes |
| Shares nested mutable objects | Usually yes | Usually no |
| Memory usage | Often lower | Can be higher |
| Copying cost | Often lower | Often higher |
| Main function | `copy.copy()` | `copy.deepcopy()` |

Example:

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print(original is shallow)
print(original[0] is shallow[0])

print(original is deep)
print(original[0] is deep[0])
```

Output:

```text
False
True
False
False
```

This example shows the difference between the two copying strategies.

# 13. Copying Dictionaries

The same concepts apply to dictionaries.

## Shallow copy

```python
import copy

original = {
    "name": "Teja",
    "marks": [80, 90, 95]
}

copied = copy.copy(original)

print(original is copied)
print(original["marks"] is copied["marks"])
```

Output:

```text
False
True
```

The outer dictionaries are different, but their `"marks"` values point to the same list.

Modify that list:

```python
import copy

original = {
    "name": "Teja",
    "marks": [80, 90, 95]
}

copied = copy.copy(original)

copied["marks"].append(100)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: {'name': 'Teja', 'marks': [80, 90, 95, 100]}
Copied: {'name': 'Teja', 'marks': [80, 90, 95, 100]}
```

Both dictionaries show the new mark because the list is shared.

## Deep copy

```python
import copy

original = {
    "name": "Teja",
    "marks": [80, 90, 95]
}

copied = copy.deepcopy(original)

copied["marks"].append(100)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: {'name': 'Teja', 'marks': [80, 90, 95]}
Copied: {'name': 'Teja', 'marks': [80, 90, 95, 100]}
```

The copied dictionary contains its own copied marks list.

# 14. Shallow Copy with a List of Dictionaries

Consider student records:

```python
import copy

students = [
    {"name": "Teja", "marks": 90},
    {"name": "Ravi", "marks": 85}
]

copied = copy.copy(students)

copied[0]["marks"] = 100

print("Original:", students)
print("Copied:", copied)
```

Output:

```text
Original: [{'name': 'Teja', 'marks': 100}, {'name': 'Ravi', 'marks': 85}]
Copied: [{'name': 'Teja', 'marks': 100}, {'name': 'Ravi', 'marks': 85}]
```

Why did the original change?

Because the dictionaries inside the list are shared.

Now use deep copy:

```python
import copy

students = [
    {"name": "Teja", "marks": 90},
    {"name": "Ravi", "marks": 85}
]

copied = copy.deepcopy(students)

copied[0]["marks"] = 100

print("Original:", students)
print("Copied:", copied)
```

Output:

```text
Original: [{'name': 'Teja', 'marks': 90}, {'name': 'Ravi', 'marks': 85}]
Copied: [{'name': 'Teja', 'marks': 100}, {'name': 'Ravi', 'marks': 85}]
```

The copied student dictionaries are separate objects.

# 15. Copying a Tuple

Tuples are immutable containers, but they can contain mutable objects.

Consider:

```python
import copy

original = ([1, 2], [3, 4])

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print(original is shallow)
print(original[0] is shallow[0])

print(original is deep)
print(original[0] is deep[0])
```

For this tuple containing lists, typical output is:

```text
True
True
False
False
```

Why is the shallow copy the same tuple object?

Python may return the original object when copying certain immutable objects, including this tuple, because creating a separate tuple would not provide a useful independent outer container.

The deep copy creates a new tuple because it needs to copy the mutable lists inside it.

**Important:** A tuple cannot have its element references reassigned, but a list stored inside a tuple can still be modified.

Example:

```python
values = ([1, 2], [3, 4])

values[0].append(100)

print(values)
```

Output:

```text
([1, 2, 100], [3, 4])
```

The tuple structure stays the same, but the nested list changes.

# 16. Copying Objects with Shared References

Deep copy does not necessarily create a separate copy for every occurrence of a reference.

It uses a memoization mechanism to preserve relationships between objects.

Example:

```python
import copy

shared = [10, 20]

original = [shared, shared]

copied = copy.deepcopy(original)

print(original[0] is original[1])
print(copied[0] is copied[1])
print(original[0] is copied[0])
```

Output:

```text
True
True
False
```

Explanation:

- Both entries in the original refer to the same inner list.
- Both entries in the deep copy refer to the same copied inner list.
- The copied inner list is separate from the original inner list.

Deep copy preserves the internal sharing relationship while separating the copied structure from the original.

# 17. Circular References

An object can contain a reference to itself, directly or indirectly.

Example:

```python
import copy

original = []
original.append(original)

copied = copy.deepcopy(original)

print(original is original[0])
print(copied is copied[0])
print(original is copied)
```

Output:

```text
True
True
False
```

The original list contains a reference to itself.

The deep copy creates a separate list whose element refers to the copied list itself.

Python's deep-copy implementation uses a memo dictionary to handle repeated references and circular structures.

# 18. Copying Custom Objects

The `copy` module also supports many user-defined objects.

```python
import copy


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


original = Student("Teja", [80, 90, 95])

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print(original is shallow)
print(original.marks is shallow.marks)

print(original is deep)
print(original.marks is deep.marks)
```

Output:

```text
False
True
False
False
```

The shallow copy has a separate `Student` instance but shares its `marks` list.

The deep copy has a separate instance and a copied marks list.

## Modifying the copied object

```python
import copy


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


original = Student("Teja", [80, 90, 95])

shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow.marks.append(100)
deep.marks.append(75)

print("Original marks:", original.marks)
print("Shallow marks:", shallow.marks)
print("Deep marks:", deep.marks)
```

Output:

```text
Original marks: [80, 90, 95, 100]
Shallow marks: [80, 90, 95, 100]
Deep marks: [80, 90, 95, 75]
```

The shallow copy shares the list, while the deep copy has its own list.

# 19. Copying and the `id()` Function

The `id()` function returns an integer identifying an object's identity during its lifetime.

We can use it to compare objects while they are alive.

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("Original outer ID:", id(original))
print("Shallow outer ID:", id(shallow))
print("Deep outer ID:", id(deep))

print("Original inner ID:", id(original[0]))
print("Shallow inner ID:", id(shallow[0]))
print("Deep inner ID:", id(deep[0]))
```

The actual numbers vary between executions.

The important relationships are:

```python
original is shallow
# False

original[0] is shallow[0]
# True

original is deep
# False

original[0] is deep[0]
# False
```

Use identity comparisons to understand object relationships rather than expecting specific `id()` values.

# 20. Copying Is Different from Rebinding

Consider:

```python
original = [1, 2, 3]

copied = original.copy()

copied = [100, 200]

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: [1, 2, 3]
Copied: [100, 200]
```

The statement:

```python
copied = [100, 200]
```

rebinds `copied` to a different list.

It does not modify the original list or the previous copied list.

This is different from mutating a shared nested object.

# 21. Common Mistakes

## Mistake 1: Assuming assignment copies a list

Incorrect assumption:

```python
original = [1, 2, 3]
copied = original
```

This does not create an independent list.

Correct:

```python
copied = original.copy()
```

This makes a shallow copy.

## Mistake 2: Assuming `.copy()` creates a deep copy

```python
original = [[1, 2], [3, 4]]
copied = original.copy()
```

The inner lists are still shared.

Use:

```python
import copy

copied = copy.deepcopy(original)
```

when independent nested objects are needed.

## Mistake 3: Using deep copy for everything

Deep copy can take additional time and memory. It can also be inappropriate for resources such as open files, sockets, locks, or other objects that cannot be meaningfully duplicated.

Use it only when the desired copying behavior calls for it.

## Mistake 4: Assuming every object is copied in the same way

Custom classes can define their own copying behavior through special methods such as `__copy__()` and `__deepcopy__()`.

Some objects cannot be copied normally, and some have special semantics.

## Mistake 5: Confusing equality with identity

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

Equal contents do not imply identical objects.

# 22. When Should You Use Shallow Copy?

Use shallow copy when:

- You need a new outer list or dictionary.
- The nested objects can safely remain shared.
- You want to add or remove outer elements independently.
- Copying all nested objects would be unnecessary.

Example:

```python
original = [10, 20, 30]
copied = original.copy()

copied.append(40)

print(original)
print(copied)
```

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```

# 23. When Should You Use Deep Copy?

Use deep copy when:

- You need an independent nested data structure.
- You will modify nested lists or dictionaries without affecting the original.
- You need a separate copy of a complex object graph, and its objects support the intended copy behavior.

Example:

```python
import copy

original = {
    "student": {
        "name": "Teja",
        "marks": [80, 90]
    }
}

copied = copy.deepcopy(original)

copied["student"]["marks"].append(100)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: {'student': {'name': 'Teja', 'marks': [80, 90]}}
Copied: {'student': {'name': 'Teja', 'marks': [80, 90, 100]}}
```

# 24. Practice Questions

### Basic

1. Assign a list to another variable and observe what happens when you append an element.
2. Compare two equal lists using `is` and `==`.
3. Make a shallow copy using `copy.copy()`.
4. Make a shallow copy using list slicing.
5. Make a shallow copy using the list `.copy()` method.

### Intermediate

6. Make a shallow copy of a nested list and modify an inner element.
7. Deep-copy a nested list and modify an inner element.
8. Compare shallow and deep copying of a dictionary containing a list.
9. Copy a list of dictionaries and update one dictionary.
10. Copy a tuple containing mutable lists.
11. Use `id()` to compare outer and inner objects.
12. Demonstrate the difference between mutating a list and rebinding a variable.

### Advanced

13. Deep-copy a structure containing the same inner object more than once.
14. Deep-copy a circular list.
15. Copy a custom `Student` object containing a mutable list.
16. Implement `__copy__()` in a custom class.
17. Explore `__deepcopy__()` and its memo dictionary.
18. Compare the cost of shallow and deep copying a large nested structure.
19. Explain why open files and other external resources should not be blindly deep-copied.
20. Decide whether shallow copy or deep copy is appropriate for a nested student-record structure.

# 25. Quick Revision

| Operation | Result |
|---|---|
| `b = a` | Creates another reference to the same object |
| `copy.copy(a)` | Creates a shallow copy |
| `a.copy()` | Creates a shallow copy for supported built-in containers such as lists and dictionaries |
| `a[:]` | Creates a shallow copy of a list |
| `copy.deepcopy(a)` | Recursively copies supported nested objects |
| `a == b` | Checks value equality |
| `a is b` | Checks object identity |
| `id(a)` | Returns an identity value for the object's lifetime |

## Final takeaway

**Shallow copy:** A new outer object, with nested objects generally shared.

**Deep copy:** A separate copied object structure, recursively copying supported nested objects while preserving internal reference relationships.

Always choose the copying method according to whether the nested objects should remain shared or become independent.
