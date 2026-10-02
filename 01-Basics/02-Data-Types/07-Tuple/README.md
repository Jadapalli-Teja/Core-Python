# Python Tuples

A tuple is an ordered, immutable collection used to store multiple values in a single object.

Tuples are created mainly using parentheses `()` or the `tuple()` constructor.

---

## 1. What is a Tuple?

A tuple can store multiple elements.

```python
numbers = (10, 20, 30, 40)

print(numbers)

Output:

(10, 20, 30, 40)

Here:

numbers → variable
(10, 20, 30, 40) → tuple object
10, 20, 30, 40 → elements

The main property of a tuple is that it is immutable.

2. Creating a Tuple

A tuple can be created using parentheses ().

numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))

Output:

(10, 20, 30, 40)
<class 'tuple'>
3. Empty Tuple

An empty tuple contains no elements.

t = ()

print(t)
print(type(t))

Output:

()
<class 'tuple'>
4. Single-Element Tuple

A single-element tuple must contain a comma.

t = (10,)

print(t)
print(type(t))

Output:

(10,)
<class 'tuple'>

The comma is important.

(10)     # int
(10,)    # tuple
print(type((10)))
print(type((10,)))

Output:

<class 'int'>
<class 'tuple'>
5. Tuple Without Parentheses

Parentheses are not always required.

numbers = 10, 20, 30

print(numbers)
print(type(numbers))

Output:

(10, 20, 30)
<class 'tuple'>

The commas are what make this a tuple.

6. Using tuple()

Python provides the tuple() constructor.

numbers = tuple()

print(numbers)
print(type(numbers))

Output:

()
<class 'tuple'>

tuple() creates an empty tuple when no argument is provided.

7. Converting a List to a Tuple

A list can be converted into a tuple.

numbers = [10, 20, 30]

t = tuple(numbers)

print(t)
print(type(t))

Output:

(10, 20, 30)
<class 'tuple'>
8. Converting a String to a Tuple

A string is an iterable, so tuple() takes its characters one by one.

text = "Python"

t = tuple(text)

print(t)

Output:

('P', 'y', 't', 'h', 'o', 'n')
9. Converting a Set to a Tuple

A set can be converted into a tuple.

numbers = {10, 20, 30}

t = tuple(numbers)

print(t)

The tuple contains the elements of the set.

The order should not be relied upon because sets are unordered collections.

10. Converting a Dictionary to a Tuple

When a dictionary is passed to tuple(), its keys are converted.

student = {
    "name": "Teja",
    "age": 21
}

t = tuple(student)

print(t)

Output:

('name', 'age')
11. Dictionary Values to Tuple

Use values() to convert dictionary values.

student = {
    "name": "Teja",
    "age": 21
}

t = tuple(student.values())

print(t)

Output:

('Teja', 21)
12. Dictionary Items to Tuple

Use items() to get key-value pairs.

student = {
    "name": "Teja",
    "age": 21
}

t = tuple(student.items())

print(t)

Output:

(('name', 'Teja'), ('age', 21))

Here the tuple contains smaller tuples.

13. Tuple From range()
numbers = tuple(range(1, 6))

print(numbers)

Output:

(1, 2, 3, 4, 5)
14. Tuple Can Store Different Data Types

A tuple can contain different types of objects.

data = (10, 3.14, "Python", True)

print(data)

Output:

(10, 3.14, 'Python', True)

A tuple can contain:

integers
floats
strings
booleans
lists
dictionaries
sets
other tuples
objects
15. Duplicate Elements

Tuples allow duplicate values.

numbers = (10, 20, 10, 30, 20)

print(numbers)

Output:

(10, 20, 10, 30, 20)
16. Tuple is Ordered

A tuple maintains the order in which elements are stored.

languages = ("Python", "Java", "C")

print(languages)

Output:

('Python', 'Java', 'C')

The positions are:

Python → index 0
Java   → index 1
C      → index 2
17. Tuple Indexing

Tuple indexing starts from 0.

languages = ("Python", "Java", "C", "SQL")

print(languages[0])
print(languages[1])
print(languages[2])

Output:

Python
Java
C
18. Negative Indexing

Negative indexing starts from the end.

languages = ("Python", "Java", "C", "SQL")

print(languages[-1])
print(languages[-2])
print(languages[-3])

Output:

SQL
C
Java
19. Tuple Slicing

Tuple slicing is similar to list slicing.

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

Output:

(20, 30, 40)

The stop index is excluded.

20. Tuple Slicing With Step
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[::2])

Output:

(10, 30, 50)
21. Reverse a Tuple Using Slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])

Output:

(50, 40, 30, 20, 10)
22. Tuple is Immutable

The most important property of a tuple is immutability.

Once a tuple is created, its elements cannot be changed.

numbers = (10, 20, 30)

numbers[0] = 100

This produces:

TypeError

You cannot directly replace a tuple element.

23. Tuple Does Not Support append()

Tuples do not have append() because they cannot be modified.

numbers = (10, 20, 30)

numbers.append(40)

This produces:

AttributeError

Tuple does not have methods such as:

append()
insert()
remove()
pop()
clear()
sort()
reverse()
24. Deleting Tuple Elements

Individual tuple elements cannot be deleted.

numbers = (10, 20, 30)

del numbers[0]

This produces an error.

However, the entire variable can be deleted.

numbers = (10, 20, 30)

del numbers

Here del removes the variable reference.

25. Mutable Objects Inside a Tuple

A tuple can contain mutable objects.

For example, a list can be stored inside a tuple.

data = ([10, 20], 30)

data[0].append(40)

print(data)

Output:

([10, 20, 40], 30)

The tuple itself was not changed.

The list object inside the tuple was changed.

This means:

Tuple immutability is not recursive.

26. Nested Tuples

A tuple can contain another tuple.

numbers = (
    (10, 20),
    (30, 40)
)

print(numbers)

Output:

((10, 20), (30, 40))

Access nested elements:

print(numbers[0])
print(numbers[0][1])

Output:

(10, 20)
20
27. len() With Tuple

len() returns the number of elements.

numbers = (10, 20, 30, 40)

print(len(numbers))

Output:

4

Time complexity:

O(1)
28. Membership Operators

Use in and not in to check membership.

numbers = (10, 20, 30)

print(20 in numbers)
print(50 in numbers)

Output:

True
False
print(50 not in numbers)

Output:

True

Membership checking takes:

O(n)

in the general case.

29. Tuple Concatenation

The + operator combines tuples.

a = (10, 20)
b = (30, 40)

result = a + b

print(result)

Output:

(10, 20, 30, 40)

A new tuple is created.

The original tuples are not changed.

30. Tuple Repetition

The * operator repeats a tuple.

numbers = (10, 20)

result = numbers * 3

print(result)

Output:

(10, 20, 10, 20, 10, 20)
31. count() Method

count() returns how many times a value occurs.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

Output:

3

Time complexity:

O(n)
32. index() Method

index() returns the index of the first occurrence.

numbers = (10, 20, 30, 20)

print(numbers.index(20))

Output:

1

If the value does not exist, Python raises ValueError.

Time complexity:

O(n)
33. Iterating Through a Tuple

A tuple can be used directly in a for loop.

numbers = (10, 20, 30)

for number in numbers:
    print(number)

Output:

10
20
30
34. enumerate() With Tuple

enumerate() provides both the index and value.

languages = ("Python", "Java", "C")

for index, language in enumerate(languages):
    print(index, language)

Output:

0 Python
1 Java
2 C
35. Tuple Packing

Packing means putting multiple values into one tuple.

student = "Teja", 21, 8.43

print(student)

Output:

('Teja', 21, 8.43)

Parentheses are optional here.

36. Tuple Unpacking

Unpacking means assigning tuple elements to separate variables.

student = ("Teja", 21, 8.43)

name, age, cgpa = student

print(name)
print(age)
print(cgpa)

Output:

Teja
21
8.43

The number of variables normally needs to match the number of elements.

37. Extended Unpacking

The * operator can collect multiple elements.

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

Output:

10
[20, 30, 40]
50

Important:

middle is a list, not a tuple.

38. Swapping Values Using Tuple Unpacking

Python can swap values without using a temporary variable.

a = 10
b = 20

a, b = b, a

print(a)
print(b)

Output:

20
10
39. Returning Multiple Values From a Function

A function can return multiple values.

def calculate():
    return 10, 20

result = calculate()

print(result)

Output:

(10, 20)

Python packs the returned values into a tuple.

They can also be unpacked:

a, b = calculate()

print(a)
print(b)

Output:

10
20
40. Tuple Comparison

Tuples can be compared using ==.

a = (10, 20, 30)
b = (10, 20, 30)

print(a == b)

Output:

True

Order matters.

print((10, 20) == (20, 10))

Output:

False
41. == vs is

== checks values.

is checks object identity.

a = (10, 20)
b = (10, 20)

print(a == b)
print(a is b)

The important difference is:

==  → Are the values equal?
is  → Are they the same object?

Use == when comparing tuple values.

42. Tuple References

Two variables can refer to the same tuple object.

a = (10, 20, 30)
b = a

print(a is b)

Output:

True

Both variables refer to the same tuple object.

43. Tuple Copying

Tuples do not have a copy() method.

numbers = (10, 20, 30)

print(numbers.copy())

This produces:

AttributeError

For an existing tuple:

numbers = (10, 20, 30)

new_numbers = tuple(numbers)

print(new_numbers)

Output:

(10, 20, 30)
44. Tuple Hashability

A tuple can be hashable if all of its elements are hashable.

numbers = (10, 20, 30)

print(hash(numbers))

This works because integers are hashable.

A hashable tuple can be used as a dictionary key.

points = {
    (10, 20): "Point A"
}

print(points[(10, 20)])

Output:

Point A
45. Tuple Containing a List

A tuple containing a list is not hashable.

data = ([10, 20], 30)

print(hash(data))

This produces:

TypeError

The reason is that lists are mutable and therefore unhashable.

46. Tuple as a Set Element

A hashable tuple can be stored inside a set.

points = {
    (10, 20),
    (30, 40)
}

print(points)

This works because the tuples contain only hashable integers.

47. sorted() With Tuple

sorted() can sort a tuple.

However, sorted() returns a list.

numbers = (30, 10, 20)

result = sorted(numbers)

print(result)
print(type(result))

Output:

[10, 20, 30]
<class 'list'>

To get a tuple:

result = tuple(sorted(numbers))

print(result)

Output:

(10, 20, 30)
48. min(), max() and sum()

These functions can be used with numeric tuples.

numbers = (10, 20, 30, 40)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

Output:

10
40
100

Time complexity:

min() → O(n)
max() → O(n)
sum() → O(n)
49. any() and all()

any() returns True when at least one value is truthy.

values = (False, False, True)

print(any(values))

Output:

True

all() returns True when every value is truthy.

values = (True, True, True)

print(all(values))

Output:

True
50. Boolean Value of a Tuple

An empty tuple is False.

t = ()

print(bool(t))

Output:

False

A non-empty tuple is True.

t = (0,)

print(bool(t))

Output:

True

The tuple is non-empty even though its element 0 is falsey.

51. Reassignment vs Modification

A tuple cannot be modified, but the variable can be reassigned.

numbers = (10, 20, 30)

numbers = (100, 200, 300)

print(numbers)

Output:

(100, 200, 300)

The original tuple was not modified.

The variable was simply made to refer to another tuple.

52. Tuple vs List
Feature	Tuple	List
Syntax	()	[]
Ordered	Yes	Yes
Mutable	No	Yes
Duplicates	Yes	Yes
Indexing	Yes	Yes
Slicing	Yes	Yes
append()	No	Yes
remove()	No	Yes
sort()	No	Yes
count()	Yes	Yes
index()	Yes	Yes
Dictionary key	Yes, if hashable	No
Set element	Yes, if hashable	No
53. Tuple Time Complexity

For a tuple containing n elements:

Operation	Time Complexity
Indexing t[i]	O(1)
Negative indexing	O(1)
len(t)	O(1)
Membership x in t	O(n)
count()	O(n)
index()	O(n)
Iteration	O(n)
Slicing	O(k)
min()	O(n)
max()	O(n)
sum()	O(n)
Concatenation	O(n + m)
Repetition	O(n × k)
sorted()	O(n log n)

Here:

n → size of first tuple
m → size of second tuple
k → number of elements produced by slicing/repetition
54. Important Properties of Tuple

A tuple is:

Ordered
Immutable
Indexed
Sliceable
Iterable
Allows duplicate values
Allows different data types
Supports nested objects
Supports in and not in
Supports + and *
Has count() and index()
Supports packing and unpacking
Can be used as a dictionary key when hashable
Can be stored inside a set when hashable
Does not support modification methods such as append() and remove()
55. Quick Revision
Tuple
   ↓
Ordered collection
   ↓
Immutable
   ↓
Created using ()
   ↓
Can also be created using tuple()
   ↓
Allows duplicates
   ↓
Allows different data types
   ↓
Supports indexing
   ↓
Supports slicing
   ↓
Supports concatenation
   ↓
Supports repetition
   ↓
Supports packing and unpacking
   ↓
Supports count() and index()
   ↓
Can contain mutable objects
   ↓
Can be used as a dictionary key if hashable
Important Examples
()                  # Empty tuple

(10,)               # Single-element tuple

(10, 20, 30)        # Normal tuple

10, 20, 30          # Tuple packing

tuple()             # Empty tuple

tuple([10, 20])     # List → Tuple

tuple("Python")     # String → Tuple

tuple(range(5))     # Range → Tuple
Most Important Point

A tuple is immutable, which means the tuple's elements cannot be replaced, added, or removed after creation.

However, a tuple can contain mutable objects such as lists, and those objects themselves can still be modified.


### The important difference from your current file

Your Tuple README should now render like your **List README screenshot**:

```text
# Python Tuples
────────────────────────────

A tuple is an ordered...

## 1. What is a Tuple?

A tuple can store...

┌──────────────────────────┐
│ numbers = (10, 20, 30)   │
│                          │
│ print(numbers)           │
└──────────────────────────┘

So don't type the code fences incorrectly. Every Python example must start and end with:

```python
your code here
```

and output should use:

```text
output here
```